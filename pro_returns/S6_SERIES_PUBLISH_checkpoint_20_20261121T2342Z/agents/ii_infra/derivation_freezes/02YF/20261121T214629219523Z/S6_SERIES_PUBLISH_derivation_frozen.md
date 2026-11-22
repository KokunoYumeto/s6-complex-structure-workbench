# 02YF / night:P4R.3: independent prerelease derivation

The complete target proof, outline and prior target code remain unopened. The simultaneous 02WU target proof is also closed. This file derives every assertion of P4R.3 from its exact statement, the safe cited inputs, the original Beauville monograph already opened, and the conductor relation with its explicit resolution map. The argument below treats repeated images of rational components directly.

## 1. Standing objects and exact numerical model

Let f:Y→B be the standing proper connected-fibre torus fibration, with Y smooth compact, b1(Y)=b2(Y)=0 and B a smooth compact curve. Let mS be the irreducible full fibre, with S singular and reduced, and ν:T→S its smooth normalization. Its minimal model T0 is ruled over a smooth curve E of genus g≥2. Let D be the full conductor on T, R=D_red and C=Sing(S)_red. The finite normalization identifies T minus R with S_reg and maps every curve component of R nonconstantly to C.

The A.5.3 input is used with the identity as the minimal resolution of T. Its exact map h is ν, so ω_T(D)=ν*ω_S with D the full scheme-theoretic divisorial conductor. P4.12 gives torsion ω_S. Thus K_T+D is numerically zero. The Kodaira-dimension assertion of P4.12 is not needed here because the target already specifies the ruled minimal model.

Beauville III.10, p.40, identifies T0 with P_E(V). Its proof extends the rational map to E using point blowups and removes the last exceptional curve because any map P1→E is constant. The point-blowup morphisms and their common-resolution factorization are II.3 pp.17–18, II.7 pp.20–21 and II.11–12 pp.23–24. The same local constructions apply to the analytic surfaces, giving the actual map q:T→T0 used here.

For h=c1(O_P(V)(1)) and F a fibre, III.18 pp.46–47 gives h²=deg V, h·F=1 and F²=0. Write K=a h+bF. Adjunction on F gives a=−2. A section has class h+rF and genus g; its adjunction gives b=deg V+2g−2. Therefore

K_T0²=8(1−g),   e(T0)=4(1−g).

The Euler formula is also the sphere-bundle count 2e(E). A point blowup adds one to Euler number and replaces K by q*K+E_exc, decreasing its square by one.

## 2. The conductor on the minimal ruled model

Let D0=q_*D. The numerical conductor relation descends through q, since the exceptional summand in Picard/cohomology is independent, and gives K_T0+D0≡0. In particular D0·F=2. Its horizontal part is either two sections, one irreducible bisection, or one coefficient-two section, together with vertical fibres V=Σa_jF_j.

Two distinct coefficient-one sections H1,H2 would give, by adjunction on H1,

2g−2=(K+H1)·H1=−H1·H2−Σa_j≤0,

contrary to g≥2. An irreducible coefficient-one bisection H would give p_a(H)=1−Σa_j≤1, while the degree-two map of its normalization to E gives geometric genus at least 2g−1≥3 by Riemann–Hurwitz. This is also impossible. Therefore

D0=2H+V,

where H→E is a section and hence an isomorphism. The reduced support R0 is H with rational fibres attached at distinct points, each in one transverse intersection. Thus R0 is connected, and collapsing each rational fibre to its attachment point is a homotopy equivalence R0→H. The bundle projection induces π1(T0)≅π1(E), and the section gives its inverse. Hence inclusion R0→T0 induces an isomorphism on fundamental groups.

This independently derives the asserted double-section form in A.5.3 in the present smooth ruled case. No target proof for A.5.3 or P4R.3 is opened to obtain it.

## 3. Every blowup preserves the inclusion isomorphism

For a reversed point blowup q_j:T_j→T_(j−1), let E_j be its exceptional curve and D_j the conductor transform. The full nonexceptional divisor pushes to D_(j−1). Since K_j=q_j*K_(j−1)+E_j and K_j+D_j has zero numerical class, the exceptional coefficient gives

D_j=q_j*D_(j−1)−E_j.

Thus the new exceptional coefficient is μ_j−1, where μ_j is the old conductor multiplicity at the centre. Effectivity forces μ_j≥1, so every centre lies on the conductor.

