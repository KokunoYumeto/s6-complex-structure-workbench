# Full positive-time spectrum of the original direction-one local electric state

8 September 2026. This proof retains the original Hamiltonian, actual
positive vacuum, direction-one link Casimirs, physical spacing, open
endpoints, and three colour components. The observable in this note is
electric only. The magnetic potential remains in the Hamiltonian and
in its actual vacuum. It is not added to the observable.

Proof inputs read in full are Section 18 of spatial_continuum.md and
sources/full_local_spectrum_inputs/FULL_LOCAL_SPECTRUM.md, whose
SHA-256 at reading was
49d17d1e19880a0416a1cbb4460ac0f43460caea476b0e058bd01371a1f513dc.
The needed weighted-vacuum and finite-projection proofs are retained in
Section 17 of the cumulative manuscript. The calculation below derives
the different directional electric coefficient, its plane-wave
polarization factor, complete density and actual positive-coupling
transport. It makes no substitution of a compact profile for the
original unbounded all-box weight \(n_2^2\).

## 1. Exact original objects and fixed-box graph map

For \(L\ge2\), the original vertices are
\(\{-L,\ldots,L\}^3\), with every contained positive edge and face.
For \(a,g>0\), write
\[
 H_{L,a,g}=\kappa\sum_eE_e+bW,\qquad
 E_e=-\sum_{\alpha=1}^3X_{e,\alpha}^2,\qquad
 W=\sum_p(2-\operatorname{tr}U_p),\qquad
 \kappa=\frac{2g^2}{a},\quad b=\frac1{2g^2a}.
 \tag{1}
\]
Here \(T_\alpha=-i\sigma_\alpha/2\) and the \(X_{e,\alpha}\)
are the original link derivatives. The full Wilson scalar is
included in \(bW\). The actual positive unit physical vacuum is
\(\psi_{L,a,g}\), with actual energy \(\mathcal E_{L,a,g}\);
put \(A_g=H_{L,a,g}-\mathcal E_{L,a,g}\ge0\).
The original vertex gauge law and its inverse-parameter
presentation have the same invariant Hilbert subspace.

Fix real \(h\in C_c^\infty(\mathbb R^3)\) and define
\[
 f_{h,L,a}(n,i)=\mathbf1_{\{i=1\}}h(a(n+\mathbf e_1/2)),\qquad
 \Gamma_h=\sum_{e\parallel1}h(am(e))E_e,
 \tag{2}
\]
\[
 D^E_h=\kappa\Gamma_h,\qquad
 \Xi^E_{h,g}=(D^E_h-\langle\psi_g,D^E_h\psi_g\rangle)\psi_g.
 \tag{3}
\]
All sums use the original finite edge set, including the boundary.
There is no face-average term in \(D^E_h\). For signed weights, the
joint Peter--Weyl decomposition realizes \(\Gamma_h\) as the real
multiplier \(\sum_e f_h(e)j_e(j_e+1)\), on the domain defined by
the squares of those eigenvalues. This gives its self-adjoint
realization; smooth functions lie in its domain. The actual vacuum
is smooth, so (3) is smooth, physical, exactly vacuum-orthogonal,
and in every power domain of the full \(H\).

Retain the exact additive tree-to-chord map \(T\), with
\(G=TT^*>0\), the chord insertion \(\iota\), and the original
oriented curl \(C=d_1\iota\). If
\[
 O^*G^{1/2}C^*CG^{1/2}O=\Sigma^2,\qquad
 \Sigma=\operatorname{diag}(\sigma_\nu),\qquad
 V_\nu=T^*G^{-1/2}Oe_\nu,
 \tag{4}
\]
then the \(V_\nu\) are a real orthonormal transverse edge basis.
Set
\[
 D^h_{\nu\eta}=\sum_{e\parallel1}h(am(e))V_\nu(e)V_\eta(e),
 \qquad \omega_\nu=\frac{\sigma_\nu}{a}.
 \tag{5}
\]
No kinetic metric or counting inner product has changed.

The exact Haar/log map on based chord functions is
\[
 (\mathcal B_gF)(x)
 =g^{3r/2}\mathcal J(gx)^{1/2}F(\exp(gx))
 \quad(x\in\Omega_g),\qquad
 \Omega_g=\{x:|x_c|<2\pi/g\},
 \tag{6}
\]
and is zero outside \(\Omega_g\), with
\(\mathcal J(y)=(16\pi^2)^{-r}
\prod_c[\sin(|y_c|/2)/(|y_c|/2)]^2\).
The kinetic-coordinate unitary is
\[
 f(x)\longmapsto(\det G)^{3/4}f(G^{1/2}Oz).
 \tag{7}
\]
We include both (6) and (7) whenever comparison vectors are written
in \(z\) coordinates, and denote their composition by
\(\mathcal C_g\). These are isometries with their exact image
domains; neither identifies the finite-\(g\) vacuum with a trial
Gaussian.

