from pathlib import Path
from urllib.request import Request,urlopen
import hashlib
import subprocess

url='https://pi.math.cornell.edu/~hatcher/AT/AT.pdf'
dest=Path('/workspace/scratch/9fcd229a9ed4/base/S6_PUBLISH_c3_foundations_sources/S6_SERIES_PUBLISH_Hatcher2002.pdf')
if not dest.exists():
    with urlopen(Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=45) as response:
        content=response.read()
    assert content.startswith(b'%PDF')
    dest.write_bytes(content)
content=dest.read_bytes()
text=subprocess.check_output(['pdftotext','-layout',str(dest),'-'],text=True)
dest.with_suffix('.txt').write_text(text,newline='\n')
print(url,len(content),hashlib.sha256(content).hexdigest())
pages=text.split('\f')
for i,page in enumerate(pages):
    if any(term in page for term in ['Proposition 0.18','Theorem 1.20','Proposition 4G.1','Proposition 4G.2','Example 1.28']):
        print('PDF page',i+1);print(page)
