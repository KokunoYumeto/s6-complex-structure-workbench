# Root mathematical audit — live record

Reader: GPT-6 Astra (OpenAI, ChatGPT Pro mode), 17 November 2026.
This records an independent reading of the producing runs, not a self-check by
those runs. A mathematical argument and an unopened literature dependency have
separate states. No blanket completion is inferred from a source's heading.

## FAMILY: recorded check preserved

`reviews/S6_02_REVIEW_FABLE/REVIEW.md`, §§1–3, was read in full, including
all 55 per-result rows. Claude Fable 5.2 (Anthropic), effort high,
12–13 November 2026, read all four proof sections, independently checked the
listed exact identities, and re-certified all 19,701 interval boxes. Its
44 correct, six known, two qualified and three open verdicts remain part of
each result's history. The qualification of B.3.1 is addressed by PUSH E.1's
explicit dictionary; the E.2.2 Eells–Kuiper definition is retained as a
reduction and the actual determination is in Paper III. The former questions
C.3.3 and E.1.5 are answered by PUSH D.1 and A.3, respectively. The two issues
in E.2.3 are separated: analytic non-filling (Paper I, PUSH B.4.33) and smooth
monodromy (Paper III). A later answer does not erase the original partial
argument. Every retained source proof is present in the candidate, subject to
the explicit duplicate/notation editing manifest.

The current rerun `code/family/rerun_manifest.json` (or the manifest named by
the runner) records the selected original mathematical programs. The PUSH
Arb rerun is a genuinely independent interval implementation. All 19,701 norm
boxes passed with maximal squared bound
1.999877571767410524070536478244687423578792301873142913, with the saved ball
radius below 9.26e-56. This establishes the numerical substep only; the local
analytic and cusp arguments are retained in full.

## PUSH: actual cusp origin and non-filling

The following full arguments were read and re-derived in this writing:
B.4.4, B.4.9, B.4.18–19, B.4.24, B.4.27, B.4.30–33. The original
independent reader's checks of B.4.24, B.4.26, B.4.30 and B.4.33 are also
preserved: `reviews/S6_FINAL_INTAKE_20261116/EXPERT_POSITION.md`, Claude Fable
5.2 (Anthropic), effort max, 16 November 2026. The high-effort final intake
explicitly did not read B.4.24 or B.4.26; the expert subsequently did.

* B.4.4: proper direct image of the relative bi-anticanonical line bundle is
  a torsion-free rank-two sheaf on a disc, hence locally free. The pencil is
  meromorphic on the total space. The graph gives the required meromorphic
  map. After vertical components are removed, the critical image is analytic
  and its three individually marked degree-one branches extend. The
  cross-ratio normalizing their target positions is meromorphic. No
  central Kähler hypothesis is used.
* B.4.27: on a sequence of point blowups of a bidisc, the exceptional tree
  gives H²(Z)=Z^N and the other required H¹,H³,H⁴ vanish. Laurent-chart
  computations give H^j(O)=0 for j>0. The exceptional intersection matrix is
  unimodular, so its divisor classes generate Pic. For the two permitted
  logarithmic divisor sheaves, H¹(M^gp)=0 and H²(M^gp)=Z^N. The period map
  on H² is diagonal with nonzero factors 12ma_i and 12ma_i+12nb_i. Its
  injectivity yields H¹(A)=0. The forbidden first-character order along the
  strict r-axis is retained throughout.
* B.4.30: the analytic logarithmic de Rham comparison supplies a locally free
  canonical extension without a Kähler assumption. In a semistable chart
  t=x_1...x_k, k≤3, the closed relative logarithmic one-form sheaf and the
  normalized invariant-form subsheaf are t-saturated inside the canonical
  extension. They agree off t=0 and therefore agree. Reduced connected
  central fibres give torsion-freeness of R¹O via the multiplication-by-t
  sequence. Angular periods are integral in the primitive cocharacter
  lattice; integration term by term divides by nonzero integers of absolute
  value at least one. Characters are units times integral monomials.
  Chains of local charts and sections across the connected fibre extend
  differences. The coefficient-ideal blowup lowers the excess fibre
  dimension by one; normal finite surface multisections are Cohen–Macaulay,
  and finite flat after the stated normalization. Principalization and
  resolution reduce generic exceptional points to t=unit·prod(x_i^m_i).
  A divisible root and a height-one lattice-polygon subdivision give a smooth
  reduced normal-crossings model. Only the analytic toroidal correspondence,
  not a projective semistable-reduction theorem, is used. Generic cyclic
  splitting of finitely many multisections gives a uniform norm exponent.
  Hartogs extends the normalized character units and their inverses across
  the finitely many omitted points. The integral first-character exclusion
  is unchanged by this operation. Literature statements are checked below.
* B.4.31: the finite set of angular meridians is permuted by the base
  monodromy and lies in ker E. On the quotient by delta the remaining
  rank-two representation is the full SL_2(Z), which has no nonzero finite
  orbit. Every angular meridian is therefore a multiple of delta.
* B.4.32: origin changes contribute only delta. The cap-section defect is a
  flat class in Lambda_Q/Q delta. The fixed lines for the two finite
  monodromies are Q(1,2,-4) and Q(1,3,-3), with zero intersection.
* B.4.33: the extending origin has zero gamma defect against both local
  origins; the actual transition has nonzero gamma winding. Its norm gives
  0=D n with D,n>0. This contradicts a filling. The exact constant and sign
  identities were independently recomputed in
  `code/editorial/root_cusp_origin_audit.py`.

