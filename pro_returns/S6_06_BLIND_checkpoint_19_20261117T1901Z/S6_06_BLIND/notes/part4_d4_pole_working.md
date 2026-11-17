# A coefficient-two exceptional curve cannot occur over a uniformly D4 germ

Current-run proof, 2026-11-17; independent audit requested. This text is not
yet inserted into the numbered theorem list.

Let S=(f=0) be a reduced hypersurface germ in a smooth threefold, with a
one-dimensional reduced critical locus C. Suppose every generic transverse
germ along C is an ordinary triple point. Let T -> N -> S be the minimal
resolution of its normalization. Use the canonical meromorphic two-form
obtained as the residue of a local ambient volume form divided by f to define
the integral total pole divisor D on T. Thus K_T+D is the pullback of the
trivial dualizing line of this germ, with the specified comparison map.

**Claim.** An exceptional component H of positive geometric genus cannot
have coefficient two in D.

## 1. The precise comparison after the ambient point blowup

Blow up the ambient origin. Let S1 be the strict transform, N1 its
normalization, and T1 the minimal resolution of N1. The proper map N1 -> S
lifts to N by the universal property of normalization, and T1 -> N is a
resolution. It dominates the minimal resolution T; its map to T is a
sequence of point blowups. The strict transform of H is consequently still
present and has the same pole coefficient two.

Write d=mult_0(f) and E for the ambient exceptional divisor. The actual
adjunction isomorphism is

    omega_S1 = pi^*omega_S tensor O((2-d)E)|S1.

Let D1 be the total conductor/pole divisor of T1 relative to omega_S1,
and let e be the Cartier pullback of E. Then, with the same residue form,

    D_on_T1 = D1 + (d-2)e.

D1 is effective. Its strict conductor coefficients are positive integers.
For exceptional curves of the minimal resolution of N1, the argument of
P4R.6 applies without any global compactness assertion: K_T1.F is
nonnegative for every such curve, since no smooth rational (-1)-curve
occurs. Adding the strict conductor has nonnegative intersection with F.
The negative-definite exceptional matrix has nonpositive inverse, giving
nonnegative exceptional coefficients of D1.

If H is exceptional over N1, its D1 coefficient is strictly positive.
Indeed a zero coefficient would give
0=(K_T1+D1).H=2g(H)-2-H^2 + D1.H >0. More generally, if its coefficient is
one, adjunction gives

    0=2g(H)-2 + (D1-H).H.

It follows that H is elliptic and disjoint from every other positive
component of D1. A zero-coefficient exceptional curve cannot meet a
positive-coefficient one: its own intersection equation would have a
strictly positive right side. The connected exceptional fibre therefore
consists of H alone and is disjoint from the strict conductor. The germ of
S1 at its image is normal with an isolated simple elliptic singularity.
If another hypersurface branch were present, its curve intersection with
this branch would give strict conductor meeting H, so this conclusion
concerns the entire local germ of S1.

Set n=ord_H(e), a positive integer, and a=coeff_H(D1). The coefficient
identity is exactly

    2=(d-2)n+a.

Consequently d>=5 is impossible. If d=4, then n=1,a=0 and H cannot be
exceptional over N1. At its generic point the normalization map N1 -> S1
is an isomorphism, so H is birational to a reduced component of the
projective quartic tangent cone.

Every second derivative of f vanishes on C. Taking the leading term along
any analytic arc of C proves that the homogeneous quartic tangent cone has
a point of multiplicity at least three. Every reduced component of this
quartic is rational: an irreducible quartic has arithmetic genus three
and loses at least three at that point; a positive-genus cubic component
would be smooth elliptic and, together with the remaining line, could
have multiplicity at most two there. All components of degree at most two
are rational. Thus d=4 is impossible as well.

It remains to treat d=3. Its coefficient identity permits only
(n,a)=(2,0) or (1,1).

## 2. The exact cubic normal form

Choose a coordinate u with nonzero pure cubic initial coefficient and
apply Weierstrass preparation. Since f=df=0 on C, multiplication by its
unit does not change the vanishing of its Hessian on C. After depressing
the monic cubic, write

    f = unit*(u^3+b(x,z)u+c(x,z)).

