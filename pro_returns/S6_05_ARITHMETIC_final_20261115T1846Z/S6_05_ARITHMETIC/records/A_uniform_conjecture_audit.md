# Uniform character-sum criterion: primary-source audit

Updated 15 November 2026, 18:10 UTC.

The existing Statement A.5.4 now includes the exact sufficient hypothesis

\[
\left|\sum_{z\leq X}a_\ell(18z^2-2)-{\bf1}_{\ell=0}cX\right|
\ll_\eta X^{1/2+\eta}(1+|\ell|)^\eta,\qquad
|\ell|\leq \lfloor\sqrt X\rfloor.
\]

The proof of its implication to the requested sharp square-root bound uses the
positive ideal counting measure, its exact Fourier coefficients, weighted
Erdős–Turán at H=floor(sqrt X), and the already proved Pell endpoint correction.
This is an explicitly proposed sufficient hypothesis, not a named conjecture
claimed to have been found in the literature. The requested implication from
a numbered published conjecture remains undecided.

## Sources opened in full and their exact scope

1. Nordentoft, A. C., Petridis, Y. N., and Risager, M. S. (2022).
   *Bounds on shifted convolution sums for Hecke eigenforms*. Research in
   Number Theory, 8, 26. https://doi.org/10.1007/s40993-022-00320-1
   Primary full text:
   https://link.springer.com/article/10.1007/s40993-022-00320-1
   Equation (2) states the expected sharp X^(1/2+epsilon) h^epsilon bound
   with an O_f constant, for a fixed holomorphic level-one form. The following
   paragraph explicitly says that possible k^epsilon dependence and the
   weight-uniform range are not settled in the formulation. Proposition 1.1,
   under Ramanujan–Petersson for Maass forms, concerns a fixed smooth weight
   and an O_(f,W) constant. Neither statement supplies our varying
   real-quadratic characters through |ell|≈sqrt X.

2. Nelson, P. D. (2022). *Quadratic Hecke sums and mass equidistribution*.
   International Mathematics Research Notices, 2022(17), 13659–13701.
   https://doi.org/10.1093/imrn/rnab093
   Primary author preprint, version 3:
   https://arxiv.org/pdf/2001.08704
   Conjectures 1.6 and 1.8 assume non-dihedral holomorphic full-level forms
   and irreducible integer-valued quadratic polynomials. Their rates are
   o(k) and logarithmic savings, respectively, not the desired square-root
   sum. Remark 1.9 explicitly leaves formulation of dihedral/reducible
   variants for further work. Remark 1.13 explains the fixed-form uniformity
   limitation of earlier shifted-convolution estimates. Our polynomial
   18z²−2 has discriminant 144 and is reducible.

3. Merikoski, J. (2025). *On primes represented by aX²+bY³*.
   arXiv:2503.05396, version 1.
   https://arxiv.org/pdf/2503.05396
   Conjecture C_a(epsilon), printed on preprint page 2, has precisely the
   real-quadratic ideal Hecke coefficients and epsilon dependence on
   discriminant and |ell|². Its sum, however, runs over a rectangle of
   two variables and the argument is |(c1*y1³−c2*y2³)/a|.
   The weaker Conjecture L_(a,b)(epsilon), Remark 7.1, is also about
   binary cubics and an average over discriminants.
   Section 1.2.4 discusses other sequences without stating a corresponding
   general conjecture. Equations (2.2) and (2.3) use the same absolute-norm
   ideal-character conventions as our A.4.2.
   Restricting the binary cubic to an affine line on which its cubic
   coefficient cancels does not produce our polynomial: after rational
   rescaling this is (u+h)^3−u^3, whose quadratic discriminant is
   −3h^4. Extracting a diagonal from bounds on rectangles would in any
   case need an extra argument and cannot be done without a loss.

