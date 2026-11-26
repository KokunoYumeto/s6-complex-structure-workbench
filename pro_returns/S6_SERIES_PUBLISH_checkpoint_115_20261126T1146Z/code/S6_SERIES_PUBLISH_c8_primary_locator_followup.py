"""Apply three precise, evidenced source locators without changing mathematics."""
from datetime import datetime, timezone
import S6_SERIES_PUBLISH_c8_integrate_units as u
import S6_SERIES_PUBLISH_c8_root_units as r

changes=[
 ('retained_angle',r'\cite{Johnson1980Root}',r'\cite[Theorem~3A, p.~371]{Johnson1980Root}',
  'The complete attached c4 02J7_source_reading.md records the actual rendered p371 and complete Theorem3A proof, with canonical-lift pp366/368 and Lemma3 p372. Bibliography editor reread that complete record. This is inherited primary evidence with its stated scope, not a new primary opening.'),
 ('elliptic_finite_multiplicities',r'\cite[Proposition 3.1]{manYang26}',r'\cite[Proposition~3.1, p.~11]{manYang26}',
  'Bibliography editor read the full Proposition3.1 statement/proof in exact Yang v1 p11. Same elliptic j-function and same actual period-marking application.'),
 ('elliptic_finite_multiplicities',r'\cite[Appendix~B.4]{manYang26}',r'\cite[Theorem~4.8, pp.~22--23; Corollary~4.13, p.~25]{manYang26}',
  'The complete opened AppendixB.4 pp65-67 concerns boundary/sweep chains. The actual geometric cusp owner is Theorem4.8 and Corollary4.13 at r=1, whose full statements/proofs were read by the bibliography editor, with Lemma4.5 p21. The preceding proof already identifies the primitive index-one Type C family by its actual periods and integral marking; the claimed one normalized dP6 component is unchanged.')]
source=u.repairs.SOURCE.read_text();candidate=source
df,ds=r.table(r.DEFECTS);ef,es=r.table(u.ROOT/'CHECK_EVENTS.tsv')
for i,(key,before,after,reason) in enumerate(changes,1):
 p=u.WORK/u.BY_KEY[key].owner/(key+'.tex');old=p.read_text()
 assert old.count(before)==1 and candidate.count(old)==1
 new=old.replace(before,after,1);u.check_permanent_identifiers(old,new,set(),set())
 line=old[:old.index(before)].count('\n')+1
 ident=f'III-C8-PRIMARY-LOCATOR-FOLLOWUP-{i:02d}'
 assert not any(x['change_id']==ident for x in ds)
 ds.append(dict(change_id=ident,type='D06',statement_id=key,old_location=str(p.relative_to(u.ROOT))+':'+str(line),old_page='pending page concordance',new_location=str(p.relative_to(u.ROOT))+':'+str(line),new_page='pending final PDF',old_text=before,new_text=after,reason=reason,review_status='actual application context and precise supporting source correspondence read; bounded actual readback pending; final bibliography admission remains open'))
 candidate=candidate.replace(old,new,1);p.write_text(new,encoding='utf-8',newline='\n')
 print('EXACT_CHANGE',p.relative_to(u.ROOT),line);print('OLD',before);print('NEW',after)
u.check_permanent_identifiers(source,candidate,set(),set())
now=datetime.now(timezone.utc).isoformat();eid='publish:c8:III:primary-locator-followup'
assert not any(x['event_id']==eid for x in es)
row={k:'' for k in ef}
row.update(statement_id='III:primary-citation-locators',date='2026-11-25',who='GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; numerical effort not separately exposed; continuation eight root',type='used and rechecked in this run',outcome='Read the bounded Johnson spin-form and Yang j/cusp application contexts, and the exact supporting source-reading reports. Three locator corrections preserve all actual mathematical maps and conclusions. Primary opening/record-reading attribution stays with the bibliography editor. No independent, required or criterion credit.',event_id=eid,phase='continuation8 publication reference integration',source_file='code/S6_SERIES_PUBLISH_c8_primary_locator_followup.py',source_event_type='used and rechecked in this run',evidence_group=eid,date_utc=now,where='code/S6_SERIES_PUBLISH_c8_primary_locator_followup.out')
es.append(row)
u.repairs.SOURCE.write_text(candidate,encoding='utf-8',newline='\n')
r.write_table(r.DEFECTS,df,ds);r.write_table(u.ROOT/'CHECK_EVENTS.tsv',ef,es)
print('UTC',now,'EXACT_DEFECT_ROWS',3,'ROOT_USED_EVENTS',1,'NO_CRITERION_INCREMENT')
