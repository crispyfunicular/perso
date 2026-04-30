#!/usr/bin/env python3
"""
Build the course submission bundle under rendu_TTS/:
- pick 5 demonstration sentences (NOT from phrases.txt poem lines)
- extract MFA phone sequences from aligned_one TextGrids for those sentences
- concatenate phone clips (+ light crossfade + WORLD re-synthesis)
- write paired .wav + .TextGrid into rendu_TTS/
- copy the course notebook (without editing the original file in-repo)
- generate REPORT_TTS.pdf from REPORT_TTS.md via pandoc

Run with the MFA python (has numpy/soundfile/pyworld after setup):
  /home/morgane/miniconda3/envs/mfa/bin/python rendu_TTS/build_rendu_outputs.py
"""

from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List, Sequence, Tuple

# Make repo root importable
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from projet_tts import (  # noqa: E402
    PhoneIndex,
    build_index_from_project,
    crossfade_concatenate,
    extract_segment,
    is_real_phone,
    linear_fade_edges,
    normalize_rms,
    read_textgrid_tier,
    read_wav_mono,
    world_resynth,
    write_simple_textgrid_words_phones,
)
import numpy as np
import soundfile as sf


POEM_LINES = {
    "celui qui croyait au ciel, celui qui n'y croyait pas.",
    "tous deux adoraient la belle, prisonnière des soldats.",
    "lequel montait à l'échelle et lequel guettait en bas",
    "quand les blés sont sous la grelle, fou qui fait le délicat.",
    "fou qui songe à ses querelles au coeur du commun combat.",
    "l'alouette et l'hirondelle, la rose et le réséda.",
}


