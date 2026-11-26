from S6_SERIES_PUBLISH_c3_foundations_sec07_helpers import *
from datetime import datetime, timezone

prefix='S6_SERIES_PUBLISH_sec07_contracted'
path=OUT/(prefix+'_defects.tsv')
with path.open(newline='') as f:
    reader=csv.DictReader(f,delimiter='\t')
    fields,rows=reader.fieldnames,list(reader)
for row in rows:
    row['review_status']=(
        'Complete original/current and receiving proofs read and compared, including '
        'P293, UN9, CR1, CR2, CR3, CR5, CR6, UN10, MH3, all of R6/A.5.17 '
        'and all current/receiving UN7. P300 first-clause generality and the full '
        'P4.52 strict-transform consumer were reread and compared. Six guards replay once; every old label and '
        'target has unchanged multiplicity. All25-class subsection source pass done; '
        'global placement/front matter and integrated build/page reading remain with root. '
        'No new required-check or independent-check credit. Root admission pending.')
with path.open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n')
    w.writeheader();w.writerows(rows)

with (ROOT/'agents/continuation3_foundations/S6_SERIES_PUBLISH_foundations_CHECK_EVENTS.tsv').open(newline='') as f:
    event_fields=next(csv.reader(f,delimiter='\t'))
now=datetime.now(timezone.utc).isoformat()
reading=[
 ('duality_alias','lem:II:contracted-section-duality',
  'Read complete original/current CR2 and complete current/receiving P293. '
  'Every CR2 conclusion is P293 restricted to the global CR1 data: '
  'g in {1,2}, one normalization point above q, smooth reduced conductor at q, '
  'generic node or cusp. The identity map on S,T,Z,C,V,p0,q proves the consolidation. '
  'CR2 tag01BR/label moves onto P293. Every body consumer was searched: CR3 '
  'explicitly retains all CR1 global hypotheses, while CR5 and UN10 are consolidated '
  'at UN10. P293 proof and its pre-equation C.UNCR.3 alias are unchanged. '
  'The full receiving UN9 proof was read in its earlier position; its statement '
  'and proof are byte-identical to the admitted product-node owner.'),
 ('topology','cdp:st:C.2.CR.1',
  'Read complete current and receiving CR1, and complete P252, P232, P246, P294, '
  'P245, P4R.1, P300, P293, P222, P282 and VII2 inputs. '
  'P252 uses exactly Z→Z0,D=2C+V and the adjunction class from P281. '
  'The shifted-gcd proof is retained, and the complete coefficient-one-leaf induction '
  'moves from CR3 at the same global scope. P232 uses Z1=W,Z2=Wprime,m=d and the '
  'same a; C.CR.5 aliases its existing Jacobian equation. P300 uses N=T,T=Z,nu=eta, '
  'rho=h and the same dualizing generator. P294 uses h:Z→S,A=D_red,C=Gamma_red, '
  'inclusion j and k=h|D; j* is invertible and k* zero. P4R.1 and P245 bound '
  'the free rank by one, and the original global D1.9 class excludes zero. '
  'The coherent normalization/duality calculation retains all C.CR.1/8/9 values. '
  'VII2 first assertion has exactly the torsion-canonical/chi-zero scope. '
  'The chosen v,N0 and Euler formula use the same blowdowns and P294 Euler map.'),
 ('genus_two','cdp:st:C.2.CR.3',
  'Read complete old/current and receiving CR3. The statement explicitly inherits '
  'CR1 global hypotheses and g=2; the broader CR2 alias does not broaden it. '
  'The exceptional fibre E0, first nonexceptional vertices, strict coefficient-one '
  'leaves, one-branch attachments at p and absence of further exceptional tails '
  'remain. Under the node assumption D_T=(pi D_red)_red is the rational star. '
  'Every image curve passes through the smooth q, so Gamma_red=G has n=1. '
  'C.CR.8 makes each possible multibranch point a two-branch point. P255 applies '
  'to the exact eta:T→S, whole G and D_T. Its beta(D_T)≥b0(D_T)=1 contradicts '
  'the star. The rational unibranch compact-normalization homeomorphism and pi1 '
  'contradiction remain, as do the cusp coefficient-two/degree-one conclusions.'),
 ('genus_euler','cdp:st:C.2.UN.10',
  'Read complete old/current and receiving UN10, CR5 and MH3, complete current/receiving '
  'UN9, and the admitted full product-cusp owner. The same local proper-map '
  'normalization/resolution data apply P293. Normal-implies-regular-in-codimension-one '
  'puts each singular curve in the conductor. The full-critical-curve node theorem '
  'gives two normalization points; the exact cusp normalization (u,z)→(u³,−u²,z) '
  'is smooth and contradicts the contracted positive-genus section. '
  'The original local g=1 conclusion remains. Compact Y, b1=b2=0 and base P1 '
  'are explicitly stated before the global Euler clause. MH2 on the same ruled Z '
  'gives e(S)=0, and the identical CR1 blowdowns give n=v−N0. '
  'C.CR.19, C.CR.20, C.MH.15 and tags01BU/01C6/01CN remain. The last two '
  'equation payloads are together e(S)=n−v+N0=0,n=v−N0, with the alias hook '
  'before the formula. Full UN7 was reread to confirm the removed later '
  'exclusion sentence stays proved there. A temporary receiving explanatory '
  'implication was corrected before admission; no original theorem was refuted.'),
 ('planar_conductor','cdp:st:C.2.CR.6',
  'Read complete old/current and receiving CR6 and complete P293/P222/P282. '
  'The residue quotient gives a conductor coordinate x; its pure one-dimensional '
  'quotient makes the remaining plane ideal unmixed height one and principal, '
  'with full multiplicities. Finite curve duality is P282 on the same plane curve. '
  'Reopened the primary van Straten1987 thesis, printed p60 (PDF p63), as rendered '
  'image and text, Sections2.2.2/2.2.3. The proper bimeromorphic smooth-source '
  'rho gives R1 rho_* omega=0 and the residue surjection. A lift differs from '
  'a du∧dv/f_D by a holomorphic two-form, so the first exceptional order is '
  'ord(a)+1−m and C.CR.22 follows for every representative. The transverse '
  'coordinate forces m≤2. Quadratic completion/unit maps, odd exponents via P282, '
  'even semigroup conductor2s and global degree sums remain. Primary URL: '
  'https://download.uni-mainz.de/mathematik/Algebraische%20Geometrie/DvS-Publikationen/'
  'DvS_1987_weakly%20normal%20Surface%20Singularities%20and%20their%20improvements.pdf; '
  'SHA256 583d6e337304958cb3dfb6519cb8c82901928667ccacfeae74d0e03a19d1e906. '
  'This is an exact theorem/application locus opening, not a whole-thesis or '
  'original-general-vanishing-proof reading.'),
 ('proper_divisor','lem:II:proper-conductor-divisor',
  'Read complete original/current R6 and complete receiving P300. The same '
  'meromorphic pullback defines D; local generators change by units. P222 gives '
  'the conductor canonical module and positive strict pole coefficients. P243, '
  'adjunction/minimality and degree zero of rho*omega_S on curves mapped to points '
  'give Md=−b,b≥0 for every compact reduced hypersurface. A positive-geometric-genus '
  'exceptional component has p_a≥1 and negative square, so K.E>0 and the whole '
  'block has positive coefficients. The first three steps prove the complete '
  'general first clause; only the fourth step imposes the proper torus hypotheses. '
  'The unit branch-conductor implication is explicit through the product '
  'normalization and an idempotent extended by zero in a local ring, proving '
  'normalization is an isomorphism at that image. Full A.5.17 was reread and '
  'A.5.15 hypotheses compared: the isolated normal point has full f=u g^m, '
  'root H=exp(log(u)/m)g, and identity inclusion '
  'K∩H^−1(delta)→f^−1(delta^m). The complete sphere/transport proof excludes '
  'the point. Every exceptional block meets strict conductor and has positive '
  'coefficients. All support/complement conclusions remain at proper-disc scope. '
  'P300 precedes R6 and uses no later P281/UN17 numerical premise.'),
 ('strict_transform','night:P4.52',
  'Read complete current P4.52 and complete generalized receiving P300. '
  'The exact general-clause application is beta:Xprime→X the point blowup, '
  'Sprime the compact reduced strict transform, mu=beta|Sprime, '
  'rho1:T1→Sprime its finite normalization followed by minimal resolution. '
  'Sprime is a Cartier hypersurface in the smooth blown-up threefold. '
  'The original generator pulls back along mu rho1; hypersurface adjunction '
  'gives omega_Sprime=mu*omega_S tensor O((2−d)E), hence '
  'D_old=D1+(d−2)rho1*E. At the strict horizontal H this gives '
  '2=(d−2)n+a with a the P300 effective-divisor coefficient. '
  'When H is rho1-exceptional its positive genus makes a>0. '
  'No proper torus-fibre structure is imposed on Sprime. This is bounded '
  'premise/application evidence only; the P4.52 receiving subsection is '
  'not yet delivered or marked complete.'),
 ('global_divisor','night:P4R.6',
  'Read complete original/current and receiving R6. Its statement payload, '
  'global compactness and b1=b2=0 hypotheses, all conclusions, tag02YI and '
  'both labels are unchanged; only the hidden dependency record changes. '
  'Its proof applies P300 to the restriction with identical S,N,T,nu,pi,rho '
  'and D. P4.12 gives omega_S^m=O, hence '
  '(omega_T(D))^m=rho*(omega_S^m)=O. The separate proper support owner '
  'keeps the local UN7 consumer in its original domain.'),
 ('local_consumer','cdp:st:C.2.UN.7',
  'Read entire current and receiving UN7 statement and proof. Only its '
  'contracted-case support application and hidden dependency record change. '
  'P300 is applied with X=U,N=T,T=Z,nu=eta,rho=h to the same proper fibre '
  'tube; the separate P281 canonical/numerical input is unchanged and earlier '
  'than UN7. C.UI.14 and all formulas, the proper Lefschetz calculation, '
  'rational/ruled conclusions, parity, finite-character comparison, '
  'e(S)≥2/pi1(S)=1 contracted conclusion and global D1.9 exclusion remain. '
  'No whole UN7 subsection closure is claimed.')
]
events=[]
for suffix,owner,outcome in reading:
    event=dict.fromkeys(event_fields,'')
    event.update(
        statement_id=owner,date=now[:10],
        who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; inherited effort not separately exposed; continuation3 foundations',
        type='used and rechecked in this run',
        outcome=outcome+' Exposed reading and direct comparison only; no independent-check credit, required-check increment, integrated build or final page reading is claimed.',
        event_id='publish:c3:foundations:sec07:contracted:'+suffix,
        phase='publication complete contracted-boundary subsection',
        source_file=str(path.relative_to(ROOT)),
        source_event_type='used and rechecked in this run',
        evidence_group='publish:c3:foundations:sec07:contracted',
        date_utc=now,
        where='Complete contracted subsection; P300 before R6; bounded R6/UN7 applications')
    events.append(event)
