# YH statement-directed work before target-proof exposure

Recorded by ii_check_a on 22 November 2026 before the scheduled 00:26 checkpoint. Both A and root have kept the WW and YH target proofs closed. Root contributed the general graph-quotient Euler estimate in messages during this interval; A and root independently found the same local hypersurface argument for its remaining rational-free case. This is an unfrozen working derivation, not a completed independent-check event. A fresh computation and final exact input bindings remain to be written before freeze.

## Exact divisor scope on the Hopf minimal model

Let ν:T→S be the smooth normalization in YH and β:T→H its sequence of point blowdowns to the Hopf minimal model. The canonical conductor divisor D satisfies ω_T(D)=ν*ω_S, and WJ makes this line torsion. Put D0=β_*D. The point-blowup formula and intersection with its exceptional curve show at every step that the new coefficient is μ−1, where μ is the multiplicity at the centre. Thus K_T+D=β*(K_H+D0) as line bundles. Pullback by point blowups is injective on Picard groups, so K_H+D0 is torsion. D0 is effective.

Kill the finite-order line L=ω_H(D0) by its cyclic étale cover: a chosen trivialization L^ℓ=O gives the algebra ⊕_{j=0}^{ℓ−1}L^−j, and the local coordinate satisfies t^ℓ=1. This is finite étale because ℓt^(ℓ−1) is a unit. Take a connected component and then a finite primary Hopf cover. The composite p:H'→H is finite étale, K_H'=p*K_H, and D'=p*D0 is an effective anticanonical divisor. Every multiplicity is unchanged by this étale pullback. The source of the primary-cover input is the actually opened Gauduchon–Ornea original p.1109; the primary contracting normal forms are the actually opened Khaled arXiv2310.05265v2, formula(1) and Theorem2.1, p.5.

On the universal cover C²\{0} of H', an anticanonical section is P(z,w)∂z∧∂w. Hartogs extends the holomorphic function P across 0. The deck generator g imposes P∘g=(det Dg)P.

For a diagonal normal form g(z,w)=(αz,βw), |α|,|β|<1, the Taylor coefficient of z^i w^j can be nonzero only when α^(i−1)β^(j−1)=1. With a=−log|α|>0 and b=−log|β|>0, this implies a(i−1)+b(j−1)=0. If i,j≥1, the only solution is (1,1). Otherwise i=0 gives j=1+a/b, or j=0 gives i=1+b/a. At most one of these extra integer possibilities occurs unless a=b; its complex coefficient equation further requires α=β^r or β=α^r. Thus the forms are:

* a multiple of zw in the nonresonant diagonal case;
* w(cz+dw^r) when α=β^r, r≥2, and the coordinate-interchanged form for the opposite resonance;
* a homogeneous quadratic when α=β; its factorization has one or two linear factors;
* the corresponding pure power when the zw coefficient vanishes.

When |α|=|β| but α≠β, the pure-square coefficient equations fail and only zw remains. For the nonlinear normal form g(z,w)=(β^r z+λw^r,βw), λ≠0, decompose P into weighted-homogeneous pieces of weights wt(z)=r, wt(w)=1. Composition preserves these pieces, and its diagonal eigenvalue on weight k is β^k. The required character is β^(r+1), so only weight r+1 survives. That space is spanned by zw and w^(r+1). Substitution of P=czw+dw^(r+1) forces cλβ=0, hence c=0. This case has one reduced root.

Each listed nonzero zero set has smooth C* components in C²\{0}, disjoint from the other components there. In w(cz+dw^r), c≠0 gives w=0 and z=−(d/c)w^r; their only intersection in C² is 0. A homogeneous quadratic has either a double line or two lines meeting only at 0. The deck action on the parameter of each component is a strict scalar contraction. Its quotient is C*/⟨λ⟩, equivalently C/(2πi Z+logλ Z), a smooth elliptic curve. This describes the actual anticanonical support D', not an arbitrary curve on the surface.

The finite étale descent preserves local smoothness and disjointness of this support. A component orbit maps to one component downstairs; a point with a singular or crossing reduced support downstairs would have the same local germ on an étale lift, contrary to the upstairs description. Each component cover is unramified, and Riemann–Hurwitz makes its quotient elliptic. Therefore Supp D0 is a disjoint union of smooth elliptic curves. No bound on their number is needed for the Euler argument below. The classification also proves that two distinct roots have coefficients one, but that stronger fact is not used below.

## Blowups and the open-stratum Euler number

At every reverse blowup the coefficient is μ−1. Effectiveness puts the centre on the divisor. A smooth coefficient-one centre creates an exceptional curve outside the reduced conductor; a higher-coefficient smooth centre adds a rational leaf; a crossing subdivides its edge. Thus every connected component of D_red is one elliptic root with rational trees attached. Write d for the number of these connected components and v for their total number of rational exceptional components. Each elliptic root has Euler number zero, and each attached rational leaf increases the Euler number by 2−1=1; edge subdivision has the same increase. Therefore e(D_red)=v.

