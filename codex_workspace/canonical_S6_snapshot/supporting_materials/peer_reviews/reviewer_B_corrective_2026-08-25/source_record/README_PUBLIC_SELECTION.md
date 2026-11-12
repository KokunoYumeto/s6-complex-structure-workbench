# Reviewer B source-record selection

This reviewer package, together with this `source_record/` subtree, preserves
the portable, nonduplicate material selected from the integrated proof-repair
evidence container identified in
`../../../workbench_history/PROJECT_MERGE_MAP.md`. Corrective reports are in
the sibling `../report/` folder; this subtree contains source extracts,
scripts, manifests, audit tables, and session-visible text.

The selection omits generated page images, TeX build logs, derivative PDFs,
and byte-identical copies already present elsewhere in this project. One
machine-local path in `PRODUCT_PROGRESS_RECORD.md` was replaced by the
corresponding project-relative location; the adjacent historical `.sha256`
therefore identifies the unsanitized record in the external container, not
the portable copy in this folder. Every source-container path is classified
in `REVIEWER_B_ARCHIVE_COVERAGE.json`.
