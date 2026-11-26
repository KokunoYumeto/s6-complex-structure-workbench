from S6_SERIES_PUBLISH_c3_edit import *

folder = ROOT / 'agents/continuation3_foundations'
fragment = folder / 'S6_SERIES_PUBLISH_II_integral_specialization.tex'
replace_fragment('\\section{Integral specialization, coherent restrictions and component counts}',
    '\\section{Complete smooth-fibre classification and actual Hopf occurrence}', fragment)
_, defects = read_tsv(folder / 'S6_SERIES_PUBLISH_integral_defects.tsv')
_, events = read_tsv(folder / 'S6_SERIES_PUBLISH_integral_CHECK_EVENTS.tsv')
print('Instance rows:', append_rows(ROOT / 'S6_SERIES_PUBLISH_defects_II.tsv', defects, 'change_id'))
print('Actual exposed-reading rows:', append_rows(ROOT / 'CHECK_EVENTS.tsv', events, 'event_id'))
import_restructured_status('sec:II:02', fragment, folder / 'S6_SERIES_PUBLISH_integral_unit_progress.tsv')
print('The exact rational source application and complete integral refinement were reviewed by root; no independent event added.')
