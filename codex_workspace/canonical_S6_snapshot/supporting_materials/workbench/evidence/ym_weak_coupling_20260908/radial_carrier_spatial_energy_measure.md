# Where the radial carrier's finite energy is located

8 September 2026.

The radial carrier has a nonzero limiting energy and a Gamma spectral
law. The full compact local-energy observable has an exact relation to
that carrier, not merely a comparison of their names or dimensions.
This note calculates its spatial distribution. The energy is spread
over a box whose physical side length tends to infinity. Every fixed
compact region receives vanishing carrier energy, while the original
box-scale coordinate \(x/\ell_j\) carries an explicit nonzero limiting
density. Both the uncentered unit phase state and the original
vacuum-orthogonal centered state are retained.

## 1. Original model and observable

Use the original open box, Haar measure, full gauge-invariant Hilbert
space, and
\[
 H_g=\kappa K+bW,\quad \kappa=\frac{2g^2}{a},\
 b=\frac1{2g^2a},\quad
 K=\sum_eE_e,\quad W=\sum_p(2-\operatorname{tr}U_p).
 \tag{1}
\]
The letter \(b\) here is the original Wilson coefficient, not a radial
carrier amplitude. Let \(\psi_g>0\) be the actual unit vacuum and
\(A_g=H_g-\mathcal E_g\). For real edge weights \(f\), put
\[
 f_p=\tfrac14\sum_{e\in\partial p}f_e,\quad
 D_f=\kappa\sum_ef_eE_e+b\sum_pf_p(2-\operatorname{tr}U_p),
 \quad C_f=D_f-\langle\psi_g,D_f\psi_g\rangle .
 \tag{2}
\]
All faces adjacent to a weighted edge occur, with their original
quarter coefficients. For constant \(f=1\), \(C_1=A_g\).

Choose one of the three specified lowest transverse modes, denoted
\(i\in\{1,2,3\}\) by its normal plane. Its actual smooth
gauge-invariant cutoff phase is \(Q_{g,i}\), exactly the quadratic
chart multiplier of the radial companion. Define
\[
 B_g(\beta)=e^{i\beta Q_{g,i}},\quad
 \phi_g(\beta)=B_g(\beta)\psi_g,\quad
 m_g(\beta)=\langle\psi_g,B_g(\beta)\psi_g\rangle,\quad
 v_g(\beta)=(B_g(\beta)-m_g(\beta))\psi_g .
 \tag{3}
\]
There is no rescaling by \(\|v_g\|\).
The unit phase state has norm one; \(v_g\perp\psi_g\).

## 2. Exact positive local energy measure at finite coupling

On the common smooth physical core,
\[
 R_{g,i;f}:=\tfrac12[Q_{g,i},[D_f,Q_{g,i}]]
           =\kappa\sum_{e,\alpha}f_e(X_{e,\alpha}Q_{g,i})^2 .
 \tag{4}
\]
The Wilson multiplication commutes with the phase exactly. Applying
the product rule to each electric square, including the first
commutator, gives
\[
 B_g(\beta)^*D_fB_g(\beta)
 =D_f+i\beta[D_f,Q_{g,i}]+\beta^2R_{g,i;f}.
 \tag{5}
\]
Its vacuum expectation of the linear term is zero. In fact
\(\psi_g,D_f\psi_g,Q_{g,i}\psi_g\) are real, and symmetry gives
\(\langle\psi_g,[D_f,Q_{g,i}]\psi_g\rangle=0\).
Consequently
\[
 \boxed{\langle\phi_g(\beta),C_f\phi_g(\beta)\rangle
           =\beta^2\langle\psi_g,R_{g,i;f}\psi_g\rangle .}
 \tag{6}
\]
This is an exact identity in the full nonlinear model, not a
removal of the magnetic energy from its Hamiltonian.

With original edge midpoints \(am(e)\), define the positive finite
measure
\[
 \mu_{g,\beta}=\beta^2\kappa\sum_e
       \left(\sum_\alpha\int\psi_g^2
                     (X_{e,\alpha}Q_{g,i})^2\,dU\right)
                       \delta_{am(e)} .
 \tag{7}
\]
For \(f_e=h(am(e))\), equation (6) is exactly
\(\langle\phi_g,C_f\phi_g\rangle=\int h\,d\mu_{g,\beta}\).
Every coefficient in (7) is nonnegative. Its total mass is
\(\langle\phi_g,A_g\phi_g\rangle
 =\langle v_g,A_gv_g\rangle\), since the vacuum subtraction in
