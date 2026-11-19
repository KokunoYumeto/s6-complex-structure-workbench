from pathlib import Path
import shutil,subprocess,sys,json,hashlib,datetime,concurrent.futures
R=Path(__file__).resolve().parents[4];W=R/'work/S6_10_PAPERS';dest=W/'code/V/replay_universal_survivor';dest.mkdir(exist_ok=True)
names=['fourfolds_relative_six_probe.py','fourfolds_universal_56_obstruction.py','fourfolds_local_caps.py','fourfolds_cusp_boundary.py','fourfolds_survivor_test.py'];dependencies=['fourfolds_family_survivors.py','fourfolds_relative_normalform.py'];manifest=[]
for name in names+dependencies:
 src=R/'sources/returns/S6_04_MAPS_MANIFOLDS/code'/name;target=dest/name;shutil.copy2(src,target)
 manifest.append({'source':str(src.relative_to(R)),'target':str(target.relative_to(W)),'sha256':hashlib.sha256(src.read_bytes()).hexdigest()})
(dest/'source_manifest.json').write_text(json.dumps(manifest,indent=2))
def run(name):
 start=datetime.datetime.now(datetime.timezone.utc).isoformat()
 with (dest/(name+'.current.stdout.txt')).open('w') as f:p=subprocess.run([sys.executable,name],cwd=dest,stdout=f,stderr=subprocess.STDOUT)
 r={'program':name,'exit_code':p.returncode,'started_at':start,'ended_at':datetime.datetime.now(datetime.timezone.utc).isoformat()};print(r,flush=True);return r
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:results=list(ex.map(run,names))
(dest/'current_results.json').write_text(json.dumps(results,indent=2))