The actual-origin issue left outside the scope of the expert's check is
resolved as follows. With gamma=(6mu,C-s-12v), delta=(0,1), the transition is
F=(mu(s+12v)/2,C(s+12v)/12-(s+12v)^2/24+6v). Its s- and v-differences are
the claimed periods, including Delta_v(n)F=n gamma-6n(n-1)delta. In the
ordinary/cusp overlap, the comparison has second constant
D=C_0,21-12kappa_0. The origin sigma(c)=(-c mu/2,-c²/24-cD/12) gives exactly
the closing cocycle. Root's independent polynomial calculation and the maps
auditor's independent reconstruction agree. Integral deck factors
exp(2pi i h lambda_1) are one. No conclusion rests on a formal cocycle whose
geometric origin has not been matched.

## PUSH E.2: stability chain (transferred to Paper II)

All of E.2.4–E.2.24 have now been read, including E.2.7 in this writing.
Their expanded full text is preserved in `push_E2_stability_for_II.tex`.
The mathematical steps below passed; remaining exact source verification is
tracked separately in the bibliography record.

* E.2.5: the relative Picard vector group gives a unique root
  L^D=K^A for A=12kl and D=kl-3k-4l≠0. Direct image injects the two generic
  sections into the central space of sections. The valid CDP theorem on
  nonholomorphic meromorphic maps and c_3 excludes indeterminacy on S^6.
  Two independent functions would produce local indeterminacy, so the
  algebraic dimension is one. Stein factorization gives P¹ and the residual
  effective fixed divisor.
* E.2.6: for positive canonical slope, c_1(K_F)=0 and surface theory imply
  kappa(F)≥0; positive kappa would make a meromorphic ratio nonconstant on a
  general fibre. Thus K_F is torsion and the horizontal fixed divisor is
  absent. Flat irreducible general pencil divisors and connected central
  normalization remove the vertical fixed part and force degree one.
  A smooth surface with the torus topology and these invariants is a complex
  torus. The reduced fraction of 1/m+1/n recovers coprime m,n. Opposite signs
  would make the canonical bundle torsion, contradicting the volume/Stokes
  argument.
* E.2.7: bounded z=exp(-pi i c/(kl)) extends. The three critical sections may
  collide but their normalizing projective transformation is meromorphic.
  A fixed ordinary target gives a smooth compact torus family over the disc,
  with identity H_1 monodromy. A zero of order d in z contributes S_-h,
  h=2kld>0. The base path has ordinary, finite peripheral, or cusp peripheral
  monodromy. Finite cases cannot cancel S_-h after taking order 3 or 4.
  In the cusp case I+nN-hE is identity only if n=h=0, since its u-to-w
  coefficient is n. The maximum principle excludes the outer radius.
  Translation comparisons do not affect H_1.
* E.2.8: Alexander-duality ranks force irreducible fibres and trivial
  rank-one H¹ monodromy. A horizontal effective divisor would give a
  topologically trivial effective divisor on a class-C normalization, which
  is impossible by a Kähler integral. The negative-slope residual case has
  a class-VII normalization with b_1=1.
* E.2.9: H⁰(V(-nD)) stabilizes to zero by finite dimensionality, Krull
  intersection and analytic continuation; the full nonreduced support is
  handled by its finite filtration. Relative Gorenstein fibre duality gives
  the complementary H² vanishing for large n. Compactness supplies a common
  n; positive base twist kills H²,H³, while a separate negative twist kills
  H⁰. Along an affine holomorphic Picard line each jumping set is proper
  analytic, so one bundle avoids all three. Hence chi(B)≤0. For B=T_X,
  Hirzebruch–Riemann–Roch gives chi=c_3/2=1, a contradiction. This proof
  allows a non-Kähler general fibre and is not a duplicate of CDP E1.
* E.2.10: the previous horizontal-vanishing result reduces either slope to
  the vertical argument of E.2.6.
* E.2.11: under the explicitly assumed good Jacobian extension on a bidisc,
  Hartogs extends the torsor fields. Completeness on compact fibres gives
  a torus action. A connected stabilizer acts trivially on the fibre tangent
  by holomorphic representation theory and on the base quotient; averaging
  splits the tangent representation, then local linearization forces the
  stabilizer to be trivial. Finite isotropy remains. A flowbox gives a finite
  transverse map C²→B; an isolated critical point would force a critical
  determinant curve. Thus the map is a submersion and the finite isotropy
  is trivial as well.
* E.2.12–13: finite monodromy forces its order to divide the local exponent,
  so the finite period model extends after its holomorphic root. A cusp
  unipotent power cannot be identity. On a punctured bidisc the period
  kernel extends, supplying the good Jacobian required in E.2.11.
  Normalizing r^m=a^m·unit gives free unramified root charts; purity then
  forces the exact central multiplicity. No unproved extension of an
  arbitrary Jacobian is assumed.
* E.2.14: comparison with a central regular bidisc extends the coefficient
  of the normalized delta field; a zero would divide the generator by the
  base parameter and contradict its primitive choice. The complete
  period-one action is transported equivariantly. A collapse of the finite
  marked tori would extend the delta flow to a compact elliptic action with
  a fixed point, impossible for a nontrivial compact complex group action.
* E.2.15: in the remaining isotrivial case the marked periods are constant.
  A pluricanonical volume integral gives
  integral |q^(-D-2A)phi(1/q)|^(2/A)<infinity. Subharmonic estimates imply
  pole order at most A-1. If D≥-A this would make the entire nonvanishing
  phi extend with a zero at infinity. Here D/A≥-1/2, so collapse is excluded.
