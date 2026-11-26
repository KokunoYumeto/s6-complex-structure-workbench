"""Admit the four graph-cap source units and close the actual S5 boundary."""
from datetime import datetime,timezone
import S6_SERIES_PUBLISH_c8_integrate_units as u
import S6_SERIES_PUBLISH_c8_root_units as r
now=datetime.now(timezone.utc).isoformat()
note='agents/continuation8_iii_root/S6_SERIES_PUBLISH_III_os49_graph_admission.md'
df,ds=r.table(r.DEFECTS);ef,es=r.table(u.ROOT/'CHECK_EVENTS.tsv')
pf,ps=r.table(u.ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv')
f=u.ROOT/'agents/continuation8_iii_later';nd=ne=0
for row in r.table(f/'S6_SERIES_PUBLISH_III_os49_graph_caps_publication_defects.tsv')[1]:
 assert not any(x['change_id']==row['change_id'] for x in ds)
 out={k:row.get(k,'') for k in df};out['review_status']=row.get('review_status','')+'; whole attributed publication review, root full sign-note/SB reading and exact canonical placement admitted '+now+'; common/PDF gates remain. '+note
 ds.append(out);nd+=1
for row in r.table(f/'S6_SERIES_PUBLISH_III_os49_graph_caps_publication_CHECK_EVENTS.tsv')[1]:
 assert row['type']=='used and rechecked in this run'
 assert not any(x['event_id']==row['event_id'] for x in es)
 out={k:row.get(k,'') for k in ef};out['outcome']=row['outcome']+' Root read the complete review/criterion matrix and whole sign note plus final SB proof; other whole-proof readings remain attributed. No added independent-check credit. '+note
 es.append(out);ne+=1
assert(nd,ne)==(63,4),(nd,ne)
closed=added=0
for ident,title in [('night:P3F.31','Return of the positive-diagonal family'),('night:P3F.32','Return for all sphere caps'),('night:P3F.33','The complete free affine sector'),('night:P3F.34','Integral homology of every free cap')]:
 assert not any(x['paper']=='III' and x['unit_id']==ident for x in ps)
 for c in [f'D{i:02d}' for i in range(1,28)]+['structure']:
  hold=c in {'D04','D06','D09','D18'};row={k:'' for k in pf}
  row.update(paper='III',unit_id=ident,unit_title=title,row_kind='structure' if c=='structure' else 'defect',defect_type='' if c=='structure' else c,status='open' if hold else 'done',date_utc=now,evidence=note,detail='Common reference/program/bibliography gate remains open.' if hold else 'Complete attributed predecessor/current proof comparison and all28 criteria admitted; exact root sign/SB scope documented; actual next subsection or section is present.')
  ps.append(row);added+=1;closed+=not hold
for row in ps:
 if row['paper']=='III' and row['unit_id']=='night:P3F.29':
  assert row['status']=='open';hold=row['defect_type'] in {'D04','D06','D09','D18'}
  row.update(unit_title='Coprime finite caps',status='open' if hold else 'done',date_utc=now,evidence=note,detail='The complete earlier construction/Q30N/P29 review now has the actual S8 following subsection; four common gates remain.');closed+=not hold
assert(closed,added)==(120,112),(closed,added)
r.write_table(r.DEFECTS,df,ds);r.write_table(u.ROOT/'CHECK_EVENTS.tsv',ef,es);r.write_table(u.ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv',pf,ps)
print('UTC',now);print('EXACT_DEFECT_ROWS',nd,'ATTRIBUTED_USED_EVENTS',ne)
print('SOURCE_CRITERIA_CLOSED',closed,'NEW_ACTUAL_UNIT_ROWS',added)
print('ALL_OS49_SOURCE_UNITS_HAVE_ACTUAL_BOUNDARIES; FOUR_COMMON_GATES_AND_FINAL_PAGES_OPEN')

