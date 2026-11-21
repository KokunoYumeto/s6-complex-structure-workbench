# Paper I: comparison of push A2.1 and A2.2

## Chronology and scope

The preread derivation was frozen at **2026-11-21T02:44:27.950775Z**, SHA256 `b147a8c43570f65566c645047d4d4221d5f092ec9a21a4b50447ecc30dfd8bad`. The freeze record binds the statement-only intake, dependency statements, derivation and new computation files. Only afterward were the target proof bodies opened: A2.1 original lines12010–12068 and A2.2 lines12091–12167. Their full text and opening timestamp are in `S6_SERIES_PUBLISH_I_push_A2_printed_proofs.json`.

Allowed input exposure is explicit: I read the setup and A1.2's full construction proof, original lines11877–11992. Consequently this is not a fresh reproof of A1.2's compact plumbing, covering action, or finite caps. No source target proof step was exposed by the earlier isolated program-name scans; their printed source lines do not intersect these target proof ranges. Target statements and their cited inputs were extracted without following proof text.

## A2.1: PASS

The six rays and chosen bottom diagonal match exactly. The preread computation found twelve nondegenerate tetrahedra, all unimodular, six triangulations, three retaining BC, and precisely two satisfying the G1 side-face identification. Its three BC rows agree entry-for-entry with the printed table, including the excluded middle row. The paired left/right diagonals are CE/DE and AF/BF.

The preread ray argument matches all three exclusions in the printed second step: a ray over the base interior produces a dimension-three fibre component; a ray on the u=0 face violates the fixed boundary; a q=0 ray of reduced u-height one is already an existing rho_l. The derivation also explains why no nonsimplicial coarsening with those boundary and period constraints survives: an interior face extending BC contains E or F and forces one of the two full patterns. Direct local monomial products establish the converse flatness, without relying solely on the phrase “saturated image.”

The independently chosen infinite-refinement construction uses the same valid orbit of maximal cones as the printed proof, not the historical intersecting two-face attempt. The new rays are `(m,m,3m,1)`, the basis replacements stay unimodular, the bottom stays fixed, and all u-heights remain one. Period translates have disjoint maximal interiors. This proves the third assertion and explains its failure of joint flatness.

### Different-method computation requirement

The first new program was written and run before the proof was opened, without reading or importing the historical program. However, the printed proof then revealed that the historical program also used combined barycentric-halfspace intersection vertices. Therefore I do **not** describe that first enumeration as a different-method computation.

I instead wrote and ran `S6_SERIES_PUBLISH_I_push_A2_staircases.py` after comparison. It uses maximal chains in the Boolean lattice of the three lower prism vertices and Smith normal form, not intersection enumeration. Here is its completeness argument. At generic base barycentric coordinates lambda_i, a nondegenerate prism tetrahedron has one vertical vertex pair i and one vertex over each other base vertex. Its vertical intersection is the interval from sum_(j in S)lambda_j to that sum plus lambda_i. A triangulation has three tetrahedra by normalized volume. Covering the vertical unit interval forces their endpoints to concatenate from the empty subset to the full subset, adding one coordinate each time. There are exactly 3! maximal chains. Constructing their tetrahedra and imposing BC and the G1 face map gives counts six, three, two again. This is a genuinely different mathematical and computational method, explicitly **after** printed-proof exposure.

## A2.2: PASS for the complete stated theorem

The frozen derivation covers every assertion in the theorem: both smooth total spaces, properness, joint flatness, the exact nonzero-u family, reduced irreducible central fibres, smooth double S with no triple points, the two normalization modifications, the unchanged sections and their gluing by T, and the trivial normal product/T1.

The explicit model starts with the blow-up of `(x,u)` in `xy=uzv`. Its charts are `u=ax,y=azv` and `x=tu,ty=zv`. The selected incidence equations `t lambda=v mu,z lambda=y mu` yield ray cones ABCF,ABEF,BCDF. Swapping the branch and the incidence choice gives ABCE,BCDE,CDEF. Thus the preread calculation identifies the precise morphism from the written blow-up/resolution charts to the two fans, including preservation of BC. The second new program recovers all local map exponents by character-lattice pairing and checks Smith invariants, disjoint q/u supports, exponents zero or one, and at most two u factors. This supplies a different-method verification of the local equations beyond direct symbolic substitution.

The normalization chart `(y,zv)` blows up to `y=Azv` and `By=zv`; the latter has a unique nondegenerate quadratic node. The section A=0 avoids it. The global unique-node assertion uses the one node of the I1 fibre in the input construction. The exact normal-product isomorphism is `J(-S_infinity) -> O`, given inversely by the nowhere-vanishing section phi of J(-S_infinity). T preserves that fibre divisor. This agrees with the printed proof's normal calculation and fixes its coordinate direction.

### Additional proof assertions: exposed comparison only

The printed A2.2 proof also describes the exceptional fibre over the node as a chain of two projective lines and gives a crepant/flop comparison. Those additional assertions were not explicitly derived in the frozen statement-directed record. They receive **no targeted credit**.

I checked them after reading. In the selected normalization resolution chart `v=t b,y=z b`, the inverse image of `(y,z,v)=0` has `z=0,tb=0`: the strict transform and the small-resolution exceptional line meet once; together with the complementary chart they are two P1s. For crepancy, the hypersurface residue `dx wedge du wedge dz wedge dv / x` becomes a nonvanishing coordinate volume form in the three smooth charts: respectively `dx wedge da wedge dz wedge dv`, `dy wedge du wedge dr wedge dv` up to sign, and `dt wedge du wedge dz wedge db` up to sign. The opposite branch has the same calculation after exchanging x,y. At a smooth point of S_infinity, the common local equation is the ordinary threefold node `xy=uq` times the transverse curve coordinate; the two displayed small resolutions give its standard flop. At the nodal point, the comparison is exactly the two prism fans already computed. This is a scoped exposed reread, not a newly blind proof of an added theorem.

## Outcome and limits

No false assertion, incompatible constant, coordinate error or counterexample was found in these two target statements. No main TeX was edited. The stronger second sentence of A2.1 is read within the already specified period-invariant class; explicitly repeating “period-invariant” would improve clarity without changing that scope. Program paths and historical correction prose remain presentation matters for the publication pass.

Recorded events: two scoped targeted proof checks of the stated results; one new computation event for the genuinely different Boolean-chain/Smith/character method, with its post-reading timing stated. The first same-method preread program and the exposed extra A2.2 paragraph are retained as evidence without separate independent or computational credit.
