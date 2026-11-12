| Item | Statements | Outcome | Missing work / exact scope |
| --- | --- | --- | --- |
| A.1 | A.1.1, A.1.2 | (a) | None within the stated prompt scope. |
| A.2 | A.2.1 | (a) | None within the stated prompt scope. |
| A.3 | A.3.1 | (a) | None within the stated prompt scope. |
| A.4 | A.4.1, A.4.2, A.4.3 | (a) | None within the stated prompt scope. |
| A.5 | A.5.1, A.5.2 | (a) | None within the stated prompt scope. |
| B.1 | B.1.1, B.1.2, B.1.3, B.1.4 | (a) | None within the stated prompt scope. |
| B.2 | B.2.1, B.2.2, B.2.3 | (b) | None within the stated prompt scope. |
| B.3 | B.3.1 | (a) | Complete for Viaclovsky’s stated coprime sphere multiplicities and admissible vectors; the comparison gives step 2klZ. |
| B.4 | B.4.1, B.4.2 | (a) | None within the stated prompt scope. |
| C.1 | C.1.1, C.1.2 | (a) | None within the stated prompt scope. |
| C.2 | C.2.1, C.2.2, C.2.3 | (a) | None within the stated prompt scope. |
| C.3 | C.3.1, C.3.2, C.3.3, C.3.4 | (c) — unfinished | Compact replacement across the boundary, including the collapsed order-four neighbourhood, remains unconstructed. The actual rank-three quotient, its separation properties, and the Albanese natural boundary are proved. |
| C.4 | C.4.1 | (a) | None within the stated prompt scope. |
| D.1 | D.1.1, D.1.2, D.1.3, D.1.4, D.1.5, D.1.6, D.1.7 | (b) | None within the stated prompt scope. |
| D.2 | D.2.1, D.2.2, D.2.3 | (a) | None within the stated prompt scope. |
| E.1 | E.1.1, E.1.2, E.1.3, E.1.4, E.1.5 | (c) — unfinished | Equivariant periodic gluing at xy=u*z*v with the prescribed general Mumford resolution and proposed central normalization. |
| E.2 | E.2.1, E.2.2, E.2.3 | (c) — unfinished | Compatible nonreduced finite-fibre neighbourhoods and infinity filling, and descent of the auxiliary base change. Global central topology is therefore uncomputed. The smooth monodromy is reduced to the explicit invariant permitted in the prompt. |
| F.1 | F.1.1, F.1.2 | (a) | None within the stated prompt scope. |
| F.2 | F.2.1, F.2.2, F.2.3 | (b) | None within the stated prompt scope. |
| F.3 | F.3.1, F.3.2, F.3.3 | (a) | None within the stated prompt scope. |

# S6_02_FAMILY research record

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 12 November 2026. No human authorship or priority is claimed for this deliverable. Source authors are named only in citations to their own works.

**This is a partial research package with three unfinished prompt items: C.3, E.1 and E.2.** Every one of the twenty items has numbered mathematics, and each unfinished item contains constructed cases, executed computations, and a specific smallest remaining target. The compact degeneration is not presented as settled.

## Principal mathematical outcomes

For the original retained sphere data, A.1–A.5 prove that the fibration is intrinsic, that every biholomorphism preserves its base, and that `X_c ≅ X_cprime` exactly for `cprime-c ∈ 2Z`. The local cyclic-cover lifts, integral norm obstruction, cusp-stratum maps, collar identities, coherent shift action, and proper family descent are written out. The automorphism group is exactly C*, including its components. Under the declared cusp normalization, the conjugate member is `X_(1-barc)`, so the real locus in the parameter disc is `w=-barw`.

A.5.2 also proves `h^q(X_c,T_Xc)=(1,1,1,0)` and a smooth reduced one-dimensional Kuranishi germ for every admissible retained member. The family is locally miniversal. The calculation uses an actual morphism to the root curve P(3,4), pointwise base change on its finite atlases, a multiplicative cusp resolution, the nonzero gamma class, and the branchwise normal-derivative quotient. The invariant-exponent calculation is independently checked in code. It answers the small-deformation question for the retained (3,4) family.

For all admissible (3,4) discrete data, including arbitrary cusp sections and both fibre-linear signs, the complete invariants are

`(|p|, exp(-pi*i*(c+k2)))`, with `p=12*l0-4*r1-3*r2`.

The proof gives exactly two sphere classes at fixed Engel u, interchanged by a circuit around zero. For coprime sphere multiplicities `(3k,4l)`, B.3.1 gives every norm congruence; the fixed-data shift subgroup is `2klZ`, and fixed u has `2kl` classes in one cycle. The explicit integral marking matrix on the first page fixes the signs in the dictionary.

With `(beta_part+tau)(infinity)=0` and Engel’s reference linearization chosen to be the transported period lift at c=0, the scalar is `lambda0=1` and `u=w^2`. The theta formula for beta is proved from its actual transformation laws. The global maximum is

`M=-(3/pi)*log(6) = -1.71100425815613411418…`, attained only at `t=1`.

Consequently the exact class disc is `0<|w|<216`, and the corresponding quotient parameter disc is `0<|u|<46656`. These values include the declared reference choice; rescaling that reference changes the u radius by the explicit scalar in B.1.4. They are not claimed invariant under such a rescaling.

The maximum proof combines a quantitative analytic neighbourhood of tau=i, an analytic cusp bound for Im(tau)>=2, and a completed outward interval cover of the remaining compact region. The independent partition checker verifies 19,911 exact rational leaves: 19,701 strict norm certificates, 36 local-proof boxes, and 174 exact exclusions outside the modular domain. There are zero pending or undecided boxes. The exact rational area is 23/40. The largest reported squared-norm bound is `9999999982782673130994674616307871/5000000000000000000000000000000000`, strictly less than 2. Thus the numerical exploration has been replaced by a global proof.

