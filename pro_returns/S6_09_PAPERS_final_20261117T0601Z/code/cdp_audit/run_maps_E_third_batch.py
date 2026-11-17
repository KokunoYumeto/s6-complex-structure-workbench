"""Unchanged exact certificates whose complete sources were read in this run."""
import hashlib,json,shutil,subprocess,sys,time
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor,as_completed
ROOT=Path('/workspace/scratch/037cd144174c');SRC=ROOT/'sources/returns/S6_04_MAPS_MANIFOLDS';DST=ROOT/'deliverables/code/cdp_audit/maps_E'
META={'model':'GPT-6 Astra (OpenAI, ChatGPT Pro mode)','effort':'Pro','date':'2026-11-17','timezone':'UTC','reader':'/root/cdp_audit'}
names={'maps_complement_module.py': (['E.2.16'], 'Complete integral torus-knot group-ring operations, actual local chain maps and global cone, all unit cancellations, full peripheral chain columns and exact relation reductions.'), 'maps_splice_module.py': (['E.2.17'], 'Actual infinite amalgam normal form, peripheral chain identities, exact aspherical kernel and all unit/pure-norm reductions;14-generator and12-generator integral coinvariant matrices both checked.'), 'maps_cusp_quadratic.py': (['E.2.18'], 'All base complement code read plus every changed line compared; tracks actual E/U/D cusp cycles through identical cancellations and verifies the universal quadratic identity.'), 'maps_splice_quadratic.py': (['E.2.18'], 'All base splice code read plus every changed line compared; tracks actual t/e inclusions, verifies eight invariant columns and order6 of both displayed coinvariant images.')}
for n in names:shutil.copy2(SRC/'code'/n,DST/'code'/n)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def run(n):
 p=DST/'code'/n;log=p.with_suffix('.rerun.txt');start=time.monotonic()
 with log.open('w') as f:r=subprocess.run([sys.executable,str(p)],cwd=DST,stdout=f,stderr=subprocess.STDOUT)
 checks=[]
 for suffix in ['.out','.stdout.txt','.out.json']:
  original=(SRC/'code'/n).with_suffix(suffix)
  if original.exists():
   actual=p.with_suffix('.out.json') if suffix=='.out.json' else log
   checks.append({'retained_source_output':str(original.relative_to(ROOT)),'retained_sha256':sha(original),'actual_output':str(actual.relative_to(ROOT)),'actual_sha256':sha(actual) if actual.exists() else None,'byte_identical':actual.exists() and actual.read_bytes()==original.read_bytes()})
 return {'program':n,'results':names[n][0],'scope':names[n][1],'reader':META,'program_source_scope':'Every source line and each imported operative helper was read; no modification made.','command':[sys.executable,str(p.relative_to(ROOT))],'cwd':str(DST.relative_to(ROOT)),'source':str((SRC/'code'/n).relative_to(ROOT)),'source_sha256':sha(SRC/'code'/n),'executed':str(p.relative_to(ROOT)),'executed_sha256':sha(p),'modifications':'none','exit_code':r.returncode,'elapsed_seconds':round(time.monotonic()-start,3),'output':str(log.relative_to(ROOT)),'output_sha256':sha(log),'retained_output_checks':checks}
mf=DST/'execution_manifest.json';rows=json.loads(mf.read_text())
with ThreadPoolExecutor(max_workers=3) as pool:
 for f in as_completed([pool.submit(run,n) for n in names]):
  r=f.result();rows=[x for x in rows if x['program']!=r['program']]+[r];mf.write_text(json.dumps(rows,indent=2)+'\n');print(r['program'],r['exit_code'],r['elapsed_seconds'],[(Path(c['retained_source_output']).suffix,c['byte_identical']) for c in r['retained_output_checks']],flush=True)
