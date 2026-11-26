"""Retrieve only the LU audit's named stored output and matching stream names."""
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import urlopen

BASE = ('https://raw.githubusercontent.com/KokunoYumeto/'
        's6-complex-structure-workbench/'
        'a02f2eacf5a8c3db7cf8cdfcdba50c0002ee91c7/'
        'pro_returns/S6_10_PAPERS_checkpoint_15_20261119T1045Z/S6_10_PAPERS/')
STORE = Path('/tmp/S6_SERIES_PUBLISH_c7_LU_historical')
targets = [('code/III/manifolds_corrected_initial_audit.json', True),
           ('code/III/manifolds_corrected_initial_audit.out', False),
           ('records/manifolds_corrected_initial_audit.out', False)]
print('START', datetime.now(timezone.utc).isoformat(), flush=True)
for locator, required in targets:
    print('URL', BASE + locator, flush=True)
    try:
        with urlopen(BASE + locator, timeout=45) as response:
            content = response.read()
            print('HTTP', response.status, flush=True)
    except HTTPError as error:
        print('HTTP', error.code, flush=True)
        if required:
            raise
        continue
    assert content
    destination = STORE / ('S6_SERIES_PUBLISH_' + Path(locator).name)
    if destination.exists():
        assert destination.read_bytes() == content
    else:
        destination.write_bytes(content)
    print('FILE', destination, 'BYTES', len(content), 'SHA256',
          sha256(content).hexdigest(), flush=True)
print('COMPLETE', datetime.now(timezone.utc).isoformat(), flush=True)
