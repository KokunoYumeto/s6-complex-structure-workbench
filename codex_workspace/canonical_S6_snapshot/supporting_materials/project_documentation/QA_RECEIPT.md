# Public-project QA receipt

Historical checkpoint date: 2026-09-03  
Superseding local delta: 2026-09-04

The original body of this receipt records the consolidated mathematical and
publication state at the 3 September checkpoint.  It is preserved below for
provenance; every use of “current” in that original body means current at that
checkpoint.  Historical reviewer records remain separately attributed;
VERIFIED, OPEN, and REFUTED classifications belong to the Codex
validate/repair/disprove layer and are not claims of journal certification or
community acceptance.

## Superseding local delta — 4 September 2026

### Source and ledger state

The canonical root now has exactly 11 standalone TeX entry points: the four
principal reading roots and seven focused companion drafts listed in
`PROJECT_README.md`.  It also has the two root bibliography files
`references.bib` and `s6_cone_sphere_routes_companion.bib`.  Generated build
products and the two AI-ingestible Markdown bundles are separate from that TeX
entry-point count.

The live JSON-Line ledgers parse without error and contain:

- 79 claims: 69 VERIFIED, zero CONDITIONAL, four OPEN, six REFUTED;
- 40 uncertainties: 31 VERIFIED, zero CONDITIONAL, five OPEN, four REFUTED;
- 58 morphisms: 55 VERIFIED, one OPEN, two REFUTED; and
- 164 explicit dependency edges, with no duplicate edge, unresolved endpoint,
  self-dependency, or cycle.

The workbench input closure contains 48 TeX files and 47 input edges, with no
missing target, duplicate edge, or input cycle.  After TeX comments are
removed, it contains 1,515 distinct labels; 1,316 reference commands with
1,682 key occurrences; and 200 citation commands with 205 key occurrences.
All 883 distinct reference targets resolve.  The 66 distinct citation keys are
exactly the 66 distinct manual bibliography keys, with no missing, duplicate,
or unused key.

The newly integrated worldline module contributes four VERIFIED claims and
four VERIFIED morphisms.  The six preserved reviewer suites (127/127), direct
boundary-Picard suite (14/14), analytic all-Picard suite (25/25), cusp-spectral
suite (13/13), and new worldline suite (39/39) together report 218/218 passing
fixed assertions; this is a harness-assertion count, not a claim that all 218
assertions are mathematically independent.  The source packet's 33-check
program was also replayed independently and passed 33/33.  It is reported
separately because the 39-check companion extends rather than merely
aggregates the packet test.

### Current compiled identities

The following byte identities were measured from the current root builds,
the unchanged installed annotated/clean reference PDFs, or the indicated
isolated final rebuilds.  They are build identities, not a claim of completed
visual inspection.

| Artifact | Location at this checkpoint | Pages | Bytes | SHA-256 |
|---|---|---:|---:|---|
| annotated audit | installed reference PDF | 129 | 1,362,369 | 2a8ec028302f230fcbfcd525089bdb8e5839012838b5461ad90d21e38efec92b |
| clean reconstruction | installed reference PDF | 108 | 1,114,711 | 81d2459b35364ee462a0cbc1d49a5ae96cdea4ff3772db1a5288abcfd421adcc |
| validate/repair/disprove workbench | current root build | 449 | 3,876,368 | d91d302fb2cf0fca2a32e39e211eb9fbeaf8e870fd7e905c4d97debfebc4fa35 |
| mathematical overview | current root build | 21 | 573,911 | 853d3013bd68e6e9c68bcb39797a6b79689afac499e6c57b50c2778e5dc4e8f9 |
| Koide arithmetic draft | isolated final rebuild | 18 | 515,628 | c23610a7917bd464f2fef65829bc998c8a23dc6de207b7d502f179dad0cf21da |
| spectral-degeneration draft | current root build | 87 | 1,146,578 | 15f667cb583ee00932ca01ca9dd84902d05b9280175ea9a625575c7aecfc5e11 |
| compact-link Gaussian draft | current root build | 28 | 618,408 | 0fd7b86c048b4f3f20be34aa76cce882ed3e4476006f6e6f61ae289b410b52f2 |
| cone/sphere-routes draft | current root build | 46 | 738,326 | c01b66492a8b6523e88cf2c9ed672ffb9a716329cd148712b0e1d327a0a8973e |
| Erdős--Straus--Koide bridge draft | current root build | 12 | 390,968 | 27ebd03b16d60a3682023c5af72b8947cf8df5975f3a4233854e2ba11cb52698 |
| higher-rung SU(3) Gram-cone draft | current root build | 17 | 462,085 | 3f19a8eccc6e821e1dba990a2e6d3224edf688f3f9170bb93d42fcb9477d7eee |
| worldline presymplectic-reduction draft | current root build | 14 | 477,446 | a7115970a3ba3ee9e3360bc0c1b1edd1ecd51747a7040e882b7a8cd2b6326e99 |
| peer-verification monograph | isolated final rebuild | 471 | 4,156,135 | bc4c4ca950532e5b747446d97bc0edd7d6f53e1cc2fdfd8c1ce037c9879c2dbf |

