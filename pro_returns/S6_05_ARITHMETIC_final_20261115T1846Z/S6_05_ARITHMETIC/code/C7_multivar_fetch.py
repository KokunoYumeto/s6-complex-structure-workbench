#!/usr/bin/env python3
"""Preserve the two primary sources for the complexified-norm audit."""
from pathlib import Path
from urllib.request import urlopen
import hashlib
import subprocess

root=Path(__file__).resolve().parents[1]
sources=[
 ('C_Waldschmidt1975_dimension','https://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/Fourier.pdf'),
 ('C_Waldschmidt2009_auxiliary','https://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/SASTRAaftp.pdf')]
for stem,url in sources:
    with urlopen(url) as response:
        data=response.read()
        print('URL:',response.url)
        print('Content-Type:',response.headers.get('Content-Type'))
    assert data.startswith(b'%PDF-')
    path=root/'records'/(stem+'.pdf')
    path.write_bytes(data)
    print('Bytes:',len(data),'SHA256:',hashlib.sha256(data).hexdigest())
    subprocess.run(['pdftotext','-layout',str(path),str(path.with_suffix('.txt'))],check=True)
print('Checked: 1975 Theorem 1 and proof, pp.24-27; 2009 Theorems 3.6-3.7.')
