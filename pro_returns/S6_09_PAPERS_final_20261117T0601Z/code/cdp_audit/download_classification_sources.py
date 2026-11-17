"""Fetch original statements used by the compact-surface classification audit."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from urllib.request import Request,urlopen
import hashlib,json
ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/'reference_downloads/cdp_audit'
sources={
'Peters2021':'https://nyjm.albany.edu/j/2021/27-32p.pdf',
'BMS2012':'https://mathweb.tifr.res.in/~mahan/kahler3fld.pdf',
'Peters1990':'https://cpeters1.win.tue.nl/ConfsAndSchools/Canada/surface.pdf',
'Teleman2008':'https://www.i2m.univ-amu.fr/perso/andrei.teleman/documents/postnikov.pdf',
'BBK2019':'https://arxiv.org/pdf/1709.00062',
'Kawai1969':'https://www.jstage.jst.go.jp/article/jmath1948/21/4/21_4_604/_pdf/-char/en',
'SS2002':'https://arxiv.org/pdf/math/0001077',
}
def get(item):
 key,url=item; r={'key':key,'url':url}
 try:
  with urlopen(Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=40) as f: data=f.read();r['resolved_url']=f.url
  if not data.startswith(b'%PDF'): raise ValueError('Response was not a PDF; no source file claimed')
  p=OUT/(key+'.pdf');p.write_bytes(data)
  r.update(status='downloaded actual PDF',path=str(p.relative_to(ROOT)),sha256=hashlib.sha256(data).hexdigest(),bytes=len(data))
 except Exception as e:r.update(status='download failed',error=str(e))
 return r
with ThreadPoolExecutor(max_workers=4) as pool:rows=list(pool.map(get,sources.items()))
(OUT/'downloads_classification.json').write_text(json.dumps(rows,indent=2)+'\n')
for r in rows:print(r['key'],r['status'],r.get('bytes',r.get('error')))
