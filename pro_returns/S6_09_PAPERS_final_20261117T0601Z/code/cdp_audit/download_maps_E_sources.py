import urllib.request,hashlib,json,subprocess
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor,as_completed
D=Path('/workspace/scratch/037cd144174c/reference_downloads/maps_E');D.mkdir(exist_ok=True,parents=True)
urls={
'Scott1983':'https://courses.mai.liu.se/GU/TA1022/Scott.pdf',
'DavisKirk2001':'https://webhomes.maths.ed.ac.uk/~v1ranick/papers/davkir.pdf',
'Hirsch1976':'https://people.dm.unipi.it/benedett/HIRSCH.pdf',
'Whitehead1950':'https://webhomes.maths.ed.ac.uk/~v1ranick/papers/jhcw10.pdf',
'Vogel2009':'https://annals.math.princeton.edu/wp-content/uploads/annals-v169-n1-p03.pdf',
'Milnor1965':'https://www.math.auckland.ac.nz/~hekmati/Books/Milnor2.pdf',
'Winter2008':'https://arxiv.org/pdf/0711.1638v3',
'PetersSterk2024':'https://www-fourier.univ-grenoble-alpes.fr/~peters/Books/QuadraticForms/QuadForms.pdf'}
def get(k,u):
 p=D/(k+'.pdf')
 try:
  if not p.exists():
   with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=45) as r:b=r.read()
   if not b.startswith(b'%PDF'):raise ValueError('not PDF')
   p.write_bytes(b)
  b=p.read_bytes();subprocess.run(['pdftotext','-layout',str(p),str(p.with_suffix('.txt'))],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
  return {'key':k,'url':u,'path':str(p),'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b),'status':'downloaded; reading scope recorded separately'}
 except Exception as e:return {'key':k,'url':u,'status':'download failed','error':str(e)}
out=D/'download_manifest.json';rows=json.loads(out.read_text()) if out.exists() else []
with ThreadPoolExecutor(max_workers=4) as e:
 for f in as_completed([e.submit(get,k,u) for k,u in urls.items()]):
  r=f.result();rows=[x for x in rows if x['key']!=r['key']]+[r];out.write_text(json.dumps(rows,indent=2)+'\n');print(r['key'],r['status'],r.get('bytes',''),flush=True)
