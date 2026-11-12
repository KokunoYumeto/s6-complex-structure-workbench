# S6 annotated mathematical proof audit

Canonical Overleaf project: <https://www.overleaf.com/project/6a8ca9bd0c2a1270c91e5ce1>  
Current public read link: <https://www.overleaf.com/read/rtmyqxyrzprn#fa24eb>

This is one consolidated project containing the reconstructed manuscript, its
annotation and review record, and the integrated validate/repair/disprove
workbench.

## Current addition — 8 September 2026

The live reading workspace now also contains
`s6_magnetic_translation_quantum_draft.tex`: the complete current magnetic
background-to-vacuum calculation, the full-box plaquette continuation,
and the full local-energy-current calculation in one editable paper.
The new current part retains every face and gives the vacuum second
coefficient, first-contribution cancellation, exact two-face channels,
and affine volume count. Its source Markdown, exact checking programs and
current supporting mathematical notes are mirrored under
`supporting_materials/workbench/evidence/ym_magnetic_translation_20260908/`.
This is a live source snapshot, not a publication or audit-release checkpoint.
The source mirror does not wait for PDF generation; all existing PDFs remain
available and unchanged. The current source bundle includes this new root.
The same draft now also contains the complete actual-vacuum electric
covariance and unsigned-incidence-kernel calculation, through its
all-real-weights minimum section. The local-current part includes the
exact all-coupling affine spectral-measure identity. These are complete
live source additions within the existing root, not additional projects.
Parts 5 and 6 now contain the complete actual first physical excitation-band
calculation and full open-box face-graph derivation, including the bulk
symbol and the limit of the first-band Taylor coefficient. The full
current sources and available independent calculations/checking inputs
are mirrored alongside them. The coefficient limit is not presented as
an interchange of volume and coupling limits.
Part 7 contains the complete native center-disorder bridge, relating the
continuous magnetic translation to center cochains, Wilson loops and
actual-vacuum spectral moments. Its current source, checker and result
snapshot are included with the existing magnetic draft.
Parts 8 and 9 add the complete native magnetic open-face spectral measure
and physical-band transport calculations. Their original scale dictionary,
finite-volume amplitudes, coefficients and spectral weights remain in full.
Part 10 adds the complete separated-link electric covariance, graph map,
fourth spectral functional and physical-time correlation, retaining the
corrected `kappa t` Duhamel factor and all original physical coefficients.
Part 11 adds the full native magnetic leakage volume polynomial and exact
ratio, also propagated into the existing physical-band transport formulas.

Three additional live topic papers are available as editable roots:
`s6_volume_uniform_local_vacuum_draft.tex`,
`s6_extensive_quantum_blocking_draft.tex`, and
`s6_spatial_continuum_draft.tex`. Their complete supplied sources and
checking inputs are mirrored under
`supporting_materials/workbench/evidence/ym_sidebar_topics_20260908/`.
The supplied volume-estimate, blocking and spatial-continuum PDFs are
included unchanged; this mirror does not claim a new build or rendering
review. Incoming authored mathematical files from all three topic
directories are discovered beyond the original file list and mirrored
into their existing reading roots. The current volume-estimate paper
includes its all-coupling Section 10 and Sections 11--12 on the full
creation-cluster construction and stated uniform strong-coupling
gap/denominator bounds, with its supplied 17-page PDF.
All earlier papers remain available.

For the original retained period matrix, `D = Lq + 6m^2` and
`Q = [[A, M I], [B, 0]]` give the complete inverse metric and the exact
nonlinear curvature pullback with every commutator and coupling retained.
On a finite four-dimensional `SU(2)` Wilson regulator, integrating one
interior link with all six incident plaquettes gives exactly
`2 B_e - log Z(r_e)`, where `H_e = sum_(p contains e) b_p V_ep`,
`r_e^2 = tr(H_e H_e*)/2`, `B_e = sum_(p contains e) b_p`, and
`Z(r) = I_1(2r)/r`, with `Z(0) = 1`. The retained-cusp draft also
constructs the smooth-connection realization of every finite link field
and an extensive exact integration on the specified four-dimensional patch.

For the finite interacting `SU(n)` Hamiltonian
`H = -sum_e kappa_e Delta_e^T + sum_p b_p(n - Re tr U_p)`, the positive
ground state defines the actual measure `dmu = psi_0^2 dlambda`.
The gauge-invariant Wilson-loop trial vector
`psi_0(W_C - mu(W_C))` has the exact quotient
`Q_C = (K_C/(2n)) (n^2 - r_C)/(r_C - |m_C|^2)` for every simple edge
loop, where `K_C = sum_(e in C) kappa_e`, `m_C = mu(W_C)`, and
`r_C = mu(|W_C|^2)`. Repeated edges, loop cross terms, center-selection
rules, the closed ground-state form, and explicit finite-regulator bounds
are proved with the full interacting potential retained in `mu`.

The `SU(2)` temporal Wilson transfer has exact character multipliers
`I_(2j+1)(2b_t)/I_1(2b_t)`. With the original Lie metric
`c(X,Y) = -tr(XY)/2`, `b_t = a/(2 g_YM^2 epsilon)` and
`b_s = epsilon/(2 g_YM^2 a)`, its scalar-adjusted powers converge strongly
on the invariant Hilbert space to `exp(-t H)`, where
`H = -(g_YM^2/(2a)) sum_e Delta_e^c
+ (1/(2 g_YM^2 a)) sum_p(2 - Re tr U_p)`.
The scalar transfer factor and its energy shift, gauge projection,
operator cores, and strong resolvent limit are all explicit. The spatial
lattice, its spacing, and the positive coupling stay fixed in this limit.

