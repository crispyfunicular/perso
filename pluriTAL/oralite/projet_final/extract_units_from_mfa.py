#!/usr/bin/env python3
"""
Extract needed diphones/triphones for target phrases, and locate matching
occurrences in MFA TextGrid phone alignments.
"""

from __future__ import annotations

import argparse
import csv
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Iterator, List, Sequence, Tuple


@dataclass(frozen=True)
class PhoneInterval:
    start: float
    end: float
    phone: str


@dataclass(frozen=True)
class Match:
    unit: str
    unit_type: str  # "diphone" | "triphone"
    textgrid: str
    start: float
    end: float
    phones: str


TEXTGRID_INTERVAL_RE = re.compile(
    r"""
    xmin\s*=\s*(?P<xmin>[0-9.]+)\s*
    xmax\s*=\s*(?P<xmax>[0-9.]+)\s*
    text\s*=\s*"(?P<text>[^"]*)"\s*
    """,
    re.VERBOSE,
)


# Phone equivalence for "ambiguous" phones in French.
# We canonicalize phones for matching and unit extraction so that e.g. a~ɑ,
# and ɛ̃~œ̃ are treated as similar.
PHONE_EQUIV_GROUPS: List[set[str]] = [
    {"a", "ɑ"},
    {"ɛ̃", "œ̃"},
]


def canonical_phone(p: str, enable_equiv: bool) -> str:
    p = normalize_phone(p)
    if not enable_equiv:
        return p
    for grp in PHONE_EQUIV_GROUPS:
        if p in grp:
            # Stable canonical representative: shortest, then lexicographic
            return sorted(grp, key=lambda s: (len(s), s))[0]
    return p


def read_textgrid_phones(path: Path, tier_name: str = "phones") -> List[PhoneInterval]:
    """
    Parse a Praat 'ooTextFile' TextGrid and return phone intervals from the given tier.

    Assumes the TextGrid is in the plain text format that MFA outputs.
    """
    text = path.read_text(encoding="utf-8", errors="replace")

    # Find the phones tier block
    idx = text.find(f'name = "{tier_name}"')
    if idx == -1:
        return []

    # Heuristic: tier runs until next 'item [' or EOF
    next_item = text.find("item [", idx + 1)
    tier_block = text[idx:] if next_item == -1 else text[idx:next_item]

    intervals: List[PhoneInterval] = []
    for m in TEXTGRID_INTERVAL_RE.finditer(tier_block):
        phone = m.group("text")
        start = float(m.group("xmin"))
        end = float(m.group("xmax"))
        intervals.append(PhoneInterval(start=start, end=end, phone=phone))
    return intervals


def normalize_phone(p: str) -> str:
    return p.strip()


def is_real_phone(p: str) -> bool:
    p = normalize_phone(p)
    if p == "":
        return False
    if p.lower() in {"spn", "sil"}:
        return False
    return True


def phones_sequence(intervals: Sequence[PhoneInterval]) -> List[PhoneInterval]:
    return [pi for pi in intervals if is_real_phone(pi.phone)]


def build_inventory(textgrids: Sequence[Path], tier_name: str = "phones") -> List[str]:
    inv: set[str] = set()
    for tg in textgrids:
        for pi in phones_sequence(read_textgrid_phones(tg, tier_name=tier_name)):
            inv.add(normalize_phone(pi.phone))
    # Longest-first greedy matching works better with multi-char phones (e.g. ɑ̃, mʲ)
    return sorted(inv, key=lambda s: (-len(s), s))


