#!/usr/bin/env python3
"""Retrieve original LM mathematical outputs; no target algorithm execution."""
from hashlib import sha256
from pathlib import Path
from urllib.request import Request, urlopen
import json

BASE = ('https://raw.githubusercontent.com/KokunoYumeto/'
        's6-complex-structure-workbench/'
        'a02f2eacf5a8c3db7cf8cdfcdba50c0002ee91c7/'
        'pro_returns/S6_10_PAPERS_checkpoint_15_20261119T1045Z/'
        'S6_10_PAPERS/code/III/')
DEST = Path('/tmp/S6_SERIES_PUBLISH_c7_LM_historical')
DEST.mkdir(exist_ok=True)
for name in ('maps_D2_II_frame_checks.json','fourfolds_D2_remaining_AH.json',
             'manifolds_extended_critical_cycles.json',
             'manifolds_extended_critical_symbolic.json'):
    url=BASE+name
    data=urlopen(Request(url,headers={'User-Agent':'S6-series-source-audit'}),
                 timeout=40).read()
    parsed=json.loads(data)
    target=DEST/('S6_SERIES_PUBLISH_'+name)
    target.write_bytes(data)
    print(json.dumps({'url':url,'path':str(target),'bytes':len(data),
                      'sha256':sha256(data).hexdigest(),
                      'top_keys':list(parsed)},sort_keys=True))
print('RETRIEVAL ONLY; historical algorithms not imported or executed')
