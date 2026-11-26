"""Record retrieval identities only; no external source copies are retained.

The cited passages are opened separately in the source-reading activity.
These byte hashes identify the retrieved editions; they prove no theorem.
"""
from concurrent.futures import ThreadPoolExecutor
from hashlib import sha256
from datetime import datetime, timezone
import json
from urllib.request import Request, urlopen

SOURCES = [
    ('E26', 'https://arxiv.org/pdf/2609.38442v1'),
    ('AC26', 'https://alpo.ge/s6.pdf'),
    ('BHS19', 'https://arxiv.org/pdf/1910.14116v3'),
    ('mapsToda52', 'https://www.i-repository.net/contents/osakacu/sugaku/DB-M-002-02-01.pdf'),
    ('mapsAPS2', 'https://webhomes.maths.ed.ac.uk/~v1ranick/papers/aps002.pdf'),
    ('mapsWaldhausen68', 'https://www.maths.gla.ac.uk/~mpowell/Waldhausen-Irreducible3ManifoldsSufficiently-1968.pdf'),
    ('Hatcher2002', 'https://pi.math.cornell.edu/~hatcher/AT/AT.pdf'),
    ('manZhubr75', 'https://www.mathnet.ru/php/getFT.phtml?jrnid=im&option_lang=eng&paperid=2054&what=fullteng'),
]

def retrieve(item):
    key, url = item
    try:
        request = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urlopen(request, timeout=15) as response:
            data = response.read()
            return dict(key=key, requested_url=url, resolved_url=response.url,
                        retrieved_utc=datetime.now(timezone.utc).isoformat(),
                        bytes=len(data), sha256=sha256(data).hexdigest(),
                        pdf_header=data.startswith(b'%PDF-'),
                        content_type=response.headers.get('content-type', ''),
                        saved_external_source=False)
    except Exception as error:
        return dict(key=key, requested_url=url, error=str(error),
                    saved_external_source=False)

with ThreadPoolExecutor(max_workers=4) as pool:
    for result in pool.map(retrieve, SOURCES):
        print(json.dumps(result, ensure_ascii=False, sort_keys=True))
