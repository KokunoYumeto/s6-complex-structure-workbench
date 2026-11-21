# Paper V: analytic and complex-geometric check

Checker: GPT-6 Astra (OpenAI), ChatGPT Pro mode, inherited effort; S6_SERIES_PUBLISH / v_analytic_check. Work began 20 November 2026, approximately 22:45 UTC. This report concerns the corrected attached Paper V, not the earlier checkpoint-10 wording. It records both completed checks and their limits.

## Scope and outcome

The checked chain comprises the global lifted period construction (maps:src:F.3.6 and night:P1.8), the normalized connection/height/minimum (night:P1.15–16 and night:P1.18), the local Kuhn filling (night:P1.9), Theorem E's coherent cohomology, Hodge numbers, deformation, automorphism and boundary claims (night:P1A.1–6 and night:P1.17), and the analytic assertions of Theorem F (maps:src:F.3.4 and F.3.8–11).

No contradiction to a stated mathematical result was found in this scope. The rewrite exposed an implicit scalar in the height definition and a parameter map in the base/fibre conjugation. Both have now been made explicit and independently computed. The exact classifications F.2.37–39 are being checked by the topology agent, and are not certified by this analytic report. The source's cited theorems remain cited inputs; reading their exact statements is distinguished below from reproving them.

The file S6_SERIES_PUBLISH_V_analytic_preread.md was written before the printed proofs were read. It contains independent derivations of the root-line cohomology and canonical class, the one-dimensional Kuranishi criterion, the punctured-disc parameter/filling argument and the topological section step for the Oka construction. Other steps were checked after reading, and the events identify them as such.

## The exact normalization that the height definition needs

In the algebraic frame, put omega_alg = 3 omega_03 + omega_12. Contraction with the residue pairing J_03 = 4/3, J_12 = 4 takes omega_alg to 8. For v in P, the contraction is applied to its unique wedge lift j(v), not to its primitive representative. The raw primitive coefficient is therefore alpha_0 = alpha_alg/8. The normalized contraction of night:P1.15 is

alpha = (625 pi i/128) alpha_alg = (625 pi i/16) alpha_0.

Thus the primitive-decomposition identity is precisely

j(v) = v + alpha_0(v) omega_alg = v + alpha(v) omega_norm,

where omega_norm = (16/(625 pi i)) omega_alg. Omitting this scalar silently identifies two normalization conventions. The supplied replacement keeps both explicitly and then uses only alpha and sigma_b in the paper.

The real comparison is also explicit. Let the companion integral cup form be epsilon J_c, where epsilon is the sign in night:P1.7, and let omega_c = (1,1,1,1,1,1) be its invariant wedge vector. Its J_c contraction is 2. The period comparison Pi satisfies Pi^t (epsilon J_c) Pi = 2 pi i J by the residue formula (obtained by the boundary integral on a cut polygon). Consequently exterior-square Pi takes omega_alg to (8 pi i/epsilon) omega_c. The extension's cusp-normalized comparison is induced by the full wedge map

Psi = (625 epsilon/256) exterior-square Pi.

The scalar follows from the residue ratio (625/192)/(4/3) = 625/256 and the factor 2 pi i in logarithmic monodromy. The one-dimensional extension calculation lifts its quotient to the complete rank-six comparison fixing e. Thus Psi(omega_norm) = omega_c/2, and the induced primitive contraction is the real J_c contraction. This proves that the normalized real vector n with alpha(n)=1 exists and is unique; it is not an inference from a numerical real-system solution.

The independent numerical guard reconstructs rank-four periods separately by DOP853, normalizes their cup form, and compares their wedge quotient to the independent rank-six calculation. It returns the scale 2.441406249999998 + 2.36e-16 i, compared with 625/256 = 2.44140625. The largest rank-five discrepancy is 1.36e-13; the image of omega_norm differs from omega_c/2 by 3.29e-16. These are floating-point comparisons; the proof is the residue/cusp calculation above.

## The conjugation parameter map

Put k = 625 pi/96. In the fixed flat marking the period columns are W_xi = (Y_1,Y_2,Y_3+ki xi e_0). The real normalized matrix K = X conjugate(X)^{-1} satisfies K^2=I, K e_0=e_0, and Y(conjugate(lambda)) = K conjugate(Y(lambda)). Direct substitution gives

conjugate(W_{-conjugate(xi)}(conjugate(lambda))) = K W_xi(lambda).

Thus the combined base and fibre conjugation used to obtain homology matrices A^t,B^t acts on the family parameter by xi -> -conjugate(xi). It preserves Im(xi)>c_* and fixes xi=ic. This explicit map makes the conjugated construction holomorphic in the stated coordinate xi. A replacement numbered remark is supplied.

## Connection and period minimum

A new exact program reconstructs the rank-four Gauss–Manin connection from the polynomial identity for differentiating x^k dx/y, reduces modulo exact differentials, takes its exterior square and quotients the invariant bivector. All 25 entries of the displayed quotient connection agree. The rank-six cusp residue has square zero and rank three. No supplied audit program was imported for this reconstruction.

