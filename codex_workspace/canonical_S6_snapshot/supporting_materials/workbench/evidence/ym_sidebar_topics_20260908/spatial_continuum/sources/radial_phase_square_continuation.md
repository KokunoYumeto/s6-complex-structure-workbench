## 22. A positive Gamma limit and an exact rescaled electric observable

### 22.1. The radial family with all raw spectral weights retained

The retained radial Gamma and amplitude/time proofs extend the
fixed-parameter calculation in Section 20. We first give the full
measure calculation needed for the new operator map below. Keep
\[
 L_j=j^2,\quad a_j=\frac1{100j},\quad
 \sigma_j=\sqrt8\sin\frac{\pi}{4j^2+2},\quad
 \lambda_j=\frac{2\sigma_j}{a_j},\quad
 c_j=j\lambda_j,\quad c_\Gamma=100\sqrt2\pi,\quad k=\frac32 .
 \tag{278}
\]
Here \(j\ge2\) is an integer, and \(c_\Gamma\) is the physical
Gamma scale, distinct from the spacetime coordinate constant in
Section 21. The full actual finite-box Hamiltonian and vacuum remain
those of (190)--(205). At each fixed box use the same exact tree,
Haar, logarithm and kinetic-coordinate maps. Put
\[
 F_j(y)=\chi(y)\frac{\sigma_j}{4}
       |(O^{\mathsf T}G^{-1/2}y)_{\nu_j}|^2,\qquad
 Q_{g,j}=g^{-2}F_j,\qquad
 B_{g,j}(\beta)=e^{i\beta Q_{g,j}} .
 \tag{279}
\]
The real invariant cutoff is supported strictly inside the full
logarithm chart and equals one near zero. Extend \(F_j\) by zero
off that chart; it is a globally smooth real physical function.
Thus \(Q_{g,j}\) is a bounded self-adjoint multiplication operator
at every finite \(g>0,j\), even though no bound uniform in the
regulator is asserted. In the transported limit it becomes
\(q=\sigma_j|z_{\nu_j}|^2/4\). Its probability law in the
comparison vacuum is \(d\rho(q)=q^{k-1}e^{-q}dq/\Gamma(k)\).
All three colour coordinates and the original kinetic tensor occur
in (279).

Let \(\beta_j=\sqrt j\), subtract the actual mean
\(m_{g,j}=\langle\psi_{g,j},B_{g,j}(\beta_j)\psi_{g,j}\rangle\),
and set \(v_{g,j}=(B_{g,j}(\beta_j)-m_{g,j})\psi_{g,j}\).
Its raw norm is \(1-|m_{g,j}|^2>0\), by the strict
Cauchy--Schwarz inequality for a nonconstant multiplier and the
strictly positive vacuum. The finite-box theorem and (253) give
the complete comparison measure
\[
 \nu_{0,j}=\sum_{n=1}^{\infty}
 \frac{(k)_n}{n!}\frac{j^n}{(j+1)^{n+k}}\,
 \delta_{\lambda_j n},\qquad
 d_j=\nu_{0,j}([0,\infty))=1-(j+1)^{-k}.
 \tag{280}
\]
The missing \(n=0\) coefficient is exactly the removed vacuum
component, not an omitted low-energy mass.

