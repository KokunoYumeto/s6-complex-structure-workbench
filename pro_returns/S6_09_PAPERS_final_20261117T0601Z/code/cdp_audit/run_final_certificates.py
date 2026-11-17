"""Re-run unchanged tree certificates in a separate output directory."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import hashlib,json,subprocess,sys,time
ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/'deliverables/code/cdp_audit'
RUN=OUT/'final_certificates';RUN.mkdir(parents=True,exist_ok=True)
SOURCE=ROOT/'sources/returns/S6_03_CDP/code'
scopes={'E_weighted_elliptic_trees.py': 'UN63 exact signed-edge, finite-character jet, weighted insertion and invariant-ring identities; bounded cyclotomic and integer ranges are supplemental checks, not analytic existence proofs.', 'D_complete_rooted_generation.py': 'UN86 canonical-character descent, intrinsic ratio branch, normalized invariant monoids and signed Euler composition; geometric existence is checked in the full text.', 'E_weighted_flat_toric.py': 'UN76 root lattice, primitive canonical ratio, finite affine iteration and compact-middle determinant identities; proper analytic occurrence is proved separately.', 'E_toric_compact_period_audit.py': 'UN73 symbolic real determinant identity for arbitrary symmetric metric and skew part; positivity follows from the separately checked displayed inequalities.', 'E_nonlinear_star_criterion.py': 'UN49 integral boundary identities, bounded nonlinear canonical periods, symbolic twistor inverse and torsor translations.', 'E_secondary_star_criterion.py': 'UN50 coprime integer charts through20, Bezout boundary bases and exact secondary period with full finite order.', 'E_hopf_boundary.py': 'UN38 invariant canonical forms for resonances1..8 and bounded resonant Laurent identities; the all-order argument is checked in the proof.'}
def run(item):
 name,scope=item;src=SOURCE/name;data=src.read_bytes();dst=RUN/name;dst.write_bytes(data);start=time.time()
 p=subprocess.run([sys.executable,str(dst)],cwd=RUN,capture_output=True,text=True,timeout=300)
 log=RUN/(name+'.output.txt');log.write_text(p.stdout+'\nSTDERR\n'+p.stderr)
 original_out=src.with_suffix('.out')
 original_match=original_out.exists() and original_out.read_bytes()==p.stdout.encode()
 return {'source':str(src.relative_to(ROOT)),'source_sha256':hashlib.sha256(data).hexdigest(),'executed':str(dst.relative_to(ROOT)),'executed_sha256':hashlib.sha256(data).hexdigest(),'command':[sys.executable,str(dst.relative_to(ROOT))],'modifications':'none; original files not changed','exit_code':p.returncode,'elapsed_seconds':round(time.time()-start,3),'output':str(log.relative_to(ROOT)),'stdout_matches_original_out':original_match,'scope':scope,'checker':'GPT-6 Astra (OpenAI, ChatGPT Pro mode), effort Pro, writing run; 17 November 2026 UTC'}
with ThreadPoolExecutor(max_workers=4) as pool:rows=list(pool.map(run,scopes.items()))
(OUT/'execution_manifest_final_certificates.json').write_text(json.dumps(rows,indent=2)+'\n')
for r in rows:print(r['source'],r['exit_code'],r['elapsed_seconds'],r['stdout_matches_original_out'])
