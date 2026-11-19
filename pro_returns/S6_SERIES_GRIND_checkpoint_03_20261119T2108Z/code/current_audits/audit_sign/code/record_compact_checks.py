import csv,hashlib,json
from pathlib import Path
D=Path('/workspace/scratch/6c4e6df38b6d/S6_SERIES_GRIND_work/audit_sign')
who='GPT-6 Astra (OpenAI), ChatGPT Pro mode, reasoning effort inherited (not separately exposed), S6_SERIES_GRIND/sign_theorem_audit'
items={
34:'All fourteen proof steps checked after recording the root-torsor mechanism. Verified the exact exponential pushout, full Picard classes including degree-zero data, inertia descent, signed divisor representations, vertical extensions on the auxiliary blowup/root surface, free coarse quotient, prescribed multiplicity-one component, actual product off zero, and Euler-zero SNC supports. No fault found.',
41:'All twelve numbered steps and final integral/coherent restriction maps checked. Verified dual axis-line maps, finite Hausdorff proper plumbing, exact period quotient and degree-one height comparison, nodal cubic pencil, section-translation graph extension, actual central Tate series and prescribed multiplier, compact suspension replacement and primitive cohomology maps. Opened Schutt-Shioda section7.6 pp33-34 and Papikian Theorem2.1/equation2.1 p2. No fault found.',
42:'All twelve steps and intervening constructions checked. Verified the compact hyperelliptic base and order-r translation, weighted smooth nonzero line chart, exact nonlinear contraction, uniform polynomial norm bound and arbitrary-beta compact quotient, actual four-period tori, reduced fibre and canonical orders, free half-translation quotient to P1, and integral Seifert pair and cohomology maps. No fault found.',
48:'All fourteen steps checked after the related UN51/57 mechanism had been read; not a separate blind reconstruction. Verified common lattice sign/transversality, a-not-equal-one by the explicit embedded elliptic map, degree-d Tate base change and resolution charts, fixed integral transport of secondary groups, affine constants, exact compact replacement, and secondary period divisor. No fault found.',
51:'All ten numbered steps and final all-ruled clause checked. Verified exact line-puncture lattices, affine dual-normal maps, injected semidirect-product group and coframe quotient, the single-Hopf obstruction, ruled moving frame and full degree-zero line, complete affine-period adjustment, and compact suspension comparison. UN48 compact input now checked. Arbitrary all-ruled horizontal translation is retained. No fault found.',
55:'All eleven steps checked. Verified actual coordinate/lattice change, preservation of the full elliptic translation, inverse twistor map and everywhere-positive determinant, proper period quotient, exact fillings at zero/infinity and their reversed logarithmic coefficient, and compact gluing including the one-component self-identification. No fault found.',
61:'All seventeen steps checked after independent tree/period derivation. Verified actual leaf incidence maps, forced root(pg,q)=(1,2), residue minimum and minimality, explicit marked elliptic fibration, normal orders and path heights, common core period, full inverse torsor, identical boundary pushouts and integral Chern commutator, compact twistor family and exact reconstruction of all marked torsors. UN60 construction input now checked individually. No fault found.'}
p=D/'CHECK_EVENTS_additions.tsv';rows=list(csv.DictReader(p.open(),delimiter='\t'));seen={r['event_id'] for r in rows}
for n,outcome in items.items():
 label=f'cdp:st:C.2.UN.{n}';typ='targeted proof check and source comparison' if n==41 else 'targeted proof check';eid='ce:grind-sign:'+hashlib.sha256((label+typ+outcome).encode()).hexdigest()[:16]
 if eid not in seen:rows.append(dict(statement_id=label,date='2026-11-19',who=who,type=typ,outcome=outcome,event_id=eid,phase='current'))
with p.open('w') as f:
 w=csv.DictWriter(f,fieldnames=['statement_id','date','who','type','outcome','event_id','phase'],delimiter='\t');w.writeheader();w.writerows(rows)
c=json.load(open(D/'UN_coverage.json'))
for r in c:
 n=int(r['label'].split('.')[-1])
 if n in items:r['current_audit_scope']=items[n]
(D/'UN_coverage.json').write_text(json.dumps(c,indent=2)+'\n')
s=json.load(open(D/'SOURCE_OPENINGS.json'));keys={r['key'] for r in s['sources']}
for r in [dict(key='SchuttShioda2010',url='https://arxiv.org/pdf/0907.0298',reading='Original author arXivv3 opened',locators='section7.6 pp33-34; section7.2 Lemma7.3 p32',statement_scope='UN41/43/48 actual extension of section translations on the relatively minimal elliptic surface and its multiplicative smooth central group.',refs=['turn154562589view0','turn529120295view1']),dict(key='Papikian2004Tate',url='https://math.stanford.edu/~vakil/snowbird/mihranjun21.pdf',reading='Author notes dated13 June2004 opened',locators='Theorem2.1 and equation2.1 p2; j-series p3',statement_scope='UN41 exact complex multiplicative uniformization, two coordinate series and a4/a6 coefficients; the manuscript independently computes the central nodal coordinate and matches the prescribed section.',refs=['turn154562589view1','turn529120295view0'])]:
 if r['key'] not in keys:s['sources'].append(r)
(D/'SOURCE_OPENINGS.json').write_text(json.dumps(s,indent=2)+'\n')
print(len(rows),'events')
