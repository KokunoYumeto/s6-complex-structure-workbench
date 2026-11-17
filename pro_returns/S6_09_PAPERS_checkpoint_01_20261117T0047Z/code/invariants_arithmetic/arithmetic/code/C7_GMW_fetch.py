"""Preserve and render the primary variable-degree Schneider criterion."""
from pathlib import Path
from urllib.request import urlopen
import hashlib
import subprocess

root=Path(__file__).resolve().parents[1]
archive=root.parent/'research_downloads/C7_division'
archive.mkdir(parents=True,exist_ok=True)
url='https://matwbn.icm.edu.pl/ksiazki/aa/aa47/aa4721.pdf'
data=urlopen(url,timeout=40).read()
assert data.startswith(b'%PDF-')
pdf=archive/'C_GramainMignotteWaldschmidt1986.pdf'
pdf.write_bytes(data)
print('URL:',url)
print('Bytes:',len(data),'SHA256:',hashlib.sha256(data).hexdigest())
subprocess.run(['pdftotext','-layout',str(pdf),str(pdf.with_suffix('.txt'))],check=True)
out=archive/'C_GMW1986_render'
out.mkdir(exist_ok=True)
subprocess.run(['pdftoppm','-f','2','-l','4','-png','-r','135',str(pdf),str(out/'page')],check=True)
print('Rendered pages2–4 containing the variable-degree criterion.')
