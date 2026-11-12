# Exact definitions, domains, codomains, and conventions

This ledger transcribes the mathematical objects in the packet and supplies the types that are implicit in its prose.  A star is conjugate transpose.  Every Hermitian matrix space is regarded as a real vector space.  The signature convention for the Lorentz determinant is (+---).

## 1. Fixed linear data

The integral map and its primitive kernel vector are

\[
P=\begin{pmatrix}1&-1&0\\0&1&-1\end{pmatrix}:
\mathbb Z^3\twoheadrightarrow\mathbb Z^2,
\qquad
u=\begin{pmatrix}1\\1\\1\end{pmatrix},
\qquad
\ker_{\mathbb Z}P=\mathbb Zu.
\]

The same symbol (P) denotes its scalar extensions (P:\mathbb R^3\to\mathbb R^2) and (P:\mathbb C^3\to\mathbb C^2).  Define

\[
C=PP^*=\begin{pmatrix}2&-1\\-1&2\end{pmatrix},
\qquad
C^{-1}=\frac13\begin{pmatrix}2&1\\1&2\end{pmatrix},
\]

\[
R_P=P^*C^{-1}=\frac13
\begin{pmatrix}2&1\\-1&1\\-1&-2\end{pmatrix}:
\mathbb C^2\longrightarrow\mathbb C^3,
\qquad
\Pi_u=\frac{uu^*}{3}:\mathbb C^3\longrightarrow\mathbb C^3,
\]

and

\[
X=(R_P\;u):\mathbb C^2\oplus\mathbb C\longrightarrow\mathbb C^3,
\qquad
X^{-1}=\begin{pmatrix}P\\u^*/3\end{pmatrix}.
\]

The exact identities are

\[
PR_P=I_2,\qquad R_PP=I_3-\Pi_u,\qquad
Pu=0,\qquad u^*R_P=0,\qquad \det X=1.
\]

## 2. Hermitian spaces, cones, and observation maps

Set

\[
\mathcal J_r=\operatorname{Herm}_r(\mathbb C),
\qquad
\mathcal P_r=\{H\in\mathcal J_r:H\succeq0\}.
\]

Thus (\dim_{\mathbb R}\mathcal J_3=9) and (\dim_{\mathbb R}\mathcal J_2=4).  The packet also uses

\[
\mathcal J_+=\mathcal P_3,\qquad
\mathcal L_+=\mathcal P_2,\qquad
\mathcal N_+=\{G\in\mathcal P_2:\det G=0\},
\]

\[
\mathcal C_{\mathrm{sing}}
=\{H\in\mathcal P_3:\det H=0\}.
\]

The observation and its linear section are the real-linear maps

\[
\mathcal O_P:\mathcal J_3\longrightarrow\mathcal J_2,
\qquad H\longmapsto PHP^*,
\]

\[
\jmath_P:\mathcal J_2\longrightarrow\mathcal J_3,
\qquad G\longmapsto R_PGR_P^*.
\]

Their restrictions give (\mathcal O_P:\mathcal P_3\to\mathcal P_2) and (jmath_P:\mathcal P_2\to\mathcal C_{\mathrm{sing}}).  The adapted-coordinate isomorphism is

\[
\mathcal B_X:
\mathcal J_2\oplus\mathbb C^2\oplus\mathbb R
\longrightarrow\mathcal J_3,
\qquad
(G,z,\lambda)\longmapsto
X\begin{pmatrix}G&z\\z^*&\lambda\end{pmatrix}X^*.
\]

Its inverse is

\[
H\longmapsto
\left(PHP^*,\frac13PHu,\frac19u^*Hu\right).
\]

For (\varepsilon>0), the determinant-opening affine map is

\[
a_\varepsilon:\mathcal L_+\longrightarrow\mathcal J_+,
\qquad
G\longmapsto uu^*+\varepsilon\jmath_P(G).
\]

It is a map of pairs

\[
a_\varepsilon:(\mathcal L_+,\mathcal N_+)
\longrightarrow(\mathcal J_+,\mathcal C_{\mathrm{sing}}).
\]

For (K\in\operatorname{Mat}_{3\times3}(\mathbb C)), the quadratic elementary symmetric polynomial used by the packet is

\[
e_2(K)=\frac12\bigl((\operatorname{tr}K)^2-\operatorname{tr}(K^2)\bigr).
\]

## 3. Spin action

For (g\in SL_2(\mathbb C)), define

\[
T_P(g)=R_PgP+\Pi_u
=X(g\oplus1)X^{-1}\in SL_3(\mathbb C).
\]

Thus

\[
T_P:SL_2(\mathbb C)\hookrightarrow SL_3(\mathbb C)
\]

