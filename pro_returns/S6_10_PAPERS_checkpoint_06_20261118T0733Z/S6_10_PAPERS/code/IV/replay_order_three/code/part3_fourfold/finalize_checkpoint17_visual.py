from pathlib import Path
from datetime import datetime,timezone
import json
root=Path(__file__).resolve().parents[2]
meta=json.loads((root/'records/typesetting_checkpoint17.json').read_text())
contacts={str(i):meta['contact_sheets'][str(i)] for i in [3,4,5]}
pages=[p for ps in contacts.values() for p in ps]
assert len(pages)==24 and len(set(pages))==24
out={'utc':datetime.now(timezone.utc).isoformat(),'reviewer':'fourfold',
     'checkpoint':17,'master_build':57,'status':'PASS',
     'contact_sheets':contacts,'pages_reviewed':pages,'page_count_reviewed':24,
     'full_size_pages':[294,349,350],
     'findings':['All three assigned contact sheets were directly inspected.',
       'No clipping, collisions, missing symbols, broken table rules, or malformed displayed equations were observed.',
       'The dense source-profile table on page294, corrected characteristic-pair equations on349, and physical/dual-line transfer and correction notice on350 were also inspected at full size.',
       'Historical-statement correction notices and the preserved earlier arguments remain visually distinct and within the page boundaries.']}
(root/'records/checkpoint17_visual_fourfold.json').write_text(json.dumps(out,indent=2)+'\n')
with (root/'records/literature_fourfold.md').open('a') as f:
    f.write('\n## '+out['utc']+'\n- Source: master57 checkpoint17 contact sheets3–5, full pages294/349/350, and typesetting_checkpoint17.json.\n- Reason: direct checkpoint visual QA.\n- Material taken: page mappings, visible layout and corrected-formula rendering only; no new mathematical claim.\n')
print(json.dumps({'status':'PASS','pages':24,'full_size_pages':[294,349,350]}))
