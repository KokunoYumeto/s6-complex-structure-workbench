"""Read mathematical certificates, isolated from source assembly records."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import hashlib,json,subprocess,sys,time
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'deliverables/code/cdp_audit'
RUN=OUT/'weighted_stars';(RUN/'code').mkdir(parents=True,exist_ok=True);(RUN/'records').mkdir(exist_ok=True)
SOURCE=ROOT/'sources/returns/S6_03_CDP'
(RUN/'records/root_results.csv').write_bytes((SOURCE/'records/root_results.csv').read_bytes())
scopes={
 'E_hopf_graph_reduction.py':'Exact symbolic two-component incidence determinant, one specified branched unicycle, and35 bounded cycle/tail graphs. General graph and analytic residue proofs read separately.',
 'E_hopf_tree_heights.py':'One specified weighted tree linear system,19 finite gauge identities, bounded root congruences and collar powers. No geometric occurrence inference from these equation tests.',
 'root_mixed_hopf_stars.py':'Bounded coprime degree search p,q<=50,m<=10,40 exact insertion maps and bounded secondary cases, with symbolic log-form and common-period identities. CSV writes only to isolated copied input.',
 'D_weighted_hopf_cycles.py':'3456 root/inertia tuples, finite invariant monomial bounds,300 resolution charts,60 secondary lattice cases and exact primary-triangle action. The all-orders local invariant-ring proof is checked separately.',
 'D_all_weighted_cycles.py':'Symbolic target-frame equivariance/affine correction/infinity action/real determinant; all four stated finite-linear examples, plus bounded exponent arithmetic through N=120.'}
def run(item):
 name,scope=item;src=SOURCE/'code'/name;data=src.read_bytes();dst=RUN/'code'/name;dst.write_bytes(data);start=time.time()
 p=subprocess.run([sys.executable,str(dst)],cwd=RUN,capture_output=True,text=True,timeout=120)
 log=RUN/(name+'.output.txt');log.write_text(p.stdout+'\nSTDERR\n'+p.stderr)
 return {'source':str(src.relative_to(ROOT)),'source_sha256':hashlib.sha256(data).hexdigest(),'executed':str(dst.relative_to(ROOT)),'executed_sha256':hashlib.sha256(data).hexdigest(),'modifications':'none; auxiliary input records copied to isolated run tree','exit_code':p.returncode,'elapsed_seconds':round(time.time()-start,3),'output':str(log.relative_to(ROOT)),'scope':scope,'checker':'GPT-6 Astra (OpenAI, ChatGPT Pro mode), effort Pro, writing run; 17 November 2026 UTC'}
with ThreadPoolExecutor(max_workers=3) as pool:rows=list(pool.map(run,scopes.items()))
(OUT/'execution_manifest_weighted_stars.json').write_text(json.dumps(rows,indent=2)+'\n')
for r in rows:print(r['source'],r['exit_code'],r['elapsed_seconds'])