Here is the Section 17 graph argument needed for (3). Its actual
vacuum moment calculation gives
\[
 \begin{gathered}
 \int W^n\psi_g^2\,dU\le B_ng^{2n},\qquad
 B_0=1,\quad B_1=2aK,\\
 B_{n+1}=2aKB_n+16n^2B_{n-1}\quad(n\ge1),\qquad
 K=3\sqrt{N_EM_F}/a .
 \end{gathered}
 \tag{8}
\]
where \(N_E,M_F\) are the original edge and face counts. It follows
from the full ground-state equation, the bound
\(\sum_{e,\alpha}|X_{e,\alpha}W|^2\le16W\), and the
ground-state form identity. At fixed box the potential has its
unique zero at the identity chords, with
\(W(y)\ge c|y|^2\) locally and \(W\ge c_\rho>0\) outside that
neighborhood. The third scaled moment in (8) controls the squared
tail of \((W/g^2)\psi_g\) by
\(B_3/(cR^2)+g^2B_3/c_\rho\).
The full Taylor coefficient and strong actual-vacuum convergence
therefore give
\[
 \mathcal B_g((W/g^2)\psi_g)
 \longrightarrow \tfrac14\sum_\alpha\|Cx^\alpha\|^2\Phi_0.
 \tag{9}
\]
The unchanged eigen-equation is
\[
 g^2\sum_eE_e\psi_g
 =\frac{a\mathcal E_g}{2}\psi_g-\frac{W}{4g^2}\psi_g.
 \tag{10}
\]
Together with (9), it proves convergence in the total electric
graph. Since the separate positive link Casimirs strongly commute,
\[
 \|\Gamma_hF\|\le\|f_h\|_\infty\|\textstyle\sum_eE_eF\|.
 \tag{11}
\]
Apply (11) to the difference between the actual vacuum and the
inverse image of a compact invariant cutoff times its limiting
Gaussian. On that compact chart the exact differentiated
coefficients converge. Let the cutoff radius tend to infinity
using the Gaussian graph norm. This proves the arbitrary signed
weight graph limit, with all constants fixed before \(g\to0\):
\[
 \mathcal C_g(g^2\Gamma_h\psi_g)
 \longrightarrow
 -\sum_{\nu,\eta,\alpha}D^h_{\nu\eta}
          \partial_{z_\nu^\alpha}\partial_{z_\eta^\alpha}\Phi_0.
 \tag{12}
\]
It uses the full potential moments, rather than inferring
unbounded operator convergence from vacuum norm convergence.

Use the original creation operators and variance,
\[
 \partial_{z_\nu^\alpha}
 =\sqrt{\sigma_\nu/8}\,(a_{\nu\alpha}-a_{\nu\alpha}^\dagger),
 \quad
 z_\nu^\alpha=\sqrt{2/\sigma_\nu}
                    (a_{\nu\alpha}+a_{\nu\alpha}^\dagger),
 \quad
 A_0=\sum_{\nu,\alpha}\omega_\nu
                      a_{\nu\alpha}^\dagger a_{\nu\alpha}.
 \tag{13}
\]
Subtracting the expectation in (12) removes its scalar term.
Since \(\kappa/g^2=2/a\), the exact fixed-box vector limit is
\[
 \boxed{\mathcal C_g\Xi^E_{h,g}\longrightarrow
 X^E_{h,0}
 =-\frac14\sum_{\nu,\eta,\alpha}
     \sqrt{\omega_\nu\omega_\eta}\,D^h_{\nu\eta}
          a_{\nu\alpha}^\dagger a_{\eta\alpha}^\dagger\Phi_0.}
 \tag{14}
\]
The sign is negative. Indeed
\((a_\nu-a_\nu^\dagger)(a_\eta-a_\eta^\dagger)\Phi_0
=-\delta_{\nu\eta}\Phi_0+
a_\nu^\dagger a_\eta^\dagger\Phi_0\), and the electric
operator has the preceding minus sign.

Define the real symmetric pair matrix
\[
 B^{E,L,a}_{h;\nu\eta}
 =-\sqrt{\omega_\nu\omega_\eta}
       \sum_{e\parallel1}h(am(e))V_\nu(e)V_\eta(e).
 \tag{15}
\]
There are three equal-colour contractions. The norm of a
symmetric two-creation kernel is twice its squared Hilbert--Schmidt
norm: commuting its two annihilators through the two creators
gives the two ordered contractions. Consequently the complete
fixed-box raw measure is
\[
 \boxed{\nu^{E,L,a}_{h,0}
 =\frac38\sum_{\nu,\eta}|B^{E,L,a}_{h;\nu\eta}|^2
          \delta_{\omega_\nu+\omega_\eta}.}
 \tag{16}
\]
The sum is ordered, including both occurrences of distinct modes.
The coefficient is exactly \(3\cdot2/4^2=3/8\).
The strong vector theorem (14), convergence of all finite physical
spectral projections and energies, and convergence of the total
vector norms prove weak convergence of actual finite measures to
(16) at fixed box. A finite comparison spectral cutoff contains
all but a chosen tail of the comparison vector; projection and
norm convergence give the same bound for the actual vector.
Within it, only finitely many clusters occur and their projections
and energies converge. This proves all bounded continuous tests.

## 2. Every open-box mode and the directional parity calculation

Put \(N=2L+1\) and \(\ell=aN\). The physical endpoints are
still \(\pm aL\). On vertices and positive edges respectively use
\[
 v_j(n)=\sqrt{\frac{2-\delta_{j0}}N}
       \cos\frac{\pi j(n+L+1/2)}N,\quad
 s_j=2\sin\frac{\pi j}{2N},\quad 0\le j<N,
 \tag{17}
\]
\[
 w_j(n)=-\sqrt{\frac2N}
       \sin\frac{\pi j(n+L+1)}N,\qquad j>0.
 \tag{18}
\]
There is no \(w_0\). Finite geometric sums give orthonormality
on the unchanged vertex and edge ranges. Direct differencing
gives \(d_0v_j=s_jw_j\), and transposition gives
\(d_0^*w_j=s_jv_j\).

