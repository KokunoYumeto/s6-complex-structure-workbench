#!/usr/bin/env python3
from pathlib import Path
import ast,hashlib,json,datetime,subprocess
D=Path(__file__).resolve().parent
fresh=D/'S6_SERIES_PUBLISH_II_G3_G4_fresh_exact.py'
assert hashlib.sha256(fresh.read_bytes()).hexdigest()=='836a1e0b329113a2f155d076f2ad3caa6672e375ba0f06e139bc44090b8f3487'
t=ast.parse(fresh.read_text());safe=[n for n in t.body if isinstance(n,(ast.Import,ast.ImportFrom,ast.FunctionDef))]
ns={};exec(compile(ast.Module(body=safe,type_ignores=[]),str(fresh),'exec'),ns)
b=[[1,0,-6,-2],[0,-1,-1,1],[0,1,0,-1],[0,0,0,1]];cube=ns['mul'](ns['mul'](b,b),b);assert cube==ns['eye'](4)
old=D/'S6_SERIES_PUBLISH_II_G4_prior_program_slice.py';r=subprocess.run(['python',str(old)],capture_output=True,text=True);assert r.returncode==0
f=D/'S6_SERIES_PUBLISH_II_G4_prior_program_reexecution.txt';f.write_text(r.stdout)
o={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'after new G3/G4 freezes and target release','fresh_prerelease_program_sha256':hashlib.sha256(fresh.read_bytes()).hexdigest(),'new_step':'The old routine also checks B_star^3=I; this exact supplementary calculation uses the fresh standard-library multiplication and preserves the prerelease program/output unchanged.','B_star_cube':cube,'prior_slice_sha256':hashlib.sha256(old.read_bytes()).hexdigest(),'prior_output_path':str(f),'prior_output_sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'prior_returncode':r.returncode,'events_added':0}
f=D/'S6_SERIES_PUBLISH_II_G4_postrelease_exact_output.json';f.write_text(json.dumps(o,indent=2)+'\n');print(json.dumps(o,indent=2))
