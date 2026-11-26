#!/usr/bin/env python3
"""Retrieve exactly the released LF historical sources and cited outputs.

This is a provenance retrieval, not a replay of the historical algorithms.
All attempts, failures, returned hashes, and the saved byte paths are retained.
No non-LF record is selected or printed. Every returned LF file is to be read.
"""
from pathlib import Path
from hashlib import sha256
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
from datetime import datetime, timezone
import json

LANE = Path('agents/continuation7_iii_three_primary_receiving')
STORE = Path('/tmp/S6_SERIES_PUBLISH_c7_LF_historical')
STORE.mkdir(exist_ok=True)
BASE = ('https://raw.githubusercontent.com/KokunoYumeto/'
        's6-complex-structure-workbench/'
        'a02f2eacf5a8c3db7cf8cdfcdba50c0002ee91c7/'
        'pro_returns/S6_10_PAPERS_checkpoint_15_20261119T1045Z/'
        'S6_10_PAPERS/')
FILES = [
    ('manifolds_tate_markings.py', ['code/III/', 'code/']),
    ('fourfolds_D2_c3_AH.py', ['code/III/', 'code/']),
    ('fourfolds_D2_c3_tate.out', ['code/III/', 'code/']),
    ('fourfolds_D2_c3_AH.out', ['code/III/', 'code/']),
    ('fourfolds_D2_c3_AH.json', ['records/', 'code/III/']),
]
records = []
for name, directories in FILES:
    entry = {'name': name, 'attempts': [], 'available': False}
    for directory in directories:
        url = BASE + directory + name
        try:
            with urlopen(Request(url, headers={'User-Agent': 'S6-source-audit'}),
                         timeout=30) as response:
                content = response.read()
            content.decode('utf-8')
            if name.endswith('.json'):
                json.loads(content)
        except (HTTPError, URLError, TimeoutError, UnicodeDecodeError,
                json.JSONDecodeError) as error:
            attempt = {'url': url, 'status': 'failed', 'error': str(error)}
            entry['attempts'].append(attempt)
            print('RETRIEVAL_FAILURE', json.dumps(attempt, sort_keys=True), flush=True)
            continue
        target = STORE / ('S6_SERIES_PUBLISH_' + name)
        with target.open('xb') as stream:
            stream.write(content)
        digest = sha256(content).hexdigest()
        entry['attempts'].append({'url': url, 'status': 'success'})
        entry.update({'available': True, 'url': url, 'sha256': digest,
                      'bytes': len(content), 'lines': len(content.splitlines()),
                      'local_path': str(target)})
        print('RETRIEVED', name, 'SHA256', digest, 'BYTES', len(content),
              'LINES', len(content.splitlines()), flush=True)
        break
    records.append(entry)
manifest = {'completed_utc': datetime.now(timezone.utc).isoformat(),
            'scope': 'Read-only retrieval of the five released LF historical files; '
                     'no historical algorithm executed.',
            'files': records}
target = LANE / 'S6_SERIES_PUBLISH_III_02LF_historical_retrieval_v001.json'
with target.open('x') as stream:
    json.dump(manifest, stream, indent=2)
    stream.write('\n')
print('MANIFEST', str(target), sha256(target.read_bytes()).hexdigest(), flush=True)
print('AVAILABLE', sum(x['available'] for x in records), 'OF', len(records), flush=True)
