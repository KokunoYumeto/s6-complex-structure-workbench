"""Run fully inspected certificates in a separate code/records tree."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import hashlib,json,subprocess,sys,time
ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/'deliverables/code/cdp_audit'
RUN=OUT/'cycles';(RUN/'code').mkdir(parents=True,exist_ok=True);(RUN/'records').mkdir(exist_ok=True)
SOURCE=ROOT/'sources/returns/S6_03_CDP'
(RUN/'records/root_results.csv').write_bytes((SOURCE/'records/root_results.csv').read_bytes())
scopes={
 'A_twistor_log_cycles.py':'Full symbolic four-period determinant, transverse determinant, inverse real-linear map, infinity frame, and exact unipotent rank-one monodromy. Compact analytic gluing is independently read.',
 'root_all_diagonal_cycles.py':'Full symbolic global determinant and conjugate Hopf frame/contracting-log identities; free secondary characters with orders1..24 only. Its CSV publication operates only on the copied records tree.',
 'D_hopf_cycle_matrices.py':'Exact two-edge identity equations, the explicit three-cycle matrices/logarithms, affine normal-constant solution, and bounded secondary HNF divisibility samples with orders1..24 and repetitions1..6.',
 'A_mixed_cycles.py':'169 exact mixed-cycle samples with a,b in1..13, separate ruled frames and normal-period comparison; symbolic retention of arbitrary horizontal all-ruled translation.'}
def run(item):
 name,scope=item;src=SOURCE/'code'/name;data=src.read_bytes();dst=RUN/'code'/name;dst.write_bytes(data);start=time.time()
 p=subprocess.run([sys.executable,str(dst)],cwd=RUN,capture_output=True,text=True,timeout=120)
 log=RUN/(name+'.output.txt');log.write_text(p.stdout+'\nSTDERR\n'+p.stderr)
 return {'source':str(src.relative_to(ROOT)),'source_sha256':hashlib.sha256(data).hexdigest(),'executed':str(dst.relative_to(ROOT)),'executed_sha256':hashlib.sha256(data).hexdigest(),'modifications':'none; auxiliary input records copied to isolated run tree','exit_code':p.returncode,'elapsed_seconds':round(time.time()-start,3),'output':str(log.relative_to(ROOT)),'scope':scope,'checker':'GPT-6 Astra (OpenAI, ChatGPT Pro mode), effort Pro, writing run; 17 November 2026 UTC'}
with ThreadPoolExecutor(max_workers=3) as pool:rows=list(pool.map(run,scopes.items()))
(OUT/'execution_manifest_cycles.json').write_text(json.dumps(rows,indent=2)+'\n')
for r in rows:print(r['source'],r['exit_code'],r['elapsed_seconds'])
