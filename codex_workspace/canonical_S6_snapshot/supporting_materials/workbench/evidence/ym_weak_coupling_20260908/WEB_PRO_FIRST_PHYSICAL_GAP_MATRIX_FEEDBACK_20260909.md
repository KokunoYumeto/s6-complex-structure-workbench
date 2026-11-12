# Yang–Mills continuation: evaluate the retained physical gap matrix

9 September 2026. This supersedes the earlier request to derive only
the first coupling coefficients. Supply this note together with
cubic_singlet_vacuum_energy.md and operator_coupling_expansion_full_graph.md,
or with the current complete TeX/Bib bundle containing those proofs.
Also include cubic_box_gap_symmetry.md, which proves the exact reduction
of this calculation to three entries without removing any spatial modes.

## What is now calculated

For the original full open-box SU(2) Hamiltonian
\[
 H_g={2g^2\over a}\sum_eE_e+
           {1\over2g^2a}\sum_p(2-\operatorname{tr}U_p),
\]
the exact tree/Haar map gives fully evaluated \(H_1,H_2\), including
both kinetic tensors, every ordered plaquette slot, and the Haar scalar
\(-\operatorname{tr}G/(2a)\). The complete cubic vacuum vector is
\[
 H_1\Phi=\sum_{\mu<\nu<\rho}\Theta_{\mu\nu\rho}
                          \det(z_\mu,z_\nu,z_\rho)\Phi ,
\]
with explicitly computed graph coefficients, raw determinant norm
\(48/(\sigma_\mu\sigma_\nu\sigma_\rho)\), and exact excitation
\((\sigma_\mu+\sigma_\nu+\sigma_\rho)/a\).
Every spatial mode remains.

The full first physical oscillator cluster consists of six color-singlet
quadratics in the three lowest spatial modes. Writing their orthonormal
vectors as \(S_I\), the actual fixed-box first gap satisfies
\[
 \Delta_L(g,a)={2\sigma_*\over a}
                 +g^2\lambda_{\min}(\mathsf K)+O_{L,a}(g^3).
\]
The source proves the cutoff residual, actual spectral projection and
weighted graph estimate; it does not assume differentiability at zero
coupling. The finite coefficient matrix is
\[
 \mathsf K_{IJ}
 =\langle S_I,H_2S_J\rangle-e_2\delta_{IJ}
 -\sum_{|n|=3,5}{c_{I,n}c_{J,n}\over\omega_n-2\sigma_*/a},
 \quad c_{I,n}=\langle h_n\Phi,H_1S_I\rangle .
\]
Its coefficients are specified by finite polynomials and complete
Gaussian pairings in equations (29)–(36), not left as unknown matrix
elements. Degree-one intermediate states vanish by color invariance.
All remaining denominators are strictly positive.

Equations (39)–(44) prove an exact cancellation of spectator vacuum
terms. In the finite normal-ordered polynomial, decompose \(H_n\) into
terms acting only outside the three lowest modes and terms touching at
least one lowest mode. The outside-only cubic and quartic contributions
cancel from \(\mathsf K\), with their full energy denominators and the
Haar scalar retained on both sides. The surviving cubic vectors have at
most two outside quanta. This is an exact computational reduction proved
from occupation numbers, not deletion of high spatial modes.

One further usable estimate is
\[
 \|D_{h,g}u\|\le\sqrt2\|h\|_\infty
 [\,\|H_gu\|^2+6|P|\|u\|^2/a^2\,]^{1/2}.
\]
It follows by integration by parts from \(KW=3W-6|P|\) and the original
\(\kappa b=a^{-2}\), so it does not lose two powers of \(g\).

## One bounded, demanding next calculation

Evaluate the complete matrix \(a\mathsf K\) on the original \(L=2\)
box, retaining all 176 spatial modes, all original edges and faces,
and all color contractions. Use the spectator cancellation to avoid
enumerating irrelevant occupation lists. The cubic-box symmetry proof
now gives exactly a \(3\times3\) diagonal-state block with entries \(d\)
on its diagonal and \(o\) off its diagonal, and an off-diagonal-state
block \(cI_3\), with no mixing. Thus only \(ad,ao,ac\) need evaluation:
the six corrections are \(a(d+2o)\) once, \(a(d-o)\) twice, and \(ac\)
three times. The proof constructs the original signed graph symmetries
and their nonlinear-chart/physical-band correspondence; do not assume
the particular rooted tree was itself invariant. Give certified rational
intervals for its six eigenvalues, or an exact algebraic representation
and a reproducible integer outward-enclosure checker. Include the
actual tree, full transverse basis, mode ordering, matrix entries,
and the map back to the physical correction
\(g^2a^{-1}\lambda_{\min}(a\mathsf K)\). Multiplying by \(a\) here
records the exact scale factor; it does not set the physical spacing
or energy to one.

Do not substitute a smaller graph, one plaquette, a lowest-mode
truncation, an Abelian color sector, or floating-point eigenvalues
presented as exact signs. Do not repeat only the nonzero cubic vertex
certificate: the target is the complete physical excitation correction,
including the moving vacuum and quartic terms.

Then inspect the resulting contraction formula for the term whose
dependence on \(L\) would govern a physical-scale limit. Any asymptotic
claim must be derived from that formula with an explicit error.
The sign at \(L=2\), by itself, proves neither a mass gap nor its failure
in an interacting continuum. If the finite matrix is all that can be
completed, deliver its complete checked calculation without replacing
the remaining question by an assumed bound.

## Existing checks and scope

The supplied check_cubic_singlet_vacuum_energy.py currently verifies
85 exact identities: arbitrary ordered SU(2) face coefficients through
degree four; symbolic quartic covariance; cubic kinetic contraction;
the three-mode eigenvalue and raw norm; exact rational kinetic Wick
tests; and all six first-cluster norms, cross inner products and
excitations. It does not evaluate the full \(L=2\) matrix and is not
a continuum certificate.

The separate check_cubic_box_gap_symmetry.py passes 99 exact checks:
all 48 signed-coordinate actions on the lowest modes and their six
quadratic states, every commutator with the displayed matrix, the full
symmetric commutant dimension three, and the complete characteristic
polynomial. This verifies the finite matrix algebra, not the pending
three coefficient values.
