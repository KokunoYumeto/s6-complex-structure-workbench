"""Admit the exact residual front/body comparison and two reference kinds."""
from S6_SERIES_PUBLISH_c4_edit import *
import csv
csv.field_size_limit(10000000)

prefix = ROOT/'agents/continuation4_horizontal'
_, guards = read_tsv(prefix/'S6_SERIES_PUBLISH_D23_kind_guards.tsv')
_, defects = read_tsv(prefix/'S6_SERIES_PUBLISH_D23_kind_defects.tsv')
_, proposals = read_tsv(prefix/'S6_SERIES_PUBLISH_D24_closure_unit_proposals.tsv')
assert len(guards)==len(defects)==2 and len(proposals)==107
before=SOURCE.read_text(); after=before
for g in guards:
    assert after.count(g['old_text'])==1
    after=after.replace(g['old_text'],g['new_text'],1)
assert identifiers(before)==identifiers(after)
for row in defects:
    row['review_status']='Root read the exact old/new phrases, receiving context and the target cited-result environment/name definitions. Only the displayed reference kind changes through the identical label. D23 awaits final images; no new proof credit.'
fields,units=read_tsv(ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv')
index={(r['paper'],r['unit_id'],r['defect_type']):r for r in units}
for p in proposals:
    key=(p['paper'],p['unit_id'],'D24')
    assert key in index and p['paper']=='II' and p['defect_type']=='D24'
    assert index[key]['status']=='open'
    assert index[('II',p['unit_id'],'D12')]['status']=='done'
    index[key].update(status='done',date_utc=now(),evidence=p['evidence'],detail=p['detail'])
_, old=read_tsv(ROOT/'S6_SERIES_PUBLISH_defects_II.tsv')
assert not {r['change_id'] for r in old}.intersection(r['change_id'] for r in defects)
SOURCE.write_text(after,newline='\n')
print('Reference-kind corrections:',append_rows(ROOT/'S6_SERIES_PUBLISH_defects_II.tsv',defects,'change_id'))
write_tsv(ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv',fields,units)
print('Existing D24 rows closed:',len(proposals))
print('Methodology and rendered-page/D23 gates remain open. No proof events added.')
