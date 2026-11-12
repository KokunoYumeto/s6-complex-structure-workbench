# Current exact Yang-Mills and cusp calculations for AI review

8 September 2026. Complete proof texts follow, not compressed summaries.

The original magnetic bundle and printed compact links are related by the
explicit vertex-frame map h(n)=exp(-2πH n₁n₂/N²), including both wraps.
Full nonlinear field/action transport through the original cusp covers is
proved with the original metric, Lie inner product and coupling retained.

For the full SU(2) Wilson action on an actual four-dimensional physical
patch, an extensive set of links is integrated exactly. At the original
magnetic background, the ratio of its integrated to original action cost
tends to I₂(12b)/I₁(12b), where b=1/(2gYM²), without a Gaussian replacement.
The finite Hamiltonian calculation gives actual vacuum-weighted Wilson-loop
variations and their exact relation to spectral first moments. With spatial
spacing a and time spacing epsilon kept independent, the exact temporal
character multiplier is I_(2j+1)(2b_t)/I_1(2b_t), b_t=a/(2gYM² epsilon).
The fully proved time limit, including integration of the temporal links,
gives H=-(2gYM²/a) sum_e Delta_e^T
       +(1/(2gYM²a)) sum_p (2-Re tr U_p)
on gauge-invariant functions. The probability-Haar scalar multiplying the
raw transfer is retained explicitly, together with its common energy shift.
No magnetic plaquette is discarded. The original Lie metric is c=-tr/2,
so Delta^c=4 Delta^T; the coefficient in that metric is gYM²/(2a).

The adjacent-plaquette calculation and its full-box extension evaluate a
nonzero quantum elimination coupling on an actual gauge-invariant retained
Wilson loop. In every fixed open three-dimensional box [-L,L]³, L≥2,
with all its links and plaquettes retained in H and original coefficients
kappa and b, ||B f||²=b²/12+O_L(b³/kappa). The explicit resolvent-corrected
full-system trial vector lowers the retained-only excitation quotient by
(1951/81675)b²/kappa+O_L(b³/kappa²), at fixed kappa and small positive b/kappa.
The two contributing eliminated Casimir channels are 9kappa/2 and 13kappa/2.
This coefficient is computed from the derivative of the actual analytic
vacuum; independent Haar links are used only at its exact b=0 endpoint.
The full positive-b state is not replaced by that endpoint.

For the two-plaquette system the absolute excitation quotients are also
evaluated: R_ret=3kappa+(5/9)b²/kappa+O(b³/kappa²), and
R_corrected=3kappa+(43424/81675)b²/kappa+O(b³/kappa²).
Thus both lie above their zero-b value to this order, despite the strict
improvement at the same positive b. They are trial quotients, not exact
excited eigenvalues. The complete proof also retains the vacuum energy
E=4b-(2/3)b²/kappa+O(b³/kappa²) and gives the unsubtracted-H quotients.
The full-box spectral-projection disk is |b/kappa|<3/(16M), with
M=3(2L)²(2L+1); its shrinking radius and box-dependent remainder have not
been replaced by a volume-uniform or continuum statement.

The goal remains a counterexample to the genuine interacting four-dimensional
quantum mass-gap assertion. No such counterexample is claimed in these
files. The computed marginal-density values are not already vacuum energies.
The next research step is to calculate their full surviving-link correlations
and transfer to physical spectral weight, retaining all generated interactions.
The completed fixed-spatial-regulator time limit must not be silently
substituted for a simultaneous spatial-continuum and infinite-volume limit.
Do not assume the same one-plaquette action survives repeated integration.

The final analytic note independently tests the actual announced Euler
construction under positive viscosity and constructs explicit correction
maps; it does not identify that theorem as a Navier-Stokes counterexample.

Primary references are given within the proof texts. The classical single-link
integral and standard compact-group representation identities are not claimed
as new discoveries. Their exact use in this retained cusp calculation is shown.

## Complete source: retained_cusp_nonlinear_bridge.md

```markdown
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

```

## Complete source: wilson_variation/wilson_finite_lattice.tex

```latex
\documentclass[11pt]{article}
\usepackage[margin=1in]{geometry}
\usepackage{amsmath,amssymb,amsthm,mathtools}
\usepackage[hidelinks]{hyperref}
\newtheorem{theorem}{Theorem}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{corollary}[theorem]{Corollary}
\theoremstyle{definition}
\newtheorem{definition}[theorem]{Definition}
\newcommand{\tr}{\operatorname{tr}}
\newcommand{\SU}{\operatorname{SU}}
\newcommand{\Rea}{\operatorname{Re}}
\newcommand{\Ima}{\operatorname{Im}}
\newcommand{\Var}{\operatorname{Var}}
\newcommand{\Cov}{\operatorname{Cov}}
\newcommand{\dd}{\,\mathrm d}
\title{Exact vacuum-weighted Wilson-loop variation on a finite interacting lattice}
\author{}
\date{8 September 2026}
\begin{document}
\maketitle

\section{Objects, orientations, and both Lie metrics}

Fix an integer $n\geq2$, a finite oriented graph with vertex set $\mathsf V$
and one chosen orientation for every physical edge in a nonempty edge set
$\mathsf E$, and a finite list $\mathsf P$ of oriented closed plaquette words.
Write $N=|\mathsf E|$. Reverse traversal of $e$ uses $U_e^{-1}$, not a new
independent link. The configuration manifold and its probability Haar measure
are
\[
 \mathcal Q=\SU(n)^{\mathsf E},\qquad
 d\lambda(U)=\prod_{e\in\mathsf E}dU_e,\qquad \lambda(\mathcal Q)=1.
\]
For a word $C=((e_1,\varepsilon_1),\ldots,(e_\ell,\varepsilon_\ell))$
with $\varepsilon_j\in\{1,-1\}$, define, in the written order,
\[
 H_C(U)=U_{e_1}^{\varepsilon_1}\cdots U_{e_\ell}^{\varepsilon_\ell},
 \qquad W_C(U)=\tr H_C(U).
\]
A simple edge loop here means a nonempty closed word using each physical edge
at most once. Vertices may be repeated; all statements below needing simplicity
need precisely the absence of repeated physical edges. Ordinary simple
plaquettes and primitive winding loops on a sufficiently large periodic
hypercubic lattice satisfy this definition. If a small periodic lattice makes
one plaquette repeat an edge, use the repeated-occurrence formula below.

Choose an anti-Hermitian traceless basis $T_a$, $1\leq a\leq n^2-1$, with
\[
 -2\tr(T_aT_b)=\delta_{ab}.
\]
The derivatives requested in this calculation are exactly
\[
 X_{e,a}f(U)=\left.\frac d{dt}\right|_{t=0}
 f(\ldots,e^{tT_a}U_e,\ldots),\qquad
 \Delta_e^T=\sum_aX_{e,a}^2.
\]
In this convention $X_{e,a}$ is skew-adjoint in $L^2(\lambda)$. Indeed,
left invariance of Haar gives
\[
 \int f(e^{tT_a}U_e)g(U_e)dU_e
 =\int f(U_e)g(e^{-tT_a}U_e)dU_e;
\]
differentiation proves the assertion,
with the complex conjugate placed on the first argument when appropriate.

There are two retained Lie metrics, related by an explicit dictionary:
\begin{align}
 g_T(A,B)&=-2\tr(AB),&
 c(A,B)&=-\tfrac12\tr(AB)=\tfrac14g_T(A,B),\label{eq:metrics}\\
 c(T_a,T_b)&=\tfrac14\delta_{ab},&
 S_a&=2T_a,& c(S_a,S_b)&=\delta_{ab},\nonumber\\
 X^c_{e,a}&=2X_{e,a},&
 \Delta_e^c&=4\Delta_e^T.\label{eq:metric-laplace}
\end{align}
Thus a Casimir eigenvalue measured with $c$ is four times its $g_T$ value.
The Hamiltonian in this paper is the specified operator
\begin{equation}\label{eq:H}
 H=-\sum_{e\in\mathsf E}\kappa_e\Delta_e^T+V,
 \quad
 V(U)=\sum_{p\in\mathsf P}b_p\bigl(n-\Rea W_p(U)\bigr),
 \quad \kappa_e>0,\ b_p>0.
\end{equation}
In the original cusp metric it is identically
$H=-\sum_e(\kappa_e/4)\Delta_e^c+V$.
Keeping the coefficient $\kappa_e$ in front of $\Delta_e^c$ would instead
multiply the kinetic operator by four and would define a different
Hamiltonian. No such replacement is made here. The inequalities
$|\tr U|\leq n$ for $U\in\SU(n)$ and
\begin{equation}\label{eq:Vbounds}
 0\leq V\leq M,\qquad
 M=2nB,\qquad B=\sum_{p\in\mathsf P}b_p,
\end{equation}
retain every plaquette term. The trace bound follows by summing the $n$
unit-modulus eigenvalues. The constant $2nB$ is a valid bound; no assertion
that all plaquettes attain their separate maxima simultaneously is needed.

The probability Haar convention also has an exact volume dictionary.
On the compact configuration manifold, whose real dimension is
$d=N(n^2-1)$, \eqref{eq:metrics} gives
$d\operatorname{vol}_c=2^{-d}d\operatorname{vol}_{g_T}$.
If $\mathcal V_c=\operatorname{vol}_c(\mathcal Q)$ and
$\mathcal V_T=\operatorname{vol}_{g_T}(\mathcal Q)$, then
\[
 d\lambda=\mathcal V_c^{-1}d\operatorname{vol}_c
         =\mathcal V_T^{-1}d\operatorname{vol}_{g_T},\qquad
 \mathcal V_c=2^{-d}\mathcal V_T.
\]
The map $f\mapsto\sqrt{\mathcal V_c}\,f$ is unitary from
$L^2(d\operatorname{vol}_c)$ to $L^2(d\lambda)$ and intertwines the same
differential Hamiltonian. A ground state normalized in the former
space is therefore taken to $\psi_0=\sqrt{\mathcal V_c}\,\psi_c$, so
$\psi_0^2d\lambda=\psi_c^2d\operatorname{vol}_c$ exactly. These are
volume identities on the compact group product only; they do not
identify a noncompact cusp measure with Haar measure.

Gauge transformations are
$(g\cdot U)_e=g_{s(e)}U_eg_{t(e)}^{-1}$ for
$g\in\SU(n)^{\mathsf V}$. Along a closed word all adjacent factors cancel,
so $H_C$ changes by conjugation at its base vertex and $W_C$ is invariant.
Haar measure, each $\Delta_e^T$, and $V$ are gauge invariant. The physically
restricted finite Hilbert space is therefore the closed invariant subspace
$\mathcal H_{\rm inv}\subset L^2(\mathcal Q,\lambda)$, and $H$ preserves it.

\section{Fierz identities with the stated normalization}

\begin{lemma}\label{lem:Fierz}
For arbitrary complex $n\times n$ matrices $A,B$,
\begin{align}
 \sum_a(T_a)_{ij}(T_a)_{kl}
 &=-\frac12\left(\delta_{il}\delta_{jk}
                  -\frac1n\delta_{ij}\delta_{kl}\right),\label{eq:Fierz}\\
 \sum_a\tr(T_aA)\tr(T_aB)
 &=-\frac12\left(\tr(AB)-\frac1n\tr A\tr B\right),\label{eq:bilinear}\\
 \sum_a\tr(T_aA)\overline{\tr(T_aB)}
 &=\frac12\left(\tr(AB^\dagger)
       -\frac1n\tr A\,\overline{\tr B}\right),\label{eq:sesquilinear}\\
 \sum_aT_a^2&=-C_FI_n,\qquad C_F=\frac{n^2-1}{2n}.\label{eq:fundcasimir}
\end{align}
In particular, for $A\in\SU(n)$,
\begin{equation}\label{eq:singlecontraction}
 \sum_a|\tr(T_aA)|^2=\frac{n^2-|\tr A|^2}{2n}.
\end{equation}
\end{lemma}
\begin{proof}
The matrices $Q_0=I_n/\sqrt n$ and $Q_a=i\sqrt2T_a$ form an orthonormal
basis of the real vector space of Hermitian matrices for the scalar product
$\tr(QR)$. Their complex linear span is all complex matrices. Expanding an
arbitrary matrix $D$ gives
$D=\sum_{\alpha=0}^{n^2-1}Q_\alpha\tr(Q_\alpha D)$.
Taking the coefficient of $D_{lk}$ in entry $ij$ proves
$\sum_\alpha(Q_\alpha)_{ij}(Q_\alpha)_{kl}=\delta_{il}\delta_{jk}$.
Subtract the $Q_0$ term and use $(i\sqrt2)^2=-2$ to obtain
\eqref{eq:Fierz}. Contract it with $A_{ji}B_{lk}$ to get
\eqref{eq:bilinear}. Anti-Hermiticity gives
$\overline{\tr(T_aB)}=-\tr(T_aB^\dagger)$; this proves
\eqref{eq:sesquilinear}. Put $k=j$ in \eqref{eq:Fierz} and sum $j$ to
obtain \eqref{eq:fundcasimir}. Finally $AA^\dagger=I_n$ gives
\eqref{eq:singlecontraction}.
\end{proof}

\section{Every edge orientation and the exact overlap morphism}

Fix one occurrence of physical edge $e$ in $C$ and write the ordered word
as $P U_e^{\varepsilon}Q$, where $P$ and $Q$ are the products before and
after that occurrence. Cyclic trace invariance gives the following
matrices based at the original source $s(e)$:
\begin{equation}\label{eq:based}
 A_{C,e,r}=
 \begin{cases}
 U_eQP,&\varepsilon=+1,\\
 QPU_e^{-1},&\varepsilon=-1.
 \end{cases}
\end{equation}
The occurrence index $r$ is suppressed when there is only one occurrence.
Each $A_{C,e,r}$ lies in $\SU(n)$, has trace $W_C$, and transforms by
conjugation with $g_{s(e)}$ under a gauge transformation. These statements
follow either by multiplying the factors or by following the cyclically
based closed path at $s(e)$.

The derivative of an inverse is
$X_{e,a}U_e^{-1}=-U_e^{-1}T_a$, since
$(e^{tT_a}U_e)^{-1}=U_e^{-1}e^{-tT_a}$. Consequently
\begin{align}
 X_{e,a}\tr(PU_eQ)&=\tr(PT_aU_eQ)=\tr(T_aU_eQP),\nonumber\\
 X_{e,a}\tr(PU_e^{-1}Q)&=-\tr(PU_e^{-1}T_aQ)
 =-\tr(T_aQPU_e^{-1}).\label{eq:orientations}
\end{align}
For an arbitrary closed word the product rule now gives
\begin{equation}\label{eq:repeatedderivative}
 X_{e,a}W_C=\sum_{r:e_r=e}\varepsilon_r\tr(T_aA_{C,e,r}).
\end{equation}
All factors in \eqref{eq:based} are evaluated at the original configuration;
there is no independent-link approximation in this formula.

For two words define the edgewise sesquilinear and bilinear contractions
by
\[
 \Gamma_e(F,G)=\sum_a(X_{e,a}F)\overline{X_{e,a}G},\qquad
 \Gamma_e^{\rm bil}(F,G)=\sum_a(X_{e,a}F)(X_{e,a}G).
\]
Lemma \ref{lem:Fierz} proves, occurrence by occurrence,
\begin{align}
\Gamma_e(W_C,W_D)
 &=\frac12\sum_{r:e_r=e}\sum_{s:d_s=e}\varepsilon_r\eta_s
 \left[\tr(A_{C,e,r}A_{D,e,s}^{\dagger})
       -\frac1nW_C\overline{W_D}\right],\label{eq:overlap-general}\\
\Gamma_e^{\rm bil}(W_C,W_D)
 &=-\frac12\sum_{r:e_r=e}\sum_{s:d_s=e}\varepsilon_r\eta_s
 \left[\tr(A_{C,e,r}A_{D,e,s})-\frac1nW_CW_D\right].
 \label{eq:overlap-bil-general}
\end{align}
These identities construct the exact relation between the two loop
variations: $A_{C,e,r}A_{D,e,s}^{-1}$ is the concatenation of the first
based loop and the inverse of the second, and its trace is gauge invariant.
The nonconjugated contraction concatenates the two based loops directly.
An edge not occurring in both words contributes zero.

For simple edge loops, a common edge contributes exactly
\begin{align}
\Gamma_e(W_C,W_D)
 &=\frac{\varepsilon_{Ce}\varepsilon_{De}}2
   \left[\tr(A_{Ce}A_{De}^{\dagger})
                    -\frac1nW_C\overline{W_D}\right],\label{eq:overlap-simple}\\
\Gamma_e^{\rm bil}(W_C,W_D)
 &=-\frac{\varepsilon_{Ce}\varepsilon_{De}}2
   \left[\tr(A_{Ce}A_{De})-\frac1nW_CW_D\right].\nonumber
\end{align}
In particular, for every used edge of a simple loop,
\begin{equation}\label{eq:simpleenergy}
 \Gamma_e(W_C,W_C)=\frac{n^2-|W_C|^2}{2n},\qquad
 \sum_aX_{e,a}^2W_C=-C_FW_C.
\end{equation}
The second equality follows directly from \eqref{eq:orientations} and
\eqref{eq:fundcasimir}; in negative orientation the two derivative signs
cancel. Both equalities are zero on unused edges. Define
$K_C=\sum_{e\in C}\kappa_e$. Then the full pointwise energy is
\begin{equation}\label{eq:simplefullenergy}
 \Gamma_\kappa(W_C,W_C):=\sum_e\kappa_e\Gamma_e(W_C,W_C)
       =\frac{K_C}{2n}(n^2-|W_C|^2).
\end{equation}

For later real plaquette observables the exact companion identity is
\begin{equation}\label{eq:realenergy}
 \Gamma_\kappa(\Rea W_C,\Rea W_C)
 =\frac{K_C}{4}\left[n-\Rea\tr(H_C^2)
                           -\frac2n(\Ima W_C)^2\right].
\end{equation}
To prove it, use $(\Rea z)^2=(|z|^2+\Rea z^2)/2$ in the derivative
sum, apply both contractions in Lemma \ref{lem:Fierz}, and observe
$\tr(A_{Ce}^2)=\tr(H_C^2)$ because cyclic rotations of invertible factors
are conjugate matrices. Thus the right side is nonnegative despite its
written difference of terms. The same energy holds for $n-\Rea W_C$.
Measured using $X^c=2X$, every $\Gamma_e$ in this section is multiplied
by four; pairing it with kinetic coefficient $\kappa_e/4$ recovers
exactly \eqref{eq:simplefullenergy} and \eqref{eq:realenergy}.

\section{Existence, exact ground-state transform, and orthogonality}

The domain of the nonnegative quadratic form of $H$ is the first Sobolev
space on $\mathcal Q$, with the equivalent norm given by the finitely many
fields $X_{e,a}$. Its form is
\[
 q_H(u,v)=\sum_{e,a}\kappa_e\int\overline{X_{e,a}u}X_{e,a}v\,d\lambda
                   +\int V\overline uv\,d\lambda.
\]
We use the self-adjoint operator associated to this closed form.

\begin{lemma}\label{lem:ground}
$H$ has a unique normalized strictly positive ground eigenfunction
$\psi_0\in C^\infty(\mathcal Q)$, with $H\psi_0=E_0\psi_0$ and
$\int\psi_0^2d\lambda=1$. It is gauge invariant. In particular the bottom
eigenvalue of the gauge-invariant restriction is the same $E_0$.
\end{lemma}
\begin{proof}
The free positive operator $H_0=-\sum_e\kappa_e\Delta_e^T$ has a complete
matrix-coefficient eigenbasis by the compact-group Peter--Weyl theorem
\cite{PeterWeyl}; its finite-multiplicity eigenvalues tend to infinity.
The latter fact also follows from the explicit weights and bounds proved
in Section \ref{sec:heat}. Its resolvent is compact. Bounded real
multiplication by $V$ preserves self-adjointness and compact resolvent:
for sufficiently negative $z$, the identity
$(H-z)^{-1}=(H_0-z)^{-1}[I+V(H_0-z)^{-1}]^{-1}$ proves compactness by a
convergent Neumann series. Hence the bottom of the spectrum is an
eigenvalue. The inequality $|X|u||\leq|Xu|$ almost everywhere (obtain it
first for $\sqrt{|u|^2+\epsilon^2}$ and then let $\epsilon\downarrow0$)
shows that the modulus of a minimizing eigenfunction is also minimizing.
Choose a nonnegative normalized one. The elliptic equation
$H_0\psi_0=(E_0-V)\psi_0$ and local elliptic regularity, iterated with
smooth $V$, give $\psi_0\in C^\infty$.

For completeness, positivity needs no assumption about an unknown vacuum.
The parabolic comparison inequality proved in Section \ref{sec:heat} is
$e^{-tH}f\geq e^{-Mt}e^{-tH_0}f$ for $f\geq0$.
At the explicit time $t_*$ in that section the kernel of $e^{-t_*H_0}$
is at least $2^{-N}$. Thus
$\psi_0(U)\geq e^{(E_0-M)t_*}2^{-N}\int\psi_0d\lambda>0$.
The next theorem, whose calculation uses only this already established
positivity and the eigenvalue equation, proves uniqueness: if $u$ is
another ground eigenfunction, put $f=u/\psi_0$ in its identity. The
result is $\int\psi_0^2\sum_{e,a}\kappa_e|X_{e,a}f|^2d\lambda=0$.
The fields span each tangent space and $\mathcal Q$ is connected, so
$f$ is constant. Gauge transformations preserve $H$, positivity and
normalization, and consequently fix $\psi_0$ by this uniqueness.
\end{proof}

Set
\begin{equation}\label{eq:vacuummeasure}
 d\mu=\rho\,d\lambda,\qquad \rho=\psi_0^2,
 \qquad \mu(F)=\int F\,d\mu.
\end{equation}
This measure is determined by the interacting Hamiltonian
\eqref{eq:H}; no other measure is substituted for it below.
Multiplication $\mathcal U f=\psi_0 f$ is a unitary map from
$L^2(\mu)$ onto $L^2(\lambda)$, since
$\|\mathcal U f\|_\lambda^2=\int|f|^2d\mu$, and division by the positive
$\psi_0$ is its inverse. It also maps the respective gauge-invariant
subspaces onto one another.

\begin{theorem}\label{thm:ground-transform}
For all smooth complex $f,g$,
\begin{align}
 Lg:=\mathcal U^{-1}(H-E_0)\mathcal Ug
 &=-\sum_{e,a}\kappa_e
       \bigl[X_{e,a}^2g+2(X_{e,a}\log\psi_0)X_{e,a}g\bigr]
       \label{eq:groundop}\\
 &=-\rho^{-1}\sum_{e,a}\kappa_e X_{e,a}(\rho X_{e,a}g),\nonumber\\
 \langle\psi_0f,(H-E_0)\psi_0g\rangle_\lambda
 &=\sum_{e,a}\kappa_e\int\overline{X_{e,a}f}X_{e,a}g\,d\mu.
 \label{eq:groundform}
\end{align}
The identities extend to the corresponding closed form domains. For any
nonconstant smooth $F$, the vector
$u_F=\psi_0(F-\mu(F))$ is orthogonal to $\psi_0$, and
\begin{equation}\label{eq:Rayleigh-general}
 \frac{\langle u_F,(H-E_0)u_F\rangle}{\|u_F\|^2}
 =\frac{\mu(\Gamma_\kappa(F,F))}
        {\mu(|F|^2)-|\mu(F)|^2}.
\end{equation}
\end{theorem}
\begin{proof}
The product rule gives
$X^2(\psi_0g)=\psi_0X^2g+2(X\psi_0)Xg+gX^2\psi_0$ for each $X$.
Subtracting $g(H-E_0)\psi_0=0$ from $(H-E_0)(\psi_0g)$ proves
\eqref{eq:groundop}; its divergence form uses $X\rho=2\psi_0X\psi_0$.
Multiply by $\rho\overline f$ and integrate. The skew-adjointness of
$X$ with respect to $\lambda$, proved above, gives
$-\int\overline f X(\rho Xg)d\lambda
=\int\rho\overline{Xf}Xg d\lambda$. Summing proves
\eqref{eq:groundform}. On a compact manifold multiplication and division
by the smooth positive $\psi_0$ are bounded on the first Sobolev space,
so smooth approximation proves the form extension. Finally
$\langle\psi_0,u_F\rangle=\mu(F)-\mu(F)=0$,
$\|u_F\|^2=\mu(|F|^2)-|\mu(F)|^2$, and subtracting a constant leaves
all derivatives unchanged. The variance is strictly positive because
$F$ is nonconstant and $\rho>0$ everywhere. These observations prove
\eqref{eq:Rayleigh-general}.
\end{proof}

In particular, put $m_C=\mu(W_C)$ and $r_C=\mu(|W_C|^2)$. For a simple
edge loop the exact answer is
\begin{equation}\label{eq:Rayleigh-loop}
 Q_C=\frac{K_C}{2n}\,
       \frac{n^2-r_C}{r_C-|m_C|^2}.
\end{equation}
The potential disappears from the displayed Dirichlet integrand because
the exact ground-state equation was used. It remains in $\rho$, $m_C$,
and $r_C$, as well as in the drift term in \eqref{eq:groundop}. Thus
this identity does not set $V$ or any $b_p$ to zero.

\section{Center symmetry, exact selection rules, and character limits}

Assign a central element $z_e\in Z(\SU(n))$ to each physical edge, subject
to
\begin{equation}\label{eq:centercondition}
 \prod_{r\in p}z_{e_r}^{\varepsilon_r}=1
 \quad\hbox{for every retained plaquette }p.
\end{equation}
Define $\sigma_z(U)_e=z_eU_e$. This is a Haar-preserving diffeomorphism,
commutes with the edge derivatives, and preserves every plaquette
holonomy because the factors $z_e$ are central and obey
\eqref{eq:centercondition}. It therefore preserves $H$ and, by uniqueness
and positivity, $\psi_0$ and $\mu$. For every closed word,
\[
 W_C(\sigma_z U)=\zeta_C W_C(U),\qquad
 \zeta_C=\prod_{r\in C}z_{e_r}^{\varepsilon_r}.
\]
Integration proves the exact selection rules
\begin{equation}\label{eq:selection}
 \mu(W_C)=0\quad\hbox{if }\zeta_C\ne1,
 \qquad
 \mu(W_C\overline{W_D})=0\quad\hbox{if }\zeta_C\overline{\zeta_D}\ne1.
\end{equation}
For powers and products the same proof applies with their product charge.

On a periodic hypercubic lattice, multiply the links in one coordinate
direction crossing one fixed periodic cut by $z\in Z(\SU(n))$, and
leave the other links unchanged. Each oriented plaquette crosses that
cut with total signed count zero, which verifies
\eqref{eq:centercondition} directly. A loop with integer winding $q$
in that direction acquires $z^q$. A primitive single winding has a
nontrivial charge for a nonidentity suitable $z$, and therefore $m_C=0$.
A loop whose winding in every direction is divisible by $n$ does not
obtain a zero mean from this argument. Contractible plaquettes are
center neutral; their means must be retained.

For a charged simple loop the quotient becomes
\begin{equation}\label{eq:chargedquotient}
 Q_C=\frac{K_C}{2n}\left(\frac{n^2}{r_C}-1\right),
 \qquad 0<r_C<n^2.
\end{equation}
The strict inequalities follow from $\rho>0$ and the fact that the
holonomy map of a simple loop has image all of $\SU(n)$: fix the other
edges and vary any one used edge. Some images have trace zero and
others have trace $n$, and neighborhoods of both have positive Haar
measure. In particular center symmetry does not set $r_C$ equal to one.

\begin{lemma}\label{lem:Haar-loop}
For every simple edge loop,
\[
 \int W_Cd\lambda=0,\quad
 \int|W_C|^2d\lambda=1,\quad
 \int(n^2-|W_C|^2)d\lambda=n^2-1.
\]
\end{lemma}
\begin{proof}
Condition on every edge except one appearing once. Its loop holonomy
is $A U_e^{\pm1}B$ for fixed group matrices $A,B$, and is Haar distributed
by left and right invariance and invariance under inversion. It suffices
to integrate over one Haar matrix $U$. Its mean trace is zero since
$U\mapsto zU$ preserves Haar for a nonidentity central $z$.
For arbitrary $D$, the matrix $\int UDU^\dagger dU$ commutes with every
$\SU(n)$ matrix by invariance, and so is $(\tr D)I_n/n$.
To see the scalar conclusion without an additional representation
assumption, commuting with diagonal unitary matrices kills the
off-diagonal entries and commuting with determinant-one unitary changes
of coordinate axes makes all diagonal entries equal. Set $D=E_{jl}$
and compare entries to get
$\int U_{ij}\overline{U_{kl}}dU=\delta_{ik}\delta_{jl}/n$.
Taking $j=i$, $l=k$ and summing $i,k$ gives $\int|\tr U|^2dU=1$.
The last asserted integral follows by subtraction.
\end{proof}

There is also an exact character map that retains the second moment.
The conjugation action $A\mapsto UAU^{-1}$ on $\operatorname{End}(\mathbb C^n)$
has trace $\tr U\tr U^{-1}=|\tr U|^2$. The invariant decomposition into
scalar and traceless matrices has characters $1$ and $\chi_{\rm ad}$.
Consequently
\begin{equation}\label{eq:adjointmoment}
 |\tr U|^2=1+\chi_{\rm ad}(U),\quad
 r_C=1+\mu(\chi_{\rm ad}(H_C)),\quad
 -1\leq\chi_{\rm ad}(U)\leq n^2-1.
\end{equation}
This derivation proves the equality and both bounds directly; the adjoint
character is center neutral, so \eqref{eq:selection} imposes no zero
expectation on it.

\begin{proposition}\label{prop:symmetryinsufficient}
Center and gauge invariance, positivity of a smooth density, and the
pointwise character bounds alone imply no strictly positive uniform
lower bound on $r_C$ and no upper bound strictly smaller than $n^2$.
This assertion concerns those premises alone, not the narrower family
of ground states of \eqref{eq:H}.
\end{proposition}
\begin{proof}
Let $h(U)=|W_C(U)|^2$. Its range includes $0$ and $n^2$.
For an explicit trace-zero matrix take
$\zeta=e^{2\pi i/n}$ and
$A=\alpha\operatorname{diag}(1,\zeta,\ldots,\zeta^{n-1})$ with
$\alpha=e^{-\pi i(n-1)/n}$. The geometric sum is zero and
$\det A=\alpha^n\zeta^{n(n-1)/2}=1$. Choose one edge to realize $A$
as holonomy; identity holonomy realizes $n^2$.
For each $s>0$, the densities
\[
 \rho_s^- =\frac{e^{-sh}}{\int e^{-sh}d\lambda},\qquad
 \rho_s^+ =\frac{e^{sh}}{\int e^{sh}d\lambda}
\]
are smooth, strictly positive, gauge invariant, and invariant under
every center transformation of the stated type. For $\epsilon>0$, the
set $h<\epsilon/2$ is nonempty open and has Haar measure $a_\epsilon>0$.
Its contribution to the first denominator is at least
$a_\epsilon e^{-s\epsilon/2}$, whereas the numerator mass of $h\geq\epsilon$
is at most $e^{-s\epsilon}$. Thus this latter probability tends to zero
and $\int h\rho_s^-d\lambda\to0$ by boundedness. Apply the same argument
to $n^2-h$ for $\rho_s^+$ to obtain $\int h\rho_s^+d\lambda\to n^2$.
For a nontrivially charged loop, both measures also have zero loop mean
by the selection-rule proof. No claim is made that these constructed
densities arise from positive Wilson plaquette coefficients in
\eqref{eq:H}; their role is to prove exactly the asserted insufficiency
of symmetry and character bounds alone.
\end{proof}

\section{Explicit all-coupling finite-volume estimates}\label{sec:heat}

The full Hamiltonian supplies more information than those symmetry
premises. The following bounds use it and hold for arbitrary positive
values of all retained couplings. Define
\begin{equation}\label{eq:constants}
 \kappa_* =\min_{e\in\mathsf E}\kappa_e,
 \quad D=n^2-2,
 \quad t_* =\frac{2(D\log2+\log3)}{(n-1)\kappa_*},
 \quad a_* =3^{-2N}e^{-2Mt_*}=3^{-2N}e^{-4nBt_*}.
\end{equation}
These constants are dimensionally consistent: $t_*$ is inverse energy,
$M$ is energy, and $a_*$ is dimensionless. They are estimates, not a
claim of optimal constants.

\begin{lemma}\label{lem:heat}
The integral kernel of $P_t=e^{-tH_0}$ satisfies
\begin{equation}\label{eq:kernelbounds}
 2^{-N}\leq p_{t_*}(U,V)\leq(3/2)^N
 \qquad\hbox{for all }U,V\in\mathcal Q.
\end{equation}
\end{lemma}
\begin{proof}
We give the representation constants to fix the heat time and Lie
metric exactly. The irreducibles of $\SU(n)$ are indexed by
$m=(m_1,\ldots,m_{n-1})\in\mathbb Z_{\geq0}^{n-1}$, with
$\lambda_m=\sum_i m_i\omega_i$. In the usual Euclidean root space
$\{x\in\mathbb R^n:\sum x_i=0\}$ with roots $e_i-e_j$ of squared
length two, set
\[
 \omega_i=\sum_{j=1}^i e_j-\frac in\sum_{j=1}^n e_j,
 \quad \rho_{\rm rt}=\sum_{i=1}^{n-1}\omega_i.
\]
The dimension and the $g_T$-Casimir eigenvalue are
\begin{align}
 d_m&=\prod_{1\leq i<j\leq n}
       \frac{\sum_{q=i}^{j-1}m_q+j-i}{j-i},\label{eq:dim}\\
 C_m&=\frac12(\lambda_m,\lambda_m+2\rho_{\rm rt}).\label{eq:casimir}
\end{align}
These standard representation identities can be read in row coordinates
in \cite{PolychronakosSfetsos}. To spell out the dictionary and constants,
put $\ell_i=\sum_{q=i}^{n-1}m_q$, $\ell_n=0$, and $L=\sum_i\ell_i$.
The highest weight has coordinates $\ell_i-L/n$, and
$2\rho_{{\rm rt},i}=n+1-2i$. Thus \eqref{eq:casimir} says explicitly
\[
 C_m=\frac12\left[\sum_{i=1}^n\ell_i(\ell_i+n+1-2i)-\frac{L^2}{n}\right].
\]
The dimension formula follows from the character alternant
$\det(z_i^{\ell_j+n-j})/\det(z_i^{n-j})$ by letting all $z_i$ tend to
one: the first nonzero alternant terms are the two Vandermonde
determinants in $\ell_j+n-j$ and $n-j$, whose ratio is
\eqref{eq:dim}. The Casimir formula follows by applying the Cartan and
root decomposition of the quadratic Casimir to a highest weight
vector: the Cartan term gives $(\lambda_m,\lambda_m)$, and commuting
each positive-root raising operator past its lowering operator gives
$2(\lambda_m,\rho_{\rm rt})$; the factor $1/2$ is fixed by
\eqref{eq:fundcasimir}. Hence the metric normalization is the one used
in \eqref{eq:H}, rather than an unspecified heat-kernel convention.

Write $k=\sum_i m_i$. Direct scalar multiplication gives
$(\omega_i,\rho_{\rm rt})=i(n-i)/2$. Since
$(\lambda_m,\lambda_m)\geq0$ and $i(n-i)\geq n-1$,
\[
 C_m\geq\frac{n-1}{2}k,\qquad
 d_m\leq(k+1)^{n(n-1)/2}.
\]
The number of $m$ with this sum $k$ is
$\binom{k+n-2}{n-2}\leq(k+1)^{n-2}$: the first $n-2$ entries determine
the last, and each has at most $k+1$ choices. This also covers $n=2$.

Peter--Weyl orthogonality and the Casimir action give the single-edge
heat kernel
\[
 q_s(g)=\sum_m d_m e^{-sC_m}\chi_m(g).
\]
Indeed convolution by $d_m\chi_m$ projects onto the matrix coefficients
of the corresponding irreducible (with the inverse in the kernel
argument if needed), and the heat operator multiplies that subspace by
$e^{-sC_m}$. The series is absolutely uniformly convergent for every
$s>0$: a unitary representation has $|\chi_m(g)|\leq d_m$, and the
above bounds majorize the nonconstant terms by a polynomial in $k$
times $e^{-s(n-1)k/2}$. This also proves finite eigenvalue multiplicities
and divergence of the eigenvalues used in Lemma \ref{lem:ground}.
The constant representation contributes one. For edge $e$ and time $t$,
\begin{align*}
 |q_{\kappa_et}(g)-1|
 &\leq\sum_{k\geq1}(k+1)^D e^{-\kappa_et(n-1)k/2}\\
 &\leq\sum_{k\geq1}\left(2^D e^{-\kappa_et(n-1)/2}\right)^k.
\end{align*}
The second inequality uses $k+1\leq2^k$ for integer $k\geq1$, proved
by induction. At $t=t_*$ the ratio is at most $1/3$, so the sum is at
most $1/2$. Thus $1/2\leq q_{\kappa_et_*}\leq3/2$. The free generator
is the sum of commuting edge generators on the product space, so its
kernel is the product of these $N$ kernels. This proves
\eqref{eq:kernelbounds}.
\end{proof}

\begin{lemma}\label{lem:comparison}
For every continuous $f\geq0$ and $t\geq0$,
\begin{equation}\label{eq:semigroupcomparison}
 e^{-Mt}P_tf\leq e^{-tH}f\leq P_tf.
\end{equation}
Consequently the exact vacuum satisfies
\begin{equation}\label{eq:densitybounds}
 \frac{\max\psi_0}{\min\psi_0}\leq3^Ne^{Mt_*},\qquad
 \frac{\min\rho}{\max\rho}\geq a_*,\qquad
 a_*\leq\rho(U)\leq a_*^{-1}\quad(U\in\mathcal Q).
\end{equation}
\end{lemma}
\begin{proof}
Write $\mathcal A=\sum_e\kappa_e\Delta_e^T$, so
$P_t=e^{t\mathcal A}$. The parabolic maximum principle on this compact
manifold says that a solution of
$(\partial_t-\mathcal A+V)u\geq0$ with nonnegative initial data is
nonnegative when $V\geq0$. One direct proof replaces $u$ by
$e^{-ct}u+\epsilon$ with $c>0$, considers a first negative minimum,
and uses that $\partial_tu\leq0$, $\mathcal Au\geq0$ at that point;
the positive zero-order coefficient makes the differential inequality
impossible. Letting $\epsilon\downarrow0$ proves the result. Smooth
approximation covers continuous initial data.
Apply this principle first to $u=e^{-tH}f$ to get $u\geq0$.
The free solution $v=P_tf$ is also nonnegative by the same argument
with $V=0$. Now
$(\partial_t-\mathcal A+V)v=Vv\geq0$, so $v-u\geq0$.
For $w=e^{-Mt}v$ the corresponding expression is
$(V-M)w\leq0$, so $u-w\geq0$. This proves
\eqref{eq:semigroupcomparison} with no approximation of $V$.

Apply it to $f=\psi_0$ and use
$e^{-tH}\psi_0=e^{-tE_0}\psi_0$. At time $t_*$, letting
$I_0=\int\psi_0d\lambda>0$, Lemma \ref{lem:heat} gives
\[
 e^{(E_0-M)t_*}2^{-N}I_0
 \leq\psi_0(U)\leq e^{E_0t_*}(3/2)^NI_0.
\]
Take the ratio of upper to lower bounds and square to obtain the first
two assertions in \eqref{eq:densitybounds}. Since $\int\rho d\lambda=1$,
$\min\rho\leq1\leq\max\rho$. The ratio bound then gives
$\min\rho\geq a_*\max\rho\geq a_*$ and
$\max\rho\leq\min\rho/a_*\leq a_*^{-1}$, as required.
\end{proof}

\begin{theorem}\label{thm:finite-bounds}
For every simple edge loop,
\begin{equation}\label{eq:momentbounds}
 a_*\leq r_C\leq n^2-a_*(n^2-1),\qquad
 a_*(n^2-1)\leq n^2-r_C\leq n^2-a_*.
\end{equation}
For every such loop carrying a nontrivial center charge,
\begin{equation}\label{eq:quotientbounds}
 \frac{K_C}{2n}\frac{a_*(n^2-1)}{n^2-a_*(n^2-1)}
 \leq Q_C\leq
 \frac{K_C}{2n}\frac{n^2-a_*}{a_*}.
\end{equation}
The full finite-lattice spectral gap, and also its gauge-invariant
restriction above the unique vacuum, obey the genuine lower bound
\begin{equation}\label{eq:gapbound}
 \operatorname{gap}(H)\geq a_*\kappa_*\frac{n^2-1}{2n}>0.
\end{equation}
\end{theorem}
\begin{proof}
The density inequality $\rho\geq a_*$ and Lemma \ref{lem:Haar-loop}
give $r_C\geq a_*$ and
$n^2-r_C\geq a_*(n^2-1)$ by integrating the two nonnegative functions.
These prove all of \eqref{eq:momentbounds}. For a charged loop the
function $r\mapsto(n^2-r)/r$ is strictly decreasing for $r>0$;
substitute the two endpoints into \eqref{eq:chargedquotient} to get
\eqref{eq:quotientbounds}.

For \eqref{eq:gapbound}, first the exact free-product gap is
$g_0=\kappa_*C_F$. To verify the least nonzero single-edge Casimir,
compute
$(\omega_i,\omega_j)=\min(i,j)-ij/n>0$ for $1\leq i,j\leq n-1$.
If $m_i\geq1$, all coefficients in
$C(\lambda_m)-C(\omega_i)$ are nonnegative in the expansion in
fundamental weights. Hence
\[
 C_m\geq C(\omega_i)
 =\frac{i(n-i)(n+1)}{2n}\geq\frac{n^2-1}{2n}.
\]
Equality occurs for a fundamental or antifundamental representation.
On the product space each nonconstant matrix coefficient has at least
one such nonzero edge term; taking a fundamental coefficient on an
edge with $\kappa_e=\kappa_*$ realizes $g_0$. Peter--Weyl expansion
therefore proves the free Poincare inequality
$\mathcal E_\lambda(f,f)\geq g_0\Var_\lambda(f)$.
For any complex $f$, the variational identity
$\Var_\mu(f)=\min_{c\in\mathbb C}\int|f-c|^2d\mu$ gives
\[
 \Var_\mu(f)\leq(\max\rho)\Var_\lambda(f),\qquad
 \mathcal E_\mu(f,f)\geq(\min\rho)\mathcal E_\lambda(f,f).
\]
Consequently
$\mathcal E_\mu(f,f)\geq[(\min\rho)/(\max\rho)]g_0\Var_\mu(f)
\geq a_*g_0\Var_\mu(f)$.
The exact unitary ground-state transform identifies this weighted
Poincare infimum with the spectral gap of $H$. Restricting the infimum
to gauge-invariant functions can only increase it, and the ground
state belongs to that subspace by Lemma \ref{lem:ground}.
\end{proof}

The quotient bounds and the spectral bound have different logical
roles: the upper bound on any one orthogonal trial quotient is an upper
bound on the spectral gap, while a lower bound on that one quotient
alone is not. Equation \eqref{eq:gapbound} is valid because its proof
covers every form-domain vector. All constants in
\eqref{eq:constants} retain volume and coupling dependence. For example,
$a_*$ decreases exponentially in $N$ even with $B$ fixed, and also
decreases with $Bt_*$. Thus none of these inequalities asserts a
strictly positive lower bound after removing a cutoff or taking
infinite volume, and none proves that the limiting gap vanishes.

For a normalization check only, if $V$ is identically zero then
$\psi_0=1$, $r_C=1$, and $m_C=0$ for a simple loop, yielding
$Q_C=K_CC_F$. This is an exact special case of the formula, not a
replacement for the positive-coupling vacuum. The stated interacting
results above apply with all $b_p>0$.

\section{Disjoint parallel plaquettes, covariance Fourier sums, and spectral weight}

Let $p_j$, $j=0,\ldots,m-1$, be simple plaquettes whose physical-edge
supports are pairwise disjoint. Define
\[
 W_j=W_{p_j},\quad f_j=W_j-\mu(W_j),\quad
 c_j(k)=e^{ikj},\quad F_k=\sum_{j=0}^{m-1}c_j(k)f_j.
\]
The mean subtraction is necessary for center-neutral plaquettes. It
gives $\mu(F_k)=0$ for every real $k$ without any translation assumption.
For each edge at most one $f_j$ has a nonzero derivative, so pointwise
\begin{equation}\label{eq:disjointnumerator}
 \Gamma_\kappa(F_k,F_k)
 =\sum_j|c_j(k)|^2\Gamma_\kappa(W_j,W_j)
 =\sum_j\frac{K_j}{2n}(n^2-|W_j|^2),
 \quad K_j=\sum_{e\in p_j}\kappa_e.
\end{equation}
In particular its exact vacuum expectation is independent of $k$:
\begin{equation}\label{eq:Ek}
 E_k:=\mu(\Gamma_\kappa(F_k,F_k))
      =\sum_j\frac{K_j}{2n}(n^2-r_j),\qquad r_j=\mu(|W_j|^2).
\end{equation}
Edge disjointness says nothing about statistical independence in
$\mu$. The full variance is
\begin{equation}\label{eq:Dk}
 D_k:=\mu(|F_k|^2)
 =\sum_{j,l=0}^{m-1}e^{ik(j-l)}C_{jl},\qquad
 C_{jl}=\mu\bigl[(W_j-\mu W_j)\overline{(W_l-\mu W_l)}\bigr].
\end{equation}
All plaquette interactions, including plaquettes meeting more than one
of these supports or connecting them indirectly, remain in $C_{jl}$.
The covariance matrix is Hermitian positive semidefinite because its
quadratic form is the displayed squared $L^2(\mu)$ norm.
In fact $D_k>0$: if $F_k$ were constant, varying an edge unique to $p_j$
would force $W_j$ to be constant, which it is not. Positivity of $\rho$
then gives strictly positive variance. The exact quotient is
\begin{equation}\label{eq:disjointquotient}
 Q_k=\frac{E_k}{D_k}.
\end{equation}

Suppose now the specified finite lattice and its full lists of couplings
are invariant under a translation $\tau$ of order $m$ taking $p_j$ to
$p_{j+1}$ cyclically with their chosen orientations. Such a translation
preserves $H$ and Haar measure and therefore $\psi_0$ and $\mu$ by the
same uniqueness argument as for gauge transformations. There are then
constants $K_j=K$, $r_j=r$ and a cyclic covariance
\[
 C(d)=\mu(f_{l+d}\overline{f_l}),\qquad d\in\mathbb Z/m\mathbb Z,
\]
independent of $l$. For the allowed cyclic wave numbers
$k=2\pi q/m$, $q\in\{0,\ldots,m-1\}$, set
$\widehat C(k)=\sum_{d=0}^{m-1}e^{ikd}C(d)$. Regrouping the full
double sum in \eqref{eq:Dk}, with $j=l+d$, proves
\begin{equation}\label{eq:Fourierquotient}
 D_k=m\widehat C(k),\qquad
 E_k=m\frac{K}{2n}(n^2-r),\qquad
 Q_k=\frac{K(n^2-r)}{2n\widehat C(k)}.
\end{equation}
Here $\widehat C(k)$ is real and strictly positive because it equals
$D_k/m$; $C(-d)=\overline{C(d)}$ also proves reality directly.
There is no algebraic $k^2$ factor in this numerator. Obtaining a
small quotient in this family requires the actual interacting ratio
on the right of \eqref{eq:Fourierquotient} to become small. An assertion
that all covariances vanish, or that the denominator has prescribed
small-$k$ behavior, is not contained in edge disjointness.

For real plaquette energy observables $A_j=n-\Rea W_j$, replace $f_j$
by $A_j-\mu A_j$ and use the same coefficients. All support and covariance
arguments remain exact, but the local numerator is
\begin{equation}\label{eq:real-localnumerator}
 e_j^{\rm real}
 =\frac{K_j}{4}\left[n-\mu\bigl(\Rea\tr(H_{p_j}^2)\bigr)
                       -\frac2n\mu\bigl((\Ima W_j)^2\bigr)\right]
\end{equation}
by \eqref{eq:realenergy}. Thus under the same cyclic invariance
$Q_k=e^{\rm real}/\widehat C_A(k)$ with $\widehat C_A$ the full covariance
transform of $A_j$. Replacing this local numerator by the complex
Wilson numerator would lose terms unless equality is proved in the
particular group and observable.

Finally let $\mathsf P_{H-E_0}(\cdot)$ be the spectral projection measure
of the nonnegative self-adjoint operator $H-E_0$ on the invariant
Hilbert space. The normalized state and its scalar spectral probability
measure are
\begin{equation}\label{eq:spectralmeasure}
 v_k=\frac{\psi_0F_k}{\sqrt{D_k}},\qquad
 \nu_k(A)=\langle v_k,\mathsf P_{H-E_0}(A)v_k\rangle.
\end{equation}
The orthogonality $\langle\psi_0,v_k\rangle=0$ and uniqueness of the
vacuum imply $\nu_k(\{0\})=0$. The spectral theorem and the ground-state
identity prove the exact interacting first moment
\begin{equation}\label{eq:firstmoment}
 \int_{[0,\infty)}\omega\,d\nu_k(\omega)=Q_k=\frac{E_k}{D_k}.
\end{equation}
For every $\epsilon>0$, integrating
$\epsilon\mathbf 1_{[\epsilon,\infty)}(\omega)\leq\omega$ gives
\[
 \nu_k([\epsilon,\infty))\leq Q_k/\epsilon.
\]
This is the exact connection between the computed variation and
low-energy spectral weight. It makes no unproved assertion about
$\widehat C(k)$, a continuum Hamiltonian, an infinite-volume vacuum,
or convergence of the measures $\nu_k$.

\section{Verification and scope}

The companion script \texttt{check\_wilson\_exact.py} uses exact SymPy
arithmetic. On 8 September 2026 it completed with 1,012 exact scalar
assertions, together with exact matrix-entry assertions. It verifies
the basis, Fierz and Casimir constants for $\SU(2)$, $\SU(3)$, $\SU(4)$;
the factor-four metric dictionary; explicit noncommuting $\SU(3)$
positive and negative edge variations and their cross contractions;
real trace energy; a repeated physical edge with opposite signs;
and the one-coordinate product-rule identity underlying
\eqref{eq:groundform}. The proofs above are for all $n\geq2$ and are
not inferred from those finite checks. The script does not compute
$\psi_0$, the interacting covariance matrix, or a continuum spectrum.

All main identities here concern the exact finite interacting
Hamiltonian \eqref{eq:H}. They give explicit trial vectors and their
exact relation to its spectral measure, as well as a positive but
nonuniform finite-volume spectral bound. These proved relations can
be carried into a separate continuum or geometric construction only
through a proved state-space and operator map with controlled limits;
no such map is claimed to be established by the present finite-lattice
calculation.

\begin{thebibliography}{9}
\bibitem{PeterWeyl}
F. Peter and H. Weyl,
\emph{Die Vollst\"andigkeit der primitiven Darstellungen einer
geschlossenen kontinuierlichen Gruppe},
Mathematische Annalen \textbf{97} (1927), 737--755.
\href{https://doi.org/10.1007/BF01447892}{doi:10.1007/BF01447892}.
This is the foundational compact-group completeness theorem used to
identify the complete free spectral resolution.

\bibitem{PolychronakosSfetsos}
A. P. Polychronakos and K. Sfetsos,
\emph{Composing arbitrarily many $SU(N)$ fundamentals},
Nuclear Physics B \textbf{994} (2023), 116314,
\href{https://arxiv.org/abs/2305.19345}{arXiv:2305.19345}.
The row/weight dictionary and dimension/Casimir expressions are given
in Sections 2 and 4, including equation (4.30). Our symbol $n$ is that
paper's $N$; the derivations and all bounds used here retain the
specified anti-Hermitian basis convention.
\end{thebibliography}
\end{document}

```

