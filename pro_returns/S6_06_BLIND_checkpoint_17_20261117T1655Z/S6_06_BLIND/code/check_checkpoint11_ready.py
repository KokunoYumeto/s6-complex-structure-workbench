"""Verify the immutable master/report pair prepared for checkpoint11."""
from datetime import datetime, timezone
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
    results=list(csv.DictReader(f))
assert len(results)==len({r['id'] for r in results})==219
with fitz.open(root/'S6_06_BLIND_paper.pdf') as pdf:
    assert len(pdf)==456
report=(root/'S6_06_BLIND_report.md').read_text()
assert report.startswith('INCOMPLETE')
assert 'Checkpoint 11 contained 456 manuscript pages.' in report
assert 'Next check: 2026-11-17T11:49:44+00:00.' in report
qa=json.loads((root/'records/typesetting_checkpoint11.json').read_text())
assert qa['overfull_over_2pt']==0 and qa['max_overfull_pt']<2
assert qa['visual_reviewed_page_count']==311
assert qa['contact_sheets_reviewed']==39
names=['S6_06_BLIND_paper.pdf','S6_06_BLIND_paper.tex','S6_06_BLIND_results.csv','S6_06_BLIND_report.md','S6_06_BLIND_references.bib',*expected]
files={name:{'bytes':(root/name).stat().st_size,'sha256':hashlib.sha256((root/name).read_bytes()).hexdigest()} for name in names}
record={
 'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS',
 'checkpoint':11,'master_build':44,'master_pages':456,'registered_statements':219,
 'visual_reviewed_pages':311,'reviewed_contact_sheets':39,
 'scope':'The current master and results register contain the four newly promoted K37,K38,F55,F56 results. K39 and K40 work produced after this master is retained in its separate working notes, certificates and audit records; incorporation awaits the next build.',
 'files':files
}
(root/'records/checkpoint11_ready.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
