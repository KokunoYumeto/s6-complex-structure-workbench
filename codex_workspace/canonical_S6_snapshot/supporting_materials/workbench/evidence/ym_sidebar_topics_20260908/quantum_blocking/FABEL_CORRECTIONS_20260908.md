# Mathematical corrections and new tensor transfer — 8 September 2026

These corrections concern this task's Fabel addenda, not a change to the
original Hamiltonian or vacuum. The earlier messages and drafts are historical.
Their prior scalar checker passes did not verify the following missing maps.

1. **Weighted operator and expectation.** The unfinished affine draft wrote
   only \(\sum_e f_eE_e\). The source's local-energy operator is
   \(D_f=\kappa\sum_e f_eE_e+\sum_p f_pb(2-W_p)\), with
   \(f_p=\frac14\sum_{\partial p}f_e\). For \(f=c_0+t\cdot m\),
   \(\langle D_f\rangle=c_0E_0\), not zero in general. Its centered
   constant component vanishes because \(D_{c_0}=c_0H\).
2. **Endpoint law and sign.** Ordinary column transport \(P'=-\mathcal A P\)
   obeys \(P^h=h_t^{-1}Ph_s\). The retained lattice convention requires
   \(U=P^{-1}\), so \(U^h=h_s^{-1}Uh_t\) and
   \(U_p=I+a^2F_{ij}+O(a^3)\). The old negative Cartan angle changes sign;
   its trace and magnetic energy are unchanged. A noncommuting negative
   control now detects the old endpoint error.
3. **Configuration versus state.** \(W_C(U[\mathcal A])\) is a background
   evaluation; the generic centered state \(\psi(W_C-\mu W_C)\) is
   independent of that background. The earlier draft had not constructed
   a background-dependent wave-functional. The new explicit maps use the
   full material covector and tensor as specified spatial weights of \(D_f\).
   They do not claim a fluid-to-Hamiltonian dynamical intertwiner.
4. **Vacuum moment and scaling.** \(r_C=\mu(W_C^2)\) is not a classical
   background square. The factor \(1-r_C/4\) must remain. The proven bounds
   give \((3\alpha/4)\kappa\ell\le a_C\le(1-\alpha/4)\kappa\ell\);
   they do not prove \(a_C\sim2g^2P_C/a^2\) with ratio one. Bare-loop
   numerator growth cannot be assigned to a Schur-reconstructed state
   without retaining \(M_1,M_2\). The strong-coupling bound on reconstructed
   states is used only on its original parameter range.
5. **Concentration.** Pointwise vorticity growth need not imply divergence
   of its squared spatial integral. The concentrating volume must be kept.
   During a spatial continuum path \(a\downarrow0\), \(\kappa\to0\) implies
   \(g\to0\); without that spacing condition the implication was too broad.
6. **Sources.** The new peer broadcast points to an actual public
   Navier–Stokes manuscript and pinned formal source. This task has checked
   their availability and the exported theorem statements, not the full
   analytic or kernel proof. They must not be represented as an independent
   proof completed here, nor confused with the stationary Fabel polynomial.

The new non-affine map is \(S\mapsto\Xi_{m^\mathsf T S m}\).
Its full positive spectral measure has three exact cubic-symmetry sectors:
\[
\nu_S=\frac{(\operatorname{tr}S)^2}{9}\nu_0+
\frac12\sum_i(S_{ii}-\operatorname{tr}S/3)^2\nu_{\rm d}
+\sum_{i<j}S_{ij}^2\nu_{\rm o}.
\]
For the actual \(K_\tau=C_\tau C_\tau^\mathsf T\), the complete endpoint is
\[
z^{12}\nu_{K_\tau}\longrightarrow
\frac{113569}{36864}\nu_0+
\frac{100825}{12288}\nu_{\rm d}+
\frac{531}{512}\nu_{\rm o},\qquad z=\sqrt{1-8\tau}.
\]
The limit holds in total variation and for the first two moments at a fixed
regulator. The raw state has not been normalized. The complete first-surviving
coefficient is
\[
\mathcal D_{S_*}=
\frac{L(14536832L^4+5453566L^2-1614327)}{24576}.
\]
For small positive coupling on a fixed box this yields nonzero states and
quotient \(234\kappa/49+O_L(\kappa\xi^2)\).
The three unknown interacting seed-sector limits at changing regulators
remain unevaluated. No counterexample or all-theory exclusion follows.

The cumulative TeX/PDF/Markdown now include the full proof. The authoritative
new diagnostic is check_fabel_tensor_transfer.py and FABEL_TENSOR_TRANSFER_CHECKS.json:
45 grouped exact checks, including all 36 coefficient entries on four open
boxes, all 48 signed-permutation maps on two boxes, exact boundary moments,
the full material matrix, and noncommuting transport negative controls.
These diagnostics check algebra and geometry; they do not compute the vacuum
spectrum or certify the external Navier–Stokes proof.

## Subsequent continuation in Section 14

The former unevaluated lowest-band question is now answered by the full
weighted weak-coupling graph calculation in FABEL_LOW_MODE_TRANSFER.md.
Every nonzero real symmetric tensor has positive raw mass in the
six-dimensional first physical band at sufficiently small positive
fixed-box coupling. The full Fabel path produces actual projected states
whose raw squared norms grow as a specified positive constant times
j^18 and whose energy quotients decay as 100 sqrt(2) pi / j.
The whole-state spectral fraction and an explicit lower bound are retained.
This is a proved finite-regulator sequence; the common interacting
continuum state/observable identification remains unresolved.
The old Section 13 checkpoint and its 45-group diagnostic remain scoped
to that earlier result; the new calculation has its own complete source
and independent incidence/boundary diagnostic.
