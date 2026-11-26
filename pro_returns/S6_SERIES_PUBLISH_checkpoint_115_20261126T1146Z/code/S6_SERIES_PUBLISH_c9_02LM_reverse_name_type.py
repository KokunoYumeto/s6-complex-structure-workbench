"""Correct the single pure reverse-name deletion to its registered D08 type."""
from pathlib import Path
from datetime import datetime, timezone
import csv

ROOT = Path(__file__).resolve().parents[1]
csv.field_size_limit(100000000)
p = ROOT / 'S6_SERIES_PUBLISH_defects_III.tsv'
with p.open(newline='') as stream:
    reader = csv.DictReader(stream, delimiter='\t')
    fields, rows = reader.fieldnames, list(reader)
row, = [r for r in rows if r['change_id'] == 'C9-III-02LM-NOTATION-005']
assert row['type'] == 'D20'
row['type'] = 'D08'
row['review_status'] += ' Root type correction ' + datetime.now(timezone.utc).isoformat() + ': D20 to D08. This row removes only the literal reverse-name restatement identified by P11; it changes no object assignment. Its exact old/new source fragments and used-event scope are unchanged.'
with p.open('w', newline='') as stream:
    writer = csv.DictWriter(stream, fields, delimiter='\t', lineterminator='\n')
    writer.writeheader()
    writer.writerows(rows)
print('Corrected C9-III-02LM-NOTATION-005 from D20 to D08; exact source fragments, all other rows and check events retained.')