The overview, worldline-preprint, and Koide logs have zero targeted
diagnostics.  The workbench and monograph logs have no error, undefined
control sequence, undefined reference, or undefined citation; each retains
the same five nonfatal inherited overfull-box warnings.

The 4 September visual audit rendered and inspected every one of the 973 pages
in the worldline preprint, workbench, overview, monograph, and Koide draft, and
also inspected 88 targeted or complete pages at 180 dpi.  It found no blank,
truncated, corrupt, clipped, overlapping, or broken-glyph page.  The exact
release candidates for the first four documents differ from the inspected
builds only in CreationDate, ModDate, and trailer-ID metadata: all 955
extracted page texts and decoded 55-dpi raster hashes agree, as do all 70
targeted 180-dpi raster hashes, page boxes, rotations, and UserUnit values.
The 449-, 21-, 18-, and 471-page binaries are now installed in their canonical
root or reference-PDF locations.  The authenticated Overleaf round trip
remains pending; no final remote-identity claim is made in this delta.

The annotated PDF's measured 129-page map is pages 1--9 for the review and
current-results front matter, pages 10--117 for the 108-page reconstruction,
and pages 118--129 for the indexed historical review appendix.

## Preserved 3 September checkpoint

The following sections are the dated checkpoint and intentionally retain its
then-current file counts, hashes, validation reports, release preview, and
remote-sync status.

## Canonical root

The project root contains exactly eight standalone TeX entry points, two
bibliography files, and one supporting tree:

- koide_arithmetic_preprint.tex
- main.tex
- original_clean_transcription.tex
- references.bib
- s6_compact_link_gaussian_preprint.tex
- s6_cone_sphere_routes_companion.bib
- s6_cone_sphere_routes_preprint.tex
- s6_spectral_degeneration_preprint.tex
- workbench.tex
- workbench_and_manuscript_overview.tex
- supporting_materials/

It has no reparse point or case-fold path collision. Exact file bytes and
hashes are regenerated into
supporting_materials/metadata/PROJECT_MANIFEST.json and SHA256SUMS.txt; those
machine ledgers, rather than this self-containing prose receipt, are
authoritative for payload size.

## Current publication PDFs

All five publication binaries were built from the canonical sources through 3
September 2026. Generated TeX products remained outside the source tree; only
the reviewed reference PDFs were installed under
supporting_materials/reference_pdfs/.