def tokenize_ipa_greedy(ipa: str, inventory: Sequence[str]) -> List[str]:
    """
    Tokenize an IPA phrase into phone symbols using greedy longest-match
    against the phone inventory extracted from alignments.

    Keeps '|' as a boundary marker (pause) and ignores '/'.
    """
    ipa = ipa.strip()
    ipa = ipa.replace("/", "")
    # Normalize typical separators
    ipa = re.sub(r"\s+", " ", ipa)

    tokens: List[str] = []
    for chunk in ipa.split(" "):
        if chunk == "":
            continue
        if chunk == "|":
            tokens.append("|")
            continue
        # Greedy segmentation of word chunk
        i = 0
        while i < len(chunk):
            if chunk[i] == "|":
                tokens.append("|")
                i += 1
                continue
            matched = None
            for ph in inventory:
                if chunk.startswith(ph, i):
                    matched = ph
                    break
            if matched is None:
                # Fallback: consume 1 codepoint to avoid infinite loops
                tokens.append(chunk[i])
                i += 1
            else:
                tokens.append(matched)
                i += len(matched)
    return tokens


def ngrams_from_tokens(tokens: Sequence[str], n: int) -> List[Tuple[str, ...]]:
    grams: List[Tuple[str, ...]] = []
    # Split by pause boundaries
    current: List[str] = []
    for t in tokens:
        if t == "|":
            if current:
                grams.extend(tuple(current[i : i + n]) for i in range(0, len(current) - n + 1))
            current = []
        else:
            current.append(t)
    if current:
        grams.extend(tuple(current[i : i + n]) for i in range(0, len(current) - n + 1))
    return grams


def ngram_hits_with_context(
    tokens: Sequence[str], ngram: Tuple[str, ...], context: int = 3
) -> List[Tuple[int, str]]:
    """
    Return list of (start_index_in_segment, context_string) for each hit of ngram
    inside pause-delimited segments. The index is relative to the segment (no '|').
    """
    hits: List[Tuple[int, str]] = []
    seg: List[str] = []

    def scan_segment(segment: List[str]) -> None:
        n = len(ngram)
        if len(segment) < n:
            return
        for i in range(0, len(segment) - n + 1):
            if tuple(segment[i : i + n]) == ngram:
                left = max(0, i - context)
                right = min(len(segment), i + n + context)
                snippet = " ".join(segment[left:right])
                hits.append((i, snippet))

    for t in tokens:
        if t == "|":
            if seg:
                scan_segment(seg)
            seg = []
        else:
            seg.append(t)
    if seg:
        scan_segment(seg)
    return hits


def stringify_ngram(ng: Tuple[str, ...]) -> str:
    return " ".join(ng)


def slide_matches(
    seq: Sequence[PhoneInterval], ngram: Tuple[str, ...]
) -> Iterator[Tuple[int, int, float, float]]:
    """
    Yield matches as (start_idx, end_idx_exclusive, start_time, end_time)
    where time span covers the whole n-gram.
    """
    n = len(ngram)
    phones = [normalize_phone(pi.phone) for pi in seq]
    target = list(ngram)
    for i in range(0, len(phones) - n + 1):
        if phones[i : i + n] == target:
            start_t = seq[i].start
            end_t = seq[i + n - 1].end
            yield i, i + n, start_t, end_t


def read_phrases(path: Path) -> List[str]:
    lines = [ln.rstrip("\n") for ln in path.read_text(encoding="utf-8", errors="replace").splitlines()]
    ipa_lines: List[str] = []
    in_ipa = False
    for ln in lines:
        if ln.strip() == "[IPA]":
            in_ipa = True
            continue
        if in_ipa and ln.strip():
            ipa_lines.append(ln.strip())
    return ipa_lines


