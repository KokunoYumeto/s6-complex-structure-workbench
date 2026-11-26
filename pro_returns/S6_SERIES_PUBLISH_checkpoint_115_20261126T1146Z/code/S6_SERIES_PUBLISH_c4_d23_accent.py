"""Restore the accent found by the final source notation reading."""
from S6_SERIES_PUBLISH_c4_edit import *

_, guards = read_tsv(ROOT / 'agents/continuation4_horizontal/S6_SERIES_PUBLISH_D23_residual_guards.tsv')
_, defects = read_tsv(ROOT / 'agents/continuation4_horizontal/S6_SERIES_PUBLISH_D23_residual_defects.tsv')
assert len(guards) == len(defects) == 1
guard, defect = guards[0], defects[0]
assert (guard['old_text'], guard['new_text']) == (defect['old_text'], defect['new_text'])
apply_edit(guard['old_text'], guard['new_text'], guard['change_id'], ['D23'],
    defect['statement_id'], defect['old_location'], defect['reason'],
    review='Root read the exact old/new phrase and confirmed the unchanged cohomology context. The final rendered D23 row stays open; no mathematical proof credit.')
print('One accent restored; all rendered-page gates remain open.')
