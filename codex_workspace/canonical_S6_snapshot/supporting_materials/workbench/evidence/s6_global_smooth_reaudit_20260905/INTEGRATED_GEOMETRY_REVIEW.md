# Bounded post-integration source review

Date: 2026-09-05. Reviewer: `/root/s6_period_existence_reaudit`.

**Result: PASS. No mathematical or source-integrity concern requiring a change was found in the reviewed integration.**

## Exact reviewed source

`output/s6_consolidated_canonical_2026-08-26/supporting_materials/workbench/research/candidate_geometry.tex`

SHA-256: `6B6EF348E87295AEFDE4AE4FE6A771ED83B56F848AA367EAAF8E70B37707BDB9`.

Compared against the full `CANDIDATE_GEOMETRY.diff`, `candidate_geometry_before.tex`, and `candidate_geometry_after.tex` in `supporting_materials/workbench/evidence/s6_global_smooth_reaudit_20260905/`; against this agent's original `AUDIT.md` and `period_existence_strengthening.tex`; and against the cusp worker's `CUSP_AUDIT.md` and `cusp_staged_corrections.tex` retained in that evidence directory. No new research, canonical edit, or build was performed.

## Period insertion: lines 563–616

The entire staged period proposition and its proof and following remark are present verbatim, apart from omission of the fragment's comment header and surrounding whitespace. The preceding period construction, source lines 1–560, is unchanged.

The proof retains the exact determinant `Im(tau) D`, the attained finite maximum `M`, and the strict parameter inequality `Im(c_0)<-M`. Attainment follows from continuity and the cusp limit `D→-infinity`; equality yields a zero at a maximum point; a larger imaginary constant yields opposite signs at that point and near the cusp and hence a zero on a path. These prove the stated exact parameter set, not merely sufficiency.

The inserted counterexample retains `beta_tilde=beta+i t pi`, the original modular constant `1728`, and the asymptotic `D(R)=-log(1728R)/(2pi)+Im b(0)+o(1)`. It preserves all affine transformation laws and violates the proved cusp extension, so it accurately identifies the failure of the cusp-free shortcut without contradicting the actual period theorem.

## Cusp refinements: lines 703–1016

The translated-chart expressions now use `U_sigma(S,epsilon)=U_sigma(S)∩Y_epsilon`, matching the actual domain of `Psi`. The covering statement uses those restricted open charts. The added closed-unit-polydisc identity correctly uses the weak inequalities `theta_i≥0`; its hypotheses inherit the lemma's torus-point clause. Its use in the compact representative argument includes triangle edges and vertices and does not invoke the strict formula at equality.

The matrix bound is now taken on the specified compact subdisc `|t|≤r_1`, with `0<r_1<min(r,1)` and `0<epsilon<r_1`, and the complete `C(t)` is retained. Thus the norm estimate used for freeness and proper discontinuity is valid throughout the restricted domain.

The pairwise separation addition gives the exact semigroup equality: for `a∈S_upsilon`, choose `k` large enough that `a+km∈S_kappa`; then `-km∈S_kappa'`, so `a∈S_kappa+S_kappa'`. The reverse inclusion holds by evaluation on the common face. Consequently the displayed tensor-product map is surjective, and the overlap graph is analytically closed. Applying this on the open cover of chart products proves a closed diagonal even for the countable fan. The argument agrees with the cusp report's direct proof. The cited `CoxLittleSchenck2011` item exists in `references.tex:168`, and the source citation includes the exact Proposition 3.1.3 / separation-lemma locator checked by that report; it cites no audit verdict as authority.

The connectedness addition applies to the actual restricted chart sets `|z_0z_1z_2|<epsilon`: they are star shaped and meet the common connected punctured torus. It therefore proves the connectedness needed for the particular restriction and its quotient.

The opposite-edge maps retain the sign `B_0^2=-I` and the full matrix

\[
C(0)=\begin{pmatrix}6\mu_0&h_0\\b_0-h_0&\mu_0\end{pmatrix}.
\]

The explicit products are

\[
\begin{aligned}
(0,1)C(0)B_0e_1&=-\mu_0,\\
(1,0)C(0)B_0e_2&=6\mu_0,\\
(1,1)C(0)B_0(e_1-e_2)&=-7\mu_0-b_0.
\end{aligned}
\]

They give exactly the three printed multipliers. The same primitive character is used on both curves, so the reverse map has reciprocal multiplier. The cancellation of `h_0` in the third character evaluation is justified algebraically and does not remove an input. Endpoint extension follows because these are restrictions of the ambient biholomorphisms.

## Finite-disc and gluing refinements

At lines 1203–1206, choosing a round image disc in the existing linearizing coordinate preserves both rotation invariance and translate-disjointness. It ensures the later radial contraction stays in its domain.

At lines 1502–1518, the second-countability and full-restriction statements follow from the previously proved open embeddings and the disjoint special discs. For each compact base set `K`, the finitely many sets `K∩closure(V_a)` are compact within base patches where the full inverse-image maps are proper. Their inverse images are compact, and their union is exactly `f^{-1}(K)`. This proves the global properness assertion with the required full restrictions; no image or inverse-image direction was reversed.

## Mechanical source checks

The following read-only comparisons all passed:

- Current canonical source equals the retained `candidate_geometry_after.tex` snapshot.
- Original source lines 1–560 are unchanged.
- The full staged period fragment is contained in the integrated source.
- Every old `label` and explicit `tag` remains present.
- The integrated file has no duplicate labels.
- The only added labels are `prop:period-exact-admissible-constants`, `eq:cusp-closed-chart-identity`, and `eq:cusp-exact-opposite-edge`.
- Full diff inspection found no lost equation; the removed phrases are replaced by the corresponding explicit domain, weak-inequality, separation, or properness arguments.

This review supplies no new theorem and does not require a further build beyond the single build already coordinated by the root. It is a post-integration proof/source check of the identified file and changes, not an audit of sphere recognition or an independent re-audit of every downstream claim.
