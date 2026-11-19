from pathlib import Path
import shutil,re,json,hashlib,subprocess,concurrent.futures,sys
root=Path(__file__).resolve().parents[4]
src=root/'sources/newer_night/checkpoint25'
dst=Path(__file__).parent/'replay_cp25'
files=['code/part3/e6_unselected_iii.py','code/part3/e6_unselected_iii_extension.py','code/part3/e6_d_zero_disc.py','code/part3_fourfold/e6_selected_cusp.py','code/part3_fourfold/e6_selected_cusp_all_caps.py','code/part3_fourfold/source_infinity_closed_formula.py','code/part3_root/source_zero_all_fans.py','code/part3_root/source_all_fans.py']
notes=list((src/'notes').glob('part3_e6*working.md'))+list((src/'notes').glob('part3_source_infinity*working.md'))
files+= [str(p.relative_to(src)) for p in notes]
manifest=[]
for rel in files:
 p=src/rel;q=dst/rel;q.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,q)
 manifest.append({'path':rel,'source':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
(dst/'source_manifest.json').write_text(json.dumps(manifest,indent=2))
programs=files[:6]
def run(rel):
 p=dst/rel;r=subprocess.run([sys.executable,str(p)],cwd=dst,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
 p.with_suffix('.current.stdout.txt').write_text(r.stdout)
 info={'program':rel,'exit_code':r.returncode}
 if r.returncode==0:
  data=json.loads(p.with_suffix('.json').read_text());info.update({k:data[k] for k in ['status','checks','check_count','full_algorithm_replays'] if k in data and not isinstance(data[k],list)})
 else: info['tail']=r.stdout[-3000:]
 print(json.dumps(info),flush=True);return info
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:results=list(ex.map(run,programs))
(dst/'current_results.json').write_text(json.dumps(results,indent=2))
assert all(r['exit_code']==0 for r in results)
