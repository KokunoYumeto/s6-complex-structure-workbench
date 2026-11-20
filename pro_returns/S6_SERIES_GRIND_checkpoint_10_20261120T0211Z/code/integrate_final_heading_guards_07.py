"""Apply seven reviewed presentation/dependency guards and retain exact receipts."""
from pathlib import Path
import datetime, hashlib, json, re
R=Path(__file__).resolve().parents[1]
packs=[('II','audit_sign/II_LR_sibling_item_guards_07.json',4),
       ('IV','audit_paper_i/closure_07/IV_exact_uses_patches.json',3)]
before={p:(R/f'parts/{p}.body.linked.tex').read_text() for p,_,_ in packs}
after=dict(before);receipts=[]
for paper,name,n in packs:
    f=R/name;data=json.loads(f.read_text());gs=data['guards'] if isinstance(data,dict) else data
    assert len(gs)==n
    for g in gs:
        old=g.get('old',g.get('old_text'));new=g.get('new',g.get('new_text'))
        assert after[paper].count(old)==1,(paper,g['label'])
        after[paper]=after[paper].replace(old,new,1)
    receipts.append({'paper':paper,'input':name,'sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'guards':gs})
for paper,s in after.items():
    assert re.findall(r'\\(?:tag|label)\{[^}]+\}',before[paper])==re.findall(r'\\(?:tag|label)\{[^}]+\}',s)
    (R/f'parts/{paper}.body.linked.tex').write_text(s)
out={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'guards':7,'receipts':receipts,
 'scope':'Four literal Step1–4 markers give the existing LR internal references their actual sibling proof items. Three IV uses fields now identify the exact separately reviewed geometric inputs, with K10 scope explicitly bounded. No theorem or mathematical proof text is removed.',
 'hashes':{p:{'before':hashlib.sha256(before[p].encode()).hexdigest(),'after':hashlib.sha256(after[p].encode()).hexdigest()} for p in after},
 'pending':'Assembly, build27 and actual changed-page inspection.'}
(R/'analysis/final_heading_guards_07.json').write_text(json.dumps(out,indent=2)+'\n')
qa=json.loads((R/'analysis/build26_root_IV_repaired_render.json').read_text())
assert hashlib.sha256((R/'S6_SERIES_GRIND_IV.pdf').read_bytes()).hexdigest()==qa['pdf_sha256']
qa.update({'inspection_state':'Root actually viewed both complete sheets','result':'PASS',
 'recorded_at_utc':out['utc'],'observations':'All five replaced paragraph controls display distinct hierarchical list labels. The complete I2P supporting-proof reference on page1314 now reads proof20, substep6 and fits fully. No clipping, missing glyphs or formula faults on the three listed pages.',
 'scope':'Exact three-page changed sample, not whole-PDF inspection.'})
(R/'audit_root/build26_IV_repaired_visual_QA.json').write_text(json.dumps(qa,indent=2)+'\n')
print(json.dumps({'guards':7,'IV_actual_view':qa['pages']}))
