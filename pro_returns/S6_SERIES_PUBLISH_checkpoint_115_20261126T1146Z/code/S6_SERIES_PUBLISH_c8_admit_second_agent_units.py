"""Admit completed attributed source reviews, preserving open unit boundaries."""
from datetime import datetime, timezone
import S6_SERIES_PUBLISH_c8_integrate_units as u
import S6_SERIES_PUBLISH_c8_root_units as r
now=datetime.now(timezone.utc).isoformat()
evidence='agents/continuation8_iii_root/S6_SERIES_PUBLISH_III_second_agent_units_admission.md'
df,ds=r.table(r.DEFECTS);ef,es=r.table(u.ROOT/'CHECK_EVENTS.tsv')
known_d={x['change_id'] for x in ds};known_e={x['event_id'] for x in es}
nd=ne=0
def merge_d(path,predicate=lambda x:True):
 global nd
 for row in r.table(path)[1]:
  if not predicate(row): continue
  assert row['change_id'] not in known_d,row['change_id']
  out={k:row.get(k,'') for k in df}
  out['review_status']=row.get('review_status','')+'; attributed complete publication review and exact canonical placement admitted '+now+'; global reference/program/bibliography/PDF gates remain. '+evidence
  ds.append(out);known_d.add(row['change_id']);nd+=1
def merge_e(path,predicate=lambda x:True):
 global ne
 for row in r.table(path)[1]:
  if not predicate(row): continue
  assert row['type']=='used and rechecked in this run'
  assert row['event_id'] not in known_e,row['event_id']
  out={k:row.get(k,'') for k in ef}
  out['outcome']=row['outcome']+' Root admits this attributed reading and exact source placement; no additional root whole-proof reading or independent-check credit. '+evidence
  es.append(out);known_e.add(row['event_id']);ne+=1
w=u.ROOT/'agents/continuation8_iii_weighted_units'
for key in ['LN','LQ','LS','LT','LU']:
 merge_d(w/f'S6_SERIES_PUBLISH_{key}_publication_defects.tsv')
 merge_e(w/f'S6_SERIES_PUBLISH_{key}_CHECK_EVENTS.tsv')
assert nd==538 and ne==10,(nd,ne)
f=u.ROOT/'agents/continuation8_iii_foundations'
merge_d(f/'S6_SERIES_PUBLISH_c8_foundations_defects.tsv',lambda x:x['change_id'].startswith(('III-C8-FND-FINITE-','c8-III-foundations-KM-')))
merge_e(f/'S6_SERIES_PUBLISH_c8_foundations_CHECK_EVENTS.tsv',lambda x:x['event_id'] not in known_e and (':Q1' in x['event_id'] or x['statement_id'] in {'maps:src:D.2.10','maps:src:D.2.11','maps:src:D.2.12'}))
merge_e(u.ROOT/'agents/continuation8_iii_later/S6_SERIES_PUBLISH_III_formal_publication_CHECK_EVENTS.tsv')
assert nd==615 and ne==31,(nd,ne)
pf,p=r.table(u.ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv')
specs=[
 ('maps:src:D.2.46','Whole-fibre initial pairs',False,set()),
 ('maps:src:D.2.49','Canonical star logarithms',False,set()),
 ('maps:src:D.2.50','Vertical corrections',False,set()),
 ('maps:src:D.2.51','Invariant-Chern additive caps',False,set()),
 ('maps:src:D.2.52','Height-integral initial pairs and pending next boundary',True,set()),
 ('maps:src:D.2.10',"Finite multiplicities in Yang's two families",False,set()),
 ('maps:src:D.2.11','A component-supported zero on the IV*+II+I2 profile',False,{'D12','D14','D20','structure'}),
 ('maps:src:D.2.12','Seven elliptic profiles and pending next boundary',True,set()),
]
closed=added=0
for ident,title,hold_all,extra in specs:
 assert not any(x['paper']=='III' and x['unit_id']==ident for x in p)
 for c in [f'D{i:02d}' for i in range(1,28)]+['structure']:
  hold=hold_all or c in {'D04','D06','D09','D18'}|extra
  row={k:'' for k in pf}
  row.update(paper='III',unit_id=ident,unit_title=title,row_kind='structure' if c=='structure' else 'defect',defect_type='' if c=='structure' else c,status='open' if hold else 'done',date_utc=now,evidence=evidence,detail='Whole attributed proof/criterion review admitted; following unreviewed text still belongs to this actual unit until its next subsection boundary.' if hold_all else 'Global reference/program/bibliography gates and the explicitly retained KL construction comparison remain open.' if hold else 'Complete attributed preceding/current proof and every criterion reviewed; actual bounded subsection applied. No credit from a split or source-application helper.')
  p.append(row);added+=1;closed+=not hold
for row in p:
 if row['paper']=='III' and row['unit_id']=='maps:src:D.2.9':
  assert row['status']=='open'
  hold=row['defect_type'] in {'D04','D06','D09','D18'}
  row.update(unit_title='The III*+II+I1 profile',status='open' if hold else 'done',date_utc=now,evidence=evidence,detail='The complete earlier source-unit review now has its actual next KK subsection boundary; four global gates remain.')
  closed+=not hold
 if row['paper']=='III' and row['unit_id']=='mapsD:repair:collision-realization' and row['defect_type']=='D12':
  assert row['status']=='open'
  row.update(status='done',date_utc=now,evidence=evidence,detail='The canonical KM proof now uses Q102 through the explicit period map and inverse; the complete shared period proof has one owner.')
  closed+=1
assert closed==165 and added==224,(closed,added)
r.write_table(r.DEFECTS,df,ds);r.write_table(u.ROOT/'CHECK_EVENTS.tsv',ef,es)
r.write_table(u.ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv',pf,p)
print('UTC',now)
print('EXACT_DEFECT_ROWS_MERGED',nd)
print('ATTRIBUTED_USED_AND_RECHECKED_EVENTS',ne)
print('SOURCE_CRITERIA_CLOSED',closed,'NEW_ACTUAL_UNIT_ROWS',added)
print('KM_LU_NEXT_BOUNDARIES_AND_KL_GEOMETRIC_COMPARISON_OPEN')
