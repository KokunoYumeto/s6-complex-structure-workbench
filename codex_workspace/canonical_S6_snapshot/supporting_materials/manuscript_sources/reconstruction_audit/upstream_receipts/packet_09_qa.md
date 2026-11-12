# QA ledger - packet 09, PDF pages 89-98

Authority inspected directly from `authority/s6_pages_089_098.pdf` and the supplied 200-dpi page PNGs. Extracted text was used only as a navigation and comparison aid.

| PDF page | prose/headings complete | displays & tags complete | matrices/symbols checked | notes/citations/footnotes checked | figures/layout checked | unresolved items |
|---:|---|---|---|---|---|---|
| 089 | yes | yes | yes | yes | yes; no figures | none |
| 090 | yes | yes | yes | yes | yes; no figures | none |
| 091 | yes | yes | yes | yes | yes; no figures | none |
| 092 | yes | yes | yes | yes, including footnote 5 | yes; no figures | none |
| 093 | yes | yes, including (10.6)-(10.7) | yes | yes | yes; no figures | none |
| 094 | yes | yes | yes | yes | yes; no figures | none |
| 095 | yes | yes, including (A.1)-(A.5) | yes, including every matrix entry | yes | yes; no figures | none |
| 096 | yes | yes, including (A.6) | yes, including Lemma A.1 items 1-7 and wedge-power notation | yes | yes; no figures | none |
| 097 | yes | yes | yes, including lattice and fan data | yes | yes; no figures | none |
| 098 | yes | yes | yes, including the Mayer-Vietoris map and terminal congruence symbol | yes | yes; no figures | none |

## Page inventory

- **089:** continuation of Theorem 10.5, Step 4; Step 5; Corollary 10.6 and proof; opening of Section 10.4; the restriction/injection display and the countable-set display.
- **090:** continuation of the fibrewise argument with the three vanishing/non-vanishing statements; remainder of Section 10.4; opening of Section 10.5; quoted setup from Lemma 4.2/[CDP98]; Lemma 10.7 and its proof.
- **091:** monodromy/co-invariant rank discussion; the exact cohomology sequence for the pair; the projective example; discussion of the final step in [CDP98, Theorem 3.1]; quoted Corollary 5.2 and its hypotheses.
- **092:** continuation of the hypotheses and failure analysis; the Leray differential and quoted Proposition 5.5; Proposition 10.8 and the beginning of its proof; the normalisations paragraph; footnote 5.
- **093:** continuation of Proposition 10.8; definition of `\Lambda_q`; the line `\iota_q(\mathbb C)` and flat integral class; period-matrix argument; equations (10.6) and (10.7).
- **094:** conclusion of the period argument; treatment of the remaining fibres and reductions; Remark 10.9; two stated conclusions; Section 10.6; quoted Corollary 1.3.
- **095:** continuation of the quoted parenthetical; cohomology and torsion discussion; Appendix A and Section A.1; matrices and formulas (A.1)-(A.5).
- **096:** continuation of the matrix notation; formula (A.6); Lemma A.1, items 1-7; beginning of its proof through the rank-5 lattice continuation.
- **097:** continuation and end of the proof of Lemma A.1; Section A.2; Lemma A.2, items 1-6; beginning of its proof through the printed citation list.
- **098:** continuation and end of the proof of Lemma A.2; Section A.3; Lemma A.3 and proof; Mayer-Vietoris sequence, map, rank/kernel analysis, and the deliberately incomplete final congruence continuing on page 99.

## Compilation

- Command: `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=deliverable deliverable/packet_09_standalone.tex`
- Exit status: 0
- Output: 10 pages, numbered 89-98
- Fatal errors: none
- Nonfatal warnings: none
- Overfull/underfull boxes: none
- Missing glyphs/assets: none
- Authority hashes: the completion receipt retains the original 108-page authority SHA-256 from `SCOPE.json`; the supplied ten-page slice was independently verified as `33cd80026e4805c2ff09da2e3e8945746bbb36049b1f2cef2207901ebc18ebbb`.

## Visual and textual comparison

- Render DPI: 200
- Pages compared: 89-98, all ten pages, source and reconstruction side by side
- Reading order, paragraph inventory, display inventory, printed numbering, citations, footnote, matrices, and boundary continuations: checked
- Material layout deviations: none affecting content; line wrapping and vertical spacing reflow under the supplied practical standalone preamble. A 0.55-inch standalone margin keeps one reconstructed source page on each check-PDF page.
- Mathematical-symbol discrepancies: none unresolved
- Placeholder search: zero occurrences of `TODO`, `TBD`, `???`, `SCAFFOLD NOTICE`, `continued`, or `[omitted]`
- Assets: no figures, crops, or external assets were needed

## Direct visual resolutions of extraction ambiguities

- Page 089: the corollary contains `\tfrac12 c_3(X)`; the fraction was confirmed from the PNG rather than inferred from extracted text.
- Page 091: the exact pair sequence is in cohomological degrees 4 and 5, followed by the printed homological duality identifications; all degrees and arrows were checked visually.
- Page 091: the printed quotient is `\Lambda_{\mathbb Q}/\ker\gamma\cong\mathbb Q`, and the connective word “hence” in the displayed rank computation is retained.
- Page 093: the repeated `12` in `\Lambda_q` and `\iota_q(12)` is the printed integer twelve, not a fraction.
- Page 096: the connective word “and” before the final `\bigwedge^3 V` coinvariant statement is retained.
- Page 098: the physical page ends with a bare `\cong`; it is preserved rather than completed from the next packet.

## Source anomalies preserved rather than silently corrected

No probable source error required an editorial intervention. Printed mathematical claims, punctuation, and the author's own critical discussion of cited arguments were transcribed without correction. No editorial note was inserted into the body.

## Boundary reconciliation notes

- Page 089 begins physically with “having the homotopy type ...”, continuing the sentence on page 88. No text from page 88 was imported.
- Page 098 ends physically with `\cong`. Boundary context confirms that page 99 begins with `\mathbb Z^2, whence ...`; that next-page content was not imported.
- All ten exact source-page START/END comments and literal `\hypertarget{s6-source-page-NNN}{}` anchors occur once, monotonically, for pages 089-098.

## Provenance

Independent LaTeX reconstruction from the supplied PDF authority; not the author's original TeX and not a mathematical certification or editorial edition.

## Final declaration

`COMPLETE`
