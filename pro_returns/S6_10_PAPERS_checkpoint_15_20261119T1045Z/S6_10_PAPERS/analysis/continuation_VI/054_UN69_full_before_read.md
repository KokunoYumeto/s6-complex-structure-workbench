# UN69: maximum components and actual rational-edge removal, written before target

19 November 2026. The target proof of `cdp:st:C.2.UN.69`, its displayed internal equations, and its producing code have not been opened. The assertion was read in `041_UN697480_statements.json`; the allowed input statements are in `051_UN69_allowed_input_statements.json` and `052_UN69_Hopf_allowed_statements.json`. This note derives the entire assertion from those statements and the classical surface facts specified below. It does not borrow an argument from UN69's proof. Its computation and timestamp/hash receipt will be frozen before that proof is requested.

The specified actual canonical evaluation is essential. A local generator of the rank-one direct image gives a three-form eta with divisor sum k_v T_v, after the fixed disc coordinate trivializes the base canonical line. Changing the generator by a holomorphic unit leaves all k_v unchanged. This is the definition supplied separately by root from UN64/UN66, without their proofs.

## 1. Exact canonical and normal-line maps

Let D_v be the disjoint union of the smooth connected double curves on T_v. Disjointness uses the no-triple hypothesis, including at different connected components of one intersection. The full central divisor is principal and reduced, so restriction of its specified trivialization gives

    O_{T_v}(T_v) = O_{T_v}(-D_v).

Write lambda for the canonical direct-image line on the disc, and retain its evaluation isomorphism

    K_U = f*lambda tensor O_U(sum k_w T_w).

Adjunction and that same full-fibre trivialization give the actual line-bundle equality

    K_{T_v} = O_{T_v}(sum_{w != v} (k_w-k_v-1) D_vw).       (1)

The equality includes the specified meromorphic section obtained from eta by adjunction; it is not merely a numerical equality. Restricting the full fibre to a double curve D=T_v intersect T_w also identifies the normal lines as dual, since every other component avoids D. Thus their degrees add to zero.

Put Delta=k_v-k_w and d=D^2 in T_v. Adjunction on the smooth curve D, with all other boundary curves disjoint from it, gives

    Delta d = 2-2g(D).                                     (2)

In particular a rational double curve joins unequal orders. At the endpoint with larger order its square is positive, and integrality gives precisely (Delta,d)=(1,2) or (2,1). The opposite endpoint has square -d. These statements retain the actual side of the curve and the sign of the canonical drop.

The support is connected. Indeed the Stein factor of the proper family is finite over the disc and is the disc over the punctured base because the torus fibres are connected. The finite birational map to the normal disc is an isomorphism (its finite function algebra is integral over the integrally closed disc algebra and lies in the same fraction field). The proper Stein map therefore has connected fibres. This also fixes the use of connectedness of the incidence graph below.

## 2. A local maximum and the actual minimal surface map

Fix a local maximum T of k. If it has no boundary, description 1 is already true. Otherwise set n_j=1+k_T-k_j >=1 on its connected boundary curves D_j. Equation (1) is

    -K_T = sum n_j D_j.                                    (3)

The actual line identity supplies a meromorphic two-form on T with divisor exactly -sum n_j D_j. It also proves kappa(T)=-infinity: any nonzero pluricanonical section multiplied by the corresponding positive power of the effective anticanonical section would be a nonzero holomorphic function on compact connected T with a nonempty zero divisor, which is impossible.

Consider an exceptional curve E of the first kind on T. It cannot be one of the D_j: its genus is zero and square -1, whereas (2) at a maximum would give -(n_j-1)=2. If E is not a boundary curve, adjunction gives K_T E=-1; positivity of intersections of distinct effective curves gives

    1=(-K_T)E=sum n_j(D_j E).

Therefore E meets exactly one D_j, transversely once, and its coefficient is n_j=1. Formula (2) then makes this D_j elliptic. Blow down this actual (-1)-curve by pi:T -> T_0. Its single transverse elliptic boundary descends to a smooth elliptic curve D_j^0; every other boundary is unchanged and disjoint from it. The exact blowup identities are

    K_T=pi* K_{T_0}+E,
    D_j=pi*D_j^0-E,
    D_l=pi*D_l^0 for l != j.

