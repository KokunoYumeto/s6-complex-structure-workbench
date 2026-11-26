"""Admit the fully compared outlines and final source-placement proposals."""
from S6_SERIES_PUBLISH_c4_edit import *
from S6_SERIES_PUBLISH_c4_admit import protected_statement
import csv
import re

csv.field_size_limit(10000000)
prefix = ROOT / 'agents/continuation4_horizontal/S6_SERIES_PUBLISH_outline'
_, guards = read_tsv(str(prefix) + '_guards.tsv')
_, defects = read_tsv(str(prefix) + '_defects.tsv')
_, events = read_tsv(str(prefix) + '_CHECK_EVENTS.tsv')
assert len(guards) == len(defects) == 6 and len(events) == 46
before = SOURCE.read_text()
after = before
for guard in guards:
    assert after.count(guard['old_text']) == 1, guard['change_id']
    after = after.replace(guard['old_text'], guard['new_text'], 1)
old_title = r'\subsection{Compact insertion of elliptic stars}\label{subsec:II:compact-elliptic-star-insertion}'
new_title = r'\subsection{Elliptic pruning and compact restoration}\label{subsec:II:compact-elliptic-star-insertion}'
assert after.count(old_title) == 1
after = after.replace(old_title, new_title, 1)
assert identifiers(before) == identifiers(after)
for label in ('push:src:E.5.2', 'push:src:E.5.3'):
    assert protected_statement(before, label) == protected_statement(after, label)
main_pattern = r'\\begin\{maintheorem\}[\s\S]*?\\end\{maintheorem\}'
assert re.findall(main_pattern, before) == re.findall(main_pattern, after)
assert len(re.findall(main_pattern, after)) == 7
for row in defects:
    row['review_status'] = ('Complete old/new outline and full supplying-owner comparisons by horizontal reader; '
        'root read the full comparison, all six exact substitutions, the complete receiving A-G outlines '
        'and reader routes, after its complete main A-G comparisons. Admitted; all main statements unchanged.')
defects.append(dict(change_id='II-C4-PLACEMENT-TITLE-01', type='D14',
    statement_id='subsec:II:compact-elliptic-star-insertion',
    old_location='Part V, elliptic pruning/restoration subsection',
    old_page='checkpoint44 and current working source; final concordance pending',
    new_location='Part V, elliptic pruning/restoration subsection',
    new_page='final integrated build pending', old_text=old_title, new_text=new_title,
    reason='The full one-/two-mark torsor, pruning, period, weighted insertion, finite-action and tree-restoration owners P370-P375/P353 are already in this subsection; its descriptive title must name that established general scope.',
    review_status='Conductor read all current part/section/subsection boundaries and their receiving owners; root read the complete placement comparison and previously read every affected complete owner. Only the title changes.'))
for filename, rows, identity in (('S6_SERIES_PUBLISH_defects_II.tsv', defects, 'change_id'), ('CHECK_EVENTS.tsv', events, 'event_id')):
    _, oldrows = read_tsv(ROOT / filename)
    assert len({r[identity] for r in rows}) == len(rows)
    assert not {r[identity] for r in oldrows}.intersection(r[identity] for r in rows)
fields, units = read_tsv(ROOT / 'S6_SERIES_PUBLISH_unit_progress.tsv')
index = {(r['paper'], r['unit_id'], r['defect_type']): r for r in units}
assert len(index) == len(units)
_, proposals = read_tsv(ROOT / 'agents/continuation4_conductor/S6_SERIES_PUBLISH_c4_conductor_placement_unit_status.tsv')
assert len(proposals) == 446
closures = 0
for proposal in proposals:
    key = (proposal['paper'], proposal['unit_id'], proposal['defect_type'])
    assert key in index and key[0] == 'II' and key[2] in ('D14', '')
    assert (proposal['row_kind'], key[2]) in (('defect', 'D14'), ('structure', ''))
    assert index[('II', key[1], 'D12')]['status'] == 'done', key
    row = index[key]
    assert row['status'] == 'open', key
    row.update(status='done', date_utc=now(), evidence=proposal['evidence'], detail=proposal['detail'])
    closures += 1
for unit in ('subsec:II:compact-elliptic-star-insertion', 'sec:II:10'):
    row = index[('II', unit, 'D14')]
    assert row['status'] == 'open'
    assert index[('II', unit, 'D12')]['status'] == 'done'
    row.update(status='done', date_utc=now(),
        evidence='agents/continuation4_conductor/S6_SERIES_PUBLISH_c4_conductor_placement_comparison.md; II-C4-PLACEMENT-TITLE-01',
        detail='Complete distributed ownership and final placement assessed; admitted title names the actual general elliptic pruning and compact restoration. No mathematical statement or proof changed.')
    closures += 1
for unit in ('series:II:main-theorems', 'series:II:outline', 'how-the-paper-is-organized'):
    row = index[('II', unit, 'D24')]
    assert row['status'] == 'open'
    row.update(status='done', date_utc=now(),
        evidence='S6_SERIES_PUBLISH_c4_global_comparison.md; agents/continuation4_horizontal/S6_SERIES_PUBLISH_main_C_comparison.md; agents/continuation4_horizontal/S6_SERIES_PUBLISH_outline_comparison.md; CHECK_EVENTS.tsv: publish:c4:outline:001-046',
        detail='Complete A-G main-statement, full owner and outline-step comparisons admitted; root read the complete receiving outlines, abstract/routes comparison and exact route changes. Every stated scope and map agrees with its supplying proof. Rendered-page and methodology gates remain separate.')
    closures += 1
SOURCE.write_text(after, newline='\n')
print('Exact substitutions:', len(guards) + 1)
print('Defect rows:', append_rows(ROOT / 'S6_SERIES_PUBLISH_defects_II.tsv', defects, 'change_id'))
print('Actual exposed reading/comparison events:', append_rows(ROOT / 'CHECK_EVENTS.tsv', events, 'event_id'))
write_tsv(ROOT / 'S6_SERIES_PUBLISH_unit_progress.tsv', fields, units)
print('Existing source-placement and front D24 rows closed:', closures)
print('Main A-G and protected E.5.2/E.5.3 statements preserved exactly.')
print('No independent-check, new required-check, final-build or final-page credit.')
