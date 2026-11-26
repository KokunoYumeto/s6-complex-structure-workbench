"""Close the completed P15 source sweep and the six observed D20 reopenings."""
from pathlib import Path
from datetime import datetime, timezone
import csv

ROOT = Path(__file__).resolve().parents[1]
csv.field_size_limit(100000000)

def read_table(name):
    with (ROOT / name).open(newline='') as stream:
        r = csv.DictReader(stream, delimiter='\t')
        return r.fieldnames, list(r)

def write_table(name, fields, rows):
    with (ROOT / name).open('w', newline='') as stream:
        w = csv.DictWriter(stream, fields, delimiter='\t', lineterminator='\n')
        w.writeheader()
        w.writerows(rows)

_, defects = read_table('S6_SERIES_PUBLISH_defects_III.tsv')
_, events = read_table('CHECK_EVENTS.tsv')
ids = {r['change_id'] for r in defects}
assert all(f'CLAUDE-III-P15-02LV-{n:03d}' in ids for n in range(1,49))
assert any(r['event_id'] == 'publish:c9:III:02LV:full-notation-context' for r in events)
assert any(r['event_id'] == 'publish:c9:III:02LK:notation-reread' for r in events)
assert any(r['event_id'] == 'publish:c9:III:02LR:notation-reread' for r in events)
reviews = [
    'agents/continuation9_global_sweep/S6_SERIES_PUBLISH_c9_P15_contextual_review.md',
    'agents/continuation9_findings/S6_SERIES_PUBLISH_c9_P15_bounded_scope_disposition.md',
    'agents/continuation9_findings/S6_SERIES_PUBLISH_c9_two_proof_P15_review.md',
    'agents/continuation9_findings/S6_SERIES_PUBLISH_c9_02KS_P15_review.md',
    'agents/continuation9_02LV_notation/S6_SERIES_PUBLISH_III_02LV_notation_review.md']
assert all((ROOT / name).exists() for name in reviews)
now = datetime.now(timezone.utc).isoformat()
ff, findings = read_table('S6_SERIES_PUBLISH_findings_III.tsv')
row, = [r for r in findings if r['id'] == 'P15']
assert row['status'] == 'open'
row.update(status='done', date_utc=now,
    source_resolution='The named02KM locus and whole-source contextual pass are complete. All identified persistent symbol collisions have exact admitted old/new rows and forward/reverse maps. Full bounded rereads cover02KM,02LE,02LQ,02KS,02LK,02LR,02LV and the recorded carrier interval; other inspected loci retain their explicitly recorded scopes. The final02LV packet makes the formerly unbound Wang boundary explicit through the marked cusp period maps. No unresolved source instance remains in those dispositions.',
    remaining_gate='Actual final rendered-page reading and all publication build/layout gates remain separate; no complete rereading of every unchanged proof or new independent proof is claimed.',
    evidence='; '.join(reviews) + '; code/S6_SERIES_PUBLISH_c9_02LK_notation.py/.out; code/S6_SERIES_PUBLISH_c9_02LR_notation.py/.out; all canonical CLAUDE-III-P15 rows and their scoped CHECK_EVENTS')
uf, units = read_table('S6_SERIES_PUBLISH_unit_progress.tsv')
observed = {'maps:src:D.2.25', 'maps:src:D.2.26', 'maps:src:D.2.31',
            'maps:src:D.2.41', 'maps:src:D.2.50', 'wb:sphere-metric-tangent-scope'}
closed = set()
for row in units:
    if row['paper'] == 'III' and row['defect_type'] == 'D20' and row['unit_id'] in observed:
        assert row['status'] == 'open', row['unit_id']
        row.update(status='done', date_utc=now,
            evidence='agents/continuation9_global_sweep/S6_SERIES_PUBLISH_c9_P15_contextual_review.md; canonical CLAUDE-III-P15 rows; matching c9 scoped used-and-rechecked events',
            detail='The actual notation instances that reopened this criterion are repaired and logged. The complete contextual source disposition traces each changed object through its dependent formulas and exact inverse name map; remaining local bindings retain the explicit scopes recorded there. Root read every admitted difference and reason. This source criterion does not grant PDF reading, clean-build or independent-proof credit.')
        closed.add(row['unit_id'])
assert closed == observed
write_table('S6_SERIES_PUBLISH_findings_III.tsv', ff, findings)
write_table('S6_SERIES_PUBLISH_unit_progress.tsv', uf, units)
print('P15 source finding closed, with six observed D20 criteria closed.')
print('Supplied findings:16 done; T1 full-build gate open; P4 reserved for the joint phase.')
print('The exact reading scopes remain in the existing records. No PDF or independent proof credit.')
