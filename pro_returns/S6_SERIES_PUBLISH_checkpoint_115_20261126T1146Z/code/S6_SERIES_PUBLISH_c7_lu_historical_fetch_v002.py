"""Retrieve the released LU audit and extract only its authorized following gap."""
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
from urllib.request import urlopen

ROOT = Path(__file__).resolve().parents[1]
LANE = ROOT / 'agents/continuation7_iii_corrected_initial_receiving'
BASE = ('https://raw.githubusercontent.com/KokunoYumeto/'
        's6-complex-structure-workbench/'
        'a02f2eacf5a8c3db7cf8cdfcdba50c0002ee91c7/'
        'pro_returns/S6_10_PAPERS_checkpoint_15_20261119T1045Z/'
        'S6_10_PAPERS/code/III/')
NAME = 'manifolds_corrected_initial_audit.py'
STORE = Path('/tmp/S6_SERIES_PUBLISH_c7_LU_historical')
print('START', datetime.now(timezone.utc).isoformat(), flush=True)
raw = (ROOT / 'S6_SERIES_PUBLISH_III.tex').read_bytes()
assert sha256(raw).hexdigest() == '9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0'
auxiliary = b''.join(raw.splitlines(keepends=True)[21442:21457])
target = LANE / 'S6_SERIES_PUBLISH_III_02LU_released_following_auxiliary.tex'
assert not target.exists()
target.write_bytes(auxiliary)
print('EXACT_AUXILIARY_LINES 21443--21457 SHA256', sha256(auxiliary).hexdigest(), flush=True)
print(auxiliary.decode(), end='', flush=True)
print('URL', BASE + NAME, flush=True)
with urlopen(BASE + NAME, timeout=45) as response:
    content = response.read()
    print('HTTP', response.status, flush=True)
assert content
path = STORE / ('S6_SERIES_PUBLISH_' + NAME)
if path.exists():
    assert path.read_bytes() == content
else:
    path.write_bytes(content)
print('FILE', path, 'BYTES', len(content), 'SHA256', sha256(content).hexdigest(), flush=True)
print('COMPLETE', datetime.now(timezone.utc).isoformat(), flush=True)
