# Local-energy spacetime kernel and the exact nonlinear coupling response

8 September 2026.

The complete open-mode calculation in the companion *Full local-energy
spectral measure in the expanding-box limit* produces a spatially local
energy two-point function. This note evaluates its position-space kernel,
its positive-energy continuation, and its precise correspondence with the
energy-density covariance of three free vector fields. It then derives
an exact response formula in the original positive-coupling compact-link
Hamiltonian. That formula retains the electric term, the Wilson term,
the motion of the true vacuum, the vacuum subtraction, and the change of
time evolution. It supplies a quantitative map from the computed
comparison covariance to the nonlinear regulator covariance.

The correspondence calculated here does not identify the selected
continuum covariance with an interacting Yang--Mills theory. In
particular a free stress-tensor covariance is not advertised as a new
interacting spectrum or as a mass-gap counterexample.

## 1. Original local states and the full-mode input

On the original open cubic lattice keep all positively oriented contained
edges and elementary faces, product Haar probability, the generators
\(T_\alpha=-i\sigma_\alpha/2\), and
\[
 H_g=\frac{2g^2}{a}\sum_eE_e+
                 \frac1{2g^2a}\sum_p(2-\operatorname{tr}U_p),
 \qquad E_e=-\sum_{\alpha=1}^3X_{e,\alpha}^2.
 \tag{1}
\]
The Hilbert space is the invariant subspace for the full vertex gauge
group. Its unique positive unit vacuum, vacuum energy, and excitation
operator are \(\psi_g,\mathcal E_g,A_g=H_g-\mathcal E_g\).
For real \(h\in C_c^\infty(\mathbb R^3)\) take the exact weights
\[
 h_e=h(am(e)),\qquad h_p=\tfrac14\sum_{e\in\partial p}h_e,
 \quad D_{h,g}=\frac{2g^2}{a}\sum_eh_eE_e+
          \frac1{2g^2a}\sum_ph_p(2-\operatorname{tr}U_p).
 \tag{2}
\]
Put \(m_{h,g}=\langle\psi_g,D_{h,g}\psi_g\rangle\) and
\(\Xi_{h,g}=(D_{h,g}-m_{h,g})\psi_g\).
The scalar Wilson terms in (1)--(2) remain included. The centered states
are exactly physical and vacuum orthogonal.

The complete full-mode companion proves, with
\(L_j=j^2,\ a_j=1/(100j),\ \ell_j=a_j(2L_j+1)\), and its explicitly
selected positive dyadic couplings, that for \(t>0\)
\[
 \langle\Xi_{h,g_j},e^{-tA_{g_j}}\Xi_{k,g_j}\rangle
 \longrightarrow
 C_{h,k}(t)=\frac1{320\pi^5t}\int_{\mathbb R^3}
 |p|^4e^{-t|p|}\overline{\widehat h(p)}\,\widehat k(p)\,dp,
 \quad \widehat h(p)=\int e^{-ip\cdot x}h(x)\,dx .
 \tag{3}
\]
Its real-profile formula extends sesquilinearly to complex profiles.
The same companion gives the ordered two-creation map and the raw
measure
\[
 d\nu_h(\omega)=\frac1{320\pi^5}
       \int_{|p|\le\omega}|p|^4|\widehat h(p)|^2\,dp\,d\omega .
 \tag{4}
\]
These are inputs with full proofs in the companion, not an assumed
nonlinear continuum equation. The positive-time states
\(e^{-tA_g/2}\Xi_{h,g}\) have finite norms, with limit (3).
The measure (4) has infinite total mass for nonzero compact smooth
\(h\); no unsmeared continuum vector \(\Xi_h\) is asserted.

## 2. Exact position-space kernel

Define \(r=|x|\). With the Fourier convention in (3), the kernel in
\[
 C_{h,k}(t)=\int_{\mathbb R^3}\int_{\mathbb R^3}
                  \overline{h(x)}\,k(y)\,K_t(x-y)\,dx\,dy
 \tag{5}
\]
is exactly
\[
 \boxed{K_t(x)=
 \frac{9t^4-30t^2r^2+9r^4}{\pi^4(t^2+r^2)^6}
 =\frac1{40\pi^4}\Delta_x^2(t^2+r^2)^{-2}.}
 \tag{6}
\]
Here \(t\) remains the physical excitation time of (1).

