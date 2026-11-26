"""Correct the actual Kummer boundary and reopen the discovered proof overlap."""
from datetime import datetime,timezone
from collections import Counter
import re
import S6_SERIES_PUBLISH_c8_integrate_units as u
import S6_SERIES_PUBLISH_c8_root_units as r
now=datetime.now(timezone.utc).isoformat()
path=u.WORK/'root/local_kummer.tex';before=path.read_text()
old=r'\section{The local Kummer cover and its global obstruction}'
new=r'\subsection{The local Kummer cover and its global obstruction}'
assert before.count(old)==1
after=before.replace(old,new,1)
cp=u.ROOT/'S6_SERIES_PUBLISH_III.tex';canonical=cp.read_text();assert canonical.count(before)==1
replacement=canonical.replace(before,after,1)
for pattern in [r'\\label\{([^}]+)\}',r'\\hypertarget\{([^}]+)\}']:
 assert Counter(re.findall(pattern,canonical))==Counter(re.findall(pattern,replacement))
df,ds=r.table(r.DEFECTS);ef,es=r.table(u.ROOT/'CHECK_EVENTS.tsv');pf,ps=r.table(u.ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv')
ident='III-C8-KUMMER-ACTUAL-SUBSECTION';assert not any(x['change_id']==ident for x in ds)
note='agents/continuation8_iii_root/S6_SERIES_PUBLISH_III_local_kummer_unit_review.md'
ds.append(dict(change_id=ident,type='D14',statement_id='maps:src:C.1.1',old_location='local_kummer first line, followed by cyclic-invariants subsection',old_page='pending page concordance',new_location='local_kummer actual subsection',new_page='pending final PDF',old_text=old,new_text=new,reason='The following cyclic-invariants heading is a subsection, so the old section could not be called a section without subsections. This complete 615-line mathematical unit now has its own actual subsection boundary; no additional proof or criterion credit.',review_status='Exact boundary read; proof overlap with 037X discovered in whole reading and D12/structure reopened. '+note))
for row in ps:
 if row['paper']=='III' and row['unit_id']=='maps:src:C.1.1':
  c=row['defect_type'] or 'structure'
  if c in {'D12','structure'}:
   assert row['status']=='done';row.update(status='open',date_utc=now,evidence=note,detail='Whole later 037X reading found repeated common action/flatness/invariant-ring/local-length proof. Exact-map consolidation is pending; the full existing arguments remain present.')
  elif c=='D14':row.update(date_utc=now,evidence=note,detail='Complete Kummer material is one actual subsection followed by the cyclic-invariants subsection. The earlier section-without-subsections description was corrected; no added completion count.')
eid='publish:c8:III:kummer:actual-boundary-overlap';assert not any(x['event_id']==eid for x in es)
event={k:'' for k in ef};event.update(statement_id='maps:src:C.1.1',date='2026-11-25',who='GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; numerical effort not separately exposed; continuation eight, root',type='used and rechecked in this run',outcome='The whole 532-line 037X/0382/037Y unit and all three complete c5 comparisons were read after the complete K2 proof. They expose the shared action/flatness/invariant-ring/local-length proof; D12 and structure reopen pending exact map consolidation. The actual Kummer heading is corrected to a subsection because its successor is a subsection. This corrects the earlier boundary description, with no new independent or source-completion credit.',event_id=eid,phase='continuation8 publication unit comparison',source_file=note,source_event_type='used and rechecked in this run',evidence_group='publish:c8:III:kummer',date_utc=now,where=note);es.append(event)
rp=u.ROOT/note;review=rp.read_text()
review=review.replace('The final fragment has 615 lines and is one actual section without subsections.','The final fragment has 615 lines. The later boundary correction below makes it one actual subsection.')
review += '\n## Later whole-unit overlap and actual-boundary correction\n\n'+now+' UTC. The whole 532-line later Kummer-extension unit and all three complete c5 comparisons (037X, 0382, 037Y) have now been read. Its common action, finite-flat, invariant-ring and local-length proof repeats the earlier K2 proof. D12 and structure are reopened pending an exact coordinate/parameter identification and one common proof owner. The additional conductor and whole-family deck assertions retain their own complete proofs. The analytic action-comparison remark retains every holomorphic correction matrix and the N=1 endpoint. No theorem conclusion is refuted.\n\nThe earlier description of this as a section without subsections was premature: its next cyclic-invariants heading is a subsection. The Kummer heading is now itself a subsection, giving the complete mathematical material its actual boundary. All text below that heading and every label/target are unchanged. The earlier 24-source-criteria disposition is superseded by 22 done, with D12 and structure added to the four common holds. This correction confers no added completion count.\n'
path.write_text(after,newline='\n');cp.write_text(replacement,newline='\n');rp.write_text(review,newline='\n')
r.write_table(r.DEFECTS,df,ds);r.write_table(u.ROOT/'CHECK_EVENTS.tsv',ef,es);r.write_table(u.ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv',pf,ps)
print('UTC',now);print('EXACT_HEADING_EDIT_ROWS',1,'USED_EVENT',1,'CRITERIA_REOPENED',2);print('ALL_IDENTITIES_AND_OTHER_MANUSCRIPT_BYTES_PRESERVED')
