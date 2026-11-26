"""Remove the 91 read paragraph separators before mixed-three equation labels."""
from datetime import datetime, timezone
import re
import S6_SERIES_PUBLISH_c8_integrate_units as u
import S6_SERIES_PUBLISH_c8_root_units as r

now = datetime.now(timezone.utc).isoformat()
source = u.repairs.SOURCE.read_text(encoding='utf-8')
fragment = u.WORK / 'weighted/three_primary_types.tex'
fragment_source = fragment.read_text(encoding='utf-8')
candidate, fragment_candidate = source, fragment_source
expected = set(range(5, 102)) - {56, 72, 73, 74, 75, 92}
df, ds = r.table(r.DEFECTS)
ef, es = r.table(u.ROOT / 'CHECK_EVENTS.tsv')
pf, ps = r.table(u.ROOT / 'S6_SERIES_PUBLISH_unit_progress.tsv')
changes = []
for match in re.finditer(r'\\begin\{equation\}.*?\\end\{equation\}', source, re.S):
    old = match[0]
    blank = list(re.finditer(r'\n[ \t]*\n', old))
    if not blank:
        continue
    labels = re.findall(r'\\label\{maps:eq:MT_local_(\d+)\}', old)
    assert len(labels) == 1 and int(labels[0]) in expected
    assert len(blank) == 1
    separator = blank[0]
    assert old[separator.end():].startswith(r'\hypertarget{tag-Q')
    new = old[:separator.start()] + '\n' + old[separator.end():]
    assert source.count(old) == fragment_source.count(old) == 1
    assert new.replace('\n', '').replace(' ', '').replace('\t', '') == old.replace('\n', '').replace(' ', '').replace('\t', '')
    candidate = candidate.replace(old, new, 1)
    fragment_candidate = fragment_candidate.replace(old, new, 1)
    changes.append((int(labels[0]), match.start(), old, new))
assert len(changes) == 91 and {x[0] for x in changes} == expected
u.check_permanent_identifiers(source, candidate, set(), set())
for number, start, old, new in changes:
    ident = f'III-C8-TEX-MATH-PARAGRAPH-MT-{number:03d}'
    assert not any(row['change_id'] == ident for row in ds)
    ds.append(dict(
        change_id=ident, type='D23', statement_id='maps:src:D.2.42',
        old_location=f'maps:eq:MT_local_{number}; pass03 source line {source.count(chr(10), 0, start) + 1}',
        old_page='incomplete pass03; no final PDF',
        new_location=f'same equation maps:eq:MT_local_{number}',
        new_page='pending successful full PDF', old_text=old, new_text=new,
        reason='Pass03 stopped at a literal blank paragraph inside display math. Root read this complete display. Remove only its whitespace-only line immediately before the unchanged target and label; the inverse reinserts exactly the old separator recorded here. Every mathematical character, expression, environment, tag and label is retained.',
        review_status='exact root display reading and syntax repair ' + now + '; successful successor build and rendered page remain open; no new mathematical check'))
rows = [row for row in ps if row['paper'] == 'III' and row['unit_title'] == 'Three-primary smooth types' and row['defect_type'] == 'D23']
assert len(rows) == 1
rows[0].update(status='open', date_utc=now,
               evidence='code/S6_SERIES_PUBLISH_c8_tex_III_final_pass03.log; code/S6_SERIES_PUBLISH_c8_III_blank_math_fix.py',
               detail='Actual paragraph-in-math failure repaired at all 91 completely read mixed-three displays; equations unchanged. Successful compilation and visual review remain.')
eid = 'publish:c8:III:tex-math-paragraphs'
assert not any(row['event_id'] == eid for row in es)
event = {key: '' for key in ef}
event.update(statement_id='III:layout-math-paragraphs', date='2026-11-25',
             who='GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; numerical effort not separately exposed; continuation eight root',
             type='used and rechecked in this run',
             outcome='Actual pass03 fatal context and all 91 full affected equation displays read. Exact paragraph separators before existing labels are removed, with all mathematical characters and literal identifiers preserved. The first diagnostic falsely treated the title row-break spacing as display opening; its corrected scanner excludes that occurrence, and every one of its 91 real blocks is exactly the already read block. No theorem, parameter, invariant, required-check or independent-proof credit is added. Complete pass03 streams are read by the runtime reviewer, not newly claimed here.',
             event_id=eid, phase='continuation8 actual TeX repairs',
             source_file='code/S6_SERIES_PUBLISH_c8_III_blank_math_fix.py',
             source_event_type='used and rechecked in this run', evidence_group=eid,
             date_utc=now, where='code/S6_SERIES_PUBLISH_c8_III_blank_math_diagnosis_v002.out')
es.append(event)
fragment.write_text(fragment_candidate, encoding='utf-8', newline='\n')
u.repairs.SOURCE.write_text(candidate, encoding='utf-8', newline='\n')
r.write_table(r.DEFECTS, df, ds)
r.write_table(u.ROOT / 'CHECK_EVENTS.tsv', ef, es)
r.write_table(u.ROOT / 'S6_SERIES_PUBLISH_unit_progress.tsv', pf, ps)
assert fragment.read_text(encoding='utf-8') == fragment_candidate
assert u.repairs.SOURCE.read_text(encoding='utf-8') == candidate
print('UTC', now, 'EXACT_DISPLAY_REPAIRS', len(changes), 'REOPENED_UNIT', rows[0]['unit_id'])
print('EXACT_LABEL_SUFFIXES', ','.join(str(x[0]) for x in changes))
print('ALL_MATHEMATICAL_CHARACTERS_AND_LITERAL_IDS_PRESERVED')
