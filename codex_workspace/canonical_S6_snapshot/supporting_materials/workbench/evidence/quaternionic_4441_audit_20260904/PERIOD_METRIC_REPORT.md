# Period-metric fibres: completed independent audit

## Deliverables and verification

- Complete insertion-ready mathematics: period_metric_fibres_fragment.tex.
- Portable exact checker: exact_period_metric_checker.py.
- Continuity and assignment provenance: WORK_LOG.md.

Run with Python and SymPy installed:

    python exact_period_metric_checker.py

Result: **all 61 exact checks passed**, exit code 0, SymPy 1.13.1.
The checker imports no canonical verifier, reads no data files, and uses
no floating-point arithmetic or numerical tolerances.

The fragment uses the ordinary theorem/proposition environments and provides
each requested label exactly once:

- q444:metric-fibre
- q444:metric-condition
- q444:rank-loss-metric

All TeX environments are balanced; there are no unexpected control
characters. No PDF build was performed, as this lane was confined to
report, checker, and source fragment.

Verified SHA-256 values:

- exact_period_metric_checker.py:
  9F2B837BD36BEF801E1AB556CC048183CB09AAB53F01CA35A49972AAC8FE9B26
- period_metric_fibres_fragment.tex:
  227AFC6501F0865ED93AAA446882AE6CDA1AC035B660CCE35E889E73D5921268

The audited canonical source snapshot had SHA-256
58597451E6D631B93CF9090B215A7559717A4FA94D869820EF665309DA931E7A.
The parent may subsequently edit that source. This agent made no canonical,
remote, PDF, or other-task edits and launched no Lean-family process.

## Complete result and where its proof lives

The TeX fragment contains the full definitions, inverse maps, matrix
factorizations, domain restrictions, positivity arguments, monodromy
identities, dimension arguments, norm bounds, and asymptotic proofs. The
following identifies its exact scope; it does not replace those proofs.

All original periods are retained, including the distinction between the
period right inverse S and the marked metric right inverse R. On the
guaranteed smaller cusp

\[
y=-\log|t|/(2\pi)>\max\{K,1\},\qquad \|C_3(t)\|\leq K,
\]

the original real period map

\[
\mathcal N=
\begin{pmatrix}I_3&xI_3+\operatorname{Re}C_3\\
0&yI_3+\operatorname{Im}C_3\end{pmatrix}
\]

is invertible. This is proved from
\(\|(yI+\operatorname{Im}C_3)v\|\geq(y-K)\|v\|\), not assumed
as an outstanding condition. No claim is made at other points where
this real period map might become singular.

For every prescribed positive complex Hermitian \(H=E+iF\), the exact
positive real lattice-metric fibre is

\[
W_3=\mathcal N^{-1}
\left[
\frac12\begin{pmatrix}E&-F\\F&E\end{pmatrix}
+\begin{pmatrix}U&V\\V&-U\end{pmatrix}
\right]\mathcal N^{-\mathsf T},
\]

where \(U,V\) are real symmetric and the bracket is positive definite.
The fragment supplies its complete Schur-inequality parameter domain.
It is a twelve-real-dimensional nonempty open convex fibre, not a unique
metric. The choice \(U=V=0\) proves existence for every positive \(H\).

The exact positive image of the observation is all \(G\succ0\).
All its positive intermediate lifts are

\[
H=X\begin{pmatrix}
G&z\\z^*&z^*G^{-1}z+\tau
\end{pmatrix}X^*,\qquad z\in\mathbb C^2,\quad\tau>0.
\]

The observed real-metric fibre consequently has dimension seventeen;
the fragment also proves this directly from rank four of the linear
observation map on the 21-dimensional real symmetric metric space.
Singular \(G\) cannot occur at an interior point with a positive metric,
because both relevant complex adjoints are injective.

Every smooth positive \(H(t)\), and hence every smooth positive \(G(t)\),
has a smooth equivariant metric lift. The exact identity
\(\mathcal N(s+1)=\mathcal N(s)M_3\) yields
\(W_3(s+1)=M_3^{-1}W_3(s)M_3^{-\mathsf T}\).
There is no holomorphic requirement on the real metric or the prescribed
Hermitian observation.

## Retained-constant condition obstruction

