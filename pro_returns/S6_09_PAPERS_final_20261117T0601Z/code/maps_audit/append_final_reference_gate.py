"""Append the final bounded reference check without erasing earlier proof events."""
from pathlib import Path
import json,hashlib
D=Path(__file__).resolve().parents[2];W=D/'work/maps_audit'
gate=W/'III_course_common_reference_final_gate.json'
g=json.loads(gate.read_text())
assert not g['pending_review_records']
assert g['all_original_mathematical_expressions_unchanged']
event={
    'event_id':'final-course-common-reference-check-20261117',
    'reader':'GPT-6 Astra (OpenAI, ChatGPT Pro mode)',
    'effort':'Pro','date':'2026-11-17',
    'scope':'All33 retained chapter reference namespaces, pinned course links and residual plain local/companion numbered locators; independent exact target reviews linked in the final gate. All source proof content retained. This is an additional reference/retention event, not a replacement for earlier complete proof readings.',
    'gate':'deliverables/work/maps_audit/III_course_common_reference_final_gate.json',
    'gate_sha256':hashlib.sha256(gate.read_bytes()).hexdigest(),
    'exact_changes':'deliverables/work/maps_audit/III_course_common_reference_repairs.json',
    'rows_in_gate':33,'consolidated_paragraph_edits':g['repair_counts']['paragraph_changes'],
    'all_original_mathematical_expressions_unchanged':True,
    'explicit_addition':'Circle example: the printed signed diagonal formula is applied to basis(1,a) and dual basis(a,1), replacing a pointer to an omitted exercise.',
    'nonoperative_provenance_move':'The broader operator-algebra course comparison remains verbatim in the exact move ledger; the operative pointer now cites the complete printed polynomial-clutching proof.',
    'root_owned_following_gate':'Theorem-label placement, literal raw-LaTeX fences and native statement/proof-boundary normalization, followed by final compilation.'
}
course_path=W/'III_course249_final_closure.json'
rows=json.loads(course_path.read_text())
assert len(rows)==249
for row in rows:
    row['final_common_reference_check']=event
course_path.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
lookup={(r['source_run'],r['source_id']):r for r in rows}
combined_path=W/'III_final_closure_overlay.json'
combined=json.loads(combined_path.read_text())
assert len(combined)==380
for i,row in enumerate(combined):
    key=(row['source_run'],row['source_id'])
    if key in lookup:
        row['final_common_reference_check']=event
combined_path.write_text(json.dumps(combined,ensure_ascii=False,indent=2)+'\n')
summary_path=W/'III_final_closure_summary.json'
summary=json.loads(summary_path.read_text())
summary['final_common_reference_gate']=event
summary_path.write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
events_path=W/'check_events.json'
events=json.loads(events_path.read_text())
assert isinstance(events,list)
if not any(e.get('event_id')==event['event_id'] for e in events):
    events.append(event)
events_path.write_text(json.dumps(events,ensure_ascii=False,indent=2)+'\n')
print({'course_rows_updated':len(rows),'combined_rows_preserved':len(combined),'event':event['event_id']})
