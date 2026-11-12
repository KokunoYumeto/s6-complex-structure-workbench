# Independent audit: exact spatial vacuum elimination

8 September 2026. Verdict: PASS for the stated finite-regulator theorem.
All 799 lines of the current source and the complete checker were read.
No mathematical repair is required. No PDF, mathematical source, canonical
artifact or remote content was changed in this audit.

Audited files and SHA-256:

- Source: wilson_variation/spatial_vacuum_elimination.tex,
  2790469136513c1461639229d8d506b572e255750edc6dbb89b7c52a25456464.
- Checker: wilson_variation/check_spatial_elimination.py,
  bc3041d941fbcddff48ab91adbe4ae2512b22f67dc79cd36832b31242bd58d84.

The actual source contains the repaired \(F_{T/m}^{\,m}\) occurrences and
\(\sup_f\). The checker replay passed its 12 exact scalar/block assertions
and constituent matrix-entry comparisons. Those finite identities check
algebraic signs and coefficients; the infinite-dimensional arguments are
independently established below.

## 1. Ground-state transform and the infinite-rank form splitting

Keep the original configuration space
\(\mathcal Q=\mathrm{SU}(n)^{\mathsf E}\), probability product Haar measure,
all plaquette terms, positive \(\kappa_e,b_p\), and the original basis
\(-2\operatorname{tr}(T_aT_b)=\delta_{ab}\). For the actual positive unit
ground state, \(\rho=\psi_0^2\) is smooth with positive minimum on this
finite compact connected product. The ground-state product rule gives

\[
L=\psi_0^{-1}(H-E_0)\psi_0
=-\rho^{-1}\sum_{e,a}\kappa_eX_{e,a}(\rho X_{e,a}),\qquad
q(u,v)=\sum_{e,a}\kappa_e\int\overline{X_{e,a}u}X_{e,a}v\,d\mu .
\]

The finite tangent frame, positive coefficients and upper/lower density
bounds make \(q+\|\cdot\|_\mu^2\) equivalent to the \(H^1\) norm.
Consequently its form domain is precisely \(H^1(\mathcal Q)\), not an
unspecified domain of a block matrix. Smooth functions are a form core;
weighted elliptic regularity gives \(D(L)=H^2\) and compact resolvent.
Vanishing energy forces all derivatives to vanish, hence a constant.
The kernel is therefore \(\mathbb C1\), and the finite first nonzero
eigenvalue \(\delta\) is positive.

For the stated nonempty split \(\mathsf E=\mathsf S\sqcup\mathsf R\), put

\[
\rho_R=\int\rho\,d\lambda_S,\quad p=\rho/\rho_R,\quad
Jf=f(r),\quad J^*u=\int p(s\mid r)u(s,r)\,d\lambda_S .
\]

Fubini gives the isometry and the literal adjoint; conditional Jensen
gives its contraction. Thus \(P=JJ^*\) is the orthogonal retained
projection and \(\mathbb H_Q=\ker J^*\) is a closed, infinite-dimensional
subspace. With
\(\sigma_i=X_i\log\rho-X_i\log\rho_R=X_i\log p\), differentiation proves

\[
J^*\sigma_i=0,\qquad X_iJ^*u=J^*(X_iu)+J^*(\sigma_i u).
\]

Conditional Cauchy-Schwarz gives
\(\|J^*(X_iu)\|_{\mu_R}\leq\|X_iu\|_\mu\) and
\(\|J^*(\sigma_i u)\|_{\mu_R}\leq\|\sigma_i\|_\infty\|u\|_\mu\).
After squaring their sum and retaining every coefficient,

\[
a(J^*u,J^*u)\leq2q(u,u)+2\eta\|u\|_\mu^2,\qquad
\eta=\sum_{i\in R}\kappa_i\|\sigma_i\|_\infty^2 .
\]

