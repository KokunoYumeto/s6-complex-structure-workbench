#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$ROOT"

echo "[1/9] Verifying the complete integrated SHA-256 manifest"
sha256sum -c manifests/INTEGRATED_SHA256SUMS.txt

echo "[2/9] Verifying the dated integration-update manifest"
sha256sum -c integration_update/SHA256SUMS.txt

echo "[3/9] Rerunning and byte-comparing the 17 exact integration checks"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT
cp integration_update/evidence/exact_checks/integration_exact_checks.json "$TMP/before.json"
cp integration_update/evidence/exact_checks/integration_exact_checks.txt "$TMP/before.txt"
python3 integration_update/scripts/reproduce_integration_checks.py > "$TMP/reproduce.stdout"
cmp "$TMP/before.json" integration_update/evidence/exact_checks/integration_exact_checks.json
cmp "$TMP/before.txt" integration_update/evidence/exact_checks/integration_exact_checks.txt
python3 - <<'PY'
import json
from pathlib import Path
p=Path('integration_update/evidence/exact_checks/integration_exact_checks.json')
d=json.loads(p.read_text(encoding='utf-8'))
assert d['all_passed'] is True
assert d['check_count'] == 17
print('17/17 exact integration checks pass and reproduce byte-for-byte')
PY

echo "[4/9] Verifying integration PDFs, page counts, and annotation count"
python3 - <<'PY'
from pathlib import Path
from pypdf import PdfReader
import fitz
root=Path.cwd()
expected={
    root/'integration_update/reports/S6_TWO_PAGE_MATHEMATICAL_STATUS.pdf':2,
    root/'integration_update/reports/S6_MATHEMATICAL_RESULTS_SO_FAR.pdf':5,
    root/'integration_update/reports/S6_CORRECTIVE_PEER_REVIEW_ADDENDUM.pdf':7,
    root/'integration_update/reports/S6_MATHEMATICAL_PROOF_AUDIT_REVISED.pdf':19,
    root/'integration_update/evidence/annotations/S6_REVISED_AUDIT_ANNOTATED_MANUSCRIPT.pdf':108,
    root/'integration_update/session/INTEGRATION_SESSION_VISIBLE_OUTPUTS.pdf':1,
}
for path,count in expected.items():
    actual=len(PdfReader(str(path)).pages)
    assert actual==count, f'{path}: expected {count}, got {actual}'
annotated=root/'integration_update/evidence/annotations/S6_REVISED_AUDIT_ANNOTATED_MANUSCRIPT.pdf'
doc=fitz.open(annotated)
annots=0
for page in doc:
    annot=page.first_annot
    while annot:
        annots += 1
        annot=annot.next
assert annots==108, annots
print('PDF counts and 108 revised annotations verified')
PY

echo "[5/9] Verifying revised ledgers and annotation index"
python3 - <<'PY'
from collections import Counter
from pathlib import Path
import csv
root=Path.cwd()
ledger=list(csv.DictReader((root/'integration_update/evidence/ledgers/S6_REVISED_THEOREM_AUDIT_LEDGER.csv').open(encoding='utf-8')))
assert len(ledger)==95, len(ledger)
expected={
 'REVIEWED-NO-ERROR-FOUND':28,
 'REVIEWED-DOWNSTREAM':14,
 'VERIFIED-RECONSTRUCTED':12,
 'VERIFIED-EXACT':9,
 'OPEN-NONBLOCKING':8,
 'VERIFIED-INDEPENDENT':7,
 'OPEN-REDUNDANT':4,
 'PROVISIONAL-PASS':2,
 'MIXED-PARTIAL-VERIFICATION':2,
 'VERIFIED-LOCAL':2,
 'RECONSTRUCTED-DEPENDENCIES-EXPLICIT':2,
 'SECONDARY':2,
 'MIXED-COLLAPSE-DEPENDENT':1,
 'VERIFIED-DOWNSTREAM':1,
 'VERIFIED-SCOPE-SEPARATION':1,
}
actual=dict(Counter(r['status'] for r in ledger))
assert actual==expected, actual
risks=list(csv.DictReader((root/'integration_update/evidence/ledgers/S6_REVISED_PROOF_RISK_LEDGER.csv').open(encoding='utf-8')))
assert [r['risk_id'] for r in risks]==['C1','C2','B1','V1','L1','MV1','G1','A1','D1','E1']
idx=list(csv.DictReader((root/'integration_update/evidence/annotations/S6_REVISED_ANNOTATION_INDEX.csv').open(encoding='utf-8')))
assert len(idx)==108
assert [int(r['physical_page']) for r in idx]==list(range(1,109))
print('95-row theorem ledger, 10-entry risk ledger, and 108-row annotation index verified')
PY

echo "[6/9] Verifying the integrated summary and exact preservation of the supplied progress record"
python3 - <<'PY'
from pathlib import Path
import hashlib,json
root=Path.cwd()
summary=json.loads((root/'integration_update/reports/S6_INTEGRATED_VALIDATION_SUMMARY.json').read_text(encoding='utf-8'))
assert summary['revised_disposition']=='RECONSIDERED - PROVISIONALLY FAVORABLE WITH FOCUSED VERIFICATION REQUESTS'
assert summary['main_route_status']['appendix_B_nearby_cycles']=='VERIFIED-RECONSTRUCTED'
assert summary['main_route_status']['section_7_7_leray_transgressions']=='VERIFIED-RECONSTRUCTED'
assert summary['main_route_status']['section_7_5_van_kampen']=='VERIFIED-RECONSTRUCTED'
assert summary['main_route_status']['section_7_2_cusp_collapse']=='OPEN-NONBLOCKING-FOR-RECOGNITION'
p=root/'integration_update/source_record/PRODUCT_PROGRESS_RECORD.md'
h=hashlib.sha256(p.read_bytes()).hexdigest()
assert h=='5a80ded90f83529f88994a1d377a84ac8314d9e733e0393d799b25c77a1f50d6', h
print('Integrated status fields and Product/Codex source-record hash verified')
PY

echo "[7/9] Scanning report build logs for fatal, box, or package warnings"
python3 - <<'PY'
from pathlib import Path
import re
root=Path('integration_update')
logs=[
 root/'reports/S6_MATHEMATICAL_RESULTS_SO_FAR.pandoc.log',
 root/'reports/S6_CORRECTIVE_PEER_REVIEW_ADDENDUM.pandoc.log',
 root/'reports/S6_MATHEMATICAL_PROOF_AUDIT_REVISED.pandoc.log',
 root/'reports/S6_TWO_PAGE_MATHEMATICAL_STATUS.pdflatex.final.log',
 root/'session/INTEGRATION_SESSION_VISIBLE_OUTPUTS.pandoc.log',
]
pat=re.compile(r'(^!|LaTeX Warning|Package .* Warning|Overfull|Underfull)',re.M)
for p in logs:
    text=p.read_text(encoding='utf-8',errors='replace')
    assert not pat.search(text), f'warning/failure marker in {p}'
print('Build logs are free of fatal, LaTeX/package, and box warnings')
PY

echo "[8/9] Running the frozen baseline evidence verifier"
bash scripts/run_all_checks.sh

echo "[9/9] Rechecking complete manifest after all reproducibility runs"
sha256sum -c manifests/INTEGRATED_SHA256SUMS.txt

echo "PASS: integrated package, exact calculations, reports, revised annotations, ledgers, source record, and historical baseline are internally consistent."
echo "Scope: this PASS records reproducibility and the stated reconstruction status; it does not replace independent external review of the remaining analytic and reference-level checks."
