# 02YD / night:P4R.2 — derivation before opening the target proof

Checker: ii_check_a, GPT-6 Astra, ChatGPT Pro mode, effort Pro, continuing publication run, 2026-11-21. The target proof, outline and any old target program remain closed while this file is written. The inputs are the exact statement packet, its cited-input supplement, the already frozen and checked Y2 group result, and the previously opened primary classification loci bound below. No argument from the YD target is an input.

## 0. Statement and exact standing scope

The target concerns a proper surjective holomorphic map f:Y→B from a connected smooth compact complex threefold with b1(Y)=b2(Y)=0 to a smooth compact curve, with connected fibres and smooth general fibre a complex two-torus. Its specified fibre is mS with S irreducible, reduced and singular. Its normalization ν:T→S is smooth and bijective. The conclusions are e(S)≥0, and e(S)=0 exactly when T itself is a minimal ruled surface over an elliptic curve or a Hopf surface.

The safe cited-input supplement includes P4.12 (02WJ): ω_S^m≅O_S, χ(O_S)=0, h1(O_S)∈{1,2}; every normal such support is smooth; the minimal resolved normalization model of a singular support has κ=−∞. It also includes P4R.1 (02Y2): π1(S) has a normal abelian subgroup with finite cyclic quotient of order dividing m. Y2 has now been derived, frozen and compared in this run. The supplement's P4.8 statement has a normal-crossing hypothesis; no normal-crossing assumption occurs in the present target, and that input is not used to extend its scope. The derivation below proves the present assertion directly under the printed hypotheses.

The finite normalization map ν is the map used throughout; its bijectivity is a hypothesis. No homeomorphism of an unrelated model is assumed.

## 1. The normalization is a homeomorphism, and its conductor is nonempty

S is compact and Hausdorff. T is compact because ν is finite and proper. A continuous bijection from a compact space to a Hausdorff space is a homeomorphism: a closed subset of T is compact, its image in S is compact and hence closed, so the inverse is continuous. Applying this argument to ν gives the actual homeomorphism ν:T→S. Thus ν_* identifies π1(T) with π1(S), and its maps on integral homology are isomorphisms. In particular e(S)=e(T).

The surface S is nonnormal. Indeed P4.12 says that every normal support in this setting is smooth, whereas S is singular. Equivalently the smooth normalization map cannot be an isomorphism. The nonnormal locus of a reduced hypersurface surface in a smooth threefold has a curve component: its local rings are Cohen–Macaulay and satisfy Serre's S2 condition; regularity in codimension one would therefore make them normal. Consequently the conductor ideal Ann_O_S(ν_*O_T/O_S) is nontrivial along a curve. Its pullback divisor D on the smooth normalization T is an effective nonzero integral divisor, with its genuine scheme multiplicities. The safe A.5.3 statement identifies this divisor by

    ω_T(D) ≅ ν^*ω_S.

This conductor fact will be used only in the zero-Euler class-VII case to exclude the curve-free surfaces; it adds no assumption about ordinary double curves or reduced conductor coefficients.

## 2. The minimal model and the classification inputs

Let q:T→T0 contract the finite sequence of point blowups from the minimal model, and let k be the number of those blowups. The exact P4.12 input gives κ(T0)=−∞. Thus p_g(T0)=0. The argument divides according to the minimal surface classification, with primary scope as follows.

For the Kähler case, the previously opened Kodaira1954 Main Theorem (original pp.314–315; all original pp.313–316 read) applies after choosing an integral Kähler class. Such a choice exists on T0 because p_g=0 gives H^{2,0}=H^{0,2}=0, so every real H2 class has type(1,1); rational classes are dense, and the Kähler cone is open. Multiply a rational Kähler class by a positive integer to make it integral. Kodaira's theorem gives the holomorphic section embedding Φ:T0→P^N. This is the exact identification with the projective surface to which Beauville's classification is applied. No categorical transfer is left implicit.

In the opened original Beauville monograph, *Surfaces algébriques complexes*, Astérisque54(1978), TheoremVI.17 p.111 and CorollaryVI.18 p.112 give the ruled/rational conclusion for κ=−∞; the complete proofs at these loci were read in the earlier WM primary opening. The cited surface is Φ(T0), and its ruling is pulled back through Φ^{-1}. The minimal rational possibilities P2 and the Hirzebruch surfaces F_n (n≠1) are supplied by V.10 pp.79–80, with proof already read. The minimal nonrational ruled case is III.10 p.40, with proof read. Thus T0 is P2 or a P1-bundle over a smooth compact curve C of genus g≥0.

