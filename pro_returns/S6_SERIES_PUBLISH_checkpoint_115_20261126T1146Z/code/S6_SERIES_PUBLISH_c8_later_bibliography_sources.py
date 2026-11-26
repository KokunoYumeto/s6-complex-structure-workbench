"""Retrieve named primary editions for a bounded bibliography/page check.

External PDFs and extracted text remain in a temporary directory outside the
checkpoint.  The printed identities describe actual retrievals, not theorem
verification.  No body, bibliography, or shared publication record is edited.
"""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
from urllib.request import Request, urlopen
import json
import subprocess
import sys

TEMP = Path('/tmp/S6_SERIES_PUBLISH_c8_III_bibliography_sources')
TEMP.mkdir(parents=True, exist_ok=True)
SOURCES = [
    ('Yang_v1', 'https://arxiv.org/pdf/2609.29666v1'),
    ('Liu_Rollenske_v2', 'https://arxiv.org/pdf/2609.33826v2'),
    ('Debray_Gunningham_author', 'https://adebray.github.io/papers/arf_brown.pdf'),
    ('Ulmer_Urzua_v2', 'https://arxiv.org/pdf/2002.01906v2'),
    ('Viaclovsky_two_v1', 'https://arxiv.org/pdf/2609.33785v1'),
    ('Viaclovsky_logs_v1', 'https://arxiv.org/pdf/2610.39102v1'),
    ('Pontryagin_1955_scan', 'https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/pont4.pdf'),
    ('Pontryagin_1950_scan', 'https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/pont3.pdf'),
    ('BHS_journal', 'https://archive.intlpress.com/site/pub/files/_fulltext/journals/acta/2023/0231/0002/ACTA-2023-0231-0002-a001.pdf'),
    ('Engel_v1', 'https://arxiv.org/pdf/2609.38442v1'),
    ('Besser_Livne_v2', 'https://arxiv.org/pdf/1202.2808v2'),
    ('Schuett_Shioda_v3', 'https://arxiv.org/pdf/0907.0298v3'),
    ('Fukae_v1', 'https://arxiv.org/pdf/math/0205062v1'),
    ('Wang_v2', 'https://arxiv.org/pdf/2609.11541v2'),
]

def retrieve(item):
    key, url = item
    result = dict(key=key, requested_url=url)
    try:
        request = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urlopen(request, timeout=20) as response:
            data = response.read()
            result.update(resolved_url=response.url,
                          retrieved_utc=datetime.now(timezone.utc).isoformat(),
                          bytes=len(data), sha256=sha256(data).hexdigest(),
                          content_type=response.headers.get('content-type', ''))
        if not data.startswith(b'%PDF-'):
            raise ValueError('Retrieved bytes do not have a PDF header')
        pdf = TEMP / (key + '.pdf')
        extracted = TEMP / (key + '.txt')
        pdf.write_bytes(data)
        process = subprocess.run(['pdftotext', '-layout', str(pdf), str(extracted)],
                                 capture_output=True, text=True, check=False)
        result.update(extraction_exit=process.returncode,
                      extraction_stderr=process.stderr,
                      temporary_pdf=str(pdf), temporary_text=str(extracted),
                      checkpoint_source_copy=False)
    except Exception as error:
        result['error'] = str(error)
    return result

selected = SOURCES
if len(sys.argv) > 1:
    requested = set(sys.argv[1:])
    known = {key for key, _ in SOURCES}
    if requested - known:
        raise ValueError('Unknown source keys: ' + ', '.join(sorted(requested - known)))
    selected = [item for item in SOURCES if item[0] in requested]
with ThreadPoolExecutor(max_workers=4) as pool:
    for result in pool.map(retrieve, selected):
        print(json.dumps(result, ensure_ascii=False, sort_keys=True))