When μ_j=1, the conductor is smooth and reduced at that point; its strict transform is isomorphic to it and the exceptional curve is absent. When μ_j≥2, the exceptional P1 is part of R_j. The map R_j→R_(j−1) is a homeomorphism off E_j and collapses exactly E_j to the centre. By properness and compactness, the target is the quotient by that connected simply connected subspace. A compatible triangulation makes it a cofibration, and van Kampen gives an isomorphism of fundamental groups. The blowup map T_j→T_(j−1) also induces a π1 isomorphism: locally it replaces a four-ball by the disc bundle of O_P1(−1), with simply connected boundary S3.

Both maps commute with the conductor inclusions. Starting from the isomorphism in Section 2 therefore proves, through the commutative squares at all stages,

π1(R)→π1(T) is an isomorphism.

The support has one strict transform H' of genus g and a tree of rational curves attached to it. This follows geometrically as well: a blowup at a smooth conductor point adds a rational leaf or no component, while a blowup at a node subdivides the corresponding edge. The initial support is nodal, and those operations preserve nodality and the tree incidence.

## 4. The normalization pushout

The finite normalization ν realizes S as the quotient of T which identifies precisely the points of R having the same image in C. Its restriction outside R is an isomorphism. The quotient is a homeomorphism onto S because T is compact, S is Hausdorff and the finite map is surjective. Thus S is the topological pushout of R⊂T and R→C.

Choose a triangulation compatible with the compact analytic pair and the finite curve map; R⊂T is a cofibration. Its ordinary pushout has the fundamental group of the corresponding mapping-cylinder pushout. Since R,T,C are connected, van Kampen gives

π1(S)=π1(T)*_(π1(R))π1(C).

The first arrow from π1(R) is an isomorphism by Section 3, so the inclusion-induced map π1(C)→π1(S) is an isomorphism. This is the claimed normalization-pushout map, not merely an abstract group equality.

No injectivity of the component-image correspondence was used. In particular, different rational curves lying over different ruling fibres may map to the same irreducible component of C; their images are handled by the single finite map R→C in this pushout.

## 5. All possible image-curve fundamental groups and Euler numbers

Only H' can dominate a component of C with positive normalization genus: a rational component maps through its smooth normalization, and a nonconstant map from P1 forces the image normalization to have genus zero. Thus C has at most one positive-genus normalization component.

For any connected reduced compact curve C, replacing it by its normalization and then identifying the finite sets above singular points gives

π1(C)=(*_i π1(C_i^ν))*F_b,

where b is the first Betti number of its incidence graph. If c is its number of irreducible components and h_i their normalization genera, the same finite point-identification model gives

e(C)=c+1−b−2Σh_i.

Explicitly, if a singular point p has r_p local branches, the normalization sequence of topological spaces removes Σ(r_p−1) points in Euler number, and b=Σ(r_p−1)−c+1. This proves the displayed identity even at unibranch singularities, where r_p=1 contributes zero topological identification.

P4R.1 gives π1(S) an abelian normal subgroup with finite cyclic quotient, so Section 4 makes π1(C) virtually abelian. A positive-genus normalization component cannot have genus h≥2: projection onto its surface group is a quotient of π1(C), and a finite-index subgroup of that surface group is the group of a finite unramified cover of genus 1+d(h−1)>1, hence is not abelian. Thus the only possible positive genus is h=1.

If all components are rationally normalized, the group is F_b. The finite-index rank formula 1+d(b−1) forces b≤1, and e(C)=c+1−b≥1. If exactly one component has genus one, the group is Z²*F_b. A positive b gives a quotient F2 by retaining one elliptic generator and one graph generator, impossible for a virtually abelian group. Hence b=0 and e(C)=c−1≥0. In every case e(C)≥0.

The only zero-Euler case in this classification is c=1 with elliptic normalization and b=0. A curve with unibranch singularities may have that topology; the next step handles it without assuming smoothness.

## 6. Strict positivity and the zero-case contradiction

Suppose the image-curve Euler number equals zero. Then its unique component has elliptic normalization. Every rational component of R would have a finite nonconstant map to that component and hence to its normalization; Riemann–Hurwitz rules this out. Therefore R consists only of H'. There were no vertical conductor fibres on T0 and no blowups: the first possible blowup would be centred on 2H, have μ=2 and introduce a rational exceptional conductor component, whose strict transform persists at all later stages. Thus T=T0 and R=H.

For those exact maps, e(T)=4(1−g) and e(R)=2−2g. Since T minus R identifies with S_reg,

e(S_reg)=e(T)−e(R)=2−2g<0,

contradicting the P4.13 input e(S_reg)≥0. Hence the zero image-curve case cannot occur. In fact e(C)>0 in this setting, which gives the stated e(C)≥0 and

e(S)=e(S_reg)+e(C)>0.

