from S6_SERIES_PUBLISH_c3_edit import *

agent = ROOT / 'agents/continuation3_foundations'
units = [
    ('sec:II:conventions', 'Common conventions', 'Index, Picard components and endpoint cohomology', 'common_conventions'),
    ('sec:II:01', 'Index, Picard components and endpoint cohomology', 'Integral specialization, coherent restrictions and component counts', 'index_picard_endpoints'),
]
for unit, start, end, name in units:
    before, after = replace_fragment('\\section{' + start + '}', '\\section{' + end + '}', agent / f'S6_SERIES_PUBLISH_II_{name}.tex')
    print(f'{unit}: integrated {len(before)} -> {len(after)} characters; original labels and tags preserved')

_, defects = read_tsv(agent / 'S6_SERIES_PUBLISH_foundations_defects.tsv')
_, events = read_tsv(agent / 'S6_SERIES_PUBLISH_foundations_CHECK_EVENTS.tsv')
print('New defect rows:', append_rows(ROOT / 'S6_SERIES_PUBLISH_defects_II.tsv', defects[:10], 'change_id'))
print('New exposed-reading events:', append_rows(ROOT / 'CHECK_EVENTS.tsv', events[:4], 'event_id'))
import_unit_status(agent / 'S6_SERIES_PUBLISH_foundations_unit_progress.tsv', {x[0] for x in units})

apply_edit('\\allowdisplaybreaks[2]\n', '\\allowdisplaybreaks[2]\n\\numberwithin{equation}{section}\n',
    'II-C3-EQUATION-COUNTER', ['D19'], '', 'Preamble: equation counter',
    'Use the ordinary equation counter reset by section. Existing manual tags are converted in their text units; their labels are retained. This setting changes no equation payload.')
set_unit_status('sec:II:01', 'D19', 'done',
    'The unit contains no manual tags; the global section equation counter is now installed.', 'S6_SERIES_PUBLISH_II.tex')
print('First two unit text changes admitted. Exact Paper I locators and final structure remain open as recorded.')