The full supplied Arb certificate was then re-executed from its attached source, with a fresh output directory. This regenerated the normalized root frames, the endpoint balls, all four central Hessian squares, the whole inner cusp determinant bounds, and all 1,600 outer rectangles. Its saved-certificate verifier passed. A first verifier invocation reached its mathematical tests but failed while recording paths because the output directory was external to its own tree; placing the generated output beneath the program directory resolved that bookkeeping assumption without changing mathematics or source.

A new independent endpoint program uses adaptive Dormand–Prince 8(5,3) integration and all-root-frame intertwiner equations, rather than the certificate's Taylor recurrence or Arb. At the tightest tolerance it gives c_* = 1.094540250311401, h_b(0) = -0.9317933763565212 and h_b(1) = -1.034276622416319. The three tolerance runs agree with the certified values to approximately fourteen digits. This is an independent floating-point comparison, not a replacement interval enclosure.

A second new program verifies the finite whole-base cover by different exact methods: vertical-slab tiling checks replace the source verifier's quadtree-prefix argument, and rational bivariate Bernstein bounds for |1+w^5|^2 - |w|^10/16 replace its complex-ball inverse-power cusp exclusions. All 96 cusp exclusions pass without further subdivision. The exact areas are 2401/2500, 2401/2500, 1/8 and 10609/10000. All 1,088 serialized strict height bounds, four Hessian bounds and four inner cusp determinant coefficients pass rational comparisons. This independently verifies the finite coverage and signs; the ODE interval enclosures themselves come from the separately recorded rerun.

The compact replacement for night:P1.18 retains the precise connection inputs, root maps, tail estimate, implicit derivative formulas, full-domain covering maps, strict outer bounds, Hessian lower bound, inner cusp graph and determinant polynomial. It removes software versions, commands, implementation choices, check counts, program paths and duplicate alternative-splitting decimals from the proof. The supplied full derivation and outputs remain in the check record.

## Theorem E: checks of the complete analytic chain

- Direct images: the explicit primitive intersection gives V/F as an extension of L^{-1}+L^{-2} by O. The root-line formula makes the relevant extension group vanish. At the cusp, the toric normalization complex is the dual three-torus with exterior cup product; the logarithmic invariant classes identify its cohomology with the quotient extension. Constant fibre dimensions and Grauert base change therefore give R^q h_* O = exterior^q(O+L^{-1}+L^{-2}). The root-character calculation, not merely degree, gives K_base=L^{-9}; the logarithmic determinant gives K_M=h^*L^{-6}. The independent degree sums give h^q(O_M)=(1,1,0,0,0).
- Hodge table: the projected residue was independently computed from Gamma_6 and the lifted plane. Both displayed connecting matrices and their opposite determinants agree. The sole exceptional parameter is 5i/(3pi), outside Im(xi)>c_*>1. The residue resolutions, toric coherent vanishings, Serre duality and the independently recomputed chi_y=-y+4y^2-y^3 give the printed table. In particular its ordinary/logarithmic comparison uses the entire branch residue sequence at self-intersections, not only its smooth-stratum restriction.
- Tangent cohomology: the line-weight calculation gives (1,2,1,0,0) for h^*L^5 and (0,0,0,1,1) for h^*(F tensor L^{-6}); the nonzero residue of the sole global logarithmic section removes the degree-zero term. Serre duality gives (1,1,1,2,0). The parameter derivative has rank one and the base derivative is invertible, so the global parameter class survives the normal tangent sequence. The nonzero derivative into a one-dimensional miniversal germ kills its defining ideal and proves smoothness.
- Algebraic dimension and automorphisms: the independent simultaneous alternating-invariant system has rank 15, so a horizontal effective divisor would have zero Chern class on a torus and strictly positive Kähler pairing, a contradiction. The three intrinsically distinguished special values force the base automorphism to be the identity. The independent common centralizer has dimension one. The order-five affine cap excludes -I. The displayed integral lattice quotient has Smith factors 1,1,2, and the fixed half-period splits the additive translation extension. Hence the full automorphism group is C times Z/2 and the parameter is injective on isomorphism classes.
- Antiholomorphic isomorphisms: the exact anti-intertwiner system has dimension one; R and -R are its only unimodular scalar choices. The finite cap excludes R. The based cusp change gives the printed P block, and -P e_2=(0,-1,1), outside the prescribed primitive ray set. Bounded angular translations preserve the linear fan action. All computations agree with the printed obstruction.
- Nonextension: the anticanonical fourth power has the two sections lambda^18, lambda^19 and recovers the pencil. Proper-image and coherent base-change arguments make every exceptional set away from the central parameter a proper analytic subset. On the complementary regular locus, evaluation gives three independent closed forms, hence compact tori. Identity of the marked period maps then contradicts real transversality along a real hypersurface, which cannot lie in a proper complex-analytic subset of the two-dimensional base. The finite ramified-coordinate variant preserves these noncentral hypersurfaces.
- Punctured discs: this argument was derived before reading. The unique local classifying maps glue by parameter injectivity. The Cayley coordinate is bounded and extends, with interior limit by the maximum principle. A double cover kills the Z/2 torsor and H^1(Delta*,O)=0 kills the additive torsor. The pullback of the compact family extends smoothly. The printed proof agrees with that derivation.

