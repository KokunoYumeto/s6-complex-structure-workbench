"""Close P11/P15 only after the actual final authored source dispositions."""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import csv

ROOT = Path(__file__).resolve().parents[1]
csv.field_size_limit(100000000)
parser = argparse.ArgumentParser()
parser.add_argument('--reviewed', required=True)
parser.add_argument('--named-retentions', required=True)
args = parser.parse_args()

def read(name):
    with (ROOT / name).open(newline='') as f:
        reader = csv.DictReader(f, delimiter='\t')
        return reader.fieldnames, list(reader)

_, units = read('S6_SERIES_PUBLISH_unit_progress.tsv')
source_rows = [r for r in units if r['paper'] == 'III' and r['defect_type'] == 'D20']
assert source_rows and all(r['status'] == 'done' for r in source_rows), [(r['unit_id'], r['status']) for r in source_rows if r['status'] != 'done']
_, required = read('S6_SERIES_PUBLISH_required_progress_III.tsv')
assert len(required) == 128 and all(r['status'] == 'done' for r in required)
reviews = [
    'agents/continuation9_global_sweep/S6_SERIES_PUBLISH_c9_P11_P15_final_source_disposition.md',
    'agents/continuation9_retained_scopes/S6_SERIES_PUBLISH_c9_authored_retention_disposition.md',
    args.named_retentions,
]
for name in reviews:
    assert (ROOT / name).is_file(), name
_, events = read('CHECK_EVENTS.tsv')
event_ids = {
    'ce:c9-iii-current02-02kd-retention-reconciliation',
    'ce:c9-iii-current02-02ls-retention-reconciliation',
    'ce:c9-iii-current02-02l8-branch-retention',
    'C9-III-RETAINED-02LL-USED-001',
    'publish:c9:III:02LE:period_vector',
    'ce:c9-iii-current02-02lq-retention-reconciliation',
    'C9-III-RETAINED-02L1-USED-001',
    'C9-III-RETAINED-02L7-USED-001',
    'publish:c9:III:02OG:generator_branch',
    'ce:c9-iii-current02-02l2-retention-reconciliation',
}
for event_id in event_ids:
    event, = [e for e in events if e['event_id'] == event_id]
    assert event['source_event_type'] == 'used and rechecked in this run', event_id
fields, findings = read('S6_SERIES_PUBLISH_findings_III.tsv')
assert all(r['status'] == 'done' for r in findings if r['id'] not in ('P4', 'P11', 'P15', 'T1'))
now = datetime.now(timezone.utc).isoformat()
for key in ('P11', 'P15'):
    row, = [r for r in findings if r['id'] == key]
    assert row['status'] == 'open', key
    conclusion = (
        'The named and whole-source inverse/identity prose decisions, complete attributed candidate02 image reading, and all subsequent exact source repairs have their final contextual dispositions. Actual group, lattice, chart, gauge, collar, quotient, section and homotopy inverse maps retain their complete formulas. Only the specifically recorded reverse-name or repeated identity prose was removed.'
        if key == 'P11' else
        'Every concrete naming case from the original named finding, contextual source pass, complete candidate02 image reading and final authored-retention reconciliation is settled by its admitted exact packet or actual current-symbol/formal-input identity. Paragraph or item separation gives no exception. The final period, finite-lift, branch, lattice, relation and downstream-import comparisons preserve their original objects, entries, maps and inverses. The attributed complete and bounded proof-read scopes remain exactly those recorded by their readers; no fresh full-source proof read beyond those scopes is claimed.'
    )
    row.update(status='done', date_utc=now,
        source_resolution=row['source_resolution'] + ' Final source disposition: ' + conclusion + ' Root review: ' + args.reviewed,
        remaining_gate='Final count-paragraph agreement, both repaired-source builds, actual changed-page reading and all final layout/provenance gates remain separately open. No final-PDF or independent-proof credit is created by this source closure.',
        evidence=row['evidence'] + '; ' + '; '.join(reviews))
path = ROOT / 'S6_SERIES_PUBLISH_findings_III.tsv'
with path.open('w', newline='') as f:
    writer = csv.DictWriter(f, fields, delimiter='\t', lineterminator='\n')
    writer.writeheader()
    writer.writerows(findings)
print('P11 and P15 closed at the exact final source-disposition scope.')
print('All required128 III checks retained. P4 remains joint; no source, raw event, derived count or visual gate changed.')
print('Root review:', args.reviewed)
