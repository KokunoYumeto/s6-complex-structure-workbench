"""Transcribe this writing's actual Paper III mathematical review events.

The list is manually maintained after reading and re-deriving an argument.
Neither copying a statement nor executing an extraction script adds a check.
"""
from pathlib import Path
import csv,json
OUT=Path(__file__).resolve().parents[2]
WHO='GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro)'
DATE='2026-11-18'

proved={
'A.2.2':'The local-ball pinch inserts an arbitrary element of pi6(S3)=Z/12 while fixing the exterior. The cusp-target constraint is checked through the solid torus target and its vanishing pi6.',
'B.1.1':'Transport of the framing difference gives the common invariant mod-two covector gamma. On L=ker gamma the spin lift exists; twice its H3 obstruction is the restriction of the common invariant class dual to d, which vanishes because d lies in L. Torsion-freeness of H3(T3;Z) then kills the obstruction. The exact A1,A2 fixed spaces were recomputed.',
'B.1.2':'The regular inverse image is T3 with the compared Lie framing. The periodic flat Dirac spectrum pairs nonzero eigenvalues and has kernel dimension two; APS II Theorem4.14 gives real e=1/2. Toda Theorem4.1 and Corollaries4.2–4.3 give the stabilization injection and the class 6nu-prime.',
'B.2.1':'The explicit power map P(3,4) has degree12. Postcomposition is multiplication by12 on pi6(S3), hence kills the quotient class; composing with the Hopf map proves nullity of f. The independent normalized-section homotopy was also followed.',
'B.3.1':'The bounded correction in the period chart was retained in the differential normal frame. The explicit SU(3) comparison diag(exp(-i(a+b)),exp(ia),exp(ib)) contracts through the displayed SU(2) factors. The induced Lie spin torus has Arf invariant one and represents eta squared.',
'B.3.2':'The difference of the two real-period lifts is zero on the exterior collar and extends over the cusp. Straight-line interpolation gives the required marked homotopy; each angle-forgotten map factors through the displayed contractible cone.',
'B.3.3':'The quotient map factors through e and the cusp-core collapse. The null homotopy of the core in S3 gives the S3 wedge S2 splitting; the original map factors through the S3 summand, so no mixed term is added.',
'B.5.1':'The finite affine cap map, logarithmic translation drift, honeycomb seam maps, frozen-period comparison and positive quotient product were re-derived. Waldhausen Theorem6.1 p77 was opened and its boundary-fixed hypothesis and alternative checked. The exact cell counts were recomputed by maps_cw.py.',
'B.5.2':'Van Kampen reduces the group to x^3=x^4. Primitive finite pullback lattices, integral Smith forms, cusp collapse matrices and the swept-torus coefficient were re-derived. maps_cw.py passed. Hurewicz, relative Hurewicz and Whitehead were matched to Hatcher Theorems4.32 and4.5.',
'C.1.1':'The map q=v^N uses C(v^N)/N. Monomial bases prove the absolute map finite flat of degree N^3. The relative invariant ring gives degree N^2, while double/triple fibre lengths prove its exact nonflat locus. The marked lattice and conjugated monodromy were recomputed.',
'C.1.2':'For adjacent A2 fan triangles the primitive ray indices satisfy the displayed equal-index and divisibility relations. Applying the reverse relations across adjacent edges makes every index equal, forcing the scalar sublattice nZ3.',
'C.1.3':'Purity on the regular locus puts branch divisors over the base. Continuing the marked Kummer sublattice by A2 gives Zw plus NZd in the toric directions, incompatible with the scalar sublattice forced by smoothness over the entire fan.',
'C.1.4':'The exact matrix D=A2^2 A1 A2^2 A1^-1 produces N^2 distinct sublattices D^a M0^b L_N, detected by u+bw+ad modN. A single prescribed N-fold cusp has insufficient based sheets.',
'C.1.5':'The finite semidirect quotient and subgroup recover L_N and the prescribed meridian. The monomial normal completions have fractional representatives in a half-open unit box, giving an explicit finite free module over the smooth target ring and therefore a finite flat normal global cover.',
'D.1.1':'Euler characteristic multiplies by the cyclic degree d. Poincare duality on the simply connected cover gives b3=2+2b2-2d and b2>=d-1, excluding the proposed connected sum.',
'D.1.2':'The connected cusp-cover lattice and d-component normalization were checked. The Laurent relation matrix reduces integrally to diag(1,t-1,t-1,0), giving the displayed torsion-free cusp homology ranks.',
'D.1.3':'For every nontrivial deck character, a nontrivial scalar in the torus Koszul differential is invertible, so the regular local systems are acyclic. Only the two cusp degrees survive; the trivial character supplies degrees zero and six.',
'D.1.4':'Primitive finite degree-two pullback lattices and the alpha2 matrix were re-derived. Its maximal-minor gcd is one for d prime6. The cusp meridian sweep has coefficient d rather than a rank-only determination; the pair sequence, duality and UCT give both Z/d groups.',
'D.1.5':'Spin follows from c1 mod2; the displayed fibre class has square zero, giving the rational cup products. Pullback of the base characteristic classes gives the stated torsion restriction before its later integral refinement.',
'D.1.6':'The cusp divisor relation sum x_j=0 and adjacent intersection products were re-derived on the toric components. The ruling class generates the torsion group using the displayed curve relations and the invertibility of two modulo d.',
'D.1.7':'The full-twist marking change is a biholomorphism with its displayed integral action. A proper family over a connecting parameter path transports the differentiable type, which therefore depends only on d.',
'D.1.8':'Homology transfer sends a torsion curve to d equal lifted curve classes and hence to zero. Poincare duality identifies this transfer with pullback in degree four, proving the asserted vanishing of c2 and p1 on the cover.',
'D.1.9':'The finite-coefficient class u and every displayed triple product were re-derived. The toric support function has component restriction eta=-5H+6E1-E3, whose square is -12; the cubic pullback evaluates to zero modulo d.',
'D.1.10':'The low-dimensional path-fibration transgression over Z[1/6], coefficient reduction and Kunneth calculation give the stated H6 of K(A,2). The integral and finite-coefficient cubic evaluations determine the displayed fundamental-class image.',
'D.1.11':'Zhubr Theorem1 pp794–795 was opened. The constructed cover supplies existence and the computed quadruple supplies uniqueness. Since multiplication by4 is injective on H2 for d prime6, the vanishing Pontryagin class forces the refined p-invariant to vanish.',
'D.1.12':'The explicit canonical logarithmic data and cyclic translation of the gamma coordinate were checked. Their commutation with the marked monodromies, finite-cap freeness and cyclic cusp-component permutation give the free action and the stated quotient.',
'D.3.1':'The moving section, annular line-bundle gluing and uniform collar separation were re-derived. The node equation xy=u(zv-s), its small resolution and the unchanged finite-root caps give a proper analytic moving-zero family with the asserted singular member.',
'D.3.3':'The root canonical weights and coarse direct-image degrees were re-derived. The varying period eliminates extra generic algebraic classes; formal cohomology of the exceptional curve gives the stated structure-sheaf cohomology through the small resolution.',
'E.1.2':'The root-atlas Weierstrass coefficients, integral product comparison AZ3B^-1=diag(Z2,s+cE), unimodular Kuhn fan, proper period action and facewise extension of the section were re-derived. The resolution adds no rays and is crepant.',
'E.2.1':'The root canonical calculation gives K=Pi*L^-5. Leray with the split relative elliptic complex gives the displayed h0q; the meromorphic product comparison gives a=2. The Chern/Riemann–Roch identities and signature give the positive rank-two form. Exact external source scopes remain separately itemized in the citation log.',
}

