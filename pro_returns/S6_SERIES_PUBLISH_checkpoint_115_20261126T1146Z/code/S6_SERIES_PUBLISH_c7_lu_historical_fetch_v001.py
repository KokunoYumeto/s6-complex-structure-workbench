"""Retrieve only the individually released LU historical implementation.

No historical module is imported or executed. Its named dependencies remain
closed until their exact input scope is separately authorized.
"""
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
from urllib.request import urlopen

BASE = ('https://raw.githubusercontent.com/KokunoYumeto/'
        's6-complex-structure-workbench/'
        'a02f2eacf5a8c3db7cf8cdfcdba50c0002ee91c7/'
        'pro_returns/S6_10_PAPERS_checkpoint_15_20261119T1045Z/'
        'S6_10_PAPERS/code/III/')
NAME = 'manifolds_corrected_initial.py'
DESTINATION = Path('/tmp/S6_SERIES_PUBLISH_c7_LU_historical')
DESTINATION.mkdir(parents=True, exist_ok=True)
path = DESTINATION / ('S6_SERIES_PUBLISH_' + NAME)
print('START', datetime.now(timezone.utc).isoformat(), flush=True)
print('URL', BASE + NAME, flush=True)
with urlopen(BASE + NAME, timeout=45) as response:
    content = response.read()
    print('HTTP', response.status, flush=True)
assert content
if path.exists():
    assert path.read_bytes() == content
else:
    path.write_bytes(content)
print('FILE', path, 'BYTES', len(content), 'SHA256',
      sha256(content).hexdigest(), flush=True)
print('COMPLETE', datetime.now(timezone.utc).isoformat(), flush=True)
