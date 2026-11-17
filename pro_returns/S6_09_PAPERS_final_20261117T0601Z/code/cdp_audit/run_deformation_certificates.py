"""Rerun six fully inspected source programs, unmodified, in an isolated copy."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import hashlib,json,subprocess,sys,time
ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/'deliverables/code/cdp_audit'
RUN=OUT/'deformations';RUN.mkdir(exist_ok=True)
SOURCE=ROOT/'sources/returns/S6_03_CDP/code'
scopes={
 'E_checks.py':'Exact E5 boundary determinant, E8 heat identity, E10 disjointness, E13 residue determinant, E14 cusp jet; E11 finite sample of coprime k,l<=40, not an exhaustive proof.',
 'E_theta_numeric.py':'Two numerical methods at 70 digits and two specified period points. Floating-point consistency only; no interval certificate or proof claim.',
 'E_counterexamples.py':'Exact square-zero truncations and E10 cohomology, plus two floating-point E18 calculations at 70 digits. Finite samples and numerical checks are not general proofs.',
 'E_topology.py':'Exact marking, exterior-square Smith form, primitive kernel, norm pairing and symbolic gluing determinant. Additional bounded admissible samples test the Smith form; the general Smith proof is separate.',
 'C_jets.py':'Exact tacnode numerator covariance, diagonal cubic-discriminant weight, double-pole linear systems and bounded cusp valuation check.',
 'C_euler.py':'Exact listed blowup Betti/Euler arithmetic and twelve quotient triangulations; the geometric construction is independently read.'}
def run(item):
 name,scope=item;src=SOURCE/name;data=src.read_bytes();dst=RUN/name;dst.write_bytes(data);start=time.time()
 try:
  p=subprocess.run([sys.executable,str(dst)],cwd=RUN,capture_output=True,text=True,timeout=120)
  log=RUN/(name+'.output.txt');log.write_text(p.stdout+'\nSTDERR\n'+p.stderr)
  return {'source':str(src.relative_to(ROOT)),'source_sha256':hashlib.sha256(data).hexdigest(),'executed':str(dst.relative_to(ROOT)),'executed_sha256':hashlib.sha256(data).hexdigest(),'modifications':'none','exit_code':p.returncode,'elapsed_seconds':round(time.time()-start,3),'output':str(log.relative_to(ROOT)),'scope':scope,'checker':'GPT-6 Astra (OpenAI, ChatGPT Pro mode), effort Pro, writing run; 17 November 2026 UTC'}
 except subprocess.TimeoutExpired:
  return {'source':str(src.relative_to(ROOT)),'exit_code':None,'error':'Timed out; no successful check claimed'}
with ThreadPoolExecutor(max_workers=3) as pool:rows=list(pool.map(run,scopes.items()))
(OUT/'execution_manifest_deformations.json').write_text(json.dumps(rows,indent=2)+'\n')
for r in rows:print(r['source'],r['exit_code'],r.get('elapsed_seconds',r.get('error')))