They transform (3) to pi*(-K_{T_0})=pi*(sum n_l D_l^0), hence to the same line identity on T_0. Pullback is injective here: a trivialization away from the image point extends across that point together with its inverse, or equivalently pi_*O_T=O_{T_0}. Thus the coefficient-one elliptic boundary, every strictly weighted boundary, their smoothness, and their mutual disjointness are retained by the actual map.

Repeat these surface contractions. Each lowers b2 by one, so this yields an actual point-blowup map from T to a minimal surface, with exactly the same boundary coefficients and connected boundary curves. These maps determine the original surface; the ambient contractions used later are the specific maps provided by UN64. The classical inputs here are the Castelnuovo contraction, point-blowup canonical formulas and minimal models (Peters, Compact Complex Surfaces, printed p8). Classification (Theorem3.1, printed p10, with the rational/ruled definitions p9) says that this minimal kappa=-infinity surface is rational/ruled or class VII. In the last case UN19 applies to this original central component and says its minimal model is Hopf.

## 3. Rational and ruled minimal maxima

Suppose the minimal model is a holomorphic P1-bundle q:T_0 -> B. Intersect (3) with a fibre F. Since -K F=2,

    sum n_j deg(D_j -> B)=2.                               (4)

At least one boundary is horizontal. A vertical boundary in a P1-bundle would be a whole fibre, and would intersect that horizontal curve. Disjointness therefore excludes every vertical boundary. If some n_j>1, the positive integers in (4) force exactly one boundary, coefficient n=2 and degree one. This is a section and gives canonical drop one. If no n_j>1, every original adjacent order equals k_T, which is description1.

If the minimal model is P2, disjoint nonempty curves consist of a single curve by the positive degree intersection formula. The equality -K=3H gives n deg D=3. A strict coefficient gives n=3 and D a line, with drop two; otherwise n=1.

In either strict case the minimal model has exactly one boundary and its coefficient is greater than one. No exceptional blowdown in Section2 could have occurred on the original surface: every such step requires a coefficient-one elliptic boundary, and that boundary survives all subsequent steps. Hence the original T itself is unblown, with exactly the displayed ruled section or plane line. UN64 now supplies the actual ambient contraction and its inverse ordinary blowup, with the specified parent and normal maps.

The strict ruled section cannot have rational base. Here is a direct map proving that exclusion. If B=P1, the UN64 contraction produces a smooth threefold U', a proper f':U' -> disc, and an actual centre B in the smooth locus of the central surface P'. The map f' is a submersion along B, and its displayed exact normal sequence identifies the normal of B inside P' with K_B=O_{P1}(-2). Choose a smooth splitting of df' on a neighbourhood of the compact B and a horizontal vector field lifting a fixed short real path in the disc. Compactness gives one common short time of flow on an entire neighbourhood of B. The flow maps B to an embedded oriented sphere in an actual smooth nearby torus fibre. Its differential identifies the normal plane bundle in P' with the normal plane bundle in that nearby fibre, so the sphere has self-intersection -2.

The underlying real four-manifold of a complex two-torus has universal cover R4. Any map from the simply connected sphere lifts to R4 and is null-homotopic there, hence is null-homotopic and homologically zero in the torus. The self-intersection of a homologically zero oriented embedded surface is zero, contradicting -2. This argument uses the actual smooth submersion and its actual flow; it requires neither a deformation of an abstract ruled surface nor a change to the given neighbourhood. Therefore the ruled base in the strict case has positive genus.

## 4. Hopf minimal maxima: exact coefficients and normal orders

Hopf surfaces have b2=0 and universal cover C2 minus the origin. A rational curve cannot map nontrivially into one: its map lifts to the universal cover, and its two coordinate functions on P1 are constant. Every smooth boundary curve on a Hopf surface has genus one by adjunction, since all its numerical intersections with K and with itself vanish.

