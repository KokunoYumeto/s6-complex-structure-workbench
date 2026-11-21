# Prereading derivation: wbII:prop:direct-boundary-picard (03IL)

The invariant-lattice input gives E=nq, n in Z, with exactly q=u wedge w+6 gamma wedge delta. There is no rescaling from q to 2q here. For v_1=(1,2,-4,0) and v_2=(-1,-3,3,0), direct contraction gives

    i_v1 q=4u+2w+6delta,
    i_v2 q=-3u-3w-6delta.

The supplied coinvariant map kills gamma,u,w and carries delta to its primitive generator. The actual finite norm identities with m_1=3 and m_2=4 consequently give

    dbar_1=2n[delta],    dbar_2=-(3n/2)[delta].

The cusp solid-torus calculation gives dbar_0=0. The based boundary relation gives their sum zero, hence (n/2)[delta]=0 in the real coinvariant line. Therefore n=0. This reasoning uses the actual finite covers and their logarithmic overlaps; it does not assume an unproved parity convention for an auxiliary finite-filling basis.

For the line bundle restricted to N_0, the local Chern compatibility gives sp^2(c_1(L|W))=c_1(L|F)=0. The supplied integral local specialization theorem is injective in degree two, so c_1(L|W)=0 integrally. Pull back along the exact normalization eta:dP6->W to obtain c_1(eta^*i^*L)=0. On dP6, H^1(O)=0 (the proved toric cohomology/GAGA input), and the exponential sequence makes Pic(dP6)->H^2(dP6,Z) injective. Thus eta^*i^*L is the trivial holomorphic line bundle. Both conclusions hold for the given arbitrary analytic L on X. Global Leray transgressions and the packaged H^2(X,Z)=0 statement were not used.

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
