# A radial state with a non-atomic low-energy scaling limit

8 September 2026. This note constructs an exact finite-regulator state
sequence for the unchanged open-box SU(2) Hamiltonian. Unlike the
fixed-\(\beta\) lowest-mode diagonal, whose mass collapses to a zero atom,
the radial parameter grows with the box. The raw spectral measures converge
to an explicit Gamma density supported down to zero. Every finite regulator
has positive coupling, the full Wilson potential, the actual positive
vacuum, and the exact physical projection.

## 1. The finite-regulator state

Use the operator, maximal-tree quotient, physical Hilbert space, actual
ground state \(\psi_{g,L,a}\), and chart observable of the companion proofs.
The original operator, with no Wilson term removed, is
\[
 H_{g,L,a}=\frac{2g^2}{a}\sum_{e\in E}
 \left(-\sum_{\alpha=1}^3X_{e,\alpha}^2\right)
 +\frac1{2g^2a}\sum_{p\in P}(2-\operatorname{tr}U_p),
 \qquad T_\alpha=-i\sigma_\alpha/2.
\]
Here \(E\) and \(P\) contain all positive edges and contained faces in the
open box with vertices \(\{-L,\ldots,L\}^3\), and the Hilbert measure is
product Haar restricted to all vertex-gauge-invariant functions. Its
unique positive unit vacuum and excitation energy are denoted by
\(\psi_{g,L,a}\) and \(\mathcal E_{g,L,a}\). The additive tree quotient
retains \(G=TT^*>0\), chord insertion \(\iota\), and face curl
\(C=d_1\iota\). Choose \(O\) with
\(O^{\mathsf T}G^{1/2}C^*CG^{1/2}O=\operatorname{diag}(\sigma_\nu^2)\).
These are the actual kinetic and curl tensors, not a substituted metric.
For integers \(j\ge2\), \(L_j=j^2\), \(a_j=1/(100j)\), choose a lowest physical oscillator mode
with
\[
 \sigma_j=\sqrt8\sin\frac{\pi}{4j^2+2},\qquad
 \beta_j=\sqrt j,\qquad \theta_j=\frac{\beta_j\sigma_j}{4}.
 \tag{1}
\]
For each fixed \(j\), use the companion's globally smooth chart-cutoff
multiplier
\[
 B_{g,j}(Z)=
 \exp\!\left(i\theta_j\chi(y)
 \left|(O^{\mathsf T}G^{-1/2}(y/g))_{\nu_j}\right|^2\right)
 \tag{2}
\]
in the logarithm chart and \(1\) outside it. It is invariant under the
residual simultaneous colour action. Define the actual centered vector and
its raw positive spectral measure:
\[
 v_{g,j}=(B_{g,j}-c_{g,j})\psi_{g,j},\quad
 c_{g,j}=\langle\psi_{g,j},B_{g,j}\psi_{g,j}\rangle,
\]
\[
 \nu_{g,j}(J)=
 \left\langle v_{g,j},
 \mathbf1_J(H_{g,j}-\mathcal E_{g,j})v_{g,j}\right\rangle .
 \tag{3}
\]
The cutoff \(\chi\) is real, smooth, invariant under simultaneous colour
rotations, equal to one near zero and supported strictly inside the
product logarithm chart. Thus (2) extends smoothly by one. Since \(O,G\)
act only on spatial chord indices, (2) is exactly gauge invariant. It has
modulus one, so the raw squared norm in (3) is \(1-|c_{g,j}|^2\).
The multiplier is nonconstant on an open set of the selected three
coordinates. Positivity of \(\psi_{g,j}\) and equality conditions in
Cauchy--Schwarz give \(|c_{g,j}|<1\); hence the vector is nonzero for
every \(g>0\). Subtracting \(c_{g,j}\) removes its entire vacuum component.
Its finite-regulator domain is smooth functions on the compact quotient,
contained in the domain of the full Hamiltonian.

The fixed-box theorem permits a strictly positive \(g_j<1/j\) matching the
actual raw measure to its comparison measure. Section 3 gives the exact
selection, without replacing a state by a unit-norm surrogate.

## 2. Exact comparison measure

The companion Laguerre calculation applies with \(k=3/2\) and
\(\beta=\beta_j\). Its raw comparison measure is
\[
 \nu_{0,j}=
 \sum_{n=1}^{\infty}
 \frac{(k)_n}{n!}
 \frac{\beta_j^{2n}}{(1+\beta_j^2)^{n+k}}\,
 \delta_{\,2n\sigma_j/a_j}.
 \tag{4}
\]
Its exact total mass is
\[
 d_j=1-(1+\beta_j^2)^{-k}
     =1-(j+1)^{-3/2}\longrightarrow1.                 \tag{5}
\]
The \(n=0\) term is absent because the state is vacuum-orthogonal; it is
not silently folded into the raw measure.

