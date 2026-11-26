"""Admit precise source loci and justified printed-bibliography omissions."""
from S6_SERIES_PUBLISH_c4_edit import *
from S6_SERIES_PUBLISH_c4_admit import protected_statement
import json
import csv
import re

csv.field_size_limit(10000000)
prefix = ROOT / 'agents/continuation4_reductions/S6_SERIES_PUBLISH_c4_bibliography'
guards = json.loads(Path(str(prefix) + '_guards.json').read_text())
_, proposed_defects = read_tsv(str(prefix) + '_defects.tsv')
_, events = read_tsv(str(prefix) + '_CHECK_EVENTS.tsv')
assert len(guards) == len(proposed_defects) == 9 and len(events) == 3
defects = []
for guard, item in zip(guards, proposed_defects):
    assert item['old_text'] in guard['old']
    assert item['new_text'] in guard['new']
    defects.append(dict(change_id='II-C4-' + guard['key'], type=item['defect_type'],
        statement_id=item['unit_id'], old_location=item['unit_id'],
        old_page='current working source; final concordance pending',
        new_location=item['unit_id'], new_page='final integrated build pending',
        old_text=item['old_text'], new_text=item['new_text'], reason=item['reason']))
before = SOURCE.read_text()
after = before
for guard in guards:
    assert after.count(guard['old']) == 1, guard['key']
    after = after.replace(guard['old'], guard['new'], 1)
assert identifiers(before) == identifiers(after)
for label in ('push:src:E.5.2', 'push:src:E.5.3'):
    assert protected_statement(before, label) == protected_statement(after, label)
assert len(re.findall(r'\\bibitem(?:\[[\s\S]*?\])?\{', after)) == 125
for row in defects:
    row['review_status'] = ('Root read the complete bibliography coverage note, exact omission entries, '
        'both bounded old/new citation comparisons, all three event scopes and both primary-locus records. '
        'No mathematical statement, proof step, identifier or program entry changes; shared bibliography '
        'and historical records are retained. Global D18 and final-page gates remain separate.')
for filename, rows, identity in (('S6_SERIES_PUBLISH_defects_II.tsv', defects, 'change_id'), ('CHECK_EVENTS.tsv', events, 'event_id')):
    _, oldrows = read_tsv(ROOT / filename)
    assert len({r[identity] for r in rows}) == len(rows)
    assert not {r[identity] for r in oldrows}.intersection(r[identity] for r in rows)
SOURCE.write_text(after, newline='\n')
print('Exact bounded substitutions:',len(guards))
print('Defect rows:',append_rows(ROOT / 'S6_SERIES_PUBLISH_defects_II.tsv',defects,'change_id'))
print('Bounded source/application events:',append_rows(ROOT / 'CHECK_EVENTS.tsv',events,'event_id'))
print('Printed bibliography: 125 entries. Shared bibliography and histories retained.')
print('No global D18, independent-check, required-check or rendered-page credit.')
