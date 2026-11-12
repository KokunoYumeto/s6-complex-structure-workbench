# Retained cusp coordinates and nonlinear gauge-field integration

Research calculation, 8 September 2026. This document proves the maps below;
it does not claim a quantum mass-gap counterexample. All couplings are retained.

## 1. Exact original metric and nonlinear action

Use precisely the period data in the compact-link manuscript, with
\(L=\operatorname{Im}\tau\), \(m=\operatorname{Im}\mu\),
\(q=-\operatorname{Im}\beta\), and \(D=Lq+6m^2>0\). Define
\[
A=\begin{pmatrix}6\operatorname{Re}\mu&\operatorname{Re}\tau\\
\operatorname{Re}\beta&\operatorname{Re}\mu\end{pmatrix},\qquad
B=\begin{pmatrix}6m&L\\-q&m\end{pmatrix}.
\]
The original physical coordinate order is \((x_1,x_2,x_3,x_4)\).
Let \(R(x_1,x_2,x_3,x_4)=(x_1,x_3,x_2,x_4)\); \(R\) is orthogonal,
\(\det R=-1\), and it is only a recorded permutation, not a replacement
of any period. For the original cover matrix \(P_M=P\operatorname{diag}(1,1,M,M)\),
\[
 Q:=RP_M=\begin{pmatrix}A&MI_2\\B&0\end{pmatrix},\qquad
 Q^{-1}=\begin{pmatrix}0&B^{-1}\\M^{-1}I_2&-M^{-1}AB^{-1}\end{pmatrix},
\quad B^{-1}=D^{-1}\begin{pmatrix}m&-L\\q&6m\end{pmatrix}.
\]
Multiplying the two displayed block matrices gives the identity on both
sides, which proves the inverse including all signs. Consequently, writing
\(K=B^{-1}B^{-\mathsf T}\),
\[
G^{-1}=(P_M^{\mathsf T}P_M)^{-1}
=\begin{pmatrix}
K&-M^{-1}KA^{\mathsf T}\\
-M^{-1}AK&M^{-2}(I_2+AKA^{\mathsf T})
\end{pmatrix},
\]
where
\[
K=D^{-2}\begin{pmatrix}
m^2+L^2&mq-6mL\\mq-6mL&q^2+36m^2
\end{pmatrix},\qquad \det K=D^{-2}.
\]
Indeed \(G^{-1}=Q^{-1}Q^{-\mathsf T}\). The determinant is
\(\det P_M=-M^2D\), and physical volume is \(\mathcal D=M^2D\).
The sign of the original orientation and the positive volume density are
recorded separately.

For each ordered pair \(I=(i,j)\), \(1\leq i<j\leq4\), define the full
six-by-six two-form metric
\[
\mathcal K_{(i,j),(k,l)}=(G^{-1})_{ik}(G^{-1})_{jl}
                         -(G^{-1})_{il}(G^{-1})_{jk}.
\]
Every entry, including entries with \((i,j)\ne(k,l)\), is retained. This
is the Gram matrix of the six covectors \(dy^i\wedge dy^j\); it is positive
definite because the exterior-square map of the invertible matrix
\(P_M^{-\mathsf T}\) is invertible. In particular
\(\mathcal K_{12,12}=D^{-2}\), without imposing \(A=0\) or \(m=0\).

Take gauge group \(SU(n)\), \(n\geq2\), with the original invariant
inner product \(c(X,Y)=-\tfrac12\operatorname{tr}(XY)\) on anti-Hermitian
trace-free matrices. For a connection \(\mathscr A=\sum_\alpha
\mathscr A_\alpha dx^\alpha\), the coordinate map
\(\phi_M(y)=[P_My]\) gives
\[
 \widetilde{\mathscr A}_i(y)=\sum_\alpha(P_M)_{\alpha i}
                       \mathscr A_\alpha(P_My),\qquad
 \widetilde F_{ij}=\partial_i\widetilde{\mathscr A}_j
  -\partial_j\widetilde{\mathscr A}_i
  +[\widetilde{\mathscr A}_i,\widetilde{\mathscr A}_j]
 =\sum_{\alpha,\beta}(P_M)_{\alpha i}(P_M)_{\beta j}
                       F_{\alpha\beta}(P_My).
\]
The derivative identity is the chain rule; the commutator identity follows
by bilinearity of the matrix commutator. No bracket has been omitted.
Changing variables in the original action gives exactly
\[
 S(\mathscr A)=\frac1{2g_{\rm YM}^2}\int |F_{\mathscr A}|^2dx
 =\frac{M^2D}{2g_{\rm YM}^2}\int_{[0,1)^4}
   \sum_{I,J}\mathcal K_{I,J}\,c(\widetilde F_I,\widetilde F_J)\,d^4y.
\]
For the previously displayed flux \(\widetilde F_{12}=2\pi H\),
\(H=\operatorname{diag}(i,-i)\), \(c(H,H)=1\), all other curvature
components zero, this is \(2\pi^2M^2/(g_{\rm YM}^2D)\).
For general connections it is the full mixed quadratic form in their
nonlinear curvatures, not six independent scalar plaquette weights.