is a group homomorphism.  It acts on (\mathcal J_3) by congruence (H\mapsto T_P(g)HT_P(g)^*), and in block coordinates this is

\[
(G,z,\lambda)\longmapsto(gGg^*,gz,\lambda).
\]

The Pauli-coordinate identification is

\[
G=p^0I_2+p^1\sigma_1+p^2\sigma_2+p^3\sigma_3,
\qquad
\det G=(p^0)^2-(p^1)^2-(p^2)^2-(p^3)^2.
\]

Consequently the first summand is the Lorentz vector representation, the second is the defining complex, or left-Weyl, representation, and the third is trivial.  The central element (-I_2) fixes (G,\lambda) and sends (z\mapsto-z).

## 4. Topological coordinate maps

Let

\[
\mathfrak p=\operatorname{Herm}_3^0(\mathbb C)
=\{A=A^*:\operatorname{tr}A=0\}.
\]

The rank-deficient-cone coordinate maps are

\[
\Phi_{\mathrm G}:\mathfrak p\longrightarrow\mathcal C_{\mathrm{sing}},
\qquad
A\longmapsto A-\lambda_{\min}(A)I_3,
\]

\[
\Psi_{\mathrm G}:\mathcal C_{\mathrm{sing}}\longrightarrow\mathfrak p,
\qquad
Q\longmapsto Q-\frac{\operatorname{tr}Q}{3}I_3.
\]

They are inverse positively homogeneous homeomorphisms.  A compatible half-space coordinate for all of (\mathcal J_+) is

\[
H\longmapsto
\left(A=H-\frac{\operatorname{tr}H}{3}I_3,
r=\frac{\operatorname{tr}H}{3}+\lambda_{\min}(A)\right)
\in\mathfrak p\times[0,\infty).
\]

The inverse is (H=A+(r-\lambda_{\min}(A))I_3).  Therefore

\[
\mathcal C_{\mathrm{sing}}\cong\mathbb R^8,\quad
\mathcal C_{\mathrm{sing}}^+\cong S^8,\quad
\mathcal J_+\cong\mathbb R^8\times[0,\infty),\quad
\mathcal J_+^+\cong B^9.
\]

Here a superscript (+) means one-point compactification, not positive part.

## 5. Phase-retaining (SU(3)) carrier

Define

\[
\mathcal Y_3
=\{(H,\omega)\in\mathcal J_+\times\mathbb C:
|\omega|^2=\det H\}.
\]

The packet's global coordinate map is

\[
\Theta:\mathcal Y_3\longrightarrow\mathfrak p\times\mathbb C,
\qquad
(H,\omega)\longmapsto
\left(H-\frac{\operatorname{tr}H}{3}I_3,\omega\right).
\]

For (A\in\mathfrak p) and (r\ge0), let (\tau(A,r)\ge-\lambda_{\min}(A)) be the unique solution of

\[
\det(A+\tau I_3)=r.
\]

Then

\[
\Theta^{-1}(A,\omega)
=\bigl(A+\tau(A,|\omega|^2)I_3,\omega\bigr).
\]

In block coordinates (\mathcal Y_3) is

\[
\left\{(G,z,\lambda,\omega):
\begin{pmatrix}G&z\\z^*&\lambda\end{pmatrix}\succeq0,
\quad
|\omega|^2=\lambda\det G-z^*\operatorname{adj}(G)z
\right\}.
\]

## 6. Colour quotient

The colour configuration space is

\[
\mathscr V=\operatorname{Mat}_{3\times2}(\mathbb C)\oplus\mathbb C^3
\cong\operatorname{Mat}_{3\times3}(\mathbb C),
\qquad
(Z,\phi)\longleftrightarrow B=[Z\ \phi].
\]

The commuting actions are

\[
U\cdot(Z,\phi)=(UZ,U\phi),\qquad U\in SU(3),
\]

\[
g\cdot(Z,\phi)=(Zg^*,\phi),\qquad g\in SL_2(\mathbb C).
\]

Define

\[
M(B)=B^*B=\begin{pmatrix}G&z\\z^*&\lambda\end{pmatrix},
\quad
G=Z^*Z,\quad z=Z^*\phi,\quad \lambda=\phi^*\phi,
\]

\[
H_P(B)=XM(B)X^*,\qquad \omega(B)=\det B.
\]

The complete quotient map is

\[
\Gamma_P:\mathscr V\longrightarrow\mathcal Y_3,
\qquad
(Z,\phi)\longmapsto(H_P(B),\omega(B)).
\]

Its fibres are the left (SU(3))-orbits.

## 7. Toroidal lattice and shared-kernel maps

