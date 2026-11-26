"""Record one confirmed source-role reopening with its actual evidence."""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import csv

ROOT = Path(__file__).resolve().parents[1]
csv.field_size_limit(100000000)
parser = argparse.ArgumentParser()
parser.add_argument('--unit', required=True)
parser.add_argument('--evidence', required=True)
parser.add_argument('--detail', required=True)
args = parser.parse_args()
assert (ROOT / args.evidence).is_file()
path = ROOT / 'S6_SERIES_PUBLISH_unit_progress.tsv'
with path.open(newline='') as f:
    reader = csv.DictReader(f, delimiter='\t')
    fields, rows = reader.fieldnames, list(reader)
row, = [r for r in rows if r['paper'] == 'III' and r['unit_id'] == args.unit and r['defect_type'] == 'D20']
assert row['status'] == 'done', args.unit
row.update(status='open', date_utc=datetime.now(timezone.utc).isoformat(),
    evidence=row['evidence'] + '; ' + args.evidence,
    detail=row['detail'] + ' Reopened for the confirmed current-source role: ' + args.detail + ' Exact repair and affected-use comparison remain; all final rendering gates remain open.')
with path.open('w', newline='') as f:
    writer = csv.DictWriter(f, fields, delimiter='\t', lineterminator='\n')
    writer.writeheader()
    writer.writerows(rows)
print('Reopened D20:', args.unit)
print(args.detail)
print('No source, raw event, derived count or other unit changed.')
