INCOMPLETE

# S6_09_PAPERS — writing, proof comparisons and discrepancy record

The writing began on 16 November 2026 at 23:47 UTC. The principal task is the three complete papers. The required sequence is inventory, Paper I with all checks and PDF inspection, Paper II, Paper III, and a final common-reference check. Parallel readers may check later material while the preceding paper is being completed; this does not constitute assembly of a later paper.

## Completeness and current state

The fixed inventory contains all 745 run rows and 183 additional working-edition/course rows, 928 in total, in the required 17 columns. The run counts are INV 47, FAM 55, PUSH 154, CDP 239, MAPS 198, and ARI Part C 52. Producing-run badges are provenance, not independent verification. A historical recorded check counts at its stated scope; a title comparison, a statement reading, a full proof reading, an original-source hypothesis match and a computational rerun remain different events.

| Paper | Assigned rows | Validation state |
|---|---:|---|
| I | 338 | Writing/checking in progress |
| II | 313 | Not assembled; the required sequence is being observed |
| III | 277 | Not assembled; the required sequence is being observed |

Each printed result has its complete proof in the main text or a linked appendix. Shared statements retain every distinct proof. The result index is a concordance; neither it nor a repository pointer replaces a proof. Programs are named, their commands and outputs are retained, and the mathematical argument specifies what their results establish. A failed argument remains visible with its correction or with its precise gap.

## Models, dates and methodology

The working edition was AI-produced by GPT-5.6 Sol (OpenAI), Codex reasoning effort ultra, 24 August–9 September 2026, with a few inputs by GPT-5.6 Sol (OpenAI), ChatGPT Pro mode, 24 August–9 September 2026. The six research runs were AI-produced by GPT-6 Astra (OpenAI), ChatGPT Pro mode, 12–16 November 2026. The current writing and independent readings are by GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro, 17 November 2026. The historical readings were by Claude Fable 5.2 (Anthropic), effort high and effort max, and Claude Opus 5.5 (Anthropic), effort max, 12–16 November 2026, at the dates and scopes retained per event. Where a report header differs from the registry, the report header controls.

The attached course is an additional provenance stratum: its course.json and provenance.json name GPT-6 Astra (OpenAI), Codex reasoning effort ultra, 9 October 2026; individual companion chapters also carry 8 or 10 October dates. Retained prerequisite providers have their own source provenance. These are not silently attributed to the August–September working edition. The final chapter-specific record controls the provenance of each retained course argument.

No human has checked the mathematics. No person is named as an author of or contributor to this work. The work is AI-produced, and the text is dedicated under CC0 1.0. Other authors receive credit only for their own results and sources.

The requested wording identifying ChatGPT Pro mode with one universal highest effort setting is not supported by the official documentation opened in this writing. That documentation distinguishes reasoning mode from reasoning effort. The papers therefore retain the recorded Pro-mode designation, explain the distinction, and do not assert the unsupported equivalence. Anthropic's opened official effort documentation identifies max as its maximum capability setting. The exact sources and opened scopes are retained below and in the bibliography.

## Credit and allowed date statements

The original AC26 PDF controls every difference with the searchable transcription. The standard mod-2Z classification is attributed to DGKX version 1, Theorem 1.4; that version is dated 23 September 2026, version 2 omits the result, and the complete public working-edition proof was present by 8 September 2026. These are the only comparative date statements about results. The standard tangent dimensions, Kuranishi germ and full automorphism group are expressly re-derived after reading DGKX version 1. AC26 receives credit for the contradiction to CDP20, Corollary 2.3. Source searches record found loci or the actual searched scope; a failure to find a matching statement is not an exhaustive literature-absence claim.

## Principal corrections and distinctions

1. The invariant source's reversed-meridian matrix is Q=P_mark S. It is not interchangeable with the required FAMILY matrix. Positive base loops, clockwise analytic root decks, affine twist vectors and collar integration orientations are transported explicitly.
2. The order-four Albanese lattice contains the factor 1/2. Its nome is iw/216; the order-three nome is −w²/48³, and their relation is q1=(27/64)q2². The Engel reference lift is fixed at c=0, so its parameter is w² with that specific linearization.
3. The degree-one cusp-torsion assertion is false in AC26's original PDF, Remark 9.21 on page 81. It is not merely a transcription error. The full local module calculation proves that degree-one torsion is supported on the two multiple fibres, while degree-two cusp torsion remains. Remark 1.3 must be qualified by degree.
4. The historical FAMILY questions C.3.3 and E.1.5 retain their entire local arguments, but their printed headings and inventory kinds identify the subsequent complete boundary and virtual-Euler exclusions. They are not counted among the outstanding questions.
5. The strongest filling obstruction uses the actual affine origins. The former reading's unverified origin-comparison step has been derived from the marked cusp gluing, with the radial gamma defect and all finite twists retained. A linear lattice comparison alone is not treated as that proof.
6. The obsolete global-meridians program failed. Its corrected successor and the independent quotient fixed-space computation passed. Both outputs remain. The all-fan homology program required a dependency-ordered rerun; its initial failure and successful rerun remain.
7. The normalized norm and the Betti measure require the stated orientation and factor 12. The Cayley coordinate is k_chi with z=k_chi²; untransported occurrences of the old local variable were corrected without changing the formulas.
8. The two source entries named Brunella1999 are different works. The forms paper has been given the separate key Brunella1999Forms; the original forms PDF identifies Marco Brunella, overriding an erroneous author field on the publisher HTML. Metadata checking does not by itself verify its use in a proof.
9. The analytic base-change checks retain their precise domains. Reduced-base Bănică–Stănăşilă statements are not silently used for nonreduced Kuranishi bases. The local one-variable Kuranishi algebra and the nonzero actual-family map provide the required argument.
10. The provisional MAPS fourfold torsion differential has a complete Fox/Wang calculation in the audit supplement. The finite Smith computations alone would not identify the geometric differential. The earlier factor-four shortcut is not retained as a proof.

## Format decisions

The full binding post format, its template and its worked example were opened. LuaLaTeX replaces the format template's pdfLaTeX because the task explicitly requires LuaLaTeX. Every paper is one self-contained TeX source with an inline bibliography. Long result, notation, verification and program tables belong in appendices. Proofs keep their checked local subdivision when forcibly rewriting every paragraph into a new step numbering would obscure the exact source comparison; the complete reasoning is retained. Source numbers are mapped to actual printed numbers in the full concordance. Typed status is carried by the statement, its caption or explicit credit, and the separate final part. The front matter is kept near the requested three-page scale and is visually checked. No mathematical argument is shortened to meet a page target.

## Typesetting: before and after

The per-build table below records every saved Paper I build. Failed or intermediate runs are not delivery passes. One distinct long inline exterior-power basis caused the 6.88432pt overflow; it was repaired with explicit mathematical break opportunities. The final validation file records the current pages corresponding to that location and every page inspected as an image.

| Build | Completed PDF in log | Overfull boxes | Boxes exceeding 2pt | Maximum excess (pt) |
|---|---|---:|---:|---:|
| S6_09_PAPERS_I_build_02.stdout | No completed PDF recorded | 0 | 0 | 0.00000 |
| S6_09_PAPERS_I_build_03.stdout | No completed PDF recorded | 1 | 1 | 6.88432 |
| S6_09_PAPERS_I_build_04.stdout | 353 pages | 1 | 1 | 6.88432 |
| S6_09_PAPERS_I_build_05.stdout | No completed PDF recorded | 0 | 0 | 0.00000 |
| S6_09_PAPERS_I_build_06.stdout | No completed PDF recorded | 0 | 0 | 0.00000 |
| S6_09_PAPERS_I_build_07.stdout | 378 pages | 1 | 1 | 6.88432 |
| S6_09_PAPERS_I_build_08.stdout | No completed PDF recorded | 1 | 1 | 6.88432 |
| S6_09_PAPERS_I_build_09.stdout | No completed PDF recorded | 1 | 1 | 6.88432 |
| S6_09_PAPERS_I_build_10.stdout | 410 pages | 1 | 1 | 6.88432 |
| S6_09_PAPERS_I_build_11.stdout | 447 pages | 0 | 0 | 0.00000 |
| S6_09_PAPERS_I_build_12.stdout | 461 pages | 0 | 0 | 0.00000 |
| S6_09_PAPERS_I_build_13.stdout | No completed PDF recorded | 0 | 0 | 0.00000 |

## Full root proof and source-comparison record

# Root mathematical audit — live record

Reader: GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 17 November 2026.
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

Reader throughout this section: GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro),
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

Checker: GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), effort Pro, writing run, 17 November 2026.

- PUSH C.3.5: full source and transformed paperI_closing_cocycle.tex read. The raw shift composition has central defect; the quadratic correction cancels it with the stated positive-loop convention. The cusp-origin extension uses the actual three affine gluing equations, not only linear lattice automorphisms. The independent closing-origin rerun agrees. Exact known source matched to DGKX v1 Proposition 7.8 and Appendix C Proposition C.2; whole proof retained in the credited appendix.
- CDP D.1.14: complete four-step kernel proof read. Integral stabilizer equation forces the lower-left vector into 6Z²; the middle-block presentation and mod-12 character are consistent. The U,V,Z commutator basis gives exactly the kernel over I and the generated middle blocks give surjectivity. Full proof printed in I with the single FAM F.1.1 statement.
- CDP E9: complete root-bundle, branch-normal, Beltrami and analytic-local-algebra proof read. The root degrees -1,-2,-5,-6 all have coarse O(-1); the branch-normal K_dP6 yields H²=1. Three distinct fixed critical values eliminate the base infinitesimal transformation. The nonzero Beltrami class makes the classifying map locally invertible and forces the one-variable Kuranishi ideal to vanish. Full proof retained under the shared FAM A.5.2 statement, credited as a re-derivation of DGKX v1 Theorem 6.12 and Proposition 6.16.
- Finite extension transgression: the section carry cocycle, bar coboundary -xi(c), negative-carry generator convention and multiplicative derivation rule checked. Indices and the nonzero order-two class are unaffected by common sign reversal. Full direct derivation inserted after the exact-algebra proof.

## Full construction appendix audit

GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), effort Pro, 17 November 2026, delegated maps audit: read all 1,581 lines of candidate_geometry.tex, all 587 lines of exact_algebra.tex, and all 760 lines of finite_filling_certificates.tex. Re-derived modular deck normalization, both affine torsors, bounded-chart cusp properness, the full residual overlap group, every finite normalization branch, peripheral kernels and normal characters. No new mathematical gap found. Exact arithmetic reruns and original-source checks have their separate manifests; no inference from the source's verification badges.

## Semidirect-product credit and complete rewording

GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), effort Pro, 17 November 2026 UTC. Original page visually opened; full lemma and proof read. For a split group extension, the correct abelianization is the direct sum of Q_ab and the Q-coinvariants of K_ab. The WB lemma is a re-derivation of this known formula, not a new result. The complete quotient proof is independently worded in work/root/semidirect_abelianization_rederivation.tex, with the normal subgroup, induced quotient maps and commutator quotient explicitly justified. The original AC26 statement and proof were checked on the rendered page, not only in the searchable transcription. A prose-only 14-word overlap scan of the current I manuscript against the AC26 transcription found no long identical prose run; this is a locator aid, not a mathematical or originality certificate.


## Invariant and arithmetic corrections

Source record: `work/invariants_arithmetic/corrections.json`.

```json
[
  {
    "id": "INV B1.0",
    "change": "Translate the reversed-meridian source dictionary Q to the required P_mark convention, display Q=P_mark S explicitly, and fix the transported reference lambda_0=1. Retain the full theta-quotient proof.",
    "reason": "Source and required family meridian conventions differ; Q and P_mark are not interchangeable."
  },
  {
    "id": "INV D1.3; D2.1; D3.1",
    "change": "Credit DGKX v1 theorems as re-derived; remove source wording treating their theorem status as merely asserted/superseded.",
    "reason": "User credit requirement and the v1 theorem statements."
  },
  {
    "id": "ARI C.1.2",
    "change": "Replace the y=T pole assertion by a half-period zero and g3=0 contradiction.",
    "reason": "At tau=1/2+iT, mu=1/2-iT is congruent to 1/2 modulo the lattice, not to zero."
  },
  {
    "id": "ARI C.8.12-C.8.15",
    "change": "Rename the Cayley coordinate w to chi and the scalar cusp beta to beta_cusp.",
    "reason": "Avoid conflict with the global parameter w=exp(-pi i c) and the period beta."
  },
  {
    "id": "ARI C.8.14",
    "change": "Complete the w-to-chi coordinate rename in the two products kw^2: z=v^2=k chi^2 and D(k chi^2).",
    "reason": "The initial token substitution missed w when preceded by k; these are the same Cayley coordinate, never the family parameter w."
  }
]
```

## CDP technical corrections

Source record: `work/cdp_audit/TECHNICAL_CORRECTIONS.md`.

# Technical corrections and distinctions to preserve

Checker: GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), writing run, 17 November 2026 (Europe/Berlin). This note records specific findings, not a blanket verification of the CDP return. Exact per-result scopes and remaining dependencies are in `result_audit.json`; exact opened source locators and fingerprints are in `references_verified.json`.

## A.2.6: the normalized differential module

The sentence identifying the raw differential image is false as written. Its exact replacement is:

> The B-module generated by the differential image, where B=C{t}, is t^4 B dt.

For R=C{t^5,t^6,t^7}, the actual R-module image is R⟨t^4,t^5,t^6⟩dt. Its valuation set omits 7 and 8, so it is not t^4B dt. After extension to B and quotient by torsion, the generated module is t^4B dt. The following determinant computation is normalized and therefore still gives 19−4=15. The primeness, critical-locus, transverse-cusp and symbolic-square counterexample proofs all survive this correction. The exact polynomial/semigroup program has been rerun successfully. The full corrected statement and proof are retained in `corrected_A1_1_A2_6_full_proofs.tex`.

## A.1.1: replace the undefined lead reference

Replace “the two vanishings in Lead 1” by the two explicit assumptions H^0(S,N^*⊗A)=0 and H^0(S,Q⊗A)=0. They are precisely the hypotheses needed in the two long exact sequences to identify H^0(S,V⊗A) with ker δ_A. The corrected full block preserves labels A:filtration1 and A:filtration2. Its pre-statement definitions of N^*, V, T, Q and A must accompany it.

## D.1.14: placement and duplicate-method credit

The SL₂(ℤ) group calculation belongs with Paper I's monodromy. Its kernel method agrees with FAM F1.1; it is not a mathematically independent method and should not be identified with FAM F1.2. The full proof is in `paperI_CDP_D1_14_group_proof.tex`. Preserve the exact source concordance while using one coherent exposition.

## INV E2.3: distinguish the resolved question from the remaining one

The working-era open question about the comb Kuranishi germ is resolved by the later CDP E15 proof, which gives the exact tangent dimension and smoothness. Its record must retain the historical open status and add the later resolution. The question about the splitting type of K_m is a different question and remains open; it must not be silently marked resolved by the Kuranishi calculation. Viaclovsky's supplied October 2026 source establishes the previous 8m−8 family lower bound, not the later exact 8m+1 smooth miniversal germ.

## Scope of the CDP corrections

A.4.2 disproves the genus-at-least-two inference used in the printed proof of CDP2020 Proposition 7.3: the normalized twist family may be constant and trivial. It does not by itself refute that proposition. B1 and the correction-note nodal example disprove the omitted-torsion endpoint implication; a local example alone is not a theorem-level global counterexample. Keep these logically separate from D.2.7's actual compact construction and its independently recomputed integral Mayer–Vietoris calculation.

## Fujimoto1988: exact false statement and retained earlier credit

The original definition on pp.91–92 permits proper holomorphic elliptic fibre spaces with smooth source and base and connected fibres; it does not assume a Kähler source or projectivity. Theorem 2.8 and Corollary 2.10, pp.96–97, were opened together with the full proof. For m>1 and 0<|q|<1, the smooth compact Hopf threefold

H_m=(ℂ³\{0})/⟨(a,b,c)↦(qa,q^m b,q^m c)⟩

maps to ℙ² by [a:b:c]↦[a^m:b:c]. It has connected generic elliptic fibre ℂ*/q^ℤ and a multiplicity-m fibre over the line {a^m=0}, whose self-intersection is one. The complement of that line is ℂ². Thus both the asserted cyclic quotient of the complement's fundamental group and the divisibility m|C² fail. The source's normalization of ξ^m=s_D^m splits into m graphs; its asserted connected degree-m Stein cover does not follow. This is an exact counterexample to the printed theorem and corollary, not a judgment about the rest of the paper.

Fujimoto's Example 3.4(1), p.99, already contains a Kodaira-dimension-one component in an abelian-surface degeneration. That prior construction credit must remain even when explaining the defect in Theorem 2.8. The original pages were opened through web retrieval; a failed direct download is not described as a retained PDF.

## Analytic source hypotheses

Grauert1960 §6 Hauptsatz IIa, p.59, was read in the original scan, including its complete proof. It is the proper analytic formal-functions theorem for a coherent sheaf and does not require projectivity or reducedness. It therefore supplies the exact formal-functions input used in PUSH B4.11. The 1963 correction retracts a closedness assertion about the §7 base-change failure locus; it does not invalidate IIa. For cohomology jumping loci and constant-zero top-cohomology base change, use the independently opened Bănică–Stănăşilă finite-complex and cohomological-flatness results, with the reduced-base hypothesis stated when the converse requires it.

Kulikov's 1981 §7 explicitly says that the relevant selector uses only ruled current maximal components. Its §8 removes the earlier distinguished-component and H^1(dual complex)=0 steps. The 1977 local contraction, sigma-atlas, fibre cleanup and reverse-order overlap restoration were checked in the original, then matched to these 1981 alterations. Consequently UN77/81/84 may use the local algorithm under their displayed hypotheses without claiming that the entire 1977 projective theorem holds in that setting. Diagnostic resolution components must not be counted as retained global modification stages.

Nakano1970 alone is not the final sufficient blowdown theorem: its stated extra condition is removed, and its cohomological proof repaired, by Fujiki–Nakano1971. The actual ordinary blowdown input in UN64 is the corrected theorem with a holomorphic projective-space-bundle exceptional divisor and normal O(−1) on its fibres.

Gross–Siebert2006I classifies the relevant central algebraic log spaces. UN71 must retain its explicit analytic-to-algebraic conductor comparison and its independent construction of an actual proper smoothing; a classification of central log spaces is not a uniqueness theorem for analytic smoothing germs.

## Distinct no-horizontal-divisor results

CDP E1 assumes H²(Y,ℝ)=0 and a Kähler general fibre for an arbitrary compact total space. PUSH E2.9 assumes a complex structure on S⁶ and irreducibility of every reduced fibre, and can have non-Kähler fibres. Its argument uses opposite Picard twists and χ(T)=1. They are not duplicate statements. Both proofs and both hypothesis sets should remain available in Paper II, with cross-references where the arguments overlap.

## Verification boundaries

The finite programs check their displayed identities, lattice matrices, transition formulas or bounded graph cases. They do not certify all analytic arguments. The parent-alignment graph program uses a fixed random seed and is not exhaustive. Each execution manifest records the exact copied program, original path, hash, exit status and output. A per-row “proof followed” record still lists any unexamined classification source or upstream proof. Full extracted blocks occasionally include the next statement's preparatory text, and pre-statement definitions must be recovered from the canonical source when drafting.


## MAPS proof and dependency record

Source record: `work/maps_audit/audit_notes.md`.

# Paper III audit record

Reader: GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 17 November 2026. This is an audit-in-progress record, not a certification that all 198 MAPS results are checked.

## Scope and source graph

The final MAPS register has 198 rows (184 labelled Proved, 7 Known, 6 Refuted, 1 Open). `source_order.json` records the 69 actually included TeX files, totaling 1,348,597 bytes. `maps_A.tex` and `maps_B.tex` are the active split source; `maps.tex` duplicates their combined contents and must not be printed additionally. `source_blocks.json` extracts the located full statement-and-proof blocks for subsequent collation; extraction alone is not a proof check. The aliases K1, K8, K11, K15 and references to Leads are imported prompt conventions, not independently defined in the MAPS paper. They must be replaced by explicit definitions and companion theorem locators in the final paper.

## Recorded outside checks retained

`reviews/S6_FINAL_INTAKE_20261116/INTAKE_FINAL.md`, introduction and §3, records Claude Fable 5.2 (Anthropic) at effort high, 16 November 2026, full readings of F.2.5, the first half of F.2.6, F.3.4–F.3.6, F.4.1 and A.3.1; the statement and setup of A.3.2 were read. The statements, but not full proofs, of B.6.16–B.6.22 were read. The tuple F.2.5 and exterior-square identity F.11 were independently recomputed. F.2.6's torsion differentials, the Kuhn cusp filling, and the Nagy and Jin source matches were expressly not verified by that reader. That is a scoped prior check, not a blanket unchecked label.

## New source openings and computations

The publisher full text of Csaba Nagy's *Extended surgery theory for simply-connected 4k-manifolds*, Compositio Mathematica 162 (2026), was retrieved. Theorem 1.4 exactly supplies the inertia criterion used in F.4.1: for a closed 3-connected eight-manifold inertia is trivial precisely when p1 is divisible by eight. Since Theta8 is Z/2, otherwise the inertia group is all of Theta8. The record's claim that this reference could not be opened is superseded for this writing. The application remains dependent on the manifold's verified connectivity and Pontryagin class. The HTML source and extraction are in `sources/external/maps_audit/`, outside the deliverables; provenance and SHA-256 are in `external_provenance.json`.

Huize Jin's arXiv:2608.26698v2 PDF was retrieved from arXiv. Proposition 3.1 gives the bordism invariant (-p1*x+4*x^3)/24. Lemma 4.8 and Theorem 4.9 give cube values 1,8 on the primitive and double-sphere Dehn twists, and the rank-two integral Torelli classification of S2 x S3. These are the actual source statements required by MAPS B.6.18. A full geometric match of the actual return to those invariants is still in progress.

Alarcón and Forstnerič's *Oka-1 manifolds* (2025), Definitions 2.1, 7.7, 7.11, the observation preceding Proposition 7.13, and Proposition 7.13(d), were opened and matched to MAPS F.3.8–F.3.9. The proof correctly uses an LSAP fibre-bundle section theorem, not the unanswered assertion that every Oka-1 fibre bundle is Oka-1. The explicit spanning tube is valid: its nine real integer directions are a complex basis; all lines lie uniformly inside det(Im Z)>0; least singular value is at least 1/sqrt(3), and radius 1/4 suffices. The supplied exact verifier was rerun and passed. F.3.11 imposes bounded correction at one retained cusp while other finite points remain punctures; it must not be strengthened to simultaneous good reduction at every puncture.

`fourfolds_nonselfdual.py`, `fourfolds_oka_tubes.py`, and `fourfolds_periods.py` were copied unchanged to `code/maps_audit/` and rerun under the supplied primary Python runtime. Outputs are saved beside them. The exact matrix, Smith, finite covering-index, genus-two discriminant, exterior-square quotient, and all four nonzero Z/2 torsion-residue assertions pass. The output itself states that H2=H3=0 requires the geometric identification of d2; a successful arithmetic run is not treated as a substitute for that identification.

## Proof readings performed so far

MAPS A.1.1–A.2.2 and B.1.1–B.3.3 have been read step by step. The algebraic and homotopy arguments are internally consistent. External source matches for stable homotopy and APS remain to be completed. B.1.1's use of doubling the stable comparison removes its mod-two pi1 obstruction, and the remaining H3 class restricts trivially because the monodromy-invariant vector d lies in ker(gamma). This is sufficient to identify the framed regular inverse image with the Lie-framed T3. A.2.1 requires the specified solid-torus image condition; A.2.2 is the counterexample if that condition is removed.

MAPS A.3.1–A.3.4 have been read in full. Their explicit real-locus calculations refine Paper I's real structures and should be located there, except A.3.4's quotient-map restriction, which is naturally in Paper III and cross-references the real-locus theorem. The matrix/finite coset computations remain to be rerun; the topological argument recognizes negative-imaginary-w fixed loci by a semifree circle action and positive-imaginary-w fixed loci by determinant-one solid-torus meridians. They do not classify the embedding S3 into S6.

MAPS F.2.5–F.2.6, F.3.5–F.3.11 and F.4.1 have been read in full. The explicit F.3.5–F.3.7 construction uses the primitive exterior square of a genus-two variation and a nonsplit trivial-line extension, not a polarized three-torus family. The H1(P*) vanishing follows from root-line coarse degrees 0,-1,-1. The constant imaginary shift makes the real obstruction function nonzero everywhere because it has one sign near the cusp and is bounded away from that end. The proof does not use an unjustified Oka compactification statement.

## Working edition coverage

The sphere-carrier sources explicitly remain in scope despite their exclusion from the earlier prompts. Their actual files include `workbench/cusp_cone_sphere_routes.tex`, `cusp_sphere_route_strengthening.tex`, and `cusp_s12_carrier_homotopy.tex`; the full higher-rung file also contains unrelated quaternionic/octonionic material that must not be included merely because it shares a file. The classical Theta6 proof is in `codex_workspace/courses/CG-S6/src/sphere-twists-and-the-original-smooth-six-sphere-comparison.md` and relies on the accompanying handle and framed-bordism chapters. The survey's G2-8 almost-complex homotopy claim is a section-homotopy assertion, not a literal trivialization of the twistor bundle; the correct obstruction argument uses connected fibre CP3 and pi6(CP3)=0 over S6.


## Bibliography collision resolutions

Source record: `records/bibliography_collision_resolutions.json`.

```json
[
  {
    "key": "E26",
    "retained": "sources/returns/S6_02_FAMILY/S6_02_FAMILY_references.bib",
    "other": "sources/returns/S6_02_PUSH/S6_02_PUSH_references.bib",
    "other_title": "Complex structures on {$S^6$}",
    "resolution": "Retain the reference from the earlier source in merge order: the alternative is a capitalization/TeX-protection variant of the same work; checked against the source-verification record."
  },
  {
    "key": "EichlerZagier1982",
    "retained": "sources/returns/S6_01_INVARIANTS/S6_01_INVARIANTS_references.bib",
    "other": "sources/returns/S6_05_ARITHMETIC/S6_05_ARITHMETIC_references.bib",
    "other_title": "On the zeros of the {Weierstrass} $\\wp$-function",
    "resolution": "Retain the reference from the earlier source in merge order: the alternative is a capitalization/TeX-protection variant of the same work; checked against the source-verification record."
  },
  {
    "key": "DukeImamoglu2008",
    "retained": "sources/returns/S6_01_INVARIANTS/S6_01_INVARIANTS_references.bib",
    "other": "sources/returns/S6_05_ARITHMETIC/S6_05_ARITHMETIC_references.bib",
    "other_title": "The zeros of the {Weierstrass} $\\wp$-function and hypergeometric series",
    "resolution": "Retain the reference from the earlier source in merge order: the alternative is a capitalization/TeX-protection variant of the same work; checked against the source-verification record."
  },
  {
    "key": "Buchdahl1999",
    "retained": "sources/returns/S6_02_PUSH/S6_02_PUSH_references.bib",
    "other": "sources/returns/S6_03_CDP/S6_03_CDP_references.bib",
    "other_title": "On compact {K}\\\"ahler surfaces",
    "resolution": "Retain the reference from the earlier source in merge order: the alternative is a capitalization/TeX-protection variant of the same work; checked against the source-verification record."
  },
  {
    "key": "AC26",
    "retained": "sources/returns/S6_02_FAMILY/S6_02_FAMILY_references.bib",
    "other": "sources/returns/S6_03_CDP/S6_03_CDP_references.bib",
    "other_title": "The {$(3,4,\\infty)$} modular family of {2}-tori, completed at its three special points, is a complex structure on {$S^6$}",
    "resolution": "Retain the reference from the earlier source in merge order: the alternative is a capitalization/TeX-protection variant of the same work; checked against the source-verification record."
  },
  {
    "key": "KamenovaTori",
    "retained": "sources/returns/S6_02_PUSH/S6_02_PUSH_references.bib",
    "other": "sources/returns/S6_03_CDP/S6_03_CDP_references.bib",
    "other_title": "Degenerations of 2-Dimensional Tori",
    "resolution": "Retain the reference from the earlier source in merge order: the alternative is a capitalization/TeX-protection variant of the same work; checked against the source-verification record."
  },
  {
    "key": "AC26",
    "retained": "sources/returns/S6_02_FAMILY/S6_02_FAMILY_references.bib",
    "other": "sources/returns/S6_04_MAPS_MANIFOLDS/S6_04_MAPS_MANIFOLDS_references.bib",
    "other_title": "The (3,4,infinity) modular family of 2-tori, completed at its three special points, is a complex structure on the six-sphere",
    "resolution": "Retain the reference from the earlier source in merge order: the alternative is a capitalization/TeX-protection variant of the same work; checked against the source-verification record."
  },
  {
    "key": "CDP20",
    "retained": "sources/returns/S6_03_CDP/S6_03_CDP_references.bib",
    "other": "sources/previous_attempt/S6_07_PAPER_references.bib",
    "other_title": "The algebraic dimension of compact complex threefolds with vanishing second Betti number: corrigendum and addendum",
    "resolution": "Reject the previous-attempt title suffix corrigendum and addendum: the original published title is The algebraic dimension of compact complex threefolds with vanishing second Betti number. Original PDF and DOI10.1112/S0010437X19007802 control."
  },
  {
    "key": "Johansson2016",
    "retained": "sources/returns/S6_02_PUSH/S6_02_PUSH_references.bib",
    "other": "sources/previous_attempt/S6_07_PAPER_references.bib",
    "other_title": "Arb: Efficient Arbitrary-Precision Midpoint-Radius Interval Arithmetic",
    "resolution": "Retain the reference from the earlier source in merge order: the alternative is a capitalization/TeX-protection variant of the same work; checked against the source-verification record."
  },
  {
    "key": "PythonFlint2026",
    "retained": "sources/returns/S6_02_PUSH/S6_02_PUSH_references.bib",
    "other": "sources/previous_attempt/S6_07_PAPER_references.bib",
    "other_title": "python-flint 0.9.0 documentation: arb, real numbers",
    "resolution": "Retain the reference from the earlier source in merge order: the alternative is a capitalization/TeX-protection variant of the same work; checked against the source-verification record."
  },
  {
    "key": "E26",
    "retained": "sources/returns/S6_02_FAMILY/S6_02_FAMILY_references.bib",
    "other": "sources/returns/S6_02_PUSH/sections/core_references.bib",
    "other_title": "Complex structures on {$S^6$}",
    "resolution": "Retain the reference from the earlier source in merge order: the alternative is a capitalization/TeX-protection variant of the same work; checked against the source-verification record."
  },
  {
    "key": "KervaireMilnor1963",
    "retained": "sources/returns/S6_02_PUSH/S6_02_PUSH_references.bib",
    "other": "deliverables/work/maps_audit/topology_checked_references.bib",
    "other_title": "Groups of Homotopy Spheres. {I}",
    "resolution": "Retain the reference from the earlier source in merge order: the alternative is a capitalization/TeX-protection variant of the same work; checked against the source-verification record."
  },
  {
    "key": "Brunella1999",
    "resolution": "Split two distinct works. Brunella1999 is On the automorphism group of a complex sphere, DocumentaMath4(1999)451–462, DOI10.4171/DM/64. Brunella1999Forms is On holomorphic forms on compact complex threefolds, CMH74(1999)642–656, DOI10.1007/S000140050109. Both original first pages opened. The Forms publisher-page author metadata is inconsistent with its originalPDF; originalPDF names MarcoBrunella and controls. Source scope remains unverified until the operative theorem is independently matched."
  }
]
```

## Statement-kind corrections

Source record: `records/inventory_kind_corrections.json`.

```json
[
  {
    "source_run": "S6_01_INVARIANTS",
    "source_id": "A4.2",
    "from": "Counterexample or correction",
    "to": "Correction"
  },
  {
    "source_run": "S6_01_INVARIANTS",
    "source_id": "C3.8",
    "from": "Open problem",
    "to": "Open question with complete partial proof"
  },
  {
    "source_run": "S6_01_INVARIANTS",
    "source_id": "E2.4",
    "from": "Counterexample or correction",
    "to": "Counterexample"
  },
  {
    "source_run": "S6_02_FAMILY",
    "source_id": "B.2.3",
    "from": "Counterexample or correction",
    "to": "Correction"
  },
  {
    "source_run": "S6_02_FAMILY",
    "source_id": "C.3.3",
    "from": "Open problem",
    "to": "Proved local obstruction; resolved source question"
  },
  {
    "source_run": "S6_02_FAMILY",
    "source_id": "D.1.3",
    "from": "Counterexample or correction",
    "to": "Counterexample"
  },
  {
    "source_run": "S6_02_FAMILY",
    "source_id": "E.1.5",
    "from": "Open problem",
    "to": "Proved local obstruction; resolved source question"
  },
  {
    "source_run": "S6_02_FAMILY",
    "source_id": "F.2.1",
    "from": "Counterexample or correction",
    "to": "Counterexample"
  },
  {
    "source_run": "S6_02_PUSH",
    "source_id": "A.2.3",
    "from": "Counterexample or correction",
    "to": "Counterexample"
  },
  {
    "source_run": "S6_02_PUSH",
    "source_id": "A.3.2",
    "from": "Theorem",
    "to": "Counterexample"
  },
  {
    "source_run": "S6_02_PUSH",
    "source_id": "A.3.3",
    "from": "Counterexample or correction",
    "to": "Counterexample"
  },
  {
    "source_run": "S6_02_PUSH",
    "source_id": "B.1.1",
    "from": "Counterexample or correction",
    "to": "Counterexample"
  },
  {
    "source_run": "S6_02_PUSH",
    "source_id": "B.3.1",
    "from": "Counterexample or correction",
    "to": "Counterexample"
  },
  {
    "source_run": "S6_02_PUSH",
    "source_id": "B.4.1",
    "from": "Counterexample or correction",
    "to": "Counterexample"
  },
  {
    "source_run": "S6_02_PUSH",
    "source_id": "B.5.1",
    "from": "Counterexample or correction",
    "to": "Counterexample"
  },
  {
    "source_run": "S6_02_PUSH",
    "source_id": "C.5.1",
    "from": "Counterexample or correction",
    "to": "Counterexample"
  },
  {
    "source_run": "S6_02_PUSH",
    "source_id": "D.2.2",
    "from": "Counterexample or correction",
    "to": "Counterexample"
  },
  {
    "source_run": "S6_02_PUSH",
    "source_id": "E.5.1",
    "from": "Counterexample or correction",
    "to": "Counterexample"
  },
  {
    "source_run": "S6_03_CDP",
    "source_id": "A.3.2",
    "from": "Counterexample or correction",
    "to": "Counterexample"
  },
  {
    "source_run": "S6_03_CDP",
    "source_id": "A.4.2",
    "from": "Counterexample or correction",
    "to": "Counterexample"
  },
  {
    "source_run": "S6_03_CDP",
    "source_id": "C.3.2",
    "from": "Counterexample or correction",
    "to": "Counterexample"
  },
  {
    "source_run": "S6_03_CDP",
    "source_id": "C.3.3",
    "from": "Counterexample or correction",
    "to": "Counterexample"
  },
  {
    "source_run": "S6_03_CDP",
    "source_id": "C2b",
    "from": "Counterexample or correction",
    "to": "Counterexample"
  },
  {
    "source_run": "S6_03_CDP",
    "source_id": "D.1.5",
    "from": "Counterexample or correction",
    "to": "Counterexample"
  },
  {
    "source_run": "S6_03_CDP",
    "source_id": "D.1.6",
    "from": "Counterexample or correction",
    "to": "Counterexample"
  },
  {
    "source_run": "S6_03_CDP",
    "source_id": "D.1.13",
    "from": "Counterexample or correction",
    "to": "Counterexample"
  },
  {
    "source_run": "S6_03_CDP",
    "source_id": "E10",
    "from": "Counterexample or correction",
    "to": "Counterexample"
  },
  {
    "source_run": "S6_03_CDP",
    "source_id": "E12",
    "from": "Counterexample or correction",
    "to": "Counterexample"
  },
  {
    "source_run": "S6_03_CDP",
    "source_id": "E17",
    "from": "Counterexample or correction",
    "to": "Counterexample"
  },
  {
    "source_run": "S6_03_CDP",
    "source_id": "E18",
    "from": "Counterexample or correction",
    "to": "Counterexample"
  },
  {
    "source_run": "S6_04_MAPS_MANIFOLDS",
    "source_id": "A.1.2",
    "from": "Counterexample or correction",
    "to": "Correction"
  },
  {
    "source_run": "S6_04_MAPS_MANIFOLDS",
    "source_id": "A.2.2",
    "from": "Counterexample or correction",
    "to": "Counterexample"
  },
  {
    "source_run": "S6_04_MAPS_MANIFOLDS",
    "source_id": "B.6.7",
    "from": "Counterexample or correction",
    "to": "Counterexample"
  },
  {
    "source_run": "S6_04_MAPS_MANIFOLDS",
    "source_id": "D.1.1",
    "from": "Counterexample or correction",
    "to": "Counterexample"
  },
  {
    "source_run": "S6_04_MAPS_MANIFOLDS",
    "source_id": "E.1.1",
    "from": "Counterexample or correction",
    "to": "Counterexample"
  },
  {
    "source_run": "S6_04_MAPS_MANIFOLDS",
    "source_id": "F.2.3",
    "from": "Counterexample or correction",
    "to": "Counterexample"
  },
  {
    "source_run": "S6_05_ARITHMETIC",
    "source_id": "C.8.9",
    "from": "Counterexample or correction",
    "to": "Correction"
  },
  {
    "source_run": "WORKING_CDP",
    "source_id": "test:cdp-comparison",
    "from": "test",
    "to": "Verification with proved assertions"
  },
  {
    "source_run": "working_edition",
    "source_id": "topology_reduction:L600",
    "from": "test",
    "to": "Verification with proved assertions"
  },
  {
    "source_run": "working_edition",
    "source_id": "record:vankampen",
    "from": "auditrecord",
    "to": "Verification record"
  },
  {
    "source_run": "working_edition",
    "source_id": "topology_reduction:L1113",
    "from": "test",
    "to": "Verification with proved assertions"
  },
  {
    "source_run": "WORKING_INV",
    "source_id": "record:h12-direct-images",
    "from": "auditrecord",
    "to": "Verification record"
  }
]
```

## Results moved between papers

| Source | Result | Paper | Printed label |
|---|---|---|---|
| S6_02_FAMILY | E.2.2 | III | `` |
| S6_02_FAMILY | E.2.3 | III | `` |
| S6_02_PUSH | C.1.1 | III | `` |
| S6_02_PUSH | C.1.2 | III | `` |
| S6_02_PUSH | C.2.1 | III | `` |
| S6_02_PUSH | C.2.2 | III | `` |
| S6_02_PUSH | C.2.3 | III | `` |
| S6_02_PUSH | C.3.1 | III | `` |
| S6_02_PUSH | C.3.2 | III | `` |
| S6_02_PUSH | C.3.3 | III | `` |
| S6_02_PUSH | C.3.4 | III | `` |
| S6_02_PUSH | C.3.6 | III | `` |
| S6_02_PUSH | C.3.7 | III | `` |
| S6_02_PUSH | C.3.8 | III | `` |
| S6_02_PUSH | C.3.9 | III | `` |
| S6_02_PUSH | C.3.10 | III | `` |
| S6_02_PUSH | C.3.11 | III | `` |
| S6_02_PUSH | C.3.12 | III | `` |
| S6_02_PUSH | C.3.13 | III | `` |
| S6_02_PUSH | C.3.14 | III | `` |
| S6_02_PUSH | C.3.15 | III | `` |
| S6_02_PUSH | C.3.16 | III | `` |
| S6_02_PUSH | C.3.17 | III | `` |
| S6_02_PUSH | C.3.18 | III | `` |
| S6_02_PUSH | C.3.19 | III | `` |
| S6_02_PUSH | C.3.20 | III | `` |
| S6_02_PUSH | C.3.21 | III | `` |
| S6_02_PUSH | C.3.22 | III | `` |
| S6_02_PUSH | C.3.23 | III | `` |
| S6_02_PUSH | C.3.24 | III | `` |
| S6_02_PUSH | C.3.25 | III | `` |
| S6_02_PUSH | C.3.26 | III | `` |
| S6_02_PUSH | C.3.27 | III | `` |
| S6_02_PUSH | C.4.1 | III | `` |
| S6_02_PUSH | C.4.2 | III | `` |
| S6_02_PUSH | C.5.1 | III | `` |
| S6_02_PUSH | E.2.4 | II | `` |
| S6_02_PUSH | E.2.5 | II | `` |
| S6_02_PUSH | E.2.6 | II | `` |
| S6_02_PUSH | E.2.7 | II | `` |
| S6_02_PUSH | E.2.8 | II | `` |
| S6_02_PUSH | E.2.9 | II | `` |
| S6_02_PUSH | E.2.10 | II | `` |
| S6_02_PUSH | E.2.11 | II | `` |
| S6_02_PUSH | E.2.12 | II | `` |
| S6_02_PUSH | E.2.13 | II | `` |
| S6_02_PUSH | E.2.14 | II | `` |
| S6_02_PUSH | E.2.15 | II | `` |
| S6_02_PUSH | E.2.16 | II | `` |
| S6_02_PUSH | E.2.17 | II | `` |
| S6_02_PUSH | E.2.18 | II | `` |
| S6_02_PUSH | E.2.19 | II | `` |
| S6_02_PUSH | E.2.20 | II | `` |
| S6_02_PUSH | E.2.21 | II | `` |
| S6_02_PUSH | E.2.22 | II | `` |
| S6_02_PUSH | E.2.23 | II | `` |
| S6_02_PUSH | E.2.24 | II | `` |
| S6_02_PUSH | E.5.1 | II | `` |
| S6_02_PUSH | E.5.2 | II | `` |
| S6_02_PUSH | E.5.3 | II | `` |
| S6_03_CDP | D.1.14 | I | `fam:src:F.1.1` |
| S6_03_CDP | E9 | I | `fam:src:A.5.2` |
| S6_04_MAPS_MANIFOLDS | A.1.1 | I | `mapsI:src:A.1.1` |
| S6_04_MAPS_MANIFOLDS | A.1.2 | I | `mapsI:src:A.1.2` |
| S6_04_MAPS_MANIFOLDS | A.1.3 | I | `mapsI:src:A.1.3` |
| S6_04_MAPS_MANIFOLDS | A.2.1 | I | `mapsI:src:A.2.1` |
| S6_04_MAPS_MANIFOLDS | A.3.1 | I | `mapsI:src:A.3.1` |
| S6_04_MAPS_MANIFOLDS | A.3.2 | I | `mapsI:src:A.3.2` |
| S6_04_MAPS_MANIFOLDS | A.3.3 | I | `mapsI:src:A.3.3` |
| S6_04_MAPS_MANIFOLDS | A.3.4 | I | `mapsI:src:A.3.4` |

## Original-source opening records

Each entry gives the actual scope checked. A downloaded or identified source is not thereby verified. The shared bibliography contains the operative verification state, including explicit unverified nonoperative comparisons.

### work/root/references_verified.json

```json
[
  {
    "keys": [
      "IKN2005E"
    ],
    "locator": "Illusie–Kato–Nakayama (2005), Theorems 6.2, 6.3, 6.4, pp.32–35",
    "source": "sources/external/root/IKN2005.pdf",
    "verification": "Proper separated fs log smooth analytic family; log smooth base; constant unipotent system; semistable characteristic cokernel torsion free. Locally free canonical log de Rham extension, without Kähler hypotheses.",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 17 November 2026",
    "status": "verified in the specified scope"
  },
  {
    "keys": [
      "IKN2007ErratumE"
    ],
    "locator": "Illusie–Kato–Nakayama (2007), erratum, pp.113–116",
    "source": "https://www.ms.u-tokyo.ac.jp/journal/pdf/jms140105.pdf",
    "verification": "Opened through web retrieval; correction concerns algebraic Hodge Theorem 7.1, not analytic Theorem 6.3.",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 17 November 2026",
    "status": "verified in the specified scope"
  },
  {
    "keys": [
      "KKN2008",
      "KKN2008Root"
    ],
    "locator": "Kajiwara–Kato–Nakayama (2008), Definitions 1.2.3–1.2.6, Lemma 1.2.9, §§1.3,5.1.1–5.1.2, Theorem 5.3.2",
    "source": "sources/external/root/KKN2008I.pdf",
    "verification": "Admissibility checked on faces and preserved by fs base change; nondegenerate log complex torus; complete Y-invariant fan with finitely many orbits gives proper analytic model, no polarization required.",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 17 November 2026",
    "status": "verified in the specified scope"
  },
  {
    "keys": [
      "BM95AB",
      "BierstoneMilman1997"
    ],
    "locator": "Bierstone–Milman, alg-geom/9508005, Theorems 1.6 and 1.10",
    "source": "sources/external/root/BM1995.pdf",
    "verification": "Analytic embedded resolution and principalization near relatively compact exceptional set; no algebraic compactification inference.",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 17 November 2026",
    "status": "verified in the specified scope"
  },
  {
    "keys": [
      "Parusinski1990E"
    ],
    "locator": "Parusiński (1990), Corollary 1.2 and proof, manuscript pp.3–5",
    "source": "sources/external/root/Parusinski1990.pdf",
    "verification": "Coefficient-ideal blowup argument read; finite local projections and compactness give an equidimensional modification in the excess-one situation.",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 17 November 2026",
    "status": "verified in the specified scope"
  },
  {
    "keys": [
      "EH2024E"
    ],
    "locator": "Enokizono–Hashizume (2024), Lemma 2.14 and proof",
    "source": "sources/external/root/EH2024v3.pdf",
    "verification": "Analytic strict toroidal subdivisions and proper modifications; their projective main theorem is not used.",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 17 November 2026",
    "status": "verified in the specified scope"
  },
  {
    "keys": [
      "Lazzeri1973Root"
    ],
    "locator": "Lazzeri (1973), Theorem 2, corollary and concluding remark, pp.274–275",
    "source": "sources/external/root/Lazzeri1973.pdf",
    "verification": "Isolated hypersurface singularity, deformation with all critical points on one fibre: more than one singular point gives strictly smaller total vanishing-cycle module. Combined with conservation of Milnor number in the actual plane slice.",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 17 November 2026",
    "status": "verified in the specified scope"
  },
  {
    "keys": [
      "Meersseman2019E"
    ],
    "locator": "Meersseman (2019), §3.2, Theorem 3.4, Remark 3.6, pp.898–899; Convention 3.2",
    "source": "sources/external/root/Meersseman2019.pdf",
    "verification": "Connected C-infinity neighbourhood of an integrable structure has the Kuranishi local product, analytic retraction and diffeomorphism action; restriction from Sobolev to smooth structures explicitly justified.",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 17 November 2026",
    "status": "verified in the specified scope"
  },
  {
    "keys": [
      "HondaViaclovsky2025D"
    ],
    "locator": "Honda–Viaclovsky (2025), Corollary 3.7 and proof, p.11; Theorem 3.5, p.10",
    "source": "sources/external/root/HondaViaclovsky2025.pdf",
    "verification": "Corollary 3.7 requires irreducible singular support and gives H1 local invariant cycles without Kähler. The printed converse relating global monodromy to fibre equality is separately corrected in PUSH B.4.17; it is not used.",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 17 November 2026",
    "status": "verified in the specified scope"
  },
  {
    "keys": [
      "AKMW02AB"
    ],
    "locator": "Abramovich–Karu–Matsuki–Wlodarczyk (2002), Theorems 1.6.1 and 2.7.1, §§5.5–5.6 pp.565–566",
    "source": "sources/external/root/retrieved/AKMW02AB.pdf",
    "verification": "Opened statements and proof of reduction to finite conical complexes; analytic strict toroidal charts, barycentric strictification, subdivision/modification correspondence, and factorization of the finite complex by regular stars. The full analytic theorem requires completeness; the paper uses its finite combinatorial argument plus the explicit analytic chart realization, with compactness near the central set.",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 17 November 2026",
    "status": "verified in the specified scope"
  },
  {
    "keys": [
      "Matsuki00ErrAB"
    ],
    "locator": "Matsuki (2000), §2, p.2, and final remark p.3",
    "source": "sources/external/root/retrieved/Matsuki00ErrAB.pdf",
    "verification": "Corrected weak factorization for proper toroidal birational morphisms between nonsingular strict toroidal embeddings: smooth irreducible closed-stratum centres and every intermediate toroidal over the target. Strong factorization is expressly not used. This supplies termination of the finite path search in PUSH A.2.5.",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 17 November 2026",
    "status": "verified in the specified scope"
  },
  {
    "keys": [
      "NO10"
    ],
    "locator": "Nakayama–Ogus (2010), Theorem 5.1 and proof, p.2226",
    "source": "sources/external/root/retrieved/NO10.pdf",
    "verification": "Proper separated exact relatively smooth morphism of log analytic spaces, fine base and relatively coherent total space: rounded map is an oriented manifold fibre bundle. Semistable charts have N→N^k diagonal, fs exact log smooth; all hypotheses hold in the stated semistable application.",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 17 November 2026",
    "status": "verified in the specified scope"
  },
  {
    "keys": [
      "GrafKovacs2014Root"
    ],
    "locator": "§1.D, p.120",
    "source": "sources/external/root/retrieved/GrafKovacs2014Root.pdf",
    "verification": "Proper complex algebraic varieties with Du Bois singularities have surjective H^i(C) to H^i(O); normal crossings are Du Bois. Used only in the algebraic central-fibre branch, never extended to arbitrary analytic spaces.",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 17 November 2026",
    "status": "verified in the specified scope"
  },
  {
    "keys": [
      "Buchdahl1999"
    ],
    "locator": "Theorem 11, p.297",
    "source": "sources/external/root/retrieved/Buchdahl1999.pdf",
    "verification": "Every compact complex surface with even first Betti number is Kähler. The constructed compact smooth torsor surface has b1=6; no classification assumption is required.",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 17 November 2026",
    "status": "verified in the specified scope"
  },
  {
    "keys": [
      "Loj64"
    ],
    "locator": "§3, Theorems 1–2, pp.463–464",
    "source": "sources/external/root/retrieved/Loj64.pdf",
    "verification": "Locally finite semianalytic subsets of a countable real-analytic manifold admit a compatible triangulation. The compact neighbourhoods and analytic fibre cycles used in the virtual Euler proof meet these hypotheses.",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 17 November 2026",
    "status": "verified in the specified scope"
  },
  {
    "keys": [
      "FG10"
    ],
    "locator": "Theorem 5.8 and Remark 5.9, p.102",
    "source": "sources/external/root/retrieved/FG10.pdf",
    "verification": "Virtual Euler and virtual Chern numbers of proper lci schemes are invariant under lci deformation and equal smoothing invariants. This is cited as the algebraic comparison only; the non-Kähler analytic application has its own perfect-complex and cycle argument.",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 17 November 2026",
    "status": "verified in the specified scope"
  },
  {
    "keys": [
      "Chen2026HodgeRoot"
    ],
    "locator": "Definition 2.3 and Theorem 2.4(3)–(4), pp.9–10 of arXiv v2",
    "source": "sources/external/root/retrieved/Chen2026HodgeRoot.pdf",
    "verification": "Proper semistable analytic degeneration with K1 (all closed strata ddbar, including Kähler strata) gives the stated limiting mixed Hodge complex and E1 degeneration on nearby fibres. K1 is not omitted and no Kähler total space is assumed.",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 17 November 2026",
    "status": "verified in the specified scope"
  },
  {
    "keys": [
      "Levy08"
    ],
    "locator": "Lemma 3.1 and §3.1, Lemma 3.2, pp.588–590",
    "source": "sources/external/root/retrieved/Levy08.pdf",
    "verification": "The exact functor yields topological K-classes, homotopy compatible; finite local complexes glue after adding continuous acyclic summands. This supplies the topological realization of the analytic perfect cotangent complex on compact triangulated neighbourhoods.",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 17 November 2026",
    "status": "verified in the specified scope"
  },
  {
    "keys": [
      "Manetti1991D"
    ],
    "locator": "§1, Lemma1 and proof, original printed p.93",
    "source": "sources/external/root/Manetti1991_p93.jpg",
    "verification": "Original GDZ scan visually opened: reduced compact complex space with isolated singular points and H²(Theta)=0. The restriction map from a semiuniversal deformation germ to the product of local semiuniversal germs is smooth, so every prescribed local deformation globalizes. Applies to the compact normal contraction of the degree-eight elliptic axis; no rational-curve, projectivity or Kähler hypothesis. Pages92–93 opened; exact scan hashes in Manetti1991_pages.json.",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 17 November 2026",
    "status": "verified in the specified scope"
  },
  {
    "keys": [
      "DlousskyTeleman2020D"
    ],
    "locator": "§3.1 Lemma3.2, §3.2 Proposition3.3, printed pp.10–11 of arXiv manuscript",
    "source": "sources/external/root/retrieved/DlousskyTeleman2020D.pdf",
    "verification": "Compact complex space with single singularity; regular morphism of global-to-local semiuniversal germs makes smoothability equivalent. Compactness shrinks to one neighborhood and keeps all singular fibres inside the specified local germ. Proposition3.4 is confined to rational cycles and is not used for elliptic contraction.",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 17 November 2026",
    "status": "verified in the specified scope"
  },
  {
    "keys": [
      "CornulierChabauty"
    ],
    "locator": "Theorem3.1, pp.10–11, including definition of R/Z annihilator",
    "source": "https://www.normalesup.org/~cornulier/pontri.pdf",
    "verification": "The annihilator map on closed subgroups of any finite-dimensional real vector space is a Chabauty homeomorphism. All groups used in the limiting-period proof are closed full lattices in R4, and bounded integral dual labels give the computed discrete graph.",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 17 November 2026",
    "status": "verified in the specified scope"
  },
  {
    "keys": [
      "Fujino2021E"
    ],
    "locator": "Definition3.1, Lemma3.3 and Corollary3.4, pp.5–6 author manuscript",
    "source": "https://www.math.kyoto-u.ac.jp/~fujino/surfaces-classC2.pdf",
    "verification": "Irreducible compact normal analytic surface in class C has a Kähler resolution; every resolution is Kähler. Proof uses invariance of b1 under surface blow-ups and the even-b1 characterization. Only the surface assertion is used.",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 17 November 2026",
    "status": "verified in the specified scope"
  },
  {
    "keys": [
      "Grauert1962E"
    ],
    "locator": "§3 Satz8 p.353; §4 Sätze1–2 pp.355–357, corollary to Satz7 p.363; correction addendum p.367",
    "source": "https://de.scribd.com/document/864372889/grauert1962",
    "verification": "Original German article reproduction opened at exact statements. Negative normal line gives an exceptional compact submanifold; strongly pseudoconvex-neighborhood cohomology images of high ideal powers vanish, with the printed correction included. Positive-power H1 vanishings give local equivalence to the normal bundle. This is not used as an unchecked substitute for analytic formal functions; that exact theorem is Grauert1960 HauptsatzIIa, separately opened.",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 17 November 2026",
    "status": "verified in the specified scope"
  },
  {
    "keys": [
      "AtiyahSinger1968IIIE"
    ],
    "locator": "Atiyah–Singer (1968), III, printed pp.565–566, formula (4.4), Theorem (4.6)",
    "source": "sources/external/root/retrieved/AtiyahSinger1968IIIE.pdf",
    "source_sha256": "2299cc0b6ddd36d7d4bbba87da602da853d188281ee35d952f20de3c6752d296",
    "verification": "Original scanned pages visually opened. Compact complex manifold, holomorphic vector bundle and finite group; no Kähler hypothesis. B.4.14 applies to nontrivial roots of unity and then determines the finite Laurent-polynomial C* character.",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 17 November 2026",
    "status": "verified in the specified scope"
  },
  {
    "keys": [
      "Pinkham1974Root"
    ],
    "locator": "Pinkham (1974), Remark 7.6(iii), printed pp.45–46; Section 9, pp.63–65",
    "source": "sources/external/root/retrieved/Pinkham1974Root.pdf",
    "source_sha256": "0fd47261a0eb321be0eece5cd3394291c887ac22a7b76fed70d3ab30284bfccb",
    "verification": "Original text opened. Normal projective cone swept by hyperplanes gives the flat family; degree-eight quadric smoothing component distinguished from the cubic-blowup component. Used as context for the independently written affine construction, not as a global analytic gluing theorem.",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 17 November 2026",
    "status": "verified in the specified scope"
  },
  {
    "keys": [
      "BiliottiGhigi2021Root"
    ],
    "source": "sources/external/root/retrieved/BiliottiGhigi2021Root.pdf",
    "locator": "Theorem 1.2, manuscript p.3",
    "verification": "Opened exact theorem and class-C definition. Compactification of divergent automorphisms assumes Fujiki class C; this is explicitly unavailable in the filling problem, so no compactness conclusion is imported.",
    "status": "verified in the specified scope",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 17 November 2026",
    "source_sha256": "0444364ab72d923ef34d840dcfb302dc90b6053def45826013b23558e0668429"
  },
  {
    "keys": [
      "Meersseman2011Root"
    ],
    "source": "sources/external/root/retrieved/Meersseman2011Root.pdf",
    "locator": "Theorem 3 and opening proof, journal p.511",
    "verification": "Reduced parameter space and constant h0 yield the local isomorphism property for families pointwise isomorphic on the entire base. Punctured-base agreement alone does not meet the premise.",
    "status": "verified in the specified scope",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 17 November 2026",
    "source_sha256": "3d9621b7981af8b7c1544b66167483c724799e3910fbf145b978748ebc4d88d3"
  },
  {
    "keys": [
      "EGFS25"
    ],
    "source": "sources/external/root/retrieved/EGFS25.pdf",
    "locator": "Construction 3.8 and Remark 3.9, manuscript pp.23–25",
    "verification": "Opened the full multivariable fan construction: positive semidefinite symmetric forms with positive definite sum, periodic fan and flat fan map; arbitrary period twists are symmetric. PUSH invokes its related polarized construction only, and proves its nonsymmetric analytic quotient independently.",
    "status": "verified in the specified scope",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 17 November 2026",
    "source_sha256": "a341ca773e7f20a607fece5e01f7e7d00c614b09632209202617b141919aa3a4"
  },
  {
    "keys": [
      "DMM16"
    ],
    "source": "sources/external/root/retrieved/DMM16.pdf",
    "locator": "Section 2, p.6, Toric maps",
    "verification": "Properness is exactly inverse-image equality of fan supports. Applied on each finite fan over an original affine chart; analytification of this proper algebraic toric map gives the local analytic modification. No finite-type conclusion is asserted for the whole infinite fan before quotient.",
    "status": "verified in the specified scope",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 17 November 2026",
    "source_sha256": "e769d3c50f9499507f05a7e0e67441fd371bd874bb4aa9726923f5a5cc35fef6"
  },
  {
    "keys": [
      "KKN2008PicardE"
    ],
    "source": "sources/external/root/retrieved/KKN2008PicardE.pdf",
    "locator": "Definition 7.1, pp.164–165; Sections 9.1–9.3, p.173",
    "verification": "Opened all goodness conditions and the explicit distinction in 9.2: log de Rham comparison (i) needs no projectivity under log-smooth-base/exact hypotheses, whereas Hodge filtration and log Hodge structure need further conditions. The present non-Kähler filling is not classified by the full log Picard theorem.",
    "status": "verified in the specified scope",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 17 November 2026",
    "source_sha256": "9231d235ee5b85abe1a7bf083adbeb72fc61130e3b6cda4b88bb8df347fb10b7"
  },
  {
    "keys": [
      "Fujiki2009D"
    ],
    "source": "sources/external/root/retrieved/Fujiki2009D.pdf",
    "locator": "Theorem 1.1 and Section 2, equations (1)–(10), manuscript pp.1–5",
    "verification": "Parabolic Inoue surface with b2=m>0, identity automorphisms C*, explicit infinite toric atlas and deck action. For m=8 the central scaling action fixes the elliptic curve and has reciprocal weights at the eight cycle nodes; the paper separately derives its vector-field/cohomology calculation.",
    "status": "verified in the specified scope",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 17 November 2026",
    "source_sha256": "21b64005400ed93ddd7c80805b3e15dba6f5d31334cfe79a9378f2b57847c6de"
  },
  {
    "keys": [
      "Doi2009Root"
    ],
    "source": "sources/external/root/retrieved/Doi2009Root.pdf",
    "locator": "Theorem 5.5 and following comparison, pp.882–883",
    "verification": "Simple normal crossing complex surface with at most double curves, dual normal bundles, anticanonical conductors and matching opposite residues. Conclusion is a smooth real total space with continuously varying complex structures off the double locus, expressly weaker than a holomorphic smoothing. It cannot supply the required proper holomorphic family.",
    "status": "verified in the specified scope",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 17 November 2026",
    "source_sha256": "5f5b897c6f1e414de51242c321a63b46455a37c1aae8bf21abbb87b56957c9bd"
  },
  {
    "keys": [
      "Nishiguchi1988IIRoot"
    ],
    "source": "sources/external/root/retrieved/Nishiguchi1988IIRoot.pdf",
    "locator": "Theorem 1.4, manuscript p.7; Example 2.1, pp.13–14",
    "verification": "Opened exact classification alternatives and explicit elliptic Hopf component glued to an elliptic K3 along a smooth fibre. Supports existence of non-Kähler components in analytic semistable degenerations only; no Kähler component hypothesis may be inferred merely from properness.",
    "status": "verified in the specified scope",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 17 November 2026",
    "source_sha256": "1977b1f3a14fd4df14c52d91837273119312dc86b6999ec118840691396b1c7a"
  },
  {
    "keys": [
      "KamenovaToriRoot"
    ],
    "source": "sources/external/root/retrieved/KamenovaToriRoot.pdf",
    "locator": "Definition of degeneration, p.1; Theorem 3.1, p.2",
    "verification": "Semistable Kähler total space and trivial canonical bundle are explicit hypotheses of the torus degeneration classification; these are unavailable for the proposed non-Kähler caps. No classification is transferred without them.",
    "status": "verified in the specified scope",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 17 November 2026",
    "source_sha256": "8cd2ddcef5c77b97f6d1b648a73191734696dceb1c9281c09342413596cfbd0b"
  },
  {
    "keys": [
      "Cartan1952B_AB"
    ],
    "source": "sources/external/root/retrieved/Cartan1952B_AB.pdf",
    "locator": "Exposé 19, Section 5, pp.19-14–19-15",
    "verification": "Opened full cocycle proof of Theorem B on a Stein manifold: positive coherent cohomology vanishes. Applied to the actual locally free sheaf of vector translations on the Stein punctured-base product, not to the nonlinear torus torsor without its separate integral obstruction.",
    "status": "verified in the specified scope",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 17 November 2026",
    "source_sha256": "c0ef7ba59cfa32cc1fe6604baeffa1e5d95aa8b525a63a896f188813d02a68fd"
  },
  {
    "keys": [
      "PY16push"
    ],
    "source": "https://archive.ymsc.tsinghua.edu.cn/pacm_download/50/409-higher_analytic_stacks.pdf",
    "locator": "Theorem 7.4 and proof, pp.45–46; Proposition 7.3",
    "verification": "Proper algebraic stack over C has equivalent algebraic and analytic coherent-sheaf categories. The weighted projective root curve is a proper algebraic Deligne–Mumford stack; invertibility of a line bundle is local on its atlas. This supplies exactly the Picard comparison, independently also proved by the explicit analytic characters.",
    "status": "verified in the specified scope",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 17 November 2026"
  },
  {
    "keys": [
      "McMullen1996Complex"
    ],
    "source": "https://people.math.harvard.edu/~ctm/home/text/class/berkeley/241/96/course/course.pdf",
    "locator": "Section 67, p.15",
    "verification": "Opened identification of infinitesimal complex deformations with H1 of holomorphic vector fields. Used as context only: the paper prints the complete Čech coboundary-to-trivialization argument and records its sign convention.",
    "status": "verified in the specified scope",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 17 November 2026"
  },
  {
    "keys": [
      "PareschiPopaSchnell2017"
    ],
    "source": "https://msp.org/gt/2017/21-4/gt-v21-n4-p12-p.pdf",
    "locator": "Section 8, Proposition 8.1 and proof, pp.2437–2438",
    "verification": "Opened exact torus algebraic-reduction statement: quotient by a connected complex subtorus is an abelian variety realizing the algebraic reduction. Applied to a compact two-dimensional complex torus; no projectivity of the original torus is presumed.",
    "status": "verified in the specified scope",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 17 November 2026"
  },
  {
    "keys": [
      "LinWang2010D"
    ],
    "source": "https://arxiv.org/pdf/math/0608358",
    "locator": "Author preprint v2, equation (1.1), Theorem 1.3, pp.2–3; publisher bibliographic record",
    "verification": "Opened fixed-torus Green critical equation and upper bound five, with the three half-period critical points. This counts critical points in the torus coordinate, not critical moduli of the composite height used here.",
    "status": "verified in the specified scope",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 17 November 2026"
  },
  {
    "keys": [
      "ChenKuoLin2019D"
    ],
    "source": "https://files.sciengine.com/pdfs/1674-7283/D32F7CA22FD34AC2AB4CEDD492E051EB.pdf",
    "locator": "Definitions (1.2)–(1.3), Theorem 1.1; Appendix A, (A.1)–(A.3), Propositions A.1–A.2, pp.2101–2102",
    "verification": "Opened derivative identities and complete simple-zero proof. Their eta1 is pi²E2/3, matching our normalization; their holomorphic functions f(k,C) differ from the real-analytic factor 3ZP−2g2 on wp=0. No global modulus exclusion is inferred from their theorem.",
    "status": "verified in the specified scope",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 17 November 2026"
  },
  {
    "keys": [
      "ChenFuLin2025GenericD"
    ],
    "source": "https://arxiv.org/html/2503.06935v1",
    "locator": "Definition (1.1) and Theorem 1.1",
    "verification": "Opened multiple Green function and measure-zero exceptional moduli theorem. It supplies generic nondegeneracy of fibre-coordinate critical points, not exclusion of every critical modulus for the specific composite function.",
    "status": "verified in the specified scope",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 17 November 2026"
  },
  {
    "keys": [
      "ChenFuLin2025HitchinD"
    ],
    "source": "https://arxiv.org/html/2508.17604v2",
    "locator": "Section 1.1, Theorems A, B and 1.2",
    "verification": "Opened exact fixed-torus theorem: an existing nontrivial critical pair has positive Hessian. This is compared only with the first factor of the composite derivative; it does not handle its other factor or establish the present global level classification.",
    "status": "verified in the specified scope",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 17 November 2026"
  },
  {
    "keys": [
      "AbashevaDeev2024AB"
    ],
    "source": "sources/external/root/retrieved/AbashevaDeev2024AB.pdf",
    "locator": "Section2.2, items2.2.4–2.2.9, pp.4–5; Proposition3.1.2 and its proof, p.13",
    "verification": "Opened diagonal-Hopf quotient and normal-line character convention; scalar quotient parameters are compared only in the explicit scalar case. Proposition3.1.2 explicitly records torsion canonical bundle for minimal Kodaira-dimension-zero surfaces. Application separately proves an effective torsion divisor must vanish; it does not apply the non-torsion-normal-bundle hypothesis to an arbitrary surface.",
    "status": "verified in the specified scope",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 17 November 2026",
    "sha256": "506d60ef501997ba8e773dd1610a4d2c721dff120e6c5009d55a0e52245a410d"
  },
  {
    "keys": [
      "DlousskyTeleman2012AB"
    ],
    "source": "sources/external/root/retrieved/DlousskyTeleman2012AB.pdf",
    "locator": "Section1.2, pp.3–4; Remark2.1 and Proposition2.3 with full proof, pp.6–7",
    "verification": "Original text explicitly permits a holomorphic submersion of relative dimension2 without properness. Simply exceptional divisor has H0=H1=0 for its fibre normal line; the total normal sequence gives the smooth local Douady germ and local biholomorphism to the base. PUSH uses its actual relative surface neighborhood, not an arbitrary singular cap. The GSS exceptional-curve nonproperness example is used as context only.",
    "status": "verified in the specified scope",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 17 November 2026",
    "sha256": "4baffa01de38f40df1b2d021a6776964c50561acc3e1a66b6d2dae9718d87830"
  },
  {
    "keys": [
      "Yang2026",
      "Y26"
    ],
    "source": "sources/papers/arXiv_2609.29666_Yang_src/Compact_Complex_Threefolds_REPAIRED_v4_5.tex",
    "locator": "Section6, lemmas fibrewise-affine-form, monodromy-centralizer, affine-norm-condition, toroidal-translation-valuation; proposition torus-translation-globalization; proposition parameter-translations and full proof",
    "verification": "Read the centralizer/norm and complete collar-patching proof for the source TypeB/TypeC families. Exact period is6/r; equality of torus lattices alone is insufficient. Necessity uses order-six norm lattice and excludes epsilon=−1, sufficiency uses zero cusp valuation and explicit finite-collar windings in the torsion-free obstruction group. These results are comparisons with distinct finite orders, not a claimed theorem for the standard3,4 family.",
    "status": "verified in the specified scope",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 17 November 2026",
    "sha256": "5061ce4e6cda8ed7ba3bb2a7a597d50e018bfd53fb9e49e7b38317f628c332a5"
  },
  {
    "keys": [
      "ViaclovskyLog2026",
      "Viaclovsky2026Log",
      "VL26",
      "ViaLog26push"
    ],
    "source": "sources/papers/arXiv_2610.39102_Viaclovsky_log_transformations_src/Logarithmic_S6_October_28_2026_Final.tex",
    "locator": "Proposition4.7, source label nonbih, and its complete proof",
    "verification": "Opened exact multiplicity-invariance and positive Kuranishi-dimension argument. Stokes plus H2=0 forces fibre preservation; three distinct local monodromy orders fix the base. Varying the fourth period with three fixed independent columns is nonconstant, and countability of markings excludes local isotriviality. It proves dimension at least1, not local miniversality or global period classification.",
    "status": "verified in the specified scope",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 17 November 2026",
    "sha256": "de895f47e8c416b91cfe78d0578b138e44a17ae95050c03a502c37dc264cefbf"
  },
  {
    "keys": [
      "Fujimoto1990AB"
    ],
    "source": "sources/external/root/retrieved/Fujimoto1990AB.pdf",
    "locator": "Section1, construction and Definition1.1, journal pp.85–86; introductory theorem(A) and scope discussion",
    "verification": "Read Cartier-divisor logarithmic cocycle construction with alpha in the elliptic period lattice, over a possibly noncompact complex base. Outside divisor, the logarithm provides the comparison. Our higher-torus use is independently proved by the displayed period homomorphism; no elliptic theorem is generalized silently. The source explicitly restricts its classification theorem by Kähler or base h20 condition.",
    "status": "verified in the specified scope",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 17 November 2026",
    "sha256": "36563ece817361e74d7b057aa100918372bf21e9877046fa79db6414ddd1b9d2"
  },
  {
    "keys": [
      "IstratiEtAl2022Root"
    ],
    "source": "sources/external/root/retrieved/IstratiEtAl2022Root.pdf",
    "locator": "Theorem7.1 and preceding construction, p.1373",
    "verification": "Opened exact Nakamura family for an n-dimensional toric Kato manifold: flat proper holomorphic family, smooth total space, prescribed toric divisor and central self-identification. This is a non-Kähler comparison only and does not extend the particular affine two-torus family studied here.",
    "status": "verified in the specified scope",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 17 November 2026",
    "sha256": "5d22bdb2d5b66b6b50408b7fd233aef1d27543d06e54e7d4c3aebc67efbad1d0"
  },
  {
    "keys": [
      "Demailly2012E"
    ],
    "source": "sources/external/root/retrieved/Demailly2012E.pdf",
    "locator": "ChapterII Theorem4.19, pp.95–96; Theorem7.6, Definition7.9, Theorem7.12, pp.112–115; Theorems8.7–8.8, pp.118–119",
    "verification": "Opened finite local parametrization theorem for irreducible analytic germs, normal-singular-locus codimension≥2, normalization existence/finiteness, and Remmert proper mapping theorem. Matched finite-projection/fibre-isolation, normalized curve smoothness, and proper analytic image arguments in PUSH. The generic projection is chosen to isolate the central fibre, not asserted for every projection.",
    "status": "verified in the specified scope",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 17 November 2026",
    "sha256": "d7c7654a7417e8322e5dcf8fe8ec818b4c1a18cf280b41f2df5a871b776d89a1"
  },
  {
    "keys": [
      "Merkulov1995D"
    ],
    "source": "https://www.cambridge.org/core/journals/mathematical-proceedings-of-the-cambridge-philosophical-society/article/abs/moduli-spaces-of-compact-complex-submanifolds-of-complex-fibered-manifolds/5126226B2B286808A2682C79B6366009",
    "locator": "Publisher-opened original opening extract, p.71",
    "verification": "Exact Kodaira completeness statement is visible in original paper opening: compact embedded complex submanifold with H1(N)=0 belongs to a smooth locally complete family with tangent H0(N). Only this stated theorem is used; no unread Merkulov connection theorem is imported. Kodaira1962 original full text remains unavailable and is not the operative citation.",
    "status": "verified in the specified scope",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 17 November 2026"
  },
  {
    "keys": [
      "KatzarkovEtAl2025Root"
    ],
    "source": "https://www.researchgate.net/publication/390669954_On_Hodge_polynomials_for_nonalgebraic_complex_manifolds",
    "locator": "Original article Example1, p.7, displayed in full-text transcription",
    "verification": "Opened the complete example: scalar elliptic Hopf surface minus one fibre and E×P1 minus the infinity fibre have common analytic open E×C and are not bimeromorphic. Used solely to show that a punctured analytic piece does not determine its compactification; no definable-bimeromorphism theorem is applied.",
    "status": "verified in the specified scope",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 17 November 2026"
  },
  {
    "keys": [
      "Nakayama2002Root"
    ],
    "source": "sources/external/root/retrieved/Nakayama2002Root.pdf",
    "locator": "Theorem7.1.3 and setup, journal p.604 (PDF page154), visually inspected",
    "verification": "Exact setup is a polydisc with coordinate divisor, Zariski-open complement of codimension≥2, and a locally bimeromorphically projective elliptic fibration smooth off divisor. Extension up to bimeromorphism is equivalent to being bimeromorphically projective. The source theorem is not applied to a two-torus family. Text font encoding was unreadable; original page was rendered and inspected, rather than treating corrupted extraction as verification.",
    "status": "verified in the specified scope",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 17 November 2026",
    "sha256": "dafa3f3e06e64a0cd485d0067c937f2a1a132304a2f1533e13588d1179d1b502"
  },
  {
    "keys": [
      "Teleman2010AB"
    ],
    "source": "sources/external/root/retrieved/Teleman2010AB.pdf",
    "locator": "Introduction pp.1750–1751",
    "verification": "Opened the discussion that a Kato/GSS surface is a degeneration of blown-up primary Hopf surfaces. Used only as context for the independently constructed marked insertion; no general class-VII GSS conjecture is assumed.",
    "status": "verified in the specified scope",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 17 November 2026",
    "sha256": "3f2c3f03cdf87a3e64125810336b766a38d9e36e5f3b0a1fe4b6c97c9ad4a50f"
  },
  {
    "keys": [
      "SS00",
      "SchroeerSiebert2002Root"
    ],
    "source": "sources/external/root/retrieved/SS00.pdf",
    "locator": "Section3, Propositions3.1,3.2,3.4 and complete proofs; Remark3.3, preprint pp.6–9",
    "verification": "Opened diagonal Hopf quotient, elliptic double-curve gluing, canonical descent, and explicit normal-character condition for d-semistability. The two congruences concern the source's specified glued surface; used as a comparison, never as an unrestricted smoothing theorem for our radial winding cap.",
    "status": "verified in the specified scope",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 17 November 2026",
    "sha256": "88c238a3151ae5e4fa68bee7dfd6158b6075f2a72d407d16e9262a7ac7dbcfec"
  },
  {
    "keys": [
      "Johansson2016"
    ],
    "source": "sources/external/root/retrieved/Johansson2016.pdf",
    "locator": "Sections2.2–2.3,3.1–3.2,5, pp.2–7",
    "verification": "Opened exact interval-enclosure semantics, midpoint and radius types, outward radius rounding, exact sign extraction and propagated error including midpoint rounding. Distinguished analytic truncation bounds from finite ball arithmetic and from software correctness. Mathematical certificates contain all analytic tails and box-cover logic separately.",
    "status": "verified in the specified scope",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 17 November 2026",
    "sha256": "44802d5cce02bf91a3d155870b8f315f2955866e283bfb48f6776a07f35f6ebf"
  },
  {
    "keys": [
      "PythonFlint2026"
    ],
    "source": "sources/external/root/retrieved/PythonFlint2026.html",
    "locator": "flint.arb constructor; lower,upper,abs_lower,abs_upper documentation",
    "verification": "Opened full exact integer/rational/decimal constructor semantics and upward radius rounding; lower/upper return exact floating bounds rounded outward. Certificate decisions compare actual Arb bounds, not printed rounded decimal approximations. Local installed python-flint0.9.0 reruns are recorded.",
    "status": "verified in the specified scope",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 17 November 2026",
    "sha256": "623fa9dd987b3b466e219a34d1151738387d0b32f8f3f9c2d4ff8b1784eab340"
  },
  {
    "keys": [
      "CDL24"
    ],
    "source": "sources/external/root/retrieved/CDL24.pdf",
    "locator": "Proposition0.9.2 p.143; Section4.2 opening p.370; Lemma4.7.8, exact sequence4.7.4, Theorem4.7.9 pp.445–446",
    "verification": "Opened relative Picard/Brauer exact sequence and Br(C)=0 for a smooth curve over an algebraically closed field. Opened global Weil–Châtelet localization and vanishing of torsion obstruction for a nontrivial Jacobian. Applied to the projective elliptic surface over a complex function field, not to the non-Kähler threefold itself; the paper also gives the characteristic-zero cd1 proof of H2(K,E)=0.",
    "status": "verified in the specified scope",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 17 November 2026",
    "sha256": "3c6bf1d54954e28728935bbe1f4b1e38435fe469cf2b8543d657087815a2f526"
  },
  {
    "keys": [
      "HS53"
    ],
    "source": "sources/external/root/retrieved/HS53.pdf",
    "locator": "ChapterIII Section4 Theorem2 and following m=1 remark, pp.129–130",
    "verification": "Opened full five-term transgression exact sequence for a group extension and its proof. Continuous Galois version is obtained by the explicitly explained filtered passage over finite quotients for finite images of continuous cochains. Applied with Galois-invariant E(L), not with a trivial-action replacement.",
    "status": "verified in the specified scope",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 17 November 2026",
    "sha256": "69a46088fb51ad5845871241124f55bb5c6c3baf0e24c736b73c4a7d76ccd7d4"
  },
  {
    "keys": [
      "Xiao91"
    ],
    "source": "sources/external/root/retrieved/Xiao91.pdf",
    "locator": "Section4, equation(4) and following two paragraphs, preprint p.21",
    "verification": "Opened algebraic elliptic fibration torsor/finite translating-twist identification and surjectivity of localization for nontrivial Jacobian. This verifies the geometric interpretation used in PUSH, together with the independently opened CDL exact sequence; no explicit equation for the selected torsor is inferred.",
    "status": "verified in the specified scope",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 17 November 2026",
    "sha256": "5b2d8287a1f18dc1e692d7e4548dc0ab487ac9405f6b420bb5ecf45b322e2889"
  },
  {
    "keys": [
      "Shioda90",
      "Shioda1990"
    ],
    "source": "sources/external/root/retrieved/Shioda90.pdf",
    "locator": "Assumption1.1; Theorem1.3; Theorem4.1; Theorems8.4,8.6 and table8.16; Proposition8.12 and equation8.25",
    "verification": "Opened original statements and height proofs: smooth projective relatively minimal elliptic surface, section, at least one singular fibre. The constructed surface satisfies them. Height is positive definite modulo torsion; I_n contributions and section intersections match the explicit matrix; NS/trivial-lattice quotient is MW, Pic0 comes from base, and finite extension multiplies heights by degree.",
    "status": "verified in the specified scope",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 17 November 2026",
    "sha256": "495a3efea5dd0466c5c9c3ae075d7dfbeb432b2cc5255edfe54885216eaea6aa"
  },
  {
    "keys": [
      "ViaclovskyTwo2026",
      "Viaclovsky2026Two",
      "VTwo26",
      "ViaTwo26push"
    ],
    "source": "sources/papers/arXiv_2609.33785_Viaclovsky_two_parameter_src/Viaclovsky_S6_September_26_2026.tex",
    "locator": "Section2 elliptic-surface input; Section3 Proposition3.1, equation3.1 and rank-one normalization proof; Proposition6.1 and full proof",
    "verification": "Opened y²=x³+tx+1, rank-one normalization P_E(O⊕L) with explicit central multipliers and boundary translation; canonical pencil K=f*O(−1). These are the precise changed-input comparisons in FAM A5.2; no tangent-cohomology or full classification theorem for that new model is imported.",
    "status": "verified in the specified scope",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 17 November 2026",
    "sha256": "11cb218c0d67fae857c2538cd259bb10988eb9bd6c65475fe616c2929845cd9c"
  },
  {
    "keys": [
      "OpenAIReasoning2026"
    ],
    "source": "https://developers.openai.com/api/docs/guides/reasoning",
    "locator": "Reasoning effort and Reasoning mode sections, lines1293–1324 of opened official page",
    "verification": "Official documentation explicitly separates reasoning mode from reasoning effort and says pro performs more model work. It does not support the requested universal statement that Pro mode is the highest-effort setting. Papers preserve recorded Pro mode while documenting this qualification; no unobserved API effort setting is inferred.",
    "status": "verified in the specified scope",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 17 November 2026"
  },
  {
    "keys": [
      "AnthropicEffort2026"
    ],
    "url": "https://platform.claude.com/docs/en/build-with-claude/effort",
    "status": "verified in specified scope",
    "opened_locators": "How effort works and Effort levels, lines127–145; model-specific paragraphs165–181 in opened web rendering.",
    "verification_scope": "The max effort level is the maximum capability setting with unrestricted token spending, supported by the two Claude models named in the historical reading record. This is effort-setting documentation, not evidence for mathematical correctness.",
    "own_check": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), effort Pro, 17 November 2026.",
    "web_refs": [
      "turn181view0",
      "turn181view1"
    ]
  },
  {
    "key": "CDP2020",
    "title": "The algebraic dimension of compact complex threefolds with vanishing second Betti number",
    "url": "https://www.cambridge.org/core/services/aop-cambridge-core/content/view/CDF2D04CFB35CEE105E10B188D97D68A/S0010437X19007802a.pdf/the-algebraic-dimension-of-compact-complex-threefolds-with-vanishing-second-betti-number.pdf",
    "status": "verified in the specified scope",
    "opened_locators": [
      "Published pp.680,684–685,692–694",
      "Theorem 2.2, Corollary 2.3, Proposition 2.4; Lemmas 4.2–4.3; §7 endpoint inference and Proposition 7.3 through its ruled-surface step"
    ],
    "uses": [
      "Working corrected global/relative criterion",
      "Correction note exact p.692 endpoint implication",
      "CDP A.4.2 constant genus-one family counterexample",
      "CDP D.1.1–D.1.3 coinvariant correction"
    ],
    "verification_scope": "Exact printed hypotheses and failed inferences opened. The original p.692 endpoint implication drops cotangent torsion. Proposition7.3 expressly permits constant normalized twists before concluding genus at least2. Lemma4.2 repeats the unsound direct-sum abelianization. No theorem-level refutation is inferred without the constructed global example.",
    "own_check": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), writing run; 17 November 2026 (Europe/Berlin)",
    "web_refs": [
      "turn23view0",
      "turn22search6"
    ],
    "local_pdf": "reference_downloads/cdp_audit/CDP2020.pdf",
    "sha256": "c4cb6408f97dec241d1d1e6f9cc30029f3d51272433717d0592a46ec501898b4",
    "download_status": "genuine PDF retained and opened in stated scope",
    "not_verified": [],
    "keys": [
      "CDP20",
      "CDP2020D",
      "CDP2020"
    ],
    "alias_basis": "Same original publication and DOI; all aliases share the exact opened scope, without broadening it."
  },
  {
    "key": "CDP1998",
    "title": "The algebraic dimension of compact complex threefolds with vanishing second Betti number",
    "url": "https://arxiv.org/pdf/math/9607215",
    "status": "verified in the specified scope",
    "opened_locators": [
      "arXiv:math/9607215v1, pp.11–12, Lemma5.2(1)–(3)"
    ],
    "uses": [
      "CDP D.1.1–D.1.2; working semidirect abelianization"
    ],
    "verification_scope": "The opened preprint numbers the published Lemma3.2 as Lemma5.2. Its proof explicitly passes from a split group extension to a direct sum with full H1(fibre). The published page numbering has not yet been independently checked in a journal scan.",
    "own_check": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), writing run; 17 November 2026 (Europe/Berlin)",
    "web_refs": [
      "turn23view1"
    ],
    "local_pdf": "reference_downloads/cdp_audit/CDP1998_preprint.pdf",
    "sha256": "7b7dbaf4e872e22ad7acbacc36ade6d67742bb226f37bfde0642a6a8d1852c78",
    "download_status": "downloaded",
    "not_verified": [],
    "keys": [
      "CDP98",
      "CDP1998"
    ],
    "alias_basis": "Same original publication; all aliases share the exact opened scope."
  },
  {
    "keys": [
      "AC2026",
      "AC26"
    ],
    "locator": "AC26, original PDF p.90, section10.5, Lemma10.7 and its complete proof",
    "source": "sources/original/AC26_original_manuscript.pdf",
    "opened_image": "sources/external/root/ac26_pages/page090.png",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), effort Pro, 17 November 2026 UTC",
    "status": "verified in the specified scope",
    "verification": "Original page visually opened; full lemma and proof read. For a split group extension, the correct abelianization is the direct sum of Q_ab and the Q-coinvariants of K_ab. The WB lemma is a re-derivation of this known formula, not a new result. The complete quotient proof is independently worded in work/root/semidirect_abelianization_rederivation.tex, with the normal subgroup, induced quotient maps and commutator quotient explicitly justified.",
    "source_proof_sha256": "9936b0004576135d92be9385c957d97630a06fcaf447cc302e31ad14e3f84090",
    "printed_rederivation_sha256": "2848a151b8d27a75cb498eaaae1878340e4449216aeafbf50b4f6561e8fcad38",
    "retention": "Every mathematical step of the WB quotient method is retained, with explicit AC26 credit. Its original text remains in the extracted provenance file; no AC26 prose is reproduced in the paper."
  }
]
```

### work/invariants_arithmetic/references_verified.json

```json
[
  {
    "citation_key": "AC2026",
    "status": "verified_for_stated_use",
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "opened_locator": "Attached original PDF: Remark 1.3 p.5; Proposition 7.27 pp.62–63; Theorem 9.1 pp.64–65; Proposition 9.11 pp.70–71; Lemma 9.12 pp.71–74; Proposition 9.13 pp.74–75; Remark 9.21 p.81; Theorem 10.5 pp.88–89; Proposition 10.8 pp.92–94. Also original PDF Theorem 5.4(iii) p.32 and its flat-character proof p.35; Theorem 9.1(vi) p.65; Proposition 9.20 p.80; Corollary 9.22 p.81. The original PDF, not the transcription, governs the comparison.",
    "actual_use": "Credit for construction, canonical pencil, structure-sheaf cohomology/direct images, cusp cup product, transgression factor twelve, Picard restriction injection and uniform fibrewise non-torsion. The precise full Hodge table and twisted tangent formulas require the later computations.",
    "hypotheses_and_normalization_check": "Original PDF controls transcription. Remark9.21 p.81 explicitly asserts that Omega^1_{X/B} has torsion along W union S1 union S2; its cusp clause is false by the complete local-module proof. Remark1.3 p.5 uses plural Omega^p and must be qualified by degree, since Omega² and Omega³ have nonzero cusp torsion. This corrects the original PDF itself, not merely its transcription. Scheme fibres include3S1 and4S2. Proposition7.27 leaves a common orientation sign, fixed by the family marking. Theorem10.5 gives nonzero R² for every twist and H² for general twists, not all precise jump multiplicities.",
    "citation_contexts": [
      {
        "file": "deliverables/work/invariants_arithmetic/sections/inv_part_A.tex",
        "line": 29,
        "context": "cheme fibres, including $3S_1$ and $4S_2$.\n\\end{proposition}\n\\begin{proof}\nWe derive the assertion from the local charts and the discriminant;\nthe same direct images are stated in Proposition 9.13 of\n\\citet{AC2026}, but that proposition is not an input to this proof.\nFlatness holds\nbecause a nonzero local parameter on the smooth base is a nonzero divisor\nin the "
      },
      {
        "file": "deliverables/work/invariants_arithmetic/sections/inv_part_A.tex",
        "line": 77,
        "context": "ers leaves\n$R^{-1}R_1^{-2}R_2^{-1}=R^{-12}$, so its coarse direct image is\n$\\OO_B(-1)$.  This supplies the degree used below independently of\nthe asserted direct-image or canonical-bundle formulas in \\citet{AC2026}.\n\nThe same base-change calculation identifies $\\gamma,u$ with a\nframe through the cusp.  At a multiple fibre finite pushforward and the\nReynolds proj"
      }
    ],
    "extent": "Original relevant statement and surrounding hypotheses opened; no claim that the entire external proof has been re-proved.",
    "local_source": "sources/original/AC26_original_manuscript.pdf",
    "source_sha256": "283bba102dd1d5dc346af81b28145bdaaea6654398d5032e76e97bafb9a858f2",
    "verified": true,
    "visual_check": "sources/audit_cache/inv_ari/literature/scans/AC26-81.png; original Remark9.21 visually reopened2026-11-17. The earlier audit-only faulty-transcription attribution is superseded."
  },
  {
    "citation_key": "Engel2026",
    "status": "verified_for_stated_use",
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "opened_locator": "S6.tex §1 lines235–280; §2 lines288–390; main-thm lines882–910; integral homology lines1617–1643; remarks1647–1725.",
    "actual_use": "Comparison of equivalent elliptic-surface construction, section height 1/6, line-bundle lift, sphere criterion, automorphism identity component and period signatures.",
    "hypotheses_and_normalization_check": "The introduction explicitly omits Dolbeault calculations. Do not credit E26 with the INV full Hodge/Bott–Chern table or exact twisted tangent jumps. Sphere criterion is |12 psi(a0+a1)|=1.",
    "citation_contexts": [],
    "extent": "Original relevant statement and surrounding hypotheses opened; no claim that the entire external proof has been re-proved.",
    "local_source": "sources/papers/arXiv_2609.38442_Engel_src/S6.tex",
    "source_sha256": "95ea78327c33351d609a3001539756f0043dfdef13a37a81927608c953c98c36",
    "verified": true
  },
  {
    "citation_key": "DuEtAl2026v1",
    "status": "verified_for_stated_use",
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "opened_locator": "v5oka_maps_modifications_deformations.tex intro lines300–345; Theorem6.12 (p2:thm:tangent-cohomology) lines9445–9487; Corollary6.13 lines9490ff.; Proposition6.16 (p2:prop:kuranishi-line) lines9876–9917; connected automorphisms lines9967–10010. Also §6: weighted-root-base lemma and proof lines8541–8614; root-stack-lift and proper-flat-root-fibration lines8628–8727; cusp-normalization-resolution and cusp-structure-cup lines8768–8877; vertical-log-bundle lines8897–9000; log-tangent-sequence lines9017–9048; structure-direct-images statement and relevant proof lines9154–9235,9275–9306; vertical/horizontal/log tangent calculation lines9312–9364. §7 intrinsic-fibration theorem and proof lines10018–10120. Theorem1.4 exact-period statement lines335–344.",
    "actual_use": "Credit for original-family tangent cohomology (1,1,1,0), nonzero parameter Kodaira–Spencer map, smooth reduced one-dimensional Kuranishi germ; original-family classification and automorphisms in Theorem1.4.",
    "hypotheses_and_normalization_check": "This is the historical first version. The exact statements are known-source duplicates of INV D1.3–D3.1/FAM A5.2; the printed explicit Koszul and gluing proofs are preserved. The second version omits these results, which alone is not a mathematical refutation.",
    "citation_contexts": [
      {
        "file": "deliverables/work/invariants_arithmetic/sections/inv_part_D.tex",
        "line": 879,
        "context": "e and re-derivation of the tangent theorem.}\nThe tangent cohomology $(1,1,1,0)$ and the smooth one-dimensional\nKuranishi germ are theorems of Du, Guo, Kusakabe, and Xie,\narXiv:2610.00250v1, Section~6 \\citep{DuEtAl2026v1}.\nThe invariant run re-derived these results after reading that paper.\nThe present proof prints the root-base calculation, its local\ncomparisons, and "
      }
    ],
    "extent": "Original relevant statement and surrounding hypotheses opened; no claim that the entire external proof has been re-proved.",
    "local_source": "sources/papers/arXiv_2610.00250v1_Du_Guo_Kusakabe_Xie_src/v5oka_maps_modifications_deformations.tex",
    "source_sha256": "924a4a72d80793927f3104121a44786ea2b9869ae6ea2bca5a6a69553ab2884e",
    "verified": true
  },
  {
    "citation_key": "DuEtAl2026v2",
    "status": "verified_for_stated_use",
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "opened_locator": "submited-tams.tex introduction lines312–320 and whole-file searches for tangent/Kuranishi/classification; section inventory.",
    "actual_use": "Version comparison for scope of Oka construction, maps and point-deletion results.",
    "hypotheses_and_normalization_check": "The relevant deformation and global parameter-classification assertions of v1 are absent. Do not cite v2 as a proof of the v1 tangent theorem.",
    "citation_contexts": [
      {
        "file": "deliverables/work/invariants_arithmetic/sections/inv_part_D.tex",
        "line": 883,
        "context": " re-derived these results after reading that paper.\nThe present proof prints the root-base calculation, its local\ncomparisons, and the additional coarse direct images and all Picard\ntwists. Version~2 \\citep{DuEtAl2026v2} does not contain the deformation\nsection; this does not alter the credit for the version~1 theorems.\n"
      }
    ],
    "extent": "Original relevant statement and surrounding hypotheses opened; no claim that the entire external proof has been re-proved.",
    "local_source": "sources/papers/arXiv_2610.00250v2_Du_Guo_Kusakabe_Xie_src/submited-tams.tex",
    "source_sha256": "a2013b8390b1eba4f9c57eb78597eb3b8b6ac09c50714492c6912803a8bebe50",
    "verified": true
  },
  {
    "citation_key": "Yang2026",
    "status": "verified_for_stated_use",
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "opened_locator": "Compact_Complex_Threefolds_REPAIRED_v4_5.tex main statements lines174–205,207ff.,249–261,320ff.",
    "actual_use": "Compare B(4,6), C(3,6) rational-homology families, r cusp components, fundamental groups and affine deformation/period statements.",
    "hypotheses_and_normalization_check": "These are different finite filling types. Their Hodge/rational Betti statements must not be substituted for the original AC26 family. Detailed Lemmas6.6–6.9/Proposition6.15 centralizer transfer still requires its separate root-owned application check.",
    "citation_contexts": [],
    "extent": "Original relevant statement and surrounding hypotheses opened; no claim that the entire external proof has been re-proved.",
    "local_source": "sources/papers/arXiv_2609.29666_Yang_src/Compact_Complex_Threefolds_REPAIRED_v4_5.tex",
    "source_sha256": "5061ce4e6cda8ed7ba3bb2a7a597d50e018bfd53fb9e49e7b38317f628c332a5",
    "verified": true
  },
  {
    "citation_key": "Wang2026",
    "status": "verified_for_stated_use",
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "opened_locator": "order_two_rational_homology_sphere_new.tex main statement lines99ff.,775ff.; Prop2.4 init:open lines218ff.; specialization/filling propositions375ff.,499ff.",
    "actual_use": "Compare order-two rational homology sphere, contracting quotient construction, and finite filling mechanism.",
    "hypotheses_and_normalization_check": "Curve configuration IV*, I2, I1, I1 with P(t)=(1,sqrt(2)t); H2/H3=Z/2 and simple connectivity. These results are not a proof of the original full Hodge/tangent computation.",
    "citation_contexts": [],
    "extent": "Original relevant statement and surrounding hypotheses opened; no claim that the entire external proof has been re-proved.",
    "local_source": "sources/papers/arXiv_2609.11541_Wang_src/order_two_rational_homology_sphere_new.tex",
    "source_sha256": "1ae1686d7ebb4e538c0aee38adce5643b3e51fe955ed6796e0cfc61cc6cf9c29",
    "verified": true
  },
  {
    "citation_key": "ViaclovskyLog2026",
    "status": "verified_for_stated_use",
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "opened_locator": "Logarithmic_S6_October_28_2026_Final.tex main theorem lines219–229; questions233–250; simply-connected theorem606ff.",
    "actual_use": "Credit for logarithmic transformation sphere families with coprime 3k,4l and invariance of those multiplicities; compare generalized INV B canonical calculations.",
    "hypotheses_and_normalization_check": "The source asserts positive Kuranishi dimension and asks for exact deformation dimension/miniversality. It does not supply the INV exact tangent theorem for every generalized pair.",
    "citation_contexts": [
      {
        "file": "deliverables/work/invariants_arithmetic/sections/inv_part_B.tex",
        "line": 175,
        "context": "cities and the anticanonical ring}\n\n\\begin{proposition}[INV B2.1; Proved: Canonical bundles for all coprime multiplicities]\\label{inv:B2.1}\nLet $X=X_{3k,4l}(u)$ with admissible translation data as in\n\\citet[Theorem 1.1 and Proposition 2.3]{ViaclovskyLog2026},\n$\\gcd(3k,4l)=1$, and any nonzero $u$ in its construction domain.\nThen\n\\[\nK_X=f^*\\OO_B(-1)\\otimes\n\\OO_X\\bigl((k-1)S_1+(3l-1)S_2\\bigr).\n\\]\nMoreover $("
      }
    ],
    "extent": "Original relevant statement and surrounding hypotheses opened; no claim that the entire external proof has been re-proved.",
    "local_source": "sources/papers/arXiv_2610.39102_Viaclovsky_log_transformations_src/Logarithmic_S6_October_28_2026_Final.tex",
    "source_sha256": "de895f47e8c416b91cfe78d0578b138e44a17ae95050c03a502c37dc264cefbf",
    "verified": true
  },
  {
    "citation_key": "ViaclovskyTwoParameter2026",
    "status": "verified_for_stated_use",
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "opened_locator": "Viaclovsky_S6_September_26_2026.tex main theorem256ff.; canonical/algebraic-dimension proposition1339ff.; cohomology lines1433–1470.",
    "actual_use": "Compare two-parameter III*,I1^3 construction and structure-sheaf Hodge numbers.",
    "hypotheses_and_normalization_check": "The source computes h0q=(1,1,0,0) and explicitly leaves remaining Hodge numbers open; no full-table credit.",
    "citation_contexts": [],
    "extent": "Original relevant statement and surrounding hypotheses opened; no claim that the entire external proof has been re-proved.",
    "local_source": "sources/papers/arXiv_2609.33785_Viaclovsky_two_parameter_src/Viaclovsky_S6_September_26_2026.tex",
    "source_sha256": "11cb218c0d67fae857c2538cd259bb10988eb9bd6c65475fe616c2929845cd9c",
    "verified": true
  },
  {
    "citation_key": "ViaclovskyCombs2026",
    "status": "verified_for_stated_use",
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "opened_locator": "Viaclovsky_Comb_S6_Draft_October_7_2026.tex main theorem236–260; general flat-torus cohomology theorems418ff.,490ff.; original-family Hodge proposition2430ff.; comb cohomology2471ff.; questions2695ff.",
    "actual_use": "Credit for comb families h01=2m+1, h02=2m, h03=0 and lower deformation bound; general direct-image local-freeness and cup-product results.",
    "hypotheses_and_normalization_check": "m>=12 in the construction theorem; deformation lower bound 8m−8 is not an exact dimension. CDP agent owns INV E application and full comb proof dependency audit.",
    "citation_contexts": [],
    "extent": "Original relevant statement and surrounding hypotheses opened; no claim that the entire external proof has been re-proved.",
    "local_source": "sources/papers/arXiv_2610.10451_Viaclovsky_combs_src/Viaclovsky_Comb_S6_Draft_October_7_2026.tex",
    "source_sha256": "42dea62b023dfb75a009a8c83c15349ddc8f853162f753e3547ca583d07b74d5",
    "verified": true
  },
  {
    "citation_key": "LiuRollenske2026",
    "status": "verified_for_stated_use",
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "opened_locator": "S6_arxiv.tex theorem and proof lines1702–1728; Remark1729ff.; following begin{comment} block explicitly excluded.",
    "actual_use": "Credit for distinct sphere construction and singular-fibre distinction.",
    "hypotheses_and_normalization_check": "Remark leaves canonical/Hodge invariants for later. Unpublished commented calculations after line1732 are not theorem assertions or proof sources.",
    "citation_contexts": [],
    "extent": "Original relevant statement and surrounding hypotheses opened; no claim that the entire external proof has been re-proved.",
    "local_source": "sources/papers/arXiv_2609.33826_Liu_Rollenske_src/S6_arxiv.tex",
    "source_sha256": "d3cdd5ffbd84d03ea0180988a92e4c0627b76cc47dc9375365e61c8dcc4d377e",
    "verified": true
  },
  {
    "citation_key": "McHugh2018",
    "status": "verified_for_stated_use",
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "opened_locator": "BCA-FonCmpctCmplx3flds-111518.tex lines600–810: Theorem6.3, Proposition6.4, hBC22 formula and §7.1.",
    "actual_use": "Independent derivation of the Bott–Chern dimension table in INV C2.2 and the working edition.",
    "hypotheses_and_normalization_check": "Compact complex threefold; substitute b1=b2=0, h20=h02=0, E2^{3,1}=0 and the relevant k^{p,q}=0. The latter vanishing is established from the actual Betti data, not assumed from a generally false injection.",
    "citation_contexts": [
      {
        "file": "deliverables/work/invariants_arithmetic/sections/inv_part_C.tex",
        "line": 204,
        "context": "oming differential and a closed corner of a square\nis in both images.  Thus $k^{p,q}=0$ for $0<p+q<6$.\nAlso $E_2^{3,1}=0$ by C1.1 and $H^{1,1}(X;\\R)=0$ because\n$H^2(X;\\R)=0$.  Reading the formulas in\n\\citet[Theorem 6.3, Proposition 6.4, (7), pp. 20--25]{McHugh2018}\ntherefore gives\n\\[\nh_{BC}^{1,1}=2h^{0,1}=2,\\qquad\nh_{BC}^{1,2}=h^{1,2}=h,\\qquad\nh_{BC}^{2,2}=-1+(h+1)+h=2h.\n\\]\nThe remaining entries in his table are"
      }
    ],
    "extent": "Original relevant statement and surrounding hypotheses opened; no claim that the entire external proof has been re-proved.",
    "local_source": "sources/papers/arXiv_1708.03251_src/BCA-FonCmpctCmplx3flds-111518.tex",
    "source_sha256": "7117356d0c724c128bb0be980e1f9a01000f459124879b3a34d47b5af9d6392e",
    "verified": true
  },
  {
    "citation_key": "Angella2018",
    "status": "verified_for_stated_use",
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "opened_locator": "angella-5-final.tex §4 lines975–1155, including the complex-six-sphere Bott–Chern calculations and Schweitzer duality.",
    "actual_use": "Independent known-source Bott–Chern formulas specialized to the computed Hodge numbers.",
    "hypotheses_and_normalization_check": "Conditional general formulas for a complex structure on S6; the input Hodge numbers come from INV A, not from this external article.",
    "citation_contexts": [
      {
        "file": "deliverables/work/invariants_arithmetic/sections/inv_part_C.tex",
        "line": 213,
        "context": "ives\n\\[\nh_{BC}^{1,1}=2h^{0,1}=2,\\qquad\nh_{BC}^{1,2}=h^{1,2}=h,\\qquad\nh_{BC}^{2,2}=-1+(h+1)+h=2h.\n\\]\nThe remaining entries in his table are precisely the boundary entries\nof \\eqref{inv:eq:C-BC-A}.  In\n\\citet[Section 4, pp. 13--16]{Angella2018}, the relation\n\\[\nh_{BC}^{2,2}=2h_{BC}^{2,1}-2h^{0,1}+2\n\\]\ngives $2h$, and the boundary values reduce to those above because\n$h^{2,0}=h^{0,2}=0$.  Thi"
      }
    ],
    "extent": "Original relevant statement and surrounding hypotheses opened; no claim that the entire external proof has been re-proved.",
    "local_source": "sources/papers/arXiv_1705.10518_src/angella-5-final.tex",
    "source_sha256": "7cb4fefe5fb37557b56c5b89854eb799252433928e97bbaa8fdc405f45cc28d6",
    "verified": true
  },
  {
    "citation_key": "huber2022",
    "status": "verified_for_stated_use",
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "opened_locator": "gesamt-ams.tex lines2138–2205, Theorem6.1 (analytic subgroup theorem), refined annihilator formulation and proof.",
    "actual_use": "Transcendence of the compact slope via non-splitting of the universal vector extension; limits of exponential arguments in C7.7/C7.9/C7.11.",
    "hypotheses_and_normalization_check": "Connected commutative algebraic group over Qbar; an algebraic Lie subspace containing a logarithm of a nonzero algebraic point forces an algebraic subgroup. The actual subspace must be algebraic: the real compact slope is not silently treated as algebraic.",
    "citation_contexts": [
      {
        "file": "deliverables/work/invariants_arithmetic/sections/ari_diagonal_obstruction.tex",
        "line": 103,
        "context": "riod\n$\\omega_1(1,c)$ by a sufficiently large positive integer\ngives a vector in $\\ell_c$ whose exponential is a nonzero\ntorsion point of $G_Q$, hence an algebraic point. The\nanalytic subgroup theorem\n\\citep[Theorem 6.1]{huber2022} supplies a positive-dimensional\nconnected algebraic subgroup with Lie algebra contained in\n$\\ell_c$. Its dimension is one, and its projection to $E$\n"
      },
      {
        "file": "deliverables/work/invariants_arithmetic/sections/ari_complexified.tex",
        "line": 141,
        "context": "extension of $E$ would lie on the algebraic\nline of slope $s_2+k$. Dividing this period by a sufficiently\nlarge integer supplies a nonzero algebraic torsion exponential.\nThe analytic subgroup theorem\n\\citep[Theorem 6.1]{huber2022} would give a one-dimensional\nalgebraic subgroup with that Lie line. Its projection to $E$\nis nonzero, so it is an elliptic curve isogenous to $E$ and"
      },
      {
        "file": "deliverables/work/invariants_arithmetic/sections/ari_cm_transcendence.tex",
        "line": 120,
        "context": "algebraic. Therefore\n$\\sigma(u)e^{-u\\zeta(u)/2}$ is transcendental, as also stated\nexplicitly after Corollary 1 of the cited paper.\n\nFor the second assertion we apply the analytic subgroup theorem\nin \\citet[Theorem 6.1]{huber2022}. In the algebraic universal\nvector extension $\\widetilde E$ a logarithm of an algebraic lift\nof $P$ has coordinates $(u,\\zeta(u)-b)$, where $b$ is an"
      }
    ],
    "extent": "Original relevant statement and surrounding hypotheses opened; no claim that the entire external proof has been re-proved.",
    "local_source": "sources/papers/arXiv_1805.10104_Huber_Wuestholz_src/gesamt-ams.tex",
    "source_sha256": "66e182fd9973e070a826624d7d49e5370fad9b462f7e8664a573da903f11e2d1",
    "web_open_locator": "turn32view1",
    "verified": true
  },
  {
    "citation_key": "bertolin2022",
    "status": "verified_for_stated_use",
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "opened_locator": "SemiAbelianTowers-final.tex Construction3.4 and Lemma3.5 lines580–658; remaining detailed period-conjecture case references tracked separately. Also Definitions2.3–2.4 and semi-abelian exponential lines375–458; Proposition4.12 and Remark4.13 lines971–1005; Section6.1 elliptic Weil bracket lines1276–1365; corrected Table2 lines1403–1452.",
    "actual_use": "Mumford–Tate unipotent dimensions for the 1-motive and explicit diagonal bracket calculation.",
    "hypotheses_and_normalization_check": "Base field algebraically closed. B is the smallest abelian subvariety containing the point/extension data, Z includes bracket image plus the remaining torus point; dim UR=2dim B+dim Z. C7.4 stays conditional on the stated period conjecture. The generalized logarithm includes first-, second- and third-kind coordinates and depends on a path modulo the specified periods. Proposition4.12 is conditional on the Generalized Period conjecture; the P=Q specialization is Remark4.13. The corrected dependent nondeficient row has unipotent dimension3 and total dimensions5(CM),7(non-CM), matching the explicitly nonzero diagonal bracket 2 psi in C.7.3.",
    "citation_contexts": [
      {
        "file": "deliverables/work/invariants_arithmetic/sections/ari_periods.tex",
        "line": 83,
        "context": "$1$-motive. This also avoids treating an integral with an endpoint\nat a residue pole as an unregularized ordinary integral.\nThe description agrees with the generalized logarithm and\nSerre function in \\citet[Definitions 2.3--2.4 and\nSection 6]{bertolin2022}; the signs in\n\\eqref{ari:eq:cp-periods} are for the exponential rather than the\nquasi-periods of $f_u$ itself.\n\\end{proof}\n\n\\begin{proposition}[ARI C"
      },
      {
        "file": "deliverables/work/invariants_arithmetic/sections/ari_periods.tex",
        "line": 147,
        "context": "ity assertion about its theta value.\n\\end{proof}\n\n\\subsection{The conditional theorem and its exact conjectural input}\n\nWe use Grothendieck's period conjecture in the form stated as\nConjecture 1.1 of \\citet{bertolin2022}: for a motive $M$ over\n$\\overline\\Q$, the field generated by its periods over\n$\\overline\\Q$ has transcendence degree $\\dim G_{\\mathrm{mot}}(M)$.\nOnly"
      },
      {
        "file": "deliverables/work/invariants_arithmetic/sections/ari_periods.tex",
        "line": 257,
        "context": " $N(P_t)$ is transcendental.\nMore generally the conclusion holds for every nontorsion\nalgebraic point on an elliptic curve over $\\overline\\Q$.\nThe weaker named Relative Semi-abelian Conjecture 4.7 of\n\\citet{bertolin2022}, restricted to the groups and algebraic\nlifts used in this proof, already suffices.\n\\end{proposition}\n\\begin{proof}\nSuppose $N(P)$ is algebraic. Stat"
      },
      {
        "file": "deliverables/work/invariants_arithmetic/sections/ari_periods.tex",
        "line": 280,
        "context": "ds, $2\\pi i$, and\n$\\kappa_j=\\zeta(u)\\omega_j-\\eta_j u$; the determinant of\nthe two equations for $u,\\zeta(u)$ is, up to sign,\n$\\omega_1\\eta_2-\\omega_2\\eta_1= -2\\pi i$.\nThis is also the observation of \\citet[Remark 4.13]{bertolin2022}.\nThe real-linear expression for $\\eta(u)$ is\n\\begin{equation}\\label{ari:eq:cp-real-linear}\n \\eta(u)=\n \\frac{(u\\bar\\omega_2-\\bar u\\omega_2)\\eta_1\n    "
      }
    ],
    "extent": "Original relevant statement and surrounding hypotheses opened; no claim that the entire external proof has been re-proved.",
    "local_source": "sources/papers/arXiv_2010.15170_Bertolin_Philippon_Saha_Saha_src/SemiAbelianTowers-final.tex",
    "source_sha256": "543afa029adf0e90b94cd387ea22d79f309520dc3b9cef49fc456863078400c8",
    "web_open_locator": "turn32view0",
    "verified": true
  },
  {
    "citation_key": "demarco2017",
    "status": "verified_for_stated_use",
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "opened_locator": "VCHequidistribution_arxiv_v_2.tex Theorem1.1/Corollary1.2 lines142–172; local heights/divisor degree/continuity lines237–311.",
    "actual_use": "Local-height measure and small-height equidistribution, including C8.10.",
    "hypotheses_and_normalization_check": "Nonrepeating Galois orbits of small points; generic height positive. Height normalization is relative to (O), so the measure has mass1/12 and 12m_P is the probability measure. No additional isotriviality hypothesis is inserted.",
    "citation_contexts": [
      {
        "file": "deliverables/work/invariants_arithmetic/sections/ari_heights.tex",
        "line": 58,
        "context": "he canonical N\\'eron function.\nIts normalization is uniquely determined by continuity away from\n$O$, its logarithmic pole at $O$, and the multiplication law.\nThese are the three properties printed in\n\\citet[Section 2.1]{demarco2017}; their duplication law includes\nthe discriminant term $\\frac14\\log|\\Delta|_v$.\nUnder a coordinate scaling the changes in the sigma or formal\nparamete"
      },
      {
        "file": "deliverables/work/invariants_arithmetic/sections/ari_heights.tex",
        "line": 283,
        "context": "ular. Its height contribution is $1/12$.\nAt all other function-field places the point is integral\nand the discriminant is a unit. This proves\n$D_P=(\\infty)/12$ and the generic height.\n\nTheorem 1.1 of \\citet{demarco2017} applies with $K=\\Q$,\n$B=\\mathbb P^1$, the displayed elliptic surface and rational\nsection, since the generic height is positive. It equips\nthis divis"
      },
      {
        "file": "deliverables/work/invariants_arithmetic/sections/ari_heights.tex",
        "line": 326,
        "context": "e slide~21 states the uniform\ncanonical-versus-Weil-height bound in terms of the base height.\nFor our explicit bounded remainder and local normalization, the\nfully opened Theorems~1.1, 2.2 and 2.3 of\n\\citet{demarco2017}, applied above, remain the cited proof.\n\\end{proof}\n\n\\begin{proposition}[ARI C.6.5; Proved: rigorous high-precision height enclosures]\\label{ari:C.6."
      },
      {
        "file": "deliverables/work/invariants_arithmetic/sections/ari_measure.tex",
        "line": 126,
        "context": "parameters, their Galois-orbit probability measures likewise\nconverge to $12m_P$. Thus the probability-limit assertion\nin Lead 15(b) requires the factor $12$.\n\\end{proposition}\n\\begin{proof}\nWe apply \\citet[Theorem 1.1 and Corollary 1.2]{demarco2017}.\nTheir hypotheses are a number field, a smooth projective\nbase curve, an elliptic surface and a rational section of\nnonzero generic canonical height."
      }
    ],
    "extent": "Original relevant statement and surrounding hypotheses opened; no claim that the entire external proof has been re-proved.",
    "local_source": "sources/papers/arXiv_1701.07947_DeMarco_Mavraki_src/VCHequidistribution_arxiv_v_2.tex",
    "source_sha256": "141cb2a0751fdd4a4e39c093d57f2a1872682d5f7d71fc42fbde1401caa228be",
    "web_open_locator": "turn27view2",
    "verified": true
  },
  {
    "citation_key": "DukeImamoglu2008",
    "status": "verified_for_stated_use",
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "opened_locator": "Original attached PDF, Theorem1 p.2 and formula(6) p.4.",
    "actual_use": "Explicit zero of the Weierstrass function in INV A2.3.",
    "hypotheses_and_normalization_check": "The branch used in the family is mu=1−z0. Period and hypergeometric normalizations checked; zero replacement is not a pole.",
    "citation_contexts": [
      {
        "file": "deliverables/work/invariants_arithmetic/sections/inv_part_A.tex",
        "line": 649,
        "context": "ord-and-tangent formulas is included in the exact computation log.\nThis proves $\\wp(\\mu,\\tau)=0$.\n\nWe checked the original theorem on page 399 of\n\\citet{EichlerZagier1982}, as well as equation (6) of\n\\citet{DukeImamoglu2008}.  With the normalized $\\Delta$, their\ncoefficient is indeed $144\\pi i\\sqrt6$, their constant is\n$\\log(5+2\\sqrt6)/(2\\pi i)$, and the integrand is\n$(\\s"
      },
      {
        "file": "deliverables/work/invariants_arithmetic/sections/ari_critical.tex",
        "line": 9,
        "context": " $\\mu$ do not affect any expression below. We use\nEichler and Zagier's unnumbered theorem on p.~399 of\n\\cite{EichlerZagier1982}, also stated as equation (6) and the\nunnumbered theorem in Section~2 of \\cite{DukeImamoglu2008}.\nFor the cusp branch in this problem their theorem says\n\\begin{equation}\\label{ari:eq:cc-EZ}\n \\begin{aligned}\n \\mu&=\\frac12-i\\beta_{\\rm cusp}-\n      "
      }
    ],
    "extent": "Original relevant statement and surrounding hypotheses opened; no claim that the entire external proof has been re-proved.",
    "local_source": "sources/papers/Duke_Imamoglu_zeros_of_Weierstrass_p.pdf",
    "source_sha256": "c06a396561cf2c79469436693b821282047c0411fdb14a08a6f32a7adab046f9",
    "verified": true
  },
  {
    "citation_key": "EichlerZagier1982",
    "status": "verified_for_stated_use",
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "opened_locator": "Original author-hosted scan, pp.399–403, zero formula and its normalizations.",
    "actual_use": "Independent Weierstrass zero formula, modular determinant constants and chosen branch.",
    "hypotheses_and_normalization_check": "Matched the article lattice/eta conventions to mu=1−z0 and the family marking; no phase inferred from absolute values.",
    "citation_contexts": [
      {
        "file": "deliverables/work/invariants_arithmetic/sections/inv_part_A.tex",
        "line": 648,
        "context": "Inverting the displayed $E_6$ Cartan matrix and the\nchord-and-tangent formulas is included in the exact computation log.\nThis proves $\\wp(\\mu,\\tau)=0$.\n\nWe checked the original theorem on page 399 of\n\\citet{EichlerZagier1982}, as well as equation (6) of\n\\citet{DukeImamoglu2008}.  With the normalized $\\Delta$, their\ncoefficient is indeed $144\\pi i\\sqrt6$, their constant is\n"
      },
      {
        "file": "deliverables/work/invariants_arithmetic/sections/ari_critical.tex",
        "line": 8,
        "context": "u(\\tau),\\tau)$, where\n$t=j(\\tau)/1728$ and $\\wp_\\tau(\\mu)=0$. The sign and lattice\ntranslation of $\\mu$ do not affect any expression below. We use\nEichler and Zagier's unnumbered theorem on p.~399 of\n\\cite{EichlerZagier1982}, also stated as equation (6) and the\nunnumbered theorem in Section~2 of \\cite{DukeImamoglu2008}.\nFor the cusp branch in this problem their theorem sa"
      }
    ],
    "extent": "Original relevant statement and surrounding hypotheses opened; no claim that the entire external proof has been re-proved.",
    "web_open_locator": "turn5view0; turn7view2",
    "verified": true
  },
  {
    "citation_key": "Stelzig2021",
    "status": "verified_for_stated_use",
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "opened_locator": "Original arXiv1812.00865v3, Theorem A (=Theorem3), p.2; bounded double-complex decomposition.",
    "actual_use": "Square/zigzag decomposition for INV C2.1.",
    "hypotheses_and_normalization_check": "Bounded double complex over a field; vector spaces need not be finite-dimensional. Infinite cardinal square multiplicities are allowed, while the finite cohomological summands are counted separately.",
    "citation_contexts": [
      {
        "file": "deliverables/work/invariants_arithmetic/sections/inv_part_C.tex",
        "line": 134,
        "context": "ch's numerical tables.  The totals are\n$(1,0,2,2,2,2,1)$ and $(1,2,2,2,2,0,1)$, respectively.\n\\end{proposition}\n\\begin{proof}\nWe apply the structure theorem for bounded double complexes over a\nfield, \\citet[Theorem 3]{Stelzig2021}, to the actual algebraic double\ncomplex $(A^{\\bullet,\\bullet}(X),\\partial,\\bar\\partial)$.\nThe word bounded refers to the bidegrees, not to the dimens"
      },
      {
        "file": "deliverables/work/invariants_arithmetic/sections/inv_part_C.tex",
        "line": 162,
        "context": ",1)&h\\\\\n(1,2)&(2,2)&h\\\\\n(2,2)&(3,2)&1.\n\\end{array}\n\\end{equation}\nThe vertical arrows are their reflections in $p=q$, with the same\nmultiplicities.  The correspondence with spectral-sequence ranks is\n\\citet[Proposition 6(1)]{Stelzig2021}; alternatively one computes\ncolumn cohomology on each horizontal arrow directly.\n\nWe now evaluate the displayed definitions, rather than use a formul"
      }
    ],
    "extent": "Original relevant statement and surrounding hypotheses opened; no claim that the entire external proof has been re-proved.",
    "url": "https://arxiv.org/pdf/1812.00865v3",
    "web_open_locator": "turn7view0",
    "verified": true
  },
  {
    "citation_key": "Gauduchon1985",
    "status": "verified_for_stated_use",
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "opened_locator": "Original eight-page paper, Theorem2 pp.132–133.",
    "actual_use": "Existence/uniqueness up to scale of Gauduchon conformal representative.",
    "hypotheses_and_normalization_check": "Compact connected complex manifold of dimension at least2; the actual manifold has dimension3. This is not a Kähler assertion.",
    "citation_contexts": [
      {
        "file": "deliverables/work/invariants_arithmetic/sections/inv_part_C.tex",
        "line": 531,
        "context": "quation}\nThis Ricci form is semipositive and has rank one at regular points\nof $f$.  No Chern--Ricci-flat Hermitian metric exists on $X$.\n\\end{proposition}\n\\begin{proof}\nGauduchon's conformal theorem\n\\citep[Theorem 2, pp. 132--133]{Gauduchon1985} applies to the compact\nconnected complex manifold $X$.  In complex dimension three, it\nproduces a positive conformal multiple $\\omega_0$ of any Hermi"
      }
    ],
    "extent": "Original relevant statement and surrounding hypotheses opened; no claim that the entire external proof has been re-proved.",
    "web_open_locator": "turn16view1; turn17view0",
    "verified": true
  },
  {
    "citation_key": "STW2017",
    "status": "verified_for_stated_use",
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "opened_locator": "Original arXiv1503.04491v2, Theorem1.3 p.3.",
    "actual_use": "Prescribed Chern–Ricci form in a fixed Gauduchon Aeppli class in INV C3.6.",
    "hypotheses_and_normalization_check": "Real Bott–Chern representative of c1BC, compact Hermitian manifold with Gauduchon initial form. The nonzero c1BC excludes a Ricci-flat representative.",
    "citation_contexts": [
      {
        "file": "deliverables/work/invariants_arithmetic/sections/inv_part_C.tex",
        "line": 553,
        "context": "e use the conventional unnormalized\nChern--Ricci form $-i\\partial\\bar\\partial\\log\\det g$,\nwhich represents $2\\pi c_{1,BC}(T_X)$.  Thus the real closed form\n$\\pi\\theta$ represents its class.  Applying\n\\citet[Theorem 1.3]{STW2017} with background $\\omega_0$ and prescribed\nform $\\pi\\theta$ proves \\eqref{inv:eq:C-Ricci} and preservation of the\nAeppli class.  Finally C3.1 shows $["
      }
    ],
    "extent": "Original relevant statement and surrounding hypotheses opened; no claim that the entire external proof has been re-proved.",
    "url": "https://arxiv.org/pdf/1503.04491v2",
    "web_open_locator": "turn5view2",
    "verified": true
  },
  {
    "citation_key": "BourdonClarkStankewicz2017",
    "status": "verified_for_stated_use",
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "opened_locator": "Original arXiv1411.2742v3, Theorem4.15 p.23.",
    "actual_use": "Rational CM torsion possibilities for all orders in ARI C5.1.",
    "hypotheses_and_normalization_check": "The field is Q(j), including nonmaximal CM orders. Applied with rational j, so no maximal-order-only restriction is silently ignored.",
    "citation_contexts": [
      {
        "file": "deliverables/work/invariants_arithmetic/sections/ari_special.tex",
        "line": 776,
        "context": "ders $3,4$, respectively, the\nlimiting points have orders $3,2$. Thus these are the only CM\ntorsion points on the completed family.\n\\end{proposition}\n\\begin{proof}\nThe precise torsion theorem used is \\cite{BourdonClarkStankewicz2017},\nTheorem 4.15(a), on page 23 of arXiv:1411.2742v3:\nfor an elliptic curve $E/F$ with CM by any imaginary quadratic order,\n\\[\n F=\\mathbb Q(j(E))\\quad\\L"
      }
    ],
    "extent": "Original relevant statement and surrounding hypotheses opened; no claim that the entire external proof has been re-proved.",
    "url": "https://arxiv.org/pdf/1411.2742v3",
    "web_open_locator": "turn25view0;turn26view0",
    "verified": true
  },
  {
    "citation_key": "Sutherland2023CM",
    "status": "verified_for_stated_use",
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "opened_locator": "MIT18.783 Lecture20, Theorem20.12 and Corollary20.13 p.6.",
    "actual_use": "Algebraic integrality of CM j for arbitrary orders and class-polynomial route.",
    "hypotheses_and_normalization_check": "Theorem covers orders, not merely maximal rings. Rational algebraic integer j is integral; finite class-number-one enumeration is separately rerun.",
    "citation_contexts": [
      {
        "file": "deliverables/work/invariants_arithmetic/sections/ari_special.tex",
        "line": 806,
        "context": "ucible over $\\mathbb Q$, and its coefficients are not\nintegers. Neither root is an algebraic integer. By the integrality\ntheorem for singular moduli (for example, Theorem 20.12 and\nCorollary 20.13 of \\cite{Sutherland2023CM}, proved there for all\nimaginary quadratic orders), this excludes complex multiplication\nin every remaining case. The required hypothesis is simply th"
      }
    ],
    "extent": "Original relevant statement and surrounding hypotheses opened; no claim that the entire external proof has been re-proved.",
    "url": "https://math.mit.edu/classes/18.783/2023/LectureNotes20.pdf",
    "web_open_locator": "turn25view1;turn26view1;turn27view1",
    "verified": true
  },
  {
    "citation_key": "Shin2015",
    "status": "verified_for_stated_use",
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "opened_locator": "Original arXiv1009.2253v6, definition p.1, Remark2.2 p.3, Proposition2.3(ii),(iii) pp.3–4.",
    "actual_use": "Siegel-function multipliers and modular-unit normalization in C4.1.",
    "hypotheses_and_normalization_check": "g_a transformation under T, S and lattice translation matched exactly; power12N removes multipliers under the stated congruence group. Local-height zero-mean constant checked independently.",
    "citation_contexts": [
      {
        "file": "deliverables/work/invariants_arithmetic/sections/ari_special.tex",
        "line": 490,
        "context": "proposition}\n\\begin{proof}\nDividing the two product expressions gives the first identity exactly,\nincluding the factor $i$. Its absolute value is the asserted norm.\nThis agrees with the convention in \\cite{Shin2015}, equation (1).\nFor completeness the transformation argument needed here can be\nchecked directly. For $T:\\tau\\mapsto\\tau+1$ and\n$S:\\tau\\mapsto-1/\\tau$"
      },
      {
        "file": "deliverables/work/invariants_arithmetic/sections/ari_special.tex",
        "line": 505,
        "context": "a+b}}{g_a}\n =\\exp\\bigl(\\pi i(a_1b_2-a_2b_1+b_1b_2+b_1+b_2)\\bigr).\n\\]\nThese follow from the two Jacobi transformations and the lattice\ntranslations. They are the cases of Proposition 2.3(ii)--(iii) of\n\\cite{Shin2015} used here. The multipliers on $\\Gamma(n)$ are killed\nby $12n$. The product gives a Laurent series in $q^{1/n}$ with\ncoefficients in $\\mathbb Q(\\zeta_"
      }
    ],
    "extent": "Original relevant statement and surrounding hypotheses opened; no claim that the entire external proof has been re-proved.",
    "url": "https://arxiv.org/pdf/1009.2253v6",
    "web_open_locator": "turn25view2;turn27view0",
    "verified": true
  },
  {
    "citation_key": "Schnell19",
    "status": "verified_for_stated_use",
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "opened_locator": "Lecture4 (February6), Theorem4.1 p.1; equation4.3 and Cases1–2 p.2; Theorem4.4 and quotient statement p.3.",
    "actual_use": "Appell–Humbert classification, nonnegative Hermitian form for an effective line bundle, pullback of an ample bundle from a quotient, Riemann projectivity criterion.",
    "hypotheses_and_normalization_check": "Compact complex torus V/Lambda; integral imaginary Hermitian form and semicharacter. A nonzero section excludes negative directions, forces semicharacter trivial on the null lattice, and descends to the quotient; positivity there proves ampleness.",
    "citation_contexts": [],
    "extent": "Original relevant statement and surrounding hypotheses opened; no claim that the entire external proof has been re-proved.",
    "retrieval": {
      "key": "Schnell19",
      "url": "https://www.math.stonybrook.edu/~cschnell/mat615/lectures/lecture4.pdf",
      "file": "sources/audit_cache/inv_ari/literature/Schnell19.pdf",
      "sha256": "711e26be8c2de831e7b3e81f0e4ca38ed2f24fcbddeca284609ba14bb6f263cf",
      "bytes": 473140,
      "kind": ".pdf",
      "seconds": 4.124960422515869
    },
    "web_open_locator": "turn42view0",
    "verified": true
  },
  {
    "citation_key": "CrCremonaSiksek2006",
    "status": "verified_for_stated_use",
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "opened_locator": "Original author PDF §1–2 pp.1–3, Proposition3 §5, Theorem1 §6 p.8.",
    "actual_use": "Automatic eclib lower-height saturation bound in C6.R1.",
    "hypotheses_and_normalization_check": "Minimal Weierstrass model and Egr=E(Q)∩E0(R)∩prod E0(Qp). Their canonical height is the x-height/2(O) convention, twice the paper height relative to (O). Bounds and regulator use the same convention; all component primes are included.",
    "citation_contexts": [
      {
        "file": "deliverables/work/invariants_arithmetic/sections/ari_rank.tex",
        "line": 57,
        "context": "pectively\n\\[\n 1,1,1,2,2,2,3,5,5\n\\]\nin the rank-one order $i=2,3,4,5,6,7,9,10,11$; the algorithm also\nchecks the primes dividing component-group orders. The underlying\nheight lower bound is the one in\n\\citet[Theorem 1]{CrCremonaSiksek2006}, applied to a minimal\nWeierstrass equation and the subgroup\n$E(\\Q)\\cap E^0(\\R)\\cap\\bigcap_pE^0(\\Q_p)$.\nFor the largest curve the lower bound on the n"
      }
    ],
    "extent": "Original relevant statement and surrounding hypotheses opened; no claim that the entire external proof has been re-proved.",
    "retrieval": {
      "key": "CrCremonaSiksek2006",
      "url": "https://johncremona.github.io/papers/HeightLB.pdf",
      "file": "sources/audit_cache/inv_ari/literature/CrCremonaSiksek2006.pdf",
      "sha256": "da4115cb6e73fb6b79d33923a69b4b98dc6525e631ed6d3978ead0d5de971fee",
      "bytes": 195837,
      "kind": ".pdf",
      "seconds": 3.9789836406707764
    },
    "verified": true
  },
  {
    "citation_key": "CrRubin1999",
    "status": "verified_for_stated_use",
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "opened_locator": "Original notes §10, Theorem10.1 p.47; surrounding standing CM setup.",
    "actual_use": "Coates–Wiles contrapositive to deduce central vanishing from nontorsion, including sign+1 curves in C6.R2.",
    "hypotheses_and_normalization_check": "Full maximal CM over K is the stated setup. Nonmaximal cases first pass to an isogenous maximal-order curve; rational full-CM L(E/K)=L(E/Q)^2. The theorem conclusion is E(K) finite when L(bar psi,1) nonzero, not the whole BSD formula.",
    "citation_contexts": [
      {
        "file": "deliverables/work/invariants_arithmetic/sections/ari_rank.tex",
        "line": 225,
        "context": "ed as \\path{code/Crank_cm_stream*}.\n\nThe exact root numbers are $+1$ for $i=1,8$ and $-1$ otherwise.\nAll points are nontorsion by Statement C.5. For a CM curve,\nthe Coates--Wiles theorem, in the form\n\\citet[Theorem 10.1]{CrRubin1999}, says that a nonzero central\nHecke $L$-value forces the Mordell--Weil group over the CM field\nto be finite. For a nonmaximal CM order first pass to a"
      }
    ],
    "extent": "Original relevant statement and surrounding hypotheses opened; no claim that the entire external proof has been re-proved.",
    "retrieval": {
      "key": "CrRubin1999",
      "url": "https://swc-math.github.io/aws/1999/99RubinCM.pdf",
      "file": "sources/audit_cache/inv_ari/literature/CrRubin1999.pdf",
      "sha256": "dcb99254ea3042d1f0c81d0cd2383399188954402b8453ce36ec988a5df3f1c5",
      "bytes": 490120,
      "kind": ".pdf",
      "seconds": 5.947563886642456
    },
    "verified": true
  },
  {
    "citation_key": "CrGrossZagier1986",
    "status": "verified_for_stated_use",
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "opened_locator": "Original preprint Theorem I.7.3, printed pp.11–12 (PDFpage8, visually read); proof V§2 printed pp.128–130, textlines5653ff.",
    "actual_use": "Rational nonzero factor between simple central derivative, a rational point height and real period in C6.R3.",
    "hypotheses_and_normalization_check": "Modularity is assumed in the source and holds for the CM curves via Hecke theta series. L(E,1)=0 is checked. Proof chooses a quadratic twist with nonzero central value by Waldspurger. Full real period and (O)-height change the source normalization only by rational factors.",
    "citation_contexts": [
      {
        "file": "deliverables/work/invariants_arithmetic/sections/ari_rank.tex",
        "line": 253,
        "context": "roof}\nGross--Zagier's theorem applies because each curve is modular and\n$L(E_i,1)=0$. CM modularity follows from its Hecke-character\ntheta series. Their Theorem I.7.3, in the opened original\npreprint \\citep{CrGrossZagier1986}, gives a rational point $R$ and\na nonzero rational factor relating $L'(E,1)$ to its canonical\nheight times the real period. Changing their period con"
      }
    ],
    "extent": "Original relevant statement and surrounding hypotheses opened; no claim that the entire external proof has been re-proved.",
    "retrieval": {
      "key": "CrGrossZagier1986",
      "url": "https://archive.mpim-bonn.mpg.de/id/eprint/3578/1/preprint_1985_30.pdf",
      "file": "sources/audit_cache/inv_ari/literature/CrGrossZagier1986.pdf",
      "sha256": "e5f6b8471ffbebff714cbd765ae8ce9061d03fe46ffd5cdb39941c94764eeabe",
      "bytes": 4529176,
      "kind": ".pdf",
      "seconds": 9.276689767837524
    },
    "verified": true
  },
  {
    "citation_key": "CrGross1991",
    "status": "verified_for_stated_use",
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "opened_locator": "Original scan §1 printed pp.235–236 (PDFpages1–2 visually read), Theorem1.3; §2 opening p.237.",
    "actual_use": "Kolyvagin finite Sha and rank1 conclusion for a non-torsion Heegner point in C6.R3.",
    "hypotheses_and_normalization_check": "Imaginary quadratic K with all primes of N split, D≠3,4, and non-torsion y_K. The non-CM assumption on p.237 applies to the subsequent simplified proof, not Theorem1.3 on p.236. The analytic-rank-one application uses the nonzero Heegner height. Restriction/corestriction and finite 2-torsion descend finiteness from K to Q.",
    "citation_contexts": [
      {
        "file": "deliverables/work/invariants_arithmetic/sections/ari_rank.tex",
        "line": 265,
        "context": "ity.\n\nThe rank-one Gross--Zagier--Kolyvagin implication asserts rank one\nand finite Tate--Shafarevich group when the central zero is simple.\nOne can use Kolyvagin's Heegner-point theorem as stated in\n\\citet[Theorem 1.3]{CrGross1991}, together with the nonzero\nGross--Zagier Heegner height; a modern primary research statement\nof the rank conclusion is \\citet[Theorem 1.1]{CrJetchev2"
      }
    ],
    "extent": "Original relevant statement and surrounding hypotheses opened; no claim that the entire external proof has been re-proved.",
    "retrieval": {
      "key": "CrGross1991",
      "url": "https://wstein.org/papers/bib/gross-kolyvagins_work_on_modular_elliptic_curves.pdf",
      "file": "sources/audit_cache/inv_ari/literature/CrGross1991.pdf",
      "sha256": "60b310c58a3494860c5967a03569a7d30033e9074d9d3d9a0d5bc2dfedd46b32",
      "bytes": 1937865,
      "kind": ".pdf",
      "seconds": 4.705339431762695
    },
    "verified": true
  },
  {
    "citation_key": "CrJetchev2008",
    "status": "verified_for_stated_use",
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "opened_locator": "Original arXiv0707.0032, Introduction Theorem1.1 p.2, textlines53–70.",
    "actual_use": "Modern primary statement of Gross–Zagier–Kolyvagin rank equality in analytic rank<=1.",
    "hypotheses_and_normalization_check": "Theorem1.1 itself asserts rank equality, not Sha finiteness. The latter is separately sourced to Gross Theorem1.3; no stronger conclusion is assigned to Jetchev1.1.",
    "citation_contexts": [
      {
        "file": "deliverables/work/invariants_arithmetic/sections/ari_rank.tex",
        "line": 267,
        "context": " Kolyvagin's Heegner-point theorem as stated in\n\\citet[Theorem 1.3]{CrGross1991}, together with the nonzero\nGross--Zagier Heegner height; a modern primary research statement\nof the rank conclusion is \\citet[Theorem 1.1]{CrJetchev2008}.\nThe hypotheses are satisfied separately by the positive derivative\nand exact sign in each of the nine rows. The two remaining rows\nhave analytic ran"
      }
    ],
    "extent": "Original relevant statement and surrounding hypotheses opened; no claim that the entire external proof has been re-proved.",
    "retrieval": {
      "key": "CrJetchev2008",
      "url": "https://arxiv.org/pdf/0707.0032",
      "file": "sources/audit_cache/inv_ari/literature/CrJetchev2008.pdf",
      "sha256": "1b61d9e99665d7a2387a5fd3dcd1a6d4f80b0a1dd2eb8e87ce0b6c0ea6716151",
      "bytes": 291013,
      "kind": ".pdf",
      "seconds": 6.057862043380737
    },
    "verified": true
  },
  {
    "citation_key": "miller2011",
    "status": "verified_for_stated_use",
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "opened_locator": "Original arXiv1010.2431v3, Definition1.1/Theorem1.2 p.2; Table9 p.23.",
    "actual_use": "Full BSD for the three conductor3136,3136,361 curves in C6.R4.",
    "hypotheses_and_normalization_check": "Analytic rank<=1, conductor<5000. The eleven exceptional curve-prime pairs have conductors546,570,858,870,1050,1230,1938,1950,2370,2550,3270. None is one of the three curves; isogeny invariance noted before the theorem. The integer analytic quotient is then isolated independently by exact doublings/Arb.",
    "citation_contexts": [
      {
        "file": "deliverables/work/invariants_arithmetic/sections/ari_rank.tex",
        "line": 316,
        "context": " For the smallest of these examples,\n$E:y^2+y=x^3-38x+90$ and $P=(0,9)$, this gives the exact\nreduction\n\\[\n N(P)=\\exp\\left(-\\frac{L'(E,1)}{4\\Omega_E}\\right).\n\\]\n\\end{proposition}\n\\begin{proof}\nWe use \\citet[Theorem 1.2 and Table 9]{miller2011}. In the\nnotation of its Definition 1.1, the theorem proves\n$\\mathrm{BSD}(E/\\Q,p)$ for every prime $p$ when the curve has\nanalytic rank at most one, c"
      }
    ],
    "extent": "Original relevant statement and surrounding hypotheses opened; no claim that the entire external proof has been re-proved.",
    "retrieval": {
      "key": "miller2011",
      "url": "https://arxiv.org/pdf/1010.2431v3",
      "file": "sources/audit_cache/inv_ari/literature/miller2011.pdf",
      "sha256": "52cbe68361e6eb07f94e13197a88eb5295c3f92e339a65d1488324d5489055ae",
      "bytes": 322037,
      "kind": ".pdf",
      "seconds": 3.7768378257751465
    },
    "verified": true
  },
  {
    "citation_key": "CgzCai2014",
    "status": "verified_for_stated_use",
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "opened_locator": "Original publisher PDF Theorem1.1 pp.2524–2525; conventions pp.2523–2524 and pairing discussion p.2531.",
    "actual_use": "Exact Gross–Zagier denominator bound for C6.R5.",
    "hypotheses_and_normalization_check": "Conductor-one genus character, conductor prime to N, no inert prime dividing N, repeated primes split, and shared N,D local-character compatibility checked in the exact metadata program. Formula factor2^-mu 8pi²(f,f)/(u²sqrt(|D|c²)deg f) uses the number-field-normalized height pairing; YZZ normalization below supplies the extra factor4.",
    "citation_contexts": [
      {
        "file": "deliverables/work/invariants_arithmetic/sections/ari_gz_factors.tex",
        "line": 146,
        "context": "hbb F_p^\\times$\nis surjective. Since $p$ is odd and unramified in $K$, this also\nproves that the conductor contains every $p\\mid d$ exactly once.\nThus the primitive ring-class-character hypotheses of\n\\citet[Theorem 1.1, pp.~2524--2525]{CgzCai2014} hold. Their\n$\\mu(N_0,D)=0$ and\n$u=[\\mathcal O_{|d|}^{\\times}:\\Z^{\\times}]=1$; the latter remains\ntrue for $D=-3$ because $|d|>1$.\n\nLet $P_{\\mathfrak "
      }
    ],
    "extent": "Original relevant statement and surrounding hypotheses opened; no claim that the entire external proof has been re-proved.",
    "retrieval": {
      "key": "CgzCai2014",
      "url": "https://msp.org/ant/2014/8-10/ant-v8-n10-p05-p.pdf",
      "file": "sources/audit_cache/inv_ari/literature/CgzCai2014.pdf",
      "sha256": "3eef3f34a03d21575bdb352acfaa0bef2fbe3701068a65798cb89a6ae84333e7",
      "bytes": 1409076,
      "kind": ".pdf",
      "seconds": 5.655363321304321
    },
    "verified": true
  },
  {
    "citation_key": "CgzBelabas2019",
    "status": "verified_for_stated_use",
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "opened_locator": "Original publisher PDF AppendixB p.102, unnumbered 26569a1/26569a2 table (PDFpage23), visually read.",
    "actual_use": "Manin constant1 and modular degree59368 for 26569a1 in C6.R5.",
    "hypotheses_and_normalization_check": "Table columns are deg and c_E; 26569a1 has59368 and1, 26569a2 has9676984 and1. No nonexistent Table5 is cited. Optimality/homology columns are (1,1) for a1.",
    "citation_contexts": [
      {
        "file": "deliverables/work/invariants_arithmetic/sections/ari_gz_factors.tex",
        "line": 120,
        "context": ". For the first five bases this\nis independently returned by PARI's unconditional modular-symbol\nalgorithm. For $26569\\mathrm a1$, the value one and modular degree\n$59368$ are explicitly tabulated by\n\\citet[Appendix B, p.~102, unnumbered $26569\\mathrm a1/26569\\mathrm a2$\nblock]{CgzBelabas2019}; their Algorithm 1 describes the computation.\nThe first five completed computations are in\n\\path{code/B_C6_gz_setup.out}. The separate exact audit\n\\p"
      }
    ],
    "extent": "Original relevant statement and surrounding hypotheses opened; no claim that the entire external proof has been re-proved.",
    "retrieval": {
      "key": "CgzBelabas2019",
      "url": "https://www.numdam.org/item/10.5802/pmb.37.pdf",
      "file": "sources/audit_cache/inv_ari/literature/CgzBelabas2019.pdf",
      "sha256": "04c9c47cdfa16390fb7b24f838423dd5a69d06a9d8448c376e6e05278ec9bd4b",
      "bytes": 1341347,
      "kind": ".pdf",
      "seconds": 7.4757914543151855
    },
    "verified": true
  },
  {
    "citation_key": "CgzYZZ2011",
    "status": "verified_for_stated_use",
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "opened_locator": "Original complete preprint §7.1.1 pp.218–219, Theorems7.1.1–7.1.2 and Proposition7.1.3; textlines11243–11328.",
    "actual_use": "Resolve field-degree and polarization factors in C6.R5.",
    "hypotheses_and_normalization_check": "The absolute values are normalized over K and the displayed height divides by[K:F], hence over quadratic F it is2 times the absolute height over Q. Pairing is h(x+y)−h(x)−h(y), hence its diagonal is2h, not h. Together the diagonal over the quadratic base is4 times the paper (O)-height. L is symmetric ample, as O(origin) on E.",
    "citation_contexts": [
      {
        "file": "deliverables/work/invariants_arithmetic/sections/ari_gz_factors.tex",
        "line": 188,
        "context": "uct}\n L'(E_i,1)L(E_i^D,1)\n  =\\frac{2V_0}{c_0^2|d|\\sqrt{|D|}}\\,\\widehat h_K(Y).\n\\end{equation}\nHere $\\widehat h_K$ is the diagonal N\\'eron--Tate pairing relative\nto $K$. This convention is explicit in\n\\citet[\\S7.1.1, pp.~218--219, Theorem 7.1.2]{CgzYZZ2011}:\ntheir underlying height is normalized by $[L:K]^{-1}$ over a\nfield of definition $L$, and their pairing is\n$\\widehat h_{\\mathcal L}(x+y)-\\widehat h_"
      }
    ],
    "extent": "Original relevant statement and surrounding hypotheses opened; no claim that the entire external proof has been re-proved.",
    "retrieval": {
      "key": "CgzYZZ2011",
      "url": "https://www.researchgate.net/profile/Xinyi-Yuan-11/publication/267551160_Gross-Zagier_Formula_On_Shimura_Curves/links/548e842c0cf225bf66a5ff13/Gross-Zagier-Formula-On-Shimura-Curves.pdf?origin=publication_detail",
      "file": "sources/audit_cache/inv_ari/literature/CgzYZZ2011.pdf",
      "sha256": "7a6b79df81cf5d88e8a4bfbad5a2a9502dcb7b4ac16631e3d270c69bb71a7235",
      "bytes": 1546742,
      "kind": ".pdf",
      "seconds": 4.856720685958862
    },
    "verified": true
  },
  {
    "citation_key": "CgzStein2007",
    "status": "verified_for_stated_use",
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "opened_locator": "Original book §9.4.1.2, Theorem9.18 printed pp.171–172.",
    "actual_use": "Finite coefficient equality via Sturm bound in C6.R5.",
    "hypotheses_and_normalization_check": "Weight2, congruence subgroup Gamma0(N), integral coefficients; agreement beyond k[SL2Z:Gamma]/12 suffices. Congruence for every prime ideal gives exact equality of integral coefficients; only this elementary corollary is used.",
    "citation_contexts": [
      {
        "file": "deliverables/work/invariants_arithmetic/sections/ari_gz_factors.tex",
        "line": 273,
        "context": "evel valence formula\ntherefore implies $\\operatorname{ord}_\\infty g\\leq kI/12$.\nEquivalently, agreement through $\\lfloor kI/12\\rfloor$ proves\nequality. The stronger arithmetic congruence statement is\n\\citet[Theorem 9.18]{CgzStein2007}; only the elementary\ncharacteristic-zero argument is needed here. For $k=2,N=s^2$\nthe four bounds are\n\\[\n \\left\\lfloor\\frac{s^2+s}{6}\\right\\rfloor\n  "
      }
    ],
    "extent": "Original relevant statement and surrounding hypotheses opened; no claim that the entire external proof has been re-proved.",
    "retrieval": {
      "key": "CgzStein2007",
      "url": "https://wstein.org/books/modform/stein-modform.pdf",
      "file": "sources/audit_cache/inv_ari/literature/CgzStein2007.pdf",
      "sha256": "b50e81d48d2fb794948414fee625d1d3ca19c191a87430ca38c8713c8f466b75",
      "bytes": 2546615,
      "kind": ".pdf",
      "seconds": 4.349894285202026
    },
    "verified": true
  },
  {
    "citation_key": "CrBDP2012",
    "status": "verified_for_stated_use",
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "opened_locator": "Original publisher-format author PDF Theorem1 printed p.262, standing assumptions pp.261–262.",
    "actual_use": "Precise ordinary p-adic Rubin formula in the scope discussion after C6.R4.",
    "hypotheses_and_normalization_check": "Curve over Q with full CM, prime split and prime to conductor, simple central zero. Katz special value equals p-adic logarithm square divided by p-adic period modulo K*. It does not give algebraicity of the real exponential height.",
    "citation_contexts": [
      {
        "file": "deliverables/work/invariants_arithmetic/sections/ari_rank.tex",
        "line": 379,
        "context": "The applicable ordinary CM results concern a prime $p$ at which\n$E$ has good ordinary reduction, equivalently $p$ splits in the CM\nfield. One precise opened formulation of Rubin's rank-one formula\nis \\citet[Theorem 1]{CrBDP2012}: for a curve over $\\Q$ with CM\nby the maximal order, an ordinary prime prime to the conductor,\nand a simple central zero, an appropriate Katz $p$-adi"
      }
    ],
    "extent": "Original relevant statement and surrounding hypotheses opened; no claim that the entire external proof has been re-proved.",
    "retrieval": {
      "key": "CrBDP2012",
      "url": "https://www.math.mcgill.ca/darmon/pub/Articles/Research/52.BDP2/bdp-pjm.pdf",
      "file": "sources/audit_cache/inv_ari/literature/CrBDP2012.pdf",
      "sha256": "d3299513bcf61f61c91308e2ce1a25aa6a6bcc61a367fe293f0d50b0de1aa660",
      "bytes": 548475,
      "kind": ".pdf",
      "seconds": 4.738961935043335
    },
    "verified": true
  },
  {
    "citation_key": "CrCastella2025",
    "status": "verified_for_stated_use",
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "opened_locator": "Original author PDF dated2025-02-14, TheoremA and Remark1.1.1 p.2.",
    "actual_use": "Precise p-primary BSD scope discussion after C6.R4.",
    "hypotheses_and_normalization_check": "Full CM, F(Etors)/K abelian, ord L(psi)=1, p not dividing6hK and split, Hecke conductor prime to p, different divides conductor exactly. Source explicitly distinguishes K⊂F (rank2) and K not⊂F (rank1). Nonmaximal orders require isogeny; the -16 different condition is not claimed. p=3 is excluded and inert at -163, so no actual Sha=9 conclusion.",
    "citation_contexts": [
      {
        "file": "deliverables/work/invariants_arithmetic/sections/ari_rank.tex",
        "line": 389,
        "context": "y verified here.\nIt is a $p$-adic identity; it does not identify the real exponential\n$\\exp\\widehat h(P)$ as algebraic.\n\nFor the $p$-part of the real leading-term formula, a modern precise\nversion is \\citet[Theorem A]{CrCastella2025}. In addition to analytic\nrank one it requires full CM, abelian torsion field over the CM\nfield, $p\\nmid6h_K$, splitting of $p$, conductor prime to $p"
      }
    ],
    "extent": "Original relevant statement and surrounding hypotheses opened; no claim that the entire external proof has been re-proved.",
    "retrieval": {
      "key": "CrCastella2025",
      "url": "https://web.math.ucsb.edu/~castella/Katz.pdf",
      "file": "sources/audit_cache/inv_ari/literature/CrCastella2025.pdf",
      "sha256": "1f04566f5d7bf58c18f5a0c31101ebf5d48655f72620d289c606bbc8dab69664",
      "bytes": 616078,
      "kind": ".pdf",
      "seconds": 4.547553777694702
    },
    "verified": true
  },
  {
    "citation_key": "agboola2006",
    "status": "verified_for_stated_use",
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "opened_locator": "Original publisher PDF introduction pp.1001–1002; Rubin AppendixA pp.1042–1043, TheoremA.1 and LemmaA.2.",
    "actual_use": "Nonzero ordinary p-adic height of the rank-one CM point in C7.8.",
    "hypotheses_and_normalization_check": "Standing hypotheses: full CM, class number1, p>3 good ordinary; appendix sign−1. TheoremA.1 only guarantees nonzero height of an actual non-torsion algebraic point, not arbitrary pairing nondegeneracy after tensoring. Rational point has zero anticyclotomic projection, and the three projections in LemmaA.2 are pairwise independent linear forms.",
    "citation_contexts": [
      {
        "file": "deliverables/work/invariants_arithmetic/sections/ari_padic.tex",
        "line": 11,
        "context": " ordinary reduction, $p\\mathcal O_K=\\mathfrak p\n\\mathfrak p^*$. For a nontorsion $P\\in E(\\Q)$ the\n$\\mathfrak p$-adic height and the cyclotomic $p$-adic height\nof $P$ over $K$, in the normalization of\n\\citet[Appendix A]{agboola2006}, are nonzero.\nIn particular this applies to\n\\[\n E:y^2+y=x^3-38x+90,\\qquad P=(0,9),\\qquad p=5.\n\\]\n\\end{proposition}\n\\begin{proof}\nWe use the exact the"
      },
      {
        "file": "deliverables/work/invariants_arithmetic/sections/ari_padic.tex",
        "line": 19,
        "context": "e nonzero.\nIn particular this applies to\n\\[\n E:y^2+y=x^3-38x+90,\\qquad P=(0,9),\\qquad p=5.\n\\]\n\\end{proposition}\n\\begin{proof}\nWe use the exact theorem reproduced as Theorem A.1 in Rubin's\nappendix to \\citet{agboola2006}, attributed there to\n\\citet{bertrand1984}: for a number field $F$ and a point of\ninfinite order in $E(F)$, its height $h_{F,\\mathfrak p}$ is\nnonzero."
      }
    ],
    "extent": "Original relevant statement and surrounding hypotheses opened; no claim that the entire external proof has been re-proved.",
    "retrieval": {
      "key": "agboola2006",
      "url": "https://web.math.ucsb.edu/~agboola/papers/bisi_aif_2006.pdf",
      "file": "sources/audit_cache/inv_ari/literature/agboola2006.pdf",
      "sha256": "1c176f86e757830dd18d36568c3066e2682733e8e3de6193133f886090280741",
      "bytes": 654462,
      "kind": ".pdf",
      "seconds": 4.99127721786499
    },
    "verified": true
  },
  {
    "citation_key": "waldschmidt1979sigma",
    "status": "verified_for_stated_use",
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "opened_locator": "Author-hosted English translation of the1979 paper, §4 Theorem1 and §5 Corollary1 p.3; whole pp.1–3 read.",
    "actual_use": "Transcendence of algebraically twisted third-kind sigma value and sigma(u) exp(−u zeta(u)/2) in C7.7.",
    "hypotheses_and_normalization_check": "Algebraic invariants and algebraic elliptic points, u0 nontorsion, u and u+u0 not poles, algebraic beta. The word algebraic point means algebraic wp-coordinate, not algebraic logarithm. The bare real norm contains an extra nonholomorphic Gaussian and is excluded.",
    "citation_contexts": [
      {
        "file": "deliverables/work/invariants_arithmetic/sections/ari_cm_transcendence.tex",
        "line": 96,
        "context": ". The first\nassertion concerns the displayed holomorphic normalization;\nit does not assert transcendence of either $N(P)$ or\n$\\theta(u)=\\sigma(u)e^{-s_2u^2/2}$.\n\\end{proposition}\n\\begin{proof}\nWe use \\citet[Theorem 1 and Corollary 1]{waldschmidt1979sigma},\nwhose complete proof was opened in the translation hosted by its\nauthor. Its Theorem 1 states that, for algebraic invariants\n$g_2,g_3$, algebraic el"
      }
    ],
    "extent": "Original relevant statement and surrounding hypotheses opened; no claim that the entire external proof has been re-proved.",
    "retrieval": {
      "key": "waldschmidt1979sigma",
      "url": "https://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/GDL/SigmaNoteCanada1979-eng.pdf",
      "file": "sources/audit_cache/inv_ari/literature/waldschmidt1979sigma.pdf",
      "sha256": "8d504460bd539f934aef8c8825ee9ec152ed8133666adbe8798b745e28bc3d87",
      "bytes": 192149,
      "kind": ".pdf",
      "seconds": 4.248716592788696
    },
    "verified": true
  },
  {
    "citation_key": "noguchi2024",
    "status": "verified_for_stated_use",
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "opened_locator": "Theorem1.3, p.2 and the definitions immediately preceding it (extracted text lines25–100).",
    "actual_use": "Scope check of the semi-abelian functional transcendence route.",
    "hypotheses_and_normalization_check": "The theorem concerns an A-nondegenerate entire map into a semi-abelian variety and the transcendence degree of its graph, at least dim(A)+1. It is a functional statement and does not assert transcendence of the metric norm at an algebraic point.",
    "citation_contexts": [
      {
        "file": "deliverables/work/invariants_arithmetic/sections/ari_diagonal_obstruction.tex",
        "line": 165,
        "context": " after an isogeny. Every proper\nconnected subgroup is therefore contained in the torus,\nwhereas $\\exp_{G_Q}f$ has nonconstant elliptic projection.\nThus $f$ is $G_Q$-nondegenerate in Definition 1.2 of\n\\citet{noguchi2024}. Their Theorem 1.3 gives\n\\[\n \\dim_{\\C}\\overline{\\{(\\exp_{G_Q}f(z),f(z)):z\\in\\C\\}}^{\\rm Zar}\n       \\ge \\dim G_Q+1=3.\n\\]\nThe graph is contained in $G_"
      }
    ],
    "extent": "The complete cited statement and its relevant surrounding hypotheses were opened. The application and its limits were checked independently; this is not a claim to reprove every external theorem.",
    "retrieval": {
      "key": "noguchi2024",
      "url": "https://www.ms.u-tokyo.ac.jp/~noguchi/An-axsch.pdf",
      "file": "sources/audit_cache/inv_ari/literature/noguchi2024.pdf",
      "sha256": "524b23cf67587abfb22e07b14b97158f2390b4528b85ffa2f934b1d7f2c42a16",
      "bytes": 154890,
      "kind": ".pdf",
      "seconds": 4.889240741729736
    },
    "verified": true,
    "local_source": "sources/audit_cache/inv_ari/literature/noguchi2024.pdf",
    "source_sha256": "524b23cf67587abfb22e07b14b97158f2390b4528b85ffa2f934b1d7f2c42a16"
  },
  {
    "citation_key": "waldschmidt2009auxiliary",
    "status": "verified_for_stated_use",
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "opened_locator": "Theorem3.4 (one-variable Schneider–Lang criterion) and Theorem3.6 (several-variable criterion), extracted text lines1320ff. and1477–1505.",
    "actual_use": "Check of derivative-closed fixed-number-field interpolation assumptions.",
    "hypotheses_and_normalization_check": "The derivatives must be polynomial expressions over one number field in the entire functions; the multivariable theorem additionally uses finite growth and a lattice basis. In the proposed theta route the logarithmic derivative is transcendental at the algebraic point, so the needed arithmetic closure has not been established.",
    "citation_contexts": [
      {
        "file": "deliverables/work/invariants_arithmetic/sections/ari_complexified.tex",
        "line": 168,
        "context": "_1=0$, $\\wp(u)=4$ and $s_2=-2$,\nwhich give the last displayed formula in the statement.\n\\end{proof}\n\n\\paragraph{The precise several-variable criteria that were checked.}\nThe differential criterion of\n\\citet[Theorems 3.6 and 3.7]{waldschmidt2009auxiliary}\nrequires a finite algebraically independent family whose\npartial derivatives belong to the polynomial ring generated\nby that family over one number f"
      }
    ],
    "extent": "The complete cited statement and its relevant surrounding hypotheses were opened. The application and its limits were checked independently; this is not a claim to reprove every external theorem.",
    "retrieval": {
      "key": "waldschmidt2009auxiliary",
      "url": "https://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/SASTRAaftp.pdf",
      "file": "sources/audit_cache/inv_ari/literature/waldschmidt2009auxiliary.pdf",
      "sha256": "3b14bea582d73bc4cb4000cab90dafc374ccdb56418f04a26aaf1a8e322d2732",
      "bytes": 1105261,
      "kind": ".pdf",
      "seconds": 12.779705286026001
    },
    "verified": true,
    "local_source": "sources/audit_cache/inv_ari/literature/waldschmidt2009auxiliary.pdf",
    "source_sha256": "3b14bea582d73bc4cb4000cab90dafc374ccdb56418f04a26aaf1a8e322d2732"
  },
  {
    "citation_key": "waldschmidt1975dimension",
    "status": "verified_for_stated_use",
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "opened_locator": "Theorem1 and inequalities(1)–(3), p.24; proof pp.25–27.",
    "actual_use": "Exact multivariable interpolation threshold in the complexified norm obstruction.",
    "hypotheses_and_normalization_check": "Values lie in one fixed number field; meromorphic functions admit entire denominators with the stated growth and value-size bounds, sampling cardinality at least N^ell, separation at least N^(-lambda). The sufficient inequality is (d-1)ell > sum(rho_j)+2d(n-1)(lambda+1). The proposed d=3,n=2,ell=4,rho_j=2 would need 8>12+6lambda and fails. An upper degree envelope is never treated as a lower bound.",
    "citation_contexts": [
      {
        "file": "deliverables/work/invariants_arithmetic/sections/ari_complexified.tex",
        "line": 180,
        "context": "zed algebraic orbit points. The issue persists\nalthough the first cancelling direction is algebraic; the\ndirection also varies with $\\alpha$.\n\nFor a criterion without differential equations we opened\n\\citet[Theorem 1, p.~24]{waldschmidt1975dimension}, including\nits proof and a visual check of the displayed inequalities.\nFor $d$ meromorphic functions on $\\C^n$ with growth and\narithmetic-size expone"
      }
    ],
    "extent": "The complete cited statement and its relevant surrounding hypotheses were opened. The application and its limits were checked independently; this is not a claim to reprove every external theorem.",
    "retrieval": {
      "key": "waldschmidt1975dimension",
      "url": "https://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/Fourier.pdf",
      "file": "sources/audit_cache/inv_ari/literature/waldschmidt1975dimension.pdf",
      "sha256": "a628c5f95ecb040df617250e229aef9fff4487a95c25c11d831cd3969f928454",
      "bytes": 2145671,
      "kind": ".pdf",
      "seconds": 24.078907251358032
    },
    "verified": true,
    "local_source": "sources/audit_cache/inv_ari/literature/waldschmidt1975dimension.pdf",
    "source_sha256": "a628c5f95ecb040df617250e229aef9fff4487a95c25c11d831cd3969f928454",
    "visual_check": "sources/audit_cache/inv_ari/literature/scans/waldschmidt1975dimension-03.png, printed p.24, inspected visually."
  },
  {
    "citation_key": "bertrand2017",
    "status": "verified_for_stated_use",
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "opened_locator": "Original author slides5–8 and final slide15, comment(c); full displayed semi-abelian exponential and real compact determinant on slides7–8.",
    "actual_use": "Context for the compact-subgroup interpretation in C.7.2 and precise documentation of the withdrawn unrestricted-lift theta inference in C.7.7.",
    "hypotheses_and_normalization_check": "Slides7–8 use f_v(z)=sigma(v+z)/(sigma(v)sigma(z)) exp(-zeta(v)z), the specified algebraic section and real place. The final-slide pointwise equivalence requires original lift conventions: replacing v by v+omega changes the expression by (eta(omega)-s2 omega)u. Neither direction of that unverified unrestricted-lift assertion is used. The compact character in the manuscript is calculated independently.",
    "citation_contexts": [
      {
        "file": "deliverables/work/invariants_arithmetic/sections/ari_periods.tex",
        "line": 129,
        "context": "(u)|\\,|\\Delta|^{-1/6}N(P)^2$.\nThen \\eqref{ari:eq:cp-chi} vanishes. This proves both directions\nwith the chosen rational trivialization of the fibre.\nThe compact interpretation is the one discussed by\n\\citet[slides 5--8]{bertrand2017}; here the calculation fixes\nits normalization on the diagonal $P=P$.\n\nFor the real formula, the rectangular elliptic curve has its\ntwo zeros of $\\wp$"
      },
      {
        "file": "deliverables/work/invariants_arithmetic/sections/ari_cm_transcendence.tex",
        "line": 144,
        "context": "geny, since pullback is invertible in\ncharacteristic zero.\n\\end{proof}\n\n\\paragraph{A theta criterion requiring its original normalization.}\nAn earlier draft applied the pointwise criterion printed in\n\\citet[final slide, comment (c)]{bertrand2017} to\n$g(u,v)-s_2uv$, where\n$g(u,v)=\\log(\\sigma(u+v)/(\\sigma(u)\\sigma(v)))$.\nIt inferred transcendence of $\\theta(u)$ by taking $v=u$.\nWe withdraw that "
      }
    ],
    "extent": "The complete cited statement and its relevant surrounding hypotheses were opened. The application and its limits were checked independently; this is not a claim to reprove every external theorem.",
    "retrieval": {
      "key": "bertrand2017",
      "url": "https://webusers.imj-prg.fr/~daniel.bertrand/Recherche/rpdf/DB_Fieldspost.pdf",
      "file": "sources/audit_cache/inv_ari/literature/bertrand2017.pdf",
      "sha256": "e6b048ad97823062723cddb9672f027ea3664472825eeb79ff2b9fd64bd99f6d",
      "bytes": 276902,
      "kind": ".pdf",
      "seconds": 4.430939435958862
    },
    "verified": true,
    "local_source": "sources/audit_cache/inv_ari/literature/bertrand2017.pdf",
    "source_sha256": "e6b048ad97823062723cddb9672f027ea3664472825eeb79ff2b9fd64bd99f6d"
  },
  {
    "citation_key": "bertrand1984",
    "status": "unverified_original_not_used_for_strengthening",
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "opened_locator": "Complete original Corollary3 and its lift convention not obtained. Unrestricted theta-lift criterion is withdrawn. Only the precisely reproduced p-adic nonvanishing theorem in Rubin AppendixA of agboola2006 is invoked.",
    "actual_use": "See the exact printed citation contexts; no theorem status is inferred from retrieval alone.",
    "hypotheses_and_normalization_check": "Complete original Corollary3 and its lift convention not obtained. Unrestricted theta-lift criterion is withdrawn. Only the precisely reproduced p-adic nonvanishing theorem in Rubin AppendixA of agboola2006 is invoked.",
    "citation_contexts": [
      {
        "file": "deliverables/work/invariants_arithmetic/sections/ari_padic.tex",
        "line": 20,
        "context": "\\[\n E:y^2+y=x^3-38x+90,\\qquad P=(0,9),\\qquad p=5.\n\\]\n\\end{proposition}\n\\begin{proof}\nWe use the exact theorem reproduced as Theorem A.1 in Rubin's\nappendix to \\citet{agboola2006}, attributed there to\n\\citet{bertrand1984}: for a number field $F$ and a point of\ninfinite order in $E(F)$, its height $h_{F,\\mathfrak p}$ is\nnonzero. We retain the standing hypotheses of that"
      },
      {
        "file": "deliverables/work/invariants_arithmetic/sections/ari_cm_transcendence.tex",
        "line": 149,
        "context": "$, where\n$g(u,v)=\\log(\\sigma(u+v)/(\\sigma(u)\\sigma(v)))$.\nIt inferred transcendence of $\\theta(u)$ by taking $v=u$.\nWe withdraw that inference pending verification of the original\nlift conventions in \\citet[Corollary 3]{bertrand1984}.\nIndeed replacing $v$ by $v+\\omega$, $\\omega\\in\\Lambda$,\nchanges $g(u,v)-s_2uv$, modulo $2\\pi i\\Z$, by\n\\[\n (\\eta(\\omega)-s_2\\omega)u=\\frac{\\pi\\bar\\om"
      }
    ],
    "extent": "Original relevant statement and surrounding hypotheses opened; no claim that the entire external proof has been re-proved.",
    "verified": false
  },
  {
    "citation_key": "bertrand1995",
    "status": "verified_for_stated_use",
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "opened_locator": "Original paper, Theorem2.1 p.147 and its construction; Proposition2.2 and Theorem3.1 p.150 (extracted text lines90–160 and240–290).",
    "actual_use": "Counterexamples to a universal claim that an algebraic point in a multiplicative extension’s maximal compact subgroup is torsion; distinction from the additive extension theorem.",
    "hypotheses_and_normalization_check": "Theorem2.1 assumes a real number field, a geometrically simple polarized abelian variety with a non-Rosati-invariant endomorphism and infinitely many rational points. The example uses an antisymmetric endomorphism h-h^dagger and a Ribet lift. The additive statement in Theorem3.1 does not transfer to multiplicative extensions.",
    "citation_contexts": [
      {
        "file": "deliverables/work/invariants_arithmetic/sections/ari_padic.tex",
        "line": 62,
        "context": "ely such a\nnew argument; replacing the real factor by the holomorphic\nCM correction does not preserve the norm being asked about.\n\nThere is also a definite limitation on the maximal-compact\napproach. \\citet[Theorem 2.1]{bertrand1995} constructs\nnontrivial multiplicative extensions of polarized abelian\nvarieties with nontorsion algebraic points in their maximal\nreal compact subgrou"
      },
      {
        "file": "deliverables/work/invariants_arithmetic/sections/ari_padic.tex",
        "line": 79,
        "context": "o isogeny. The diagonal positivity\nused in C.7.3--C.7.4 is therefore essential, but these\ncounterexamples neither prove nor refute the desired\nunconditional diagonal statement. The additive result in\n\\citet[Theorem 3.1]{bertrand1995}, and its higher-dimensional\nextension in \\citet{bost2009}, requires a point in a vector\nextension, a hypothesis not furnished by C.7.2.\n"
      }
    ],
    "extent": "The complete cited statement and its relevant surrounding hypotheses were opened. The application and its limits were checked independently; this is not a claim to reprove every external theorem.",
    "retrieval": {
      "key": "bertrand1995",
      "url": "https://www.maths.tcd.ie/EMIS/journals/EM/restricted/4/4.2/bertrand.ps",
      "file": "sources/audit_cache/inv_ari/literature/bertrand1995.ps",
      "sha256": "48ae19bbaa728b4c1cbeab575f8608c131b230d8202376566a1ebfcba9d61010",
      "bytes": 689847,
      "kind": ".ps",
      "seconds": 6.428455352783203
    },
    "verified": true
  },
  {
    "citation_key": "bost2009",
    "status": "verified_for_stated_use",
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "opened_locator": "Theorems3.1.1–3.1.2, p.386 (extracted text lines1245–1310).",
    "actual_use": "Exact scope of the unitary algebraic-connection/universal-vector-extension alternative considered after C.7.7.",
    "hypotheses_and_normalization_check": "The algebraic point must lie in the maximal compact subgroup of the universal vector extension, equivalently an algebraic connection must be unitary at an embedding. A point in a multiplicative extension’s compact subgroup alone does not meet this hypothesis.",
    "citation_contexts": [
      {
        "file": "deliverables/work/invariants_arithmetic/sections/ari_padic.tex",
        "line": 80,
        "context": "ial, but these\ncounterexamples neither prove nor refute the desired\nunconditional diagonal statement. The additive result in\n\\citet[Theorem 3.1]{bertrand1995}, and its higher-dimensional\nextension in \\citet{bost2009}, requires a point in a vector\nextension, a hypothesis not furnished by C.7.2.\n"
      },
      {
        "file": "deliverables/work/invariants_arithmetic/sections/ari_cm_transcendence.tex",
        "line": 223,
        "context": "\nspecific checked applications therefore do not decide the\nmetric norm; their source scopes and the larger CM\nindependence tuples are recorded separately.\n\nWe also tested an additive-extension route.\n\\citet[Theorem 3.1.2]{bost2009} proves that an algebraic point\nof the universal vector extension of an abelian variety which\nlies in its maximal compact subgroup at one complex embe"
      }
    ],
    "extent": "The complete cited statement and its relevant surrounding hypotheses were opened. The application and its limits were checked independently; this is not a claim to reprove every external theorem.",
    "retrieval": {
      "key": "bost2009",
      "url": "https://www.numdam.org/article/AST_2009__327__361_0.pdf",
      "file": "sources/audit_cache/inv_ari/literature/bost2009.pdf",
      "sha256": "c6c06921e868e219c0095bd9b102db45c18bf525e16cd2e1a36118ce7fc7cf65",
      "bytes": 6153829,
      "kind": ".pdf",
      "seconds": 76.18616580963135
    },
    "verified": true,
    "local_source": "sources/audit_cache/inv_ari/literature/bost2009.pdf",
    "source_sha256": "c6c06921e868e219c0095bd9b102db45c18bf525e16cd2e1a36118ce7fc7cf65"
  },
  {
    "citation_key": "gramain1986values",
    "status": "verified_for_stated_use",
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "opened_locator": "Theorem2.1 and hypotheses(1)–(8), original printed pp.101–102; auxiliary-function proof pp.102–103.",
    "actual_use": "The exact variable-degree interpolation inequality used to diagnose the division-value approach in C.7.11.",
    "hypotheses_and_normalization_check": "The degree bound is the joint field degree of all k values. Hypothesis(5) is d product_j max(d psi_j,theta_j(R)) <= c0 mu^(k-1) phi^k, with phi=log((R^2+r(N)r(N+1))/(R(r(N)+r(N+1)))); monotonicity and mu phi/d tending to infinity are also required. On fixed nested discs our proved degree/count estimates do not establish the decisive inequality. This is a failed sufficient certificate, not a lower bound on actual degrees or an impossibility theorem.",
    "citation_contexts": [
      {
        "file": "deliverables/work/invariants_arithmetic/sections/ari_division_values.tex",
        "line": 40,
        "context": " family on the real division grids is $O(n^5)$, with\nuniformly bounded heights.\n\nThese proved degree and height envelopes do not verify the\nvariable-degree criterion of Gramain--Mignotte--Waldschmidt\n\\citep[Theorem 2.1]{gramain1986values}.  This is a failure of the\navailable sufficient certificate, not a proof that the actual\ndegrees violate every possible application of that theorem.\n"
      },
      {
        "file": "deliverables/work/invariants_arithmetic/sections/ari_division_values.tex",
        "line": 122,
        "context": "t h(R)+O_E(1)$ uniformly over\n$E(\\overline\\Q)$.  Since\n$\\widehat h(R)=(m/n)^2\\widehat h(Q)$, the coordinate heights\nare uniformly bounded when $|m|\\leq n$.\nThe polynomial evaluation height inequality\n\\citep[Lemma 1.0]{gramain1986values} now gives\n$h(\\psi_n(R))=O_{E,Q}(n^2)$, and the same estimate for its\ninvariant derivative at torsion points.  Also\n\\[\n h(N(mQ))\\leq m^2h(N(Q))+O_{E,Q"
      }
    ],
    "extent": "The complete cited statement and its relevant surrounding hypotheses were opened. The application and its limits were checked independently; this is not a claim to reprove every external theorem.",
    "retrieval": {
      "key": "gramain1986values",
      "url": "https://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/AA/ActaArith47_1986.pdf",
      "file": "sources/audit_cache/inv_ari/literature/gramain1986values.pdf",
      "sha256": "c179051d1c5584b10f0728a6a2447a012fb3c0a0113f5424b64970c9ac086ed5",
      "bytes": 1040316,
      "kind": ".pdf"
    },
    "verified": true,
    "local_source": "sources/audit_cache/inv_ari/literature/gramain1986values.pdf",
    "source_sha256": "c179051d1c5584b10f0728a6a2447a012fb3c0a0113f5424b64970c9ac086ed5",
    "visual_check": "sources/audit_cache/inv_ari/literature/scans/gramain1986values-03.png and -04.png (printed pp.100–103), inspected visually.",
    "web_open_locator": "turn84view0; turn85view0"
  },
  {
    "citation_key": "herblot2012meromorphic",
    "status": "verified_for_stated_use",
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "opened_locator": "Theorem6.1 p.31, extracted text lines1814–1855, with the arithmetic-formal-curve hypotheses in its statement.",
    "actual_use": "Exact scope of the variable-residue-degree formal-curve alternative in C.7.11.",
    "hypotheses_and_normalization_check": "Projective variety over Q, formal curves over the residue number fields of the marked closed points, alpha_j-arithmetic estimates and a common meromorphic uniformization of order rho. The inequality involves sum 1/(alpha_j d_j). A transcendental tangent slope prevents the proposed germ from being defined over its residue number field.",
    "citation_contexts": [
      {
        "file": "deliverables/work/invariants_arithmetic/sections/ari_division_values.tex",
        "line": 44,
        "context": ".  This is a failure of the\navailable sufficient certificate, not a proof that the actual\ndegrees violate every possible application of that theorem.\nThe arithmetic-germ hypotheses in the criteria of\n\\citet[Theorem 6.1]{herblot2012meromorphic} and\n\\citet[Theorem 4.16]{gasbarri2010analytic} also remain unavailable;\nthe relevant nontorsion germs have a transcendental tangent.\n\\end{proposition"
      }
    ],
    "extent": "The complete cited statement and its relevant surrounding hypotheses were opened. The application and its limits were checked independently; this is not a claim to reprove every external theorem.",
    "retrieval": {
      "key": "herblot2012meromorphic",
      "url": "https://webusers.imj-prg.fr/~mathilde.herblot/publi/SL.pdf",
      "file": "sources/audit_cache/inv_ari/literature/herblot2012meromorphic.pdf",
      "sha256": "3c940dcecc68edca25fe11dd738ea91d20ff97582e1630d273ac1e0effb5866b",
      "bytes": 764126,
      "kind": ".pdf",
      "seconds": 15.128874778747559
    },
    "verified": true,
    "local_source": "sources/audit_cache/inv_ari/literature/herblot2012meromorphic.pdf",
    "source_sha256": "3c940dcecc68edca25fe11dd738ea91d20ff97582e1630d273ac1e0effb5866b"
  },
  {
    "citation_key": "gasbarri2010analytic",
    "status": "verified_for_stated_use",
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "opened_locator": "Definition2.1 and the setup, Definition3.7 pp.14–15, Theorem4.16 p.25 (extracted text lines312–333,806–837,1390–1425).",
    "actual_use": "Exact LG-germ and number-field assumptions in the alternative algebraicity criterion.",
    "hypotheses_and_normalization_check": "The formal germ is defined over the point’s number field, is analytic at finite places, and admits a good formal parameterization with the specified factorial denominator bounds outside a finite set of places. These are additional hypotheses, not consequences of algebraicity of a sequence of norm values.",
    "citation_contexts": [
      {
        "file": "deliverables/work/invariants_arithmetic/sections/ari_division_values.tex",
        "line": 45,
        "context": " certificate, not a proof that the actual\ndegrees violate every possible application of that theorem.\nThe arithmetic-germ hypotheses in the criteria of\n\\citet[Theorem 6.1]{herblot2012meromorphic} and\n\\citet[Theorem 4.16]{gasbarri2010analytic} also remain unavailable;\nthe relevant nontorsion germs have a transcendental tangent.\n\\end{proposition}\n\n\\begin{proof}\n\\emph{Propagation and degrees."
      }
    ],
    "extent": "The complete cited statement and its relevant surrounding hypotheses were opened. The application and its limits were checked independently; this is not a claim to reprove every external theorem.",
    "retrieval": {
      "key": "gasbarri2010analytic",
      "url": "https://preprints.ihes.fr/storage/newscheiderlang.pdf",
      "file": "sources/audit_cache/inv_ari/literature/gasbarri2010analytic.pdf",
      "sha256": "894afe05ea3984a91ee36d948d0921f3f7145a8faaac29abceed3f478b57cebb",
      "bytes": 385007,
      "kind": ".pdf",
      "seconds": 8.1949622631073
    },
    "verified": true,
    "local_source": "sources/audit_cache/inv_ari/literature/gasbarri2010analytic.pdf",
    "source_sha256": "894afe05ea3984a91ee36d948d0921f3f7145a8faaac29abceed3f478b57cebb"
  },
  {
    "citation_key": "adamczewski2017mahler",
    "status": "verified_for_stated_use",
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "opened_locator": "System(1.2), definition of regular argument and Theorem1.1, p.56.",
    "actual_use": "Mahler-method scope check after C.7.11.",
    "hypotheses_and_normalization_check": "Functions have algebraic Taylor coefficients and solve a linear system f(z)=A(z)f(z^q), A in GL_n(Qbar(z)); the algebraic argument is inside convergence and regular along its forward power orbit. No such representation has been obtained for the compact normalization and its rational Lattès map. The text does not rule out every possible alternative representation.",
    "citation_contexts": [
      {
        "file": "deliverables/work/invariants_arithmetic/sections/ari_division_values.tex",
        "line": 295,
        "context": "t even defined over $\\overline\\Q$;\nthe required arithmetic-germ hypothesis has not been gained\nby passing to division values.\n\\end{proof}\n\nWe also checked the Mahler-functional-equation route against\n\\citet[Theorem 1.1 and system (1.2)]{adamczewski2017mahler}.\nThat theorem requires algebraic Taylor coefficients, a linear\npower-map functional system and an algebraic regular argument.\nThe compact normalizati"
      }
    ],
    "extent": "The complete cited statement and its relevant surrounding hypotheses were opened. The application and its limits were checked independently; this is not a claim to reprove every external theorem.",
    "retrieval": {
      "key": "adamczewski2017mahler",
      "url": "https://faverjon.perso.math.cnrs.fr/AdamczewskiFaverjon_mahler1.pdf",
      "file": "sources/audit_cache/inv_ari/literature/adamczewski2017mahler.pdf",
      "sha256": "840b34c66d3a4d0d778d43ec8d0d13d1f6b0cddc199407d8358f18a63212ca4e",
      "bytes": 635930,
      "kind": ".pdf",
      "seconds": 6.304190635681152
    },
    "verified": true,
    "local_source": "sources/audit_cache/inv_ari/literature/adamczewski2017mahler.pdf",
    "source_sha256": "840b34c66d3a4d0d778d43ec8d0d13d1f6b0cddc199407d8358f18a63212ca4e"
  },
  {
    "citation_key": "einsiedler2001entropy",
    "status": "verified_for_stated_use",
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "opened_locator": "Section5, Theorem5.1 pp.9–10, definitions x(2^nQ)=a_n/b_n^2 and r(n)=4^n, with the full proof.",
    "actual_use": "Scope of the entropy interpretation of the canonical height.",
    "hypotheses_and_normalization_check": "The transformations are the nonautonomous sequence T_j(x)=b_j x on R, and the scale is 4^n. This is not the entropy of a single algebraic automorphism and does not provide algebraicity of the exponential of a height.",
    "citation_contexts": [
      {
        "file": "deliverables/work/invariants_arithmetic/sections/ari_division_values.tex",
        "line": 304,
        "context": "ic coordinate is a Latt\\`es map.  We have not obtained\na representation satisfying the stated hypotheses; we do not\nassert that every alternative representation is impossible.\nThe entropy identity of\n\\citet[Theorem 5.1]{einsiedler2001entropy} uses a sequence of\ntransformations built from the denominators of $x(2^nQ)$,\nwith scale $4^n$.  It does not identify the height with the\nentropy of a"
      }
    ],
    "extent": "The complete cited statement and its relevant surrounding hypotheses were opened. The application and its limits were checked independently; this is not a claim to reprove every external theorem.",
    "retrieval": {
      "key": "einsiedler2001entropy",
      "url": "https://people.math.ethz.ch/~einsiedl/height.pdf",
      "file": "sources/audit_cache/inv_ari/literature/einsiedler2001entropy.pdf",
      "sha256": "5b2f901e0e971b30421f02d26d22673d5264aa26f9641fa464b0de77fba9909c",
      "bytes": 242280,
      "kind": ".pdf",
      "seconds": 5.248764753341675
    },
    "verified": true,
    "local_source": "sources/audit_cache/inv_ari/literature/einsiedler2001entropy.pdf",
    "source_sha256": "5b2f901e0e971b30421f02d26d22673d5264aa26f9641fa464b0de77fba9909c"
  },
  {
    "citation_key": "waldschmidt1988periodrank",
    "status": "verified_for_stated_use",
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "opened_locator": "Theorem4.1 and formula(4.2), pp.385–386; Corollary4.3 p.386.",
    "actual_use": "Period-refined rank bound for the compact complex line of C.7.9/C.7.11.",
    "hypotheses_and_normalization_check": "A finitely generated subgroup Y of V exponentiates to algebraic points; kappa is rank(Y intersect ker exp). For a Zariski-dense one-dimensional analytic subgroup, Corollary4.3 bounds total rank by (d1+2d2-kappa)/(d-1). For the nonsplit two-dimensional G_Q, d0=d1=0,d2=2,kappa=1, so the allowed rank is3 and the available rank2 gives no contradiction. d1 is a multiplicative quotient dimension, not the torus-subgroup dimension.",
    "citation_contexts": [
      {
        "file": "deliverables/work/invariants_arithmetic/sections/ari_division_values.tex",
        "line": 312,
        "context": "a single finite-dimensional algebraic automorphism,\nand supplies no algebraic value for its exponential.\n\nThe period-refined algebraic-group rank theorem has also been\nchecked in the original sources\n\\citep[Theorem 4.1 and Corollary 4.3]{waldschmidt1988periodrank}\n\\citep[main theorem, p.~363]{roy1993periodrank}.\nIts coefficient is\n$\\alpha(G)=2\\dim G-2d_0(G)-d_1(G)$, where $d_1$\ncounts multiplicative \\emph{quoti"
      }
    ],
    "extent": "The complete cited statement and its relevant surrounding hypotheses were opened. The application and its limits were checked independently; this is not a claim to reprove every external theorem.",
    "retrieval": {
      "key": "waldschmidt1988periodrank",
      "url": "https://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/Durham1986TMGSSV.pdf",
      "file": "sources/audit_cache/inv_ari/literature/waldschmidt1988periodrank.pdf",
      "sha256": "d4615aec78b11a4d4dfb0795e103c256df52f4bf4140f9d3990802d79a04017e",
      "bytes": 767740,
      "kind": ".pdf",
      "seconds": 10.012282371520996
    },
    "verified": true,
    "local_source": "sources/audit_cache/inv_ari/literature/waldschmidt1988periodrank.pdf",
    "source_sha256": "d4615aec78b11a4d4dfb0795e103c256df52f4bf4140f9d3990802d79a04017e",
    "visual_check": "sources/audit_cache/inv_ari/literature/scans/waldschmidt1988periodrank-06.png and -07.png (printed pp.384–387), inspected visually."
  },
  {
    "citation_key": "roy1993periodrank",
    "status": "verified_for_stated_use",
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "opened_locator": "Definition of d0,d1,alpha on p.359; main theorem p.363, conditions(i)–(iii); proof pp.363–364.",
    "actual_use": "Independent, refined algebraic-group rank statement used after C.7.11.",
    "hypotheses_and_normalization_check": "Psi is rational over Qbar, W is a Qbar-rational subspace of V, and V contains no nonzero obstruction subspace Psi(S). The bound is (alpha_K(G)-kappa) dim(V/W). For K=Q, nonsplit G_Q has alpha=4 and kappa=1. Its compact line has no nonzero algebraic vector, so W=0 and the bound permits rank3.",
    "citation_contexts": [
      {
        "file": "deliverables/work/invariants_arithmetic/sections/ari_division_values.tex",
        "line": 313,
        "context": "no algebraic value for its exponential.\n\nThe period-refined algebraic-group rank theorem has also been\nchecked in the original sources\n\\citep[Theorem 4.1 and Corollary 4.3]{waldschmidt1988periodrank}\n\\citep[main theorem, p.~363]{roy1993periodrank}.\nIts coefficient is\n$\\alpha(G)=2\\dim G-2d_0(G)-d_1(G)$, where $d_1$\ncounts multiplicative \\emph{quotients}, not the dimension of\nthe torus subgroup. "
      }
    ],
    "extent": "The complete cited statement and its relevant surrounding hypotheses were opened. The application and its limits were checked independently; this is not a claim to reprove every external theorem.",
    "retrieval": {
      "key": "roy1993periodrank",
      "url": "https://www.cambridge.org/core/services/aop-cambridge-core/content/view/A1E35F3798690D084664ACD83D1557E8/S0008439500013138a.pdf/autour_du_theoreme_du_sousgroupe_algebrique.pdf",
      "file": "sources/audit_cache/inv_ari/literature/roy1993periodrank.pdf",
      "sha256": "6c71e58c55a258d96e42231562a789f0cdccb7d85db54a3e34bdddbcd57fb2ef",
      "bytes": 969866,
      "kind": ".pdf"
    },
    "verified": true,
    "local_source": "sources/audit_cache/inv_ari/literature/roy1993periodrank.pdf",
    "source_sha256": "6c71e58c55a258d96e42231562a789f0cdccb7d85db54a3e34bdddbcd57fb2ef",
    "url": "https://www.cambridge.org/core/services/aop-cambridge-core/content/view/A1E35F3798690D084664ACD83D1557E8/S0008439500013138a.pdf/autour_du_theoreme_du_sousgroupe_algebrique.pdf",
    "web_open_locator": "turn84view2 lines48–64,170–237; turn85view2"
  },
  {
    "citation_key": "CrDarmon2009",
    "status": "verified_for_stated_use",
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "opened_locator": "Section 3, pp.4–5, Assumption 3.1 and the definition of the canonical Hecke character/theta series (extracted text lines160–220).",
    "actual_use": "Exact CM theta coefficients used by Crank_cm_stream.cpp and the Gross–Zagier interval regeneration.",
    "hypotheses_and_normalization_check": "Imaginary quadratic class number one, unit group {+1,-1}, odd prime discriminant D=7,11,19,43,67,163; canonical curve conductor D^2 and psi((a))=epsilon_D(a mod sqrt(-D))a. The half-sum over nonzero lattice elements becomes the real paired coefficient used in the integer stream. No generalized-cycle statement is used.",
    "citation_contexts": [
      {
        "file": "deliverables/work/invariants_arithmetic/sections/ari_gz_factors.tex",
        "line": 250,
        "context": "$. Hecke's theta construction\nplaces $\\sum_{\\mathfrak a}\\psi(\\mathfrak a)q^{N\\mathfrak a}$ in\n$S_2(\\Gamma_0(s^2))$: the nebentypus is\n$\\chi_{-s}(n)(n/s)=1$. This exact special case is also written\nin \\citet[\\S3, pp.~4--5]{CrDarmon2009}. Grouping conjugate\ngenerators $\\alpha=(u+v\\sqrt{-s})/2$ gives the integral formula\nused by the coefficient stream:\n\\[\n b_n=\\sum_{a^2=n,\\ a>0}\\left(\\"
      },
      {
        "file": "deliverables/work/invariants_arithmetic/sections/ari_rank.tex",
        "line": 178,
        "context": "               \\ u\\equiv v\\pmod2\\right).\n\\]\nThis is the Hecke-character theta series for\n$\\mathcal O_{\\Q(\\sqrt{-D})}$, grouping conjugate algebraic integers\nand then applying the quadratic twist; see\n\\citet[Section 3]{CrDarmon2009}. The first 10000 coefficients agree\nexactly with PARI for both the untwisted and twisted curve. The same\ncode at $D=67,d=217$ reproduces the independ"
      }
    ],
    "extent": "The complete cited statement and its relevant surrounding hypotheses were opened. The application and its limits were checked independently; this is not a claim to reprove every external theorem.",
    "retrieval": {
      "key": "CrDarmon2009",
      "url": "https://www.math.mcgill.ca/darmon/pub/Articles/Expository/13.Oberwolfach/paper.pdf",
      "file": "sources/audit_cache/inv_ari/literature/CrDarmon2009.pdf",
      "sha256": "c9eff395aabcbe1237bb2add9d152655b68f4209b7eae342aa5600c8b653292d",
      "bytes": 190217,
      "kind": ".pdf",
      "seconds": 4.8257997035980225
    },
    "verified": true,
    "local_source": "sources/audit_cache/inv_ari/literature/CrDarmon2009.pdf",
    "source_sha256": "c9eff395aabcbe1237bb2add9d152655b68f4209b7eae342aa5600c8b653292d"
  },
  {
    "citation_key": "waldschmidt1988theta",
    "status": "verified_for_stated_use",
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "opened_locator": "Original published exposition, p.15-03 (CM normalized sigma result and regularized s2), p.15-05 (periodic functional-equation theorem).",
    "actual_use": "Verified published statement of transcendence of the holomorphic normalized sigma value; precise exclusion of the algebraic-q route for CM tau.",
    "hypotheses_and_normalization_check": "The lattice has algebraic invariants, E has CM and exp_E(u) is algebraic nontorsion; the asserted value is sigma(u)exp(-s2 u^2/2), where s2 is the explicitly regularized lattice sum. This concerns the holomorphic value, not its Hermitian norm. The periodic functional-equation theorem assumes q=exp(i pi tau) in a number field; CM tau makes this q transcendental. The exposition attributes the first theorem to Bertrand1982; it is not a claim that the inaccessible original proof was read.",
    "citation_contexts": [
      {
        "file": "deliverables/work/invariants_arithmetic/sections/ari_cm_transcendence.tex",
        "line": 166,
        "context": "tion\nof that criterion here. The withdrawn text and the lift audit\nare retained in the records.\n\nA subsequent source check resolves the normalization of the\none-variable holomorphic assertion itself:\n\\citet[p.~15-03]{waldschmidt1988theta} explicitly states that\n$\\sigma(u)e^{-s_2u^2/2}$ is transcendental when the invariants\nare algebraic, $E$ has CM, and $\\exp_Eu$ is an algebraic\nnontor"
      },
      {
        "file": "deliverables/work/invariants_arithmetic/sections/ari_cm_transcendence.tex",
        "line": 215,
        "context": "u)$ algebraic, so the conclusion instead forces independence\nof $e^{i\\pi u/\\omega_1}$ and\n$\\zeta(u)-\\eta_1u/\\omega_1$; it yields no contradiction.\nThe periodic-functional-equation theorem reported in\n\\citet[p.~15-05]{waldschmidt1988theta} assumes algebraic\n$q=e^{i\\pi\\tau}$, whereas this $q$ is transcendental for\nimaginary quadratic $\\tau$ by Gelfond--Schneider.  These\nspecific checked "
      }
    ],
    "extent": "The complete cited statement and its relevant surrounding hypotheses were opened. The application and its limits were checked independently; this is not a claim to reprove every external theorem.",
    "retrieval": {
      "key": "waldschmidt1988theta",
      "url": "https://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/PPN320141322_0016__0_0.pdf",
      "file": "sources/audit_cache/inv_ari/literature/waldschmidt1988theta.pdf",
      "sha256": "10a3ef68f8b7f7f8bd73df459a6907b7ea2b5ba2da4efbadf19bfa90e11ba42f",
      "bytes": 527851,
      "kind": ".pdf",
      "seconds": 3.094747543334961
    },
    "verified": true,
    "local_source": "sources/audit_cache/inv_ari/literature/waldschmidt1988theta.pdf",
    "source_sha256": "10a3ef68f8b7f7f8bd73df459a6907b7ea2b5ba2da4efbadf19bfa90e11ba42f",
    "visual_check": "sources/audit_cache/inv_ari/literature/scans/waldschmidt1988theta-04.png and -06.png, printed pp.15-03 and15-05, inspected visually."
  },
  {
    "citation_key": "reyssat1982weierstrass",
    "status": "verified_for_stated_use",
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "opened_locator": "Corollary2, first page and proof Section5.1, original Acta Arithmetica paper.",
    "actual_use": "Precise independence statement for the alternative normalized sigma function in C.7.7.",
    "hypotheses_and_normalization_check": "Algebraic Weierstrass invariants, a nonzero period omega and an elliptic logarithm u of an algebraic nontorsion point. At least two of exp(pi i u/omega), s_omega(u), s_omega_prime(u) are algebraically independent. This does not assert that s_omega(u) alone is transcendental; if it were algebraic, the other two can account for the required independence.",
    "citation_contexts": [
      {
        "file": "deliverables/work/invariants_arithmetic/sections/ari_cm_transcendence.tex",
        "line": 207,
        "context": " which C.7.7 excludes.\nReplacing the norm by the holomorphic theta value would\ntherefore change the problem precisely by the factor in\n\\eqref{ari:eq:ct-Gaussian}.\n\nThe related independence theorem of\n\\citet[Corollary~2]{reyssat1982weierstrass} says that two of\n$e^{i\\pi u/\\omega_1}$, $s(u)$ and $s'(u)$ are algebraically\nindependent, where $s(z)=\\sigma(z)e^{-\\eta_1z^2/(2\\omega_1)}$.\nFor real "
      }
    ],
    "extent": "The complete cited statement and its relevant surrounding hypotheses were opened. The application and its limits were checked independently; this is not a claim to reprove every external theorem.",
    "retrieval": {
      "key": "reyssat1982weierstrass",
      "url": "https://matwbn.icm.edu.pl/ksiazki/aa/aa41/aa4137.pdf",
      "error": "HTTP Error 403: Forbidden",
      "seconds": 5.261593818664551
    },
    "verified": true,
    "url": "https://matwbn.icm.edu.pl/ksiazki/aa/aa41/aa4137.pdf",
    "web_open_locator": "turn84view1; turn85view1, Corollary2 lines50–55 and proof lines665–686"
  },
  {
    "citation_key": "nguyen2023",
    "status": "verified_for_stated_use",
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "opened_locator": "Theorem1.4 and Corollary1.6, p.3 (extracted text lines105–145).",
    "actual_use": "Scope check of a polynomial canonical-height/Böttcher-coordinate route; no application to prove the Lattès norm.",
    "hypotheses_and_normalization_check": "Nonintegrable polynomial dynamics and an argument in the Böttcher domain are essential. Corollary1.6 gives algebraicity only in the bounded-conjugates case. The family uses a rational Lattès map and does not satisfy these polynomial hypotheses.",
    "citation_contexts": [
      {
        "file": "deliverables/work/invariants_arithmetic/sections/ari_cm_transcendence.tex",
        "line": 242,
        "context": ")$. Its canonical height is\n$\\widehat h_{f_E}(x(P))=2\\widehat h_O(P)$. For rational\nparameters C.6 therefore makes algebraicity of $N(P)$\nequivalent to algebraicity of\n$\\exp(\\widehat h_{f_E}(x(P)))$.\n\\citet[Theorem 1.4 and Corollary 1.6]{nguyen2023} settle the\ncorresponding multiplicative-height problem for nonintegrable\npolynomials using B\\\"ottcher coordinates in the basin of\ninfinity. They do n"
      }
    ],
    "extent": "The complete cited statement and its relevant surrounding hypotheses were opened. The application and its limits were checked independently; this is not a claim to reprove every external theorem.",
    "retrieval": {
      "key": "nguyen2023",
      "url": "https://arxiv.org/pdf/2112.14937",
      "file": "sources/audit_cache/inv_ari/literature/nguyen2023.pdf",
      "sha256": "f9b846a101b94ef098e5f35e45e0132b8dd1f54bd9f3d4d2c7a48610856499fd",
      "bytes": 228861,
      "kind": ".pdf",
      "seconds": 4.474793195724487
    },
    "verified": true,
    "local_source": "sources/audit_cache/inv_ari/literature/nguyen2023.pdf",
    "source_sha256": "f9b846a101b94ef098e5f35e45e0132b8dd1f54bd9f3d4d2c7a48610856499fd"
  },
  {
    "citation_key": "xie2024algebraicity",
    "status": "verified_for_stated_use",
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "opened_locator": "Theorem1.3 p.3 and Theorem2.3 p.12 (extracted text lines125–165 and640–670).",
    "actual_use": "Check of the quantitative algebraicity criterion for the compact leaf in C.7.11.",
    "hypotheses_and_normalization_check": "A local analytic germ defined over a fixed number field and points rational over that field, together with the stated positive approximation/height lower ratio, are required. The proposed compact-leaf germ has a transcendental tangent slope, so the field-of-definition hypothesis fails before any approximation estimate is considered.",
    "citation_contexts": [
      {
        "file": "deliverables/work/invariants_arithmetic/sections/ari_cm_transcendence.tex",
        "line": 256,
        "context": " of infinity is absent. This checks\nthe failed hypothesis, rather than treating a theorem for\npolynomials as a theorem for all rational maps.\n\nWe also checked the arithmetic algebraicity criterion of\n\\citet[Theorems 1.3 and 2.3]{xie2024algebraicity}.\nBesides sufficiently rapid height-normalized approximation by\npoints in a fixed number field, it requires the analytic germ\nto be formally defined o"
      }
    ],
    "extent": "The complete cited statement and its relevant surrounding hypotheses were opened. The application and its limits were checked independently; this is not a claim to reprove every external theorem.",
    "retrieval": {
      "key": "xie2024algebraicity",
      "url": "https://arxiv.org/pdf/2202.09032",
      "file": "sources/audit_cache/inv_ari/literature/xie2024algebraicity.pdf",
      "sha256": "fe1c93d499dfac09d15a4a7595aa9040d67e779f1cf5c3ec32a4b78c93614dab",
      "bytes": 591980,
      "kind": ".pdf",
      "seconds": 9.697959184646606
    },
    "verified": true,
    "local_source": "sources/audit_cache/inv_ari/literature/xie2024algebraicity.pdf",
    "source_sha256": "fe1c93d499dfac09d15a4a7595aa9040d67e779f1cf5c3ec32a4b78c93614dab"
  },
  {
    "citation_key": "pham2025sigma",
    "status": "unverified_original_not_used_for_strengthening",
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "opened_locator": "Publisher abstract only; no proof or precise hypotheses opened, and no theorem is invoked from it.",
    "actual_use": "See the exact printed citation contexts; no theorem status is inferred from retrieval alone.",
    "hypotheses_and_normalization_check": "Publisher abstract only; no proof or precise hypotheses opened, and no theorem is invoked from it.",
    "citation_contexts": [
      {
        "file": "deliverables/work/invariants_arithmetic/sections/ari_cm_transcendence.tex",
        "line": 277,
        "context": "o\nNorthcott finiteness. The full hypothesis audit and the opened\npreprint are retained in the records.\n\n\\paragraph{A current source whose theorem text remains unchecked.}\nThe publisher's abstract for \\citet{pham2025sigma} announces\ncomplex and $p$-adic linear-independence results for semiabelian\nvarieties and applications to Weierstrass sigma functions.\nWe opened its m"
      }
    ],
    "extent": "Original relevant statement and surrounding hypotheses opened; no claim that the entire external proof has been re-proved.",
    "verified": false
  },
  {
    "citation_key": "DuGuoKusakabeXie2026v1",
    "status": "verified_for_stated_use",
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "opened_locator": "v5oka_maps_modifications_deformations.tex intro lines300–345; Theorem6.12 (p2:thm:tangent-cohomology) lines9445–9487; Corollary6.13 lines9490ff.; Proposition6.16 (p2:prop:kuranishi-line) lines9876–9917; connected automorphisms lines9967–10010. Also §6: weighted-root-base lemma and proof lines8541–8614; root-stack-lift and proper-flat-root-fibration lines8628–8727; cusp-normalization-resolution and cusp-structure-cup lines8768–8877; vertical-log-bundle lines8897–9000; log-tangent-sequence lines9017–9048; structure-direct-images statement and relevant proof lines9154–9235,9275–9306; vertical/horizontal/log tangent calculation lines9312–9364. §7 intrinsic-fibration theorem and proof lines10018–10120. Theorem1.4 exact-period statement lines335–344.",
    "actual_use": "Credit for original-family tangent cohomology (1,1,1,0), nonzero parameter Kodaira–Spencer map, smooth reduced one-dimensional Kuranishi germ; original-family classification and automorphisms in Theorem1.4.",
    "hypotheses_and_normalization_check": "This is the historical first version. The exact statements are known-source duplicates of INV D1.3–D3.1/FAM A5.2; the printed explicit Koszul and gluing proofs are preserved. The second version omits these results, which alone is not a mathematical refutation.",
    "citation_contexts": [
      {
        "file": "deliverables/work/invariants_arithmetic/sections/ari_special.tex",
        "line": 189,
        "context": "nvariance at rational boundary\npoints and is valid. The existence criterion and exact $2\\mathbb Z$\nidentification are R4 and R5; the latter is also Theorem~1.4\n(label \\texttt{p2:thm:exact-period}) of\n\\cite{DuGuoKusakabeXie2026v1}. Its hypotheses specify precisely the\nretained period family, affine finite twists and cusp collar. They\ncoincide with the family in this prompt; the"
      },
      {
        "file": "deliverables/work/invariants_arithmetic/sections/ari_special.tex",
        "line": 271,
        "context": "c\\in1/2+\\mathbb Z$, iff\n$w=-\\bar w$, iff $q_2=iw/216$ is real. Its square is a holomorphic\ntranslation $d_0\\in\\mathbb C/\\mathbb Z$, since the automorphism group\nis the $\\mathbb C^*$ of Theorem~1.4 of\n\\cite{DuGuoKusakabeXie2026v1}. The constructed reflection acts on\nthis additive translation coordinate by conjugation. Commutation\nwith its square gives $d_0=\\bar d_0$ in $\\mathbb"
      }
    ],
    "extent": "Original relevant statement and surrounding hypotheses opened; no claim that the entire external proof has been re-proved.",
    "local_source": "sources/papers/arXiv_2610.00250v1_Du_Guo_Kusakabe_Xie_src/v5oka_maps_modifications_deformations.tex",
    "source_sha256": "924a4a72d80793927f3104121a44786ea2b9869ae6ea2bca5a6a69553ab2884e",
    "same_source_as": "DuEtAl2026v1",
    "verified": true
  },
  {
    "citation_key": "callSilverman1993",
    "status": "verified_for_stated_use",
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "opened_locator": "Theorem4.1 and following elliptic-family remark, pp.183–184; full setup on p.183.",
    "actual_use": "General specialization limit and author reproduction of Tate’s stronger elliptic-family bounded-variation theorem in C.6.4.",
    "hypotheses_and_normalization_check": "Smooth projective one-dimensional base, degree-one base height, a section, and a fibrewise morphism multiplying the chosen divisor class by alpha>1. Theorem4.1 is the ratio limit. The following remark separately states hhat(P_t)=h_{T,D_P}(t)+O_P(1), deg D_P=hhat(P_generic), for elliptic families. The explicit 1/2 log2 bound is proved locally in this manuscript and is not attributed to the general theorem.",
    "citation_contexts": [
      {
        "file": "deliverables/work/invariants_arithmetic/sections/ari_heights.tex",
        "line": 300,
        "context": "estimate with\nconstant $\\frac12\\log2$; the general bounded-variation\nstatement alone does not supply that constant.\n\nWe spell out the comparison with the opened primary author sources.\nTheorem 4.1 of \\citet[pp.~183--184]{callSilverman1993} concerns a\nsmooth projective base curve $T$, a degree-one base height $h_T$,\na section, and a fibrewise morphism whose pullback multiplies the\nchosen"
      }
    ],
    "extent": "The complete cited statement and its relevant surrounding hypotheses were opened. The application and its limits were checked independently; this is not a claim to reprove every external theorem.",
    "retrieval": {
      "key": "callSilverman1993",
      "url": "https://www.numdam.org/item/CM_1993__89_2_163_0.pdf",
      "file": "sources/audit_cache/inv_ari/literature/callSilverman1993.pdf",
      "sha256": "01a4cd0c246182c6496dcddb1f43e4343d17db4f55a22d73f35d057190bc0586",
      "bytes": 2969316,
      "kind": ".pdf",
      "seconds": 33.26794362068176
    },
    "verified": true,
    "local_source": "sources/audit_cache/inv_ari/literature/callSilverman1993.pdf",
    "source_sha256": "01a4cd0c246182c6496dcddb1f43e4343d17db4f55a22d73f35d057190bc0586",
    "visual_check": "sources/audit_cache/inv_ari/literature/scans/callSilverman1993-22.png and -23.png (printed pp.183–184), inspected visually."
  },
  {
    "citation_key": "tate1983variation",
    "status": "unverified_original_not_used_for_strengthening",
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "opened_locator": "Original full paper not obtained; the actual invoked specialization statement is checked in Call–Silverman1993 and Silverman2006 below.",
    "actual_use": "See the exact printed citation contexts; no theorem status is inferred from retrieval alone.",
    "hypotheses_and_normalization_check": "Original full paper not obtained; the actual invoked specialization statement is checked in Call–Silverman1993 and Silverman2006 below.",
    "citation_contexts": [
      {
        "file": "deliverables/work/invariants_arithmetic/sections/ari_heights.tex",
        "line": 319,
        "context": "rmula\n$\\widehat h_t(P_t)=h_{T,D_P}(t)+O_P(1)$, with\n$\\deg D_P=\\widehat h_{\\Q(T)}(P)$. This is an author-verified\nreproduction of Tate's result, not a claim to have read the\ninaccessible original scan \\citep{tate1983variation}.\nThe same distinction applies to \\citet{silverman1983specialization}:\nthe limit theorem is reproduced by the author on slide~22 of\n\\citet{silverman20"
      }
    ],
    "extent": "Original relevant statement and surrounding hypotheses opened; no claim that the entire external proof has been re-proved.",
    "verified": false
  },
  {
    "citation_key": "silverman1983specialization",
    "status": "unverified_original_not_used_for_strengthening",
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "opened_locator": "Original full paper not obtained; the actual invoked specialization statement is checked in Call–Silverman1993 and Silverman2006 below.",
    "actual_use": "See the exact printed citation contexts; no theorem status is inferred from retrieval alone.",
    "hypotheses_and_normalization_check": "Original full paper not obtained; the actual invoked specialization statement is checked in Call–Silverman1993 and Silverman2006 below.",
    "citation_contexts": [
      {
        "file": "deliverables/work/invariants_arithmetic/sections/ari_heights.tex",
        "line": 320,
        "context": "_P=\\widehat h_{\\Q(T)}(P)$. This is an author-verified\nreproduction of Tate's result, not a claim to have read the\ninaccessible original scan \\citep{tate1983variation}.\nThe same distinction applies to \\citet{silverman1983specialization}:\nthe limit theorem is reproduced by the author on slide~22 of\n\\citet{silverman2006heights}, while slide~21 states the uniform\ncanonical-versus-Weil-h"
      }
    ],
    "extent": "Original relevant statement and surrounding hypotheses opened; no claim that the entire external proof has been re-proved.",
    "verified": false
  },
  {
    "citation_key": "silverman2006heights",
    "status": "verified_for_stated_use",
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "opened_locator": "Original author slides21–22, extracted text lines478–510.",
    "actual_use": "Author reproduction of the 1983 specialization limit and uniform canonical-versus-Weil height bound.",
    "hypotheses_and_normalization_check": "Slide21 bounds the height difference by c1 h_T(t)+c2. Slide22 gives the specialization ratio limit. The constant-part condition belongs to the subsequent injectivity corollary, not to the limit theorem. The unavailable 1983 original is explicitly identified as not opened.",
    "citation_contexts": [
      {
        "file": "deliverables/work/invariants_arithmetic/sections/ari_heights.tex",
        "line": 322,
        "context": "o have read the\ninaccessible original scan \\citep{tate1983variation}.\nThe same distinction applies to \\citet{silverman1983specialization}:\nthe limit theorem is reproduced by the author on slide~22 of\n\\citet{silverman2006heights}, while slide~21 states the uniform\ncanonical-versus-Weil-height bound in terms of the base height.\nFor our explicit bounded remainder and local norma"
      }
    ],
    "extent": "The complete cited statement and its relevant surrounding hypotheses were opened. The application and its limits were checked independently; this is not a claim to reprove every external theorem.",
    "retrieval": {
      "key": "silverman2006heights",
      "url": "https://slmath-production-assets.sfo3.digitaloceanspaces.com/attachments/workshops/301/HtSurveyMSRIJan06.pdf",
      "file": "sources/audit_cache/inv_ari/literature/silverman2006heights.pdf",
      "sha256": "f645a11dafb66b7cce33b48e32534e555f761a943ff4440f0d826f070ec1f5bf",
      "bytes": 233539,
      "kind": ".pdf",
      "seconds": 4.174625635147095
    },
    "verified": true,
    "local_source": "sources/audit_cache/inv_ari/literature/silverman2006heights.pdf",
    "source_sha256": "f645a11dafb66b7cce33b48e32534e555f761a943ff4440f0d826f070ec1f5bf"
  },
  {
    "citation_key": "CrRubin1991",
    "status": "unverified_original_not_used_for_strengthening",
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "opened_locator": "Complete original theorem text not obtained; metadata only. No additional hypothesis-free consequence is based on it. Verified replacement formulations are CrBDP2012 and CrCastella2025.",
    "actual_use": "See the exact printed citation contexts; no theorem status is inferred from retrieval alone.",
    "hypotheses_and_normalization_check": "Complete original theorem text not obtained; metadata only. No additional hypothesis-free consequence is based on it. Verified replacement formulations are CrBDP2012 and CrCastella2025.",
    "citation_contexts": [
      {
        "file": "deliverables/work/invariants_arithmetic/sections/ari_rank.tex",
        "line": 401,
        "context": "n\nhas a different-conductor hypothesis at $2$ that fails, and we\ndo not claim that this particular formulation proves its full\nleading-term formula. Rubin's original ordinary main-conjecture\npaper is \\citep{CrRubin1991}; its bibliographic record was checked,\nbut its complete theorem text was not available in the opened\npublisher copy, so no additional hypothesis-free"
      }
    ],
    "extent": "Original relevant statement and surrounding hypotheses opened; no claim that the entire external proof has been re-proved.",
    "verified": false
  },
  {
    "citation_key": "Friedman2016AB",
    "citation_contexts": [],
    "status": "verified_for_stated_use",
    "verified": true,
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "opened_locator": "Definition1.1 and Lemma1.2 pp.4–5; Lemma2.2 p.11; Theorem2.4 pp.12–13 and Lemma2.7 p.14.",
    "actual_use": "Rational anticanonical-pair charge used in PUSH B.4.28: Q=Euler(Y minus D)>=0 and Q=0 exactly for toric pairs.",
    "hypotheses_and_normalization_check": "The standing pair is a smooth projective rational surface and a reduced anticanonical cycle, including the one-component nodal case. No negative-definiteness assumption is required by Lemma2.7. Interior blowups increase Q by1; corner blowups preserve it. Inspection of the complete minimal-pair list plus these blowup rules proves the characterization. These hypotheses match the rational normalized components after the proof reduces to anticanonical cycles.",
    "extent": "The complete cited statement and its relevant surrounding hypotheses were opened. The application and its limits were checked independently; this is not a claim to reprove every external theorem.",
    "local_source": "sources/external/root/retrieved/Friedman2016AB.pdf",
    "source_sha256": "6e21e896c33c3397b316763493c8994c1773dc0787496fcc3af0a0b682dd2d92",
    "url": "https://arxiv.org/pdf/1502.02560"
  },
  {
    "citation_key": "Dloussky2005AB",
    "citation_contexts": [],
    "status": "verified_for_stated_use",
    "verified": true,
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "opened_locator": "Definition2.20 and standing VII_0^+ hypotheses p.14; Corollary2.25 pp.16–17; Lemma2.26 p.17; Proposition2.27 and complete proof pp.17–19.",
    "actual_use": "Classification of a minimal class VII component with reduced actual anticanonical divisor in PUSH B.4.28.",
    "hypotheses_and_normalization_check": "Minimality and b2>0 are standing assumptions. A global spherical shell is not assumed. Corollary2.25 gives a cycle in the NAC support; an actual reduced anticanonical divisor is the m=1,F=0 case and has coefficient1 on that cycle. Lemma2.26 removes branches, and Proposition2.27(i) gives an Inoue or Inoue–Hirzebruch surface. The proof explicitly includes the square-zero/Enoki case, which with NAC is the parabolic Inoue case. The half-Inoue alternative is excluded separately by the absence of an actual anticanonical divisor.",
    "extent": "The complete cited statement and its relevant surrounding hypotheses were opened. The application and its limits were checked independently; this is not a claim to reprove every external theorem.",
    "local_source": "sources/external/root/retrieved/Dloussky2005AB.pdf",
    "source_sha256": "f461b07b3bb60a6c1433172a5514fa6e90a41e43dac6f23396a4713d99f5c3f9",
    "url": "https://arxiv.org/pdf/math/0406387"
  },
  {
    "citation_key": "FujikiPontecorvo2010AB",
    "citation_contexts": [],
    "status": "verified_for_stated_use",
    "verified": true,
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "opened_locator": "Sections3.2–3.3, printed pp.20–22, definitions and equations(8)–(10), Lemmas3.2–3.3.",
    "actual_use": "Identify the parabolic/hyperbolic/half Inoue cases and their canonical divisors in PUSH B.4.28.",
    "hypotheses_and_normalization_check": "Hyperbolic has two rational cycles; parabolic has one rational cycle and one elliptic curve; these are the unique maximal reduced curves and satisfy -K=C, also after corner blowups. Half Inoue has empty |-K| and C in |-(K+L)| for nontrivial two-torsion L. Lemmas3.2–3.3 themselves additionally assume pi1=Z and a disconnected anticanonical curve: they are NOT used to classify an arbitrary class VII component before Dloussky’s result. For the parabolic case C_cycle^2=0 and K^2=-b2 imply E^2=-b2.",
    "extent": "The complete cited statement and its relevant surrounding hypotheses were opened. The application and its limits were checked independently; this is not a claim to reprove every external theorem.",
    "local_source": "sources/external/root/retrieved/FujikiPontecorvo2010AB.pdf",
    "source_sha256": "83bebf4558568c1c779cada41f6a192e22f689dc105ae0583bdab4b81d788773",
    "url": "https://archive.ymsc.tsinghua.edu.cn/pacm_download/21/834-JDG-85-1-A2-fujiki.pdf"
  },
  {
    "citation_key": "Oda1978D",
    "citation_contexts": [],
    "status": "verified_for_stated_use",
    "verified": true,
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "opened_locator": "Section15, definitions of U_N and U_N^+ pp.128–129; Theorem15.1 and its complete geometric proof/sketch pp.130–131.",
    "actual_use": "Toric-lattice description and complement topology of a hyperbolic Inoue–Hirzebruch surface in PUSH B.4.28.",
    "hypotheses_and_normalization_check": "N is a rank2 lattice in a real quadratic field. Multiplication by the generator of the totally positive unit group U_N^+ acts on N with determinant1 and positive reciprocal unequal eigenvalues, hence is hyperbolic. The first/fourth quadrant toric construction has two cycles; the complement is R times a compact-real-torus bundle over S1. The half quotient uses U_N rather than U_N^+ and is not substituted for the two-cycle case. The rank of T-I is2 over Q. Adjacent smooth toric rays supply the primitive angular lattice used by the manuscript.",
    "extent": "The complete cited statement and its relevant surrounding hypotheses were opened. The application and its limits were checked independently; this is not a claim to reprove every external theorem.",
    "local_source": "sources/external/root/retrieved/Oda1978D.pdf",
    "source_sha256": "84d3af61db92c6c239c4b7a59d9a4ce840f6d4952a45dfc9f05c6af3aed18f0c",
    "url": "https://mathweb.tifr.res.in/Documents/Publications/Lectures/tifr58.pdf"
  },
  {
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "citation_key": "AtiyahSinger1963",
    "title": "The index of elliptic operators on compact manifolds",
    "url": "https://scispace.com/pdf/the-index-of-elliptic-operators-on-compact-manifolds-3n33719pz0.pdf",
    "status": "verified_for_stated_use",
    "verified": true,
    "opened_locator": "Original journal scan, §3.2 and Theorem 3, published p.427 (PDF p.6); preceding definition of the index, pp.422–425.",
    "actual_use": "Hirzebruch–Riemann–Roch for the holomorphic cotangent bundle in the parameterized Hodge calculation.",
    "hypotheses_and_normalization_check": "The theorem explicitly allows every compact complex manifold and every holomorphic vector bundle. Hermitian metrics define the elliptic Dolbeault operator; no Kähler or projectivity hypothesis occurs. Its Todd class is that of the complex tangent bundle. The appendix independently expands ch(Omega^1) and Td, using c1=c2=0 and integral c3=2.",
    "local_source": null,
    "source_sha256": null,
    "web_refs": [
      "turn168view1",
      "turn169view0"
    ],
    "aliases": [],
    "citation_contexts": [
      {
        "file": "deliverables/work/invariants_arithmetic/working_hodge_frolicher_proofs.tex",
        "line": 124,
        "context": "1c_2,\\\\\n \\operatorname{ch}(\\Omega_X^1)\n &=3-c_1+\\frac12(c_1^2-2c_2)\n   -\\frac16(c_1^3-3c_1c_2+3c_3).\n\\end{align*}\nHirzebruch--Riemann--Roch for arbitrary compact complex manifolds\n\\cite[Theorem~3, p.~427]{AtiyahSinger1963} hence gives\n\\[\n \\chi(\\Omega_X^1)=-\\frac12\\int_Xc_3=-1.\n\\]\nThe already known zero entries reduce this identity to\n$-h^{1,1}+h^{1,2}=-1$, proving $h^{1,1}=m+1$.\n\\end{proof}\n\nThis specializes the general constraints of Gra"
      }
    ],
    "extent": "Original operative statement and surrounding hypotheses opened; no claim that the full external article was independently reproved."
  },
  {
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "citation_key": "Frolicher1955",
    "title": "Relations between the cohomology groups of Dolbeault and topological invariants",
    "url": "https://www.pnas.org/doi/pdf/10.1073/pnas.41.9.641",
    "status": "verified_for_stated_use",
    "verified": true,
    "opened_locator": "Original publisher PDF, pp.641–644 in full; Lemmas 1–2 and Theorem 3 on p.643.",
    "actual_use": "E1 equals Dolbeault cohomology and E-infinity is the associated graded complex de Rham cohomology.",
    "hypotheses_and_normalization_check": "The bounded filtration is by holomorphic degree of smooth forms on a complex manifold. The identification and finite stabilization do not require Kählerness. Compactness supplies the finite dimensions used here. The candidate-specific vanishing of higher differentials and exactness of the middle rows are proved in the appendix, not taken from this source.",
    "local_source": null,
    "source_sha256": null,
    "web_refs": [
      "turn168view0"
    ],
    "aliases": [],
    "citation_contexts": [
      {
        "file": "deliverables/work/invariants_arithmetic/working_hodge_frolicher_proofs.tex",
        "line": 146,
        "context": "ion of \\cref{inv:C1.1}.\n\n\n\\begin{proof}\nFr\\\"olicher's original construction identifies $E_1$ with Dolbeault\ncohomology and $E_\\infty$ with the associated graded de Rham cohomology\n\\cite[p.~643, Lemmas~1--2 and Theorem~3]{Frolicher1955}.  The table in\n\\cref{wb:thm:parametric-hodge-diamond} leaves only the displayed\n$q=1$ and $q=2$ row complexes between the endpoint classes.  Since\n$H^k_{\\mathrm{dR}}(X;\\mathbb C)=0$ for $1\\le k\\le5$, every middle\n$E_\\in"
      }
    ],
    "extent": "Original operative statement and surrounding hypotheses opened; no claim that the full external article was independently reproved."
  },
  {
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "citation_key": "Serre1955Duality",
    "title": "Un théorème de dualité",
    "url": "https://www.college-de-france.fr/media/jean-pierre-serre/UPL35645220559164287_Un_theoreme_de_dualite.pdf",
    "status": "verified_for_stated_use",
    "verified": true,
    "opened_locator": "§13, Theorem 4, published p.22; §15, cup product and integration, p.23.",
    "actual_use": "Dolbeault–Serre duality for the smooth compact threefold and its cup-product pairing.",
    "hypotheses_and_normalization_check": "The theorem pairs H^q(Omega^p(V)) with H^(n-q)(Omega^(n-p)(V dual)) for a holomorphic vector bundle on a compact complex n-fold. No Kähler assumption is required. Here n=3 and V is trivial. Singular and nonreduced fibres instead use RR70; this smooth theorem is not extended to them.",
    "local_source": "sources/audit_cache/inv_ari/working_literature/Serre1955Duality.pdf",
    "source_sha256": "48ccd4a6820ea5dc2783b7845909c2e816e919168c79fa2fedb6107ea8801d97",
    "web_refs": [
      "turn149view1"
    ],
    "aliases": [],
    "citation_contexts": [
      {
        "file": "deliverables/work/invariants_arithmetic/working_hodge_frolicher_proofs.tex",
        "line": 110,
        "context": "rent Leray on\n$\\mathbb P^1$ therefore gives\n\\[\n (h^{0,0},h^{0,1},h^{0,2},h^{0,3})=(1,1,0,0).\n\\]\nTogether with \\cref{wb:prop:workbench-holomorphic-form-vanishing} and Serre\nduality \\cite[\\S13, Theorem~4, p.~22]{Serre1955Duality}, this fixes every\nentry except the four middle entries, with\n$h^{1,2}=h^{2,1}=m$ and $h^{1,1}=h^{2,2}$.\n\nThe verified integral sphere topology gives $c_1(X)=c_2(X)=0$ and\n$\\int_Xc_3(X)=2$.  In complex dimension three,\n\\"
      }
    ],
    "extent": "Original operative statement and surrounding hypotheses opened; no claim that the full external article was independently reproved."
  },
  {
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "citation_key": "Grothendieck1957",
    "title": "Sur la classification des fibrés holomorphes sur la sphère de Riemann",
    "url": "https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/AG/AG-25.pdf",
    "status": "verified_for_stated_use",
    "verified": true,
    "opened_locator": "Theorem 2.1, published p.126 (PDF p.7), with the preceding holomorphic bundle convention.",
    "actual_use": "Splitting of the locally free direct images on the base P1.",
    "hypotheses_and_normalization_check": "The base is the Riemann sphere and the object is a holomorphic vector bundle. The theorem splits it into line bundles with degrees unique up to permutation. The appendix computes extension groups and degrees directly; it never infers projectivity of the total threefold from this classification.",
    "local_source": "sources/audit_cache/inv_ari/working_literature/Grothendieck1957.pdf",
    "source_sha256": "c6cbd9ab65c5e10f9b24bc245d3650986ae9e0535b2cc1a5b8ed892d090a5a18",
    "web_refs": [
      "turn150search7"
    ],
    "aliases": [],
    "citation_contexts": [
      {
        "file": "deliverables/work/invariants_arithmetic/working_hodge_frolicher_proofs.tex",
        "line": 433,
        "context": "\\mathcal O)$, or\n$H^1(\\mathcal O(1))$, all zero.  This proves the three asserted splittings.\nThis is also the elementary filtered form of the\nBirkhoff--Grothendieck classification\n\\cite[Theorem~2.1, p.~126]{Grothendieck1957}; the divisor modifications and\n$\\operatorname{Ext}^1$ identifications may equivalently be read in\n\\cite[Tags 0C6K, 0B3A, and 01XT]{StacksProject}.\n\nFinally, \\eqref{inv:wb:eq:11.3a}--\\eqref{inv:wb:eq:11.4} make every dir"
      }
    ],
    "extent": "Original operative statement and surrounding hypotheses opened; no claim that the full external article was independently reproved."
  },
  {
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "citation_key": "Deligne1970",
    "title": "Équations différentielles à points singuliers réguliers",
    "url": "https://publications.ias.edu/sites/default/files/Number9.pdf",
    "status": "verified_for_stated_use",
    "verified": true,
    "opened_locator": "Chapter II, §3.2 Proposition 3.2 and Lemma 3.2.1, pp.72–73; §3.3.1–3.3.2, pp.73–75; §3.4–3.7, pp.75–78, especially residue isomorphism 3.5.3 and Proposition 3.6.",
    "actual_use": "Locally free logarithmic differentials, the relative monomial conormal sequence, and residues on the normalized strata of a self-crossing divisor.",
    "hypotheses_and_normalization_check": "The analytic version explicitly allows a smooth total space and smooth one-dimensional base with local equation t=product z_i^e_i, positive e_i, and a normal-crossing boundary containing the central fibre. It gives the split local relative logarithmic sequence used here. Normalized strata and their orientation sheaves handle global self-crossing; the degree-one target is the structure sheaf of the normalization, not the unnormalized divisor.",
    "local_source": "sources/audit_cache/inv_ari/working_literature/Deligne1970.pdf",
    "source_sha256": "0dc37edd7758198cc4cd7ebed0dae63ff821336cebe739636a31591671593ba2",
    "web_refs": [],
    "aliases": [],
    "citation_contexts": [
      {
        "file": "deliverables/work/invariants_arithmetic/working_hodge_frolicher_proofs.tex",
        "line": 258,
        "context": "H.11.2}\\label{inv:wb:eq:11.2}\n\\]\nThe local $d\\log$ bases and their relative form, including\n$t=\\prod z_i^{e_i}$ and analytic base change, are the logarithmic conormal\nformalism of \\cite[Chapter~II, \\S3.2--3.3, pp.~72--75]{Deligne1970}; the\ndisplay above also follows directly from the stated local equations.\n\n\\subsubsection{the three logarithmic relative direct images}\\label{inv:wbproof:prop:log-relative-direct-images}\nThe following working-edition ar"
      },
      {
        "file": "deliverables/work/invariants_arithmetic/working_hodge_frolicher_proofs.tex",
        "line": 471,
        "context": "s a logarithmic analytic special-fibre theorem.  In the present family,\nDeligne's local monomial calculation supplies the locally split logarithmic\nsequence \\eqref{inv:wb:eq:11.2} \\cite[Chapter~II, \\S3.3]{Deligne1970}.  Taking a local\nsplitting and a \\v Cech representative, the connecting cochain is the\ndifference of the two splittings.  Since exterior product of cochains obeys\n\\[\n \\delta(\\alpha\\wedge\\beta)\n =\\delta\\alpha\\wedge\\beta+"
      },
      {
        "file": "deliverables/work/invariants_arithmetic/working_hodge_frolicher_proofs.tex",
        "line": 617,
        "context": "ormalization in the target is indispensable at the self-crossing\ncusp.  This is the degree-one residue sequence associated with the normalized\nstrata of a normal-crossings divisor\n\\cite[Chapter~II, \\S3.4--3.7, pp.~76--78]{Deligne1970}; the displayed local\ncalculation fixes its convention in the present self-crossing model.\n\n\\subsubsection{absolute cotangent direct images}\\label{inv:wbproof:prop:absolute-cotangent-direct-images}\nThe following working-"
      }
    ],
    "extent": "Original operative statement and surrounding hypotheses opened; no claim that the full external article was independently reproved."
  },
  {
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "citation_key": "KatzOda1968",
    "title": "On the differentiation of de Rham cohomology classes with respect to parameters",
    "url": "https://www.its.caltech.edu/~matilde/GaussManinKatzOda.pdf",
    "status": "verified_for_stated_use",
    "verified": true,
    "opened_locator": "§2, equations (5)–(10), published pp.202–204; §3, the Čech connecting description, pp.205–209.",
    "actual_use": "Credit for the smooth Gauss–Manin connecting construction and its exterior-product Leibniz rule.",
    "hypotheses_and_normalization_check": "Katz–Oda assume a smooth algebraic morphism of smooth schemes. The appendix explicitly limits this citation to that formalism. Its logarithmic analytic special-fibre statement is separately derived from Deligne’s local split sequence and the Čech difference of splittings; it does not apply the algebraic theorem to singular analytic fibres.",
    "local_source": "sources/audit_cache/inv_ari/working_literature/KatzOda1968.pdf",
    "source_sha256": "c6b78daf421a0597d88cf2cc0349201bdaabb343e2265933f31545b0ddf18527",
    "web_refs": [
      "turn153view1"
    ],
    "aliases": [],
    "citation_contexts": [
      {
        "file": "deliverables/work/invariants_arithmetic/working_hodge_frolicher_proofs.tex",
        "line": 467,
        "context": "rtion of \\cref{inv:A2.1}.\n\n\n\\begin{proof}\nOn the smooth locus, the connecting construction and its\nexterior-product Leibniz rule are the Gauss--Manin/Kodaira--Spencer\nformalism of\n\\cite[\\S2, equations~(5)--(10), pp.~202--204]{KatzOda1968}.\nKatz--Oda work with a smooth algebraic morphism; the citation is not being\nused as a logarithmic analytic special-fibre theorem.  In the present family,\nDeligne's local monomial calculation supplies the locally split l"
      }
    ],
    "extent": "Original operative statement and surrounding hypotheses opened; no claim that the full external article was independently reproved."
  },
  {
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "citation_key": "Schweitzer2007",
    "title": "Autour de la cohomologie de Bott–Chern",
    "url": "https://arxiv.org/pdf/0709.3528",
    "status": "verified_for_stated_use",
    "verified": true,
    "opened_locator": "§1.a, definitions and algebra; §2.c, Lemma 2.5 and the harmonic duality, pp.9–10; §8.a, pp.25–26, line-bundle transition, curvature and Chern normalization.",
    "actual_use": "Bott–Chern/Aeppli definitions and pairing, Hodge-star duality, and c1_BC(L)=[i F/(2 pi)].",
    "hypotheses_and_normalization_check": "Duality requires a compact complex manifold and a Hermitian metric, without Kählerness. The conjugate-linear star convention has target bidegree (n-p,n-q); the dimension identity agrees with the complex-linear convention after conjugation. The source distinguishes the ordinary Chern class i Theta/(2 pi) from its 2 pi i multiple; the appendix uses the ordinary class consistently.",
    "local_source": "sources/audit_cache/inv_ari/working_literature/Schweitzer2007.pdf",
    "source_sha256": "07ae9a20f069faa914535a9cdcbfd36681698430384eea873351d3f77dda0dc2",
    "web_refs": [],
    "aliases": [],
    "citation_contexts": [
      {
        "file": "deliverables/work/invariants_arithmetic/working_hodge_frolicher_proofs.tex",
        "line": 1148,
        "context": "able gives\n$h^{2,3}_{BC}=h^{3,2}_{BC}=1$, the two endpoint dimensions equal to one,\nand every other entry zero.  This proves \\cref{inv:C2.1}.  The Hodge-star duality\nof Schweitzer \\cite[\\S2.c, pp.~9--10]{Schweitzer2007},\n$h_A^{p,q}=h_{BC}^{3-p,3-q}$, proves \\cref{inv:C2.1}.  Summing along diagonals and\nusing $b_0=b_6=1$ and $b_k=0$ for $1\\le k\\le5$ proves\n\\cref{inv:C2.1,inv:C3.4}.\n\\end{proof}\n\nThe dimension calculation above is complet"
      },
      {
        "file": "deliverables/work/invariants_arithmetic/working_bott_chern_proofs.tex",
        "line": 9,
        "context": "ut and conventions}\n\nLet $f\\colon X\\to B=\\mathbb P^1$ be the compact complex threefold of\n\\cref{wb:thm:candidate-global-geometry}.  We use\n$d=\\partial+\\bar\\partial$ and, following\n\\cite[\\S1.a]{Schweitzer2007},\n\\begin{equation}\n H^{p,q}_{BC}(X)=\n \\frac{\\ker\\partial\\cap\\ker\\bar\\partial\n       \\subset\\mathcal A^{p,q}(X)}\n      {\\operatorname{im}(\\partial\\bar\\partial)}.\n\\label{wb:eq:bcpr-bc-definition}\n\\end{equation}\nThe natural"
      },
      {
        "file": "deliverables/work/invariants_arithmetic/working_bott_chern_proofs.tex",
        "line": 25,
        "context": "t-map}\n\\end{equation}\nExterior multiplication makes the direct sum of the Bott--Chern groups a\nbigraded algebra, and complex conjugation interchanges bidegrees $(p,q)$\nand $(q,p)$ \\cite[\\S1.a]{Schweitzer2007}.\n\nBy \\cref{wb:cor:exact-hodge-diamond}, the two nonzero rows of the\nFr\\\"olicher differential are the exact complexes\n\\begin{equation}\n 0\\longrightarrow H^{0,1}_{\\bar\\partial}(X)\n \\xrightarrow{d_1}H^{1,1}_{\\bar\\partial}("
      },
      {
        "file": "deliverables/work/invariants_arithmetic/working_bott_chern_proofs.tex",
        "line": 440,
        "context": "\\end{equation}\nWith the Bott--Chern convention\n\\begin{equation}\n c_{1,BC}(L,h)=\n \\left[\\frac{i}{2\\pi}F_{\\nabla^h}\\right]_{BC}\n\\label{wb:eq:bcpr-chern-convention}\n\\end{equation}\nof \\cite[\\S8.a]{Schweitzer2007},\n\\cref{wb:eq:bcpr-unit-chern-curvature} gives, for every $z\\in\\mathbb C$,\n\\begin{equation}\n c_{1,BC}\\bigl(\\exp(z\\mathfrak g)\\bigr)\n =z\\mathsf A+\\bar z\\,\\mathsf B.\n\\label{wb:eq:bcpr-chern-exp-identity}\n\\end{equation}\nCon"
      },
      {
        "file": "deliverables/work/invariants_arithmetic/working_bott_chern_proofs.tex",
        "line": 704,
        "context": "d{equation}\nThis step uses Dolbeault--Serre duality together with the independently\nproved injectivity of \\cref{wb:eq:bcpr-bc-to-dolbeault-32}.  The\nBott--Chern--Aeppli pairing of\n\\cite[\\S2.c]{Schweitzer2007} by itself would supply a perfect pairing but\nwould not annihilate this product.\n\nThe only products not yet considered which can have bidegree at most\n$(3,3)$ are\n\\begin{equation}\n \\mathsf A\\mathsf D,\\quad\n \\mathsf A\\ove"
      }
    ],
    "extent": "Original operative statement and surrounding hypotheses opened; no claim that the full external article was independently reproved."
  },
  {
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "citation_key": "Ugarte2000",
    "title": "Hodge numbers of a hypothetical complex structure on the six sphere",
    "url": "https://zaguan.unizar.es/record/165697/files/texto_completo.pdf?version=1",
    "status": "verified_for_stated_use",
    "verified": true,
    "opened_locator": "Lemma 2.1 and Proposition 3.1, pp.175–176; Theorem 3.2 and full proof, pp.176–177; Corollary 3.3 and Remark 3.4, p.177.",
    "actual_use": "Historical credit for constraints on Hodge numbers of a complex six-sphere, including second-page symmetry and inequalities.",
    "hypotheses_and_normalization_check": "Theorem 3.2 concerns an arbitrary complex structure on the topological six-sphere, not every compact complex threefold. It gives E3=E-infinity, E2 symmetries and h2^(0,1)=h^(1,2)-h^(1,1)+1. The stronger E2 degeneration here uses independently proved holomorphic-form vanishing and the candidate’s direct images; it is not attributed to Ugarte.",
    "local_source": "sources/audit_cache/inv_ari/working_literature/Ugarte2000.pdf",
    "source_sha256": "d68f5e112017c5e2d4b7f58f1873a9098e38c21c35e0307cf1f205d4326b578b",
    "web_refs": [],
    "aliases": [],
    "citation_contexts": [
      {
        "file": "deliverables/work/invariants_arithmetic/working_hodge_frolicher_proofs.tex",
        "line": 134,
        "context": "pecializes the general constraints of Gray and Ugarte; a convenient\npublished synthesis is Angella \\cite{Angella2018}, while the second-page\nsymmetry and inequalities originate in \\cite{Ugarte2000}.  The argument\nabove uses the stronger candidate-specific direct images and form\nvanishings, rather than assuming a general Hodge pattern for a hypothetical\ncomplex $S^6$.\n\n\\subsubsection{the complete Fr\\\"olicher page}\\"
      }
    ],
    "extent": "Original operative statement and surrounding hypotheses opened; no claim that the full external article was independently reproved."
  },
  {
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "citation_key": "Serre1973",
    "title": "A course in arithmetic",
    "url": "https://www.math.purdue.edu/~jlipman/MA598/Serre-Course%20in%20Arithmetic.pdf",
    "status": "verified_for_stated_use",
    "verified": true,
    "opened_locator": "Chapter VII, §3.1 Theorem 3, p.85; §3.2 Theorem 4 and proof, p.88; §3.3 equation (22) and Proposition 5, p.89; visually inspected PDF pp.94–100, printed pp.84–90.",
    "actual_use": "The modular invariant has ramification order two at tau=i, used to compute the scalar Kodaira–Spencer zero.",
    "hypotheses_and_normalization_check": "The valence formula and Theorem 4 proof give a simple zero of G3 at i and no zero of Delta on the upper half-plane. Since j=1728 g2^3/Delta and Delta=g2^3-27g3^2, j-1728=1728*27*g3^2/Delta has exactly a double zero at i. This is a derivation from the opened statements, with Serre’s G3 of weight six identified with the usual E6 up to a nonzero scalar.",
    "local_source": "sources/audit_cache/inv_ari/working_literature/Serre1973.pdf",
    "source_sha256": "15cea1a59aec4541efd5e9565d03624e5e6a3e896418e70b9934de27519a21ae",
    "web_refs": [
      "turn169view2"
    ],
    "aliases": [],
    "citation_contexts": [
      {
        "file": "deliverables/work/invariants_arithmetic/working_hodge_frolicher_proofs.tex",
        "line": 1012,
        "context": "bigr).\n\\tag{WBH.11.19a}\\label{inv:wb:eq:11.19a}\n\\]\n\nAt the order-four lift $z_2$, the quotient coordinate has order four while\nthe modular invariant has order two at $\\tau=i$; see\n\\cite[Chapter~VII]{Serre1973}.  Equivalently,\n$j(\\tau)-1728$ has a double zero at $i$ and\n$j(\\tau(z))-1728$ has order four at $z_2$.  Hence\n\\[\n \\operatorname{ord}_{z_2}(\\tau-i)=2,\\qquad \\dot\\tau(z_2)=0.\n\\tag{WBH.11.20}\\label{inv:wb:eq:11.20}\n\\]\nBy \\"
      }
    ],
    "extent": "Original operative statement and surrounding hypotheses opened; no claim that the full external article was independently reproved."
  },
  {
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "citation_key": "StacksProject",
    "title": "The Stacks Project",
    "url": "https://stacks.math.columbia.edu/",
    "status": "verified_for_stated_use",
    "verified": true,
    "opened_locator": "Tag 0C6K, Remark 31.15.11; Tag 0B3A, Lemma 20.5.1 and proof; Tag 01XT, Lemma 30.8.1 and its Čech proof.",
    "actual_use": "Cartier modification sequences, Ext^1(O,F)=H^1(F), and the line-bundle cohomology calculation on projective space.",
    "hypotheses_and_normalization_check": "The Ext statement is for ringed spaces. The Cartier exact sequences require a regular section; the elementary modifications here are on the smooth base. Tag 01XT is stated algebraically. The analytic P1 calculation in the appendix is also the same Laurent–Čech computation; no algebraic proper-base-change theorem is asserted for the analytic family.",
    "local_source": null,
    "source_sha256": null,
    "web_refs": [
      "turn152view0",
      "turn152view1",
      "turn152view2"
    ],
    "aliases": [],
    "citation_contexts": [
      {
        "file": "deliverables/work/invariants_arithmetic/working_hodge_frolicher_proofs.tex",
        "line": 435,
        "context": "irkhoff--Grothendieck classification\n\\cite[Theorem~2.1, p.~126]{Grothendieck1957}; the divisor modifications and\n$\\operatorname{Ext}^1$ identifications may equivalently be read in\n\\cite[Tags 0C6K, 0B3A, and 01XT]{StacksProject}.\n\nFinally, \\eqref{inv:wb:eq:11.3a}--\\eqref{inv:wb:eq:11.4} make every direct image free of ranks $2,4,2$ at\nthe finite points; \\eqref{inv:wb:eq:11.3} does the same at the cusp, and the smooth locus is\nstandard.  The mul"
      }
    ],
    "extent": "Original operative statement and surrounding hypotheses opened; no claim that the full external article was independently reproved."
  },
  {
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "citation_key": "AngellaTomassini2013",
    "title": "On the partial-partial-bar lemma and Bott–Chern cohomology",
    "url": "https://arxiv.org/pdf/1402.1954",
    "status": "verified_for_stated_use",
    "verified": true,
    "opened_locator": "Author version of Inventiones 192 (2013), pp.71–81; combined Theorems A–B in the introduction (PDF p.2) and §1, pp.2–3.",
    "actual_use": "Credit for the general non-Kählerness inequality and the dimension formulation; the numerical defect table here is calculated directly.",
    "hypotheses_and_normalization_check": "Compact complex manifolds are the sole geometric hypothesis. The inequality is sum over p+q=k of (hBC+hA) at least 2bk; equality for every k characterizes the partial-partial-bar lemma. No equality case is assumed for this threefold. The citation was in the source duplicate statement and should remain credited when its statement is merged.",
    "local_source": "sources/audit_cache/inv_ari/working_literature/AngellaTomassini2013.pdf",
    "source_sha256": "538ff89c724981d47b7f281d6839dfbb7a61da6105880ef723acd90b40f4931f",
    "web_refs": [
      "turn169view1"
    ],
    "aliases": [],
    "citation_contexts": [
      {
        "file": "sources/overleaf_working_edition/supporting_materials/workbench/hodge_frolicher.tex",
        "context": "Original duplicate Bott–Chern table statement: non-Kählerness degrees credited to Theorem A. Statement merged; provenance retained."
      }
    ],
    "extent": "Original operative statement and surrounding hypotheses opened; no claim that the full external article was independently reproved."
  },
  {
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "citation_key": "BS76",
    "title": "Algebraic methods in the global theory of complex spaces",
    "url": "https://djvu.online/file/2hQiOnz8WuoQk",
    "status": "verified_for_stated_use",
    "verified": true,
    "opened_locator": "Chapter III, §3 Theorem 3.4 and proof pp.116–120; Corollaries 3.5, 3.7 and 3.10 pp.120–122; §4 Theorem 4.12(i)–(iii) and proof pp.134–135.",
    "actual_use": "Analytic cohomology and base change, cohomological flatness, local freeness, and semicontinuity for full scheme fibres.",
    "hypotheses_and_normalization_check": "Properness, coherence and flatness of the coefficient sheaf are required. The constant-dimension converse in Theorem 4.12(ii) additionally requires a reduced base, satisfied by P1 and the discs here. The fibres themselves may be nonreduced. Corollary 3.10 identifies local freeness of all higher images with cohomological flatness in the bounded range.",
    "local_source": null,
    "source_sha256": null,
    "web_refs": [
      "turn157view1",
      "turn159view0",
      "turn159view1",
      "turn160view0",
      "turn160view1"
    ],
    "aliases": [
      "BanicaStanasila1976",
      "BS76push"
    ],
    "citation_contexts": [
      {
        "file": "deliverables/work/invariants_arithmetic/working_analytic_picard_proofs.tex",
        "line": 94,
        "context": "-sheaf-audit}.  Grauert's\ntheorem therefore gives local freeness of ranks \\(1,2,1\\) and base change\non a neighbourhood of \\(B^\\circ\\cup\\{p_0\\}\\); the precise analytic statement is\n\\cite[Chapter~III, \\S4, Theorem~4.12]{BS76}, originally due to\nGrauert \\cite{Grauert1960}.\n\nAt \\(p_j\\), use the finite cover \\(J'_j\\to N_j\\).  If\n\\(\\widetilde f:J'_j\\to\\Delta_j\\) is the smooth torus family and\n\\(\\pi(s)=s^{m_j}\\), exactness of finite-group invaria"
      },
      {
        "file": "deliverables/work/invariants_arithmetic/working_hodge_frolicher_proofs.tex",
        "line": 456,
        "context": "including for the nonreduced\nfinite fibres; precisely the same criterion, with citation, is recorded in\nthe proof of\n\\cref{wb:thm:structure-direct-images-audit}; see in particular\n\\cite[Chapter~III, \\S3, Theorem~3.4 and Corollary~3.10]{BS76}.\n\\end{proof}\n\n\\subsubsection{the logarithmic Kodaira--Spencer divisor}\\label{inv:wbproof:prop:log-ks-divisor}\nThe following working-edition argument proves the corresponding assertion of \\cref{inv:A2.1}.\n\n\n\\begin{proof}"
      }
    ],
    "extent": "Original operative statement and surrounding hypotheses opened; no claim that the full external article was independently reproved."
  },
  {
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "citation_key": "Cartan1954Quotient",
    "title": "Quotient d’une variété analytique par un groupe discret d’automorphismes",
    "url": "https://www.numdam.org/item/SHC_1953-1954__6__A12_0/",
    "status": "verified_for_stated_use",
    "verified": true,
    "opened_locator": "Exposé 12, §1, conditions (I)–(II), pp.1–2, and Theorem 1, p.2; original PDF first three pages including cover read locally.",
    "actual_use": "Analytic quotient structure in the finite free quotient charts.",
    "hypotheses_and_normalization_check": "The action has a Hausdorff quotient, finite stabilizers, and neighborhoods meeting only stabilizer translates. A finite group acting on the Hausdorff manifold here satisfies these conditions. The theorem gives a normal analytic space; smoothness of the free quotient is separately proved by disjoint local charts.",
    "local_source": "sources/external/maps_audit/cartan1954_quotient.pdf",
    "source_sha256": "38e9c37dfc803e71093d15a2e905c7f808c8cbc46ef5584a174bb307bdafde85",
    "web_refs": [],
    "aliases": [
      "Cartan1954"
    ],
    "citation_contexts": [
      {
        "file": "deliverables/work/invariants_arithmetic/working_hodge_frolicher_proofs.tex",
        "line": 284,
        "context": "ad C=\\mathbb C\\{s\\},\\qquad t=s^m,\n \\qquad (m,a)=(3,2)\\text{ or }(4,1).\n\\]\nCartan's analytic quotient theorem identifies local holomorphic functions on\nthe quotient with invariants \\cite[\\S1, Theorem~1, pp.~1--2]{Cartan1954Quotient}.\nThe action on the total space is free, so the quotient map is finite \\'etale;\nthe corresponding locally free sheaves and their equivariant structures\ndescend by finite \\'etale descent.  This sheaf statement is not bein"
      }
    ],
    "extent": "Original operative statement and surrounding hypotheses opened; no claim that the full external article was independently reproved."
  },
  {
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "citation_key": "Grauert1960",
    "title": "Ein Theorem der analytischen Garbentheorie und die Modulräume komplexer Strukturen",
    "url": "https://www.numdam.org/article/PMIHES_1960__5__5_0.pdf",
    "status": "verified_for_stated_use",
    "verified": true,
    "opened_locator": "§6 HauptsatzI, HauptsatzII and HauptsatzIIa p59; IIa formula and complete proof visually inspected on originalPDF page58; §7 Satz2 p61, read together with the1963 correction",
    "actual_use": "Proper direct-image coherence in the working structure-sheaf proof; base change uses the separately opened BS76 statements.",
    "hypotheses_and_normalization_check": "HauptsatzIIa is the analytic formal-functions isomorphism between the inverse limit of higher direct images of S/S.m_tilde^nu and the maximal-ideal completion of the stalk of R^i pi_* S. It requires a proper holomorphic map of complex spaces and coherent S, without projectivity or reducedness. Formula and full short proof were read in the original scan, rendered as reference_downloads/cdp_audit/Grauert1960_IIa.png. Its §7 Satz2 assertion about the failure locus must be read with the later correction. For closed analytic cohomology-jumping loci and base change this audit uses the separately opened BS76 finite-complex and flatness theorems.",
    "local_source": "reference_downloads/cdp_audit/Grauert1960.pdf",
    "source_sha256": "0559856be254902e7dd116725732117606912ab7d72b0f0fe88b600566829cde",
    "web_refs": [
      "turn50view2",
      "turn52view4"
    ],
    "aliases": [
      "Grauert60push",
      "Grauert1960D"
    ],
    "citation_contexts": [
      {
        "file": "deliverables/work/invariants_arithmetic/working_analytic_picard_proofs.tex",
        "line": 95,
        "context": "ks \\(1,2,1\\) and base change\non a neighbourhood of \\(B^\\circ\\cup\\{p_0\\}\\); the precise analytic statement is\n\\cite[Chapter~III, \\S4, Theorem~4.12]{BS76}, originally due to\nGrauert \\cite{Grauert1960}.\n\nAt \\(p_j\\), use the finite cover \\(J'_j\\to N_j\\).  If\n\\(\\widetilde f:J'_j\\to\\Delta_j\\) is the smooth torus family and\n\\(\\pi(s)=s^{m_j}\\), exactness of finite-group invariants in characteristic\nzero gives\n\\[\n R^qf_*\\ma"
      }
    ],
    "original_check_provenance": {
      "agent": "/root/cdp_audit",
      "record": "work/cdp_audit/references_verified.json",
      "citation_key": "Grauert1960",
      "recorded_checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), writing run; 17 November 2026 (Europe/Berlin)"
    },
    "extent": "Original-source reading is the recorded parallel writing-run check; this reader separately matched the WB application to those precise hypotheses."
  },
  {
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "citation_key": "RR70",
    "title": "Complexe dualisant et théorèmes de dualité en géométrie analytique complexe",
    "url": "https://www.numdam.org/article/PMIHES_1970__38__77_0.pdf",
    "status": "verified_for_stated_use",
    "verified": true,
    "opened_locator": "§3, Theorem1, published p.81; dualizing-complex amplitude on p.89; Proposition2 and complete-intersection calculation p.91",
    "actual_use": "Serre duality on the compact possibly nonreduced Gorenstein Cartier fibres.",
    "hypotheses_and_normalization_check": "Original journal PDF read locally. Countable-at-infinity bounded-dimensional analytic spaces are allowed. On compact fibres the coherent groups are finite-dimensional and separated; the Cartier Gorenstein dualizing complex is an invertible sheaf shifted by dimension. A locally free twist reduces Ext to cohomology of its dual tensor the dualizing line. No smoothness or reducedness is inserted.",
    "local_source": "reference_downloads/cdp_audit/RamisRuget1970.pdf",
    "source_sha256": "283dbde1ce597b2cdd7ae4110e3f0f991aeee23a6086568cc10e6e5e720c674b",
    "web_refs": [],
    "aliases": [
      "RR70push",
      "RamisRuget1970"
    ],
    "citation_contexts": [
      {
        "file": "deliverables/work/invariants_arithmetic/working_analytic_picard_proofs.tex",
        "line": 164,
        "context": "wb:eq:9.15}\n\\]\nThe relative theorem is the one of Ramis--Ruget--Verdier\n\\cite[pp.~261--283]{RRV71}; the absolute singular\ndualizing-complex comparison is independently recorded in\n\\cite[Theorems~1--2 and Proposition~2]{RR70}.\n\nThe relative cup product\n\\[\n \\bigwedge^2G\\longrightarrow R^2f_*\\mathcal O_X\n\\tag{WBA.9.16}\\label{inv:wb:eq:9.16}\n\\]\nis an isomorphism.  It is so on every smooth torus fibre.  At the cusp it\nis so by the base-change as"
      }
    ],
    "original_check_provenance": {
      "agent": "/root/cdp_audit",
      "record": "work/cdp_audit/references_verified.json",
      "citation_key": "RR70",
      "recorded_checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), writing run; 17 November 2026 (Europe/Berlin)"
    },
    "extent": "Original-source reading is the recorded parallel writing-run check; this reader separately matched the WB application to those precise hypotheses."
  },
  {
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "citation_key": "RRV71",
    "title": "Dualité relative en géométrie analytique complexe",
    "url": "https://gdz.sub.uni-goettingen.de/id/PPN356556735_0013",
    "status": "verified_for_stated_use",
    "verified": true,
    "opened_locator": "Introduction equation(1), original p.261; §1 proper-duality trace quasi-isomorphism p.264; §2 relative trace, pp.265–268; Proposition2.1 continuity statement p.266",
    "actual_use": "Relative analytic duality for the proper flat Gorenstein surface family over the smooth curve.",
    "hypotheses_and_normalization_check": "Opened the original journal scan through its public GDZ IIIF manifest and visually checked pp.261,264,265,266 after reading the text of §§1–2. The introduction explicitly asserts that equation(1) is an isomorphism for a proper morphism of complex analytic spaces; §1 writes the required Rf_*RHom(F,K_X•)→RHom(Rf_*F,K_Y•). No projectivity or Kähler hypothesis occurs. For E3.1 the smooth total space and base give absolute dualizing complexes ω_Y[3] and ω_U[1]; projection and cancellation give Rp_*ω_Y/U[2]≅RHom(Rp_*O_Y,O_U), and the independently checked locally free cohomology gives the degree−2 edge. Proposition2.1 is the continuity step for the trace construction, not a theorem numbered as the general duality result. The article’s remaining functional-analytic proofs in §§3–4 were not audited.",
    "local_source": null,
    "source_sha256": null,
    "web_refs": [
      "turn123view0",
      "turn125view0"
    ],
    "aliases": [
      "RRV71push",
      "RamisRugetVerdier1971"
    ],
    "citation_contexts": [
      {
        "file": "deliverables/work/invariants_arithmetic/working_analytic_picard_proofs.tex",
        "line": 162,
        "context": "t}, it gives\n\\[\n R^2f_*\\mathcal O_X\\simeq\\mathfrak K^\\vee\n \\simeq\\mathcal O_B(-1).\n\\tag{WBA.9.15}\\label{inv:wb:eq:9.15}\n\\]\nThe relative theorem is the one of Ramis--Ruget--Verdier\n\\cite[pp.~261--283]{RRV71}; the absolute singular\ndualizing-complex comparison is independently recorded in\n\\cite[Theorems~1--2 and Proposition~2]{RR70}.\n\nThe relative cup product\n\\[\n \\bigwedge^2G\\longrightarrow R^2f_*\\mathcal O_X\n\\tag{WBA.9.16}\\"
      }
    ],
    "original_check_provenance": {
      "agent": "/root/cdp_audit",
      "record": "work/cdp_audit/references_verified.json",
      "citation_key": "RRV71",
      "recorded_checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), writing run; 17 November 2026 (Europe/Berlin)"
    },
    "extent": "Original-source reading is the recorded parallel writing-run check; this reader separately matched the WB application to those precise hypotheses.",
    "original_page_files": [
      {
        "page": "261",
        "url": "https://images.p.sub.uni-goettingen.de/iiif/image/gdz:PPN356556735_0013:00000275/full/1800,/0/default.jpg",
        "path": "reference_downloads/cdp_audit/RRV71_p261.jpg",
        "sha256": "6986f780a581fd6efc07462a77c50c67fb0422fd2e836a81922fd738fb12ca81",
        "bytes": 830095
      },
      {
        "page": "262",
        "url": "https://images.p.sub.uni-goettingen.de/iiif/image/gdz:PPN356556735_0013:00000276/full/1800,/0/default.jpg",
        "path": "reference_downloads/cdp_audit/RRV71_p262.jpg",
        "sha256": "c82972927ab912874716d4ea8bcd7809adfd3ee9a00f76155cbc1fd6288f687a",
        "bytes": 836349
      },
      {
        "page": "263",
        "url": "https://images.p.sub.uni-goettingen.de/iiif/image/gdz:PPN356556735_0013:00000277/full/1800,/0/default.jpg",
        "path": "reference_downloads/cdp_audit/RRV71_p263.jpg",
        "sha256": "591e6ac8c06854c9e18ee56289912dafbf98df87dcac36439702c546ce103e7c",
        "bytes": 890538
      },
      {
        "page": "264",
        "url": "https://images.p.sub.uni-goettingen.de/iiif/image/gdz:PPN356556735_0013:00000278/full/1800,/0/default.jpg",
        "path": "reference_downloads/cdp_audit/RRV71_p264.jpg",
        "sha256": "fc94bb88f92e0dd20afa7e4a5751c0d10682adff81000758eb846dc786c4eb19",
        "bytes": 733095
      },
      {
        "page": "265",
        "url": "https://images.p.sub.uni-goettingen.de/iiif/image/gdz:PPN356556735_0013:00000279/full/1800,/0/default.jpg",
        "path": "reference_downloads/cdp_audit/RRV71_p265.jpg",
        "sha256": "a6b7d205128fa94a9c64493199fa8f9a6f033ba94d9f37833d50ed2c2b9e97f3",
        "bytes": 837271
      },
      {
        "page": "266",
        "url": "https://images.p.sub.uni-goettingen.de/iiif/image/gdz:PPN356556735_0013:00000280/full/1800,/0/default.jpg",
        "path": "reference_downloads/cdp_audit/RRV71_p266.jpg",
        "sha256": "1319c20a09ddf5b7232fc0bf5598ab2c432c49d011cd3406b8cec1c744e2266a",
        "bytes": 728476
      },
      {
        "page": "267",
        "url": "https://images.p.sub.uni-goettingen.de/iiif/image/gdz:PPN356556735_0013:00000281/full/1800,/0/default.jpg",
        "path": "reference_downloads/cdp_audit/RRV71_p267.jpg",
        "sha256": "46abb6ca6005298239af3c3e63e7541351c3c000979daa513456704ffdb8a0b9",
        "bytes": 826516
      },
      {
        "page": "268",
        "url": "https://images.p.sub.uni-goettingen.de/iiif/image/gdz:PPN356556735_0013:00000282/full/1800,/0/default.jpg",
        "path": "reference_downloads/cdp_audit/RRV71_p268.jpg",
        "sha256": "0d293523c4f2924e6c0eb770dbda585add939be6839cba41ae4c959350449700",
        "bytes": 708212
      }
    ]
  }
]
```

### work/invariants_arithmetic/working_references_verified.json

```json
[
  {
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "citation_key": "AtiyahSinger1963",
    "title": "The index of elliptic operators on compact manifolds",
    "url": "https://scispace.com/pdf/the-index-of-elliptic-operators-on-compact-manifolds-3n33719pz0.pdf",
    "status": "verified_for_stated_use",
    "verified": true,
    "opened_locator": "Original journal scan, §3.2 and Theorem 3, published p.427 (PDF p.6); preceding definition of the index, pp.422–425.",
    "actual_use": "Hirzebruch–Riemann–Roch for the holomorphic cotangent bundle in the parameterized Hodge calculation.",
    "hypotheses_and_normalization_check": "The theorem explicitly allows every compact complex manifold and every holomorphic vector bundle. Hermitian metrics define the elliptic Dolbeault operator; no Kähler or projectivity hypothesis occurs. Its Todd class is that of the complex tangent bundle. The appendix independently expands ch(Omega^1) and Td, using c1=c2=0 and integral c3=2.",
    "local_source": null,
    "source_sha256": null,
    "web_refs": [
      "turn168view1",
      "turn169view0"
    ],
    "aliases": [],
    "citation_contexts": [
      {
        "file": "deliverables/work/invariants_arithmetic/working_hodge_frolicher_proofs.tex",
        "line": 124,
        "context": "1c_2,\\\\\n \\operatorname{ch}(\\Omega_X^1)\n &=3-c_1+\\frac12(c_1^2-2c_2)\n   -\\frac16(c_1^3-3c_1c_2+3c_3).\n\\end{align*}\nHirzebruch--Riemann--Roch for arbitrary compact complex manifolds\n\\cite[Theorem~3, p.~427]{AtiyahSinger1963} hence gives\n\\[\n \\chi(\\Omega_X^1)=-\\frac12\\int_Xc_3=-1.\n\\]\nThe already known zero entries reduce this identity to\n$-h^{1,1}+h^{1,2}=-1$, proving $h^{1,1}=m+1$.\n\\end{proof}\n\nThis specializes the general constraints of Gra"
      }
    ],
    "extent": "Original operative statement and surrounding hypotheses opened; no claim that the full external article was independently reproved."
  },
  {
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "citation_key": "Frolicher1955",
    "title": "Relations between the cohomology groups of Dolbeault and topological invariants",
    "url": "https://www.pnas.org/doi/pdf/10.1073/pnas.41.9.641",
    "status": "verified_for_stated_use",
    "verified": true,
    "opened_locator": "Original publisher PDF, pp.641–644 in full; Lemmas 1–2 and Theorem 3 on p.643.",
    "actual_use": "E1 equals Dolbeault cohomology and E-infinity is the associated graded complex de Rham cohomology.",
    "hypotheses_and_normalization_check": "The bounded filtration is by holomorphic degree of smooth forms on a complex manifold. The identification and finite stabilization do not require Kählerness. Compactness supplies the finite dimensions used here. The candidate-specific vanishing of higher differentials and exactness of the middle rows are proved in the appendix, not taken from this source.",
    "local_source": null,
    "source_sha256": null,
    "web_refs": [
      "turn168view0"
    ],
    "aliases": [],
    "citation_contexts": [
      {
        "file": "deliverables/work/invariants_arithmetic/working_hodge_frolicher_proofs.tex",
        "line": 146,
        "context": "ion of \\cref{inv:C1.1}.\n\n\n\\begin{proof}\nFr\\\"olicher's original construction identifies $E_1$ with Dolbeault\ncohomology and $E_\\infty$ with the associated graded de Rham cohomology\n\\cite[p.~643, Lemmas~1--2 and Theorem~3]{Frolicher1955}.  The table in\n\\cref{wb:thm:parametric-hodge-diamond} leaves only the displayed\n$q=1$ and $q=2$ row complexes between the endpoint classes.  Since\n$H^k_{\\mathrm{dR}}(X;\\mathbb C)=0$ for $1\\le k\\le5$, every middle\n$E_\\in"
      }
    ],
    "extent": "Original operative statement and surrounding hypotheses opened; no claim that the full external article was independently reproved."
  },
  {
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "citation_key": "Serre1955Duality",
    "title": "Un théorème de dualité",
    "url": "https://www.college-de-france.fr/media/jean-pierre-serre/UPL35645220559164287_Un_theoreme_de_dualite.pdf",
    "status": "verified_for_stated_use",
    "verified": true,
    "opened_locator": "§13, Theorem 4, published p.22; §15, cup product and integration, p.23.",
    "actual_use": "Dolbeault–Serre duality for the smooth compact threefold and its cup-product pairing.",
    "hypotheses_and_normalization_check": "The theorem pairs H^q(Omega^p(V)) with H^(n-q)(Omega^(n-p)(V dual)) for a holomorphic vector bundle on a compact complex n-fold. No Kähler assumption is required. Here n=3 and V is trivial. Singular and nonreduced fibres instead use RR70; this smooth theorem is not extended to them.",
    "local_source": "sources/audit_cache/inv_ari/working_literature/Serre1955Duality.pdf",
    "source_sha256": "48ccd4a6820ea5dc2783b7845909c2e816e919168c79fa2fedb6107ea8801d97",
    "web_refs": [
      "turn149view1"
    ],
    "aliases": [],
    "citation_contexts": [
      {
        "file": "deliverables/work/invariants_arithmetic/working_hodge_frolicher_proofs.tex",
        "line": 110,
        "context": "rent Leray on\n$\\mathbb P^1$ therefore gives\n\\[\n (h^{0,0},h^{0,1},h^{0,2},h^{0,3})=(1,1,0,0).\n\\]\nTogether with \\cref{wb:prop:workbench-holomorphic-form-vanishing} and Serre\nduality \\cite[\\S13, Theorem~4, p.~22]{Serre1955Duality}, this fixes every\nentry except the four middle entries, with\n$h^{1,2}=h^{2,1}=m$ and $h^{1,1}=h^{2,2}$.\n\nThe verified integral sphere topology gives $c_1(X)=c_2(X)=0$ and\n$\\int_Xc_3(X)=2$.  In complex dimension three,\n\\"
      }
    ],
    "extent": "Original operative statement and surrounding hypotheses opened; no claim that the full external article was independently reproved."
  },
  {
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "citation_key": "Grothendieck1957",
    "title": "Sur la classification des fibrés holomorphes sur la sphère de Riemann",
    "url": "https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/AG/AG-25.pdf",
    "status": "verified_for_stated_use",
    "verified": true,
    "opened_locator": "Theorem 2.1, published p.126 (PDF p.7), with the preceding holomorphic bundle convention.",
    "actual_use": "Splitting of the locally free direct images on the base P1.",
    "hypotheses_and_normalization_check": "The base is the Riemann sphere and the object is a holomorphic vector bundle. The theorem splits it into line bundles with degrees unique up to permutation. The appendix computes extension groups and degrees directly; it never infers projectivity of the total threefold from this classification.",
    "local_source": "sources/audit_cache/inv_ari/working_literature/Grothendieck1957.pdf",
    "source_sha256": "c6cbd9ab65c5e10f9b24bc245d3650986ae9e0535b2cc1a5b8ed892d090a5a18",
    "web_refs": [
      "turn150search7"
    ],
    "aliases": [],
    "citation_contexts": [
      {
        "file": "deliverables/work/invariants_arithmetic/working_hodge_frolicher_proofs.tex",
        "line": 433,
        "context": "\\mathcal O)$, or\n$H^1(\\mathcal O(1))$, all zero.  This proves the three asserted splittings.\nThis is also the elementary filtered form of the\nBirkhoff--Grothendieck classification\n\\cite[Theorem~2.1, p.~126]{Grothendieck1957}; the divisor modifications and\n$\\operatorname{Ext}^1$ identifications may equivalently be read in\n\\cite[Tags 0C6K, 0B3A, and 01XT]{StacksProject}.\n\nFinally, \\eqref{inv:wb:eq:11.3a}--\\eqref{inv:wb:eq:11.4} make every dir"
      }
    ],
    "extent": "Original operative statement and surrounding hypotheses opened; no claim that the full external article was independently reproved."
  },
  {
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "citation_key": "Deligne1970",
    "title": "Équations différentielles à points singuliers réguliers",
    "url": "https://publications.ias.edu/sites/default/files/Number9.pdf",
    "status": "verified_for_stated_use",
    "verified": true,
    "opened_locator": "Chapter II, §3.2 Proposition 3.2 and Lemma 3.2.1, pp.72–73; §3.3.1–3.3.2, pp.73–75; §3.4–3.7, pp.75–78, especially residue isomorphism 3.5.3 and Proposition 3.6.",
    "actual_use": "Locally free logarithmic differentials, the relative monomial conormal sequence, and residues on the normalized strata of a self-crossing divisor.",
    "hypotheses_and_normalization_check": "The analytic version explicitly allows a smooth total space and smooth one-dimensional base with local equation t=product z_i^e_i, positive e_i, and a normal-crossing boundary containing the central fibre. It gives the split local relative logarithmic sequence used here. Normalized strata and their orientation sheaves handle global self-crossing; the degree-one target is the structure sheaf of the normalization, not the unnormalized divisor.",
    "local_source": "sources/audit_cache/inv_ari/working_literature/Deligne1970.pdf",
    "source_sha256": "0dc37edd7758198cc4cd7ebed0dae63ff821336cebe739636a31591671593ba2",
    "web_refs": [],
    "aliases": [],
    "citation_contexts": [
      {
        "file": "deliverables/work/invariants_arithmetic/working_hodge_frolicher_proofs.tex",
        "line": 258,
        "context": "H.11.2}\\label{inv:wb:eq:11.2}\n\\]\nThe local $d\\log$ bases and their relative form, including\n$t=\\prod z_i^{e_i}$ and analytic base change, are the logarithmic conormal\nformalism of \\cite[Chapter~II, \\S3.2--3.3, pp.~72--75]{Deligne1970}; the\ndisplay above also follows directly from the stated local equations.\n\n\\subsubsection{the three logarithmic relative direct images}\\label{inv:wbproof:prop:log-relative-direct-images}\nThe following working-edition ar"
      },
      {
        "file": "deliverables/work/invariants_arithmetic/working_hodge_frolicher_proofs.tex",
        "line": 471,
        "context": "s a logarithmic analytic special-fibre theorem.  In the present family,\nDeligne's local monomial calculation supplies the locally split logarithmic\nsequence \\eqref{inv:wb:eq:11.2} \\cite[Chapter~II, \\S3.3]{Deligne1970}.  Taking a local\nsplitting and a \\v Cech representative, the connecting cochain is the\ndifference of the two splittings.  Since exterior product of cochains obeys\n\\[\n \\delta(\\alpha\\wedge\\beta)\n =\\delta\\alpha\\wedge\\beta+"
      },
      {
        "file": "deliverables/work/invariants_arithmetic/working_hodge_frolicher_proofs.tex",
        "line": 617,
        "context": "ormalization in the target is indispensable at the self-crossing\ncusp.  This is the degree-one residue sequence associated with the normalized\nstrata of a normal-crossings divisor\n\\cite[Chapter~II, \\S3.4--3.7, pp.~76--78]{Deligne1970}; the displayed local\ncalculation fixes its convention in the present self-crossing model.\n\n\\subsubsection{absolute cotangent direct images}\\label{inv:wbproof:prop:absolute-cotangent-direct-images}\nThe following working-"
      }
    ],
    "extent": "Original operative statement and surrounding hypotheses opened; no claim that the full external article was independently reproved."
  },
  {
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "citation_key": "KatzOda1968",
    "title": "On the differentiation of de Rham cohomology classes with respect to parameters",
    "url": "https://www.its.caltech.edu/~matilde/GaussManinKatzOda.pdf",
    "status": "verified_for_stated_use",
    "verified": true,
    "opened_locator": "§2, equations (5)–(10), published pp.202–204; §3, the Čech connecting description, pp.205–209.",
    "actual_use": "Credit for the smooth Gauss–Manin connecting construction and its exterior-product Leibniz rule.",
    "hypotheses_and_normalization_check": "Katz–Oda assume a smooth algebraic morphism of smooth schemes. The appendix explicitly limits this citation to that formalism. Its logarithmic analytic special-fibre statement is separately derived from Deligne’s local split sequence and the Čech difference of splittings; it does not apply the algebraic theorem to singular analytic fibres.",
    "local_source": "sources/audit_cache/inv_ari/working_literature/KatzOda1968.pdf",
    "source_sha256": "c6b78daf421a0597d88cf2cc0349201bdaabb343e2265933f31545b0ddf18527",
    "web_refs": [
      "turn153view1"
    ],
    "aliases": [],
    "citation_contexts": [
      {
        "file": "deliverables/work/invariants_arithmetic/working_hodge_frolicher_proofs.tex",
        "line": 467,
        "context": "rtion of \\cref{inv:A2.1}.\n\n\n\\begin{proof}\nOn the smooth locus, the connecting construction and its\nexterior-product Leibniz rule are the Gauss--Manin/Kodaira--Spencer\nformalism of\n\\cite[\\S2, equations~(5)--(10), pp.~202--204]{KatzOda1968}.\nKatz--Oda work with a smooth algebraic morphism; the citation is not being\nused as a logarithmic analytic special-fibre theorem.  In the present family,\nDeligne's local monomial calculation supplies the locally split l"
      }
    ],
    "extent": "Original operative statement and surrounding hypotheses opened; no claim that the full external article was independently reproved."
  },
  {
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "citation_key": "Schweitzer2007",
    "title": "Autour de la cohomologie de Bott–Chern",
    "url": "https://arxiv.org/pdf/0709.3528",
    "status": "verified_for_stated_use",
    "verified": true,
    "opened_locator": "§1.a, definitions and algebra; §2.c, Lemma 2.5 and the harmonic duality, pp.9–10; §8.a, pp.25–26, line-bundle transition, curvature and Chern normalization.",
    "actual_use": "Bott–Chern/Aeppli definitions and pairing, Hodge-star duality, and c1_BC(L)=[i F/(2 pi)].",
    "hypotheses_and_normalization_check": "Duality requires a compact complex manifold and a Hermitian metric, without Kählerness. The conjugate-linear star convention has target bidegree (n-p,n-q); the dimension identity agrees with the complex-linear convention after conjugation. The source distinguishes the ordinary Chern class i Theta/(2 pi) from its 2 pi i multiple; the appendix uses the ordinary class consistently.",
    "local_source": "sources/audit_cache/inv_ari/working_literature/Schweitzer2007.pdf",
    "source_sha256": "07ae9a20f069faa914535a9cdcbfd36681698430384eea873351d3f77dda0dc2",
    "web_refs": [],
    "aliases": [],
    "citation_contexts": [
      {
        "file": "deliverables/work/invariants_arithmetic/working_hodge_frolicher_proofs.tex",
        "line": 1148,
        "context": "able gives\n$h^{2,3}_{BC}=h^{3,2}_{BC}=1$, the two endpoint dimensions equal to one,\nand every other entry zero.  This proves \\cref{inv:C2.1}.  The Hodge-star duality\nof Schweitzer \\cite[\\S2.c, pp.~9--10]{Schweitzer2007},\n$h_A^{p,q}=h_{BC}^{3-p,3-q}$, proves \\cref{inv:C2.1}.  Summing along diagonals and\nusing $b_0=b_6=1$ and $b_k=0$ for $1\\le k\\le5$ proves\n\\cref{inv:C2.1,inv:C3.4}.\n\\end{proof}\n\nThe dimension calculation above is complet"
      },
      {
        "file": "deliverables/work/invariants_arithmetic/working_bott_chern_proofs.tex",
        "line": 9,
        "context": "ut and conventions}\n\nLet $f\\colon X\\to B=\\mathbb P^1$ be the compact complex threefold of\n\\cref{wb:thm:candidate-global-geometry}.  We use\n$d=\\partial+\\bar\\partial$ and, following\n\\cite[\\S1.a]{Schweitzer2007},\n\\begin{equation}\n H^{p,q}_{BC}(X)=\n \\frac{\\ker\\partial\\cap\\ker\\bar\\partial\n       \\subset\\mathcal A^{p,q}(X)}\n      {\\operatorname{im}(\\partial\\bar\\partial)}.\n\\label{wb:eq:bcpr-bc-definition}\n\\end{equation}\nThe natural"
      },
      {
        "file": "deliverables/work/invariants_arithmetic/working_bott_chern_proofs.tex",
        "line": 25,
        "context": "t-map}\n\\end{equation}\nExterior multiplication makes the direct sum of the Bott--Chern groups a\nbigraded algebra, and complex conjugation interchanges bidegrees $(p,q)$\nand $(q,p)$ \\cite[\\S1.a]{Schweitzer2007}.\n\nBy \\cref{wb:cor:exact-hodge-diamond}, the two nonzero rows of the\nFr\\\"olicher differential are the exact complexes\n\\begin{equation}\n 0\\longrightarrow H^{0,1}_{\\bar\\partial}(X)\n \\xrightarrow{d_1}H^{1,1}_{\\bar\\partial}("
      },
      {
        "file": "deliverables/work/invariants_arithmetic/working_bott_chern_proofs.tex",
        "line": 440,
        "context": "\\end{equation}\nWith the Bott--Chern convention\n\\begin{equation}\n c_{1,BC}(L,h)=\n \\left[\\frac{i}{2\\pi}F_{\\nabla^h}\\right]_{BC}\n\\label{wb:eq:bcpr-chern-convention}\n\\end{equation}\nof \\cite[\\S8.a]{Schweitzer2007},\n\\cref{wb:eq:bcpr-unit-chern-curvature} gives, for every $z\\in\\mathbb C$,\n\\begin{equation}\n c_{1,BC}\\bigl(\\exp(z\\mathfrak g)\\bigr)\n =z\\mathsf A+\\bar z\\,\\mathsf B.\n\\label{wb:eq:bcpr-chern-exp-identity}\n\\end{equation}\nCon"
      },
      {
        "file": "deliverables/work/invariants_arithmetic/working_bott_chern_proofs.tex",
        "line": 704,
        "context": "d{equation}\nThis step uses Dolbeault--Serre duality together with the independently\nproved injectivity of \\cref{wb:eq:bcpr-bc-to-dolbeault-32}.  The\nBott--Chern--Aeppli pairing of\n\\cite[\\S2.c]{Schweitzer2007} by itself would supply a perfect pairing but\nwould not annihilate this product.\n\nThe only products not yet considered which can have bidegree at most\n$(3,3)$ are\n\\begin{equation}\n \\mathsf A\\mathsf D,\\quad\n \\mathsf A\\ove"
      }
    ],
    "extent": "Original operative statement and surrounding hypotheses opened; no claim that the full external article was independently reproved."
  },
  {
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "citation_key": "Ugarte2000",
    "title": "Hodge numbers of a hypothetical complex structure on the six sphere",
    "url": "https://zaguan.unizar.es/record/165697/files/texto_completo.pdf?version=1",
    "status": "verified_for_stated_use",
    "verified": true,
    "opened_locator": "Lemma 2.1 and Proposition 3.1, pp.175–176; Theorem 3.2 and full proof, pp.176–177; Corollary 3.3 and Remark 3.4, p.177.",
    "actual_use": "Historical credit for constraints on Hodge numbers of a complex six-sphere, including second-page symmetry and inequalities.",
    "hypotheses_and_normalization_check": "Theorem 3.2 concerns an arbitrary complex structure on the topological six-sphere, not every compact complex threefold. It gives E3=E-infinity, E2 symmetries and h2^(0,1)=h^(1,2)-h^(1,1)+1. The stronger E2 degeneration here uses independently proved holomorphic-form vanishing and the candidate’s direct images; it is not attributed to Ugarte.",
    "local_source": "sources/audit_cache/inv_ari/working_literature/Ugarte2000.pdf",
    "source_sha256": "d68f5e112017c5e2d4b7f58f1873a9098e38c21c35e0307cf1f205d4326b578b",
    "web_refs": [],
    "aliases": [],
    "citation_contexts": [
      {
        "file": "deliverables/work/invariants_arithmetic/working_hodge_frolicher_proofs.tex",
        "line": 134,
        "context": "pecializes the general constraints of Gray and Ugarte; a convenient\npublished synthesis is Angella \\cite{Angella2018}, while the second-page\nsymmetry and inequalities originate in \\cite{Ugarte2000}.  The argument\nabove uses the stronger candidate-specific direct images and form\nvanishings, rather than assuming a general Hodge pattern for a hypothetical\ncomplex $S^6$.\n\n\\subsubsection{the complete Fr\\\"olicher page}\\"
      }
    ],
    "extent": "Original operative statement and surrounding hypotheses opened; no claim that the full external article was independently reproved."
  },
  {
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "citation_key": "Serre1973",
    "title": "A course in arithmetic",
    "url": "https://www.math.purdue.edu/~jlipman/MA598/Serre-Course%20in%20Arithmetic.pdf",
    "status": "verified_for_stated_use",
    "verified": true,
    "opened_locator": "Chapter VII, §3.1 Theorem 3, p.85; §3.2 Theorem 4 and proof, p.88; §3.3 equation (22) and Proposition 5, p.89; visually inspected PDF pp.94–100, printed pp.84–90.",
    "actual_use": "The modular invariant has ramification order two at tau=i, used to compute the scalar Kodaira–Spencer zero.",
    "hypotheses_and_normalization_check": "The valence formula and Theorem 4 proof give a simple zero of G3 at i and no zero of Delta on the upper half-plane. Since j=1728 g2^3/Delta and Delta=g2^3-27g3^2, j-1728=1728*27*g3^2/Delta has exactly a double zero at i. This is a derivation from the opened statements, with Serre’s G3 of weight six identified with the usual E6 up to a nonzero scalar.",
    "local_source": "sources/audit_cache/inv_ari/working_literature/Serre1973.pdf",
    "source_sha256": "15cea1a59aec4541efd5e9565d03624e5e6a3e896418e70b9934de27519a21ae",
    "web_refs": [
      "turn169view2"
    ],
    "aliases": [],
    "citation_contexts": [
      {
        "file": "deliverables/work/invariants_arithmetic/working_hodge_frolicher_proofs.tex",
        "line": 1012,
        "context": "bigr).\n\\tag{WBH.11.19a}\\label{inv:wb:eq:11.19a}\n\\]\n\nAt the order-four lift $z_2$, the quotient coordinate has order four while\nthe modular invariant has order two at $\\tau=i$; see\n\\cite[Chapter~VII]{Serre1973}.  Equivalently,\n$j(\\tau)-1728$ has a double zero at $i$ and\n$j(\\tau(z))-1728$ has order four at $z_2$.  Hence\n\\[\n \\operatorname{ord}_{z_2}(\\tau-i)=2,\\qquad \\dot\\tau(z_2)=0.\n\\tag{WBH.11.20}\\label{inv:wb:eq:11.20}\n\\]\nBy \\"
      }
    ],
    "extent": "Original operative statement and surrounding hypotheses opened; no claim that the full external article was independently reproved."
  },
  {
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "citation_key": "StacksProject",
    "title": "The Stacks Project",
    "url": "https://stacks.math.columbia.edu/",
    "status": "verified_for_stated_use",
    "verified": true,
    "opened_locator": "Tag 0C6K, Remark 31.15.11; Tag 0B3A, Lemma 20.5.1 and proof; Tag 01XT, Lemma 30.8.1 and its Čech proof.",
    "actual_use": "Cartier modification sequences, Ext^1(O,F)=H^1(F), and the line-bundle cohomology calculation on projective space.",
    "hypotheses_and_normalization_check": "The Ext statement is for ringed spaces. The Cartier exact sequences require a regular section; the elementary modifications here are on the smooth base. Tag 01XT is stated algebraically. The analytic P1 calculation in the appendix is also the same Laurent–Čech computation; no algebraic proper-base-change theorem is asserted for the analytic family.",
    "local_source": null,
    "source_sha256": null,
    "web_refs": [
      "turn152view0",
      "turn152view1",
      "turn152view2"
    ],
    "aliases": [],
    "citation_contexts": [
      {
        "file": "deliverables/work/invariants_arithmetic/working_hodge_frolicher_proofs.tex",
        "line": 435,
        "context": "irkhoff--Grothendieck classification\n\\cite[Theorem~2.1, p.~126]{Grothendieck1957}; the divisor modifications and\n$\\operatorname{Ext}^1$ identifications may equivalently be read in\n\\cite[Tags 0C6K, 0B3A, and 01XT]{StacksProject}.\n\nFinally, \\eqref{inv:wb:eq:11.3a}--\\eqref{inv:wb:eq:11.4} make every direct image free of ranks $2,4,2$ at\nthe finite points; \\eqref{inv:wb:eq:11.3} does the same at the cusp, and the smooth locus is\nstandard.  The mul"
      }
    ],
    "extent": "Original operative statement and surrounding hypotheses opened; no claim that the full external article was independently reproved."
  },
  {
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "citation_key": "AngellaTomassini2013",
    "title": "On the partial-partial-bar lemma and Bott–Chern cohomology",
    "url": "https://arxiv.org/pdf/1402.1954",
    "status": "verified_for_stated_use",
    "verified": true,
    "opened_locator": "Author version of Inventiones 192 (2013), pp.71–81; combined Theorems A–B in the introduction (PDF p.2) and §1, pp.2–3.",
    "actual_use": "Credit for the general non-Kählerness inequality and the dimension formulation; the numerical defect table here is calculated directly.",
    "hypotheses_and_normalization_check": "Compact complex manifolds are the sole geometric hypothesis. The inequality is sum over p+q=k of (hBC+hA) at least 2bk; equality for every k characterizes the partial-partial-bar lemma. No equality case is assumed for this threefold. The citation was in the source duplicate statement and should remain credited when its statement is merged.",
    "local_source": "sources/audit_cache/inv_ari/working_literature/AngellaTomassini2013.pdf",
    "source_sha256": "538ff89c724981d47b7f281d6839dfbb7a61da6105880ef723acd90b40f4931f",
    "web_refs": [
      "turn169view1"
    ],
    "aliases": [],
    "citation_contexts": [
      {
        "file": "sources/overleaf_working_edition/supporting_materials/workbench/hodge_frolicher.tex",
        "context": "Original duplicate Bott–Chern table statement: non-Kählerness degrees credited to Theorem A. Statement merged; provenance retained."
      }
    ],
    "extent": "Original operative statement and surrounding hypotheses opened; no claim that the full external article was independently reproved."
  },
  {
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "citation_key": "BS76",
    "title": "Algebraic methods in the global theory of complex spaces",
    "url": "https://djvu.online/file/2hQiOnz8WuoQk",
    "status": "verified_for_stated_use",
    "verified": true,
    "opened_locator": "Chapter III, §3 Theorem 3.4 and proof pp.116–120; Corollaries 3.5, 3.7 and 3.10 pp.120–122; §4 Theorem 4.12(i)–(iii) and proof pp.134–135.",
    "actual_use": "Analytic cohomology and base change, cohomological flatness, local freeness, and semicontinuity for full scheme fibres.",
    "hypotheses_and_normalization_check": "Properness, coherence and flatness of the coefficient sheaf are required. The constant-dimension converse in Theorem 4.12(ii) additionally requires a reduced base, satisfied by P1 and the discs here. The fibres themselves may be nonreduced. Corollary 3.10 identifies local freeness of all higher images with cohomological flatness in the bounded range.",
    "local_source": null,
    "source_sha256": null,
    "web_refs": [
      "turn157view1",
      "turn159view0",
      "turn159view1",
      "turn160view0",
      "turn160view1"
    ],
    "aliases": [
      "BanicaStanasila1976",
      "BS76push"
    ],
    "citation_contexts": [
      {
        "file": "deliverables/work/invariants_arithmetic/working_analytic_picard_proofs.tex",
        "line": 94,
        "context": "-sheaf-audit}.  Grauert's\ntheorem therefore gives local freeness of ranks \\(1,2,1\\) and base change\non a neighbourhood of \\(B^\\circ\\cup\\{p_0\\}\\); the precise analytic statement is\n\\cite[Chapter~III, \\S4, Theorem~4.12]{BS76}, originally due to\nGrauert \\cite{Grauert1960}.\n\nAt \\(p_j\\), use the finite cover \\(J'_j\\to N_j\\).  If\n\\(\\widetilde f:J'_j\\to\\Delta_j\\) is the smooth torus family and\n\\(\\pi(s)=s^{m_j}\\), exactness of finite-group invaria"
      },
      {
        "file": "deliverables/work/invariants_arithmetic/working_hodge_frolicher_proofs.tex",
        "line": 456,
        "context": "including for the nonreduced\nfinite fibres; precisely the same criterion, with citation, is recorded in\nthe proof of\n\\cref{wb:thm:structure-direct-images-audit}; see in particular\n\\cite[Chapter~III, \\S3, Theorem~3.4 and Corollary~3.10]{BS76}.\n\\end{proof}\n\n\\subsubsection{the logarithmic Kodaira--Spencer divisor}\\label{inv:wbproof:prop:log-ks-divisor}\nThe following working-edition argument proves the corresponding assertion of \\cref{inv:A2.1}.\n\n\n\\begin{proof}"
      }
    ],
    "extent": "Original operative statement and surrounding hypotheses opened; no claim that the full external article was independently reproved."
  },
  {
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "citation_key": "Cartan1954Quotient",
    "title": "Quotient d’une variété analytique par un groupe discret d’automorphismes",
    "url": "https://www.numdam.org/item/SHC_1953-1954__6__A12_0/",
    "status": "verified_for_stated_use",
    "verified": true,
    "opened_locator": "Exposé 12, §1, conditions (I)–(II), pp.1–2, and Theorem 1, p.2; original PDF first three pages including cover read locally.",
    "actual_use": "Analytic quotient structure in the finite free quotient charts.",
    "hypotheses_and_normalization_check": "The action has a Hausdorff quotient, finite stabilizers, and neighborhoods meeting only stabilizer translates. A finite group acting on the Hausdorff manifold here satisfies these conditions. The theorem gives a normal analytic space; smoothness of the free quotient is separately proved by disjoint local charts.",
    "local_source": "sources/external/maps_audit/cartan1954_quotient.pdf",
    "source_sha256": "38e9c37dfc803e71093d15a2e905c7f808c8cbc46ef5584a174bb307bdafde85",
    "web_refs": [],
    "aliases": [
      "Cartan1954"
    ],
    "citation_contexts": [
      {
        "file": "deliverables/work/invariants_arithmetic/working_hodge_frolicher_proofs.tex",
        "line": 284,
        "context": "ad C=\\mathbb C\\{s\\},\\qquad t=s^m,\n \\qquad (m,a)=(3,2)\\text{ or }(4,1).\n\\]\nCartan's analytic quotient theorem identifies local holomorphic functions on\nthe quotient with invariants \\cite[\\S1, Theorem~1, pp.~1--2]{Cartan1954Quotient}.\nThe action on the total space is free, so the quotient map is finite \\'etale;\nthe corresponding locally free sheaves and their equivariant structures\ndescend by finite \\'etale descent.  This sheaf statement is not bein"
      }
    ],
    "extent": "Original operative statement and surrounding hypotheses opened; no claim that the full external article was independently reproved."
  },
  {
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "citation_key": "Grauert1960",
    "title": "Ein Theorem der analytischen Garbentheorie und die Modulräume komplexer Strukturen",
    "url": "https://www.numdam.org/article/PMIHES_1960__5__5_0.pdf",
    "status": "verified_for_stated_use",
    "verified": true,
    "opened_locator": "§6 HauptsatzI, HauptsatzII and HauptsatzIIa p59; IIa formula and complete proof visually inspected on originalPDF page58; §7 Satz2 p61, read together with the1963 correction",
    "actual_use": "Proper direct-image coherence in the working structure-sheaf proof; base change uses the separately opened BS76 statements.",
    "hypotheses_and_normalization_check": "HauptsatzIIa is the analytic formal-functions isomorphism between the inverse limit of higher direct images of S/S.m_tilde^nu and the maximal-ideal completion of the stalk of R^i pi_* S. It requires a proper holomorphic map of complex spaces and coherent S, without projectivity or reducedness. Formula and full short proof were read in the original scan, rendered as reference_downloads/cdp_audit/Grauert1960_IIa.png. Its §7 Satz2 assertion about the failure locus must be read with the later correction. For closed analytic cohomology-jumping loci and base change this audit uses the separately opened BS76 finite-complex and flatness theorems.",
    "local_source": "reference_downloads/cdp_audit/Grauert1960.pdf",
    "source_sha256": "0559856be254902e7dd116725732117606912ab7d72b0f0fe88b600566829cde",
    "web_refs": [
      "turn50view2",
      "turn52view4"
    ],
    "aliases": [
      "Grauert60push",
      "Grauert1960D"
    ],
    "citation_contexts": [
      {
        "file": "deliverables/work/invariants_arithmetic/working_analytic_picard_proofs.tex",
        "line": 95,
        "context": "ks \\(1,2,1\\) and base change\non a neighbourhood of \\(B^\\circ\\cup\\{p_0\\}\\); the precise analytic statement is\n\\cite[Chapter~III, \\S4, Theorem~4.12]{BS76}, originally due to\nGrauert \\cite{Grauert1960}.\n\nAt \\(p_j\\), use the finite cover \\(J'_j\\to N_j\\).  If\n\\(\\widetilde f:J'_j\\to\\Delta_j\\) is the smooth torus family and\n\\(\\pi(s)=s^{m_j}\\), exactness of finite-group invariants in characteristic\nzero gives\n\\[\n R^qf_*\\ma"
      }
    ],
    "original_check_provenance": {
      "agent": "/root/cdp_audit",
      "record": "work/cdp_audit/references_verified.json",
      "citation_key": "Grauert1960",
      "recorded_checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), writing run; 17 November 2026 (Europe/Berlin)"
    },
    "extent": "Original-source reading is the recorded parallel writing-run check; this reader separately matched the WB application to those precise hypotheses."
  },
  {
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "citation_key": "RR70",
    "title": "Complexe dualisant et théorèmes de dualité en géométrie analytique complexe",
    "url": "https://www.numdam.org/article/PMIHES_1970__38__77_0.pdf",
    "status": "verified_for_stated_use",
    "verified": true,
    "opened_locator": "§3, Theorem1, published p.81; dualizing-complex amplitude on p.89; Proposition2 and complete-intersection calculation p.91",
    "actual_use": "Serre duality on the compact possibly nonreduced Gorenstein Cartier fibres.",
    "hypotheses_and_normalization_check": "Original journal PDF read locally. Countable-at-infinity bounded-dimensional analytic spaces are allowed. On compact fibres the coherent groups are finite-dimensional and separated; the Cartier Gorenstein dualizing complex is an invertible sheaf shifted by dimension. A locally free twist reduces Ext to cohomology of its dual tensor the dualizing line. No smoothness or reducedness is inserted.",
    "local_source": "reference_downloads/cdp_audit/RamisRuget1970.pdf",
    "source_sha256": "283dbde1ce597b2cdd7ae4110e3f0f991aeee23a6086568cc10e6e5e720c674b",
    "web_refs": [],
    "aliases": [
      "RR70push",
      "RamisRuget1970"
    ],
    "citation_contexts": [
      {
        "file": "deliverables/work/invariants_arithmetic/working_analytic_picard_proofs.tex",
        "line": 164,
        "context": "wb:eq:9.15}\n\\]\nThe relative theorem is the one of Ramis--Ruget--Verdier\n\\cite[pp.~261--283]{RRV71}; the absolute singular\ndualizing-complex comparison is independently recorded in\n\\cite[Theorems~1--2 and Proposition~2]{RR70}.\n\nThe relative cup product\n\\[\n \\bigwedge^2G\\longrightarrow R^2f_*\\mathcal O_X\n\\tag{WBA.9.16}\\label{inv:wb:eq:9.16}\n\\]\nis an isomorphism.  It is so on every smooth torus fibre.  At the cusp it\nis so by the base-change as"
      }
    ],
    "original_check_provenance": {
      "agent": "/root/cdp_audit",
      "record": "work/cdp_audit/references_verified.json",
      "citation_key": "RR70",
      "recorded_checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), writing run; 17 November 2026 (Europe/Berlin)"
    },
    "extent": "Original-source reading is the recorded parallel writing-run check; this reader separately matched the WB application to those precise hypotheses."
  },
  {
    "checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "citation_key": "RRV71",
    "title": "Dualité relative en géométrie analytique complexe",
    "url": "https://gdz.sub.uni-goettingen.de/id/PPN356556735_0013",
    "status": "verified_for_stated_use",
    "verified": true,
    "opened_locator": "Introduction equation(1), original p.261; §1 proper-duality trace quasi-isomorphism p.264; §2 relative trace, pp.265–268; Proposition2.1 continuity statement p.266",
    "actual_use": "Relative analytic duality for the proper flat Gorenstein surface family over the smooth curve.",
    "hypotheses_and_normalization_check": "Opened the original journal scan through its public GDZ IIIF manifest and visually checked pp.261,264,265,266 after reading the text of §§1–2. The introduction explicitly asserts that equation(1) is an isomorphism for a proper morphism of complex analytic spaces; §1 writes the required Rf_*RHom(F,K_X•)→RHom(Rf_*F,K_Y•). No projectivity or Kähler hypothesis occurs. For E3.1 the smooth total space and base give absolute dualizing complexes ω_Y[3] and ω_U[1]; projection and cancellation give Rp_*ω_Y/U[2]≅RHom(Rp_*O_Y,O_U), and the independently checked locally free cohomology gives the degree−2 edge. Proposition2.1 is the continuity step for the trace construction, not a theorem numbered as the general duality result. The article’s remaining functional-analytic proofs in §§3–4 were not audited.",
    "local_source": null,
    "source_sha256": null,
    "web_refs": [
      "turn123view0",
      "turn125view0"
    ],
    "aliases": [
      "RRV71push",
      "RamisRugetVerdier1971"
    ],
    "citation_contexts": [
      {
        "file": "deliverables/work/invariants_arithmetic/working_analytic_picard_proofs.tex",
        "line": 162,
        "context": "t}, it gives\n\\[\n R^2f_*\\mathcal O_X\\simeq\\mathfrak K^\\vee\n \\simeq\\mathcal O_B(-1).\n\\tag{WBA.9.15}\\label{inv:wb:eq:9.15}\n\\]\nThe relative theorem is the one of Ramis--Ruget--Verdier\n\\cite[pp.~261--283]{RRV71}; the absolute singular\ndualizing-complex comparison is independently recorded in\n\\cite[Theorems~1--2 and Proposition~2]{RR70}.\n\nThe relative cup product\n\\[\n \\bigwedge^2G\\longrightarrow R^2f_*\\mathcal O_X\n\\tag{WBA.9.16}\\"
      }
    ],
    "original_check_provenance": {
      "agent": "/root/cdp_audit",
      "record": "work/cdp_audit/references_verified.json",
      "citation_key": "RRV71",
      "recorded_checker": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), writing run; 17 November 2026 (Europe/Berlin)"
    },
    "extent": "Original-source reading is the recorded parallel writing-run check; this reader separately matched the WB application to those precise hypotheses.",
    "original_page_files": [
      {
        "page": "261",
        "url": "https://images.p.sub.uni-goettingen.de/iiif/image/gdz:PPN356556735_0013:00000275/full/1800,/0/default.jpg",
        "path": "reference_downloads/cdp_audit/RRV71_p261.jpg",
        "sha256": "6986f780a581fd6efc07462a77c50c67fb0422fd2e836a81922fd738fb12ca81",
        "bytes": 830095
      },
      {
        "page": "262",
        "url": "https://images.p.sub.uni-goettingen.de/iiif/image/gdz:PPN356556735_0013:00000276/full/1800,/0/default.jpg",
        "path": "reference_downloads/cdp_audit/RRV71_p262.jpg",
        "sha256": "c82972927ab912874716d4ea8bcd7809adfd3ee9a00f76155cbc1fd6288f687a",
        "bytes": 836349
      },
      {
        "page": "263",
        "url": "https://images.p.sub.uni-goettingen.de/iiif/image/gdz:PPN356556735_0013:00000277/full/1800,/0/default.jpg",
        "path": "reference_downloads/cdp_audit/RRV71_p263.jpg",
        "sha256": "591e6ac8c06854c9e18ee56289912dafbf98df87dcac36439702c546ce103e7c",
        "bytes": 890538
      },
      {
        "page": "264",
        "url": "https://images.p.sub.uni-goettingen.de/iiif/image/gdz:PPN356556735_0013:00000278/full/1800,/0/default.jpg",
        "path": "reference_downloads/cdp_audit/RRV71_p264.jpg",
        "sha256": "fc94bb88f92e0dd20afa7e4a5751c0d10682adff81000758eb846dc786c4eb19",
        "bytes": 733095
      },
      {
        "page": "265",
        "url": "https://images.p.sub.uni-goettingen.de/iiif/image/gdz:PPN356556735_0013:00000279/full/1800,/0/default.jpg",
        "path": "reference_downloads/cdp_audit/RRV71_p265.jpg",
        "sha256": "a6b7d205128fa94a9c64493199fa8f9a6f033ba94d9f37833d50ed2c2b9e97f3",
        "bytes": 837271
      },
      {
        "page": "266",
        "url": "https://images.p.sub.uni-goettingen.de/iiif/image/gdz:PPN356556735_0013:00000280/full/1800,/0/default.jpg",
        "path": "reference_downloads/cdp_audit/RRV71_p266.jpg",
        "sha256": "1319c20a09ddf5b7232fc0bf5598ab2c432c49d011cd3406b8cec1c744e2266a",
        "bytes": 728476
      },
      {
        "page": "267",
        "url": "https://images.p.sub.uni-goettingen.de/iiif/image/gdz:PPN356556735_0013:00000281/full/1800,/0/default.jpg",
        "path": "reference_downloads/cdp_audit/RRV71_p267.jpg",
        "sha256": "46abb6ca6005298239af3c3e63e7541351c3c000979daa513456704ffdb8a0b9",
        "bytes": 826516
      },
      {
        "page": "268",
        "url": "https://images.p.sub.uni-goettingen.de/iiif/image/gdz:PPN356556735_0013:00000282/full/1800,/0/default.jpg",
        "path": "reference_downloads/cdp_audit/RRV71_p268.jpg",
        "sha256": "0d293523c4f2924e6c0eb770dbda585add939be6839cba41ae4c959350449700",
        "bytes": 708212
      }
    ]
  }
]
```

### work/cdp_audit/references_verified.json

```json
[
  {
    "key": "GS2014",
    "title": "Normal crossing properties of complex hypersurfaces via logarithmic residues",
    "url": "https://arxiv.org/pdf/1109.2612",
    "status": "verified in the specified scope",
    "opened_locators": [
      "arXiv:1109.2612v7, Theorems 1.1 and 1.3, p.3",
      "Proposition 3.4, p.9; Corollary 3.5, p.10; proof of Theorem 1.3, p.12"
    ],
    "uses": [
      "CDP A.2.1 inverse Jacobian/residue identification",
      "CDP A.2.2 Jacobian-conductor inclusion",
      "CDP A.2.3 normalization-residue normal-crossing criterion"
    ],
    "verification_scope": "Opened and matched reduced hypersurface hypotheses. No free-divisor hypothesis from the later Corollary 3.7 is imported. The residue criterion is known; these algebraic identifications are re-derived.",
    "own_check": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), effort Pro, writing run; 17 November 2026 UTC",
    "web_refs": [
      "turn18view0"
    ],
    "local_pdf": "reference_downloads/cdp_audit/GS2014.pdf",
    "sha256": "98bf8328a08614509b1dcc20d2e387d7c5a2cce5b70687cf7ad77a1a21aa70dc",
    "download_status": "genuine PDF retained and opened in stated scope",
    "not_verified": []
  },
  {
    "key": "Kulikov1981",
    "title": "On modifications of degenerations of surfaces with kappa=0",
    "url": "https://www.mathnet.ru/php/getFT.phtml?jrnid=im&option_lang=eng&paperid=1953&what=fullteng",
    "status": "verified in the specified scope",
    "opened_locators": [
      "All four English pages, 339–342",
      "Theorem 1-prime p.340; modification definition §2 p.339; finite reduction §§7–10 pp.341–342; corrections §11 p.342"
    ],
    "uses": [
      "CDP C.2.UN.75 Hopf-minimum canonical-flat reduction",
      "CDP UN77/81 restored ruled cleanup and UN84 stopped selection"
    ],
    "verification_scope": "Theorem1-prime applies to good analytic degenerations with trivial canonical class on nearby fibres; class-VII components must attain the minimum canonical coefficient. Projectivity is not a hypothesis. Independently, §7 expressly states the selector needs only ruled current maxima; §8 removes H¹(dual complex)=0 and distinguished-component steps, inserts missing fibre links in actual smooth charts, assigns them orderq+1 and adds none for a maximal-order selected component. §9 proves finite full-positive-order card induction. This matches the stopped/cleanup uses without invoking the final theorem outside its hypothesis. Opened via web PDF; no successful direct-download hash claimed.",
    "own_check": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), effort Pro, writing run; 17 November 2026 UTC",
    "web_refs": [
      "turn18view1",
      "turn11view0",
      "turn12view0",
      "turn64view0"
    ],
    "local_pdf": null,
    "sha256": null,
    "download_status": "download failed",
    "not_verified": []
  },
  {
    "key": "Kulikov1977",
    "title": "Degenerations of K3 surfaces and Enriques surfaces",
    "url": "https://www.mathnet.ru/php/getFT.phtml?jrnid=im&option_lang=eng&paperid=1877&what=fullteng",
    "status": "verified in the specified scope",
    "opened_locators": [
      "Definition of good degeneration, p958; §§2.18–2.21 pp964–965",
      "§§4.5–4.8.12 pp970–976; §§4.9–4.10.8 pp977–982",
      "§4.11.2 and §§4.12–4.14.5 pp982–985; §§4.16.2–4.17 pp986–988"
    ],
    "uses": [
      "CDP C.2.UN.75 retained-overlap interpretation of local modifications",
      "CDP UN77/81 cleanup of actual sigma-atlas and UN84 stopped component selection"
    ],
    "verification_scope": "Read the specified actual local contractions, typeI/II and chain/cycle selector, fibre minimization, reverse-order restoration of overlap, singular sigma-atlas, last-locally-blown-branch reordering and Lemma4.14 conditions(a)–(e). The maximum chosen last branch gives condition(e) because every local child has order one larger. The auxiliary resolution is diagnostic, not a retained global semistable stage. Read4.17 final smoothness and the same-receiver typeII balance. Original TheoremI is projective; the applications use the1981 explicit changes to its algorithm, not an unrestricted1977 theorem.",
    "own_check": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), effort Pro, writing run; 17 November 2026 UTC",
    "web_refs": [
      "turn18view2",
      "turn11view1",
      "turn12view1",
      "turn72view1",
      "turn73view0",
      "turn73view1",
      "turn75view0",
      "turn75view1",
      "turn75view2",
      "turn77view0",
      "turn77view1"
    ],
    "local_pdf": null,
    "sha256": null,
    "download_status": "download failed",
    "not_verified": []
  },
  {
    "key": "CDP2020",
    "title": "The algebraic dimension of compact complex threefolds with vanishing second Betti number",
    "url": "https://www.cambridge.org/core/services/aop-cambridge-core/content/view/CDF2D04CFB35CEE105E10B188D97D68A/S0010437X19007802a.pdf/the-algebraic-dimension-of-compact-complex-threefolds-with-vanishing-second-betti-number.pdf",
    "status": "verified in the specified scope",
    "opened_locators": [
      "Published pp.680,684–685,692–694",
      "Theorem 2.2, Corollary 2.3, Proposition 2.4; Lemmas 4.2–4.3; §7 endpoint inference and Proposition 7.3 through its ruled-surface step"
    ],
    "uses": [
      "Working corrected global/relative criterion",
      "Correction note exact p.692 endpoint implication",
      "CDP A.4.2 constant genus-one family counterexample",
      "CDP D.1.1–D.1.3 coinvariant correction"
    ],
    "verification_scope": "Exact printed hypotheses and failed inferences opened. The original p.692 endpoint implication drops cotangent torsion. Proposition7.3 expressly permits constant normalized twists before concluding genus at least2. Lemma4.2 repeats the unsound direct-sum abelianization. No theorem-level refutation is inferred without the constructed global example.",
    "own_check": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), effort Pro, writing run; 17 November 2026 UTC",
    "web_refs": [
      "turn23view0",
      "turn22search6"
    ],
    "local_pdf": "reference_downloads/cdp_audit/CDP2020.pdf",
    "sha256": "c4cb6408f97dec241d1d1e6f9cc30029f3d51272433717d0592a46ec501898b4",
    "download_status": "genuine PDF retained and opened in stated scope",
    "not_verified": []
  },
  {
    "key": "CDP1998",
    "title": "The algebraic dimension of compact complex threefolds with vanishing second Betti number",
    "url": "https://arxiv.org/pdf/math/9607215",
    "status": "verified in the specified scope",
    "opened_locators": [
      "arXiv:math/9607215v1, pp.11–12, Lemma5.2(1)–(3)"
    ],
    "uses": [
      "CDP D.1.1–D.1.2; working semidirect abelianization"
    ],
    "verification_scope": "The opened preprint numbers the published Lemma3.2 as Lemma5.2. Its proof explicitly passes from a split group extension to a direct sum with full H1(fibre). The published page numbering has not yet been independently checked in a journal scan.",
    "own_check": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), effort Pro, writing run; 17 November 2026 UTC",
    "web_refs": [
      "turn23view1"
    ],
    "local_pdf": "reference_downloads/cdp_audit/CDP1998_preprint.pdf",
    "sha256": "7b7dbaf4e872e22ad7acbacc36ade6d67742bb226f37bfde0642a6a8d1852c78",
    "download_status": "downloaded",
    "not_verified": []
  },
  {
    "key": "HKP2000",
    "title": "Group actions on S6 and complex structures on P3",
    "url": "https://arxiv.org/pdf/math/9812076",
    "status": "verified in the specified scope",
    "opened_locators": [
      "arXiv:math/9812076v1, p.2, Corollary1.3 and its complete proof; Corollary1.4"
    ],
    "uses": [
      "INV E2.4 universal two-vector-field bound and the precise failed CDP dependence"
    ],
    "verification_scope": "The universal h0(T)<=2 assertion is printed. The proof uses constancy of meromorphic functions attributed to CDP1998. It does not establish the bound independently of that input. The audit distinguishes this corollary from non-almost-homogeneity itself.",
    "own_check": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), effort Pro, writing run; 17 November 2026 UTC",
    "web_refs": [
      "turn23view2"
    ],
    "local_pdf": "reference_downloads/cdp_audit/HKP2000_preprint.pdf",
    "sha256": "fe053b6c4b572a432be3de60fd1a8a2305e0978712f85ae77a0ee2f7f1b4500f",
    "download_status": "downloaded",
    "not_verified": []
  },
  {
    "key": "ACampo1975",
    "title": "La fonction zêta d'une monodromie",
    "url": "https://www.e-periodica.ch/cntmng?bot=1&pid=com-001%3A1975%3A50%3A%3A27",
    "status": "verified in the specified scope",
    "opened_locators": [
      "Theorem1, p.235 (PDF page4), formula inspected in rendered image",
      "§2.1–§2.2, pp.237–241, proper analytic normal-crossing global boundary construction and fibration lemma"
    ],
    "uses": [
      "CDP C.2.UN.11 monodromy-to-stratum Euler formula",
      "Boundary retraction/normal-crossing support comparisons"
    ],
    "verification_scope": "The source supports sum_{m|k} m chi(S_m) for the kth Lefschetz number, and its global construction is explicitly for a proper analytic map from a smooth space with normal-crossing divisor. Initial web bot failure was bypassed by downloading and opening the genuine journal scan. The formula was visually checked because OCR omitted symbols.",
    "own_check": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), effort Pro, writing run; 17 November 2026 UTC",
    "web_refs": [
      "turn22search7"
    ],
    "local_pdf": "reference_downloads/cdp_audit/ACampo1975.pdf",
    "sha256": "d05a9845d695dae388e39773769cd2854e7ebfbdac634b4aadb7f95b00ba1c1e",
    "download_status": "genuine PDF retained and opened in stated scope",
    "not_verified": []
  },
  {
    "key": "SchnellLecture3",
    "title": "MAT615 Lecture3: Holomorphic line bundles, Appell–Humbert theorem",
    "url": "https://www.math.stonybrook.edu/~cschnell/mat615/lectures/lecture3.pdf",
    "status": "verified in the specified scope",
    "opened_locators": [
      "Equations(3.3)–(3.10), pp.3–7; explicit exponential connecting two-cocycle and alternating Chern form"
    ],
    "uses": [
      "Working prop:local-cusp-picard-obstruction exact c1=-2q sign",
      "Working prop:analytic-ah-boundary factor extension",
      "Working lem:analytic-support-specialization mixed-block sign"
    ],
    "verification_scope": "Opened the actual author notes and matched the factor-of-automorphy and antisymmetrized logarithm convention. The bespoke descent/cusp support computations remain independently proved in the manuscript.",
    "own_check": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), effort Pro, writing run; 17 November 2026 UTC",
    "web_refs": [
      "turn23view3"
    ],
    "local_pdf": "reference_downloads/cdp_audit/SchnellLecture3.pdf",
    "sha256": "973a56aef940573a125488ecc8030e858eecfd68bfa43dc33297e8a2c4e14928",
    "download_status": "genuine PDF retained and opened in stated scope",
    "not_verified": []
  },
  {
    "key": "Guillot2024",
    "title": "On the singularities of complete holomorphic vector fields in dimension two",
    "url": "https://www.matem.unam.mx/~guillot/guillot-singularities.pdf",
    "status": "verified in the specified scope",
    "opened_locators": [
      "Theorem3.3 and complete proof, p.9",
      "Theorem9.2 and preceding scope definition, p.28"
    ],
    "uses": [
      "CDP C.2.UN.15/16 closure of the semicomplete locus on the smooth threefold and component",
      "CDP C.2.UN.16/22 algebraic-dimension-zero birational holomorphic/fibration alternative"
    ],
    "verification_scope": "Theorem3.3 expressly works on a complex manifold of any dimension; Theorem9.2 expressly covers compact complex surfaces with meromorphic fields semicomplete on their holomorphic locus. Thus neither Kählerness nor entire solutions are silently inserted.",
    "own_check": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), effort Pro, writing run; 17 November 2026 UTC",
    "web_refs": [
      "turn29view0",
      "turn31view0",
      "turn31view1"
    ],
    "local_pdf": null,
    "sha256": null,
    "download_status": "not attempted in this checkpoint",
    "not_verified": []
  },
  {
    "key": "Guillot2019",
    "title": "Meromorphic vector fields with single-valued solutions on complex surfaces",
    "url": "https://arxiv.org/pdf/1603.02288",
    "status": "verified in the specified scope",
    "opened_locators": [
      "Main Theorem and following clarification, p.2",
      "Proposition22, p.25"
    ],
    "uses": [
      "CDP C.2.UN.15 exclusion of general-type components",
      "CDP C.2.UN.22 dense-leaf projective branch"
    ],
    "verification_scope": "The main theorem requires compact Kähler surface and a Zariski-dense univalent maximal solution. The uses checked here are on projective models and supply semicompleteness, hence meet those hypotheses. Holomorphic branch is controlled by Proposition22; no non-Kähler use of this theorem is made.",
    "own_check": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), effort Pro, writing run; 17 November 2026 UTC",
    "web_refs": [
      "turn29view1",
      "turn31view2",
      "turn30view3"
    ],
    "local_pdf": null,
    "sha256": null,
    "download_status": "not attempted in this checkpoint",
    "not_verified": []
  },
  {
    "key": "DOT2000",
    "title": "Surfaces de la classe VII0 admettant un champ de vecteurs",
    "url": "https://ems.press/content/serial-article-files/42865?nt=1",
    "status": "verified in the specified scope",
    "opened_locators": [
      "Introduction p.256; opening of §2 p.260"
    ],
    "uses": [
      "CDP C.2.UN.16 at most one holomorphic field on minimal classVII with b2>0",
      "CDP C.2.UN.19 algebraic dimension zero of that class"
    ],
    "verification_scope": "The exact dimension bound is stated under minimality,b1=1,b2>=1. These hypotheses are the ones used after descending the two fields to the same minimal model.",
    "own_check": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), effort Pro, writing run; 17 November 2026 UTC",
    "web_refs": [
      "turn29view2",
      "turn31view4"
    ],
    "local_pdf": null,
    "sha256": null,
    "download_status": "not attempted in this checkpoint",
    "not_verified": []
  },
  {
    "key": "DOT2001",
    "title": "Surfaces de la classe VII0 admettant un champ de vecteurs, II",
    "url": "https://ems.press/content/serial-article-files/42912?nt=1",
    "status": "verified in the specified scope",
    "opened_locators": [
      "Theorem0.3, pp.641–642, full minimal-surface list"
    ],
    "uses": [
      "CDP C.2.UN.16 classification with two holomorphic fields",
      "CDP C.2.UN.22 nonnegative-Kodaira branches"
    ],
    "verification_scope": "Opened the complete list and its compact minimal surface hypothesis. In algebraic dimension zero, elliptic Seifert alternatives are excluded by their fibration. The theorem is cited as established classification, not re-proved.",
    "own_check": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), effort Pro, writing run; 17 November 2026 UTC",
    "web_refs": [
      "turn29view3",
      "turn31view3"
    ],
    "local_pdf": null,
    "sha256": null,
    "download_status": "not attempted in this checkpoint",
    "not_verified": []
  },
  {
    "key": "RR70",
    "title": "Complexe dualisant et théorèmes de dualité en géométrie analytique complexe",
    "url": "https://www.numdam.org/article/PMIHES_1970__38__77_0.pdf",
    "status": "verified in the specified scope",
    "opened_locators": [
      "§3, Theorem1, published p.81; dualizing-complex amplitude on p.89; Proposition2 and complete-intersection calculation p.91"
    ],
    "uses": [
      "Compact singular or nonreduced Cartier-fibre Serre duality in working thm:cartier-duality and prop:cartier-duality-absolute",
      "PUSH E.2.9 absolute fibre duality",
      "UN65/68 Gorenstein SNC surface duality"
    ],
    "verification_scope": "Original journal PDF read locally. Countable-at-infinity bounded-dimensional analytic spaces are allowed. On compact fibres the coherent groups are finite-dimensional and separated; the Cartier Gorenstein dualizing complex is an invertible sheaf shifted by dimension. A locally free twist reduces Ext to cohomology of its dual tensor the dualizing line. No smoothness or reducedness is inserted.",
    "own_check": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), effort Pro, writing run; 17 November 2026 UTC",
    "web_refs": [],
    "local_pdf": "reference_downloads/cdp_audit/RamisRuget1970.pdf",
    "sha256": "283dbde1ce597b2cdd7ae4110e3f0f991aeee23a6086568cc10e6e5e720c674b",
    "download_status": "downloaded",
    "not_verified": [],
    "aliases": [
      "RR70push",
      "RamisRuget1970"
    ]
  },
  {
    "key": "BS76",
    "title": "Algebraic Methods in the Global Theory of Complex Spaces",
    "url": "https://djvu.online/file/2hQiOnz8WuoQk",
    "status": "verified in the specified scope",
    "opened_locators": [
      "ChapterIII Theorem4.1, p.124, complete statement",
      "ChapterIII Theorem4.12(i)–(iii) and proof, pp.134–135; cohomological-flatness criteria immediately before"
    ],
    "uses": [
      "Proper finite free cohomology complexes and analytic jumping loci",
      "Semicontinuity and constant-zero top-cohomology base change in working and PUSH E.2.9",
      "Euler characteristic invariance in UN65/68"
    ],
    "verification_scope": "Actual book transcription opened through web retrieval. Theorem4.1 is bounded when the coherent sheaf is flat over the base. Theorem4.12(ii) converse requires a reduced base; the uses on P1, discs and affine Picard lines meet it. Do not replace finite-complex reasoning on nonreduced bases by this converse. Direct HTML download returned an anti-bot challenge, not a copy of the book; no source hash is claimed.",
    "own_check": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), effort Pro, writing run; 17 November 2026 UTC",
    "web_refs": [
      "turn46view0",
      "turn48view0",
      "turn48view1"
    ],
    "local_pdf": null,
    "sha256": null,
    "download_status": "download failed",
    "not_verified": [],
    "aliases": [
      "BS76push",
      "BanicaStanasila1976"
    ]
  },
  {
    "key": "Nakano1970",
    "title": "On the Inverse of Monoidal Transformation",
    "url": "https://ems.press/content/serial-article-files/41677",
    "status": "verified in the specified scope",
    "opened_locators": [
      "Main Theorem, published p.484; ordinary blowdown local conclusion"
    ],
    "uses": [
      "CDP UN64 smooth ordinary blowdown of a projective-space-bundle divisor"
    ],
    "verification_scope": "Original theorem statement read. It has both normal O(-1) condition alpha and an extra canonical condition beta. The latter is removed by Fujiki–Nakano1971; the original alone is not the cited sufficient theorem.",
    "own_check": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), effort Pro, writing run; 17 November 2026 UTC",
    "web_refs": [
      "turn46view2"
    ],
    "local_pdf": "reference_downloads/cdp_audit/Nakano1970.pdf",
    "sha256": "ec60be2235c29e43943641ec03472867c457206170a1b2e5a0485802d03fc37a",
    "download_status": "genuine PDF retained and opened in stated scope",
    "not_verified": []
  },
  {
    "key": "FujikiNakano1971",
    "title": "Supplement to On the Inverse of Monoidal Transformation",
    "url": "https://www.jstage.jst.go.jp/article/kyotoms1969/7/3/7_3_637/_pdf/-char/ja",
    "status": "verified in the specified scope",
    "opened_locators": [
      "Introduction p.637; §2 Theorem2-prime pp.640–641 and Proposition9-prime p.642 with its local chart conclusion"
    ],
    "uses": [
      "CDP UN64 curve and point blowdowns with normal O(-1) on every projective fibre",
      "Subsequent actual contraction records using UN64"
    ],
    "verification_scope": "The supplement explicitly repairs the earlier cohomological proof and makes normal condition alpha sufficient. The local maps give ordinary blowups of smooth centres and glue off the exceptional divisor. UN64 supplies the prescribed holomorphic projective bundle and exactly this normal restriction.",
    "own_check": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), effort Pro, writing run; 17 November 2026 UTC",
    "web_refs": [
      "turn46view1",
      "turn47view2",
      "turn48view2"
    ],
    "local_pdf": "reference_downloads/cdp_audit/FujikiNakano1971.pdf",
    "sha256": "2c2d2f6c8445f26437cdf64398745215b6448debc86f72829a7159fec8e6b72c",
    "download_status": "genuine PDF retained and opened in stated scope",
    "not_verified": []
  },
  {
    "key": "Grauert1960",
    "title": "Ein Theorem der analytischen Garbentheorie und die Modulräume komplexer Strukturen",
    "url": "https://www.numdam.org/article/PMIHES_1960__5__5_0.pdf",
    "status": "verified in the specified scope",
    "opened_locators": [
      "§6 HauptsatzI, HauptsatzII and HauptsatzIIa p59; IIa formula and complete proof visually inspected on originalPDF page58",
      "§7 Satz2 p61, read together with the1963 correction"
    ],
    "uses": [
      "Proper direct-image coherence; separation of coherence from base-change/jumping-locus claims",
      "PUSH B4.11 analytic formal-functions comparison"
    ],
    "verification_scope": "HauptsatzIIa is the analytic formal-functions isomorphism between the inverse limit of higher direct images of S/S.m_tilde^nu and the maximal-ideal completion of the stalk of R^i pi_* S. It requires a proper holomorphic map of complex spaces and coherent S, without projectivity or reducedness. Formula and full short proof were read in the original scan, rendered as reference_downloads/cdp_audit/Grauert1960_IIa.png. Its §7 Satz2 assertion about the failure locus must be read with the later correction. For closed analytic cohomology-jumping loci and base change this audit uses the separately opened BS76 finite-complex and flatness theorems.",
    "own_check": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), effort Pro, writing run; 17 November 2026 UTC",
    "web_refs": [
      "turn50view2",
      "turn52view4"
    ],
    "local_pdf": "reference_downloads/cdp_audit/Grauert1960.pdf",
    "sha256": "0559856be254902e7dd116725732117606912ab7d72b0f0fe88b600566829cde",
    "download_status": "genuine PDF retained and opened in stated scope",
    "not_verified": [],
    "aliases": [
      "Grauert60push",
      "Grauert1960D"
    ]
  },
  {
    "key": "Grauert1963",
    "title": "Berichtigung: Ein Theorem der analytischen Garbentheorie und die Modulräume komplexer Strukturen",
    "url": "https://www.numdam.org/item/PMIHES_1963__16__35_0.pdf",
    "status": "verified in the specified scope",
    "opened_locators": [
      "Entire two-page correction pp.35–36, particularly item2 p.36"
    ],
    "uses": [
      "PUSH E.2.9 and working analytic-base-change source qualification"
    ],
    "verification_scope": "Read all corrections. Item2 explicitly withdraws the closedness assertion for the locus where the §7 Satz2 base-change map is not bijective. It does not invalidate the proper-coherence theorem or the independently established finite-complex approach.",
    "own_check": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), effort Pro, writing run; 17 November 2026 UTC",
    "web_refs": [
      "turn50view1",
      "turn52view3"
    ],
    "local_pdf": "reference_downloads/cdp_audit/Grauert1963.pdf",
    "sha256": "04b24590e8c56e1a05c0cb520843e8160447ebb560d9ca2394b0682d83ed489c",
    "download_status": "genuine PDF retained and opened in stated scope",
    "not_verified": [],
    "aliases": [
      "Grauert63push",
      "Grauert1963ErratumD"
    ]
  },
  {
    "key": "GrossSiebert2006I",
    "title": "Mirror symmetry via logarithmic degeneration data I",
    "url": "https://arxiv.org/pdf/math/0309070",
    "status": "verified in the specified scope",
    "opened_locators": [
      "arXiv:math/0309070v3: Definition1.60 pp.45–46; Theorem3.22 pp.95–97; Example3.30 p.106",
      "Definition4.3 pp.108–109; complete units-to-residues comparison in Theorem4.14 pp.114–116",
      "Theorems5.2 pp.128–129 and5.4 p.134, statements and the latter proof"
    ],
    "uses": [
      "CDP UN71 central-log-space gluing classification after its analytic-to-algebraic comparison"
    ],
    "verification_scope": "Opened the original preprint and matched the hypotheses. The classification is for proper reduced toric log Calabi–Yau algebraic spaces; no polarization is required by Theorem5.4. UN71 supplies algebraicity via its SNC conductor gluing and constant residue maps. Empty affine discriminant gives p=0 simplicity. The source classifies central log spaces, not analytic smoothing germs; actual proper smoothing is separately constructed in UN71.",
    "own_check": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), effort Pro, writing run; 17 November 2026 UTC",
    "web_refs": [
      "turn50view0",
      "turn52view0",
      "turn52view1",
      "turn52view2",
      "turn53view0",
      "turn53view1"
    ],
    "local_pdf": "reference_downloads/cdp_audit/GrossSiebert2006I.pdf",
    "sha256": "9201a67b58ca563f5ac867803b132fd620fb0cff0d0546e5aab957a9125bfb1e",
    "download_status": "genuine PDF retained and opened in stated scope",
    "not_verified": []
  },
  {
    "key": "Viaclovsky2026Combs",
    "title": "Combs and complex structures on the six-sphere",
    "url": "https://arxiv.org/abs/2610.10451",
    "status": "verified in the specified scope",
    "opened_locators": [
      "Supplied TeX dated7October2026: t:main (lines236–258), allfree (490–576), degrees (699 onward)",
      "localquotient (1882–1901); degreechange (2139); normalbundle/parambundles (2149–2177)",
      "paramspace (2182–2240), effective (2242–2285), initial bundles (2330–2428), smoothingbound (2454–2478)"
    ],
    "uses": [
      "INV E2.1 known coherent degrees and dimensions",
      "CDP E15 and INV E2.2 comparison with the previously established 8m-8 lower bound"
    ],
    "verification_scope": "The actual supplied source was opened and its stated hypotheses matched, including m>=12, unchanged singular-fibre types and fixed limiting periods. It establishes det degree2m-1, nonnegative splitting, h(O) and a section-family lower bound8m-8. It does not establish the later exact tangent dimensions or smooth miniversal8m+1 germ; those require the separate complete E15 proof. No independent online metadata verification is claimed.",
    "own_check": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), effort Pro, writing run; 17 November 2026 UTC",
    "web_refs": [],
    "local_pdf": null,
    "sha256": "42dea62b023dfb75a009a8c83c15349ddc8f853162f753e3547ca583d07b74d5",
    "download_status": "supplied source opened",
    "not_verified": [],
    "supplied_source": "sources/papers/arXiv_2610.10451_Viaclovsky_combs_src/Viaclovsky_Comb_S6_Draft_October_7_2026.tex",
    "aliases": [
      "ViaclovskyCombs2026"
    ]
  },
  {
    "key": "Buchdahl1999",
    "title": "On compact Kähler surfaces",
    "url": "https://www.numdam.org/article/AIF_1999__49_1_287_0.pdf",
    "status": "verified in the specified scope",
    "opened_locators": [
      "Theorem11, printed p.297"
    ],
    "uses": [
      "CDP C.2.UN.5 smooth central surface with b1=4 is Kähler"
    ],
    "verification_scope": "The exact theorem statement was opened: a compact complex surface with even first Betti number is Kähler. The application supplies a smooth compact connected surface and b1=4 by the actual smooth family. The entire analytic metric proof was not audited.",
    "own_check": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), effort Pro, writing run; 17 November 2026 UTC",
    "web_refs": [
      "turn79view0",
      "turn80view1"
    ],
    "local_pdf": "reference_downloads/cdp_audit/Buchdahl1999.pdf",
    "sha256": "9d5be904779f040102392f41f6acb4717e2b8ec874443d128532f234406c8c0e",
    "download_status": "genuine PDF retained and opened in stated scope",
    "not_verified": []
  },
  {
    "key": "Catanese2002",
    "title": "Deformation types of real and complex manifolds",
    "url": "https://arxiv.org/pdf/math/0111245",
    "status": "verified in the specified scope",
    "opened_locators": [
      "arXiv:math/0111245v2: Definition3.1 and Theorems3.2–3.3, p.9",
      "Theorem4.6, full statement and proof, pp.13–14; Lemma4.7 and Proposition4.8, p.15"
    ],
    "uses": [
      "CDP C.2.UN.5 smooth torus specialization and bielliptic deck-quotient classification"
    ],
    "verification_scope": "Opened the torus deformation result and its proof, and the cohomological-torus criterion with closed holomorphic one-forms. The manuscript supplies its own Kähler Albanese argument. Opened the complete seven-type bielliptic list and the E×F/G definition, including translations on E and F/G=P1. These are established classification inputs; no audit of every classification proof is claimed.",
    "own_check": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), effort Pro, writing run; 17 November 2026 UTC",
    "web_refs": [
      "turn79view1",
      "turn80view2",
      "turn80view3",
      "turn81view1",
      "turn81view2",
      "turn82view1"
    ],
    "local_pdf": "reference_downloads/cdp_audit/Catanese2002.pdf",
    "sha256": "7f0c802148fad516463507da5ca8bf1b78d9cb4ef72550931948acea0c48a78b",
    "download_status": "genuine PDF retained and opened in stated scope",
    "not_verified": []
  },
  {
    "key": "AKMW2002",
    "title": "Torification and factorization of birational maps",
    "url": "https://arxiv.org/pdf/math/9904135",
    "status": "verified in the specified scope",
    "opened_locators": [
      "arXiv:math/9904135v4: §1.2.4 and Lemma1.3.1, including its full short proof, p.6",
      "§5.1 analytic-extension remark"
    ],
    "uses": [
      "CDP C.2.UN.3 elimination of the inverse bimeromorphic map by smooth blowups off the common open subset"
    ],
    "verification_scope": "The elimination proof uses Chow flattening and principalization and expressly extends to analytic spaces. Its centres lie away from the common isomorphism locus. After shrinking the proper fibre tube, the vertical centres in this application are compact. The full weak-factorization theorem is not needed or claimed to have been audited.",
    "own_check": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), effort Pro, writing run; 17 November 2026 UTC",
    "web_refs": [
      "turn79view2",
      "turn80view4",
      "turn80view5",
      "turn81view0",
      "turn82view2"
    ],
    "local_pdf": "reference_downloads/cdp_audit/AKMW2002.pdf",
    "sha256": "55bbc2c58f29d4b9dbe965035f80f3844f6968eaf98076ac625132ac3b3977a5",
    "download_status": "genuine PDF retained and opened in stated scope",
    "not_verified": []
  },
  {
    "key": "Fujimoto1988Log",
    "title": "Logarithmic transformations on elliptic fiber spaces",
    "url": "https://scispace.com/pdf/logarithmic-transformations-on-elliptic-fiber-spaces-1uinrvp8jj.pdf",
    "status": "verified in the specified scope",
    "opened_locators": [
      "Original pp.91–92, definition of elliptic fibre space",
      "Theorem2.8 and full proof, pp.96–97; Corollary2.10",
      "§3 construction and Example3.4(1), pp.97–99"
    ],
    "uses": [
      "CDP C.2.UN.6 credit for Kodaira-dimension-one components",
      "CDP C.2.UN.6 explicit counterexample to Theorem2.8 and Corollary2.10 as printed"
    ],
    "verification_scope": "The printed definition imposes properness, smooth source and base, connected fibres and generically elliptic fibres, with no Kähler or projectivity hypothesis. The weighted Hopf threefold [a:b:c] modulo (qa,q^m b,q^m c), mapped by [a^m:b:c] to P2, meets all these hypotheses and has a multiplicity-m line with self-intersection1. The original proof treats the normalization of xi^m=s_D^m as a connected degree-m Stein cover, although that equation splits into m graphs. The assertion about divisibility and the resulting P2 corollary fail; no blanket refutation of the paper is intended. The original example already supplies a Kodaira-dimension-one component. Actual journal pages were opened through web retrieval; the failed direct download is not recorded as a PDF.",
    "own_check": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), effort Pro, writing run; 17 November 2026 UTC",
    "web_refs": [
      "turn79search12",
      "turn80view0",
      "turn81view3",
      "turn81view4",
      "turn81view5",
      "turn82view0"
    ],
    "local_pdf": null,
    "sha256": null,
    "download_status": "download failed",
    "not_verified": [],
    "aliases": [
      "Fujimoto1988Root"
    ]
  },
  {
    "key": "Nemethi1991Join",
    "title": "Generalized local and global Sebastiani–Thom type theorems",
    "url": "https://www.numdam.org/article/CM_1991__80_1_1_0.pdf",
    "status": "verified in the specified scope",
    "opened_locators": [
      "§2.1, TheoremL1 p.2; Example2.4(a) p.3"
    ],
    "uses": [
      "CDP A5.15 independent join-model check for nonisolated Hirzebruch germs"
    ],
    "verification_scope": "The statement expressly allows arbitrary analytic germs g and h. The auxiliary p=c+d has connected Milnor fibre, so its hypothesis is met. Example2.4(a) identifies the direct sum with the join. The manuscript separately computes the annulus components and wedge ranks and constructs an explicit spherical cycle, including reducible monomials. The full general proof of the theorem was not audited.",
    "own_check": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), effort Pro, writing run; 17 November 2026 UTC",
    "web_refs": [
      "turn96view0"
    ],
    "local_pdf": "reference_downloads/cdp_audit/Nemethi1991Join.pdf",
    "sha256": "4959e3e0f464ce45b52a4f3d883b374c8c6dc8b89552755d282d60a2d3351943",
    "download_status": "genuine PDF retained and opened in stated scope",
    "not_verified": []
  },
  {
    "key": "MPW2005Hirzebruch",
    "title": "The boundary of the Milnor fiber of Hirzebruch surface singularities",
    "url": "https://arxiv.org/pdf/math/0509451",
    "status": "verified in the specified scope",
    "opened_locators": [
      "arXiv:math/0509451v1: scope p.2; Theorem4.1 and comments pp.6–7",
      "Theorem4.2(1)–(3) p.7; rational Euler formula p.8; Lemma4.6 and complete proof p.11"
    ],
    "uses": [
      "CDP A5.15 independent Seifert boundary and intersection-rank check"
    ],
    "verification_scope": "The body permits 1≤k≤l, including equality, although the abstract uses a strict inequality. Its irreducibility hypothesis is gcd(m,k,l)=1 and is retained in the manuscript supplementary calculation. The genus, rational Euler number and lens-space specialization match after (m,k,l)=(a,b,c), with b and c exchanged if necessary. The elementary congruence proof of Lemma4.6 was read; the entire Seifert-foliation proof was not audited.",
    "own_check": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), effort Pro, writing run; 17 November 2026 UTC",
    "web_refs": [
      "turn96view1",
      "turn97view1",
      "turn97view2"
    ],
    "local_pdf": "reference_downloads/cdp_audit/MPW2005Hirzebruch.pdf",
    "sha256": "4c7ba34577af15e36f280d76c156380658bf46e9c36d7f8f1eb59d2a879f0299",
    "download_status": "genuine PDF retained and opened in stated scope",
    "not_verified": []
  },
  {
    "key": "vanStraten1987",
    "title": "Weakly Normal Surface Singularities and Their Improvements",
    "url": "https://download.uni-mainz.de/mathematik/Algebraische%20Geometrie/DvS-Publikationen/DvS_1987_weakly%20normal%20Surface%20Singularities%20and%20their%20improvements.pdf",
    "status": "verified in the specified scope",
    "opened_locators": [
      "§§2.2.2–2.2.5, printed pp.60–61, original PDF pages63–64"
    ],
    "uses": [
      "CDP C2.CR2 analytic canonical-module defect and length comparison"
    ],
    "verification_scope": "Opened proper analytic duality, the proper bimeromorphic vanishing theorem for smooth source, and the normal Cohen–Macaulay isolated-singularity canonical-form defect. These exactly give length(ω_T/pi_*ω_Z)=length(R¹pi_*O_Z). The source attributes duality to RRV and vanishing to Grauert–Riemenschneider; this record is an opening of the thesis, not a claim that those two original papers have both been opened.",
    "own_check": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), effort Pro, writing run; 17 November 2026 UTC",
    "web_refs": [
      "turn97view0",
      "turn100view1",
      "turn100view2",
      "turn100view3",
      "turn105view0"
    ],
    "local_pdf": "reference_downloads/cdp_audit/vanStraten1987.pdf",
    "sha256": "583d6e337304958cb3dfb6519cb8c82901928667ccacfeae74d0e03a19d1e906",
    "download_status": "genuine PDF retained and opened in stated scope",
    "not_verified": []
  },
  {
    "key": "Milnor1968",
    "title": "Singular Points of Complex Hypersurfaces",
    "url": "https://djvu.online/file/kCFrJq27uCPRi",
    "status": "verified in the specified scope",
    "opened_locators": [
      "Lemma6.1 and complete proof pp.55–56",
      "AppendixB LemmasB1–B3 and positivity proof pp.111–114"
    ],
    "uses": [
      "CDP A5.17 Milnor boundary transversality and morsification of isolated critical points"
    ],
    "verification_scope": "Read the actual book transcription at the specified pages. The boundary submersion argument uses curve selection; the gradient perturbation creates a nonempty cluster of nondegenerate critical points by positivity of local degree. The manuscript supplies its own proper boundary transport into the global torus and the sphere self-intersection. No downloaded book file is claimed.",
    "own_check": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), effort Pro, writing run; 17 November 2026 UTC",
    "web_refs": [
      "turn100view0",
      "turn103view1",
      "turn103view2",
      "turn105view1"
    ],
    "local_pdf": null,
    "sha256": null,
    "download_status": "not attempted in this checkpoint",
    "not_verified": []
  },
  {
    "key": "Steenbrink1999",
    "title": "Cup products and mixed Hodge structures",
    "url": "https://arxiv.org/pdf/math/9902134",
    "status": "verified in the specified scope",
    "opened_locators": [
      "§3 Lemma1, Theorem1 and full residue proof, Corollaries1–2, pp.5–7",
      "§4 equation(3) and excision comparison, pp.8–9"
    ],
    "uses": [
      "CDP C2.MH1 restricted logarithmic complex and actual support-to-restriction arrow"
    ],
    "verification_scope": "The source starts with a complete smooth algebraic ambient space. The matched local proof is holomorphic-coordinate residue algebra; its graded terms are de Rham complexes of intersections with the stratum. MH1 explicitly extends that construction to an analytic neighbourhood whose compact strata are projective and proves its support weight bound by Thom/Gysin complexes. The global complete-algebraic theorem is not cited as if its ambient hypothesis were absent.",
    "own_check": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), effort Pro, writing run; 17 November 2026 UTC",
    "web_refs": [
      "turn108view0",
      "turn110view0",
      "turn112view0",
      "turn112view1",
      "turn114view0"
    ],
    "local_pdf": "reference_downloads/cdp_audit/Steenbrink1999.pdf",
    "sha256": "70f48cb73d5df029f9d0434618191d21730aa021aa5dc3be0e8a93ecb5286cc9",
    "download_status": "genuine PDF retained and opened in stated scope",
    "not_verified": []
  },
  {
    "key": "Rossi2017",
    "title": "A small and non-simple geometric transition",
    "url": "https://arxiv.org/pdf/1211.6329",
    "status": "verified in the specified scope",
    "opened_locators": [
      "arXiv:1211.6329v3: §3 Proposition4, construction and local resolution calculation pp.10–11",
      "Remark5 Hodge-number comparison p.20"
    ],
    "uses": [
      "CDP C2.UN8 credit for Namikawa cuspidal self-product, graph blowups and known ambient Hodge numbers"
    ],
    "verification_scope": "Opened the original double graph-blowup construction and two-projective-line exceptional chain, plus h11=21 and h21=3. These construction and Hodge-number claims are known. The manuscript separately derives the integral central-fibre groups, generic Picard ranks and exact obstruction to a nonzero local character. The later local-deformation assertions in Rossi are not used or audited here.",
    "own_check": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), effort Pro, writing run; 17 November 2026 UTC",
    "web_refs": [
      "turn108view1",
      "turn110view1",
      "turn110view2",
      "turn112view2",
      "turn114view1"
    ],
    "local_pdf": "reference_downloads/cdp_audit/Rossi2017.pdf",
    "sha256": "000ad2e03b115a872c1d8ab4283e72c81c25216dd5376e549ceedf3e3e1c84bb",
    "download_status": "genuine PDF retained and opened in stated scope",
    "not_verified": []
  },
  {
    "key": "Dloussky2006",
    "title": "On surfaces of class VII_0^+ with numerically anticanonical divisor",
    "url": "https://arxiv.org/pdf/math/0406387",
    "status": "verified in the specified scope",
    "opened_locators": [
      "arXiv:math/0406387v3: Theorem0.2 p.2; Lemma2.22 and following paragraph p.15",
      "Corollary2.25 and proof pp.16–17; Proposition2.27 and complete proof pp.17–19; Proposition2.29 and proof p.19",
      "Theorem2.38 and its proof pp.24–25, with the preceding square-zero Enoki/Inoue case"
    ],
    "uses": [
      "CDP VII1 torsion-anticanonical support and rational-curve configuration",
      "CDP UN17/19 and subsequent class-VII recognition restricted to surfaces with the required anticanonical divisor"
    ],
    "verification_scope": "Matched the numerically anticanonical hypothesis, the connected cycle-with-trees or Inoue alternatives, and the prohibition of isolated tree support. Theorem2.38 itself excludes square-zero divisors; the immediately preceding paragraph handles that separate Enoki case and characterizes the anticanonical parabolic Inoue case. VII1 independently uses positivity of the Gauduchon degree to force coefficient one on its square-zero cycle. The complete proofs of the listed elementary support statements were read; the entire classification proof through every earlier lemma was not audited.",
    "own_check": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), effort Pro, writing run; 17 November 2026 UTC",
    "web_refs": [
      "turn137view0",
      "turn139view2",
      "turn139view3",
      "turn139view4",
      "turn139view5",
      "turn139view6"
    ],
    "local_pdf": "reference_downloads/cdp_audit/Dloussky2006.pdf",
    "sha256": "f461b07b3bb60a6c1433172a5514fa6e90a41e43dac6f23396a4713d99f5c3f9",
    "download_status": "genuine PDF retained and opened in stated scope",
    "not_verified": []
  },
  {
    "key": "DOT2003",
    "title": "Class VII_0 surfaces with b_2 curves",
    "url": "https://www.jstage.jst.go.jp/article/tmj/55/2/55_2_283/_pdf/-char/en",
    "status": "verified in the specified scope",
    "opened_locators": [
      "Introduction p.283; §1 pp.284–285 including Lemma1.1 and its proof",
      "§3 p.296, actual divisor-neighbourhood and fundamental-group identifications"
    ],
    "uses": [
      "CDP VII1 rational-curve count and intermediate cycle-with-trees configuration",
      "Class-VII divisor comparisons retaining the actual neighbourhood maps"
    ],
    "verification_scope": "The original publisher PDF states at most b2 rational curves for minimal class VII surfaces and exactly b2 for surfaces with a global spherical shell. Its intermediate configuration has one cycle with attached trees; the opened page296 identifies the actual inclusion-induced fundamental groups. The manuscript supplies the point-blowup transfer and does not invoke a classification of all class VII surfaces without an anticanonical divisor. The full global-spherical-shell theorem proof was not audited.",
    "own_check": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), effort Pro, writing run; 17 November 2026 UTC",
    "web_refs": [
      "turn137view1",
      "turn139view1"
    ],
    "local_pdf": "reference_downloads/cdp_audit/DOT2003.pdf",
    "sha256": "b1b66ca42a4765dc3242dd68342cb62d414f45527486932fe425b6a8fe8cc962",
    "download_status": "genuine PDF retained and opened in stated scope",
    "not_verified": []
  },
  {
    "key": "KamenovaTori",
    "title": "Degenerations of 2-Dimensional Tori",
    "url": "https://www.math.stonybrook.edu/~kamenova/homepage_files/degen.pdf",
    "status": "verified in the specified scope",
    "opened_locators": [
      "All four author-hosted pages, especially Theorem3.1 and proof pp.2–3"
    ],
    "uses": [
      "CDP UN65 and IRR1 comparison with the known Kähler semistable classification"
    ],
    "verification_scope": "Read the entire four-page manuscript. It assumes a Kähler total space and trivial total canonical line. Its list includes an elliptic-ruled path; CDP supplies a separate residue and finite-trace exclusion of that path in its exact setting. The source is used for attribution and comparison, not to remove its Kähler hypothesis or to establish the new analytic classification. No publication year is stated in the source or inferred here.",
    "own_check": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), effort Pro, writing run; 17 November 2026 UTC",
    "web_refs": [
      "turn137view2",
      "turn139view0"
    ],
    "local_pdf": "reference_downloads/cdp_audit/KamenovaTori.pdf",
    "sha256": "8cd2ddcef5c77b97f6d1b648a73191734696dceb1c9281c09342413596cfbd0b",
    "download_status": "genuine PDF retained and opened in stated scope",
    "not_verified": []
  },
  {
    "key": "HuybrechtsK3Draft",
    "title": "Lectures on K3 Surfaces",
    "url": "https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf",
    "status": "verified in the specified scope",
    "opened_locators": [
      "Author-hosted prepublication draft, Chapter1 Example1.3(iii), pp.8–9, including both quotient/blowup maps and canonical/cohomology calculation"
    ],
    "uses": [
      "CDP UN13 attribution for the classical Kummer construction"
    ],
    "verification_scope": "Opened the exact construction of the resolution of A/{±1}, the alternative blow-up-then-quotient map, and the form and trace calculation making the result K3. UN13 retains its independent threefold quotient charts, support cohomology and vertical-refinement proof. The rest of the book is not recorded as read.",
    "own_check": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), effort Pro, writing run; 17 November 2026 UTC",
    "web_refs": [
      "turn137view3"
    ],
    "local_pdf": "reference_downloads/cdp_audit/HuybrechtsK3Draft.pdf",
    "sha256": "59da72d5807fd05d08ce28ceaf30a030cfc7e52b92e27778d824ac86cb1dd287",
    "download_status": "genuine PDF retained and opened in stated scope",
    "not_verified": []
  },
  {
    "key": "MerleTeissier1977",
    "title": "Conditions d’adjonction, d’après Du Val",
    "url": "https://www.numdam.org/item/SSS_1976-1977____A16_0.pdf",
    "status": "verified in the specified scope",
    "opened_locators": [
      "Exposé14, §2 Theorem2.1.1 and complete toric determinant proof; Corollary2.1.3 (PDF pages14–16, visually inspected)"
    ],
    "uses": [
      "CDP D4.1 and RAT6 geometric genera of cubic ADE suspensions",
      "CDP RAT8 cusp-plus-two-branches and four-transverse-branches Newton computations"
    ],
    "verification_scope": "The theorem requires an isolated hypersurface singularity nondegenerate for its Newton polyhedron. The original proof identifies the adjunction ideal by strict interior membership after multiplying by every coordinate; Corollary2.1.3 counts strictly positive lattice points outside that interior, so the inequality in the manuscript is correctly non-strict. The ADE and two additional equations have their face nondegeneracy checked in the proof. The determinant proof and displayed hypotheses were read; the full background theory of toric resolution is not claimed as independently reproved.",
    "own_check": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), effort Pro, writing run; 17 November 2026 UTC",
    "web_refs": [
      "turn145view0"
    ],
    "local_pdf": "reference_downloads/cdp_audit/MerleTeissier1977.pdf",
    "sha256": "52afab559bd2842082f35d86f495f2ef378a1eb51fcb99bcbda09207f7843da3",
    "download_status": "genuine PDF retained and opened in stated scope",
    "not_verified": []
  },
  {
    "key": "Steenbrink1989Spectrum",
    "title": "The spectrum of hypersurface singularities",
    "url": "https://www.numdam.org/article/AST_1989__179-180__163_0.pdf",
    "status": "verified in the specified scope",
    "opened_locators": [
      "§1, printed pp.165–167: weighted Jacobian-monomial formula, Thom–Sebastiani convolution theorem and geometric-genus interval"
    ],
    "uses": [
      "CDP D4.1 and RAT6 weighted suspension monodromy, geometric genus and link Betti numbers"
    ],
    "verification_scope": "Opened the original scan at all three pages. The monomial formula has spectral value sum((a_i+1)w_i)-1; the geometric-genus interval is(-1,0], and convolution adds one. The uses here are isolated weighted homogeneous germs, hence have semisimple monodromy; the manuscript separately explains the Milnor-fibre variation and exceptional-intersection comparisons giving link b1. The general nonisolated spectrum theorem is not needed or independently audited.",
    "own_check": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), effort Pro, writing run; 17 November 2026 UTC",
    "web_refs": [
      "turn145view1"
    ],
    "local_pdf": "reference_downloads/cdp_audit/Steenbrink1989Spectrum.pdf",
    "sha256": "78b930f354b7fc8859e0384b203211a453ab53ced6df1879cec2bd04ae3b46eb",
    "download_status": "genuine PDF retained and opened in stated scope",
    "not_verified": []
  },
  {
    "key": "Arnold1976NormalForms",
    "title": "Local normal forms of functions",
    "url": "https://webhomes.maths.ed.ac.uk/~v1ranick/papers/arnold15.pdf",
    "status": "verified in the specified scope",
    "opened_locators": [
      "Analytic equivalence and normal-form conventions pp.87–88; §1 I.1.0 simple A–D–E list p.92",
      "§2 notation p.100 and determinator items2–9 p.101, including E6/E7/E8 weighted initial forms"
    ],
    "uses": [
      "CDP RAT6 analytic normal forms for all reduced plane germs of delta at most five"
    ],
    "verification_scope": "Matched actual analytic-equivalence conventions and the zero-modality A–D–E forms. RAT6 supplies the exhaustive low-delta branch/Puiseux case analysis; the opened determinator gives the analytic reduction of its weighted initial forms. This is not an attribution of the entire low-delta argument to the source, nor a claim to have checked every proof in the article.",
    "own_check": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), effort Pro, writing run; 17 November 2026 UTC",
    "web_refs": [
      "turn145view2"
    ],
    "local_pdf": "reference_downloads/cdp_audit/Arnold1976NormalForms.pdf",
    "sha256": "1d75961a44caa5dba08a5729fcf612b1c94a479df02e64bcb1bbf8f3e32ebee8",
    "download_status": "genuine PDF retained and opened in stated scope",
    "not_verified": []
  },
  {
    "key": "RRV71",
    "title": "Dualité relative en géométrie analytique complexe",
    "url": "https://gdz.sub.uni-goettingen.de/id/PPN356556735_0013",
    "status": "verified in the specified scope",
    "opened_locators": [
      "Introduction equation(1), original p.261; §1 proper-duality trace quasi-isomorphism p.264",
      "§2 relative trace, pp.265–268; Proposition2.1 continuity statement p.266"
    ],
    "uses": [
      "PUSH E3.1 analytic relative duality for proper flat Gorenstein surface families over curve charts",
      "CDP CR2 proper analytic duality for a resolution of a normal Cohen–Macaulay surface"
    ],
    "verification_scope": "Opened the original journal scan through its public GDZ IIIF manifest and visually checked pp.261,264,265,266 after reading the text of §§1–2. The introduction explicitly asserts that equation(1) is an isomorphism for a proper morphism of complex analytic spaces; §1 writes the required Rf_*RHom(F,K_X•)→RHom(Rf_*F,K_Y•). No projectivity or Kähler hypothesis occurs. For E3.1 the smooth total space and base give absolute dualizing complexes ω_Y[3] and ω_U[1]; projection and cancellation give Rp_*ω_Y/U[2]≅RHom(Rp_*O_Y,O_U), and the independently checked locally free cohomology gives the degree−2 edge. Proposition2.1 is the continuity step for the trace construction, not a theorem numbered as the general duality result. The article’s remaining functional-analytic proofs in §§3–4 were not audited.",
    "own_check": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), effort Pro, writing run; 17 November 2026 UTC",
    "web_refs": [
      "turn123view0",
      "turn125view0"
    ],
    "local_pdf": null,
    "sha256": null,
    "download_status": "original journal pages261–268 downloaded; inspected in the specified scope",
    "not_verified": [
      "Complete functional-analytic proofs of §§3–4 were not audited."
    ],
    "aliases": [
      "RRV71push",
      "RamisRugetVerdier1971"
    ],
    "original_page_files": [
      {
        "page": "261",
        "url": "https://images.p.sub.uni-goettingen.de/iiif/image/gdz:PPN356556735_0013:00000275/full/1800,/0/default.jpg",
        "path": "reference_downloads/cdp_audit/RRV71_p261.jpg",
        "sha256": "6986f780a581fd6efc07462a77c50c67fb0422fd2e836a81922fd738fb12ca81",
        "bytes": 830095
      },
      {
        "page": "262",
        "url": "https://images.p.sub.uni-goettingen.de/iiif/image/gdz:PPN356556735_0013:00000276/full/1800,/0/default.jpg",
        "path": "reference_downloads/cdp_audit/RRV71_p262.jpg",
        "sha256": "c82972927ab912874716d4ea8bcd7809adfd3ee9a00f76155cbc1fd6288f687a",
        "bytes": 836349
      },
      {
        "page": "263",
        "url": "https://images.p.sub.uni-goettingen.de/iiif/image/gdz:PPN356556735_0013:00000277/full/1800,/0/default.jpg",
        "path": "reference_downloads/cdp_audit/RRV71_p263.jpg",
        "sha256": "591e6ac8c06854c9e18ee56289912dafbf98df87dcac36439702c546ce103e7c",
        "bytes": 890538
      },
      {
        "page": "264",
        "url": "https://images.p.sub.uni-goettingen.de/iiif/image/gdz:PPN356556735_0013:00000278/full/1800,/0/default.jpg",
        "path": "reference_downloads/cdp_audit/RRV71_p264.jpg",
        "sha256": "fc94bb88f92e0dd20afa7e4a5751c0d10682adff81000758eb846dc786c4eb19",
        "bytes": 733095
      },
      {
        "page": "265",
        "url": "https://images.p.sub.uni-goettingen.de/iiif/image/gdz:PPN356556735_0013:00000279/full/1800,/0/default.jpg",
        "path": "reference_downloads/cdp_audit/RRV71_p265.jpg",
        "sha256": "a6b7d205128fa94a9c64493199fa8f9a6f033ba94d9f37833d50ed2c2b9e97f3",
        "bytes": 837271
      },
      {
        "page": "266",
        "url": "https://images.p.sub.uni-goettingen.de/iiif/image/gdz:PPN356556735_0013:00000280/full/1800,/0/default.jpg",
        "path": "reference_downloads/cdp_audit/RRV71_p266.jpg",
        "sha256": "1319c20a09ddf5b7232fc0bf5598ab2c432c49d011cd3406b8cec1c744e2266a",
        "bytes": 728476
      },
      {
        "page": "267",
        "url": "https://images.p.sub.uni-goettingen.de/iiif/image/gdz:PPN356556735_0013:00000281/full/1800,/0/default.jpg",
        "path": "reference_downloads/cdp_audit/RRV71_p267.jpg",
        "sha256": "46abb6ca6005298239af3c3e63e7541351c3c000979daa513456704ffdb8a0b9",
        "bytes": 826516
      },
      {
        "page": "268",
        "url": "https://images.p.sub.uni-goettingen.de/iiif/image/gdz:PPN356556735_0013:00000282/full/1800,/0/default.jpg",
        "path": "reference_downloads/cdp_audit/RRV71_p268.jpg",
        "sha256": "0d293523c4f2924e6c0eb770dbda585add939be6839cba41ae4c959350449700",
        "bytes": 708212
      }
    ],
    "manifest_url": "https://manifests.sub.uni-goettingen.de/iiif/presentation/PPN356556735_0013/manifest?version=8b7f2484",
    "manifest_sha256": "be2eb6eec6bc73771d2c5b3f1d868173ff635eba0b40e6320860f1f42e2d40cc"
  },
  {
    "key": "Peters2021",
    "title": "On complex surfaces with definite intersection form",
    "url": "https://nyjm.albany.edu/j/2021/27-32p.pdf",
    "status": "verified in the specified scope",
    "opened_locators": [
      "Published pp842–843, Noether formula(2), Proposition2.1 and complete classification table Theorem2.2"
    ],
    "uses": [
      "CDP A5.2 negative holomorphic Euler classification",
      "CDP NC4 non-Kähler normalization invariants",
      "CDP C3.1 preliminary surface list"
    ],
    "verification_scope": "Original published table opened. All Chern numbers refer to minimal models; blowing up preserves coherent Euler and adds one to topological Euler. This supplies the stated numerical branches, not a proof of the full Enriques–Kodaira classification.",
    "own_check": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), effort Pro, writing run; 17 November 2026 UTC",
    "web_refs": [
      "turn158view0",
      "turn162view0"
    ],
    "local_pdf": "reference_downloads/cdp_audit/Peters2021.pdf",
    "sha256": "a503b2b1810caba753f843ce781d4c10dd29ea235c7955df616f7c05c0f4527c",
    "download_status": "genuine PDF retained and opened in stated scope",
    "not_verified": []
  },
  {
    "key": "Peters1990",
    "title": "Compact Complex Surfaces",
    "url": "https://cpeters1.win.tue.nl/ConfsAndSchools/Canada/surface.pdf",
    "status": "verified in the specified scope",
    "opened_locators": [
      "Front matter: Canadian Mathematical Society Summer Meeting, June1990",
      "Theorem1.1 p6; Theorem3.1 pp9–10 and surrounding definitions"
    ],
    "uses": [
      "CDP C3.1 full preliminary classification",
      "CDP C3.7 even-b1 Kähler criterion"
    ],
    "verification_scope": "Author-hosted lecture text opened. The compact complex surface hypotheses match. The classification theorem is imported as known; its full historical proof is not asserted to have been audited. Publication details beyond the supplied front matter are not inferred.",
    "own_check": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), effort Pro, writing run; 17 November 2026 UTC",
    "web_refs": [
      "turn158view2",
      "turn161view5",
      "turn163view1"
    ],
    "local_pdf": "reference_downloads/cdp_audit/Peters1990.pdf",
    "sha256": "51f9c99621b3819aa85894a8cdee4a528b0894364fc22b40a651f1bae55ceed3",
    "download_status": "genuine PDF retained and opened in stated scope",
    "not_verified": []
  },
  {
    "key": "BMS2012",
    "title": "Three manifold groups, Kähler groups and complex surfaces",
    "url": "https://mathweb.tifr.res.in/~mahan/kahler3fld.pdf",
    "status": "verified in the specified scope",
    "opened_locators": [
      "Author PDF dated27October2011, Theorem3.2 p16",
      "Opening of §3.3 pp17–18"
    ],
    "uses": [
      "CDP NC4 minimal non-Kähler elliptic Euler zero",
      "CDP C3.12 elliptic/classVII alternatives and orbifold quotient comparison"
    ],
    "verification_scope": "Matched only the odd-b1 elliptic-or-classVII classification, Euler-zero minimal elliptic conclusion and fibration group sequence. The paper’s unrestricted Hopf cyclic-group wording is not used; secondary Hopf groups need not be cyclic. No unrelated three-manifold classification argument is imported.",
    "own_check": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), effort Pro, writing run; 17 November 2026 UTC",
    "web_refs": [
      "turn158view1",
      "turn161view2",
      "turn162view2"
    ],
    "local_pdf": "reference_downloads/cdp_audit/BMS2012.pdf",
    "sha256": "1bfc9f90846000474ae1c6377850513e2ce85a74942b5f8fcc48e0a08a6addb6",
    "download_status": "genuine PDF retained and opened in stated scope",
    "not_verified": [
      "Do not use this record to assert that every Hopf surface has infinite cyclic fundamental group."
    ]
  },
  {
    "key": "Teleman2008",
    "title": "Gauge theoretical methods in the classification of non-Kählerian surfaces",
    "url": "https://www.i2m.univ-amu.fr/perso/andrei.teleman/documents/postnikov.pdf",
    "status": "verified in the specified scope",
    "opened_locators": [
      "Author PDF dated3April2008, introduction pp1–2, especially p2 classVII b2=0 statement"
    ],
    "uses": [
      "CDP C3.1 Hopf/Inoue classification; VII branch"
    ],
    "verification_scope": "The exact minimal classVII b2=0 statement and definition of Hopf/Inoue surfaces opened. The survey credits Bogomolov and the completed Teleman and Li–Yau–Zheng proofs. Those complete classification proofs were not rechecked here.",
    "own_check": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), effort Pro, writing run; 17 November 2026 UTC",
    "web_refs": [
      "turn158view3",
      "turn161view6"
    ],
    "local_pdf": "reference_downloads/cdp_audit/Teleman2008.pdf",
    "sha256": "526195163b35b80f45c0df7e342034653893b90e7c050f8ed590a569e6fd0cdd",
    "download_status": "genuine PDF retained and opened in stated scope",
    "not_verified": []
  },
  {
    "key": "BBK2019",
    "title": "Classifying VII0 surfaces with b2=0 via group theory",
    "url": "https://arxiv.org/pdf/1709.00062",
    "status": "verified in the specified scope",
    "opened_locators": [
      "arXiv1709.00062v3,20May2019, Theorem1 p1"
    ],
    "uses": [
      "CDP C3.1 precise finite-etale-cover scope"
    ],
    "verification_scope": "The original theorem gives a Hopf or Inoue finite etale cover. This qualification is retained in the fibre exclusions; the article’s complete group-theoretic proof is not claimed checked.",
    "own_check": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), effort Pro, writing run; 17 November 2026 UTC",
    "web_refs": [
      "turn158view4"
    ],
    "local_pdf": "reference_downloads/cdp_audit/BBK2019.pdf",
    "sha256": "390eeef64b8bcc1c6fc0505e1748443e08c1677d693e749c6b9ea85312c52af7",
    "download_status": "genuine PDF retained and opened in stated scope",
    "not_verified": []
  },
  {
    "key": "Kawai1969",
    "title": "On compact complex analytic manifolds of complex dimension3, II",
    "url": "https://www.jstage.jst.go.jp/article/jmath1948/21/4/21_4_604/_pdf/-char/en",
    "status": "verified in the specified scope",
    "opened_locators": [
      "Published pp604–605 Theorem1 and Proposition2",
      "Proposition2 entire relative period, translation-gluing and compactification proof pp605–608",
      "Following corollary p608 read to separate it from the imported construction"
    ],
    "uses": [
      "CDP C3.7 relative Albanese map for bielliptic fibres"
    ],
    "verification_scope": "Full Proposition2 proof read in the original PDF. The source’s selected divisor need not be invariant: the CDP proof uses its finite orbit sum, after resolution, and takes the image of the induced projective map. This preserves the Albanese curve and supplies the necessary linearization. The later multiple-fibre corollary is not used.",
    "own_check": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), effort Pro, writing run; 17 November 2026 UTC",
    "web_refs": [
      "turn163view0"
    ],
    "local_pdf": "reference_downloads/cdp_audit/Kawai1969.pdf",
    "sha256": "ab7430d51afbcc6aaa471266d9a743ca0f2be447c23967ae1c4fe27b417ca826",
    "download_status": "genuine PDF retained and opened in stated scope",
    "not_verified": []
  },
  {
    "key": "SS2002",
    "title": "Irreducible degenerations of primary Kodaira surfaces",
    "url": "https://arxiv.org/pdf/math/0001077",
    "status": "verified in the specified scope",
    "opened_locators": [
      "arXivmath/0001077v2, §1 pp2–3: degree, intrinsic Picard quotient and (d,j,alpha) coordinates",
      "Definition2.1 and Propositions2.4–2.6 with full proofs pp4–6",
      "Proposition3.1 with full contraction-normal-form proof pp6–7",
      "Proposition4.1 with full proof p13"
    ],
    "uses": [
      "CDP C3.8 Hopf normal forms",
      "CDP C3.9–10 intrinsic primary-Kodaira moduli coordinate",
      "CDP A4.5 normalization cases and translation gluing"
    ],
    "verification_scope": "The admissibility definition requires irreducible normal crossings, d-semistability and trivial dualizing line, without assuming an existing Kodaira smoothing. The normalized surface cases, diagonal Hopf criterion and ruled translation criterion match these hypotheses. In §1 the positive-degree class fixes the inversion ambiguity in C*.",
    "own_check": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), effort Pro, writing run; 17 November 2026 UTC",
    "web_refs": [
      "turn161view0",
      "turn162view3",
      "turn179view1",
      "turn179view2",
      "turn179view3"
    ],
    "local_pdf": "reference_downloads/cdp_audit/SS2002.pdf",
    "sha256": "931d4ed7ed12e9262c2f073b40f25343a5237013cf59d3117bef13013bb63e7e",
    "download_status": "genuine PDF retained and opened in stated scope",
    "not_verified": []
  },
  {
    "key": "Borcea1984",
    "title": "Moduli for Kodaira surfaces",
    "url": "https://www.numdam.org/article/CM_1984__52_3_373_0.pdf",
    "status": "verified in the specified scope",
    "opened_locators": [
      "Introduction pp373–374, fixed differentiable type",
      "§3 equations(9)–(12), pp376–377; Remark1 complete holomorphic period family p377",
      "Theorem3 and proof pp378–379; Theorem4 and Remark2 p380"
    ],
    "uses": [
      "CDP C3.9–10 primary-Kodaira Picard/moduli comparison and actual local product",
      "CDP D1.12 invariant-form cup product"
    ],
    "verification_scope": "Opened the complete-family statement and its explicit quotient construction, the period-line classification and the product C times punctured-disc moduli. The C3.10 local product follows by a holomorphic map into a countable integral-cohomology orbit; central shear effects are computed independently in CDP.",
    "own_check": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), effort Pro, writing run; 17 November 2026 UTC",
    "web_refs": [
      "turn164view1",
      "turn175view1",
      "turn176view1",
      "turn177view2"
    ],
    "local_pdf": "reference_downloads/cdp_audit/Borcea1984.pdf",
    "sha256": "ea232736beef772c958b6e661fffb323a691f0a85fc0b090b43dbc2d495303a7",
    "download_status": "genuine PDF retained and opened in stated scope",
    "not_verified": []
  },
  {
    "key": "Steenbrink1976",
    "title": "Limits of Hodge structures",
    "url": "https://www.academia.edu/47027671/Limits_of_Hodge_structures",
    "status": "verified in the specified scope",
    "opened_locators": [
      "Original authored scan transcription, §2.1 p234",
      "Theorem2.18 and full proof pp237–238; §2.19, Proposition2.20 and proof, Theorem2.21 pp238–239"
    ],
    "uses": [
      "CDP D2.3 logarithmic period comparison with arbitrary multiplicities",
      "CDP C3.10 holomorphic extension of a constant H2 frame and projection to R2O"
    ],
    "verification_scope": "Section2 assumes a proper holomorphic map, smooth connected total space, smooth punctured family and normal-crossing support. It does not assume Kählerness. The relative logarithmic complex is locally free in direct hypercohomology; residues lie in[0,1) and exponentiate to monodromy. Thus identity monodromy forces zero residue. Later mixed-Hodge assertions have additional hypotheses and are not imported by this record.",
    "own_check": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), effort Pro, writing run; 17 November 2026 UTC",
    "web_refs": [
      "turn164view2",
      "turn175view2",
      "turn176view0",
      "turn177view3"
    ],
    "local_pdf": null,
    "sha256": null,
    "download_status": "not attempted in this checkpoint",
    "not_verified": [
      "No unrestricted non-Kähler global invariant-cycle or Hodge-degeneration theorem is claimed.",
      "The complete proofs of all preliminary local lemmas in §§1–2 were not newly rederived in this check."
    ]
  },
  {
    "key": "Inoue1974",
    "title": "On surfaces of class VII0",
    "url": "https://www.digizeitschriften.de/download/pdf/356556735_0024/log19.pdf",
    "status": "verified in the specified scope",
    "opened_locators": [
      "Original indexed journal scan, Propositions2 and5 and full proofs pp274–275,280",
      "Propositions3–4 and full proofs pp277–279; explicit transition formula in Proposition4"
    ],
    "uses": [
      "CDP C3.12 rigidity and complete S+ family with constant first-coordinate affine transformations"
    ],
    "verification_scope": "The original propositions establish rigidity for SM and S− and a locally complete one-parameter S+ family. Its parameter changes only z; w_i=alpha^m w_j+a has constant real-affine coefficients. The full local-completeness Kodaira–Spencer argument was read. The remaining classification §§5–9 is outside this check.",
    "own_check": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), effort Pro, writing run; 17 November 2026 UTC",
    "web_refs": [
      "turn175view0",
      "turn176view2",
      "turn176view3",
      "turn176view4",
      "turn177view0",
      "turn177view1"
    ],
    "local_pdf": null,
    "sha256": null,
    "download_status": "not attempted in this checkpoint",
    "not_verified": []
  },
  {
    "key": "Kodaira1963II",
    "title": "On compact analytic surfaces: II",
    "url": "https://it.scribd.com/document/480913137/kodaira1963-II",
    "status": "verified in the specified scope",
    "opened_locators": [
      "Public transcription of original Annals77(1963)563–626 scan",
      "Definition and relative-minimality hypothesis pp563–564; Theorem6.2 pp564–566, proof opening pp566–568",
      "TableI and Theorem9.1 p604; group-law formulas on p605"
    ],
    "uses": [
      "CDP UN20/22/29/33/66/67 elliptic-fibre types and identity-monodromy comparisons"
    ],
    "verification_scope": "Opened the original theorem, including its no-exceptional-fibre-curve hypothesis. The source allows analytic elliptic surfaces over compact curves, not just projective total spaces. Fibre types and multiplicities were read. The TableI OCR is partly damaged; exact individual monodromy matrices are not certified from that transcription alone.",
    "own_check": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), effort Pro, writing run; 17 November 2026 UTC",
    "web_refs": [
      "turn174view0",
      "turn175view3"
    ],
    "local_pdf": null,
    "sha256": null,
    "download_status": "not attempted in this checkpoint",
    "not_verified": [
      "Exact individual TableI matrix entries require visual verification; the present record does not certify those OCR-damaged entries."
    ]
  },
  {
    "key": "Brunella1999Forms",
    "title": "On holomorphic forms on compact complex threefolds",
    "url": "https://ems.press/content/serial-article-files/42850",
    "status": "verified in the specified scope",
    "opened_locators": [
      "Original published PDF title page p642",
      "§2 pp648–650: standing a(M)=1 and nonclosed-global-one-form hypotheses; Lemmas4/5 and full proofs; Proposition2 conclusion"
    ],
    "uses": [
      "CDP records/D_notes.md relative-Albanese comparison preceding the completed C3.10 proof",
      "Clarifies why a compactified relative Albanese cannot be imported for primary Kodaira fibres"
    ],
    "verification_scope": "The original author is Marco Brunella; the EMS landing-page attribution to Luis Paris is erroneous and is not used. Lemma5 constructs the elliptic relative Albanese over the smooth open base and expressly permits a noncompactifiable quotient. Its boundary-integral proof shows closedness of an already existing global one-form via a uniform positive lower bound on areas of compact curves. It does not construct a global one-form or compactify the quotient. The final CDP C3.10 proof uses Borcea and logarithmic periods instead, so this citation is a methodological comparison, not a dependency of that completed theorem. This is the CMH74(1999)642–656 paper, distinct from Brunella’s Doc.Math.4(1999)451–462 sphere paper.",
    "own_check": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), effort Pro, writing run; 17 November 2026 UTC",
    "web_refs": [
      "turn188view0",
      "turn189view0"
    ],
    "local_pdf": "reference_downloads/cdp_audit/Brunella1999Forms.pdf",
    "sha256": "d7ac8b414e79a14427fd14d14049aece467c80d8a5ff30754b76520614d8f14b",
    "download_status": "genuine PDF retained and opened in stated scope",
    "not_verified": [
      "No compactifiability assertion for the relative Albanese is supported.",
      "The remaining integrable-form and foliation theorems of §§1/3 are outside this specified check."
    ],
    "aliases": [
      "Brunella1999"
    ]
  },
  {
    "key": "KhaledTeleman2026",
    "title": "On the classification of Inoue surfaces",
    "url": "https://arxiv.org/pdf/2406.15158",
    "status": "verified in the specified scope",
    "opened_locators": [
      "arXiv2406.15158v4,13July2026, §§2.1–2.3 pp6–11",
      "Definitions2.5/2.16/2.25, Remarks2.7–2.8/2.18–2.21/2.27",
      "TypeIII double-cover statement p14"
    ],
    "uses": [
      "CDP C3.12 exact surface-group presentations, affine first coordinates and finite-cover type comparisons",
      "CDP A4.9 local-system eigenvalue assertions"
    ],
    "verification_scope": "Read the original affine generators and complete stated group normal forms. TypeI has Z^3 semidirect Z with real eigenvalue alpha>1; typeII has the Heisenberg subgroup and alpha,alpha^-1 on its rank-two quotient; typeIII has alpha,-alpha^-1 and inverts the central generator, with a typeII double cover. Every first coordinate is alpha^m*w+a with a real. This record does not import the article’s later full biholomorphism classification or claim its entire proof audited.",
    "own_check": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), effort Pro, writing run; 17 November 2026 UTC",
    "web_refs": [
      "turn164view3",
      "turn172view3"
    ],
    "local_pdf": "reference_downloads/cdp_audit/KhaledTeleman2026.pdf",
    "sha256": "a02fcbbe234e2065d796e183c2a62dbfe895f63c120492dc7a57b2c36001af86",
    "download_status": "genuine PDF retained and opened in stated scope",
    "not_verified": []
  },
  {
    "key": "Wang2026",
    "title": "A complex rational homology six-sphere",
    "url": "https://arxiv.org/abs/2609.11541",
    "status": "verified in the specified scope",
    "opened_locators": [
      "Supplied original source order_two_rational_homology_sphere_new.tex, intro:main and main:theorem",
      "Complete proofs of fill:tate/fill:rankone, fill:a2, fill:good and fill:log, lines294–671",
      "Complete mon:jacobi-lemma and mon:representation proofs, lines907–1027"
    ],
    "uses": [
      "CDP D1.6 actual compact example and exact integral-homology theorem",
      "CDP D1.13 canonical-line computation through the actual fillings"
    ],
    "verification_scope": "Opened the supplied source, matched the primitive (2,1) rank-one exponent, the q=z0*z1*z2 rank-two charts, the normalized cubic comparison v->r^2*v and the free invariant translation. The named local-filling and displayed monodromy proofs were read in full. The main integral-homology theorem is imported at its exact statement; this record does not claim an independent audit of its entire topology section.",
    "own_check": "GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), effort Pro, writing run; 17 November 2026 UTC",
    "web_refs": [],
    "local_pdf": null,
    "sha256": null,
    "download_status": "user-supplied original source opened in specified scope",
    "not_verified": [
      "The complete integral homology calculation and cited Mumford/Engel construction theorems are not independently audited by this source-opening record."
    ],
    "local_source": "sources/papers/arXiv_2609.11541_Wang_src/order_two_rational_homology_sphere_new.tex",
    "source_sha256": "1ae1686d7ebb4e538c0aee38adce5643b3e51fe955ed6796e0cfc61cc6cf9c29"
  }
]
```

### work/maps_audit/references_verified.json

```json
[
  {
    "key": "Dimca2004",
    "url": "https://www.scribd.com/document/768903674/Dimca-Sheaves-in-Topology",
    "sha256": "a87ad75b555b4db44459c1f5a50380ac001327b8728bb3a439668455a20fcc30",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "verification_scope": "Exact original statement opened and hypotheses matched. Proper analytic f0:N0→disc; target function identity; constant integral constructible complex. Z is noetherian of global dimension one. Spaces locally compact, countable at infinity, finite real dimension. Original book reproduction matched to official Springer edition DOI 10.1007/978-3-642-18868-8.",
    "opened_locators": [
      "Def. 4.2.1 pp.102–103",
      "Prop.4.2.2",
      "Prop.4.2.11 p.109 entire proof",
      "Th.2.3.26 pp.41–42",
      "Cor.2.3.4 p.33",
      "Chapter 4 coefficient hypotheses p.81",
      "Example 3.1.2(ii); §3.1 dimensional hypotheses"
    ],
    "source": "sources/external/maps_audit/dimca_book_mirror.html",
    "status": "verified in the specified scope"
  },
  {
    "key": "Hatcher2002",
    "url": "https://pi.math.cornell.edu/~hatcher/AT/AT.pdf",
    "sha256": "bebb3032bf9021b956da3bd070eb6c67dc662cf849be9cdf6679f677560e5618",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "verification_scope": "Exact original statement opened and hypotheses matched. Collared manifold inclusion is cofibration; weak equivalence between CW types is homotopy equivalence; cofibration homotopy equivalence yields strong deformation retraction. Simply connected homology sphere gives homotopy sphere. Arbitrary local-system H_c² identification proved directly in candidate to avoid overreading the ring-bundle wording.",
    "opened_locators": [
      "Prop.0.19 and Cor.0.20 pp.16–17 complete proofs",
      "Th.4.5",
      "Th.4.32",
      "Cor.4.33",
      "§3.H pp.335–336"
    ],
    "source": "sources/external/maps_audit/hatcher.pdf",
    "status": "verified in the specified scope",
    "keys": [
      "Hatcher2002",
      "mapsHatcher02"
    ]
  },
  {
    "key": "Brown1962",
    "url": "https://www.maths.gla.ac.uk/~mpowell/Brown%20collars.pdf",
    "sha256": "8b54579c2ea344eab381257476d8f7e7d23c7b28bf059e4833259e8a51cb9204",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "verification_scope": "Exact original statement opened and hypotheses matched. Boundary of topological manifold has a collar; applied to actual boundary quotient. Correct DOI is 10.2307/1970177.",
    "opened_locators": [
      "Theorem 2 p.339",
      "Theorem 1 and Lemma 5 used in its proof"
    ],
    "source": "sources/external/maps_audit/brown_collars.pdf",
    "status": "verified in the specified scope"
  },
  {
    "key": "Smale1961",
    "url": "https://www.math.uchicago.edu/~shmuel/tom-readings/Smale%2C%20PC.pdf",
    "sha256": "f588608785f691c3f2efbf411b3f404b5771855624dfbfc17ed0a5f320204bc3",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "verification_scope": "Exact original statement opened and hypotheses matched. Closed smooth homotopy n-sphere, n≥5; conclude homeomorphism to standard sphere.",
    "opened_locators": [
      "Theorem A p.391"
    ],
    "source": "sources/external/maps_audit/smale1961.pdf",
    "status": "verified in the specified scope"
  },
  {
    "key": "Smale1962",
    "url": "https://webhomes.maths.ed.ac.uk/~v1ranick/papers/structur.pdf",
    "sha256": "164243cd982784303016304e69821ba02ca860770868e2636681243e7f545b5d",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "verification_scope": "Exact original statement opened and hypotheses matched. Simply connected oriented smooth h-cobordant n-manifolds, n≥5, are oriented diffeomorphic; Cor.1.2 explicitly states every homotopy six-sphere is diffeomorphic to S6.",
    "opened_locators": [
      "Theorem 1.1 p.387",
      "Corollary 1.2 p.388"
    ],
    "source": "sources/external/maps_audit/smale1962.pdf",
    "status": "verified in the specified scope"
  },
  {
    "key": "KervaireMilnor1963",
    "url": "https://doi.org/10.2307/1970128",
    "sha256": "d5d79b945ef347db92a07add5a03589c8c34a55312bf3e6d241ba52ec528d8e0",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "verification_scope": "Exact original statement opened and hypotheses matched. Theta6 has order one; h-cobordism classes coincide with oriented diffeomorphism classes for dimension six. Scanned original visually inspected.",
    "opened_locators": [
      "Opening table pp.504–505; following remark"
    ],
    "source": "sources/external/maps_audit/kervaire_milnor.pdf",
    "status": "verified in the specified scope",
    "keys": [
      "KervaireMilnor1963",
      "ffKervaireMilnor63"
    ]
  },
  {
    "key": "Knudson2004",
    "url": "https://arxiv.org/pdf/math/0409133",
    "sha256": "6a94b548547341f3484c4d687c8c3d5129cb2925d21c7ad8234f1feacd425834",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "verification_scope": "Exact original statement opened and hypotheses matched. Finite-dimensional Z/p-CW mod-p homology sphere; fixed set empty or mod-p homology sphere. Involution on closed smooth real six-sphere meets CW hypothesis by Illman1972 Th.3.1.",
    "opened_locators": [
      "Theorem 4.1(1)"
    ],
    "source": "sources/external/maps_audit/knudson.pdf",
    "status": "verified in the specified scope"
  },
  {
    "key": "Illman1972",
    "url": "https://ncatlab.org/nlab/files/Illman_EquivariantAlgebraicTopology1972.pdf",
    "sha256": "ae23a9ccca5ef2f9b5fa41d5cea8af08fad137a64649ac5cf1d69b23c5c40a9b",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "verification_scope": "Exact original statement opened and hypotheses matched. Smooth antiholomorphic involution is a differentiable Z/2 action on compact smooth manifold; equivariant triangulation gives finite-dimensional G-CW structure. Original scanned theorem visually read; theorem proof not independently reproved.",
    "opened_locators": [
      "Chapter 3 hypothesis compact Lie group p.44",
      "Theorem 3.1 p.48; PDF page 53"
    ],
    "source": "sources/external/maps_audit/illman1972.pdf",
    "status": "verified in the specified scope"
  },
  {
    "keys": [
      "StacksProject"
    ],
    "opened_locators": [
      "Remark 13.12.4",
      "Example 20.29.3",
      "Lemma 21.26.1",
      "Section 12.24, equations and Lemma 12.24.2",
      "Section 20.31, Lemmas 20.31.1–3 and Remark 20.31.2"
    ],
    "source": [
      "https://stacks.math.columbia.edu/tag/08J5",
      "https://stacks.math.columbia.edu/tag/0FLJ",
      "https://stacks.math.columbia.edu/tag/0F16",
      "https://stacks.math.columbia.edu/tag/012K",
      "https://stacks.math.columbia.edu/tag/0FKU"
    ],
    "verification_scope": "Exact original statement opened and hypotheses matched. Canonical truncation triangles for any complex in an abelian category. | Exact original statement opened and hypotheses matched. Hypercohomology spectral sequence and bounded-below convergence; cohomological d2 indexing. | Exact original statement opened and hypotheses matched. Conditional MV triangle: comparison map must be an isomorphism. Candidate proves it for the two-open cover by degreewise exact flabby Cech sequence. | Exact original statement opened and hypotheses matched. Exact filtered-complex dr representative formula. | Exact original statement opened and hypotheses matched. Derived cup product, its naive-complex comparison and functoriality.",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "status": "verified in the specified scope"
  },
  {
    "key": "Beardon1983",
    "url": "https://ru.djvu.online/file/s9XGIhPaw1MHy",
    "edition_opened": "1986 Russian translation, section 10.6; English corrected second printing, section 7.38 only",
    "opened_locators": [
      "Definition 10.6.1, pp.247–248 (translation)",
      "Definition 10.6.3 and Theorem 10.6.4, forward implication and proof, pp.249–250 (translation)",
      "English section 7.38, Theorem 7.38.2 and subsequent parabolic criterion, pp.179–181"
    ],
    "verification_scope": "The actual triangle has angles pi/3, pi/4, 0. Reflection products give its elliptic rotations and parabolic cusp; the orientation-preserving subgroup has index two. The forward signature construction supplies the unique parabolic conjugacy class. The manuscript proves simultaneous reversal by explicit products and reduced words.",
    "limits": "English section 10.6 NOT opened; no assertion of its page-level verification. The converse of Theorem 10.6.4 is not used. Translation page numbers are not English page numbers.",
    "applications": [
      "WORK:lem:triangle-generator-orientations"
    ],
    "artifacts": [
      {
        "source": "sources/external/maps_audit/wb_foundation_final_open.json",
        "sha256": "e5636ba86ea9f7564c7af4095ccbe430a0c8c19955abd1b4d13c5a42c5fc1630",
        "artifact_type": "web-rendered primary translation excerpt"
      },
      {
        "source": "sources/external/maps_audit/wb_beardon_and_fulton_open.json",
        "sha256": "04b196dd50744d2b0402fb3f42bf1812abd5306bce5ce8a4b42d0925dee3e7f3",
        "artifact_type": "web-rendered English primary-text excerpts"
      }
    ],
    "status": "verified in the specified translation and English section 7.38 scopes",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "source": [
      "sources/external/maps_audit/wb_foundation_final_open.json",
      "sources/external/maps_audit/wb_beardon_and_fulton_open.json"
    ],
    "sha256": "e5636ba86ea9f7564c7af4095ccbe430a0c8c19955abd1b4d13c5a42c5fc1630",
    "sha256_scope": "web-rendered primary translation excerpt"
  },
  {
    "key": "Serre1973",
    "url": "https://www.math.purdue.edu/~jlipman/MA598/Serre-Course%20in%20Arithmetic.pdf",
    "edition_opened": "1973 Springer English edition, original scanned pages",
    "opened_locators": [
      "Chapter VII, Theorems 1–2, pp.78–79",
      "Theorem 3, p.85",
      "Theorem 4 and Proposition 5, pp.88–89",
      "Proposition 8 and normalized Fourier expansions, pp.92–93"
    ],
    "verification_scope": "The modular quotient has stabilizer orders 3 and 2, j has values 0 and 1728 there, is unramified elsewhere, and identifies the quotient with the affine line. The printed Fourier expansions give j(q)=q^(-1)(1+O(q)). These match local degrees 3 and 4 of the source map, so both deleted meridians act trivially on the lift.",
    "limits": "The nondegenerate period construction and its analytic estimates are separate manuscript proofs, not consequences attributed to Serre.",
    "applications": [
      "WORK:prop:period-input-audit"
    ],
    "artifacts": [
      {
        "source": "sources/external/maps_audit/serre1973.pdf",
        "sha256": "15cea1a59aec4541efd5e9565d03624e5e6a3e896418e70b9934de27519a21ae",
        "artifact_type": "original book scan"
      }
    ],
    "status": "verified in the specified scope",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "source": [
      "sources/external/maps_audit/serre1973.pdf"
    ],
    "sha256": "15cea1a59aec4541efd5e9565d03624e5e6a3e896418e70b9934de27519a21ae",
    "sha256_scope": "original book scan"
  },
  {
    "key": "Brown1982",
    "url": "https://ru.djvu.online/file/QtlfpGD38sXAT",
    "edition_opened": "1982 Springer English edition, web-rendered original text",
    "opened_locators": [
      "Chapter I section 5, bar boundary (5.2), pp.18–19",
      "Chapter VII section 5, cohomology and cup products, pp.170–171",
      "Chapter VII section 6, Theorem 6.3 and cohomology version, pp.171–172"
    ],
    "verification_scope": "The group extension has normal subgroup Lambda, cyclic quotient C_m, and trivial integral coefficients. The contractible universal cover identifies space and group cohomology; conjugation gives the displayed exterior-power action. Brown supplies the multiplicative Hochschild–Serre sequence. The specific transgression is independently computed from the section factor set in the accompanying supplement.",
    "limits": "The downloaded HTML is a CAPTCHA and is not a source artifact. The preserved web-rendered original excerpts are the evidence. The explicit extension transgression is not claimed to be printed in these Brown pages.",
    "applications": [
      "WORK:prop:finite-indices"
    ],
    "artifacts": [
      {
        "source": "sources/external/maps_audit/wb_brown_final_scope.json",
        "sha256": "c8d31d2aa6cbdff135763bdfc3b67c6d6ec4045d84e8ac34bacc48cd9921c8f5",
        "artifact_type": "web-rendered original book excerpt"
      },
      {
        "source": "sources/external/maps_audit/wb_source_group_and_orbits.json",
        "sha256": "4feb88bb4120ad34610da9de95064b85662dc92d941e5b13052404e9fa44ffb1",
        "artifact_type": "web-rendered original bar-resolution excerpt"
      }
    ],
    "status": "verified in the specified scope",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "source": [
      "sources/external/maps_audit/wb_brown_final_scope.json",
      "sources/external/maps_audit/wb_source_group_and_orbits.json"
    ],
    "sha256": "c8d31d2aa6cbdff135763bdfc3b67c6d6ec4045d84e8ac34bacc48cd9921c8f5",
    "sha256_scope": "web-rendered original book excerpt"
  },
  {
    "key": "Cartan1954Quotient",
    "url": "https://www.numdam.org/item/SHC_1953-1954__6__A12_0.pdf",
    "edition_opened": "Original 1953–1954 seminar, Exposé 12",
    "opened_locators": [
      "Section 1, conditions (I)–(II), pp.1–2",
      "Theorem 1, p.2"
    ],
    "verification_scope": "Finite group action on the Hausdorff complex manifold satisfies orbit separation, finite stabilizers and the stated local separation condition. Cartan supplies the analytic quotient and invariant structure sheaf. In the finite fillings the action is free, and the manuscript separately proves smoothness using disjoint translated charts.",
    "limits": "Smoothness is not inferred for an arbitrary nonfree finite quotient.",
    "applications": [
      "WORK:ffcert:prop:quotient-charts"
    ],
    "artifacts": [
      {
        "source": "sources/external/maps_audit/cartan1954_quotient.pdf",
        "sha256": "38e9c37dfc803e71093d15a2e905c7f808c8cbc46ef5584a174bb307bdafde85",
        "artifact_type": "original seminar scan"
      }
    ],
    "status": "verified in the specified scope",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "source": [
      "sources/external/maps_audit/cartan1954_quotient.pdf"
    ],
    "sha256": "38e9c37dfc803e71093d15a2e905c7f808c8cbc46ef5584a174bb307bdafde85",
    "sha256_scope": "original seminar scan",
    "previous_record": {
      "key": "Cartan1954Quotient",
      "url": "https://www.numdam.org/item/SHC_1953-1954__6__A12_0.pdf",
      "edition_opened": "Original 1953–1954 seminar, Exposé 12",
      "opened_locators": [
        "Section 1, conditions (I)–(II), pp.1–2",
        "Theorem 1, p.2"
      ],
      "verification_scope": "Finite group action on the Hausdorff complex manifold satisfies orbit separation, finite stabilizers and the stated local separation condition. Cartan supplies the analytic quotient and invariant structure sheaf. In the finite fillings the action is free, and the manuscript separately proves smoothness using disjoint translated charts.",
      "limits": "Smoothness is not inferred for an arbitrary nonfree finite quotient.",
      "applications": [
        "WORK:prop:finite-quotient-audit"
      ],
      "artifacts": [
        {
          "source": "sources/external/maps_audit/cartan1954_quotient.pdf",
          "sha256": "38e9c37dfc803e71093d15a2e905c7f808c8cbc46ef5584a174bb307bdafde85",
          "artifact_type": "original seminar scan"
        }
      ],
      "status": "verified in the specified scope",
      "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
      "effort": "Pro",
      "date": "2026-11-17",
      "source": [
        "sources/external/maps_audit/cartan1954_quotient.pdf"
      ],
      "sha256": "38e9c37dfc803e71093d15a2e905c7f808c8cbc46ef5584a174bb307bdafde85",
      "sha256_scope": "original seminar scan"
    }
  },
  {
    "key": "Fulton1993",
    "url": "https://www.scribd.com/document/768783720/Introduction-to-Toric-Varieties-Fulton",
    "edition_opened": "Reproduction of 1993 book, including 1996 errata page",
    "opened_locators": [
      "Section 1.2, separation lemma and Proposition 3, pp.13–14",
      "Section 1.3, affine toric charts and face localization, pp.15–19",
      "Section 1.4, fan gluing and closed-diagonal lemma, pp.20–22"
    ],
    "verification_scope": "Rational strongly convex cones and their common faces give the affine semigroup charts and open gluing used in the manuscript. The source assumes finite fans by default. The countable fan and proper cusp quotient require the manuscript’s additional explicit arguments.",
    "limits": "Chapter 3 has not been opened. Replace its broad citation for orbit correspondence by Cox–Little–Schenck Theorem 3.2.6. Divisor/line-bundle applications elsewhere are outside this verification scope.",
    "applications": [
      "WORK:thm:candidate-cusp-geometry"
    ],
    "artifacts": [
      {
        "source": "sources/external/maps_audit/wb_foundation_final_open.json",
        "sha256": "e5636ba86ea9f7564c7af4095ccbe430a0c8c19955abd1b4d13c5a42c5fc1630",
        "artifact_type": "web-rendered original book excerpt"
      },
      {
        "source": "sources/external/maps_audit/wb_foundation_final_find.json",
        "sha256": "bc8e02bfae7c2a864388fae8bbd05277b73c67946dc56cba7ec9de83da8be0af",
        "artifact_type": "web-rendered original book excerpt"
      }
    ],
    "status": "verified in the specified Chapter 1 scope",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "source": [
      "sources/external/maps_audit/wb_foundation_final_open.json",
      "sources/external/maps_audit/wb_foundation_final_find.json"
    ],
    "sha256": "e5636ba86ea9f7564c7af4095ccbe430a0c8c19955abd1b4d13c5a42c5fc1630",
    "sha256_scope": "web-rendered original book excerpt",
    "previous_record": {
      "key": "Fulton1993",
      "url": "https://www.scribd.com/document/768783720/Introduction-to-Toric-Varieties-Fulton",
      "edition_opened": "Reproduction of 1993 book, including 1996 errata page",
      "opened_locators": [
        "Section 1.2, separation lemma and Proposition 3, pp.13–14",
        "Section 1.3, affine toric charts and face localization, pp.15–19",
        "Section 1.4, fan gluing and closed-diagonal lemma, pp.20–22"
      ],
      "verification_scope": "Rational strongly convex cones and their common faces give the affine semigroup charts and open gluing used in the manuscript. The source assumes finite fans by default. The countable fan and proper cusp quotient require the manuscript’s additional explicit arguments.",
      "limits": "Chapter 3 has not been opened. Replace its broad citation for orbit correspondence by Cox–Little–Schenck Theorem 3.2.6. Divisor/line-bundle applications elsewhere are outside this verification scope.",
      "applications": [
        "WORK:prop:candidate-cusp-geometry"
      ],
      "artifacts": [
        {
          "source": "sources/external/maps_audit/wb_foundation_final_open.json",
          "sha256": "e5636ba86ea9f7564c7af4095ccbe430a0c8c19955abd1b4d13c5a42c5fc1630",
          "artifact_type": "web-rendered original book excerpt"
        },
        {
          "source": "sources/external/maps_audit/wb_foundation_final_find.json",
          "sha256": "bc8e02bfae7c2a864388fae8bbd05277b73c67946dc56cba7ec9de83da8be0af",
          "artifact_type": "web-rendered original book excerpt"
        }
      ],
      "status": "verified in the specified Chapter 1 scope",
      "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
      "effort": "Pro",
      "date": "2026-11-17",
      "source": [
        "sources/external/maps_audit/wb_foundation_final_open.json",
        "sources/external/maps_audit/wb_foundation_final_find.json"
      ],
      "sha256": "e5636ba86ea9f7564c7af4095ccbe430a0c8c19955abd1b4d13c5a42c5fc1630",
      "sha256_scope": "web-rendered original book excerpt"
    }
  },
  {
    "key": "CoxLittleSchenck2011",
    "url": "https://pi.math.cornell.edu/~tsh/cornell-only/cox-little-schenck-toric.pdf",
    "edition_opened": "Authors’ 2010 prepublication text; final bibliographic edition 2011",
    "opened_locators": [
      "Lemma 1.2.13, pp.28–29",
      "Definition 3.1.2, Proposition 3.1.3 and Theorem 3.1.5, pp.106–108",
      "Theorem 3.2.6 and Proposition 3.2.7, pp.119–121",
      "Proposition 12.1.9 and Theorem 12.1.10, pp.565–567"
    ],
    "verification_scope": "Pairwise cone separation, affine gluing, and orbit correspondence match each finite collection of manuscript charts. The source’s fan definition is finite; the infinite-fan extension is independently proved. The fundamental-group result is checked for corroboration, while the candidate now prints its own ray-disc and transversality proof.",
    "limits": "Opened edition is the authors’ 2010 text, not a downloaded 2011 final-edition scan. Binary downloads returned HTTP 403; preserved rendered excerpts are the source evidence. No unexamined divisor theorem is certified.",
    "applications": [
      "WORK:thm:candidate-cusp-geometry",
      "WORK:prop:geometric-pi1"
    ],
    "artifacts": [
      {
        "source": "sources/external/maps_audit/wb_sources_cls_open.json",
        "sha256": "562c11c44dcbdbf0ae68cee0cde4bd388b761b9baa667bd9b63718b45a0e345c",
        "artifact_type": "web-rendered author prepublication excerpt"
      },
      {
        "source": "sources/external/maps_audit/wb_source_group_and_orbits.json",
        "sha256": "4feb88bb4120ad34610da9de95064b85662dc92d941e5b13052404e9fa44ffb1",
        "artifact_type": "web-rendered author prepublication excerpt"
      },
      {
        "source": "sources/external/maps_audit/wb_source_last_open.json",
        "sha256": "885b4d985afcc1845636321b5be10425c8a3d8de51350cc8ab2bb99d584bc748",
        "artifact_type": "web-rendered author prepublication excerpt"
      }
    ],
    "status": "verified in the specified author-prepublication scope",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "source": [
      "sources/external/maps_audit/wb_sources_cls_open.json",
      "sources/external/maps_audit/wb_source_group_and_orbits.json",
      "sources/external/maps_audit/wb_source_last_open.json"
    ],
    "sha256": "562c11c44dcbdbf0ae68cee0cde4bd388b761b9baa667bd9b63718b45a0e345c",
    "sha256_scope": "web-rendered author prepublication excerpt",
    "previous_record": {
      "key": "CoxLittleSchenck2011",
      "url": "https://pi.math.cornell.edu/~tsh/cornell-only/cox-little-schenck-toric.pdf",
      "edition_opened": "Authors’ 2010 prepublication text; final bibliographic edition 2011",
      "opened_locators": [
        "Lemma 1.2.13, pp.28–29",
        "Definition 3.1.2, Proposition 3.1.3 and Theorem 3.1.5, pp.106–108",
        "Theorem 3.2.6 and Proposition 3.2.7, pp.119–121",
        "Proposition 12.1.9 and Theorem 12.1.10, pp.565–567"
      ],
      "verification_scope": "Pairwise cone separation, affine gluing, and orbit correspondence match each finite collection of manuscript charts. The source’s fan definition is finite; the infinite-fan extension is independently proved. The fundamental-group result is checked for corroboration, while the candidate now prints its own ray-disc and transversality proof.",
      "limits": "Opened edition is the authors’ 2010 text, not a downloaded 2011 final-edition scan. Binary downloads returned HTTP 403; preserved rendered excerpts are the source evidence. No unexamined divisor theorem is certified.",
      "applications": [
        "WORK:prop:candidate-cusp-geometry",
        "WORK:prop:geometric-pi1"
      ],
      "artifacts": [
        {
          "source": "sources/external/maps_audit/wb_sources_cls_open.json",
          "sha256": "562c11c44dcbdbf0ae68cee0cde4bd388b761b9baa667bd9b63718b45a0e345c",
          "artifact_type": "web-rendered author prepublication excerpt"
        },
        {
          "source": "sources/external/maps_audit/wb_source_group_and_orbits.json",
          "sha256": "4feb88bb4120ad34610da9de95064b85662dc92d941e5b13052404e9fa44ffb1",
          "artifact_type": "web-rendered author prepublication excerpt"
        },
        {
          "source": "sources/external/maps_audit/wb_source_last_open.json",
          "sha256": "885b4d985afcc1845636321b5be10425c8a3d8de51350cc8ab2bb99d584bc748",
          "artifact_type": "web-rendered author prepublication excerpt"
        }
      ],
      "status": "verified in the specified author-prepublication scope",
      "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
      "effort": "Pro",
      "date": "2026-11-17",
      "source": [
        "sources/external/maps_audit/wb_sources_cls_open.json",
        "sources/external/maps_audit/wb_source_group_and_orbits.json",
        "sources/external/maps_audit/wb_source_last_open.json"
      ],
      "sha256": "562c11c44dcbdbf0ae68cee0cde4bd388b761b9baa667bd9b63718b45a0e345c",
      "sha256_scope": "web-rendered author prepublication excerpt"
    }
  }
]
```

### work/maps_audit/wb_foundation_source_checks.json

```json
[
  {
    "key": "Beardon1983",
    "url": "https://ru.djvu.online/file/s9XGIhPaw1MHy",
    "edition_opened": "1986 Russian translation, section 10.6; English corrected second printing, section 7.38 only",
    "opened_locators": [
      "Definition 10.6.1, pp.247–248 (translation)",
      "Definition 10.6.3 and Theorem 10.6.4, forward implication and proof, pp.249–250 (translation)",
      "English section 7.38, Theorem 7.38.2 and subsequent parabolic criterion, pp.179–181"
    ],
    "verification_scope": "The actual triangle has angles pi/3, pi/4, 0. Reflection products give its elliptic rotations and parabolic cusp; the orientation-preserving subgroup has index two. The forward signature construction supplies the unique parabolic conjugacy class. The manuscript proves simultaneous reversal by explicit products and reduced words.",
    "limits": "English section 10.6 NOT opened; no assertion of its page-level verification. The converse of Theorem 10.6.4 is not used. Translation page numbers are not English page numbers.",
    "applications": [
      "WORK:lem:triangle-generator-orientations"
    ],
    "artifacts": [
      {
        "source": "sources/external/maps_audit/wb_foundation_final_open.json",
        "sha256": "e5636ba86ea9f7564c7af4095ccbe430a0c8c19955abd1b4d13c5a42c5fc1630",
        "artifact_type": "web-rendered primary translation excerpt"
      },
      {
        "source": "sources/external/maps_audit/wb_beardon_and_fulton_open.json",
        "sha256": "04b196dd50744d2b0402fb3f42bf1812abd5306bce5ce8a4b42d0925dee3e7f3",
        "artifact_type": "web-rendered English primary-text excerpts"
      }
    ],
    "status": "verified in the specified translation and English section 7.38 scopes",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "source": [
      "sources/external/maps_audit/wb_foundation_final_open.json",
      "sources/external/maps_audit/wb_beardon_and_fulton_open.json"
    ],
    "sha256": "e5636ba86ea9f7564c7af4095ccbe430a0c8c19955abd1b4d13c5a42c5fc1630",
    "sha256_scope": "web-rendered primary translation excerpt"
  },
  {
    "key": "Serre1973",
    "url": "https://www.math.purdue.edu/~jlipman/MA598/Serre-Course%20in%20Arithmetic.pdf",
    "edition_opened": "1973 Springer English edition, original scanned pages",
    "opened_locators": [
      "Chapter VII, Theorems 1–2, pp.78–79",
      "Theorem 3, p.85",
      "Theorem 4 and Proposition 5, pp.88–89",
      "Proposition 8 and normalized Fourier expansions, pp.92–93"
    ],
    "verification_scope": "The modular quotient has stabilizer orders 3 and 2, j has values 0 and 1728 there, is unramified elsewhere, and identifies the quotient with the affine line. The printed Fourier expansions give j(q)=q^(-1)(1+O(q)). These match local degrees 3 and 4 of the source map, so both deleted meridians act trivially on the lift.",
    "limits": "The nondegenerate period construction and its analytic estimates are separate manuscript proofs, not consequences attributed to Serre.",
    "applications": [
      "WORK:prop:period-input-audit"
    ],
    "artifacts": [
      {
        "source": "sources/external/maps_audit/serre1973.pdf",
        "sha256": "15cea1a59aec4541efd5e9565d03624e5e6a3e896418e70b9934de27519a21ae",
        "artifact_type": "original book scan"
      }
    ],
    "status": "verified in the specified scope",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "source": [
      "sources/external/maps_audit/serre1973.pdf"
    ],
    "sha256": "15cea1a59aec4541efd5e9565d03624e5e6a3e896418e70b9934de27519a21ae",
    "sha256_scope": "original book scan"
  },
  {
    "key": "Brown1982",
    "url": "https://ru.djvu.online/file/QtlfpGD38sXAT",
    "edition_opened": "1982 Springer English edition, web-rendered original text",
    "opened_locators": [
      "Chapter I section 5, bar boundary (5.2), pp.18–19",
      "Chapter VII section 5, cohomology and cup products, pp.170–171",
      "Chapter VII section 6, Theorem 6.3 and cohomology version, pp.171–172"
    ],
    "verification_scope": "The group extension has normal subgroup Lambda, cyclic quotient C_m, and trivial integral coefficients. The contractible universal cover identifies space and group cohomology; conjugation gives the displayed exterior-power action. Brown supplies the multiplicative Hochschild–Serre sequence. The specific transgression is independently computed from the section factor set in the accompanying supplement.",
    "limits": "The downloaded HTML is a CAPTCHA and is not a source artifact. The preserved web-rendered original excerpts are the evidence. The explicit extension transgression is not claimed to be printed in these Brown pages.",
    "applications": [
      "WORK:prop:finite-indices"
    ],
    "artifacts": [
      {
        "source": "sources/external/maps_audit/wb_brown_final_scope.json",
        "sha256": "c8d31d2aa6cbdff135763bdfc3b67c6d6ec4045d84e8ac34bacc48cd9921c8f5",
        "artifact_type": "web-rendered original book excerpt"
      },
      {
        "source": "sources/external/maps_audit/wb_source_group_and_orbits.json",
        "sha256": "4feb88bb4120ad34610da9de95064b85662dc92d941e5b13052404e9fa44ffb1",
        "artifact_type": "web-rendered original bar-resolution excerpt"
      }
    ],
    "status": "verified in the specified scope",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "source": [
      "sources/external/maps_audit/wb_brown_final_scope.json",
      "sources/external/maps_audit/wb_source_group_and_orbits.json"
    ],
    "sha256": "c8d31d2aa6cbdff135763bdfc3b67c6d6ec4045d84e8ac34bacc48cd9921c8f5",
    "sha256_scope": "web-rendered original book excerpt"
  },
  {
    "key": "Cartan1954Quotient",
    "url": "https://www.numdam.org/item/SHC_1953-1954__6__A12_0.pdf",
    "edition_opened": "Original 1953–1954 seminar, Exposé 12",
    "opened_locators": [
      "Section 1, conditions (I)–(II), pp.1–2",
      "Theorem 1, p.2"
    ],
    "verification_scope": "Finite group action on the Hausdorff complex manifold satisfies orbit separation, finite stabilizers and the stated local separation condition. Cartan supplies the analytic quotient and invariant structure sheaf. In the finite fillings the action is free, and the manuscript separately proves smoothness using disjoint translated charts.",
    "limits": "Smoothness is not inferred for an arbitrary nonfree finite quotient.",
    "applications": [
      "WORK:ffcert:prop:quotient-charts"
    ],
    "artifacts": [
      {
        "source": "sources/external/maps_audit/cartan1954_quotient.pdf",
        "sha256": "38e9c37dfc803e71093d15a2e905c7f808c8cbc46ef5584a174bb307bdafde85",
        "artifact_type": "original seminar scan"
      }
    ],
    "status": "verified in the specified scope",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "source": [
      "sources/external/maps_audit/cartan1954_quotient.pdf"
    ],
    "sha256": "38e9c37dfc803e71093d15a2e905c7f808c8cbc46ef5584a174bb307bdafde85",
    "sha256_scope": "original seminar scan"
  },
  {
    "key": "Fulton1993",
    "url": "https://www.scribd.com/document/768783720/Introduction-to-Toric-Varieties-Fulton",
    "edition_opened": "Reproduction of 1993 book, including 1996 errata page",
    "opened_locators": [
      "Section 1.2, separation lemma and Proposition 3, pp.13–14",
      "Section 1.3, affine toric charts and face localization, pp.15–19",
      "Section 1.4, fan gluing and closed-diagonal lemma, pp.20–22"
    ],
    "verification_scope": "Rational strongly convex cones and their common faces give the affine semigroup charts and open gluing used in the manuscript. The source assumes finite fans by default. The countable fan and proper cusp quotient require the manuscript’s additional explicit arguments.",
    "limits": "Chapter 3 has not been opened. Replace its broad citation for orbit correspondence by Cox–Little–Schenck Theorem 3.2.6. Divisor/line-bundle applications elsewhere are outside this verification scope.",
    "applications": [
      "WORK:thm:candidate-cusp-geometry"
    ],
    "artifacts": [
      {
        "source": "sources/external/maps_audit/wb_foundation_final_open.json",
        "sha256": "e5636ba86ea9f7564c7af4095ccbe430a0c8c19955abd1b4d13c5a42c5fc1630",
        "artifact_type": "web-rendered original book excerpt"
      },
      {
        "source": "sources/external/maps_audit/wb_foundation_final_find.json",
        "sha256": "bc8e02bfae7c2a864388fae8bbd05277b73c67946dc56cba7ec9de83da8be0af",
        "artifact_type": "web-rendered original book excerpt"
      }
    ],
    "status": "verified in the specified Chapter 1 scope",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "source": [
      "sources/external/maps_audit/wb_foundation_final_open.json",
      "sources/external/maps_audit/wb_foundation_final_find.json"
    ],
    "sha256": "e5636ba86ea9f7564c7af4095ccbe430a0c8c19955abd1b4d13c5a42c5fc1630",
    "sha256_scope": "web-rendered original book excerpt"
  },
  {
    "key": "CoxLittleSchenck2011",
    "url": "https://pi.math.cornell.edu/~tsh/cornell-only/cox-little-schenck-toric.pdf",
    "edition_opened": "Authors’ 2010 prepublication text; final bibliographic edition 2011",
    "opened_locators": [
      "Lemma 1.2.13, pp.28–29",
      "Definition 3.1.2, Proposition 3.1.3 and Theorem 3.1.5, pp.106–108",
      "Theorem 3.2.6 and Proposition 3.2.7, pp.119–121",
      "Proposition 12.1.9 and Theorem 12.1.10, pp.565–567"
    ],
    "verification_scope": "Pairwise cone separation, affine gluing, and orbit correspondence match each finite collection of manuscript charts. The source’s fan definition is finite; the infinite-fan extension is independently proved. The fundamental-group result is checked for corroboration, while the candidate now prints its own ray-disc and transversality proof.",
    "limits": "Opened edition is the authors’ 2010 text, not a downloaded 2011 final-edition scan. Binary downloads returned HTTP 403; preserved rendered excerpts are the source evidence. No unexamined divisor theorem is certified.",
    "applications": [
      "WORK:thm:candidate-cusp-geometry",
      "WORK:prop:geometric-pi1"
    ],
    "artifacts": [
      {
        "source": "sources/external/maps_audit/wb_sources_cls_open.json",
        "sha256": "562c11c44dcbdbf0ae68cee0cde4bd388b761b9baa667bd9b63718b45a0e345c",
        "artifact_type": "web-rendered author prepublication excerpt"
      },
      {
        "source": "sources/external/maps_audit/wb_source_group_and_orbits.json",
        "sha256": "4feb88bb4120ad34610da9de95064b85662dc92d941e5b13052404e9fa44ffb1",
        "artifact_type": "web-rendered author prepublication excerpt"
      },
      {
        "source": "sources/external/maps_audit/wb_source_last_open.json",
        "sha256": "885b4d985afcc1845636321b5be10425c8a3d8de51350cc8ab2bb99d584bc748",
        "artifact_type": "web-rendered author prepublication excerpt"
      }
    ],
    "status": "verified in the specified author-prepublication scope",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17",
    "source": [
      "sources/external/maps_audit/wb_sources_cls_open.json",
      "sources/external/maps_audit/wb_source_group_and_orbits.json",
      "sources/external/maps_audit/wb_source_last_open.json"
    ],
    "sha256": "562c11c44dcbdbf0ae68cee0cde4bd388b761b9baa667bd9b63718b45a0e345c",
    "sha256_scope": "web-rendered author prepublication excerpt"
  }
]
```

### work/maps_audit/topology_source_checks.json

```json
[
  {
    "key": "Dimca2004",
    "file": "sources/external/maps_audit/dimca_book_mirror.html",
    "url": "https://www.scribd.com/document/768903674/Dimca-Sheaves-in-Topology",
    "sha256": "a87ad75b555b4db44459c1f5a50380ac001327b8728bb3a439668455a20fcc30",
    "locators": [
      "Def. 4.2.1 pp.102–103",
      "Prop.4.2.2",
      "Prop.4.2.11 p.109 entire proof",
      "Th.2.3.26 pp.41–42",
      "Cor.2.3.4 p.33",
      "Chapter 4 coefficient hypotheses p.81",
      "Example 3.1.2(ii); §3.1 dimensional hypotheses"
    ],
    "application_match": "Proper analytic f0:N0→disc; target function identity; constant integral constructible complex. Z is noetherian of global dimension one. Spaces locally compact, countable at infinity, finite real dimension. Original book reproduction matched to official Springer edition DOI 10.1007/978-3-642-18868-8.",
    "scope": "Exact original statement opened and hypotheses matched.",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17"
  },
  {
    "key": "Hatcher2002",
    "file": "sources/external/maps_audit/hatcher.pdf",
    "url": "https://pi.math.cornell.edu/~hatcher/AT/AT.pdf",
    "sha256": "bebb3032bf9021b956da3bd070eb6c67dc662cf849be9cdf6679f677560e5618",
    "locators": [
      "Prop.0.19 and Cor.0.20 pp.16–17 complete proofs",
      "Th.4.5",
      "Th.4.32",
      "Cor.4.33",
      "§3.H pp.335–336"
    ],
    "application_match": "Collared manifold inclusion is cofibration; weak equivalence between CW types is homotopy equivalence; cofibration homotopy equivalence yields strong deformation retraction. Simply connected homology sphere gives homotopy sphere. Arbitrary local-system H_c² identification proved directly in candidate to avoid overreading the ring-bundle wording.",
    "scope": "Exact original statement opened and hypotheses matched.",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17"
  },
  {
    "key": "Brown1962",
    "file": "sources/external/maps_audit/brown_collars.pdf",
    "url": "https://www.maths.gla.ac.uk/~mpowell/Brown%20collars.pdf",
    "sha256": "8b54579c2ea344eab381257476d8f7e7d23c7b28bf059e4833259e8a51cb9204",
    "locators": [
      "Theorem 2 p.339",
      "Theorem 1 and Lemma 5 used in its proof"
    ],
    "application_match": "Boundary of topological manifold has a collar; applied to actual boundary quotient. Correct DOI is 10.2307/1970177.",
    "scope": "Exact original statement opened and hypotheses matched.",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17"
  },
  {
    "key": "Smale1961",
    "file": "sources/external/maps_audit/smale1961.pdf",
    "url": "https://www.math.uchicago.edu/~shmuel/tom-readings/Smale%2C%20PC.pdf",
    "sha256": "f588608785f691c3f2efbf411b3f404b5771855624dfbfc17ed0a5f320204bc3",
    "locators": [
      "Theorem A p.391"
    ],
    "application_match": "Closed smooth homotopy n-sphere, n≥5; conclude homeomorphism to standard sphere.",
    "scope": "Exact original statement opened and hypotheses matched.",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17"
  },
  {
    "key": "Smale1962",
    "file": "sources/external/maps_audit/smale1962.pdf",
    "url": "https://webhomes.maths.ed.ac.uk/~v1ranick/papers/structur.pdf",
    "sha256": "164243cd982784303016304e69821ba02ca860770868e2636681243e7f545b5d",
    "locators": [
      "Theorem 1.1 p.387",
      "Corollary 1.2 p.388"
    ],
    "application_match": "Simply connected oriented smooth h-cobordant n-manifolds, n≥5, are oriented diffeomorphic; Cor.1.2 explicitly states every homotopy six-sphere is diffeomorphic to S6.",
    "scope": "Exact original statement opened and hypotheses matched.",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17"
  },
  {
    "key": "KervaireMilnor1963",
    "file": "sources/external/maps_audit/kervaire_milnor.pdf",
    "url": "https://doi.org/10.2307/1970128",
    "sha256": "d5d79b945ef347db92a07add5a03589c8c34a55312bf3e6d241ba52ec528d8e0",
    "locators": [
      "Opening table pp.504–505; following remark"
    ],
    "application_match": "Theta6 has order one; h-cobordism classes coincide with oriented diffeomorphism classes for dimension six. Scanned original visually inspected.",
    "scope": "Exact original statement opened and hypotheses matched.",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17"
  },
  {
    "key": "Knudson2004",
    "file": "sources/external/maps_audit/knudson.pdf",
    "url": "https://arxiv.org/pdf/math/0409133",
    "sha256": "6a94b548547341f3484c4d687c8c3d5129cb2925d21c7ad8234f1feacd425834",
    "locators": [
      "Theorem 4.1(1)"
    ],
    "application_match": "Finite-dimensional Z/p-CW mod-p homology sphere; fixed set empty or mod-p homology sphere. Involution on closed smooth real six-sphere meets CW hypothesis by Illman1972 Th.3.1.",
    "scope": "Exact original statement opened and hypotheses matched.",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17"
  },
  {
    "key": "Illman1972",
    "file": "sources/external/maps_audit/illman1972.pdf",
    "url": "https://ncatlab.org/nlab/files/Illman_EquivariantAlgebraicTopology1972.pdf",
    "sha256": "ae23a9ccca5ef2f9b5fa41d5cea8af08fad137a64649ac5cf1d69b23c5c40a9b",
    "locators": [
      "Chapter 3 hypothesis compact Lie group p.44",
      "Theorem 3.1 p.48; PDF page 53"
    ],
    "application_match": "Smooth antiholomorphic involution is a differentiable Z/2 action on compact smooth manifold; equivariant triangulation gives finite-dimensional G-CW structure. Original scanned theorem visually read; theorem proof not independently reproved.",
    "scope": "Exact original statement opened and hypotheses matched.",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17"
  },
  {
    "key": "Stacks-08J5",
    "file": null,
    "url": "https://stacks.math.columbia.edu/tag/08J5",
    "sha256": null,
    "locators": [
      "Remark 13.12.4"
    ],
    "application_match": "Canonical truncation triangles for any complex in an abelian category.",
    "scope": "Exact original statement opened and hypotheses matched.",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17"
  },
  {
    "key": "Stacks-0FLJ",
    "file": null,
    "url": "https://stacks.math.columbia.edu/tag/0FLJ",
    "sha256": null,
    "locators": [
      "Example 20.29.3"
    ],
    "application_match": "Hypercohomology spectral sequence and bounded-below convergence; cohomological d2 indexing.",
    "scope": "Exact original statement opened and hypotheses matched.",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17"
  },
  {
    "key": "Stacks-0F16",
    "file": null,
    "url": "https://stacks.math.columbia.edu/tag/0F16",
    "sha256": null,
    "locators": [
      "Lemma 21.26.1"
    ],
    "application_match": "Conditional MV triangle: comparison map must be an isomorphism. Candidate proves it for the two-open cover by degreewise exact flabby Cech sequence.",
    "scope": "Exact original statement opened and hypotheses matched.",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17"
  },
  {
    "key": "Stacks-012K",
    "file": null,
    "url": "https://stacks.math.columbia.edu/tag/012K",
    "sha256": null,
    "locators": [
      "Section 12.24, equations and Lemma 12.24.2"
    ],
    "application_match": "Exact filtered-complex dr representative formula.",
    "scope": "Exact original statement opened and hypotheses matched.",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17"
  },
  {
    "key": "Stacks-0FKU",
    "file": null,
    "url": "https://stacks.math.columbia.edu/tag/0FKU",
    "sha256": null,
    "locators": [
      "Section 20.31, Lemmas 20.31.1–3 and Remark 20.31.2"
    ],
    "application_match": "Derived cup product, its naive-complex comparison and functoriality.",
    "scope": "Exact original statement opened and hypotheses matched.",
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "effort": "Pro",
    "date": "2026-11-17"
  }
]
```

## Hourly checkpoints and retained history

The checkpoint schedule begins at 23:47 UTC on 16 November 2026. Checkpoint 01 was saved at the first hourly boundary, 00:47 UTC on 17 November. Later checkpoints use new consecutive numbers and are never overwritten. Every checkpoint is a complete ZIP of the deliverables and work records written by that boundary; supplied source archives and their extracted copies are excluded. The final package retains the checkpoint files or an exact older version of every superseded passage, with a path-and-hash retention manifest. The source-extraction duplicate removed from the authored work directory is listed as supplied material, not an omitted proof.

The three-hour progress check falls at 02:47 UTC on 17 November, with hourly checks thereafter. Writing or checking the three papers moves the principal task; optional extensions or polishing after a paper is finished do not.
