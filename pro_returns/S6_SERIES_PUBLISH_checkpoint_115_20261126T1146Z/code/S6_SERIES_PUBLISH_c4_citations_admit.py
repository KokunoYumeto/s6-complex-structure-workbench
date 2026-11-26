"""Admit bounded exact-edition citation changes, with honest reading scope."""
from S6_SERIES_PUBLISH_c4_edit import *
from S6_SERIES_PUBLISH_c4_admit import protected_statement
import csv
import json

csv.field_size_limit(10000000)
prefix = ROOT / 'agents/continuation4_reductions/S6_SERIES_PUBLISH_c4_citations'
guards = json.loads(Path(str(prefix) + '_guards.json').read_text())
_, compact = read_tsv(str(prefix) + '_defects.tsv')
_, events = read_tsv(str(prefix) + '_CHECK_EVENTS.tsv')
assert (len(guards), len(compact), len(events)) == (8, 34, 8)
def mathematics(text):
    text = re.sub(r'\\cite[a-zA-Z]*\*?(?:\[[^\]]*\]){0,2}\{[^}]*\}', '', text)
    return re.sub(r'\s+', '', text)
before = SOURCE.read_text()
after = before
for guard in guards:
    assert after.count(guard['old']) == 1, guard['key']
    assert mathematics(guard['old']) == mathematics(guard['new']), guard['key']
    after = after.replace(guard['old'], guard['new'], 1)
assert identifiers(before) == identifiers(after)
for label in ('push:src:E.5.2', 'push:src:E.5.3'):
    assert protected_statement(before, label) == protected_statement(after, label)
defects = []
for n, row in enumerate(compact, 1):
    defects.append(dict(change_id=f'II-C4-CITATION-{n:03d}', type='D18',
        statement_id=row['unit_id'], old_location=row['unit_id'],
        old_page='current working source; final page concordance pending',
        new_location=row['unit_id'], new_page='final integrated build pending',
        old_text=row['old_text'], new_text=row['new_text'], reason=row['reason'],
        review_status='Bounded primary-page/application comparison by reductions reader; root read the source-scope notes and every exact citation diff. Noncitation mathematics, identifiers and protected statements verified unchanged. No new complete-proof or independent credit.'))
for row in events:
    row['evidence_group'] = row['event_id']
    row['source_event_type'] = row['type']
    row['source_file'] = str(prefix.relative_to(ROOT)) + '_comparison.md'
for filename, rows, identity in (('S6_SERIES_PUBLISH_defects_II.tsv', defects, 'change_id'), ('CHECK_EVENTS.tsv', events, 'event_id')):
    _, existing = read_tsv(ROOT / filename)
    assert not {r[identity] for r in existing}.intersection(r[identity] for r in rows)
SOURCE.write_text(after, newline='\n')
print('Exact citation guards:', len(guards))
print('D18 rows:', append_rows(ROOT / 'S6_SERIES_PUBLISH_defects_II.tsv', defects, 'change_id'))
print('Bounded source/application events:', append_rows(ROOT / 'CHECK_EVENTS.tsv', events, 'event_id'))
print('All noncitation mathematics and identifiers preserved. No unit closure or complete-proof credit.')
