"""
Small utilities for the course TTS extension:
- parse MFA/Praat TextGrids (phones tier)
- build a phone occurrence index from a corpus of (wav, TextGrid) pairs
- concatenate phone clips with light crossfade + WORLD re-synthesis

This is intentionally dependency-light (numpy + soundfile + pyworld).
"""

from __future__ import annotations

import math
import random
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

import numpy as np
import pyworld as pw
import soundfile as sf


TEXTGRID_INTERVAL_RE = re.compile(
    r"""
    xmin\s*=\s*(?P<xmin>[0-9.]+)\s*
    xmax\s*=\s*(?P<xmax>[0-9.]+)\s*
    text\s*=\s*"(?P<text>[^"]*)"\s*
    """,
    re.VERBOSE,
)


@dataclass(frozen=True)
class Interval:
    start: float
    end: float
    text: str


def read_textgrid_tier(path: Path, tier_name: str) -> List[Interval]:
    text = path.read_text(encoding="utf-8", errors="replace")
    idx = text.find(f'name = "{tier_name}"')
    if idx == -1:
        raise ValueError(f'Tier "{tier_name}" not found in {path}')
    nxt = text.find("item [", idx + 1)
    block = text[idx:] if nxt == -1 else text[idx:nxt]
    out: List[Interval] = []
    for m in TEXTGRID_INTERVAL_RE.finditer(block):
        out.append(Interval(start=float(m.group("xmin")), end=float(m.group("xmax")), text=m.group("text")))
    return out


def is_real_phone(p: str) -> bool:
    p = p.strip()
    if p == "":
        return False
    if p.lower() in {"sil", "spn"}:
        return False
    return True


def phone_sequence_from_textgrid(tg: Path, tier: str = "phones") -> List[Interval]:
    return [it for it in read_textgrid_tier(tg, tier) if is_real_phone(it.text)]


@dataclass
class PhoneOcc:
    wav_path: Path
    tg_path: Path
    start: float
    end: float
    phone: str


class PhoneIndex:
    def __init__(self, rng: Optional[random.Random] = None):
        self.rng = rng or random.Random(0)
        self.by_phone: Dict[str, List[PhoneOcc]] = {}

    def add_corpus_pair(self, wav: Path, tg: Path, tier: str = "phones") -> None:
        if not wav.exists():
            raise FileNotFoundError(str(wav))
        if not tg.exists():
            raise FileNotFoundError(str(tg))
        for it in phone_sequence_from_textgrid(tg, tier):
            self.by_phone.setdefault(it.text.strip(), []).append(
                PhoneOcc(wav_path=wav, tg_path=tg, start=it.start, end=it.end, phone=it.text.strip())
            )

    def pick(self, phone: str) -> PhoneOcc:
        phone = phone.strip()
        choices = self.by_phone.get(phone, [])
        if not choices:
            raise KeyError(f"No occurrences for phone '{phone}' in index")
        return self.rng.choice(choices)


def read_wav_mono(path: Path) -> Tuple[np.ndarray, int]:
    x, sr = sf.read(str(path), always_2d=False)
    if x.ndim > 1:
        x = np.mean(x, axis=1)
    x = np.asarray(x, dtype=np.float64)
    return x, int(sr)


def extract_segment(x: np.ndarray, sr: int, t0: float, t1: float) -> np.ndarray:
    i0 = int(math.floor(t0 * sr))
    i1 = int(math.ceil(t1 * sr))
    i0 = max(0, min(i0, len(x)))
    i1 = max(0, min(i1, len(x)))
    if i1 <= i0:
        return np.zeros(0, dtype=np.float64)
    return x[i0:i1].astype(np.float64, copy=False)


def rms(x: np.ndarray) -> float:
    if x.size == 0:
        return 0.0
    return float(np.sqrt(np.mean(x * x) + 1e-12))


def normalize_rms(x: np.ndarray, target: float = 0.06) -> np.ndarray:
    r = rms(x)
    if r <= 1e-8:
        return x
    return x * (target / r)


