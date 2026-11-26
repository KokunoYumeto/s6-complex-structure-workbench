"""Record the exact applied locator edits and clarify Q109's cited scope."""
from datetime import datetime, timezone
from pathlib import Path
import json
import S6_SERIES_PUBLISH_c8_integrate_units as u
import S6_SERIES_PUBLISH_c8_root_units as r

now=datetime.now(timezone.utc).isoformat()
path=u.ROOT/'code/S6_SERIES_PUBLISH_c8_bibliography_locators.apply.out'
lines=path.read_text().splitlines()
actual=[json.loads(x) for x in lines[1:-1]]
prior=[json.loads(x) for x in (u.ROOT/'code/S6_SERIES_PUBLISH_c8_bibliography_locators.root_inspect.out').read_text().splitlines()[1:-1]]
assert actual==prior and lines[-1].startswith('APPLIED exactly')
assert not (u.ROOT/'code/S6_SERIES_PUBLISH_c8_bibliography_locators.apply.err').read_text()
canonical=[x for x in actual if x['path']=='S6_SERIES_PUBLISH_III.tex'];assert len(canonical)==35
df,ds=r.table(r.DEFECTS);ef,es=r.table(u.ROOT/'CHECK_EVENTS.tsv')
for i,item in enumerate(canonical,1):
 for kind in ['D06','D18']:
  ident=f'III-C8-BIBLIOGRAPHY-LOCATOR-{i:02d}-{kind}'
  assert not any(x['change_id']==ident for x in ds)
  ds.append(dict(change_id=ident,type=kind,statement_id='III:primary-locator-consolidation',old_location='canonical III line '+str(item['line']),old_page='unbuilt intermediate source; source locator retained',new_location='same cited mathematical application',new_page='pending final PDF',old_text=item['old'],new_text=item['new'],reason=item['evidence']+' Root read every actual application context; all35 canonical contexts equal their wholly read fragment contexts. Exact statement/page and source-opening scope are in '+item['review'],review_status='complete proposal/inspection/actual application read; all70 output rows match exactly; empty stderr; no theorem scope or criterion increment'))
source=u.repairs.SOURCE.read_text();p=u.WORK/'foundations/elliptic_basic_families.tex';old=p.read_text()
before='The integral homology\nof the initial family is calculated in'
after='The second homology of the initial family is expressed by the\nintegral cap-map cokernel in'
assert old.count(before)==1 and source.count(old)==1
new=old.replace(before,after,1);candidate=source.replace(old,new,1)
u.check_permanent_identifiers(source,candidate,set(),set())
for kind in ['D18','D26']:
 ident='III-C8-Q109-CITED-H2-SCOPE-'+kind
 assert not any(x['change_id']==ident for x in ds)
 ds.append(dict(change_id=ident,type=kind,statement_id='mapsIII:rem:initial-logarithmic-homology',old_location='Q109 complete remark, foundations/elliptic_basic_families.tex lines439-448',old_page='unbuilt intermediate source',new_location='same complete remark',new_page='pending final PDF',old_text=before,new_text=after,reason='The complete opened Viaclovsky Logs v1 Proposition4.1, p9, gives precisely the integral H2 cap-map cokernel. This sentence now states that exact cited output for the same initial family. The preceding complete III theorem still proves its full homology and both determinant cases through the already supplied integral maps. Root read the entire Q109 remark; no family datum, III homology conclusion or proof is changed.',review_status='whole cited-scope comparison and original remark read; actual final bounded readback pending; no new refutation of the III theorem or completed-criterion increment'))
for ident,detail in [
 ('III:primary-locator-consolidation','All35 final locator occurrences and their exact identical canonical/fragment application contexts read. Actual70-row application output equals the inspected proposal, with empty stderr. Primary source readings retain the bibliography editor and predecessor attribution; two cited construction owners are corrected without changing displayed maps.'),
 ('mapsIII:rem:initial-logarithmic-homology','Complete Q109 remark and its cited H2 scope read. The same initial-family domain and complete preceding III homology theorem remain; the source summary now names the integral second-homology cokernel of exact Logs Proposition4.1 p9.')]:
 eid='publish:c8:III:bibliography-locators:'+ident
 assert not any(x['event_id']==eid for x in es)
 event={k:'' for k in ef};event.update(statement_id=ident,date='2026-11-25',who='GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; numerical effort not separately exposed; continuation eight root',type='used and rechecked in this run',outcome=detail+' No independent, required, program-rerun or source-criterion completion credit.',event_id=eid,phase='continuation8 publication source-locator reconciliation',source_file='code/S6_SERIES_PUBLISH_c8_admit_bibliography_locators.py',source_event_type='used and rechecked in this run',evidence_group=eid,date_utc=now,where='agents/continuation8_iii_later/S6_SERIES_PUBLISH_III_bibliography_publication_review.md');es.append(event)
p.write_text(new,encoding='utf-8',newline='\n');u.repairs.SOURCE.write_text(candidate,encoding='utf-8',newline='\n')
r.write_table(r.DEFECTS,df,ds);r.write_table(u.ROOT/'CHECK_EVENTS.tsv',ef,es)
print('UTC',now,'CITATION_DEFECT_ROWS',70,'Q109_SCOPE_ROWS',2,'ROOT_USED_EVENTS',2)
start=new.index('\\begin{remark}[The initial logarithmic homology calculation]');end=new.index('\\end{remark}',start)+len('\\end{remark}')
print('ACTUAL_FINAL_Q109\n'+new[start:end])
print('NO_SOURCE_CRITERION_OR_INDEPENDENT_INCREMENT')
