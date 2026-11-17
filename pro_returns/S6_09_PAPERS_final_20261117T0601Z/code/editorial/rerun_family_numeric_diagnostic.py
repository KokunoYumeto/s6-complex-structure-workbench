"""Retain and rerun the cited non-rigorous FAMILY grid diagnostic."""
from pathlib import Path
import shutil,subprocess,sys,time,json,hashlib
ROOT=Path(__file__).resolve().parents[3]
src=ROOT/'sources/returns/S6_02_FAMILY/code/cd_numerics.py'
out=ROOT/'deliverables/code/family';dst=out/src.name
shutil.copy2(src,dst);start=time.time()
p=subprocess.run([sys.executable,str(dst)],cwd=out,capture_output=True,text=True)
(out/'cd_numerics.rerun.stdout.txt').write_text(p.stdout)
(out/'cd_numerics.rerun.stderr.txt').write_text(p.stderr)
r={'program':str(dst.relative_to(ROOT/'deliverables')),'command':['python','cd_numerics.py'],
 'cwd':'code/family','returncode':p.returncode,'seconds':time.time()-start,
 'program_sha256':hashlib.sha256(dst.read_bytes()).hexdigest(),
 'role':'Numerical grid diagnostic only; no rigorous inequality rests on this computation.'}
(out/'numeric_diagnostic_rerun.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps(r,indent=2))
