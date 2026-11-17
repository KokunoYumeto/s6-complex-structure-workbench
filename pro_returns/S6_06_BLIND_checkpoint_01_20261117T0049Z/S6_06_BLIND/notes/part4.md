# Part 4: independently derived results

Working source for the final paper. Statements P4.1--P4.8 below have proofs;
P4.9 records the still unresolved general irreducible case. All orientations
on complex spaces are complex orientations. All homology groups in the
example are integral. A meridian is counterclockwise in its local base
coordinate, including the coordinate 1/t at infinity. The common fibre
lattice is Λ = Z e1 + Z e2 + Z e3 + Z e4, in exactly the order of the prompt.

## P4.1 (Proved). The local analytic modification

Let E = C/(Z+iZ), q=exp(-2π), and identify E with C*/q^Z by
z↦exp(2πiz). Let B be a copy of E. Write π:V→B×Δ for the blowup at
(0,0), let R be its exceptional curve, and set L=O_V(R). The quotient
U=L^×/q^Z is a smooth complex threefold, and U→V→Δ is proper. Its
noncentral fibres are E×B, and its central fibre is the reduced union of
a primary Kodaira surface K and the scalar primary Hopf surface H_q,
meeting transversally in one elliptic curve.

**Proof.** Around the blown-up point take coordinates (z,t). The two
blowup charts are (u,v), with z=u and t=uv, and (r,s), with z=rs and
t=s. On their overlap r=1/v and s=uv. Frames for O(R) are u^{-1} and
s^{-1}, and the fibre coordinates satisfy λ_B=vλ_A. Quotienting either
nonzero fibre coordinate by multiplication by q gives a holomorphic
product chart with fibre E. The transitions are holomorphic translations
in E, so they define a smooth holomorphic principal E-bundle over V.
The scalar action is free and properly discontinuous: in each line-bundle
trivialization the logarithm of the absolute value of a nonzero fibre
coordinate is translated by the nonzero real number log q. Compact
subsets meet only finitely many translates. Thus the quotient is
Hausdorff. Local product charts with compact fibre E prove that U→V is
proper, and the blowup V→B×Δ and projection B×Δ→Δ are proper.

The canonical section of O(R) has coefficients u and s in these frames.
It has no zero over t≠0. Dividing λ_A by u, or λ_B by s, therefore
trivializes U over Δ*. This is the product trivialization required in the
question, not a choice of an unspecified topological marking.