For \(\boldsymbol j=(j_1,j_2,j_3)\), let
\(I=\{i:j_i>0\}\) and \(s=(s_{j_1},s_{j_2},s_{j_3})\).
Each real unit \(\epsilon\in\mathbb R^I\) with
\(s\cdot\epsilon=0\) gives
\[
 V_{\boldsymbol j,\epsilon}(n,i)
 =\epsilon_iw_{j_i}(n_i)\prod_{d\ne i}v_{j_d}(n_d),
 \qquad \sigma=|s|.
 \tag{19}
\]
There are \(|I|-1\) polarizations for \(|I|\ge2\) and none
otherwise. The tensor one-form space at this index is
\(\mathbb R^I\); its gradient line is \(\mathbb Rs\).
The exact curl squared form is
\(|s|^2|\epsilon|^2-|s\cdot\epsilon|^2\).
Thus its transverse complement is exactly (19), proving
completeness and the original frequencies. Orthogonal changes
inside eigenspaces give the same ordered spectral sum (16).

Each mode component is bounded by \(2\sqrt2N^{-3/2}\).
Choose \(R_h\) so that a fixed unit neighborhood of the support
of \(h\) lies in \([-R_h,R_h]^3\). For \(a\le1\), the
number of direction-one edge samples meeting this support is at
most \((2R_h/a+3)^3\). Thus (15) satisfies the global bound
\[
 |B^{E,L,a}_{h;\nu\eta}|
 \le K_h\ell^{-3}\sqrt{\omega_\nu\omega_\eta},\qquad
 K_h=8(2R_h+3)^3\|h\|_\infty .
 \tag{20}
\]
This constant does not depend on \(L,a\) once the box contains
the fixed neighborhood. Every edge sample and zero weight remains
in the original sum.

The sine bounds give
\[
 \frac{2|\boldsymbol j|}{\ell}
      \le\omega_{\boldsymbol j}
      \le\frac{\pi|\boldsymbol j|}{\ell}.
 \tag{21}
\]
For \(\ell\ge1\) and each \(u>0\), grouping triples in
shells \(m\le|\boldsymbol j|<m+1\) proves
\[
 \ell^{-3}\sum_\nu\omega_\nu e^{-u\omega_\nu}\le C_u.
 \tag{22}
\]
The shell has at most \(C(m+1)^2\) triples, and each has at
most two polarizations. One justification for this shell count
is to surround each nonnegative integer triple by its disjoint
unit cube: their union lies between spheres whose radii differ
by a fixed constant. Their volume difference is bounded by
\(C(m+1)^2\). The resulting series is bounded by a constant
times \(\ell^{-4}\sum_{m\ge1}(m+1)^3e^{-2um/\ell}\);
integral comparison bounds it uniformly for \(\ell\ge1\).

Combining (20),(22), the contribution of
\(\omega_\nu+\omega_\eta>R\) to (16) after multiplication
by \(e^{-t(\omega_\nu+\omega_\eta)}\) is at most
\(C_{h,t}e^{-tR/2}\), uniformly in the regulators.
Every fixed additional power of the pair energy is handled by
using a smaller positive time. The same shell proof gives
\[
 \limsup_{\ell\to\infty}\ell^{-3}
       \sum_{\omega_\nu<\varepsilon}\omega_\nu
       \le C\varepsilon^4.
 \tag{23}
\]
In a bounded frequency region the triples with a zero coordinate
number \(O_R(\ell^2)\), so their paired contribution is
\(O_{h,R}(\ell^{-1})\). Strips of width \(\delta\) adjoining
a coordinate plane have limiting contribution \(O_{h,R}(\delta)\).
These bounds justify retaining a bounded momentum region away
from its coordinate planes and zero before taking its Riemann
sum, then removing these restrictions.

