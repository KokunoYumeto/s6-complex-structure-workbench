# Degree-two horizontal cover: spectral identities and the two-common-zero remainder

Current status: the exact identities and direct-contact lemma below
are retained as an auxiliary route. The full degree-two sector is now
excluded by the independently audited two-junction proof in
`part4_d4_two_junction_closure.md` and the sole-three-point proof P4R.20.
The direct comparison through an intervening chain was not completed
or used in those proofs. Its former open-status passages are preserved
verbatim in `records/part4_degree_two_route_history.md`.

## 1. Objects and their actual maps

After P4.55, A is a smooth projective line, H maps to A with degree
two, and the third generic D4 normalization preimage is supplied by one
rational vertical conductor curve R, mapping with degree one to A.
Write T for the minimal normalization resolution, D for its total pole
divisor, and rho:T->S for the actual map. H and R both have pole
coefficient two. H is the horizontal section of the ruling; R lies in
one ruling fibre.

Put E=N_A/Y^*, of degree two, and use the quotient convention P(E),
with tautological class xi and fibre F. The normal derivative of rho
gives the actual meromorphic spectral maps from H and R; canceling the
common local power extends them to morphisms of smooth curves. Their
images are Gamma_H and Gamma_R. H is the normalization of Gamma_H,
while Gamma_R is a section and is isomorphic to A. The full residual
cubic, after removing the common zero divisor on A of degree b, has
class 3xi-bF.

Let delta_H be the total normalization colength of Gamma_H, and let
n=length(Gamma_H intersect Gamma_R). These are nonnegative integers.
Parameterize the section class by an integer t:

    Gamma_R = xi-tF,
    Gamma_H = 2xi+(t-b)F.

The projective-bundle identities are

    xi^2=2,  xi F=1,  F^2=0,  K_P(E)=-2xi.

They give exactly

    p_a(Gamma_H)=1+t-b=g(H)+delta_H,
    n=Gamma_H Gamma_R=4-t-b,
    g(H)+delta_H+n=5-2b.                              (H2.1)

No common zero or spectral singularity is deleted from these formulas.

## 2. The rational sheet's actual normal derivative

On R, the normal derivative takes the form

    N_R/T -> L_R,

where L_R is the actual tautological normal-direction line pulled back
from Gamma_R. Its zeros form an effective divisor Z_R. Equivalently,
the dual map is the quotient

    E -> N_R/T^*(-Z_R).

The degree of L_R is minus xi Gamma_R=t-2. Consequently

    R^2=t-2-deg Z_R.                                  (H2.2)

Adjunction and (K_T+D)R=0, with coefficient_R(D)=2, give

    R^2+(D-2R)R=2.

Combining this with (H2.1)--(H2.2) yields

    (D-2R)R=n+b+deg Z_R.                              (H2.3)

This is an equality of the actual pole and normal-derivative degrees.
It does not assert that Z_R vanishes or that every pole neighbour maps
onto the other global image component.

For reference, the corresponding degree formula on H is

    (D-2H)H=n+2b+2delta_H+deg Z_H,                    (H2.4)

where Z_H is the zero divisor of N_H/T->L_H. Indeed
deg L_H=-(4+t-b),
2g(H)-2=2(t-b)-2delta_H,
and adjunction gives (D-2H)H=-(2g-2)-H^2.
The degree of the spectral normalization conductor is 2delta_H.

## 3. Immediate constraints on common cubic zeros

Since g(H)>=1 and delta_H,n>=0, (H2.1) gives b<=2.
If b=2, all terms are forced:

    g(H)=1, delta_H=0, n=0, t=2,
    Gamma_H=2xi, Gamma_R=xi-2F,
    R^2=-deg Z_R,
    (D-2R)R=2+deg Z_R.                               (H2.5)

Thus the elliptic spectral curve is smooth and disjoint from the
rational spectral section. The following lemma excludes a direct
contact of their actual curves H and R on T. It does not identify
an intervening exceptional or vertical chain with a direct contact.

