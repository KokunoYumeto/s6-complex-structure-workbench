# TeX and source audit

## Completeness

- The complete ZIP contains `s6_canonical.tex`, `parts/packet_01_body.tex` through `parts/packet_10_body.tex`, and the self-contained `s6_canonical_full.tex`.
- All 133 entries listed in its checksum manifest verify.
- The static verifier reports source-page markers and anchors 1–108 exactly once, no missing or duplicate pages, and no placeholder packet bodies.

## Builds

- Both entry points compile locally with MiKTeX pdfTeX 1.40.29 to 108 letter-size pages.
- The final logs contain no fatal errors, undefined references, missing-character messages, or overfull/underfull boxes.
- The archive's byte-identity claim is valid for its recorded TeX Live 1.40.26 environment, but does not reproduce under local MiKTeX.

## Confirmed page-71 defect

Under local MiKTeX, modular and monolithic builds differ visually only on page 71. The modular content stream places a phrase beginning “elliptic surface with this homological monodromy…” around x=15,291–15,764 pt, outside a 612-pt page, without a log warning. The monolithic source and packaged PDF render it correctly.

The source locator is a 1,315-character physical line at `parts/packet_07_body.tex:248`, but line length is not the cause. A scratch-only split produced a byte-identical, still-defective modular PDF. Treat the packaged PDF and `s6_canonical_full.tex` as authoritative while the modular-only engine/source-boundary interaction is isolated. Add out-of-page word-box QA as well as cross-engine raster comparison; log scanning alone does not detect the defect.

On Windows, `scripts/generate_monolithic.py` also writes CRLF and changes the regenerated source hash although LF-normalized text is identical. Use an explicit LF newline setting for source-byte stability.

## Prior report

The old report PDF is 18 pages and rebuilds exactly, but its TeX log reports four overfull boxes. The long SHA-256 on page 3 is visibly clipped, and a results path on page 17 overruns. This integrated report uses breakable formatting.
