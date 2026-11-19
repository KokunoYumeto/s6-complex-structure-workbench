"""Unchanged-byte execution of the local trace and higher-period certificates."""
from pathlib import Path
import datetime,hashlib,json,shutil,subprocess,sys,time
W=Path(__file__).resolve().parents[2];source=W.parents[1]/'sources/newer_night/checkpoint27'
dest=W/'code/IV/replay_trace_batch';dest.mkdir(parents=True,exist_ok=True)
scripts=['code/part3_fourfold/outer_descent.py','code/part3/compact_torsor.py','code/part3_fourfold/direct_section.py','code/part3_fourfold/normal_clutch.py','code/part3_fourfold/higher_parameter.py']
events=[]
for rel in scripts:
 p=source/rel;q=dest/rel;q.parent.mkdir(parents=True,exist_ok=True)
 if q.exists():raise RuntimeError('Existing replay '+str(q))
 shutil.copyfile(p,q);sha=hashlib.sha256(p.read_bytes()).hexdigest();assert sha==hashlib.sha256(q.read_bytes()).hexdigest()
 start=datetime.datetime.now(datetime.timezone.utc).isoformat();tick=time.monotonic()
 r=subprocess.run([sys.executable,str(q)],cwd=dest,capture_output=True,text=True,timeout=240)
 q.with_suffix('.current.stdout').write_text(r.stdout);q.with_suffix('.current.stderr').write_text(r.stderr)
 e=dict(script=rel,source_sha256=sha,copied_sha256=hashlib.sha256(q.read_bytes()).hexdigest(),started_at=start,finished_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),seconds=round(time.monotonic()-tick,3),exit_code=r.returncode)
 if 'normal_clutch' in rel or 'higher_parameter' in rel:e['convention_note']='Received negative characteristic pairs are the U=M^-1 values. Current physical M values are their negatives, through the separately proved extending line duality. Received output bytes are preserved.'
 events.append(e);(dest/'current_execution.json').write_text(json.dumps(events,indent=2)+'\n');print(json.dumps(e),flush=True)
 if r.returncode:raise RuntimeError(r.stderr)
