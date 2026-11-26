#!/usr/bin/env python3
"""Retrieve the named helper solely to read the archived default-input rule."""
from pathlib import Path
from hashlib import sha256
from urllib.request import Request,urlopen
STORE=Path('/tmp/S6_SERIES_PUBLISH_c7_LN_historical')
url=('https://raw.githubusercontent.com/KokunoYumeto/s6-complex-structure-workbench/'
     'a02f2eacf5a8c3db7cf8cdfcdba50c0002ee91c7/pro_returns/'
     'S6_10_PAPERS_checkpoint_15_20261119T1045Z/S6_10_PAPERS/code/III/'
     'manifolds_weighted_profiles.py')
with urlopen(Request(url,headers={'User-Agent':'S6-LN-default-input-reading'}),timeout=30) as f: raw=f.read()
p=STORE/'S6_SERIES_PUBLISH_manifolds_weighted_profiles.py'
with p.open('xb') as f:f.write(raw)
print('SUCCESS',url,'LOCAL',p,'SHA256',sha256(raw).hexdigest(),'BYTES',len(raw),'LINES',len(raw.splitlines()),flush=True)
print('SCOPE saved source for bounded reading of default_finite input choice only; not imported or executed.',flush=True)
