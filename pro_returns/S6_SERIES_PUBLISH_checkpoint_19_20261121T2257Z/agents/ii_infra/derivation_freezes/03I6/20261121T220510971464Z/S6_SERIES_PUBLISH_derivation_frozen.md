# Prereading derivation: wbII:lem:analytic-support-specialization (03I6)

Let L=pi^*M. The following construction applies to an arbitrary analytic line bundle; it does not start by assuming L has a toric divisor or a torus action. Every full smooth-cone chart restricted to Y_epsilon is

    U_sigma={ (z_0,z_1,z_2) in C^3 : |z_0z_1z_2|<epsilon }.

It contracts by radial scaling. It is Stein directly from holomorphic convexity: for a compact K its O(U_sigma)-hull lies in the compact polynomial hull in C^3 and satisfies |z_0z_1z_2|<=max_K|z_0z_1z_2|<epsilon; hence it is compact inside U_sigma. Coordinates separate points and give local coordinates. Cartan Theorem B and the exponential sequence now give Pic(U_sigma)=0. The exact primary Theorem B statement is Cartan, Seminaire 1951-52, expose 18, printed p.18-7; its actual image confirms H^q=0 for q>=1.

Choose a holomorphic frame e_sigma on each such chart. All charts contain T=(C*)^2 times Delta*, so choose e_T as the restriction of one of these frames. Write e_T=f_sigma e_sigma on T. The three integral windings of f_sigma form n_sigma in M'=Z^3. Around a common divisor E_v, f_sigma/f_tau is the transition unit between two holomorphic nonvanishing frames and extends across that divisor. Its winding on the transverse meridian is zero. Hence

    phi(v)=<n_sigma,(v,1)>

is independent of the chart containing that ray. This is an actual integral support function derived from the analytic frames. Terms with zero winding have zero Chern class in the relevant exponential-sequence calculation; no global meromorphic representative of L has been assumed.

On E_v the same local frames and transverse meridians give the divisor-class coefficients phi(v+a_i)-phi(v) along its boundary hexagon. Its degree on the i-th curve is therefore

    d_i(v)=phi(v+a_{i-1})+phi(v+a_{i+1})-phi(v+a_i)-phi(v).

This follows by pairing with the hexagon intersection matrix, whose diagonal is -1 and adjacent entries are 1. Deck equivariance of the pullback L identifies E_v with E_{v+B_0 lambda}, preserving the labeled boundary directions. Since B_0 is unimodular, d_i(v) is constant in v. The common curve between adjacent components has the same line-bundle degree from either component, giving d_i=d_{i+3}. Denote the first three integers by d_1,d_2,d_3 and define

    Bform=[[d_2+d_3,d_3],[d_3,d_1+d_3]].

This is an integral symmetric form. The integer-valued polynomial

    Q_B(v)=B11*v1(v1-1)/2+B12*v1*v2+B22*v2(v2-1)/2

has exactly these six degrees. For psi=phi-Q_B all six degree equations vanish. The third gives Delta_1 Delta_2 psi=0; combining the second and first respectively with it gives Delta_1^2 psi=0 and Delta_2^2 psi=0. Applying these difference equations successively on the integral grid gives psi(v)=c+ell_1 v_1+ell_2 v_2 with integral constants. Thus phi(v+B_0 lambda)-phi(v) is affine in v with linear part Bform(B_0 lambda,v). The binomial polynomial treats odd diagonal coefficients integrally; no division by two of an arbitrary integer quadratic coefficient has been made.

It remains to identify the actual fibre Chern form. Write the deck action on e_T as e_T(p)->j_lambda(p)e_T(Psi_lambda p). If Psi_lambda maps U_sigma to U_tau, its action on the chosen local frames is a holomorphic unit b_{lambda,sigma} on the contractible chart. Its winding is zero. The exact frame equation gives

    j_lambda=b_{lambda,sigma} f_sigma/(f_tau o Psi_lambda).

Consequently the winding of j_lambda along a torus loop m is the negative linear part of the support-function difference, namely -Bform(B_0 lambda,m). Pulling e_T to the additive cover of F_t makes all integral m-translation factors equal to 1. The logarithmic commutator on the fundamental square for (lambda,m) is then exactly that winding. The exponential-sequence/argument-principle definition of c_1 therefore gives

    E_M((lambda,0),(0,m))=-Bform(B_0 lambda,m).

This proves the displayed map between the degree data and the actual Appell--Humbert form. For E_M=0, unimodularity of B_0 gives Bform=0, hence d_1=d_2=d_3=0. The toric boundary curves generate the curve lattice of E_0=dP6, and their intersection pairing detects every Chern class. Thus c_1(L|E_0)=0; H^1(E_0,O)=0 and the exponential sequence give L|E_0=O_E0. The identity L|E_0=nu^*(M|W) is restriction of the given maps. No integral nearby-cycle specialization is used.

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
