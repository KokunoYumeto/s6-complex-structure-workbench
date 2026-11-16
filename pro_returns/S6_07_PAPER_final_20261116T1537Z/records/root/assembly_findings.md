## Assembly decisions, source discrepancies and limits

The paper retains the binding T/K/A assignments and the selected proof architecture. These assignments describe the supplied work and the requested presentation; they are not a fresh independent validation of the mathematics. Conflicting instructions are identified below. Consequently, this report does not claim that both sides of each conflict have simultaneously been satisfied.

### 1. Missing computation artifacts

FAM C.2.3 and PUSH E.4 are retained with T status. The attached TeX and status files describe the norm-box certificate, the local treatment, and a second certification using Arb. Neither archive supplies the certificate data or the verifier programs. The paper therefore gives the reported counts, precision, software information and bounds, while explicitly marking unavailable bytes, hashes, original invocation details and machine specifications. No certificate was reconstructed, no substitute floating-point grid was treated as a proof, and no present-session certificate execution is claimed. The complete selected ARI C.8.1–C.8.5 duplication ladder is printed beside this record.

The first certificate account has 19,911 leaves in all: 19,701 norm boxes, 36 local boxes, and 174 outside boxes. The supplied review reports rerunning the 19,701 norm boxes with identical results. The Arb account reports area 23/40, depth 38 and upper bound 1.999877571767410525. These are historical/source-run records. Their presence here does not imply access to the missing files.

FAM C.1.2 is also retained with its complete statement and proof because FAM A.4.1 invokes its special-value interval. Its named numerical and special-interval programs and complete outputs are absent. Its proof's tail estimate and description of the historical evaluations remain intact. Other source-proof references to exact or numerical programs are likewise historical descriptions, not new executions by the assembler.

### 2. Conflicting quotation requirements

Prompt condition 13 requests the sentence as printed in AC26 Remarks 1.3 and 9.21, while condition 12 forbids reproducing any AC26 text. Both cannot be obeyed literally. The paper follows the explicit prohibition: it gives exact locators, a labelled paraphrase, the source-run corrected assertion and the reason. The literal-quotation component is therefore not fulfilled. This conflict is named in the paper's Limits part and in the cohomology record. Engel's wording is supplied as permitted quotation, including the complete Conjecture 8.2 target.

### 3. Binding status and proof placement versus generic known-result format

The specific table requires T status and full proofs in the main text for several statements or components already in AC26 or in standard torus theory. The generic format instead describes known results as K/New proof, with re-derivations in Appendix B. The paper preserves the specific binding statuses and proof placement, labels the relevant contribution as a new proof, and credits the known statement. This affects, in particular, INV A1.0's structure-sheaf direct images, FAM B.1.3's geometric zero interpretation, the AC26 parts of FAM D.1–D.2, and the standard torus results requested in §9. It does not convert a known theorem into a novelty claim.

The audit located the exact Néron–Severi equation in AC26 Lemma 9.2; the related independence, indefinite class and generic assertions in Lemmas 9.3–9.4, Proposition 9.5 and Corollary 9.8; and the special-fibre normalization and conductor geometry in Proposition 4.6. The elliptic-logarithm interpretation is already in AC26 Remark 3.12. All receive explicit credit. The supplied FAM headings “Known, with derivation” for D.1.2, D.1.6 and D.2.3 yield to the prompt's binding T heading, with their credit retained.

### 4. Standard scope and the exact source of the intrinsic-pencil companion

FAM A.1.1 states an intrinsic-pencil result for every admissible affine translation and cusp collar. DGKXv1 Theorem 7.1 is the standard-data known result. Their scopes are not identical. The FAM statement and its proof are retained, while the credit table identifies the extra scope instead of attributing it to the known theorem.

The all-maps-to-P¹ assertion is not literally a separate clause of FAM A.1.1. Its supplied source is DGKXv1 Theorem 7.2, labelled `thm:all-maps-factor`. That exact statement is credited as K; the supplied proof is printed in Appendix B. This addition implements an explicit requested row, using an attached source rather than a newly devised theorem.

### 5. The standard 2Z theorem and workbench proof