Gauge maps obey the original convention
\(\mathscr A^h=h^{-1}\mathscr A h+h^{-1}dh\). Pullback commutes with
this expression, with \(\widetilde h=h\circ\phi_M\). Along every path,
the parallel-transport ODE with coefficient \(-\mathscr A(\dot\gamma)\)
is carried to the identical ODE under \(\phi_M\). Thus both ordered
holonomies and their traces are preserved, including nonlinear dependence
on the connection. This supplies the gauge and observable maps alongside
the metric and action maps.

## 2. Exact local transport of full nonlinear fields through the cusp limit

Retain \(B_T=TJ+C_T\), where
\(J=\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)\),
\(\sup_T\|C_T\|_{\rm op}\leq C\). Each covered period, in the recorded
permuted physical order, is
\[
 \lambda(n,z)=(A_Tn+Mz,B_Tn),\qquad n,z\in\mathbb Z^2.
\]
Its original-order value is \(R^{\mathsf T}\lambda(n,z)\); since \(R\)
is orthogonal, the following norms have exactly their original values.
If \(n\ne0\), its length is at least \((T-C)|n|\geq T-C\).
If \(n=0\) and the period is nonzero, its length is \(M|z|\geq M\).
Thus \(\operatorname{sys}(\widetilde F_{T,M})\geq\min(T-C,M)\).

Let \(\mathscr A\in C_c^\infty(\mathbb R^4;
T^*\mathbb R^4\otimes\mathfrak{su}(n))\) have support in \(B_R(0)\).
For \(\operatorname{sys}>8R\), the quotient map restricts to an
isometric embedding of \(B_{2R}\): for \(x,y\in B_{2R}\) and a
nonzero period \(\lambda\),
\[
 |x-y+\lambda|\geq|\lambda|-|x-y|>8R-4R\geq|x-y|.
\]
Transport \(\mathscr A\) by this embedding and extend it by zero outside
the image of \(B_{2R}\). It is smooth since \(\mathscr A\) is identically
zero on a neighborhood of the boundary. Denote the resulting connection
on the trivial bundle by \(\iota_{T,M}\mathscr A\). Then
\[
 F_{\iota\mathscr A}=\iota(d\mathscr A+\mathscr A\wedge\mathscr A),
 \qquad S(\iota\mathscr A)=S(\mathscr A).
\]
Both identities follow on the embedded ball from the chain rule and the
unchanged Euclidean metric; on the complement both sides vanish. The
Yang--Mills differential expression \(d_{\mathscr A}^*F_{\mathscr A}\)
is transported identically for the same reason. These statements concern
arbitrary compactly supported connections, not only a flat background or
its Hessian. They do not assert the existence of a nonzero compactly
supported solution of the Yang--Mills equation.

A smooth gauge transformation equal to the identity outside \(B_R\)
extends by the identity in precisely the same manner, and
\(\iota(\mathscr A^h)=(\iota\mathscr A)^{\iota h}\). Wilson traces along
paths in \(B_{2R}\) agree by uniqueness of the transport ODE. Given a
finite collection of such fields, variations and paths, one common \(R\)
makes all these identities simultaneous. Thus the covered cusp supplies
exact local transports of the full interacting classical field data on
every fixed bounded domain. The probability distribution on those data
is a separate calculation, performed at a finite regulator below.

## 3. Every finite link field has a smooth-connection realization

Fix the embedded finite cubical graph on one covered torus. Give each
geometric edge one orientation and use inverse parallel transport as the
link convention. For arbitrary \(U_e\in SU(n)\), choose
\(X_e\in\mathfrak{su}(n)\) with \(\exp X_e=U_e\). Such a choice exists:
unitarily diagonalize \(U_e\), choose real eigenangles whose sum is an
integer multiple of \(2\pi\), and change one angle by that multiple so
their sum is zero. Conjugating the diagonal imaginary angles back gives
the required trace-free anti-Hermitian logarithm.