4. Michel, P. (2003). *On the shifted convolution problem*. Lecture at the
   Fields Institute, 5 May 2003.
   Working primary PDF:
   https://www.epfl.ch/labs/tan/wp-content/uploads/2018/10/Fields2003.pdf
   This is Michel's lecture, not a paper authored by Sarnak. The lecture
   quotes a Sarnak shifted-Dirichlet-series theorem. Its numbered
   Conjecture 1 is a triple-product average for a particular level-aspect
   application; it is not a sharp sum with epsilon-uniform dependence on
   the varying Maass spectral parameter. The EPFL repository API URL
   redirected to an expired CDN URL in the web tool; the author-hosted
   URL above opened successfully.

5. Blomer, V., Jana, S., and Nelson, P. D. (2025).
   *Local integral transforms and global spectral decomposition*.
   Geometric and Functional Analysis, 35, 1051–1107.
   https://doi.org/10.1007/s00039-025-00714-0
   Full primary HTML:
   https://link.springer.com/article/10.1007/s00039-025-00714-0
   Theorem 5, including (1.17) and (1.18), keeps f,g and the smooth
   weight fixed. Section 4.1 also keeps the relevant local representations
   fixed in its constants. No numbered uniform sharp shifted-sum
   conjecture covering our family was located in the text.

6. Xu, Z. (2025). *Uniform subconvexity bounds for GL(2)×GL(2)
   L-functions in the spectral aspect*. arXiv:2509.05968, version 1.
   https://arxiv.org/pdf/2509.05968
   Theorem 1.1 and Corollary 1.2 give uniform spectral-aspect Rankin–Selberg
   moment/subconvexity statements, with square-free level and real primitive
   nebentypus hypotheses. They do not state a sharp shifted-sum square-root
   conjecture. Our natural discriminant is 12, so even the stated
   square-free-level condition must not be silently ignored.

## Main next test

The direct ternary delta-method candidate remains Sun (2025), Conjecture 1.4,
with the theta contribution removed. The exact good-modulus Gauss calculation
and the current arithmetic/multiplier issues are in
records/B_A5_Sun_delta_obstruction.tex.
The present analytic test retains the amplitude multiplying e(D/q), because
an inverse-phase factor q/D can compensate the derivative of that phase.
The decisive remaining question is the sum over the growing dual-frequency
range after this compensation. A single radial face-normal ray would have
one O(1) variation per retained frequency. The pure normal ray has square
dual norm and requires a theta-term audit, so a fixed nonzero tangential
translate such as c=(1,0,k), with H(c)=k²−18, is the more informative test.
No conclusion from this model to the actual arithmetic remainder is yet
claimed.

## Follow-up at 18:34 UTC: compensation and completion quantified

The test just proposed has now been completed. The full weight, including
the reciprocal phase amplitude, has total modulus variation bounded below
per retained radial frequency. See records/B_A5_compensated_weight.tex and
the independent audit records/A_compensated_weight_independent_audit.md.
The direct absolute Abel estimate has scale X^(1/2+epsilon) K on a dyadic
normal-frequency block K. Completing that frequency first gives an exact
ordinary-Kloosterman transformation, with all normalizations and 200 exact
cyclotomic-ring checks preserved in records/A_normal_completion.tex and
code/A_normal_completion_check.py/.out. Steiner (2019), Conjecture 2,
applies to each resulting fixed-h modulus sum with s=24 and B=3, but
absolute summation over h has scale X^(1+epsilon)/K. The crossover remains
X^(3/4+epsilon) at K=X^(1/4). These are limits of the two specified
procedures, not a proof of logical nonimplication from either conjecture.

A final targeted search for a published joint quadratic-index/modulus
conjecture did not supply the missing bound. The following additional
primary source was opened in full:

El Abdalaoui, H., Shparlinski, I. E., and Steiner, R. S. (2024).
Chowla and Sarnak conjectures for Kloosterman sums. Mathematische
Nachrichten, 297(1), 209–228. https://doi.org/10.1002/mana.202200480
Full primary HTML:
https://onlinelibrary.wiley.com/doi/full/10.1002/mana.202200480
Conjectures 2.1 and 2.2 fix the Kloosterman index and give qualitative
little-o statements in the horizontal aspect. Their Theorem 2.8 is a
vertical bound at one fixed prime modulus. None states the quantitative
joint estimate needed when h is near X, the index is 18h^2−2, and q is
near X. No transfer of those statements is asserted.
