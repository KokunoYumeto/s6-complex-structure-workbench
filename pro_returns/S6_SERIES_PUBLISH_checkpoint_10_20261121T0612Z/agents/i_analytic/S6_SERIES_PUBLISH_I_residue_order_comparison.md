# Paper I: period, residue, rank and absolute direct-image order

## Scope and exposure

This is an exposed editorial proof comparison. The complete attached original and candidate11 current proofs of `inv:A1.3` and `inv:A2.4` were read, along with the supplying current `inv:A1.1`, `inv:A1.2`, `inv:A2.1` and `inv:A2.2` proofs. The proposed common lemma and both replacement proofs were then read in full. This record supplies no independent, targeted or computational credit. The original source's counterfactual wording had already been replaced in the current source; this extraction preserves every current mathematical statement clause verbatim.

## Finding

The existing rank/scalar proof does not use the absolute six-bundle table. Its last Hodge-number paragraph does refer back to the residue calculation inside that table's proof. The absolute proof opens by citing the later global rank result. This is a dependency-order problem in exposition: the common residue argument and the sheaf-surjectivity argument can be supplied before either final result.

## Exact repair

The two guarded replacements delete the old absolute-table block at its first location, and replace the later global-rank block by: the common lemma `pub:I:residue-kernel-rank`, the original global-rank statement with its scalar/equivalence proof, and the relocated original absolute-table statement with its splitting/duality proof. Root allocates `S6_NEW_RESIDUE_TAG`. All original labels, permanent tags, equation labels and complete mathematical statement clauses remain exactly present once. Only dependency fields and the proof organization change.

The resulting order is logarithmic bundles/direct images → finite coordinate and elliptic logarithm → raw determinant and finite coefficients → residue/kernel lemma → nonzero scalar/global rank → absolute cotangent table → Hodge table. The supplying finite-coordinate/period blocks remain byte-for-byte in their current order when the earlier absolute block is removed.

## Proof accounting

| Original span | Single destination | Mathematical content preserved |
|---|---|---|
| `inv:A2.4`, Step 1 | New lemma, Step 1 | Exact invariant κ0 matrix and cup-product row; simple determinant zero forces a unit; cusp invertibility; sheaf surjectivity. |
| `inv:A1.3`, Step 1 after its forward citation, and Step 2 through cancellation | New lemma, Steps 2–3 | Logarithmic conormal long exact sequence; residue normalization; evaluation weights 1,3,4; local map m_j x[b0]; image/kernel equality; both torsion summands cancel. |
| `inv:A2.4`, final cohomology paragraph | New lemma, Step 4 | h0(K)=2−r and h1(K)=1−r; Leray explicitly adds the remaining one-dimensional terms. |
| `inv:A2.4`, scalar and q_E proof | Original rank proposition after lemma | Variable invariant eigenframe v(s), v(0)=1; scalar −μ_s(0)/4; independent global basis and exact rank criterion. |
| `inv:A1.3`, final part of Step 2 and Step 3 | Relocated absolute-table proof | Rank-one constant summand gives K=O⊕O(−1)^2; analytic relative duality yields the second column. |

The residue comparison to Ω_B^1 is explicitly pullback, and the R2 comparison is to R2 f_*E before using its bundle splitting. Thus the new lemma does not call an arbitrary splitting canonical. The Hodge-number statements use the actual rank r of the displayed map; no additional conditional theorem is introduced.

## Verification

Exact-string guards occur once in the source. An off-source preview verifies that both original statement environments are identical after removing only the dependency metadata line, that the new label occurs once, and that every original label/tag in the affected region is preserved. The complete original/current/replacement proof archive and exact moved-span map are in `S6_SERIES_PUBLISH_I_residue_order_archive.json`. No root TeX was edited.
