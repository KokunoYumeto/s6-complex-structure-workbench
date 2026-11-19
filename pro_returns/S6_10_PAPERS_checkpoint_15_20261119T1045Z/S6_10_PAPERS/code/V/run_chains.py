from pathlib import Path
import subprocess,sys,json,datetime,concurrent.futures
W=Path(__file__).resolve().parents[2]
dest=W/'code/V/replay_chains/code'
names=['fourfolds_vankampen.py','fourfolds_three_point_family.py','fourfolds_involution_classes.py','fourfolds_bar_koszul.py','fourfolds_affine_cap_chains.py','fourfolds_kuhn_cap_chains.py','fourfolds_global_chains.py','fourfolds_peripheral_signs.py']
def run(name):
 start=datetime.datetime.now(datetime.timezone.utc).isoformat()
 with (dest/(name+'.current.stdout.txt')).open('w') as f:p=subprocess.run([sys.executable,name],cwd=dest,stdout=f,stderr=subprocess.STDOUT)
 r={'program':name,'exit_code':p.returncode,'started_at':start,'ended_at':datetime.datetime.now(datetime.timezone.utc).isoformat()};print(r,flush=True);return r
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:results=list(ex.map(run,names))
(dest/'current_results.json').write_text(json.dumps(results,indent=2))