| Artifact | Pages | Bytes | SHA-256 |
|---|---:|---:|---|
| annotated audit | 128 | 1,355,022 | 71ab4e07f1752d6ff49ce696f72203bc9262d6ddbe339a5eb3ffe4e17a633b29 |
| clean reconstruction | 108 | 1,114,711 | 81d2459b35364ee462a0cbc1d49a5ae96cdea4ff3772db1a5288abcfd421adcc |
| validate/repair/disprove workbench | 283 | 2,582,279 | f234b9fc9710bf7074bbfda4a5031a93c8aaa230f192327a3ad0aaba0edafe8e |
| mathematical overview | 10 | 457,863 | 2462767c3df7038e5e54a4c2914d785e1f5ede9551cfa260d65ca14b2076b565 |
| peer-verification monograph | 294 | 2,788,757 | d48af790408ca4182d286dd24f3c8547e46057c4c00621e42808d06bcae3efa4 |

The five fail-closed reports under
supporting_materials/reproducibility/publication_pdf_qa/ all have passed=true.
Each PDF parses strictly, is unencrypted, has only unrotated US-letter pages,
has readable text and nonempty content on every page, embeds every used font,
and resolves every internal link destination. The reports record respectively
566, 420, 1,708, 13, and 1,722 named destinations; 146, 4, 1,342, 0, and
1,344 link annotations; and 22, 18, 38, 27, and 46 unique fonts. Their error arrays are
empty.

The final local compile logs contain zero targeted TeX errors, package errors,
LaTeX/package warnings, undefined controls, undefined references or citations,
missing files, overfull boxes, and underfull boxes. Visual inspection covered
the annotated opening and current-results pages, the monograph orientation,
the terminal CDP and Picard argument, and the resulting page transitions; no
blank page, clipping, overlap, broken glyph, unreadable formula, or margin
defect was found.

## Annotated-source and clean-source identity

The annotated page map is:

- physical pages 1--8: independent review records and later exact
  validate/repair/disprove certificates;
- physical pages 9--116: the source-faithful 108-page reconstruction; and
- physical pages 117--128: the indexed historical review appendix.

supporting_materials/reproducibility/annotated_qa/verification.json passes
every structural gate: all 108 source-page destinations and every audit
destination exist; each badge resolves to its matching appendix entry; all
pages are letter-sized; and the annotated source text and coordinates agree
with the clean PDF after badge regions are filtered. The generated standalone
annotated source and maintainable annotated source compile byte-identically to
the 128-page hash above. The clean comparison hash is the 108-page hash above.

## Mathematical ledgers and exact certificates

Every JSON-Line research ledger parses, every identifier is unique, and every
dependency identifier resolves:

- 75 claims: 65 VERIFIED, zero CONDITIONAL, four OPEN, six REFUTED;
- 40 uncertainties: 31 VERIFIED, zero CONDITIONAL, five OPEN, four REFUTED;
- 54 morphisms: 51 VERIFIED, one OPEN, two REFUTED; and
- 157 dependency rows, with no duplicate edge or missing claim identifier.

The current TeX corpus has 147 citation commands containing 148 uses of 47
distinct citation keys and 47 distinct bibliography-item keys, with no missing
or duplicate key. It has 177 distinct labels, 328 cross-reference commands,
448 cross-reference uses, and no unresolved or duplicate reference target.
This audit strips TeX comments before collecting citation and reference
commands.

Six retained reviewer/check packages account for 127/127 passing exact
assertions: 28/28, 14/14, 38/38, 17/17, 8/8, and 22/22. The current direct
boundary-Picard certificate passes 14/14 additional exact checks, and the
current analytic all-Picard certificate passes 25/25. Thus the retained and
current exact-arithmetic evidence passes 166/166 assertions. The exact JSON
results and scope notes remain beside their scripts; finite arithmetic is not
silently substituted for the geometric proofs written in the TeX sources.

## Public provenance

The short mathematician-facing chronology contains 26 selected milestones.
It is 21,147 bytes with SHA-256
70aa383a1706bd2b5701ded15707b8cf221a82f8d198bbb98b7c97a065773e80.
Its selection table and receipt verify every retained source ordinal,
timestamp, and source-text hash against the frozen private prefix while
publishing no private raw session record.