The second u derivative is 6u. It vanishes on C, so C lies in the smooth
surface u=0. Its reduced ideal is (u,h(x,z)). The cubic has order three
along every generic component of C; the cube of this complete-intersection
ideal is unmixed and therefore equals its symbolic cube. Coefficient
comparison gives the exact expression

    f = unit*(u^3+h^2 B(x,z)u+h^3 C(x,z)).

If C is singular, ord(h)>=2, and the tangent cone is the triple plane
u^3. After the ambient point blowup, the strict transform is singular
along the whole reduced exceptional line: the degree-four term restricts
to zero there. In particular it has no isolated normal singularity on
that line.

If C is smooth, choose x=h, so the entire equation belongs to (u,x)^3.
Every homogeneous term f_j has degree at least three in u,x. Its cubic
tangent cone is a binary cubic in u,x, hence a union of three lines,
counted with multiplicities, through the tangent direction of C.

## 3. Components lying over the exceptional curve

For (n,a)=(2,0), the normalization is an isomorphism at the generic point
of H. Hence H is birational to a line component of the cubic tangent
cone, and is rational.

For (n,a)=(1,1), if H dominates a tangent-cone line, a generic transverse
branch on H has conductor exponent one. A reduced plane curve branch
with conductor exponent one is smooth and meets exactly one other smooth
branch transversely. Thus the generic transverse germ of S1 on that line
is an ordinary double point.

If the tangent-cone line has multiplicity one, S1 is smooth generically
on it, contradicting a=1. If it has multiplicity three, its normalized
ordinary-double cover has two geometric branches. Their orders of the
exceptional coordinate have weighted sum three. A connected double cover
would have equal orders on both branches and give an even sum. Thus the
branch with order one has degree one over the line and is rational.

The only remaining case is a double line together with a distinct simple
line. In particular C is smooth, since the singular-C normal form above
has triple-plane tangent cone. Make a linear change of u,x so that
f_3=xu^2. On the x-chart of the blowup put u=xv, z=xw. The strict equation
is

    v^2 + x f_4(1,v,w) + x^2 f_5(1,v,w)+... .

For an ordinary double curve along x=v=0 we must have
f_4(1,0,w)=0 identically. Its transverse quadratic form is

    v^2 + x v B(w)+x^2 C(w),

where B=partial_v f_4(1,0,w) has degree at most one in w, and
C=f_5(1,0,w) has degree at most two. These degree bounds follow directly
from the normal-degree-at-least-three condition on every f_j. The two
branches of the normalization over the exceptional line are obtained by
adjoining a root of q^2+B(w)q+C(w)=0. The discriminant is a polynomial of
degree at most two. Its quadratic function-field extension of C(w) is
branched at at most two points, including infinity. Riemann--Hurwitz
makes its compact normalization rational. This includes a split cover,
whose components are separately rational.

## 4. Components exceptional over a point of N1

The remaining possibility has n=a=1 and H exceptional over N1. Section 1
would make S1 normal with an isolated simple elliptic singularity at its
image. We now exclude that exact possibility.

For a singular C, Section 2 shows that the entire exceptional line is in
the critical locus, so no point on it is an isolated normal singularity.
For a smooth C, the strict transform of C passes through the common
intersection point of the tangent-cone lines. Hence that point also
cannot be an isolated normal singularity of S1.

Away from this common point, consider a line of multiplicity e=2 or3.
Use the affine parameter w on it and a normal coordinate v. After
dividing by the nonzero factor from any other tangent-cone line, the
strict equation has the form

    v^e+x G(v,w,x),

where G(0,w,0) is affine linear in w. This is again exactly the degree
bound f_4 in the preceding section. If this linear function is nonzero
at a point, S1 is smooth there. If it vanishes identically, the full line
is critical. At a simple zero, partial_w G is a unit, and the exact
coordinate change W=G(v,w,x) gives v^e+xW. This is a rational double
point A_(e-1). A multiplicity-one line is smooth away from intersections.
Thus no isolated simple elliptic singularity occurs anywhere on the
exceptional curve.

All possibilities for H have been exhausted. This proves the claim.

## Scope in the remaining global problem

In the ruled positive-genus case a contracted horizontal section has pole
coefficient two. The claim excludes its occurrence at any image point
where every local critical-curve branch has generic transverse type D4.
It does not assert the same for mixed A1/A2/A3/D4 branches. It also does not
exclude an uncontracted higher-genus section by itself.
