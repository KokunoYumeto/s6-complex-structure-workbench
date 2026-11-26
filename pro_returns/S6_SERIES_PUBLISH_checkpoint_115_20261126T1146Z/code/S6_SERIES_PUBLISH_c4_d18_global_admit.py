"""Admit the completed source/locus bibliography gate, with exact old units."""
from S6_SERIES_PUBLISH_c4_edit import *
import csv
csv.field_size_limit(10000000)
prefix=ROOT/'agents/continuation4_reductions/S6_SERIES_PUBLISH_c4_bibliography'
_, proposals=read_tsv(str(prefix)+'_unit_status.tsv')
_, prepared=read_tsv(str(prefix)+'_CHECK_EVENTS.tsv')
assert len(proposals)==85
events=[r for r in prepared if r['event_id']=='II-C4-BIBLIOGRAPHY-GLOBAL-COVERAGE']
assert len(events)==1
fields,units=read_tsv(ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv')
index={(r['paper'],r['unit_id'],r['defect_type']):r for r in units}
for p in proposals:
    key=(p['paper'],p['unit_id'],p['defect_type'])
    assert key[0]=='II' and key[2]=='D18' and key in index
    assert index[key]['status']=='open'
    assert index[('II',key[1],'D12')]['status']=='done'
    index[key].update(status='done',date_utc=now(),evidence=p['evidence'],detail=p['detail'])
front=('the-series-and-this-paper','series:II:main-theorems','series:II:outline','known-and-new')
for unit in front:
    row=index[('II',unit,'D18')]
    assert row['status']=='open' and index[('II',unit,'D12')]['status']=='done'
    row.update(status='done',date_utc=now(),
        evidence='S6_SERIES_PUBLISH_c4_global_comparison.md; agents/continuation4_horizontal/S6_SERIES_PUBLISH_outline_comparison.md; agents/continuation4_reductions/S6_SERIES_PUBLISH_c4_bibliography_coverage.md; S6_SERIES_PUBLISH_c4_primary_readings.tsv',
        detail='Root read the complete main A-G statements and supplying proofs, the final outlines, Known and new source claims and complete first-part comparison. Exact cited versions/pages are supported by the retained primary readings and fresh literature searches. Global printed citation/bibliography reconciliation is admitted. Rendered bibliography remains a separate page gate.')
_,old=read_tsv(ROOT/'CHECK_EVENTS.tsv')
assert events[0]['event_id'] not in {r['event_id'] for r in old}
print('Global source-coverage event:',append_rows(ROOT/'CHECK_EVENTS.tsv',events,'event_id'))
write_tsv(ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv',fields,units)
print('Existing body D18 rows closed:',len(proposals))
print('Existing complete-front D18 rows closed:',len(front))
print('Methodology, final source-record merge and rendered bibliography remain separate gates.')