The central divisor in V is B'∪R, with B' the strict transform of B×{0}.
In the first chart it is uv=0. The intersection numbers are R²=-1 and
R·B'=1. Consequently L|R=O_P1(-1), and L|B' has degree +1. The
principal E-bundle (L|B')^×/q^Z has trivial relative canonical bundle,
base an elliptic curve, and primitive nonzero circle Chern class. Its
universal-cover presentation is the usual primary Kodaira presentation;
equivalently it is a principal elliptic bundle over an elliptic curve
with primitive nonzero Chern vector. Its canonical bundle is trivial
(the base differential and dλ/λ give a nowhere-zero two-form), and the
circle-bundle computation below gives b1=3. This identifies K as a
primary Kodaira surface by BHPV VI.1.1, Table 10.

The tautological evaluation map O_P1(-1)^×→C²\{0} is a biholomorphism:
a nonzero vector determines its line. It intertwines fibrewise scalar
multiplication by q with scalar multiplication on C². Thus the second
component is H_q=(C²\{0})/q^Z. Over the unique point B'∩R the two
components meet in E. In product coordinates on U the map is still
(u,v,c)↦uv, so this intersection is transverse and has multiplicity one.
There are no other singular points of the map. ∎

## P4.2 (Proved). Global charts, compactness, and monodromy

The three indicated markings and the indicated principal-bundle clutch
produce a smooth compact complex threefold Y with a proper holomorphic
map f:Y→P¹, connected fibres, and precisely the three reduced
normal-crossings fibres described in P4.1. The homological monodromy on
H1 of a smooth fibre is the identity.

**Proof.** The map ℓ(t)=(log t)/(2πi) modulo Z+iZ is a single-valued
holomorphic map from an annulus to E: a change of logarithm adds an
integer. Thus a_out=a_in+(ℓ(t),0) is a holomorphic transition between
trivial A-bundles. It defines a Hausdorff holomorphic principal A-bundle
Y0 over P¹, and compactness follows from local triviality and compact
base and fibre. Choose disjoint coordinate discs around 0,1,∞. In each
disc replace A×Δ with the U of P4.1 using the specified factorization
A=C_i×B_i and the canonical trivialization over Δ*.

The factorization maps C_i×B_i→A are respectively
(z,w)↦(w,z), (z,w)↦(iz,iz+w), and (z,w)↦(z,iz+w).
Each is a holomorphic group isomorphism. Its lattice matrix is S_i
below, of determinant +1. These formulas, the transition λ_B=vλ_A,
and the original transition ℓ give all the gluing maps. Points over
different base points are separated in the base. Points over a fixed
base point lie in a single Hausdorff local model; this proves
Hausdorffness of the glued space. Properness is local on the base and
holds for the old bundle and for each U. Hence Y is compact.

Every central component map to its base curve has connected elliptic
fibres, and the two components meet. All other fibres equal A. The
charts uv=t show that the only critical fibres occur at the three
specified values. The product trivialization over each punctured disc
identifies every smooth fibre with the same A. The remaining global
transition is a translation in A; translations induce the identity on
H1(A;Z). Therefore the representation π1(P¹\{0,1,∞})→GL(Λ) is the
identity. ∎

## P4.3 (Proved). Local chain complexes and attaching maps

In local coordinates write the lattice of C_i×B_i as (a,c,b,d), with
a the image of the cycle 1 in C_i and c the image of i. The inclusion
of a regular fibre A into U induces

    H1(A)=Λ → H1(U)=Λ/Za,
    H2(A)=∧²Λ → H2(U)=∧²Λ/Z(a∧c).

Both maps are the indicated quotient maps; both target groups are free.
The meridian and its products with the four fibre one-cycles have zero
image in H1(U) and H2(U), respectively.

**Proof.** A Hermitian metric on L gives a diffeomorphism
L^×/q^Z ≅ S(L)×S¹_c. The two factors are the unit-circle bundle and
the logarithm of the norm modulo log q. The base V has the homotopy
type B∨S². One may choose the B summand to be the regular fibre B_t,
t≠0, and the S² summand to be R, joining their base points by a path.
For completeness, blowing up a four-ball replaces it by the disc
bundle of O(-1); on the boundary the attaching map is the Hopf map.
The complement of the four-ball in B×Δ has homotopy type B∨S³,
and its boundary sphere gives the S³ summand (the map to B is null
because π3(B)=0). The homotopy pushout therefore has type B∨S².
This also follows on universal covers: the replacement adds one
two-sphere at each lift of the blown-up point, and adds no other
homology; the comparison induces an isomorphism on π1 and on the
homology of the simply connected covers, hence is a homotopy
equivalence.

The circle Chern class evaluates to zero on B_t and to -1 on R.
Consequently its total space has the homotopy-pushout model
T³_(a,b,d) ← S¹_a → S³, with the second map the inclusion of a
Hopf fibre. This second map is nullhomotopic. Its homotopy pushout
has the homotopy type (T³∪_a D²)∨S³. Multiplication by S¹_c
gives the following integral cellular chain complex for U. Start with
the exterior-cell complex of T⁴ in the order (a,c,b,d), whose
differentials vanish. Add cells r of dimension 2, rc and h of
dimension 3, and hc of dimension 4. The only nonzero differentials are

    ∂r=a,                  ∂(rc)=a∧c.

The sign of r is chosen to make ∂r=a; this fixes the sign of rc.
All entries of these differentials are 0 or 1. The resulting free
homology ranks are (1,3,5,5,2), and the two displayed quotient maps
follow directly from the inclusion of the torus subcomplex.

For the meridian, choose a point of B different from 0. Its product
with the disc avoids R, and the canonical section trivializes L there,
so the meridian bounds. A generator b or d of H1(B) can likewise be
represented by a loop avoiding 0; its product with the disc, lifted
by the same trivialization, bounds the product with the meridian.
The cycles a and c are treated over one fixed point of B\{0}.
Thus every fibre one-cycle times the meridian has zero homology
class in U. ∎

The matrices S_i, whose columns are (a_i,c_i,b_i,d_i) in the common
basis, are

    S1 = [[0,0,1,0], [0,0,0,1], [1,0,0,0], [0,1,0,0]],
    S2 = [[0,-1,0,0], [1,0,0,0], [0,-1,1,0], [1,0,0,1]],
    S3 = [[1,0,0,0], [0,1,0,0], [0,-1,1,0], [1,0,0,1]].

Let Q_i=S_i^{-1}. The matrix R1_i is Q_i with its first row
deleted. Let ∧²Q_i have ordered row and column indices
(ac,ab,ad,cb,cd,bd) and (12,13,14,23,24,34), respectively.
Deleting its first row gives R2_i. This specifies every entry of every
local map. The program prints these matrices explicitly and writes
them to `code/part4/example_matrices.json`.

## P4.4 (Proved). Integral global H1 and H2

The indicated Y has H1(Y;Z)=H2(Y;Z)=0. Its fundamental group is
also trivial.

**Proof.** Let P be the complement of three small open base discs and
W=f^{-1}(P). The bundle is trivial over P, so W=A×P. Let s1,s2
generate H1(P) and put s3=-s1-s2. The three overlaps are
N_i=A×S¹. The original principal-bundle clutch contributes +e1 to
the first meridian, because continuation of ℓ around t=0 adds +1.
Thus, with g1=e1, g2=g3=0 and v1=(1,0), v2=(0,1),
v3=(-1,-1), their maps into W are

    x ↦ x,          s_i ↦ g_i + v_i.

In degree two the maps are

    x∧y ↦ x∧y,      x∧s_i ↦ x∧g_i + x⊗v_i.

These follow either from products of the represented cycles or from
the classifying maps to the aspherical space A×P. In particular the
clutch contribution in degree two is retained.

Order H1(W) as (e1,e2,e3,e4,s1,s2), and append the three ordered
local groups (c_i,b_i,d_i). On the source use three consecutive
blocks (e1,e2,e3,e4,s_i). The Mayer--Vietoris map F1 is the
15×15 integer matrix with block i having upper block

    [[I4, g_i], [0_(2×4), v_i]]

and lower block -R1_i in the i-th local summand and zero in the
other local summands. These blocks have respectively six and nine
rows. The complete matrix is printed in the attached output. Its
determinant is -1.

Order H2(W) as (12,13,14,23,24,34,e1s1,...,e4s1,e1s2,...,e4s2),
and append the three five-dimensional local H2 groups. On the source
use three blocks (12,13,14,23,24,34,e1s_i,...,e4s_i). The map F2
is the 29×30 matrix whose i-th ten-column block has top six rows
[I6, (e_j∧g_i)_{j=1}^4], next eight rows [0, I4⊗v_i] in the
displayed base order, and local rows [-R2_i,0] in summand i.
All other local rows are zero. This is a full integer specification,
not merely a rank statement; the code emits all entries.

The degree-zero map is

    F0 = [[1,1,1],[-1,0,0],[0,-1,0],[0,0,-1]].

Its kernel is zero. Hence the low-degree Mayer--Vietoris sequence is

    Z^30 --F2--> Z^29 → H2(Y) → Z^15 --F1--> Z^15
                         → H1(Y) → Z^3 --F0--> Z^4.

The calculation can be checked without row-reduction software.
Eliminating the three local H1 groups and the two independent base
meridians leaves Λ modulo e1,a1,a2,a3. Their relation matrix is

    [[1,0,0,1], [0,0,1,0], [0,1,0,0], [0,0,1,1]],

whose determinant is -1. Thus F1 is an integral isomorphism.

For H2, the ∧²Λ columns eliminate the fifteen local generators and
leave the relations η_i=a_i∧c_i. The i=2 meridian columns kill
Λ⊗s2; the i=3 columns then kill Λ⊗s1; the i=1 columns leave
e1∧Λ. The resulting six relations, in the basis
(12,13,14,23,24,34), form the matrix

    [[1,0,0,0,1,1],
     [0,1,0,0,0,-1],
     [0,0,1,0,1,0],
     [0,0,0,0,-1,0],
     [0,0,0,0,0,-1],
     [0,0,0,1,1,1]].

Its determinant is +1. This proves surjectivity of F2 over Z,
including the absence of torsion. The attached independent Smith
normal-form calculation gives fifteen unit factors for F1 and
twenty-nine unit factors for F2.

For π1, the local pushout in P4.3 gives π1(U_i)=Λ/Za_i,
with meridian trivial. The group π1(W)=Λ×F(s1,s2), and the overlap
maps impose a1=a2=a3=0, s1+e1=0, s2=0,
and s1+s2=0. Thus both base generators and e1 vanish, and the
same four-column unimodular relation matrix kills Λ. Van Kampen
therefore gives π1(Y)=1. ∎

## P4.5 (Proved). Algebraic dimension and characteristic numbers

For this example a(Y)=1, c3[Y]=χ_top(Y)=0, and b3(Y)=2. Its full
integral homology is free with ranks (1,0,0,2,0,0,1).

**Proof.** Every smooth fibre has Euler number zero. Each special
support is K∪_E H_q. Both K and H_q are elliptic bundles over
compact curves, so their Euler numbers are zero, as is that of E.
Additivity gives χ(K∪_E H_q)=0. A finite stratification of the base
and multiplicativity on the smooth bundle therefore give χ(Y)=0.
The Euler class of the real tangent bundle underlying a complex
rank-three bundle is c3, with the complex orientation, so c3[Y]=0.
Poincaré duality and P4.4 give b4=b5=0 and χ(Y)=2-b3, hence b3=2.
The universal-coefficient theorem and duality also show H3 has no
torsion: its torsion equals that of H2. The other groups have already
been computed.

The universal-coefficient theorem gives H²(Y;Z)=0. A horizontal
effective divisor D would restrict to a nonzero effective divisor on
a general smooth fibre A. Its first Chern class there is the restriction
of c1(O_Y(D)), hence zero. For a Kähler form ω on A, however,
the integral of ω over a nonzero effective divisor is positive and
equals the cup-product pairing with this first Chern class. This is
a contradiction. Thus every divisor on Y is vertical. In particular
the polar divisor of a meromorphic function is vertical, and the
function restricts to a holomorphic, hence constant, function on a
general compact fibre. It descends over the smooth part of the base
by local holomorphic sections. Near an exceptional base value,
multiplication by a sufficiently high power of the base coordinate
removes the vertical poles; connected fibres imply that the resulting
holomorphic function descends as well. The descended function is
therefore meromorphic on P¹. Hence C(Y)=f^*C(P¹), of transcendence
degree one. ∎

## P4.6 (Proved). Euler number of a normal-crossings divisor

Let X be a compact complex threefold with b2(X)=0. Let F be a
reduced compact normal-crossings divisor, allowing branches of one
global irreducible component to meet each other. Write T(F) for the
number of its ordinary triple points. Then

                         χ_top(F)=T(F),

and T(F) is even. This assertion concerns the reduced support and
does not impose equal multiplicities on a fibre having support F.

**Proof.** Put S=⊔S_i for the normalization of F and let ν:S→X
be its holomorphic normalization immersion. Let D_i be the conductor
divisor on S_i, including all other local branches of F. Since F has
normal crossings, S_i is smooth, D_i is a nodal reduced divisor,
and the quotient N_i=ν_i^*T_X/T_{S_i} is a line bundle. The
differential of a local equation of F identifies

    N_i = ν_i^*O_X(F) ⊗ O_{S_i}(-D_i).

This equality can be checked in a chart x1...xk=0: on the branch
x1=0 the normal derivative is x2...xk, whose zero divisor is D_i.
All comparison maps here are holomorphic vector-bundle maps; in
particular no embeddedness of S_i in X is asserted.

Because b2(X)=0, c1(T_X) and c1(O_X(F)) vanish in real
cohomology. Poincaré duality gives b4(X)=0, so c2(T_X) vanishes
as well. The tangent exact sequence therefore gives

    c1(K_{S_i})=-[D_i],       c2(S_i)=c1(K_{S_i})².

Write a=Σ_i χ(S_i,O_{S_i}). The surface Riemann--Roch
(Noether) formula gives Σ e(S_i)=6a.

Let Γ be the normalization of the double-curve locus of F, with
one sheet for each unordered pair of local branches. The
normalization of ⊔D_i is an unramified degree-two cover of Γ:
it records which of the two branches is selected. Each triple point
contributes three nodes to ⊔D_i. Adjunction on each S_i gives
χ(D_i,O_{D_i})=-D_i·(D_i+K_{S_i})/2=0. Normalizing these
nodal curves therefore gives

                0=2χ(Γ,O_Γ)-3T(F)=e(Γ)-3T(F).

The normalization complex for F is locally the alternating
restriction complex for the coordinate hyperplanes. It is exact.
When branches are permuted globally, its double-curve term is
O_Γ tensored with the sign line of the two-sheeted branch cover;
this line has order at most two and degree zero on every component,
so its coherent Euler characteristic equals χ(Γ,O_Γ). The
triple-point term has length one at each triple point. Thus

    χ(F,O_F)=a-χ(Γ,O_Γ)+T(F)=a-T(F)/2.

The sequence 0→O_X(-F)→O_X→O_F→0 and analytic
Hirzebruch--Riemann--Roch give χ(F,O_F)=0: the Chern characters
of O_X(-F) and O_X agree in rational cohomology. Consequently
T(F)=2a. Ordinary Euler additivity, checked stalkwise at a single,
double, or triple point, gives

    e(F)=Σe(S_i)-e(Γ)+T(F)=6a-2T(F)=T(F).

The same equality also proves that T(F) is even. Nothing in this
argument uses the scheme multiplicities of a fibre or a base change. ∎

## P4.7 (Proved). The numerical sign theorem in the NC class

Let f:X→B be a proper surjective holomorphic map with connected
fibres from a compact complex threefold with b1(X)=b2(X)=0 to a
smooth compact curve, and let every reduced fibre support have
normal crossings. Then B=P¹,

    c3[X]=Σ_b T((f^{-1}(b))_red) ∈ {0,2},
    b3(X)=2-c3[X].

The torus hypothesis is unnecessary for these numerical conclusions
in this class.

**Proof.** The beginning of the Leray sequence for the constant real
sheaf, using f_*R=R because the fibres are connected, injects
H¹(B;R) into H¹(X;R). Thus B has genus zero. A smooth fibre G
has trivial normal line bundle, and the tangent sequence gives
c2(G)=c2(X)|G=0; hence e(G)=0, with no assumption on the
biholomorphic type of G. The set of critical values is finite.
Over its complement Ehresmann's theorem gives a smooth bundle.
Euler additivity and P4.6 now give the displayed sum of triple-point
counts. Poincaré duality gives e(X)=2-b3(X). The cup pairing on
H³(X;R) is nondegenerate and alternating, so b3 is even.
Nonnegativity of the sum completes the proof. ∎

## P4.8 (Proved in the NC class). Normalizations and the equality case

For a torus fibration as in P4.7, every irreducible singular support
with rational normalization has Euler number 2. Every other
irreducible support has Euler number zero. In the zero case, the
normalizations and gluings have precisely the forms named in the
prompt within the NC category: smooth supports with finite
unramified torus covers; singular irreducible supports with smooth
minimal elliptic-ruled or Hopf normalization; and reducible supports
whose normalization components are smooth minimal Hopf or
non-Kähler elliptic surfaces, glued through finite unramified maps
of smooth elliptic curves.

**Proof.** We use the verified classification statement BHPV VI.1.1
and Table 10 (publisher preview pp. 243--244), OVV Theorems 4.2
and 5.1, and the verified class-VII theorem described below. The
hypotheses of these surface statements apply to the compact smooth
normalization components S_i. The comparison ν_i is the
normalization immersion used in P4.6; its exact tangent sequence
has already established e(S_i)=K_{S_i}².

For a component with nonempty conductor, a Kähler form ω would
give K_{S_i}·ω=-D_i·ω<0. Every pluricanonical section has an
effective zero divisor, so this inequality implies Kodaira dimension
-∞. The classification then makes S_i rational or ruled. For a
ruled surface over a curve of genus g, followed by k blowups,
e=4(1-g)+k and K²=8(1-g)-k. Their equality gives
k=2(1-g). Thus g≤1; at g=1, k=0. Rational components have
χ(O)=1 and e=6, whether their minimal model is P² or a
Hirzebruch surface. A non-Kähler minimal model is elliptic or
class VII by OVV Theorem 5.1. A minimal elliptic model has only
smooth elliptic reduced fibres by Theorem 4.2, hence e=K²=0.
A class-VII model has b1=1 and p_g=0, so χ(O)=0 and K²=-e.
Blowups preserve χ(O) and change e,K² by +1,-1. In all
non-Kähler cases e=K² therefore forces e=0 and minimality.
The class-VII case has b2=0. Its finite étale Hopf/Inoue cover
comes from Buonerba--Bogomolov--Kurnosov Theorem 1. The
presence of the nonempty conductor excludes the Inoue case;
Inoue's covering families have no compact curves (Inoue 1972,
Propositions 1(i) and 2(i), pp. 445--446); the minus family has
the corresponding plus family as its unramified double cover (Khaled--Teleman 2026, Theorem 3.1 and the proof of Remark 3.4, pp. 303, 305).
A finite étale quotient of
a Hopf surface has universal cover C²\{0}, so is a Hopf surface
by definition.

