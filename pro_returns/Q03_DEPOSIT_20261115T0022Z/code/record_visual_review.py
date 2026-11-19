#!/usr/bin/env python3
"""Serialize completed manual visual review of one exact PDF.

The recorded observations were made by viewing the PNGs/contact sheets through
the image-viewing tool. Executing this script does not perform visual review.
The hardcoded PDF hash prevents the observations being silently applied to a
different revision.
"""
import hashlib
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
EXPECTED='d8782e70ae9286badbf36c6ac98247698f7747fa00f1c9733d4a76b1d1c6265a'
pdf=ROOT/'work/build_final/Q03_DEPOSIT_post.pdf'
assert hashlib.sha256(pdf.read_bytes()).hexdigest()==EXPECTED
build=json.loads((ROOT/'work/build_final/build_check.json').read_text())
assert build['pages']==38 and build['overfull_count']==0
full_pages=[1,3,4,5,6,7,14,20,27]
result={
  'date':'2026-11-15','reviewer':'GPT-6 Astra (OpenAI), effort ChatGPT Pro mode',
  'pdf_sha256':EXPECTED,'source_sha256':build['source_sha256'],
  'render_resolution_dpi':85,
  'reviewed_contact_pages':list(range(1,39)),
  'contact_sheets_reviewed':[f'work/build_final/contacts/contact-{i:02d}.png' for i in range(1,8)],
  'root_full_page_views':full_pages,
  'previous_overflow_pages_reviewed':[3,4,5,6,34,35],
  'tail_review':'Additional individual-page review is recorded in work/E_visual_tail.md.',
  'observations':[
    'All38 final pages inspected in numbered contact sheets; no clipping, overlapping text or missing page content observed.',
    'The dependency table on pages3–6 stays within the text width, with repeated headers and readable row wrapping.',
    'The cost table on page30 and verification table on pages34–35 stay within their margins.',
    'TheoremA and its Uses line now share page1; TheoremB starts page2.',
    'Lemma8.1 heading, statement, formula and Uses line are together on page27.',
    'Proof displays, page numbers, source URLs and reference continuations remain readable.',
    'Final build has0 overfull boxes,0 boxes over2pt, and no undefined references or citations.'
  ],
  'unresolved_visual_findings':[]
}
(ROOT/'code/visual_review.json').write_text(json.dumps(result,indent=2))
report='''### Completed visual inspection of the final PDF

**Reviewer:** GPT-6 Astra (OpenAI), effort ChatGPT Pro mode, 15 November 2026.
The inspected final PDF has **38 pages** and SHA-256
`'''+EXPECTED+'''`.
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
'''
(ROOT/'work/visual_qa_report.md').write_text(report)
print(json.dumps({'PDF_pages':38,'all_contact_pages_reviewed':True,
                  'root_full_page_views':full_pages,'unresolved_findings':0,
                  'pdf_sha256':EXPECTED},indent=2))
