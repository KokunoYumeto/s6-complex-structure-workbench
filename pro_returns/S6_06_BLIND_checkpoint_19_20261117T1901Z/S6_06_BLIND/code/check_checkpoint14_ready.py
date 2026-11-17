"""Verify the complete master/report pair for the fourteenth hourly archive."""
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
    rows=list(csv.DictReader(f))
ids={r['id'] for r in rows}
assert len(rows)==len(ids)==236
assert all(f'P3K.{i}' in ids for i in range(40,57))
assert 'P3K.39' not in ids and 'P3K.57' not in ids
with fitz.open(root/'S6_06_BLIND_paper.pdf') as pdf:
    assert len(pdf)==519
report=(root/'S6_06_BLIND_report.md').read_text()
assert report.startswith('INCOMPLETE')
assert 'Checkpoint 14 contained 519 manuscript pages.' in report
assert 'Next check: 2026-11-17T14:49:44+00:00.' in report
qa=json.loads((root/'records/typesetting_checkpoint14.json').read_text())
assert qa['master_build']==49 and qa['visual_reviewed_page_count']==46
assert qa['contact_sheets_reviewed']==6 and qa['overfull_over_2pt']==0
assert qa['max_overfull_pt']<2
names=['S6_06_BLIND_paper.pdf','S6_06_BLIND_paper.tex',
       'S6_06_BLIND_results.csv','S6_06_BLIND_report.md',
       'S6_06_BLIND_references.bib',*expected]
files={name:{'bytes':(root/name).stat().st_size,
             'sha256':hashlib.sha256((root/name).read_bytes()).hexdigest()}
       for name in names}
record={
 'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','checkpoint':14,
 'master_build':49,'master_pages':519,'registered_statements':236,
 'visual_reviewed_pages':46,'reviewed_contact_sheets':6,
 'new_statements':[f'P3K.{i}' for i in range(50,57)],
 'scope':'Seven complete new proofs are included. The source-zero global attachment remains open. The infinity partial-filling/excision proof and marked global groupoid are retained as separately audited working proofs, outside the numbered master. The original blind Part5 is unchanged.',
 'files':files
}
(root/'records/checkpoint14_ready.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