Every conductor curve on a minimal elliptic non-Kähler component
is vertical: a horizontal curve would pair positively with a regular
elliptic fibre, which is homologically zero (OVV Theorem 4.2).
Thus it is a smooth elliptic curve. On a Hopf surface the compact
curves are smooth elliptic curves. These facts also follow here
numerically once T=0: adjunction to a conductor component C gives
2g(C)-2=(K+D)·C=0 because the other conductor components
are disjoint.

In an irreducible singular fibre there is one normalization component.
P4.6 gives T=2χ(O_{S_1}), hence 2 in the rational case and zero
in the elliptic-ruled or non-Kähler case. The global bound in P4.7
is consistent with, and also bounds, each such contribution.

For a reducible connected fibre, each normalization component meets
another global irreducible component. The pullback of that other
component's divisor to S_i is a nonzero effective divisor with zero
real Chern class, since b2(X)=0. A Kähler normalization would
pair it positively with a Kähler form, a contradiction. Hence all
normalizations are non-Kähler, have χ(O)=0, and T=0. There
are no triple points; every double curve is smooth elliptic by
adjunction. The branch maps are unramified, exactly as in P4.6.

A smooth reduced support G of a multiple fibre mG is covered by
the central fibre of the normalized cyclic base change t=u^m.
Locally the original map is t=z^m times a holomorphic unit;
extracting its root produces m smooth charts. Their gluing shows
that the map from the new central fibre to G is unramified and
finite. The new map is a proper submersion near the central fibre,
and its nearby fibres are the original tori. Catanese, *Deformation
in the large of some complex manifolds, I*, Theorem 2.1 (Annali
di Matematica 183 (2004), 261--289), states that every deformation
of an n-dimensional complex torus is an n-dimensional complex
torus. Its definition of deformation is precisely a proper
holomorphic submersion over a connected disk, with no Kähler
assumption on the total space. Those hypotheses hold for this
normalized base change, so the central fibre is a torus. The
nearby fibres are connected; Ehresmann's theorem therefore also
shows that the central fibre is connected. ∎

