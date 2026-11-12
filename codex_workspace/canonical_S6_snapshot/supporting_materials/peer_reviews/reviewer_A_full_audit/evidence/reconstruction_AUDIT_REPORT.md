# Full Canonical LaTeX Consolidation and Audit Report

**Audit date:** 2026-08-24  
**Coverage:** physical source pages 1-108  
**Disposition:** **PASS - no unresolved source-fidelity discrepancy**

## 1. Deliverable audited

The audited deliverable is an independent LaTeX reconstruction of the complete authority PDF represented by ten completed packet archives. It is not the author's original TeX source.

Two source forms are supplied:

- `s6_canonical_full.tex`: one self-contained canonical file, with all ten packet bodies inlined.
- `s6_canonical.tex` plus `parts/packet_01_body.tex` through `parts/packet_10_body.tex`: the maintainable modular form.

Both forms compile to the same 108-page PDF. In the audited environment their PDFs are byte-identical.

| Item | Audited value |
|---|---|
| Physical pages | 108 |
| Page range | 1-108, continuous |
| Page size | US Letter, 612 x 792 points |
| Canonical PDF SHA-256 | `7eddbed85b2817d068d3757ee2247bfcd02d4b410dbb348f7416bc50a3771ccb` |
| Reassembled authority SHA-256 | `912611c9213ed730532f16b30117a32885901d79db8d4a129c134e1193f5b78c` |
| Original full-PDF SHA-256 recorded by every packet | `283bba102dd1d5dc346af81b28145bdaaea6654398d5032e76e97bafb9a858f2` |
| Encryption | none |
| PDF preflight warnings | none |
| Missing or unembedded fonts | none |
| LaTeX warnings/errors/overflow notices | none |

## 2. Audit scope and conclusion

The audit tested fidelity to the supplied authority slices and packet evidence. It covered archive integrity, packet coverage, source inheritance, page markers, prose and mathematical transcription diagnostics, typography, pagination, packet boundaries, PDF structure, font embedding, deterministic rebuilding, and visual comparison of every page.

The final disposition is based on all of the following together:

1. all ten packet completion receipts report `COMPLETE`;
2. all 108 upstream page receipts are present and clear;
3. packet coverage is exactly pages 1-108, with no gap, overlap, duplicate, or omitted page;
4. every physical page has exactly one start marker, one end marker, and one source-page anchor in the consolidated source;
5. all 108 authority/canonical page pairs were reviewed at 200 dpi;
6. all nine packet boundaries were separately reviewed;
7. all pages flagged by extraction diagnostics were separately inspected at full comparison scale;
8. the final PDF passes structural, preflight, renderer-parity, build-log, font, and reproducibility checks.

**Result:** 108 of 108 pages pass. The unresolved-transcription list is empty.

The audit does not independently prove the mathematical claims in the document or verify external bibliographic facts; it verifies that the reconstructed source faithfully represents the supplied authority.

## 3. Input packet audit

### 3.1 Coverage

| Packet | Pages | Page count | Completion | Upstream page checks |
|---:|---:|---:|---|---:|
| 01 | 001-011 | 11 | COMPLETE | 11 clear |
| 02 | 012-022 | 11 | COMPLETE | 11 clear |
| 03 | 023-033 | 11 | COMPLETE | 11 clear |
| 04 | 034-044 | 11 | COMPLETE | 11 clear |
| 05 | 045-055 | 11 | COMPLETE | 11 clear |
| 06 | 056-066 | 11 | COMPLETE | 11 clear |
| 07 | 067-077 | 11 | COMPLETE | 11 clear |
| 08 | 078-088 | 11 | COMPLETE | 11 clear |
| 09 | 089-098 | 10 | COMPLETE | 10 clear |
| 10 | 099-108 | 10 | COMPLETE | 10 clear |

### 3.2 ZIP and ledger integrity

Every supplied ZIP passes a complete `unzip -t` test. Eight packet checksum ledgers pass every listed entry. Two ledgers contain stale metadata:

- **Packet 6:** 4 stale deliverable hashes and one absent ledger-listed optional `assets/README.md`; the QA record states the assets directory is intentionally empty.
- **Packet 9:** 5 stale deliverable/template hashes.

