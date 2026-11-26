#!/usr/bin/env python3
"""Retrieve the one LF Tate marking table cited by the released source."""
from pathlib import Path
from urllib.request import Request, urlopen
from hashlib import sha256
from datetime import datetime, timezone
import json

url = ('https://raw.githubusercontent.com/KokunoYumeto/'
       's6-complex-structure-workbench/'
       'a02f2eacf5a8c3db7cf8cdfcdba50c0002ee91c7/'
       'pro_returns/S6_10_PAPERS_checkpoint_15_20261119T1045Z/'
       'S6_10_PAPERS/code/III/manifolds_c3_tate_markings.json')
with urlopen(Request(url, headers={'User-Agent': 'S6-source-audit'}),
             timeout=30) as response:
    data = response.read()
parsed = json.loads(data)
target = Path('/tmp/S6_SERIES_PUBLISH_c7_LF_historical/'
              'S6_SERIES_PUBLISH_manifolds_c3_tate_markings.json')
with target.open('xb') as stream:
    stream.write(data)
record = {'completed_utc': datetime.now(timezone.utc).isoformat(),
          'url': url, 'sha256': sha256(data).hexdigest(),
          'bytes': len(data), 'lines': len(data.splitlines()),
          'initial_rows': len(parsed), 'local_path': str(target),
          'scope': 'Historical table retrieval only; no historical algorithm run.'}
manifest = Path('agents/continuation7_iii_three_primary_receiving/'
                'S6_SERIES_PUBLISH_III_02LF_tate_retrieval_v001.json')
with manifest.open('x') as stream:
    json.dump(record, stream, indent=2)
    stream.write('\n')
print(json.dumps(record, sort_keys=True), flush=True)
print('MANIFEST_SHA256', sha256(manifest.read_bytes()).hexdigest(), flush=True)
