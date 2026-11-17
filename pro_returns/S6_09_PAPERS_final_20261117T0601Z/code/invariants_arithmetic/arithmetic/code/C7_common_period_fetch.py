"""Retrieve primary public sources for the common-period theta route."""
from pathlib import Path
from urllib.request import urlopen
from concurrent.futures import ThreadPoolExecutor
import hashlib
import subprocess

root = Path(__file__).resolve().parents[1]
archive = root.parent / 'research_downloads/C7_division'
archive.mkdir(parents=True, exist_ok=True)
sources = [
    ('C_Waldschmidt1988_theta.pdf',
     'https://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/PPN320141322_0016__0_0.pdf'),
    ('C_BundschuhWaldschmidt1996_errata.pdf',
     'https://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/ActaArith78-1996.pdf'),
    ('C_Reyssat1982_Weierstrass.pdf',
     'https://matwbn.icm.edu.pl/ksiazki/aa/aa41/aa4137.pdf'),
]

def fetch(item):
    name, url = item
    data = urlopen(url, timeout=40).read()
    assert data.startswith(b'%PDF-')
    path = archive / name
    path.write_bytes(data)
    subprocess.run(['pdftotext', '-layout', str(path), str(path.with_suffix('.txt'))], check=True)
    return str(path), url, len(data), hashlib.sha256(data).hexdigest()

with ThreadPoolExecutor(max_workers=2) as pool:
    for path, url, size, sha in pool.map(fetch, sources):
        print('PATH:', path, '\nURL:', url, '\nBYTES:', size, '\nSHA256:', sha)

out = archive / 'C_Waldschmidt1988_render'
out.mkdir(exist_ok=True)
subprocess.run(['pdftoppm', '-f', '2', '-l', '8', '-png', '-r', '125',
                str(archive / sources[0][0]), str(out/'page')], check=True)
print('Rendered source PDF pages 2--8 for visual primary-statement verification.')
out = archive / 'C_Reyssat1982_render'
out.mkdir(exist_ok=True)
subprocess.run(['pdftoppm', '-f', '1', '-l', '4', '-png', '-r', '150',
                str(archive / sources[2][0]), str(out/'page')], check=True)
print('Rendered Reyssat PDF pages 1--4 containing the theorem and CM corollary statements.')
