# Independent derivation: 02WQ / night:P4.19

The statement and the cited P4.16/P4.18 statements have been read. The target proof and all prior computational routines remain unopened. The normalization, conductor and affine-fibre isomorphism are computed directly below.

## 1. The finite normalization morphism

Let `F=y(x²-zy²)` and let S be its reduced zero germ. It has a planar component A={y=0} and an umbrella component B={x²=zy²}. The normalization is the disjoint union of two smooth planes, with maps

    nu_A:(x,z)↦(x,0,z),
    nu_B:(y,t)↦(yt,y,t²).

The second map is finite because t²=z, and birational because t=x/y in the meromorphic field of B. The smooth source is therefore the normalization. The derivative of F is `(2xy, x²-3zy², -y³)`, so the reduced singular locus is the single smooth curve C={x=y=0}, with coordinate z.

## 2. Both conductor multiplicities

The ring of the umbrella component inside its normalization is `R_B=C{y,yt,t²}⊂C{y,t}`. A monomial y^i t^j belongs to R_B exactly when j is even or i≥1. This also describes convergent power series: separate their even and odd powers of t; every odd part must be divisible by y. Its conductor in C{y,t} is therefore the ideal (y). Indeed multiplying by t tests the only missing generator, and an element belongs to the conductor precisely when both it and its t multiple have no odd coefficient free of y.

For the union, its local ring is the fibre product of the two component rings along their scheme-theoretic intersection. On the plane the other equation restricts to x², so that intersection has ring C{x,z}/(x²). On B the plane equation is y, giving the same intersection ring after y=0. Thus an element supported only on the planar normalization component is a conductor element exactly when its planar function belongs to x² C{x,z}; arbitrary multiplication within that smooth component preserves this ideal.

An element supported only on the umbrella normalization component must multiply every function of C{y,t} into the ideal y R_B. The condition is `h C{y,t}⊂yR_B`. It forces h to be divisible by y; after dividing by y it is the previously computed umbrella conductor condition. Hence h belongs exactly to y² C{y,t}. Conversely every such h has the required product property. The conductor on the full normalization is therefore

    x² C{x,z}  ⊕  y² C{y,t}.

Its divisor has multiplicity2 on each reduced conductor component. The reduced planar conductor maps to C by the identity on z. The reduced umbrella conductor maps by `t↦z=t²`, a finite degree-two map ramified at t=0. These are the exact normalization morphisms proving the stated ramification and multiplicities.

## 3. The actual affine nearby fibre and its topology

On F=1, y is nonzero. Solving the equation gives

    z=(y x²-1)/y³.

Thus the map

    C*×C→{F=1},      (y,x)↦(x,y,(y x²-1)/y³)

is a holomorphic isomorphism with inverse the coordinate projection (x,y,z)↦(y,x). Substitution verifies both compositions and F=1 exactly. The product C*×C deformation retracts onto S¹, by contracting the C coordinate and radially projecting the nonzero C coordinate. Consequently π2 and H2 of this affine nearby fibre are zero. Every spherical class has square0.

The finite conductor map t↦t² and this explicit fibre isomorphism hold for the same germ F. They establish that the stated conductor ramification, by itself, does not supply the nonzero spherical intersection class used in P4.16–P4.18. The assertion has been proved for this exact hypersurface germ and its affine nearby fibre; no additional compact threefold construction is asserted or used.

## Fresh computation

The independently written group05 program verifies the umbrella normalization and the nearby-fibre inverse on exact integer/rational grids. Its conductor computation uses the parity membership rule for the actual subring C[y,yt,t²], testing h and ht in yR_B; the all-exponent derivation above proves the ideal y² and the program checks the stated finite exponent range. Source/output hashes and the prerelease run are in the group05 receipt. No old code was reused.
