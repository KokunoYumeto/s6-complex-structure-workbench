#!/usr/bin/env python3
"""Read back existing transition matrices, without a new mathematical test."""
from datetime import datetime, timezone
from hashlib import sha256
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
LANE=ROOT/'agents/continuation7_iii_star_logs_receiving'
P='S6_SERIES_PUBLISH_III_02LQ_'
path=LANE/(P+'post_exposure_data_v2.json')
data=json.loads(path.read_text())['marking_transitions']
assert len(data)==12
out=['# Exact LQ basis-transition readback','',
     'Recorded UTC: '+datetime.now(timezone.utc).isoformat()+'.','',
     'Source: `'+path.name+'`, SHA256 `'+sha256(path.read_bytes()).hexdigest()+'`.','',
     'These are the twelve previously generated and validated transition pairs, read back verbatim from their saved integer arrays. No new arithmetic computation is performed here. For historical basis C and frozen fresh basis H, new_to_old = C^{-1}H and old_to_new = H^{-1}C. Columns are coordinates; both maps preserve the marked delta and induce the identity on the x,w fibre quotient. The v2 program already checked both inverse products and the monodromy and quotient equations.','']
for row in data:
    out += ['## '+str(row['name']),'']
    for key in ('new_to_old','old_to_new'):
        out += ['`'+key+'`','',r'\[',r'\begin{pmatrix}']
        out += [' & '.join(map(str,line))+(r' \\' if i<3 else '') for i,line in enumerate(row[key])]
        out += [r'\end{pmatrix}',r'\]','']
body='\n'.join(out)+'\n'
target=LANE/(P+'basis_transition_readback.md')
assert not target.exists()
target.write_text(body)
print(body,end='')
print('READBACK_SHA256',sha256(body.encode()).hexdigest())