## Complete source: wilson_variation/temporal_transfer.tex

```latex
\documentclass[11pt]{article}
\usepackage[margin=1in]{geometry}
\usepackage{amsmath,amssymb,amsthm,mathtools}
\usepackage{mathrsfs}
\usepackage[hidelinks]{hyperref}
\newtheorem{theorem}{Theorem}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{proposition}[theorem]{Proposition}
\newcommand{\SU}{\operatorname{SU}}
\newcommand{\tr}{\operatorname{tr}}
\newcommand{\Rea}{\operatorname{Re}}
\newcommand{\dd}{\,\mathrm d}
\title{Exact SU(2) Wilson transfer operator and the finite-spatial-lattice time limit}
\author{}
\date{8 September 2026}
\begin{document}
\maketitle

\section{Retained action, coefficients, and conventions}

Fix $a>0$ and $g_{\rm YM}>0$. The spatial regulator is a fixed finite
oriented cubical graph with vertices $\mathsf V$, physical spatial edges
$\mathsf E$, and the full set $\mathsf P_s$ of its geometric spatial
plaquettes, each included once, with $|\mathsf E|\geq1$.
Open spatial boundary conditions or a
fixed periodic spatial lattice are both allowed. Reverse traversal uses
$U_e^{-1}$, not a second independent link. Write $N=|\mathsf E|$ and
\[
 \mathcal Q=\SU(2)^{\mathsf E},\qquad
 \mathcal H=L^2(\mathcal Q,\lambda),\qquad
 d\lambda=\prod_{e\in\mathsf E}dU_e,
\]
with probability Haar on each link. The spatial graph, $a$, and
$g_{\rm YM}$ stay fixed in every limit in this paper.

The original invariant Lie metric and continuum action are
\begin{equation}\label{eq:original-action}
 c(X,Y)=-\frac12\tr(XY),\qquad
 S(\mathscr A)=\frac1{2g_{\rm YM}^2}
 \int\sum_{\mu<\nu}c(F_{\mu\nu},F_{\mu\nu})\,d^4x.
\end{equation}
For time spacing $\epsilon>0$, retain exactly
\begin{equation}\label{eq:anisotropic}
 b_t(\epsilon)=\frac{a}{2g_{\rm YM}^2\epsilon},\qquad
 b_s(\epsilon)=\frac{\epsilon}{2g_{\rm YM}^2a}.
\end{equation}
For the frozen-curvature holonomy $e^{\delta F}$,
$2-\Rea\tr e^{\delta F}=\delta^2c(F,F)+O_F(\delta^4)$ on
$\mathfrak{su}(2)$, by the exponential series, tracelessness and the
paired eigenvalues of $F$. The exact coefficient checks are
\[
 \frac{b_t(a\epsilon)^2}{a^3\epsilon}
 =\frac1{2g_{\rm YM}^2},\qquad
 \frac{b_sa^4}{a^3\epsilon}=\frac1{2g_{\rm YM}^2}.
\]
These equalities record the prescribed classical action convention.
The transfer calculation below uses the full compact plaquette action,
not a curvature truncation, and proves no spatial continuum limit.

Choose $T_1,T_2,T_3\in\mathfrak{su}(2)$ with
$-2\tr(T_aT_b)=\delta_{ab}$, for example $T_a=i\sigma_a/2$ with the
Pauli matrices. Define
\[
 X_{e,a}f(U)=\left.\frac d{dt}\right|_{0}
 f(\ldots,e^{tT_a}U_e,\ldots),\qquad
 \Delta_e^T=\sum_{a=1}^3X_{e,a}^2.
\]
In the original metric, $c(T_a,T_b)=\delta_{ab}/4$, so the
$c$-orthonormal basis is $S_a=2T_a$, and
\begin{equation}\label{eq:metricdictionary}
 X^c_{e,a}=2X_{e,a},\qquad \Delta_e^c=4\Delta_e^T.
\end{equation}
The probability Haar convention changes no operator coefficient. If
$d\operatorname{vol}_c=\mathcal V_c d\lambda$ on this compact product,
$f\mapsto\sqrt{\mathcal V_c}f$ is the exact unitary change from
$L^2(d\operatorname{vol}_c)$ to $L^2(d\lambda)$ and intertwines the same
differential operators.

The original inverse-transport gauge law and the convention used in the
companion Hamiltonian derivation are related at the configuration level by
\begin{equation}\label{eq:gaugedictionary}
 (\beta_hU)_e=h_{s(e)}^{-1}U_eh_{t(e)},\qquad
 (\alpha_gU)_e=g_{s(e)}U_eg_{t(e)}^{-1},\qquad
 \alpha_gU=\beta_hU\ \text{when }g_v=h_v^{-1}\text{ for every }v.
\end{equation}
Inversion preserves Haar, so their vertex gauge averages are the same
operator. No link variable is inverted by this dictionary; only the
parameter describing the same vertex change is replaced by its inverse.

\section{The exact single-link character multiplier}

For $b>0$, let
\begin{equation}\label{eq:kernel}
 Z(b)=\int_{\SU(2)}e^{b\Rea\tr U}dU,\qquad
 k_b(U)=\frac{e^{b\Rea\tr U}}{Z(b)},\qquad
 (\mathcal K_b f)(U')=\int k_b(U'U^{-1})f(U)dU.
\end{equation}
Every $U\in\SU(2)$ has eigenvalues $e^{i\theta},e^{-i\theta}$ with
$0\leq\theta\leq\pi$. Probability Haar integration of a class function is
\[
 \int f(U)dU=\frac2\pi\int_0^\pi f(\theta)\sin^2\theta\,d\theta.
\]
For example, write $U=w_0I+i\sum_{a=1}^3w_a\sigma_a$ on the unit
three-sphere. Slicing at $w_0=\cos\theta$ gives density
$(2/\pi)\sqrt{1-w_0^2}dw_0$, which is the displayed formula.

Define the integer-order modified Bessel functions by their entire series
\begin{equation}\label{eq:Besselseries}
 I_d(2b)=\sum_{r=0}^{\infty}\frac{b^{2r+d}}{r!(r+d)!},
 \qquad d\in\mathbb Z_{\geq0}.
\end{equation}
They also satisfy
\begin{equation}\label{eq:Besselintegral}
 I_d(2b)=\frac1\pi\int_0^\pi e^{2b\cos\theta}\cos(d\theta)\,d\theta.
\end{equation}
To prove this, multiply the uniformly absolutely convergent series for
$e^{bz}$ and $e^{b/z}$ on $|z|=1$. The coefficient of $z^d$ is
\eqref{eq:Besselseries}, and Fourier orthogonality gives
\eqref{eq:Besselintegral}. For $d\geq1$, integration of the derivative
of $e^{2b\cos\theta}\sin(d\theta)$ over $[0,\pi]$ gives
\begin{equation}\label{eq:recurrence}
 I_{d-1}(2b)-I_{d+1}(2b)=\frac db I_d(2b).
\end{equation}
The endpoint term is zero, and
$2\sin\theta\sin(d\theta)=\cos((d-1)\theta)-\cos((d+1)\theta)$
fixes every coefficient in this recurrence.

The spin-$j$ irreducible representation has $j\in\frac12\mathbb Z_{\geq0}$,
dimension $d=2j+1$, and character
\[
 \chi_j(\theta)=\sum_{r=0}^{d-1}e^{i(d-1-2r)\theta}
 =\frac{\sin(d\theta)}{\sin\theta}.
\]
The finite sum is the character of the $(d-1)$st symmetric power of the
defining representation; its equality with the sine quotient is the
finite geometric-series identity, including endpoint values by
continuity. These are all irreducibles of $\SU(2)$, and their matrix
coefficients are complete by Peter--Weyl \cite{PeterWeyl}.

\begin{theorem}\label{thm:multiplier}
The exact normalization and the exact spin-$j$ multiplier of
\eqref{eq:kernel} are
\begin{equation}\label{eq:multiplier}
 Z(b)=\frac{I_1(2b)}b,\qquad
 \mathcal K_bD^j_{rs}=m_j(b)D^j_{rs},\qquad
 m_j(b)=\frac{I_{2j+1}(2b)}{I_1(2b)}.
\end{equation}
For every $j$ and $b>0$, $0<m_j(b)\leq1$, and $m_0(b)=1$.
The operator $\mathcal K_b$ is a positive self-adjoint contraction,
is injective, and is trace class.
\end{theorem}
\begin{proof}
The exact unnormalized character integral is
\begin{align*}
 \int e^{b\Rea\tr U}\chi_j(U)dU
 &=\frac2\pi\int_0^\pi e^{2b\cos\theta}
                      \sin\theta\sin(d\theta)d\theta\\
 &=I_{d-1}(2b)-I_{d+1}(2b)=\frac dbI_d(2b).
\end{align*}
Set $d=1$ to obtain $Z(b)$. Since $k_b$ is central, the matrix
$\int k_b(W)D^j(W^{-1})dW$ commutes with the representation and hence
is scalar. Its trace divided by $d$ is
$(dZ(b))^{-1}\int e^{b\Rea\tr W}\chi_j(W)dW=I_d/I_1$.
The substitution $U=W^{-1}U'$ in \eqref{eq:kernel} proves the asserted
matrix-coefficient eigenvalue. In particular the dimension factor in
the character integral is exactly canceled by division by $d$; no
dimension factor remains in the multiplier.

All terms in \eqref{eq:Besselseries} are positive for $b>0$, which
proves $m_j>0$. The integral expression for the normalized multiplier
and $|\chi_j(U)|\leq d$ prove $|m_j|\leq1$. The matrix coefficients
form an orthogonal complete basis, so these real positive eigenvalues
prove positivity, self-adjointness, contraction, and injectivity.
For fixed $b$, \eqref{eq:Besselseries} gives
$I_d(2b)\leq b^de^{b^2}/d!$, since $(r+d)!\geq d!$.
Thus
\[
 \tr\mathcal K_b=\sum_{d=1}^{\infty}d^2\frac{I_d(2b)}{I_1(2b)}<\infty,
\]
where the multiplicity is exactly $d^2$. The factorial majorant proves
the convergence and hence trace-classness.
\end{proof}

\section{Controlled small-time derivative of the full compact kernel}

\begin{lemma}\label{lem:asymptotic}
For each fixed spin $j$,
\begin{equation}\label{eq:large-b}
 m_j(b)=1-\frac{j(j+1)}b+O_j(b^{-2})\qquad(b\longrightarrow\infty).
\end{equation}
The estimate is proved from the exact compact integral and does not
replace that integral by a different finite-$b$ kernel.
\end{lemma}
\begin{proof}
Set $y=1-\cos\theta\in[0,2]$. Under the probability density $k_b dU$,
the density of $y$ is proportional to
$e^{-2by}y^{1/2}(2-y)^{1/2}dy$. Write
\[
 J_q(b)=\int_0^2e^{-2by}y^{q+1/2}(2-y)^{1/2}dy,
 \qquad q=0,1,2.
\]
On $[0,1]$, Taylor's theorem with a bounded second derivative gives
$\sqrt{2-y}=\sqrt2(1-y/4)+R(y)$, with $|R(y)|\leq C y^2$.
The part on $[1,2]$ is bounded by a constant times $e^{-2b}$.
The tails when extending the two leading integrals to $[0,\infty)$
have the same exponentially small order times a polynomial in $b$.
Finally, the error integral over $[0,1]$ is bounded by
$C\int_0^\infty e^{-2by}y^{q+5/2}dy$.
Using the exact substitution $z=2by$ in these gamma integrals gives
\begin{equation}\label{eq:J-expansion}
 J_q(b)=\frac{\sqrt2\,\Gamma(q+3/2)}{(2b)^{q+3/2}}
 \left[1-\frac{q+3/2}{8b}+O_q(b^{-2})\right].
\end{equation}
Every error assertion follows from the displayed remainder bound and
the exponentially small tail; none extends a finite-$b$ probability
measure by declaration. Since $J_0>0$, division gives
\[
 \mathbb E_b[y]=\frac{J_1}{J_0}=\frac3{4b}+O(b^{-2}),\qquad
 \mathbb E_b[y^2]=\frac{J_2}{J_0}=\frac{15}{16b^2}+O(b^{-3}).
\]
The character $\chi_j$ is the polynomial $U_{d-1}(\cos\theta)$, where
$U_0(x)=1$, $U_1(x)=2x$, and
$U_{r+1}(x)=2xU_r(x)-U_{r-1}(x)$. Induction at $x=1$ gives
\[
 U_{d-1}(1)=d,\qquad U'_{d-1}(1)=\frac{d(d^2-1)}3.
\]
For the derivative formula, differentiate the recurrence; the induction
step is
$U'_{r+1}(1)=2(r+1)+2U'_r(1)-U'_{r-1}(1)$, which the displayed
cubic expression satisfies with its initial values. Polynomial Taylor
expansion on the whole compact interval $y\in[0,2]$ therefore yields
\[
 \frac{\chi_j(\theta)}d
 =1-\frac{d^2-1}{3}y+R_j(y),\qquad |R_j(y)|\leq C_jy^2.
\]
Its exact $\mathbb E_b$ average is $m_j(b)$. Substitute the two moment
estimates and use $(d^2-1)/4=j(j+1)$ to prove \eqref{eq:large-b}.
\end{proof}

Substitution of the retained $b_t$ gives the exact infinitesimal
coefficient
\begin{equation}\label{eq:epsilonmultiplier}
 m_j(b_t(\epsilon))
 =1-\epsilon\frac{2g_{\rm YM}^2}{a}j(j+1)+O_j(\epsilon^2).
\end{equation}
For the chosen basis, $-\Delta^T$ has eigenvalue $j(j+1)$ on spin $j$.
Indeed take the displayed Pauli basis and put $J_a=-i\,dD^j(T_a)$.
Its anti-Hermitian generators satisfy $[T_a,T_b]=-\varepsilon_{abc}T_c$,
so the Hermitian generators satisfy $[J_a,J_b]=i\varepsilon_{abc}J_c$.
Let $J_\pm=J_1\pm iJ_2$. Directly from these commutators,
$[J_3,J_\pm]=\pm J_\pm$ and
$\sum_aJ_a^2=J_-J_++J_3^2+J_3$. On the highest vector
$e_1^{\otimes 2j}$ of the symmetric power, $J_3$ has eigenvalue $j$
and $J_+$ is zero, so the sum of squares has value $j(j+1)$.
Expanding its commutator with each $J_a$ shows it commutes with all
three; irreducibility therefore extends this value to the whole
representation. An orthogonal change to any other specified
orthonormal $T$ basis leaves the sum of squares unchanged.
For $j=1/2$, it is explicitly
$-\sum_aT_a^2=3I/4$, fixing the absolute scale. Thus
\eqref{eq:epsilonmultiplier} has precisely the $\Delta^T$ convention,
and \eqref{eq:metricdictionary} supplies the other metric.

On the full finite edge product define
\begin{equation}\label{eq:freeproduct}
 (K_\epsilon f)(U')=
 \int_{\mathcal Q}\prod_{e\in\mathsf E}
 k_{b_t(\epsilon)}(U'_eU_e^{-1})f(U)d\lambda(U),
 \qquad
 H_0=-\frac{2g_{\rm YM}^2}{a}\sum_e\Delta_e^T.
\end{equation}
A product matrix coefficient with spins $\boldsymbol j=(j_e)$ has
$K_\epsilon$ eigenvalue $\prod_em_{j_e}(b_t(\epsilon))$ and
$H_0$ eigenvalue $(2g_{\rm YM}^2/a)\sum_ej_e(j_e+1)$.
For every finite linear combination $f$ of such coefficients,
\begin{equation}\label{eq:corederivative}
 \lim_{\epsilon\downarrow0}\frac{K_\epsilon f-f}{\epsilon}=-H_0f.
\end{equation}
This follows by the finite product expansion of
\eqref{eq:epsilonmultiplier}, not by an assertion uniform over arbitrary
spins. Contraction and density then imply $K_\epsilon f\to f$ for every
$f\in\mathcal H$: approximate $f$ by a fixed finite combination and
bound the two approximation errors by its distance from $f$.

\section{Exact magnetic factor and temporal-link Gauss integration}

For the ordered spatial plaquette holonomy $U_p$, set
\begin{equation}\label{eq:magnetic}
 V(U)=\frac1{2g_{\rm YM}^2a}
        \sum_{p\in\mathsf P_s}(2-\Rea\tr U_p),\qquad
 M_\epsilon f(U)=e^{-\epsilon V(U)/2}f(U).
\end{equation}
Every magnetic plaquette is present in this sum. It is a bounded
nonnegative real smooth multiplication operator, with
$0\leq V\leq2|\mathsf P_s|/(g_{\rm YM}^2a)$.
In particular $\epsilon V=b_s\sum_p(2-\Rea\tr U_p)$ exactly.

Define the vertex gauge average
\begin{equation}\label{eq:Gauss}
 (P_Gf)(U)=\int_{\SU(2)^{\mathsf V}}f(\alpha_gU)\prod_vdg_v.
\end{equation}
Every pullback in the integrand is unitary. Haar inversion proves
$P_G^*=P_G$, Haar invariance in two successive integrals proves
$P_G^2=P_G$, and another left translation of the integration variable
shows that the range consists exactly of the invariant functions.
Thus $P_G$ is the orthogonal projection onto
$\mathcal H_{\rm inv}$. Equation \eqref{eq:gaugedictionary} proves that
it is also the original-$h$ Gauss average. Gauge invariance of spatial
Wilson traces proves $M_\epsilon P_G=P_GM_\epsilon$.
The identity
\[
 (\alpha_gU')_e(\alpha_gU)_e^{-1}
 =g_{s(e)}U'_eU_e^{-1}g_{s(e)}^{-1}
\]
and centrality of $k_b$ prove that $K_\epsilon$ commutes with $P_G$.

To compute the temporal integral, write $U$ and $U'$ for two adjacent
spatial slices and $q_v$ for the temporal link at vertex $v$ from the
first slice to the second. In the original inverse-transport convention,
the oriented temporal plaquette associated to edge $e:s\to t$ is
\begin{equation}\label{eq:temporalplaquette}
 P_e(U',q,U)=U_eq_t(U'_e)^{-1}q_s^{-1}.
\end{equation}
Its inverse is $q_sU'_eq_t^{-1}U_e^{-1}$, and $\Rea\tr A^{-1}=
\Rea\tr A$ for a unitary matrix. Hence
\begin{equation}\label{eq:temporal-conjugacy}
 \Rea\tr P_e=\Rea\tr[(\alpha_qU')_eU_e^{-1}].
\end{equation}
This equality includes every temporal vertex variable; it makes no
global temporal gauge-fixing assumption. Under independent original
vertex changes $h^{(0)}$ and $h^{(1)}$ on the two slices,
\[
 U_e\mapsto(h_s^{(0)})^{-1}U_eh_t^{(0)},\quad
 U'_e\mapsto(h_s^{(1)})^{-1}U'_eh_t^{(1)},\quad
 q_v\mapsto(h_v^{(0)})^{-1}q_vh_v^{(1)}.
\]
Multiplication in \eqref{eq:temporalplaquette} cancels the intermediate
factors and gives $P_e\mapsto(h_s^{(0)})^{-1}P_eh_s^{(0)}$.
This verifies directly its original gauge law.

Define the raw two-slice Wilson kernel, with symmetric magnetic endpoint
weights, by
\begin{equation}\label{eq:rawkernel}
 \mathcal T_\epsilon^{\rm raw}(U',U)
 =e^{-\epsilon V(U')/2}e^{-\epsilon V(U)/2}
 \int\exp\!\left[-b_t\sum_e(2-\Rea\tr P_e(U',q,U))\right]\prod_vdq_v.
\end{equation}
The integral is over the whole non-Abelian group at every temporal
vertex. With
\begin{equation}\label{eq:scalar}
 c_\epsilon=[e^{-2b_t}Z(b_t)]^N,\qquad
 F_\epsilon=M_\epsilon K_\epsilon M_\epsilon,
\end{equation}
equations \eqref{eq:kernel} and \eqref{eq:temporal-conjugacy} give the
exact operator identity
\begin{equation}\label{eq:fulltransfer}
 \mathcal T_\epsilon^{\rm raw}
 =c_\epsilon M_\epsilon P_GK_\epsilon M_\epsilon
 =c_\epsilon F_\epsilon P_G
 =c_\epsilon P_GF_\epsilon.
\end{equation}
In particular the normalized transfer is $F_\epsilon$ on
$\mathcal H_{\rm inv}$ and $F_\epsilon P_G$ on $\mathcal H$.
The operator $F_\epsilon$ is positive, self-adjoint, injective and a
contraction because $K_\epsilon$ has those properties and
$M_\epsilon$ is positive, bounded, and invertible. Injectivity follows
from
$\langle f,F_\epsilon f\rangle=
\langle M_\epsilon f,K_\epsilon M_\epsilon f\rangle$ and the strictly
positive eigenvalues of $K_\epsilon$. All these statements remain
valid after restriction to the invariant subspace.

For several adjacent slices, the two half magnetic factors at each
interior slice multiply to $e^{-\epsilon V}$. On an open time interval
the two boundary slices carry half weights; on a periodic time lattice
all slices have their full weight. Fubini's theorem therefore identifies
the exact product of \eqref{eq:rawkernel} with the full anisotropic
Wilson integral, retaining all temporal and spatial plaquettes. In the
periodic case with $m$ time steps the exact partition identity is
\begin{equation}\label{eq:partition}
 Z_{\rm Wilson}^{(m)}
 =c_\epsilon^m\tr_{\mathcal H}(F_\epsilon^mP_G)
 =c_\epsilon^m\tr_{\mathcal H_{\rm inv}}(F_\epsilon^m).
\end{equation}
The traces are well defined: the proof of Theorem \ref{thm:multiplier}
gives a trace-class single-link operator, a finite tensor product is
trace class, and multiplication by bounded operators and $P_G$ preserves
that property. The integral and trace equality can also be checked by
successively integrating its positive continuous compact kernels.
Equation \eqref{eq:partition} is an exact finite-$\epsilon$ identity;
the strong convergence below alone is not used to assert trace-norm
convergence of these partition functions.

The Wilson constant and the normalization are explicitly retained as the
common energy shift
\begin{equation}\label{eq:shift}
 E_{\rm scalar}(\epsilon)
 =-\frac1\epsilon\log c_\epsilon
 =\frac N\epsilon\bigl[2b_t-\log Z(b_t)\bigr].
\end{equation}
In particular $0<c_\epsilon<1$, because
$e^{-2b}Z(b)=\int e^{-b(2-\Rea\tr U)}dU$ is a strictly positive average
of a function at most one and strictly below one on a set of positive
Haar measure. From the proved $J_0$ expansion,
\[
 e^{-2b}Z(b)=\frac1{2\sqrt\pi\,b^{3/2}}
             \left[1-\frac3{16b}+O(b^{-2})\right].
\]
Thus the shift is not finite as $\epsilon\downarrow0$; it is a known
scalar that affects all energies equally. The exact relation
\eqref{eq:fulltransfer}, rather than an unrecorded removal of constants,
specifies which operator has the finite time limit.

\section{The actual core and the strong time-continuum limit}

Let $\mathscr D$ be the finite linear span of product matrix coefficients
of all edge representations, and let $\mathscr D_{\rm inv}=P_G\mathscr D$.
Peter--Weyl completeness makes $\mathscr D$ dense in $\mathcal H$ and
$\mathscr D_{\rm inv}$ dense in $\mathcal H_{\rm inv}$. The gauge action
mixes only matrix coefficients with the same finite list of edge spins,
so $P_G\mathscr D\subset\mathscr D$. The diagonal positive operator $H_0$
in \eqref{eq:freeproduct} is self-adjoint on
\[
 D(H_0)=\left\{f:\sum_{\boldsymbol j,\boldsymbol r,\boldsymbol s}
 \left(\frac{2g_{\rm YM}^2}{a}\sum_ej_e(j_e+1)\right)^2
 |f_{\boldsymbol j,\boldsymbol r,\boldsymbol s}|^2<\infty\right\},
\]
where coefficients use an orthonormal matrix-coefficient basis.
Finite spectral truncation proves that $\mathscr D$ is an operator core:
both $f$ and $H_0f$ are approximated by the same finite sums. The
projection $P_G$ commutes with $H_0$, so applying it to these graph-norm
approximations proves the invariant core assertion as well.

Since $V$ in \eqref{eq:magnetic} is bounded and real, the operator
\begin{equation}\label{eq:resultH}
 H=H_0+V
 =-\frac{2g_{\rm YM}^2}{a}\sum_e\Delta_e^T
 +\frac1{2g_{\rm YM}^2a}\sum_{p\in\mathsf P_s}(2-\Rea\tr U_p)
\end{equation}
is self-adjoint and nonnegative on $D(H_0)$. Bounded perturbation does
not change the core, since the graph norms of $H_0$ and $H_0+V$ are
equivalent by the two inequalities
$\|Hf\|\leq\|H_0f\|+\|V\|\|f\|$ and its converse. All gauge
invariance statements persist. The original-metric expression is exactly
\begin{equation}\label{eq:resultHc}
 H=-\frac{g_{\rm YM}^2}{2a}\sum_e\Delta_e^c
 +\frac1{2g_{\rm YM}^2a}\sum_{p\in\mathsf P_s}(2-\Rea\tr U_p).
\end{equation}
No conventional redefinition of $g_{\rm YM}$ was used to obtain either
expression.

For $f\in\mathscr D$, use the exact algebraic decomposition
\[
 (F_\epsilon-I)f=(M_\epsilon-I)f
    +M_\epsilon(K_\epsilon-I)f
    +M_\epsilon K_\epsilon(M_\epsilon-I)f.
\]
Boundedness of $V$ gives
$(M_\epsilon-I)/\epsilon\to-V/2$ in operator norm. Equation
\eqref{eq:corederivative}, the strong convergence $K_\epsilon\to I$,
and the contraction bounds therefore prove
\begin{equation}\label{eq:Fderivative}
 \frac{F_\epsilon f-f}{\epsilon}\longrightarrow-Hf
 \quad\text{for every }f\in\mathscr D,
\end{equation}
and in particular for every $f\in\mathscr D_{\rm inv}$. The magnetic
operator need not commute with the kinetic operator for this argument.

\begin{theorem}\label{thm:stronglimit}
For every fixed $t>0$ and every $f\in\mathcal H$,
\begin{equation}\label{eq:stronglimit}
 F_{t/m}^{\,m}f\longrightarrow e^{-tH}f
 \qquad(m\longrightarrow\infty).
\end{equation}
Consequently the exact normalized Wilson transfer obeys
\begin{equation}\label{eq:projectedlimit}
 \left(c_{t/m}^{-1}\mathcal T_{t/m}^{\rm raw}\right)^mf
 =F_{t/m}^{\,m}P_Gf\longrightarrow e^{-tH}P_Gf.
\end{equation}
On $\mathcal H_{\rm inv}$ the limit is the strongly continuous
semigroup $e^{-tH}$, with generator \eqref{eq:resultH} or equivalently
\eqref{eq:resultHc}. At $t=0$ its identity is $I$ on that subspace;
on the unrestricted space the projected family has value $P_G$.
\end{theorem}
\begin{proof}
We give the positive-contraction specialization of the product-formula
argument directly; the general framework is Chernoff's theorem
\cite{Chernoff}. Put
$A_\epsilon=(I-F_\epsilon)/\epsilon$. It is bounded, self-adjoint and
nonnegative, and \eqref{eq:Fderivative} gives
$A_\epsilon f\to Hf$ on the operator core $\mathscr D$.
For any $\lambda_0>0$ and $f\in\mathscr D$,
\begin{equation}\label{eq:resolventidentity}
 (\lambda_0+A_\epsilon)^{-1}(\lambda_0+H)f-f
 =(\lambda_0+A_\epsilon)^{-1}(H-A_\epsilon)f\longrightarrow0.
\end{equation}
The resolvents have norms at most $1/\lambda_0$. Moreover
$(\lambda_0+H)\mathscr D$ is dense: for arbitrary $u$, apply a
graph-norm approximation from $\mathscr D$ to
$f=(\lambda_0+H)^{-1}u$. Thus the uniform bound extends
\eqref{eq:resolventidentity} to all vectors and proves
$(\lambda_0+A_\epsilon)^{-1}\to(\lambda_0+H)^{-1}$ strongly.

For completeness this implies $e^{-tA_\epsilon}\to e^{-tH}$ strongly
for each fixed $t>0$ without any estimate of an unknown spectrum.
Set $R_\epsilon=(\lambda_0+A_\epsilon)^{-1}$ and
$R=(\lambda_0+H)^{-1}$. On $[0,1/\lambda_0]$ define the continuous
function
\[
 h_t(y)=\begin{cases}\exp[-t(y^{-1}-\lambda_0)],&y>0,\\0,&y=0.
 \end{cases}
\]
Uniform polynomial approximation on this interval and strong convergence
of every polynomial in the uniformly bounded $R_\epsilon$ prove
$h_t(R_\epsilon)\to h_t(R)$ strongly. The spectral calculus identifies
these two operators with the desired semigroups.

It remains to compare powers with this exponential. For integer $m\geq1$
and $0\leq x\leq1$,
\begin{equation}\label{eq:scalarpower}
 0\leq e^{-mx}-(1-x)^m\leq\frac1m.
\end{equation}
For $x\leq1/2$, the integral identity
$-\log(1-x)-x=\int_0^x u/(1-u)du\leq x^2$ gives
\[
 e^{-mx}-(1-x)^m
 \leq mx^2e^{-mx}\leq\frac4{e^2m}<\frac1m.
\]
For $x\geq1/2$ the difference is at most $e^{-m/2}\leq2/(em)<1/m$;
the last inequality follows by maximizing $s e^{-s/2}$ for $s>0$.
The endpoint $x=1$ also satisfies the bound. Spectral calculus with
$x=I-F_\epsilon=\epsilon A_\epsilon$ now yields
\[
 \|F_\epsilon^m-e^{-m\epsilon A_\epsilon}\|\leq1/m.
\]
Take $\epsilon=t/m$ and combine with the established strong convergence
of $e^{-tA_{t/m}}$. This proves \eqref{eq:stronglimit}.
Finally \eqref{eq:fulltransfer}, $P_G^2=P_G$, and commutation with
$F_\epsilon$ prove \eqref{eq:projectedlimit}. The same reasoning
applies directly on the verified invariant core.
\end{proof}

\section{Effective Hamiltonians and the exact finite-vacuum bridge}

On $\mathcal H_{\rm inv}$, positivity and injectivity allow the
self-adjoint functional-calculus definition
\begin{equation}\label{eq:effectiveH}
 H_\epsilon=-\epsilon^{-1}\log(F_\epsilon|_{\mathcal H_{\rm inv}}),
 \qquad
 H_\epsilon^{\rm raw}=E_{\rm scalar}(\epsilon)I+H_\epsilon.
\end{equation}
Zero is not an eigenvalue of $F_\epsilon$, so the logarithm is densely
defined even though zero is a spectral accumulation point. The operator
$H_\epsilon$ is nonnegative. Equation \eqref{eq:effectiveH} is the exact
scalar-energy dictionary, and the raw and normalized effective operators
have identical energy differences and eigenvectors at each $\epsilon$.

They satisfy $H_\epsilon\to H|_{\mathcal H_{\rm inv}}$ in the strong
resolvent sense. Here is a direct consequence of the proof already given,
which also covers arbitrary $\epsilon\downarrow0$ rather than only
$t/m$. Fix $t>0$ and set $m_\epsilon=\lfloor t/\epsilon\rfloor$ and
$t_\epsilon=m_\epsilon\epsilon$. The power comparison gives
$\|F_\epsilon^{m_\epsilon}-e^{-t_\epsilon A_\epsilon}\|
\leq1/m_\epsilon$. For $t_\epsilon\geq t/2$, the scalar mean-value
bound yields
\[
 \sup_{x\geq0}|e^{-t_\epsilon x}-e^{-tx}|
 \leq|t-t_\epsilon|\sup_{x\geq0}xe^{-(t/2)x}
 \leq\frac{2\epsilon}{et}\longrightarrow0.
\]
Thus $F_\epsilon^{m_\epsilon}\to e^{-tH}$ strongly. If
$t/\epsilon=m_\epsilon+\delta$ with $0\leq\delta<1$, then for
$0\leq z\leq1$,
\[
 0\leq z^{m_\epsilon}-z^{m_\epsilon+\delta}
 \leq z^{m_\epsilon}(1-z)
 \leq\frac1{m_\epsilon+1}.
\]
The middle inequality uses $z^\delta\geq z$, and the last follows by
maximizing $z^m(1-z)$. Applying spectral calculus gives
$e^{-tH_\epsilon}=F_\epsilon^{t/\epsilon}\to e^{-tH}$ strongly.
For any $\lambda_0>0$ the resolvent identity
\[
 (\lambda_0+H_\epsilon)^{-1}f
 =\int_0^\infty e^{-\lambda_0t}e^{-tH_\epsilon}f\,dt
\]
and the uniform contraction bound permit dominated convergence in norm,
proving the asserted strong resolvent convergence.

The resulting Hamiltonian is precisely the finite interacting one in
the companion derivation, with the explicit substitution
\begin{equation}\label{eq:companiondictionary}
 n=2,\qquad \kappa_e=\frac{2g_{\rm YM}^2}{a},\qquad
 b_p^{\rm Hamiltonian}=\frac1{2g_{\rm YM}^2a}
                       =\frac{b_s(\epsilon)}\epsilon.
\end{equation}
All magnetic interactions survive this limit. This yields a concrete
state-space and operator map from the finite anisotropic Wilson integral
to the vacuum-weighted finite-lattice identities; it does not identify
the interacting vacuum with Haar measure.

For example, let $\psi_0>0$ be the normalized exact ground state of
\eqref{eq:resultH}, $E_0$ its eigenvalue, and $d\mu=\psi_0^2d\lambda$.
The finite compact elliptic Hamiltonian has this unique ground state
by the positivity and compact-resolvent argument in the companion
paper. For any nonzero smooth gauge-invariant $F$ with $\mu(F)=0$, put
$u=\psi_0F$ and $D=\|u\|^2>0$. The exact ground-state product rule gives
\begin{equation}\label{eq:vacuumform}
 \langle u,(H-E_0)u\rangle
 =\frac{2g_{\rm YM}^2}{a}\sum_{e,a}\int|X_{e,a}F|^2d\mu.
\end{equation}
To see the cancellation, expand
$X^2(\psi_0F)=\psi_0X^2F+2(X\psi_0)XF+F X^2\psi_0$,
subtract $F(H-E_0)\psi_0=0$, and integrate each Haar-skew derivative
by parts. The remaining integral is exactly \eqref{eq:vacuumform}.
Thus no component of $V$ was omitted in passing to that form.

The strong transfer limit proves the concrete correlation identity
\begin{equation}\label{eq:correlation}
 \lim_{m\to\infty}
 \frac{\langle u,F_{t/m}^{\,m}u\rangle}
      {\langle\psi_0,F_{t/m}^{\,m}\psi_0\rangle}
 =\langle u,e^{-t(H-E_0)}u\rangle
 =D\int_{[0,\infty)}e^{-t\omega}d\nu_F(\omega),
\end{equation}
where $\nu_F(A)=D^{-1}\langle u,\mathbf1_A(H-E_0)u\rangle$.
The denominator converges to $e^{-tE_0}>0$. The raw scalar
$c_{t/m}^m$ cancels exactly if both numerator and denominator are
written using the raw transfer. The state $\psi_0$ in
\eqref{eq:correlation} is the actual limiting finite-lattice vacuum,
not a constant trial state. The spectral theorem and
\eqref{eq:vacuumform} give its first moment
\[
 \int\omega\,d\nu_F(\omega)
 =\frac{(2g_{\rm YM}^2/a)\sum_{e,a}\mu(|X_{e,a}F|^2)}{\mu(|F|^2)}.
\]
These are fixed-spatial-regulator statements. Strong time convergence
alone does not supply a spatial continuum vacuum, a limiting spectral
gap, or a gapless interacting four-dimensional quantum theory.

\section{Exact checks and provenance}

The companion script \texttt{check\_temporal\_coefficients.py} completed
237 exact scalar assertions plus exact matrix-entry checks. It verifies
the two anisotropic action coefficients, Bessel recurrence coefficients
through bounded formal orders, the character derivatives for dimensions
1 through 9, the resulting spin coefficients, the SU(2) metric and
Casimir constants, a noncommuting temporal-plaquette example and its
original gauge law, the $g=h^{-1}$ dictionary, and the magnetic endpoint
weights. The all-spin and operator convergence proofs are the analytic
arguments above; they are not inferred from finitely many checked spins.
No numerical integration, spatial continuum calculation, or approximate
vacuum was used.

\begin{thebibliography}{9}
\bibitem{PeterWeyl}
F. Peter and H. Weyl, \emph{Die Vollst\"andigkeit der primitiven
Darstellungen einer geschlossenen kontinuierlichen Gruppe},
Mathematische Annalen \textbf{97} (1927), 737--755,
\href{https://doi.org/10.1007/BF01447892}{doi:10.1007/BF01447892}.

\bibitem{Chernoff}
P. R. Chernoff, \emph{Note on product formulas for operator semigroups},
Journal of Functional Analysis \textbf{2} (1968), 238--242,
\href{https://doi.org/10.1016/0022-1236(68)90020-7}
{doi:10.1016/0022-1236(68)90020-7}.
The positive self-adjoint contraction specialization needed here is
proved directly in Theorem \ref{thm:stronglimit}.
\end{thebibliography}
\end{document}

```