For a direct quantitative limit, let \(Q\) have law \(\rho\),
and conditionally on \(Q=q\) let \(N_j\) be Poisson with mean
\(jq\). Gamma integration gives
\[
 {\mathbb P}(N_j=n)
 =\frac{j^n}{n!\Gamma(k)}
   \int_0^\infty q^{n+k-1}e^{-(j+1)q}\,dq
 =\frac{(k)_n}{n!}\frac{j^n}{(j+1)^{n+k}}.
 \tag{281}
\]
Thus the law of \(\lambda_jN_j\) is exactly
\(\nu_{0,j}+(j+1)^{-k}\delta_0\). Since
\({\mathbb E}(N_j/j-Q\mid Q)=0\),
\({\mathbb E}((N_j/j-Q)^2\mid Q)=Q/j\),
\({\mathbb E}Q=k\) and \({\mathbb E}Q^2=k(k+1)\),
\[
 {\mathbb E}|\lambda_jN_j-c_\Gamma Q|^2
 =\frac{kc_j^2}{j}+k(k+1)(c_j-c_\Gamma)^2.
 \tag{282}
\]
The mixed term vanishes by conditional expectation. For
\(x_j=\pi/(4j^2+2)\), integration of \(1-\cos x\le x^2/2\)
gives \(0\le x_j-\sin x_j\le x_j^3/6\), and therefore
\[
 0<c_\Gamma-c_j\le
 \frac{c_\Gamma}{2j^2+1}
 +\frac{400\sqrt2\pi^3j^2}{6(4j^2+2)^3}.
 \tag{283}
\]
For finite measures, let \(d_{\rm BL}\) use tests of supremum
norm at most one and Lipschitz constant at most one. The coupling,
Cauchy--Schwarz and the removed zero mass yield
\[
 \begin{split}
 d_{\rm BL}(\nu_{0,j},\gamma_\Gamma)
 &\le
 \left[\frac{kc_j^2}{j}
       +k(k+1)(c_j-c_\Gamma)^2\right]^{1/2}+(j+1)^{-k}
 \longrightarrow0,\\
 d\gamma_\Gamma(\omega)
 &=\frac{\omega^{1/2}e^{-\omega/c_\Gamma}}
       {\Gamma(3/2)c_\Gamma^{3/2}}\,d\omega .
 \end{split}
 \tag{284}
\]
The density follows by the change of variable \(\omega=c_\Gamma q\).
It has total mass one, zero mass at zero, and positive mass on every
\((0,\epsilon)\), \(\epsilon>0\).

At each fixed \(j\), actual-vacuum and finite-projection convergence
give convergence of the actual raw measure to (280), including total
mass. A positive dyadic \(g_j\) can consequently satisfy
\[
 g_j<j^{-5},\quad
 d_{\rm BL}(\nu_{g_j,j},\nu_{0,j})<j^{-1},\quad
 |\|v_{g_j,j}\|^2-d_j|<j^{-1},\quad
 |m_{g_j,j}-(1-i\sqrt j)^{-k}|<j^{-1}.
 \tag{285}
\]
Below we impose additional proved fixed-box weighted convergence
conditions on this selection. This refines the finite list used to
choose the dyadic; it does not identify it with either prescribed
running-coupling trajectory or with Section 18's native covariance
sequence. All original coefficients remain
\(\kappa_j=200jg_j^2\), \(b_j=50j/g_j^2\),
\(\xi_j=1/(4g_j^4)\), including the scalar \(2b_j|P_j|\).
Equations (284)--(285) prove the actual nonlinear raw limit
\(\nu_{g_j,j}\Rightarrow\gamma_\Gamma\) and
\(\|v_{g_j,j}\|^2\to1\). The absence of endpoint atoms gives
\[
 \nu_{g_j,j}((0,\epsilon))
 \longrightarrow\gamma_\Gamma((0,\epsilon))>0 .
 \tag{286}
\]
This is a positive low-energy limit of this radial observable.
It has not been identified with the original magnetic translation
state or a spatial local interacting continuum.

### 22.2. Exact phase conjugation in the full nonlinear Hamiltonian

Fix \(j,g>0\), abbreviate \(A=H-\mathcal E\), \(Q=Q_{g,j}\),
and retain every edge and colour derivative \(X=X_{e,\alpha}\).
Each \(X\) is skew-adjoint for the original Haar measure. For a
smooth physical function \(f\), the product rule gives
\[
 X(e^{i\beta Q}f)
 =e^{i\beta Q}(Xf+i\beta(XQ)f).
 \tag{287}
\]
Applying \(X\) a second time and using the entire Hamiltonian gives
\[
 \begin{split}
 B(\beta)^*AB(\beta)&=A+\beta J+\beta^2R,\\
 J=i[A,Q]&=-i\kappa\sum_{e,\alpha}
       \bigl(2(X_{e,\alpha}Q)X_{e,\alpha}
                    +X_{e,\alpha}^2Q\bigr),\\
 R=\tfrac12[Q,[A,Q]]
     &=\kappa\sum_{e,\alpha}(X_{e,\alpha}Q)^2\ge0 .
 \end{split}
 \tag{288}
\]
These identities hold on smooth physical functions and extend to
the original second-order Sobolev operator domain, since each
coefficient and each multiplier is smooth on the compact group.
The Wilson multiplication, its scalar term and \(\mathcal E\)
commute with \(B\); none has been deleted. For the double
commutator, \([J,Q]=-2iR\) follows by applying the displayed
first-order expression to \(Qf\), so
\([Q,[A,Q]]=-i[Q,J]=2R\). This checks both signs.
Gauge invariance follows either from the commutator formula or
from gauge invariance of \(A,Q\). In particular \(R\) is an
actual nonnegative, bounded, gauge-invariant multiplication
operator at every finite regulator.

