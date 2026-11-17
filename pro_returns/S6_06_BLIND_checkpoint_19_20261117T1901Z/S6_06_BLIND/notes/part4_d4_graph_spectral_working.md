# Global conductor graph and spectral cubic in the last ruled sector

Status: complete scoped proofs, sent for independent audit. These results do not assert a conclusion for the remaining degree-two horizontal cover. The input is the remaining positive ruled support after P4.54 and P4R.18. We retain every vertical conductor component and every local branch of the other image component.

Let T→N→S be the minimal normalization resolution. Its pole support is a smooth positive-genus horizontal section H with rational vertical trees. H is noncontracted. The reduced normalization conductor D has a tree as its point-identification graph, and H remains a smooth embedded component of D: the ruling descends to N and its restriction to H is an inverse to H→N. Contracting exceptional vertical trees cannot identify two points of H. The image conductor C=A∪B has two rational normalization components and one graph cycle. The map H→A^ν=P1 has degree d=2 or 3, and the full generic transverse germ along A is D4.

At a point p of C, points of N over p correspond to local irreducible hypersurface branches of S. Any two such branches intersect along a curve. Thus the nonempty subsets of the analytic branches of C recorded on those normalization points pairwise intersect. We always count branches of D on its normalization, including distinct branches which meet at the same point of N.

## G1. A self-identification away from the other component is impossible

Suppose a point p of B has two analytic branches and p∉A. Let D_B be the reduced union of the conductor components mapping onto B. It has c_B normalized components and s_B≥1 connected components, and its graph is a forest. Every one of these components maps finitely and surjectively to B^ν, so the numbers r_+,r_- of points over the two normalization preimages of p satisfy r_+,r_-≥c_B.

There are n normalization points over p. Their nonempty supports in {+,-} pairwise intersect. The elementary two-element Helly argument gives a common element, say +: a singleton forces its element into every support, and without a singleton all supports are {+,-}. Hence r_+≥n. The graph contribution at p is

    r_++r_--n≥c_B.

The entire forest D_B has total contribution c_B−s_B<c_B. This is impossible. The same proof applies to a self-identification of A away from B, using the union D_A of all conductor components mapping onto A.

Consequently the one image-graph cycle is realized either at two distinct intersections A∩B, or at one point with three analytic curve branches belonging to both components. No separated self-node-plus-attachment configuration remains.

## G2. The horizontal image A is smooth, for both d=2 and d=3

Let C_{A,sch} be the primary component of the actual conductor scheme supported on A. The actual primary-restriction injection of P4R.13, as used in P4R.18, gives

    g(H)−1 ≤ χ(O_{C_{A,sch}}).

The generic ordinary-triple conductor is the square of the transverse maximal ideal. Purity of the actual conductor quotient identifies its A-primary inverse image with P_A^(2), exactly as in P4.31. Therefore the P4.34 conormal calculation gives

    χ(O_{C_{A,sch}})=5−Σ_p[δ(A,p)+τ_p−r_p].

For a planar singular point the bracket is exactly 5δ(A,p); for a nonplanar point with at most two analytic branches it is at least seven. The global image-graph formula Σ_p(r_p(C)−1)=2 and connectedness exclude three branches of A at a point: they would already use both identifications and the necessary meeting with B would use another. Thus these are all relevant local cases.

Since g(H)≥1, the total defect is at most five. If A is singular, it is consequently planar everywhere, has total delta invariant one, and g(H)=1. Thus A is locally a complete intersection in Y. Its conormal Q=P_A/P_A² is locally free of rank two. On its normalization j:P1→A put E0=j*Q. Adjunction gives

    ω_A = (ω_Y|A) ⊗ (det Q)^(-1).

The degree of j*ω_Y is zero because b2(Y)=0. The degree of j*ω_A is 2p_a(A)−2=0, since p_a(A)=1. Degree is unchanged by this finite birational normalization: the normalization exact sequence for a line bundle and for O_A have the same finite-length correction. Hence deg E0=0.

The reduced equation of S has generic order three along A. Powers of a local complete-intersection curve ideal are unmixed, so P_A^(3)=P_A³. Its actual third normal term is therefore a global section

    q3 ∈ H0(A, Sym³Q ⊗ O_Y(S)|A).

Pulling to P1 gives a cubic section of Sym³E0 tensored with a degree-zero line bundle. That line bundle is trivial on P1. Use the quotient convention P(E0), with tautological class ξ and fibre class F. The cubic zero divisor has class 3ξ. Remove its common zero fibres, of total degree b≥0; the residual reduced spectral curve Γ has class 3ξ−bF. Generic D4 gives three distinct roots, so no horizontal multiplicity occurs.

