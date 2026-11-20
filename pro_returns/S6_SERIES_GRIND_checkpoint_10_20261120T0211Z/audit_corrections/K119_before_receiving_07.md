# K119: isolated-statement derivation before receiving its proof

## Exposure boundary and inputs

This note is written before opening K119's supporting proof or the receiving K119 calculations. The target read is `audit_paper_i/iv_os45/K119_statement_only_07.tex`, SHA `ffe30a241c6de33526897cdac6b9abfd187f7afdf1e1ea0059eb4e6493cab9b5`. Its complete statement includes the proposed endpoint identity and named comparison maps; that exposure is retained.

The permitted pre-existing inputs used are K116's literal source, fixed-C* continuation, source/Tate/Cartier/infinity maps and compactness argument; K78's full extending-period/groupoid/Cauchy/end-point method; and the previously read rank-two construction and F35 fan maps. I read K116 input ranges O45.1–2, O45.4–6 and O45P.4–7, as copied in `K119_input_K116_07.tex`, and K78 OCS.1–5. I did not read K119's OC45/ORC proof. The five source matrices were separately supplied as input only in `K119_permitted_K10_matrix_inputs_07.json`; homology is the inverse transpose of those actual cohomology matrices.

Prior layout exposure is recorded in my actual build12, build13/14 and build18 QA receipts. The inspected pages extend respectively through1178,1180 and1166; the receipts identify their later samples as K109–114 and endpoint-format pages. No substantive K119 proof reading is recorded. I do not describe this as an unqualified absence of every incidental earlier visual exposure.

The fresh program `code/K119_statement_exact_07.py` has passed139 exact assertions, including all source constants below and the full integral period complex. The first attempt used structural symbolic equality for the collision pullback; that comparison failed even though its expanded difference is zero. The failed source/stdout are retained. The corrected run is completed before receiving K119.

## 1. All twenty-four points and actual local parameters

For (R=t^2+a), (f=R^2+t), (g=R^3+3tR/2+3/8), direct expansion gives

\[
D=64(g^2-f^3)=48a(t^2+a)^2+8t^3+72at+9.
\]

At the original cap (t=0), its value is (3(16a^3+3)). These are three distinct nonzero a-values. At each one,

\[
D_t(0,a_*)=72a_*\ne0,\qquad
D_a(0,a_*)=144a_*^2,
\]

