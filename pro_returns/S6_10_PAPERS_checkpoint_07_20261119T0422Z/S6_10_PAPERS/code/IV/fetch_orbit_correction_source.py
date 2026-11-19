"""Retrieve and render the primary orbit-map correction slides for reading."""
from pathlib import Path
import hashlib,json,urllib.request
import fitz
P=Path(__file__).resolve().parents[2]
D=P/'analysis/IV/references';D.mkdir(parents=True,exist_ok=True)
u='https://www.fields.utoronto.ca/talk-media/1/23/28/slides.pdf'
with urllib.request.urlopen(u,timeout=40) as response:
    raw=response.read();final_url=response.url
assert raw.startswith(b'%PDF')
f=D/'KarshonOrbitSlidesD.pdf';f.write_bytes(raw)
d=fitz.open(f)
(D/'KarshonOrbitSlidesD.txt').write_text('\n'.join(f'=== PDF PAGE {i+1} ===\n'+x.get_text() for i,x in enumerate(d)))
images=D/'page_checks';images.mkdir(exist_ok=True)
for n in [2,6,7,13,14,15]:d[n-1].get_pixmap(matrix=fitz.Matrix(1.5,1.5)).save(images/f'KarshonOrbit_{n:02}.png')
(D/'Karshon_download_receipt.json').write_text(json.dumps({'url':u,'final_url':final_url,'sha256':hashlib.sha256(raw).hexdigest(),'pages':len(d),'bytes':len(raw),'scope':'Download and extraction only; no reading or proof credit.'},indent=2))
print('Retrieved',len(d),'pages, SHA256',hashlib.sha256(raw).hexdigest())
a=fitz.open(P/'analysis/I_sources/AtiyahSinger1968IIIE.pdf')
for n in [1,20,21]:a[n-1].get_pixmap(matrix=fitz.Matrix(1.5,1.5)).save(images/f'AtiyahSinger_pdf{n:02}.png')
