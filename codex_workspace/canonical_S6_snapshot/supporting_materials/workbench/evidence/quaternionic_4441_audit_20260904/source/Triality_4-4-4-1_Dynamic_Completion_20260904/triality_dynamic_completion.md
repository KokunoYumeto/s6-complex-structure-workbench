# The 4+4+4+1 triality completion and the unlocked S8

## 1. The literal 13-dimensional object

The first exact realization of

\[
4+4+4+1
\]

is the equal-diagonal slice of the quaternionic rank-three Hermitian Jordan algebra:

\[
\mathcal T_{13}
=\left\{
\begin{pmatrix}
\lambda&q_3&\bar q_2\\
\bar q_3&\lambda&q_1\\
q_2&\bar q_1&\lambda
\end{pmatrix}:
\lambda\in\mathbb R,\ q_i\in\mathbb H
\right\}
\cong\mathbb R\oplus\mathbb H^3.
\]

Its Moore determinant is

\[
\boxed{
\mathcal N_{13}
=\lambda^3-\lambda(|q_1|^2+|q_2|^2+|q_3|^2)
+2\operatorname{Re}(q_1q_2q_3).}
\]

The three quaternionic summands are not a direct sum of uncoupled copies. They are the three oriented edges of a triangle. Under

\[
(s_1,s_2,s_3):
\begin{cases}
q_1\mapsto s_2q_1s_3^{-1},\\
q_2\mapsto s_3q_2s_1^{-1},\\
q_3\mapsto s_1q_3s_2^{-1},
\end{cases}
\qquad s_i\in\operatorname{Sp}(1),
\]

the loop product transforms by conjugation and its real part is invariant. The effective compact group is

\[
\operatorname{Sp}(1)^3/\{\pm(1,1,1)\},
\]

with a cyclic permutation of the three edges.

The positive-semidefinite region is exactly

\[
\lambda\ge0,
\qquad |q_i|^2\le\lambda^2,
\qquad \mathcal N_{13}\ge0.
\]

Its one-point compactification is a closed 13-ball, and the compactified determinant boundary is

\[
\boxed{S^{12}.}
\]

More generally, equal-diagonal rank-three slices over the normed division algebras give

\[
\begin{array}{c|c|c}
\mathbb A&\dim_{\mathbb R}(\mathbb R\oplus\mathbb A^3)&
(\partial\mathcal C(\mathbb A))^+\\ \hline
\mathbb R&4&S^3\\
\mathbb C&7&S^6\\
\mathbb H&13&S^{12}\\
\mathbb O&25&S^{24}.
\end{array}
\]

This explains the recurring dimensions by one rank-three construction. It does not identify the complex equal-diagonal S6 with a separately constructed torus-fibred complex threefold.

## 2. Why 13 dimensions do not close dynamically

The 13-dimensional equal-diagonal slice is not a Jordan subalgebra. Squaring the three edge generators gives

\[
\operatorname{diag}(0,1,1),\qquad
\operatorname{diag}(1,0,1),\qquad
\operatorname{diag}(1,1,0),
\]

and their linear combinations generate the three independent diagonal units. Thus the Jordan closure is

\[
\boxed{\operatorname{Herm}_3(\mathbb H),\qquad \dim_{\mathbb R}=15.}
\]

Write the diagonal entries as

\[
a_i=\lambda+\eta_i,
\qquad \eta_1+\eta_2+\eta_3=0.
\]

Then

\[
\begin{aligned}
\det_{\mathbb H}Q
={}&\mathcal N_{13}
-\frac\lambda2(\eta_1^2+\eta_2^2+\eta_3^2)
+\eta_1\eta_2\eta_3\\
&-(\eta_1|q_1|^2+\eta_2|q_2|^2+\eta_3|q_3|^2).
\end{aligned}
\]

At the equal-diagonal locus,

\[
D_\eta\det[\delta\eta]
=-\sum_i|q_i|^2\delta\eta_i.
\]

The normal force vanishes for every trace-free diagonal variation exactly when

\[
|q_1|=|q_2|=|q_3|.
\]