For any smooth \(h\), the exact ground-state form identity is
\(q_A[h\psi]=\kappa\int\psi^2\sum|Xh|^2\,dU\).
It is obtained by expanding \(X(h\psi)\), integrating its mixed
terms by parts, and substituting the full equation \(H\psi=\mathcal E\psi\);
the potential cancels against that equation with its complete
coefficient. Setting \(h=e^{i\beta Q}\) in (287) proves
\[
 q_A[(B(\beta)-\langle B(\beta)\rangle_\psi)\psi]
 =q_A[B(\beta)\psi]=\beta^2\langle R\rangle_\psi .
 \tag{289}
\]
Centering does not change this form because \(A\psi=0\).
This is an exact electric-energy formula for a raw state.


### 22.3. The complete fixed-box weighted tail estimate

Continue at fixed \(j\), and abbreviate \(F=F_j\),
\(R_g=R_{g,j}\), \(a=a_j\), and \(\nu=\nu_j\), so
\(\sigma_\nu=\sigma_j\). Write
\(W=\sum_p(2-\operatorname{tr}U_p)\) for the complete face
potential, and \(N,M\) for the original edge and face counts.
All formulas involving \(\mathcal B_g\) below are in the
original scaled chord coordinates \(x\); their \(\Phi_0\)
is the exact comparison vacuum in those coordinates. The
constant-Jacobian kinetic-coordinate unitary from (224)
then gives the stated radial \(L^2(\rho)\) map.

Let \(\mathcal X_{e,\alpha}\) be the exact quotient fields of Section
17.1, and define the globally smooth nonnegative function
\[
 S(y)=\sum_{e,\alpha}(\mathcal X_{e,\alpha}F(y))^2.
\]
The quotient identity intertwines the original sums of squared
derivatives, so
\[
 R_g=\frac{2}{ag^2}S.
 \tag{290}
\]
There is a finite constant \(C_S\), depending on the fixed box, mode
and cutoff, with
\[
 S\le C_SW \quad\hbox{on the whole compact chord manifold}.
 \tag{291}
\]
Here is the global justification. The original face potential has
expansion
\(W(y)=\frac14\sum_\alpha\|Cy^\alpha\|^2+O(|y|^3)\).
The matrix \(C^*C\) is strictly positive on chord coordinates. Hence
choose a chart radius \(\rho>0\) and \(c_*>0\) with
\(W(y)\ge c_*|y|^2\) for \(|y|<\rho\). The smooth function \(F\) has
zero value and zero differential at zero; its differentiated square
satisfies \(S(y)\le C_*|y|^2\) there. For example bounded second
derivatives of \(F\), together with bounded coefficient vectors of the
finitely many \(\mathcal X_{e,\alpha}\), give such a finite \(C_*\)
by the fundamental theorem of calculus along the segment from zero.
All faces flat on the contractible open box imply all based chord
holonomies are the identity: elementary face moves identify the
canonical tree paths, and the original chord words then equal \(I\).
Thus \(W\) has precisely one zero on the chord manifold. Compactness
gives \(W\ge c_\rho>0\) off the radius-\(\rho\) neighborhood.
One can take
\[
 C_S=\max\left\{\frac{C_*}{c_*},
                 \frac{\max S}{c_\rho}\right\}.
\]
This proves (291), including the region where the cutoff changes.

Put \(U_g=W/g^2\) and \(D_S=2C_S/a\). Equations (290)--(291) give
\[
 0\le R_g\le D_SU_g.
 \tag{292}
\]
The complete actual-vacuum moment proof in Section 17.4 gives, for
every integer \(n\ge0\),
\[
 \int U_g^n\psi_g^2\,dU\le B_n,\quad
 B_0=1,\quad B_1=2aK,\quad
 B_{n+1}=2aK B_n+16n^2B_{n-1}\ (n\ge1),\quad
 K=\frac{3\sqrt{NM}}a.
 \tag{293}
\]
Here \(N,M\) are the original numbers of edges and faces.
These estimates use the actual energy bound \(\mathcal E_g\le K\).
Their derivation retains the exact identity
\(q_H[f\psi]-\mathcal E_g\|f\psi\|^2
=\kappa\int\psi^2\sum|Xf|^2\),
the full-potential bound \(\sum|XW|^2\le16W\), and consequently
\(bM_{n+1}\le\mathcal E_g M_n+4\kappa n^2M_{n-1}\).
Thus (293) is available for arbitrarily high fixed powers, not merely
the first vacuum moment.

