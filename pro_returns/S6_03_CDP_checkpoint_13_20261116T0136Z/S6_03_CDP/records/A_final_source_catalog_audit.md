# Final source, catalogue, and prompt-coverage audit

Audit date: 16 November 2026. Auditor: the local-sheaves agent, GPT-6 Astra. This records the source audit after the promotion of C.2.UN.85–86; PDF compilation and visual inspection are recorded separately by the root agent.

## Executed inventory

`code/A_final_catalog_audit.py` was executed against the current authored `sections/part_*.tex` entry points, their included proof fragments, `build/ordered/manifest.json`, the consolidated results CSV, every author results CSV, and the consolidated bibliography. Its exact output is `code/A_final_catalog_audit.out`; the detailed machine-readable result is `records/A_final_catalog_audit.json`.

The current source has **239 numbered statements, 239 unique statement IDs, 239 assembled statements, and 239 consolidated catalogue rows**. There are no duplicated statement IDs, equation tags, or labels. There is no numbered theorem/lemma/example environment lacking its explicit catalogue identifier. There are no missing or extra consolidated statement rows, and every source status agrees exactly with its consolidated status. Author metadata occasionally expands the same status with a descriptive phrase; all such differences retain the same Proved/Refuted/Known classification. No current statement has an unclassified or Open status.

Fifteen early root statements use the assembler's explicit metadata rather than a separate author-override row: B1–B3, C2a–C2d, C4a–C4d, C4g, and C5a–C5c. They are present in the consolidated CSV, with their actual source location and requested-item mapping. The audit reports their lack of an author override separately; it is not a missing final row.

All **87 bibliography entries** have a literal `verified` marker. No cited key is missing from the bibliography, and there are no duplicate final bibliography keys. The verification notes identify the checked primary text, section, theorem, or page. Research sources that could not be opened remain documented as unread leads in the research record and are not imported as proved results through an unverified bibliography entry.

## Exact repairs made during this audit

The C4f equation namespace C.G.1–4 duplicated C.G.1–2 in the CDP Euler theorem. At the root author's request, every tag and reference in `sections/part_C4.tex` was changed to the unused namespace C.VC.1–4. Ten textual occurrences were changed. The complete original is preserved in `records/versions/part_C4_before_CG_namespace_repair_20261116.tex`. No formula or proof text changed.

The secondary-Kodaira occurrence statement UN21 duplicated C.SK.1–6 in the general-fibre exclusion proof. Its author changed the UN21 namespace to C.SKD and preserved the complete previous source. The final audit finds no remaining collision.

Fifteen A bibliography entries had explicit direct-source checking evidence but omitted the literal verification marker. The marker was added without changing that evidence. The preceding bibliography is preserved in `records/versions/A_references_before_verification_markers_20261116.bib`. In particular the AKMW/KKN readings and the Ferreira–Rebelo–Reis Lemma 2.2 reading already appear in A's reading record. D and E separately repaired their checked entries, retaining originals; E reopened the Schuett–Shioda primary text before adding the previously absent verification note.

D normalized three descriptive source status slots to Proved or Refuted while retaining their explanatory text in the statement bodies. D also moved descriptive scope text out of 29 F-number fields into the corresponding notes and assigned the checked F16 mapping. No mathematical assertion was changed by those catalogue repairs.

## Coverage of every requested Part

The original prompt was reread, including each lettered subtask, the nine Leads, its version-specific DGKX instruction, and its full-fibre and comparison-map requirements. The following is a coverage audit, not a replacement for the proofs.