with (OUT/(prefix+'_CHECK_EVENTS.tsv')).open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=event_fields,delimiter='\t',lineterminator='\n')
    w.writeheader();w.writerows(events)

status=[]
unit='subsec:II:contracted-ruled-boundaries'
fragment='agents/continuation3_foundations/sec07/S6_SERIES_PUBLISH_II_sec07_contracted.tex'
for kind in [f'D{i:02}' for i in range(1,26)]+['restructuring']:
    state='done'
    why=('Complete current and receiving subsection read for this class; every changed '
         'instance is logged, and no further source instance remains in this receiving unit.')
    if kind=='D04':
        why='Printed legacy statement/equation citations use current labels. Every permanent label and target is preserved.'
    if kind=='D10':
        why='The existing Paper II D10 closure stands: only mathematical titles/numbers/tags print, with hidden dependency records.'
    if kind=='D12':
        why=('CR2 aliases P293; CR5/MH3 share UN10 with explicit local/global domains. '
             'Earlier P252/P232/P294/P245/P4R1/P255/P300/P282/VII2 own repeated arguments. '
             'CR1 keeps its coefficient induction and CR3 its strict-leaf geometry.')
    if kind=='D13':
        why='All results are in numbered statements/proofs; no orphan paragraph remains between the six receiving owners.'
    if kind=='D14':
        state='open'
        why=('Local order is complete and P300 precedes R6/CR1/UN7 with no P281 forward input. '
             'Final whole-paper placement remains with root; relocation alone closes no row.')
    if kind=='D16':
        why='The existing Paper II D16 closure stands; all receiving owners have mathematical titles, including P300 and merged UN10.'
    if kind=='D17':
        why=('Apply exact earlier topology/duality/blowup owners. The short plane-residue/first-blowup '
             'comparison remains because the reopened vanishing theorem does not state that conductor-order formula.')
    if kind=='D18':
        why='The analytic source is van Straten1987 Section2.2.3, printed p60, reopened as image/text; bibliography identity unchanged.'
    if kind=='D19':
        why=('All converted equations use section numbering and keep old labels/targets. '
             'C.CR.5 aliases P232. C.CR.20/C.MH.15 label one equation with both full payloads and its alias hook before the formula.')
    if kind=='D20':
        why='Fibration target B0 and ruling target B match P293; every normalization/resolution/divisor map is explicit.'
    if kind=='D23':
        state='open'
        why='Full source read and equation-whitespace/statement-kind corrections done; integrated compilation and final page typography remain with root.'
    if kind=='D24':
        state='open'
        why='Root must reconcile further-results aliases CR2/CR5/MH3 and final outline/contents with the body; this package leaves front matter to root.'
    if kind=='D25':
        why=('All inference/consumer domains compared; P300 resolves the broad UN7 premise exactly, '
             'and its separately proved general first clause covers the P4.52 strict transform. '
             'Original mathematical statements stand. A reversed explanation in the temporary receiving '
             'UN10 draft was corrected and logged without refuting an original statement.')
    if kind=='restructuring':
        state='open'
        why=('Local consolidations/dependencies are complete in this actual subsection, ending before '
             'the new reduced-horizontal subsection. Root admission/final placement remain. '
             'P300/R6 and UN7 guards are bounded evidence, not extra completed units.')
    status.append(dict(unit=unit,row=kind,status=state,basis=why,fragment=fragment))
