"""Admit the reviewed explicit 02KU mathematical computation method."""
from pathlib import Path
from collections import Counter
from datetime import datetime, timezone
import csv
import re

ROOT = Path(__file__).resolve().parents[1]
csv.field_size_limit(100000000)

def read_table(path):
    with path.open(newline='') as stream:
        reader = csv.DictReader(stream, delimiter='\t')
        return reader.fieldnames, list(reader)

def write_table(path, fields, rows):
    with path.open('w', newline='') as stream:
        writer = csv.DictWriter(stream, fields, delimiter='\t', lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)

folder = ROOT / 'agents/continuation9_findings'
batches = [('P14', 12, 1)]
source = ROOT / 'S6_SERIES_PUBLISH_III.tex'
before = source.read_text()
after = before
edits, added_events = [], []
for name, expected_edits, expected_events in batches:
    _, rows = read_table(folder / f'S6_SERIES_PUBLISH_c9_{name}_defects.tsv')
    _, events = read_table(folder / f'S6_SERIES_PUBLISH_c9_{name}_CHECK_EVENTS.tsv')
    assert len(rows) == expected_edits
    assert len(events) == expected_events
    for row in rows:
        assert after.count(row['old_text']) == 1, row['change_id']
        after = after.replace(row['old_text'], row['new_text'], 1)
    edits.extend(rows)
    added_events.extend(events)
inverse = after
for row in reversed(edits):
    assert inverse.count(row['new_text']) == 1, row['change_id']
    inverse = inverse.replace(row['new_text'], row['old_text'], 1)
assert inverse == before
identifiers = lambda s: Counter(re.findall(r'\\(?:label|hypertarget)\{[^{}]*\}', s))
assert identifiers(before) == identifiers(after)
df, defects = read_table(ROOT / 'S6_SERIES_PUBLISH_defects_III.tsv')
ef, events = read_table(ROOT / 'CHECK_EVENTS.tsv')
assert not {r['change_id'] for r in defects} & {r['change_id'] for r in edits}
assert not {r['event_id'] for r in events} & {r['event_id'] for r in added_events}
assert all(r['type'] == 'used and rechecked in this run' for r in added_events)
now = datetime.now(timezone.utc).isoformat()
for row in edits:
    row['review_status'] += (' Root read the exact differences and scoped reasons, '
        'including the explicit cone, Smith coordinate maps and peripheral presentation, and admitted them at ' + now +
        '; final rendered-page review remains open.')
source.write_text(after, newline='\n')
write_table(ROOT / 'S6_SERIES_PUBLISH_defects_III.tsv', df, defects + edits)
write_table(ROOT / 'CHECK_EVENTS.tsv', ef, events + added_events)
print('Admitted twelve P14 edits: marked-model interpretation, exact algebraic method, program scope and primary-source consultation locator.')
print('Admitted one scoped used-and-rechecked event; no independent-check credit.')
print('Exact reverse substitutions reconstruct the pre-edit source; all labels and targets preserved.')
print('Paper III final PDF and whole-unit gates remain open.')
