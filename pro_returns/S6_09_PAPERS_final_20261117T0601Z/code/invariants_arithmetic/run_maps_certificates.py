"""Rerun previously inspected original MAPS certificates in an isolated copy."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import sys,json,hashlib,subprocess,shutil,time
ROOT=Path(__file__).resolve().parents[3]
SRC=ROOT/'sources/returns/S6_04_MAPS_MANIFOLDS'
PROJ=ROOT/'deliverables/code/invariants_arithmetic/maps_D_project'
OUT=ROOT/'deliverables/work/invariants_arithmetic/maps_D_program_runs.json'
(PROJ/'code').mkdir(parents=True,exist_ok=True)
(PROJ/'records').mkdir(exist_ok=True)

def run(name):
    a=SRC/'code'/(name+'.py');b=PROJ/'code'/a.name
    shutil.copy2(a,b)
    start=time.time()
    try:
        p=subprocess.run([sys.executable,b.name],cwd=PROJ/'code',text=True,capture_output=True,timeout=900)
        code=p.returncode; output=p.stdout+p.stderr
    except subprocess.TimeoutExpired as ex:
        code='timeout900'; output=str(ex.stdout or '')+'\n'+str(ex.stderr or '')
    op=b.with_suffix('.writing.out');op.write_text(output)
    orig=SRC/'code'/(name+'.out');extra=PROJ/'records'/(name+'.json')
    return {'program':str(b.relative_to(ROOT)),'original_program':str(a.relative_to(ROOT)),
      'program_sha256':hashlib.sha256(b.read_bytes()).hexdigest(),'command':'python '+str(b.relative_to(ROOT)),
      'exit_code':code,'elapsed_seconds':round(time.time()-start,3),
      'output':str(op.relative_to(ROOT)),'output_sha256':hashlib.sha256(op.read_bytes()).hexdigest(),
      'matches_retained_output':orig.exists() and orig.read_bytes()==op.read_bytes(),
      'json_output':str(extra.relative_to(ROOT)) if extra.exists() else None,'run_date':'2026-11-17 UTC',
      'read_scope':'Complete certificate program inspected before invoking this runner; full geometric proof read separately.'}

names=sys.argv[1:]
old=json.loads(OUT.read_text()) if OUT.exists() else []
names=[n for n in names if not any(Path(r['program']).stem==n and r['exit_code']==0 for r in old)]
for name in names:
    shutil.copy2(SRC/'code'/(name+'.py'),PROJ/'code'/(name+'.py'))
new=list(ThreadPoolExecutor(4).map(run,names))
OUT.write_text(json.dumps(old+new,indent=2)+'\n')
print(json.dumps(new,indent=2))