## 4. Direct-contact obstruction for disjoint spectral images

Assume Gamma_H and Gamma_R are disjoint, and suppose H and R meet on
T. Since the reduced pole support is SNC, take local coordinates
(u,v) with H=(u=0), R=(v=0). There is no third pole component through
their intersection. The residue two-form therefore pulls back as

    omega=unit * du wedge dv/(u^2 v^2).                (H2.6)

Let A=(x=y=0) in actual ambient coordinates, and choose z as a local
coordinate of A at the image point. Because R->A is an isomorphism,
the linear term z_1 of z(u,v) is nonzero. Both x and y vanish on H and
R, so write

    x=uv A(u,v),    y=uv B(u,v).

If either A(0,0) or B(0,0) were nonzero, the two limiting normal
directions would coincide. Disjointness of the spectral images thus
gives A(0,0)=B(0,0)=0. On the point blowup e of (u,v), let

    m=min(ord_e x,ord_e y)>=3,    ord_e z=1.

The cubic normal tensor at the image point must vanish. Otherwise
its distinct root clusters give actual analytic factors of f by
Weierstrass preparation and Hensel factorization in a normal chart.
The distinct limiting directions of H and R put them in different
factors, hence in different local normalization components. They
could not meet in one point of T, whose germ maps to one local
normalization component. This factorization uses the nonzero cubic
and the distinct root clusters only; it does not require all three
roots to be distinct.

It follows that, for f=F3(x,y,z)+O((x,y)^4), every coefficient of
F3(x,y,z) vanishes at z=0. Since f lies in (x,y)^3,

    ord_e(f_x composed rho)>=2m+1,
    ord_e(f_y composed rho)>=2m+1.                    (H2.7)

Choose one minimal-order normal coordinate, say x, whose leading
homogeneous term x_m is nonzero. It is divisible by uv. It cannot
be a scalar multiple of z_1^m: no nonzero power of a linear form is
divisible by both u and v. Therefore dx_m wedge dz_1 is nonzero,
and the point-blowup order is exactly

    ord_e(rho^*(dx wedge dz))=m.

The actual residue equality omega=-rho^*(dx wedge dz)/(f_y composed
rho), together with (H2.7), gives pole order at least m+1>=4 on e.
But (H2.6) gives exactly pole order three: du wedge dv gains one
exceptional factor, while u^2v^2 has order four. This contradiction
proves that H and R do not meet directly.

In particular, in the b=2 case deg Z_R cannot be zero. Otherwise
R^2=0; a component of a ruling fibre with square zero is the whole
smooth fibre, so it meets the section H directly. Thus

    b=2 => deg Z_R>=1 and R^2<=-1.                    (H2.8)

This auxiliary route reaches a genuine intervening vertical chain.
The completed two-junction proof avoids identifying it with a direct
contact: the descended ruling supplies the other junction, where the
actual H and R normalization preimages are separated.

## 5. Junctions with another branch of multiplicity at least three

Let C' be another local critical-curve branch through a point of the
smooth A, and suppose its generic normal multiplicity is at least
three. Every ambient second derivative of f vanishes on C'.
Parameterize it and write (a,b)t^q for its first nonzero normal
displacement (x(t),y(t)) from A. In the normal Hessian of
f=F3(x,y,z)+O((x,y)^4), the leading term on that arc is the Hessian
of F3(x,y,0) evaluated at (a,b), times t^q. Hence

    Hess(F3)(a,b)=0.

A nonzero binary cubic with this property is a cube: in coordinates
with (a,b)=(1,0), its x^3,x^2y,xy^2 coefficients are all zero. P4R.19
excludes that nonzero cube. Thus the entire cubic normal tensor
vanishes at the junction. This argument also includes tangent
intersections, since it uses the first nonzero normal displacement.

Two distinct such junctions force b=2 and the exact configuration
(H2.5)--(H2.8). The subsequent complete proof in
`part4_d4_two_junction_closure.md` uses that bound and the separate
normalization preimages at the other junction. No unproved chain
identification is used in the completed exclusion.
