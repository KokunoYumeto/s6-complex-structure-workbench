# Research tree

Inventory and ledger counts last audited: 2026-09-03 05:19:12 +02:00
(Europe/Berlin).

The TeX files at this level are the publication-facing components compiled by
`workbench.tex` from the consolidated project root:

- status.tex — exact current results and evidence boundary;
- mathematical_summary.tex — concise theorem-level results and significance;
- scalar_gauss_domain_shared.tex — the entire two-cross scalar--Gauss
  domain: classified bijection `D x {+1,-1}^2 x U(1)^2`, full literal
  quotient by simultaneous `(p_plus,p_minus,zeta)` sign change, and
  an explicit family at every original `t=g^2>0`. Here
  `D={(u,v0,y):u>0,d=u*v0-2/3-y^2>0,c=4*v0-5*u>0}` and `t=72*d/c`.
  It is input once by `quaternionic_4441_reconciliation.tex`, immediately
  after `two_cross_exceptional_shared.tex`. The two spatial residuals
  cannot vanish simultaneously throughout that class, and unrestricted exceptional-set
  existence remains OPEN. Evidence is under
  `supporting_materials/workbench/evidence/scalar_gauss_domain_20260905/`.
  The earlier dated inventory below remains historical; no quantum gap
  follows from this classical residual classification;
- scalar_gauss_smooth_shared.tex — the exact smooth refinement of the
  literal domain, with four embedded six-dimensional components and
  `S_sg ≅ {+1,-1}^2 x (0,infinity) x R^2 x T^3`. The unchanged original
  coupling `t=g^2` is the positive product coordinate. Every positive
  fixed-coupling level has four embedded five-dimensional components
  `R^2 x T^3`. The complete phase and literal inverse charts are proved;
  this source is included once immediately after scalar_gauss_domain_shared.tex
  in the common quaternionic module. It introduces no spatial equation,
  physical gauge quotient or quantum spectral claim;
- validation_protocol.tex — methodology;
- literature_log.tex — relation to existing literature;
- es_niemeier_shared.tex — the index-72 modulo-840 `A5^4 D4` lattice,
  the full splitting `O(N)=W(A5^4 D4) semidirect L(GL2(F3))`, the residue
  six-cycle inside the Weyl group and centralizing the chosen complement,
  exact marked flag-weight/triality maps, and retained shell and finite-sample
  Fourier counts. The abstract quotient is credited to Cheng–Duncan–Harvey;
  the coordinate/code realization and all shell-count conventions are explicit;
- es_niemeier_bibliography.tex — the five shared `esn:` bibliography entries,
  input once inside each host bibliography, not a separate proof module;
- ES_NIEMEIER_PROVENANCE.md — exact source excerpts, labels, snapshot digests,
  and the original residual-note counting correction. This companion travels
  with the shared source package. The workbench and the ES/higher-rung roots
  each input the proof once; the generated `higher_rung_24d_continuation.tex`
  must exclude the standalone root's host-only proof and bibliography inputs;
- candidate_geometry.tex — full analytic construction and local fibres;
  the current bounded refinements prove the exact period half-plane
  `Im(c0)<-max D_part`, the cusp-free `beta+i*t` counterexample, and the
  exact opposite-edge multipliers `exp(-2*pi*i*mu0)`, `exp(12*pi*i*mu0)`,
  `exp(-2*pi*i*(7*mu0+b0))`. They retain the full holomorphic cusp matrix,
  restricted chart domains and weak closed-polydisc inequalities. These
  refinements do not add a sphere-identification or CDP theorem;
- exact_algebra.tex — complete integral certificates;
- erdos_straus_selector_crosswalk.tex — the complete first-half divisor-shell
  selector, its exact marked bijection with the normalized S6 terminal
  relation matrices, and the proof that the correspondence is an integral
  row-shear rather than a geometric map;
- integral_leray.tex — nearby cycles, transgressions, \(\pi_1\), and
  \(S^6\) recognition;
- algebraic_dimension.tex — direct proof of the meromorphic function field;
- analytic_picard.tex — direct images, Picard line, finite normal characters,
  and uniform non-torsion;
- analytic_picard_local_obstruction.tex — the verified cusp-local line bundle
  with nonzero normalized restriction to `dP6`, showing that any purely
  analytic global zero-restriction proof must also encode both finite
  fillings;
- analytic_picard_completion.tex — the completed third global restriction
  certificate from holomorphic `O*` factors, finite-filling norms, the cusp
  argument principle, and the toric support-function cross block;
