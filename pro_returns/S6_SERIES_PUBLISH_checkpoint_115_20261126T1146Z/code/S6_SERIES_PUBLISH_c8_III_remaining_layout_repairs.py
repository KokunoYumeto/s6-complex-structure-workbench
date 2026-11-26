"""Apply reviewed pass03 width, bookmark and fraction-presentation repairs."""
from datetime import datetime, timezone
import argparse
import re
import S6_SERIES_PUBLISH_c8_integrate_units as u
import S6_SERIES_PUBLISH_c8_root_units as r
from S6_SERIES_PUBLISH_c8_III_check_counts import parse_statements
from S6_SERIES_PUBLISH_c8_tex_layout_proposals import REPAIRS, verify_repair

TITLES = [
    ('The $IV^*+III+I_1$ profile', '$IV^*+III+I_1$', 'IV*+III+I1'),
    ('The $III^*+3I_1$ profile', '$III^*+3I_1$', 'III*+3I1'),
    ("Wang's primitive $I_2$ filling", '$I_2$', 'I2'),
    ('The $III^*+II+I_1$ profile', '$III^*+II+I_1$', 'III*+II+I1'),
    ('A component-supported zero on the $IV^*+II+I_2$ profile', '$IV^*+II+I_2$', 'IV*+II+I2'),
    (r'Logarithmic families with smooth type $S^2\times S^4$', r'$S^2\times S^4$', 'S2 x S4'),
    ('The $I_3^*$ homology obstruction', '$I_3^*$', 'I3*'),
    ('The $I_1^*$ integral obstruction', '$I_1^*$', 'I1*'),
]

