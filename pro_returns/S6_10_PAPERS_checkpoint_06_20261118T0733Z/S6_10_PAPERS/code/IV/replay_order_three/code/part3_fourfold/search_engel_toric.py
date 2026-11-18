#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime,timezone
import re
ROOT=Path(__file__).resolve().parents[2]
p=ROOT.parent/'background/papers/arXiv_2609.38442_Engel_src/S6.tex'
lines=p.read_text().splitlines()
pat=re.compile(r'Mumford|Kulikov|polyhedral|triangulat|properly|period matrix',re.I)
hits=[(i+1,s) for i,s in enumerate(lines) if pat.search(s)]
with (ROOT/'records/literature_fourfold.md').open('a') as f:
    f.write('\n- '+datetime.now(timezone.utc).isoformat()+' — Searched supplied Engel S6.tex for Mumford/Kulikov/triangulation/proper-action construction. Reason: determine the exact periodic toric quotient theorem usable for the rescaled K39 source collision. Material: construction locators and matching lines only; no forbidden fourfold tangent/aut material.\n')
for i,s in hits: print(f'{i}: {s}')
