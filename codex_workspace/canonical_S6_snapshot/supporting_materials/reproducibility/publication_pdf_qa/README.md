# Publication PDF structural audits

The five `*.audit.json` files were regenerated on 4 September 2026 by
`../verify_publication_pdf.py` from the PDFs in
`../../reference_pdfs/`.  Each fail-closed audit records the PDF byte count and
SHA-256 digest and checks:

- strict PDF parsing and successful text extraction on every page;
- unrotated US-letter page geometry and readable content streams;
- resolution of every internal named link destination;
- absence of encryption; and
- embedding of every used font program.

All five current reports have `"passed": true` and empty error arrays.  They
cover the 129-page annotated edition, 108-page clean reconstruction, 21-page
overview, 449-page workbench, and 471-page publication monograph at the exact
installed byte identities recorded in `../../reference_pdfs/README.md`.  TeX
diagnostics, source-equivalence checks, and visual inspection are recorded
separately in `../../project_documentation/QA_RECEIPT.md`.
