# Yang--Mills feedback: full local spectrum completed; retain the interaction next

9 September continuation: the full first coupling coefficients, cubic
singlet inverse, vacuum correction and six-dimensional first physical-gap
matrix are now explicitly calculated. The new bounded task is
WEB_PRO_FIRST_PHYSICAL_GAP_MATRIX_FEEDBACK_20260909.md, together with
cubic_singlet_vacuum_energy.md. The earlier request below is retained as
the preceding checkpoint, not an instruction to repeat completed work.

8 September 2026. This updates the earlier request to calculate the full
local-energy two-mode spectrum: that calculation is now complete. Do not
repeat only the oscillator spectrum or relabel it as an interacting
mass-gap counterexample.

## Exact retained objects

\[
 H_g=\frac{2g^2}{a}\sum_eE_e+\frac1{2g^2a}
                  \sum_p(2-\operatorname{tr}U_p),\qquad
 L_j=j^2,\quad a_j=\frac1{100j},\quad\ell_j=a_j(2j^2+1).
\]
All original edges, faces, SU(2) colour coordinates, gauge projection,
Haar measure, actual positive vacuum \(\psi_g\) and vacuum energy
\(\mathcal E_g\) are retained. Set \(A_g=H_g-\mathcal E_g\).
For \(h\in C_c^\infty(\mathbb R^3)\) put
\[
 h_e=h(am(e)),\quad h_p=\tfrac14\sum_{e\in\partial p}h_e,\quad
 D_{h,g}=\frac{2g^2}{a}\sum_eh_eE_e+
     \frac1{2g^2a}\sum_ph_p(2-\operatorname{tr}U_p),\quad
 \Xi_{h,g}=(D_{h,g}-\langle D_{h,g}\rangle_{\psi_g})\psi_g .
\]

## Completed all-mode calculation

With \(\widehat h(k)=\int e^{-ik\cdot x}h(x)\,dx\), the complete
open standing-wave, parity/sign and continuum calculation gives
\[
 \rho_h(\omega)=\frac1{320\pi^5}
          \int_{|k|\le\omega}|k|^4|\widehat h(k)|^2\,dk,\qquad
 C_h(t)=\frac1{320\pi^5t}
          \int |k|^4e^{-t|k|}|\widehat h(k)|^2\,dk.
\]
This is the covariance of the unprojected local-energy state at positive
Euclidean time. Both electric and magnetic pair terms are included;
opposite momenta cancel, exactly as \(D_1=H\) requires.
For \(H_h=\int h\ne0\),
\[
 \rho_h(\omega)\sim\frac{H_h^2}{560\pi^4}\omega^7,\quad
 C_h(t)\sim\frac{9H_h^2}{\pi^4t^8},\quad
 -C_h'(t)\sim\frac{72H_h^2}{\pi^4t^9}.
\]
The raw spectral measure has infinite total mass, but
\(e^{-t\omega}\rho_h(\omega)d\omega\) is finite with every moment
for each \(t>0\). No vector is divided by its norm.

All finite-edge covariance tests can be imposed on one positive dyadic
\(g_j\), using the proved fixed-box nonlinear graph convergence.
They give the same actual sequence for every compact smooth \(h\) and
every positive time. Its limiting state map is explicitly the
equal-colour two-creation map in transverse Fock space with Hamiltonian
\(d\Gamma(|p|)\). Thus this is a proved free spectral correspondence
from the specified nonlinear regulators, not an identified interacting
continuum theory.

The position kernel is now evaluated:
\[
 K_t(x)=\frac{9t^4-30t^2|x|^2+9|x|^4}
                    {\pi^4(t^2+|x|^2)^6}.
\]
It matches the 00,00 free-vector stress covariance with
\(C_T=12/\pi^4\), in Osborn--Petkou (1994), Eqs. (2.23),(5.16).
The joint measure is
\(|k|^4\mathbf1_{\{\omega\ge|k|\}}d\omega\,d^3k/(320\pi^5)\).
Its reflected two-point form is positive and its real-time
commutator expectation is supported on the light cone.
These assertions do not replace missing higher local products.

