"""Wrap the first nine fully read pass03 overflow displays at exact boundaries."""
from datetime import datetime, timezone
import re
import S6_SERIES_PUBLISH_c8_integrate_units as u
import S6_SERIES_PUBLISH_c8_root_units as r
from S6_SERIES_PUBLISH_c8_III_check_counts import parse_statements

# Each unique needle selects the complete display read with its surrounding proof.
# Each breakpoint inserts a TeX row break while retaining every old character.
SPECS = [
    (10887, '2.66841', r' a_0=(0,1),\quad a_1=(1,0),\quad',
     [r' \qquad' + '\n (e_0,e_1,e_2,e_3)=']),
    (12858, '37.15933', r'U=y+it,\quad V=y-it,\quad UV=(x-1)(2x+1)^2,',
     [r'\qquad V=\frac{(x-1)(2x+1)^2}{U}']),
    (13571, '72.90521', r'D=[T_0-I\ T_1-I\ T_2-I],\qquad',
     [r'j_0(x)=(x,0,0)', r'j_2(x)=(0,0,x)']),
    (14119, '3.4316', r' [t^j](F^3-27H^2)=0\quad(13-N\leq j\leq12),\qquad',
     [r' (F^3-27H^2)^{(j)}(b)=0', r' f_4=f_4(0).']),
    (18680, '20.702', r' D_0C=I_3,\quad D_\Gamma K=0,\quad LK=I_9,\quad',
     [r' KL(I-CD_0)=I-CD_0', r' Lj_0\delta=(-1,0,-1,0,0,-1,0,0,0)^t.']),
    (18973, '49.8181', r' A_0=\begin{pmatrix}3&7\\-1&-2\end{pmatrix},\quad g_0=(-5,2)^t;',
     [r' \quad A_c=\begin{pmatrix}7&12\\-3&-5\end{pmatrix}',
      r' \quad A_*=\begin{pmatrix}-2&-1\\1&0\end{pmatrix}']),
    (19188, '9.36247', r' (x,y,w)=(q/(X_1X_2),X_2,X_1),\quad',
     [r" (x',y',w')=(q/X_2,X_1X_2,1/X_1)", r" \quad (x',y',w')=(wx,wy,w^{-1})."]),
    (20985, '39.15', r' \ell=(-z_{Q,1},-z_{Q,2},0,1)^t,\qquad',
     [r' B^{-1}(x_1,x_2,x_3,x_4)^t']),
    (23306, '78.0133', r'ab=d/\nu,\qquad \gcd(b\kappa,\nu)=1,\qquad',
     [r'[j=a\kappa]-[j=0]-[j=a\kappa-b\kappa]+[j=-b\kappa]']),
]

def prepare():
    source = u.repairs.SOURCE.read_text(encoding='utf-8')
    owners, _, _ = parse_statements(source)
    fragments = {path: path.read_text(encoding='utf-8') for path in u.WORK.rglob('*.tex')}
    changes = []
    for line, width, needle, breaks in SPECS:
        positions = [match.start() for match in re.finditer(re.escape(needle), source)]
        selected = [pos for pos in positions
                    if source.count('\n', 0, source.index(r'\]', pos)) + 1 == line]
        assert len(selected) == 1, (line, needle, positions)
        position = selected[0]
        start = source.rfind(r'\[', 0, position)
        stop = source.index(r'\]', position) + 2
        old = source[start:stop]
        assert r'\]' not in source[start:position]
        body = old[2:-2]
        inserted = []
        for boundary in breaks:
            assert body.count(boundary) == 1, (line, boundary)
            insertion = '\\\\{}\n' + boundary
            body = body.replace(boundary, insertion, 1)
            inserted.append((insertion, boundary))
        inverse = body
        for insertion, boundary in reversed(inserted):
            inverse = inverse.replace(insertion, boundary, 1)
        assert inverse == old[2:-2]
        new = '\\[\n\\begin{gathered}{}' + body + '\\end{gathered}\n\\]'
        owner = [row for row in owners if row.start <= start < row.stop]
        assert len(owner) == 1
        paths = [path for path, text in fragments.items() if old in text]
        assert len(paths) == 1 and fragments[paths[0]].count(old) == 1
        headings = list(re.finditer(r'(?m)^\\(?:section|subsection)\{', source[:start]))
        heading = headings[-1]
        end = u.group_end(source, heading.end() - 1)
        title = source[heading.end():end - 1]
        changes.append((line, width, old, new, owner[0].statement_id, paths[0], title))
    return source, fragments, changes