## Complete source: wilson_variation/spatial_vacuum_elimination.tex

```latex
\documentclass[11pt]{article}
\usepackage[margin=1in]{geometry}
\usepackage{amsmath,amssymb,amsthm,mathtools,mathrsfs}
\usepackage[hidelinks]{hyperref}
\newtheorem{theorem}{Theorem}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{corollary}[theorem]{Corollary}
\newcommand{\SU}{\operatorname{SU}}
\newcommand{\tr}{\operatorname{tr}}
\newcommand{\Rea}{\operatorname{Re}}
\newcommand{\Var}{\operatorname{Var}}
\newcommand{\dd}{\,\mathrm d}
\title{Exact spatial elimination in the true lattice vacuum:\\marginals, temporal memory, and excitation estimates}
\author{}
\date{8 September 2026}
\begin{document}
\maketitle

\section{The finite interacting Hamiltonian and its actual vacuum}

Let $n\geq2$. Fix a finite lattice with physical oriented links
$\mathsf E$, all its retained oriented plaquette words $\mathsf P$, and
positive coefficients $\kappa_e,b_p$. Reverse traversal uses $U_e^{-1}$.
Take precisely
\begin{equation}\label{eq:H}
 H=-\sum_{e\in\mathsf E}\kappa_e\sum_{a=1}^{n^2-1}X_{e,a}^2
       +\sum_{p\in\mathsf P}b_p(n-\Rea\tr U_p),\qquad
 X_{e,a}f=\left.\frac d{dt}\right|_0f(\ldots,e^{tT_a}U_e,\ldots),
\end{equation}
where $T_a$ is anti-Hermitian, traceless, and
$-2\tr(T_aT_b)=\delta_{ab}$. Its Hilbert space is the probability-Haar
space $L^2(\mathcal Q,\lambda)$ on $\mathcal Q=\SU(n)^{\mathsf E}$.
Every potential term in \eqref{eq:H} is retained. The original metric
$c(X,Y)=-\tfrac12\tr(XY)$ has orthonormal basis $2T_a$ and
$\Delta_e^c=4\sum_aX_{e,a}^2$. Hence the same kinetic operator is
$-\sum_e(\kappa_e/4)\Delta_e^c$.

Let $\psi_0$ be the actual positive normalized ground state,
$H\psi_0=E_0\psi_0$ and $\int\psi_0^2d\lambda=1$. Existence,
smoothness, strict positivity, uniqueness, and gauge invariance hold
for this finite compact elliptic Schr\"odinger operator; they are proved
for \eqref{eq:H} in \texttt{wilson\_finite\_lattice.tex}. Set
\[
 \rho=\psi_0^2,\quad d\mu=\rho d\lambda,\quad
 \mathbb H=L^2(\mathcal Q,\mu),\quad \mathcal Uu=\psi_0u.
\]
The map $\mathcal U:\mathbb H\to L^2(\lambda)$ is unitary, and the
exact ground-state transform is
\begin{align}
 L&=\mathcal U^{-1}(H-E_0)\mathcal U
   =-\rho^{-1}\sum_{e,a}\kappa_eX_{e,a}(\rho X_{e,a}),\label{eq:L}\\
 q(u,v)&=\langle L^{1/2}u,L^{1/2}v\rangle_\mu
   =\sum_{e,a}\kappa_e\int\overline{X_{e,a}u}X_{e,a}v\,d\mu.
   \label{eq:fullform}
\end{align}
Indeed the product rule in $H(\psi_0u)-uH\psi_0$ gives the displayed
divergence operator, and Haar integration by parts gives the form.
These steps use the eigenvalue equation for the full potential.

All inner products below are conjugate-linear in the first argument.
The form domain $\mathcal V$ of $q$ is $H^1(\mathcal Q)$: the fields
span the tangent spaces and the positive smooth $\rho$ is bounded
above and below on the compact product. Its form norm is
$\|u\|_\mathcal V^2=q(u,u)+\|u\|_\mu^2$. Smooth functions are a form
core, and the smooth weighted elliptic operator has domain $H^2$ and
smooth operator core. The compact Sobolev embedding gives compact
resolvent. If $q(u,u)=0$, every derivative is zero and connectedness
gives a constant function. Consequently the kernel is exactly
$\mathbb C1$ and the first nonzero eigenvalue $\delta$ is positive.
These are finite-regulator assertions; $\delta$ is not assumed to have
a positive bound uniform in a spatial continuum limit.

\section{The true marginal, conditional projection, and retained form}

Split the physical links into two disjoint nonempty sets
$\mathsf E=\mathsf S\sqcup\mathsf R$. There is no independence
assumption and no restriction on shared plaquettes in the operator
calculation. Write
\[
 \mathcal Q=\mathcal Q_S\times\mathcal Q_R,\quad U=(s,r),\quad
 d\lambda=d\lambda_Sd\lambda_R,
\]
and define
\begin{equation}\label{eq:marginal}
 \rho_R(r)=\int_{\mathcal Q_S}\rho(s,r)d\lambda_S(s),\qquad
 d\mu_R=\rho_Rd\lambda_R,\qquad
 p(s\mid r)=\frac{\rho(s,r)}{\rho_R(r)}.
\end{equation}
Differentiation under a compact integral proves that $\rho_R$ is smooth.
Its positivity follows from $\rho>0$, and
$\int\rho_Rd\lambda_R=1$ by Fubini. The density $p$ is also smooth
and positive and integrates to one for each $r$.

Let $\mathbb K=L^2(\mathcal Q_R,\mu_R)$ and define
\begin{equation}\label{eq:conditional}
 (Jf)(s,r)=f(r),\qquad
 (J^*u)(r)=\int p(s\mid r)u(s,r)d\lambda_S(s),\qquad
 P=JJ^*,\quad Q=I-P.
\end{equation}
Fubini proves $\|Jf\|_\mu=\|f\|_{\mu_R}$ and
$\langle Jf,u\rangle_\mu=\langle f,J^*u\rangle_{\mu_R}$.
Jensen's inequality proves $\|J^*u\|\leq\|u\|$. Therefore $P$ is
the orthogonal projection onto functions of the retained links, and
\[
 \mathbb H=J\mathbb K\oplus\mathbb H_Q,\qquad
 \mathbb H_Q=\ker J^*=Q\mathbb H.
\]
In particular every $h\in\mathbb H_Q$ is orthogonal to $1=J1$.

For a retained index $i=(e,a)$ with $e\in\mathsf R$, write $X_i=X_{e,a}$
and $\kappa_i=\kappa_e$. These fields act on $r$ and leave $s$ fixed.
Define the real conditional score
\begin{equation}\label{eq:score}
 \ell_i=X_i\log\rho,\qquad
 \bar\ell_i=X_i\log\rho_R,\qquad
 \sigma_i=\ell_i-J\bar\ell_i=X_i\log p(s\mid r).
\end{equation}
Compactness makes every $\sigma_i$ and its derivatives bounded.
Differentiation of \eqref{eq:marginal} gives
$J^*\ell_i=\bar\ell_i$, so $J^*\sigma_i=0$.

\begin{lemma}\label{lem:projection-domain}
Conditional expectation satisfies the exact derivative identity
\begin{equation}\label{eq:conditional-derivative}
 X_iJ^*u=J^*(X_i u)+J^*(\sigma_i u)
\end{equation}
for smooth $u$. It extends boundedly from $\mathcal V$ to
$\mathcal V_R:=H^1(\mathcal Q_R)$, with
\begin{equation}\label{eq:projection-bound}
 a(J^*u,J^*u)\leq2q(u,u)+2\eta\|u\|_\mu^2,
 \quad
 \eta=\sum_{i\in R}\kappa_i\|\sigma_i\|_\infty^2,
\end{equation}
where
\begin{equation}\label{eq:reducedform}
 a(f,g)=\sum_{i\in R}\kappa_i\int\overline{X_if}X_ig\,d\mu_R.
\end{equation}
Both $P$ and $Q$ preserve the full form domain and are bounded for its
norm. The lift $J$ identifies $\mathcal V_R$ with
$\mathcal V\cap J\mathbb K$.
\end{lemma}
\begin{proof}
Differentiate $J^*u=\int p u\,d\lambda_S$ and use $X_ip=p\sigma_i$.
Conditional Cauchy--Schwarz and Fubini give
$\|J^*X_iu\|_{\mu_R}\leq\|X_iu\|_\mu$ and
$\|J^*(\sigma_i u)\|_{\mu_R}\leq\|\sigma_i\|_\infty\|u\|_\mu$.
Squaring their sum with $(x+y)^2\leq2x^2+2y^2$ and summing all
retained $\kappa_i$ proves \eqref{eq:projection-bound}.
Smooth approximation extends the derivative identity in the weak
Sobolev sense and the norm bound to $\mathcal V$. Since
$q(Jf,Jf)=a(f,f)$ and $J$ is an isometry in $L^2$, this proves the
claims about $P$ and $Q$. Conversely the weak retained derivatives of
$Jf$ are the lifts of those of $f$, so $Jf\in\mathcal V$ implies
$f\in\mathcal V_R$. Repeated differentiation of the compact conditional
integral also shows $J^*:H^k(\mathcal Q)\to H^k(\mathcal Q_R)$ is
bounded for each nonnegative integer $k$; in particular these maps
preserve smooth functions.
\end{proof}

The form $a$ is closed on $\mathcal V_R$ and has the self-adjoint
weighted elliptic generator
\begin{equation}\label{eq:A}
 A=-\rho_R^{-1}\sum_{i\in R}\kappa_iX_i(\rho_RX_i),
 \qquad D(A)=H^2(\mathcal Q_R).
\end{equation}
For a nonconstant smooth retained observable $F$, let
$f=F-\mu_R(F)$ and $u_F=\psi_0Jf$. Then
\begin{equation}\label{eq:Rayleigh}
 \langle\psi_0,u_F\rangle_\lambda=0,\qquad
 \frac{\langle u_F,(H-E_0)u_F\rangle_\lambda}{\|u_F\|_\lambda^2}
 =\frac{\displaystyle\sum_{i\in R}\kappa_i\mu_R(|X_iF|^2)}
        {\displaystyle\mu_R(|F|^2)-|\mu_R(F)|^2}.
\end{equation}
The numerator follows from \eqref{eq:fullform}, since the eliminated-link
derivatives of $Jf$ vanish; the denominator and orthogonality follow
from Fubini. Positivity of $\rho_R$ makes the denominator strictly
positive. Eliminated kinetic coefficients and all magnetic coefficients
still affect $\psi_0$, $\rho_R$, and the conditional density.

For the original gauge law $U_e\mapsto h_{s(e)}^{-1}U_eh_{t(e)}$,
the same vertex transformation acts separately on $s$ and $r$.
Gauge invariance of $\rho$ and Haar substitution in $s$ prove
$\rho_R(h\cdot r)=\rho_R(r)$ and covariance of $p(s\mid r)$.
Thus $J,J^*,P,Q$ intertwine these gauge actions. The equally valid law
$g_{s(e)}U_eg_{t(e)}^{-1}$ uses $g_v=h_v^{-1}$ and gives exactly the
same subspaces. Every formula therefore restricts to gauge-invariant
observables and vectors. For such a nonconstant $F$, \eqref{eq:Rayleigh}
is an upper bound on the physical finite-lattice gap. The infimum of
these quotients over retained invariant functions is at least the
infimum over all full invariant functions; a lower bound on one
retained quotient alone is not a full spectral lower bound.

\section{The exact coupling to eliminated functions and its domains}

For $f\in C^\infty(\mathcal Q_R)$, expand \eqref{eq:L} and compare
with \eqref{eq:A}. The retained second-derivative terms cancel, and
all eliminated derivatives of $Jf$ are zero. Hence
\begin{equation}\label{eq:B}
 LJf=JAf+Bf,\qquad
 Bf=-\sum_{i\in R}\kappa_i\sigma_i J(X_if),\qquad J^*Bf=0.
\end{equation}
This is the exact first-order map from retained variation to the
eliminated subspace. It extends boundedly
$B:\mathcal V_R\to\mathbb H_Q$, because
\begin{equation}\label{eq:Bbound}
 \|Bf\|_\mu^2\leq\eta\,a(f,f).
\end{equation}
Pointwise Cauchy--Schwarz with the factors $\sqrt{\kappa_i}\sigma_i$
and $\sqrt{\kappa_i}X_if$, followed by integration, proves this bound.
The exact squared norm retains the full conditional covariance:
\begin{equation}\label{eq:Fisher}
 \|Bf\|_\mu^2
 =\int\sum_{i,j\in R}\kappa_i\kappa_j
       I_{ij}(r)\overline{X_if(r)}X_jf(r)\,d\mu_R(r),
 \quad I_{ij}=J^*(\sigma_i\sigma_j).
\end{equation}
The matrix $I(r)$ is positive semidefinite by the exact identity
\[
 \sum_{i,j}\overline z_i I_{ij}(r)z_j
 =J^*\left(\left|\sum_i z_i\sigma_i\right|^2\right)(r)\geq0.
\]
Because $J^*\ell_i=\bar\ell_i$, it is exactly the conditional covariance
of $X_i\log\rho$ and $X_j\log\rho$ under $p(s\mid r)$.

Define $\mathcal V_Q=\mathcal V\cap\mathbb H_Q$ and restrict the
full form:
\begin{equation}\label{eq:Cform}
 c_Q(h,k)=q(h,k),\qquad h,k\in\mathcal V_Q.
\end{equation}
This is a closed densely defined nonnegative form on $\mathbb H_Q$.
Closedness follows since $\mathbb H_Q$ is $L^2$ closed. Density and a
form core follow by applying the bounded $Q$ of Lemma
\ref{lem:projection-domain} to smooth approximations; thus
$Q C^\infty(\mathcal Q)$ is a form core. Let $C$ be its associated
self-adjoint operator. There is no unsupported assertion here that
the formal differential compression $QLQ$ has an automatically chosen
operator domain. The form determines the domain uniquely by
\[
 D(C)=\{h\in\mathcal V_Q:\text{there exists }v\in\mathbb H_Q
       \text{ with }c_Q(k,h)=\langle k,v\rangle
       \text{ for every }k\in\mathcal V_Q\},\quad Ch=v.
\]
For smooth $h\in\mathbb H_Q$ this definition gives $Ch=QLh$ by
integration by parts. Since every $h\in\mathbb H_Q$ is orthogonal to
$1$, the full Poincare inequality gives
\begin{equation}\label{eq:Cgap}
 c_Q(h,h)\geq\delta\|h\|_\mu^2,
 \qquad C\geq\delta I>0.
\end{equation}
In particular $C^{-1}$ exists as a bounded operator. It and all
$(C+z)^{-1}$, $z\geq0$, map into $D(C)\subset\mathcal V_Q$.

For $f,g\in\mathcal V_R$ and $h,k\in\mathcal V_Q$, the exact block
form is
\begin{equation}\label{eq:blockform}
 q(Jf+h,Jg+k)=a(f,g)+\langle Bf,k\rangle
                         +\langle h,Bg\rangle+c_Q(h,k).
\end{equation}
For smooth functions this follows from \eqref{eq:B}; the bounded map
$B:\mathcal V_R\to\mathbb H_Q$ and the form-domain decomposition in
Lemma \ref{lem:projection-domain} extend it to the displayed domains.

The adjoint coupling has an explicit expression as well. For smooth
$h\in\mathbb H_Q$, Haar integration by parts in $r$ gives
\begin{equation}\label{eq:Bstar}
 B^*h=\rho_R^{-1}\sum_{i\in R}\kappa_i
                   X_i\bigl(\rho_R J^*(\sigma_i h)\bigr).
\end{equation}
Indeed $\langle Bf,h\rangle=-\sum_i\kappa_i
\int\rho_R\overline{X_if}J^*(\sigma_ih)d\lambda_R$, which becomes
$\langle f,B^*h\rangle$ with the sign in \eqref{eq:Bstar}.
Using \eqref{eq:conditional-derivative} with $u=\sigma_i h$ expands it
as the finite sum
\[
 B^*h=\sum_{i\in R}\kappa_i
 \left[J^*(\sigma_iX_ih)+J^*((X_i\sigma_i)h)
       +J^*(\sigma_i^2h)+\bar\ell_iJ^*(\sigma_i h)\right].
\]
Every coefficient is bounded, so this formula extends to a bounded map
$B^*:\mathcal V_Q\to\mathbb K$. On $\mathbb H_Q$ without this
regularity, the symbol $B^*$ is instead the bounded dual map into
$\mathcal V_R^*$ specified by $\langle f,B^*h\rangle=\langle Bf,h\rangle$.
These two definitions agree on their common domain.

Replacing $X_i$ by $X_i^c=2X_i$, $\sigma_i$ by $2\sigma_i$, and every
kinetic coefficient by $\kappa_i/4$ leaves \eqref{eq:A}, \eqref{eq:B},
and \eqref{eq:blockform} unchanged. This records the full original
metric dictionary for the eliminated coupling as well as for $H$.

\section{Exact compressed resolvents as closed Schur forms}

For $z>0$, put $R_z=(C+z)^{-1}$ and define on $\mathcal V_R$
\begin{equation}\label{eq:Schurform}
 s_z(f,g)=a(f,g)+z\langle f,g\rangle-\langle Bf,R_zBg\rangle.
\end{equation}
The last term is well defined by \eqref{eq:Bbound}. All occurrences of
$B^*R_zB$ below mean this form on the stated domain, not a product of
unbounded operators with unspecified domains.

\begin{theorem}\label{thm:Schur}
The form $s_z$ is closed, positive, and coercive on $\mathcal V_R$.
Its self-adjoint operator $S_z$ obeys $S_z\geq zI$ and
\begin{equation}\label{eq:Schurresolvent}
 J^*(L+z)^{-1}J=S_z^{-1}
   =\left[A+z-B^*(C+z)^{-1}B\right]^{-1}.
\end{equation}
The eliminated component of $(L+z)^{-1}Jg$ is exactly
$-R_zB S_z^{-1}g$. Moreover, in operator order,
\begin{equation}\label{eq:resolventorder}
 J^*(L+z)^{-1}J\ \geq\ (A+z)^{-1}.
\end{equation}
\end{theorem}
\begin{proof}
The block form and completion of the square give, for every
$f\in\mathcal V_R$, $h\in\mathcal V_Q$,
\begin{equation}\label{eq:square}
 q(Jf+h,Jf+h)+z(\|f\|^2+\|h\|^2)
 =s_z(f,f)+\|(C+z)^{1/2}(h+R_zBf)\|^2.
\end{equation}
Thus $s_z(f,f)$ is the infimum over $h$, uniquely attained at
$h=-R_zBf$, and nonnegativity of $q$ gives $s_z(f,f)\geq z\|f\|^2$.
For an explicit form-norm lower bound, apply
\eqref{eq:projection-bound} to $v=Jf+h$, for which $J^*v=f$:
\[
 a(f,f)+\|f\|^2
 \leq2q(v,v)+(2\eta+1)\|v\|^2
 \leq K_z\bigl(q(v,v)+z\|v\|^2\bigr),
 \quad K_z=\max\{2,(2\eta+1)/z\}.
\]
Take the minimizing $h$ to obtain
$s_z(f,f)\geq K_z^{-1}(a(f,f)+\|f\|^2)$.
Conversely $s_z(f,f)\leq a(f,f)+z\|f\|^2$ by choosing $h=0$.
These two bounds make its norm equivalent to the complete
$\mathcal V_R$ norm and prove closedness and coercivity. The
associated operator therefore exists and is at least $zI$.

For $g\in\mathbb K$, let $v=(L+z)^{-1}Jg$ and decompose it as
$v=Jf+h$ using the bounded form projection. The weak resolvent
equation tested against $k\in\mathcal V_Q$ gives
$c_Q(k,h)+z\langle k,h\rangle=-\langle k,Bf\rangle$.
The definition of $C$ proves $h=-R_zBf$. Testing against $Jf'$ for
$f'\in\mathcal V_R$ then gives
$s_z(f',f)=\langle f',g\rangle$, so $f=S_z^{-1}g$.
This proves both the compressed inverse and the reconstruction formula
with their domains resolved.

Finally, $s_z(f,f)\leq a(f,f)+z\|f\|^2$. For a positive coercive
closed form $t$ with associated operator $T$, completing the square in
its form space gives
$\langle g,T^{-1}g\rangle=\sup_f[2\Rea\langle g,f\rangle-t(f,f)]$.
Applying this formula to the two forms proves
\eqref{eq:resolventorder}. It is an order statement for the resolvents;
no ordering of their time exponentials is inferred from it.
\end{proof}

This is a weighted, infinite-rank Schur complement. The projection and
effective-resolvent method itself is established in Feshbach's work and
in the modern Feshbach--Schur formulation \cite{Feshbach,DSS}. The proof
above supplies the conditional-score coupling, form domains, and
coercivity needed for this particular infinite-dimensional projection.

\section{Full temporal correlations and exact memory}

Define the compressed correlation operator on the retained Hilbert space
by
\begin{equation}\label{eq:Kt}
 K(t)=J^*e^{-tL}J,\qquad t\geq0.
\end{equation}
It is a positive self-adjoint contraction with $K(0)=I$ and $K(t)1=1$.
These statements follow respectively from positivity in the spectral
sense, contraction, the isometry $J$, and $L1=0$. Its matrix elements
are the actual full quantum vacuum correlations, since
\begin{equation}\label{eq:quantumcorrelation}
 \langle f,K(t)g\rangle_{\mu_R}
 =\langle\psi_0Jf,e^{-t(H-E_0)}\psi_0Jg\rangle_\lambda.
\end{equation}
The spectral theorem also gives its norm-convergent Laplace integral
\begin{equation}\label{eq:Laplace}
 \int_0^\infty e^{-zt}K(t)\,dt
 =J^*(L+z)^{-1}J=S_z^{-1},\qquad z>0.
\end{equation}
The integral is convergent in operator norm because $\|K(t)\|\leq1$.

\begin{theorem}\label{thm:memory}
For smooth initial $f_0\in C^\infty(\mathcal Q_R)$, set
$f(t)=K(t)f_0$. It satisfies the exact equation in $\mathbb K$
\begin{equation}\label{eq:memory}
 f'(t)=-Af(t)+\int_0^t B^*e^{-(t-s)C}Bf(s)\,ds,
 \qquad f(0)=f_0.
\end{equation}
The integral is a well-defined Bochner integral; its positive sign is
fixed by eliminating the other component of the full equation.
For every smooth $f$,
\begin{equation}\label{eq:secondmoment}
 \langle f,K(t)f\rangle
 =\|f\|^2-t\,a(f,f)
       +\frac{t^2}{2}\bigl(\|Af\|^2+\|Bf\|^2\bigr)+o(t^2).
\end{equation}
The equality $K(t)=e^{-tA}$ for all $t\geq0$ holds if and only if
$B=0$ on $\mathcal V_R$.
\end{theorem}
\begin{proof}
Let $v(t)=e^{-tL}Jf_0$ and $h(t)=Qv(t)$. Smooth initial data belong to
all powers of the compact elliptic operator $L$, so spectral calculus
and elliptic regularity make $v(t)$ smooth in space and continuously
differentiable in every required Sobolev norm for $t\geq0$. Lemma
\ref{lem:projection-domain} implies the same spatial regularity for
$f(t)=J^*v(t)$ and $h(t)$. The full equation $v'=-Lv$ and
\eqref{eq:blockform} therefore give
\[
 f'=-Af-B^*h,\qquad h'=-Bf-Ch,\qquad h(0)=0.
\]
For the second equation, differentiating
$e^{-(t-s)C}h(s)$ and integrating in $s$ gives
\begin{equation}\label{eq:eliminatedevolution}
 h(t)=-\int_0^te^{-(t-s)C}Bf(s)\,ds.
\end{equation}
This differentiation is justified since the smooth $h(s)$ lies in
$D(C)$ with $Ch(s)=QLh(s)$ continuously in $\mathbb H_Q$.

The map $B^*:\mathcal V_Q\to\mathbb K$ was proved bounded above.
Spectral calculus for $C\geq0$ gives
\[
 \|e^{-\tau C}\|_{\mathbb H_Q\to\mathcal V_Q}
 \leq1+(2e\tau)^{-1/2},\qquad\tau>0,
\]
because $\sup_{x\geq0}\sqrt{x}e^{-\tau x}=(2e\tau)^{-1/2}$.
Consequently the integrand in \eqref{eq:eliminatedevolution} is
integrable in the form norm near $s=t$, as $Bf(s)$ is continuous in
$\mathbb H_Q$. Applying the bounded $B^*$ to that form-norm integral
and substituting into the first equation proves \eqref{eq:memory}
as a strong $\mathbb K$ identity. This also specifies rigorously the
memory-kernel domain: $B^*e^{-\tau C}B$ maps $\mathcal V_R$ to
$\mathbb K$ for $\tau>0$, with an integrable $O(1+\tau^{-1/2})$
bound on bounded time intervals. This is an exact projection-memory
construction of the type introduced by Mori \cite{Mori}, with the
Euclidean generator and signs derived here.

For \eqref{eq:secondmoment}, apply the scalar spectral theorem to the
smooth vector $Jf$, which lies in $D(L^2)$. The zeroth, first and
second moments are $\|f\|^2$, $a(f,f)$, and
\[
 \|LJf\|_\mu^2=\|JAf+Bf\|_\mu^2=\|Af\|_{\mu_R}^2+\|Bf\|_\mu^2.
\]
The second-order Taylor remainder is $o(t^2)$ by dominated convergence
against its finite second spectral moment. This proves the expansion.
The corresponding expansion for $e^{-tA}$ has second coefficient
$\|Af\|^2/2$. Equality of all the correlation operators therefore
forces $Bf=0$ for every smooth $f$, and density and \eqref{eq:Bbound}
extend this to $\mathcal V_R$. Conversely, if $B=0$, the exact closed
form \eqref{eq:blockform} is the orthogonal direct sum of $a$ and $c_Q$.
Its self-adjoint operator and semigroup are direct sums as well, giving
$K(t)=e^{-tA}$.
\end{proof}

In particular the explicit second-derivative diagnostic is
\[
 \left.\frac{d^2}{dt^2}\right|_{t=0}
 \left[\langle Jf,e^{-tL}Jf\rangle_\mu
              -\langle f,e^{-tA}f\rangle_{\mu_R}\right]=\|Bf\|_\mu^2.
\]

For the unrestricted retained function space this condition has a
concrete statistical characterization:
\begin{equation}\label{eq:factorization}
 B=0\text{ on }\mathcal V_R
 \quad\Longleftrightarrow\quad
 \rho(s,r)=\rho_S(s)\rho_R(r)
 \text{ for positive probability densities }\rho_S,\rho_R.
\end{equation}
The reverse implication follows immediately from $\sigma_i=0$.
For the forward implication, \eqref{eq:B} vanishes for every smooth
test function $f$. The resulting functions are smooth, so vanishing
in $L^2$ means vanishing pointwise. At any fixed $r$, a smooth function
with arbitrary prescribed differential at $r$ is obtained from local
coordinates and a smooth cutoff. The independent tangent basis $X_i$
and positive $\kappa_i$ then force each $\sigma_i(s,r)=0$. Thus every
$r$ derivative of $p(s\mid r)$ is zero, and connectedness of
$\mathcal Q_R$ makes it independent of $r$. Normalization gives the
factorization. If one restricts tests to gauge-invariant functions,
the exact criterion is $B=0$ on that invariant form space; the stronger
factorization is not asserted from that smaller test space.

\section{Constructed excitation vectors using the eliminated resolvent}

The marginal quotient can be improved by an explicit full-state vector.
Let $0\ne f\in\mathcal V_R$ satisfy $\mu_R(f)=0$. For every $z\geq0$
define
\begin{equation}\label{eq:correctedstate}
 w_z=(C+z)^{-1}Bf,\qquad
 u_z=\psi_0(Jf-w_z).
\end{equation}
Equation \eqref{eq:Cgap} guarantees existence even at $z=0$, and
$w_z\in\mathcal V_Q$. Orthogonality gives
$\langle\psi_0,u_z\rangle_\lambda=0$ and
$\|u_z\|_\lambda^2=\|f\|_{\mu_R}^2+\|w_z\|_\mu^2>0$.
All gauge actions commute with the forms and their resolvents; hence
if $f$ is invariant, $u_z$ is invariant as well.
For a full original-Hilbert-space form-domain vector $u$, write
\[
 \mathfrak h_0[u]=\|(H-E_0)^{1/2}u\|_\lambda^2
                =q(u/\psi_0,u/\psi_0).
\]
This is the energy used below. It equals
$\langle u,(H-E_0)u\rangle$ when $u\in D(H)$, but no such stronger
domain membership is assumed for the constructed form-domain vector.

\begin{theorem}\label{thm:improvedtrial}
The actual full-Hamiltonian Rayleigh quotient of \eqref{eq:correctedstate}
is
\begin{equation}\label{eq:improvedquotient}
 \frac{\mathfrak h_0[u_z]}{\|u_z\|^2}
 =\frac{a(f,f)-\langle Bf,w_z\rangle-z\|w_z\|^2}
        {\|f\|^2+\|w_z\|^2}
 \leq\frac{a(f,f)}{\|f\|^2}.
\end{equation}
The inequality is strict whenever $Bf\ne0$. The numerator is
nonnegative. For $z=0$, $-w_0$ uniquely minimizes the full Dirichlet
energy among all $Jf+h$, $h\in\mathcal V_Q$, with the retained
conditional mean $f$ fixed.
\end{theorem}
\begin{proof}
The equation $(C+z)w_z=Bf$ gives
$c_Q(w_z,w_z)=\langle Bf,w_z\rangle-z\|w_z\|^2$.
Insert $h=-w_z$ in \eqref{eq:blockform}. The two cross terms subtract
$2\langle Bf,w_z\rangle$, yielding exactly the numerator in
\eqref{eq:improvedquotient}. It is nonnegative because it is the full
closed form $q(Jf-w_z,Jf-w_z)$. The scalar
$\langle Bf,w_z\rangle=\langle Bf,(C+z)^{-1}Bf\rangle$ is
nonnegative and strictly positive when $Bf\ne0$. The numerator is
therefore at most $a(f,f)$ and the denominator at least $\|f\|^2$;
when $Bf\ne0$ the numerator is strictly smaller. The base energy is
positive for a nonzero centered $f$, because $\rho_R>0$ on a connected
space. This proves the claimed strict inequality. Completion of the
square in \eqref{eq:square} with $z=0$ remains valid because $C>0$,
and proves the minimization statement.
\end{proof}

For a centered retained $f$, define the actual excitation spectral
probability measure
\[
 \nu_f(E)=\|f\|^{-2}
 \langle\psi_0Jf,\mathbf1_E(H-E_0)\psi_0Jf\rangle.
\]
Its first moment is $a(f,f)/\|f\|^2$, its second moment for smooth
$f$ is $(\|Af\|^2+\|Bf\|^2)/\|f\|^2$, and its Laplace transform
is $\langle f,K(t)f\rangle/\|f\|^2$. The corrected states have their
own actual spectral measures with first moment
\eqref{eq:improvedquotient}. In particular each invariant corrected
state gives a genuine upper bound on the full physical spectral gap;
none of these energies is assigned from an independently chosen
single-slice density.

\section{Exact nonlinear Wilson integration leading to this marginal}

We now construct the connection to the completed compact-link
integration. Specialize to $\SU(2)$ and the fixed spatial regulator
with the original action metric, spatial mesh $a>0$, and coupling
$g_{\rm YM}>0$. Retain
\begin{equation}\label{eq:physicalcoefficients}
 \kappa_e=\frac{2g_{\rm YM}^2}{a},\qquad
 b_p^{\rm Hamiltonian}=\frac1{2g_{\rm YM}^2a},\qquad
 b_t(\epsilon)=\frac{a}{2g_{\rm YM}^2\epsilon},\qquad
 b_s(\epsilon)=\frac{\epsilon}{2g_{\rm YM}^2a}.
\end{equation}
The companion \texttt{temporal\_transfer.tex} defines the positive
normalized transfer operator
\[
 F_\epsilon=e^{-\epsilon V/2}K_\epsilon e^{-\epsilon V/2}.
\]
The exact temporal link kernel has
spin-$j$ multiplier $I_{2j+1}(2b_t)/I_1(2b_t)$, temporal vertex
integration gives the Gauss projector $P_G$, and the raw transfer is
\begin{equation}\label{eq:rawrelation}
 T_\epsilon^{\rm raw}=c_\epsilon F_\epsilon P_G,
 \qquad c_\epsilon=[e^{-2b_t}Z(b_t)]^{|\mathsf E|},\qquad
 Z(b)=I_1(2b)/b.
\end{equation}
That companion proves, on the actual dense invariant core and then
strongly on the full Hilbert space,
$F_{T/m}^{\,m}\to e^{-TH}$ for fixed $T>0$. This is a time limit at
fixed spatial graph, with every coefficient in
\eqref{eq:physicalcoefficients} retained.

For $T>0$ and integer $m\geq1$, put $\epsilon=T/m$ and
\begin{equation}\label{eq:slabdensities}
 \phi_{T,m}=F_{T/m}^{\,m}1,\qquad
 \rho_{T,m}(U)=\frac{\phi_{T,m}(U)^2}{\|\phi_{T,m}\|_\lambda^2},\qquad
 \rho_{R;T,m}(r)=\int\rho_{T,m}(s,r)d\lambda_S(s).
\end{equation}
All these functions are positive, and $1$ is gauge invariant, so the
Gauss projector is retained automatically. Kernel composition and
Fubini identify \eqref{eq:slabdensities} with the central-slice density
of a two-sided finite Euclidean Wilson slab with slices
$-m,-m+1,\ldots,m$, fixed central slice $U$, and constant outer
boundary states. Each temporal plaquette has weight $b_t$, every
interior spatial plaquette has weight $b_s$, and spatial plaquettes
on the two outer boundary slices have half weight. The central
magnetic factor is full, because the two half factors multiply.
The two raw factors $c_\epsilon^m$ multiply to $c_\epsilon^{2m}$ in
both numerator and normalization and cancel exactly. This proves a
specific Euclidean-integral representation, including both temporal
sides and their boundary weights.

Assume now that $\mathsf S$ is the selected spatial-link set with no
two selected edges belonging to one spatial plaquette, and that each
plaquette uses any one physical edge at most once. Apply the selection
only at the central time slice. A temporal plaquette has only one
spatial edge at that slice, so no spacetime plaquette contains two
selected central links either. Let $Y$ denote every remaining slab
variable except the retained central links $r$.
For each selected central edge $e$, cyclically rotate and, when
necessary, invert a plaquette inside its real trace to write all its
incident contributions as $\Rea\tr(U_eV_{ep})$. Define
\begin{align}
 H_e(Y,r)&=\sum_{p\ni(e,0)}b_pV_{ep},&
 B_e&=\sum_{p\ni(e,0)}b_p,\nonumber\\
 r_e^2(Y,r)&=\tfrac12\tr(H_eH_e^\dagger)
 =\sum_{p\ni(e,0)}b_p^2
   +\sum_{p<q\ni(e,0)}b_pb_q\Rea\tr(V_{ep}V_{eq}^\dagger).
   \label{eq:allstaples}
\end{align}
The weights in this sum are the actual anisotropic weights of their
plaquettes. For a spatial interior edge there are four spatial staples
of weight $b_s$ and two temporal staples of weight $b_t$, so
$B_e=4b_s+2b_t$. At a spatial boundary the displayed incident sum,
rather than this interior count, is used.

The exact single-link integral is
\begin{equation}\label{eq:Zintegration}
 \int_{\SU(2)}e^{-2B_e+\Rea\tr(U_eH_e)}dU_e
   =e^{-2B_e}Z(r_e),\qquad
 Z(r)=\sum_{k=0}^\infty\frac{r^{2k}}{k!(k+1)!},\quad Z(0)=1.
\end{equation}
To prove it, write every $\SU(2)$ matrix as a unit real quaternion.
The real linear combination $H_e$ then obeys
$H_eH_e^\dagger=r_e^2I$ and $\det H_e=r_e^2$.
For $r_e>0$, $H_e/r_e\in\SU(2)$ and Haar translation reduces the
integral to
$(2/\pi)\int_{-1}^1e^{2r_ex}\sqrt{1-x^2}dx$.
Termwise integration of its uniformly convergent exponential series,
using
$\int_{-1}^1x^{2k}\sqrt{1-x^2}dx
=\pi(2k)!/[2\cdot4^kk!(k+1)!]$, gives
\eqref{eq:Zintegration}. The even moment formula follows by integration
by parts from the semicircle area at $k=0$. At $r_e=0$ the quaternion
is zero and the integral is exactly one before its constant factor.

No incident plaquette is shared by selected links. Thus the exact
central retained density in \eqref{eq:slabdensities} is
\begin{equation}\label{eq:integratedslab}
 \rho_{R;T,m}(r)=
 \frac{\displaystyle\int
    e^{-S_{\rm rest}(Y,r)}
    \prod_{e\in\mathsf S}e^{-2B_e}Z(r_e(Y,r))\,dY}
      {\displaystyle\int_{\mathcal Q_R}\int
    e^{-S_{\rm rest}(Y,r')}
    \prod_{e\in\mathsf S}e^{-2B_e}Z(r_e(Y,r'))\,dY\,d\lambda_R(r')}.
\end{equation}
Here $S_{\rm rest}$ is precisely the slab action with those incident
plaquettes removed; it includes every other plaquette and the stated
outer boundary weights. The integrals over $Y$ include all temporal
vertex links. Formula \eqref{eq:integratedslab} follows by applying
\eqref{eq:Zintegration} to the finite positive integrand and Fubini.
All cross-staple traces, the two temporal staples, and all induced
interactions remain in it. For a general split $\mathsf S$, the
unfactorized exact integral over selected links in
\eqref{eq:slabdensities} remains valid; only the product expression
\eqref{eq:integratedslab} uses the no-shared-plaquette property.

\begin{theorem}\label{thm:slablimit}
The exact true-vacuum marginal is the sequential $L^1$ limit
\begin{equation}\label{eq:sequentiallimit}
 \rho_R=\lim_{T\to\infty}\lim_{m\to\infty}\rho_{R;T,m},
 \qquad\epsilon=T/m,
\end{equation}
with the spatial graph and $a,g_{\rm YM}$ fixed. In particular the
nonlinear integration \eqref{eq:integratedslab}, performed with all
its interactions, has this precise relation to the true vacuum.
\end{theorem}
\begin{proof}
Strong transfer convergence gives
$\phi_{T,m}\to\phi_T:=e^{-TH}1$ in $L^2(\lambda)$ for each fixed
$T>0$. This nonzero positive vector has a nonzero norm. Normalization
is continuous at a nonzero vector, and
$\|v^2-w^2\|_1\leq(\|v\|_2+\|w\|_2)\|v-w\|_2$ for real
functions. Consequently
\[
 \rho_{T,m}\longrightarrow
 \rho_T:=\frac{(e^{-TH}1)^2}{\|e^{-TH}1\|^2}
 \quad\text{in }L^1(\lambda).
\]
Marginalization is an $L^1$ contraction by Fubini and the triangle
inequality, so the retained marginals converge in $L^1(\lambda_R)$.

Set $c_0=\langle\psi_0,1\rangle_\lambda>0$. Spectral decomposition,
the unique ground state, and the finite gap $\delta$ give
\[
 e^{TE_0}e^{-TH}1=c_0\psi_0+r_T,\qquad
 r_T\perp\psi_0,\qquad
 \|r_T\|\leq e^{-T\delta}\sqrt{1-c_0^2}.
\]
The norm of this vector is $\sqrt{c_0^2+\|r_T\|^2}$. Subtracting
$\psi_0$ after normalizing and using the triangle inequality gives
\[
 \left\|\frac{e^{-TH}1}{\|e^{-TH}1\|}-\psi_0\right\|_2
 \leq\frac{2\|r_T\|}{c_0}.
\]
Thus the same square-density inequality and marginal contraction yield
\begin{equation}\label{eq:vacuumerror}
 \|\rho_{R;T}-\rho_R\|_1
 \leq\|\rho_T-\rho\|_1
 \leq\frac{4\sqrt{1-c_0^2}}{c_0}e^{-T\delta}.
\end{equation}
This proves \eqref{eq:sequentiallimit}. It does not exchange the two
limits or infer a spatial continuum limit from them.
\end{proof}

The resulting excitation estimate can be obtained continuously from
these exact marginal integrations. Fix a nonconstant smooth invariant
$F(r)$ and put
\[
 \gamma_R(F)=\sum_{i\in R}\kappa_i|X_iF|^2,
 \qquad Q_R(F)=\frac{\mu_R(\gamma_R(F))}{\Var_{\mu_R}(F)}.
\]
For a probability density $\widetilde\rho_R$ let $\widetilde Q_R(F)$
be the same ratio with that density. Set
$\eta_1=\|\widetilde\rho_R-\rho_R\|_1$,
$M_F=\|F\|_\infty$, $G_F=\|\gamma_R(F)\|_\infty$, and
$v_F=\Var_{\mu_R}(F)>0$. Direct integration gives
\[
 |\widetilde\mu_R(\gamma_R)-\mu_R(\gamma_R)|\leq G_F\eta_1,
 \quad
 |\Var_{\widetilde\mu_R}(F)-v_F|\leq3M_F^2\eta_1.
\]
The second inequality uses the second-moment error at most
$M_F^2\eta_1$ and
$\bigl|\lvert\widetilde\mu_R(F)\rvert^2-\lvert\mu_R(F)\rvert^2\bigr|
\leq2M_F^2\eta_1$ for the mean term. If
$\eta_1\leq v_F/(6M_F^2)$, the new variance is at least $v_F/2$;
subtracting the two fractions then proves the explicit estimate
\begin{equation}\label{eq:quotienterror}
 |\widetilde Q_R(F)-Q_R(F)|
 \leq\frac{2G_F}{v_F}\eta_1
      +\frac{6G_FM_F^2}{v_F^2}\eta_1.
\end{equation}
In particular the sequential limits of the quotients constructed from
\eqref{eq:integratedslab} equal the genuine full-vacuum Rayleigh
quotient \eqref{eq:Rayleigh}, and hence its actual spectral first
moment. The controlled finite integrals, the true marginal, and the
quantum excitation estimate are related by the displayed maps and
limits. The single-time density proportional to
$\exp[-\sum_pb_p(2-\Rea\tr U_p)]$ is nowhere substituted for
$\psi_0^2$.

\section{Verification and literature provenance}

The calculation uses the full finite interacting Hamiltonian, not a
Gaussian or Abelian replacement. The map $B$, its conditional
covariance, the closed Schur form, the memory integral, and the
corrected full trial states all retain the actual $\rho=\psi_0^2$.
The scalar Schur/memory signs and corrected Rayleigh algebra are also
checked in \texttt{check\_spatial\_elimination.py}; that finite exact
algebra check does not replace the proved form-domain argument.
It passed 12 exact scalar/block assertions, together with exact
matrix-entry checks. An additional explicit rational-matrix quotient
checks the strict decrease; it is an algebra diagnostic and is not
presented as a lattice vacuum or a continuum approximation.

The general projection and Schur ideas are established methods, not
claimed as new results here. The locally retained source of
Dusson--Sigal--Stamm was inspected at Theorem 1.2 and the subsequent
effective-interaction equations; the retained projection here has
infinite rank, so its bounded finite-rank formulas are not invoked
without the form proof above. The earlier complete finite-vacuum and
time-transfer sources in this directory provide the retained kinetic,
potential, metric, and temporal-normalization dictionaries used here.
No infinite-volume or spatial-continuum spectral conclusion is made.

\begin{thebibliography}{9}
\bibitem{Feshbach}
H. Feshbach, \emph{Unified Theory of Nuclear Reactions},
Reviews of Modern Physics \textbf{36} (1964), 1076--1078,
\href{https://doi.org/10.1103/RevModPhys.36.1076}
{doi:10.1103/RevModPhys.36.1076}.

\bibitem{DSS}
G. Dusson, I. M. Sigal, and B. Stamm,
\emph{The Feshbach--Schur map and perturbation theory},
\href{https://arxiv.org/abs/2105.02058}{arXiv:2105.02058v1} (2021),
Theorem 1.2 and equations (1.10)--(1.16).

\bibitem{Mori}
H. Mori, \emph{Transport, Collective Motion, and Brownian Motion},
Progress of Theoretical Physics \textbf{33} (1965), 423--455,
\href{https://doi.org/10.1143/PTP.33.423}{doi:10.1143/PTP.33.423}.
\end{thebibliography}
\end{document}

```

