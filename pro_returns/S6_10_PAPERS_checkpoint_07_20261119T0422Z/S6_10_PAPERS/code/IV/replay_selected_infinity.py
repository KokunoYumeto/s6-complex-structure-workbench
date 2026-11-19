"""Current, isolated execution of the received K101 certificates.

Received program bytes and their embedded historical attribution are unchanged.
Only this wrapper supplies the current execution record.
"""
from pathlib import Path
import datetime,hashlib,json,shutil,subprocess,sys,time
W=Path(__file__).resolve().parents[2]
source=W.parents[1]/'sources/newer_night/checkpoint27'
dest=W/'code/IV/replay_selected_infinity'
dest.mkdir(parents=True,exist_ok=True)
inputs=list(source.glob('code/**/e6_selected_infinity*'))
inputs+=list(source.glob('notes/part3_e6_selected_infinity*'))
inputs+=[source/x for x in [
 'code/part3_fourfold/e6_fixed_face_orbits.py',
 'code/part3_fourfold/e6_fixed_face_orbits.json',
 'code/part3_root/e6_common_period_fan.json',
 'code/part3/e6_common_corner_lift.json',
 'code/part3_fourfold/e6_p_one_common_cayley.json']]
manifest=[]
for p in sorted(set(inputs)):
 if not p.is_file():continue
 q=dest/p.relative_to(source);q.parent.mkdir(parents=True,exist_ok=True)
 if q.exists():raise RuntimeError('Existing replay file: '+str(q))
 shutil.copyfile(p,q)
 a=hashlib.sha256(p.read_bytes()).hexdigest();b=hashlib.sha256(q.read_bytes()).hexdigest()
 assert a==b
 manifest.append({'path':str(p.relative_to(source)),'source_sha256':a,'copied_sha256':b,'bytes':p.stat().st_size})
(dest/'records').mkdir(exist_ok=True)
(dest/'input_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
scripts=[
 'code/part3_fourfold/e6_selected_infinity_source.py',
 'code/part3/e6_selected_infinity_root.py',
 'code/part3_fourfold/e6_selected_infinity_joint_line.py',
 'code/part3_fourfold/e6_selected_infinity_graphs.py',
 'code/part3_fourfold/e6_selected_infinity_native_graph.py',
 'code/part3/e6_selected_infinity_toric_audit.py',
 'code/part3/e6_selected_infinity_factor_overlay.py',
 'code/part3_root/e6_selected_infinity_mu4_fan.py',
 'code/part3_root/e6_selected_infinity_mu2_pair.py',
 'code/part3_root/e6_selected_infinity_mu2_fixed.py',
 'code/part3_root/e6_selected_infinity_mu2_residue_comparison.py',
 'code/part3_root/e6_selected_infinity_a3_source.py',
 'code/part3_fourfold/e6_fixed_face_orbits.py',
 'code/part3_fourfold/e6_selected_infinity_surface_refinement.py',
 'code/part3_fourfold/e6_selected_infinity_strict_surfaces.py',
 'code/part3_fourfold/e6_selected_infinity_curve_clutch.py',
 'code/part3_fourfold/e6_selected_infinity_compact_surface_stars.py',
 'code/part3_root/e6_selected_infinity_moving_cap.py',
 'code/part3/e6_selected_infinity_moving_c2.py',
 'code/part3_root/e6_selected_infinity_full_pair_ledger.py',
 'code/part3_fourfold/e6_selected_infinity_outer_transfer.py']
events=[]
for rel in scripts:
 p=dest/rel
 started=datetime.datetime.now(datetime.timezone.utc).isoformat();tick=time.monotonic()
 r=subprocess.run([sys.executable,str(p)],cwd=dest,capture_output=True,text=True,timeout=240)
 p.with_suffix('.current.stdout').write_text(r.stdout)
 p.with_suffix('.current.stderr').write_text(r.stderr)
 result=p.with_suffix('.json');status=count=None
 if result.is_file():
  j=json.loads(result.read_text());status=j.get('status')
  for key in ('checks','check_count','cases'):
   v=j.get(key)
   if v is not None:count=len(v) if isinstance(v,list) else v;break
 rec=dict(script=rel,source_sha256=hashlib.sha256((source/rel).read_bytes()).hexdigest(),
          copied_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),
          started_at=started,finished_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),
          seconds=round(time.monotonic()-tick,3),exit_code=r.returncode,
          output_status=status,output_count=count)
 events.append(rec)
 (dest/'current_execution.json').write_text(json.dumps(events,indent=2)+'\n')
 print(json.dumps(rec),flush=True)
 if r.returncode:print(r.stderr,flush=True);break