The first five bullets were checked by a combination of proof rereading and new exact computations. They are not described as independent re-proofs in the event log. The last bullet merits a targeted proof-check event because its derivation was recorded first.

## Theorem F: analytic scope

The nine spanning tube directions have determinant -16 by a new exact calculation. For the six nonskew directions, their transverse squared singular values are (1+qs)^2+qs^2 with q=1 or 2; completing the square gives the bound 1/(q+1). The skew directions have least singular value at least one. Perturbations of Frobenius norm below 1/4 therefore remain in the positive-determinant graph chart. Transitivity carries this tube to every point. The opened Oka-1 source supplies precisely the LSAP and bundle-section implications used.

The isolated-point extension proof was checked as a relative exhaustion proof. All new attaching arcs lie away from the exceptional cusp point. The old spray is vertical and fixes the prescribed finite jets; its domination is needed only on those attaching arcs. Openness retains its old image, LSAP controls the new image, and summable approximation errors give a limiting holomorphic section. This does not require a fibre-bundle assertion over the cusp point.

In the bounded-cusp theorem the enlarged bundle is actually open: near each finite C_0 the growing positive scalar y(t) dominates Im(C), uniformly on a bounded C-neighbourhood. Thus the added cusp fibre is the affine chart of graphs. A local polynomial realizes any finite jet. Connectedness and simple connectivity of D_3 extend that section continuously away from the cusp disc, and the relative section theorem preserves its jet. Undoing the logarithmic gauge gives exactly Z=log(t)I/(2pi i)+C(t), with C holomorphic at zero. The other marked points remain punctures throughout; no compact filling at those points has been inferred from this result.

The abelian-surface exclusion uses Deligne's semisimplicity in its stated algebraic scope. With maximal rank-two square-zero cusp, invariants and coinvariants of the rank-four middle system vanish. The two trivial rank-one outer pieces of the rank-six filtration then make its fixed space and its dual fixed space both one-dimensional. The Euler-parity calculation gives the asserted contradiction to b_1=b_2=0. No proportionality of the two source sections enters the argument.

## Primary sources opened

1. Alarcón–Forstnerič, Oka-1 manifolds: attached source S6_PUBLISH_literature_arxiv/2303.15855/V1.tex, Definition def:LSAP, Remark rem:LSAP, the observation immediately before Proposition prop:LSAP and that proposition (arXiv v5 Proposition 7.13, pp.23–24). Spanning tube domination, LSAP and LSAP-fibre bundle implications verified. Published metadata verified at https://link.springer.com/article/10.1007/s00209-025-03833-4: Math. Z. 311, article 33 (2025).
2. Forstnerič–Prezelj, https://arxiv.org/pdf/math/0101040, arXiv v3, Theorem1.2, printed p.3: the frame bundle over an open Riemann surface has the required dominating fibre spray (g,A)->g exp A. The holomorphic frame used by the isolated-point proof follows.
3. Deligne, Hodge II, https://www.numdam.org/article/PMIHES_1971__40__5_0.pdf, Definition4.2.4 and Proposition4.2.5, p.44; Theorem4.2.6, p.45. The exact algebraic/semisimple scope used in F.3.4 was read.
4. Yang, attached source Compact_Complex_Threefolds_REPAIRED_v4_5.tex, thm:higher-dimensional-periodic and cor:kuhn-euler, cited Theorem8.7/Corollary8.8 pp.57–59. The arbitrary nonsymmetric correction and uniform compact-parameter properness are explicit. The substitutions n=3,B=I,D=C and D(q,s)=sC(q) give the common cusp and its smooth comparison. The provenance agent independently matched this exact attached source byte-for-byte to arXiv:2609.29666v1; its receipt is in the provenance subdirectory.

## Replacement files and exact preservation

- S6_SERIES_PUBLISH_V_period_merger.tex combines original Theorems6.6 and6.7 (baseline pages42–46). Both statement labels/tags remain. The duplicated lifting and intersection arguments occur once. Its F.18/F.19/F.20 labels move to the height definition below; every other F.13–F.23 label/tag stays in the merged proof.
- S6_SERIES_PUBLISH_V_hb_definition.tex replaces Definition8.2 (baseline p.52), proves well-definedness without invoking the later transversality theorem, makes the contraction scalar explicit, fixes the based meridians for X, and gives one exact change-of-splitting remark without a second numerical normalization.
- S6_SERIES_PUBLISH_V_parameter_morphism.tex records the exact xi -> -conjugate(xi) map in the compact-filling construction.
- S6_SERIES_PUBLISH_V_minimum_compact.tex replaces Theorem8.4 (baseline pp.55–63), retaining its equation/layout tags and its unique-minimum result. The alternative splitting's numerical constants are retained only in these records and the regenerated certificate.

These are replacement passages, not a claim that the final integrated Paper V has already been typeset or page-read. Root integration, final label/tag checks, page numbers and rendered-page review remain separate.
