# Final standalone PDF visual QA - 2026-09-04

## Scope and provenance

Delegated task, verbatim:

> Read-only bounded PDF visual QA. Do not spawn children or contact other tasks. cwd C:\Users\user\Documents\math. Read full PDF skill C:\Users\user\.codex\plugins\cache\openai-primary-runtime\pdf\26.903.11726\skills\pdf\SKILL.md yourself before actions. Existing final standalone16-page PDF and rendered page-1.png to page-16.png in tmp/pdfs/homogeneous_quantum_20260904_v5/s6_homogeneous_quantum_confinement. Inspect each PNG using view_image; do not rerender/build. Check formulas,line breaks,glyphs,margins,page continuity. Write actual reviewed PDF SHA256 and pagewise QA via apply_patch in agent_work/quantum_final_visual_20260904/REPORT.md. No canonical writes. Root will check cumulative changed workbench/overview. Any issue report promptly; otherwise concise pass. Prior QA reports are not authority, verify final images.

The complete PDF skill was read before the review. No earlier QA report was used as authority. This review used `view_image` on every existing PNG, individually presented at full-page scale, in numeric order from 1 through 16. No PDF, TeX, or image was rebuilt, rerendered, or edited. This report is the only authored file.

Reviewed PDF:

`C:\Users\user\Documents\math\tmp\pdfs\homogeneous_quantum_20260904_v5\s6_homogeneous_quantum_confinement\s6_homogeneous_quantum_confinement.pdf`

- PDF size: 497,462 bytes.
- SHA256, computed directly from the reviewed PDF: `703415F196FA90D5A9A20A91E23F2F44C8A2EE5788EEC785E3467009660C21F8`.
- Initial hash measurement: 2026-09-04T18:06:37+02:00.
- Render directory: `C:\Users\user\Documents\math\tmp\pdfs\homogeneous_quantum_20260904_v5\s6_homogeneous_quantum_confinement`.
- Existing rendered pages reviewed: `page-1.png` through `page-16.png`, all 16 pages.

## Result

PASS for the requested visual and layout checks. No clipped formulas or text, overlapping equation numbers, missing/unreadable glyphs, broken display equations, or margin violations were observed. Printed page numbers run continuously from 1 to 16. Section and proof transitions are continuous; the final page ends with the Gauss-law reference and normal whitespace. This is a visual QA result, not an independent proof audit or a verification that the supplied PNGs were generated from the hashed PDF; rerendering was expressly outside this task.

## Pagewise findings

| Page | Material visually checked | Finding |
| --- | --- | --- |
| 1 | Title, author line, date, abstract, Section 1 heading, original density and covariant-derivative displays | PASS. Title and heading fit; signs, indices, derivatives, and gauge/scalar glyphs are readable. The action and definitions remain above the footer. |
| 2 | Section 1.1, configuration space, retained action, Proposition 1.1, equations (1)-(3) | PASS. Multiline action and Hamiltonian displays fit; equation labels are distinct. Gauss-map brackets and trace-free subscripts are intact. |
| 3 | Proposition 1.1 proof, coordinates and measure, mass metric, kinetic operator, Section 1.2 and equations (4)-(6) | PASS. Matrix-diagonal notation, powers, complex derivatives, and square roots render correctly. The lemma statement continues coherently onto page 4. |
| 4 | Lemma 1.2 continuation and proof, Theorem 1.3, form/domain display (7) | PASS. The cubic calculation, fractions, original constants, form notation, and operator domain are legible. No display or proof-ending collision. |
| 5 | Theorem 1.3 proof, Theorem 1.4, Gauss generator and domain, averaging formula (8), physical Hamiltonian | PASS. Long domains and the Haar-average expression fit the text width. Hatted generators, intersections, and restriction notation are readable. |
| 6 | Theorem 1.4 proof, flow identity, commutator display, beginning of explicit three-matrix bound | PASS. Integral limits, Lie brackets, representation glyphs, and proof ending are intact. The paragraph introducing the two retained parameters continues on page 7. |
| 7 | Quadratic form (MQ.1), Lemma 1.5, adjoint spectrum and frequency sum (MQ.2)-(MQ.3), root-basis calculation | PASS. Long eigenvalue row, eigenvalue-coordinate row, radicals, and equality-case formulas stay within the margins. |
| 8 | Lemma 1.6, oscillator identity (MQ.4), Theorem 1.7 and equations (MQ.5)-(MQ.8), start of proof | PASS. Set braces, sums, square-root bounds, integral displays, and equation labels are clear and nonoverlapping. |
| 9 | Directed-pair decomposition (MQ.9), compactness estimates (MQ.10)-(MQ.12), finite-rank approximation proof | PASS. The wide decomposition remains within the margin; labels remain distinct. Integral domains, products, and projection notation are readable. |
| 10 | Compact-resolvent proof conclusion, Proposition 1.8, energy-origin bounds (MQ.13)-(MQ.14), retained gauge-density subsection | PASS. Fractional powers and constants are intact. The bottom density display is separated from the footer; its explanation continues on page 11. |
| 11 | Exact coefficient map (MQ.15), primary literature and scope, Section 1.3, Theorem 1.9 and inequality (9) | PASS. Coefficient identities, citations and wrapped DOI text remain legible. The multiline inequality fits and its concluding theorem sentence continues on page 12. |
| 12 | Theorem 1.9 continuation, coupled compactness proof, tail and derivative bounds | PASS. Original coefficients, retained-metric notation, minimum expressions, powers, and the closing proof square render cleanly. |
| 13 | Theorem 1.10, heat kernel, Brownian bridge, formula (10), kernel proof and primary citation | PASS. Gaussian exponent, determinant factor, Brownian-bridge indices, expectation and integral notation are clear. The wrapped source URL is readable. |
| 14 | Spectral-infimum and uniqueness proof, Corollary 1.11, ordered physical eigenvalues and gap statement | PASS. Averaging expression, gradient inequality, semigroup comparison, and eigenvalue superscripts are intact. Both proof endings are correctly separated. |
| 15 | Proposition 1.12, classical embedding and gauge-orbit limitation, explicit gauge transformations, Fourier-mode example | PASS. Exponential phases, primes, inverse matrices, and the final quartic display are legible. The example continues naturally on page 16. |
| 16 | Fourier averages, product-sector/domain obstruction, projected equation, concluding scope and Gauss-law reference | PASS. Mixed-term coefficient, perpendicular subscripts, distributional notation, and source URL are intact. No truncated ending or extraneous blank page is present. |

## Limitations and handoff

- No mathematical claims have been changed or independently certified by this visual review.
- No canonical files were modified.
- The cumulative workbench and overview were outside this subtask and remain for the root agent's review.
