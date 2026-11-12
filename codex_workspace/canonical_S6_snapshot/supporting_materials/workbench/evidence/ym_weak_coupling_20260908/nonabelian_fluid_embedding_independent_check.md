# Non-Abelian fluid encoding: exact inverse, curvature and current

9 September 2026. Independent calculation of the non-Abelian connection
proposed in the interacting tensor-band continuation. This note proves
identities for the original fluid field, rather than replacing it with a
different profile. The identities do not themselves construct a quantum
vacuum or a continuum spectral measure.

## 1. Spaces, coefficients and inverse

Let \(I\) be an open time interval and let
\(u\in C^\infty(I\times\mathbb R^3;\mathbb R^3)\) satisfy
\(\sum_i\partial_i u_i=0\). Spatial support is assumed compact whenever
an integral over all of \(\mathbb R^3\) is used. All pointwise identities
below require no support assumption. Retain
\(c>0\), \(g>0\), \(\lambda\in\mathbb R\setminus\{0\}\),
\(X^0=cs\), \(X^i=x^i\), and the metric
\(\eta=\operatorname{diag}(-1,1,1,1)\).

For the Pauli matrices \(\sigma_a\), put \(T_a=-i\sigma_a/2\).
Then
\[
 [T_a,T_b]=\sum_d\varepsilon_{abd}T_d,\qquad
 -2\operatorname{tr}(T_aT_b)=\delta_{ab}.
 \tag{1}
\]
Consequently the coefficient vector of
\([v\cdot T,w\cdot T]\) is \(v\times w\). We use this specified
identification of the color basis with the oriented Cartesian basis
\((e_1,e_2,e_3)\) throughout.

Define a connection by its coefficient vectors:
\[
 \mathbf A_0=0,\qquad
 \mathbf A_i=\lambda e_i\times u,\qquad
 A_\mu=\mathbf A_\mu\cdot T.
 \tag{2}
\]
This is an injective linear map from the stated fluid fields to a
specified subspace of smooth connections. Its inverse on that image is
\[
 u=-\frac1{2\lambda}\sum_i e_i\times\mathbf A_i.
 \tag{3}
\]
Indeed,
\(\sum_i e_i\times(e_i\times u)=\sum_i(u_i e_i-u)=-2u\).
This is an inverse in the displayed representative and frame, not an
assertion that the same formula descends to all gauge-equivalence classes.

There is also an exact correspondence with the earlier Cartan encoding
\(C_0=0,\ C_i=\lambda u_iT_3\). Recover
\(u_i=-2\operatorname{tr}(T_3C_i)/\lambda\), then use (2).
Conversely apply (3), then set \(C_i=\lambda u_iT_3\).
Both compositions are the identity on their respective specified images.
The two encodings are thus explicitly related without identifying their
curvature or their dynamics.

## 2. Full curvature

Use
\[
 F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu+[A_\mu,A_\nu],
 \quad
 \mathbf E_i=\mathbf F_{0i},\quad
 \mathbf B_i=\tfrac12\sum_{j,k}\varepsilon_{ijk}\mathbf F_{jk}.
 \tag{4}
\]
The temporal term and the unreduced magnetic components are
\[
 \mathbf E_i=\frac{\lambda}{c}e_i\times u_s,\qquad
 B_i^a=\lambda(\partial_a u_i-\delta_{ia}\operatorname{div}u)
                    +\lambda^2u_i u_a.
 \tag{5}
\]
To verify the second formula, expand (4) and use
\[
 \sum_k\varepsilon_{ijk}\varepsilon_{akb}
       =\delta_{ib}\delta_{ja}-\delta_{ia}\delta_{jb},
 \quad
 ((e_j\times u)\times(e_k\times u))_a
       =\sum_b\varepsilon_{jkb}u_bu_a,
 \quad
 \tfrac12\sum_{j,k}\varepsilon_{ijk}\varepsilon_{jkb}=\delta_{ib}.
 \tag{6}
\]
For the original incompressible field this gives exactly
\[
 \boxed{\,B_i^a=\lambda\partial_a u_i+\lambda^2u_i u_a\,}.
 \tag{7}
\]
In particular the commutator is retained:
\[
 [A_i,A_j]=\lambda^2\sum_k\varepsilon_{ijk}u_k\,(u\cdot T).
 \tag{8}
\]
If \(u\ne0\) at a point, some \(u_k\ne0\), and (8) is nonzero for
the complementary oriented pair. This encoding does not take values
in one fixed commuting color line.

