"""Admit LH, LI and LP full reviews at their actual current boundaries."""
from datetime import datetime,timezone
import re
import S6_SERIES_PUBLISH_c8_integrate_units as u
import S6_SERIES_PUBLISH_c8_root_units as r
now=datetime.now(timezone.utc).isoformat();note='agents/continuation8_iii_root/S6_SERIES_PUBLISH_III_odd_integral_engel_admission.md'
df,ds=r.table(r.DEFECTS);ef,es=r.table(u.ROOT/'CHECK_EVENTS.tsv');pf,ps=r.table(u.ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv')
nd=ne=0
for lane,dfile,efile,keys,counts in [
 ('continuation8_iii_foundations','S6_SERIES_PUBLISH_c8_foundations_defects.tsv','S6_SERIES_PUBLISH_c8_foundations_CHECK_EVENTS.tsv',['weighted_odd_cap_kernels','weighted_integral_homology'],(211,6)),
 ('continuation8_iii_weighted_units','S6_SERIES_PUBLISH_LP_publication_defects.tsv','S6_SERIES_PUBLISH_LP_CHECK_EVENTS.tsv',[],(221,2))]:
 folder=u.ROOT/'agents'/lane;selected=r.table(folder/dfile)[1];events=r.table(folder/efile)[1]
 if keys:
  labels=set()
  for key in keys:labels.update(re.findall(r'\\label\{([^}]+)\}',(u.WORK/'foundations'/f'{key}.tex').read_text()))
  selected=[x for x in selected if x['statement_id'] in labels];events=[x for x in events if x['statement_id'] in labels]
 assert(len(selected),len(events))==counts,(lane,len(selected),len(events))
 for row in selected:
  assert not any(x['change_id']==row['change_id'] for x in ds)
  out={k:row.get(k,'') for k in df};out['review_status']=row.get('review_status','')+'; full attributed review and actual boundaries admitted '+now+'; common/PDF holds: '+note;ds.append(out);nd+=1
 for row in events:
  assert row['type']=='used and rechecked in this run' and not any(x['event_id']==row['event_id'] for x in es)
  out={k:row.get(k,'') for k in ef};out['outcome']=row['outcome']+' Root read each entire substantive review, every criterion and actual canonical application/boundary output. Whole mathematical readings remain attributed; no new independent credit. '+note;es.append(out);ne+=1
closed=added=0
for ident,title,complete in [('maps:src:D.2.40','Shared odd factors and saturated cap kernels',True),('maps:src:D.2.41','Integral bar coordinates at every positive weight',True),('maps:src:D.2.48','Weighted Engel smooth types and pending next boundary',False)]:
 assert not any(x['paper']=='III' and x['unit_id']==ident for x in ps),ident
 for c in [f'D{i:02d}' for i in range(1,28)]+['structure']:
  done=complete and c not in {'D04','D06','D09','D18'};row={k:'' for k in pf};row.update(paper='III',unit_id=ident,unit_title=title,row_kind='structure' if c=='structure' else 'defect',defect_type='' if c=='structure' else c,status='done' if done else 'open',date_utc=now,evidence=note,detail='Full attributed predecessor/current proofs and all28 criteria admitted; '+('actual complete successor present, with four common gates open.' if complete else 'all28 held until LV is a complete actual following unit.'));ps.append(row);added+=1;closed+=done
for ident,title in [('maps:src:D.2.37','Weighted natural profiles and their integral cap maps'),('maps:src:D.2.44','Residual orders four, eight and twenty')]:
 rows=[x for x in ps if x['paper']=='III' and x['unit_id']==ident];assert len(rows)==28 and all(x['status']=='open' for x in rows),ident
 for row in rows:
  c=row['defect_type'] or 'structure';done=c not in {'D04','D06','D09','D18'};row.update(unit_title=title,status='done' if done else 'open',date_utc=now,evidence=note,detail='The wholly admitted proof now has its complete actual following subsection. Four common gates and final PDF remain.');closed+=done
assert(nd,ne,closed,added)==(432,8,96,84),(nd,ne,closed,added)
r.write_table(r.DEFECTS,df,ds);r.write_table(u.ROOT/'CHECK_EVENTS.tsv',ef,es);r.write_table(u.ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv',pf,ps)
print('UTC',now);print('EXACT_DEFECT_ROWS',nd,'ATTRIBUTED_USED_EVENTS',ne);print('SOURCE_CRITERIA_CLOSED',closed,'NEW_ACTUAL_UNIT_ROWS',added);print('LP_ALL28_HELD; FOUR_COMMON_GATES_AND_FINAL_PDF_OPEN')
