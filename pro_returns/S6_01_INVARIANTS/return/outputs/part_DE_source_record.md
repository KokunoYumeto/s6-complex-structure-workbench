# Part D/E source record

## Attached sources opened

- `original/AC26_original_manuscript.pdf`: PDF text extraction, especially pp. 70–75 (canonical characters, normalization cohomology, direct images), pp. 81–83 (vertical fields), pp. 88–94 (twisted tangent nonvanishing). Compared against the transcription at the indicated statements. The mathematical proofs in D do not infer a tangent dimension from these status claims.
- `workbench/period_parameter_deformation.tex`: read in full, including PD1–PD18, the Kodaira–Spencer sign and the actual finite/cusp gluing.
- `workbench/analytic_canonical_ring.tex`: read in full; used to inspect the pencil-stability problem, then derived via root bundles and the computed semiuniversal family.
- `workbench/analytic_picard.tex`: inspected the restriction normalization and the L12 convention. The positive sign is established separately in C3.2.
- `course/non-normal-fibres-and-vanishing.md`: sections 6, 9–11 and cusp stalk discussion. The normalization kernel and the r=1 calculation were reproved in D1.3/D4.2.
- `course/tangent-index-with-torsion-line-bundles.md`: index expansion and its rational-class specialization.
- `papers/arXiv_2610.10451_Viaclovsky_combs.pdf`: Theorems 1.1, 2.2, 2.3; Proposition 3.2; Proposition 6.1 and Section 6.3; equation 7.5; Lemmas 8.1–8.2 and Proposition 8.3; Section 9.1–9.3; all questions in Section 10. PDF text is in `background/text/arXiv_2610.10451_Viaclovsky_combs.txt`.
- `papers/arXiv_2610.39102_Viaclovsky_log_transformations.pdf`: Theorem 1.1 and Questions 1–4, finite-root construction, Proposition 4.7 and proof.
- `papers/arXiv_1705.10518_Angella.pdf`: the Hodge constraints and absence of universal h10=0 inference; E2 holomorphic-form vanishings are proved for the actual comb geometry.
- Survey F1, F5, F7, F8, F19 and the relevant B/G1a/G1b notes.

## New primary web sources opened

- Du, Y.-H., Guo, B., Kusakabe, Y., & Xie, S.-Y. (2026), arXiv:2610.00250v1, *Oka geometry and deformations of torus-fibred complex six-spheres*, Section 6, pp. 73–85. URL: https://arxiv.org/pdf/2610.00250v1 . Verified/opened. Its root-stack strategy prompted the independent D calculation. Parent verified that current v2 omits the deformation section and claims; v1 is not treated as an established theorem. The manuscript contains a short provenance paragraph and makes no priority claim.
- Huckleberry, A. T., Kebekus, S., & Peternell, T. (2000). *Group actions on S6 and complex structures on P3*. Duke Mathematical Journal, 102(1), 101–124. https://doi.org/10.1215/S0012-7094-00-10214-1 . Primary preprint opened at https://arxiv.org/pdf/math/9812076 , p. 2, Corollary 1.3 and proof. The proof explicitly invokes CDP98 to make meromorphic coefficients constant. Verified/opened; reference key suggested `HKP2000`.
- NIST Digital Library of Mathematical Functions, §§23.15, 23.18 and 27.14(iv),(vi), especially equations 27.14.12 and 27.14.16–18 for the eta product and discriminant normalization. URLs https://dlmf.nist.gov/23.15 , https://dlmf.nist.gov/23.18 , https://dlmf.nist.gov/27.14 . Verified/opened. D1.2 uses only the weight-twelve transformation and the simple cusp zero of eta^24.

## Computations run and retained

- `code/d_exact.py` with `outputs/d_exact_stdout.txt` and `outputs/d_exact.json`: two independent exact cohomology methods for 481 root weights; all integral-twist indices; explicit tangent local syzygies; two exact cusp character complexes; elliptic doubling and exact order four at t=32/5; comb degree/bound examples.
- `code/d_koszul.py` with `outputs/d_koszul_stdout.txt` and `outputs/d_koszul.json`: explicit tangent-twist differentials, Smith normal forms, independent jet ranks, every finite stabilizer character, and the exact order-three joint scalar. An intermediate incorrect g3 scaling was caught before publication and corrected: y=f^3 wp'/2 requires f^6 g3=-4B=-8t^4(t-1)^2. The final checked coefficient is 123 i k/(64 pi), not the earlier draft number.
- `code/d_division_polynomials.py` with `outputs/d_division_polynomials_stdout.txt` and `outputs/d_division_polynomials.json`: exact division-polynomial factors at P for orders 2–12, supplying the algebraic indexing of regular Picard jump fibres.
- `code/d_comb.py` with `outputs/d_comb_stdout.txt` and `outputs/d_comb.json`: the exact coarse degrees are calculated from both stabilizer-character contributions and all possible nonnegative splitting pairs for m=12,13,20,100. Both methods give h(T)=(2m+1,8m+1,6m+1,0), with the R2 torsion length 4m. For m=12 the tangent tuple is (25,97,73,0).

## Independent audit

The cohomology agent independently checked D1–D3, every integral root character, the cusp extension, the order-three joint coefficient, the explicit Fourier frames and contraction argument, the finite Smith generators, and the E2 determinant and kernel-degree calculations. The Hodge agent independently checked the order-three elliptic expansion and the joint scalar. These are AI checks and are not represented as human replication.

## Remaining unresolved quantity

E2.3 remains unfinished: no exact smoothed comb period section is specified by m alone, and this work does not construct its smoothing matrices and determine the splitting and h0 of K_m or the Kuranishi bracket and higher obstruction maps. All four comb tangent dimensions are nevertheless fully computed in E2.2. All standard-family D items and E1 are answered by proved sheaf calculations; D4 includes the regular nonintegral jumps and both multiple-fibre layers.
