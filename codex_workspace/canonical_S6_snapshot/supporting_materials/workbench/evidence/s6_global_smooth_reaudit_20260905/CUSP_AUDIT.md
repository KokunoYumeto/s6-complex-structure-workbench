# Independent audit of the toric cusp quotient

Date: 2026-09-05. Scope: the cusp construction in `candidate_geometry.tex`, with the earlier full local construction in `canonical_modular/parts/packet_03_body.tex` checked as mathematical evidence. The parent audits the global period existence and other fillings. This document proves the cusp assertions directly for the actual holomorphic matrix appearing in the manuscript. It makes no claim that a global complex structure on S6 or a counterexample to a published theorem has been established.

## Finding and exact extent

No false assertion was found among the cusp theorem's geometric conclusions: the specified action has a smooth Hausdorff quotient, the filling is proper, the full central fibre is reduced with normal crossings, its normalization is the stated degree-six del Pezzo surface, its three double curves are rational and pass through two triple points, and its canonical bundle is trivial. The punctured quotient identification has the stated sign of the cusp action.

The revised text abbreviates three details that should be restored: restrict chart polydisks to `Y_epsilon` in the proper-discontinuity proof; take the bound on C over a specified closed subdisc; and state the weak-inequality chart identity used for the compact representatives. These are exact textual repairs, not missing mathematical hypotheses. The earlier source already includes all three details. The exact boundary maps, which are only described by orbit combinatorics in the revised text, are computed below without discarding C(0).

## Input objects, markings, and domains

Keep the two marked lattices distinct:

\[
\bar\Lambda=\mathbb Z\overline{\widehat\gamma}\oplus\mathbb Z\overline{\widehat u},
\qquad \Lambda_{\rm tor}=\mathbb Z\widehat w\oplus\mathbb Z\widehat\delta.
\]

Their ordered-basis map is exactly

\[
B_0=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\quad
B_0\overline{\widehat\gamma}=-\widehat\delta,\quad
B_0\overline{\widehat u}=\widehat w,
\quad B_0^{-1}=-B_0.
\]

The toric cocharacter lattice is `N'=Z²⊕Z`, with character lattice `M'=Hom(N',Z)`. Its dense torus has characters `(x1,x2,t)`. The full cusp matrix is

\[
 C(t)=\begin{pmatrix}6\mu(t)&h(t)\\b(t)-h(t)&\mu(t)\end{pmatrix},
 \qquad Z(s)=sB_0+C(t),\qquad t=e^{2\pi i s}.
\]

Here `mu,b,h` are exactly the cusp germs supplied by the period construction, holomorphic on some disc `|t|<r`. Their global existence is outside this audit. Every local argument below uses the full displayed C and proves the conclusion for that input, without setting any entry to zero, changing B0, or assuming a polarization. Fix `r1` with `0<r1<min(r,1)` and set

\[
 R(t)=-2\pi\operatorname{Im}C(t),\qquad
 M=\max_{|t|\le r_1}\|R(t)\|<\infty.
\]

The finiteness follows from continuity on this specified compact disc. Choose `0<epsilon<r1` with `|log epsilon|>2M`. This is always possible. All subsequent actions and bounds are on `Y_epsilon={|t|<epsilon}`.

The triangulation consists of the triangles

\[
 L_v=\operatorname{conv}(v,v+e_1,v+e_2),\qquad
 U_v=\operatorname{conv}(v+e_1,v+e_2,v+e_1+e_2),
 \quad v\in\mathbb Z^2,
\]

and all their edges and vertices. This is the triangulation of the square lattice by the diagonal joining `v+e1` to `v+e2`. For a nonempty cell P, let

\[
 \widehat P=\{(ay,a):a\ge0,\ y\in P\}\subset N'_{\mathbb R}.
\]

The fan consists of these cones and `{0}`. The cells are locally finite in the height-one plane. No assertion that the whole cone family is locally finite at the origin is needed or made.

## 1. The countable toric space and its analytic separation

