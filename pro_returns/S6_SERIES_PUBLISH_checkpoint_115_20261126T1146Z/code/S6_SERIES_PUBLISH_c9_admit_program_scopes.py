"""Relocate five exact computational comparison scopes into the Programs table."""
from pathlib import Path
from collections import Counter
from datetime import datetime, timezone
import csv
import json
import re

ROOT = Path(__file__).resolve().parents[1]
csv.field_size_limit(100000000)
folder = ROOT / 'agents/continuation9_global_sweep'
edits = json.loads((folder / 'S6_SERIES_PUBLISH_c9_program_scope_proposals.json').read_text())
assert len(edits) == 5
source = ROOT / 'S6_SERIES_PUBLISH_III.tex'
before = source.read_text()
after = before
for edit in edits:
    assert after.count(edit['old']) == 1, edit['change_id']
    after = after.replace(edit['old'], edit['new'], 1)
inverse = after
for edit in reversed(edits):
    assert inverse.count(edit['new']) == 1, edit['change_id']
    inverse = inverse.replace(edit['new'], edit['old'], 1)
assert inverse == before
identifiers = lambda s: Counter(re.findall(r'\\(?:label|hypertarget)\{[^{}]*\}', s))
assert identifiers(before) == identifiers(after)
path = ROOT / 'S6_SERIES_PUBLISH_defects_III.tsv'
with path.open(newline='') as stream:
    reader = csv.DictReader(stream, delimiter='\t')
    fields, rows = reader.fieldnames, list(reader)
with (folder / 'S6_SERIES_PUBLISH_c9_program_scope_defects.tsv').open(newline='') as stream:
    additions = list(csv.DictReader(stream, delimiter='\t'))
assert {r['change_id'] for r in additions} == {e['change_id'] for e in edits}
assert not {r['change_id'] for r in rows} & {r['change_id'] for r in additions}
now = datetime.now(timezone.utc).isoformat()
for row in additions:
    row['review_status'] += ' Root read all five exact scopes and their retained count meanings; admitted at ' + now + '; final Programs-table page reading pending.'
source.write_text(after, newline='\n')
with path.open('w', newline='') as stream:
    writer = csv.DictWriter(stream, fields, delimiter='\t', lineterminator='\n')
    writer.writeheader()
    writer.writerows(rows + additions)
print('Admitted five Programs-table scope relocations with their exact old/new records.')
print('Inverse substitutions recover the source; all labels and targets preserved.')
print('No check event or new mathematical/visual completion credit added.')
