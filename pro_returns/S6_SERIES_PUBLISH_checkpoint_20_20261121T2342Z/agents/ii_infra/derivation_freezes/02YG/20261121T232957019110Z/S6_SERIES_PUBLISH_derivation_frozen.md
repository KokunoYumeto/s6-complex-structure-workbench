# 02YG / night:P4R.4 — independent derivation before target release

Checker: ii_check_a, GPT-6 Astra, ChatGPT Pro mode, effort Pro, continuing publication run, 2026-11-21. The complete target statement and safe cited-input supplement have been read. The target proof, outline and old target routines remain closed. The primary neighborhood input is the actually opened Łojasiewicz1964 Theorem2, p.464, with its complete main proof read; the actual proper-complex-morphism neighborhood paragraph of Fernández de Bobadilla–Kollár2012, p.85, was also opened while checking Y2. The derivation below proves the particular tube π1 comparison explicitly.

## 0. Exact statement, inputs and conventions

For a proper holomorphic degeneration f:X→Δ of complex two-tori with smooth total threefold and central fibre mS, S irreducible and reduced, let Λ=H1(F;Z)≅Z4 for a nearby torus F. The target chooses a positive small-loop monodromy A on Λ and claims that a positive meridian is μ=λt^m for some λ∈Λ in the split extension Λ⋊_A〈t〉; that

    π1(S) ≅ (Λ⋊_A〈t〉)/〈〈μ〉〉,
    π1(S)/imΛ ≅ Z/mZ,
    b1(S) = dim_Q ker(A−I);

and that, in the higher-genus ruled-normalization situation of P4R.3, a singular-locus incidence graph which is a tree of rational normalization components gives e(S)≥3.

The safe inputs are P4R.1 (Y2), P4.13 (WK), and P4R.3 (YF). WK states the exact identity m e(S_reg)=det(I−A^m) and nonnegativity of e(S_reg). YF states π1(S)≅π1(C), where C=Sing(S)_red, for the specified support with smooth normalization birationally ruled over a genus≥2 curve. Its normalization/conductor pushout has already been independently derived and checked in this run. The graph argument below uses the actual normalization map of C and retains the sphere classes; it makes no homotopy identification of the whole curve with a one-dimensional graph.

Fix the complex orientation of the base disk and of a transverse complex normal disk. Products of paths are read as composition, from right to left. With this convention a lift t of the positive base generator acts by conjugation on the fibre group as the positive parallel-transport monodromy A. Changing the fibre basepoint along the endpoint-return path conjugates the action on π1(F); because Λ is abelian it does not change A on Λ. The semidirect product has multiplication (x,n)(y,k)=(x+A^n y,n+k). This specifies the sign and action convention used in every displayed map.

## 1. The fundamental group of a sufficiently small full tube equals that of S

The opened Łojasiewicz theorem gives a compatible locally finite triangulation τ:|K|→X with S the image of a finite subcomplex L. After barycentric subdivision L is full. On the open star of L, set Q=Σ_{v∈L}λ_v and r_K(x)=Σ_{v∈L}(λ_v/Q)v. The homotopy H_s(x)=(1−s)x+s r_K(x) fixes L and stays in the star since Q(H_s)=(1−s)Q+s>0. Its transport by τ is a strong deformation retraction to S. Successive subdivisions, finite stars and uniform continuity on their compact union make these retracting neighborhoods cofinal among neighborhoods of S. These are exactly the maps proved in the frozen Y2 derivation §§1–2.

Choose an outer such neighborhood N0. Properness gives b>0 with U_b=f^{-1}(Δ_b)⊂N0. Choose another retracting neighborhood N1 with S⊂N1⊂U_b. Properness again gives 0<a<b with U_a=f^{-1}(Δ_a)⊂N1. Thus

    S ⊂ U_a ⊂ N1 ⊂ U_b ⊂ N0.

The inclusions S→N1 and S→N0 are homotopy equivalences; their induced π1 maps use a fixed basepoint s∈S.

