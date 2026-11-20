"""Apply the reviewed explicit low-F hypotheses and exact notation repairs."""
from pathlib import Path
import re,json,hashlib
R=Path(__file__).resolve().parents[1]
p=R/'parts/IV.body.linked.tex';old=p.read_text();new=old
patches=json.loads((R/'audit_corrections/IV_low_F_scope_and_residual_patches.json').read_text())
for patch in patches:
 label=r'\label{'+patch['label']+'}'
 assert new.count(label)==1,patch['label']
 start=new.index(label);end=new.index(r'\end{proof}',start)+len(r'\end{proof}')
 block=new[start:end];assert block.count(patch['old_text'])==1,patch['label']
 block=block.replace(patch['old_text'],patch['new_text'])
 new=new[:start]+block+new[end:]
for macro in ['label','tag']:
 pattern=r'\\'+macro+r'\{[^}]+\}'
 assert re.findall(pattern,old)==re.findall(pattern,new),macro
for env in ['proof','enumerate']:
 assert new.count(r'\begin{'+env+'}')==new.count(r'\end{'+env+'}'),env
p.write_text(new)
(R/'analysis/IV_low_F_scope_changes_05.json').write_text(json.dumps({'changes':patches,'before_sha256':hashlib.sha256(old.encode()).hexdigest(),'after_sha256':hashlib.sha256(new.encode()).hexdigest(),'equation_tags_and_labels_preserved_in_order':True,'scope_review':'Each newly stated choice is an input already used in the full corresponding proof. All previous claim conclusions remain; the source, line, parameter, fan and boundary maps are now stated locally.'},indent=2)+'\n')
print(json.dumps({'patches_applied':len(patches),'tags_and_labels_preserved':True}))
