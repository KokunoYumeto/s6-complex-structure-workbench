#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime, timezone
import json
root=Path(__file__).resolve().parents[2]
data={
 'utc':datetime.now(timezone.utc).isoformat(),
 'master_build':46,
 'status':'PASS',
 'reviewer':'fourfold',
 'contact_sheets':{
    '5':[340,341,342,343,344,345,346,347],
    '6':[348,349,350,351,352,353,360,380]},
 'page_count_reviewed':16,
 'full_size_pages':[347,351,352],
 'findings':[
  'Directly inspected both contact sheets and all three requested full-size pages.',
  'No clipping, text/equation collisions, missing glyphs or malformed displays observed.',
  'New K45 statement and RF.1--RF.3 equations are legible and remain within the margins.',
  'The long cap exact sequences and OC.2--OC.4 displays on page347 render correctly.',
  'Dense matrix page360 remains inside the page frame at contact-sheet inspection.'
 ]
}
(root/'records/checkpoint12_visual_fourfold.json').write_text(
    json.dumps(data,indent=2)+'\n')
with (root/'records/literature_fourfold.md').open('a') as f:
 f.write('\n- '+data['utc']+' — Direct visual review of build46 '
         'records/render_checkpoint12/contact_5.png, contact_6.png, '
         'page_347.png, page_351.png, page_352.png. Reason: final '
         'checkpoint12 layout audit. Material:16 displayed master pages; '
         'no clipping, collisions, missing glyphs or malformed equations.\n')
print(json.dumps(data,indent=2))