Part D gives an exact classification for every smooth fibre through the displayed six-integer Neron–Severi equation. Nonzero isotropic integral classes give the elliptic-quotient locus; negative Pfaffian classes give the abelian locus, with the sign derived from the complex orientation. These explicit countable zero sets determine algebraic dimensions zero, one and two. They are exact equations, not a finite list of exceptional t-values. All compact curves are classified through their actual elliptic-kernel, theta-section, finite-cover, or normalization maps. All irreducible compact surfaces are reduced fibres. Rational curves occur only in W, while ordinary fibres do contain elliptic curves.

Part F determines the monodromy group as an explicit integral central extension and an index-twelve subgroup of the primitive-vector stabilizer (index twenty-four in the line stabilizer). Its Zariski closure and Levi image are proved. Full-domain properness is false: a displayed rational complex structure has an infinite integral unipotent stabilizer. The largest proper-action open set is exactly `psi(delta_hat,J*delta_hat) != 0`. Every admissible period lies in its positive component. The quotient period curve is an injective immersion; adding the two finite punctures gives a proper embedded affine line, and the cusp escapes compact subsets.

## Corrections and dispositions of the proposed leads

| Source / claim | Disposition and exact correction |
| --- | --- |
| Lead 1 | Proved by the exact centralizer and the two integral norm images, including the normalized-cover lift and exact generator commutation. |
| Lead 2 | Proved with the stated finite translations, cusp cocharacter, vanishing H1 of the correction sheaf, and coherent cocycle identity. |
| Lead 3 | Proved, including the precise Albanese moduli and their j-functions. The generic necessity argument has an explicitly countable exceptional set, and the full classification uses the integral norm proof. |
| Lead 4 | Proved for the positive linear part and extended to both signs and arbitrary cusp data. The resulting complete invariant uses absolute p together with the corrected exponential coordinate. |
| Lead 5 | Proved with the explicit branch `exp(2*pi*i*mu0)=-(5+2*sqrt6)`, the zero-of-wp identification, and gluing units `(-a^-1,a^6,-a^-7*w^2)`. Every hexagon automorphism is checked to obtain the abstract surface criterion `cprime-c ∈ Z`. |
| Lead 6 | **False in its unrestricted elliptic-quotient wording.** At t=32/5 the section has exact order four, yet the explicitly admissible member in D.1.3 has a surjection onto E_t with connected elliptic kernel. The four period images under `3*zeta1+4*zeta2` are `(-101*tau,2*tau+2,3,4)` and generate the target lattice. The specified first-coordinate projection has the exact two-point criterion claimed in the workbench. D.1.6 gives the full replacement for arbitrary elliptic quotients. |
| Lead 7 | Proved for the full automorphism group; B.4.2 additionally gives all antiholomorphic maps and the split extended group on the real locus. |
| Engel Remark 8.1 | The fixed-sphere-data family requires the double-cover qualification `u=w^2` for global descent. B.2.3 supplies two independent obstructions to descent over the original u-disc, and constructs the corrected global family and valid local u-families. |
| Engel shift-vector comparison | In the first-page integral marking and declared root orientation, `c -> c+1` gives `(a0,a1) -> (a0-delta/3,a1+delta/4)`. B.2.2 supplies the actual lattice and complex-period comparison maps fixing this sign. |
| Course, cusp-and-compact-threefold §10.2 | For its displayed section `P_*=(0,sqrt2*t^2*(t-1))`, the chart value `Y2=y/t^2` tends to `-sqrt2`. Its component label must be `E_(2,-)`. Both endpoint inverse-Cartan entries equal 4/3, so the height conclusion survives. |
| AC26 Lemma 9.4, orientation comparison | The formal coefficient `eta wedge eta=12 vol` is correct. The displayed period map has real determinant `T*D<0`, so its integral in the complex orientation is -12. D.1.4 gives the exact comparison; it does not call the coefficient identity false. |
| Rank-three boundary quotient | Real rank three of the period matrix does not guarantee a discrete image of Z^4. C.3.1 gives the exact rational-kernel criterion. The quotient is noncompact in the discrete case and non-Hausdorff in the other case. |
| Klingler full-domain proposal | False for the actual monodromy group and the full line parabolic. F.2.1 is a complete exact counterexample; F.2.2 supplies the uniquely largest invariant proper-action open set. |

## Sources actually read

The archive identity check verified all 43 manifest entries, including nine PDFs totalling 329 pages. This count records file identities, not a claim to have read every page. The report sections below state the inspected locations. The original AC26 PDF was extracted and compared with its supplied transcription; page66 was visually inspected for the orientation-sensitive formula. Engel’s initial construction, line-bundle lemma and proof, finite modifications, integral monodromy, and final questions were read directly.

Yang’s Section6.2 and Viaclovsky’s logarithmic-transform Theorem1.1, Questions1.1 and Proposition4.7 were read for their exact hypotheses and comparison maps. The introductions and principal stated results of the two-parameter, combs, Liu–Rollenske, and Wang papers were inspected to delimit the present period system. The attached Duke–Imamoglu theorem and its relation to Eichler–Zagier were read; our required zero and cusp constant are independently derived, and no unopened original Eichler–Zagier text is a premise.

Public searching located arXiv:2610.00250v1 and its later v2. The historical version states the classification and deformation results; the current version omits those sections. We checked the actual v1 argument rather than drawing a conclusion from that version change. A.5.2 gives the written derivation, and `ab_deformation.py` checks its root-character arithmetic and local algebra. The source versions have separate verified bibliography entries. No reason for the deletion and no priority is asserted.

The public search queries, dates and primary URLs are in `evidence/literature_search_log.md`. The mathematical derivations from Schnell’s Appell–Humbert and Riemann criteria, and from the Cerf/Smale/Eells–Kuiper comparisons, are explicit in the paper. Every bibliography entry says `verified` and records what was opened.