This proves the bounded \(H^1\) projection and the exact form-domain
decomposition
\(\mathcal V=J\mathcal V_R\oplus\mathcal V_Q\), with
\(\mathcal V_R=H^1(\mathcal Q_R)\) and
\(\mathcal V_Q=H^1(\mathcal Q)\cap\mathbb H_Q\). The sum is orthogonal
in the Hilbert norm, not asserted orthogonal in energy. Iterated
differentiation proves the asserted boundedness on each \(H^k\).

The restricted form \(c_Q=q|_{\mathcal V_Q}\) is closed because
\(\mathbb H_Q\) is Hilbert-closed, and is dense because applying the
bounded \(Q\) to smooth approximants gives a core \(QC^\infty\).
Its representation theorem defines \(C\) with exactly the weak domain
printed in the source. For smooth eliminated \(h\), integration by parts
gives \(Ch=QLh\); this is not used as an assumed domain prescription.
Since \(h\perp1\), the full Poincare bound proves

\[
c_Q(h,h)\geq\delta\|h\|_\mu^2,\qquad C\geq\delta I .
\]

In particular both \((C+z)^{-1}\), \(z>0\), and \(C^{-1}\) exist and
map into \(D(C)\subset\mathcal V_Q\).

## 2. Conditional coupling, covariance and adjoint domains

Subtracting the two weighted divergence operators cancels every retained
second derivative. All eliminated derivatives of \(Jf\) vanish. Thus

\[
LJf=JAf+Bf,\qquad
Bf=-\sum_{i\in R}\kappa_i\sigma_iJ(X_if),\qquad J^*Bf=0 .
\]

Pointwise Cauchy-Schwarz with weights \(\sqrt{\kappa_i}\), followed by
integration, proves \(\|Bf\|_\mu^2\leq\eta a(f,f)\). Therefore \(B\)
extends boundedly from \(\mathcal V_R\) to \(\mathbb H_Q\). Expanding its
norm before integrating gives exactly the printed covariance tensor
\(I_{ij}=J^*(\sigma_i\sigma_j)\); for every complex vector \(z\),

\[
\sum_{i,j}\overline z_i I_{ij}z_j
=J^*\left(\left|\sum_i z_i\sigma_i\right|^2\right)\geq0.
\]

The covariance is taken in the actual conditional density \(p\).
It has not been replaced by an independent-link covariance.

With the stated conjugate-linear first-slot convention, Haar integration
by parts gives the positive divergence sign in

\[
B^*h=\rho_R^{-1}\sum_i\kappa_i
X_i\bigl(\rho_RJ^*(\sigma_i h)\bigr).
\]

Differentiating this conditional integral yields exactly its four terms
\(J^*(\sigma_iX_ih)\), \(J^*((X_i\sigma_i)h)\),
\(J^*(\sigma_i^2h)\), and
\(\bar\ell_iJ^*(\sigma_i h)\), each multiplied by \(\kappa_i\).
Bounded smooth coefficients and the conditional contraction prove
\(B^*:\mathcal V_Q\to\mathbb K\) bounded. On \(\mathbb H_Q\) alone the
adjoint means the bounded dual map to \(\mathcal V_R^*\), exactly as
specified. The two definitions agree on \(\mathcal V_Q\).

These bounds extend the smooth block identity to every stated form
vector. Replacing \(X_i,\sigma_i,\kappa_i\) by
\(2X_i,2\sigma_i,\kappa_i/4\) leaves the maps and forms unchanged,
checking the original metric factor without altering the Hamiltonian.

## 3. Infinite-rank Schur form and reconstruction

For \(z>0\), define \(R_z=(C+z)^{-1}\) and
\(s_z=a+z\langle\cdot,\cdot\rangle-\langle B\cdot,R_zB\cdot\rangle\)
on the fixed complete space \(\mathcal V_R\). The boundedness just
proved makes its last term a continuous form. The exact square identity is

\[
q(Jf+h,Jf+h)+z(\|f\|^2+\|h\|^2)
=s_z(f,f)+\|(C+z)^{1/2}(h+R_zBf)\|^2 .
\]

