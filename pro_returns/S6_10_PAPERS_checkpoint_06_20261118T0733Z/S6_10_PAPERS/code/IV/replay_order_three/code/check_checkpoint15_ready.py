"""Verify the corrected complete master and report for the hourly archive."""
from datetime import datetime,timezone
from pathlib import Path
from collections import Counter
import csv,hashlib,json
import fitz
root=Path(__file__).resolve().parents[1]
expected={
 'notes/part5.tex':'f7b2188bbd5fc453780421599b65168141c8ed09480b1396794f02f41a680e0f',
 'notes/part5_blind.md':'ffdac7780a3d5c35565e31e6bb1bebf459e0f7dc75355e19fc216b5ba4b9a1e4'
}
for name,digest in expected.items():
    assert hashlib.sha256((root/name).read_bytes()).hexdigest()==digest
rows=list(csv.DictReader((root/'S6_06_BLIND_results.csv').open()))
ids={r['id'] for r in rows}
assert len(rows)==len(ids)==243
assert all(f'P3K.{i}' in ids for i in range(40,64))
assert 'P3K.39' not in ids
corrections=json.loads((root/'records/scalar_fan_correction_scope.json').read_text())['scope']
byid={r['id']:r for r in rows}
assert len(corrections)==14
assert all(byid[sid]['status']=='Open' for sid in corrections)
with fitz.open(root/'S6_06_BLIND_paper.pdf') as pdf:
    page_count=len(pdf)
report=(root/'S6_06_BLIND_report.md').read_text()
assert report.startswith('INCOMPLETE')
assert f'Checkpoint 15 contained {page_count} manuscript pages.' in report
assert 'Next check: 2026-11-17T15:49:44+00:00.' in report
assert 'newly located proof error' in report and 'P3K.63' in report
qa=json.loads((root/'records/typesetting_checkpoint15.json').read_text())
assert qa['master_build']==51 and qa['pages']==page_count
assert qa['visual_reviewed_page_count']==len(qa['rendered_pages'])
assert qa['contact_sheets_reviewed']==len(qa['contact_sheets'])
assert qa['overfull_over_2pt']==0 and qa['max_overfull_pt']<2
names=['S6_06_BLIND_paper.pdf','S6_06_BLIND_paper.tex',
       'S6_06_BLIND_results.csv','S6_06_BLIND_report.md',
       'S6_06_BLIND_references.bib',*expected]
files={name:{'bytes':(root/name).stat().st_size,
 'sha256':hashlib.sha256((root/name).read_bytes()).hexdigest()} for name in names}
record={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','checkpoint':15,
 'master_build':51,'master_pages':page_count,'registered_statements':len(rows),
 'statement_status_counts':dict(Counter(r['status'] for r in rows)),
 'visual_reviewed_pages':qa['visual_reviewed_page_count'],
 'reviewed_contact_sheets':qa['contact_sheets_reviewed'],
 'new_statements':[f'P3K.{i}' for i in range(57,64)],
 'reopened_compound_statements':sorted(corrections),
 'scope':'Seven new complete proofs are included. Fourteen earlier compound scalar-fan assertions are explicitly reopened after a located product/outer-line error; their prior texts are preserved. The narrow C2 comparison repairs the new infinity/groupoid dependence. Source-zero individual values and the remaining integer fixed-star index are open. Original blind Part5 is unchanged.',
 'next_checkpoint_scheduler_pty':46917,'files':files}
(root/'records/checkpoint15_ready.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
