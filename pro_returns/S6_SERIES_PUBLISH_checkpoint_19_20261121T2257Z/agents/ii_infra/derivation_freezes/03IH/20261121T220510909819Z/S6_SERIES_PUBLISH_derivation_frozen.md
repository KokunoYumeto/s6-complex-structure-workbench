# Prereading derivation: wbII:prop:analytic-ah-boundary (03IH)

Take an open pants neighbourhood and its simply connected base cover U. In the period construction the additive fibre cover is U times C^2. It is Stein and contractible, so Cartan B and the exponential sequence trivialize the pullback of L holomorphically. The actual deck group is Lambda semidirect pi_1(P), with the zero-section splitting prescribed in the target. In a chosen frame let j_g be its nonvanishing holomorphic transition factors. Holomorphic logarithms exist on this simply connected additive cover.

The numbers

    c(g,h)=(log j_g(hx)+log j_h(x)-log j_{gh}(x))/(2 pi i)

are constant integers and satisfy the two-cocycle identity by associativity of the factors. On the lattice the alternating part is the fibre Chern form E, by the argument principle on a fundamental square. Transport of the restricted bundle proves invariance of E. The real two-cocycle

    c_E((lambda,g),(mu,h))=1/2 E(lambda,A_g mu)

is an explicit reference extension: invariance of E proves its cocycle identity, and its lattice alternating part is E. Integration of the constant vertical form over the affine triangle with sides lambda and A_g mu is exactly this half-E expression. Thus this reference records the flat vertical class, with zero mixed contribution in the zero-section marking.

Subtract c_E. The resulting real central extension restricts to an extension of Lambda with zero commutators. Choose lifts of its four basis vectors and define the lift of any lattice vector by their commuting integer powers; this is a splitting of that restricted extension. Choose lifts of the two free base generators and extend along reduced words; freeness gives a splitting over pi_1(P). In the resulting extension write

    ghat lambdahat ghat^{-1}=i(k_g(lambda)) (A_g lambda)hat.

The function k_g is additive. Conjugating twice gives k_{gh}(lambda)=k_h(lambda)+k_g(A_h lambda). Define d(g)(nu)=k_g(A_g^{-1}nu). It follows by substitution that d(gh)=d(g)+T_g d(h). Replacing the lattice splitting by its translate a(lambda) changes k_g(lambda) by a(lambda)-a(A_g lambda), hence d(g) by (T_g-I)a. Changes of frame or logarithms give an isomorphic central extension and the same class. This proves uniqueness of the class associated to this line bundle and this fixed flat reference; it does not claim that every arbitrary crossed homomorphism on the free group lies in one cohomology class.

The chosen base lifts multiply according to rho_1 rho_2 rho_0=1 without a vertical endpoint. Thus d_1+T_1d_2+T_1T_2d_0=0 and the barred sum is zero. The mixed commutator of the logarithmic factors on the rectangle formed by nu and the base loop is the first Chern integer on that rectangle after subtracting the reference vertical contribution. With the rectangle ordered (fibre,base), the base-first convention gives <d(rho),nu>=-<c_1(L)-[Omega_E],sweep(nu,rho)>. This sign follows directly by interchanging the two oriented edge parameters of the rectangle.

For a finite filling take the full clockwise root circle s=r exp(-2 pi i theta). The exact logarithmic overlap sends the flat zero section to cap real coordinates theta v+k(theta), with k(theta)=Pi_{s,R}^{-1}(i(log r)/(2 pi) Pi_s v) periodic. The homotopy k(theta)->k(0) proves that the swept cap torus has Chern pairing E(nu,v). The logarithmic commutator just computed is its negative, so <N_Td,nu>=E(v,nu) on every lattice vector, and N_Td=i_vE. Projection gives m dbar=[i_vE]. Inverse local loop conventions give the same finite norm by the explicit finite reindexing of its terms.

At the cusp the actual map (u,q)->(q exp(-2 pi i u),1,exp(2 pi i u)) in the chart t=z_0z_1z_2 is a solid torus whose boundary is exactly the deltahat sweep. The line bundle extends over that solid torus. Its exponential transition cocycle therefore has zero boundary Chern number, or equivalently its argument-principle commutator is zero. The flat vertical reference has zero boundary pairing. Hence <d_0,deltahat>=0; evaluation identifies the real coinvariant line with its delta coefficient, so dbar_0=0. All these identities have been obtained from holomorphic factors, their logarithmic cocycle, and actual filling maps. No global Leray transgression or local integral nearby-cycle theorem enters this derivation.

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
