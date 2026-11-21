# 02WX / night:P4.25: independent derivation before target-proof release

The target proof and old target computations remain closed. The original
statement/supplement and the root's citation-only standing-domain packet are the
input boundary. The local classification argument, the actual multiplicity
maps and the stated global receiving scope are derived below before release.

## 1. Standing map and primary classification

The actual map is f:Y→B, proper and surjective with connected fibres, Y smooth
compact complex of dimension three, b1(Y)=b2(Y)=0, and smooth general fibre a
complex two-torus. For the first assertion let F_red be any reduced fibre
support which is semi-log-canonical. Its irreducible components can carry
different positive multiplicities in the full fibre. Those multiplicities are
retained below; they are not replaced by a common integer.

The exact published Liu–Rollenske article is Le Matematiche 67(2) (2012),
185–202, DOI 10.4418/2012.67.2.14. Theorem 1.1 is on p.186, Table 1 on p.187,
Definition 2.3 and Lemma 2.2 on p.189, and the normal-crossing-pair observation
on p.190. Proposition 3.1 and its complete proof occupy pp.192–196;
Proposition 4.1 and its complete proof occupy pp.196–200. The full published
text, including these complete proofs, has been read; Table 1 was also viewed
as a full-page image. The exact retrieval SHA is
def3c8f41beaa7d24894b8d8680fb290b6df7f55d768d75be3e665341cf39a71.

At every point the table gives a local analytic isomorphism of hypersurface
germs. For a singular germ its embedding dimension is three. Lift the images
of the three coordinate classes under that local-ring isomorphism to
convergent ambient functions. Their linear terms form an invertible matrix on
the cotangent space, so the resulting map Φ of ambient threefold germs is a
biholomorphism by the inverse function theorem. The principal defining ideals
are then carried to each other up to a holomorphic unit. Consequently the
actual local fibration function is, in the Φ coordinates,

    U ∏ g_i^(m_i),

where the g_i are the irreducible factors of the displayed reduced normal
form, U is a unit, and m_i are precisely the original fibre multiplicities.
This is the required map from the table to the actual fibre function.

The retained cases are the smooth germ, the ordinary double germ
x²+y²=(x+iy)(x−iy), and the ordinary triple germ xyz. The exact linear map
(x,y,z)↦(x+iy,x−iy,z) identifies the double germ with uv=0. The other cases
will be excluded by compact negative spheres in the nearby fibre.

## 2. The sphere obstruction and its orientation

Let M_P be the smooth complex surface

    {(s,a,b): s in an open subset of C*, ab=P(s)},

where P has two distinct simple zeros s0,s1. Choose a smooth embedded path γ
from s0 to s1 with no other zeros on it. The set over γ defined by |a|=|b|
is a circle over each interior point, with its circle collapsed at either
endpoint. It is a smooth embedded sphere L. Near a simple zero, use P(s) as
the base coordinate; the end has the form (a,b)=(z,e^(iθ) conjugate(z)),
after a smooth choice of the phase of the path, which proves smoothness.

For the restriction of the standard Kähler form in the (s,a,b) coordinates,
the action (a,b)↦(e^(iθ)a,e^(−iθ)b) has moment function proportional to
|a|²−|b|². Its derivative along L is zero. The circle tangent and the path
tangent therefore pair to zero under the Kähler form, so L is Lagrangian.
The complex structure identifies its normal bundle with TL. The orientation
of (e1,e2,Je1,Je2) differs by one transposition from the complex orientation
(e1,Je1,e2,Je2). Hence the oriented normal Euler number is −e(TL)=−2.
Thus L.L=−2, with the orientation sign fixed explicitly.

Every continuous S²→a complex two-torus lifts to its universal cover C²,
because S² is simply connected. The lift contracts linearly, so its homology
class in the torus is zero. An embedded sphere in that torus therefore has
self-intersection zero. The compact sphere above cannot embed as an open-
subset sphere in a nearby torus: its normal bundle in that open subset is
the restriction of the same normal bundle in the torus and has Euler number
−2. This is the obstruction used in every case below.

## 3. Units and positive weighted scaling

