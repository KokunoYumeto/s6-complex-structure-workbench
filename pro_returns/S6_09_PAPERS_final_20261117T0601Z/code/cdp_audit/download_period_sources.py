"""Download the exact primary period-family sources used in the audit."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from urllib.request import Request,urlopen
import hashlib,json,subprocess
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'reference_downloads/cdp_audit'
sources={
'Borcea1984':'https://www.numdam.org/article/CM_1984__52_3_373_0.pdf',
'KhaledTeleman2026':'https://arxiv.org/pdf/2406.15158',
}
def get(item):
 key,url=item;r={'key':key,'url':url}
 try:
  with urlopen(Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=35) as f:data=f.read();r['resolved_url']=f.url
  if not data.startswith(b'%PDF'):raise ValueError('Response was not a PDF')
  p=OUT/(key+'.pdf');p.write_bytes(data)
  r.update(status='downloaded actual PDF',path=str(p.relative_to(ROOT)),sha256=hashlib.sha256(data).hexdigest(),bytes=len(data))
  subprocess.run(['pdftotext','-layout',str(p),str(p.with_suffix('.txt'))],check=True)
 except Exception as e:r.update(status='download failed',error=str(e))
 return r
with ThreadPoolExecutor(max_workers=2) as pool:rows=list(pool.map(get,sources.items()))
(OUT/'downloads_periods.json').write_text(json.dumps(rows,indent=2)+'\n')
for r in rows:print(r['key'],r['status'],r.get('bytes',r.get('error')))