Eliminating a chosen spatial link set in that actual vacuum gives the
conditional isometry `J`, its orthogonal projection, and the exact
compressed resolvent
`J*(L+z)^(-1)J = (A+z-B*(C+z)^(-1)B)^(-1)`.
The closed forms, conditional-score coupling `B`, temporal memory,
and corrected excitation vectors are derived in the spatial-elimination
draft. On the specified seven-link, two-adjacent-plaquette `SU(2)` complex,
the actual-vacuum excitation trial quotients are exactly
`R_ret = 3 kappa + (5/9) b^2/kappa + O(b^3/kappa^2)` and
`R_corr = 3 kappa + (43424/81675) b^2/kappa + O(b^3/kappa^2)`.
These are trial quotients, not eigenvalue identities. Both increase from
`3 kappa` at second order, although the corrected trial is lower at the
same positive `b`. The original scalar is retained:
`E_xi = 4b - (2/3) b^2/kappa + O(b^3/kappa^2)` for the vacuum,
so the unsubtracted trial energies are respectively
`3 kappa + 4b - (1/9) b^2/kappa + O(b^3/kappa^2)` and
`3 kappa + 4b - (11026/81675) b^2/kappa + O(b^3/kappa^2)`.

The complete appended proof extends the eliminated-coupling norm squared
`b^2/12 + O_L(b^3/kappa)` and the difference
`R_ret - R_corr = (1951/81675) b^2/kappa + O_L(b^3/kappa^2)`
to every fixed open three-dimensional box `[-L,L]^3`, `L >= 2`, with
all `N = 3(2L)(2L+1)^2` links and all `M = 3(2L)^2(2L+1)` plaquettes
retained in the original Hamiltonian and its actual vacuum. It proves
the complete incidence cancellation, opposite-Pauli-basis dictionary,
moving conditional form domains and resolvent expansion. The explicit
ground-state projection disk is `|b/kappa| < 3/(16M)`; the strict
improvement holds for sufficiently small positive `b/kappa` for each
fixed box. The remainders and further bounds may depend on `L`.
The absolute coefficients `5/9` and `43424/81675` above are proved for
the two-face system only, not asserted for the full box.

The complete proofs are the additive root drafts
`s6_retained_cusp_nonlinear_draft.tex` (9-page PDF),
`s6_interacting_wilson_variation_draft.tex` (12-page PDF), and
`s6_wilson_temporal_transfer_draft.tex` (10-page PDF).
The further audited proofs `s6_spatial_vacuum_elimination_draft.tex`
and `s6_adjacent_plaquette_quantum_draft.tex` are included as editable
source-only drafts in this batch; no corresponding reading PDF is claimed.
Exact checking programs, current full-source Markdown, completed independent
audits, replay receipts, the byte-verified 13-source Pro packet, and PDF
verification evidence are in
`supporting_materials/workbench/evidence/ym_interacting_20260908/`.
The three standalone PDFs were built and visually checked separately;
this addition does not rebuild or replace the cumulative workbench PDF.
These results establish finite interacting quantum and exact nonlinear
maps. A spatial continuum theory and a volume-uniform or vanishing
four-dimensional quantum Yang-Mills gap are not established by these drafts.

## Previous addition — 6 September 2026

For the original modulo-840 Niemeier lattice `N` and its specified Leech
neighbour `Lambda`, set `tau(q)=Re((q1 q2) q3)` on `O^3` and
`F=tau∘L` on the original Niemeier span. This retained cubic has exact
additive value-generated groups in the explicitly fixed Cayley–Dickson frame.
The Albert determinant is `lambda^3 - lambda (y,y) + 2 F(y)`:

- `V_F(N) = (1/27)Z + (sqrt(2)/54)Z + (sqrt(3)/18)Z`.
- `V_F(Lambda) = (1/27)Z + (sqrt(2)/216)Z + (sqrt(3)/54)Z`.
- `V_F(J) = V_F(M) = (1/27)Z + (sqrt(2)/216)Z + (sqrt(3)/18)Z`.
- The successive inclusions from `V_F(N)` through this common group to
  `V_F(Lambda)` have quotients `Z/4` and `Z/3`, respectively; complete
  original-coordinate generators and Bezout certificates are supplied.
- Their inclusion has quotient `Z/12`; it is not a lattice inclusion
  `N ⊂ Lambda` and is not asserted independently of the specified frame.

The three neighbours cycled by the original residue operator `rho(361)`
have the same pairwise intersection `J`, with determinant `81` and index
`9` in each neighbour. The fixed fourth isotropic plane gives the
`A2^12` Niemeier lattice with exactly `72` roots and the same intersection
`J`, also of index `9`.

