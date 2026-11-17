from pathlib import Path
import urllib.request, json, hashlib, concurrent.futures, subprocess
root=Path('/workspace/scratch/037cd144174c')
out=root/'sources/external/maps_audit';out.mkdir(parents=True,exist_ok=True)
urls={
'knudson':'https://arxiv.org/pdf/math/0409133',
'hatcher':'https://pi.math.cornell.edu/~hatcher/AT/AT.pdf',
'brown_collars':'https://www.maths.gla.ac.uk/~mpowell/Brown%20collars.pdf',
'cox_little_schenck':'https://pi.math.cornell.edu/~tsh/cornell-only/cox-little-schenck-toric.pdf',
'fintushel_pao':'https://msp.org/pjm/1983/109-2/pjm-v109-n2-p09-p.pdf',
'davis':'https://people.math.osu.edu/davis.12/old_papers/AJM-82.pdf',
'haefliger':'https://www.maths.ed.ac.uk/~v1ranick/tda/haefliger.pdf',
'wall6':'https://webhomes.maths.ed.ac.uk/~v1ranick/papers/wclass5.pdf',
'eells_kuiper':'https://webhomes.maths.ed.ac.uk/~v1ranick/papers/eellskuiper.pdf',
'kervaire_milnor':'https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/kervaire-milnor.pdf',
'chern_simons':'https://math.mit.edu/juvitop/pastseminars/notes_2019_Fall/Chern-Simons.pdf',
}
def fetch(kv):
 k,u=kv;p=out/(k+'.pdf');r={'key':k,'url':u,'file':str(p.relative_to(root))}
 try:
  if not p.exists():
   request=urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'})
   with urllib.request.urlopen(request,timeout=30) as response:data=response.read()
   if not data.startswith(b'%PDF'):raise ValueError('not PDF')
   p.write_bytes(data)
  r.update(bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),retrieval='success; not yet read')
  subprocess.run(['pdftotext','-layout',str(p),str(p.with_suffix('.txt'))],capture_output=True)
 except Exception as e:r.update(retrieval='failed',error=str(e))
 return r
record=[]
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as e:
 for r in e.map(fetch,urls.items()):
  record.append(r);print(r,flush=True)
  (root/'deliverables/work/maps_audit/topology_source_retrieval.json').write_text(json.dumps(record,indent=2))
