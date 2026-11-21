# Paper V: review of the integrated analytic chain

Checker: GPT-6 Astra (OpenAI), ChatGPT Pro mode, inherited effort, v_analytic_check. This follows the original-source checks recorded in `S6_SERIES_PUBLISH_V_analytic_check.md`. It records proof and dependency review of the integrated manuscript, not a final rendered-page review.

## Status and the origin of the clarifications

No contradiction to an original stated theorem was established in this analytic scope. The raw-coefficient normalization error arose in this checker's first proposed merger: it combined the raw primitive-decomposition coefficient with P1.15's fixed contraction without also rescaling the polarization bivector. Root caught that draft issue before accepting the normalization. The corrected replacement proves both scalars and the full wedge morphism explicitly. It is not recorded as an original-source refutation.

The original compact-filling proof conjugated base and fibres without stating the complex parameter transport. Its imaginary subfamily is fixed by the exact map xi_old=-conjugate(xi_new). The new canonical complex family needed that latent coordinate convention written at the construction step. The integrated proof now does so. This is a coordinate clarification, not a claim that an original real-family theorem was false.

## Normalization and dependency order

The integrated order is: rank-three bundle P and its splitting obstruction; algebraic Gamma_6 and sigma_b; normalized-height definition and well-definedness; merged lift/transversality/cusp theorem; exact conjugation map; compact filling; global height minimum; its endpoint application. It removes the former P1.15/P1.8 recorded cycle and the P1.16/P1.18 numerical proof cycle.

The primitive decomposition uses alpha_0=alpha_alg/8, alpha=(625 pi i/16)alpha_0 and omega_norm=(16/(625 pi i))omega_alg. Thus j(v)=v+alpha_0(v)omega_alg=v+alpha(v)omega_norm. The full map Psi=(625 epsilon/256) exterior-square Pi takes omega_norm to omega_c/2, and its induced primitive contraction is contr_(J_c). This is the exact real normalization in which alpha(n)=1 and sigma_b(n)-conjugate(sigma_b(n))=2i h_b e. Based meridians, not just unbased local conjugacy classes, determine X; the scalar commutant and Xe_0=e_0 prove uniqueness.

The old alternative splitting is related by the exact map already in PV04. In the convention sigma=sigma_b+z_0 alpha e, it reads xi_b=xi+z_0, h_sigma=h_b+Im(z_0), and c_sigma=c_b-Im(z_0). The boundary section now uses the canonical normalization throughout.

The added dependency guards record the actual inputs of compact filling, the real-system and conjugation inputs of the minimum, the threshold used to exclude the exceptional Hodge determinant, the intrinsic pencil/cusp inputs of the antiholomorphic obstruction, and the minimum/marking inputs of nonextension. The unused shifted-fivefold dependency in P1A.5 is removed. These are dependency corrections to the rewritten presentation.

## Exact conjugation and the compact family

The new exact calculation verifies K^2=I, K e_0=e_0, KA=A^(-1)K and KB=B^(-1)K. The anti-intertwiner equations have one-dimensional solution space; imposing K e_0=e_0 makes it unique. The rational-connection proof then identifies this real integral K with X conjugate(X)^(-1).

For W_xi=(Y_1,Y_2,Y_3+(625 pi i/96)xi e_0), direct substitution proves

conjugate(W_(-conjugate(xi))(conjugate(lambda))) = K W_xi(lambda).

This parameter map preserves the imaginary part. The actual compact-filling proof now starts from raw parameter -conjugate(xi), defines Fhat_xi=K F_xi, and obtains cohomology monodromies A^(-1), B^(-1) and homology monodromies A^t, B^t. Its cusp correction is C_new,xi(q)=-conjugate(C_(-conjugate(xi))(conjugate(q))). This expression is jointly holomorphic in xi and q. Finite affine actions and logarithmic gluing maps are holomorphic in xi; the bounded cusp correction admits a uniform small disc on each relatively compact parameter neighbourhood. Consequently the compact family is holomorphic in the declared coordinate xi.

