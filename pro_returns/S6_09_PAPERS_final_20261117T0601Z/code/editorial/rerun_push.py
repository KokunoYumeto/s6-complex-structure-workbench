"""Re-run the mathematical PUSH checks in isolated copied paths.

Editorial, fetching, checkpoint and status-changing scripts are excluded.
The computational certificate chain is sequential; independent exact checks
run concurrently. Every return code and output is preserved.
"""
from pathlib import Path
import concurrent.futures as cf
import subprocess, shutil, sys, os, json, hashlib, time

WORK = Path(__file__).resolve().parents[3]
DEL = WORK/'deliverables'
SRC = WORK/'sources/returns/S6_02_PUSH/code'
DST = DEL/'code/push/code'
DST.mkdir(parents=True,exist_ok=True)
skip = ('sources','source_audit','registry','catalogue','close_A_scope','order_sections',
        'final_status','update_homology','C_ocr','C_wall_ocr','C_cap','C_index','C_sources')
names=[]
for p in SRC.glob('*.py'):
    if not p.name.startswith(('ab_push_','d_push_','e_push_','b_hodge_','b_nc_','root_quadric_','d_root_','e4_')):continue
    if any(k in p.name for k in skip):continue
    if p.name.startswith('e_push_C_'):continue
    shutil.copy2(p,DST/p.name)
    names.append(p.name)
inp=DEL/'code/background/s6_02_return/code'
inp.mkdir(parents=True,exist_ok=True)
shutil.copy2(WORK/'sources/returns/S6_02_FAMILY/code/f_interval_parallel_certificate.json',inp/'f_interval_parallel_certificate.json')
env=os.environ.copy();env['PYTHONPATH']=str(WORK/'deps/python')+os.pathsep+env.get('PYTHONPATH','')
logdir=DEL/'code/push/logs';logdir.mkdir(exist_ok=True)
heavy=['e4_arb_certificate.py','e4_cover_and_local.py','d_root_gradient_certificate.py',
       'd_push_rho_containment.py','d_push_rho_branch_audit.py',
       'd_push_global_arb.py','d_push_global_refine.py','d_push_global_cover_audit.py']
manifest=[]
def run(name):
    cmd=[sys.executable,str(DST/name)]
    if name in ['e4_arb_certificate.py','d_push_global_arb.py']:cmd+=['--workers','4']
    start=time.time()
    with (logdir/(name+'.txt')).open('w') as f:
        try:
            proc=subprocess.run(cmd,cwd=DST.parent,env=env,stdout=f,stderr=subprocess.STDOUT,timeout=1200)
            rc=proc.returncode
        except subprocess.TimeoutExpired:rc=124
    row={'program':name,'command':cmd,'returncode':rc,'seconds':round(time.time()-start,3),
         'sha256':hashlib.sha256((DST/name).read_bytes()).hexdigest(),
         'log':str((logdir/(name+'.txt')).relative_to(DEL))}
    print(name,rc,row['seconds'],flush=True)
    return row
with cf.ThreadPoolExecutor(max_workers=4) as pool:
    for row in pool.map(run,sorted(set(names)-set(heavy))):
        manifest.append(row)
        (DEL/'code/push/rerun_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
for name in heavy:
    row=run(name);manifest.append(row)
    (DEL/'code/push/rerun_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    if row['returncode'] and name in ['e4_arb_certificate.py','d_push_global_arb.py','d_push_global_refine.py']:
        print('Dependent chain paused after failure:',name,flush=True);break