Select a closed subinterval in the interior of each edge. These finitely
many subintervals admit disjoint tubular neighborhoods, each disjoint from
all other edges. In tube coordinates \((s,z)\), choose smooth functions
\(b_e(s)\), \(\rho_e(z)\), supported away from the tube boundary, with
\(\int b_e(s)ds=1\) and \(\rho_e(0)=1\). Set
\[
 \mathscr A=\sum_e X_e b_e(s)\rho_e(z)\,ds,
\]
extending each summand by zero. This is a global smooth connection on the
trivial bundle. Along edge \(e\) its coefficient commutes with itself at
different times, so ordinary parallel transport is \(\exp(-X_e)\), and
inverse parallel transport is exactly \(U_e\). All other summands vanish
on that edge. The continuum-to-link map is therefore surjective for this
finite graph.

This proof does not assert a globally continuous choice of logarithms or
an action-preserving right inverse. It gives an exact realization of every
link configuration, including the previously printed flux. For the latter,
the displayed logarithms lie in the same Cartan line, so the constructed
connection is globally Abelian and its total real curvature period on a
closed two-torus is zero by Stokes' theorem. The nonzero principal
plaquette logarithms still agree with the printed links: exponentiation
does not determine the integral curvature outside the finite graph.
The next explicit vertex-frame calculation relates the original
constant-curvature bundle connection to these printed links as well;
it does not identify the two smooth connections or their actions.

On the original magnetic line-sum bundle, retain the lifted connection
\(d+2\pi u_1Hdu_2\) and transition
\(G_k(u)=\exp(-2\pi k_1u_2H)\). Choose vertex representatives
\(u_j=n_j/N\) in the half-open fundamental cube (and \(u_3=Mn_3/N\),
\(u_4=Mn_4/N\) on the cover). In those vertex frames, inverse transport is
\[
 W_1(n)=\begin{cases}I&n_1<N-1,\\
 e^{-2\pi Hn_2/N}&n_1=N-1,\end{cases}\quad
 W_2(n)=e^{2\pi Hn_1/N^2},\qquad W_3=W_4=I.
\]
For a non-wrapping first-direction edge the connection integral is zero.
For a wrapping first-direction edge it is also zero in the lift, but the
endpoint frame is changed by \(G_{(1,0,0,0)}\). Ordinary transport in the
chosen endpoint frame therefore has the additional factor
\(G_{(1,0,0,0)}^{-1}=e^{2\pi Hn_2/N}\), giving the stated inverse
transport. The second-direction integral is \(2\pi H n_1/N^2\);
its wrap transition is the identity because that transition has \(k_1=0\).
The remaining two directions have both zero integral and identity transition.

Set \(h(n)=e^{-2\pi Hn_1n_2/N^2}\) at these finitely many vertices,
with vertex indices always represented in \(\{0,\ldots,N-1\}\).
The gauge formula \(U_j(n)=h(n)^{-1}W_j(n)h(n+e_j)\) gives
\[
 U_1(n)=e^{-2\pi Hn_2/N^2},\qquad
 U_2(n)=\begin{cases}I&n_2<N-1,\\
 e^{2\pi Hn_1/N}&n_2=N-1,\end{cases}\qquad U_3=U_4=I.
\]
For the four nontrivial cases, the exponents after division by \(2\pi H\)
are respectively
\[
 \frac{n_1n_2-(n_1+1)n_2}{N^2}=-\frac{n_2}{N^2},\quad
 \frac{(N-1)n_2}{N^2}-\frac{n_2}{N}=-\frac{n_2}{N^2},
\]
\[
 \frac{n_1n_2+n_1-n_1(n_2+1)}{N^2}=0,\quad
 \frac{n_1(N-1)+n_1}{N^2}=\frac{n_1}{N}.
\]
The other vertex factors cancel. These are exactly the printed compact
flux links. Thus the original smooth magnetic connection does realize
that finite link field in explicitly related vertex frames. The auxiliary
smooth connection constructed by edge tubes also realizes it, and can have
a different action: finite holonomies do not determine a smooth connection.

## 4. One exact nonlinear integration step, with all neighboring staples