* E.2.16: the finite multiplicities are exact and the critical supports
  irreducible. The fundamental group maps onto the triangle group
  Delta(m,n,d); for d≥2 it is nontrivial (including the (3,4,2) finite
  case), hence d=1. Euler number and the invariant-cycle statement then
  determine the cusp normalization's first Betti number.
* E.2.17: conservation of the plane Milnor number and nonsplitting give a
  single ordinary node in transverse flowboxes. At the fixed curve the
  invariant function has the form T g(T,z), T=xy, and g(0,z) is a nonzero
  section of O(2). A double zero would split a plane singularity into two
  critical points with the same critical value, forbidden by nonsplitting.
  Thus there are precisely two simple zeros and the actual family has the
  claimed xy/xyz models. Normalizations vary smoothly.
* E.2.18: the normalization has b_1=0,b_2=4 and a hexagon of six (-1)
  curves. Contracting three alternate curves leaves b_2=1 and a triangle
  of (+1) curves. Its canonical degree is negative, giving P²; the original
  pair is its blowup at the three vertices. The toric logarithmic tangent
  frame persists by base change.
* E.2.19: conductor transition matrices of logarithmic vector fields are
  constant on each compact component and identity off the central
  parameter, hence identity everywhere. The normal-crossings equalizer has
  no extra triple-point condition. Complete commuting fields and primitive
  period loops recover the actual two-dimensional torus action, including
  its full central lattice and the integral toric characters.
* E.2.20: a stratified q-preserving transport identifies the actual cusp
  covering. The union of maximal infinite-fan charts is simply connected;
  the deck group is Lambda/Lambda_tor. Crossing q=ab expresses adjacent
  origin ratios as powers of q times units, with no essential singularity.
  Unimodular triple characters identify the actual charts by Laurent
  monomials times these units. A finite fundamental domain gives a common
  neighbourhood; no infimum over infinitely many shrinking radii is used.
* E.2.21: finite affine classes are integral and locally constant. Vector
  remainders are removed by finite averaging. Collar period classes,
  including the cusp, are constant. The exact sequence with O·delta and
  O(-infinity) has H¹=0, and a Cauchy/Laurent solution depends holomorphically
  on parameters. This identifies the actual whole family.
* E.2.22: propagation removes finitely many analytic discrete layers for
  the pencil, critical sections, roots, normalization and NC rank tests,
  toric action, and period kernel. Identities propagate from the known open
  set; the real determinant stays in the admissible component, including
  at finite roots. Fill the layers in reverse order using E.2.21. A deleted
  layer may accumulate only at an earlier deleted one, which this ordering
  handles.
* E.2.23: the known locus is locally open; connected Riemann-surface
  propagation makes it closed. Finite projection of an arbitrary analytic
  branch to a polydisc and a complex line yields a curve connecting a
  known point to the tested point. Normalize that curve and apply the disc
  result. The recovered multiplicities distinguish the components.
* E.2.24: the C-infinity Kuranishi local product/retraction transports the
  analytic-base result to the space of integrable structures. Each specified
  pair gives an open and closed invariant set and therefore an open and
  closed subset in the diffeomorphism quotient. The cited precise local
  Kuranishi theorem is checked separately, not replaced by a generic
  assertion about moduli spaces.

## External analytic sources already opened and matched

* Illusie–Kato–Nakayama (2005), Theorems 6.2–6.4: proper separated fs log
  smooth analytic morphism, log-smooth base (or exactness), constant
  unipotent coefficients, and torsion-free characteristic cokernels in the
  semistable charts give the ordinary locally free canonical log de Rham
  extension used above. No polarization or Kähler condition is added. The
  2007 erratum addresses the algebraic Hodge statement 7.1, not 6.3.
* Kajiwara–Kato–Nakayama (2008), Definitions 1.2.3–1.2.6, Lemma 1.2.9,
  §§1.3 and 5.1.1–5.1.2, Theorem 5.3.2: the pairing and admissible ghost
  data define an unpolarized log complex torus. Pullback preserves the
  required admissibility/nondegeneracy. A Y-invariant fan with full support
  and finitely many Y-orbits gives a proper log-smooth analytic model.
  Projectivity is not asserted or needed. The diagonal ghost data in the
  application satisfy the face-by-face nondegeneracy conditions.
* Bierstone–Milman (1995 preprint), Theorems 1.6 and 1.10: analytic
  embedded resolution and principalization on relatively compact sets;
  these, rather than a compactification theorem, are used locally.
* Parusiński (1990), Corollary 1.2 and its coefficient-ideal proof, pp.3–5
  of the manuscript: finite projections and principalized coefficients
  lower the excess fibre dimension. The proof has been read and matched
  to the proper local excess-one application.
* Enokizono–Hashizume (2024), Lemma 2.14 and proof: analytic strict toroidal
  subdivisions correspond to proper modifications. Only this local
  correspondence is used; the projective hypotheses of the main theorem
  are not imported into the analytic non-filling proof.

## Computational discrepancies

## Complete current reading of the untwisted and auxiliary end models

Reader throughout this section: GPT-6 Astra (OpenAI, ChatGPT Pro mode),
17 November 2026. Every statement and complete proof in PUSH A.1–A.4,
B.1–B.3, and B.4.1–B.4.33 was read, with the following rederivations.
This records the mathematical reading; the separate literature ledger
controls which external dependencies have also been verified.

* A.1.1–A.1.2: the rectangular-cone dual monoid gives `xy=uzv`;
  the core and nodal collars have compact representatives, and the
  norm inequalities separate all overlapping translates. Relative
  Cohen–Macaulayness and pure dimension give joint flatness. The
  displayed small resolution has normal `O(-1)⊕O(-1)`.
