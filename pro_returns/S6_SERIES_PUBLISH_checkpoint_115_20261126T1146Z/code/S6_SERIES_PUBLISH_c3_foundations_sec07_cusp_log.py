from S6_SERIES_PUBLISH_c3_foundations_sec07_helpers import *
from datetime import datetime,timezone

prefix='S6_SERIES_PUBLISH_sec07_cusp'
path=OUT/(prefix+'_defects.tsv')
with path.open(newline='') as f:
    reader=csv.DictReader(f,delimiter='\t');fields=reader.fieldnames;rows=list(reader)
for row in rows:
    row['review_status']='Complete original/current and receiving P4.28/CR.4/P295 proofs read and compared; both guards replay once; root admission pending. Bounded transfer only.'
    if row['type']=='D25' and row['statement_id']=='lem:II:boundary-deformation-transport':
        row['review_status']='OPEN inherited unequal-multiplicity premise in unchanged P4R.14/P4R.15/P4.41/P4.45 applications; P295 and the merged cusp owner themselves are fully read and proved at their stated scope.'
with path.open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');writer.writeheader();writer.writerows(rows)
with (ROOT/'agents/continuation3_foundations/S6_SERIES_PUBLISH_foundations_CHECK_EVENTS.tsv').open(newline='') as f:
    event_fields=next(csv.reader(f,delimiter='\t'))
now=datetime.now(timezone.utc).isoformat()
data=[
 ('transport','lem:II:boundary-deformation-transport','Read the full original/current P4.28 and CR.4 boundary constructions, and the complete receiving P295 proof. Its product chart yields dg_tau(W)=0 and d rho(W) nonzero; the corrected field V−d rho(V)W/d rho(W) solves the parameter equation and is tangent to the fixed boundary. Partitions of unity preserve those equations. The proof retains the finite critical-value argument, uniform outer value, local regular-value change, target path, inverse parameter flow, nested-ball inclusions, complex orientations and compact intersection pairing. The final torus inclusion explicitly uses xi F=g0^m. Its product-chart scope allows a fixed transverse function q independent of a tangential coordinate; it does not identify different q or claim a reduced-function fibre lies in an unequal-power full fibre.'),
 ('cusp','night:P4.28','Read all eight old P4.28 proof items, all seven old CR.4 proof items, and the complete merged receiving proof. Generic cusp plus smooth singular curve proves local irreducibility and supplies xi F=g^m after an explicit unit root. The critical germ is the same curve because the function is constant zero on every critical component through the point. The rank-one quadratic form uses the original invertible x+(b/a)y map over C{z}; the exact Morse coordinate and kernel residual remain. The rank-one residual-zero family keeps its x^2−zy^3 map and square −6 compact spherical class. The rank-zero direct family g+epsilon x^2+delta y^3 keeps C.CR.16, and its single Weierstrass/Tschirnhaus calculation keeps C.CR.17/18. The prepared family U_delta(Y^3+x^2(H_delta+eta)) retains its full nested-ball comparison. In the same Phi_delta coordinates, the direct family is exactly U_delta(Y^3+x^2(H_delta+epsilon/U_delta)); thus both original families and their explicit relation remain. The simultaneous cube-root map gives the binomial (3,2,1) sphere of square −4, as a continuous spherical cycle, without requiring an embedded representative. The explicit finite normalization and rational inverse remain. A final weighted unit-coordinate map gives the exact normal form for every original reduced generator.'),
 ('cr4','cdp:st:C.2.CR.4','Read the complete original/current and receiving CR.4 content against the merged early cusp owner. Tag01BT and the stable statement label now alias P4.28; C.CR.15–18 retain all permanent targets and section-numbered equation labels. Its local holomorphic-map scope and full-critical-curve input are covered by the receiving singular-curve statement and the proved critical-germ comparison. The unit and common multiplicity are related through the full-map root, then the explicit coordinate change (X,Y,z)→(v^(1/2)X,v^(1/3)Y,z). The old rank-one residual u is the receiving h1 under the same Morse map. Its full direct perturbation and all Weierstrass divisibilities remain. The old separate boundary and asphericity proofs now apply P295 to exactly the A2 product charts and xi F=g^m. No conclusion or labelled formula is removed.'),
 ('consumers','night:P4.28','Read all complete current proofs of P4.29, P4R.14, P4R.15, P4.41 and P4.45, and compared the complete CR.5 and UN.10 uses. P4.29/CR.5/UN.10 have an irreducible full fibre mS, so the merged local cusp owner applies with its original maps. P4R.14 retains the quadratic-matrix coordinate use and has A3 boundary charts; P4R.15 has A_(m_i−1) boundary charts; P4.41 uses nested A3 comparisons; P4.45 uses moving D4 charts. The latter four broad standing-domain statements do not by themselves identify the reduced function with a common power root of the full map when component multiplicities differ. Their existing statements and proofs remain unchanged in these bounded guards; their full-fibre transport premise is explicitly OPEN for the following weighted-function comparison. No claim of a counterexample, refutation, stronger proved scope or conditional replacement is made.')
]
source_note=(' Fresh primary source https://arxiv.org/pdf/1512.02840v1, SHA256 b889ac5d0826e5e539a3df5db1f523d81cc343cccf9de395cd42eb1cebc05c58, 1567333 bytes. Read pp.1–4: Section3 p.3 states the boundary-admissibility condition and Milnor-data comparison; Section3.1 pp.3–4 gives the semilocal critical-value and local-fibre data. This records only those opened loci, not a full reading of the paper. Both bounded guards replay once; every existing label and target has unchanged multiplicity. No independent-check credit, required-check increment, integrated compilation or final rendered page reading is claimed.')
events=[]
for suffix,owner,outcome in data:
    event=dict.fromkeys(event_fields,'')
    event.update(statement_id=owner,date=now[:10],who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; inherited effort not separately exposed; continuation3 foundations',type='used and rechecked in this run',outcome=outcome+source_note,event_id='publish:c3:foundations:sec07:cusp:'+suffix,phase='publication boundary and cusp consolidation',source_file=str(path.relative_to(ROOT)),source_event_type='used and rechecked in this run',evidence_group='publish:c3:foundations:sec07:cusp',date_utc=now,where='P295 immediately before P4.28; CR.4 alias at the merged cusp owner; unchanged external consumer comparison')
    events.append(event)
with (OUT/(prefix+'_CHECK_EVENTS.tsv')).open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=event_fields,delimiter='\t',lineterminator='\n');writer.writeheader();writer.writerows(events)
lines=['# Bounded boundary-transport and cusp consolidation','',
 'Scope: P295 immediately before P4.28 and the merged P4.28/CR.4 cusp owner. Both original/current proofs, the whole receiving proof, and the complete named external consumer proofs were read. No subsection completion or movement credit is claimed.','',
 '| Class | Bounded status | Reason |','|---|---|---|']