Every cell is bounded. Consequently a nonzero point of `hat P` has strictly positive height; a line through the origin cannot be contained in the cone. The cone is strongly convex. At positive height, membership in a cone is equivalent to membership of the height-one rescaling in its cell. Thus

\[
 \widehat P\cap\widehat Q=\widehat{P\cap Q},
\]

with the convention that an empty cell gives the zero cone. The common cell is a face of both P and Q. The support is exactly `(R²×R_{>0})∪{0}`.

For L_v the ordered matrix of ray generators has determinant

\[
 \det((v,1),(v+e_1,1),(v+e_2,1))
 =\det((v,1),(e_1,0),(e_2,0))=1.
\]

For U_v, subtract the first column from the other two to obtain determinant

\[
 \det((v+e_1,1),(e_2-e_1,0),(e_2,0))=-1.
\]

Every maximal cone therefore has an integral basis of ray generators. If `m0,m1,m2` is its dual basis, its affine chart is `Spec C[z0,z1,z2]=C³`, with `zi=chi^{mi}`. For a face, its chart is obtained by inverting the coordinates for vertices not in that face. These localizations give the transition maps; on the dense torus they are the identity, so the cocycle identities follow exactly.

For completeness, analytic Hausdorffness is not an inference from countability. Consider any two cones sigma and sigma', put tau=sigma∩sigma', and write `S_sigma=sigma^vee∩M'`. The cone separation lemma supplies an integral character m which is nonnegative on sigma, nonpositive on sigma', and zero on each precisely on tau. Given `p∈S_tau`, take an integer k large enough that `p+km` is nonnegative on all the finitely many generating rays of sigma. Such k exists: on rays of tau this already holds, and on all other rays m is positive. Then