For a weighted homogeneous polynomial G with positive integer weights
(w1,w2,w3) and degree W, the coordinate map

    Ψ(z1,z2,z3)=(U(z)^(w1/W) z1,
                 U(z)^(w2/W) z2,
                 U(z)^(w3/W) z3)

is defined using one local holomorphic logarithm of the nonzero unit U.
It satisfies G∘Ψ=U G. Its derivative at zero is an invertible diagonal
matrix, so it is a biholomorphism of germs. This absorbs the actual unit
through a specified morphism. It is also valid for G=∏g_i^(m_i) when its
weighted degree includes the original multiplicities.

For any compact sphere in G^−1(1), the maps

    σ_λ(z1,z2,z3)=(λ^w1 z1,λ^w2 z2,λ^w3 z3), λ>0,

send it into G^−1(λ^W) and into every sufficiently small coordinate ball.
The inverse Ψ^−1 and Φ put this exact sphere in a nearby fibre of the
original f. Every σ_λ, Ψ and Φ is holomorphic on the relevant neighborhood
and preserves the complex orientation, so the normal Euler number is still
−2. No passage from an affine fibre to a local Milnor fibre is left implicit.

## 4. Degenerate double points

### 4a. T_(2,q,infinity), q≥3

The reduced equation is

    g=x²+y²z²+y^q.

It is irreducible as a polynomial: a quadratic factorization in x would
require z²+y^(q−2) to be a square in C(y,z); its reduced divisor has
components of multiplicity one, so this is impossible. Its positive weights
(q,2,q−2) have degree 2q. An analytic factorization into nonunits would
give a polynomial factorization by taking their lowest weighted parts.
Thus the analytic germ is irreducible as well. Its local full multiplicity
is one integer m, and the unit is absorbed for G=g^m as in Section 3.

On g=1 with y≠0 set

    s=y, a=x/y+iz, b=x/y−iz.

The inverse is y=s, x=s(a+b)/2, z=(a−b)/(2i). Under these exact maps,

    ab=(1−s^q)/s².

The q-th roots of one are q distinct simple zeros in C*, with q≥3.
Section 2 supplies a compact sphere of square −2. Positive weighted scaling
puts it in g=λ^(2q), hence in the actual full fibre g^m=λ^(2qm).
This excludes all finite-q double degenerate cusps.

### 4b. T_(2,infinity,infinity), with unequal component multiplicities

The two irreducible smooth branches have equations

    U=x−iyz, V=x+iyz.

Write their actual positive multiplicities as a0,b0. The local full function,
after the explicit unit map, is U^a0 V^b0. Its weights are (2,1,1), of total
degree 2(a0+b0). Put d=gcd(a0,b0), a'=a0/d, b'=b0/d. On a connected
component of U^a0 V^b0=1 choose nonzero constants A,B with
A^a0 B^b0=1 and use

    U=A s^b', V=B s^(−a'), s∈C*.

Choose integers r,t with rb'−ta'=1. The inverse parameter is
s=(U/A)^r(V/B)^t on that component. The inverse ambient coordinates are
x=(U+V)/2 and yz=(V−U)/(2i), so it is the conic surface

    yz=(B s^(−a')−A s^b')/(2i).

Its a'+b' simple zeros are the nonzero roots of s^(a'+b')=B/A.
There are at least two. The negative sphere from Section 2 and the weighted
map of Section 3 exclude this germ for every pair (a0,b0), not only for
equal multiplicities.

### 4c. The pinch point

The equation x²+y²z is carried to x²−z y² by the exact coordinate change
z↦−z. The analytic germ is irreducible, so its full function has a common
positive multiplicity. The already independently derived P4.16 input excludes
it with precisely this map and every such multiplicity.

## 5. Degenerate triple points

### 5a. T_(p,q,infinity), q≥p≥3

The reduced equation is g=xyz+x^p+y^q. It is primitive and degree one in z
over C[x,y]; gcd(xy,x^p+y^q)=1, so it is irreducible in C[x,y,z]. Its
positive integer weights are (q,p,pq−p−q), of degree pq. The last weight is
positive for p,q≥3. Lowest weighted parts again show that it is analytically
irreducible. Thus its full local function has one multiplicity m.

On g=1 with x≠0 the exact coordinate maps are

    s=x, a=y, b=xz+y^(q−1);
    x=s, y=a, z=(b−a^(q−1))/s.

They identify this open subset with

    ab=1−s^p.

The p simple roots of one give a negative sphere. Its image under the
weights above lies in g^m=λ^(mpq), and hence in a nearby torus, a
contradiction. This excludes every finite-p, finite-q triple degenerate cusp.

### 5b. T_(p,infinity,infinity), p≥3, with unequal multiplicities

The two reduced irreducible factors are U=x and V=yz+x^(p−1). The second
factor is irreducible (a primitive degree-one polynomial in z); its analytic
irreducibility also follows from its positive weighted initial form. Let
their actual multiplicities be a0,b0. Use weights (2,p−1,p−1), so
U^a0 V^b0 has degree 2a0+2(p−1)b0. With d,a',b',A,B and the exact Bezout
inverse parameter defined as in Section 4b,

    x=A s^b', V=B s^(−a'),
    yz=B s^(−a')−A^(p−1)s^((p−1)b').

