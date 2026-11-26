#!/usr/bin/env python3
"""Retrieve the exact released LN audit records; do not execute historical code."""
from pathlib import Path
from hashlib import sha256
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
import json

ROOT = Path.cwd()
STORE = Path('/tmp/S6_SERIES_PUBLISH_c7_LN_historical')
STORE.mkdir(exist_ok=True)
BASE = ('https://raw.githubusercontent.com/KokunoYumeto/'
        's6-complex-structure-workbench/'
        'a02f2eacf5a8c3db7cf8cdfcdba50c0002ee91c7/'
        'pro_returns/S6_10_PAPERS_checkpoint_15_20261119T1045Z/'
        'S6_10_PAPERS/')
for name in ['manifolds_general_initial_constants.json',
             'manifolds_general_initial_audit.json',
             'manifolds_general_initial_audit.out']:
    found = False
    for directory in ['records/', 'code/III/']:
        url = BASE + directory + name
        try:
            with urlopen(Request(url, headers={'User-Agent': 'S6-LN-source-reading'}),
                         timeout=30) as response:
                raw = response.read()
            raw.decode('utf-8')
            if name.endswith('.json'):
                json.loads(raw)
        except (HTTPError, URLError, TimeoutError, UnicodeDecodeError,
                json.JSONDecodeError) as error:
            print('FAILURE', url, repr(error), flush=True)
            continue
        path = STORE / ('S6_SERIES_PUBLISH_' + name)
        with path.open('xb') as stream:
            stream.write(raw)
        print('SUCCESS', url, 'LOCAL', path, 'SHA256', sha256(raw).hexdigest(),
              'BYTES', len(raw), 'LINES', len(raw.splitlines()), flush=True)
        found = True
        break
    if name.endswith('.json'):
        assert found, name
    else:
        print('STDOUT_AVAILABLE', found, flush=True)
canonical = (ROOT / 'S6_SERIES_PUBLISH_III.tex').read_bytes()
assert sha256(canonical).hexdigest() == \
    '9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0'
lines = canonical.decode().splitlines(keepends=True)
block = ''.join(lines[19263:19286])
assert 'The replay' in block and '\\begin{theorem}' not in block
path = ROOT / ('agents/continuation7_iii_general_initial_receiving/'
               'S6_SERIES_PUBLISH_III_02LN_released_following_auxiliary.tex')
with path.open('x') as stream:
    stream.write(block)
print('FOLLOWING_AUXILIARY', path, 'LINES', len(block.splitlines()),
      'SHA256', sha256(block.encode()).hexdigest(), flush=True)
print('COMPLETE: actual archived outputs retrieved where present; no historical algorithm executed.', flush=True)