The standard-data classification is stated as DGKXv1 Theorem 1.4. The paper contains the requested single sentence that version 2 does not contain it and the requested independent-workbench sentence. Appendix A preserves the complete mathematical content of `workbench/period_shift_classification.tex`, in the common notation. Its original equation tags remain. No comparison of dates or result precedence is made.

Three missing internal source labels in that workbench file are editorially resolved: `ffcert:normalization` points to FAM A.1.2, `period-input-audit` to FAM A.3.1, and `canonical-ring` to FAM A.1.1. These are reference repairs; no proof argument is supplied to replace a missing mathematical step. The exact transformation is reproducible from `records/scripts/build_root.py`.

### 6. Higher multiplicities, conditional cover dependence and the open list

FAM B.3.1 proves the 2klZ identification only in its stated model and marking. PUSH E.1 supplies a separate announced dictionary to the Viaclovsky coordinates. That dictionary remains A; the theorem is not silently transported across it.

INV B3.2 has binding status T, but its supplied proof invokes INV B1.2, whose binding status is A. Both statuses and the dependency are retained and expressly disclosed in a Uses line and the Limits part. This is an unresolved source dependence, not a gap patched in this assembly.

MAPS B.6.24 announces trivial monodromy for every admissible coprime sphere pair in its stated fixed-twist scope. The §12 question about other families is therefore phrased for families beyond that scope, including the two-parameter, comb and Liu–Rollenske constructions. The source announcement is not weakened. The proposed interpretation J = epsilon(P.O) remains an unverified reader remark and is not used as an input.

### 7. Mixed statements partitioned to implement the binding table

INV B2.1 combines a canonical formula and Hodge clauses. The paper separates its exact content into a canonical T statement and a Hodge A statement, repeating the hypotheses. PUSH A.3.2 ends its Euler obstruction with a sentence about replacement fillings; its obstruction remains T, and that final mathematical sentence is a separate A statement, followed by the full selected filling announcements. No mathematical sentence is discarded by these partitions, and the ledger records each change.

PUSH E.2.1 is the sole printed source theorem and proof for §6c. CDP E11 is recorded as corroboration of the common tangent-cohomology conclusion, not merged into an enlarged theorem. The exact qualifier “two runs, no second reader” is preserved.

### 8. Required supporting source material and the local corollary

Supporting source proofs FAM A.1.2 and A.4.1 and INV A4.1, B1.1 and B3.1 are printed where the selected arguments require them. The standard-data valuation/monomial argument used by INV B3.3 is extracted from its own source B2.2 with the existing (k,l) = (1,1) specialization; no general conclusion from that source is imported. The cotangent/conormal argument needed by CDP C5b is taken from the supplied INV D1.3 paragraphs, because its original CDP C5a dependency is outside the requested selection. These source transfers are disclosed in the cohomology record.

The §6d algebraic-dimension corollary is the explicit consequence described in REVIEW_S6_02_FAMILY, F4, and RESPONSE_INTAKE §1.3, using FAM A.5.2. It is not literally a separately numbered FAM A.5.2 clause. The ledger cites the actual status-file source, and the paper asserts only the requested neighbourhood of the standard family. The optional comb sentence is omitted; no excluded comb theorem is imported.

### 9. Proof order and source locators

The fixed section order leaves ARI C.2.1 and C.8.6 using the maximum whose full proof is in §4; several proofs refer to supporting re-derivations in Appendix B. INV A2.4's counterfactual final clause points to the residue calculation. These dependencies are explicit. The generic no-forward-reference rule cannot be satisfied without changing the fixed source order or redistributing its statements; no clause is deleted to conceal a dependency.

ARI C.8.4 refers to division polynomials from C.4.2, although C.4.2 is the division identity and the explicit higher polynomials are in C.4.4. Its source proof wording is retained; the Uses line identifies both. The FAM citation to Shioda's “Table 8.9” is corrected to the actually opened local-contribution table (8.16), p.229, with Theorem 8.6 on p.228. The two unsuitable DGKX lemma citations in the FAM A.5.2 re-derivation are replaced by opened analytic base-change and duality references. A resulting grammatical artifact was found on rendered page 56 and corrected; the exact intermediate-to-final diff is retained.