## Complete source: euler_transfer/EXACT_VISCOUS_TRANSFER.md

```markdown
# Exact positive-viscosity transfer of the announced Euler construction

Date: 2026-09-08. This is a calculation for the velocity field constructed in *Blowup for the Euler Equations with Smooth Forcing*, the manuscript linked from the 2026-09-07 announcement. The downloaded source is identified in SOURCE_RECEIPTS.md. Its full 112-page proof and its Lean development have not been independently reverified here. The statements about that construction below are the stated results and formulas of the identified manuscript. Every new transfer identity and obstruction asserted here is proved below. No Navier-Stokes or Yang-Mills counterexample is asserted.

## 1. The actual objects, geometry, and equations

The source's Theorem 1.1 fixes any radius \(r_0>0\) and height \(z_0\), and produces \(T_*>0\), \(0<R<r_0/2\), smooth axisymmetric initial data with nonzero swirl and zero meridional velocity, and an axisymmetric force \(f_E\in C^\infty(\mathbb R^3\times[0,T_*])\). Its velocity and pressure solve
\[
 \partial_tu+(u\cdot\nabla)u+\nabla p_E=f_E,
 \qquad \operatorname{div}u=0
 \tag{1}
\]
on \(\mathbb R^3\times[0,T_*)\). In physical cylindrical coordinates \((r,\varphi,z)\), the construction has fixed support within
\[
 \mathcal T_R=\{(r,\varphi,z):(z-z_0)^2+(r-r_0)^2<R^2\}.
\]
Although the theorem initially states the support of circulation and azimuthal vorticity, Section 13.2 explicitly proves the support of the velocity itself in this torus. Thus the state has support in \(B_L(z_0e_z)\), where the exact convenient radius is \(L=r_0+R\). This follows by the triangle inequality from the distance to the circle of radius \(r_0\). No changing spatial domain is used below.

The source's physical volume coordinate, orientation, and elliptic coefficients are
\[
 y=(z,r^2/2),\quad J(a_1,a_2)=(-a_2,a_1),\quad
 A(y)=\begin{pmatrix}(2y_2)^{-1}&0\\0&1\end{pmatrix},
 \quad L_E=\partial_{y_2}^2+(2y_2)^{-1}\partial_{y_1}^2,
 \quad W=(2y_2)^{-2}.
\]
Here \(L_E\) is the source operator denoted \(L\); the subscript only avoids collision with the enclosing-ball radius. With \(v=J\nabla_y\Psi\),
\[
 u^z=-\Psi_{y_2},\qquad u^r=\Psi_{y_1}/r,\qquad
 u^\varphi=\Gamma/r,\qquad \xi=\omega^\varphi/r=L_E\Psi,
 \quad D_v=\partial_t+v\cdot\nabla_y.
\]
The exact Euler residuals and source compact recovery are
\[
 F_E^\Gamma=D_v\Gamma,\qquad
 E_E^\xi=D_v\xi-W\partial_{y_1}(\Gamma^2),
\]
\[
 f_E^\varphi=F_E^\Gamma/r,\qquad
 (f_E^z,f_E^r/r)=\mathcal R_y E_E^\xi,
 \quad\operatorname{curl}_y\mathcal R_yE_E^\xi=E_E^\xi.
 \tag{2}
\]
Here \(\operatorname{curl}_y(h_1,h_2)=\partial_{y_1}h_2-\partial_{y_2}h_1\). All radial denominators are bounded because the support stays in \(r_0-R\le r\le r_0+R\).

The source proves that \(\Gamma,u^r,u^z\) remain uniformly bounded, while \(\|\nabla\Gamma(t)\|_\infty\), \(\|\omega(t)\|_\infty\), and \(\int_0^{T_*}\|\omega(t)\|_\infty\,dt\) diverge. The full physical velocity is bounded because \(|u^\varphi|\le (r_0-R)^{-1}|\Gamma|\).

## 2. Exact viscous map, with arbitrary pressure and fixed positive viscosity

Fix any constant physical kinematic viscosity \(\nu_{\mathrm{vis}}>0\). The subscript distinguishes it from the source's unrelated cone margin also named \(\nu\). For the same velocity and pressure, define
\[
 f_{\mathrm{vis}}=f_E-\nu_{\mathrm{vis}}\Delta_xu.
 \tag{3}
\]
Subtraction of \(\nu_{\mathrm{vis}}\Delta_xu\) from both sides of (1) proves exactly
\[
 \partial_tu+(u\cdot\nabla)u+\nabla p_E
   =\nu_{\mathrm{vis}}\Delta_xu+f_{\mathrm{vis}}.
\]
Thus (3) gives a genuine morphism between forced equations on every compact preterminal interval, preserving the initial datum, velocity, divergence, viscosity value, and physical coordinates. It does not by itself preserve the closed-time smooth-force class.

Every other pressure \(p_E+q\) for this same velocity requires the force
\[
 \widetilde f_{\mathrm{vis}}=f_E-\nu_{\mathrm{vis}}\Delta_xu+\nabla q.
 \tag{4}
\]
This follows by subtracting the two momentum equations componentwise, so (4) is exhaustive for fixed \(u\). Curl eliminates the pressure exactly:
\[
 \operatorname{curl}(\widetilde f_{\mathrm{vis}}-f_E)
       =-\nu_{\mathrm{vis}}\Delta_x\omega.
 \tag{5}
\]

For completeness, on \(L^2(\mathbb R^3;\mathbb R^3)\) the solenoidal projection has Fourier multiplier
\[
 \widehat{\mathbb Ph}(k)=\left(I-\frac{kk^T}{|k|^2}\right)\widehat h(k)
 \quad(k\ne0).
\]
The value at \(k=0\) is immaterial to \(L^2\). Since \(k\cdot\widehat u=0\), multiplication by \(-|k|^2\) proves \(\mathbb P\Delta u=\Delta u\). Since the multiplier annihilates \(k\), it annihilates gradients whenever the projected expressions are defined. Consequently
\[
 \mathbb Pf_{\mathrm{vis}}=\mathbb Pf_E-\nu_{\mathrm{vis}}\Delta u.
 \tag{6}
\]
Pressure absorption cannot remove this solenoidal viscous term. Equation (5) remains meaningful locally even without an \(L^2\) hypothesis on \(\nabla q\).

The energy identity independently checks the sign in (3). Compact support permits integration by parts:
\[
 \int u\cdot f_{\mathrm{vis}}\,dx
   =\int u\cdot f_E\,dx+\nu_{\mathrm{vis}}\int|\nabla u|^2\,dx.
\]
Hence the positive-viscosity energy identity reads
\(\frac12\partial_t\|u\|_2^2+\nu_{\mathrm{vis}}\|\nabla u\|_2^2
=\langle u,f_{\mathrm{vis}}\rangle\), exactly as required.

## 3. Exact viscous reduced operators in the source's coordinates

For an axisymmetric scalar, the Cartesian scalar Laplacian is
\(\Delta_0=\partial_z^2+\partial_r^2+r^{-1}\partial_r\).
The vector Laplacian of the azimuthal component is \((\Delta_0-r^{-2})u^\varphi\). Directly differentiating \(u^\varphi=\Gamma/r\) gives
\[
 r(\Delta_0-r^{-2})(\Gamma/r)
   =\partial_z^2\Gamma+\partial_r^2\Gamma-r^{-1}\partial_r\Gamma
   =:D_\Gamma\Gamma.
\]
Likewise
\[
 r^{-1}(\Delta_0-r^{-2})(r\xi)
   =\partial_z^2\xi+\partial_r^2\xi+3r^{-1}\partial_r\xi
   =:D_\xi\xi.
\]
The factors follow from
\(\partial_r^2(\Gamma/r)=\Gamma_{rr}/r-2\Gamma_r/r^2+2\Gamma/r^3\)
and \(\partial_r^2(r\xi)=r\xi_{rr}+2\xi_r\).
Using \(\partial_r=r\partial_{y_2}\) then gives the exact operators
\[
 D_\Gamma=\partial_{y_1}^2+2y_2\partial_{y_2}^2,
 \qquad
 D_\xi=\partial_{y_1}^2+2y_2\partial_{y_2}^2+4\partial_{y_2}.
 \tag{7}
\]
Therefore the correct source residuals for positive viscosity are
\[
 F_{\mathrm{vis}}^\Gamma=F_E^\Gamma-\nu_{\mathrm{vis}}D_\Gamma\Gamma,
 \qquad
 E_{\mathrm{vis}}^\xi=E_E^\xi-\nu_{\mathrm{vis}}D_\xi\xi.
 \tag{8}
\]
The second follows equivalently by taking curl of (3). In fact
\(r^{-1}(\partial_z(\Delta u)^r-\partial_r(\Delta u)^z)
=r^{-1}(\Delta\omega)^\varphi=D_\xi\xi\).

The compatibility of the compact source inverse survives:
\[
 D_\xi\xi=\partial_{y_1}(\partial_{y_1}\xi)
    +\partial_{y_2}(2y_2\partial_{y_2}\xi+2\xi),
 \qquad \int_{\mathbb R^2}D_\xi\xi\,dy=0.
\]
Thus applying the same \(\mathcal R_y\) to (8) gives a legitimate compact force. Its azimuthal component equals that of (3), and its meridional curl agrees with (3); their difference has zero full curl and zero azimuthal component. The difference is smooth through the axis because both forces vanish nearby. On simply connected \(\mathbb R^3\) it is an exact gradient. One explicit potential for a smooth curl-free difference \(h\) is
\(q(x,t)=\int_0^1h(sx,t)\cdot x\,ds\): differentiating and using \(\partial_i h_j=\partial_j h_i\) gives \(\partial_iq=h_i\). This proves the precise equivalence between compact recovery and the direct force map, including pressure.

## 4. Terminal obstruction for this actual field, independent of pressure

Let \(G(x)=(4\pi|x|)^{-1}\), so \(-\Delta G=\delta_0\). For a smooth compactly supported vector field \(h\),
\[
 h=-G*\Delta h.
 \tag{9}
\]
One proof is integration by parts in the distribution identity \(-\Delta G=\delta_0\), component by component. Compact support removes all boundary terms; the locally integrable kernel makes the convolution well defined.

The integral of \(G(x-y)\) over a ball of radius \(L\) centered at \(c\), with \(\rho=|x-c|\), is exactly
\[
 \int_{B_L(c)}G(x-y)\,dy=
 \begin{cases}(3L^2-\rho^2)/6,&0\le\rho\le L,\\
 L^3/(3\rho),&\rho\ge L.
 \end{cases}
 \tag{10}
\]
To verify (10), use spherical shells about \(c\). The angular integral at shell radius \(a\) is
\(\int_{S^2}|x-c-a\theta|^{-1}\,d\theta=4\pi/\max(\rho,a)\).
For \(\rho,a>0\), this follows by integrating
\(2\pi\int_{-1}^1(\rho^2+a^2-2\rho a s)^{-1/2}\,ds\);
zero radii follow by continuity. Integration of \(a^2/\max(\rho,a)\) from zero to \(L\) yields (10).
Its maximum is \(L^2/2\). Taking Euclidean vector norms in (9) therefore gives
\[
 \|h\|_\infty\le\frac{L^2}{2}\|\Delta h\|_\infty
 \quad\text{when }\operatorname{supp}h\subset B_L(c).
 \tag{11}
\]
Apply this at each preterminal time to the source vorticity. Its derivatives have the same support. Equations (5) and (11) imply
\[
 \|\operatorname{curl}\widetilde f_{\mathrm{vis}}(t)\|_{L^\infty(B_L)}
 \ge \frac{2\nu_{\mathrm{vis}}}{L^2}\|\omega(t)\|_\infty
       -\|\operatorname{curl}f_E(t)\|_{L^\infty(B_L)}
 \longrightarrow+\infty.
 \tag{12}
\]
The last term is bounded on the fixed compact cylinder because the actual Euler force is smooth through \(T_*\). Hence no single-valued smooth pressure correction can make the same actual velocity solve positive-viscosity Navier-Stokes with force smooth through \(T_*\). Equation (12) even rules out a uniform \(C^1\) force bound there.

The actual axisymmetric construction gives the stronger failure of the force's \(C^0\) norm. Define its swirl field
\(U_{\mathrm{sw}}=(\Gamma/r)e_\varphi\). It is a smooth Cartesian field supported in the same ball, because it vanishes near the axis. Its curl consists precisely of
\[
 \omega^r=-r^{-1}\partial_z\Gamma=-r^{-1}\partial_{y_1}\Gamma,
 \qquad \omega^z=r^{-1}\partial_r\Gamma=\partial_{y_2}\Gamma.
 \tag{13}
\]
These are exactly the components whose divergence is proved in source (14.5), so
\(\|\operatorname{curl}U_{\mathrm{sw}}(t)\|_\infty\to\infty\).
Differentiating (9), and using \(|a\times b|\le|a||b|\), gives
\[
 \|\operatorname{curl}h\|_\infty
       \le L\|\Delta h\|_\infty.
 \tag{14}
\]
Here \(\int_{B_L(c)}|\nabla G(x-y)|\,dy\le L\). To prove the constant, use the layer-cake representation of the decreasing radial kernel \((4\pi|z|^2)^{-1}\). At every radius, the intersection of \(B_L(c)\) with a ball centered at \(x\) has volume at most the smaller of the two ball volumes. The concentric case attains that upper bound at every layer. The centered integral is \(\int_0^Ldr=L\).

For arbitrary single-valued \(q\), its angular derivative has zero angular average:
\[
 \frac1{2\pi}\int_0^{2\pi}e_\varphi\cdot\nabla q(r,\varphi,z,t)\,d\varphi
 =\frac1{2\pi r}[q(r,2\pi,z,t)-q(r,0,z,t)]=0.
\]
The azimuthal component of \(\Delta u\) is exactly that of \(\Delta U_{\mathrm{sw}}\), which is axisymmetric. Taking the angular average of (4), then a supremum over the fixed torus, yields
\[
 \|\widetilde f_{\mathrm{vis}}(t)\|_{L^\infty(B_L)}
 \ge \nu_{\mathrm{vis}}\|\Delta U_{\mathrm{sw}}(t)\|_\infty
       -\|f_E^\varphi(t)\|_\infty
 \ge\frac{\nu_{\mathrm{vis}}}{L}\|\operatorname{curl}U_{\mathrm{sw}}(t)\|_\infty
       -\|f_E^\varphi(t)\|_\infty
 \longrightarrow+\infty.
 \tag{15}
\]
No axisymmetry of the new pressure or new force was assumed in this angular-average argument. This is a result about the proposed transport of the particular field. It is not a nonexistence result for different Navier-Stokes profiles or a dismissal of the cascade mechanism.

## 5. The actual scale schedule and the exact diffusion seen by its phase

Source (12.1)-(12.4), visually checked on pages 95-96, chooses
\[
 \beta=1/8,\quad\bar\beta=h=7/8,\quad a=4,\quad p=8,\quad q=10,
 \quad r=40,\quad d=16,\quad e=8,
\]
\[
 c_Q\ge2^{18},\quad q_0\ge2^{20},\quad Q_i=q_0+i,
 \quad u=q/c_Q,\quad v=q/(q_0+1),\quad h_*=h-dv.
\]
The letter \(r=40\) in this list is the source's exponent, not the physical radial coordinate. The strict requirements are
\[
 dv<1/16,\quad8u+100v<1/16,\quad9/c_Q+51/(q_0+1)<1.
\]
With the source scalar \(y=\log N_1\), a fixed positive initial frequency \(N_0\), and fixed \(s_0,C_\ell\),
\[
 N_1=e^y,\quad N_i=N_{i-1}^{Q_i}\ (i\ge2),\qquad
 \Pi_1=N_0^8y^{40},\quad\Pi_i=N_{i-1}^8(\log N_i)^{40}\ (i\ge2),
\]
\[
 \ell_1=s_0/(C_\ell N_0y^2),\quad\ell_i=N_{i-1}^{-4}\ (i\ge2),
 \quad\delta_i=\Pi_i^{16}N_i^{-7/8}.
\]
Here \(\delta_i\) is a correction parameter, not an insertion duration. The depth and seed are
\[
 k_i=\max\{k\in\mathbb N_0:k\le Q_i/c_Q,\ \mathcal K_{\rm ho}(k)\le\log N_i\},
 \quad J_i=2k_i+8,
\]
\[
 T_i^{\rm seed}=-N_i^{-k_i-8},\qquad
 \Lambda_i=(k_i+8-7/8)\log N_i.
 \tag{16}
\]
The source-defined function \(\mathcal K_{\rm ho}\) is fixed before \(y\), and \(k_i\to\infty\). No numerical value for the source's threshold or that function was independently computed here.

The clocks obey \(c_\sigma N_i^{1/8}\le\sigma_i^2\le C_\sigma N_i^{1/8}\), with \(\sigma_0=\sqrt{A_0}\). For \(i\ge2\),
\[
 s_i=\Lambda_i\sigma_{i-2}/\sigma_{i-1},\qquad
 \Gamma_i^{\rm gr}=\sigma_{i-1}\sin s_i,
\]
\[
 c_T\Lambda_i/\Gamma_i^{\rm gr}\le|I_i^{\rm gr}|
 \le|W_i|\le C'_T\Lambda_i/\Gamma_i^{\rm gr}
 \le C''_T/\sigma_{i-2}.
 \tag{17}
\]
Since \(\sin s\le s\), also \(|I_i^{\rm gr}|\ge c_T/\sigma_{i-2}\). The insertion times increase to finite \(T_*\). At the growth hit \(t_i^a\), the exact central amplitude condition is
\(-T_i(0,t_i^a)=N_i^{-7/8}\); hence its principal circulation gradient has magnitude
\(N_i^{1/8}|\zeta_i(0,t_i^a)|\). The complete force increments satisfy, with the same chosen sequence,
\[
 \|f_i\|_{C^k_{x,t}([0,T_*))}\le C_kN_i^{-1/2}\quad(k\le k_i),
 \qquad
 \sup_{t<T_*}(\|\gamma_i\|_\infty+\|J\nabla\psi_i\|_\infty)
 \le CN_i^{-1/2}.
 \tag{18}
\]
Source (14.4)-(14.5) gives a fixed \(c_*>0\) and fixed off-axis geometric factor with meridional vorticity at least \(c_*N_n^{1/8}\) for every \(t\ge\tau_{n+1}\). Inserting that lower bound in (15) gives a force lower bound of the same \(N_n^{1/8}\) order, after multiplying by the retained \(\nu_{\mathrm{vis}}/L\), for the transported field. This bound concerns the complete field and cannot be invalidated by cancellation among its correction levels.

For the phase calculation, keep the source's actual material flow \(X_m(a,t)\), inverse \(A_m(y,t)\), matrix \(H_m=(D_aX_m)^{-1}\), covector \(\zeta_m=H_m^Tp_m\), and phase \(s=N_mp_m\cdot A_m\), with \(|p_m|=1\). The principal circulation and streamfunction are
\[
 \gamma_{m,0}=(w_mT_mF(s)g_m(a))^\flat,\quad
 \psi_{m,0}=(w_mB_mP(s)g_m(a))^\flat,
 \quad\Omega_m=N_m^2\kappa_mB_m,
\]
\[
 \kappa_m=\zeta_m^TA(X_m)\zeta_m,\quad
 \widehat\Omega_m=\sigma_{m-1}\Omega_m/N_m,
 \quad\partial_t\binom{T_m}{\widehat\Omega_m}
 =\mathcal B_m\binom{T_m}{\widehat\Omega_m},
\]
\[
 \mathcal B_m=\begin{pmatrix}0&-d_m/(\sigma_{m-1}\kappa_m)\\
 \sigma_{m-1}c_m\zeta_{m,1}&0\end{pmatrix},\quad
 d_m=(J\zeta_m)\cdot(\nabla\Gamma_{<m})\circ X_m,\quad
 c_m=2(W\Gamma_{<m})\circ X_m.
 \tag{19}
\]
The source profile \(F\) is smooth, odd, \(2\pi\)-periodic, and exactly \(s\) near zero; \(P'=F\). It must not be replaced by a sinusoid or by a single Fourier mode.

Here is the exact chain rule including every lower derivative of the material map. Set \(B_{\rm ph}=\operatorname{diag}(1,2y_2)\), \(\phi=p_m\cdot A_m\), and use \(H_{kj}=\partial_{y_j}(A_m)_k\). For every smooth profile \(Q(s,a,t)\),
\[
\begin{split}
 D_\Gamma Q^\flat={}&\big[N_m^2\chi_m Q_{ss}
  +N_m(D_\Gamma\phi)Q_s
  +2N_m\sum_{j,k}(B_{\rm ph})_{jj}\zeta_{m,j}H_{kj}Q_{sa_k}\\
 &+\sum_{j,k,l}(B_{\rm ph})_{jj}H_{kj}H_{lj}Q_{a_ka_l}
  +\sum_k(D_\Gamma(A_m)_k)Q_{a_k}\big]^\flat,
\end{split}
 \tag{20}
\]
where \(\chi_m=\zeta_{m,1}^2+2y_2\zeta_{m,2}^2=2y_2\kappa_m\). All coefficients are evaluated at \(y=X_m(a,t)\). To prove (20), first apply
\(\partial_{y_j}Q^\flat=(N_m\zeta_{m,j}Q_s+\sum_kH_{kj}Q_{a_k})^\flat\), then differentiate once more and sum the diagonal coefficients of (7). The terms differentiating \(\zeta\) give \(D_\Gamma\phi\); those differentiating \(H\) give \(D_\Gamma(A_m)_k\). Thus no frozen-flow approximation was made. The exact expression for \(D_\xi Q^\flat\) adds
\(4[N_m\zeta_{m,2}Q_s+\sum_kH_{k2}Q_{a_k}]^\flat\).

In particular the circulation's highest phase residual from viscosity is
\(-\nu_{\mathrm{vis}}N_m^2\chi_mw_mT_mg_mF''\).
Although \(F''=0\) on the central linear interval, it is not identically zero: a periodic function with zero second derivative everywhere would be affine and periodic, hence constant, contradicting \(F'(0)=1\). The high derivative term therefore survives away from that interval. At the hit its coefficient has size proportional to \(\nu_{\mathrm{vis}}N_m^{9/8}\). This last statement is about a coefficient of the exact profile expression, not an unproved lower bound after summing all fields; (15) supplies the latter.

The physical radius and magnification do not eliminate viscosity. The source's physical radius change is \(x=z_0e_z+r_0\widehat x\), \(u=r_0\widehat u\), with time unchanged. Since \(\Delta_xu=r_0^{-1}\Delta_{\widehat x}\widehat u\), the coefficient in the unit-radius momentum equation is \(\nu_{\mathrm{vis}}/r_0^2\). The source next uses \(y=y_*+\varepsilon_{\rm geom}x'\), with \(y_*=(0,1/2)\) at unit radius. Equations (7) become
\[
 D_\Gamma=\varepsilon_{\rm geom}^{-2}
   (\partial_{x'_1}^2+c_{\rm geom}\partial_{x'_2}^2),\qquad
 D_\xi=\varepsilon_{\rm geom}^{-2}
   (\partial_{x'_1}^2+c_{\rm geom}\partial_{x'_2}^2
                   +4\varepsilon_{\rm geom}\partial_{x'_2}),
\]
where \(c_{\rm geom}=1+2\varepsilon_{\rm geom}x'_2\). Thus the schedule's magnified phase sees the fixed positive coefficient
\(\nu_{\rm eff}=\nu_{\mathrm{vis}}/(r_0^2\varepsilon_{\rm geom}^2)\),
and principal symbol \(\chi'_m=\zeta_{m,1}^2+c_{\rm geom}\zeta_{m,2}^2\). All factors are retained; reducing the fixed geometric scale increases this coefficient.

## 6. Explicit repairs and what they do to the amplification

The exact highest-phase repair of (19) is a heat equation in the full periodic phase, not a scalar adjustment of \(T_m\). With the same supplied material coefficients, define the two-component phase profile \(\mathcal U\) by
\[
 \partial_t\mathcal U=\mathcal B_m(a,t)\mathcal U
       +\nu_{\rm eff}N_m^2\chi'_m(a,t)\partial_s^2\mathcal U.
 \tag{21}
\]
Its solution for smooth periodic initial phase data is explicitly
\[
 \mathcal U(s,a,t)=\mathcal P_m(a;t,\tau_m)
  \sum_{j\in\mathbb Z}e^{ijs-j^2D_m(a,t)}\mathcal U_j(a,\tau_m),
 \quad D_m=\nu_{\rm eff}N_m^2\int_{\tau_m}^t\chi'_m(a,\theta)\,d\theta.
 \tag{22}
\]
Indeed, \(\partial_t\mathcal P_m=\mathcal B_m\mathcal P_m\), the matrix does not depend on \(s\), and differentiating each exponential supplies the second term in (21). Smooth periodic data have rapidly decaying Fourier coefficients, which justify termwise differentiation on each compact preterminal interval. For the actual source principal datum these coefficients equal a fixed vector times the Fourier coefficients of the actual \(F\). Oddness gives zero mean. Every nonzero phase mode is damped.

Equations (21)-(22) solve the highest-phase part exactly. They do not purport to solve the full Navier-Stokes correction hierarchy: its exact additional label derivatives, curvature terms, and nonlinear interactions are present in (20) and (8). In particular changing the principal flow alters that hierarchy and cannot inherit its Euler estimates without a new calculation.

There is already a quantitative result on the unchanged Euler history. The source's central covector and ellipticity bounds give a fixed \(\chi'_->0\). On the actual \(m\)-th growth interval, (17) proves for \(m\ge3\)
\[
 D_m(0,t_m^a)\ge\nu_{\rm eff}\chi'_-c_T N_m^2/\sigma_{m-2}
 \ge\frac{\nu_{\rm eff}\chi'_-c_T}{\sqrt{C_\sigma}}
       N_m^{\,2-1/(16Q_mQ_{m-1})}.
 \tag{23}
\]
The identity used is
\(N_{m-2}=N_m^{1/(Q_mQ_{m-1})}\), followed by
\(\sigma_{m-2}\le\sqrt{C_\sigma}N_{m-2}^{1/16}\).
The source gain is \(\Lambda_m=(k_m+57/8)\log N_m\), where
\(k_m\le Q_m/c_Q\). Since \(Q_m\le\log N_{m-1}\le\log N_m\),
\(\Lambda_m\le((\log N_m)/c_Q+57/8)\log N_m\).
On the other hand the exponent in (23) exceeds one, so \(D_m/\Lambda_m\to\infty\), by the elementary fact that \(e^x/x^2\to\infty\). Consequently even the smallest nonzero Fourier frequency in (22) acquires damping that exceeds the actual logarithmic gain by an unbounded factor. The unchanged seed and time schedule cannot retain its Euler phase amplification under this explicit repair. Increasing the seed to cancel that damping would multiply a nonzero Fourier coefficient by \(e^{j^2D_m}\), overwhelming the polynomially small seed (16); it is not a small perturbation of the stated data. This proves what happens to this concrete repair, without claiming that no redesigned cascade can work.

A second exact map changes the full velocity and retains the positive viscosity and the initial datum. Let \(S_t=e^{\nu_{\mathrm{vis}}t\Delta}\) and set
\[
 U=S_tu,\qquad P=S_tp_E,\qquad
 F=S_tf_E+(U\cdot\nabla)U-S_t((u\cdot\nabla)u).
 \tag{24}
\]
At \(t=0\), \(U=u_0\). Differentiation of the heat convolution and (1) gives
\(\partial_tU=\nu_{\mathrm{vis}}\Delta U+S_t\partial_tu\).
Spatial differentiation commutes with convolution. Substitution proves exactly
\[
 \partial_tU+(U\cdot\nabla)U+\nabla P
       =\nu_{\mathrm{vis}}\Delta U+F,\quad\operatorname{div}U=0
\]
at all preterminal times. All convolutions are legitimate there; a spatial constant can be subtracted from the source pressure outside its compact force region if desired.

This correction removes the sought velocity singularity. The heat kernel
\(K_t(x)=(4\pi\nu_{\mathrm{vis}}t)^{-3/2}e^{-|x|^2/(4\nu_{\mathrm{vis}}t)}\)
satisfies
\(\int|\nabla K_t|\,dx=2/\sqrt{\pi\nu_{\mathrm{vis}}t}\).
To check the constant, \(|\nabla K_t|=|x|K_t/(2\nu_{\mathrm{vis}}t)\); direct radial integration gives
\(\int|x|K_t\,dx=4\sqrt{\nu_{\mathrm{vis}}t/\pi}\).
Hence
\[
 \|\operatorname{curl}U(t)\|_\infty
 \le\frac{2}{\sqrt{\pi\nu_{\mathrm{vis}}t}}\|u(t)\|_\infty.
 \tag{25}
\]
The source's uniform velocity bound makes this uniformly finite for \(t\ge T_*/2\). The output force in (24) is established as smooth preterminally; all of its terminal time derivatives have not been proved bounded here. Neither (24) nor (22) is claimed as an admissible singular Navier-Stokes example. They are explicit corrections with their proved effects.

The completed calculation therefore locates the exact transferred forcing, the exact pressure freedom, the radial diffusion operators, the unchanged cascade's diffusion exponent, and two concrete correction maps. The direct transfer of the actual announced field loses even bounded forcing at terminal time; the repaired principal evolution suppresses its stated amplification; the full heat map suppresses its vorticity singularity. Constructing a different positive-viscosity singular profile with smooth terminal force remains unachieved by these calculations.

```

