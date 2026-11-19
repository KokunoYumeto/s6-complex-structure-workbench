"""Replay the five new exact cap certificates in byte-verified isolated copies."""
from pathlib import Path
import ast, datetime, hashlib, json, shutil, subprocess, sys

W=Path(__file__).resolve().parents[2]
S=W.parents[1]/'sources/newer_night/checkpoint28'
D=W/'code/IV/replay_cp28_caps'
D.mkdir(exist_ok=True)
programs=[
 'code/part3_fourfold/e6_selected_infinity_negative_norm.py',
 'code/part3_fourfold/e6_selected_infinity_reduced_caps.py',
 'code/part3_fourfold/e6_selected_infinity_m2_branch.py',
 'code/part3_fourfold/e6_selected_infinity_m2_odd_ideal.py',
 'code/part3_fourfold/e6_selected_infinity_good_caps.py',
]
inputs=set(programs)
for p in programs:
 for node in ast.walk(ast.parse((S/p).read_text())):
  if isinstance(node,ast.Constant) and isinstance(node.value,str):
   v=node.value
   if v.startswith(('code/','notes/','records/')) and (S/v).is_file():inputs.add(v)
ledger=[]
for p in sorted(inputs):
 src=S/p;dest=D/p;dest.parent.mkdir(parents=True,exist_ok=True)
 shutil.copyfile(src,dest)
 a=hashlib.sha256(src.read_bytes()).hexdigest();b=hashlib.sha256(dest.read_bytes()).hexdigest()
 assert a==b
 ledger.append(dict(path=p,source_sha256=a,copied_sha256=b,bytes=src.stat().st_size))
(D/'input_manifest.json').write_text(json.dumps(dict(source_checkpoint=28,files=ledger),indent=2)+'\n')
events=[]
for p in programs:
 started=datetime.datetime.now(datetime.timezone.utc).isoformat()
 proc=subprocess.run([sys.executable,str(D/p)],cwd=D,text=True,capture_output=True)
 ended=datetime.datetime.now(datetime.timezone.utc).isoformat()
 out=D/(Path(p).stem+'.stdout.txt');err=D/(Path(p).stem+'.stderr.txt')
 out.write_text(proc.stdout);err.write_text(proc.stderr)
 payload={}
 result=(D/p).with_suffix('.json')
 if result.is_file():payload=json.loads(result.read_text())
 e=dict(program=p,started_at=started,ended_at=ended,exit_code=proc.returncode,
        program_sha256=hashlib.sha256((D/p).read_bytes()).hexdigest(),
        stdout=str(out.relative_to(W)),stderr=str(err.relative_to(W)),
        result_status=payload.get('status'),checks=payload.get('checks'),
        result_sha256=hashlib.sha256(result.read_bytes()).hexdigest() if result.is_file() else None)
 events.append(e)
 (D/'current_execution.json').write_text(json.dumps(dict(source_checkpoint=28,
  scope='Current executions of unchanged received algebra programs; analytic product, compactness and orientation arguments were separately read and rederived.',events=events),indent=2)+'\n')
 print(json.dumps(e),flush=True)
 if proc.returncode:raise SystemExit(proc.returncode)
