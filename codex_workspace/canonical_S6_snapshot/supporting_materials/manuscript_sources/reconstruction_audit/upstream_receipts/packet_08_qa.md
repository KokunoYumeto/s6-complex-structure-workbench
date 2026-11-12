# QA ledger — packet 08, source PDF pages 78–88

The authoritative PDF slice and its 200-dpi page images were inspected directly. Extracted text was used only as a navigation and prose-completeness aid; mathematical notation, accents, superscripts, subscripts, equation tags, and page boundaries were checked against the page images.

| PDF page | prose/headings complete | displays & tags complete | matrices/symbols checked | notes/citations/footnotes checked | figures/layout checked | unresolved items |
|---:|---|---|---|---|---|---|
| 078 | complete | complete; (9.12) and all unnumbered displays | complete | complete | no figures; source-page boundary checked | none |
| 079 | complete | complete; toric substitutions and Lemma 9.17 formulas | complete | complete | no figures; source-page boundary checked | none |
| 080 | complete | complete; cubic differential calculations and Proposition 9.20 displays | complete | complete | no figures; source-page boundary checked | none |
| 081 | complete | complete; Hodge-number displays and vertical-field display | complete | complete | no figures; source-page boundary checked | none |
| 082 | complete | complete; inline toric formulas, \(\operatorname{Aut}^0\) display, and quotient-pair display | complete | complete | no figures; dense page and boundary checked | none |
| 083 | complete | complete; fixed-locus display | complete | complete | no figures; source-page boundary checked | none |
| 084 | complete | complete; period matrix and numbered lists | complete | complete | no figures; list continuation into p. 085 checked | none |
| 085 | complete | complete; quoted theorem/corollary formulas | complete | complete; footnote 3 checked | no figures; source-page boundary checked | none |
| 086 | complete | complete; quoted (1), quoted (11), and (10.1) | complete | complete | no figures; source-page boundary checked | none |
| 087 | complete | complete; (10.2)–(10.4) and local-model formula | complete | complete | no figures; proof continuation into p. 088 checked | none |
| 088 | complete | complete; (10.5), duality display, and cohomology sequence | complete | complete; footnote 4 checked | no figures; terminal packet boundary checked | none |

## Page inventories and audit findings

**Page 078.** Continuation of the argument preceding Step 2; coordinate form (9.12); heading “Step 2: matching the charts, and regularity at \(\Sigma\)”; Lemma 9.16 statement, items (i)–(ii), cusp-coordinate definitions, three vanishing-order lines, and proof through the introduction of a maximal cone and its coordinate chart. The page ends after “with coordinates”.

**Page 079.** Continuation with the toric coordinates \(w_k\); formulas for \(t,x_i,dt/t,dx_i/x_i\); the three substituted forms for \(p=1,2,3\); completion of Lemma 9.16; heading “Step 3: descent through the elliptic points, and two vanishing lemmas”; Lemma 9.17 with (D0)–(D2) and proof; Lemma 9.18 with proof; Lemma 9.19 statement. No numbered equation tags occur on this page.

