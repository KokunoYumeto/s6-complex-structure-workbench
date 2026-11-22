# 02YJ / night:P4R.7 — independent derivation before target release

Checker: ii_check_a. The exact YJ statement and its cited-input supplement have been read. The YJ proof, printed outline, historical check derivation and historical YJ programs remain closed. The previously completed YF proof and the independently derived, now admitted YI result are explicit inputs; their exposure is recorded rather than treated as fresh YJ work.

## 0. Domain, maps and the claim

Use the standing proper surjective holomorphic fibration f:Y→B with connected fibres, smooth compact complex threefold Y, b1(Y)=b2(Y)=0, smooth compact base curve and smooth general fibre a complex two-torus. The specified full fibre is mS, with S reduced, irreducible and singular. Write ν:N→S for normalization and π:T→N for the minimal resolution. Put ρ=ν∘π. The target assumes that T is birationally ruled over a smooth compact curve R of genus g≥2 and asserts e(S)≥0. Its statement permits N to be singular.

Let C=Sing(S)_red. By the exact YI statement, there is an effective integral divisor D on T with

    ω_T(D) ≅ ρ*ω_S,
    D_red = ρ^−1(C)_red.

Every exceptional configuration of π has strictly positive coefficients and meets the strict conductor. WJ gives ω_S^⊗m≅O_S, hence K_T+D is torsion and in particular numerically trivial. The exact substitutions into the YI input are its ν,π,ρ,T,S,m without alteration. These identities are the only additional resolution information used below.

The support C is a nonempty compact reduced curve. WJ states that a normal support in this setting is smooth, so all singular points are nonnormal. The normalization conductor is nontrivial there; its inverse image in N is divisorial by the reflexive canonical-module identity proved in YI. Its finite image is therefore a curve, with no isolated singular points outside it.

## 1. The ruled model and the horizontal pole divisor

Choose a sequence of point blowdowns β:T→T0 to a minimal ruled surface r0:T0→R. The ruling on T is r=r0∘β. Beauville's opened original III.10, p.40, identifies T0 with a projective bundle P_R(V), and III.18, pp.46–47, gives the Picard/intersection formulas and canonical class. With h=c1(O_P(V)(1)) and F a fibre,

    h²=deg V,   h·F=1,   F²=0,
    K_T0=−2h+(deg V+2g−2)F.

These are the same projective bundle and quotient-line convention used in the completed YF check. Put D0=β_*D. This is an effective integral divisor. Pushing forward K_T+D and using the blowup canonical formula gives K_T0+D0 numerically trivial: intersection against each curve class on T0 equals intersection of K_T+D against its pullback. In particular D0·F=2.

For any horizontal prime component H of coefficient one in D0, adjunction and effectiveness give

    2p_a(H)−2=(K_T0+H)·H=−(D0−H)·H≤0.

The other divisor has no common component with H, so its intersection is nonnegative. The normalization H̃ maps finitely to R with positive degree d. Riemann–Hurwitz gives

    2g(H̃)−2=d(2g−2)+deg Ram>0.

The normalization exact sequence gives p_a(H)≥g(H̃), a contradiction. Thus every horizontal coefficient is at least two. Since the total weighted horizontal degree D0·F is two, there is exactly one horizontal component H, its coefficient is two, and its degree over R is one.

The normalization of H maps with degree one to the smooth R and is therefore isomorphic to R. Its map to T0 is a section of r0. A section of the separated projective bundle is a closed embedding, so H itself is a smooth copy of R. Every vertical prime divisor of T0 is an entire smooth rational ruling fibre. Consequently

    D0=2H+Σ_j a_j F_j,   a_j≥1,

with distinct fibres F_j. The reduced support is H with mutually disjoint rational fibres attached transversely at one point each. This derivation uses only K_T+D numerical triviality on the smooth resolution; it makes no smoothness assumption on N.

## 2. The blowup maps preserve a section with rational trees

At a point blowup γ:T'→T'' in the reverse of β, write D'' for the pushed-down divisor, μ for its multiplicity at the centre, and E for the exceptional curve. If D'=D''_strict+aE, the canonical formula in Beauville II.3(iv), pp.17–18, gives

    K_T'+D'=γ*(K_T''+D'')+(1+a−μ)E.

Intersecting with E gives 0=−(1+a−μ), so a=μ−1. Since D' is effective, μ≥1 and the centre lies on D''. The divisor retains its original coefficient on every strict transform.

The reduced divisor starts with simple normal crossings, consisting of H and the fibres F_j. At a smooth point of a conductor component of coefficient one, a=0: the strict transform is analytically the same smooth curve, and the new exceptional curve is absent from D'_red. At a smooth point of coefficient at least two, a≥1: the exceptional P1 is a leaf meeting the strict transform once. At a crossing of two positive components, a=μ−1≥1: the two strict transforms become disjoint near the centre and the new P1 joins them, subdividing the previous graph edge. These are all possible centres on a simple-normal-crossing divisor; each operation preserves that property and introduces no graph cycle.

