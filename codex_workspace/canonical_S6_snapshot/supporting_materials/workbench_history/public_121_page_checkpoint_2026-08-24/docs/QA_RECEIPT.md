# Public-project QA receipt

Date: 2026-08-25

The reorganized public tree was tested from its project root with MiKTeX 26.5, pdfTeX 1.40.29, and latexmk 4.88.

## Compile results

| Entry point | Pages | PDF SHA-256 | Result |
|---|---:|---|---|
| `main.tex` | 121 | `41608c05bc19df14314be5245d42bf617756b9c7633e94b8c9fac8b3b1ccbbe4` | pass |
| `clean_transcription.tex` | 108 | `0ba4ff2490fbc67763d9dc596852ab514134833a415beebc12c5f10fe82bec0d` | pass |
| `manuscript/s6_canonical_annotated_standalone.tex` | 121 | `41608c05bc19df14314be5245d42bf617756b9c7633e94b8c9fac8b3b1ccbbe4` | pass |
| `manuscript/annotated_maintainable.tex` | 121 | `41608c05bc19df14314be5245d42bf617756b9c7633e94b8c9fac8b3b1ccbbe4` | pass |
| `manuscript/canonical_modular/s6_canonical.tex` | 108 | `e50936781d0688115650d46ccccd1cf1549a8fa9e3d174695a2385f15d9ee3b2` | pass; provenance form |

All five final logs contain zero LaTeX, package, overfull-box, underfull-box, fatal-error, or emergency-stop matches. The modular input paths were restored to directory-relative form, so both its local scripts and the documented `latexmk -cd` build work. The monolithic forms remain preferred because of the separately recorded modular page-71 portability defect.

## Structural verification

`reproducibility/annotated_qa/verify_pdf.py` returned `passed: true`:

- clean document: 108 US-letter pages;
- annotated document: 121 US-letter pages;
- one reader guide on physical page 1 with no source-page badge;
- all 108 source pages on physical pages 2-109, each with one visible badge and matching appendix link;
- all 108 audit destinations and all 108 source-page destinations present;
- source text and coordinates identical to the clean comparison after filtering only the badge region; and
- main, compatibility-wrapper, and one-file annotated outputs byte-identical in the same environment.

The machine-readable result is `reproducibility/annotated_qa/verification.json`.

## Visual QA

The new guide and source page 1 were rendered at 180 dpi and inspected at original resolution. The guide has clear hierarchy, readable type, no overflow, no clipping, no accidental second page, and no audit badge. Source page 71 was rechecked as physical annotated PDF page 72; its text and `X 71` badge are visible. The appendix start was inspected on physical PDF page 110. Automated link inspection confirms every badge target.

## Exact checks and package integrity

- Reviewer A: 28/28 exact checks rerun successfully; 25/25 internal manifest rows verify.
- Reviewer B: 38/38 exact checks rerun successfully; its summary continues to mark the four geometric obligations as uncertified.
- Superseded packet-06 review: 22/22 exact checks rerun successfully; 21/21 internal manifest rows verify.
- Reviewer C / Codex: 9/9 internal checksum rows verify.
- Reviewer B final source ZIP: all 169 rows were verified during reconciliation; the included compact evidence subset remains explicitly labeled as a subset.

Rerun outputs were compared with the archived receipts and the intact reviewer-package files were restored from their exact source ZIPs after the check, preserving their internal manifests.

## Cross-engine boundary

Overleaf uses TeX Live rather than this MiKTeX environment. Local QA proves package completeness and source preservation, not cross-engine byte identity. The imported Overleaf project must separately show 121 pages, zero compile diagnostics, a clean guide, source page 71, and a working annotation link.