In both packets, the authority PDF, page images, text evidence, and coordinate evidence pass their recorded hashes. The stale entries therefore document input-ledger defects, not damage to the authority material used for reconstruction. Exact expected and actual hashes are recorded in `INPUT_ARCHIVE_AUDIT.md` and `input_checksum_verification.txt`.

The consolidated release does not reuse those stale ledgers. It supplies a newly generated `SHA256SUMS.txt` over the release contents.

## 4. Source consolidation audit

### 4.1 Source inheritance

Packets 2-10 are byte-identical to the actual completed packet body files. Packet 1 differs only by two audited page-2 layout values: horizontal margins and local font size/leading. No prose, symbol, equation, citation, equation tag, or source-page boundary was changed. Detailed hashes appear in `part_provenance.tsv` and `part_provenance.json`.

### 4.2 Canonical preamble

The ten packet-local preambles were replaced by one consolidated 10-point, letter-paper preamble. The principal text and mathematics typography is URW Palladio/Pazo through `mathpazo`, matching the font family embedded in every supplied authority slice. Packet-local shorthand remains enclosed in TeX groups, preventing command-name collisions without rewriting the packet bodies.

### 4.3 Page markers and anchors

Static source verification found:

| Check | Result |
|---|---:|
| Start markers | 108, exactly 001-108 |
| End markers | 108, exactly 001-108 |
| Source-page anchors | 108, exactly 001-108 |
| Duplicate markers or anchors | 0 |
| Missing markers or anchors | 0 |
| Placeholder tokens (`TODO`, `TBD`, `FIXME`, and related forms) | 0 |
| External `input`, `include`, or `includegraphics` in monolithic source | 0 |

### 4.4 Consolidation changes

All consolidation changes are listed in `CORRECTION_LEDGER.md`. They are limited to typography, page geometry, warning elimination, deterministic metadata, and exact modular/monolithic token equivalence. No mathematical or prose correction was silently introduced.

The most consequential pagination check concerned pages 89-98: retaining packet 9's audited 0.55-inch geometry keeps page 98 on its intended physical page and preserves the 98/99 continuation. The global geometry produced a spurious 109th page and was rejected.

## 5. Build and reproducibility audit

Both source forms were built with `latexmk` and pdfTeX under fixed reproducibility variables. The preamble suppresses volatile timestamps and sets a fixed trailer identifier.

### 5.1 Clean-build result

| Check | Modular | Monolithic |
|---|---:|---:|
| Build exit code | 0 | 0 |
| Physical pages | 108 | 108 |
| Page size | 612 x 792 pt | 612 x 792 pt |
| LaTeX/package warnings | 0 | 0 |
| Overfull boxes | 0 | 0 |
| Underfull boxes | 0 | 0 |
| Missing-character notices | 0 | 0 |
| PDF SHA-256 | `7eddbed...1ccb` | `7eddbed...1ccb` |
| Byte-identical PDF bytes | yes | yes |

Repeated clean modular builds were byte-identical in the audited environment. The release scripts regenerate the monolithic source, rebuild both forms, scan the logs, and compare the resulting PDF bytes.

### 5.2 Font audit

`pdffonts` reports every font as embedded and subset. The final PDF contains the expected URW Palladio, Pazo Math, Computer Modern support, Euler Fraktur, AMS symbol, and RSFS fonts. There are no broken-glyph or missing-font warnings.

### 5.3 PDF preflight

The canonical PDF and reassembled authority both open successfully, are unencrypted, contain 108 pages, contain searchable text, have no XFA, and generate no preflight warnings. The final canonical PDF uses letter-size pages throughout.

## 6. Automated transcription diagnostics

Automated PDF text extraction is sensitive to matrices, accents, ligatures, superscripts, stacked notation, and reading order. The metrics below were therefore used to identify pages for additional human inspection, not as substitutes for page review.

### 6.1 Character, order, and token diagnostics

Across 108 pages:

