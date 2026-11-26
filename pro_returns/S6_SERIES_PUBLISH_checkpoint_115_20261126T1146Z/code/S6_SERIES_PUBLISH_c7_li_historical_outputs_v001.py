"""Retrieve LI saved mathematical output after original release."""
from hashlib import sha256
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError
import json

base = ('https://raw.githubusercontent.com/KokunoYumeto/'
        's6-complex-structure-workbench/'
        'a02f2eacf5a8c3db7cf8cdfcdba50c0002ee91c7/'
        'pro_returns/S6_10_PAPERS_checkpoint_15_20261119T1045Z/'
        'S6_10_PAPERS/code/III/')
dest = Path('/tmp/S6_SERIES_PUBLISH_c7_LI_historical')
for name in ('manifolds_all_weighted_profiles.json',
             'manifolds_all_weighted_profiles.out'):
    url = base + name
    try:
        data = urlopen(Request(url, headers={'User-Agent': 'S6-series-source-audit'}),
                       timeout=40).read()
    except HTTPError as exc:
        print(json.dumps({'url': url, 'http_status': exc.code}, sort_keys=True))
        continue
    path = dest / ('S6_SERIES_PUBLISH_' + name)
    assert not path.exists()
    path.write_bytes(data)
    record = {'url': url, 'path': str(path), 'bytes': len(data),
              'sha256': sha256(data).hexdigest()}
    if name.endswith('.json'):
        parsed = json.loads(data)
        record['top_keys'] = list(parsed)
        record['counts'] = {k: parsed[k] for k in ('chainchecks', 'wordchecks',
                            'checks', 'even_checks', 'overlap_comparisons')}
        record['saved_samples'] = len(parsed['samples'])
    print(json.dumps(record, sort_keys=True))
print('Retrieval only; historical source not imported or executed.')