For algebraic dimension zero use the actual primary/secondary presentations of UN43. The required primary curve classification has been opened in Abasheva--Deev, arXiv2303.10764v1, Section2.2.2 printed p4 (the nonlinear surface has exactly its one axis curve) and Section2.2.6 printed p5 (a nonresonant diagonal surface has exactly its two axes). The finite primary covering is etale, so it preserves the coefficients of the pulled-back canonical divisor. No UN38 argument about an unmodified actual component is applied to a surface obtained by the classification blowdowns.

For a diagonal primary cover with contraction F(z,w)=(alpha z,beta w), write the pulled-back form as

    g(z,w) dz wedge dw / (z^a w^b),

where a or b is zero when the corresponding axis is not in the divisor. The curve classification and exact divisor of the form imply that g and 1/g are holomorphic on C2 minus the origin. Hartogs extends both, and their product remains1; thus g(0) !=0. Invariance of the form, evaluated at0 after the denominators are cleared, is

    alpha^(1-a) beta^(1-b)=1.

The no-resonance condition forces a=b=1. Indeed any nonzero pair of opposite-sign exponents would give a multiplicative resonance, while same-sign nonzero exponents cannot have product of absolute value1. Hence every boundary coefficient is one. The same conclusion descends through the specified finite primary cover.

For a nonlinear primary cover F(z,w)=(beta^r z+w^r,beta w), the only boundary is the w=0 axis. Its form is g dz wedge dw / w^n with the same extended unit g. Since det DF=beta^(r+1), invariance gives beta^(r+1-n)=1, so n=r+1 and the canonical drop is r. On the axis the normal line has multiplier beta and the tangent coordinate transforms by z -> beta^r z. On the secondary quotient the additional generator acts as z -> zeta^r z, with normal multiplier zeta. The r-th normal power is trivialized by the actual function z on the axis cover C*. Conversely a trivialization of the d-th power pulls back to a nowhere-zero holomorphic function h on C* satisfying

    h(beta^r z)=beta^d h(z).

The Laurent expansion forces a nonzero coefficient only at the integer exponent j with rj=d, since |beta|<1. Therefore a positive trivial power d must be divisible by r. For d=r the function z also satisfies the secondary relation h(zeta^r z)=zeta^r h(z). Thus the exact normal order on the actual secondary axis is r, including r=1. The equalities retain the normal quotient even when the nonlinear derivative has a tangent off-diagonal entry.

For algebraic dimension one, UN37 supplies the actual connected elliptic reduction q:H -> P1, fixed Jacobian, identity integral monodromy, and only smooth multiple fibres. Every compact boundary curve is vertical: a horizontal curve would meet a general fibre positively, impossible because b2(H)=0. Write its full marked fibre multiplicity as m_j.

We record the local multiplicity and normal map rather than replacing a multiple fibre by its reduced support. Near a smooth full fibre mC, the local equation is q=u x^m with u a holomorphic unit. Normalize the actual base change q=s^m. In its local charts choose v with v^m=u and use s=vx. The map to H is etale near C, the new central curve E covers C with degree m, and the new map to the s-disc is a submersion. After shrinking it is proper and smooth, with connected elliptic punctured fibres; smooth local triviality makes E connected as well. The deck group mu_m acts freely on E. A fixed-point-free finite automorphism of an elliptic curve is a translation (a nonidentity linear part makes z -> az+b have a fixed point), so its generator is a translation of exact order m.

The global normal coordinate s trivializes the normal of E and the deck generator acts with the primitive normal character zeta. Thus N_{C/H} pulled back to E is this trivial line, with that precise deck character. A trivialization of N^d pulls back to a nowhere-zero holomorphic function on compact connected E, hence a constant; equivariance then requires zeta^d=1. Conversely the m-th power descends trivially. This proves that the exact order of the original normal line is the full multiplicity m.

