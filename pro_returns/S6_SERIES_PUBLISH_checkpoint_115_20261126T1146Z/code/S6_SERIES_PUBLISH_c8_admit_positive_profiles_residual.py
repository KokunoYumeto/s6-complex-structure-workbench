"""Admit complete positive-weight/profile/residual reviews at actual boundaries."""
from datetime import datetime,timezone
import re
import S6_SERIES_PUBLISH_c8_integrate_units as u
import S6_SERIES_PUBLISH_c8_root_units as r
now=datetime.now(timezone.utc).isoformat()
note='agents/continuation8_iii_root/S6_SERIES_PUBLISH_III_positive_profiles_residual_admission.md'
df,ds=r.table(r.DEFECTS);ef,es=r.table(u.ROOT/'CHECK_EVENTS.tsv');pf,ps=r.table(u.ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv')
nd=ne=0
for lane,dfile,efile,keys,counts in [
 ('continuation8_iii_foundations','S6_SERIES_PUBLISH_c8_foundations_defects.tsv','S6_SERIES_PUBLISH_c8_foundations_CHECK_EVENTS.tsv',['positive_engel_weights','weighted_natural_profiles'],(220,7)),
 ('continuation8_iii_weighted_units','S6_SERIES_PUBLISH_RESIDUAL_publication_defects.tsv','S6_SERIES_PUBLISH_RESIDUAL_CHECK_EVENTS.tsv',[],(426,4))]:
 folder=u.ROOT/'agents'/lane;selected=r.table(folder/dfile)[1];events=r.table(folder/efile)[1]
 if keys:
  labels=set()
  for key in keys:labels.update(re.findall(r'\\label\{([^}]+)\}',(u.WORK/'foundations'/f'{key}.tex').read_text()))
  selected=[x for x in selected if x['statement_id'] in labels]
  events=[x for x in events if x['statement_id'] in labels]
 assert(len(selected),len(events))==counts,(lane,len(selected),len(events))
 for row in selected:
  assert not any(x['change_id']==row['change_id'] for x in ds)
  out={k:row.get(k,'') for k in df};out['review_status']=row.get('review_status','')+'; complete attributed review and actual canonical boundaries admitted '+now+'; common/PDF holds: '+note;ds.append(out);nd+=1
 for row in events:
  assert row['type']=='used and rechecked in this run' and not any(x['event_id']==row['event_id'] for x in es)
  out={k:row.get(k,'') for k in ef};out['outcome']=row['outcome']+' Root read complete substantive reviews and all criterion tables, exact correction/downstream comparisons and actual application/boundary outputs. Whole mathematical readings remain attributed. No new independent credit. '+note;es.append(out);ne+=1
closed=added=0
for ident,title,complete in [('maps:src:D.2.34','All positive weights of the Engel construction',True),('maps:src:D.2.37','Weighted natural profiles and pending next boundary',False),('maps:src:D.2.44','Residual orders four, eight and twenty and pending next boundary',False)]:
 assert not any(x['paper']=='III' and x['unit_id']==ident for x in ps),ident
 for c in [f'D{i:02d}' for i in range(1,28)]+['structure']:
  done=complete and c not in {'D04','D06','D09','D18'};row={k:'' for k in pf};row.update(paper='III',unit_id=ident,unit_title=title,row_kind='structure' if c=='structure' else 'defect',defect_type='' if c=='structure' else c,status='done' if done else 'open',date_utc=now,evidence=note,detail='Complete attributed old/current proof and all28 review admitted; '+('actual following unit present; four common gates remain.' if complete else 'all28 held until the following unreviewed proof has its complete actual-unit boundary.'));ps.append(row);added+=1;closed+=done
for ident,title in [('maps:src:D.2.33','Original multiplicative caps and their integral homology'),('maps:src:D.2.39','Three-primary smooth types')]:
 rows=[x for x in ps if x['paper']=='III' and x['unit_id']==ident];assert len(rows)==28 and all(x['status']=='open' for x in rows),ident
 for row in rows:
  c=row['defect_type'] or 'structure';done=c not in {'D04','D06','D09','D18'};row.update(unit_title=title,status='done' if done else 'open',date_utc=now,evidence=note,detail='Previously complete full proof now has its actual complete successor. Four common gates and final PDF remain.');closed+=done
assert(nd,ne,closed,added)==(646,11,72,84),(nd,ne,closed,added)
r.write_table(r.DEFECTS,df,ds);r.write_table(u.ROOT/'CHECK_EVENTS.tsv',ef,es);r.write_table(u.ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv',pf,ps)
print('UTC',now);print('EXACT_DEFECT_ROWS',nd,'ATTRIBUTED_USED_EVENTS',ne);print('SOURCE_CRITERIA_CLOSED',closed,'NEW_ACTUAL_UNIT_ROWS',added);print('LD_AND_RESIDUAL_ALL28_HELD; FOUR_COMMON_GATES_AND_FINAL_PDF_OPEN')