Let \(\mathcal B_g\) be the exact Haar-density and dilation isometry,
zero-extended outside \(\Omega_g\), and \(f_g=\mathcal B_g\psi_g\).
For an integer \(m\ge1\) and radius \(R>0\), split \(|x|>R\) into
\(|gx|<\rho\) and its complement. On the former region
\(U_g\ge c_*R^2\), and on the latter \(U_g\ge c_\rho/g^2\).
Equations (292)--(293) therefore give the explicit weighted squared tail
\[
 \boxed{
 \int_{|x|>R}|\mathcal B_g(R_g^m\psi_g)(x)|^2\,dx
 \le D_S^{2m}B_{2m+1}
           \left(\frac1{c_*R^2}+\frac{g^2}{c_\rho}\right).
 }
 \tag{294}
\]
In particular \(m=1\) uses \(B_3\), and \(m=2\) uses \(B_5\).
No assumption about a cutoff-region tail has been inserted.

### 22.4. Exact coefficient and vacuum-vector limit

Write
\[
 z^\alpha=O^{\mathsf T}G^{-1/2}x^\alpha,\qquad
 q(x)=\frac{\sigma_\nu}{4}|z_\nu|^2,\qquad
 \lambda=\frac{2\sigma_\nu}{a}.
\]
On each fixed ball, \(\chi(gx)=1\) for small enough \(g\).
The exact tangent coefficients of the quotient fields have squared
Gram matrix \(G\otimes I_3\). It follows directly from (290) that the
transported multiplier \(r_g(x)=R_g(\exp(gx))\) satisfies
\[
 r_g(x)\longrightarrow
 \frac2a\sum_\alpha(\nabla_{x^\alpha}q)^{\mathsf T}
                       G(\nabla_{x^\alpha}q)
 =\frac2a\frac{\sigma_\nu^2}{4}|z_\nu|^2
 =\lambda q(x).
 \tag{295}
\]
This convergence is uniform on each fixed ball. The middle equality
uses the selected row of \(O^{\mathsf T}G^{-1/2}\) and
\(O^{\mathsf T}O=I\); it retains the original quotient kinetic metric.
The Haar-density factor commutes with multiplication, so it introduces
no omitted term into (295).

The actual strong vacuum limit \(f_g\to\Phi_0\), local coefficient
convergence (295), and the tail bound (294) prove
\[
 \boxed{\mathcal B_g(R_g^m\psi_g)
            \longrightarrow(\lambda q)^m\Phi_0
       \quad\hbox{strongly in }L^2,\qquad m\ge1.}
 \tag{296}
\]
Indeed convergence on a fixed ball follows by multiplying strongly
convergent vectors by uniformly convergent bounded multipliers there.
First taking \(g\downarrow0\), then \(R\to\infty\), controls the full
error using (294) and the polynomial times Gaussian tail of the limit.
In particular, with \(k=3/2\) and
\(d\rho(q)=q^{k-1}e^{-q}dq/\Gamma(k)\),
\[
 \langle R_g\rangle_{\psi_g}\to\lambda k,\qquad
 \langle R_g^n\rangle_{\psi_g}\to\lambda^n(k)_n
 \quad(n\ge1).
 \tag{297}
\]
One obtains each expectation by (296) and the strong unit vacuum limit.

### 22.5. Weighted transport on actual carrier time-orbit vectors

For each fixed box and real \(\beta\), set
\[
 m_g(\beta)=\langle\psi_g,e^{i\beta Q_g}\psi_g\rangle,\qquad
 v_g(\beta)=(e^{i\beta Q_g}-m_g(\beta))\psi_g,\qquad
 h_g(\beta,t)=e^{-tA}v_g(\beta),\quad t\ge0.
\]
The fixed-box spectral theorem and bounded phase-vector convergence
give strong transport to the exact oscillator time vector
\[
 h_0(\beta,t)=e^{-tA_0}
       (e^{i\beta q}-(1-i\beta)^{-k})\Phi_0.
 \tag{298}
\]
This convergence is uniform for \(\beta,t\) in compact parameter
sets. A direct proof uses compactness of the comparison phase-vector
family in \(L^2\), a finite uniform net and finite oscillator spectral
cutoffs, convergence of the corresponding actual projections, and
uniform convergence of the finitely many exponential energy factors.
The initial phase vectors converge uniformly even over all phase
parameters: the actual multiplier equals \(e^{i\beta q}\) on a ball
whose radius tends to infinity, while both multipliers have modulus one.

