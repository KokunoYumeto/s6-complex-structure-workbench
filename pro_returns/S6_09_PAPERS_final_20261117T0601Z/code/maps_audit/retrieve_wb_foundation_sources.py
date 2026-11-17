from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
import urllib.request, hashlib, json, subprocess
root=Path('sources/external/maps_audit'); root.mkdir(parents=True,exist_ok=True)
jobs=[
('beardon1983','https://pdfcoffee.com/the-geometry-of-discrete-groups-alan-f-beardon-pdf-free.html','html'),
('brown1982','https://ru.djvu.online/file/QtlfpGD38sXAT','html'),
('fulton1993','https://www.scribd.com/document/768783720/Introduction-to-Toric-Varieties-Fulton','html'),
('serre1973','https://www.math.purdue.edu/~jlipman/MA598/Serre-Course%20in%20Arithmetic.pdf','pdf'),
('cox_little_schenck2011','https://pi.math.cornell.edu/~tsh/cornell-only/cox-little-schenck-toric.pdf','pdf'),
('cartan1954_quotient','https://www.numdam.org/item/SHC_1953-1954__6__A12_0.pdf','pdf')]
def get(job):
 k,u,ext=job; p=root/(k+'.'+ext); r={'key':k,'url':u,'source':str(p),'date':'2026-11-17','status':'retrieved; not yet opened'}
 try:
  req=urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'})
  with urllib.request.urlopen(req,timeout=25) as resp: data=resp.read()
  p.write_bytes(data); r['sha256']=hashlib.sha256(data).hexdigest();r['bytes']=len(data)
  if ext=='pdf':
   if not data.startswith(b'%PDF'): raise ValueError('Response is not PDF')
   subprocess.run(['pdftotext','-layout',str(p),str(p.with_suffix('.txt'))],check=True)
  else:
   from bs4 import BeautifulSoup
   soup=BeautifulSoup(data,'html.parser')
   for q in soup(['script','style','nav','footer','header']):q.decompose()
   p.with_suffix('.txt').write_text(soup.get_text('\n',strip=True))
 except Exception as e:r['status']='Failed: '+str(e)
 return r
out=[]
with ThreadPoolExecutor(max_workers=6) as ex:
 for f in as_completed([ex.submit(get,j) for j in jobs]):
  r=f.result();out.append(r);print(json.dumps(r),flush=True)
  Path('deliverables/work/maps_audit/wb_foundation_retrieval.json').write_text(json.dumps(out,indent=2)+'\n')
