#!/usr/bin/env python3
"""Read primary publications externally; retain only provenance in this tree."""
import hashlib
from pathlib import Path
import subprocess
import urllib.request

OUT = Path('/workspace/scratch/9cfb6f861d2c/S6_SERIES_PUBLISH_external_tmp')
OUT.mkdir(exist_ok=True)
sources = [
    ('S6_SERIES_PUBLISH_III_038X_Baues1998',
     'https://www.cambridge.org/core/services/aop-cambridge-core/content/view/338873CA3FE7693927F42A0CC8488F0D/S0010437X98000013a.pdf/the-degree-of-maps-between-certain-6-manifolds.pdf',
     9, 9),
    ('S6_SERIES_PUBLISH_III_038X_HatcherVB',
     'https://pi.math.cornell.edu/~hatcher/VBKT/VB.pdf', 112, 113),
    ('S6_SERIES_PUBLISH_III_038X_ChaPowell2014',
     'https://msp.org/pjm/2014/272-1/pjm-v272-n1-p01-p.pdf', 15, 15),
]
for stem, url, first, last in sources:
    path = OUT / (stem+'.pdf')
    request = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(request, timeout=45) as response:
        final = response.geturl()
        data = response.read()
    assert data.startswith(b'%PDF')
    path.write_bytes(data)
    text = OUT / (stem+'_reading.txt')
    subprocess.run(['pdftotext', '-layout', '-f', str(first), '-l', str(last),
                    str(path), str(text)], check=True)
    print(stem)
    print('requested:', url)
    print('received:', final)
    print('bytes:', len(data), '; SHA256:', hashlib.sha256(data).hexdigest())
    print('PDF pages read:', first, '-', last)
    print('external publication and extraction:', path, text)
print('No primary publication bytes or extracted text were written in the checkpoint.')
