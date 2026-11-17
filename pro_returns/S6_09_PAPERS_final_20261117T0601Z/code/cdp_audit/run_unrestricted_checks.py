"""Rerun inspected exact certificates on isolated copies; retain limited scope."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import hashlib,json,subprocess,sys,time
ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/'deliverables/code/cdp_audit'; SOURCE=ROOT/'sources/returns/S6_03_CDP'
names=['root_exceptional_leaves.py','A_translation_exceptions.py','A_torsion_interfaces.py','D_trivial_canonical.py','D_flat_toric.py','D_toric_gluing.py','E_k3_quotient_descent.py','root_maximal_hopf_leaf.py']
(OUT/'records/root_results.csv').write_bytes((SOURCE/'records/root_results.csv').read_bytes())
def run(name):
 src=SOURCE/'code'/name;data=src.read_bytes();edited=data
 if name=='root_exceptional_leaves.py':
  edited=data.replace(b'root = Path(__file__).resolve().parents[1]',b'root = Path(__file__).resolve().parent')
 dst=OUT/name;dst.write_bytes(edited);start=time.time()
 try:
  p=subprocess.run([sys.executable,str(dst)],cwd=OUT,capture_output=True,text=True,timeout=120)
  log=OUT/(name+'.output.txt');log.write_text(p.stdout+'\nSTDERR\n'+p.stderr)
  return dict(source=str(src.relative_to(ROOT)),source_sha256=hashlib.sha256(data).hexdigest(),executed=str(dst.relative_to(ROOT)),executed_sha256=hashlib.sha256(edited).hexdigest(),modifications='redirect output root to audit copy' if edited!=data else 'none',exit_code=p.returncode,elapsed_seconds=round(time.time()-start,3),output=str(log.relative_to(ROOT)),scope='Finite exact algebra/graph certificates only; general analytic proofs remain separate',checker='GPT-6 Astra (OpenAI, ChatGPT Pro mode), writing run;17 November2026 Europe/Berlin')
 except subprocess.TimeoutExpired as e:
  return dict(source=str(src.relative_to(ROOT)),exit_code=None,error='Timed out after120seconds',scope='No successful certificate claimed')
with ThreadPoolExecutor(max_workers=3) as pool: rows=list(pool.map(run,names))
(OUT/'execution_manifest_unrestricted.json').write_text(json.dumps(rows,indent=2)+'\n')
for row in rows:print(row['source'],row['exit_code'],row.get('elapsed_seconds',row.get('error')))
