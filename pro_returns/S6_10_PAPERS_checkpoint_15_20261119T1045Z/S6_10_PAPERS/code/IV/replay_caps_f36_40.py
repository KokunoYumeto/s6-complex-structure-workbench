"""Replay the seven fully read exact certificates in isolated unchanged copies."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import hashlib,json,shutil,subprocess,time
P=Path(__file__).resolve().parents[2];R=P.parents[1];S=R/'sources/newer_night/checkpoint29';D=P/'code/IV/replay_caps_f36_40'
files=['code/part3/i1star_boundary.py','code/part3/i1star_iv_boundary.py','code/part3/i1star_iv_reduced_boundary.py','code/part3_root/reduced_iii_audit.py','code/part3/reduced_iii_cap_maps.py','code/part3_root/multiplicative_cap_boundary.py','code/part3/i1star_smooth_caps.py']
manifest=[]
for f in files:
 s=S/f;d=D/f;d.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(s,d)
 manifest.append({'source':str(s.relative_to(R)),'copy':str(d.relative_to(P)),'sha256':hashlib.sha256(s.read_bytes()).hexdigest(),'identical':s.read_bytes()==d.read_bytes()})
def run(f):
 p=D/f;start=time.monotonic();r=subprocess.run(['python',str(p)],cwd=D,capture_output=True,text=True)
 p.with_suffix('.current.stdout').write_text(r.stdout);p.with_suffix('.current.stderr').write_text(r.stderr)
 j=p.with_suffix('.json');o=json.loads(j.read_text()) if r.returncode==0 and j.exists() else {}
 return {'program':f,'returncode':r.returncode,'seconds':time.monotonic()-start,'output':str(j.relative_to(P)),'output_sha256':hashlib.sha256(j.read_bytes()).hexdigest() if j.exists() else None,'status':o.get('status',o.get('all_pass')),'stdout_tail':r.stdout[-1000:],'stderr':r.stderr}
with ThreadPoolExecutor(max_workers=3) as pool:results=list(pool.map(run,files[:-1]))
if all(r['returncode']==0 for r in results):results.append(run(files[-1]))
record={'source_files':manifest,'runs':results,'all_completed_successfully':len(results)==7 and all(r['returncode']==0 for r in results),'scope':'Exact execution checks only. Seven complete source programs were read, and full F36–40 geometric proofs were separately read/rederived. Inherited output statements about prior independent audits grant no new current credit.','source_comment_correction':'The reduced-IV boundary program comment says -6G; the exact executable matrix is the inverse of the +2G matrix and its result keys correctly say -2G. The copied program is unchanged.'}
(P/'analysis/IV/root_F36_40_certificate_replays.json').write_text(json.dumps(record,indent=2))
print(json.dumps(record,indent=2));raise SystemExit(0 if record['all_completed_successfully'] else 1)