## Executed computations and their evidentiary roles

| Program group | Arithmetic / precision | Independent comparison and role |
| --- | --- | --- |
| `ab_exact.py`, `ab_geometry.py` | Exact integer and rational | Centralizer, norms, Smith/Hermite forms, product lattices, affine identities, cocharacters, automorphism cocycles, geometric-height and conjugation checks. Proofs establish extension and global gluing. |
| `ab_deformation.py` | Exact integer and rational | 481 weighted root characters compared by coarse invariant exponents and weighted monomial counts; cusp cup, gamma class, Leray terms, and volume/normal calculations checked. |
| `cd_numerics.py`, `cd_periods.py`, `cd_special_intervals.py` | 90-digit evaluations; independent 60-digit intervals | Jacobi series versus 120-factor triple product, independent cusp root, and certified special-value intervals. Twenty digits are displayed. |
| `cd_bounds.py`, `cd_local_bound.py` | 50-digit intervals and analytic estimates | Coarse global bound and a quantitative local maximum radius, with explicit analytic tails. |
| `f_interval_cert.py`, `f_interval_parallel.py` | Outward interval arithmetic at 30 decimal digits; rational boxes | Complete strict compact-domain cover. Fourier, theta and eta tails are included. |
| `f_interval_verify.py` | Exact `Fraction` arithmetic | Independently reconstructs the binary partition, area, strict bound comparisons, local omissions and modular-domain exclusions. It checks coverage rather than substituting a second floating-point grid. |
| `cd_multiples_initial.py`, `cd_torsion_independent.py`, `cd_exact.py` | Exact rational polynomial and matrix arithmetic | Independent point addition versus division-polynomial recurrence; torsion roots, counterexample images, Neron–Severi/Pfaffian identities, boundary kernel, and all dihedral gluing actions. |
| `e_degeneration.py` | Exact integer and rational | Translation, local modification, Smith forms and both independent Euler computations; topology assigned only to actually constructed spaces. |
| `f_exact.py` | Exact SymPy and a separate `Fraction` matrix implementation | Integral monodromy, character, group law, null-stabilizer counterexample, orientation/signature and period comparison checked independently. |

The exploratory grid of 5,151 points and early interval experiments are retained and identified as exploratory. The global theorem uses the completed corrected certificate. The two radius computations compare interval exponentials with the exact integers `6^3` and `6^6`. No sampled decimal is used as a substitute for a proof.

All computation outputs are retained beside their scripts. The detailed section records below give the mathematical dependency and precision for each. Source identity, ledger assembly, compiler and visual audit scripts are also included. The rebuild uses LuaLaTeX and BibTeX; the workspace-local bootstrap handles the supplied minimal TeX installation without changing system files. On a configured TeX Live installation the ordinary LuaLaTeX build applies directly.

## Exact remaining targets and smallest instances

**C.3, boundary replacement.** The unique degeneration occurs over t=1 when `Im(c)=(3/pi)*log6`. The exact rank-three quotient and rational/irrational separation criterion are proved. The second Albanese j-function has a natural boundary on the corresponding real parameter line. The smallest missing construction is a compact complex-space replacement for the order-four neighbourhood at this boundary, with the stated nonreduced structure and compatible parameter maps. The quotient calculation and natural-boundary obstruction do not establish nonexistence of every possible compactification.

**E.1, untwisted compact limit.** The projective-line-bundle pushout Q is constructed as a compact complex space, its integral topology is computed, and its proper flat smoothing is constructed over every finite-base disc. The smallest missing point is one lift of the nodal point at infinity, where `xy=u*z*v`. The explicit blow-up resolves the general-fibre node and changes one central branch. The required equivariant periodic gluing must retain the prescribed general Mumford resolution, yield a proper quotient, and settle the proposed central normalization. It has not been constructed or ruled out.

**E.2, sphere-family compact limit.** The two reduced special surfaces have actual semistable finite-quotient fillings after `w=s^6`; their topology is computed. The first missing finite-place germ is the order-three action on a two-parameter plumbing with its original normal character and central multiplicity, followed by descent from s to w. The order-four germ and the infinity filling must be compatible. No global central threefold has been constructed, so no Euler characteristic, fundamental group or homology is assigned to such a limit. The smooth monodromy is identity on integral cohomology and is reduced to the explicit Eells–Kuiper residue of the displayed clutching map, meeting that alternative of the prompt. The numerical residue itself remains unevaluated.

## Detailed section records
# A/B audit and mathematical results

The section file `AB.tex` contains the proofs. These arguments concern the actual original period matrix, the prescribed periodic triangular cusp fan, the root-cover affine actions and their actual logarithmic collars. They include the normalized-base-change comparison and the exact source-to-target lattice maps.

## Item coverage

| Item | Statements | Outcome | Exact scope |
| --- | --- | --- | --- |
| A.1 | A.1.1, A.1.2 | (a) | Canonical bundle, direct image for every integer k, full graded ring, intrinsic base, multiplicities, normalized covers and degree-9/8 product covers. |
| A.2 | A.2.1 | (a) | Rational/integral centralizer, exact deck lift, norm groups, exclusion of negative linear part, necessary parity. |
| A.3 | A.3.1 | (a) | All local maps, every cusp stratum, original collar identities, vector sheaf, additive correction, coherent even shifts and proper punctured-disc family. |
| A.4 | A.4.1–A.4.3 | (a) | Exact Albanese j-functions, generic necessity via the two j-functions, everywhere nonzero KS class, precise comparisons with read Viaclovsky and Yang proofs. |
| A.5 | A.5.1, A.5.2 | (a) | Complete fixed-data classification; exact tangent cohomology (1,1,1,0); smooth reduced Kuranishi disc and miniversality at every admissible parameter. |
| B.1 | B.1.1–B.1.4 | (a) | Typed theta quotient, exact inverse-generator sign, MW generator, zero of wp, geometric line-bundle comparison, lambda0=1 for an explicitly stated reference, exact parameter domain. |
| B.2 | B.2.1–B.2.3 | (a)/(b) | Complete all-data arithmetic classification; two classes at fixed u; corrected signs under explicit marking; refutation of global fixed-data u-descent in E26 Remark8.1, with the proper double-cover family in its place. |
| B.3 | B.3.1 | (a) | All primitive translation data of the stipulated coprime higher-multiplicity sphere members; step 2kl Z; 2kl classes at fixed u. |
| B.4 | B.4.1, B.4.2 | (a) | Full holomorphic group C*, complete conjugation relation, real locus, and split holomorphic/antiholomorphic group with explicit action. |