partial={
'B.4.1':'The exact matrices and framing mechanism were re-derived; the attached Viaclovsky and Liu–Rollenske source locators require current matching before the family-wide claim is closed.',
'D.2.28':'The full table statement and short assembly proof were read. The exact classification and marked realization in D.2.22–27 remain its current dependency gate.',
'D.2.44':'The refined Pontryagin/Arf argument was read through its first major section; the complete long proof and all dependency closures are still under review.',
}

night={
'P3F.26':('review in progress','The full construction was read, including the integral H,K basis, component-supported line extension and cusp fan. The exact parabolic relation certificates remain to be recomputed.'),
'P3F.33':('proved','The free-sector condition was re-derived by separating powers divisible by3 from the finite-rotation powers. The integral affine coinvariants give pi1=Z/|n|; the sphere case uses the stated n=1 filling calculation.'),
'P3F.34':('proved','The entire integral Gysin proof was re-derived: primitive boundary kernel, exterior restriction plane fixed by all n=1 fillings, cross-product index g|n| and first Smith invariant g. The n=0 case was followed separately. This extends the properly scoped coprime S6_09 theorem; it corrects the unqualified research CSV value.'),
}

def main():
    reviews={}; events=[]
    def add(label,state,scope,kind='D'):
        reviews[label]={'state':state,'scope':scope,'date':DATE,'who':WHO}
        events.append({'label':label,'date':DATE,'who':WHO,'type':kind,'verdict':state,'scope':scope,'independence':'Source proofs and historical checks were available; this is a re-derivation, not a blind check.'})
    for sid,scope in proved.items():add('maps:src:'+sid,'proved',scope)
    for sid,scope in partial.items():add('maps:src:'+sid,'review in progress',scope,'F-partial')
    for sid,(state,scope) in night.items():add('night:'+sid,state,scope,'D' if state=='proved' else 'F-partial')
    extra=OUT/'analysis/III_additional_review_events.json'
    if extra.exists():
        for label,event in json.loads(extra.read_text()).items():
            events[:]=[x for x in events if x['label']!=label]
            add(label,event['state'],event['scope'],event.get('type','D' if event['state']=='proved' else 'F-partial'))
    # Source D.2.4 is an explicitly open research scope, not an unchecked theorem.
    add('maps:src:D.2.4','open','The source records the remaining classification problem; no resolution is claimed by this writing.','scope-record')
    rp=OUT/'analysis/III_proof_reviews.json'
    previous=json.loads(rp.read_text()) if rp.exists() else {}
    previous.update(reviews);rp.write_text(json.dumps(previous,indent=2))
    dest=OUT/'records/III_events.tsv';dest.parent.mkdir(parents=True,exist_ok=True)
    with dest.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(events[0]),delimiter='\t');w.writeheader();w.writerows(events)
    print(json.dumps({'current_full_receiving_derivations':sum(x['state']=='proved' for x in reviews.values()),'partial_or_open_records':sum(x['state']!='proved' for x in reviews.values())}))

if __name__=='__main__':main()