The Catanese source, including the proof of Theorem 2.7 from which
Theorem 2.1 follows, has been opened and checked at
https://www.mathe8.uni-bayreuth.de/de/team/prof-fabrizio-catanese-old/pdf/085.pdf.
Inoue's original propositions have been opened at
https://www.jstage.jst.go.jp/article/pjab1945/48/7/48_7_445/_pdf.

There is one further exclusion in the irreducible case: P4.12 below
proves that ω_G is torsion for every irreducible support, including
singular ones. Thus K_{S_1}+D_1 is torsion in the NC case. A nonempty
D_1 makes every positive plurigenus of S_1 vanish: a nonzero
pluricanonical section, multiplied by the effective conductor section,
would give a nonconstant vanishing section of a torsion line bundle;
a sufficiently high power would be a holomorphic function on a compact
connected surface with a zero. This is impossible. Consequently its
non-Kähler minimal model is class VII; the elliptic alternatives with
nonnegative Kodaira dimension cannot occur for an irreducible support.
The reducible case retains the non-Kähler elliptic alternatives already
listed above.

## P4.9 (Open at this working stage). Arbitrary irreducible singular supports

The arguments above prove the complete numerical sign statement for
normal-crossings supports, with no uniform-multiplicity assumption.
They have not yet proved it for a non-NC irreducible support. The
normalization of such a support may be singular and its normalization
map may fail to be an immersion. Therefore the vector-bundle
sequence used in P4.6, and the nodal conductor count used there,
cannot be transferred without additional local terms.

