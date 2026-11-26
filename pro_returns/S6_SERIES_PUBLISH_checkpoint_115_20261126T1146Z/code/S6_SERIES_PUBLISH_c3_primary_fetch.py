"""Fetch primary works outside the checkpoint tree; output byte metadata only."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import hashlib
import json
import subprocess
import urllib.request

DEST = Path('/workspace/scratch/9fcd229a9ed4/primary-c3-root')
DEST.mkdir(parents=True, exist_ok=True)
SOURCES = [
    ('Koenigs1884', 'https://www.numdam.org/article/ASENS_1884_3_1__S3_0.pdf'),
    ('LiuRollenske2012SLC', 'https://lematematiche.dmi.unict.it/index.php/lematematiche/article/download/922/837/3577'),
    ('Stein1954Exp13', 'https://www.numdam.org/item/SHC_1953-1954__6__A13_0.pdf'),
    ('Stein1954Exp14', 'https://www.numdam.org/item/SHC_1953-1954__6__A14_0.pdf'),
    ('Stacks0B3N', 'https://stacks.math.columbia.edu/tag/0B3N'),
]

def fetch(item):
    name, url = item
    suffix = '.html' if name.startswith('Stacks') else '.pdf'
    path = DEST / (name + suffix)
    data = path.read_bytes() if path.exists() else urllib.request.urlopen(url, timeout=45).read()
    if suffix == '.pdf':
        assert data.startswith(b'%PDF'), (name, data[:20])
    path.write_bytes(data)
    if suffix == '.pdf':
        subprocess.run(['pdftotext', '-layout', str(path), str(path.with_suffix('.txt'))], check=True)
    return dict(source=name, url=url, bytes=len(data), sha256=hashlib.sha256(data).hexdigest())

with ThreadPoolExecutor(max_workers=2) as executor:
    for result in executor.map(fetch, SOURCES):
        print(json.dumps(result))
