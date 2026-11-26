"""Record the observed branch-integer naming case and its exact admission."""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import csv

ROOT = Path(__file__).resolve().parents[1]
csv.field_size_limit(100000000)
parser = argparse.ArgumentParser()
parser.add_argument('mode', choices=('open', 'close'))
parser.add_argument('--evidence', required=True)
args = parser.parse_args()
assert (ROOT / args.evidence).is_file()

def read(name):
    with (ROOT / name).open(newline='') as f:
        reader = csv.DictReader(f, delimiter='\t')
        return reader.fieldnames, list(reader)

def write(name, fields, rows):
    with (ROOT / name).open('w', newline='') as f:
        writer = csv.DictWriter(f, fields, delimiter='\t', lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)

uf, units = read('S6_SERIES_PUBLISH_unit_progress.tsv')
row, = [r for r in units if r['paper'] == 'III' and r['unit_id'] == 'maps:src:D.2.32' and r['defect_type'] == 'D20']
now = datetime.now(timezone.utc).isoformat()
if args.mode == 'open':
    assert row['status'] == 'done'
    detail = ' Reopened after actual current-source reading: the branch-shear integer k and its later k_0 spelling occur alongside the named primitive wedge class k. Root read the full shear paragraph, wedge-class definition and quotient map, and the later fixed-sweep branch morphism. The exact shear/inverse and all affected uses require qualification as one branch integer; paragraph separation is no exception.'
else:
    assert row['status'] == 'open'
    assert 'Admitted 2 exact source rows and 1 scoped used-and-rechecked events.' in (ROOT / args.evidence).read_text()
    detail = ' Closed by the root-reviewed two-fragment branch packet. The same branch integer k_br is followed through the shear, inverse subtraction, fixed-sweep change and primitive-class invariance. The wedge class retains its original formula and all quotient maps. Exact full-source reversal and permanent identifiers passed; changed-page gates remain open.'
row.update(status='open' if args.mode == 'open' else 'done', date_utc=now,
    evidence=row['evidence'] + '; ' + args.evidence, detail=row['detail'] + detail)
ff, findings = read('S6_SERIES_PUBLISH_findings_III.tsv')
finding, = [r for r in findings if r['id'] == 'P15']
assert finding['status'] == 'open'
finding['date_utc'] = now
finding['source_resolution'] += detail
finding['remaining_gate'] = 'Finish every actual remaining D20 source role and final authored-retention/whole-paper P11/P15 disposition. The final count paragraph and same-source builds follow; all final changed-page gates remain open.'
write('S6_SERIES_PUBLISH_unit_progress.tsv', uf, units)
write('S6_SERIES_PUBLISH_findings_III.tsv', ff, findings)
print('02L8 branch naming criterion:', row['status'])
print('Source, raw events and derived counts unchanged by this status record; final image gates remain open.')
