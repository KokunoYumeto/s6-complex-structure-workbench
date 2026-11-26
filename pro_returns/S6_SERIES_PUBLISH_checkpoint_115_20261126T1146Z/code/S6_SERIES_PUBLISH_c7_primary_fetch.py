"""Fetch a primary source to a temporary directory, printing identity only."""
from pathlib import Path
import hashlib
import urllib.request

url = 'https://msp.org/pjm/1980/89-1/pjm-v89-n1-p10-s.pdf'
destination = Path(__file__).resolve().parents[3] / 'temporary_literature' / 'Kas_1980.pdf'
destination.parent.mkdir(exist_ok=True)
with urllib.request.urlopen(url, timeout=40) as response:
    data = response.read()
assert data.startswith(b'%PDF-'), 'Publisher response is not a PDF.'
destination.write_bytes(data)
print('source\turl\tsize_bytes\tsha256\tlocus')
print('A. Kas, Pacific J. Math. 89 (1980), 89-104', url, len(data),
      hashlib.sha256(data).hexdigest(),
      'Theorem 1.7, pp93-95; surface framing consequence p96', sep='\t')
print('Temporary PDF excluded from every checkpoint and final ZIP.')
