INCOMPLETE

| Item | Outcome | Exact scope |
|---|---|---|
| A.1 | Proved | Proper nodal plumbing; central fibre exactly Q. |
| A.2 | Partial | Two joint-flat minimal models proved; unrestricted subdivisions and all their normalized components remain open (A.2.3). |
| A.3(i–ii) | Refuted | No smooth proper-flat Engel filling with central fibre Q, even without a map to B; virtual Euler number 0. |
| A.3(iii) | Refuted | Horizontal blow-ups give infinitely many smooth reduced-normal-crossings fillings. |
| A.4 | Partial; minimal cases independently audited | Integral topology and monodromy for Q and the two minimal models; all unrestricted refinements remain open (A.4.5). |
| B.1 | Corrected and proved locally | Product assertion false; genuine semiabelian local fillings and deck actions. |
| B.2 | Partial | n+1 joint-flat reduced refinements after u=r^n; unrestricted subdivisions remain open (B.2.2). |
| B.3 | Stated gluing refuted; corrected construction open | Component rotations contradict the prescribed cusp; the split elliptic genus-three-cover repair fails its exact trace condition; a nonsplit unramified genus-one torsor with the required cyclic lift exists, but its threefold cusp comparison remains open. |
| B.4 | Open | No global descended resolution or full minimal-exponent theorem constructed. |
| B.5 | Open globally | No topology assigned to an unconstructed central fibre. |
| C.1 | Partial | Clutching, orientations and mapping torus proved; numerical class open. |
| C.2 | Partial | Spin-c formula proved; actual filling numbers open. |
| C.3 | Partial | Circle action and explicit closing cocycle proved; numerical class open. |
| C.4 | Structural assertions proved | Twist independence and conjugation; numerical value unknown. |
| D.1 | Proved | Even fibrewise-isomorphic proper flat extensions are excluded. |
| D.2 | Corrected and proved | Lead9 false; nonseparation, reflection and foliation determined. |
| D.3 | Proved | Every local Chabauty limit classified and realized. |
| D.4 | Proved | Every supercritical level is one nested C1 Jordan curve; exact regular crossing at t=0; complete interval and analytic nonvanishing certificate. |
| E.1 | Proved | Dictionary, full sufficiency, count and parameter dependence. |
| E.2 | Partial | Local deformation theory and irreducible-family separation proved; arbitrary chains open. |
| E.3 | Proved as specified | Chartwise analytic foundations and five historical proofs audited. |
| E.4 | Proved | All19701 boxes certified independently with Arb; analytic constants rederived. |
| E.5 | Corrected and proved on source domain | III* and ranks1,1,2; exact classification on the specified logarithmic continuation. |
| Lead1 | Corrected and strengthened | Local smooth-zero Euler value1, not0; integrated contribution0. |
| Lead2 | Proved in stated minimal category | Global nodal plumbing and two minimal untwisted refinements. |
| Lead3 | Refuted as worded | Exact-Q smoothing and unrestricted uniqueness false. |
| Lead4 | Product claim false | Nonproduct local replacement supplied. |
| Lead5 | Proposed gluing false | Corrected cusp and global filling still required. |
| Lead6 | Formula proved | Its geometric numerical application remains open. |
| Lead7 | Partial | Explicit shear and closing maps; smooth class unresolved. |
| Lead8 | Proved | Stronger fibrewise statement. |
| Lead9 | False | Explicit quadratic nonseparation counterexample. |

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 15 November2026. No human verification or priority is claimed.

The detailed section reports below record source reading, computations, corrections, exact limits and attempted approaches. They are incorporated without treating a local or conditional result as completion of a global prompt item. The complete statement registry is S6_02_PUSH_results.csv.

## Execution and retention

The initial workspace interruption resolved within the retry period. Recovery and safe extraction were recorded at 2026-11-15 12:38:56 UTC. The first hourly checkpoint was saved at approximately 13:39 UTC, with its exact name, digest and durable identifier in checkpoints.md. The next hourly deadline is 14:38:56 UTC. Inputs are excluded. Every checkpoint uses a new incrementing filename and is never overwritten.

The initial compiler failed because the system lacked LuaLaTeX formats and usable font maps. An isolated reproducible runtime was prepared without changing system directories. Source syntax errors and compiler logs are retained. A failed compiler PDF is a temporary byproduct, not a delivered PDF. Draft01 had two overfull horizontal boxes above 2pt (14.53073pt and 10.80035pt); the formulas were split. Draft03 and draft04 each passed all four LuaLaTeX/BibTeX stages with zero overfull boxes. Draft03 was rendered at eleven pages spread through its 54 pages; the contact sheet and first-page conventions were visually inspected. Draft04 additionally verifies that every required convention fits on the first page. Draft09 passed all four compilation stages with zero overfull boxes and no unresolved references, citations or rerun warnings in the final log. It includes the torsor construction and the computed untwisted coboundary. An initial attempt to render during compilation encountered a transient incomplete PDF; that failed log is retained and a fresh render was made after compilation completed. Draft09 was rendered at eleven representative pages of its 69 pages (1,2,3,11,12,20,30,40,50,59,69); the contact sheet and page12 were visually inspected. The separate C.3.7 cusp-orbit proof and registry are included as sources but await insertion into the next PDF revision.

External copyrighted PDFs and private OCR extracts are not republished. Search evidence retains source metadata, URLs and source references; full retrieved page bodies are omitted. This preserves the source audit without redistributing the papers. Runtime downloads and caches are reproducible build dependencies.

No checkpointed mathematical passage will be silently removed. A final retention record will identify every superseded passage and its replacement.



---

## Detailed record: AB_push_report.md

INCOMPLETE

# A/B outcome table

This working section is AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). It makes no priority claim. The local constructions and refutations below are proved; the corrected global S6 filling has not been constructed. Work on that missing construction continues.

| Prompt item | Status and result | Proof |
|---|---|---|
| A.1 | Proved. Global proper flat nodal plumbing, the two-parameter fan and period action, proper discontinuity via the unfolded plumbing, and the exact contracted diagonal curve. | A.1.1–A.1.2 |
| A.2 | Open in its literal unrestricted scope. Two minimal/joint-flat reduced models are completely constructed and classified. The unrestricted two-model assertion is false: infinitely many further invariant smooth refinements exist; allowing nonreduced central divisors enlarges the class further. | A.2.1–A.2.3 |
| A.3(i) | Refuted. No proper flat filling of Engel X(u) with central fibre exactly Q exists over B times the disc. | A.3.1–A.3.2 |
| A.3(ii) | Refuted more strongly without any map to B: every smooth proper-flat deformation of Q has Euler number zero, while Engel X(u) has Euler number two. | A.3.1–A.3.2 |
| A.3(iii) | Refuted. Explicit horizontal blow-ups give arbitrarily many smooth reduced-NC fillings, still jointly flat over B times the disc. | A.3.3 |
| A.4 | Open for every arbitrary refinement in A.2.3. Proved for Q and the two minimal models: torsion-free integral homology, fundamental groups, Euler numbers, nearby functions and integral monodromy. Classical Kahler Clemens–Schmid hypotheses fail. | A.4.1–A.4.5 |
| B.1 | Product claim refuted. The corrected non-product root filling, explicit deck extensions, all fixed-point checks, quotient flatness/properness, multiplicities and normal characters are proved. | B.1.1–B.1.2 |
| B.2 | Open for arbitrary additional refinements. Proved for the plain base-changed untwisted cusp fan with joint flatness and reduced centre: 13 models at u=r^12 and 3 at u=w^2; cusp component monodromy is trivial. | B.2.1–B.2.2 |
| B.3 | Lead 5's specified gluing is refuted by a component-cover obstruction. A corrected cusp needs rotation −1 and a genus-three component cover. Cyclic fractional-period repairs and the split ruled-normalization trace construction are ruled out under their explicit hypotheses. A nonsplit everywhere-locally-trivial genus-one torsor with the required affine deck relation exists. Its threefold cusp gluing and smoothing, hence a corrected global filling, remain open. | B.3.1–B.3.6; B.4.1 |
| B.4 | Open. Descent and the minimum semistable exponent for an alternative global model remain unproved. | B.4.1 |
| B.5 | Open. Central topology cannot be assigned before a corrected global model exists. | B.5.1 |
| Lead 1 | Refuted pointwise and corrected: the nearby Euler function is 1 on the smooth part of S_infinity as well as its node; its integral on C* is 0. The stronger no-Q result requires no leading-section assumption. | A.3.1–A.3.2; A.4.3 |
| Lead 2 | Proved for the fan, global nodal quotient and two minimal refinements; unrestricted uniqueness is not a valid conclusion. | A.1.1–A.2.2 |
| Lead 3 | Refuted as a conjunction: the no-Q assertion is true even without B, but unrestricted two-model uniqueness is false. | A.3.2–A.3.3 |
| Lead 4 | Refuted as stated because the product fails generically. Finite-action and semistable-quotient conclusions hold for the corrected semiabelian model. | B.1.1–B.1.2 |
| Lead 5 | Refuted for the exact prescribed pieces: their component permutations violate the fundamental-group relation. This does not refute every possible corrected cusp construction. | B.3.1 |

## Main question reached

The precise Q in Engel's Conjecture 8.2 cannot be the limit of the untwisted family in any proper flat holomorphic filling with smooth nearby fibre. Its virtual Euler number is zero, independently of any elliptic-fibration map. The direct plumbing constructs the nodal alternative with Euler number one; two minimal crepant subdivisions construct smooth-total-space semistable alternatives with a specified blow-up and small resolution as normalization. Their nearby fibres are the actual untwisted X(u).

For the S6 family, the finite-place semistable construction exists, but the proposed global assembly is inconsistent. Its central cycle would define a degree-12 component cover over the three-punctured base. The finite monodromies rotate by +4 and −3; the plain cusp has identity permutation. Their product cannot be identity, even after reversing either local labelling. A different cusp model is therefore necessary.

The necessary component curve has the explicit model b³=a⁴+1. Its pulled-back elliptic surface is Y²=X³−3bX+2a². Three explicit sections give the full integral Mordell–Weil group; an integral Néron–Severi determinant and component-height congruences prove that its twelve-fold deck trace image is exactly 12ZP. Thus no section has trace6P, excluding the split ruled-normalization repair. The full NS determinant is−32. Boundary_d independently checked the geometric and lattice trace proof.

