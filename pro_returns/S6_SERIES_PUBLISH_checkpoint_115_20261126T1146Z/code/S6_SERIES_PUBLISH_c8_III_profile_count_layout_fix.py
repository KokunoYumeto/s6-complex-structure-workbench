"""Reflow the read 21-entry profile/count table into three bands of seven."""
from datetime import datetime, timezone
import re
import S6_SERIES_PUBLISH_c8_integrate_units as u
import S6_SERIES_PUBLISH_c8_root_units as r

now = datetime.now(timezone.utc).isoformat()
source = u.repairs.SOURCE.read_text(encoding='utf-8')
needle = r' \begin{array}{c|rrrrrrrrrrr}'
assert source.count(needle) == 1
position = source.index(needle)
start = source.rfind(r'\[', 0, position)
stop = source.index(r'\]', position) + 2
old = source[start:stop]
lines = old.splitlines()
assert len(lines) == 8
header1 = lines[2].strip().removesuffix(r'\\').split('&')[1:]
values1 = lines[3].strip().removesuffix(r'\\ \hline').split('&')[1:]
header2 = lines[4].strip().removesuffix(r'\\').split('&')[1:]
values2 = lines[5].strip().split('&')[1:]
assert len(header1) == len(values1) == 11
assert len(header2) == len(values2) == 10
pairs = list(zip(header1 + header2, values1 + values2))
assert len(pairs) == 21 and sum(int(value) for _, value in pairs) == 172
newlines = [r'\[', r' \begin{array}{c|rrrrrrr}']
recovered = []
for band in range(3):
    selected = pairs[7*band:7*(band+1)]
    recovered.extend(selected)
    newlines.append(' &' + '&'.join(label for label, _ in selected) + r'\\')
    newlines.append(r' \#&' + '&'.join(value for _, value in selected) + (r'\\ \hline' if band < 2 else ''))
newlines.extend([r' \end{array}', r'\]'])
new = '\n'.join(newlines)
assert recovered == pairs
fragment = u.WORK / 'weighted/three_primary_types.tex'
fragment_source = fragment.read_text(encoding='utf-8')
assert fragment_source.count(old) == 1
candidate = source.replace(old, new, 1)
u.check_permanent_identifiers(source, candidate, set(), set())
df, ds = r.table(r.DEFECTS)
ef, es = r.table(u.ROOT / 'CHECK_EVENTS.tsv')
pf, ps = r.table(u.ROOT / 'S6_SERIES_PUBLISH_unit_progress.tsv')
ident = 'III-C8-TEX-P04-PROFILE-COUNT-TABLE'
assert not any(row['change_id'] == ident for row in ds)
reason = 'Actual pass04 overflow122.48746pt at41577. Root read the whole table and surrounding enumeration/domain. Preserve the exact ordered21 profile-count pairs, sending index i=1..21 to band1+floor((i-1)/7), column1+((i-1) mod7); the inverse is i=7(band-1)+column. Only the array width and row placement change; the explicit old/new pairs are identical and their displayed total remains172.'
ds.append(dict(change_id=ident, type='D23', statement_id='maps:src:D.2.42', old_location='pass04 source41577; mixed-three natural-row count table', old_page='incomplete pass04; no final PDF', new_location='same21 profile-count pairs, three bands of seven', new_page='pending complete build and visual reading', old_text=old, new_text=new, reason=reason, review_status='whole root table/context reading and exact layout map ' + now + '; successful build and page open'))
rows = [row for row in ps if row['paper'] == 'III' and row['unit_id'] == 'maps:src:D.2.39' and row['defect_type'] == 'D23']
assert len(rows) == 1
rows[0].update(status='open', date_utc=now, evidence='code/S6_SERIES_PUBLISH_c8_III_profile_count_layout_fix.py; code/S6_SERIES_PUBLISH_c8_tex_III_final_pass04.log', detail='Read21 ordered profile/count pairs reflowed with an explicit reversible index map after actual122.48746pt overflow; full build and visual review remain.')
eid = 'publish:c8:III:tex-pass04-profile-table'
assert not any(row['event_id'] == eid for row in es)
event = {key: '' for key in ef}
event.update(statement_id='III:layout-pass04-profile-table', date='2026-11-25', who='GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; numerical effort not separately exposed; continuation eight root', type='used and rechecked in this run', outcome=reason + ' No mathematical enumeration is rerun, and no required, independent, final-build or page-reading credit is added.', event_id=eid, phase='continuation8 actual TeX repairs', source_file='code/S6_SERIES_PUBLISH_c8_III_profile_count_layout_fix.py', source_event_type='used and rechecked in this run', evidence_group=eid, date_utc=now, where='code/S6_SERIES_PUBLISH_c8_tex_III_final_pass04.log')
es.append(event)
fragment.write_text(fragment_source.replace(old, new, 1), encoding='utf-8', newline='\n')
u.repairs.SOURCE.write_text(candidate, encoding='utf-8', newline='\n')
r.write_table(r.DEFECTS, df, ds)
r.write_table(u.ROOT / 'CHECK_EVENTS.tsv', ef, es)
r.write_table(u.ROOT / 'S6_SERIES_PUBLISH_unit_progress.tsv', pf, ps)
print('UTC', now, 'EXACT_ORDERED_PAIRS', len(pairs), 'SUM', sum(int(v) for _, v in pairs))
print('ACTUAL_OLD_TABLE\n' + old + '\nACTUAL_NEW_TABLE\n' + new)