Therefore the two missing real diagonal anisotropies are generated dynamically by unequal occupation of the three four-dimensional sectors.

The dimensions have distinct meanings:

- **13:** triality-symmetric ansatz \(\mathbb R\oplus\mathbb H^3\);
- **14:** fixed-trace shape body, or equivalently the trace-free linear carrier \(\operatorname{Herm}_3^0(\mathbb H)\);
- **15:** the unconstrained Jordan-closed algebra \(\operatorname{Herm}_3(\mathbb H)\).

## 3. The exact SU(3) enlargement of the old nine-dimensional object

Fix \(\mathbb C_i\subset\mathbb H\). There is an exact real-linear decomposition

\[
\boxed{
\operatorname{Herm}_3(\mathbb H)
\cong
\operatorname{Herm}_3(\mathbb C_i)\oplus\mathbb C_i^3.}
\]

For \(A\in\operatorname{Herm}_3(\mathbb C_i)\) and \(b\in\mathbb C_i^3\), define

\[
B(b)=
\begin{pmatrix}
0&\bar b_3&-\bar b_2\\
-\bar b_3&0&\bar b_1\\
\bar b_2&-\bar b_1&0
\end{pmatrix},
\qquad
\Theta(A,b)=A+B(b)j.
\]

Then

\[
\boxed{
\det_{\mathbb H}\Theta(A,b)=\det_{\mathbb C}A-b^*Ab.}
\]

The action is

\[
(A,b)\longmapsto(UAU^*,Ub),
\qquad U\in SU(3).
\]

Taking traces gives

\[
\operatorname{Herm}_3^0(\mathbb H)
\cong
\operatorname{Herm}_3^0(\mathbb C_i)\oplus\mathbb C_i^3
\cong\mathbb R^8\oplus\mathbb R^6.
\]

Hence the old carrier has the exact equivariant inclusion

\[
\boxed{S^8\hookrightarrow S^{14}.}
\]

This is also an inclusion of Gram boundaries. For \(\mathbb A=\mathbb C_i,\mathbb H\), the spectral-floor map

\[
K\longmapsto K-\lambda_{\min}(K)I_3
\]

is an equivariant homeomorphism from \(\operatorname{Herm}_3^0(\mathbb A)\) to the singular positive cone. The complex/quaternionic inclusion commutes with these maps.

Full color forces the extra six real coordinates. The standard complex triplet is irreducible as a real SU(3) representation. Therefore no 13-dimensional **linear SU(3)-invariant** completion can contain the full old 9-dimensional object and a nonzero quaternionic direction. The minimal dimensions are:

\[
9+6=15,
\qquad
8+6=14\quad\text{after fixing trace}.
\]

## 4. The old CP2 opens into HP2

The complex rank-one projectors form \(\mathbb{CP}^2\). In the quaternionic completion they form \(\mathbb{HP}^2\).

Represent a quaternionic line by a unit vector

\[
v=z+w j,
\qquad z,w\in\mathbb C^3,
\qquad \|z\|^2+\|w\|^2=1,
\]

and put \(Z=(z\ w)\). Then

\[
\delta([v])=4\det(Z^*Z)\in[0,1]
\]

is a complete SU(3)-orbit invariant, giving

\[
\boxed{\mathbb{HP}^2/SU(3)\cong[0,1].}
\]

The orbit types are

\[
\begin{array}{c|c|c}
\delta&\text{orbit}&\text{stabilizer}\\ \hline
0&\mathbb{CP}^2&S(U(1)\times U(2))\\
0<\delta<1&SU(3)/U(1)_{1,-1,0}&U(1)_{1,-1,0}\\
1&S^5=SU(3)/SU(2)&SU(2).
\end{array}
\]

The whole quaternionic projective plane is

\[
\boxed{
\mathbb{HP}^2
\cong
SU(3)\times_{U(2)}D^4
\cup_{SU(3)/U(1)_{1,-1,0}}
SU(3)\times_{SU(2)}D^3.}
\]

Thus the old \(\mathbb{CP}^2\) is one endpoint of a genuine internal interval. The other endpoint is \(S^5\).