We have checked CDP 2020, sections 4--7, including Lemma 4.6,
Proposition 4.7, Proposition 4.11, and the proof of Proposition 7.3.
Their integral low-cohomology hypotheses are stronger than the
rational hypotheses here, and their final argument uses the
disputed global restriction result. We have not used those final
vanishings as a proof of the desired sign theorem. Kamenova's
Theorem 3.1 was opened and checked; it requires a semistable
Kähler total space with trivial canonical bundle, and does not
supply the missing comparison for the present arbitrary family.

The exact remaining local problem is to control the Euler
contribution of the nonimmersive normalization and its nonnodal
conductor, or to prove a replacement positivity statement for such
irreducible torus degenerations. No failure of an attempted proof
is reported as a counterexample.

P4.12 below advances this problem: every normal irreducible support
is smooth, and every singular irreducible support has a normalization
whose minimal resolved model is rational, irrational ruled, or class
VII. The remaining work is specifically the nonnormal case and its
conductor, not normal isolated surface singularities.

## P4.10 (Proved). Dropping b2=0: an explicit Euler-number-24 example

There is a smooth projective threefold Z with b1(Z)=0 and a connected
torus fibration Z→P¹ whose reduced special fibres are irreducible and
normal crossings, but c3[Z]=24. Thus b2=0 cannot be omitted, even in
the intersection of the irreducible-fibre and normal-crossings classes.

**Construction and proof.** On the two standard affine charts of P¹,
with coordinates t and s=t^{-1}, use the projective cubics

    y²z=x³-3xz²+t⁶z³,
    y_∞²z=x_∞³-3s⁴x_∞z²+z³,

glued by x_∞=s²x, y_∞=s³y. Equivalently these are the Weierstrass
cubics for the line bundle O_P¹(1), in the projective plane bundle
P(O plus O(2) plus O(3)). Let π:S→P¹ denote this elliptic surface,
with zero section [x:y:z]=[0:1:0]. The discriminant is a nonzero
constant times t¹²-4 on the first chart and 1-4s¹² on the second.
Its twelve zeros are simple, and infinity is smooth. At a discriminant
zero, x³-3x+t⁶ has a double root x=1 or x=-1 and a distinct third
root. The fibre therefore has an ordinary node. The derivative of
t⁶ is nonzero there, so the total surface is smooth. The zero section
is also a smooth point of every cubic (the derivative with respect to
z at [0:1:0] is nonzero). The local map at a node is consequently
xy=t after holomorphic coordinates and a translation of the base.