## 3. Pointwise and integrated curvature norms

The coefficient norm is exactly the norm from (1). Expanding all terms
in (7) gives
\[
 \begin{aligned}
 |\mathbf B|^2
 &=\lambda^2\sum_{i,a}(\partial_a u_i)^2
   +2\lambda^3\sum_{i,a}u_i u_a\partial_a u_i+\lambda^4|u|^4\\
 &=\lambda^2|\nabla u|^2+
   \lambda^3\operatorname{div}(|u|^2u)+\lambda^4|u|^4 .
 \end{aligned}
 \tag{9}
\]
The last equality uses
\(\operatorname{div}(|u|^2u)=
 2\sum_{i,a}u_i u_a\partial_a u_i+|u|^2\operatorname{div}u\).
Compact spatial support therefore implies
\[
 \boxed{\ \int|\mathbf B|^2dx
  =\lambda^2\|\nabla u\|_2^2+\lambda^4\|u\|_4^4.\ }
 \tag{10}
\]
All boundary terms vanish because their integrands are compactly
supported. Also
\[
 \int|\operatorname{curl}u|^2dx
 =\int\sum_{i,a}(\partial_a u_i)^2dx
   -\int\sum_{i,a}\partial_a u_i\,\partial_i u_a\,dx
 =\|\nabla u\|_2^2,
 \tag{11}
\]
because integration by parts turns the last sum into
\(\int(\operatorname{div}u)^2dx=0\).

There is a pointwise estimate which does not discard the derivative
term in (9). Regard \(B=(B_i^a)\) as a real \(3\)-by-\(3\) matrix.
Its trace is \(\lambda^2|u|^2\). Frobenius Cauchy--Schwarz gives
\[
 (\lambda^2|u|^2)^2=|\langle B,I_3\rangle_F|^2
 \le 3|B|^2,\qquad
 \boxed{\,|B|^2\ge \lambda^4|u|^4/3\,}.
 \tag{12}
\]
Equality holds precisely when
\[
 \partial_a u_i=
 \lambda\bigl(|u|^2\delta_{ia}/3-u_i u_a\bigr).
 \tag{13}
\]
The electric identity is
\[
 \sum_i|\mathbf E_i|^2
 =\frac{\lambda^2}{c^2}\sum_i(|u_s|^2-(u_s)_i^2)
 =\frac{2\lambda^2}{c^2}|u_s|^2.
 \tag{14}
\]
Thus, if the specified classical energy convention is
\(\mathcal E=(2g^2)^{-1}\int(|\mathbf E|^2+|\mathbf B|^2)dx\),
its value on (2) is exactly
\[
 \mathcal E=
 \frac{\lambda^2}{g^2c^2}\|u_s\|_2^2+
 \frac{\lambda^2}{2g^2}\|\operatorname{curl}u\|_2^2+
 \frac{\lambda^4}{2g^2}\|u\|_4^4.
 \tag{15}
\]
The factor \(2\) in (14) and the factor \(1/3\) in (12) depend on
the displayed dimensions and norm; neither is suppressed.

## 4. Full current and its Gauss component

Define the induced current, without imposing that it vanish, by
\[
 D^\mu F_{\mu\nu}=g^2j_\nu,\qquad
 D_\mu V=\partial_\mu V+[A_\mu,V].
 \tag{16}
\]
Write \(\boldsymbol\omega=\operatorname{curl}u\) and
\(C=(u\cdot\nabla)u\). Direct substitution gives
\[
 \boxed{\ g^2\mathbf j_0
 =-\frac{\lambda}{c}\operatorname{curl}u_s
  -\frac{\lambda^2}{c}u\times u_s.\ }
 \tag{17}
\]
Indeed \(F_{i0}=-F_{0i}\), so the derivative part is
\(-(\lambda/c)\sum_i e_i\times\partial_i u_s\).
The commutator part uses the exact identity
\(\sum_i(e_i\times u)\times(e_i\times v)=u\times v\).
Equation (17) is the lower-index component; \(j^0=-j_0\).

