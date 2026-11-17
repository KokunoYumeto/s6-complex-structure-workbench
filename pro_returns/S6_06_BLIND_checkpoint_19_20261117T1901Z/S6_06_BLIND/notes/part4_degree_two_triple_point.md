# The sole three-branch image point in the degree-two remainder

Current status: **Proved, P4R.20**, after complete independent
audits by both root and checks. The first audit-request status below is
retained as history.
The export is `notes/part4_degree_two_triple_point.tex`; exact executed
certificates are `code/part4/degree_two_triple_point.py`, `.json`, and `.out`.

Status: complete proof submitted for independent audit. The standing
inputs are P4.55 and the exact identities in
`part4_degree_two_spectral_working.md`. This note treats the remaining
case in which the generic transverse germ along B has at least three
normalization branches. It keeps its unrestricted intersection
multiplicities and conductor exponents.

## Claim and notation

The unique image-graph cycle cannot be concentrated at one point p
with three local critical-curve branches, namely the smooth branch A
and the two local branches B+ and B- of the other global component.

Write c for the number of normalized conductor components W_i mapping
onto B, and d_i for their finite degrees over B^nu. Put r_B=sum d_i;
this is the number of generic normalization branches of the full
transverse plane curve along B. In this note r_B>=3. The normalization
conductor has components H,R,W_1,...,W_c and a tree graph, with total
point-identification contribution c+1. H maps with degree two to A,
R with degree one. Distinct points of H are not identified in N.
Distinct points of R are not identified either: such an identification
through a contracted vertical tree would create a cycle in the ruling
fibre. We count all branches on the normalization of this conductor.

## 1. The graph when c>=2

Let r_A be the number of normalized conductor points above the A
branch at p. It is two when H->A is ramified there, and three otherwise.
Let r_+,r_- count those above B+,B-. Every W_i is surjective to B^nu,
so r_+,r_- >=c. Let n_p be the number of normalization points of S
over p. The nonempty supports of these points in {A,+,-} pairwise
intersect, because distinct analytic hypersurface components intersect
in a curve.

A singleton support {A} would force all points to carry A, giving
n_p<=r_A and graph contribution at least r_++r_- >=2c>c+1.
A singleton {+} would force all points to carry +, giving contribution
at least r_A+r_- >=c+2. The same applies to {-}. Thus every support
has at least two elements. It follows that

    graph contribution >=(r_A+r_++r_-)/2 >=c+1.

The entire global budget is c+1. Equality is forced everywhere:

    r_A=2, r_+=r_-=c, n_p=c+1.

Every normalization point over p has exactly two normalized conductor
branches with different image labels. All graph identifications occur
at p. The horizontal cover is ramified over p. Each W_i has precisely
one point over each of B+ and B-, and therefore has valence two in the
conductor graph. H and R each have valence one. The connected tree is
thus exactly a path, labeled consecutively

    H -- W_1 -- W_2 -- ... -- W_c -- R.                 (T2.1)

Relabel the two local B branches so that the H endpoint carries B+.
This uses the unique B+ point on W_1, so its next point has label B-.
Every internal normalization point has support {+,-}; it therefore
joins that B- point to the B+ point of W_2. Induction along the path
shows that each W_i has its B+ point on the left and its B- point
on the right. The R endpoint consequently carries B-.

The local hypersurface factors at the endpoints will be called f_H
and f_R. The c-1 internal points correspond to factors f_j whose
conductor support has labels {+,-}. The endpoint factors have labels
{A,+} and {A,-}. These are all c+1 local irreducible hypersurface
factors.

## 2. The endpoint intersection is the actual double ribbon

The set-theoretic intersection of f_H and f_R is A alone. Along
generic A, f_H supplies two ordinary-triple branches and f_R supplies
the third. Their complete-intersection multiplicity along A is two.
The one-dimensional complete-intersection ring is Cohen--Macaulay
and has no zero-dimensional embedded component. A coordinate z on
the smooth A is a nonzerodivisor, so this ring is finite free of rank
two over C{z}. Its quotient by z has length two.

If both f_H and f_R had no linear term, their restrictions modulo z
would lie in the square of (x,y). The Artinian quotient would then
have dimension at least three, from 1,x,y, contrary to length two.
At least one factor is smooth at p. It cannot be f_H: a smooth local
surface is its own normalization and has one generic preimage of A,
whereas this component supplies the ramified double cover H.
Therefore f_R is smooth. Take an actual ambient coordinate u=f_R.
On its plane u=0, the divisor cut out by f_H is exactly twice the
smooth curve A, so in further coordinates A=(u=v=0),

    f_H(0,v,z)=unit * v^2.

Weierstrass preparation in v and depression of the resulting monic
quadratic, using f_H in (u,v)^2, give the exact equality

    f_H=unit * [v^2+u^2 g(u,z)].                       (T2.2)

All coordinate changes preserve A. Its actual full cubic tensor is,
up to a nonvanishing scalar function,

    [product_j f_j(0,0,z)] * u[v^2+u^2 g(0,z)].        (T2.3)

The coefficient of uv^2 in the bracket is one. Thus its common zero
order at p is exactly the sum of ord_A f_j.

## 3. The scalar-zero degree and the pole on the smooth R branch

On the smooth normalization branch f_R=0, its conductor divisor is
the restriction of the product of the other hypersurface factors.
The factor f_H contributes 2A. Every f_j cuts out only B- there.
The global pole divisor has SNC support on the minimal normalization
resolution, and this branch is already smooth; hence A and this
B-curve are smooth and transverse. Choose its equation z=0 on this
surface, with z still a coordinate on A, and extend it to the ambient
threefold. Then

    f_j|_{f_R=0}=unit * z^{e_j},     e_j>=1.

