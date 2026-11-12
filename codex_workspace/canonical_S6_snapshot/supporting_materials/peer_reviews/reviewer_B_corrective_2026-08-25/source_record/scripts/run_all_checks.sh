#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

echo "[1/7] Verifying static SHA-256 manifest"
sha256sum -c manifests/SHA256SUMS.txt

echo "[2/7] Rerunning exact finite-algebra checks"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT
python3 scripts/reproduce_core_checks.py --json "$TMP/core_checks.json" --text "$TMP/core_checks.txt"
cmp "$TMP/core_checks.json" evidence/core_checks/core_checks.json
cmp "$TMP/core_checks.txt" evidence/core_checks/core_checks.txt

echo "[3/7] Verifying PDF page counts and annotations"
python3 - <<'PY'
from pathlib import Path
import fitz
from pypdf import PdfReader
root=Path.cwd()
expected={
    root/'source/s6_canonical_108_pages.pdf':108,
    root/'evidence/annotations/S6_AUDIT_ANNOTATED_MANUSCRIPT.pdf':108,
    root/'evidence/critical_pages/S6_CRITICAL_EVIDENCE_PAGES.pdf':37,
    root/'evidence/critical_pages/manuscript_pages_040_062.pdf':23,
    root/'evidence/critical_pages/manuscript_pages_095_108.pdf':14,
    root/'reports/S6_MATHEMATICAL_PROOF_AUDIT.pdf':6,
    root/'session/ASSISTANT_VISIBLE_OUTPUTS.pdf':7,
}
for path,count in expected.items():
    actual=len(PdfReader(str(path)).pages)
    assert actual==count, f'{path}: expected {count} pages, got {actual}'
doc=fitz.open(root/'evidence/annotations/S6_AUDIT_ANNOTATED_MANUSCRIPT.pdf')
annots=0
for page in doc:
    annot=page.first_annot
    while annot:
        annots+=1
        annot=annot.next
assert annots==108, f'expected 108 annotations, got {annots}'
print('PDF page counts and 108 annotations verified')
PY

echo "[4/7] Verifying theorem and risk ledgers"
python3 - <<'PY'
from collections import Counter
from pathlib import Path
import csv
root=Path.cwd()
rows=list(csv.DictReader((root/'evidence/ledgers/S6_THEOREM_AUDIT_LEDGER.csv').open(encoding='utf-8')))
assert len(rows)==92, len(rows)
expected={
    'CONDITIONAL-PASS':34,
    'REVIEWED-NO-ERROR-FOUND':28,
    'CRITICAL-UNRESOLVED':15,
    'VERIFIED-EXACT':9,
    'SECONDARY':6,
}
actual=dict(Counter(r['status'] for r in rows))
assert actual==expected, actual
risks=list(csv.DictReader((root/'evidence/ledgers/S6_PROOF_RISK_LEDGER.csv').open(encoding='utf-8')))
assert [r['risk_id'] for r in risks]==['R1','R2','R3','R4','R5']
print('Ledger counts verified:', actual)
PY

echo "[5/7] Verifying canonical source page markers"
python3 - <<'PY'
from pathlib import Path
import re
p=Path('source/s6_canonical_full_108_pages.tex')
s=p.read_text(encoding='utf-8',errors='replace')
starts=re.findall(r'SOURCE PDF PAGE (\d{3}) START',s)
ends=re.findall(r'SOURCE PDF PAGE (\d{3}) END',s)
expected=[f'{i:03d}' for i in range(1,109)]
assert starts==expected, 'page-start markers are incomplete or out of order'
assert ends==expected, 'page-end markers are incomplete or out of order'
print('108 start markers and 108 end markers verified')
PY

echo "[6/7] Verifying audit summaries and critical-page index"
python3 - <<'PY'
from pathlib import Path
import csv,json
root=Path.cwd()
summary=json.loads((root/'reports/S6_MATHEMATICAL_PROOF_AUDIT_SUMMARY.json').read_text())
assert summary['exact_core_check_count']==38
assert summary['exact_core_checks_passed'] is True
assert summary['theorem_ledger_rows']==92
assert summary['critical_evidence_pdf_pages']==37
assert summary['annotated_manuscript_pages']==108
idx=list(csv.DictReader((root/'evidence/critical_pages/CRITICAL_PAGE_INDEX.csv').open(encoding='utf-8')))
assert len(idx)==37
assert [int(r['physical_page']) for r in idx]==list(range(40,63))+list(range(95,109))
print('Summary and critical-page index verified')
PY

echo "[7/7] Verification complete"
echo "PASS: static files, exact checks, PDFs, annotations, ledgers, markers, and indices are consistent."
echo "Scope reminder: this PASS verifies the evidence package; it does not certify unresolved geometric obligations R1-R4."