For each \(i\), the complete spatial expression is
\[
 \begin{aligned}
 g^2\mathbf j_i={}&-\frac{\lambda}{c^2}e_i\times u_{ss}
                  -\lambda\nabla\omega_i\\
 &-\lambda^2\left[
       2\omega_i u+
       \sum_{j,k}\varepsilon_{ijk}u_k\partial_j u+
       e_i\times C\right]
       -\lambda^3|u|^2(e_i\times u).
 \end{aligned}
 \tag{18}
\]
Here \(\nabla\omega_i\) is the color coefficient vector whose component
\(a\) is \(\partial_a\omega_i\). For a complete sign check, first use
\(F_{ji}=-\sum_k\varepsilon_{ijk}B_k\) to obtain
\[
 g^2\mathbf j_i=
 -\frac{\lambda}{c^2}e_i\times u_{ss}
 -\sum_{j,k}\varepsilon_{ijk}
       [\,\partial_j\mathbf B_k+
               \lambda(e_j\times u)\times\mathbf B_k\,].
 \tag{19}
\]
Then (7) and the vector triple-product identity give
\[
 \begin{aligned}
 \partial_j\mathbf B_k+\lambda(e_j\times u)\times\mathbf B_k
 ={}&\lambda\nabla\partial_j u_k\\
 &+\lambda^2[\,2(\partial_j u_k)u+
                u_k\partial_j u-e_j C_k\,]\\
 &+\lambda^3[\,u_j u_k u-|u|^2u_k e_j\,].
 \end{aligned}
 \tag{20}
\]
Contract (20) using
\(\sum_{j,k}\varepsilon_{ijk}u_j u_k=0\) and
\(\sum_{j,k}\varepsilon_{ijk}e_jv_k=-e_i\times v\).
This proves every term of (18). In particular the coefficient \(2\)
comes from two different terms, the derivative of the quadratic
magnetic part and the commutator with its linear part.

Covariant conservation also holds with these same conventions:
\[
 g^2D^\nu j_\nu
 =D^\nu D^\mu F_{\mu\nu}
 =\tfrac12[D^\nu,D^\mu]F_{\mu\nu}
 =\tfrac12[F^{\nu\mu},F_{\mu\nu}]=0.
 \tag{21}
\]
The second equality follows by exchanging the two summed indices
and using antisymmetry. In the specified diagonal metric each term
in the last sum is the commutator of a scalar multiple of
\(F_{\mu\nu}\) with itself, and vanishes.

## 5. Substitution of the original viscous fluid equation

Suppose the same field satisfies the smooth forced incompressible
Navier--Stokes equation before its terminal time:
\[
 u_s+(u\cdot\nabla)u-\nu\Delta u+\nabla p=f,\qquad \nu>0.
 \tag{22}
\]
Define, with every original term retained,
\[
 N=\nu\Delta u-(u\cdot\nabla)u-\nabla p+f.
 \tag{23}
\]
Then \(u_s=N\) and direct differentiation gives
\[
 u_{ss}=\nu\Delta N-(N\cdot\nabla)u-(u\cdot\nabla)N
                       -\nabla p_s+f_s.
 \tag{24}
\]
Putting (23)--(24) into (17)--(18) is the exact fluid-to-current
map; it keeps viscosity, pressure, both differentiated transport
terms, forcing, color commutators and the nonzero Gauss component.
No equation in (22) sets (17) or (18) to zero.