The number of nonzero simple roots is a'+(p−1)b'≥p≥3. Hence a compact
negative sphere exists and contracts into the actual nearby fibre by the
specified positive weights. This covers both independent multiplicities.

The sole remaining triple germ is xyz=0, already a normal-crossing divisor.

## 6. Isolated normal cases and the actual perturbation maps

The remaining excluded table entries are the isolated normal singularities
A_n,D_n,E6,E7,E8, the three simple-elliptic families and the isolated cusp
family T_(p,q,r). A reduced hypersurface germ with isolated singular locus
has one analytic component: two distinct two-dimensional components in a
smooth threefold would intersect in a curve of singular points. Thus the
actual full local function is U g^m. Taking a holomorphic m-th root of U
gives h=U^(1/m)g and f=h^m. The critical point of h is isolated. Indeed,
any positive-dimensional analytic component of dh=0 through the origin would
have h constantly zero, producing a curve in the singular locus of h=0.

The primary multiplicity input is Milnor, Singular Points of Complex
Hypersurfaces, Princeton and Tokyo, 1968, Appendix B, pp.111–114:
Lemmas B.1–B.3, Corollary B.4, their complete proofs, and the concluding
positivity proof. These exact complete page images have now been read.
The opening hypotheses on p.111 and Lemma B.3 are analytic. Although the
displayed positivity theorem on p.114 says polynomial equations, its proof
uses only the following analytic constructions, which are reproduced here
for the actual h rather than asserted by an unstated identification.

Put G=(h_x,h_y,h_z). Its only zero in a sufficiently small closed ball is
the origin. Its degree μ on the boundary is defined by G/||G||. For a small
complex η outside the finite spectrum of DG(0), G'=G−ηz has an invertible
derivative at zero and has no zero on the boundary. The inverse function
theorem gives an open neighborhood V of zero in the image of a small
neighborhood of zero under G'. Choose a small regular value a in V.
The zeros of G'−a in the closed ball are isolated, stay away from the
boundary, and are therefore finite by compactness. At least one lies in
that inverse-function neighborhood. Each has degree +1 because its
complex derivative is invertible: the real determinant is the positive
number |det_C DG'|². On the boundary, the homotopies from G to G' and
then G'−a stay nonzero. Additivity of degree, obtained by removing small
balls around these zeros and applying the boundary homology relation,
therefore gives μ≥1. This is the complete analytic transport of the
positivity argument, with its explicit maps G, G' and G'−a.

Now choose a small regular value c of G. By precisely the same boundary
degree argument the equation G=c has μ≥1 solutions, each with invertible
Jacobian. These are the nondegenerate critical points of h_c=h−c·z.
They all tend to zero as c tends to zero: on every closed annulus in the
chosen ball the continuous nonzero function ||G|| has a positive minimum.
This also holds uniformly for h_sc=h−sc·z, 0≤s≤1.

