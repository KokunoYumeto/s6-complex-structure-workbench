"""Apply reviewed local formula, source-credit, and prose patches with receipts."""
from pathlib import Path
import json,re,hashlib

R=Path(__file__).resolve().parents[1]
path=R/'parts/IV.body.linked.tex'
old=path.read_text();new=old
files=['IV_low_F_final_format_patches.json','IV_low_F_workflow_patches.json']
receipts=[]
for name in files:
    for patch in json.loads((R/'audit_corrections'/name).read_text()):
        before=patch['old_text'];after=patch['new_text']
        assert new.count(before)==1,(patch['label'],new.count(before),before)
        new=new.replace(before,after)
        receipts.append(dict(patch,proposal_file=name))
for macro in ['tag','label']:
    pattern=r'\\'+macro+r'\{([^}]+)\}'
    assert re.findall(pattern,old)==re.findall(pattern,new),macro
for env in ['proof','enumerate']:
    assert new.count(r'\begin{'+env+'}')==new.count(r'\end{'+env+'}'),env
path.write_text(new)
(R/'analysis/IV_low_F_format_changes_04.json').write_text(json.dumps({'changes':receipts,'before_sha256':hashlib.sha256(old.encode()).hexdigest(),'after_sha256':hashlib.sha256(new.encode()).hexdigest(),'all_equation_tags_and_labels_preserved_in_order':True},indent=2)+'\n')
print(json.dumps({'applied':len(receipts),'equation_tags_and_labels_preserved':True}))
