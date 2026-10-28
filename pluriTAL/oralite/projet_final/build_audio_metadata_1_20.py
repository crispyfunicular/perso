#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
import re
import wave
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Sequence, Tuple


@dataclass(frozen=True)
class Interval:
    start: float
    end: float
    text: str


TEXTGRID_INTERVAL_RE = re.compile(
    r"""
    xmin\s*=\s*(?P<xmin>[0-9.]+)\s*
    xmax\s*=\s*(?P<xmax>[0-9.]+)\s*
    text\s*=\s*"(?P<text>[^"]*)"\s*
    """,
    re.VERBOSE,
)


def read_textgrid_tier(path: Path, tier_name: str) -> List[Interval]:
    text = path.read_text(encoding="utf-8", errors="replace")
    idx = text.find(f'name = "{tier_name}"')
    if idx == -1:
        return []
    nxt = text.find("item [", idx + 1)
    block = text[idx:] if nxt == -1 else text[idx:nxt]
    out: List[Interval] = []
    for m in TEXTGRID_INTERVAL_RE.finditer(block):
        out.append(Interval(start=float(m.group("xmin")), end=float(m.group("xmax")), text=m.group("text")))
    return out


def wav_duration_seconds(wav: Path) -> Optional[float]:
    try:
        with wave.open(str(wav), "rb") as wf:
            frames = wf.getnframes()
            rate = wf.getframerate()
            if rate <= 0:
                return None
            return frames / float(rate)
    except Exception:
        return None


def load_legacy_alignment_analysis_csv(path: Path) -> Dict[str, dict]:
    """
    Load aligned_out/alignment_analysis.csv keyed by basename (without extension).
    """
    if not path.exists():
        return {}
    rows: Dict[str, dict] = {}
    with path.open("r", encoding="utf-8", newline="") as f:
        r = csv.DictReader(f)
        for row in r:
            key = (row.get("file") or "").strip()
            if not key:
                continue
            rows[key] = row
    return rows


def tier_nonempty_coverage(intervals: Sequence[Interval]) -> Tuple[float, int, int]:
    """
    Return (covered_seconds, nonempty_count, total_intervals)
    where covered_seconds sums intervals whose text is not empty after strip.
    """
    nonempty = 0
    covered = 0.0
    for it in intervals:
        t = it.text.strip()
        if t == "":
            continue
        nonempty += 1
        covered += max(0.0, it.end - it.start)
    return covered, nonempty, len(intervals)


def main() -> None:
    project_root = Path(__file__).resolve().parent
    audio_dir = project_root / "audio"
    corpus_dir = project_root / "corpus"
    aligned_one = project_root / "aligned_one"
    aligned_out = project_root / "aligned_out"
    legacy_csv = aligned_out / "alignment_analysis.csv"
    legacy = load_legacy_alignment_analysis_csv(legacy_csv)

    out_csv = project_root / "audio_metadata_1-20.csv"

    basenames: List[str] = []
    for i in range(1, 21):
        for side in ("1", "2"):
            base = f"{i}-{side}"
            wav = audio_dir / f"{base}.wav"
            if wav.exists():
                basenames.append(base)

    basenames = sorted(set(basenames), key=lambda s: (int(s.split("-")[0]), int(s.split("-")[1])))

    fieldnames = [
        "basename",
        "wav_path",
        "lab_path",
        "textgrid_aligned_one_path",
        "textgrid_aligned_out_path",
        "wav_duration_s",
        "wav_mtime_utc",
        "textgrid_mtime_utc",
        "words_nonempty_coverage_s",
        "words_nonempty_count",
        "words_interval_count",
        "phones_nonempty_coverage_s",
        "phones_nonempty_count",
        "phones_interval_count",
        "legacy_alignment_analysis_json",
    ]

    rows: List[dict] = []
    for base in basenames:
        wav = audio_dir / f"{base}.wav"
        lab = corpus_dir / f"{base}.lab"
        tg1 = aligned_one / f"{base}.TextGrid"
        tg2 = aligned_out / f"{base}.TextGrid"

        wav_dur = wav_duration_seconds(wav)
        wav_mtime = datetime.fromtimestamp(wav.stat().st_mtime, tz=timezone.utc).isoformat()
        tg_mtime = ""
        if tg1.exists():
            tg_mtime = datetime.fromtimestamp(tg1.stat().st_mtime, tz=timezone.utc).isoformat()
        elif tg2.exists():
            tg_mtime = datetime.fromtimestamp(tg2.stat().st_mtime, tz=timezone.utc).isoformat()

        tg_path = tg1 if tg1.exists() else (tg2 if tg2.exists() else None)
        words_cov_s = words_nonempty = words_total = ""
        phones_cov_s = phones_nonempty = phones_total = ""
        if tg_path is not None:
            w_cov, w_n, w_t = tier_nonempty_coverage(read_textgrid_tier(tg_path, "words"))
            p_cov, p_n, p_t = tier_nonempty_coverage(read_textgrid_tier(tg_path, "phones"))
            words_cov_s, words_nonempty, words_total = f"{w_cov:.6f}", str(w_n), str(w_t)
            phones_cov_s, phones_nonempty, phones_total = f"{p_cov:.6f}", str(p_n), str(p_t)

        legacy_row = legacy.get(base)
        legacy_json = json.dumps(legacy_row, ensure_ascii=False) if legacy_row else ""

        rows.append(
            {
                "basename": base,
                "wav_path": str(wav.as_posix()),
                "lab_path": str(lab.as_posix()) if lab.exists() else "",
                "textgrid_aligned_one_path": str(tg1.as_posix()) if tg1.exists() else "",
                "textgrid_aligned_out_path": str(tg2.as_posix()) if tg2.exists() else "",
                "wav_duration_s": "" if wav_dur is None else f"{wav_dur:.6f}",
                "wav_mtime_utc": wav_mtime,
                "textgrid_mtime_utc": tg_mtime,
                "words_nonempty_coverage_s": words_cov_s,
                "words_nonempty_count": words_nonempty,
                "words_interval_count": words_total,
                "phones_nonempty_coverage_s": phones_cov_s,
                "phones_nonempty_count": phones_nonempty,
                "phones_interval_count": phones_total,
                "legacy_alignment_analysis_json": legacy_json,
            }
        )

    with out_csv.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for row in rows:
            w.writerow(row)


if __name__ == "__main__":
    main()
