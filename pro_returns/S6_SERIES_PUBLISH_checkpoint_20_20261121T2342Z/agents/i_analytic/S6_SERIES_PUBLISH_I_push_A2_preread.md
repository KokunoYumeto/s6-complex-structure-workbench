# Paper I: preread derivation for push A2.1 and A2.2

## Access and scope

The own printed proof of neither target has been opened. I extracted only the two target statements and the input statements push A1.1 and A1.2. I then read the setup preceding A1.1 and the complete A1.2 proof as an allowed dependency input: its explicit plumbing, compact representatives, joint flatness, toric covering, and relation to the fixed bottom diagonal. The dependency proof occupies original lines 11877–11992; the target A2.1 starts at line11996. A1.2's local small-resolution description is an input, not a newly independently proved external theorem.

Earlier general program-reference scans displayed isolated references, not either target's own printed proof steps. There is no recalled or recorded earlier exposure to those target proofs. The original source SHA256 is `d2e6c3bec1500144bfc0ef85e636ded534f2abc998cf58fdaf521b1e8a183169`. This record is to be frozen before reading the target proofs. The requested credit is a targeted check of the steps actually derived below, with the dependency input disclosed; no claim of an independent reconstruction of the entire plumbing construction is made.

## A2.1: the fundamental prism

Use lattice coordinates `(y1,y2,hq,hu)` from A1.1. The six rays of P00 are

```
a=(0,0,1,0), b=(1,0,1,0), c=(0,1,1,0), d=(1,1,1,0),
e=(0,0,0,1), f=(0,1,0,1).
```

The slice hq+hu=1 is the triangular prism with coordinates `(y1,y2,hq)`, inequalities `0<=hq<=1`, `0<=y1<=hq`, `0<=y2<=1`. Its normalized volume is three. The specified bottom diagonal is b–c: its direction is e1−e2, as in A1.2. Thus the bottom triangles are abc and bcd.

The G1 face identification sends the left quadrilateral `(a,c,e,f)` to the right quadrilateral `(b,d,e,f)` by `a→b,c→d,e→e,f→f`. The other two faces are triangles abe and cdf, identified by G2. Consequently only the paired left/right quadrilateral triangulations impose an additional compatibility condition.

A new program independently enumerates all tetrahedra on these six vertices. It computes their intersections by exact active-facet vertex enumeration, retains precisely the face-to-face triples of total normalized volume three with exterior faces in the prism boundary, then applies the fixed-bottom and G1 matching conditions. This differs from relying on any historical fan program. It gives six triangulations in total, three with bottom b–c, and two with the period matching:

```
+ : abef, abcf, bcdf;
- : abce, bcde, cdef.
```

All maximal determinants have absolute value one. Every maximal cone contains either one or two u-height-one rays, and its other rays have q-height one and u-height zero. These computations establish the finite tetrahedral classification.

The classification also excludes an additional nonsimplicial subdivision with the same conditions. The interior bottom edge b–c must extend into an interior separating face. With no new rays that face contains e or f. The face bce forces the left diagonal ce, hence the matching right diagonal de, and the second displayed triangulation. The face bcf forces the right diagonal bf, hence the matching left diagonal af, and the first triangulation. Keeping both choices would require crossing faces and a new ray. Thus the period condition prevents coarsening an interior face while retaining the specified bottom diagonal.

## Why joint flatness and reduced u leave no new rays

A new ray with both base heights positive gives a toric divisor over the base origin. The total local toric space has dimension four, so that divisor has dimension three, whereas the general joint fibre has dimension two. This contradicts flatness over the smooth two-dimensional base. A ray of u-height zero lies in the prescribed bottom fan and cannot be added while retaining that triangulation. For a ray of q-height zero the defining inequalities force y1=0. Reduced u means its primitive u-height is one, hence it is `(0,l,0,1)` for an integer l; these are exactly the existing period translates of e. The support has no nonzero vector with both heights zero. Therefore the flat/reduced/boundary conditions introduce no new rays, and the preceding classification applies.

For either displayed smooth fan, take the four dual affine coordinates of a maximal cone. The functions q and u are products of disjoint sets of these coordinates, each to exponent one. The respective numbers are (3,1) or (2,2). Each monomial map to a one-dimensional smooth base is flat, and their product is flat over the bidisc. This also verifies joint flatness directly for both selected fans.

## Infinitely many reduced-u invariant refinements

Select a maximal cone of either fan with exactly one u-ray; its other three rays have u-height zero. Star-subdivide every period translate of its interior by the sum of its primitive generators. These interiors are disjoint and have trivial period stabilizers, so the operation is period-invariant. A sum of a lattice basis is primitive, and replacing any one basis vector by that sum has determinant ±1. The new ray has u-height one. In the child cone containing the same three bottom rays, repeat. After n steps its top ray is `top+n*(bottom1+bottom2+bottom3)`. Its u-height stays one and its q-height grows by three each time. The program verifies the determinant identities symbolically in n. Each finite stage is smooth, retains the bottom triangulation, and has reduced u-central divisor; the ray sets distinguish infinitely many stages. These refinements have divisors over the base origin, in agreement with the failure of joint flatness.