The complete analytic proof in the fragment gives, for
\(W_*=M(x)W_3M(x)^T\) and \(aI_6\preceq W_*\preceq bI_6\),

\[
a[1+(y-K)^2]C\preceq G\preceq b[1+(y+K)^2]C.
\]

The original eigenvalues of \(C\) are 1 and 3. In particular

\[
\frac{\lambda_{\min}G}{\lambda_{\max}G}
\geq
\frac{1+(y-K)^2}
{3\kappa_*(t)[1+(y+K)^2]},
\qquad
\kappa_*=\frac{\lambda_{\max}W_*}{\lambda_{\min}W_*}.
\]

Therefore observed projective rank loss forces
\(\kappa_*(t)\to\infty\). Bounded relative condition number alone
excludes it, even with a variable common metric scale. The matrices
themselves are not normalized; the ratio is only a stated diagnostic.
Conversely, divergence of the metric condition number is not claimed
to imply observed rank loss.

## Explicit rank loss and its full constants

For arbitrary retained constants
\(\alpha_{\rm obs},\beta_{\rm obs},\lambda,p>0\), the fragment constructs

\[
G=\operatorname{diag}(\alpha_{\rm obs},\beta_{\rm obs}y^{-p}),
\qquad H=RGR^*+\lambda uu^*,
\]

and its exact smooth positive metric lift. It proves

\[
\det G=\alpha_{\rm obs}\beta_{\rm obs}y^{-p},
\]

\[
\det W_*=
\frac{\alpha_{\rm obs}^2\lambda^2\beta_{\rm obs}^2y^{-2p}}
{64\det(yI+\operatorname{Im}C_3)^2},
\]

with the unchanged correction retained explicitly through

\[
\det(yI+\operatorname{Im}C_3)
=y\left[y^2+y\,\operatorname{tr}((\operatorname{Im}C_2)B_0^{-1})
+\det(\operatorname{Im}C_2)\right].
\]

Writing \(L_{\max}=\max\{2\alpha_{\rm obs}/3,3\lambda\}\),
the full analytic eigenvalue argument proves

\[
\det W_*\sim
\frac{\alpha_{\rm obs}^2\lambda^2\beta_{\rm obs}^2}{64}y^{-2p-6},
\qquad
\lambda_{\min}W_*\sim\frac{\beta_{\rm obs}}4y^{-p-2},
\]

\[
\lambda_{\max}W_*\longrightarrow L_{\max}/2,
\qquad
\kappa_*\sim\frac{2L_{\max}}{\beta_{\rm obs}}y^{p+2}.
\]

These limits hold with the original \(y=-\log|t|/(2\pi)\). The
bounded correction contributes to the exact determinant and metric,
even though it does not alter these leading coefficients.

## Precisely what is and is not selected

The correction map itself is injective on the retained image:
\(C_2=PC_3SB_0\). The fragment proves the exact compensating congruence
between two period--metric pairs,

\[
\widetilde W_3=
(\widetilde{\mathcal N}^{-1}\mathcal N)
W_3(\widetilde{\mathcal N}^{-1}\mathcal N)^T,
\]

which preserves the observed \(H\), positivity, and monodromy.
Thus the observation cannot recover the period correction when the
metric is unconstrained in this way. Its constants have been retained
in the compensating metric, not silently erased.

For the very same periods the admissible relative choice \(W_*=I_6\)
gives the canonical growing determinant \(3y^4+O(y^3)\), whereas
the constructed family gives a determinant tending to zero.
This proves nonselection from period data and positivity alone.
No metric-selection law, units, dynamics, physical mass identification,
quantum gap, or extension across other fillings has been inferred.

## What the executable assertions cover

The 61 assertions check the original period intertwiners and correction
inverse; the full symbolic inverse real period map; the complete
twelve-parameter kernel and linear ranks; the exact Hermitian quadratic
form proving positivity of the realification; inverse-congruence
monodromy; the full positive observed \(H\)-lift factorization; the
relative Gram expansion; the scalar limit of the condition bound; the
exact rank-loss determinant and characteristic polynomial with all
constants; and a full nonreal rational example in the original period
coordinates, whose six leading principal minors are all positive.

The checker does not replace analytic proofs of smoothness, uniform
operator-norm bounds, or the least-eigenvalue asymptotics with sampling.
Those proofs appear in full in the insertion-ready TeX fragment.
