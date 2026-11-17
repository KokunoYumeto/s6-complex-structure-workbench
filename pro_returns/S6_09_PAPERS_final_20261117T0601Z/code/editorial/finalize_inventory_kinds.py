"""Make the inventory kind describe the statement actually printed."""
from pathlib import Path
import csv,json,zipfile

OUT=Path(__file__).resolve().parents[2]
p=OUT/'S6_09_PAPERS_inventory.csv'
with p.open(newline='') as f:
    reader=csv.DictReader(f);fields=reader.fieldnames;rows=list(reader)
corrections={('S6_01_INVARIANTS','A4.2'),('S6_02_FAMILY','B.2.3'),
             ('S6_04_MAPS_MANIFOLDS','A.1.2'),('S6_05_ARITHMETIC','C.8.9')}
changes=[]
for r in rows:
    k=(r['source_run'],r['source_id']);old=r['kind']
    if r['kind']=='Counterexample or correction':
        r['kind']='Correction' if k in corrections else 'Counterexample'
    if k in {('S6_02_FAMILY','C.3.3'),('S6_02_FAMILY','E.1.5')}:
        r['kind']='Proved local obstruction; resolved source question'
        r['check_outcome']='Passed. The entire local obstruction is retained and its question is answered by the complete later PUSH argument in the same paper; it is not an outstanding open question.'
    if k==('S6_02_PUSH','A.3.2'):r['kind']='Counterexample'
    if k==('S6_05_ARITHMETIC','C.7.4'):r['kind']='Conditional theorem'
    if k==('S6_05_ARITHMETIC','C.7.5'):r['kind']='Computational diagnostic'
    if r['kind'] in ['test','auditrecord']:
        r['kind']='Verification record' if r['kind']=='auditrecord' else 'Verification with proved assertions'
    if r['paper']=='I' and r['kind']=='Open problem':r['kind']='Open question with complete partial proof'
    if old!=r['kind']:changes.append({'source_run':k[0],'source_id':k[1],'from':old,'to':r['kind']})
with p.open('w',newline='') as f:
    w=csv.DictWriter(f,fields);w.writeheader();w.writerows(rows)
record=OUT/'records/inventory_kind_corrections.json'
history=json.loads(record.read_text()) if record.exists() else []
checkpoint=OUT.parent/'S6_09_PAPERS_checkpoint_02.zip'
if checkpoint.exists():
    with zipfile.ZipFile(checkpoint) as z:
        name='records/inventory_kind_corrections.json'
        if name in z.namelist():history=json.loads(z.read(name))+history
merged=[];seen=set()
for x in history+changes:
    key=json.dumps(x,sort_keys=True)
    if key not in seen:seen.add(key);merged.append(x)
record.write_text(json.dumps(merged,indent=2)+'\n')
print('Inventory kind corrections:',len(changes))
