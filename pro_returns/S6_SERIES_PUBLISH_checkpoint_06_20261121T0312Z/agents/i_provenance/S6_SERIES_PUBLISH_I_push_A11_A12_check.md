# Statement-first checks of push A.1.1 and A.1.2

## Result

A.1.1 passes in full. A.1.2 passes as a theorem, including the exact global pinching, flatness, properness, chosen curve and normal bundle, with one correction to the printed proof's final small-resolution charts. The statement is unchanged.

The complete independent derivations were frozen at 2026-11-21T02:36:21.413731Z with SHA256 cab50d1206590b4b6bdfb70a7ef59fa2c436691383132e0ba630d6e56ce31d2b. Only then were both entire printed proofs opened. Their source blocks and hash are retained in the printed_proofs JSON. The newly written exact computation also ran successfully; its first attempt passed the mathematical assertions but failed JSON serialization of a SymPy integer, corrected before the successful saved run. No attached program was rerun.

## A.1.1 comparison

The independent fan-intersection argument covers the collapsed hq=0 faces as well as the interior rectangles. Its semigroup proof uses integral maximal minors, the unique primitive relation, and normality of the hypersurface, whereas the printed proof explicitly subtracts x or y. Both prove the same integral monoid. The five character vectors, q=zv and xy=uzv agree exactly. The fresh computation verifies lattice index1, primitive kernel (1,1,-1,-1,-1), and the joint-base Groebner basis (xy-uq,zv-q). Normality is proved in the frozen derivation by the codimension-three singular locus and the hypersurface criterion; it is not attributed to a finite sample enumeration.

## A.1.2 comparison, Steps1–6

The frozen construction uses the same actual normal lines L_x and L_(Tx)^-1 and derives the bundle-valued equation a_x b_(Tx)=u phi_x. Consequently its overlap is a_x=u phi_x a_(Tx), covering T^-1, exactly as in printed Steps1 and4. Both constructions choose disjoint collars using a uniform Hermitian bound on compact S. The printed core radii r,2r and compact representatives3r/2,7r/4 are a more explicit choice of the nested radii in the independent construction. I read and checked their inequalities: every point outside the compact core lies in the compact node representative, and vice versa, using |u| ||phi||<r². The separated collars give the stated Hausdorff quotient.

The independent complete-intersection argument and printed Step3 both give joint flatness over B×Delta_u, including the nonreduced finite Kodaira fibres. Smoothness of S supplies the regular local base; the fibres S_t need not be smooth. At u=0 both conductor maps are exactly s0(x)~s∞(Tx). At the unique node of S_infinity the actual coordinates q=zv give xy=uzv. For nonzero u its Hessian determinant is u², confirming the ordinary double point. The smooth points of that fibre have xy=uq and are smooth for nonzero u. Thus there is exactly one node. The independent toric comparison uses the common dense torus and the period-equivariant fan refinement. Printed Step6 additionally spells out its Tate-cover coordinates and the two unfolded indices; these were read and agree with the same monomial actions and bundle-valued gluing. Neither argument uses the polarized survey to supply properness for unrestricted units.

## The selected-diagonal error in Step7

The printed coordinates x=za and z=xb have character a=x/z, of valuation y2-y1. Their fan subdivision uses the diagonal [0,e1+e2]. The selected A2 subdivision in the statement uses [e1,e2], of direction e1-e2. This is a concrete wrong intermediate identification; it does not refute the unchanged existence, curve-direction, or normal-bundle theorem.

For the selected curve fix u≠0 and set Y=y/u. The exact charts are

* U_a=(v,Y,a), with (x,y,z,v)=(av,uY,aY,v).
* U_b=(x,z,b), with (x,y,z,v)=(x,ubz,z,bx).

Their transition is b=a^-1 and (x,z)=a(v,Y). The new character a=x/v has valuation y1+y2-hq. Fresh inversion of the two unimodular character matrices gives upper rays {(e1,1),(e2,1),(e1+e2,1)} and lower rays {(0,1),(e1,1),(e2,1)}. Their common edge is exactly [(e1,1),(e2,1)]. Both substitutions satisfy xy=uzv identically. The exceptional P1 has coordinates a,b, and the two normal components transform by multiplication by a; this is O(-1)⊕O(-1).

There is an exact comparison of the two resolutions. Both map to the same node xY=zv and are isomorphic over its complement of the vertex. Write its rank-one matrix as [[x,z],[v,Y]]. The selected resolution records its row proportionality [a:1], while the old one records the column proportionality [c:1]. Their common resolution records both factors, namely the line bundle O(-1,-1) over the Segre quadric P1×P1, with the evaluation map lambda·(a0,a1)^t(c0,c1). Projection to either factor gives the corresponding small resolution; over the zero matrix the projections contract opposite rulings. This explicitly describes the flop and proves how the two charts are related. No categorical distinction is asserted without this map.

The error has a separate scoped error record. No fictitious refined theorem is introduced and no theorem is marked refuted. The targeted check's outcome records the proof correction. The independent derivation and new computation share one evidence group; associations to the two statements do not create two independent executions.

## Editorial and provenance scope

The correction guard changes only the exact selected-diagonal calculation in Step7. Full old and new text is retained in the guarded JSON. Primary Engel section2 was an input, with the exact L,T,phi action retained; source opening receives no mathematical event. These checks do not claim a final PDF-page read or independent verification of every cited general theorem.
