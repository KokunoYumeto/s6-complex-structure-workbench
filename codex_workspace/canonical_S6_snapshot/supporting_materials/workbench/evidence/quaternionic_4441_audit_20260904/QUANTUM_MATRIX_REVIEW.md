# Pure bosonic su(3) three-matrix operator: independent audit

Date: 2026-09-04.

## Completed artifacts

- quantum_matrix_insertion.tex: complete insertion-ready proof with qh:
  labels and collision-free positive coefficients a_g,b_g.
- matrix_quantum_fragment.tex: original full proof with a,b retained,
  preserved as requested.
- exact_matrix_quantum_checker.py: portable checker; 82 exact named
  assertions passed in 1.9 seconds with SymPy 1.13.1.

The insertion copy uses labels qh:matrix-root-sum, qh:matrix-slice,
qh:matrix-compact, and qh:matrix-bottom. Its equation tags are MQ.1-MQ.15.
No canonical, remote, other-lane, or Lean-family changes were made.

## Precise result and constants

The configuration space is the real vector space su(3)^3, dimension 24,
with the unchanged metric <X,Y>=-tr(XY), its Lebesgue measure, and its
orthonormal-coordinate Laplacians. The operator is the Friedrichs
realization of the explicitly closed form

\[
H_A=-a_g\sum_i\Delta_{A_i}
       +b_g\sum_{i<j}\|[A_i,A_j]\|^2,\qquad a_g,b_g>0.
\]

For eigenvalues theta_1<=theta_2<=theta_3 of -iX, with their original
zero trace, the exact sum of square roots of positive eigenvalues of
-ad_X^2, counted with real multiplicity, is

\[
\mathcal S(X)=2\sum_{p<q}|\theta_p-\theta_q|
            =4(\theta_3-\theta_1).
\]

It satisfies the sharp bounds

\[
2\sqrt6\|X\|\leq\mathcal S(X)\leq4\sqrt2\|X\|.
\]

The lower equality is attained at repeated eigenvalues, not invalidated
by them: a nonzero wall has four positive real frequencies; the regular
case has six and the zero matrix has none. Counting each positive root
once instead gives S/2 and the lower constant sqrt(6).

The proof explicitly splits the kinetic and quartic terms into six
directed pair oscillators. For every 0<=vartheta<1 it gives

\[
q[\psi]\geq\vartheta a_g\|\nabla\psi\|_2^2+
2\sqrt{6(1-\vartheta)a_gb_g}
\int\sum_i\|A_i\|\,|\psi|^2.
\]

At vartheta=1/2 this is

\[
H_A\geq-\frac{a_g}{2}\Delta+
                   2\sqrt{3a_gb_g}\sum_i\|A_i\|.
\]

Each original derivative is allocated twice with coefficient
(1-vartheta)a_g/2, and each unordered potential term is allocated
twice with coefficient b_g/2. The proof checks this exact allocation.
No position-dependent diagonalizing basis is differentiated: the
oscillator estimate is applied on a fixed-matrix slice and then integrated.

The form domain is H^1 intersected with the weighted L^2 potential domain.
The proof establishes closure and its C_c^infinity core. It then establishes
compactness directly, without a black-box matrix discreteness theorem:
outside the cube [-R,R]^24 the L^2 mass is at most q/(c_vartheta R);
inside, a piecewise-mean projection on cubes of side h has squared error
at most h^2 q/(vartheta a_g). Hence its full finite-rank approximation
error is bounded by

\[
q[\psi]\left(\frac{h^2}{\vartheta a_g}
                    +\frac1{c_\vartheta R}\right).
\]

Bounded form-domain sets are therefore totally bounded in L^2. The
resolvent factors through this compact inclusion. This proves compact
resolvent and only isolated finite-multiplicity eigenvalues tending
to infinity, despite the unchanged commuting valleys of the potential.

A separate elementary one-dimensional argument gives the additional
explicit absolute energy-origin bound

\[
H_A\geq9(3/2)^{1/3}a_g^{2/3}b_g^{1/3}I.
\]

This number is not asserted to bound the excitation difference E_1-E_0.
The proof uses the exact one-dimensional inequality
-alpha d^2/dx^2+gamma|x| >=
3(alpha gamma^2)^(1/3)/2^(8/3), derived from the first absolute moment
and the derivative norm, then sums the 24 retained coordinates.