\[
 p=(p+km)+(-km)\in S_\sigma+S_{\sigma'}.
\]

The reverse containment follows by evaluating on tau. Hence `S_tau=S_sigma+S_sigma'`. The ring map

\[
 \mathbb C[S_\sigma]\otimes\mathbb C[S_{\sigma'}]
 \longrightarrow\mathbb C[S_\tau],\qquad
 \chi^a\otimes\chi^b\longmapsto\chi^{a+b}
\]

is surjective. Its spectrum identifies the graph of the chart gluing with a closed algebraic subset of the product of the two affine charts, and therefore with a closed subset for the usual complex topology. The products of chart images form an open cover of `Y×Y`; the diagonal is closed on each of them, hence is closed. Thus Y is Hausdorff. This argument uses single pairs of cones, so the number of cones is immaterial.

The cone separation lemma used here is the pairwise statement in Cox–Little–Schenck, Proposition 3.1.3 and the immediately preceding discussion, pp. 106–108; Danilov, §5.4, p. 113, gives the same argument. Both primary texts explicitly make the separation test on two affine pieces. The extension to this countable fan is the preceding open-cover argument, not a claim that their finite-fan compactness theorems apply to Y. [Cox–Little–Schenck](https://web.ma.utexas.edu/users/ikmartin/pages/blog/toric-page/documents/Toric-Varieties_Cox-Little-Schenck.pdf), [Danilov](https://www.math.purdue.edu/~arapura/danilov.pdf).

Each chart embeds openly and has a countable basis; there are countably many charts. Their combined bases give a countable basis for Y. The chart construction makes it a smooth complex threefold. Each chart meets the common dense torus. More specifically, its intersection with `Y_epsilon` is `{|z0 z1 z2|<epsilon}`, which is star shaped under simultaneous multiplication of all three coordinates by a real number in `[0,1]`. It is connected and meets `(C*)²×{0<|t|<epsilon}`, a connected space. It follows that `Y_epsilon` is connected as well.

## 2. The function t and the components of its zero fibre

The height character evaluates to 1 on each generator `(vi,1)`. Therefore

\[
 (0,0,1)=m_0+m_1+m_2,\qquad t=z_0z_1z_2
\]

in every maximal chart. Its zero divisor is the locally finite divisor `sum_v E_v`, with coefficient 1 at every prime component. At a point with r of these coordinates zero, absorb the product of the nonzero coordinates into one zero coordinate and subtract the other coordinates' values. The resulting Jacobian is invertible, and the local formula for t is the product of exactly r coordinates, for `r=1,2,3`. This proves both reducedness and the asserted exact normal-crossing equations.

The component E_v has star fan in `N'/Z(v,1)`. The explicit quotient map

\[
 q_v:N'\to\mathbb Z^2,\qquad q_v(y,a)=y-av
\]

has kernel `Z(v,1)` and sends `(v+w,1)` to w. The ray directions in their cyclic order are

\[
 e_1,\ e_2,\ e_2-e_1,\ -e_1,\ -e_2,\ e_1-e_2.
\]

This is an exact quotient-lattice identification, not a change to the original fan. Set `a=e1`, `b=e2-e1`, `c=-e2`. Then `a+b+c=0` and `det(a,b)=1`. The coarser fan with rays a,b,c is the fan of P²; the lattice map to its usual fan is `[[1,1],[0,1]]`, which sends a,b,c respectively to `(1,0),(0,1),(-1,-1)`. The remaining three rays are `a+b=e2`, `b+c=-e1`, and `c+a=e1-e2`. They subdivide each of its three two-dimensional cones once.

In a smooth cone with coordinate functions u,v, inserting the sum of its two ray generators gives the two charts of the blowup of `(u,v)=(0,0)`: their maps are `(r,s)↦(r,rs)` and `(r,s)↦(rs,s)`. Their overlap is the usual blowup overlap, verified by these formulas. Applying this to the three distinct torus fixed points gives an explicit morphism `E_v→P²` identifying E_v with the blowup of those three points. Those points are the three coordinate points, hence are noncollinear. In particular E_v is compact, smooth and irreducible. Its canonical class is `-3H+E1+E2+E3`, and its square is `9-1-1-1=6`; its anticanonical boundary is the displayed cycle of six curves. Each is a (-1)-curve, either an exceptional curve or the strict transform of a coordinate line. This is exactly the surface denoted dP6 in the manuscript.

If ampleness is included in the definition of dP6, it can also be checked directly. The anticanonical class has positive square 6. It meets each exceptional curve and each strict transform of a line through two marked points in 1. An irreducible plane curve of degree d other than those three lines has multiplicities mi at the points satisfying `mi+mj≤d` by intersection with the corresponding connecting line. Hence `sum mi≤3d/2` and its strict transform has anticanonical intersection `3d-sum mi≥3d/2>0`. These exhaust irreducible curves. The surface Nakai criterion then gives ampleness.

## 3. The exact holomorphic action

For `lambda∈barLambda`, the lattice map

\[
 \varphi_\lambda(y,a)=(y+aB_0\lambda,a)
\]

is integral, has inverse `varphi_{-lambda}`, and sends `hat P` to `hat(P+B0 lambda)`. On characters its pullback is

\[
 \varphi_\lambda^*(m,k)=(m,k+mB_0\lambda).
\]

This proves, in each chart and on overlaps, that its holomorphic toric automorphism is

\[
 \Phi_\lambda(x,t)=(t^{B_0\lambda}x,t).
\]

Let `c_lambda(t)=exp(2 pi i C(t)lambda)`, componentwise. Its entries never vanish and are holomorphic on `|t|<r`. The action of the torus `(C*)²×{1}` on Y is holomorphic, so

\[
 T_{c_\lambda}(p)=(c_\lambda(t(p)),1)\cdot p
\]

is holomorphic on `Y_epsilon`. It has inverse `T_{c_{-lambda}}` because it preserves t. The maps `Phi_lambda` fix this fibre torus pointwise at the cocharacter level and preserve t; hence they commute with every `T_{c_mu}`. Linearity of C gives `c_lambda c_mu=c_{lambda+mu}`. Consequently

\[
 \Psi_\lambda=T_{c_\lambda}\Phi_\lambda,\qquad
 \Psi_\lambda\Psi_\mu=\Psi_{\lambda+\mu},\qquad
 \Psi_\lambda^{-1}=\Psi_{-\lambda}.
\]

The twist preserves each torus orbit, so the action on orbit labels is exactly translation `P↦P+B0 lambda`, with the original B0 sign.

## 4. Chart bounds, including central boundary points

For a triangle sigma let theta_i be its affine barycentric functions and put

\[
 U_\sigma(S,\epsilon)=\{p\in U_{\widehat\sigma}:|z_i(p)|<S\ \forall i,\ |t(p)|<\epsilon\}.
\]

For a torus point with `0<|t|<epsilon`, write `y=log|x|/log|t|`. The identity `(y,1)=sum_i theta_i(y)(vi,1)` gives exactly

\[
 \log|z_i|=\log|t|\,\theta_i(y).
\]

Thus the strict polydisk bound is equivalent to `theta_i(y)>-log S/|log|t||`. The closed unit polydisk bound is separately equivalent to `theta_i(y)≥0` for every i, that is, `y∈sigma` including its edges and vertices. These statements are different at equality.

Every torus point with `|t|<1` has y in at least one triangle, so lies in the closed unit polydisk of that triangle. For a point of a central orbit `O_hat P`, choose a triangle sigma containing P. The coordinates indexed by vertices of P are zero, and the remaining coordinates are nonzero characters of the quotient lattice `N'/(N'∩span_R hat P)`. The remaining dual coordinate inequalities are equivalent to the negative logarithm of the orbit point lying in the image cone of sigma in this quotient vector space.

Those image cones cover the quotient vector space. Indeed, lift any vector n of the quotient, take a relative interior point p0 of `P×{1}`, and consider `p0+u n` for small positive u. Its height is positive. Its height-one rescaling lies in a triangle containing P: a sufficiently small neighborhood of p0 meets no triangle not containing P, since the triangulation is locally finite and P is the unique cell whose relative interior contains p0. Its class in the quotient is `u[n]`, so the relevant quotient cone contains `[n]`. This proves the cover. It also proves the stronger fact that the chosen triangle can contain P itself, essential later when P has vertex zero.

It follows that the open sets `U_sigma(2,epsilon)` cover `Y_epsilon`. Compact subsets have finite subcovers. No global compactness of Y is being used.

## 5. Freeness, proper discontinuity, and the analytic quotient

On the dense torus, a fixed point of `Psi_lambda` would satisfy

\[
 (\log|t| B_0+R(t))\lambda=0.
\]

For nonzero lambda, the first summand has norm `|log|t|| |lambda|>2M|lambda|`, while the second has norm at most `M|lambda|`. They cannot sum to zero. On the central fibre a fixed point would imply `P+B0 lambda=P` for its orbit cell P. A bounded nonempty cell cannot be preserved by a nonzero translation: iteration would put `p+nB0 lambda` in P for all integers n. Since B0 is injective, lambda must be zero. This proves freeness everywhere.

For `0<|t|<epsilon`, retain the matrix

\[
 B_t=B_0+\frac{R(t)}{\log|t|}.
\]

We have `||B_t-B0||<1/2`, so `|B_t lambda|≥|lambda|/2`, `||B_t||≤3/2`, and B_t is invertible. The exact action in logarithmic positions is

\[
 y(\Psi_\lambda p)=y(p)+B_t\lambda.
\]

Put `eta0=log 2/|log epsilon|`. If `Psi_lambda U_sigma(2,epsilon)` meets `U_sigma'(2,epsilon)`, its intersection is open in `Y_epsilon` and has a point on the dense invariant torus. For its preimage p and image p', y(p) and y(p') belong respectively to the bounded thickenings defined by `theta_i>-eta0`. Therefore

\[
 \frac12|\lambda|\le|B_t\lambda|=|y(p')-y(p)|
 \le \sup\{|a-b|:a\in\sigma'^{(\eta_0)},\ b\in\sigma^{(\eta_0)}\}<\infty.
\]

For this fixed pair of triangles only finitely many integral lambda satisfy the inequality. Taking a finite union over the chart covers of two compact sets proves that the set of group translates meeting both compacts is finite.

Here is the quotient consequence without suppressing the topology. For p choose a compact neighborhood K. Only finitely many nonidentity lambda can satisfy `Psi_lambda K∩K≠empty`. Freeness and Hausdorffness give, for each of these finitely many lambda, disjoint neighborhoods of p and `Psi_lambda p`. Their pullback intersections with `int K` give an open V with `Psi_lambda V∩V=empty` for every nonidentity lambda. Thus the quotient map restricts to a homeomorphism on V and the inverse image of its image is a disjoint union of its translates. The quotient map is open because saturation is a union of open translates. For two different orbits, compact neighborhoods of representatives leave only finitely many possible intersecting translates; the same finite-neighborhood separation produces disjoint saturated images. Thus the quotient is Hausdorff. Its local charts descend from V and have holomorphic transition maps. It is a smooth complex threefold, and the quotient map is a holomorphic covering. Images of a countable base under the open quotient map give second countability. Connectedness follows from that of `Y_epsilon`.

## 6. Properness by a compact set of representatives

Fix `0<epsilon1<epsilon`. Let F0 be the finite set of triangles meeting the closed ball of radius sqrt(2) about zero. Finiteness follows from local finiteness of the triangulation on that compact ball. Define

\[
 K_0=\bigcup_{\sigma\in F_0}
 \{p\in U_{\widehat\sigma}:|z_i(p)|\le1\ \forall i,\ |t(p)|\le\epsilon_1\}.
\]

Each displayed set is closed in the compact unit polydisk of a C³ chart and lies in `Y_epsilon`, so K0 is compact.

For a torus point p with `0<|t|≤epsilon1`, put `u=B_t^{-1}y(p)` and choose integral lambda by rounding each coordinate of `-u`, so `|u+lambda|_infty≤1/2`. Then

\[
 |y(\Psi_\lambda p)|=|B_t(u+\lambda)|
 \le\frac32\frac{\sqrt2}{2}=\frac{3}{2\sqrt2}<\sqrt2.
\]

A triangle containing this logarithmic position belongs to F0. The weak-inequality chart identity puts the translated point in its closed unit polydisk, hence in K0.

For a central point with orbit label P, choose a vertex v of P and use `lambda=B0 v`, since `B0 lambda=B0² v=-v`. The translated orbit has cell `P-v`, containing zero as a vertex. The strengthened central chart-cover assertion gives a closed unit polydisk for a triangle containing `P-v`, hence containing zero and belonging to F0. It does not require the twist `c_lambda(0)` to have modulus 1: the quotient-cone cover applies to every point of this translated orbit, with its full logarithm.

Thus the image of K0 in the quotient is precisely `f0^{-1}({|t|≤epsilon1})`, so this inverse image is compact. For any compact subset A of the open base disc, choose such a closed subdisc containing A. The inverse image of A is closed in this compact Hausdorff inverse image, hence compact. This proves properness. Surjectivity follows from the dense torus over nonzero t and any point of a central component.

## 7. Central normalization and exact opposite-edge gluing

Each central orbit corresponds to a cell P. Its orbit under the deck group contains a cell with a vertex zero, because B0 identifies the translation lattice with all of Z². Therefore every point of W has a representative in E0. For an orbit labeled by P, the possible representative cells containing zero are exactly `P-v`, one for each vertex v of P. Distinct v give distinct cells; otherwise P would be invariant under a nonzero translation. For each such cell there is exactly one representative point, since no nonidentity translation stabilizes P. Hence a smooth point, a double point, and a triple point of W have respectively 1, 2, and 3 preimages in E0.

In particular, the restriction `nu:E0→W` is generically one-to-one and surjective. It is proper because E0 is compact and W is Hausdorff. Locally, the covering `Y_epsilon→N0` identifies W with a union of r coordinate planes (`1≤r≤3`), and the r local branches lift to the r preimages just described. Its normalization ring is explicitly

\[
 \overline{\mathbb C\{z_0,z_1,z_2\}/(\prod_{i\in I}z_i)}
 =\bigoplus_{i\in I}\mathbb C\{z_0,z_1,z_2\}/(z_i).
\]

The restriction map embeds the left source ring into the product, which is finite over it: it is generated as a module by the finitely many branch idempotents, and these are integral (`e²-e=0`). The product is normal because its factors are convergent-power-series rings and has the same total fraction ring. An element of that total fraction ring integral over the source is also integral over the product, hence belongs to the normal product. This proves the displayed normalization formula. The actual map from E0 is precisely these disjoint branch maps, so nu is the normalization, including its finite analytic structure. Its image is irreducible since E0 is irreducible. Double points exist, so W is not normal. It is an irreducible normal-crossings divisor; hence it is not a simple-normal-crossings divisor.

For the exact identifications set `C_v=E0∩E_v`, for a neighboring vertex v. A generic point on C_v has cell `{0,v}`. Its only other representative in E0 has cell `{0,-v}`, obtained by

\[
 \lambda_v=B_0v,\qquad B_0\lambda_v=-v.
\]

Thus the edge map is exactly `iota_v=Psi_{B0 v}|_{C_v}:C_v→C_{-v}`. A character `(a,0)∈M'` descends to the dense orbit of C_v exactly when `a v=0`. Use the same primitive a on C_v and C_{-v}, and let `w=chi^{(a,0)}`. Then the exact pullback formula gives

\[
 \iota_v^*w_{-v}
 =\exp(2\pi i\,aC(0)B_0v)\,w_v,
\]

since the t exponent `a B0(B0 v)=-a v` is zero. With `mu0=mu(0)`, `b0=b(0)` and the unchanged full C(0), this is:

| v | a | lambda_v | multiplier on the same character w |
|---|---|---|---|
| e1 | (0,1) | (0,-1) | `exp(-2 pi i mu0)` |
| e2 | (1,0) | (1,0) | `exp(12 pi i mu0)` |
| e1-e2 | (1,1) | (-1,-1) | `exp(-2 pi i (7 mu0+b0))` |

For example the third exponent is the sum of the entries of `-C(0)(1,1)^t`, namely `-6mu0-h0-(b0-h0)-mu0=-7mu0-b0`. The h0 terms cancel by this character calculation, not by changing h or C. These scalars are nonzero for every finite input. Each map extends over the two endpoints as an isomorphism of P¹; it is the restriction of the holomorphic ambient automorphism already proved. Reversing the map gives `iota_{-v}` and the reciprocal scalar. The character conventions in the table are essential: replacing w by w^{-1} on just one of the two curves would express the same map as a scalar times an inverse, rather than the table's scalar multiplication.

There are exactly three translation classes of unoriented edges and exactly two classes of triangles, the L_v and U_v. A translation preserves triangle type and acts transitively within each type. Each edge borders one triangle of each type. Therefore each `C_v→W` is injective, including its endpoints: no nonzero translation stabilizes its open edge, and its two endpoints belong to distinct triangle classes. Locally it is the coordinate-axis embedding in the normal-crossing chart, so its image is a smooth rational curve. The three resulting curves meet precisely at the images of the two triangle classes; all three pass through both points. The six boundary vertices of E0 alternate between these classes, giving three normalization preimages at each triple point. This proves the stated compact central-fibre description with its actual holomorphic identifications.

## 8. The canonical form

On the dense torus retain

\[
 \Omega=\frac{dx_1\wedge dx_2\wedge dt}{x_1x_2}.
\]

The coordinate basis change has determinant +1 or -1 as computed above. Hence

\[
 \frac{dz_0}{z_0}\wedge\frac{dz_1}{z_1}\wedge\frac{dz_2}{z_2}
 =\pm\frac{dx_1}{x_1}\wedge\frac{dx_2}{x_2}\wedge\frac{dt}{t},
 \qquad \Omega=\pm dz_0\wedge dz_1\wedge dz_2.
\]

It extends and has no zero on every chart. The extensions agree since they agree on the dense torus. For the exact action,

\[
 \Psi_\lambda^*(dx_i/x_i)=dx_i/x_i+
 \left((B_0\lambda)_i/t+2\pi i(C'(t)\lambda)_i\right)dt.
\]

All extra terms disappear after wedging with dt. Therefore `Psi_lambda^*Omega=Omega` on the dense torus and, by holomorphic continuation, on `Y_epsilon`. The covering charts descend Omega to a nowhere vanishing three-form on N0. Thus `omega_{N0}=O_{N0}` intrinsically, before any global gluing.

## 9. Punctured overlap and the cusp sign

The cusp inputs give `s(g0 z)=s(z)-1`, `t_c=e^{2 pi i s}`, and the marked periods `[Z(s)|I2]`. The chosen cusp cover U0 has deck group `<g0>≅Z`; a connected cover of a punctured disc with infinite deck group must have trivial subgroup of `pi1≅Z`, so it is universal. The map s is an isomorphism of universal logarithmic covers, with the prescribed clockwise deck generator `s↦s-1`. This uses the chosen base coordinate and does not reverse the generator.

Write a lattice element as `(a,b)∈Z²⊕Z²`, with a in the gamma-hat/u-hat part and b in the w-hat/delta-hat part. The cusp monodromy is exactly

\[
 M_0=\begin{pmatrix}I_2&0\\B_0&I_2\end{pmatrix},\qquad
 M_{g_0}=M_0^{-1}=\begin{pmatrix}I_2&0\\-B_0&I_2\end{pmatrix}.
\]

Since `Z(s-1)=Z(s)-B0`, we have `Pi(g0 z)=Pi(z)M_{g0}` and the complex linear lift `R_g0=I2`. Thus

\[
 \widetilde g_0(z,\zeta)=(g_0z,\zeta),\quad
 T_\lambda(z,\zeta)=(z,\zeta+\Pi(z)\lambda),\quad
 \widetilde g_0T_\lambda=T_{M_0\lambda}\widetilde g_0.
\]

For `G0=Lambda semidirect_{M0} Z`, let `H=Lambda_tor×<g0 tilde>`. Its normality follows from

\[
 T_\lambda\widetilde g_0T_\lambda^{-1}
 =T_{(I-M_0)\lambda}\widetilde g_0\in H,
\]

because `(I-M0)Lambda=Lambda_tor`, and the short lattice is fixed by M0. The map

\[
 \mathcal E(z,\zeta)=(e^{2\pi i\zeta_1},e^{2\pi i\zeta_2},e^{2\pi is(z)})
\]

is a holomorphic covering with deck group exactly H: equality of its images means that s differs by an integer and zeta by an integral vector, and uniqueness on the universal s-cover supplies exactly one such element of H. Its quotient is `(C*)²×D0*`.

The quotient homomorphism `G0→barLambda`, `(T_lambda g0^n)↦bar lambda`, is well defined because M0 induces the identity on barLambda. Its kernel is H. For the residual translation,

\[
 \mathcal E T_\lambda
 =\left(\exp(2\pi i C(t)\bar\lambda)t^{B_0\bar\lambda}x,t\right)
 =\Psi_{\bar\lambda}\mathcal E.
\]

Consequently the induced double quotient is exactly

\[
 (U_0\times\mathbb C^2)/G_0
 \xrightarrow{\sim}((\mathbb C^*)^2\times D_0^*)/\bar\Lambda
 =N_0\setminus W.
\]

All maps in the construction are holomorphic coverings with local holomorphic inverses, so the induced bijection and inverse are holomorphic. On a fibre its covering kernel is `Z²+Z(s)Z²`. Real independence can be proved locally without importing the global inequality D<0, since

\[
 \operatorname{Im}Z(s)=-\frac{\log|t|}{2\pi}B_t
\]

is invertible. The real map `(a,b)↦Z(s)a+b` is then an isomorphism R⁴→C²: its imaginary part determines a uniquely and its real part determines b. Therefore the kernel is a full rank-four lattice and the quotient is a compact complex two-torus. This proves the strongest local statement available from the actual cusp input; it does not supply the separately required global period solution.

## 10. Exact corrections and locators

All paths in this paragraph are relative to `output/s6_consolidated_canonical_2026-08-26/supporting_materials/`.

| Item | Revised-source locator | Exact issue | Completed repair / earlier evidence |
|---|---|---|---|
| C bound | `workbench/research/candidate_geometry.tex:777` | Holomorphic at zero gives a bound on a smaller closed disc, not automatically a bound on the whole stated open disc. | Use the fixed r1 and M above. `manuscript_sources/canonical_modular/parts/packet_03_body.tex:77` takes its norm on `|t|≤r/2`. |
| Chart domains | `candidate_geometry.tex:801` | The symbol `U_sigma(2)` was defined on all Y, whereas Psi is only defined on `Y_epsilon`. | Use `U_sigma(2,epsilon)=U_sigma(2)∩Y_epsilon` in every translated-chart expression. Earlier source lines 252–269 uses this restricted notation. |
| Closed polydisks | `candidate_geometry.tex:840` | Formula (2.5c) is strict and cannot literally be invoked with S=1 for points on triangle edges. | Add `p∈closed U_sigma(1) iff y(p)∈sigma`; earlier source lines 185 and 189 state and prove it. |
| Connected restriction | `candidate_geometry.tex:741`, theorem line 708 | Connected Y alone would not imply connected `Y_epsilon`. | The star-shaped chart intersections and common connected punctured torus above prove it. Earlier source line 276 contains this argument. |
| Edge maps | `candidate_geometry.tex:865` | The phrase opposite edges records the pairs but does not print their full maps. | Use `iota_v=Psi_{B0 v}` and the character table above; earlier source line 328 gives the exact ambient restriction. |
| Infinite fan | `candidate_geometry.tex:738` | A pairwise separation proof is referenced but abbreviated. | Section 1 above completes it and checks the actual primary proof. This is valid and is not a false assertion. |

For a concrete demonstration of the strict/closed difference, in the original chart `sigma=conv(0,e1,e2)` take `0<t<epsilon` real and `(x1,x2)=(t,1)`. Then `y=e1∈sigma`, and the exact chart coordinates are `(z0,z1,z2)=(1,t,1)`. The point belongs to the closed unit polydisk and not the open unit polydisk. This disproves the incorrect strict inference, while proving that the weak-inequality repair retains the compact-representative argument.

The original source's more detailed local proof has therefore been used to close omissions, not accepted because of an audit verdict or a Verified label. No correction changes the cusp fan, periods, lattice, action, scheme fibre, or conclusion. No statement about the finite fillings, global compactification, global topology, or a theorem-level CDP conclusion is certified by this bounded audit.

## Provenance and outputs

`USER_INPUTS.md` preserves the delegated-session user message verbatim. `LOGBOOK.md` preserves the assignment and progress. `SOURCE_HASHES.json` records the exact local sources used. `STAGED_CORRECTIONS.tex` contains copy-ready replacement passages without editing the canonical file. The original manuscript source's relevant locations are §§4.1–4.7, printed pages 24–30, with §4.4 for chart control, Theorem 4.5 for the action and properness, and Proposition 4.6 for the central normalization. The primary references inspected were Cox–Little–Schenck pp. 106–108 (PDF indices 127–129) and Danilov §5.4, printed p. 113 (PDF index 17). No external messages, publication, canonical edits, builds, Lean runs, or heavy calculations were performed.