| Metric | Mean | Minimum |
|---|---:|---:|
| Character sequence ratio | 0.9800688923 | 0.8958286861, page 32 |
| Word/order sequence ratio | 0.9649309592 | 0.7853277210, page 9 |
| Token F1 | 0.9815587516 | 0.8190018040, page 9 |

The lowest token result occurs on a matrix-heavy page where the two PDF extractors serialize mathematical objects differently. The authority/canonical image pair was reviewed directly and no content discrepancy was found.

### 6.2 Prose-oriented diagnostics

After filtering punctuation and common mathematical extraction artifacts:

| Metric | Mean | Minimum |
|---|---:|---:|
| Prose sequence ratio | 0.9809986309 | 0.8924302789, page 33 |
| Prose bag-of-words F1 | 0.9890447921 | 0.9416666667, page 32 |

Pages 32 and 33 contain dense mathematics and extraction-order differences. Both were reviewed at 200 dpi and pass.

Detailed CSV and JSON outputs are included for every page. The page audit records the diagnostic values alongside the visual and structural disposition.

## 7. Full visual audit

### 7.1 All-page comparison

The authority and canonical PDFs were rendered at 200 dpi, producing 1700 x 2200 pixel images for every physical page. All 108 pairs were reviewed in ten packet contact sheets. The page-by-page results are in `PAGE_AUDIT.csv`.

The following pages received additional full-scale inspection because of dense notation, lower extraction similarity, layout sensitivity, or continuation risk:

`2, 9, 22, 27, 28, 32, 33, 34, 35, 41, 42, 44, 48, 54, 70, 74, 96, 97, 99, 100`.

All pass. No clipped equations, omitted symbols, duplicated text, substituted black squares, broken accents, or unresolved visible transcription errors were found.

### 7.2 Packet-boundary comparison

Both sides of every packet boundary were checked separately:

`11/12, 22/23, 33/34, 44/45, 55/56, 66/67, 77/78, 88/89, 98/99`.

Page numbering, continuation text, paragraph flow, equation continuation, and geometry remain coherent. The page 98/99 continuation was explicitly verified after restoring packet 9's audited width.

### 7.3 Structural visual checks

| Check | Result |
|---|---|
| Pages rendered | 108 authority + 108 canonical |
| Render dimensions | 1700 x 2200 on every page |
| Blank canonical pages | none |
| Ink touching the 3-pixel page edge | none |
| Footer page-number mismatches | none |
| Intentionally unnumbered pages | 1 and 2 in both authority and canonical |
| Visible clipping or overlap | none found |

## 8. Independent renderer-parity audit

The final canonical PDF was rendered independently by Poppler (`pdftoppm`) and PDFium at 72 dpi. Pages were matched numerically; this corrects a lexicographic filename-order issue in the generic parity toolkit's raw summary.

| Metric | Result |
|---|---:|
| Pages compared | 108 |
| Mean tolerant ink coverage | 0.9987402574 |
| Minimum tolerant ink coverage | 0.9976278905, page 46 |
| Maximum content-bounding-box delta | 1 pixel |
| Pages below 0.95 tolerant coverage | 0 |
| Pages with bounding-box delta over 2 pixels | 0 |

This check found no renderer-specific disappearance, clipping, or displacement.

## 9. Evidence index

The release includes:

- `PAGE_AUDIT.csv`: one row for each of the 108 pages;
- `contact_sheets/`: all 108 authority/canonical pairs arranged by packet;
- `detailed_pairs/low_extraction/`: full-size comparisons for diagnostic outliers;
- `detailed_pairs/boundaries/`: full-size comparisons around all packet boundaries;
- text and prose similarity CSV/JSON files;
- structural visual CSV/JSON files;
- corrected renderer-parity CSV/JSON files;
- source marker, provenance, completion-receipt, preflight, font, and checksum reports;
- upstream packet completion and QA receipts;
- deterministic build and verification scripts.

## 10. Final disposition

The consolidated canonical source builds successfully in both modular and monolithic forms, produces exactly 108 letter-size pages, and has no build warnings, font failures, structural defects, missing page markers, packet-boundary errors, or unresolved source-fidelity discrepancies.

**Final audit status: PASS - 108/108 pages, zero unresolved source-fidelity discrepancies.**
