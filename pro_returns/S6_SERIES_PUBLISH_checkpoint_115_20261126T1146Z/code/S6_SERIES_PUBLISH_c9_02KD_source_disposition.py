"""Close the admitted early finite-homology source naming case."""
from pathlib import Path
from datetime import datetime, timezone
import csv

ROOT = Path(__file__).resolve().parents[1]
csv.field_size_limit(100000000)

def read(name):
    with (ROOT / name).open(newline='') as f:
        reader = csv.DictReader(f, delimiter='\t')
        return reader.fieldnames, list(reader)

def write(name, fields, rows):
    with (ROOT / name).open('w', newline='') as f:
        writer = csv.DictWriter(f, fields, delimiter='\t', lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)

_, events = read('CHECK_EVENTS.tsv')
event, = [r for r in events if r['event_id'] == 'ce:c9-iii-current02-02kd-retention-reconciliation']
assert event['source_event_type'] == 'used and rechecked in this run'
evidence = 'agents/continuation9_findings/S6_SERIES_PUBLISH_c9_current02_02KD_retention_review.md'
assert (ROOT / evidence).is_file()
assert (ROOT / 'code/S6_SERIES_PUBLISH_c9_admit_02KD_retention.out').is_file()
now = datetime.now(timezone.utc).isoformat()
uf, units = read('S6_SERIES_PUBLISH_unit_progress.tsv')
row, = [r for r in units if r['paper'] == 'III' and r['unit_id'] == 'maps:src:D.1.1' and r['defect_type'] == 'D20']
assert row['status'] == 'open'
row.update(status='done', date_utc=now,
    evidence=row['evidence'] + '; ' + evidence + '; code/S6_SERIES_PUBLISH_c9_admit_02KD_retention.out',
    detail=row['detail'] + ' The exact10-fragment packet is admitted after root reviewed every difference and the complete comparison. It assigns q_circ, C_fin, C_2^coh, C_j^tr and the two resolution generators through all affected maps and inverses, including the two actual02KF imports. The finite quotient functional and exported h,z,z_0,B retain their values. Explicit formal input coefficients keep their stated binders. Complete-source reversal and permanent targets passed. Final changed-page and publication gates remain open; no independent-proof credit.')
ff, findings = read('S6_SERIES_PUBLISH_findings_III.tsv')
row, = [r for r in findings if r['id'] == 'P15']
assert row['status'] == 'open'
row['date_utc'] = now
row['source_resolution'] += ' The early02KD current-source case is now admitted, including its two actual02KF circle-name imports and the complete coordinate/cohomology/homology/chain comparisons.'
row['remaining_gate'] = 'Finish and admit the actual02LL packet, then read the final authored-retention and whole-paper P11/P15 source disposition. The ledger paragraph and same-source builds follow source closure; changed-page/layout gates remain separately open.'
write('S6_SERIES_PUBLISH_unit_progress.tsv', uf, units)
write('S6_SERIES_PUBLISH_findings_III.tsv', ff, findings)
print('Closed the early02KD-containing maps:src:D.1.1 D20 row. Only the actual02LL-containing D20 scope remains open.')
print('Whole-paper source disposition and all final rendering gates remain open; raw events and derived counts unchanged.')
