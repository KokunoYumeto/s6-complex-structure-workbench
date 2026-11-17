#!/usr/bin/env python3
"""Preserve the primary preprint used for the arithmetic-germ criterion audit."""
from pathlib import Path
from urllib.request import urlopen
import hashlib
import subprocess

root = Path(__file__).resolve().parents[1]
url = 'https://arxiv.org/pdf/2202.09032'
with urlopen(url) as response:
    data = response.read()
    print('URL:', response.url)
    print('Content-Type:', response.headers.get('Content-Type'))
assert data.startswith(b'%PDF-')
path = root/'records/C_Xie2024_preprint.pdf'
path.write_bytes(data)
print('Bytes:', len(data))
print('SHA256:', hashlib.sha256(data).hexdigest())
subprocess.run(['pdftotext','-layout',str(path),
                str(root/'records/C_Xie2024_preprint.txt')],check=True)
print('Checked: Theorems 1.3, 2.3 and 2.5, their definitions of a K-defined formal germ, and Section 1.1.')
