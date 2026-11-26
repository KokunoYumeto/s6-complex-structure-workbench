"""Admit KP/KQ and correct the recorded actual dependency-order chronology."""
from datetime import datetime,timezone
import S6_SERIES_PUBLISH_c8_integrate_units as u
import S6_SERIES_PUBLISH_c8_root_units as r
now=datetime.now(timezone.utc).isoformat()
note='agents/continuation8_iii_root/S6_SERIES_PUBLISH_III_product_star_admission.md'
df,ds=r.table(r.DEFECTS);ef,es=r.table(u.ROOT/'CHECK_EVENTS.tsv')
pf,ps=r.table(u.ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv')
f=u.ROOT/'agents/continuation8_iii_foundations';nd=ne=0
for row in r.table(f/'S6_SERIES_PUBLISH_c8_foundations_defects.tsv')[1]:
 if not row['change_id'].startswith('C8-FND-PRODUCT-STAR-'):continue
 assert not any(x['change_id']==row['change_id'] for x in ds)
 out={k:row.get(k,'') for k in df};out['review_status']=row.get('review_status','')+'; complete attributed publication-unit review and corrected canonical prerequisite order admitted '+now+'; common gates open. '+note
 ds.append(out);nd+=1
for row in r.table(f/'S6_SERIES_PUBLISH_c8_foundations_CHECK_EVENTS.tsv')[1]:
 if row['statement_id'] not in {'maps:src:D.2.15','maps:src:D.2.16','mapsIII:def:two-component-os56','mapsIII:def:odd-star-logarithmic-data'}:continue
 assert row['type']=='used and rechecked in this run'
 assert not any(x['event_id']==row['event_id'] for x in es)
 out={k:row.get(k,'') for k in ef};out['outcome']=row['outcome']+' Root read the full unit reviews and actual corrected placement; whole proof/primary readings remain attributed and no extra independent credit is added. '+note
 es.append(out);ne+=1
assert(nd,ne)==(92,4),(nd,ne)
eid='publish:c8:III:foundations:actual-order-correction'
assert not any(x['event_id']==eid for x in es)
row={k:'' for k in ef};row.update(statement_id='maps:src:D.2.10; maps:src:D.2.11; maps:src:D.2.12; maps:src:D.2.13; maps:src:D.2.14; maps:src:D.2.19; maps:src:D.2.22; maps:src:D.2.23; maps:src:D.2.15; maps:src:D.2.16',date='2026-11-25',who='GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; numerical effort not separately exposed; continuation eight, root',type='used and rechecked in this run',outcome='Bounded actual dependency-order inspection found that an earlier catalogue move had left KK/KL/KM later. Their unchanged complete fragments were moved before KN/KO at 18:14:22 UTC. The exact current ranges were then read, including LO before KP. Earlier premature placement wording is corrected explicitly. No whole-proof, new theorem, independent-check or completion-count credit.',event_id=eid,phase='continuation8 publication dependency order',source_file=note,source_event_type='used and rechecked in this run',evidence_group='publish:c8:III:foundations-order',date_utc=now,where=note);es.append(row)
closed=added=0
for ident,title in [('maps:src:D.2.15','Logarithmic families with smooth type S2 x S4'),('maps:src:D.2.16','Odd-star fillings and regular logarithmic transformations')]:
 assert not any(x['paper']=='III' and x['unit_id']==ident for x in ps)
 for c in [f'D{i:02d}' for i in range(1,28)]+['structure']:
  hold=c in {'D04','D06','D09','D18'};row={k:'' for k in pf}
  row.update(paper='III',unit_id=ident,unit_title=title,row_kind='structure' if c=='structure' else 'defect',defect_type='' if c=='structure' else c,status='open' if hold else 'done',date_utc=now,evidence=note,detail='Common reference/program/bibliography gate open.' if hold else 'Complete attributed whole-source review and all28 findings admitted; actual earlier prerequisites and next subsection/section boundaries read.')
  ps.append(row);added+=1;closed+=not hold
for row in ps:
 if row['paper']=='III' and row['unit_id']=='maps:src:D.2.23':
  assert row['status']=='open';hold=row['defect_type'] in {'D04','D06','D09','D18'}
  row.update(unit_title='Fundamental groups of natural section-line families',status='open' if hold else 'done',date_utc=now,evidence=note,detail='Its complete prior source review now has the actual following KP subsection; four common gates remain.');closed+=not hold
 if row['paper']=='III' and row['unit_id'] in {'maps:src:D.2.10','maps:src:D.2.11','maps:src:D.2.12','maps:src:D.2.13','maps:src:D.2.14','maps:src:D.2.19','maps:src:D.2.22'} and (row['defect_type']=='D14' or row['row_kind']=='structure'):
  assert row['status']=='done'
  row.update(date_utc=now,evidence=note,detail='Actual complete order read after the 18:14:22 correction: marked data/LO, cohomology, basic families, KK/KL, KM, KN/KO, catalogue, KP/KQ. Earlier placement chronology corrected without added completion credit.')
assert(closed,added)==(72,56),(closed,added)
r.write_table(r.DEFECTS,df,ds);r.write_table(u.ROOT/'CHECK_EVENTS.tsv',ef,es);r.write_table(u.ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv',pf,ps)
prior=u.ROOT/'agents/continuation8_iii_root/S6_SERIES_PUBLISH_III_smooth_logs_admission.md'
t=prior.read_text()
add='\n## Later actual-order correction\n\nThe KM-before-KN statement above was premature when this note was written. The bounded actual source-order inspection and content-preserving correction at 18:14:22 UTC are recorded in '+note+'. The verified complete order there supersedes that earlier chronology; no new proof or criterion credit comes from correcting the move.\n'
assert '## Later actual-order correction' not in t
prior.write_text(t+add,encoding='utf-8',newline='\n')
print('UTC',now);print('EXACT_DEFECT_ROWS',nd,'ATTRIBUTED_USED_EVENTS',ne,'BOUNDED_ORDER_EVENT',1)
print('SOURCE_CRITERIA_CLOSED',closed,'NEW_ACTUAL_UNIT_ROWS',added)
print('PRIOR_PLACEMENT_CHRONOLOGY_CORRECTED; COMMON_AND_PDF_GATES_OPEN')

