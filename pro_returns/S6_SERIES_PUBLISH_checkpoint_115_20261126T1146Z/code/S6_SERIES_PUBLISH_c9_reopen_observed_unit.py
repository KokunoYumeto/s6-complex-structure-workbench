"""Reopen one exact existing unit from an authored actual finding."""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import argparse
import csv
import hashlib
import io

ROOT = Path(__file__).resolve().parents[1]
csv.field_size_limit(100000000)
p = argparse.ArgumentParser()
p.add_argument('--unit', required=True)
p.add_argument('--type', required=True)
p.add_argument('--evidence', required=True)
p.add_argument('--reason', required=True)
p.add_argument('--source-sha256', required=True)
a = p.parse_args()
assert hashlib.sha256((ROOT / 'S6_SERIES_PUBLISH_III.tex').read_bytes()).hexdigest() == a.source_sha256
assert (ROOT / a.evidence).is_file() and a.unit in (ROOT / a.evidence).read_text()
path = ROOT / 'S6_SERIES_PUBLISH_unit_progress.tsv'
raw = path.read_bytes()
reader = csv.DictReader(io.StringIO(raw.decode(), newline=''), delimiter='\t')
fields = reader.fieldnames
rows = list(reader)
row, = [r for r in rows if (r['paper'], r['unit_id'], r['row_kind'], r['defect_type']) == ('III', a.unit, 'defect', a.type)]
old = dict(row)
assert row['status'] == 'done'
now = datetime.now(timezone.utc).isoformat()
row.update(status='open', date_utc=now, evidence=row['evidence'] + '; ' + a.evidence,
    detail=row['detail'] + ' Reopened from actual reading: ' + a.reason.strip() + ' This reopening earns no movement credit.')
def encode(value):
    stream = io.StringIO(newline='')
    csv.DictWriter(stream, fields, delimiter='\t', lineterminator='\n').writerow(value)
    return stream.getvalue().encode()
before, after = encode(old), encode(row)
assert raw.count(before) == 1 and after not in raw
changed = raw.replace(before, after, 1)
assert changed.replace(after, before, 1) == raw and b'\r' not in changed
assert path.read_bytes() == raw
path.write_bytes(changed)
assert path.read_bytes() == changed
print('UTC', now)
print('Reopened exact existing III unit', a.unit, a.type)
print('Evidence', a.evidence)
print('Reason', a.reason)
print('III units', dict(Counter(r['status'] for r in rows if r['paper'] == 'III')))
print('Only this exact existing unit row changed; all prior evidence and every other row byte preserved.')
