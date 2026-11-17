"""Rerun the exact programs referenced by the remaining F proof blocks.

Runs are sequential because some programs write inputs for later ones.
Every result, timeout and failure is retained; none is converted to a pass.
"""
from pathlib import Path
import ast,hashlib,json,os,shutil,subprocess,time
D=Path(__file__).resolve().parents[2];R=D.parent
SRC=R/'sources/returns/S6_04_MAPS_MANIFOLDS/code'
dest=D/'code/root_maps_F';dest.mkdir(exist_ok=True)
rows=json.loads((D/'work/root/F_referenced_programs.json').read_text())
names={n for x in rows for n in x['programs']}|{'fourfolds_finite_types.py'}
queue=list(names);copied={}
while queue:
 name=queue.pop()
 if name in copied:continue
 p=SRC/name
 assert p.exists(),p
 shutil.copy2(p,dest/name)
 copied[name]=hashlib.sha256(p.read_bytes()).hexdigest()
 if p.suffix!='.py':continue
 tree=ast.parse(p.read_text())
 for n in ast.walk(tree):
  modules=[x.name for x in n.names] if isinstance(n,ast.Import) else [n.module] if isinstance(n,ast.ImportFrom) and n.module else []
  for module in modules:
   candidate=module.split('.')[0]+'.py'
   if (SRC/candidate).exists():queue.append(candidate)
(dest/'copied_programs.json').write_text(json.dumps(copied,indent=2)+'\n')
jobs=['fourfolds_finite_types.py']+sorted(n for n in names if n.endswith('.py') and n!='fourfolds_finite_types.py')
records=[]
manifest=dest/'execution_manifest.json'
for name in jobs:
 start=time.time();out=dest/(name+'.rerun.txt')
 cmd=[os.environ.get('CODEX_PRIMARY_RUNTIME_PYTHON','python3'),name]
 try:
  with out.open('w') as f:
   p=subprocess.run(cmd,cwd=dest,stdout=f,stderr=subprocess.STDOUT,timeout=300)
  code=p.returncode;status='completed'
 except subprocess.TimeoutExpired:
  code=None;status='timed out after 300 seconds; retained partial output'
 rec={'program':'code/root_maps_F/'+name,'command':['python3',name],'working_directory':'code/root_maps_F',
      'sha256':copied[name],'exit_code':code,'status':status,'seconds':round(time.time()-start,3),
      'output':str(out.relative_to(D)),'output_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),
      'reader':'GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 17 November 2026',
      'scope':'Exact finite/programmatic claims at the explicitly cited F proof loci; no automatic analytic or topological conclusion.'}
 records.append(rec);manifest.write_text(json.dumps(records,indent=2)+'\n')
 print(json.dumps({k:rec[k] for k in ['program','exit_code','status','seconds']}),flush=True)
print('Finished',len(records),'runs;',sum(r['exit_code']==0 for r in records),'exit zero.',flush=True)