* A.2.1–A.2.5: the two prism triangulations, mixed-ray obstruction
  to joint flatness, infinite disjoint star centres, explicit blow-up
  charts and both flops were checked. The universal-blow-up assertion
  is refuted by the `P³` Betti number. The finite fan algorithm tests
  containment, determinants, volume, boundary matching and orbit
  finiteness. Exhaustiveness and termination use only corrected weak
  factorization, not the withdrawn strong-factorization argument.
* A.3.1–A.3.3: analytic perfect-complex K-classes and fibre cycles
  give the virtual Euler invariant without a Kähler assumption.
  The alternative smooth-total-space vanishing-cycle proof is
  distinct and retained. The iterated curve blow-ups are disjoint
  from the conductor and have normal `O⊕O(-1)`, so their normal
  deformations split and preserve the stated crossing conditions.
* A.4.1–A.4.9: all integral Thom, Gysin and Mayer–Vietoris maps
  were recomputed conceptually against the exact reruns. The
  discriminant is 11, the nearby Betti tuple is
  `(1,1,8,14,8,1,1)`, and the degree-three monodromy Smith entries
  are `1,1,1,1,1,11`. The global all-fan argument retains integral
  blow-up summands. Its second proof uses actual sheaf-level Gysin
  splittings and local augmented branch-simplex complexes over Z,
  rather than rational averaging.
* B.1.1–B.2.3: the actual unit factors give the free rotations
  `+4,-3`; the ruled normal line is generally nontorsion. All
  base-changed minimal fans and the extension to arbitrary finite
  fans use the correct peripheral labels. A local change of origin
  is not asserted to extend globally.
* B.3.1–B.3.8: the rotation sum obstruction, genus-three cyclic
  cover, valuation lower bound for cusp multiplicity, Mordell–Weil
  height matrix, saturation exclusion, trace `12ZP`, degree-six
  transgression and Poincaré line adjustment were rederived. The
  only possible half-lattice classes have forbidden heights;
  local divisibility uses the identity Néron component. The
  analytic torsor has `b1=6`; Buchdahl's even-Betti theorem applies
  to that compact smooth surface.
* B.4.1–B.4.6: both specialization-surjectivity proofs are retained:
  logarithmic rounding and the independent gradient-retraction /
  normal-meridian proof. The Du Bois conclusion is algebraic;
  the analytic Hodge conclusion assumes the stated closed-stratum
  condition. The normalization argument uses the ddbar lemma only
  on the stated pieces, and the block argument checks the actual
  five-term maps. Historical wording that denies a priority claim
  is to be removed; it is not mathematical content.
* B.4.7–B.4.8: the Cartier elliptic cocycle has Chern vectors
  `1,i,1+i`; the two central fibre inclusions kill both lattice
  generators. The degree-one Mayer–Vietoris map is unimodular.
  The good-reduction interface has the nonzero mixed Chern class
  `(0,mN)` after every cover, and moving translations cannot
  remove it because the normal line has fibre degree zero.
* B.4.10–B.4.14: the explicit moving Kato embedding, convergent
  infinite products, normal factors, negative elliptic contraction
  and local-to-global obstruction sequence were read in full.
  The degree-eight cone is explicitly smoothed by an anticanonical
  quadric, and its vertex blow-up has equation `t=ξe`. All three
  normal products include the triple-curve line. The third space
  is proper over an open disc, not compact. The finite-support
  and nonzero-normal-degree obstructions are separate arguments.
  The global vector-field germ equation leaves only the Euler
  field; the holomorphic Lefschetz sum is the constant `-8`,
  giving nine trivial tangent-cohomology characters and eight
  after contraction. The twist `O(-b)` means a single point of
  `P¹` and has degree `-1`.
* B.4.15–B.4.17: the cocharacter is single valued in the actual
  rank-three semiabelian quotient. The small-resolution charts,
  Cartier twist, properness, vertical projective bundles and their
  two-curve blow-ups were checked. The dual complex is a cylinder
  with 36 literal elementary collapses. The constant-sheaf
  branch resolution includes the alternating branch action for
  self-crossings. The compact-base counterexample has trivial
  monodromy and central `b1=0` versus nearby `b1=1`; it corrects
  the cited unrestricted invariant-cycle assertion, not the
  irreducible-support version used elsewhere.
* B.4.20–B.4.23: the other Kato axis has defining function
  `h=π*w-s`, closing factor `a`, and nodal equation `uv=s`.
  Its actual base map `s=uv-h` is different from the normal-line
  model. The repaired collar uses six point blow-ups and 72
  smooth curve blow-ups; the exceptional coefficients
  `(0,2,4,6,8,10,12,10,8,6,4,2)` give the genuine function
  `H=h/q`. Character charts and the uniformly convergent product
  conjugate the closing, so this is a neighbourhood comparison,
  not just a normal-line identity. The local fourfold resolution
  retains `q=s^n` and its multiplicity. The exceptional curves
  meet the persistent axis in the nonextending section `[-s^12]`.
  A proposed proper divisor closure would extend its degree-one
  horizontal intersection and is therefore impossible. The
  separate deformation argument has normal sequence
  `0→O(-1)→N→O²→0`; its section map is an isomorphism, exactly
  when the curve avoids every conductor branch.
* B.4.25–B.4.26: the Hopf bivector automorphy gives dimensions
  one or two, with infinitely many resonances by the explicit
  Rouché estimate. Coherent `R¹` torsion has locally finite
  support, contradicting these accumulating jumps in any proper
  completion. Resolution reduces singular completions to this
  case. The multisection norm formula at an axis has the correct
  integral ghost exponent and sign. Generic local hyperplane
  sections of a two-dimensional origin fibre give a finite
  multisection, forbidden by the nonzero radial ghost class.