## Complete source: check_retained_cusp_bridge.py

```python
"""Exact algebra checks; analytic arguments are in the companion proof text."""
from pathlib import Path
import json
from fractions import Fraction
from itertools import product
import sympy as s

checks = []

def zero(name, value):
    entries = list(value) if isinstance(value, s.MatrixBase) else [value]
    assert all(s.cancel(v) == 0 for v in entries), name
    checks.append(name)

L, m, q, M = s.symbols('L m q M', nonzero=True, real=True)
aa, ab, ac, ad = s.symbols('aa ab ac ad', real=True)
A = s.Matrix([[aa, ab], [ac, ad]])
B = s.Matrix([[6*m, L], [-q, m]])
D = L*q + 6*m*m
Bi = s.Matrix([[m, -L], [q, 6*m]])/D
zero('retained B inverse', B*Bi-s.eye(2))
Q = A.row_join(M*s.eye(2)).col_join(B.row_join(s.zeros(2)))
Qi = s.zeros(2).row_join(Bi).col_join((s.eye(2)/M).row_join(-A*Bi/M))
zero('retained period right inverse', Q*Qi-s.eye(4))
zero('retained period left inverse', Qi*Q-s.eye(4))
zero('permuted orientation determinant', Q.det()-M**2*D)
K = Bi*Bi.T
Ke = s.Matrix([[m*m+L*L, m*q-6*m*L], [m*q-6*m*L, q*q+36*m*m]])/D**2
zero('all entries of upper metric block', K-Ke)
zero('retained two-form minor', K.det()-D**-2)
Gi = K.row_join(-K*A.T/M).col_join((-A*K/M).row_join((s.eye(2)+A*K*A.T)/M**2))
zero('full mixed metric entries', Gi-Qi*Qi.T)
zero('full inverse metric identity', (Q.T*Q)*Gi-s.eye(4))

# Quaternion staple formula with arbitrary real, non-unit coefficients.
h0, h1, h2, h3 = s.symbols('h0 h1 h2 h3', real=True)
sigma = [s.Matrix([[0,1],[1,0]]), s.Matrix([[0,-s.I],[s.I,0]]), s.diag(1,-1)]
H = h0*s.eye(2)+s.I*(h1*sigma[0]+h2*sigma[1]+h3*sigma[2])
r2 = h0*h0+h1*h1+h2*h2+h3*h3
zero('full quaternion staple norm', H*H.conjugate().T-r2*s.eye(2))
zero('full quaternion staple determinant', H.det()-r2)

# Verify the exact beta-integral coefficient recurrence at many orders.
for k in range(16):
    beta_val = s.gamma(s.Rational(1,2)+k)*s.gamma(s.Rational(3,2))/s.gamma(k+2)
    target = s.pi*s.factorial(2*k)/(2*4**k*s.factorial(k)*s.factorial(k+1))
    zero(f'Haar moment coefficient {k}', s.expand_func(beta_val)-target)

r = s.symbols('r')
Z = sum(r**(2*k)/(s.factorial(k)*s.factorial(k+1)) for k in range(18))
ode = s.diff(Z,r,2)+3*s.diff(Z,r)/r-4*Z
zero('Bessel radial ODE through degree 32', s.series(ode,r,0,33).removeO())
eta = s.series(s.diff(Z,r)/(2*Z),r,0,9).removeO()
zero('exact mean small-r coefficients', eta-(r/2-r**3/12+r**5/48-r**7/180))
zero('Haar second moment at zero', s.limit(eta/(2*r),r,0)-s.Rational(1,4))
zero('second-moment sum retains unit quaternion constraint', (1-3*eta/(2*r))+3*eta/(2*r)-1)

for N in range(2,14):
    for n1 in range(N):
        for n2 in range(N):
            h = -Fraction(n1*n2,N*N)
            h1 = -Fraction(((n1+1)%N)*n2,N*N)
            h2 = -Fraction(n1*((n2+1)%N),N*N)
            w1 = -Fraction(n2,N) if n1 == N-1 else Fraction(0)
            w2 = Fraction(n1,N*N)
            assert -h+w1+h1 == -Fraction(n2,N*N)
            assert -h+w2+h2 == (Fraction(n1,N) if n2 == N-1 else Fraction(0))
    checks.append(f'magnetic vertex gauge, every vertex and wrap, N={N}')

theta,b = s.symbols('theta b', real=True)
expH = s.diag(s.exp(s.I*theta),s.exp(-s.I*theta))
zero('retained six-staple background coefficient',
     s.expand_complex(b*(4*s.eye(2)+expH+expH.conjugate().T)-b*(4+2*s.cos(theta))*s.eye(2)))
zero('local full-star cost difference', 2*b*(2-2*s.cos(theta))-4*b*(1-s.cos(theta)))
zero('exact local r interval width', 6*b-b*(4+2*s.cos(theta))-2*b*(1-s.cos(theta)))

for N in (2,4,6,8):
    selected = {(n1,n2,n3,n4) for n1 in range(N)
                for n2,n3,n4 in product(range(1,N),repeat=3)
                if (n2+n3+n4)%2 == 1}
    assert len(selected) == N*((N-1)**3+1)//2
    degrees = {e:0 for e in selected}
    magnetic_count = magnetic_selected = 0
    for n in product(range(N+1),repeat=4):
        for i in range(4):
            for j in range(i+1,4):
                if n[i] == N or n[j] == N:
                    continue
                touches = []
                if i == 0:
                    upper = tuple(n[k]+int(k==j) for k in range(4))
                    touches = [e for e in (n,upper) if e in selected]
                assert len(touches) <= 1
                for e in touches:
                    degrees[e] += 1
                if (i,j) == (0,1):
                    magnetic_count += 1
                    magnetic_selected += len(touches)
    assert all(v==6 for v in degrees.values())
    assert magnetic_count == N*N*(N+1)**2
    assert magnetic_selected == 2*len(selected)
    checks.append(f'full 4D patch incidence and extensive integration counts, N={N}')

j = s.symbols('j', positive=True)
Nj = 2*j*j
mj = Nj*((Nj-1)**3+1)/2
pj = Nj**2*(Nj+1)**2
zero('bulk selected-star coverage limit', s.limit(2*mj/pj,j,s.oo)-1)
thetaj = 2*s.pi/(10000*j**6)
zero('retained leading extensive-action coefficient',
     s.limit(j**4*b*pj*thetaj**2,j,s.oo)-64*s.pi*s.pi*b/10**8)

receipt = {'status':'PASS','checks':checks,'check_count':len(checks),
           'scope':'Exact finite algebra and series coefficients only; not a quantum continuum calculation.'}
out = Path(__file__).with_name('RETAINED_CUSP_BRIDGE_CHECKS.json')
out.write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'PASS','check_count':len(checks),'receipt':str(out)}))

```

