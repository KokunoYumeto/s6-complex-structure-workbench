# Independent A proof record: visual inspection

The final `build/A_special_qa.pdf` contains five pages. It was recompiled after changing the endpoint symbol regularity from a claimed C1 extension to the proved uniformly bounded Lipschitz extension. The final compilation has no overfull boxes.

`code/A_special_render.py` rendered the final PDF with Poppler at 110 dpi into `records/A_special_render/page-1.png` through `page-5.png`. All five final page images were opened and visually inspected on 15 November 2026, after the final compilation completed.

- Page 1: hypergeometric Fourier derivation, gamma normalizations, and boxed kernel identity are legible and within the margins.
- Page 2: branch audit, scalar check, explicit Volterra bounds, source URLs, and the BV lemma statement are legible, with no clipped equations or overlapping text.
- Page 3: exact phase Jacobian, pushed-forward density, derivative estimates, and proof ending are clearly set. Equation numbers and references are present.
- Page 4: geometric translate summation, dyadic convergence, and the finite-height/intersecting-axis treatment have consistent spacing and no overflow.
- Page 5: the outgoing-symbol regularity and oscillatory consequence are legible, including the revised Lipschitz wording. The remaining lower white space is a normal final-page ending.

Visual result: pass. No clipping, collisions, missing glyphs, malformed formulas, or page-number defects were observed. The mathematical audits are preserved separately and are not inferred from this rendering check.
