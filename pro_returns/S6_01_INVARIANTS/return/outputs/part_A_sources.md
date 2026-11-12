# Part A source and calculation record

## Sources actually read

- Entire attached development prompt.
- Entire `workbench/hodge_frolicher.tex`, with particular attention to lines218-1188.
- Original AC26 transcription: Definition3.1 and Theorem3.4; Lemma3.10; Section9.3 Proposition9.13 and its full proof; canonical line statements; Remarks1.3 and9.21. Original PDF pages5 and81 rendered and visually inspected: the claimed degree-one relative torsion along W appears in the authority itself.
- Engel attached PDF, Section2 and its Weierstrass equation, Mordell-Weil and fibre description; Lemma2.1 and its height computation; relevant topology/linearization passages.
- Attached Duke-Imamoglu PDF: introduction, Theorem1, equations(4)-(6), and Section2.
- Eichler-Zagier original PDF opened from the author's official MPIM page; theorem on printed page399 and both proofs read via extracted text. Formula coefficient, denominator and path checked against Duke-Imamoglu equation(6).
- Course `cusp-and-compact-threefold.md`, Sections9-11 and13: read as untrusted comparison material. The rational-section cocycle and height argument were independently checked and written with explicit reductions.
- Reader B notes opening source index and Hodge references; survey findings F1,F5,F19.

## Searches

Web searches on12 November2026 included `Shioda 1990 On Mordell Weil lattices Theorem8.6 pdf`, `Eichler Zagier On the zeros of the Weierstrass function 1982 pdf`, exact Shioda title with8.6, and exact Duke-Imamoglu title/year/DOI. Original Shioda PDF fetch returned HTTP429; indexed author-upload text exposed the height formula. It is not used as an unexamined authority in the proof: the needed height calculation is derived directly from the E6/A1 intersection matrices. No priority claim is made. Root literature searches cover newer S6 papers.

## Computations actually run

`code/a_calculations.py` and its complete `outputs/a_calculations.txt` include exact covariance residuals for g1,g2,g2_squared, invariant exponents for(3,2),(4,1),(9,6),(20,5), exact triple-chart torsion syzygies, exact E6 Cartan inverse, and elliptic addition formulas for2P* and3P* with zero curve-equation residuals.

At100 decimal working digits it evaluates the order-four scalar by an E4 divisor-sum Fourier series and an independent Abel-period quadrature. Gamma and Duke-Imamoglu hypergeometric evaluations agree as additional checks. A separate Newton solver evaluates two nearby Weierstrass zeros using the wp Fourier expansion, for s=10^-5,10^-10,10^-15; the symmetric derivative agrees to31 decimal places at the last step. The order-three K coefficient is computed from independent E6 Fourier and Jacobi-theta evaluations. These are numerical corroborations, not interval certificates; analytic proofs establish nonzero values and exact orders.

An initial Sympy structural equality assertion for the already equal factorizations of x(3P*) failed because multiplication trees differed. Replacing it with exact factor(left-right)==0 passed; no mathematical formula was changed. The final rerun output is attached in full.

## Decisions and corrections

The workbench's cotangent direct images and h12=1 are confirmed by a different global computation: calculate O(2S1+3S2), apply relative duality to detE, and use the globally nonzero logarithmic vertical vector. A second independent modular identity determines the full period determinant. The scalar is normalized to a named fourth-root coordinate; the prompt's equation t-1=s^4 alone leaves four possible phases, while the workbench's ds/dz=1 normalization is different.

AC26 Remark9.21, transcription line4330, is false about Omega1 relative torsion at W. The corrected local modules prove torsion exactly at the two multiple fibres. Degree2 has cusp torsion, so Remark1.3's plural wording needs this distinction. The workbench's lines984-1006 are correct in degree1.

All four A items have proofs in the fragment. Explicit generators are supplied in the requested Leray associated-graded sense; lifting the second H11 class has exactly the stated one-dimensional ambiguity. No elementary atlas coefficient formula for a distinguished global Q is claimed.