The original positive heat semigroup satisfies
\[
 |e^{-tA}(u\psi_g)|\le\|u\|_\infty\psi_g.
 \tag{299}
\]
For completeness, the product-group electric heat kernels are positive;
the full real bounded Wilson multiplication has positive exponential.
The Trotter product and strong convergence preserve positivity and
\(|e^{-tA}u|\le e^{-tA}|u|\). The identity \(e^{-tA}\psi_g=\psi_g\)
then proves (299). Gauge restriction preserves it. Thus
\[
 |h_g(\beta,t)|\le2\psi_g,
 \tag{300}
\]
uniformly for all real \(\beta\) and \(t\ge0\).

Multiply the squared tail bound (294) by four and use (300). The same
local convergence argument as in (296) proves, for every fixed integer
\(m\ge1\),
\[
 \boxed{\mathcal B_g(R_g^m h_g(\beta,t))
       \longrightarrow(\lambda q)^m h_0(\beta,t)
       \quad\hbox{strongly, uniformly on compact }(\beta,t)\hbox{ sets}.}
 \tag{301}
\]
The local part is uniform by (298) and the fixed-ball multiplier bound;
the tail is uniform by (294),(300). Finite linear combinations inherit
the same result. This proves the required polynomial powers on these
time-orbit vectors. It makes no assertion about arbitrary interspersed
unbounded products.

### 22.6. A positive-coupling diagonal retaining the weighted tests

For \(j\ge2\), retain
\[
 L_j=j^2,\quad a_j=\frac1{100j},\quad
 \sigma_j=\sqrt8\sin\frac{\pi}{4j^2+2},\quad
 \lambda_j=\frac{2\sigma_j}{a_j},\quad
 c_j=j\lambda_j\longrightarrow c_\Gamma=100\sqrt2\pi.
\]
The preexisting diagonal selected only bounded phase/time kernels and
configuration flatness. Those tests alone do not establish (301) after
multiplication by a growing power of \(j\). Refine the positive dyadic
choice at stage \(j\) as follows. In addition to every previous
stage-\(j\) test and \(g<j^{-5}\), require
\[
 \sup_{|\beta|\le j^2,\ 0\le t\le j}
 \left\|\mathcal B_g((jR_g)^m h_g(\beta,t))
                   -c_j^m q^m h_0(\beta,t)\right\|<\frac1j,
 \qquad 0\le m\le j,
 \tag{302}
\]
The zero power explicitly includes unweighted vector transport; the compact-family convergence of (298) proves this case. Also impose the corresponding vacuum-vector tests
\[
 \left\|\mathcal B_g((jR_g)^m\psi_g)
                   -c_j^m q^m\Phi_0\right\|<\frac1j
 \quad(1\le m\le j),\qquad
 |\langle R_g\rangle-\lambda_j k|<j^{-5}.
 \tag{303}
\]
At each fixed \(j\), there are finitely many powers and each compact
supremum tends to zero by (296),(301). Thus all tests hold at every
sufficiently small positive \(g\); a dyadic exists. Take the least
positive dyadic exponent satisfying the entire list. This is a
definite refined sequence, not an assertion that an earlier least
dyadic already satisfies the new conditions. Its original coefficients
remain \(\kappa_j=200jg_j^2\), \(b_j=50j/g_j^2\),
\(\xi_j=1/(4g_j^4)\), with every face and scalar Wilson term present.
Spectral tests for the centered \(R_g\) vacuum vector used below can
be included in this same finite list, by the fixed-box argument in
Section 22.8.

### 22.7. The exact nonconstant carrier operator

