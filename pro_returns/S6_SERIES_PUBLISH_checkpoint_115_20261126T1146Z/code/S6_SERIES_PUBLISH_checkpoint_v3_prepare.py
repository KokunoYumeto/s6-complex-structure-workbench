#!/usr/bin/env python3
"""Keep checkpoint prose synchronized with the validated defect-class state."""
from pathlib import Path
import datetime as dt,difflib,hashlib,json
R=Path(__file__).resolve().parents[1]
sha=lambda b:hashlib.sha256(b).hexdigest()
oldp=R/'code/S6_SERIES_PUBLISH_continuation2_checkpoint_v2.py';newp=R/'code/S6_SERIES_PUBLISH_continuation2_checkpoint_v3.py'
OUT=R/'records/S6_SERIES_PUBLISH_checkpoint_helper_v3';assert not OUT.exists() and not newp.exists()
b=oldp.read_bytes();assert sha(b)=='751dfa5b8fad97695665f0f0df168daed470b990f38741d4ed5d23684cb6a5a6';s=b.decode()
pairs=[
 (' assert 0<=resolved<=required_total\n'," assert 0<=resolved<=required_total\n from S6_SERIES_PUBLISH_continuation2_progress_review_v4 import update_defect_classes\n progress_rows=json.loads((R/'records/S6_SERIES_PUBLISH_progress_rows_current.json').read_text())['rows']\n update_defect_classes(progress_rows)\n defect_rows=[x for x in progress_rows if x['paper']=='II' and x['kind']=='defect']\n defect_done=sum(x['status']=='done' for x in defect_rows);defect_open=len(defect_rows)-defect_done\n"),
 ('required rows resolved and {required_total-resolved} open. Paper II source','required rows resolved and {required_total-resolved} open; {defect_done}/{len(defect_rows)} defect classes are complete and {defect_open} remain open. Paper II source'),
 ('II_additional_required_count=len(additional),source_sha256=sourcehash','II_additional_required_count=len(additional),II_defect_classes_done=defect_done,II_defect_classes_open=defect_open,source_sha256=sourcehash'),
 ('All 25 defect classes, restructuring, provenance, integrated typesetting and full rendered-page reading remain subject to their recorded gates.','Of the {len(defect_rows)} defect classes, {defect_done} are complete and {defect_open} remain open under their validated source audits. Restructuring, provenance, integrated typesetting and full rendered-page reading remain open.'),
 ('additional_II_required_count=len(additional),base_required=True)','additional_II_required_count=len(additional),II_defect_classes_done=defect_done,II_defect_classes_open=defect_open,base_required=True)')]
for old,new in pairs:assert s.count(old)==1,old;s=s.replace(old,new,1)
compile(s,str(newp),'exec');newp.write_text(s);OUT.mkdir()
diff=''.join(difflib.unified_diff(b.decode().splitlines(True),s.splitlines(True),fromfile=oldp.name,tofile=newp.name));(OUT/'helper.diff').write_text(diff)
record=dict(created_utc=dt.datetime.now(dt.timezone.utc).isoformat(),original_path=str(oldp.relative_to(R)),original_sha256=sha(b),new_path=str(newp.relative_to(R)),new_sha256=sha(s.encode()),diff_sha256=sha(diff.encode()),scope='Only validated defect-class counts and checkpoint prose added.45-minute schedule, archive selection and complete payload verification remain unchanged. No checkpoint created by this preparation.')
(OUT/'receipt.json').write_text(json.dumps(record,indent=2)+'\n')
note='''\n\n## Checkpoint32 count-scope clarification\n\nCheckpoint32's snapshot prose reported196/197 required checks and one open by the inherited197-row count. The current authoritative set at that time also contained the separately discovered P4.40 error row, so its full state was196/198 and two open, as review21 recorded. The old checkpoint and its prose remain immutable. Both open rows were resolved by the later R13/P4.40 correction; the current total is198/198. The distinct checkpoint_v2 helper corrected the required-row denominator, and checkpoint_v3 additionally derives defect-class counts from their source-validated closure records. This clarification changes no check event or progress status.\n'''
for name in ['PROGRESS_LEDGER.md','S6_SERIES_PUBLISH_report.md']:
 with (R/name).open('ab') as f:f.write(note.encode())
print(json.dumps(record,indent=2))