## Exact canonical coefficient dictionary and scope

The current canonical homogeneous density and full scalar potential
were read at q444:full-gauge-density and its proof. Its pure gauge
part is

\[
L=\mathcal V_3g^{-2}\sum_i\|\dot A_i\|^2-
\mathcal V_3g^{-2}\sum_{i<j}\|[A_i,A_j]\|^2
\]

in temporal gauge at the unreduced homogeneous coordinate level.
The momentum is 2 V_3 dot(A_i)/g^2. Quantization by
p_i=-i hbar grad(A_i), with hbar>0 retained, gives exactly

\[
a_g=\frac{\hbar^2g^2}{4\mathcal V_3},\qquad
b_g=\frac{\mathcal V_3}{g^2},\qquad a_gb_g=\hbar^2/4.
\]

The full scalar potential m^2 s/2+Gamma s^2/4
-kappa(det Phi-b*Phi b) is recorded, not included in the pure matrix
operator here. The parent handles the scalar coupling and Gauss-invariant
subspace separately. No continuum, infinite-volume, or interacting
field-theoretic mass-gap conclusion is made.

## Primary reading and downloaded versions

The canonical local source read is:

output/s6_consolidated_canonical_2026-08-26/supporting_materials/workbench/research/quaternionic_4441_reconciliation.tex

Read q444:full-gauge-density, the complete displayed homogeneous density,
the retained scalar potential, and their signs and coupling factors.
A bounded local filename search found no separate Simon/Luscher source file.

Downloaded and read the original published scan of B. Simon,
Some quantum operators with discrete spectrum but classically continuous
spectrum, Annals of Physics 146 (1983), 209-220, DOI
[10.1016/0003-4916(83)90057-X](https://doi.org/10.1016/0003-4916(83)90057-X).
Source URL: [author-hosted PDF](https://math.caltech.edu/SimonPapers/158.pdf).
Local file: references/Simon_1983_158.pdf.
This is the 12-page published journal scan, not a new preprint version.
SHA256: DF9C5AF529AD41ED92A78D848A6FFAAFB7E85F4CBB6F788A55A03AB76E57DCB7.

The entire extracted text was read. Following the PDF skill, complete
PDF pages 3,4,8,9,12 (printed pages 211,212,216,217,220) were rendered
and visually read. These contain equation (3), the Section 2 zero-point
oscillator argument, Section 7's Lie-algebra theorem, and the final
note on slice compactness. The complete proof here derives the requested
su(3) constants and direct cell approximation rather than invoking the
paper's Fefferman-Phong theorem. The discreteness phenomenon is classical,
not claimed as a new discovery.

The related M. Luscher publication was checked in its publisher metadata:
[Some analytic results concerning the mass spectrum of Yang-Mills gauge
theories on a torus](https://www.sciencedirect.com/science/article/pii/0550321383904364),
Nuclear Physics B 219 (1983), 233-261,
DOI 10.1016/0550-3213(83)90436-4.
Its bibliographic identity and small-volume scope are cited in the integration
copy. No full Luscher PDF was successfully downloaded: the available mirror
had an expired TLS certificate, and a web fetch failed. No certificate
validation was disabled. No detailed Luscher theorem, perturbative result,
or coefficient is assumed in this proof.

## Actual mechanical scope

Run:

    python exact_matrix_quantum_checker.py

Result: PASS, 82 exact named assertions.

The checker uses only SymPy, no numerical tolerance, no network, and no
external input files. A matrix identity is counted once. Its generic
symbolic checks include the original basis Gram, the eight-coordinate
adjoint and commutator quadratic form, the retained Casimir factor 6,
the full diagonal frequency list, sharp-root remainders, the complex
oscillator completion identity, directed-pair allocation, the lower
energy constant, and the canonical momentum/volume/hbar dictionary.
Exact fixtures include both root walls, zero, equally spaced eigenvalues,
a regular matrix, and a genuinely non-diagonal SU(3)-conjugate root-wall
matrix with metric covariance.

Form closure, integration/Fubini, tail bounds, local approximation and
compactness are proved analytically in the full TeX. They are not
represented as mechanically certified by the finite symbolic checker.
