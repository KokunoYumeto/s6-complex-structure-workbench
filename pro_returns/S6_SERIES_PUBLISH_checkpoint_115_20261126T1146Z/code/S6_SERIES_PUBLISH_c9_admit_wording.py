"""Apply the 49 individually reviewed wording edits and their scoped records."""
from pathlib import Path
from collections import Counter
from datetime import datetime, timezone
import csv
import json
import re

ROOT = Path(__file__).resolve().parents[1]
csv.field_size_limit(100000000)

def read_table(p):
    with p.open(newline='') as f:
        r = csv.DictReader(f, delimiter='\t')
        rows = list(r)
        return r.fieldnames, rows

def write_table(p, fields, rows):
    with p.open('w', newline='') as f:
        w = csv.DictWriter(f, fields, delimiter='\t', lineterminator='\n')
        w.writeheader(); w.writerows(rows)

folder = ROOT / 'agents/continuation9_global_sweep'
edits = json.loads((folder / 'S6_SERIES_PUBLISH_c9_wording_proposals.json').read_text())
source = ROOT / 'S6_SERIES_PUBLISH_III.tex'
before = source.read_text()
after = before
assert len(edits) == 49
for e in edits:
    assert after.count(e['old']) == 1, e['change_id']
    after = after.replace(e['old'], e['new'], 1)
inverse = after
for e in reversed(edits):
    assert inverse.count(e['new']) == 1, e['change_id']
    inverse = inverse.replace(e['new'], e['old'], 1)
assert inverse == before
identity = lambda s: Counter(re.findall(r'\\(?:label|hypertarget)\{[^{}]*\}', s))
assert identity(before) == identity(after)
df, defects = read_table(ROOT / 'S6_SERIES_PUBLISH_defects_III.tsv')
ef, events = read_table(ROOT / 'CHECK_EVENTS.tsv')
_, new_defects = read_table(folder / 'S6_SERIES_PUBLISH_c9_wording_defects.tsv')
_, new_events = read_table(folder / 'S6_SERIES_PUBLISH_c9_wording_events.tsv')
assert {x['change_id'] for x in new_defects} == {x['change_id'] for x in edits}
assert not {x['change_id'] for x in new_defects} & {x['change_id'] for x in defects}
assert not {x['event_id'] for x in new_events} & {x['event_id'] for x in events}
assert all(x['type'] == 'used and rechecked in this run' for x in new_events)
now = datetime.now(timezone.utc).isoformat()
for x in new_defects:
    x['review_status'] += ' Root reviewed every exact difference and interpretation, including the revised sphere wording, and admitted the guarded source edit at ' + now + '; final rendered-page review remains open.'
source.write_text(after, newline='\n')
write_table(ROOT / 'S6_SERIES_PUBLISH_defects_III.tsv', df, defects + new_defects)
write_table(ROOT / 'CHECK_EVENTS.tsv', ef, events + new_events)
print('Admitted', len(edits), 'wording edits and', len(new_events), 'scoped used-and-rechecked events.')
print('Exact reverse substitutions reconstruct the pre-edit source; label/target multiplicities preserved.')
print('The weighted-computation remark was also read against its explicit Mayer-Vietoris proof tail by root.')
print('No independent-check, required-check, final-page or whole-unit completion credit.')
