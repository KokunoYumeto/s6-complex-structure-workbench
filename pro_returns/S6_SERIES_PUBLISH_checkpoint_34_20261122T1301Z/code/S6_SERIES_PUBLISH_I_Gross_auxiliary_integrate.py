"""Apply the fully compared finite-splitting choice for Gross's auxiliary field."""
import datetime,hashlib,json
from pathlib import Path
from S6_SERIES_PUBLISH_editing import Editor
r=Path(__file__).resolve().parents[1];p=r/'agents/i_analytic/S6_SERIES_PUBLISH_I_Gross_auxiliary_guards.json'
data=json.loads(p.read_text());ed=Editor('I');before=hashlib.sha256(ed.before.encode()).hexdigest()
assert before==data['source_base_sha256']
for i,g in enumerate(data['guards']):
 ed.replace(g['old'],g['new'],'D25' if i==0 else 'D18',g['reason'],'ari:C.6.R3',count=g['expected_count'])
ed.save()
receipt={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'guard_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'source_before_sha256':before,'source_after_sha256':hashlib.sha256(ed.text.encode()).hexdigest(),'guards_applied':3,'root_scope':'Complete original,current and replacement proof read and compared, together with the complete agent scope comparison. The BFH splitting prescription supplies the missing discriminant prerequisite; theorem statement unchanged.','new_root_events':0,'existing_event':'One exposed used-and-rechecked association recorded by the analytic agent; no independent/computational credit.'}
(r/'records/S6_SERIES_PUBLISH_I_Gross_auxiliary_applied.json').write_text(json.dumps(receipt,indent=2)+'\n')
