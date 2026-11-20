#!/usr/bin/env python3
"""Row-level bounded literature outcomes from the actual opened-source audit."""
from pathlib import Path
import json
root=Path(__file__).resolve().parents[1]
shared=('Opened-source and search scopes are recorded in audit_paper_i/sources_and_searches.md and '
        'AUDIT_PAPER_I.md, section 5. AC26 authoritative original PDF Remark3.12 p19; E26 Definition2.3 p5, '
        'Remark8.1/Conjecture8.2 p22 and Remark8.4 pp23–24; attached DGKX v1/v2; Viaclovsky '
        'Theorem1.1 p1 and Proposition2.3 pp5–6. Specific proper-filling/corner, maximal-domain and norm '
        'primary-source searches are logged there. Negative outcomes are limited to those opened scopes and queries.')
rows={}
def put(label,credit,transport,disposition,searches=shared):
    rows[label]={'credited_to':credit,'credit_transport':transport,
                 'source_credit_verdict':'bounded primary-source comparison complete at the stated opened scopes',
                 'literature_disposition':disposition,'literature_searches':searches}
put('I:weierstrass-comparison',
    'AC26 original Remark3.12 p19 supplies the original pointed cubic; E26 supplies its elliptic-surface presentation. The receiving coordinate comparison is verified explicitly.',
    'From original y0^2=4x0^3−3C x0−D to arithmetic: (x,y)=(−x0,y0/(2i)), inverse (−x,2iy). From arithmetic to geometric: (X,Y)=(2x,−2sqrt(2)y), inverse (X/2,−Y/(2sqrt(2))). Marked points, invariant differentials and discriminants are transported; Delta_geo=64 Delta_ar.',
    'Known source cubics cited; exact normalization map retained with its inverse. No model distinction asserted without this isomorphism.')
put('I:monodromy-fundamental-set',
    'The monodromy construction is inherited from AC26/E26; E26 Remark8.4 pp23–24 is the opened proper-domain antecedent. The actual lifted fundamental representatives are the receiving calculation.',
    'g(B,x,t)g(C,y,u)=g(BC,x+By,t+u−6x^tJBy); the kernel character is t+6(x1+x2+x1x2)−alpha(B) mod12. Modular reduction uses g(A,0,alpha(A)), followed by the actual Heisenberg and central translations; paired faces and elliptic stabilizers remain.',
    'No identical full fundamental-set statement was located in the bounded opened-source comparison. The exact character/lift calculation supplies the stated additional form; no universal absence claim.')
put('night:P2.1',
    'AC26/E26 supply the marked periods and logarithmic-transform construction. The complete two-axis descent is the receiving specialization.',
    'Retain N=12, gamma=(6mu,C−s−12v), u=(s+h,mu), w=(1,0),delta=(0,1). The positive source and parameter deck matrices and H=−(4l1 logt+3l2 log(t−1))/(2pi i) are evaluated on those same columns; cusp coefficient a=4l1+3l2−12l0.',
    'Known period construction credited; the precise two-axis deck comparison is retained. No matching complete corner statement was found in the checked scopes.')
put('night:P2.2',
    'AC26/E26 are construction inputs. The receiving exact origin comparison corrects the corner sign in the supplied earlier formulation, through its explicit polynomial identity.',
    'Subtract the two actual origins, with a=b−12l0=−p. Their differences are am gamma−6am^2 delta and an gamma−6an(n−1)delta; the radial class is −pn gamma modulo delta. No origin or line coefficient is identified only by notation.',
    'Full chart/origin result retained; the negative source-comparison outcome is bounded to opened AC26, E26, both DGKX versions and logged further searches.')
