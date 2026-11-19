# Weight/support batch: derivations written before printed proofs

Checker: GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro, S6_10_PAPERS continuation, 19 November 2026.

Inputs read: statements MH.1--4, CR.1, CR.5, VII.3--4; D.1.8--9 statements; Steenbrink, arXiv:math/9902134v1, §§3--4, especially Theorem 1, Corollary 2 and equation (3). Target proofs MH.1--4 have not been read.

## MH.1

Write i:D→U' and j:U'\D→U'. The exact localization triangle is Ri!Q→i*Q→i*Rj*Q; after global sections and shrinking the tube it is RΓ_D(U',Q)→RΓ(D,Q)→RΓ(W\D,Q). Thus acyclicity makes the first map an isomorphism on cohomology. This is the actual forget-support-and-restrict map, not an arbitrarily chosen vector-space identification.

For each compact projective intersection C of the components of D, choose coordinates in which D is z₁⋯zₗ=0 and I_C=(z_j:j∈J). For η=Σz_jη_j, dη=Σz_j((dz_j/z_j)∧η_j+dη_j), so I_CΩ(log D) is a differential subcomplex. Define L_C=Ω(log D)/I_CΩ(log D), with the quotient logarithmic and Hodge filtrations. Iterated residues identify its logarithmic graded pieces with ⊕_{|I|=k}Ω_{D_I∩C}[−k], with rational Tate normalization supplied by (2πi)^{-k}. To check the residue kernel, express forms in the basis dz_j/z_j: a surviving residue containing a normal coordinate of C either has that coordinate as a coefficient, or has its differential. Thus the kernel is I_CΩ+dI_C∧Ω. This proves the quotient quasi-isomorphism with i_C*Rj*Q locally by the logarithmic Poincaré lemma. It is precisely the coordinate calculation in the opened source, valid on analytic charts.

Take the alternating restriction total complex over the intersections C. Its graded residue pieces are de Rham complexes on compact projective intersections, including their finite étale covers. Their pure Hodge structures supply the mixed-Hodge-complex condition; restrictions are algebraic by Chow and the normal-bundle Chern classes are algebraic (1,1) classes on the projective strata. The support complex is Cone(K(D)→K(D log D))[−1]. Its map to K(D) is the cone projection. The remaining point that must be checked on comparison is that the filtration on this analytic support cone is identified with duality against K(D), with Tate twist (−3), so that H^k_D has weights ≥k. Merely quoting Steenbrink's complete algebraic-ambient theorem would not establish that extension.

Once that precise compatibility has been supplied, H^k(D) has weights ≤k and the support-to-restriction isomorphism has source weights ≥k, hence H^k(D) is pure. Finite monodromy is treated on a finite étale trivializing cover and by the rational representation projector; it is not necessary to assert acyclicity of the entire cover. For the original S, ambient blowup pullback has the actual degree-one Gysin left inverse. A projective hyperresolution of the proper analytic image S, compatible with D→S, makes pullback a morphism of Hodge structures. Therefore H^k(S,V) is a sub-Hodge structure of the pure H^k(D,r*V). The unresolved preread gate is the analytic support-duality compatibility, not the linear weight argument.

## MH.2

The integral invariant supplied by D.1.9 restricts nontrivially to the smooth torus in a small tube. Choose a prime p not dividing the nonzero coordinate gcd of that restriction, and reduce it mod p. The augmentation representation V of Q[Z/p] has rank d=p−1, is self-dual under the group-basis inner product, and splits over C into all nontrivial characters. On a torus each such character has a nontrivial multiplier on some circle factor; the cochain Koszul complex is contracted by dividing contraction with that factor by its multiplier minus one. Hence H*(F,V)=0. The bundle spectral sequence over the punctured disk gives H*(U\S,V)=0. The finite local system is defined on the whole tube, using the actual integral class there, so the localization triangle applies with no new ramification or change of the fibre multiplicity.

Duality on the oriented real six-dimensional tube gives H^k(S,V)≅H^{6−k}(S,V)*. Since S has real dimension four, h⁰=h¹=0 and h²=h⁴. Euler characteristic with a rank-d local system is d e(S), by the alternating dimensions of a finite cellular cochain complex. Thus d e(S)=2h⁴(S,V)−h³(S,V).

Choose the closed curve/finite set C⊂S over which h:Z→S fails to be an isomorphism, and E=h^{-1}C. The actual abstract blowup square yields the triangle RΓ(S,V)→RΓ(Z,V)⊕RΓ(C,V)→RΓ(E,V). Curves have H³=H⁴=0, so H⁴(S,V)→H⁴(Z,V) is an isomorphism and H³(S,V)→H³(Z,V) is onto. Its kernel is the image of H²(E,V). The latter has weights ≤2. MH.1 gives pure weight three on H³(S,V), forcing this image to vanish. Thus h³ is also preserved. Rational/ruled Z is projective, and an embedded resolution has projective components (strict transform and projective bundles over projective curves or points), so MH.1 applies after its analytic-support gate is closed.

For rational Z every finite local system pulled back from S is trivial because Z is simply connected; h⁴=d and h³=0, giving e(S)=2. For a ruled Z→B, point blowups leave π₁ and H³,H⁴ unchanged, and the actual ruling induces π₁(Z)≅π₁(B). Therefore V is pulled back from a finite local system W on B. Leray/projective-bundle cohomology gives H⁴(Z,V)=H²(B,W)(−1), H³(Z,V)=H¹(B,W)(−1). Self-duality makes h²(B,W)=h⁰(B,W), so 2h⁴−h³=dχ(B)=d(2−2g). This derives the printed Euler expression without assuming that the character is trivial on Z.

## MH.3

CR.5 supplies g=1. MH.2 then gives e(S)=0. In CR.1 the exact expression becomes e(S)=n−v+N₀, hence n=v−N₀. The independently stated UN.7 excludes occurrence of all these assumptions simultaneously; this row is a consequence of the listed geometric hypotheses and supplies no new example.

## MH.4

The same finite local system and tube duality give d e(S)=2h⁴(S,V)−h³(S,V), independently of mixed Hodge theory. For any proper surface modification/normalization, the abstract blowup square and the dimensions of the curves yield h⁴(S,V)=h⁴(Z,V) and h³(S,V)≥h³(Z,V). On a class VII surface, a nontrivial finite character gives h⁴=0; hence e(S)≤0. For a trivial summand, h⁴ equals its rank and h³=b₁ times that rank=rank, because b₁=1. Thus each trivial summand contributes at most its rank to the upper bound, and overall e(S)≤1. This also handles a representation with both invariant and noninvariant summands. VII.3 gives e(S)≥0; UN.1 gives e(S) even; therefore e(S)=0. This argument uses only the exact maps and duality, and no purity assertion for nonprojective class VII surfaces.
