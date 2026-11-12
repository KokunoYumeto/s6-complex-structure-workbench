# S6 annotated mathematical proof audit

Canonical Overleaf project: <https://www.overleaf.com/project/6a8ca9bd0c2a1270c91e5ce1>  
Current public read link: <https://www.overleaf.com/read/rtmyqxyrzprn#fa24eb>

## Start here

1. `main.tex` — the project-compilable 123-page annotated edition and the Overleaf main document. Physical pages 1–2 are the independent review record; page 3 is the subsequent Codex validate/repair/disprove results block; pages 4–111 are the 108-page reconstruction; pages 112–123 are the preserved indexed review appendix.
2. `original_clean_transcription.tex` — the self-contained 108-page clean LaTeX reconstruction without the annotation layer.
3. `supporting_materials/` — every review, source/provenance file, verification artifact, reference PDF, receipt, and archive, grouped by purpose and indexed by its own README.

Both root TeX entry points compile with pdfLaTeX in this project. The clean transcription is a standalone file; the annotated main document imports its editable corrective-results source from `supporting_materials/audit_annotation_sources/`. The root is deliberately kept human-facing: the annotated edition first, the clean reconstruction second, and all evidentiary material in one organized subtree.

## Methodology

The authority PDF was first transcribed to LaTeX in ten-page strips by ChatGPT Pro mode and then consolidated. Two separate ChatGPT Pro-mode threads performed full mathematical reviews as literal peers of the Claude model reported to have produced the mathematics. Codex consolidated the sources and reviews, performed the third mathematical and TeX audit, built the page-linked annotation layer, and organized this Overleaf edition. The web work used ChatGPT Professional Pro mode; the local Codex work used ChatGPT 5.6 Sol in Ultra mode.

## Status

The 24 August review recommendation and all of its page-level annotations are preserved as historical evidence.  The subsequent complete-source work records two exact defects in the published CDP dependency chain and reconstructs the candidate's construction, topology, algebraic-reduction, and analytic Picard arguments.  In the current workbench, construction, intrinsic specialization/Leray, based van Kampen/sphere recognition, algebraic reduction, and Proposition 10.8 uniform non-torsion are marked **VERIFIED** in the local sense defined there: a complete auditable proof is written in the workbench.  The optional cellular-collapse/Mayer–Vietoris comparison and external CDP adjudication remain **OPEN**.  Frozen reviewer labels are not silently rewritten; the current status is governed by the front matter and the workbench ledgers.
