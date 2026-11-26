"""Admit the 43 reviewed source-stage front/methodology unit closures.

The five dynamic Methodology rows and every D23 image row remain open.
This reads the exact per-key proposal; it creates no new unit or check event.
"""
from pathlib import Path
from datetime import datetime,timezone
import csv
import re

ROOT=Path(__file__).resolve().parents[1]
plan_name='agents/continuation4_reductions/S6_SERIES_PUBLISH_c4_remaining_nonD23_closure_plan.md'
plan=(ROOT/plan_name).read_text()
proposed={}
for line in plan.splitlines():
    cells=[x.strip() for x in line.split('|')[1:-1]]
    if len(cells)==4 and re.fullmatch(r'`[^`]+`',cells[0]) and re.fullmatch(r'D\d+',cells[1]):
        key=(cells[0].strip('`'),'defect',cells[1])
        assert key not in proposed
        proposed[key]=cells[2]+' '+cells[3]
    if len(cells)==3 and cells[2].startswith('Source-clear'):
        m=re.fullmatch(r'(D\d+|—) / (defect|structure)',cells[0])
        if m:
            key=('methodology',m[2],'' if m[1]=='—' else m[1])
            assert key not in proposed
            proposed[key]=cells[1]+' '+cells[2]
assert len(proposed)==43,len(proposed)
path=ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv'
csv.field_size_limit(100000000)
with path.open() as f:
    reader=csv.DictReader(f,delimiter='\t'); fields=reader.fieldnames; rows=list(reader)
index={(r['unit_id'],r['row_kind'],r['defect_type']):r for r in rows if r['paper']=='II'}
assert all(index[key]['status']=='open' for key in proposed)
unchanged=[r.copy() for r in rows if r['paper']!='II' or (r['unit_id'],r['row_kind'],r['defect_type']) not in proposed]
stamp=datetime.now(timezone.utc).isoformat()
for key,detail in proposed.items():
    row=index[key]
    row['status']='done';row['date_utc']=stamp
    row['evidence']+='; '+plan_name
    row['detail']+=' Fourth-continuation source-stage closure: '+detail+' Root read the complete 48-row plan and exact final source-stage mappings. The underlying admitted full-proof comparisons and the new first-part reading retain their actual scopes. Dynamic record reconciliation and the current rendered-image findings remain in their separate open rows; no new mathematical check or independence is inferred.'
assert [r for r in rows if r['paper']!='II' or (r['unit_id'],r['row_kind'],r['defect_type']) not in proposed]==unchanged
with path.open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n')
    writer.writeheader();writer.writerows(rows)
remaining=[r for r in rows if r['paper']=='II' and r['status']=='open']
assert len(remaining)==216
assert sum(r['defect_type']=='D23' for r in remaining)==211
assert {(r['unit_id'],r['defect_type']) for r in remaining if r['defect_type']!='D23'}=={('methodology',d) for d in ['D09','D15','D18','D24','D25']}
print('Closed 43 reviewed source-stage rows. Remaining: 211 D23 rows and five dynamic Methodology rows.')