(3) has zero excitation form.

For the centered state define instead the signed finite measure
\[
 \widetilde\mu_{g,\beta}
     =\sum_e\langle v_g(\beta),C_{\mathbf1_e}v_g(\beta)\rangle
                                                  \delta_{am(e)} .
 \tag{8}
\]
The local operator \(C_{\mathbf1_e}\) includes its adjacent
quarter-weight faces. Linearity proves that (8) integrates any
edge-sampled \(h\) to \(\langle v_g,C_fv_g\rangle\), and its
total mass agrees with that of (7). No local positivity of (8)
is assumed.

## 3. Full comparison coefficients and the centered correction

At a fixed box write \(V_i\) for the original counting-unit transverse
edge cochain and \(Y_i=d_1V_i/\sigma\) for its counting-unit curl.
For every edge weight set
\[
 A_i^f=\sum_ef_eV_i(e)^2,\qquad
 F_i^f=\sum_pf_pY_i(p)^2,\qquad
 \lambda=\frac{2\sigma}{a},\quad k=\frac32 .
 \tag{9}
\]
The fixed-box weighted phase-gradient proof in the compact/radial
companion gives
\[
 \langle\psi_g,R_{g,i;f}\psi_g\rangle
                       \longrightarrow k\lambda A_i^f .
 \tag{10}
\]
It retains the cutoff derivatives and controls them by the complete
vacuum moment and chart-tail estimates, rather than discarding the
cutoff outside a formal oscillator calculation.

The centered local correction can also be evaluated exactly in that
comparison. Put \(q=\sigma|z_i|^2/4\). Its vacuum density is
\(q^{k-1}e^{-q}/\Gamma(k)\), so
\[
 m_0(\beta)=(1-i\beta)^{-k}.
 \tag{11}
\]
Only the pair with both modes equal to \(i\) contributes to
\(\langle C_f\Phi_0,e^{i\beta q}\Phi_0\rangle\).
The exact pair coefficient is
\(\sigma(F_i^f-A_i^f)/(4a)\), and its creation vector is
\((2q-2k)\Phi_0\). Direct Gamma integration therefore gives
\[
 \langle\Phi_0,C_f e^{i\beta q}\Phi_0\rangle
 =\frac{ik\beta\sigma}{2a}(F_i^f-A_i^f)
                                      (1-i\beta)^{-k-1}.
 \tag{12}
\]
For example the integral used is
\(2k[(1-i\beta)^{-k-1}-(1-i\beta)^{-k}]\).
This fixes the sign and the factor two.
Expanding both vacuum subtractions in (3), using (6),(10), and
taking the real part of (12), proves the full formula
\[
 \boxed{\langle v_0(\beta),C_fv_0(\beta)\rangle
   =k\lambda\beta^2 A_i^f+
       \frac{k\sigma\beta^2}{a}
          (1+\beta^2)^{-k-1}(F_i^f-A_i^f).}
 \tag{13}
\]
In taking the real part,
\(\operatorname{Re}\{i\beta/(1-i\beta)\}
 =-\beta^2/(1+\beta^2)\).
The sign of the extra term in (13) is thus positive times
\(F_i^f-A_i^f\). This term would be missed by identifying the
centered and uncentered configuration measures.

For \(f=1\), \(F_i^1=A_i^1=1\), so the correction vanishes.
For the single-edge weights, both
\(A_i^{\mathbf1_e}\) and \(F_i^{\mathbf1_e}\) are nonnegative and
their sums over all edges are one. Hence the total variation of
the comparison centered correction is at most
\[
 k\lambda\beta^2(1+\beta^2)^{-k-1}.
 \tag{14}
\]
This inequality retains every edge and the quarter-face averages.

## 4. A common actual positive-coupling refinement

