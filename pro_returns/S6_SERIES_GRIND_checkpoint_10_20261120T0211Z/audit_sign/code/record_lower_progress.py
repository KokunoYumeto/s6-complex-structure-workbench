from pathlib import Path
import csv,json
p=Path(__file__).resolve().parents[1]
f=p/'CHECK_EVENTS_additions.tsv'
with f.open() as h:rows=list(csv.DictReader(h,delimiter='\t'))
fields=list(rows[0]);ids={x['event_id'] for x in rows}
who='GPT-6 Astra (OpenAI), ChatGPT Pro mode, reasoning effort inherited (not separately exposed), S6_SERIES_GRIND/sign_theorem_audit'
events=[
 ('K111_lower_parent_2018','computation or formal certificate','Fresh K111_lower_parent_reconstruction.py passes2018 exact checks. From the twelve printed determinant-three raw lower cones it builds all96 regular full charts, extracts all36 physical lower-face charts, checks full raw invariant-semigroup pullbacks, source orders, L/T coefficient columns and inverses, and derives minimal normal degrees(-1,0,1),(-1,1,0) and relative intersections(-2/3,-1/3,-2/3). No old lower-star array or degree table is construction input. The actual324-chart refinements and321 contractions remain separate.'),
 ('K111_small_one_corner_145','computation or formal certificate','Fresh K111_small_one_corner.py passes145 checks on the newly built small raw-parent resolutions. All compact fixed-face owners are enumerated:60 isolated points, no compact curves, pair(12,88). This is the small resolution only. It has not been identified with the common-boundary endpoint and is not substituted for CFL one-end(2736,17092).'),
 ('K111_IL_edge_chain_reduction','targeted proof check','Reduced the remaining IL input to the ordered primitive native common-edge chain on3y-x-36r=0, including actual period closure. Derived its integral boundary-lattice map U(a,b)=(3a,a+12b,b,0), the raw determinant-three joins, the explicit floor/ceiling lift and its normal-character evaluations, and the modulo-three ordinary-contraction degree rule with reciprocal chart and line maps. These identities are on the stated written lifts; matching them to every actual324-chart common refinement remains open. Full derivation is K111_IL_edge_chain_reduction.md.')]
for key,kind,outcome in events:
 eid='S6_SERIES_GRIND_sign_'+key
 if eid not in ids:
  rows.append(dict(statement_id='night:P3K.111',date='2026-11-19',who=who,type=kind,outcome=outcome,event_id=eid,phase='continued mathematical review'))
with f.open('w') as h:
 w=csv.DictWriter(h,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
c=json.loads((p/'K111_coverage.json').read_text())
for name in ['code/K111_lower_parent_reconstruction.py','code/K111_small_one_corner.py']:
 if name not in c['fresh_exact_code']:c['fresh_exact_code'].append(name)
c['fresh_exact_checks']=2407
c['lower_scope']='2018 checks reconstruct all twelve minimal raw lower stars and exact source/normal/period maps.145 additional checks enumerate the small-resolution compact one-end points. The324-chart common-refinement matching and321-contraction histogram remain open.'
c['smallest_IL_input']='Ordered primitive common-edge chain on native3y-x-36r=0 with actual period closure and quotient-subdivision data; full derivation in K111_IL_edge_chain_reduction.md.'
(p/'K111_coverage.json').write_text(json.dumps(c,indent=2,ensure_ascii=False)+'\n')
a=json.loads((p/'row_assessments.json').read_text());r=a['night:P3K.111']
r['confidence_line']+=' Fresh2018-check reconstruction now covers all twelve minimal lower source stars and their full maps;145 checks cover the stated small one-end compact resolution.'
r['remaining_risk']='The full common/endpoint fixed-stratum atlas supplying CFL(2723,19124) remains unreconstructed. For IL, the smallest absent input is the ordered native common-edge chain on3y-x-36r=0 and its complete quotient subdivision: it must produce and identify the actual324-chart source stars and321-contraction histogram. The minimal three-chart stars and normal degrees are freshly checked. Historical computation records, F41 original chain arrays, K94 simultaneous-source construction and larger F41/F46/K96 chain inputs retain their precise inherited scopes. No absolute seed closure is asserted.'
(p/'row_assessments.json').write_text(json.dumps(a,indent=2,ensure_ascii=False)+'\n')
print(len(rows),'events;',c['fresh_exact_checks'],'scoped K111 exact checks')
