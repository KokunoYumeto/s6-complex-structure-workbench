#!/usr/bin/env python3
"""Read-only retrieval of the two individually released LN historical sources."""
from pathlib import Path
from hashlib import sha256
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

STORE = Path('/tmp/S6_SERIES_PUBLISH_c7_LN_historical')
STORE.mkdir(exist_ok=True)
BASE = ('https://raw.githubusercontent.com/KokunoYumeto/'
        's6-complex-structure-workbench/'
        'a02f2eacf5a8c3db7cf8cdfcdba50c0002ee91c7/'
        'pro_returns/S6_10_PAPERS_checkpoint_15_20261119T1045Z/'
        'S6_10_PAPERS/')
for name in ['manifolds_general_initial.py', 'manifolds_general_initial_audit.py']:
    found = False
    for directory in ['code/III/', 'code/']:
        url = BASE + directory + name
        try:
            with urlopen(Request(url, headers={'User-Agent': 'S6-LN-source-reading'}),
                         timeout=30) as response:
                raw = response.read()
            raw.decode('utf-8')
        except (HTTPError, URLError, TimeoutError, UnicodeDecodeError) as error:
            print('FAILURE', url, repr(error), flush=True)
            continue
        path = STORE / ('S6_SERIES_PUBLISH_' + name)
        with path.open('xb') as stream:
            stream.write(raw)
        print('SUCCESS', url, 'LOCAL', path, 'SHA256', sha256(raw).hexdigest(),
              'BYTES', len(raw), 'LINES', len(raw.splitlines()), flush=True)
        found = True
        break
    assert found, name
print('COMPLETE: two source files retrieved; no historical algorithm executed.', flush=True)
