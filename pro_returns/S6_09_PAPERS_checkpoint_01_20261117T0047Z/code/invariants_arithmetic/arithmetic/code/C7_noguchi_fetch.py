#!/usr/bin/env python3
"""Preserve the public author manuscript used for the functional route audit."""
from pathlib import Path
from urllib.request import urlopen
import hashlib
import subprocess

root = Path(__file__).resolve().parents[1]
url = 'https://www.ms.u-tokyo.ac.jp/~noguchi/An-axsch.pdf'
with urlopen(url) as response:
    data = response.read()
    print('URL:', response.url)
    print('Content-Type:', response.headers.get('Content-Type'))
assert data.startswith(b'%PDF-')
path = root/'records/C_Noguchi2024_author.pdf'
path.write_bytes(data)
print('Bytes:', len(data))
print('SHA256:', hashlib.sha256(data).hexdigest())
subprocess.run(['pdftotext','-layout',str(path),
                str(root/'records/C_Noguchi2024_author.txt')],check=True)
print('Checked: Definition 1.2, Theorem 1.3, proof in Section 3.')
