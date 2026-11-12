# QA ledger — packet 02, PDF pages 12–22

Authority inspected directly: `authority/s6_pages_012_022.pdf` and the eleven supplied 200-dpi page images. Extracted text, coordinate JSON, and word boxes were used only as secondary navigation and comparison aids.

| PDF page | page inventory | prose/headings | displays, tags, matrices, symbols | citations, notes, footnotes | figures/layout | unresolved |
|---:|---|---|---|---|---|---|
| 012 | Proposition 2.11 proof material: parts (ii) and (iii), stabiliser and cusp-coordinate arguments; opening of Remark 2.12; two displayed formulas. | checked | checked symbol by symbol | `[Bea83]`, chapter references, and internal references checked; no footnotes | checked; no figures or tables | none |
| 013 | Completion of Remark 2.12; Remark 2.13; Definition 2.14 with equation `(2.4)`; Definition 2.15; Section 3 title and opening paragraph. | checked | checked, including equation tag `(2.4)`, representation formulas, inverses, transpose, hats, and section-opening notation | all cross-references checked; no footnotes | checked; no figures or tables | none |
| 014 | Completion of the Section 3 opening paragraph; Definition 3.1 with conditions `(τ1)`–`(β3)`; Remark 3.2; Definition 3.3; Theorem 3.4(i). | checked | checked, including four 2-by-2 matrices, period matrix notation, quotients, and the definition of `D` | all theorem and section references checked; no footnotes | checked; no figures or tables | none |
| 015 | Theorem 3.4(ii)–(v); subsection 3.1; modular-function and modular-form facts; Lemma 3.5 statement and initial setup. | checked | checked, including the matrices `S`, `S_1`, modular expansions, regions, and set inclusions | `[Ser73]` and all internal references checked; no footnotes | checked; no figures or tables | none |
| 016 | Completion of Lemma 3.5 and its proof; Proposition 3.6 statement and proof through existence, equivariance, local orders, and normalisation. | checked | checked, including matrix products, traces, lifts, local parameters, and roots of unity | all cross-references checked; no footnotes | checked; no figures or tables | none |
| 017 | Completion of Proposition 3.6; Corollary 3.7 and proof; subsection 3.2 opening; Lemma 3.8 statement. | checked | checked, including the nilpotent matrix parametrisation, cusp expansion `q=t_c/1728(1+O(t_c))`, covering maps, and cocycle notation | all references checked; no footnotes | checked; no figures or tables | none |
| 018 | Lemma 3.8 proof; Definition 3.9; Lemma 3.10 and proof; Proposition 3.11 statement and opening proof; two orbit tables. | checked | checked, including products over cyclic orbits, modular-form expression for `F`, sheaf notation, orders of vanishing, and both tables reconstructed as LaTeX arrays | all references checked; no footnotes | checked; two source tables reconstructed semantically; no image assets | none |
| 019 | Completion of Proposition 3.11 proof; Remark 3.12; subsection 3.3; Proposition 3.13 statement and opening proof with the `φ_1` formulas. | checked | checked, including local/global torsor calculations, fixed-point values, Weierstrass-model formula, sums, substitutions, and rational identities | `[Kod64]`, `[BHPV, V10]`, and all cross-references checked; no footnotes | checked; no figures or tables | none |
| 020 | Completion of Proposition 3.13 proof; subsection 3.4; Lemma 3.14 and proof; Proposition 3.15 statement. | checked | checked, including the `φ_2` orbit sum, torsor averaging formula, real determinant identity, complex determinant factors, and invariance calculation | all references checked; no footnotes | checked; no figures or tables | none |
| 021 | Proposition 3.15 proof; subsection 3.5; Proposition 3.16 and proof. | checked | checked, including `σ_1`, `σ_2`, the two `R_g` matrices, six transformation formulas, transpose convention, and cocycle identity | all references checked; no footnotes | checked; no figures or tables | none |
| 022 | Subsection 3.6; Convention 3.17 and meridian orientations; Remark 3.18; Proposition 3.19 and proof. | checked | checked, including inverse monodromy, forward-transport convention, matrix product order, quotient action, and the final automorphism formula | all references checked; no footnotes | checked; no figures or tables | none |

## Compilation

- Command: `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=deliverable deliverable/packet_02_standalone.tex`
- Exit status: `0`
- Output: 11-page letter-size PDF, with printed page numbers 12–22.
- Fatal errors: none.
- Nonfatal warnings: none from LaTeX or packages; no overfull or underfull boxes reported.
- Missing glyphs/assets: none.
- External assets used: none; `deliverable/assets/README.md` records this explicitly.

## Visual and textual comparison

- Render DPI: 200.
- Final pages compared side by side: 012–022, all eleven pages.
- Reading order, paragraph boundaries, theorem/definition/remark numbering, display count, equation tag `(2.4)`, matrices, the two page-018 tables, citations, proof-end squares, and page numbers were checked.
- A separate symbol pass covered every display, matrix, inverse, transpose, exponent, summation bound, root, arrow, and indexed object.
- No clipping, missing page material, raster substitution, or misplaced source-page boundary was found.
- Material typographic deviation: the check PDF uses the supplied shared Latin Modern preamble rather than the source PDF's Palatino/Pazo font set. Consequently some line breaks and vertical page fill differ from the authority. The source-page content boundaries, semantic paragraph/display structure, and all substantive printed content are preserved.
- A secondary normalized text comparison was used only as a backstop; its residual differences were attributable to PDF math extraction and reading-order artifacts, not identified transcription omissions.

## Normalisations and source anomalies

Standard LaTeX commands replace PDF glyph encodings for ligatures, minus signs, arrows, section signs, accents, quotes, and mathematical alphabets. These are typographic normalisations only; no mathematical or editorial claim was changed.

No probable source error requiring an editorial note was identified on pages 12–22. No silent correction was made.

## Boundary reconciliation

- Page 012 begins in the proof of Proposition 2.11, immediately after the material assigned to page 011. Only the marks physically printed on page 012 were transcribed.
- Page 012 ends inside Remark 2.12 at the words “the local”; page 013 resumes with “parameter of the cusp”. Both physical-page fragments are retained exactly once.
- Page 013 ends inside the opening paragraph of Section 3 after `ρ:=e^{iπ/3},`; page 014 resumes with the definition of `ζ_j`.
- Page 022 ends with the proof-end square for Proposition 3.19. The next-page Remark 3.20 and subsection 3.7 material supplied as boundary context were not imported.

## Final declaration

`COMPLETE`
