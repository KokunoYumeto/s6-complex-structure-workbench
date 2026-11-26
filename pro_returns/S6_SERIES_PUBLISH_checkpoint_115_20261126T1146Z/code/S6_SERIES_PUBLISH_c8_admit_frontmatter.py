"""Admit six wholly read introductory units and exposed integration checks."""
from datetime import datetime, timezone
import S6_SERIES_PUBLISH_c8_integrate_units as u
import S6_SERIES_PUBLISH_c8_root_units as r

now=datetime.now(timezone.utc).isoformat()
note='agents/continuation8_iii_root/S6_SERIES_PUBLISH_III_frontmatter_final_admission.md'
df,ds=r.table(r.DEFECTS);ef,es=r.table(u.ROOT/'CHECK_EVENTS.tsv');pf,ps=r.table(u.ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv')
folder=u.ROOT/'agents/continuation8_iii_later'
edits=r.table(folder/'S6_SERIES_PUBLISH_III_frontmatter_publication_defects.tsv')[1]
events=r.table(folder/'S6_SERIES_PUBLISH_III_frontmatter_publication_CHECK_EVENTS.tsv')[1]
dep=[x for x in r.table(u.ROOT/'agents/continuation8_iii_foundations/S6_SERIES_PUBLISH_c8_foundations_CHECK_EVENTS.tsv')[1] if x['event_id'].startswith('ce:III:c8:dependency-order:')]
assert (len(edits),len(events),len(dep))==(30,8,8)
for row in edits:
 assert not any(x['change_id']==row['change_id'] for x in ds)
 out={k:row.get(k,'') for k in df};out['review_status']+='; complete root review and actual canonical placement admitted '+now+'; '+note;ds.append(out)
for row in events+dep:
 assert row['type']=='used and rechecked in this run'
 assert not any(x['event_id']==row['event_id'] for x in es)
 out={k:row.get(k,'') for k in ef};out['outcome']+=' Complete substantive review and this actual event payload read by root; final placement/evidence in '+note;es.append(out)
common={'D04','D06','D18'}
units=[('the-series-and-this-paper',common|{'D24'}),('series:III:main-theorems',common),('the-proofs-in-outline',common),('known-and-new',common),('methodology',common|{'D09','D15'}),('how-the-paper-is-organized',common)]
closed=0
for ident,holds in units:
 rows=[x for x in ps if x['paper']=='III' and x['unit_id']==ident]
 assert len(rows)==28 and all(x['status']=='open' for x in rows)
 for row in rows:
  criterion=row['defect_type'] or 'structure';done=criterion not in holds
  row.update(status='done' if done else 'open',date_utc=now,evidence=note,detail='Whole761-line introduction, complete350-line review/all28 criteria and actual canonical boundaries read. Exact unit-specific final reference, provenance, program-table and five-paper holds remain in root review; final PDF gate open.')
  closed+=done
assert closed==147,closed
for ident in [x[0] for x in units]+['III:AMS-equation-alias-runtime','III:exact-citation-owner-and-external-route']:
 eid='publish:c8:III:front-final:'+ident
 assert not any(x['event_id']==eid for x in es)
 row={k:'' for k in ef}
 row.update(statement_id=ident,date='2026-11-25',who='GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; numerical effort not separately exposed; continuation eight root',type='used and rechecked in this run',outcome='Complete attributed source/review/actual streams read; exact scope and remaining gates in '+note+'. No independent, required, mathematical-program rerun or final-page credit.',event_id=eid,phase='continuation8 publication introduction integration',source_file=note,source_event_type='used and rechecked in this run',evidence_group='publish:c8:III:front-final',date_utc=now,where=note)
 es.append(row)
source=u.repairs.SOURCE.read_text()
for key in ['preamble','front_matter']:
 fragment=(u.WORK/'root'/(key+'.tex')).read_text();assert source.count(fragment)==1,key
assert source.count('\\StatementRecord')==source.count('\\SBack')==0
r.write_table(r.DEFECTS,df,ds);r.write_table(u.ROOT/'CHECK_EVENTS.tsv',ef,es);r.write_table(u.ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv',pf,ps)
print('UTC',now,'EXACT_DEFECT_ROWS',len(edits),'FRONT_USED_EVENTS',len(events),'DEPENDENCY_USED_EVENTS',len(dep),'ROOT_USED_EVENTS',8)
print('ACTUAL_UNITS',6,'CRITERIA_CLOSED',closed,'NEW_UNIT_ROWS',0)
print('FINAL_REFERENCE_BIBLIOGRAPHY_PROGRAM_COUNTS_PROVENANCE_SERIES_AND_PDF_GATES_REMAIN')
