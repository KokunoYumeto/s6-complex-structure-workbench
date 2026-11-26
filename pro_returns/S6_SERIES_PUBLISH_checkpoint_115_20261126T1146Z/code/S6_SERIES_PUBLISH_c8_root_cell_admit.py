"""Admit the whole cell-presentation publication reading, retaining common gates."""
from datetime import datetime,timezone
import S6_SERIES_PUBLISH_c8_integrate_units as u
import S6_SERIES_PUBLISH_c8_root_units as r
now=datetime.now(timezone.utc).isoformat()
note='agents/continuation8_iii_root/S6_SERIES_PUBLISH_III_cell_unit_review.md'
df,ds=r.table(r.DEFECTS);ef,es=r.table(u.ROOT/'CHECK_EVENTS.tsv');pf,ps=r.table(u.ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv')
selected=[x for x in ds if x['change_id'].startswith('III-C8-CELL-')]
assert len(selected)==47,len(selected)
for row in selected:row['review_status']='Whole predecessor/current proofs, complete JC comparison, exact JB prior scope, source inputs and all final contexts read; common/PDF gates open. '+note
outcomes={
 'mapsIII:def:marked-family':'Bounded follow-up to the wholly reviewed common unit: A1,A2,M0 now name the actual original analytic deck-generator maps. The exact clockwise/counterclockwise roof reversal and inverse are in Q016. No extension to unrelated generic finite-cap matrices is made.',
 'mapsIII:def:three-filling-datum':'The full old input/convention text and numbered definition were compared. Both roof-coordinate maps and inverse compositions, actual clockwise chart, both loop conjugations, point returns and original marked scope were read.',
 'maps:src:B.5.1':'The entire 668-line predecessor and first 720-line edited unit were read, followed by the whole final cellular object/arrow construction and all final contexts. The complete cusp-product argument is retained; actual maps and inverses expand every cellular replacement. The bounded logarithmic drift-direction correction is recorded without changing any boundary map or conclusion. Exact primary-source/page and failed-fetch limits are in the review.',
 'maps:src:B.5.2':'The complete old/current ten-item proof and whole c5 comparison were read. Every integral matrix, lattice, kernel, homology argument and normal-framing construction remains. The inverse attachment/splitting maps and J4 ownership are explicit; boundary spaces now have E names while the matrix M0 remains unchanged.'}
for label,outcome in outcomes.items():
 eid='publish:c8:III:cell:'+label
 assert not any(x['event_id']==eid for x in es)
 row={k:'' for k in ef};row.update(statement_id=label,date='2026-11-25',who='GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; numerical effort not separately exposed; continuation eight, root',type='used and rechecked in this run',outcome=outcome+' Actual successful edit streams and complete source-fetch outcomes read. Failed parser and incidental path reads have no mathematical credit. No new independent-check or final-page credit.',event_id=eid,phase='continuation8 publication unit comparison',source_file=note,source_event_type='used and rechecked in this run',evidence_group='publish:c8:III:cell',date_utc=now,where=note);es.append(row)
selected=[x for x in ps if x['paper']=='III' and x['unit_id']=='maps:eq:B.5.1']
assert len(selected)==28 and all(x['status']=='open' for x in selected)
closed=0
for row in selected:
 c=row['defect_type'] or 'structure';hold=c in {'D04','D06','D09','D18'}
 row.update(unit_title='A cell presentation from the three fillings',status='open' if hold else 'done',date_utc=now,evidence=note,detail='Common reference/program/bibliography gate remains open.' if hold else 'Complete old/current actual subsection, full comparisons, exact maps and all28 criteria read; actual next section present. Final build and page gates separate.');closed+=not hold
assert closed==24
r.write_table(r.DEFECTS,df,ds);r.write_table(u.ROOT/'CHECK_EVENTS.tsv',ef,es);r.write_table(u.ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv',pf,ps)
print('UTC',now);print('EXACT_CELL_EDIT_ROWS_ADMITTED',47,'USED_EVENTS',len(outcomes),'SOURCE_CRITERIA_CLOSED',closed);print('FOUR_COMMON_GATES_AND_FINAL_PDF_OPEN; NO_INDEPENDENT_CHECK_CREDIT')
