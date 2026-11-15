"""Merge statement registers without altering contributors' source records."""
from pathlib import Path
import csv,json
root=Path(__file__).resolve().parents[1]
fields=['id','statement','status','where_proved','depends_on','item_of_the_prompt',
        'findings_of_the_survey_settled','notes']
rows=[]
for path in sorted((root/'records').glob('*results.csv')):
 with path.open(newline='') as f:
  for row in csv.DictReader(f):
   row['findings_of_the_survey_settled']=row.get('findings_of_the_survey_settled',row.get('findings_of_the_survey_settled (F-numbers)',''))
   rows.append({k:row.get(k,'') for k in fields})
ids=[r['id'] for r in rows]
assert len(ids)==len(set(ids)), 'duplicate numbered statements'
def key(row):
 p=row['id'].split('.')
 return (p[0],tuple(int(x) if x.isdigit() else x for x in p[1:]))
rows.sort(key=key)
with (root/'S6_04_MAPS_MANIFOLDS_results.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
print(json.dumps({'statements':len(rows),'source_registers':[p.name for p in sorted((root/'records').glob('*results.csv'))]},indent=2))
