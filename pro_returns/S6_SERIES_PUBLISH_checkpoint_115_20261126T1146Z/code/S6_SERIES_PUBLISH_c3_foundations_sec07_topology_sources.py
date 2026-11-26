from pathlib import Path
from urllib.request import Request,urlopen
import hashlib
import subprocess

url='https://www.numdam.org/item/ASNSP_1964_3_18_4_449_0.pdf'
dest=Path('/workspace/scratch/9fcd229a9ed4/base/S6_PUBLISH_c3_foundations_sources/S6_SERIES_PUBLISH_Lojasiewicz1964.pdf')
if not dest.exists():
    with urlopen(Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=40) as response:
        content=response.read()
    assert content.startswith(b'%PDF')
    dest.write_bytes(content)
content=dest.read_bytes()
text=subprocess.check_output(['pdftotext','-layout',str(dest),'-'],text=True)
dest.with_suffix('.txt').write_text(text,newline='\n')
pages=text.split('\f')
print(url,hashlib.sha256(content).hexdigest(),len(content))
for i,page in enumerate(pages):
    if 'THEOREM 2.' in page:
        for j in range(max(0,i-1),i+1):
            print('PDF page',j+1);print(pages[j])
