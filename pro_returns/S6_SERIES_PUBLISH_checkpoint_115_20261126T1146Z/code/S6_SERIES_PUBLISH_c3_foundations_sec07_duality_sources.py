from pathlib import Path
from urllib.request import Request,urlopen
import hashlib
import subprocess

url='https://download.uni-mainz.de/mathematik/Algebraische%20Geometrie/DvS-Publikationen/DvS_1987_weakly%20normal%20Surface%20Singularities%20and%20their%20improvements.pdf'
dest=Path('/workspace/scratch/9fcd229a9ed4/base/S6_PUBLISH_c3_foundations_sources/S6_SERIES_PUBLISH_vanStraten1987.pdf')
if not dest.exists():
    with urlopen(Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=45) as response:
        content=response.read()
    assert content.startswith(b'%PDF')
    dest.write_bytes(content)
content=dest.read_bytes()
text=subprocess.check_output(['pdftotext','-layout',str(dest),'-'],text=True)
dest.with_suffix('.txt').write_text(text,newline='\n')
print(url,hashlib.sha256(content).hexdigest(),len(content))
for i,page in enumerate(text.split('\f')):
    if any(term in page for term in ['2.2.2','2.2.3','2.2.4','2.2.5']):
        print('PDF page',i+1)
        print(page)