- hodge_frolicher.tex — the complete Hodge, Bott–Chern, and Aeppli diamonds,
  Frölicher page, logarithmic cotangent direct images, cyclic invariant
  lattices, Kodaira–Spencer divisor, residue cancellation, scalar calculation,
  and the correction that the relative cotangent sheaf is
  torsion-free but non-locally-free at the cusp and has torsion only at the two
  multiple fibres;
- bott_chern_algebra.tex — exact marked-fibre period formulas, explicit global
  Bott–Chern generators, and the complete algebra
  \(H^{*,*}_{BC}(X)=\mathbb C\mathbf1\oplus N_{\mathrm{BC}}\), with
  \(N_{\mathrm{BC}}^2=0\); all products are determined, while a
  preferred literal global coefficient atlas through the singular fillings
  is not claimed;
- cusp_spectral_geometry.tex — the exact radial period and dual lattices,
  scalar spectrum, native \(\mathbb T^2\times\mathbb R^2\) limit, auxiliary finite-cover
  \(\mathbb R^4\) limits, the exact four-copy regular-locus \(\mathbb T^4\)
  quotient with pointed \(\mathbb R^4\) limit, its finite-filling Seifert
  normalizations and toric-cusp nonextension theorem, and the classified
  first-coordinate elliptic-quotient locus; neither literal fixed-target cover
  construction nor the unmodified four-copy quotient descends to a compact
  \(S^{12}/S^{24}\) construction;
- cusp_toric_cover_completion.tex — the corrected local Kummer completion:
  after the cyclic base change \(t=v^N\), the source factor
  \(C_N(v)=C(v^N)/N\) makes
  \((\xi_1,\xi_2,v)\mapsto(\xi_1^N,\xi_2^N,v^N)\) equivariant.  The descended
  map has degree \(N^3\) to the original cusp family; relative to the normal
  base change it has degree \(N^2\), is quasi-étale but nonflat exactly above
  the double and triple strata, and restricts on the central normalization to
  toric multiplication \([N]:\mathrm{dP}_6\to\mathrm{dP}_6\);
- PRO_MODE_R4_REQUEST_RESPONSE_CROSSWALK_2026-09-03.md — the
  source-line audit of the requested native \(\mathbb R^4\) generalization,
  the T1/T2 work, and the pre-feedback Pro response.  It records the exact
  near miss: the response found \(F_T^2\to Q_T^2\to\mathbb R^4\) but tested
  \(X\times X\not\simeq S^{12}\) instead of the based smash source
  \(X\wedge X\cong S^{12}\);
- cusp_cone_sphere_routes.tex — the exact cone-compactified answer to the
  \(S^{12}/S^{24}\) request: the native two-torus quotient gives a global based map
  \(X^{\wedge2}\cong S^{12}\to\operatorname{Susp}(T^3)^{\wedge2}\), while the
  full-base invariant circle quotient and the two finite Seifert targets give
  \(X^{\wedge4}\cong S^{24}\to\mathcal C^{\wedge4}\), with the cusp boundary
  torus coned to a vertex.  Their synchronized radial target slices converge
  intrinsically and pointed-locally to \(\mathbb R^4\); the explicit targets
  are stratified spaces, not spheres or compact four-manifolds;
- cusp_sphere_route_strengthening.tex — the optimality proof showing that two
  copies are minimal cusp-locally and four copies are minimal over the full
  regular base; the continuous surjective quotient maps
  \(\widehat q_3^{\wedge2}:S^{12}\twoheadrightarrow S^6\) and
  \(\widehat q_\gamma^{\wedge4}:S^{24}\twoheadrightarrow S^8\); the exact
  theorem that for every based \(f:S^6\to S^2\), the factor
  \(f\wedge\operatorname{id}_{S^6}=\Sigma^6f:S^{12}\to S^8\) is null because
  \(\pi_{12}(S^8)\cong\pi_4^{\mathrm S}=0\), so
  \(f^{\wedge r}\simeq *\) for every \(r\ge2\) and in particular the full
  \(\widehat q_\gamma^{\wedge4}\) quotient is based null-homotopic; the exact
  stable calculation for every based \(g:S^6\to S^3\): since
  \(\pi_6(S^3)=\mathbb Z/12\), one has
  \(\operatorname{st}([g])=2a\nu\in\pi_3^{\mathrm S}=\mathbb Z/24\), hence
  \(\operatorname{st}([g\wedge g])=4a^2\nu^2=0\) in
  \(\pi_6^{\mathrm S}=\mathbb Z/2\); the Hatcher p. 339 group table together
  with Toda Propositions 3.1 and 5.11 identifies
  \(\operatorname{st}:\pi_{12}(S^6)\xrightarrow{\cong}\pi_6^{\mathrm S}\)
  as an isomorphism, proving the full \(\widehat q_3^{\wedge2}\) quotient
  based null-homotopic as well; the
  uncomputed one-copy classes of \(\widehat q_3\) and
  \(\widehat q_\gamma\); the still-undetermined
  conical-target classes of
  \(q_2^{\wedge2}:S^{12}\to\mathcal A^{\wedge2}\) and
  \(q_1^{\wedge4}:S^{24}\to\mathcal C^{\wedge4}\), with
  \(q_{1,\mathrm{cusp}}^{\wedge4}:S^{24}\to\mathcal B^{\wedge4}\) likewise
  uncomputed; their moving embedded metric four-spheres with eventual exact
  Euclidean balls; the separate null-homotopies of those slice inclusions;
  and the Hausdorff, second-countable noncompact comparison
  five-manifolds with boundary fibre \(\mathbb R^4\), whose maps to the compact
  cone carriers are continuous, surjective, nonproper, and nonquotient;
