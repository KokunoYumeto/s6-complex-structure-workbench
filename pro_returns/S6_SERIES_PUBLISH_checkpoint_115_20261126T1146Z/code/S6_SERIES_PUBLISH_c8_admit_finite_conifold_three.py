"""Admit the completed finite-cap, conifold and three-primary publication readings."""
from datetime import datetime, timezone
import S6_SERIES_PUBLISH_c8_integrate_units as u
import S6_SERIES_PUBLISH_c8_root_units as r

now=datetime.now(timezone.utc).isoformat()
note='agents/continuation8_iii_root/S6_SERIES_PUBLISH_III_finite_conifold_three_admission.md'
df,ds=r.table(r.DEFECTS);ef,es=r.table(u.ROOT/'CHECK_EVENTS.tsv')
pf,ps=r.table(u.ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv')
nd=ne=0
inputs=[
 ('continuation8_iii_foundations','S6_SERIES_PUBLISH_c8_foundations_defects.tsv','S6_SERIES_PUBLISH_c8_foundations_CHECK_EVENTS.tsv',89,7),
 ('continuation8_iii_later','S6_SERIES_PUBLISH_III_conifold_publication_defects.tsv','S6_SERIES_PUBLISH_III_conifold_publication_CHECK_EVENTS.tsv',29,5),
 ('continuation8_iii_weighted_units','S6_SERIES_PUBLISH_THREE_publication_defects.tsv','S6_SERIES_PUBLISH_THREE_CHECK_EVENTS.tsv',916,4)]
for lane,dfile,efile,expected_d,expected_e in inputs:
 folder=u.ROOT/'agents'/lane
 selected=r.table(folder/dfile)[1]
 events=r.table(folder/efile)[1]
 if lane=='continuation8_iii_foundations':
  selected=[x for x in selected if x['change_id'].startswith('C8-FND-FINITE-CAPS-')]
  events=[x for x in events if x['statement_id'] in {'maps:src:D.2.29','maps:src:D.2.30','mapsIII:def:primitive-fixed-finite-data','mapsIII:rem:finite-torsion-examples','mapsIII:rem:primitive-finite-calculations','mapsIII:def:general-finite-additive-data','mapsIII:rem:general-finite-calculations'}]
 assert(len(selected),len(events))==(expected_d,expected_e),(lane,len(selected),len(events))
 for row in selected:
  assert not any(x['change_id']==row['change_id'] for x in ds)
  out={k:row.get(k,'') for k in df};out['review_status']=row.get('review_status','')+'; complete attributed review and exact canonical placement admitted '+now+'; actual-unit/global gate limits: '+note
  ds.append(out);nd+=1
 for row in events:
  assert row['type']=='used and rechecked in this run'
  assert not any(x['event_id']==row['event_id'] for x in es)
  out={k:row.get(k,'') for k in ef};out['outcome']=row['outcome']+' Root read the complete substantive review and all-criterion evidence, plus the final MK proof; other full-proof readings remain attributed. No new independent-check credit. Actual boundaries and holds: '+note
  es.append(out);ne+=1
assert(nd,ne)==(1034,16)
closed=added=0
def disposition(c,complete):
 return 'done' if complete and c not in {'D04','D06','D09','D18'} else 'open'
def add(ident,title,complete):
 global closed,added
 assert not any(x['paper']=='III' and x['unit_id']==ident for x in ps)
 for c in [f'D{i:02d}' for i in range(1,28)]+['structure']:
  status=disposition(c,complete);row={k:'' for k in pf}
  row.update(paper='III',unit_id=ident,unit_title=title,row_kind='structure' if c=='structure' else 'defect',defect_type='' if c=='structure' else c,status=status,date_utc=now,evidence=note,detail='Full attributed predecessor/current proof and all criteria admitted. '+('Actual next subsection/section is present; four common gates remain.' if complete else 'All criteria held until the unreviewed following text receives its completed actual-unit boundary.'))
  ps.append(row);added+=1;closed+=status=='done'
for ident,title,complete in [
 ('maps:src:D.2.29','Finite caps with a primitive contracting period',True),
 ('maps:src:D.2.30','All finite additive lattices and affine twists',False),
 ('maps:src:D.3.3','Complex invariants of the smoothing',True),
 ('maps:src:D.3.4','Comparison with Calabi–Eckmann deformations',True),
 ('maps:src:E.2.2','Transverse pullbacks of the sphere fibration',True),
 ('maps:src:D.2.39','Three-primary smooth types and pending next boundary',False)]:add(ident,title,complete)
existing={
 'maps:src:D.2.28':'Classification over twenty-one elliptic profiles',
 'maps:src:D.2.35':'Minimal primary smooth types',
 'maps:src:D.3.1':'Moving the zero of the linearization',
 'maps:src:D.3.2':'Topology of the smoothing'}
for ident,title in existing.items():
 rows=[x for x in ps if x['paper']=='III' and x['unit_id']==ident]
 assert len(rows)==28 and all(x['status']=='open' for x in rows),ident
 for row in rows:
  c=row['defect_type'] or 'structure';status=disposition(c,True)
  row.update(unit_title=title,status=status,date_utc=now,evidence=note,detail='The complete admitted proof unit now has its actual following subsection/section. Four common reference/program/bibliography gates remain; no heading-only credit.')
  closed+=status=='done'
assert(closed,added)==(192,168),(closed,added)
r.write_table(r.DEFECTS,df,ds);r.write_table(u.ROOT/'CHECK_EVENTS.tsv',ef,es);r.write_table(u.ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv',pf,ps)
print('UTC',now);print('EXACT_DEFECT_ROWS',nd,'ATTRIBUTED_USED_EVENTS',ne)
print('SOURCE_CRITERIA_CLOSED',closed,'NEW_ACTUAL_UNIT_ROWS',added)
print('L6_AND_THREE_PRIMARY_ALL28_HELD; COMMON_REFERENCE_PROGRAM_BIBLIOGRAPHY_AND_FINAL_PAGES_OPEN')