Take the original sequence
\[
 L_j=j^2,\quad a_j=\frac1{100j},\quad N_j=2j^2+1,\quad
 \ell_j=a_jN_j,\quad
 \sigma_j=\sqrt8\sin\frac{\pi}{2N_j},\quad
 \beta_j=\sqrt j,\quad c_\Gamma=100\sqrt2\pi .
 \tag{15}
\]
Then \(j\lambda_j\to c_\Gamma\) and \(\ell_j/j\to1/50\).
The original carrier amplitude, coordinates and physical time
have not changed.

At each stage \(j\), add to the finite union of the previous
kernel, weighted-moment and local-energy tests the following
tests for every original edge: the expectations
\(\langle\phi_g(\beta_j),C_{\mathbf1_e}\phi_g(\beta_j)\rangle\)
and \(\langle v_g(\beta_j),C_{\mathbf1_e}v_g(\beta_j)\rangle\)
differ from their complete fixed-box values (6),(10),(13) by
less than \(j^{-10}/|\mathsf E_{L_j}|\).
All these are finitely many scalar tests.

For the uncentered term, (6) and the proved weighted gradient
convergence (10) establish convergence at this fixed \(j,\beta_j\).
For the centered correction, the graph convergence
\(C_{\mathbf1_e}\psi_g\to C_{\mathbf1_e,0}\Phi_0\)
and the bounded phase-vacuum convergence prove convergence of
the two mixed matrix elements in its exact expansion.
The vacuum multiplier expectation converges as well. Thus the
additional finite list holds for every sufficiently small
positive \(g\).

Choose the least positive dyadic exponent satisfying this union
and the earlier positive-coupling bound. This defines an actual
refinement \(g_j^\sharp\), not a claim that a previously selected
least exponent already satisfies new tests.
The total variation distances between (7),(8) and their respective
comparison edge measures are at most \(j^{-10}\).
This gives one sequence for every bounded edge weight at stage
\(j\), with error at most \(j^{-10}\|f\|_\infty\).
In particular it covers both fixed physical profiles and the
expanding profiles below without a separate coupling choice.

## 5. Vanishing energy in fixed compact physical regions

For \(h\in C_c(\mathbb R^3)\), write \(p,q\) for the two spatial
directions other than \(i\), and define
\[
 M_{h,i}=\int_{\mathbb R^3}(x_p^2+x_q^2)h(x)\,dx .
 \tag{16}
\]
The original lowest cochain components have squares
\[
 \frac2{N_j^3}
 \cos^2\frac{\pi a_j(n_p+1/2)}{\ell_j}
 \sin^2\frac{\pi a_j n_q}{\ell_j},\qquad
 \frac2{N_j^3}
 \sin^2\frac{\pi a_j n_p}{\ell_j}
 \cos^2\frac{\pi a_j(n_q+1/2)}{\ell_j}.
 \tag{17}
\]
The remaining coordinate is the unit constant vertex factor.
The original midpoint/vertex positions in (17) are retained.
On a fixed compact set,
\(\ell_j\sin(\pi x/\ell_j)\to\pi x\) and
\(\cos(\pi x/\ell_j)\to1\), uniformly.
Multiplication by the original spacing volume \(a_j^3\) in the
shifted Riemann sums therefore proves
\[
 \ell_j^5 A_i^{h,j}\longrightarrow2\pi^2M_{h,i}.
 \tag{18}
\]
This argument uses the modulus of continuity of \(h\), an enlarged
compact support for face weights, and a uniform bound on the
number of sampled cells times \(a_j^3\).
The companion's exact curl squares also give
\(F_i^{h,j}=O_h(\ell_j^{-3})\).

Combining (6),(10),(15),(18) and the total-variation error gives
\[
 \boxed{\ell_j^5\int h\,d\mu_{g_j^\sharp,\sqrt j}
             \longrightarrow300\sqrt2\pi^3M_{h,i}.}
 \tag{19}
\]
For the centered correction in (13),
\(\sigma_j/a_j=O(\ell_j^{-1})\) and
\(j(1+j)^{-k-1}=O(j^{-3/2})\). Its compact-profile size is
therefore \(O_h(\ell_j^{-4}j^{-3/2})\). Multiplication by
\(\ell_j^5\) makes it tend to zero because
\(\ell_j j^{-3/2}\to0\). The error \(j^{-10}\ell_j^5\)
also tends to zero. Thus (19) holds for
\(\widetilde\mu_{g_j^\sharp,\sqrt j}\) as well.