def main():
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--apply', action='store_true')
    args = parser.parse_args()
    source, fragments, changes = prepare()
    for line, width, old, new, sid, path, title in changes:
        print('PASS03_LINE', line, 'OVERFULL_PT', width, 'OWNER', sid, 'UNIT', title, 'FRAGMENT', path)
        print('EXACT_OLD_DISPLAY\n' + old)
        print('EXACT_NEW_DISPLAY\n' + new)
    if not args.apply:
        print('INSPECTION_ONLY; NO_WRITES; ALL_NINE_INSERTION_MAPS_INVERT_EXACTLY')
        return
    now = datetime.now(timezone.utc).isoformat()
    df, ds = r.table(r.DEFECTS)
    ef, es = r.table(u.ROOT / 'CHECK_EVENTS.tsv')
    pf, ps = r.table(u.ROOT / 'S6_SERIES_PUBLISH_unit_progress.tsv')
    candidate = source
    updated = dict(fragments)
    reopened = set()
    for line, width, old, new, sid, path, title in changes:
        ident = f'III-C8-TEX-OVERFLOW-P03-{line}'
        assert not any(row['change_id'] == ident for row in ds)
        candidate = candidate.replace(old, new, 1)
        updated[path] = updated[path].replace(old, new, 1)
        ds.append(dict(change_id=ident, type='D23', statement_id=sid,
            old_location=f'pass03 source line {line}', old_page='incomplete pass03; no final PDF',
            new_location='same complete display; rows at existing formula boundaries', new_page='pending converged build and rendered reading',
            old_text=old, new_text=new,
            reason=f'Actual overfull {width}pt. Root read the complete display and surrounding proof. Insert only gathered and row breaks at the recorded formula boundaries. Removing those inserted exact strings recovers the complete old display; every old character, map, inverse, parameter and expression is retained.',
            review_status='root complete display reading and exact invertible layout insertion ' + now + '; actual successor build and visual page pending'))
        ledger_title = {"Wang's primitive $I_2$ filling": "Wang's primitive I2 filling"}.get(title, title)
        rows = [row for row in ps if row['paper'] == 'III' and row['unit_id'] == sid
                and row['unit_title'] == ledger_title and row['defect_type'] == 'D23']
        assert len(rows) == 1, title
        rows[0].update(status='open', date_utc=now,
            evidence='code/S6_SERIES_PUBLISH_c8_tex_III_final_pass03.log; code/S6_SERIES_PUBLISH_c8_III_first_overflow_repairs.py',
            detail='Actual overfull display above2pt repaired by exact row insertions; successful compilation and current rendered page remain to be checked.')
        reopened.add(rows[0]['unit_id'])
    u.check_permanent_identifiers(source, candidate, set(), set())
    eid = 'publish:c8:III:tex-pass03-first-nine-widths'
    assert not any(row['event_id'] == eid for row in es)
    event = {key: '' for key in ef}
    event.update(statement_id='III:layout-pass03-first-nine', date='2026-11-25',
        who='GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; numerical effort not separately exposed; continuation eight root',
        type='used and rechecked in this run',
        outcome='Root read all nine complete overflow displays, surrounding mathematical context, and every proposed old/new display. Exact insertion/inverse guards preserve all old characters. Actual pass03 widths are attributed to the whole-log runtime reading. The first inspection stopped on repeated chart text, then selected its exact pass03 location; the first apply stopped before writes on the Wang title spelling, whose source/ledger forms are now paired explicitly with its same statement/unit identifier. This repairs layout only and adds no statement, required, independent-proof or page-reading credit.',
        event_id=eid, phase='continuation8 actual TeX repairs',
        source_file='code/S6_SERIES_PUBLISH_c8_III_first_overflow_repairs.py',
        source_event_type='used and rechecked in this run', evidence_group=eid,
        date_utc=now, where='code/S6_SERIES_PUBLISH_c8_III_first_overflow_repairs_inspect_v003.out')
    es.append(event)
    for path, content in updated.items():
        if content != fragments[path]:
            path.write_text(content, encoding='utf-8', newline='\n')
    u.repairs.SOURCE.write_text(candidate, encoding='utf-8', newline='\n')
    r.write_table(r.DEFECTS, df, ds)
    r.write_table(u.ROOT / 'CHECK_EVENTS.tsv', ef, es)
    r.write_table(u.ROOT / 'S6_SERIES_PUBLISH_unit_progress.tsv', pf, ps)
    print('APPLIED_UTC', now, 'EXACT_EDITS', len(changes), 'REOPENED_UNITS', len(reopened))

if __name__ == '__main__':
    main()
