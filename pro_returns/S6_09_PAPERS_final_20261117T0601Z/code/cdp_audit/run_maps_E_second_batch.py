"""Unchanged exact certificates whose complete sources were read in this run."""
import hashlib,json,shutil,subprocess,sys,time
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor,as_completed
ROOT=Path('/workspace/scratch/037cd144174c');SRC=ROOT/'sources/returns/S6_04_MAPS_MANIFOLDS';DST=ROOT/'deliverables/code/cdp_audit/maps_E'
META={'model':'GPT-6 Astra (OpenAI, ChatGPT Pro mode)','effort':'Pro','date':'2026-11-17','timezone':'UTC','reader':'/root/cdp_audit'}
names={
'maps_shifted_pi2.py':(['E.2.10','E.2.11'],'All sixteen integral boundary-sign cases, retained-coordinate vanishing, order12 image witness, radical and primitive-extension Smith form. Full group-ring homotopy is not inferred.'),
'manifolds_cusp_alexander.py':(['E.2.12'],'Exact Laurent normalization matrix with both explicit unimodular transformations. The normalization spectral sequence and geometric cover are receiving-proof inputs.'),
'maps_shifted_circle.py':(['E.2.13'],'Integral relation Smith form, primitive character, all cone-image orders, genus6 cover, central basis and signed weighted-Hopf connection integral.'),
'maps_shifted_return.py':(['E.2.14'],'Full rational boundary matrices, common images, primitive torus contraction, all variation ranks and Wang Jordan counts.'),
'maps_shifted_cover.py':(['E.2.14'],'All six cyclotomic character orders with exact companion matrices, actual affine transports and every exterior degree.'),
'maps_shifted_cover_integral.py':(['E.2.15'],'Regular12-sheet permutation integral coefficients; Hermite image bases and full Smith primitivity in every exterior degree.'),
'maps_shifted_fibre_integral.py':(['E.2.15'],'Verified full Smith basis transformations, saturated boundary images, common-image integral kernel, all torsion residues and divisibility72. Geometric image primitivity is proved separately.'),
'maps_cusp_smooth_plumbing.py':(['E.2.19'],'All six unimodular charts, Picard intersections, normal-degree-1, q-preserving opposite pair involution, exact triple rotations and original boundary monodromy.'),
'maps_finite_cap_framings.py':(['E.2.20'],'Both finite affine actions, complete product normal coordinates, unimodular angular inverses, mapping-torus seams and actual meridians.'),
'maps_ordinary_handles.py':(['E.2.4','E.2.21'],'All monomial charts and sector seams, six distinct endpoint placements and two normal rotations, full finite76/2432 handle inventories. Smooth comparison is the separately checked full geometric proof.')}
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
