#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

export SOURCE_DATE_EPOCH=1704067200
export FORCE_SOURCE_DATE=1
export TZ=UTC

python3 scripts/generate_monolithic.py >/dev/null
rm -rf build build_monolithic
mkdir -p build build_monolithic

LATEXMK=(latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error)
"${LATEXMK[@]}" -outdir=build s6_canonical.tex | tee build/latexmk_stdout.log
"${LATEXMK[@]}" -outdir=build_monolithic s6_canonical_full.tex | tee build_monolithic/latexmk_stdout.log

warning_pattern='(^!|LaTeX Warning|Package .* Warning|Overfull|Underfull|Missing character|Undefined control sequence|Fatal error|Emergency stop)'
for log in build/s6_canonical.log build_monolithic/s6_canonical_full.log; do
  if grep -nEi "$warning_pattern" "$log"; then
    echo "Build log is not clean: $log" >&2
    exit 1
  fi
done

cmp -s build/s6_canonical.pdf build_monolithic/s6_canonical_full.pdf || {
  echo "Modular and monolithic PDFs differ" >&2
  exit 1
}

pages="$(pdfinfo build/s6_canonical.pdf | awk '/^Pages:/ {print $2}')"
size="$(pdfinfo build/s6_canonical.pdf | awk -F': +' '/^Page size:/ {print $2}')"
[[ "$pages" == "108" ]] || { echo "Expected 108 pages, found $pages" >&2; exit 1; }
[[ "$size" == 612\ x\ 792\ pts* ]] || { echo "Expected letter size, found: $size" >&2; exit 1; }

sha256sum build/s6_canonical.pdf build_monolithic/s6_canonical_full.pdf