The nonsplit alternative can be taken further: the nonzero class6P in the cyclic cohomology quotient has an everywhere-unramified invariant genus-one torsor preimage. Hochschild–Serre gives a generic preimage; local norm calculations and Ogg–Shafarevich localization remove its ramification. Its projective genus-one surface has an affine deck liftA satisfyingA¹²=t6P. This supplies an existence result for a possible normalization base. It supplies no normal line bundles, corrected threefold cusp chart, or smoothing of that chart to the actual S6 family.

## Geometry, topology and independent checks

R has Betti numbers (1,0,11,0,11,0,1); each modified normalization R' has (1,0,12,0,12,0,1). Both are simply connected. Q has free homology with Betti numbers (1,1,8,7,10,0,1), fundamental group Z and Euler number 12. Each minimal corrected central fibre has free homology with Betti numbers (1,1,9,7,11,0,1), fundamental group Z and Euler number 14. Their dual complex is a circle.

The untwisted X(u) has free homology with Betti numbers (1,1,8,14,8,1,1). For the positive u-circle, N=T−I acts only on H3, has square zero and rank six. Its nonzero Smith entries are 1,1,1,1,1,11. The calculation uses the unimodular rational-elliptic-surface lattice, the primitive classes F, P−O and 6P−O−3F, and the Thom/Gysin/Mayer–Vietoris sequences of the constructed semistable model. The relevant rank-two negative lattice has determinant 11.

The D agent independently reviewed the analytic virtual Euler argument, branch K-class, compact core/node construction, normalization blow-up charts and component-cover obstruction. The root agent reviewed the A.4 ranks and lattice discriminant. These are independent AI checks, not human refereeing. The analytic proof cites Levy's perfect-complex comparison and Łojasiewicz's compatible triangulation; the algebraic Fantechi–Göttsche theorem is not used as an unproved analytic extension.

## Reading and literature status

Read: the full prompt; Engel's source Sections 2, 3, 8; the previous return's AB and E sections; the relevant original period/deck formulas; and the supplied review's degeneration leads. R8's line bundle and inverse lift, R10's local equation/pinching, and R1/R11's finite-action formulas were checked at use. Finite covariance identities were recomputed from the matrices.

Primary-source details, search strings and limits are in `evidence/ab_push_search_log.md`. Opened texts include Mumford (1972), Engel–de Gaay Fortman–Schreieder (2507.15695v3), Fantechi–Göttsche (2010), Łojasiewicz (1964), Levy (2008), the full Alexeev–Nakamura primary PDF, the relevant theorems of the author-hosted Schröer–Siebert PDF, Schnell's analytic Néron-model paper, Kamenova's torus-degeneration manuscript, and Shioda's original Mordell–Weil-lattice paper. The polarized, Kähler or positive-Chern hypotheses of the comparison texts are recorded rather than silently imported. The supplied AI review had proposed the prism and two normalizations. No novelty is claimed for proving those proposed constructions, the virtual Euler method, or its application here.

## Exact computation record

| Program | Purpose | Saved output |
|---|---|---|
| `ab_push_fan.py` | Six prism triangulations; two periodic choices with a fixed bottom. | `.out`, `.json` |
| `ab_push_local_checks.py` | Character/ray pairings, local charts, section 2P, virtual Euler polynomial, node generization and boundary maps. | `.out`, `.json` |
| `ab_push_monodromy.py` | E8 realization, translation isometry, integral kernels/quotients and Smith form. | `.out`, `.json` |
| `ab_push_order_sections.py` | One-time section-order repair. | `.out` |
| `ab_push_finite_decks.py` | Period covariance, shifts and all powers, peripheral contradiction and conditional genus-three cover. | `.out`, `.json` |
| `ab_push_basechange_fan.py` | All 3 and 13 bridge fans: determinants, exact intersections, volumes and periodicity. | `.out`, `.json` |
| `ab_push_cusp_root_repair.py` | Exact obstruction to the specified fractional-period cyclic-root repair, including all tested residues for d≤60. | `.out`, `.json` |
| `ab_push_trace_sections.py` | Exact section ansatz, discriminant, deck orbit, collinearity and elliptic trace. | `.out`, `.json` |
| `ab_push_trace_obstruction.py` | Local infinity expansions, height and integral NS matrices, saturation index, torsion and all trace-obstruction congruences. | `.out`, `.json` |
| `ab_push_torsor_cocycles.py` | All 1,728 cyclic carry-cocycle identities, its order-two class, and the three local norm/component algebra checks. | `.out`, `.json` |
| `ab_push_catalogue.py` | Statement ledger with the required eight columns. | `.out` |

All mathematical computations are exact integer/rational or symbolic calculations. The early local-check failure and its correction from SymPy Poly to `as_expr` are preserved in `ab_push_local_checks_initial_failure.txt`. Two text patches failed validation before modifying files (a missing patch-line prefix; duplicate operations on a report filename); both were reapplied in valid smaller pieces. These were editing failures, not failed mathematical tests. The ordering script is a historical one-time operation and should not be rerun after the text has already been reordered.

## Corrections to supplied material

Lead 1 confuses the pointwise Euler function with its integral on C*. Lead 3's uniqueness needs the minimal/joint-flat toroidal restriction and is false even for joint-flat families if arbitrary horizontal blow-ups are allowed. Lead 4 confuses a torsion specialization with a generically non-torsion line bundle. The second finite component shift is −3 in the fixed orientation. Lead 5 omits a nonextendable overlap; component permutations already contradict its gluing. R2's H1 vanishing is not a theorem about extension across r=0.

The contracted cusp diagonal has direction e1−e2. It differs from the e2-direction curve fixed by Aut(C*). The base-changed minimal cusp fan has n+1 bridge choices, not only the two endpoint base changes.

## Unfinished work and approaches attempted

The main missing step is a cusp degeneration compatible with the finite component shifts and the actual two-parameter translation cocycle. The naive product and plain-cusp gluing are refuted. The corrected finite root models and untwisted fans exist, but none has the required cusp component rotation.

A polarized multivariable Mumford theorem cannot simply be applied because the period units need not satisfy its symmetry hypothesis. Direct compact plumbing proves the untwisted case instead. R2's fixed-parameter cohomology vanishing supplies no boundary control for the overlap exponential involving log(s)log(r). The degree-12 cyclic component cover with ramification (3,4,12) exists as a curve, but does not construct a central threefold or smoothing. Schröer–Siebert's Hopf-normalization degenerations smooth to primary Kodaira surfaces with positive Chern class; that feature prevents a direct application to these torus fibres. Schnell's analytic Néron comparison assumes polarizability, and Kamenova's result assumes a Kähler total space. Neither proves intrinsicness of the component torsor in the present analytic setting.

The cyclic cusp-root fractional-period repair fails because a nonzero r-component shift forces nonreduced q-fibres, whereas the given general family has reduced Mumford fibres. The alternative split ruled normalization fails because trace6P is absent from the explicitly computed section group over the necessary genus-three cover. A nontrivial genus-one torsor with precisely that affine descent obstruction now exists by B.3.6, even with trivial local torsor classes. Tsen's theorem does not assert that a genus-one torsor has a point; the torsor route is a genuine remaining possibility. The next step is to determine its normal line bundle and affine action at the I12 fibre, then construct a cusp chart with the required punctured-family comparison. A bare pinching of two disjoint sections would still have a dual-circle obstruction, so the cusp must contribute additional geometry.

The mu6 action, fixed loci, quotient resolution, least base-change exponent, global central homology and the intersection numbers needed for Eells–Kuiper remain unproved. No values are assigned. A next construction must give a modified cusp fan or non-toric chart carrying the required component rotation, prove that its punctured restriction is the actual S6 family, and exhibit its finite-place overlap maps before properness or topology is asserted.


---

## Detailed record: C_push_report.md

## C: established comparisons and unresolved value

The mapping-torus connected-sum comparison is proved with the positive-loop convention and its boundary orientation. Both spin structures give the same Eells–Kuiper value. A concrete positive generator has Euler class 1, p1=6, p1²=36, signature 1 and mu=1/28.

Lead 6's spin-c coefficients are correct when the boundary determinant trivialization induces the spin structure used in the comparison. The formula is derived by eliminating p2 between the spin-c Dirac index and the signature theorem, and checked against Crowley–Nordström's normalization in exact symbolic arithmetic. H² through H⁵ of the mapping torus vanish; the p1 lift is unique rationally, the c1 lift need not be unique, and the displayed numbers are independent of that ambiguity.

The circle action and the local shear can be verified, but a global scalar-gauge isotopy is invalid: the primitive gamma coordinate on a regular torus cannot extend to the simply connected sphere. Furthermore all 28 sphere mapping classes possess representatives for a semifree circle action with fixed S². Thus that equivariance alone cannot decide the residue. Sixfold base change leaves an explicit order-two ambiguity {0,14}.

The class is unchanged by the admissible sphere twist data via the parameter-holomorphic comparison maps in E.1.3. The antiholomorphic involution reverses both fibre orientation and loop direction; it imposes no order-two constraint.

The actual element [Phi] has NOT been computed. No characteristic numbers of an unconstructed filling are claimed. The geometric route requires the full intersection form and Chern classes of an actual descended resolution. The twist route requires an identification of the global correction cocycle with an exotic-diffeomorphism class; local shear and circle fixed-point data do not supply this. These remain unfinished parts C.1–C.3, and the numeric portion of C.4. The file records them as Open, not as values or completed reductions.

Sources opened: Eells–Kuiper (1962), §3 and §6, formula (11), bundle calculations (12)–(13); Kervaire–Milnor (1963), primary pages 504–505, Theorem 1.1, the table and Lemma 2.1, plus the bP8 order calculation; Poénaru (1971), Theorem 1 and Corollary 1, page156; Crowley–Nordström (2020), Lemma 2.1 and equation (2.1); Durán–Rigas (2007 preprint / 2009 publication), Theorem 2.1 and §3.2. The original Cerf1970 scan was initially too large for web extraction but subsequently downloaded successfully; its primary page8, Théorème0 and Corollaires1–2, was read and visually inspected. The Γ4=0 book is bibliographically verified but not opened; it is not substituted for the dimension-six theorem. The primary downloads, metadata-only review output, and rendering commands are recorded in code/c_fetch_primary.py, code/c_review_primary.py and code/c_render_primary.py and their outputs. The scans and private text extracts are not republished.