Here are the boundary and fibre identifications in detail. First choose a
small radius ε such that the sphere of radius ε is transverse to h=0.
Such radii exist by Sard's theorem applied to the squared distance on
the smooth punctured hypersurface h=0. At a point of that intersection,
the real differential of h restricted to the sphere is surjective: its
kernel is the three-dimensional intersection of the four-dimensional
tangent space to h=0 with the five-dimensional sphere tangent space.
Compactness of the intersection gives a number δ>0 such that the
restriction to the sphere stays submersive over |h|≤2δ. On the remaining
compact part of the sphere, |h| is bounded away from zero. Consequently,
after reducing δ and c, the same boundary statement holds uniformly for
h_sc, 0≤s≤1. All critical values of all these h_sc lie in |t|<δ/2,
by the preceding annulus argument and continuity near zero.

Fix a t0 with |t0|=δ. The compact family

    {(z,s): ||z||≤ε, h_sc(z)=t0, 0≤s≤1}

is a smooth family of manifolds with boundary. In the interior solve
d_z h_sc(v)=c·z for a real horizontal vector v; at the boundary impose
v tangent to the sphere as well, which is possible by the boundary
surjectivity just proved. Local solutions glue by a partition of unity,
since the equations are affine and linear in v. Their flow exists for
the entire compact parameter interval and preserves the boundary. It
gives an orientation-preserving diffeomorphism from h_c=t0 in the ball
to h=t0 there. The fibre orientations are their complex orientations;
the continuous horizontal flow preserves them.

Choose a critical point p of h_c and its critical value v. The analytic
Morse coordinates are explicit in construction: after a complex linear
coordinate change one second derivative in the first coordinate is
nonzero; the implicit function theorem solves h_{c,z1}=0 as z1=a(z2,z3).
Taylor division writes h_c−h_c(a,z2,z3)=(z1−a)²u with u(0)≠0.
Taking a holomorphic square root of u gives the first square coordinate.
The remaining Hessian is its invertible Schur complement. Repeating
this construction gives the exact germ h_c=v+w1²+w2²+w3².
For small positive real r the real sphere

    {w in R³: w1²+w2²+w3²=r}

lies in h_c=v+r. It is Lagrangian for the standard form in these Morse
coordinates, and the tangent/normal orientation calculation in Section 2
gives self-intersection −2. The holomorphic coordinate map preserves
that oriented normal bundle.

The finitely many critical values of h_c can be avoided by a path from
v+r to t0 inside |t|<2δ. Along the compact inverse image of this path,
solve d h_c(v)=dot(t) by horizontal vector fields tangent to the sphere
on its boundary, using the boundary surjectivity above. Their complete
flow carries this small embedded sphere to h_c=t0 while preserving its
normal Euler number. Compose with the preceding parameter-flow map to
h=t0, and include this local hypersurface in the global fibre f=t0^m.
Choose t0 away from the finite set of global critical values; all small
noncentral regular fibres are the given complex two-tori. This gives the
forbidden embedded sphere of square −2 in an actual torus fibre.

Thus every isolated normal singularity in the Liu–Rollenske table is
excluded, including all the simple-elliptic and cusp entries. No
weighted-homogeneous assumption was imposed on these entries. Together
with Sections 4–5, the table leaves precisely the smooth, ordinary-double
and ordinary-triple normal-crossing germs.

## 7. The actual reduced resolution divisor

Let ν:N→S be the normalization and π:T→N a resolution, so ρ=ν∘π. The
divisor in the target is interpreted with its natural residue identification:
for a local generator Ω of the hypersurface dualizing line, D is minus the
divisor of the pulled-back meromorphic two-form ρ*Ω. Changes of Ω by units
change the form by the pulled-back unit and do not alter D. This specifies
the actual divisor, not merely its linear-equivalence class.

Assume this D is reduced and has normal crossings. At a general point of
any singular curve of S, a transverse plane curve is reduced and Gorenstein.
Its normalization conductor exponents are exactly the strict coefficients
of D, hence are all one. For r branches the conductor length identity gives
2δ=r. The inequality δ≥r−1, with equality only for smooth branches meeting
as an ordinary node when r=2, gives r≤2. The case r=1 would make 2δ=1,
which is impossible. Thus r=2 and δ=1, so S is ordinary double in
codimension one. The case of no singular curve gives normality in
codimension one directly.

