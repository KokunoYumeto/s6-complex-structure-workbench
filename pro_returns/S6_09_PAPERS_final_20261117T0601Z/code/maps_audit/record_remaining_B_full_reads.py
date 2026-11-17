"""Register complete receiving-proof reads; keep source/program/credit gates distinct."""
from pathlib import Path
import csv,hashlib,json

ROOT=Path(__file__).resolve().parents[3]; W=ROOT/'deliverables/work/maps_audit'
META=dict(reader='GPT-6 Astra (OpenAI, ChatGPT Pro mode)',effort='Pro',date='2026-11-17')
spec={
'B.5.2':('Nonabelian presentation and its elimination; primitive finite H1 bases; both integral finite H2 pullback lattices and their parity test; alpha1/alpha2/c2; cusp kernel tori; sweep/contraction sign and the primitive coefficient +1; Mayer–Vietoris, duality, Euler and Hurewicz/Whitehead; retained actual normal framing.', ['B.5.1 complete topological attachment and its source gate','Hatcher relative Hurewicz/Whitehead exact source scope'], ['maps_cw.py']),
'B.6.1':('Degree-six pullback replaces monodromy by its sixth power; image/kernel of multiplication by6 on Z/28; inverse of3 modulo14; exact two-residue scope and absence of an unconditional restriction.', ['K3 identification of the oriented mapping class with Theta7'], []),
'B.6.2':('Read the entire synthesis and all retained failed approaches. Checked the endpoint-versus-isotopy distinction for a fractional deck interpolation, the real reflection exponent2 modulo3, and the precise downstream references for the actual zero result.', ['B.6.21–25, fully read in this batch','Olbermann/Krylov/Randal-Williams source comparison for the retained historical approaches'], []),
'B.6.3':('Full moving-zero comparison, cancellation of both logarithmic additions, extension across both primitive rank-one fans, four monodromies, rational specialization, parabolic quotient bases and parameter coboundaries; Leray dimension exhaustion and integral Torelli conclusion.', ['D.3.2 actual conifold smoothing and its b3','K8 actual holomorphic closing map (transferred to I)','Exact matrix certificate'], ['maps_smoothing_monodromy.py']),
'B.6.4':('Affine return defects; nilpotent fibre connection; the two coinvariant identities; actual local skyscraper classes and their Wang boundary terms; Cech identification of d2; dimension exhaustion and zero swept critical classes; saturated vertical tangent bundle/Koszul sign; integral p1 and Kreck normal-framing implication.', ['Krylov Section2.1 equation(2) and Theorem2 normalization','D.3.2 smoothing topology','Exact cohomology certificate'], ['maps_mapping_torus_cohom.py']),
'B.6.5':('Fixed-s rather than conformal quadratic germs; derivative retraction and ruling-preserving SO(4,C) reduction; explicit quaternionic equivariant trace, common link and orientations; primitive H3 trace restriction, Wang injection, p1=0/signature=0; both spin lifts and normalized Eells–Kuiper gluing.', ['Crowley–Nordstrom2019 §1.4 equations(2)–(3)','K3 oriented mapping-torus/sphere identification','B.6.4 central subgroup'], []),
'B.6.6':('Every higher-family finite norm solution and split cusp winding; relative vertical sheaf through coalescence; vanishing H1 correction depending holomorphically on both parameters; scaled parabolic coboundaries and local Wang terms; unchanged critical-curve tangent calculation and fixed-s trace.', ['K1 complete higher-family holomorphic comparison','D.3.2 surgery recognition','B.6.3–5, fully read in this batch'], []),
'B.6.7':('The actual ordinary affine automorphism; based homotopy conjugacy quotient by delta; unique rational solution (1/6,0,0); invariance under basepoint/peripheral/integral marking changes; exact order6, residual scalar windings and root obstruction.', ['K8 actual origin and finite affine defects','Exact quotient Smith/cocycle certificate'], ['maps_ordinary_shear_obstruction.py']),
'B.6.8':('Higher repeated-norm defects, primitive quotient coboundary and first coordinate b/6−kN1; b=±1 forces exact order6; special original-pair integral change of marking and limitations of the obstruction.', ['K1 finite norm solutions','Exact symbolic identities'], ['maps_ordinary_shear_obstruction.py']),
'B.6.9':('Unique boundary Spin-c structure; both spin structures induce it; expansion of the normalized Spin-c formula, all coefficients and relative lift conditions; torsion-free H4 ensures c2 restriction vanishes. Conditional scope retained.', ['Crowley–Nordstrom2021 §2.2 equation(2.1)','B.6.4–6 and K3 boundary invariants'], []),
'B.6.10':('Connected cyclic cover, branch indices and Riemann–Hurwitz; actual good-reduction charts; elliptic-surface invariants; height and section intersections; all canonical-form valuations and eigensections; base/surface fixed-point traces and exact Fourier characters.', ['Shioda1990 Theorem8.6 and Proposition8.12; section self-intersections','Standard elliptic canonical/direct-image formulas','Exact character certificate'], ['fourfolds_B6_cover.py']),
'B.6.11':('Full normalization intersection formula with both positive cross terms and the negative difference pairing; conductor relation, surface translation matrix and image/radical; signature+2; tangent-normal c1 identity, integral injection, boundary cohomology and primitive nonspin class.', ['K13 A.2.2 normalization H2 calculation after the conductor blow-up and small resolution: exact full upstream proof locator requested from root','Engel Lemma2.1 section intersections','Exact plumbing matrix certificate'], ['fourfolds_B6_plumbing.py']),
'B.6.12':('Both character parabolic complexes and pure braid conventions; hyperbolic commutators; nonconstant one-dimensional period domains and countable rational Hodge loci; equivariant Mordell–Weil embedding, even integral norm and primitivity; exact norm image12ZP and both zero-preserving automorphism cases.', ['Griffiths1968II Theorem(1.1)','Shioda1990 Lemmas8.1–8.3, Theorems8.6–8.9','B.6.10 geometric family and Hodge characters','Exact braid/cocycle certificate'], ['maps_component_periods.py']),
'B.6.13':('Analytic exponential sequence including nodal stalk; local group-cohomology witnesses at all three stabilizers; coarse sheaf H2/H3 vanishing and transgression; finite-order4 invariant torsor via exact lattice coinvariants and Hodge characters; compact gluing and exact F^12; Picard obstruction, finite splitting cover, narrow height degree12d and unique Pic0 correction.', ['B.6.10–12 exact source scopes','Shioda1990 Theorem8.6 and Proposition8.12','Standard equivariant Cech spectral sequence and relative Picard descent','Exact local/norm certificates'], ['fourfolds_B6_torsor_local.py','maps_component_periods.py']),
'B.6.14':('Reduced irreducible central fundamental class and zero relative intersection map; nonzero extended base class via absent elliptic invariant vectors and Leray; preservation through the stated modifications; Wang b2=0 contradiction; exact local equation xy=rz and multiplicity12 retained under a free quotient.', ['B.6.10 actual Jacobian monodromy','B.6.11 semistable retraction context','Exact local root/multiplicity certificate'], ['fourfolds_B6_torsor_local.py']),
'B.6.15':('Wang generators and unimodular xy pairing; spin Dirac congruence ell=4k mod24; tangent/Spin-c determinant of the disc bundle; full Gysin free/torsion groups; Thom relative lifts and all three characteristic pairings; both nonzero-k formulas and zero-k case.', ['Spin Dirac index theorem exact source scope','Crowley–Nordstrom2021 Spin-c formula','Exact rational coefficient certificate'], ['maps_free_circle.py']),
'B.6.21':('Original |k|=1 cup normalization and independent ell=−4 force k=−1 by the spin congruence; free invariant and the actual rank-one trace correction both vanish; K3 fixes the oriented sphere class.', ['B.6.16–20 complete actual cap/critical/trace proof chain, previously read','K3 Eells–Kuiper normalization'], []),
'B.6.22':('Higher finite circle freeness; exact integral parameter-lift change removing the cusp defect; unchanged actual quotient map and holomorphic unit extension; every changed finite/nodal defect and peripheral relation; oriented tangent invariant ell=−2h and unchanged parametrized spin trace.', ['K1 actual fixed-data comparison and sphere theorem','B.6.16–19, previously read','Exact all-parameter symbolic calculation'], ['manifolds_mapping_general.py']),
'B.6.23':('Every cap primitive in the actual marked quotient, cancellation using P=4A+3B, all four raw collar cube terms and constant orientation calibration; P=−1 inversion reverses circle and quotient orientations together, leaving both characteristic numbers unchanged.', ['B.6.20 complete collar multiplicative comparison, previously read','B.6.22 actual higher caps, fully read','Exact symbolic all-multiplicity certificate'], ['manifolds_mapping_general.py']),
'B.6.24':('Both boundary spin choices; equality of the actual primitive boundary torsion generator; rank-one reciprocal linking forms fix the trace sign for |k|>2; |k|=1 cancellation and |k|=2 Eells–Kuiper denominator exclusion; all positive multiplicities and exact zero class.', ['B.6.19 Borel restriction identification and rank-one trace, previously read','B.6.22–23 actual higher cup/tangent invariants','K3 Theta7 normalization','Exact trace/linking coefficient certificate'], ['maps_trace_linking.py']),
'B.6.25':('Endpoint-flat isotopy defines the stated well-defined smooth mapping-torus product diffeomorphism for (z,1)~(Phi z,0); product boundary orientation, parallelizability, zero middle characteristic numbers, one0/one1-handle and extension of either circle spin structure.', ['B.6.24 zero class, fully read; no filling assumed before that conclusion'], []),
}
batch=json.loads((W/'remaining_B_batch.json').read_text())
rows=[]
for item in batch:
 ident=item['id'];scope,deps,programs=spec[ident]
 sources=[]
 for src in item['sources']:
  p=ROOT/src['file']; body='\n'.join(p.read_text().splitlines()[src['start_line']-1:src['end_line']])+'\n'
  sources.append(dict(**src,source_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),read_block_sha256=hashlib.sha256(body.encode()).hexdigest()))
 rows.append(dict(id=ident,statement=item['statement'],source_status=item['source_status'],
                  current_event_id='new-maps-B-remaining-full-20261117:'+ident,
                  source_blocks=sources,receiving_proof_fully_read=True,mathematical_read_scope=scope,
                  outcome='Complete receiving proof read and independently rederived; no internal contradiction found. Separate exact upstream/source/program/credit gates are retained below.',
                  dependency_closure=deps,programs_to_attach=programs,program_gate='not inferred from proof reading; separate code-read/rerun record required',
                  credit_gate='per-result AC26/E26/DGKX/elsewhere comparison still to be recorded',
                  prior_checks_retained=item['prior_checks'],previous_check_record=item['current_recorded_check'],
                  **META))
