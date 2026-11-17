"""Retain genuine primary PDFs already opened in the local-topology audit."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from urllib.request import Request,urlopen
import hashlib,json
ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/'reference_downloads/cdp_audit'
sources={
'Nemethi1991Join':'https://www.numdam.org/article/CM_1991__80_1_1_0.pdf',
'MPW2005Hirzebruch':'https://arxiv.org/pdf/math/0509451',
'vanStraten1987':'https://download.uni-mainz.de/mathematik/Algebraische%20Geometrie/DvS-Publikationen/DvS_1987_weakly%20normal%20Surface%20Singularities%20and%20their%20improvements.pdf',
'Steenbrink1999':'https://arxiv.org/pdf/math/9902134',
'Rossi2017':'https://arxiv.org/pdf/1211.6329',
}
def get(item):
 key,url=item;r={'key':key,'url':url}
 try:
  with urlopen(Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=35) as f:data=f.read();r['resolved_url']=f.url
  if not data.startswith(b'%PDF'):raise ValueError('Response was not a PDF; no source file claimed')
  p=OUT/(key+'.pdf');p.write_bytes(data)
  r.update(status='downloaded actual PDF',path=str(p.relative_to(ROOT)),sha256=hashlib.sha256(data).hexdigest(),bytes=len(data))
 except Exception as e:r.update(status='download failed',error=str(e))
 return r
with ThreadPoolExecutor(max_workers=5) as pool:rows=list(pool.map(get,sources.items()))
(OUT/'downloads_local_topology.json').write_text(json.dumps(rows,indent=2)+'\n')
for r in rows:print(r['key'],r['status'],r.get('bytes',r.get('error')))