For the non-Kähler case, the opened Ornea–Verbitsky–Vuletescu arXiv1810.05768v3 (26June2020, byte-identical to the attached source) states in Theorem5.1, PDFp.27, that a minimal non-Kähler surface is isotrivial elliptic or classVII; the complete four-step proof was read. Its isotrivial elliptic alternative can overlap classVII. In the elliptic alternative the opened Theorem4.2/Corollary4.3 and local cyclic construction yield e(T0)=0 and K_T0^2=0; the holomorphic Noether identity gives χ(O_T0)=0. Since p_g=0, this implies h1(O_T0)=1. The opened Theorem2.5 gives b1=2h1(O)-1=1 for a non-Kähler surface. Together with κ=−∞ this puts the elliptic alternative in classVII as well. Hence the non-Kähler minimal T0 in the present problem has b1(T0)=1 and b2(T0)≥0.

For clarity about the elliptic numerical transport: Theorem4.2 gives the local elliptic action and isotrivial fibration p:T0→C. On its cyclic product cover the derivative quotient has K=p^*K_C(R_p). The ramification divisor is a sum of fibres, so its self-intersection and its intersection with pulled-back divisors vanish, giving K^2=0. All fibre supports are elliptic and their smooth product covers identify the Euler contribution as zero, giving e=0. These are the same maps and computations recorded in the already opened WM primary-scope record. They do not identify the isotrivial and classVII names by terminology alone; the calculated b1=1 and κ=−∞ verify the defining conditions.

## 3. A ruled base of genus at least two is excluded by the actual π1 maps

Suppose the minimal model is a P1-bundle p:T0→C. Local triviality of this bundle and simple connectedness of P1 give an isomorphism p_*:π1(T0)→π1(C). Concretely a base loop lifts to a path in the total space and can be closed within the connected fibre; a homotopy of base loops lifts over its parameter square, and the remaining fibre loop is null because π1(P1)=0. These two constructions prove surjectivity and injectivity.

Each point blowup induces an isomorphism on fundamental groups. In local complex coordinates the blowup replaces a four-ball by the disk bundle of O_{P1}(-1), with the common boundary S3. Both the ball and the new disk bundle are simply connected (the latter retracts to P1), and the boundary is simply connected. Van Kampen applied to the complement of a slightly smaller ball and either local piece gives the same π1 and identifies the two maps through the blowdown. The local blowdown is ([u:v],a)↦(au,av) in the tautological line; thus the map is the actual q in our surface, not an abstract group identification. Iteration gives q_*:π1(T)→π1(T0) an isomorphism.

The composite

    π1(S) --(ν_*)^{-1}--> π1(T) --q_*--> π1(T0) --p_*--> π1(C)

is therefore an isomorphism. Y2 supplies a finite-index abelian subgroup of its domain, and so π1(C) is virtually abelian.

For g≥2 this is impossible. Let H be a finite-index abelian subgroup of π1(C), of index d. The corresponding connected unramified topological covering C_H→C is a compact orientable surface. Lifting a finite cell decomposition proves e(C_H)=d e(C), so its genus is g_H=1+d(g−1)≥2. Its fundamental group has the presentation with generators a_i,b_i and sole relation ∏[a_i,b_i]=1. Map a_1 and a_2 to the two free generators x,y, and all b_i and all remaining a_i to the identity. The relation maps to the identity, giving an epimorphism π1(C_H)→F2. The reduced word xyx^{-1}y^{-1} is nontrivial, so F2 is nonabelian. Thus π1(C_H)=H cannot be abelian. This contradiction proves g≤1 for the actual ruling.

This argument uses no injectivity claim for a conductor curve and no replacement of the possibly nonnormal support by a normalization unless justified by the assumed bijection. The exact ν homeomorphism is essential.

## 4. Euler identities through the actual blowdowns

The Euler characteristic of a P1-bundle over a genus-g curve is

    e(T0)=e(P1)e(C)=2(2−2g)=4−4g.

To prove the multiplication here, take the usual finite cell decomposition of C with one zero-cell, 2g one-cells and one two-cell. Trivialize the bundle over each open cell. Its fibre has a cell decomposition with one zero-cell and one two-cell. Additivity of Euler characteristic over this finite decomposition gives degree counts 1,2g,2,2g,1 and the displayed alternating sum. The attaching maps of a nontrivial bundle do not alter the count. For P2, its usual cells in real dimensions0,2,4 give e(P2)=3.