## Complete source: wilson_variation/check_wilson_exact.py

```python
"""Small exact algebra checks for wilson_finite_lattice.tex.

This verifies finite matrix identities and one product-rule identity. It does
not compute a Yang--Mills vacuum, any continuum limit, or any spectral gap.
Run: python check_wilson_exact.py
"""

import sympy as s


def su_basis(n):
    out = []
    for i in range(n):
        for j in range(i + 1, n):
            a, b = s.zeros(n), s.zeros(n)
            a[i, j], a[j, i] = s.Rational(1, 2), -s.Rational(1, 2)
            b[i, j] = b[j, i] = s.I / 2
            out.extend((a, b))
    for k in range(1, n):
        d = [1] * k + [-k] + [0] * (n - k - 1)
        out.append(s.I * s.diag(*d) / s.sqrt(2 * k * (k + 1)))
    return out


def zero(x):
    assert s.simplify(x) == 0, x


def matrix_zero(a):
    for x in a:
        zero(x)


checks = 0
for n in (2, 3, 4):
    basis = su_basis(n)
    assert len(basis) == n * n - 1
    for a, ta in enumerate(basis):
        matrix_zero(ta.H + ta)
        zero(s.trace(ta))
        for b, tb in enumerate(basis):
            zero(-2 * s.trace(ta * tb) - int(a == b))
            zero(-s.trace((2 * ta) * (2 * tb)) / 2 - int(a == b))
            checks += 2
    for i in range(n):
        for j in range(n):
            for k in range(n):
                for l in range(n):
                    lhs = sum(ta[i, j] * ta[k, l] for ta in basis)
                    rhs = -(s.Integer(i == l) * int(j == k)
                            - s.Rational(1, n) * int(i == j) * int(k == l)) / 2
                    zero(lhs - rhs)
                    checks += 1
    casimir = sum((ta * ta for ta in basis), s.zeros(n))
    matrix_zero(casimir + s.Rational(n * n - 1, 2 * n) * s.eye(n))
    checks += n * n

n = 3
basis = su_basis(n)
u = s.Matrix([[s.Rational(3, 5), s.Rational(4, 5), 0],
              [-s.Rational(4, 5), s.Rational(3, 5), 0], [0, 0, 1]])
r = s.Matrix([[1, 0, 0], [0, s.Rational(5, 13), 12 * s.I / 13],
              [0, 12 * s.I / 13, s.Rational(5, 13)]])
v = s.diag(s.I, -s.I, 1)
for m in (u, r, v):
    matrix_zero(m.H * m - s.eye(n))
    zero(m.det() - 1)

ap, am = u * r, v * u.H
wp, wm = s.trace(ap), s.trace(am)
dp = [s.trace(ta * u * r) for ta in basis]
dm = [-s.trace(u.H * ta * v) for ta in basis]
for ta, d in zip(basis, dm):
    zero(d + s.trace(ta * am))
    checks += 1
for a, w, ds in ((ap, wp, dp), (am, wm, dm)):
    zero(sum(d * s.conjugate(d) for d in ds)
         - (n * n - w * s.conjugate(w)) / (2 * n))
    zero(sum(d * d for d in ds)
         + (s.trace(a * a) - w * w / n) / 2)
    zero(sum(s.re(d) ** 2 for d in ds)
         - (n - s.re(s.trace(a * a)) - 2 * s.im(w) ** 2 / n) / 4)
    checks += 3

zero(sum(x * s.conjugate(y) for x, y in zip(dp, dm))
     + (s.trace(ap * am.H) - wp * s.conjugate(wm) / n) / 2)
zero(sum(x * y for x, y in zip(dp, dm))
     - (s.trace(ap * am) - wp * wm / n) / 2)
checks += 2

# A word with two occurrences of the same physical edge, with opposite signs.
a1, a2 = u * r * u.H * v, v * u * r * u.H
ds = [s.trace(ta * u * r * u.H * v - u * r * u.H * ta * v)
      for ta in basis]
for ta, d in zip(basis, ds):
    zero(d - s.trace(ta * a1) + s.trace(ta * a2))
    # Setting v=I makes the trace of u*r*u^-1 independent of u.
    zero(s.trace(ta * u * r * u.H - u * r * u.H * ta))
    checks += 2
rhs = 0
for eps, a in ((1, a1), (-1, a2)):
    for eta, b in ((1, a1), (-1, a2)):
        rhs += eps * eta * (s.trace(a * b.H)
                            - s.trace(a) * s.conjugate(s.trace(b)) / n) / 2
zero(sum(d * s.conjugate(d) for d in ds) - rhs)
checks += 1

# Exact local ground-state product rule in one coordinate, arbitrary functions.
x = s.symbols('x', real=True)
kappa = s.symbols('kappa', positive=True)
psi, f, g = (s.Function(z)(x) for z in ('psi', 'f', 'g'))
potential_minus_ground = kappa * s.diff(psi, x, 2) / psi
shifted_h = -kappa * s.diff(psi * g, x, 2) + potential_minus_ground * psi * g
identity = (psi * f * shifted_h
            - kappa * psi**2 * s.diff(f, x) * s.diff(g, x)
            + kappa * s.diff(psi**2 * f * s.diff(g, x), x))
zero(identity)
checks += 1

print(f'PASS: {checks} exact scalar assertions, plus exact matrix entries.')
print('Checked SU(2), SU(3), SU(4) Fierz normalization and Casimir; metric factor 4;')
print('oriented SU(3) loop contractions, repeated-edge terms, real trace, product rule.')
print('No interacting vacuum or continuum spectrum was computed.')

```

## Complete source: wilson_variation/check_temporal_coefficients.py

```python
"""Exact finite algebra checks for temporal_transfer.tex; no numerical limit."""
import sympy as s


def zero(value):
    assert s.simplify(value) == 0, value


def matrix_zero(value):
    for entry in value:
        zero(entry)


checks = 0
a, eps, g2, b, x = s.symbols('a eps g2 b x', positive=True)
bt = a / (2 * g2 * eps)
bs = eps / (2 * g2 * a)
zero(bt * (a * eps)**2 / (a**3 * eps) - 1 / (2 * g2))
zero(bs * a**4 / (a**3 * eps) - 1 / (2 * g2))
zero(bs / eps - 1 / (2 * g2 * a))
zero((2 * g2 / a) / 4 - g2 / (2 * a))
checks += 4


def bessel_polynomial(d, cutoff):
    return sum(b**(2 * r + d) / (s.factorial(r) * s.factorial(r + d))
               for r in range(cutoff + 1))


for d in range(1, 10):
    # Exact formal coefficients, no use of floating point or Bessel asymptotics.
    recurrence = (bessel_polynomial(d - 1, 10)
                  - bessel_polynomial(d + 1, 10)
                  - s.Integer(d) * bessel_polynomial(d, 10) / b)
    for power in range(d - 1, d + 18):
        zero(s.expand(recurrence).coeff(b, power))
        checks += 1
    character = s.chebyshevu(d - 1, x)
    zero(character.subs(x, 1) - d)
    zero(s.diff(character, x).subs(x, 1) / d - s.Rational(d*d - 1, 3))
    casimir = s.Rational(d*d - 1, 4)
    first_coefficient = s.Rational(d*d - 1, 3) * s.Rational(3, 4)
    zero(first_coefficient - casimir)
    zero((casimir / bt) / eps - 2 * g2 * casimir / a)
    checks += 4

# The two exact leading moment ratios arising from the gamma integrals.
zero(s.gamma(s.Rational(5, 2)) / (2 * s.gamma(s.Rational(3, 2)))
     - s.Rational(3, 4))
zero(s.gamma(s.Rational(7, 2)) / (4 * s.gamma(s.Rational(3, 2)))
     - s.Rational(15, 16))
checks += 2

# Metric convention and its unaltered kinetic coefficient.
sigma = [s.Matrix([[0, 1], [1, 0]]),
         s.Matrix([[0, -s.I], [s.I, 0]]),
         s.diag(1, -1)]
basis = [s.I * q / 2 for q in sigma]
for i, ta in enumerate(basis):
    for j, tb in enumerate(basis):
        zero(-2 * s.trace(ta * tb) - int(i == j))
        zero(-s.trace((2 * ta) * (2 * tb)) / 2 - int(i == j))
        checks += 2
matrix_zero(sum((ta * ta for ta in basis), s.zeros(2))
            + s.Rational(3, 4) * s.eye(2))


def q0(c, d):
    return s.Matrix([[c, d], [-d, c]])


def q1(c, d):
    return s.Matrix([[c, s.I * d], [s.I * d, c]])


u = q0(s.Rational(3, 5), s.Rational(4, 5))
up = q1(s.Rational(5, 13), s.Rational(12, 13))
vs = s.diag(s.I, -s.I)
vt = q0(s.Rational(8, 17), s.Rational(15, 17))
h0s, h0t, h1s, h1t = up, vt, u, vs
for value in (u, up, vs, vt):
    matrix_zero(value.H * value - s.eye(2))
    zero(value.det() - 1)
    checks += 1

plaquette = u * vt * up.H * vs.H
transformed_future = vs * up * vt.H
matrix_zero(plaquette.H - transformed_future * u.H)
zero(s.re(s.trace(plaquette))
     - s.re(s.trace(transformed_future * u.H)))
checks += 1

# Original inverse-transport gauge law h_source^-1 U h_target at both times.
u_h = h0s.H * u * h0t
up_h = h1s.H * up * h1t
vs_h = h0s.H * vs * h1s
vt_h = h0t.H * vt * h1t
p_h = u_h * vt_h * up_h.H * vs_h.H
matrix_zero(p_h - h0s.H * plaquette * h0s)
# Dictionary alpha_g=beta_h with g=h^-1.
gs, gt = h0s.H, h0t.H
matrix_zero(gs * u * gt.H - u_h)

# Symmetric endpoint magnetic weights produce one complete interior slice.
v0, v1, v2 = s.symbols('v0 v1 v2', real=True)
zero(eps * (v0 + v1) / 2 + eps * (v1 + v2) / 2
     - eps * (v0 / 2 + v1 + v2 / 2))
checks += 1

print(f'PASS: {checks} exact scalar assertions, plus exact matrix-entry checks.')
print('Checked anisotropic action coefficients, spin multiplier coefficients,')
print('SU(2) metrics/Casimir, temporal plaquette ordering, gauge dictionary,')
print('and symmetric magnetic endpoint weights. No numerical vacuum was used.')

```

## Complete source: wilson_variation/check_spatial_elimination.py

```python
"""Exact sign/coefficient checks; the unbounded-domain proofs are in the TeX.

The finite matrices below are an algebra diagnostic, not a numerical model
of the interacting Yang--Mills vacuum or a continuum approximation.
"""
import sympy as s


def zero(value):
    assert s.simplify(value) == 0, value


def matrix_zero(value):
    for entry in value:
        zero(entry)


checks = 0
x, y = s.symbols('x y', real=True)
kappa, z = s.symbols('kappa z', positive=True)
rho = s.Function('rho')(y, x)
marginal = s.Function('rho_R')(x)
f = s.Function('f')(x)
full_lift = -kappa * (s.diff(f, x, 2) + s.diff(rho, x) * s.diff(f, x) / rho)
reduced = -kappa * (s.diff(f, x, 2)
                    + s.diff(marginal, x) * s.diff(f, x) / marginal)
score = s.diff(rho, x) / rho - s.diff(marginal, x) / marginal
zero(full_lift - reduced + kappa * score * s.diff(f, x))
checks += 1

# The first retained basis vector is an exact zero-energy constant.
lmat = s.Matrix([[0, 0, 0], [0, 5, 2], [0, 2, 3]])
jmat = s.Matrix([[1, 0], [0, 1], [0, 0]])
amat = s.diag(0, 5)
bmat = s.Matrix([[0, 2]])
cmat = s.Matrix([[3]])
rmat = (cmat + z * s.eye(1)).inv()
schur = amat + z * s.eye(2) - bmat.T * rmat * bmat
matrix_zero(jmat.T * (lmat + z * s.eye(3)).inv() * jmat - schur.inv())
matrix_zero(jmat.T * lmat * jmat - amat)
matrix_zero(jmat.T * lmat**2 * jmat - amat**2 - bmat.T * bmat)
checks += 3

fvec = s.Matrix([0, 1])
wvec = rmat * bmat * fvec
uvec = jmat * fvec - s.Matrix([0, 0, wvec[0]])
base_energy = (fvec.T * amat * fvec)[0]
correction = (fvec.T * bmat.T * wvec)[0]
wnorm = (wvec.T * wvec)[0]
num = base_energy - correction - z * wnorm
den = (fvec.T * fvec)[0] + wnorm
zero((uvec.T * lmat * uvec)[0] - num)
zero((uvec.T * uvec)[0] - den)
zero((num / den).subs(z, 0) - s.Rational(33, 13))
zero((num / den - 5) - (-4 * (8 + 2 * z) / ((z + 3)**2 + 4)))
checks += 4

f1, f2, h = s.symbols('f1 f2 h', real=True)
fv = s.Matrix([f1, f2])
hv = s.Matrix([h])
v = jmat * fv + s.Matrix([0, 0, h])
square = ((fv.T * schur * fv)[0]
          + ((hv + rmat * bmat * fv).T
             * (cmat + z * s.eye(1)) * (hv + rmat * bmat * fv))[0])
zero((v.T * (lmat + z * s.eye(3)) * v)[0] - square)
checks += 1

# Formal short-time coefficient from the memory equation has the plus sign.
t = s.symbols('t', nonnegative=True)
kseries = s.eye(2) - t * amat + t**2 * (amat**2 + bmat.T * bmat) / 2
matrix_zero(kseries.diff(t).subs(t, 0) + amat)
matrix_zero(kseries.diff(t, 2).subs(t, 0) - amat**2 - bmat.T * bmat)
checks += 2

# Exact metric dictionary in the B term: X_c=2X, sigma_c=2sigma, kappa_c=kappa/4.
sigma, xf = s.symbols('sigma xf', real=True)
zero(-(kappa / 4) * (2 * sigma) * (2 * xf) + kappa * sigma * xf)
checks += 1

print(f'PASS: {checks} exact scalar/block assertions, plus exact matrix entries.')
print('Checked conditional-score cancellation, Schur inverse and reconstruction,')
print('square completion, corrected Rayleigh numerator/denominator, second moment,')
print('memory sign, and original metric factor. No vacuum approximation was used.')

```

## Complete source: adjacent_plaquette_quantum_correction.md

```markdown
# A nonzero quantum elimination correction on two adjacent Wilson plaquettes

8 September 2026. This is an explicit finite interacting calculation, not
a four-dimensional continuum mass-gap result. It evaluates a vacuum-dependent
elimination correction on a genuine gauge-invariant retained observable.

## 1. Original coefficients, graph and operator

Take two adjacent square plaquettes, P and Q, with a single common edge e,
six other distinct edges, and open boundary. This finite cell complex has
seven physical links; no link outside this specified complex is presumed
to have been integrated without its interaction. Choose orientations so
their ordered holonomies, after cyclic changes of their base vertices, are
\[
 P=U_e A,\qquad Q=U_e^{-1}B,
\]
where A and B are the ordered products of the respective three outer links.
Set \(W_P=\operatorname{tr}P\), \(W_Q=\operatorname{tr}Q\). These are real
for SU(2). Each Haar measure has total mass one; the total configuration
space is \(\mathcal Q=SU(2)^7\), with product measure \(d\lambda\).
Use the anti-Hermitian basis \(T_a=i\sigma_a/2\),
\(-2\operatorname{tr}T_aT_b=\delta_{ab}\), and the actual Hamiltonian
\[
 H= -\kappa\sum_{f=1}^7\Delta_f^T
       +b(4-W_P-W_Q),\qquad \kappa>0,\quad b>0.
\]
Every plaquette of this complex is retained. Its relation to the original
action convention \(c=-\operatorname{tr}/2\) is
\[
 \Delta^c=4\Delta^T,\qquad
 \kappa=\frac{2g_{\rm YM}^2}{a},\quad
 b=\frac1{2g_{\rm YM}^2a},\quad
 \xi:=\frac b\kappa=\frac1{4g_{\rm YM}^4}.
\]
Thus the small parameter below is a specified strong-coupling parameter,
not a removal of the interaction at the positive values under study.

The compact elliptic operator H has a unique strictly positive smooth
ground state. One proof is the strictly positive heat kernel for the
product Laplacian and its Feynman--Kac formula with the bounded real
potential. Compactness gives a lowest eigenfunction; replacing it by its
absolute value does not increase its form, and positivity improvement
makes the lowest eigenspace one-dimensional. Gauge transformations commute
with H and preserve positivity, so this ground state is gauge invariant.
Write its unit-L2 representative as \(\psi_\xi\), its eigenvalue as
\(E_\xi\), and \(d\mu_\xi=\rho_\xi d\lambda=\psi_\xi^2d\lambda\).
The unit-L2 convention fixes the state only: all scalar factors below are
retained explicitly.

## 2. Controlled first derivative of the actual vacuum

Let \(H_0=-\sum_f\Delta_f^T\). The exact operator identity is
\[
 H=\kappa[H_0-\xi(W_P+W_Q)]+4bI.
\]
The scalar \(4bI\) is not discarded from H; it changes its ground energy
by exactly 4b and leaves its ground vector and excitation differences
unchanged. The constant function is the simple zero eigenvector of H0,
and the next eigenvalue on the full link Hilbert space is 3/4, from the
spin-1/2 Casimir on one link. On the complex circle \(|z|=3/8\), the
resolvent of H0 has norm at most 8/3. Since \(|W_P+W_Q|\leq4\), its
resolvent Neumann series converges uniformly when \(|\xi|<3/32\).
The Riesz integral therefore gives an analytic rank-one eigenprojection
near zero. For real sufficiently small xi this is the ground projection;
the remainder of the spectrum stays separated by bounded perturbation.

Choose its analytic eigenvector \(\phi_\xi\) with
\(\int\phi_\xi d\lambda=1\). This fixes a representative, not the
physical state norm. Put
\[
 Z_\xi=\int\phi_\xi^2d\lambda,\qquad
 \psi_\xi=\phi_\xi/Z_\xi^{1/2},\qquad
 \rho_\xi=\phi_\xi^2/Z_\xi.
\]
Haar integration of a link appearing once gives \(\int W_P=\int W_Q=0\).
Each plaquette uses four links, each with Casimir 3/4, so
\(H_0W_P=3W_P\) and \(H_0W_Q=3W_Q\). Differentiating the eigen-equation
at xi=0, including its scalar eigenvalue, now gives
\[
 \phi_\xi=1+\frac\xi3(W_P+W_Q)+O(\xi^2),\qquad
 \log\rho_\xi=\frac{2\xi}3(W_P+W_Q)+O(\xi^2).
\]
The remainders hold in every fixed Ck norm. To justify this regularity,
start with the L2 analytic Riesz vector. The eigen-equation expresses H0
applied to that vector as multiplication by a fixed smooth function times
the vector, plus its scalar eigenvalue times the vector. The elliptic
estimate for the product Laplacian gains two Sobolev derivatives at each
iteration. Multiplication by the fixed Wilson polynomial is bounded in
each such Sobolev norm. Iterating also on the differentiated equations
gives analytic dependence in each fixed Sobolev norm; Sobolev embedding
then gives the stated fixed Ck bounds. Strict positivity near 1 permits
the ordinary logarithm with these same local analytic bounds.

The normalization factor is
\(Z_\xi=1+2\xi^2/9+O(\xi^3)\): the linear coefficient has zero mean,
its squared norm is 2/9, and every higher coefficient of phi has zero
mean by the chosen representative. This records rather than hides the
first state-normalization correction.

## 3. Eliminated link and the true conditional score

Let S consist of one outer edge of P which is not in Q, and let R contain
the other six edges. Use lower-case s and r for their configuration
variables. Define the actual marginal and lift
\[
 \rho_{R,\xi}(r)=\int\rho_\xi(s,r)d\lambda_S(s),\qquad Jf(s,r)=f(r).
\]
J is an isometry from \(L^2(\rho_{R,\xi}d\lambda_R)\) into
\(L^2(\mu_\xi)\). Its adjoint is the literal conditional integral
\[
 (J_\xi^*u)(r)=\rho_{R,\xi}(r)^{-1}
             \int u(s,r)\rho_\xi(s,r)d\lambda_S(s).
\]
Put \(P_\xi=JJ_\xi^*\) and \(Q_\xi=I-P_\xi\). These symbols denote
orthogonal Hilbert-space projections, not the two plaquette holonomies.
In particular the formula specifies every dependence of the projection
on the true vacuum.

The ground-state transformed nonnegative operator is
\[
 L_\xi=\psi_\xi^{-1}(H-E_\xi)\psi_\xi
       =-\kappa\sum_{f,a}\rho_\xi^{-1}X_{f,a}(\rho_\xi X_{f,a}).
\]
For a smooth retained function f, direct differentiation and conditional
integration give
\[
 L_\xi Jf=JA_\xi f+B_\xi f,
\]
\[
 A_\xi f=-\kappa\sum_{f'\in R,a}
       \rho_{R,\xi}^{-1}X_{f',a}(\rho_{R,\xi}X_{f',a}f),
\]
\[
 B_\xi f=-\kappa\sum_{f'\in R,a}
 (X_{f',a}\log\rho_\xi-X_{f',a}\log\rho_{R,\xi})X_{f',a}f.
\]
The last function has zero conditional mean, since differentiating the
marginal integral gives
\(J_\xi^*(X\log\rho_\xi)=X\log\rho_{R,\xi}\). Thus it is the actual
component in the eliminated subspace. No independent-link vacuum is used.

Choose the gauge-invariant retained observable
\(f_\xi=W_Q-\mu_\xi(W_Q)\). Haar integration over S annihilates WP
and all its derivatives on R, while leaving WQ unchanged. Therefore
\[
 B_\xi f_\xi=-\frac{2b}{3}\,G+O(b^2/\kappa),\qquad
 G:=\sum_{a=1}^3(X_{e,a}W_P)(X_{e,a}W_Q).
\]
Only the common edge contributes: all other derivatives of the two
plaquettes have disjoint supports. The remainder is in any fixed Sobolev
norm on this finite compact configuration space, at fixed kappa.

## 4. Exact color contraction and two eliminated eigencomponents

Set \(Q'=BU_e^{-1}\). Then trace Q'=trace Q and
\[
 X_{e,a}W_P=\operatorname{tr}(T_aP),\qquad
 X_{e,a}W_Q=-\operatorname{tr}(T_aQ').
\]
The SU(2) Fierz identity in this exact basis is
\[
 \sum_a\operatorname{tr}(T_aC)\operatorname{tr}(T_aD)
 =-\tfrac12[\operatorname{tr}(CD)-\tfrac12\operatorname{tr}C\operatorname{tr}D].
\]
It follows by substituting the three Pauli matrices, or equivalently their
entry identity \(\sum_a(T_a)_{ij}(T_a)_{kl}
=-\tfrac12(\delta_{il}\delta_{jk}-\tfrac12\delta_{ij}\delta_{kl})\).
Let
\[
 R_0=\operatorname{tr}(AB),\quad D_0=W_PW_Q,\quad
 D_1=D_0-\tfrac12R_0.
\]
R0 is the outer six-edge Wilson loop and is independent of the shared edge.
The contraction, with its opposite shared-edge orientation retained, is
\[
 G=\tfrac12R_0-\tfrac14D_0
   =\tfrac38R_0-\tfrac14D_1.
\]
To check all Haar inner products explicitly, for fixed Ue the products
P and Q' are independent Haar SU(2) matrices because A and B are products
of disjoint independent Haar edges. Write
\(P=p_0I+i\sum p_a\sigma_a\), \(Q'=q_0I+i\sum q_a\sigma_a\).
Each p or q is uniform on the unit three-sphere, so
\(\mathbb E p_\alpha p_\beta=\delta_{\alpha\beta}/4\), and the same
holds for q. Direct substitution gives
\[
 G=-\sum_{a=1}^3p_aq_a,\quad
 R_0=2(p_0q_0-\sum_ap_aq_a),\quad
 D_1=3p_0q_0+\sum_ap_aq_a.
\]
Consequently
\[
 \|R_0\|_\lambda^2=1,\qquad \|D_1\|_\lambda^2=\tfrac34,
 \quad\langle R_0,D_1\rangle_\lambda=0,
 \quad\|G\|_\lambda^2=\tfrac3{16}.
\]
Each of the six outer-link Laplacians acts on R0 and D1 by -3/4.
For the common edge, the product rule gives
\[
 \Delta_e^T D_0=-\tfrac32D_0+2G=R_0-2D_0=-2D_1,
 \qquad \Delta_e^T R_0=0.
\]
Therefore
\[
 \kappa H_0R_0=\tfrac{9\kappa}{2}R_0,\qquad
 \kappa H_0D_1=\tfrac{13\kappa}{2}D_1.
\]
Both have zero conditional mean over S, so these are also their
eigenvalues in the eliminated subspace at xi=0. In particular
\[
 B_\xi f_\xi=-\frac b4R_0+\frac b6D_1+O(b^2/\kappa),\qquad
 \|B_\xi f_\xi\|_{\mu_\xi}^2
      =\frac{b^2}{12}+O(b^3/\kappa).
\]
This proves that the eliminated quantum coupling on an actual retained
Wilson observable is nonzero for all sufficiently small positive b/kappa.
It is not a nonzero coupling assumed for an unspecified observable.

## 5. A full-system trial state with a strictly lower excitation energy

Let Cxi be the nonnegative self-adjoint operator associated to the closed
form of Lxi restricted to \(\ker J_\xi^*\). The form domain is the
intersection of that closed subspace with H1. The smooth positive density
and its derivatives are bounded above and below on the compact product.
The explicit conditional integral above is a bounded map on H1; therefore
the domain is closed in the form norm and dense in the eliminated
subspace, by applying Qxi to smooth approximations. This constructs Cxi
without assuming a domain for a formal operator product.

For z>0, define
\[
 w_{\xi,z}=(C_\xi+z)^{-1}B_\xi f_\xi,\qquad
 u_{\xi,z}=\psi_\xi(Jf_\xi-w_{\xi,z}).
\]
All conditional projections, operators and vectors here commute with the
vertex gauge action; hence u is a physical gauge-invariant state. Its
inner product with the vacuum is zero, since f is centered and w has
zero conditional mean. Put
\[
 d_\xi=\|f_\xi\|_{\rho_{R,\xi}}^2,\quad
 a_\xi=\kappa\sum_{f'\in R,a}\mu_\xi(|X_{f',a}f_\xi|^2),
 \quad I_{\xi,z}=\langle B_\xi f_\xi,w_{\xi,z}\rangle,
 \quad J_{\xi,z}=\|w_{\xi,z}\|^2.
\]
I is real and nonnegative. Testing the resolvent equation by w gives
\(\mathfrak c_\xi(w,w)=I_{\xi,z}-zJ_{\xi,z}\). The cross form between
Jf and w is exactly \(\langle B_\xi f,w\rangle\). Expanding the full
form and norm, with their cross terms, gives the exact two Rayleigh values
\[
 \mathcal R_{\rm retained}=\frac{a_\xi}{d_\xi},\qquad
 \mathcal R_{\rm full}(z)=
 \frac{a_\xi-I_{\xi,z}-zJ_{\xi,z}}{d_\xi+J_{\xi,z}},
\]
and the exact decrease
\[
 \mathcal R_{\rm retained}-\mathcal R_{\rm full}(z)
 =\frac{I_{\xi,z}+(z+\mathcal R_{\rm retained})J_{\xi,z}}
        {d_\xi+J_{\xi,z}}>0
\]
whenever Bxi fxi is nonzero. This is a constructed improved vector in the
original seven-link interacting Hilbert space, not an assignment of an
effective classical potential to a quantum energy.

For completeness the expansions of this resolvent as xi tends to zero
are controlled on the fixed compact complex. The densities and their
first derivatives differ from their xi=0 values by O(xi), uniformly.
The conditional integral formula implies
\(P_\xi-P_0=O(\xi)\) both on L2 and on H1. All Pxi have exactly the
same range, the functions of the retained links. Thus
\(P_\xi P_0=P_0\), \(P_0P_\xi=P_\xi\), and consequently
\(Q_0Q_\xi=Q_0\), \(Q_\xi Q_0=Q_\xi\).
On \(\ker P_0\), the map \(T_\xi=Q_\xi|_{\ker P_0}\)
therefore has the exact inverse \(Q_0|_{\ker P_\xi}\).
Both preserve H1 by the conditional integral bounds. This is an exact
identification of the moving form domains, not an assumption that the
conditional projections are independent of xi. After this
identification, the forms Cxi+z are uniformly coercive in H1 and differ
from the xi=0 form by O(xi) in H1 form norm. Subtracting their weak
resolvent equations and using coercivity proves an O(xi) difference of
solution maps from the dual of H1 to H1. Applying this to the already
proved \(B_\xi f_\xi=b(-R_0/4+D_1/6)+O(b\xi)\) justifies, without
an unproved interchange of spectra or projections,
\[
 w_{\xi,z}=-\frac{b}{4(9\kappa/2+z)}R_0
             +\frac{b}{6(13\kappa/2+z)}D_1+O(\xi^2)
\]
at fixed positive kappa and z. The error is in H1 and includes the
variation of the conditional projection and state density.

In particular, with the retained choice z=kappa,
\[
 I_{\xi,\kappa}=\frac{b^2}{\kappa}
           \left(\frac1{88}+\frac1{360}\right)+O(b^3/\kappa^2)
           =\frac{7b^2}{495\kappa}+O(b^3/\kappa^2),
\]
\[
 J_{\xi,\kappa}=\frac{b^2}{\kappa^2}
           \left(\frac1{484}+\frac1{2700}\right)+O(b^3/\kappa^3)
           =\frac{199b^2}{81675\kappa^2}+O(b^3/\kappa^3).
\]
Haar integration gives \(d_0=1\) and \(a_0=3\kappa\); their changes
are O(xi) with the respective retained scales. Substitution in the exact
decrease formula therefore proves the explicit positive coefficient
\[
 \boxed{\mathcal R_{\rm retained}-\mathcal R_{\rm full}(\kappa)
     =\frac{1951}{81675}\frac{b^2}{\kappa}
          +O(b^3/\kappa^2).}
\]
In the original coupling and spatial spacing this coefficient is
\(1951/[653400\,g_{\rm YM}^6a]\), with remainder of order
\(1/(g_{\rm YM}^{10}a)\) in the stated strong-coupling regime.

### 5.1 Absolute excitation energies, not only their difference

The absolute trial-state energies can also be computed to this order. Let
\(F=W_P+W_Q\), and write the mean-one vacuum representative as
\(\phi_\xi=1+\xi F/3+\xi^2\phi_2+O(\xi^3)\). Its eigen-equation and
mean constraint give
\[
 H_0\phi_2=(F^2-2)/3,\qquad \int\phi_2d\lambda=0.
\]
The subtracted 2 is the exact \(\int F^2d\lambda\), not a removed
plaquette. The identity \(W_Q^2=1+\chi_{\rm ad}(Q)\) follows by
\(2\cos\theta\) squared, with
\(\chi_{\rm ad}=1+2\cos2\theta\). The adjoint Casimir is 2 on each
of Q's four links, so \(H_0\chi_{\rm ad}(Q)=8\chi_{\rm ad}(Q)\).
The independent Haar holonomies P and Q satisfy
\[
 \int W_Q^2=1,\qquad\int W_Q^4=2,\qquad
 \int F^2W_Q^2=3,\qquad\int F^2\chi_{\rm ad}(Q)=1.
\]
For the fourth moment, \(W_Q=2q_0\) and the S3 marginal used above gives
\(\int q_0^4=1/8\), either by its beta integral or the corresponding
even moment recurrence. Cross terms vanish by Haar symmetry of P and Q.
Self-adjointness of H0 now yields
\[
 \int\phi_2 W_Q^2d\lambda
 =\int\phi_2\chi_{\rm ad}(Q)d\lambda=\frac1{24}.
\]
Using the full state-density expansion, including Zxi,
\[
 \rho_\xi=1+\frac{2\xi}3F
     +\xi^2\left(\frac{F^2}{9}+2\phi_2-\frac29\right)+O(\xi^3),
\]
therefore gives
\[
 r_\xi:=\mu_\xi(W_Q^2)=1+\frac7{36}\xi^2+O(\xi^3),\qquad
 \mu_\xi(W_Q)=\frac23\xi+O(\xi^2),
\]
\[
 d_\xi=r_\xi-\mu_\xi(W_Q)^2=1-\frac14\xi^2+O(\xi^3).
\]
For a single edge of the SU(2) loop,
\(\sum_a|X_{e,a}W_Q|^2=(4-W_Q^2)/4\), by the displayed Pauli
coordinates. Summing its four edges gives exactly
\(a_\xi=\kappa(4-r_\xi)\). Hence the absolute excitation Rayleigh
values relative to the same actual vacuum are
\[
 \boxed{\mathcal R_{\rm retained}
    =3\kappa+\frac59\frac{b^2}{\kappa}+O(b^3/\kappa^2),}
\]
\[
 \boxed{\mathcal R_{\rm full}(\kappa)
    =3\kappa+\frac{43424}{81675}\frac{b^2}{\kappa}
         +O(b^3/\kappa^2).}
\]
The latter coefficient is precisely
\(5/9-1951/81675=43424/81675\). The elimination correction decreases
the variational energy at the same positive coupling, but both trial
energies increase from their common zero-b value to this order. Neither
the decrease nor the positive second-order coefficients determine the
full spectrum or a limiting four-dimensional gap.

For completeness the energy origin is explicit as well. Taking the Haar
mean of the second-order eigen-equation gives
\(e(\xi)=-2\xi^2/3+O(\xi^3)\). The actual, unsubtracted Hamiltonian
therefore has vacuum energy
\[
 E_\xi=4b-\frac{2b^2}{3\kappa}+O(b^3/\kappa^2).
\]
Adding this same scalar to each excitation quotient gives the two trial
quotients for H itself:
\[
 3\kappa+4b-\frac19\frac{b^2}{\kappa}+O(b^3/\kappa^2),\qquad
 3\kappa+4b-\frac{11026}{81675}\frac{b^2}{\kappa}
       +O(b^3/\kappa^2),
\]
respectively. The mass-gap question concerns energies above the vacuum,
so the preceding excitation quotients, not this common scalar shift,
are the quantities used in the variational comparison.

## 6. Meaning and sources

The correction is already present in a nonlinear gauge-invariant quantum
calculation: it comes from covariance between a retained loop and the
eliminated link through their common plaquette edge. Its two explicit
Casimir channels, 9kappa/2 and 13kappa/2, supply the coefficient above.
The improved state still has an excitation Rayleigh value near 3kappa in
this regime. No small-energy continuum state or four-dimensional quantum
mass-gap disproof is inferred from this finite-complex result.

The exact general marginal, resolvent and trial-state identities are
proved in the companion source `spatial_vacuum_elimination.tex`; the
calculation above evaluates its nonzero coupling rather than assuming it.
The original coefficient dictionary is proved from the temporal Wilson
integral in `temporal_transfer.tex`. The compact-ground-state and Fierz
identities are expanded in `wilson_finite_lattice.tex`.

The general elimination method is established literature, not claimed as
a new discovery: G. Dusson, I. M. Sigal and B. Stamm,
*The Feshbach–Schur map and perturbation theory*, pp. 65–88 (2021),
<https://doi.org/10.4171/ECR/18-1/5>,
<https://arxiv.org/abs/2105.02058>.
The lattice Hamiltonian context is J. Kogut and L. Susskind,
*Hamiltonian formulation of Wilson's lattice gauge theories*,
Physical Review D 11 (1975), 395–408,
<https://doi.org/10.1103/PhysRevD.11.395>.

```