* B.4.28: each reduced anticanonical surface contribution is
  nonnegative; zero contributions are classified with the exact
  cited surface hypotheses under separate source review. Normal
  degrees exclude parabolic components. In the elliptic case
  the neck-crossing map factors through the dual graph, so has
  rank at most one. Hyperbolic Inoue links kill both angular
  generators in nearby `H1`; the torus exterior cohomology ring
  makes their two-cycle zero, whereas the extended dualizing
  form has nonzero residue integral on it. The remaining toric
  dual complex is an oriented closed surface with Euler zero.
* B.4.29: the small resolution of two Tate nodes is proper with
  reduced crossing centre and rank-two monodromy. Translation
  by `exp(2πi/t)` has two distinct central limits. Pulling back
  a hypothetical proper meromorphic graph along the zero
  section produces a dominating degree-one curve and forces
  an impossible extension. Relative forms, Gauss–Manin data,
  and the absolute top form remain fixed; the horizontal term
  in an absolute one-form is exactly what those data discard.

The central arguments B.4.9, B.4.18–B.4.19, B.4.24, B.4.27,
and B.4.30–B.4.33 have their more detailed records above. All
programs cited in this group were rerun; the dependency-order
and obsolete-initial-program exceptions below remain explicit.

The original `ab_push_global_meridians_initial.py` fails its obsolete
assertion. The corrected `ab_push_global_meridians.py` and independent
fixed-space computation pass. The failed initial program is retained as a
superseded exploratory calculation and is not a proof dependency.
`ab_push_all_fan_homology.py` initially lacked a generated JSON dependency
because independent jobs were scheduled together. Rerunning after the
dependency was generated passed. Both outputs are retained; this was an
execution-order failure, not a mathematical failure.

## Live outstanding tasks

This audit is not the final paper-completeness certificate. Current work:
remaining cited literature; per-row credit and source-to-print comparisons;
duplicate statement consolidation while preserving all distinct proofs;
notation and cross-paper theorem references; the exact list of unresolved
working-edition items; final PDF typesetting and visual checks.

## Complete outer-end and generalized-family reading, 17 November 2026

Checker for every scope below: GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 17 November 2026. These are actual step-by-step readings and independent derivations, not status inferred from the producer. External-source scopes are separately recorded in references_verified.json; source-to-final comparison remains a separate editorial gate.

- PUSH D.1.1–D.1.3: checked the index-two Albanese period, nome iw/216, exponential cusp growth at every rational boundary angle, and the natural-boundary contradiction. In D.1.2 the coherent direct-image/base-change argument is over a reduced smooth curve after removal of a discrete set; the unique anticanonical section has horizontal divisor 2D. Connectedness of the threefolds is made explicit: otherwise a section can vanish identically on a disconnected component. Properness removes critical images; b1=2 permits the compact-surface Kähler theorem. The application is to the connected constructed family and needs no strengthening.
- D.2.1–D.2.4: rederived h=mu−(1−tau)/2, tau=i−3pi i h²/2, B=−3i h² and D* =−3|h|²; checked the integer counterexample n²gamma−6nw+3ndelta. The Hausdorff reflection uses the exact character annihilator: rational G_a is a circle and irrational G_a a point. The moving deck translation is −a/4. The leaf lattice is a Gaussian index-two lattice homothetic to E_i; no complex compact fibre is inferred from a circle reflection.
- D.3.1–D.3.2: checked bounded dual labels, cancellation of the quadratic terms, the O(h³)/delta error, and realization of each primitive subgroup K and real functional ell by V_n=nv+v0. All stated real dimensions and the two path-dependent limits follow. The limiting objects are explicitly real tori/closed-subgroup quotients.
- D.4.1–D.4.8: checked the local Jordan estimate, the superharmonic Laplacian, closure A(Z⁴+V_k), and the distinction between period-image closure and a chosen Chabauty limit. Recomputed the heat-derivative factor iZ(3ZP−2g2)/(4pi²P). Checked the norm-three distribution relation and N=3^(1/4) at the equianharmonic point; the coarse C1 derivative is nonzero there. D.4.6 is a historical question answered by D.4.7–D.4.8, not a remaining open problem. Read all analytic tail and Cauchy estimates and reran the Arb certificate: 19,701 initial boxes plus 67 refinements give the stated final 19,755 leaves. The proper C1 submersion and complete positive-gradient flow establish the global nested Jordan levels. Literature on fixed-torus critical points is only compared in its exact scope.
- E.1.1–E.1.3: checked the determinant −1 change of marking, positive-loop versus clockwise deck inversions, and the extra N1 coefficient. Necessity uses the intrinsic fibration and the rational centralizer; sufficiency solves the full finite norm equations, cusp cocycle, and H1(V)=0, with all translations retained. The congruences give exactly 2klZ. Parameter-dependent gluing over a Stein disc uses the actual vector-bundle extension and connected translation group.
- E.2.1–E.2.3: checked the weighted root curve P(3k,4l), its torsion-free Picard presentation under gcd(3k,4l)=1, monomial cohomology counts, the extra horizontal monomial precisely when k>1, and the nonzero normal connecting residue. The Kuranishi proof does not infer nonreduced base change from a reduced-base theorem: it writes the complete one-variable local ring C{t}/I and uses the existing nonzero Kodaira–Spencer disc to force I=0. Checked multiplicity invariance, the sign of kl−3k−4l, impossibility of equality, and recovery of the ordered pair from asymptotic pluricanonical dimensions.
- E.3.1–E.3.3: read the full analytic base-change/root-chart/trace argument and the five comparisons with DGKX version 1. The exact scope distinguishes the root tangent computation, Kuranishi map, intrinsic pencil, quadratic cusp closing and full automorphism computation. No generalized theorem is attributed to a source that treats only the standard family.
- E.4.1–E.4.3: checked the independent Arb proof of the sharp maximum, including Cauchy contraction, 438 boundary edges, area 23/40, the local 18.37 and 0.546 estimates, two-zero Rouché count and cusp bound N<1.082. This is an additional proof of the shared maximum theorem, not a new duplicate statement.

