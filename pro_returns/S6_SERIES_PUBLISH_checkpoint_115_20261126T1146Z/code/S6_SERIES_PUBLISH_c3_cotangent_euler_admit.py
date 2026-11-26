from S6_SERIES_PUBLISH_c3_edit import *

folder = ROOT / 'agents/continuation3_conductor'
fragment = folder / 'S6_SERIES_PUBLISH_c3_conductor_01_replacement.tex'
replace_fragment(
    '\\section{Cotangent torsion, conductor and the printed endpoint error}',
    '\\section{Normalization, conductor genus and local torus exclusions}', fragment)
for name, target, key in [
    ('defects', 'S6_SERIES_PUBLISH_defects_II.tsv', 'change_id'),
    ('CHECK_EVENTS', 'CHECK_EVENTS.tsv', 'event_id')]:
    _, rows = read_tsv(folder / f'S6_SERIES_PUBLISH_c3_conductor_01_{name}.tsv')
    print(name, append_rows(ROOT / target, rows, key))
import_restructured_status('sec:II:04', fragment,
    folder / 'S6_SERIES_PUBLISH_c3_conductor_01_unit_status.tsv')

fragment = folder / 'S6_SERIES_PUBLISH_c3_conductor_02_replacement.tex'
text = SOURCE.read_text()
start = '\\section{Euler identities, normal-crossing fibres and conductor jets}'
end = '\\section{Irreducible supports: topology, conductor and equality}'
a, b = text.index(start), text.index(end)
before, after = text[a:b], fragment.read_text()
preserve_identifiers(before, after)
text = text[:a] + text[b:]
insertion = text.index('\\section{Normalization, conductor genus and local torus exclusions}')
text = text[:insertion] + after + text[insertion:]
_, repairs = read_tsv(folder / 'S6_SERIES_PUBLISH_c3_conductor_02_remote_reference_repairs.tsv')
for row in repairs:
    a = text.index('\\label{' + row['statement_id'] + '}')
    b = text.index('\\end{proof}', a) + len('\\end{proof}')
    block = text[a:b]
    assert block.count(row['old_text']) == 1, row['statement_id']
    text = text[:a] + block.replace(row['old_text'], row['new_text'], 1) + text[b:]
SOURCE.write_text(text, newline='\n')
for name, target, key in [
    ('defects', 'S6_SERIES_PUBLISH_defects_II.tsv', 'change_id'),
    ('CHECK_EVENTS', 'CHECK_EVENTS.tsv', 'event_id')]:
    _, rows = read_tsv(folder / f'S6_SERIES_PUBLISH_c3_conductor_02_{name}.tsv')
    print(name, append_rows(ROOT / target, rows, key))
import_restructured_status(['cdp:st:C.2.NC.2', 'cdp:st:C2d'], fragment,
    folder / 'S6_SERIES_PUBLISH_c3_conductor_02_unit_status.tsv')
print('C2a now has an explicit unit row; former section-leading material was not separately tracked.')
print('Restored existing owner 01C8; fixed its three actual reader uses; moved C2d before its normalization consumers.')
