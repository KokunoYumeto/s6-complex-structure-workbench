# Consolidation and Correction Ledger

No source prose or mathematical expression was silently corrected during consolidation.

## C-001 — Unified source-matched typography

The packet-local preambles were replaced by one canonical 10-point letter-paper preamble using URW Palladio/Pazo (`mathpazo`), matching the principal font family embedded in every authority slice. Packet-local macros remain isolated in groups so that identical command names do not collide.

**Effect:** typography and namespace consistency only; no source content changed.

## C-002 — Page 2 layout refinement

Packet 1 page 2 originally used 0.50-inch side margins and `\small`. The consolidated source uses 0.55-inch side margins and `\fontsize{10.5pt}{12.2pt}\selectfont` on that page. This brings the dense setup sheet materially closer to the authority page's scale while retaining all content on physical page 2.

**Effect:** two layout-only substitutions; text and mathematics unchanged.

## C-003 — Packet 9 assembly width

Pages 89–98 retain the packet's audited 0.55-inch geometry. Using the global 0.69-inch geometry caused the final material of page 98 to overflow into a 109th page. Restoring the packet width yields the intended 108-page document and preserves the physical 98/99 continuation.

**Effect:** assembly pagination only; source content unchanged.

## C-004 — RSFS optical-size declaration

A continuous `rsfs` optical-size declaration was added to avoid TeX font-substitution warnings in scaled script/display contexts.

**Effect:** removes a build warning; mathematical glyph identity is preserved.

## C-005 — Deterministic PDF metadata

The main preamble sets a fixed trailer identifier and suppresses volatile pdfTeX metadata. The build scripts also set `SOURCE_DATE_EPOCH`, `FORCE_SOURCE_DATE`, and `TZ`.

**Effect:** repeated clean builds are byte-identical in the audited environment; page content is unchanged.

## C-006 — Monolithic input-boundary token

The monolithic generator preserves the ordinary space token contributed by the endline after packet 7's modular `\input`. This makes the modular and monolithic outputs byte-identical, including the terminal proof square on page 77.

**Effect:** exact source-form equivalence; no printed-content change relative to the modular canonical build.
