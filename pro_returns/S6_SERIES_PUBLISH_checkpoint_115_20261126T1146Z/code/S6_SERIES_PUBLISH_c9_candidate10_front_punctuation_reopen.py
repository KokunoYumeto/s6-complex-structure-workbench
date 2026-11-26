"""Reopen the existing D23 row on the two actual main-theorem punctuation findings."""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import csv
import hashlib
import io

ROOT = Path(__file__).resolve().parents[1]
csv.field_size_limit(100000000)
path = ROOT / 'S6_SERIES_PUBLISH_unit_progress.tsv'
original = path.read_bytes()
source = (ROOT / 'S6_SERIES_PUBLISH_III.tex').read_bytes()
assert hashlib.sha256(source).hexdigest() == '5a95d62059fcaf7859df33f5793d9cd97462024d50a1f7ee59f9fae0b2704187'
reader = csv.DictReader(io.StringIO(original.decode(), newline=''), delimiter='\t')
fields, rows = reader.fieldnames, list(reader)
old, = [r for r in rows if (r['paper'], r['unit_id'], r['row_kind'], r['defect_type']) == ('III', 'series:III:main-theorems', 'defect', 'D23')]
assert old['status'] == 'done'
stamp = datetime.now(timezone.utc).isoformat()
new = dict(old)
new.update(status='open', date_utc=stamp,
    evidence=old['evidence'] + '; agents/continuation9_candidate10_front_punctuation/S6_SERIES_PUBLISH_c9_candidate10_front_punctuation_review.md; code/S6_SERIES_PUBLISH_c9_candidate10_front_punctuation.out',
    detail=old['detail'] + ' Root reread the entire current front matter at source215–954 and observed two literal punctuation defects in main B/F: a full stop immediately before the following lowercase where clause, and a comma splice after the integer parameter declaration. The two guarded punctuation proposals preserve every mathematical expression. Reopened on this actual source finding; exact source admission and complete successor-unit image inspection remain open. Historical evidence is retained.')

def encode(row):
    stream = io.StringIO(newline='')
    csv.DictWriter(stream, fields, delimiter='\t', lineterminator='\n').writerow(row)
    return stream.getvalue().encode()

old_bytes, new_bytes = encode(old), encode(new)
assert original.count(old_bytes) == 1 and new_bytes not in original
candidate = original.replace(old_bytes, new_bytes, 1)
assert candidate.replace(new_bytes, old_bytes, 1) == original
assert path.read_bytes() == original and (ROOT / 'S6_SERIES_PUBLISH_III.tex').read_bytes() == source
path.write_bytes(candidate)
assert path.read_bytes() == candidate
updated = list(csv.DictReader(io.StringIO(candidate.decode(), newline=''), delimiter='\t'))
assert [r for r in updated if r['paper'] != 'III'] == [r for r in rows if r['paper'] != 'III']
print('Reopened D23 / series:III:main-theorems at', stamp)
print('Actual Paper III statuses:', dict(Counter(r['status'] for r in updated if r['paper'] == 'III')))
print('Only the exact existing unit row changed. Source, mathematical events and counts remain unchanged.')