This completes every target conclusion, including the precise inclusion and pushout isomorphisms and the allowance for repeated images of rational conductor components. The proof is unconditional under the target's stated hypotheses.

## 7. Primary and computational scope

The primary surface formulas are from Beauville, Surfaces algébriques complexes, Astérisque 54 (1978), the actual publisher-archive PDF already opened. The exact loci are III.10 p.40, III.18 pp.46–47 and the local point-blowup/common-resolution results II.3 and II.7–12 cited above. The conductor relation is the safe A.5.3 statement with identity resolution. P4.12 supplies the torsion line, P4.13 supplies the open-stratum sign and P4R.1 supplies the virtually abelian group. Only their stated conclusions are used; no unreleased proof of them has been read for this derivation.

The new program S6_SERIES_PUBLISH_II_A_WU_YF_ruled_cells.py was authored from scratch while both this target and 02WU remained closed. It uses weighted divisor trees and explicit rational-leaf contractions, performs the actual μ−1 blowup operations and calculates the conductor/surface/open Euler counts. It computes the allowed image-curve Euler cases and the contradiction value −2(g−1). Its general mathematical justification is given in Sections 2–6; finite cases are implementation certificates only. The additional Chern and low-jet parts belong to the simultaneously derived 02WU scope and are not used as extra proof inputs for this target.

The first stage-output metadata retained a mutable weight-list reference; it was detected by reading the output, preserved with its original program/receipt, and corrected before either proof freeze. The final run exited zero at 2026-11-21T21:43:47.234651+00:00. All 64 final divisor-stage records and every remaining output section were printed and read before this derivation was frozen. No historical routine has been opened or reused for either target.

## Exact input and computation bindings

The binding appendix is added by a separate hash-only step before freeze. Both target proofs remain closed when this complete derivation is written.

Binding recorded 2026-11-21T21:46:28.485810+00:00.

- agents/ii_infra/statement_packets_v2/S6_SERIES_PUBLISH_II_02YF_statement_inputs.tex — SHA256 5161412c16ccab2641e108517d75c80d8a735a90569445eb12396956042c99ca.
- agents/ii_infra/statement_supplements_v1/S6_SERIES_PUBLISH_II_02YF_cited_input_supplement.tex — SHA256 92c5c5e5b94ee6086601638af4cba782fac7b3298907c4fcbc27ac533fd2b7a8.
- agents/ii_checks_A/recovery_20261121T195642Z/S6_SERIES_PUBLISH_II_WM_WS_safe_scope_01.json — SHA256 8070638508547ad0e9b1b5748f4562bd65c387c4161d55c8bc9f30b2c2fbc7c4.
- agents/ii_checks_A/recovery_20261121T195642Z/S6_SERIES_PUBLISH_II_01BB_resolution_conductor_inputs.tex — SHA256 dc327be8fa7560c681198fed9fca6e88468ddbb830008c4975753e9e6220a4b0.
- agents/ii_checks_A/recovery_20261121T195642Z/S6_SERIES_PUBLISH_Beauville_1978.pdf — SHA256 a2bdff071df610a8e39200a16ad7675149c1ddf601157b3e3e56cbf285994e4e.
- agents/ii_checks_A/recovery_20261121T195642Z/S6_SERIES_PUBLISH_Beauville_1978_opened_scope_01.json — SHA256 0d2ea94f1a73cee925d69c09fa90003cee229c1d35871e79024ded0e59a2b245.
- agents/ii_checks_A/recovery_20261121T195642Z/group07_WT/S6_SERIES_PUBLISH_II_A_02WT_reading_precision.json — SHA256 5346326bee017ed8dfe21a3022202abf3f40943a81ffa54ac4d704566bb758a7.
- code/S6_SERIES_PUBLISH_II_A_WU_YF_ruled_cells.py — SHA256 33f8dad777fef0cc6129aa1f77136f4e4f7beed0068081a336a4041e34697a34.
- code/S6_SERIES_PUBLISH_II_A_WU_YF_ruled_cells.out — SHA256 56524f9f0c9ef4a320dc80d866cbf0753896f469bb681a87c7f08c4b38d38030.
- agents/ii_checks_A/recovery_20261121T195642Z/S6_SERIES_PUBLISH_II_A_WU_YF_ruled_cells_run.json — SHA256 71299a19d52cc2382473390e4a39c863533589db7e73d4ec5e2d4a617f416063.
- agents/ii_checks_A/recovery_20261121T195642Z/S6_SERIES_PUBLISH_II_A_WU_YF_first_attempt_correction.json — SHA256 66d380562fab0ecbba4856912cdbd17c7e4ac87187da5032b817cbadc6c13dd9.
