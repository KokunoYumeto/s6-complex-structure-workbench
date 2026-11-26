"""Repair the observed array-row optional-spacing parse, preserving its formula."""
from datetime import datetime, timezone
import S6_SERIES_PUBLISH_c8_integrate_units as u
import S6_SERIES_PUBLISH_c8_root_units as r
import S6_SERIES_PUBLISH_c8_III_check_counts as counts

now=datetime.now(timezone.utc).isoformat()
path=u.WORK/'root/cyclic_invariants.tex'
old=path.read_text(encoding='utf-8');source=u.repairs.SOURCE.read_text(encoding='utf-8')
before=r' [\mathrm{point}]\times z_3&u_0^3.'
after=r' {}[\mathrm{point}]\times z_3&u_0^3.'
assert old.count(before)==1 and source.count(old)==1
new=old.replace(before,after,1);candidate=source.replace(old,new,1)
u.check_permanent_identifiers(source,candidate,set(),set())
owners=counts.parse_statements(source)[0]
offset=source.index(before)
owner=[x.statement_id for x in owners if x.start<=offset<x.stop]
assert len(owner)==1
df,ds=r.table(r.DEFECTS);ident='III-C8-TEX-ARRAY-BRACKET-01'
assert not any(x['change_id']==ident for x in ds)
ds.append(dict(change_id=ident,type='D23',statement_id=owner[0],old_location='canonical III line7172; cyclic_invariants.tex line827',old_page='pass01 stopped on provisional page79; no completed PDF',new_location='same finite-coordinate dual-pair display',new_page='pending successful full PDF',old_text=before,new_text=after,reason='Actual pdfLaTeX pass01 reports Missing number at the bracket starting the third array row. The preceding row terminator scans that bracket as optional vertical spacing. The inserted empty TeX group terminates that optional-argument scan; it contributes no mathematical atom, and the point cross z3 / u0^3 pair remains literal. Root read the complete display and surrounding integral Kunneth/evaluation argument.',review_status='exact parse repair applied '+now+'; next actual full build and visual page reading remain; no mathematical scope or check credit'))
pf,ps=r.table(u.ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv')
rows=[x for x in ps if x['paper']=='III' and x['unit_title']=='Finite-coefficient cubics and the fundamental class' and x['defect_type']=='D23']
assert len(rows)==1
rows[0].update(status='open',date_utc=now,evidence='code/S6_SERIES_PUBLISH_c8_tex_III_final_pass01.out; code/S6_SERIES_PUBLISH_c8_III_array_layout_fix.py',detail='Observed actual array-row parse failure repaired by an empty TeX group; actual successful successor build/page remains to verify the repaired display.')
ef,es=r.table(u.ROOT/'CHECK_EVENTS.tsv');eid='publish:c8:III:tex-array-bracket-01'
assert not any(x['event_id']==eid for x in es)
event={k:'' for k in ef};event.update(statement_id='III:layout-array-bracket',date='2026-11-25',who='GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; numerical effort not separately exposed; continuation eight root',type='used and rechecked in this run',outcome='Actual pass01 exit1 and fatal tail/empty stderr read; full affected display and surrounding integral pairing argument read. The empty TeX group repairs optional-spacing parsing without changing any mathematical entry. Full pass01 log reading attributed to runtime reviewer; successor compilation and PDF page remain. No proof, independent, required or page credit.',event_id=eid,phase='continuation8 actual TeX repair',source_file='code/S6_SERIES_PUBLISH_c8_III_array_layout_fix.py',source_event_type='used and rechecked in this run',evidence_group=eid,date_utc=now,where='code/S6_SERIES_PUBLISH_c8_tex_III_final_pass01.out');es.append(event)
path.write_text(new,encoding='utf-8',newline='\n');u.repairs.SOURCE.write_text(candidate,encoding='utf-8',newline='\n')
r.write_table(r.DEFECTS,df,ds);r.write_table(u.ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv',pf,ps);r.write_table(u.ROOT/'CHECK_EVENTS.tsv',ef,es)
print('UTC',now,'OWNER',owner[0],'D23_REOPENED',rows[0]['unit_id'])
start=new.index('The finite-coordinate dual pairs are')
print('ACTUAL_DISPLAY\n'+new[start:new.index('Each displayed pairing',start)])
print('COUNTS_UNCHANGED',len(counts.current_data()['selected']))