Take a finite four-dimensional orthogonal cubical regulator inside one of
the locally isometric domains, and the full \(SU(2)\) Wilson action
\[
 S_W(U)=\sum_p b_p(2-\operatorname{Re}\operatorname{tr}U_p),\qquad b_p>0.
\]
Each unordered geometric plaquette is included once. For constant mesh
spacing \(a\) and the Lie metric and continuum action of section 1,
\(b_p=1/(2g_{\rm YM}^2)\) has the classical continuum coefficient:
\(2-\operatorname{Re}\operatorname{tr}\exp(a^2F)=a^4c(F,F)+O(a^8)\)
for the displayed constant-curvature exponential. No assertion about a
quantum continuum limit follows from this classical coefficient matching.
The following exact integration works for arbitrary positive \(b_p\).

Keep all links except an interior link \(U_e\) fixed. There are six
incident plaquettes. Cyclic permutation inside the trace, and taking an
inverse when the plaquette uses \(U_e^{-1}\), write each contribution as
\(\operatorname{Re}\operatorname{tr}(U_e V_{ep})\), with
\(V_{ep}\in SU(2)\) the ordered product of its other three links. Define
\[
 H_e=\sum_{p\ni e}b_pV_{ep},\qquad
 r_e^2=\tfrac12\operatorname{tr}(H_eH_e^*)
 =\sum_{p\ni e}b_p^2+
   \sum_{p<q,\ p,q\ni e}b_pb_q\operatorname{Re}\operatorname{tr}(V_{ep}V_{eq}^*).
\]
All six coefficients and all fifteen pairwise traces remain present.
Every \(SU(2)\) matrix has the form \(a_0I+i\sum a_j\sigma_j\) with
real \(a_\alpha\) and \(\sum a_\alpha^2=1\). Consequently the real
linear combination \(H_e\) satisfies \(H_eH_e^*=r_e^2I\),
\(\det H_e=r_e^2\). When \(r_e>0\), the identity
\(H_e=r_eV_e\) defines \(V_e\in SU(2)\), with \(r_e\) retained as an
independent exact coefficient, not replaced by one. If \(r_e=0\),
\(H_e=0\) and the conditional link distribution is Haar.

Use Haar probability measure solely as the convention for finite integrals;
this does not change a physical period, field amplitude or coupling. Under
\(W=U_eV_e\), write \(w_0=\tfrac12\operatorname{tr}W\). The marginal
Haar density of \(w_0\in[-1,1]\) is
\(\tfrac2\pi(1-w_0^2)^{1/2}dw_0\), obtained by slicing the unit
three-sphere in four real quaternion coordinates. Therefore
\[
 Z(r):=\int_{SU(2)}e^{\operatorname{Re}\operatorname{tr}(UH)}dU
 =\frac2\pi\int_{-1}^1e^{2rs}\sqrt{1-s^2}\,ds
 =\sum_{k=0}^\infty\frac{r^{2k}}{k!(k+1)!}
 =\frac{I_1(2r)}r,\qquad Z(0)=1.
\]
To prove the series, integrate the exponential term by term (uniform
absolute convergence on the compact interval). Odd powers vanish, and
\(\int_{-1}^1s^{2k}\sqrt{1-s^2}ds
=\pi(2k)!/[2\,4^k k!(k+1)!]\), by the beta integral, or induction by
integration by parts from the area of a semicircle. This also defines the
Bessel expression without importing a special-function convention.

Writing \(B_e=\sum_{p\ni e}b_p\), integration of this link replaces
its incident action by exactly
\[
 2B_e-\log Z(r_e).
\]
The additive constant \(2B_e\) is retained. Other plaquette terms remain
unchanged. The series has nonnegative terms and converges for every finite
\(r\), so \(Z(r)>0\) and this logarithm is well-defined. This is an
explicit nonlinear map from six interacting plaquettes to an effective
interaction among their boundary links, not a Gaussian integration.