## Exact conventions and maps

The analytic deck generators satisfy s_j(g_j z)=exp(−2πi/m_j)s_j(z), g1g2g0=1. Positive parameter circuits remain counterclockwise: a w circuit changes c by −2 and a u circuit changes c by −1.

The integral map into Engel's common basis (e1,e2,e3,e4) has columns

P_E = [[0,−2,−1,−2],[2,−1,0,−1],[0,2,1,3],[−1,0,0,0]].

It has determinant −1, intertwines T0 P_E=P_E A1 and T1 P_E=P_E A2, sends delta to Engel's positive circle class, and satisfies psi P_E=−gamma. It also intertwines the actual local complex periods: Engel's two fixed elliptic moduli can be −kappa1 and 1−kappa2 in this marking. His positive-root affine generators are inverses of our negative-root generators, so a0=−P_E w1/3 and a1=−P_E w2/4. All sign claims in B.2 are derived through this map.

For b0part=0 the base reflection acts on periods as (tau,mu,beta)→(−bar tau,1−bar mu,−bar beta). Its exact integral map is H=[[1,0,0,0],[0,1,0,0],[−6,0,−1,0],[0,−1,0,−1]]. It sends the canonical model to parameter −bar c with twists −epsilon+delta and epsilonprime−3delta. The proved all-data classification then returns this to canonical parameter 1−bar c. Consequently the real locus is w=−bar w, and the full automorphism group there is C* semidirect C2 with action z→1/bar z.

## Sources actually read

The relevant passages of `original/AC26_transcription.tex` were read for the full period laws, matrices, finite action, admissible vectors, explicit collars and arbitrary cusp sections (Sections2–6 and the fundamental-group conventions). The PDF is the governing source; no transcription-only correction to its mathematical formulas is asserted here.

The complete `workbench/period_shift_classification.tex` and `workbench/analytic_canonical_ring.tex` were read. The finite product-cover and normalization parts of `workbench/finite_filling_certificates.tex` and the full relevant period-variation proof of `workbench/period_parameter_deformation.tex` were read. The corresponding course chapters were checked at their canonical, theta, Mordell–Weil, resolution, height and global-linearization arguments. The stated survey items F2,F3,F4,F5,F12,F17,F22,F26,F29 and the reader's G1a sketches were read as claims to be checked.

The extracted text of the attached Engel PDF was read at Lemma2.1, Corollary2.2, Definitions2.3–2.5, Propositions2.4–2.9, Construction3.5/Lemma3.6, Theorem5.1, equation6.1 and Remarks8.1–8.2. The attached Viaclovsky logarithmic-transformations PDF was read at Theorem1.1, Questions1.1, the exact higher-root construction and Proposition4.7. The attached Yang PDF was read at its centralizer, affine lift, finite norm and analytic collar arguments, especially Lemmas6.6–6.9 and Proposition6.15. Current literature checking is recorded in the root report; no priority claim is made.

The actual primary HTML of Du–Guo–Kusakabe–Xie, arXiv:2610.00250v1, Section6 was then read and audited in full at the root construction (Lemmas6.1–6.3), the multiplicative cusp resolution (Lemma6.4/Proposition6.5), vertical-bundle descent (Proposition6.6), logarithmic tangent and relative duality (Lemmas6.7–6.9), direct images (Proposition6.10), normal quotient and tangent dimensions (Lemma6.11/Theorem6.12), and Kuranishi conclusion (Proposition6.16). The deformation claims disappear from version2. A.5.2 records that version fact and supplies its own proof, including an independent coarse-invariant-exponent calculation of all required root-line cohomology. The former uncomputed tangent datum is therefore now proved; validity is based on the actual displayed proof, not on the historical theorem label.

For the explicit A.5 scope boundary, Viaclovsky's attached two-parameter paper was read at its initial surface y²=x³+tx+1, Section3.1's exact rank-one quotient and boundary multipliers, and Proposition6.1's invariant canonical form. The scope paragraph specifies the single rank-one fibre over p1, 4p1³+27=0, and derives h•(K_R)=(0,1,1) for its elliptic-ruled normalization. The first unperformed transfer datum is the connecting map from this H¹(K_R) into the changed model's logarithmic tangent H²; the specified attack uses the full holomorphic collar units. Global classification for that changed period system additionally requires its four-matrix centralizer and defects. This is an explicit excluded-system test, outside the retained-family theorem, rather than an additional unfinished A/B target.

## Computations run

`ab_exact.py` computes the norm matrices, fixed-coordinate Smith forms, centralizer, exact moving lattices, product-cover determinants, even-shift local equations, cusp cocycle and full integral automorphism-cocycle quotient. It independently compares the direct congruence criteria with Hermite lattice membership in 2,880 cases. It also checks the higher-root norm identities and shift step for (k,l)=(1,1),(3,1),(1,5),(5,7),(7,5). The outputs are in `ab_exact.out`. The proofs use symbolic identities for the full generality; the finite comparisons are independent checks.