Inductively, D_red is the strict transform H_T of H with finite rational trees attached at points. Every rational component belongs to exactly one such tree. The strict transform H_T remains a section of r:T→R, because its map under each point blowup restricts to the isomorphism of the smooth original curve with its strict transform. The support D_red is connected.

There is a continuous quotient q:D_red→H_T which is the identity on H_T and contracts each attached rational tree to its attachment point. The inclusion i:H_T→D_red satisfies q∘i=id_H_T. Van Kampen, adding each rational P1 along one point and each tree edge along contractible neighborhoods, proves that i_* and q_* are inverse isomorphisms on π1. This assertion is about π1. A rational component still contributes its degree-two sphere class; q kills that class. No deformation retraction of all of D_red onto H_T is asserted.

## 3. The inclusion of the full pole divisor induces a π1 isomorphism

The smooth P1-bundle T0→R induces an isomorphism on π1, since its fibre is simply connected and it is locally a product. A point blowup replaces a four-ball with the disc bundle of O_P1(−1), with common boundary S3; both inserted and removed pieces are simply connected. Van Kampen shows that each blowdown induces a π1 isomorphism. Hence r_*:π1(T)→π1(R) is an isomorphism.

The restriction r|H_T is the section isomorphism to R. The composite

    π1(H_T) --i_*--> π1(D_red) --> π1(T) --r_*--> π1(R)

is therefore the isomorphism induced by H_T≅R. Since i_* and r_* are already isomorphisms, the middle inclusion map j_*:π1(D_red)→π1(T) is an isomorphism as well. These are actual inclusion, quotient, blowdown and ruling maps. The argument remains valid when π later contracts H_T or any of its rational trees to points of N; that contraction has not been identified with β.

## 4. Proper resolution pushout, including contracted conductor components

Because D_red=ρ^−1(C)_red, every fibre of ρ over C is contained in D_red. Over S\C, normalization and resolution identify T\D_red with S_reg. The map ρ|D_red:D_red→C is surjective and proper; it may contract curves. It is not required to be finite in this argument.

Form the topological pushout

    P = T ⊔ C / { d ∼ ρ(d) for d∈D_red }.

The maps ρ on T and identity on C induce a continuous map P→S. It is surjective. Over S\C its fibres are singletons because ρ is an isomorphism there. Over a point c∈C the construction identifies every point of ρ^−1(c) with that same c, because the entire fibre is in D_red. Thus P→S is injective as well. P is compact, as a quotient of compact T⊔C, and S is Hausdorff. A continuous bijection from a compact space to a Hausdorff space is a homeomorphism: images of closed subsets are compact and hence closed, which gives continuity of the inverse. This proves the exact topological quotient identity, including every contraction in π.

The analytic pair (T,D_red) has a compatible triangulation by the previously opened Łojasiewicz Theorem 2, p.464. In fact the simple-normal-crossing description above supplies compatible local coordinate triangulations. D_red is a subcomplex, so j:D_red→T is a cofibration. Its homotopy extension property identifies the ordinary pushout with the double mapping-cylinder homotopy pushout of T←D_red→C: the map collapsing the cylinder to the common image is the comparison map. To construct its homotopy inverse, the cylinder path from d in T to ρ(d) in C is extended from D_red across T by the homotopy extension property; the resulting endpoint map on T agrees with the inclusion of C on D_red, and therefore descends to P. The cylinder path and the extension give the two comparison homotopies.

All three spaces T,D_red,C are connected; C is connected because it is the continuous image of connected D_red. Applying van Kampen to the double mapping cylinder gives

    π1(S) ≅ π1(T) *_{π1(D_red)} π1(C).

Since j_* is an isomorphism, this amalgam is π1(C). Explicitly, the map from π1(C) into the amalgam is inverse to the homomorphism which is identity on π1(C) and equals (ρ|D_red)_*∘j_*^−1 on π1(T). The defining amalgam relations make these maps inverse. This proves π1(S)≅π1(C) for the proper contraction map, without requiring smooth normalization.

The accepted smooth-normalization YF proof provides the same construction with ρ=ν and finite ρ|D_red. Here the exact extension is to ρ=ν∘π with the full inverse-image equality from YI. No conclusion is transported merely by matching the symbols D and C; the homeomorphism and both inverse group maps have been established above.

## 5. Virtually abelian compact curve groups and their Euler numbers

The exact Y2 statement gives π1(S) an abelian normal subgroup of finite cyclic index dividing m. Hence π1(C) is virtually abelian under the isomorphism in §4.

Let C_1,…,C_c be the irreducible components, with smooth normalizations C̃_i of genus g_i, and write G=Σ_i g_i. The normalization of a compact reduced curve identifies only finitely many points. An injective unibranch normalization map is a local homeomorphism onto the curve; at a multibranch point the preimages are joined in a homotopy model by a finite star. Introduce one auxiliary vertex for each such singular point and one edge for each of its branches. The resulting connected incidence graph has component vertices and auxiliary point vertices; let b be its first Betti number.

