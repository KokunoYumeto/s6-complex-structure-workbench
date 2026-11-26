"""Admit the final main-C map and domain corrections after full comparison."""
from S6_SERIES_PUBLISH_c4_edit import *
from S6_SERIES_PUBLISH_c4_admit import protected_statement
import csv

csv.field_size_limit(10000000)
prefix = ROOT / 'agents/continuation4_horizontal/S6_SERIES_PUBLISH_main_C'
_, guards = read_tsv(str(prefix) + '_guards.tsv')
_, defects = read_tsv(str(prefix) + '_defects.tsv')
_, events = read_tsv(str(prefix) + '_CHECK_EVENTS.tsv')
_, proposals = read_tsv(str(prefix) + '_unit_proposals.tsv')
assert len(guards) == len(defects) == 5 and len(events) == 15
before = SOURCE.read_text()
after = before
for guard in guards:
    assert after.count(guard['old_text']) == 1, guard['change_id']
    after = after.replace(guard['old_text'], guard['new_text'], 1)
assert identifiers(before) == identifiers(after)
for label in ('push:src:E.5.2', 'push:src:E.5.3'):
    assert protected_statement(before, label) == protected_statement(after, label)
for row in defects:
    row['review_status'] = 'Complete main-C, G1, outline and exact application comparison by horizontal reader; root read the complete comparison, receiving main C and G1 map additions, P4.6 and D2.2/D2.4, after the complete G1 and horizontal proofs. Admitted with all identifiers and protected statements unchanged.'
for filename, rows, identity in (('S6_SERIES_PUBLISH_defects_II.tsv', defects, 'change_id'), ('CHECK_EVENTS.tsv', events, 'event_id')):
    _, oldrows = read_tsv(ROOT / filename)
    oldkeys = {r[identity] for r in oldrows}
    assert len({r[identity] for r in rows}) == len(rows)
    assert not oldkeys.intersection(r[identity] for r in rows)
fields, units = read_tsv(ROOT / 'S6_SERIES_PUBLISH_unit_progress.tsv')
closures = 0
for proposal in proposals:
    # Other outline clauses have their own complete step-to-owner review.
    # Its first-part rows remain open until that review is admitted.
    if proposal['unit_id'] != 'sec:II:all:12':
        continue
    matches = [r for r in units if r['paper'] == 'II' and r['unit_id'] == proposal['unit_id'] and r['defect_type'] == 'D24']
    assert len(matches) == 1
    row = matches[0]
    if row['status'] != 'done':
        closures += 1
    row['status'] = 'done'
    row['date_utc'] = now()
    row['evidence'] = 'agents/continuation4_horizontal/S6_SERIES_PUBLISH_main_C_comparison.md; complete G1 and D2.2/D2.4 comparison'
    row['detail'] = 'The entire final sign/equality section was compared with main C and its six outline steps. The reduction inclusion, normalization composite and scheme conductor are explicit. Whole-front-unit and final-PDF gates remain separate.'
SOURCE.write_text(after, newline='\n')
print('Exact substitutions:', len(guards))
print('Defect rows:', append_rows(ROOT / 'S6_SERIES_PUBLISH_defects_II.tsv', defects, 'change_id'))
print('Actual comparison events:', append_rows(ROOT / 'CHECK_EVENTS.tsv', events, 'event_id'))
write_tsv(ROOT / 'S6_SERIES_PUBLISH_unit_progress.tsv', fields, units)
print('Existing final-body D24 row closed:', closures)
print('Whole main-theorem and outline rows remain open pending complete outline comparison.')
print('Identifiers and protected E.5.2/E.5.3 statements preserved exactly.')
