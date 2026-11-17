"""Run inspected local-topology arithmetic on an isolated directory tree."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import hashlib,json,subprocess,sys,time,shutil
ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/'deliverables/code/cdp_audit'
ISOLATED=OUT/'local_topology'
SOURCE=ROOT/'sources/returns/S6_03_CDP/code'
(ISOLATED/'code').mkdir(parents=True,exist_ok=True)
(ISOLATED/'records').mkdir(exist_ok=True)
shutil.copyfile(OUT/'records/D_monodromy_signatures.csv',ISOLATED/'records/D_monodromy_signatures.csv')
names=['E_Hirzebruch.py','root_cusp_product.py','E_vertical_refinements.py','E_elliptic_roots.py','A_zero_curve_index.py']
def run(name):
 src=SOURCE/name;data=src.read_bytes();dst=ISOLATED/'code'/name;dst.write_bytes(data);start=time.time()
 try:
  p=subprocess.run([sys.executable,str(dst)],cwd=ISOLATED,capture_output=True,text=True,timeout=120)
  log=ISOLATED/(name+'.output.txt');log.write_text(p.stdout+'\nSTDERR\n'+p.stderr)
  return dict(source=str(src.relative_to(ROOT)),source_sha256=hashlib.sha256(data).hexdigest(),executed=str(dst.relative_to(ROOT)),executed_sha256=hashlib.sha256(data).hexdigest(),modifications='none',exit_code=p.returncode,elapsed_seconds=round(time.time()-start,3),output=str(log.relative_to(ROOT)),scope='Displayed finite exact polynomial, Seifert, Smith-form, rank and nineteen-signature calculations; analytic/topological proofs were read separately.',checker='GPT-6 Astra (OpenAI, ChatGPT Pro mode), writing run;17 November2026 Europe/Berlin')
 except subprocess.TimeoutExpired:
  return dict(source=str(src.relative_to(ROOT)),exit_code=None,error='Timed out; no successful certificate claimed')
with ThreadPoolExecutor(max_workers=3) as pool:rows=list(pool.map(run,names))
(OUT/'execution_manifest_local_topology.json').write_text(json.dumps(rows,indent=2)+'\n')
for r in rows:print(r['source'],r['exit_code'],r.get('elapsed_seconds',r.get('error')))