The inclusion U_a→U_b is a homotopy equivalence. Here is the exact construction. Choose a smooth increasing radius function h:[0,b)→[0,a) with h(r)=r for r≤a/3 and h(r)<a for every r<b. For s∈[0,1] put h_s(r)=(1−s)r+s h(r). The base path h_s(r)e^{iθ} stays away from0 whenever r>0 and is stationary for r≤a/3. A horizontal complement for the proper smooth submersion over Δ* lifts these radial paths. Properness over the compact annulus a/3≤|t|≤b prevents finite-time escape and gives smooth dependence. The resulting maps Φ_s:U_b→U_b are the identity on f^{-1}(Δ_{a/3}), hence extend continuously across S, with Φ_0=id and Φ_1(U_b)⊂U_a. For points already in U_a, the same homotopy stays in U_a. Therefore Φ_1 is a homotopy inverse to the inclusion U_a→U_b, with both homotopies fixing S.

At π1, write the maps in the chain as

    π1(U_a) --u--> π1(N1) --v--> π1(U_b) --w--> π1(N0).

The composite vu is an isomorphism by the radial homotopy. The composite wv is an isomorphism because both N1 and N0 retract to S and their inclusions of S commute. Hence v is surjective (vu is surjective) and injective (wv is injective). It is an isomorphism. It follows that the actual inclusion S→U_b induces an isomorphism on π1. The restriction of the N0 retraction r:U_b→S is its inverse on π1, since r∘i=id_S. This establishes precisely the tube comparison needed for the exact group statement, including an injectivity proof rather than only the surjection used by Y2.

The published paragraph after Definition1 in Bobadilla–Kollár, p.85, states a general neighborhood deformation retraction. The above interleaving and radial maps prove the π1 form for round disks in the present degeneration and specify all maps used; no assumption on an unspecified shape of base neighborhood is needed.

## 2. The punctured tube and the oriented meridian

Put U=U_b and U*=U\S. The pullback along the positive universal covering e:H→Δ_b*, e(w)=exp(2πiw), is U_H={(x,w):f(x)=e(w)}. Horizontal transport along straight segments in the half-plane H identifies U_H with F×H. Projection c:U_H→U* is a connected regular covering with deck group Z. Thus, at a basepoint q∈U*,

    1→Λ→Π:=π1(U*,q) --winding--> Z→1,

where Λ is precisely the image of π1(F,q)≅Z4. This is the exact construction in the frozen Y2 argument, with the covering projection c furnishing the injection.

Choose t∈Π of winding1. The map n↦t^n splits the quotient. Every element g has unique expression λt^n with n=winding(g), and λ=gt^{-n}. The action convention in §0 identifies its conjugation action with A, so this gives the displayed isomorphism Π≅Λ⋊_A〈t〉.

At a smooth point of S, the actual defining map is f=u z^m with u a holomorphic unit and z a transverse coordinate. Choose a holomorphic logarithm of u in a small coordinate ball and set z'=z exp((log u)/m), leaving the other coordinates fixed. Its Jacobian in the normal direction is nonzero, so it is a biholomorphic coordinate change and f=(z')^m. The positive normal circle z'=r exp(2πiθ), θ from0 to1, has base windingm. After a chosen path from q to its basepoint, its class μ lies in Π and has the unique expression

    μ=λt^m,      λ=μt^{-m}∈Λ.

No determination of λ or choice of a zero-section of f is required or asserted. A different connecting path conjugates μ; its normal closure and winding remain unchanged.

## 3. The complete kernel of the inclusion U*→U

Every loop in the smooth six-manifold U can be perturbed relative its basepoint off S, whose real dimension is at most four. One explicit construction was given before the Y2 freeze: in a convex coordinate ball the bad intermediate vertices of a segment from a fixed point outside S form countably many images of parameter spaces of dimension at most five, and have six-dimensional measure zero. Choosing vertices outside those sets and replacing small arcs by two-segment paths gives a based homotopy to a loop in U*. Hence π1(U*)→π1(U) is surjective.

