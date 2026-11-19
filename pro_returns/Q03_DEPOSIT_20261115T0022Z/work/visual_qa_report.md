### Completed visual inspection of the final PDF

**Reviewer:** GPT-6 Astra (OpenAI), effort ChatGPT Pro mode, 15 November 2026.
The inspected final PDF has **38 pages** and SHA-256
`d8782e70ae9286badbf36c6ac98247698f7747fa00f1c9733d4a76b1d1c6265a`.
Its source hash is recorded in `code/visual_review.json` and the final build record.

All 38 pages were rendered at 85 dpi and inspected in seven numbered contact
sheets. Additional individual-page views by the assembling reviewer covered
pages **1, 3, 4, 5, 6, 7, 14, 20 and 27**, spanning the title/results, every
dependency-table continuation, foundations, walks, the capacity injection and
global child formulas. The cost/verification/reference pages receive the
additional review documented in `work/E_visual_tail.md`. Every page belonging
to a previously overflowing table was visually examined: pages 3–6 and 34–35.

The dependency and verification tables now fit their columns and margins;
no clipping, overlap or missing content was observed. The first-page Theorem A
Uses line is together with its statement, and Theorem B begins page 2. The
Lemma 8.1 heading and its displayed statement are together on page 27. The
remaining proof displays, source URLs, page numbers and reference continuations
were checked in the contact sheets. The final page ends with the completed
bibliography and has its normal remaining white space.

The baseline supplied post built to 32 pages with zero overfull messages. The
first revised 38-page assembly had six messages: four dependency-table
alignments of 4.70132 pt and two verification-header overflows of 1.4092 pt.
Column widths were repaired. Subsequent layout edits shortened the abstract's
repeated attribution wording while preserving its content, adjusted title
spacing, kept numbered headings with following text, and explicitly ended the
first page after Theorem A's Uses line. The delivered 38-page build has **zero
overfull boxes, zero boxes over 2 pt, and zero undefined-reference/citation
warnings**. There is no unresolved visual finding.

`code/render_review.py` reproduces the contact sheets; `code/record_visual_review.py`
serializes these completed observations and requires the exact inspected PDF
hash. Neither script treats rendering alone as a visual inspection. Final
page PNGs, contact sheets and the full build logs are retained in the archive.