## Working-edition analytic proofs compared in full

- analytic_canonical_ring.tex: read every step of CR1–CR5. Evaluation has orders 0 and 2 on the finite covers; the cusp frame is a unit. The exact meromorphic direct-image calculation works for positive and negative integers. The weighted polynomial ring follows degree by degree with every scalar retained. Older numeric pointers must be replaced by internal labels to the corresponding finite-character and Hodge-line calculations.
- period_parameter_deformation.tex: read the complete construction, uniform properness estimates, exact real-linear marked map, Beltrami sign conversion, nonzero invariant Dolbeault class, and the dual-number base-change proof. The three scheme-theoretic critical values are fixed even infinitesimally, so a trivialization of the total space would trivialize a regular torus deformation. The plus-graph Beltrami convention gives the negative of the tangent connecting class; both signs are retained explicitly.
- algebraic_dimension.tex: read the full torus-algebraic-reduction argument, five-function independence by exact cusp and order-four transformations, Appell–Humbert matrix inversion, countability argument, and meromorphic descent. The latter uses connectedness of the smooth locus, the analytic vertical differential equation, and a transverse ramified curve estimate at the finitely many missing base points. Editorial provenance/status prose is not part of the proof and is removed from the mathematical exposition.

## Original sources opened during this reading

- Atiyah–Singer (1968), III: original scanned printed pages 565–566, formula (4.4) and Theorem (4.6), visually opened. The theorem is for a compact complex manifold and a finite automorphism group; B.4.14 applies it to each nontrivial root of unity, then identifies the finite Laurent-polynomial character of C*. No Kähler hypothesis is present. The elliptic contribution and eight node contributions sum to −8 exactly.
- Pinkham (1974): original printed pp.45–46, Remark 7.6(iii), and pp.63–65, Section 9 and Theorem 9.3, opened. The normal cone swept by a hyperplane pencil gives the explicit flat smoothing; the degree-eight quadric component is distinguished from the cubic blowup component. The paper independently constructs the analytic affine smoothing and does not infer globalization merely from the existence of this local cone smoothing.

## Period-shift and Hodge-line full original proofs

Read and rederived all of workbench/period_shift_classification.tex: full centralizer, order-four norm parity, explicit root-disc conjugacies and integral defects, cusp multipliers, zero common-coinvariant obstruction, translation-sheaf H1=0, coherent even-shift action. Neither abstract lattice equality nor local maps alone are used as a global gluing proof.

Read and rederived analytic_picard.tex lines26–254 in full: finite determinant eigencharacters, convergent unit gauge, invariant-module calculation distinguishing pulled-back dt frame from differential, eta section divisor, cusp canonical volume, modular Theta divisor and O(1) Hodge line. Full proof retained in Paper I through maps_audit/paperI_hodge_line.tex; shared with that independent reader.

## Additional complete proof comparisons, 17 November 2026

Checker: GPT-6 Astra (OpenAI, ChatGPT Pro mode), effort Pro, writing run, 17 November 2026.

- PUSH C.3.5: full source and transformed paperI_closing_cocycle.tex read. The raw shift composition has central defect; the quadratic correction cancels it with the stated positive-loop convention. The cusp-origin extension uses the actual three affine gluing equations, not only linear lattice automorphisms. The independent closing-origin rerun agrees. Exact known source matched to DGKX v1 Proposition 7.8 and Appendix C Proposition C.2; whole proof retained in the credited appendix.
- CDP D.1.14: complete four-step kernel proof read. Integral stabilizer equation forces the lower-left vector into 6Z²; the middle-block presentation and mod-12 character are consistent. The U,V,Z commutator basis gives exactly the kernel over I and the generated middle blocks give surjectivity. Full proof printed in I with the single FAM F.1.1 statement.
- CDP E9: complete root-bundle, branch-normal, Beltrami and analytic-local-algebra proof read. The root degrees -1,-2,-5,-6 all have coarse O(-1); the branch-normal K_dP6 yields H²=1. Three distinct fixed critical values eliminate the base infinitesimal transformation. The nonzero Beltrami class makes the classifying map locally invertible and forces the one-variable Kuranishi ideal to vanish. Full proof retained under the shared FAM A.5.2 statement, credited as a re-derivation of DGKX v1 Theorem 6.12 and Proposition 6.16.
- Finite extension transgression: the section carry cocycle, bar coboundary -xi(c), negative-carry generator convention and multiplicative derivation rule checked. Indices and the nonzero order-two class are unaffected by common sign reversal. Full direct derivation inserted after the exact-algebra proof.

## Full construction appendix audit

GPT-6 Astra (OpenAI, ChatGPT Pro mode), effort Pro, 17 November 2026, delegated maps audit: read all 1,581 lines of candidate_geometry.tex, all 587 lines of exact_algebra.tex, and all 760 lines of finite_filling_certificates.tex. Re-derived modular deck normalization, both affine torsors, bounded-chart cusp properness, the full residual overlap group, every finite normalization branch, peripheral kernels and normal characters. No new mathematical gap found. Exact arithmetic reruns and original-source checks have their separate manifests; no inference from the source's verification badges.

