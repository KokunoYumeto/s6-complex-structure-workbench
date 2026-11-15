"""Correct one duplicated article introduced by the status reconciliation."""
from pathlib import Path
import json

root=Path(__file__).resolve().parents[1]
paths=[
 root/'sections/B_analytic_comparison_audit.tex',
 root/'code/ab_push_final_status_cleanup.py',
 root/'sections/ab_push_final_status_audit.md',
 root/'evidence/ab_push_final_status_audit.json'
]
before='an unrestricted proof needs additional information beyond a'
after='unrestricted proof needs additional information beyond a'
records=[]
for p in paths:
    text=p.read_text()
    assert text.count(before)==1,(p,text.count(before))
    p.write_text(text.replace(before,after,1))
    records.append({'file':str(p.relative_to(root)),'before':before,'after':after})
(root/'evidence/ab_push_final_status_grammar.json').write_text(json.dumps(records,indent=2)+'\n')
print('PASS: removed duplicated article in the current source, reproducibility script and both audit renderings.')
print('No mathematical claim, status, scope, historical report or referee was changed.')
