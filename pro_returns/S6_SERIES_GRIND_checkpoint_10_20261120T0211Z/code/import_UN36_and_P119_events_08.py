"""Import the accepted UN36 row and preserve the nine P1.19 event scopes."""
from pathlib import Path
import csv, datetime, hashlib, json

R = Path(__file__).resolve().parents[1]
proposal_path = R/'audit_sign/UN36_final_completion_proposal_08.json'
proposal = json.loads(proposal_path.read_text())
inventory_path = R/'S6_SERIES_GRIND_inventory.csv'
with inventory_path.open() as f:
    reader = csv.DictReader(f); columns = list(reader.fieldnames); rows = list(reader)
matched = [r for r in rows if r['label'] == proposal['label']]
assert len(matched) == 1
changes = []
for update in proposal['guarded_source_updates']:
    field = update['field']
    assert matched[0].get(field, '') == update['old_value'], field
    if field not in columns: columns.append(field)
    value = update['new_value']
    if field == 'credit_transport':
        value = value.replace('Its torsion-free kernel is the stated K_i.',
                              'On H2(Z_i;Z) modulo its torsion, the kernel of this intersection map is the stated K_i.')
    matched[0][field] = value
    changes.append(dict(update, applied_value=value))
with inventory_path.open('w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=columns); writer.writeheader(); writer.writerows(rows)

assessment_path = R/'audit_sign/row_assessments.json'
assessment = json.loads(assessment_path.read_text())
before = assessment[proposal['label']]
assessment[proposal['label']] = proposal['assessment_proposal']
assessment_path.write_text(json.dumps(assessment, indent=2, ensure_ascii=False)+'\n')

event_path = R/'audit_p119_fresh/events_08.jsonl'
event_rows = [json.loads(line) for line in event_path.read_text().splitlines() if line.strip()]
types = {
    'fresh_computation_from_isolated_inputs': 'computation or formal certificate',
    'verification_of_own_saved_arrays': 'computation or formal certificate',
    'pre_receiving_derivation_freeze': 'independent re-proof',
    'receiving_proof_read_and_full_review': 'targeted proof check',
    'post_receiving_argument_tightening': 'targeted proof check',
    'receiving_saved_outputs_read': 'used and rechecked in this run',
    'post_receiving_convention_correction': 'targeted proof check',
    'full_integral_chain_comparison': 'computation or formal certificate',
    'whole_row_proposal_pending_final_QA': 'used and rechecked in this run',
}
out=[]
for n, event in enumerate(event_rows, 1):
    when = event.get('utc') or event['utc_interval']['saved_mtime']
    outcome = event['scope']
    if event.get('exposure'): outcome += ' Exposure: '+event['exposure']
    outcome += ' Exact source event: audit_p119_fresh/events_08.jsonl, row '+str(n)+'.'
    out.append({'statement_id': 'night:P1.19', 'date': when,
                'who': 'GPT-6 Astra (OpenAI), ChatGPT Pro mode, reasoning effort inherited; no separate numeric effort exposed, S6_SERIES_GRIND/p119_fresh_derivation',
                'type': types[event['event_type']], 'outcome': outcome,
                'event_id': 'ce:grind-p119-fresh-08:'+str(n),
                'evidence_group': 'ce:grind-p119-fresh-08:'+str(n)})
tsv = R/'audit_p119_fresh/events_08.tsv'
assert not tsv.exists()
with tsv.open('w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=list(out[0]), delimiter='\t'); writer.writeheader(); writer.writerows(out)

receipt = {
    'utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'UN36_proposal_sha256': hashlib.sha256(proposal_path.read_bytes()).hexdigest(),
    'UN36_source_changes': changes, 'UN36_assessment_before': before,
    'UN36_assessment_after': proposal['assessment_proposal'],
    'P119_source_event_sha256': hashlib.sha256(event_path.read_bytes()).hexdigest(),
    'P119_typed_events': out,
    'scope': 'UN36 alone closes at the exact accepted provenance. P1.19 event transport preserves each chronology and exposure statement; its canonical completion remains pending final actual visual review.'
}
(R/'analysis/UN36_and_P119_events_import_08.json').write_text(json.dumps(receipt, indent=2)+'\n')
print(json.dumps({'UN36_done': 1, 'P119_typed_events': len(out)}))
