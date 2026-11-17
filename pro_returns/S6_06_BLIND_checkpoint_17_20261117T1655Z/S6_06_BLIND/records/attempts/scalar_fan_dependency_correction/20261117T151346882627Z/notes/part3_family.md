# Part 3: rank-one sources, height arithmetic, and the mapping-class bridge

This file records independent derivations, begun after the blind Part 5 proof
was written but before its scheduled hourly checkpoint. No source stating
the tangent cohomology or full automorphism group of the AC26 threefold has
been opened. The calculations below do not use any earlier-run proof.

## P3F.1. The eight Mordell--Weil lattices and the 21 fibre configurations

**Proved.** The rank-one, torsion-free Mordell--Weil cases in the
Oguiso--Shioda Main Theorem are precisely the following. Here (P) denotes
a generator, (h(P)=\langle P,P\rangle), and (I_1^r) denotes (r)
distinct nodal fibres. Every configuration in the last column occurs over
the complex numbers with Mordell--Weil group isomorphic to \(\mathbb Z\).

| OS91 row | Root lattice | \(h(P)\) | Configurations |
|---|---|---|---|
|43|\(E_7\)|\(1/2\)|\(III^*+I_1^3\); \(III^*+II+I_1\)|
|45|\(A_7\)|\(1/8\)|\(I_8+I_1^4\); \(I_8+II+I_1^2\)|
|46|\(D_7\)|\(1/4\)|\(I_3^*+I_1^3\); \(I_3^*+II+I_1\)|
|47|\(A_6+A_1\)|\(1/14\)|\(I_7+I_2+I_1^3\); \(I_7+I_2+II+I_1\); \(I_7+III+I_1^2\)|
|49|\(E_6+A_1\)|\(1/6\)|\(IV^*+I_2+I_1^2\); \(IV^*+I_2+II\); \(IV^*+III+I_1\)|
|50|\(D_5+A_2\)|\(1/12\)|\(I_1^*+I_3+I_1^2\); \(I_1^*+I_3+II\); \(I_1^*+IV+I_1\)|
|55|\(A_4+A_3\)|\(1/20\)|\(I_5+I_4+I_1^3\); \(I_5+I_4+II+I_1\)|
|56|\(A_4+A_2+A_1\)|\(1/30\)|\(I_5+I_3+I_2+I_1^2\); \(I_5+I_3+I_2+II\); \(I_5+I_3+III+I_1\); \(I_5+IV+I_2+I_1\)|

The primary table was read in the scanned original, printed pp.85--86.
The program `code/part3/enumerate_mw_one.py` transcribes every rank-one row,
43--61, including all eleven rows with torsion. It then selects torsion
order one. Thus the eight-entry count is obtained by a reproducible
selection from the whole relevant table.

We now justify the refinement from root lattices to Kodaira fibres. The
Kodaira/root correspondences are (A_1=I_2\) or (III), (A_2=I_3\) or
(IV), (A_n=I_{n+1}\) for (n\geq3), (D_n=I^*_{n-4}),
(E_6=IV^*), and (E_7=III^*). Any further fibre is irreducible, hence
(I_1) or (II). Their Euler numbers must sum to 12. The program takes
the Cartesian product of these choices, then enumerates every nonnegative
solution (r+2s=12-\sum e(F_{\rm red})). It obtains 24 candidates.

For a candidate let (d=\deg j=\sum n(i_n+i_n^*)), and use (j/1728),
so that the elliptic values are (0,1,\infty). Put

\[
 a_0=ii+iv^*,\qquad b_0=iv,
 \qquad a_1=iii+iii^*.
\]

The minimal ramification profiles over 0 and 1 are respectively

\[
 1^{a_0}2^{b_0}3^{(d-a_0-2b_0)/3},\qquad
 1^{a_1}2^{(d-a_1)/2}.
\]

Over infinity they are the multiplicative fibre indices, including the
indices of (I_n^*). Hence the excess ramification

\[
 x=2d-2-\sum_{u\in\{0,1,\infty\}}\sum_{e\in\rho_u}(e-1)
\]

is nonnegative. This is Miranda90 (1.11), and follows directly from
Riemann--Hurwitz: additional ramification can only increase the displayed
sum. Precisely three of the 24 candidates have (x=-1):

\[
 I_8+II+II,\qquad I_7+III+II,\qquad I_5+IV+III.
\]

They cannot occur. The other 21 have (x=0) or 1. For each of them the
program constructs four explicit permutations

\[
 \sigma_0\sigma_1\sigma_*\sigma_\infty=1
\]

