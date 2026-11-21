# Prereading derivation: wbII:lem:picard-crossed-defect (03IC)

The flat torus bundle over the pants core P has its zero section. Its section lifts respect composition. With the stated whiskers the relation rho_1 rho_2 rho_0=1 therefore lifts to the stated relation with no vertical factor. The tautological cusp gluing has mu=0 and hence its image ell_0=gamma(mu)=0. Only this forward implication is needed; injectivity of an unspecified map gamma is not being assumed from the parenthetical word “equivalently.”

Let E be the restriction of c_1(L) to a marked fibre. Parallel transport of the restricted line bundle identifies its Chern class, proving A_g^*E=E. Consequently the constant vertical alternating two-form E in flat real coordinates descends to a globally defined closed form Omega_E. It has the same fibrewise cohomology class as c_1(L).

Retract P to its two-loop graph. The cellular filtration of the torus bundle over that graph gives in total degree two

    0 -> H^1(P,V_R) -> H^2(J_P,R) -> H^0(P,wedge^2 V_R) -> 0.

Here the left map is the base-first cup map. This exact sequence can be obtained directly by gluing the two cylinder bundles to one fibre: the only base cochain groups are C^0=V_R and C^1=V_R plus V_R, with differential a -> ((T_rho1-I)a,(T_rho2-I)a). There is no base cell in degree two or higher and hence no missing higher-base differential. The global vertical form proves surjectivity onto its invariant class as well. The difference kappa=c_1(L)-[Omega_E] restricts to zero and therefore has a unique class in H^1(P,V_R).

Choose its two values on free generators, and extend along words by z(gh)=z(g)+T_g z(h); the inverse rule z(g^{-1})=-T_g^{-1}z(g) makes cancellations exact. The cellular coboundary changes z(g) by (T_g-I)a. Applying z to rho_1 rho_2 rho_0=1 gives d_1+T_1d_2+T_1T_2d_0=0; applying V_R -> (V_G)_R gives the barred sum zero. A principal change dies in coinvariants. Since deltahat is fixed by A_0, <(T_0-I)a,deltahat>=<a,A_0^{-1}deltahat-deltahat>=0. This proves representative independence of the indicated number.

Finally restrict to the mapping torus of any rho and a fixed fibre cycle nu. A representative of the base-first edge class is dtheta wedge alpha in a cut cylinder; its integral on the product oriented as (nu,rho) is -alpha(nu). The endpoint correction in the cut cylinder is exactly the crossed-cocycle coboundary already described, so it vanishes on the fixed cycle. Thus <z(rho),nu>=-<kappa,a_*([S^1_nu] times [rhoutil])>. This proves the asserted sign and actual map, without identifying a fibre-first cup map with the base-first one.

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
