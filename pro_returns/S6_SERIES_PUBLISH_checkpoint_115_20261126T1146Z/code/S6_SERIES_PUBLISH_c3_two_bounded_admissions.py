from S6_SERIES_PUBLISH_c3_edit import *
import json

text = SOURCE.read_text()
original = text
con = ROOT / 'agents/continuation3_conductor'
pre = 'S6_SERIES_PUBLISH_c3_conductor_04_'
start = r'\section{Unrestricted Euler topology and component covers}'
end = r'\begin{proposition}[The same punctured torus family'
remainder06 = '\\subsection{Vertical modifications and component covers}\\label{subsec:II:vertical-modification-inputs}\n\n'
remainder07 = '\n\n\\subsection{Local numerical and conductor criteria}\\label{subsec:II:local-numerical-conductor-inputs}'
late_heading = r'\subsection{Euler numbers and monodromy signatures}'
found = ROOT / 'agents/continuation3_foundations/sec07'
normal = found / 'S6_SERIES_PUBLISH_II_sec07_normal.tex'
if r'\hypertarget{tag-P233}' not in text:
    a = text.index(start)
    b = text.index(end, a)
    parity = (con / (pre + 'replacement.tex')).read_text()
    remainder06 = '\\subsection{Vertical modifications and component covers}\\label{subsec:II:vertical-modification-inputs}\n\n'
    text = text[:a] + parity + '\n\n' + remainder06 + text[b:]
    _, repairs = read_tsv(con / (pre + 'remote_repairs.tsv'))
    for row in repairs:
        assert text.count(row['old_text']) == 1, row['statement_id']
        text = text.replace(row['old_text'], row['new_text'], 1)
    late_heading = r'\subsection{Euler numbers and monodromy signatures}'
    assert text.count(late_heading) == 1
    text = text.replace(late_heading, late_heading + r'\label{subsec:II:euler-monodromy-signatures}', 1)

    found = ROOT / 'agents/continuation3_foundations/sec07'
    normal = found / 'S6_SERIES_PUBLISH_II_sec07_normal.tex'
    guards = json.loads((found / 'S6_SERIES_PUBLISH_sec07_normal_guards.json').read_text())
    for guard in guards:
        assert text.count(guard['old']) == 1, guard['key']
        text = text.replace(guard['old'], guard['new'], 1)
    normal_text = normal.read_text().strip()
    assert text.count(normal_text) == 1
    remainder07 = '\n\n\\subsection{Local numerical and conductor criteria}\\label{subsec:II:local-numerical-conductor-inputs}'
    text = text.replace(normal_text, normal_text + remainder07, 1)
    preserve_identifiers(original, text)
    for old, new in zip(identifiers(original), identifiers(text)):
        for name, count in old.items():
            assert new[name] == count, name
    assert text.count(r'\hypertarget{tag-P233}') == 1
    SOURCE.write_text(text, newline='\n')
else:
    assert remainder06.strip() in text and remainder07.strip() in text
    print("Source stage already admitted; completing record and unit stages.")

for folder, prefix in [(con, pre), (found, 'S6_SERIES_PUBLISH_sec07_normal_')]:
    for suffix, target, key in [('defects.tsv', 'S6_SERIES_PUBLISH_defects_II.tsv', 'change_id'),
                                ('CHECK_EVENTS.tsv', 'CHECK_EVENTS.tsv', 'event_id')]:
        _, incoming = read_tsv(folder / (prefix + suffix))
        print(prefix + suffix, append_rows(ROOT / target, incoming, key))

path = ROOT / 'S6_SERIES_PUBLISH_unit_progress.tsv'
fields, rows = read_tsv(path)
renames = {
    'sec:II:06': ('subsec:II:vertical-modification-inputs', 'Vertical modifications and component covers'),
    'sec:II:07': ('subsec:II:local-numerical-conductor-inputs', 'Local numerical and conductor criteria'),
    'cdp:st:C2b': ('subsec:II:euler-monodromy-signatures', 'Euler numbers and monodromy signatures'),
}
for old, (new, title) in renames.items():
    selected = [r for r in rows if r['paper'] == 'II' and r['unit_id'] == old]
    assert len(selected) == 26, (old, len(selected))
    for row in selected:
        row.update(unit_id=new, unit_title=title,
                   detail=row['detail'] + ' Unit boundary/name migrated after the bounded extraction; this migration is not movement credit.')
