"""Rerun inspected finite certificates on isolated, unmodified copies."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import hashlib,json,subprocess,sys,time
ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/'deliverables/code/cdp_audit'
SOURCE=ROOT/'sources/returns/S6_03_CDP/code'
names=['A_minimal_reduction.py','A_nonminimal_maxima.py','E_nonminimal_parent_alignment.py','A_ruled_crossing_contraction.py','D_rooted_kulikov.py','D_truncated_kulikov.py','D_compact_boundary_countermodel.py','E_aligned_parent_reduction.py']
def run(name):
 src=SOURCE/name; data=src.read_bytes(); dst=OUT/name; dst.write_bytes(data); start=time.time()
 try:
  p=subprocess.run([sys.executable,str(dst)],cwd=OUT,capture_output=True,text=True,timeout=300)
  log=OUT/(name+'.output.txt'); log.write_text(p.stdout+'\nSTDERR\n'+p.stderr)
  return dict(source=str(src.relative_to(ROOT)),source_sha256=hashlib.sha256(data).hexdigest(),executed=str(dst.relative_to(ROOT)),executed_sha256=hashlib.sha256(data).hexdigest(),modifications='none',exit_code=p.returncode,elapsed_seconds=round(time.time()-start,3),output=str(log.relative_to(ROOT)),scope='Finite exact arithmetic/graph/chart tests only; E_nonminimal_parent_alignment uses fixed-seed sampled blowup graphs. General analytic proofs are audited separately.',checker='GPT-6 Astra (OpenAI, ChatGPT Pro mode), writing run;17 November2026 Europe/Berlin')
 except subprocess.TimeoutExpired:
  return dict(source=str(src.relative_to(ROOT)),exit_code=None,error='Timed out after300seconds; no successful certificate claimed')
with ThreadPoolExecutor(max_workers=3) as pool:
 rows=list(pool.map(run,names))
(OUT/'execution_manifest_geometric.json').write_text(json.dumps(rows,indent=2)+'\n')
for r in rows: print(r['source'],r['exit_code'],r.get('elapsed_seconds',r.get('error')))
