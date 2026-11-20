"""Guarded application of fully read OS45 and canonical-ring format patches."""
from pathlib import Path
import json
R=Path(__file__).resolve().parents[1];receipt=[]
for paper,file in [('IV','audit_paper_i/iv_os45/execution_prose_patches.json'),('I','audit_paper_i/known_proof_patches.json')]:
    path=R/f'parts/{paper}.body.linked.tex';text=path.read_text()
    for patch in json.loads((R/file).read_text()):
        assert text.count(patch['old'])==1,(patch['id'],text.count(patch['old']))
        text=text.replace(patch['old'],patch['new'],1)
        receipt.append(dict(patch,paper=paper))
    path.write_text(text)
(R/'analysis/agent_format_changes_03.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({'changes':len(receipt)}))
