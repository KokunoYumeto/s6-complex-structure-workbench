"""Record the complete base-map proof comparison and criterion review."""
from datetime import datetime, timezone
import S6_SERIES_PUBLISH_c8_integrate_units as u
import S6_SERIES_PUBLISH_c8_root_units as r
now=datetime.now(timezone.utc).isoformat()
evidence='agents/continuation8_iii_root/S6_SERIES_PUBLISH_III_base_map_unit_review.md'
ef,events=r.table(u.ROOT/'CHECK_EVENTS.tsv')
eid='publish:c8:III:base-map:maps:src:B.2.1'
assert not any(x['event_id']==eid for x in events)
row={k:'' for k in ef}
row.update(statement_id='maps:src:B.2.1',date='2026-11-25',who='GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; numerical effort not separately exposed; continuation eight, root',type='used and rechecked in this run',outcome='Entire preceding64 lines, both proofs, complete c4 comparison and entire rewritten105 lines read. One divisor-root proof retains the explicit base isomorphism/inverse, line frames/lifts/inverses, homotopy, full degree-twelve calculation, quaternionic power action and based translation. Exact VB Prop.3.10 p.86 and AT Cor.4.25 p.361 full proofs read at author source. No new independent proof credit; D18/common bibliography and final PDF gates open.',event_id=eid,phase='continuation8 publication unit comparison',source_file=evidence,source_event_type='used and rechecked in this run',evidence_group='publish:c8:III:base-map',date_utc=now,where=evidence)
events.append(row)
pf,p=r.table(u.ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv')
selected=[x for x in p if x['paper']=='III' and x['unit_id']=='maps:src:B.2.1']
assert len(selected)==28 and all(x['status']=='open' for x in selected)
for row in selected:
 hold=row['defect_type']=='D18'
 row.update(status='open' if hold else 'done',date_utc=now,evidence=evidence,detail='Exact local primary locators read; common bibliography entry must include the p.86 line-bundle use.' if hold else 'Complete preceding/current proof, complete admitted comparison and all28 source findings read; final PDF/build gates remain separate.')
r.write_table(u.ROOT/'CHECK_EVENTS.tsv',ef,events);r.write_table(u.ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv',pf,p)
print('UTC',now)
print('USED_AND_RECHECKED_EVENTS 1; SOURCE_CRITERIA_CLOSED 27; D18_OPEN')