def norm_text(s: str) -> str:
    s = s.strip().lower()
    s = s.replace("’", "'")
    s = re.sub(r"[^a-z0-9àâäéèêëïîôùûçœæ' -]+", "", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def french_tokens(sentence: str) -> List[str]:
    """
    Tokenize a French sentence into MFA-like word tokens.

    Main goal: split leading clitics like "l'herbe" -> ["l'", "herbe"] to match MFA word tiers.
    """
    s = sentence.strip()
    if s.endswith("."):
        s = s[:-1].strip()

    raw_tokens = [t for t in re.split(r"\s+", s) if t]
    out: List[str] = []
    for tok in raw_tokens:
        tok = tok.strip()
        if not tok:
            continue
        m = re.match(r"^(l|d|j|m|t|s|n|c)\x27(.+)$", tok, flags=re.IGNORECASE)
        if m:
            clitic = m.group(1).lower() + "'"
            rest = m.group(2)
            out.append(clitic)
            if rest:
                out.append(rest)
            continue
        out.append(tok)
    return [norm_text(t) for t in out if norm_text(t)]


@dataclass(frozen=True)
class WordSpan:
    start: float
    end: float
    text: str


def read_lab_sentences(lab_path: Path) -> List[str]:
    txt = lab_path.read_text(encoding="utf-8", errors="replace").splitlines()
    if not txt:
        return []
    line = txt[0].strip()
    parts = [p.strip() for p in line.split(".") if p.strip()]
    out = []
    for p in parts:
        s = p.strip()
        if not s.endswith("."):
            s = s + "."
        out.append(s)
    return out


def word_spans_for_sentence(words_tier: Sequence, sentence: str) -> List[WordSpan]:
    """
    Map a sentence string to contiguous word intervals by greedy matching on normalized tokens.
    words_tier elements must have .start/.end/.text
    """
    target_tokens = french_tokens(sentence)
    spans: List[WordSpan] = []

    intervals = [WordSpan(start=w.start, end=w.end, text=w.text) for w in words_tier]

    def is_meta_word(s: str) -> bool:
        raw = s.strip()
        if raw == "":
            return True
        if raw.startswith("<") and raw.endswith(">"):
            return True
        t = norm_text(s)
        if t == "":
            return True
        return False

    labs: List[str] = []
    idx_map: List[int] = []
    for j, it in enumerate(intervals):
        if is_meta_word(it.text):
            continue
        labs.append(norm_text(it.text))
        idx_map.append(j)

    if not target_tokens:
        return []

    # Find first occurrence of target_tokens as a subsequence in labs (exact contiguous match)
    starts: List[int] = [k for k, lab in enumerate(labs) if lab == target_tokens[0]]
    chosen_start = None
    for s in starts:
        if s + len(target_tokens) > len(labs):
            continue
        if labs[s : s + len(target_tokens)] == target_tokens:
            chosen_start = s
            break
    if chosen_start is None:
        raise ValueError(f"Sentence not found in word tier: {sentence!r}")

    for off in range(len(target_tokens)):
        spans.append(intervals[idx_map[chosen_start + off]])

    return spans


def phones_for_word_spans(phones_tier: Sequence, spans: Sequence[WordSpan]) -> List[Tuple[float, float, str]]:
    if not spans:
        return []
    t0 = spans[0].start
    t1 = spans[-1].end
    out: List[Tuple[float, float, str]] = []
    for p in phones_tier:
        if not is_real_phone(p.text):
            continue
        # midpoint membership in [t0, t1]
        mid = 0.5 * (p.start + p.end)
        if mid >= t0 - 1e-6 and mid <= t1 + 1e-6:
            out.append((p.start, p.end, p.text.strip()))
    return out


def concat_with_phone_layout(
    phones: Sequence[str],
    index: PhoneIndex,
    *,
    crossfade_ms: float,
    fade_ms: float,
    world: bool,
) -> Tuple[np.ndarray, int, List[Tuple[float, float, str]], float]:
    """
    Returns (wave, sr, phone_intervals_relative, xmax)
    Phone intervals are BEFORE WORLD (layout), but wave may be WORLD-resynth => lengths can differ.
    We rescale phone times to match final waveform length.
    """
    segs: List[np.ndarray] = []
    sr_out = None

    for ph in phones:
        occ = index.pick(ph)
        x, sr = read_wav_mono(occ.wav_path)
        if sr_out is None:
            sr_out = sr
        elif sr != sr_out:
            raise ValueError("Sample rate mismatch in corpus")

        seg = extract_segment(x, sr, occ.start, occ.end)
        seg = normalize_rms(seg)
        seg = linear_fade_edges(seg, sr, fade_ms=fade_ms)
        segs.append(seg)

    y_pre = crossfade_concatenate(segs, sr_out, xf_ms=crossfade_ms)

    K = len(phones)
    total_pre = len(y_pre) / float(sr_out)
    if K <= 0:
        rel_phones = []
    else:
        # Equal partition on the *pre-synth* timeline (demo-stable under crossfade).
        step = total_pre / K
        rel_phones = [(i * step, (i + 1) * step, phones[i]) for i in range(K)]

    y = world_resynth(y_pre, sr_out) if world else y_pre
    xmax = float(len(y) / sr_out)

    # rescale phone times to xmax
    if rel_phones:
        old_xmax = rel_phones[-1][1]
        scale = xmax / old_xmax if old_xmax > 0 else 1.0
        rel_phones = [(a * scale, b * scale, lab) for (a, b, lab) in rel_phones]

    return y, sr_out, rel_phones, xmax


def main() -> None:
    root = ROOT
    rendu = root / "rendu_TTS"
    rendu.mkdir(parents=True, exist_ok=True)

    # 5 demo sentences (from corpus lists, not poem)
    demos: List[Tuple[str, str]] = [
        ("12-1", "Il tombe lourdement sur un sol plat."),
        ("18-1", "La neige couvre la cime des montagnes."),
        ("18-2", "Je ne peux atteindre les bocaux de confiture."),
        ("11-2", "Papa coupe l'herbe dans le jardin."),
        ("15-2", "Le capitaine regarde par le hublot de sa cabine."),
    ]

    for _, sent in demos:
        if norm_text(sent) in {norm_text(x) for x in POEM_LINES}:
            raise SystemExit(f"Accidentally picked a poem line: {sent}")

    index = build_index_from_project(root, textgrid_glob="aligned_one/*.TextGrid", tier="phones")

    manifest = []
    for idx, (base, sentence) in enumerate(demos, start=1):
        tg_path = root / "aligned_one" / f"{base}.TextGrid"
        words = read_textgrid_tier(tg_path, "words")
        ph_tier = read_textgrid_tier(tg_path, "phones")
        spans = word_spans_for_sentence(words, sentence)
        ref_phones = [p for _, _, p in phones_for_word_spans(ph_tier, spans)]

        out_wav = rendu / f"synthese_{idx:02d}.wav"
        out_tg = rendu / f"synthese_{idx:02d}.TextGrid"

        y, sr, rel_phones, xmax = concat_with_phone_layout(
            ref_phones,
            index,
            crossfade_ms=6.0,
            fade_ms=3.0,
            world=True,
        )
        sf.write(str(out_wav), y.astype(np.float32, copy=False), sr)

        # single-word tier: whole sentence
        words_intervals = [(0.0, xmax, sentence.replace("\n", " ").strip())]
        write_simple_textgrid_words_phones(out_tg, xmax, words_intervals, rel_phones)

        manifest.append(
            {
                "id": f"synthese_{idx:02d}",
                "source_recording": base,
                "sentence": sentence,
                "phones_reference_from_source_alignment": ref_phones,
                "wav": str(out_wav.as_posix()),
                "textgrid": str(out_tg.as_posix()),
            }
        )

    (rendu / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")

    # Copy notebook without touching the original in-place
    nb_src = root / "Vocodeurs_M1_TAL_version_finale.ipynb"
    nb_dst = rendu / "Vocodeurs_M1_TAL_version_finale.ipynb"
    shutil.copyfile(nb_src, nb_dst)

    # Append extension section to the copied notebook only
    nb = json.loads(nb_dst.read_text(encoding="utf-8"))
    nb.setdefault("cells", [])
    nb["cells"].append(
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## Extension — rendu TTS (projet final)\n",
                "\n",
                "Cette section a été **ajoutée** pour le rendu : le notebook original du cours n’a pas été réécrit.\n",
                "\n",
                "- **Synthèse**: concaténation de clips phonème extraits des alignements MFA (`aligned_one/*.TextGrid`) + crossfade + re-synthèse WORLD légère (`projet_tts.py`).\n",
                "- **Phrases**: 5 phrases de démonstration (hors poème) listées dans `rendu_TTS/manifest.json`.\n",
                "- **Fichiers générés**: `rendu_TTS/synthese_01.wav` … + `TextGrid` associés.\n",
                "\n",
                "> Si tu exécutes ce notebook ailleurs (Colab), installe les dépendances comme dans la partie cours (`pyworld`, `soundfile`, etc.).\n",
            ],
        }
    )
    nb["cells"].append(
        {
            "cell_type": "code",
            "metadata": {},
            "source": [
                "from pathlib import Path\n",
                "import json\n",
                "import soundfile as sf\n",
                "\n",
                "rendu = Path('rendu_TTS')\n",
                "print('manifest:', json.loads((rendu / 'manifest.json').read_text(encoding='utf-8'))[0].keys())\n",
                "\n",
                "wav = rendu / 'synthese_01.wav'\n",
                "x, sr = sf.read(wav, always_2d=False)\n",
                "print(wav, 'sr=', sr, 'samples=', len(x))\n",
            ],
        }
    )
    nb_dst.write_text(json.dumps(nb, ensure_ascii=False, indent=1), encoding="utf-8")

    # Write report markdown + PDF
    report_md = rendu / "REPORT_TTS.md"
    report_md.write_text(
        "\n".join(
            [
                "# Rapport — TTS par concaténation + WORLD (extension)",
                "",
                "## Objectif",
                "Mettre en œuvre une chaîne TTS de type **unit selection** à partir d’alignements MFA (phones) et d’une resynthèse WORLD légère pour lisser les discontinuités.",
                "",
                "## Fichiers",
                "- Notebook rendu (copie + section ajoutée) : `rendu_TTS/Vocodeurs_M1_TAL_version_finale.ipynb`",
                "- Phrases + métadonnées : `rendu_TTS/manifest.json`",
                "- Audios + TextGrids : `rendu_TTS/synthese_01.*` … `synthese_05.*`",
                "- Code : `projet_tts.py` et `rendu_TTS/build_rendu_outputs.py`",
                "",
                "## Modifications du notebook (principe “minimum”)",
                "- Le fichier original `Vocodeurs_M1_TAL_version_finale.ipynb` à la racine du projet **n’est pas modifié**.",
                "- Le rendu utilise une **copie** dans `rendu_TTS/` avec quelques cellules **ajoutées en fin** pour pointer vers les sorties.",
                "",
                "## Amélioration proposée",
                "- **Coarticulation / jonctions** : fenêtrage en bords de clips + **crossfade** entre unités + **WORLD resynth** sur la chaîne concaténée pour réduire les à-coups spectraux.",
                "",
                "## Limites / problèmes rencontrés",
                "- La sélection d’unités est **aléatoire** parmi les occurrences d’un phone : la qualité varie.",
                "- Le placement temporel des phones dans le `TextGrid` de sortie est **approximatif** après resynthèse (normalisation longueur).",
                "",
                "## Combescure (100 phrases)",
                "Les 100 phrases Combescure correspondent aux fichiers **`1-1` … `20-2`** : 20 listes × 2 fichiers, 5 phrases par fichier (donc 20 × 2 × 5 = 100). Les transcriptions sont dans `corpus/*.lab` et les alignements MFA dans `aligned_one/*.TextGrid`.",
                "",
            ]
        ),
        encoding="utf-8",
    )

    pdf_out = rendu / "REPORT_TTS.pdf"
    subprocess.run(
        [
            "pandoc",
            str(report_md),
            "-o",
            str(pdf_out),
            "--pdf-engine=pdflatex",
        ],
        check=True,
    )

    print("Wrote:", rendu / "manifest.json")
    print("Wrote PDF:", pdf_out)


if __name__ == "__main__":
    main()
