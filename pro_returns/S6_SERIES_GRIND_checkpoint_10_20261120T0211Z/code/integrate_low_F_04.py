"""Apply six reviewed source-credit/computation paragraphs with exact receipts."""
from pathlib import Path
import json,re,hashlib

R=Path(__file__).resolve().parents[1]
path=R/'parts/IV.body.linked.tex'
old=path.read_text();new=old
patches=json.loads((R/'audit_corrections/IV_low_F_computation_patches.json').read_text())
receipts=[]
for patch in patches:
    before=patch['old_text'];after=patch['new_text']
    assert new.count(before)==1,(patch['label'],new.count(before))
    new=new.replace(before,after)
    receipts.append(patch)
for macro in ['tag','label']:
    pattern=r'\\'+macro+r'\{([^}]+)\}'
    assert re.findall(pattern,old)==re.findall(pattern,new),macro
for env in ['proof','enumerate']:
    assert new.count(r'\begin{'+env+'}')==new.count(r'\end{'+env+'}'),env
path.write_text(new)
(R/'analysis/IV_low_F_changes_04.json').write_text(json.dumps({'changes':receipts,'before_sha256':hashlib.sha256(old.encode()).hexdigest(),'after_sha256':hashlib.sha256(new.encode()).hexdigest(),'all_equation_tags_and_labels_preserved_in_order':True},indent=2)+'\n')
print(json.dumps({'applied':len(receipts),'equation_tags_and_labels_preserved':True}))
