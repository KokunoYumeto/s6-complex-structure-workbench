"""Admit the completed OS49 construction and minimal-primary packet scopes."""
from datetime import datetime,timezone
import S6_SERIES_PUBLISH_c8_integrate_units as u
import S6_SERIES_PUBLISH_c8_root_units as r
now=datetime.now(timezone.utc).isoformat()
note='agents/continuation8_iii_root/S6_SERIES_PUBLISH_III_os49_minimal_admission.md'
df,ds=r.table(r.DEFECTS);ef,es=r.table(u.ROOT/'CHECK_EVENTS.tsv')
pf,ps=r.table(u.ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv')
nd=ne=0
def merge_d(path):
 global nd
 for row in r.table(path)[1]:
  assert not any(x['change_id']==row['change_id'] for x in ds),row['change_id']
  out={k:row.get(k,'') for k in df}
  out['review_status']=row.get('review_status','')+'; attributed complete publication review and exact canonical placement admitted '+now+'; final common/boundary/PDF holds as recorded. '+note
  ds.append(out);nd+=1
def merge_e(path,predicate=lambda x:True):
 global ne
 for row in r.table(path)[1]:
  if not predicate(row):continue
  assert row['type']=='used and rechecked in this run'
  assert not any(x['event_id']==row['event_id'] for x in es),row['event_id']
  out={k:row.get(k,'') for k in ef}
  out['outcome']=row['outcome']+' Root read the full review and exact admission scopes; only Q30N/P29 and the earlier bridge have the additional stated root whole-source reading. No other second whole-proof or independent credit. '+note
  es.append(out);ne+=1
l=u.ROOT/'agents/continuation8_iii_later';w=u.ROOT/'agents/continuation8_iii_weighted_units'
merge_d(l/'S6_SERIES_PUBLISH_III_os49_construction_publication_defects.tsv')
merge_e(l/'S6_SERIES_PUBLISH_III_os49_construction_publication_CHECK_EVENTS.tsv')
assert(nd,ne)==(88,5),(nd,ne)
merge_d(w/'S6_SERIES_PUBLISH_MINIMAL_publication_defects.tsv')
merge_e(w/'S6_SERIES_PUBLISH_MINIMAL_CHECK_EVENTS.tsv')
merge_e(u.ROOT/'agents/continuation8_iii_foundations/S6_SERIES_PUBLISH_c8_foundations_CHECK_EVENTS.tsv',lambda x:x['event_id']=='ce:III:c8:foundations:02KL:os49-owner-comparison')
assert(nd,ne)==(912,12),(nd,ne)
closed=added=0
old=[x for x in ps if x['paper']=='III' and x['unit_id']=='sec:III:os49-night']
assert len(old)==28 and all(x['status']=='open' for x in old)
for row in old:
 c='structure' if row['row_kind']=='structure' else row['defect_type']
 hold=c in {'D04','D06','D09','D18'}
 row.update(unit_id='night:P3F.26',unit_title='An explicit sphere filling',status='open' if hold else 'done',date_utc=now,evidence=note,detail='Former section-level scope sec:III:os49-night is now this actual first subsection; no extra rows for rekeying. Whole attributed source review admitted; common gates open.' if hold else 'Former section-level scope rekeyed to the complete actual subsection; every criterion has the whole attributed proof review; no progress from the split alone.')
 closed+=not hold
for ident,title,hold_all in [
 ('night:P3F.27','The angular clutch',False),
 ('night:P3F.28','Iterates of the section line',False),
 ('night:P3F.29','Coprime finite caps and pending next boundary',True),
 ('maps:src:D.2.35','Minimal primary smooth types and pending next boundary',True),
]:
 assert not any(x['paper']=='III' and x['unit_id']==ident for x in ps),ident
 for c in [f'D{i:02d}' for i in range(1,28)]+['structure']:
  hold=hold_all or c in {'D04','D06','D09','D18'}
  row={k:'' for k in pf}
  row.update(paper='III',unit_id=ident,unit_title=title,row_kind='structure' if c=='structure' else 'defect',defect_type='' if c=='structure' else c,status='open' if hold else 'done',date_utc=now,evidence=note,detail='Complete attributed fragment review admitted, but the next actual subsection boundary remains pending; all28 source criteria held.' if hold_all else 'Common reference/program/bibliography gate remains open.' if hold else 'Whole attributed source/comparison and all28 findings admitted; actual following subsection present; final build/pages separate.')
  ps.append(row);added+=1;closed+=not hold
for row in ps:
 if row['paper']=='III' and row['unit_id']=='maps:src:D.2.11' and (row['defect_type'] in {'D12','D14','D20'} or row['row_kind']=='structure'):
  assert row['status']=='open'
  row.update(status='done',date_utc=now,evidence=note,detail='The complete Q30N source/line/period/stem/root/collar/normal/fan map and inverse are canonical before the KL application; whole bridge and final P29 read by root and cross-read by foundations.');closed+=1
 if row['paper']=='III' and row['unit_id']=='maps:src:D.2.52':
  assert row['status']=='open'
  hold=row['defect_type'] in {'D04','D06','D09','D18'}
  row.update(unit_title='Height-integral initial pairs',status='open' if hold else 'done',date_utc=now,evidence=note,detail='Its earlier complete source review now has the actual following minimal-primary subsection, correctly placed after LU; four common gates remain.');closed+=not hold
assert(closed,added)==(100,112),(closed,added)
r.write_table(r.DEFECTS,df,ds);r.write_table(u.ROOT/'CHECK_EVENTS.tsv',ef,es);r.write_table(u.ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv',pf,ps)
print('UTC',now)
print('EXACT_DEFECT_ROWS',nd,'ATTRIBUTED_USED_EVENTS',ne)
print('SOURCE_CRITERIA_CLOSED',closed,'NEW_ACTUAL_UNIT_ROWS',added,'EXISTING_SCOPE_ROWS_REKEYED',len(old))
print('S5_MINIMAL_NEXT_BOUNDARIES_AND_COMMON_GATES_OPEN')

