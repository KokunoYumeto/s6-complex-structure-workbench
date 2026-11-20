# OS45 K116/K117/K119: frozen statement-only derivations

Author: GPT-6 Astra, ChatGPT Pro mode, inherited effort; same model family. Date: 19 November 2026.

**Chronology.** I read only the three theorem statements, their status records, and the first proof header/comment at K116 before this derivation. I have not opened an argument from the supporting proofs of K116, K117 or K119. The extracted statements are in `../IV_K116_K117_K119_statements.txt`. This file records exactly what can be derived from their displayed data, and what remains to be checked.

## Literal source and ordered node cover

Write D=64(f³−g²). Direct expansion gives

`D=−48a(t²+a)²−8t³−72at−9`.

The given section G=(R,√3/2) lies on the cubic because substitution gives 3/4. Substituting a=−u/3−u⁴/9 and tc=1/(2u)−u²/3 gives f(tc)=ξ² and g(tc)=ξ³ for ξ=1/(4u²)+u/3. Thus the fibre cubic is exactly `(x−ξ)²(x+2ξ)`, not just an abstract nodal model. The displayed parametrization x=S²−2ξ, y=S(S²−3ξ) follows by direct substitution. Its node branches satisfy c²=3ξ=(4u³+3)/(4u²), hence c=v/(2u) in the ordered cover.

The actual inverse map is S=c(1+Z)/(1−Z), for Z=(S−c)/(S+c). At the actual section, R(tc)=1/(4u²)−2u/3 and xG−ξ=−u, so SG=yG/(xG−ξ)=−√3/(2u). Consequently Z(G)=(√3+v)/(√3−v), exactly the stated PG. The chosen branch order, section, and inverse coordinate are retained by these formulas.

The curve v²=4u³+3 is a smooth genus-one curve with one point at infinity. The map to the a-line has degree eight, because a has an order-eight pole at that infinity point. Its derivative in u is −(4u³+3)/9=−v²/9.

## Collision polynomial and puncture count

The discriminant of the quartic D as a polynomial in t is `331776(256a³−3)³`. The resultant of f and g in t is `(256a³−3)/4096`. At a³=3/256 the common zero is tII=−16a², R=4a. Direct differentiation there gives ft=−2 and gt=−3a. Thus both f and g have simple zeros and the fibre is type II; the total surface is smooth there because gt≠0.

The literal source pullback factors as

`256a(u)³−3 = −(4u³+3)²(16u⁶+120u³+243)/729`.

The residual cubic D/(t−tc) has discriminant

`−1024u⁴(16u⁶+120u³+243)³/6561`.

The degree-six polynomial is squarefree, nonzero at u=0, and coprime to both u³+3 and 4u³+3. Each of its six u roots has two distinct v values. Hence there are twelve ordered unselected-II points. The difference between selected and cusp values is exactly

`tc−tII=(2u³+9)(4u³+3)²/(162u)`.

Neither factor vanishes at one of these twelve points, so the selected fibre remains nodal. The ordinary cap remains ordinary because `16a³+3=51/16` at a³=3/256. The infinity-type coefficient a is nonzero there.

The proposed complete deleted set has these disjoint parts: eight finite points over a=0 (u=0 or u³=−3, with two v values), the single infinity point, three selected-II branch points v=0, twelve unselected-II points, and twenty-four ordinary-cap points derived below. Their total is 48. The exact gcd calculations establish pairwise disjointness of the finite parts. This derives a 48-point candidate set from the source conditions; the printed O45.2 list and its individually marked loop names still require comparison. A once-punctured-per-point genus-one surface has a presentation `[A,B] μ1…μ48=1` after a compatible oriented choice of handle and peripheral paths. The specific based paths in the source proof are not yet identified by this topological count.

## Ordered selected-II loop and original-height winding

Fix u0³=−3/4. The exact difference is

`a−a0=−(u−u0)²(u²+2uu0+3u0²)/9`,

while `v²=4(u−u0)(u²+uu0+u0²)`. Therefore

`a−a0=−v⁴ (u²+2uu0+3u0²)/[144(u²+uu0+u0²)²]`.

The displayed factor has value −1/(216u0²)≠0 at v=0. A sufficiently small positive v-circle consequently makes four positive a-turns. It returns to the actual rational functions u,a,tc,ξ and to v itself, so the original ordered source endpoint closes by its identity.

The selected discriminant derivative is

`Dt(tc)=2(4u³+3)³/(27u²)`.

Using the standard Tate parameter with j(Q)=Q⁻¹+744+… and j=1728 f³/(f³−g²), the leading coefficient in the **original height q=t−tc** is

`κ(q=0)=Dt(tc)/(64·1728·ξ⁶)=2u¹⁰/(4u³+3)³=2u¹⁰/v⁶`.

The numerator is a nonvanishing holomorphic unit at the selected-II point; the exact winding is −6 on one positive ordered v-circle. This calculation does not replace q by a rescaled height. PG=(√3+v)/(√3−v) is a unit near v=0 with value one; hence PG⁻¹ and PG⁸ have zero winding. The unit/normalization and zero winding of the complete remaining β factor require the actual point-line lift computation; they have not been inferred solely from the section coordinates.

## Prism equations and finite fan algorithm

For nonzero weights w0,w1,w2, write V symmetric and impose

`V(wi ei−w0 e0)=Ii ei−I0 e0`, `wi δi−w0 δ0=Ji−J0`, i=1,2.

Direct entrywise substitution proves the complete family of solutions

`Vrs=(Ir/wr) δrs+C/(wr ws)`, `δr=(Jr+E)/wr`.