The relative dualizing differential dx/y has the transitions of
π^*O(1); it generates the dualizing sheaf also at nodal fibres.
Thus ω_S=π^*O(-1). Relative duality gives R¹π_*O_S=O(-1),
where π_*O_S=O because the cubic fibres are connected. Leray then
gives h¹(S,O_S)=0, and ω_S has no positive tensor power with a
section. The verified surface-classification theorem BHPV VI.1.1
therefore makes S a rational surface: the ruled alternative has
base genus h¹(O_S)=0. In particular π1(S)=0, since the minimal
rational models P² and the Hirzebruch surfaces are simply connected
and blowing up a point preserves the fundamental group.

Form W=S×_P¹ S. It is projective and has exactly twelve singular
points. They occur when both factors are the node of the same
singular cubic. Their equations are

    xy=uv,

with f=xy=uv. Let Δ_S⊂W be the diagonal and blow up its coherent
ideal. Away from the twelve singular points this divisor is Cartier,
so the blowup is the identity. At a singular point put
r=x-u and h=y-v. The equation becomes r y+u h=0 and the diagonal
ideal is (r,h). The blowup has the two smooth charts

    h=a r, y=-a u, x=u+r,       f=-a u x,
    r=b h, u=-b y, x=-b v,      f=-b y v.

In the first chart (a,u,x) are coordinates, and in the second
(b,y,v) are coordinates. The exceptional fibre is P¹; the chart
parameters satisfy b=a^{-1}. Thus the blowup Z is smooth and
projective. The displayed equations show that its special fibres
are reduced normal-crossings surfaces. Each remains irreducible:
the original product of two irreducible nodal cubics is irreducible,
and the exceptional locus has dimension one, so cannot create a
new surface component. Its normalization is rational, as is also
seen by taking the birational map from P¹×P¹.

The Euler number of a nodal cubic is 2-1=1. Its self-product has
Euler number 1. The resolution replaces its one conifold point by
P¹, so each resolved special fibre has Euler number 1-1+2=2.
Every other fibre is E_t×E_t, with Euler number zero. Additivity
therefore gives e(Z)=12·2=24 and c3[Z]=24.

For completeness π1(Z)=0, without a genericity assumption on the
twelve simultaneous singular values. Let U be the inverse image of
their complement. Any loop in the smooth Z can be moved off these
divisors by transversality, so π1(U)→π1(Z) is surjective. The
bundle U→P¹ minus twelve points has fibre E×E and a section. The
section extends over P¹ in Z, so all base generators become trivial;
π1(Z) is generated by the image of π1(E×E). The maps

    S→Z, p↦(p,O(π(p))),       S→Z, p↦(O(π(p)),p)

are well-defined because their images avoid every conifold point.
They extend the two factor inclusions of E into E×E. Since S is
simply connected, both factors of π1(E×E) die in π1(Z). Hence
π1(Z)=0 and b1(Z)=0. Finally a projective Kähler class is nonzero
in H²(Z;R), since its cube has positive integral. Thus b2(Z)>0,
identifying the precise omitted hypothesis. ∎

The executed exact checks are `code/part4/necessity_examples.py`
and `.out`. They verify the discriminant degree and squarefreeness,
the two resolution substitutions and the Euler count 24.

## P4.11 (Proved). Dropping the torus condition changes the equality case

There is a smooth compact complex threefold C with b1(C)=b2(C)=0,
e(C)=0, and a holomorphic submersion C→P¹ all of whose fibres are
primary Hopf surfaces. None has a finite unramified torus cover.
Consequently the torus assumption is necessary for the equality
classification as worded in the prompt. P4.7 proves that it is
unnecessary for the numerical sign theorem with NC supports, so a
counterexample to that numerical assertion cannot be supplied.

**Construction and proof.** On

    V=(C² minus {0})×(C² minus {0})

let the additive group C act by

    τ·(z,w)=(e^τ z,e^{iτ}w).

Writing τ=a+ib, the logarithms of the two Euclidean norms change
by a and -b. Thus the action is free. It is proper: if both a point
and its translate range over fixed compact subsets of V, then the
ratios of the two positive norms bound a and b. Every orbit has a
unique representative with ||z||=||w||=1, obtained by

    a=-log||z||,      b=log||w||.

This gives an explicit smooth diffeomorphism C=V/C≅S³×S³ and
proves compactness. Holomorphic local slices, for example z_j=1
after taking a local logarithm of z_j, furnish the complex quotient
charts. The transverse residual transition is holomorphic, so C is
a smooth compact complex threefold. The product CW complex of two
3-spheres gives integral homology free of ranks
(1,0,0,2,0,0,1), in particular b1=b2=0 and e=0.

The map [z,w]↦[z1:z2] is invariant under the action and gives a
holomorphic submersion to P¹. In an affine base chart choose the
representative z=λ(1,ξ). Quotienting the λ coordinate sets λ=1;
the choices of logarithm differ by τ=2πik, and change w by
e^{-2πk}. Thus the fibre and its local bundle trivialization are
explicitly

    H=(C² minus {0})/⟨w↦e^{-2π}w⟩.

The universal cover C² minus {0} retracts onto S³ and is simply
connected, so π1(H)=Z. A connected finite unramified cover by a
two-torus would inject its π1=Z⁴ as a finite-index subgroup of Z.
Every subgroup of Z is cyclic, while Z⁴ is not: their abelian
group ranks differ. This proves the failure of the smooth-support
equality classification by its exact covering morphism. ∎

## P4.12 (Proved). Canonical torsion and exclusion of normal singular supports

In the setting of Part 4.2, let f^{-1}(b)=mS be a fibre with
irreducible reduced support. Then ω_S^m is trivial,
χ(S,O_S)=0, and h¹(S,O_S) is either 1 or 2. Every normal such S
is smooth. For a singular (therefore nonnormal) S, a minimal resolved
model of its normalization has Kodaira dimension -∞.

