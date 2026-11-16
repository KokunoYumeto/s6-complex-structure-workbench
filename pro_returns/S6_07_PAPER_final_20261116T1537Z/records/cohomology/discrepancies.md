# Cohomology assembly discrepancies

1. Binding row 5.1 assigns T and a text proof to INV A1.0, whose Rq O result is explicitly credited by the return to AC26 Proposition 9.13 and is also in DGKXv1. Retain T and the full text proof as the specific instruction; mark kind New proof and credit both sources. This conflicts with the generic request to move every known-result proof to Appendix B.
2. The correction format requests literal sentences from AC26 Remarks 1.3 and 9.21, while condition 12 forbids reproduction of any AC26 text. Exact locators and a labelled paraphrase are used; the literal-quotation requirement is not met.

3. The binding T statement inv:B3.2 invokes inv:B1.2, which the binding map makes A. This source dependency is expressly stated in its Uses line and metadata. Its supplied proof is printed in full; the dependency is not silently removed or independently repaired.

4. The actual rank input inv:A2.4 precedes inv:A1.3. Its explicitly counterfactual final clause still refers to the later residue calculation. The Uses line identifies that clause and dependency; this is not hidden as an acyclic proof order.

5. Historical verification is limited to the supplied review and intake records. INV A1.0--A1.2, A4.1--A4.2, B1.1--B1.2, B3.1, and the metric proofs were not among the fully read proofs in the bounded INV intake. The intake read only the first half of C2.1 and B3.3. C5b's Euler-characteristic check covered n=-1,0,12, not all integers. No new independent proof verification is asserted by this assembly.

6. INV B2.1 combines a canonical formula with Hodge clauses. It is printed as inv:B2.1-canonical (T) and inv:B2.1-hodge (A), repeating every source hypothesis in both. The separation implements the binding status map and is recorded as a statement partition, not as a new theorem or a merged claim.

7. Source support statements inv:B1.1, inv:B3.1, and inv:A4.1 are included with full proofs because the binding statements use them. The existing normal-crossing contraction paragraph from B3.3 has been moved into the proof of B3.1; its later occurrence is a cross-reference. The mathematical argument is the supplied source argument.

8. The proof of inv:B3.3 invoked the valuation and monomial argument of source inv:B2.2. That argument is printed inside the B3.3 proof at the only required pair (k,l)=(1,1), with m1=3, m2=4, d=6. The source's final d=0 exclusion for general pairs is not imported. The weighted variables are consistently interchanged to the first-run convention. This proof-source specialization is explicitly recorded; the B3.3 statement is unchanged.

9. The proof of cdp:C5b invoked an excluded C5a input and earlier CDP material. The matching supplied normal-derivative and fibre-conormal argument from INV D1.3 is printed at that point. The source statement is unchanged; both proof sources are recorded. No all-n numerical check is claimed.

10. The two incorrect DGKX lemma citations in the supplied FAM A.5.2 re-derivation are replaced by opened standard analytic sources: Banica--Stanasila III.4.10 and III.4.12 for proper analytic base change, Ramis--Ruget--Verdier pp. 261 and 264--266 for relative duality, and Ramis--Ruget p. 91 Proposition 2 for the Gorenstein dualizing sheaf. The known tangent and Kuranishi result remains credited to DGKXv1 Theorem 1.3 and its tangent-cohomology theorem; the re-derivation is in Appendix B.

11. Section 6d prints only the requested corollary that all sufficiently small deformations of the standard member have algebraic dimension one. Its provenance is the F4 consequence in REVIEW_S6_02_FAMILY and RESPONSE_INTAKE §1.3, using FAM A.5.2. It does not assert a stability theorem for all complex structures or for all multiplicity families.

12. Source statements about symbolic residuals, numerical values, integer matrices, and computer-produced double-complex tables are explicitly attributed to their producing runs. They were not rerun in this assembly. PUSH E.2.1 is labelled exactly “two runs, no second reader”; agreement with CDP E11 is not converted into a new reader check.

13. The optional combinatorial tangent sentence is omitted. No new combinatorial model or general Kuranishi calculation is introduced to extend the binding scope.

14. The prior-source comparison searches each of AC26, E26, and DGKXv1 separately for every printed claim, records the actual terms and line hits, and inspects relevant positive passages. Negative findings mean only that matching full content was not located in those files; they do not establish priority. The AC26 target prose is not reproduced in any of these records.

15. The source's internal “Part A” references are editorially resolved to the printed direct-image subsection, with its Hodge-diamond reference resolved to the precise Hodge-table subsection. Symbol substitutions are excluded from all label and reference keys, fixing the intermediate invalid identifier without changing any mathematical content.

The current package contains 30 printed formal statements. All have source,
status, proof-location, Uses, and three-file credit records. The machine
checks compare each complete `statement_as_printed` string with the actual
fragment and scan identifier keys for unintended TeX commands. Citation
checks are S checks of opened sources and exact matching scope, not
independent proof checks.