---

## Detailed record: D_push_report.md

# Part D working report

| Prompt item | Statements | Outcome |
|---|---|---|
| D.1; Lead 8 | D.1.1–D.1.3 | Proved: the modular invariant has a natural boundary; every proposed flat proper extension, including fibrewise-isomorphic extensions, is impossible. |
| D.2; Lead 9 | D.2.1–D.2.4 | Lead 9 false: second-order escaping periods also identify the imaginary transverse direction. The fixed-parameter total-space Hausdorff reflection has a circle (rational a) or a point (irrational a) at the centre. |
| D.3 | D.3.1–D.3.2 | All local Chabauty limits classified by primitive sublattices and real homomorphisms; no path-independent local limit. |
| D.4 | D.4.1–D.4.8 | Proved: every supercritical degeneracy locus is one nested C1 Jordan curve, analytic except possibly at its exact regular t=0 crossing; no singular coarse levels. Small-height shape, both complex-manifold regions, vanishing lattice covolume, and rank-three group closures are determined. D.4.6 explicitly records and supersedes its earlier Open status. |

## Sources read and exact inherited steps checked

Read the complete supplied prompt. Read the return's AB.tex A.1.1 canonical evaluation calculation and A.4.1 full translation-lattice Albanese computation; CD.tex C.1–C.3, including the local theta-polydisc calculation. The canonical evaluation gives h0(K^-1)=1 and divisor 2S2. The Albanese lattice requires the half-period translations, not merely the fixed eigenspace. The local calculation supplies an analytic coordinate h=mu-(1-tau)/2, a nonzero derivative of e2, and log N=log sqrt2-(pi/2)|h|²+O(|h|⁴); the coefficients needed below have been rederived.

Opened Buchdahl (1999), Theorem 11, pp. 296–297, from the original journal PDF; Grauert (1960), §6 Hauptsatz I and §7 Sätze 1–2 (the last is not used after the erratum check), from the original journal PDF; Cornulier's author PDF, Theorem 3.1 and its proof, pp. 10–11. The final direct-image argument in D.1 proves base change over the smooth base curve by the long exact cohomology sequence and the closed discrete torsion support of R1π_*L; it does not invoke the originally stated generic base-change theorem.

## Corrections

An initial draft cited Grauert (1960), §7 Satz 2 for a closed analytic base-change exceptional set. The foundations audit found that Grauert's 1963 erratum corrects precisely this assertion. The final proof removes this citation: coherence alone plus 0→L --t→L→i_*L_b→0 yields the exact canonical base-change sequence, and the torsion of the coherent R1π_*L on a smooth curve has closed discrete support. The mathematical theorem remains supported by the repaired argument.

Lead 8's outline becomes a proof only after removing the proper images of the nonsmooth loci, then the base-change exceptional set, then the reduced anticanonical divisor's singular and critical loci. Each exclusion is closed discrete in its then-current open curve; the final complement is at most countable, sufficient to leave a boundary-circle point in an open good locus. A global closed-discrete-union assertion is unnecessary and has been removed. The latter reduction avoids treating the nonreduced divisor 2S2 as a smooth surface. The fibrewise-isomorphic variant needs no family isomorphism or Kuranishi calculation.

Lead 9's first-order period direction is correct but its conclusion is false. For a=0, h=1/n and the integral vector n²(gamma+3u−3w)−6n w+3n delta, the period tends to (eta,xi)=(0,−3i). This is outside the asserted moving complex line modulo the central period group. The overlooked scale is n²: the quadratic term survives after the linear moving period has been cancelled. Exact model arithmetic is in code/d_push_exact.py. The actual analytic period differs by O(n^-2), proved in D.2.1. The central fibre's own Hausdorffization, the leaf-space Hausdorffization and the Hausdorffization of the entire root family are three different objects.

## Computation record

`d_push_exact.py` uses exact SymPy arithmetic to check the transformed period determinant, the entire dual-lattice formula, the cancellation responsible for the quadratic degeneration, the counterexample lattice vector, the theta-derivative constants and the rational central-circle period. Output is `d_push_exact.out`. An initial expected determinant sign was wrong; the failed assertion and correction are preserved in `d_push_exact_initial_error.out`. No theorem rests on floating-point arithmetic. `d_push_numeric.py` evaluates the equianharmonic crossing height in 110-digit mpmath arithmetic by two distinct expressions (theta series divided by eta, and the cancelled theta/eta product); both give 1.848362329764999227374945515886084283435696822219612834750098356396585750079055814438, differing by 6.6530623e-111. Equality with the proposed closed form was not inferred from these numerical comparisons; it is now proved independently by D.4.5. The two methods share arbitrary-precision arithmetic but do not share the expression being summed.

## Literature search record

Queries run on 15 November 2026: "Buchdahl even first Betti number compact complex surfaces Kähler 1999 pdf"; "Chabauty topology Pontryagin duality annihilator closed subgroups R n continuity"; "Grauert 1960 Ein Theorem analytischen Garbentheorie proper direct image theorem pdf"; "Remmert proper mapping theorem Satz 1957 Holomorphe und meromorphe Abbildungen komplexer Räume"; "Chabauty Pontryagin annihilator homeomorphism Cornulier theorem pdf"; "complex structures S6 boundary Albanese natural boundary 2026 Engel Alpoge". The last search found Engel's preprint and contemporary seminars, but no publication establishing the Part-D boundary results. We make no novelty or priority claim. The first-order lead and modular invariant are already in the supplied AI return/review; the correction and deductions here are independent calculations from their periods.

Opened URLs: https://www.numdam.org/article/AIF_1999__49_1_287_0.pdf ; https://www.numdam.org/article/PMIHES_1960__5__5_0.pdf ; https://www.normalesup.org/~cornulier/pontri.pdf . A guessed 1963 erratum PDF URL failed; it is not cited. A Remmert paper surfaced by search concerned compact images and was not used for the proper mapping theorem, which is explicitly stated in Grauert §7 Satz 1.

## Previously open D.4 step, now resolved

The initial proof identified the zero set with the modular-norm level in D.4.2, but superharmonicity and connected sublevel sets did not exclude additional maxima. This gap was recorded as Open in D.4.6 and retained through the earlier checkpoint. The equianharmonic height was first supported numerically and then proved analytically in D.4.5. The subsequent local/cusp and compact interval certificates, followed by C1 level transport, now settle the global gap in D.4.7–D.4.8. No Part-D item remains open.

## Final primary-source verification

The correct Grauert erratum URL https://www.numdam.org/item/PMIHES_1963__16__35_0.pdf was opened and its item 2 on printed p. 36 read: the non-bijectivity locus in original §7 Satz2 need not be closed. This confirms the repair recorded above. Cornulier's publisher PDF https://msp.org/agt/2011/11-4/agt-v11-n4-p06-p.pdf was opened; Theorem3.1 remains numbered 3.1 and its proof is on pp.2017–2018. Bibliographic details: Algebraic & Geometric Topology 11(4), 2007–2035 (2011), DOI 10.2140/agt.2011.11.2007.

## Additional global-level-set approach

The exact modulus derivative is ∂τD=iZ(3Zwp′−2g2)/(4π²wp′), where Z=∂μlogθ1+2πi Imμ/Imτ. The heat-equation derivation is D.4.4. `d_push_gradient.py` checks it against an independent symmetric difference of the product expression at three moduli in 80-digit arithmetic; discrepancies are below 9e-25 at step 1e-12. This check is supporting evidence, not a critical-point certificate. The resulting precise task was determining zeros of both factors away from elliptic ramification; it is now certified below. Searches for "Weierstrass zeros Green function theta norm critical points modular function" and related terms led to Lin–Wang (2010), whose Theorem1.3 and introduction were opened. That result counts critical points in the elliptic-curve variable at fixed modulus, whereas our problem differentiates in modulus; it therefore cannot replace the needed factor analysis. URL: https://www.math.purdue.edu/~eremenko/Pdf/Lin/lin-annals.pdf .


## Exact equianharmonic crossing completed

D.4.5 proves N((2−rho)/3,rho)=3^(1/4) and hence Dpart=−(3/(2π))log48. The proof first determines the zero mean of log N directly from the horizontal average of the Jacobi product. Multiplication by alpha=1+rho has matrix [[1,−1],[1,2]], degree3, and kernel {0,±mu}. The functions log N(alpha z) and the sum of log N(z+v) over this kernel have identical distributional Laplacians. Their difference is harmonic and its mean is zero, so it is identically zero. Taking z→0 gives N(mu)^2=|alpha|=sqrt3. The R3 normalization then supplies the exact crossing height. This is a complete analytic argument, not a numerical conjecture or an assumed closed form for beta. The lattice, mean integral and logarithm coefficients are checked in code/d_push_equianharmonic.py/.out. At that stage the remaining open statement was renumbered D.4.6; its subsequent resolution is explicit. The final Part-D count is17 rows:16 in D_push_results.csv and D.4.7 in its separately maintained CSV. No novelty or priority is claimed.

## Supplemental independent reviews and the closing cocycle

The parent requested independent review of the virtual Euler obstruction and of the mapping-torus orientation. These checks are saved separately in sections/D_referee_AB_C.md, with two primary references in sections/D_referee_references.bib and exact checks in code/d_push_referee.py/.out. Both A.3.1 and A.3.2 validate; the analytic specialization proof was sharpened using the codimension-three singular set in the inverse image of a radial segment. The review also checked the global core/node plumbing, the two normalization modifications and the degree-12 component-cover obstruction for literal Lead5.