**Page 080.** Proof of Lemma 9.19, including \(\kappa=\psi\otimes\psi\otimes d\tau\), the cusp calculation, and the line-bundle vanishing; heading “Step 4: the vanishing theorem”; Proposition 9.20 and its proof for \(p=1,2,3\); concluding paragraph concerning Theorem 9.1(vi), Serre duality, \(K_X\), and the variant \(X'\).

**Page 081.** Section 9.6; Remark 9.21 with all Hodge-number identities, Euler-characteristic equations, expected values, and discussion of direct images; Corollary 9.22 and proof; section 9.7; Proposition 9.23 statement and proof through Construction, Verticality, and the first sentence of Uniqueness. The page ends after “with \(\mathcal O\xi\subset\mathcal V\) a subbundle.”

**Page 082.** Continuation and completion of Proposition 9.23: local descriptions of \(\mathcal V\), toric-chart calculation, quotient line bundle \(\mathcal Q\), computation of \(\operatorname{Aut}^0(X)\), and proof-ending square; Proposition 9.24 statement; beginning of its proof, including the three quotient pairs. The page ends after “On \(\mathfrak h_z^\circ\times\mathbb C^2\) only the \(\mathbb C\)-flow lifts,”.

**Page 083.** Continuation and completion of Proposition 9.24: descent of fixed points, fixed locus in \(W\), normal weights, and Euler characteristic; Remarks 9.25 and 9.26; section 9.8 and Remark 9.27. The finite-subgroup condition involving \(\frac1n(e_2,0)\), determinant tests, and all hats/bars were checked visually.

**Page 084.** Section 10 title and introductory paragraph; source-fact list (X1)–(X4), including the \(2\times4\) period matrix; discussion locating two failures in [CDP20, CDP98]; numbered items (i) and the beginning of (ii). Item (ii) remains open across the physical page break, as in the source.

**Page 085.** Completion of item (ii); scope-of-discussion paragraphs; section 10.1; definition of torsion and the torsion-free quotient; verbatim quotations of [CDP20, Theorem 2.2] and [CDP20, Corollary 2.3]; explanatory paragraph ending with “The remaining”; footnote 3 reproduced at the page foot.

**Page 086.** Completion of “The remaining case”; verbatim quotation of [CDP20, Proposition 2.4], including displayed hypothesis (1); quoted reduction to displayed statement (11); discussion of the failed implication; section 10.2; Definition 10.1; local normal-crossings computation and equation (10.1).

**Page 087.** Lemma 10.2, exact sequence (10.2), maps \(\alpha,\beta\), and proof; global-sections formula (10.3); conormal sequence (10.4); Lemma 10.3 parts (a)–(c); proof through the component argument, ending with “as \(\sigma\not\equiv0\)”. The closure bar in \(\widetilde S':=\overline{\eta^{-1}(S'\setminus D)}\) was checked against the page image.

**Page 088.** Completion of Lemma 10.3 and proof-ending square; Remark 10.4; section 10.3; Theorem 10.5 parts (a)–(c); proof Steps 1–4 through the packet boundary; equation (10.5), duality formula, base-change formula, cohomology sequence, and footnote 4. The page ends mid-sentence immediately after \(f^*(c)\), with no material imported from page 89.

## Compilation

- Command: `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=deliverable deliverable/packet_08_standalone.tex`
- Exit status: `0`
- Output: 11 letter-size pages, numbered 78–88
- Fatal errors: none
- Nonfatal warnings in final `build.log`: none
- Missing glyphs/assets: none; all used fonts are embedded; no external assets are used

## Visual comparison

- Render DPI: 200
- Pages compared: 78–88 inclusive, every authoritative PNG against the corresponding compiled page
- Material layout deviations: none. The reconstruction preserves one source page per output page, reading order, paragraph/list structure, display placement, theorem numbering, footnote placement, and page-boundary continuations. Minor line-wrap and interword-spacing differences are ordinary consequences of an independent LaTeX reconstruction and do not alter structure or content.
- Mathematical-symbol discrepancies: none identified after a separate pass over every display, matrix, decorated symbol, pullback/pushforward, inverse, exponent, and equation tag
- Textual cross-check: normalized alphabetic/numeric token comparison between the authority PDF text layer and compiled PDF showed complete prose coverage; remaining extraction differences were limited to decorated mathematical glyph segmentation (for example tildes and hats)

## Source anomalies preserved rather than silently corrected

No probable substantive source error was identified in pages 78–88. Printed spelling variation, punctuation, quotation ellipses, citation forms, and the abrupt page-088 sentence boundary were preserved. PDF text-layer artifacts were resolved only by direct visual inspection; no editorial correction or explanatory note was inserted into the transcription.

## Boundary reconciliation notes

- Page 078 begins within the ongoing argument from the preceding packet, at “By Lemma 9.14(i), …”; only marks printed on page 078 were transcribed.
- The physical-page continuations 082→083, 084→085, 085→086, and 087→088 retain their grammatical, proof, and list structure without duplicated or inferred text.
- Page 088 ends mid-sentence after “(a finitely generated group, \(f^*(c)\)”. No text from source page 89 was imported.

## Final declaration

`COMPLETE`