The Hopf minimal model has Euler number zero: its finite primary cover is the Hopf manifold with the homotopy type of S³×S¹, and finite unramified cover multiplies Euler number by the degree. Each of the k point blowups adds one. Hence e(T)=k. Since ν is an isomorphism outside the conductor and has smooth source, C=Sing(S)_red is exactly its image. Therefore T\D_red≅S_reg and e(S_reg)=k−v. Also v≤k, since every rational conductor component is one of the k exceptional curves of β. This proves k−v≥0 without an additional monodromy assumption.

## The graph quotient of the actual pushout

The finite normalization map gives the compact-to-Hausdorff homeomorphism S≅T∪_{D_red} C. The analytic inclusion D_red⊂T is a cofibration, so the double mapping cylinder computes this pushout up to homotopy. The map D_red→C is kept unchanged.

Let r and e denote the numbers of rational and elliptic components of the smooth normalization of C. Every such component is dominated by a component of D_red. Riemann–Hurwitz gives genus at most one. Each elliptic image must be dominated by an elliptic root: a rational tree component cannot map nonconstantly to a genus-one curve. Each root has one irreducible image. Thus e≤d.

Let c be the number of connected components of C and b the sum of the first Betti numbers of their normalization incidence graphs. Give C its homotopy model of normalized surfaces joined by incidence stars. Collapse each normalized surface to its component vertex, obtaining a graph G with c components and cycle rank b. The induced map from a connected component D_a of D_red to G kills its π1: π1(D_a) is generated by its elliptic root, and that root maps through the normalization of one irreducible component of C, which has been collapsed. The map D_a→G therefore lifts to the universal-cover tree of that component of G and is nullhomotopic. Choose the nullhomotopy by contraction of that lifted tree to a fixed vertex.

In the double mapping cylinder, collapse T to a point and use these chosen nullhomotopies on its d conductor-cylinder components. This defines a map to the graph obtained from G by adding one new vertex and d edges, one from the new vertex to the chosen image vertex of each D_a. Every connected component of C receives at least one D_a because D_red→C is surjective. The new graph is connected and has cycle rank b+d−c. Its fundamental group is therefore F_{b+d−c}.

The map on π1 is surjective. Generators for each incidence-graph cycle come from loops in C. The remaining d−c generators are obtained by traversing one conductor cylinder from the T side, a path in the corresponding connected component of C, and another conductor cylinder back, using paths in connected T to close the loop. These loops map to the usual independent added-edge cycles after choosing one attaching edge for each connected component of C. Thus the exact pushout supplies an epimorphism

    π1(S) → F_{b+d−c}.

Y2 makes π1(S) virtually abelian, and every quotient is virtually abelian. A free group of rank at least two is not virtually abelian: its finite-index subgroups are fundamental groups of graph covers, with rank at least two. Consequently b+d−c≤1.

The curve-normalization cell count is

    e(C)=r−e+c−b.

Indeed the normalized surfaces have total Euler number 2r, and the point identifications remove r+e−c+b. Combining this with the graph bound gives e(C)≥r−e+d−1≥r−1. Therefore e(C)≥0 whenever r≥1.

## The rational-free case and the hypersurface branch map

Now r=0. Every normalized image component is elliptic. Finiteness of ν makes each component of D_red map nonconstantly onto an image component. Riemann–Hurwitz therefore excludes all rational components of D_red. The divisor D_red consists of disjoint smooth elliptic roots, so at every point of T the conductor has at most one smooth irreducible curve germ.

Fix p∈C and factor the reduced local hypersurface equation in the smooth threefold as ∏g_i, where the g_i are the irreducible analytic surface branches S_i. Each normalization point above p has a unique irreducible conductor curve germ, whose finite image is an irreducible curve germ C_i. Every pair of distinct hypersurface branches S_i,S_j meets in a curve through p: the ideal (g_i,g_j) has height at most two in the regular local ring of dimension three. Its preimage in each normalization branch has dimension one and lies in the conductor. Since there is only one conductor curve germ there, this preimage is that germ. Thus its image is both C_i and C_j, so C_i=C_j. With only one surface branch there is already one image curve germ.

Hence C is locally unibranch everywhere. Its curve normalization is a finite continuous bijection, and compactness/Hausdorffness makes it a homeomorphism. Its normalized components are elliptic, so their images are disjoint as connected components and e(C)=0. This proves the remaining case.

Combining the cases gives e(C)≥0 and finally e(S)=k−v+e(C)≥0, exactly the YH statement. The only still-outstanding work before freeze is to bind the complete normal-form input scope and run/read the new graph/cell computation. Neither printed WW nor printed YH proof has been used.

## Prerelease normal-form precision before checkpoint

The nonlinear weighted-degree paragraph above has the displayed two-dimensional weight-(r+1) space for r≥2. The Jordan case r=1 must also be included: then P=A z²+B zw+C w², and g=(βz+λw,βw), λ≠0. Comparing the zw coefficient in P∘g=β²P gives 2Aβλ=0, so A=0. Comparing the w² coefficient then gives Bβλ=0, so B=0. Thus P=Cw², again one smooth reduced root. This completes the nonlinear normal forms. The initial message/paragraph is retained with this explicit range correction; no target proof has been opened and no derivation has yet been frozen.
