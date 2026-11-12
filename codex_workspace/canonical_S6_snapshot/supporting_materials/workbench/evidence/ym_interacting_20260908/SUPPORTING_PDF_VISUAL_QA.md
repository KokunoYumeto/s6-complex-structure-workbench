# Supporting draft PDF visual QA

Completed 2026-09-08 at 11:20 UTC. Status: PASS.

These are supporting draft PDFs for the existing project, not a new release.
Compilation and rendering were serial. The required PDF operation marker was
recorded once for the two requested outputs. Neither mathematical source nor
layout source was edited for this delivery.

| Document | Pages actually inspected | PDF SHA-256 |
| --- | --- | --- |
| `wilson_finite_lattice.pdf` | 1-12, every page | `31fd692a982fc32111ed096b9288b7d5165c5319201fa277490effa8484ff8da` |
| `temporal_transfer.pdf` | 1-10, every page | `9dd495e8ddf15c007fbc144b9432930ee4076531ff4842530873d2741214c047` |

All 22 pages were rendered by Poppler at 144 dpi and inspected as complete
original-size images. Mathematical formulas, section headings, references,
page transitions and numerical footers are legible and clear of collisions.
The long covariance formulas, temporal kernel and operator convergence
formulas fit their margins. No clipping, overlap, missing glyphs or visual
defects were found. The explicit nonempty-edge hypothesis is visible in the
transfer document.

Both final TeX logs have zero overfull, underfull or unresolved-reference
diagnostics. Auxiliary files were stable. All source hashes are unchanged by
the build. Exact page-bound checks passed for every extracted text block, and
the footer on each page agrees with its numerical PDF page. The private local
profile name is absent from extracted PDF text and PDF metadata.

`SUPPORTING_PDF_QA_RECEIPT.json` records source and PDF hashes, final log hashes,
individual rendered-image hashes, page bounds, numerical footers and the
complete inspected-page lists. No canonical files, remote files or project
settings were changed by this bounded check.