The boundary proof now applies the fixed real integral change K^(-1) to the actual compact-family Hodge plane before comparing it with the raw algebraic graph F_xi. That exact marking map preserves real transversality. The finite-boundary failure locus and the locus at infinity both use h_b. The newly declared parameter domain is U throughout, including the punctured-disc classifying map and its Cayley transform.

The supplemental conjugation program initially used a structural SymPy equality between two algebraically equal expanded expressions; that harness assertion failed. Replacing it by simplification of their difference made the same mathematical identity pass. No matrix or parameter formula was changed. The final program/output/JSON are retained.

## Root gauges and the compact certificate proof

The regular-root identities are

H(u^4)D_0(u)=U_0(1)^(-1)U_0(u),

H(u^(-5))D_infinity(u)=U_infinity(1)^(-1)U_infinity(u).

They follow from equality of the transformed right equations and value I at u=1. Therefore H_infinity is the regularized limit lim_(u->0)H(u^(-5))D_infinity(u)=U_infinity(1)^(-1); it is not an ordinary limit of the meromorphic frame matrix. The exact coefficient maps are q_reg=D^(-1)q: at infinity the variable pair is (u^8 v_2,u^4 v_1), and at zero it is (u^(-6)v_2,u^(-3)v_1). Nontrivial root characters force the limiting regular coefficients to vanish, giving the endpoint-height formulas.

Any real invertible left change T fixing e_0 has block form (1,r;0,S). It preserves the condition that the lower five coordinates of Yq be real, changes its top coordinate only by a real number on that locus, and leaves the right equation Y'=YG unchanged. This proves exactly why the centrewise real preconditioning used by the supplied interval certificate preserves the computed height. Its formula and implementation remain in the saved program, while this mathematical justification remains in the proof.

The global minimum argument retains the strict central Hessian bound, the four strict outer-region bounds, the complete geometric coverage maps, and the positive inner-cusp determinant polynomial. These are whole-region inequalities. The shorter point theorem uses the same regenerated root certificate at H(1)=I; its 6.18e-76 radius is contained, by exact rational comparisons, in the retained wider interval and in both strict theorem endpoints. Its loop-to-root relation is an exact gauge identity, so it no longer repeats the entire numerical transport method. The full earlier proof and all diagnostic constants remain in the check record.

## Primary sources and executable inputs

The exact arXiv v5 Oka-1 PDF was fetched from https://arxiv.org/pdf/2303.15855v5 with HTTP 200. Definition 2.1 is the definition of tubes on p.4; Theorem 2.2 and Corollary 2.4 on p.5 concern Oka-1 consequences. The operative local-spray inputs are Definition 7.11, Remark 7.12 and the observation preceding Proposition 7.13 on p.23, followed by Proposition 7.13(d), p.24 for LSAP-fibre bundles. The table's tentative Theorem 2.1/Corollary 2.4 locator was corrected accordingly.

Ten original computational source URLs were fetched from the pinned workbench commit. Every response was HTTP 200, and each body matched both the attached source and its checkpoint-10 SHA-256 manifest entry. The four modules under code/paper_v are the operative interval certificate. The older exact-check and loop-comparison programs can remain in the check record. The receipt provides immutable URLs and hashes; no new-check script is made into a logical premise of the paper.

The additional cusp-line-bundle metric check proves the sign of sum S_ij a_i wedge b_j in the actual angular/deck convention. It is recorded separately and was supplied to the topology checker. The common cusp/deformation argument supports dimensions two and three after choosing a sufficiently small common disc; it permits nonsymmetric bounded corrections exactly as the opened Yang theorem does.

## Limits of this event

This integrated pass is a source/proof reread with exact supplemental calculations and coordinate derivations. It is not a blind re-proof of the whole paper, and it does not certify final pagination or visual layout. The independent numerical endpoint comparison, independent finite-cover verification, and supplied interval rerun remain separately described events. The exact integral admissible-data classification and the topological/fivefold arguments remain assigned to the topology checker.