The investigation of the proposed monodromy order bound produced an explicit affine lift of R2 and a source comparison with the known v1 lift. Its durable output is the fully proved Proposition C.3.5 in sections/C_closing_cocycle.tex, with a separate registry row. The exact scalar t^4/(t−1)^3 has finite orders4,−3 and cusp order−1; its actual cusp map also has a two-coordinate holomorphic unit representative. The latter distinction prevents the scalar pole from being treated as an intrinsic obstruction to an arbitrary quotient isotopy. Patching the scalar and cusp-unit isotopies remains unproved, and no order bound is asserted. Both the earlier lift and the clean known normalization were checked in code/d_push_monodromy.py/.out and code/d_push_closing.py/.out. The audit trail and corrected intermediate gamma coefficient are retained in sections/D_monodromy_order_note.md.


## Coarse regularity at the exact crossing

D.4.5 also now proves that the coarse function is C¹ at t=0, with Dpart(t)=Dpart(0)+(7/(32π))Re(t)+O(|t|^(4/3)) and Wirtinger derivative tending to7/(64π). The norm is invariant under rho², which fixes mu modulo the lattice, so Z vanishes there. The heat equation gives Z_tau=iP/(4π), Z_bartau=0; Ramanujan gives g2'=3iP²/π. Substitution in D.4.4 and division by t_tau from the cubic modular ramification gives the exact coefficient. Thus the zero level at H0 is a regular C¹ arc tangent to the imaginary axis, not a singular coarse level. The complex modulus derivative vanishes only because t has order-three ramification. The exact coefficient arithmetic was added to d_push_equianharmonic.py. The separate d_push_equianharmonic_crossing.py uses90-digit arithmetic and compares the theta derivative with a finite difference of the product norm at three nearby moduli; discrepancies are below1.2e-34. This is a supporting implementation check, not a numerical proof.

## Completed global critical-factor certificate and level classification

The exploratory `d_push_global_scan.py` evaluates19,922 points with complex128 arithmetic and36 Fourier terms, including499 samples of the circular modular boundary. Its largest wp residual is below3.0e-13; it records358 unsuccessful root-solving starts and is explicitly not a proof. It found no unexpected factor zeros, which motivated the rigorous calculation.

The compact calculation `d_push_global_arb.py` uses the independently certified E.4 root enclosures for the19,701 exact rational rectangles. It independently sums the derivative factors through36 Fourier terms with explicit geometric-moment tail bounds and outward Arb arithmetic at192 bits. Its first complete pass proves18,263 rectangles, assigns1,425 whole closed rectangles to |tau−i|<3/20000, and leaves13 coarse rectangles near rho undecided. The original run and its failures remain in the deliverable. `d_push_global_refine.py` replaces those13 rectangles by67 exact dyadic child rectangles using18 subdivision nodes at depth at most2. It redoes74 strict root contractions, proves56 refined leaves and assigns11 whole leaves to |tau−rho|<1/50. The final cover therefore has18,319 nonvanishing leaves,1,425 i-leaves and11 rho-leaves. The smallest proved absolute lower bounds exceed0.00133357953708 for Z and13.58699524669 for F=3ZP−2g2. The paper uses the weaker exact rational bounds13/10000 and13.

`d_push_global_cover_audit.py` verifies the exact original cover, every subdivision, every local-disc containment, the input hashes, the positivity bounds and the polynomial identity det_R Pi=Im(tau)Im(beta)−6(Im(mu))². Its PASS result is saved as JSON and ordinary output. The original cover has36 omitted rectangles inside the i-disc and174 rectangles strictly outside the modular domain, and its exact area is23/40. Every boundary point is covered; there is no numerical gap between the finite cover and local proofs.

The independent root contribution D.4.7, in sections/D_global_local.tex and code/d_root_gradient_certificate.py, supplies the i-disc, rho-disc and infinite cusp region. Its local-i error is less than0.198862|h| against the leading coefficient pi/2. For every Im(tau)≥2 the q-disc contraction and independent interval0≤1/Im(tau)≤1/2 give |Z|>1.39894 and |F|>127.018. Near rho,400 exact offset rectangles prove derivative closeness to the nonzero complex-linear leading terms. The failed one-square image-inclusion test was preserved and was not called a contraction. Its derivative norm nevertheless is below0.432523 on the fixed root square of radius1/80, giving uniqueness there. The independently checked400 refined root boxes all lie within coordinate distance0.007730605<1/80 of the same centre, so the local analytic root branches glue. These independent checks are code/d_push_rho_branch_audit.py/.out and d_push_rho_containment.py/.out.

The resulting real function f=−Dpart is a proper C1 submersion from the finite plane minus{1} to(H*,infinity). To avoid using a smooth-fibration theorem at a merely C1 point, D.4.8 constructs a smooth vector field with df(V)>0 on each compact height band. Its smooth flow has unique C1 hitting times for each level; this transports the known small Jordan curve to every finite supercritical height. Thus every level is one C1 Jordan curve, real analytic except possibly at the unique regular t=0 crossing. Its interior contains1 and has D>0; its exterior contains the cusp and has D<0. The interiors are nested and exhaust the plane. This closes the earlier Open item D.4.6 rather than leaving the computational evidence as a conjecture.

The additional primary-source search and exact theorem comparisons are in sections/D_global_literature_audit.md. Chen–Kuo–Lin2019 AppendixA verifies the classical derivative identities independently; the fixed-torus and generic-degeneracy theorems of Chen–Fu–Lin2025 do not replace this composite modulus calculation. All added bibliography entries are marked opened. No priority is claimed.


---

## Detailed record: E_push_report.md

INCOMPLETE

| Prompt item | Statements | State reached |
|---|---|---|
| E.1: dictionary, higher-root sufficiency, count, Question 3 | E.1.1–E.1.3 | Proved, including full analytic gluing and holomorphic dependence in the parameter. |
| E.2: tangent cohomology, KS, Kuranishi, miniversality, Question 2 | E.2.1 | Proved for every coprime pair. |
| E.2: local deformation separation | E.2.2 | Proved. |
| E.2: a single irreducible connected analytic family | E.2.3 | Different pairs cannot occur in one such family, even allowing unconstructed intervening members. |
| E.2: arbitrary deformation equivalence, Question 1 | E.2.4 | Unresolved for connected reducible bases and chains through unconstructed smooth members. |
| E.3(i): base change and relative duality | E.3.1 | Derived on actual root charts from opened standard theorems; descent verified. |
| E.3(ii): `p2:thm:kuranishi-aut` | E.3.2 | Complete relative to the constructed family and standard cited theorems; proves identity component, with full group treated separately. |
| E.3(ii): `p2:thm:exact-period` | E.3.2 | Complete; explicit even-shift maps and quadratic strictification checked exactly. |
| E.3(ii): `p2:thm:tangent-cohomology` | E.3.2 | Complete for standard multiplicities; chartwise analytic foundations independently checked. |
| E.3(ii): `p2:thm:intrinsic-fibration` | E.3.2 | Complete; intrinsic pencil is used before the centralizer calculation. |
| E.3(ii): `p2:thm:full-automorphisms` | E.3.2 | Complete; residual integral cusp cocycle and zero-class extension checked. |
| E.3(ii): versions and scope beyond the standard family | E.3.2–E.3.3 | v2 omissions verified textually, without mathematical inference; no general-twist, exact-M, or Parts A–D result found in v1. |
| E.5: source configuration | E.5.1 | Prompt refuted: III* at infinity; two rank-one fibres and one hexagonal rank-two fibre. |
| E.5: matrices, centralizers, fixed and norm groups | E.5.2 | Proved with exact rational/integer computation. |
| E.5: all collars and biholomorphism theorem | E.5.3 | Proved on the source's sufficiently small parameter domain and its specified logarithmic continuation. |

## Scope and attribution

This section is AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). It claims no priority and attributes no result to a person beyond the statements actually read in the cited papers. It is a contribution to the full S6_02_PUSH package, not a complete answer to the whole prompt. E.4 belongs to the root agent and is included in its correct position immediately before E.5.

## Main deductions and corrections

The integral map from the prompt's marking to Viaclovsky's logarithmic-transformation marking is

`PV = [[-2,1,0,1],[-6,0,-1,0],[0,-1,0,0],[-1,0,0,0]]`, with determinant −1.

It sends the fixed vectors to `-u0` and `delta-u1`. Inverting the clockwise generator gives `w1=N0 epsilon-rho0 delta_hat` and `w2=N1 epsilon'-(rho1+N1)delta_hat`. The `N1` correction in the second formula is essential. The reference section has zero cusp-comparison class. This fills the dictionary gap identified in R5 and supplies actual root-disc, middle and cusp maps for sufficiency. For standard sphere twists the parameter is `W=(-1)^s2 w`; the comparisons vary holomorphically locally, and their connected automorphism transitions preserve the smooth monodromy class.

The larger-root calculation is not a formal replacement of 1 by kl in the old vanishing statements. With z=kl, d=3k+4l, the horizontal line is O(d−12z), and O(d−13z) has H1 of dimension one exactly when k>1. Thus logarithmic tangent cohomology is (1,1,1,1) when k>1 and (1,1,0,0) when k=1. The dual residue of the monomial x^(3l−2)y^(k−2) is nonzero at the cusp. It makes the connecting map from H2(K_dP6) onto logarithmic H3 have rank one and gives absolute tangent cohomology (1,1,1,0) in every case. This is the concrete step missing from a naive extension of R4.

The signed canonical growth `s=1/12−1/(3k)−1/(4l)` determines the ordered pair: the reduced fraction `1/12−s=(m+n)/(mn)` recovers the sum and product because m,n are coprime. Cohomology jumping loci plus local miniversality prove separation in any single irreducible analytic family. This is stronger than local separation and weaker than separation under arbitrary chains. The distinction is retained in E.2.4.

For the two-parameter source, the given Weierstrass equation has a III* fibre, not III. The torus degeneration orders are (1,0), (1,0), (1,1), so only the first two nodal values yield rank-one fillings. The source itself says this correctly. The finite norm image is `4Z ell + 2Z delta`; a candidate map with fibre-linear scalar −1 fails its first congruence, and scalar +1 requires an even additive period shift. The explicit even-shift defects `(-h u/2, 0, h u/2, -h w/2)` obey the sphere relation. Their rank-one/rank-two collar regularity is imposed explicitly, rather than inferred solely from membership in a vanishing lattice. The difference bundle on P(1,4) is O⊕O(−1), whose H1 vanishes, completing the gluing.

## What was read and checked