for kind in [f'D{i:02}' for i in range(1,26)]+['restructuring']:
    state='done';reason='The complete bounded receiving text was read for this class; no additional instance remains in this transfer. The enclosing contracted-boundary subsection remains open.'
    if kind=='D10':reason='P295 is a titled numbered owner with permanent tag and explicit data; CR.4 is a statement alias at the one cusp owner. Existing labels and targets remain.'
    if kind=='D12':reason='One boundary construction and one Weierstrass calculation serve the two original cusp proofs. Both perturbation families remain with their exact identity in the same coordinates; no unproved family identification is used.'
    if kind=='D16':reason='Every original cusp conclusion and formula remains in the single proved owner, including exact function normal form, full-map root, smooth normalization and continuous spherical cycles. Existing closures are preserved.'
    if kind in ['D17','D18']:reason='The primary Siersma–Tibar admissibility and comparison loci were freshly opened at Section3/3.1 pp.3–4. The product-chart verification and compact-cycle map comparison stay because they establish the exact hypotheses needed here.'
    if kind=='D19':reason='C.CR.15–18 have section equation numbering and their original labels/targets. All pre-existing P4.28 identifiers remain; P295 introduces no legacy tag.'
    if kind in ['D14','D24','restructuring']:
        state='open';reason='The bounded order is P295 then the merged cusp owner, earlier than CR.5/UN.10. Admission and the whole contracted-boundary pass remain. The four broad-domain weighted-function applications require the explicitly logged comparison.'
    if kind=='D23':
        state='open';reason='The complete source, coordinate equations and alias placements were read. Integrated compilation and final page reading remain with root.'
    if kind=='D25':
        state='open';reason='The new P295 and cusp proofs are established at their exact stated scopes. P4R.14/P4R.15/P4.41/P4.45 still need a proved actual-full-function comparison for unequal component multiplicities; their original domains are retained, with no conditional replacement or counterexample claim.'
    lines.append(f'| {kind} | {state} | {reason} |')
