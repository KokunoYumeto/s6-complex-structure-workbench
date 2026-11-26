from S6_SERIES_PUBLISH_c3_edit import *

folder = ROOT / 'agents/continuation3_foundations'
fragment = folder / 'S6_SERIES_PUBLISH_II_smooth_fibres.tex'
replace_fragment(
    '\\section{Complete smooth-fibre classification and actual Hopf occurrence}',
    '\\section{Cotangent torsion, conductor and the printed endpoint error}', fragment)
_, defects = read_tsv(folder / 'S6_SERIES_PUBLISH_classification_defects.tsv')
_, events = read_tsv(folder / 'S6_SERIES_PUBLISH_classification_CHECK_EVENTS.tsv')
print('Instance rows:', append_rows(ROOT / 'S6_SERIES_PUBLISH_defects_II.tsv', defects, 'change_id'))
print('Actual exposed-reading rows:', append_rows(ROOT / 'CHECK_EVENTS.tsv', events, 'event_id'))
import_restructured_status('sec:II:03', fragment,
    folder / 'S6_SERIES_PUBLISH_classification_unit_progress.tsv')
print('Necessary-list and final-list scopes compared clause by clause; all original permanent identifiers retained.')

