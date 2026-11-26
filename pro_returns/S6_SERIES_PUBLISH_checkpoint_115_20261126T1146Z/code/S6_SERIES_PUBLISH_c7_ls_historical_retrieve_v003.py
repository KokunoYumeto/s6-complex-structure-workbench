"""Retrieve only the two explicitly imported LS matrix helpers.

They are retained byte-for-byte; later reading is confined to named
integer/bar definitions used by the sixteen authorized LS computations.
"""
from pathlib import Path
from urllib.request import Request, urlopen
from datetime import datetime, timezone
from hashlib import sha256

lane = Path('agents/continuation7_iii_vertical_correction_receiving')
base = ('https://raw.githubusercontent.com/KokunoYumeto/'
        's6-complex-structure-workbench/a02f2eacf5a8c3db7cf8cdfcdba50c0002ee91c7/'
        'pro_returns/S6_10_PAPERS_checkpoint_15_20261119T1045Z/S6_10_PAPERS/code/III/')
print('START', datetime.now(timezone.utc).isoformat(), flush=True)
for name in ('manifolds_rankone_families.py','manifolds_all_weighted_profiles.py'):
    url = base + name
    try:
        with urlopen(Request(url, headers={'User-Agent':'S6-series-source-audit'}), timeout=25) as response:
            blob=response.read()
        blob.decode()
        path=lane/('S6_SERIES_PUBLISH_'+name)
        with path.open('xb') as f:
            f.write(blob)
        print('SUCCESS',url,'PATH',path,'SHA256',sha256(blob).hexdigest(),
              'BYTES',len(blob),'LINES',len(blob.splitlines()),flush=True)
    except Exception as error:
        print('FAILED',url,type(error).__name__,str(error),flush=True)
print('COMPLETE',datetime.now(timezone.utc).isoformat(),flush=True)
