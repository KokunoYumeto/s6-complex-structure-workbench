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