In particular both measures converge vaguely to zero on fixed
compact physical sets. Their total masses instead converge to
\[
 kc_\Gamma=150\sqrt2\pi>0 .
 \tag{20}
\]
For the positive measures (7), the mass outside every fixed
compact set tends to this total mass. This follows by choosing
a compactly supported continuous majorant of the set and applying
(19). It is not a conclusion drawn merely from a zero low-band
projection.

## 6. Exact box-scale coordinate map and retained limiting density

Define the coordinate pushforward \(s_j(x)=x/\ell_j\).
It is invertible on \(\mathbb R^3\), with inverse
\(s_j^{-1}(\xi)=\ell_j\xi\). Apply it to the actual measures;
no state or measure is divided by its mass.
The finite support is the original midpoint box divided by
\(\ell_j\); its endpoints tend to \([-1/2,1/2]^3\).

For continuous \(h\) on a neighbourhood of this cube, the same
cochain formula (17) is now an ordinary counting Riemann sum
with mesh \(1/N_j\). It proves
\[
 \sum_e h(am(e)/\ell_j)V_i(e)^2
 \longrightarrow\int_{[-1/2,1/2]^3}h(\xi)\rho_i(\xi)\,d\xi,
 \tag{21}
\]
where
\[
 \boxed{\rho_i(\xi)=
 2\{\cos^2(\pi\xi_p)\sin^2(\pi\xi_q)
       +\sin^2(\pi\xi_p)\cos^2(\pi\xi_q)\}
 =1-\cos(2\pi\xi_p)\cos(2\pi\xi_q).}
 \tag{22}
\]
The constant coordinate \(i\) has length one in this cube.
Each sine-square and cosine-square integral on
\([-1/2,1/2]\) is \(1/2\), so \(\int\rho_i=1\).
This value follows from the original counting-unit cochain, not
from a new normalization of the energy measure.

The total-variation bound (14) tends to zero because
\(j\lambda_j\) stays bounded and \((1+j)^{-5/2}\to0\).
The actual edge-test errors vanish as well. Equations
(10),(15),(21) therefore prove the two weak finite-measure limits
\[
 \boxed{(s_j)_*\mu_{g_j^\sharp,\sqrt j},\
        (s_j)_*\widetilde\mu_{g_j^\sharp,\sqrt j}
 \ \Longrightarrow\
 150\sqrt2\pi\,\rho_i(\xi)
                    \mathbf1_{[-1/2,1/2]^3}\,d^3\xi .}
 \tag{23}
\]
For the signed centered measures weak convergence follows from
their vanishing total-variation distance to the positive comparison
measure. Equations (19),(20),(23) specify both spatial scales
exactly. The limiting Gamma energy is not concentrated at a
point of the original physical space; its nonzero density is
visible on the growing box scale.

## 7. Consequence for the local spectral programme

The spatial measures (7),(8) encode local-energy expectations,
that is, spatially resolved first moments. They are not a joint
positive measure of position and spectral energy, and (23) does
not identify such a measure with the Gamma spectral law. Local
energies and the full Hamiltonian need not commute. Both
distributions have been calculated at their stated levels.

The full compact local-energy spectrum proved in the companion
uses a growing family of transverse modes and retains nonzero
positive-time norms. Equations (19)--(23) instead evaluate the
energy of one specified global radial carrier with its increasing
occupation. They are two computations within the same original
local energy and phase-gradient identities, not claims that the
two sectors are unrelated.

This spatial measure calculation rules out interpreting the
carrier's finite total energy as a nonzero limiting energy
localized in a fixed compact region, on this specified sequence.
It does not rule out other states, mixed local excitations, or
another retained-coupling continuum trajectory. The full local
products and the nonlinear coupling-response integral are the
remaining concrete routes to test that larger construction.

The proof inputs are the included *Compact local energy, radial
electric observables, and a full-mode low-energy lower bound*
(weighted phase-gradient convergence and original cochain squares),
*Spatial continuum*, Sections 22--23 (actual radial moment tails
and common-mode maps), and the complete full-mode local-spectrum
companion. All formulas above concern the original finite
Hamiltonian and its proved fixed-box maps; no outside fluid or
Yang--Mills existence theorem is assumed here.