For \(t\ge0\), summing the negative-binomial series gives
\[
 L_j(t):=\int e^{-t\omega}\,d\nu_{0,j}(\omega)
 =
 \left[1+j\left(1-e^{-t\lambda_j}\right)\right]^{-k}
 -(j+1)^{-k},
 \quad \lambda_j=\frac{2\sigma_j}{a_j}.                 \tag{6}
\]
The physical spacing and frequency give
\[
 j\lambda_j
 =400\sqrt2\,j^2\sin\frac{\pi}{4j^2+2}
 \longrightarrow c:=100\sqrt2\,\pi .                  \tag{7}
\]
Hence, for each fixed \(t\),
\[
 L_j(t)\longrightarrow(1+ct)^{-3/2}.                  \tag{8}
\]
This is the Laplace transform of
\[
 d\gamma_c(\omega)=
 \frac{\omega^{1/2}e^{-\omega/c}}
 {\Gamma(3/2)c^{3/2}}\,d\omega,\qquad \omega\ge0.       \tag{9}
\]
Here is a direct quantitative proof of raw-measure convergence. Let \(Q\)
have density \(q^{k-1}e^{-q}/\Gamma(k)\) on \(q>0\), and, for each \(j\),
let \(N_j\), conditional on \(Q=q\), be Poisson with mean \(jq\).
Integration, with the original parameter \(j\) retained, gives
\[
 \begin{split}
 \mathbb P(N_j=n)
 &=\frac{j^n}{n!\Gamma(k)}
     \int_0^\infty q^{n+k-1}e^{-(j+1)q}\,dq\\
 &=\frac{(k)_n}{n!}\frac{j^n}{(j+1)^{n+k}} .
 \end{split}
\]
Consequently the law of \(\lambda_jN_j\) is exactly
\(\nu_{0,j}+(j+1)^{-k}\delta_0\). This is an auxiliary probability
coupling; the original state measure still excludes the zero coefficient.
Put \(c_j=j\lambda_j\). Conditional expectation makes the mixed term in
the following square vanish, and the Poisson conditional variance is
\(jQ\). Since \(\mathbb EQ=k\), \(\mathbb EQ^2=k(k+1)\),
\[
 \begin{split}
 \mathbb E|\lambda_jN_j-cQ|^2
 &=\mathbb E|c_j(N_j/j-Q)+(c_j-c)Q|^2\\
 &=\frac{kc_j^2}{j}+k(k+1)(c_j-c)^2 .
 \end{split}
\]
For \(x_j=\pi/(4j^2+2)\), the elementary inequalities
\(0\le x-\sin x\le x^3/6\) give the explicit retained-scale estimate
\[
 0<c-c_j\le
 \frac{c}{2j^2+1}
 +\frac{400\sqrt2\,\pi^3j^2}{6(4j^2+2)^3}.
\]
Indeed \(c-400\sqrt2j^2x_j=c/(2j^2+1)\). The sine inequality follows by
integrating \(1-\cos s\le s^2/2\), which itself follows by integrating
\(\sin u\le u\). Thus no asymptotic constant is left unspecified.

Define \(d_{\rm BL}\) on finite measures using all tests \(f\) with
\(\|f\|_\infty\le1\) and Lipschitz constant at most one. The coupling,
Cauchy--Schwarz, and the removed zero coefficient now prove
\[
 d_{\rm BL}(\nu_{0,j},\gamma_c)
 \le
 \left[\frac{kc_j^2}{j}+k(k+1)(c_j-c)^2\right]^{1/2}
 +(j+1)^{-k}\longrightarrow0 .
\]
The law of \(cQ\) is (9), by the explicit change of variable \(\omega=cq\).
This proves
\[
 \nu_{0,j}\Longrightarrow\gamma_c.                    \tag{10}
\]
In particular \(\gamma_c((0,\varepsilon))>0\) for every
\(\varepsilon>0\), while \(\gamma_c(\{0\})=0\).

## 3. Transport to the actual nonlinear Hamiltonian

For each fixed \(j\), the actual-vacuum and finite-spectral-projection
theorem for the full nonlinear Hamiltonian gives weak convergence of the
actual raw measure to (4) as \(g\downarrow0\), with total-mass convergence.
Choose \(0<g_j<1/j\) so that
\[
 d_{\mathrm{BL}}(\nu_{g_j,j},\nu_{0,j})<\frac1j,\qquad
 \left|\|v_{g_j,j}\|^2-d_j\right|<\frac1j.               \tag{11}
\]
For a definite selection let \(n_j\) be the least positive integer such
that \(g_j=2^{-n_j}\) satisfies these inequalities. Existence follows
because both inequalities hold at every sufficiently small positive
coupling for that fixed \(j\). This uses no volume-uniform estimate and
provides no explicit renormalized running-coupling formula. All coefficients
remain \(\kappa_j=200jg_j^2\), \(b_j=50j/g_j^2\),
\(\xi_j=1/(4g_j^4)\), including the scalar \(2b_j|P_j|\).
Combining (10), (11) and the explicit coupling estimate proves
\[
 \nu_{g_j,j}\Longrightarrow\gamma_c,\qquad
 \|v_{g_j,j}\|^2\longrightarrow1.                       \tag{12}
\]
The raw norm and raw amplitudes remain explicit; no state rescaling is
used in (11)--(13). Since the Gamma law has no endpoint
atoms, portmanteau gives
\[
 \lim_{j\to\infty}
 \nu_{g_j,j}((0,\varepsilon))
 =\gamma_c((0,\varepsilon))>0
 \qquad(\varepsilon>0).                                \tag{13}
\]
Every \(v_{g_j,j}\) is a nonzero smooth gauge-invariant vector orthogonal to
the actual finite-volume vacuum, and every \(g_j\) is strictly positive.
Thus (12)--(13) concern the full nonlinear Hamiltonian at every selected
positive coupling. The limiting comparison calculation does not assert
that interactions survive as nontrivial continuum dynamics.