(OUT/(prefix+'_status.md')).write_text('\n'.join(lines)+'\n',newline='\n')
consumer_map=r'''# Exact cusp and boundary consumer map

| Consumer | Preserved input and map | Bounded result |
|---|---|---|
| P4.28 / CR.4 | Generic cusp on a smooth singular curve forces local irreducibility. A unit root gives `xi F=g^m`; product charts have `q=X²+Y³`. | One complete cusp owner, with CR.4 statement alias and C.CR.15–18. |
| P4.29 | Its irreducible full fibre is `mS`; its proved smooth conductor and generic cusp meet the common owner's local data. | Both product-cusp uses remain valid; complete proof read. |
| CR.5 | The CR.1 irreducible full fibre is `mS`; its genus-two smooth reduced conductor has the cusp alternative. | Same local cusp normalization contradiction; complete proof read. |
| UN.10 | Local proper-map input explicitly has irreducible full fibre `mS`; P293 supplies the genus-two smooth conductor. | Same local cusp normalization contradiction without ambient Betti input. |
| P4R.14 | DVR quadratic coordinate map remains in P4.28. Boundary product charts have `q=X²+Y⁴`. Its prepared polar model is `X(Y²+XH)`. | Boundary transport for the deformed reduced function is within P295. Actual full-map unequal powers remain open. |
| P4R.15 | Boundary factors give the explicit Morse/root charts `q=X²+Y^{m_i}`; the local suspension is `X²+g(Y,Z)`. | Same boundary transport; unequal powers of two analytic factors when `g` is a square remain open. |
| P4.41 | The displayed conductor-derived functions and nested moving A3 curves use `q=X²+Y⁴`. | Reduced-function compact-cycle transport is covered; the full weighted fibre map remains open. |
| P4.45 | The displayed binary cubic `F(u,x,y,H)` and moved curve `H_s=0` retain ordinary-triple transverse type. | Product-chart verification and the actual full weighted cubic factors require the following comparison; no original hypothesis is narrowed. |

## Direct and prepared cusp families

For the root function `g` chosen from the original full map, the direct family is `g_(epsilon,delta)=g+epsilon x²+delta y³`. Let `Phi_delta` be the Tschirnhaus coordinate change for `g_(0,delta)`, keeping `x,z`. Then

`g_(0,delta) o Phi_delta^(-1) = U_delta (Y³+x²H_delta)`,

`g_(epsilon,delta) o Phi_delta^(-1) = U_delta (Y³+x²(H_delta+epsilon/U_delta))`.

The prepared family is `U_delta (Y³+x²(H_delta+eta))`. The displayed equalities provide the exact relation; no parameter-preserving identification of `eta` with a constant `epsilon/U_delta` is used. Each chosen simple zero has the explicit coordinate `Z=H`, followed by simultaneous multiplication of all three coordinates by the cube root of `U`. The prepared route retains its two nested-ball transports. Both yield the same written binomial target through their respective maps.

## Strongest settled unequal-power reduction

For a factor-preserving local model `(X-Y^k Z^l)^a (X+Y^k Z^l)^b=t`, put `d=gcd(a,b)`, `a=d a0`, `b=d b0`. On a chosen component, choose constants `c0,d0` with `c0^a0 d0^b0=t^(1/d)`. The exact parameterization is

`X-Y^k Z^l=c0 s^b0`, `X+Y^k Z^l=d0 s^(-a0)`,

and hence `Y^k Z^l=(d0 s^(-a0)-c0 s^b0)/2`. Bezout integers `r,t` with `b0 r-a0 t=1` give the inverse `s=((X-Y^k Z^l)/c0)^r ((X+Y^k Z^l)/d0)^t`. The subsequent compact matching-sphere support and root map near an arc avoiding `s=0` remain to be compared with A.5.15 before this is credited as a full-fibre sphere construction.

For two analytic branches the quadratic discriminant is a square, so the existing R14 simple-discriminant-zero perturbation is not automatically a factor-preserving family with unequal powers. No assertion of nonexistence of another comparison, or of a refuting example, is made.
'''
(OUT/(prefix+'_consumers.md')).write_text(consumer_map,newline='\n')
print(f'{len(rows)} defect rows, {len(events)} exposed-reading events; P295 allocated; unequal-multiplicity consumer row remains OPEN.')
