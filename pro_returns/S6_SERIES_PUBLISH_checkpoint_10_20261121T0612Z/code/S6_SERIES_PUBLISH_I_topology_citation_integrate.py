from pathlib import Path
import datetime,hashlib,json
from S6_SERIES_PUBLISH_editing import Editor
r=Path(__file__).resolve().parents[1];ed=Editor('I')
p=r/'agents/i_topology/editorial/S6_SERIES_PUBLISH_I_candidate11_citation_guards.json'
x=json.loads(p.read_text())
for g in x['patches']:
 ed.replace(g['old'],g['new'],'D18',g['reason'],','.join(g['statement_ids']))
ed.save()
(r/'records/S6_SERIES_PUBLISH_I_topology_citation_applied.json').write_text(json.dumps({'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'guard_file':str(p.relative_to(r)),'guard_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'source_before_sha256':hashlib.sha256(ed.before.encode()).hexdigest(),'source_after_sha256':hashlib.sha256(ed.text.encode()).hexdigest(),'count':len(x['patches']),'root_review':'Every exact guard and the full primary locator closure report read before applying. Primary images actually read by topology; root does not claim an additional primary-image reading or mathematical event.','math_events_added':0},indent=2)+'\n')