The total e=sum e_j is the generic conductor exponent of the global
B-normalization component W_c on this branch. Restricting to A
and using (T2.3) shows that the common cubic-zero order at p is e.

The local B branch on f_R=0 is smooth. The plane-curve conductor
formula gives

    e=sum(other branches of B) I(branch_R,branch)
       >=r_B-1>=2.

The global spectral identity g(H)+delta_H+n=5-2b gives b<=2.
Since b>=e, equality follows:

    b=e=2, r_B=3, g(H)=1, delta_H=n=0.                 (T2.4)

In particular the residual spectral curve Gamma_H is smooth, and is
disjoint from the rational section Gamma_R. The cubic has no other
common zero.

## 4. The actual normalization at the ramified endpoint

The horizontal map is ramified at p by Section 1. Equation (T2.2)
represents its spectral double cover by w^2+g(0,z)=0. Smoothness of
Gamma_H in (T2.4) makes g_z(0,0) nonzero, after translating the
double root to w=0. The surface

    N_H={w^2+g(u,z)=0},
    (u,w,z) -> (u,v=uw,z)                              (T2.5)

is smooth at the point, is finite over the branch (T2.2), and is
birational away from u=0. It is therefore the actual normalization
there. The minimal normalization resolution has no exceptional
curve over this smooth point. Coordinates (u,w) give z=psi(u,w),
with z|_H a function of order two in w. H is u=0.

The other conductor branch W_1 meets H transversely by SNC.
Consequently u restricts to a coordinate on W_1. Its image B+
has u of order one as well. Since W_1 has only one point over the
normalization point B+ at p, its global degree is d_1=1.
Likewise f_R=0 is smooth, its B-curve meets A transversely, and
d_c=1.

Now sum d_i=r_B=3. For c>=2, the two endpoint degrees one exclude
c=2, and c>3 is impossible. Thus

    c=3,       d_1=d_2=d_3=1.                         (T2.6)

There are exactly two B-only factors f_1,f_2, and e_1=e_2=1 by
sum e_j=2.

## 5. Incompatible conductor exponents on the same global B sheet

Each f_j intersects the branch f_H only along B+. Pull it back by
the actual smooth normalization map (T2.5). Its divisor is supported
only on W_1. On H its zero has order two, because its order on A
is one and H->A has ramification index two. Since H and W_1 meet
transversely, its divisor is exactly 2W_1 locally. Hence the generic
intersection multiplicity of f_H with each f_j along B+ is two.

In the path (T2.1) with c=3, the branch W_3 occurs on the smooth
R endpoint over B-, and on one of the B-only factors over B+.
At B- its conductor exponent is e=2. At B+ that same global
normalization-conductor curve has intersection multiplicity two
with f_H and positive intersection multiplicity with the other
B-only factor. Its conductor exponent is therefore at least three.
Conductor multiplicity is constant at the generic point of the
global irreducible curve W_3; it cannot take these two different
values on its nonempty open subsets. This is the contradiction.

The complete marking can also be read directly from the path. Over
B+, the factors (f_H,f_1,f_2) carry (W_1,W_2,W_3); over B-, the
factors (f_1,f_2,f_R) carry (W_1,W_2,W_3). If p_+,p_- are the
intersection multiplicities of f_1 and f_2 on the two B branches,
their conductor vectors are respectively

    (4, 2+p_+, 2+p_+),       (1+p_-, 1+p_-, 2).

Here p_+,p_->=1. The third entries already contradict equality.
There is no omitted intrinsic branch-delta term in these vectors:
the exponent two of the smooth R branch at B- forces its two
intersection multiplicities to equal one, which makes both other
generic B branches smooth as well.

## 6. The case c=1

Here the conductor graph has components H,R,W and total budget two.
The points of W over B+ and B- cannot be identified in N, since
that would give a loop in the conductor tree. Points carrying B+
and B- must therefore be distinct. Their supports must intersect,
so both carry A. Each contributes at least one to the graph budget,
which is then exhausted. Each has exactly one A branch and one
B branch; no further identification is possible.

If H is ramified over p, the two A branches are H and R. There
are just the two factors f_H and f_R, with supports {A,+} and
{A,-}. The length-two ribbon argument of Section 2 makes f_R
smooth. No other factor contains B- and it has no singularity
on its smooth branch. Thus B- cannot be a critical curve at all,
a contradiction.

If H is unramified, the three normalized A preimages are distinct.
Two occur at the B attachment points and the third gives an
A-only normalization point. There are three hypersurface factors,
each supplying one generic D4 branch along A. Every pair meets
only along A with generic multiplicity one. Its complete-intersection
curve is therefore the reduced smooth A: it is pure and generically
reduced, with no other component. Modulo its coordinate z the
intersection ring has length one, forcing independent normal linear
terms for the two factors. All three factors are consequently
smooth near p, and their only pairwise intersection is A. Neither
B+ nor B- can then be a critical-curve branch. This final
contradiction completes the exclusion.

## Remaining scope

This proof excludes the single three-branch image point in the
generic-r_B>=3 sector. The independently audited two-distinct-junction
proof is now complete in `part4_d4_two_junction_closure.md`. It uses
the descended ruling to choose separate H/R normalization preimages
and does not require the unfinished auxiliary chain comparison.
The previous status paragraph is preserved verbatim in
`records/part4_degree_two_route_history.md`.