The hypersurface S is S2 and its dualizing sheaf is invertible. Write D_N
for the normalization conductor Weil divisor. The codimension-one residue
identity extends reflexively to K_N+D_N=ν*K_S, a Cartier divisor. The
specified resolution identity gives

    K_T+D=π*(K_N+D_N),   π_*D=D_N.

The smooth normal-crossing pair (T,D) is log canonical: under a blowup of
a point meeting zero, one or two coefficient-one components, the new
coefficient is respectively −1,0 or1; subsequent point blowups retain
coefficients at most one. All divisorial valuations of a smooth surface
are obtained through such point blowups. Liu–Rollenske Lemma 2.2 transports
log canonicity through the exact π above. Their Definition 2.3 now makes
S semi-log-canonical. Sections 1–6 therefore give
normal crossings on S. Its normalization is locally the disjoint union
of the coordinate planes, hence is smooth.

## 8. Exact scope of the final invocation

The reduced-support normal-crossing conclusion permits P4.6 for that
specified support in the standing compact setting, because b2(Y)=0.
It gives e(S)=T(S) with T(S) even, retaining precisely its specified
normal-crossing divisor S and the original ambient Y.

The P4.7/P4.8 statements have hypotheses on all reduced supports, as is
explicit in the safe P4.8 input. Their global conclusions follow for the
original f:Y→B when all those reduced supports have normal crossings;
the first assertion here verifies that hypothesis for a fibration all of
whose reduced supports are semi-log-canonical. The original final bare
phrase 'P4.6–P4.8 apply' does not state this quantifier. The proposed
wording will retain every conclusion, state the full all-supports domain
of the global conclusions, and retain the individual-support P4.6
conclusion. This is an explicit scope clarification and will be reported
as D25 rather than using an unchanged-statement flag.

The safe receiver scan (SHA 87576521d10b3e465c39bda665eb10ae6ad6db9c275532713665593af8974626)
finds two statement/tag index occurrences and a metadata dependency in
P4.26. The second index was initially classified by its nearest heading;
root has supplied its exact index-row text, which adds no mathematical claim. The entire P4.26 statement has been read; its local
normal-crossing Euler assertion and its explicitly quantified global
assertion are consistent with the maps just given. No P4.26 proof has
been opened and no independent credit for that owner is taken. Root also inspected the two bare P4.25 receiving calls in the future
P4.26 proof and reported that both use the retained local conclusions.
This bounded receiver finding is bound by root receipt SHA
9531e0acb7cf3042c1081dcff2c5e45d75790ac211c2a9df288eee4c8d2c6797.
That receipt includes receiving-proof fragments and has not been opened
by this checker before the P4.26 freeze; the safe finding above is the
parent message, with no transmitted receiving argument.

## 9. Fresh computations and timing boundary

The independent program is code/S6_SERIES_PUBLISH_II_A_02WX_conic_maps.py,
SHA 2b782256fbf968a1ae674a05f70c787ea9099d38c641ab6f426d8931138ffa5b,
with output SHA bae9e32d1088fcb8ae2c722eae39d0c2b61fc5dc7bea059a4e3a66d8fbd0535e.
It ran at 22:34:31.460000–22:34:31.512635 UTC on 2026-11-21 and its
complete output was read before this derivation was frozen. The exact
Gaussian-integer finite grids, with stated separate-degree bounds,
certify the conic coordinate identities. The Euclidean-algorithm rows
verify the inverse exponents on the displayed sample multiplicities;
the universal inverse is proved in Sections 4b and 5b. The programme also
checks the positive weights, the Morse Hessian determinant, the sphere
cell Euler number and normal orientation permutation, and the conductor
and blowup arithmetic. These computations were written without reading
the target proof or any associated prior routine. Their scope is the
displayed algebra and arithmetic, not an asserted numerical proof of
the universal geometric argument.

All sections of this derivation precede release of the 02WX target proof.
