from pathlib import Path
from datetime import datetime, timezone
import json

root = Path(__file__).resolve().parents[2]
typesetting = json.loads((root/'records/typesetting_checkpoint16.json').read_text())
contacts = {str(i):typesetting['contact_sheets'][str(i)] for i in range(17,23)}
pages = [p for v in contacts.values() for p in v]
assert typesetting['master_build'] == 54
assert len(pages) == 48 and len(set(pages)) == 48
record = {
    'utc':datetime.now(timezone.utc).isoformat(),
    'master_build':54,'status':'PASS','reviewer':'fourfold',
    'contact_sheets':contacts,'page_count_reviewed':48,
    'full_size_pages':[469,475], 'findings':[],
    'observations':[
        'Directly inspected all six contact sheets 17 through 22, covering all 48 assigned master pages.',
        'Directly inspected full-size pages 469 and 475, including the K68 physical/Thom statement and K66 corrected pair/sign displays.',
        'The correction notices on the reviewed historical statements, the complete K65 seam table, K68 anti-linear and inverse-clutch maps, and K66/K67 formula displays are legible.',
        'No clipped content, colliding elements, missing symbols or malformed equations were observed.'
    ]
}
(root/'records/checkpoint16_visual_fourfold.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'status':'PASS','pages':48,'full_size':[469,475],'master_build':54},indent=2))
