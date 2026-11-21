"""Apply the read classical-beta citation comparison and final Fourier grammar guard."""
import datetime,hashlib,json
from pathlib import Path
from S6_SERIES_PUBLISH_editing import Editor
r=Path(__file__).resolve().parents[1];ed=Editor('I');before=hashlib.sha256(ed.before.encode()).hexdigest()
files=['agents/i_provenance/S6_SERIES_PUBLISH_I_candidate11_beta_guards.json','agents/i_analytic/S6_SERIES_PUBLISH_I_final_global_ABC_grammar_guard.json'];bindings=[]
for f in files:
 p=r/f;d=json.loads(p.read_text());gs=d.get('changes',d.get('guards',[]))
 assert d.get('source_sha256',d.get('source_base_sha256'))==before
 for g in gs:
  kind='D17' if g['id'].endswith('BETA01') else 'D18' if g['id'].endswith('BETA02') else 'D08' if g['id'].endswith('BETA03') else 'D23'
  ed.replace(g['old'],g['new'],kind,g['reason'],g.get('statement','ari:C.8.2'),count=g.get('expected_count',1))
 bindings.append({'file':f,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'guards':len(gs)})
ed.save()
receipt={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source_before_sha256':before,'source_after_sha256':hashlib.sha256(ed.text.encode()).hexdigest(),'packages':bindings,'root_comparison':'Complete old/new beta proof read, with exact pair, measure and convergence map; final wording changes and Fourier guard read. Complete source comparisons are in the delegated records.','new_root_events':0}
(r/'records/S6_SERIES_PUBLISH_I_beta_and_grammar_applied.json').write_text(json.dumps(receipt,indent=2)+'\n')