To prove this, spherical integration, first for \(r>0\), gives
\[
 \int_{\mathbb R^3}e^{-t|p|}e^{ip\cdot x}\,dp
 =\frac{4\pi}{r}\int_0^\infty se^{-ts}\sin(rs)\,ds
 =\frac{8\pi t}{(t^2+r^2)^2}.
 \tag{7}
\]
The last integral follows by differentiating in \(t\) the imaginary
part of \(\int_0^\infty e^{-(t-ir)s}ds=(t-ir)^{-1}\).
Absolute exponential domination permits these operations and gives the
value at \(r=0\) by continuity. Multiplication by \(|p|^4\) is
\(\Delta_x^2\) under this transform. Thus the factors
\((320\pi^5t)^{-1}\) and \(8\pi t\) in (3),(7) leave
\((40\pi^4)^{-1}\).

For completeness set \(u=t^2+r^2\). On radial functions in three space
dimensions, \(\Delta f(r)=f''(r)+2f'(r)/r\). It yields
\[
 \Delta u^{-2}=12(r^2-t^2)u^{-4},\qquad
 \Delta^2u^{-2}
       =120(3t^4-10t^2r^2+3r^4)u^{-6}.
 \tag{8}
\]
The expressions are smooth at \(r=0\); hence the radial computation
proves (6) everywhere when \(t>0\). Fubini in (3), using compact
integrable profiles and the exponentially integrable momentum weight,
proves (5).

Three exact consequences are
\[
 K_t(0)=\frac9{\pi^4t^8},\qquad
 K_{bt}(bx)=b^{-8}K_t(x)\ (b>0),\qquad
 \int_{\mathbb R^3}K_t(x)\,dx=0 .
 \tag{9}
\]
For the last identity \(K_t\) is integrable, its Fourier value at zero
is zero by the \(|p|^4\) factor, and (7) fixes the Fourier factors.
Alternatively integrate the two Laplacians by parts on balls and
use the explicit derivative decay. This is the continuum counterpart
of \(D_{1,g}=H_g\), whose centered vacuum vector is exactly zero.
The kernel in (6) need not be pointwise nonnegative; covariance
positivity follows from the nonnegative Fourier density, not from
the sign of this function.

At fixed \(t>0\) and for fixed compact profiles, a displacement
\(Rn\), \(|n|=1,\ R\to\infty\), has
\[
 \int\!\!\int \overline{h(x)}\,k(y)
                   K_t(x-y-Rn)\,dx\,dy
 =\frac{9\overline{\int h}\int k}{\pi^4R^8}+O_{h,k,t}(R^{-9}).
 \tag{10}
\]
The rational formula (6) expands uniformly for \(x,y\) in their
fixed compact supports: \(R^8K_t(x-y-Rn)=9/\pi^4+O(R^{-1})\).
Integration against \(|h(x)k(y)|\) proves (10), with no assumption
of positivity of either profile.

## 3. The precise free stress-tensor correspondence

For \(X=(t,x)\in\mathbb R^4\setminus\{0\}\), set
\[
 I_{\mu\nu}(X)=\delta_{\mu\nu}
                     -\frac{2X_\mu X_\nu}{|X|^2},\qquad
 \mathcal I_{\mu\nu,\rho\sigma}
 =\tfrac12(I_{\mu\rho}I_{\nu\sigma}+I_{\mu\sigma}I_{\nu\rho})
                         -\tfrac14\delta_{\mu\nu}\delta_{\rho\sigma}.
 \tag{11}
\]
Direct substitution, not a fit of exponents, gives
\[
 \boxed{K_t(x)=
       \frac{12}{\pi^4|X|^8}\mathcal I_{00,00}(X).}
 \tag{12}
\]
Indeed \(\mathcal I_{00,00}=(1-2t^2/|X|^2)^2-1/4\);
putting it over the denominator \(|X|^{12}\) produces exactly
the numerator in (6).

Osborn and Petkou give (11) as their Eq. (2.23) and the free vector
coefficient \(C_T=16/S_4^2\) in Eq. (5.16), with
\(S_4=2\pi^2\). Thus each free vector contributes \(4/\pi^4\);
the three retained adjoint colour coordinates contribute
\(3(4/\pi^4)=12/\pi^4\), exactly (12).
The matched coefficient is established literature, not a new value
of \(C_T\). Our new correspondence here evaluates the complete
retained-regulator covariance in that convention.

Equation (12) identifies this one energy-density covariance. It
does not prove convergence of the other stress components, their
Ward identities as operator distributions, or higher products of
the interacting regulator fields. Equality of this two-point
function also does not assert that every correlation in any theory
containing it is free.

## 4. Positive energy, reflected covariance, and real time

The retained joint momentum measure is
\[
 d\varrho(\omega,p)=
       \frac{|p|^4}{320\pi^5}\mathbf1_{\{\omega\ge|p|\}}
                             \,d\omega\,d^3p .
 \tag{13}
\]
It is a positive tempered measure: on a Euclidean ball of radius
\(R\) its mass is at most a constant times \(R^8\), by direct
integration; the same estimate controls every Schwartz test.
Its support lies in the closed forward light cone.
Its Laplace transform in \(\omega\) is precisely the Fourier
kernel in (3), since
\(\int_{|p|}^\infty e^{-t\omega}d\omega=e^{-t|p|}/t\).

For compact smooth test functions \(f(t,x)\) supported at strictly
positive times, the reflected two-point quadratic form is
\[
 \int_{t,s>0}\!\!\int
       \overline{f(t,x)}K_{t+s}(x-y)f(s,y)\,dx\,dy\,dt\,ds
 =
 \int\left|\int_0^\infty
              e^{-t\omega}\widehat f(t,p)\,dt\right|^2
                                      d\varrho(\omega,p)\ge0 .
 \tag{14}
\]
Compact positive-time support supplies an exponential factor at
infinity, so Fubini is justified. Spatial Fourier signs agree by
the evenness in \(p\). Formula (14) is reflection positivity of
this two-point covariance; it is not the full hierarchy of
reflection-positivity inequalities for unspecified higher fields.

The positive-energy real-time distribution is
\[
 W(s,x)=\lim_{\epsilon\downarrow0}K_{\epsilon+is}(x)
       =\int e^{-is\omega+ip\cdot x}\,d\varrho(\omega,p),
 \tag{15}
\]
where the second integral is a distribution and fixes the sign
of the boundary value. To justify the limit, pair its Fourier
form with a Schwartz spacetime test; the factor
\(e^{-\epsilon\omega}\le1\) and the polynomial growth of (13)
give dominated convergence. For \(\operatorname{Re}z>0\) the
integral is analytic and equals the rational formula (6) with
\(t=z\), first for real \(z>0\) and then by analytic continuation.

Away from \(r^2=s^2\), the boundary values at \(s\) and \(-s\)
are the same real rational function. Therefore
\[
 \operatorname{supp}\{W(s,x)-W(-s,-x)\}
                         \subset\{(s,x):r^2=s^2\}.
 \tag{16}
\]
This support assertion is a direct statement about the computed
two-point commutator distribution. It does not infer an
operator commutator identity from its vacuum expectation.
The behaviour at the cone tip is determined by (13),(15);
no unverified product of singular delta distributions is used.

Thus this local covariance has an exact four-dimensional
spacetime map, positive energy and a light-cone-supported
commutator expectation. Its continuous spectrum near zero
is exhibited by (4). These statements close the two-point
spacetime calculation while retaining its precisely stated scope.

## 5. Exact differentiation of the nonlinear regulator

Fix the original finite box and \(a>0\). No coupling limit is
taken in the identities of this section. Abbreviate
\[
 K=\sum_eE_e,\quad W=\sum_p(2-\operatorname{tr}U_p),\quad
 K_h=\sum_eh_eE_e,\quad
 W_h=\sum_ph_p(2-\operatorname{tr}U_p).
 \tag{17}
\]
Here \(K\) denotes an operator, not the position-space kernel
\(K_t(x)\). For \(g>0\) the exact derivatives are
\[
 V_g:=\partial_gH_g=\frac{4g}{a}K-\frac1{g^3a}W,\qquad
 Z_{h,g}:=\partial_gD_{h,g}
                  =\frac{4g}{a}K_h-\frac1{g^3a}W_h.
 \tag{18}
\]
Both signs and all scalar Wilson pieces are present.

The original \(H_g\) has common domain \(H^2\) on every compact
positive interval of \(g\); \(W\) is bounded and the electric
coefficient is positive. The graph norms are equivalent there.
Thus \(H_{g+\epsilon}-H_g\), composed with a fixed nonreal
resolvent of \(H_g\), is a bounded operator tending to zero in
norm. More precisely, with \(\mathscr X=H^2\) carrying a fixed
equivalent graph norm and \(R_0(z)=(H_{g_0}-z)^{-1}\),
\[
 (H_g-z)^{-1}
 =R_0(z)[I+(H_g-H_{g_0})R_0(z)]^{-1}.
\]
The first factor maps \(L^2\) boundedly into \(\mathscr X\), and
the bracket is differentiable in bounded operators on \(L^2\).
The Neumann expansion therefore proves differentiability in
\(\mathcal B(L^2,\mathscr X)\), not merely in
\(\mathcal B(L^2,L^2)\).
Integrating the resolvent on a small circle containing
only the simple vacuum eigenvalue proves differentiability of
its rank-one projection. Applying that projection to \(\psi_g\)
and taking its positive real unit representative gives a
differentiable vacuum. This use of the unit-vacuum convention
does not divide any trial state \(\Xi_{h,g}\) by its norm.
Elliptic regularity gives smooth vacuum functions, and the
differentiated equations hold in the original operator domain.

Define the reduced inverse on the actual physical space,
\[
 P_g=I-|\psi_g\rangle\langle\psi_g|,\qquad
 R_g=(A_g|_{\psi_g^\perp})^{-1}P_g,\qquad
 v_g=\langle\psi_g,V_g\psi_g\rangle,\qquad
 \eta_g=R_g(V_g-v_g)\psi_g .
 \tag{19}
\]
Compact resolvent and vacuum simplicity imply a strictly positive
first excitation at this fixed regulator, so \(R_g\) is bounded.
No uniform bound in \(L,a,g\) is asserted. Gauge invariance of
every operator in (19) preserves Gauss' law exactly.
Differentiating \(H_g\psi_g=\mathcal E_g\psi_g\), and using the
real positive unit-vacuum convention, proves
\[
 \mathcal E_g'=v_g,\qquad
 \psi_g'=-\eta_g,\qquad
 m_{h,g}'=\langle\psi_g,Z_{h,g}\psi_g\rangle
                    -2\operatorname{Re}
                           \langle\eta_g,D_{h,g}\psi_g\rangle .
 \tag{20}
\]
The identity \(\langle\psi_g,\psi_g'\rangle=0\) follows because
both vectors are real and differentiation of the unit norm gives
zero real part. Applying \(P_g\) to the differentiated eigenvalue
equation then proves (19)--(20).

Consequently the full derivative of the centered local state is
\[
 \boxed{\Xi_{h,g}'=
        (Z_{h,g}-m_{h,g}')\psi_g
                       -(D_{h,g}-m_{h,g})\eta_g.}
 \tag{21}
\]
The signed weighted energy has its Peter--Weyl diagonal
self-adjoint domain plus bounded Wilson multiplication, not
necessarily all of \(H^2\). Its application in (21) is legitimate:
\(\eta_g\) solves an elliptic equation with smooth right side and
is smooth at this finite regulator. All displayed vectors belong
to the required common smooth domain.

## 6. A response formula retaining all intermediate states

For real \(h\), put
\(C_{g;h}(t)=\langle\Xi_{h,g},e^{-tA_g}\Xi_{h,g}\rangle\).
At any \(g,t>0\), the exact derivative is
\[
 \boxed{\begin{split}
 \partial_gC_{g;h}(t)
 ={}&2\operatorname{Re}
       \langle\Xi_{h,g}',e^{-tA_g}\Xi_{h,g}\rangle\\
 &-\int_0^t
 \langle\Xi_{h,g},e^{-(t-s)A_g}
                    (V_g-v_g)e^{-sA_g}\Xi_{h,g}\rangle\,ds .
 \end{split}}
 \tag{22}
\]
To verify Duhamel's term without assuming a bounded \(V_g\),
work on the smooth vectors above. Graph norm equivalence makes
\(V_g\) bounded from \(\mathscr X=H^2\) to \(L^2\).
Write \(S_\epsilon(u)=e^{-uA_{g+\epsilon}}\), \(S(u)=e^{-uA_g}\).
The product rule on a fixed smooth vector \(\xi\) gives
\[
 \frac d{ds}\{S_\epsilon(t-s)S(s)\xi\}
  =S_\epsilon(t-s)(A_{g+\epsilon}-A_g)S(s)\xi,
\]
and integration gives the exact sign
\[
 S_\epsilon(t)\xi-S(t)\xi
  =-\int_0^tS_\epsilon(t-s)
                (A_{g+\epsilon}-A_g)S(s)\xi\,ds .
 \tag{22a}
\]
Spectral calculus bounds \(\|S(s)\xi\|\) and
\(\|A_gS(s)\xi\|\) uniformly on \(0\le s\le t\).
Thus this trajectory is bounded in \(\mathscr X\).
Equation (22a) first proves strong semigroup convergence,
uniform on bounded time intervals for \(\xi\in\mathscr X\);
density and the contraction bounds extend it to each
fixed \(L^2\) vector. Also
\((A_{g+\epsilon}-A_g)/\epsilon\to V_g-v_g\)
in \(\mathcal B(\mathscr X,L^2)\).
The set \(\{(V_g-v_g)S(s)\xi:0\le s\le t\}\) is compact
in \(L^2\), by graph-norm continuity and compactness of the
parameter interval. A finite net and the contraction bounds
make strong semigroup convergence uniform on this set.
We may therefore divide (22a) by \(\epsilon\) and pass to
the limit in its Bochner integral, including both endpoints.
This proves the unbounded-insertion derivative used in (22).
Differentiating the two external vectors supplies
the first line of (22). No projection onto a low spectral band
has been inserted in its integral or in \(R_g\).

The constant-profile check is exact even though the profile is
then not compact in the continuum: on a finite box take \(h_e=1\)
for every edge. Then \(D_h=H_g,\ m_h=\mathcal E_g,\ Z_h=V_g\).
The expectation \(\langle\eta_g,H_g\psi_g\rangle\) vanishes, so
\(m_h'=v_g\). Equations (19),(21) give
\[
 \Xi_{1,g}=0,\qquad
 \Xi_{1,g}'=(V_g-v_g)\psi_g-A_g\eta_g=0.
 \tag{23}
\]
Both sides of (22) vanish. Omitting the vacuum response
\(-(D_h-m_h)\eta_g\) would fail this elementary consistency test.

For each fixed box the full weak-coupling graph theorem proves
\(C_{g;h}(t)\to C_{0;h}^{L,a}(t)\) as \(g\downarrow0\), where
the right side is the complete oscillator sum, not its lowest
band. The fundamental theorem of calculus therefore gives
\[
 \boxed{C_{g;h}(t)-C_{0;h}^{L,a}(t)
       =\lim_{\epsilon\downarrow0}
                    \int_\epsilon^g \partial_vC_{v;h}(t)\,dv,}
 \tag{24}
\]
with the integrand explicitly (18)--(22).
The integral is the displayed improper limit. No absolute
integrability or volume-uniform derivative bound at zero
coupling is inferred.

Formula (24) is the requested exact relation between the
comparison covariance and the original nonlinear one. On the
specific dyadic trajectory used in (3), the defining tests force
this difference to tend to zero at every fixed positive time.
That is a calculated property of this trajectory and these
observables, not a general theorem that non-Abelian interactions
vanish on all continuum trajectories.

The next interaction calculation has a definite integrand: retain
\(V_g-v_g\) in the full semigroup, \(R_g\) in the vacuum response,
and the two derivative terms of \(D_h\), then control (24) jointly
with \(a\downarrow0\) and \(\ell\uparrow\infty\) on a
physical-scale trajectory. The present work does not supply
that bound or identify an interacting reconstruction. It does
supply the exact response whose survival must be computed,
rather than replaced by an assumed remainder.

## Literature and proof dependencies

The full-mode lattice-to-spectral calculation, original graph
convergence, state domains and Fourier factors are proved in
Sections 14--16 of the included *Extensive quantum blocking and
local energy* manuscript. The exact compact/radial comparison is
proved separately in *Compact local energy, radial electric
observables, and a full-mode low-energy lower bound*.

H. Osborn and A. C. Petkou, *Implications of conformal invariance
in field theories for general dimensions*, Annals of Physics
231 (1994), 311--362,
[doi:10.1006/aphy.1994.1045](https://doi.org/10.1006/aphy.1994.1045),
[arXiv:hep-th/9307010v2](https://arxiv.org/abs/hep-th/9307010v2),
Eqs. (2.23), (5.3), (5.14)--(5.16). The actual source TeX was
read for these equations. It supplies the known free-vector
stress-tensor convention, not a new proof of our regulator limit.

A. Jaffe and E. Witten, *Quantum Yang--Mills Theory*, in
*The Millennium Prize Problems* (2006), 129--152,
[official problem text](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf),
Sections 3--4. Its local-field, spacetime and short-distance
requirements explain why the two-point correspondence and the
nonlinear response must both be retained.

S. Chatterjee, *Yang--Mills for probabilists*,
[arXiv:1803.01950](https://arxiv.org/abs/1803.01950),
the section entitled *The problem of defining the continuum
limit*. Its source TeX was consulted for the scale/correlation
and Wilson-loop discussion. No result here assigns a continuum
interpretation to a coupling sequence merely because each
member has positive coupling.