In the complex-plus-triplet coordinates of a rank-one projector,

\[
\boxed{
 b_P^*b_P
 =\|z\wedge w\|^2
 =\det(Z^*Z)
 =\frac\delta4.}
\]

The new triplet norm is therefore an exact coordinate along the unlocked interval.

## 5. Projection back to the old cone

The complex projection

\[
\pi_{\mathbb C}:\operatorname{Herm}_3(\mathbb H)_{\succeq0}
\longrightarrow
\operatorname{Herm}_3(\mathbb C)_{\succeq0},
\qquad
\pi_{\mathbb C}(\Theta(A,b))=A
\]

is positive, proper, surjective, and SU(3)-equivariant.

Its fibres are:

- over \(A>0\), the six-ball \(\{b:b^*Ab\le\det A\}\), with boundary \(S^5\);
- over rank-two \(A\), a two-ball in \(\ker A\), with radius determined by the product of the two positive eigenvalues;
- over rank at most one, a point.

So the new boundary does not replace the old S8. It maps over the whole old positive cone, with new S5 fibres already over the old interior.

An explicit path leaving the old boundary while remaining rank-deficient is

\[
Q_t=
\begin{pmatrix}
1&0&0\\
0&1&t j\\
0&-t j&t^2
\end{pmatrix}.
\]

It is positive semidefinite of quaternionic rank two for all \(t\), complex at \(t=0\), and genuinely quaternionic for \(t\ne0\).

## 6. The second 13-dimensional slice: exact Lorentz content

There are two different 13-dimensional slices inside the same 15-dimensional closure.

The equal-diagonal slice \(\mathcal T_{13}\) has manifest cyclic three-edge symmetry but contains only the seven-dimensional equal-diagonal complex subspace of the old object.

A second slice contains the complete old nine-dimensional object. Retain the earlier matrix \(X=(R_P\ u)\), and write

\[
X^{-1}AX^{-*}=
\begin{pmatrix}G&z\\z^*&\lambda\end{pmatrix},
\qquad
X^*b=\begin{pmatrix}\chi\\\rho\end{pmatrix}.
\]

Then the full 15-dimensional cubic is

\[
\boxed{
\begin{aligned}
\det_{\mathbb H}\Theta(A,b)
={}&\lambda\det G-z^*\operatorname{adj}(G)z-\chi^*G\chi\\
&-2\operatorname{Re}(\rho\chi^*z)-\lambda|\rho|^2.
\end{aligned}}
\]

Under \(SL_2(\mathbb C)\),

\[
G\mapsto gGg^*,\qquad
z\mapsto gz,\qquad
\chi\mapsto g^{-*}\chi,
\qquad \lambda,\rho\text{ fixed}.
\]

Thus

\[
15=4+4+4+1+2.
\]

Setting \(\rho=0\) gives an invariant 13-dimensional Lorentz slice

\[
\boxed{
\mathcal N_{L13}
=\lambda\det G-z^*\operatorname{adj}(G)z-\chi^*G\chi,}
\]

with

\[
13=4+4+4+1.
\]

This slice contains the old 9-dimensional object at \(\chi=0\). However, the omitted complex scalar \(\rho\) supplies the direct spinor-mixing term

\[
-2\operatorname{Re}(\rho\chi^*z).
\]

Hence the 13-dimensional Lorentz slice is a consistent reduction, while the fully mixed closure is 15-dimensional.

The exact order-three color permutation induces

\[
C_1=
\begin{pmatrix}-1&-1\\1&0\end{pmatrix},
\qquad C_1^3=I_2,
\]

on the Lorentz block variables.

## 7. Truly nonlinear triality dynamics

Define

\[
\mathscr R^2=\lambda^2+\sum_i|q_i|^2
\]

and

\[
V_{13}
=\frac{\mu^2}{2}\mathscr R^2
+\frac\gamma4\mathscr R^4
-\kappa\mathcal N_{13},
\qquad
\mu^2\ge0,\ \gamma>0.
\]

The mechanical Lagrangian

