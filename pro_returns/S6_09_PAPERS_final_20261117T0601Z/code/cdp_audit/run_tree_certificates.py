"""Re-run unchanged tree certificates in a separate output directory."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import hashlib,json,subprocess,sys,time
ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/'deliverables/code/cdp_audit'
RUN=OUT/'trees';RUN.mkdir(parents=True,exist_ok=True)
SOURCE=ROOT/'sources/returns/S6_03_CDP/code'
scopes={
 'E_hopf_tree_pruning.py':'120 primitive SL2 basis changes,400 two-mark Picard Smith forms, bounded exact weighted insertions and one complete nested height record. The sheaf classification and global analytic replacement are proved separately.',
 'A_rooted_hopf_trees.py':'30 specified chains,stars and binary trees through10 nonroot vertices; symbolic central-extension associativity/commutator and exact analytic-torsor determinant. General leaf elimination and actual group injection are checked in the written proof.',
 'A_tree_periods.py':'Exact symbolic primitive elliptic period coefficient and bounded insertion-order identities for m1..15 and orders through24. No global geometric existence is inferred from the finite loop.',
 'D_quasibundle_trees.py':'60 exact root-line charts,9600 canonical pole inequalities, the stated six-component incidence matrix and plurigenus arithmetic through120. The genuine analytic root-torsor construction is checked separately.'}
def run(item):
 name,scope=item;src=SOURCE/name;data=src.read_bytes();dst=RUN/name;dst.write_bytes(data);start=time.time()
 p=subprocess.run([sys.executable,str(dst)],cwd=RUN,capture_output=True,text=True,timeout=120)
 log=RUN/(name+'.output.txt');log.write_text(p.stdout+'\nSTDERR\n'+p.stderr)
 original_out=src.with_suffix('.out')
 original_match=original_out.exists() and original_out.read_bytes()==p.stdout.encode()
 return {'source':str(src.relative_to(ROOT)),'source_sha256':hashlib.sha256(data).hexdigest(),'executed':str(dst.relative_to(ROOT)),'executed_sha256':hashlib.sha256(data).hexdigest(),'command':[sys.executable,str(dst.relative_to(ROOT))],'modifications':'none; original files not changed','exit_code':p.returncode,'elapsed_seconds':round(time.time()-start,3),'output':str(log.relative_to(ROOT)),'stdout_matches_original_out':original_match,'scope':scope,'checker':'GPT-6 Astra (OpenAI, ChatGPT Pro mode), effort Pro, writing run; 17 November 2026 UTC'}
with ThreadPoolExecutor(max_workers=4) as pool:rows=list(pool.map(run,scopes.items()))
(OUT/'execution_manifest_trees.json').write_text(json.dumps(rows,indent=2)+'\n')
for r in rows:print(r['source'],r['exit_code'],r['elapsed_seconds'],r['stdout_matches_original_out'])
