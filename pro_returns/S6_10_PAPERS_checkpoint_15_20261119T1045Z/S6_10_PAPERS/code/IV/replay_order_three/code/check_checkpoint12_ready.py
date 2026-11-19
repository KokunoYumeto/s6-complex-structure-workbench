"""Verify the actual master/report pair ready for the twelfth hourly archive."""
from datetime import datetime,timezone
from pathlib import Path
import csv
import hashlib
import json
import fitz

root=Path(__file__).resolve().parents[1]
expected={
 'notes/part5.tex':'f7b2188bbd5fc453780421599b65168141c8ed09480b1396794f02f41a680e0f',
 'notes/part5_blind.md':'ffdac7780a3d5c35565e31e6bb1bebf459e0f7dc75355e19fc216b5ba4b9a1e4'
}
for name,digest in expected.items():
    assert hashlib.sha256((root/name).read_bytes()).hexdigest()==digest
with (root/'S6_06_BLIND_results.csv').open() as f:
    rows=list(csv.DictReader(f))
assert len(rows)==len({r['id'] for r in rows})==225
assert all(f'P3K.{i}' in {r['id'] for r in rows} for i in range(40,46))
assert 'P3K.39' not in {r['id'] for r in rows}
with fitz.open(root/'S6_06_BLIND_paper.pdf') as pdf:
    assert len(pdf)==481
report=(root/'S6_06_BLIND_report.md').read_text()
assert report.startswith('INCOMPLETE')
assert 'Checkpoint 12 contained 481 manuscript pages.' in report
assert 'Next check: 2026-11-17T12:49:44+00:00.' in report
qa=json.loads((root/'records/typesetting_checkpoint12.json').read_text())
assert qa['master_build']==46 and qa['visual_reviewed_page_count']==54
assert qa['contact_sheets_reviewed']==7 and qa['overfull_over_2pt']==0
assert qa['max_overfull_pt']<2
names=['S6_06_BLIND_paper.pdf','S6_06_BLIND_paper.tex','S6_06_BLIND_results.csv','S6_06_BLIND_report.md','S6_06_BLIND_references.bib',*expected]
files={name:{'bytes':(root/name).stat().st_size,'sha256':hashlib.sha256((root/name).read_bytes()).hexdigest()} for name in names}
record={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','checkpoint':12,
        'master_build':46,'master_pages':481,'registered_statements':225,
        'visual_reviewed_pages':54,'reviewed_contact_sheets':7,
        'new_statements':[f'P3K.{i}' for i in range(40,46)],
        'scope':'The six new proofs are in the master. K39 source-zero construction, regularization and endpoint comparisons remain in working notes with explicit uncomputed boundary/return obligations. All prior attempts and intermediate build45 review evidence remain included.',
        'files':files}
(root/'records/checkpoint12_ready.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