## Semidirect-product credit and complete rewording

GPT-6 Astra (OpenAI, ChatGPT Pro mode), effort Pro, 17 November 2026 UTC. Original page visually opened; full lemma and proof read. For a split group extension, the correct abelianization is the direct sum of Q_ab and the Q-coinvariants of K_ab. The WB lemma is a re-derivation of this known formula, not a new result. The complete quotient proof is independently worded in work/root/semidirect_abelianization_rederivation.tex, with the normal subgroup, induced quotient maps and commutator quotient explicitly justified. The original AC26 statement and proof were checked on the rendered page, not only in the searchable transcription. A prose-only 14-word overlap scan of the current I manuscript against the AC26 transcription found no long identical prose run; this is a locator aid, not a mathematical or originality certificate.

## Editorial report-path repair, 17 November 2026

A reused Python loop variable sent several report refreshes to the newest saved stdout-log path. The affected report versions are preserved under records/misdirected_report_*.md and identified in records/report_path_repair.json. The variable is now report_path; the actual report is refreshed at its required filename. No mathematical source or PDF was changed. The current real engine log is preserved, and build 18 supplies a fresh authentic final log. Misdirected files do not support a typesetting claim.

## Typed reference and dependency-line review, 17 November 2026

Visual review found that shared LaTeX theorem counters made cleveref call lemmas and propositions theorems. Standard alias counters now preserve the common numerical order while retaining each environment type. Every formal statement receives a Uses line exposing the references already in its own statement and retained proof; this extraction is an index, not a correctness inference. The result concordance prints its complete positive-credit field without the former display truncation. No statement or proof was shortened.

## Program-command spacing repair, 17 November 2026

The rendered program table showed that url-package path text suppresses literal spaces. The command manifest itself was correct. The printed commands now use shell-quoted argument arrays and explicit intertoken spaces outside path spans. The same spacing fix keeps source identifiers legible in the result concordance. All published commands retain their exact working directories and arguments; no computation changed.

## Paper II: the twelve reserved compact occurrence proofs

GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro, 17 November 2026. Every source block was read in full, including its specified input files. Detailed independent steps, exact hashes and source scopes are in `cdp_reserved_full_checks.json`; four original programs reproduced their retained outputs byte-for-byte. Their finite checks are not substituted for geometric proofs.

### CDP C.2.UN.18

Full signed-root construction rederived, including both finite free quotient charts, the torsion-line product cover and its two nonzero Jacobians, exact canonical divisor and floor direct image, meridians m delta+ + h and m delta- - h, primitive Mayer–Vietoris maps, integral support groups, deck-cocycle R1 trivialization, plurigenus persistence and actual compact gluing. The comparison is Fujimoto Example3.4(1), opened separately by the CDP reader, not a new claim of the existence of a Kodaira-dimension-one component.

### CDP C.2.UN.21

Full half-period involution and its freeness checked on every fixed base point; exact full fibres 2P+2Q and2B retained. Recomputed circle-bundle/Gysin ranks, integral plus/minus eigenlattices, Wang torsion, invariant bounding chain for the attaching torus, and both coherent invariant maps. Checked the nilpotent t modulo t² eigenspaces: each sign contributes one invariant, so full-fibre h(O)=(1,2,1) although the reduced support has(1,1,0). Quadratic normalization recovers the primary cover with no claim that secondary type persists.

### CDP C.2.UN.25

Full compact Weierstrass base, signed root charts, Klein-four product cover, free eta and eta-k actions, sixteen k fixed points, eight A1 surface singularities, actual ambient resolution charts and coefficients 2M+2A+4Q1+4Q2+sum E_i rederived. Read enriques_support.inc.tex in full: two affine-D4 blocks, sole fibre relation, incidence ranks7,8, curve-class rank14, absence of higher targets, coherent restriction isomorphisms, and six disjoint negative-two operations. Both original exact programs were rerun unchanged and reproduced original outputs byte-for-byte.

### CDP C.2.UN.27

Full all-r construction and elliptic_root_support.inc.tex read. Rechecked the parity sign(-1)^r in the lifted involution, total sixteen fixed points, eight A1 quotients, exact invariant form divisor sum J_j minus F_infinity and P_m=max(0,1-m+r floor(m/2)). Recomputed projective cohomology and symbolic incidence kernels for every r; finite reruns r=2,3,4 are explicitly only checks of those cases. The all-r proof uses the displayed kernel equations and constant rank14, not extrapolation from runs.

### CDP C.2.UN.30

Full torsion-point signed-root construction read and rederived. Checked the etale product cover, sixteen fixed points on the component and thirty-two ambient fixed points, quotient chart T=R u², exact canonical divisor sum J_j, plurigenera1+r floor(m/2), and projectivity/Noether calculation giving chi(O)=2. Verified the star curve-class map has rank17 for every r and recomputed both support cohomology rows, with twenty balancing blocks disjoint from the elliptic/K3 components.

### CDP C.2.UN.34

Full actual root-orbicurve torsor reconstruction read. Recomputed the averaging coordinate change making finite translations constant. Checked exactness and connected additive kernel of(C*)²→A, vanishing H² of the additive sheaf on the root curve, lifting the complete analytic torsor class to two line bundles, divisor representatives retaining degree-zero classes, actual exceptional restriction maps, faithful root translations, compactness/properness and punctured product trivialization. The selected surface is unchanged, including individual translations; genus≤1 is used only in the compact auxiliary base construction.

