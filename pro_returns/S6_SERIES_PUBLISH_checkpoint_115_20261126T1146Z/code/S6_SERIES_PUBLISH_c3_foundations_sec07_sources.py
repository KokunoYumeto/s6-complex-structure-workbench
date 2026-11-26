from pathlib import Path
import hashlib
import urllib.request
import subprocess

OUT = Path('/workspace/scratch/9fcd229a9ed4/base/S6_PUBLISH_c3_foundations_sources')
OUT.mkdir(exist_ok=True)
for name, url, terms in [
    ('Catanese2002_v2', 'https://arxiv.org/pdf/math/0111245v2', ['deformation in the large', 'Bagnera']),
    ('Steenbrink1999_v1', 'https://arxiv.org/pdf/math/9902134v1', ['Theorem 1.', 'Corollary 2.', 'excision']),
]:
    dest = OUT / f'S6_SERIES_PUBLISH_{name}.pdf'
    if not dest.exists():
        request = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(request, timeout=35) as response:
            data = response.read()
        assert data.startswith(b'%PDF'), url
        dest.write_bytes(data)
    data = dest.read_bytes()
    pages = subprocess.check_output(['pdftotext', '-layout', str(dest), '-'], text=True).split('\f')
    print(name, url, hashlib.sha256(data).hexdigest(), len(pages)-1)
    for i, text in enumerate(pages):
        if any(term.casefold() in text.casefold() for term in terms):
            print(f'PDF PAGE {i+1}\n{text}')
