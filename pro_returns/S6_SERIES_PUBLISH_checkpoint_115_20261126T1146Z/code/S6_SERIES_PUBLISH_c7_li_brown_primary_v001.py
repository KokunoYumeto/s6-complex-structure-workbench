"""Retrieve the cited Brown primary and locate I.5, without copying source prose."""
from hashlib import sha256
from pathlib import Path
from urllib.request import Request, urlopen
import json
import subprocess

url = ('https://ebooks.karbust.me/Mathematics/Kenneth%20S.%20Brown%20-%20'
       'Cohomology%20of%20Groups%20%281982%29%20%5B978-1-4684-9327-6%5D.pdf')
dest = Path('/tmp/S6_SERIES_PUBLISH_c7_LI_Brown')
dest.mkdir(exist_ok=True)
pdf = dest / 'S6_SERIES_PUBLISH_Brown1982.pdf'
data = urlopen(Request(url, headers={'User-Agent': 'S6-series-source-audit'}),
               timeout=40).read()
assert data.startswith(b'%PDF')
pdf.write_bytes(data)
txt = dest / 'S6_SERIES_PUBLISH_Brown1982.txt'
subprocess.run(['pdftotext', '-layout', str(pdf), str(txt)], check=True)
pages = txt.read_text(errors='replace').split('\f')
candidates = [i+1 for i, page in enumerate(pages)
              if 'The Standard Resolution' in page and 'CHAPTER I' not in page]
print(json.dumps({'url': url, 'path': str(pdf), 'bytes': len(data),
                  'sha256': sha256(data).hexdigest(),
                  'candidate_pdf_pages': candidates}, sort_keys=True))
print('Primary retrieval and locator only; no page reading claimed by this program.')
