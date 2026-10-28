#!/usr/bin/env bash
set -euo pipefail

# Usage:
#   bash projet_final/script_mfa.sh all
#   bash projet_final/script_mfa.sh one projet_final/audio/1-1.wav
#   bash projet_final/script_mfa.sh list projet_final/audio/a.wav projet_final/audio/b.wav
#
# Output:
#   projet_final/aligned_one/<basename>.TextGrid

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CORPUS_DIR="$PROJECT_ROOT/corpus"
WAV_DIR="$PROJECT_ROOT/audio"
OUT_DIR="$PROJECT_ROOT/aligned_one"

ACOUSTIC_MODEL="french_mfa"
DICTIONARY="french_mfa"

source "$HOME/miniconda3/etc/profile.d/conda.sh"
conda activate mfa

mkdir -p "$OUT_DIR"

mode="${1:-all}"

align_one() {
  local wav="$1"
  local base
  base="$(basename "${wav%.wav}")"
  local lab="$CORPUS_DIR/${base}.lab"

  if [[ ! -f "$wav" ]]; then
    echo "Missing wav: $wav" >&2
    exit 2
  fi
  if [[ ! -f "$lab" ]]; then
    echo "Missing lab: $lab" >&2
    exit 2
  fi

  mfa align_one "$wav" "$lab" "$DICTIONARY" "$ACOUSTIC_MODEL" "$OUT_DIR/${base}.TextGrid"
  echo "Wrote: $OUT_DIR/${base}.TextGrid"
}

case "$mode" in
  one)
    wav="${2:?Provide a .wav path, e.g. projet_final/audio/1-1.wav}"
    align_one "$PROJECT_ROOT/$wav"
    ;;
  all)
    shopt -s nullglob
    for wav in "$WAV_DIR"/*.wav; do
      align_one "$wav"
    done
    ;;
  list)
    shift
    if [[ $# -lt 1 ]]; then
      echo "Usage: $0 list <wav1> [wav2 ...]" >&2
      exit 2
    fi
    for rel in "$@"; do
      align_one "$PROJECT_ROOT/$rel"
    done
    ;;
  *)
    echo "Unknown mode: $mode (use: one|all|list)" >&2
    exit 2
    ;;
esac