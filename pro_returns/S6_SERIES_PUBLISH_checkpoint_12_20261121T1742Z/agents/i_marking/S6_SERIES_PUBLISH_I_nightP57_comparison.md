# Paper I night:P5.7 — full-proof comparison, source receipt, and history scope

## Outcome

**PASS for the mathematical and source-content comparison.** The complete receiving proof agrees with the frozen derivation: the difference of particular beta solutions is a constant, the exact parameter map is a=c+delta with the displayed inverse, the admissible half-planes map bijectively, the core/finite/cusp chart arrows agree, and the four standard-data conclusions compare with the cited v1 assertions. The complete v2 statement inventory supports the claimed omission of those four assertions.

**One attribution guard is proposed at the root's explicit request.** The September 8 history is supported by the supplied authorial chronology; an independently dated public deposit on that day has not been authenticated in this check. The official September 23 submission date is directly present in the retained arXiv HTML. The guard preserves the required chronology and changes only its attribution. It makes no mathematical change and does not refute the reported historical fact.

The checker did not modify the main TeX. No mathematical guard is proposed. No aliases receive check credit.

## Exact chronology of this check

The frozen derivation was completed at **2026-11-21T03:56:57.098276+00:00**, SHA256 `944914a7daa9397c912afdd8ccd4062023e4dd9dd4dcbb5ac4b04ffb67eb81c2`. The freeze manifest SHA256 is `cea89a074fb9c85da400ee427ee047ba4ac664a09783fd3cd33dfe4f457b547f`.

The complete receiving target proof was first opened at **2026-11-21T03:57:09.992605+00:00**. The source snapshot SHA256 was `dc9350391c46d4ef5232224bfd3386aaf5f58f648c8f474954fcb90a02cafd03`. The exact statement hash is `61460a90f9ceec30c20bf37e7df11472efa52677f7f5e491e7018c2788349648`; the complete proof hash is `d68495607e51dc909d8f4f0cd8c6fa889adf3e2058bb16cbea7c0901e31d658c`. The target occupied lines 30835–30882 in that snapshot.

The expected formula a=c+delta had been named in the root's assignment before this derivation. Prior inv:B1.0 inputs exposed the period/parameter definitions and covariance matrices. Both exposures are disclosed. No receiving P5.7 proof or earlier parameter-comparison report was opened before the freeze. The delta definition, sign, domain mapping, and all chart/coefficient derivations were developed from the supplied statement/primary inputs before target-proof exposure.

## Claim-by-claim comparison

| Target/proof assertion | Frozen derivation and evidence | Resolution |
|---|---|---|
| Same fixed oriented triangle, lattice, twists and cusp data | Literal receiving adoption plus primary construction inputs; exact ordered-basis identity and v1,v2 shown | Same fixed standard scope |
| beta_part-beta0 is constant | Reconstructed equal increments; invariant difference descends across finite root points by power series and across the cusp by extension; compact P1 maximum principle | Same argument as complete proof, with hypotheses explicit |
| delta sign and parameter map | delta=beta_part-beta0=-(beta0+tau)(p0); a=c+delta, c=a-delta | Exact agreement |
| Period matrices agree | All common entries identified; varying entry reconstructed by exact affine coefficient equations | Omega_(c+delta)=Pi_c |
| Admissible half-planes agree | M=M0+Im(delta); Im(a)+M0=Im(c)+M | Exact bijection with displayed inverse |
| Ordinary, finite and cusp charts identify | Explicit identity in zeta/root/toric coordinates over parameter translation; equal lattice arrows, finite translations, and C_a(q) coefficients | Complete fixed-data atlas morphism supplied |
| Exact period | a'-a=c'-c; F(c+2n)=F(c)+2n; signs related by 2n -> -2n | Same 2Z subgroup and quotient map |
| Tangent tuple and Kuranishi conclusion | Receiving theorem specialized at k=l=1; actual v1 pp.3,81–82,85 read | All hypotheses retained; conclusions coincide |
| Full automorphism group | Actual v1 Theorem1.4 p.3 and Theorem7.14 p.95 read; Phi conjugates each alpha-translation to itself | Full group, not only an unexamined identity-component claim |
| v2 omission | Actual front matter pp.1–3; complete 42-statement source inventory and all relevant whole-source contexts reviewed | Textual omission of four assertions supported |
| Re-derived-after-reading work history | Received authorial statement | Retained as reported process history; no independent authentication claimed |
| September 8 / September 23 history | Authorial working-edition assertion versus exact official retained submission history | Proposed wording attributes the former; latter directly supported |

The target proof's citation of Theorem1.4 for full automorphisms is supported directly: the actually viewed p.3 theorem includes Aut(X_a)=C*. The additional actual read of Theorem7.14 supplies its explicit full-group statement. No change to that citation is required.

