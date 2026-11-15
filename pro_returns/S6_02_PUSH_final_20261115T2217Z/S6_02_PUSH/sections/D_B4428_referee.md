# Independent referee of the B.4.28 candidate

Referee: boundary_d. Full initial source read: `sections/ab_push_log_canonical_torus.tex`, 2026-11-15, approximately 21:12 UTC.

## Initial verdict: a substantive gap in the proposed fundamental-group step

The component classification, nonnegative open Euler charges, elimination of interior blowups, elliptic normal-degree balance, and annular-twist rank bound are consistent with the stated extra hypothesis that the central dualizing bundle is trivial. However, the initial formula expressing pi1(D) as a free product of one Z per hyperbolic Inoue component and pi1 of the dual complex is not justified and must not be used.

Although each individual rational double curve is simply connected, paths through a whole conductor cycle can represent a nontrivial element of the normalization component's fundamental group. Triple-point attaching relations retain these path elements. In a hyperbolic Inoue component, a conductor cycle lifts to an infinite chain under the cyclic toric cover; its cycle loop therefore maps nontrivially to the component's infinite cyclic group. Edge groups being trivial does not eliminate this twisting in the complex-of-spaces presentation.

The diagnostic is concrete: replacing each split hyperbolic vertex's two deleted discs by an annulus can give a connected closed surface of Euler characteristic zero, and hence an abelian Z^2 fundamental group. Thus the proposed free-product contradiction is not a harmless omission. This was communicated to limits_ab and root immediately, and limits_ab independently confirmed and withdrew the step.

## Root's replacement: a local residue and hyperbolic-link contradiction

The following replacement has been independently checked and does not require a global torus-bundle assembly.

1. A sufficiently small closed boundary of either rational cycle in a hyperbolic Inoue component is a T2 mapping torus with hyperbolic monodromy A in SL2(Z). It lies entirely in the complement of the conductor. A compact neighbourhood of this boundary transports into each nearby smooth fibre by the submersion theorem.
2. Its T2 fibre can be chosen as the local angular torus at a node of the conductor cycle. In Oda's toric cover, the compact angular torus is N_R/N. The adjacent rays at a smooth toric node form an integral basis; the dual characters x,y identify its angular torus precisely with |x|=epsilon1, |y|=epsilon2. A fundamental path in the moment space, parallel to the infinite boundary chain and joining a point to its A-image, can be chosen through that cone point. Its compact-torus inverse image is the required mapping torus.
3. Corner blowups are periodic toric star subdivisions. They do not change the dense torus, the deck matrix A, or the angular T2; they only replace its coordinate basis by a unimodular basis. The same marking therefore holds for every allowed corner blowup.
4. The mapping-torus relations imply `(A-I)v=0` for the images of the two fibre circles in the abelian fundamental group of a nearby complex two-torus. Since A is hyperbolic, A-I is invertible over Q, so both images vanish rationally. The induced H2 class of the angular torus is zero: H2 of a real four-torus is dual to the products of H1 classes, and all such products pull back to zero.
5. The proper family is Gorenstein and h0 of its relative dualizing restriction is one on the central fibre and on all nearby two-tori. Grauert base change extends a nonzero generator of the trivial central dualizing bundle to a relative section, which remains nonvanishing near the compact centre.
6. At the corresponding triple point the local equation is xyz=t. The relative section is `U(x,y,z) dlog(x) wedge dlog(y)`, where U(0,0,0) is nonzero. Its integral over `|x|=epsilon1, |y|=epsilon2, z=t/(xy)` is `(2 pi i)^2` times the diagonal coefficient series `sum a_nnn t^n`, hence is nonzero for sufficiently small t. This contradicts the zero rational homology class from the mapping-torus relation.

This excludes the hyperbolic components directly in the nearby torus and repairs the conditional classification once written into the source. The former central free-product formula is not repaired or retained.

## Primary source opened for the exact angular marking

Oda, T. (1978). *Lectures on Torus Embeddings and Applications*. TIFR Lectures 58. Original full PDF: https://mathweb.tifr.res.in/Documents/Publications/Lectures/tifr58.pdf . Section15, Theorem15.1 and its proof, printed pp.130–131, describe the toric cover, its two infinite boundary chains, the hyperbolic unit deck action, and explicitly identify the complement of the two cycles as R times a compact angular-torus bundle over S1. Current retrieval records: turn631view0, turn632view0, turn632view1. The lattice/character identification in items 2–3 is the direct toric-coordinate calculation, not a claim that the source states a general semistable-plumbing theorem.

Fujiki, A., & Pontecorvo, M. (2010). *Anti-self-dual bihermitian structures on Inoue surfaces*. Journal of Differential Geometry, 85, 15–71. Original full article opened at https://archive.ymsc.tsinghua.edu.cn/pacm_download/21/834-JDG-85-1-A2-fujiki.pdf ; Sections3.2–3.3 confirm the topology, anticanonical configurations and corner-blowup conventions. Current retrieval records: turn630view0–2, turn631view1–2.

The extra central-dualizing triviality hypothesis remains essential to this argument. No K-trivial reduction for arbitrary analytic completions has been supplied.

## Final revised-source verdict

The revised source was reread in full at the changed hyperbolic and final dual-complex sections. **PASS.** It now contains the marked hyperbolic mapping torus, the compact-core transport, the H1-to-H2 vanishing in the actual nearby two-torus, and the exact convergent diagonal-series residue integral. The false free-product formula is absent from the proposition and retained only as a rejected historical attempt. The final rational toric dual complex is a closed oriented surface with coherent Euler characteristic zero, hence a torus. The extra central-dualizing triviality assumption remains explicit.

Bibliographic precision suggested to the author: use the already opened constant-dimension base-change theorem BS76push, III Theorem4.12, or the established Grauert60push alias. A suppressed Grauert1960D key and a generic Section7 reference should not be propagated into the assembled bibliography.