with (OUT/(prefix+'_unit_progress.tsv')).open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['unit','row','status','basis','fragment'],delimiter='\t',lineterminator='\n')
    w.writeheader();w.writerows(status)
lines=['# Contracted ruled boundaries: unit status','',
       'The full subsection and every rewritten proof have been read against the complete original/current owners. '
       'Six guards replay once and preserve all old label/target multiplicities. P300 is the only new tag. '
       'No central files are written. Root admission is pending.','',
       '| Class | Receiving status | Exact basis |','|---|---|---|']
lines.extend(f"| {r['row']} | {r['status']} | {r['basis']} |" for r in status)
(OUT/(prefix+'_status.md')).write_text('\n'.join(lines)+'\n',newline='\n')

comparison=r'''# Contracted-boundary consolidation

## Complete subsection

The receiving subsection consists of P293, UN9, CR1, CR3, merged UN10 and CR6. It ends before the actual subsection subsec:II:reduced-horizontal-boundaries; IRR1 and the later rational/ruled material remain open. Every original/current proof and every receiving proof was read. Existing P281/P289 equation alias hooks and the complete admitted UN9 proof are untouched.

| Original owner or calculation | Receiving owner and exact map | Scope and preserved conclusion |
|---|---|---|
| CR2 | P293 on identical S,T,Z,C,V,p0,q; tag01BR/label moves onto P293. | The complete old conclusion holds locally. CR3 explicitly inherits every original CR1 global hypothesis. |
| CR1 ruled-boundary topology | P252 with T=Z,T0=Z0,H=C0 and the same D, using KZ+D=h*omegaS from P281. | Exact tree, section/ruling maps and inclusion-induced group isomorphism. |
| CR1 blowup identity | P232 with Z1=W,Z2=Wprime,m=d and the same a. | C.CR.5 aliases the single Jacobian formula and its complete proof. |
| CR3 coefficient-one leaves | CR1 with the same reverse blowups. | Shifted gcd induction and full leaf induction both remain. |
| CR1 support | P300 with N=T,T=Z,nu=eta,rho=h and the same pulled-back generator. | C.CR.6, all exceptional configurations and the complement isomorphism. |
| CR1 pushout | P294 with h:Z→S,A=D_red,C=Gamma_red,j inclusion,k=h restricted to D_red. | Inclusion Gamma→S induces the group isomorphism; j* invertible, k* zero. |
| CR1 free rank and Euler | P4R.1 on mS, then P245 on rationally normalized Gamma. | The original global D1.9 class forces rank one; C.CR.1/8/9 remain. |
| CR1 reduced conductor chi | VII2 first assertion on compact S with torsion omegaS and chi(O_S)=0. | That first assertion requires no class-VII hypothesis; chi(Gamma_red)≥−1 and the original delta bound follow. |
| CR3 branch reception | P255 with eta:T→S, whole G and D_T=(pi D_red)_red. | Full E0/strict-leaf star geometry remains. C.CR.8 forces each possible multibranch point to have two branches; P255 excludes it for this star. Rational-normalization/pi1 and cusp coefficient/degree conclusions remain. |
| CR5 and MH3 | Global clause of UN10 on identical S,T,Z,C,V and chosen n,v,N0. | Genus one remains local. Euler conclusions explicitly retain compact Y, b1=b2=0 and base P1. Tags01BU/01C6 are aliases. |
| C.CR.20 and C.MH.15 | One equation: e(S)=n−v+N0=0, n=v−N0. | Both complete old payloads are present, with both labels and targets. |
| CR6 | P293 residue, P222 purity, P282 finite curve duality and branch formula. | Full ideal (x,g), adjoint-form/first-exceptional order, quadratic coordinate maps, even semigroup and covering degrees remain. |

CR3 remains a numbered graph exclusion at its original global genus-two domain. Its specific strict-leaf geometry and rational-normalization conclusion remain in its proof. The local UN10 proof uses the broader full-function UN9 and product-cusp owners. The coefficient-one-leaf fact has a single proof in CR1.

## P300 and the local consumer

The complete old R6 proof constructs D by meromorphic pullback, applies finite duality and solves Md=−b with minimality/P243. The degree is zero because each exceptional curve maps to a point. These first three steps work for every compact reduced hypersurface in a smooth threefold and prove the first clause of P300. A component of positive geometric genus has p_a≥1 and negative square, so K.E>0; the same positive inverse-matrix argument gives positive coefficients on its whole exceptional block. The full isolated-point exclusion uses the proper torus degeneration and has original f=u g^m, exact H=exp(log(u)/m)g, and identity inclusion K∩H^−1(delta)→f^−1(delta^m); A.5.17 owns its full sphere and transport proof.

P300 states and proves the general divisor/effectiveness assertion first, then imposes the proper-disc torus hypotheses for its full support/pole assertion. It is inserted immediately before R6. R6 keeps its entire original global statement and both labels, applies P300 to the identical data, and obtains torsion from its existing final P4.12 application. There is no earlier R6→P281 or UN17 dependency.

The strict-transform consumer in P4.52 uses only the general first clause. Its exact maps are the ambient point blowup beta:Xprime→X, the compact reduced strict transform Sprime, mu=beta|Sprime, and rho1:T1→Sprime consisting of finite normalization and minimal resolution. Hypersurface adjunction gives omega_Sprime=mu*omega_S tensor O((2−d)E). Comparing the pullbacks of the same original generator gives D_old=D1+(d−2)rho1*E. On the strict horizontal curve H, its unchanged old pole order is two, so 2=(d−2)n+a, where n=ord_H(rho1*E)>0 and a≥0 is the coefficient in the effective divisor D1. When H is rho1-exceptional, positive genus gives a>0 by the proved first clause. This application imposes no torus-fibre hypothesis on Sprime. The complete current P4.52 was read for this map; its complete receiving rewrite remains a separate next package, with no unit-completion credit here.

UN7 explicitly applies P300 with X=U,N=T,T=Z,nu=eta,rho=h. Its P281 canonical/numerical input is separately cited and unchanged. The complete current and receiving UN7 proofs were read. All formulas and conclusions outside the bounded application are unchanged, including e(S)≥2, pi1(S)=1 and global nonoccurrence. No whole UN7-unit completion is claimed.

## Primary analytic source

The already downloaded primary van Straten1987 thesis was reopened as rendered image and extracted text at printed p60 (PDF p63), Sections2.2.2/2.2.3. Its PDF SHA256 is 583d6e337304958cb3dfb6519cb8c82901928667ccacfeae74d0e03a19d1e906.

URL: https://download.uni-mainz.de/mathematik/Algebraische%20Geometrie/DvS-Publikationen/DvS_1987_weakly%20normal%20Surface%20Singularities%20and%20their%20improvements.pdf

The short residue/lift/first-blowup comparison stays because the cited theorem does not state this conductor-order formula. No source copy or passage is in this package.

## Guards and remaining integration

Six guards replace the complete subsection, transfer C.CR.5 into the existing P232 alias hook, remove later MH3, insert P300 and the exact global R6 application, and change the two bounded UN7 application/dependency loci. All replay once and preserve every old label/target multiplicity. R6 statement payload is unchanged; P293 and UN9 proof payloads are unchanged. Numbered equations have no blank paragraphs.

Root should consolidate the further-results lines for CR2, CR5 and MH3 into the receiving owners, retaining global D14/D24/restructuring and integrated D23 gates. P300 is now allocated and unavailable for another use.
'''
(OUT/(prefix+'_comparison.md')).write_text(comparison,newline='\n')
print(f'{len(rows)} defect rows; {len(events)} exposed-reading events; 26 actual-subsection status rows; P300 allocated.')