(W/'maps_B_remaining_full_checks.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
fields=['id','statement','source_status','receiving_proof_fully_read','mathematical_read_scope','outcome','dependency_closure','programs_to_attach','credit_gate','reader','effort','date']
with (W/'maps_B_remaining_full_checks.csv').open('w',newline='') as f:
 writer=csv.DictWriter(f,fieldnames=fields);writer.writeheader()
 for row in rows:writer.writerow({k:json.dumps(row[k],ensure_ascii=False) if isinstance(row[k],list) else row[k] for k in fields})
events=json.loads((W/'check_events.json').read_text()); known={x.get('event_id') for x in events}
for row in rows:
 if row['current_event_id'] not in known:
  events.append(dict(event_id=row['current_event_id'],results=['MAPS:'+row['id']],scope=row['mathematical_read_scope'],outcome=row['outcome'],remaining_dependencies=row['dependency_closure'],locators=row['source_blocks'],**META))
(W/'check_events.json').write_text(json.dumps(events,ensure_ascii=False,indent=2)+'\n')
inventory=json.loads((W/'results_audit.json').read_text()); byid={x['id']:x for x in rows}
for row in inventory:
 if row['id'] not in byid:continue
 new=byid[row['id']]
 row.setdefault('prior_audit_states',[]).append({k:row.get(k) for k in ['audit_state','your_check','audit_notes']})
 row['audit_state']='full receiving proof read; separate source/dependency/program/credit closure tracked'
 row['your_check']=new['mathematical_read_scope']
 row['audit_notes']=new['outcome']+' See maps_B_remaining_full_checks.json.'
 ids=row.setdefault('check_event_ids',[])
 if new['current_event_id'] not in ids:ids.append(new['current_event_id'])
 row['current_full_read_record']='deliverables/work/maps_audit/maps_B_remaining_full_checks.json'
(W/'results_audit.json').write_text(json.dumps(inventory,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(full_receiving_proofs=len(rows),line_ranges=sum(s['end_line']-s['start_line']+1 for row in rows for s in row['source_blocks']),mathematical_certification_scope='Receiving proof only; gates separate')))
