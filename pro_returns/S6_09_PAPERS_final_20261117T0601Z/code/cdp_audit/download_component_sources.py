"""Fetch published primary sources; a successful status requires PDF bytes."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from urllib.request import Request,urlopen
import hashlib,json
ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/'reference_downloads/cdp_audit'
sources={
'Buchdahl1999':'https://www.numdam.org/article/AIF_1999__49_1_287_0.pdf',
'Catanese2002':'https://arxiv.org/pdf/math/0111245',
'AKMW2002':'https://arxiv.org/pdf/math/9904135',
'Fujimoto1988Log':'https://scispace.com/pdf/logarithmic-transformations-on-elliptic-fiber-spaces-1uinrvp8jj.pdf',
}
def get(item):
 key,url=item; r={'key':key,'url':url}
 try:
  with urlopen(Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=35) as f: data=f.read();r['resolved_url']=f.url
  if not data.startswith(b'%PDF'): raise ValueError('Response was not a PDF; no source file claimed')
  p=OUT/(key+'.pdf');p.write_bytes(data)
  r.update(status='downloaded actual PDF',path=str(p.relative_to(ROOT)),sha256=hashlib.sha256(data).hexdigest(),bytes=len(data))
 except Exception as e: r.update(status='download failed',error=str(e))
 return r
with ThreadPoolExecutor(max_workers=4) as pool: rows=list(pool.map(get,sources.items()))
(OUT/'downloads_components.json').write_text(json.dumps(rows,indent=2)+'\n')
for r in rows:print(r['key'],r['status'],r.get('bytes',r.get('error')))
