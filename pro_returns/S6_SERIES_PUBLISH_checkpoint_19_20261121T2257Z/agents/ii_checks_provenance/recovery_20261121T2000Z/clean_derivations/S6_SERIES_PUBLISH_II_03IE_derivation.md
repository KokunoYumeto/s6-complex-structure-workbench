# Prereading derivation: wbII:lem:picard-finite-norm (03IE)

Fix one actual finite filling of order m, with invariant integral vector v. Pull back the clockwise meridian to its full root circle s(theta)=r exp(-2 pi i theta), 0<=theta<=1. Its linear monodromy is the identity, and the crossed-cocycle identity gives z(rho^m)=N_T d. The pullback of the line bundle extends over the smooth torus family over the root disc. Its real homology marking extends over that disc and its fibrewise Chern class is E.

The supplied logarithmic overlap map from cap coordinates to flat coordinates is

    zeta_flat = zeta_cap + (log s)/(2 pi i) Pi_s v.

This direction follows directly from equivariance: the clockwise deck generator changes log s/(2 pi i) by -1/m, cancelling the affine translation v/m in the cap action. It is not an arbitrary coordinate convention.

On the pulled-back flat zero section the cap coordinate is

    - (log s)/(2 pi i) Pi_s v
       = theta Pi_s v + i (log r)/(2 pi) Pi_s v.

The real period map Pi_{s,R}:Lambda_R -> C^2 is an isomorphism. In its real coordinates this path is theta v + k(theta), where

    k(theta)=Pi_{s,R}^{-1}( i (log r)/(2 pi) Pi_s v ).

The function k is periodic on the full root circle. In particular the imaginary constant multiplying Pi_s v has not been silently treated as a real multiple of v. The path has integral endpoint difference v. For every nu in Lambda its swept torus in the cap has representative u nu+theta v+k(theta). The explicit homotopy replacing k(theta) by k(0)+t(k(theta)-k(0)) preserves the periodic endpoints and proves its homology class is the product (nu,v). The cap-disc trivialization gives Chern pairing E(nu,v).

On the original flat sweep Omega_E has zero integral, because one tangent direction is horizontal and the other vertical. The base-first sign in the defect definition therefore gives

    <N_Td,nu> = -E(nu,v) = E(v,nu)

for every integral nu. Equality on the basis gives N_Td=i_v E as an equality in V_R. Projecting to coinvariants replaces each T^k d by d, giving m dbar=[i_vE]. The same norm is obtained from the positive-meridian matrix or its inverse by the finite reindexing k -> m-k, so this calculation respects the stated clockwise meridian.

## Scope, exposure and exact inputs

This is a fresh derivation from the exact named statement and its safe cited-input packet and supplement. The target's printed proof, its method outline and old owner-specific check records remain unopened. All eight boundary derivations are being written together before any of their proofs is released. Paper I was extensively read in the earlier publication work, and its established construction is an input here; no claim of discovery independent of Paper I is made. The claim sought is a new derivation of this Paper II target before reading that target's proof. A later complete comparison and source review remain required.

The exact construction packet is S6_SERIES_PUBLISH_II_boundary_construction_inputs.json, SHA c92879fad86dfe710f2771af118d359bdfc51603c2219826a4e80e0f8d4bf7f6. It supplies the integral marking (gammahat, uhat, what, deltahat), the period matrix, finite affine actions, logarithmic connectors, cusp coordinates, toric rays, and the complete pre-IN Phi/Psi definitions. Safe statements supply the invariant and coinvariant lattices and the integral local specialization map. The displayed symbols in this derivation denote those exact maps.

For a chosen based loop g, A_g means its actual homology parallel transport and T_g=(A_g^{-1})^t. Current Paper I labels its positive base meridians counterclockwise, whereas these targets choose clockwise boundary meridians. Reversing a local meridian inverts its transport. For a finite order m transport, sum_{k=0}^{m-1} T^k equals sum_{k=0}^{m-1} T^{-k}, so the norm and the common invariant/coinvariant modules used below have the explicit inverse-loop transport. No unexplained equality of the positive-meridian product with the clockwise based product is used. The based boundary relation itself is taken in the target's zero-section whiskers.

The fresh program S6_SERIES_PUBLISH_II_boundary_preproof_exact.py and its output were written, executed, and completely read before target proof release. It uses Fraction elimination and integer coefficient-basis interpolation, and checks the finite norms, contractions, quadratic shifts, divisor degrees, support-form recovery and Chern matrix. The written arguments prove the analytic and unrestricted assertions. No comparison with an unidentified inherited program is asserted. Timing and hashes are bound in the companion input receipt.

## Bound inputs

[
  {
    "path": "agents/ii_checks_provenance/recovery_20261121T2000Z/S6_SERIES_PUBLISH_II_boundary_construction_inputs.json",
    "sha256": "c92879fad86dfe710f2771af118d359bdfc51603c2219826a4e80e0f8d4bf7f6"
  },
  {
    "path": "agents/ii_checks_provenance/recovery_20261121T2000Z/clean_derivations/S6_SERIES_PUBLISH_II_boundary_preproof_exact.py",
    "sha256": "7861945b4c8f8835bde08e625a4a90584eb7b97b4a8cf2dabc14c9a571af50ab"
  },
  {
    "path": "agents/ii_checks_provenance/recovery_20261121T2000Z/clean_derivations/S6_SERIES_PUBLISH_II_boundary_preproof_exact.output.json",
    "sha256": "304faf772523cb4bd9c36267c075eabf1447fbb1ec63ec9f6852309f9d84d954"
  },
  {
    "path": "agents/ii_checks_provenance/recovery_20261121T2000Z/primary_inputs/Cartan1952_exp18.pdf",
    "sha256": "750b33ff7f82bc35358693a73793a92ceb7159fddd72a615b8cffc731f7958d1"
  },
  {
    "path": "agents/ii_checks_provenance/recovery_20261121T2000Z/primary_inputs/Cartan1952_exp18_printed_7.png",
    "sha256": "21581388abb63a5397404ad279016d93e9e53ff7826a42429801157d5e0bd766"
  }
]
