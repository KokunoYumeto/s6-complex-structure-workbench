# Bounded audit of the coupled quantum compactness proof

Date: 4 September 2026. Read-only audit; no canonical changes, child agents, other-task contacts, Lean, or heavy calculations.

## Assignment, verbatim

> Thanks. Before integration, independent bounded audit of the root+matrix quantum proof useful now: read agent_work/quaternionic_quantum_root_20260904/ROOT_PROOF.tex and agent_work/quaternionic_matrix_quantum_check_20260904/matrix_quantum_fragment.tex. Check scalar sharp bound (convex vertices), exact coefficients, full 38-coordinate compactness, and the absolute energy-origin bound; look for real gaps or missing assumptions. Output short audit in your directory; no canonical changes, children or heavy runs. Intrinsic supplement is retained for next integration, not discarded.

Both named TeX files were read completely. The root logbook was also read to distinguish an integration dependency from missing mathematical work.

## Verdict

**The scalar bound, all checked constants, directed-pair oscillator argument, full 38-coordinate compactness argument, and pure-matrix absolute-energy bound are correct. No substantive counterexample or coefficient error was found.** The matrix proof includes its form-domain/core construction and handles root walls correctly. The root fragment still needs the full-operator/domain/positive-parameter setup promised by its logbook; the integration details below make that dependence precise.

## Scalar estimate and exact constant

For fixed eigenvalues and (u=\sum z_i>0), the coefficients (z_i/u) are nonnegative and sum to one. Each vertex is exactly

\[
 \lambda_i(\lambda_j\lambda_k-u)
 =\lambda_i^3-s\lambda_i/2,
 \qquad
 s=(3\lambda_i^2+d_i^2)/2+2u,
 \quad d_i=\lambda_j-\lambda_k.
\]

Hence (|\lambda_i|\leq\sqrt{2s/3}). The two stationary points and two endpoints of (x^3-sx/2) on this interval all have absolute value (s^{3/2}/(3\sqrt6)). The triangle inequality applied to the convex combination proves the stated bound. The separate (u=0) and (s=0) cases are handled correctly; the exhibited diagonal field attains equality, so the constant is sharp.

For (\alpha=|\kappa|/(3\sqrt6)), the minimum of (\Gamma t^4/8-\alpha t^3) over (t\geq0) is attained at (t=6\alpha/\Gamma) when (\alpha>0). Its value is

\[
 -54\alpha^4/\Gamma^3=-\kappa^4/(54\Gamma^3).
\]

Thus (C_\kappa), the retained quartic coefficient (\Gamma/8), and both signs of (\kappa) are correct. No potential or energy origin has been replaced by this bounding expression.

## Matrix frequencies and coupled coefficients

The real root multiplicity is two per unordered root. Consequently

\[
 \mathcal S(X)=2\sum_{p<q}|\theta_p-\theta_q|
 =4(\theta_3-\theta_1)\geq2\sqrt6\|X\|.
\]

At a nonzero wall four real positive frequencies remain. In (MQ.9), each derivative and each unordered commutator potential has exactly its original total coefficient. One directed pair contributes (\sqrt{(1-\vartheta)ab}\,\mathcal S(A_i)/2); two partners per fixed (i) therefore give (2\sqrt{6(1-\vartheta)ab}\|A_i\|). With the original coefficients

\[
 a_g=\hbar^2g^2/(4\mathcal V_3),\qquad b_g=\mathcal V_3/g^2,
 \qquad a_gb_g=\hbar^2/4,
\]

the root coefficient (\hbar\sqrt{6(1-\eta)}) is exact. Also ([A_i,\Phi]^*=[A_i,\Phi]), so its squared trace term has the required nonnegative sign; (\|A_ib\|^2\geq0) directly. The scalar kinetic metric has fourteen real dimensions, and the gauge factors have (3\cdot8=24), totaling thirty-eight.

## Compactness and the integration details to retain

The tail dichotomy (\sum_i\|A_i\|^2\geq R^2/2) or (s\geq R^2/2) is exhaustive outside (r<R). Both entries of the displayed (w_R), including the scalar factor (\mathcal V_3\Gamma R^4/32), are correct. The cube-complement inclusion has the right direction. The dimension-independent cube estimate is valid: distinct summands (P_1\cdots P_{j-1}(I-P_j)\psi) are orthogonal, and prior-coordinate averaging contracts the relevant derivative norm. It therefore applies in thirty-eight coordinates with the stated constant. The finite-rank approximation proves compactness in all coordinates, including commuting gauge directions.

