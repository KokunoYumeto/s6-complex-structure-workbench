# Prereading derivation: wbII:prop:local-cusp-picard-obstruction (03IN)

Set B=B_0, H=diag(1,-6), Q(v)=v^tHv. The toric fan is smooth with rays (v,1), v in Z^2. On each full cone the primitive ray generators form a Z-basis, so the three integer Q-values are the values of one integral character. This constructs the local Cartier equation for the prescribed divisor. The fan is locally finite, so each chart meets finitely many relevant divisors; the Cartier equations agree on overlaps up to a unit. This proves local finiteness and the Cartier assertion for D_Q.

The actual action Psi_lambda sends E_v to E_{v+B lambda}. Consequently

    Psi_lambda^*D_Q-D_Q=div(f_lambda),
    f_lambda=x^{2HB lambda} t^{Q(B lambda)}.

This is the exact character-divisor identity, because Q(v+B lambda)-Q(v)=2(HB lambda) dot v+Q(B lambda). Write

    C=[[6mu,h],[b-h,mu]],
    S=C^t HB=[[6(b-h),6mu],[6mu,h]].

The matrix S is symmetric. Define b_lambda=exp(2 pi i lambda^t S lambda), g_lambda=b_lambda f_lambda. Substituting the actual Psi action x -> exp(2 pi i C lambda)t^{B lambda}x gives

    f_lambda (f_mu o Psi_lambda)
       = f_{lambda+mu} exp(4 pi i lambda^t S mu).

Since b_{lambda+mu}/(b_lambda b_mu) is that same exponential, g_lambda(g_mu o Psi_lambda)=g_{lambda+mu}. Multiplication by g_lambda is the isomorphism Psi_lambda^*O(D_Q)->O(D_Q): its divisor is precisely the source divisor minus the target divisor. Thus the action on the actual bundle fibre from p to Psi_lambda(p) is multiplication by g_lambda(p)^{-1}. This inverse is necessary for the Chern-class sign. The equivariance cocycle and the given free properly discontinuous quotient descend the line bundle to N_0.

The coefficient of E_0 is Q(0)=0. Only the six adjacent E_ai meet E_0 as boundary curves. Restriction therefore gives O_E0(sum Q(ai) C_i). The values in the stated ray order are (1,-6,-5,1,-6,-5). The dP6 hexagon has C_i^2=-1 and C_i.C_{i+/-1}=1, all other distinct intersections zero. Its degrees are consequently (-12,2,0,-12,2,0), in particular nonzero.

On a nonzero fibre use additive coordinates x=exp(2 pi i zeta), t=exp(2 pi i s), and the ordered lattice [Z|I_2], Z=sB+C. The actual action factors are

    j_lambda(zeta)=exp[-2 pi i(2 zeta^t HB lambda+s Q(B lambda)+lambda^t S lambda)],
    j_m=1 for m in Z^2.

The logarithmic commutator for (lambda,m) is

    (log j_lambda(zeta+m)-log j_lambda(zeta))/(2 pi i)
       =-2 m^t HB lambda.

This is the first Chern alternating form obtained from the transition factors and the oriented fundamental square. The lambda-lambda part vanishes because Z^t HB=s B^t HB+S is symmetric; the m-m part is zero. In the basis (gammahat,uhat,what,deltahat), m^t HB lambda=lambda_2 m_1+6lambda_1 m_2=q(lambda,m). Thus the full alternating form is exactly -2q, with no unproved coordinate interchange or orientation replacement.

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
