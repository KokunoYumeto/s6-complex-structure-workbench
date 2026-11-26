"""Admit the fully read final cusp/retained common-proof consolidation."""
from datetime import datetime, timezone
import S6_SERIES_PUBLISH_c8_integrate_units as u
import S6_SERIES_PUBLISH_c8_root_units as r

now=datetime.now(timezone.utc).isoformat()
note='agents/continuation8_iii_root/S6_SERIES_PUBLISH_III_cusp_retained_final_admission.md'
df,ds=r.table(r.DEFECTS)
ef,es=r.table(u.ROOT/'CHECK_EVENTS.tsv')
pf,ps=r.table(u.ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv')
source=u.repairs.SOURCE.read_text()
folder=u.ROOT/'agents/continuation8_iii_weighted_units'
edits=[];events=[]
for name,nd,ne in [('BASED_SMOOTHING',6,1),('CUSP_NULLBORDISM',62,3),('NATIVE_SPHERE',88,5)]:
 d=r.table(folder/f'S6_SERIES_PUBLISH_{name}_publication_defects.tsv')[1]
 e=r.table(folder/f'S6_SERIES_PUBLISH_{name}_CHECK_EVENTS.tsv')[1]
 assert (len(d),len(e))==(nd,ne)
 edits.extend(d);events.extend(e)
for row in edits:
 assert not any(x['change_id']==row['change_id'] for x in ds)
 out={k:row.get(k,'') for k in df}
 out['review_status']+='; actual complete canonical consolidation and all28 criteria admitted '+now+'; '+note
 ds.append(out)
for row in events:
 assert row['type']=='used and rechecked in this run'
 assert not any(x['event_id']==row['event_id'] for x in es)
 out={k:row.get(k,'') for k in ef}
 out['outcome']+=' Root read the complete substantive review/all28 criteria, exact final source changes, successful canonical application/empty stderr and actual boundaries. '+note
 es.append(out)
units=[
 ('mapsIII:based-regular-fibre-smoothing','Based smoothing at a regular fibre',{'D18'}),
 ('wb:h24:ret:section','The regular cusp torus',{'D04','D06','D09','D18'}),
 ('mapsIII:lem:retained-angle-differential','Differential and orientation of the cusp torus',{'D04','D06','D09','D18'}),
 ('wb:h24:ret:framing-proposition','Stable framing and the spin invariant',{'D04','D06','D09','D18'}),
 ('maps:src:B.3.1','The retained-angle homotopy class',{'D04','D06','D09','D18'}),
 ('wb:cusp-null:eq:periods','A framed nullbordism of the cusp fibre',{'D04','D06','D09','D18'}),
 ('wb:cusp-s12-carrier-homotopy','Coefficients and framed fibres of the sphere carriers',{'D04','D06','D09','D18'}),
]
closed=0
for ident,title,holds in units:
 assert '\\label{'+ident+'}' in source
 rows=[x for x in ps if x['paper']=='III' and x['unit_id']==ident]
 assert len(rows)==28 and all(x['status']=='open' for x in rows)
 for row in rows:
  c=row['defect_type'] or 'structure';done=c not in holds
  row.update(unit_title=title,status='done' if done else 'open',date_utc=now,evidence=note,
   detail='Complete attributed source/comparison and every criterion admitted after actual canonical consolidation; exact remaining common gates and final PDF are recorded in the root review.')
  closed+=done
ident='mapsIII:def:cusp-suspension-maps'
for row in ps:
 if row['paper']=='III' and row['unit_id']==ident and (row['defect_type'] or 'structure') in {'D12','structure'}:
  assert row['status']=='open'
  row.update(status='done',date_utc=now,evidence=note,detail='The complete J7 proof and Q257 moved comparison now have single final canonical owners; whole remainder and actual boundaries read.')
  closed+=1
for ident in ['maps:src:B.4.1','maps:src:B.2.1']:
 rows=[x for x in ps if x['paper']=='III' and x['unit_id']==ident]
 assert len(rows)==28
 for row in rows:
  row['evidence']+='; '+note
  row['detail']+=' Final exact common-owner/memberwise-scope change read; status unchanged.'
assert closed==173,closed
root_ids=[x[0] for x in units]+['mapsIII:def:cusp-suspension-maps','maps:src:B.4.1','maps:src:B.2.1']
for ident in root_ids:
 eid='publish:c8:III:cusp-retained-final:'+ident
 assert not any(x['event_id']==eid for x in es)
 row={k:'' for k in ef}
 row.update(statement_id=ident,date='2026-11-25',who='GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; numerical effort not separately exposed; continuation eight root',type='used and rechecked in this run',outcome='Complete attributed whole-source/proof comparisons and all28 criteria read. Exact common-owner maps/inverses, final changes and actual canonical boundaries read. Scope and remaining gates are in '+note+'. No independent, required, program-rerun or final-page credit.',event_id=eid,phase='continuation8 publication unit comparison',source_file=note,source_event_type='used and rechecked in this run',evidence_group='publish:c8:III:cusp-retained-final',date_utc=now,where=note)
 es.append(row)
assert any(line.startswith('\\bibitem') and '{CuspNullMilnor1965}' in line for line in source.splitlines())
for key in ['based_smoothing','retained_angle','quotient_maps','named_fibrations','cusp_nullbordism','full_sphere_nullity','base_map']:
 fragment=(u.WORK/u.BY_KEY[key].owner/(key+'.tex')).read_text()
 assert source.count(fragment)==1,key
r.write_table(r.DEFECTS,df,ds)
r.write_table(u.ROOT/'CHECK_EVENTS.tsv',ef,es)
r.write_table(u.ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv',pf,ps)
print('UTC',now,'EXACT_DEFECT_ROWS',len(edits),'ATTRIBUTED_USED_EVENTS',len(events),'ROOT_USED_EVENTS',len(root_ids))
print('ACTUAL_NEWLY_ADMITTED_UNITS',len(units),'CRITERIA_CLOSED',closed,'NEW_UNIT_ROWS',0)
print('FINAL_REFERENCE_BIBLIOGRAPHY_PROGRAM_TABLE_BUILD_AND_PAGE_GATES_REMAIN')
