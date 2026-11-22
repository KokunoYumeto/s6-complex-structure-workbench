# Independent derivation: 02WP / night:P4.18

The statement and its cited-input statements P4.15/P4.16 have been read; all target proofs remain unopened. The construction below proves the all-parameter spherical obstruction directly and does not assume a rank condition on the normalization.

## 1. A finite map of the actual affine nearby fibres

For a≥2 and b,c≥1 write

    M={x^a-y^b z^c=1},       Q={x^a-u v=1}.

Both surfaces are smooth. On M, a zero y or z forces x^a=1 and a nonzero x derivative; when both are nonzero, a y or z derivative is nonzero. There is a finite proper holomorphic map of degree bc

    p:M→Q,           (x,y,z)↦(x,u=y^b,v=z^c).

Its generic fibres have exactly bc points, all orientation preserving under the complex orientations. Finiteness follows algebraically from the monic equations for y and z and also directly from properness of the power maps.

Choose two consecutive roots of x^a=1 and a simple path between them containing no other root. As derived explicitly in the parallel independent P4.17 calculation, the locus over that path with |u|=|v| and uv=x^a-1 is a compact smoothly embedded Lagrangian sphere K in Q. Direct cancellation of the Kähler form on its circle-over-interval parameterization proves the Lagrangian assertion, and the complex-structure normal-bundle map gives K²=-2.

## 2. The pullback class is spherical, including all branch singularities

Over the interior of the path, the inverse image of K is described by the angle equation `bθ+cψ=arg(x^a-1)` on a two-torus. It has d=gcd(b,c) circles. The deck group Z/b⊕Z/c acts, and continuation around the circle is addition by (1,-1). That permutation has exactly d orbits, each of length bc/d. At each endpoint both y and z vanish, so every circle collapses to a point. The closure of each cylinder is the continuous image of S², with its orientation pulled back from K off the endpoints. It can have an isolated nonsmooth parametrization at the endpoint, which does not affect its fundamental two-cycle.

Let α∈H_c²(Q;Z) be the Poincaré dual of K. The class dual to p*α is the sum of these d oriented spherical fundamental classes. Here is a local justification at the only two possible nonsmooth points. Near an endpoint Q has coordinates (u,v), since the x derivative is nonzero. The inverse image of a sufficiently small coordinate polydisc is the polydisc `|y|<ε^(1/b), |z|<ε^(1/c)` in the smooth source coordinates (y,z), and is contractible. Away from these two polydiscs, the inverse-image cylinders represent the ordinary pullback Thom class. Perturb the two target caps to be transverse to p while keeping their boundary circles fixed. The resulting pullback caps define the Gysin cycle; their difference from the original collapsed cylinder caps is a closed two-cycle in those contractible polydiscs and is zero in homology. Thus the asserted class identification is exact, including at the isolated parametrization singularities.

A sum of finitely many spherical classes in a connected space is spherical: choose their common endpoint as base point and compose the pinch map from S² to a wedge of d spheres with the d displayed maps. Write β for this spherical class in H2(M;Z). Properness and the degree of p give

    β² = integral_M p*α cup p*α
       = bc integral_Q α cup α
       = -2bc.

The equality is the change-of-degree formula for the compactly supported top-degree class α cup α. The value is nonzero for every b,c≥1. This suffices for the statement; no claim about a complete intersection basis for M is needed.

## 3. Transport into the actual torus fibre

The polynomial g=x^a-y^bz^c is weighted homogeneous of positive weights `(b+c,a,a)` and degree D=a(b+c). A germ with common multiplicity m has equation `F=u g^m`. Choose `lambda=u^(1/(mD))` locally and use the biholomorphism `phi(x_j)=lambda(x)^(w_j)x_j`. Its derivative is diagonal with nonzero entries at the origin, and `(g∘phi)^m=F` exactly.

Weighted scaling takes the compact representative of β and a compact neighbourhood of it from g=1 into an arbitrarily small coordinate ball in g=ε^D. Composition with phi^-1 places it inside the actual fibre F=ε^(mD). Compactly supported Poincaré duality and extension by zero preserve its square -2bc under this open embedding. On the other hand the composite spherical map into the nearby complex two-torus is nullhomotopic because that torus has universal cover C². Its global H2 class is zero, forcing square0. This contradiction proves every asserted exclusion, for every common multiplicity.

## 4. The displayed example and its differential

For `x²-z³y⁴=0`, the map

    nu:C²_(y,t)→S,         (y,t)↦(x=y²t³,y,z=t²)

is finite and birational. The element t satisfies the monic equation t²=z and belongs to the meromorphic field as x/(y²z). Its source is smooth and normal, hence this finite map is the normalization. The two derivative columns in the ambient coordinates (x,y,z) are `(2yt³,1,0)` and `(3y²t²,0,2t)`. The three maximal minors are

    -3y²t²,       4yt⁴,       2t.

Their ideal in the smooth normalization ring is exactly (t), since2 is a unit. Thus the rank drops along the whole divisor t=0, with rank1 there and rank2 elsewhere. This proves the normalization and divisorial rank-drop clauses through their actual map, while the preceding finite-map spherical argument still excludes the germ.

## Fresh computation

The prerelease group05 program enumerates the deck permutation orbits for b,c=1,...,8 and checks their count and length against the proved formulas d and bc/d. It also verifies the example normalization and the derivative minors by exact integer polynomial grids with explicit degree bounds, and carries the root-lattice arithmetic of the base matching spheres. Its finite computational scope is distinguished from the all-parameter proof above. No printed target proof or prior routine has been opened.
