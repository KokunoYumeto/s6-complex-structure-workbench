"""Admit a root-reviewed exact defect packet and its scoped check events.

The mandatory --reviewed argument records root's actual completed review.
No derived count, manifest, census or seal is produced.
"""
from pathlib import Path
from collections import Counter
from datetime import datetime, timezone
import argparse
import csv
import re

ROOT = Path(__file__).resolve().parents[1]
csv.field_size_limit(100000000)
p = argparse.ArgumentParser()
p.add_argument('--defects', required=True, type=Path)
p.add_argument('--events', required=True, type=Path)
p.add_argument('--edits', required=True, type=int)
p.add_argument('--event-count', required=True, type=int)
p.add_argument('--reviewed', required=True)
a = p.parse_args()

def read_table(path):
    with path.open(newline='') as stream:
        r = csv.DictReader(stream, delimiter='\t')
        return r.fieldnames, list(r)

def write_table(path, fields, rows):
    with path.open('w', newline='') as stream:
        w = csv.DictWriter(stream, fields, delimiter='\t', lineterminator='\n')
        w.writeheader()
        w.writerows(rows)

df, defects = read_table(ROOT / 'S6_SERIES_PUBLISH_defects_III.tsv')
ef, events = read_table(ROOT / 'CHECK_EVENTS.tsv')
ndf, new_defects = read_table(a.defects)
nef, new_events = read_table(a.events)
assert ndf == df and nef == ef
assert len(new_defects) == a.edits and len(new_events) == a.event_count
assert not {r['change_id'] for r in defects} & {r['change_id'] for r in new_defects}
assert not {r['event_id'] for r in events} & {r['event_id'] for r in new_events}
assert len({r['change_id'] for r in new_defects}) == len(new_defects)
assert len({r['event_id'] for r in new_events}) == len(new_events)
assert all(r['type'] == 'used and rechecked in this run' for r in new_events)
assert all(r['source_event_type'] == 'used and rechecked in this run' for r in new_events)
source = ROOT / 'S6_SERIES_PUBLISH_III.tex'
before = source.read_text()
after = before
for row in new_defects:
    old, new = row['old_text'], row['new_text']
    assert old != new and after.count(old) == 1, row['change_id']
    after = after.replace(old, new, 1)
inverse = after
for row in reversed(new_defects):
    old, new = row['old_text'], row['new_text']
    assert inverse.count(new) == 1, row['change_id']
    inverse = inverse.replace(new, old, 1)
assert inverse == before
ids = lambda s: Counter(re.findall(r'\\(?:label|hypertarget)\{[^{}]*\}', s))
assert ids(before) == ids(after)
forms = lambda s: Counter(re.findall(r'\\(?:begin|end)\{(?:proof|theorem|proposition|lemma|corollary|definition|remark|example)\}', s))
assert forms(before) == forms(after)
fields = lambda s: Counter((a or b).strip() for a, b in re.findall(r'\\mathbb\s*(?:\{([^{}]+)\}|([A-Za-z]))', s))
assert fields(before) == fields(after), 'Blackboard field/group tokens changed'
now = datetime.now(timezone.utc).isoformat()
for row in new_defects:
    row['review_status'] += ' Root admission ' + now + ': ' + a.reviewed + ' Exact reverse substitutions and permanent-target multiplicities checked. Final page review remains.'
for row in new_events:
    row['outcome'] += ' Source packet admitted by root at ' + now + '; the exposed scope and event type are unchanged.'
source.write_text(after, newline='\n')
write_table(ROOT / 'S6_SERIES_PUBLISH_defects_III.tsv', df, defects + new_defects)
write_table(ROOT / 'CHECK_EVENTS.tsv', ef, events + new_events)
print('Packet:', a.defects)
print('Root review:', a.reviewed)
print('Admitted', len(new_defects), 'exact source rows and', len(new_events), 'scoped used-and-rechecked events.')
print('Exact reverse source recovery, formal-environment counts and permanent targets verified.')