## A2.2: explicit modifications and the fixed diagonal

In the node chart of A1.1 use `xy=uzv`, `q=zv`. The valuation morphism to the cocharacter lattice is

`(val z, val x, val z+val v, val u)=(y1,y2,hq,hu)`.

Blow up the Weil ideal `(x,u)` and take the strict transform. One chart is

`u=ax, y=azv`, with free coordinates `(x,a,z,v)`.

The other chart is `x=tu`, with equation `ty=zv` and coordinate u. Resolve this conifold by the incidence equations

`t*lambda=v*mu, z*lambda=y*mu` in P1.

On lambda=1 the free coordinates are `(u,v,y,r)`, where `t=vr,z=yr`; on mu=1 they are `(u,t,z,b)`, where `v=tb,y=zb`. Thus q is respectively `vy r` and `tz b`, while u is a free coordinate. The program computes the divisor valuations of these three affine charts and obtains exactly `abef,bcdf,abcf`. This proves that the resolution uses the stipulated bottom diagonal b–c, not merely one of the two conifold resolutions.

For the other model blow up `(y,u)`. Interchanging x and y sends the bottom diagonals to each other, so the conifold incidence choice must also be interchanged. The resulting valuation cones are exactly `abce,bcde,cdef`. This explicit coordinate transport identifies both abstract subdivisions with the two section modifications. During development, before either target proof was read, I checked both incidence choices; the first valid conifold choice gave the opposite bottom diagonal, and the valuation computation selected the one written here. This is recorded as a preread development choice, not a disagreement with a printed proof.

Each blow-up and incidence resolution is proper: the incidence description is closed in the appropriate product with P1, and the blow-up is projective. The local descriptions glue to the period-invariant toric subdivisions. The disclosed A1.2 covering construction supplies free, properly discontinuous deck actions and the compact plumbing quotient; refining equivariantly keeps those local covering charts. Hence properness descends and composes with the proper map in A1.2. The modifications are the identity away from the cusp locus, where the same plumbing and finite caps remain.

## Smoothness, flatness, and the central fibre

Every displayed chart has four free holomorphic coordinates. The first has `u=ax,q=zv`; the other two have u as one coordinate and q a product of the other three. These are the disjoint-product flat maps found combinatorially. Outside the cusp, phi does not vanish and the plumbing is `ab=u` over the smooth surface S; its joint map is the product of the flat elliptic-surface map S→B with the flat nodal map `(a,b)→ab`. This includes the nonreduced special fibres of S→B: the total surface S is smooth and the projection is flat. The total spaces are therefore smooth and their joint maps flat. For u nonzero the bottom restriction is precisely the prescribed small resolution of the one node of A1.2, hence the resulting family is the original specified untwisted X(u).

At u=0 the first chart has the reduced normal-crossing equation `a*x=0`, with double locus `a=x=0` and free coordinates `(z,v)`. The other charts have smooth central equation u=0. There are at most two local components, so no triple locus. The top rays form one orbit under the second period; accordingly the central fibre is globally irreducible. The double locus is the same smooth surface S, and its gluing remains T because the modifications use the original plumbing identifications.

To identify the normalization explicitly, consider the original branch x=0, with local coordinates `(y,z,v)`. Blowing up its ideal `(y,q)=(y,zv)` has charts

`y=a*zv` and `t*y=zv`.

These are exactly the component charts above. Thus the normalization is the blow-up of R along S_infinity in the corresponding section, followed by the chosen small resolution. The second chart has one ordinary double point: its gradient is `(y,t,-v,-z)`, vanishing only at the origin, and its quadratic form is nondegenerate. The I1 fibre has one node in the quotient, so there is one such point globally. The section's proper transform lies in the first chart at a=0; blowing up its Cartier divisor S_infinity leaves it isomorphic to S, and the small-resolution node is away from it. The other section is unchanged. Reversing the two sections gives the other normalization.

Finally the setup fixes the exact line-bundle identity

`J=L tensor T^*(L^(-1))=O(S_infinity)`

and a section phi with precisely that divisor. Blowing up S_infinity in one section tensors its normal bundle by O(−S_infinity). The other normal bundle is unchanged; T preserves S_infinity because it lies over the same base point. The product on the glued double surface is therefore `J tensor O(−S_infinity)`. The exact trivialization sends 1 to phi, interpreted as a nowhere-vanishing section of J(−S_infinity). For a double normal crossing the T1 line is this product, so T1 is O_S. This calculation also agrees with the local smoothing coordinate u=ax.

## Computational scope

The new program computes all finite fan determinants, the exhaustive face/volume classification, exact matching of the two period-compatible fans, symbolic repeated-star determinants, the blow-up identities, and the ray valuations identifying both incidence choices with the fixed bottom. No historical program is imported or run. It does not recreate the global A1.2 compact plumbing proof. The first development run used structural equality between an expanded expression and a factored expression; replacing it by expansion of the difference corrected the program assertion, with no mathematical change. The failed initial source and development note are retained.

Pending next step: freeze this file and completed outputs, then and only then read each target's own printed proof and compare every corresponding step. No check event is credited before that comparison.