The optional complete sanitized conversation edition also passed its separate
fail-closed gate. After structurally excluding 166 platform-injected
context-only user-role records, it represents all 976 actual human/assistant
natural-language events: 190 user and 786 assistant events. Of these, 940 are
verbatim-redacted and 36 abusive/profane user turns are represented by neutral
editorial summaries anchored to their exact private-source text hashes. An
independent replay verifies all 36 summaries, every event anchor, deterministic
derivation, canonical JSONL, output hash, receipt count, and privacy scan. The
unresolved queue is empty and both programs report RELEASE_READY.

| Sanitized-provenance artifact | Bytes | SHA-256 |
|---|---:|---|
| complete conversation JSONL | 726,648 | d69f2f5d3901a2c3988cef5791d6b80d1072a579479dfe34730a4593d0126132 |
| editorial summaries | 23,673 | 343a75c177a1e20d83348d1f4da39ba35c762d83cf877d22fea21d767e2c26a9 |
| redaction receipt | 3,657 | b32372a9125167d798748beeb5493817137bb7b308f2cee314ba9b65124afd1d |
| independent validation report | 3,601 | 9bd0f1cd701a03e66748b24b1cd5f390f3356f90b4899f53cb1ecea78b0057ab |

The private 1,433,492,250-byte source prefix has SHA-256
65f0ecc4d0e16fc3f178c2c6c8cc7e991d6dee5af0eb7e8343e4a9cc89029156
and is not a publication payload. The public edition contains no system,
developer, tool, compaction, goal, ambient-UI, AGENTS-context, or delegated
control record.

The wider optional typed-record annex uses a later, separately frozen
1,483,338,786-byte prefix with SHA-256
d9991d392c62c9c898cb80ff64db6c1cc822909e24c1e0e885864ba87070880a.
It contains 20,977 ordered events: 1,011 conversation messages, 9,570 tool
calls, 9,567 tool outputs, and 829 metadata-only internal-agent markers. The
15,175,531-byte JSONL has SHA-256
96fd78b767d1c16c6b424e381a657f3582981211deeace97fe8b78be9af51f79;
its deterministic 2,746,333-byte gzip has SHA-256
d896ccaa5261a86f9339de6098fd27ecb739569128d572d0a6ca78549380def3
and decompresses byte-for-byte to that JSONL. Thirty-seven user turns are
neutral source-hash-anchored summaries. An independent parent rerun verified
the chronology, tool pairing, deterministic derivation, 12-row hash ledger,
gzip identity, empty unresolved queue, and a zero-finding parsed-field privacy
scan before authorizing inclusion. The annex records seven legacy orphan tool
outputs and ten unpaired calls at legacy/frozen boundaries; raw tool arguments
and output bodies remain deliberately omitted.

## Curated Zenodo-package preview

The DOI builder selects a public allowlist rather than depositing the complete
collaboration tree. Its latest prepare-only round trip selected 286 canonical
files and excluded 188 archival/private/build-history files. The resulting
source ZIP contains 294 entries and 39,321,011 uncompressed payload bytes. It
is 20,772,198 bytes with SHA-256
e2d40875521e0a723e86dac2019641609fad876efd5e09e7931be9a1d2b82e12.
Extraction reproduced the staging inventory exactly, and an independent second
pack was byte-identical. The builder scanned 269 UTF-8 text files and 23 PDFs
with zero privacy findings, rechecked the five publication-PDF page counts and
hashes, and independently admitted both provenance annexes. All 20 rows
in the outer upload checksum ledger verify. The preview remains marked
NOT_RELEASE_READY only because the public creator and record-level license
have not yet been selected.

## Overleaf state

The canonical collaboration project is
https://www.overleaf.com/project/6a8ca9bd0c2a1270c91e5ce1, with public read
view https://www.overleaf.com/read/rtmyqxyrzprn#fa24eb. Sharing controls are
owner-managed and must not be opened or changed by this workflow. The previous
remote readback is preserved as a historical checkpoint; the current 283-page
workbench, 294-page monograph support, four specialist drafts, metadata, and
this receipt still require exact-tree synchronization and a new remote
readback. No claim of final remote identity is made before that check.
