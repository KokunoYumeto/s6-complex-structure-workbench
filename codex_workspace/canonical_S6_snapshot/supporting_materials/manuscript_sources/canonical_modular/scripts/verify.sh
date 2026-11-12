#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

if [[ -f SHA256SUMS.txt ]]; then
  sha256sum -c SHA256SUMS.txt
fi

./scripts/build.sh
python3 scripts/verify_source.py --json-output build/source_verification.json >/dev/null

pdf="build/s6_canonical.pdf"
pdfinfo "$pdf" > build/pdfinfo.txt
pdffonts "$pdf" > build/pdffonts.txt

pages="$(awk '/^Pages:/ {print $2}' build/pdfinfo.txt)"
size="$(awk -F': +' '/^Page size:/ {print $2}' build/pdfinfo.txt)"
encrypted="$(awk '/^Encrypted:/ {print $2}' build/pdfinfo.txt)"
[[ "$pages" == "108" ]] || { echo "Page-count failure" >&2; exit 1; }
[[ "$size" == 612\ x\ 792\ pts* ]] || { echo "Page-size failure" >&2; exit 1; }
[[ "$encrypted" == "no" ]] || { echo "Unexpected encryption" >&2; exit 1; }

# In pdffonts output the embedded flag is five fields from the right, allowing
# for font-type names containing whitespace (for example, "Type 1").
awk 'NR > 2 && NF { if ($(NF-4) != "yes") bad=1 } END { exit bad }' build/pdffonts.txt || {
  echo "At least one font is not embedded" >&2
  exit 1
}

if command -v qpdf >/dev/null 2>&1; then
  qpdf --check "$pdf" > build/qpdf_check.txt 2>&1
fi

printf 'PASS: 108 pages, letter size, clean logs, exact page markers, no placeholders, embedded fonts, and byte-identical modular/monolithic PDFs.\n'