def linear_fade_edges(x: np.ndarray, sr: int, fade_ms: float = 3.0) -> np.ndarray:
    n = x.size
    if n == 0:
        return x
    fade = int(max(1, (fade_ms / 1000.0) * sr))
    fade = min(fade, n // 2)
    if fade <= 0:
        return x
    ramp_in = np.linspace(0.0, 1.0, fade, endpoint=False)
    ramp_out = np.linspace(1.0, 0.0, fade, endpoint=False)
    y = x.copy()
    y[:fade] *= ramp_in
    y[-fade:] *= ramp_out
    return y


def crossfade_concatenate(segs: Sequence[np.ndarray], sr: int, xf_ms: float = 5.0) -> np.ndarray:
    if not segs:
        return np.zeros(0, dtype=np.float64)
    xf = int(max(1, (xf_ms / 1000.0) * sr))
    out = segs[0].astype(np.float64, copy=True)
    for nxt in segs[1:]:
        if out.size == 0:
            out = nxt.astype(np.float64, copy=True)
            continue
        if nxt.size == 0:
            continue
        n = min(xf, out.size, nxt.size)
        if n <= 0:
            out = np.concatenate([out, nxt])
            continue
        a = out[:-n]
        b = nxt[n:]
        w = np.linspace(1.0, 0.0, n, endpoint=False)
        overlap = out[-n:] * w + nxt[:n] * (1.0 - w)
        out = np.concatenate([a, overlap, b])
    return out


def world_resynth(x: np.ndarray, sr: int) -> np.ndarray:
    """
    Cheap WORLD re-synthesis of a waveform (analysis -> modify minimally -> synth).
    """
    if x.size == 0:
        return x
    x64 = np.asarray(x, dtype=np.float64)
    f0, t = pw.harvest(x64, sr)
    sp = pw.cheaptrick(x64, f0, t, sr)
    ap = pw.d4c(x64, f0, t, sr)
    y = pw.synthesize(f0, sp, ap, sr)
    # WORLD output length can differ slightly; trim/pad to original-ish
    if y.size > x64.size * 1.5:
        y = y[: x64.size + int(0.05 * sr)]
    return y.astype(np.float64, copy=False)


def synthesize_phone_sequence(
    phones: Sequence[str],
    index: PhoneIndex,
    out_wav: Path,
    *,
    crossfade_ms: float = 6.0,
    fade_ms: float = 3.0,
    world: bool = True,
) -> None:
    segs: List[np.ndarray] = []
    sr_out: Optional[int] = None

    for ph in phones:
        occ = index.pick(ph)
        x, sr = read_wav_mono(occ.wav_path)
        if sr_out is None:
            sr_out = sr
        elif sr != sr_out:
            raise ValueError(f"Sample rate mismatch: {sr} vs {sr_out} ({occ.wav_path})")

        seg = extract_segment(x, sr, occ.start, occ.end)
        seg = normalize_rms(seg)
        seg = linear_fade_edges(seg, sr, fade_ms=fade_ms)
        segs.append(seg)

    y = crossfade_concatenate(segs, sr_out, xf_ms=crossfade_ms)
    if world:
        y = world_resynth(y, sr_out)

    out_wav.parent.mkdir(parents=True, exist_ok=True)
    sf.write(str(out_wav), y.astype(np.float32, copy=False), sr_out)


def write_simple_textgrid_words_phones(
    out_tg: Path,
    xmax: float,
    words: Sequence[Tuple[float, float, str]],
    phones: Sequence[Tuple[float, float, str]],
) -> None:
    """
    Write a minimal Praat TextGrid (long text format) with tiers words+phones.
    """

    out_tg.parent.mkdir(parents=True, exist_ok=True)
    with out_tg.open("w", encoding="utf-8") as f:
        f.write('File type = "ooTextFile"\n')
        f.write('Object class = "TextGrid"\n\n')
        f.write("xmin = 0 \n")
        f.write(f"xmax = {xmax} \n")
        f.write("tiers? <exists> \n")
        f.write("size = 2 \n")
        f.write("item []: \n")
        # NOTE: Praat expects numbered items; we keep names in tier headers via write_tier (compatible enough for MFA-like files)
        # We'll mimic MFA structure: item [1] words, item [2] phones
        f.write("    item [1]:\n")
        f.write('        class = "IntervalTier" \n')
        f.write('        name = "words" \n')
        f.write("        xmin = 0 \n")
        f.write(f"        xmax = {xmax} \n")
        f.write(f"        intervals: size = {len(words)} \n")
        for i, (xmin, xmx, lab) in enumerate(words, start=1):
            f.write(f"        intervals [{i}]:\n")
            f.write(f"            xmin = {xmin} \n")
            f.write(f"            xmax = {xmx} \n")
            f.write(f'            text = "{lab}" \n')

        f.write("    item [2]:\n")
        f.write('        class = "IntervalTier" \n')
        f.write('        name = "phones" \n')
        f.write("        xmin = 0 \n")
        f.write(f"        xmax = {xmax} \n")
        f.write(f"        intervals: size = {len(phones)} \n")
        for i, (xmin, xmx, lab) in enumerate(phones, start=1):
            f.write(f"        intervals [{i}]:\n")
            f.write(f"            xmin = {xmin} \n")
            f.write(f"            xmax = {xmx} \n")
            f.write(f'            text = "{lab}" \n')


def build_index_from_project(
    project_root: Path,
    *,
    textgrid_glob: str = "aligned_one/*.TextGrid",
    tier: str = "phones",
    rng: Optional[random.Random] = None,
) -> PhoneIndex:
    idx = PhoneIndex(rng=rng)
    for tg in sorted(project_root.glob(textgrid_glob)):
        base = tg.stem
        wav = project_root / "audio" / f"{base}.wav"
        idx.add_corpus_pair(wav, tg, tier=tier)
    return idx