The unique minimizing \(h=-R_zBf\) belongs to \(\mathcal V_Q\).
It follows that \(s_z(f,f)\geq z\|f\|^2\). More importantly, with
\(v=Jf+h\), the projection bound and contraction imply

\[
a(f,f)+\|f\|^2
\leq2q(v,v)+(2\eta+1)\|v\|^2
\leq K_z\bigl(q(v,v)+z\|v\|^2\bigr),\quad
K_z=\max\{2,(2\eta+1)/z\}.
\]

Evaluate at the minimizer and also use \(h=0\) to obtain

\[
K_z^{-1}(a(f,f)+\|f\|^2)
\leq s_z(f,f)\leq a(f,f)+z\|f\|^2 .
\]

These are the needed complete form-norm bounds; mere pointwise positivity
would not suffice. They prove that \(s_z\) is closed and coercive, with
associated \(S_z\geq zI\).

For \(v=(L+z)^{-1}Jg=Jf+h\), testing its weak equation in
\(\mathcal V_Q\) gives \((C+z)h=-Bf\) in the precise weak-domain sense,
so \(h=-R_zBf\). The retained tests then give \(S_zf=g\). Therefore

\[
J^*(L+z)^{-1}J=S_z^{-1},\qquad
Q(L+z)^{-1}J=-R_zBS_z^{-1}.
\]

The variational inverse identity
\(\langle g,T^{-1}g\rangle
=\sup_f(2\operatorname{Re}\langle g,f\rangle-t(f,f))\), applied to
\(s_z\leq a+z\), proves the stated resolvent order. No exponential
ordering or finite-rank approximation is used.

## 4. Strong memory identity and exact second moment

For smooth \(f_0\), \(Jf_0\) belongs to every power domain of the compact
elliptic \(L\). Spectral calculus gives time differentiability in each
required graph norm even at zero; elliptic regularity converts these to
the needed Sobolev norms. Bounded \(P,Q\) on all \(H^k\) then make
\(f(t)=J^*e^{-tL}Jf_0\), \(h(t)=Qe^{-tL}Jf_0\) smooth in space, with

\[
f'=-Af-B^*h,\qquad h'=-Bf-Ch,\qquad h(0)=0.
\]

Here \(h(t)\in D(C)\) and \(Ch(t)=QLh(t)\) is continuous in
\(\mathbb H_Q\); thus differentiation of
\(e^{-(t-s)C}h(s)\) is legitimate and proves
\(h(t)=-\int_0^te^{-(t-s)C}Bf(s)\,ds\).

The integrability needed before applying the unbounded Hilbert-space
adjoint is supplied by its bounded form-space version. In the norm
\(\|h\|_{\mathcal V_Q}^2=\|h\|_\mu^2+c_Q(h,h)\), spectral calculus gives

\[
\|e^{-\tau C}\|_{\mathbb H_Q\to\mathcal V_Q}
\leq1+(2e\tau)^{-1/2},\qquad \tau>0 .
\]

The continuous forcing \(Bf(s)\) and this integrable endpoint bound
make the integral a \(\mathcal V_Q\)-valued Bochner integral. Applying
bounded \(B^*:\mathcal V_Q\to\mathbb K\) proves exactly

\[
f'(t)=-Af(t)+\int_0^tB^*e^{-(t-s)C}Bf(s)\,ds .
\]

The plus sign is forced by the two negative off-diagonal evolution
terms. No assertion that \(B^*\) is bounded on all \(\mathbb H_Q\)
enters this argument.

The full correlation identity follows from the unitary multiplication
by \(\psi_0\). Its Laplace integral converges in operator norm: the
positive semigroup is norm-continuous away from \(t=0\), is bounded by
one, and the omitted initial interval has integral norm at most its
length. The exponential tail is integrable. Thus the integral equals
the compressed resolvent already proved.

For smooth \(f\), the finite second spectral moment of \(Jf\) and dominated
Taylor remainder give

\[
\langle f,K(t)f\rangle
=\|f\|^2-ta(f,f)
+\frac{t^2}{2}\bigl(\|Af\|^2+\|Bf\|^2\bigr)+o(t^2).
\]