put('night:P2.3',
    'The source torus and finite logarithmic actions are inherited from AC26/E26. E26 Conjecture8.2 p22 is an opened proposed limit, not a proved filling antecedent.',
    'The actual rank-one charts Xi=W/r^i,Yi=r^(i+1)/W have XiYi=r and inverse unit overlaps. The affine finite actions rotate the components of the specified cover y^12=t^(4l1)(t−1)^(3l2).',
    'Retain the precise partial filling and cover calculation; do not credit E26 with its completed proper two-axis extension.')
put('night:P2.4',
    'AC26 Theorem9.1(iii),p64 and Proposition9.11,pp70–71 give the canonical input. Bierstone–Milman resolution and Grauert coherence/base change are the opened analytic inputs.',
    'The actual identity K_X^−2=f^*O(1) gives a rank-two anticanonical direct image. Its resolved pencil and three labelled critical sections recover the original base by their meromorphic cross-ratio.',
    'Known analytic results are applied through the specified pencil and cross-ratio map; this is not attributed to a source as a blanket extension theorem.')
put('night:P2.5',
    'The original monodromy matrices are inherited construction data. The displayed annihilator calculation is the receiving exact lattice application.',
    'On Lambda/Z delta, the rows u,6g+w,−w have determinant6 and common rational kernel zero; the integral quotient is free.',
    'Exact annihilator calculation retained and independently recomputed; no additional source theorem is asserted.')
put('night:P2.6',
    'Grauert/Stein factorization and the original source monodromy supply the stated known inputs, at the opened hypotheses in the source log.',
    'The source/parameter cross-cocycles vanish in the actual free quotient Lambda/Z delta. The horizontal-divisor normal meridian has a finite orbit under a finite-index base subgroup; the exact P2.5 kernel then kills its lattice class.',
    'Retain the full normal-meridian comparison; source theorem hypotheses and quotient map are explicit.')
put('night:P2.7',
    'AC26/E26 provide the family; E26 Conjecture8.2,p22 is the specific proposed limit compared. Bierstone–Milman and Grauert/Stein statements provide resolution, principalization and connected-fibre inputs.',
    'The actual origins yield commuting lifts Qo=T_(−mb gamma)Q and Ro=R. Their commutator gives (m alpha_i+n beta_i)kappa_j=(m alpha_j+n beta_j)kappa_i. The connected corner carries ratio0 from a horizontal component to ratioa at the strict cusp, while gcd(a,12)=1.',
    'The full proper Hausdorff analytic-filling obstruction is retained with arbitrary central singularities/components/multiplicities and finite covers. No identical theorem was located in the bounded four-core-source and further primary searches.')
put('night:P2.8',
    'An explicit admissible-twist specialization of P2.1–P2.7; their source and analytic credits apply.',
    'Substitute (l0,l1,l2)=(0,2,−1), giving p=−5,a=b=5 and y^12=t^8/(t−1)^3. The two origin differences are exactly five times the universal vector, with rotations8,−3,−5 mod12.',
    'Application/example of the proved receiving corner theorem; not assigned a separate broad novelty claim.')
put('night:P2.9',
    'Viaclovsky Theorem1.1,p1 and Proposition2.3,pp5–6 supply the higher (3k,4l) family and free finite root construction. The original determinant and analytic inputs are separately credited.',
    'Use N=12kl and d=4l+3k−kl !=0 in K_X^−N=f^*O(d); choose its positive-degree power and recover the rational-normal-curve base by three labelled critical points. The full origins retain N, and the congruences a=m2*l1 modm1, a=m1*l2 modm2 give gcd(a,N)=1.',
    'Known higher construction cited; the complete corner obstruction in that construction is retained. Bounded comparisons found no identical higher proper-filling assertion; determinant inputs keep their actual proof-review scope.')
put('night:P2.10',
    'E26 Conjecture8.2,p22 and its following logarithmic-transform paragraph are the exact opened comparison. They remain conjectural in the source comparison.',
    'The receiving untwisted model sets the logarithmic translations to zero and retains both actual neck line bundles and their prescribed plumbing maps, modification and finite quotient. No equality with a different one-component cap is inferred.',
    'Keep the full explicit untwisted plumbing and its scope; the original-family obstruction is not transferred after deleting its twists.')
