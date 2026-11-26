"""Close one root-reviewed source naming criterion at its admitted scope."""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import csv

ROOT = Path(__file__).resolve().parents[1]
csv.field_size_limit(100000000)
parser = argparse.ArgumentParser()
parser.add_argument('--unit', required=True)
parser.add_argument('--event', required=True)
parser.add_argument('--review', required=True)
parser.add_argument('--admission', required=True)
parser.add_argument('--rows', type=int, required=True)
parser.add_argument('--events', type=int, required=True)
parser.add_argument('--detail', required=True)
args = parser.parse_args()
assert (ROOT / args.review).is_file()
admission = (ROOT / args.admission).read_text()
assert f'Admitted {args.rows} exact source rows and {args.events} scoped used-and-rechecked events.' in admission
with (ROOT / 'CHECK_EVENTS.tsv').open(newline='') as f:
    event, = [r for r in csv.DictReader(f, delimiter='\t') if r['event_id'] == args.event]
assert event['source_event_type'] == 'used and rechecked in this run'
path = ROOT / 'S6_SERIES_PUBLISH_unit_progress.tsv'
with path.open(newline='') as f:
    reader = csv.DictReader(f, delimiter='\t')
    fields, rows = reader.fieldnames, list(reader)
row, = [r for r in rows if r['paper'] == 'III' and r['unit_id'] == args.unit and r['defect_type'] == 'D20']
assert row['status'] == 'open', args.unit
row.update(status='done', date_utc=datetime.now(timezone.utc).isoformat(),
    evidence=row['evidence'] + '; ' + args.review + '; ' + args.admission,
    detail=row['detail'] + ' Exact current-source disposition admitted: ' + args.detail + ' Complete-source reversal and permanent identifiers passed; final changed-page gates remain open. No independent-proof credit is added.')
with path.open('w', newline='') as f:
    writer = csv.DictWriter(f, fields, delimiter='\t', lineterminator='\n')
    writer.writeheader()
    writer.writerows(rows)
print('Closed D20:', args.unit)
print(args.detail)
print('No source, raw event, derived count or other unit changed.')