## What the global Gamma carrier does spatially

Keep its original amplitude \(\beta_j=\sqrt j\), mode phase
\(Q_{g,i}\), and centered state
\(v_j=(e^{i\sqrt jQ_{g,i}}-\langle e^{i\sqrt jQ_{g,i}}\rangle)\psi_g\).
Its total excitation mean tends to \(150\sqrt2\pi\).
The spatial measure of its local-energy expectations tends vaguely
to zero on fixed compact physical sets. Under the exact coordinate
pushforward \(\xi=x/\ell_j\), its measure instead tends to
\[
 150\sqrt2\pi
 [1-\cos(2\pi\xi_p)\cos(2\pi\xi_q)]
                 \mathbf1_{[-1/2,1/2]^3}\,d^3\xi,\quad p,q\ne i.
\]
This holds for the actual centered state on a further specified
finite-edge-test refinement. It is a spatial first-moment statement,
not a joint position/spectral measure. The full local spectrum above
uses the growing family of modes, not just this delocalized carrier.

## Exact finite-coupling response now available

At fixed \(L,a,g>0\), abbreviate \(K=\sum E_e,\ W=\sum(2-\operatorname{tr}U_p)\).
Keep
\[
 V_g=H_g'=\frac{4g}{a}K-\frac1{g^3a}W,\quad
 Z_{h,g}=D_{h,g}'=\frac{4g}{a}K_h-\frac1{g^3a}W_h,\quad
 v_g=\langle V_g\rangle_{\psi_g}.
\]
With \(R_g=A_g^{-1}\) on the vacuum complement and zero on the
vacuum, put \(\eta_g=R_g(V_g-v_g)\psi_g\). Then
\[
 \psi_g'=-\eta_g,\quad
 m_{h,g}'=\langle Z_{h,g}\rangle_{\psi_g}
                   -2\operatorname{Re}\langle\eta_g,D_{h,g}\psi_g\rangle,
\]
\[
 \Xi_{h,g}'=(Z_{h,g}-m_{h,g}')\psi_g
                          -(D_{h,g}-m_{h,g})\eta_g .
\]
The full response is
\[
 \partial_g C_{g;h}(t)=
 2\operatorname{Re}\langle\Xi_{h,g}',e^{-tA_g}\Xi_{h,g}\rangle
 -\int_0^t\langle\Xi_{h,g},e^{-(t-s)A_g}
                    (V_g-v_g)e^{-sA_g}\Xi_{h,g}\rangle\,ds .
\]
All domains and the unbounded Duhamel insertion are proved at fixed
regulator. The constant weight \(h_e=1\) makes both the state and
its derivative exactly zero, checking the vacuum-motion terms.
The actual difference from the full fixed-box comparison is the
improper integral of this derivative from zero to \(g\).

## One bounded demanding task

Calculate the first interaction-sensitive contribution to this complete
local covariance response, including the reduced-resolvent vacuum terms
and both Wilson/electric derivatives. Work from the full retained graph
operator and its native curl/mode tensors; do not replace it by a
homogeneous truncation. Give an explicit finite-mode sum or kernel and
its dependence on \(a,L,g,t\) for a fixed nonzero compact smooth profile,
then determine a regime where the remainder is actually bounded.

The useful output is an evaluated correction with its scale dependence,
not the statement that an unknown correction should be small. If a
nonuniform term appears, retain it and determine its spatial/momentum
map rather than selecting \(g\) so small that the term disappears.
Do not infer a full interacting construction or its gap from one
perturbative coefficient. The currently proved identities supply
the exact relation to be continued.

Complete proof sources in the canonical AI bundle:
FULL_LOCAL_SPECTRUM.md; local_energy_spacetime_and_coupling_response.md;
radial_carrier_spatial_energy_measure.md; the original finite-box,
graph, state, and complete quantum-blocking companions.
