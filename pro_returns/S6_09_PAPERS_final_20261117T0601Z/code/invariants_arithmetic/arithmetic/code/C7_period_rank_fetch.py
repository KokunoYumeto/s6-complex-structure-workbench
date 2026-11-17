"""Retrieve primary period-rank theorem sources through their public links."""
from pathlib import Path
from urllib.request import urlopen
from urllib.parse import urljoin
from concurrent.futures import ThreadPoolExecutor
from html.parser import HTMLParser
import hashlib
import subprocess

class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links=[]
        self.current=None
        self.metas={}
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='a' and 'href' in a:
            self.current=[a['href'],'']
        if tag=='meta' and 'name' in a:
            self.metas[a['name']]=a.get('content','')
    def handle_data(self,data):
        if self.current is not None:
            self.current[1]+=data
    def handle_endtag(self,tag):
        if tag=='a' and self.current is not None:
            self.links.append(self.current)
            self.current=None

root = Path(__file__).resolve().parents[1]
archive = root.parent/'research_downloads/C7_division'
archive.mkdir(exist_ok=True, parents=True)
pages = [
 ('author', 'https://webusers.imj-prg.fr/~michel.waldschmidt/texts.html'),
 ('roy', 'https://www.cambridge.org/core/journals/canadian-mathematical-bulletin/article/autour-du-theoreme-du-sousgroupe-algebrique/A1E35F3798690D084664ACD83D1557E8'),
]
def run(item):
    name, url = item
    data = urlopen(url, timeout=25).read()
    (archive/f'C_period_rank_{name}.html').write_bytes(data)
    soup = Links()
    soup.feed(data.decode('utf8',errors='replace'))
    if name == 'author':
        for href, title in soup.links:
            if any(x in title.lower()
                   for x in ['autour du th', 'transcendence methods of', 'dependence of logarithms']):
                print('AUTHOR LINK:',title,urljoin(url,href),flush=True)
    else:
        meta=soup.metas.get('citation_pdf_url')
        assert meta
        pdfurl=urljoin(url,meta)
        print('ROY PDF URL:',pdfurl,flush=True)
        pdf=urlopen(pdfurl,timeout=30).read()
        assert pdf.startswith(b'%PDF-')
        path=archive/'C_RoyWaldschmidt1993.pdf'
        path.write_bytes(pdf)
        print('PATH:',path,'BYTES:',len(pdf),'SHA256:',hashlib.sha256(pdf).hexdigest(),flush=True)
        subprocess.run(['pdftotext','-layout',str(path),str(path.with_suffix('.txt'))],check=True)
        out=archive/'C_RoyWaldschmidt1993_render'
        out.mkdir(exist_ok=True)
        subprocess.run(['pdftoppm','-f','1','-l','5','-png','-r','130',str(path),str(out/'page')],check=True)
with ThreadPoolExecutor(max_workers=2) as pool:
    for fut in [pool.submit(run,item) for item in pages]:
        try:
            fut.result()
        except Exception as exc:
            print(type(exc).__name__+':',exc,flush=True)

url='https://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/Durham1986TMGSSV.pdf'
try:
    data=urlopen(url,timeout=25).read()
    assert data.startswith(b'%PDF-')
    path=archive/'C_Waldschmidt1988_period_rank.pdf'
    path.write_bytes(data)
    print('PATH:',path,'URL:',url,'BYTES:',len(data),
          'SHA256:',hashlib.sha256(data).hexdigest(),flush=True)
    out=archive/'C_Waldschmidt1988_period_rank_render'
    out.mkdir(exist_ok=True)
    subprocess.run(['pdftoppm','-f','6','-l','8','-png','-r','150',
                    str(path),str(out/'page')],check=True)
except Exception as exc:
    print(type(exc).__name__+':',exc,flush=True)