We identify its components through an exact morphism. At a generic point of H, the first normal derivative of the finite normalization morphism gives the normal direction of its smooth transverse branch, hence a point of P(E0). This meromorphic map on smooth H extends over every missing point by cancelling the common power in its two local coordinates. It lies over the actual finite map H→P1. Distinct generic H-preimages give distinct cubic roots. Thus H maps finitely and birationally to one spectral component Γ_H, and is its normalization. When d=3, Γ=Γ_H. When d=2, the third generic preimage is supplied by exactly one rational vertical conductor component, of degree one over A. Its direction gives a section Γ_R≅P1, and Γ=Γ_H∪Γ_R. These exhaust all three generic roots.

For a rank-two bundle of degree e on P1 the ruled-surface intersection identities are

    ξ²=e,  ξF=1,  F²=0,  K=-2ξ+(e−2)F.

Adjunction for Γ=3ξ−bF gives

    p_a(Γ)=3e−2−2b.

Here e=0, so p_a(Γ)=−2−2b. In degree three, normalization gives p_a(Γ)≥g(H)≥1. In degree two, the exact union sequence gives

    p_a(Γ)=p_a(Γ_H)+p_a(Γ_R)+length(Γ_H∩Γ_R)−1
           ≥g(H)−1≥0.

Both contradict the negative arithmetic genus. Hence A is smooth. This proof retains the actual cubic morphism and uses no classification of the other transverse type.

## G3. In degree three, a three-branch image point is impossible

Now d=3, so H is the only normalization-conductor component mapping onto A. By G2, A is smooth. A point realizing the image graph cycle with three local branches must consequently consist of the A branch and two B branches, denoted + and −.

Let c_B be the number of normalized conductor components mapping to B. The whole conductor D has 1+c_B normalized components and a tree graph, so its total point-identification contribution is c_B. At the proposed point let r_A≥1 and r_+,r_-≥c_B count its conductor branches, and let n be its normalization points. A normalization point contains at most one A-conductor branch because H is embedded and its distinct points are not identified.

A singleton support {A} would force every normalization point to carry A. Then n=r_A, so the graph contribution is r_++r_-≥2c_B>c_B. A singleton {+} would force r_+≥n, and the contribution would be at least r_A+r_-≥1+c_B. The same holds for {−}. Every support therefore has at least two elements. Hence r_A+r_++r_-≥2n, and the graph contribution is at least

    (r_A+r_++r_-)/2 ≥ c_B+r_A/2 > c_B.

This too contradicts the tree. Thus only two distinct A–B junctions remain in degree three.

## G4. At both degree-three junctions the entire cubic must vanish

Let p,q be the two distinct A–B junctions. Suppose a local normalization branch over p has conductor only over A. Pairwise hypersurface intersections then force every normalization point over p to carry A. Since H is the only A component and is embedded, n=r_A, and the graph contribution at p is r_B≥c_B. This uses the whole graph budget c_B.

At q there must be a normalization point carrying both A and B. Otherwise a point carrying A and a point carrying B would have disjoint supports, contradicting their curve intersection. Such a point contributes positively to the conductor graph. This exceeds the budget. Thus no A-only local branch exists at either junction.

We prove the local cubic implication without discarding B. Along the now smooth A, choose coordinates A=(x=y=0). Suppose its nonzero cubic normal form has a simple root. On the normal blowup chart x=yu, the strict equation has that simple root at y=0. The implicit-function theorem gives u=α(y,z); the actual function has an analytic factor

    f1=x−yα(y,z),

which is smooth. Exact division gives f=f1 f2. On f1=0 the second factor is y² times a unit, because the remaining two cubic roots have different direction from this simple root. Thus this smooth local branch intersects all the other branches only along A, and its conductor contains only A. This is the forbidden A-only branch.

A nonzero binary cubic has a simple root unless it is a cube. P4R.19 excludes the latter case by its actual weighted finite maps and nonzero compact intersection class. Therefore the entire cubic normal tensor vanishes at p and at q.

## G5. Exclusion of the degree-three horizontal cover

Since A=P1 is smooth, E=N_A/Y* has degree two: adjunction and c1(Y)·A=0 give deg N_A/Y=−2. Its actual cubic has at least two common zeros by G4. Remove their fibre divisor, of degree b≥2. The residual spectral cubic has class 3ξ−bF on P(E), and is irreducible with normalization H by the exact direction morphism in G2. Its arithmetic genus is

    p_a(Γ)=3·2−2−2b=4−2b≤0.

But p_a(Γ)≥g(H)≥1. This contradiction excludes d=3. The remaining horizontal map therefore has degree exactly two; its third generic spectral sheet is the unique rational vertical conductor component of degree one over A.

## Scope after these proofs

The still undecided configuration has A=P1 smooth, H→A of degree two, and one rational vertical conductor component R→A of degree one. The other image component B retains its unrestricted generic transverse type. Neither the allowed two-root attachment model nor the extra rational sheet has been omitted.
