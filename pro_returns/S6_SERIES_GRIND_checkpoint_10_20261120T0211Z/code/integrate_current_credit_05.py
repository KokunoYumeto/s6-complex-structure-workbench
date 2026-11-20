"""Import exact reviewed source transports without awarding layout gates."""
from pathlib import Path
import csv, hashlib, json

R = Path(__file__).resolve().parents[1]
csv.field_size_limit(10**9)
receipt = R / 'analysis/current_credit_import_05.json'
assert not receipt.exists()
path = R / 'parts/I.body.linked.tex'
old = path.read_text(); new = old
patches = json.loads((R / 'audit_paper_i/open_atlas/page_locator_followup_patches.json').read_text())
for p in patches:
    assert new.count(p['old']) == 1
    new = new.replace(p['old'], p['new'], 1)
path.write_text(new)

credit = json.loads((R / 'audit_corrections/IV_low_F_inventory_credit_proposal.json').read_text())
assert len(credit) == 30
inventory = R / 'S6_SERIES_GRIND_inventory.csv'
with inventory.open() as f:
    rows = list(csv.DictReader(f))
columns = list(rows[0]); changes = []
for row in rows:
    label = row['label']
    if label in credit:
        changes.append({'source_inventory_row': row['source_inventory_row'], 'label': label,
                        'previous_fields': {k: row.get(k) for k in credit[label]},
                        'new_fields': credit[label]})
        row.update(credit[label])
    if label == 'inv:C3.8':
        row['credited_to'] = row['credited_to'].replace('section 6.4 scalar cocycle preceding Lemma 6.14',
            'section 6.4 scalar cocycle and Lemma 6.14 with full proof p.84, conventions pp.82--83')
        row['completion_state'] = 'pending independent reconstruction and rendered layout'
with inventory.open('w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=columns); writer.writeheader(); writer.writerows(rows)

assessment_path = R / 'audit_paper_i/row_assessments.json'
assessment = json.loads(assessment_path.read_text())
a = assessment['inv:C3.8']
a['remaining_risk'] = a['remaining_risk'].replace('The final source page locator, rendered-layout verification and global main-theorem assessment remain recorded gates.',
    'The source page locator is verified on original DGKX v1 p.84; rendered-layout verification and global main-theorem assessment remain recorded gates.')
a['completion_state'] = 'pending independent reconstruction and rendered layout'
assessment_path.write_text(json.dumps(assessment, indent=2, ensure_ascii=False) + '\n')

events_path = R / 'audit_root/CHECK_EVENTS.tsv'
with events_path.open() as f:
    events = list(csv.DictReader(f, delimiter='\t'))
fields = list(events[0]); event_id = 'root-I-atlas-integration-source-05'
assert not any(e['event_id'] == event_id for e in events)
events.append(dict(statement_id='inv:C3.8', date='2026-11-19',
    who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; inherited effort; S6_SERIES_GRIND root',
    type='targeted proof check',
    outcome='Applied the nine guarded full-proof and outline replacements after the complete receiving review in audit_root/I_coefficient_atlas_review_04.md. Preserved the entire earlier operator statement/proof and two gauge consequences; relocated the atlas before the actual final part. Reviewed all three source transports a=c+delta, f=-eta_DGKX and the Cech--Dolbeault sign. Freshly opened the primary Atiyah-class manuscript Theorem3.1 proof p10 and visually read original DGKXv1 p84 with its complete six-arrow scalar table and Lemma6.14 proof. Added exact p82--84 locator and standard-family parameter/fan hypotheses. Promoted the three canonical C3.8 mathematical aliases to proved, with independent before-reading reconstruction and rendered layout explicitly pending. This is a full targeted receiving review after reading, not a new blind proof.',
    event_id=event_id, phase='S6_SERIES_GRIND'))
with events_path.open('w', newline='') as f:
    writer=csv.DictWriter(f, fieldnames=fields, delimiter='\t'); writer.writeheader(); writer.writerows(events)
receipt.write_text(json.dumps({'I_patches':patches,
    'I_before_sha256':hashlib.sha256(old.encode()).hexdigest(),
    'I_after_sha256':hashlib.sha256(new.encode()).hexdigest(),
    'IV_credit_changes':changes, 'whole_row_completion_awarded':False,
    'source_page_reading':'Original DGKX v1 printed p84 viewed by root; full page/hypothesis receipt retained.'},indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'I_patches':len(patches),'IV_credit_row_updates':len(changes),'root_event_added':event_id}))