Differentiating the uniformly convergent series gives
\(Z'(r)=2I_2(2r)/r\) and \(Z''+3Z'/r=4Z\). Let
\(\eta(r)=I_2(2r)/I_1(2r)\). Then the exact conditional mean is
\[
 \mathbb E[U_e\mid U_{f\ne e}]=\eta(r_e)V_e^*,
\]
because transverse quaternion coordinates have zero mean, while
\(\mathbb E[w_0]=Z'/(2Z)=\eta\). Their second moments are
\[
 \mathbb E[w_0^2]=1-\frac{3\eta}{2r},\qquad
 \mathbb E[w_jw_k]=\delta_{jk}\frac{\eta}{2r}\quad(1\leq j,k\leq3),
 \quad \mathbb E[w_0w_j]=0.
\]
At \(r=0\) these have continuous values \(1/4\), since the displayed
series gives \(\eta(r)=r/2+O(r^3)\). The longitudinal variance is
\(1-3\eta/(2r)-\eta^2\); it has not been replaced by a harmonic width.
The gauge law \(U_e\mapsto g_s^{-1}U_eg_t\) sends
\(H_e\mapsto g_t^{-1}H_eg_s\); hence \(r_e\) is gauge invariant and
the conditional mean has exactly the same gauge law as \(U_e\).

## 5. Exact integration at the retained small-curvature background

Use an orthogonal physical cubical patch with common spacing \(a>0\),
not the generally skew period-coordinate mesh. On that patch take the
retained Abelian magnetic curvature in its physical magnetic two-plane,
\(F_{12}=\mathfrak bH\), \(\mathfrak b=2\pi/D_T\), with the other
components zero. In this paragraph indices 1 and 2 label an explicitly
chosen orthonormal frame of that two-plane, not the first two original
period-coordinate indices. The remaining two orthonormal directions are
in its orthogonal complement. This is the smooth magnetic background's
local curvature, pulled to a covered torus; its amplitude is unchanged by
the covering. A local potential is \(\mathscr A=\mathfrak b x_1Hdx_2\).
The inverse-transport convention gives every positively oriented magnetic
plaquette the holonomy \(\exp(\vartheta H)\), where
\(\vartheta=\mathfrak b a^2=2\pi a^2/D_T\), and gives the other
plaquettes the identity. This follows either by integrating this potential
on the four edges, whose coefficients commute, or by Stokes' theorem in
the fixed Cartan line.

Let all six incident plaquettes of an interior link in the magnetic plane
have the same retained Wilson coefficient \(b=1/(2g_{\rm YM}^2)>0\).
Write \(U_e^{(0)}\) for that background link. The two magnetic staples
occur with opposite orientations relative to the link; the other four
plaquettes are flat. Thus the exact sum, before integrating \(U_e\), is
\[
 H_e=b(U_e^{(0)})^{-1}
       (4I+e^{\vartheta H}+e^{-\vartheta H})
     =b(4+2\cos\vartheta)(U_e^{(0)})^{-1}.
\]
All factors commute here because this specific background is Abelian;
the integrated link \(U_e\) still ranges over the entire non-Abelian
group \(SU(2)\), not its diagonal subgroup. Since
\(4+2\cos\vartheta\geq2\),
\(r_\vartheta=b(4+2\cos\vartheta)>0\). The exact change of the integrated
six-plaquette incident contribution, relative to its flat-background
value, is
\[
 \Delta S_{\rm eff}(\vartheta)
 =\log Z(6b)-\log Z\bigl(b(4+2\cos\vartheta)\bigr)
 =\int_{b(4+2\cos\vartheta)}^{6b}2\eta(s)\,ds.
\]
For the full action one must also retain
\(S_{\rm nonincident}(U^{(\vartheta)})-
S_{\rm nonincident}(U^{(0)})\); the displayed quantity is the local
incident contribution, not an identification of the entire lattice cost.
No expansion in \(g_{\rm YM}\), no quadratic replacement of the
plaquette interaction, and no limit of \(b\) was used.

For every \(s>0\), \(0<\eta(s)<1\). The upper inequality follows from
\(w_0<1\) almost surely under a positive Haar density. To prove strict
positivity, pair \(w_0\) with \(-w_0\) in its symmetric Haar marginal:
the first moment numerator becomes an integral over \((0,1)\) of
\(w_0(e^{2sw_0}-e^{-2sw_0})\sqrt{1-w_0^2}\), which is positive.
Consequently, whenever \(\cos\vartheta<1\),
\[
 0<\Delta S_{\rm eff}(\vartheta)
       <4b(1-\cos\vartheta).
\]
The right side is exactly the original action of the two affected magnetic
plaquettes relative to two flat plaquettes. The inequality is therefore a
computed reduction of this local cost by integration of one full compact
link. It is not an assertion about the mass gap.

The exact integral also yields its leading retained-scale coefficient:
\[
 \Delta S_{\rm eff}(\vartheta)
   =2b\,\eta(6b)\,\vartheta^2+O_b(\vartheta^4)
   =\frac{8\pi^2 b\,\eta(6b)a^4}{D_T^2}
       +O_b(a^8D_T^{-4}).
\]
This expansion is a consequence of the exact expression, which remains
the definition and retains every higher term. Specifically
\(6b-r_\vartheta=2b(1-\cos\vartheta)
=b\vartheta^2+O_b(\vartheta^4)\), and the smooth function
\(2\eta(s)\) can be integrated over that actual interval. The first
moment of the integrated link is exactly
\(\eta(r_\vartheta)U_e^{(0)}\); its two-point moments remain the
full expressions in section 4. This computes one genuine interacting
fluctuation step at the cusp background, with its geometric curvature
scale and gauge coupling both present.

### 5.1 An extensive exact integration on a four-dimensional cusp patch

The same calculation can be applied simultaneously to a growing number of
links without discarding the interactions. Take the physical box with
vertices \(a\{0,\ldots,N\}^4\), \(N\geq2\) even, and all its internal
nearest-neighbor links and plaquettes. Let \(\mathcal E_*\) be the
first-direction links based at vertices satisfying
\[
 0\leq n_1\leq N-1,\qquad 1\leq n_2,n_3,n_4\leq N-1,
 \qquad n_2+n_3+n_4\equiv1\pmod2.
\]
Each such link has all six incident plaquettes. No plaquette contains two
selected links: its two first-direction edges have transverse coordinates
differing by one in exactly one direction, and hence opposite parity.
Plaquettes not involving direction 1 contain no selected link at all.
Therefore, for any configuration of the remaining links,
\[
 \int e^{-S_W(U)}\prod_{e\in\mathcal E_*}dU_e
 =e^{-S_{\rm rest}(U)}
   \prod_{e\in\mathcal E_*}e^{-12b}Z(r_e(U)).
\]
This is an identity between finite-dimensional functions, with all
interactions in the functions \(r_e(U)\) retained. Its proof is the
decomposition of the action into its disjoint incident plaquette sets,
followed by Fubini's theorem for a positive continuous integrand on a
compact product. It integrates over all of \(SU(2)\) independently on
each selected link. The surviving links interact through the products of
staples; they have not been assigned independent distributions.

The number of selected links and the total number of magnetic plaquettes
are, respectively,
\[
 m_N=\frac N2\big((N-1)^3+1\big),\qquad
 p_N=N^2(N+1)^2.
\]
For the first count there are \(N/2\) odd and \(N/2-1\) even integers
in \(\{1,\ldots,N-1\}\). If \(E\) and \(O\) count even and odd sums
of three such integers, then \(E+O=(N-1)^3\) and
\(E-O=((N/2-1)-N/2)^3=-1\). Thus \(O=((N-1)^3+1)/2\);
the first coordinate supplies the factor \(N\). For the second count,
the first two plaquette coordinates each have \(N\) choices and the
other two each have \(N+1\) choices. Exactly \(2m_N\) magnetic
plaquettes belong to selected-link stars, with no overlaps.

Evaluate the resulting exact marginal density at the remaining links of
the constant-curvature background, and compare with the remaining links
of the flat background. The full effective-action difference on this box
is now
\[
 \Delta S_{*,N}(\vartheta)
 =(p_N-2m_N)\,2b(1-\cos\vartheta)
   +m_N\left[\log Z(6b)-\log Z\big(b(4+2\cos\vartheta)\big)\right].
\]
This includes the nonincident term explicitly. The original box action
difference was \(S_{0,N}=2bp_N(1-\cos\vartheta)\). Hence
\[
 0<\Delta S_{*,N}<S_{0,N}\qquad(\cos\vartheta<1),
\]
and for any sequence \(N\to\infty\), \(\vartheta\to0\) with
\(\vartheta\ne0\),
\[
 \frac{\Delta S_{*,N}}{S_{0,N}}\longrightarrow\eta(6b).
\]
Indeed \(2m_N/p_N\to1\), and the ratio of the integrated star cost to
its original two-plaquette cost tends to \(\eta(6b)\) by the exact
integral in section 5. The ratio tends to a strictly positive number
below one at every fixed retained \(b>0\). This is one exact integration
layer; it is not iterated by assuming the same action form at the next
layer.

Here is a sequence with all geometric and cutoff constants specified.
Take the original covered cusp at \(T_j=j^2\), \(M_j=j\), the physical
mesh spacing \(a_j=1/(100j)\), and \(N_j=2j^2\). Its box side is
\(a_jN_j=j/50\). Centering this box at the origin puts it in a ball of
radius \(j/50\), since a four-dimensional cube of side \(\ell\) has
half-diagonal \(\ell\). For sufficiently large \(j\), the earlier
systole bound gives \(\operatorname{sys}\geq j>8j/50\), so the whole
box and a collar embed isometrically in the actual covered cusp. The
mesh tends to zero and its physical box grows without bound. Retaining
the original \(D_{T_j}=j^4(1+O(j^{-2}))\) gives
\[
 \vartheta_j=\frac{2\pi}{10^4 j^2D_{T_j}},\qquad
 j^4S_{0,N_j}(\vartheta_j)
     \longrightarrow\frac{64\pi^2b}{10^8},\qquad
 j^4\Delta S_{*,N_j}(\vartheta_j)
     \longrightarrow\frac{64\pi^2b}{10^8}\eta(6b).
\]
For these constants, \(p_{N_j}/j^8\to16\),
\(j^{12}\vartheta_j^2\to4\pi^2/10^8\), and
\(2(1-\cos\vartheta_j)/\vartheta_j^2\to1\), proving both limits.
Thus the already known small classical curvature cost remains small
after an extensive exact integration of nonlinear compact links on a
four-dimensional physical exhaustion, with its leading coefficient
calculated. This determines a ratio of finite marginal-density values;
it does not yet determine a vacuum excitation energy or a temporal
correlation decay rate.

### 5.2 Retained anisotropic time step

The temporal coordinate must also be specified when relating this action
to a Hamiltonian. Let directions 1, 2 and 3 be spatial, with mesh \(a\),
and direction 4 Euclidean temporal, with mesh \(\epsilon\). For the
original action and Lie metric, coefficient matching gives
\[
 b_s=\frac{\epsilon}{2g_{\rm YM}^2a},\qquad
 b_t=\frac{a}{2g_{\rm YM}^2\epsilon}.
\]
Indeed a spatial plaquette has curvature area \(a^2\) and a temporal
plaquette area \(a\epsilon\), whereas the physical cell volume is
\(a^3\epsilon\). Multiplying each squared area by its displayed
coefficient gives \(a^3\epsilon/(2g_{\rm YM}^2)\). The isotropic
choice \(\epsilon=a\) recovers \(b_s=b_t=b\), including every factor.

For a selected spatial link in the magnetic plane, there are two magnetic
spatial staples, two other spatial staples and two temporal staples.
Its exact flat and magnetic staple radii are consequently
\[
 r_0=4b_s+2b_t,\qquad
 r_\vartheta=2b_s(1+\cos\vartheta)+2b_t,
 \qquad r_0-r_\vartheta=2b_s(1-\cos\vartheta).
\]
The exact integrated star cost is still
\[
 \Delta S^{a,\epsilon}_{\rm star}
 =\log Z(r_0)-\log Z(r_\vartheta)
 =\int_{r_\vartheta}^{r_0}2\eta(s)ds.
\]
Thus the same nonlinear integration has an explicit time-step dictionary,
not an identification of \(a\) and \(\epsilon\) made after the fact.

For clarity, the first large-\(r\) coefficient used here can be proved
from the exact Haar integral. Set \(w_0=1-z/r\). Apart from factors
that cancel in expectations, the density of \(z\in[0,2r]\) is
\[
 e^{-2z}z^{1/2}\left(1-\frac z{2r}\right)^{1/2}dz.
\]
On \(0\leq z\leq r\), the last factor equals \(1+O(z/r)\), with an
absolute bound supplied by the mean value theorem on \([0,1/2]\).
The tail \(z\geq r\) is bounded by the exponentially integrable
\(e^{-2z}z^{1/2}\), and the same argument works after multiplication
by \(z\). Hence the mean of \(z\) is
\[
 \frac{\int_0^\infty e^{-2z}z^{3/2}dz}
      {\int_0^\infty e^{-2z}z^{1/2}dz}+O(r^{-1})
 =\frac34+O(r^{-1}),
\]
where integration by parts gives the ratio \(3/4\). Since
\(w_0=1-z/r\), this proves
\(\eta(r)=1-3/(4r)+O(r^{-2})\), with no Gaussian substitution for
the finite integral.

Keeping \(a>0\) and \(g_{\rm YM}>0\) fixed and taking
\(\epsilon\downarrow0\), the exact star formula gives
\[
 \frac{\Delta S^{a,\epsilon}_{\rm star}}
      {4b_s(1-\cos\vartheta)}
 =1-\frac{3}{4r_0}+O_{a,g_{\rm YM}}(\epsilon^2)
 =1-\frac{3g_{\rm YM}^2\epsilon}{4a}
       +O_{a,g_{\rm YM}}(\epsilon^2)
\]
when \(\cos\vartheta<1\). This follows by averaging \(\eta\) over
the actual interval, whose width is at most \(4b_s=O(\epsilon)\),
while \(r_0\) is of order \(\epsilon^{-1}\). Equivalently,
\[
 4b_s(1-\cos\vartheta)-\Delta S^{a,\epsilon}_{\rm star}
 =\frac{3\epsilon^2}{2a^2}(1-\cos\vartheta)
      +O_{a,g_{\rm YM}}(\epsilon^3).
\]
The error estimate is uniform for real \(\vartheta\), using
\(0\leq1-\cos\vartheta\leq2\). At \(\cos\vartheta=1\) the exact
difference vanishes, while the ratio is interpreted by its continuous
value. The strict finite-step reduction proved above is preserved;
its size in a continuous-time limit is now explicitly calculated.
At fixed spatial regulator and fixed temporal extent, there are at most
a constant times \(\epsilon^{-1}\) selected links, so their total
one-layer reduction is \(O_{a,g_{\rm YM}}(\epsilon)\). No uniform
claim in \(a\downarrow0\) follows from this fixed-\(a\) estimate.
In the isotropic joint sequence of section 5.1 the exact coefficient
remains \(\eta(6b)\). Both limiting procedures and their retained
coefficients are therefore visible.

## 6. What this calculation transports, and the next actual calculation

The cusp sequence now has a fully explicit nonlinear classical action and
observable transport on any fixed bounded physical domain. The finite
compact-link regulator has an exact integration of a link retaining every
neighboring plaquette, with the induced interaction displayed above.
Neither operation changes \(SU(2)\) to a commutative field theory.

Successive integration produces further interactions; the displayed
six-staple formula is not asserted to stay in the original one-plaquette
form after previous eliminations. For a region \(\Lambda\), the exact
marginal is obtained by integrating its complement in
\(e^{-S_W}\prod_e dU_e\), leaving the positive boundary-dependent
factor \(Z_{\Lambda^c}(U_{\partial\Lambda})\). Discarding that factor
would discard an interaction. Its effect on gauge-invariant covariance
and spectral weight is the quantity to calculate, alongside the exact
Hamiltonian ground-state identities in the companion calculation.
No vanishing interacting infinite-volume quantum gap is proved here.

## Literature and provenance

The period matrix, covering map, action convention and original flux are
the formulas with these source labels in the canonical compact-link draft:

- `cusp-link-period-matrix`;
- `cusp-link-cover-matrix`;
- `cusp-link-magnetic-ym-normalization`;
- `cusp-link-flux-theorem`.

The block inverses, full curvature transport,
local nonlinear extension and finite-graph realization are proved above.

The single-link integral is established lattice-gauge mathematics, not
claimed here as a newly discovered integration method. Its role here is to
compute the interaction retained in this cusp-to-regulator route.

- K. G. Wilson, *Confinement of quarks*, Physical Review D **10** (1974),
  2445-2459, <https://doi.org/10.1103/PhysRevD.10.2445>.
- J. Kogut and L. Susskind, *Hamiltonian formulation of Wilson's lattice
  gauge theories*, Physical Review D **11** (1975), 395-408,
  <https://doi.org/10.1103/PhysRevD.11.395>.
- M. Creutz, *Monte Carlo study of quantized SU(2) gauge theory*, Physical
  Review D **21** (1980), 2308-2315,
  <https://doi.org/10.1103/PhysRevD.21.2308>. Author's primary inventory:
  <https://www.latticeguy.net/mypubs/pubs.html>, item 37.
- D. Tong, *Lectures on Gauge Theory*, chapter 4, especially Wilson loops,
  the Wilson action and Haar integration, <https://www.damtp.cam.ac.uk/user/tong/gaugetheory.html>.
  The locally retained text was inspected rather than relying only on recall.
- A. Jaffe and E. Witten, *Quantum Yang-Mills Theory*,
  <https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf>,
  specifies the quantum existence and mass-gap target; no part of that
  target is replaced by the finite calculations above.