For positive index coordinates set
\(k_i=\pi j_i/\ell\), \(\beta_i=j_i\bmod2\) and
\(\chi_{\boldsymbol j}=(-1)^{\sum_i\lfloor j_i/2\rfloor}\).
At the physical location of each mode component the exact
standing-wave identity is
\[
 \ell^{3/2}a^{-3/2}V_{\boldsymbol j,\epsilon}(x)
 =\chi_{\boldsymbol j}\sum_{\rho\in\{-1,1\}^3}
       U_{\beta\rho}\epsilon^\rho e^{i(\rho k)\cdot x},
 \quad
 U_{\beta\rho}=\frac{i}{\sqrt8}e^{i\pi\rho\cdot\beta/2},
 \quad \epsilon_i^\rho=\rho_i\epsilon_i.
 \tag{24}
\]
The common \(x\) denotes the component expressions restricted
to their original edge positions in the sum. No sample is moved.
Expand each cosine and negative sine in (17)--(19) to verify
(24); the differentiated component contributes \(i\rho_i\)
relative to the two undifferentiated components. Also
\[
 \sum_{\beta\in\{0,1\}^3}
 e^{i\pi(\rho-\rho')\cdot\beta/2}
 =8\mathbf1_{\{\rho=\rho'\}},
 \tag{25}
\]
so the eight-by-eight matrix \(U\) is unitary.

On bounded frequencies, \(s/a\to k\) uniformly. The directional
edge sum in (15) is a Riemann sum for the product of the two
direction-one components and \(h\); smoothness and compact
support bound its sample error by \(O_{h,R}(a)\) after its
volume factor. There are \(O_R(\ell^6)\) mode pairs, and the
coefficient error is \(o(1)\ell^{-3}\) per pair. Equation (20)
therefore bounds the error in the squared sum by \(o(1)\).
One may sum polarizations using \(I-kk^*/|k|^2\), avoiding
any singular choice of frame; local continuous polarization
frames on the retained compact sets give the same statement.

For each fixed parity the momentum grid has step \(2\pi/\ell\).
Align its eight parity grids with one grid; their shifts are at
most \(\pi/\ell\) in each coordinate and compact-set uniform
continuity makes the change tend to zero. Equation (25), applied
to both mode indices, then turns the two standing-wave parity
sums into the Hilbert--Schmidt sum over the two momentum signs.
The signed factors \(\chi_{\boldsymbol j}\) cancel in the
modulus squared, not in the original individual modes.
The two grid densities and the squared coefficient give precisely
\(\ell^{-6}(\ell/(2\pi))^6=(2\pi)^{-6}\).
Their sign grids exhaust momentum space after removing only
the controlled coordinate strips.

For any measurable real transverse polarization frames
\(e_r(p)\), the resulting plane-wave coefficient is
\[
 \boxed{
 \mathcal R^{E,rs}_h(p,q)
 =-\frac{\widehat h(-p-q)}{(2\pi)^3}
       \sqrt{|p||q|}\,(e_r(p))_1(e_s(q))_1,\qquad
 \widehat h(k)=\int_{\mathbb R^3}e^{-ik\cdot x}h(x)\,dx .
 }
 \tag{26}
\]
The minus sign is the electric pair sign in (14).
Polarization completeness yields exactly
\[
 \sum_r(e_r(p))_1^2=1-\frac{p_1^2}{|p|^2},\qquad
 \sum_{r,s}|(e_r(p))_1(e_s(q))_1|^2
 =\left(1-\frac{p_1^2}{|p|^2}\right)
  \left(1-\frac{q_1^2}{|q|^2}\right).
 \tag{27}
\]
Values at zero momentum are irrelevant to the integral.
The preferred direction one has been retained. In particular
the coefficient at \(q=-p\) is generally nonzero. There is no
magnetic pair term in this observable to cancel it.

It follows, with all cutoffs removed by (20)--(23), that for any
\(a\downarrow0\), \(\ell=a(2L+1)\to\infty\) and \(t>0\),
\[
 \boxed{
 C^{E,L,a}_{0;h,h}(t)\longrightarrow C^E_h(t)
 =\frac{3}{8(2\pi)^6}
 \int_{\mathbb R^3}\!\int_{\mathbb R^3}
 |p||q|\left(1-\frac{p_1^2}{|p|^2}\right)
       \left(1-\frac{q_1^2}{|q|^2}\right)
 |\widehat h(p+q)|^2e^{-t(|p|+|q|)}\,dp\,dq .
 }
 \tag{28}
\]
All energy moments with the same positive-time damping converge
by the proved uniform tails. Real mixed covariances follow by
polarization. This is the directional electric counterpart of the
incoming all-mode result, with a different retained pair kernel.

## 3. Exact anisotropic density

Write \(k=p+q\), \(K=|k|\), and \(k_\perp^2=K^2-k_1^2\).
The raw locally finite measure in (28) is absolutely continuous:
\[
 \boxed{
 \rho^E_h(\omega)=\frac1{2560\pi^5}
 \int_{|k|<\omega}|\widehat h(k)|^2
 \left[(\omega^2-K^2)^2+
       (\omega^2-K^2)k_\perp^2+k_\perp^4\right]\,dk,\qquad
 d\nu^E_h(\omega)=\rho^E_h(\omega)\,d\omega .
 }
 \tag{29}
\]
There is no atom at zero or at the threshold. Here is a direct
evaluation of the full inner angular integral, including the
preferred axis.

Fix \(K>0\), put \(r=|p|\), \(s=|k-p|\), and
\(\omega=r+s\). Align a temporary polar coordinate axis with
\(k\), without moving the fixed vector \(\mathbf e_1\).
The polar-angle change to \(s\) gives measure
\((rs/K)\,dr\,d\phi\) after the energy delta function is
integrated. For \(\omega>K\), set
\[
 x=\frac{r-s}{K}\in[-1,1],\quad
 r=\frac{\omega+Kx}{2},\quad s=\frac{\omega-Kx}{2},
 \quad D=\omega^2-K^2,
 \tag{30}
\]
\[
 A=\frac{K+\omega x}{2},\quad B=\frac{K-\omega x}{2},
 \quad R^2=\frac{D(1-x^2)}4,\quad
 \mu=\frac{k_1}{K},\quad \eta=\mu^2,\quad e=1-\eta.
 \tag{31}
\]
The variables \(A,B\) are the axial components of \(p,q\) in
this calculation, not the Hamiltonian or its coefficients.
The transverse parts are opposite, with length \(R\).
Thus
\[
 p_1=\mu A+\sqrt e\,R\cos\phi,\qquad
 q_1=\mu B-\sqrt e\,R\cos\phi,\qquad
 r^2=A^2+R^2,\quad s^2=B^2+R^2.
 \tag{32}
\]
The original angular integrand times its Jacobian reduces to
\(\tfrac12(r^2-p_1^2)(s^2-q_1^2)\,dx\,d\phi\).
Using the exact averages of \(\cos\phi,\cos^2\phi,\cos^4\phi\),
the azimuthal mean of that product before its factor \(1/2\) is
\[
 P=e^2A^2B^2+
 \left[\frac{e(1+\eta)}2(A^2+B^2)-2\eta e AB\right]R^2
 +\left(\eta+\frac{3e^2}{8}\right)R^4.
 \tag{33}
\]
All four needed polynomial integrals are
\[
 \begin{split}
 \int_{-1}^1A^2B^2\,dx
  &=\frac{K^4-\frac23K^2\omega^2+\frac15\omega^4}{8},\\
 \int_{-1}^1(A^2+B^2)R^2\,dx
  &=\frac{D(5K^2+\omega^2)}{30},\\
 \int_{-1}^1ABR^2\,dx
  &=\frac{D(5K^2-\omega^2)}{60},\\
 \int_{-1}^1R^4\,dx&=\frac{D^2}{15}.
 \end{split}
 \tag{34}
\]
Each follows by expanding (31) and using
\(\int_{-1}^1x^{2m}dx=2/(2m+1)\).
Substituting \(\eta=1-e\) and \(\omega^2=D+K^2\) into
(33)--(34) gives
\[
 \int_{-1}^1P\,dx=\frac{D^2+DeK^2+e^2K^4}{15}.
 \tag{35}
\]
The coefficients of \(D^2,DeK^2,e^2K^4\) are all \(1/15\);
the remaining expanded terms cancel. Consequently the original
inner momentum integral is
\[
 \begin{split}
 &\int_{\mathbb R^3}|p||k-p|
 \left(1-\frac{p_1^2}{|p|^2}\right)
 \left(1-\frac{(k_1-p_1)^2}{|k-p|^2}\right)
 \delta(\omega-|p|-|k-p|)\,dp\\
 &\qquad=\frac{\pi}{15}
       [(\omega^2-K^2)^2+(\omega^2-K^2)k_\perp^2+k_\perp^4]
       \mathbf1_{\{\omega>K\}}.
 \end{split}
 \tag{36}
\]
The triangle inequality gives zero below threshold. The
degenerate boundary has zero measure in the joint integral.
At \(K=0\) the expression has limit \(\pi\omega^4/15\);
that outer null set requires no special assignment.
Tonelli applies to the nonnegative integrand, and the retained
constant is
\([3/(8(2\pi)^6)](\pi/15)=1/(2560\pi^5)\), proving (29).

The density is nonnegative and locally integrable. Its bracket
is strictly positive for \(K<\omega\), since \(D>0\).
If nonzero compact smooth \(h\) had \(\widehat h=0\) on a
ball, its convergent entire Taylor expansion, obtained by
integrating the exponential series over its compact support,
would vanish everywhere. Fourier uniqueness then forces \(h=0\).
For a direct uniqueness proof, multiply the zero transform by
a Gaussian and use its elementary inverse Fourier integral and
Fubini; every Gaussian convolution of \(h\) is zero, and these
convolutions converge to \(h\). Thus
\(\rho^E_h(\omega)>0\) for every \(\omega>0\) when \(h\ne0\).
In particular the measure gives positive mass to every
\((0,\varepsilon)\) and has no zero atom.

Integrating the polynomial in (29) over \(\omega\ge K\)
also evaluates the exact physical-time correlation:
\[
 \boxed{
 C^E_h(t)=\frac1{2560\pi^5}
 \int_{\mathbb R^3}e^{-tK}|\widehat h(k)|^2
 \left[
 \frac{k_\perp^4}{t}+
 \frac{2Kk_\perp^2}{t^2}+
 \frac{10K^2-2k_1^2}{t^3}+
 \frac{24K}{t^4}+\frac{24}{t^5}
 \right]\,dk,\qquad t>0 .
 }
 \tag{37}
\]
To check every coefficient, expand the bracket of (29) as
\[
 \omega^4-(K^2+k_1^2)\omega^2+
                    (K^4-K^2k_1^2+k_1^4)
 \tag{38}
\]
and integrate each monomial by repeated integration by parts
from \(K\) to infinity. All coefficients in (37) are
nonnegative; in particular \(10K^2-2k_1^2\ge8K^2\).

## 4. Infrared coefficients and the raw large-time amplitudes

Let \(m\) be the least degree of a nonzero homogeneous Taylor
polynomial \(P_m\) of \(\widehat h\) at zero. Its explicit
value is
\[
 P_m(k)=\frac{(-i)^m}{m!}\int_{\mathbb R^3}(k\cdot x)^m h(x)\,dx.
 \tag{39}
\]
For \(h\ne0\) such a degree exists by the preceding analyticity
and uniqueness argument. Uniformly for \(|z|\le1\),
\(\widehat h(\omega z)=\omega^mP_m(z)+O_h(\omega^{m+1})\).
Scaling \(k=\omega z\) in (29) proves
\[
 \rho^E_h(\omega)=A^E_{h,m}\omega^{7+2m}
                   +O_h(\omega^{8+2m}),\qquad\omega\downarrow0,
 \tag{40}
\]
where the full positive anisotropic coefficient is
\[
 \begin{split}
 A^E_{h,m}
 &=\frac1{2560\pi^5}
 \int_{|z|<1}|P_m(z)|^2
 \bigl[(1-|z|^2)^2+
       (1-|z|^2)(|z|^2-z_1^2)+(|z|^2-z_1^2)^2\bigr]\,dz\\
 &=\frac1{2560\pi^5}\int_{S^2}|P_m(n)|^2
 \left[
 \frac1{2m+3}-\frac{1+n_1^2}{2m+5}
             +\frac{1-n_1^2+n_1^4}{2m+7}
 \right]\,d\Omega(n)>0 .
 \end{split}
 \tag{41}
\]
The second line is the elementary radial integration of the first,
using homogeneity. Positivity follows from the first line:
its bracket is positive inside the ball and a nonzero polynomial
cannot vanish on an open ball.

For \(H_h=\int h\ne0\), \(m=0\) and \(P_0=H_h\).
Using
\(\int_{S^2}1=4\pi\), \(\int n_1^2=4\pi/3\),
\(\int n_1^4=4\pi/5\) in (41) gives
\[
 \boxed{\rho^E_h(\omega)\sim
       \frac{H_h^2}{3360\pi^4}\omega^7.}
 \tag{42}
\]
The sphere integrals follow by a polar axis along \(\mathbf e_1\)
and \(2\pi\int_{-1}^1u^{2r}du\).

Equations (29),(40), the rapid decay of \(\widehat h\), and the
substitution \(v=t\omega\) give
\[
 C^E_h(t)\sim
 A^E_{h,m}\Gamma(8+2m)t^{-(8+2m)},\qquad
 -{C^E_h}'(t)\sim
 A^E_{h,m}\Gamma(9+2m)t^{-(9+2m)}
 \quad(t\to\infty).
 \tag{43}
\]
For rigor, split the frequency integral at a fixed small positive
number. The complement is exponentially small in large \(t\);
inside, the remainder in (40) is bounded by its next power and
its gamma integral. Repeated integration by parts evaluates
each integer gamma integral. In particular, if \(H_h\ne0\),
\[
 \boxed{
 C^E_h(t)\sim\frac{3H_h^2}{2\pi^4t^8},\qquad
 -{C^E_h}'(t)\sim\frac{12H_h^2}{\pi^4t^9},\qquad
 -{C^E_h}'(t)/C^E_h(t)\sim\frac8t.
 }
 \tag{44}
\]
For general \(m\), the quotient is \((8+2m)/t+o(t^{-1})\).
The norms in (43)--(44) tend to zero with their full displayed
amplitudes. These are not unit-vector limits.

An exact continuity bound follows directly from (28):
\[
 \boxed{C^E_h(t)\le\frac{3}{2\pi^4t^8}\|h\|_1^2.}
 \tag{45}
\]
Indeed \(|\widehat h|\le\|h\|_1\) and
\[
 \int_{\mathbb R^3}|p|
 \left(1-\frac{p_1^2}{|p|^2}\right)e^{-t|p|}\,dp
 =\frac{8\pi}{3}\int_0^\infty r^3e^{-tr}\,dr
 =\frac{16\pi}{t^4}.
 \tag{46}
\]
Squaring (46) and multiplying by the exact prefactor in (28)
proves (45).

## 5. Complete ultraviolet polynomial and equal-time divergence

Since \(h\) is compact smooth, integration by parts makes
\(\widehat h\) decrease faster than any inverse power. Extending
the integral in (29),(38) from \(K<\omega\) to all \(k\)
therefore makes an error \(O_{h,N}(\omega^{-N})\) for every
fixed integer \(N\). On the omitted region \(K\ge\omega\),
all terms of (38) are bounded by a constant times \(K^4\);
the stated remainder follows by choosing a sufficiently high
Fourier decay power and integrating its radial tail.

Put \(\nabla_\perp=(\partial_2,\partial_3)\) and
\(\Delta_\perp=\partial_2^2+\partial_3^2\), and define
\[
 A_h=\|h\|_2^2,\qquad
 B_h=\|\nabla h\|_2^2+\|\partial_1h\|_2^2,\qquad
 D_h=\|\Delta_\perp h\|_2^2+
        \|\partial_1\nabla_\perp h\|_2^2+
        \|\partial_1^2h\|_2^2 .
 \tag{47}
\]
Here \(D_h\) denotes this scalar only in (47)--(50);
the directional electric operator remains \(D^E_h\) in (3).
The full ultraviolet expansion is
\[
 \boxed{
 \rho^E_h(\omega)=
 \frac{A_h\omega^4-B_h\omega^2+D_h}{320\pi^2}
          +O_{h,N}(\omega^{-N})\quad(\omega\to\infty).
 }
 \tag{48}
\]
Every coefficient follows from (38) and Fourier norm identities.
In particular
\[
 K^4-K^2k_1^2+k_1^4
 =k_\perp^4+k_1^2k_\perp^2+k_1^4,
 \tag{49}
\]
which gives the three nonnegative terms in \(D_h\).
With the Fourier convention (26), Parseval contributes
\((2\pi)^3\), giving \(8\pi^3/(2560\pi^5)=1/(320\pi^2)\).
This identity can be justified directly here: insert a Gaussian
factor in \(\int|\widehat h(k)|^2dk\), apply Fubini and the
elementary Gaussian Fourier integral, and let its width tend to
zero. The resulting approximate identity gives
\((2\pi)^3\int|h(x)|^2dx\). Integration by parts yields the
same statement for the derivatives in (47).

For \(h\ne0\), \(A_h>0\), so the locally finite raw measure has
infinite total mass. Positive-time damping gives finite mass and
all energy moments, since the density is bounded by a constant
times \(1+\omega^4\). Its exact small-time singular expansion is
\[
 C^E_h(t)=\frac1{320\pi^2}
    \left(\frac{24A_h}{t^5}-\frac{2B_h}{t^3}
                          +\frac{D_h}{t}\right)+O_h(1)
 \quad(t\downarrow0).
 \tag{50}
\]
To see that the remainder is bounded, subtract the polynomial
in (48) on the whole half-line. The resulting function is
integrable: it is bounded near zero and rapidly decreasing at
infinity. Its Laplace integral is therefore bounded. In
particular
\[
 C^E_h(t)\sim\frac{3\|h\|_2^2}{40\pi^2t^5},\quad
 -{C^E_h}'(t)\sim\frac{3\|h\|_2^2}{8\pi^2t^6},\quad
 -{C^E_h}'(t)/C^E_h(t)\sim\frac5t.
 \tag{51}
\]
The first-moment statement follows either by differentiating the
integral with its polynomial remainder, or repeating (50) with
one additional power of \(\omega\). Spatial smearing alone
therefore does not supply an equal-time Hilbert vector in this
limiting two-creation representation. This does not assert a
divergence at any finite regulator, where (3) is smooth.

## 6. The explicit common two-creation state map

Let the one-particle space be the complex \(L^2\) transverse
vector fields on momentum space with three colour coordinates,
using Lebesgue measure. Take its symmetric Fock space and
\(A_{\mathrm{fr}}=d\Gamma(|p|)\). On the \(n\)-particle space
this multiplies by \(\sum_{i=1}^n|p_i|\), with maximal squared
energy domain; the direct sum of these maximal real
multiplication operators is nonnegative and self-adjoint.
Its nonreal resolvents are the corresponding bounded
multipliers, which also verify these domain statements.

For \(t>0\) define the equal-colour symmetric two-particle vector
\[
 J^E_t h=\frac14\sum_{\alpha=1}^3\sum_{r,s=1}^2
 \int e^{-t(|p|+|q|)/2}\mathcal R^{E,rs}_h(p,q)
       a^\dagger_{r\alpha}(p)a^\dagger_{s\alpha}(q)
                       \Omega\,dp\,dq.
 \tag{52}
\]
Precisely, its two-particle wavefunction is
\(\sqrt2/4\) times the displayed symmetric kernel with equal
colours, so (52) requires no distributional operator product.
Equation (28) proves square integrability. It is invariant
under the original simultaneous adjoint rotations of the three
colour coordinates. The trace metric
\(-2\operatorname{tr}(T_\alpha T_\beta)=\delta_{\alpha\beta}\)
makes those rotations orthogonal; their contraction in (52)
is exactly preserved.

The full raw identities are
\[
 \|J^E_t h\|^2=C^E_h(t),\qquad
 \langle J^E_t h,A_{\mathrm{fr}}^nJ^E_t h\rangle
   =\int\omega^ne^{-t\omega}\rho^E_h(\omega)\,d\omega,
 \qquad
 e^{-sA_{\mathrm{fr}}/2}J^E_t h=J^E_{t+s}h.
 \tag{53}
\]
They follow directly from multiplication by the pair energy
and the factor \(3/8\) already proved. For nonzero \(h\)
the norm is positive by (29), proving injectivity on the real
test profiles. Complex-linear extension has the same Hermitian
norm formula. Changing a transverse polarization frame applies
pointwise orthogonal matrices and their tensor squares to
(26),(52), preserving the Hilbert vector and all norms.
Spatial translation \(h(x)\mapsto h(x-b)\) multiplies the
kernel by \(e^{i(p+q)\cdot b}\), the exact two-particle
translation representation. The direction-one axis remains
fixed; full spatial rotation covariance would also rotate
that prescribed axis.

This gives a typed common Hilbert and spectral map for the
positive-time vectors. Its Hamiltonian is the explicitly defined
free transverse multiplication operator. The correspondence
does not identify it with the full interacting continuum theory
or establish products of several local observables.

## 7. A common actual positive dyadic sequence

Retain \(L_j=j^2\), \(a_j=1/(100j)\), and
\(\ell_j=a_j(2L_j+1)\), for integers \(j\ge2\).
For actual finite-regulator vectors write
\[
 C^E_{g;h,k}(t)=
 \langle\Xi^E_{h,g},e^{-tA_g}\Xi^E_{k,g}\rangle,\qquad
 y^E_{h,g}(t)=e^{-tA_g/2}\Xi^E_{h,g}.
 \tag{54}
\]
Enumerate the positive rational times \(t_1,t_2,\ldots\).
Let \(\mathsf E_1\) be the original direction-one edges and
\(n_1=|\mathsf E_1|\). For each \(e\in\mathsf E_1\), use
the original single-edge electric state
\[
 \Xi^E_{e,g}=\kappa(E_e-\langle E_e\rangle_{\psi_g})\psi_g.
 \tag{55}
\]
These states have no added quarter-face observable term.
The full Hamiltonian used to evolve them is still (1).
Set \(\varepsilon_j=j^{-40}(1+\ell_j)^{-10}\).
At stage \(j\), impose all previously proved stage-\(j\)
conditions that are to be retained in the programme,
\(0<g<j^{-5}\), and the additional finite tests
\[
 \left|C^E_{g;e,e'}(t_n)
     -C^{E,L_j,a_j}_{0;e,e'}(t_n)\right|
       <\frac{\varepsilon_j}{n_1^2}
 \quad(e,e'\in\mathsf E_1,\ 1\le n\le j).
 \tag{56}
\]
At fixed \(j\), (14)--(16) prove convergence for each such
test. Mixed terms follow by real polarization, since the
Hamiltonian, weights and vacuum are real. The list is finite
at each stage, so it holds for every sufficiently small
positive coupling. The previously retained finite tests
likewise hold on tails by their proved fixed-box convergence.
Take the least positive integer exponent \(k_j\) for which
the entire list holds at \(g_j=2^{-k_j}\). Existence follows
from these tails and well ordering. This refines the coupling
selection; it does not assert that an earlier least dyadic
already met these extra electric tests.

Linearity in the original direction-one weights gives
\[
 |C^E_{g_j;h,k}(t_n)-C^{E,L_j,a_j}_{0;h,k}(t_n)|
 \le\varepsilon_j\|h\|_\infty\|k\|_\infty
 \quad(n\le j).
 \tag{57}
\]
Thus one sequence gives every fixed compact smooth profile at
each positive rational time. The all-mode limit (28) identifies
these limits. For every real \(t>0\), the actual diagonal
covariance \(C^E_{g_j;h,h}(t)\) is decreasing in \(t\)
because its spectral measure is nonnegative. Squeeze it between
two rational times and use the continuity of (37); then
polarize to obtain
\[
 C^E_{g_j;h,k}(t)\longrightarrow C^E_{h,k}(t)
 \quad(t>0)
 \tag{58}
\]
for all real compact smooth \(h,k\).

All original couplings remain
\[
 \kappa_j=200jg_j^2,\qquad
 b_j=50j/g_j^2,\qquad
 \xi_j=1/(4g_j^4),
 \tag{59}
\]
with every nonlinear Wilson term and its scalar, and the
actual vacuum at each positive \(g_j\). No uniform dependence
of the fixed-box approximation on \(L,a\) was assumed.
This sequence is not identified with the prescribed logarithmic
or fixed-electric-coefficient coupling paths.

For precision, let \(\nu^E_{h,g_j}\) be the actual unfiltered
raw spectral measure of (3). For fixed \(t>0\), define the
finite measure
\(\mu_{j,t}=e^{-t\omega}\nu^E_{h,g_j}\).
Its mass tends to \(C^E_h(t)\) and its Laplace transform
at \(s>0\) tends to \(C^E_h(t+s)\). The exact bound
\[
 (1-e^{-sR})\mu_{j,t}([R,\infty))
 \le C^E_{g_j;h,h}(t)-C^E_{g_j;h,h}(t+s)
 \tag{60}
\]
proves tightness: first choose \(s>0\) small using
continuity at \(t\), then \(R\) large so its denominator
is bounded away from zero. Finitely many initial measures
are controlled separately. On a compact energy interval,
polynomials in \(e^{-\omega}\) approximate all continuous
functions by the change \(z=e^{-\omega}\) and polynomial
approximation on its compact range. The Laplace limits and
tightness therefore identify the full weak limit:
\[
 \boxed{\mu_{j,t}\Longrightarrow
           e^{-t\omega}\rho^E_h(\omega)\,d\omega.}
 \tag{61}
\]
Applying (61) at \(t/2\) to the bounded continuous test
\(\omega^n e^{-t\omega/2}\) proves every positive-time
energy moment, including
\[
 \|y^E_{h,g_j}(t)\|^2\to C^E_h(t),\qquad
 \langle y^E_{h,g_j}(t),A_{g_j}y^E_{h,g_j}(t)\rangle
                   \to-{C^E_h}'(t).
 \tag{62}
\]
The damped vectors lie in every excitation-power domain:
the spectral multiplier \(\omega^m e^{-t\omega/2}\)
is bounded at each fixed \(t>0\).

For finitely many profiles and positive times, their actual
Gram and semigroup matrix elements converge to those of
(52). The mixed time is the sum of the two half-times
and any intervening nonnegative evolution time, so (58)
applies. This proves the common state correspondence at
the level claimed, without asserting an isometry between
the entire varying Hilbert spaces.

## 8. Locally finite raw convergence and unfiltered escape

Equation (61) also proves vague convergence of the actual
unfiltered measures to (29): multiply any compactly
supported continuous test by \(e^{t\omega}\).
Because the limiting density has no atoms, the same argument
by continuous upper and lower approximation gives
\[
 \nu^E_{h,g_j}([0,\Omega])
 \longrightarrow\int_0^\Omega\rho^E_h(\omega)\,d\omega
 \quad(0<\Omega<\infty).
 \tag{63}
\]
The limit is finite and positive for \(h\ne0\).
For the damped vectors their raw low-energy mass is instead
\(\int_0^\Omega e^{-t\omega}\rho^E_h(\omega)d\omega>0\).
These limits retain the original raw spectral amplitudes.

On the same actual sequence the unfiltered norms diverge:
\[
 \boxed{\|\Xi^E_{h,g_j}\|^2\longrightarrow\infty
        \quad(h\ne0).}
 \tag{64}
\]
Indeed their total spectral masses dominate
\(C^E_{g_j;h,h}(t)\). For any prescribed \(M\), choose
a fixed small \(t>0\) with \(C^E_h(t)>2M\), possible by
(50). Equation (58) makes that lower bound exceed \(M\)
at every sufficiently late regulator. Since \(M\) was
arbitrary, this proves (64), with no unsupported rate
in the regulator.

After these raw facts have been retained, their consequence
for the corresponding probabilities is
\[
 \frac{\nu^E_{h,g_j}([0,\Omega])}
      {\|\Xi^E_{h,g_j}\|^2}\longrightarrow0
 \quad(\Omega<\infty).
 \tag{65}
\]
This does not replace any original state by a unit vector;
it records what division by its explicitly diverging mass
would do. Positive raw low-energy mass in (63) and
probability escape in (65) both follow from the full
calculation.

Equations (43),(62) give the physical large-time filtered
raw amplitudes at each fixed positive time before any
time sequence is taken. If an actual time-growing sequence
is desired, set \(t=n\), and choose the least increasing
regulator index \(j_n\) for which the two errors in (62)
are each smaller than \(1/n\) times their respective
strictly positive limits. These indices exist by (62).
Then the actual vectors \(y^E_{h,g_{j_n}}(n)\) retain
the norm and energy amplitudes of (43), with ratio
\((8+2m)/n+o(n^{-1})\). This is an explicit further
selection, not an exchange of the positive-time and
regulator limits.

The original all-box covariance
\(\Gamma=\sum_{e\parallel1}n_2^2E_e\) has a different
noncompact spatial coefficient and its raw scaling is
not determined by replacing it with a fixed \(h\).
The native magnetic \(K_\theta\) state requires its
already specified separate covariance comparison.
This note supplies the exact direction-one local
electric coefficient, full positive-time spectral map,
anisotropic density, ultraviolet and infrared raw
amplitudes, and a common positive-coupling sequence.
It neither identifies that sequence with a prescribed
running-coupling path nor constructs an interacting
four-dimensional mass-gap counterexample.