The full prompt was read. Relevant original-return A.1–A.5, B.2–B.4 and root/cusp arguments were compared with the exact matrices and with the source proofs. The logarithmic-transformation source was read for its markings, translation vectors, sphere condition and Questions 1–4. The two-parameter source was read through its local completions, monodromy, topology input, canonical-pencil proof and simultaneous family construction. The relevant deformation/classification sections and appendices of Du–Guo–Kusakabe–Xie v1 were read, including finite root normalization, cusp cup product, direct images, tangent cohomology, complete groupoid KS cocycle, Kuranishi ring argument, exact period maps, all automorphisms and quadratic strictification. The corresponding v2 attachment and version-specific official records were checked. The five requested labels occur only in v1. Their absence in v2 is not used as evidence either for or against the proofs.

The combs source was also checked for a possible route through larger Kuranishi germs. It explicitly distinguishes the smoothed comb constructions from small deformations of the original manifold; it supplies no family joining two of the multiplicity pairs. Consequently it does not close E.2.4.

### Opened standard analytic sources

- Bănică, C., & Stănășilă, O. (1976). *Algebraic methods in the global theory of complex spaces*. Chapter III, Theorem 4.1 (finite free complexes), Theorem 4.10 (canonical base change), and Theorem 4.12(ii) (constant fibre cohomology); Chapter VII, Theorem 4.3 (compact complex Serre duality). [Opened full text](https://djvu.online/file/2hQiOnz8WuoQk).
- Grauert, H. (1960). *Ein Theorem der analytischen Garbentheorie und die Modulräume komplexer Strukturen*. *Publications Mathématiques de l'IHÉS, 5*, 5–64. [Original paper](https://www.numdam.org/article/PMIHES_1960__5__5_0.pdf).
- Grauert, H. (1963). Correction to the preceding paper. *Publications Mathématiques de l'IHÉS, 16*, 35–36. [Correction](https://www.numdam.org/item/PMIHES_1963__16__35_0.pdf). Its warning about the potentially nonclosed exceptional locus of §7 Satz 2 was read explicitly. The proof in E.3.1 uses constant cohomology and the later formulation; the generic-curve route uses rank minors of the finite free complex instead of the erroneous closedness inference.
- Ramis, J.-P., & Ruget, G. (1970). *Complexe dualisant et théorèmes de dualité en géométrie analytique complexe*. *Publications Mathématiques de l'IHÉS, 38*, 77–91. Section 3, Theorem 1 and p. 91, Proposition 2 and complete intersections. [Original paper](https://www.numdam.org/item/PMIHES_1970__38__77_0.pdf).
- Ramis, J.-P., Ruget, G., & Verdier, J.-L. (1971). *Dualité relative en géométrie analytique complexe*. *Inventiones Mathematicae, 13*, 261–283. Introduction equation (1), §1 pp. 264–265, and Proposition 2.1 p. 266. [Opened original full-text transcription](https://www.academia.edu/5435625/Dualit%C3%A9_relative_en_g%C3%A9om%C3%A9trie_analytique_complexe). Publisher PDF access failed; no nonexistent theorem number is assigned to its main displayed identity.
- Porta, M., & Yu, T. Y. (2016). *Higher analytic stacks and GAGA theorems*. *Advances in Mathematics, 302*, 351–409. Theorem 7.4 was opened in the revised paper; official Caltech repository metadata confirms the volume, pages and DOI. [Opened paper](https://archive.ymsc.tsinghua.edu.cn/pacm_download/50/409-higher_analytic_stacks.pdf).

## Literature search record

Searches were run on 15 November 2026 using the exact identifiers 2610.00250v1/v2, 2610.39102 and 2609.33785, paired with Kuranishi, deformation, classification, biholomorphic and parameters. Both search systems were used; recent-source queries used a 90-day filter. Authoritative historical sources were separately searched and opened for their exact statements. Source metadata, URLs and retrieval references are saved as `evidence/E_search1.json` through `E_search17.json`; full copyrighted retrieved page bodies are excluded from the deliverable. Failed publisher and arXiv requests are retained in the source audit rather than silently treated as successful.

The official arXiv record and attachment title for the two-parameter paper agree. Its attachment is dated 26 September; its submission record is 27 September 2026. The exact logarithmic-transform title and online HTML were checked. For Du–Guo–Kusakabe–Xie, the mathematical audit is explicitly an audit of the attached v1 source, with separate version-specific online metadata. These are cited as preprints, not as verified journal publications. No further source settling arbitrary deformation equivalence of the higher multiplicity families was located. This limited search result is not a claim that no such result exists.

## Exact computation records

`code/e_push_exact.py` and `.out` check both changes of marking, all fixed-vector identities, the original centralizer and norm matrices, all cohomology formulas for the 1,965 coprime pairs with k,l≤80, and exact recovery of every such pair from its signed canonical slope. The infinite family is proved by the monomial and coprimality arguments; the finite loop is independent confirmation.

`code/e_push_two_parameter.py` and `.out` check all four cohomological and homological matrices, group relations, rational centralizer bases, fixed and norm groups, Smith and Hermite forms, primitive vanishing lattices, the even-shift root solution and sphere cocycle, all four symbolic period-covariance identities, and the Weierstrass discriminant. No floating arithmetic is used.

`code/e_push_source_audit.py` and `.out` record attachment hashes, label locations and version-scope checks. They also verify the v1 raw even-shift defects, its quadratic strictification, the cusp automorphism residual cocycle, and the cusp cup pairing. The source's two-parameter theorem numbering is extracted from the actual theorem counters. Presence/absence checks are expressly not substitutes for the prose proof audit.

## The remaining E.2 obstruction and attempted routes

1. Direct extension of old root acyclicity fails when k>1. This issue was resolved by the nonzero residue calculation and is not a remaining gap.
2. Local miniversality proves an open fixed-pair locus. It does not establish closedness in the full deformation space. A smooth limiting fibre outside the construction could have a larger, reducible Kuranishi germ.
3. Canonical and anticanonical section growth separates pairs in one irreducible family. It does not separate arbitrary chains: at a new intervening fibre the sections can jump on different branches, so equality of their generic values on one irreducible base cannot be carried through that fibre.
4. Part D's outer-boundary obstruction addresses the finite-radius end of the period disc. It does not rule out a smooth limiting complex manifold at the zero end after some reparameterization.
5. Extending the canonical sections to a putative limit does not prove the pencil remains free of base points. No Kähler positivity is available on the total threefold. The next mathematical step would have to exclude such a base-pointed limiting pencil, establish persistence of the complete torus fibration at every smooth boundary, or find a deformation invariant on all intervening complex six-spheres. None of these has been proved here.

The parent report must preserve the INCOMPLETE status until this distinction and all of its other remaining items are resolved. The section is not being represented as a completed solution of Question 1.


---

## Detailed record: E4_push_report.md

## E.4: completed independent certificate

All 19,701 boxes passed a new 192-bit Arb/acb implementation through python-flint 0.9.0. Only exact rational box endpoints were reused. No mpmath import, old radius, old preconditioner, old root, or old interval routine enters the new proof. The largest certified upper bound is enclosed by 1.999877571767410524070536478244687423578792301873142913 ± 9.26e-56, at zero-based input index 17866. Runtime was 49.0401 seconds. This is a rigorous enclosure, not a sample maximum.

An exact Fraction-based vertical sweep at 438 distinct vertical edges checks all 19,911 leaves: 19,701 norm boxes, 36 local boxes, 174 boxes outside the modular domain. Interiors are disjoint and the exact covered area is 23/40. The entire omitted square lies strictly in the independently treated analytic disc.

The analytic local proof was re-derived with all constants. Independent 256-bit Arb bounds give |G| < 18.372504033, |H| < 0.546229725, d in (10.03,10.04), g2(i)/4 in (47.26,47.30), Rouche lower bound >0.0321759437 and perturbation <0.0307366421, |tau-i|/|h|² <6.123343, |h|² <0.000044338219, and remainder coefficient <4399.024 <5000. The analytic cusp inequalities were also independently evaluated. Together these confirm R3's maximum and radius.

The program initially contained two dead, unreachable expressions while the half-integer theta sum was being entered; they were removed before the final rerun. They had no effect on the results. All operative calculations and final outputs are included. No input files are reproduced.

Literature: Johansson's Arb preprint (arXiv:1611.02831) and the python-flint 0.9.0 arb documentation were opened. This is independent evidence for the supplied return's maximum claim, not a claimed new mathematical result.


---

## Detailed record: root_literature_audit.md

## Root literature and source audit

The audit date is 15 November 2026. The attached original manuscript and attached arXiv versions are treated as mathematical inputs, not as verified authorities. Source-specific comparisons occur in the paper. No result is claimed to have priority on the basis of a search failing to find it.

### Smooth monodromy and characteristic numbers

Searches used the titles of Eells–Kuiper, Kervaire–Milnor and Cerf, and combinations of “mapping torus”, “homotopy sphere”, “spin-c Eells-Kuiper”, “equivariant diffeomorphism”, “semifree circle action” and “Blakers-Massey”. The primary scans of Eells–Kuiper (1962), Kervaire–Milnor (1963), Cerf (1970) and Poénaru (1971) were opened. The paper uses the exact statements and formulas recorded in its Part C and in C_push_report.md. The current arXiv source of Crowley–Nordström's Exotic G2-manifolds was checked for the spin-c normalization. Durán–Rigas, arXiv:0708.1577, §3.2, was read to test and reject the proposed inference from circle equivariance to a small mapping-class order.

The original Cerf1970 scan initially exceeded the web extractor's capacity; an independent local download succeeded, and primary page8 was inspected. The Γ4=0 book was bibliographically verified only and is explicitly marked not opened. It is not cited as the proof of the dimension-six identification. The scripts c_fetch_primary.py, c_review_primary.py and c_render_primary.py preserve the access record while leaving the scans and private OCR outside the deliverable.

Further searches and primary readings on circle actions, orbit knots and lift independence are documented in the C-related section notes and their bibliography. These establish comparison tools. They do not identify the annular twist of this family with an integer Haefliger invariant, and no numerical value of [Phi] is inferred from them.

### New trace obstruction and its limits

Queries included “Shioda On Mordell Weil lattices 1990 theorem 8.6 discriminant formula PDF”, “Oguiso Shioda Mordell Weil lattice rational elliptic surface 1991 pdf”, and the exact phrases “elliptic surface genus 3 I12 Mordell Weil”, “b^3 a^4 Mordell elliptic”, and “y^2=x^3 3b 2a elliptic surface”. The equation-specific searches did not locate the exact trace statement in B.3.4. This absence is not a claim of novelty.

The Rikkyo repository verified the original metadata of Shioda (1990), On the Mordell-Weil lattices, Commentarii Mathematici Universitatis Sancti Pauli39(2),211–240, DOI10.14992/00009994. Its direct PDF endpoint returned429. The primary author-uploaded PDF was then opened successfully at https://www.researchgate.net/profile/Tetsuji-Shioda/publication/247043151_On_the_Mordell-Weil_Lattices/links/5704b7fe08ae13eb88b69184/On-the-Mordell-Weil-Lattices.pdf . Theorems1.3,8.4,8.6 and8.7, Corollary5.3, and equations(8.11),(8.12),(8.20) were checked. The determinant relation follows from the narrow-lattice statement and its finite index.

Schütt and Shioda, Elliptic Surfaces, arXiv:0907.0298v3, was also opened at https://arxiv.org/pdf/0907.0298 . Section11.10 equation(22) explicitly records the determinant relation; Section6.10 gives the Hodge numbers and Corollary6.13 the rank formula. This is corroboration by the originating author, not a substitute for checking the original height theorem. The concrete sections, intersection numbers, local infinity expansions, saturation congruences and trace obstruction in B.3.4 are calculated afresh in the accompanying exact programs.

The obstruction applies to a split elliptic normalization. A genus-one torsor without a section is a separate possibility. The report and statement preserve this distinction. Likewise, the polarized hypotheses in Mumford/Alexeev–Nakamura and the polarizable-variation hypothesis in analytic Néron-model results are not discarded when considering an arbitrary nonpolarized analytic filling.

### Interval arithmetic and boundary levels

The primary Arb paper, Johansson, arXiv:1611.02831, §§2–3, and the official python-flint Arb constructor documentation were opened. The E.4 proof gives its own series, geometric tail bounds and strict contraction argument; only rational rectangle endpoints were imported from the earlier certificate. The exact cover was checked separately with rational arithmetic. The D.4 certificate explicitly depends on these newly certified roots; it does not claim arithmetic independence from them. Its i-neighbourhood proof is analytic, and its rho/cusp code implements its own Fourier series and derivative bounds at256 bits. The compact part uses192-bit Arb enclosures and an exact refinement tree.

The D.4 source comparisons with Lin–Wang, Chen–Kuo–Lin and Chen–Fu–Lin are recorded in D_global_literature_audit.md and integrated into D.4.8. The distinction is between a Green function on a fixed torus and the composite modulus function evaluated at a zero of the Weierstrass function. The precise latter level-set theorem is proved by the included certificates and C1 level transport.

### Citation format and evidence retention

The bibliography uses author–date citations and records opened/not-opened status in every entry. The official CTAN apacite page was checked as an available APA6 format implementation; it is a typesetting source, not a mathematical reference. Web result files in evidence contain metadata and retrieval identifiers only. Full copyrighted page bodies, primary scans and private OCR extracts are not republished.


---

## Detailed record: E_C_attempts_report.md

# Independent attack on the actual smooth monodromy

**State: the residue of the actual six-sphere monodromy in Θ₇ remains uncomputed.** The computations below do not assign the invariant of an untwisted mapping torus to the six-sphere mapping torus. They do not infer an order bound from circle equivariance, from a meromorphic scalar gauge, or from the existence of local quotient trivializations.

## Proven calculations and their scope

1. `C_untwisted_coboundary.tex`, C.2.2–C.2.3, computes the intersection form and a relative Pontryagin square for the **actual** semistable untwisted filling A.2.2. The form has rank two, signature +2, and nonzero Smith factors 1,11. Its nondegenerate quotient is `[[6,1],[1,2]]`; its first Pontryagin covector is `−4(a·F)−28h`; its rational relative square is 4512/11. The formal combination 79/176 is not an Eells–Kuiper value for MΦ. The determinant class restricts nontrivially to this other boundary. The branch self-intersection formula was independently checked by the A/B agent; `e_push_C_attempts.py` reconstructs the lattice independently of the A/B program.
2. The cyclic cover `y^12=t^4/(t−1)^3` is connected, with local deck shifts (4,−3,−1), ramification orders (3,4,12), and genus three. This is the component-label cover already identified in B.3.2. It is not a threefold filling. The same affine curve is the (3,4) torus-knot Milnor fibre after choosing coordinates; this observation does not identify an associated seven-sphere.
3. On the cusp-link logarithm cover, use coordinates `(a,g,u,w,d)` for q-angle and the lattice coordinates γ,u,w,δ. The deck transformation is `(a,g,u,w,d)↦(a+1,g,u,w+u,d−g)`. Naive γ-translation by r has deck defect `−rδ`. Its commuting lift is `(a,g+r,u,w,d−ra)`. At r=1 its endpoint, after removing the full γ period, is the δ-gauge `−a`, of q-degree −1. Thus a loop in quotient γ-translations does not automatically lift to an identity-ended loop on the original cusp link. The δ-circle bundle over `S¹γ×Nil³` has a nonzero mixed Chern class on q-angle × γ. Exact algebra is in `e_push_C_attempts.py` and independently in the D agent's cusp-twist program.

## Orbit-space reduction being developed

Along a real c-path, projection modulo the δ-circle discards Re ζ₂. The projected ordinary period lattice is independent of Re c. In a finite root chart, the c-dependent overlap is a real C* flow with time `(c−c₀) ε_j log|s_j|`; this can be extended by a smooth invariant cutoff which is bounded near the root centre and equals the logarithm on the overlap. The cusp toric charts themselves change by a δ-phase. These chartwise statements admit local equivariant horizontal vector fields; their differences are vertical circle fields, so an invariant partition of unity can produce a global horizontal field. This requires working with actual smooth equivariant maps in the slices; arbitrary maps of a chosen topological quotient need not be smooth at the fixed set.

For h=12, the ordinary closing scalar is `K=t^4/(t−1)^3`. The valid cusp unit is the bounded two-torus unit U in `C_closing_cocycle.tex`, with `U·(γ-deck)=(1,K)`. After projection, its additive logarithm u satisfies `u+vγ=R_log|K|`. Removing a cutoff copy of the unit isotopy and a cutoff real C* flow leaves, on the quotient annulus, translation by `χ(|q|)vγ`, identity at its two ends. This describes the candidate residual quotient twist. The preceding mixed Euler calculation shows why its full lift cannot simply be declared supported in the annulus. The outside gauge and its framing remain part of the global data.

The direct gauge comparison lemma C.3.6 establishes that two **existing smooth equivariant lifts of the same orbit map** have the same mapping class. It does not prove that the orbit twist is isotopic to the identity, nor that every quotient isotopy lifts smoothly through the fixed stratum.

## Cusp orbit topology and why a local spanning ball is unavailable

The D agent independently verified the conductor description used here. The quotient of the normalization dP₆ by the δ-circle is a compact oriented three-manifold Y with two boundary two-spheres, hence `S²×I`. Besides the two fixed divisors it has two isolated toric fixed vertices; their quotients are interior R³ points. Gluing the fixed boundary spheres first gives `S²×S¹`; the remaining four edge intervals form two disjoint circles, each crossing the glued fixed sphere once, which are then identified by the other conductor pairings.

For the full quotient H=W/δ, the normalized conductor has homology H₀=Z, H₁=Z, H₂=Z². The conductor quotient is the fixed S² with two arcs joining its two triple points; it has H₁=Z², H₂=Z. The degree-two map to Y and the conductor quotient has both columns `(1,−1)`. Complex orientations of the two fixed curves give the same generator in H₂(Y), because the two normal circle weights and the two boundary orientations both reverse. The hexagonal loop maps to a commutator of the two arc loops, so its H₁ map is zero. The pushout gives torsion-free homology `(Z,Z²,Z²,Z)` and π₁(H)=Z². The fixed S² is primitive and nonzero in H₂(H). In particular it cannot bound a three-chain, let alone a framed three-ball, in H. Extension of this conclusion from H to a whole cusp orbit neighbourhood additionally uses an equivariant tubular retraction; it is not silently assumed.

The source's rank-three quotient gives a map S⁶→S³ with Seifert multiplicities (3,4). Its ordinary γ-circle is a regular Seifert fibre, the (3,4) torus knot. This identifies an attaching loop but not the transverse framing or a capped Seifert four-manifold for the fixed S³ in the clutching seven-sphere.

## Corrected knot-invariant literature

Takase (2007), §2.1, Corollary 2.6, explicitly corrects a sign error in his 2004 paper. With his orientation convention,

`Ω(F)=−(σ(V)−⟨e(νV)²,[V,∂V]⟩)/8`

for an embedded Seifert four-manifold of `F:S³↪S⁶`. Corollary 2.14 shows that any Haefliger knot admits Seifert surfaces of arbitrary signature, so signature alone cannot determine Ω. Moriyama (2011), Theorem 8.1, independently gives the same formula, and expressly restricts that statement to **embedded** Seifert surfaces. Neither formula can be applied to a conductor quotient or an immersed surface without the appropriate correction.

Moriyama's Theorem 1.2(3) gives a useful alternative. For an actual seven-dimensional quasi-e-cobordism `(Z,V,e)`, with boundary the relevant six-dimensional orbit pair,

`σ(∂(Z,V,e))=Sign(V)−4∫_V γ²`,

where `2ρ*γ=e|S(νV)−e(T_vertical S(νV))`. For a knot in S⁶ the left side is `−8Ω`. The meridian of an e-class is two, whereas the principal Hopf circle bundle has meridian one. This factor of two must be kept in converting circle-bundle data. A doubled principal-circle Euler class need only be a **quasi** e-class; its discrepancy along the fixed set is exactly the self-linking class γ.

Primary PDFs and SHA-256 metadata are retained by `e_push_C_sources.py/.json`. Search/open responses are `E_C_search1.json` through `E_C_search15.json`. ASIII's analytic Riemann–Roch theorem was also inspected visually on original pages 564–565, with page images and local OCR retained. Its compact-complex hypothesis applies to the non-Kähler R⁺.

## Local fixed-set calculation for the untwisted filling

The fixed surfaces in W_A must be disjoint. This is verified directly in its three total-space resolution charts, rather than inferred from the unresolved central fibre. In the conifold chart `ay=zv`, use `a=zA,v=Ay` or `z=aD,y=Dv`, with u unchanged. The circle weights in coordinates `(u,z,A,y)` are `(0,0,+1,−1)` and in `(u,a,D,v)` are `(0,+1,−1,0)`. Their fixed surfaces normalize the nodal curve times the u-disc. They join globally to the horizontal `P¹×D²`. The other chart `u=xb,y=bzv`, in `(x,b,z,v)`, has weights `(+1,−1,0,0)` and fixed surface `x=b=0`, the compact vertical S. On the overlap `a=1/b`, so the two fixed components do not meet.

The compact fixed S has normal weight lines with Chern classes `n=m−F` and `−n`. Conjugating the negative weight converts the scalar normal rank-two bundle to `L_n⊕L_n`; the quotient normal R³ bundle is trivial. Its quasi-e discrepancy has square `γ²=n²=−2`. Thus its local expression `Sign(S)−4γ²=−8−4(−2)` vanishes. The horizontal component has signature zero and scalar-normal determinant zero (the original two weight lines restrict to O(−1), with opposite signs). These are untwisted local contributions. They do not prove that the finite logarithmic transforms preserve the boundary orbit invariant.

The nonsplit torsor constructed in B.3.6 may admit a relative-degree-zero line representing P because the Brauer group of the complex base curve vanishes. A height/Deligne-pairing argument should compute its square as −2; this has been communicated to A/B for verification. Even if established, its A-equivariant structure, the prescribed cusp matching, and a smooth filling with the correct boundary would still be needed.

## Other approaches tried and the precise missing step

- Taking `(MΦ×D²)/S¹` directly gives a cone on CP² along the fixed three-manifold. CP² has nonzero signature, so this is not a smooth eight-dimensional filling obtained by replacing each cone independently. A global fixed-surface cap and its normal data are needed.
- The Gromoll-filtration information in Crowley–Schick (2013), Appendix A, gives a proper subgroup in this dimension, but no membership of this specific Φ has been proved. Fibre preservation or circle equivariance does not supply that membership.
- Free circle actions and their characteristic bordism may provide surgery corrections; however even an empty-fixed-set six-dimensional pair with a nonzero Euler class has characteristic obstructions. Thus it is not valid to assert that modifications in the free region contribute zero merely because they avoid fixed points.
- The regular (3,4) Seifert fibre suggests ±1 surgeries with Brieskorn boundaries Σ(3,4,11) or Σ(3,4,13). Their suspended singularity signatures can be computed, but no comparison map between their handlebodies and the actual cusp-annulus twist has been constructed. Their natural circle fixed sets also differ. No numerical monodromy value is inferred from these examples.
- The determinant eleven in the untwisted intersection form does not justify adjoining a guessed E₈ or other plumbing. The surgery framings and the resulting boundary have to be established before such an intersection completion has meaning for this problem.

## Exact next target

Construct the global capped quotient pair for the annular γ-twist, preserving the circle-bundle class and the fixed normal framing, or construct an actual equivariant smooth cobordism from its mapping torus to a calculable boundary. Then either compute an embedded Seifert normal Euler square or use Moriyama's quasi-e signature formula. At present this comparison, including the finite-root/cusp overlap, is missing. No value, vanishing result, or nontrivial order bound for the actual [Φ] has been established by this attempt.


---

## Detailed record: D_cusp_twist_audit.md

# Cusp-twist investigation: exact progress and unresolved comparison

This is a supplementary research and source audit for Part C and Lead 7. It does not assign a value in `Theta_7`. The complete Part D results are in `D_push.tex`; they are unaffected by the unresolved Part C computation.

## Established comparisons

1. `C_closing_cocycle.tex`, C.3.5, verifies the known even-shift formula against both finite root charts and the full cusp toric filling. For the twelve-unit closing shift the ordinary scalar is `K=t^4/(t-1)^3`, while its cusp representative is a holomorphic two-coordinate torus unit. Their ratio is exactly the gamma deck transformation. The scalar pole alone is therefore not an obstruction to extending the actual map.
2. `C_orbit_lift_comparison.tex`, C.3.6, proves directly that smooth equivariant lifts of the same orbit map differ by an isotopically trivial gauge. It also lifts orbit isotopies supported in the free stratum. This does not supply the missing orbit isotopy.
3. `code/d_push_cusp_twist_linear.py` and its output multiply the prescribed integral monodromy matrices exactly. In the ordered basis `(gamma,u,w,delta)`, the cusp monodromy fixes `w,delta`, sends `u` to `u+w`, and sends `gamma` to `gamma-delta`.

Consequently the orbit collar modulo the delta circle has boundary `S^1_gamma x Nil^3`, where `Nil^3` is the mapping torus of the two-torus shear `u -> u+w`. The principal delta-circle bundle on that collar is nontrivial: its Euler class has evaluation of absolute value one on the cusp-angle/gamma two-torus. For an explicit sign convention use the mapping-torus relation `(theta+1,a,b)~(theta,a,b-a)`, with `a,b` the gamma and delta coordinates. Its covering deck map is `(theta,a,b)->(theta+1,a,b+a)`; the invariant connection `db-theta da` has curvature `-dtheta wedge da`, giving Euler number `-1`. This `theta` orientation is the stated monodromy convention and must not be silently replaced by a positive `q`-loop convention.

This mixed Euler class is the concrete reason that a fractional gamma translation on the orbit collar cannot simply be lifted with identity phase at both ends. A full smooth equivariant lift nevertheless exists for the original monodromy, with its outside gauge. C.3.6 removes the ambiguity only after an orbit map or orbit isotopy has actually been constructed.

## Cusp conductor geometry independently checked

The classification agent computes the conductor pushout. Independent checks made here are:

- On the toric normalization `dP_6`, the delta circle fixes two opposite divisors and also the two toric vertices not incident to them. The latter have normal weights `(1,-1)` and quotient neighbourhood `R^3`; they are not extra boundary components.
- The orbit quotient of the normalization is an oriented three-manifold with two spherical boundary components, identified by the toric argument as `S^2 x I`.
- At a fixed divisor of normal circle weight `+1`, the boundary orientation of the orbit quotient is the complex curve orientation; at weight `-1`, it is the opposite. Thus the two fixed divisors with their complex orientations represent the same class in the quotient's second homology. Both conductor maps have degree `+1` on the resulting fixed sphere.
- Gluing just those two fixed boundary spheres gives an oriented `S^2` bundle over the circle, hence `S^2 x S^1`: the gluing is a holomorphic automorphism of `P^1`, isotopic to the identity. The four remaining toric-edge intervals then form two disjoint embedded circles. Each crosses the glued fixed sphere once, and the other two opposite-side identifications identify these circles with an interchange of their two distinguished vertices.

These observations support the classification agent's pushout calculation `H_*(W/S^1)=(Z,Z^2,Z^2,Z)` and the nonzero primitive class of the fixed `S^2`. They do not prove that this sphere bounds a three-ball in the cusp body. In fact its nonzero homology class excludes a bounding three-chain in the central orbit fibre; transfer of this exclusion to a full cusp neighbourhood requires the stated equivariant deformation-retraction comparison.

## Global structure that may supply the missing framing

Engel's attached source, `background/papers/arXiv_2609.38442_Engel_src/S6.tex`, final remarks following the degeneration conjecture, describes the quotient by the invariant rank-three torus system as `S^3`, Seifert fibred with exceptional multiplicities `(3,4)`. A regular gamma fibre is therefore the regular `(3,4)` torus-knot fibre, with orientations and framing still to be compared to the present cusp collar. This gives a concrete candidate for the global attaching loop; it does not identify the high-dimensional knot produced by the annular twist.

There is a second numerical/geometric match: AB's component cover `b^3=a^4+1` is the affine Milnor fibre of the `(3,4)` plane-curve singularity. Its compactification has genus three and one point at infinity. The split elliptic pullback studied in B.3.4 has `chi(O)=1`, a single `I_12` fibre, and signature `-8`. No map has been constructed that makes this elliptic surface a Seifert four-manifold for the orbit knot. Its signature cannot be substituted into a Haefliger or Eells--Kuiper formula without that construction and the normal Euler-class comparison.

## Exact remaining step

Construct, with the actual finite-root and cusp overlap maps, either:

- an isotopy of the annular gamma orbit twist through maps that lift smoothly, or
- the associated embedded `S^3` in the six-dimensional orbit sphere together with an embedded Seifert four-manifold and its normal Euler class, or
- a projected immersion of that specific knot with its double-linking, Ekholm and Smale data.

The central conductor incidence and the collar monodromy do not supply these framings. Counting its two triple points or its one double circle, or using generic circle equivariance, does not determine a residue in `Z/28`. No order bound is asserted.

## Primary sources opened and the precise use attempted

The bibliographic records are in `D_cusp_twist_references.bib`.

| Source | Material read | Outcome for this problem |
|---|---|---|
| Davis (1982), *Some group actions on homotopy spheres of dimension seven and fifteen*, AJM 104(1), 59–90; https://people.math.osu.edu/davis.12/old_papers/AJM-82.pdf | Introduction, Example 7.14, Proposition 7.15, Corollary 7.16 | Confirms the orbit-knot route and generator examples; does not identify our clutching knot. |
| Fintushel and Pao (1983), *Circle actions on homotopy spheres with codimension 4 fixed point set*, PJM 109(2), 349–362; https://msp.org/pjm/1983/109-2/pjm-v109-n2-p09-p.pdf | Introduction, Propositions 1.1–1.4 | Checks orbit-space smoothing and the scope of the semifree classification; supplies no numerical value here. |
| Haefliger and Salem (1991), *Actions of tori on orbifolds*, AGAG 9(1), 37–59 | Original Theorem 3.1 and Lemma 3.2 facsimile on pp. 5–6 of Karshon's slides below | Equivariance is essential in the general theorem. The printed non-equivariant slice lemma is false. C.3.6 avoids it with a direct proof. Full original paper was not opened. |
| Karshon, *Equivariant orbit preserving diffeomorphisms*, joint work with Schwarz; https://www.fields.utoronto.ca/talk-media/1/23/28/slides.pdf | All 20 slides | Contains the original excerpt, counterexample to its overbroad lemma, and corrected proof outline. No date invented. |
| Karshon and Tolman (2014), GT 18, 669–716; https://msp.org/gt/2014/18-2/gt-v18-n2-p03-s.pdf | Theorem 4.9, p. 690 | Led to the exact orbit-preserving statement; no Hamiltonian structure on `X_c` is assumed. |
| Roseman and Takase (2007), AGT 7, 359–377; https://msp.org/agt/2007/7-1/agt-v7-n1-p17-s.pdf | Theorem 2.1; §§2.2–2.3; Theorem 3.1; beginning of §4 | Provides graphing and an explicit generator construction; a comparison to our annular twist is still missing. |
| Sakai (2015), HHA 17(2), 317–341; https://arxiv.org/pdf/1405.1947 | Theorems 2.5 and 2.11, Corollary 2.7, §3 | Double-point linking determines crossing-change differences, with a separate invariant of the projected immersion. No projection of our knot has been constructed. |
| Gauniyal and Turchin (2026), PEMS 69(4), 1466–1505, https://doi.org/10.1017/S0013091526101485 | Introduction and §4 | The formula requires tangential Smale/Ekholm terms as well as double-linking. In particular a small conductor double-locus count cannot establish vanishing. |

The attempted Springer PDF for Levine (1973), *Semi-free circle actions on spheres*, Inventiones 22, 161–186, https://doi.org/10.1007/BF01392300, redirected to an access page; its theorem was not read or applied. The attempted Schwarz (1980) Numdam PDF was not retrieved within the tool's content limit; no assertion depends on it. The publisher-hosted Sakai PDF returned an access error, so the arXiv author preprint was used.

## Search audit

Queries were run through both search engines where coverage was incomplete. Exact strings included:

```text
"semifree circle" "homotopy spheres" fixed 3 7 spheres
"semi-free" "circle" "7-spheres" fixed
"semifree" "homotopy 7" fixed
"boundary twist" "Haefliger"
"torus twist" "exotic" sphere
"Gromoll" "circle" "Haefliger"
Levine "Semi-free circle actions on spheres" 1973 pdf
"Haefliger" "torus" "twist" diffeomorphism
"boundary twist" "circle action" high dimensional
"Haefliger" "Salem" "Actions of tori on orbifolds" pdf
"Actions of tori on orbifolds" "3.1"
"Levine" "Semi-free circle actions" brandeis pdf
"Haefliger invariant" "torus knot"
"Haefliger invariant" "spinning"
"Haefliger" "Seifert" "circle action" knot
"deform spinning" "S3" "S6"
"Lin–Wang type formula for the Haefliger invariant" Sakai arxiv
"Haefliger" "circle" "torus knot" invariant
"Haefliger invariant" "double point" "linking"
"exotic" "sphere" "torus twist"
"Haefliger" "point pushing"
"diffeomorphism" "S6" "Seifert"
"semifree" "torus knot" spheres
```

No directly applicable theorem identifying this gamma twist with a numbered homotopy sphere was located. This is a record of the searches performed, not a novelty or exhaustive-literature claim.


---

## Detailed record: retention_record.md

## Checkpoint retention record

No checkpointed file or passage is discarded. Unchanged files remain at their original paths; every changed version is retained byte for byte below. The current source supersedes its historical counterpart. A prior Open statement may therefore remain in an archived version even when the current numbered statement has been resolved. The original ZIPs are never modified.

| Checkpoint | Previous file | Retained full version | Current replacement |
|---|---|---|---|
| S6_02_PUSH_checkpoint_01.zip | S6_02_PUSH_paper.aux | retained/checkpoint_01/S6_02_PUSH_paper.aux | S6_02_PUSH_paper.aux |
| S6_02_PUSH_checkpoint_01.zip | S6_02_PUSH_paper.log | retained/checkpoint_01/S6_02_PUSH_paper.log | S6_02_PUSH_paper.log |
| S6_02_PUSH_checkpoint_01.zip | S6_02_PUSH_paper.out | retained/checkpoint_01/S6_02_PUSH_paper.out | S6_02_PUSH_paper.out |
| S6_02_PUSH_checkpoint_01.zip | S6_02_PUSH_paper.tex | retained/checkpoint_01/S6_02_PUSH_paper.tex | S6_02_PUSH_paper.tex |
| S6_02_PUSH_checkpoint_01.zip | S6_02_PUSH_paper.toc | retained/checkpoint_01/S6_02_PUSH_paper.toc | S6_02_PUSH_paper.toc |
| S6_02_PUSH_checkpoint_01.zip | S6_02_PUSH_references.bib | retained/checkpoint_01/S6_02_PUSH_references.bib | S6_02_PUSH_references.bib |
| S6_02_PUSH_checkpoint_01.zip | S6_02_PUSH_report.md | retained/checkpoint_01/S6_02_PUSH_report.md | S6_02_PUSH_report.md |
| S6_02_PUSH_checkpoint_01.zip | S6_02_PUSH_results.csv | retained/checkpoint_01/S6_02_PUSH_results.csv | S6_02_PUSH_results.csv |
| S6_02_PUSH_checkpoint_01.zip | code/ab_push_catalogue.out | retained/checkpoint_01/code/ab_push_catalogue.out | code/ab_push_catalogue.out |
| S6_02_PUSH_checkpoint_01.zip | code/ab_push_catalogue.py | retained/checkpoint_01/code/ab_push_catalogue.py | code/ab_push_catalogue.py |
| S6_02_PUSH_checkpoint_01.zip | code/assemble_records.out | retained/checkpoint_01/code/assemble_records.out | code/assemble_records.out |
| S6_02_PUSH_checkpoint_01.zip | code/assemble_records.py | retained/checkpoint_01/code/assemble_records.py | code/assemble_records.py |
| S6_02_PUSH_checkpoint_01.zip | code/assembly_summary.json | retained/checkpoint_01/code/assembly_summary.json | code/assembly_summary.json |
| S6_02_PUSH_checkpoint_01.zip | code/build_paper.py | retained/checkpoint_01/code/build_paper.py | code/build_paper.py |
| S6_02_PUSH_checkpoint_01.zip | code/d_push_equianharmonic.out | retained/checkpoint_01/code/d_push_equianharmonic.out | code/d_push_equianharmonic.out |
| S6_02_PUSH_checkpoint_01.zip | code/d_push_equianharmonic.py | retained/checkpoint_01/code/d_push_equianharmonic.py | code/d_push_equianharmonic.py |
| S6_02_PUSH_checkpoint_01.zip | code/d_push_registry.out | retained/checkpoint_01/code/d_push_registry.out | code/d_push_registry.out |
| S6_02_PUSH_checkpoint_01.zip | code/d_push_registry.py | retained/checkpoint_01/code/d_push_registry.py | code/d_push_registry.py |
| S6_02_PUSH_checkpoint_01.zip | code/package_checkpoint_01.out | retained/checkpoint_01/code/package_checkpoint_01.out | code/package_checkpoint_01.out |
| S6_02_PUSH_checkpoint_01.zip | code/refresh_report.out | retained/checkpoint_01/code/refresh_report.out | code/refresh_report.out |
| S6_02_PUSH_checkpoint_01.zip | code/refresh_report.py | retained/checkpoint_01/code/refresh_report.py | code/refresh_report.py |
| S6_02_PUSH_checkpoint_01.zip | evidence/ab_push_search_log.md | retained/checkpoint_01/evidence/ab_push_search_log.md | evidence/ab_push_search_log.md |
| S6_02_PUSH_checkpoint_01.zip | sections/AB_push.tex | retained/checkpoint_01/sections/AB_push.tex | sections/AB_push.tex |
| S6_02_PUSH_checkpoint_01.zip | sections/AB_push_references.bib | retained/checkpoint_01/sections/AB_push_references.bib | sections/AB_push_references.bib |
| S6_02_PUSH_checkpoint_01.zip | sections/AB_push_report.md | retained/checkpoint_01/sections/AB_push_report.md | sections/AB_push_report.md |
| S6_02_PUSH_checkpoint_01.zip | sections/AB_push_results.csv | retained/checkpoint_01/sections/AB_push_results.csv | sections/AB_push_results.csv |
| S6_02_PUSH_checkpoint_01.zip | sections/C_push.tex | retained/checkpoint_01/sections/C_push.tex | sections/C_push.tex |
| S6_02_PUSH_checkpoint_01.zip | sections/C_push_report.md | retained/checkpoint_01/sections/C_push_report.md | sections/C_push_report.md |
| S6_02_PUSH_checkpoint_01.zip | sections/D_push.tex | retained/checkpoint_01/sections/D_push.tex | sections/D_push.tex |
| S6_02_PUSH_checkpoint_01.zip | sections/D_push_references.bib | retained/checkpoint_01/sections/D_push_references.bib | sections/D_push_references.bib |
| S6_02_PUSH_checkpoint_01.zip | sections/D_push_report.md | retained/checkpoint_01/sections/D_push_report.md | sections/D_push_report.md |
| S6_02_PUSH_checkpoint_01.zip | sections/D_push_results.csv | retained/checkpoint_01/sections/D_push_results.csv | sections/D_push_results.csv |
| S6_02_PUSH_checkpoint_01.zip | sections/D_referee_AB_C.md | retained/checkpoint_01/sections/D_referee_AB_C.md | sections/D_referee_AB_C.md |
| S6_02_PUSH_checkpoint_01.zip | sections/D_referee_references.bib | retained/checkpoint_01/sections/D_referee_references.bib | sections/D_referee_references.bib |
| S6_02_PUSH_checkpoint_01.zip | sections/E_push_report.md | retained/checkpoint_01/sections/E_push_report.md | sections/E_push_report.md |
| S6_02_PUSH_checkpoint_01.zip | sections/conventions_push.tex | retained/checkpoint_01/sections/conventions_push.tex | sections/conventions_push.tex |

Exact byte counts and SHA256 digests are in code/retention_record.json.