Before treating `ROOT_PROOF.tex` as a standalone theorem, integration should explicitly provide:

1. **Parameters and the full operator.** Retain (\hbar>0), (g^2>0), (\mathcal V_3>0), (\Gamma>0), (m^2\geq0), and (\kappa\in\mathbb R). The root theorem's “full Hamiltonian of this paper” and “stated parameters” (approximately lines 89–118) depend on that setup. Positivity of the first three parameters is essential, not cosmetic.
2. **The full shifted form/core.** Put (c_E=\hbar^2/(2\mathcal V_3)) and write the original multiplication potential explicitly as

   \[
   \mathcal U=\frac{\mathcal V_3}{g^2}\sum_{i<j}\|[A_i,A_j]\|^2
   +\frac{\mathcal V_3}{2}\sum_i\operatorname{tr}[A_i,\Phi]^2
   +\mathcal V_3\sum_i\|A_ib\|^2+\mathcal V_3V(\Phi,b).
   \]

   The proved scalar bound gives (\mathcal U+\mathcal V_3C_\kappa\geq0). Thus the shifted full form has domain

   \[
   \{\psi\in H^1(\mathbb R^{38}):
        \sqrt{\mathcal U+\mathcal V_3C_\kappa}\,\psi\in L^2\},
   \]

   and value (a_g\|\nabla_A\psi\|^2+c_E\|\nabla_E\psi\|^2+
   \int(\mathcal U+\mathcal V_3C_\kappa)|\psi|^2). Completeness follows from (H^1) convergence, convergence of the weighted products, and an almost-everywhere subsequence identifying their limit. Smooth cutoffs converge in both norms; compactly supported mollification then converges because this continuous weight is bounded on a fixed enlarged compact support. This supplies the full-form core needed at root lines 118–120, by exactly the argument already written for the matrix form. The root logbook says that this setup is being supplied by another integration fragment, so its absence here is not evidence that the assembled paper lacks it.
3. **Name a coercive resolvent shift.** At root lines 166–168, use (\widetilde q+\|\psi\|_2^2) in the Riesz construction, yielding ((H_{\rm hom}+(\mathcal V_3C_\kappa+1)I)^{-1}). Nonnegativity of (\widetilde q) alone is not the usual Riesz coercivity statement. This extra shift makes the argument immediate, with no need to infer a positive bottom during the compactness proof. It changes no physical energy origin.

## Absolute energy origin, not an excitation-gap constant

The one-dimensional estimate is valid: the two-ended integration bound gives (\|f\|_\infty^2\leq\|f\|_2\|f'\|_2), and Markov's inequality then gives (tM^2\geq1/64). Minimization yields exactly (3(\alpha\gamma^2)^{1/3}/2^{8/3}). Summing twenty-four coordinates with (\alpha=a/2) and (\gamma=\sqrt{3ab/2}) gives

\[
 H_A\geq9(3/2)^{1/3}a^{2/3}b^{1/3}I
 =9\left(\frac{3\hbar^4g^2}{32\mathcal V_3}\right)^{1/3}I.
\]

Combining only with the scalar bound and the other nonnegative terms gives the valid full-model absolute-origin statement

\[
 H_{\rm hom}\geq
 \left[9\left(\frac{3\hbar^4g^2}{32\mathcal V_3}\right)^{1/3}
 -\frac{\mathcal V_3\kappa^4}{54\Gamma^3}\right]I.
\]

That bracket need not be positive. Neither this estimate nor the positive pure-matrix bottom is a lower bound on (E_1-E_0); the source correctly distinguishes them. Compactness establishes discrete finite-multiplicity levels, not this numerical value for their separation, and not a uniform infinite-volume or continuum gap.

One harmless statement refinement: in the matrix root-sum lemma, either explicitly restrict the upper-equality characterization to nonzero (X), or permit (r=0) in ((-r,0,r)). The proof already correctly records equality at (X=0).

The intrinsic Lie-normalizer supplement remains retained for its next integration; nothing in this audit discards or replaces it.