One point blowup has Euler increment one. Its blowdown is an isomorphism away from the exceptional P1 and replaces that P1 by one point. Additivity over the exceptional divisor and its complement gives

    e(blowup)=e(original)−e(point)+e(P1)=e(original)+1.

Equivalently, the local disk-bundle replacement in §3 adds one middle-dimensional class. Iterating along q gives e(T)=e(T0)+k.

The projective alternatives therefore have

    e(T)=3+k       for T0=P2,
    e(T)=4−4g+k   for a P1-bundle over C.

By §3, g is0 or1. These Euler numbers are nonnegative. The first and the g=0 case are strictly positive. In the g=1 case e(T)=k, so zero occurs exactly when k=0 and T itself is the minimal ruled surface over the elliptic curve C.

For classVII, b1(T0)=1 by definition, and orientation plus Poincaré duality gives b3(T0)=1 and b0=b4=1. Hence

    e(T0)=1−1+b2(T0)−1+1=b2(T0),
    e(T)=b2(T0)+k.

This is nonnegative. Equality forces both b2(T0)=0 and k=0. Thus T=T0 is already a minimal classVII surface with b2=0.

The new prerelease program `code/S6_SERIES_PUBLISH_II_A_02YD_euler_cells.py` performs these calculations by formal cell-degree convolution and alternating coefficient sums in the symbolic variables g,k,b. It verifies the universal polynomial identities, including the local blowup increment, rather than sampling integer values. Its run receipt and full output are bound before freeze. The classification and genus exclusion are proved in this document and are not delegated to the program.

## 5. The class-VII zero case is exactly Hopf

In the remaining zero case, k=0 and b2(T)=0, while the conductor divisor from §1 is nonempty. Apply the already opened Buonerba–Bogomolov–Kurnosov arXiv1709.00062v3, Theorem1 on p.1 (PDFpp.1–2 and the exact attached theorem text were read): there is a finite étale covering a:T'→T with T' a Hopf or Inoue surface. Its conclusion is a cover, so it is not directly read as an isomorphism T≅T'.

The inverse image a^{-1}(D_red) is a nonempty compact curve: a is finite and surjective, and local étale coordinates preserve complex dimension. Inoue's original 1974 paper proves that the families S_M, S^+ and S^- contain no curves. The exact opened loci are Proposition2(i), p.274 continuing on p.275; Proposition3(i), p.277 with its explicit proof reference to Proposition2; and the unramified double cover paragraph after equation(21), p.279. The full page images at these loci were read in the earlier primary opening and their exact PDF/image hashes are retained. Therefore T' cannot be Inoue.

It follows that T' is Hopf. By the defining Hopf covering there is a universal holomorphic covering h:C^2\{0}→T'. The composition a∘h:C^2\{0}→T is a covering, because a is étale, and its domain is simply connected (it retracts to S3). Hence it is a universal covering of T. This exact composition proves that T is a Hopf surface. It is the map required to carry the cover conclusion to the target's Hopf conclusion; no equality between T and T' is asserted.

Conversely, a Hopf surface has e=0. One can see this either from its classVII b1=1,b2=0 invariants, or by the standard primary finite cover S1×S3 and the multiplicativity of Euler characteristic under a finite cover. Here the first is already part of the primary classVII zero classification. Thus, for the actual T in the statement, T Hopf gives e(T)=0. Similarly a minimal ruled surface over an elliptic curve has e(T)=0 by §4. Composing with the actual homeomorphism ν gives e(S)=0 in exactly the two claimed cases.

## 6. Conclusion and evidence boundary

We have shown e(S)=e(T)≥0 under the complete printed standing hypotheses. Its zero cases are exactly T minimal ruled over a genus-one curve or T Hopf. The bijective normalization condition was used only through its explicitly proved homeomorphism, and every classification transport was specified: Φ for the projective model, q for point blowdowns, p for the ruling, and a∘h for the Hopf covering. No normal-crossing or coefficient-one conductor condition was added.

Primary reuse is limited to actually opened sources and loci. The exact receipts are `S6_SERIES_PUBLISH_Beauville_1978_opened_scope_01.json` with its timing-precision supplement, and `S6_SERIES_PUBLISH_II_A_02WM_primary_scope.json`, which binds OVVv3, BBKv3, the original Inoue article, Kodaira1954 and the additional Beauville classification loci. These are source-reading records, not a prior YD check or derivation. The canonical YD proof is still closed at completion of this derivation. Freeze and release must precede any comparison with it.
