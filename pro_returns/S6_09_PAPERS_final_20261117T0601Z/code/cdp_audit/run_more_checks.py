"""Copy and rerun source certificates without changing original sources."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import hashlib,json,subprocess,sys,time
ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/'deliverables/code/cdp_audit'; WORK=ROOT/'deliverables/work/cdp_audit'
files=[ROOT/'sources/returns/S6_03_CDP/code'/name for name in ['A_return_germs.py','D_monodromy_signatures.py','E_comb_checks.py','E_singular_curve.py','B_examples.py']]
files += [ROOT/'sources/overleaf_working_edition/supporting_materials/reproducibility/verify_analytic_picard_completion.py']
(OUT/'records').mkdir(exist_ok=True)
def run(src):
 data=src.read_bytes(); dst=OUT/src.name; edited=data
 if src.name=='D_monodromy_signatures.py':
  edited=data.replace(b'ROOT = Path(__file__).resolve().parents[1]',b'ROOT = Path(__file__).resolve().parent')
 dst.write_bytes(edited);start=time.time()
 args=[sys.executable,str(dst)]
 if src.name=='verify_analytic_picard_completion.py': args += ['--json-output',str(WORK/'analytic_picard_completion_results.json')]
 p=subprocess.run(args,cwd=OUT,capture_output=True,text=True,timeout=90)
 log=OUT/(src.name+'.output.txt');log.write_text(p.stdout+'\nSTDERR\n'+p.stderr)
 return {'source':str(src.relative_to(ROOT)),'source_sha256':hashlib.sha256(data).hexdigest(),'executed':str(dst.relative_to(ROOT)),'executed_sha256':hashlib.sha256(edited).hexdigest(),'modifications':'output root changed to audit directory' if edited!=data else 'none','exit_code':p.returncode,'elapsed_seconds':round(time.time()-start,3),'output':str(log.relative_to(ROOT)),'scope':'exact algebra only; no geometric proof certified by program','checker':'GPT-6 Astra (OpenAI, ChatGPT Pro mode), 17 November 2026 UTC'}
with ThreadPoolExecutor(max_workers=3) as pool: rows=list(pool.map(run,files))
p=OUT/'execution_manifest_more.json';p.write_text(json.dumps(rows,indent=2)+'\n')
for r in rows: print(r['executed'],r['exit_code'],r['elapsed_seconds'])