\[
L_{13}
=\frac12\dot\lambda^2+rac12\sum_i|\dot q_i|^2-V_{13}
\]

is globally well posed for all initial conditions. The quartic term makes the potential coercive, and the conserved energy prevents finite-time escape.

The equations include

\[
\ddot q_3+(\mu^2+\gamma\mathscr R^2)q_3
-2\kappa(\bar q_2\bar q_1-\lambda q_3)=0
\]

and its cyclic companions. Therefore

\[
q_3=\dot q_3=0,
\qquad q_1q_2\ne0,
\qquad\kappa\ne0
\]

implies

\[
\boxed{\ddot q_3=2\kappa\bar q_2\bar q_1\ne0.}
\]

Two occupied sectors dynamically create the third. This is the precise sense in which the construction is not a mirrored pair plus a spectator.

Promoting the three edges to bifundamental quaternionic scalar fields gives a local four-dimensional triangle gauge theory with gauge group

\[
\operatorname{Sp}(1)^3/\{\pm1\}
\]

and covariant derivatives

\[
D_\mu q_1=\partial_\mu q_1+A_\mu^{(2)}q_1-q_1A_\mu^{(3)},
\]

with cyclic analogues. The cubic loop is gauge invariant and the model is power-counting renormalizable.

## 8. The SU(3) dynamical unlock

For the full-color version, use

\[
Q=(\Phi,b)\in
\operatorname{Herm}_3^0(\mathbb C)\oplus\mathbb C^3
\cong\mathbb R^{14}
\]

with an SU(3) connection \(\mathcal A_\mu\). Define

\[
\mathscr S^2=\operatorname{tr}(\Phi^2)+2b^*b,
\qquad
\mathcal N_{14}=\det\Phi-b^*\Phi b.
\]

The local action is

\[
\begin{aligned}
\mathcal L_{14}
={}&-\frac1{2g_c^2}\operatorname{tr}(\mathcal F_{\mu\nu}\mathcal F^{\mu\nu})
+\frac12\operatorname{tr}(D_\mu\Phi D^\mu\Phi)
+(D_\mu b)^*D^\mu b\\
&-\frac{m^2}{2}\mathscr S^2
-\frac\Gamma4\mathscr S^4
+\kappa\mathcal N_{14}.
\end{aligned}
\]

This is a local power-counting-renormalizable classical SU(3) gauge theory. The old S8 sector is \(b=0\). The transverse mass matrix at a constant old-sector background is

\[
\boxed{
M_b^2(\Phi_0)
=(m^2+\Gamma\operatorname{tr}\Phi_0^2)I_3+\kappa\Phi_0.}
\]

A negative eigenvalue is an explicit instability out of the old S8.

## 9. Exact vacuum topology and phase transition

For trace-free quaternionic Hermitian \(Q\), let

\[
s(Q)=\operatorname{tr}(Q^2),
\qquad n(Q)=\det_{\mathbb H}Q.
\]

The sharp inequality is

\[
\boxed{54n(Q)^2\le s(Q)^3.}
\]

Equality holds, away from zero, exactly at

\[
Q=x(3P-I_3),
\qquad P\in\mathbb{HP}^2.
\]

For

\[
V_{14}(Q)=\frac{m^2}{2}s(Q)+\frac\Gamma4s(Q)^2-\kappa n(Q),
\]

define

\[
m_c^2=\frac{\kappa^2}{27\Gamma}.
\]

For \(\kappa\ne0\):

- if \(m^2>m_c^2\), the unique vacuum is \(Q=0\);
- if \(m^2=m_c^2\), the origin coexists with
  \[
  Q=\frac\kappa{9\Gamma}(3P-I_3),\quad P\in\mathbb{HP}^2;
  \]
- if \(0\le m^2<m_c^2\), the complete minimum set is
  \[
  \boxed{\mathcal V_{\min}\cong\mathbb{HP}^2,}
  \]
  with
  \[
  x_*=\frac{\kappa+\operatorname{sgn}(\kappa)
  \sqrt{\kappa^2-24\Gamma m^2}}{12\Gamma}.
  \]

