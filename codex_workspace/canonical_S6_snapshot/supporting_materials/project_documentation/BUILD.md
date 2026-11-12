# Build and verification

## Overleaf

- Main document: project-root `main.tex`
- Compiler: pdfLaTeX
- TeX Live: latest available
- Expected annotated result: 129 US-letter pages
- Expected clean result: 108 US-letter pages
- Expected validate/repair/disprove workbench: 449 US-letter pages
- Expected mathematical overview: 21 US-letter pages
- Expected Koide arithmetic draft: 18 US-letter pages
- Expected spectral-degeneration draft: 87 US-letter pages
- Expected compact-link Gaussian draft: 28 US-letter pages
- Expected cone/sphere-routes draft: 46 US-letter pages
- Expected Erdős--Straus--Koide bridge draft: 12 US-letter pages
- Expected higher-rung SU(3) Gram-cone draft: 17 US-letter pages
- Expected worldline presymplectic-reduction draft: 14 US-letter pages
- Expected publication monograph: 471 US-letter pages

The annotated composition is nine pages of current front matter, 108
unchanged reconstructed manuscript pages, and the twelve-page indexed review
appendix. Source page 71 is therefore physical annotated page 80.

These are the measured 4 September 2026 page counts.  The worldline preprint,
workbench, overview, Koide draft, and monograph have passed the dated full-page
visual inspection recorded in
`C:/Users/user/Documents/math/agent_work/worldline_pdf_visual_qa_20260904/QA_RECEIPT.md`.
For the four independently rebuilt release candidates, every decoded 55-dpi
page raster and every targeted 180-dpi raster agrees with the visually
inspected build; the remaining binary differences are confined to PDF date
and trailer-ID metadata.

## Local builds from the consolidated project root

Keep generated files outside the source tree:

```powershell
latexmk -pdf -file-line-error -interaction=nonstopmode -halt-on-error `
  -outdir=<external-build-directory> main.tex
latexmk -pdf -file-line-error -interaction=nonstopmode -halt-on-error `
  -outdir=<external-build-directory> original_clean_transcription.tex
latexmk -pdf -file-line-error -interaction=nonstopmode -halt-on-error `
  -outdir=<external-build-directory> workbench.tex
latexmk -pdf -file-line-error -interaction=nonstopmode -halt-on-error `
  -outdir=<external-build-directory> workbench_and_manuscript_overview.tex
latexmk -pdf -file-line-error -interaction=nonstopmode -halt-on-error `
  -outdir=<external-build-directory> koide_arithmetic_preprint.tex
latexmk -pdf -file-line-error -interaction=nonstopmode -halt-on-error `
  -outdir=<external-build-directory> s6_spectral_degeneration_preprint.tex
latexmk -pdf -file-line-error -interaction=nonstopmode -halt-on-error `
  -outdir=<external-build-directory> s6_compact_link_gaussian_preprint.tex
latexmk -pdf -file-line-error -interaction=nonstopmode -halt-on-error `
  -outdir=<external-build-directory> s6_cone_sphere_routes_preprint.tex
latexmk -pdf -file-line-error -interaction=nonstopmode -halt-on-error `
  -outdir=<external-build-directory> s6_erdos_straus_koide_bridge_preprint.tex
latexmk -pdf -file-line-error -interaction=nonstopmode -halt-on-error `
  -outdir=<external-build-directory> s6_higher_rung_su3_gram_cone_preprint.tex
latexmk -pdf -file-line-error -interaction=nonstopmode -halt-on-error `
  -outdir=<external-build-directory> `
  s6_worldline_presymplectic_reduction_preprint.tex
latexmk -pdf -file-line-error -interaction=nonstopmode -halt-on-error `
  -outdir=<external-build-directory> `
  supporting_materials/publication/s6_peer_verification_monograph.tex
```

The current modular reconstruction is retained at
`supporting_materials/manuscript_sources/canonical_modular/s6_canonical.tex`.
Its inputs are directory-relative, so use `latexmk -cd` when building it.

## Archival standalone source

The maintainable `main.tex` imports one current front-matter file. Regenerate
the archival one-file edition with:

```powershell
python supporting_materials/reproducibility/annotated_qa/build_standalone.py
```

This writes
`supporting_materials/manuscript_sources/s6_canonical_annotated_standalone.tex`.

## Structural QA

After compiling the clean, annotated, and regenerated standalone PDFs, run:

```powershell
python -m pip install -r `
  supporting_materials/reproducibility/annotated_qa/requirements.txt
python supporting_materials/reproducibility/annotated_qa/verify_pdf.py `
  <clean-108-page.pdf> <annotated-129-page.pdf> `
  --standalone <standalone-129-page.pdf> `
  --output supporting_materials/reproducibility/annotated_qa/verification.json
```

The verifier checks all page sizes and counts, the nine-page physical
offset, all 108 badge links and destinations, source text/coordinates outside
badge regions, and byte identity of the two annotated builds. Dated compile
and visual results are preserved in `QA_RECEIPT.md`; regenerate that receipt
as part of a new release rather than treating an earlier receipt as current.

MiKTeX and Overleaf TeX Live need not produce byte-identical PDFs; page count,
content, link destinations, and clean diagnostics are the cross-engine gates.

## Metadata and deterministic release archive

After installing the six final reference PDFs under
`supporting_materials/reference_pdfs/`, regenerate the live inventory and then
run the fail-closed package check:

```powershell
python supporting_materials/reproducibility/generate_project_metadata.py
python supporting_materials/reproducibility/deterministic_release_roundtrip.py `
  --check-only
```

Create the sibling ZIP, SHA-256 sidecar, and sanitized round-trip receipt with:

```powershell
python supporting_materials/reproducibility/deterministic_release_roundtrip.py
```

The packer fixes ZIP timestamps, ordering, permissions, and compression;
rejects unsafe, duplicate, case-fold-colliding, or symbolic-link entries;
extracts to a unique temporary directory; compares every path, byte count, and
SHA-256 digest; validates the manifest, checksum ledger, file tree, and six
PDF page geometries; and requires a byte-identical second pack before replacing
the release artifacts outside the source tree.
