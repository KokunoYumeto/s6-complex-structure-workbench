from pathlib import Path
import json,hashlib,datetime
from S6_SERIES_PUBLISH_editing import Editor
r=Path(__file__).resolve().parents[1];ed=Editor('I')
p=r/'agents/i_provenance/S6_SERIES_PUBLISH_I_primary_citation_guards_06.json';d=json.loads(p.read_text())
for x in d['changes']:ed.replace(x['old'],x['new'],'D04',x['reason'],x['id'],count=x.get('expected_count',1))
q=r/'agents/i_provenance/S6_SERIES_PUBLISH_I_shared_bib_guards_06.json';bd=json.loads(q.read_text());bp=r/'S6_SERIES_PUBLISH_references.bib';s=bp.read_text()
for x in bd['changes']:
 assert s.count(x['old'])==x.get('expected_count',1),x['id']
 s=s.replace(x['old'],x['new'])
ed.save();bp.write_text(s)
(r/'records/S6_SERIES_PUBLISH_I_primary6_integration.json').write_text(json.dumps({'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'guards':[{'path':str(z.relative_to(r)),'sha256':hashlib.sha256(z.read_bytes()).hexdigest()} for z in [p,q]],'scope':'Exact verified locator and bibliography integration; root read all replacements and their primary-opening receipt scopes. No mathematical event.'},indent=2)+'\n')