### 10. Notation changes and ambiguities

The complete mapping is in `S6_07_PAPER_notation_sheet.md`, Appendix C.4, and the scoped transformation records. Distinct symbols separate the modular nome from the two Albanese nomes, the modular discriminant from a parameter disc, the theta norm from determinant or Bott–Chern notation, the root base from its coarse curve, and elliptic-curve lattices from the rank-four period lattice. Labels and equation identifiers are protected from symbol substitutions.

FAM's cubic section and ARI's rational division model differ by the recorded homothety and sign: x_F = 2 x_div and y_F = −2 sqrt(2) y_div. The normalization is stated rather than silently equated. MAPS' shorthand S(t)d adds a lattice vector to a fibre vector; the printed formula uses S(t)e with e = Pi_c d explicitly. FAM D.1.4's otherwise locally undefined U is identified as Im(mu), without changing its matrices. The circle action is rho_circ, reserving rho for exp(pi i/3). Other purely local collisions and bibliography-key changes are itemized in the sheet.

Three formal definitions intentionally combine separated exact excerpts: the period shears and monomial equations in PUSH A.2.4, the standard-family scope from the PUSH conventions, and the hypotheses/parameter from PUSH E.2.5 and E.2.7. Each component is checked against its actual source. The final source-path audit found that three `additional_sources` fields were present in detailed records but not yet promoted into the compact CSV/printed path column. The writer now includes every such path, including `E_zero_period_obstruction.tex`. This is a traceability correction, not a mathematical change.

### 11. Literature availability and bounded attribution

AC26 was checked in the supplied AI transcription, not an original PDF. Every corresponding bibliography note says so. E26, DGKXv1/v2 and the relevant Viaclovsky source were checked in the supplied full TeX. The fresh opened-source ledgers identify the exact external work, URL, locator and matched scope. Negative checks mean that the recorded searches did not locate the complete statement in those three supplied prior-source files; they do not establish absence from the literature.

The Gray article was not obtained despite fresh searches. Its bibliographic identification is retained as unverified background, and it is the only uncited bibliography entry. It supplies no mathematical premise. The repository URL was supplied by the prompt; public retrieval returned a failure. Its availability is marked unverified, and all announcement pointers give only the supplied run and statement identifiers. No repository path, public opening or unseen proof is invented.

The intake also credits the numerical Hodge table to a workbench calculation by GPT-5.6 Sol (Codex reasoning effort ultra), based on a degree count for the scalar. That Hodge proof is not an attached workbench file and was not freshly opened here. The Known-and-new table and A3.1 source row state this bounded historical credit, while attributing the displayed determinant identity and closed scalar to INV. This is separate from the attached and printed period-shift workbench proof.

### 12. Runtime and presentation repairs

The workspace's installed LuaLaTeX binaries initially lacked usable format/cache/font-map support and Lua dependencies. A local runtime repair used genuine upstream Lua packages and the installed TeX sources; URLs and hashes are recorded in `records/build/runtime_packages.json`. No fabricated substitute library was used. The final single TeX file uses standard packages, an inline bibliography, no external images, no external input commands and no shell escape. It can be compiled directly with a complete standard LuaLaTeX installation; the workspace-specific helper is optional.

The first complete PDF's overflows were confined to Appendix C. They came from URLs, long identifiers, literal Markdown tables and narrow headers. The source was corrected with breakable paths/identifiers and real LaTeX notation tables. A preliminary abstract overflow was fixed by changing fraction layout, without changing a formula. Intermediate missing Unicode glyphs and label corruption from overly broad substitutions were caught and removed. The rendered verification table also exposed a schema mismatch in eleven source-check records: their separate citation_key, match and effort fields had not been carried into the combined table. The aggregate writer now preserves the exact citation key, matched scope, local-source routing and model effort for each; the original ledgers were unchanged. The final audit reports the actual log counts and rendered-page review below; it does not conceal warnings by increasing an overflow tolerance.

## Component records

The following retained records give the statement-level details from each assembly scope. Where a finding overlaps the integrated account above, it describes the same disclosed issue. These are assembly and source-fidelity records, not independent referee reports.