def unit_for(source, position, progress):
    headings = list(re.finditer(r'(?m)^\\(?:section|subsection)\{', source))
    index = max(i for i, heading in enumerate(headings) if heading.start() <= position)
    left = headings[index].start()
    right = headings[index + 1].start() if index + 1 < len(headings) else len(source)
    labels = set(re.findall(r'\\label\{([^{}]+)\}', source[left:right]))
    rows = [row for row in progress if row['paper'] == 'III'
            and row['defect_type'] == 'D23' and row['unit_id'] in labels]
    assert len(rows) == 1, (position, [(row['unit_id'], row['unit_title']) for row in rows])
    return rows[0]

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--apply', action='store_true')
    args = parser.parse_args()
    source = u.repairs.SOURCE.read_text(encoding='utf-8')
    owners, _, _ = parse_statements(source)
    df, ds = r.table(r.DEFECTS)
    ef, es = r.table(u.ROOT / 'CHECK_EVENTS.tsv')
    pf, ps = r.table(u.ROOT / 'S6_SERIES_PUBLISH_unit_progress.tsv')
    fragments = {path: path.read_text(encoding='utf-8') for path in u.WORK.rglob('*.tex')}
    edits = []
    for repair in REPAIRS:
        verify_repair(repair)
        assert source.count(repair['old']) == 1
        position = source.index(repair['old'])
        owner = [row for row in owners if row.start <= position < row.stop]
        assert len(owner) == 1 and owner[0].statement_id == repair['owner']
        edits.append((repair['name'], repair['old'], repair['new'], repair['owner'],
                      f"Actual pass03 {repair['width_pt']}pt at {repair['pass03_line']}. " + repair['reason'], position))
    for number, (title, math, plain) in enumerate(TITLES, 1):
        old = '\\subsection{' + title + '}'
        wrapper = '\\texorpdfstring{' + math + '}{' + plain + '}'
        new = old.replace(math, wrapper, 1)
        assert source.count(old) == 1 and new.replace(wrapper, math, 1) == old
        position = source.index(old)
        row = unit_for(source, position, ps)
        edits.append((f'bookmark-{number:02d}', old, new, row['unit_id'],
                      'Actual hyperref warning removed mathematical tokens from this bookmark. The first texorpdfstring argument is the complete unchanged printed math; the second is its explicit plain bookmark spelling. Removing this exact wrapper recovers the old heading.', position))
    needle = r'{b\over2}'
    assert source.count(needle) == 1
    position = source.index(needle)
    start = source.rfind(r'\begin{equation}', 0, position)
    stop = source.index(r'\end{equation}', position) + len(r'\end{equation}')
    old = source[start:stop]
    assert r'\label{maps:eq:MP_local_44}' in old
    new = old.replace(needle, r'\frac{b}{2}', 1)
    edits.append(('fraction-MP44', old, new, 'maps:src:D.2.38',
                  'Actual amsmath foreign-command warning. The grouped primitive fraction has numerator b and denominator2; frac has those same two arguments. Replacing the exact frac command by the recorded grouped primitive recovers the old equation. Root read the whole character formula and surrounding slope/fan comparison.', start))
    candidate = source
    updated = dict(fragments)
    prepared = []
    for name, old, new, sid, reason, position in edits:
        paths = [path for path, text in fragments.items() if old in text]
        assert len(paths) == 1 and fragments[paths[0]].count(old) == 1, name
        unit = unit_for(source, position, ps)
        candidate = candidate.replace(old, new, 1)
        updated[paths[0]] = updated[paths[0]].replace(old, new, 1)
        prepared.append((name, old, new, sid, reason, unit))
        print('REPAIR', name, 'OWNER', sid, 'UNIT', unit['unit_id'], 'FRAGMENT', paths[0])
        print('EXACT_OLD\n' + old + '\nEXACT_NEW\n' + new)
    assert len(prepared) == 18
    u.check_permanent_identifiers(source, candidate, set(), set())
    if not args.apply:
        print('INSPECTION_ONLY; 18 EXACT_GUARDS; NO_WRITES')
        return
    now = datetime.now(timezone.utc).isoformat()
    reopened = set()
    for name, old, new, sid, reason, unit in prepared:
        ident = 'III-C8-TEX-REMAINING-P03-' + name
        assert not any(row['change_id'] == ident for row in ds)
        ds.append(dict(change_id=ident, type='D23', statement_id=sid,
            old_location='actual pass03 warning and exact guarded source', old_page='incomplete pass03; no final PDF',
            new_location='same display, inline list or printed title', new_page='pending successful converged build and rendered reading',
            old_text=old, new_text=new, reason=reason,
            review_status='root complete exact old/new reading ' + now + '; runtime full-context/log reading attributed in its build note; successor build and PDF remain open'))
        unit.update(status='open', date_utc=now,
                    evidence='code/S6_SERIES_PUBLISH_c8_tex_final_build_notes.md; code/S6_SERIES_PUBLISH_c8_III_remaining_layout_repairs.py',
                    detail='Actual pass03 warning repaired with exact expression/identity preservation; successful compilation and current PDF/bookmark review remain open.')
        reopened.add(unit['unit_id'])
    eid = 'publish:c8:III:tex-pass03-remaining-layout'
    assert not any(row['event_id'] == eid for row in es)
    event = {key: '' for key in ef}
    event.update(statement_id='III:layout-pass03-remaining', date='2026-11-25',
        who='GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; numerical effort not separately exposed; continuation eight root and tex_runtime reviewer',
        type='used and rechecked in this run',
        outcome='Runtime reviewer read complete pass03 log/stdout/empty stderr and all nine assigned width contexts with their owners. Root read complete proposal code, actual old/new output and empty stderr, all eight actual titles, and the full primitive-fraction formula with surrounding context. Accepted18 layout-only repairs preserve mathematical expressions, scopes and all literal IDs. Printed title math is unchanged by explicit bookmark alternatives. No proof, independent, required-check, final build or visual-page credit is inferred.',
        event_id=eid, phase='continuation8 actual TeX repairs',
        source_file='code/S6_SERIES_PUBLISH_c8_III_remaining_layout_repairs.py',
        source_event_type='used and rechecked in this run', evidence_group=eid, date_utc=now,
        where='code/S6_SERIES_PUBLISH_c8_tex_layout_proposals.out; code/S6_SERIES_PUBLISH_c8_tex_III_final_pass03.log')
    es.append(event)
    for path, content in updated.items():
        if content != fragments[path]:
            path.write_text(content, encoding='utf-8', newline='\n')
    u.repairs.SOURCE.write_text(candidate, encoding='utf-8', newline='\n')
    r.write_table(r.DEFECTS, df, ds)
    r.write_table(u.ROOT / 'CHECK_EVENTS.tsv', ef, es)
    r.write_table(u.ROOT / 'S6_SERIES_PUBLISH_unit_progress.tsv', pf, ps)
    print('APPLIED_UTC', now, 'EXACT_EDITS', len(prepared), 'AFFECTED_UNITS', len(reopened))

if __name__ == '__main__':
    main()