[Robert A. Wilson's octonionic Leech construction](https://webspace.maths.qmul.ac.uk/r.a.wilson/pubs_files/octoLeech1rev.pdf)
is embedded by the specified isometry `x ↦ x/sqrt(2)`, retaining the
original triality metric. The fixed Gram matrix is `3 G_E8`, the
orthogonal complement is explicitly isometric to `A2 ⊗ E8`, and the
quotient by their sum is `F3^8`, of order `3^8`. The cycle directions
are retained as `c(q1,q2,q3)=(q3,q1,q2)` and `c_W=c^(-1)`.
Its literal intersections with both `L(N)` and `L(Lambda)` equal
`{sqrt(2)(a,a,a): a in D_H}`, where `D_H` is `D4` in the first four
fixed Cayley coordinates. This rank-four lattice has Gram matrix
`6 G_D4`, determinant `5184`, minimum squared norm `12`, and
value-generated subgroup `4 sqrt(2) Z` for `tau` (`8 sqrt(2) Z` for `2tau`).
The actual image is smaller: `12 sqrt(2)` is not attained by `tau` on
this intersection.

The complete new proofs are the shared sources
`es_niemeier_cubic_arithmetic.tex`,
`es_niemeier_residue_fixed_neighbor.tex`, and
`es_niemeier_JM_cubic_extension.tex`, together with
`es_niemeier_wilson_cyclic.tex` under
`supporting_materials/workbench/research/`. Each is included once through
`es_niemeier_shared.tex` in the higher-rung draft, ES bridge draft and
cumulative workbench; Wilson's human-authored source is cited in their
common bibliography. Exact checking programs and outputs are under
`supporting_materials/workbench/evidence/lattice_foundation_20260906/`.
The earlier original-metric neighbour, rootlessness, triality tensor,
spectral graph, flag-cell collapse and retained cusp-bundle proofs remain
in the same source closure.

The additional exact certificates are in
`supporting_materials/workbench/evidence/period_lattice_continuation_20260906/`.
They include the full cubic-group harness, both finite-filling product maps,
and the retained-period deformation matrix identities, with execution logs
and hashes. The analytic arguments themselves are proved in the TeX, not
inferred from those finite calculations.

For the original analytic fibration, the workbench additionally proves
`omega_X = O_X(-2 S2)` and the anticanonical ring `C[U,V]`, with degrees
`1,2`; the complete system `|-2K_X|` recovers the specified fibration.
The proof in `analytic_canonical_ring.tex` uses the actual six cusp charts
and finite fillings, not a sphere-topology identification. It adds no
sphere-topology or interacting quantum mass-gap conclusion. The historical
`main.tex` and `original_clean_transcription.tex` remain unchanged.

The current workbench also includes `finite_filling_certificates.tex`:
product covers of the two original reduced central surfaces of degrees
9 and 8, the complete normalization of their actual ramified base changes,
and the full peripheral inclusion kernels. Its normal-line calculation
retains exact holomorphic orders 3 and 4 while explicitly trivializing
the underlying smooth line bundles.

In `period_parameter_deformation.tex`, varying the original constant
`beta = beta_part + c` gives a parameter-holomorphic family. The marked
real-linear fibre comparison yields the exact Beltrami matrix and its
nonzero infinitesimal class; the connecting Kodaira–Spencer convention has
the explicitly recorded opposite sign. The intrinsic anticanonical pencil
and its three fixed critical values give the proof for the whole analytic
threefold. This result does not assume the claimed smooth S6 identification.

## Additive release presentation

Zenodo releases front readable papers stating key advances. Existing papers
remain available as provenance. A separate complete project archive supplies
the full proof-bearing sources, calculations, evidence and supporting files;
its manifest distinguishes the mathematical record from any omitted build
cache, credential or private session material. The full archive is not a
substitute for a reader-facing PDF or an assertion that every exploratory
claim has been validated.

The expanded `s6_koide_es_divisor_extension_audit.pdf` now includes the
fifteen-state `p=1201` selector census, its exact map to the three-dimensional
real Jordan corner, and counts at other primes in the same residue class.
`S6_CURRENT_FULL_TEX_FOR_AI.md` includes these updated sources together with
the existing canonical TeX/Bib closure.

## Start here

1. `main.tex` — the project-compilable 129-page annotated edition and the
   Overleaf main document. Physical page 1 gives Reviewer B's revised
   complete-source determination, page 2 gives Reviewer A's corrective audit,
   and pages 3–9 are the subsequent validate/repair/disprove results and exact
   sign, Hodge, Bott--Chern, affine-defect, toric-restriction, native-cusp,
   sphere-carrier, and spectral-scope certificates; pages 10–117 are the
   108-page reconstruction; and pages 118–129 are the
   preserved indexed review appendix.
2. `original_clean_transcription.tex` — the self-contained 108-page clean
   LaTeX reconstruction without the annotation layer.
3. `workbench.tex` — the live validate/repair/disprove paper obtained by
   integrating the former 56-page workbench, the nonduplicate mathematics of
   the 18-page repair branch, and the subsequent Reviewer B/Codex validation
   work. Its supporting proofs, exact certificates, typed ledgers, literature
   log, and status map are under `supporting_materials/workbench/research/`.
   Compiled page counts and visual checks are checkpoint-specific. The latest
   5 September retained-angle build has 637 workbench pages. The current
   higher-rung draft has 50 pages and the cone/sphere draft has 64 pages.
   The final build and visual-check receipts are in
   `supporting_materials/workbench/evidence/retained_angle_20260905/`.
4. `workbench_and_manuscript_overview.tex` — a standalone concise
   mathematical account of the candidate construction, the initial audit
   objections, the replacement nearby-cycle/Leray proof, the resulting
   topology and algebraic dimension, the exact Hodge/Frölicher and
   Bott--Chern/Aeppli calculations, the explicit Bott--Chern generators and
   square-zero positive-degree ideal,
   the independent collapse/Mayer--Vietoris certificate, and the CDP20
   consequence, including the exact CDP connecting-map defect and the
   distinction between its local counterexample and the completed
   candidate-level counterexample.  It also gives the equation-first map of
   the later cusp/Kummer and sphere-carrier results, finite gauge systems,
   rank-two and rank-three SU(3) Gram/Lorentz carriers, the exact
   Erdős--Straus--Koide incidence calculation, and the worldline reduction and
   its dynamical limitations. The cumulative source also includes the
   divisor-channel count, rational-map update, and quaternionic continuation;
   the 5 September overview build has 27 pages; its first pages include the
   actual derivative-framing calculations, the zero angle-forgetting class,
   and the nonzero retained-angle and Hopf--cusp classes.

These four principal entry points compile with pdfLaTeX from this project.
Select the
document you want as the main file; restore `main.tex` when returning to the
annotated edition. The annotated document imports its editable results and
annotation sources from `supporting_materials/audit_annotation_sources/`.

For citation and deposit,
`supporting_materials/reference_pdfs/s6_peer_verification_monograph.pdf`
places a publication title and attribution page before the concise overview
and the complete workbench.  The 4 September 2026 QA candidate has 471 pages,
4,156,135 bytes, and SHA-256
`bc4c4ca950532e5b747446d97bc0edd7d6f53e1cc2fdfd8c1ce037c9879c2dbf`;
fresh visual inspection and installation of that candidate in the reference
path are still pending at this checkpoint.  The installed snapshot and the
other reference-PDF records are described exactly in
`supporting_materials/reference_pdfs/README.md`. Its editable wrapper is
`supporting_materials/publication/s6_peer_verification_monograph.tex`; it is a
publication artifact, not a fifth competing root entry point.

## Shareable companion drafts

Twenty narrower root files expose coherent subsets of the workbench without
requiring a reader to traverse the full verification paper:

1. `s6_spectral_degeneration_preprint.tex` — exact cusp spectra,
   fixed-energy counting, magnetic line bundles, and gap-closing results;
2. `s6_cone_sphere_routes_preprint.tex` — the native
   \(\mathbb T^2\times\mathbb R^2\) quotient and the exact
   \(S^{12}/S^{24}\) sphere-carrier routes, including their literal
   nonclosed \(\mathbb R^4\) open cells and exact Euclidean boundary
   decompactifications, and the based null-homotopy theorems for both full
   sphere carriers \(\widehat q_3^{\wedge2}:S^{12}\twoheadrightarrow S^6\)
   and \(\widehat q_\gamma^{\wedge4}:S^{24}\twoheadrightarrow S^8\);
3. `s6_compact_link_gaussian_preprint.tex` — compact-link holonomy,
   finite Gaussian quantization, and the boundary separating that theorem
   from nonlinear Haar-space Yang--Mills;
4. `koide_arithmetic_preprint.tex` — the Koide discriminant and
   defect-one arithmetic counting results;
5. `s6_erdos_straus_koide_bridge_preprint.tex` — the exact marked
   Erdős--Straus--\(S^6\) selector correspondence, followed by the shared
   modulo-840 lattice, full Weyl quotient, marked triality and exact shell
   maps (the filename is retained for continuity; these proofs do not
   contain a Koide morphism);
6. `s6_higher_rung_su3_gram_cone_preprint.tex` — the rank-two baseline for
   the \(\mathrm{SU}(3)\) Gram cone of two complex triplets, its compact
   representation quotient, and its gauge-theoretic boundary;
7. `s6_worldline_presymplectic_reduction_preprint.tex` — the exact
   massive and stratified massless reductions of the \(SU(3)\)-Gram
   worldline action, its zero-momentum counterexample, and the separate
   hard-constraint threshold dynamics.
8. `s6_koide_es_divisor_extension_audit.tex` — the audit of the Pro v3
   divisor channels and density-one argument, followed by a different rational
   map to the defect-one Koide surface with its inverse and exact denominator
   formula, extended on 5 September with the full fifteen-selector Jordan
   test and exact same-residue countercounts. The original orthogonal map is
   retained. The source
   packet, independent checks, and feedback are under
   `supporting_materials/workbench/evidence/koide_es_v3_audit_20260904/`.
9. `s6_quaternionic_4441_reconciliation.tex` — the cumulative proof supplement
   identifying the two Lorentz thirteen-slices as the same embedded space,
   deriving every positive fibre and the sphere pair, and retaining the
   nonunitary Jordan metric. It computes the actual omitted-coordinate force
   in the supplied scalar model and the different constrained equations;
   group-action and gauge-sign corrections are explicit. For the literal
   rotating scalar orbit, every unrestricted fixed spatial pair has at most
   fourteen positive couplings and twenty-eight tuples counting both
   frequency signs. The full residual polynomial has degree exactly
   twenty-eight whenever its retained Q7 denominator is not identically
   zero. A fixed 24-by-24 Sylvester polynomial places the entire spatial
   projection inside a proper nowhere-dense, measure-zero real algebraic
   set; existence within that exceptional set remains open. Original packets,
   independent checks, and feedback are under
   `supporting_materials/workbench/evidence/quaternionic_4441_audit_20260904/`.

10. `s6_homogeneous_quantum_confinement.tex` — the full 38-coordinate
    homogeneous SU(3) gauge--scalar Hamiltonian, exact Gauss domains,
    compact resolvent, unique physical ground state and positive
    finite-model excitation gap. It retains all interactions and constants,
    gives the classical torus-field embedding and the explicit Fourier
    coupling obstructing a fixed-vacuum quantum-subsector map. This is
    not a continuum or volume-uniform Yang--Mills gap. Complete proof
    module and independent checkers are included below supporting_materials.

11. `s6_higher_rung_24d_preprint.tex` — the higher torus wrap, its exact
    local quotient maps and global Euler obstruction, the octonionic
    determinant-boundary sphere, the triality flag and cohomology, and
    the explicitly typed peripheral and stable mod--12/mod--24 bridges.
    The cusp coefficient is computed as zero, and the retained-angle
    Hopf smash is nonzero. The shared modulo-840 lattice/flag-weight
    comparison and full Weyl quotient follow the higher-wrap portion;
    their source provenance accompanies the project. The global torus-wrap
    completion remains open.

12. `s6_retained_cusp_nonlinear_draft.tex` — the original period metric,
    full nonlinear gauge pullback, smooth realization of arbitrary finite
    link fields, exact six-staple `SU(2)` integration, and the extensive
    retained-background integration on a finite four-dimensional patch.

13. `s6_interacting_wilson_variation_draft.tex` — the interacting finite
    `SU(n)` vacuum transform, exact oriented Wilson-loop Dirichlet and
    covariance formulas, repeated-edge terms, center selection, and
    finite-regulator estimates. The actual vacuum measure is retained.

14. `s6_wilson_temporal_transfer_draft.tex` — the exact `SU(2)` temporal
    character multipliers, retained anisotropic coefficients, scalar
    transfer factor, gauge projection, and strong time-continuum and
    resolvent limits on a fixed finite spatial lattice.

15. `s6_spatial_vacuum_elimination_draft.tex` — the actual interacting
    vacuum marginal, conditional-score coupling, form-domain Schur
    resolvent, temporal memory, and corrected physical excitation vectors.
    This addition is source-only.

16. `s6_adjacent_plaquette_quantum_draft.tex` — a nonzero elimination
    coupling and explicit Rayleigh improvement in the true vacuum of the
    specified two-face `SU(2)` complex, including absolute excitation and
    unsubtracted energy quotients, followed by the complete fixed full-box
    extension of its improvement coefficient with every plaquette retained.
    Exact color, Haar, incidence, domain, and rational calculations are
    included. This addition is source-only, under the same root.

17. `s6_magnetic_translation_quantum_draft.tex` — the complete current
    magnetic continuation into the actual interacting vacuum, gauge
    projection, class-convolution formula, full-box plaquette calculation,
    local energy currents with their first surviving quantum state,
    the complete unsigned incidence kernel and electric covariance,
    and the actual first physical excitation band with its complete
    open-box face-graph derivation, followed by the full native
    center-disorder bridge and actual-vacuum spectral moments, plus the
    complete native open-face measure and physical-band transport proofs,
    the full separated-link covariance and spectral-functional result,
    and the complete native leakage volume polynomial and ratio.
    This live editable source is mirrored while mathematics
    continues; no new PDF or continuum mass-gap conclusion is implied.

18. `s6_volume_uniform_local_vacuum_draft.tex` — the complete current
    volume-independent local-estimate calculation in the full interacting
    Wilson vacuum, preserving the original finite-box coefficients.

19. `s6_extensive_quantum_blocking_draft.tex` — the complete extensive
    true-vacuum blocking calculation, exact path-product maps, associative
    memory, and uniform loop spectral-weight analysis.

20. `s6_spatial_continuum_draft.tex` — the complete retained-cusp spatial
    refinement and magnetic-vacuum spectral-measure calculation, including
    the stated finite-regulator sequences and their limiting scope.

21. `s6_xi4_heat_transport_draft.tex` and its supplied reading PDF —
    *The heat generator on the retained inverse-fibre cover*. The complete
    heat, spectral, arithmetic and spatial transport paper includes the
    original fourth-order electric-correlation proof appendix. Its source
    manuscript, complete transitive TeX inputs, original proof snapshots and supplied
    checking material are preserved under
    `supporting_materials/workbench/evidence/ym_sidebar_topics_20260908/xi4_heat_transport/`.
    This paper does not claim a Riemann-hypothesis or Navier–Stokes counterexample.

22. `s6_weak_coupling_physical_draft.tex` — *The original finite-box SU(2)
    Hamiltonian at small positive coupling*. This complete source draft
    retains the nonlinear operator, maximal-tree coordinates and residual
    gauge action in its fixed-box physical-eigenvalue limit calculation.
    Part 2 contains the complete actual-vacuum, observable and spectral-map
    continuation. Part 3 gives the full-vacuum potential moments and
    electric-state graph limit, including raw mode-pair masses and the
    native-state comparison with its stated fixed-box and joint-limit scope.
    All three complete Markdown manuscripts and supplied exact checking
    material are in
    `supporting_materials/workbench/evidence/ym_weak_coupling_20260908/`.
    The stated fixed-volume limit does not claim an interacting continuum
    construction or a continuum mass-gap disproof. No PDF is supplied for
    this source-only draft.

These are maintained shareable drafts derived from the proof-bearing
workbench, not additional authorities or prerequisites.

## Supporting materials

`supporting_materials/` is the evidence and provenance subtree, indexed by
`supporting_materials/README.md`. It contains the maintainable and modular
manuscript sources, reconstruction audits and receipts, the three review
records, annotation sources, reference PDFs, reproducibility scripts and QA
evidence, publication documentation, machine-readable metadata, and preserved
review packages. These files support the four reading entry points above;
active mathematical proofs and ledgers belong in `supporting_materials/workbench/research/`.

Six preserved console records use the suffix `.log.txt` rather than `.log`.
The appended `.txt` is an Overleaf-compatibility filename only; it does not
change the recorded console text. Where an original archive checksum ledger
uses the former `.log` name, that ledger remains frozen as provenance.

## Methodology and model provenance

The authority PDF was transcribed to LaTeX in ten source strips—eight of
11 pages and two of 10 pages—in ChatGPT Professional Pro-mode sessions and
then consolidated. Two independent ChatGPT
Professional Pro-mode sessions performed full mathematical reviews as peers
of the Claude model reported to have produced the original mathematics.
Codex then consolidated the sources and reviews, performed a third
mathematical and TeX audit, built the page-linked annotation layer, replayed
the exact arithmetic, and organized the integrated workbench. The Codex work
used ChatGPT 5.6 Sol in Ultra mode.

The explicit candidate and its original claims remain attributed to their
reported Claude/Fabel source.  The Codex paper is presented as an AI-produced
verification aid, not as a priority claim: it supplies explicit morphisms,
integral matrices, comparison maps, calculations, repairs, and proof
certificates intended to reduce the time required for independent human
checking.  The strength of those additions is stated theorem by theorem, while
specialist replication and external adjudication remain separate questions.

This disclosure is intentionally readable from the online project itself.
Further details are in `supporting_materials/workbench/research/tool_disclosure.tex`,
`supporting_materials/project_documentation/RIGHTS_AND_PROVENANCE.md`, and the
review receipts under `supporting_materials/peer_reviews/`; none requires a
reader to resolve a path on the editor's computer. Model names describe the
recorded tool configuration, not independent mathematical authorship or
verification.

The raw Codex session JSONL is not a publication artifact.  A DOI release
includes the curated mathematical provenance edition defined in
`supporting_materials/project_documentation/PUBLIC_PROVENANCE_POLICY.md`,
together with its redaction receipt and frozen-source hash.  It may also carry
the optional complete sanitized conversation derivative described there, but
only after every profane turn has a hash-anchored neutral summary and an
independent validator reports zero unresolved or privacy findings.
The separate `supporting_materials/publication/full_record_public_annex_v2/`
extends that record with privacy-preserving typed tool and internal-agent
metadata. Its exact 1,483,338,786-byte frozen-prefix identity, deterministic
gzip, automated replay, empty unresolved queue, and parent authorization are
recorded beside the stream; private raw tool bodies are not published.

## Status

The 24 August review recommendation and all of its page-level annotations are
preserved as historical evidence. The subsequent complete-source work records
two exact defects in the published CDP dependency chain and reconstructs the
candidate's construction, topology, algebraic-reduction, and analytic Picard
arguments. In the current workbench, construction, intrinsic
specialization/Leray, based van Kampen/sphere recognition, algebraic
reduction, Proposition 10.8 uniform non-torsion, the independent
cellular-collapse/Mayer--Vietoris comparison, and the exact cotangent/Hodge
calculation are marked **VERIFIED** in the local sense defined there. The
cusp-local Picard obstruction is also **VERIFIED**: it constructs a line
bundle on the cusp neighbourhood whose normalized restriction to `dP6` is
nonzero, so no purely cusp-local argument can prove the global zero
restriction. The completed third certificate incorporates both finite
fillings through holomorphic `O*` factors and a toric support function, and
avoids both global integral Leray and local integral specialization. In each case, a
complete auditable proof is written in the workbench. In particular,
`R^0f_*Omega_X^1=O(-2)`, `R^1f_*Omega_X^1=O+O(-1)^2`,
`R^2f_*Omega_X^1=O+O(-1)`, `h^{1,2}=1`, `h^{1,1}=2`, and
`E_2=E_infinity`. The same data give total Bott--Chern dimensions
`(1,0,2,2,2,2,1)`, total Aeppli dimensions `(1,2,2,2,2,0,1)`, and
non-ddbar degrees `(0,2,4,4,4,2,0)`. Exact marked-fibre period formulas
extend to explicit global Bott--Chern generators, and their full bigraded
algebra is
\(H^{*,*}_{BC}(X)=\mathbb C\mathbf1\oplus N_{\mathrm{BC}}\), with
\(N_{\mathrm{BC}}^2=0\) for the positive-degree ideal
\(N_{\mathrm{BC}}\).
This determines the global cohomology classes and every product but does not
assert a preferred literal global coefficient atlas through the finite
fillings and cusp. Independent specialist replication and external CDP
adjudication remain **OPEN**. Frozen reviewer labels are not
silently rewritten; current status is governed by the annotated front matter
and the workbench ledgers.

The native \(\mathbb T^2\times\mathbb R^2\) cusp quotient has also been
globalized in the precise sphere-carrier sense requested later.  After a based
choice \(X\cong_{\mathrm{diff}}S^6\), the workbench constructs the continuous
surjective conical-target quotient maps
\[
 q_2^{\wedge2}:S^{12}=X^{\wedge2}\twoheadrightarrow\mathcal A^{\wedge2},
 \qquad
 q_1^{\wedge4}:S^{24}=X^{\wedge4}\twoheadrightarrow\mathcal C^{\wedge4},
\]
and the further sphere-target quotients
\[
 \widehat q_3^{\wedge2}:S^{12}\twoheadrightarrow S^6,
 \qquad
 \widehat q_\gamma^{\wedge4}:S^{24}\twoheadrightarrow S^8.
\]
Both full carriers are based null-homotopic.  For any based
\(f:S^6\to S^2\), the smash square factors through
\(f\wedge\operatorname{id}_{S^6}=\Sigma^6f:S^{12}\to S^8\), and
\(\pi_{12}(S^8)\cong\pi_4^{\mathrm S}=0\).  Thus \(f\wedge f\simeq *\) and
\(f^{\wedge r}=(f\wedge f)\wedge f^{\wedge(r-2)}\simeq *\) for every
\(r\ge2\).  In particular, the full surjective quotient
\(\widehat q_\gamma^{\wedge4}\) is based null-homotopic.  For any based
\(g:S^6\to S^3\), write \(\operatorname{st}\) for stabilization.  The exact
data
\[
 \pi_6(S^3)\cong\mathbb Z/12,
 \quad \pi_3^{\mathrm S}=\mathbb Z/24\langle\nu\rangle,
 \quad \pi_6^{\mathrm S}=\mathbb Z/2\langle\nu^2\rangle,
\]
\[
 \pi_{12}(S^6)=\mathbb Z/2\langle\nu_6\circ\nu_9\rangle,
 \qquad
 \operatorname{st}:\pi_{12}(S^6)\xrightarrow{\ \cong\ }\pi_6^{\mathrm S}
\]
use the group table in Hatcher, p. 339, and the signed smash/stabilization
calculation in Toda, Propositions 3.1 and 5.11.  Since \(12[g]=0\),
\(\operatorname{st}([g])=2a\nu\).  Therefore
\[
 \operatorname{st}([g\wedge g])
 =\operatorname{st}([g])^2=4a^2\nu^2=0,
\]
and injectivity of the displayed stabilization map gives
\([g\wedge g]=0\in\pi_{12}(S^6)\).
Thus \(g^{\wedge r}\simeq *\) for every \(r\ge2\), and in particular
\([\widehat q_3^{\wedge2}]=0\in\pi_{12}(S^6)\).  The one-copy classes of
\(\widehat q_3\) and \(\widehat q_\gamma\) remain uncomputed.  The unstable
classes of \(q_2^{\wedge2}\) and \(q_1^{\wedge4}\) remain **OPEN**; the class of
\(q_{1,\mathrm{cusp}}^{\wedge4}:S^{24}\to\mathcal B^{\wedge4}\) is likewise
uncomputed.  The moving target four-spheres have eventually exact Euclidean
balls and converge pointed-locally to \(\mathbb R^4\).  Two copies are
rank-minimal cusp-locally and four are rank-minimal over the full regular
base.  Their based inclusions into \(S^6\) and \(S^8\) are separately
null-homotopic.  Fixed unrescaled target metrics collapse the slices to the
cone vertex, the full cusp-adapted metric bubbles have dimensions \(8\) and
\(12\), and no source-sphere metric, almost-complex structure, physical
spacetime, or interacting Yang--Mills theorem is thereby obtained.

The workbench now also proves the strongest corrected CDP conclusion supported
by the intact argument. If one `L0` satisfies
`H^2(X,T_X tensor L0)=0`, then generic off-degree-one vanishing and
`c3(X)<=0` follow; one vanishing `R^2 f_*(T_X tensor L)=0` is a sufficient
relative hypothesis. On reduced full fibres, the invalid p. 692 shortcut is
replaced by the exact injectivity condition on the conductor connecting map
after the two endpoint vanishings. The candidate fails the global and relative
conditions by different arguments: `c3(X)=2` and the corrected theorem imply
`H^2(X,T_X tensor L0) != 0` for every `L0` by contraposition, while the cusp
conductor makes `R^2 f_*(T_X tensor L)` nonzero for every `L`.

The 4 September worldline reduction computes the exact finite-dimensional
phase spaces associated with the later \(SU(3)\)-Gram model.  With
\(P_\alpha(Z)=\alpha Z^*Z\), the massive rank-two shell reduces
symplectically to
\(T^*\mathcal H^+_{m_0,c}\) by
\([x,p]\mapsto(p,A\mapsto-\langle x,A\rangle_L)\) under the retained
convention \(\Omega=-\mathrm d\langle p,\mathrm dx\rangle_L\).  On the
nonzero rank-one stratum the intrinsic quotient is
\(T^*\mathcal N_+^\times\), but
\(\mathrm d(\det P_\alpha)_Z=0\) on the rank-at-most-one locus: the written
multiplier action yields \(\dot x=\lambda p\), not \(\lambda=e\), has four
rank-opening ambient null directions, and at \(Z=0\) admits arbitrary
\(x(\tau)\).  For the packet with fixed
\(\lambda_0>0\) and \(\omega_0\ne0\), the exact momentum map has rank four
off the threshold and rank three at the threshold; direct variation gives
\(\dot p=0,\dot x=0\) above threshold and the ordinary characteristic only
at threshold.  Its positive spectral endpoint is therefore a
constraint-selected algebraic threshold in a separate multiplication/Fock
representation, not a dynamically generated interacting Yang--Mills mass.
The complete proofs and the 39/39 exact companion checks are in
`supporting_materials/workbench/research/worldline_presymplectic_reduction.tex`
and its evidence directory.

For every line bundle `L`, the all-Pic conductor input now has three independent
certificates. The global Leray-edge proof kills the permanent-cycle image of
`c1(L)` using `d2^(0,2)(2q)=omega[delta]`. The newer direct boundary proof
instead writes `c1(L|F)=2nq` and computes the three pair-of-pants defects as
`(4n,-3n,0)[delta]`; their boundary sum forces `n=0`, and local Chern
specialization makes the normalized restriction to `dP6` trivial. The second
proof uses no global Leray differential or packaged `H^2(X;Z)=0` theorem. The
third proof gives `(dbar1,dbar2,dbar0)=(2k,-3k/2,0)[delta]` for
`c1(L|F)=kq`, so boundary balance forces `k=0` without integral
specialization. Its central support-function polarization is
`B=[[d2+d3,d3],[d3,d1+d3]]`, with mixed block
`E_L((lambda,0),(0,m))=-B(B0 lambda,m)`; unimodularity of `B0` forces all
central degrees to vanish. The cusp-local obstruction explains why both
finite fillings are essential to this global analytic proof.

Reviewer B's 26 August follow-up independently confirms the
properness–flatness–top-base-change–duality–conductor chain from its three
named candidate inputs. Its seven-page report, fail-closed ledgers, and eight
exact local certificates are under
`supporting_materials/peer_reviews/reviewer_B_candidate_validation_2026-08-26/`.

### 4 September gauge and metric continuation

The existing quaternionic draft contains the complete homogeneous gauge
equations and exact constant-matter frame maps. The literal moving-kernel
orbit has no lift with arbitrary time-dependent real-skew connections,
nor with constant spatial fields in the constant-matter frame and arbitrary
complex temporal connection. Their stated matter-stabilizer gauge
saturations are also excluded. Arbitrary time-dependent complex `su(3)`
lifts outside these classes remain open (`q444:static-lift-system`,
`q444:real-no-lift`, `q444:static-complex-no-lift`).

A different, current-free full-gauge sector supplies exact nonconstant
periodic fields with arbitrarily small positive classical frequency and
finite-volume energy excess, and exact nonlinear null waves
(`q444:vk-sector`, `q444:vk-periodic`, `q444:vk-wave`). The full retained
gauge-inertia calculation gives all eight classical transverse mass branches.
The nonlinear gauge-invariant conserved current detects the diagonal branch
with `mu_d^2=(2g^2/3)||b||^2`, equal to `2g^2/(3V_mu)` times the
marked determinant Haar average (`q444:gauge-spectrum`, `q444:current-mass`).
This is a proved linearized classical mass relation in the specified
adjoint-plus-fundamental theory, not a pure quantum Yang–Mills spectrum.

The positive period weight `W` is the lattice cometric; its inverse is the
covariant lattice metric. At fixed original periods, Hermitian compatibility
gives exactly `h3=2H^-1`. Native Euclidean `h3=I` yields `H=2I`,
`G=2PP*`, and quotient metric `h2=(PP*)^-1`. The unchanged-lattice
character spectrum is `lambda_k=4pi^2 k^T W k`; the source and quotient
first positive gaps are asymptotic to `4pi^2/y^2` and `8pi^2/y^2`,
respectively, with the full corrections and `y=-log|t|/(2pi)` retained
(`q444:hermitian-cometric`, `q444:torus-laplace`,
`q444:metric-submersion`, `q444:native-period-spectrum`). The earlier
12- and 17-dimensional positive cometric fibres and the exact rank-loss
condition-number cost are unchanged. No preferred global dynamical metric
or interacting quantum Hamiltonian is inferred from these geometric spectra.

The same draft is integrated into workbench.tex and its overview. Evidence,
portable checkers, build/visual receipts and updated Pro feedback are in
supporting_materials/workbench/evidence/quaternionic_4441_audit_20260904/.
S6_CURRENT_FULL_TEX_FOR_AI.md embeds the current source and bibliography
bytes. Frozen publication artifacts and original reviewer annotations
are unchanged.

## Rotating-gauge and moving Fourier-state continuation

The quaternionic draft now includes the complete genuinely complex
restricted rotating-pair exclusion, the positive unrestricted Gauss
inverse with both frequency signs, the full scalar-coordinate
equivalence, the quantitative stabilizer signature constraint, and
the two-by-two spatial stress equation. The 5 September continuation below
determines every fixed-pair coupling fibre exactly and places the complete
spatial projection inside a proper algebraic exceptional set. Existence
within that set and global emptiness of the full rotating ansatz remain open.

The quantum draft now includes an actual quartic ground-state isometry,
its exact Berry/Born-Huang and off-diagonal terms, full domain proofs,
and a finite-energy physical-time error O(V3^-1/2) in its explicitly
proved regime. All Fourier interactions remain. This is a precise
two-coordinate quantum comparison, not a continuum gap claim.
The same proofs are embedded in workbench.tex and reflected in the overview.
Current proof/check/build receipts and Pro feedback are in the evidence
directory above. The historical source and annotations are preserved.

## 5 September: exact finite coupling and spatial projection

The existing quaternionic draft now contains the full residual polynomial,
with degree exactly twenty-eight whenever Q7 is not identically zero,
and exact both-sign reconstruction. Every fixed unrestricted
spatial pair has at most fourteen positive g² values and at most twenty-eight
original solution tuples. Three explicit vector tests detect an identically
empty Gauss denominator domain. A nonzero 24-by-24 Sylvester determinant
polynomial places all possible spatial solutions inside a proper closed,
nowhere-dense, measure-zero real algebraic set in all sixteen coordinates.
The displayed full-pair witness has exact rational and finite-field
certificates; the independent full-eight-dimensional replay gives determinant
60 modulo 101 after the retained denominator multiplication. Existence within
the exceptional set is still open. These are results for the stated rotating
ansatz, not arbitrary complex time dependence or a continuum quantum spectrum.

Complete proofs are included in the quaternionic draft and `workbench.tex`;
the mathematical overview gives the explicit polynomial and map. Reproducible
source/check certificates are under
`supporting_materials/workbench/evidence/finite_coupling_20260905/`.
The designated [final build receipt](../workbench/evidence/finite_coupling_20260905/FINAL_BUILD_RECEIPT.json)
records the measured build results when complete. Earlier retained-angle
page counts and release receipts continue to identify their dated checkpoint.

## 5 September: exact exclusion within the exceptional spatial set

The quaternionic draft and workbench now contain the full proof excluding
the eight-dimensional linear class where both spatial matrices exchange
the matter line and its orthogonal complement. Gauss forces the temporal
block; complete scalar and gauge residuals yield a strictly positive
contradiction for every original g²>0 and both frequency signs. The same
class lies inside the spatial Sylvester zero set, through an explicit
degree-four block factor and its squared common residual factor.

A new denominator-free residual identity gives a positive lower bound for
the full spatial-equation error on the exact scalar-plus-Gauss zero set.
The bound is uniform when spatial norm is bounded and g² stays away from
zero. The subsequent complete scalar--Gauss classification below proves
that its constrained domain is nonempty at every original positive
coupling. This is a spatial-error certificate; no quantum mass gap follows.
Existence of full solutions outside the
excluded class is still open. Full equations, inverse coordinate maps,
proofs, and 28 exact checks are retained under
`supporting_materials/workbench/evidence/two_cross_exceptional_20260905/`.

## 5 September: the complete scalar--Gauss domain at every coupling

For `delta=sqrt(2/3)`, the classified domain is exactly
`D x {+1,-1}^2 x U(1)^2`, where
`D={(u,v0,y):u>0,d=u*v0-delta^2-y^2>0,c=4*v0-5*u>0}`.
The original coupling is `t=g^2=72*d/c`. The full literal domain adds
the frame phase zeta and is in bijection with the quotient by the sole
free involution `(p_plus,p_minus,zeta)->(-p_plus,-p_minus,-zeta)`.
All inverse matrices, both sign choices and continuous phases are retained.

At every prescribed original `tau=g^2>0`, the exact choice
`rho=(tau+sqrt(tau^2+4608*delta^2))/(96*delta)` with
`M=delta*[[rho,1],[1,2*rho]]` gives `t=tau`. Every scalar and Gauss
entry vanishes. The two spatial residuals cannot vanish simultaneously throughout this
class, and full existence on the remaining unrestricted exceptional set
remains OPEN. The shared source `scalar_gauss_domain_shared.tex` is included
once by the common quaternionic host; complete proof, independent review,
and all 25 exact replay groups are retained under
`supporting_materials/workbench/evidence/scalar_gauss_domain_20260905/`.
Historical annotation snapshots and dated release receipts are preserved.

The smooth continuation `scalar_gauss_smooth_shared.tex` follows that
source once in the common quaternionic module. It proves
`S_sg ≅ {+1,-1}^2 x (0,infinity) x R^2 x T^3` in literal matrix coordinates.
There are four embedded six-dimensional components; the unchanged original
`t=g^2` is the positive coordinate, and each fixed positive coupling has
four embedded five-dimensional components `R^2 x T^3`. The smooth inverse
retains every sign and phase. It imposes no spatial equation or physical
gauge quotient and yields no quantum spectral conclusion.

The current period/cusp refinements are in `candidate_geometry.tex`:
`prop:period-exact-admissible-constants` gives precisely `Im(c0)<-M`,
where `M=max_(B minus p0) D_part` is attained. The cusp-free affine solution
`beta(z)+i*t(pi(z))` has `D_tilde=D+Re(t)` unbounded above.
`eq:cusp-exact-opposite-edge` retains the multipliers
`exp(-2*pi*i*mu0)`, `exp(12*pi*i*mu0)`, and
`exp(-2*pi*i*(7*mu0+b0))` in the stated same-character conventions.
The proof now states restricted chart domains, the fixed closed-subdisc
bound and weak inequalities for closed polydiscs explicitly. These bounded
period, cusp and finite-filling audits add no sphere-identification or CDP
theorem; source integration is separate from build and publication receipts.


### 6 September: exact lattice, spectral, umbral, and parameter maps

The higher-rung draft now includes the full Albert orbit family and an
inverse-bearing spectral/projector map of the common marked lattice.
The shared ES/lattice draft includes the complete D4 cubic image and exact
CDH shadow, theta multiplier, glue-action and Fricke coefficient maps.
The workbench also proves the retained analytic family's identifications
modulo 2Z, with all finite-filling and cusp maps. The overview and AI source
bundle follow these sources. Historical annotated and clean roots remain
unchanged. This update does not announce a new moonshine module or infer
the original sphere theorem from these parameter calculations.
