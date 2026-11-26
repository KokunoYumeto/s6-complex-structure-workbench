"""Fetch two primary signature sources outside every deliverable tree."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import hashlib
import urllib.request

TEMP = Path(__file__).resolve().parents[3] / 'temporary_literature'
SOURCES = [
    ('Milnor_1964', 'https://ncatlab.org/nlab/files/Milnor_DifferentialTopology.pdf',
     'Differential topology, 1964; printed p173, PDF page9'),
    ('Kauffman_CyclicBC', 'https://homepages.math.uic.edu/~kauffman/CyclicBC.pdf',
     'On Knots, Chapter XIII, Theorem13.1, printed p299, PDF page15'),
]

def fetch(item):
    name, url, locus = item
    with urllib.request.urlopen(url, timeout=40) as response:
        data = response.read()
    assert data.startswith(b'%PDF-'), name
    TEMP.mkdir(exist_ok=True)
    (TEMP / (name + '.pdf')).write_bytes(data)
    return name, url, len(data), hashlib.sha256(data).hexdigest(), locus

print('source\turl\tsize_bytes\tsha256\tlocus', flush=True)
with ThreadPoolExecutor(max_workers=2) as pool:
    for result in pool.map(fetch, SOURCES):
        print(*result, sep='\t', flush=True)
print('Downloaded publications and page images are excluded from all return ZIPs.')
