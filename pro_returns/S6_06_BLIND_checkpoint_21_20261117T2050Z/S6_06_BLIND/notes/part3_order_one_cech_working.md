# Exact source Cech cochain for order-one elliptic clutches

This is a complete source-level derivation for independent audit. The gamma marking is retained throughout. The line transport is displayed as an actual line bundle and an actual evaluation map; no assertion that its residual base line or vertical divisor vanishes is made. No return invariant is assigned here.

## 1. The actual source obtained from the translation clutches

Let the rational relatively minimal elliptic source with section be f:S->P1. Choose disjoint closed discs at the finitely many marked clutch sites, slightly enlarge each to an open disc U_i, and let U_0 be the complement of smaller closed discs. Each overlap U_0 intersect U_i is an annulus containing only smooth fibres. The order-one elliptic part of the prescribed collar is an actual holomorphic translation section u_0i on that annulus. At a smooth-site disc, choose its single-valued period frame Pi(q). A marked logarithmic period lambda then gives, explicitly,

    u_0i(q) = Pi(q) lambda log(q)/(2 pi i) modulo Lambda(q).

Changing the branch of log adds the period Pi(q)lambda, so this formula is a single-valued section of the elliptic group. At a singular-site disc, use the actual annular translation section with its own descent law; the displayed linear-log formula does not assert a single-valued period frame there. For example, on a Tate annulus put s=log(q)/(2pi i), tau(q)=Ns+tau0(q), where tau0 is single-valued. For the marked elliptic integers (c,j), the exact formula is

    u(s)=(jN/2)s(s-1)+j tau0(q)s+c s,
    u(s+1)-u(s)=j tau(q)+c.

Thus it descends modulo the actual Tate lattice, including the graph period j. In the line gauge with a-period character one and tau-period character P(q), the scalar exp(j log(P(q))s) has quotient P(q)^j under s->s+1 and exactly compensates that lattice shift in the line. The integral delta choice remains an additional retained scalar factor. More general given extending annular translation sections are treated by the same gluing. The integral gamma component of the original threefold clutch is not included in u_0i and is not changed.

Glue S|U_0 and S|U_i by t_(u_0i). There are no triple overlaps in this cover. This defines a smooth complex surface S_u with a holomorphic map f_u:S_u->P1. Its inverse image over each U_i or U_0 is the original proper local elliptic model. Consequently it is Hausdorff: points with different base images are separated on P1, and points over the same image lie in one original local model. Properness is local on the target and follows directly from those local proper models. Equivalently, a compact subset of P1 admits a finite cover by smaller relatively compact base neighbourhoods whose inverse images are compact in the original local models. Thus S_u is compact. Its fibres, including their multiplicities and their local analytic models, are precisely those of S. In particular there is no multiple fibre.

## 2. Canonical and coherent identifications, with their gluing maps

On every original local model choose the invariant relative dualizing form eta and a base coordinate q. The holomorphic two-form dq wedge eta is nowhere zero on the minimal smooth elliptic surface. The original source canonical bundle is f^*O(-1); this is also the explicit source canonical form used in P3K.22. A base-dependent elliptic translation has

    t_u^*eta = eta + h dq

on the smooth locus, because the restriction to every smooth fibre is its invariant one-form. Hence

    t_u^*(dq wedge eta) = dq wedge eta.

Both sides extend holomorphically across the local minimal model, so this equality is exact. The canonical transition functions of the glued surface are therefore the original transition functions, giving the actual line-bundle isomorphism

    omega_(S_u) = f_u^* O_P1(-1).                         (OC.1)

The connected fibres give (f_u)_*O=O. The original source has R1 f_*O=O(-1). Translation acts as the identity on H1(E,O_E): under Serre duality its dual is the identity on the invariant differential. All annular transition maps on the locally free rank-one sheaf R1 f_*O are therefore exactly the identity. Applying the local proper-direct-image identifications on the displayed cover gives

    R1(f_u)_*O = O_P1(-1).                               (OC.2)

This argument uses the actual sheaf gluing; it does not replace a local system coinvariant by a sheaf obstruction. Leray now gives h1(O_Su)=h2(O_Su)=0 and chi(O_Su)=1. Equation (OC.1) gives H0(omega_Su^r)=H0(O_P1(-r))=0 for every r>0, hence kappa=-infinity.

The compact-surface classification already verified in this run, BHPV, second edition, VI.1.1 and Table 10, pp.243-244, makes S_u rational: the class-VII alternatives have chi(O)=0, and a ruled surface over a positive-genus curve has q>0. The numerical inputs above exclude both. The canonical class has square zero, so Noether's formula gives e(S_u)=12. A minimal rational surface is P2 or a Hirzebruch surface and has Euler number 3 or 4. Thus S_u contains a smooth rational (-1)-curve E.

By adjunction K_Su.E=-1. With F=f_u^*O(1), equation (OC.1) gives F.E=1. Consequently E is not vertical, and f_u|E is a degree-one holomorphic map of smooth compact curves to P1. It is an isomorphism. We have obtained an actual holomorphic section sigma of S_u.

## 3. The exact Cech cochain and source isomorphism