The two vector equations have one redundant symmetric scalar equation, so V has one remaining degree of freedom. Equivalently, their difference annihilates the two-plane spanned by wi ei−w0 e0; symmetry makes that difference a multiple of (1/wr)(1/ws). The scalar δ system likewise leaves a single constant E. Specifying V22=a and δ2=2a−b gives exactly C=w2²a−w2I2 and E=w2(2a−b)−J2. This proves uniqueness, product order and every displayed division of the nonzero-weight target solution over the rationals.

For the vertical basis Pj=[[1,0],[j,1]], the exact data are w=(0,1,−1), I=(12j−6,0,0), J=(6−12j,−6,6). The prescribed vertical V and δ satisfy all the prism equations. Those equations leave V00 and δ0 undetermined. In particular, the crucial values 18j(j−1) and −12−18j(j−1), and the physical score −1−3j(j−1), do **not** follow from the prism system alone. They require the relative line, tangent, Chern-cap and physical inverse-clutch geometry.

For P=[[p,−r],[q,s]], p,r>0 and ps+rq=1, multiplication on the right by Q0⁻¹ sends (p,r) to (p,r−p); multiplication by Q1⁻¹ sends it to (p−r,r). The prescribed choice gives nonnegative entries and strictly decreases p+r until r=0,p=1, an actual vertical seed. Reversing the word gives the original matrix exactly. At every nonvertical target, P⁻¹e2=(r,p), so all three weights are nonzero. The fresh bounded program tests the stated full rational recurrence, integrality of all V/δ/s entries, preservation of the retained edge values, and all prism equations for coprime 1≤p,r≤15 and seven signed lower-row shifts. This is a bounded corroboration; the universal integrality and physical meaning require the full integral geometric argument.

## Twenty-four ordinary-cap collisions

At t=0, D=−3(16a³+3). Pulling this locus back gives exactly

`729(16a(u)³+3)=2187−16u³(u³+3)³`

`=−(2u³−3)(8u⁹+84u⁶+342u³+729)`.

The degree-twelve polynomial in u is squarefree and coprime to u, u³+3, 4u³+3 and the unselected-II polynomial. Every u root has two distinct v values. Thus the locus has 24 distinct ordered points. The three u roots with u³=3/2 give six selected-cap points because tc=−(2u³−3)/(6u); the other nine u roots give eighteen unselected-cap points.

At a cap collision, ξ=−a and the central cubic is `(x+a)²(x−2a)`. The moving nodal value s(a) satisfies

`ds/da=−Da/Dt=−2a`,

which is nonzero. The central Tate leading coefficient in height t−s is exactly 1/(288a²). The section's normalization has (SG/c)²=1/3; substituting SG/c=±1/√3 gives PG=−2±√3. These values are nonzero and are not roots of unity.

There is an exact local smoothing chart. With the actual moving nodal root ξ(a), put

`h=[−3(f−ξ²)x+2(g−ξ³)]/(t−s)`.

The numerator vanishes at t=s, so this is holomorphic. Its value at the cap node is 6a≠0. Choose the locally fixed square root of x+2ξ and set

`X=y−(x−ξ)√(x+2ξ)`, `Y=[y+(x−ξ)√(x+2ξ)]/h`.

Then XY=t−s exactly. Conversely t=s+XY, y=(X+hY)/2 and `2(x−ξ)√(x+2ξ)=hY−X`. The latter equation has nonzero derivative in x at the node, giving its actual local inverse. This derives the displayed smoothing chart without suppressing the higher coefficients in h.

## Geometric comparison framework and gates still requiring proof review

At an unselected-II point the source surface remains smooth, the selected nodal branch is still marked and simple, a≠0 keeps the infinity type fixed, and t=0 remains ordinary. The sections G and O stay in the smooth locus. A proper relative construction over the disc, with all actual line/fan/cap maps extending and one common contraction scalar, gives a smooth compact family. Its boundary transport is isotopic to the identity. The unresolved work at this prereading stage is to verify that this is the **same** full original construction and that the source topology and all prescribed selected fans are carried by explicit maps. The source algebra alone does not establish those identifications.

At a cap collision one can protect a nearby ordinary point t=d over a small parameter disc and compare the cap through the actual period flow `F_w=(exp(−w log P)Z,exp(w log C)V)`, whose inverse is F_−w. The stated logarithmic parameter jump is not discarded. Every source and physical integer in γref must be carried through the based integral comparison. The exact return identity is algebraic: from F1 EX F0⁻¹=C EY, taking inverses and composing with PY gives

`F0(EX⁻¹F1⁻¹ PY F0)F0⁻¹=EY⁻¹ C⁻¹ PY`.

The displayed C* physical action has the explicit path exp(θ log C), and transport around a proper smooth disc family has identity isotopy class. The outstanding application is the actual full-disc construction and its endpoint equality. Here the return identity and the physical path are derived exactly; existence and full endpoint equality of those particular comparison maps still require their complete coefficient, Cartier, period and cap calculations.

A constant-argument scalar segment carries a nonzero original scalar to a smaller common contraction scalar without introducing a logarithmic argument jump. It still requires verification that the whole original quotient and cap construction persists throughout that segment and that its endpoints retain every prescribed marking.

**No full theorem closure is claimed at this freeze.** The remaining work is the entire printed geometric chain, especially the original K10 sphere topology, every selected-fan comparison, the vertical Chern seeds and inverse-clutch sign, the full β/Cartier coefficients, and all source/physical endpoint maps.

## Executed prereading checks

The fresh exact program passed 50 named source/coordinate checks and 1001 integral fan cases comprising 7343 forward steps. These counts retain the bounded scope described above.
