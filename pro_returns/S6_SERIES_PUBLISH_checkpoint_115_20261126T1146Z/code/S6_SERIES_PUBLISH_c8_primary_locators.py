"""Apply exact version-matched citation owners and the newly read page locators."""
from datetime import datetime, timezone
import re
import S6_SERIES_PUBLISH_c8_integrate_units as u
import S6_SERIES_PUBLISH_c8_root_units as r

mapping={'mapsLR':'manLR26','mapsVia2':'manViaclovskyTwo26','mapsViaLog':'manViaclovskyLogs26'}
pattern=re.compile(r'\\cite(?:\[[^\]]*\])?\{([^}]+)\}')
source=u.repairs.SOURCE.read_text();candidate=source
df,ds=r.table(r.DEFECTS);ef,es=r.table(u.ROOT/'CHECK_EVENTS.tsv')
updates=[];changes=[];counts={k:0 for k in mapping}
for key in ['named_fibrations','retained_angle','os49_construction','elliptic_finite_multiplicities']:
 p=u.WORK/u.BY_KEY[key].owner/(key+'.tex');old=p.read_text();new=old
 if key=='named_fibrations':
  def sub(m):
   k=m.group(1)
   if k not in mapping:return m.group(0)
   after=m.group(0)[:-len(k)-1]+mapping[k]+'}'
   changes.append((p,old[:m.start()].count('\n')+1,m.group(0),after,'Same exact opened archive version: LR2609.33826v2; two-parameter2609.33785v1; logarithmic2610.39102v1. The identity map on the source edition with the same statement/equation locator identifies the application. Exact primary openings and bytes are in the bibliography review.'))
   counts[k]+=1;return after
  new=pattern.sub(sub,new)
  pairs=[
   ('Propositions~3.12--3.13, pp.~12--14','Propositions~3.12--3.13, pp.~13--14'),
   ('Proposition~3.12, pp.~12--13','Proposition~3.12, pp.~13--14'),
   ('Lemma~3.10, pp.~10--11','Lemma~3.10, pp.~11--12')]
  for before,after in pairs:
   assert new.count(before)==1
   line=new[:new.index(before)].count('\n')+1
   changes.append((p,line,before,after,'LR v2 complete pp11-14 and full Theorem5.1 p21 were read by the bibliography editor; exact same-v2 hash agrees with the attached c5 record. These are the actual printed lemma/proposition pages. Proposition2.12/Definition2.13 pp7-8 was separately read and its locator remains unchanged.'))
   new=new.replace(before,after,1)
 elif key=='retained_angle':
  for before,after in [
   ('\\cite[Theorem 3.2 and Remark 3.3]{DebrayGunningham2018Root}','\\cite[Theorem~3.2 and Remark~3.3, p.~6]{DebrayGunningham2018Root}'),
   ('\\cite[Theorem 3.6]{DebrayGunningham2018Root}','\\cite[Theorem~3.6, p.~6]{DebrayGunningham2018Root}')]:
   assert new.count(before)==1
   line=new[:new.index(before)].count('\n')+1
   changes.append((p,line,before,after,'Exact arXiv1803.11183v1 dated30 March2018: complete p6 text and rendered image read by bibliography editor; these statements and the already located Example3.8 share that page. Mathematical statement/locator identity is unchanged.'))
   new=new.replace(before,after,1)
 else:
  for number,page in [('3.4','13'),('3.6','14')]:
   before='\\cite[Proposition '+number+']{manYang26}';after='\\cite[Proposition~'+number+', p.~'+page+']{manYang26}'
   assert new.count(before)==1
   line=new[:new.index(before)].count('\n')+1
   changes.append((p,line,before,after,'Yang exact v1 complete pp13-14 read as text and rendered images by bibliography editor. Proposition3.4 is p13 and Proposition3.6 p14. The same named result and its actual application maps are unchanged.'))
   new=new.replace(before,after,1)
 assert new!=old
 u.check_permanent_identifiers(old,new,set(),set())
 assert candidate.count(old)==1,key
 candidate=candidate.replace(old,new,1);updates.append((p,new))
assert counts=={'mapsLR':5,'mapsVia2':4,'mapsViaLog':5},counts
assert len(changes)==23,len(changes)
u.check_permanent_identifiers(source,candidate,set(),set())
for i,(p,line,before,after,reason) in enumerate(changes,1):
 ident=f'III-C8-PRIMARY-LOCATORS-{i:03d}'
 assert not any(x['change_id']==ident for x in ds)
 ds.append(dict(change_id=ident,type='D06',statement_id=p.stem,old_location=str(p.relative_to(u.ROOT))+':'+str(line),old_page='pending page concordance',new_location=str(p.relative_to(u.ROOT))+':'+str(line),new_page='pending final PDF',old_text=before,new_text=after,reason=reason,review_status='root read every affected application context and exact version/page correspondence; actual changed-token output pending read; final bibliography source-event admission remains open'))
now=datetime.now(timezone.utc).isoformat()
eid='publish:c8:III:exact-edition-page-locators'
assert not any(x['event_id']==eid for x in es)
event={k:'' for k in ef}
event.update(statement_id='III:primary-citation-locators',date='2026-11-25',who='GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; numerical effort not separately exposed; continuation eight root',type='used and rechecked in this run',outcome='Read every bounded JA/Yang/retained application context and exact editor-reported primary edition/page correspondence. Apply14 same-edition citation aliases,3 corrected LR ranges,4 Yang pages and2 Debray pages. Exact source-opening scope remains attributed to bibliography editor; no new root primary opening, independent proof, required check or criterion closure.',event_id=eid,phase='continuation8 publication reference integration',source_file='code/S6_SERIES_PUBLISH_c8_primary_locators.py',source_event_type='used and rechecked in this run',evidence_group=eid,date_utc=now,where='code/S6_SERIES_PUBLISH_c8_primary_locators.out')
es.append(event)
for p,new in updates:p.write_text(new,encoding='utf-8',newline='\n')
u.repairs.SOURCE.write_text(candidate,encoding='utf-8',newline='\n')
r.write_table(r.DEFECTS,df,ds);r.write_table(u.ROOT/'CHECK_EVENTS.tsv',ef,es)
print('UTC',now)
for p,line,before,after,reason in changes:
 print('EXACT_CHANGE',p.relative_to(u.ROOT),line);print('OLD',before);print('NEW',after)
print('CITATION_OWNER_COUNTS',counts,'EXACT_DEFECT_ROWS',len(changes),'ROOT_USED_EVENTS',1)
print('ALL_OLD_IDENTITIES_PRESERVED; NO_MATHEMATICAL_OR_CRITERION_INCREMENT')
