"""Admit complete extension/named units and attributed smooth-logarithmic units."""
from datetime import datetime,timezone
import S6_SERIES_PUBLISH_c8_integrate_units as u
import S6_SERIES_PUBLISH_c8_root_units as r
now=datetime.now(timezone.utc).isoformat()
rr='agents/continuation8_iii_root/S6_SERIES_PUBLISH_III_extension_named_units_review.md'
fr='agents/continuation8_iii_root/S6_SERIES_PUBLISH_III_smooth_logs_admission.md'
df,ds=r.table(r.DEFECTS);ef,es=r.table(u.ROOT/'CHECK_EVENTS.tsv')
pf,ps=r.table(u.ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv')
f=u.ROOT/'agents/continuation8_iii_foundations'
nd=ne=0
for row in r.table(f/'S6_SERIES_PUBLISH_c8_foundations_defects.tsv')[1]:
 if not row['change_id'].startswith('C8-FND-SMOOTH-'):continue
 assert not any(x['change_id']==row['change_id'] for x in ds)
 out={k:row.get(k,'') for k in df}
 out['review_status']=row.get('review_status','')+'; attributed complete source-unit admission '+now+'; four common source gates and final PDF open. '+fr
 ds.append(out);nd+=1
smooth_labels={'maps:src:D.2.13','maps:src:D.2.14','mapsIII:def:smooth-logarithmic-data','mapsIII:def:twisted-smale-suspension'}
for row in r.table(f/'S6_SERIES_PUBLISH_c8_foundations_CHECK_EVENTS.tsv')[1]:
 if row['statement_id'] not in smooth_labels:continue
 assert row['type']=='used and rechecked in this run'
 assert not any(x['event_id']==row['event_id'] for x in es)
 out={k:row.get(k,'') for k in ef}
 out['outcome']=row['outcome']+' Root read both complete reviews and actual placement outputs; underlying whole-proof and primary-page readings remain attributed, with no second root reading or independent credit. '+fr
 es.append(out);ne+=1
assert (nd,ne)==(58,4),(nd,ne)
for row in ds:
 if row['change_id'].startswith(('III-C8-EXT-NAMED-READBACK-','III-C8-NAMED-','III-C8-EXTENSION-')):
  row['review_status']='Root completed the whole preceding/current proof comparison and final exact context readbacks; final references/bibliography/PDF gates remain as recorded. '+rr
outcomes={
 'mapsIII:def:torus-extension-data':'The whole old hypothesis block and numbered definition were compared, including the precise restriction h|U and all compactness/frontier/basepoint data.',
 'mapsIII:carrier-extension-lemma':'The whole old/current proof and complete c4 comparison were read. Both homotopy stages, uniform endpoint continuity and fixed exterior/basepoint remain exactly.',
 'maps:src:B.3.2':'Bounded follow-up to the already wholly read J8 proof: the entire revised proof was read against the whole Q8 proof, with the exact period cover, collar correction, target maps and unreduced rotation retained. No second independent check.',
 'mapsIII:angle-forgotten-one-copy-null':'The whole preceding extension/smash proof, complete c5 comparison and entire final source were read. The exact based J8 homotopy now supplies every positive smash power, including one, with full quotient continuity.',
 'mapsIII:def:three-sphere-families':'All old input paragraphs and the entire numbered definition were compared. The three marked family scopes, lattice table, finite parameters, signed sphere condition and prescribed product-cell/suspension maps are unchanged.',
 'maps:src:B.4.1':'Whole preceding/current proof and both complete c5 comparison/source records were read, including recovered output and every final context. Complete family-specific inverse lattices, finite/cusp geometry, frame transfer, marked torus and parameter scopes remain; exact common contraction and homotopy inputs now have sole earlier owners.',
 'mapsIII:rem:three-family-quotient-class':'The full old final sentence and new numbered remark were compared. The exact distinct-member statement and class 6nu-prime are retained without stronger classification wording.'
}
for label,outcome in outcomes.items():
 eid='publish:c8:III:extension-named:'+label
 assert not any(x['event_id']==eid for x in es)
 row={k:'' for k in ef};row.update(statement_id=label,date='2026-11-25',who='GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; numerical effort not separately exposed; continuation eight, root',type='used and rechecked in this run',outcome=outcome+' No new independent-check or final-page credit.',event_id=eid,phase='continuation8 publication unit comparison',source_file=rr,source_event_type='used and rechecked in this run',evidence_group='publish:c8:III:extension-named',date_utc=now,where=rr);es.append(row)
closed=added=0
for ident,title,holds,evidence in [
 ('mapsIII:carrier-extension-section','Smash powers of the angle-forgetting maps',set(),rr),
 ('maps:src:B.4.1','Quotient maps in three sphere-fibration families',{'D04','D06','D09','D18'},rr),
]:
 selected=[x for x in ps if x['paper']=='III' and x['unit_id']==ident]
 assert len(selected)==28 and all(x['status']=='open' for x in selected),(ident,len(selected))
 for row in selected:
  criterion='structure' if row['row_kind']=='structure' else row['defect_type']
  hold=criterion in holds
  row.update(unit_title=title,status='open' if hold else 'done',date_utc=now,evidence=evidence,detail='Common cross-paper/program/bibliography gate remains open.' if hold else 'Whole preceding/current unit and admitted comparison read with all28 criteria; actual subsection boundary present; final PDF gate separate.')
  closed+=not hold
for ident,title,holds,evidence in [
 ('mapsIII:carrier-extension-lemma','Suspension homotopies from torus extensions',{'D18'},rr),
 ('maps:src:D.2.13','Integral homology of smooth logarithmic modifications',{'D04','D06','D09','D18'},fr),
 ('maps:src:D.2.14','Twisted suspensions and oriented smooth types',{'D04','D06','D09','D18'},fr),
]:
 assert not any(x['paper']=='III' and x['unit_id']==ident for x in ps),ident
 for criterion in [f'D{i:02d}' for i in range(1,28)]+['structure']:
  hold=criterion in holds
  row={k:'' for k in pf}
  row.update(paper='III',unit_id=ident,unit_title=title,row_kind='structure' if criterion=='structure' else 'defect',defect_type='' if criterion=='structure' else criterion,status='open' if hold else 'done',date_utc=now,evidence=evidence,detail='Common reference/program/bibliography gate remains open.' if hold else 'Complete whole-source publication comparison admitted with all28 findings and actual canonical subsection boundaries; final build/page gates separate.')
  ps.append(row);added+=1;closed+=not hold
for row in ps:
 if row['paper']=='III' and row['unit_id']=='maps:src:B.3.1' and (row['defect_type']=='D12' or row['row_kind']=='structure'):
  assert row['status']=='open'
  row.update(status='done',date_utc=now,evidence=rr,detail='Full Q8/J8/Q7/JA comparison identifies the exact common homotopies and their inverses/input maps; all family-specific geometry retained.');closed+=1
 if row['paper']=='III' and row['unit_id'] in {'maps:src:D.2.19','maps:src:D.2.22'} and (row['defect_type']=='D14' or row['row_kind']=='structure'):
  assert row['status']=='done'
  row.update(date_utc=now,evidence=fr,detail='Actual order KM, KN, KO, KT, KX, KY now supplies every geometric prerequisite; evidence corrected without new completion credit.')
assert (closed,added)==(129,84),(closed,added)
r.write_table(r.DEFECTS,df,ds);r.write_table(u.ROOT/'CHECK_EVENTS.tsv',ef,es);r.write_table(u.ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv',pf,ps)
print('UTC',now)
print('SMOOTH_DEFECT_ROWS',nd,'ATTRIBUTED_EVENTS',ne,'ROOT_USED_EVENTS',len(outcomes))
print('SOURCE_CRITERIA_CLOSED',closed,'NEW_ACTUAL_UNIT_ROWS',added)
print('KY_NEXT_BOUNDARY_AND_COMMON_GATES_REMAIN_OPEN; NO_INDEPENDENT_CHECK_CREDIT')

