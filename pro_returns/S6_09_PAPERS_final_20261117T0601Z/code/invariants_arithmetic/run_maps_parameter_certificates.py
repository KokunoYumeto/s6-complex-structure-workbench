"""Execute one fully inspected original program with explicit parameters."""
from pathlib import Path
import json,sys,subprocess,hashlib,shutil,time
ROOT=Path(__file__).resolve().parents[3]
SRC=ROOT/'sources/returns/S6_04_MAPS_MANIFOLDS'
PROJ=ROOT/'deliverables/code/invariants_arithmetic/maps_D_project'
LEDGER=ROOT/'deliverables/work/invariants_arithmetic/maps_D_program_runs.json'
name=sys.argv[1];args=sys.argv[2:];p=PROJ/'code'/(name+'.py')
shutil.copy2(SRC/'code'/p.name,p)
token=hashlib.sha256(json.dumps(args).encode()).hexdigest()[:10]
out=p.with_suffix('.'+token+'.writing.out');start=time.time()
try:
 r=subprocess.run([sys.executable,p.name]+args,cwd=p.parent,text=True,capture_output=True,timeout=900)
 code=r.returncode;output=r.stdout+r.stderr
except subprocess.TimeoutExpired as e:
 code='timeout900';output=str(e.stdout or '')+'\n'+str(e.stderr or '')
out.write_text(output)
record={'program':str(p.relative_to(ROOT)),'original_program':str((SRC/'code'/p.name).relative_to(ROOT)),
 'program_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'arguments':args,
 'command':'python '+str(p.relative_to(ROOT))+' '+' '.join(args),'exit_code':code,
 'elapsed_seconds':round(time.time()-start,3),'output':str(out.relative_to(ROOT)),
 'output_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),
 'run_date':'2026-11-17 UTC','read_scope':'Whole original program read independently before running; exact argument scope stated.'}
if name=='manifolds_tate_markings':
 record['generated_json_comparisons']=[]
 for c in args[1:]:
  f=PROJ/'records'/('manifolds_c'+c+'_tate_markings.json');old=SRC/'records'/f.name
  if f.exists():record['generated_json_comparisons'].append({'path':str(f.relative_to(ROOT)),'sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'byte_identical_retained':old.exists() and f.read_bytes()==old.read_bytes()})
j=json.loads(LEDGER.read_text());j.append(record);LEDGER.write_text(json.dumps(j,indent=2)+'\n')
print(json.dumps(record,indent=2))