The fixed marked Jacobian gives an invariant relative one-form theta on the regular part of q. It extends as a nonvanishing relative form on each rooted smooth family just constructed. One way to retain the map is to take the rank-one direct image of the relative cotangent bundle over the smooth disc, choose a local generator, and divide it by its nonzero period over the fixed integral cycle. Cohomology and base change give a nonzero form on every elliptic fibre; its period is a holomorphic unit, and constant modulus and the fixed marking make this normalized form invariant under the deck action. Therefore the original canonical form, after dividing by theta, is the pullback of an actual meromorphic one-form alpha on P1. On a local base disc this follows directly because its coefficient is holomorphic and constant on each compact fibre off its vertical divisor; a local transversal identifies the descended coefficient. These descended coefficients patch by the ordinary base one-form transition law.

Write alpha locally as q^ell h(q)dq, with h a unit. Pullback to the rooted family is

    theta wedge m s^(m ell+m-1) h(s^m) ds.

Since the map back to H is etale, at a marked pole of canonical order n this gives exactly

    -n = m-1+m ell,
    ell = -1-(n-1)/m.                                     (5)

At an unmarked multiple fibre, the same formula with n=0 is impossible for m>1. At an unmarked simple fibre it gives ell=0. Consequently every multiple fibre is marked, alpha has no zero or other pole, and at each marked point a_j=(n_j-1)/m_j is a nonnegative integer. Taking the degree of the actual divisor of alpha on P1 gives

    sum_j (1+a_j)=2.                                      (6)

Thus either there are two marked fibres, both n_j=1, or exactly one marked fibre with n=m+1 and canonical drop m. The latter is a terminal Hopf surface with the exact normal order m already proved. These are precisely the local normal-order/drop descriptions referred to in UN50 and UN58; no hypothesis that every other component is Hopf was introduced.

In every strict Hopf case the minimal model has one boundary of coefficient greater than one. The survival argument of Section2 again excludes all original blowups. This proves description3 on the original actual component. The diagonal and two-marked-fibre alternatives have all coefficients one and give description1.

## 5. Global maximum plateaus

Sections2--4 prove the three stated descriptions at every local maximum. In either strict description the component is terminal and its sole neighbour has smaller order. If the orders are not all equal, any connected plateau at the largest order has an edge to smaller order, by connectedness of the full graph. At that endpoint the strict local classification makes the endpoint a leaf. It therefore has no edge to another vertex of its plateau, so the plateau has just that vertex. This applies to every largest-order plateau. In particular every global maximum is one of the strict-drop leaves in the statement.

## 6. A positive rational boundary forces a rational surface

Take any rational double curve and let T be its larger-order endpoint. By (2) its square d in T is positive (1 or2). This curve D is nef: intersections with distinct irreducible curves are nonnegative, and D^2>0. Adjunction gives K_T D=-2-d<0. Hence no positive pluricanonical divisor exists, since its intersection with the nef D would have to be nonnegative. This is also the elementary argument of Peters Proposition2.1 printed p8. Thus kappa(T)=-infinity.

Take the actual finite sequence of point contractions to a minimal model. Classification and UN19 give a rational/ruled surface or a Hopf surface. The Hopf option is impossible: the image of D is constant by the universal-cover argument in Section4, so D would be an exceptional curve of the point-blowup map. The exceptional subspace has negative definite intersection form, since the total transforms of the exceptional divisors give the diagonal form (-1,...,-1); in particular D^2<0.

If the minimal model is a ruled surface over a positive-genus curve, the composite map P1=D -> B is constant, by the Riemann--Hurwitz formula. If D is contracted it again has negative square. Otherwise its image is a ruling fibre F, and its square as a strict transform is F^2 minus the sum of squares of the successive point multiplicities, hence at most zero. Both possibilities contradict d>0. The remaining minimal surfaces are P2 and the Hirzebruch surfaces over P1. Thus the original T is rational, with an actual point-blowup presentation.

