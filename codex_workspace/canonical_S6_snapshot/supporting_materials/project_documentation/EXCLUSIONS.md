# Public-mirror exclusions

This Overleaf tree is a complete shareable research package, not a byte-for-byte copy of every local build directory. Omissions are explicit:

1. **Third-party literature PDFs and scans.** Journal articles, books, publisher PDFs, and library scans are cited but not redistributed.
2. **Bulky visual QA derivatives.** Page PNGs, contact sheets, detailed JPEG comparison pairs, and duplicate render directories are reproducible verification debris rather than source.
3. **Build debris.** `.aux`, `.fls`, `.fdb_latexmk`, `.log`, SyncTeX, temporary PDFs, and local cache files are omitted. In addition to being reproducible, some raw logs expose local absolute paths.
4. **The full canonical audit ZIP.** `s6_canonical_108_pages_audited.zip` is 69,059,626 bytes with SHA-256 `5cb503a66ed3ba66b4e42ff507ba381194b8fba8911a90fca18dd4ef391aaabb`. It is too large to embed safely in this Overleaf import. Its substantive TeX, scripts, reconstruction records, packet receipts, clean PDF, and authority PDF are included in browsable form; only the bulky image/log layer and duplicate container are omitted.
5. **The full Reviewer B integrated-evidence ZIP.**
   `reviewer_b_integrated_proof_repair_evidence_2026-08-25.zip` is
   87,012,011 bytes with SHA-256
   `155cf2aa4d243a92cb6a19d28a7ee3412c10de871b5283a4d7a96564fa735821`.
   Its portable nonduplicate reports, source extracts, tables, scripts, and
   manifests are included under `supporting_materials/peer_reviews/reviewer_B_corrective_2026-08-25/`;
   the excluded remainder consists of generated renders/logs, derivative
   PDFs, and redundant release snapshots. The selection policy is documented
   in `supporting_materials/workbench_history/PROJECT_MERGE_MAP.md`, and every archive file is
   classified in
   `supporting_materials/peer_reviews/reviewer_B_corrective_2026-08-25/source_record/REVIEWER_B_ARCHIVE_COVERAGE.json`.
6. **Superseded duplicate trees.** Byte-identical round-trip extractions and
   duplicate compiled outputs are normally represented once. Complete dated
   history/evidence layouts may retain a copy where removing it would destroy
   the meaning of that checkpoint.
7. **The raw annotated-release ZIP.** The original `s6_annotated_peer_review_2026-08-24.zip` has SHA-256 `8280c5c04239e000142132a77834856f97eb4164fbc858b3d0375b3b44e5b084`. Its embedded MiKTeX logs expose local absolute user paths, so the public mirror carries the substantive files in curated form and omits that archive container.

The exact small review/release ZIPs are retained under `supporting_materials/archive/review_packages/`. Their unpacked contents are also included so Overleaf readers can browse and edit them.