| Prompt item | Answering statements | Audited outcome and scope |
|---|---|---|
| A.1 | A.1.1–2; A.2.1–3 | The canonical conormal maps, connecting homomorphisms, general inverse-Jacobian description, and double/triple formulas are proved. The normalization inclusion and its normal-crossing isomorphism are canonical. |
| A.2 | A.2.1–6; A.5.5 and subsequent local calculations | Pinch, cusp, ordinary and arbitrary reduced hypersurface criteria retain the actual fractional ideals and the scheme-theoretic conductor. Exact local code and outputs are attached. |
| A.3 | A.3.1–5; A.4.9 | The full thickening filtration retains its actual lifting maps. The support-only shortcut is refuted; the smooth-multiple generic assertion is proved. Arbitrary unequal multiplicities in reducible supports are handled by the component-addition filtration. |
| A.4 | A.4.1–9 | The printed genus inference is refuted by its exact elliptic-ruled example. Proposition 7.3 is proved by the separate unitary-local-system argument. Both specified groups on W are computed for every ambient line bundle. |
| A.5 | A.5.1–21; C4e | The normalization-triviality obstruction and the independent normal-surface smoothness theorem repair the two relevant CDP statements. The ambient conclusion and torsion-free conclusion are compared by the actual kernel inclusion. |
| B.1 | B1 | Smooth total space, section extension, all cohomology dimensions, and every gluing scalar are computed. The two test vanishings hold precisely away from scalar 1, while the ambient section dimension remains one. |
| B.2 | B2–B3 | The compact elliptic-surface product has its bundles, twelve local contributions, direct images and global tangent-twist cohomology computed. The failed ambient CDP hypotheses are identified. |
| B.3 | C4b–C4g; A.3.5; A.5.12–13; C.2.G.1 | Under the full CDP hypotheses the fixed nonnormal-support and universal normalization obstructions are proved, including all permitted general-fibre types and multiplicities. The original, two-parameter and Liu–Rollenske examples provide the specified tests, including the non-necessity of a nonreduced-fibre failure. |
| C.1 | C.1.1–3 | The index, rational Betti-number hypotheses, nonreduced effective divisor, universal Picard line family and generic endpoint vanishings are explicit. |
| C.2 | C2a–d; C.2.G.1; C.2.UN.1–86, especially UN4, UN12, UN71, UN73, UN85–86 | Unrestricted nonnegativity is refuted by complete compact blowup examples, and every even Euler value is realized. The CDP sign/equality theorem is proved. Every irreducible zero support is classified; the final finite rooted generation covers arbitrary reducible supports and full multiplicities, with an exact zero-Euler selection. Rank-two toric cores retain their periodic affine lattices and have the stated positive even Euler values. |
| C.3 | C.3.1–12 | The corrected count and exact geometric arguments leave precisely tori and primary/secondary algebraic-dimension-zero Hopf general fibres, with actual occurrences. Euler localization is given for every surviving type. |
| C.4 | C4a–C4f; C.2.G.1 | The corrected geometric tangent-vanishing criterion, its all-twist obstruction, and the six-sphere fibre restrictions are proved with the required full-fibre comparison. |
| C.5 | C5a–C5c | The normalization tangent quotient is exact in the stated NC setting. Every Picard twist, all cohomology groups, resonance lengths and the normalization-map ranks are computed. The all-twist surjectivity expectation is refuted at its explicit integral exceptions; the S6_01 D.1–D.4 comparison is stated at the end of C5c. |
| D.1 | D.1.1–15 | The integral/rational coinvariant count, coherent restriction map, invariant-span argument, splitting information and all-fibre non-torsion locus are proved. Both an additional integral-CDP counterexample and a same-integral-monodromy/different-coherent-splitting comparison are supplied. R7 is checked by the displayed lattice maps. |
| D.2 | D.2.1–8; C.2.G.1 | A compact integral-H1/H2-zero example with identity monodromy is constructed and computed. Every such CDP fibration has c3=0; the exact geometry and b3=2 conclusion are proved. |
| E.1 | E1; E7; E19 | Vertical divisors and the equality of meromorphic fields are proved by the actual pullback map, then applied to each named family. |
| E.2 | E2; E17 | The nonholomorphic reduction theorem is proved, with the printed pencil-specific direct-image step checked. The overgeneral embedded-component auxiliary statement is refuted by its complete example. |
| E.3 | E3; E9; E11–15; E19 | Algebraic-dimension exclusions and the tangent/Kuranishi computations cover the original family, the affine twists, higher multiplicities, two-parameter family, combs and Liu–Rollenske family. DGKX version 1 is cited for its stated deformation result; version 2's omission is recorded without inference. |
| E.4 | E4–8; E10; E16; E18 | The actual sheaf maps, full-fibre corrections, all-orders P1 stability and exact rank divisors are proved. Fixed higher-genus-target stability and the unrestricted theta-square identity are refuted by complete examples. The named-family conclusions agree with E.3. |

## Coverage and verdict for every Lead

