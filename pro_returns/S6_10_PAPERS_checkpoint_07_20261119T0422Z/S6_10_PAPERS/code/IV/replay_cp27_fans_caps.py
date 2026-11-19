"""Current isolated execution of the two new cp27 algebra certificates.

Original program bytes and their historical attribution are preserved.
This wrapper records only the actual current execution.
"""
from pathlib import Path
import datetime, hashlib, json, shutil, subprocess, sys, time
W=Path(__file__).resolve().parents[2]
source=W.parents[1]/'sources/newer_night/checkpoint27'
dest=W/'code/IV/replay_cp27_fans_caps'
dest.mkdir(parents=True,exist_ok=True)
paths=[
 'code/part3_fourfold/e6_selected_infinity_all_fans.py',
 'code/part3_root/source_all_fans.py',
 'code/part3_root/e6_order_three_all_caps.py',
 'notes/part3_e6_selected_infinity_all_fans_working.md',
 'notes/part3_e6_order_three_all_caps_working.md']
manifest=[]
for rel in paths:
 p=source/rel;q=dest/rel;q.parent.mkdir(parents=True,exist_ok=True)
 if q.exists():raise RuntimeError('Existing replay input '+str(q))
 shutil.copyfile(p,q)
 a=hashlib.sha256(p.read_bytes()).hexdigest();b=hashlib.sha256(q.read_bytes()).hexdigest()
 assert a==b
 manifest.append(dict(path=rel,source_sha256=a,copied_sha256=b,bytes=p.stat().st_size))
(dest/'input_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
events=[]
for rel in [paths[0],paths[2]]:
 p=dest/rel;start=datetime.datetime.now(datetime.timezone.utc).isoformat();tick=time.monotonic()
 r=subprocess.run([sys.executable,str(p)],cwd=dest,capture_output=True,text=True,timeout=240)
 p.with_suffix('.current.stdout').write_text(r.stdout);p.with_suffix('.current.stderr').write_text(r.stderr)
 j=json.loads(p.with_suffix('.json').read_text()) if p.with_suffix('.json').exists() else {}
 record=dict(script=rel,source_sha256=hashlib.sha256((source/rel).read_bytes()).hexdigest(),copied_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),started_at=start,finished_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),seconds=round(time.monotonic()-tick,3),exit_code=r.returncode,output_status=j.get('status'),output_count=j.get('checks'))
 events.append(record);(dest/'current_execution.json').write_text(json.dumps(events,indent=2)+'\n');print(json.dumps(record),flush=True)
 if r.returncode:raise RuntimeError(r.stderr)