For a loop in its kernel take a null-homotopy disk in U. Smooth it relative a boundary collar, perturb it off the singular strata of S (real dimension≤2), and make it transverse to S_reg (real dimension4). Relative general position is justified by local bump-function translations: the parameter evaluation map is a submersion away from the fixed boundary collar, and regular parameters give the stated transversality. The singular-stratum dimension sum is2+2<6, so these preimages are empty. Transversality to S_reg gives isolated intersections; compactness of the disk and avoidance of the closed singular part make their number finite.

Deleting small disks about these intersections expresses the original based loop as a product of conjugates of meridians or their inverses. Conversely each meridian bounds its transverse disk in U. Therefore the kernel is the normal closure of all such meridians. The smooth locus of an irreducible analytic surface is connected. The detailed local Weierstrass/monodromy justification and the global branch-closure argument were verified in the Y2 comparison. Along a path in S_reg, its complex normal line is trivial over the interval; small positive normal circles form an annulus in U*. This gives conjugacy of all positive meridians. Consequently

    ker(Π→π1(U))=〈〈μ〉〉.

Combining with the actual inclusion isomorphism i_*:π1(S)→π1(U) from §1 gives

    π1(S) ≅ Π/〈〈μ〉〉.

This is an isomorphism produced by the map r_*∘(U*→U)_*, with its kernel just computed. It is the precise small-tube comparison claimed by the target.

## 4. The exact quotient by the fibre lattice

Let G=Π/〈〈μ〉〉 and L its image of Λ. The winding map Π→Z carries μ to m; every conjugate of μ has windingm and every inverse has winding−m. Thus the image of its normal closure under winding is exactly mZ. Quotienting G by L gives

    G/L = Π/(Λ·〈〈μ〉〉) ≅ Z/mZ.

Explicitly, winding modulo m descends to G/L, and the inverse sends the class of n to the class of t^n. The relations in each direction are exactly those just listed. This proves equality of the quotient order with m; it is stronger than the divisibility conclusion of Y2 and uses the complete kernel plus the actual tube π1 isomorphism.

## 5. Abelianization and b1

Use the usual four additive generators of Λ. The abelianization of Π has presentation Λ/(A−I)Λ plus the free generator t. Adding the relation μ=λt^m gives the integral presentation matrix

    M = [ A−I   λ ]
        [  0    m ].

Here the first four columns are the abelianized conjugation relations and the last is the meridian relation; columns are relation vectors in Z4⊕Z. Thus H1(S;Z)=coker M by the actual group presentation, including its torsion.

Over Q, multiply M on the left by

    U = [ I   −λ/m ]       with inverse V = [ I   λ ].
        [ 0    1/m ]                        [ 0   m ]

Direct multiplication gives UV=VU=I and UM=diag(A−I,1). This is an explicit isomorphism of the ambient rational relation spaces; it does not suppress any claim about the original integral cokernel. Hence rank_Q M=rank_Q(A−I)+1, and

    b1(S)=5−rank_Q M=4−rank_Q(A−I)=dim_Q ker(A−I).

The new prerelease program independently expands these three universal matrix identities over Z[a_ij,λ_i,m,m^{-1}] and checks every coefficient residual. Its mathematical consequence is the rank argument just given. It does not merely compare ranks on sample matrices.

## 6. The rational incidence tree and its actual topological maps

Now take the support of P4R.3. Its input conclusion supplies π1(S)≅π1(C), C=Sing(S)_red. In the target's final sector, the normalization of every irreducible component of C is P1, and the full normalization incidence graph Γ is a tree. Let v≥1 be the number of normalized components. Let P be the finite set of points where the normalization map

    ν_C: C~ = ⨿_{i=1}^v P1_i → C

has more than one preimage; put r_p=#ν_C^{-1}(p). The graph has v component vertices, one vertex for each p∈P, and one edge for each branch over each p. Unibranch singular points have one preimage and make no point-identification contribution; they can equivalently be included as leaf point-vertices without changing any formula below.