**Canonical torsion.** Choose a disk Δ containing no other critical
value, with coordinate t vanishing at b, and U=f^{-1}(Δ). The
coherent direct image f_*ω_U is torsion-free of rank one: multiplication
by a nonzero holomorphic function on Δ is injective on sections, and
the canonical space of every nearby torus is one-dimensional. Thus
f_*ω_U is a line bundle on Δ. A generator gives a nonzero section
v of ω_U. On every noncentral fibre it has no zeros, because its
restriction is a nonzero torus volume form (times the base differential).
It follows that div(v)=aS for an integer a≥0. If a≥m, division by
t would give another holomorphic section, contradicting that v is
a generator of the direct image at 0. Hence 0≤a<m and

    ω_U≅O_U(aS),             O_U(mS)≅O_U.

Adjunction gives ω_S≅O_U((a+1)S)|S, hence ω_S^m≅O_S.
The ambient Riemann--Roch calculation in P4.6, applied to S,
gives χ(O_S)=0. Since S is reduced and irreducible, h⁰(O_S)=1.
A torsion line bundle on a compact reduced irreducible space has
at most one independent section: a nonzero section has a power
equal to a nonzero constant, and therefore is nowhere zero.
Serre duality for the Gorenstein surface S consequently gives
h²(O_S)=h⁰(ω_S)∈{0,1}, and h¹(O_S)=1+h⁰(ω_S).

**A resolution fact with its numerical proof.** For a minimal
resolution π:T→S of a normal Gorenstein surface, write

    K_T=π^*K_S+Σ a_j E_j.

Its exceptional intersection matrix M has nonnegative off-diagonal
entries and is negative definite. Here is the local argument, so
the algebraic hypothesis of Mumford's original presentation is not
being imported. Pull back a generic holomorphic function vanishing
at the contracted point. Its divisor is H+Σm_jE_j with m_j>0;
H is the strict transform. Intersecting with E_j gives M m≤0,
strictly in at least one entry of each connected exceptional block.
After scaling by the diagonal matrix diag(m_j), the negative
quadratic form is a sum of terms

    c_ij (z_i-z_j)²  and  d_i z_i²,      c_ij,d_i≥0,

with connected support and at least one positive d_i. It is positive
definite. This is the elementary proof recorded in Mumford 1961,
§I, p.6 (an unnumbered assertion, not a numbered theorem).

For each E_j, adjunction gives
K_T·E_j=2p_a(E_j)-2-E_j²≥0. The only possible negative case
would be a smooth rational (-1)-curve, excluded by minimality.
The inverse of a negative definite matrix with nonnegative
off-diagonal entries has nonpositive entries: with Q=-M, choose
c larger than every eigenvalue and diagonal entry of Q; then
Q^{-1}=c^{-1}Σ_{k≥0}(I-Q/c)^k is entrywise nonnegative.
The discrepancy equations M a=(K_T·E_j)_j therefore give a_j≤0.
Thus K_T=π^*K_S-E with an effective exceptional integral divisor E.

Put p=dim H⁰(S,R¹π_*O_T). The Leray sequence and the fact
that this sheaf is supported at finitely many points give

    χ(O_T)=χ(O_S)-p=-p.                         (12.1)

The higher direct images R²π_*I_Z vanish for every coherent ideal
I_Z, since all fibres of π have dimension at most one. The exact
sequence for an effective exceptional cycle Z therefore gives a
surjection

    R¹π_*O_T -> R¹π_*O_Z.                       (12.2)

In particular p≥h¹(Z,O_Z).

**Normal supports.** Suppose first E=0. Then K_T is torsion.
It has no exceptional (-1)-curve, and the surface classification
gives Kodaira dimension zero. Its possible holomorphic Euler
characteristics are nonnegative. Equation (12.1) forces p=0 and
χ(O_T)=0. The remaining surfaces are tori, bielliptic surfaces,
or Kodaira surfaces. They have no rational curves: tori have no
nonconstant maps from P¹, bielliptic surfaces have finite unramified
torus covers, and primary Kodaira surfaces have elliptic fibrations
with smooth elliptic reduced fibres over an elliptic curve. A map
from P¹ to a secondary Kodaira surface lifts to its finite unramified
primary Kodaira cover, so those also have no rational curves.
A negative curve on a surface with torsion K is,
by adjunction, a smooth rational (-2)-curve. Thus T has no
exceptional curves and S is smooth.

Now suppose E≠0. The torsion relation K_T+E=π^*K_S makes
every plurigenus vanish, so T is rational, ruled, or a blowup of
a class-VII surface. Rational T is impossible by (12.1), since
χ(O_T)=1. In the class-VII case χ(O_T)=0 and p=0. But

    χ(O_E)=-E·(E+K_T)/2=0.

Since E is a nonempty effective compact divisor, h⁰(O_E)≥1 and
h¹(O_E)=h⁰(O_E)≥1, contradicting (12.2) and p=0.

Finally let T be ruled, after blowups, over a curve C of genus g≥1.
Equation (12.1) gives p=g-1. A general ruling fibre F has
K_T·F=-2. Since π^*K_S is numerically trivial, E·F=2.
At least one exceptional component E_j therefore maps onto C.
Its normalization has genus at least g by the Riemann--Hurwitz
formula, so h¹(E_j,O_{E_j})≥g. Equation (12.2), with Z=E_j,
gives p≥g, contradicting p=g-1. This exhausts the normal case.

**Nonnormal supports.** Write ν:N→S for normalization and
π:T→N for its minimal resolution. The residue/adjunction
comparison gives a pole divisor along the conductor on N.
On T its strict transform D is nonzero and effective. The
exceptional discrepancy calculation just given, with
(K_T+D)·E_j in place of K_T·E_j, makes the remaining pole
divisor effective as well, because D·E_j≥0. Thus, after taking
the m-th power to trivialize the pulled-back ω_S,

    mK_T + D'  ~  0