The two terms in \(LJf=JAf+Bf\) are orthogonal. Comparing with the
retained semigroup forces \(B=0\) on smooth functions if the semigroups
coincide, and its bounded form extension gives the full criterion.
Conversely \(B=0\) makes the closed form an orthogonal direct sum.
For unrestricted retained tests, arbitrary pointwise differentials in
a smooth local cutoff force each score to vanish; connectedness in
\(r\) gives \(p(s\mid r)=\rho_S(s)\). This proves precisely the
factorization criterion. The source correctly does not infer it from
only invariant test functions.

## 5. Strict full-state form quotient, including \(z=0\)

For nonzero centered \(f\in\mathcal V_R\), \(C\geq\delta I\) makes
\(w_z=(C+z)^{-1}Bf\) available for every \(z\geq0\).
The multiplication by \(\psi_0\) maps form domains unitarily; hence
\(u_z=\psi_0(Jf-w_z)\) is an actual original-Hilbert-space form vector.
Its vacuum inner product vanishes and
\(\|u_z\|^2=\|f\|^2+\|w_z\|^2>0\). No operator-domain membership is
needed or asserted for this general \(f\).

Testing the resolvent equation with \(w_z\) gives
\(c_Q(w_z,w_z)=I-zJ\), where
\(I=\langle Bf,(C+z)^{-1}Bf\rangle\), \(J=\|w_z\|^2\).
The block cross terms subtract \(2I\), so the exact quotient is

\[
\frac{\mathfrak h_0[u_z]}{\|u_z\|^2}
=\frac{a(f,f)-I-zJ}{\|f\|^2+J}.
\]

Its numerator is the nonnegative full form, not a guessed effective
energy. The exact decrease is

\[
\frac{I+(z+a(f,f)/\|f\|^2)J}{\|f\|^2+J}.
\]

The strictly positive inverse quadratic form gives \(I>0\) whenever
\(Bf\ne0\); this proves strict improvement. At \(z=0\), completing
the square with positive \(C\) proves unique minimization of energy
at fixed conditional mean, without asserting minimization of the
unconstrained Rayleigh quotient. Gauge covariance of the conditional
integral and forms makes all these vectors invariant when \(f\) is.
Thus their variational gap bounds have the stated physical subspace.

## 6. Two-sided Wilson slab and exact nonlinear integration

Keep the original constants

\[
\kappa_e=\frac{2g_{\rm YM}^2}{a},\quad
b_p^{\rm Hamiltonian}=\frac1{2g_{\rm YM}^2a},\quad
b_t=\frac{a}{2g_{\rm YM}^2\epsilon},\quad
b_s=\frac{\epsilon}{2g_{\rm YM}^2a}.
\]

The previously audited temporal proof supplies
\(T_\epsilon^{\rm raw}=c_\epsilon F_\epsilon P_G\),
\(c_\epsilon=[e^{-2b_t}Z(b_t)]^{|\mathsf E|}\), and
\(F_{T/m}^{\,m}\to e^{-TH}\) strongly at fixed spatial regulator.
Because \(1\) is invariant and the factors commute with \(P_G\), each
raw half slab has boundary vector \(c_\epsilon^mF_\epsilon^m1\).
Symmetry and reality of the kernel identify the two half-slab amplitudes.
Their product at the fixed central slice is therefore
\(c_\epsilon^{2m}\phi_{T,m}(U)^2\).

Composing the magnetic half-factors gives weight \(b_s\) at every
interior slice, including the central slice, and half weight at the two
outer slices. Every temporal plaquette retains weight \(b_t\).
Integrating the central slice gives the same scalar
\(c_\epsilon^{2m}\) in the normalization, so precisely
\(\rho_{T,m}=\phi_{T,m}^2/\|\phi_{T,m}\|^2\) remains. Temporal vertex
integrations, both time directions and outer boundary factors are present.