Construct X_Γ from the disjoint P1_i by adding, for each p, one new vertex and an interval from that vertex to each point of ν_C^{-1}(p). There is a continuous map q:X_Γ→C: on each sphere it is ν_C, and every added interval is collapsed to p. Its quotient by each finite star is exactly C, since the proper normalization map gives the topological quotient by its finite fibres. Each star is a contractible subcomplex after triangulating the spheres with the finitely many branch preimages as vertices. Collapsing it is a homotopy equivalence. To verify this last map, contract the subcomplex to a point and extend that contraction to X_Γ by the homotopy extension property of a CW subcomplex; the terminal map factors through the quotient, and the extended homotopy gives inverses up to homotopy. The stars are disjoint, so these finite collapses may be performed successively. Thus q is a homotopy equivalence, with this explicit construction.

There is also the map X_Γ→Γ which collapses each P1 component to its component vertex and retains the added intervals. Van Kampen, with simply connected sphere vertex spaces, shows that this map induces an isomorphism on π1. It kills the sphere H2 classes and is not used as a homotopy equivalence of spaces. Therefore π1(C)≅π1(Γ). Since Γ is a tree, π1(C)=1, hence π1(S)=1 by P4R.3.

Euler characteristic is computed by the same finite normalization quotient:

    e(C)=2v−Σ_p(r_p−1).

Write p=#P and E=Σ_p r_p. A connected tree has E=v+p−1. Hence Σ_p(r_p−1)=E−p=v−1, and e(C)=v+1≥2. This counts all branches mapping to the same point and permits components on different ruling fibres to have the same image, as required by the P4R.3 input. It does not count only pairwise transverse nodes or omit unibranch singularities.

## 7. e(S_reg)=1 and the lower bound3

Since π1(S)=1, the exact quotient in §4 is trivial, so Z/mZ is trivial and m=1. With μ=λt, the group presentation allows elimination of t=λ^{-1}. Conjugation by an element of the abelian lattice is trivial, so the remaining relations are precisely (A−I)Λ=0. This gives an isomorphism

    G ≅ Λ/(A−I)Λ.

For completeness the inverse sends a lattice class to its class in G, while t is sent to −λ in the lattice quotient; all conjugation and meridian relations are satisfied. Because G=1, the endomorphism A−I:Z4→Z4 is surjective. Choose integral preimages of the four standard basis vectors to form an integral right inverse B. Then (A−I)B=I, and determinant multiplicativity gives det(A−I)det(B)=1. The two integer factors force det(A−I)=±1.

In dimension4, det(I−A)=det(A−I). The new program verifies this exact sign identity by the two complete24-term Leibniz expansions with symbolic entries. WK now applies with the original positive monodromy and m=1:

    e(S_reg)=det(I−A)≥0.

Together with the value±1 this yields e(S_reg)=1. Finally Euler additivity gives

    e(S)=e(S_reg)+e(C)=1+(v+1)=v+2≥3.

Here additivity may be read using compactly supported Euler characteristic for the two strata. S and C are compact. S_reg is an oriented real-four-dimensional manifold of finite topological type, so Poincaré duality gives e_c(S_reg)=e(S_reg); thus this is the same number as in WK. No compactness of S_reg is assumed.

The fresh program also certifies the universal graph Euler substitution 2v+p−E→v+1 under E=v+p−1 and the final support expression v+2. The inequalities use v≥1, proved by the nonempty singular locus in this sector, rather than finite numerical sampling.

## 8. Prerelease completion and scope

All parts of the printed statement have now been derived: the actual meridian normal-closure quotient; the exact cyclic quotient Z/mZ; the rational b1 formula with its explicit relation-space isomorphism; and the rational-tree Euler bound using all normalization branches and the exact group elimination. The program `code/S6_SERIES_PUBLISH_II_A_02YG_relation_certificate.py` is new and was written with the target proof and old target routines closed. Its code/output/run receipt will be bound and read before the freeze.

The use of already checked Y2 and YF is explicit. The WK Euler identity is used only as the safe cited statement. The full topological maps used for the curve and its incidence graph retain the two-dimensional sphere classes at the appropriate stage. No hypothetical theorem or unproved identification is substituted for a required step. This complete derivation is ready to freeze before any target proof release.