`ab_geometry.py` checks the Engel marking directly and independently via Viaclovsky's intermediate basis; the E6 inverse matrix and exact 1/6 height; the critical-point expansion in the resolution with leading coefficient −1/8; the exact cusp sign; every full affine reflection law, the reflection lattice matrix and transformed twists. Its output is `ab_geometry.out`. All arithmetic in these two scripts is exact in integers, rationals, rational functions or algebraic extensions. There are no floating-point precision claims in these scripts.

`ab_deformation.py` independently compares the coarse root-invariant cohomology formula with weighted monomial counts for 481 weights, checks the Picard relation minors, the invariant gamma character, the cusp cup form and its determinant, all Leray summands, and the invariant volume-form determinants in the two maximal-cone representatives. Its output is `ab_deformation.out`. These exact calculations verify the data in A.5.2; the sheaf exactness, actual quotient maps, descent and deformation-germ argument are proved in the text.

The separate interval program `cd_special_intervals.py` supplies the rigorous nonzero imaginary difference of kappa1part−kappa2part used for the generic Albanese cross-check. Its certified interval lies wholly between −0.2 and −0.1. This converts the two-Albanese argument into a complete generic necessity proof with an explicitly defined countable exceptional set; the integral proof also handles that set.

## Corrections and strengthening

1. Lead1 and Lead2 are proved with all exact finite lifts, collar equations and coherent maps. Their norm images and parity are confirmed.
2. Lead3 is proved. The two Albanese quotients include both the product-cover kernel and the cyclic translation; ignoring either changes the modulus. The generic cross-check uses the certified nonreal difference of the two additive modulus constants.
3. Lead4 extends to arbitrary cusp sections and both signs of the fibre-linear part. The exact invariant is (|p|,exp(−πi(c+k2))). The gamma winding supplies p'=a p, and the remaining cusp winding is removed by an explicit integral moving-lattice adjustment. This closes the unspecified cusp step of G1a-13(a).
4. With the explicit positive-root convention above, c→c+1 changes Engel's data by (−delta/3,+delta/4). The signs in Lead4 were explicitly subject to conventions; they are now fixed by a displayed integral map and affine inverse calculation.
5. E26 Remark8.1's claimed global proper family over the original u-disc with fixed sphere logarithmic data fails the order-two finite-filling descent test. The corrected statement is a local u-family and a global proper family after u=w². This is proved by the norm obstruction and independently by the odd Laurent leading term of j(Alb(S2)). The untwisted family is not refuted by this argument.
6. Lead7 is proved for the entire holomorphic automorphism group. Saturation and the full integral coboundary index are checked. The additional antiholomorphic calculation gives the exact real locus and split full group.
7. A sign-label error occurs in `course/cusp-and-compact-threefold.md` Section10.2: for its stated P_*=(0,sqrt(2)t²(t−1)) and chart Y2=y/t², the value at t=0 is −sqrt(2), so it meets E_{2,−}, whereas the course says E_{2,+}. Both endpoint height corrections are 4/3, so the generator/height conclusion survives. The proof here retains the correct chart value and uses the sign-independent height calculation.
8. Viaclovsky's countability argument establishes local non-isotriviality and positive Kuranishi dimension. The explicit Beltrami computation here additionally proves a nonzero derivative at every admissible parameter. The distinction is witnessed by the exact example z→z², whose nonconstant image has zero derivative at zero; no unsupported implication is used.
9. A.5.2 additionally computes every tangent cohomology group using the actual root curve and cusp-only logarithmic tangent bundle. The gamma class extends nonvanishing through the cusp by an explicit deck cocycle, the cusp cup pairing is nondegenerate, and the normal quotient is the pushforward of the canonical line of dP6 via the invariant cusp volume form. The resulting h¹=1 together with the already nonzero Kodaira–Spencer map forces the actual Kuranishi ideal to vanish. This proves local miniversality, including reducedness.

## Final scope and status

There are 19 numbered A/B statements: 18 Proved and one Refuted, with a proved replacement. All nine requested A/B items have complete outcomes in the scope of the stipulated construction. The single refuted statement is the fixed-sphere-data global u-descent assertion of E26 Remark8.1; the replacement is the local-u/global-w family. The former optional Open entry A.5.2 has been replaced by the full tangent and Kuranishi calculation. Global classification remains explicitly within this construction and its stated higher-multiplicity variants; the proved local miniversality says that every sufficiently small deformation of each original member is represented here.

An independent agent audited the full A.5.2 root-chart, invariant-exponent, cusp-cup, gamma-extension, duality, normal-quotient and Kuranishi calculations and found no correction. The changed-system scope test above records precisely what substitutions would be needed before applying these results to VTwo26.


# C--D proof and computation record

| Item | Statements | Outcome | Exact scope |
|---|---|---|---|
| C.1 | C.1.1--C.1.2 | (a) | Explicit normalized beta formula, cusp branch, and all special values; two independent calculations and rigorous interval enclosures. |
| C.2 | C.2.1--C.2.3 | (a) | Exact M=-(3/pi)log6, unique maximum t=1, exact radii 216 and 46656. Analytic cusp/local proof and completed interval-cover certificate. |
| C.3 | C.3.1--C.3.4 | (c) | Rank-three quotient, rational/irrational alternatives, degree-four product cover in the rational case, and Albanese natural boundary proved. Compact threefold boundary replacement unfinished. |
| C.4 | C.4.1 | (a) | Gluing constants, abstract cusp-surface classification, and fixed double curve proved. |
| D.1 | D.1.1--D.1.7 | (b) | Lead6 equivalence refuted. Complete replacement gives exact NS lattice, all elliptic/abelian/algebraic-dimension loci, torsion density/count, and explicit dimension-one examples. |
| D.2 | D.2.1--D.2.3 | (a) | All surfaces and curves classified by explicit normalization, finite-cover, and theta-section maps; rational and elliptic existence questions decided. |

