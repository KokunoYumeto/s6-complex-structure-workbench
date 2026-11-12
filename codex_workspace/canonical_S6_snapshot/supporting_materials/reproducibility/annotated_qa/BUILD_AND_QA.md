# Annotated-PDF build and QA

## Target reference artifact

- PDF: `supporting_materials/reference_pdfs/s6_canonical_annotated_peer_review.pdf`
- Pages: 128, all US letter (612 x 792 pt)
- Composition: eight current-finding and exact-certificate pages, 108 source pages, 12 annotation pages
- PDF SHA-256: regenerate from the current reference PDF before release
- Metadata title: `Annotated peer-review edition of the 108-page S6 canonical reconstruction`

## Reproducible source forms

`main.tex` is the canonical maintainable source. `build_standalone.py` inlines the current front matter, badge layer, and appendix into `supporting_materials/manuscript_sources/s6_canonical_annotated_standalone.tex`. The maintainable and standalone forms compile to byte-identical PDFs in the recorded local environment.

## Automated verification

`verify_pdf.py` checks:

1. 108 canonical comparison pages and 128 annotated pages;
2. US-letter size throughout;
3. no top-right audit badge on the eight front-matter pages;
4. one matching badge link on every source page, accounting for the eight-page offset;
5. all 108 audit and source destinations;
6. word-for-word and coordinate-for-coordinate source preservation outside the badge region;
7. byte equality of preferred annotated builds; and
8. derivative metadata identity.

The current result in `verification.json` is regenerated as part of each
release.  It records the byte-identical maintainable and generated standalone
annotated PDFs and the comparison-PDF SHA-256.

## Visual inspection

For the current release, render all eight current-finding and certificate
pages, the first manuscript page, source page 71, and the appendix start from
the regenerated 128-page PDF. Check for clipping, overlap, missing glyphs, off-page text,
misplaced badges, and unintended pages. The front-matter transition to verify
is physical page 9 / source page 1.

See `supporting_materials/project_documentation/QA_RECEIPT.md` for entry-point
hashes, log scans, exact-check reruns, package-manifest verification, and the
prior 28 August 2026 Overleaf cross-engine result.