Fix \(b_0\ne0\), a real offset \(\alpha\), and put
\(s_j=b_0\sqrt j\), \(\beta_j=s_j+\alpha\).
The exact oscillator radial map sends the vacuum to \(1\) in
\(L^2(\rho)\), and
\[
 A_{0,j}=\lambda_jN,\qquad
 N=-q\partial_q^2-(k-q)\partial_q,\qquad
 U_s f=e^{isq}f,\qquad R_{0,j}=\lambda_jQ,\quad Qf=qf.
 \tag{304}
\]
The identity on exponential functions
\[
 e^{-uN}e^{i\beta q}
 =[1-i\beta(1-e^{-u})]^{-k}
  \exp\left(\frac{i\beta e^{-u}q}
                  {1-i\beta(1-e^{-u})}\right)
 \tag{305}
\]
can be verified by differentiating in \(u\) and using (304).
At \(u=0\) it has the specified initial value. The differentiated
functions lie in the operator domain at finite \(u\): their derivatives
are polynomials times an exponential of nonpositive real part, hence
square-integrable for the Gamma density. More explicitly, multiplying
by the radial oscillator ground Gaussian and returning to the three
original selected-mode coordinates gives a smooth Schwartz function
of those coordinates, in the original oscillator operator domain;
this fixes the radial endpoint domain rather than inferring it from
integrability alone. Uniqueness of the
self-adjoint semigroup evolution proves (305). Its prefactor has
modulus at most one, and the real part of its exponential coefficient
is \(-\beta^2e^{-u}(1-e^{-u})/
[1+\beta^2(1-e^{-u})^2]\le0\).

Take \(u=t\lambda_j\) in (305) and multiply by \(e^{-is_jq}\).
Its prefactor tends to one, while its exponential coefficient tends to
\(i\alpha-c_\Gamma b_0^2t\), because
\[
 1-e^{-t\lambda_j}\sim t\lambda_j,\quad
 \beta_j(1-e^{-t\lambda_j})\to0,\quad
 s_j\beta_j(1-e^{-t\lambda_j})\to c_\Gamma b_0^2t.
 \tag{306}
\]
For \(t=0\) the same limits are exact directly. The subtracted centered
term is
\((1-i\beta_j)^{-k}e^{-is_jq}\); its \(q^m\)-weighted norm is
\((1+\beta_j^2)^{-k/2}\sqrt{(k)_{2m}}\to0\).
The uncentered expression and its limit have modulus at most one.
Dominated convergence against \(q^{2m}\rho\), whose integral is
\((k)_{2m}\), proves
\[
 q^m U_{s_j}^{-1}e^{-t\lambda_jN}
       \{e^{i\beta_jq}-(1-i\beta_j)^{-k}\}
 \longrightarrow q^m e^{i\alpha q-c_\Gamma b_0^2tq}
 \quad\hbox{in }L^2(\rho),\qquad m\ge0.
 \tag{307}
\]
The estimates are uniform for bounded \(\alpha,t\). Equivalently one
can combine ordinary strong convergence and the domination bound with
the split
\(R^{2m}\|\text{unweighted error}\|^2
+4\int_{q>R}q^{2m}d\rho\).

Combining (302),(307), the exact radial coordinate map and demodulation
therefore identifies the actual operator \(jR_g\) on finite carrier
time-orbit vectors with
\[
 R_\infty=c_\Gamma Q,\qquad
 H_{b_0}=c_\Gamma b_0^2Q=b_0^2R_\infty .
 \tag{308}
\]
For a precise common-coordinate statement, first transport by
\(\mathcal B_{g_j}\), then use the orthogonal mode/Gaussian radial
isometry on its comparison vector and demodulate by \(U_{s_j}^{-1}\).
The norm error between the actual transported vector and this
comparison vector tends to zero by (302). The other modes remain in
their normalized vacuum factors. Thus the varying number of other
modes introduces no unidentified Hilbert-space map in the stated
Gram and operator limits.

For nonnegative times \(u,v\), offsets \(\alpha,\delta\), and an
integer \(m\ge0\), the complete limiting insertion is
\[
 \boxed{
 \left\langle e^{-uH_{b_0}}e^{i\alpha q},
            R_\infty^m e^{-vH_{b_0}}e^{i\delta q}\right\rangle
 =\frac{c_\Gamma^m(k)_m}
 {[1+c_\Gamma b_0^2(u+v)+i(\alpha-\delta)]^{k+m}} .
 }
 \tag{309}
\]
This follows by integrating \(c_\Gamma^mq^m\) against the original Gamma
density. Its real denominator part is positive, fixing the complex
power. The same limit for actual insertions follows from (302),(307)
and Cauchy--Schwarz. In particular it retains their imaginary parts.

