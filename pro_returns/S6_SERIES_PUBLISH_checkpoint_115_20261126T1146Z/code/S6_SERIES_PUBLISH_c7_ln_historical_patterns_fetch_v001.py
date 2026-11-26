#!/usr/bin/env python3
"""Fetch the exact archived input, retaining only the 30 LN-reference rows in W.

The complete JSON is parsed to index its patterns; only the explicitly named
LN-overlap rows are printed/read. No imported historical program is executed.
"""
from pathlib import Path
from hashlib import sha256
from urllib.request import Request,urlopen
import json
ROOT=Path.cwd()
STORE=Path('/tmp/S6_SERIES_PUBLISH_c7_LN_historical')
BASE=('https://raw.githubusercontent.com/KokunoYumeto/s6-complex-structure-workbench/'
      'a02f2eacf5a8c3db7cf8cdfcdba50c0002ee91c7/pro_returns/'
      'S6_10_PAPERS_checkpoint_15_20261119T1045Z/S6_10_PAPERS/code/III/')
name='manifolds_original_multiplicative.json'
url=BASE+name
with urlopen(Request(url,headers={'User-Agent':'S6-LN-exact-overlap-input'}),timeout=30) as f:
    raw=f.read()
p=STORE/('S6_SERIES_PUBLISH_'+name)
with p.open('xb') as f:f.write(raw)
data=json.loads(raw)
audit=json.loads((STORE/'S6_SERIES_PUBLISH_manifolds_general_initial_audit.json').read_text())
ids=sorted(set(r['pattern'] for r in audit['old_overlap']))
assert len(ids)==30 and len(data['patterns'])==495
selected=[dict(index=i,pattern=data['patterns'][i]) for i in ids]
output=ROOT/'agents/continuation7_iii_general_initial_receiving/S6_SERIES_PUBLISH_III_02LN_historical_overlap_inputs.json'
with output.open('x') as f:json.dump(selected,f,indent=2);f.write('\n')
print('SUCCESS',url,'LOCAL',p,'SHA256',sha256(raw).hexdigest(),'BYTES',len(raw),flush=True)
for item in selected:print(json.dumps(item,sort_keys=True),flush=True)
print('SCOPE complete495-pattern JSON parsed; exactly30 LN-reference rows extracted and printed; other pattern records not manually read; no historical algorithm execution.',flush=True)
