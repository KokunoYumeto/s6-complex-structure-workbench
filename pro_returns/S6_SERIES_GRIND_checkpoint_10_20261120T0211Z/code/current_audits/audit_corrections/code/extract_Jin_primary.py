from pathlib import Path
from html.parser import HTMLParser
import urllib.request,json,hashlib

root=Path(__file__).resolve().parents[1]
raw=(root/'Jin_primary_html_attempt.txt').read_bytes()
p=root/'primary_sources';p.mkdir(exist_ok=True)
(p/'Jin_2608.26698v2.html').write_bytes(raw)
class Extract(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True);self.out=[];self.math=False;self.hidden=None
    def handle_starttag(self,tag,attrs):
        at=dict(attrs)
        if tag in ('script','style'):self.hidden=tag
        if self.hidden:return
        if tag=='math':
            self.math=True;self.out.append(' $'+at.get('alttext','[MISSING MATH ALTTEXT]')+'$ ');return
        if self.math:return
        if tag in ('section','div','p','h1','h2','h3','h4','h5','h6','tr'):
            self.out.append('\n')
            if at.get('id'):self.out.append('['+at['id']+'] ')
        if tag=='td':self.out.append(' | ')
    def handle_endtag(self,tag):
        if tag==self.hidden:self.hidden=None;return
        if self.hidden:return
        if tag=='math':self.math=False;return
        if self.math:return
        if tag in ('section','div','p','h1','h2','h3','h4','h5','h6','tr'):self.out.append('\n')
    def handle_data(self,data):
        if not self.math and not self.hidden:self.out.append(data)
e=Extract();e.feed(raw.decode())
lines=[' '.join(l.split()) for l in ''.join(e.out).splitlines()]
txt='\n'.join(l for l in lines if l)+'\n'
(p/'Jin_2608.26698v2_math.txt').write_text(txt)
meta={'url':'https://arxiv.org/html/2608.26698v2','bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),'math_text_bytes':len(txt)}
(p/'Jin_2608.26698v2_metadata.json').write_text(json.dumps(meta,indent=2)+'\n')
print(meta,flush=True)
try:
    data=urllib.request.urlopen('https://arxiv.org/pdf/2608.26698v2',timeout=20).read()
    (p/'Jin_2608.26698v2.pdf').write_bytes(data)
    meta.update(pdf_bytes=len(data),pdf_sha256=hashlib.sha256(data).hexdigest(),pdf_header=str(data[:8]))
    (p/'Jin_2608.26698v2_metadata.json').write_text(json.dumps(meta,indent=2)+'\n')
    print(meta,flush=True)
except Exception as err:
    (p/'Jin_pdf_fetch_error.txt').write_text(type(err).__name__+': '+str(err)+'\n')
    print(type(err).__name__+': '+str(err),flush=True)
