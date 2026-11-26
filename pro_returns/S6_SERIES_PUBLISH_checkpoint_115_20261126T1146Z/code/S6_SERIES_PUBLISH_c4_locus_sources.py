"""Reopen exact primary versions in temporary storage and record access metadata.

The temporary PDFs and any extracted text are excluded from every return ZIP.
This program records retrieval only; an actual reading is recorded separately.
"""
from S6_SERIES_PUBLISH_c4_edit import *
import hashlib
import urllib.request

cache = Path('/tmp/S6_SERIES_PUBLISH_c4_primary')
cache.mkdir(exist_ok=True)
items = [
    ('Engel-v1.pdf', 'https://arxiv.org/pdf/2609.38442v1'),
    ('Rossi-v3.pdf', 'https://arxiv.org/pdf/1211.6329v3'),
    ('Combs-v1.pdf', 'https://arxiv.org/pdf/2610.10451v1'),
]
rows = []
for name, url in items:
    path = cache / name
    origin = 'existing temporary retrieval in this continuation'
    if not path.exists():
        request = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(request, timeout=45) as response:
            data = response.read()
        if not data.startswith(b'%PDF-'):
            raise ValueError('The primary response is not a PDF: ' + url)
        path.write_bytes(data)
        origin = 'downloaded by this program'
    data = path.read_bytes()
    row = dict(name=name, url=url, date_utc=now(), bytes=str(len(data)),
               sha256=hashlib.sha256(data).hexdigest(), retrieval=origin)
    rows.append(row)
    print(name, row['bytes'], row['sha256'], origin)
write_tsv(ROOT / 'S6_SERIES_PUBLISH_c4_locus_sources.tsv',
          ['name', 'url', 'date_utc', 'bytes', 'sha256', 'retrieval'], rows)
