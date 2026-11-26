"""Display exact staged/source defect differences for human-readable root review.

No artifact, census or derived-file diff is saved by this read-only helper.
"""
import argparse
import csv
import difflib
import json
from pathlib import Path

csv.field_size_limit(100000000)
p = argparse.ArgumentParser()
p.add_argument('path', type=Path)
p.add_argument('--prefix', default='')
p.add_argument('--first', type=int, default=1)
p.add_argument('--last', type=int)
a = p.parse_args()
if a.path.suffix == '.json':
    rows = json.loads(a.path.read_text())
else:
    with a.path.open(newline='') as stream:
        rows = list(csv.DictReader(stream, delimiter='\t'))
rows = [r for r in rows if r.get('change_id', '').startswith(a.prefix)]
for index, row in enumerate(rows, 1):
    if index < a.first or (a.last is not None and index > a.last):
        continue
    print('\nROW', index, row.get('change_id'), row.get('statement_id'))
    print('REASON:', row.get('reason', row.get('interpretation', '')))
    old = row.get('old', row.get('old_text', row.get('old_value', row.get('old_row', ''))))
    new = row.get('new', row.get('new_text', row.get('new_value', row.get('new_row', ''))))
    if not isinstance(old, str):
        old = json.dumps(old, ensure_ascii=False, indent=2) + '\n'
    if not isinstance(new, str):
        new = json.dumps(new, ensure_ascii=False, indent=2) + '\n'
    print(''.join(difflib.unified_diff(old.splitlines(True), new.splitlines(True), n=2)))