Choose a spanning tree of that graph and collapse it. The homotopy model becomes the closed surfaces C̃_i joined at one point, together with b extra circle loops. Van Kampen therefore gives

    π1(C) ≅ (*_{i=1}^c π1(C̃_i)) * F_b.

For the Euler number, suppose there are s auxiliary vertices and E incidence edges. Give each normalized surface one vertex, 2g_i one-cells and one two-cell. The full model has c+s vertices, E+2G one-cells and c two-cells, and its incidence graph has b=E−c−s+1. Therefore

    e(C)=(c+s)−(E+2G)+c=c+1−2G−b.

This counts arbitrary identifications among the conductor-image components. It makes no assumption that curves on distinct ruling fibres have distinct images, and no assumption that the conductor-image map is unramified.

A genus-h≥2 surface factor cannot be virtually abelian. Any finite-index subgroup corresponds to an unramified connected finite cover of that closed surface; a degree-d cover has genus 1+d(h−1)≥2. Its group is nonabelian, for example because its standard surface presentation surjects onto a free group of rank at least two. A quotient of a virtually abelian group is virtually abelian, so projection onto this factor excludes every g_i≥2.

Two distinct genus-one factors contain a free subgroup generated by one infinite-order element from each factor; the free-product normal form proves that it is F2. One genus-one factor together with one free generator gives the same F2 subgroup. A free group F_b with b≥2 also contains F2. Every subgroup of a virtually abelian group is virtually abelian, because intersection with a finite-index abelian subgroup has finite index. F2 is not virtually abelian: a finite-index subgroup is the fundamental group of a finite cover of the two-circle graph, with rank 1+d≥2. These cases are impossible.

It follows that either all g_i=0 and b∈{0,1}, or exactly one g_i=1 and b=0. In the first case e(C)=c+(1−b)≥0 because c≥1; in the second e(C)=c−1≥0. This completes the curve Euler bound.

## 6. Euler number of the surface and conclusion

The exact WK statement applies to the same proper local degeneration and full fibre mS. Its conclusion gives

    m e(S_reg)=det(I−A^m),   e(S_reg)≥0,

where A is the monodromy on H1 of the nearby complex two-torus. There is no change of fibre multiplicity or monodromy in this use. Only its nonnegative bound is required.

The closed analytic curve C and its complement S_reg form a finite triangulable stratification of compact S. Additivity of compactly supported Euler number gives

    e(S)=e(S_reg)+e(C)≥0.

The exact map T\D_red→S_reg is the isomorphism from §4, but no Euler correction for contracted exceptional curves is needed: their entire image is already in the closed stratum C, whose topology has been computed by the actual quotient. This proves the complete target statement with singular N permitted.

## 7. Fresh program, method and input scopes

The new code `code/S6_SERIES_PUBLISH_II_A_02YJ_affine_chain_certificate.py` was written and run while the target proof remained closed. It ran at 00:12:50.832414–00:12:50.850863 UTC on 22 November 2026, exit 0. Code SHA256 is `a617a9043dff2f65261114defcd957156f0d2232eef74c21ce9b3afd21af289f`; output SHA256 is `6495f294e8ba5915ce3352b63a2cf3e19f66ee5f8109b6873bc4aa66a230515e`. Its whole source and every output field are read before freezing this derivation.

The curve identity is an affine polynomial in (c,s,b,G). An affine polynomial is exactly its constant term plus the sum of its coordinate coefficients times the variables. Values at zero and the four unit vectors therefore recover all five coefficients; the program gets zero for every coefficient of the Euler residual. It similarly recovers the zero residuals for the two virtually abelian cases and for 1+(μ−1)−μ. This is a universal coefficient recovery, not a finite collection of example curves.

For a rational leaf attached at p, take the chain basis (p,v) in degree zero, an edge with boundary v−p, and the sphere cell in degree two. The matrices U=[[1,1],[0,1]] and V=[[1,−1],[0,1]] give mutually inverse integral changes between (p,v) and (p,v−p), with determinant one. The boundary becomes (0,1)^t, splitting off the contractible new vertex-edge pair; the degree-two sphere cell remains. This is the precise chain computation corresponding to the π1-preserving tree attachment and the killed H2 class under q. The program verifies the inverses, determinants and boundary image. The π1 statement itself is the van Kampen proof in §2.

The existing Beauville primary source was actually read at III.10 p.40, III.18 pp.46–47 and II.3(iv) pp.17–18 during the completed ruled-surface checks. The YF proof just reread uses these same exact projective bundle and blowup maps. The Łojasiewicz source was actually read at Theorem 2 and the complete main proof, with full images of printed pp.463–474; the new use is the same analytic-pair triangulation. These prior primary openings are reused with their exact receipts, with no new whole-source reading credit.

All statement conclusions have now been derived. The YJ proof and its historical programs remain closed at the time this record is frozen.