so the actual discriminant root (s=t_n(a)) has (s'(a_*)=-2a_*). It is an honest local coordinate. One explicit specification retaining every coefficient is the contour formula

\[
s(a)=\frac1{2\pi i}\int_{|t|=\epsilon}
t\,\frac{D_t(t,a)}{D(t,a)}\,dt,
\]

where the fixed small circle encloses just this root. The inverse is the analogous root formula for (D(s,a)) on a small circle around (a_*). Thus no discriminant root is replaced by an unspecified local parameter.

Substituting (a=-u/3-u^4/9) gives

\[
729(16a^3+3)=2187-16u^3(u^3+3)^3
=-(2u^3-3)(8u^9+84u^6+342u^3+729).
\]

The degree-twelve polynomial is square-free, and its gcd with each of (u), (u^3+3), (4u^3+3), and (16u^6+120u^3+243) is one. These exact gcds are in the new output. Each u-root therefore has two distinct v-lifts. Also

\[
t_c=\frac{3-2u^3}{6u},\qquad
\frac{da}{du}=-\frac{4u^3+3}{9}\ne0
\]

at every collision. The three roots of (u^3=3/2) yield six ordered selected-cap points. The other nine u-roots yield eighteen unselected-cap points. The other source boundaries are disjoint, including (a=0), (256a^3=3), (u=0), the branch locus (v=0) and the point at infinity. Positive local complex meridians in u, a and s have degree+1 under these actual local inverses. The two v-sheets are treated with their own markings; no unproved same-fan identification between them is used.

## 2. Full source chart, point coordinate and constants

Choose the holomorphic branch (\xi(t,a)^2=f(t,a)) with (\xi(0,a_*)=-a_*). Define

\[
h_n(t,a)=\frac{2(g(t,a)-\xi(t,a)^3)}{t-s(a)}.
\]

Its singularity is removable and its central value is (6a_*\ne0). With the specified square-root branch, the full coordinate change is

\[
X=y-(x-\xi)\sqrt{x+2\xi},\qquad
Y=\frac{y+(x-\xi)\sqrt{x+2\xi}}{h_n},\qquad XY=t-s.
\]

The inverse first sets (t=s+XY) and (y=(X+h_nY)/2). For (w=(h_nY-X)/2), write (x=\xi+z). The inverse of (z\sqrt{3\xi+z}=w) has the convergent Lagrange series

\[
z=\sum_{n\ge1}
\frac{(-1)^{n-1}(n/2)_{n-1}}
{n!\,(3\xi)^{(3n-2)/2}}w^n.
\]

This gives the entire source inverse, with the initial square root fixed. In particular its first derivative is (1/\sqrt{3\xi}\), and every higher coefficient is specified.

At the central node the cubic is

\[
y^2=(x+a_*)^2(x-2a_*).
\]

Using (S=y/(x+a_*)), its node branches are (S=\pm\sqrt{-3a_*}). At G, (S_G=\sqrt3/(4a_*)) and (S_G^2=-a_*). The normalized multiplicative coordinate ((S-c)/(S+c)) therefore gives (P_*=-2+\sqrt3) or its reciprocal (-2-\sqrt3), according to the actual ordered branch. The complete Tate parameter is the inverse of the original j-function, with its fixed small-parameter branch. Since (j=1728f^3/(f^3-g^2)), its leading factor is

\[
Q=(t-s)\kappa,
\qquad \kappa(0,0)=\frac1{288a_*^2}.
\]

This is checked from the full discriminant derivative using (16a_*^3+3=0).

The source's actual tangent slope at G is (-\sqrt3 t), and (x(2G)=t^2-2a). Hence its original tangent quotient is

\[
f_2(p)=\frac{y-\sqrt3/2+\sqrt3t(x-R)}{x-t^2+2a}.
\]

Its value at the central node is (c_2=-\sqrt3/(2a_*)). Put (F_b(Z)=\Theta_Q(Z/b)/\Theta_Q(Z)). On the same fibre, the entire divisor identity for the chronological f8 gives

\[
f_8=A_8\frac{F_P^8}{F_{P^8}},
\]

with a base coefficient (A_8); this coefficient cancels at the two actual source points p and p−G. Therefore, without removing any theta factor,

\[
B_{8,1}(p)\frac{F_{P^8}(P^{-1}Z)}{F_{P^8}(Z)}
=\left(f_2(p)\frac{F_P(P^{-1}Z)}{F_P(Z)}\right)^8.
\]

The central theta product is (1-Z). Taking the limit on the node branch (Z=0), the theta ratio is one, so the last expression is (c_2^8=9/a_*^2). Thus the original fixed normalization gives

\[
\beta(0,0)=C_*\frac9{a_*^2}.
\]

The full function is the displayed point-independent theta/Miller expression, evaluated at a protected regular section. Its reciprocal is the reciprocal of that same expression. This preserves the fixed C*, all higher coefficients, and both point/O Cartier modules. An independently varying linearization has not been substituted for this defined continuation.

## 3. Actual extending period sheaf and an integral inverse

Use the supplied five (H_i=T_i^{-t}) in their original order and let (P_i=H_1\cdots H_{i-1}). At each unselected I1 and at I8 the extending periods are the actual invariant stalk (\ker(H_i-I)), of rank3. This follows from the full rank-one source/point-line chart: one radial logarithmic period is excluded and the remaining three extend. At the selected cusp the two independent radial periods are excluded, leaving the two angular periods; this is the rank2 invariant stalk. K116's actual infinity word map and selected toric charts identify these stalks with the supplied matrix marking.

Let (E_i) be the integer Hermite basis of the actual image ((H_i-I)\Lambda), retaining its possible index in its saturation. The based parabolic complex is

\[
\Lambda\xrightarrow{D_0}\bigoplus_i\operatorname{im}(H_i-I)
\xrightarrow{D_1}\Lambda,
\qquad D_1(z_i)=\sum_iP_i z_i.
\]

The first arrow has i-th component ((H_i-I)x), in the E_i coordinates. It computes the invariant extension integrally: a punctured-sphere cocycle restricts to zero in every local coinvariant precisely when its local entries are in these actual images. The based product relation is the second arrow. This is the integral cancellation of the circle complexes, with no saturation or complex averaging.

The new calculation gives these literal matrices:

\[
D_0=\begin{pmatrix}
-3&-8&0&0\\0&-1&0&0\\-2&-3&1&0\\
-1&0&1&0\\0&-3&-1&0\\1&0&0&0
\end{pmatrix},
\qquad
D_1=\begin{pmatrix}
0&0&0&0&0&0\\0&0&1&-2&-1&0\\
1&1&-6&9&3&0\\3&0&-8&8&0&1
\end{pmatrix}.
\]

Their product is zero. The full Smith changes show

\[
H^0(\mathcal H)=\mathbb Z\delta,
\qquad H^1(\mathcal H)=0,
\qquad H^2(\mathcal H)=\mathbb Z\psi,
\]

where (psi=(1,0,0,0)) is primitive. In particular the middle vanishing is integral, including torsion.

Here is an explicit inverse for every zero-norm integral discrepancy (ell=x_u u+x_w w+x_\delta\delta). In the original lattice set

\[
\begin{aligned}
r_1&=(24x_w-9x_\delta)\gamma+(-8x_w+3x_\delta)u,\\
r_2&=-3x_u u,\\
r_3&=(-x_u-6x_w+2x_\delta)\gamma
       +(x_u+6x_w-2x_\delta)u,\\
r_4&=(x_u+3x_w-x_\delta)\gamma,\qquad r_5=0.
\end{aligned}
\]

Exact multiplication verifies

\[
\sum_{i=1}^5P_i(H_i-I)r_i=\ell.
\]

The formula uses the actual unsaturated monodromy images. Its selected-site component is zero. For a changed based cut system, the actual Hurwitz change on adjacent cocycles is also explicit. For (H'=H_iH_{i+1}H_i^{-1}), it sends

\[
(z_i,z_{i+1})\longmapsto
((I-H')z_i+H_i z_{i+1},z_i),
\]

with inverse (z_i=z'_{i+1}), (z_{i+1}=H_i^{-1}(z'_i-(I-H')z'_{i+1})). On actual-image preimages it sends ((r_i,r_{i+1})) to ((H_i r_{i+1}-(H_i-I)r_i,r_i)). These are integral reciprocal maps, so the formula transports along every prescribed original marked path. It applies to the actual local angular cycle after that marked transport, without replacing it by an unspecified primitive vector.

## 4. Full Lie and Cartier maps for moving the cap

The sheaf of extending translations has the actual exponential sequence

\[
0\longrightarrow\mathcal H\longrightarrow\mathcal V
\xrightarrow{\exp}\mathcal A\longrightarrow0.
\]

The physical vertical field gives the subline (mathcal O\subset\mathcal V). Projection to the elliptic source gives quotient (mathcal O(-1)): its finite invariant differential extends in the actual nodal dualizing chart, while at infinity (dx/y=z\,dX/Y). The dual source frames satisfy (e_0=t e_\infty). The line extension is split by the explicit Laurent/Cauchy solution in (mathcal O(1)). Its cocycle is obtained by differentiating the full point-line transition functions, so this operation retains those coefficients. Consequently (H^0(\mathcal V)=\mathbb C\) in the physical direction and (H^1(\mathcal V)=H^2(\mathcal V)=0).

The integral middle vanishing above now gives the entire global translation group:

\[
H^0(\mathcal A)=\mathbb C/(2\pi i\mathbb Z)
\xrightarrow{\exp}\mathbb C^*_{\rm physical}.
\]

There is no unexamined finite component in this conclusion; it is removed by the actual integral H1 computation. The same translation sheaf acts on each clutched torsor because its translation transition maps commute.

Choose one protected smooth value d, away from all moving singular fibres on a sufficiently small full s-disc. In the local point coordinate the actual complex translation flow is

\[
\mathcal F_w(Z,V)=(e^{-w\log P}Z,e^{w\log C}V),
\qquad C=\lambda(t-t_c)\beta.
\]

It has inverse (mathcal F_{-w}), in the same based logarithms, and (mathcal F_1=B). Thus (Psi_d=\mathcal F_{\log(t-d)/(2\pi i)}) is the actual positive cap-to-ordinary gluing, since a branch change applies precisely the original suspension deck map. This retains the direction; K78's ordinary-to-disc convention is not silently substituted for it.

In the original point-line coordinate the complete coefficient is

\[
(Z,v_M)\longmapsto
\left(AZ,
e^{w\log C}\frac{F_{P^8}(Z)}{F_{P^8}(AZ)}v_M\right),
\qquad A=e^{-w\log P}.
\]

Its inverse evaluates the reciprocal at the target point (Z'=AZ). The numerator and denominator are the actual point/O Cartier arrows, so their apparent meromorphic factors are not removed. This is an isomorphism of the actual point modules. The flow commutes with both full period generators. On the protected cap it is holomorphic and has the stated inverse.

Compare the original cap at0 with the cap at d, transporting its complete integral vector, including k,r and (d_\delta), along the prescribed cuts. Their total norm difference is (1-1=0). The preceding explicit integral inverse removes every remaining zero-norm component in the full based period cochain. Eliminating the ordinary identity-action cut edges uses integral identity blocks; the inverse recovers their actual cochain entries. Thus no cap vector is reduced to its norm without a computed integral cochain.

On a refined base atlas let (g^X_{ij}=t_{\theta_{ij}}g^Y_{ij}) be the actual overlap difference. Lift it to the actual Lie coordinates and subtract the periods of that integral cochain. The resulting Lie cochain is closed. A concrete solution is as follows. Choose a fixed smooth base partition (
ho_j), put (a_i=\sum_j\rho_j\theta_{ij}), and subtract a global solution of the glued form (\bar\partial a_i). After the explicit splitting of (mathcal V), choose the partition constant near infinity. The form has compact affine support. In each of its two summands use

\[
u(t)=\frac1\pi\int_{\mathbb C}
\frac{\alpha_{\bar w}(w)}{t-w}\,dA(w).
\]

This has (\bar\partial u=\alpha) and (u=O(t^{-1})). For the (mathcal O(-1)) component, its infinity coordinate is (tu(t)), which also extends. Thus (s_i=a_i-u_i) is holomorphic and satisfies (\theta_{ij}=s_i-L_{ij}s_j). The literal maps

\[
F_i=t_{-s_i},\qquad F_i g^X_{ij}=g^Y_{ij}F_j
\]

glue, and their inverses are the opposite translations. On each parameter sector all base covers and contours can be fixed, so the full coefficients vary holomorphically in the parameter. Local comparisons along the interval are matched by their actual physical-scalar ratios.

At a selected fan these Lie sections exponentiate to entire nonzero torus units A,D. On its two standard vertices the maps are

\[
(a,b,c)\mapsto((AD)^{-1}a,Ab,Dc),\qquad
(u,v,w)\mapsto(ADu,D^{-1}v,A^{-1}w).
\]

They preserve the original height product and have reciprocal maps. Evaluating the same full units in each primitive character extends across every cone of any prescribed basis fan. At infinity the K116 full theta shift, point-module arrow and integer word map retain all eight components. These are the actual extended maps needed in the cap comparison.

## 5. The filled comparison family and the exact endpoint

The family Y with the cap at d exists on the full s-disc. The original moving node chart is (XY=t-s), so its total source and projection to s are smooth. At a selected collision the original selected height is exactly (t-s), and the prescribed toric charts vary with that height. At an unselected collision its whole Hom coefficient is a unit there. The infinity charts persist since (a_*\ne0). The protected ordinary cap is smooth throughout the disc.

On the compact source complement choose the original point-line Hermitian metric and the maximum of the full unscaled Hom norm. Taking a common sufficiently small nonzero scalar makes the original lift uniformly contracting. The compact annular fundamental domains and the finite original toric/cap collar representatives give properness and Hausdorffness. The explicit local charts make the projection a submersion. K116 and F35 supply the original sphere fibre on the prescribed fan; the actual comparison maps carry that fibre to Y. A physical-circle-averaged connection and reversed flow give its disc trivialization with the complex orientation.

At the original cap, (Q(0,s)=-s\kappa(0,s)), so a positive s-loop changes (\log Q) by (2\pi i). P and the full beta are nonzero holomorphic units and have zero local winding. At an unselected-cap point (t_c(0)\ne0), so C is also a unit and the original retained period jumps by (k\alpha). At a selected-cap point (t_c=s), so (C(0,s)=-\lambda s\beta(0,s)) adds one physical period; the complete jump is (k\alpha+\delta). The original fixed C* and fixed scalar give no other winding. All r and (d_\delta) components remain in the same computed cochain.

At a common protected reference fibre, the comparisons and actual endpoints have the same original linear period marking. Their discrepancy is therefore an extending translation with identity linear part. The explicit integral preimages carry the full jump, and the Cauchy solution carries its full Lie remainder. By the calculated global translation group,

\[
F_1E_XF_0^{-1}=CE_Y,
\qquad C\in\mathbb C^*_{\rm physical}.
\]

For any actual disc transport (P_Y:Y_0\to Y_1), the transported original return satisfies the literal identity

\[
F_0(E_X^{-1}F_1^{-1}P_YF_0)F_0^{-1}
=E_Y^{-1}C^{-1}P_Y.
\]

This follows by taking the inverse of (F_1E_XF_0^{-1}=CE_Y), so no endpoint has been replaced by an unmarked identification. The path (\exp(\theta\log C)) is the actual physical action on every line, cap and fan. It removes C through an oriented isotopy. The remaining Y-return is the boundary of its disc trivialization, hence is isotopic to the identity. The resulting class is0 for every one of the twenty-four marked meridians. Reversing the path uses the reciprocal source, Cartier, cochain, cap and flow maps and also gives0.

Finally, for each original admitted fixed scalar decrease its modulus to the common disc scalar along its constant-argument interval. Contraction is preserved on the original boundary throughout this interval. The full (\log\lambda) remains in the periods and cap maps, with no additional turn. The resulting proper annular family, its endpoint-relative horizontal flow and its reverse identify the original return with the computed one. This proves the prescribed fixed-scalar scope rather than a claim only at the auxiliary smaller scalar.

## Frozen conclusion and receiving boundary

The above derives the complete zero-return route from the isolated statement and the permitted pre-existing constructions. The actual integral period complex and explicit zero-norm preimages are newly derived; the source, Cartier, Lie, endpoint and scalar maps are written before the receiving K119 proof is opened. The known construction/fan inputs remain cited inputs, and no fresh independent proof of all their supporting theorems is claimed.

No unresolved mathematical step in this derivation has been deferred to the receiving K119 proof. The receiving comparison must still check that its exact source frames, branch signs, original reference integers, period-image complex and endpoint maps agree with these constructions. The code alone is not the full geometric proof; the analytic and topological maps above are its written complement.

Actor: GPT-6 Astra (OpenAI), ChatGPT Pro mode; reasoning effort inherited from root and not separately exposed.
