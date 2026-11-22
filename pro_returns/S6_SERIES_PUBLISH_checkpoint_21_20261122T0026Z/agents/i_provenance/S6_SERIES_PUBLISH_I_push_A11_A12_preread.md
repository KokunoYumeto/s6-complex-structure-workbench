# Independent statement-first derivations: push A.1.1 and A.1.2

The target statements and preceding definitions were read from the separate statement intake. Neither target proof has been opened. The primary Engel source, section2, lines335–556, was read as an input: its exact map is phi_x:L_(Tx)→L_x, its divisor is the nodal fibre S_infinity, and its punctured quotient uses a_x=u phi_x a_(Tx). The argument below is frozen before target-proof comparison. Prior editorial exposure includes other Paper I constructions but not either push A.1 proof.

## A.1.1: fan and saturated semigroup

Use N=Z^4 with coordinates (y1,y2,hq,hu). The cells are the closed intervals y1 in [k hq,(k+1)hq], y2 in [l(hq+hu),(l+1)(hq+hu)], with hq,hu nonnegative. Adjacent cells meet at the indicated endpoint face. Nonadjacent k-cells meet only on hq=0,y1=0; nonadjacent l-cells meet only when hq+hu=0, hence at the origin. Intersections involving both constraints are their common faces. Thus cells and all their faces form a fan. G1,G2 are determinant-one integral shears and send indices (k,l) to (k+1,l),(k,l+1); they commute.

For P00, hq≥0 is redundant. Its five facet normals in M are
x=(0,1,0,0), y=(0,-1,1,1), z=(1,0,0,0), v=(-1,0,1,0), u=(0,0,0,1).
They span M and satisfy the single primitive relation x+y=z+v+u. Their semigroup ring is C[x,y,z,v,u]/(xy-uzv). The binomial is irreducible and its primitive exponent relation generates the rank-one lattice kernel. Its singular set is x=y=0, uv=uz=zv=0, the three coordinate axes in a four-dimensional hypersurface. The hypersurface is Cohen–Macaulay and regular in codimension1, hence normal. Thus the semigroup is saturated in the full generated lattice and equals P00^vee∩M. This proves the integral chart identification. The character q is (0,0,1,0)=z+v, so q=zv. The singular locus proves non-smoothness. For fixed nonzero u, scale y by u^-1; xy=zv has the unique ordinary double point x=y=z=v=0.

## A.1.2: exact global plumbing

The input is the compact smooth rational elliptic surface pi:S→B, T=t_(6P), L=O(P-O), J=L⊗T*L^-1, and the specified phi with divisor S_infinity. In R=P_S(O⊕L), the zero and infinity normal lines are L and L^-1.

At the identification s0(x)~s∞(Tx), the normal coordinates are a_x in L_x and b_(Tx) in L_(Tx)^-1. Their tensor product lies in J_x. The intrinsic smoothing equation is a_x b_(Tx)=u phi_x. It respects every change of frame because both sides are J-valued. Since b_(Tx)=a_(Tx)^-1 on the punctured line, the transition is exactly a_x=u phi_x a_(Tx), the primary linearization covering T^-1. At u=0 its two branches recover precisely Q with normalization R and the prescribed conductor map. This establishes the actual comparison map and its direction.

Choose Hermitian metrics, disjoint zero/infinity tube radius r in R, C=max_S||phi||, and delta C<r²/8. Glue the chart {ab=u phi, ||a||<r, ||b||<r} over S to the unchanged R-core along the a-annulus r/2<||a||<r and the b-annulus, using T on the latter. The other coordinate has norm<r/4 on either annulus; consequently the two ends cannot produce an additional double boundary identification. The bundle transitions preserve the equation and give holomorphic overlaps.

This gluing is Hausdorff: in a finite bundle atlas, a sequence leaving a plumbing chart across its outer a-boundary has its unique limit in the retained R-annulus, and similarly for b. A sequence leaving an R-chart toward a removed tube has its unique limit in the corresponding plumbing chart. The bound on the other coordinate separates these cases; the overlap graphs have no extra double limits. Over a closed smaller u-disc, the compact R-core and closed radius-r plumbing disc bundles over compact S cover the family. At radius r the annular maps extend into the R-core. Hence the family is proper over Delta_u, and its map (f,varpi) to B×Delta_u is proper. The function f is well-defined because T preserves pi.

Away from S_infinity, phi is a unit and ab=u phi is smooth after eliminating u. At a smooth point of S_infinity its equation is ab=u q times a unit. At the node, the actual smooth surface coordinates z,v satisfy q=zv; absorb the unit into a normal coordinate and obtain xy=uzv, q=zv. The latter is the normal reduced fourfold proved in A.1.1. Thus the total space is reduced.

Every local total ring is Cohen–Macaulay, being this hypersurface over a smooth surface chart with u. All fibres over (t,u) have pure dimension2: at u=0 they are the pinched ruled surfaces over the one-dimensional S_t; away from infinity at u≠0 they are the punctured-line quotient over S_t; at infinity the chart is xy=uzv,q=zv. The base B×Delta_u is smooth of dimension2 and the total spaces have dimension4. The local Cohen–Macaulay flatness criterion therefore gives flatness. In the nodal chart the equations xy-uq and zv-q also have relatively prime leading monomials xy,zv over C[q,u], so the monomials without either factor form a free base-module basis; the analytic regular-sequence argument gives the same local flatness.

For u≠0, the punctured part is Engel's X°(u) through the exact transition above. At the cusp the square fan of A.1.1 is obtained from Engel's chosen A2 triangulation by forgetting the diagonal [e1,e2]. Fan refinement induces the proper toric contraction, is the identity on the common torus, and commutes with both period translations. It therefore descends and glues to the identity on X°(u). The square diagonals form one Z² orbit, so one rational curve is contracted and one node remains.

The local normal bundle and the direction can be proved explicitly. In xy=zv the resolution charts for that diagonal are
U_a: coordinates(v,y,a), x=a v, z=a y;
U_b: coordinates(x,z,b), v=b x, y=b z.
On their overlap b=a^-1 and (x,z)=a(v,y). Their cocharacter regions are y1+y2≥hq and y1+y2≤hq, so the common diagonal is [e1,e2], of direction e1−e2. The exceptional curve is v=y=0 and x=z=0 in the two charts, hence P1 with coordinates a,b. Each normal fibre coordinate transforms by multiplication by a, the tautological O_P1(-1) transition. Thus the normal bundle is O(-1)⊕O(-1). These charts contract only their zero section to the ordinary double point. Their identical fan charts and identity on the dense torus identify the resolution with Engel's chosen filling.

The direct compact-core construction supplies properness. No extension of the polarized symmetric hypotheses in the Mumford survey to arbitrary nonsymmetric unit matrices is assumed.

## Scope

A.1.1 has a complete independent statement-first proof. A.1.2 has a complete independent statement-first construction and comparison, using Engel's named L,T,phi and punctured quotient as primary inputs. Neither target proof was used. Primary-source reading has no mathematical event. A new exact semigroup/incidence calculation may be logged separately with the same evidence group after execution.
