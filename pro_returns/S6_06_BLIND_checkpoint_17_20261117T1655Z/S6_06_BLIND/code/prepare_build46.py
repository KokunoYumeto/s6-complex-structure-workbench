"""Preserve build45 review evidence, then register the audited K45 proof."""
from pathlib import Path
import shutil
import json
from datetime import datetime,timezone

root=Path(__file__).resolve().parents[1]
dest=root/'records/checkpoint12_build45'
dest.mkdir(exist_ok=True)
names=['S6_06_BLIND_paper.pdf','S6_06_BLIND_paper.log','S6_06_BLIND_paper.tex',
       'records/typesetting_checkpoint12.json','records/page_boundaries_checkpoint12.json',
       'records/checkpoint12_visual_root.json','records/checkpoint12_visual_checks.json',
       'records/checkpoint12_visual_blind.json','records/finalize_checkpoint12_qa.out',
       'records/checkpoint12_audit_checkpoint_pdf.out']
for name in names:
    shutil.copy2(root/name,dest/Path(name).name)
shutil.copytree(root/'records/render_checkpoint12',dest/'rendered_pages',dirs_exist_ok=True)
(dest/'preservation.json').write_text(json.dumps({
    'utc':datetime.now(timezone.utc).isoformat(),'master_build':45,
    'reason':'K45 was proved and independently audited before the hourly deadline; a fresh master and full required visual sample are being prepared.',
    'original_files':names,
    'render_copy':'records/render_checkpoint12 -> records/checkpoint12_build45/rendered_pages',
    'scope':'This is retained intermediate review evidence inside the hourly deliverable, not an additional checkpoint ZIP.'
},indent=2)+'\n')
p=root/'notes/part3.tex'
s=p.read_text()
entry='\\input{notes/part3_source_cusp_reflection.tex}'
assert entry not in s
p.write_text(s+'\n'+entry+'\n')
p=root/'code/audit_checkpoint12_pdf.py'
s=p.read_text().replace('range(40,45)','range(40,46)').replace("'master_build':45","'master_build':46").replace('five newly incorporated proofs','six newly incorporated proofs')
p.write_text(s)
print('Preserved build45 and its complete review; included K45 for build46.')