## Sources inspected

We read AC26 transcription page 2 and sections 3, 4, and 9, especially Lemmas 9.2--9.4 and Proposition 9.5. Original PDF page 66 was rendered and visually inspected for its orientation-sensitive self-intersection statement. We read the supplied Engel PDF section 2, including the complete statement and proof of Lemma 2.1; D.1.2 derives its application to 6kP. We read the attached Duke--Imamoglu Theorem 1 and its discussion of the Eichler--Zagier formula. The cusp constant and normalized beta formula here are independently derived; no unopened Eichler--Zagier paper supplies an unverified step.

The course sources inspected were `global-periods-and-line-bundle-quotients.md` sections 4--6 and `cusp-and-compact-threefold.md` sections 5 and 9--13. We read the first-coordinate-quotient subsection of `workbench/cusp_spectral_geometry.tex`, and relevant G1a and F reader notes. B.1.3 independently proves the period section's Mordell--Weil identification, used in C.1.1.

We opened Christian Schnell's MAT615 Lecture 4 (6 February 2019), official Stony Brook PDF, and read Theorems 4.1, 4.4, equation (4.3), and the effective-bundle discussion on pages 2--3. D.1.6 and D.2.3 give the exact reduction from those theorems to this period matrix, including rational kernel, quotient lattice, complex orientation, and automorphy factors. These sources have been read; none is invoked merely by reputation.

## Corrections and proved additions

The normalized missing period is beta_part=(6i/pi)Log(theta1(mu,tau)/(2sqrt3 eta_D(tau))), with beta_part+tau tending to zero at the chosen cusp. Both affine transformation laws hold exactly: the possible logarithmic defects are constant multiples of twelve, and evaluation at the two fixed points removes them. The special values are computed independently by Jacobi series and triple product, and then enclosed by interval arithmetic. The cusp branch is mu0=1/2-i log(5+2sqrt6)/(2pi).

The broad elliptic-quotient equivalence in Lead 6 is **false**. At t=32/5 the section has exact order four, so 6P is nonzero. At the explicitly specified admissible parameter c=-2.25-34.02109724218209472308i (decimal approximation), L=3zeta1+4zeta2 maps the four periods to (-101tau,2tau+2,3,4), generating the entire lattice of the specified E_t. Its kernel is connected and elliptic. Admissibility is proved by an analytic inequality Im c<-22, without reliance on the decimal. The strongest correct first-coordinate statement is D.1.1; D.1.6 supplies the exact criterion for every quotient. The workbench itself restricts its assertion to the first coordinate; the overextension occurs in the Lead's wording.

The three cusp gluing constants are (-a^-1,a^6,-a^-7 w^2), a=5+2sqrt6. All twelve hexagon automorphisms were checked exactly. Consequently W_c and W_cprime are biholomorphic as abstract compact complex spaces exactly when cprime-c is integral. This is an unmarked classification. The vertical C* fixes the double curve of edge direction e2.

AC26 Lemma 9.4 gives the coefficient identity eta wedge eta=12 vol. That identity is correct. The actual real period map has determinant TD<0, so integration in the complex orientation gives -12. D.1.4 states the exact comparison; it does not label the coefficient identity false. The sign is essential for deciding positive Riemann forms using the Pfaffian.

The exact NS group at every smooth fibre is the integer kernel of E12-E13 tau+(6E23-E14)mu+E24 beta+E34(6mu^2-tau beta)=0. Elliptic quotients occur exactly where this kernel contains a nonzero matrix of Pfaffian zero; abelian surfaces occur exactly where it contains a matrix of negative Pfaffian. Their explicit countable unions of zero sets give every algebraic-dimension locus for fixed c. No finite algebraic description of these countable analytic loci is asserted or needed for the stated exact criterion. On the explicit period locus beta=-6tau-12mu, the very general fibre has NS=Zeta+ZE with Pf(aeta+bE)=6a^2, and therefore algebraic dimension one; its parameters are admissible near the cusp and P can be non-torsion.

All compact irreducible curves are vertical, and every irreducible compact surface is a reduced fibre. Curves in W are images of strict transforms of irreducible plane curves or exceptional curves on dP6, with precisely the three conductor pairings. Curves in S_j are finite images of curves in its product cover. Dimension-zero smooth fibres have no curves; dimension-one fibres have exactly the translates of their unique elliptic kernel; curves in abelian fibres are elliptic translates and irreducible zero divisors of the displayed positive theta automorphy equations. Thus the classification includes the exceptional smooth fibres, without relying on a finite numerical list. No rational curve lies outside W; ordinary fibres over t_± contain elliptic curves.

The exact maximum occurs only at t=1, so the actual admissibility boundary degenerates precisely the torus cover of the order-four filling. At a rank-three period point, the period subgroup is discrete exactly when its real kernel line is rational. The rational critical fibre at t=1 has a degree-four cover E_i times C*, and is noncompact. The irrational quotient is non-Hausdorff; its maximal Hausdorff group quotient is R times (S1)^2. The Albanese j-invariant has a natural boundary on the explicit critical c-line, ruling out a holomorphic-coefficient Weierstrass replacement in that same parameter. These are proved obstructions to concrete replacements, not an assertion that every compact threefold modification is impossible.

## Computations run and retained

`cd_periods.py` contains the initial high-precision evaluation. `cd_numerics.py` independently computes special values at ninety digits by Jacobi series and the Jacobi triple product, with 120 factors. It also computes the cusp logarithm by a logarithm and a trigonometric root, and runs the explicitly non-certified 5151-point grid. Five grid points are independently checked at ninety digits. `cd_special_intervals.py` encloses the two beta values and the nonzero imaginary difference of the two Albanese constants with sixty-digit interval arithmetic and explicit tails. It also proves the stronger cusp theta-norm bound below 1.082 for Im tau at least two.

