from pathlib import Path
import hashlib,json,shutil,datetime,subprocess,time
W=Path(__file__).resolve().parents[2];SRC=W.parents[1]/'sources/newer_night/checkpoint29';OUT=W/'code/IV/replay_cp29_retained_batch'
programs=['canonical_scalar_catalogue','fixed_source_cap_loops','moving_order_one_sites','os49_cap_loops','source_cusp_fixed_edge','source_cusp_reflection','source_cusp_reflected_pair']
files=[f'code/part3/{n}.py' for n in programs]+['code/part3/scalar_dependency_scope.py','code/part3_fourfold/source_reduction.json','code/part3/additive_returns.json','code/part3/joint_additive_returns.json','records/scalar_fan_correction_scope.json']
manifest=[]
for rel in files:
 src=SRC/rel;dest=OUT/rel;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(src,dest);raw=src.read_bytes();assert raw==dest.read_bytes();manifest.append({'path':rel,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()})
(OUT/'source_manifest.json').write_text(json.dumps({'source_checkpoint':29,'copied':manifest,'scope':'Unchanged program replay. Literal prior audit declarations in program output are historical strings and receive no current proof credit. Withdrawn all-fan polynomials and old positive physical source indices retain only their explicitly identified algebraic scope.'},indent=2))
logs=OUT/'execution_logs';logs.mkdir(exist_ok=True);results=[]
for name in programs:
 start=datetime.datetime.now(datetime.timezone.utc).isoformat();t=time.monotonic();r=subprocess.run(['python',str(OUT/f'code/part3/{name}.py')],cwd=OUT,capture_output=True,text=True);(logs/(name+'.stdout')).write_text(r.stdout);(logs/(name+'.stderr')).write_text(r.stderr)
 output=OUT/f'code/part3/{name}.json';obj=json.loads(output.read_text()) if output.exists() else {};checks=obj.get('checks_count',obj.get('exact_checks',obj.get('checks')));checks=len(checks) if isinstance(checks,list) else checks
 results.append({'program':f'code/part3/{name}.py','started_at':start,'seconds':time.monotonic()-t,'exit_code':r.returncode,'checks':checks,'output_sha256':hashlib.sha256(output.read_bytes()).hexdigest() if output.exists() else None,'stdout':str((logs/(name+'.stdout')).relative_to(OUT)),'stderr':str((logs/(name+'.stderr')).relative_to(OUT))})
 (OUT/'current_results.json').write_text(json.dumps(results,indent=2));print(name,r.returncode,checks,flush=True)
 if r.returncode:print(r.stderr[-3000:]);break
