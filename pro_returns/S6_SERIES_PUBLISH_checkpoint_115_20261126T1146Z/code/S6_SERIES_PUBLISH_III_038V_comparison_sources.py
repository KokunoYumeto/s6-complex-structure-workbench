#!/usr/bin/env python3
"""Record sources opened only in the post-release 038V comparison."""
from datetime import datetime, timezone
import hashlib
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parent.parent
EXTERNAL = ROOT.parent.parent / 'S6_SERIES_PUBLISH_external_tmp'
assert ROOT not in EXTERNAL.parents and ROOT != EXTERNAL
EXTERNAL.mkdir(exist_ok=True)
SOURCES = [
    ('Toda_JSTOR_HTTP_response.html', 'https://www.jstor.org/stable/j.ctt1bgzb5t'),
    ('IsaksenWangXu_2023.pdf', 'https://www.numdam.org/item/10.1007/s10240-023-00139-1.pdf'),
]
print('Post-release retrieval UTC:', datetime.now(timezone.utc).isoformat())
for name, url in SOURCES:
    print('Name:', name)
    print('Requested URL:', url)
    try:
        request = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urlopen(request, timeout=45) as response:
            data = response.read()
            print('Final URL:', response.geturl())
            print('HTTP status:', response.status)
            print('Content type:', response.headers.get('Content-Type', ''))
        (EXTERNAL / name).write_bytes(data)
        print('Bytes:', len(data))
        print('SHA256:', hashlib.sha256(data).hexdigest())
        print('Transient path:', EXTERNAL / name)
        if b'<title>Client Challenge</title>' in data:
            print('Response is Client Challenge, not a primary-source byte version.')
            print('The public Proposition3.1 excerpt was read in the web opener only.')
    except (HTTPError, URLError, TimeoutError) as exc:
        print('Ordinary download unavailable:', type(exc).__name__, str(exc))
        print('Only the public content actually opened in the web tool is credited.')
print('All published-source bytes remain outside the checkpoint.')
