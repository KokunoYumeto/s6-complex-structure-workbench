"""Admit the complete framing publication review at its actual scope."""
from datetime import datetime, timezone
import S6_SERIES_PUBLISH_c8_integrate_units as u
import S6_SERIES_PUBLISH_c8_root_units as r
now=datetime.now(timezone.utc).isoformat()
evidence='agents/continuation8_iii_root/S6_SERIES_PUBLISH_III_framing_unit_review.md'
fields,events=r.table(u.ROOT/'CHECK_EVENTS.tsv')
outcomes={
 'mapsIII:def:framing-conventions':'Whole definition and all preceding convention text read; exact character kernel, stable/unstable generators, suspended Hopf maps and frame order retained.',
 'maps:src:B.1.1':'Whole preceding and publication proofs and admitted comparisons read. The broader existing J5 sphere/affine/Spin proof is relocated here with its full |p|=1 scope. Actual mod-two and integral fixed-lattice equations, signed integral duality map/inverse and equivariance replace the program-only assertion. Transfer, integral H3, skeletal collapse and lift ambiguity are complete.',
 'maps:src:B.1.2':'Whole preceding and publication proofs and admitted comparison read. The exact full-scope framing lemma supplies the sole comparison. All source/target, regular-fibre derivative, quaternionic disk, product collapse, APS spectrum/invariant and Toda stabilization/injection calculations remain. All three old equation identities are preserved.'
}
for label,outcome in outcomes.items():
 eid='publish:c8:III:framed:'+label
 assert not any(x['event_id']==eid for x in events)
 row={k:'' for k in fields}
 row.update(statement_id=label,date='2026-11-25',who='GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; numerical effort not separately exposed; continuation eight, root',type='used and rechecked in this run',outcome=outcome+' No new independent derivation/check credit.',event_id=eid,phase='continuation8 publication unit comparison',source_file=evidence,source_event_type='used and rechecked in this run',evidence_group='publish:c8:III:framed',date_utc=now,where=evidence)
 events.append(row)
pf,progress=r.table(u.ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv')
selected=[x for x in progress if x['paper']=='III' and x['unit_id']=='maps:src:B.1.1']
assert len(selected)==28 and all(x['status']=='open' for x in selected)
closed=0
for row in selected:
 hold=row['defect_type'] in {'D04','D06','D09','D18'}
 row.update(unit_title='Framings and the quotient homotopy class',status='open' if hold else 'done',date_utc=now,evidence=evidence,detail='Global current-edition references, program-table disposition and bibliography remain open.' if hold else 'Whole preceding and current bounded unit, both admitted comparisons, exact final inverse and every criterion read; final build and rendered-page gates remain separate.')
 closed+=not hold
r.write_table(u.ROOT/'CHECK_EVENTS.tsv',fields,events)
r.write_table(u.ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv',pf,progress)
print('UTC',now)
print('USED_AND_RECHECKED_EVENTS',len(outcomes))
print('SOURCE_CRITERIA_CLOSED',closed)
print('D04_D06_D09_D18_AND_FINAL_BUILD_PAGES_OPEN')