## Exact new computation and method relation

The new standard-library exact program is `S6_SERIES_PUBLISH_I_nightP57_exact_reconstruction.py`, SHA256 `72aa987a0df7c549b42467be7703a3f59eca1c9fb154ba41dd45d661d0aa0d0e`. Its full output has SHA256 `4966335b4e8081a810f90a8e9bd49c1c9e72d9f400cd91ecf2e4707144c52a44`. It was written and executed before the target proof was opened, and every exact assertion passed.

The program constructs polynomial coefficient equations for unknown scaled generator values (tau*tau', tau*mu', tau*(beta'-beta)), then solves the integer coefficient systems by Cramer's rule on nonzero integer minors. It reconstructs the primary/receiving generator laws before inserting their values and checks all covariance entries. It then reconstructs the affine parameter coefficients, verifies the varying period entry, cusp E21 entry, parameter differences, 2Z-equivariance, half-plane affine forms, and logarithmic radius identity. No floating-point sampling is used.

The complete target proof verifies the parameter equality by direct substitution. The relation between the methods is explicit: the proof evaluates Omega at a=c+delta, while the program first solves the coefficient conditions for the unknown affine map and reconstructs the generator transformations from the full covariance equations. They share the same exact input data.

After freezing and comparing the proof, a bounded search for P5.7 legacy code was performed. Relevant nodes of `agents/i_analytic/S6_SERIES_PUBLISH_I_residual_guards.py` and `code/S6_SERIES_PUBLISH_I_front_status.py` were inspected. They contain editorial source substitutions and references to the already compared map, with no dedicated algebraic verifier in those inspected nodes. `agents/i_provenance/code/S6_SERIES_PUBLISH_I_finish_boundary_reread.py` supplies the input supplement. The exact inspected excerpts and full file hashes are retained in `S6_SERIES_PUBLISH_I_nightP57_legacy_method_exposure.json`; no legacy script was run or imported. No assertion is made about an unlocated or uninspected historical verifier. The method comparison established here is against the actual complete proof's substitution and the actually inspected editorial nodes.

The documentary scanner is a separate new program. It parses actual TeX environment boundaries after removing line comments with source offsets preserved. The full inventory contains 42 mathematical statement blocks: 7 theorems, 15 propositions, 14 lemmas, 4 corollaries, 2 definitions. The checker read all extracted blocks and all relevant whole-source contexts. This supports the printed-content comparison, with no claim of full rendered-page review or independent proof of all v2 results.

## Primary exposure, citations, and limits

Actually viewed primary pages: DGKX v1 pp.3,81,82,85,95; DGKX v2 pp.1–3; AC2026 pp.14–15. Full visible pages, including surrounding primary proof text, were read. The supplied PDFs, page images, source files, HTML dates, intake packets, and supplement are content-bound in the 30-file freeze manifest. This checker did not newly download/authenticate their remote origin; it used the authenticated local primary inputs and read the cited content itself.

The September 23 date is directly printed in the retained official HTML, including timestamp `Wed, 23 Sep 2026 17:09:17 UTC`. The received original Paper I reports a public working-edition proof by September 8. This check preserves that report with attribution and supplies no independent deposit timestamp. A later repository commit cannot by itself establish the earlier public-availability date. The same authorial-evidence qualification applies to the claimed order of re-derivation after reading v1.

An initial scaled-image misreading of AC p.15(iv) was corrected before freeze: the primary sign is minus infinity. A 3x PDF-region rendering and extracted text confirm it. The mistaken caveat was explicitly retracted to root and provenance. No source-sign correction or defect row is warranted.

The mathematical comparison uses the receiving cited theorem statements as inputs; it supplies no new independent proof of their tangent cohomology, deformation theory, full automorphism group, or exact-period theorem. Its new work is the exact source-to-receiving comparison and documentary scope verification. All source hypotheses, base indices, standard twists, cusp condition, and constants 3,4,2Z are retained.

## Guard for root integration

Replace only:

`The working-edition proof of the exact $2\mathbb Z$ equivalence`
`is dated 8 September 2026.`

with:

`Our working-edition chronology records the public proof of the exact`
`$2\mathbb Z$ equivalence by 8 September 2026.`

The root requested this exact publication-facing attribution. The official v1 submission sentence, v2 omission sentence, and plain credited re-derivation statement remain. The exact old/new guard is saved separately and bound to the checked target statement/proof hashes.

## Check accounting

Two event rows are supplied in one evidence group: a targeted proof check and a computation/formal-certificate row. The documentary source inventory is part of that same source-comparison check. No independent date-check event, no source-theorem re-proof event, and no alias events are awarded. Main TeX integration of the attribution guard belongs to the root.