Write s_i for sigma in the original chart S|U_i. With the gluing convention p_0=t_(u_0i)(p_i), these local sections satisfy the exact equality

    s_0 = s_i + u_0i.

The maps

    Psi_i:S|U_i -> S|U_i,       p_i |-> p_i-s_i(f(p_i))   (OC.3)

agree on the glued overlaps: p_0-s_0=p_i+u_0i-(s_i+u_0i)=p_i-s_i. Hence they define a source isomorphism Psi:S_u->S over the identity of P1. This is the required cochain u_0i=s_0-s_i. In particular it is not obtained by identifying an unproved monodromy coinvariant with an obstruction group.

Here is an explicit extension argument at the singular fibres. A section meets the smooth multiplicity-one part of a Kodaira fibre because its fibre intersection number is one. The fibrewise addition formula on the Weierstrass model makes translation by that section a meromorphic map of the smooth minimal source. Resolve its graph over a small base disc, with proper modifications p,q:Z->S. Let Omega be the nowhere-zero two-form dq wedge eta on that local source. On the common dense open set, p^*Omega=q^*Omega. Their zero divisors have positive support exactly the exceptional curves of p and q: each point blowup adds its positive canonical exceptional discrepancy, and Omega has no zeros or poles. Thus these exceptional supports agree. Each connected fibre of p is sent to a point by q, since all its curve components are q-exceptional and adjacent components have the same image. Normal descent through p_*O_Z=O_S factors q as a holomorphic map through p. Repeating with the inverse translation proves that (OC.3) and its inverse are holomorphic on the entire local minimal model.

Every source suspension translation is t_(-Q). Since translations commute, Psi_i t_(-Q)=t_(-Q) Psi_i. On a ramified root, the pulled-back section is equivariant for the canonical root deck D; therefore Psi_i also commutes with D and with every affine source cap t_R D. The same graph/two-form extension gives the maps on the minimal root models. Thus the source gamma generator is fixed by the actual cochain, and the marked integers m,n of every retained nontrivial cap are unchanged.

## 4. Exact line transport and the residual delta data

Keep the actual line lifts in the original clutches. The elliptic-plus-delta part glues the source line bundles to a line M_u on S_u; the gamma translation factor is retained separately in the suspension. On a regular annulus a lift of t_u exists directly on the universal vector cover: the flat degree-zero line has constant period characters, and the scalar acquired when log q changes branch is cancelled by the corresponding exponential scalar. The two resulting quotient actions agree because the added elliptic period and its line character cancel. This also displays the original delta choice; it is not set to one.

Transport this actual line by Psi and denote the resulting line on S by M_tilde. On each smooth elliptic fibre, translation preserves the degree-zero Picard point. Thus Q_line=M_tilde tensor M^(-1) restricts to the trivial line on every smooth fibre. Its proper direct image L=f_*Q_line is a torsion-free rank-one coherent sheaf on the smooth base P1, hence a line bundle. The canonical evaluation map

    f^*L -> Q_line

is an isomorphism on every smooth fibre: there H0 has dimension one and evaluation is the usual trivial-line evaluation. Globally it is a nonzero morphism of line bundles, so its divisor D_vert is effective and supported on the singular fibres. We obtain the exact isomorphism

    M_tilde = M tensor f^*L tensor O_S(D_vert).             (OC.4)

The map, rather than merely its numerical class, is the evaluation map just constructed. The choice L=f_*Q_line fixes the whole-fibre ambiguity: no complete fibre can be subtracted from D_vert while preserving the evaluation lattice. On the complement of its support, choose the canonical section of O(D_vert) and local frames for L. The remaining transition functions are actual base units h_ij(q); their winding numbers record the degree of L. All vertical coefficients and all these transition units are retained.

On a minimal root with multidegree-zero root line N, the translated line admits the actual local lift obtained by the direct-image/whole-fibre calculation of P3K.15. Degree-zero translation lifts commute with the suspension lift on smooth fibres, as is seen on (C times C*)/Lambda with constant period characters; extension gives that equality on the root neighbourhood. Its commutator with the finite deck can leave a finite character chi in mu_m. The scalar norm-zero averaging formula in part3_os50_affine_conjugacy_working.md removes only the base-unit coboundary and retains chi. Therefore the cochain carries the exact root line comparisons and delta phases; it does not erase them.

## 5. Scope of the result and remaining global task

Sections 1-3 give an actual global source trivialization of every prescribed finite collection of order-one elliptic translation clutches, including clutches whose enclosed local source fibre is singular. They preserve the gamma marking and transport each nontrivial cap by an actual local source map. Section 4 gives the resulting line by an actual evaluation morphism and retains its base line, vertical divisor, and finite root characters.

To use this in the final exhaustive sphere/return classification, the transported line and its retained delta data must be inserted into the existing cap and page calculations. No equality between M_tilde and M, no disappearance of L or D_vert, and no equality of return invariants is asserted here. The exact source cochain is complete; the numerical processing of its line output remains a separate calculation.

Primary source already opened and verified earlier in this run: BHPV2004, Compact Complex Surfaces, second edition, VI.1.1/Table 10, pp.243-244, publisher preview https://page-one.springer.com/pdf/preview/10.1007/978-3-642-57739-0_7 . No new external source was opened for this note.
