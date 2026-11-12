# Audit Evidence Directory

This directory contains the complete page-status ledger and the compact
non-raster audit records retained in the consolidated project.

- `PAGE_AUDIT.csv` has one disposition row for every physical page 1-108.
- The upstream `contact_sheets/`,
  `detailed_pairs/low_extraction/`, and
  `detailed_pairs/boundaries/` raster directories were reviewed but are
  intentionally omitted from this compact tree.  Their omission and retained
  replacements are recorded in
  `../../project_documentation/EXCLUSIONS.md`.
- text, prose, structural, renderer-parity, preflight, font, provenance, checksum, and build reports are supplied in CSV, JSON, or plain text.
- `upstream_receipts/` contains every packet's completion JSON and QA ledger.

The individual 200-dpi page renders, contact sheets, and full-scale selected
pairs are not duplicated here.  The retained audit ledgers and reports record
their results, and the final and authority PDFs can be rerendered at any
resolution.
