from pathlib import Path
import urllib.request,hashlib,json,datetime,subprocess,concurrent.futures
L=Path('/workspace/scratch/653608133b22/work/agents/i_provenance/literature')
items=[('McHugh2018v4','https://arxiv.org/pdf/1708.03251v4'),('Angella2017v2','https://arxiv.org/pdf/1705.10518v2'),('ConradSL2Z','https://kconrad.math.uconn.edu/blurbs/grouptheory/SL(2,Z).pdf')]
def get(it):
 n,u=it;p=L/f'S6_SERIES_PUBLISH_I_{n}.pdf';r={'name':n,'url':u,'retrieved_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 try:
  with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=50) as f:data=f.read();r['http_status']=f.status;r['resolved_url']=f.url
  assert data.startswith(b'%PDF');p.write_bytes(data);r.update(path=str(p),sha256=hashlib.sha256(data).hexdigest(),bytes=len(data));subprocess.run(['pdftotext','-layout',str(p),str(p.with_suffix('.txt'))],check=True,capture_output=True)
 except Exception as e:r['error']=str(e)
 return r
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:r=list(ex.map(get,items))
(L/'S6_SERIES_PUBLISH_I_locator_batch05_retrieval.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
for name,pp in [('McHugh2018v4',range(20,26)),('Angella2017v2',range(13,17))]:
 p=L/f'S6_SERIES_PUBLISH_I_{name}.pdf'
 if p.exists():
  for n in pp:subprocess.run(['pdftoppm','-f',str(n),'-l',str(n),'-scale-to','1700','-png','-singlefile',str(p),str(L/f'S6_SERIES_PUBLISH_I_{name}_p{n:03d}')],check=True,capture_output=True)
P=Path('/workspace/scratch/653608133b22/work/agents/provenance/literature/S6_SERIES_PUBLISH_Engel.pdf')
for n in [6,11]:subprocess.run(['pdftoppm','-f',str(n),'-l',str(n),'-scale-to','1700','-png','-singlefile',str(P),str(L/f'S6_SERIES_PUBLISH_I_Engel_p{n:03d}')],check=True,capture_output=True)
P=L/'S6_SERIES_PUBLISH_I_AC26_primary.pdf'
for n in [51,52,53,54,55,56,61,62,63,101,102,103,104,105]:
 q=L/f'S6_SERIES_PUBLISH_I_AC26_p{n:03d}.png'
 if not q.exists():subprocess.run(['pdftoppm','-f',str(n),'-l',str(n),'-scale-to','1700','-png','-singlefile',str(P),str(q.with_suffix(''))],check=True,capture_output=True)
print('renders complete')
