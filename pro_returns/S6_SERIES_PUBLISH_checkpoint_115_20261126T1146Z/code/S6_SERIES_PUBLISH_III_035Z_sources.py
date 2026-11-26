#!/usr/bin/env python3
"""Record precise primary-source versions; keep source bytes outside checkpoint."""
from datetime import datetime, timezone
import hashlib
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parent.parent
EXTERNAL = ROOT.parent.parent / 'S6_SERIES_PUBLISH_external_tmp'
assert ROOT not in EXTERNAL.parents and ROOT != EXTERNAL
EXTERNAL.mkdir(exist_ok=True)
SOURCES = [
    ('Hatcher_ATch4.pdf',
     'https://pi.math.cornell.edu/~hatcher/AT/ATch4.pdf'),
    ('Hatcher_ATch5.pdf',
     'https://pi.math.cornell.edu/~hatcher/AT/ATch5.pdf'),
    ('GrbicVucic_2021_full.html',
     'https://www.mathnet.ru/php/archive.phtml?wshow=paper&jrnid=sm&paperid=9436&option_lang=rus'),
]

print('Retrieved UTC:', datetime.now(timezone.utc).isoformat())
for name, url in SOURCES:
    request = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urlopen(request, timeout=45) as response:
        data = response.read()
        status = response.status
        final_url = response.geturl()
        mime = response.headers.get('Content-Type', '')
    (EXTERNAL / name).write_bytes(data)
    print('Name:', name)
    print('Requested URL:', url)
    print('Final URL:', final_url)
    print('HTTP status:', status)
    print('Content type:', mime)
    print('Bytes:', len(data))
    print('SHA256:', hashlib.sha256(data).hexdigest())
    print('Transient path:', EXTERNAL / name)
print('Published-source bytes are outside the checkpoint and must not be packaged.')