on (d\) letters. The first, second, and fourth have the three profiles
above. The third is the identity for (x=0), a transposition for (x=1).
The generated group is transitive, and the program checks
\(\sum_\nu(d-\#\mathrm{cycles}(\sigma_\nu))=2d-2\).
The permutations are printed in full in `enumerate_mw_one.out` and stored
in `mw_one_configurations.json`.

To explain exactly what these certificates establish, take positively
oriented meridians about (0,1,z_*,\infty\) on the Riemann sphere, with
their product relation in the displayed order. The permutations define a
connected finite unramified cover of the complement. At a cycle of length
(e), attach a disc by the chart (z\mapsto z^e). This gives a compact
connected Riemann surface and a holomorphic branched map. The verified
Euler equation gives genus zero, so the source is a Riemann sphere. This
is a (j)-map with the specified profiles. Miranda90 Proposition3.4
constructs the corresponding elliptic surface by pullback of its displayed
universal (j=t\) surface, followed by the specified quadratic twists and
minimalizations. Its Euler number is 12 and it has a section, and the
proposition proves it is rational. Thus each certificate is an existence
certificate, not merely a necessary numerical test.

The root system (A_7) requires an extra check: OS91 rows44 and45 have the
same root system but different torsion. Here are explicit torsion-free
models for both configurations. Write

\[
 R=t^2+s,\qquad A=R^2+bt,\qquad
 B=R^3+\frac32btR+\frac38b^2,
 \qquad y^2=x^3-3Ax+2B.
\]

For ((s,b)=(1,1)),

\[
 4(-3A)^3+27(2B)^2
 =\frac{27}{16}(48t^4+8t^3+96t^2+72t+57).
\]

The program verifies that this quartic is square-free and coprime to
(A,B), so there are four (I_1)'s. At infinity the minimal Weierstrass
coefficients are units and the discriminant has order8, giving (I_8).
For ((s,b)=(3,48)), the same discriminant expression is

\[
 186624(t+3)^2(3t^2-10t+51).
\]

Here (A,B) each have a simple zero at (-3); hence that fibre is (II).
The quadratic factor is square-free, coprime to (t+3), and gives two
(I_1)'s. Again the infinity fibre is (I_8).

Neither model has a 2-torsion point. After (x=X+R), its cubic is

\[
 X^3+3(t^2+s)X^2-3btX+\frac34b^2.
\]

A root in \(\mathbb C(t)\) would be a polynomial because the cubic is
monic over the integrally closed ring \(\mathbb C[t]\). Its degree is at
most two. For degree at most one, comparing the coefficient of (t^4)
first eliminates the linear term, then the coefficient of (t^2)
eliminates the constant term. The nonzero constant (3b^2/4) remains.
For a quadratic root, its leading coefficient must be (-3); the next
two coefficients force (X=-3(t^2+s)), which leaves
(9bt(t^2+s)+3b^2/4\ne0). Thus no root exists. OS91's only two
rank-one (A_7) cases have torsion 0 and \(\mathbb Z/2\); both displayed
models therefore belong to row45. The remaining seven root systems each
have a unique torsion-free rank-one row, so no such ambiguity occurs.

This proves the exact count (2+2+2+3+3+3+2+4=21).

## P3F.2. Heights, component data, and the sign of the correction term

The primary source is Shioda90 Theorem8.6, equation(8.12), with local
contributions in table(8.16), printed pp.228--229. Proposition8.12,
equation(8.25), printed p.231, gives multiplication of heights by the
degree of a field extension. The scanned statements and their proofs
were read; OCR is retained only as a discovery aid.

For a section (R\ne O) of a relatively minimal elliptic surface with
section,

\[
 h(R)=2\chi(\mathcal O)+2(R\cdot O)
       -\sum_v\operatorname{contr}_v(R).
\]

Consequently the exact rearrangement is

\[
 (R\cdot O)=\frac{h(R)-2\chi(\mathcal O)
                    +\sum_v\operatorname{contr}_v(R)}2. \tag{P3F.2.1}
\]

The local contributions in Shioda's convention are nonnegative. The
general formula stated in the prompt with a minus sign before these
contributions therefore has the wrong sign in this convention. This is
an algebraic discrepancy independent of the unfinished identification of
the expression with a monodromy invariant.

For a primitive generator of each of the eight rational-surface cases,
the local contributions and component orders are as follows. Either
choice of a pair of components exchanged by inversion is allowed.

|Root system|Component data for (P)|Sum of contributions|Orders|
|---|---|---|---|
|\(E_7\)|nonidentity component|\(3/2\)|2|
|\(A_7\)|component3 or5 of (I_8\)|\(15/8\)|8|
|\(D_7\)|a spinor component|\(7/4\)|4|
|\(A_6+A_1\)|component2 or5 of (I_7\), nonidentity (A_1\)|\(10/7+1/2\)|7,2|
|\(E_6+A_1\)|nonidentity in both|\(4/3+1/2\)|3,2|
|\(D_5+A_2\)|spinor, nonidentity|\(5/4+2/3\)|4,3|
|\(A_4+A_3\)|component2 or3 of (I_5\), component1 or3 of (I_4\)|\(6/5+3/4\)|5,4|
|\(A_4+A_2+A_1\)|component1 or4 of (I_5\), nonidentity (A_2,A_1\)|\(4/5+2/3+1/2\)|5,3,2|

Here (A_1) and (A_2) have the same nonzero local contribution for
either of their two Kodaira realizations. To derive, rather than assume,
the table, use (h(P)) from P3F.1 and enumerate all multiplicity-one
components in Shioda's local table. The sum of the largest permitted
contributions is always smaller than (4-h(P)). Since (P\cdot O\geq0)
is an integer, the height formula excludes (P\cdot O\geq1).
It follows that (P\cdot O=0). The equation
\(\sum\operatorname{contr}_v(P)=2-h(P)\) then gives exactly the
component choices displayed. Thus for every one of the 21 configurations
the primitive generator is disjoint from the zero section.

For the OS49 configuration (IV^*+II+I_2), place (IV^*) at0 and
(I_2) at infinity, and pull back by the degree3 map (t=z^3).
The relatively minimal pullback has three (II) fibres and one (I_6),
so \(\chi=1\). The (IV^*) fibre has good reduction on the cubic root
chart. The generator has height (3/6=1/2). Its component1 at (I_2)
pulls back to component3 at (I_6), contributing (3\cdot3/6=3/2).
Equation(P3F.2.1) gives (P'\cdot O'=0). Substituting the negative sign
from the prompt instead would give (-3/2), not the intersection number.
This calculation concerns the explicit compact elliptic pullback.
The actual regular-binding page and its boundary comparison are
constructed in P3F.31; its map has three separate I2 fibres.

## P3F.3. Jin's mapping-class theorem in the exact coordinates required

The primary source is Huize Jin, arXiv:2608.26698v2 (12September2026),
Theorem1.2, Corollary1.3, Proposition3.1, Lemmas4.4 and4.8, and
Theorem4.9. The downloaded PDF is retained in `records/primary_sources`.
The ambient manifold is the oriented product (M=S^2\times S^3).
Its orientation-preserving Torelli group is

\[
 I(M)=\mathbb Za\oplus\mathbb Zb.
\]

Here (a=t_{S_1,\alpha}) twists a standard (S^2\times D^3), and
(b=t_{S_1\#S_1,\alpha}) twists the connected sum of two oriented
copies of that core (S^2). The normalization of
\(\alpha\in\pi_3SO(3)\) is that the rank3 bundle over (S^4) clutched
by \(\alpha\) has first Pontryagin number4. The twist is explicitly

\[
 (x,y)\longmapsto(\alpha(y)x,y),
\]

where \(\alpha:D^3\to SO(3)\) equals the identity near its boundary.
Extending by the identity gives the same formula with
\(\alpha:S^3\to SO(3)\). In particular the core sphere has dimension2.

For (f\in I(M)), Jin uses

\[
 M_f=M\times[0,1]/((x,0)\sim(f(x),1)),
\]

with the preferred spin structure specified by a fixed disc and a class
\(x\in H^2(M_f;\mathbb Z)\) restricting to the positive generator on
(S^2\). Put

\[
 k(f)=\langle x^3,[M_f]\rangle,\qquad
 \ell(f)=\langle p_1(TM_f)x,[M_f]\rangle,
 \qquad A(f)=\frac{4k(f)-\ell(f)}{24}.
\]

The theorem identifies \(f\mapsto(A(f),k(f))\) with an isomorphism
\(I(M)\to\mathbb Z^2\). Its normalization gives

\[
 (k(a),\ell(a))=(1,4),\qquad
 (k(b),\ell(b))=(8,8),
\]

so (b-8a\) and (a\) map to the standard ordered basis of
\(\mathbb Z^2\). In particular

\[
 [f]=(k(f)-8A(f))a+A(f)b. \tag{P3F.3.1}
\]

These assertions follow from the cited theorem by direct substitution,
and verify that the congruence is
\(\ell\equiv4k\pmod{24}\). The pair ((-1,-4)) gives ([f]=-a\).
It is a nonzero element of (I(S^2\times S^3)); its effect on the
associated glued 7-manifold is computed explicitly next.

## P3F.4. The Hopf gluing associated with the subgroup \(\mathbb Za\)

**Proved.** Every Hopf lift of (a^n\), for (n\in\mathbb Z\), gives
the standard oriented 7-sphere by the following gluing construction.
This specifies the morphisms required to pass from these mapping classes
to homotopy spheres.

Use unit quaternions (S^3\subset\mathbb H\) and
\(S^2\subset\operatorname{Im}\mathbb H\), with Hopf map
\(h(u)=uiu^{-1}\). The principal circle acts on the right on (u\).
On

\[
 p:S^3\times S^3\longrightarrow S^2\times S^3,
 \qquad p(u,y)=(h(u),y),
\]

fix its Chern class to be the chosen positive generator; reversing the
orientation of the Hopf fibre changes the sign and does not change the
extension argument. Lift \(\alpha:S^3\to SO(3)\) to
\(\widetilde\alpha:S^3\to SU(2)\), using the double cover given by
quaternionic conjugation. The lift exists because (S^3\) is simply
connected. The map

\[
 A_n:S^3\times S^3\to S^3\times S^3,
 \qquad (u,y)\longmapsto(\widetilde\alpha(y)^n u,y)
\]

is a smooth principal-circle-bundle automorphism covering (a^n\).
The equality (h(vu)=v h(u)v^{-1}\) verifies this statement, and left
quaternionic multiplication commutes with the right Hopf action.
Crucially it is the boundary restriction of the explicit diffeomorphism

\[
 E_n:D^4\times S^3\longrightarrow D^4\times S^3,
 \qquad (q,y)\longmapsto(\widetilde\alpha(y)^n q,y). \tag{P3F.4.1}
\]

Its inverse uses the inverse unit quaternion, and it preserves orientation.

Fix the orientations in the decomposition

\[
 S^7=\partial(D^4\times D^4)
     =(D^4\times S^3)\cup_{\mathrm{id}}(S^3\times D^4)
\]

by the outward-normal-first convention and rounding the corner. Gluing
the first piece to the second by (A_n\) gives a manifold carried to
this standard boundary by (E_n\) on the first piece and the identity
on the second. This is an explicit orientation-preserving diffeomorphism.

Any two principal-circle lifts of the same base map differ by a gauge
map (g:S^2\times S^3\to S^1\). Because
\(H^1(S^2\times S^3;\mathbb Z)=0\), it lifts to a smooth real function
and is isotopic to the constant map through gauge transformations. Base
isotopies lift to bundle isotopies, by the homotopy lifting property for
bundle isomorphisms (or by horizontal lifting for a chosen connection).
Boundary-isotopic gluing maps give diffeomorphic glued manifolds: extend
the isotopy over a collar. Thus the conclusion depends only on the base
mapping class, and holds for every lift and every representative of
(a^n\).

For completeness, the same Hopf-lift construction assigns a homotopy
7-sphere to any (f\in I(S^2\times S^3)\). Its lift acts on
\(H_3(S^3\times S^3)\) by a matrix

\[
 \begin{pmatrix}1&c\\0&1\end{pmatrix}
\]

for an integer (c\): the lower row follows by projection to the base
(S^3\), and the first diagonal entry follows from the positive Hopf
bundle map over the positive (S^2\) generator. In Mayer--Vietoris the
map to the two piecewise (H_3\)'s is
\(\left(\begin{smallmatrix}0&1\\1&c\end{smallmatrix}\right)\), of
determinant (-1\). All intermediate reduced homology vanishes; van
Kampen gives simple connectivity. Hence the glued manifold is a homotopy
sphere. No assertion that this assignment is a group homomorphism is
needed for the explicit computation on \(\mathbb Za\).

Combining this construction with (P3F.3.1) computes the Hopf-glued sphere
for the numerical pair ((-1,-4)): its oriented class is zero.
P3F.8 supplies the actual geometric identification with the family,
and P3K.6--9 derive the characteristic numbers from its charts and
its specified descended rotating framing. The classification theorem
is used only after these geometric comparisons.

## P3F.5. The precise Haefliger formula and the missing page comparison

Takase's primary correction paper, *The Hopf invariant of a Haefliger
knot*, arXiv:math/0506356, Theorem2.3 and Corollary2.6, gives the formula

\[
 \Omega(F)=-\frac{\sigma(V)-e(\nu V)^2}{8} \tag{P3F.5.1}
\]

for an actual Seifert embedding (V^4\hookrightarrow S^6\) with
\(\partial V=S^3\). The orientation conventions are stated on p.2 of
that paper. The square is computed using the boundary identification and
the cap, not an unspecified square on an arbitrary open surface.

The algebraic expression in the prompt would match this formula after
the explicit comparison (e(\nu V)^2=4s_\delta\) and the compatible
relative Pontryagin/trivialization comparison. The following test shows
that the compact elliptic pullback cannot simply be punctured and used
with this normal Euler class. The degree12 pullback over the compact
genus3 curve has \(\chi(\mathcal O)=1\), no multiple fibres, and

\[
 K=(\chi+2g-2)F=5F,\qquad w_2=F\bmod2.
\]

Its section intersects (F\) once, so this class is nonzero, including
after removing a small ball disjoint from the section. An oriented
embedding of this punctured surface in (S^6\) would satisfy
\(w_2(TV)=w_2(\nu V)=e(\nu V)\bmod2\), by the Whitney formula and
the spin structure on (S^6\). The particular normal Euler class \(2c_1(M)\) has zero reduction. Thus that specific puncturing with that specific normal bundle cannot furnish the required Seifert embedding. The prompt itself requires only its square: the characteristic class \(K+2c_1(M)\) has the same square \(4c_1(M)^2\), because \(K^2=K\cdot M=0\). Therefore this parity test does not refute the square required in the prompt.

This is a proved obstruction to that comparison. It does not rule out
the additional removals, handle attachments, and compatible framings
that an actual open-book page may possess. Those modifications have to
be constructed and included when computing its characteristic numbers.

## State of the family-monodromy application

The 21 configurations above are now completely enumerated and realized.
The statement in the supplied CSV about a bounded slice of 50 inputs
does not define its bounds or which section pairs, linearizations, and
local fillings constitute an input. The number50 is therefore not used
as a computed result here. The further supplied rows assert additional
larger searches, but provide no proof data and do not define the missing
bounded slice.

The initial main-case gap has been resolved by the actual orbit and
Hopf comparison P3F.7--13, the real trace P3K.6--7, the independent
analytic index calculation P3K.8, and the rotating-frame computation
P3K.9. These prove zero positive-loop class for the original family
and give ((k,\ell)=(-1,-4)\) in the stated descended framing.
P3F.25 applies the same actual trace to the further verified families
and computes the nonzero weighted OS47 example. The actual
component-supported OS49 page and both diagonal-fan returns are
proved in P3F.31--32 and P3K.17, retaining the marking of P3F.27. The exact earlier status passages are preserved, with their
superseding proof identifiers, in
`records/part3_superseded_status.md`.

## P3F.6. Proved: the two degree-twelve maps must be distinguished explicitly

Let C be the smooth compactification of b³=a⁴+1. The function x=b³
defines a degree12 map to P1 with ramification profiles

| x-value | profile |
|---|---|
| 0 | 3,3,3,3 |
| 1 | 4,4,4 |
| infinity | 12 |

Indeed near b=0 the four roots of a⁴=-1 are distinct, so b is a local
parameter and x=b³. Near a=0 there are three points and x-1=a⁴. The
coprimality of 3 and4 gives one point at infinity, with poles of orders3
and4 for a,b respectively, and hence pole order12 for x. The total
ramification is8+9+11=28, and Riemann--Hurwitz gives 2g-2=-24+28=4.

For the E26 base with IV*,III,I1 over0,1,infinity, the pullback by t=x
has a single I12 fibre after minimalization, by local semistable base
change of the nodal model. There is a different map on the very same
curve that gives twelve I1 fibres. Choose a regular finite value t*
different from0,1 and set

    t=mu(x)=t* x/(x+t*-1).

This sends the three branch values0,1,infinity to0,1,t*. Its inverse
image of the source cusp infinity is the regular x-value1-t*, and so
has12 distinct points, all unramified. The pullback has twelve I1
fibres. Its order3 and order4 branches still remove IV* and III, while
the order12 branch lies over a smooth elliptic fibre. The curve alone
therefore does not specify which of these fibrations is being used.
The Milnor page of a regular (3,4) Seifert fibre uses a regular binding
value t* and leads to the second map. The actual four-dimensional
page, its boundary surgeries and its real trace are constructed in
P3K.6--7.

In either compact minimal pullback, the canonical formula gives
K=5F, chi(O)=1, and sigma=-8. The height pulls back to2. All multiples
of P meet the identity component in the I12 case, because P already
meets the smooth locus of the original I1 fibre; there are no reducible
fibres in the twelve-I1 case. Hence (mP).O=m²-1 in both cases.

The parity test in P3F.5 only excludes the normal Euler class2M for a
ball-puncture of this nonspin compact surface. It does not exclude the
square required in the prompt: e=K+2M is characteristic, and
e²=4M² because K²=K.M=0. No conclusion about the actual relative normal
class follows until its cap and framing have been identified.

## P3F.7. Proved: the orbit pair and the local conifold surgery

For the AC26 sphere member, its delta circle is semifree, has one fixed
curve F=P1, and its orbit pair is diffeomorphic to the standard pair
(S5,S2). Its fixed normal bundle is O(-1) plus O(-1) with respective
weights(-1,+1). Replacing that fixed neighbourhood by the conifold
smoothing gives a free circle manifold S3 times S3, with quotient
S2 times S3.

Proof. On an ordinary fibre the delta circle is primitive and acts
freely. At a finite cap, a nontrivial deck power has nonintegral gamma
character, since gamma(v_j) is prime to m_j. It therefore cannot agree
with a delta circle rotation. This proves freeness there. In the cusp
fan the directions are ±e1,±e2,±(e1-e2). A finite circle stabilizer at
an edge of direction d has order dividing det(d,e2), which is±1 off
the e2 edges; on an e2 edge the entire circle fixes it. At the two-dimensional torus orbit corresponding to a vertex of the
height-one triangulation there is no stabilizer. The zero-dimensional
torus orbits corresponding to triangles are fixed, and each lies on
one of the fixed edges. The period lattice acts transitively on the e2 edges, with no
stabilizer, so their quotient is one fixed P1.

For the vertical wall use the four rays

    r0=(0,0,1), r1=(0,1,1), r+=(1,0,1), r-=(-1,1,1).

They satisfy r++r-=r0+r1. The two adjacent unimodular charts have
coordinates(x0,x1,z) and(x0',x1',z'), with exact transition

    x0'=z x0,  x1'=z x1,  z'=1/z,
    q=x0 x1 z=x0' x1' z'.

The fixed curve is x0=x1=0. The transitions give O(-1)², and the
cocharacter e2 has weights(-1,+1,0). These identities are independently
checked from the ray matrices in code/part3/orbit_mv.py. The map

    A=x0, B=z x0, C=x1, D=z x1

contracts the curve to AD=BC. It intertwines the circle with weights
(-1,-1,+1,+1) on(A,B,C,D). On AD-BC=epsilon nonzero the action is free.
For epsilon=1, polar decomposition of SL2(C) as U H gives the explicit
equivariant diffeomorphism SU2 times R3, with the circle acting on U
by left multiplication and acting trivially on H. A compact Milnor
neighbourhood is thus S3 times D3 and its quotient is S2 times D3.

For completeness, the orbit is identified integrally. Let A=X minus F
and B=A/S1. General position gives pi1(A)=0. Alexander duality gives
H*(A;Z)=Z in degrees0,3 and zero otherwise. The oriented normal link
S3 is a primitive generator of H3(A). Its quotient is the normal link
S2, and the circle bundle on these links is the Hopf bundle. In the
Gysin sequence, e generates H2(B), and integration H3(A)->H2(B) is
multiplication by1: evaluate on this linked S2 and its Hopf preimage.
Every other positive-degree group of B vanishes. Also pi1(B)=0 by the
homotopy sequence of the principal circle bundle.

Conjugating the negative-weight line converts the fixed normal bundle
to a positive-weight complex bundle O(1) plus O(-1). Its clutching loop
diag(z,z^-1) in SU2 bounds the explicit disc with SU2 coordinates
(a,b)=(r exp(i theta),sqrt(1-r²)); joining its centre to the identity
gives a nullhomotopy. Thus it is a trivial unitary rank2 bundle. Its
orbit normal bundle is a trivial oriented rank3 bundle. With this
trivialization the boundary is F times S2, and the Euler class is just
the meridian generator, with no F term.

Now Y=X/S1 is the union of B (truncated at that boundary) and F times
D3. The maps on H0 and H2 in Mayer--Vietoris, with domain H2 ordered
(F,meridian) and target(complement,tube), are respectively

    [1;-1],       [[0,1],[-1,0]].

The latter has determinant1. H4(boundary)=Z maps to zero and gives
H5(Y)=Z; every other positive intermediate group is zero. All matrices
and their Smith forms are printed in orbit_mv.out. Van Kampen gives
pi1(Y)=0. Thus Y is a homotopy5-sphere. Kervaire--Milnor1963, the table
on p505 and the Smale comparison stated immediately above it, gives
Theta5=0, so Y is diffeomorphic to S5. Haefliger1966 Corollary6.6 says
C_n^q=0 for n<2q-3; with n=2,q=3, and Theorem1.2 converting concordance
to isotopy, every embedding S2 in S5 is unknotted. This identifies the
orbit pair.

One may now construct the equivariant identification with the standard
circle action on the sphere boundary of D3 times D4. On the free
complement the principal circle bundle over S2 times D3 has Euler
generator and is the product Hopf bundle S3 times D3. On the fixed
tube it is the trivial positive-weight rank2 bundle just constructed.
Their two boundary identifications differ by a gauge map from S2 times
S2 to S1. Such a map has a global logarithm because H1(S2 times S2;Z)=0,
so it extends over a collar and removes the discrepancy. This gives an
equivariant diffeomorphism. It is also the specialization of Levine's
classification as stated in Harvey--Kerin--Shankar2020 Theorem4.1,
whose hypotheses are checked here: smooth codimension4 fixed set and
H2(F;Z) without2-torsion. Replacing the fixed tube S2 times D4 by the
free piece D3 times S3 doubles the free complement, giving S3 timesS3;
the quotient doubles S2 timesD3, giving S2 timesS3. The normal framing
is unique up to homotopy because pi2(SO4)=0. This is the asserted
conifold surgery. End of proof.

## P3F.8. Proved: the actual equivariant family has a typed Hopf-gluing image

Let Phi be the actual positive parameter return map of the sphere
family, with the complex orientation, represented by an equivariant
Ehresmann trivialization. There is a Torelli diffeomorphism f of
S2 timesS3, supported in S2 timesD3, for which the oriented sphere
clutched by Phi is exactly the Hopf-lift gluing lambda(f) of P3F.4.
This statement identifies the morphism; it does not assume values of
the two integer invariants of f.

Proof. The parameter family carries the delta circle action. Its fixed
curves form a P1 bundle around the parameter circle; the two normal
weight lines have degree-1. The fixed-curve bundle is smoothly trivial
because PGL2(C) is connected. Each weight line over P1 timesS1 is
isomorphic as a smooth complex line bundle to the pullback of O(-1),
since H2(P1 timesS1;Z)=Z. Thus its equivariant normal disc bundle can
be trivialized around the parameter circle. Choose an Ehresmann
connection agreeing with that trivialization near the fixed set;
averaging over the compact circle makes it equivariant. Its return map
is the identity near the fixed tube.

Under P3F.7 write the sphere as

    (S2_y timesD4_u) union (D3_y timesS3_u),

with the circle the Hopf action on the u coordinate. Conjugating the negative
normal line reverses its real two-plane orientation; choose the
orientation of the y factor so that this identification preserves the
complex orientation of X. The restriction
of Phi to the free part is an equivariant map tilde f of D3_y timesS3_u
equal to the identity near its boundary. Its quotient is a map of
D3_y timesS2_u relative boundary. Extend it by the identity over the
other hemisphere of S3_y. This defines f:S3_y timesS2_u -> S3_y timesS2_u.
It fixes the H2 generator, since that generator is represented in the
identity hemisphere. It preserves orientation, so Poincare duality
makes it fix H3 as well. Consequently f is in the Torelli group.

Its Hopf lift A on S3_y timesS3_u equals tilde f on the first
hemisphere and the identity on the second. Any other lift differs by
a gauge map S2 timesS3 -> S1. Its H1 is zero, so that map has a global
logarithm and yields an isotopy of lifts.

Here is the cut-and-reglue comparison. In the standard sphere
boundary(D4_u timesD4_y), put

    H=D4_u timesS3_y,  K=S3_u timesD4_y,
    N=S3_u timesD3_y in boundary H=boundary K.

Our gluing convention identifies x in boundary H with A(x) in
boundary K, after the standard product-boundary identification.
The ball B7=D4_u timesD3_y has boundary equal to N union
(D4_u timesS2_y). Its complement in the rounded product boundary is
the other standard7-ball: this follows by taking the two hemispheres
of the y boundary and rounding their product collars. Regluing H to
K by A changes the identification only on N. Equivalently cut out B7
and reglue its boundary by the map equal to tilde f on N and the
identity on D4_u timesS2_y. That boundary map is precisely Phi in the
displayed decomposition of S6. The identity on the common collar
makes the two quotient constructions coincide pointwise outside N,
and their collar identifications coincide on N. Hence

    D7 union_Phi D7  =  (D4_u timesS3_y) union_A (S3_u timesD4_y)

as oriented smooth manifolds, with outward boundary orientation on
the first piece and the complex sphere orientation used to choose
the initial identification. This is lambda(f). End of proof.

The actual sixfold descent of P2.1 is

    H(t)delta, H(t)=-(4l1 log t+3l2 log(t-1))/(2pi i),

with cusp coefficient -p after carrying the collar integer l0.
P3K.6--7 constructs its real trace with the complete line clutch.
P3K.9 evaluates its characteristic pair as(-6,-24), including the
normal-frame comparison, and descends it to(-1,-4) for one parameter
loop. The forward geometric mapping-torus orientation and Jin's
reverse convention are both included in P3K.7.

## P3F.9. The resolved cusp orbit as a nodal elliptic neighbourhood times a circle

The local calculation giving the product is as follows. Start with the
ordinary conifold xy=uv, with the circle acting on u,v with weights+1,-1
and fixing x,y. A small resolution has charts

    (x,v,z),   u=xz, y=vz;
    (u,y,w),   x=uw, v=yw;      w=1/z.

The orbit charts, with the Hopf smoothing defined using these normal
coordinates, are

    (x,y,b), b=(|z|²-|v|²)/2;
    (x,y,b'), b'=(|u|²-|w|²)/2.

On the overlap r=|z|²>0 they satisfy

    2b=r-|y|²/r,       2b'=|x|²r-1/r,
    db'/db=(|x|²+r^(-2))/(1+|y|²r^(-2))>0.       (P3F.9.1)

Thus projection to(x,y) is a smooth submersion with oriented
one-dimensional fibres. Every fibre is a line: away from(x,y)=(0,0)
the two charts join its negative and positive ends in the displayed
increasing order; over(0,0) the exceptional interval joins the two
half-lines. A smooth section can be chosen in the free part. For
epsilon>0 choose the unique r>0 solving

    |x|²r-|y|²/r+2epsilon(r-1)/(r+1)=0.

The left side increases strictly from a negative to a positive value;
its derivative is |x|²+|y|²/r²+4epsilon/(r+1)²>0. Consequently r is a
smooth positive function of(x,y), and the representatives
z=sqrt(r),v=y/sqrt(r),u=x sqrt(r) give the section in the orbit.
A positive vertical vector field, patched by a partition of unity and
rescaled to be complete, identifies each line with R by flow from this
section. It therefore gives a product diffeomorphism over C².

This comparison can be made relative to a prescribed product
identification outside the node neighbourhood. The quotient smoothing
uses a choice of invariant metric in the fixed normal bundle; choose
it to agree with the original product normal metric outside that
neighbourhood. There projection to(x,y) is the original smooth
submersion. On overlapping local line trivialisations the transitions
are increasing by(P3F.9.1). Taking a partition of unity on the base and
a convex combination of increasing, proper fibre coordinates produces
an increasing proper coordinate agreeing with the prescribed one where
the outer partition has weight1. This is a relative product
trivialization. Its derivative over the fixed (x,y) base is an upper
triangular real matrix with identity base block and a positive fibre
derivative. Contracting the off-diagonal block and then the positive
scalar gives a homotopy to the identity relative to the prescribed
outer product. Thus this comparison retains the stable boundary
framing, not just the orbit diffeomorphism type. In particular one must not equate all quadratic
invariants in different normal metrics at a fixed point: their
transition can involve a radial square root. The metric choice and the
positive-coordinate construction avoid that error.

Apply this calculation to the square Mumford fan before triangulation.
The square model is the fibre product of the two nodal elliptic models;
the A2 triangulation is its small resolution, one per lattice cell.
The circle acts in the second nodal factor. Its orbit is a smooth
circle bundle over the base disc, since its local quotient at the node
is(q=uv,(|u|²-|v|²)/2). It is a product over the disc. Before resolving
the conifold, the total orbit is therefore E_I1 timesS1, where E_I1 is
a compact neighbourhood of one nodal elliptic fibre in a smooth
elliptic surface. The relative comparison above replaces the node
orbit without changing this product diffeomorphism type or its outer
boundary marking.

The bounded toric units of the actual construction do not change this
statement. Choose their logarithms on the cusp disc. Their interpolation
to constant units gives the same unimodular charts and a proper smooth
family after shrinking the disc uniformly; the logarithmic terms
dominate every bounded unit. Averaging an Ehresmann field gives an
equivariant comparison. In the source elliptic factor, the gamma deck
translates by the section6P. Its Tate coordinate is a unit a(q), and
the explicit path Z->exp(t log a(q)) Z extends across the nodal fibre.
Its suspension is consequently a product E_I1 timesS1_gamma. The
source Picard line restricted to an elliptic neighbourhood selected
disjoint from the fixed sphere is topologically trivial: its degree on
the nodal fibre is zero, and that neighbourhood retracts onto the nodal
fibre. An extending Hermitian metric removes its radial unit on this
slice. This statement does not trivialize the principal-circle line on
the complement of the fixed sphere in the entire orbit neighbourhood.
That line has Chern number one, up to the fixed orientation convention,
on a meridian two-sphere; its meridian class is retained in every
subsequent clutch or index comparison. These comparisons preserve the integral
gamma,u,w and q markings on the outer boundary. Changes in the affine
stable frames consist of unit scalings and triangular shears and are
homotopic to the indicated diagonal factors; no three-dimensional
Pontryagin framing class is introduced by a logarithm of a unit.

The fixed sphere projects in E_I1 to the normalization of the nodal
fibre. The small-resolution interval separates its two preimages of
the node in the gamma direction. Its projected normal complex line
has transition a'=z²a, namely O(-2). Its Euler number, with the complex
orientation of that line and of the normalization, is-2. The gamma
coordinate of this sphere can be confined to an arbitrarily short arc
by taking the relative node comparison sufficiently small. Rotation of
the S1_gamma factor is a free action on the cusp orbit body and extends
the marked boundary gamma circle action.

This proves the claimed product comparison with the explicit boundary
marking, rather than identifying the singular central fibre itself
with a product. The map to the elliptic surface changes the transverse
leaves in the node neighbourhood, as its displayed small-resolution
charts show.

## P3F.10. Construction and characteristic data of the actual four-dimensional page

Here the data are the original sphere twists(0,1,-1). On the ordinary
and finite-cap orbit pieces, use the invariant gamma character in
smooth flat coordinates. The resulting three-dimensional quotient is
formed from S1_gamma times the punctured base and the two solid tori

    (S1_gamma timesDelta_s)/(g,s)->(g+l_j/m_j,zeta_j s).

The two meridian relations are3x=gamma and4y=-gamma; after the cusp
solid torus the third isx+y=0. The relevant integer matrix is
[[3,0,-1],[0,4,1],[1,1,0]], of determinant-1. The union of the two
Seifert solid tori is explicitly the standard weighted circle
fibration on S3 with weights3,4. Its meridian/longitude basis change is
unimodular, and the two stabilizer orders are3,4. This supplies the
Seifert identification, including the labelled exceptional fibres.

To compare the smooth flat coordinates with the holomorphic logarithmic
gluing, subtract the angular translation from(log s)/(2pi i)Pi v_j.
The remaining radial translation is single valued on the annulus and
has a real scalar homotopy to zero. Translation by this homotopy on a
collar gives the required equivariant identification. At the cusp use
P3F.9, relative to the outer gamma marking. This constructs a smooth
map of the actual orbit Y=S5 to the weighted S3. Its fibres are the
source elliptic curves; the critical curve is the nodal critical point
in E_I1 timesS1_gamma. Near that curve its formula is the ordinary
positive node map(x,y,gamma)->(xy,gamma). Thus it is an actual
one-parameter family of positive genus-one Lefschetz maps. The cusp
modification is included in the construction of this map.

Choose as binding a regular weighted fibre at a value t* different
from0,1,infinity. Its Milnor open-book page is explicitly the affine
curve b³-a⁴=1, embedded in S3 by

    (a,b)->(rho³ a,rho⁴ b),
    rho⁶|a|²+rho⁸|b|²=1, rho>0.

The inverse divides by the positive twelfth root of b³-a⁴ on the chosen
argument page. Its projection to the weighted base is the degree12
map of P3F.6, followed by the unique Möbius map sending the binding
value to t*. After adding the boundary circle the page is a genus3
surface C° with one boundary component. The regular cusp fibre in the
weighted S3 intersects this page in12 points. Their signs are positive
in the complex Milnor orientation, equivalently the map to the base is
holomorphic and unramified there. Its inverse image V0 in Y is
therefore a genus-one Lefschetz fibration over C° with twelve positive
nodal fibres. The boundary is the torus mapping torus of a translation,
hence T3. It need not be S3.

The page can be chosen disjoint from the fixed sphere: by P3F.9 its
gamma image lies in an arbitrarily short arc, and the phase of the
Milnor page can be chosen so that its twelve intersections with the
critical gamma circle avoid that arc. The delta circle bundle
therefore restricts to an honest principal circle bundle over V0.

We justify the comparison with its sectioned Jacobian without requiring
a section of a compact torsor. The affine elliptic bundle over C° is
locally the stated Jacobian, including the irreducible nodal fibres.
Its torsor obstruction lies in H²(C°,j_*Lambda_E). This group is zero:
cut the surface along its handle generators and disjoint paths to the
nodal values. In the punctured surface fundamental group, every nodal
meridian is an independent free generator because the boundary word
is not imposed as a relation. The restriction map from cocycles to
the direct sum of their cusp coinvariants is consequently surjective.
The exact sequence for j_*Lambda_E gives H²=0. Equivalently this is the
integer Cech obstruction to matching the local origins. The sheaf of
smooth Lie-algebra sections is fine, so this vanishing constructs a
smooth global section and an affine identification with the Jacobian.

The circle line has the fibrewise Picard class of P, not6P. This follows
both from the source definition M=O(P-O) and from its two elliptic
period multipliers: the u column contains mu while the gamma column
contains6mu. The latter records translation in the suspension. Under
an affine identification of a torus torsor with its Jacobian, a degree
zero line has the same Picard point. The quotient of two lines with
the same normalized fibrewise Picard point is pulled back from the
base: normalize a trivializing holomorphic fibre section at the chosen
origin, and its overlap ratios are constant on the compact fibres.
This argument remains valid at each irreducible node, where the
multiplicative gluing unit is the one supplied by M and a local ball
has no line-bundle obstruction. Thus on V0 its Chern class is that of
the Jacobian line O(P'-O'), up to a base pullback. Since the base has
boundary, that pullback is topologically trivial.

On the boundary regular torus the degree-zero line has unitary flat
fibre multipliers and the translating point has a flat lift. Thus its
restriction to T3 has zero Chern class. A relative lift of its Chern
class exists. If u and u+delta g are two lifts, with
g in H1(boundary V0;Z), the absolute class of delta g is zero and
restriction of the absolute class of u to the boundary is zero.
The relative cup-product boundary formula gives

    u cup delta g=delta(i*u cup g)=0,
    (delta g)²=0.

The relative square is therefore independent of every boundary gauge.
Choose the affine boundary identification furnished by the section
above and cap the Jacobian by its regular fibre timesD2. This gives
the compact elliptic pullback under the regular-binding cover of
P3F.6, with twelve I1 fibres. Its P'-O' line extends the actual page
line with some boundary gauge; gauge independence now makes

    s_delta=(P'-O')²=-2chi-2(P'.O')=-2.

This is the square of the section line P, not the square of6P. The
proof uses a section only on the surface with boundary; it does not
make any claim about a section on a compact genus-one torsor.

The same affine comparison identifies the relative stable tangent
framing with the regular product cap framing up to a map with zero
Pontryagin winding. Indeed its derivative is triangular with identity
linear derivative on the elliptic translation directions. The
remaining diagonal factors are complex line scalings; their maps
factor through a product of U1 groups. The universal degree-three
Pontryagin transgression vanishes on that torus (equivalently each
line factor has zero pi3), even when those scalings depend on all
boundary variables.
The triangular part is contracted by scaling its off-diagonal block.
The regular product cap has zero relative contribution. Therefore

    chi(O of the capped Jacobian)=1,
    signature(V0)=signature(capped Jacobian)=-8,
    p_rel=integral p1(capped Jacobian)=3signature=-24.

The signature equality uses the regular fibre neighbourhood
T2 timesD2, whose intersection form has zero signature; gluing along
the closed T3 boundary gives additivity. These statements give the
page and its actual line and framing data. The required actual return
comparison is the real spin bordism P3K.6--7, and its normal-frame
term is computed in P3K.9. Thus the later finite-group conclusion
uses both the page calculation and that geometric comparison.


## P3F.11. Proved: normal-framing changes and the integral reduction of parameter covers

Fix the orbit, Hopf and gluing conventions in P3F.7–8. For an
orientation-preserving equivariant return preserving the two complex
normal weight lines, its conifold replacement determines an integer

    A(Phi)=(4k(f)-ell(f))/24.

This integer is independent of the choice of equivariant tubular
trivialization used for the replacement. It is additive under
composition. In particular the actual return of the sixth parameter
cover has integer exactly6A(Phi). This assertion concerns the integral
Torelli invariant; it does not infer a class in Z/28 from multiplication
by6 in Z/28.

Here is the complete framing comparison. After conjugating the
negative normal line, the positive-weight bundle is
E+=O(1) direct-sum O(-1), trivial as an SU2 bundle as in P3F.7.
A loop of its unitary bundle automorphisms projectivizes to a loop
of SO3 gauge transformations of the normal quotient. To compare two
replacement fillings, take the product of this loop with the collar
of the boundary S2 and collapse its two ends. Its adjoint is a map

    alpha:S3 -> SO3.

On the replacement S2-meridian timesD3 this comparison is exactly
(x,y)->(alpha(y)x,y). This follows in each normal trivialization by
applying the projectivized unitary matrix to the Hopf line [u]; on the
common boundary the two original trivializations are those same
matrices. Hence the comparison is the primitive-sphere twist a to
an integral power, with no second Torelli component.

For precision about all loops, evaluation at one point gives the
fibration Map_*(S2,SO3)->Map(S2,SO3)->SO3 with its constant-map section.
Its fundamental group splits as pi3(SO3) plus pi1(SO3). The latter
factor consists of matrices independent of the S2 variable and
extends over the D3; it contributes no boundary-clutching map.
The first factor is exactly the displayed alpha. A loop of
orientation-preserving parametrizations of the fixed S2 also extends
by its radial SO3 action on D3, after Smale1959 Theorem A
(the strong deformation retraction of Diff+(S2) to SO3); equivalently its only fundamental-group ambiguity is
that same extending constant rotation. Thus it adds no second
Torelli component. These statements describe the actual morphism
from a normal-trivialization change to the return-map difference.

For the holomorphic phase loops the integer can be computed without
any homotopy shorthand. Let n_-,n_+ be their winding numbers on the
original weight-minus and weight-plus lines. Over S2_F timesS2_theta,
write h,t for the positive generators, and form the bundle obtained
by clutching those phase loops. Its two positive-weight line classes
are

    h-n_- t,      -h+n_+ t.

Consequently c1=(n_+-n_-)t and c2=(n_-+n_+)h t. The adjoint oriented
three-plane bundle has

    p1=c1²-4c2=-4(n_-+n_+)h t.

With Jin's generator alpha normalized by p1=+4, the comparison is
-(n_-+n_+)a. In particular it can alter k and ell by an arbitrary
common multiple of(1,4), but it leaves A unchanged. This fixes the
sign of this phase-loop convention as well as its divisibility.

Jin Theorem4.9, with g=1, identifies the mapping-torus map with the
homomorphism to Spin bordism over CP-infinity; its characteristic
coordinates are(A,k). The representatives a,b have coordinates
(0,1) and(1,8), respectively, as verified in P3F.3. For two returns
choose tubular connections that are constant on a common collar and
concatenate them. Their quotient replacements concatenate as the
actual diffeomorphisms f and g, so the replacement of the composite
is fg. Additivity of the cited bordism homomorphism gives
A(fg)=A(f)+A(g). The framing calculation proves that this remains
true for every separate choice of the tubular connections.

There is also a direct zero-class implication requiring no division
in a finite group: the kernel of A in the exact presentation
I(S2 timesS3)=Za direct-sum Zb is Za. P3F.4 constructs the Hopf lift
of every a-power and extends it over D4 timesS3. Together with the
pointwise cut-and-reglue identification P3F.8, it proves that the
actual clutched sphere of a return in this kernel is standard.
P3K.7--8 proves that the AC26 return belongs to this kernel, by two
computations through the actual trace. The integral framework here
then gives the reduction from six parameter loops to one.

## P3F.12. Proved: the compact fixed-sheet torsor and its line class

The central-node component cover of the actual partial parameter filling
is y^12=t^4/(t-1)^3. Its compact normalization C has genus3, with one
point above the cusp. The Jacobian after minimalization has one I12
fibre there. The affine defect of the actual fixed sheet around that
point is translation by6P: this is the first-coordinate part of
Delta_Q F=gamma-6delta in P2.2, with q=Q^12. We retain this defect in
the following argument; the component cover alone did not remove it.

Let Lambda_E be the source elliptic lattice on the complement of the
cusp of C. The original source matrices and cyclic-cover shifts are

    A=[[0,1],[-1,-1]], shift4;
    B=[[0,-1],[1,0]], shift-3.

The commutator belongs to the cover subgroup, and

    G=[A,B]=[[1,-1],[-1,2]],
    G-I=[[0,-1],[-1,1]], det(G-I)=-1.

Thus H0(C minus cusp;Lambda_E)=0 integrally. The program
compact_torsor.py prints this matrix, its determinant and Smith form;
root's independent full Schreier enumeration is in torsor_schreier.py.
For C0=C minus an open cusp disc, Poincare--Lefschetz duality with the
oriented local system identifies H²(C0,boundary;Lambda_E) with this
coinvariant group. The restriction H¹(C0;Lambda_E) to H¹(boundary;
Lambda_E) is therefore surjective, including its torsion. Gluing the
disc with the invariant-lattice extension j_*Lambda_E gives
H²(C,j_*Lambda_E)=0. Equivalently, the top compact-support cohomology
of the punctured curve is its integral coinvariant group; adding the
skyscraper of local invariant sections changes no degree-two group.

The local sheaf here has a concrete meaning. On an I_n Tate chart
with parameter Q, the multiplicative parameter is Q^n times a unit.
A translation in the identity component is multiplication of the
Tate coordinate by a nonzero smooth unit a(Q). It acts in every
resolved node chart by opposite unit multiplications; these formulas
extend across all components of the I_n fibre. Locally a(Q) has a
smooth logarithm. The kernel of this exponential consists of the
invariant integral period: the other period contains log Q and
cannot be a smooth single-valued section through Q=0. Hence, for the
sheaf A^0 of these extending identity-component translations, there
is an exact sequence

    0 -> j_*Lambda_E -> L_infty -> A^0 -> 0,

where L_infty is the sheaf of smooth sections of the extended complex
Lie line bundle, and is fine. This verifies the sheaf at the singular
fibre, rather than using the group law of the smooth fibres only.
The local defect6P is in this identity component: P has a nonzero
unit Tate coordinate at the original I1 fibre, and its pullback and
all its multiples have component zero in I12. Its local logarithm
therefore gives an extending translation.

It follows from the exact sequence and the vanishing just proved that
H¹(C,A^0)=0. The actual affine fixed sheet, after the chosen local I12
extension, has a smooth translation section. Its translations extend
through the fixed I12 resolution by the displayed unit formulas.
It is therefore smoothly isomorphic, over C and by translations, to
the sectioned Jacobian. This does not supply a holomorphic section or
a holomorphic parameter filling.

The circle line also needs comparison under this isomorphism. Its
fibrewise Picard point is P, and its multidegree on the components of
I12 is zero. The latter follows from the actual source line P-O:
both sections meet the identity component once, and neither meets
any other component. The unit translation used above preserves the
components and the fibrewise Picard point. Divide the transported
line by O(P'-O') on the Jacobian. On every smooth elliptic fibre this
quotient is holomorphically trivial, and at I12 its unit gluing has
product1 and multidegree zero. Thus it is trivial on that fibre too.

Here is the local see-saw construction in this situation. Normalize
a nonzero fibrewise holomorphic trivializing section at the zero
section. Away from the nodal value it varies smoothly: it is the
normalized one-dimensional kernel of the fibrewise Dolbeault
operator. At I12 the construction uses the actual multiplicative
unit charts: choose a frame on the first rational component and
continue across the successive node units eta_i. The continued
frame on the last component agrees with the first because
product eta_i=1. The units and their logarithms extend smoothly in Q,
so this normalized frame extends over the nodal charts. Two such
normalized local frames differ by a function of the base alone,
because a holomorphic function on a connected compact fibre is
constant. Their transition functions define a line bundle on C.
This proves, for the actual transported line, the equality

    c1(L)=c1(O(P'-O'))+n F       for an integer n.

It proves the required filtration statement via explicit normalized
frames. In particular it does not infer that equality merely from
triviality of the action on the associated graded of Leray.
Since F²=F.(P'-O')=0, its square is exactly-2. The smooth affine
comparison preserves orientation and signature, so p1 of the compact
sheet pairs to-24. The unspecified integer n records the permitted
boundary gauge and has no effect on either of these pairings.

## P3F.13. Exact angular clutch at the parameter corner

For the default twists let F(s,v) be the exact origin difference in
P2.2, and keep gamma(s,v)=(6mu,C-s-12v). Direct polynomial subtraction
gives, for real theta,

    F(s,v+theta)-F(s,v)
       = theta gamma(s,v)+6theta(1-theta)delta.       (P3F.13.1)

On a fixed-radius parameter circle, v=ib+theta. The final summand is
real in the delta direction. It is a unitary gauge, equal to1 after
exponentiation at both endpoints. It can be removed by a homotopy
of periodic gauges. The circle quotient of the origin comparison is
therefore exactly the gamma-translation loop, with all radial terms
independent of theta.

The base deck must still be retained. Since gamma(s+12,v)=
gamma(s,v)-12delta,

    [F(s+12,v+theta)-F(s+12,v)]
       -[F(s,v+theta)-F(s,v)]=-12theta delta.        (P3F.13.2)

Thus the two angular lifts differ on the Q deck by the unitary gauge
exp(-24pi i theta) in the exp(2pi i zeta2) convention, of winding-12.
This gauge is the integral clutch of the circle line. It does not
disappear on passing to the orbit: its degree is retained by the
principal circle bundle. compact_torsor.py checks both exact
identities and the endpoint values.

The normal-crossing chart suggested by the second Tate multiplier is
XY=Qr after q=Q^12, because q r^12=(Qr)^12. Its elementary small
resolution has charts

    X=Qz, r=zY;          Q=Xw, Y=wr.

At a node Q=uv of the resolved source I12 surface the remaining
chart uv=Xw is resolved by

    X=uk, v=kw;          u=Xk, w=kv.

These four-variable charts are smooth and separate the central fixed
surface from the fixed cusp trace. They give the local candidate for
an orbit bordism after deleting fixed tubes. The central fixed-sheet
normals have opposite weights and product trivial, so their positive
Hopf projectivization is a product S2 bundle with Euler class
u+c1(L). This inner boundary is nonspin when the compact sheet has
K=5F. The canonical quotient structure is spin^c with determinant
-K on that boundary; no claim that this compact product is spin is
made.

Historical scope of this complex corner attempt: its cyclic descent
and outer identification after resolving the source I12 charts were
not completed. P3F.13 proves the exact local clutch, including its
line gauge. The actual global application is now proved by the real
trace P3K.6--7, the analytic symbol comparison P3K.8, and the rotating
normal framing P3K.9. Those constructions retain the same clutch and
compute the original return without asserting this complex corner
completion.

## P3F.14. Proved: the characteristic formula for an actual fixed-sheet boundary

This is the general calculation for the explicitly specified Hopf
boundary. The earlier complex corner attempt did not supply a global
boundary identification; the actual real trace P3K.6--9 now supplies
the application and its complete orientation and line comparison. Let S be a compact
complex surface, and let L_+,L_- be its two complex normal lines of
circle weights+1,-1 in a stable complex eight-dimensional chart.
Write a=c1(L_+), b=c1(L_-), d=c1(TS). Its free normal-sphere quotient
is B=P(L_+ direct-sum conjugate(L_-)). Orient its sphere fibre so that
the circle Euler class x has integral1. Then

    pi_*(x)=1, pi_*(x²)=a-b,
    pi_*(x³)=a²-ab+b²,
    p1(TB)=pi^*(p1(TS)+(a+b)²).

These follow from the projective-bundle relation with roots a,-b.
The stable complex structure inherited from the original two opposite
weights has spin^c determinant D=pi^*(d+a+b). Indeed the associated
normal lines have opposite circle characters, so those characters
cancel in their determinant. The degree-six spin^c index polynomial
for this structure twisted by the circle line is

    integral_B exp(D/2) exp(x) Ahat(TB).

Substitution of the four displayed pushforwards gives exactly

    (3d²-p1(TS))/24 + (a²+ad)/2
       = chi(O_S)+(a²-a.K_S)/2
       = chi(S,L_+).

The equality on the right is the surface Riemann--Roch polynomial;
the calculation also proves that the negative-weight normal line b
cancels entirely. No spin structure on S or on B is required.
For an actual spin-six boundary with D=0 the same index polynomial is
(4x³-p1 x)/24, the integer A used in P3F.11.

For the compact fixed sheet of P3F.12, a=M+nF, chi(O)=1,
M²=-2, M.K=F²=M.F=0. Its index contribution is therefore0 for every
such fibre-supported shift. The fixed cusp curve has positive normal
line O(-1); its Dolbeault cohomology on P1 is zero in both degrees.
These are exact local index inputs. P3K.6--8 subsequently constructs
the actual real bordism and identifies its spin-c symbol. The
resulting return index therefore follows through that comparison;
no analytic corner completion is asserted.

## P3F.15. Proved: cyclic label and line-clutch identities

Here is the explicit descent on the rank-one node charts. Bounded
nonzero period units are harmless in these identities: choose their
logarithms on the cusp disc and split their twelfth roots in the
following multipliers. Put rho=Qr, zeta=exp(2pi i/12), eta=exp(pi i/12),
and index the node charts by i in Z, modulo the gamma period of length12:

    X_i=W/rho^i, Y_i=rho^(i+1)/W, X_i Y_i=rho.

The deck map on the dense torus is

    D:(Q,i,W)->(zeta Q,i-1,eta rho^(-1) W).

Consequently its formulas in the node charts are

    X'_(i-1)=eta zeta^(1-i) X_i,
    Y'_(i-1)=eta^(-1) zeta^i Y_i.

Their product is zeta rho, as required for the new parameter. Both
multipliers are units, so this map extends across each node and
preserves the opposite circle weights. It is free on the twelve node
labels even at Q=0. After twelve iterations the W multiplier is
eta^12 zeta^(-66) rho^(-12)=rho^(-12), since the two first factors
both equal-1. Accompany each step by the locally defined elliptic
translation-P/2; the twelfth step is-6P. Thus the twelfth iterate is
the inverse gamma period, including its source-translation part.
This proves descent on the labelled rank-one charts.

On a fixed-radius r-circle, each factor rho^(-1) has angular winding-1.
The twelve-step gauge has winding-12. It is exactly the winding in
(P3F.13.2), with the same W/exp(zeta2) sign conversion. This verifies
the integral circle-line clutch, not just the orbit action. It leaves the
outer contraction in the earlier complex corner attempt unproved.
The actual monodromy application is instead completed by the real
trace P3K.6--9.


Multiplicity check on the outstanding outer identification: a free
action on the twelve labels, with reduced divisor Q=0 on those charts,
would descend q=Q^12 to a divisor of multiplicity twelve. The actual
outer cusp for r nonzero has multiplicity one. Thus the labelled
fixed-sheet descent above cannot itself be its outer chart. A valid
comparison must explicitly account for the ramification or fixed
strata, or for a changed divisor multiplicity. The missing morphism
is therefore stronger than merely contracting the additional source
I12 exceptional curves.
