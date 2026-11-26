"""Post-release LI historical source retrieval; no import or execution."""
from hashlib import sha256
from pathlib import Path
from urllib.request import Request, urlopen
import json

base = ('https://raw.githubusercontent.com/KokunoYumeto/'
        's6-complex-structure-workbench/'
        'a02f2eacf5a8c3db7cf8cdfcdba50c0002ee91c7/'
        'pro_returns/S6_10_PAPERS_checkpoint_15_20261119T1045Z/'
        'S6_10_PAPERS/code/III/')
dest = Path('/tmp/S6_SERIES_PUBLISH_c7_LI_historical')
dest.mkdir(exist_ok=True)
name = 'manifolds_all_weighted_profiles.py'
url = base + name
data = urlopen(Request(url, headers={'User-Agent': 'S6-series-source-audit'}),
               timeout=40).read()
path = dest / ('S6_SERIES_PUBLISH_' + name)
assert not path.exists()
path.write_bytes(data)
print(json.dumps({'url': url, 'path': str(path), 'bytes': len(data),
                  'sha256': sha256(data).hexdigest()}, sort_keys=True))
print('Retrieval only; historical source not imported or executed.')
