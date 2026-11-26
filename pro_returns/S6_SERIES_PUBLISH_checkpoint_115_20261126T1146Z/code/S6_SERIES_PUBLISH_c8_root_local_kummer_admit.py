"""Admit the complete local-Kummer publication reading at its actual boundary."""
from datetime import datetime,timezone
import S6_SERIES_PUBLISH_c8_integrate_units as u
import S6_SERIES_PUBLISH_c8_root_units as r
now=datetime.now(timezone.utc).isoformat()
note='agents/continuation8_iii_root/S6_SERIES_PUBLISH_III_local_kummer_unit_review.md'
df,ds=r.table(r.DEFECTS);ef,es=r.table(u.ROOT/'CHECK_EVENTS.tsv');pf,ps=r.table(u.ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv')
selected=[x for x in ds if x['change_id'].startswith('III-C8-KUMMER-')]
assert len(selected)==61,len(selected)
for row in selected:row['review_status']='Whole predecessor/current proofs, all five complete c4 comparisons, complete fan supplement and every final context read; four common/PDF gates open. '+note
outcomes={
 'mapsIII:def:kummer-data':'The full common input and final numbered definition were read. The original marked periods, all positive roots, complete translated two-triangle fan and exact based-generator/point-return convention are explicit.',
 'maps:src:C.1.1':'The full old/current construction and entire c4 comparison were read. All chart maps, finite free module, normalized-base-change map, degree N^3/N^2, exact bad strata, fibre lattice and N=1 endpoint remain.',
 'maps:src:C.1.2':'The complete old/current whole-fan proof, entire c4 comparison and full coordinate supplement were read. Every adjacent-cone divisibility step and analytic extension remains. The neighbouring normalization ring, finite map, basis and cotangent/index obstruction are now explicit.',
 'maps:src:C.1.3':'The complete old/current obstruction and whole c4 comparison were read. Stein factorization, vertical ramification, both commuting transport squares, inverse based loop, smooth fan pullback and exact lattice involution remain in the full proof.',
 'maps:src:C.1.4':'The complete old/current proof and entire c4 comparison were read. The full normal-source Stein factor, proper analytic bad-base image, sheet-to-lattice map, exact monodromy orbit and N^2<=N contradiction are printed alongside the unchanged all-N integer computation. Supplementary primary records were read only at the bounded scope stated in the review.',
 'maps:src:C.1.5':'The complete old/current global-cover proof and entire c4 comparison were read. Every finite quotient/coset map, inverse, period-cover formula, invariant-ring inverse, normal extension/gluing and forced singularity argument is retained for the full parameter range.',
 'mapsIII:rem:kummer-finite-values':'All original finite values and final numbered remark were compared. Exact historical path-index entries were read; no old mathematical program was newly executed or claimed wholly read. The all-N proof owners and finite congruence scope are explicit.'}
for label,outcome in outcomes.items():
 eid='publish:c8:III:kummer:'+label
 assert not any(x['event_id']==eid for x in es)
 row={k:'' for k in ef};row.update(statement_id=label,date='2026-11-25',who='GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; numerical effort not separately exposed; continuation eight, root',type='used and rechecked in this run',outcome=outcome+' All actual editor failure/success streams and final corrections read. Both bibliography entries and four automatic equations read. No new independent-check or final-page credit.',event_id=eid,phase='continuation8 publication unit comparison',source_file=note,source_event_type='used and rechecked in this run',evidence_group='publish:c8:III:kummer',date_utc=now,where=note);es.append(row)
selected=[x for x in ps if x['paper']=='III' and x['unit_id']=='maps:src:C.1.1']
assert len(selected)==28 and all(x['status']=='open' for x in selected)
closed=0
for row in selected:
 c=row['defect_type'] or 'structure';hold=c in {'D04','D06','D09','D18'}
 row.update(unit_title='The local Kummer cover and its global obstruction',status='open' if hold else 'done',date_utc=now,evidence=note,detail='Common reference/program/bibliography gate remains open.' if hold else 'Whole actual section, all five complete comparisons, exact maps and all28 criteria read; actual next subsection present. Final build/pages separate.');closed+=not hold
assert closed==24
r.write_table(r.DEFECTS,df,ds);r.write_table(u.ROOT/'CHECK_EVENTS.tsv',ef,es);r.write_table(u.ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv',pf,ps)
print('UTC',now);print('EXACT_KUMMER_EDIT_ROWS_ADMITTED',61,'USED_EVENTS',len(outcomes),'SOURCE_CRITERIA_CLOSED',closed);print('FOUR_COMMON_GATES_AND_FINAL_PDF_OPEN; NO_INDEPENDENT_CHECK_CREDIT')
