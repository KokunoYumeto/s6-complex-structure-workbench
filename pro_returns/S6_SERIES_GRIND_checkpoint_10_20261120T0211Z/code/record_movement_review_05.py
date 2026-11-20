"""Record scheduled review5 once; preserve earlier reviews and pending proposals."""
from pathlib import Path
from collections import Counter
import csv, datetime, hashlib, json

R = Path(__file__).resolve().parents[1]
now = datetime.datetime.now(datetime.timezone.utc)
assert now >= datetime.datetime(2026, 11, 20, 1, 40, 1, tzinfo=datetime.timezone.utc)
p = R / 'analysis/movement_reviews.json'
reviews = json.loads(p.read_text())
assert len(reviews) == 4 and reviews[-1]['review_number'] == 4
with (R / 'S6_SERIES_GRIND_inventory.csv').open() as f:
    rows = list(csv.DictReader(f))
done = [r for r in rows if r['completion_state'].startswith('done')]
pending = [r for r in rows if not r['completion_state'].startswith('done')]
labels = sorted({r['label'] for r in done})
new = sorted(set(labels) - set(reviews[-1]['completed_unique_labels']))
snapshot = R / 'analysis/review05_all_open_rows.tsv'
assert not snapshot.exists()
fields = ['label', 'tag', 'paper', 'status', 'completion_state', 'confidence_state', 'confidence_line', 'remaining_risk', 'format_check', 'layout_check']
with snapshot.open('w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=fields, delimiter='\t', extrasaction='ignore')
    w.writeheader()
    w.writerows(pending)
math_open = [{k:r.get(k, '') for k in ['label', 'tag', 'paper', 'status', 'remaining_risk']}
             for r in rows if r['status'] in ['open', 'proved under hypotheses H']]
gates = dict(reviews[-1]['main_gates'])
gates['five finished papers'] = f'{len(labels)} unique labels and {len(done)} source placements meet the recorded whole-row requirements; {len(pending)} placements retain their individual gates. Full snapshot: analysis/review05_all_open_rows.tsv.'
gates['maps:src:D.2.4'] = ('The weighted OS45/default member with P=2G, Q=8G, weights(2,0,0,0,0), prescribed triangular Mumford caps and ordinary clutch e=1 now has a complete accepted proof P_ref=0. The actual theta/fan collar, embedded odd sphere, integral Wang mod2 detector, equivariant relative lambda class, reference-frame transport and total critical-specialization parity are written and integrated. Broader star-log sectors and h>1 original-additive-cap torsion markings remain open. The D2.53 whole-row chronology/prerequisite gates are assessed separately.')
gates['inv:E2.3'] = ('The full root proof for a nonempty open twelve-tooth family and an independently frozen full derivation both give K12=O(-8) plus O(-9)^2. The receiving reviewer reports agreement and two explicit publication-completeness paragraphs. Root has not yet read the complete independent proof or imported the receiving report; the proposal remains pending and contributes no accepted movement at this review.')
gates['Paper V global topology'] = ('The algebraic reconstruction and exact adapters remain valid. A new all-degree integral geometric comparison, including the signed cap maps and freeword cusp homotopy, is frozen with154 exact assertions. Root and receiving review are still in progress. P1.19 remains open in the final part until the full geometric maps have been accepted and integrated. No candidate computation or claimed diagram comparison receives closure credit.')
for label in ['night:P1.19', 'night:P1.4', 'night:P1.8', 'night:P1.17']:
    rr = [r for r in rows if r['label'] == label]
    if rr:
        gates[label] = '; '.join(dict.fromkeys(r['completion_state'] + ' — ' + r['remaining_risk'] for r in rr))
receipts = [
    'analysis/III_refined_class_integration_09.json',
    'analysis/III_refined_final_QA_import_09.json',
    'audit_corrections/III_equivariant_09/independent_full_derivation.md',
    'audit_sign/III_equivariant_09/statement_first_derivation.md',
    'audit_sign/III_equivariant_09/receiving_comparison.md',
    'audit_sign/III_equivariant_09/MV_oddness_addendum.md',
    'audit_sign/III_equivariant_09/collar_exact_certificate.json',
    'audit_sign/III_equivariant_09/MV_oddness_exact_certificate.json',
    'audit_corrections/III_equivariant_09/post_freeze_receiving_supplement.md',
    'audit_corrections/III_equivariant_09/build38_visual_QA.json',
    'analysis/III_final_crossreference_transport_09.json',
    'analysis/P14_final_completion_08.json',
    'analysis/current_reference_integrity.json',
    'analysis/crosspaper_current_page_comparison.json',
    'analysis/checkpoint_09_receipt.json',
]
assert all((R / x).is_file() for x in receipts)
reductions = [
    f'{len(new)} further unique labels reached whole-row completion at the recorded proof/source/computation/format/layout scopes: ' + ', '.join(new) + '.',
    'Weighted OS45/default refined class: the previously unresolved0-or4 alternative in Z/8 is resolved by the complete accepted and integrated proof P_ref=0 for the specified P,Q,weights,caps,e=1 member. The wider D2.4 family remains open.'
]
movement = True
record = {
    'review_number':5, 'utc':now.isoformat(), 'scheduled_utc':'2026-11-20T01:40:01Z',
    'interval':'Fifth scheduled formal review, one hour after review4; recorded after immutable checkpoint09 verification.',
    'mathematical_status_changes':['Weighted OS45/default D2.53 subcase: refined-class gate resolved with P_ref=0; broader D2.4 remains open.'],
    'strictly_smaller_main_gates':reductions,
    'new_completed_unique_labels':new, 'completed_unique_labels':labels,
    'completed_inventory_placements':len(done),
    'whole_row_completion_counts':dict(Counter(r['completion_state'] for r in rows)),
    'all_open_rows_snapshot':str(snapshot.relative_to(R)),
    'all_open_rows_snapshot_sha256':hashlib.sha256(snapshot.read_bytes()).hexdigest(),
    'all_open_inventory_placements':len(pending), 'open_rows':math_open, 'main_gates':gates,
    'movement':movement, 'consecutive_reviews_without_movement':0,
    'evidence_sha256':{x:hashlib.sha256((R/x).read_bytes()).hexdigest() for x in receipts},
    'qualification':'Only completed whole rows or strict mathematical gate reductions count. The comb and Paper V geometric proposals remain pending acceptance. Clean builds, source opening, exact checks, packaging and equivalent reformulations alone receive no movement credit.',
    'decision':'Continue the authorized work.', 'next_review_utc':'2026-11-20T02:40:01Z'
}
reviews.append(record)
p.write_text(json.dumps(reviews, indent=2) + '\n')
rp = R / 'analysis/run.json'
run = json.loads(rp.read_text())
run['next_movement_review_utc'] = record['next_review_utc']
rp.write_text(json.dumps(run, indent=2) + '\n')
lines = [f'\n## {now.isoformat()} — formal movement review5\n',
         f'Movement: True. Consecutive reviews without movement:0. Continue the authorized work. Next review:{record["next_review_utc"]}.\n',
         '### Strict reductions since review4\n']
lines += ['- ' + x + '\n' for x in reductions]
lines += ['\n### Current main gates\n']
lines += ['- **' + k + '**: ' + v + '\n' for k,v in gates.items()]
lines += ['\n### Every mathematically open placement\n']
lines += [f"- {r['paper']} {r['label']} [{r['tag']}]: {r['status']}.\n" for r in math_open]
lines += [f'\nThe full {len(pending)}-placement pending snapshot is `{snapshot.relative_to(R)}`, SHA256`{record["all_open_rows_snapshot_sha256"]}`.\n', record['qualification'] + '\n']
with (R/'PROGRESS_LEDGER.md').open('a') as f:
    f.write('\n'.join(lines))
print(json.dumps({'review':5, 'utc':now.isoformat(), 'movement':movement,
    'new_done_labels':new, 'done_labels':len(labels), 'done_placements':len(done),
    'next_review':record['next_review_utc']}))