`cd_bounds.py` evaluates the monotone global Fourier bounds by fifty-digit interval arithmetic. `cd_local_bound.py` evaluates every constant in the Cauchy--Rouche proof of the strict maximum on |tau-i|<=0.00015; its independently differentiated theta-constant series checks the needed e2 derivative. `cd_interval_cover.py` is the exploratory interval-cover implementation; its partial output is not used as a proof. The corrected full computation is `f_interval_cert.py` scheduled by `f_interval_parallel.py`, with 19,701 accepted outward interval boxes at 30 decimal digits. The saved `f_interval_parallel_certificate.json` is independently checked by `f_interval_verify.py`. All19911 rational leaves cover the starting rectangle, with the analytic local square and exact unit-circle exclusions accounted for. Every corrected acceptance uses interval endpoints, never a rounded floating comparison.

`cd_multiples_initial.py` is the supplied reader's addition checker, copied with its attribution comment and run as an initial check. `cd_torsion_independent.py` independently computes division polynomials, exact counterexample images, the E6 correction matrix, and both the positive and isotropic NS examples. `cd_exact.py` verifies the real determinant, boundary kernel, and full dihedral action. Each executable's output is included. `cd_registry.py` generates the statement ledger.

## Remaining obstruction

The compact boundary replacement in C.3 is unfinished. Its smallest unresolved case is a proper compact complex-space filling of the order-four surface degeneration in the original parameter, with a proof that it glues to the ordinary fibres. The unique affected base fibre is t=1. Both rational and irrational real boundary parameters have been analyzed at the level of the actual period quotient and Albanese invariant. The quotient analysis does not itself produce such a filling.

C.2 is settled by its completed certificate. The corrected computation accepted 19,701 norm boxes, omitted 36 boxes covered by the explicit local analytic proof, and excluded 174 boxes lying strictly inside the unit circle. No pending or undecided boxes remain. The independent rational-cover verifier reconstructs all 19,911 leaves, checks exact covered area 23/40, and verifies every exclusion and reported strict interval bound. Together with the analytic cusp estimate, this proves the unique maximum at t=1, M=-(3/pi)log6, w-radius 216, and reference u-radius 46,656. Full code, JSON certificate, and outputs are included.


## Part E: the actual candidate, local fillings, and unresolved compact gluing

| Item | Statements | Outcome | Missing requested result |
| --- | --- | --- | --- |
| E.1 | E.1.1–E.1.5 | (c), unfinished | A compact equivariant two-parameter filling at infinity with the prescribed general Mumford fibre and the proposed central normalization. |
| E.2 | E.2.1–E.2.3 | (c), unfinished | A compact sphere-family filling, including the nonreduced finite-fibre neighbourhoods and descent of their actions. The smooth monodromy is reduced to the explicit invariant allowed by the prompt. |

We constructed the compact pushout Q by actual local analytic rings, proved that its normalization is the stated projective-line bundle, and computed its local smoothing sheaf. The resulting local plumbing exists over the entire finite part of the elliptic base, including the Kodaira fibres at 0 and 1. Its comparison with Engel's nonzero-parameter quotient is the explicit inverse bundle map in E.1.2.

At the node over infinity the joint germ is `xy=u*z*v`, with original elliptic-base coordinate `q=z*v`. This family is flat over u. For nonzero u its fibre has an ordinary double point. Blowing up `(x,z)` gives a projective small resolution on those fibres and remains flat, but one branch of the central normalization is blown up along a curve. The actual substitutions prove the alteration of that candidate. They do not prove that every equivariant construction must alter it. The two period actions and the complete periodic fan have not been glued across `(q,u)=(0,0)`.

We nevertheless computed the integral topology of the **constructed candidate**: pi1(Q)=Z, H_i(Q)=(Z,Z,Z^8,Z^7,Z^10,0,Z), and Euler characteristic 12. The two section inclusions give an explicit homology map. Its rank and primitivity are proved using a squarefree Gram determinant, and independently checked by exact Smith forms. The Euler characteristic is checked by both homology and stratification. These invariants are not assigned to an unconstructed limit of the compact sphere family.

The two reduced bielliptic surface families do have explicit semistable fillings after `w=s^6`. They are finite free quotients of a twelve-gon Tate curve times the fixed elliptic curve. The central surfaces have four and three ruled components. Their fundamental groups are Z^2 semidirect Z with rotations of orders three and four. Their integral homology is respectively `(Z, Z+Z/3, Z^5, Z^9, Z^4)` and `(Z, Z+Z/2, Z^4, Z^7, Z^3)`; both Euler characteristics vanish. We checked the full twisted cycle matrices as well as the independent two-by-two determinants.

The sphere family's smooth monodromy fixes integral cohomology. We gave an actual representative by parallel transport along `c(r)=c0-2r` followed by the coherent even-shift gluing. Its oriented two-disc clutching sphere has Eells–Kuiper residue `(p1^2-4 signature)/32 mod28`. This is the explicit invariant reduction permitted in E.2, with the orientation and denominator fixed from the original Eells–Kuiper formula. The characteristic numbers of a bounding eight-manifold for this particular clutching sphere have not been computed.

### Reading and exact computations

We read Engel Sections 2, 3, 7 and 8, in particular Lemma 2.1 and proof, Corollary 2.2, and Conjecture 8.2. We inspected the supplied period and finite-product presentations and compared the signs with the explicit first-page marking map. For the smooth monodromy comparison we opened Cerf's seven-page primary article, Theorem 1 and Corollaries 1–2, Smale's original paper, Theorems A, I and J, and visually inspected Eells–Kuiper Section 7, printed pages 100–103.

