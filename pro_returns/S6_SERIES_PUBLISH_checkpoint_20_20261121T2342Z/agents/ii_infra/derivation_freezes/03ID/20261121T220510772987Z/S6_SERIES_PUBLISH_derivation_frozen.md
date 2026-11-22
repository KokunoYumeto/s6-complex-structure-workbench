# Prereading derivation: wbII:lem:picard-cusp-defect (03ID)

Use the actual cusp toric chart t=z_0 z_1 z_2, x_1=z_1, x_2=z_2 supplied in the input. The holomorphic map in the second variable

    H:S^1 times Delta_r -> Y_epsilon,
    H(u,q)=(q exp(-2 pi i u),1,exp(2 pi i u))

is continuous on the whole solid torus, including q=0. Its base coordinate is t=q. On its boundary q=r exp(-2 pi i v), x_1=1 and x_2=exp(2 pi i u). These are exactly the flat zero-section lift of the clockwise cusp meridian swept by deltahat: the period column of deltahat is (0,1). Composing H with the actual cusp quotient map produces the required solid torus in N_0. Tautological cusp gluing has no additional vertical translation.

Every first Chern class pairs to zero on this boundary, because it extends over the solid torus. The constant vertical form has zero pairing on its flat boundary sweep, as one direction is horizontal. The base-first defect pairing therefore gives <d_0,deltahat>=0. The supplied integral computation identifies V_G with Z[delta], and evaluation on deltahat is the displayed coefficient map. Hence dbar_0=0.

For the second assertion use the actual inclusions i_W:W->N_0 and i_F:F->N_0. The proper local cusp tube comparison identifies the specialization map with restriction from the tube: sp^2 i_W^*=i_F^* on H^2(N_0,Z). This is also the natural map from the constant sheaf to nearby cycles; its equality on these maps follows from restricting the same cochain or line-bundle transition cocycle to the central and nearby fibres. The established Paper I cusp-tube retraction supplies an inverse to i_W^*, so this describes exactly the named specialization rather than a replacement isomorphism. Apply the equality to c_1(L). Naturality of the exponential-sequence connecting homomorphism gives i_W^*c_1(L)=c_1(L|W) and i_F^*c_1(L)=c_1(L|F), proving the formula. No global H^2(X) computation is involved.

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
