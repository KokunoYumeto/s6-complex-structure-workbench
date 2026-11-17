"""Rerun only source-read MAPS E certificates, without changing originals."""
import hashlib,json,shutil,subprocess,sys,time
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor,as_completed
ROOT=Path('/workspace/scratch/037cd144174c')
SRC=ROOT/'sources/returns/S6_04_MAPS_MANIFOLDS'
DST=ROOT/'deliverables/code/cdp_audit/maps_E';(DST/'code').mkdir(parents=True,exist_ok=True);(DST/'records').mkdir(exist_ok=True)
meta={'model':'GPT-6 Astra (OpenAI, ChatGPT Pro mode)','effort':'Pro','date':'2026-11-17','timezone':'UTC'}
names={
 'fourfolds_checks.py':{'results':['E.1.4','E.2.1','E.2.3'],'scope':'Finite elliptic coinvariants, affine quotient H1, shifted group abelianization, root-line degrees and complete rational shifted-product d2 matrices. It does not compute the fourfold E2 exterior row.'},
 'fourfolds_shifted_integral.py':{'results':['E.2.5'],'scope':'Exact degree1/2 exterior matrices, integral coboundary/coinvariant primitivity and the18-row finite cokernel. Higher extensions are not computed by this program.'},
 'manifolds_shifted_mv.py':{'results':['E.2.6'],'scope':'Every full integral MV matrix for all sixteen independent boundary-adjoint sign choices. Geometric decomposition and boundary adjoints are checked in the full proof separately.'},
 'shifted_group_bordism.py':{'results':['E.2.9'],'scope':'Group relation Smith form, primitive abelian character, orbifold Euler and elementary stable-product arithmetic. Stable stems and geometric bordism are theorem/proof inputs, not computed here.'}}
for name in names:shutil.copy2(SRC/'code'/name,DST/'code'/name)
def run(name):
 p=DST/'code'/name; log=p.with_suffix('.rerun.txt');start=time.monotonic()
 with log.open('w') as out:r=subprocess.run([sys.executable,str(p)],cwd=DST,stdout=out,stderr=subprocess.STDOUT)
 original=(SRC/'code'/name).read_bytes();expected=SRC/'code'/name.replace('.py','.out')
 return {'program':name,**names[name],'reader':meta,'command':[sys.executable,str(p.relative_to(ROOT))],'cwd':str(DST.relative_to(ROOT)),'source':str((SRC/'code'/name).relative_to(ROOT)),'source_sha256':hashlib.sha256(original).hexdigest(),'executed':str(p.relative_to(ROOT)),'executed_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'modifications':'none','exit_code':r.returncode,'elapsed_seconds':round(time.monotonic()-start,3),'output':str(log.relative_to(ROOT)),'stdout_matches_retained_source_output':log.read_bytes()==expected.read_bytes() if expected.exists() else None}
manifest=DST/'execution_manifest.json';rows=json.loads(manifest.read_text()) if manifest.exists() else []
with ThreadPoolExecutor(max_workers=3) as ex:
 for future in as_completed({ex.submit(run,n):n for n in names}):
  r=future.result();rows=[x for x in rows if x['program']!=r['program']]+[r];manifest.write_text(json.dumps(rows,indent=2)+'\n');print(r['program'],r['exit_code'],r['elapsed_seconds'],flush=True)
