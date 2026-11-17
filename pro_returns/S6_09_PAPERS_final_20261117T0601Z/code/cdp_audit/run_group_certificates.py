"""Rerun three read source certificates without changing any source file."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import hashlib,json,subprocess,sys,time
ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/'deliverables/code/cdp_audit'
RUN=OUT/'groups';RUN.mkdir(exist_ok=True)
SOURCE=ROOT/'sources/returns/S6_03_CDP/code'
scopes={
 'A_meridian_groups.py':'539 fixed-seed exact tuples over seven specified integral monodromies and seven multiplicity vectors, eleven seeds each. Compares Smith invariants, T-stability and extension abelianization; no geometric occurrence or exhaustive all-matrix claim.',
 'D_cyclic_k3.py':'Exact four symplectic cyclic orders 2,3,4,6: all powers, fixed isogeny degrees, stabilizer orbits, quotient singularities and Euler24 resolutions.',
 'root_cyclic_elliptic_types.py':'Exact finite characters for cyclic elliptic-base orders2,3,4,6 and four rational-base actions; Riemann–Hurwitz, Euler and character identities. Local Kodaira type dictionary is geometric input, not independently established by this program.'}
def run(item):
 name,scope=item;src=SOURCE/name;data=src.read_bytes();dst=RUN/name;dst.write_bytes(data);start=time.time()
 p=subprocess.run([sys.executable,str(dst)],cwd=RUN,capture_output=True,text=True,timeout=120)
 log=RUN/(name+'.output.txt');log.write_text(p.stdout+'\nSTDERR\n'+p.stderr)
 return {'source':str(src.relative_to(ROOT)),'source_sha256':hashlib.sha256(data).hexdigest(),'executed':str(dst.relative_to(ROOT)),'executed_sha256':hashlib.sha256(data).hexdigest(),'modifications':'none','exit_code':p.returncode,'elapsed_seconds':round(time.time()-start,3),'output':str(log.relative_to(ROOT)),'scope':scope,'checker':'GPT-6 Astra (OpenAI, ChatGPT Pro mode), effort Pro, writing run; 17 November 2026 UTC'}
with ThreadPoolExecutor(max_workers=3) as pool:rows=list(pool.map(run,scopes.items()))
(OUT/'execution_manifest_groups.json').write_text(json.dumps(rows,indent=2)+'\n')
for r in rows:print(r['source'],r['exit_code'],r['elapsed_seconds'])