At a nonzero vacuum, the scalar Hessian has:

- eight zero modes tangent to \(\mathbb{HP}^2\);
- one radial eigenvalue
  \[
  M_{\rm rad}^2=x_*(12\Gamma x_*-\kappa)>0;
  \]
- one fivefold eigenvalue
  \[
  M_5^2=3\kappa x_*>0.
  \]

After gauging SU(3), the vacuum quotient is the interval \([0,1]\). Generic vacua break

\[
SU(3)\longrightarrow U(1)_{1,-1,0}.
\]

The two endpoints have enhanced stabilizers \(U(2)\) and \(SU(2)\). Thus one exact gauge-invariant flat internal coordinate remains.

Adding the SU(3)-invariant perturbation

\[
\Delta V_\nu=\nu b^*b
\]

restricts on the unperturbed vacuum manifold to

\[
\boxed{
\Delta V_\nu=\frac{9\nu x_*^2}{4}\delta.}
\]

Therefore \(\nu>0\) relocks the vacuum to the old \(\mathbb{CP}^2\), \(\nu<0\) selects the \(S^5\) endpoint, and \(\nu=0\) leaves the whole internal interval free.

## 10. A rigorous finite-lattice quantum theory

Let \(\Lambda=(V,E,\mathcal P)\) be a finite connected oriented spatial lattice. Take configuration space

\[
\mathfrak M_\Lambda
=SU(3)^E\times(\operatorname{Herm}_3^0(\mathbb C)\oplus\mathbb C^3)^V.
\]

The Hilbert space is

\[
\mathscr H_\Lambda
=L^2(\mathfrak M_\Lambda,
\prod_e dU_e\prod_v dQ_v),
\]

with normalized Haar measure on links and Lebesgue measure on all fourteen scalar modes.

For positive constants \(a_g,a_s,\beta_p,\beta_h\), define

\[
H_\Lambda
=-a_g\sum_e\Delta_{SU(3),e}
-a_s\sum_v\Delta_{\mathcal S,v}
+W_\Lambda,
\]

where

\[
\begin{aligned}
W_\Lambda
={}&\beta_p\sum_p(3-\operatorname{Re}\operatorname{tr}U_p)
+\beta_h\sum_{e:s\to t}
\|Q_t-\rho(U_e)Q_s\|^2\\
&+\sum_vV_{14}(Q_v).
\end{aligned}
\]

The vertex gauge action is

\[
U_e\mapsto g_tU_eg_s^{-1},
\qquad Q_v\mapsto\rho(g_v)Q_v.
\]

The exact Gauss-law projection is

\[
\boxed{
P_{\rm phys}
=\int_{SU(3)^V}\mathcal U_\Lambda(g)\,dg.}
\]

The Friedrichs Hamiltonian is bounded below and has compact resolvent. Its ground state is unique, strictly positive, and gauge invariant. On the physical Hilbert space

\[
\mathscr H_{\Lambda,\rm phys}=P_{\rm phys}\mathscr H_\Lambda,
\]

the Hamiltonian has a one-dimensional ground state and a strictly positive finite-volume gap.

This is a genuine nonlinear compact-link quantum system, not a Gaussian Lie-algebra Hessian. No uniform continuum or infinite-volume gap is claimed.

## 11. Exact present interpretation

The answer to “13 or 14?” is not one number:

- **13** is the exact cyclic three-sector ansatz, and also the exact Lorentz vector plus two-spinor plus scalar reduction;
- **14** is the minimal trace-free linear carrier that can contain the old S8 and a full SU(3) triplet of escape directions;
- **15** is the smallest Jordan-closed, fully mixed completion.

The key unlocked topology is

\[
\mathbb{CP}^2
\subset
\mathbb{HP}^2,
\qquad
\mathbb{HP}^2/SU(3)=[0,1],
\]

inside the exact boundary inclusion

\[
S^8\hookrightarrow S^{14}.
\]

The key unlocked dynamics is the cubic source term: two occupied triangle edges generate the third, while in the full-color model the triplet mass matrix can make the old S8 transversely unstable.