The multiplication operator \(c_\Gamma Q\) is nonconstant, positive and
self-adjoint on
\(\{f:\int q^2|f|^2d\rho<\infty\}\): its nonreal resolvents are
the bounded multipliers \((c_\Gamma q-z)^{-1}\), and testing the adjoint on
compactly supported functions proves maximality of this domain.
The carrier time-orbit vectors, together with their modulations, are
dense. For example the functions \(e^{i\alpha q}\) are total:
orthogonality makes the Fourier transform of the finite density
\(\overline f\,d\rho\) zero. Extend that integrable density by
zero to the negative real axis, and convolve it with a Gaussian.
The Gaussian Fourier integral and Fubini express the convolution
as the integral of the zero Fourier transform times a Gaussian
multiplier, so every such convolution vanishes. Gaussian
convolutions approach the original density in \(L^1\): uniform
continuity and Gaussian tails prove this first for continuous
compactly supported functions, and density with the \(L^1\)
contraction bound proves the general case. Thus \(f=0\).
The same argument for the finite measure
\((1+q^{2m})d\rho\) proves that the modulation span is a
core for the maximal multiplication domain of \(Q^m\).
Formula (309) specifies the operator correspondence on the tested
polynomial domains, rather than only its expectation in one vector.
It does not assert convergence of arbitrary interspersed unbounded
products or identify a continuum local field algebra.

For the actual first carrier energy, (289),(303) give
\[
 q_{A_j}[v_{g_j}(\beta_j)]
 =\beta_j^2\langle R_{g_j}\rangle
 \longrightarrow k c_\Gamma b_0^2.
 \tag{310}
\]
Indeed \(\beta_j^2\lambda_j\to c_\Gamma b_0^2\), while
\(\beta_j^2|\langle R_{g_j}\rangle-\lambda_j k|
\le\beta_j^2j^{-5}\to0\). This proves the previously unavailable
unbounded first moment at physical time zero.

Finally, for \(s_j=b_0\sqrt j\), (288) gives the unchanged-regulator
realization
\[
 jR_{g_j}
 =\frac{B_{s_j}^{-1}A_jB_{s_j}
        +B_{-s_j}^{-1}A_jB_{-s_j}-2A_j}{2b_0^2}.
 \tag{311}
\]
It explains exactly in which sense this nonconstant multiplier is a
rescaled electric-energy observable.

### 22.8. The vacuum image and its entire raw limiting measure

The vacuum cannot be discarded when extending the observable algebra.
At each fixed \(j\), (296),(297) prove
\[
 \mathcal B_g
   \{j(R_g-\langle R_g\rangle)\psi_g\}
 \longrightarrow c_j(q-k)\Phi_0.
 \tag{312}
\]
The exact Laguerre identity \(N(q-k)=q-k\) and
\(\int(q-k)^2d\rho=k\) show that the complete comparison raw excitation
measure of this vector is
\[
 k c_j^2\,\delta_{\lambda_j}.
 \tag{313}
\]
This is a spectral-vector calculation: all other oscillator factors
are in their vacuum, and \(q-k\) is exactly its first radial Laguerre
eigenvector up to sign and norm.

The strong vector convergence (312) and finite spectral projection
convergence imply weak convergence of the actual raw measure to
(313) at fixed \(j\), including its total mass. To check tightness,
choose a finite comparison spectral cutoff containing this
eigenvector. Its limiting omitted mass is zero, while total masses
converge by (312). The actual omitted mass then tends to zero.
Finite cluster projections and their converging energies determine
every bounded continuous test. This repeats the exact argument used
for the bounded-phase vectors, now with the separately proved
weighted strong vector convergence.

Add to stage \(j\)'s finite tests a bounded-Lipschitz error below
\(1/j\) between this actual measure and (313), and the corresponding
norm error below \(1/j\). These thresholds exist at every fixed
box by the preceding proof and can be included in the same positive
dyadic choice. Since \(\lambda_j\to0\) and \(c_j\to c_\Gamma\), the actual
centered vacuum images
\(w_j=j(R_{g_j}-\langle R_{g_j}\rangle)\psi_{g_j}\) then satisfy
\[
 \boxed{\nu_{w_j}\Longrightarrow k c_\Gamma^2\delta_0,\qquad
 \|w_j\|^2\to k c_\Gamma^2>0,\qquad
 \langle w_j,e^{-tA_j}w_j\rangle\to k c_\Gamma^2\quad(t\ge0).}
 \tag{314}
\]
Every finite \(w_j\) is exactly vacuum-orthogonal. It is nonzero:
\(R_g\) vanishes on an open region outside the cutoff support and
is strictly positive on an open set near a point where the selected
quadratic has nonzero derivative. Since \(\psi_g>0\), \(R_g\) cannot
have zero variance. This argument does not require a limiting norm
to establish finite-regulator nonzero states.

