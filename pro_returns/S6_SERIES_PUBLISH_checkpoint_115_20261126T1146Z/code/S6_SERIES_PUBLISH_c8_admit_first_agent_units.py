"""Admit the explicitly reviewed first elliptic units, with global gates open."""
from __future__ import annotations
from datetime import datetime, timezone
import S6_SERIES_PUBLISH_c8_integrate_units as u
import S6_SERIES_PUBLISH_c8_root_units as r

now=datetime.now(timezone.utc).isoformat()
evidence="agents/continuation8_iii_root/S6_SERIES_PUBLISH_III_first_agent_units_admission.md"
df,defects=r.table(r.DEFECTS)
ef,events=r.table(u.ROOT/'CHECK_EVENTS.tsv')
known_d={x['change_id'] for x in defects}
known_e={x['event_id'] for x in events}
defect_added=event_added=0
fdir=u.ROOT/'agents/continuation8_iii_foundations'
ldir=u.ROOT/'agents/continuation8_iii_later'
selected_labels={'mapsD:repair:collision-realization','maps:src:D.2.43','maps:src:D.2.47','maps:src:D.2.2','maps:src:D.2.3',*[f'maps:src:D.2.{i}' for i in range(5,10)]}
later_labels={f'maps:src:D.2.{i}' for i in [17,18,20,21,24,25,26,27,28]}
sources=[
 (fdir/'S6_SERIES_PUBLISH_c8_foundations_defects.tsv', fdir/'S6_SERIES_PUBLISH_c8_foundations_CHECK_EVENTS.tsv',True),
 (ldir/'S6_SERIES_PUBLISH_III_additive_publication_defects.tsv', ldir/'S6_SERIES_PUBLISH_III_additive_publication_CHECK_EVENTS.tsv',False),
 (ldir/'S6_SERIES_PUBLISH_III_spheres_publication_defects.tsv', ldir/'S6_SERIES_PUBLISH_III_spheres_publication_CHECK_EVENTS.tsv',False),
]
for dpath,epath,foundation in sources:
 _,local_d=r.table(dpath)
 for row in local_d:
  if foundation and not row['change_id'].startswith(('III-C8-FND-MARKED-','III-C8-FND-COHOM-','III-C8-FND-BASIC-')): continue
  assert row['change_id'] not in known_d,row['change_id']
  merged={k:row.get(k,'') for k in df}
  merged['review_status']=row.get('review_status','')+'; attributed whole-unit review and canonical placement admitted '+now+'; global references/program table/bibliography and final PDF gates open. '+evidence
  defects.append(merged);known_d.add(row['change_id']);defect_added+=1
 _,local_e=r.table(epath)
 for row in local_e:
  if foundation and row['statement_id'] not in selected_labels: continue
  if not foundation and row['statement_id'] not in later_labels: continue
  assert row['type']=='used and rechecked in this run'
  assert row['event_id'] not in known_e,row['event_id']
  merged={k:row.get(k,'') for k in ef}
  merged['outcome']=row['outcome']+' Root admitted the attributed publication reading and exact canonical placement; no second root whole-proof reading or additional independent check is claimed. '+evidence
  events.append(merged);known_e.add(row['event_id']);event_added+=1
assert defect_added==360,(defect_added,event_added)
assert event_added==19,(defect_added,event_added)

pf,progress=r.table(u.ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv')
specs=[
 ('mapsD:repair:collision-realization','Marked rational elliptic surfaces','mapsD:repair:modular-collisions',False),
 ('maps:src:D.2.43','Triangular caps and their integral homology',None,False),
 ('maps:src:D.2.47','Component intersections in triangular caps',None,False),
 ('maps:src:D.2.2','Integral cohomology, Euler numbers and clutching','maps:src:D.2.2',False),
 ('maps:src:D.2.5','The IV*+III+I1 profile',None,False),
 ('maps:src:D.2.6','The III*+3I1 profile',None,False),
 ('maps:src:D.2.7',"Wang's primitive I2 filling",None,False),
 ('maps:src:D.2.8','The oriented type of the Wang family',None,False),
 ('maps:src:D.2.9','The III*+II+I1 profile and the pending next boundary',None,True),
 ('maps:src:D.2.17','Two additive profiles',None,False),
 ('maps:src:D.2.18','The three-component cusp',None,False),
 ('maps:src:D.2.20','Six primitive original families',None,False),
 ('maps:src:D.2.21','A mixed original and logarithmic pair',None,False),
 ('maps:src:D.2.24','The I3-star homology obstruction',None,False),
 ('maps:src:D.2.25','All-multiplicative profiles',None,False),
 ('maps:src:D.2.26','Sixteen finite and multiplicative profiles',None,False),
 ('maps:src:D.2.27','The I1-star integral obstruction',None,False),
 ('maps:src:D.2.28','The classification over twenty-one profiles and pending next boundary',None,True),
]
closed=added=0
for ident,title,old_ident,hold_all in specs:
 if old_ident:
  selected=[x for x in progress if x['paper']=='III' and x['unit_id']==old_ident]
  assert len(selected)==28,(ident,len(selected))
 else:
  assert not any(x['paper']=='III' and x['unit_id']==ident for x in progress)
  selected=[]
  for criterion in [f'D{i:02d}' for i in range(1,28)]+['structure']:
   row={k:'' for k in pf}
   row.update(paper='III',unit_id=ident,row_kind='structure' if criterion=='structure' else 'defect',defect_type='' if criterion=='structure' else criterion,status='open')
   selected.append(row);progress.append(row);added+=1
 for row in selected:
  assert row['status']=='open'
  row.update(unit_id=ident,unit_title=title,date_utc=now,evidence=evidence)
  hold=hold_all or row['defect_type'] in {'D04','D06','D09','D18'} or (ident=='mapsD:repair:collision-realization' and row['defect_type']=='D12')
  row['status']='open' if hold else 'done'
  if hold_all:
   row['detail']='The finished fragment is canonical, but its last subsection still includes following unreviewed material until the next actual subsection boundary is applied; all current-unit criteria stay open.'
  elif hold:
   row['detail']='Global current-edition references, program-table placement/pin or bibliography remains open; OG D12 also awaits replacement of the duplicate KM period paragraph. Exact remaining gate in root admission note.'
  else:
   row['detail']='Complete attributed before/after proof and all-register source review admitted; actual bounded subsection placed in prerequisite order. No credit from the split, helper or identity check.'
   closed+=1
assert closed==383,closed
assert added==448,added
r.write_table(r.DEFECTS,df,defects)
r.write_table(u.ROOT/'CHECK_EVENTS.tsv',ef,events)
r.write_table(u.ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv',pf,progress)
print('UTC',now)
print('EXACT_LOCAL_DEFECT_ROWS_MERGED',defect_added)
print('ATTRIBUTED_USED_AND_RECHECKED_EVENTS',event_added)
print('SOURCE_CRITERIA_CLOSED_AFTER_WHOLE_UNIT_REVIEW',closed)
print('NEW_ACTUAL_UNIT_ROWS',added)
print('LZ_AND_L3_ALL_CRITERIA_OPEN_UNTIL_NEXT_BOUNDARY')
print('GLOBAL_REFERENCE_PROGRAM_BIBLIOGRAPHY_BUILD_PAGE_GATES_OPEN')
