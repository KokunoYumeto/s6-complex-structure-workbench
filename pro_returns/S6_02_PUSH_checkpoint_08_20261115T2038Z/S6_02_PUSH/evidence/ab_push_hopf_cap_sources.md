# Primary-source audit for the parabolic cap and analytic comparison

2026-11-15, 16:40–16:58 UTC. Queries: `Hopf surface elliptic curves normal bundle diagonal contraction primary`; `Nishiguchi degenerations K3 surfaces Hopf elliptic curves d semistable`; `"Irreducible degenerations of primary Kodaira surfaces" journal 2000`; `"Complex surfaces with many algebraic structures" authors arxiv`; stronger verification queries `"degeneration" "tori" "Hopf" "surface"` and `"semistable" "complex tori" "Hopf"`.

1. Opened Schröer–Siebert, *Irreducible degenerations of primary Kodaira surfaces*, author PDF <https://www.math.uni-duesseldorf.de/~schroeer/publications_pdf/kodaira.pdf>. Section3, Proposition3.1, pp6–7: diagonal Hopf quotient and elliptic curves; Proposition3.4, p9: explicit normal-line factors and T1 product. Introduction explicitly limits its claims to the stated Kodaira-surface setting. Publication metadata independently opened at <https://www.math.uni-hamburg.de/home/siebert/research/research.html> and <https://arxiv.org/abs/math/0001077>: *Complex geometry (Göttingen,2000)*,193–222, Springer,2002. Existing bibliography key SS00 is reused; no duplicate entry added.

2. Opened Nishiguchi's original MPI/88-48, *Degeneration of K3 surfaces,II*, <https://archive.mpim-bonn.mpg.de/id/eprint/3390/1/preprint_1988_48.pdf>. Theorem1.4,p7 and §§2–3 explicitly permit Hopf/CB components; Example1.8,pp10–12, has parabolic Inoue components and elliptic overlaps. These are cautionary comparisons, not an existence theorem for the S6 degeneration. Existing key Nishiguchi1988IIRoot is reused.

3. Opened Abasheva–Déev author preprint <https://arxiv.org/pdf/2303.10764>, Section2.2,pp4–5, including diagonal contraction, scalar cases, degree-zero line factors, and normal-bundle classes. Published DOI metadata <https://doi.org/10.1093/imrn/rnad190> identifies IMRN2024(9),7379–7400. The direct OUP article open returned a non-retryable500 redirect; the primary arXiv PDF was opened instead. Paragraph2.2.5's claim that all automorphisms of a diagonal Hopf surface are diagonal is overbroad for a scalar contraction. Our proof does not use that sentence: the scalar nonisomorphism follows directly by Hartogs extension and the derivative at zero. New bibliography key AbashevaDeev2024AB records the precise scope.

4. Stronger searches for general non-Kähler torus-degeneration classification again returned Kamenova's theorem with Kähler-total-space and trivial-canonical-bundle assumptions; neither is imported. No unrestricted comparison theorem was found or asserted.

## Constructive proof and exact data

`sections/ab_push_hopf_cap.tex` constructs the principal elliptic bundle by an explicit cocycle from two line bundles on the blow-up of P1×disc. Properness, smoothness, the local xy=u model, the two central Hopf multipliers, and the generic product are proved there. The no-meromorphic-comparison assertion uses the already established invariance of π1 under smooth proper modifications and the semistable retraction, rather than an unproved classification of exceptional components.

`code/ab_push_hopf_cap.py`, `.out`, `.json` contain exact Chern and normalization matrices, Smith factors, Betti/Euler calculations, and the symbolic determinant identities proving generic simplicity of the prescribed two-tori. The latter is a limitation on adapting this example; the example is explicitly not an S6 filling.

## Fujimoto primary-source attribution, 17:11--17:21 UTC

Opened the HUSCAP primary proceedings PDF <https://eprints.lib.hokudai.ac.jp/repo/huscap/all/5450/16.pdf>, and visually inspected the paper heading on zero-based PDF page84. The heading is *Generalized Logarithmic Transformations---elliptic bundle case*; the contents use the alternate title recorded in the BibTeX note. Definition1.1 (printed85--86) is exactly the known Cartier logarithm mechanism used in B.4.7. Proposition1.14 (printed93) concerns extension of fixed principal elliptic bundles across codimension at least3. Example1.15 (printed93--94) does not claim nonexistence of every relative compactification. Root is separately documenting later Fujimoto1988/Nakayama results. Example1.11 has a trivial E-bundle over a (1,1) curve in P1×P1; direct normal pullback gives O_P1(2), not a trivial normal line. No theorem for simple two-torus degenerations is imported.

Corrected the missing backslash before `exp` in the scalar Hopf multiplier. This is a typesetting correction, not a change in the exact multiplier calculation.
