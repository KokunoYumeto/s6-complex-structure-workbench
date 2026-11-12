# QA ledger - packet 05, PDF pages 45-55

Authority checked directly: `authority/s6_pages_045_055.pdf` and the corresponding 200-dpi page PNGs. Extracted text was used only as a navigation and completeness aid. This ledger records the physical-page inventory and final verification state.

| PDF page | page inventory | prose/headings complete | displays, tags, matrices, and symbols checked | citations, cross-references, and footnotes checked | figures/layout checked | unresolved items |
|---:|---|---|---|---|---|---|
| 045 | Continuation of the proof preceding this packet: parts (ii)-(iv); local manifold models; toric moment-hexagon argument; vertex, edge, and 2-cell construction of `\vartheta`; one principal equivariant-propagation display; proof closes. | checked | checked | `[Bro62]`, `[Ful93, §4.1]`, Lemmas 4.2-4.3, Theorem 4.5 checked; no footnotes | checked; no figures or tables | none |
| 046 | Lemma 7.8 statement and proof; definition of `Q^+`, `H`, and the deformation retraction; Lemma 7.9 statement; list (P1)-(P4); definition of `R_s`; proof begins and ends in a displayed equivariance computation continuing on page 47. | checked | checked | `[Hat02, Thm. 4.5]`, `[Hat02, Prop. 0.19, Cor. 0.20]`, `[Bro62]`, internal references checked; no footnotes | checked; no figures or tables | none |
| 047 | Completion of Lemma 7.9; Lemma 7.10 statement with parts (i)-(iii); initial-data and restriction displays; proof through the cell description and quotient construction, ending at the fixed-level parameter `\theta_0`. | checked | checked | Lemmas 7.5-7.7 and equations (7.1)-(7.3) checked; no footnotes | checked; no figures or tables | none |
| 048 | Continuation of Lemma 7.10 proof; `\Gamma^0` action and product splitting; coordinate facts (F1)-(F2); interpolation lemma; homotopy construction; numbered equations (7.4) and (7.5); tent function introduced at the page boundary. | checked | checked | Lemmas 7.5, 7.7, 7.9 and equations (7.2)-(7.4) checked; no footnotes | checked; no figures or tables | none |
| 049 | Tent function and band `U_\delta`; definition of `w`; piecewise definition (7.6) of `K_u`; properties (K1)-(K5); piecewise definition of `P'_s`; equation (7.7); application of Lemma 7.9 and definition of `r`. | checked | checked | Cross-references (F1), (F2), (P1)-(P4), (K1)-(K5), Lemma 7.9 checked; no footnotes | checked; no figures or tables | none |
| 050 | Equality on `Y_{t_0}` and equation (7.8); equality on `F`; other-level homotopy; completion of Lemma 7.10; proof of Proposition 7.2; section 7.3 heading; Proposition 7.11 statement and proof begins. | checked | checked | Lemmas 7.3, 7.5-7.10 and equations (7.1), (7.7), (7.8) checked; no footnotes | checked; no figures or tables | none |
| 051 | Continuation and completion of Proposition 7.11: regular-neighbourhood/excision argument, relative and absolute homology displays, fundamental group, Euler characteristic; Proposition 7.12 statement begins with invariant-lattice displays and specialisation formulas. | checked | checked | Propositions 7.2, 7.11; Lemmas 7.3-7.4, 7.9; Corollary 4.8 checked; no footnotes | checked; no figures or tables | none |
| 052 | Completion of Proposition 7.12 statement; factor markings and orientations; proof in degrees 1 and 2; numbered formula (7.9); cellular description of `T_B`, homology display, coefficient/intersection display; proof continues on page 53. | checked | checked | Proposition 7.2, Proposition 7.11, Lemmas 7.5 and 7.10, §2 checked; no footnotes | checked; no figures or tables | none |
| 053 | Completion of Proposition 7.12, monodromy/kernel argument, and nearby-cycles note; section 7.4 heading; admissibility data; Lemma 7.13 statement and proof; Proposition 7.14 statement, index array, and cokernel assertions. | checked | checked | Appendix B/Theorem B.1, §2, §5, Lemma 7.4, `[BHPV, Ser]` checked; no footnotes | checked; no figures or tables | none |
| 054 | Continuation and proof of Proposition 7.14; two pullback-lattice displays; two Gram matrices and two degree-3 pairing matrices; Remark 7.15; section 7.5 heading; fundamental-group presentation, covering generator, and filling relation; sentence continues on page 55. | checked | checked | Lemmas 6.5 and 7.13, Proposition 5.6, Proposition 7.26, §§2, 3, 5, 6 checked; no footnotes | checked; no figures or tables | none |
| 055 | Continuation of the sign discussion; relation for `\hat\rho_j`; toric meridian at `p_0`; numbered equation (7.10); Lemma 7.16 statement, filling relation, order formula, and proof through the two mixed assignments; page ends mid-proof at “again cyclically reduced”. | checked | checked | Lemma 7.4, Lemma 7.16, Propositions 2.11 and 4.7, Theorems 7.17 and 7.22, `[Bea83, Ch. 10]`, §§3-7.5 checked; no footnotes | checked; no figures or tables | none |

## Compilation

- Command: `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=deliverable deliverable/packet_05_standalone.tex`
- Exit status: `0`
- Compiled page count: `11`
- Fatal errors: none
- Nonfatal warnings: the first LaTeX pass requested a rerun because the hyperref output file changed; `latexmk` performed the required second pass. No unresolved warning remains.
- Missing glyphs/assets: none
- PDF preflight: opens successfully, unencrypted, 11 pages, not image-only, no preflight warnings.

## Visual and textual comparison

- Render DPI: `200`
- Pages compared: source PDF pages `45-55` against compiled pages `1-11`, one-to-one.
- Checks performed: page boundaries, reading order, paragraph continuity, theorem/lemma/proposition labels, section headings, list labels, all displays and printed tags `(7.4)`-`(7.10)`, matrices, hats/bars/duals, blackboard-torus notation, signs, citations, and terminal proof marks.
- Material layout deviations: exact source line wrapping and vertical fill were not treated as authority. The reconstruction uses the supplied practical standalone framework with Palatino-compatible text and independent LaTeX reflow; all physical source-page boundaries remain explicit and the output remains exactly 11 pages.
- Mathematical-symbol discrepancies: none identified after the symbol-level pass.
- Clipping, overlap, black boxes, or broken glyphs: none observed.
- Textual completeness aid: normalized prose-word sequence comparison showed no substantive omitted passage; remaining differences were mathematical tokenization, ligature, and line-break artifacts.

## Source anomalies and normalizations

- No probable mathematical source error was identified in this slice.
- PDF ligatures, discretionary hyphenation, and extraction-induced token joins were normalized to ordinary LaTeX source without changing wording or mathematical content.
- Blackboard `\mathbb{T}_B` was retained distinctly from the factor torus `T_B`.
- No silent editorial correction was made.

## Boundary reconciliation notes

- Page 45 begins with part `(ii)` of a proof whose preceding text is on page 44. No page-44 text was imported.
- Page 46 ends inside the equivariance computation in the proof of Lemma 7.9; page 47 begins with “using (P4).” Both physical-page fragments are preserved in their respective page anchors.
- Pages 47-50, 50-51, 51-52, 52-53, and 54-55 contain printed continuations and are preserved without duplication.
- Page 55 ends mid-proof after the words “again cyclically reduced”. No page-56 continuation was imported.

## Final declaration

`COMPLETE`
