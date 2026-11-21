"""Recompute current counts from attachments and explicitly named event bundles."""
from pathlib import Path
import subprocess, json, shutil, datetime

r=Path(__file__).resolve().parents[1]
inputs=sorted((r/'agents').rglob('S6_SERIES_PUBLISH*CHECK_EVENTS.tsv'))
inputs+=sorted((r/'records').glob('S6_SERIES_PUBLISH_*_root_*CHECK_EVENTS.tsv'))
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
 'command':cmd,'exit_code':result.returncode
},indent=2)+'\n')
print(result.stdout)