put('night:P2.11',
    'E26 Conjecture8.2,p22 is the precisely identified proposed one-component central geometry. The receiving assertion is its virtual-Euler obstruction.',
    'Apply normalization and the double-locus smoothing identity to the stated one-component proposal: its virtual Euler contribution is0, whereas the prescribed smooth six-sphere has Euler2.',
    'A bounded, source-specific obstruction to that stated proposal is retained; E26 is not described as proving the conjectured smoothing.')

dg_transport=('For fixed standard ordered data, delta=beta_part−beta0 is constant, a=c+delta, '
              'c=a−delta, Omega_(c+delta)=Pi_c, M_part=M0+Im(delta), and a′−a=c′−c. '
              'The identity in the ordered lattice carries the finite twists and untranslated '
              'unit-square fan. Root bundles are identified by the identical root charts and '
              'vertical fields; V_here=E_DGKX, E_here=h^*E_DGKX. This standard-data map does not '
              'by itself extend a source theorem to arbitrary different affine twists.')
for n,credit,extra in [
 (1,'DGKX v1 Section6, p2:prop:vertical-log-bundle and p2:lem:log-tangent-sequence; the tangent computation culminating in Theorem6.12,pp81–82.',
  'The ordinary quotient is realized by the actual kernel/image of df at q=xy and q=xyz, with J=I_D⊗O(S1+S2).'),
 (2,'AC26 Lemma9.12 and Proposition9.13,pp72–76; DGKX v1 p2:prop:structure-direct-images and p2:prop:vertical-log-bundle, Section6.',
  'The coarse tables are obtained by the explicitly retained root-character invariants and projection formula; all ordinary cusp scheme structures are retained.'),
 (3,'DGKX v1 Theorem6.12,pp81–82 gives (h0,h1,h2,h3)(T_X)=(1,1,1,0).',
  'The standard-data tangent tuple is a credited re-derivation in the permitted Paper I appendix.'),
 (4,'DGKX v1 Proposition6.16,p85 gives the reduced smooth Kuranishi germ and miniversal parameter family.',
  'The actual parameter map has invertible derivative, so its induced analytic germ is the same miniversal germ; no fine-moduli claim is made.'),
 (5,'DGKX v1 Theorem7.14,p95 gives the full automorphism group C* for the standard data (also Theorem1.4,p3).',
  'The literal physical action is [z]∈C/Z ↦ exp(2pi i z) on the original line; the receiving proof separately retains the all-admissible-twist lattice/root-character argument.'),
 (6,'DGKX v1 Theorem1.4,p3 gives the exact 2Z equivalence for the standard data; v2 omits it.',
  'Our exact-equivalence proof was in the public working edition by8September2026; v1 is dated23September2026. The receiving general fixed-twist proof retains the whole torsor class −p and its change −bp delta2, with p odd.')
]:
    put('night:P5.'+str(n),credit,dg_transport+' '+extra,
        'Known standard-data conclusion/inputs explicitly credited and re-derived under the permitted Paper I appendix exception. The printed fixed-admissible-twist extension retains its own full equations; no broader source scope is inferred.',
        'Attached DGKX v1 and v2 opened. Exact version-specific theorem scopes and affine parameter transport are in audit_corrections/P5_7_insertion.tex. Current additional opening: v1 source lines8890–9055,9140–9188,9438–9495,10018–10120, retaining stable labels; exact page locators for Theorem6.12,Proposition6.16,Theorem7.14 and Theorem1.4 are those recorded from the attached edition.')
assert len(rows)==19
(root/'I_literature_inventory_updates.json').write_text(json.dumps(rows,indent=2)+'\n')
print(json.dumps({'rows':len(rows),'labels':list(rows)},indent=2))
