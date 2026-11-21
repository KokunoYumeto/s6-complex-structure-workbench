from pathlib import Path
import datetime,hashlib,json,re
from S6_SERIES_PUBLISH_editing import Editor,block
r=Path(__file__).resolve().parents[1];ed=Editor('I');tag='PI19'
for p in list(r.glob('S6_SERIES_PUBLISH_*.tex'))+list((r.parent/'source').rglob('*.tex')):
 assert 'tag-'+tag not in p.read_text(errors='replace'),p
p=r/'agents/i_topology/editorial/S6_SERIES_PUBLISH_I_candidate11_cusp_guards.json';x=json.loads(p.read_text())
for g in x['patches']:
 ed.replace(g['old'],g['new'].replace('TOPOLOGY-CUSP-TAG',tag),'D14',g['reason'],','.join(g['statement_ids']))
ed.save()
receipt={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'guard_file':str(p.relative_to(r)),'guard_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'source_before_sha256':hashlib.sha256(ed.before.encode()).hexdigest(),'source_after_sha256':hashlib.sha256(ed.text.encode()).hexdigest(),'new_label':'I:lem:cusp-tube-contraction','new_tag':tag,'root_review':'Root read both complete candidate11 statement/proof blocks and every exact proposed guard, including the complete new lemma and proof. The component inequality and time-reparametrized homotopy have been checked from the displayed vector field and uniform tail bound. Topology independently performed the exposed complete original/current/proposed comparisons, with its existing one used-and-rechecked evidence group. No additional root mathematical event or independence credit.','applied_lemma':block(ed.text,'I:lem:cusp-tube-contraction'),'preserved_result_statements':['inv:B3.1','inv:B3.3'],'math_events_added_by_integration':0}
(r/'records/S6_SERIES_PUBLISH_I_cusp_contraction_applied.json').write_text(json.dumps(receipt,indent=2)+'\n')