Its intersection form has one positive direction: for P2 it is (1); for F_e the section/fibre matrix is [[-e,1],[1,0]], of signature(1,1); each actual blowup adds an orthogonal (-1) by total pullback and the exceptional divisor. A rational surface obtained this way is projective (the blowup is the projective relative Proj of the point ideal), so the class of any nonempty effective curve is nonzero, as witnessed by its positive degree against an ample divisor. In a form of signature(1,b2-1), the orthogonal complement of a positive vector is negative definite. Thus every other boundary curve E on T, being disjoint from the positive D, has E^2<0.

Now suppose E joins T to a component Q with higher order. Equation (2) says

    (k_T-k_Q)E^2=2-2g(E).

Its left side is strictly positive; smoothness makes g(E) a nonnegative integer, so g(E)=0. Moreover E has positive square on Q, by the actual dual-normal equality. This is the exact propagation step: any strictly upward exit from the current positive-rational endpoint is again a rational edge of the same kind.

## 7. Actual leaf elimination, neighbourhoods and Euler count

Start from any rational edge at its larger-order endpoint. If that endpoint is not a local maximum, choose a neighbour of strictly higher order. Section6 proves that this is another rational edge with positive square at its new endpoint. Continue. Strict increase of the integer order on a finite graph prevents a repeated vertex, so the path terminates at a local maximum. That maximum has a lower-order rational boundary. The local classification makes it a strict terminal leaf. Its sole boundary cannot be the positive-genus section of a ruled component and cannot be elliptic on a Hopf component. It is therefore precisely an unblown plane with a line boundary and order drop two.

Apply the actual plane-line contraction supplied by UN64. It contracts the plane to a smooth point in the descended central component, is the inverse of the ordinary point blowup of the smooth threefold, keeps the same proper punctured torus family, and has the stated canonical drop. The parent boundary line has square -1 and is the exceptional curve of its induced point blowdown. All other boundary curves are disjoint from it because there are no triple points. Choose their neighbourhoods disjoint from that compact exceptional configuration. The blowdown is an isomorphism on those actual neighbourhoods. Thus exactly one connected rational double curve disappears; every other double curve, its genus and its neighbourhood map are unchanged, and no new double curve is created.

Repeat on the resulting actual family as long as a rational edge remains. The number of such connected curves drops by exactly one each time, so there are exactly r0 point contractions. UN64's exact Euler comparison gives e(S_j)=e(S_{j+1})+2 at each step; summing gives e(S)=e(S_nr)+2r0. The ordinary blowup maps, their smooth centres and their identifications off the centres are retained throughout. Reversing that recorded sequence therefore recovers the original support together with its original smooth threefold neighbourhood, not only its abstract component list.

Every removed rational edge was a terminal edge of the then-current full incidence graph. A cycle consisting of original rational edges could not lose its first edge by a terminal deletion, so no rational edge belongs to such a cycle. More strongly, a rational edge belonging to any cycle of the original full graph could not be removed by these terminal deletions while all other edges persist unless some other rational edge of that cycle were removed first; choosing the first removed cycle edge is the same contradiction. Thus no rational double edge belongs to any cycle of the actual incidence graph, exactly as asserted.

## 8. Scope of the independent computation and primary inputs

The fresh program separately checks the signs in (1)--(2), the exact blowup coefficient cancellation, the positive integer cases (4), the plane degree equation, the Hopf pole partition and normal-character orders, and the finite graph propagation/terminal-removal lemma on explicitly enumerated small marked graphs. The written arguments prove these statements in all sizes; finite tests are not substituted for those proofs. The program also checks the actual ruled intersection matrix and its positive-vector orthogonal form. It is authored from this note and the supplied statements, without any old producer or target import.

The only classical classification inputs used are the actual compact-surface classification/minimal models, the first-kind curve contraction and its ordinary blowup formulas, the elementary primary Hopf curve classification, adjunction, Hartogs extension, Riemann--Hurwitz, coherent base change for a smooth elliptic family, and smooth local triviality for a proper submersion. Exact primary openings will be recorded separately; the target-specific coefficients, line maps, unit retention, normal-cover characters, compact sphere transport, monotone graph argument and ambient reconstruction above are the independently written derivation. No blanket completion claim will be made until comparison with every current printed route is recorded.
