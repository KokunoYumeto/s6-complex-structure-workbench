"""Admit the complete Kummer refinement and close its proved shared-owner overlap."""
from datetime import datetime,timezone
import S6_SERIES_PUBLISH_c8_integrate_units as u
import S6_SERIES_PUBLISH_c8_root_units as r
now=datetime.now(timezone.utc).isoformat();note='agents/continuation8_iii_root/S6_SERIES_PUBLISH_III_kummer_extension_unit_review.md'
df,ds=r.table(r.DEFECTS);ef,es=r.table(u.ROOT/'CHECK_EVENTS.tsv');pf,ps=r.table(u.ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv')
selected=[x for x in ds if x['change_id'].startswith('III-C8-KUMMER-EXT-') or x['change_id']=='III-C8-KUMMER-COMPATIBLE-DISCS'];assert len(selected)==13,len(selected)
for row in selected:row['review_status']='Whole 532-line input, all three complete c5 comparisons, complete 451-line rewrite and every final context read; exact common-proof identification and all refinement arguments admitted. '+note
outcomes={
 'mapsIII:def:completed-cusp-root-data':'Complete old and numbered data read. The exact target-family scope, t=q and inverse, same fan/C/units, compatible discs and both source actions are explicit.',
 'wb:cusp-cover-extension-theorem':'All six original clauses, entire old/current proofs and full c5 comparison read. K2 owns the identical common proof through actual maps and inverses. The full conductor/normalization square, branch support, N double branches and global deck action remain, with both actual loop directions.',
 'wb:cusp-cover-naive-action-failure':'Complete old/current remark and whole c5 comparison read. Every holomorphic C, exact two composites and multiplier, all Taylor coefficients, N=1 and exceptional constant/integral cases remain; the inverse multiplier is explicit.',
 'wb:cusp-cover-global-scope':'Complete old/current remark and full c5 comparison read. The actual A1 inverse loop and integral-local-system obstruction remain. Repeated factorization/endpoint proof has its exact earlier owner; no changed-base exclusion is added.',
 'mapsIII:def:kummer-data':'Bounded follow-up after its entire prior reading: the compatible root/target discs and full inverse-image relation are now explicit, with epsilon_N avoiding the log-coordinate name. The complete K2 proof is the common owner after the exact later comparison.'}
for label,outcome in outcomes.items():
 eid='publish:c8:III:kummer-extension:'+label;assert not any(x['event_id']==eid for x in es)
 row={k:'' for k in ef};row.update(statement_id=label,date='2026-11-25',who='GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; numerical effort not separately exposed; continuation eight, root',type='used and rechecked in this run',outcome=outcome+' Both actual edit outputs and empty errors read. No historical program rerun, new primary reading, independent-check or final-page credit.',event_id=eid,phase='continuation8 publication unit comparison',source_file=note,source_event_type='used and rechecked in this run',evidence_group='publish:c8:III:kummer-extension',date_utc=now,where=note);es.append(row)
closed=0
rows=[x for x in ps if x['paper']=='III' and x['unit_id']=='wb:cusp-cover-section'];assert len(rows)==28 and all(x['status']=='open' for x in rows)
for row in rows:
 c=row['defect_type'] or 'structure';done=c not in {'D04','D06','D09','D18'};row.update(unit_title='Completed Kummer covers',status='done' if done else 'open',date_utc=now,evidence=note,detail='Whole predecessor/current unit and complete comparisons admitted; exact common-proof maps and actual next section read. Four common/PDF gates remain.');closed+=done
for row in ps:
 if row['paper']=='III' and row['unit_id']=='maps:src:C.1.1' and (row['defect_type'] or 'structure') in {'D12','structure'}:
  assert row['status']=='open';row.update(status='done',date_utc=now,evidence=note,detail='The discovered common-proof overlap is resolved by the complete K2/037X map-and-inverse comparison. K2 is the sole common proof owner; distinct refinements remain.');closed+=1
assert closed==26
rp=u.ROOT/'agents/continuation8_iii_root/S6_SERIES_PUBLISH_III_local_kummer_unit_review.md'
with rp.open('a',newline='\n') as f:f.write('\n## Completed common-proof consolidation\n\n'+now+' UTC. The entire later Kummer rewrite and every final context have been read and admitted in `'+note+'`. K2 is the common proof owner through the exact t=q, period-basis, fan, correction and compatible-radius maps and inverses. The additional conductor/global-deck arguments remain complete. D12 and structure therefore close again; this unit returns to 24 source criteria done and four common holds. The Q017 compatible discs are explicit. No independent-check or final-page credit is added.\n')
r.write_table(r.DEFECTS,df,ds);r.write_table(u.ROOT/'CHECK_EVENTS.tsv',ef,es);r.write_table(u.ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv',pf,ps)
print('UTC',now);print('EXACT_EDIT_ROWS',13,'USED_EVENTS',5,'SOURCE_CRITERIA_CLOSED',closed);print('FOUR_COMMON_GATES_AND_FINAL_PDF_OPEN')