## Complete source: check_adjacent_plaquette.py

```python
"""Exact finite algebra for the adjacent-plaquette quantum correction.

The analytic ground-state and form-resolvent arguments are in the proof;
this script checks the original color, Haar and rational coefficients.
"""
from pathlib import Path
from hashlib import sha256
import json
import sympy as s

checks = []

def eq(name, value):
    assert s.expand(value) == 0, (name, value)
    checks.append(name)

p = s.symbols('p0:4', real=True)
q = s.symbols('q0:4', real=True)
sigma = [s.Matrix([[0, 1], [1, 0]]),
         s.Matrix([[0, -s.I], [s.I, 0]]), s.diag(1, -1)]
basis = [s.I*x/2 for x in sigma]
P = p[0]*s.eye(2) + sum((s.I*p[i+1]*sigma[i] for i in range(3)),s.zeros(2))
Q = q[0]*s.eye(2) + sum((s.I*q[i+1]*sigma[i] for i in range(3)),s.zeros(2))
dot = sum(p[i]*q[i] for i in range(1,4))
G = -sum(s.trace(t*P)*s.trace(t*Q) for t in basis)
R = s.trace(P*Q)
D = s.trace(P)*s.trace(Q)
D1 = D-R/2
eq('opposite-edge derivative contraction',G+dot)
eq('exact Fierz contraction',G-R/2+D/4)
eq('two-channel decomposition',G-s.Rational(3,8)*R+D1/4)
eq('outer trace coordinates',R-2*(p[0]*q[0]-dot))
eq('spin-one coordinates',D1-3*p[0]*q[0]-dot)

def haar_degree_two(poly):
    """Every argument has degree exactly two in each independent S^3 vector."""
    answer = s.S(0)
    for powers,coef in s.Poly(s.expand(poly),*(p+q)).terms():
        pp,qq=powers[:4],powers[4:]
        assert sum(pp)==sum(qq)==2
        if 2 in pp and 2 in qq:
            answer += coef/16
    return answer

eq('Haar R norm',haar_degree_two(R**2)-1)
eq('Haar D1 norm',haar_degree_two(D1**2)-s.Rational(3,4))
eq('Haar channel orthogonality',haar_degree_two(R*D1))
eq('Haar contraction norm',haar_degree_two(G**2)-s.Rational(3,16))
eq('Haar plaquette product norm',haar_degree_two(D**2)-1)

# Product rule for the common link: each fundamental trace has Δ=-3/4.
delta_D = -s.Rational(3,2)*D+2*G
eq('shared-edge spin-one Casimir',delta_D+2*D1)
eq('outer-loop free energy',6*s.Rational(3,4)-s.Rational(9,2))
eq('spin-one total free energy',6*s.Rational(3,4)+2-s.Rational(13,2))

k,b,z,g,a=s.symbols('kappa b z g a',positive=True)
eq('actual B leading coefficient',-2*b*G/3-(-b*R/4+b*D1/6))
eq('actual B squared leading norm',haar_degree_two((-2*b*G/3)**2)-b*b/12)
I_at_k=(b*b/(16*(s.Rational(9,2)*k+k))
        +b*b/(48*(s.Rational(13,2)*k+k)))
J_at_k=(b*b/(16*(s.Rational(9,2)*k+k)**2)
        +b*b/(48*(s.Rational(13,2)*k+k)**2))
eq('resolvent inner coefficient',I_at_k-s.Rational(7,495)*b*b/k)
eq('resolvent squared norm coefficient',J_at_k-s.Rational(199,81675)*b*b/k**2)
eq('Rayleigh improvement coefficient',I_at_k+4*k*J_at_k
   -s.Rational(1951,81675)*b*b/k)
eq('original coupling coefficient',
   s.Rational(1951,81675)*(1/(2*g**2*a))**2/(2*g**2/a)
   -s.Rational(1951,653400)/(g**6*a))
eq('original coupling parameter',(1/(2*g**2*a))/(2*g**2/a)-1/(4*g**4))

eq('vacuum second coefficient against loop square',s.Rational(1,3)/8-s.Rational(1,24))
r2=s.Rational(3,9)+2*s.Rational(1,24)-s.Rational(2,9)
eq('actual loop second moment coefficient',r2-s.Rational(7,36))
d2=r2-s.Rational(2,3)**2
eq('actual loop variance coefficient',d2+s.Rational(1,4))
ret2=-r2-3*d2
eq('absolute retained Rayleigh coefficient',ret2-s.Rational(5,9))
eq('absolute corrected Rayleigh coefficient',ret2-s.Rational(1951,81675)
   -s.Rational(43424,81675))

root=Path(__file__).resolve().parent
proof=root/'adjacent_plaquette_quantum_correction.md'
receipt={'status':'PASS','checks':checks,'check_count':len(checks),
         'proof_bytes':proof.stat().st_size,
         'proof_sha256':sha256(proof.read_bytes()).hexdigest(),
         'scope':'Exact coefficient checks; not a computed interacting vacuum or continuum gap.'}
(root/'ADJACENT_PLAQUETTE_CHECKS.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf8')
print(json.dumps(receipt,indent=2))

```

## Complete source: wilson_variation/BULK_PLAQUETTE_EXTENSION.md

