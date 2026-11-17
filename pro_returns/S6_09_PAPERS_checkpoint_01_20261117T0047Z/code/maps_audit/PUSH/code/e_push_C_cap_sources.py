"""Download primary cap-route sources outside the deliverable package.

Only metadata is saved in the package. OCR and full primary papers stay in
external_sources/C_independent_primary. No source text is treated as a proof
without an explicit reading record.
"""
from pathlib import Path
import hashlib
import json
import subprocess
import urllib.request

HERE = Path(__file__).resolve()
ROOT = HERE.parents[2]
DEST = ROOT / 'external_sources' / 'C_independent_primary'
DEST.mkdir(parents=True, exist_ok=True)
SOURCES = {
    'Wall1966V': 'https://webhomes.maths.ed.ac.uk/~v1ranick/papers/wclass5.pdf',
    'Haefliger1966': 'https://webhomes.maths.ed.ac.uk/~v1ranick/tda/haefliger.pdf',
    'Krylov2004': 'https://arxiv.org/pdf/math/0409342',
    'Olbermann2010': 'https://msp.org/agt/2010/10-4/agt-v10-n4-p03-s.pdf',
    'FintushelPao1983': 'https://msp.org/pjm/1983/109-2/pjm-v109-n2-p09-p.pdf',
}
records = []
for name, url in SOURCES.items():
    path = DEST / (name + '.pdf')
    if not path.exists():
        request = urllib.request.Request(url, headers={'User-Agent': 'Research source verification'})
        path.write_bytes(urllib.request.urlopen(request, timeout=40).read())
    data = path.read_bytes()
    if not data.startswith(b'%PDF'):
        raise ValueError(f'{name}: download is not a PDF')
    textpath = path.with_suffix('.txt')
    subprocess.run(['pdftotext', '-layout', str(path), str(textpath)], check=True)
    rec = {'source': name, 'url': url, 'path': str(path),
           'sha256': hashlib.sha256(data).hexdigest(), 'bytes': len(data),
           'text_bytes': textpath.stat().st_size}
    records.append(rec)
    print(json.dumps(rec))
HERE.with_suffix('.json').write_text(json.dumps(records, indent=2) + '\n')
