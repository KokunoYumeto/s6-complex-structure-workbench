# Prereading derivation: wbII:thm:analytic-all-picard (03IW)

Take an arbitrary holomorphic line bundle L on the given standard X. Its fibre Chern form E is invariant, so the exact integral invariant lattice gives E=nq with n in Z and q=u wedge w+6gamma wedge delta. The holomorphic-factor boundary construction gives a crossed class with barred boundary sum zero, finite norm identities, and zero cusp defect. Contracting with the actual v_1 and v_2 gives 6n[delta] and -6n[delta] in coinvariants. Division by the actual covering orders 3 and 4 yields dbar_1=2n[delta] and dbar_2=-(3n/2)[delta]. Therefore (n/2)[delta]=0 and n=0. This uses the explicit norm transports and does not replace q by a differently normalized generator.

Restrict the same L to the actual cusp neighbourhood N_0, obtaining M. The previous conclusion is E_M=0. The analytic support-function construction from holomorphic chart frames gives the integral symmetric form B with mixed pairing E_M((lambda,0),(0,m))=-B(B_0lambda,m). Since B_0 is unimodular this forces B=0, hence all three independent central degrees vanish. The boundary curves detect the integral first Chern class on dP6, and Pic^0(dP6)=0, so nu^*(M|W) is holomorphically trivial.

The map nu here is precisely the normalization eta followed by the inclusion of W in the cusp neighbourhood, while M is L restricted along the cusp-neighbourhood inclusion. Composition of these actual restriction maps is eta^*i^*. Thus r(L)=O_dP6 for every L, proving r is the zero homomorphism. The calculation uses only the holomorphic factors, finite logarithmic overlaps, explicit cusp solid torus, and analytic chart-frame support function. It does not use global integral Leray transgressions or local integral nearby-cycle specialization.

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