for a nonzero effective integral divisor D'. This also follows
from the precise conductor formula CDP2020 Lemma 4.6, which
does not use its disputed global restriction argument. A positive
pluricanonical section on T would contradict this effective
anticanonical relation by taking powers. Hence κ(T)=-∞, and
BHPV VI.1.1 gives the stated minimal-model alternatives. ∎

This proposition does not by itself bound the genus in the ruled
alternative for a nonnormal support, compute its Euler number, or
settle the class-VII conductor case. Those are still the exact
remaining steps of P4.9.

## P4.13 (Proved). The smooth locus has nonnegative Euler number

For any proper holomorphic degeneration of complex two-tori with
smooth total threefold and central fibre mS of irreducible reduced
support, let A be its monodromy on H1 of a nearby torus. Then

    m e(S_reg) = det(I-A^m),       0 <= e(S_reg) <= 16/m.

This result does not require b2 of a global compactification to vanish.
Consequently a negative Euler number of S in the unresolved case would
have to arise from its singular locus.

**Proof.** Resolve the pair by a proper holomorphic modification
π:U'→U, isomorphic away from S and over S_reg, so that the total
central divisor has normal crossings. Every exceptional component has
multiplicity at least 2m: the first centre lies over a singular point
of the reduced divisor, whose multiplicity is at least two; subsequent
centres either inherit such an exceptional multiplicity or add it to
other positive multiplicities. The strict transform has multiplicity m.

We give the trace argument to specify the analytic comparison. At a
point on k branches of multiplicities n1,...,nk, the local model is
z1^n1...zk^nk=t. Its nearby fibre retracts onto a disjoint union of
real (k-1)-tori. Monodromy permutes the components and acts by a
translation on each component that it preserves. For k≥2 its
alternating cohomological trace is therefore zero. At a point on a
single branch of multiplicity n, the local nearby fibre consists of
n contractible components, cyclically permuted; the trace of the d-th
iterate is n if n divides d, and zero otherwise. Stratifying the
compact central divisor and taking alternating traces in its nearby-
cycle spectral sequence consequently gives

    L(A^d on H*(T4)) = Σ_{n_j | d} n_j e(E_j^o).

This is exactly the global form of A'Campo's Theorem 1, obtained from
the proper analytic construction in his §2 and the spectral-sequence
argument in §3. The local torus calculation above checks its hypotheses
and shows why no Kähler hypothesis enters. For d=m only the strict
transform contributes, and its open stratum is S_reg. Thus the right
side is m e(S_reg).

The same local model proves quasi-unipotence without an additional
polarization assumption. A common multiple N of the n_j makes
monodromy act trivially on every local nearby-cohomology sheaf. It
therefore acts trivially on the E2 page, and its action on the filtered
abutment is unipotent. In particular every eigenvalue of A is a root
of unity. The cohomology of a real four-torus is the exterior algebra
on H1, so its Lefschetz number is det(I-A^m). Nonreal eigenvalues pair
with their conjugates and contribute |1-λ^m|²; a real eigenvalue is
1 or -1, contributing zero or two. The determinant is nonnegative
and at most 2^4. This proves the identity and the bound. ∎

## P4.14 (Proved). The omitted genus-one conductor models

The curve-classification inference in CDP2020, Proposition 7.3,
printed p.694, needs an additional argument: a reduced reducible
Gorenstein curve with trivial dualizing sheaf and rational normalization
need not be a nodal cycle. In particular the two reduced plane cubics

    Z(Y²-XZ)=0,                  XY(X-Y)=0

have respectively two tangent rational components and three concurrent
rational components. Each has arithmetic genus one, dualizing sheaf
O, and conductor order two on every normalization branch. They refute
that intermediate classification as written. They do not themselves
give compact threefold counterexamples to the sign theorem.

**Proof.** A plane cubic is Cartier in P², so adjunction gives its
dualizing sheaf O(3-3)=O and its arithmetic genus one. In the first
cubic the line Z=0 meets the smooth conic Y²=XZ with intersection
multiplicity two at [1:0:0]. The local equation is analytically
y(y-x²)=0. Its normalization consists of two parameter discs, with
restrictions of a holomorphic function equal to (p(t,0),p(t,t²)).
The image consists exactly of pairs whose difference is divisible by
t²: given (a,b), use p(x,y)=a(x)+y(b(x)-a(x))/x². Its codimension is
two, and its conductor is (t²) on each branch.

For the second cubic use branches (x,y)=(t,0),(0,t),(t,t). The three
constant coefficients must be equal, and the third linear coefficient
must be the sum of the first two. These are exactly three independent
conditions. Every triple of coefficients in each degree k≥2 is
realized independently by x^k-x^{k-1}y, y^k-xy^{k-1}, and
x^{k-1}y (with the evident adjustment at k=2, where the first two
and third still give the three independent restrictions). Hence the
normalization quotient has length three and the conductor is again
(t²) on every branch. The normalization Euler characteristics are
two and three, respectively; subtracting the lengths gives zero for
χ(O_C) in both cases, agreeing with adjunction.

The exact rational jet matrices through orders 2,3,4,6,8, their ranks,
and the conductor tests are recomputed in
`code/part4/genus_one_conductor.py` and its executed output. In a
surface family, monodromy can assemble the two or three normalization
branches into one curve covering the image double curve with degree
two or three. Thus a unique horizontal conductor component of
multiplicity two does not by itself imply that this covering has
degree one, or that the image conductor is generically reduced. ∎