For the stated central-link selection, no spacetime plaquette meets two
selected links. Cyclic trace changes and inversion inside real trace put
every incident term in the exact form
\(-2b_p+b_p\operatorname{Re}\operatorname{tr}(U_eV_{ep})\).
For \(H_e=\sum_pb_pV_{ep}\), the quaternion identity gives

\[
H_eH_e^\dagger=r_e^2I,\qquad
r_e^2=\sum_pb_p^2+
\sum_{p<q}b_pb_q\operatorname{Re}\operatorname{tr}(V_{ep}V_{eq}^\dagger).
\]

This checks the cross-term factor. If \(r_e>0\), Haar translation by
\(H_e/r_e\in\mathrm{SU}(2)\) reduces the link integral to the normalized
semicircle integral. Expanding the exponential and integrating its even
moments gives

\[
\int e^{-2B_e+\operatorname{Re}\operatorname{tr}(U_eH_e)}dU_e
=e^{-2B_e}\sum_{k\geq0}\frac{r_e^{2k}}{k!(k+1)!}.
\]

At \(r_e=0\), \(H_e=0\) and this equals \(e^{-2B_e}\), so the endpoint
is covered. On a three-dimensional spatial interior edge the actual sum
is \(B_e=4b_s+2b_t\); boundary edges use their actual incident sums.
No-shared-plaquette selection makes each staple independent of the other
selected central links. Fubini therefore proves the source's product
integral while retaining \(S_{\rm rest}\), every cross-staple trace and
the two temporal staples. The unfactorized formula remains valid for
a general selection, exactly as stated.

## 7. Sequential \(L^1\) limit and the observable quotient

At fixed \(T>0\), strong transfer convergence gives
\(\phi_{T,m}\to e^{-TH}1\) in \(L^2\). The limit is nonzero and
positive. Normalizing these nonzero vectors is continuous, and

\[
\|v^2-w^2\|_1\leq(\|v\|_2+\|w\|_2)\|v-w\|_2
\]

gives convergence of the actual squared densities in \(L^1\).
Marginalization is an \(L^1\) contraction, so it also proves the
first sequential limit for retained densities.

For \(c_0=\langle\psi_0,1\rangle>0\), decompose the other limit as

\[
e^{TE_0}e^{-TH}1=c_0\psi_0+r_T,\qquad
\|r_T\|\leq e^{-T\delta}\sqrt{1-c_0^2},\qquad r_T\perp\psi_0 .
\]

The displayed normalization estimate \(2\|r_T\|/c_0\) is valid by
the triangle inequality and
\(\|c_0\psi_0+r_T\|=\sqrt{c_0^2+\|r_T\|^2}\geq c_0\).
The two unit-vector norms in the squared-density bound contribute
another factor two. Hence exactly

\[
\|\rho_{R;T}-\rho_R\|_1
\leq \frac{4\sqrt{1-c_0^2}}{c_0}e^{-T\delta}.
\]

This proves the claimed order
\(\lim_{T\to\infty}\lim_{m\to\infty}\), not an exchange of limits.

Finally, for the fixed smooth nonconstant retained observable, positivity
of the true density gives \(v_F>0\). The \(L^1\) errors are bounded by
\(G_F\eta_1\) for the Dirichlet integrand and \(3M_F^2\eta_1\) for
variance: the latter is the second-moment error \(M_F^2\eta_1\) plus
the squared-mean error \(2M_F^2\eta_1\). Under
\(\eta_1\leq v_F/(6M_F^2)\), the perturbed variance is at least
\(v_F/2\). Subtracting the fractions gives exactly

\[
|\widetilde Q_R(F)-Q_R(F)|
\leq\frac{2G_F}{v_F}\eta_1+
\frac{6G_FM_F^2}{v_F^2}\eta_1 .
\]

Thus the finite nonlinear slab integrations converge to the actual
true-vacuum marginal and its retained spectral first moment with the
stated maps and constants. This is sufficient support for the concrete
adjacent-plaquette calculation already audited. It does not assert
uniform spatial estimates, a joint continuum limit or a four-dimensional
continuum mass-gap result.
