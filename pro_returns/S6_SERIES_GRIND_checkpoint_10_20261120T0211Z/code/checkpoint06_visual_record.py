"""Collect actual image receipts without treating old PDF hashes as current views."""
from pathlib import Path
import datetime,hashlib,json
R=Path(__file__).resolve().parents[1]
sources={
'I':['audit_paper_i/build22_I_changed_visual_QA.json'],
'II':['audit_root/build23_II_changed_visual_QA.json'],
'III':['audit_root/build23_III_changed_visual_QA.json'],
'IV':['audit_root/build22_IV_visual_QA.json','audit_sign/build22_IV_visual_QA.json','audit_root/build23_IV_locator_visual_QA.json'],
'V':['audit_paper_i/build23_V_changed_visual_QA.json']}
all_receipts={};aggregate={}
for paper,paths in sources.items():
    items=[];pages=set()
    for name in paths:
        p=R/name;d=json.loads(p.read_text());items.append(dict(path=name,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),receipt=d))
        for k in ['pages','viewed_pages','actual_pages','inspected_pages','rendered_pages']:
            value=d.get(k,[])
            if isinstance(value,list):pages.update(x for x in value if isinstance(x,int))
        for sheet in d.get('sheets',[]):pages.update(sheet.get('pages',[]))
    all_receipts[paper]=items
    aggregate[paper]=dict(rendered_pages=sorted(pages),pdf_sha256=hashlib.sha256((R/f'S6_SERIES_GRIND_{paper}.pdf').read_bytes()).hexdigest(),inspection_state='Actual image inspections are individually identified in analysis/checkpoint06_visual_receipts.json by their own PDF/image hashes. The PDF hash here identifies the current file only; no later recompilation is represented as a new image inspection. Earlier spread samples remain in their original receipts.',receipts=paths)
(R/'analysis/checkpoint06_visual_receipts.json').write_text(json.dumps(dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),papers=all_receipts),indent=2)+'\n')
(R/'analysis/rendered_qa.json').write_text(json.dumps(aggregate,indent=2)+'\n')
print(json.dumps({p:len(v['rendered_pages']) for p,v in aggregate.items()}))
