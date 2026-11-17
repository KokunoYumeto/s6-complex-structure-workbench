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
This calculation concerns the explicit compact elliptic pullback. It
does not yet identify its boundary modification with the page of a
threefold-family monodromy.

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
for the numerical pair ((-1,-4)): its oriented class is zero. The
remaining application to the AC26 family consists of an actual geometric
identification of the family's clutched sphere with this Hopf gluing,
and a derivation of the numerical pair from its charts. Neither is
supplied by the abstract classification theorem, and neither is claimed
to have been completed in this file.

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

For the family application the smallest undecided instance remains the
original ((3,4)\) sphere family: one must identify its positive parameter
return map, including the cusp collar, with a geometric representative
on the quotient model and evaluate the normal/relative characteristic
data. The direct images and full automorphism result in the independent
Part5 notes do not determine that isotopy class. The construction of
P3F.4 now supplies the explicit passage to an oriented standard sphere
for the classified pair ((-1,-4)\); it leaves the geometric evaluation
of that pair visible rather than assuming it.

Approaches pursued here are the exact rank-one table enumeration,
permutation-certified existence of every source, section-height and
component calculations, Jin's full integral classification in fixed
coordinates, explicit Hopf-lift extension over (D^4\times S^3\), and
Takase's corrected normal-Euler formula. The next geometric calculation
is the local-to-global comparison of the original toric cusp collar with
the Hopf-lift gluing. It must carry the phase of the linearization and
the finite logarithmic transformations, not only the fibre period
matrix.

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
value t* and leads to the second map. The four-dimensional page still
requires its separate construction, including its boundary surgeries.

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

The remaining numerical step in P3.1 is therefore exact: compute
k=integral_{M_f}x³ and ell=integral_{M_f}p1 x for this f, including the
finite-root and cusp collar contributions. Parent Statement P2.1
provides the actual sixfold descent

    H(t)delta, H(t)=-(4l1 log t+3l2 log(t-1))/(2pi i),

with cusp coefficient -p after carrying the collar integer l0. Its
circle quotient is a radial translation in the line-bundle direction.
The page/cap identification needed to turn that exact formula into
the values(-6,-24) for the sixth power has not yet been written. No
finite-group class is declared computed from that missing comparison.