The released positive-viscosity construction is an eligible input on
each smooth preterminal interval: see OpenAI, *Finite time blowup for
Navier--Stokes*, [paper and formal source](https://openai.com/index/navier-stokes-solution/).
Equations (10), (14), and (17)--(24) specify what must be evaluated on
that actual field. They do not identify the fluid's smooth external
force with a smooth gauge current at a singular endpoint.

The current is derived from the connection, not removed. In particular
the non-Abelian quartic magnetic term in (10) is a proved feature of
the map; a source-free quantum spectrum is not a consequence of that
identity alone.

## 6. An exact right inverse for non-Abelian curvature samples

The quartic term also gives a direct construction, independent of the
singular fluid profile. Let \(\mathsf E\) be any finite set of original
cubic-grid edges of physical spacing \(a>0\), and let \(p_e\) be their
distinct midpoints. Given arbitrary real weights \(h_e\ge0\), we now
construct a smooth compactly supported incompressible field \(U_h\)
such that the connection (2) satisfies
\[
 \sum_i|\mathbf B_i[U_h](p_e)|^2=h_e\qquad(e\in\mathsf E).
 \tag{25}
\]
This is a right inverse of the explicitly defined finite sampling
map, not a substitution for the released blowup solution.

Set \(\rho=a/8\). Distinct edge midpoints are separated by at least
\(a/\sqrt2\): in lattice units each has precisely one half-integer
coordinate; either their half-integer positions coincide and a
nonzero difference has size at least one, or two coordinates differ
by at least \(1/2\). Thus the closed radius-\(\rho\) balls are disjoint.

Define \(b(t)=e^{-1/t}\) for \(t>0\), and \(b(t)=0\) for \(t\le0\).
All derivatives of its positive branch tend to zero at zero, because
each is a polynomial in \(1/t\) times \(e^{-1/t}\); hence \(b\) is
smooth. For \(r_e=x-p_e\), put
\[
 \chi_e(x)=
 \frac{b(1-|r_e|^2/\rho^2)}
 {b(1-|r_e|^2/\rho^2)+b(|r_e|^2/\rho^2-1/4)},\qquad
 v_e=\frac{h_e^{1/4}}{|\lambda|}e_3 .
 \tag{26}
\]
The denominator is positive everywhere: both terms could vanish only
if \(|r_e|^2/\rho^2\ge1\) and \(|r_e|^2/\rho^2\le1/4\)
simultaneously. The cutoff equals one for \(|r_e|\le\rho/2\)
and zero for \(|r_e|\ge\rho\).

Set
\[
 V_h(x)=\frac12\sum_{e\in\mathsf E}\chi_e(x)(v_e\times r_e),
 \qquad U_h=\operatorname{curl}V_h .
 \tag{27}
\]
The sum is finite and smooth with compact support. Antisymmetry of
the curl and commutation of second derivatives give
\(\operatorname{div}U_h=0\). In the radius-\(\rho/2\) ball at \(p_e\)
only that summand remains, and its cutoff is one. Componentwise,
\[
 \bigl(\operatorname{curl}(v\times r)\bigr)_i
 =\sum_{j,k,b,d}\varepsilon_{ijk}\varepsilon_{kbd}
          v_b\partial_j r_d
 =\sum_{j,k,b}\varepsilon_{ijk}\varepsilon_{kbj}v_b=2v_i.
 \tag{28}
\]
Therefore \(U_h=v_e\), \(\nabla U_h=0\) throughout that inner ball.
By (7),
\[
 B_i^a[U_h](p_e)=\lambda^2(v_e)_i(v_e)_a,\qquad
 \sum_{i,a}|B_i^a[U_h](p_e)|^2
       =\lambda^4|v_e|^4=h_e.
 \tag{29}
\]
This proves (25). If \(h_e>0\), the sampled magnetic field is
entirely the retained commutator term, not a derivative term in a
commuting encoding. The fourth root is the stated set-map on
nonnegative weights; differentiability in \(h\) at a zero weight
is not asserted.

For completeness these fields occur in explicit regular forced
Navier--Stokes flows for every prescribed \(\nu>0\).
Let \(\theta\in C_c^\infty((0,\infty);\mathbb R)\) equal one on
a nonempty time interval and put
\[
 u(s,x)=\theta(s)U_h(x),\quad p(s,x)=0,\quad
 f(s,x)=\theta'(s)U_h(x)+
       \theta(s)^2(U_h\cdot\nabla)U_h(x)
       -\nu\theta(s)\Delta U_h(x).
 \tag{30}
\]
Direct substitution proves (22), with zero initial velocity and
smooth compact spacetime forcing. The velocity and force are defined
through the time plateau and thereafter; no endpoint singularity is
introduced. On the plateau, at each sampled point, (17)--(18) give
\[
 \mathbf j_0(p_e)=0,\qquad
 g^2\mathbf j_i(p_e)=
       -\lambda^3|v_e|^2(e_i\times v_e).
 \tag{31}
\]
Thus the gauge source remains explicit even where the fluid is
locally constant. Formula (30) depends on the prescribed weights and
the grid spacing. Neither fixed forcing across regulators nor a
source-free field equation is claimed.