rows = [r for r in rows if not (r['paper'] == 'II' and r['unit_id'] == 'night:P4R.1')]
known = {(r['paper'], r['unit_id'], r['defect_type'] or r['row_kind']) for r in rows}
for statusfile, fragment in [(con / (pre + 'unit_status.tsv'), con / (pre + 'replacement.tex')),
                             (found / 'S6_SERIES_PUBLISH_sec07_normal_unit_progress.tsv', normal)]:
    _, incoming = read_tsv(statusfile)
    for item in incoming:
        unit = item['unit']
        criterion = item.get('criterion', item.get('row'))
        if criterion == 'restructuring':
            criterion = 'structure'
        key = ('II', unit, criterion)
        assert key not in known, key
        known.add(key)
        status = item['status']
        detail = item.get('reason', item.get('basis', ''))
        if criterion in ['D14', 'structure']:
            status = 'open'
            detail += ' Final whole-paper placement remains open.'
        title = item.get('title', 'Normal irreducible supports')
        rows.append(dict(zip(fields, ['II', unit, title,
            'structure' if criterion == 'structure' else 'defect',
            '' if criterion == 'structure' else criterion, status, now(),
            str(fragment.relative_to(ROOT)), detail])))
write_tsv(path, fields, rows)

boundary_rows = []
for index, (owner, old, new, reason) in enumerate([
    ('sec:II:06', '', remainder06, 'Separates the unreviewed component-cover remainder from the fully compared parity/blowup unit; all remainder defect rows stay as they were.'),
    ('sec:II:07', '', remainder07, 'Separates the unreviewed numerical/conductor remainder from the fully compared normal-support unit; all remainder defect rows stay as they were.'),
    ('sec:II:all:08', late_heading, late_heading + r'\label{subsec:II:euler-monodromy-signatures}', 'Stable subsection identity after C2b is transferred to the earlier single construction owner; no mathematical text changes.')], 1):
    boundary_rows.append({'change_id': f'II-C3-BOUNDED-BOUNDARY-{index:02}', 'type': 'D14',
        'statement_id': owner, 'old_location': owner, 'old_page': 'source boundary',
        'new_location': owner, 'new_page': 'integrated PDF pending',
        'old_text': old, 'new_text': new, 'reason': reason,
        'review_status': 'Root read receiving boundaries; this records unit placement without claiming final whole-paper order.'})
append_rows(ROOT / 'S6_SERIES_PUBLISH_defects_II.tsv', boundary_rows, 'change_id')
add_event('lem:II:compact-analytic-tube; night:P4R.1; cdp:st:C.2.UN.1; cdp:st:C.2.UN.2; cdp:st:C2b; cdp:st:C.2.UN.5',
    'II-C3-ROOT-TWO-BOUNDED-ADMISSIONS', 'used and rechecked in this run',
    'Root read the complete old and receiving UN.1/UN.2, C2b, P4R.1, P233 and UN.5 blocks. Compared the exact round-tube homotopy, meridian inclusion map and unchanged rational abelianization, both blowup specializations and all integral cohomology formulas, and the unchanged normal-support statement and cyclic quotient maps. The Catanese primary-locus reading is credited to the foundations agent, whose exposed comparison event is imported. Every old label and tag retains its multiplicity. Remainder units retain their open rows; final placement, integrated typography and final-page reading remain open.',
    'S6_SERIES_PUBLISH_II.tex', source='code/S6_SERIES_PUBLISH_c3_two_bounded_admissions.py')
print('Admitted conductor04 and normal-support units; remainder units retained without closure credit.')