`code/e_degeneration.py` was executed and its output is retained. It verifies the translation matrix and its action on the intersection lattice, primitive homology maps, Smith normal forms, both local modification substitutions, and the integral cycle complexes. `code/e_registry.py` creates the eight statement rows and its output is also retained.

### Smallest undecided instances

For E.1 the smallest unresolved chart is one lift of the nodal point, with equation `xy=u*z*v`, equipped with both deck generators. The required construction must have the prescribed general-fibre small resolution, a proper periodic quotient, and the proposed central normalization. Our single explicit blow-up has the first local property and changes the last.

For E.2 the first unresolved finite-place chart is the order-three affine action over a simultaneous `(t,s)` plumbing with the original normal character and central multiplicity three, followed by descent from `s` to `w=s^6`. The order-four chart and the infinity chart must then be made compatible. Until this is done, there is no global central fibre whose topology has been established. The one remaining numerical monodromy instance is the residue for the loop based at `c0=-i(M+1)`.



## Part F: completed mathematical outcomes

| Item | Statements | Outcome | Remaining instance |
|---|---|---|---|
| F.1 | F.1.1, F.1.2 | (a) Proved | None for the group, its abstract multiplication, its integral embedding, its Zariski closure, and its Levi image. |
| F.2 | F.2.1, F.2.2, F.2.3 | (b) Full-domain properness refuted; strongest replacement proved | None: the largest invariant open set is determined for both groups and contains every admissible period image. |
| F.3 | F.3.1, F.3.2, F.3.3 | (a) Proved | None for the quotient by the proper open set, the alternative explicitly permitted in F.3. |

### Sources read and comparisons made

We read the matrices and period laws in the attached authority PDF [AC26], especially page 2 and the corresponding material of Sections 2 and 3, through its extracted text. We compared them with the LaTeX transcription at lines 130–158 and 418–451, `workbench/exact_algebra.tex` at its initial matrix certificate, and `workbench/hodge_frolicher.tex` at the proposition labelled `prop:period-derivative-determinant`. We read [E26], Lemma 7.2 and Remark 8.4, in the text extracted from the attached PDF. We read the survey's F28 and its surrounding entries. No result in Part F is accepted on the basis of a workbench status label.

F.1.1 supplies an exact answer that the input survey did not give. In the block coordinates of the paper, the monodromy group is the kernel of the explicit character

`g(B,x,t) -> t + 6(x1+x2+x1*x2) - alpha(B) mod 12`.

Its index in the integral stabilizer of the vector `delta_hat` is 12. Its index in the integral stabilizer of the primitive line is 24. The kernel of its Levi projection is an explicit integral Heisenberg group. F.1.2 specifies the abstract central extension by its actual integral two-cocycle, rather than leaving an extension class unnamed, and proves that the Zariski closure is the full six-dimensional vector stabilizer.

F.2.1 gives the complete counterexample to full-domain properness requested in Klingler's question. The rational complex structure `J0` has an infinite stabilizer generated by a displayed integral unipotent matrix `R`. We verify `J0^2=-I`, compatibility with the exact alternating form, real signature `(2,2)`, membership `R in Gamma`, commutation, and infinite order. F.2.2 strengthens this counterexample: rational conjugates of `J0` are dense in the null locus `psi(delta_hat,J delta_hat)=0`; each has an infinite stabilizer in `Gamma`. This density proves maximality of the complementary open set. Properness on that complement follows from its real-parabolic homogeneous-space description with compact stabilizer. The argument applies to the full integral line parabolic as well.

F.2.3 computes the exact comparison with the supplied period coordinates:

`psi(delta_hat,J delta_hat) = -6 / (Im beta - 6(Im mu)^2/Im tau)`.

Thus every admissible period lies in the positive component of the maximal proper-action open set. This answers the open-set alternative of [E26] Remark 8.4.

F.3.1 uses the actual morphisms from marked periods to the elliptic modular invariant and from the proper quotient to the `t`-line. It proves `j(tau)=1728t` by exact cancellation in the displayed Weierstrass equation. This gives a holomorphic left inverse to the period curve, hence injectivity and immersion. After adding the two finite punctures, the curve is a proper holomorphic embedding of the affine `t`-line in the proper quotient. F.3.2 determines its closure there and gives its three local limiting behaviours. At the cusp, the curve escapes compact subsets of this quotient and its compact-dual Hodge plane tends to `span_C(gamma,u)`. The intersection of that plane with its conjugate is computed explicitly, so the statement that this is outside the open period domain has its required comparison.

F.3.3 independently recovers the workbench's generic determinant nonvanishing and its zero at the order-three point. The immersion proof uses the derivative of `j(tau)`, whose value is exactly 1728 in the base coordinate, and is consequently valid at all points of `B°`.

### Computation record

`code/f_exact.py` was run. Its complete output is `code/f_exact.out.txt`. Every numerical claim in this part is an exact integer or rational identity. The group generators, invariant form, commutator and null-stabilizer counterexample are checked first by SymPy and independently by a separate matrix implementation using Python's `fractions.Fraction`. Symbolic calculations also check the Heisenberg multiplication, the full six-element group `SL2(F2)` acting on the quadratic function, the independent nilpotent logarithms, the sign comparison with `D`, the Weierstrass discriminant and `j`-invariant, and the derivative determinant at the elliptic point. These finite checks certify the displayed matrices; the infinite-group and maximal-open-set conclusions have their proofs in F.tex.

### Corrections and scope

The full-domain properness proposal is false for the actual monodromy group. The replacement is a uniquely largest invariant analytic open set containing all admissible images. The survey's F28 can therefore be replaced by the concrete statements F.1.1–F.2.3. The workbench determinant proposition is verified in its stated scope. The closure requested in F.3 is computed in the proper quotient explicitly permitted by that question. No priority is claimed; the overall bibliography and report record the root literature search.
