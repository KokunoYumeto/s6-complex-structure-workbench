# MH.1 comparison: the actual analytic support map

This receipt was written **after** comparison with the printed proof. The preread gate in `006_MH_prederivations.md` remains part of the provenance. Accordingly this is a targeted proof check, not an independently written re-proof of MH.1.

## Objects and maps

Put X=U', i:D→X, j:X\D→X. All objects below are subsequently restricted to the compact divisor D; an algebraic compactification of X is not introduced.

The rational support object is

    A_Q = Cone[Q_D → i*Rj*Q_{X\D}][−1].

The localization triangle identifies this canonically with i*Ri!Q_X. The arrow

    a_Q:A_Q→Q_D

is its cone projection. After RΓ(D,−), this is precisely the direct-limit map H_D^k(X,Q)→colim_W H^k(W,Q)=H^k(D,Q), formed by forgetting support and then restriction. No choice of a vector-space isomorphism occurs here.

For each C=D_I, let L_C be Ω_X(log D)/I_CΩ_X(log D), with the quotient logarithmic residue filtration and form-degree filtration. Let L be its alternating Čech totalization over D^{[p]}. Let K be the Čech de Rham totalization of the same projective strata. L rationally realizes i*Rj*Q, K realizes Q_D, and the regular-form maps K→L realize the displayed rational arrow. Thus

    A_C = Cone[K→L][−1],    a_C:A_C→K

is the same support object and the same arrow, including the Hodge filtration. The weight filtration is the mixed-cone filtration on this Čech/logarithmic construction, rather than an arbitrarily assigned filtration on H_D.

## Why the filtered comparison is analytic-local

For one smooth divisor D_i, the residue sequence of complexes is

    0→Ω_X→Ω_X(log D_i)→Ω_{D_i}[−1]→0.

The residue sends (dz_i/z_i)∧η to η|_{D_i}. With rational residue divided by 2πi, the support cone is Ω_{D_i}[−2](−1). In local trivializations of the normal line bundle, dlog(z_i) changes by dlog(g_ij). This change preserves the logarithmic filtration and form degree; its extension class is c₁(N_{D_i/X}). Consequently the induced support-to-restriction morphism is the Thom/Gysin self-intersection map, represented on D_i by cup product with this actual first Chern class. A holomorphic line bundle on the projective D_i is algebraic, so this is a morphism of Hodge structures with exactly the displayed Tate twist.

For a union, use the **natural closed-support** triangle

    RΓ_{A∩B}→RΓ_A⊕RΓ_B→RΓ_{A∪B}.

Apply it to the divisor components and form the alternating intersection totalization. In a chart D={z₁⋯z_r=0}, its comparison with the log cone is given by the preceding residues, iterated in increasing coordinate order. Omitting z_i changes the sign by its position in the ordered wedge. The identity Res_i Res_j=−Res_j Res_i supplies the anticommutation needed for a map of total complexes. This verifies the triangle and the cone projection simultaneously: each support inclusion is the same localization inclusion before the residue identification, and each final projection is the map that forgets support.

The weight filtration on this support totalization has the stratum of codimension c=p+1 in Čech degree −p; its Thom model is Ω_{D_I}[−2c](−c). The corresponding graded rational and complex pieces are identified by the iterated residue divided by (2πi)^c. On logarithmic overlap maps z_i'=g_i z_i the extra term dlog(g_i) has one fewer logarithmic factor, so it preserves this filtration; form-degree compatibility follows because all residues lower degree by c and the twist shifts F by c. Thus these local comparisons glue as filtered maps, and their graded maps are exactly the residue/Thom isomorphisms. They are filtered quasi-isomorphisms. This checks the filtration on the **actual** cone, not a replacement cohomology group.

Equivalently, the associated spectral sequence is

    E₁^{−p,q}=⊕_{|I|=p+1} H^{q−2p−2}(D_I,Q)(−p−1)
                  ⇒ H_D^{q−p}(X,Q).

Its d₁ is the alternating Gysin map. Every D_I is projective. The summand has weight (q−2p−2)+2p+2=q, which in total degree k=q−p is k+p≥k. Hence the support complex has weights ≥k in degree k. The target K has the ordinary proper Čech weights ≤k. The cone projection a is a morphism for both filtrations by the just-described comparison. Acyclicity of i*Rj*V makes its map on degree-k cohomology an isomorphism. Strictness then yields weight k.

## Finite coefficients and descent to S

A finite étale trivializing cover of a neighbourhood restricts to finite étale covers of all D_I. These remain projective because the pulled-back ample class is positive. The cover need not itself have acyclic punctured cohomology: use the rational representation projector defining V in a finite sum of regular representations. All residue, support and restriction maps commute with deck transformations, so their projected summands have the same actual-map and filtration properties.

Finally, r* on shrinking smooth ambient neighbourhoods has the oriented degree-one trace left inverse, by the projection formula. Passing to the direct limit gives the actual injective pullback H^k(S,V)→H^k(D,r*V). To identify its Hodge structure, choose projective resolutions of the normalization and conductor of S. They exist because S is the proper image of the projective components of D and their resolved modifications. Resolve the fibre products with D^{[p]} over S; those fibre products are closed analytic subspaces of products of projective varieties and hence projective algebraic by Chow. Their proper hyperresolutions give a common projective simplicial refinement. The induced pullbacks on its projective strata realize precisely r* under cohomological descent. Therefore r* is a morphism of the stated Hodge structures and its image is pure.

## Source scope and outcome

Opened primary source: J. H. M. Steenbrink, *Cup products and mixed Hodge structures*, arXiv:math/9902134v1, 23 February 1999, §3 Theorem 1 and Corollary 2, printed pp. 5--7; §4 equation (3), printed p. 9. URL: https://arxiv.org/pdf/math/9902134 . The source itself assumes a complete smooth algebraic ambient space. Its local residue calculation and the support cone are used here; the compact-projective-stratum verification above supplies the analytic-neighbourhood extension and the actual arrow. This comparison closes the preread analytic-support gate by the explicit residue/Thom and localization maps; the historical preread gate is not erased.