| Lead | Exact verdict | Statements |
|---|---|---|
| 1 | The kernel exact sequences and the normal-crossing normalization formula are true, with the actual canonical maps. | A.1.1–2; A.2.1–3 |
| 2 | The nodal tests are true; excluding roots of unity is stronger than necessary. The two vanishings require only scalar different from 1. The ambient group is one-dimensional for every scalar. | B1 |
| 3 | The normal-singular exclusion is repaired independently, and trivial normalization pullback forces an ambient section through the proved injection. This does not contradict the separate torsion-free vanishing. | A.4.1–2; A.5.1–2; A.4.9 |
| 4 | The index and generic endpoint statements are proved with rational b1=b2=0 and an arbitrary nonzero effective Cartier divisor. Their all-twist consequences follow exactly. | C.1.1–3 |
| 5 | Euler localization is true with the finite exceptional set and actual local triviality specified. Unrestricted fibrewise nonnegativity is false; its sharp replacement includes the full even range and the completed geometric generation/zero criterion. | C2a–d; C.3.5; C.2.UN.1–4, 39, 85–86; C.2.G.1 |
| 6 | The semidirect-product and coinvariant count are true. The invariant-span equivalence describes the final step of the printed argument; the entire coherent restriction need not be generated only by that lattice. The integral representation alone does not determine coherent splitting. | D.1.1–4; D.1.10; D.1.15 |
| 7 | Verticality and meromorphic descent are proved with the connected-fibre and Kähler-general-fibre hypotheses, then checked on the named families. | E1; E7; E19 |
| 8 | The NC tangent quotient and its H3-dependent surjectivity statement are proved. The predicted all-twist surjection for X is false at the explicitly computed integral twists, although H2 is nonzero for every twist. | C5a–c |
| 9 | The infinitesimal cup-product criterion and P1 all-orders extension are proved with the corrected sheaf maps. The fixed positive-genus target assertion and universal square determinant formula are false; their exact replacements and all named rank loci are computed. | E4–8; E10; E16; E18 |

## Final mathematical audit of the formerly outstanding clause

The final UN85 source was read in full after its NC precision changes. Its potential counts actual recorded models, not an unproved class of dynamically eligible surfaces. The complete-fibre coefficient graph includes coefficient-zero curves. The shifted-coefficient invariant excludes every problematic last-exceptional nodal image, and the simply connected image curve gives the actual two surface germs even when they belong to one global prime. The recorded point map then factors through both normalized contractions and its defect drops by two. Whole sigma blocks may reset all recognitions except the protected Hopf neighbourhood; their strict component-card decrease precedes that finite reset. The endpoint common Jacobian comparison is made along quasi-bundle edges, and nonlinear leaves use their separate exact period cover. The final source, its executed certificates, and `code/A_nc_interface_branches.py` all passed independent audits.

UN86 was then read in full. Its actual embedded resolution, literal normalized root, equivariant height-one subdivisions, regular action restored before quotient, ordinary inverse blowdowns and independently supplied finite-data converse are explicit. The quotient is identified by its invariant local ring. The correction term retains the full original multiplicities and finite sheet permutations. The intrinsic normal-root covers and density threshold identify the canonical-flat versus positive-Hopf branch without a chosen resolution.

The compact paragraph was checked after correction: a Riemann–Roch restriction map prescribes a simple zero at the selected value and value one at every other critical value, with its only possible pole at a regular value. Additional root branch values therefore have smooth product base changes; the original singular fibres elsewhere have unramified base changes. The selected local coordinate and its unit root comparison are retained. This proves the stated compact comparison without silently ignoring extra singularities.

The result is an exhaustive **finite generative classification of actual fibres**, with necessary and sufficient finite map data and the exact Euler-zero selection. It supplies both construction directions and recovers each original neighbourhood from its actual endpoint. It does not claim a unique reduction record or identify different analytic core neighbourhoods from equal central log data. Those retained transverse parameters do not leave an unclassified type of fibre in the stated generation theorem. No further mathematical gap was found in the requested C.2 extension.

## Current editorial scope

At the audited source snapshot, no current `part_*.tex` proof passage asserted that the unrestricted C.2 problem remained unresolved. The working paper's opening incomplete label and the many chronological report entries still needed their root-owned completion update. Those historical passages should be retained as dated prior states or preserved in the existing versions/checkpoints, not treated as current mathematical conclusions. The root agent owns that editorial update and the final PDF/render verification.

Prompt rule 8 also requests the literature position of each requested item. The final report should make that correspondence explicit alongside its completed outcome table: known result with the checked derivation, a new proof of a checked assertion, a refutation of a specified printed assertion, or no matching statement located in the recorded searches. The verified bibliography and item-specific primary-source discussions supply the evidence; they should not be converted into an unsupported priority claim. This is a reporting requirement, not an additional unresolved mathematical clause.

The inventory checks are not themselves mathematical proofs. The completion assessment above rests on the full UN85–86 map audits together with the separately recorded proofs and independent audits of their dependencies; the catalogue simply verifies that those statements and every requested item are actually present in the deliverables.