For \(t>0\) and any nonnegative integer \(r\), the test
\(\omega^r e^{-t\omega}\) is bounded and continuous. Consequently the
actual correlations and all their derivatives at positive times converge:
\[
 \int\omega^r e^{-t\omega}\,d\nu_{g_j,j}
 \longrightarrow
 (k)_r c^r(1+ct)^{-k-r}.
\]
This does not assert convergence of unbounded energy moments at \(t=0\).

## 4. The cyclic Hilbert-space map determined by these states

Let \(\mathcal H_\gamma=L^2((0,\infty),\gamma_c)\),
\(v=1\), and \(M_\omega f=\omega f\) on
\(\{f:\int\omega^2|f|^2d\gamma_c<\infty\}\). Real multiplication on
this maximal domain is self-adjoint: its nonreal resolvent is the bounded
multiplier \((\omega-z)^{-1}\); testing the adjoint on compactly supported
functions gives the same maximal domain. Its spectral projections are
multiplication by indicators. In particular its vector \(v\) has exactly
the raw measure (9).

For finitely many coefficients \(a_\ell\) and times \(t_\ell\ge0\), put
\(A_j=H_{g_j,j}-\mathcal E_{g_j,j}\). Expanding the scalar products yields
\[
 \left\|\sum_\ell a_\ell e^{-t_\ell A_j}v_{g_j,j}\right\|^2
 \longrightarrow
 \int\left|\sum_\ell a_\ell e^{-t_\ell\omega}\right|^2d\gamma_c .
\]
This specifies an exact isometry from the limiting time-orbit Gram space
to \(\mathcal H_\gamma\). The image is dense: if \(h\) is orthogonal to
all exponentials, then the finite measure \(\overline h\,d\gamma_c\)
has zero Laplace transform. Push it by \(x=e^{-\omega}\) to \((0,1]\)
and extend it to \([0,1]\) with zero mass at zero. Testing integer times
shows all its polynomial moments vanish. Polynomials are uniformly dense
in continuous functions on \([0,1]\), so the measure is zero and \(h=0\).
The semigroup is intertwined with multiplication by \(e^{-t\omega}\);
the time and energy scales have not been changed.

Adding \(\mathbb C\Omega\) with energy zero retains the finite-vacuum
Gram vectors orthogonal to this cyclic sector. The resulting particular
spectral representation has a unique vacuum and positive spectrum down
to zero. It is not yet a representation of the continuum local gauge
observable algebra.

## 5. Exact scope

This proves a non-atomic low-energy scaling measure for one explicitly
selected sequence of finite nonlinear lattice Hamiltonians. It does not
yet prove that the varying Hilbert spaces reconstruct the prescribed
nontrivial Yang--Mills theory on \(\mathbb R^4\), or that this selected bare
coupling sequence has its renormalized physical scale. Those are additional
state-identification, reconstruction, and nontriviality maps. The result
supplied here is the exact state, raw measure, Gamma limit, and positive
mass in every interval \((0,\varepsilon)\); no free-field replacement is
used.

The subsequent full amplitude/time proof constructs the precise larger
representation containing these states. A nonzero carrier
\(b_0+\alpha/\sqrt j\) retains the kernel
\([1+cb_0^2t+i(\alpha-\delta)]^{-3/2}\), but also applying the common
modulation to the vacuum retains an entire additional zero-energy
origin fibre. The configuration-bridge proof further shows that on a
compatible selected diagonal the unchanged bounded local cylinder
algebra acts by scalars on the complete Gamma time orbit. Thus the
unique-vacuum statement for the restricted cyclic representation of
Section 4 must not be read as a unique-vacuum claim for the full
retained modulation algebra or for a local field theory.

## 6. Reproducibility and literature

The exact series coefficients and moment identities are algebraic checks;
the Gamma integral, sine estimate and convergence are proved analytically
above. The supplied checker separates exact symbolic identities from
floating-point illustrations; neither certifies the nonlinear companion
theorem. That theorem is proved in the included finite-box and state-map
companions, which are necessary proof inputs.

For the continuum target, A. Jaffe and E. Witten, *Quantum Yang--Mills
Theory*, Section 2, specifies a nontrivial four-dimensional quantum field
theory, not only an excitation operator and a cyclic vector
([Clay problem text](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf)).
S. Chatterjee, *Yang--Mills for probabilists*, Sections 3 and 6--7,
explains the continuum loop-observable construction and its scaling
([arXiv:1803.01950](https://arxiv.org/abs/1803.01950)).
Those works identify which additional mathematical structures must be
constructed; they are not invoked as premises establishing this limit.