```markdown
# The adjacent-plaquette quantum correction in a full finite three-dimensional Wilson box

8 September 2026. All links and all elementary spatial plaquettes of the box are retained in the Hamiltonian. The only integration used to define the conditional projection eliminates one specified link from the **actual ground-state density**. This calculation neither replaces that density by a one-time Wilson density nor takes a spatial continuum or infinite-volume limit.

## 1. Exact statement, lattice, metric, and coupling dictionary

Let \(L\geq2\) be an integer. The vertices are

\[
\mathsf V_L=\{-L,-L+1,\ldots,L\}^3.
\]

There is one positively directed physical link \((n,i)\), from \(n\) to \(n+\mathbf e_i\), whenever both endpoints belong to \(\mathsf V_L\). Its variable is \(U_i(n)\in SU(2)\). A negatively traversed link contributes \(U_i(n)^{-1}\), not an independent variable. The set \(\mathsf E_L\) contains every such link. The set \(\mathsf P_L\) contains every elementary square \((n;i,j)\), \(1\leq i<j\leq3\), whose four vertices belong to \(\mathsf V_L\), with holonomy

\[
U_{n;i,j}=U_i(n)U_j(n+\mathbf e_i)
 U_i(n+\mathbf e_j)^{-1}U_j(n)^{-1},
\qquad W_{n;i,j}=\operatorname{tr}U_{n;i,j}.
\tag{1.1}
\]

Every \(W_p\) is real. There are

\[
N=|\mathsf E_L|=3(2L)(2L+1)^2,
\qquad M=|\mathsf P_L|=3(2L)^2(2L+1).
\tag{1.2}
\]

Indeed, a link direction has \(2L\) initial coordinates in that direction and \(2L+1\) choices in either transverse direction. A face plane has \(2L\) choices in each of its two directions and \(2L+1\) in the third. The three choices of direction, or plane, give (1.2). Boundary conditions are open; there are no periodic identifications.

Use \(T_a=-i\sigma_a/2\), \(a=1,2,3\), where \(\sigma_a\) are the Pauli matrices. Thus

\[
-2\operatorname{tr}(T_aT_b)=\delta_{ab},\quad
X_{e,a}f=\left.\frac{d}{dt}f(\ldots,e^{tT_a}U_e,\ldots)\right|_{t=0},
\quad \Delta_e^T=\sum_aX_{e,a}^2.
\tag{1.3}
\]

The companion two-plaquette calculation uses the opposite basis
\(T_a^{\mathrm{pair}}=+i\sigma_a/2\). The exact dictionary is
\(T_a=-T_a^{\mathrm{pair}}\), hence
\(X_{e,a}=-X_{e,a}^{\mathrm{pair}}\). It leaves
\(\sum_aX_{e,a}^2\) unchanged. Both factors in each derivative
contraction change sign: in particular
\(G=\sum_a(X_{e,a}W_P)(X_{e,a}W_Q)\) is unchanged, and the score
\(\sigma_{e,a}\) defined in (4.5) changes sign together with
\(X_{e,a}f\). Thus the operator B in (4.5), its norm, and the
Rayleigh coefficients below agree exactly with that convention.

The Hilbert space is \(\mathcal H=L^2(SU(2)^{\mathsf E_L},dU)\), where \(dU\) is product Haar probability measure. For \(\kappa,b>0\), the full nonlinear Wilson Hamiltonian is

\[
H_{\kappa,b}=-\kappa\sum_{e\in\mathsf E_L}\Delta_e^T
 +b\sum_{p\in\mathsf P_L}(2-W_p).
\tag{1.4}
\]

No term in either sum is dropped. Put \(\xi=b/\kappa\), \(H_0=-\sum_e\Delta_e^T\), and \(\mathcal V=\sum_{p\in\mathsf P_L}W_p\). Then the exact, including constant, identity is

\[
\boxed{H_{\kappa,b}=\kappa(H_0-\xi\mathcal V)+2bM\,I.}
\tag{1.5}
\]

The original metric is \(c(X,Y)=-\tfrac12\operatorname{tr}(XY)\), which is one quarter of the metric in (1.3). Its orthonormal basis is \(2T_a\), so \(X_{e,a}^c=2X_{e,a}\) and \(\Delta_e^c=4\Delta_e^T\). The original physical parameters are retained without substitution:

\[
\kappa=\frac{2g_{\mathrm{YM}}^2}{a},\qquad
b=\frac{1}{2g_{\mathrm{YM}}^2a},\qquad
\xi=\frac{1}{4g_{\mathrm{YM}}^4}.
\tag{1.6}
\]

Consequently the kinetic term in (1.4) is also

\[
-\frac{g_{\mathrm{YM}}^2}{2a}\sum_e\Delta_e^c.
\]

Let \(\psi_\xi>0\) be the normalized ground state of (1.4), \(\rho_\xi=\psi_\xi^2\), and \(E_\xi\) its ground energy. Define the particular faces and links

\[
Q=((0,0,0);1,2),\quad P=((-1,0,0);1,2),
\quad e=((0,0,0),2),\quad s=((-1,0,0),2).
\tag{1.7}
\]

Eliminate \(S=\{s\}\); retain \(R=\mathsf E_L\setminus\{s\}\). Write the retained centered observable as

\[
f_\xi=W_Q-\int W_Q\rho_\xi\,dU.
\tag{1.8}
\]

The conditional projection, the operator \(B_\xi\), the eliminated form operator \(C_\xi\), and the corrected physical vector \(u_\xi\) are defined in Sections 4 and 7 below, with their domains. The conclusions are

\[
\boxed{\|B_\xi f_\xi\|_{L^2(\rho_\xi dU)}^2
=\frac{b^2}{12}+O_L\!\left(\frac{b^3}{\kappa}\right),}
\tag{1.9}
\]

and

\[
\boxed{\mathcal R_{\mathrm{ret}}(\xi)-\mathcal R_{\mathrm{corr}}(\xi)
=\frac{1951}{81675}\frac{b^2}{\kappa}
 +O_L\!\left(\frac{b^3}{\kappa^2}\right).}
\tag{1.10}
\]

Here both quotients are exact quadratic-form Rayleigh quotients for \(H_{\kappa,b}-E_\xi\), the latter on a corrected full-system, gauge-invariant, vacuum-orthogonal vector. For each fixed \(L\), the remainders mean bounds by constants depending on that box for sufficiently small positive \(\xi\). The statements follow from convergent analytic perturbation locally at zero, not a formal substitution for the vacuum. In particular \(B_\xi f_\xi\ne0\) and the improvement is strict on an actual nonempty interval \(0<\xi<\epsilon_L\). No lower bound on \(\epsilon_L\) uniform in \(L\) is asserted.

The explicit resolvent Neumann disk supplied by the all-plaquette potential is

\[
\boxed{|\xi|<\frac{3}{16M}.}
\tag{1.11}
\]

It controls the isolated ground spectral projection as proved below. It is not an assertion that every local remainder estimate or strict-positivity test has the entire disk as its optimal radius.

## 2. Literal full-box incidence and orientations

A face containing the direction-2 link \(s=((-1,0,0),2)\) must lie in plane \(12\) or \(23\). In plane \(12\), it must extend from that link either in the positive or the negative direction 1. In plane \(23\), it must extend either in the positive or the negative direction 3. Thus its complete incidence star is

\[
\begin{split}
\mathsf I(s)=\{&((-1,0,0);1,2),\;((-2,0,0);1,2),\\
              &((-1,0,0);2,3),\;((-1,0,-1);2,3)\}.
\end{split}
\tag{2.1}
\]

All four faces exist when \(L\geq2\). This enumeration exhausts the possibilities because an elementary square has two coordinate directions, one of which must be the direction of its specified boundary link, and its unit transverse extent has only the two stated choices.

The last three faces in (2.1) have first coordinate at most \(-1\) at every vertex. Every vertex of \(Q\) has first coordinate 0 or 1. Hence each of those three faces has no vertex, and therefore no physical edge, in common with \(Q\). The remaining face is \(P\), and direct inspection of (1.1) gives

\[
\partial P\cap\partial Q=\{e\},\qquad
\{(p,i):p\in\mathsf I(s),\ i\in\partial p\cap\partial Q\}
=\{(P,e)\}.
\tag{2.2}
\]

The intersection here is of unoriented physical edges. The occurrence of \(e\) in \(P\) is positive, while its occurrence in \(Q\) is negative. The occurrence of \(s\) in \(P\) is negative. This proves the asserted incidence with no implicit exclusion of any other box plaquette.

For the based calculations, let

\[
\begin{split}
A&=U_1(-1,1,0)^{-1}U_2(-1,0,0)^{-1}U_1(-1,0,0),\\
B&=U_1(0,0,0)U_2(1,0,0)U_1(0,1,0)^{-1}.
\end{split}
\tag{2.3}
\]

Coordinates displayed as arguments are triples. Cyclically rotating the corresponding plaquette words in (1.1) gives the exactly equal Wilson traces of the based matrices

\[
P_*=U_eA,\qquad Q_*=U_e^{-1}B,\qquad Q'_*=BU_e^{-1}.
\tag{2.4}
\]

The products \(A,B\) use six distinct outer physical links and neither uses \(e\). The link \(s\) appears once, inversely, in \(A\), and does not appear in \(B\). The union of the two plaquette boundaries has exactly seven physical links. Every other link of the full box is still present in (1.4).

## 3. The actual all-plaquette vacuum and its controlled expansion

### 3.1 Free spectrum, bounded interaction, and the exact radius

On a single \(SU(2)\) factor with (1.3), the spin-\(j\) matrix coefficients have \(-\Delta^T\) eigenvalue \(j(j+1)\), for \(j=0,\tfrac12,1,\ldots\). To fix its normalization directly, \(T_a=-i\sigma_a/2\) gives \(-\sum_aT_a^2=\tfrac34I\) on the fundamental representation. On the spin-\(j\) representation the corresponding angular momenta satisfy \(J_3v_m=mv_m\) and \(J_\pm v_m=\sqrt{(j\mp m)(j\pm m+1)}v_{m\pm1}\); therefore \(J_3^2+(J_+J_-+J_-J_+)/2=j(j+1)I\). The matrix coefficients form the complete Peter--Weyl orthogonal decomposition. Taking their tensor products gives the complete product spectrum as sums of these eigenvalues. The free eigenvalue 0 is simple, represented by the constant 1, and the first nonzero eigenvalue on the full, not gauge-reduced, Hilbert space is \(3/4\).

Since \(W_p\in[-2,2]\), one has \(\|\mathcal V\|_\infty\leq2M\). At the all-identity configuration \(\mathcal V=2M\). Continuity and positive Haar measure of every neighborhood of that configuration give the reverse essential-supremum inequality. Thus

\[
\|\mathcal V\|_{\mathcal H\to\mathcal H}=2M.
\tag{3.1}
\]

For \(z\) on \(|z|=3/8\), the distance from \(z\) to the free spectrum is at least \(3/8\), so

\[
\|(z-H_0)^{-1}\|\leq\frac83.
\]

Factoring \(z-H_0+\xi\mathcal V\) gives a norm-convergent resolvent Neumann series whenever

\[
q:=\frac{16M}{3}|\xi|<1.
\tag{3.2}
\]

The contour projection

\[
\Pi_\xi=\frac{1}{2\pi i}\oint_{|z|=3/8}
 (z-H_0+\xi\mathcal V)^{-1}\,dz
\tag{3.3}
\]

is analytic throughout (1.11). Its rank is locally constant because it is a norm-continuous family of projections; the disk is connected, and its rank at zero is one. It therefore has rank one throughout that disk. This establishes (1.11) with the full \(2M\) potential norm and with no two-face replacement.

For real \(\xi\) in that interval, the bottom eigenvalue \(e(\xi)\) of \(H_0-\xi\mathcal V\) lies between \(-2M|\xi|\) and 0. The upper bound uses the constant trial vector and \(\int\mathcal V\,dU=0\). By the min--max principle the second eigenvalue is at least \(3/4-2M|\xi|>3/8\), whereas \(-3/8<e(\xi)\leq0\). Consequently (3.3) is the actual ground projection for every such real \(\xi\). The energy of (1.4) is exactly

\[
E_\xi=\kappa e(\xi)+2bM.
\tag{3.4}
\]

Existence of a smooth ground eigenfunction follows from compact resolvent and elliptic regularity of the compact product Laplacian with smooth bounded potential. It can be taken nonnegative: the local identity \(|\nabla|u||\leq|\nabla u|\), obtained first away from \(u=0\) and then by approximating \(|u|\) by \(\sqrt{|u|^2+\varepsilon^2}\), shows that replacing a minimizer by its modulus does not increase its form energy. The strong maximum principle for the resulting elliptic eigen-equation on this connected manifold makes that nonnegative eigenfunction strictly positive. Simplicity can also be checked directly: for a positive ground state \(\psi\), integration by parts and its eigen-equation give

\[
\langle\psi F,(H-E)\psi F\rangle
=\kappa\sum_{i,a}\int |X_{i,a}F|^2\psi^2\,dU
\tag{3.5}
\]

for smooth \(F\). Polarization and density extend this to the form domain. A second ground eigenfunction divided by \(\psi\) would make every derivative on the right vanish and hence would be constant. This also proves uniqueness of the positive normalized state used here.

### 3.2 Haar orthogonality and the first derivative

For each face \(p\), Haar integration over any one of its four distinct edges annihilates \(W_p\). Indeed, \(\int_{SU(2)}U\,dU=0\): multiplying the integration variable by the central element \(-I\) changes this integral to its negative. The same statement holds for \(U^{-1}\), and it remains true after multiplication by matrices independent of that edge. Thus \(\int W_p=0\).

For distinct elementary faces in an open box, their sets of four boundary edges differ. Choose an edge in one set absent from the other and integrate it first. This proves \(\int W_pW_q=0\) when \(p\ne q\). To justify the asserted difference of boundary sets without a geometric assumption, two adjacent perpendicular coordinate directions and the minima of the vertex coordinates are recovered from the four-edge set of an elementary square; this recovers its plane and lower corner uniquely. Finally \(\int W_p^2=1\): integrate three edges first or fix them and use Haar invariance on the fourth to reduce to \(\int_{SU(2)}(\operatorname{tr}U)^2dU\). With \(U=u_0I+i\sum_{a=1}^3u_a\sigma_a\), Haar measure is uniform on the unit sphere in \(\mathbb R^4\), so \(\int u_0^2=1/4\), and this integral is 1. We have proved

\[
\int W_pW_q\,dU=\delta_{pq},\qquad
\|\mathcal V\|_2^2=M,\qquad H_0W_p=3W_p.
\tag{3.6}
\]

The last identity uses four fundamental edge Casimirs \(3/4\), with all other edges acting trivially.

Choose the analytic ground representative \(\phi_\xi\) near zero by \(\int\phi_\xi dU=1\) and \(\phi_0=1\). This is a legitimate local analytic normalization: the resolvent bound gives

\[
\|\Pi_\xi-\Pi_0\|\leq\frac{q}{1-q},
\tag{3.7}
\]

by integrating the Neumann-series difference over a circle of length \(2\pi(3/8)\). For \(q<1/2\), \(\langle1,\Pi_\xi1\rangle\ne0\), and \(\phi_\xi=\Pi_\xi1/\langle1,\Pi_\xi1\rangle\) supplies the normalization. The spectral-projection disk (1.11) itself did not require this auxiliary choice of vector normalization on the full complex disk.

Differentiating \((H_0-\xi\mathcal V)\phi_\xi=e(\xi)\phi_\xi\) at zero and taking its Haar mean yields \(e'(0)=-\int\mathcal V=0\). The remaining equation and the normalization give

\[
H_0\phi'_0=\mathcal V,\qquad \int\phi'_0=0,
\qquad \phi'_0=\frac13\mathcal V.
\tag{3.8}
\]

These are expansions of the actual eigenvector. Their remainders hold in every fixed \(C^k\) norm, not only in \(L^2\). Here is the regularity argument. Define Sobolev norms on the compact product group by the elliptic operator \(H_0+1\). Multiplication by the fixed smooth function \(\mathcal V\) is bounded in each integer Sobolev norm, and \((H_0+1)^{-1}:H^m\to H^{m+2}\) is bounded. The equation

\[
\phi_\xi=(H_0+1)^{-1}\big[(e(\xi)+1+\xi\mathcal V)\phi_\xi\big]
\]

therefore upgrades analyticity successively from \(L^2\) to \(H^2,H^4,\ldots\). Sobolev embedding in the fixed dimension \(3N\) then gives analytic \(C^k\) representatives and bounded Taylor remainders on a sufficiently small disk. All constants may depend on \(L,k\). On the real interval, the chosen ground vector is positive by the preceding ground-state argument.

Set \(Z_\xi=\int\phi_\xi^2dU\) and \(\psi_\xi=\phi_\xi/\sqrt{Z_\xi}\), taking the square root that is positive for real \(\xi\) near zero. Because every higher Taylor coefficient of \(\phi_\xi\) has zero Haar mean, (3.6)--(3.8) give

\[
\begin{split}
\phi_\xi&=1+\frac\xi3\sum_{p\in\mathsf P_L}W_p+O_{L,k}(\xi^2),\\
Z_\xi&=1+\frac M9\xi^2+O_L(\xi^3),\\
\psi_\xi&=1+\frac\xi3\sum_{p\in\mathsf P_L}W_p+O_{L,k}(\xi^2),\\
\log\rho_\xi&=\frac{2\xi}{3}\sum_{p\in\mathsf P_L}W_p+O_{L,k}(\xi^2).
\end{split}
\tag{3.9}
\]

The \(M/9\) normalization coefficient explicitly records all the box plaquettes. Logarithms are taken of the actual positive density, which is uniformly close to 1 for sufficiently small real \(\xi\) in any fixed box.

## 4. Exact conditional projection and the surviving quantum coupling

Write \(U=(u,r)\), with \(u=U_s\), and define

\[
\rho_{R,\xi}(r)=\int_{SU(2)}\rho_\xi(u,r)\,du,
\quad p_\xi(u\mid r)=\frac{\rho_\xi(u,r)}{\rho_{R,\xi}(r)}.
\tag{4.1}
\]

Let \(Jf(u,r)=f(r)\), and let

\[
(J_\xi^*v)(r)=\int v(u,r)p_\xi(u\mid r)\,du.
\tag{4.2}
\]

Direct integration shows that \(J\) is an isometry from \(L^2(\rho_{R,\xi}dr)\) into \(L^2(\rho_\xi dU)\), and (4.2) is its adjoint. Define \(P_\xi=JJ_\xi^*\) and \(Q_\xi=I-P_\xi\). Then \(P_\xi\) is the orthogonal projection onto functions independent of \(u\), and \(\mathcal K_\xi=\operatorname{ran}Q_\xi=\ker J_\xi^*\).

Conjugating by the true vacuum gives the nonnegative operator

\[
\mathscr L_\xi=\psi_\xi^{-1}(H_{\kappa,b}-E_\xi)\psi_\xi
=-\kappa\sum_{i\in\mathsf E_L,a}
 \big[X_{i,a}^2+(X_{i,a}\log\rho_\xi)X_{i,a}\big],
\tag{4.3}
\]

with closed form

\[
q_\xi(v,w)=\kappa\sum_{i,a}\int
 \overline{X_{i,a}v}\,X_{i,a}w\,\rho_\xi dU,
\quad D(q_\xi)=H^1(SU(2)^{\mathsf E_L}).
\tag{4.4}
\]

The form domain equality follows because \(\rho_\xi\) is smooth, strictly positive, and bounded above and below on the finite compact configuration manifold. Formula (4.3) is obtained by the Leibniz rule, cancellation of the ground-state eigen-equation, and \(2X\log\psi=X\log\rho\); it retains the exact kinetic coefficient \(\kappa\).

For a retained smooth \(f\), the \(s\) derivatives vanish. Differentiating (4.1) under its finite compact integral gives

\[
X_{i,a}\log\rho_{R,\xi}
=\int (X_{i,a}\log\rho_\xi)p_\xi\,du
\quad(i\in R).
\]

It follows from (4.3) that the exact eliminated coupling is

\[
\begin{split}
B_\xi f&:=Q_\xi\mathscr L_\xi Jf
 =-\kappa\sum_{i\in R,a}\sigma_{i,a,\xi}X_{i,a}f,\\
\sigma_{i,a,\xi}&=X_{i,a}\log\rho_\xi-X_{i,a}\log\rho_{R,\xi},
\qquad J_\xi^*\sigma_{i,a,\xi}=0.
\end{split}
\tag{4.5}
\]

In particular second derivatives of \(f\) cancel exactly; no second-order term has been discarded in (4.5).

If \(p\in\mathsf I(s)\), integration over \(u\) kills \(W_p\), and also kills each \(X_{i,a}W_p\), \(i\in R\), since that derivative commutes with integration over \(u\). If \(p\notin\mathsf I(s)\), \(W_p\) is independent of \(u\). Consequently (3.9) gives, with \(C^k\) remainders,

\[
\begin{split}
\log\rho_{R,\xi}
 &=\frac{2\xi}{3}\sum_{p\notin\mathsf I(s)}W_p+O_{L,k}(\xi^2),\\
\sigma_{i,a,\xi}
 &=\frac{2\xi}{3}\sum_{p\in\mathsf I(s)}X_{i,a}W_p
   +O_{L,k}(\xi^2).
\end{split}
\tag{4.6}
\]

Since \(Xf_\xi=XW_Q\), its only nonzero derivatives belong to edges of \(Q\). Combining (2.2), (4.5), and (4.6) therefore leaves exactly one face-edge pair:

\[
B_\xi f_\xi=-\frac{2b}{3}G+O_{L,k}\!\left(\frac{b^2}{\kappa}\right),
\qquad G=\sum_{a=1}^3(X_{e,a}W_P)(X_{e,a}W_Q).
\tag{4.7}
\]

Every other face in the Hamiltonian contributed to (3.9) and (4.6); it disappears from the displayed first derivative only by the proved conditional cancellation or the proved edge-disjointness. Higher orders still contain the full interacting box.

## 5. Exact Fierz contraction, Haar norms, and free electric modes

Under \(U_e\mapsto e^{tT_a}U_e\), (2.4) yields

\[
X_{e,a}W_P=\operatorname{tr}(T_aP_*),\qquad
X_{e,a}W_Q=-\operatorname{tr}(T_aQ'_*).
\tag{5.1}
\]

The Pauli completeness identity

\[
\sum_a(\sigma_a)_{ij}(\sigma_a)_{kl}
=2\delta_{il}\delta_{jk}-\delta_{ij}\delta_{kl}
\]

gives, by multiplying by matrix entries and summing indices,

\[
\sum_a\operatorname{tr}(T_aC)\operatorname{tr}(T_aD)
=-\frac12\operatorname{tr}(CD)+\frac14\operatorname{tr}C\operatorname{tr}D.
\tag{5.2}
\]

Define functions on the **full** configuration space by

\[
R_0=\operatorname{tr}(AB),\qquad D_0=W_PW_Q,
\qquad D_1=D_0-\frac12R_0.
\tag{5.3}
\]

Since \(\operatorname{tr}(P_*Q'_*)=\operatorname{tr}(U_eABU_e^{-1})=R_0\), equations (5.1)--(5.2) give

\[
G=\frac12R_0-\frac14D_0
=\frac38R_0-\frac14D_1.
\tag{5.4}
\]

These functions are gauge invariant: \(W_P,W_Q\) are traces of closed holonomies, and \(AB\) is the closed six-edge outer loop after cancellation of the common edge. They have zero Haar conditional mean over \(s\). In fact \(R_0\) contains \(U_s^{-1}\) once, \(D_0\) contains it once in \(W_P\), and \(W_Q\) is independent of it; the Haar annihilation used in Section 3 proves each assertion.

For their norms, condition on \(U_e\). The disjoint outer-link products \(A,B\) are independent Haar-distributed matrices: for any fixed values of the other factors, a product containing a single Haar factor or its inverse is Haar by left/right invariance. Thus \(P_*=U_eA\) and \(Q'_*=BU_e^{-1}\) are independent Haar matrices even conditionally on \(U_e\). Write

\[
P_*=p_0I+i\sum_ap_a\sigma_a,\qquad
Q'_*=q_0I+i\sum_aq_a\sigma_a.
\]

The vectors \(p,q\) are independent uniform unit vectors in \(\mathbb R^4\). Their second moments are \(\mathbb E[p_\alpha p_\beta]=\delta_{\alpha\beta}/4\), and likewise for \(q\): off-diagonal moments vanish by sign symmetries, diagonal moments agree by rotational symmetry, and their sum is 1. Matrix multiplication and (5.1) now give

\[
G=-\sum_{a=1}^3p_aq_a,\quad
R_0=2\left(p_0q_0-\sum_{a=1}^3p_aq_a\right),\quad
D_1=3p_0q_0+\sum_{a=1}^3p_aq_a.
\tag{5.5}
\]

Set \(x=p_0q_0\), \(y=\sum_{a=1}^3p_aq_a\). The moments just proved give \(\mathbb E x^2=1/16\), \(\mathbb E y^2=3/16\), and \(\mathbb E xy=0\). Hence

\[
\|R_0\|_0^2=1,\quad \|D_1\|_0^2=\frac34,
\quad\langle R_0,D_1\rangle_0=0,
\quad\|G\|_0^2=\frac3{16}.
\tag{5.6}
\]

The subscript 0 denotes Haar inner product on the entire box. All additional link integrals are integrals of 1, so (5.6) contains no omitted factor depending on the number of additional links.

On any of the six outer links, \(R_0,D_0,D_1\) are linear combinations of fundamental matrix entries or inverse fundamental matrix entries. Each consequently has eigenvalue \(-3/4\) for that link Laplacian. On \(e\), \(R_0\) is independent of \(U_e\). The product rule, (5.4), and the fundamental plaquette Casimirs give

\[
\begin{split}
\Delta_e^T D_0
&=-\frac32D_0+2G
=R_0-2D_0=-2D_1,\\
\Delta_e^T R_0&=0,\qquad \Delta_e^T D_1=-2D_1.
\end{split}
\tag{5.7}
\]

On every link outside these seven, both \(R_0\) and \(D_1\) are constant. Such a link is in spin zero, with Casimir zero. Summing over **all** \(N\) links therefore gives the exact full-box identities

\[
H_0R_0=\frac92R_0,\qquad H_0D_1=\frac{13}{2}D_1.
\tag{5.8}
\]

Combining (4.7) and (5.4) yields

\[
B_\xi f_\xi=b\left(-\frac14R_0+\frac16D_1\right)
 +O_{L,k}(\kappa\xi^2).
\tag{5.9}
\]

As \(\rho_\xi=1+O_L(\xi)\), (5.6) proves

\[
\begin{split}
\|B_\xi f_\xi\|_\xi^2
&=b^2\left(\frac1{16}+\frac1{36}\frac34\right)
 +O_L(\kappa^2\xi^3)\\
&=\frac{b^2}{12}+O_L\!\left(\frac{b^3}{\kappa}\right).
\end{split}
\tag{5.10}
\]

In particular the positive leading coefficient is independent of the fixed box size, although the remainder is not.

## 6. The exact retained form and its first vacuum moments

For the centered \(f_\xi\), put

\[
m_\xi=\int W_Q\rho_\xi dU,\quad
r_\xi=\int W_Q^2\rho_\xi dU,\quad
d_\xi=\|Jf_\xi\|_\xi^2=r_\xi-m_\xi^2,
\]

and

\[
a_\xi=q_\xi(Jf_\xi,Jf_\xi)
=\kappa\sum_{i\in\partial Q,a}\int
 |X_{i,a}W_Q|^2\rho_\xi dU.
\tag{6.1}
\]

For any used edge of a simple \(SU(2)\) loop, its derivative is, up to an orientation sign, \(\operatorname{tr}(T_aC)\), with \(C\) a based version of its holonomy. Writing \(C=c_0I+i\sum_ac_a\sigma_a\) gives \(\operatorname{tr}(T_aC)=c_a\), so

\[
\sum_a|X_{i,a}W_Q|^2=\sum_ac_a^2
=1-\frac14W_Q^2.
\]

The four edges of \(Q\) give the exact identities

\[
a_\xi=\kappa(4-r_\xi),\qquad
\mathcal R_{\mathrm{ret}}(\xi)=\frac{a_\xi}{d_\xi}
=\kappa\frac{4-r_\xi}{r_\xi-m_\xi^2}.
\tag{6.2}
\]

The true vacuum is present in both moments. Equations (3.6) and (3.9) give \(m_\xi=2\xi/3+O_L(\xi^2)\). They also give \(r_\xi=1+O_L(\xi^2)\). For the latter claim, the linear term is \(\tfrac23\sum_p\int W_Q^2W_p\). If \(p\ne Q\), an edge of \(p\) outside \(Q\) annihilates the integral; if \(p=Q\), multiplying any one \(Q\)-edge by \(-I\) changes \(W_Q^3\) to its negative. Thus every summand is zero. Consequently

\[
d_\xi=1+O_L(\xi^2),\qquad
a_\xi=3\kappa+O_L(\kappa\xi^2),\qquad
\mathcal R_{\mathrm{ret}}(\xi)=3\kappa+O_L(\kappa\xi^2).
\tag{6.3}
\]

Strict positivity of \(d_\xi\) follows directly as well: the density has full support and the continuous nonconstant function \(W_Q\) cannot have zero variance.

## 7. Eliminated form domain and a genuine improved quantum vector

The definition of the eliminated operator does not assume that a formal product \(Q_\xi\mathscr L_\xi Q_\xi\) has any particular operator domain. First note that \(P_\xi,Q_\xi\) preserve \(H^1\). For \(i\in R\), differentiating (4.2) yields

\[
X_{i,a}J_\xi^*v
=J_\xi^*(X_{i,a}v)+J_\xi^*(\sigma_{i,a,\xi}v).
\tag{7.1}
\]

Conditional Cauchy--Schwarz bounds each right-hand term in \(L^2(\rho_{R,\xi})\) by the corresponding full \(L^2(\rho_\xi)\) norm, with the bounded score coefficient on the second term. The \(s\) derivative of \(P_\xi v\) is zero. This proves the \(H^1\) assertion. It also shows that \(P_\xi,Q_\xi\) preserve smooth functions. Smooth functions are dense in \(H^1\); applying \(Q_\xi\) to smooth approximants proves that

\[
\mathcal D_\xi=H^1\cap\mathcal K_\xi
\]

is dense in \(\mathcal K_\xi\), and is the form closure of its smooth elements. It is closed for the \(H^1\) norm because \(\mathcal K_\xi\) is closed in the weighted \(L^2\) norm. Thus \(q_\xi|_{\mathcal D_\xi}\) is a densely defined closed nonnegative form. Define \(C_\xi\) to be its self-adjoint operator by the explicit representation condition

\[
\begin{split}
D(C_\xi)=\{w\in\mathcal D_\xi: &\text{there is }h\in\mathcal K_\xi
\text{ with }q_\xi(v,w)=\langle v,h\rangle_\xi\text{ for all }v\in\mathcal D_\xi\},\\
C_\xi w&=h.
\end{split}
\tag{7.2}
\]

Put \(g_\xi=B_\xi f_\xi\in\mathcal K_\xi\), and define

\[
w_\xi=(C_\xi+\kappa)^{-1}g_\xi,
\qquad u_\xi=\psi_\xi(Jf_\xi-w_\xi).
\tag{7.3}
\]

Existence and uniqueness of \(w_\xi\) follow already by applying the coercive-form representation to \(q_\xi+\kappa\langle\cdot,\cdot\rangle_\xi\) on \(\mathcal D_\xi\). In particular \(w_\xi\in\mathcal D_\xi\). Since multiplication by the smooth positive \(\psi_\xi\) maps \(H^1\) to itself, \(u_\xi\) belongs to the full quadratic-form domain of \(H_{\kappa,b}\).

Moreover, \(\langle1,w_\xi\rangle_\xi=0\), since the constant belongs to the retained range. Centering (1.8) therefore proves \(\langle\psi_\xi,u_\xi\rangle=0\). The denominator \(d_\xi+\|w_\xi\|_\xi^2\) is positive, so the physical vector is nonzero.

All operators and this vector respect the Gauss constraint. In the convention \(U_e\mapsto g_{s(e)}U_eg_{t(e)}^{-1}\), Wilson traces, Haar measure, and the product kinetic energy are invariant. Uniqueness of the positive normalized vacuum makes \(\psi_\xi\) invariant. In (4.2), changing the eliminated variable by the corresponding left/right multiplications proves that conditional expectation intertwines the induced action on retained variables. Thus \(J,P_\xi,Q_\xi\), the closed forms, and their uniquely defined resolvents intertwine gauge transformations; \(f_\xi,g_\xi,w_\xi,u_\xi\) are invariant. The original convention \(U_e\mapsto h_{s(e)}^{-1}U_eh_{t(e)}\) is the same action with \(g_v=h_v^{-1}\) at every vertex. No gauge convention or coefficient is changed.

Set

\[
I_\xi=\langle g_\xi,w_\xi\rangle_\xi,
\qquad J_\xi^{\mathrm{num}}=\|w_\xi\|_\xi^2.
\tag{7.4}
\]

The superscript distinguishes this scalar from the lift \(J\). Testing the weak resolvent equation with \(w_\xi\) shows

\[
I_\xi=q_\xi(w_\xi,w_\xi)+\kappa J_\xi^{\mathrm{num}}\geq0.
\tag{7.5}
\]

For smooth \(Jf_\xi\), integration by parts against \(w_\xi\in H^1\), followed by (4.5) and \(P_\xi w_\xi=0\), gives \(q_\xi(Jf_\xi,w_\xi)=\langle g_\xi,w_\xi\rangle_\xi=I_\xi\). Orthogonality of the retained and eliminated ranges and (3.5) now give the **exact** corrected quotient

\[
\mathcal R_{\mathrm{corr}}(\xi)
:=\frac{\|(H_{\kappa,b}-E_\xi)^{1/2}u_\xi\|^2}{\|u_\xi\|^2}
=\frac{a_\xi-I_\xi-\kappa J_\xi^{\mathrm{num}}}{d_\xi+J_\xi^{\mathrm{num}}}.
\tag{7.6}
\]

Only form-domain membership is needed; an unproved operator-domain assertion about \(u_\xi\) is not used. Subtracting (7.6) from (6.2) gives

\[
\mathcal R_{\mathrm{ret}}-\mathcal R_{\mathrm{corr}}
=\frac{I_\xi+(\kappa+\mathcal R_{\mathrm{ret}})J_\xi^{\mathrm{num}}}
 {d_\xi+J_\xi^{\mathrm{num}}}.
\tag{7.7}
\]

If \(g_\xi\ne0\), then \(w_\xi\ne0\), and (7.5) gives \(I_\xi>0\). Since the retained form is nonnegative, (7.7) is then strictly positive. This is a correction of an actual excitation estimate in the full interacting Hilbert space, not the energy of a separately postulated marginal dynamics.

## 8. Resolvent expansion with the moving conditional kernel controlled

It remains to prove that the free modes (5.8) really determine the displayed second-order coefficient despite the changing density and the changing eliminated subspace. We work on a fixed Sobolev space and prove that step explicitly.

At \(\xi=0\), conditional expectation is ordinary Haar integration over \(s\), denoted \(P_0\). Integration commutes with every retained derivative and annihilates the integral of every \(s\) derivative by Haar invariance. Thus \(P_0\) commutes with \(H_0\) on smooth functions and, by the spectral or closed-form extension, on its natural domains. From (5.3) and Haar annihilation, \(R_0,D_1\in\mathcal K_0\). Equations (5.8) are therefore also the eigenvalue equations for \(C_0=\kappa H_0|_{\mathcal K_0}\).

Regard functions and projections for small real \(\xi\) on the same underlying unweighted \(L^2(dU)\) and \(H^1\) spaces. Equation (3.9) gives \(\rho_\xi=1+O_{L,1}(\xi)\), \(\rho_{R,\xi}=1+O_{L,1}(\xi)\), and \(p_\xi(u\mid r)=1+O_{L,1}(\xi)\). The integral formula (4.2) and Cauchy--Schwarz imply

\[
\|P_\xi-P_0\|_{L^2\to L^2}=O_L(|\xi|),\qquad
\|P_\xi-P_0\|_{H^1\to H^1}=O_L(|\xi|).
\tag{8.1}
\]

For the second bound, differentiate the kernel formula: its derivative is the integral of the differentiated input against \(p_\xi-1\), plus the input against a derivative of \(p_\xi\); both kernels have the stated \(O_L(|\xi|)\) supremum bound. Derivatives in the eliminated variable of the output are zero. This proves the bound in all first-derivative directions.

All \(P_\xi\) have exactly the same range, namely functions independent of \(s\), and act as the identity on that range. As operators on the common function space this gives

\[
P_\xi P_0=P_0,\quad P_0P_\xi=P_\xi,
\quad Q_0Q_\xi=Q_0,\quad Q_\xi Q_0=Q_\xi.
\tag{8.2}
\]

In particular

\[
T_\xi:=Q_\xi|_{\mathcal K_0}:\mathcal K_0\longrightarrow\mathcal K_\xi
\]

is a bounded bijection with inverse \(Q_0|_{\mathcal K_\xi}\). The same holds between the form spaces \(\mathcal D_0\) and \(\mathcal D_\xi\), and \(T_\xi-I=O_L(|\xi|)\) as a map from \(\mathcal D_0\) into \(H^1\), by (8.1).

On the fixed Hilbert form space \(\mathcal D_0=H^1\cap\mathcal K_0\), pull back the dimensionless resolvent form:

\[
\mathfrak a_\xi(v,h)
=\kappa^{-1}q_\xi(T_\xi v,T_\xi h)
 +\langle T_\xi v,T_\xi h\rangle_\xi.
\tag{8.3}
\]

Choose the explicit equivalent first-order Sobolev norm

\[
\|v\|_{H^1}^2=\|v\|_0^2+\sum_{i,a}\|X_{i,a}v\|_0^2.
\]

Then \(\mathfrak a_0(v,v)=\|v\|_{H^1}^2\). Density boundedness, (8.1), and Cauchy--Schwarz give

\[
|\mathfrak a_\xi(v,h)-\mathfrak a_0(v,h)|
\leq C_L|\xi|\|v\|_{H^1}\|h\|_{H^1}.
\tag{8.4}
\]

For sufficiently small \(|\xi|\), this also yields \(\mathfrak a_\xi(v,v)\geq\tfrac12\|v\|_{H^1}^2\). No estimate is required uniformly in \(L\).

Write

\[
g_1=-\frac14R_0+\frac16D_1,
\qquad g_\xi=\kappa\xi g_1+O_L(\kappa\xi^2)
\quad\hbox{in }L^2.
\tag{8.5}
\]

If \(h_\xi=T_\xi^{-1}w_\xi\), its exact weak equation is

\[
\mathfrak a_\xi(v,h_\xi)
=\kappa^{-1}\langle T_\xi v,g_\xi\rangle_\xi
=\xi\langle v,g_1\rangle_0
 +O_L(\xi^2)\|v\|_{H^1}.
\tag{8.6}
\]

The last remainder follows from (8.1), (8.5), and \(\rho_\xi-1=O_L(\xi)\). By (5.8), the unique vector satisfying \(\mathfrak a_0(v,h_1)=\langle v,g_1\rangle_0\) is

\[
h_1=(H_0+1)^{-1}g_1
=-\frac1{22}R_0+\frac1{45}D_1.
\tag{8.7}
\]

Subtract \(\xi\mathfrak a_\xi(v,h_1)\) from (8.6) and use (8.4). The resulting functional is \(O_L(\xi^2)\|v\|_{H^1}\). Test it with \(v=h_\xi-\xi h_1\); coercivity gives

\[
\|h_\xi-\xi h_1\|_{H^1}=O_L(\xi^2).
\]

Finally \(T_\xi h_1=h_1+O_L(\xi)\) in \(H^1\). We have proved the genuine moving-domain resolvent expansion

\[
\boxed{w_\xi=\xi\left(-\frac1{22}R_0+\frac1{45}D_1\right)
 +O_L(\xi^2)\quad\hbox{in }H^1.}
\tag{8.8}
\]

This argument uses no unverified derivative of an operator with changing domain and no finite-mode approximation to the interacting vacuum. The two modes suffice for the leading coefficient because the exact forcing has the leading term (8.5) and their free eigenvalues are known; every other box mode remains in the exact resolvent and in its proved remainder.

## 9. The exact second-order coefficient and its meaning

Equations (5.6), (8.5), (8.8), and \(\rho_\xi=1+O_L(\xi)\) give

\[
\begin{split}
I_\xi
&=\kappa\xi^2\left(\frac1{88}+\frac1{360}\right)
 +O_L(\kappa\xi^3)
=\frac7{495}\frac{b^2}{\kappa}
 +O_L\!\left(\frac{b^3}{\kappa^2}\right),\\
J_\xi^{\mathrm{num}}
&=\xi^2\left(\frac1{484}+\frac1{2700}\right)+O_L(\xi^3)
=\frac{199}{81675}\frac{b^2}{\kappa^2}
 +O_L\!\left(\frac{b^3}{\kappa^3}\right).
\end{split}
\tag{9.1}
\]

For example, the \(D_1\) contribution to \(I_\xi/(\kappa\xi^2)\) is \(\tfrac16\cdot\tfrac1{45}\cdot\tfrac34=1/360\); its contribution to \(J_\xi^{\mathrm{num}}/\xi^2\) is \(\tfrac1{45^2}\cdot\tfrac34=1/2700\). Thus the multiplicity and normalization of this second mode have not been suppressed.

Substituting (6.3) and (9.1) into the exact quotient difference (7.7), and using \(d_\xi+J_\xi^{\mathrm{num}}=1+O_L(\xi^2)\), yields

\[
\begin{split}
\mathcal R_{\mathrm{ret}}-\mathcal R_{\mathrm{corr}}
&=\kappa\xi^2\left(\frac7{495}+4\frac{199}{81675}\right)
 +O_L(\kappa\xi^3)\\
&=\frac{1951}{81675}\frac{b^2}{\kappa}
 +O_L\!\left(\frac{b^3}{\kappa^2}\right).
\end{split}
\tag{9.2}
\]

This proves (1.10). Together with (5.10) and (7.7), it proves the actual strict improvement for every sufficiently small positive \(\xi\) in each fixed full box. More explicitly, the proved remainder in (5.10) has an upper bound \(C_L\kappa^2\xi^3\) on some interval. Restricting that interval so \(C_L\xi<1/24\) gives \(\|g_\xi\|_\xi^2\geq\kappa^2\xi^2/24>0\). This deduction requires no sign assumption about any unknown higher coefficient.

In the original physical parameters (1.6), the leading difference is

\[
\frac{1951}{653400}\frac{1}{g_{\mathrm{YM}}^6a},
\qquad O_L\!\left(\frac{1}{g_{\mathrm{YM}}^{10}a}\right)
\tag{9.3}
\]

for the remainder. The exact Wilson constant shift is \(2bM=M/(g_{\mathrm{YM}}^2a)\). It contributes to \(E_\xi\) in (3.4) and cancels from the excitation operator \(H-E_\xi\), not from the Hamiltonian definition by omission.

The parameter conversion of the remainder scale, including its fixed numerical factor, is \(b^3/\kappa^2=1/(32g_{\mathrm{YM}}^{10}a)\); the corresponding leading scale is \(b^2/\kappa=1/(8g_{\mathrm{YM}}^6a)\).

The correction is an upper-bound improvement for the finite-box physical excitation gap: the spectral theorem and vacuum orthogonality give \(\operatorname{gap}(H|_{\mathrm{Gauss}})\leq\mathcal R_{\mathrm{corr}}<\mathcal R_{\mathrm{ret}}\) on the stated small-coupling interval. The retained quotient approaches \(3\kappa\), not zero, as \(\xi\to0\) at fixed \(\kappa\). A positive improvement of that quotient does not assert a vanishing gap. The explicit Neumann disk shrinks as \(M^{-1}\), and no other bound here removes that volume dependence. Thus the calculation establishes a genuinely full, finite, interacting three-dimensional spatial-lattice excitation correction without asserting a four-dimensional continuum mass-gap conclusion.

## 10. Provenance and exact checker

This extension supplies the full-box incidence, the all-plaquette vacuum expansion and norm/radius, and the controlled passage to the two leading free modes. The corresponding two-face calculation is in `../adjacent_plaquette_quantum_correction.md`; the general infinite-rank conditional-form construction is in `spatial_vacuum_elimination.tex`. All specific form-domain and coefficient arguments needed for this extension are reproduced above. The Schur/projection correction is not claimed as a new general method; primary-source attribution for that method is given in the companion proof (including Dusson--Sigal--Stamm, *The Feshbach--Schur map and perturbation theory*, arXiv:2105.02058v1, DOI `10.4171/ECR/18-1/5`). No new remote source retrieval was used for this bounded extension.

`check_bulk_plaquette_incidence.py` enumerates the entire open cubical graph and every face for \(L=2,3,4,5\). It checks the counts (1.2), face-edge containment, oriented occurrences of \(e,s\), the complete four-face star, the unique surviving pair (2.2), injectivity of elementary-face edge supports, and the exact rational Neumann-bound identity. Using rational arithmetic only, it checks the two free eigenvalues, \(1/12\), \(7/495\), \(199/81675\), \(1951/81675\), and the physical factor \(1951/653400\). These finite checks diagnose incidence and algebra; the continuum-free analytic and operator-domain proofs are Sections 3--9, not inferred from numerical computation.

```

## Complete source: wilson_variation/check_bulk_plaquette_incidence.py

```python
"""Exact full-open-box incidence and rational-coefficient diagnostics.

This enumerates the entire finite graph, not a two-face truncation.  It does
not approximate the vacuum, perform a continuum calculation, or use floating
point arithmetic.  The analytic argument is in BULK_PLAQUETTE_EXTENSION.md.
"""

from fractions import Fraction as F
from itertools import combinations, product


def shifted(vertex, axis):
    result = list(vertex)
    result[axis] += 1
    return tuple(result)


def oriented_boundary(face):
    vertex, (i, j) = face
    return (
        ((vertex, i), 1),
        ((shifted(vertex, i), j), 1),
        ((shifted(vertex, j), i), -1),
        ((vertex, j), -1),
    )


def edge_set(face):
    return {edge for edge, sign in oriented_boundary(face)}


q_face = ((0, 0, 0), (0, 1))
p_face = ((-1, 0, 0), (0, 1))
s_edge = ((-1, 0, 0), 1)
e_edge = ((0, 0, 0), 1)
expected_incident = {
    p_face,
    ((-2, 0, 0), (0, 1)),
    ((-1, 0, 0), (1, 2)),
    ((-1, 0, -1), (1, 2)),
}

assert dict(oriented_boundary(p_face))[e_edge] == 1
assert dict(oriented_boundary(q_face))[e_edge] == -1
assert dict(oriented_boundary(p_face))[s_edge] == -1
assert edge_set(p_face) & edge_set(q_face) == {e_edge}
assert len(edge_set(p_face) | edge_set(q_face)) == 7
assert len((edge_set(p_face) | edge_set(q_face)) - {e_edge}) == 6
assert s_edge not in edge_set(q_face)

box_results = []
for half_side in (2, 3, 4, 5):
    vertices = set(product(range(-half_side, half_side + 1), repeat=3))
    edges = {
        (vertex, axis)
        for vertex in vertices
        for axis in range(3)
        if vertex[axis] < half_side
    }
    faces = {
        (vertex, axes)
        for vertex in vertices
        for axes in combinations(range(3), 2)
        if all(vertex[axis] < half_side for axis in axes)
    }
    edge_count = 3 * (2 * half_side) * (2 * half_side + 1) ** 2
    face_count = 3 * (2 * half_side) ** 2 * (2 * half_side + 1)
    assert len(edges) == edge_count
    assert len(faces) == face_count
    assert all(edge_set(face) <= edges for face in faces)
    assert p_face in faces and q_face in faces

    incident = {face for face in faces if s_edge in edge_set(face)}
    assert incident == expected_incident
    intersections = {face: edge_set(face) & edge_set(q_face) for face in incident}
    assert intersections[p_face] == {e_edge}
    assert all(not common for face, common in intersections.items() if face != p_face)
    surviving_pairs = {
        (face, edge)
        for face in incident
        for edge in edge_set(face) & edge_set(q_face)
    }
    assert surviving_pairs == {(p_face, e_edge)}

    # Distinct elementary faces have an edge absent from the other face.
    # This is the incidence input to Haar orthogonality, checked without
    # quadratic pair enumeration by injectivity of the four-edge supports.
    assert len({frozenset(edge_set(face)) for face in faces}) == face_count

    # At the strict Neumann-radius boundary the norm bound is exactly one.
    radius = F(3, 16 * face_count)
    assert F(8, 3) * (2 * face_count) * radius == 1
    assert 2 * face_count * radius == F(3, 8)
    box_results.append((half_side, edge_count, face_count, radius))

# Haar mode norms and the actual dimensionless free electric eigenvalues.
norm_r = F(1)
norm_d = F(3, 4)
lambda_r = 6 * F(3, 4)
lambda_d = 6 * F(3, 4) + 2
assert lambda_r == F(9, 2)
assert lambda_d == F(13, 2)

g_r, g_d = -F(1, 4), F(1, 6)
h_r = g_r / (lambda_r + 1)
h_d = g_d / (lambda_d + 1)
assert h_r == -F(1, 22)
assert h_d == F(1, 45)
norm_g = g_r**2 * norm_r + g_d**2 * norm_d
i_coefficient = g_r * h_r * norm_r + g_d * h_d * norm_d
j_coefficient = h_r**2 * norm_r + h_d**2 * norm_d
improvement = i_coefficient + 4 * j_coefficient
assert norm_g == F(1, 12)
assert i_coefficient == F(7, 495)
assert j_coefficient == F(199, 81675)
assert improvement == F(1951, 81675)
assert improvement / 8 == F(1951, 653400)

for half_side, edges, faces, radius in box_results:
    print(f"L={half_side}: all {edges} links and {faces} faces; "
          f"unique surviving pair (P,e); Neumann radius {radius}")
print("PASS: exact orientation, whole-box incidence, Haar-support injectivity, "
      "free electric energies, and all correction coefficients.")

```