def write_csv(path: Path, header: Sequence[str], rows: Iterable[Sequence[str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(list(header))
        for r in rows:
            w.writerow(list(r))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--phrases", type=Path, default=Path("phrases.txt"))
    ap.add_argument("--textgrids-glob", type=str, default="aligned_out/*.TextGrid")
    ap.add_argument("--tier", type=str, default="phones")
    ap.add_argument("--outdir", type=Path, default=Path("unit_matches"))
    ap.add_argument("--max-matches-per-unit", type=int, default=50)
    ap.add_argument("--derive-diphones-from-triphones", action="store_true")
    ap.add_argument("--equiv", action="store_true", help="treat some phones as equivalent (a~ɑ, ɛ̃~œ̃)")
    args = ap.parse_args()

    textgrids = sorted(Path(".").glob(args.textgrids_glob))
    if not textgrids:
        raise SystemExit(f"No TextGrid files found with glob: {args.textgrids_glob}")

    inventory = build_inventory(textgrids, tier_name=args.tier)

    phrases_ipa = read_phrases(args.phrases)
    if not phrases_ipa:
        raise SystemExit(f"No [IPA] lines found in {args.phrases}")

    # Build required units (canonicalized if --equiv)
    phrase_tokens_raw: List[List[str]] = [tokenize_ipa_greedy(p, inventory) for p in phrases_ipa]
    phrase_tokens: List[List[str]] = [
        ["|" if t == "|" else canonical_phone(t, enable_equiv=args.equiv) for t in toks]
        for toks in phrase_tokens_raw
    ]
    required_tri: set[Tuple[str, str, str]] = set()
    required_di: set[Tuple[str, str]] = set()

    for toks in phrase_tokens:
        required_tri.update(ngrams_from_tokens(toks, 3))
        required_di.update(ngrams_from_tokens(toks, 2))

    # Index occurrences in corpus
    matches: List[Match] = []
    counts: dict[Tuple[str, str], int] = {}
    derived_diphone_matches: List[Match] = []
    derived_counts: dict[str, int] = {}

    def add_match(unit_str: str, unit_type: str, tg: Path, start: float, end: float, phones: str) -> None:
        key = (unit_type, unit_str)
        if counts.get(key, 0) >= args.max_matches_per_unit:
            return
        counts[key] = counts.get(key, 0) + 1
        matches.append(
            Match(
                unit=unit_str,
                unit_type=unit_type,
                textgrid=str(tg.as_posix()),
                start=start,
                end=end,
                phones=phones,
            )
        )

    # Triphones first (preferred)
    for tg in textgrids:
        seq_raw = phones_sequence(read_textgrid_phones(tg, tier_name=args.tier))
        # Canonicalize for matching if --equiv
        seq = [
            PhoneInterval(
                start=pi.start,
                end=pi.end,
                phone=canonical_phone(pi.phone, enable_equiv=args.equiv),
            )
            for pi in seq_raw
        ]
        for tri in required_tri:
            for _, _, st, en in slide_matches(seq, tri):
                add_match(stringify_ngram(tri), "triphone", tg, st, en, stringify_ngram(tri))

        # Also diphones (fallback)
        for di in required_di:
            for _, _, st, en in slide_matches(seq, di):
                add_match(stringify_ngram(di), "diphone", tg, st, en, stringify_ngram(di))

        # Optionally derive diphones from found triphones
        if args.derive_diphones_from_triphones:
            for tri in required_tri:
                for idx0, idx1, _, _ in slide_matches(seq, tri):
                    # tri length is 3, indices cover [idx0, idx0+3)
                    a = normalize_phone(seq[idx0].phone)
                    b = normalize_phone(seq[idx0 + 1].phone)
                    c = normalize_phone(seq[idx0 + 2].phone)
                    di1 = f"{a} {b}"
                    di2 = f"{b} {c}"

                    # AB: start(A) -> end(B), BC: start(B) -> end(C)
                    st_ab, en_ab = seq[idx0].start, seq[idx0 + 1].end
                    st_bc, en_bc = seq[idx0 + 1].start, seq[idx0 + 2].end

                    for unit, st_u, en_u in ((di1, st_ab, en_ab), (di2, st_bc, en_bc)):
                        if unit not in {stringify_ngram(d) for d in required_di}:
                            continue
                        if derived_counts.get(unit, 0) >= args.max_matches_per_unit:
                            continue
                        derived_counts[unit] = derived_counts.get(unit, 0) + 1
                        derived_diphone_matches.append(
                            Match(
                                unit=unit,
                                unit_type="diphone_from_triphone",
                                textgrid=str(tg.as_posix()),
                                start=st_u,
                                end=en_u,
                                phones=unit,
                            )
                        )

    # Summaries
    needed_rows = []
    for i, p in enumerate(phrases_ipa, start=1):
        toks = phrase_tokens[i - 1]
        needed_rows.append([str(i), p, " ".join(toks)])

    write_csv(
        args.outdir / "phrases_tokenized.csv",
        ["phrase_id", "phrase_ipa", "tokens"],
        needed_rows,
    )

    write_csv(
        args.outdir / "units_needed_triphone.csv",
        ["triphone"],
        [[stringify_ngram(t)] for t in sorted(required_tri)],
    )
    write_csv(
        args.outdir / "units_needed_diphone.csv",
        ["diphone"],
        [[stringify_ngram(d)] for d in sorted(required_di)],
    )

    # Count coverage
    tri_found = {m.unit for m in matches if m.unit_type == "triphone"}
    di_found = {m.unit for m in matches if m.unit_type == "diphone"}
    derived_di_found = {m.unit for m in derived_diphone_matches}
    coverage_rows = [
        ["triphone", str(len(required_tri)), str(len(tri_found)), f"{(len(tri_found) / max(1, len(required_tri))):.3f}"],
        ["diphone", str(len(required_di)), str(len(di_found)), f"{(len(di_found) / max(1, len(required_di))):.3f}"],
    ]
    write_csv(args.outdir / "coverage.csv", ["unit_type", "needed", "found", "ratio"], coverage_rows)

    write_csv(
        args.outdir / "matches.csv",
        ["unit_type", "unit", "textgrid", "start", "end", "phones"],
        (
            [m.unit_type, m.unit, m.textgrid, f"{m.start:.6f}", f"{m.end:.6f}", m.phones]
            for m in matches
        ),
    )

    if args.derive_diphones_from_triphones:
        write_csv(
            args.outdir / "derived_diphone_matches.csv",
            ["unit_type", "unit", "textgrid", "start", "end", "phones"],
            (
                [m.unit_type, m.unit, m.textgrid, f"{m.start:.6f}", f"{m.end:.6f}", m.phones]
                for m in derived_diphone_matches
            ),
        )

    # Also list missing triphones/diphones
    missing_tri = sorted(set(stringify_ngram(t) for t in required_tri) - tri_found)
    write_csv(args.outdir / "missing_triphones.csv", ["triphone"], ([t] for t in missing_tri))

    missing_di = sorted(set(stringify_ngram(d) for d in required_di) - di_found)
    write_csv(args.outdir / "missing_diphones.csv", ["diphone"], ([d] for d in missing_di))

    if args.derive_diphones_from_triphones:
        missing_di_after = sorted(set(stringify_ngram(d) for d in required_di) - (di_found | derived_di_found))
        write_csv(
            args.outdir / "missing_diphones_after_triphone_split.csv",
            ["diphone"],
            ([d] for d in missing_di_after),
        )

    # Map missing diphones back to the target phrases (where they occur)
    missing_di_tuples = sorted(d for d in required_di if stringify_ngram(d) in set(missing_di))
    rows = []
    for phrase_id, (phrase_ipa, toks) in enumerate(zip(phrases_ipa, phrase_tokens), start=1):
        for di in missing_di_tuples:
            hits = ngram_hits_with_context(toks, di, context=3)
            for start_idx, snippet in hits:
                rows.append(
                    [
                        stringify_ngram(di),
                        str(phrase_id),
                        phrase_ipa,
                        str(start_idx),
                        snippet,
                    ]
                )
    write_csv(
        args.outdir / "missing_diphones_in_phrases.csv",
        ["diphone", "phrase_id", "phrase_ipa", "start_index_in_segment", "tokens_context"],
        rows,
    )


if __name__ == "__main__":
    main()