- cusp_sphere_fixed_metric.tex — one fixed cusp-adapted metric on each compact
  codomain, the slice-rescaling trichotomy, and the sharp distinction between
  the \(\mathbb R^4\) moving-slice bubbles and the full ambient
  \(\mathbb R^8/\mathbb R^{12}\) bubbles.  In every fixed compatible metric
  the unrescaled target slices collapse to the cone vertex, and unit-volume
  normalization gives a flat four-torus rather than \(\mathbb R^4\);
- cusp_globalization_replacement.tex — the complete proof-bearing subfile for
  the four-copy quotient, its minimality, the no-finite-base-cover theorem,
  degrees \(27\) and \(64\) at the finite fillings, and the product, smash,
  almost-complex, and cusp-extension obstructions;
- cusp_spectral_interpretation.tex — unit-volume metric dependence and the
  rigorously typed auxiliary direct-integral threshold operator;
- cusp_gauge_operators.tex — continuum and finite classical gauge Hessians,
  their exact spectra, and the explicit bridge that would be required before
  any quantum mass-gap conclusion;
- cusp_compact_link_gaussian.tex — the transported cubical decomposition whose
  vertices are precisely the finite \(N_{\rm mesh}\)-torsion subgroup, the
  endpoint-correct holonomy and inverse-transport laws, a periodic compact
  \(SU(2)\) link flux with exact logarithmic and sector-Wilson actions, and a
  finite Gaussian oscillator with independent cover index \(M_{\rm cov}\) and
  mesh size \(N_{\rm mesh}\).  It proves a resolved diagonal cusp sequence and
  explicitly distinguishes the Lebesgue Gaussian Coulomb space from compact
  Haar link space and its nonlinear vertex Gauss law;
- cusp_su2_magnetic.tex — integral magnetic line bundles, exact Landau
  spectra, and the reducible \(SU(2)\) Yang--Mills critical point with its
  explicit negative mode;
- koide_period_discriminant.tex — the exact linear discriminant/Koide-cone
  correspondence and its stated separation from the proof that the completed
  threefold is \(S^6\);
- koide_counting_repair.tex — the exact Vieta-to-ternary bijection, local
  densities, archimedean factor, adelic sign balance, and unconditional
  asymptotic for reduced positive defect-one solutions; only the square-root
  discrepancy estimate remains open;
- topology_reduction.tex — verified cusp collapse and specialization comparison,
  actual finite-band and cusp Mayer–Vietoris maps, and the commuting Leray
  comparison;
- cdp_program.tex — conductor, counterexample, duality, base change, three
  independent all-Pic restriction certificates, and the CDP comparison;
- local_repairs.tex — definite local corrections;
- tool_disclosure.tex — automated-tool disclosure;
- references.tex — consolidated bibliography, with review provenance clearly
  labelled as such rather than presented as external literature.

The ledgers/ subfolder contains internal machine-readable claim, dependency,
morphism, uncertainty, literature-source, and research-history records. Those
files are deliberately not compiled and are not substitutes for mathematical
proofs or public citations.

This level contains 33 files: 31 publication-facing TeX components, this
README, and the Pro-response crosswalk.  The `ledgers/` subfolder contains
eight files.  Across the complete workbench tree there are 49 files.  The
claim ledger records 65 VERIFIED, four
OPEN, six REFUTED, and zero CONDITIONAL entries.

The clean reconstruction and annotated audit are the consolidated root files
`original_clean_transcription.tex` and `main.tex`. Comparative methodology is
under `supporting_materials/workbench/comparative_context/`; historical review evidence and source
snapshots are indexed by `supporting_materials/README.md`. None is silently
edited by the live mathematical paper.
