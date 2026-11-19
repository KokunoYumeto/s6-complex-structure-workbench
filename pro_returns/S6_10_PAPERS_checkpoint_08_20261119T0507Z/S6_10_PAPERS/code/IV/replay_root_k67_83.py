"""Five unchanged exact certificate runs, separate from the full receiving proofs."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import datetime,hashlib,json,shutil,subprocess,time
P=Path(__file__).resolve().parents[2];R=P.parents[1]
S=R/'sources/newer_night/checkpoint29';D=P/'code/IV/replay_root_k67_83'
files=['code/part3/shorter_scalar_vertical_fans.py','code/part3/scalar_nonvertical.py',
       'code/part3/os49_order_two_cap.py','code/part3_root/source_zero_vertical_fans.py',
       'code/part3/source_zero_good_cut.py']
manifest=[]
for name in files+['notes/part3_source_zero_good_cut_working.md']:
 source,target=S/name,D/name;target.parent.mkdir(parents=True,exist_ok=True)
 shutil.copy2(source,target);assert source.read_bytes()==target.read_bytes()
 manifest.append({'source':str(source.relative_to(R)),'copy':str(target.relative_to(P)),
                  'sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'unchanged':True,
                  'read_scope':'Complete program read' if name.endswith('.py') else 'Exact metadata hash input only; the complete exported K83 TeX proof was read separately.'})
def run(name):
 p=D/name;start=datetime.datetime.now(datetime.timezone.utc).isoformat();tick=time.monotonic()
 result=subprocess.run(['python',str(p)],cwd=D,capture_output=True,text=True)
 p.with_suffix('.current.stdout').write_text(result.stdout);p.with_suffix('.current.stderr').write_text(result.stderr)
 out=p.with_suffix('.json');data=json.loads(out.read_text()) if result.returncode==0 and out.exists() else {}
 return {'program':name,'started_utc':start,'seconds':time.monotonic()-tick,
         'returncode':result.returncode,'status':data.get('status'),
         'output':str(out.relative_to(P)),'sha256':hashlib.sha256(out.read_bytes()).hexdigest() if out.exists() else None,
         'stdout_tail':result.stdout[-1200:],'stderr':result.stderr}
with ThreadPoolExecutor(max_workers=3) as pool:runs=list(pool.map(run,files))
record={'source_checkpoint':29,'inputs':manifest,'runs':runs,
        'all_pass':all(x['returncode']==0 and x['status']=='PASS' for x in runs),
        'scope':'Execution checks only. All five complete programs were read. K67/K70/K81/K82/K83 whole geometric proofs have separate current records.',
        'historical_program_prose':'The unchanged K67 final stdout line and K83 program preamble/output retain historical working/audit-pending wording. Those strings carry no current proof credit. Full current proof review, including the K83 receiving inequality repair, is recorded separately.'}
(P/'analysis/IV/root_K67_83_certificate_replays.json').write_text(json.dumps(record,indent=2))
print(json.dumps({'all_pass':record['all_pass'],'runs':[{k:r[k] for k in ['program','returncode','status','seconds']} for r in runs]},indent=2))
raise SystemExit(0 if record['all_pass'] else 1)