Let (L_3\cong\mathbb Z^3), (\overline L_3\cong\mathbb Z^3), (A_F\cong\mathbb Z^2), and (B_F\cong\mathbb Z^2).  Besides (P:L_3\to A_F), define

\[
B_0=\begin{pmatrix}0&1\\-1&0\end{pmatrix}:B_F\longrightarrow A_F,
\qquad
Q=B_0^{-1}P
=\begin{pmatrix}0&-1&1\\1&-1&0\end{pmatrix}:
\overline L_3\longrightarrow B_F,
\]

\[
\Phi=P\oplus Q:L_3\oplus\overline L_3
\longrightarrow A_F\oplus B_F,
\qquad
\Phi(a,b)=(Pa,Qb).
\]

The monodromies and filling projections required to type the packet's imported filling square are

\[
M_3:L_3\oplus\overline L_3\to L_3\oplus\overline L_3,
\qquad M_3(a,b)=(a+b,b),
\]

\[
M_F:A_F\oplus B_F\to A_F\oplus B_F,
\qquad M_F(a',b')=(a'+B_0b',b'),
\]

\[
c_3:L_3\oplus\overline L_3\to\overline L_3,
\quad c_3(a,b)=b,
\qquad
c_F:A_F\oplus B_F\to B_F,
\quad c_F(a',b')=b'.
\]

The torus map is

\[
\overline P:(L_3\otimes\mathbb R)/L_3
\longrightarrow(A_F\otimes\mathbb R)/A_F,
\qquad [x]\longmapsto[Px],
\]

with (\ker\overline P=(\mathbb Ru)/(\mathbb Zu)\cong S^1).  For every (k\ge1), the Gram-naturality map is

\[
\operatorname{Mat}_{3\times k}(\mathbb C)\longrightarrow\mathcal J_3,
\qquad A\longmapsto AA^*,
\]

followed by

\[
\mathcal O_P(AA^*)=(PA)(PA)^*.
\]

On the common complex kernel line there is a precise additional quotient map

\[
q:\mathbb Cu\longrightarrow\mathbb R_{\ge0}uu^*,
\qquad tu\longmapsto |t|^2uu^*.
\]

It is the orbit map for scalar (U(1)): for (r>0), (q^{-1}(r uu^*)=\{\sqrt r e^{i\theta}u:\theta\in\mathbb R\}), and (q^{-1}(0)=\{0\}).  Under ([su]\mapsto e^{2\pi i s}u), the torus kernel is exactly the (U(1))-fibre over (uu^*).  Thus the circle and the ray are related by an explicit orbit map; they are not literally the same object.

## 8. Momentum and representation maps

Fix (\alpha>0).  Define

\[
p:\operatorname{Mat}_{3\times2}(\mathbb C)\longrightarrow
\operatorname{Herm}_2(\mathbb C)_{\succeq0},
\qquad
p(Z)=\alpha Z^*Z,
\]

and

\[
m^2(Z)=\det p(Z).
\]

In the packet convention (m^2) has momentum-squared units and the physical mass is (M_{\mathrm{phys}}=\sqrt{m^2}/c).  On

\[
\mathscr H_Z=L^2(\operatorname{Mat}_{3\times2}(\mathbb C),d^{12}Z)^{SU(3)},
\]

the Lorentz action and translations are

\[
(\mathsf U_g\psi)(Z)=\psi\bigl(Z(g^{-1})^*\bigr),
\qquad
(\mathsf T(a)\psi)(Z)=
e^{-ia_\mu p^\mu(Z)/\hbar}\psi(Z).
\]

The observer Hamiltonian and mass-squared operator are maximal multiplication operators

\[
H_n=c\,n_\mu\widehat p^\mu,
\qquad
\widehat M^2=\det\widehat p.
\]

## 9. Fixed-((\lambda_0,\omega_0)) sector

Fix

\[
\lambda_0>0,\qquad \omega_0\in\mathbb C^*.
\]

The constrained configuration, gauge quotient, and invariant-coordinate model are

\[
\mathscr S_{\lambda_0,\omega_0}
=\{(Z,\phi):\phi^*\phi=\lambda_0,
\ \det[Z\ \phi]=\omega_0\},
\]

\[
\mathscr Q_{\lambda_0,\omega_0}
=\mathscr S_{\lambda_0,\omega_0}/SU(3)
\cong
\{(G,z):G>0,
\ z^*\operatorname{adj}(G)z=\lambda_0\det G-|\omega_0|^2\}.
\]

Define

\[
\mu=\sqrt{\det G},\qquad
A=\log(\mu^{-1}G)\in\operatorname{Herm}_2^0(\mathbb C),
\qquad
w=G^{-1/2}z\in\mathbb C^2.
\]

Then

\[
\mu(w)=\frac{|\omega_0|}{\sqrt{\lambda_0-\|w\|^2}},
\qquad
G(A,w)=\mu(w)e^A,
\qquad
z(A,w)=G(A,w)^{1/2}w,
\]

with (|w|^2<\lambda_0).  This types the diffeomorphism

\[
\mathscr Q_{\lambda_0,\omega_0}
\cong\operatorname{Herm}_2^0(\mathbb C)
\times\mathbb B^4_{\sqrt{\lambda_0}}
\cong\mathbb H^3\times\mathbb B^4_{\sqrt{\lambda_0}}.
\]

Equivariantly,

\[
\mathscr Q_{\lambda_0,\omega_0}
\cong SL_2(\mathbb C)\times_{SU(2)}
\mathbb B^4_{\sqrt{\lambda_0}},
\]

where ((g,w)\sim(gk,k^{-1}w)).  The map to invariant coordinates is

\[
[g,w]\longmapsto
\bigl(G=\mu(w)gg^*,\ z=\sqrt{\mu(w)}gw\bigr).
\]

The constrained momentum projection is

\[
p:\mathscr Q_{\lambda_0,\omega_0}\longrightarrow
\left\{p\in\operatorname{Herm}_2(\mathbb C)_{>0}:
\det p\ge\frac{\alpha^2|\omega_0|^2}{\lambda_0}\right\},
\qquad
(G,z)\longmapsto\alpha G.
\]

For a fixed (G>0), its spin-cover little group is

\[
K_G=\{g\in SL_2(\mathbb C):gGg^*=G\}
=G^{1/2}SU(2)G^{-1/2}.
\]

## 10. Constrained action and Hilbert-space operators

Let (I\subset\mathbb R) be a world-line interval, let (x:I\to\operatorname{Herm}_2(\mathbb C)) be Minkowski position, let (Z:I\to\operatorname{Mat}_{3\times2}(\mathbb C)), (\phi:I\to\mathbb C^3), (\rho:I\to\mathbb R), and (\chi:I\to\mathbb C).  The packet action is

\[
S=\int_I\left[
\langle p(Z),\dot x\rangle_L
-\rho(\phi^*\phi-\lambda_0)
-2\operatorname{Re}\!\left(
\overline\chi(\det[Z\ \phi]-\omega_0)
\right)\right]d\tau,
\]

where the packet writes the first term as (p_\mu\dot x^\mu).  After exact reduction by the regular constraints and colour orbits, its intrinsic action is

\[
S_{\mathrm{red}}[x,A,w]
=\int_I\langle p(A,w),\dot x\rangle_Ld\tau,
\qquad
p(A,w)=\alpha\mu(w)e^A.
\]

The distributional constrained measure and invariant Hilbert space proposed separately in the packet are

\[
d\mu_{\lambda_0,\omega_0}
=\delta(\phi^*\phi-\lambda_0)
\delta(\operatorname{Re}\omega-\operatorname{Re}\omega_0)
\delta(\operatorname{Im}\omega-\operatorname{Im}\omega_0)d^{18}B,
\]

\[
\mathscr H_{\lambda_0,\omega_0}
=L^2(\mathscr S_{\lambda_0,\omega_0},d\mu_{\lambda_0,\omega_0})^{SU(3)}.
\]

On it, the packet defines multiplication operators (\widehat M^2=\det\widehat p) and (H_n=c\,n_\mu\widehat p^\mu).  These operators are not the Hamiltonian generators of the reduced (\tau)-evolution displayed above; that distinction is part of the verdict.

## 11. Explicitly unconstructed maps

The packet correctly does not define any of the following:

1. a pointwise map from the toroidal total space to (\mathcal Y_3) compatible with fan charts, periods, monodromy, and fillings;
2. the global analytic overlap cocycle through both finite fillings;
3. an intertwiner from the one-particle or Fock carrier into an interacting (SU(3)) gauge-field Hilbert space with a spacetime connection and an energy-form estimate;
4. a geometrically forced, globally Poincaré-invariant projector selecting a single spin, such as (j=\tfrac12), from (L^2(SU(2))).

The illustrative but unconstructed field-theory maps in `remaining_maps.md` are

\[
J_n:\text{packet state space}\longrightarrow\mathscr H_{\mathrm{field}},
\]

required to satisfy, for specified vectors (\psi_n),

\[
\|J_n\psi_n\|\ge c_0>0,
\qquad
\langle J_n\psi_n,H_{\mathrm{field}}J_n\psi_n\rangle
\le Cq_n[\psi_n].
\]

No domain, construction, or proof of such (J_n) is supplied by the packet.