A representation retaining the vacuum \(\Omega\), this operator's
centered vacuum image \(w\), its inner products and its correlations
must have \(\langle\Omega,w\rangle=0\) and \(\|w\|^2=k c_\Gamma^2\).
If its Hamiltonian is nonnegative, (314) forces \(w\) into its kernel:
for any \(t>0\),
\(\int(1-e^{-tE})d\nu_w(E)=0\), and positivity makes the measure
supported at \(E=0\). Thus it has a second independent zero-energy
vector. Constant autocorrelation without retained orthogonality
would not imply this conclusion; orthogonality is part of the
operator/vacuum map just specified.

There is an exact relation to the previously constructed origin
modulation sector. In \(L^2(\rho)\),
\[
 \frac{e^{i\alpha q}-(1-i\alpha)^{-k}}{i\alpha}
       \longrightarrow q-k\qquad(\alpha\to0).
 \tag{315}
\]
The inequality \(|(e^{i\alpha q}-1)/\alpha|\le q\) and the finite
second Gamma moment prove strong convergence of its first term;
differentiating the Gamma integral gives the scalar derivative
\(k\). Hence the centered vacuum image of \(R_\infty=c_\Gamma Q\) is the
precise derivative of the origin modulation state. Its zero-energy
limit is consistent with that sector's already computed vanishing
physical-time generator.

The positive carrier result (308)--(310) is therefore an actual
nonconstant observable extension beyond the scalar unscaled
configuration cylinders. Its vacuum extension is equally explicit
and has the zero-energy consequence (314). Neither statement alone
constructs the desired local interacting four-dimensional theory;
they specify the maps, domains, moments and the exact obstruction
for this particular retained observable/state family.


### 22.9. Exact relation to the unchanged local cylinders

The retained configuration bridge uses the same original face-filling
map from Section 13. If a fixed coarse index \(k_0\) divides \(j\),
replace a coarse edge by the ordered product of \(j/k_0\) fine
links. Its physical endpoints agree because
\(a_j(j/k_0)n=a_{k_0}n\). No noncommuting factors are reordered.
On the cofinal subsequence \(j=n!\), this gives every fixed coarse
index eventually. The vacuum estimate in (107), with
\(m=j/k_0\) and \(\sqrt{N_jM_j}\le18\sqrt5j^6\), gives
\[
\int\|I-U_p\|_{\rm HS}^2\,d(p_{k_0,j})_*\mu_j
\le\frac{216\sqrt5}{k_0^2}g_j^2j^8
\le\frac{216\sqrt5}{k_0^2j^2}.
\tag{316}
\]
All elementary coarse faces therefore become flat in every
subsequential compact configuration limit. Equation (110)
identifies all such flat fields as
\(U_e=q_{s(e)}^{-1}q_{t(e)}\), with one fixed root value.
They form one compact vertex-gauge orbit. Haar averaging on that
orbit is its unique invariant probability: the gauge average
of a continuous function is constant on the transitive orbit,
and integration against any invariant probability gives that
same constant. Thus all subsequential vacuum measures have the
same limit. Every fixed continuous gauge-invariant cylinder
\(F_j=F\circ p_{k_0,j}\) consequently satisfies
\[
\|(F_j-F(I))\psi_j\|\longrightarrow0 .
\tag{317}
\]
The full nonlinear semigroup domination (299) gives, for a finite
carrier time-orbit combination
\(w_j=\sum_\ell a_\ell e^{-t_\ell A_j}v_j(\beta_{j,\ell})\),
\[
\|(F_j-F(I))w_j\|
\le2\sum_\ell|a_\ell|\,\|(F_j-F(I))\psi_j\|
\longrightarrow0 .
\tag{318}
\]
The same inequality includes any finite collection of bounded
phase carriers. Their limiting cylinder representation is exactly
\(F\mapsto F(I)I\); this is a unital star representation because
evaluation preserves sums, products and conjugation. Its norm
bound by \(\|F\|_\infty\) extends it to the uniform closure.

Equations (308)--(315) now give a concrete observable extension
beyond (318): \(jR_g\) acts by the nonconstant \(c_\Gamma Q\)
on a carrier sector, has the complete polynomial insertion
kernel (309), and its centered vacuum image has the positive
zero-energy raw measure (314). The original phase coordinate
uses a selected global transverse mode, so this result does not
identify \(R_g\) with a spatial local electric or curvature
field. No interchange of an unbounded multiplier with (318)
was used; its tails and weighted limits were proved separately.
The original native magnetic covariance and either prescribed
running-coupling trajectory remain different, unresolved
continuum calculations.
