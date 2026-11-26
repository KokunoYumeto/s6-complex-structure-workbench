"""Recompute current counts from attachments and explicitly named event bundles."""
from pathlib import Path
import subprocess, json, shutil, datetime, csv, hashlib

r=Path(__file__).resolve().parents[1]
inputs=sorted((r/'agents').rglob('S6_SERIES_PUBLISH*CHECK_EVENTS.tsv'))
# This is a retained pre-binding copy of the same two events, not another
# event bundle. Prove the identity correspondence before excluding its copy.
archived=[p for p in inputs if 'S6_SERIES_PUBLISH_I_candidate11_tail_before_locator_refresh' in p.parts]
excluded=[]
for p in archived:
 current=p.parent.parent/p.name
 with p.open() as f: old_rows=list(csv.DictReader(f,delimiter='\t'))
 with current.open() as f: current_rows={x['event_id']:x for x in csv.DictReader(f,delimiter='\t')}
 assert {x['event_id'] for x in old_rows}==set(current_rows)
 for old in old_rows:
  new=current_rows[old['event_id']]
  for key in ['statement_id','date','who','type','evidence_group']:
   assert old[key]==new[key],(p,key)
 excluded.append({'path':str(p.relative_to(r)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
                  'operative_bundle':str(current.relative_to(r)),
                  'reason':'Archived pre-binding version of identical event IDs, subjects, dates, checkers, types and evidence groups. Current bundle adds the applied-source outcome; count each event once.'})
inputs=[p for p in inputs if p not in archived]
inputs+=sorted((r/'records').glob('S6_SERIES_PUBLISH_*CHECK_EVENTS.tsv'))
assert len(set(inputs))==len(inputs)
cmd=['python',str(r/'agents/provenance/code/S6_SERIES_PUBLISH_recompute_records.py'),
     '--source',str(r.parent/'source'),'--output',str(r/'records'),
     '--tex-dir',str(r)]
for p in inputs: cmd+=['--extra-events',str(p)]
result=subprocess.run(cmd,check=True,capture_output=True,text=True)
shutil.copyfile(r/'records/CHECK_EVENTS.tsv',r/'CHECK_EVENTS.tsv')
(r/'records/S6_SERIES_PUBLISH_refresh_check_records.out').write_text(result.stdout)
(r/'records/S6_SERIES_PUBLISH_refresh_check_records.json').write_text(json.dumps({
 'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'event_bundles':[str(p.relative_to(r)) for p in inputs],
 'excluded_archived_event_versions':excluded,
 'command':cmd,'exit_code':result.returncode
},indent=2)+'\n')
print(result.stdout)
