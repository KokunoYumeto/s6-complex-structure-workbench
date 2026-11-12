#!/usr/bin/env python3
"""Assemble bibliography and the machine-readable statement ledger.

This script does not write mathematical claims. It consolidates the inspected
metadata and checks every claim ID against the actual paper fragments.
"""
import csv
import json
import re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
out=ROOT/'outputs'
bibs=[out/'root_references.bib',out/'part_A_references.bib',out/'part_C_references.bib']
if (out/'part_D_references.bib').exists():
    bibs.append(out/'part_D_references.bib')
combined='\n\n'.join(p.read_text(encoding='utf-8').rstrip() for p in bibs)+'\n'
keys=re.findall(r'@\w+\{([^,]+),',combined)
assert len(keys)==len(set(keys)), 'Duplicate bibliography key'
assert len(re.findall(r'(?i)verified',combined))>=len(keys), 'Missing verification labels'
(ROOT/'S6_01_INVARIANTS_references.bib').write_text(combined,encoding='utf-8')

rows=[]
for p in sorted(out.glob('part_*_statements.json')):
    rows.extend(json.loads(p.read_text(encoding='utf-8')))
for row in rows:
    row['item_of_the_prompt']=';'.join(t.strip() for t in row['item_of_the_prompt'].split(';'))
byid={r['id']:r for r in rows}
assert len(byid)==len(rows), 'Duplicate statement ID'
tex='\n'.join(p.read_text(encoding='utf-8') for p in sorted((ROOT/'fragments').glob('part_*.tex')))
claims=re.findall(r'\\begin\{claim\}\{([^}]+)\}\{([^}]+)\}',tex)
assert len(claims)==len(set(i for i,s in claims)), 'Duplicate claim ID in paper'
missing=[i for i,s in claims if i not in byid]
extra=sorted(set(byid)-{i for i,s in claims})
assert not missing and not extra,(missing,extra)
allowed={'Proved','Refuted','Known','Open'}
for i,s in claims:
    assert s in allowed,(i,s)
    assert byid[i]['status']==s,(i,s,byid[i]['status'])
ordered=[byid[i] for i,s in claims]
fields=['id','statement','status','where_proved','depends_on','item_of_the_prompt',
        'findings_of_the_survey_settled (F-numbers)','notes']
with (ROOT/'S6_01_INVARIANTS_results.csv').open('w',newline='',encoding='utf-8') as f:
    writer=csv.DictWriter(f,fieldnames=fields)
    writer.writeheader()
    for row in ordered:
        row=dict(row)
        if 'findings_of_the_survey_settled' in row:
            row['findings_of_the_survey_settled (F-numbers)']=row.pop('findings_of_the_survey_settled')
        writer.writerow(row)
items=[f'{p}.{j}' for p,n in [('A',4),('B',3),('C',3),('D',4),('E',2)] for j in range(1,n+1)]
coverage={item:[r['id'] for r in ordered if item in r['item_of_the_prompt'].split(';')] for item in items}
assert all(coverage.values()),coverage
(out/'prompt_coverage.json').write_text(json.dumps(coverage,indent=2)+'\n')
print(f'Bibliography: {len(keys)} verified entries.')
print(f'Statements: {len(ordered)}; all IDs and exact status labels match.')
for item,ids in coverage.items(): print(item,','.join(ids))
