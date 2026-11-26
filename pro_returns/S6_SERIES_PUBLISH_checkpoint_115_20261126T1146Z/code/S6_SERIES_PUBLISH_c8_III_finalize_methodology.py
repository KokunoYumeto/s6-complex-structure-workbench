"""Insert exact current statement counts and the evidenced rational-bound method."""
from datetime import datetime, timezone
import json
import textwrap
import S6_SERIES_PUBLISH_c8_integrate_units as u
import S6_SERIES_PUBLISH_c8_root_units as r
import S6_SERIES_PUBLISH_c8_III_check_counts as counts

now=datetime.now(timezone.utc).isoformat()
data=counts.current_data()
assert len(data['selected'])==1066 and len(data['groups'])==799
assert tuple(data['counts'][t] for t in counts.TYPES)==(421,2,50,473,90,30)
front_path=u.WORK/'root/front_matter.tex'
old=front_path.read_text(encoding='utf-8')
source=u.repairs.SOURCE.read_text(encoding='utf-8')
assert source.count(old)==1
assert 'The records associate ' not in old
before='proofs, exact arithmetic, interval computations and comparison with'
after='proofs, exact arithmetic, certified rational bounds and comparison with'
assert old.count(before)==1
new=old.replace(before,after,1)
anchor='No human has checked the mathematics.'
assert new.count(anchor)==1
paragraph=textwrap.fill(counts.count_prose(data),width=76)
new=new.replace(anchor,paragraph+'\n\n'+anchor,1)
candidate=source.replace(old,new,1)
u.check_permanent_identifiers(source,candidate,set(),set())
df,ds=r.table(r.DEFECTS)
changes=[
 ('III-C8-METHODOLOGY-FINAL-COUNTS','D15',anchor,paragraph+'\n\n'+anchor,'Exact final current-statement selection from authoritative CHECK_EVENTS:249 formal owners,1066 associations,799 groups, six unchanged types. The exact wholly withdrawn L5 event is excluded and its actual replacement retained; merely mentioning withdrawn older premises does not exclude a row. All statement/equation/section/admin subject boundaries are explicit in the delivered selector.'),
 ('III-C8-METHODOLOGY-RATIONAL-BOUNDS-D15','D15',before,after,'The concrete III certified-bound computation is the admitted whole-segment rational Rouche certificate in the KM analytic-cover source and c5 comparison lines421–428. State this evidenced method in the methodology.'),
 ('III-C8-METHODOLOGY-RATIONAL-BOUNDS-D18','D18',before,after,'Exact source-supported computation method, approved after the bibliography/provenance reviewer read its KM owner; no software or interval-library execution is inferred from another paper.'),
]
for ident,kind,a,b,reason in changes:
    assert not any(x['change_id']==ident for x in ds)
    ds.append(dict(change_id=ident,type=kind,statement_id='methodology',old_location='canonical III section1.5 and exact front_matter fragment',old_page='unbuilt intermediate source',new_location='same methodology passage',new_page='pending final PDF',old_text=a,new_text=b,reason=reason,review_status='whole selector source, actual successful inspect output/emptystderr and whole methodology passage read; canonical application '+now+'; final provenance and PDF gates remain'))
ef,es=r.table(u.ROOT/'CHECK_EVENTS.tsv')
eid='publish:c8:III:final-methodology-count-selection'
assert not any(x['event_id']==eid for x in es)
event={k:'' for k in ef}
event.update(statement_id='III:provenance-counts',date='2026-11-25',who='GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; numerical effort not separately exposed; continuation eight root',type='used and rechecked in this run',outcome='Whole320-line selector, complete actual successful inspect output and empty stderr read by root and provenance reviewer. Actual final counts recomputed; exact withdrawn/replacement outcome guards and stable subject/event selection checked. This administrative event remains outside statement totals. Source method wording names the evidenced certified rational bounds. No mathematical/independent/required or page credit.',event_id=eid,phase='continuation8 final methodology counts',source_file='code/S6_SERIES_PUBLISH_c8_III_check_counts.py',source_event_type='used and rechecked in this run',evidence_group=eid,date_utc=now,where='agents/continuation8_iii_weighted_units/S6_SERIES_PUBLISH_III_check_counts_inspect_v001.out')
es.append(event)
pf,ps=r.table(u.ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv')
selected=[x for x in ps if x['paper']=='III' and x['unit_id']=='methodology' and x['defect_type']=='D15']
assert len(selected)==1 and selected[0]['status']=='open'
selected[0].update(status='done',date_utc=now,evidence='code/S6_SERIES_PUBLISH_c8_III_check_counts.py; code/S6_SERIES_PUBLISH_c8_III_finalize_methodology.py',detail='Final exact statement-associated count paragraph and evidenced rational-bound method inserted; all six categories and distinct recorded groups recomputed from authoritative events. Remaining D18 provenance/PDF/joint gates are separate.')
front_path.write_text(new,encoding='utf-8',newline='\n')
u.repairs.SOURCE.write_text(candidate,encoding='utf-8',newline='\n')
r.write_table(r.DEFECTS,df,ds);r.write_table(u.ROOT/'CHECK_EVENTS.tsv',ef,es);r.write_table(u.ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv',pf,ps)
final=counts.current_data()
assert [x['event_id'] for x in final['selected']]==[x['event_id'] for x in data['selected']]
assert final['counts']==data['counts'] and final['groups']==data['groups']
record=counts.summary(final)
record['selected_event_ids']=[x['event_id'] for x in final['selected']]
record['recorded_evidence_groups']=sorted(final['groups'])
record['interpretation']='Exact statement-event associations; six unchanged types, unique event IDs, explicitly withdrawn event excluded. Administrative and page records remain outside the selected current formal statement subjects.'
out=u.ROOT/'records/S6_SERIES_PUBLISH_III_current_check_counts.json'
assert not out.exists()
out.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
print('UTC',now,'DEFECT_ROWS',len(changes),'ADMIN_USED_EVENT',1,'METHODOLOGY_D15_CLOSED',1)
print('FINAL_COUNTS',dict(final['counts']),'ASSOCIATIONS',len(final['selected']),'GROUPS',len(final['groups']))
print('EXACT_EVENT_ID_SELECTION_UNCHANGED_AFTER_SOURCE_AND_ADMIN_RECORD_WRITE')
start=new.index('The models worked from explicit statements')
stop=new.index('\\subsection{How the paper is organized}',start)
print('ACTUAL_FINAL_METHODOLOGY_END\n'+new[start:stop])
print('WROTE',str(out))
