#!/usr/bin/env python3
"""Record the assigned direct master51 visual inspection."""
from pathlib import Path
from datetime import datetime,timezone
import json
ROOT=Path(__file__).resolve().parents[2]
now=datetime.now(timezone.utc).isoformat()
with (ROOT/'records/literature_fourfold.md').open('a') as log:
 log.write('\n- '+now+' — Opened checkpoint15 contact sheets 9–12 and full-size pages 400,410,416, plus typesetting_checkpoint15.json. Reason: direct final master51 visual QA. Material: the complete assigned 32 pages, dense fan and Tate displays, statement openings, correction notices and page boundaries.\n')
t=json.loads((ROOT/'records/typesetting_checkpoint15.json').read_text())
c={str(i):t['contact_sheets'][str(i)] for i in range(9,13)}
assert sum(map(len,c.values()))==32 and t['master_build']==51
r=dict(utc=now,status='PASS',master_build=51,reviewer='fourfold',
 contact_sheets=c,page_count_reviewed=32,full_size_pages=[400,410,416],
 findings=['All four assigned contact sheets directly reviewed, covering all 32 assigned pages.',
 'Dense pages 400,410,416 additionally inspected at full size.',
 'No clipping, collisions, malformed equation, missing symbol, orphan heading, or bad page boundary found.',
 'K57 exact fan and Tate displays, K58 statement table, and the refreshed narrow K62 dependency paragraph are legible.',
 'The corrected statement opening on page349 is visibly distinguished and fits cleanly.'])
(ROOT/'records/checkpoint15_visual_fourfold.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps(r,indent=2))