### CDP C.2.UN.35

Full equivariant construction and equivariant_torus_h1.inc.tex read and rederived. Checked the complexified lattice exact sequence, inverse character on the additive kernel, coherent H² on the quotient orbicurve, algebraic generic torsor and invariant meromorphic frame. Reproved curve-field C1 by Riemann–Roch and the homogeneous ideal height bound, norm surjectivity, every cyclic lattice d=1,2,3,4,6, the explicit transfer formula and coprime2/3 argument. Matched Steinberg Theorem1.9 exactly to perfect characteristic-zero curve fields and connected algebraic tori. Checked vertical extension at a node, root inertia order, actual equivariant restriction, finite quotient/resolution, balancing, and the intrinsic fibration argument needed for exhaustion. Original lattice certificate rerun matches its output.

### CDP C.2.UN.37

Full proof for every algebraic-dimension-one primary or secondary Hopf surface read. Rechecked holomorphicity of the meromorphic reduction from zero intersection and positivity; adjunction plus absence of rational curves makes every irreducible curve smooth elliptic. Normalized multiple-fibre cover is etale and connected, all finite deck maps are translations, integral monodromy is identity, and the holomorphic j-function is constant on P1. The exact surface and torsor satisfy the already fully checked UN34 hypotheses.

### CDP C.2.UN.41

All698 source lines read, including proper two-axis plumbing with closed overlap graphs and compact neck/core cover, real independence of the four periods, degree-one height-circle comparison, varying multipliers, cubic-pencil compact suspension, minimal graph translation extension, convergent Tate coefficient/coordinate comparison, and both integral/coherent restriction matrices. Matched Schuett–Shioda v3 section7.6 pp33–34. Added an explicit in-paper use of UN40 plus the generic-level-divisor argument to prove a(H)=0 for multiplicatively independent multipliers.

### CDP C.2.UN.42

Full weighted-blowup construction rederived: smooth nonzero tautological line, exact nonlinear Hopf contraction after rescaling, uniform polynomial bound on lifted translations, exponential norm domination for every|beta|<1, proper discontinuity/freeness and compact fundamental annulus. Checked the commuting half-translation quotient, full SNC fibre and other double torus quotients, exact canonical evaluation order, single-multiple Seifert model, pair-preserving circle isotopy, primitive restriction maps and coherent deck-cocycle surjectivity.

### CDP C.2.UN.43

Full secondary Hopf proof read. Checked normal-core contraction centrality via log determinant character, finite-cover meromorphic fields, nonresonant and nonlinear centralizers including r=1, abelian deck splitting and coprime finite weights. The exact normal forms were opened by the independent CDP reader in Khaled Theorem2.1 and Kato pp230–232; no unrestricted diagonal-centralizer claim is imported. Rechecked the selected exact-torsion base-cover sheet is unramified at the node, global section translation, equivariant plumbing on every neck, freeness, resolution away from the prescribed tube, and nonlinear scalar action. The base-curve scope is retained; no unwarranted rational-base conclusion.

### CDP C.2.UN.45

Full all-curve occurrence proof read. Verified primitive-element plane normalization, adjunction decrease of arithmetic genus guaranteeing termination of singular-point blowups, generic multiplicity one of the actual normal-bundle exceptional divisor, and balancing away from that component. Rechecked the integral projective-bundle map with lines convention xi²+c1(N)xi=0 and the coherent Leray maps. Original program rerun checks50 explicit branch/genus cases; the all-genus argument remains the exact subtraction and adjunction proof, while arbitrary curves use their given plane normalization.


## Paper II full replacement comparison and source closeout

GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 17 November 2026: independently read the complete C2c analytic toric degeneration and E6 relative nonreduced Douady replacements, rederived the compact representative/properness bounds and the Artin lifting plus finite-complex unit argument, and matched their printed transformations. UN41 now includes the explicit two-curves/generic-level-divisor proof of algebraic dimension zero. INV E2.3 is corrected: E15 settles the Kuranishi ideal, while the K_m splitting remains separate. The full INV E2.2 tangent calculation is retained as a distinct proof of the single E15 tuple; its canonical, direct-image and Hodge statements remain. The original publisher preview BHPV VI pp243–244 and original AC26 PDF p30 were opened and hypotheses matched at the exact scopes recorded in references_verified.json.

## Paper II comb partial analysis

GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 17 November2026: root independently re-derived the entire added partial proof in editorial/II_comb_remaining_analysis.tex. Exact coarse splittings have total degree2m-1; the injective coarse Hom comparison, local eigenspace condition and line-bundle section count give h0(Km)<=2m+2. Substituting into the checked Hodge formulas gives the stated two intervals. The two homogeneous-coordinate surjections are everywhere onto and their kernel splittings and h0 values0,2 follow directly. Neither map is claimed to arise from an actual comb. The unchanged d_comb.py was read in full and rerun for12,13,20,100; all exact symbolic checks passed. The Kuranishi clause is resolved by the independent CDP E15 proof, not by the script.

Checked complete partial proof and exact numerical rerun; the actual comb kernel splitting remains open because the admissible period section, transition functions and derivative are not determined by the numerical data. Smooth reduced Kuranishi germ established at CDP E15; no claim of geometric nonuniqueness from abstract bundle maps.

Replaced stale Kuranishi-open wording with E15 and added the complete checked Km bounds and explicit algebraic examples. Distinguish V tensor G from V-dual tensor G; invariant classes alone do not identify the Hom bundle. Exact remaining gap and attempted approaches are in work/cdp_audit/comb_Km_attempts.md.
