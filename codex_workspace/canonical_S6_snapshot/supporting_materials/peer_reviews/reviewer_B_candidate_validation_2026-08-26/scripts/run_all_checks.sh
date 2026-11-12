#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

python "$ROOT/scripts/check_exact_identities.py" > "$TMP/exact_checks.log"
python - "$ROOT/evidence/exact_identity_checks.json" <<'PY'
import json, sys
p=sys.argv[1]
d=json.load(open(p, encoding='utf-8'))
assert d['passed'] == d['total'], d
assert d['total'] == 8, d
print(f"exact identities: {d['passed']}/{d['total']} PASS")
PY

python - "$ROOT/evidence/verification_ledger.csv" <<'PY'
import csv, sys
rows=list(csv.DictReader(open(sys.argv[1], newline='', encoding='utf-8')))
ids={r['id'] for r in rows}
required={'PF-03','PF-04','BC-01','DU-01','DU-02','LM-01','LM-02','LM-03','TRIV-01','S10-01','S10-02','CAND-X','CAND-W','TOP-H2'}
assert required <= ids, sorted(required-ids)
assert next(r for r in rows if r['id']=='BC-01')['status']=='VERIFIED'
assert next(r for r in rows if r['id']=='CAND-X')['status']=='OPEN-CANDIDATE-SPECIFIC'
assert next(r for r in rows if r['id']=='CAND-W')['status']=='OPEN-CANDIDATE-SPECIFIC'
assert next(r for r in rows if r['id']=='TOP-H2')['status']=='OPEN-CANDIDATE-SPECIFIC'
print(f"verification ledger: {len(rows)} claims, fail-closed statuses PASS")
PY

PDF="$ROOT/reports/S6_CANDIDATE_SPECIFIC_VALIDATION_UPDATE.pdf"
PAGES="$(pdfinfo "$PDF" | awk -F: '/^Pages/{gsub(/ /,"",$2); print $2}')"
[ "$PAGES" = "7" ]
pdftotext "$PDF" "$TMP/report.txt"
grep -q "Top-degree cohomology and base change" "$TMP/report.txt"
grep -q "OPEN-CANDIDATE-SPECIFIC" "$ROOT/evidence/verification_ledger.csv"
if grep -q $'\xef\xbf\xbd' "$TMP/report.txt"; then
  echo "replacement character found in PDF text" >&2
  exit 1
fi
echo "report PDF: 7 pages, required text present, no replacement character"

if [ -f "$ROOT/SHA256SUMS" ]; then
  (cd "$ROOT" && sha256sum -c SHA256SUMS)
fi

echo "ALL CHECKS PASS"
