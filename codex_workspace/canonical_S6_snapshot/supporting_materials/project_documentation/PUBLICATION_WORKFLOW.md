# Publication workflow

This file describes the current consolidated public-edition pipeline.
Historical projects are retained under `supporting_materials/workbench_history/`; they do not
compete with the project-root documents.

1. Reconstruct and source-audit all 108 manuscript pages.
2. Preserve the two complete Pro-mode mathematical audits and the superseded packet-06 review as separate evidence streams.
3. Perform the Codex third mathematical and TeX review and maintain its issue ledger independently.
4. Reconcile the three streams into page-level badges and a reviewer-separated appendix without changing the manuscript pages.
5. Lead the document with the independent Pro-mode findings followed by the
   later proof-level validate/repair/disprove results.
6. Maintain the complete mathematical paper at root `workbench.tex`, with
   its proof inputs under `supporting_materials/workbench/`, and integrate
   only proved changes into the public front matter.
7. Maintain the concise standalone root overview as the cold-reader route
   through the candidate, audit, replacement proof, and CDP consequence.
8. Compile all four advertised TeX entry points and run structural,
   exact-check, warning, privacy, and visual QA.
9. At the final release freeze, derive the public mathematical provenance
   edition from the source session JSONL under the rules in
   `PUBLIC_PROVENANCE_POLICY.md`. Never publish the raw JSONL. Record its
   frozen byte count and SHA-256, retained-event hashes, exclusion counts by
   category, and the editor-visible redaction receipt.
   When the optional complete sanitized conversation edition is included,
   require its generator and independent replaying validator both to report
   `RELEASE_READY`, require an empty unresolved queue, and publish its
   hash-anchored editorial-summary table and validation receipt with it.
   A wider full typed-record annex may also be included when its own streaming
   generator and independent full-prefix validator pass, the unresolved queue
   is empty, every private field is replaced by typed metadata or a certified
   summary, and a separate parent review authorizes inclusion. The private raw
   JSONL, raw tool arguments, and raw tool output bodies remain excluded.
10. Regenerate the reference PDFs, metadata manifest, file tree, SHA-256
   ledger, and Overleaf-compatible ZIP.
11. Round-trip the ZIP and verify every recorded file hash and path.
12. Synchronize the exact tree to the existing canonical Overleaf project,
    compile root `main.tex` with pdfLaTeX/TeX Live, and inspect the opening
    pages, source page 71, a badge destination, and diagnostics.
13. Never open or alter sharing controls; the project owner manages them.

The 128-page annotated edition remains a stable reading record while the
validate/repair/disprove paper continues at root `workbench.tex`. Dated front-matter
updates must identify their evidence boundary rather than rewriting old review
dispositions.

## Final DOI presentation

Current user-directed presentation, 6 September 2026: front a readable PDF
of the key advances and exact results, with direct locations of the complete
proofs. Do not front the source ZIP or a cumulative monograph solely because
it contains the most pages. Preserve every previously released paper and
artifact byte for byte; add dated new files in a consolidated version of
the existing DOI family.

Also include a complete project ZIP carrying the full mathematical sources,
calculations, exact datasets, checkers, results, supporting papers, historical
mathematics and sanitized provenance. Include work not selected for the front
note. Account for every source entry in a manifest; explicitly document
credential/private-material, third-party-literature and build-cache exclusions
without silently dropping mathematical derivations. Preserve the full
mathematics of mixed private/workflow records in public derivatives, with
transformation receipts. Keep original attribution and rights scopes.

Metadata describes what each paper and archive contains and which statements
are proved, corrected, refuted or still open. A bounded new version need not
wait until every research question in the continuing program is solved.
Freeze and verify the results claimed in that version, compile and visually
check its PDFs, round-trip the complete project archive, publish the already
authorized additive release, and anonymously verify public access and all
released byte counts and hashes. Do not seek redundant user authorization.
Keep the online workspace current between consolidated DOI releases.
