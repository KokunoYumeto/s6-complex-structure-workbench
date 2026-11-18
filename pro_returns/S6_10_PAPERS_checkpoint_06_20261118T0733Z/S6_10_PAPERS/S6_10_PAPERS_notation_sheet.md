# S6_10_PAPERS notation and explicit transports

The retained notation is reproduced below from the S6_09 sheet. Receiving additions and corrections precede it.

- Geometric and arithmetic Weierstrass models are related by (x,y) -> (2x,-2 sqrt(2)y), with lattice map z -> z/(-sqrt(2)); Paper I proves the normalization and norm transport.
- The physical point line M and the graph-normal meridian line are related by the explicit Hermitian map to M^{-1}; Paper IV records its circle weight -1 and the oriented cap map.
- The corrected physical index is A_M=H/2-chi. All family classes retain their actual cusp fan and endpoint maps.
- The ordinary period upper half-plane is denoted by mathbb H. Night-source occurrences of mathcal H are transported with their local definition, not silently identified with the upper half-plane.
- The parameter maps are w=exp(-pi i c), u=w^2, and q_2=iw/216 for the standard fixed data.

# S6_09_PAPERS — common notation and source-to-print concordance

**Scope.** This dictionary covers Papers I–III and every row of the common result inventory. FAMILY supplies the binding marking, base orientation and parameter normalization. The adaptations below identify the other sources in that marking. A displayed change of basis, a reversal of a loop, a dual representation, and a change from an additive to a multiplicative parameter are separate operations.

**Current inventory.** Paper I: 348 rows; Paper II: 313 rows; Paper III: 523 rows. The appendices give all 1184 result identifiers, their actual paper and printed label, the retained consolidation aliases, and every label in the assembled TeX files. Printed numbers come from the available auxiliary files; the labels remain the stable references when a later build changes numbering. Source and auxiliary-file hashes, coverage checks and the regeneration command are in the accompanying notation audit.

**Preparation and review.** GPT-6 Astra (OpenAI, ChatGPT Pro mode), effort Pro, 17 November 2026 UTC. The source-specific mathematical reviews and earlier AI model/date/effort records remain in the result inventory. This dictionary does not claim human verification or add a human contributor.

## 1. Base, divisors, periods and integral marking

### 1.1. Base points and full fibres

The common base is

$$
B=\mathbb P^1_{t_B},\qquad p_1=0,\quad p_2=1,\quad p_0=\infty,
\qquad \Sigma=\{p_0,p_1,p_2\},\quad B^\circ=B\setminus\Sigma.
$$

The papers usually write $t$ for $t_B$. We add the subscript only in this dictionary when a source also uses $t$ for a cusp coordinate or a deformation parameter. The reduced divisors are $S_1,S_2,W$, and

$$
f^*p_1=3S_1,\qquad f^*p_2=4S_2,\qquad f^*p_0=W,
\qquad D=W+S_1+S_2.
$$

Thus coherent restriction to a **full fibre** retains its nilpotent normal directions; restriction to $S_j$ means its reduction. In topological Euler localization the fibre is reduced because nilpotents do not change its underlying space. In higher multiplicity families, replace $3,4$ by the stated $3k,4l$, retaining the specified root characters. These conventions are fixed in FAMILY `sections/conventions.tex`, Paper I, `inv:A1.0` (number `8.1`), and Paper II, `cdp:st:C2a` (number `9.5`).

### 1.2. Positive meridians and analytic deck generators

A positive base meridian is counterclockwise in a holomorphic local coordinate. The analytic root-deck generator is clockwise:

$$
s_j(g_jz)=e^{-2\pi i/m_j}s_j(z),\qquad g_1g_2g_0=1.
$$

The lift of a positive base loop ends at the inverse deck translate. Identifying that endpoint with the starting fibre applies $g_j$; its homology monodromy is consequently $A_j$. The clockwise boundary of a deleted disc, used in a Stokes or collar calculation, has its own boundary orientation. The collar convention is recorded in Paper I, `inv:C3.2` (number `10.6`). A matrix conjugacy alone changes neither of these loop orientations.

### 1.3. Homology, dual cohomology and row order

Use column coordinates in

$$
\Lambda=H_1(F;\mathbb Z)
 =\mathbb Z\langle\widehat\gamma,\widehat u,\widehat w,\widehat\delta\rangle.
$$

The ordered dual cohomology basis is $(\gamma,u,w,\delta)$. A hat denotes an integral cycle. An unhatted letter in this ordered list denotes a covector. In particular, the cohomology class $w$ and the scalar family parameter $w=e^{-\pi ic}$ are different objects.

In additive fibre coordinates $(\zeta_1,\zeta_2)$, equivalently $(\xi,\eta)$ where explicitly so named, the periods are

$$
\Pi_c=
\begin{pmatrix}
6\mu&\tau&1&0\\
\beta_c&\mu&0&1
\end{pmatrix},\qquad
\beta_c=\beta^{\mathrm{part}}+c,\qquad
(\beta^{\mathrm{part}}+\tau)(p_0)=0.
$$

Its rows are $6\mu\gamma+\tau u+w$ and $\beta_c\gamma+\mu u+\delta$. The common finite homology matrices are

$$
A_1=\begin{pmatrix}
1&0&0&0\\6&0&1&0\\-6&-1&-1&0\\-2&1&0&1
\end{pmatrix},\qquad
A_2=\begin{pmatrix}
1&0&0&0\\0&0&-1&0\\-6&1&0&0\\3&0&1&1
\end{pmatrix},\qquad A_0=(A_1A_2)^{-1}.
$$

If a local calculation orders the complex coordinates as $(\zeta_2,\zeta_1)$, its period matrix is $J_{\mathrm{swap}}\Pi_c$, where

$$
J_{\mathrm{swap}}=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
$$

The corresponding Hermitian coefficient matrix becomes $J_{\mathrm{swap}}H J_{\mathrm{swap}}^{\mathsf T}$. This row interchange is not the radial rotation matrix $J_{\mathrm{rot}}$ in §4.

For a geometric fibre map with homology matrix $M$, its pullback on covectors has matrix $M^{\mathsf T}$. Parallel transport of the **dual local system in the same base-loop direction** has matrix $M^{-\mathsf T}$. This distinction explains the inverse matrices in the fourfold cohomology calculations; see §6.1.

### 1.4. Engel and reversed-meridian adapters

Engel's base indices $(0,1,\infty)$ correspond to FAMILY $(1,2,0)$. The columns of

$$
P_{\mathrm{mark}}=
\begin{pmatrix}
0&-2&-1&-2\\2&-1&0&-1\\0&2&1&3\\-1&0&0&0
\end{pmatrix}
$$

are the FAMILY basis in Engel's common basis. Thus

$$
T_0P_{\mathrm{mark}}=P_{\mathrm{mark}}A_1,
\qquad T_1P_{\mathrm{mark}}=P_{\mathrm{mark}}A_2,
\qquad \delta_E=P_{\mathrm{mark}}\widehat\delta.
$$

The reversed-meridian marking retained in INVARIANTS is

$$
Q_{\mathrm{mark}}=P_{\mathrm{mark}}S_{\mathrm{rev}},\qquad
S_{\mathrm{rev}}=
\begin{pmatrix}-1&0&0&0\\-6&0&-1&0\\6&-1&0&0\\2&1&1&1\end{pmatrix},
\qquad
Q_{\mathrm{mark}}=
\begin{pmatrix}2&-1&0&-2\\2&-1&0&-1\\0&2&1&3\\1&0&0&0\end{pmatrix}.
$$

It satisfies $T_0Q_{\mathrm{mark}}=Q_{\mathrm{mark}}A_1^{-1}$ and $T_1Q_{\mathrm{mark}}=Q_{\mathrm{mark}}A_2^{-1}$. For FAMILY finite-twist vectors $v_1,v_2$, Engel's positive-root affine vectors are

$$
a_0=-P_{\mathrm{mark}}v_1/3,\qquad
a_1=-P_{\mathrm{mark}}v_2/4.
$$

The exact transition is proved in Paper I, `inv:B1.0` (number `9.1`) and the family comparison statements. The symbol $Q_{\mathrm{mark}}$ here is unrelated to a quotient surface, the cotangent quotient $Q$, or the real torus $Q_T$.

## 2. Family parameters, line bundles and analytic invariants

### 2.1. Additive and multiplicative parameters

Set $v_{\mathrm{fib}}=e^{2\pi i\zeta_2}$. The first period acts by

$$
(\zeta_1,v_{\mathrm{fib}})\longmapsto
(\zeta_1+6\mu,e^{2\pi i\beta_c}v_{\mathrm{fib}}).
$$

Engel's contracting generator is the inverse lift over the translation $-6P$ on the complement of the zero section of $M_S=\mathcal O_S(P-O)$. With its reference inverse lift transported from $c=0$,

$$
w_{\mathrm{fam}}=e^{-\pi ic},\qquad
u_E=w_{\mathrm{fam}}^2,\qquad
0<\lvert w_{\mathrm{fam}}\rvert<216,\qquad
0<\lvert u_E\rvert<46656.
$$

A different reference lift changes $u_E$ by a fixed nonzero scalar. The multiplicative coordinate $u_E$, the cohomology covector $u$, an elliptic logarithm $u$, and a local deformation variable $u$ retain their stated local meanings.

A positive $w_{\mathrm{fam}}$-circle lifts to $c(r)=c_0-2r$, $0\le r\le1$. With coherent even-shift maps $F_{n,c}:X_c\to X_{c+n}$, the closing diffeomorphism is

$$
\Phi=F_{2,c_0-2}\circ H,
$$

where $H$ is parallel transport along that lifted path. On fibre homology $F_{n,c}$ acts by $I-nE$, $E=\widehat\delta\otimes\gamma$. This convention is used in Paper III, `fam:src:E.2.2` (number `8.1`) and Paper I, `push:src:C.3.5` (number `18.5`).

In the fixed exponential cusp chart, $q_c=e^{2\pi is}$, $C_{c,21}=c+C_{0,21}$, and

$$
\ell=(2\pi i)^{-1}\log(F/G)=-s/12+\kappa_0(q_c),\qquad
D_{\mathrm{orig}}=C_{0,21}-12\kappa_0,
$$

the coherent cusp-origin correction is

$$
\sigma(c)=\left(-\frac{c\mu}{2},-\frac{c^2}{24}-\frac{cD_{\mathrm{orig}}}{12}\right),
\qquad
\overline b_{h,c}=\sigma(c+h)-\sigma(c).
$$

This $D_{\mathrm{orig}}$ is a holomorphic residual function, not the real determinant $D_c$. The actual cusp logarithm is computed in Paper I, `mapsI:src:A.3.2` (number `18.2`); direct subtraction of the displayed quadratic primitive gives the stated coherent origin. The scoped check is retained in `work/maps_audit/closing_origin_check.tex`. The scalar representative $t_B^4/(t_B-1)^3$ and the holomorphic cusp-unit representative of the closing translation differ by a deck period; they are compared in the complete closing-cocycle proof rather than equated as scalar functions.

### 2.2. Determinant and orientation

Write $y=\operatorname{Im}\tau>0$, $m=\operatorname{Im}\mu$, $r=\operatorname{Im}\beta_c$. Then

$$
D_c=r-6m^2/y=D_{\mathrm{part}}+\operatorname{Im}c<0
$$

on an admissible fibre. In real coordinate order $(\operatorname{Re}\zeta_1,\operatorname{Im}\zeta_1,\operatorname{Re}\zeta_2,\operatorname{Im}\zeta_2)$, the period determinant is $yD_c$. The marked lattice orientation is opposite to the complex orientation. With

$$
\eta_F=u\wedge w+6\gamma\wedge\delta,
\qquad
\int_{F,\operatorname{or}_{\mathbb C}}\eta_F^2=-12,
$$

the Dolbeault representative of $\gamma^{0,1}$ is

$$
\Gamma=\frac{i}{2D_c}
\left(d\overline\zeta_2-\frac{m}{y}d\overline\zeta_1\right).
$$

The source symbol $\Delta$ in these real fibre formulas means $D_c$; the arithmetic discriminants in §3 are separate. $\eta_F$ is an integral two-class, not Dedekind's eta function, a quasi-period, or the stable Hopf class.

### 2.3. Primitive global class, root powers and logarithmic sheaves

The exponential sheaf map is $z\mapsto e^{2\pi iz}$. The primitive global class $\mathfrak g=g_\gamma$ satisfies

$$
\exp(12g_\gamma)=f^*\mathcal O_B(-p),\qquad
p=12l_0-4l_1-3l_2.
$$

For standard twists $(l_0,l_1,l_2)=(0,1,-1)$, $p=-1$,

$$
\mathcal O_X(S_1-S_2)=\exp(\mathfrak g),\qquad
[G_0]=12\mathfrak g.
$$

Here $G_0$ denotes the unrescaled representative. With $\int_B\omega_{FS}=1$ and $c_{1,BC}(L)=[iF_L/(2\pi)]$, the unnormalized Chern–Ricci form represents $2\pi c_{1,BC}(T_X)$; the prescribed form in the invariant calculation is $\pi f^*\omega_{FS}$.

On the root curve $\mathcal B$, let $R=R_1R_2^{-1}$. Then

$$
R_1=R^4,\quad R_2=R^3,\quad
\rho^*\mathcal O_B(1)=R^{12},\quad K_{\mathcal B}=R^{-7}.
$$

Thus $\mathcal O_{\mathcal B}(n)=R^n$ has root degree $n/12$, while $\mathcal O_B(n)$ has coarse degree $n$. The stabilizer characters must also be retained. In the fourfold construction the actual line $L=\mathcal O_X(S_1-S_2)$ has $L^{12}=\mathcal O_X(W)$; its powers supply the Weierstrass coefficients.

The invariant logarithmic notation is

$$
\mathcal L=\Omega_B^1(\log\Sigma),\qquad
\mathcal A=\Omega_X^1(\log D),\qquad
\mathcal E=\mathcal A/f^*\mathcal L.
$$

These are different from a twisting line $A$ in CDP, from a lattice action $A$, and from the exceptional divisor of a local modification.

## 3. Arithmetic and special-fibre normalizations

### 3.1. Theta variable, modular coordinate and discriminants

The theta variable has periods $(1,\tau)$. Software whose first theta argument has period $\pi$ is given $\pi z$. With $q_{\mathrm{mod}}=e^{2\pi i\tau}$,

$$
N(z,\tau)=\left\lvert\frac{\vartheta_1(z,\tau)}{\eta(\tau)}\right\rvert
e^{-\pi(\operatorname{Im}z)^2/\operatorname{Im}\tau},\qquad
D_{\mathrm{part}}=\frac6\pi\log\frac{N(\mu,\tau)}{2\sqrt3}.
$$

Here $N$ is a theta norm, not a monodromy norm operator. Put

$$
\Delta_0=q_{\mathrm{mod}}\prod_{n\ge1}(1-q_{\mathrm{mod}}^n)^{24},\qquad
t_B=\frac{j(\tau)}{1728}=\frac{E_4^3}{1728\Delta_0},\qquad
t_B-1=\frac{E_6^2}{1728\Delta_0}.
$$

For the rational Weierstrass model,

$$
E_t:\quad Y^2=X^3-\frac34t^3(t-1)X+\frac14t^4(t-1)^2,
\qquad P_t=(0,t^2(t-1)/2),
$$

the differential is $dX/(2Y)$, and $\Delta_E=27t^8(t-1)^3$. In lattice coordinates $X=\wp(u)$, $Y=\wp'(u)/2$, and

$$
g_2^3-27g_3^2=(2\pi)^{12}\eta(\tau)^{24}
$$

for the lattice $\mathbb Z+\tau\mathbb Z$. Each occurrence of a period in a special Weierstrass model also retains its explicitly printed homothety.

### 3.2. Heights and quasi-periods

The height convention is

$$
\widehat h_O(P)=\frac12\lim_{n\to\infty}n^{-2}h(x(nP)).
$$

PARI `ellheight`, the elliptic-surface self-pairing, and the rank-one BSD regulator use $2\widehat h_O$. The full real period is $\Omega=\int_{E(\mathbb R)}\lvert\omega\rvert$, including both real components when the curve is disconnected. The archimedean local height in the specified theta normalization is $-\log N$. At finite places $\lvert p\rvert_v=p^{-1}$, $n_v=[K_v:\mathbb Q_p]$; complex embeddings are counted separately in the global sum.

Quasi-periods are defined by

$$
\zeta(z+\omega_j)=\zeta(z)+\eta_j,\qquad
\omega_1\eta_2-\omega_2\eta_1=-2\pi i.
$$

The notation $\eta(u)$ denotes their real-linear extension, not the holomorphic zeta function itself. An algebraic period relation and a statement that a theta norm is algebraic are different assertions; the remaining unconditional norm-transcendence question retains its exact scope in Paper I's final part.

For the curvature and equidistribution calculation,

$$
dd^c=(i/\pi)\partial\bar\partial,\qquad
dA_z=(i/2)\,dz\wedge d\bar z,\qquad
\mu=a\tau+b\quad(a,b\in\mathbb R).
$$

The positive Betti measure is $m_P=db\wedge da$, in that order. If $L=\log N(P_t)$, its exact normalization is

$$
dd^cL=\frac1{12}\delta_\infty-m_P,\qquad
\int_Bm_P=\frac1{12}.
$$

Thus $12m_P$ is the probability measure in torsion equidistribution. The letter $L$ here denotes a scalar logarithm, while the fourfold construction uses $L$ for a line bundle. See Paper I, `ari:C.8.9` (number `14.8`) and Paper I, `ari:C.8.10` (number `14.9`).

### 3.3. Special fibres and the Cayley calculation

The elliptic special value uses $\rho=e^{\pi i/3}$; using $e^{2\pi i/3}=\rho-1$ changes the marking by $\tau\mapsto\tau+1$. The Albanese parameters are

$$
\kappa_1=c+\frac12-\frac{3i}{2\pi}\log48,
\qquad
\kappa_2=c+\frac32-\frac{3i}{\pi}\log6.
$$

Their upper-half-plane periods are respectively $-\kappa_1$ and $-\kappa_2/2$. Therefore

$$
q_1=e^{-2\pi i\kappa_1}=-w_{\mathrm{fam}}^2/48^3,
\qquad
q_2=e^{-\pi i\kappa_2}=iw_{\mathrm{fam}}/216,
\qquad q_1=\frac{27}{64}q_2^2.
$$

The factor $1/2$ in the second period is part of the full order-four Albanese lattice projection.

In the compact critical-point certificate the exact variables are

$$
\chi=\frac{\tau-i}{\tau+i},\qquad
A=E_4(i),\qquad k=\pi^2A,\qquad
v=\pi\sqrt A\,\chi,\qquad z=v^2=k\chi^2.
$$

Thus $k$ is a constant, and $\chi$ is the Cayley coordinate. The separately named cusp constant $\beta_{\mathrm{cusp}}=\log(5+2\sqrt6)/(2\pi)$ is unrelated to $\beta_c$. The underlying exact definitions are in Paper I, `ari:C.8.14` (number `15.3`).

## 4. Native cusp coordinates, real periods and carrier maps

### 4.1. Three different base variables

| Source notation | Common interpretation |
|---|---|
| FAMILY $t$, arithmetic $t=j/1728$ | Global coordinate $t_B$, with cusp at infinity. |
| Native carrier $t$, toroidal $q$ or $t_c$ | Local cusp coordinate $q_c=e^{2\pi is}$, with cusp at zero; in a maximal chart $q_c=z_0z_1z_2$. |
| Arithmetic $q=e^{2\pi i\tau}$ | Modular nome $q_{\mathrm{mod}}$. Since $\tau=s+h(q_c)$, $q_{\mathrm{mod}}=q_c e^{2\pi ih(q_c)}$. |
| A disc parameter in a deformation or plumbing | The local base variable of that displayed family, for example in $xy=uzv$; it is not automatically $t_B$, $q_c$, or $w_{\mathrm{fam}}$. |

The exact source name $t=q_c$ in the native carrier proofs is preserved. No global equality $t_B=q_c$ is used. A local coordinate at $p_0$ is compared with $1/t_B$ only through the specified analytic chart and its unit factors.

The cusp periods have the form

$$
\Pi=[Z\mid I_2],\qquad
Z=sJ_{\mathrm{rot}}+
\begin{pmatrix}6\mu(q_c)&h(q_c)\\b(q_c)-h(q_c)&\mu(q_c)\end{pmatrix},
\qquad
J_{\mathrm{rot}}=\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
$$

Thus $\tau=s+h(q_c)$ and $\beta_c=b(q_c)-h(q_c)-s$; all residual functions are holomorphic on the specified cusp disc. $J_{\mathrm{rot}}$ is an orientation-preserving quarter-turn with determinant one. It is distinct from $J_{\mathrm{swap}}$, an intersection matrix, and a Jacobian ideal.

### 4.2. Exact radial real matrices

On the positive ray of a sufficiently small fixed cusp chart, set $q_c=e^{-2\pi T}$, $s=iT$. Write

$$
\mu_T=\alpha_T+im_T,\quad h_T=\eta_T+iH_T,\quad
b_T=\xi_T+iB_T,\quad c_T=\xi_T-\eta_T,
$$

$$
L_T=T+H_T,\qquad q_T=L_T-B_T,\qquad
D_T=L_Tq_T+6m_T^2.
$$

The real scalar $q_T$ is not either nome. In coordinate order $(x_1,y_1,x_2,y_2)$,

$$
F_T=\mathbb R^4/P_T\mathbb Z^4,\qquad
P_T=\begin{pmatrix}
6\alpha_T&\eta_T&1&0\\
6m_T&L_T&0&0\\
c_T&\alpha_T&0&1\\
-q_T&m_T&0&0
\end{pmatrix},\qquad \det P_T=-D_T.
$$

The dual real lattice is $P_T^{-\mathsf T}\mathbb Z^4$, with

$$
P_T^{-\mathsf T}=\begin{pmatrix}
0&0&1&0\\
m_T/D_T&q_T/D_T&(-6m_T\alpha_T-q_T\eta_T)/D_T&(-m_Tc_T-q_T\alpha_T)/D_T\\
0&0&0&1\\
-L_T/D_T&6m_T/D_T&6(L_T\alpha_T-m_T\eta_T)/D_T&(L_Tc_T-6m_T\alpha_T)/D_T
\end{pmatrix}.
$$

The imaginary-coordinate projection $\rho(x_1,y_1,x_2,y_2)=(y_1,y_2)$ has projected period matrix

$$
Y_T=\begin{pmatrix}6m_T&L_T\\-q_T&m_T\end{pmatrix}
=TJ_{\mathrm{rot}}+O(1),\qquad
\det Y_T=D_T>0,
\qquad Q_T=\mathbb R^2/Y_T\mathbb Z^2.
$$

The exact kernel is

$$
0\longrightarrow
\frac{\mathbb Re_1\oplus\mathbb Re_3}{\mathbb Ze_1\oplus\mathbb Ze_3}
\longrightarrow F_T\longrightarrow Q_T\longrightarrow0.
$$

These are the angular cycles $(\widehat w,\widehat\delta)$; the quotient basis is $(\widehat\gamma,\widehat u)$. Since $\operatorname{Im}\tau=L_T$ and $\operatorname{Im}\beta_c=-q_T$, the determinant conventions match exactly:

$$
D_c=-D_T/L_T,\qquad L_TD_c=-D_T.
$$

The metric is the induced, **unscaled** Euclidean quotient metric. In particular $\operatorname{sys}(Q_T)\ge T-C$, and radius-$R$ balls are Euclidean once $T-C>4R$. A parameter-dependent rescaling would describe a different metric assertion. The full formulas and their proofs are Paper III, `mapsIII:carrier-real-periods` (number `9.4`) and Paper III, `wb:cusp-spec-native-quotient` (number `9.5`).

### 4.3. Flat quotients, angle forgetting and retained angle

The working source also writes $J=X^\circ=f^{-1}(B^\circ)$ for the regular
family of complex Lie groups. This $J$ is a space, distinct from
$J_{\mathrm{rot}}$, $J_{\mathrm{swap}}$ and the Jacobian ideal.
The triangle deck group $\Delta$ of the chosen period cover
$\mathfrak h_z^\circ\to B^\circ$ is the image of the based fundamental group
under its deck representation. It is not identified with
$\pi_1(B^\circ)$. Equivalently one may use the universal cover and quotient
by $\pi_1(B^\circ)$. Monodromy invariants use the image representation,
while finite base covers correspond to subgroups of the fundamental group.
This is the corrected quotient convention in
Paper III, `wb:cusp-spec-globalization-obstruction` (number `9.6`).

The native flat quotient uses

$$
K_{\Lambda}=\mathbb Z\langle\widehat w,\widehat\delta\rangle,
\qquad
\alpha([z,\Pi(z)x])=[x\bmod K_{\Lambda}]
\in(\Lambda/K_{\Lambda})\otimes\mathbb R/\mathbb Z.
$$

It is normalized to zero on the specified zero section. The actual cusp deck generator has no additional affine translation in this chart. On the radial fibre, the fixed quotient torus $\mathbb R^2/\mathbb Z^2$ identifies with $Q_T$ by $[u]\mapsto[Y_Tu]$.

The invariant covector is $\varepsilon_\gamma=\gamma$, and
$L_\Lambda=\ker\varepsilon_\gamma
=\mathbb Z\langle\widehat u,\widehat w,\widehat\delta\rangle$.
The global regular-locus quotient and its circle coordinate have different
codomains:

$$
\chi_\gamma([z,\Pi(z)x])
  =([z],\varepsilon_\gamma(x)\bmod\mathbb Z)
  \in B^\circ\times(\mathbb R/\mathbb Z),\qquad
\theta_\gamma=\operatorname{pr}_{\mathbb R/\mathbb Z}\circ\chi_\gamma.
$$

On the cusp quotient let
$\chi_\gamma^{\mathrm{quot}}([x])
=\varepsilon_\gamma(x)\bmod\mathbb Z$.
There $\theta_\gamma=\chi_\gamma^{\mathrm{quot}}\circ\alpha$.
On the radial fibre its circle coordinate and induced quotient
circumference are

$$
\theta_{\gamma,T}([y])
 =\langle P_T^{-\mathsf T}e_\gamma,y\rangle\bmod\mathbb Z,\qquad
\ell_T=\frac1{\|P_T^{-\mathsf T}e_\gamma\|}
       =\frac{D_T}{\sqrt{L_T^2+m_T^2}},
\quad e_\gamma=(1,0,0,0)^{\mathsf T}.
$$

The source also denotes this restricted character by $\chi_{\gamma,T}$;
its base coordinate has been fixed. Its circle metric and the abstract
group $\mathbb R/\mathbb Z$ are separate data. See
Paper III, `wb:cusp-spec-global-circle-quotient` (number `31`) and
Paper III, `wb:cusp-spec-global-circle-circumference` (number `35`).

The angle-forgotten rank-two carrier has the local expression $[r,c(\alpha)]$, where $c$ collapses the coordinate one-skeleton of the quotient two-torus. The circle carrier is $[r,\chi_\gamma^{\mathrm{quot}}(\alpha)]$. Their completed maps and the retained-angle collapse have different targets and boundary identifications. The complete new extension proof makes both angle-forgotten one-copy carriers based nullhomotopic; it does not extend the literal flat character pointwise across the cusp. The retained-angle map $H:X\to S^4$ keeps the base-angle direction and represents the nonzero stable second-stem class. Its source theorem is consolidated at Paper III, `maps:src:B.3.1` (number `2.5`). These maps are never identified merely because they use the same torus or the same radial coordinate.

## 5. Paper II: conormal, normalization and conductor conventions

### 5.1. The three cotangent objects

For a reduced effective Cartier divisor $i:S\hookrightarrow Y$ in a smooth complex manifold, write $j:S_{\mathrm{reg}}\hookrightarrow S$ and put

$$
N^*=\mathcal O_Y(-S)|_S,\qquad V=\Omega_Y^1|_S,
\qquad T_{\Omega}=\ker(\Omega_S^1\longrightarrow j_*\Omega^1_{S_{\mathrm{reg}}}),
\qquad Q_{\Omega}=\Omega_S^1/T_{\Omega}.
$$

The CDP source writes $T,Q$ for the last two sheaves. $T_{\Omega}$ is torsion in the differential sheaf, not the tangent bundle $T_Y$. Set $K_{\Omega}=\ker(V\to Q_{\Omega})$. Then

$$
0\to N^*\to K_{\Omega}\to T_{\Omega}\to0,
\qquad 0\to K_{\Omega}\to V\to Q_{\Omega}\to0.
$$

The maps $\delta_A:H^0(T_{\Omega}\otimes A)\to H^1(N^*\otimes A)$ and $\partial_A:H^0(Q_{\Omega}\otimes A)\to H^1(K_{\Omega}\otimes A)$ are connecting maps for these different exact sequences. Here $A$ is an invertible analytic sheaf on $S$. A vanishing for the torsion-free quotient does not by itself remove the torsion kernel. The canonical criterion is Paper II, `cdp:st:A.1.1` (number `5.1`).

For a local reduced equation $F$, the Jacobian ideal is $\mathcal J=(F_{x_0},\ldots,F_{x_n})\subset\mathcal O_S$. Its inverse is the fractional ideal

$$
\mathcal J^{-1}=\{q\in\mathcal M_S:q\mathcal J\subset\mathcal O_S\},
$$

inside the total quotient sheaf, not an inverse line bundle asserted to be locally free. The identifications are $K_{\Omega}=N^*\otimes\mathcal J^{-1}$ and $T_{\Omega}=N^*\otimes(\mathcal J^{-1}/\mathcal O_S)$; see Paper II, `cdp:st:A.2.1` (number `5.2`).

### 5.2. Normalization, conductor and branch multiplicity

Write $\eta:\widetilde S\to S$ for finite analytic normalization and $\mathcal B=\eta_*\mathcal O_{\widetilde S}$. The conductor is

$$
\mathfrak c=\operatorname{Ann}_{\mathcal O_S}(\mathcal B/\mathcal O_S).
$$

It is an ideal on both sides of the normalization, with its actual scheme structure. A reduced double locus and the divisor or ideal carrying the conductor multiplicity are distinguished. For the reduced ordinary-crossing models $F=x,xy,xyz$, let $D_{\mathrm{sing}}=S_{\mathrm{sing,red}}$ and $\widetilde D=\eta^{-1}(D_{\mathrm{sing}})_{\mathrm{red}}$. The conductor square uses the difference map

$$
\eta_*\mathcal O_{\widetilde S}\oplus\mathcal O_{D_{\mathrm{sing}}}
\longrightarrow\eta_*\mathcal O_{\widetilde D},
\qquad(\widetilde h,k)\longmapsto\widetilde h|_{\widetilde D}-\eta^*k.
$$

This minus sign fixes the descent convention. At a triple point, the branches and their incidences are counted before quotient identifications; a self-crossing component is not a smooth component merely because its normalization is smooth. For a hypersurface surface in a smooth threefold, its dualizing sheaf $\omega_S$ is distinct from the sheaf $\Omega_S^2$ of Kähler forms. Normalization formulas retain the conductor divisor with its true multiplicities.

The inverse-Jacobian simple-pole statements for cusp, tacnode and ordinary-triple transverse types use respectively $x^2-y^3$, $x^2-y^4$, and $xy(x-y)$. Under the genus-one and constant-type hypotheses of Paper II, `cdp:st:C2d` (number `9.8`), normalization along the double curve has one branch, an étale two-branch cover, or an étale three-branch cover. Those covers need not split globally. In the tacnode jet the invariant numerator is $ac-b^2/4$, not an expression divided by the leading quadratic coefficient. The inverse-Jacobian convention is Paper II, `cdp:st:A.2.2` (number `5.3`).

### 5.3. Euler numbers, ranks and analytic categories

For a proper surjective holomorphic map $g:Y\to C$ from a connected compact complex manifold of dimension three to a compact Riemann surface, with connected general fibre a complex two-torus, let $\Sigma$ be a finite set containing the critical values. Then $e(Y)=\sum_{c\in\Sigma}e((Y_c)_{\mathrm{red}})$. In the stipulated unimodular periodic rank-two toric model, the quotient triangulation has $V-E+F=0$, $3F=2E$, and $e(S)=F=2V$; rank-one elliptic-ruled models have Euler number zero. These hypotheses do not imply that every singular fibre in an unrestricted torus fibration has nonnegative Euler number. The exact theorem, counterexample and model class are Paper II, `cdp:st:C2a` (number `9.5`), Paper II, `cdp:st:C2b` (number `9.6`), and Paper II, `cdp:st:C2c` (number `9.7`).

Throughout Paper II, a proper analytic map, an algebraic morphism and a formal degeneration are used with their stated categories. The analytic realization and compactness arguments printed for the toric models supply the comparison when a source theorem begins over a complete discrete valuation ring. A numerical divisor class, a holomorphic line bundle, a topologically trivial line bundle and an element of $\operatorname{Pic}^0$ remain different data.

## 6. Paper III: marked lattices, chains and normal orientations

### 6.1. Rank-six transpose and inverse conventions

The matrices printed as $A,B$ in the non-self-dual candidate Paper III, `maps:src:F.2.5` (number `6.8`) are used through

$$
M_1=A^{\mathsf T},\qquad M_2=B^{\mathsf T},\qquad
M_0=(M_1M_2)^{-1}
$$

on the ordered rank-six **homology** lattice. The cohomology **local-system monodromies** in the same positive loop directions are

$$
M_1^{-\mathsf T}=A^{-1},\qquad M_2^{-\mathsf T}=B^{-1}.
$$

These formulas are retained even where invariant-subspace dimensions happen to agree for $A$ and $A^{-1}$. Exterior powers are taken after this choice. A matrix $P\in\mathrm{GL}(6,\mathbb Z)$ in

$$
M_0P=P\begin{pmatrix}I_3&I_3\\0&I_3\end{pmatrix}
$$

records a primitive cusp marking. An algorithmically chosen $P$ is part of its output; it is not silently identified with a different prescribed marking. An upper triangular rank-three cusp matrix in homology and its inverse transpose in cohomology therefore describe the same marked geometry, with explicitly different actions.

### 6.2. Affine data, norm operators and clutching

A finite cap datum has an actual cyclic order $m_i$, homology matrix $M_i$, and affine generator

$$
\tau_i(x)=M_ix+v_i/m_i.
$$

The norm operator $N_m=I+M+\cdots+M^{m-1}$ is distinct from the nilpotent operator $N_{\mathrm{nil}}=M_0-I$. Freeness is checked for every nonidentity power of the actual affine action. An order, a root rotation and an affine numerator cannot be replaced by the order of the linear part alone. The finite cap's normal line may have torsion first Chern class, so vanishing in rational cohomology does not trivialize it.

For a rank-four finite cap with boundary affine generator $c$ and power vector $v$, the primitive normal circle is the group word

$$
\mu_{\mathrm{norm}}=c^m v^{-1}.
$$

Its additive notation on the covering cylinder is $m\theta-v$. Sweeping a fibre loop $\lambda$ produces the norm coordinate $N_m\lambda$ and fibre bivector $-\lambda\wedge v$; the minus sign is the marked normal-orientation convention. The affine generator contributes the torus of the commuting words $c$ and $c^m v^{-1}$. These are the full integral Thom columns of Paper III, `maps:src:D.2.29` (number `4.38`), including torsion cycles.

The regular-clutch integer $e$, the cusp clutch vector $\kappa$, and a mapping-class integer in $\Theta_7$ are separate quantities. In particular, changing affine boundary rigidifications can change a filled manifold even when the punctured torus bundle is unchanged.

### 6.3. Integral CW and bar-chain conventions

All chain matrices act on column coordinates; a matrix column is the image of its ordered basis generator. Boundaries lower degree. Cellular products use the chosen order of factors, and the actual attaching maps retain the deck and affine markings. Smith decompositions record unimodular $U,V$ with $UAV=D$. An image is not replaced by its saturation in a torsion calculation.

In the global fourfold chain model,

$$
\Gamma=\mathbb Z^6\rtimes F_k,\qquad
(x,w)(y,u)=(x+M(w)y,wu).
$$

For a group bar $[(x_1,w_1)|\cdots|(x_n,w_n)]$, the torus coordinates are $y_j=M(w_1\cdots w_{j-1})x_j$. The double-bar projection uses

$$
\sum_{p+q=n}(-1)^{pq}
[w_1|\cdots|w_p]\otimes[y_{p+1}|\cdots|y_n].
$$

The horizontal action is the **right action** $\rho(w)=M(w)^{-1}$, so $\rho(wu)=\rho(u)\rho(w)$, and the horizontal differential carries sign $(-1)^q$. After the stated contractions,

$$
C_n(E)=\bigwedge^n\mathbb Z^6\oplus
\bigoplus_i\bigwedge^{n-1}\mathbb Z^6,
\quad
d(e_i\otimes\xi)=(-1)^{n-1}
(\bigwedge^{n-1}M_i^{-1}-I)\xi.
$$

This short differential does not replace the full projection or boundary inclusion: their higher finite perturbation terms remain in the certificate. The finite-cap mapping-torus convention uses $M_i$, while the complement right-action convention uses $M_i^{-1}$; the recorded comparison maps connect them. The complete construction is Paper III, `maps:src:F.2.35` (number `6.40`).

### 6.4. Other six-manifold symbols

| Symbol | Fixed interpretation in its stated construction |
|---|---|
| $p=12l_0-4l_1-3l_2$, $d=\lvert p\rvert$ | Signed twist invariant and positive covering degree. $p_j$ denotes a marked base point, while $p_1(TX)$ is a Pontryagin class. |
| $G$, $P=aG$, $Q=bG$, $d_0$ | Mordell–Weil generator, section multiples, and denominator determined by $\langle G,G\rangle=1/d_0$. |
| $D_{\mathrm{vert}}$, $M_D=\mathcal O(P-O+D_{\mathrm{vert}})$ | Actual integral vertical correction and corrected line bundle. |
| $J_{\mathrm{int}}$ | Intersection matrix of fibre components, with its primitive multiplicity vector as kernel; the source often writes $J$. |
| $\sigma_{\mathrm{comp}}$ | Component permutation induced by section translation; unrelated to a signature or an antiholomorphic involution. |
| $\mathfrak p$ with $4\mathfrak p=\operatorname{PD}(p_1)$ | The normalized integral characteristic coordinate in the stated six-dimensional classification, retaining its defining divisibility hypotheses. |
| $\mu$ in a six-dimensional classification | Cubic cup-product form, distinguished by its arguments from the elliptic logarithm and the seven-dimensional invariant $\mu_{EK}$. |

For the corrected initial line, the local equation is

$$
(\sigma_{\mathrm{comp}}-I)J_{\mathrm{int}}z
=-(\sigma_{\mathrm{comp}}-I)(e_p-e_0).
$$

It is an integral equation. The height-integral condition, corrected punctured monodromy and additional fully filled examples have their separate statements; no unsupplied original cap is inferred from the existence of a corrected line bundle. See Paper III, `maps:src:D.2.50` (number `4.59`) and Paper III, `maps:src:D.2.52` (number `4.61`).

## 7. Stable framings, spin structures and seven-dimensional invariants

### 7.1. Orientation and Pontryagin–Thom convention

Complex manifolds carry their complex orientation. A boundary uses the outward-normal-first convention. In a Pontryagin–Thom comparison the ordered normal frame precedes the tangent frame; outward stabilization is retained. A constant permutation of frame vectors is corrected once so the full frame has the stipulated orientation. Comparing a chart frame with the sphere frame is done on the actual contractible chart, not by assuming the whole complex tangent bundle is trivial.

At the fixed sphere, conjugating one complex normal coordinate reverses the real normal orientation. The surgery comparison simultaneously reverses the model $S^2$ orientation so that the ambient six-dimensional orientation is preserved; see Paper III, `maps:src:D.2.14` (number `4.23`) and the explicit local tubular model in that proof. Normal-frame changes and homology basis changes are different operations.

For a spin surface, the quadratic refinement assigns zero to a bounding induced spin circle and one to a nonbounding one. In Johnson's unit-tangent-bundle model the lift of a curve includes the fibre-class correction. Thus the quadratic value is not the raw spin-class evaluation on its tangential lift. For the Lie-framed two-torus,

$$
q(e)=q(f)=1,\quad e\cdot f=1,\quad
q(xe+yf)=x+xy+y,\quad\operatorname{Arf}=1.
$$

This intrinsic calculation is already Debray and Gunningham's Example 3.8 (2018). The receiving proof separately identifies the actual differential framing with that Lie framing. Forgetting a framed bordism gives a spin bordism; no unrestricted injectivity of framed-to-spin bordism is assumed.

### 7.2. Hopf and stable-stem generators

The conventions are

$$
\pi_3^{\mathrm S}=\mathbb Z/24\langle\nu\rangle,
\quad e_{\mathbb R}(\nu)=1/24,
\quad \pi_6(S^3)=\mathbb Z/12\langle\nu'\rangle,
\quad \operatorname{stab}(\nu')=2\nu.
$$

The map $\eta_n:S^{n+1}\to S^n$ is the $(n-2)$-fold suspension of the complex Hopf map. The Lie-framed circle represents stable $\eta$, the Lie-framed two-torus represents $\eta^2\ne0\in\pi_2^{\mathrm S}=\mathbb Z/2$, and the Lie-framed three-torus represents $\eta^3=12\nu$. Consequently the order-two unstable class in the Engel-map calculation is $6\nu'$, with stable class $12\nu$. Source or target orientation reversal does not change these order-two classes. The real Adams invariant used here is not silently replaced by the complex Adams invariant. See Paper III, `maps:src:B.1.2` (number `2.3`) and Paper III, `maps:src:B.3.1` (number `2.5`); the exact original reference scopes are recorded under `Pontryagin1950Root`, `Pontryagin1955Root`, `Johnson1980Root`, `DebrayGunningham2018Root`, and `Hatcher2002`.

### 7.3. Mapping torus and Eells–Kuiper normalization

The mapping torus is defined by $(z,1)\sim(\Phi(z),0)$, with the positive family-parameter orientation on the circle. Its oriented comparison is $(S^6\times S^1)\#\Sigma_\Phi$. The generator of

$$
\pi_0\operatorname{Diff}^+(S^6)\cong\Theta_7\cong\mathbb Z/28
$$

is chosen to have $\mu_{EK}=1/28\pmod{\mathbb Z}$. In the sphere-bundle normalization it has Euler evaluation one, Pontryagin evaluation six, $p_1^2=36$, and signature one, giving $(36-4)/896=1/28$.

For the stipulated spin coboundary $W^8$, the normalization is

$$
\mu_{EK}(\partial W)
=\frac{\langle p_1(W)^2,[W,\partial W]\rangle-4\sigma(W)}{896}
\pmod{\mathbb Z},
$$

with the relative lifts supplied by the receiving proof. In the corresponding spin-$c$ formula, for determinant class $z$ and its required relative lift,

$$
\mu_{EK}=
\frac{p_1^2-4\sigma}{896}
-\frac{p_1z^2}{192}+\frac{z^4}{384}\pmod{\mathbb Z}.
$$

The published Crowley–Nordström convention is converted by dividing its invariant by $28$ and substituting $\widehat p=(p_1+z^2)/2$, with its original hypotheses retained. Boundary orientation reversal negates $\mu_{EK}$. The exact normalizations and mapping-torus comparison are Paper III, `push:src:C.1.1` (number `A.11`), Paper III, `push:src:C.1.2` (number `A.12`), and Paper III, `push:src:C.2.1` (number `A.13`). A framing integer, an orbit-knot integer and this residue class are related only by the explicitly proved comparison; equivariance alone does not determine the residue.

## 8. Shared statements and source-name ownership

### 8.1. Main consolidated statements

| Mathematical statement | Common destination |
|---|---|
| Parameter classification | Paper I, `fam:src:A.5.1` (number `3.8`) |
| Tangent cohomology, Kodaira–Spencer map and reduced Kuranishi line | Paper I, `fam:src:A.5.2` (number `3.9`) |
| Canonical-pencil statement | Paper I, `fam:src:A.1.1` (number `3.1`) |
| Exact maximum, retaining independent interval, duplication and radial arguments | Paper I, `fam:src:C.2.3` (number `5.5`) |
| Expanded working Hodge-line proof | Paper I, `mapsI:hodge:line` (number `L.1`) |
| Finite normal-order calculation | Paper I, `wb:ffcert:thm:normal-trivialization` (number `C.15`) |
| Structure-sheaf direct images and the complete cusp cup calculation | Paper I, `inv:A1.0` (number `8.1`) |
| Picard restriction and primitive global fibre-class extension | Paper I, `inv:C3.1` (number `10.5`); Paper I, `inv:A3.2` (number `8.10`) |
| Bott–Chern product calculation | Paper I, `inv:C3.3` (number `10.7`) |
| Complete conormal filtration | Paper II, `cdp:st:A.1.1` (number `5.1`) |
| Actual retained-angle map | Paper III, `maps:src:B.3.1` (number `2.5`) |

Multiple source rows can share one statement while retaining their distinct complete proofs. A label alias records that consolidation. It does not identify merely similar statements with different hypotheses. The appendix resolves older intermediate `fam:st:` aliases to the current canonical `fam:src:` destination whenever the current inventory supplies it.

### 8.2. Namespaces

| Source family | Common printed namespace |
|---|---|
| FAMILY | `fam:src:` for result identifiers; `fam:` for retained local labels. |
| PUSH | `push:src:` for result identifiers; `push:` or the specified shared proof namespace for local labels. |
| INVARIANTS / ARITHMETIC Part C | `inv:` / `ari:`. |
| CDP | `cdp:st:` and retained `cdp:` local labels; shared Paper I statements use their actual destination. |
| MAPS in Paper I / III | `mapsI:` / `maps:src:` and the stated `maps:`, `mapsIII:` or `mapsD:` proof labels. |
| Working edition | `wb:`, `wbII:`, or the explicit `inv:`, `mapsI:`, `maps:` or `cdp:` consolidation. |
| Course providers and writing repairs | Their explicit `courseIII:`, `mapsaudit:`, `mapsD:` or other recorded labels; the complete inventory gives each exact destination. |

### 8.3. R-items in the MAPS prompt

The following R-register belongs specifically to `sources/prompts/S6_04_MAPS_MANIFOLDS/PROMPT.md`. An R-number in another prompt or a local arithmetic subsection is not imported into this register.

| Historical item | Actual source statements |
|---|---|
| R1, family classification | FAMILY A.5.1, B.2.1, C.2.3; the exact period subgroup is also DGKX version 1, Theorem 1.4. |
| R2, automorphisms and invariant lattices | FAMILY B.4.1, C.4.1, A.2.1. |
| R3, conjugation and real structures | FAMILY B.4.2. |
| R4, higher multiplicity classification | FAMILY B.3.1; the missing coordinate adapter is supplied by PUSH E.1.1–E.1.2. |
| R5, coherent shifts and positive parameter loop | FAMILY A.3.1 and E.2.2, supplemented by the complete PUSH C.3.5 closing cocycle in Paper I. |
| R6, compact curves and surfaces | FAMILY D.2.1–D.2.2. |

### 8.4. K-items inherited by MAPS from checkpoint 01

The source is `sources/per_prompt/S6_04_MAPS_MANIFOLDS/S6_CHECKPOINT_01_20261115.md`. These are historical input names, not new MAPS theorem numbers. Their present results and proofs carry the full destinations below; historical open statuses are not current claims.

| Historical item | Actual source owner and identifiers | Present location |
|---|---|---|
| K1 | PUSH E.1.1–E.1.2, coordinate dictionary and higher-twist criterion | Paper I, `push:src:E.1.1` (number `23.1`); Paper I, `push:src:E.1.2` (number `23.2`) |
| K2 | PUSH E.1.3, C.4.1, holomorphic comparison and twist-family monodromy | Paper I, `push:src:E.1.3` (number `23.3`); Paper III, `push:src:C.4.1` (number `7.35`) |
| K3 | PUSH C.1.1, C.1.2, C.2.1, seven-dimensional normalizations | Paper III, `push:src:C.1.1` (number `A.11`); Paper III, `push:src:C.1.2` (number `A.12`); Paper III, `push:src:C.2.1` (number `A.13`) |
| K4 | PUSH C.3.1, fixed sphere and normal weights | Paper III, `push:src:C.3.1` (number `A.14`) |
| K5 | PUSH C.3.2, scalar-gauge obstruction | Paper III, `push:src:C.3.2` (number `7.3`) |
| K6 | PUSH C.3.3, equivariant representatives of all sphere mapping classes | Paper III, `push:src:C.3.3` (number `A.15`) |
| K7 | PUSH C.3.4, two historical residues after base change | Paper III, `push:src:C.3.4` (number `7.4`) |
| K8 | PUSH C.3.5, exact coherent closing translation | Paper I, `push:src:C.3.5` (number `18.5`) |
| K9 | PUSH C.4.2, antiholomorphic symmetry and orientation | Paper III, `push:src:C.4.2` (number `7.36`) |
| K10 | Historical value question PUSH C.5.1 | Paper III, `push:src:C.5.1` (number `7.37`); final computations Paper III, `push:src:C.3.24` (number `7.28`) and Paper III, `push:src:C.3.27` (number `7.32`) |
| K11 | PUSH E.5.1–E.5.3, two-parameter family and corrected degeneration orders | Paper II, `push:src:E.5.1` (number `16.32`); Paper II, `push:src:E.5.2` (number `16.33`); Paper II, `push:src:E.5.3` (number `16.34`) |
| K12 | PUSH E.2.1–E.2.3, tangent calculations and multiplicity constancy | Paper I, `push:src:E.2.1` (number `23.4`); Paper I, `push:src:E.2.2` (number `23.5`); Paper I, `push:src:E.2.3` (number `23.6`) |
| K13 | PUSH A.1.1, A.1.2, A.2.1, A.2.2, A.4.1, A.4.2, untwisted geometry and plumbing | Paper I, `push:src:A.1.1` (number `20.1`); Paper I, `push:src:A.1.2` (number `20.2`); Paper I, `push:src:A.2.1` (number `20.3`); Paper I, `push:src:A.2.2` (number `20.4`); Paper I, `push:src:A.4.1` (number `20.11`); Paper I, `push:src:A.4.2` (number `20.12`) |
| K14 | CDP D.1.6 and D.1.13, Wang-family integral and positivity corrections | Paper II, `cdp:st:D.1.6` (number `3.3`); Paper II, `cdp:st:D.1.13` (number `3.11`) |
| K15 | CDP C2a–C2c, Euler localization, counterexample and toric model class | Paper II, `cdp:st:C2a` (number `9.5`); Paper II, `cdp:st:C2b` (number `9.6`); Paper II, `cdp:st:C2c` (number `9.7`) |
| K16 | CDP E6, E7, E13–E15, fibration deformations and tangent calculations | Paper II, `cdp:st:E6` (number `15.2`); Paper II, `cdp:st:E7` (number `15.3`); Paper II, `cdp:st:E13` (number `15.8`); Paper II, `cdp:st:E14` (number `15.9`); Paper II, `cdp:st:E15` (number `15.10`) |

In particular, the strings “K13, A.2.2” and “K1, E.1.2” refer to **PUSH**, even when embedded inside a MAPS proof. Applying a local MAPS prefix to those strings changes the reference's mathematical meaning. The corrected ownership is also recorded in `work/root/III_prompt_alias_corrections.json`.

### 8.5. The separate arithmetic checkpoint register

The arithmetic checkpoint has a different K-register. Its source is the table in
sources/per_prompt/S6_05_ARITHMETIC/S6_CHECKPOINT_01_20261115.md.
In particular its K1 is the special theta norm, while the MAPS checkpoint K1
is the higher-twist coordinate dictionary. The Paper I editorial corrections
replace these arithmetic checkpoint names by the exact results below.

| Arithmetic checkpoint item | Actual source owner and destination |
|---|---|
| K1, isogeny product and special theta norm | Paper I, `push:src:D.4.5` (number `22.14`); the complete general product and phase calculations are Paper I, `ari:C.1.1` (number `12.1`) and Paper I, `ari:C.1.2` (number `12.2`). |
| K2, second Albanese nome and boundary | Paper I, `push:src:D.1.1` (number `22.1`); Paper I, `push:src:D.1.2` (number `22.2`); Paper I, `push:src:D.1.3` (number `22.3`). |
| K3, half-period and boundary expansion | Paper I, `push:src:D.2.1` (number `22.4`); the additional fourth-order terms are Paper I, `ari:C.3.1` (number `12.6`). |
| K4, differentiated theta norm | Paper I, `push:src:D.4.4` (number `22.13`); the full first-derivative rederivation is Paper I, `ari:C.8.11` (number `14.10`). The associated checkpoint's global critical-point question is a historical question, not an extra theorem. |
| K5, degeneracy levels and rank-three closure | Paper I, `push:src:D.4.1` (number `22.10`); Paper I, `push:src:D.4.2` (number `22.11`); Paper I, `push:src:D.4.3` (number `22.12`). |
| K6, independent interval and covering certificate | Paper I, `push:src:E.4.1` (number `23.10`); Paper I, `push:src:E.4.2` (number `23.11`); Paper I, `fam:src:C.2.3` (number `5.5`). |
| K7, cotangent rank divisor | Paper II, `cdp:st:E16` (number `15.11`); Paper II, `cdp:st:E8` (number `15.4`). |

The published condition called (K1) in Chen's degeneration theorem and the
name “K3 surface” are separate mathematical uses. Neither is a checkpoint
alias.

## 9. How to read and regenerate the concordance

The result key is the pair **(source run, source identifier)**. Case in the source-run field is preserved: for example `WORKING_EDITION`, `working_edition`, and `WORKING_INV` identify different inventory inputs. Each inventory row appears once in Appendix A. Shared destinations are expected, while a missing destination is a validation failure.

Appendix B records explicit statement and equation aliases from the scoped audit files. Appendix C lists all labels actually present in the assembled TeX files, including equation, proof and section labels. Its number is the current auxiliary-file value; an unnumbered label stays identified by its exact key. The generator never invents a number from source order.

Run from the package root:

```bash
python code/invariants_arithmetic/build_all_papers_notation.py --numbers
```

In the full workspace the equivalent command is `python deliverables/code/invariants_arithmetic/build_all_papers_notation.py --numbers`. Run it after the final inventory and AUX refresh. Omitting `--numbers` produces a label-only snapshot. It updates this Markdown deliverable and its own machine-readable concordance audit, and does not modify the inventory or any manuscript.

The binding source scopes for this expansion are FAMILY `sections/conventions.tex`; the checked invariant/arithmetic notation dictionary; CDP `build/ordered/A.tex`, C2a–C2d and the complete working supplement; `carrier_radial_prerequisites.tex`; MAPS `maps_B.tex`, D.2.29, D.2.50–D.2.52, F.2.5 and the global-chain proof F.2.35; and the exact PUSH C.1–C.2 normalization statements. Their hashes and locators are recorded in `work/invariants_arithmetic/notation_source_checks.json`.


## Appendix A. Every inventory result and its actual destination

Numbers below are the available AUX values in this recorded snapshot.

| Source run | Original result identifier | Paper | Printed label | Current number |
|---|---|---|---|---|
| `S6_01_INVARIANTS` | `A1.0` | I | `inv:A1.0` | `8.1` |
| `S6_01_INVARIANTS` | `A1.1` | I | `inv:A1.1` | `8.2` |
| `S6_01_INVARIANTS` | `A1.2` | I | `inv:A1.2` | `8.3` |
| `S6_01_INVARIANTS` | `A1.3` | I | `inv:A1.3` | `8.4` |
| `S6_01_INVARIANTS` | `A2.1` | I | `inv:A2.1` | `8.5` |
| `S6_01_INVARIANTS` | `A2.2` | I | `inv:A2.2` | `8.6` |
| `S6_01_INVARIANTS` | `A2.3` | I | `inv:A2.3` | `8.7` |
| `S6_01_INVARIANTS` | `A2.4` | I | `inv:A2.4` | `8.8` |
| `S6_01_INVARIANTS` | `A3.1` | I | `inv:A3.1` | `8.9` |
| `S6_01_INVARIANTS` | `A3.2` | I | `inv:A3.2` | `8.10` |
| `S6_01_INVARIANTS` | `A4.1` | I | `inv:A4.1` | `8.11` |
| `S6_01_INVARIANTS` | `A4.2` | I | `inv:A4.2` | `8.12` |
| `S6_01_INVARIANTS` | `B1.0` | I | `inv:B1.0` | `9.1` |
| `S6_01_INVARIANTS` | `B1.1` | I | `inv:B1.1` | `9.2` |
| `S6_01_INVARIANTS` | `B1.2` | I | `inv:B1.2` | `9.3` |
| `S6_01_INVARIANTS` | `B2.1` | I | `inv:B2.1` | `9.4` |
| `S6_01_INVARIANTS` | `B2.2` | I | `inv:B2.2` | `9.5` |
| `S6_01_INVARIANTS` | `B3.1` | I | `inv:B3.1` | `9.6` |
| `S6_01_INVARIANTS` | `B3.2` | I | `inv:B3.2` | `9.7` |
| `S6_01_INVARIANTS` | `B3.3` | I | `inv:B3.3` | `9.8` |
| `S6_01_INVARIANTS` | `C1.1` | I | `inv:C1.1` | `10.1` |
| `S6_01_INVARIANTS` | `C1.2` | I | `inv:C1.2` | `10.2` |
| `S6_01_INVARIANTS` | `C2.1` | I | `inv:C2.1` | `10.3` |
| `S6_01_INVARIANTS` | `C2.2` | I | `inv:C2.2` | `10.4` |
| `S6_01_INVARIANTS` | `C3.1` | I | `inv:C3.1` | `10.5` |
| `S6_01_INVARIANTS` | `C3.2` | I | `inv:C3.2` | `10.6` |
| `S6_01_INVARIANTS` | `C3.3` | I | `inv:C3.3` | `10.7` |
| `S6_01_INVARIANTS` | `C3.4` | I | `inv:C3.4` | `10.8` |
| `S6_01_INVARIANTS` | `C3.5` | I | `inv:C3.5` | `10.9` |
| `S6_01_INVARIANTS` | `C3.6` | I | `inv:C3.6` | `10.10` |
| `S6_01_INVARIANTS` | `C3.7` | I | `inv:C3.7` | `10.11` |
| `S6_01_INVARIANTS` | `C3.8` | I | `inv:C3.8` | `T.3` |
| `S6_01_INVARIANTS` | `D1.1` | I | `inv:D1.1` | `Q.1` |
| `S6_01_INVARIANTS` | `D1.2` | I | `inv:D1.2` | `Q.2` |
| `S6_01_INVARIANTS` | `D1.3` | I | `fam:st:A.5.2` | `3.9` |
| `S6_01_INVARIANTS` | `D2.1` | I | `fam:st:A.5.2` | `3.9` |
| `S6_01_INVARIANTS` | `D3.1` | I | `fam:st:A.5.2` | `3.9` |
| `S6_01_INVARIANTS` | `D4.1` | I | `inv:D4.1` | `11.1` |
| `S6_01_INVARIANTS` | `D4.2` | I | `inv:D4.2` | `11.2` |
| `S6_01_INVARIANTS` | `D4.3` | I | `inv:D4.3` | `11.3` |
| `S6_01_INVARIANTS` | `D4.4` | I | `inv:D4.4` | `11.4` |
| `S6_01_INVARIANTS` | `D4.5` | I | `inv:D4.5` | `11.5` |
| `S6_01_INVARIANTS` | `E1.1` | II | `inv:E1.1` | `17.1` |
| `S6_01_INVARIANTS` | `E2.1` | II | `inv:E2.1` | `A.11` |
| `S6_01_INVARIANTS` | `E2.2` | II | `inv:E2.2` | `17.2` |
| `S6_01_INVARIANTS` | `E2.3` | II | `inv:E2.3` | `D.1` |
| `S6_01_INVARIANTS` | `E2.4` | II | `inv:E2.4` | `17.3` |
| `S6_02_FAMILY` | `A.1.1` | I | `fam:src:A.1.1` | `3.1` |
| `S6_02_FAMILY` | `A.1.2` | I | `fam:src:A.1.2` | `3.2` |
| `S6_02_FAMILY` | `A.2.1` | I | `fam:src:A.2.1` | `3.3` |
| `S6_02_FAMILY` | `A.3.1` | I | `fam:src:A.3.1` | `3.4` |
| `S6_02_FAMILY` | `A.4.1` | I | `fam:src:A.4.1` | `3.5` |
| `S6_02_FAMILY` | `A.4.2` | I | `fam:src:A.4.2` | `3.6` |
| `S6_02_FAMILY` | `A.4.3` | I | `fam:src:A.4.3` | `3.7` |
| `S6_02_FAMILY` | `A.5.1` | I | `fam:src:A.5.1` | `3.8` |
| `S6_02_FAMILY` | `A.5.2` | I | `fam:src:A.5.2` | `3.9` |
| `S6_02_FAMILY` | `B.1.1` | I | `fam:src:B.1.1` | `4.1` |
| `S6_02_FAMILY` | `B.1.2` | I | `fam:src:B.1.2` | `4.2` |
| `S6_02_FAMILY` | `B.1.3` | I | `fam:src:B.1.3` | `4.3` |
| `S6_02_FAMILY` | `B.1.4` | I | `fam:src:B.1.4` | `4.4` |
| `S6_02_FAMILY` | `B.2.1` | I | `fam:src:B.2.1` | `4.5` |
| `S6_02_FAMILY` | `B.2.2` | I | `fam:src:B.2.2` | `4.6` |
| `S6_02_FAMILY` | `B.2.3` | I | `fam:src:B.2.3` | `4.7` |
| `S6_02_FAMILY` | `B.3.1` | I | `fam:src:B.3.1` | `4.8` |
| `S6_02_FAMILY` | `B.4.1` | I | `fam:src:B.4.1` | `4.9` |
| `S6_02_FAMILY` | `B.4.2` | I | `fam:src:B.4.2` | `4.10` |
| `S6_02_FAMILY` | `C.1.1` | I | `fam:src:C.1.1` | `5.1` |
| `S6_02_FAMILY` | `C.1.2` | I | `fam:src:C.1.2` | `5.2` |
| `S6_02_FAMILY` | `C.2.1` | I | `fam:src:C.2.1` | `5.3` |
| `S6_02_FAMILY` | `C.2.2` | I | `fam:src:C.2.2` | `5.4` |
| `S6_02_FAMILY` | `C.2.3` | I | `fam:src:C.2.3` | `5.5` |
| `S6_02_FAMILY` | `C.3.1` | I | `fam:src:C.3.1` | `5.6` |
| `S6_02_FAMILY` | `C.3.2` | I | `fam:src:C.3.2` | `5.7` |
| `S6_02_FAMILY` | `C.3.3` | I | `fam:src:C.3.3` | `5.8` |
| `S6_02_FAMILY` | `C.3.4` | I | `fam:src:C.3.4` | `5.9` |
| `S6_02_FAMILY` | `C.4.1` | I | `fam:src:C.4.1` | `5.10` |
| `S6_02_FAMILY` | `D.1.1` | I | `fam:src:D.1.1` | `6.1` |
| `S6_02_FAMILY` | `D.1.2` | I | `fam:src:D.1.2` | `6.2` |
| `S6_02_FAMILY` | `D.1.3` | I | `fam:src:D.1.3` | `6.3` |
| `S6_02_FAMILY` | `D.1.4` | I | `fam:src:D.1.4` | `6.4` |
| `S6_02_FAMILY` | `D.1.5` | I | `fam:src:D.1.5` | `6.5` |
| `S6_02_FAMILY` | `D.1.6` | I | `fam:src:D.1.6` | `6.6` |
| `S6_02_FAMILY` | `D.1.7` | I | `fam:src:D.1.7` | `6.7` |
| `S6_02_FAMILY` | `D.2.1` | I | `fam:src:D.2.1` | `6.8` |
| `S6_02_FAMILY` | `D.2.2` | I | `fam:src:D.2.2` | `6.9` |
| `S6_02_FAMILY` | `D.2.3` | I | `fam:src:D.2.3` | `6.10` |
| `S6_02_FAMILY` | `E.1.1` | I | `fam:src:E.1.1` | `19.1` |
| `S6_02_FAMILY` | `E.1.2` | I | `fam:src:E.1.2` | `19.2` |
| `S6_02_FAMILY` | `E.1.3` | I | `fam:src:E.1.3` | `19.3` |
| `S6_02_FAMILY` | `E.1.4` | I | `fam:src:E.1.4` | `19.4` |
| `S6_02_FAMILY` | `E.1.5` | I | `fam:src:E.1.5` | `19.5` |
| `S6_02_FAMILY` | `E.2.1` | I | `fam:src:E.2.1` | `19.6` |
| `S6_02_FAMILY` | `E.2.2` | III | `fam:src:E.2.2` | `8.1` |
| `S6_02_FAMILY` | `E.2.3` | III | `fam:src:E.2.3` | `8.2` |
| `S6_02_FAMILY` | `F.1.1` | I | `fam:src:F.1.1` | `7.1` |
| `S6_02_FAMILY` | `F.1.2` | I | `fam:src:F.1.2` | `7.2` |
| `S6_02_FAMILY` | `F.2.1` | I | `fam:src:F.2.1` | `7.3` |
| `S6_02_FAMILY` | `F.2.2` | I | `fam:src:F.2.2` | `7.4` |
| `S6_02_FAMILY` | `F.2.3` | I | `fam:src:F.2.3` | `7.5` |
| `S6_02_FAMILY` | `F.3.1` | I | `fam:src:F.3.1` | `7.6` |
| `S6_02_FAMILY` | `F.3.2` | I | `fam:src:F.3.2` | `7.7` |
| `S6_02_FAMILY` | `F.3.3` | I | `fam:src:F.3.3` | `7.8` |
| `S6_02_PUSH` | `A.1.1` | I | `push:src:A.1.1` | `20.1` |
| `S6_02_PUSH` | `A.1.2` | I | `push:src:A.1.2` | `20.2` |
| `S6_02_PUSH` | `A.2.1` | I | `push:src:A.2.1` | `20.3` |
| `S6_02_PUSH` | `A.2.2` | I | `push:src:A.2.2` | `20.4` |
| `S6_02_PUSH` | `A.2.3` | I | `push:src:A.2.3` | `20.5` |
| `S6_02_PUSH` | `A.2.4` | I | `push:src:A.2.4` | `20.6` |
| `S6_02_PUSH` | `A.2.5` | I | `push:src:A.2.5` | `20.7` |
| `S6_02_PUSH` | `A.3.1` | I | `push:src:A.3.1` | `20.8` |
| `S6_02_PUSH` | `A.3.2` | I | `push:src:A.3.2` | `20.9` |
| `S6_02_PUSH` | `A.3.3` | I | `push:src:A.3.3` | `20.10` |
| `S6_02_PUSH` | `A.4.1` | I | `push:src:A.4.1` | `20.11` |
| `S6_02_PUSH` | `A.4.2` | I | `push:src:A.4.2` | `20.12` |
| `S6_02_PUSH` | `A.4.3` | I | `push:src:A.4.3` | `20.13` |
| `S6_02_PUSH` | `A.4.4` | I | `push:src:A.4.4` | `20.14` |
| `S6_02_PUSH` | `A.4.5` | I | `push:src:A.4.5` | `20.15` |
| `S6_02_PUSH` | `A.4.6` | I | `push:src:A.4.6` | `20.16` |
| `S6_02_PUSH` | `A.4.7` | I | `push:src:A.4.7` | `20.17` |
| `S6_02_PUSH` | `A.4.8` | I | `push:src:A.4.8` | `20.18` |
| `S6_02_PUSH` | `A.4.9` | I | `push:src:A.4.9` | `20.19` |
| `S6_02_PUSH` | `B.1.1` | I | `push:src:B.1.1` | `21.1` |
| `S6_02_PUSH` | `B.1.2` | I | `push:src:B.1.2` | `21.2` |
| `S6_02_PUSH` | `B.2.1` | I | `push:src:B.2.1` | `21.3` |
| `S6_02_PUSH` | `B.2.2` | I | `push:src:B.2.2` | `21.4` |
| `S6_02_PUSH` | `B.2.3` | I | `push:src:B.2.3` | `21.5` |
| `S6_02_PUSH` | `B.3.1` | I | `push:src:B.3.1` | `21.6` |
| `S6_02_PUSH` | `B.3.2` | I | `push:src:B.3.2` | `21.7` |
| `S6_02_PUSH` | `B.3.3` | I | `push:src:B.3.3` | `21.8` |
| `S6_02_PUSH` | `B.3.4` | I | `push:src:B.3.4` | `21.9` |
| `S6_02_PUSH` | `B.3.5` | I | `push:src:B.3.5` | `21.10` |
| `S6_02_PUSH` | `B.3.6` | I | `push:src:B.3.6` | `21.11` |
| `S6_02_PUSH` | `B.3.7` | I | `push:src:B.3.7` | `21.12` |
| `S6_02_PUSH` | `B.3.8` | I | `push:src:B.3.8` | `21.13` |
| `S6_02_PUSH` | `B.4.1` | I | `push:src:B.4.1` | `21.14` |
| `S6_02_PUSH` | `B.4.2` | I | `push:src:B.4.2` | `21.15` |
| `S6_02_PUSH` | `B.4.3` | I | `push:src:B.4.3` | `21.16` |
| `S6_02_PUSH` | `B.4.4` | I | `push:src:B.4.4` | `21.17` |
| `S6_02_PUSH` | `B.4.5` | I | `push:src:B.4.5` | `21.18` |
| `S6_02_PUSH` | `B.4.6` | I | `push:src:B.4.6` | `21.19` |
| `S6_02_PUSH` | `B.4.7` | I | `push:src:B.4.7` | `21.20` |
| `S6_02_PUSH` | `B.4.8` | I | `push:src:B.4.8` | `21.23` |
| `S6_02_PUSH` | `B.4.9` | I | `push:src:B.4.9` | `21.25` |
| `S6_02_PUSH` | `B.4.10` | I | `push:src:B.4.10` | `21.26` |
| `S6_02_PUSH` | `B.4.11` | I | `push:src:B.4.11` | `21.28` |
| `S6_02_PUSH` | `B.4.12` | I | `push:src:B.4.12` | `21.29` |
| `S6_02_PUSH` | `B.4.13` | I | `push:src:B.4.13` | `21.30` |
| `S6_02_PUSH` | `B.4.14` | I | `push:src:B.4.14` | `21.32` |
| `S6_02_PUSH` | `B.4.15` | I | `push:src:B.4.15` | `21.33` |
| `S6_02_PUSH` | `B.4.16` | I | `push:src:B.4.16` | `21.35` |
| `S6_02_PUSH` | `B.4.17` | I | `push:src:B.4.17` | `21.36` |
| `S6_02_PUSH` | `B.4.18` | I | `push:src:B.4.18` | `21.38` |
| `S6_02_PUSH` | `B.4.19` | I | `push:src:B.4.19` | `21.40` |
| `S6_02_PUSH` | `B.4.20` | I | `push:src:B.4.20` | `21.41` |
| `S6_02_PUSH` | `B.4.21` | I | `push:src:B.4.21` | `21.42` |
| `S6_02_PUSH` | `B.4.22` | I | `push:src:B.4.22` | `21.43` |
| `S6_02_PUSH` | `B.4.23` | I | `push:src:B.4.23` | `21.44` |
| `S6_02_PUSH` | `B.4.24` | I | `push:src:B.4.24` | `21.45` |
| `S6_02_PUSH` | `B.4.25` | I | `push:src:B.4.25` | `21.46` |
| `S6_02_PUSH` | `B.4.26` | I | `push:src:B.4.26` | `21.48` |
| `S6_02_PUSH` | `B.4.27` | I | `push:src:B.4.27` | `21.49` |
| `S6_02_PUSH` | `B.4.28` | I | `push:src:B.4.28` | `21.50` |
| `S6_02_PUSH` | `B.4.29` | I | `push:src:B.4.29` | `21.52` |
| `S6_02_PUSH` | `B.4.30` | I | `push:src:B.4.30` | `21.53` |
| `S6_02_PUSH` | `B.4.31` | I | `push:src:B.4.31` | `21.54` |
| `S6_02_PUSH` | `B.4.32` | I | `push:src:B.4.32` | `21.56` |
| `S6_02_PUSH` | `B.4.33` | I | `push:src:B.4.33` | `21.58` |
| `S6_02_PUSH` | `B.5.1` | I | `push:src:B.5.1` | `21.59` |
| `S6_02_PUSH` | `C.1.1` | III | `push:src:C.1.1` | `A.11` |
| `S6_02_PUSH` | `C.1.2` | III | `push:src:C.1.2` | `A.12` |
| `S6_02_PUSH` | `C.2.1` | III | `push:src:C.2.1` | `A.13` |
| `S6_02_PUSH` | `C.2.2` | III | `push:src:C.2.2` | `7.1` |
| `S6_02_PUSH` | `C.2.3` | III | `push:src:C.2.3` | `7.2` |
| `S6_02_PUSH` | `C.3.1` | III | `push:src:C.3.1` | `A.14` |
| `S6_02_PUSH` | `C.3.2` | III | `push:src:C.3.2` | `7.3` |
| `S6_02_PUSH` | `C.3.3` | III | `push:src:C.3.3` | `A.15` |
| `S6_02_PUSH` | `C.3.4` | III | `push:src:C.3.4` | `7.4` |
| `S6_02_PUSH` | `C.3.5` | I | `push:src:C.3.5` | `18.5` |
| `S6_02_PUSH` | `C.3.6` | III | `push:src:C.3.6` | `7.5` |
| `S6_02_PUSH` | `C.3.7` | III | `push:src:C.3.7` | `7.6` |
| `S6_02_PUSH` | `C.3.8` | III | `push:src:C.3.8` | `7.7` |
| `S6_02_PUSH` | `C.3.9` | III | `push:src:C.3.9` | `7.8` |
| `S6_02_PUSH` | `C.3.10` | III | `push:src:C.3.10` | `7.9` |
| `S6_02_PUSH` | `C.3.11` | III | `push:src:C.3.11` | `7.10` |
| `S6_02_PUSH` | `C.3.12` | III | `push:src:C.3.12` | `7.11` |
| `S6_02_PUSH` | `C.3.13` | III | `push:src:C.3.13` | `7.12` |
| `S6_02_PUSH` | `C.3.14` | III | `push:src:C.3.14` | `7.13` |
| `S6_02_PUSH` | `C.3.15` | III | `push:src:C.3.15` | `7.14` |
| `S6_02_PUSH` | `C.3.16` | III | `push:src:C.3.16` | `7.15` |
| `S6_02_PUSH` | `C.3.17` | III | `push:src:C.3.17` | `7.17` |
| `S6_02_PUSH` | `C.3.18` | III | `push:src:C.3.18` | `7.19` |
| `S6_02_PUSH` | `C.3.19` | III | `push:src:C.3.19` | `7.21` |
| `S6_02_PUSH` | `C.3.20` | III | `push:src:C.3.20` | `7.23` |
| `S6_02_PUSH` | `C.3.21` | III | `push:src:C.3.21` | `7.25` |
| `S6_02_PUSH` | `C.3.22` | III | `push:src:C.3.22` | `7.26` |
| `S6_02_PUSH` | `C.3.23` | III | `push:src:C.3.23` | `7.27` |
| `S6_02_PUSH` | `C.3.24` | III | `push:src:C.3.24` | `7.28` |
| `S6_02_PUSH` | `C.3.25` | III | `push:src:C.3.25` | `7.29` |
| `S6_02_PUSH` | `C.3.26` | III | `push:src:C.3.26` | `7.31` |
| `S6_02_PUSH` | `C.3.27` | III | `push:src:C.3.27` | `7.32` |
| `S6_02_PUSH` | `C.4.1` | III | `push:src:C.4.1` | `7.35` |
| `S6_02_PUSH` | `C.4.2` | III | `push:src:C.4.2` | `7.36` |
| `S6_02_PUSH` | `C.5.1` | III | `push:src:C.5.1` | `7.37` |
| `S6_02_PUSH` | `D.1.1` | I | `push:src:D.1.1` | `22.1` |
| `S6_02_PUSH` | `D.1.2` | I | `push:src:D.1.2` | `22.2` |
| `S6_02_PUSH` | `D.1.3` | I | `push:src:D.1.3` | `22.3` |
| `S6_02_PUSH` | `D.2.1` | I | `push:src:D.2.1` | `22.4` |
| `S6_02_PUSH` | `D.2.2` | I | `push:src:D.2.2` | `22.5` |
| `S6_02_PUSH` | `D.2.3` | I | `push:src:D.2.3` | `22.6` |
| `S6_02_PUSH` | `D.2.4` | I | `push:src:D.2.4` | `22.7` |
| `S6_02_PUSH` | `D.3.1` | I | `push:src:D.3.1` | `22.8` |
| `S6_02_PUSH` | `D.3.2` | I | `push:src:D.3.2` | `22.9` |
| `S6_02_PUSH` | `D.4.1` | I | `push:src:D.4.1` | `22.10` |
| `S6_02_PUSH` | `D.4.2` | I | `push:src:D.4.2` | `22.11` |
| `S6_02_PUSH` | `D.4.3` | I | `push:src:D.4.3` | `22.12` |
| `S6_02_PUSH` | `D.4.4` | I | `push:src:D.4.4` | `22.13` |
| `S6_02_PUSH` | `D.4.5` | I | `push:src:D.4.5` | `22.14` |
| `S6_02_PUSH` | `D.4.6` | I | `push:src:D.4.6` | `22.15` |
| `S6_02_PUSH` | `D.4.7` | I | `push:src:D.4.7` | `22.16` |
| `S6_02_PUSH` | `D.4.8` | I | `push:src:D.4.8` | `22.17` |
| `S6_02_PUSH` | `E.1.1` | I | `push:src:E.1.1` | `23.1` |
| `S6_02_PUSH` | `E.1.2` | I | `push:src:E.1.2` | `23.2` |
| `S6_02_PUSH` | `E.1.3` | I | `push:src:E.1.3` | `23.3` |
| `S6_02_PUSH` | `E.2.1` | I | `push:src:E.2.1` | `23.4` |
| `S6_02_PUSH` | `E.2.2` | I | `push:src:E.2.2` | `23.5` |
| `S6_02_PUSH` | `E.2.3` | I | `push:src:E.2.3` | `23.6` |
| `S6_02_PUSH` | `E.2.4` | II | `push:src:E.2.4` | `16.1` |
| `S6_02_PUSH` | `E.2.5` | II | `push:src:E.2.5` | `16.2` |
| `S6_02_PUSH` | `E.2.6` | II | `push:src:E.2.6` | `16.3` |
| `S6_02_PUSH` | `E.2.7` | II | `push:src:E.2.7` | `16.5` |
| `S6_02_PUSH` | `E.2.8` | II | `push:src:E.2.8` | `16.7` |
| `S6_02_PUSH` | `E.2.9` | II | `push:src:E.2.9` | `16.8` |
| `S6_02_PUSH` | `E.2.10` | II | `push:src:E.2.10` | `16.9` |
| `S6_02_PUSH` | `E.2.11` | II | `push:src:E.2.11` | `16.10` |
| `S6_02_PUSH` | `E.2.12` | II | `push:src:E.2.12` | `16.12` |
| `S6_02_PUSH` | `E.2.13` | II | `push:src:E.2.13` | `16.14` |
| `S6_02_PUSH` | `E.2.14` | II | `push:src:E.2.14` | `16.16` |
| `S6_02_PUSH` | `E.2.15` | II | `push:src:E.2.15` | `16.18` |
| `S6_02_PUSH` | `E.2.16` | II | `push:src:E.2.16` | `16.20` |
| `S6_02_PUSH` | `E.2.17` | II | `push:src:E.2.17` | `16.21` |
| `S6_02_PUSH` | `E.2.18` | II | `push:src:E.2.18` | `16.23` |
| `S6_02_PUSH` | `E.2.19` | II | `push:src:E.2.19` | `16.24` |
| `S6_02_PUSH` | `E.2.20` | II | `push:src:E.2.20` | `16.25` |
| `S6_02_PUSH` | `E.2.21` | II | `push:src:E.2.21` | `16.27` |
| `S6_02_PUSH` | `E.2.22` | II | `push:src:E.2.22` | `16.29` |
| `S6_02_PUSH` | `E.2.23` | II | `push:src:E.2.23` | `16.30` |
| `S6_02_PUSH` | `E.2.24` | II | `push:src:E.2.24` | `16.31` |
| `S6_02_PUSH` | `E.3.1` | I | `push:src:E.3.1` | `23.7` |
| `S6_02_PUSH` | `E.3.2` | I | `push:src:E.3.2` | `23.8` |
| `S6_02_PUSH` | `E.3.3` | I | `push:src:E.3.3` | `23.9` |
| `S6_02_PUSH` | `E.4.1` | I | `push:src:E.4.1` | `23.10` |
| `S6_02_PUSH` | `E.4.2` | I | `push:src:E.4.2` | `23.11` |
| `S6_02_PUSH` | `E.4.3` | I | `fam:src:C.2.3` | `5.5` |
| `S6_02_PUSH` | `E.5.1` | II | `push:src:E.5.1` | `16.32` |
| `S6_02_PUSH` | `E.5.2` | II | `push:src:E.5.2` | `16.33` |
| `S6_02_PUSH` | `E.5.3` | II | `push:src:E.5.3` | `16.34` |
| `S6_03_CDP` | `A.1.1` | II | `cdp:st:A.1.1` | `5.1` |
| `S6_03_CDP` | `A.2.1` | II | `cdp:st:A.2.1` | `5.2` |
| `S6_03_CDP` | `A.2.2` | II | `cdp:st:A.2.2` | `5.3` |
| `S6_03_CDP` | `A.2.3` | II | `cdp:st:A.2.3` | `A.2` |
| `S6_03_CDP` | `A.1.2` | II | `cdp:st:A.1.2` | `5.4` |
| `S6_03_CDP` | `A.2.4` | II | `cdp:st:A.2.4` | `5.5` |
| `S6_03_CDP` | `A.2.5` | II | `cdp:st:A.2.5` | `5.6` |
| `S6_03_CDP` | `A.2.6` | II | `cdp:st:A.2.6` | `5.7` |
| `S6_03_CDP` | `A.3.1` | II | `cdp:st:A.3.1` | `5.11` |
| `S6_03_CDP` | `A.3.2` | II | `cdp:st:A.3.2` | `5.12` |
| `S6_03_CDP` | `A.3.3` | II | `cdp:st:A.3.3` | `5.13` |
| `S6_03_CDP` | `A.3.4` | II | `cdp:st:A.3.4` | `5.14` |
| `S6_03_CDP` | `A.3.5` | II | `cdp:st:A.3.5` | `5.15` |
| `S6_03_CDP` | `A.4.1` | II | `cdp:st:A.4.1` | `5.16` |
| `S6_03_CDP` | `A.4.2` | II | `cdp:st:A.4.2` | `5.17` |
| `S6_03_CDP` | `A.5.1` | II | `cdp:st:A.5.1` | `6.1` |
| `S6_03_CDP` | `A.5.2` | II | `cdp:st:A.5.2` | `6.2` |
| `S6_03_CDP` | `A.5.3` | II | `cdp:st:A.5.3` | `6.3` |
| `S6_03_CDP` | `A.5.4` | II | `cdp:st:A.5.4` | `6.4` |
| `S6_03_CDP` | `A.5.6` | II | `cdp:st:A.5.6` | `6.5` |
| `S6_03_CDP` | `A.5.9` | II | `cdp:st:A.5.9` | `6.6` |
| `S6_03_CDP` | `A.5.11` | II | `cdp:st:A.5.11` | `6.7` |
| `S6_03_CDP` | `A.5.12` | II | `cdp:st:A.5.12` | `6.8` |
| `S6_03_CDP` | `A.5.13` | II | `cdp:st:A.5.13` | `6.9` |
| `S6_03_CDP` | `A.4.3` | II | `cdp:st:A.4.3` | `5.18` |
| `S6_03_CDP` | `A.4.4` | II | `cdp:st:A.4.4` | `5.19` |
| `S6_03_CDP` | `A.4.5` | II | `cdp:st:A.4.5` | `5.20` |
| `S6_03_CDP` | `A.4.6` | II | `cdp:st:A.4.6` | `5.21` |
| `S6_03_CDP` | `A.4.7` | II | `cdp:st:A.4.7` | `5.22` |
| `S6_03_CDP` | `A.4.8` | II | `cdp:st:A.4.8` | `5.23` |
| `S6_03_CDP` | `A.4.9` | II | `cdp:st:A.4.9` | `5.24` |
| `S6_03_CDP` | `A.5.21` | II | `cdp:st:A.5.21` | `6.21` |
| `S6_03_CDP` | `A.5.5` | II | `cdp:st:A.5.5` | `6.10` |
| `S6_03_CDP` | `A.5.7` | II | `cdp:st:A.5.7` | `6.11` |
| `S6_03_CDP` | `A.5.8` | II | `cdp:st:A.5.8` | `6.12` |
| `S6_03_CDP` | `A.5.14` | II | `cdp:st:A.5.14` | `6.13` |
| `S6_03_CDP` | `A.5.10` | II | `cdp:st:A.5.10` | `6.14` |
| `S6_03_CDP` | `A.5.20` | II | `cdp:st:A.5.20` | `6.15` |
| `S6_03_CDP` | `A.5.15` | II | `cdp:st:A.5.15` | `6.16` |
| `S6_03_CDP` | `A.5.17` | II | `cdp:st:A.5.17` | `6.17` |
| `S6_03_CDP` | `A.5.18` | II | `cdp:st:A.5.18` | `6.18` |
| `S6_03_CDP` | `A.5.19` | II | `cdp:st:A.5.19` | `6.19` |
| `S6_03_CDP` | `A.5.16` | II | `cdp:st:A.5.16` | `6.20` |
| `S6_03_CDP` | `B1` | II | `cdp:st:B1` | `5.8` |
| `S6_03_CDP` | `B2` | II | `cdp:st:B2` | `5.9` |
| `S6_03_CDP` | `B3` | II | `cdp:st:B3` | `5.10` |
| `S6_03_CDP` | `C.1.1` | II | `cdp:st:C.1.1` | `2.1` |
| `S6_03_CDP` | `C.1.2` | II | `cdp:st:C.1.2` | `A.3` |
| `S6_03_CDP` | `C.1.3` | II | `cdp:st:C.1.3` | `2.2` |
| `S6_03_CDP` | `C.3.1` | II | `cdp:st:C.3.1` | `4.9` |
| `S6_03_CDP` | `C.3.2` | II | `cdp:st:C.3.2` | `4.1` |
| `S6_03_CDP` | `C.3.3` | II | `cdp:st:C.3.3` | `4.2` |
| `S6_03_CDP` | `C.3.4` | II | `cdp:st:C.3.4` | `4.3` |
| `S6_03_CDP` | `C.3.5` | II | `cdp:st:C.3.5` | `4.11` |
| `S6_03_CDP` | `C.3.6` | II | `cdp:st:C.3.6` | `4.12` |
| `S6_03_CDP` | `C.3.7` | II | `cdp:st:C.3.7` | `4.4` |
| `S6_03_CDP` | `C.3.8` | II | `cdp:st:C.3.8` | `4.5` |
| `S6_03_CDP` | `C.3.9` | II | `cdp:st:C.3.9` | `4.6` |
| `S6_03_CDP` | `C.3.10` | II | `cdp:st:C.3.10` | `4.7` |
| `S6_03_CDP` | `C.3.11` | II | `cdp:st:C.3.11` | `4.10` |
| `S6_03_CDP` | `C2a` | II | `cdp:st:C2a` | `9.5` |
| `S6_03_CDP` | `C2b` | II | `cdp:st:C2b` | `9.6` |
| `S6_03_CDP` | `C2c` | II | `cdp:st:C2c` | `9.7` |
| `S6_03_CDP` | `C5a` | II | `cdp:st:C5a` | `13.9` |
| `S6_03_CDP` | `C.2.NC.1` | II | `cdp:st:C.2.NC.1` | `A.4` |
| `S6_03_CDP` | `C.2.NC.2` | II | `cdp:st:C.2.NC.2` | `9.1` |
| `S6_03_CDP` | `C.2.NC.3` | II | `cdp:st:C.2.NC.3` | `9.2` |
| `S6_03_CDP` | `C.2.NC.4` | II | `cdp:st:C.2.NC.4` | `9.3` |
| `S6_03_CDP` | `C.2.NC.5` | II | `cdp:st:C.2.NC.5` | `9.4` |
| `S6_03_CDP` | `C.2.UN.81` | II | `cdp:st:C.2.UN.81` | `12.11` |
| `S6_03_CDP` | `C.2.UN.57` | II | `cdp:st:C.2.UN.57` | `11.12` |
| `S6_03_CDP` | `C.2.UN.53` | II | `cdp:st:C.2.UN.53` | `11.8` |
| `S6_03_CDP` | `C.2.UN.59` | II | `cdp:st:C.2.UN.59` | `11.14` |
| `S6_03_CDP` | `C.2.UN.17` | II | `cdp:st:C.2.UN.17` | `7.8` |
| `S6_03_CDP` | `C.2.VII.1` | II | `cdp:st:C.2.VII.1` | `8.11` |
| `S6_03_CDP` | `C.2.VII.2` | II | `cdp:st:C.2.VII.2` | `8.12` |
| `S6_03_CDP` | `C.2.VII.3` | II | `cdp:st:C.2.VII.3` | `8.13` |
| `S6_03_CDP` | `C.2.VII.4` | II | `cdp:st:C.2.VII.4` | `8.14` |
| `S6_03_CDP` | `C.2.UN.79` | II | `cdp:st:C.2.UN.79` | `12.9` |
| `S6_03_CDP` | `C.2.UN.28` | II | `cdp:st:C.2.UN.28` | `7.14` |
| `S6_03_CDP` | `C.2.UN.73` | II | `cdp:st:C.2.UN.73` | `12.4` |
| `S6_03_CDP` | `C.2.UN.3` | II | `cdp:st:C.2.UN.3` | `7.3` |
| `S6_03_CDP` | `C.2.UN.86` | II | `cdp:st:C.2.UN.86` | `12.18` |
| `S6_03_CDP` | `C.2.UN.16` | II | `cdp:st:C.2.UN.16` | `7.7` |
| `S6_03_CDP` | `C.2.UN.47` | II | `cdp:st:C.2.UN.47` | `7.22` |
| `S6_03_CDP` | `C.2.UN.31` | II | `cdp:st:C.2.UN.31` | `7.16` |
| `S6_03_CDP` | `C.2.CR.1` | II | `cdp:st:C.2.CR.1` | `8.2` |
| `S6_03_CDP` | `C.2.CR.2` | II | `cdp:st:C.2.CR.2` | `8.3` |
| `S6_03_CDP` | `C.2.CR.3` | II | `cdp:st:C.2.CR.3` | `8.4` |
| `S6_03_CDP` | `C.2.CR.4` | II | `cdp:st:C.2.CR.4` | `8.5` |
| `S6_03_CDP` | `C.2.CR.5` | II | `cdp:st:C.2.CR.5` | `8.6` |
| `S6_03_CDP` | `C.2.CR.6` | II | `cdp:st:C.2.CR.6` | `8.7` |
| `S6_03_CDP` | `C.2.UN.36` | II | `cdp:st:C.2.UN.36` | `7.18` |
| `S6_03_CDP` | `C.2.D4.1` | II | `cdp:st:C.2.D4.1` | `8.23` |
| `S6_03_CDP` | `C.2.D4.3` | II | `cdp:st:C.2.D4.3` | `8.25` |
| `S6_03_CDP` | `C.2.D4.2` | II | `cdp:st:C.2.D4.2` | `8.24` |
| `S6_03_CDP` | `C.2.UN.8` | II | `cdp:st:C.2.UN.8` | `10.2` |
| `S6_03_CDP` | `C.2.UN.23` | II | `cdp:st:C.2.UN.23` | `7.12` |
| `S6_03_CDP` | `C.2.UN.41` | II | `cdp:st:C.2.UN.41` | `10.12` |
| `S6_03_CDP` | `C.2.UN.27` | II | `cdp:st:C.2.UN.27` | `10.7` |
| `S6_03_CDP` | `C.2.UN.30` | II | `cdp:st:C.2.UN.30` | `10.8` |
| `S6_03_CDP` | `C.2.UN.37` | II | `cdp:st:C.2.UN.37` | `10.11` |
| `S6_03_CDP` | `C.2.UN.6` | II | `cdp:st:C.2.UN.6` | `10.1` |
| `S6_03_CDP` | `C.2.UN.33` | II | `cdp:st:C.2.UN.33` | `7.17` |
| `S6_03_CDP` | `C.2.UN.25` | II | `cdp:st:C.2.UN.25` | `10.6` |
| `S6_03_CDP` | `C.2.UN.35` | II | `cdp:st:C.2.UN.35` | `10.10` |
| `S6_03_CDP` | `C.2.UN.64` | II | `cdp:st:C.2.UN.64` | `9.12` |
| `S6_03_CDP` | `C.2.UN.20` | II | `cdp:st:C.2.UN.20` | `7.10` |
| `S6_03_CDP` | `C.2.UN.26` | II | `cdp:st:C.2.UN.26` | `7.13` |
| `S6_03_CDP` | `C.2.UN.68` | II | `cdp:st:C.2.UN.68` | `9.16` |
| `S6_03_CDP` | `C.2.UN.44` | II | `cdp:st:C.2.UN.44` | `7.21` |
| `S6_03_CDP` | `C.2.G.1` | II | `cdp:st:C.2.G.1` | `13.1` |
| `S6_03_CDP` | `C.2.UN.85` | II | `cdp:st:C.2.UN.85` | `12.17` |
| `S6_03_CDP` | `C.2.MH.1` | II | `cdp:st:C.2.MH.1` | `8.31` |
| `S6_03_CDP` | `C.2.MH.2` | II | `cdp:st:C.2.MH.2` | `8.32` |
| `S6_03_CDP` | `C.2.MH.3` | II | `cdp:st:C.2.MH.3` | `8.33` |
| `S6_03_CDP` | `C.2.MH.4` | II | `cdp:st:C.2.MH.4` | `8.34` |
| `S6_03_CDP` | `C.2.UN.40` | II | `cdp:st:C.2.UN.40` | `11.1` |
| `S6_03_CDP` | `C.2.UN.38` | II | `cdp:st:C.2.UN.38` | `7.19` |
| `S6_03_CDP` | `C.2.UN.19` | II | `cdp:st:C.2.UN.19` | `7.9` |
| `S6_03_CDP` | `C.2.UN.48` | II | `cdp:st:C.2.UN.48` | `11.3` |
| `S6_03_CDP` | `C.2.UN.46` | II | `cdp:st:C.2.UN.46` | `11.2` |
| `S6_03_CDP` | `C.2.UN.54` | II | `cdp:st:C.2.UN.54` | `11.9` |
| `S6_03_CDP` | `C.2.UN.60` | II | `cdp:st:C.2.UN.60` | `11.15` |
| `S6_03_CDP` | `C.2.UN.58` | II | `cdp:st:C.2.UN.58` | `11.13` |
| `S6_03_CDP` | `C.2.INT.1` | II | `cdp:st:C.2.INT.1` | `8.28` |
| `S6_03_CDP` | `C.2.INT.2` | II | `cdp:st:C.2.INT.2` | `8.29` |
| `S6_03_CDP` | `C.2.INT.3` | II | `cdp:st:C.2.INT.3` | `8.30` |
| `S6_03_CDP` | `C.2.IRR.1` | II | `cdp:st:C.2.IRR.1` | `8.10` |
| `S6_03_CDP` | `C.2.UN.7` | II | `cdp:st:C.2.UN.7` | `8.26` |
| `S6_03_CDP` | `C.2.UN.12` | II | `cdp:st:C.2.UN.12` | `8.27` |
| `S6_03_CDP` | `C2d` | II | `cdp:st:C2d` | `9.8` |
| `S6_03_CDP` | `C.2.UN.24` | II | `cdp:st:C.2.UN.24` | `9.10` |
| `S6_03_CDP` | `C.2.UN.32` | II | `cdp:st:C.2.UN.32` | `9.11` |
| `S6_03_CDP` | `C.2.UN.75` | II | `cdp:st:C.2.UN.75` | `12.7` |
| `S6_03_CDP` | `C.2.UN.13` | II | `cdp:st:C.2.UN.13` | `10.3` |
| `S6_03_CDP` | `C.2.UN.82` | II | `cdp:st:C.2.UN.82` | `12.12` |
| `S6_03_CDP` | `C.2.UN.77` | II | `cdp:st:C.2.UN.77` | `12.8` |
| `S6_03_CDP` | `C.2.UN.66` | II | `cdp:st:C.2.UN.66` | `9.14` |
| `S6_03_CDP` | `C.2.UN.51` | II | `cdp:st:C.2.UN.51` | `11.6` |
| `S6_03_CDP` | `C.2.UN.72` | II | `cdp:st:C.2.UN.72` | `12.16` |
| `S6_03_CDP` | `C.2.UN.9` | II | `cdp:st:C.2.UN.9` | `8.8` |
| `S6_03_CDP` | `C.2.UN.10` | II | `cdp:st:C.2.UN.10` | `8.9` |
| `S6_03_CDP` | `C.2.UN.42` | II | `cdp:st:C.2.UN.42` | `10.13` |
| `S6_03_CDP` | `C.2.UN.49` | II | `cdp:st:C.2.UN.49` | `11.4` |
| `S6_03_CDP` | `C.2.UN.69` | II | `cdp:st:C.2.UN.69` | `12.1` |
| `S6_03_CDP` | `C.2.UN.70` | II | `cdp:st:C.2.UN.70` | `12.2` |
| `S6_03_CDP` | `C.2.UN.5` | II | `cdp:st:C.2.UN.5` | `8.1` |
| `S6_03_CDP` | `C.2.UN.18` | II | `cdp:st:C.2.UN.18` | `10.4` |
| `S6_03_CDP` | `C.2.UN.62` | II | `cdp:st:C.2.UN.62` | `11.17` |
| `S6_03_CDP` | `C.2.UN.29` | II | `cdp:st:C.2.UN.29` | `7.15` |
| `S6_03_CDP` | `C.2.UN.22` | II | `cdp:st:C.2.UN.22` | `7.11` |
| `S6_03_CDP` | `C.2.RAT.1` | II | `cdp:st:C.2.RAT.1` | `8.15` |
| `S6_03_CDP` | `C.2.RAT.2` | II | `cdp:st:C.2.RAT.2` | `8.16` |
| `S6_03_CDP` | `C.2.RAT.3` | II | `cdp:st:C.2.RAT.3` | `8.17` |
| `S6_03_CDP` | `C.2.RAT.4` | II | `cdp:st:C.2.RAT.4` | `8.18` |
| `S6_03_CDP` | `C.2.UN.67` | II | `cdp:st:C.2.UN.67` | `9.15` |
| `S6_03_CDP` | `C.2.RAT.5` | II | `cdp:st:C.2.RAT.5` | `8.19` |
| `S6_03_CDP` | `C.2.RAT.6` | II | `cdp:st:C.2.RAT.6` | `A.6` |
| `S6_03_CDP` | `C.2.RAT.7` | II | `cdp:st:C.2.RAT.7` | `8.20` |
| `S6_03_CDP` | `C.2.RAT.8` | II | `cdp:st:C.2.RAT.8` | `8.21` |
| `S6_03_CDP` | `C.2.RAT.9` | II | `cdp:st:C.2.RAT.9` | `8.22` |
| `S6_03_CDP` | `C.2.UN.61` | II | `cdp:st:C.2.UN.61` | `11.16` |
| `S6_03_CDP` | `C.2.UN.78` | II | `cdp:st:C.2.UN.78` | `12.15` |
| `S6_03_CDP` | `C.2.UN.74` | II | `cdp:st:C.2.UN.74` | `12.6` |
| `S6_03_CDP` | `C.2.UN.55` | II | `cdp:st:C.2.UN.55` | `11.10` |
| `S6_03_CDP` | `C.2.UN.45` | II | `cdp:st:C.2.UN.45` | `10.15` |
| `S6_03_CDP` | `C.2.UN.43` | II | `cdp:st:C.2.UN.43` | `10.14` |
| `S6_03_CDP` | `C.2.UN.21` | II | `cdp:st:C.2.UN.21` | `10.5` |
| `S6_03_CDP` | `C.2.UN.50` | II | `cdp:st:C.2.UN.50` | `11.5` |
| `S6_03_CDP` | `C.2.UN.34` | II | `cdp:st:C.2.UN.34` | `10.9` |
| `S6_03_CDP` | `C.2.UN.15` | II | `cdp:st:C.2.UN.15` | `7.6` |
| `S6_03_CDP` | `C.2.UN.11` | II | `cdp:st:C.2.UN.11` | `9.9` |
| `S6_03_CDP` | `C.2.UN.71` | II | `cdp:st:C.2.UN.71` | `12.3` |
| `S6_03_CDP` | `C.2.UN.83` | II | `cdp:st:C.2.UN.83` | `12.13` |
| `S6_03_CDP` | `C.2.UN.80` | II | `cdp:st:C.2.UN.80` | `12.10` |
| `S6_03_CDP` | `C.2.UN.65` | II | `cdp:st:C.2.UN.65` | `9.13` |
| `S6_03_CDP` | `C.2.UN.84` | II | `cdp:st:C.2.UN.84` | `12.14` |
| `S6_03_CDP` | `C.2.UN.1` | II | `cdp:st:C.2.UN.1` | `7.1` |
| `S6_03_CDP` | `C.2.UN.2` | II | `cdp:st:C.2.UN.2` | `7.2` |
| `S6_03_CDP` | `C.2.UN.4` | II | `cdp:st:C.2.UN.4` | `7.4` |
| `S6_03_CDP` | `C.2.UN.63` | II | `cdp:st:C.2.UN.63` | `11.18` |
| `S6_03_CDP` | `C.2.UN.76` | II | `cdp:st:C.2.UN.76` | `12.5` |
| `S6_03_CDP` | `C.2.UN.52` | II | `cdp:st:C.2.UN.52` | `11.7` |
| `S6_03_CDP` | `C.2.UN.56` | II | `cdp:st:C.2.UN.56` | `11.11` |
| `S6_03_CDP` | `C.2.UN.39` | II | `cdp:st:C.2.UN.39` | `7.20` |
| `S6_03_CDP` | `C.2.UN.14` | II | `cdp:st:C.2.UN.14` | `7.5` |
| `S6_03_CDP` | `C.3.12` | II | `cdp:st:C.3.12` | `4.8` |
| `S6_03_CDP` | `C4a` | II | `cdp:st:C4a` | `13.2` |
| `S6_03_CDP` | `C4b` | II | `cdp:st:C4b` | `13.3` |
| `S6_03_CDP` | `C4c` | II | `cdp:st:C4c` | `13.4` |
| `S6_03_CDP` | `C4d` | II | `cdp:st:C4d` | `13.5` |
| `S6_03_CDP` | `C4e` | II | `cdp:st:C4e` | `13.6` |
| `S6_03_CDP` | `C4f` | II | `cdp:st:C4f` | `13.7` |
| `S6_03_CDP` | `C4g` | II | `cdp:st:C4g` | `13.8` |
| `S6_03_CDP` | `C5b` | II | `cdp:st:C5b` | `13.10` |
| `S6_03_CDP` | `C5c` | II | `cdp:st:C5c` | `13.11` |
| `S6_03_CDP` | `D.1.1` | II | `cdp:st:D.1.1` | `A.1` |
| `S6_03_CDP` | `D.1.2` | II | `cdp:st:D.1.2` | `3.1` |
| `S6_03_CDP` | `D.1.3` | II | `cdp:st:D.1.3` | `A.5` |
| `S6_03_CDP` | `D.1.14` | I | `fam:src:F.1.1` | `7.1` |
| `S6_03_CDP` | `D.1.4` | II | `cdp:st:D.1.4` | `3.10` |
| `S6_03_CDP` | `D.1.10` | II | `cdp:st:D.1.10` | `3.7` |
| `S6_03_CDP` | `D.1.5` | II | `cdp:st:D.1.5` | `3.2` |
| `S6_03_CDP` | `D.1.6` | II | `cdp:st:D.1.6` | `3.3` |
| `S6_03_CDP` | `D.1.7` | II | `cdp:st:D.1.7` | `3.4` |
| `S6_03_CDP` | `D.1.8` | II | `cdp:st:D.1.8` | `3.5` |
| `S6_03_CDP` | `D.1.9` | II | `cdp:st:D.1.9` | `3.6` |
| `S6_03_CDP` | `D.1.11` | II | `cdp:st:D.1.11` | `3.8` |
| `S6_03_CDP` | `D.1.12` | II | `cdp:st:D.1.12` | `3.9` |
| `S6_03_CDP` | `D.1.13` | II | `cdp:st:D.1.13` | `3.11` |
| `S6_03_CDP` | `D.1.15` | II | `cdp:st:D.1.15` | `3.12` |
| `S6_03_CDP` | `D.2.1` | II | `cdp:st:D.2.1` | `14.1` |
| `S6_03_CDP` | `D.2.2` | II | `cdp:st:D.2.2` | `14.8` |
| `S6_03_CDP` | `D.2.3` | II | `cdp:st:D.2.3` | `14.2` |
| `S6_03_CDP` | `D.2.4` | II | `cdp:st:D.2.4` | `14.3` |
| `S6_03_CDP` | `D.2.7` | II | `cdp:st:D.2.7` | `14.6` |
| `S6_03_CDP` | `D.2.8` | II | `cdp:st:D.2.8` | `14.7` |
| `S6_03_CDP` | `D.2.6` | II | `cdp:st:D.2.6` | `14.5` |
| `S6_03_CDP` | `D.2.5` | II | `cdp:st:D.2.5` | `14.4` |
| `S6_03_CDP` | `E1` | II | `cdp:st:E1` | `2.3` |
| `S6_03_CDP` | `E2` | II | `cdp:st:E2` | `A.7` |
| `S6_03_CDP` | `E3` | II | `cdp:st:E3` | `A.8` |
| `S6_03_CDP` | `E4` | II | `cdp:st:E4` | `A.9` |
| `S6_03_CDP` | `E5` | II | `cdp:st:E5` | `15.1` |
| `S6_03_CDP` | `E6` | II | `cdp:st:E6` | `15.2` |
| `S6_03_CDP` | `E7` | II | `cdp:st:E7` | `15.3` |
| `S6_03_CDP` | `E8` | II | `cdp:st:E8` | `15.4` |
| `S6_03_CDP` | `E9` | I | `fam:src:A.5.2` | `3.9` |
| `S6_03_CDP` | `E10` | II | `cdp:st:E10` | `15.5` |
| `S6_03_CDP` | `E11` | II | `cdp:st:E11` | `15.6` |
| `S6_03_CDP` | `E12` | II | `cdp:st:E12` | `15.7` |
| `S6_03_CDP` | `E13` | II | `cdp:st:E13` | `15.8` |
| `S6_03_CDP` | `E14` | II | `cdp:st:E14` | `15.9` |
| `S6_03_CDP` | `E15` | II | `cdp:st:E15` | `15.10` |
| `S6_03_CDP` | `E17` | II | `cdp:st:E17` | `15.12` |
| `S6_03_CDP` | `E18` | II | `cdp:st:E18` | `15.13` |
| `S6_03_CDP` | `E19` | II | `cdp:st:E19` | `A.10` |
| `S6_03_CDP` | `E16` | II | `cdp:st:E16` | `15.11` |
| `S6_04_MAPS_MANIFOLDS` | `A.1.1` | I | `mapsI:src:A.1.1` | `17.1` |
| `S6_04_MAPS_MANIFOLDS` | `A.1.2` | I | `mapsI:src:A.1.2` | `17.2` |
| `S6_04_MAPS_MANIFOLDS` | `A.1.3` | I | `mapsI:src:A.1.3` | `17.3` |
| `S6_04_MAPS_MANIFOLDS` | `A.2.1` | I | `mapsI:src:A.2.1` | `17.4` |
| `S6_04_MAPS_MANIFOLDS` | `A.2.2` | III | `maps:src:A.2.2` | `2.1` |
| `S6_04_MAPS_MANIFOLDS` | `A.3.1` | I | `mapsI:src:A.3.1` | `18.1` |
| `S6_04_MAPS_MANIFOLDS` | `A.3.2` | I | `mapsI:src:A.3.2` | `18.2` |
| `S6_04_MAPS_MANIFOLDS` | `A.3.3` | I | `mapsI:src:A.3.3` | `18.3` |
| `S6_04_MAPS_MANIFOLDS` | `A.3.4` | I | `mapsI:src:A.3.4` | `18.4` |
| `S6_04_MAPS_MANIFOLDS` | `B.1.1` | III | `maps:src:B.1.1` | `2.2` |
| `S6_04_MAPS_MANIFOLDS` | `B.1.2` | III | `maps:src:B.1.2` | `2.3` |
| `S6_04_MAPS_MANIFOLDS` | `B.2.1` | III | `maps:src:B.2.1` | `2.4` |
| `S6_04_MAPS_MANIFOLDS` | `B.3.1` | III | `maps:src:B.3.1` | `2.5` |
| `S6_04_MAPS_MANIFOLDS` | `B.3.2` | III | `maps:src:B.3.2` | `2.6` |
| `S6_04_MAPS_MANIFOLDS` | `B.3.3` | III | `maps:src:B.3.3` | `2.7` |
| `S6_04_MAPS_MANIFOLDS` | `B.4.1` | III | `maps:src:B.4.1` | `2.8` |
| `S6_04_MAPS_MANIFOLDS` | `B.5.1` | III | `maps:src:B.5.1` | `2.9` |
| `S6_04_MAPS_MANIFOLDS` | `B.5.2` | III | `maps:src:B.5.2` | `2.10` |
| `S6_04_MAPS_MANIFOLDS` | `B.6.1` | III | `maps:src:B.6.1` | `2.11` |
| `S6_04_MAPS_MANIFOLDS` | `B.6.2` | III | `maps:src:B.6.2` | `2.12` |
| `S6_04_MAPS_MANIFOLDS` | `B.6.3` | III | `maps:src:B.6.3` | `2.13` |
| `S6_04_MAPS_MANIFOLDS` | `B.6.4` | III | `maps:src:B.6.4` | `2.14` |
| `S6_04_MAPS_MANIFOLDS` | `B.6.5` | III | `maps:src:B.6.5` | `2.15` |
| `S6_04_MAPS_MANIFOLDS` | `B.6.6` | III | `maps:src:B.6.6` | `2.16` |
| `S6_04_MAPS_MANIFOLDS` | `B.6.7` | III | `maps:src:B.6.7` | `2.17` |
| `S6_04_MAPS_MANIFOLDS` | `B.6.8` | III | `maps:src:B.6.8` | `2.18` |
| `S6_04_MAPS_MANIFOLDS` | `B.6.9` | III | `maps:src:B.6.9` | `A.3` |
| `S6_04_MAPS_MANIFOLDS` | `B.6.10` | III | `maps:src:B.6.10` | `2.19` |
| `S6_04_MAPS_MANIFOLDS` | `B.6.11` | III | `maps:src:B.6.11` | `2.20` |
| `S6_04_MAPS_MANIFOLDS` | `B.6.12` | III | `maps:src:B.6.12` | `2.21` |
| `S6_04_MAPS_MANIFOLDS` | `B.6.13` | III | `maps:src:B.6.13` | `2.22` |
| `S6_04_MAPS_MANIFOLDS` | `B.6.14` | III | `maps:src:B.6.14` | `2.23` |
| `S6_04_MAPS_MANIFOLDS` | `B.6.15` | III | `maps:src:B.6.15` | `2.24` |
| `S6_04_MAPS_MANIFOLDS` | `B.6.16` | III | `maps:src:B.6.16` | `2.25` |
| `S6_04_MAPS_MANIFOLDS` | `B.6.17` | III | `maps:src:B.6.17` | `2.26` |
| `S6_04_MAPS_MANIFOLDS` | `B.6.18` | III | `maps:src:B.6.18` | `2.27` |
| `S6_04_MAPS_MANIFOLDS` | `B.6.19` | III | `maps:src:B.6.19` | `2.28` |
| `S6_04_MAPS_MANIFOLDS` | `B.6.20` | III | `maps:src:B.6.20` | `2.29` |
| `S6_04_MAPS_MANIFOLDS` | `B.6.21` | III | `maps:src:B.6.21` | `2.30` |
| `S6_04_MAPS_MANIFOLDS` | `B.6.22` | III | `maps:src:B.6.22` | `2.31` |
| `S6_04_MAPS_MANIFOLDS` | `B.6.23` | III | `maps:src:B.6.23` | `2.32` |
| `S6_04_MAPS_MANIFOLDS` | `B.6.24` | III | `maps:src:B.6.24` | `2.33` |
| `S6_04_MAPS_MANIFOLDS` | `B.6.25` | III | `maps:src:B.6.25` | `2.34` |
| `S6_04_MAPS_MANIFOLDS` | `C.1.1` | III | `maps:src:C.1.1` | `3.1` |
| `S6_04_MAPS_MANIFOLDS` | `C.1.2` | III | `maps:src:C.1.2` | `3.2` |
| `S6_04_MAPS_MANIFOLDS` | `C.1.3` | III | `maps:src:C.1.3` | `3.3` |
| `S6_04_MAPS_MANIFOLDS` | `C.1.4` | III | `maps:src:C.1.4` | `3.4` |
| `S6_04_MAPS_MANIFOLDS` | `C.1.5` | III | `maps:src:C.1.5` | `3.5` |
| `S6_04_MAPS_MANIFOLDS` | `D.1.1` | III | `maps:src:D.1.1` | `4.1` |
| `S6_04_MAPS_MANIFOLDS` | `D.1.2` | III | `maps:src:D.1.2` | `4.2` |
| `S6_04_MAPS_MANIFOLDS` | `D.1.3` | III | `maps:src:D.1.3` | `4.3` |
| `S6_04_MAPS_MANIFOLDS` | `D.1.4` | III | `maps:src:D.1.4` | `4.4` |
| `S6_04_MAPS_MANIFOLDS` | `D.1.5` | III | `maps:src:D.1.5` | `4.5` |
| `S6_04_MAPS_MANIFOLDS` | `D.1.6` | III | `maps:src:D.1.6` | `4.6` |
| `S6_04_MAPS_MANIFOLDS` | `D.1.7` | III | `maps:src:D.1.7` | `4.7` |
| `S6_04_MAPS_MANIFOLDS` | `D.1.8` | III | `maps:src:D.1.8` | `4.8` |
| `S6_04_MAPS_MANIFOLDS` | `D.1.9` | III | `maps:src:D.1.9` | `4.9` |
| `S6_04_MAPS_MANIFOLDS` | `D.1.10` | III | `maps:src:D.1.10` | `4.10` |
| `S6_04_MAPS_MANIFOLDS` | `D.1.11` | III | `maps:src:D.1.11` | `A.4` |
| `S6_04_MAPS_MANIFOLDS` | `D.1.12` | III | `maps:src:D.1.12` | `4.11` |
| `S6_04_MAPS_MANIFOLDS` | `D.2.1` | III | `maps:src:D.2.1` | `A.5` |
| `S6_04_MAPS_MANIFOLDS` | `D.2.2` | III | `maps:src:D.2.2` | `4.12` |
| `S6_04_MAPS_MANIFOLDS` | `D.2.3` | III | `maps:src:D.2.3` | `4.13` |
| `S6_04_MAPS_MANIFOLDS` | `D.2.4` | III | `maps:src:D.2.4` | `AL.1` |
| `S6_04_MAPS_MANIFOLDS` | `D.2.5` | III | `maps:src:D.2.5` | `4.14` |
| `S6_04_MAPS_MANIFOLDS` | `D.2.6` | III | `maps:src:D.2.6` | `4.15` |
| `S6_04_MAPS_MANIFOLDS` | `D.2.7` | III | `maps:src:D.2.7` | `4.16` |
| `S6_04_MAPS_MANIFOLDS` | `D.2.8` | III | `maps:src:D.2.8` | `4.17` |
| `S6_04_MAPS_MANIFOLDS` | `D.2.9` | III | `maps:src:D.2.9` | `4.18` |
| `S6_04_MAPS_MANIFOLDS` | `D.2.10` | III | `maps:src:D.2.10` | `4.19` |
| `S6_04_MAPS_MANIFOLDS` | `D.2.11` | III | `maps:src:D.2.11` | `4.20` |
| `S6_04_MAPS_MANIFOLDS` | `D.2.12` | III | `maps:src:D.2.12` | `4.21` |
| `S6_04_MAPS_MANIFOLDS` | `D.2.13` | III | `maps:src:D.2.13` | `4.22` |
| `S6_04_MAPS_MANIFOLDS` | `D.2.14` | III | `maps:src:D.2.14` | `4.23` |
| `S6_04_MAPS_MANIFOLDS` | `D.2.15` | III | `maps:src:D.2.15` | `4.24` |
| `S6_04_MAPS_MANIFOLDS` | `D.2.16` | III | `maps:src:D.2.16` | `4.25` |
| `S6_04_MAPS_MANIFOLDS` | `D.2.17` | III | `maps:src:D.2.17` | `4.26` |
| `S6_04_MAPS_MANIFOLDS` | `D.2.18` | III | `maps:src:D.2.18` | `4.27` |
| `S6_04_MAPS_MANIFOLDS` | `D.2.19` | III | `maps:src:D.2.19` | `4.28` |
| `S6_04_MAPS_MANIFOLDS` | `D.2.20` | III | `maps:src:D.2.20` | `4.29` |
| `S6_04_MAPS_MANIFOLDS` | `D.2.21` | III | `maps:src:D.2.21` | `4.30` |
| `S6_04_MAPS_MANIFOLDS` | `D.2.22` | III | `maps:src:D.2.22` | `4.31` |
| `S6_04_MAPS_MANIFOLDS` | `D.2.23` | III | `maps:src:D.2.23` | `4.32` |
| `S6_04_MAPS_MANIFOLDS` | `D.2.24` | III | `maps:src:D.2.24` | `4.33` |
| `S6_04_MAPS_MANIFOLDS` | `D.2.25` | III | `maps:src:D.2.25` | `4.34` |
| `S6_04_MAPS_MANIFOLDS` | `D.2.26` | III | `maps:src:D.2.26` | `4.35` |
| `S6_04_MAPS_MANIFOLDS` | `D.2.27` | III | `maps:src:D.2.27` | `4.36` |
| `S6_04_MAPS_MANIFOLDS` | `D.2.28` | III | `maps:src:D.2.28` | `4.37` |
| `S6_04_MAPS_MANIFOLDS` | `D.2.29` | III | `maps:src:D.2.29` | `4.38` |
| `S6_04_MAPS_MANIFOLDS` | `D.2.30` | III | `maps:src:D.2.30` | `4.39` |
| `S6_04_MAPS_MANIFOLDS` | `D.2.31` | III | `maps:src:D.2.31` | `4.40` |
| `S6_04_MAPS_MANIFOLDS` | `D.2.32` | III | `maps:src:D.2.32` | `4.41` |
| `S6_04_MAPS_MANIFOLDS` | `D.2.33` | III | `maps:src:D.2.33` | `4.42` |
| `S6_04_MAPS_MANIFOLDS` | `D.2.34` | III | `maps:src:D.2.34` | `4.43` |
| `S6_04_MAPS_MANIFOLDS` | `D.2.35` | III | `maps:src:D.2.35` | `4.44` |
| `S6_04_MAPS_MANIFOLDS` | `D.2.36` | III | `maps:src:D.2.36` | `4.45` |
| `S6_04_MAPS_MANIFOLDS` | `D.2.37` | III | `maps:src:D.2.37` | `4.46` |
| `S6_04_MAPS_MANIFOLDS` | `D.2.38` | III | `maps:src:D.2.38` | `4.47` |
| `S6_04_MAPS_MANIFOLDS` | `D.2.39` | III | `maps:src:D.2.39` | `4.48` |
| `S6_04_MAPS_MANIFOLDS` | `D.2.40` | III | `maps:src:D.2.40` | `4.49` |
| `S6_04_MAPS_MANIFOLDS` | `D.2.41` | III | `maps:src:D.2.41` | `4.50` |
| `S6_04_MAPS_MANIFOLDS` | `D.2.42` | III | `maps:src:D.2.42` | `4.51` |
| `S6_04_MAPS_MANIFOLDS` | `D.2.43` | III | `maps:src:D.2.43` | `4.52` |
| `S6_04_MAPS_MANIFOLDS` | `D.2.44` | III | `maps:src:D.2.44` | `4.53` |
| `S6_04_MAPS_MANIFOLDS` | `D.2.45` | III | `maps:src:D.2.45` | `4.54` |
| `S6_04_MAPS_MANIFOLDS` | `D.2.46` | III | `maps:src:D.2.46` | `4.55` |
| `S6_04_MAPS_MANIFOLDS` | `D.2.47` | III | `maps:src:D.2.47` | `4.56` |
| `S6_04_MAPS_MANIFOLDS` | `D.2.48` | III | `maps:src:D.2.48` | `4.57` |
| `S6_04_MAPS_MANIFOLDS` | `D.2.49` | III | `maps:src:D.2.49` | `4.58` |
| `S6_04_MAPS_MANIFOLDS` | `D.2.50` | III | `maps:src:D.2.50` | `4.59` |
| `S6_04_MAPS_MANIFOLDS` | `D.2.51` | III | `maps:src:D.2.51` | `4.60` |
| `S6_04_MAPS_MANIFOLDS` | `D.2.52` | III | `maps:src:D.2.52` | `4.61` |
| `S6_04_MAPS_MANIFOLDS` | `D.2.53` | III | `maps:src:D.2.53` | `4.62` |
| `S6_04_MAPS_MANIFOLDS` | `D.3.1` | III | `maps:src:D.3.1` | `4.63` |
| `S6_04_MAPS_MANIFOLDS` | `D.3.2` | III | `maps:src:D.3.2` | `A.6` |
| `S6_04_MAPS_MANIFOLDS` | `D.3.3` | III | `maps:src:D.3.3` | `4.64` |
| `S6_04_MAPS_MANIFOLDS` | `D.3.4` | III | `maps:src:D.3.4` | `A.7` |
| `S6_04_MAPS_MANIFOLDS` | `E.1.1` | III | `maps:src:E.1.1` | `5.1` |
| `S6_04_MAPS_MANIFOLDS` | `E.1.2` | III | `maps:src:E.1.2` | `5.2` |
| `S6_04_MAPS_MANIFOLDS` | `E.1.3` | III | `maps:src:E.1.3` | `5.3` |
| `S6_04_MAPS_MANIFOLDS` | `E.1.4` | III | `maps:src:E.1.4` | `5.4` |
| `S6_04_MAPS_MANIFOLDS` | `E.1.5` | III | `maps:src:E.1.5` | `5.5` |
| `S6_04_MAPS_MANIFOLDS` | `E.2.1` | III | `maps:src:E.2.1` | `5.6` |
| `S6_04_MAPS_MANIFOLDS` | `E.2.2` | III | `maps:src:E.2.2` | `A.8` |
| `S6_04_MAPS_MANIFOLDS` | `E.2.3` | III | `maps:src:E.2.3` | `5.7` |
| `S6_04_MAPS_MANIFOLDS` | `E.2.4` | III | `maps:src:E.2.4` | `5.8` |
| `S6_04_MAPS_MANIFOLDS` | `E.2.5` | III | `maps:src:E.2.5` | `5.9` |
| `S6_04_MAPS_MANIFOLDS` | `E.2.6` | III | `maps:src:E.2.6` | `5.10` |
| `S6_04_MAPS_MANIFOLDS` | `E.2.7` | III | `maps:src:E.2.7` | `5.11` |
| `S6_04_MAPS_MANIFOLDS` | `E.2.8` | III | `maps:src:E.2.8` | `5.12` |
| `S6_04_MAPS_MANIFOLDS` | `E.2.9` | III | `maps:src:E.2.9` | `5.13` |
| `S6_04_MAPS_MANIFOLDS` | `E.2.10` | III | `maps:src:E.2.10` | `5.14` |
| `S6_04_MAPS_MANIFOLDS` | `E.2.11` | III | `maps:src:E.2.11` | `5.15` |
| `S6_04_MAPS_MANIFOLDS` | `E.2.12` | III | `maps:src:E.2.12` | `5.16` |
| `S6_04_MAPS_MANIFOLDS` | `E.2.13` | III | `maps:src:E.2.13` | `5.17` |
| `S6_04_MAPS_MANIFOLDS` | `E.2.14` | III | `maps:src:E.2.14` | `5.18` |
| `S6_04_MAPS_MANIFOLDS` | `E.2.15` | III | `maps:src:E.2.15` | `5.19` |
| `S6_04_MAPS_MANIFOLDS` | `E.2.16` | III | `maps:src:E.2.16` | `5.20` |
| `S6_04_MAPS_MANIFOLDS` | `E.2.17` | III | `maps:src:E.2.17` | `5.21` |
| `S6_04_MAPS_MANIFOLDS` | `E.2.18` | III | `maps:src:E.2.18` | `5.22` |
| `S6_04_MAPS_MANIFOLDS` | `E.2.19` | III | `maps:src:E.2.19` | `5.23` |
| `S6_04_MAPS_MANIFOLDS` | `E.2.20` | III | `maps:src:E.2.20` | `5.24` |
| `S6_04_MAPS_MANIFOLDS` | `E.2.21` | III | `maps:src:E.2.21` | `5.25` |
| `S6_04_MAPS_MANIFOLDS` | `F.1.1` | III | `maps:src:F.1.1` | `6.1` |
| `S6_04_MAPS_MANIFOLDS` | `F.1.2` | III | `maps:src:F.1.2` | `A.9` |
| `S6_04_MAPS_MANIFOLDS` | `F.1.3` | III | `maps:src:F.1.3` | `A.10` |
| `S6_04_MAPS_MANIFOLDS` | `F.1.4` | III | `maps:src:F.1.4` | `6.2` |
| `S6_04_MAPS_MANIFOLDS` | `F.2.1` | III | `maps:src:F.2.1` | `6.3` |
| `S6_04_MAPS_MANIFOLDS` | `F.2.2` | III | `maps:src:F.2.2` | `6.4` |
| `S6_04_MAPS_MANIFOLDS` | `F.2.3` | III | `maps:src:F.2.3` | `6.5` |
| `S6_04_MAPS_MANIFOLDS` | `F.2.4` | III | `maps:src:F.2.4` | `6.53` |
| `S6_04_MAPS_MANIFOLDS` | `F.2.5` | III | `maps:src:F.2.5` | `6.8` |
| `S6_04_MAPS_MANIFOLDS` | `F.2.6` | III | `maps:src:F.2.6` | `6.10` |
| `S6_04_MAPS_MANIFOLDS` | `F.2.7` | III | `maps:src:F.2.7` | `6.12` |
| `S6_04_MAPS_MANIFOLDS` | `F.2.8` | III | `maps:src:F.2.8` | `6.14` |
| `S6_04_MAPS_MANIFOLDS` | `F.2.9` | III | `maps:src:F.2.9` | `6.15` |
| `S6_04_MAPS_MANIFOLDS` | `F.2.10` | III | `maps:src:F.2.10` | `6.16` |
| `S6_04_MAPS_MANIFOLDS` | `F.2.11` | III | `maps:src:F.2.11` | `6.17` |
| `S6_04_MAPS_MANIFOLDS` | `F.2.12` | III | `maps:src:F.2.12` | `6.18` |
| `S6_04_MAPS_MANIFOLDS` | `F.2.13` | III | `maps:src:F.2.13` | `6.19` |
| `S6_04_MAPS_MANIFOLDS` | `F.2.14` | III | `maps:src:F.2.14` | `6.20` |
| `S6_04_MAPS_MANIFOLDS` | `F.2.15` | III | `maps:src:F.2.15` | `6.13` |
| `S6_04_MAPS_MANIFOLDS` | `F.2.16` | III | `maps:src:F.2.16` | `6.21` |
| `S6_04_MAPS_MANIFOLDS` | `F.2.17` | III | `maps:src:F.2.17` | `6.22` |
| `S6_04_MAPS_MANIFOLDS` | `F.2.18` | III | `maps:src:F.2.18` | `6.23` |
| `S6_04_MAPS_MANIFOLDS` | `F.2.19` | III | `maps:src:F.2.19` | `6.24` |
| `S6_04_MAPS_MANIFOLDS` | `F.2.20` | III | `maps:src:F.2.20` | `6.25` |
| `S6_04_MAPS_MANIFOLDS` | `F.2.21` | III | `maps:src:F.2.21` | `6.26` |
| `S6_04_MAPS_MANIFOLDS` | `F.2.22` | III | `maps:src:F.2.22` | `6.27` |
| `S6_04_MAPS_MANIFOLDS` | `F.2.23` | III | `maps:src:F.2.23` | `6.28` |
| `S6_04_MAPS_MANIFOLDS` | `F.2.24` | III | `maps:src:F.2.24` | `6.29` |
| `S6_04_MAPS_MANIFOLDS` | `F.2.25` | III | `maps:src:F.2.25` | `6.30` |
| `S6_04_MAPS_MANIFOLDS` | `F.2.26` | III | `maps:src:F.2.26` | `6.31` |
| `S6_04_MAPS_MANIFOLDS` | `F.2.27` | III | `maps:src:F.2.27` | `6.32` |
| `S6_04_MAPS_MANIFOLDS` | `F.2.28` | III | `maps:src:F.2.28` | `6.33` |
| `S6_04_MAPS_MANIFOLDS` | `F.2.29` | III | `maps:src:F.2.29` | `6.34` |
| `S6_04_MAPS_MANIFOLDS` | `F.2.30` | III | `maps:src:F.2.30` | `6.35` |
| `S6_04_MAPS_MANIFOLDS` | `F.2.31` | III | `maps:src:F.2.31` | `6.36` |
| `S6_04_MAPS_MANIFOLDS` | `F.2.32` | III | `maps:src:F.2.32` | `6.37` |
| `S6_04_MAPS_MANIFOLDS` | `F.2.33` | III | `maps:src:F.2.33` | `6.38` |
| `S6_04_MAPS_MANIFOLDS` | `F.2.34` | III | `maps:src:F.2.34` | `6.39` |
| `S6_04_MAPS_MANIFOLDS` | `F.2.35` | III | `maps:src:F.2.35` | `6.40` |
| `S6_04_MAPS_MANIFOLDS` | `F.2.36` | III | `maps:src:F.2.36` | `6.41` |
| `S6_04_MAPS_MANIFOLDS` | `F.2.37` | III | `maps:src:F.2.37` | `6.42` |
| `S6_04_MAPS_MANIFOLDS` | `F.2.38` | III | `maps:src:F.2.38` | `6.43` |
| `S6_04_MAPS_MANIFOLDS` | `F.2.39` | III | `maps:src:F.2.39` | `6.44` |
| `S6_04_MAPS_MANIFOLDS` | `F.3.1` | III | `maps:src:F.3.1` | `6.6` |
| `S6_04_MAPS_MANIFOLDS` | `F.3.2` | III | `maps:src:F.3.2` | `6.7` |
| `S6_04_MAPS_MANIFOLDS` | `F.3.3` | III | `maps:src:F.3.3` | `6.54` |
| `S6_04_MAPS_MANIFOLDS` | `F.3.4` | III | `maps:src:F.3.4` | `6.11` |
| `S6_04_MAPS_MANIFOLDS` | `F.3.5` | III | `maps:src:F.3.5` | `6.45` |
| `S6_04_MAPS_MANIFOLDS` | `F.3.6` | III | `maps:src:F.3.6` | `6.46` |
| `S6_04_MAPS_MANIFOLDS` | `F.3.7` | III | `maps:src:F.3.7` | `6.47` |
| `S6_04_MAPS_MANIFOLDS` | `F.3.8` | III | `maps:src:F.3.8` | `6.48` |
| `S6_04_MAPS_MANIFOLDS` | `F.3.9` | III | `maps:src:F.3.9` | `6.49` |
| `S6_04_MAPS_MANIFOLDS` | `F.3.10` | III | `maps:src:F.3.10` | `6.50` |
| `S6_04_MAPS_MANIFOLDS` | `F.3.11` | III | `maps:src:F.3.11` | `6.51` |
| `S6_04_MAPS_MANIFOLDS` | `F.4.1` | III | `maps:src:F.4.1` | `6.52` |
| `S6_05_ARITHMETIC` | `C.1.1` | I | `ari:C.1.1` | `12.1` |
| `S6_05_ARITHMETIC` | `C.1.2` | I | `ari:C.1.2` | `12.2` |
| `S6_05_ARITHMETIC` | `C.1.3` | I | `ari:C.1.3` | `12.3` |
| `S6_05_ARITHMETIC` | `C.2.1` | I | `ari:C.2.1` | `12.4` |
| `S6_05_ARITHMETIC` | `C.2.2` | I | `ari:C.2.2` | `12.5` |
| `S6_05_ARITHMETIC` | `C.3.1` | I | `ari:C.3.1` | `12.6` |
| `S6_05_ARITHMETIC` | `C.3.2` | I | `ari:C.3.2` | `12.7` |
| `S6_05_ARITHMETIC` | `C.4.1` | I | `ari:C.4.1` | `12.8` |
| `S6_05_ARITHMETIC` | `C.4.2` | I | `ari:C.4.2` | `12.9` |
| `S6_05_ARITHMETIC` | `C.4.3` | I | `ari:C.4.3` | `12.10` |
| `S6_05_ARITHMETIC` | `C.4.4` | I | `ari:C.4.4` | `12.11` |
| `S6_05_ARITHMETIC` | `C.4.5` | I | `ari:C.4.5` | `12.12` |
| `S6_05_ARITHMETIC` | `C.5.1` | I | `ari:C.5.1` | `12.13` |
| `S6_05_ARITHMETIC` | `C.6.1` | I | `ari:C.6.1` | `13.1` |
| `S6_05_ARITHMETIC` | `C.6.2` | I | `ari:C.6.2` | `13.2` |
| `S6_05_ARITHMETIC` | `C.6.3` | I | `ari:C.6.3` | `13.3` |
| `S6_05_ARITHMETIC` | `C.6.4` | I | `ari:C.6.4` | `13.4` |
| `S6_05_ARITHMETIC` | `C.6.5` | I | `ari:C.6.5` | `13.5` |
| `S6_05_ARITHMETIC` | `C.6.R1` | I | `ari:C.6.R1` | `13.6` |
| `S6_05_ARITHMETIC` | `C.6.R2` | I | `ari:C.6.R2` | `13.7` |
| `S6_05_ARITHMETIC` | `C.6.R3` | I | `ari:C.6.R3` | `13.8` |
| `S6_05_ARITHMETIC` | `C.6.R4` | I | `ari:C.6.R4` | `13.9` |
| `S6_05_ARITHMETIC` | `C.6.R5` | I | `ari:C.6.R5` | `13.10` |
| `S6_05_ARITHMETIC` | `C.6.T1` | I | `ari:C.6.T1` | `13.11` |
| `S6_05_ARITHMETIC` | `C.6.T2` | I | `ari:C.6.T2` | `13.12` |
| `S6_05_ARITHMETIC` | `C.8.1` | I | `ari:C.8.1` | `14.1` |
| `S6_05_ARITHMETIC` | `C.8.2` | I | `ari:C.8.2` | `14.2` |
| `S6_05_ARITHMETIC` | `C.8.3` | I | `ari:C.8.3` | `14.3` |
| `S6_05_ARITHMETIC` | `C.8.4` | I | `ari:C.8.4` | `14.4` |
| `S6_05_ARITHMETIC` | `C.8.5` | I | `fam:src:C.2.3` | `5.5` |
| `S6_05_ARITHMETIC` | `C.8.6` | I | `ari:C.8.6` | `14.5` |
| `S6_05_ARITHMETIC` | `C.8.7` | I | `ari:C.8.7` | `14.6` |
| `S6_05_ARITHMETIC` | `C.8.8` | I | `ari:C.8.8` | `14.7` |
| `S6_05_ARITHMETIC` | `C.8.9` | I | `ari:C.8.9` | `14.8` |
| `S6_05_ARITHMETIC` | `C.8.10` | I | `ari:C.8.10` | `14.9` |
| `S6_05_ARITHMETIC` | `C.8.11` | I | `ari:C.8.11` | `14.10` |
| `S6_05_ARITHMETIC` | `C.8.12` | I | `ari:C.8.12` | `15.1` |
| `S6_05_ARITHMETIC` | `C.8.13` | I | `ari:C.8.13` | `15.2` |
| `S6_05_ARITHMETIC` | `C.8.14` | I | `ari:C.8.14` | `15.3` |
| `S6_05_ARITHMETIC` | `C.8.15` | I | `ari:C.8.15` | `15.4` |
| `S6_05_ARITHMETIC` | `C.7.1` | I | `ari:C.7.1` | `16.1` |
| `S6_05_ARITHMETIC` | `C.7.2` | I | `ari:C.7.2` | `16.2` |
| `S6_05_ARITHMETIC` | `C.7.3` | I | `ari:C.7.3` | `16.3` |
| `S6_05_ARITHMETIC` | `C.7.4` | I | `ari:C.7.4` | `16.4` |
| `S6_05_ARITHMETIC` | `C.7.5` | I | `ari:C.7.5` | `16.5` |
| `S6_05_ARITHMETIC` | `C.7.6` | I | `ari:C.7.6` | `16.6` |
| `S6_05_ARITHMETIC` | `C.7.7` | I | `ari:C.7.7` | `16.7` |
| `S6_05_ARITHMETIC` | `C.7.8` | I | `ari:C.7.8` | `16.8` |
| `S6_05_ARITHMETIC` | `C.7.9` | I | `ari:C.7.9` | `16.9` |
| `S6_05_ARITHMETIC` | `C.7.10` | I | `ari:C.7.10` | `16.10` |
| `S6_05_ARITHMETIC` | `C.7.11` | I | `ari:C.7.11` | `16.11` |
| `S6_05_ARITHMETIC` | `C.7.12` | I | `ari:C.7.12` | `16.12` |
| `WORKING_EDITION` | `lem:triangle-generator-orientations` | I | `wb:lem:triangle-generator-orientations` | `B.1` |
| `WORKING_EDITION` | `prop:period-input-audit` | I | `wb:prop:period-input-audit` | `B.2` |
| `WORKING_EDITION` | `prop:period-exact-admissible-constants` | I | `wb:prop:period-exact-admissible-constants` | `B.3` |
| `WORKING_EDITION` | `lem:toric-chart-control` | I | `wb:lem:toric-chart-control` | `B.5` |
| `WORKING_EDITION` | `thm:candidate-cusp-geometry` | I | `wb:thm:candidate-cusp-geometry` | `B.6` |
| `WORKING_EDITION` | `prop:candidate-cusp-overlap` | I | `wb:prop:candidate-cusp-overlap` | `B.7` |
| `WORKING_EDITION` | `lem:middle-period-proper` | I | `wb:lem:middle-period-proper` | `B.8` |
| `WORKING_EDITION` | `prop:candidate-finite-fillings` | I | `wb:prop:candidate-finite-fillings` | `B.9` |
| `WORKING_EDITION` | `lem:finite-filling-stalk-map` | I | `wb:lem:finite-filling-stalk-map` | `B.10` |
| `WORKING_EDITION` | `thm:candidate-global-geometry` | I | `wb:thm:candidate-global-geometry` | `B.11` |
| `WORKING_EDITION` | `prop:monodromy-certificate` | I | `wb:prop:monodromy-certificate` | `C.1` |
| `WORKING_EDITION` | `thm:cusp-lattices` | I | `wb:thm:cusp-lattices` | `C.2` |
| `WORKING_EDITION` | `thm:coinvariants` | I | `wb:thm:coinvariants` | `C.3` |
| `WORKING_EDITION` | `prop:finite-indices` | I | `wb:prop:finite-indices` | `C.4` |
| `WORKING_EDITION` | `prop:terminal-group` | I | `wb:prop:terminal-group` | `C.5` |
| `WORKING_EDITION` | `prop:terminal-degree-two` | I | `wb:prop:terminal-degree-two` | `C.6` |
| `WORKING_EDITION` | `prop:terminal-all-degree` | I | `wb:prop:terminal-all-degree` | `C.7` |
| `WORKING_EDITION` | `ffcert:prop:integral-summands` | I | `wb:ffcert:prop:integral-summands` | `C.9` |
| `WORKING_EDITION` | `ffcert:thm:product-covers` | I | `wb:ffcert:thm:product-covers` | `C.10` |
| `WORKING_EDITION` | `ffcert:prop:quotient-charts` | I | `wb:ffcert:prop:quotient-charts` | `C.11` |
| `WORKING_EDITION` | `ffcert:thm:normalization` | I | `wb:ffcert:thm:normalization` | `C.12` |
| `WORKING_EDITION` | `ffcert:thm:peripheral-kernel` | I | `wb:ffcert:thm:peripheral-kernel` | `C.13` |
| `WORKING_EDITION` | `ffcert:cor:covering-h1` | I | `wb:ffcert:cor:covering-h1` | `C.14` |
| `WORKING_EDITION` | `ffcert:thm:normal-trivialization` | I | `wb:ffcert:thm:normal-trivialization` | `C.15` |
| `WORKING_EDITION` | `lem:torus-algebraic-reduction-audit` | I | `wb:lem:torus-algebraic-reduction-audit` | `J.1` |
| `WORKING_EDITION` | `prop:very-general-torus-audit` | I | `wb:prop:very-general-torus-audit` | `J.2` |
| `WORKING_EDITION` | `lem:meromorphic-descent-audit` | I | `wb:lem:meromorphic-descent-audit` | `J.3` |
| `WORKING_EDITION` | `thm:algebraic-dimension-audit` | I | `wb:thm:algebraic-dimension-audit` | `J.4` |
| `WORKING_EDITION` | `thm:canonical-ring-recovery` | I | `wb:thm:canonical-ring-recovery` | `O.1` |
| `WORKING_EDITION` | `thm:retained-period-deformation` | I | `wb:thm:retained-period-deformation` | `O.2` |
| `WORKING_EDITION` | `pshift:thm:classification` | I | `wb:pshift:thm:classification` | `3.8` |
| `WORKING_EDITION` | `pshift:lem:centralizer` | I | `wb:pshift:lem:centralizer` | `O.3` |
| `WORKING_CDP` | `prop:missing-cotangent-filtration` | II | `wbII:prop:missing-cotangent-filtration` | `5.1` |
| `WORKING_CDP` | `prop:missing-global-section-criterion` | II | `wbII:prop:missing-global-section-criterion` | `5.1` |
| `WORKING_CDP` | `lem:conormal-injective` | II | `wbII:lem:conormal-injective` | `5.1` |
| `WORKING_CDP` | `lem:conductor-square` | II | `wbII:lem:conductor-square` | `5.3` |
| `WORKING_CDP` | `prop:conductor` | II | `wbII:prop:conductor` | `B.2` |
| `WORKING_CDP` | `prop:nodal-counterexample` | II | `wbII:prop:nodal-counterexample` | `5.8` |
| `WORKING_CDP` | `thm:cartier-duality` | II | `wbII:thm:cartier-duality` | `B.7` |
| `WORKING_CDP` | `prop:cartier-duality-absolute` | II | `wbII:prop:cartier-duality-absolute` | `B.8` |
| `WORKING_CDP` | `lem:curve-flatness` | II | `wbII:lem:curve-flatness` | `B.9` |
| `WORKING_CDP` | `prop:analytic-base-change` | II | `wbII:prop:analytic-base-change` | `B.10` |
| `WORKING_CDP` | `cor:surface-top-base-change` | II | `wbII:cor:surface-top-base-change` | `B.11` |
| `WORKING_CDP` | `prop:pic0-pullback` | II | `wbII:prop:pic0-pullback` | `B.12` |
| `WORKING_CDP` | `prop:all-pic-restriction` | II | `wbII:prop:all-pic-restriction` | `B.13` |
| `WORKING_CDP` | `prop:leray-edge-restriction` | II | `wbII:prop:leray-edge-restriction` | `B.14` |
| `WORKING_CDP` | `lem:picard-crossed-defect` | II | `wbII:lem:picard-crossed-defect` | `B.15` |
| `WORKING_CDP` | `lem:picard-finite-norm` | II | `wbII:lem:picard-finite-norm` | `B.16` |
| `WORKING_CDP` | `lem:picard-cusp-defect` | II | `wbII:lem:picard-cusp-defect` | `B.17` |
| `WORKING_CDP` | `prop:direct-boundary-picard` | II | `wbII:prop:direct-boundary-picard` | `B.18` |
| `WORKING_CDP` | `cor:candidate-pic0-route` | II | `wbII:cor:candidate-pic0-route` | `B.24` |
| `WORKING_CDP` | `thm:candidate-conductor` | II | `wbII:thm:candidate-conductor` | `B.26` |
| `WORKING_CDP` | `cor:candidate-conductor-actual` | II | `wbII:cor:candidate-conductor-actual` | `B.27` |
| `WORKING_CDP` | `lem:semidirect-abelianization` | I | `wb:lem:semidirect-abelianization` | `C.8` |
| `WORKING_CDP` | `lem:cdp-generic-endpoints` | II | `wbII:lem:cdp-generic-endpoints` | `B.29` |
| `WORKING_CDP` | `thm:corrected-cdp-global` | II | `wbII:thm:corrected-cdp-global` | `B.30` |
| `WORKING_CDP` | `cor:corrected-cdp-relative` | II | `wbII:cor:corrected-cdp-relative` | `B.31` |
| `WORKING_CDP` | `thm:corrected-cdp-fibrewise` | II | `wbII:thm:corrected-cdp-fibrewise` | `B.32` |
| `WORKING_CDP` | `test:cdp-comparison` | II | `wbII:test:cdp-comparison` | `B.34` |
| `CORRECTION_NOTE_20260901` | `lem:torsion-identification` | II | `wbII:lem:torsion-identification` | `B.1` |
| `CORRECTION_NOTE_20260901` | `lem:conormal` | II | `wbII:lem:conormal` | `5.1` |
| `CORRECTION_NOTE_20260901` | `prop:filtration` | II | `wbII:prop:filtration` | `5.1` |
| `CORRECTION_NOTE_20260901` | `prop:criterion` | II | `wbII:prop:criterion` | `5.1` |
| `CORRECTION_NOTE_20260901` | `lem:conductor` | II | `wbII:lem:conductor` | `5.3` |
| `CORRECTION_NOTE_20260901` | `prop:conductor-differential` | II | `wbII:prop:conductor-differential` | `B.2` |
| `CORRECTION_NOTE_20260901` | `cor:normal-crossing-kernel` | II | `wbII:cor:normal-crossing-kernel` | `B.3` |
| `CORRECTION_NOTE_20260901` | `prop:family-geometry` | II | `wbII:prop:family-geometry` | `5.8` |
| `CORRECTION_NOTE_20260901` | `lem:gluing-bundle` | II | `wbII:lem:gluing-bundle` | `B.4` |
| `CORRECTION_NOTE_20260901` | `lem:extending-gluing` | II | `wbII:lem:extending-gluing` | `B.5` |
| `CORRECTION_NOTE_20260901` | `thm:nodal-test` | II | `wbII:thm:nodal-test` | `5.8` |
| `CORRECTION_NOTE_20260901` | `lem:generic-endpoints` | II | `wbII:lem:generic-endpoints` | `B.28` |
| `CORRECTION_NOTE_20260901` | `thm:corrected-global` | II | `wbII:thm:corrected-global` | `B.30` |
| `CORRECTION_NOTE_20260901` | `cor:relative` | II | `wbII:cor:relative` | `B.31` |
| `CORRECTION_NOTE_20260901` | `prop:relative-local` | II | `wbII:prop:relative-local` | `B.35` |
| `WORKING_CDP` | `prop:local-cusp-picard-obstruction` | II | `wbII:prop:local-cusp-picard-obstruction` | `B.19` |
| `WORKING_CDP` | `prop:analytic-ah-boundary` | II | `wbII:prop:analytic-ah-boundary` | `B.21` |
| `WORKING_CDP` | `lem:analytic-support-specialization` | II | `wbII:lem:analytic-support-specialization` | `B.22` |
| `WORKING_CDP` | `thm:analytic-all-picard` | II | `wbII:thm:analytic-all-picard` | `B.23` |
| `working_edition` | `thm:p0-integral-specialization` | I | `mapsI:top:thm:p0-integral-specialization` | `D.1` |
| `working_edition` | `prop:leray-e2` | I | `mapsI:top:prop:leray-e2` | `D.2` |
| `working_edition` | `lem:first-transgression` | I | `mapsI:top:lem:first-transgression` | `D.3` |
| `working_edition` | `lem:higher-transgressions` | I | `mapsI:top:lem:higher-transgressions` | `D.4` |
| `working_edition` | `thm:h2-vanishing` | I | `mapsI:top:thm:h2-vanishing` | `D.5` |
| `working_edition` | `prop:geometric-pi1` | I | `mapsI:top:prop:geometric-pi1` | `D.6` |
| `working_edition` | `cor:candidate-sphere` | I | `mapsI:top:cor:candidate-sphere` | `D.7` |
| `working_edition` | `prop:topological-spine` | I | `mapsI:top:prop:topological-spine` | `E.1` |
| `working_edition` | `lem:collapse-straightening` | I | `mapsI:top:lem:collapse-straightening` | `E.2` |
| `working_edition` | `lem:positive-collapse` | I | `mapsI:top:lem:positive-collapse` | `E.3` |
| `working_edition` | `lem:phase-spread-collapse` | I | `mapsI:top:lem:phase-spread-collapse` | `E.4` |
| `working_edition` | `prop:verified-cellular-collapse` | I | `mapsI:top:prop:verified-cellular-collapse` | `E.5` |
| `working_edition` | `prop:verified-collapse-homology` | I | `mapsI:top:prop:verified-collapse-homology` | `E.6` |
| `working_edition` | `thm:collapse-equals-specialization` | I | `mapsI:top:thm:collapse-equals-specialization` | `E.7` |
| `working_edition` | `topology_reduction:L600` | I | `mapsI:top:remark:L600` | `E.8` |
| `working_edition` | `record:vankampen` | I | `mapsI:top:record:vankampen` | `E.9` |
| `working_edition` | `prop:actual-finite-band-maps` | I | `mapsI:top:prop:actual-finite-band-maps` | `E.10` |
| `working_edition` | `prop:cusp-mv-blocks` | I | `mapsI:top:prop:cusp-mv-blocks` | `E.12` |
| `working_edition` | `topology_reduction:L920` | I | `mapsI:top:remark:L920` | `E.13` |
| `working_edition` | `thm:mv-leray-comparison` | I | `mapsI:top:thm:mv-leray-comparison` | `E.14` |
| `working_edition` | `topology_reduction:L1113` | I | `mapsI:top:remark:L1113` | `E.15` |
| `working_edition` | `lem:cohomological-closure` | I | `mapsI:top:lem:cohomological-closure` | `E.16` |
| `working_edition` | `thm:sphere-recognition` | I | `mapsI:top:thm:sphere-recognition` | `E.17` |
| `working_edition` | `cor:abstract-s6` | I | `mapsI:top:cor:abstract-s6` | `E.18` |
| `working_edition` | `cor:candidate-mv-sphere` | I | `mapsI:top:cor:candidate-mv-sphere` | `E.19` |
| `working_edition` | `cusp-cover-extension-theorem` | III | `wb:cusp-cover-extension-theorem` | `9.1` |
| `working_edition` | `cusp-cover-naive-action-failure` | III | `wb:cusp-cover-naive-action-failure` | `9.2` |
| `working_edition` | `cusp-cover-global-scope` | III | `wb:cusp-cover-global-scope` | `9.3` |
| `working_edition` | `cusp-spec-globalization-obstruction` | III | `wb:cusp-spec-globalization-obstruction` | `9.6` |
| `working_edition` | `cusp-cone-native-descent` | III | `wb:cusp-cone-native-descent` | `9.7` |
| `working_edition` | `cusp-cone-S12-route` | III | `wb:cusp-cone-S12-route` | `9.8` |
| `working_edition` | `cusp-cone-S24-local-route` | III | `wb:cusp-cone-S24-local-route` | `9.9` |
| `working_edition` | `cusp-cone-S24-route` | III | `wb:cusp-cone-S24-route` | `9.10` |
| `working_edition` | `cusp-cone-target-slice-embeddings` | III | `wb:cusp-cone-target-slice-embeddings` | `9.11` |
| `working_edition` | `cusp-cone-metric-scope` | III | `wb:cusp-cone-metric-scope` | `9.12` |
| `working_edition` | `cusp-cone-S12-almost-complex-obstruction` | III | `wb:cusp-cone-S12-almost-complex-obstruction` | `A.1` |
| `working_edition` | `cusp-cone-obstructions` | III | `wb:cusp-cone-obstructions` | `9.13` |
| `working_edition` | `cusp-cone-optimal-exponents` | III | `wb:cusp-cone-optimal-exponents` | `9.14` |
| `working_edition` | `cusp-cone-angle-forgotten-sphere-carriers` | III | `wb:cusp-cone-angle-forgotten-sphere-carriers` | `9.15` |
| `working_edition` | `cusp-cone-S12-sphere-map-null` | III | `wb:cusp-cone-S12-sphere-map-null` | `9.16` |
| `working_edition` | `cusp-cone-S24-sphere-map-null` | III | `wb:cusp-cone-S24-sphere-map-null` | `9.17` |
| `working_edition` | `cusp-cone-literal-R4-open-cells` | III | `wb:cusp-cone-literal-R4-open-cells` | `9.18` |
| `working_edition` | `cusp-cone-moving-S4-null-homotopy` | III | `wb:cusp-cone-moving-S4-null-homotopy` | `9.19` |
| `working_edition` | `cusp-cone-sphere-map-homotopy-status` | III | `wb:cusp-cone-sphere-map-homotopy-status` | `9.20` |
| `working_edition` | `cusp-cone-explicit-carriers` | III | `wb:cusp-cone-explicit-carriers` | `9.21` |
| `working_edition` | `cusp-cone-target-homotopy-types` | III | `wb:cusp-cone-target-homotopy-types` | `9.22` |
| `working_edition` | `cusp-cone-exact-decompactification-space` | III | `wb:cusp-cone-exact-decompactification-space` | `9.23` |
| `working_edition` | `cusp-cone-sharp-global-R4-scope` | III | `wb:cusp-cone-sharp-global-R4-scope` | `9.24` |
| `working_edition` | `cusp-s12-full-carrier-null` | III | `wb:cusp-s12-full-carrier-null` | `9.25` |
| `working_edition` | `cusp-s12-all-higher-smashes-null` | III | `wb:cusp-s12-all-higher-smashes-null` | `9.26` |
| `working_edition` | `cusp-s12-one-copy-invariant` | III | `wb:cusp-s12-one-copy-invariant` | `9.27` |
| `working_edition` | `cusp-s12-nullity-scope` | III | `wb:cusp-s12-nullity-scope` | `9.28` |
| `working_edition` | `cusp-null:thm` | III | `wb:cusp-null:thm` | `9.29` |
| `working_edition` | `cusp_s12_carrier_homotopy:L567` | III | `wb:cusp_s12_carrier_homotopy:L567` | `9.30` |
| `course_CG-S6` | `CG-S6-11-TYPES` | III | `courseIII:almost-complex-structures-and-integrability:section-1` | `AI.1` |
| `course_CG-S6` | `CG-S6-11-OCTONIONS` | III | `courseIII:almost-complex-structures-and-integrability:section-2` | `AI.2` |
| `course_CG-S6` | `CG-S6-11-NIJENHUIS` | III | `courseIII:almost-complex-structures-and-integrability:section-3` | `AI.3` |
| `course_CG-S6` | `CG-S6-11-ASSOCIATOR` | III | `courseIII:almost-complex-structures-and-integrability:section-4` | `AI.4` |
| `course_CG-S6` | `CG-S6-11-TRANSPORT` | III | `courseIII:almost-complex-structures-and-integrability:section-5` | `AI.5` |
| `course_CG-S6` | `CG-S6-11-COORDINATES` | III | `courseIII:almost-complex-structures-and-integrability:section-6` | `AI.6` |
| `course_CG-S6` | `CG-S6-11-GAUGE` | III | `courseIII:almost-complex-structures-and-integrability:section-7` | `AI.7` |
| `course_CG-S6` | `CG-S6-11-ANALYTIC` | III | `courseIII:almost-complex-structures-and-integrability:section-8` | `AI.8` |
| `course_CG-S6` | `CG-S6-11-INTEGRABILITY` | III | `courseIII:almost-complex-structures-and-integrability:section-9` | `AI.9` |
| `course_CG-S6` | `CG-S6-11-SPHERES` | III | `courseIII:almost-complex-structures-and-integrability:section-10` | `AI.10` |
| `course_CG-S6` | `CG-S6-11-EXERCISES` | III | `courseIII:almost-complex-structures-and-integrability:section-11` | `AI.11` |
| `course_CG-S6` | `CG-S6-07-HOMOLOGY` | I | `mapsI:top:lem:cohomological-closure` | `E.16` |
| `course_CG-S6` | `CG-S6-07-HOMOTOPY` | I | `mapsI:course:CG-S6-07-HOMOTOPY` | `I.1` |
| `course_CG-S6` | `CG-S6-07-SMOOTH` | III | `courseIII:integral-homology-and-sphere-recognition:section` | `AH` |
| `course_CG-S6` | `twist-actual-tube` | III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:twist-actual-tube` | `AG.1` |
| `course_CG-S6` | `twist-signed-action` | III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:twist-signed-action` | `AG.2` |
| `course_CG-S6` | `twist-integral-lagrangians` | III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:twist-integral-lagrangians` | `AG.3` |
| `course_CG-S6` | `twist-original-middle-level` | III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:twist-original-middle-level` | `AG.4` |
| `course_CG-S6` | `twist-original-gluing` | III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:twist-original-gluing` | `AG.5` |
| `course_CG-S6` | `twist-actual-cancellation` | III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:twist-actual-cancellation` | `AG.6` |
| `course_CG-S6` | `twist-original-smooth-map` | III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:twist-original-smooth-map` | `AG.7` |
| `course_CG-S6` | `twist-general-stable-framing` | III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:twist-general-stable-framing` | `AG.7.1` |
| `course_CG-S6` | `twist-worked-exercises` | III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:twist-worked-exercises` | `AG.8` |
| `working_edition_reader_extension` | `G2-8` | III | `mapsaudit:almost-complex-homotopy` | `A.2` |
| `WORKING_INV` | `prop:workbench-holomorphic-form-vanishing` | I | `inv:A3.1` | `8.9` |
| `WORKING_INV` | `thm:parametric-hodge-diamond` | I | `inv:A3.1` | `8.9` |
| `WORKING_INV` | `thm:frolicher-e2-candidate` | I | `inv:C1.1` | `10.1` |
| `WORKING_INV` | `prop:period-derivative-determinant` | I | `inv:A2.1` | `8.5` |
| `WORKING_INV` | `prop:log-relative-direct-images` | I | `inv:A1.2` | `8.3` |
| `WORKING_INV` | `prop:log-ks-divisor` | I | `inv:A2.1` | `8.5` |
| `WORKING_INV` | `prop:absolute-cotangent-direct-images` | I | `inv:A1.3` | `8.4` |
| `WORKING_INV` | `hodge_frolicher:remark:8` | I | `inv:A4.1` | `8.11` |
| `WORKING_INV` | `thm:h12-scalar` | I | `inv:A2.4` | `8.8` |
| `WORKING_INV` | `cor:exact-hodge-diamond` | I | `inv:A3.1` | `8.9` |
| `WORKING_INV` | `thm:exact-bott-chern-aeppli` | I | `inv:C2.1` | `10.3` |
| `WORKING_INV` | `record:h12-direct-images` | I | `inv:A1.3` | `8.4` |
| `WORKING_INV` | `lem:bcpr-degree-one-input` | I | `inv:C3.2` | `10.6` |
| `WORKING_INV` | `lem:bcpr-eta-extension` | I | `inv:A3.2` | `8.10` |
| `WORKING_INV` | `rem:bcpr-literal-gauge` | I | `inv:C3.8` | `T.3` |
| `WORKING_INV` | `prop:bcpr-generators-are-bases` | I | `inv:C3.3` | `10.7` |
| `WORKING_INV` | `thm:bcpr-square-zero-algebra` | I | `inv:C3.3` | `10.7` |
| `WORKING_INV` | `rem:bcpr-global-gauge-boundary` | I | `inv:C3.8` | `T.3` |
| `WORKING_INV` | `formula:bcpr-fibre-representatives` | I | `inv:C3.7` | `10.11` |
| `WORKING_INV` | `formula:bcpr-factor-twelve-chern` | I | `inv:C3.2` | `10.6` |
| `WORKING_INV` | `lem:hodge-line-audit` | I | `mapsI:hodge:line` | `L.1` |
| `WORKING_INV` | `lem:finite-normal-order-audit` | I | `wb:ffcert:thm:normal-trivialization` | `C.15` |
| `WORKING_INV` | `lem:cusp-structure-sheaf-audit` | I | `inv:A1.0` | `8.1` |
| `WORKING_INV` | `thm:structure-direct-images-audit` | I | `inv:A1.0` | `8.1` |
| `WORKING_INV` | `cor:picard-line-audit` | I | `inv:C3.1` | `10.5` |
| `WORKING_INV` | `thm:uniform-nontorsion-audit` | II | `wb:thm:uniform-nontorsion-audit` | `A.12` |
| `WORKING_INV` | `analytic_picard:remark:7` | II | `inv:wb:uniform-nontorsion-provenance` | `A.13` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-CHAIN-LEMMA-1.1` | I | `mapsI:chain:lemma:1.1` | `F.1` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-CHAIN-LEMMA-2.1` | I | `mapsI:chain:lemma:2.1` | `F.2` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-CHAIN-COROLLARY-2.2` | I | `mapsI:chain:corollary:2.2` | `F.3` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-CHAIN-LEMMA-4.1` | I | `mapsI:chain:lemma:4.1` | `F.4` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-CW-THEOREM-4.1` | I | `mapsI:cw:hurewicz-theorem-result` | `G.1` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-CW-EXERCISE-5.1` | I | `mapsI:cw:exercise:5.1` | `G.2` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-CW-EXERCISE-5.2` | I | `mapsI:cw:exercise:5.2` | `G.3` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-PF-THEOREM-5.1` | I | `mapsI:pf:theorem:5.1` | `H.1` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-PF-EXERCISE-6.1` | I | `mapsI:pf:exercise:6.1` | `H.2` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-PF-EXERCISE-6.2` | I | `mapsI:pf:exercise:6.2` | `H.3` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-CHAIN-LEMMA-5.1` | III | `courseIII:thom-euler-for-lesson11:CG-S6-CHAIN-LEMMA-5.1` | `C.1` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-CHAIN-THEOREM-5.2` | III | `courseIII:thom-euler-for-lesson11:CG-S6-CHAIN-THEOREM-5.2` | `C.2` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-CHAIN-PROPOSITION-6.1` | III | `courseIII:thom-euler-for-lesson11:CG-S6-CHAIN-PROPOSITION-6.1` | `C.3` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-CHAIN-THEOREM-7.1` | III | `courseIII:thom-euler-for-lesson11:CG-S6-CHAIN-THEOREM-7.1` | `C.4` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-CHAIN-PROPOSITION-8.1` | III | `courseIII:thom-euler-for-lesson11:CG-S6-CHAIN-PROPOSITION-8.1` | `C.5` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-CHAIN-PROPOSITION-8.2` | III | `courseIII:thom-euler-for-lesson11:CG-S6-CHAIN-PROPOSITION-8.2` | `C.6` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-PROJECTIVE-1` | III | `courseIII:projective-splitting-for-lesson11:CG-S6-PROJECTIVE-1` | `D.1` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-PROJECTIVE-2` | III | `courseIII:projective-splitting-for-lesson11:CG-S6-PROJECTIVE-2` | `D.2` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-PROJECTIVE-3` | III | `courseIII:projective-splitting-for-lesson11:CG-S6-PROJECTIVE-3` | `D.3` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-PROJECTIVE-4` | III | `courseIII:projective-splitting-for-lesson11:CG-S6-PROJECTIVE-4` | `D.4` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-PROJECTIVE-5` | III | `courseIII:projective-splitting-for-lesson11:CG-S6-PROJECTIVE-5` | `D.5` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-CHERN-1` | III | `courseIII:integral-chern-classes-for-lesson11:CG-S6-CHERN-1` | `E.1` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-CHERN-2` | III | `courseIII:integral-chern-classes-for-lesson11:CG-S6-CHERN-2` | `E.2` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-CHERN-3` | III | `courseIII:integral-chern-classes-for-lesson11:CG-S6-CHERN-3` | `E.3` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-FRAMED6-1` | III | `courseIII:framed6:1` | `AF.1` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-FRAMED6-2` | III | `courseIII:framed6:2` | `AF.2` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-FRAMED6-3` | III | `courseIII:framed6:3` | `AF.3` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-FRAMED6-4` | III | `courseIII:framed6:4` | `AF.4` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-FRAMED6-5` | III | `courseIII:framed6:5` | `AF.5` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-FRAMED6-6` | III | `courseIII:framed6:6` | `AF.6` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-FRAMED6-7` | III | `courseIII:framed6:7` | `AF.7` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-FRAMED6-8` | III | `courseIII:framed6:8` | `AF.8` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-FRAMED6-9` | III | `courseIII:framed6:9` | `AF.9` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-FRAMED6-10.1` | III | `courseIII:framed6:10.1` | `AF.10.1` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-FRAMED6-10.2` | III | `courseIII:framed6:10.2` | `AF.10.2` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-WHITNEY-RECEIVING-1` | III | `courseIII:whitney-receiving:1` | `R.1` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-WHITNEY-RECEIVING-2` | III | `courseIII:whitney-receiving:2` | `R.2` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-WHITNEY-RECEIVING-3` | III | `courseIII:whitney-receiving:3` | `R.3` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-WHITNEY-RECEIVING-4` | III | `courseIII:whitney-receiving:4` | `R.4` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-WHITNEY-RECEIVING-5.1` | III | `courseIII:whitney-receiving:5.1` | `R.5.1` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-WHITNEY-RECEIVING-5.2` | III | `courseIII:whitney-receiving:5.2` | `R.5.2` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-HIGHER-SLIDES-1` | III | `courseIII:higher-slides:1` | `T.1` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-HIGHER-SLIDES-2` | III | `courseIII:higher-slides:2` | `T.2` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-HIGHER-SLIDES-3` | III | `courseIII:higher-slides:3` | `T.3` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-HIGHER-SLIDES-4` | III | `courseIII:higher-slides:4` | `T.4` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-HIGHER-SLIDES-5` | III | `courseIII:higher-slides:5` | `T.5` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-HIGHER-SLIDES-6` | III | `courseIII:higher-slides:6` | `T.6` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-HIGHER-SLIDES-8.1` | III | `courseIII:higher-slides:8.1` | `T.7.1` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-HIGHER-SLIDES-8.2` | III | `courseIII:higher-slides:8.2` | `T.7.2` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-MIDDLE-CANCEL-1` | III | `courseIII:middle-cancel:1` | `U.1` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-MIDDLE-CANCEL-2` | III | `courseIII:middle-cancel:2` | `U.2` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-MIDDLE-CANCEL-3` | III | `courseIII:middle-cancel:3` | `U.3` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-MIDDLE-CANCEL-4` | III | `courseIII:middle-cancel:4` | `U.4` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-MIDDLE-CANCEL-5` | III | `courseIII:middle-cancel:5` | `U.5` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-MIDDLE-CANCEL-6` | III | `courseIII:middle-cancel:6` | `U.6` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-MIDDLE-CANCEL-7.1` | III | `courseIII:middle-cancel:7.1` | `U.7.1` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-MIDDLE-CANCEL-7.2` | III | `courseIII:middle-cancel:7.2` | `U.7.2` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-MORSE-CANCEL-1` | III | `courseIII:morse-cancel:1` | `J.1` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-MORSE-CANCEL-2.1` | III | `courseIII:morse-cancel:2.1` | `J.2` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-MORSE-CANCEL-6` | III | `courseIII:morse-cancel:6` | `J.6` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-MORSE-CANCEL-7.1` | III | `courseIII:morse-cancel:7.1` | `J.7.1` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-MORSE-CANCEL-7.2` | III | `courseIII:morse-cancel:7.2` | `J.7.2` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-SPIN6-1` | III | `courseIII:spin6:1` | `H.1` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-SPIN6-2` | III | `courseIII:spin6:2` | `H.2` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-SPIN6-3` | III | `courseIII:spin6:3` | `H.3` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-SPIN6-4` | III | `courseIII:spin6:4` | `H.4` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-SPIN6-5` | III | `courseIII:spin6:5` | `H.5` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-SPIN6-6` | III | `courseIII:spin6:6` | `H.6` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-SPIN6-7.1` | III | `courseIII:spin6:7.1` | `H.7.1` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-SPIN6-7.2` | III | `courseIII:spin6:7.2` | `H.7.2` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-INTEGRAL-STABLE-1` | III | `courseIII:integral-stable:1` | `AE.1` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-INTEGRAL-STABLE-2` | III | `courseIII:integral-stable:2` | `AE.2` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-INTEGRAL-STABLE-3` | III | `courseIII:integral-stable:3` | `AE.3` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-INTEGRAL-STABLE-4` | III | `courseIII:integral-stable:4` | `AE.4` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-INTEGRAL-STABLE-5` | III | `courseIII:integral-stable:5` | `AE.5` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-INTEGRAL-STABLE-6` | III | `courseIII:integral-stable:6` | `AE.6` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-INTEGRAL-STABLE-7` | III | `courseIII:integral-stable:7` | `AE.7` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-INTEGRAL-STABLE-8.1` | III | `courseIII:integral-stable:8.1` | `AE.8.1` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-INTEGRAL-STABLE-8.2` | III | `courseIII:integral-stable:8.2` | `AE.8.2` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-PONTRYAGIN-THOM-1` | III | `courseIII:pontryagin-thom:1` | `G.1` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-PONTRYAGIN-THOM-2` | III | `courseIII:pontryagin-thom:2` | `G.2` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-PONTRYAGIN-THOM-3` | III | `courseIII:pontryagin-thom:3` | `G.3` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-PONTRYAGIN-THOM-4` | III | `courseIII:pontryagin-thom:4` | `G.4` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-PONTRYAGIN-THOM-5` | III | `courseIII:pontryagin-thom:5` | `G.5` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-PONTRYAGIN-THOM-6` | III | `courseIII:pontryagin-thom:6` | `G.6` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-PONTRYAGIN-THOM-7` | III | `courseIII:pontryagin-thom:7` | `G.7` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-PONTRYAGIN-THOM-8` | III | `courseIII:pontryagin-thom:8` | `G.8` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-PONTRYAGIN-THOM-9.1` | III | `courseIII:pontryagin-thom:9.1` | `G.9.1` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-PONTRYAGIN-THOM-9.2` | III | `courseIII:pontryagin-thom:9.2` | `G.9.2` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-RELATIVE-MORSE-1` | III | `courseIII:relative-morse:1` | `I.1` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-RELATIVE-MORSE-2` | III | `courseIII:relative-morse:2` | `I.2` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-RELATIVE-MORSE-3` | III | `courseIII:relative-morse:3` | `I.3` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-RELATIVE-MORSE-4` | III | `courseIII:relative-morse:4` | `I.4` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-RELATIVE-MORSE-5.1` | III | `courseIII:relative-morse:5.1` | `I.5.1` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-RELATIVE-MORSE-5.2` | III | `courseIII:relative-morse:5.2` | `I.5.2` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-HANDLE-ARRANGEMENT-1` | III | `courseIII:handle-arrangement:1` | `M.1` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-HANDLE-ARRANGEMENT-2` | III | `courseIII:handle-arrangement:2` | `M.2` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-HANDLE-ARRANGEMENT-3` | III | `courseIII:handle-arrangement:3` | `M.3` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-HANDLE-ARRANGEMENT-4` | III | `courseIII:handle-arrangement:4` | `M.4` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-HANDLE-ARRANGEMENT-5.1` | III | `courseIII:handle-arrangement:5.1` | `M.5.1` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-HANDLE-ARRANGEMENT-5.2` | III | `courseIII:handle-arrangement:5.2` | `M.5.2` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-ZERO-TOP-1` | III | `courseIII:zero-top:1` | `N.1` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-ZERO-TOP-2` | III | `courseIII:zero-top:2` | `N.2` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-ZERO-TOP-3` | III | `courseIII:zero-top:3` | `N.3` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-ZERO-TOP-4` | III | `courseIII:zero-top:4` | `N.4` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-ZERO-TOP-5` | III | `courseIII:zero-top:5` | `N.5` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-ZERO-TOP-6.1` | III | `courseIII:zero-top:6.1` | `N.6.1` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-ZERO-TOP-6.2` | III | `courseIII:zero-top:6.2` | `N.6.2` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-TRAJECTORY-LOWERING-1` | III | `courseIII:trajectory-lowering:1` | `L.1` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-TRAJECTORY-LOWERING-2` | III | `courseIII:trajectory-lowering:2` | `L.2` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-TRAJECTORY-LOWERING-3` | III | `courseIII:trajectory-lowering:3` | `L.3` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-TRAJECTORY-LOWERING-4` | III | `courseIII:trajectory-lowering:4` | `L.4` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-TRAJECTORY-LOWERING-5` | III | `courseIII:trajectory-lowering:5` | `L.5` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-TRAJECTORY-LOWERING-6.1` | III | `courseIII:trajectory-lowering:6.1` | `L.6.1` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-TRAJECTORY-LOWERING-6.2` | III | `courseIII:trajectory-lowering:6.2` | `L.6.2` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-BELT-COMPLEMENT-1` | III | `courseIII:belt-complement:1` | `P.1` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-BELT-COMPLEMENT-2` | III | `courseIII:belt-complement:2` | `P.2` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-BELT-COMPLEMENT-3` | III | `courseIII:belt-complement:3` | `P.3` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-BELT-COMPLEMENT-4` | III | `courseIII:belt-complement:4` | `P.4` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-BELT-COMPLEMENT-5` | III | `courseIII:belt-complement:5` | `P.5` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-BELT-COMPLEMENT-6` | III | `courseIII:belt-complement:6` | `P.6` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-BELT-COMPLEMENT-7` | III | `courseIII:belt-complement:7` | `P.7` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-WHITNEY-SUPPORT-1` | III | `courseIII:whitney-support:1` | `Q.1` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-WHITNEY-SUPPORT-2` | III | `courseIII:whitney-support:2` | `Q.2` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-WHITNEY-SUPPORT-3` | III | `courseIII:whitney-support:3` | `Q.3` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-WHITNEY-SUPPORT-4` | III | `courseIII:whitney-support:4` | `Q.4` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-WHITNEY-SUPPORT-5` | III | `courseIII:whitney-support:5` | `Q.5` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-WHITNEY-SUPPORT-6` | III | `courseIII:whitney-support:6` | `Q.6` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-WHITNEY-SUPPORT-7.1` | III | `courseIII:whitney-support:7.1` | `Q.7.1` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-WHITNEY-SUPPORT-7.2` | III | `courseIII:whitney-support:7.2` | `Q.7.2` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-HANDLE-CHAINS-1` | III | `courseIII:handle-chains:1` | `O.1` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-HANDLE-CHAINS-2` | III | `courseIII:handle-chains:2` | `O.2` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-HANDLE-CHAINS-3` | III | `courseIII:handle-chains:3` | `O.3` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-HANDLE-CHAINS-4` | III | `courseIII:handle-chains:4` | `O.4` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-HANDLE-CHAINS-5` | III | `courseIII:handle-chains:5` | `O.5` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-HANDLE-CHAINS-6.1` | III | `courseIII:handle-chains:6.1` | `O.6.1` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-HANDLE-CHAINS-6.2` | III | `courseIII:handle-chains:6.2` | `O.6.2` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-HANDLE-CHAINS-8.1` | III | `courseIII:handle-chains:8.1` | `O.7.1` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-HANDLE-CHAINS-8.2` | III | `courseIII:handle-chains:8.2` | `O.7.2` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-PAIR-CREATION-1` | III | `courseIII:pair-creation:1` | `K.1` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-PAIR-CREATION-2` | III | `courseIII:pair-creation:2` | `K.2` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-PAIR-CREATION-3` | III | `courseIII:pair-creation:3` | `K.3` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-PAIR-CREATION-4` | III | `courseIII:pair-creation:4` | `K.4` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-PAIR-CREATION-5` | III | `courseIII:pair-creation:5` | `K.5` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-PAIR-CREATION-6` | III | `courseIII:pair-creation:6` | `K.6` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-PAIR-CREATION-7.1` | III | `courseIII:pair-creation:7.1` | `K.7.1` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-PAIR-CREATION-7.2` | III | `courseIII:pair-creation:7.2` | `K.7.2` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-LOW-INDEX-SLIDES-1` | III | `courseIII:low-index-slides:1` | `S.1` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-LOW-INDEX-SLIDES-2` | III | `courseIII:low-index-slides:2` | `S.2` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-LOW-INDEX-SLIDES-3` | III | `courseIII:low-index-slides:3` | `S.3` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-LOW-INDEX-SLIDES-4` | III | `courseIII:low-index-slides:4` | `S.4` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-LOW-INDEX-SLIDES-5` | III | `courseIII:low-index-slides:5` | `S.5` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-LOW-INDEX-SLIDES-6` | III | `courseIII:low-index-slides:6` | `S.6` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-LOW-INDEX-SLIDES-7` | III | `courseIII:low-index-slides:7` | `S.7` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-LOW-INDEX-SLIDES-8` | III | `courseIII:low-index-slides:8` | `S.8` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-LOW-INDEX-SLIDES-9.1` | III | `courseIII:low-index-slides:9.1` | `S.9.1` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-LOW-INDEX-SLIDES-9.2` | III | `courseIII:low-index-slides:9.2` | `S.9.2` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-ADAMS-ARITHMETIC-1` | III | `courseIII:adams-arithmetic:1` | `AD.1` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-ADAMS-ARITHMETIC-2` | III | `courseIII:adams-arithmetic:2` | `AD.2` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-ADAMS-ARITHMETIC-3` | III | `courseIII:adams-arithmetic:3` | `AD.3` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-ADAMS-ARITHMETIC-4` | III | `courseIII:adams-arithmetic:4` | `AD.4` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-ADAMS-ARITHMETIC-5` | III | `courseIII:adams-arithmetic:5` | `AD.5` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-ADAMS-ARITHMETIC-6` | III | `courseIII:adams-arithmetic:6` | `AD.6` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-ADAMS-ARITHMETIC-7` | III | `courseIII:adams-arithmetic:7` | `AD.7` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-ADAMS-ARITHMETIC-8` | III | `courseIII:adams-arithmetic:8` | `AD.8` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-ADAMS-ARITHMETIC-9` | III | `courseIII:adams-arithmetic:9` | `AD.9` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-ADAMS-TOWER-1` | III | `courseIII:adams-tower:1` | `AC.1` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-ADAMS-TOWER-2` | III | `courseIII:adams-tower:2` | `AC.2` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-ADAMS-TOWER-3` | III | `courseIII:adams-tower:3` | `AC.3` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-ADAMS-TOWER-4` | III | `courseIII:adams-tower:4` | `AC.4` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-ADAMS-TOWER-5` | III | `courseIII:adams-tower:5` | `AC.5` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-ADAMS-TOWER-6` | III | `courseIII:adams-tower:6` | `AC.6` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-ADAMS-TOWER-7.1` | III | `courseIII:adams-tower:7.1` | `AC.7.1` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-ADAMS-TOWER-7.2` | III | `courseIII:adams-tower:7.2` | `AC.7.2` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-ADAMS-TOWER-8` | III | `courseIII:adams-tower:8` | `AC.8` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-ADAMS-TOWER-9` | III | `courseIII:adams-tower:9` | `AC.9` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-ADAMS-TOWER-10` | III | `courseIII:adams-tower:10` | `AC.10` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-ADAMS-TOWER-11` | III | `courseIII:adams-tower:11` | `AC.11` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-FORMAL-CHAR2-1` | III | `courseIII:formal-char2:1` | `V.1` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-FORMAL-CHAR2-2` | III | `courseIII:formal-char2:2` | `V.2` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-FORMAL-CHAR2-3` | III | `courseIII:formal-char2:3` | `V.3` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-FORMAL-CHAR2-4` | III | `courseIII:formal-char2:4` | `V.4` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-FORMAL-CHAR2-4.1` | III | `courseIII:formal-char2:4.1` | `V.4.1` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-FORMAL-CHAR2-4.2` | III | `courseIII:formal-char2:4.2` | `V.4.2` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-PROJECTIVE-COOP-1` | III | `courseIII:projective-coop:1` | `W.1` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-PROJECTIVE-COOP-2` | III | `courseIII:projective-coop:2` | `W.2` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-PROJECTIVE-COOP-3` | III | `courseIII:projective-coop:3` | `W.3` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-PROJECTIVE-COOP-4` | III | `courseIII:projective-coop:4` | `W.4` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-PROJECTIVE-COOP-5` | III | `courseIII:projective-coop:5` | `W.5` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-PROJECTIVE-COOP-6.1` | III | `courseIII:projective-coop:6.1` | `W.6.1` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-PROJECTIVE-COOP-6.2` | III | `courseIII:projective-coop:6.2` | `W.6.2` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-ACTUAL-DEGREE8-1` | III | `courseIII:actual-degree8:1` | `X.1` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-ACTUAL-DEGREE8-2` | III | `courseIII:actual-degree8:2` | `X.2` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-ACTUAL-DEGREE8-3` | III | `courseIII:actual-degree8:3` | `X.3` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-ACTUAL-DEGREE8-4` | III | `courseIII:actual-degree8:4` | `X.4` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-ACTUAL-DEGREE8-5` | III | `courseIII:actual-degree8:5` | `X.5` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-ACTUAL-DEGREE8-6` | III | `courseIII:actual-degree8:6` | `X.6` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-ACTUAL-DEGREE8-7` | III | `courseIII:actual-degree8:7` | `X.7` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-ACTUAL-DEGREE8-8` | III | `courseIII:actual-degree8:8` | `X.8` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-ACTUAL-DEGREE8-9.1` | III | `courseIII:actual-degree8:9.1` | `X.9.1` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-ACTUAL-DEGREE8-9.2` | III | `courseIII:actual-degree8:9.2` | `X.9.2` |
| `WRITING_REPAIR` | `MAPS-AUDIT-CARRIER-EXTENSION` | III | `mapsIII:carrier-extension-lemma` | `9.42` |
| `WRITING_REPAIR` | `MAPS-AUDIT-CIRCLE-CARRIER-NULL` | III | `mapsIII:angle-forgotten-one-copy-null` | `9.43` |
| `WRITING_REPAIR` | `MAPS-AUDIT-PT-1` | III | `courseIII:pt-relative-embedding` | `G.1` |
| `WRITING_REPAIR` | `MAPS-AUDIT-PT-2` | III | `courseIII:pt-relative-normal-frame` | `G.2` |
| `WRITING_REPAIR` | `MAPS-AUDIT-PT-3` | III | `courseIII:pt-normal-inverse-comparison` | `G.3` |
| `WRITING_REPAIR` | `MAPS-AUDIT-PT-4` | III | `courseIII:pt-abstract-framed-comparison` | `G.4` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-ACTUAL-RESOLUTION-1` | III | `courseIII:actual-resolution:1` | `Y.1` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-ACTUAL-RESOLUTION-2` | III | `courseIII:actual-resolution:2` | `Y.2` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-ACTUAL-RESOLUTION-3` | III | `courseIII:actual-resolution:3` | `Y.3` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-ACTUAL-RESOLUTION-4` | III | `courseIII:actual-resolution:4` | `Y.4` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-ACTUAL-RESOLUTION-5` | III | `courseIII:actual-resolution:5` | `Y.5` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-ACTUAL-RESOLUTION-6` | III | `courseIII:actual-resolution:6` | `Y.6` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-ACTUAL-RESOLUTION-7` | III | `courseIII:actual-resolution:7` | `Y.7` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-ACTUAL-RESOLUTION-8.1` | III | `courseIII:actual-resolution:8.1` | `Y.8.1` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-ACTUAL-RESOLUTION-8.2` | III | `courseIII:actual-resolution:8.2` | `Y.8.2` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-MILNOR-COBAR-1.1` | III | `courseIII:milnor-cobar:1.1` | `Z.1` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-MILNOR-COBAR-6.1` | III | `courseIII:milnor-cobar:6.1` | `Z.6` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-MILNOR-COBAR-7.1` | III | `courseIII:milnor-cobar:7.1` | `Z.7.1` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-MILNOR-COBAR-7.2` | III | `courseIII:milnor-cobar:7.2` | `Z.7.2` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-ODD-COOP-1` | III | `courseIII:odd-coop:1` | `AB.1` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-ODD-COOP-2` | III | `courseIII:odd-coop:2` | `AB.2` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-ODD-COOP-3` | III | `courseIII:odd-coop:3` | `AB.3` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-ODD-COOP-4` | III | `courseIII:odd-coop:4` | `AB.4` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-ODD-COOP-5` | III | `courseIII:odd-coop:5` | `AB.5` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-ODD-COOP-6` | III | `courseIII:odd-coop:6` | `AB.6` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-ODD-COOP-7.1` | III | `courseIII:odd-coop:7.1` | `AB.7.1` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-ODD-COOP-7.2` | III | `courseIII:odd-coop:7.2` | `AB.7.2` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-COEFFICIENT-RINGS-1` | III | `courseIII:coefficient-rings:1` | `AA.1` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-COEFFICIENT-RINGS-2` | III | `courseIII:coefficient-rings:2` | `AA.2` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-COEFFICIENT-RINGS-3` | III | `courseIII:coefficient-rings:3` | `AA.3` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-COEFFICIENT-RINGS-4` | III | `courseIII:coefficient-rings:4` | `AA.4` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-COEFFICIENT-RINGS-5` | III | `courseIII:coefficient-rings:5` | `AA.5` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-COEFFICIENT-RINGS-6` | III | `courseIII:coefficient-rings:6` | `AA.6` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-COEFFICIENT-RINGS-7.1` | III | `courseIII:coefficient-rings:7.1` | `AA.7.1` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-COEFFICIENT-RINGS-7.2` | III | `courseIII:coefficient-rings:7.2` | `AA.7.2` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-DUALITY-2.1` | III | `courseIII:duality:2.1` | `F.1` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-DUALITY-2.2` | III | `courseIII:duality:2.2` | `F.2` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-DUALITY-2.3` | III | `courseIII:duality:2.3` | `F.3` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-DUALITY-3.1` | III | `courseIII:duality:3.1` | `F.4` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-DUALITY-3.2` | III | `courseIII:duality:3.2` | `F.5` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-DUALITY-3.3` | III | `courseIII:duality:3.3` | `F.6` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-DUALITY-4.1` | III | `courseIII:duality:4.1` | `F.7` |
| `WORKING_EDITION_COURSE_PROVIDER` | `CG-S6-DUALITY-4.2` | III | `courseIII:duality:4.2` | `F.8` |
| `WRITING_REPAIR` | `MODULAR_COLLISION_50_56` | III | `mapsD:repair:collision-realization` | `B.1` |
| `working_edition` | `sphere-metric-uniform-collapse` | III | `wb:sphere-metric-uniform-collapse` | `9.31` |
| `working_edition` | `sphere-metric-fixed-realization` | III | `wb:sphere-metric-fixed-realization` | `9.32` |
| `working_edition` | `sphere-metric-scaling-trichotomy` | III | `wb:sphere-metric-scaling-trichotomy` | `9.33` |
| `working_edition` | `sphere-metric-unit-volume` | III | `wb:sphere-metric-unit-volume` | `9.34` |
| `working_edition` | `sphere-metric-tangent-scope` | III | `wb:sphere-metric-tangent-scope` | `9.35` |
| `working_edition` | `h24:ret:chart-lemma` | III | `wb:h24:ret:chart-lemma` | `9.36` |
| `working_edition` | `h24:ret:orientation-lemma` | III | `wb:h24:ret:orientation-lemma` | `9.37` |
| `working_edition` | `h24:ret:framing-proposition` | III | `wb:h24:ret:framing-proposition` | `9.38` |
| `working_edition` | `h24:ret:q2-detected-quotient` | III | `wb:h24:ret:q2-detected-quotient` | `9.39` |
| `WRITING_REPAIR` | `carrier-real-periods` | III | `mapsIII:carrier-real-periods` | `9.4` |
| `WRITING_REPAIR` | `carrier-native-quotient` | III | `wb:cusp-spec-native-quotient` | `9.5` |

## Appendix B. Explicit statement and equation aliases

Each table identifies its source alias file. When an earlier FAMILY destination used the intermediate namespace, the recorded canonical destination is shown alongside it. Original alias files are unchanged.

### `work/invariants_arithmetic/statement_aliases.json`

| Source label or tag | Kind | Recorded destination | Current destination |
|---|---|---|---|
| `ari:C.8.5` | statement | `fam:st:C.2.3` | Paper I, `fam:src:C.2.3` (number `5.5`) |
| `inv:D1.3` | statement | `fam:st:A.5.2` | Paper I, `fam:src:A.5.2` (number `3.9`) |
| `inv:D2.1` | statement | `fam:st:A.5.2` | Paper I, `fam:src:A.5.2` (number `3.9`) |
| `inv:D3.1` | statement | `fam:st:A.5.2` | Paper I, `fam:src:A.5.2` (number `3.9`) |

### `work/invariants_arithmetic/working_statement_aliases.json`

| Source label or tag | Kind | Recorded destination | Current destination |
|---|---|---|---|
| `wb:prop:workbench-holomorphic-form-vanishing` | statement | `inv:A3.1` | Paper I, `inv:A3.1` (number `8.9`) |
| `wb:thm:parametric-hodge-diamond` | statement | `inv:A3.1` | Paper I, `inv:A3.1` (number `8.9`) |
| `wb:thm:frolicher-e2-candidate` | statement | `inv:C1.1` | Paper I, `inv:C1.1` (number `10.1`) |
| `wb:prop:period-derivative-determinant` | statement | `inv:A2.1` | Paper I, `inv:A2.1` (number `8.5`) |
| `wb:prop:log-relative-direct-images` | statement | `inv:A1.2` | Paper I, `inv:A1.2` (number `8.3`) |
| `wb:prop:log-ks-divisor` | statement | `inv:A2.1` | Paper I, `inv:A2.1` (number `8.5`) |
| `wb:prop:absolute-cotangent-direct-images` | statement | `inv:A1.3` | Paper I, `inv:A1.3` (number `8.4`) |
| `wb:thm:h12-scalar` | statement | `inv:A2.4` | Paper I, `inv:A2.4` (number `8.8`) |
| `wb:cor:exact-hodge-diamond` | statement | `inv:A3.1` | Paper I, `inv:A3.1` (number `8.9`) |
| `wb:thm:exact-bott-chern-aeppli` | statement | `inv:C2.1` | Paper I, `inv:C2.1` (number `10.3`) |
| `wb:lem:bcpr-degree-one-input` | statement | `inv:C3.2` | Paper I, `inv:C3.2` (number `10.6`) |
| `wb:lem:bcpr-eta-extension` | statement | `inv:A3.2` | Paper I, `inv:A3.2` (number `8.10`) |
| `wb:prop:bcpr-generators-are-bases` | statement | `inv:C3.3` | Paper I, `inv:C3.3` (number `10.7`) |
| `wb:thm:bcpr-square-zero-algebra` | statement | `inv:C3.3` | Paper I, `inv:C3.3` (number `10.7`) |
| `wb:lem:hodge-line-audit` | statement | `mapsI:hodge:line` | Paper I, `mapsI:hodge:line` (number `L.1`) |
| `wb:lem:finite-normal-order-audit` | statement | `wb:ffcert:thm:normal-trivialization` | Paper I, `wb:ffcert:thm:normal-trivialization` (number `C.15`) |
| `wb:lem:cusp-structure-sheaf-audit` | statement | `inv:A1.0` | Paper I, `inv:A1.0` (number `8.1`) |
| `wb:thm:structure-direct-images-audit` | statement | `inv:A1.0` | Paper I, `inv:A1.0` (number `8.1`) |
| `wb:cor:picard-line-audit` | statement | `inv:C3.1` | Paper I, `inv:C3.1` (number `10.5`) |

### `work/invariants_arithmetic/working_equation_tag_aliases.json`

| Source label or tag | Kind | Recorded destination | Current destination |
|---|---|---|---|
| `11.6` | statement | `inv:A2.1` | Paper I, `inv:A2.1` (number `8.5`) |
| `11.7` | statement | `inv:A2.1` | Paper I, `inv:A2.1` (number `8.5`) |
| `11.13` | equation | `inv:eq:A-absolute-table` | Paper I, `inv:eq:A-absolute-table` (number `16`) |
| `11.21` | equation | `inv:eq:C-BC-A` | Paper I, `inv:eq:C-BC-A` (number `22`) |
| `11.22` | equation | `inv:eq:C-BC-A` | Paper I, `inv:eq:C-BC-A` (number `22`) |
| `11.23` | statement | `inv:C2.1` | Paper I, `inv:C2.1` (number `10.3`) |
| `11.24` | equation | `inv:eq:C-delta` | Paper I, `inv:eq:C-delta` (number `28`) |
| `9.7` | statement | `inv:A1.0` | Paper I, `inv:A1.0` (number `8.1`) |
| `9.8` | statement | `inv:A1.0` | Paper I, `inv:A1.0` (number `8.1`) |
| `9.9` | statement | `inv:A1.0` | Paper I, `inv:A1.0` (number `8.1`) |
| `9.12` | statement | `inv:A1.0` | Paper I, `inv:A1.0` (number `8.1`) |
| `9.13` | statement | `inv:A1.0` | Paper I, `inv:A1.0` (number `8.1`) |
| `9.17` | statement | `inv:C3.1` | Paper I, `inv:C3.1` (number `10.5`) |
| `9.18` | statement | `inv:C3.1` | Paper I, `inv:C3.1` (number `10.5`) |
| `9.19` | equation | `inv:wb:eq:9.19` | Paper II, `inv:wb:eq:9.19` (number `{WBAPII.9.19}`) |
| `9.1` | equation_tag | `HL.9.1` | Paper I, equation tag `HL.9.1` |
| `9.2` | equation_tag | `HL.9.2` | Paper I, equation tag `HL.9.2` |
| `9.3` | equation_tag | `HL.9.3` | Paper I, equation tag `HL.9.3` |
| `9.4` | equation_tag | `HL.9.4` | Paper I, equation tag `HL.9.4` |
| `9.5` | equation_tag | `HL.9.5` | Paper I, equation tag `HL.9.5` |
| `9.5a` | equation_tag | `HL.9.5a` | Paper I, equation tag `HL.9.5a` |
| `9.5b` | equation_tag | `HL.9.5b` | Paper I, equation tag `HL.9.5b` |
| `9.5c` | equation_tag | `HL.9.5c` | Paper I, equation tag `HL.9.5c` |
| `9.5d` | equation_tag | `HL.9.5d` | Paper I, equation tag `HL.9.5d` |
| `9.5e` | equation_tag | `HL.9.5e` | Paper I, equation tag `HL.9.5e` |
| `9.5f` | equation_tag | `HL.9.5f` | Paper I, equation tag `HL.9.5f` |
| `9.5g` | equation_tag | `HL.9.5g` | Paper I, equation tag `HL.9.5g` |
| `9.6` | equation_tag | `HL.9.6` | Paper I, equation tag `HL.9.6` |
| `$11.17a_{\mathrm{fin}}$` | equation | `inv:wb:eq:11.17a-fin` | Paper I, `inv:wb:eq:11.17a-fin` (number `{WBH.$11.17a_{\mathrm  {fin}}$}`) |
| `11.17a$''$` | equation | `inv:wb:eq:11.17a-doubleprime` | Paper I, `inv:wb:eq:11.17a-doubleprime` (number `{WBH.11.17a$''$}`) |
| `11.17d$''$` | equation | `inv:wb:eq:11.17d-doubleprime` | Paper I, `inv:wb:eq:11.17d-doubleprime` (number `{WBH.11.17d$''$}`) |
| `11.17a$'$` | equation | `inv:wb:eq:11.17a-prime` | Paper I, `inv:wb:eq:11.17a-prime` (number `{WBH.11.17a$'$}`) |
| `11.17d$'$` | equation | `inv:wb:eq:11.17d-prime` | Paper I, `inv:wb:eq:11.17d-prime` (number `{WBH.11.17d$'$}`) |
| `11.10a` | equation | `inv:wb:eq:11.10a` | Paper I, `inv:wb:eq:11.10a` (number `{WBH.11.10a}`) |
| `11.10b` | equation | `inv:wb:eq:11.10b` | Paper I, `inv:wb:eq:11.10b` (number `{WBH.11.10b}`) |
| `11.11a` | equation | `inv:wb:eq:11.11a` | Paper I, `inv:wb:eq:11.11a` (number `{WBH.11.11a}`) |
| `11.16a` | equation | `inv:wb:eq:11.16a` | Paper I, `inv:wb:eq:11.16a` (number `{WBH.11.16a}`) |
| `11.16b` | equation | `inv:wb:eq:11.16b` | Paper I, `inv:wb:eq:11.16b` (number `{WBH.11.16b}`) |
| `11.16c` | equation | `inv:wb:eq:11.16c` | Paper I, `inv:wb:eq:11.16c` (number `{WBH.11.16c}`) |
| `11.17a` | equation | `inv:wb:eq:11.17a` | Paper I, `inv:wb:eq:11.17a` (number `{WBH.11.17a}`) |
| `11.17b` | equation | `inv:wb:eq:11.17b` | Paper I, `inv:wb:eq:11.17b` (number `{WBH.11.17b}`) |
| `11.17c` | equation | `inv:wb:eq:11.17c` | Paper I, `inv:wb:eq:11.17c` (number `{WBH.11.17c}`) |
| `11.17d` | equation | `inv:wb:eq:11.17d` | Paper I, `inv:wb:eq:11.17d` (number `{WBH.11.17d}`) |
| `11.17e` | equation | `inv:wb:eq:11.17e` | Paper I, `inv:wb:eq:11.17e` (number `{WBH.11.17e}`) |
| `11.17f` | equation | `inv:wb:eq:11.17f` | Paper I, `inv:wb:eq:11.17f` (number `{WBH.11.17f}`) |
| `11.18a` | equation | `inv:wb:eq:11.18a` | Paper I, `inv:wb:eq:11.18a` (number `{WBH.11.18a}`) |
| `11.18b` | equation | `inv:wb:eq:11.18b` | Paper I, `inv:wb:eq:11.18b` (number `{WBH.11.18b}`) |
| `11.19a` | equation | `inv:wb:eq:11.19a` | Paper I, `inv:wb:eq:11.19a` (number `{WBH.11.19a}`) |
| `11.19f` | equation | `inv:wb:eq:11.19f` | Paper I, `inv:wb:eq:11.19f` (number `{WBH.11.19f}`) |
| `11.20a` | equation | `inv:wb:eq:11.20a` | Paper I, `inv:wb:eq:11.20a` (number `{WBH.11.20a}`) |
| `11.10` | equation | `inv:wb:eq:11.10` | Paper I, `inv:wb:eq:11.10` (number `{WBH.11.10}`) |
| `11.11` | equation | `inv:wb:eq:11.11` | Paper I, `inv:wb:eq:11.11` (number `{WBH.11.11}`) |
| `11.12` | equation | `inv:wb:eq:11.12` | Paper I, `inv:wb:eq:11.12` (number `{WBH.11.12}`) |
| `11.14` | equation | `inv:wb:eq:11.14` | Paper I, `inv:wb:eq:11.14` (number `{WBH.11.14}`) |
| `11.15` | equation | `inv:wb:eq:11.15` | Paper I, `inv:wb:eq:11.15` (number `{WBH.11.15}`) |
| `11.16` | equation | `inv:wb:eq:11.16` | Paper I, `inv:wb:eq:11.16` (number `{WBH.11.16}`) |
| `11.17` | equation | `inv:wb:eq:11.17` | Paper I, `inv:wb:eq:11.17` (number `{WBH.11.17}`) |
| `11.18` | equation | `inv:wb:eq:11.18` | Paper I, `inv:wb:eq:11.18` (number `{WBH.11.18}`) |
| `11.19` | equation | `inv:wb:eq:11.19` | Paper I, `inv:wb:eq:11.19` (number `{WBH.11.19}`) |
| `11.20` | equation | `inv:wb:eq:11.20` | Paper I, `inv:wb:eq:11.20` (number `{WBH.11.20}`) |
| `11.25` | equation | `inv:wb:eq:11.25` | Paper I, `inv:wb:eq:11.25` (number `{WBH.11.25}`) |
| `11.3a` | equation | `inv:wb:eq:11.3a` | Paper I, `inv:wb:eq:11.3a` (number `{WBH.11.3a}`) |
| `11.1` | equation | `inv:wb:eq:11.1` | Paper I, `inv:wb:eq:11.1` (number `{WBH.11.1}`) |
| `11.2` | equation | `inv:wb:eq:11.2` | Paper I, `inv:wb:eq:11.2` (number `{WBH.11.2}`) |
| `11.3` | equation | `inv:wb:eq:11.3` | Paper I, `inv:wb:eq:11.3` (number `{WBH.11.3}`) |
| `11.4` | equation | `inv:wb:eq:11.4` | Paper I, `inv:wb:eq:11.4` (number `{WBH.11.4}`) |
| `11.5` | equation | `inv:wb:eq:11.5` | Paper I, `inv:wb:eq:11.5` (number `{WBH.11.5}`) |
| `11.8` | equation | `inv:wb:eq:11.8` | Paper I, `inv:wb:eq:11.8` (number `{WBH.11.8}`) |
| `11.9` | equation | `inv:wb:eq:11.9` | Paper I, `inv:wb:eq:11.9` (number `{WBH.11.9}`) |
| `9.10` | equation | `inv:wb:eq:9.10` | Paper I, `inv:wb:eq:9.10` (number `{WBA.9.10}`) |
| `9.11` | equation | `inv:wb:eq:9.11` | Paper I, `inv:wb:eq:9.11` (number `{WBA.9.11}`) |
| `9.14` | equation | `inv:wb:eq:9.14` | Paper I, `inv:wb:eq:9.14` (number `{WBA.9.14}`) |
| `9.15` | equation | `inv:wb:eq:9.15` | Paper I, `inv:wb:eq:9.15` (number `{WBA.9.15}`) |
| `9.16` | equation | `inv:wb:eq:9.16` | Paper I, `inv:wb:eq:9.16` (number `{WBA.9.16}`) |
| `9.20` | equation | `inv:wb:eq:9.20` | Paper II, `inv:wb:eq:9.20` (number `{WBAPII.9.20}`) |
| `9.21` | equation | `inv:wb:eq:9.21` | Paper II, `inv:wb:eq:9.21` (number `{WBAPII.9.21}`) |
| `9.22` | equation | `inv:wb:eq:9.22` | Paper II, `inv:wb:eq:9.22` (number `{WBAPII.9.22}`) |
| `9.23` | equation | `inv:wb:eq:9.23` | Paper II, `inv:wb:eq:9.23` (number `{WBAPII.9.23}`) |
| `9.24` | equation | `inv:wb:eq:9.24` | Paper II, `inv:wb:eq:9.24` (number `{WBAPII.9.24}`) |
| `9.25` | equation | `inv:wb:eq:9.25` | Paper II, `inv:wb:eq:9.25` (number `{WBAPII.9.25}`) |

### `work/maps_audit/paperI_topology_aliases.json`

| Source label or tag | Kind | Recorded destination | Current destination |
|---|---|---|---|
| `wb:sec:integral-leray` | statement | `mapsI:top:sec:integral-leray` | Paper I, `mapsI:top:sec:integral-leray` (number `D`) |
| `wb:thm:p0-integral-specialization` | statement | `mapsI:top:thm:p0-integral-specialization` | Paper I, `mapsI:top:thm:p0-integral-specialization` (number `D.1`) |
| `wb:prop:leray-e2` | statement | `mapsI:top:prop:leray-e2` | Paper I, `mapsI:top:prop:leray-e2` (number `D.2`) |
| `wb:lem:first-transgression` | statement | `mapsI:top:lem:first-transgression` | Paper I, `mapsI:top:lem:first-transgression` (number `D.3`) |
| `wb:lem:higher-transgressions` | statement | `mapsI:top:lem:higher-transgressions` | Paper I, `mapsI:top:lem:higher-transgressions` (number `D.4`) |
| `wb:thm:h2-vanishing` | statement | `mapsI:top:thm:h2-vanishing` | Paper I, `mapsI:top:thm:h2-vanishing` (number `D.5`) |
| `wb:prop:geometric-pi1` | statement | `mapsI:top:prop:geometric-pi1` | Paper I, `mapsI:top:prop:geometric-pi1` (number `D.6`) |
| `wb:cor:candidate-sphere` | statement | `mapsI:top:cor:candidate-sphere` | Paper I, `mapsI:top:cor:candidate-sphere` (number `D.7`) |
| `wb:prop:topological-spine` | statement | `mapsI:top:prop:topological-spine` | Paper I, `mapsI:top:prop:topological-spine` (number `E.1`) |
| `wb:lem:collapse-straightening` | statement | `mapsI:top:lem:collapse-straightening` | Paper I, `mapsI:top:lem:collapse-straightening` (number `E.2`) |
| `wb:lem:positive-collapse` | statement | `mapsI:top:lem:positive-collapse` | Paper I, `mapsI:top:lem:positive-collapse` (number `E.3`) |
| `wb:lem:phase-spread-collapse` | statement | `mapsI:top:lem:phase-spread-collapse` | Paper I, `mapsI:top:lem:phase-spread-collapse` (number `E.4`) |
| `wb:prop:verified-cellular-collapse` | statement | `mapsI:top:prop:verified-cellular-collapse` | Paper I, `mapsI:top:prop:verified-cellular-collapse` (number `E.5`) |
| `wb:prop:verified-collapse-homology` | statement | `mapsI:top:prop:verified-collapse-homology` | Paper I, `mapsI:top:prop:verified-collapse-homology` (number `E.6`) |
| `wb:thm:collapse-equals-specialization` | statement | `mapsI:top:thm:collapse-equals-specialization` | Paper I, `mapsI:top:thm:collapse-equals-specialization` (number `E.7`) |
| `wb:record:vankampen` | statement | `mapsI:top:record:vankampen` | Paper I, `mapsI:top:record:vankampen` (number `E.9`) |
| `wb:prop:actual-finite-band-maps` | statement | `mapsI:top:prop:actual-finite-band-maps` | Paper I, `mapsI:top:prop:actual-finite-band-maps` (number `E.10`) |
| `wb:finite-degree-three` | statement | `mapsI:top:finite-degree-three` | Paper I, `mapsI:top:finite-degree-three` (number `E.11`) |
| `wb:prop:cusp-mv-blocks` | statement | `mapsI:top:prop:cusp-mv-blocks` | Paper I, `mapsI:top:prop:cusp-mv-blocks` (number `E.12`) |
| `wb:thm:mv-leray-comparison` | statement | `mapsI:top:thm:mv-leray-comparison` | Paper I, `mapsI:top:thm:mv-leray-comparison` (number `E.14`) |
| `wb:lem:cohomological-closure` | statement | `mapsI:top:lem:cohomological-closure` | Paper I, `mapsI:top:lem:cohomological-closure` (number `E.16`) |
| `wb:thm:sphere-recognition` | statement | `mapsI:top:thm:sphere-recognition` | Paper I, `mapsI:top:thm:sphere-recognition` (number `E.17`) |
| `wb:cor:abstract-s6` | statement | `mapsI:top:cor:abstract-s6` | Paper I, `mapsI:top:cor:abstract-s6` (number `E.18`) |
| `wb:cor:candidate-mv-sphere` | statement | `mapsI:top:cor:candidate-mv-sphere` | Paper I, `mapsI:top:cor:candidate-mv-sphere` (number `E.19`) |

### `work/maps_audit/course_geometric_PaperI_aliases.json`

| Source label or tag | Kind | Recorded destination | Current destination |
|---|---|---|---|
| `CG-S6-CHAIN-LEMMA-1.1` | statement | `mapsI:chain:lemma:1.1` | Paper I, `mapsI:chain:lemma:1.1` (number `F.1`) |
| `CG-S6-CHAIN-LEMMA-2.1` | statement | `mapsI:chain:lemma:2.1` | Paper I, `mapsI:chain:lemma:2.1` (number `F.2`) |
| `CG-S6-CHAIN-COROLLARY-2.2` | statement | `mapsI:chain:corollary:2.2` | Paper I, `mapsI:chain:corollary:2.2` (number `F.3`) |
| `CG-S6-CHAIN-LEMMA-4.1` | statement | `mapsI:chain:lemma:4.1` | Paper I, `mapsI:chain:lemma:4.1` (number `F.4`) |
| `CG-S6-CW-THEOREM-4.1` | statement | `mapsI:cw:hurewicz-theorem-result` | Paper I, `mapsI:cw:hurewicz-theorem-result` (number `G.1`) |
| `CG-S6-PF-THEOREM-5.1` | statement | `mapsI:pf:theorem:5.1` | Paper I, `mapsI:pf:theorem:5.1` (number `H.1`) |

### `work/cdp_audit/paperII_statement_aliases.json`

| Source label or tag | Kind | Recorded destination | Current destination |
|---|---|---|---|
| `prop:missing-cotangent-filtration` | statement | `cdp:st:A.1.1` | Paper II, `cdp:st:A.1.1` (number `5.1`) |
| `wb:prop:missing-cotangent-filtration` | statement | `cdp:st:A.1.1` | Paper II, `cdp:st:A.1.1` (number `5.1`) |
| `wbII:prop:missing-cotangent-filtration` | statement | `cdp:st:A.1.1` | Paper II, `cdp:st:A.1.1` (number `5.1`) |
| `prop:missing-global-section-criterion` | statement | `cdp:st:A.1.1` | Paper II, `cdp:st:A.1.1` (number `5.1`) |
| `wb:prop:missing-global-section-criterion` | statement | `cdp:st:A.1.1` | Paper II, `cdp:st:A.1.1` (number `5.1`) |
| `wbII:prop:missing-global-section-criterion` | statement | `cdp:st:A.1.1` | Paper II, `cdp:st:A.1.1` (number `5.1`) |
| `lem:conormal-injective` | statement | `cdp:st:A.1.1` | Paper II, `cdp:st:A.1.1` (number `5.1`) |
| `wb:lem:conormal-injective` | statement | `cdp:st:A.1.1` | Paper II, `cdp:st:A.1.1` (number `5.1`) |
| `wbII:lem:conormal-injective` | statement | `cdp:st:A.1.1` | Paper II, `cdp:st:A.1.1` (number `5.1`) |
| `lem:conductor-square` | statement | `cdp:st:A.2.2` | Paper II, `cdp:st:A.2.2` (number `5.3`) |
| `wb:lem:conductor-square` | statement | `cdp:st:A.2.2` | Paper II, `cdp:st:A.2.2` (number `5.3`) |
| `wbII:lem:conductor-square` | statement | `cdp:st:A.2.2` | Paper II, `cdp:st:A.2.2` (number `5.3`) |
| `prop:conductor` | statement | `wbII:prop:conductor` | Paper II, `wbII:prop:conductor` (number `B.2`) |
| `wb:prop:conductor` | statement | `wbII:prop:conductor` | Paper II, `wbII:prop:conductor` (number `B.2`) |
| `wbII:prop:conductor` | statement | `wbII:prop:conductor` | Paper II, `wbII:prop:conductor` (number `B.2`) |
| `prop:nodal-counterexample` | statement | `cdp:st:B1` | Paper II, `cdp:st:B1` (number `5.8`) |
| `wb:prop:nodal-counterexample` | statement | `cdp:st:B1` | Paper II, `cdp:st:B1` (number `5.8`) |
| `wbII:prop:nodal-counterexample` | statement | `cdp:st:B1` | Paper II, `cdp:st:B1` (number `5.8`) |
| `thm:cartier-duality` | statement | `wbII:thm:cartier-duality` | Paper II, `wbII:thm:cartier-duality` (number `B.7`) |
| `wb:thm:cartier-duality` | statement | `wbII:thm:cartier-duality` | Paper II, `wbII:thm:cartier-duality` (number `B.7`) |
| `wbII:thm:cartier-duality` | statement | `wbII:thm:cartier-duality` | Paper II, `wbII:thm:cartier-duality` (number `B.7`) |
| `prop:cartier-duality-absolute` | statement | `wbII:prop:cartier-duality-absolute` | Paper II, `wbII:prop:cartier-duality-absolute` (number `B.8`) |
| `wb:prop:cartier-duality-absolute` | statement | `wbII:prop:cartier-duality-absolute` | Paper II, `wbII:prop:cartier-duality-absolute` (number `B.8`) |
| `wbII:prop:cartier-duality-absolute` | statement | `wbII:prop:cartier-duality-absolute` | Paper II, `wbII:prop:cartier-duality-absolute` (number `B.8`) |
| `lem:curve-flatness` | statement | `wbII:lem:curve-flatness` | Paper II, `wbII:lem:curve-flatness` (number `B.9`) |
| `wb:lem:curve-flatness` | statement | `wbII:lem:curve-flatness` | Paper II, `wbII:lem:curve-flatness` (number `B.9`) |
| `wbII:lem:curve-flatness` | statement | `wbII:lem:curve-flatness` | Paper II, `wbII:lem:curve-flatness` (number `B.9`) |
| `prop:analytic-base-change` | statement | `wbII:prop:analytic-base-change` | Paper II, `wbII:prop:analytic-base-change` (number `B.10`) |
| `wb:prop:analytic-base-change` | statement | `wbII:prop:analytic-base-change` | Paper II, `wbII:prop:analytic-base-change` (number `B.10`) |
| `wbII:prop:analytic-base-change` | statement | `wbII:prop:analytic-base-change` | Paper II, `wbII:prop:analytic-base-change` (number `B.10`) |
| `cor:surface-top-base-change` | statement | `wbII:cor:surface-top-base-change` | Paper II, `wbII:cor:surface-top-base-change` (number `B.11`) |
| `wb:cor:surface-top-base-change` | statement | `wbII:cor:surface-top-base-change` | Paper II, `wbII:cor:surface-top-base-change` (number `B.11`) |
| `wbII:cor:surface-top-base-change` | statement | `wbII:cor:surface-top-base-change` | Paper II, `wbII:cor:surface-top-base-change` (number `B.11`) |
| `prop:pic0-pullback` | statement | `wbII:prop:pic0-pullback` | Paper II, `wbII:prop:pic0-pullback` (number `B.12`) |
| `wb:prop:pic0-pullback` | statement | `wbII:prop:pic0-pullback` | Paper II, `wbII:prop:pic0-pullback` (number `B.12`) |
| `wbII:prop:pic0-pullback` | statement | `wbII:prop:pic0-pullback` | Paper II, `wbII:prop:pic0-pullback` (number `B.12`) |
| `prop:all-pic-restriction` | statement | `wbII:prop:all-pic-restriction` | Paper II, `wbII:prop:all-pic-restriction` (number `B.13`) |
| `wb:prop:all-pic-restriction` | statement | `wbII:prop:all-pic-restriction` | Paper II, `wbII:prop:all-pic-restriction` (number `B.13`) |
| `wbII:prop:all-pic-restriction` | statement | `wbII:prop:all-pic-restriction` | Paper II, `wbII:prop:all-pic-restriction` (number `B.13`) |
| `prop:leray-edge-restriction` | statement | `wbII:prop:leray-edge-restriction` | Paper II, `wbII:prop:leray-edge-restriction` (number `B.14`) |
| `wb:prop:leray-edge-restriction` | statement | `wbII:prop:leray-edge-restriction` | Paper II, `wbII:prop:leray-edge-restriction` (number `B.14`) |
| `wbII:prop:leray-edge-restriction` | statement | `wbII:prop:leray-edge-restriction` | Paper II, `wbII:prop:leray-edge-restriction` (number `B.14`) |
| `lem:picard-crossed-defect` | statement | `wbII:lem:picard-crossed-defect` | Paper II, `wbII:lem:picard-crossed-defect` (number `B.15`) |
| `wb:lem:picard-crossed-defect` | statement | `wbII:lem:picard-crossed-defect` | Paper II, `wbII:lem:picard-crossed-defect` (number `B.15`) |
| `wbII:lem:picard-crossed-defect` | statement | `wbII:lem:picard-crossed-defect` | Paper II, `wbII:lem:picard-crossed-defect` (number `B.15`) |
| `lem:picard-finite-norm` | statement | `wbII:lem:picard-finite-norm` | Paper II, `wbII:lem:picard-finite-norm` (number `B.16`) |
| `wb:lem:picard-finite-norm` | statement | `wbII:lem:picard-finite-norm` | Paper II, `wbII:lem:picard-finite-norm` (number `B.16`) |
| `wbII:lem:picard-finite-norm` | statement | `wbII:lem:picard-finite-norm` | Paper II, `wbII:lem:picard-finite-norm` (number `B.16`) |
| `lem:picard-cusp-defect` | statement | `wbII:lem:picard-cusp-defect` | Paper II, `wbII:lem:picard-cusp-defect` (number `B.17`) |
| `wb:lem:picard-cusp-defect` | statement | `wbII:lem:picard-cusp-defect` | Paper II, `wbII:lem:picard-cusp-defect` (number `B.17`) |
| `wbII:lem:picard-cusp-defect` | statement | `wbII:lem:picard-cusp-defect` | Paper II, `wbII:lem:picard-cusp-defect` (number `B.17`) |
| `prop:direct-boundary-picard` | statement | `wbII:prop:direct-boundary-picard` | Paper II, `wbII:prop:direct-boundary-picard` (number `B.18`) |
| `wb:prop:direct-boundary-picard` | statement | `wbII:prop:direct-boundary-picard` | Paper II, `wbII:prop:direct-boundary-picard` (number `B.18`) |
| `wbII:prop:direct-boundary-picard` | statement | `wbII:prop:direct-boundary-picard` | Paper II, `wbII:prop:direct-boundary-picard` (number `B.18`) |
| `cor:candidate-pic0-route` | statement | `wbII:cor:candidate-pic0-route` | Paper II, `wbII:cor:candidate-pic0-route` (number `B.24`) |
| `wb:cor:candidate-pic0-route` | statement | `wbII:cor:candidate-pic0-route` | Paper II, `wbII:cor:candidate-pic0-route` (number `B.24`) |
| `wbII:cor:candidate-pic0-route` | statement | `wbII:cor:candidate-pic0-route` | Paper II, `wbII:cor:candidate-pic0-route` (number `B.24`) |
| `thm:candidate-conductor` | statement | `wbII:thm:candidate-conductor` | Paper II, `wbII:thm:candidate-conductor` (number `B.26`) |
| `wb:thm:candidate-conductor` | statement | `wbII:thm:candidate-conductor` | Paper II, `wbII:thm:candidate-conductor` (number `B.26`) |
| `wbII:thm:candidate-conductor` | statement | `wbII:thm:candidate-conductor` | Paper II, `wbII:thm:candidate-conductor` (number `B.26`) |
| `cor:candidate-conductor-actual` | statement | `wbII:cor:candidate-conductor-actual` | Paper II, `wbII:cor:candidate-conductor-actual` (number `B.27`) |
| `wb:cor:candidate-conductor-actual` | statement | `wbII:cor:candidate-conductor-actual` | Paper II, `wbII:cor:candidate-conductor-actual` (number `B.27`) |
| `wbII:cor:candidate-conductor-actual` | statement | `wbII:cor:candidate-conductor-actual` | Paper II, `wbII:cor:candidate-conductor-actual` (number `B.27`) |
| `lem:cdp-generic-endpoints` | statement | `wbII:lem:cdp-generic-endpoints` | Paper II, `wbII:lem:cdp-generic-endpoints` (number `B.29`) |
| `wb:lem:cdp-generic-endpoints` | statement | `wbII:lem:cdp-generic-endpoints` | Paper II, `wbII:lem:cdp-generic-endpoints` (number `B.29`) |
| `wbII:lem:cdp-generic-endpoints` | statement | `wbII:lem:cdp-generic-endpoints` | Paper II, `wbII:lem:cdp-generic-endpoints` (number `B.29`) |
| `thm:corrected-cdp-global` | statement | `wbII:thm:corrected-cdp-global` | Paper II, `wbII:thm:corrected-cdp-global` (number `B.30`) |
| `wb:thm:corrected-cdp-global` | statement | `wbII:thm:corrected-cdp-global` | Paper II, `wbII:thm:corrected-cdp-global` (number `B.30`) |
| `wbII:thm:corrected-cdp-global` | statement | `wbII:thm:corrected-cdp-global` | Paper II, `wbII:thm:corrected-cdp-global` (number `B.30`) |
| `cor:corrected-cdp-relative` | statement | `wbII:cor:corrected-cdp-relative` | Paper II, `wbII:cor:corrected-cdp-relative` (number `B.31`) |
| `wb:cor:corrected-cdp-relative` | statement | `wbII:cor:corrected-cdp-relative` | Paper II, `wbII:cor:corrected-cdp-relative` (number `B.31`) |
| `wbII:cor:corrected-cdp-relative` | statement | `wbII:cor:corrected-cdp-relative` | Paper II, `wbII:cor:corrected-cdp-relative` (number `B.31`) |
| `thm:corrected-cdp-fibrewise` | statement | `wbII:thm:corrected-cdp-fibrewise` | Paper II, `wbII:thm:corrected-cdp-fibrewise` (number `B.32`) |
| `wb:thm:corrected-cdp-fibrewise` | statement | `wbII:thm:corrected-cdp-fibrewise` | Paper II, `wbII:thm:corrected-cdp-fibrewise` (number `B.32`) |
| `wbII:thm:corrected-cdp-fibrewise` | statement | `wbII:thm:corrected-cdp-fibrewise` | Paper II, `wbII:thm:corrected-cdp-fibrewise` (number `B.32`) |
| `test:cdp-comparison` | statement | `wbII:test:cdp-comparison` | Paper II, `wbII:test:cdp-comparison` (number `B.34`) |
| `wb:test:cdp-comparison` | statement | `wbII:test:cdp-comparison` | Paper II, `wbII:test:cdp-comparison` (number `B.34`) |
| `wbII:test:cdp-comparison` | statement | `wbII:test:cdp-comparison` | Paper II, `wbII:test:cdp-comparison` (number `B.34`) |
| `lem:torsion-identification` | statement | `wbII:lem:torsion-identification` | Paper II, `wbII:lem:torsion-identification` (number `B.1`) |
| `wb:lem:torsion-identification` | statement | `wbII:lem:torsion-identification` | Paper II, `wbII:lem:torsion-identification` (number `B.1`) |
| `wbII:lem:torsion-identification` | statement | `wbII:lem:torsion-identification` | Paper II, `wbII:lem:torsion-identification` (number `B.1`) |
| `lem:conormal` | statement | `cdp:st:A.1.1` | Paper II, `cdp:st:A.1.1` (number `5.1`) |
| `wb:lem:conormal` | statement | `cdp:st:A.1.1` | Paper II, `cdp:st:A.1.1` (number `5.1`) |
| `wbII:lem:conormal` | statement | `cdp:st:A.1.1` | Paper II, `cdp:st:A.1.1` (number `5.1`) |
| `prop:filtration` | statement | `cdp:st:A.1.1` | Paper II, `cdp:st:A.1.1` (number `5.1`) |
| `wb:prop:filtration` | statement | `cdp:st:A.1.1` | Paper II, `cdp:st:A.1.1` (number `5.1`) |
| `wbII:prop:filtration` | statement | `cdp:st:A.1.1` | Paper II, `cdp:st:A.1.1` (number `5.1`) |
| `prop:criterion` | statement | `cdp:st:A.1.1` | Paper II, `cdp:st:A.1.1` (number `5.1`) |
| `wb:prop:criterion` | statement | `cdp:st:A.1.1` | Paper II, `cdp:st:A.1.1` (number `5.1`) |
| `wbII:prop:criterion` | statement | `cdp:st:A.1.1` | Paper II, `cdp:st:A.1.1` (number `5.1`) |
| `lem:conductor` | statement | `cdp:st:A.2.2` | Paper II, `cdp:st:A.2.2` (number `5.3`) |
| `wb:lem:conductor` | statement | `cdp:st:A.2.2` | Paper II, `cdp:st:A.2.2` (number `5.3`) |
| `wbII:lem:conductor` | statement | `cdp:st:A.2.2` | Paper II, `cdp:st:A.2.2` (number `5.3`) |
| `prop:conductor-differential` | statement | `wbII:prop:conductor` | Paper II, `wbII:prop:conductor` (number `B.2`) |
| `wb:prop:conductor-differential` | statement | `wbII:prop:conductor` | Paper II, `wbII:prop:conductor` (number `B.2`) |
| `wbII:prop:conductor-differential` | statement | `wbII:prop:conductor` | Paper II, `wbII:prop:conductor` (number `B.2`) |
| `cor:normal-crossing-kernel` | statement | `wbII:cor:normal-crossing-kernel` | Paper II, `wbII:cor:normal-crossing-kernel` (number `B.3`) |
| `wb:cor:normal-crossing-kernel` | statement | `wbII:cor:normal-crossing-kernel` | Paper II, `wbII:cor:normal-crossing-kernel` (number `B.3`) |
| `wbII:cor:normal-crossing-kernel` | statement | `wbII:cor:normal-crossing-kernel` | Paper II, `wbII:cor:normal-crossing-kernel` (number `B.3`) |
| `prop:family-geometry` | statement | `cdp:st:B1` | Paper II, `cdp:st:B1` (number `5.8`) |
| `wb:prop:family-geometry` | statement | `cdp:st:B1` | Paper II, `cdp:st:B1` (number `5.8`) |
| `wbII:prop:family-geometry` | statement | `cdp:st:B1` | Paper II, `cdp:st:B1` (number `5.8`) |
| `lem:gluing-bundle` | statement | `wbII:lem:gluing-bundle` | Paper II, `wbII:lem:gluing-bundle` (number `B.4`) |
| `wb:lem:gluing-bundle` | statement | `wbII:lem:gluing-bundle` | Paper II, `wbII:lem:gluing-bundle` (number `B.4`) |
| `wbII:lem:gluing-bundle` | statement | `wbII:lem:gluing-bundle` | Paper II, `wbII:lem:gluing-bundle` (number `B.4`) |
| `lem:extending-gluing` | statement | `wbII:lem:extending-gluing` | Paper II, `wbII:lem:extending-gluing` (number `B.5`) |
| `wb:lem:extending-gluing` | statement | `wbII:lem:extending-gluing` | Paper II, `wbII:lem:extending-gluing` (number `B.5`) |
| `wbII:lem:extending-gluing` | statement | `wbII:lem:extending-gluing` | Paper II, `wbII:lem:extending-gluing` (number `B.5`) |
| `thm:nodal-test` | statement | `cdp:st:B1` | Paper II, `cdp:st:B1` (number `5.8`) |
| `wb:thm:nodal-test` | statement | `cdp:st:B1` | Paper II, `cdp:st:B1` (number `5.8`) |
| `wbII:thm:nodal-test` | statement | `cdp:st:B1` | Paper II, `cdp:st:B1` (number `5.8`) |
| `lem:generic-endpoints` | statement | `wbII:lem:generic-endpoints` | Paper II, `wbII:lem:generic-endpoints` (number `B.28`) |
| `wb:lem:generic-endpoints` | statement | `wbII:lem:generic-endpoints` | Paper II, `wbII:lem:generic-endpoints` (number `B.28`) |
| `wbII:lem:generic-endpoints` | statement | `wbII:lem:generic-endpoints` | Paper II, `wbII:lem:generic-endpoints` (number `B.28`) |
| `thm:corrected-global` | statement | `wbII:thm:corrected-cdp-global` | Paper II, `wbII:thm:corrected-cdp-global` (number `B.30`) |
| `wb:thm:corrected-global` | statement | `wbII:thm:corrected-cdp-global` | Paper II, `wbII:thm:corrected-cdp-global` (number `B.30`) |
| `wbII:thm:corrected-global` | statement | `wbII:thm:corrected-cdp-global` | Paper II, `wbII:thm:corrected-cdp-global` (number `B.30`) |
| `cor:relative` | statement | `wbII:cor:corrected-cdp-relative` | Paper II, `wbII:cor:corrected-cdp-relative` (number `B.31`) |
| `wb:cor:relative` | statement | `wbII:cor:corrected-cdp-relative` | Paper II, `wbII:cor:corrected-cdp-relative` (number `B.31`) |
| `wbII:cor:relative` | statement | `wbII:cor:corrected-cdp-relative` | Paper II, `wbII:cor:corrected-cdp-relative` (number `B.31`) |
| `prop:relative-local` | statement | `wbII:prop:relative-local` | Paper II, `wbII:prop:relative-local` (number `B.35`) |
| `wb:prop:relative-local` | statement | `wbII:prop:relative-local` | Paper II, `wbII:prop:relative-local` (number `B.35`) |
| `wbII:prop:relative-local` | statement | `wbII:prop:relative-local` | Paper II, `wbII:prop:relative-local` (number `B.35`) |
| `prop:local-cusp-picard-obstruction` | statement | `wbII:prop:local-cusp-picard-obstruction` | Paper II, `wbII:prop:local-cusp-picard-obstruction` (number `B.19`) |
| `wb:prop:local-cusp-picard-obstruction` | statement | `wbII:prop:local-cusp-picard-obstruction` | Paper II, `wbII:prop:local-cusp-picard-obstruction` (number `B.19`) |
| `wbII:prop:local-cusp-picard-obstruction` | statement | `wbII:prop:local-cusp-picard-obstruction` | Paper II, `wbII:prop:local-cusp-picard-obstruction` (number `B.19`) |
| `prop:analytic-ah-boundary` | statement | `wbII:prop:analytic-ah-boundary` | Paper II, `wbII:prop:analytic-ah-boundary` (number `B.21`) |
| `wb:prop:analytic-ah-boundary` | statement | `wbII:prop:analytic-ah-boundary` | Paper II, `wbII:prop:analytic-ah-boundary` (number `B.21`) |
| `wbII:prop:analytic-ah-boundary` | statement | `wbII:prop:analytic-ah-boundary` | Paper II, `wbII:prop:analytic-ah-boundary` (number `B.21`) |
| `lem:analytic-support-specialization` | statement | `wbII:lem:analytic-support-specialization` | Paper II, `wbII:lem:analytic-support-specialization` (number `B.22`) |
| `wb:lem:analytic-support-specialization` | statement | `wbII:lem:analytic-support-specialization` | Paper II, `wbII:lem:analytic-support-specialization` (number `B.22`) |
| `wbII:lem:analytic-support-specialization` | statement | `wbII:lem:analytic-support-specialization` | Paper II, `wbII:lem:analytic-support-specialization` (number `B.22`) |
| `thm:analytic-all-picard` | statement | `wbII:thm:analytic-all-picard` | Paper II, `wbII:thm:analytic-all-picard` (number `B.23`) |
| `wb:thm:analytic-all-picard` | statement | `wbII:thm:analytic-all-picard` | Paper II, `wbII:thm:analytic-all-picard` (number `B.23`) |
| `wbII:thm:analytic-all-picard` | statement | `wbII:thm:analytic-all-picard` | Paper II, `wbII:thm:analytic-all-picard` (number `B.23`) |

## Appendix C. Every label present in the assembled papers

This includes equations, sections, statements and retained proof labels. A label without a number remains addressable by its exact key. No number is inferred from its position in the source.

| Paper | Actual label | Current number |
|---|---|---|
| I | `app:I:programs` | `S` |
| I | `app:I:result-index` | `R` |
| I | `app:cdp-kuranishi` | `L` |
| I | `app:cdp-monodromy` | `K` |
| I | `app:rederive:ari-C.4.1` | `P.13` |
| I | `app:rederive:ari-C.5.1` | `P.14` |
| I | `app:rederive:ari-C.6.R4` | `P.15` |
| I | `app:rederive:ari-C.7.7` | `P.16` |
| I | `app:rederive:ari-C.7.8` | `P.17` |
| I | `app:rederive:fam-src-A.1.1` | `P.1` |
| I | `app:rederive:fam-src-A.5.1` | `P.2` |
| I | `app:rederive:fam-src-A.5.2` | `P.3` |
| I | `app:rederive:fam-src-B.4.1` | `P.4` |
| I | `app:rederive:fam-src-D.1.2` | `P.5` |
| I | `app:rederive:fam-src-D.1.6` | `P.6` |
| I | `app:rederive:fam-src-D.2.3` | `P.7` |
| I | `app:rederive:inv-A1.0` | `P.9` |
| I | `app:rederive:inv-C3.1` | `P.10` |
| I | `app:rederive:inv-C3.6` | `P.11` |
| I | `app:rederive:push-src-B.4.3` | `P.12` |
| I | `app:rederive:push-src-C.3.5` | `P.18` |
| I | `app:rederive:push-src-E.3.1` | `P.8` |
| I | `ari:C.1.1` | `12.1` |
| I | `ari:C.1.2` | `12.2` |
| I | `ari:C.1.3` | `12.3` |
| I | `ari:C.2.1` | `12.4` |
| I | `ari:C.2.2` | `12.5` |
| I | `ari:C.3.1` | `12.6` |
| I | `ari:C.3.2` | `12.7` |
| I | `ari:C.4.1` | `12.8` |
| I | `ari:C.4.2` | `12.9` |
| I | `ari:C.4.3` | `12.10` |
| I | `ari:C.4.4` | `12.11` |
| I | `ari:C.4.5` | `12.12` |
| I | `ari:C.5.1` | `12.13` |
| I | `ari:C.6.1` | `13.1` |
| I | `ari:C.6.2` | `13.2` |
| I | `ari:C.6.3` | `13.3` |
| I | `ari:C.6.4` | `13.4` |
| I | `ari:C.6.5` | `13.5` |
| I | `ari:C.6.R1` | `13.6` |
| I | `ari:C.6.R2` | `13.7` |
| I | `ari:C.6.R3` | `13.8` |
| I | `ari:C.6.R4` | `13.9` |
| I | `ari:C.6.R5` | `13.10` |
| I | `ari:C.6.T1` | `13.11` |
| I | `ari:C.6.T2` | `13.12` |
| I | `ari:C.7.1` | `16.1` |
| I | `ari:C.7.10` | `16.10` |
| I | `ari:C.7.11` | `16.11` |
| I | `ari:C.7.12` | `16.12` |
| I | `ari:C.7.2` | `16.2` |
| I | `ari:C.7.3` | `16.3` |
| I | `ari:C.7.4` | `16.4` |
| I | `ari:C.7.5` | `16.5` |
| I | `ari:C.7.6` | `16.6` |
| I | `ari:C.7.7` | `16.7` |
| I | `ari:C.7.8` | `16.8` |
| I | `ari:C.7.9` | `16.9` |
| I | `ari:C.8.1` | `14.1` |
| I | `ari:C.8.10` | `14.9` |
| I | `ari:C.8.11` | `14.10` |
| I | `ari:C.8.12` | `15.1` |
| I | `ari:C.8.13` | `15.2` |
| I | `ari:C.8.14` | `15.3` |
| I | `ari:C.8.15` | `15.4` |
| I | `ari:C.8.2` | `14.2` |
| I | `ari:C.8.3` | `14.3` |
| I | `ari:C.8.4` | `14.4` |
| I | `ari:C.8.5` | `5.5` |
| I | `ari:C.8.6` | `14.5` |
| I | `ari:C.8.7` | `14.6` |
| I | `ari:C.8.8` | `14.7` |
| I | `ari:C.8.9` | `14.8` |
| I | `ari:eq:Cgz-central-integrality` | `44` |
| I | `ari:eq:Cgz-denominator` | `46` |
| I | `ari:eq:Cgz-product` | `45` |
| I | `ari:eq:Cr-first` | `40` |
| I | `ari:eq:Cr-rational-factor` | `43` |
| I | `ari:eq:Cr-second` | `41` |
| I | `ari:eq:Cr-tails` | `42` |
| I | `ari:eq:ca-GHbounds` | `50` |
| I | `ari:eq:ca-H` | `49` |
| I | `ari:eq:ca-current` | `57` |
| I | `ari:eq:ca-cuspexp` | `60` |
| I | `ari:eq:ca-delta-h` | `52` |
| I | `ari:eq:ca-density0` | `58` |
| I | `ari:eq:ca-density1` | `59` |
| I | `ari:eq:ca-derivatives` | `51` |
| I | `ari:eq:ca-exp` | `48` |
| I | `ari:eq:ca-ladder` | `53` |
| I | `ari:eq:ca-mahler` | `54` |
| I | `ari:eq:ca-nu` | `56` |
| I | `ari:eq:ca-sup` | `47` |
| I | `ari:eq:ca-wpmean` | `55` |
| I | `ari:eq:cc-EZ` | `61` |
| I | `ari:eq:cc-FR` | `63` |
| I | `ari:eq:cc-Ffactored` | `68` |
| I | `ari:eq:cc-Fseries` | `67` |
| I | `ari:eq:cc-P` | `78` |
| I | `ari:eq:cc-constants` | `72` |
| I | `ari:eq:cc-cuspbound` | `64` |
| I | `ari:eq:cc-finite-table` | `76` |
| I | `ari:eq:cc-fixedfield` | `96` |
| I | `ari:eq:cc-h` | `66` |
| I | `ari:eq:cc-norms` | `69` |
| I | `ari:eq:cc-ode` | `65` |
| I | `ari:eq:cc-outer` | `73` |
| I | `ari:eq:cc-power` | `71` |
| I | `ari:eq:cc-radial` | `62` |
| I | `ari:eq:cc-rankcriterion` | `97` |
| I | `ari:eq:cc-recurrence` | `70` |
| I | `ari:eq:cc-scalar` | `77` |
| I | `ari:eq:cc-tail100` | `75` |
| I | `ari:eq:cc-tail60` | `74` |
| I | `ari:eq:cd-compatibility` | `91` |
| I | `ari:eq:cd-slope` | `90` |
| I | `ari:eq:ce-explicit-witness` | `95` |
| I | `ari:eq:ce-gap` | `94` |
| I | `ari:eq:ce-ribet-r` | `92` |
| I | `ari:eq:ce-zeta` | `93` |
| I | `ari:eq:ch-bound` | `38` |
| I | `ari:eq:ch-global` | `35` |
| I | `ari:eq:ch-local-exact` | `37` |
| I | `ari:eq:ch-local-mult` | `36` |
| I | `ari:eq:ch-wp-bracket` | `39` |
| I | `ari:eq:cp-MTdim` | `84` |
| I | `ari:eq:cp-chi` | `83` |
| I | `ari:eq:cp-klein` | `80` |
| I | `ari:eq:cp-periods` | `81` |
| I | `ari:eq:cp-positive-centre` | `85` |
| I | `ari:eq:cp-real-linear` | `86` |
| I | `ari:eq:cp-relation` | `87` |
| I | `ari:eq:cp-sigma` | `79` |
| I | `ari:eq:cp-v` | `82` |
| I | `ari:eq:cs-Li` | `32` |
| I | `ari:eq:cs-division` | `33` |
| I | `ari:eq:cs-isogeny` | `31` |
| I | `ari:eq:cs-torsionvalue` | `34` |
| I | `ari:eq:ct-CMmult` | `88` |
| I | `ari:eq:ct-Gaussian` | `89` |
| I | `ari:open:norm` | `U` |
| I | `cdp:eq:parabolic-law` | `190` |
| I | `cdp:st:D.1.14` | `7.1` |
| I | `cdp:st:E9` | `3.9` |
| I | `def:common-conventions` | `2` |
| I | `eq:d-dual-exact` | `102` |
| I | `eq:d-limit-group` | `101` |
| I | `eq:d-period-normal` | `100` |
| I | `fam:eq:F-Gamma` | `6` |
| I | `fam:eq:F-H` | `9` |
| I | `fam:eq:F-SLpresentation` | `8` |
| I | `fam:eq:F-g` | `5` |
| I | `fam:eq:F-j` | `12` |
| I | `fam:eq:F-law` | `7` |
| I | `fam:eq:F-qD` | `10` |
| I | `fam:eq:F-tauaction` | `11` |
| I | `fam:eq:ab-cusp-resolution` | `250` |
| I | `fam:eq:ab-direct-images` | `253` |
| I | `fam:eq:ab-log-tangent` | `251` |
| I | `fam:eq:ab-normal-quotient` | `254` |
| I | `fam:eq:ab-relative-dualizing` | `252` |
| I | `fam:eq:ab-root-degree` | `249` |
| I | `fam:eq:cd-NS` | `4` |
| I | `fam:eq:cd-beta` | `1` |
| I | `fam:eq:cd-norm` | `3` |
| I | `fam:eq:cd-theta-sections` | `255` |
| I | `fam:eq:cd-wp` | `2` |
| I | `fam:section:A` | `3` |
| I | `fam:section:A.1` | `3.1` |
| I | `fam:section:A.2` | `3.2` |
| I | `fam:section:A.3` | `3.3` |
| I | `fam:section:A.4` | `3.4` |
| I | `fam:section:A.5` | `3.5` |
| I | `fam:section:B` | `4` |
| I | `fam:section:B.1` | `4.1` |
| I | `fam:section:B.2` | `4.2` |
| I | `fam:section:B.3` | `4.3` |
| I | `fam:section:B.4` | `4.4` |
| I | `fam:section:C` | `5` |
| I | `fam:section:C.1` | `5.1` |
| I | `fam:section:C.2` | `5.2` |
| I | `fam:section:C.3` | `5.3` |
| I | `fam:section:C.4` | `5.4` |
| I | `fam:section:D` | `6` |
| I | `fam:section:D.1` | `6.1` |
| I | `fam:section:D.2` | `6.2` |
| I | `fam:section:E` | `19` |
| I | `fam:section:E.1` | `19.1` |
| I | `fam:section:E.2` | `19.2` |
| I | `fam:section:F` | `7` |
| I | `fam:section:F.1` | `7.1` |
| I | `fam:section:F.2` | `7.2` |
| I | `fam:section:F.3` | `7.3` |
| I | `fam:src:A.1.1` | `3.1` |
| I | `fam:src:A.1.2` | `3.2` |
| I | `fam:src:A.2.1` | `3.3` |
| I | `fam:src:A.3.1` | `3.4` |
| I | `fam:src:A.4.1` | `3.5` |
| I | `fam:src:A.4.2` | `3.6` |
| I | `fam:src:A.4.3` | `3.7` |
| I | `fam:src:A.5.1` | `3.8` |
| I | `fam:src:A.5.2` | `3.9` |
| I | `fam:src:B.1.1` | `4.1` |
| I | `fam:src:B.1.2` | `4.2` |
| I | `fam:src:B.1.3` | `4.3` |
| I | `fam:src:B.1.4` | `4.4` |
| I | `fam:src:B.2.1` | `4.5` |
| I | `fam:src:B.2.2` | `4.6` |
| I | `fam:src:B.2.3` | `4.7` |
| I | `fam:src:B.3.1` | `4.8` |
| I | `fam:src:B.4.1` | `4.9` |
| I | `fam:src:B.4.2` | `4.10` |
| I | `fam:src:C.1.1` | `5.1` |
| I | `fam:src:C.1.2` | `5.2` |
| I | `fam:src:C.2.1` | `5.3` |
| I | `fam:src:C.2.2` | `5.4` |
| I | `fam:src:C.2.3` | `5.5` |
| I | `fam:src:C.3.1` | `5.6` |
| I | `fam:src:C.3.2` | `5.7` |
| I | `fam:src:C.3.3` | `5.8` |
| I | `fam:src:C.3.4` | `5.9` |
| I | `fam:src:C.4.1` | `5.10` |
| I | `fam:src:D.1.1` | `6.1` |
| I | `fam:src:D.1.2` | `6.2` |
| I | `fam:src:D.1.3` | `6.3` |
| I | `fam:src:D.1.4` | `6.4` |
| I | `fam:src:D.1.5` | `6.5` |
| I | `fam:src:D.1.6` | `6.6` |
| I | `fam:src:D.1.7` | `6.7` |
| I | `fam:src:D.2.1` | `6.8` |
| I | `fam:src:D.2.2` | `6.9` |
| I | `fam:src:D.2.3` | `6.10` |
| I | `fam:src:E.1.1` | `19.1` |
| I | `fam:src:E.1.2` | `19.2` |
| I | `fam:src:E.1.3` | `19.3` |
| I | `fam:src:E.1.4` | `19.4` |
| I | `fam:src:E.1.5` | `19.5` |
| I | `fam:src:E.2.1` | `19.6` |
| I | `fam:src:F.1.1` | `7.1` |
| I | `fam:src:F.1.2` | `7.2` |
| I | `fam:src:F.2.1` | `7.3` |
| I | `fam:src:F.2.2` | `7.4` |
| I | `fam:src:F.2.3` | `7.5` |
| I | `fam:src:F.3.1` | `7.6` |
| I | `fam:src:F.3.2` | `7.7` |
| I | `fam:src:F.3.3` | `7.8` |
| I | `fam:st:A.1.1` | `3.1` |
| I | `fam:st:A.1.2` | `3.2` |
| I | `fam:st:A.2.1` | `3.3` |
| I | `fam:st:A.3.1` | `3.4` |
| I | `fam:st:A.4.1` | `3.5` |
| I | `fam:st:A.4.2` | `3.6` |
| I | `fam:st:A.4.3` | `3.7` |
| I | `fam:st:A.5.1` | `3.8` |
| I | `fam:st:A.5.2` | `3.9` |
| I | `fam:st:B.1.1` | `4.1` |
| I | `fam:st:B.1.2` | `4.2` |
| I | `fam:st:B.1.3` | `4.3` |
| I | `fam:st:B.1.4` | `4.4` |
| I | `fam:st:B.2.1` | `4.5` |
| I | `fam:st:B.2.2` | `4.6` |
| I | `fam:st:B.2.3` | `4.7` |
| I | `fam:st:B.3.1` | `4.8` |
| I | `fam:st:B.4.1` | `4.9` |
| I | `fam:st:B.4.2` | `4.10` |
| I | `fam:st:C.1.1` | `5.1` |
| I | `fam:st:C.1.2` | `5.2` |
| I | `fam:st:C.2.1` | `5.3` |
| I | `fam:st:C.2.2` | `5.4` |
| I | `fam:st:C.2.3` | `5.5` |
| I | `fam:st:C.3.1` | `5.6` |
| I | `fam:st:C.3.2` | `5.7` |
| I | `fam:st:C.3.3` | `5.8` |
| I | `fam:st:C.3.4` | `5.9` |
| I | `fam:st:C.4.1` | `5.10` |
| I | `fam:st:D.1.1` | `6.1` |
| I | `fam:st:D.1.2` | `6.2` |
| I | `fam:st:D.1.3` | `6.3` |
| I | `fam:st:D.1.4` | `6.4` |
| I | `fam:st:D.1.5` | `6.5` |
| I | `fam:st:D.1.6` | `6.6` |
| I | `fam:st:D.1.7` | `6.7` |
| I | `fam:st:D.2.1` | `6.8` |
| I | `fam:st:D.2.2` | `6.9` |
| I | `fam:st:D.2.3` | `6.10` |
| I | `fam:st:E.1.1` | `19.1` |
| I | `fam:st:E.1.2` | `19.2` |
| I | `fam:st:E.1.3` | `19.3` |
| I | `fam:st:E.1.4` | `19.4` |
| I | `fam:st:E.1.5` | `19.5` |
| I | `fam:st:E.2.1` | `19.6` |
| I | `fam:st:F.1.1` | `7.1` |
| I | `fam:st:F.1.2` | `7.2` |
| I | `fam:st:F.2.1` | `7.3` |
| I | `fam:st:F.2.2` | `7.4` |
| I | `fam:st:F.2.3` | `7.5` |
| I | `fam:st:F.3.1` | `7.6` |
| I | `fam:st:F.3.2` | `7.7` |
| I | `fam:st:F.3.3` | `7.8` |
| I | `inv:A1.0` | `8.1` |
| I | `inv:A1.1` | `8.2` |
| I | `inv:A1.2` | `8.3` |
| I | `inv:A1.3` | `8.4` |
| I | `inv:A2.1` | `8.5` |
| I | `inv:A2.2` | `8.6` |
| I | `inv:A2.3` | `8.7` |
| I | `inv:A2.4` | `8.8` |
| I | `inv:A3.1` | `8.9` |
| I | `inv:A3.2` | `8.10` |
| I | `inv:A4.1` | `8.11` |
| I | `inv:A4.2` | `8.12` |
| I | `inv:B1.0` | `9.1` |
| I | `inv:B1.1` | `9.2` |
| I | `inv:B1.2` | `9.3` |
| I | `inv:B2.1` | `9.4` |
| I | `inv:B2.2` | `9.5` |
| I | `inv:B3.1` | `9.6` |
| I | `inv:B3.2` | `9.7` |
| I | `inv:B3.3` | `9.8` |
| I | `inv:C1.1` | `10.1` |
| I | `inv:C1.2` | `10.2` |
| I | `inv:C2.1` | `10.3` |
| I | `inv:C2.2` | `10.4` |
| I | `inv:C3.1` | `10.5` |
| I | `inv:C3.2` | `10.6` |
| I | `inv:C3.3` | `10.7` |
| I | `inv:C3.4` | `10.8` |
| I | `inv:C3.5` | `10.9` |
| I | `inv:C3.6` | `10.10` |
| I | `inv:C3.7` | `10.11` |
| I | `inv:C3.8` | `T.3` |
| I | `inv:D1.1` | `Q.1` |
| I | `inv:D1.2` | `Q.2` |
| I | `inv:D1.3` | `3.9` |
| I | `inv:D2.1` | `3.9` |
| I | `inv:D3.1` | `3.9` |
| I | `inv:D4.1` | `11.1` |
| I | `inv:D4.2` | `11.2` |
| I | `inv:D4.3` | `11.3` |
| I | `inv:D4.4` | `11.4` |
| I | `inv:D4.5` | `11.5` |
| I | `inv:eq:A-DI-branch` | `20` |
| I | `inv:eq:A-E-line` | `13` |
| I | `inv:eq:A-H-images` | `14` |
| I | `inv:eq:A-N-images` | `15` |
| I | `inv:eq:A-absolute-table` | `16` |
| I | `inv:eq:A-modular-K` | `18` |
| I | `inv:eq:A-mu-value` | `19` |
| I | `inv:eq:A-s-branch` | `17` |
| I | `inv:eq:C-BC-A` | `22` |
| I | `inv:eq:C-G-Green` | `25` |
| I | `inv:eq:C-Pic-map` | `24` |
| I | `inv:eq:C-Ricci` | `29` |
| I | `inv:eq:C-arrows` | `23` |
| I | `inv:eq:C-collar-sum` | `27` |
| I | `inv:eq:C-delta` | `28` |
| I | `inv:eq:C-eta-negative` | `30` |
| I | `inv:eq:C-factor12` | `26` |
| I | `inv:eq:C-hodge-input` | `21` |
| I | `inv:notation-dictionary` | `A` |
| I | `inv:sec:partA` | `8` |
| I | `inv:sec:partC` | `10` |
| I | `inv:wb:analytic-picard-proofs` | `M` |
| I | `inv:wb:eq:11.1` | `{WBH.11.1}` |
| I | `inv:wb:eq:11.10` | `{WBH.11.10}` |
| I | `inv:wb:eq:11.10a` | `{WBH.11.10a}` |
| I | `inv:wb:eq:11.10b` | `{WBH.11.10b}` |
| I | `inv:wb:eq:11.11` | `{WBH.11.11}` |
| I | `inv:wb:eq:11.11a` | `{WBH.11.11a}` |
| I | `inv:wb:eq:11.12` | `{WBH.11.12}` |
| I | `inv:wb:eq:11.14` | `{WBH.11.14}` |
| I | `inv:wb:eq:11.15` | `{WBH.11.15}` |
| I | `inv:wb:eq:11.16` | `{WBH.11.16}` |
| I | `inv:wb:eq:11.16a` | `{WBH.11.16a}` |
| I | `inv:wb:eq:11.16b` | `{WBH.11.16b}` |
| I | `inv:wb:eq:11.16c` | `{WBH.11.16c}` |
| I | `inv:wb:eq:11.17` | `{WBH.11.17}` |
| I | `inv:wb:eq:11.17a` | `{WBH.11.17a}` |
| I | `inv:wb:eq:11.17a-doubleprime` | `{WBH.11.17a$''$}` |
| I | `inv:wb:eq:11.17a-fin` | `{WBH.$11.17a_{\mathrm  {fin}}$}` |
| I | `inv:wb:eq:11.17a-prime` | `{WBH.11.17a$'$}` |
| I | `inv:wb:eq:11.17b` | `{WBH.11.17b}` |
| I | `inv:wb:eq:11.17c` | `{WBH.11.17c}` |
| I | `inv:wb:eq:11.17d` | `{WBH.11.17d}` |
| I | `inv:wb:eq:11.17d-doubleprime` | `{WBH.11.17d$''$}` |
| I | `inv:wb:eq:11.17d-prime` | `{WBH.11.17d$'$}` |
| I | `inv:wb:eq:11.17e` | `{WBH.11.17e}` |
| I | `inv:wb:eq:11.17f` | `{WBH.11.17f}` |
| I | `inv:wb:eq:11.18` | `{WBH.11.18}` |
| I | `inv:wb:eq:11.18a` | `{WBH.11.18a}` |
| I | `inv:wb:eq:11.18b` | `{WBH.11.18b}` |
| I | `inv:wb:eq:11.19` | `{WBH.11.19}` |
| I | `inv:wb:eq:11.19a` | `{WBH.11.19a}` |
| I | `inv:wb:eq:11.19f` | `{WBH.11.19f}` |
| I | `inv:wb:eq:11.2` | `{WBH.11.2}` |
| I | `inv:wb:eq:11.20` | `{WBH.11.20}` |
| I | `inv:wb:eq:11.20a` | `{WBH.11.20a}` |
| I | `inv:wb:eq:11.25` | `{WBH.11.25}` |
| I | `inv:wb:eq:11.3` | `{WBH.11.3}` |
| I | `inv:wb:eq:11.3a` | `{WBH.11.3a}` |
| I | `inv:wb:eq:11.4` | `{WBH.11.4}` |
| I | `inv:wb:eq:11.5` | `{WBH.11.5}` |
| I | `inv:wb:eq:11.8` | `{WBH.11.8}` |
| I | `inv:wb:eq:11.9` | `{WBH.11.9}` |
| I | `inv:wb:eq:9.10` | `{WBA.9.10}` |
| I | `inv:wb:eq:9.11` | `{WBA.9.11}` |
| I | `inv:wb:eq:9.14` | `{WBA.9.14}` |
| I | `inv:wb:eq:9.15` | `{WBA.9.15}` |
| I | `inv:wb:eq:9.16` | `{WBA.9.16}` |
| I | `inv:wbproof:cor:exact-hodge-diamond` | `N.6.2` |
| I | `inv:wbproof:cor:picard-line-audit` | `M.2.2` |
| I | `inv:wbproof:lem:bcpr-degree-one-input` | `O.3.1` |
| I | `inv:wbproof:lem:bcpr-eta-extension` | `O.3.2` |
| I | `inv:wbproof:lem:cusp-structure-sheaf-audit` | `M.1.1` |
| I | `inv:wbproof:prop:absolute-cotangent-direct-images` | `N.5.1` |
| I | `inv:wbproof:prop:bcpr-generators-are-bases` | `O.5.1` |
| I | `inv:wbproof:prop:log-ks-divisor` | `N.4.2` |
| I | `inv:wbproof:prop:log-relative-direct-images` | `N.4.1` |
| I | `inv:wbproof:prop:period-derivative-determinant` | `N.3.1` |
| I | `inv:wbproof:prop:workbench-holomorphic-form-vanishing` | `N.1.1` |
| I | `inv:wbproof:thm:bcpr-square-zero-algebra` | `O.6.1` |
| I | `inv:wbproof:thm:exact-bott-chern-aeppli` | `N.7.1` |
| I | `inv:wbproof:thm:frolicher-e2-candidate` | `N.2.2` |
| I | `inv:wbproof:thm:h12-scalar` | `N.6.1` |
| I | `inv:wbproof:thm:parametric-hodge-diamond` | `N.2.1` |
| I | `inv:wbproof:thm:structure-direct-images-audit` | `M.2.1` |
| I | `inv:wbproof:torsion-residue` | `N.5.2` |
| I | `mapsI:chain:corollary:2.2` | `F.3` |
| I | `mapsI:chain:lemma:1.1` | `F.1` |
| I | `mapsI:chain:lemma:2.1` | `F.2` |
| I | `mapsI:chain:lemma:4.1` | `F.4` |
| I | `mapsI:chain:section` | `F` |
| I | `mapsI:chain:section-1` | `F.1` |
| I | `mapsI:chain:section-2` | `F.2` |
| I | `mapsI:chain:section-3` | `F.3` |
| I | `mapsI:chain:section-4` | `F.4` |
| I | `mapsI:circle-quotient` | `17` |
| I | `mapsI:closing:eq:C-explicit-closing` | `98` |
| I | `mapsI:closing:eq:C-twelve-scalar` | `99` |
| I | `mapsI:course:CG-S6-07-HOMOTOPY` | `I.1` |
| I | `mapsI:course:degree-one` | `189` |
| I | `mapsI:course:homotopy-section` | `I` |
| I | `mapsI:cw:cw-hurewicz-exercises` | `G.5` |
| I | `mapsI:cw:cw-manifolds` | `G.2` |
| I | `mapsI:cw:cw-open` | `G.1` |
| I | `mapsI:cw:eq:1.1` | `112` |
| I | `mapsI:cw:eq:1.2` | `113` |
| I | `mapsI:cw:eq:1.3` | `114` |
| I | `mapsI:cw:eq:1.4` | `115` |
| I | `mapsI:cw:eq:1.5` | `116` |
| I | `mapsI:cw:eq:1.6` | `117` |
| I | `mapsI:cw:eq:1.7` | `118` |
| I | `mapsI:cw:eq:2.1` | `119` |
| I | `mapsI:cw:eq:2.2` | `120` |
| I | `mapsI:cw:eq:2.3` | `121` |
| I | `mapsI:cw:eq:2.4` | `122` |
| I | `mapsI:cw:eq:2.5` | `123` |
| I | `mapsI:cw:eq:2.6` | `124` |
| I | `mapsI:cw:eq:3.1` | `125` |
| I | `mapsI:cw:eq:3.2` | `126` |
| I | `mapsI:cw:eq:3.3` | `127` |
| I | `mapsI:cw:eq:4.1` | `128` |
| I | `mapsI:cw:eq:4.2` | `129` |
| I | `mapsI:cw:eq:4.3` | `130` |
| I | `mapsI:cw:eq:4.4` | `131` |
| I | `mapsI:cw:eq:4.5` | `132` |
| I | `mapsI:cw:eq:5.1` | `133` |
| I | `mapsI:cw:eq:5.2` | `134` |
| I | `mapsI:cw:eq:5.3` | `135` |
| I | `mapsI:cw:exercise:5.1` | `G.2` |
| I | `mapsI:cw:exercise:5.2` | `G.3` |
| I | `mapsI:cw:hurewicz-coherent` | `G.3` |
| I | `mapsI:cw:hurewicz-theorem` | `G.4` |
| I | `mapsI:cw:hurewicz-theorem-result` | `G.1` |
| I | `mapsI:cw:section` | `G` |
| I | `mapsI:hodge:line` | `L.1` |
| I | `mapsI:pf:cw-inverses` | `H.4` |
| I | `mapsI:pf:eq:1.1` | `136` |
| I | `mapsI:pf:eq:1.10` | `145` |
| I | `mapsI:pf:eq:1.11` | `146` |
| I | `mapsI:pf:eq:1.12` | `147` |
| I | `mapsI:pf:eq:1.13` | `148` |
| I | `mapsI:pf:eq:1.14` | `149` |
| I | `mapsI:pf:eq:1.2` | `137` |
| I | `mapsI:pf:eq:1.3` | `138` |
| I | `mapsI:pf:eq:1.4` | `139` |
| I | `mapsI:pf:eq:1.5` | `140` |
| I | `mapsI:pf:eq:1.6` | `141` |
| I | `mapsI:pf:eq:1.7` | `142` |
| I | `mapsI:pf:eq:1.8` | `143` |
| I | `mapsI:pf:eq:1.9` | `144` |
| I | `mapsI:pf:eq:2.1` | `150` |
| I | `mapsI:pf:eq:2.2` | `151` |
| I | `mapsI:pf:eq:2.3` | `152` |
| I | `mapsI:pf:eq:2.4` | `153` |
| I | `mapsI:pf:eq:2.5` | `154` |
| I | `mapsI:pf:eq:2.6` | `155` |
| I | `mapsI:pf:eq:2.7` | `156` |
| I | `mapsI:pf:eq:3.1` | `157` |
| I | `mapsI:pf:eq:3.10` | `166` |
| I | `mapsI:pf:eq:3.2` | `158` |
| I | `mapsI:pf:eq:3.3` | `159` |
| I | `mapsI:pf:eq:3.4` | `160` |
| I | `mapsI:pf:eq:3.5` | `161` |
| I | `mapsI:pf:eq:3.6` | `162` |
| I | `mapsI:pf:eq:3.7` | `163` |
| I | `mapsI:pf:eq:3.8` | `164` |
| I | `mapsI:pf:eq:3.9` | `165` |
| I | `mapsI:pf:eq:4.1` | `167` |
| I | `mapsI:pf:eq:4.2` | `168` |
| I | `mapsI:pf:eq:4.3` | `169` |
| I | `mapsI:pf:eq:4.4` | `170` |
| I | `mapsI:pf:eq:4.5` | `171` |
| I | `mapsI:pf:eq:5.1` | `172` |
| I | `mapsI:pf:eq:5.10` | `181` |
| I | `mapsI:pf:eq:5.11` | `182` |
| I | `mapsI:pf:eq:5.12` | `183` |
| I | `mapsI:pf:eq:5.2` | `173` |
| I | `mapsI:pf:eq:5.3` | `174` |
| I | `mapsI:pf:eq:5.4` | `175` |
| I | `mapsI:pf:eq:5.5` | `176` |
| I | `mapsI:pf:eq:5.6` | `177` |
| I | `mapsI:pf:eq:5.7` | `178` |
| I | `mapsI:pf:eq:5.8` | `179` |
| I | `mapsI:pf:eq:5.9` | `180` |
| I | `mapsI:pf:eq:6.1` | `184` |
| I | `mapsI:pf:eq:6.2` | `185` |
| I | `mapsI:pf:eq:6.3` | `186` |
| I | `mapsI:pf:eq:6.4` | `187` |
| I | `mapsI:pf:eq:6.5` | `188` |
| I | `mapsI:pf:exercise:6.1` | `H.2` |
| I | `mapsI:pf:exercise:6.2` | `H.3` |
| I | `mapsI:pf:filtered-chains` | `H.2` |
| I | `mapsI:pf:integral-comparison` | `H.5` |
| I | `mapsI:pf:path-fibre-exercises` | `H.6` |
| I | `mapsI:pf:path-lifting` | `H.1` |
| I | `mapsI:pf:section` | `H` |
| I | `mapsI:pf:serre-homology` | `H.3` |
| I | `mapsI:pf:theorem:5.1` | `H.1` |
| I | `mapsI:quotient-eq-1` | `17.1` |
| I | `mapsI:quotient-eq-2` | `17` |
| I | `mapsI:quotient-eq-3` | `17` |
| I | `mapsI:quotient-eq-4` | `17` |
| I | `mapsI:quotient-eq-5` | `17` |
| I | `mapsI:quotient-eq-6` | `17.3` |
| I | `mapsI:quotient-eq-7` | `17` |
| I | `mapsI:real-eq-1` | `18` |
| I | `mapsI:real-eq-2` | `18` |
| I | `mapsI:real-eq-3` | `18.2` |
| I | `mapsI:real-eq-4` | `18` |
| I | `mapsI:real-eq-5` | `18` |
| I | `mapsI:real-eq-6` | `18` |
| I | `mapsI:real-eq-7` | `18` |
| I | `mapsI:real-eq-8` | `18` |
| I | `mapsI:real-eq-9` | `18.4` |
| I | `mapsI:real-forms` | `18` |
| I | `mapsI:src:A.1.1` | `17.1` |
| I | `mapsI:src:A.1.2` | `17.2` |
| I | `mapsI:src:A.1.3` | `17.3` |
| I | `mapsI:src:A.2.1` | `17.4` |
| I | `mapsI:src:A.3.1` | `18.1` |
| I | `mapsI:src:A.3.2` | `18.2` |
| I | `mapsI:src:A.3.3` | `18.3` |
| I | `mapsI:src:A.3.4` | `18.4` |
| I | `mapsI:top:cor:abstract-s6` | `E.18` |
| I | `mapsI:top:cor:candidate-mv-sphere` | `E.19` |
| I | `mapsI:top:cor:candidate-sphere` | `D.7` |
| I | `mapsI:top:finite-degree-three` | `E.11` |
| I | `mapsI:top:lem:cohomological-closure` | `E.16` |
| I | `mapsI:top:lem:collapse-straightening` | `E.2` |
| I | `mapsI:top:lem:first-transgression` | `D.3` |
| I | `mapsI:top:lem:higher-transgressions` | `D.4` |
| I | `mapsI:top:lem:phase-spread-collapse` | `E.4` |
| I | `mapsI:top:lem:positive-collapse` | `E.3` |
| I | `mapsI:top:prop:actual-finite-band-maps` | `E.10` |
| I | `mapsI:top:prop:cusp-mv-blocks` | `E.12` |
| I | `mapsI:top:prop:geometric-pi1` | `D.6` |
| I | `mapsI:top:prop:leray-e2` | `D.2` |
| I | `mapsI:top:prop:topological-spine` | `E.1` |
| I | `mapsI:top:prop:verified-cellular-collapse` | `E.5` |
| I | `mapsI:top:prop:verified-collapse-homology` | `E.6` |
| I | `mapsI:top:record:vankampen` | `E.9` |
| I | `mapsI:top:remark:L1113` | `E.15` |
| I | `mapsI:top:remark:L600` | `E.8` |
| I | `mapsI:top:remark:L920` | `E.13` |
| I | `mapsI:top:sec:integral-leray` | `D` |
| I | `mapsI:top:thm:collapse-equals-specialization` | `E.7` |
| I | `mapsI:top:thm:h2-vanishing` | `D.5` |
| I | `mapsI:top:thm:mv-leray-comparison` | `E.14` |
| I | `mapsI:top:thm:p0-integral-specialization` | `D.1` |
| I | `mapsI:top:thm:sphere-recognition` | `E.17` |
| I | `push:A11` | `20.1` |
| I | `push:A12` | `20.2` |
| I | `push:A21` | `20.3` |
| I | `push:A22` | `20.4` |
| I | `push:A23` | `20.5` |
| I | `push:A24` | `20.6` |
| I | `push:A25` | `20.7` |
| I | `push:A31` | `20.8` |
| I | `push:A32` | `20.9` |
| I | `push:A33` | `20.10` |
| I | `push:A41` | `20.11` |
| I | `push:A42` | `20.12` |
| I | `push:A43` | `20.13` |
| I | `push:A44` | `20.14` |
| I | `push:A45` | `20.15` |
| I | `push:A46` | `20.16` |
| I | `push:A47` | `20.17` |
| I | `push:A48` | `20.18` |
| I | `push:A49` | `20.19` |
| I | `push:B11` | `21.1` |
| I | `push:B12` | `21.2` |
| I | `push:B21` | `21.3` |
| I | `push:B22` | `21.4` |
| I | `push:B23` | `21.5` |
| I | `push:B31` | `21.6` |
| I | `push:B32` | `21.7` |
| I | `push:B33` | `21.8` |
| I | `push:B34` | `21.9` |
| I | `push:B35` | `21.10` |
| I | `push:B36` | `21.11` |
| I | `push:B37` | `21.12` |
| I | `push:B38` | `21.13` |
| I | `push:B41` | `21.14` |
| I | `push:B415` | `21.33` |
| I | `push:B416` | `21.35` |
| I | `push:B418` | `21.38` |
| I | `push:B419` | `21.40` |
| I | `push:B42` | `21.15` |
| I | `push:B420` | `21.41` |
| I | `push:B422` | `21.43` |
| I | `push:B424` | `21.45` |
| I | `push:B425` | `21.46` |
| I | `push:B426` | `21.48` |
| I | `push:B427` | `21.49` |
| I | `push:B429` | `21.52` |
| I | `push:B430` | `21.53` |
| I | `push:B432` | `21.56` |
| I | `push:B433` | `21.58` |
| I | `push:B46` | `21.19` |
| I | `push:B51` | `21.59` |
| I | `push:section:A` | `20` |
| I | `push:section:A.1` | `20.1` |
| I | `push:section:A.2` | `20.2` |
| I | `push:section:A.3` | `20.3` |
| I | `push:section:A.4` | `20.4` |
| I | `push:section:B` | `21` |
| I | `push:section:B.1` | `21.1` |
| I | `push:section:B.2` | `21.2` |
| I | `push:section:B.3` | `21.3` |
| I | `push:section:D` | `22` |
| I | `push:section:D.1` | `22.1` |
| I | `push:section:D.2` | `22.2` |
| I | `push:section:D.3` | `22.3` |
| I | `push:section:D.4` | `22.4` |
| I | `push:section:E` | `23` |
| I | `push:section:E.1` | `23.1` |
| I | `push:section:E.2` | `23.2` |
| I | `push:section:E.3` | `23.3` |
| I | `push:section:E.4` | `23.4` |
| I | `push:src:A.1.1` | `20.1` |
| I | `push:src:A.1.2` | `20.2` |
| I | `push:src:A.2.1` | `20.3` |
| I | `push:src:A.2.2` | `20.4` |
| I | `push:src:A.2.3` | `20.5` |
| I | `push:src:A.2.4` | `20.6` |
| I | `push:src:A.2.5` | `20.7` |
| I | `push:src:A.3.1` | `20.8` |
| I | `push:src:A.3.2` | `20.9` |
| I | `push:src:A.3.3` | `20.10` |
| I | `push:src:A.4.1` | `20.11` |
| I | `push:src:A.4.2` | `20.12` |
| I | `push:src:A.4.3` | `20.13` |
| I | `push:src:A.4.4` | `20.14` |
| I | `push:src:A.4.5` | `20.15` |
| I | `push:src:A.4.6` | `20.16` |
| I | `push:src:A.4.7` | `20.17` |
| I | `push:src:A.4.8` | `20.18` |
| I | `push:src:A.4.9` | `20.19` |
| I | `push:src:B.1.1` | `21.1` |
| I | `push:src:B.1.2` | `21.2` |
| I | `push:src:B.2.1` | `21.3` |
| I | `push:src:B.2.2` | `21.4` |
| I | `push:src:B.2.3` | `21.5` |
| I | `push:src:B.3.1` | `21.6` |
| I | `push:src:B.3.2` | `21.7` |
| I | `push:src:B.3.3` | `21.8` |
| I | `push:src:B.3.4` | `21.9` |
| I | `push:src:B.3.5` | `21.10` |
| I | `push:src:B.3.6` | `21.11` |
| I | `push:src:B.3.7` | `21.12` |
| I | `push:src:B.3.8` | `21.13` |
| I | `push:src:B.4.1` | `21.14` |
| I | `push:src:B.4.10` | `21.26` |
| I | `push:src:B.4.11` | `21.28` |
| I | `push:src:B.4.12` | `21.29` |
| I | `push:src:B.4.13` | `21.30` |
| I | `push:src:B.4.14` | `21.32` |
| I | `push:src:B.4.15` | `21.33` |
| I | `push:src:B.4.16` | `21.35` |
| I | `push:src:B.4.17` | `21.36` |
| I | `push:src:B.4.18` | `21.38` |
| I | `push:src:B.4.19` | `21.40` |
| I | `push:src:B.4.2` | `21.15` |
| I | `push:src:B.4.20` | `21.41` |
| I | `push:src:B.4.21` | `21.42` |
| I | `push:src:B.4.22` | `21.43` |
| I | `push:src:B.4.23` | `21.44` |
| I | `push:src:B.4.24` | `21.45` |
| I | `push:src:B.4.25` | `21.46` |
| I | `push:src:B.4.26` | `21.48` |
| I | `push:src:B.4.27` | `21.49` |
| I | `push:src:B.4.28` | `21.50` |
| I | `push:src:B.4.29` | `21.52` |
| I | `push:src:B.4.3` | `21.16` |
| I | `push:src:B.4.30` | `21.53` |
| I | `push:src:B.4.31` | `21.54` |
| I | `push:src:B.4.32` | `21.56` |
| I | `push:src:B.4.33` | `21.58` |
| I | `push:src:B.4.4` | `21.17` |
| I | `push:src:B.4.5` | `21.18` |
| I | `push:src:B.4.6` | `21.19` |
| I | `push:src:B.4.7` | `21.20` |
| I | `push:src:B.4.8` | `21.23` |
| I | `push:src:B.4.9` | `21.25` |
| I | `push:src:B.5.1` | `21.59` |
| I | `push:src:C.3.5` | `18.5` |
| I | `push:src:D.1.1` | `22.1` |
| I | `push:src:D.1.2` | `22.2` |
| I | `push:src:D.1.3` | `22.3` |
| I | `push:src:D.2.1` | `22.4` |
| I | `push:src:D.2.2` | `22.5` |
| I | `push:src:D.2.3` | `22.6` |
| I | `push:src:D.2.4` | `22.7` |
| I | `push:src:D.3.1` | `22.8` |
| I | `push:src:D.3.2` | `22.9` |
| I | `push:src:D.4.1` | `22.10` |
| I | `push:src:D.4.2` | `22.11` |
| I | `push:src:D.4.3` | `22.12` |
| I | `push:src:D.4.4` | `22.13` |
| I | `push:src:D.4.5` | `22.14` |
| I | `push:src:D.4.6` | `22.15` |
| I | `push:src:D.4.7` | `22.16` |
| I | `push:src:D.4.8` | `22.17` |
| I | `push:src:E.1.1` | `23.1` |
| I | `push:src:E.1.2` | `23.2` |
| I | `push:src:E.1.3` | `23.3` |
| I | `push:src:E.2.1` | `23.4` |
| I | `push:src:E.2.2` | `23.5` |
| I | `push:src:E.2.3` | `23.6` |
| I | `push:src:E.3.1` | `23.7` |
| I | `push:src:E.3.2` | `23.8` |
| I | `push:src:E.3.3` | `23.9` |
| I | `push:src:E.4.1` | `23.10` |
| I | `push:src:E.4.2` | `23.11` |
| I | `push:src:E.4.3` | `5.5` |
| I | `sec:I:verification` | `V` |
| I | `sec:e4` | `23.4` |
| I | `wb:cor:exact-hodge-diamond` | `8.9` |
| I | `wb:cor:picard-line-audit` | `10.5` |
| I | `wb:eq:bcpr-a-b-definitions` | `221` |
| I | `wb:eq:bcpr-a-square-bc-zero` | `241` |
| I | `wb:eq:bcpr-a-square-d1` | `239` |
| I | `wb:eq:bcpr-appell-humbert-matrix` | `206` |
| I | `wb:eq:bcpr-b-square-dolbeault-zero` | `238` |
| I | `wb:eq:bcpr-base-orientation` | `219` |
| I | `wb:eq:bcpr-bc-definition` | `191` |
| I | `wb:eq:bcpr-bc-to-dolbeault-32` | `242` |
| I | `wb:eq:bcpr-c-nonzero` | `229` |
| I | `wb:eq:bcpr-c1-pullback` | `227` |
| I | `wb:eq:bcpr-chern-convention` | `225` |
| I | `wb:eq:bcpr-chern-exp-identity` | `226` |
| I | `wb:eq:bcpr-cotangent-edge` | `215` |
| I | `wb:eq:bcpr-cotangent-kernel` | `213` |
| I | `wb:eq:bcpr-cusp-log-basis` | `212` |
| I | `wb:eq:bcpr-d-nonzero` | `232` |
| I | `wb:eq:bcpr-de-rham-primitives` | `247` |
| I | `wb:eq:bcpr-delta` | `198` |
| I | `wb:eq:bcpr-dolbeault-map` | `192` |
| I | `wb:eq:bcpr-e-nonzero` | `233` |
| I | `wb:eq:bcpr-eta-decomposition` | `204` |
| I | `wb:eq:bcpr-eta-square` | `196` |
| I | `wb:eq:bcpr-exponential-transgression` | `218` |
| I | `wb:eq:bcpr-factor-twelve` | `220` |
| I | `wb:eq:bcpr-finite-invariant-basis` | `211` |
| I | `wb:eq:bcpr-first-zero-products` | `236` |
| I | `wb:eq:bcpr-gamma-form` | `202` |
| I | `wb:eq:bcpr-generators` | `228` |
| I | `wb:eq:bcpr-global-integral-line` | `217` |
| I | `wb:eq:bcpr-global-representatives` | `216` |
| I | `wb:eq:bcpr-hodge-row-one` | `193` |
| I | `wb:eq:bcpr-hodge-row-two` | `194` |
| I | `wb:eq:bcpr-holomorphic-structure` | `222` |
| I | `wb:eq:bcpr-lattice-columns` | `199` |
| I | `wb:eq:bcpr-linear-function-increments` | `201` |
| I | `wb:eq:bcpr-nonzero-dimensions` | `195` |
| I | `wb:eq:bcpr-period-rows` | `197` |
| I | `wb:eq:bcpr-phi-primitive` | `240` |
| I | `wb:eq:bcpr-product-ab` | `234` |
| I | `wb:eq:bcpr-product-acbar-bc` | `235` |
| I | `wb:eq:bcpr-q-fibre` | `205` |
| I | `wb:eq:bcpr-q-fibre-expanded` | `207` |
| I | `wb:eq:bcpr-q-gamma-product` | `208` |
| I | `wb:eq:bcpr-q-gamma-serre-pairing` | `231` |
| I | `wb:eq:bcpr-q-square` | `209` |
| I | `wb:eq:bcpr-q-square-integral` | `214` |
| I | `wb:eq:bcpr-real-linear-functions` | `200` |
| I | `wb:eq:bcpr-relative-eta-section` | `210` |
| I | `wb:eq:bcpr-second-zero-products` | `245` |
| I | `wb:eq:bcpr-serre-pairing` | `244` |
| I | `wb:eq:bcpr-serre-pairing-zero` | `243` |
| I | `wb:eq:bcpr-sum-of-squares` | `237` |
| I | `wb:eq:bcpr-top-integration` | `248` |
| I | `wb:eq:bcpr-top-products` | `246` |
| I | `wb:eq:bcpr-u-form` | `203` |
| I | `wb:eq:bcpr-unit-chern-connection` | `223` |
| I | `wb:eq:bcpr-unit-chern-curvature` | `224` |
| I | `wb:eq:bcpr-v-class` | `230` |
| I | `wb:eq:candidate-global-canonical-on-cusp` | `111` |
| I | `wb:eq:cusp-closed-chart-identity` | `109` |
| I | `wb:eq:cusp-exact-opposite-edge` | `110` |
| I | `wb:eq:period-deck-certificate` | `108` |
| I | `wb:eq:period-deck-homomorphism` | `106` |
| I | `wb:eq:period-second-generator-from-cusp` | `107` |
| I | `wb:eq:semidirect-abelianization` | `{SD.1}` |
| I | `wb:eq:triangle-cayley-coordinates` | `104` |
| I | `wb:eq:triangle-generator-derivatives` | `103` |
| I | `wb:eq:triangle-linearizing-identities` | `105` |
| I | `wb:ffcert:cor:covering-h1` | `C.14` |
| I | `wb:ffcert:eq:addition-maps` | `{FF12}` |
| I | `wb:ffcert:eq:all-branches` | `{FF28}` |
| I | `wb:ffcert:eq:annihilators-indices` | `{FF8}` |
| I | `wb:ffcert:eq:branch-identification` | `{FF29}` |
| I | `wb:ffcert:eq:central-covariance` | `{FF18}` |
| I | `wb:ffcert:eq:central-parameters` | `{FF4}` |
| I | `wb:ffcert:eq:coinvariant-coordinates` | `{FF41}` |
| I | `wb:ffcert:eq:complex-images` | `{FF10}` |
| I | `wb:ffcert:eq:contragredient-direction` | `{FF39}` |
| I | `wb:ffcert:eq:cover-freeness` | `{FF33}` |
| I | `wb:ffcert:eq:cover-real-action` | `{FF32}` |
| I | `wb:ffcert:eq:disc-and-phase` | `{FF23}` |
| I | `wb:ffcert:eq:elliptic-factors` | `{FF11}` |
| I | `wb:ffcert:eq:full-deck-group` | `{FF30}` |
| I | `wb:ffcert:eq:image-columns` | `{FF9}` |
| I | `wb:ffcert:eq:integral-h1-image` | `{FF40}` |
| I | `wb:ffcert:eq:integral-summands` | `{FF7}` |
| I | `wb:ffcert:eq:joint-freeness` | `{FF22}` |
| I | `wb:ffcert:eq:kernel-lifts` | `{FF17}` |
| I | `wb:ffcert:eq:kernel-points` | `{FF14}` |
| I | `wb:ffcert:eq:kernel-rotation` | `{FF21}` |
| I | `wb:ffcert:eq:log-cover-action` | `{FF34}` |
| I | `wb:ffcert:eq:marking` | `{FF1}` |
| I | `wb:ffcert:eq:matrices-translations` | `{FF2}` |
| I | `wb:ffcert:eq:moving-generators` | `{FF6}` |
| I | `wb:ffcert:eq:moving-rotations` | `{FF20}` |
| I | `wb:ffcert:eq:negative-orientation` | `{FF5}` |
| I | `wb:ffcert:eq:normal-action` | `{FF42}` |
| I | `wb:ffcert:eq:normal-product-isomorphism` | `{FF46}` |
| I | `wb:ffcert:eq:normal-section-character` | `{FF43}` |
| I | `wb:ffcert:eq:normalization-deck` | `{FF27}` |
| I | `wb:ffcert:eq:normalization-map` | `{FF26}` |
| I | `wb:ffcert:eq:ordinary-log-deck` | `{FF35}` |
| I | `wb:ffcert:eq:overlap-conjugacy` | `{FF37}` |
| I | `wb:ffcert:eq:overlap-map` | `{FF36}` |
| I | `wb:ffcert:eq:periods` | `{FF3}` |
| I | `wb:ffcert:eq:product-generators` | `{FF15}` |
| I | `wb:ffcert:eq:product-intertwining` | `{FF19}` |
| I | `wb:ffcert:eq:real-overlap` | `{FF38}` |
| I | `wb:ffcert:eq:smooth-equivariance` | `{FF45}` |
| I | `wb:ffcert:eq:smooth-normal-section` | `{FF44}` |
| I | `wb:ffcert:eq:surface-product-covers` | `{FF16}` |
| I | `wb:ffcert:eq:torus-covers` | `{FF13}` |
| I | `wb:ffcert:eq:varying-action` | `{FF24}` |
| I | `wb:ffcert:eq:varying-powers` | `{FF25}` |
| I | `wb:ffcert:eq:whole-kernel` | `{FF31}` |
| I | `wb:ffcert:prop:integral-summands` | `C.9` |
| I | `wb:ffcert:prop:quotient-charts` | `C.11` |
| I | `wb:ffcert:sec:finite-fillings` | `C.6` |
| I | `wb:ffcert:thm:normal-trivialization` | `C.15` |
| I | `wb:ffcert:thm:normalization` | `C.12` |
| I | `wb:ffcert:thm:peripheral-kernel` | `C.13` |
| I | `wb:ffcert:thm:product-covers` | `C.10` |
| I | `wb:lem:bcpr-degree-one-input` | `10.6` |
| I | `wb:lem:bcpr-eta-extension` | `8.10` |
| I | `wb:lem:cusp-structure-sheaf-audit` | `8.1` |
| I | `wb:lem:finite-filling-stalk-map` | `B.10` |
| I | `wb:lem:finite-normal-order-audit` | `C.15` |
| I | `wb:lem:hodge-line-audit` | `L.1` |
| I | `wb:lem:meromorphic-descent-audit` | `J.3` |
| I | `wb:lem:middle-period-proper` | `B.8` |
| I | `wb:lem:semidirect-abelianization` | `C.8` |
| I | `wb:lem:toric-chart-control` | `B.5` |
| I | `wb:lem:torus-algebraic-reduction-audit` | `J.1` |
| I | `wb:lem:triangle-generator-orientations` | `B.1` |
| I | `wb:prop:absolute-cotangent-direct-images` | `8.4` |
| I | `wb:prop:bcpr-generators-are-bases` | `10.7` |
| I | `wb:prop:candidate-cusp-overlap` | `B.7` |
| I | `wb:prop:candidate-finite-fillings` | `B.9` |
| I | `wb:prop:finite-indices` | `C.4` |
| I | `wb:prop:log-ks-divisor` | `8.5` |
| I | `wb:prop:log-relative-direct-images` | `8.3` |
| I | `wb:prop:monodromy-certificate` | `C.1` |
| I | `wb:prop:period-derivative-determinant` | `8.5` |
| I | `wb:prop:period-exact-admissible-constants` | `B.3` |
| I | `wb:prop:period-input-audit` | `B.2` |
| I | `wb:prop:terminal-all-degree` | `C.7` |
| I | `wb:prop:terminal-degree-two` | `C.6` |
| I | `wb:prop:terminal-group` | `C.5` |
| I | `wb:prop:very-general-torus-audit` | `J.2` |
| I | `wb:prop:workbench-holomorphic-form-vanishing` | `8.9` |
| I | `wb:pshift:eq:actual-overlap-difference` | `{PS17}` |
| I | `wb:pshift:eq:affine-bundle-action` | `{PS23}` |
| I | `wb:pshift:eq:centralizer` | `{PS7}` |
| I | `wb:pshift:eq:cocycle-law` | `{PS20}` |
| I | `wb:pshift:eq:coherent-shift-action` | `{PS28a}` |
| I | `wb:pshift:eq:covariance` | `{PS4}` |
| I | `wb:pshift:eq:cusp-actions-identical` | `{PS19}` |
| I | `wb:pshift:eq:cusp-cocycle` | `{PS21}` |
| I | `wb:pshift:eq:cusp-periods` | `{PS18}` |
| I | `wb:pshift:eq:cusp-translation` | `{PS22}` |
| I | `wb:pshift:eq:finite-class` | `{PS12}` |
| I | `wb:pshift:eq:finite-data` | `{PS3}` |
| I | `wb:pshift:eq:finite-equation` | `{PS10}` |
| I | `wb:pshift:eq:finite-middle-sections` | `{PS15}` |
| I | `wb:pshift:eq:finite-norm-obstruction` | `{PS11}` |
| I | `wb:pshift:eq:finite-overlap-identity` | `{PS28}` |
| I | `wb:pshift:eq:full-isomorphism` | `{PS27}` |
| I | `wb:pshift:eq:global-correction` | `{PS26}` |
| I | `wb:pshift:eq:integer-shear` | `{PS6}` |
| I | `wb:pshift:eq:local-affine-cocycle` | `{PS16}` |
| I | `wb:pshift:eq:local-corrections` | `{PS13}` |
| I | `wb:pshift:eq:local-matrix-identity` | `{PS14}` |
| I | `wb:pshift:eq:no-analytic-obstruction` | `{PS25}` |
| I | `wb:pshift:eq:norms` | `{PS9}` |
| I | `wb:pshift:eq:parameter-disc` | `{PS29}` |
| I | `wb:pshift:eq:period-morphism` | `{PS8}` |
| I | `wb:pshift:eq:periods` | `{PS1}` |
| I | `wb:pshift:eq:rank-one-map` | `{PS2}` |
| I | `wb:pshift:eq:vector-sheaf` | `{PS24}` |
| I | `wb:pshift:lem:centralizer` | `O.3` |
| I | `wb:pshift:sec:classification` | `O.9` |
| I | `wb:pshift:thm:classification` | `3.8` |
| I | `wb:record:h12-direct-images` | `N.7.1` |
| I | `wb:rem:bcpr-global-gauge-boundary` | `T.2` |
| I | `wb:rem:bcpr-literal-gauge` | `T.1` |
| I | `wb:sec:algebraic-dimension` | `J` |
| I | `wb:sec:bcpr-product-structure` | `O` |
| I | `wb:sec:candidate-geometry` | `B` |
| I | `wb:sec:canonical-ring-recovery` | `O.7` |
| I | `wb:sec:hodge-frolicher` | `N` |
| I | `wb:sec:retained-period-deformation` | `O.8` |
| I | `wb:thm:algebraic-dimension-audit` | `J.4` |
| I | `wb:thm:bcpr-square-zero-algebra` | `10.7` |
| I | `wb:thm:candidate-cusp-geometry` | `B.6` |
| I | `wb:thm:candidate-global-geometry` | `B.11` |
| I | `wb:thm:canonical-ring-recovery` | `O.1` |
| I | `wb:thm:coinvariants` | `C.3` |
| I | `wb:thm:cusp-lattices` | `C.2` |
| I | `wb:thm:exact-bott-chern-aeppli` | `10.3` |
| I | `wb:thm:frolicher-e2-candidate` | `10.1` |
| I | `wb:thm:h12-scalar` | `8.8` |
| I | `wb:thm:parametric-hodge-diamond` | `8.9` |
| I | `wb:thm:retained-period-deformation` | `O.2` |
| I | `wb:thm:structure-direct-images-audit` | `8.1` |
| II | `app:II:inv-E1.1-rederivation` | `A` |
| II | `app:II:known` | `A` |
| II | `app:II:programs` | `D` |
| II | `app:II:result-index` | `C` |
| II | `cdp:A:filtration1` | `1` |
| II | `cdp:A:filtration2` | `2` |
| II | `cdp:eq:A.1` | `{A.1}` |
| II | `cdp:eq:A.10` | `{A.10}` |
| II | `cdp:eq:A.11` | `{A.11}` |
| II | `cdp:eq:A.12` | `{A.12}` |
| II | `cdp:eq:A.13` | `{A.13}` |
| II | `cdp:eq:A.14` | `{A.14}` |
| II | `cdp:eq:A.15` | `{A.15}` |
| II | `cdp:eq:A.15a` | `{A.15a}` |
| II | `cdp:eq:A.15b` | `{A.15b}` |
| II | `cdp:eq:A.16` | `{A.16}` |
| II | `cdp:eq:A.17` | `{A.17}` |
| II | `cdp:eq:A.18` | `{A.18}` |
| II | `cdp:eq:A.19` | `{A.19}` |
| II | `cdp:eq:A.2` | `{A.2}` |
| II | `cdp:eq:A.20` | `{A.20}` |
| II | `cdp:eq:A.21` | `{A.21}` |
| II | `cdp:eq:A.22` | `{A.22}` |
| II | `cdp:eq:A.23` | `{A.23}` |
| II | `cdp:eq:A.24` | `{A.24}` |
| II | `cdp:eq:A.25` | `{A.25}` |
| II | `cdp:eq:A.26` | `{A.26}` |
| II | `cdp:eq:A.27` | `{A.27}` |
| II | `cdp:eq:A.28` | `{A.28}` |
| II | `cdp:eq:A.29` | `{A.29}` |
| II | `cdp:eq:A.3` | `{A.3}` |
| II | `cdp:eq:A.30` | `{A.30}` |
| II | `cdp:eq:A.4` | `{A.4}` |
| II | `cdp:eq:A.5` | `{A.5}` |
| II | `cdp:eq:A.6` | `{A.6}` |
| II | `cdp:eq:A.7` | `{A.7}` |
| II | `cdp:eq:A.8` | `{A.8}` |
| II | `cdp:eq:A.9` | `{A.9}` |
| II | `cdp:eq:A.9a` | `{A.9a}` |
| II | `cdp:eq:A.9b` | `{A.9b}` |
| II | `cdp:eq:A.BP.1` | `{A.BP.1}` |
| II | `cdp:eq:A.BP.10` | `{A.BP.10}` |
| II | `cdp:eq:A.BP.11` | `{A.BP.11}` |
| II | `cdp:eq:A.BP.12` | `{A.BP.12}` |
| II | `cdp:eq:A.BP.2` | `{A.BP.2}` |
| II | `cdp:eq:A.BP.3` | `{A.BP.3}` |
| II | `cdp:eq:A.BP.4` | `{A.BP.4}` |
| II | `cdp:eq:A.BP.5` | `{A.BP.5}` |
| II | `cdp:eq:A.BP.6` | `{A.BP.6}` |
| II | `cdp:eq:A.BP.7` | `{A.BP.7}` |
| II | `cdp:eq:A.BP.8` | `{A.BP.8}` |
| II | `cdp:eq:A.BP.9` | `{A.BP.9}` |
| II | `cdp:eq:A.CD.1` | `{A.CD.1}` |
| II | `cdp:eq:A.CD.2` | `{A.CD.2}` |
| II | `cdp:eq:A.CD.3` | `{A.CD.3}` |
| II | `cdp:eq:A.CD.4` | `{A.CD.4}` |
| II | `cdp:eq:A.J.1` | `{A.J.1}` |
| II | `cdp:eq:A.J.10` | `{A.J.10}` |
| II | `cdp:eq:A.J.11` | `{A.J.11}` |
| II | `cdp:eq:A.J.12` | `{A.J.12}` |
| II | `cdp:eq:A.J.13` | `{A.J.13}` |
| II | `cdp:eq:A.J.14` | `{A.J.14}` |
| II | `cdp:eq:A.J.15` | `{A.J.15}` |
| II | `cdp:eq:A.J.16` | `{A.J.16}` |
| II | `cdp:eq:A.J.17` | `{A.J.17}` |
| II | `cdp:eq:A.J.18` | `{A.J.18}` |
| II | `cdp:eq:A.J.19` | `{A.J.19}` |
| II | `cdp:eq:A.J.2` | `{A.J.2}` |
| II | `cdp:eq:A.J.20` | `{A.J.20}` |
| II | `cdp:eq:A.J.21` | `{A.J.21}` |
| II | `cdp:eq:A.J.22` | `{A.J.22}` |
| II | `cdp:eq:A.J.23` | `{A.J.23}` |
| II | `cdp:eq:A.J.24` | `{A.J.24}` |
| II | `cdp:eq:A.J.25` | `{A.J.25}` |
| II | `cdp:eq:A.J.26` | `{A.J.26}` |
| II | `cdp:eq:A.J.27` | `{A.J.27}` |
| II | `cdp:eq:A.J.28` | `{A.J.28}` |
| II | `cdp:eq:A.J.29` | `{A.J.29}` |
| II | `cdp:eq:A.J.3` | `{A.J.3}` |
| II | `cdp:eq:A.J.30` | `{A.J.30}` |
| II | `cdp:eq:A.J.31` | `{A.J.31}` |
| II | `cdp:eq:A.J.32` | `{A.J.32}` |
| II | `cdp:eq:A.J.33` | `{A.J.33}` |
| II | `cdp:eq:A.J.33a` | `{A.J.33a}` |
| II | `cdp:eq:A.J.33b` | `{A.J.33b}` |
| II | `cdp:eq:A.J.34` | `{A.J.34}` |
| II | `cdp:eq:A.J.35` | `{A.J.35}` |
| II | `cdp:eq:A.J.36` | `{A.J.36}` |
| II | `cdp:eq:A.J.37` | `{A.J.37}` |
| II | `cdp:eq:A.J.38` | `{A.J.38}` |
| II | `cdp:eq:A.J.38a` | `{A.J.38a}` |
| II | `cdp:eq:A.J.39` | `{A.J.39}` |
| II | `cdp:eq:A.J.4` | `{A.J.4}` |
| II | `cdp:eq:A.J.40` | `{A.J.40}` |
| II | `cdp:eq:A.J.5` | `{A.J.5}` |
| II | `cdp:eq:A.J.6` | `{A.J.6}` |
| II | `cdp:eq:A.J.7` | `{A.J.7}` |
| II | `cdp:eq:A.J.8` | `{A.J.8}` |
| II | `cdp:eq:A.J.9` | `{A.J.9}` |
| II | `cdp:eq:A.NL.1` | `{A.NL.1}` |
| II | `cdp:eq:A.NL.2` | `{A.NL.2}` |
| II | `cdp:eq:A.NL.3` | `{A.NL.3}` |
| II | `cdp:eq:A.NL.4` | `{A.NL.4}` |
| II | `cdp:eq:A.NL.5` | `{A.NL.5}` |
| II | `cdp:eq:A.Pi.1` | `{A.Pi.1}` |
| II | `cdp:eq:A.Pi.2` | `{A.Pi.2}` |
| II | `cdp:eq:A.Pi.3` | `{A.Pi.3}` |
| II | `cdp:eq:A.Pi.4` | `{A.Pi.4}` |
| II | `cdp:eq:A.Q1.1` | `{A.Q1.1}` |
| II | `cdp:eq:A.Q1.2` | `{A.Q1.2}` |
| II | `cdp:eq:A.RC.1` | `{A.RC.1}` |
| II | `cdp:eq:A.RC.2` | `{A.RC.2}` |
| II | `cdp:eq:A.RC.3` | `{A.RC.3}` |
| II | `cdp:eq:A.RC.4` | `{A.RC.4}` |
| II | `cdp:eq:A.RC.5` | `{A.RC.5}` |
| II | `cdp:eq:A.RC.6` | `{A.RC.6}` |
| II | `cdp:eq:A.RC.7` | `{A.RC.7}` |
| II | `cdp:eq:A.RT.1` | `{A.RT.1}` |
| II | `cdp:eq:A.RT.10` | `{A.RT.10}` |
| II | `cdp:eq:A.RT.11` | `{A.RT.11}` |
| II | `cdp:eq:A.RT.12` | `{A.RT.12}` |
| II | `cdp:eq:A.RT.13` | `{A.RT.13}` |
| II | `cdp:eq:A.RT.14` | `{A.RT.14}` |
| II | `cdp:eq:A.RT.15` | `{A.RT.15}` |
| II | `cdp:eq:A.RT.16` | `{A.RT.16}` |
| II | `cdp:eq:A.RT.17` | `{A.RT.17}` |
| II | `cdp:eq:A.RT.18` | `{A.RT.18}` |
| II | `cdp:eq:A.RT.19` | `{A.RT.19}` |
| II | `cdp:eq:A.RT.2` | `{A.RT.2}` |
| II | `cdp:eq:A.RT.20` | `{A.RT.20}` |
| II | `cdp:eq:A.RT.21` | `{A.RT.21}` |
| II | `cdp:eq:A.RT.3` | `{A.RT.3}` |
| II | `cdp:eq:A.RT.4` | `{A.RT.4}` |
| II | `cdp:eq:A.RT.5` | `{A.RT.5}` |
| II | `cdp:eq:A.RT.6` | `{A.RT.6}` |
| II | `cdp:eq:A.RT.7` | `{A.RT.7}` |
| II | `cdp:eq:A.RT.8` | `{A.RT.8}` |
| II | `cdp:eq:A.RT.9` | `{A.RT.9}` |
| II | `cdp:eq:A.T.1` | `{A.T.1}` |
| II | `cdp:eq:A.T.10` | `{A.T.10}` |
| II | `cdp:eq:A.T.11` | `{A.T.11}` |
| II | `cdp:eq:A.T.12` | `{A.T.12}` |
| II | `cdp:eq:A.T.13` | `{A.T.13}` |
| II | `cdp:eq:A.T.14` | `{A.T.14}` |
| II | `cdp:eq:A.T.15` | `{A.T.15}` |
| II | `cdp:eq:A.T.16` | `{A.T.16}` |
| II | `cdp:eq:A.T.17` | `{A.T.17}` |
| II | `cdp:eq:A.T.18` | `{A.T.18}` |
| II | `cdp:eq:A.T.19` | `{A.T.19}` |
| II | `cdp:eq:A.T.2` | `{A.T.2}` |
| II | `cdp:eq:A.T.20` | `{A.T.20}` |
| II | `cdp:eq:A.T.21` | `{A.T.21}` |
| II | `cdp:eq:A.T.22` | `{A.T.22}` |
| II | `cdp:eq:A.T.23` | `{A.T.23}` |
| II | `cdp:eq:A.T.3` | `{A.T.3}` |
| II | `cdp:eq:A.T.4` | `{A.T.4}` |
| II | `cdp:eq:A.T.5` | `{A.T.5}` |
| II | `cdp:eq:A.T.6` | `{A.T.6}` |
| II | `cdp:eq:A.T.7` | `{A.T.7}` |
| II | `cdp:eq:A.T.8` | `{A.T.8}` |
| II | `cdp:eq:A.T.9` | `{A.T.9}` |
| II | `cdp:eq:A.U.1` | `{A.U.1}` |
| II | `cdp:eq:A.U.2` | `{A.U.2}` |
| II | `cdp:eq:A.U.3` | `{A.U.3}` |
| II | `cdp:eq:A.U.4` | `{A.U.4}` |
| II | `cdp:eq:A.U.5` | `{A.U.5}` |
| II | `cdp:eq:A.U.6` | `{A.U.6}` |
| II | `cdp:eq:A.U.7` | `{A.U.7}` |
| II | `cdp:eq:B.1` | `{B.1}` |
| II | `cdp:eq:B.2` | `{B.2}` |
| II | `cdp:eq:B.3` | `{B.3}` |
| II | `cdp:eq:B.4` | `{B.4}` |
| II | `cdp:eq:B.5` | `{B.5}` |
| II | `cdp:eq:B.6` | `{B.6}` |
| II | `cdp:eq:B.7` | `{B.7}` |
| II | `cdp:eq:C.1` | `{C.1}` |
| II | `cdp:eq:C.10` | `{C.10}` |
| II | `cdp:eq:C.11` | `{C.11}` |
| II | `cdp:eq:C.12` | `{C.12}` |
| II | `cdp:eq:C.13` | `{C.13}` |
| II | `cdp:eq:C.14` | `{C.14}` |
| II | `cdp:eq:C.15` | `{C.15}` |
| II | `cdp:eq:C.16` | `{C.16}` |
| II | `cdp:eq:C.17` | `{C.17}` |
| II | `cdp:eq:C.18` | `{C.18}` |
| II | `cdp:eq:C.19` | `{C.19}` |
| II | `cdp:eq:C.2` | `{C.2}` |
| II | `cdp:eq:C.20` | `{C.20}` |
| II | `cdp:eq:C.21` | `{C.21}` |
| II | `cdp:eq:C.22` | `{C.22}` |
| II | `cdp:eq:C.22a` | `{C.22a}` |
| II | `cdp:eq:C.22b` | `{C.22b}` |
| II | `cdp:eq:C.3` | `{C.3}` |
| II | `cdp:eq:C.4` | `{C.4}` |
| II | `cdp:eq:C.5` | `{C.5}` |
| II | `cdp:eq:C.6` | `{C.6}` |
| II | `cdp:eq:C.7` | `{C.7}` |
| II | `cdp:eq:C.8` | `{C.8}` |
| II | `cdp:eq:C.9` | `{C.9}` |
| II | `cdp:eq:C.AD.1` | `{C.AD.1}` |
| II | `cdp:eq:C.AD.10` | `{C.AD.10}` |
| II | `cdp:eq:C.AD.11` | `{C.AD.11}` |
| II | `cdp:eq:C.AD.2` | `{C.AD.2}` |
| II | `cdp:eq:C.AD.3` | `{C.AD.3}` |
| II | `cdp:eq:C.AD.4` | `{C.AD.4}` |
| II | `cdp:eq:C.AD.5` | `{C.AD.5}` |
| II | `cdp:eq:C.AD.6` | `{C.AD.6}` |
| II | `cdp:eq:C.AD.7` | `{C.AD.7}` |
| II | `cdp:eq:C.AD.8` | `{C.AD.8}` |
| II | `cdp:eq:C.AD.9` | `{C.AD.9}` |
| II | `cdp:eq:C.AP.1` | `{C.AP.1}` |
| II | `cdp:eq:C.AP.10` | `{C.AP.10}` |
| II | `cdp:eq:C.AP.11` | `{C.AP.11}` |
| II | `cdp:eq:C.AP.12` | `{C.AP.12}` |
| II | `cdp:eq:C.AP.13` | `{C.AP.13}` |
| II | `cdp:eq:C.AP.14` | `{C.AP.14}` |
| II | `cdp:eq:C.AP.2` | `{C.AP.2}` |
| II | `cdp:eq:C.AP.3` | `{C.AP.3}` |
| II | `cdp:eq:C.AP.4` | `{C.AP.4}` |
| II | `cdp:eq:C.AP.5` | `{C.AP.5}` |
| II | `cdp:eq:C.AP.6` | `{C.AP.6}` |
| II | `cdp:eq:C.AP.7` | `{C.AP.7}` |
| II | `cdp:eq:C.AP.8` | `{C.AP.8}` |
| II | `cdp:eq:C.AP.9` | `{C.AP.9}` |
| II | `cdp:eq:C.AR.1` | `{C.AR.1}` |
| II | `cdp:eq:C.AR.10` | `{C.AR.10}` |
| II | `cdp:eq:C.AR.11` | `{C.AR.11}` |
| II | `cdp:eq:C.AR.12` | `{C.AR.12}` |
| II | `cdp:eq:C.AR.13` | `{C.AR.13}` |
| II | `cdp:eq:C.AR.14` | `{C.AR.14}` |
| II | `cdp:eq:C.AR.15` | `{C.AR.15}` |
| II | `cdp:eq:C.AR.16` | `{C.AR.16}` |
| II | `cdp:eq:C.AR.2` | `{C.AR.2}` |
| II | `cdp:eq:C.AR.3` | `{C.AR.3}` |
| II | `cdp:eq:C.AR.4` | `{C.AR.4}` |
| II | `cdp:eq:C.AR.5` | `{C.AR.5}` |
| II | `cdp:eq:C.AR.6` | `{C.AR.6}` |
| II | `cdp:eq:C.AR.7` | `{C.AR.7}` |
| II | `cdp:eq:C.AR.8` | `{C.AR.8}` |
| II | `cdp:eq:C.AR.9` | `{C.AR.9}` |
| II | `cdp:eq:C.AS.1` | `{C.AS.1}` |
| II | `cdp:eq:C.AS.10` | `{C.AS.10}` |
| II | `cdp:eq:C.AS.11` | `{C.AS.11}` |
| II | `cdp:eq:C.AS.12` | `{C.AS.12}` |
| II | `cdp:eq:C.AS.13` | `{C.AS.13}` |
| II | `cdp:eq:C.AS.14` | `{C.AS.14}` |
| II | `cdp:eq:C.AS.15` | `{C.AS.15}` |
| II | `cdp:eq:C.AS.16` | `{C.AS.16}` |
| II | `cdp:eq:C.AS.17` | `{C.AS.17}` |
| II | `cdp:eq:C.AS.18` | `{C.AS.18}` |
| II | `cdp:eq:C.AS.19` | `{C.AS.19}` |
| II | `cdp:eq:C.AS.2` | `{C.AS.2}` |
| II | `cdp:eq:C.AS.3` | `{C.AS.3}` |
| II | `cdp:eq:C.AS.4` | `{C.AS.4}` |
| II | `cdp:eq:C.AS.5` | `{C.AS.5}` |
| II | `cdp:eq:C.AS.6` | `{C.AS.6}` |
| II | `cdp:eq:C.AS.7` | `{C.AS.7}` |
| II | `cdp:eq:C.AS.8` | `{C.AS.8}` |
| II | `cdp:eq:C.AS.9` | `{C.AS.9}` |
| II | `cdp:eq:C.BC.1` | `{C.BC.1}` |
| II | `cdp:eq:C.BC.10` | `{C.BC.10}` |
| II | `cdp:eq:C.BC.11` | `{C.BC.11}` |
| II | `cdp:eq:C.BC.12` | `{C.BC.12}` |
| II | `cdp:eq:C.BC.13` | `{C.BC.13}` |
| II | `cdp:eq:C.BC.2` | `{C.BC.2}` |
| II | `cdp:eq:C.BC.3` | `{C.BC.3}` |
| II | `cdp:eq:C.BC.4` | `{C.BC.4}` |
| II | `cdp:eq:C.BC.5` | `{C.BC.5}` |
| II | `cdp:eq:C.BC.6` | `{C.BC.6}` |
| II | `cdp:eq:C.BC.7` | `{C.BC.7}` |
| II | `cdp:eq:C.BC.8` | `{C.BC.8}` |
| II | `cdp:eq:C.BC.9` | `{C.BC.9}` |
| II | `cdp:eq:C.CA.1` | `{C.CA.1}` |
| II | `cdp:eq:C.CA.10` | `{C.CA.10}` |
| II | `cdp:eq:C.CA.11` | `{C.CA.11}` |
| II | `cdp:eq:C.CA.2` | `{C.CA.2}` |
| II | `cdp:eq:C.CA.3` | `{C.CA.3}` |
| II | `cdp:eq:C.CA.4` | `{C.CA.4}` |
| II | `cdp:eq:C.CA.5` | `{C.CA.5}` |
| II | `cdp:eq:C.CA.6` | `{C.CA.6}` |
| II | `cdp:eq:C.CA.7` | `{C.CA.7}` |
| II | `cdp:eq:C.CA.8` | `{C.CA.8}` |
| II | `cdp:eq:C.CA.9` | `{C.CA.9}` |
| II | `cdp:eq:C.CF.1` | `{C.CF.1}` |
| II | `cdp:eq:C.CF.2` | `{C.CF.2}` |
| II | `cdp:eq:C.CF.3` | `{C.CF.3}` |
| II | `cdp:eq:C.CF.4` | `{C.CF.4}` |
| II | `cdp:eq:C.CF.5` | `{C.CF.5}` |
| II | `cdp:eq:C.CF.6` | `{C.CF.6}` |
| II | `cdp:eq:C.CF.7` | `{C.CF.7}` |
| II | `cdp:eq:C.CF.8` | `{C.CF.8}` |
| II | `cdp:eq:C.CF.9` | `{C.CF.9}` |
| II | `cdp:eq:C.CL.1` | `{C.CL.1}` |
| II | `cdp:eq:C.CL.10` | `{C.CL.10}` |
| II | `cdp:eq:C.CL.11` | `{C.CL.11}` |
| II | `cdp:eq:C.CL.12` | `{C.CL.12}` |
| II | `cdp:eq:C.CL.13` | `{C.CL.13}` |
| II | `cdp:eq:C.CL.2` | `{C.CL.2}` |
| II | `cdp:eq:C.CL.3` | `{C.CL.3}` |
| II | `cdp:eq:C.CL.4` | `{C.CL.4}` |
| II | `cdp:eq:C.CL.5` | `{C.CL.5}` |
| II | `cdp:eq:C.CL.6` | `{C.CL.6}` |
| II | `cdp:eq:C.CL.7` | `{C.CL.7}` |
| II | `cdp:eq:C.CL.8` | `{C.CL.8}` |
| II | `cdp:eq:C.CL.9` | `{C.CL.9}` |
| II | `cdp:eq:C.CP.1` | `{C.CP.1}` |
| II | `cdp:eq:C.CP.10` | `{C.CP.10}` |
| II | `cdp:eq:C.CP.2` | `{C.CP.2}` |
| II | `cdp:eq:C.CP.3` | `{C.CP.3}` |
| II | `cdp:eq:C.CP.4` | `{C.CP.4}` |
| II | `cdp:eq:C.CP.5` | `{C.CP.5}` |
| II | `cdp:eq:C.CP.6` | `{C.CP.6}` |
| II | `cdp:eq:C.CP.7` | `{C.CP.7}` |
| II | `cdp:eq:C.CP.8` | `{C.CP.8}` |
| II | `cdp:eq:C.CP.9` | `{C.CP.9}` |
| II | `cdp:eq:C.CQ.1` | `{C.CQ.1}` |
| II | `cdp:eq:C.CQ.10` | `{C.CQ.10}` |
| II | `cdp:eq:C.CQ.11` | `{C.CQ.11}` |
| II | `cdp:eq:C.CQ.12` | `{C.CQ.12}` |
| II | `cdp:eq:C.CQ.2` | `{C.CQ.2}` |
| II | `cdp:eq:C.CQ.3` | `{C.CQ.3}` |
| II | `cdp:eq:C.CQ.4` | `{C.CQ.4}` |
| II | `cdp:eq:C.CQ.5` | `{C.CQ.5}` |
| II | `cdp:eq:C.CQ.6` | `{C.CQ.6}` |
| II | `cdp:eq:C.CQ.7` | `{C.CQ.7}` |
| II | `cdp:eq:C.CQ.8` | `{C.CQ.8}` |
| II | `cdp:eq:C.CQ.9` | `{C.CQ.9}` |
| II | `cdp:eq:C.CR.1` | `{C.CR.1}` |
| II | `cdp:eq:C.CR.10` | `{C.CR.10}` |
| II | `cdp:eq:C.CR.11` | `{C.CR.11}` |
| II | `cdp:eq:C.CR.12` | `{C.CR.12}` |
| II | `cdp:eq:C.CR.13` | `{C.CR.13}` |
| II | `cdp:eq:C.CR.14` | `{C.CR.14}` |
| II | `cdp:eq:C.CR.15` | `{C.CR.15}` |
| II | `cdp:eq:C.CR.16` | `{C.CR.16}` |
| II | `cdp:eq:C.CR.17` | `{C.CR.17}` |
| II | `cdp:eq:C.CR.18` | `{C.CR.18}` |
| II | `cdp:eq:C.CR.19` | `{C.CR.19}` |
| II | `cdp:eq:C.CR.2` | `{C.CR.2}` |
| II | `cdp:eq:C.CR.20` | `{C.CR.20}` |
| II | `cdp:eq:C.CR.21` | `{C.CR.21}` |
| II | `cdp:eq:C.CR.22` | `{C.CR.22}` |
| II | `cdp:eq:C.CR.3` | `{C.CR.3}` |
| II | `cdp:eq:C.CR.4` | `{C.CR.4}` |
| II | `cdp:eq:C.CR.5` | `{C.CR.5}` |
| II | `cdp:eq:C.CR.6` | `{C.CR.6}` |
| II | `cdp:eq:C.CR.7` | `{C.CR.7}` |
| II | `cdp:eq:C.CR.8` | `{C.CR.8}` |
| II | `cdp:eq:C.CR.9` | `{C.CR.9}` |
| II | `cdp:eq:C.CS.1` | `{C.CS.1}` |
| II | `cdp:eq:C.CS.2` | `{C.CS.2}` |
| II | `cdp:eq:C.CS.3` | `{C.CS.3}` |
| II | `cdp:eq:C.CS.4` | `{C.CS.4}` |
| II | `cdp:eq:C.CS.5` | `{C.CS.5}` |
| II | `cdp:eq:C.CS.6` | `{C.CS.6}` |
| II | `cdp:eq:C.CZ.1` | `{C.CZ.1}` |
| II | `cdp:eq:C.CZ.10` | `{C.CZ.10}` |
| II | `cdp:eq:C.CZ.11` | `{C.CZ.11}` |
| II | `cdp:eq:C.CZ.12` | `{C.CZ.12}` |
| II | `cdp:eq:C.CZ.13` | `{C.CZ.13}` |
| II | `cdp:eq:C.CZ.14` | `{C.CZ.14}` |
| II | `cdp:eq:C.CZ.2` | `{C.CZ.2}` |
| II | `cdp:eq:C.CZ.3` | `{C.CZ.3}` |
| II | `cdp:eq:C.CZ.4` | `{C.CZ.4}` |
| II | `cdp:eq:C.CZ.5` | `{C.CZ.5}` |
| II | `cdp:eq:C.CZ.6` | `{C.CZ.6}` |
| II | `cdp:eq:C.CZ.7` | `{C.CZ.7}` |
| II | `cdp:eq:C.CZ.8` | `{C.CZ.8}` |
| II | `cdp:eq:C.CZ.9` | `{C.CZ.9}` |
| II | `cdp:eq:C.D4.1` | `{C.D4.1}` |
| II | `cdp:eq:C.D4.10` | `{C.D4.10}` |
| II | `cdp:eq:C.D4.11` | `{C.D4.11}` |
| II | `cdp:eq:C.D4.12` | `{C.D4.12}` |
| II | `cdp:eq:C.D4.13` | `{C.D4.13}` |
| II | `cdp:eq:C.D4.14` | `{C.D4.14}` |
| II | `cdp:eq:C.D4.15` | `{C.D4.15}` |
| II | `cdp:eq:C.D4.16` | `{C.D4.16}` |
| II | `cdp:eq:C.D4.17` | `{C.D4.17}` |
| II | `cdp:eq:C.D4.18` | `{C.D4.18}` |
| II | `cdp:eq:C.D4.19` | `{C.D4.19}` |
| II | `cdp:eq:C.D4.2` | `{C.D4.2}` |
| II | `cdp:eq:C.D4.20` | `{C.D4.20}` |
| II | `cdp:eq:C.D4.3` | `{C.D4.3}` |
| II | `cdp:eq:C.D4.4` | `{C.D4.4}` |
| II | `cdp:eq:C.D4.5` | `{C.D4.5}` |
| II | `cdp:eq:C.D4.6` | `{C.D4.6}` |
| II | `cdp:eq:C.D4.7` | `{C.D4.7}` |
| II | `cdp:eq:C.D4.8` | `{C.D4.8}` |
| II | `cdp:eq:C.D4.9` | `{C.D4.9}` |
| II | `cdp:eq:C.DD.1` | `{C.DD.1}` |
| II | `cdp:eq:C.DD.10` | `{C.DD.10}` |
| II | `cdp:eq:C.DD.11` | `{C.DD.11}` |
| II | `cdp:eq:C.DD.12` | `{C.DD.12}` |
| II | `cdp:eq:C.DD.13` | `{C.DD.13}` |
| II | `cdp:eq:C.DD.14` | `{C.DD.14}` |
| II | `cdp:eq:C.DD.15` | `{C.DD.15}` |
| II | `cdp:eq:C.DD.16` | `{C.DD.16}` |
| II | `cdp:eq:C.DD.17` | `{C.DD.17}` |
| II | `cdp:eq:C.DD.18` | `{C.DD.18}` |
| II | `cdp:eq:C.DD.19` | `{C.DD.19}` |
| II | `cdp:eq:C.DD.2` | `{C.DD.2}` |
| II | `cdp:eq:C.DD.20` | `{C.DD.20}` |
| II | `cdp:eq:C.DD.21` | `{C.DD.21}` |
| II | `cdp:eq:C.DD.3` | `{C.DD.3}` |
| II | `cdp:eq:C.DD.4` | `{C.DD.4}` |
| II | `cdp:eq:C.DD.5` | `{C.DD.5}` |
| II | `cdp:eq:C.DD.6` | `{C.DD.6}` |
| II | `cdp:eq:C.DD.7` | `{C.DD.7}` |
| II | `cdp:eq:C.DD.8` | `{C.DD.8}` |
| II | `cdp:eq:C.DD.9` | `{C.DD.9}` |
| II | `cdp:eq:C.DH.1` | `{C.DH.1}` |
| II | `cdp:eq:C.DH.10` | `{C.DH.10}` |
| II | `cdp:eq:C.DH.11` | `{C.DH.11}` |
| II | `cdp:eq:C.DH.12` | `{C.DH.12}` |
| II | `cdp:eq:C.DH.13` | `{C.DH.13}` |
| II | `cdp:eq:C.DH.14` | `{C.DH.14}` |
| II | `cdp:eq:C.DH.14a` | `{C.DH.14a}` |
| II | `cdp:eq:C.DH.14b` | `{C.DH.14b}` |
| II | `cdp:eq:C.DH.15` | `{C.DH.15}` |
| II | `cdp:eq:C.DH.16` | `{C.DH.16}` |
| II | `cdp:eq:C.DH.2` | `{C.DH.2}` |
| II | `cdp:eq:C.DH.3` | `{C.DH.3}` |
| II | `cdp:eq:C.DH.4` | `{C.DH.4}` |
| II | `cdp:eq:C.DH.5` | `{C.DH.5}` |
| II | `cdp:eq:C.DH.6` | `{C.DH.6}` |
| II | `cdp:eq:C.DH.7` | `{C.DH.7}` |
| II | `cdp:eq:C.DH.8` | `{C.DH.8}` |
| II | `cdp:eq:C.DH.9` | `{C.DH.9}` |
| II | `cdp:eq:C.EC.1` | `{C.EC.1}` |
| II | `cdp:eq:C.EC.2` | `{C.EC.2}` |
| II | `cdp:eq:C.EH.1` | `{C.EH.1}` |
| II | `cdp:eq:C.EH.2` | `{C.EH.2}` |
| II | `cdp:eq:C.EH.3` | `{C.EH.3}` |
| II | `cdp:eq:C.EH.4` | `{C.EH.4}` |
| II | `cdp:eq:C.EH.5` | `{C.EH.5}` |
| II | `cdp:eq:C.EH.6` | `{C.EH.6}` |
| II | `cdp:eq:C.EH.7` | `{C.EH.7}` |
| II | `cdp:eq:C.EH.8` | `{C.EH.8}` |
| II | `cdp:eq:C.EL.1` | `{C.EL.1}` |
| II | `cdp:eq:C.EL.10` | `{C.EL.10}` |
| II | `cdp:eq:C.EL.11` | `{C.EL.11}` |
| II | `cdp:eq:C.EL.2` | `{C.EL.2}` |
| II | `cdp:eq:C.EL.3` | `{C.EL.3}` |
| II | `cdp:eq:C.EL.4` | `{C.EL.4}` |
| II | `cdp:eq:C.EL.5` | `{C.EL.5}` |
| II | `cdp:eq:C.EL.6` | `{C.EL.6}` |
| II | `cdp:eq:C.EL.7` | `{C.EL.7}` |
| II | `cdp:eq:C.EL.8` | `{C.EL.8}` |
| II | `cdp:eq:C.EL.9` | `{C.EL.9}` |
| II | `cdp:eq:C.EN.1` | `{C.EN.1}` |
| II | `cdp:eq:C.EN.10` | `{C.EN.10}` |
| II | `cdp:eq:C.EN.11` | `{C.EN.11}` |
| II | `cdp:eq:C.EN.12` | `{C.EN.12}` |
| II | `cdp:eq:C.EN.13` | `{C.EN.13}` |
| II | `cdp:eq:C.EN.14` | `{C.EN.14}` |
| II | `cdp:eq:C.EN.15` | `{C.EN.15}` |
| II | `cdp:eq:C.EN.16` | `{C.EN.16}` |
| II | `cdp:eq:C.EN.17` | `{C.EN.17}` |
| II | `cdp:eq:C.EN.18` | `{C.EN.18}` |
| II | `cdp:eq:C.EN.2` | `{C.EN.2}` |
| II | `cdp:eq:C.EN.3` | `{C.EN.3}` |
| II | `cdp:eq:C.EN.4` | `{C.EN.4}` |
| II | `cdp:eq:C.EN.5` | `{C.EN.5}` |
| II | `cdp:eq:C.EN.6` | `{C.EN.6}` |
| II | `cdp:eq:C.EN.7` | `{C.EN.7}` |
| II | `cdp:eq:C.EN.8` | `{C.EN.8}` |
| II | `cdp:eq:C.EN.9` | `{C.EN.9}` |
| II | `cdp:eq:C.EN.G1` | `{C.EN.G1}` |
| II | `cdp:eq:C.EN.G2` | `{C.EN.G2}` |
| II | `cdp:eq:C.EN.G3` | `{C.EN.G3}` |
| II | `cdp:eq:C.EN.G4` | `{C.EN.G4}` |
| II | `cdp:eq:C.EN.R1` | `{C.EN.R1}` |
| II | `cdp:eq:C.EN.R10` | `{C.EN.R10}` |
| II | `cdp:eq:C.EN.R11` | `{C.EN.R11}` |
| II | `cdp:eq:C.EN.R12` | `{C.EN.R12}` |
| II | `cdp:eq:C.EN.R2` | `{C.EN.R2}` |
| II | `cdp:eq:C.EN.R3` | `{C.EN.R3}` |
| II | `cdp:eq:C.EN.R4` | `{C.EN.R4}` |
| II | `cdp:eq:C.EN.R5` | `{C.EN.R5}` |
| II | `cdp:eq:C.EN.R6` | `{C.EN.R6}` |
| II | `cdp:eq:C.EN.R7` | `{C.EN.R7}` |
| II | `cdp:eq:C.EN.R8` | `{C.EN.R8}` |
| II | `cdp:eq:C.EN.R9` | `{C.EN.R9}` |
| II | `cdp:eq:C.EN.S1` | `{C.EN.S1}` |
| II | `cdp:eq:C.EN.S2` | `{C.EN.S2}` |
| II | `cdp:eq:C.EN.S3` | `{C.EN.S3}` |
| II | `cdp:eq:C.EN.S4` | `{C.EN.S4}` |
| II | `cdp:eq:C.EN.S5` | `{C.EN.S5}` |
| II | `cdp:eq:C.EN.S6` | `{C.EN.S6}` |
| II | `cdp:eq:C.EN.S7` | `{C.EN.S7}` |
| II | `cdp:eq:C.EO.1` | `{C.EO.1}` |
| II | `cdp:eq:C.EO.10` | `{C.EO.10}` |
| II | `cdp:eq:C.EO.11` | `{C.EO.11}` |
| II | `cdp:eq:C.EO.12` | `{C.EO.12}` |
| II | `cdp:eq:C.EO.13` | `{C.EO.13}` |
| II | `cdp:eq:C.EO.14` | `{C.EO.14}` |
| II | `cdp:eq:C.EO.15` | `{C.EO.15}` |
| II | `cdp:eq:C.EO.16` | `{C.EO.16}` |
| II | `cdp:eq:C.EO.2` | `{C.EO.2}` |
| II | `cdp:eq:C.EO.3` | `{C.EO.3}` |
| II | `cdp:eq:C.EO.4` | `{C.EO.4}` |
| II | `cdp:eq:C.EO.5` | `{C.EO.5}` |
| II | `cdp:eq:C.EO.6` | `{C.EO.6}` |
| II | `cdp:eq:C.EO.7` | `{C.EO.7}` |
| II | `cdp:eq:C.EO.8` | `{C.EO.8}` |
| II | `cdp:eq:C.EO.9` | `{C.EO.9}` |
| II | `cdp:eq:C.EO.H1` | `{C.EO.H1}` |
| II | `cdp:eq:C.EO.H2` | `{C.EO.H2}` |
| II | `cdp:eq:C.EO.H3` | `{C.EO.H3}` |
| II | `cdp:eq:C.EO.H4` | `{C.EO.H4}` |
| II | `cdp:eq:C.EO.H5` | `{C.EO.H5}` |
| II | `cdp:eq:C.EO.H6` | `{C.EO.H6}` |
| II | `cdp:eq:C.EO.H7` | `{C.EO.H7}` |
| II | `cdp:eq:C.EP.1` | `{C.EP.1}` |
| II | `cdp:eq:C.EP.10` | `{C.EP.10}` |
| II | `cdp:eq:C.EP.11` | `{C.EP.11}` |
| II | `cdp:eq:C.EP.2` | `{C.EP.2}` |
| II | `cdp:eq:C.EP.3` | `{C.EP.3}` |
| II | `cdp:eq:C.EP.4` | `{C.EP.4}` |
| II | `cdp:eq:C.EP.5` | `{C.EP.5}` |
| II | `cdp:eq:C.EP.6` | `{C.EP.6}` |
| II | `cdp:eq:C.EP.7` | `{C.EP.7}` |
| II | `cdp:eq:C.EP.8` | `{C.EP.8}` |
| II | `cdp:eq:C.EP.9` | `{C.EP.9}` |
| II | `cdp:eq:C.EQ.1` | `{C.EQ.1}` |
| II | `cdp:eq:C.EQ.10` | `{C.EQ.10}` |
| II | `cdp:eq:C.EQ.11` | `{C.EQ.11}` |
| II | `cdp:eq:C.EQ.2` | `{C.EQ.2}` |
| II | `cdp:eq:C.EQ.3` | `{C.EQ.3}` |
| II | `cdp:eq:C.EQ.4` | `{C.EQ.4}` |
| II | `cdp:eq:C.EQ.5` | `{C.EQ.5}` |
| II | `cdp:eq:C.EQ.6` | `{C.EQ.6}` |
| II | `cdp:eq:C.EQ.7` | `{C.EQ.7}` |
| II | `cdp:eq:C.EQ.8` | `{C.EQ.8}` |
| II | `cdp:eq:C.EQ.9` | `{C.EQ.9}` |
| II | `cdp:eq:C.ER.1` | `{C.ER.1}` |
| II | `cdp:eq:C.ER.10` | `{C.ER.10}` |
| II | `cdp:eq:C.ER.11` | `{C.ER.11}` |
| II | `cdp:eq:C.ER.12` | `{C.ER.12}` |
| II | `cdp:eq:C.ER.13` | `{C.ER.13}` |
| II | `cdp:eq:C.ER.14` | `{C.ER.14}` |
| II | `cdp:eq:C.ER.15` | `{C.ER.15}` |
| II | `cdp:eq:C.ER.16` | `{C.ER.16}` |
| II | `cdp:eq:C.ER.17` | `{C.ER.17}` |
| II | `cdp:eq:C.ER.18` | `{C.ER.18}` |
| II | `cdp:eq:C.ER.2` | `{C.ER.2}` |
| II | `cdp:eq:C.ER.3` | `{C.ER.3}` |
| II | `cdp:eq:C.ER.4` | `{C.ER.4}` |
| II | `cdp:eq:C.ER.5` | `{C.ER.5}` |
| II | `cdp:eq:C.ER.6` | `{C.ER.6}` |
| II | `cdp:eq:C.ER.7` | `{C.ER.7}` |
| II | `cdp:eq:C.ER.8` | `{C.ER.8}` |
| II | `cdp:eq:C.ER.9` | `{C.ER.9}` |
| II | `cdp:eq:C.ET.1` | `{C.ET.1}` |
| II | `cdp:eq:C.ET.10` | `{C.ET.10}` |
| II | `cdp:eq:C.ET.11` | `{C.ET.11}` |
| II | `cdp:eq:C.ET.12` | `{C.ET.12}` |
| II | `cdp:eq:C.ET.2` | `{C.ET.2}` |
| II | `cdp:eq:C.ET.3` | `{C.ET.3}` |
| II | `cdp:eq:C.ET.4` | `{C.ET.4}` |
| II | `cdp:eq:C.ET.5` | `{C.ET.5}` |
| II | `cdp:eq:C.ET.6` | `{C.ET.6}` |
| II | `cdp:eq:C.ET.7` | `{C.ET.7}` |
| II | `cdp:eq:C.ET.8` | `{C.ET.8}` |
| II | `cdp:eq:C.ET.9` | `{C.ET.9}` |
| II | `cdp:eq:C.EW.1` | `{C.EW.1}` |
| II | `cdp:eq:C.EW.10` | `{C.EW.10}` |
| II | `cdp:eq:C.EW.11` | `{C.EW.11}` |
| II | `cdp:eq:C.EW.12` | `{C.EW.12}` |
| II | `cdp:eq:C.EW.13` | `{C.EW.13}` |
| II | `cdp:eq:C.EW.14` | `{C.EW.14}` |
| II | `cdp:eq:C.EW.15` | `{C.EW.15}` |
| II | `cdp:eq:C.EW.16` | `{C.EW.16}` |
| II | `cdp:eq:C.EW.17` | `{C.EW.17}` |
| II | `cdp:eq:C.EW.18` | `{C.EW.18}` |
| II | `cdp:eq:C.EW.19` | `{C.EW.19}` |
| II | `cdp:eq:C.EW.2` | `{C.EW.2}` |
| II | `cdp:eq:C.EW.20` | `{C.EW.20}` |
| II | `cdp:eq:C.EW.21` | `{C.EW.21}` |
| II | `cdp:eq:C.EW.3` | `{C.EW.3}` |
| II | `cdp:eq:C.EW.4` | `{C.EW.4}` |
| II | `cdp:eq:C.EW.5` | `{C.EW.5}` |
| II | `cdp:eq:C.EW.6` | `{C.EW.6}` |
| II | `cdp:eq:C.EW.7` | `{C.EW.7}` |
| II | `cdp:eq:C.EW.8` | `{C.EW.8}` |
| II | `cdp:eq:C.EW.9` | `{C.EW.9}` |
| II | `cdp:eq:C.FD.1` | `{C.FD.1}` |
| II | `cdp:eq:C.FD.2` | `{C.FD.2}` |
| II | `cdp:eq:C.FD.3` | `{C.FD.3}` |
| II | `cdp:eq:C.FD.4` | `{C.FD.4}` |
| II | `cdp:eq:C.FD.5` | `{C.FD.5}` |
| II | `cdp:eq:C.FD.6` | `{C.FD.6}` |
| II | `cdp:eq:C.FG.1` | `{C.FG.1}` |
| II | `cdp:eq:C.FG.10` | `{C.FG.10}` |
| II | `cdp:eq:C.FG.11` | `{C.FG.11}` |
| II | `cdp:eq:C.FG.12` | `{C.FG.12}` |
| II | `cdp:eq:C.FG.13` | `{C.FG.13}` |
| II | `cdp:eq:C.FG.14` | `{C.FG.14}` |
| II | `cdp:eq:C.FG.15` | `{C.FG.15}` |
| II | `cdp:eq:C.FG.16` | `{C.FG.16}` |
| II | `cdp:eq:C.FG.17` | `{C.FG.17}` |
| II | `cdp:eq:C.FG.18` | `{C.FG.18}` |
| II | `cdp:eq:C.FG.19` | `{C.FG.19}` |
| II | `cdp:eq:C.FG.2` | `{C.FG.2}` |
| II | `cdp:eq:C.FG.3` | `{C.FG.3}` |
| II | `cdp:eq:C.FG.4` | `{C.FG.4}` |
| II | `cdp:eq:C.FG.5` | `{C.FG.5}` |
| II | `cdp:eq:C.FG.6` | `{C.FG.6}` |
| II | `cdp:eq:C.FG.7` | `{C.FG.7}` |
| II | `cdp:eq:C.FG.8` | `{C.FG.8}` |
| II | `cdp:eq:C.FG.9` | `{C.FG.9}` |
| II | `cdp:eq:C.FL.1` | `{C.FL.1}` |
| II | `cdp:eq:C.FL.2` | `{C.FL.2}` |
| II | `cdp:eq:C.FL.3` | `{C.FL.3}` |
| II | `cdp:eq:C.FL.4` | `{C.FL.4}` |
| II | `cdp:eq:C.FL.5` | `{C.FL.5}` |
| II | `cdp:eq:C.G.1` | `{C.G.1}` |
| II | `cdp:eq:C.G.2` | `{C.G.2}` |
| II | `cdp:eq:C.GP.1` | `{C.GP.1}` |
| II | `cdp:eq:C.GP.10` | `{C.GP.10}` |
| II | `cdp:eq:C.GP.2` | `{C.GP.2}` |
| II | `cdp:eq:C.GP.3` | `{C.GP.3}` |
| II | `cdp:eq:C.GP.4` | `{C.GP.4}` |
| II | `cdp:eq:C.GP.5` | `{C.GP.5}` |
| II | `cdp:eq:C.GP.6` | `{C.GP.6}` |
| II | `cdp:eq:C.GP.7` | `{C.GP.7}` |
| II | `cdp:eq:C.GP.8` | `{C.GP.8}` |
| II | `cdp:eq:C.GP.9` | `{C.GP.9}` |
| II | `cdp:eq:C.H.1` | `{C.H.1}` |
| II | `cdp:eq:C.HA.1` | `{C.HA.1}` |
| II | `cdp:eq:C.HA.2` | `{C.HA.2}` |
| II | `cdp:eq:C.HA.3` | `{C.HA.3}` |
| II | `cdp:eq:C.HA.4` | `{C.HA.4}` |
| II | `cdp:eq:C.HA.5` | `{C.HA.5}` |
| II | `cdp:eq:C.HA.6` | `{C.HA.6}` |
| II | `cdp:eq:C.HB.1` | `{C.HB.1}` |
| II | `cdp:eq:C.HB.2` | `{C.HB.2}` |
| II | `cdp:eq:C.HB.3` | `{C.HB.3}` |
| II | `cdp:eq:C.HB.4` | `{C.HB.4}` |
| II | `cdp:eq:C.HB.5` | `{C.HB.5}` |
| II | `cdp:eq:C.HB.6` | `{C.HB.6}` |
| II | `cdp:eq:C.HB.7` | `{C.HB.7}` |
| II | `cdp:eq:C.HB.8` | `{C.HB.8}` |
| II | `cdp:eq:C.HB.9` | `{C.HB.9}` |
| II | `cdp:eq:C.HC.1` | `{C.HC.1}` |
| II | `cdp:eq:C.HC.10` | `{C.HC.10}` |
| II | `cdp:eq:C.HC.11` | `{C.HC.11}` |
| II | `cdp:eq:C.HC.2` | `{C.HC.2}` |
| II | `cdp:eq:C.HC.3` | `{C.HC.3}` |
| II | `cdp:eq:C.HC.4` | `{C.HC.4}` |
| II | `cdp:eq:C.HC.5` | `{C.HC.5}` |
| II | `cdp:eq:C.HC.6` | `{C.HC.6}` |
| II | `cdp:eq:C.HC.7` | `{C.HC.7}` |
| II | `cdp:eq:C.HC.8` | `{C.HC.8}` |
| II | `cdp:eq:C.HC.9` | `{C.HC.9}` |
| II | `cdp:eq:C.HG.1` | `{C.HG.1}` |
| II | `cdp:eq:C.HG.10` | `{C.HG.10}` |
| II | `cdp:eq:C.HG.11` | `{C.HG.11}` |
| II | `cdp:eq:C.HG.12` | `{C.HG.12}` |
| II | `cdp:eq:C.HG.13` | `{C.HG.13}` |
| II | `cdp:eq:C.HG.14` | `{C.HG.14}` |
| II | `cdp:eq:C.HG.15` | `{C.HG.15}` |
| II | `cdp:eq:C.HG.16` | `{C.HG.16}` |
| II | `cdp:eq:C.HG.17` | `{C.HG.17}` |
| II | `cdp:eq:C.HG.2` | `{C.HG.2}` |
| II | `cdp:eq:C.HG.3` | `{C.HG.3}` |
| II | `cdp:eq:C.HG.4` | `{C.HG.4}` |
| II | `cdp:eq:C.HG.5` | `{C.HG.5}` |
| II | `cdp:eq:C.HG.6` | `{C.HG.6}` |
| II | `cdp:eq:C.HG.7` | `{C.HG.7}` |
| II | `cdp:eq:C.HG.8` | `{C.HG.8}` |
| II | `cdp:eq:C.HG.9` | `{C.HG.9}` |
| II | `cdp:eq:C.HM.1` | `{C.HM.1}` |
| II | `cdp:eq:C.HM.10` | `{C.HM.10}` |
| II | `cdp:eq:C.HM.2` | `{C.HM.2}` |
| II | `cdp:eq:C.HM.3` | `{C.HM.3}` |
| II | `cdp:eq:C.HM.4` | `{C.HM.4}` |
| II | `cdp:eq:C.HM.5` | `{C.HM.5}` |
| II | `cdp:eq:C.HM.6` | `{C.HM.6}` |
| II | `cdp:eq:C.HM.7` | `{C.HM.7}` |
| II | `cdp:eq:C.HM.8` | `{C.HM.8}` |
| II | `cdp:eq:C.HM.9` | `{C.HM.9}` |
| II | `cdp:eq:C.HQ.1` | `{C.HQ.1}` |
| II | `cdp:eq:C.HQ.10` | `{C.HQ.10}` |
| II | `cdp:eq:C.HQ.2` | `{C.HQ.2}` |
| II | `cdp:eq:C.HQ.3` | `{C.HQ.3}` |
| II | `cdp:eq:C.HQ.4` | `{C.HQ.4}` |
| II | `cdp:eq:C.HQ.5` | `{C.HQ.5}` |
| II | `cdp:eq:C.HQ.6` | `{C.HQ.6}` |
| II | `cdp:eq:C.HQ.7` | `{C.HQ.7}` |
| II | `cdp:eq:C.HQ.8` | `{C.HQ.8}` |
| II | `cdp:eq:C.HQ.9` | `{C.HQ.9}` |
| II | `cdp:eq:C.HR.1` | `{C.HR.1}` |
| II | `cdp:eq:C.HR.2` | `{C.HR.2}` |
| II | `cdp:eq:C.HR.3` | `{C.HR.3}` |
| II | `cdp:eq:C.HR.4` | `{C.HR.4}` |
| II | `cdp:eq:C.HR.5` | `{C.HR.5}` |
| II | `cdp:eq:C.HR.6` | `{C.HR.6}` |
| II | `cdp:eq:C.HR.7` | `{C.HR.7}` |
| II | `cdp:eq:C.HR.8` | `{C.HR.8}` |
| II | `cdp:eq:C.HT.1` | `{C.HT.1}` |
| II | `cdp:eq:C.HT.10` | `{C.HT.10}` |
| II | `cdp:eq:C.HT.11` | `{C.HT.11}` |
| II | `cdp:eq:C.HT.12` | `{C.HT.12}` |
| II | `cdp:eq:C.HT.2` | `{C.HT.2}` |
| II | `cdp:eq:C.HT.3` | `{C.HT.3}` |
| II | `cdp:eq:C.HT.4` | `{C.HT.4}` |
| II | `cdp:eq:C.HT.5` | `{C.HT.5}` |
| II | `cdp:eq:C.HT.6` | `{C.HT.6}` |
| II | `cdp:eq:C.HT.7` | `{C.HT.7}` |
| II | `cdp:eq:C.HT.8` | `{C.HT.8}` |
| II | `cdp:eq:C.HT.9` | `{C.HT.9}` |
| II | `cdp:eq:C.IN.1` | `{C.IN.1}` |
| II | `cdp:eq:C.IN.2` | `{C.IN.2}` |
| II | `cdp:eq:C.IN.3` | `{C.IN.3}` |
| II | `cdp:eq:C.IN.4` | `{C.IN.4}` |
| II | `cdp:eq:C.IN.5` | `{C.IN.5}` |
| II | `cdp:eq:C.IN.6` | `{C.IN.6}` |
| II | `cdp:eq:C.INT.1` | `{C.INT.1}` |
| II | `cdp:eq:C.INT.10` | `{C.INT.10}` |
| II | `cdp:eq:C.INT.11` | `{C.INT.11}` |
| II | `cdp:eq:C.INT.12` | `{C.INT.12}` |
| II | `cdp:eq:C.INT.13` | `{C.INT.13}` |
| II | `cdp:eq:C.INT.14` | `{C.INT.14}` |
| II | `cdp:eq:C.INT.15` | `{C.INT.15}` |
| II | `cdp:eq:C.INT.16` | `{C.INT.16}` |
| II | `cdp:eq:C.INT.17` | `{C.INT.17}` |
| II | `cdp:eq:C.INT.18` | `{C.INT.18}` |
| II | `cdp:eq:C.INT.19` | `{C.INT.19}` |
| II | `cdp:eq:C.INT.2` | `{C.INT.2}` |
| II | `cdp:eq:C.INT.20` | `{C.INT.20}` |
| II | `cdp:eq:C.INT.21` | `{C.INT.21}` |
| II | `cdp:eq:C.INT.22` | `{C.INT.22}` |
| II | `cdp:eq:C.INT.23` | `{C.INT.23}` |
| II | `cdp:eq:C.INT.24` | `{C.INT.24}` |
| II | `cdp:eq:C.INT.25` | `{C.INT.25}` |
| II | `cdp:eq:C.INT.26` | `{C.INT.26}` |
| II | `cdp:eq:C.INT.27` | `{C.INT.27}` |
| II | `cdp:eq:C.INT.3` | `{C.INT.3}` |
| II | `cdp:eq:C.INT.4` | `{C.INT.4}` |
| II | `cdp:eq:C.INT.5` | `{C.INT.5}` |
| II | `cdp:eq:C.INT.6` | `{C.INT.6}` |
| II | `cdp:eq:C.INT.7` | `{C.INT.7}` |
| II | `cdp:eq:C.INT.8` | `{C.INT.8}` |
| II | `cdp:eq:C.INT.9` | `{C.INT.9}` |
| II | `cdp:eq:C.IR.1` | `{C.IR.1}` |
| II | `cdp:eq:C.IR.2` | `{C.IR.2}` |
| II | `cdp:eq:C.IR.3` | `{C.IR.3}` |
| II | `cdp:eq:C.IR.4` | `{C.IR.4}` |
| II | `cdp:eq:C.IR.5` | `{C.IR.5}` |
| II | `cdp:eq:C.IR.6` | `{C.IR.6}` |
| II | `cdp:eq:C.IR.7` | `{C.IR.7}` |
| II | `cdp:eq:C.IR.8` | `{C.IR.8}` |
| II | `cdp:eq:C.IR.9` | `{C.IR.9}` |
| II | `cdp:eq:C.IZ.1` | `{C.IZ.1}` |
| II | `cdp:eq:C.IZ.2` | `{C.IZ.2}` |
| II | `cdp:eq:C.IZ.3` | `{C.IZ.3}` |
| II | `cdp:eq:C.IZ.4` | `{C.IZ.4}` |
| II | `cdp:eq:C.IZ.5` | `{C.IZ.5}` |
| II | `cdp:eq:C.IZ.6` | `{C.IZ.6}` |
| II | `cdp:eq:C.IZ.7` | `{C.IZ.7}` |
| II | `cdp:eq:C.IZ.8` | `{C.IZ.8}` |
| II | `cdp:eq:C.J.1` | `{C.J.1}` |
| II | `cdp:eq:C.J.2` | `{C.J.2}` |
| II | `cdp:eq:C.J.3` | `{C.J.3}` |
| II | `cdp:eq:C.K3.1` | `{C.K3.1}` |
| II | `cdp:eq:C.K3.10` | `{C.K3.10}` |
| II | `cdp:eq:C.K3.2` | `{C.K3.2}` |
| II | `cdp:eq:C.K3.3` | `{C.K3.3}` |
| II | `cdp:eq:C.K3.4` | `{C.K3.4}` |
| II | `cdp:eq:C.K3.5` | `{C.K3.5}` |
| II | `cdp:eq:C.K3.6` | `{C.K3.6}` |
| II | `cdp:eq:C.K3.7` | `{C.K3.7}` |
| II | `cdp:eq:C.K3.8` | `{C.K3.8}` |
| II | `cdp:eq:C.K3.9` | `{C.K3.9}` |
| II | `cdp:eq:C.KG.1` | `{C.KG.1}` |
| II | `cdp:eq:C.KG.10` | `{C.KG.10}` |
| II | `cdp:eq:C.KG.2` | `{C.KG.2}` |
| II | `cdp:eq:C.KG.3` | `{C.KG.3}` |
| II | `cdp:eq:C.KG.4` | `{C.KG.4}` |
| II | `cdp:eq:C.KG.5` | `{C.KG.5}` |
| II | `cdp:eq:C.KG.6` | `{C.KG.6}` |
| II | `cdp:eq:C.KG.7` | `{C.KG.7}` |
| II | `cdp:eq:C.KG.8` | `{C.KG.8}` |
| II | `cdp:eq:C.KG.9` | `{C.KG.9}` |
| II | `cdp:eq:C.KM.1` | `{C.KM.1}` |
| II | `cdp:eq:C.KM.10` | `{C.KM.10}` |
| II | `cdp:eq:C.KM.11` | `{C.KM.11}` |
| II | `cdp:eq:C.KM.2` | `{C.KM.2}` |
| II | `cdp:eq:C.KM.3` | `{C.KM.3}` |
| II | `cdp:eq:C.KM.4` | `{C.KM.4}` |
| II | `cdp:eq:C.KM.5` | `{C.KM.5}` |
| II | `cdp:eq:C.KM.6` | `{C.KM.6}` |
| II | `cdp:eq:C.KM.7` | `{C.KM.7}` |
| II | `cdp:eq:C.KM.8` | `{C.KM.8}` |
| II | `cdp:eq:C.KM.9` | `{C.KM.9}` |
| II | `cdp:eq:C.KM.S1` | `{C.KM.S1}` |
| II | `cdp:eq:C.KM.S2` | `{C.KM.S2}` |
| II | `cdp:eq:C.KM.S3` | `{C.KM.S3}` |
| II | `cdp:eq:C.KX.1` | `{C.KX.1}` |
| II | `cdp:eq:C.KX.10` | `{C.KX.10}` |
| II | `cdp:eq:C.KX.11` | `{C.KX.11}` |
| II | `cdp:eq:C.KX.12` | `{C.KX.12}` |
| II | `cdp:eq:C.KX.13` | `{C.KX.13}` |
| II | `cdp:eq:C.KX.14` | `{C.KX.14}` |
| II | `cdp:eq:C.KX.2` | `{C.KX.2}` |
| II | `cdp:eq:C.KX.3` | `{C.KX.3}` |
| II | `cdp:eq:C.KX.4` | `{C.KX.4}` |
| II | `cdp:eq:C.KX.5` | `{C.KX.5}` |
| II | `cdp:eq:C.KX.6` | `{C.KX.6}` |
| II | `cdp:eq:C.KX.7` | `{C.KX.7}` |
| II | `cdp:eq:C.KX.8` | `{C.KX.8}` |
| II | `cdp:eq:C.KX.9` | `{C.KX.9}` |
| II | `cdp:eq:C.MH.1` | `{C.MH.1}` |
| II | `cdp:eq:C.MH.10` | `{C.MH.10}` |
| II | `cdp:eq:C.MH.11` | `{C.MH.11}` |
| II | `cdp:eq:C.MH.12` | `{C.MH.12}` |
| II | `cdp:eq:C.MH.13` | `{C.MH.13}` |
| II | `cdp:eq:C.MH.14` | `{C.MH.14}` |
| II | `cdp:eq:C.MH.15` | `{C.MH.15}` |
| II | `cdp:eq:C.MH.16` | `{C.MH.16}` |
| II | `cdp:eq:C.MH.17` | `{C.MH.17}` |
| II | `cdp:eq:C.MH.2` | `{C.MH.2}` |
| II | `cdp:eq:C.MH.3` | `{C.MH.3}` |
| II | `cdp:eq:C.MH.4` | `{C.MH.4}` |
| II | `cdp:eq:C.MH.5` | `{C.MH.5}` |
| II | `cdp:eq:C.MH.6` | `{C.MH.6}` |
| II | `cdp:eq:C.MH.7` | `{C.MH.7}` |
| II | `cdp:eq:C.MH.8` | `{C.MH.8}` |
| II | `cdp:eq:C.MH.9` | `{C.MH.9}` |
| II | `cdp:eq:C.ML.1` | `{C.ML.1}` |
| II | `cdp:eq:C.ML.10` | `{C.ML.10}` |
| II | `cdp:eq:C.ML.2` | `{C.ML.2}` |
| II | `cdp:eq:C.ML.3` | `{C.ML.3}` |
| II | `cdp:eq:C.ML.4` | `{C.ML.4}` |
| II | `cdp:eq:C.ML.5` | `{C.ML.5}` |
| II | `cdp:eq:C.ML.6` | `{C.ML.6}` |
| II | `cdp:eq:C.ML.7` | `{C.ML.7}` |
| II | `cdp:eq:C.ML.8` | `{C.ML.8}` |
| II | `cdp:eq:C.ML.9` | `{C.ML.9}` |
| II | `cdp:eq:C.MR.1` | `{C.MR.1}` |
| II | `cdp:eq:C.MR.10` | `{C.MR.10}` |
| II | `cdp:eq:C.MR.11` | `{C.MR.11}` |
| II | `cdp:eq:C.MR.12` | `{C.MR.12}` |
| II | `cdp:eq:C.MR.13` | `{C.MR.13}` |
| II | `cdp:eq:C.MR.14` | `{C.MR.14}` |
| II | `cdp:eq:C.MR.15` | `{C.MR.15}` |
| II | `cdp:eq:C.MR.16` | `{C.MR.16}` |
| II | `cdp:eq:C.MR.2` | `{C.MR.2}` |
| II | `cdp:eq:C.MR.3` | `{C.MR.3}` |
| II | `cdp:eq:C.MR.4` | `{C.MR.4}` |
| II | `cdp:eq:C.MR.5` | `{C.MR.5}` |
| II | `cdp:eq:C.MR.6` | `{C.MR.6}` |
| II | `cdp:eq:C.MR.7` | `{C.MR.7}` |
| II | `cdp:eq:C.MR.8` | `{C.MR.8}` |
| II | `cdp:eq:C.MR.9` | `{C.MR.9}` |
| II | `cdp:eq:C.MS.1` | `{C.MS.1}` |
| II | `cdp:eq:C.MS.10` | `{C.MS.10}` |
| II | `cdp:eq:C.MS.2` | `{C.MS.2}` |
| II | `cdp:eq:C.MS.3` | `{C.MS.3}` |
| II | `cdp:eq:C.MS.4` | `{C.MS.4}` |
| II | `cdp:eq:C.MS.5` | `{C.MS.5}` |
| II | `cdp:eq:C.MS.6` | `{C.MS.6}` |
| II | `cdp:eq:C.MS.7` | `{C.MS.7}` |
| II | `cdp:eq:C.MS.8` | `{C.MS.8}` |
| II | `cdp:eq:C.MS.9` | `{C.MS.9}` |
| II | `cdp:eq:C.MX.1` | `{C.MX.1}` |
| II | `cdp:eq:C.MX.10` | `{C.MX.10}` |
| II | `cdp:eq:C.MX.2` | `{C.MX.2}` |
| II | `cdp:eq:C.MX.3` | `{C.MX.3}` |
| II | `cdp:eq:C.MX.4` | `{C.MX.4}` |
| II | `cdp:eq:C.MX.5` | `{C.MX.5}` |
| II | `cdp:eq:C.MX.6` | `{C.MX.6}` |
| II | `cdp:eq:C.MX.7` | `{C.MX.7}` |
| II | `cdp:eq:C.MX.8` | `{C.MX.8}` |
| II | `cdp:eq:C.MX.9` | `{C.MX.9}` |
| II | `cdp:eq:C.NC.1` | `{C.NC.1}` |
| II | `cdp:eq:C.NC.10` | `{C.NC.10}` |
| II | `cdp:eq:C.NC.11` | `{C.NC.11}` |
| II | `cdp:eq:C.NC.2` | `{C.NC.2}` |
| II | `cdp:eq:C.NC.3` | `{C.NC.3}` |
| II | `cdp:eq:C.NC.4` | `{C.NC.4}` |
| II | `cdp:eq:C.NC.5` | `{C.NC.5}` |
| II | `cdp:eq:C.NC.6` | `{C.NC.6}` |
| II | `cdp:eq:C.NC.7` | `{C.NC.7}` |
| II | `cdp:eq:C.NC.8` | `{C.NC.8}` |
| II | `cdp:eq:C.NC.9` | `{C.NC.9}` |
| II | `cdp:eq:C.NH.1` | `{C.NH.1}` |
| II | `cdp:eq:C.NH.10` | `{C.NH.10}` |
| II | `cdp:eq:C.NH.11` | `{C.NH.11}` |
| II | `cdp:eq:C.NH.12` | `{C.NH.12}` |
| II | `cdp:eq:C.NH.13` | `{C.NH.13}` |
| II | `cdp:eq:C.NH.14` | `{C.NH.14}` |
| II | `cdp:eq:C.NH.15` | `{C.NH.15}` |
| II | `cdp:eq:C.NH.16` | `{C.NH.16}` |
| II | `cdp:eq:C.NH.17` | `{C.NH.17}` |
| II | `cdp:eq:C.NH.18` | `{C.NH.18}` |
| II | `cdp:eq:C.NH.2` | `{C.NH.2}` |
| II | `cdp:eq:C.NH.3` | `{C.NH.3}` |
| II | `cdp:eq:C.NH.4` | `{C.NH.4}` |
| II | `cdp:eq:C.NH.5` | `{C.NH.5}` |
| II | `cdp:eq:C.NH.6` | `{C.NH.6}` |
| II | `cdp:eq:C.NH.7` | `{C.NH.7}` |
| II | `cdp:eq:C.NH.8` | `{C.NH.8}` |
| II | `cdp:eq:C.NH.9` | `{C.NH.9}` |
| II | `cdp:eq:C.NM.1` | `{C.NM.1}` |
| II | `cdp:eq:C.NM.10` | `{C.NM.10}` |
| II | `cdp:eq:C.NM.2` | `{C.NM.2}` |
| II | `cdp:eq:C.NM.3` | `{C.NM.3}` |
| II | `cdp:eq:C.NM.4` | `{C.NM.4}` |
| II | `cdp:eq:C.NM.5` | `{C.NM.5}` |
| II | `cdp:eq:C.NM.6` | `{C.NM.6}` |
| II | `cdp:eq:C.NM.7` | `{C.NM.7}` |
| II | `cdp:eq:C.NM.8` | `{C.NM.8}` |
| II | `cdp:eq:C.NM.9` | `{C.NM.9}` |
| II | `cdp:eq:C.NP.1` | `{C.NP.1}` |
| II | `cdp:eq:C.NP.2` | `{C.NP.2}` |
| II | `cdp:eq:C.NP.3` | `{C.NP.3}` |
| II | `cdp:eq:C.NP.4` | `{C.NP.4}` |
| II | `cdp:eq:C.NP.5` | `{C.NP.5}` |
| II | `cdp:eq:C.NP.6` | `{C.NP.6}` |
| II | `cdp:eq:C.NP.7` | `{C.NP.7}` |
| II | `cdp:eq:C.NP.8` | `{C.NP.8}` |
| II | `cdp:eq:C.NP.9` | `{C.NP.9}` |
| II | `cdp:eq:C.NS.1` | `{C.NS.1}` |
| II | `cdp:eq:C.NS.10` | `{C.NS.10}` |
| II | `cdp:eq:C.NS.11` | `{C.NS.11}` |
| II | `cdp:eq:C.NS.12` | `{C.NS.12}` |
| II | `cdp:eq:C.NS.13` | `{C.NS.13}` |
| II | `cdp:eq:C.NS.14` | `{C.NS.14}` |
| II | `cdp:eq:C.NS.15` | `{C.NS.15}` |
| II | `cdp:eq:C.NS.16` | `{C.NS.16}` |
| II | `cdp:eq:C.NS.17` | `{C.NS.17}` |
| II | `cdp:eq:C.NS.18` | `{C.NS.18}` |
| II | `cdp:eq:C.NS.19` | `{C.NS.19}` |
| II | `cdp:eq:C.NS.2` | `{C.NS.2}` |
| II | `cdp:eq:C.NS.20` | `{C.NS.20}` |
| II | `cdp:eq:C.NS.3` | `{C.NS.3}` |
| II | `cdp:eq:C.NS.4` | `{C.NS.4}` |
| II | `cdp:eq:C.NS.5` | `{C.NS.5}` |
| II | `cdp:eq:C.NS.6` | `{C.NS.6}` |
| II | `cdp:eq:C.NS.7` | `{C.NS.7}` |
| II | `cdp:eq:C.NS.8` | `{C.NS.8}` |
| II | `cdp:eq:C.NS.9` | `{C.NS.9}` |
| II | `cdp:eq:C.NT.1` | `{C.NT.1}` |
| II | `cdp:eq:C.NT.2` | `{C.NT.2}` |
| II | `cdp:eq:C.NT.3` | `{C.NT.3}` |
| II | `cdp:eq:C.NT.4` | `{C.NT.4}` |
| II | `cdp:eq:C.NT.5` | `{C.NT.5}` |
| II | `cdp:eq:C.NT.6` | `{C.NT.6}` |
| II | `cdp:eq:C.NT.7` | `{C.NT.7}` |
| II | `cdp:eq:C.NT.8` | `{C.NT.8}` |
| II | `cdp:eq:C.PE.1` | `{C.PE.1}` |
| II | `cdp:eq:C.PE.10` | `{C.PE.10}` |
| II | `cdp:eq:C.PE.11` | `{C.PE.11}` |
| II | `cdp:eq:C.PE.12` | `{C.PE.12}` |
| II | `cdp:eq:C.PE.13` | `{C.PE.13}` |
| II | `cdp:eq:C.PE.14` | `{C.PE.14}` |
| II | `cdp:eq:C.PE.15` | `{C.PE.15}` |
| II | `cdp:eq:C.PE.16` | `{C.PE.16}` |
| II | `cdp:eq:C.PE.17` | `{C.PE.17}` |
| II | `cdp:eq:C.PE.18` | `{C.PE.18}` |
| II | `cdp:eq:C.PE.19` | `{C.PE.19}` |
| II | `cdp:eq:C.PE.2` | `{C.PE.2}` |
| II | `cdp:eq:C.PE.20` | `{C.PE.20}` |
| II | `cdp:eq:C.PE.21` | `{C.PE.21}` |
| II | `cdp:eq:C.PE.3` | `{C.PE.3}` |
| II | `cdp:eq:C.PE.4` | `{C.PE.4}` |
| II | `cdp:eq:C.PE.5` | `{C.PE.5}` |
| II | `cdp:eq:C.PE.6` | `{C.PE.6}` |
| II | `cdp:eq:C.PE.7` | `{C.PE.7}` |
| II | `cdp:eq:C.PE.8` | `{C.PE.8}` |
| II | `cdp:eq:C.PE.9` | `{C.PE.9}` |
| II | `cdp:eq:C.PF.1` | `{C.PF.1}` |
| II | `cdp:eq:C.PF.10` | `{C.PF.10}` |
| II | `cdp:eq:C.PF.11` | `{C.PF.11}` |
| II | `cdp:eq:C.PF.12` | `{C.PF.12}` |
| II | `cdp:eq:C.PF.2` | `{C.PF.2}` |
| II | `cdp:eq:C.PF.3` | `{C.PF.3}` |
| II | `cdp:eq:C.PF.4` | `{C.PF.4}` |
| II | `cdp:eq:C.PF.5` | `{C.PF.5}` |
| II | `cdp:eq:C.PF.6` | `{C.PF.6}` |
| II | `cdp:eq:C.PF.7` | `{C.PF.7}` |
| II | `cdp:eq:C.PF.8` | `{C.PF.8}` |
| II | `cdp:eq:C.PF.9` | `{C.PF.9}` |
| II | `cdp:eq:C.PG.1` | `{C.PG.1}` |
| II | `cdp:eq:C.PG.2` | `{C.PG.2}` |
| II | `cdp:eq:C.PG.3` | `{C.PG.3}` |
| II | `cdp:eq:C.PG.4` | `{C.PG.4}` |
| II | `cdp:eq:C.PG.5` | `{C.PG.5}` |
| II | `cdp:eq:C.PG.6` | `{C.PG.6}` |
| II | `cdp:eq:C.PG.7` | `{C.PG.7}` |
| II | `cdp:eq:C.PG.8` | `{C.PG.8}` |
| II | `cdp:eq:C.PG.9` | `{C.PG.9}` |
| II | `cdp:eq:C.PK.1` | `{C.PK.1}` |
| II | `cdp:eq:C.PK.2` | `{C.PK.2}` |
| II | `cdp:eq:C.PK.3` | `{C.PK.3}` |
| II | `cdp:eq:C.PK.4` | `{C.PK.4}` |
| II | `cdp:eq:C.PK.5` | `{C.PK.5}` |
| II | `cdp:eq:C.PK.6` | `{C.PK.6}` |
| II | `cdp:eq:C.PK.7` | `{C.PK.7}` |
| II | `cdp:eq:C.PK.8` | `{C.PK.8}` |
| II | `cdp:eq:C.PK.9` | `{C.PK.9}` |
| II | `cdp:eq:C.PR.1` | `{C.PR.1}` |
| II | `cdp:eq:C.PR.10` | `{C.PR.10}` |
| II | `cdp:eq:C.PR.11` | `{C.PR.11}` |
| II | `cdp:eq:C.PR.12` | `{C.PR.12}` |
| II | `cdp:eq:C.PR.13` | `{C.PR.13}` |
| II | `cdp:eq:C.PR.14` | `{C.PR.14}` |
| II | `cdp:eq:C.PR.15` | `{C.PR.15}` |
| II | `cdp:eq:C.PR.16` | `{C.PR.16}` |
| II | `cdp:eq:C.PR.17` | `{C.PR.17}` |
| II | `cdp:eq:C.PR.18` | `{C.PR.18}` |
| II | `cdp:eq:C.PR.2` | `{C.PR.2}` |
| II | `cdp:eq:C.PR.3` | `{C.PR.3}` |
| II | `cdp:eq:C.PR.4` | `{C.PR.4}` |
| II | `cdp:eq:C.PR.5` | `{C.PR.5}` |
| II | `cdp:eq:C.PR.6` | `{C.PR.6}` |
| II | `cdp:eq:C.PR.7` | `{C.PR.7}` |
| II | `cdp:eq:C.PR.8` | `{C.PR.8}` |
| II | `cdp:eq:C.PR.9` | `{C.PR.9}` |
| II | `cdp:eq:C.PT.1` | `{C.PT.1}` |
| II | `cdp:eq:C.PT.10` | `{C.PT.10}` |
| II | `cdp:eq:C.PT.11` | `{C.PT.11}` |
| II | `cdp:eq:C.PT.12` | `{C.PT.12}` |
| II | `cdp:eq:C.PT.13` | `{C.PT.13}` |
| II | `cdp:eq:C.PT.14` | `{C.PT.14}` |
| II | `cdp:eq:C.PT.2` | `{C.PT.2}` |
| II | `cdp:eq:C.PT.3` | `{C.PT.3}` |
| II | `cdp:eq:C.PT.4` | `{C.PT.4}` |
| II | `cdp:eq:C.PT.5` | `{C.PT.5}` |
| II | `cdp:eq:C.PT.6` | `{C.PT.6}` |
| II | `cdp:eq:C.PT.7` | `{C.PT.7}` |
| II | `cdp:eq:C.PT.8` | `{C.PT.8}` |
| II | `cdp:eq:C.PT.9` | `{C.PT.9}` |
| II | `cdp:eq:C.QT.1` | `{C.QT.1}` |
| II | `cdp:eq:C.QT.10` | `{C.QT.10}` |
| II | `cdp:eq:C.QT.11` | `{C.QT.11}` |
| II | `cdp:eq:C.QT.12` | `{C.QT.12}` |
| II | `cdp:eq:C.QT.13` | `{C.QT.13}` |
| II | `cdp:eq:C.QT.2` | `{C.QT.2}` |
| II | `cdp:eq:C.QT.3` | `{C.QT.3}` |
| II | `cdp:eq:C.QT.4` | `{C.QT.4}` |
| II | `cdp:eq:C.QT.5` | `{C.QT.5}` |
| II | `cdp:eq:C.QT.6` | `{C.QT.6}` |
| II | `cdp:eq:C.QT.7` | `{C.QT.7}` |
| II | `cdp:eq:C.QT.8` | `{C.QT.8}` |
| II | `cdp:eq:C.QT.9` | `{C.QT.9}` |
| II | `cdp:eq:C.RA.1` | `{C.RA.1}` |
| II | `cdp:eq:C.RA.10` | `{C.RA.10}` |
| II | `cdp:eq:C.RA.11` | `{C.RA.11}` |
| II | `cdp:eq:C.RA.12` | `{C.RA.12}` |
| II | `cdp:eq:C.RA.13` | `{C.RA.13}` |
| II | `cdp:eq:C.RA.14` | `{C.RA.14}` |
| II | `cdp:eq:C.RA.15` | `{C.RA.15}` |
| II | `cdp:eq:C.RA.16` | `{C.RA.16}` |
| II | `cdp:eq:C.RA.17` | `{C.RA.17}` |
| II | `cdp:eq:C.RA.18` | `{C.RA.18}` |
| II | `cdp:eq:C.RA.19` | `{C.RA.19}` |
| II | `cdp:eq:C.RA.2` | `{C.RA.2}` |
| II | `cdp:eq:C.RA.20` | `{C.RA.20}` |
| II | `cdp:eq:C.RA.21` | `{C.RA.21}` |
| II | `cdp:eq:C.RA.22` | `{C.RA.22}` |
| II | `cdp:eq:C.RA.23` | `{C.RA.23}` |
| II | `cdp:eq:C.RA.24` | `{C.RA.24}` |
| II | `cdp:eq:C.RA.25` | `{C.RA.25}` |
| II | `cdp:eq:C.RA.26` | `{C.RA.26}` |
| II | `cdp:eq:C.RA.27` | `{C.RA.27}` |
| II | `cdp:eq:C.RA.28` | `{C.RA.28}` |
| II | `cdp:eq:C.RA.29` | `{C.RA.29}` |
| II | `cdp:eq:C.RA.3` | `{C.RA.3}` |
| II | `cdp:eq:C.RA.30` | `{C.RA.30}` |
| II | `cdp:eq:C.RA.31` | `{C.RA.31}` |
| II | `cdp:eq:C.RA.31a` | `{C.RA.31a}` |
| II | `cdp:eq:C.RA.32` | `{C.RA.32}` |
| II | `cdp:eq:C.RA.4` | `{C.RA.4}` |
| II | `cdp:eq:C.RA.5` | `{C.RA.5}` |
| II | `cdp:eq:C.RA.6` | `{C.RA.6}` |
| II | `cdp:eq:C.RA.7` | `{C.RA.7}` |
| II | `cdp:eq:C.RA.8` | `{C.RA.8}` |
| II | `cdp:eq:C.RA.9` | `{C.RA.9}` |
| II | `cdp:eq:C.RC.1` | `{C.RC.1}` |
| II | `cdp:eq:C.RC.10` | `{C.RC.10}` |
| II | `cdp:eq:C.RC.11` | `{C.RC.11}` |
| II | `cdp:eq:C.RC.12` | `{C.RC.12}` |
| II | `cdp:eq:C.RC.2` | `{C.RC.2}` |
| II | `cdp:eq:C.RC.3` | `{C.RC.3}` |
| II | `cdp:eq:C.RC.4` | `{C.RC.4}` |
| II | `cdp:eq:C.RC.5` | `{C.RC.5}` |
| II | `cdp:eq:C.RC.6` | `{C.RC.6}` |
| II | `cdp:eq:C.RC.7` | `{C.RC.7}` |
| II | `cdp:eq:C.RC.8` | `{C.RC.8}` |
| II | `cdp:eq:C.RC.9` | `{C.RC.9}` |
| II | `cdp:eq:C.RD.1` | `{C.RD.1}` |
| II | `cdp:eq:C.RD.10` | `{C.RD.10}` |
| II | `cdp:eq:C.RD.11` | `{C.RD.11}` |
| II | `cdp:eq:C.RD.12` | `{C.RD.12}` |
| II | `cdp:eq:C.RD.13` | `{C.RD.13}` |
| II | `cdp:eq:C.RD.14` | `{C.RD.14}` |
| II | `cdp:eq:C.RD.15` | `{C.RD.15}` |
| II | `cdp:eq:C.RD.16` | `{C.RD.16}` |
| II | `cdp:eq:C.RD.17` | `{C.RD.17}` |
| II | `cdp:eq:C.RD.18` | `{C.RD.18}` |
| II | `cdp:eq:C.RD.19` | `{C.RD.19}` |
| II | `cdp:eq:C.RD.2` | `{C.RD.2}` |
| II | `cdp:eq:C.RD.20` | `{C.RD.20}` |
| II | `cdp:eq:C.RD.21` | `{C.RD.21}` |
| II | `cdp:eq:C.RD.22` | `{C.RD.22}` |
| II | `cdp:eq:C.RD.23` | `{C.RD.23}` |
| II | `cdp:eq:C.RD.24` | `{C.RD.24}` |
| II | `cdp:eq:C.RD.25` | `{C.RD.25}` |
| II | `cdp:eq:C.RD.26` | `{C.RD.26}` |
| II | `cdp:eq:C.RD.27` | `{C.RD.27}` |
| II | `cdp:eq:C.RD.28` | `{C.RD.28}` |
| II | `cdp:eq:C.RD.29` | `{C.RD.29}` |
| II | `cdp:eq:C.RD.3` | `{C.RD.3}` |
| II | `cdp:eq:C.RD.30` | `{C.RD.30}` |
| II | `cdp:eq:C.RD.31` | `{C.RD.31}` |
| II | `cdp:eq:C.RD.32` | `{C.RD.32}` |
| II | `cdp:eq:C.RD.33` | `{C.RD.33}` |
| II | `cdp:eq:C.RD.34` | `{C.RD.34}` |
| II | `cdp:eq:C.RD.35` | `{C.RD.35}` |
| II | `cdp:eq:C.RD.36` | `{C.RD.36}` |
| II | `cdp:eq:C.RD.37` | `{C.RD.37}` |
| II | `cdp:eq:C.RD.4` | `{C.RD.4}` |
| II | `cdp:eq:C.RD.5` | `{C.RD.5}` |
| II | `cdp:eq:C.RD.6` | `{C.RD.6}` |
| II | `cdp:eq:C.RD.7` | `{C.RD.7}` |
| II | `cdp:eq:C.RD.8` | `{C.RD.8}` |
| II | `cdp:eq:C.RD.9` | `{C.RD.9}` |
| II | `cdp:eq:C.RF.1` | `{C.RF.1}` |
| II | `cdp:eq:C.RF.2` | `{C.RF.2}` |
| II | `cdp:eq:C.RF.3` | `{C.RF.3}` |
| II | `cdp:eq:C.RF.4` | `{C.RF.4}` |
| II | `cdp:eq:C.RF.5` | `{C.RF.5}` |
| II | `cdp:eq:C.RF.6` | `{C.RF.6}` |
| II | `cdp:eq:C.RF.7` | `{C.RF.7}` |
| II | `cdp:eq:C.RF.8` | `{C.RF.8}` |
| II | `cdp:eq:C.RF.9` | `{C.RF.9}` |
| II | `cdp:eq:C.RG.1` | `{C.RG.1}` |
| II | `cdp:eq:C.RG.10` | `{C.RG.10}` |
| II | `cdp:eq:C.RG.11` | `{C.RG.11}` |
| II | `cdp:eq:C.RG.12` | `{C.RG.12}` |
| II | `cdp:eq:C.RG.13` | `{C.RG.13}` |
| II | `cdp:eq:C.RG.2` | `{C.RG.2}` |
| II | `cdp:eq:C.RG.3` | `{C.RG.3}` |
| II | `cdp:eq:C.RG.4` | `{C.RG.4}` |
| II | `cdp:eq:C.RG.5` | `{C.RG.5}` |
| II | `cdp:eq:C.RG.6` | `{C.RG.6}` |
| II | `cdp:eq:C.RG.7` | `{C.RG.7}` |
| II | `cdp:eq:C.RG.8` | `{C.RG.8}` |
| II | `cdp:eq:C.RG.9` | `{C.RG.9}` |
| II | `cdp:eq:C.RH.1` | `{C.RH.1}` |
| II | `cdp:eq:C.RH.10` | `{C.RH.10}` |
| II | `cdp:eq:C.RH.2` | `{C.RH.2}` |
| II | `cdp:eq:C.RH.3` | `{C.RH.3}` |
| II | `cdp:eq:C.RH.4` | `{C.RH.4}` |
| II | `cdp:eq:C.RH.5` | `{C.RH.5}` |
| II | `cdp:eq:C.RH.6` | `{C.RH.6}` |
| II | `cdp:eq:C.RH.7` | `{C.RH.7}` |
| II | `cdp:eq:C.RH.8` | `{C.RH.8}` |
| II | `cdp:eq:C.RH.9` | `{C.RH.9}` |
| II | `cdp:eq:C.RK.1` | `{C.RK.1}` |
| II | `cdp:eq:C.RK.10` | `{C.RK.10}` |
| II | `cdp:eq:C.RK.11` | `{C.RK.11}` |
| II | `cdp:eq:C.RK.12` | `{C.RK.12}` |
| II | `cdp:eq:C.RK.13` | `{C.RK.13}` |
| II | `cdp:eq:C.RK.14` | `{C.RK.14}` |
| II | `cdp:eq:C.RK.15` | `{C.RK.15}` |
| II | `cdp:eq:C.RK.16` | `{C.RK.16}` |
| II | `cdp:eq:C.RK.17` | `{C.RK.17}` |
| II | `cdp:eq:C.RK.18` | `{C.RK.18}` |
| II | `cdp:eq:C.RK.19` | `{C.RK.19}` |
| II | `cdp:eq:C.RK.2` | `{C.RK.2}` |
| II | `cdp:eq:C.RK.20` | `{C.RK.20}` |
| II | `cdp:eq:C.RK.21` | `{C.RK.21}` |
| II | `cdp:eq:C.RK.22` | `{C.RK.22}` |
| II | `cdp:eq:C.RK.3` | `{C.RK.3}` |
| II | `cdp:eq:C.RK.4` | `{C.RK.4}` |
| II | `cdp:eq:C.RK.5` | `{C.RK.5}` |
| II | `cdp:eq:C.RK.6` | `{C.RK.6}` |
| II | `cdp:eq:C.RK.7` | `{C.RK.7}` |
| II | `cdp:eq:C.RK.8` | `{C.RK.8}` |
| II | `cdp:eq:C.RK.9` | `{C.RK.9}` |
| II | `cdp:eq:C.RU.1` | `{C.RU.1}` |
| II | `cdp:eq:C.RU.2` | `{C.RU.2}` |
| II | `cdp:eq:C.RU.3` | `{C.RU.3}` |
| II | `cdp:eq:C.RU.4` | `{C.RU.4}` |
| II | `cdp:eq:C.RU.5` | `{C.RU.5}` |
| II | `cdp:eq:C.RU.6` | `{C.RU.6}` |
| II | `cdp:eq:C.RU.7` | `{C.RU.7}` |
| II | `cdp:eq:C.RU.8` | `{C.RU.8}` |
| II | `cdp:eq:C.RU.9` | `{C.RU.9}` |
| II | `cdp:eq:C.SC.1` | `{C.SC.1}` |
| II | `cdp:eq:C.SC.2` | `{C.SC.2}` |
| II | `cdp:eq:C.SC.3` | `{C.SC.3}` |
| II | `cdp:eq:C.SC.4` | `{C.SC.4}` |
| II | `cdp:eq:C.SC.5` | `{C.SC.5}` |
| II | `cdp:eq:C.SC.6` | `{C.SC.6}` |
| II | `cdp:eq:C.SF.1` | `{C.SF.1}` |
| II | `cdp:eq:C.SF.10` | `{C.SF.10}` |
| II | `cdp:eq:C.SF.11` | `{C.SF.11}` |
| II | `cdp:eq:C.SF.12` | `{C.SF.12}` |
| II | `cdp:eq:C.SF.13` | `{C.SF.13}` |
| II | `cdp:eq:C.SF.2` | `{C.SF.2}` |
| II | `cdp:eq:C.SF.3` | `{C.SF.3}` |
| II | `cdp:eq:C.SF.4` | `{C.SF.4}` |
| II | `cdp:eq:C.SF.5` | `{C.SF.5}` |
| II | `cdp:eq:C.SF.6` | `{C.SF.6}` |
| II | `cdp:eq:C.SF.7` | `{C.SF.7}` |
| II | `cdp:eq:C.SF.8` | `{C.SF.8}` |
| II | `cdp:eq:C.SF.9` | `{C.SF.9}` |
| II | `cdp:eq:C.SH.1` | `{C.SH.1}` |
| II | `cdp:eq:C.SH.10` | `{C.SH.10}` |
| II | `cdp:eq:C.SH.11` | `{C.SH.11}` |
| II | `cdp:eq:C.SH.12` | `{C.SH.12}` |
| II | `cdp:eq:C.SH.13` | `{C.SH.13}` |
| II | `cdp:eq:C.SH.2` | `{C.SH.2}` |
| II | `cdp:eq:C.SH.3` | `{C.SH.3}` |
| II | `cdp:eq:C.SH.4` | `{C.SH.4}` |
| II | `cdp:eq:C.SH.5` | `{C.SH.5}` |
| II | `cdp:eq:C.SH.6` | `{C.SH.6}` |
| II | `cdp:eq:C.SH.7` | `{C.SH.7}` |
| II | `cdp:eq:C.SH.8` | `{C.SH.8}` |
| II | `cdp:eq:C.SH.9` | `{C.SH.9}` |
| II | `cdp:eq:C.SK.1` | `{C.SK.1}` |
| II | `cdp:eq:C.SK.2` | `{C.SK.2}` |
| II | `cdp:eq:C.SK.3` | `{C.SK.3}` |
| II | `cdp:eq:C.SK.4` | `{C.SK.4}` |
| II | `cdp:eq:C.SK.5` | `{C.SK.5}` |
| II | `cdp:eq:C.SK.6` | `{C.SK.6}` |
| II | `cdp:eq:C.SKD.1` | `{C.SKD.1}` |
| II | `cdp:eq:C.SKD.10` | `{C.SKD.10}` |
| II | `cdp:eq:C.SKD.11` | `{C.SKD.11}` |
| II | `cdp:eq:C.SKD.12` | `{C.SKD.12}` |
| II | `cdp:eq:C.SKD.13` | `{C.SKD.13}` |
| II | `cdp:eq:C.SKD.14` | `{C.SKD.14}` |
| II | `cdp:eq:C.SKD.15` | `{C.SKD.15}` |
| II | `cdp:eq:C.SKD.2` | `{C.SKD.2}` |
| II | `cdp:eq:C.SKD.3` | `{C.SKD.3}` |
| II | `cdp:eq:C.SKD.4` | `{C.SKD.4}` |
| II | `cdp:eq:C.SKD.5` | `{C.SKD.5}` |
| II | `cdp:eq:C.SKD.6` | `{C.SKD.6}` |
| II | `cdp:eq:C.SKD.7` | `{C.SKD.7}` |
| II | `cdp:eq:C.SKD.8` | `{C.SKD.8}` |
| II | `cdp:eq:C.SKD.9` | `{C.SKD.9}` |
| II | `cdp:eq:C.SN.1` | `{C.SN.1}` |
| II | `cdp:eq:C.SN.10` | `{C.SN.10}` |
| II | `cdp:eq:C.SN.2` | `{C.SN.2}` |
| II | `cdp:eq:C.SN.3` | `{C.SN.3}` |
| II | `cdp:eq:C.SN.4` | `{C.SN.4}` |
| II | `cdp:eq:C.SN.5` | `{C.SN.5}` |
| II | `cdp:eq:C.SN.6` | `{C.SN.6}` |
| II | `cdp:eq:C.SN.7` | `{C.SN.7}` |
| II | `cdp:eq:C.SN.8` | `{C.SN.8}` |
| II | `cdp:eq:C.SN.9` | `{C.SN.9}` |
| II | `cdp:eq:C.TC.1` | `{C.TC.1}` |
| II | `cdp:eq:C.TC.10` | `{C.TC.10}` |
| II | `cdp:eq:C.TC.11` | `{C.TC.11}` |
| II | `cdp:eq:C.TC.12` | `{C.TC.12}` |
| II | `cdp:eq:C.TC.2` | `{C.TC.2}` |
| II | `cdp:eq:C.TC.3` | `{C.TC.3}` |
| II | `cdp:eq:C.TC.4` | `{C.TC.4}` |
| II | `cdp:eq:C.TC.5` | `{C.TC.5}` |
| II | `cdp:eq:C.TC.6` | `{C.TC.6}` |
| II | `cdp:eq:C.TC.7` | `{C.TC.7}` |
| II | `cdp:eq:C.TC.8` | `{C.TC.8}` |
| II | `cdp:eq:C.TC.9` | `{C.TC.9}` |
| II | `cdp:eq:C.TEST.1` | `{C.TEST.1}` |
| II | `cdp:eq:C.TEST.2` | `{C.TEST.2}` |
| II | `cdp:eq:C.TG.1` | `{C.TG.1}` |
| II | `cdp:eq:C.TG.10` | `{C.TG.10}` |
| II | `cdp:eq:C.TG.11` | `{C.TG.11}` |
| II | `cdp:eq:C.TG.12` | `{C.TG.12}` |
| II | `cdp:eq:C.TG.13` | `{C.TG.13}` |
| II | `cdp:eq:C.TG.14` | `{C.TG.14}` |
| II | `cdp:eq:C.TG.15` | `{C.TG.15}` |
| II | `cdp:eq:C.TG.2` | `{C.TG.2}` |
| II | `cdp:eq:C.TG.3` | `{C.TG.3}` |
| II | `cdp:eq:C.TG.4` | `{C.TG.4}` |
| II | `cdp:eq:C.TG.5` | `{C.TG.5}` |
| II | `cdp:eq:C.TG.6` | `{C.TG.6}` |
| II | `cdp:eq:C.TG.7` | `{C.TG.7}` |
| II | `cdp:eq:C.TG.8` | `{C.TG.8}` |
| II | `cdp:eq:C.TG.9` | `{C.TG.9}` |
| II | `cdp:eq:C.TI.1` | `{C.TI.1}` |
| II | `cdp:eq:C.TI.10` | `{C.TI.10}` |
| II | `cdp:eq:C.TI.11` | `{C.TI.11}` |
| II | `cdp:eq:C.TI.12` | `{C.TI.12}` |
| II | `cdp:eq:C.TI.13` | `{C.TI.13}` |
| II | `cdp:eq:C.TI.14` | `{C.TI.14}` |
| II | `cdp:eq:C.TI.2` | `{C.TI.2}` |
| II | `cdp:eq:C.TI.3` | `{C.TI.3}` |
| II | `cdp:eq:C.TI.4` | `{C.TI.4}` |
| II | `cdp:eq:C.TI.5` | `{C.TI.5}` |
| II | `cdp:eq:C.TI.6` | `{C.TI.6}` |
| II | `cdp:eq:C.TI.7` | `{C.TI.7}` |
| II | `cdp:eq:C.TI.8` | `{C.TI.8}` |
| II | `cdp:eq:C.TI.9` | `{C.TI.9}` |
| II | `cdp:eq:C.TK.1` | `{C.TK.1}` |
| II | `cdp:eq:C.TK.2` | `{C.TK.2}` |
| II | `cdp:eq:C.TK.3` | `{C.TK.3}` |
| II | `cdp:eq:C.TK.4` | `{C.TK.4}` |
| II | `cdp:eq:C.TK.5` | `{C.TK.5}` |
| II | `cdp:eq:C.TK.6` | `{C.TK.6}` |
| II | `cdp:eq:C.TK.7` | `{C.TK.7}` |
| II | `cdp:eq:C.TL.1` | `{C.TL.1}` |
| II | `cdp:eq:C.TL.2` | `{C.TL.2}` |
| II | `cdp:eq:C.TL.3` | `{C.TL.3}` |
| II | `cdp:eq:C.TL.4` | `{C.TL.4}` |
| II | `cdp:eq:C.TL.5` | `{C.TL.5}` |
| II | `cdp:eq:C.TL.6` | `{C.TL.6}` |
| II | `cdp:eq:C.TL.7` | `{C.TL.7}` |
| II | `cdp:eq:C.TL.8` | `{C.TL.8}` |
| II | `cdp:eq:C.TX.1` | `{C.TX.1}` |
| II | `cdp:eq:C.TX.10` | `{C.TX.10}` |
| II | `cdp:eq:C.TX.11` | `{C.TX.11}` |
| II | `cdp:eq:C.TX.12` | `{C.TX.12}` |
| II | `cdp:eq:C.TX.13` | `{C.TX.13}` |
| II | `cdp:eq:C.TX.14` | `{C.TX.14}` |
| II | `cdp:eq:C.TX.2` | `{C.TX.2}` |
| II | `cdp:eq:C.TX.3` | `{C.TX.3}` |
| II | `cdp:eq:C.TX.4` | `{C.TX.4}` |
| II | `cdp:eq:C.TX.5` | `{C.TX.5}` |
| II | `cdp:eq:C.TX.6` | `{C.TX.6}` |
| II | `cdp:eq:C.TX.7` | `{C.TX.7}` |
| II | `cdp:eq:C.TX.8` | `{C.TX.8}` |
| II | `cdp:eq:C.TX.9` | `{C.TX.9}` |
| II | `cdp:eq:C.UC.1` | `{C.UC.1}` |
| II | `cdp:eq:C.UC.10` | `{C.UC.10}` |
| II | `cdp:eq:C.UC.2` | `{C.UC.2}` |
| II | `cdp:eq:C.UC.3` | `{C.UC.3}` |
| II | `cdp:eq:C.UC.4` | `{C.UC.4}` |
| II | `cdp:eq:C.UC.5` | `{C.UC.5}` |
| II | `cdp:eq:C.UC.6` | `{C.UC.6}` |
| II | `cdp:eq:C.UC.7` | `{C.UC.7}` |
| II | `cdp:eq:C.UC.8` | `{C.UC.8}` |
| II | `cdp:eq:C.UC.9` | `{C.UC.9}` |
| II | `cdp:eq:C.UI.1` | `{C.UI.1}` |
| II | `cdp:eq:C.UI.10` | `{C.UI.10}` |
| II | `cdp:eq:C.UI.11` | `{C.UI.11}` |
| II | `cdp:eq:C.UI.12` | `{C.UI.12}` |
| II | `cdp:eq:C.UI.13` | `{C.UI.13}` |
| II | `cdp:eq:C.UI.14` | `{C.UI.14}` |
| II | `cdp:eq:C.UI.15` | `{C.UI.15}` |
| II | `cdp:eq:C.UI.16` | `{C.UI.16}` |
| II | `cdp:eq:C.UI.2` | `{C.UI.2}` |
| II | `cdp:eq:C.UI.3` | `{C.UI.3}` |
| II | `cdp:eq:C.UI.4` | `{C.UI.4}` |
| II | `cdp:eq:C.UI.5` | `{C.UI.5}` |
| II | `cdp:eq:C.UI.6` | `{C.UI.6}` |
| II | `cdp:eq:C.UI.7` | `{C.UI.7}` |
| II | `cdp:eq:C.UI.8` | `{C.UI.8}` |
| II | `cdp:eq:C.UI.9` | `{C.UI.9}` |
| II | `cdp:eq:C.UN.1` | `{C.UN.1}` |
| II | `cdp:eq:C.UN.2` | `{C.UN.2}` |
| II | `cdp:eq:C.UN.3` | `{C.UN.3}` |
| II | `cdp:eq:C.UN.4` | `{C.UN.4}` |
| II | `cdp:eq:C.UN.5` | `{C.UN.5}` |
| II | `cdp:eq:C.UN.6` | `{C.UN.6}` |
| II | `cdp:eq:C.UNCR.1` | `{C.UNCR.1}` |
| II | `cdp:eq:C.UNCR.2` | `{C.UNCR.2}` |
| II | `cdp:eq:C.UNCR.3` | `{C.UNCR.3}` |
| II | `cdp:eq:C.UNN.1` | `{C.UNN.1}` |
| II | `cdp:eq:C.UNN.2` | `{C.UNN.2}` |
| II | `cdp:eq:C.UNNODE.1` | `{C.UNNODE.1}` |
| II | `cdp:eq:C.UNNODE.2` | `{C.UNNODE.2}` |
| II | `cdp:eq:C.UNNODE.3` | `{C.UNNODE.3}` |
| II | `cdp:eq:C.VC.1` | `{C.VC.1}` |
| II | `cdp:eq:C.VC.2` | `{C.VC.2}` |
| II | `cdp:eq:C.VC.3` | `{C.VC.3}` |
| II | `cdp:eq:C.VC.4` | `{C.VC.4}` |
| II | `cdp:eq:C.VII.1` | `{C.VII.1}` |
| II | `cdp:eq:C.VII.10` | `{C.VII.10}` |
| II | `cdp:eq:C.VII.11` | `{C.VII.11}` |
| II | `cdp:eq:C.VII.12` | `{C.VII.12}` |
| II | `cdp:eq:C.VII.2` | `{C.VII.2}` |
| II | `cdp:eq:C.VII.3` | `{C.VII.3}` |
| II | `cdp:eq:C.VII.4` | `{C.VII.4}` |
| II | `cdp:eq:C.VII.5` | `{C.VII.5}` |
| II | `cdp:eq:C.VII.6` | `{C.VII.6}` |
| II | `cdp:eq:C.VII.7` | `{C.VII.7}` |
| II | `cdp:eq:C.VII.8` | `{C.VII.8}` |
| II | `cdp:eq:C.VII.9` | `{C.VII.9}` |
| II | `cdp:eq:C.VR.1` | `{C.VR.1}` |
| II | `cdp:eq:C.VR.2` | `{C.VR.2}` |
| II | `cdp:eq:C.VR.3` | `{C.VR.3}` |
| II | `cdp:eq:C.VR.4` | `{C.VR.4}` |
| II | `cdp:eq:C.VR.5` | `{C.VR.5}` |
| II | `cdp:eq:C.VR.6` | `{C.VR.6}` |
| II | `cdp:eq:C.VR.7` | `{C.VR.7}` |
| II | `cdp:eq:C.VR.8` | `{C.VR.8}` |
| II | `cdp:eq:C.VR.9` | `{C.VR.9}` |
| II | `cdp:eq:C.WF.1` | `{C.WF.1}` |
| II | `cdp:eq:C.WF.10` | `{C.WF.10}` |
| II | `cdp:eq:C.WF.11` | `{C.WF.11}` |
| II | `cdp:eq:C.WF.12` | `{C.WF.12}` |
| II | `cdp:eq:C.WF.13` | `{C.WF.13}` |
| II | `cdp:eq:C.WF.14` | `{C.WF.14}` |
| II | `cdp:eq:C.WF.15` | `{C.WF.15}` |
| II | `cdp:eq:C.WF.16` | `{C.WF.16}` |
| II | `cdp:eq:C.WF.17` | `{C.WF.17}` |
| II | `cdp:eq:C.WF.18` | `{C.WF.18}` |
| II | `cdp:eq:C.WF.19` | `{C.WF.19}` |
| II | `cdp:eq:C.WF.2` | `{C.WF.2}` |
| II | `cdp:eq:C.WF.20` | `{C.WF.20}` |
| II | `cdp:eq:C.WF.21` | `{C.WF.21}` |
| II | `cdp:eq:C.WF.22` | `{C.WF.22}` |
| II | `cdp:eq:C.WF.23` | `{C.WF.23}` |
| II | `cdp:eq:C.WF.24` | `{C.WF.24}` |
| II | `cdp:eq:C.WF.25` | `{C.WF.25}` |
| II | `cdp:eq:C.WF.26` | `{C.WF.26}` |
| II | `cdp:eq:C.WF.27` | `{C.WF.27}` |
| II | `cdp:eq:C.WF.28` | `{C.WF.28}` |
| II | `cdp:eq:C.WF.3` | `{C.WF.3}` |
| II | `cdp:eq:C.WF.4` | `{C.WF.4}` |
| II | `cdp:eq:C.WF.5` | `{C.WF.5}` |
| II | `cdp:eq:C.WF.6` | `{C.WF.6}` |
| II | `cdp:eq:C.WF.7` | `{C.WF.7}` |
| II | `cdp:eq:C.WF.8` | `{C.WF.8}` |
| II | `cdp:eq:C.WF.9` | `{C.WF.9}` |
| II | `cdp:eq:C.WH.0` | `{C.WH.0}` |
| II | `cdp:eq:C.WH.1` | `{C.WH.1}` |
| II | `cdp:eq:C.WH.10` | `{C.WH.10}` |
| II | `cdp:eq:C.WH.11` | `{C.WH.11}` |
| II | `cdp:eq:C.WH.12` | `{C.WH.12}` |
| II | `cdp:eq:C.WH.13` | `{C.WH.13}` |
| II | `cdp:eq:C.WH.14` | `{C.WH.14}` |
| II | `cdp:eq:C.WH.15` | `{C.WH.15}` |
| II | `cdp:eq:C.WH.16` | `{C.WH.16}` |
| II | `cdp:eq:C.WH.17` | `{C.WH.17}` |
| II | `cdp:eq:C.WH.2` | `{C.WH.2}` |
| II | `cdp:eq:C.WH.3` | `{C.WH.3}` |
| II | `cdp:eq:C.WH.4` | `{C.WH.4}` |
| II | `cdp:eq:C.WH.5` | `{C.WH.5}` |
| II | `cdp:eq:C.WH.6` | `{C.WH.6}` |
| II | `cdp:eq:C.WH.7` | `{C.WH.7}` |
| II | `cdp:eq:C.WH.8` | `{C.WH.8}` |
| II | `cdp:eq:C.WH.9` | `{C.WH.9}` |
| II | `cdp:eq:C.WM.1` | `{C.WM.1}` |
| II | `cdp:eq:C.WM.2` | `{C.WM.2}` |
| II | `cdp:eq:C.WM.3` | `{C.WM.3}` |
| II | `cdp:eq:C.WM.4` | `{C.WM.4}` |
| II | `cdp:eq:C.WM.5` | `{C.WM.5}` |
| II | `cdp:eq:C.WM.6` | `{C.WM.6}` |
| II | `cdp:eq:C.WM.7` | `{C.WM.7}` |
| II | `cdp:eq:C.WM.8` | `{C.WM.8}` |
| II | `cdp:eq:C.WM.9` | `{C.WM.9}` |
| II | `cdp:eq:C.WT.1` | `{C.WT.1}` |
| II | `cdp:eq:C.WT.10` | `{C.WT.10}` |
| II | `cdp:eq:C.WT.11` | `{C.WT.11}` |
| II | `cdp:eq:C.WT.12` | `{C.WT.12}` |
| II | `cdp:eq:C.WT.13` | `{C.WT.13}` |
| II | `cdp:eq:C.WT.14` | `{C.WT.14}` |
| II | `cdp:eq:C.WT.15` | `{C.WT.15}` |
| II | `cdp:eq:C.WT.16` | `{C.WT.16}` |
| II | `cdp:eq:C.WT.17` | `{C.WT.17}` |
| II | `cdp:eq:C.WT.18` | `{C.WT.18}` |
| II | `cdp:eq:C.WT.19` | `{C.WT.19}` |
| II | `cdp:eq:C.WT.2` | `{C.WT.2}` |
| II | `cdp:eq:C.WT.20` | `{C.WT.20}` |
| II | `cdp:eq:C.WT.21` | `{C.WT.21}` |
| II | `cdp:eq:C.WT.22` | `{C.WT.22}` |
| II | `cdp:eq:C.WT.23` | `{C.WT.23}` |
| II | `cdp:eq:C.WT.23a` | `{C.WT.23a}` |
| II | `cdp:eq:C.WT.24` | `{C.WT.24}` |
| II | `cdp:eq:C.WT.25` | `{C.WT.25}` |
| II | `cdp:eq:C.WT.26` | `{C.WT.26}` |
| II | `cdp:eq:C.WT.27` | `{C.WT.27}` |
| II | `cdp:eq:C.WT.28` | `{C.WT.28}` |
| II | `cdp:eq:C.WT.29` | `{C.WT.29}` |
| II | `cdp:eq:C.WT.3` | `{C.WT.3}` |
| II | `cdp:eq:C.WT.30` | `{C.WT.30}` |
| II | `cdp:eq:C.WT.31` | `{C.WT.31}` |
| II | `cdp:eq:C.WT.32` | `{C.WT.32}` |
| II | `cdp:eq:C.WT.33` | `{C.WT.33}` |
| II | `cdp:eq:C.WT.34` | `{C.WT.34}` |
| II | `cdp:eq:C.WT.35` | `{C.WT.35}` |
| II | `cdp:eq:C.WT.36` | `{C.WT.36}` |
| II | `cdp:eq:C.WT.37` | `{C.WT.37}` |
| II | `cdp:eq:C.WT.38` | `{C.WT.38}` |
| II | `cdp:eq:C.WT.39` | `{C.WT.39}` |
| II | `cdp:eq:C.WT.4` | `{C.WT.4}` |
| II | `cdp:eq:C.WT.40` | `{C.WT.40}` |
| II | `cdp:eq:C.WT.41` | `{C.WT.41}` |
| II | `cdp:eq:C.WT.42` | `{C.WT.42}` |
| II | `cdp:eq:C.WT.43` | `{C.WT.43}` |
| II | `cdp:eq:C.WT.5` | `{C.WT.5}` |
| II | `cdp:eq:C.WT.6` | `{C.WT.6}` |
| II | `cdp:eq:C.WT.7` | `{C.WT.7}` |
| II | `cdp:eq:C.WT.8` | `{C.WT.8}` |
| II | `cdp:eq:C.WT.9` | `{C.WT.9}` |
| II | `cdp:eq:C.ZC.1` | `{C.ZC.1}` |
| II | `cdp:eq:C.ZC.2` | `{C.ZC.2}` |
| II | `cdp:eq:C.ZC.3` | `{C.ZC.3}` |
| II | `cdp:eq:C.ZC.4` | `{C.ZC.4}` |
| II | `cdp:eq:C.ZC.5` | `{C.ZC.5}` |
| II | `cdp:eq:C.ZC.6` | `{C.ZC.6}` |
| II | `cdp:eq:C.ZC.7` | `{C.ZC.7}` |
| II | `cdp:eq:C.ZC.8` | `{C.ZC.8}` |
| II | `cdp:eq:C.ZC.9` | `{C.ZC.9}` |
| II | `cdp:eq:D.18` | `{D.18}` |
| II | `cdp:eq:D.19` | `{D.19}` |
| II | `cdp:eq:D.20` | `{D.20}` |
| II | `cdp:eq:D.21` | `{D.21}` |
| II | `cdp:eq:D.22` | `{D.22}` |
| II | `cdp:eq:D.23` | `{D.23}` |
| II | `cdp:eq:D.24` | `{D.24}` |
| II | `cdp:eq:D.25` | `{D.25}` |
| II | `cdp:eq:D.26` | `{D.26}` |
| II | `cdp:eq:D.27` | `{D.27}` |
| II | `cdp:eq:D.28` | `{D.28}` |
| II | `cdp:eq:D.29` | `{D.29}` |
| II | `cdp:eq:D.30` | `{D.30}` |
| II | `cdp:eq:D.31` | `{D.31}` |
| II | `cdp:eq:D.32` | `{D.32}` |
| II | `cdp:eq:D.33` | `{D.33}` |
| II | `cdp:eq:D.34` | `{D.34}` |
| II | `cdp:eq:D.35` | `{D.35}` |
| II | `cdp:eq:D.36` | `{D.36}` |
| II | `cdp:eq:D.S.1` | `{D.S.1}` |
| II | `cdp:eq:D.S.2` | `{D.S.2}` |
| II | `cdp:eq:D.S.3` | `{D.S.3}` |
| II | `cdp:eq:D.S.4` | `{D.S.4}` |
| II | `cdp:eq:D.S.5` | `{D.S.5}` |
| II | `cdp:eq:D1` | `{D1}` |
| II | `cdp:eq:D2` | `{D2}` |
| II | `cdp:eq:D3` | `{D3}` |
| II | `cdp:eq:D4` | `{D4}` |
| II | `cdp:eq:D5` | `{D5}` |
| II | `cdp:eq:E-Leray-map` | `3` |
| II | `cdp:eq:E-all-fibres` | `16` |
| II | `cdp:eq:E-graph-pencil` | `15` |
| II | `cdp:eq:E-log-period` | `5` |
| II | `cdp:eq:E-surj-embedding` | `4` |
| II | `cdp:eq:E-theta-general` | `6` |
| II | `cdp:eq:E.16.1` | `{E.16.1}` |
| II | `cdp:eq:E.16.2` | `{E.16.2}` |
| II | `cdp:eq:E.16.3` | `{E.16.3}` |
| II | `cdp:eq:E.19.1` | `{E.19.1}` |
| II | `cdp:eq:E.19.2` | `{E.19.2}` |
| II | `cdp:eq:E13-connection` | `7` |
| II | `cdp:eq:E13-residue` | `8` |
| II | `cdp:eq:E14-canonical` | `10` |
| II | `cdp:eq:E14-elliptic-family` | `9` |
| II | `cdp:eq:E14-jet-map` | `12` |
| II | `cdp:eq:E14-log-coho` | `11` |
| II | `cdp:eq:E15-positive` | `13` |
| II | `cdp:eq:E15-products` | `14` |
| II | `cdp:sec:E` | `2` |
| II | `cdp:st:A.1.1` | `5.1` |
| II | `cdp:st:A.1.2` | `5.4` |
| II | `cdp:st:A.2.1` | `5.2` |
| II | `cdp:st:A.2.2` | `5.3` |
| II | `cdp:st:A.2.3` | `A.2` |
| II | `cdp:st:A.2.4` | `5.5` |
| II | `cdp:st:A.2.5` | `5.6` |
| II | `cdp:st:A.2.6` | `5.7` |
| II | `cdp:st:A.3.1` | `5.11` |
| II | `cdp:st:A.3.2` | `5.12` |
| II | `cdp:st:A.3.3` | `5.13` |
| II | `cdp:st:A.3.4` | `5.14` |
| II | `cdp:st:A.3.5` | `5.15` |
| II | `cdp:st:A.4.1` | `5.16` |
| II | `cdp:st:A.4.2` | `5.17` |
| II | `cdp:st:A.4.3` | `5.18` |
| II | `cdp:st:A.4.4` | `5.19` |
| II | `cdp:st:A.4.5` | `5.20` |
| II | `cdp:st:A.4.6` | `5.21` |
| II | `cdp:st:A.4.7` | `5.22` |
| II | `cdp:st:A.4.8` | `5.23` |
| II | `cdp:st:A.4.9` | `5.24` |
| II | `cdp:st:A.5.1` | `6.1` |
| II | `cdp:st:A.5.10` | `6.14` |
| II | `cdp:st:A.5.11` | `6.7` |
| II | `cdp:st:A.5.12` | `6.8` |
| II | `cdp:st:A.5.13` | `6.9` |
| II | `cdp:st:A.5.14` | `6.13` |
| II | `cdp:st:A.5.15` | `6.16` |
| II | `cdp:st:A.5.16` | `6.20` |
| II | `cdp:st:A.5.17` | `6.17` |
| II | `cdp:st:A.5.18` | `6.18` |
| II | `cdp:st:A.5.19` | `6.19` |
| II | `cdp:st:A.5.2` | `6.2` |
| II | `cdp:st:A.5.20` | `6.15` |
| II | `cdp:st:A.5.21` | `6.21` |
| II | `cdp:st:A.5.3` | `6.3` |
| II | `cdp:st:A.5.4` | `6.4` |
| II | `cdp:st:A.5.5` | `6.10` |
| II | `cdp:st:A.5.6` | `6.5` |
| II | `cdp:st:A.5.7` | `6.11` |
| II | `cdp:st:A.5.8` | `6.12` |
| II | `cdp:st:A.5.9` | `6.6` |
| II | `cdp:st:B1` | `5.8` |
| II | `cdp:st:B2` | `5.9` |
| II | `cdp:st:B3` | `5.10` |
| II | `cdp:st:C.1.1` | `2.1` |
| II | `cdp:st:C.1.2` | `A.3` |
| II | `cdp:st:C.1.3` | `2.2` |
| II | `cdp:st:C.2.CR.1` | `8.2` |
| II | `cdp:st:C.2.CR.2` | `8.3` |
| II | `cdp:st:C.2.CR.3` | `8.4` |
| II | `cdp:st:C.2.CR.4` | `8.5` |
| II | `cdp:st:C.2.CR.5` | `8.6` |
| II | `cdp:st:C.2.CR.6` | `8.7` |
| II | `cdp:st:C.2.D4.1` | `8.23` |
| II | `cdp:st:C.2.D4.2` | `8.24` |
| II | `cdp:st:C.2.D4.3` | `8.25` |
| II | `cdp:st:C.2.G.1` | `13.1` |
| II | `cdp:st:C.2.INT.1` | `8.28` |
| II | `cdp:st:C.2.INT.2` | `8.29` |
| II | `cdp:st:C.2.INT.3` | `8.30` |
| II | `cdp:st:C.2.IRR.1` | `8.10` |
| II | `cdp:st:C.2.MH.1` | `8.31` |
| II | `cdp:st:C.2.MH.2` | `8.32` |
| II | `cdp:st:C.2.MH.3` | `8.33` |
| II | `cdp:st:C.2.MH.4` | `8.34` |
| II | `cdp:st:C.2.NC.1` | `A.4` |
| II | `cdp:st:C.2.NC.2` | `9.1` |
| II | `cdp:st:C.2.NC.3` | `9.2` |
| II | `cdp:st:C.2.NC.4` | `9.3` |
| II | `cdp:st:C.2.NC.5` | `9.4` |
| II | `cdp:st:C.2.RAT.1` | `8.15` |
| II | `cdp:st:C.2.RAT.2` | `8.16` |
| II | `cdp:st:C.2.RAT.3` | `8.17` |
| II | `cdp:st:C.2.RAT.4` | `8.18` |
| II | `cdp:st:C.2.RAT.5` | `8.19` |
| II | `cdp:st:C.2.RAT.6` | `A.6` |
| II | `cdp:st:C.2.RAT.7` | `8.20` |
| II | `cdp:st:C.2.RAT.8` | `8.21` |
| II | `cdp:st:C.2.RAT.9` | `8.22` |
| II | `cdp:st:C.2.UN.1` | `7.1` |
| II | `cdp:st:C.2.UN.10` | `8.9` |
| II | `cdp:st:C.2.UN.11` | `9.9` |
| II | `cdp:st:C.2.UN.12` | `8.27` |
| II | `cdp:st:C.2.UN.13` | `10.3` |
| II | `cdp:st:C.2.UN.14` | `7.5` |
| II | `cdp:st:C.2.UN.15` | `7.6` |
| II | `cdp:st:C.2.UN.16` | `7.7` |
| II | `cdp:st:C.2.UN.17` | `7.8` |
| II | `cdp:st:C.2.UN.18` | `10.4` |
| II | `cdp:st:C.2.UN.19` | `7.9` |
| II | `cdp:st:C.2.UN.2` | `7.2` |
| II | `cdp:st:C.2.UN.20` | `7.10` |
| II | `cdp:st:C.2.UN.21` | `10.5` |
| II | `cdp:st:C.2.UN.22` | `7.11` |
| II | `cdp:st:C.2.UN.23` | `7.12` |
| II | `cdp:st:C.2.UN.24` | `9.10` |
| II | `cdp:st:C.2.UN.25` | `10.6` |
| II | `cdp:st:C.2.UN.26` | `7.13` |
| II | `cdp:st:C.2.UN.27` | `10.7` |
| II | `cdp:st:C.2.UN.28` | `7.14` |
| II | `cdp:st:C.2.UN.29` | `7.15` |
| II | `cdp:st:C.2.UN.3` | `7.3` |
| II | `cdp:st:C.2.UN.30` | `10.8` |
| II | `cdp:st:C.2.UN.31` | `7.16` |
| II | `cdp:st:C.2.UN.32` | `9.11` |
| II | `cdp:st:C.2.UN.33` | `7.17` |
| II | `cdp:st:C.2.UN.34` | `10.9` |
| II | `cdp:st:C.2.UN.35` | `10.10` |
| II | `cdp:st:C.2.UN.36` | `7.18` |
| II | `cdp:st:C.2.UN.37` | `10.11` |
| II | `cdp:st:C.2.UN.38` | `7.19` |
| II | `cdp:st:C.2.UN.39` | `7.20` |
| II | `cdp:st:C.2.UN.4` | `7.4` |
| II | `cdp:st:C.2.UN.40` | `11.1` |
| II | `cdp:st:C.2.UN.41` | `10.12` |
| II | `cdp:st:C.2.UN.42` | `10.13` |
| II | `cdp:st:C.2.UN.43` | `10.14` |
| II | `cdp:st:C.2.UN.44` | `7.21` |
| II | `cdp:st:C.2.UN.45` | `10.15` |
| II | `cdp:st:C.2.UN.46` | `11.2` |
| II | `cdp:st:C.2.UN.47` | `7.22` |
| II | `cdp:st:C.2.UN.48` | `11.3` |
| II | `cdp:st:C.2.UN.49` | `11.4` |
| II | `cdp:st:C.2.UN.5` | `8.1` |
| II | `cdp:st:C.2.UN.50` | `11.5` |
| II | `cdp:st:C.2.UN.51` | `11.6` |
| II | `cdp:st:C.2.UN.52` | `11.7` |
| II | `cdp:st:C.2.UN.53` | `11.8` |
| II | `cdp:st:C.2.UN.54` | `11.9` |
| II | `cdp:st:C.2.UN.55` | `11.10` |
| II | `cdp:st:C.2.UN.56` | `11.11` |
| II | `cdp:st:C.2.UN.57` | `11.12` |
| II | `cdp:st:C.2.UN.58` | `11.13` |
| II | `cdp:st:C.2.UN.59` | `11.14` |
| II | `cdp:st:C.2.UN.6` | `10.1` |
| II | `cdp:st:C.2.UN.60` | `11.15` |
| II | `cdp:st:C.2.UN.61` | `11.16` |
| II | `cdp:st:C.2.UN.62` | `11.17` |
| II | `cdp:st:C.2.UN.63` | `11.18` |
| II | `cdp:st:C.2.UN.64` | `9.12` |
| II | `cdp:st:C.2.UN.65` | `9.13` |
| II | `cdp:st:C.2.UN.66` | `9.14` |
| II | `cdp:st:C.2.UN.67` | `9.15` |
| II | `cdp:st:C.2.UN.68` | `9.16` |
| II | `cdp:st:C.2.UN.69` | `12.1` |
| II | `cdp:st:C.2.UN.7` | `8.26` |
| II | `cdp:st:C.2.UN.70` | `12.2` |
| II | `cdp:st:C.2.UN.71` | `12.3` |
| II | `cdp:st:C.2.UN.72` | `12.16` |
| II | `cdp:st:C.2.UN.73` | `12.4` |
| II | `cdp:st:C.2.UN.74` | `12.6` |
| II | `cdp:st:C.2.UN.75` | `12.7` |
| II | `cdp:st:C.2.UN.76` | `12.5` |
| II | `cdp:st:C.2.UN.77` | `12.8` |
| II | `cdp:st:C.2.UN.78` | `12.15` |
| II | `cdp:st:C.2.UN.79` | `12.9` |
| II | `cdp:st:C.2.UN.8` | `10.2` |
| II | `cdp:st:C.2.UN.80` | `12.10` |
| II | `cdp:st:C.2.UN.81` | `12.11` |
| II | `cdp:st:C.2.UN.82` | `12.12` |
| II | `cdp:st:C.2.UN.83` | `12.13` |
| II | `cdp:st:C.2.UN.84` | `12.14` |
| II | `cdp:st:C.2.UN.85` | `12.17` |
| II | `cdp:st:C.2.UN.86` | `12.18` |
| II | `cdp:st:C.2.UN.9` | `8.8` |
| II | `cdp:st:C.2.VII.1` | `8.11` |
| II | `cdp:st:C.2.VII.2` | `8.12` |
| II | `cdp:st:C.2.VII.3` | `8.13` |
| II | `cdp:st:C.2.VII.4` | `8.14` |
| II | `cdp:st:C.3.1` | `4.9` |
| II | `cdp:st:C.3.10` | `4.7` |
| II | `cdp:st:C.3.11` | `4.10` |
| II | `cdp:st:C.3.12` | `4.8` |
| II | `cdp:st:C.3.2` | `4.1` |
| II | `cdp:st:C.3.3` | `4.2` |
| II | `cdp:st:C.3.4` | `4.3` |
| II | `cdp:st:C.3.5` | `4.11` |
| II | `cdp:st:C.3.6` | `4.12` |
| II | `cdp:st:C.3.7` | `4.4` |
| II | `cdp:st:C.3.8` | `4.5` |
| II | `cdp:st:C.3.9` | `4.6` |
| II | `cdp:st:C2a` | `9.5` |
| II | `cdp:st:C2b` | `9.6` |
| II | `cdp:st:C2c` | `9.7` |
| II | `cdp:st:C2d` | `9.8` |
| II | `cdp:st:C4a` | `13.2` |
| II | `cdp:st:C4b` | `13.3` |
| II | `cdp:st:C4c` | `13.4` |
| II | `cdp:st:C4d` | `13.5` |
| II | `cdp:st:C4e` | `13.6` |
| II | `cdp:st:C4f` | `13.7` |
| II | `cdp:st:C4g` | `13.8` |
| II | `cdp:st:C5a` | `13.9` |
| II | `cdp:st:C5b` | `13.10` |
| II | `cdp:st:C5c` | `13.11` |
| II | `cdp:st:D.1.1` | `A.1` |
| II | `cdp:st:D.1.10` | `3.7` |
| II | `cdp:st:D.1.11` | `3.8` |
| II | `cdp:st:D.1.12` | `3.9` |
| II | `cdp:st:D.1.13` | `3.11` |
| II | `cdp:st:D.1.15` | `3.12` |
| II | `cdp:st:D.1.2` | `3.1` |
| II | `cdp:st:D.1.3` | `A.5` |
| II | `cdp:st:D.1.4` | `3.10` |
| II | `cdp:st:D.1.5` | `3.2` |
| II | `cdp:st:D.1.6` | `3.3` |
| II | `cdp:st:D.1.7` | `3.4` |
| II | `cdp:st:D.1.8` | `3.5` |
| II | `cdp:st:D.1.9` | `3.6` |
| II | `cdp:st:D.2.1` | `14.1` |
| II | `cdp:st:D.2.2` | `14.8` |
| II | `cdp:st:D.2.3` | `14.2` |
| II | `cdp:st:D.2.4` | `14.3` |
| II | `cdp:st:D.2.5` | `14.4` |
| II | `cdp:st:D.2.6` | `14.5` |
| II | `cdp:st:D.2.7` | `14.6` |
| II | `cdp:st:D.2.8` | `14.7` |
| II | `cdp:st:E1` | `2.3` |
| II | `cdp:st:E10` | `15.5` |
| II | `cdp:st:E11` | `15.6` |
| II | `cdp:st:E12` | `15.7` |
| II | `cdp:st:E13` | `15.8` |
| II | `cdp:st:E14` | `15.9` |
| II | `cdp:st:E15` | `15.10` |
| II | `cdp:st:E16` | `15.11` |
| II | `cdp:st:E17` | `15.12` |
| II | `cdp:st:E18` | `15.13` |
| II | `cdp:st:E19` | `A.10` |
| II | `cdp:st:E2` | `A.7` |
| II | `cdp:st:E3` | `A.8` |
| II | `cdp:st:E4` | `A.9` |
| II | `cdp:st:E5` | `15.1` |
| II | `cdp:st:E6` | `15.2` |
| II | `cdp:st:E7` | `15.3` |
| II | `cdp:st:E8` | `15.4` |
| II | `inv:E1.1` | `17.1` |
| II | `inv:E2.1` | `A.11` |
| II | `inv:E2.2` | `17.2` |
| II | `inv:E2.3` | `D.1` |
| II | `inv:E2.4` | `17.3` |
| II | `inv:wb:eq:9.19` | `{WBAPII.9.19}` |
| II | `inv:wb:eq:9.20` | `{WBAPII.9.20}` |
| II | `inv:wb:eq:9.21` | `{WBAPII.9.21}` |
| II | `inv:wb:eq:9.22` | `{WBAPII.9.22}` |
| II | `inv:wb:eq:9.23` | `{WBAPII.9.23}` |
| II | `inv:wb:eq:9.24` | `{WBAPII.9.24}` |
| II | `inv:wb:eq:9.25` | `{WBAPII.9.25}` |
| II | `inv:wb:uniform-nontorsion-provenance` | `A.13` |
| II | `invII:eq:E.1` | `{E.1}` |
| II | `invII:eq:E.2` | `{E.2}` |
| II | `invII:eq:E.3` | `{E.3}` |
| II | `invII:eq:E.4a` | `{E.4a}` |
| II | `invII:eq:E.5` | `{E.5}` |
| II | `invII:eq:E.6` | `{E.6}` |
| II | `invII:eq:E.7` | `{E.7}` |
| II | `push:src:E.2.10` | `16.9` |
| II | `push:src:E.2.11` | `16.10` |
| II | `push:src:E.2.12` | `16.12` |
| II | `push:src:E.2.13` | `16.14` |
| II | `push:src:E.2.14` | `16.16` |
| II | `push:src:E.2.15` | `16.18` |
| II | `push:src:E.2.16` | `16.20` |
| II | `push:src:E.2.17` | `16.21` |
| II | `push:src:E.2.18` | `16.23` |
| II | `push:src:E.2.19` | `16.24` |
| II | `push:src:E.2.20` | `16.25` |
| II | `push:src:E.2.21` | `16.27` |
| II | `push:src:E.2.22` | `16.29` |
| II | `push:src:E.2.23` | `16.30` |
| II | `push:src:E.2.24` | `16.31` |
| II | `push:src:E.2.4` | `16.1` |
| II | `push:src:E.2.5` | `16.2` |
| II | `push:src:E.2.6` | `16.3` |
| II | `push:src:E.2.7` | `16.5` |
| II | `push:src:E.2.8` | `16.7` |
| II | `push:src:E.2.9` | `16.8` |
| II | `push:src:E.5.1` | `16.32` |
| II | `push:src:E.5.2` | `16.33` |
| II | `push:src:E.5.3` | `16.34` |
| II | `sec:II:01` | `2` |
| II | `sec:II:02` | `3` |
| II | `sec:II:03` | `4` |
| II | `sec:II:04` | `5` |
| II | `sec:II:05` | `6` |
| II | `sec:II:06` | `7` |
| II | `sec:II:07` | `8` |
| II | `sec:II:08` | `9` |
| II | `sec:II:09` | `10` |
| II | `sec:II:10` | `11` |
| II | `sec:II:11` | `12` |
| II | `sec:II:12` | `13` |
| II | `sec:II:13` | `14` |
| II | `sec:II:14` | `15` |
| II | `sec:II:combs` | `17` |
| II | `sec:II:conventions` | `1` |
| II | `sec:II:push-stability` | `16` |
| II | `wb:thm:uniform-nontorsion-audit` | `A.12` |
| II | `wbII:cor:candidate-conductor-actual` | `B.27` |
| II | `wbII:cor:candidate-pic0-route` | `B.24` |
| II | `wbII:cor:corrected-cdp-relative` | `B.31` |
| II | `wbII:cor:normal-crossing-kernel` | `B.3` |
| II | `wbII:cor:relative` | `B.31` |
| II | `wbII:cor:surface-top-base-change` | `B.11` |
| II | `wbII:eq:CN:2.2` | `{W.145}` |
| II | `wbII:eq:CN:4.3` | `{W.160}` |
| II | `wbII:eq:CN:4.4` | `{W.161}` |
| II | `wbII:eq:CN:4.5` | `{W.163}` |
| II | `wbII:eq:CN:4.5a` | `{W.162}` |
| II | `wbII:eq:CN:4.6` | `{W.164}` |
| II | `wbII:eq:CN:4.7` | `{W.165}` |
| II | `wbII:eq:CN:4.8` | `{W.166}` |
| II | `wbII:eq:CN:4.9` | `{W.167}` |
| II | `wbII:eq:CN:5.2` | `{W.169}` |
| II | `wbII:eq:CN:6.1` | `{W.176}` |
| II | `wbII:eq:CN:6.2` | `{W.177}` |
| II | `wbII:eq:CN:6.3` | `{W.178}` |
| II | `wbII:eq:CN:6.4` | `{W.179}` |
| II | `wbII:eq:W:5.1` | `{W.1}` |
| II | `wbII:eq:W:5.10` | `{W.10}` |
| II | `wbII:eq:W:5.11` | `{W.11}` |
| II | `wbII:eq:W:5.15a` | `{W.12}` |
| II | `wbII:eq:W:5.16` | `{W.13}` |
| II | `wbII:eq:W:5.17` | `{W.14}` |
| II | `wbII:eq:W:5.17-A1` | `{W.93}` |
| II | `wbII:eq:W:5.17-A10` | `{W.102}` |
| II | `wbII:eq:W:5.17-A11` | `{W.103}` |
| II | `wbII:eq:W:5.17-A12` | `{W.104}` |
| II | `wbII:eq:W:5.17-A13` | `{W.105}` |
| II | `wbII:eq:W:5.17-A14` | `{W.106}` |
| II | `wbII:eq:W:5.17-A14a` | `{W.107}` |
| II | `wbII:eq:W:5.17-A14c` | `{W.108}` |
| II | `wbII:eq:W:5.17-A14d` | `{W.109}` |
| II | `wbII:eq:W:5.17-A14e` | `{W.110}` |
| II | `wbII:eq:W:5.17-A14f` | `{W.111}` |
| II | `wbII:eq:W:5.17-A15` | `{W.112}` |
| II | `wbII:eq:W:5.17-A16` | `{W.113}` |
| II | `wbII:eq:W:5.17-A17` | `{W.114}` |
| II | `wbII:eq:W:5.17-A18` | `{W.115}` |
| II | `wbII:eq:W:5.17-A19` | `{W.116}` |
| II | `wbII:eq:W:5.17-A19a` | `{W.117}` |
| II | `wbII:eq:W:5.17-A19b` | `{W.118}` |
| II | `wbII:eq:W:5.17-A19c` | `{W.119}` |
| II | `wbII:eq:W:5.17-A2` | `{W.94}` |
| II | `wbII:eq:W:5.17-A20` | `{W.120}` |
| II | `wbII:eq:W:5.17-A21` | `{W.121}` |
| II | `wbII:eq:W:5.17-A22` | `{W.122}` |
| II | `wbII:eq:W:5.17-A23` | `{W.123}` |
| II | `wbII:eq:W:5.17-A24` | `{W.124}` |
| II | `wbII:eq:W:5.17-A25` | `{W.125}` |
| II | `wbII:eq:W:5.17-A26` | `{W.126}` |
| II | `wbII:eq:W:5.17-A27` | `{W.127}` |
| II | `wbII:eq:W:5.17-A28` | `{W.128}` |
| II | `wbII:eq:W:5.17-A29` | `{W.129}` |
| II | `wbII:eq:W:5.17-A3` | `{W.95}` |
| II | `wbII:eq:W:5.17-A30` | `{W.130}` |
| II | `wbII:eq:W:5.17-A31` | `{W.131}` |
| II | `wbII:eq:W:5.17-A32` | `{W.132}` |
| II | `wbII:eq:W:5.17-A33` | `{W.133}` |
| II | `wbII:eq:W:5.17-A34` | `{W.134}` |
| II | `wbII:eq:W:5.17-A34a` | `{W.135}` |
| II | `wbII:eq:W:5.17-A34b` | `{W.136}` |
| II | `wbII:eq:W:5.17-A34c` | `{W.137}` |
| II | `wbII:eq:W:5.17-A35` | `{W.138}` |
| II | `wbII:eq:W:5.17-A36` | `{W.139}` |
| II | `wbII:eq:W:5.17-A37` | `{W.140}` |
| II | `wbII:eq:W:5.17-A38` | `{W.141}` |
| II | `wbII:eq:W:5.17-A4` | `{W.96}` |
| II | `wbII:eq:W:5.17-A5` | `{W.97}` |
| II | `wbII:eq:W:5.17-A6` | `{W.98}` |
| II | `wbII:eq:W:5.17-A7` | `{W.99}` |
| II | `wbII:eq:W:5.17-A8` | `{W.100}` |
| II | `wbII:eq:W:5.17-A9` | `{W.101}` |
| II | `wbII:eq:W:5.17-T` | `{W.16}` |
| II | `wbII:eq:W:5.17-U` | `{W.17}` |
| II | `wbII:eq:W:5.17-V` | `{W.15}` |
| II | `wbII:eq:W:5.17a` | `{W.18}` |
| II | `wbII:eq:W:5.17aa` | `{W.68}` |
| II | `wbII:eq:W:5.17ab` | `{W.69}` |
| II | `wbII:eq:W:5.17ac` | `{W.70}` |
| II | `wbII:eq:W:5.17ad` | `{W.71}` |
| II | `wbII:eq:W:5.17ae` | `{W.72}` |
| II | `wbII:eq:W:5.17af` | `{W.73}` |
| II | `wbII:eq:W:5.17ag` | `{W.74}` |
| II | `wbII:eq:W:5.17ah` | `{W.75}` |
| II | `wbII:eq:W:5.17ai` | `{W.76}` |
| II | `wbII:eq:W:5.17aj` | `{W.77}` |
| II | `wbII:eq:W:5.17ak` | `{W.78}` |
| II | `wbII:eq:W:5.17al` | `{W.79}` |
| II | `wbII:eq:W:5.17am` | `{W.80}` |
| II | `wbII:eq:W:5.17an` | `{W.81}` |
| II | `wbII:eq:W:5.17ao` | `{W.82}` |
| II | `wbII:eq:W:5.17ap` | `{W.83}` |
| II | `wbII:eq:W:5.17aq` | `{W.84}` |
| II | `wbII:eq:W:5.17ar` | `{W.85}` |
| II | `wbII:eq:W:5.17as` | `{W.86}` |
| II | `wbII:eq:W:5.17at` | `{W.87}` |
| II | `wbII:eq:W:5.17au` | `{W.88}` |
| II | `wbII:eq:W:5.17av` | `{W.89}` |
| II | `wbII:eq:W:5.17aw` | `{W.90}` |
| II | `wbII:eq:W:5.17ax` | `{W.91}` |
| II | `wbII:eq:W:5.17ay` | `{W.92}` |
| II | `wbII:eq:W:5.17b` | `{W.19}` |
| II | `wbII:eq:W:5.17c` | `{W.20}` |
| II | `wbII:eq:W:5.17d` | `{W.21}` |
| II | `wbII:eq:W:5.17e` | `{W.22}` |
| II | `wbII:eq:W:5.17f` | `{W.44}` |
| II | `wbII:eq:W:5.17g` | `{W.23}` |
| II | `wbII:eq:W:5.17h` | `{W.24}` |
| II | `wbII:eq:W:5.17i` | `{W.25}` |
| II | `wbII:eq:W:5.17j` | `{W.27}` |
| II | `wbII:eq:W:5.17j'` | `{W.26}` |
| II | `wbII:eq:W:5.17k` | `{W.28}` |
| II | `wbII:eq:W:5.17l` | `{W.29}` |
| II | `wbII:eq:W:5.17l'` | `{W.30}` |
| II | `wbII:eq:W:5.17l''` | `{W.31}` |
| II | `wbII:eq:W:5.17l'''` | `{W.32}` |
| II | `wbII:eq:W:5.17m` | `{W.33}` |
| II | `wbII:eq:W:5.17m'` | `{W.34}` |
| II | `wbII:eq:W:5.17m''` | `{W.35}` |
| II | `wbII:eq:W:5.17n` | `{W.36}` |
| II | `wbII:eq:W:5.17o` | `{W.37}` |
| II | `wbII:eq:W:5.17p` | `{W.38}` |
| II | `wbII:eq:W:5.17p'` | `{W.40}` |
| II | `wbII:eq:W:5.17p0` | `{W.39}` |
| II | `wbII:eq:W:5.17q` | `{W.41}` |
| II | `wbII:eq:W:5.17r` | `{W.42}` |
| II | `wbII:eq:W:5.17s` | `{W.43}` |
| II | `wbII:eq:W:5.17t` | `{W.61}` |
| II | `wbII:eq:W:5.17u` | `{W.62}` |
| II | `wbII:eq:W:5.17v` | `{W.63}` |
| II | `wbII:eq:W:5.17w` | `{W.64}` |
| II | `wbII:eq:W:5.17x` | `{W.65}` |
| II | `wbII:eq:W:5.17y` | `{W.66}` |
| II | `wbII:eq:W:5.17z` | `{W.67}` |
| II | `wbII:eq:W:5.18` | `{W.45}` |
| II | `wbII:eq:W:5.19` | `{W.46}` |
| II | `wbII:eq:W:5.2` | `{W.2}` |
| II | `wbII:eq:W:5.20` | `{W.47}` |
| II | `wbII:eq:W:5.23` | `{W.50}` |
| II | `wbII:eq:W:5.24` | `{W.51}` |
| II | `wbII:eq:W:5.25` | `{W.52}` |
| II | `wbII:eq:W:5.26` | `{W.53}` |
| II | `wbII:eq:W:5.27` | `{W.54}` |
| II | `wbII:eq:W:5.28` | `{W.55}` |
| II | `wbII:eq:W:5.29` | `{W.56}` |
| II | `wbII:eq:W:5.3` | `{W.3}` |
| II | `wbII:eq:W:5.30` | `{W.57}` |
| II | `wbII:eq:W:5.31` | `{W.58}` |
| II | `wbII:eq:W:5.32` | `{W.59}` |
| II | `wbII:eq:W:5.33` | `{W.60}` |
| II | `wbII:eq:W:5.4` | `{W.4}` |
| II | `wbII:eq:W:5.5` | `{W.5}` |
| II | `wbII:eq:W:5.6` | `{W.6}` |
| II | `wbII:eq:W:5.7` | `{W.7}` |
| II | `wbII:eq:W:5.8` | `{W.8}` |
| II | `wbII:eq:W:5.9` | `{W.9}` |
| II | `wbII:eq:analytic-factor-horizontal-winding` | `19` |
| II | `wbII:eq:analytic-residual-descent-factor` | `18` |
| II | `wbII:eq:analytic-toric-open-directions` | `17` |
| II | `wbII:lem:analytic-support-specialization` | `B.22` |
| II | `wbII:lem:cdp-generic-endpoints` | `B.29` |
| II | `wbII:lem:conductor` | `5.3` |
| II | `wbII:lem:conductor-square` | `5.3` |
| II | `wbII:lem:conormal` | `5.1` |
| II | `wbII:lem:conormal-injective` | `5.1` |
| II | `wbII:lem:curve-flatness` | `B.9` |
| II | `wbII:lem:extending-gluing` | `B.5` |
| II | `wbII:lem:generic-endpoints` | `B.28` |
| II | `wbII:lem:gluing-bundle` | `B.4` |
| II | `wbII:lem:picard-crossed-defect` | `B.15` |
| II | `wbII:lem:picard-cusp-defect` | `B.17` |
| II | `wbII:lem:picard-finite-norm` | `B.16` |
| II | `wbII:lem:torsion-identification` | `B.1` |
| II | `wbII:prop:all-pic-restriction` | `B.13` |
| II | `wbII:prop:analytic-ah-boundary` | `B.21` |
| II | `wbII:prop:analytic-base-change` | `B.10` |
| II | `wbII:prop:cartier-duality-absolute` | `B.8` |
| II | `wbII:prop:conductor` | `B.2` |
| II | `wbII:prop:conductor-differential` | `B.2` |
| II | `wbII:prop:criterion` | `5.1` |
| II | `wbII:prop:direct-boundary-picard` | `B.18` |
| II | `wbII:prop:family-geometry` | `5.8` |
| II | `wbII:prop:filtration` | `5.1` |
| II | `wbII:prop:leray-edge-restriction` | `B.14` |
| II | `wbII:prop:local-cusp-picard-obstruction` | `B.19` |
| II | `wbII:prop:missing-cotangent-filtration` | `5.1` |
| II | `wbII:prop:missing-global-section-criterion` | `5.1` |
| II | `wbII:prop:nodal-counterexample` | `5.8` |
| II | `wbII:prop:pic0-pullback` | `B.12` |
| II | `wbII:prop:relative-local` | `B.35` |
| II | `wbII:rem:local-cusp-picard-obstruction` | `B.20` |
| II | `wbII:rem:relative-local-scope` | `B.36` |
| II | `wbII:rem:scope` | `B.6` |
| II | `wbII:sec:working-supplement` | `B` |
| II | `wbII:subsec:analytic-all-picard` | `B.10` |
| II | `wbII:subsec:local-cusp-picard-obstruction` | `B.9` |
| II | `wbII:test:cdp-comparison` | `B.34` |
| II | `wbII:thm:analytic-all-picard` | `B.23` |
| II | `wbII:thm:candidate-conductor` | `B.26` |
| II | `wbII:thm:cartier-duality` | `B.7` |
| II | `wbII:thm:corrected-cdp-fibrewise` | `B.32` |
| II | `wbII:thm:corrected-cdp-global` | `B.30` |
| II | `wbII:thm:corrected-global` | `B.30` |
| II | `wbII:thm:nodal-test` | `5.8` |
| III | `app:III:known` | `A` |
| III | `app:III:programs` | `AK` |
| III | `app:III:provenance` | `AL` |
| III | `app:III:result-index` | `AJ` |
| III | `courseIII:actual-degree8:1` | `X.1` |
| III | `courseIII:actual-degree8:2` | `X.2` |
| III | `courseIII:actual-degree8:3` | `X.3` |
| III | `courseIII:actual-degree8:4` | `X.4` |
| III | `courseIII:actual-degree8:5` | `X.5` |
| III | `courseIII:actual-degree8:6` | `X.6` |
| III | `courseIII:actual-degree8:7` | `X.7` |
| III | `courseIII:actual-degree8:8` | `X.8` |
| III | `courseIII:actual-degree8:9.1` | `X.9.1` |
| III | `courseIII:actual-degree8:9.2` | `X.9.2` |
| III | `courseIII:actual-resolution:1` | `Y.1` |
| III | `courseIII:actual-resolution:2` | `Y.2` |
| III | `courseIII:actual-resolution:3` | `Y.3` |
| III | `courseIII:actual-resolution:4` | `Y.4` |
| III | `courseIII:actual-resolution:5` | `Y.5` |
| III | `courseIII:actual-resolution:6` | `Y.6` |
| III | `courseIII:actual-resolution:7` | `Y.7` |
| III | `courseIII:actual-resolution:8.1` | `Y.8.1` |
| III | `courseIII:actual-resolution:8.2` | `Y.8.2` |
| III | `courseIII:adams-arithmetic:1` | `AD.1` |
| III | `courseIII:adams-arithmetic:2` | `AD.2` |
| III | `courseIII:adams-arithmetic:3` | `AD.3` |
| III | `courseIII:adams-arithmetic:4` | `AD.4` |
| III | `courseIII:adams-arithmetic:5` | `AD.5` |
| III | `courseIII:adams-arithmetic:6` | `AD.6` |
| III | `courseIII:adams-arithmetic:7` | `AD.7` |
| III | `courseIII:adams-arithmetic:8` | `AD.8` |
| III | `courseIII:adams-arithmetic:9` | `AD.9` |
| III | `courseIII:adams-tower:1` | `AC.1` |
| III | `courseIII:adams-tower:10` | `AC.10` |
| III | `courseIII:adams-tower:11` | `AC.11` |
| III | `courseIII:adams-tower:2` | `AC.2` |
| III | `courseIII:adams-tower:3` | `AC.3` |
| III | `courseIII:adams-tower:4` | `AC.4` |
| III | `courseIII:adams-tower:5` | `AC.5` |
| III | `courseIII:adams-tower:6` | `AC.6` |
| III | `courseIII:adams-tower:7.1` | `AC.7.1` |
| III | `courseIII:adams-tower:7.2` | `AC.7.2` |
| III | `courseIII:adams-tower:8` | `AC.8` |
| III | `courseIII:adams-tower:9` | `AC.9` |
| III | `courseIII:almost-complex-structures-and-integrability:analytic-estimates` | `AI.8` |
| III | `courseIII:almost-complex-structures-and-integrability:analytic-flows` | `AI.9` |
| III | `courseIII:almost-complex-structures-and-integrability:associator-and-kernel` | `AI.4` |
| III | `courseIII:almost-complex-structures-and-integrability:charts-and-tensors` | `AI.1` |
| III | `courseIII:almost-complex-structures-and-integrability:coordinate-equation` | `AI.6` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:1.1` | `2027` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:1.10` | `2036` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:1.2` | `2028` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:1.3` | `2029` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:1.4` | `2030` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:1.5` | `2031` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:1.6` | `2032` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:1.7` | `2033` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:1.8` | `2034` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:1.9` | `2035` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:10.1` | `2114` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:10.10` | `2123` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:10.11` | `2124` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:10.12` | `2125` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:10.13` | `2126` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:10.14` | `2127` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:10.15` | `2128` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:10.16` | `2129` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:10.17` | `2130` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:10.18` | `2131` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:10.2` | `2115` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:10.3` | `2116` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:10.4` | `2117` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:10.5` | `2118` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:10.6` | `2119` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:10.7` | `2120` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:10.8` | `2121` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:10.9` | `2122` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:11.1` | `2132` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:11.2` | `2133` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:11.3` | `2134` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:11.4` | `2135` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:11.5` | `2136` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:11.6` | `2137` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:2.1` | `2037` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:2.10` | `2046` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:2.11` | `2047` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:2.12` | `2048` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:2.13` | `2049` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:2.14` | `2050` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:2.15` | `2051` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:2.16` | `2052` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:2.17` | `2053` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:2.2` | `2038` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:2.3` | `2039` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:2.4` | `2040` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:2.5` | `2041` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:2.6` | `2042` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:2.7` | `2043` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:2.8` | `2044` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:2.9` | `2045` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:3.1` | `2054` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:3.2` | `2055` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:3.3` | `2056` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:3.4` | `2057` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:3.5` | `2058` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:3.6` | `2059` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:3.7` | `2060` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:3.8` | `2061` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:3.9` | `2062` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:4.1` | `2063` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:4.10` | `2072` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:4.11` | `2073` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:4.12` | `2074` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:4.2` | `2064` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:4.3` | `2065` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:4.4` | `2066` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:4.5` | `2067` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:4.6` | `2068` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:4.7` | `2069` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:4.8` | `2070` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:4.9` | `2071` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:5.1` | `2075` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:5.2` | `2076` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:5.3` | `2077` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:6.1` | `2078` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:6.2` | `2079` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:6.3` | `2080` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:6.4` | `2081` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:6.5` | `2082` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:6.6` | `2083` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:6.7` | `2084` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:6.8` | `2085` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:6.9` | `2086` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:7.1` | `2087` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:7.2` | `2088` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:7.3` | `2089` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:7.4` | `2090` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:7.5` | `2091` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:7.6` | `2092` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:7.7` | `2093` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:7.8` | `2094` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:7.9` | `2095` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:8.1` | `2096` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:8.10` | `2105` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:8.11` | `2106` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:8.12` | `2107` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:8.13` | `2108` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:8.2` | `2097` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:8.3` | `2098` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:8.4` | `2099` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:8.5` | `2100` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:8.6` | `2101` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:8.7` | `2102` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:8.8` | `2103` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:8.9` | `2104` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:9.1` | `2109` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:9.2` | `2110` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:9.3` | `2111` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:9.4` | `2112` |
| III | `courseIII:almost-complex-structures-and-integrability:eq:9.5` | `2113` |
| III | `courseIII:almost-complex-structures-and-integrability:exercise-1` | `AI.11.1` |
| III | `courseIII:almost-complex-structures-and-integrability:exercise-2` | `AI.11.2` |
| III | `courseIII:almost-complex-structures-and-integrability:exercise-3` | `AI.11.3` |
| III | `courseIII:almost-complex-structures-and-integrability:exercise-4` | `AI.11.4` |
| III | `courseIII:almost-complex-structures-and-integrability:exercise-5` | `AI.11.5` |
| III | `courseIII:almost-complex-structures-and-integrability:exercise-6` | `AI.11.6` |
| III | `courseIII:almost-complex-structures-and-integrability:integrability-exercises` | `AI.11` |
| III | `courseIII:almost-complex-structures-and-integrability:integrability-map-figure-style-min-width:900px-max-width:none-width:900px` | `AI.9` |
| III | `courseIII:almost-complex-structures-and-integrability:octonion-circle-figure-style-min-width:900px-max-width:none-width:900px` | `AI.4` |
| III | `courseIII:almost-complex-structures-and-integrability:octonion-comparison` | `AI.2` |
| III | `courseIII:almost-complex-structures-and-integrability:periodic-gauge` | `AI.7` |
| III | `courseIII:almost-complex-structures-and-integrability:round-sphere-obstruction` | `AI.3` |
| III | `courseIII:almost-complex-structures-and-integrability:section` | `AI` |
| III | `courseIII:almost-complex-structures-and-integrability:section-1` | `AI.1` |
| III | `courseIII:almost-complex-structures-and-integrability:section-10` | `AI.10` |
| III | `courseIII:almost-complex-structures-and-integrability:section-10.1` | `AI.10.1` |
| III | `courseIII:almost-complex-structures-and-integrability:section-10.2` | `AI.10.2` |
| III | `courseIII:almost-complex-structures-and-integrability:section-10.3` | `AI.10.3` |
| III | `courseIII:almost-complex-structures-and-integrability:section-10.4` | `AI.10.4` |
| III | `courseIII:almost-complex-structures-and-integrability:section-10.5` | `AI.10.5` |
| III | `courseIII:almost-complex-structures-and-integrability:section-11` | `AI.11` |
| III | `courseIII:almost-complex-structures-and-integrability:section-2` | `AI.2` |
| III | `courseIII:almost-complex-structures-and-integrability:section-3` | `AI.3` |
| III | `courseIII:almost-complex-structures-and-integrability:section-4` | `AI.4` |
| III | `courseIII:almost-complex-structures-and-integrability:section-5` | `AI.5` |
| III | `courseIII:almost-complex-structures-and-integrability:section-6` | `AI.6` |
| III | `courseIII:almost-complex-structures-and-integrability:section-7` | `AI.7` |
| III | `courseIII:almost-complex-structures-and-integrability:section-8` | `AI.8` |
| III | `courseIII:almost-complex-structures-and-integrability:section-8.1` | `AI.8.1` |
| III | `courseIII:almost-complex-structures-and-integrability:section-8.2` | `AI.8.2` |
| III | `courseIII:almost-complex-structures-and-integrability:section-8.3` | `AI.8.3` |
| III | `courseIII:almost-complex-structures-and-integrability:section-9` | `AI.9` |
| III | `courseIII:almost-complex-structures-and-integrability:source-theorem-9.1` | `AI.1` |
| III | `courseIII:almost-complex-structures-and-integrability:sphere-classification` | `AI.10` |
| III | `courseIII:almost-complex-structures-and-integrability:transport-of-structures` | `AI.5` |
| III | `courseIII:belt-complement:1` | `P.1` |
| III | `courseIII:belt-complement:2` | `P.2` |
| III | `courseIII:belt-complement:3` | `P.3` |
| III | `courseIII:belt-complement:4` | `P.4` |
| III | `courseIII:belt-complement:5` | `P.5` |
| III | `courseIII:belt-complement:6` | `P.6` |
| III | `courseIII:belt-complement:7` | `P.7` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:belt-complement-diagram` | `P.3` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:belt-complement-map` | `P.1` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:belt-exercises` | `P.4` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:belt-homotopy` | `P.3` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:belt-sources` | `P.8` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:core-avoidance` | `P.2` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:1.1` | `789` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:1.10` | `799` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:1.11` | `800` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:1.12` | `801` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:1.13` | `802` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:1.13a` | `803` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:1.13b` | `804` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:1.14` | `805` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:1.15` | `806` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:1.16` | `807` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:1.17` | `808` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:1.18` | `809` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:1.2` | `790` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:1.3` | `791` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:1.4` | `792` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:1.5` | `793` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:1.6` | `794` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:1.7` | `795` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:1.8` | `796` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:1.8a` | `797` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:1.9` | `798` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:2.1` | `810` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:2.10` | `820` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:2.11` | `821` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:2.2` | `811` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:2.3` | `812` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:2.4` | `813` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:2.5` | `814` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:2.6` | `815` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:2.7` | `816` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:2.7a` | `817` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:2.8` | `818` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:2.9` | `819` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:3.1` | `822` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:3.2` | `823` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:3.3` | `824` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:3.4` | `825` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:3.5` | `826` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:4.1` | `827` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:4.2` | `828` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:4.3` | `829` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:4.4` | `830` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:4.5` | `831` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:4.6` | `832` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:5.1` | `833` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:5.10` | `842` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:5.11` | `843` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:5.12` | `844` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:5.13` | `845` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:5.14` | `846` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:5.2` | `834` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:5.3` | `835` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:5.4` | `836` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:5.5` | `837` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:5.6` | `838` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:5.7` | `839` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:5.8` | `840` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:5.9` | `841` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:6.1` | `847` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:6.10` | `856` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:6.11` | `857` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:6.12` | `858` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:6.13` | `859` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:6.14` | `860` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:6.15` | `861` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:6.16` | `862` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:6.17` | `863` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:6.18` | `864` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:6.19` | `865` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:6.2` | `848` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:6.20` | `866` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:6.21` | `867` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:6.22` | `868` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:6.3` | `849` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:6.4` | `850` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:6.5` | `851` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:6.6` | `852` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:6.7` | `853` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:6.8` | `854` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:6.9` | `855` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:7.1` | `869` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:7.10` | `878` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:7.11` | `879` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:7.12` | `880` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:7.13` | `881` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:7.2` | `870` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:7.3` | `871` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:7.4` | `872` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:7.5` | `873` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:7.6` | `874` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:7.7` | `875` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:7.8` | `876` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:eq:7.9` | `877` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:full-original-frame` | `P.6.6` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:normal-frame-diagram` | `P.6.6` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:rank-three-framing` | `P.6` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:relative-disk-diagram` | `P.5` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:relative-embedded-disks` | `P.5` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:section` | `P` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:section-1` | `P.1` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:section-2` | `P.2` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:section-3` | `P.3` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:section-4` | `P.4` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:section-5` | `P.5` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:section-6` | `P.6` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:section-6.1` | `P.6.1` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:section-6.2` | `P.6.2` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:section-6.3` | `P.6.3` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:section-6.4` | `P.6.4` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:section-6.5` | `P.6.5` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:section-6.6` | `P.6.6` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:section-7` | `P.7` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:section-7.1` | `P.7.1` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:section-7.2` | `P.7.2` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:section-7.3` | `P.7.3` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:section-7.4` | `P.7.4` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:section-7.5` | `P.7.5` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:section-7.6` | `P.7.6` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:whitney-adapted-frame` | `P.7.5` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:whitney-boundary` | `P.7` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:whitney-boundary-diagram` | `P.7.6` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:whitney-filled-collar` | `P.7.3` |
| III | `courseIII:belt-sphere-complements-and-the-whitney-disk:whitney-orientations` | `P.7.4` |
| III | `courseIII:coefficient-complete-certificate` | `AA.8` |
| III | `courseIII:coefficient-rings-and-the-original-degree-six-class:coefficient-adem-maps` | `AA.3` |
| III | `courseIII:coefficient-rings-and-the-original-degree-six-class:coefficient-all-length-receiving` | `AA.5` |
| III | `courseIII:coefficient-rings-and-the-original-degree-six-class:coefficient-homological-maps` | `AA.4` |
| III | `courseIII:coefficient-rings-and-the-original-degree-six-class:coefficient-original-algebras` | `AA.1` |
| III | `courseIII:coefficient-rings-and-the-original-degree-six-class:coefficient-original-h28` | `AA.6` |
| III | `courseIII:coefficient-rings-and-the-original-degree-six-class:coefficient-source-scope` | `AA` |
| III | `courseIII:coefficient-rings-and-the-original-degree-six-class:coefficient-two-gradings` | `AA.2` |
| III | `courseIII:coefficient-rings-and-the-original-degree-six-class:coefficient-worked-exercises` | `AA.7` |
| III | `courseIII:coefficient-rings-and-the-original-degree-six-class:eq:1.1` | `1466` |
| III | `courseIII:coefficient-rings-and-the-original-degree-six-class:eq:1.10` | `1475` |
| III | `courseIII:coefficient-rings-and-the-original-degree-six-class:eq:1.11` | `1476` |
| III | `courseIII:coefficient-rings-and-the-original-degree-six-class:eq:1.12` | `1477` |
| III | `courseIII:coefficient-rings-and-the-original-degree-six-class:eq:1.13` | `1478` |
| III | `courseIII:coefficient-rings-and-the-original-degree-six-class:eq:1.2` | `1467` |
| III | `courseIII:coefficient-rings-and-the-original-degree-six-class:eq:1.3` | `1468` |
| III | `courseIII:coefficient-rings-and-the-original-degree-six-class:eq:1.4` | `1469` |
| III | `courseIII:coefficient-rings-and-the-original-degree-six-class:eq:1.5` | `1470` |
| III | `courseIII:coefficient-rings-and-the-original-degree-six-class:eq:1.6` | `1471` |
| III | `courseIII:coefficient-rings-and-the-original-degree-six-class:eq:1.7` | `1472` |
| III | `courseIII:coefficient-rings-and-the-original-degree-six-class:eq:1.8` | `1473` |
| III | `courseIII:coefficient-rings-and-the-original-degree-six-class:eq:1.9` | `1474` |
| III | `courseIII:coefficient-rings-and-the-original-degree-six-class:eq:2.1` | `1479` |
| III | `courseIII:coefficient-rings-and-the-original-degree-six-class:eq:2.2` | `1480` |
| III | `courseIII:coefficient-rings-and-the-original-degree-six-class:eq:2.3` | `1481` |
| III | `courseIII:coefficient-rings-and-the-original-degree-six-class:eq:3.1` | `1482` |
| III | `courseIII:coefficient-rings-and-the-original-degree-six-class:eq:3.2` | `1483` |
| III | `courseIII:coefficient-rings-and-the-original-degree-six-class:eq:3.3` | `1484` |
| III | `courseIII:coefficient-rings-and-the-original-degree-six-class:eq:3.4` | `1485` |
| III | `courseIII:coefficient-rings-and-the-original-degree-six-class:eq:3.5` | `1486` |
| III | `courseIII:coefficient-rings-and-the-original-degree-six-class:eq:3.6` | `1487` |
| III | `courseIII:coefficient-rings-and-the-original-degree-six-class:eq:3.7` | `1488` |
| III | `courseIII:coefficient-rings-and-the-original-degree-six-class:eq:3.8` | `1489` |
| III | `courseIII:coefficient-rings-and-the-original-degree-six-class:eq:4.1` | `1490` |
| III | `courseIII:coefficient-rings-and-the-original-degree-six-class:eq:4.10` | `1501` |
| III | `courseIII:coefficient-rings-and-the-original-degree-six-class:eq:4.2` | `1491` |
| III | `courseIII:coefficient-rings-and-the-original-degree-six-class:eq:4.2a` | `1492` |
| III | `courseIII:coefficient-rings-and-the-original-degree-six-class:eq:4.2b` | `1493` |
| III | `courseIII:coefficient-rings-and-the-original-degree-six-class:eq:4.3` | `1494` |
| III | `courseIII:coefficient-rings-and-the-original-degree-six-class:eq:4.4` | `1495` |
| III | `courseIII:coefficient-rings-and-the-original-degree-six-class:eq:4.5` | `1496` |
| III | `courseIII:coefficient-rings-and-the-original-degree-six-class:eq:4.6` | `1497` |
| III | `courseIII:coefficient-rings-and-the-original-degree-six-class:eq:4.7` | `1498` |
| III | `courseIII:coefficient-rings-and-the-original-degree-six-class:eq:4.8` | `1499` |
| III | `courseIII:coefficient-rings-and-the-original-degree-six-class:eq:4.9` | `1500` |
| III | `courseIII:coefficient-rings-and-the-original-degree-six-class:eq:5.1` | `1502` |
| III | `courseIII:coefficient-rings-and-the-original-degree-six-class:eq:5.10` | `1511` |
| III | `courseIII:coefficient-rings-and-the-original-degree-six-class:eq:5.11` | `1512` |
| III | `courseIII:coefficient-rings-and-the-original-degree-six-class:eq:5.12` | `1513` |
| III | `courseIII:coefficient-rings-and-the-original-degree-six-class:eq:5.13` | `1514` |
| III | `courseIII:coefficient-rings-and-the-original-degree-six-class:eq:5.2` | `1503` |
| III | `courseIII:coefficient-rings-and-the-original-degree-six-class:eq:5.3` | `1504` |
| III | `courseIII:coefficient-rings-and-the-original-degree-six-class:eq:5.4` | `1505` |
| III | `courseIII:coefficient-rings-and-the-original-degree-six-class:eq:5.5` | `1506` |
| III | `courseIII:coefficient-rings-and-the-original-degree-six-class:eq:5.6` | `1507` |
| III | `courseIII:coefficient-rings-and-the-original-degree-six-class:eq:5.7` | `1508` |
| III | `courseIII:coefficient-rings-and-the-original-degree-six-class:eq:5.8` | `1509` |
| III | `courseIII:coefficient-rings-and-the-original-degree-six-class:eq:5.9` | `1510` |
| III | `courseIII:coefficient-rings-and-the-original-degree-six-class:eq:6.1` | `1515` |
| III | `courseIII:coefficient-rings-and-the-original-degree-six-class:eq:6.2` | `1516` |
| III | `courseIII:coefficient-rings-and-the-original-degree-six-class:eq:6.3` | `1517` |
| III | `courseIII:coefficient-rings-and-the-original-degree-six-class:eq:6.4` | `1518` |
| III | `courseIII:coefficient-rings-and-the-original-degree-six-class:eq:6.5` | `1519` |
| III | `courseIII:coefficient-rings-and-the-original-degree-six-class:eq:7.1` | `1520` |
| III | `courseIII:coefficient-rings-and-the-original-degree-six-class:eq:7.10` | `1529` |
| III | `courseIII:coefficient-rings-and-the-original-degree-six-class:eq:7.11` | `1530` |
| III | `courseIII:coefficient-rings-and-the-original-degree-six-class:eq:7.2` | `1521` |
| III | `courseIII:coefficient-rings-and-the-original-degree-six-class:eq:7.3` | `1522` |
| III | `courseIII:coefficient-rings-and-the-original-degree-six-class:eq:7.4` | `1523` |
| III | `courseIII:coefficient-rings-and-the-original-degree-six-class:eq:7.5` | `1524` |
| III | `courseIII:coefficient-rings-and-the-original-degree-six-class:eq:7.6` | `1525` |
| III | `courseIII:coefficient-rings-and-the-original-degree-six-class:eq:7.7` | `1526` |
| III | `courseIII:coefficient-rings-and-the-original-degree-six-class:eq:7.8` | `1527` |
| III | `courseIII:coefficient-rings-and-the-original-degree-six-class:eq:7.9` | `1528` |
| III | `courseIII:coefficient-rings-and-the-original-degree-six-class:exercise-7.1` | `AA.7.1` |
| III | `courseIII:coefficient-rings-and-the-original-degree-six-class:exercise-7.2` | `AA.7.2` |
| III | `courseIII:coefficient-rings-and-the-original-degree-six-class:section` | `AA` |
| III | `courseIII:coefficient-rings-and-the-original-degree-six-class:section-1` | `AA.1` |
| III | `courseIII:coefficient-rings-and-the-original-degree-six-class:section-2` | `AA.2` |
| III | `courseIII:coefficient-rings-and-the-original-degree-six-class:section-3` | `AA.3` |
| III | `courseIII:coefficient-rings-and-the-original-degree-six-class:section-4` | `AA.4` |
| III | `courseIII:coefficient-rings-and-the-original-degree-six-class:section-5` | `AA.5` |
| III | `courseIII:coefficient-rings-and-the-original-degree-six-class:section-6` | `AA.6` |
| III | `courseIII:coefficient-rings-and-the-original-degree-six-class:section-7` | `AA.7` |
| III | `courseIII:coefficient-rings:1` | `AA.1` |
| III | `courseIII:coefficient-rings:2` | `AA.2` |
| III | `courseIII:coefficient-rings:3` | `AA.3` |
| III | `courseIII:coefficient-rings:4` | `AA.4` |
| III | `courseIII:coefficient-rings:5` | `AA.5` |
| III | `courseIII:coefficient-rings:6` | `AA.6` |
| III | `courseIII:coefficient-rings:7.1` | `AA.7.1` |
| III | `courseIII:coefficient-rings:7.2` | `AA.7.2` |
| III | `courseIII:creating-an-original-cancelling-handle-pair:eq:1.1` | `527` |
| III | `courseIII:creating-an-original-cancelling-handle-pair:eq:1.10` | `536` |
| III | `courseIII:creating-an-original-cancelling-handle-pair:eq:1.11` | `537` |
| III | `courseIII:creating-an-original-cancelling-handle-pair:eq:1.12` | `538` |
| III | `courseIII:creating-an-original-cancelling-handle-pair:eq:1.2` | `528` |
| III | `courseIII:creating-an-original-cancelling-handle-pair:eq:1.3` | `529` |
| III | `courseIII:creating-an-original-cancelling-handle-pair:eq:1.4` | `530` |
| III | `courseIII:creating-an-original-cancelling-handle-pair:eq:1.5` | `531` |
| III | `courseIII:creating-an-original-cancelling-handle-pair:eq:1.6` | `532` |
| III | `courseIII:creating-an-original-cancelling-handle-pair:eq:1.7` | `533` |
| III | `courseIII:creating-an-original-cancelling-handle-pair:eq:1.8` | `534` |
| III | `courseIII:creating-an-original-cancelling-handle-pair:eq:1.9` | `535` |
| III | `courseIII:creating-an-original-cancelling-handle-pair:eq:2.1` | `539` |
| III | `courseIII:creating-an-original-cancelling-handle-pair:eq:2.2` | `540` |
| III | `courseIII:creating-an-original-cancelling-handle-pair:eq:2.3` | `541` |
| III | `courseIII:creating-an-original-cancelling-handle-pair:eq:2.4` | `542` |
| III | `courseIII:creating-an-original-cancelling-handle-pair:eq:2.5` | `543` |
| III | `courseIII:creating-an-original-cancelling-handle-pair:eq:2.6` | `544` |
| III | `courseIII:creating-an-original-cancelling-handle-pair:eq:2.7` | `545` |
| III | `courseIII:creating-an-original-cancelling-handle-pair:eq:3.1` | `546` |
| III | `courseIII:creating-an-original-cancelling-handle-pair:eq:3.2` | `547` |
| III | `courseIII:creating-an-original-cancelling-handle-pair:eq:3.3` | `548` |
| III | `courseIII:creating-an-original-cancelling-handle-pair:eq:3.4` | `549` |
| III | `courseIII:creating-an-original-cancelling-handle-pair:eq:3.5` | `550` |
| III | `courseIII:creating-an-original-cancelling-handle-pair:eq:3.6` | `551` |
| III | `courseIII:creating-an-original-cancelling-handle-pair:eq:3.7` | `552` |
| III | `courseIII:creating-an-original-cancelling-handle-pair:eq:3.8` | `553` |
| III | `courseIII:creating-an-original-cancelling-handle-pair:eq:4.1` | `554` |
| III | `courseIII:creating-an-original-cancelling-handle-pair:eq:4.2` | `555` |
| III | `courseIII:creating-an-original-cancelling-handle-pair:eq:4.3` | `556` |
| III | `courseIII:creating-an-original-cancelling-handle-pair:eq:4.4` | `557` |
| III | `courseIII:creating-an-original-cancelling-handle-pair:eq:4.5` | `558` |
| III | `courseIII:creating-an-original-cancelling-handle-pair:eq:5.1` | `559` |
| III | `courseIII:creating-an-original-cancelling-handle-pair:eq:5.2` | `560` |
| III | `courseIII:creating-an-original-cancelling-handle-pair:eq:5.3` | `561` |
| III | `courseIII:creating-an-original-cancelling-handle-pair:eq:5.4` | `562` |
| III | `courseIII:creating-an-original-cancelling-handle-pair:eq:5.5` | `563` |
| III | `courseIII:creating-an-original-cancelling-handle-pair:eq:5.6` | `564` |
| III | `courseIII:creating-an-original-cancelling-handle-pair:eq:5.7` | `565` |
| III | `courseIII:creating-an-original-cancelling-handle-pair:eq:5.8` | `566` |
| III | `courseIII:creating-an-original-cancelling-handle-pair:eq:6.1` | `567` |
| III | `courseIII:creating-an-original-cancelling-handle-pair:eq:6.2` | `568` |
| III | `courseIII:creating-an-original-cancelling-handle-pair:eq:6.3` | `569` |
| III | `courseIII:creating-an-original-cancelling-handle-pair:eq:6.4` | `570` |
| III | `courseIII:creating-an-original-cancelling-handle-pair:eq:6.5` | `571` |
| III | `courseIII:creating-an-original-cancelling-handle-pair:eq:6.6` | `572` |
| III | `courseIII:creating-an-original-cancelling-handle-pair:eq:6.7` | `573` |
| III | `courseIII:creating-an-original-cancelling-handle-pair:eq:6.8` | `574` |
| III | `courseIII:creating-an-original-cancelling-handle-pair:eq:7.1` | `575` |
| III | `courseIII:creating-an-original-cancelling-handle-pair:eq:7.2` | `576` |
| III | `courseIII:creating-an-original-cancelling-handle-pair:eq:7.3` | `577` |
| III | `courseIII:creating-an-original-cancelling-handle-pair:eq:7.4` | `578` |
| III | `courseIII:creating-an-original-cancelling-handle-pair:eq:7.5` | `579` |
| III | `courseIII:creating-an-original-cancelling-handle-pair:pair-attaching-disk` | `K.6` |
| III | `courseIII:creating-an-original-cancelling-handle-pair:pair-cancelled-model` | `K.2` |
| III | `courseIII:creating-an-original-cancelling-handle-pair:pair-connecting-trajectory` | `K.4` |
| III | `courseIII:creating-an-original-cancelling-handle-pair:pair-exercises` | `K.7` |
| III | `courseIII:creating-an-original-cancelling-handle-pair:pair-global-model` | `K.1` |
| III | `courseIII:creating-an-original-cancelling-handle-pair:pair-global-product` | `K.3` |
| III | `courseIII:creating-an-original-cancelling-handle-pair:pair-original-band` | `K.5` |
| III | `courseIII:creating-an-original-cancelling-handle-pair:section` | `K` |
| III | `courseIII:creating-an-original-cancelling-handle-pair:section-1` | `K.1` |
| III | `courseIII:creating-an-original-cancelling-handle-pair:section-2` | `K.2` |
| III | `courseIII:creating-an-original-cancelling-handle-pair:section-3` | `K.3` |
| III | `courseIII:creating-an-original-cancelling-handle-pair:section-4` | `K.4` |
| III | `courseIII:creating-an-original-cancelling-handle-pair:section-5` | `K.5` |
| III | `courseIII:creating-an-original-cancelling-handle-pair:section-6` | `K.6` |
| III | `courseIII:creating-an-original-cancelling-handle-pair:section-7` | `K.7` |
| III | `courseIII:creating-an-original-cancelling-handle-pair:section-7.1` | `K.7.1` |
| III | `courseIII:creating-an-original-cancelling-handle-pair:section-7.2` | `K.7.2` |
| III | `courseIII:duality:2.1` | `F.1` |
| III | `courseIII:duality:2.2` | `F.2` |
| III | `courseIII:duality:2.3` | `F.3` |
| III | `courseIII:duality:3.1` | `F.4` |
| III | `courseIII:duality:3.2` | `F.5` |
| III | `courseIII:duality:3.3` | `F.6` |
| III | `courseIII:duality:4.1` | `F.7` |
| III | `courseIII:duality:4.2` | `F.8` |
| III | `courseIII:formal-char2:1` | `V.1` |
| III | `courseIII:formal-char2:2` | `V.2` |
| III | `courseIII:formal-char2:3` | `V.3` |
| III | `courseIII:formal-char2:4` | `V.4` |
| III | `courseIII:formal-char2:4.1` | `V.4.1` |
| III | `courseIII:formal-char2:4.2` | `V.4.2` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:1.1` | `1023` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:1.2` | `1024` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:1.3` | `1025` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:1.4` | `1026` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:1.5` | `1027` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:1.6` | `1028` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:1.7` | `1029` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:1.8` | `1030` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:1.9` | `1031` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:2.1` | `1032` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:2.2` | `1033` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:2.3` | `1034` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:2.4` | `1035` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:3.1` | `1036` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:3.10` | `1045` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:3.11` | `1046` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:3.12` | `1047` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:3.13` | `1048` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:3.14` | `1049` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:3.2` | `1037` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:3.3` | `1038` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:3.4` | `1039` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:3.5` | `1040` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:3.6` | `1041` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:3.7` | `1042` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:3.8` | `1043` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:3.9` | `1044` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:4.1` | `1050` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:4.2` | `1051` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:4.3` | `1052` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:4.4` | `1053` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:5.1` | `1054` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:5.10` | `1063` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:5.11` | `1064` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:5.12` | `1065` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:5.13` | `1066` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:5.14` | `1067` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:5.15` | `1068` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:5.2` | `1055` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:5.3` | `1056` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:5.4` | `1057` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:5.5` | `1058` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:5.6` | `1059` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:5.7` | `1060` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:5.8` | `1061` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:5.9` | `1062` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:6.1` | `1069` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:6.10` | `1078` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:6.11` | `1079` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:6.12` | `1080` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:6.13` | `1081` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:6.14` | `1082` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:6.15` | `1083` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:6.16` | `1084` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:6.17` | `1085` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:6.18` | `1086` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:6.19` | `1087` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:6.2` | `1070` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:6.20` | `1088` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:6.3` | `1071` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:6.4` | `1072` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:6.5` | `1073` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:6.6` | `1074` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:6.7` | `1075` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:6.8` | `1076` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:6.9` | `1077` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:7.1` | `1089` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:7.10` | `1098` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:7.11` | `1099` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:7.12` | `1100` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:7.13` | `1101` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:7.14` | `1102` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:7.15` | `1103` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:7.2` | `1090` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:7.3` | `1091` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:7.4` | `1092` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:7.5` | `1093` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:7.6` | `1094` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:7.7` | `1095` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:7.8` | `1096` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:7.9` | `1097` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:8.1` | `1104` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:8.2` | `1105` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:8.3` | `1106` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:8.4` | `1107` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:8.5` | `1108` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:8.6` | `1109` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:8.7` | `1110` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:8.8` | `1111` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:8.9` | `1112` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:9.1` | `1113` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:9.10` | `1122` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:9.11` | `1123` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:9.2` | `1114` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:9.3` | `1115` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:9.4` | `1116` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:9.5` | `1117` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:9.6` | `1118` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:9.7` | `1119` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:9.8` | `1120` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:eq:9.9` | `1121` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:section` | `S` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:section-1` | `S.1` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:section-2` | `S.2` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:section-3` | `S.3` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:section-4` | `S.4` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:section-5` | `S.5` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:section-5.1` | `S.5.1` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:section-6` | `S.6` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:section-6.1` | `S.6.1` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:section-6.2` | `S.6.2` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:section-6.3` | `S.6.3` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:section-7` | `S.7` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:section-7.1` | `S.7.1` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:section-7.2` | `S.7.2` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:section-7.3` | `S.7.3` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:section-8` | `S.8` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:section-8.1` | `S.8.1` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:section-9` | `S.9` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:section-9.1` | `S.9.1` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:section-9.2` | `S.9.2` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:slide-based-sign` | `S.4` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:slide-belt-crossing` | `S.3` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:slide-exercises` | `S.9` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:slide-index-one-cancellation` | `S.7` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:slide-loop-isotopy` | `S.5` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:slide-normal-closure` | `S.2` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:slide-original-flow` | `S.6` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:slide-original-group` | `S.1` |
| III | `courseIII:framed-handle-slides-and-index-one-removal:slide-reversal` | `S.8` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:1.1` | `263` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:1.2` | `264` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:1.3` | `265` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:1.4` | `266` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:1.5` | `267` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:1.6` | `268` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:1.7` | `269` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:1.8` | `270` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:2.1` | `271` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:2.2` | `272` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:2.3` | `273` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:2.4` | `274` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:2.5` | `275` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:2.6` | `276` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:2.7` | `277` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:2.8` | `278` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:2.9` | `279` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:3.1` | `280` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:3.10` | `289` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:3.11` | `290` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:3.12` | `291` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:3.13` | `292` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:3.14` | `293` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:3.15` | `294` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:3.2` | `281` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:3.3` | `282` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:3.4` | `283` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:3.5` | `284` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:3.6` | `285` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:3.7` | `286` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:3.8` | `287` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:3.9` | `288` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:4.1` | `295` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:4.2` | `296` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:4.3` | `297` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:4.4` | `298` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:4.5` | `299` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:4.6` | `300` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:4.7` | `301` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:4.8` | `302` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:4.9` | `303` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:5.1` | `304` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:5.10` | `313` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:5.11` | `314` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:5.12` | `315` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:5.13` | `316` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:5.2` | `305` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:5.3` | `306` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:5.4` | `307` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:5.5` | `308` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:5.6` | `309` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:5.7` | `310` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:5.8` | `311` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:5.9` | `312` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:6.1` | `317` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:6.10` | `326` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:6.11` | `327` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:6.12` | `328` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:6.13` | `329` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:6.14` | `330` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:6.15` | `331` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:6.16` | `332` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:6.17` | `333` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:6.2` | `318` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:6.3` | `319` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:6.4` | `320` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:6.5` | `321` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:6.6` | `322` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:6.7` | `323` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:6.8` | `324` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:6.9` | `325` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:7.1` | `334` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:8.1` | `335` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:8.10` | `344` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:8.11` | `345` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:8.12` | `346` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:8.13` | `347` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:8.14` | `348` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:8.15` | `349` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:8.16` | `350` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:8.2` | `336` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:8.3` | `337` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:8.4` | `338` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:8.5` | `339` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:8.6` | `340` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:8.7` | `341` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:8.8` | `342` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:8.9` | `343` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:9.1` | `351` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:9.10` | `360` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:9.11` | `361` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:9.12` | `362` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:9.13` | `363` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:9.14` | `364` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:9.15` | `365` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:9.16` | `366` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:9.2` | `352` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:9.3` | `353` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:9.4` | `354` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:9.5` | `355` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:9.6` | `356` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:9.7` | `357` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:9.8` | `358` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:eq:9.9` | `359` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:exercise-9.1` | `G.9.1` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:exercise-9.2` | `G.9.2` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:pt-bijection` | `G.7` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:pt-bordism-to-homotopy` | `G.4` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:pt-full-tube-and-collapse` | `G.3` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:pt-inverse-tube-comparison` | `G.6` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:pt-original-embedding` | `G.1` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:pt-relative-regular-value` | `G.5` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:pt-sources-and-scope` | `G` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:pt-stabilization-and-original-framing` | `G.8` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:pt-stable-normal-frame` | `G.2` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:pt-worked-exercises` | `G.9` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:section` | `G` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:section-1` | `G.1` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:section-2` | `G.2` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:section-3` | `G.3` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:section-4` | `G.4` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:section-5` | `G.5` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:section-6` | `G.6` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:section-7` | `G.7` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:section-8` | `G.8` |
| III | `courseIII:framed-manifolds-and-the-pontryagin-thom-map:section-9` | `G.9` |
| III | `courseIII:framed6:1` | `AF.1` |
| III | `courseIII:framed6:10.1` | `AF.10.1` |
| III | `courseIII:framed6:10.2` | `AF.10.2` |
| III | `courseIII:framed6:2` | `AF.2` |
| III | `courseIII:framed6:3` | `AF.3` |
| III | `courseIII:framed6:4` | `AF.4` |
| III | `courseIII:framed6:5` | `AF.5` |
| III | `courseIII:framed6:6` | `AF.6` |
| III | `courseIII:framed6:7` | `AF.7` |
| III | `courseIII:framed6:8` | `AF.8` |
| III | `courseIII:framed6:9` | `AF.9` |
| III | `courseIII:handle-arrangement:1` | `M.1` |
| III | `courseIII:handle-arrangement:2` | `M.2` |
| III | `courseIII:handle-arrangement:3` | `M.3` |
| III | `courseIII:handle-arrangement:4` | `M.4` |
| III | `courseIII:handle-arrangement:5.1` | `M.5.1` |
| III | `courseIII:handle-arrangement:5.2` | `M.5.2` |
| III | `courseIII:handle-chains:1` | `O.1` |
| III | `courseIII:handle-chains:2` | `O.2` |
| III | `courseIII:handle-chains:3` | `O.3` |
| III | `courseIII:handle-chains:4` | `O.4` |
| III | `courseIII:handle-chains:5` | `O.5` |
| III | `courseIII:handle-chains:6.1` | `O.6.1` |
| III | `courseIII:handle-chains:6.2` | `O.6.2` |
| III | `courseIII:handle-chains:8.1` | `O.7.1` |
| III | `courseIII:handle-chains:8.2` | `O.7.2` |
| III | `courseIII:higher-index-framed-slides-and-chain-maps:eq:1.1` | `1124` |
| III | `courseIII:higher-index-framed-slides-and-chain-maps:eq:1.2` | `1125` |
| III | `courseIII:higher-index-framed-slides-and-chain-maps:eq:1.3` | `1126` |
| III | `courseIII:higher-index-framed-slides-and-chain-maps:eq:1.4` | `1127` |
| III | `courseIII:higher-index-framed-slides-and-chain-maps:eq:1.5` | `1128` |
| III | `courseIII:higher-index-framed-slides-and-chain-maps:eq:2.1` | `1129` |
| III | `courseIII:higher-index-framed-slides-and-chain-maps:eq:2.10` | `1138` |
| III | `courseIII:higher-index-framed-slides-and-chain-maps:eq:2.2` | `1130` |
| III | `courseIII:higher-index-framed-slides-and-chain-maps:eq:2.3` | `1131` |
| III | `courseIII:higher-index-framed-slides-and-chain-maps:eq:2.4` | `1132` |
| III | `courseIII:higher-index-framed-slides-and-chain-maps:eq:2.5` | `1133` |
| III | `courseIII:higher-index-framed-slides-and-chain-maps:eq:2.6` | `1134` |
| III | `courseIII:higher-index-framed-slides-and-chain-maps:eq:2.7` | `1135` |
| III | `courseIII:higher-index-framed-slides-and-chain-maps:eq:2.8` | `1136` |
| III | `courseIII:higher-index-framed-slides-and-chain-maps:eq:2.9` | `1137` |
| III | `courseIII:higher-index-framed-slides-and-chain-maps:eq:3.1` | `1139` |
| III | `courseIII:higher-index-framed-slides-and-chain-maps:eq:3.2` | `1140` |
| III | `courseIII:higher-index-framed-slides-and-chain-maps:eq:3.3` | `1141` |
| III | `courseIII:higher-index-framed-slides-and-chain-maps:eq:3.4` | `1142` |
| III | `courseIII:higher-index-framed-slides-and-chain-maps:eq:3.5` | `1143` |
| III | `courseIII:higher-index-framed-slides-and-chain-maps:eq:3.6` | `1144` |
| III | `courseIII:higher-index-framed-slides-and-chain-maps:eq:4.1` | `1145` |
| III | `courseIII:higher-index-framed-slides-and-chain-maps:eq:4.2` | `1146` |
| III | `courseIII:higher-index-framed-slides-and-chain-maps:eq:4.3` | `1147` |
| III | `courseIII:higher-index-framed-slides-and-chain-maps:eq:4.4` | `1148` |
| III | `courseIII:higher-index-framed-slides-and-chain-maps:eq:4.5` | `1149` |
| III | `courseIII:higher-index-framed-slides-and-chain-maps:eq:4.6` | `1150` |
| III | `courseIII:higher-index-framed-slides-and-chain-maps:eq:4.7` | `1151` |
| III | `courseIII:higher-index-framed-slides-and-chain-maps:eq:5.1` | `1152` |
| III | `courseIII:higher-index-framed-slides-and-chain-maps:eq:5.2` | `1153` |
| III | `courseIII:higher-index-framed-slides-and-chain-maps:eq:5.3` | `1154` |
| III | `courseIII:higher-index-framed-slides-and-chain-maps:eq:5.4` | `1155` |
| III | `courseIII:higher-index-framed-slides-and-chain-maps:eq:5.5` | `1156` |
| III | `courseIII:higher-index-framed-slides-and-chain-maps:eq:5.6` | `1157` |
| III | `courseIII:higher-index-framed-slides-and-chain-maps:eq:5.7` | `1158` |
| III | `courseIII:higher-index-framed-slides-and-chain-maps:eq:6.1` | `1159` |
| III | `courseIII:higher-index-framed-slides-and-chain-maps:eq:6.2` | `1160` |
| III | `courseIII:higher-index-framed-slides-and-chain-maps:eq:8.1` | `1161` |
| III | `courseIII:higher-index-framed-slides-and-chain-maps:eq:8.2` | `1162` |
| III | `courseIII:higher-index-framed-slides-and-chain-maps:eq:8.3` | `1163` |
| III | `courseIII:higher-index-framed-slides-and-chain-maps:eq:8.4` | `1164` |
| III | `courseIII:higher-index-framed-slides-and-chain-maps:eq:8.5` | `1165` |
| III | `courseIII:higher-index-framed-slides-and-chain-maps:eq:8.6` | `1166` |
| III | `courseIII:higher-index-framed-slides-and-chain-maps:eq:8.7` | `1167` |
| III | `courseIII:higher-index-framed-slides-and-chain-maps:eq:8.8` | `1168` |
| III | `courseIII:higher-index-framed-slides-and-chain-maps:eq:8.9` | `1169` |
| III | `courseIII:higher-index-framed-slides-and-chain-maps:exercise-1` | `T.7.1` |
| III | `courseIII:higher-index-framed-slides-and-chain-maps:exercise-2` | `T.7.2` |
| III | `courseIII:higher-index-framed-slides-and-chain-maps:higher-slide-cobordism` | `T.3` |
| III | `courseIII:higher-index-framed-slides-and-chain-maps:higher-slide-crossing` | `T.2` |
| III | `courseIII:higher-index-framed-slides-and-chain-maps:higher-slide-exercises` | `T.7` |
| III | `courseIII:higher-index-framed-slides-and-chain-maps:higher-slide-integer-changes` | `T.6` |
| III | `courseIII:higher-index-framed-slides-and-chain-maps:higher-slide-matrices` | `T.5` |
| III | `courseIII:higher-index-framed-slides-and-chain-maps:higher-slide-prism` | `T.4` |
| III | `courseIII:higher-index-framed-slides-and-chain-maps:higher-slide-stages` | `T.1` |
| III | `courseIII:higher-index-framed-slides-and-chain-maps:section` | `T` |
| III | `courseIII:higher-index-framed-slides-and-chain-maps:section-1` | `T.1` |
| III | `courseIII:higher-index-framed-slides-and-chain-maps:section-2` | `T.2` |
| III | `courseIII:higher-index-framed-slides-and-chain-maps:section-3` | `T.3` |
| III | `courseIII:higher-index-framed-slides-and-chain-maps:section-4` | `T.4` |
| III | `courseIII:higher-index-framed-slides-and-chain-maps:section-5` | `T.5` |
| III | `courseIII:higher-index-framed-slides-and-chain-maps:section-6` | `T.6` |
| III | `courseIII:higher-index-framed-slides-and-chain-maps:section-8` | `T.7` |
| III | `courseIII:higher-slides:1` | `T.1` |
| III | `courseIII:higher-slides:2` | `T.2` |
| III | `courseIII:higher-slides:3` | `T.3` |
| III | `courseIII:higher-slides:4` | `T.4` |
| III | `courseIII:higher-slides:5` | `T.5` |
| III | `courseIII:higher-slides:6` | `T.6` |
| III | `courseIII:higher-slides:8.1` | `T.7.1` |
| III | `courseIII:higher-slides:8.2` | `T.7.2` |
| III | `courseIII:integral-chern-classes-for-lesson11:CG-S6-CHERN-1` | `E.1` |
| III | `courseIII:integral-chern-classes-for-lesson11:CG-S6-CHERN-2` | `E.2` |
| III | `courseIII:integral-chern-classes-for-lesson11:CG-S6-CHERN-3` | `E.3` |
| III | `courseIII:integral-chern-classes-for-lesson11:character-operations` | `E.3` |
| III | `courseIII:integral-chern-classes-for-lesson11:chern-rules` | `E.2` |
| III | `courseIII:integral-chern-classes-for-lesson11:eq:1.1` | `236` |
| III | `courseIII:integral-chern-classes-for-lesson11:eq:1.2` | `237` |
| III | `courseIII:integral-chern-classes-for-lesson11:eq:1.3` | `238` |
| III | `courseIII:integral-chern-classes-for-lesson11:eq:1.4` | `239` |
| III | `courseIII:integral-chern-classes-for-lesson11:eq:2.1` | `240` |
| III | `courseIII:integral-chern-classes-for-lesson11:eq:2.2` | `241` |
| III | `courseIII:integral-chern-classes-for-lesson11:eq:2.3` | `242` |
| III | `courseIII:integral-chern-classes-for-lesson11:eq:3.1` | `243` |
| III | `courseIII:integral-chern-classes-for-lesson11:eq:3.2` | `244` |
| III | `courseIII:integral-chern-classes-for-lesson11:eq:3.3` | `245` |
| III | `courseIII:integral-chern-classes-for-lesson11:integral-definition` | `E.1` |
| III | `courseIII:integral-chern-classes-for-lesson11:section` | `E` |
| III | `courseIII:integral-chern-classes-for-lesson11:section-1` | `E.1` |
| III | `courseIII:integral-chern-classes-for-lesson11:section-2` | `E.2` |
| III | `courseIII:integral-chern-classes-for-lesson11:section-3` | `E.3` |
| III | `courseIII:integral-handle-chains-and-signed-incidences:eq:1.1` | `728` |
| III | `courseIII:integral-handle-chains-and-signed-incidences:eq:1.2` | `729` |
| III | `courseIII:integral-handle-chains-and-signed-incidences:eq:1.3` | `730` |
| III | `courseIII:integral-handle-chains-and-signed-incidences:eq:1.4` | `731` |
| III | `courseIII:integral-handle-chains-and-signed-incidences:eq:1.5` | `732` |
| III | `courseIII:integral-handle-chains-and-signed-incidences:eq:2.1` | `733` |
| III | `courseIII:integral-handle-chains-and-signed-incidences:eq:2.2` | `734` |
| III | `courseIII:integral-handle-chains-and-signed-incidences:eq:2.3` | `735` |
| III | `courseIII:integral-handle-chains-and-signed-incidences:eq:2.4` | `736` |
| III | `courseIII:integral-handle-chains-and-signed-incidences:eq:2.5` | `737` |
| III | `courseIII:integral-handle-chains-and-signed-incidences:eq:2.6` | `738` |
| III | `courseIII:integral-handle-chains-and-signed-incidences:eq:2.7` | `739` |
| III | `courseIII:integral-handle-chains-and-signed-incidences:eq:3.1` | `740` |
| III | `courseIII:integral-handle-chains-and-signed-incidences:eq:3.10` | `749` |
| III | `courseIII:integral-handle-chains-and-signed-incidences:eq:3.2` | `741` |
| III | `courseIII:integral-handle-chains-and-signed-incidences:eq:3.3` | `742` |
| III | `courseIII:integral-handle-chains-and-signed-incidences:eq:3.4` | `743` |
| III | `courseIII:integral-handle-chains-and-signed-incidences:eq:3.5` | `744` |
| III | `courseIII:integral-handle-chains-and-signed-incidences:eq:3.6` | `745` |
| III | `courseIII:integral-handle-chains-and-signed-incidences:eq:3.7` | `746` |
| III | `courseIII:integral-handle-chains-and-signed-incidences:eq:3.8` | `747` |
| III | `courseIII:integral-handle-chains-and-signed-incidences:eq:3.9` | `748` |
| III | `courseIII:integral-handle-chains-and-signed-incidences:eq:4.1` | `750` |
| III | `courseIII:integral-handle-chains-and-signed-incidences:eq:4.2` | `751` |
| III | `courseIII:integral-handle-chains-and-signed-incidences:eq:4.3` | `752` |
| III | `courseIII:integral-handle-chains-and-signed-incidences:eq:4.4` | `753` |
| III | `courseIII:integral-handle-chains-and-signed-incidences:eq:4.5` | `754` |
| III | `courseIII:integral-handle-chains-and-signed-incidences:eq:4.6` | `755` |
| III | `courseIII:integral-handle-chains-and-signed-incidences:eq:4.7` | `756` |
| III | `courseIII:integral-handle-chains-and-signed-incidences:eq:5.1` | `757` |
| III | `courseIII:integral-handle-chains-and-signed-incidences:eq:5.10` | `766` |
| III | `courseIII:integral-handle-chains-and-signed-incidences:eq:5.2` | `758` |
| III | `courseIII:integral-handle-chains-and-signed-incidences:eq:5.3` | `759` |
| III | `courseIII:integral-handle-chains-and-signed-incidences:eq:5.4` | `760` |
| III | `courseIII:integral-handle-chains-and-signed-incidences:eq:5.5` | `761` |
| III | `courseIII:integral-handle-chains-and-signed-incidences:eq:5.6` | `762` |
| III | `courseIII:integral-handle-chains-and-signed-incidences:eq:5.7` | `763` |
| III | `courseIII:integral-handle-chains-and-signed-incidences:eq:5.8` | `764` |
| III | `courseIII:integral-handle-chains-and-signed-incidences:eq:5.9` | `765` |
| III | `courseIII:integral-handle-chains-and-signed-incidences:eq:6.1` | `767` |
| III | `courseIII:integral-handle-chains-and-signed-incidences:eq:6.10` | `776` |
| III | `courseIII:integral-handle-chains-and-signed-incidences:eq:6.11` | `777` |
| III | `courseIII:integral-handle-chains-and-signed-incidences:eq:6.12` | `778` |
| III | `courseIII:integral-handle-chains-and-signed-incidences:eq:6.13` | `779` |
| III | `courseIII:integral-handle-chains-and-signed-incidences:eq:6.2` | `768` |
| III | `courseIII:integral-handle-chains-and-signed-incidences:eq:6.3` | `769` |
| III | `courseIII:integral-handle-chains-and-signed-incidences:eq:6.4` | `770` |
| III | `courseIII:integral-handle-chains-and-signed-incidences:eq:6.5` | `771` |
| III | `courseIII:integral-handle-chains-and-signed-incidences:eq:6.6` | `772` |
| III | `courseIII:integral-handle-chains-and-signed-incidences:eq:6.7` | `773` |
| III | `courseIII:integral-handle-chains-and-signed-incidences:eq:6.8` | `774` |
| III | `courseIII:integral-handle-chains-and-signed-incidences:eq:6.9` | `775` |
| III | `courseIII:integral-handle-chains-and-signed-incidences:eq:8.1` | `780` |
| III | `courseIII:integral-handle-chains-and-signed-incidences:eq:8.2` | `781` |
| III | `courseIII:integral-handle-chains-and-signed-incidences:eq:8.3` | `782` |
| III | `courseIII:integral-handle-chains-and-signed-incidences:eq:8.4` | `783` |
| III | `courseIII:integral-handle-chains-and-signed-incidences:eq:8.5` | `784` |
| III | `courseIII:integral-handle-chains-and-signed-incidences:eq:8.6` | `785` |
| III | `courseIII:integral-handle-chains-and-signed-incidences:eq:8.7` | `786` |
| III | `courseIII:integral-handle-chains-and-signed-incidences:eq:8.8` | `787` |
| III | `courseIII:integral-handle-chains-and-signed-incidences:eq:8.9` | `788` |
| III | `courseIII:integral-handle-chains-and-signed-incidences:exercise-8.1` | `O.7.1` |
| III | `courseIII:integral-handle-chains-and-signed-incidences:exercise-8.2` | `O.7.2` |
| III | `courseIII:integral-handle-chains-and-signed-incidences:handle-chain-boundary` | `O.2` |
| III | `courseIII:integral-handle-chains-and-signed-incidences:handle-chain-exercises` | `O.7` |
| III | `courseIII:integral-handle-chains-and-signed-incidences:handle-filtration` | `O.1` |
| III | `courseIII:integral-handle-chains-and-signed-incidences:handle-integral-bases` | `O.4` |
| III | `courseIII:integral-handle-chains-and-signed-incidences:handle-signed-incidence` | `O.3` |
| III | `courseIII:integral-handle-chains-and-signed-incidences:handle-six-seven` | `O.6` |
| III | `courseIII:integral-handle-chains-and-signed-incidences:handle-unit-contraction` | `O.5` |
| III | `courseIII:integral-handle-chains-and-signed-incidences:section` | `O` |
| III | `courseIII:integral-handle-chains-and-signed-incidences:section-1` | `O.1` |
| III | `courseIII:integral-handle-chains-and-signed-incidences:section-2` | `O.2` |
| III | `courseIII:integral-handle-chains-and-signed-incidences:section-3` | `O.3` |
| III | `courseIII:integral-handle-chains-and-signed-incidences:section-3.1` | `O.3.1` |
| III | `courseIII:integral-handle-chains-and-signed-incidences:section-3.2` | `O.3.2` |
| III | `courseIII:integral-handle-chains-and-signed-incidences:section-4` | `O.4` |
| III | `courseIII:integral-handle-chains-and-signed-incidences:section-5` | `O.5` |
| III | `courseIII:integral-handle-chains-and-signed-incidences:section-6` | `O.6` |
| III | `courseIII:integral-handle-chains-and-signed-incidences:section-6.1` | `O.6.1` |
| III | `courseIII:integral-handle-chains-and-signed-incidences:section-6.2` | `O.6.2` |
| III | `courseIII:integral-handle-chains-and-signed-incidences:section-8` | `O.7` |
| III | `courseIII:integral-homology-and-sphere-recognition:eq:10.1` | `2005` |
| III | `courseIII:integral-homology-and-sphere-recognition:eq:10.10` | `2014` |
| III | `courseIII:integral-homology-and-sphere-recognition:eq:10.11` | `2015` |
| III | `courseIII:integral-homology-and-sphere-recognition:eq:10.2` | `2006` |
| III | `courseIII:integral-homology-and-sphere-recognition:eq:10.3` | `2007` |
| III | `courseIII:integral-homology-and-sphere-recognition:eq:10.4` | `2008` |
| III | `courseIII:integral-homology-and-sphere-recognition:eq:10.5` | `2009` |
| III | `courseIII:integral-homology-and-sphere-recognition:eq:10.6` | `2010` |
| III | `courseIII:integral-homology-and-sphere-recognition:eq:10.7` | `2011` |
| III | `courseIII:integral-homology-and-sphere-recognition:eq:10.8` | `2012` |
| III | `courseIII:integral-homology-and-sphere-recognition:eq:10.9` | `2013` |
| III | `courseIII:integral-homology-and-sphere-recognition:eq:11.1` | `2016` |
| III | `courseIII:integral-homology-and-sphere-recognition:eq:11.10` | `2025` |
| III | `courseIII:integral-homology-and-sphere-recognition:eq:11.11` | `2026` |
| III | `courseIII:integral-homology-and-sphere-recognition:eq:11.2` | `2017` |
| III | `courseIII:integral-homology-and-sphere-recognition:eq:11.3` | `2018` |
| III | `courseIII:integral-homology-and-sphere-recognition:eq:11.4` | `2019` |
| III | `courseIII:integral-homology-and-sphere-recognition:eq:11.5` | `2020` |
| III | `courseIII:integral-homology-and-sphere-recognition:eq:11.6` | `2021` |
| III | `courseIII:integral-homology-and-sphere-recognition:eq:11.7` | `2022` |
| III | `courseIII:integral-homology-and-sphere-recognition:eq:11.8` | `2023` |
| III | `courseIII:integral-homology-and-sphere-recognition:eq:11.9` | `2024` |
| III | `courseIII:integral-homology-and-sphere-recognition:exercise-11.1` | `AH.2.1` |
| III | `courseIII:integral-homology-and-sphere-recognition:exercise-11.2` | `AH.2.2` |
| III | `courseIII:integral-homology-and-sphere-recognition:exercise-11.3` | `AH.2.3` |
| III | `courseIII:integral-homology-and-sphere-recognition:exercise-11.4` | `AH.2.4` |
| III | `courseIII:integral-homology-and-sphere-recognition:section` | `AH` |
| III | `courseIII:integral-homology-and-sphere-recognition:section-10` | `AH.1` |
| III | `courseIII:integral-homology-and-sphere-recognition:section-11` | `AH.2` |
| III | `courseIII:integral-homology-and-sphere-recognition:smooth-recognition` | `AH.1` |
| III | `courseIII:integral-homology-and-sphere-recognition:solved-exercises` | `AH.2` |
| III | `courseIII:integral-stable:1` | `AE.1` |
| III | `courseIII:integral-stable:2` | `AE.2` |
| III | `courseIII:integral-stable:3` | `AE.3` |
| III | `courseIII:integral-stable:4` | `AE.4` |
| III | `courseIII:integral-stable:5` | `AE.5` |
| III | `courseIII:integral-stable:6` | `AE.6` |
| III | `courseIII:integral-stable:7` | `AE.7` |
| III | `courseIII:integral-stable:8.1` | `AE.8.1` |
| III | `courseIII:integral-stable:8.2` | `AE.8.2` |
| III | `courseIII:low-index-slides:1` | `S.1` |
| III | `courseIII:low-index-slides:2` | `S.2` |
| III | `courseIII:low-index-slides:3` | `S.3` |
| III | `courseIII:low-index-slides:4` | `S.4` |
| III | `courseIII:low-index-slides:5` | `S.5` |
| III | `courseIII:low-index-slides:6` | `S.6` |
| III | `courseIII:low-index-slides:7` | `S.7` |
| III | `courseIII:low-index-slides:8` | `S.8` |
| III | `courseIII:low-index-slides:9.1` | `S.9.1` |
| III | `courseIII:low-index-slides:9.2` | `S.9.2` |
| III | `courseIII:manifold-duality-the-diagonal-and-wu-classes.source:eq:1.1` | `246` |
| III | `courseIII:manifold-duality-the-diagonal-and-wu-classes.source:eq:1.2` | `247` |
| III | `courseIII:manifold-duality-the-diagonal-and-wu-classes.source:eq:1.3` | `248` |
| III | `courseIII:manifold-duality-the-diagonal-and-wu-classes.source:eq:1.4` | `249` |
| III | `courseIII:manifold-duality-the-diagonal-and-wu-classes.source:eq:1.5` | `250` |
| III | `courseIII:manifold-duality-the-diagonal-and-wu-classes.source:eq:2.1` | `251` |
| III | `courseIII:manifold-duality-the-diagonal-and-wu-classes.source:eq:2.2` | `252` |
| III | `courseIII:manifold-duality-the-diagonal-and-wu-classes.source:eq:3.1` | `253` |
| III | `courseIII:manifold-duality-the-diagonal-and-wu-classes.source:eq:3.2` | `254` |
| III | `courseIII:manifold-duality-the-diagonal-and-wu-classes.source:eq:4.1` | `255` |
| III | `courseIII:manifold-duality-the-diagonal-and-wu-classes.source:eq:4.2` | `256` |
| III | `courseIII:manifold-duality-the-diagonal-and-wu-classes.source:eq:4.3` | `257` |
| III | `courseIII:manifold-duality-the-diagonal-and-wu-classes.source:eq:4.4` | `258` |
| III | `courseIII:manifold-duality-the-diagonal-and-wu-classes.source:eq:4.5` | `259` |
| III | `courseIII:manifold-duality-the-diagonal-and-wu-classes.source:eq:4.6` | `260` |
| III | `courseIII:manifold-duality-the-diagonal-and-wu-classes.source:eq:4.7` | `261` |
| III | `courseIII:manifold-duality-the-diagonal-and-wu-classes.source:eq:4.8` | `262` |
| III | `courseIII:manifold-duality-the-diagonal-and-wu-classes.source:section` | `F` |
| III | `courseIII:manifold-duality-the-diagonal-and-wu-classes.source:section-1` | `F.1` |
| III | `courseIII:manifold-duality-the-diagonal-and-wu-classes.source:section-2` | `F.2` |
| III | `courseIII:manifold-duality-the-diagonal-and-wu-classes.source:section-3` | `F.3` |
| III | `courseIII:manifold-duality-the-diagonal-and-wu-classes.source:section-4` | `F.4` |
| III | `courseIII:middle-cancel:1` | `U.1` |
| III | `courseIII:middle-cancel:2` | `U.2` |
| III | `courseIII:middle-cancel:3` | `U.3` |
| III | `courseIII:middle-cancel:4` | `U.4` |
| III | `courseIII:middle-cancel:5` | `U.5` |
| III | `courseIII:middle-cancel:6` | `U.6` |
| III | `courseIII:middle-cancel:7.1` | `U.7.1` |
| III | `courseIII:middle-cancel:7.2` | `U.7.2` |
| III | `courseIII:milnor-cobar:1.1` | `Z.1` |
| III | `courseIII:milnor-cobar:6.1` | `Z.6` |
| III | `courseIII:milnor-cobar:7.1` | `Z.7.1` |
| III | `courseIII:milnor-cobar:7.2` | `Z.7.2` |
| III | `courseIII:morse-cancel:1` | `J.1` |
| III | `courseIII:morse-cancel:2.1` | `J.2` |
| III | `courseIII:morse-cancel:6` | `J.6` |
| III | `courseIII:morse-cancel:7.1` | `J.7.1` |
| III | `courseIII:morse-cancel:7.2` | `J.7.2` |
| III | `courseIII:morse-cancellation-with-controlled-support:eq:1.1` | `495` |
| III | `courseIII:morse-cancellation-with-controlled-support:eq:1.2` | `496` |
| III | `courseIII:morse-cancellation-with-controlled-support:eq:1.3` | `497` |
| III | `courseIII:morse-cancellation-with-controlled-support:eq:1.4` | `498` |
| III | `courseIII:morse-cancellation-with-controlled-support:eq:1.5` | `499` |
| III | `courseIII:morse-cancellation-with-controlled-support:eq:1.6` | `500` |
| III | `courseIII:morse-cancellation-with-controlled-support:eq:2.1` | `501` |
| III | `courseIII:morse-cancellation-with-controlled-support:eq:3.1` | `502` |
| III | `courseIII:morse-cancellation-with-controlled-support:eq:3.2` | `503` |
| III | `courseIII:morse-cancellation-with-controlled-support:eq:3.3` | `504` |
| III | `courseIII:morse-cancellation-with-controlled-support:eq:3.4` | `505` |
| III | `courseIII:morse-cancellation-with-controlled-support:eq:3.5` | `506` |
| III | `courseIII:morse-cancellation-with-controlled-support:eq:3.6` | `507` |
| III | `courseIII:morse-cancellation-with-controlled-support:eq:3.7` | `508` |
| III | `courseIII:morse-cancellation-with-controlled-support:eq:4.1` | `509` |
| III | `courseIII:morse-cancellation-with-controlled-support:eq:4.2` | `510` |
| III | `courseIII:morse-cancellation-with-controlled-support:eq:4.3` | `511` |
| III | `courseIII:morse-cancellation-with-controlled-support:eq:4.4` | `512` |
| III | `courseIII:morse-cancellation-with-controlled-support:eq:4.5` | `513` |
| III | `courseIII:morse-cancellation-with-controlled-support:eq:5.1` | `514` |
| III | `courseIII:morse-cancellation-with-controlled-support:eq:5.2` | `515` |
| III | `courseIII:morse-cancellation-with-controlled-support:eq:5.3` | `516` |
| III | `courseIII:morse-cancellation-with-controlled-support:eq:5.4` | `517` |
| III | `courseIII:morse-cancellation-with-controlled-support:eq:5.5` | `518` |
| III | `courseIII:morse-cancellation-with-controlled-support:eq:6.1` | `519` |
| III | `courseIII:morse-cancellation-with-controlled-support:eq:6.2` | `520` |
| III | `courseIII:morse-cancellation-with-controlled-support:eq:7.1` | `521` |
| III | `courseIII:morse-cancellation-with-controlled-support:eq:7.2` | `522` |
| III | `courseIII:morse-cancellation-with-controlled-support:eq:7.3` | `523` |
| III | `courseIII:morse-cancellation-with-controlled-support:eq:7.4` | `524` |
| III | `courseIII:morse-cancellation-with-controlled-support:eq:7.5` | `525` |
| III | `courseIII:morse-cancellation-with-controlled-support:eq:7.6` | `526` |
| III | `courseIII:morse-cancellation-with-controlled-support:exercise-7.1` | `J.7.1` |
| III | `courseIII:morse-cancellation-with-controlled-support:exercise-7.2` | `J.7.2` |
| III | `courseIII:morse-cancellation-with-controlled-support:morse-cancellation-data` | `J.2` |
| III | `courseIII:morse-cancellation-with-controlled-support:morse-cancellation-exercises` | `J.7` |
| III | `courseIII:morse-cancellation-with-controlled-support:morse-cancellation-fibres` | `J.3` |
| III | `courseIII:morse-cancellation-with-controlled-support:morse-coordinate-comparison` | `J.1` |
| III | `courseIII:morse-cancellation-with-controlled-support:morse-cutoff-diagram` | `J.3` |
| III | `courseIII:morse-cancellation-with-controlled-support:morse-monotone-minorant` | `J.4` |
| III | `courseIII:morse-cancellation-with-controlled-support:morse-product-map` | `J.6` |
| III | `courseIII:morse-cancellation-with-controlled-support:morse-supported-cutoff` | `J.5` |
| III | `courseIII:morse-cancellation-with-controlled-support:section` | `J` |
| III | `courseIII:morse-cancellation-with-controlled-support:section-1` | `J.1` |
| III | `courseIII:morse-cancellation-with-controlled-support:section-2` | `J.2` |
| III | `courseIII:morse-cancellation-with-controlled-support:section-3` | `J.3` |
| III | `courseIII:morse-cancellation-with-controlled-support:section-4` | `J.4` |
| III | `courseIII:morse-cancellation-with-controlled-support:section-5` | `J.5` |
| III | `courseIII:morse-cancellation-with-controlled-support:section-6` | `J.6` |
| III | `courseIII:morse-cancellation-with-controlled-support:section-7` | `J.7` |
| III | `courseIII:morse-cancellation-with-controlled-support:source-theorem-2.1` | `J.1` |
| III | `courseIII:morse-trajectories-and-critical-value-lowering:eq:0.1` | `580` |
| III | `courseIII:morse-trajectories-and-critical-value-lowering:eq:1.1` | `581` |
| III | `courseIII:morse-trajectories-and-critical-value-lowering:eq:1.10` | `590` |
| III | `courseIII:morse-trajectories-and-critical-value-lowering:eq:1.11` | `591` |
| III | `courseIII:morse-trajectories-and-critical-value-lowering:eq:1.12` | `592` |
| III | `courseIII:morse-trajectories-and-critical-value-lowering:eq:1.2` | `582` |
| III | `courseIII:morse-trajectories-and-critical-value-lowering:eq:1.3` | `583` |
| III | `courseIII:morse-trajectories-and-critical-value-lowering:eq:1.4` | `584` |
| III | `courseIII:morse-trajectories-and-critical-value-lowering:eq:1.5` | `585` |
| III | `courseIII:morse-trajectories-and-critical-value-lowering:eq:1.6` | `586` |
| III | `courseIII:morse-trajectories-and-critical-value-lowering:eq:1.7` | `587` |
| III | `courseIII:morse-trajectories-and-critical-value-lowering:eq:1.8` | `588` |
| III | `courseIII:morse-trajectories-and-critical-value-lowering:eq:1.9` | `589` |
| III | `courseIII:morse-trajectories-and-critical-value-lowering:eq:2.1` | `593` |
| III | `courseIII:morse-trajectories-and-critical-value-lowering:eq:2.2` | `594` |
| III | `courseIII:morse-trajectories-and-critical-value-lowering:eq:2.3` | `595` |
| III | `courseIII:morse-trajectories-and-critical-value-lowering:eq:3.1` | `596` |
| III | `courseIII:morse-trajectories-and-critical-value-lowering:eq:3.10` | `605` |
| III | `courseIII:morse-trajectories-and-critical-value-lowering:eq:3.11` | `606` |
| III | `courseIII:morse-trajectories-and-critical-value-lowering:eq:3.12` | `607` |
| III | `courseIII:morse-trajectories-and-critical-value-lowering:eq:3.13` | `608` |
| III | `courseIII:morse-trajectories-and-critical-value-lowering:eq:3.2` | `597` |
| III | `courseIII:morse-trajectories-and-critical-value-lowering:eq:3.3` | `598` |
| III | `courseIII:morse-trajectories-and-critical-value-lowering:eq:3.4` | `599` |
| III | `courseIII:morse-trajectories-and-critical-value-lowering:eq:3.5` | `600` |
| III | `courseIII:morse-trajectories-and-critical-value-lowering:eq:3.6` | `601` |
| III | `courseIII:morse-trajectories-and-critical-value-lowering:eq:3.7` | `602` |
| III | `courseIII:morse-trajectories-and-critical-value-lowering:eq:3.8` | `603` |
| III | `courseIII:morse-trajectories-and-critical-value-lowering:eq:3.9` | `604` |
| III | `courseIII:morse-trajectories-and-critical-value-lowering:eq:4.1` | `609` |
| III | `courseIII:morse-trajectories-and-critical-value-lowering:eq:4.2` | `610` |
| III | `courseIII:morse-trajectories-and-critical-value-lowering:eq:4.3` | `611` |
| III | `courseIII:morse-trajectories-and-critical-value-lowering:eq:4.4` | `612` |
| III | `courseIII:morse-trajectories-and-critical-value-lowering:eq:4.5` | `613` |
| III | `courseIII:morse-trajectories-and-critical-value-lowering:eq:4.6` | `614` |
| III | `courseIII:morse-trajectories-and-critical-value-lowering:eq:4.7` | `615` |
| III | `courseIII:morse-trajectories-and-critical-value-lowering:eq:4.8` | `616` |
| III | `courseIII:morse-trajectories-and-critical-value-lowering:eq:4.9` | `617` |
| III | `courseIII:morse-trajectories-and-critical-value-lowering:eq:5.1` | `618` |
| III | `courseIII:morse-trajectories-and-critical-value-lowering:eq:5.2` | `619` |
| III | `courseIII:morse-trajectories-and-critical-value-lowering:eq:5.3` | `620` |
| III | `courseIII:morse-trajectories-and-critical-value-lowering:eq:5.4` | `621` |
| III | `courseIII:morse-trajectories-and-critical-value-lowering:eq:5.5` | `622` |
| III | `courseIII:morse-trajectories-and-critical-value-lowering:eq:6.1` | `623` |
| III | `courseIII:morse-trajectories-and-critical-value-lowering:eq:6.10` | `632` |
| III | `courseIII:morse-trajectories-and-critical-value-lowering:eq:6.11` | `633` |
| III | `courseIII:morse-trajectories-and-critical-value-lowering:eq:6.2` | `624` |
| III | `courseIII:morse-trajectories-and-critical-value-lowering:eq:6.3` | `625` |
| III | `courseIII:morse-trajectories-and-critical-value-lowering:eq:6.4` | `626` |
| III | `courseIII:morse-trajectories-and-critical-value-lowering:eq:6.5` | `627` |
| III | `courseIII:morse-trajectories-and-critical-value-lowering:eq:6.6` | `628` |
| III | `courseIII:morse-trajectories-and-critical-value-lowering:eq:6.7` | `629` |
| III | `courseIII:morse-trajectories-and-critical-value-lowering:eq:6.8` | `630` |
| III | `courseIII:morse-trajectories-and-critical-value-lowering:eq:6.9` | `631` |
| III | `courseIII:morse-trajectories-and-critical-value-lowering:section` | `L` |
| III | `courseIII:morse-trajectories-and-critical-value-lowering:section-1` | `L.1` |
| III | `courseIII:morse-trajectories-and-critical-value-lowering:section-1.1` | `L.1.1` |
| III | `courseIII:morse-trajectories-and-critical-value-lowering:section-2` | `L.2` |
| III | `courseIII:morse-trajectories-and-critical-value-lowering:section-3` | `L.3` |
| III | `courseIII:morse-trajectories-and-critical-value-lowering:section-3.1` | `L.3.1` |
| III | `courseIII:morse-trajectories-and-critical-value-lowering:section-4` | `L.4` |
| III | `courseIII:morse-trajectories-and-critical-value-lowering:section-5` | `L.5` |
| III | `courseIII:morse-trajectories-and-critical-value-lowering:section-6` | `L.6` |
| III | `courseIII:morse-trajectories-and-critical-value-lowering:section-6.1` | `L.6.1` |
| III | `courseIII:morse-trajectories-and-critical-value-lowering:section-6.2` | `L.6.2` |
| III | `courseIII:morse-trajectories-and-critical-value-lowering:section-7` | `L.7` |
| III | `courseIII:morse-trajectories-and-critical-value-lowering:trajectory-disk-coordinates` | `L.3` |
| III | `courseIII:morse-trajectories-and-critical-value-lowering:trajectory-holonomy` | `L.1` |
| III | `courseIII:morse-trajectories-and-critical-value-lowering:trajectory-lowering-exercises` | `L.6` |
| III | `courseIII:morse-trajectories-and-critical-value-lowering:trajectory-lowering-sources` | `L.7` |
| III | `courseIII:morse-trajectories-and-critical-value-lowering:trajectory-ordered-morse` | `L.5` |
| III | `courseIII:morse-trajectories-and-critical-value-lowering:trajectory-supported-lowering` | `L.4` |
| III | `courseIII:morse-trajectories-and-critical-value-lowering:trajectory-unstable-disk` | `L.2` |
| III | `courseIII:odd-coop:1` | `AB.1` |
| III | `courseIII:odd-coop:2` | `AB.2` |
| III | `courseIII:odd-coop:3` | `AB.3` |
| III | `courseIII:odd-coop:4` | `AB.4` |
| III | `courseIII:odd-coop:5` | `AB.5` |
| III | `courseIII:odd-coop:6` | `AB.6` |
| III | `courseIII:odd-coop:7.1` | `AB.7.1` |
| III | `courseIII:odd-coop:7.2` | `AB.7.2` |
| III | `courseIII:pair-creation:1` | `K.1` |
| III | `courseIII:pair-creation:2` | `K.2` |
| III | `courseIII:pair-creation:3` | `K.3` |
| III | `courseIII:pair-creation:4` | `K.4` |
| III | `courseIII:pair-creation:5` | `K.5` |
| III | `courseIII:pair-creation:6` | `K.6` |
| III | `courseIII:pair-creation:7.1` | `K.7.1` |
| III | `courseIII:pair-creation:7.2` | `K.7.2` |
| III | `courseIII:pontryagin-thom:1` | `G.1` |
| III | `courseIII:pontryagin-thom:2` | `G.2` |
| III | `courseIII:pontryagin-thom:3` | `G.3` |
| III | `courseIII:pontryagin-thom:4` | `G.4` |
| III | `courseIII:pontryagin-thom:5` | `G.5` |
| III | `courseIII:pontryagin-thom:6` | `G.6` |
| III | `courseIII:pontryagin-thom:7` | `G.7` |
| III | `courseIII:pontryagin-thom:8` | `G.8` |
| III | `courseIII:pontryagin-thom:9.1` | `G.9.1` |
| III | `courseIII:pontryagin-thom:9.2` | `G.9.2` |
| III | `courseIII:projective-coop:1` | `W.1` |
| III | `courseIII:projective-coop:2` | `W.2` |
| III | `courseIII:projective-coop:3` | `W.3` |
| III | `courseIII:projective-coop:4` | `W.4` |
| III | `courseIII:projective-coop:5` | `W.5` |
| III | `courseIII:projective-coop:6.1` | `W.6.1` |
| III | `courseIII:projective-coop:6.2` | `W.6.2` |
| III | `courseIII:projective-splitting-for-lesson11:CG-S6-PROJECTIVE-1` | `D.1` |
| III | `courseIII:projective-splitting-for-lesson11:CG-S6-PROJECTIVE-2` | `D.2` |
| III | `courseIII:projective-splitting-for-lesson11:CG-S6-PROJECTIVE-3` | `D.3` |
| III | `courseIII:projective-splitting-for-lesson11:CG-S6-PROJECTIVE-4` | `D.4` |
| III | `courseIII:projective-splitting-for-lesson11:CG-S6-PROJECTIVE-5` | `D.5` |
| III | `courseIII:projective-splitting-for-lesson11:eq:1.1` | `228` |
| III | `courseIII:projective-splitting-for-lesson11:eq:1.2` | `229` |
| III | `courseIII:projective-splitting-for-lesson11:eq:2.1` | `230` |
| III | `courseIII:projective-splitting-for-lesson11:eq:2.2` | `231` |
| III | `courseIII:projective-splitting-for-lesson11:eq:3.1` | `232` |
| III | `courseIII:projective-splitting-for-lesson11:eq:3.2` | `233` |
| III | `courseIII:projective-splitting-for-lesson11:eq:4.1` | `234` |
| III | `courseIII:projective-splitting-for-lesson11:eq:5.1` | `235` |
| III | `courseIII:projective-splitting-for-lesson11:finite-projective-space` | `D.2` |
| III | `courseIII:projective-splitting-for-lesson11:gysin-maps` | `D.1` |
| III | `courseIII:projective-splitting-for-lesson11:integral-flag-map` | `D.4` |
| III | `courseIII:projective-splitting-for-lesson11:line-tensor-rule` | `D.5` |
| III | `courseIII:projective-splitting-for-lesson11:projective-module` | `D.3` |
| III | `courseIII:projective-splitting-for-lesson11:section` | `D` |
| III | `courseIII:projective-splitting-for-lesson11:section-1` | `D.1` |
| III | `courseIII:projective-splitting-for-lesson11:section-2` | `D.2` |
| III | `courseIII:projective-splitting-for-lesson11:section-3` | `D.3` |
| III | `courseIII:projective-splitting-for-lesson11:section-4` | `D.4` |
| III | `courseIII:projective-splitting-for-lesson11:section-5` | `D.5` |
| III | `courseIII:pt-abstract-framed-comparison` | `G.4` |
| III | `courseIII:pt-normal-inverse-comparison` | `G.3` |
| III | `courseIII:pt-relative-embedding` | `G.1` |
| III | `courseIII:pt-relative-embedding-setup` | `G.10` |
| III | `courseIII:pt-relative-normal-frame` | `G.2` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:eq:1.1` | `1170` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:eq:1.2` | `1171` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:eq:1.3` | `1172` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:eq:1.4` | `1173` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:eq:1.5` | `1174` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:eq:1.6` | `1175` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:eq:1.7` | `1176` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:eq:1.8` | `1177` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:eq:1.9` | `1178` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:eq:2.1` | `1179` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:eq:2.10` | `1188` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:eq:2.11` | `1189` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:eq:2.12` | `1190` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:eq:2.13` | `1191` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:eq:2.14` | `1192` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:eq:2.15` | `1193` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:eq:2.16` | `1194` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:eq:2.17` | `1195` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:eq:2.18` | `1196` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:eq:2.19` | `1197` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:eq:2.2` | `1180` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:eq:2.20` | `1198` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:eq:2.21` | `1199` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:eq:2.22` | `1200` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:eq:2.23` | `1201` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:eq:2.3` | `1181` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:eq:2.4` | `1182` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:eq:2.5` | `1183` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:eq:2.6` | `1184` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:eq:2.7` | `1185` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:eq:2.8` | `1186` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:eq:2.9` | `1187` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:eq:3.1` | `1202` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:eq:3.10` | `1212` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:eq:3.11` | `1213` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:eq:3.12` | `1214` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:eq:3.13` | `1215` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:eq:3.14` | `1216` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:eq:3.2` | `1203` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:eq:3.3` | `1204` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:eq:3.4` | `1205` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:eq:3.4a` | `1206` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:eq:3.5` | `1207` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:eq:3.6` | `1208` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:eq:3.7` | `1209` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:eq:3.8` | `1210` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:eq:3.9` | `1211` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:eq:4.1` | `1217` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:eq:4.2` | `1218` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:eq:4.3` | `1219` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:eq:4.4` | `1220` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:eq:4.5` | `1221` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:eq:4.6` | `1222` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:eq:4.7` | `1223` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:eq:5.1` | `1224` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:eq:5.2` | `1225` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:eq:5.3` | `1226` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:eq:5.4` | `1227` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:eq:5.5` | `1228` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:eq:5.6` | `1229` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:eq:5.7` | `1230` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:eq:6.1` | `1231` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:eq:6.2` | `1232` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:eq:6.3` | `1233` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:eq:6.4` | `1234` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:eq:6.5` | `1235` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:eq:6.6` | `1236` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:eq:6.7` | `1237` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:eq:6.8` | `1238` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:eq:7.1` | `1239` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:eq:7.10` | `1248` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:eq:7.11` | `1249` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:eq:7.12` | `1250` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:eq:7.2` | `1240` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:eq:7.3` | `1241` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:eq:7.4` | `1242` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:eq:7.5` | `1243` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:eq:7.6` | `1244` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:eq:7.7` | `1245` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:eq:7.8` | `1246` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:eq:7.9` | `1247` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:exercise-1` | `U.7.1` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:exercise-2` | `U.7.2` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:middle-actual-incidence` | `U.4` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:middle-collar-comparison` | `U.1` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:middle-level-comparisons` | `U.3` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:middle-realization-exercises` | `U.7` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:middle-realization-sources` | `U.8` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:middle-realize-stage` | `U.2` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:middle-six-seven-reduction` | `U.6` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:middle-trajectory-cancellation` | `U.5` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:section` | `U` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:section-1` | `U.1` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:section-2` | `U.2` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:section-3` | `U.3` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:section-4` | `U.4` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:section-5` | `U.5` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:section-6` | `U.6` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:section-7` | `U.7` |
| III | `courseIII:realizing-framed-handles-and-middle-cancellation:section-8` | `U.8` |
| III | `courseIII:rearranging-the-original-framed-handles:arrangement-boundary-comparison` | `M.1` |
| III | `courseIII:rearranging-the-original-framed-handles:arrangement-exercises` | `M.5` |
| III | `courseIII:rearranging-the-original-framed-handles:arrangement-interchange` | `M.4` |
| III | `courseIII:rearranging-the-original-framed-handles:arrangement-outward-motion` | `M.3` |
| III | `courseIII:rearranging-the-original-framed-handles:arrangement-tube-compression` | `M.2` |
| III | `courseIII:rearranging-the-original-framed-handles:eq:1.1` | `634` |
| III | `courseIII:rearranging-the-original-framed-handles:eq:1.10` | `643` |
| III | `courseIII:rearranging-the-original-framed-handles:eq:1.11` | `644` |
| III | `courseIII:rearranging-the-original-framed-handles:eq:1.12` | `645` |
| III | `courseIII:rearranging-the-original-framed-handles:eq:1.13` | `646` |
| III | `courseIII:rearranging-the-original-framed-handles:eq:1.14` | `647` |
| III | `courseIII:rearranging-the-original-framed-handles:eq:1.15` | `648` |
| III | `courseIII:rearranging-the-original-framed-handles:eq:1.16` | `649` |
| III | `courseIII:rearranging-the-original-framed-handles:eq:1.17` | `650` |
| III | `courseIII:rearranging-the-original-framed-handles:eq:1.18` | `651` |
| III | `courseIII:rearranging-the-original-framed-handles:eq:1.19` | `652` |
| III | `courseIII:rearranging-the-original-framed-handles:eq:1.2` | `635` |
| III | `courseIII:rearranging-the-original-framed-handles:eq:1.3` | `636` |
| III | `courseIII:rearranging-the-original-framed-handles:eq:1.4` | `637` |
| III | `courseIII:rearranging-the-original-framed-handles:eq:1.5` | `638` |
| III | `courseIII:rearranging-the-original-framed-handles:eq:1.6` | `639` |
| III | `courseIII:rearranging-the-original-framed-handles:eq:1.7` | `640` |
| III | `courseIII:rearranging-the-original-framed-handles:eq:1.8` | `641` |
| III | `courseIII:rearranging-the-original-framed-handles:eq:1.9` | `642` |
| III | `courseIII:rearranging-the-original-framed-handles:eq:2.1` | `653` |
| III | `courseIII:rearranging-the-original-framed-handles:eq:2.2` | `654` |
| III | `courseIII:rearranging-the-original-framed-handles:eq:2.3` | `655` |
| III | `courseIII:rearranging-the-original-framed-handles:eq:2.4` | `656` |
| III | `courseIII:rearranging-the-original-framed-handles:eq:2.5` | `657` |
| III | `courseIII:rearranging-the-original-framed-handles:eq:2.6` | `658` |
| III | `courseIII:rearranging-the-original-framed-handles:eq:2.7` | `659` |
| III | `courseIII:rearranging-the-original-framed-handles:eq:2.8` | `660` |
| III | `courseIII:rearranging-the-original-framed-handles:eq:3.1` | `661` |
| III | `courseIII:rearranging-the-original-framed-handles:eq:3.10` | `670` |
| III | `courseIII:rearranging-the-original-framed-handles:eq:3.11` | `671` |
| III | `courseIII:rearranging-the-original-framed-handles:eq:3.2` | `662` |
| III | `courseIII:rearranging-the-original-framed-handles:eq:3.3` | `663` |
| III | `courseIII:rearranging-the-original-framed-handles:eq:3.4` | `664` |
| III | `courseIII:rearranging-the-original-framed-handles:eq:3.5` | `665` |
| III | `courseIII:rearranging-the-original-framed-handles:eq:3.6` | `666` |
| III | `courseIII:rearranging-the-original-framed-handles:eq:3.7` | `667` |
| III | `courseIII:rearranging-the-original-framed-handles:eq:3.8` | `668` |
| III | `courseIII:rearranging-the-original-framed-handles:eq:3.9` | `669` |
| III | `courseIII:rearranging-the-original-framed-handles:eq:4.1` | `672` |
| III | `courseIII:rearranging-the-original-framed-handles:eq:4.10` | `681` |
| III | `courseIII:rearranging-the-original-framed-handles:eq:4.11` | `682` |
| III | `courseIII:rearranging-the-original-framed-handles:eq:4.12` | `683` |
| III | `courseIII:rearranging-the-original-framed-handles:eq:4.13` | `684` |
| III | `courseIII:rearranging-the-original-framed-handles:eq:4.14` | `685` |
| III | `courseIII:rearranging-the-original-framed-handles:eq:4.15` | `686` |
| III | `courseIII:rearranging-the-original-framed-handles:eq:4.16` | `687` |
| III | `courseIII:rearranging-the-original-framed-handles:eq:4.17` | `688` |
| III | `courseIII:rearranging-the-original-framed-handles:eq:4.2` | `673` |
| III | `courseIII:rearranging-the-original-framed-handles:eq:4.3` | `674` |
| III | `courseIII:rearranging-the-original-framed-handles:eq:4.4` | `675` |
| III | `courseIII:rearranging-the-original-framed-handles:eq:4.5` | `676` |
| III | `courseIII:rearranging-the-original-framed-handles:eq:4.6` | `677` |
| III | `courseIII:rearranging-the-original-framed-handles:eq:4.7` | `678` |
| III | `courseIII:rearranging-the-original-framed-handles:eq:4.8` | `679` |
| III | `courseIII:rearranging-the-original-framed-handles:eq:4.9` | `680` |
| III | `courseIII:rearranging-the-original-framed-handles:eq:5.1` | `689` |
| III | `courseIII:rearranging-the-original-framed-handles:eq:5.10` | `698` |
| III | `courseIII:rearranging-the-original-framed-handles:eq:5.2` | `690` |
| III | `courseIII:rearranging-the-original-framed-handles:eq:5.3` | `691` |
| III | `courseIII:rearranging-the-original-framed-handles:eq:5.4` | `692` |
| III | `courseIII:rearranging-the-original-framed-handles:eq:5.5` | `693` |
| III | `courseIII:rearranging-the-original-framed-handles:eq:5.6` | `694` |
| III | `courseIII:rearranging-the-original-framed-handles:eq:5.7` | `695` |
| III | `courseIII:rearranging-the-original-framed-handles:eq:5.8` | `696` |
| III | `courseIII:rearranging-the-original-framed-handles:eq:5.9` | `697` |
| III | `courseIII:rearranging-the-original-framed-handles:exercise-5.1` | `M.5.1` |
| III | `courseIII:rearranging-the-original-framed-handles:exercise-5.2` | `M.5.2` |
| III | `courseIII:rearranging-the-original-framed-handles:section` | `M` |
| III | `courseIII:rearranging-the-original-framed-handles:section-1` | `M.1` |
| III | `courseIII:rearranging-the-original-framed-handles:section-1.1` | `M.1.1` |
| III | `courseIII:rearranging-the-original-framed-handles:section-1.2` | `M.1.2` |
| III | `courseIII:rearranging-the-original-framed-handles:section-1.3` | `M.1.3` |
| III | `courseIII:rearranging-the-original-framed-handles:section-2` | `M.2` |
| III | `courseIII:rearranging-the-original-framed-handles:section-3` | `M.3` |
| III | `courseIII:rearranging-the-original-framed-handles:section-4` | `M.4` |
| III | `courseIII:rearranging-the-original-framed-handles:section-4.1` | `M.4.1` |
| III | `courseIII:rearranging-the-original-framed-handles:section-4.2` | `M.4.2` |
| III | `courseIII:rearranging-the-original-framed-handles:section-4.3` | `M.4.3` |
| III | `courseIII:rearranging-the-original-framed-handles:section-4.4` | `M.4.4` |
| III | `courseIII:rearranging-the-original-framed-handles:section-5` | `M.5` |
| III | `courseIII:relative-morse-functions-and-original-handles:eq:1.1` | `409` |
| III | `courseIII:relative-morse-functions-and-original-handles:eq:1.2` | `410` |
| III | `courseIII:relative-morse-functions-and-original-handles:eq:1.3` | `411` |
| III | `courseIII:relative-morse-functions-and-original-handles:eq:1.4` | `412` |
| III | `courseIII:relative-morse-functions-and-original-handles:eq:1.5` | `413` |
| III | `courseIII:relative-morse-functions-and-original-handles:eq:1.6` | `414` |
| III | `courseIII:relative-morse-functions-and-original-handles:eq:1.7` | `415` |
| III | `courseIII:relative-morse-functions-and-original-handles:eq:1.8` | `416` |
| III | `courseIII:relative-morse-functions-and-original-handles:eq:1.9` | `417` |
| III | `courseIII:relative-morse-functions-and-original-handles:eq:2.1` | `418` |
| III | `courseIII:relative-morse-functions-and-original-handles:eq:2.10` | `427` |
| III | `courseIII:relative-morse-functions-and-original-handles:eq:2.11` | `428` |
| III | `courseIII:relative-morse-functions-and-original-handles:eq:2.12` | `429` |
| III | `courseIII:relative-morse-functions-and-original-handles:eq:2.13` | `430` |
| III | `courseIII:relative-morse-functions-and-original-handles:eq:2.14` | `431` |
| III | `courseIII:relative-morse-functions-and-original-handles:eq:2.2` | `419` |
| III | `courseIII:relative-morse-functions-and-original-handles:eq:2.3` | `420` |
| III | `courseIII:relative-morse-functions-and-original-handles:eq:2.4` | `421` |
| III | `courseIII:relative-morse-functions-and-original-handles:eq:2.5` | `422` |
| III | `courseIII:relative-morse-functions-and-original-handles:eq:2.6` | `423` |
| III | `courseIII:relative-morse-functions-and-original-handles:eq:2.7` | `424` |
| III | `courseIII:relative-morse-functions-and-original-handles:eq:2.8` | `425` |
| III | `courseIII:relative-morse-functions-and-original-handles:eq:2.9` | `426` |
| III | `courseIII:relative-morse-functions-and-original-handles:eq:3.1` | `432` |
| III | `courseIII:relative-morse-functions-and-original-handles:eq:3.10` | `441` |
| III | `courseIII:relative-morse-functions-and-original-handles:eq:3.11` | `442` |
| III | `courseIII:relative-morse-functions-and-original-handles:eq:3.12` | `443` |
| III | `courseIII:relative-morse-functions-and-original-handles:eq:3.13` | `444` |
| III | `courseIII:relative-morse-functions-and-original-handles:eq:3.2` | `433` |
| III | `courseIII:relative-morse-functions-and-original-handles:eq:3.3` | `434` |
| III | `courseIII:relative-morse-functions-and-original-handles:eq:3.4` | `435` |
| III | `courseIII:relative-morse-functions-and-original-handles:eq:3.5` | `436` |
| III | `courseIII:relative-morse-functions-and-original-handles:eq:3.6` | `437` |
| III | `courseIII:relative-morse-functions-and-original-handles:eq:3.7` | `438` |
| III | `courseIII:relative-morse-functions-and-original-handles:eq:3.8` | `439` |
| III | `courseIII:relative-morse-functions-and-original-handles:eq:3.9` | `440` |
| III | `courseIII:relative-morse-functions-and-original-handles:eq:4.1` | `445` |
| III | `courseIII:relative-morse-functions-and-original-handles:eq:4.10` | `454` |
| III | `courseIII:relative-morse-functions-and-original-handles:eq:4.11` | `455` |
| III | `courseIII:relative-morse-functions-and-original-handles:eq:4.12` | `456` |
| III | `courseIII:relative-morse-functions-and-original-handles:eq:4.13` | `457` |
| III | `courseIII:relative-morse-functions-and-original-handles:eq:4.14` | `458` |
| III | `courseIII:relative-morse-functions-and-original-handles:eq:4.15` | `459` |
| III | `courseIII:relative-morse-functions-and-original-handles:eq:4.16` | `460` |
| III | `courseIII:relative-morse-functions-and-original-handles:eq:4.17` | `461` |
| III | `courseIII:relative-morse-functions-and-original-handles:eq:4.18` | `462` |
| III | `courseIII:relative-morse-functions-and-original-handles:eq:4.19` | `463` |
| III | `courseIII:relative-morse-functions-and-original-handles:eq:4.2` | `446` |
| III | `courseIII:relative-morse-functions-and-original-handles:eq:4.20` | `464` |
| III | `courseIII:relative-morse-functions-and-original-handles:eq:4.21` | `465` |
| III | `courseIII:relative-morse-functions-and-original-handles:eq:4.22` | `466` |
| III | `courseIII:relative-morse-functions-and-original-handles:eq:4.23` | `467` |
| III | `courseIII:relative-morse-functions-and-original-handles:eq:4.24` | `468` |
| III | `courseIII:relative-morse-functions-and-original-handles:eq:4.25` | `469` |
| III | `courseIII:relative-morse-functions-and-original-handles:eq:4.26` | `470` |
| III | `courseIII:relative-morse-functions-and-original-handles:eq:4.27` | `471` |
| III | `courseIII:relative-morse-functions-and-original-handles:eq:4.28` | `472` |
| III | `courseIII:relative-morse-functions-and-original-handles:eq:4.29` | `473` |
| III | `courseIII:relative-morse-functions-and-original-handles:eq:4.3` | `447` |
| III | `courseIII:relative-morse-functions-and-original-handles:eq:4.30` | `474` |
| III | `courseIII:relative-morse-functions-and-original-handles:eq:4.31` | `475` |
| III | `courseIII:relative-morse-functions-and-original-handles:eq:4.32` | `476` |
| III | `courseIII:relative-morse-functions-and-original-handles:eq:4.33` | `477` |
| III | `courseIII:relative-morse-functions-and-original-handles:eq:4.34` | `478` |
| III | `courseIII:relative-morse-functions-and-original-handles:eq:4.35` | `479` |
| III | `courseIII:relative-morse-functions-and-original-handles:eq:4.36` | `480` |
| III | `courseIII:relative-morse-functions-and-original-handles:eq:4.37` | `481` |
| III | `courseIII:relative-morse-functions-and-original-handles:eq:4.38` | `482` |
| III | `courseIII:relative-morse-functions-and-original-handles:eq:4.4` | `448` |
| III | `courseIII:relative-morse-functions-and-original-handles:eq:4.5` | `449` |
| III | `courseIII:relative-morse-functions-and-original-handles:eq:4.6` | `450` |
| III | `courseIII:relative-morse-functions-and-original-handles:eq:4.7` | `451` |
| III | `courseIII:relative-morse-functions-and-original-handles:eq:4.8` | `452` |
| III | `courseIII:relative-morse-functions-and-original-handles:eq:4.9` | `453` |
| III | `courseIII:relative-morse-functions-and-original-handles:eq:5.1` | `483` |
| III | `courseIII:relative-morse-functions-and-original-handles:eq:5.10` | `492` |
| III | `courseIII:relative-morse-functions-and-original-handles:eq:5.11` | `493` |
| III | `courseIII:relative-morse-functions-and-original-handles:eq:5.12` | `494` |
| III | `courseIII:relative-morse-functions-and-original-handles:eq:5.2` | `484` |
| III | `courseIII:relative-morse-functions-and-original-handles:eq:5.3` | `485` |
| III | `courseIII:relative-morse-functions-and-original-handles:eq:5.4` | `486` |
| III | `courseIII:relative-morse-functions-and-original-handles:eq:5.5` | `487` |
| III | `courseIII:relative-morse-functions-and-original-handles:eq:5.6` | `488` |
| III | `courseIII:relative-morse-functions-and-original-handles:eq:5.7` | `489` |
| III | `courseIII:relative-morse-functions-and-original-handles:eq:5.8` | `490` |
| III | `courseIII:relative-morse-functions-and-original-handles:eq:5.9` | `491` |
| III | `courseIII:relative-morse-functions-and-original-handles:exercise-5.1` | `I.5.1` |
| III | `courseIII:relative-morse-functions-and-original-handles:exercise-5.2` | `I.5.2` |
| III | `courseIII:relative-morse-functions-and-original-handles:relative-morse-attachment` | `I.4` |
| III | `courseIII:relative-morse-functions-and-original-handles:relative-morse-exercises` | `I.5` |
| III | `courseIII:relative-morse-functions-and-original-handles:relative-morse-existence` | `I.1` |
| III | `courseIII:relative-morse-functions-and-original-handles:relative-morse-hessian` | `I.2` |
| III | `courseIII:relative-morse-functions-and-original-handles:relative-morse-levels` | `I.3` |
| III | `courseIII:relative-morse-functions-and-original-handles:section` | `I` |
| III | `courseIII:relative-morse-functions-and-original-handles:section-1` | `I.1` |
| III | `courseIII:relative-morse-functions-and-original-handles:section-2` | `I.2` |
| III | `courseIII:relative-morse-functions-and-original-handles:section-3` | `I.3` |
| III | `courseIII:relative-morse-functions-and-original-handles:section-3.1` | `I.3.1` |
| III | `courseIII:relative-morse-functions-and-original-handles:section-3.2` | `I.3.2` |
| III | `courseIII:relative-morse-functions-and-original-handles:section-3.3` | `I.3.3` |
| III | `courseIII:relative-morse-functions-and-original-handles:section-4` | `I.4` |
| III | `courseIII:relative-morse-functions-and-original-handles:section-4.1` | `I.4.1` |
| III | `courseIII:relative-morse-functions-and-original-handles:section-4.2` | `I.4.2` |
| III | `courseIII:relative-morse-functions-and-original-handles:section-4.3` | `I.4.3` |
| III | `courseIII:relative-morse-functions-and-original-handles:section-4.4` | `I.4.4` |
| III | `courseIII:relative-morse-functions-and-original-handles:section-5` | `I.5` |
| III | `courseIII:relative-morse:1` | `I.1` |
| III | `courseIII:relative-morse:2` | `I.2` |
| III | `courseIII:relative-morse:3` | `I.3` |
| III | `courseIII:relative-morse:4` | `I.4` |
| III | `courseIII:relative-morse:5.1` | `I.5.1` |
| III | `courseIII:relative-morse:5.2` | `I.5.2` |
| III | `courseIII:removing-the-original-zero-and-top-handles:eq:0.1` | `699` |
| III | `courseIII:removing-the-original-zero-and-top-handles:eq:0.2` | `700` |
| III | `courseIII:removing-the-original-zero-and-top-handles:eq:1.1` | `701` |
| III | `courseIII:removing-the-original-zero-and-top-handles:eq:1.2` | `702` |
| III | `courseIII:removing-the-original-zero-and-top-handles:eq:1.3` | `703` |
| III | `courseIII:removing-the-original-zero-and-top-handles:eq:1.4` | `704` |
| III | `courseIII:removing-the-original-zero-and-top-handles:eq:2.1` | `705` |
| III | `courseIII:removing-the-original-zero-and-top-handles:eq:2.2` | `706` |
| III | `courseIII:removing-the-original-zero-and-top-handles:eq:2.3` | `707` |
| III | `courseIII:removing-the-original-zero-and-top-handles:eq:3.1` | `708` |
| III | `courseIII:removing-the-original-zero-and-top-handles:eq:3.2` | `709` |
| III | `courseIII:removing-the-original-zero-and-top-handles:eq:3.3` | `710` |
| III | `courseIII:removing-the-original-zero-and-top-handles:eq:3.4` | `711` |
| III | `courseIII:removing-the-original-zero-and-top-handles:eq:4.1` | `712` |
| III | `courseIII:removing-the-original-zero-and-top-handles:eq:4.2` | `713` |
| III | `courseIII:removing-the-original-zero-and-top-handles:eq:4.3` | `714` |
| III | `courseIII:removing-the-original-zero-and-top-handles:eq:4.4` | `715` |
| III | `courseIII:removing-the-original-zero-and-top-handles:eq:4.5` | `716` |
| III | `courseIII:removing-the-original-zero-and-top-handles:eq:4.6` | `717` |
| III | `courseIII:removing-the-original-zero-and-top-handles:eq:4.7` | `718` |
| III | `courseIII:removing-the-original-zero-and-top-handles:eq:5.1` | `719` |
| III | `courseIII:removing-the-original-zero-and-top-handles:eq:5.2` | `720` |
| III | `courseIII:removing-the-original-zero-and-top-handles:eq:5.3` | `721` |
| III | `courseIII:removing-the-original-zero-and-top-handles:eq:5.4` | `722` |
| III | `courseIII:removing-the-original-zero-and-top-handles:eq:6.1` | `723` |
| III | `courseIII:removing-the-original-zero-and-top-handles:eq:6.2` | `724` |
| III | `courseIII:removing-the-original-zero-and-top-handles:eq:6.3` | `725` |
| III | `courseIII:removing-the-original-zero-and-top-handles:eq:6.4` | `726` |
| III | `courseIII:removing-the-original-zero-and-top-handles:eq:6.5` | `727` |
| III | `courseIII:removing-the-original-zero-and-top-handles:section` | `N` |
| III | `courseIII:removing-the-original-zero-and-top-handles:section-1` | `N.1` |
| III | `courseIII:removing-the-original-zero-and-top-handles:section-2` | `N.2` |
| III | `courseIII:removing-the-original-zero-and-top-handles:section-3` | `N.3` |
| III | `courseIII:removing-the-original-zero-and-top-handles:section-4` | `N.4` |
| III | `courseIII:removing-the-original-zero-and-top-handles:section-5` | `N.5` |
| III | `courseIII:removing-the-original-zero-and-top-handles:section-6` | `N.6` |
| III | `courseIII:removing-the-original-zero-and-top-handles:section-6.1` | `N.6.1` |
| III | `courseIII:removing-the-original-zero-and-top-handles:section-6.2` | `N.6.2` |
| III | `courseIII:removing-the-original-zero-and-top-handles:section-7` | `N.7` |
| III | `courseIII:removing-the-original-zero-and-top-handles:zero-branch-arrangement` | `N.1` |
| III | `courseIII:removing-the-original-zero-and-top-handles:zero-component-graph` | `N.2` |
| III | `courseIII:removing-the-original-zero-and-top-handles:zero-dual-top` | `N.4` |
| III | `courseIII:removing-the-original-zero-and-top-handles:zero-exercises` | `N.6` |
| III | `courseIII:removing-the-original-zero-and-top-handles:zero-presentation-comparison` | `N.5` |
| III | `courseIII:removing-the-original-zero-and-top-handles:zero-sources` | `N.7` |
| III | `courseIII:removing-the-original-zero-and-top-handles:zero-supported-cancellation` | `N.3` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:eq:1.1` | `1918` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:eq:1.10` | `1927` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:eq:1.11` | `1928` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:eq:1.12` | `1929` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:eq:1.13` | `1930` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:eq:1.14` | `1931` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:eq:1.2` | `1919` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:eq:1.3` | `1920` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:eq:1.4` | `1921` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:eq:1.5` | `1922` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:eq:1.6` | `1923` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:eq:1.7` | `1924` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:eq:1.8` | `1925` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:eq:1.9` | `1926` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:eq:2.1` | `1932` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:eq:2.2` | `1933` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:eq:2.3` | `1934` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:eq:2.4` | `1935` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:eq:2.5` | `1936` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:eq:2.6` | `1937` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:eq:2.7` | `1938` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:eq:3.1` | `1939` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:eq:3.10` | `1948` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:eq:3.11` | `1949` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:eq:3.2` | `1940` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:eq:3.3` | `1941` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:eq:3.4` | `1942` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:eq:3.5` | `1943` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:eq:3.6` | `1944` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:eq:3.7` | `1945` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:eq:3.8` | `1946` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:eq:3.9` | `1947` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:eq:4.1` | `1950` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:eq:4.10` | `1959` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:eq:4.11` | `1960` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:eq:4.2` | `1951` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:eq:4.3` | `1952` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:eq:4.4` | `1953` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:eq:4.5` | `1954` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:eq:4.6` | `1955` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:eq:4.7` | `1956` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:eq:4.8` | `1957` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:eq:4.9` | `1958` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:eq:5.1` | `1961` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:eq:5.2` | `1962` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:eq:5.3` | `1963` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:eq:5.4` | `1964` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:eq:5.5` | `1965` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:eq:5.6` | `1966` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:eq:5.7` | `1967` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:eq:6.1` | `1968` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:eq:6.2` | `1969` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:eq:6.3` | `1970` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:eq:6.4` | `1971` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:eq:6.5` | `1972` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:eq:6.6` | `1973` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:eq:6.7` | `1974` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:eq:6.8` | `1975` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:eq:7.1` | `1976` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:eq:7.10` | `1985` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:eq:7.11` | `1986` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:eq:7.12` | `1987` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:eq:7.13` | `1988` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:eq:7.14` | `1989` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:eq:7.15` | `1990` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:eq:7.16` | `1991` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:eq:7.17` | `1992` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:eq:7.18` | `1993` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:eq:7.19` | `1994` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:eq:7.2` | `1977` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:eq:7.3` | `1978` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:eq:7.4` | `1979` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:eq:7.5` | `1980` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:eq:7.6` | `1981` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:eq:7.7` | `1982` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:eq:7.8` | `1983` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:eq:7.9` | `1984` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:eq:8.1` | `1995` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:eq:8.10` | `2004` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:eq:8.2` | `1996` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:eq:8.3` | `1997` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:eq:8.4` | `1998` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:eq:8.5` | `1999` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:eq:8.6` | `2000` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:eq:8.7` | `2001` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:eq:8.8` | `2002` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:eq:8.9` | `2003` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:exercise-8.1` | `AG.8.1` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:exercise-8.2` | `AG.8.2` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:section` | `AG` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:section-1` | `AG.1` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:section-2` | `AG.2` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:section-3` | `AG.3` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:section-4` | `AG.4` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:section-5` | `AG.5` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:section-6` | `AG.6` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:section-7` | `AG.7` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:section-7.1` | `AG.7.1` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:section-8` | `AG.8` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:twist-actual-cancellation` | `AG.6` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:twist-actual-tube` | `AG.1` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:twist-general-stable-framing` | `AG.7.1` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:twist-integral-lagrangians` | `AG.3` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:twist-original-gluing` | `AG.5` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:twist-original-middle-level` | `AG.4` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:twist-original-smooth-map` | `AG.7` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:twist-signed-action` | `AG.2` |
| III | `courseIII:sphere-twists-and-the-original-smooth-six-sphere-comparison:twist-worked-exercises` | `AG.8` |
| III | `courseIII:spin-six-and-the-framing-comparison:eq:1.1` | `367` |
| III | `courseIII:spin-six-and-the-framing-comparison:eq:1.2` | `368` |
| III | `courseIII:spin-six-and-the-framing-comparison:eq:1.3` | `369` |
| III | `courseIII:spin-six-and-the-framing-comparison:eq:1.4` | `370` |
| III | `courseIII:spin-six-and-the-framing-comparison:eq:1.5` | `371` |
| III | `courseIII:spin-six-and-the-framing-comparison:eq:1.6` | `372` |
| III | `courseIII:spin-six-and-the-framing-comparison:eq:1.7` | `373` |
| III | `courseIII:spin-six-and-the-framing-comparison:eq:1.8` | `374` |
| III | `courseIII:spin-six-and-the-framing-comparison:eq:1.9` | `375` |
| III | `courseIII:spin-six-and-the-framing-comparison:eq:2.1` | `376` |
| III | `courseIII:spin-six-and-the-framing-comparison:eq:2.2` | `377` |
| III | `courseIII:spin-six-and-the-framing-comparison:eq:2.3` | `378` |
| III | `courseIII:spin-six-and-the-framing-comparison:eq:2.4` | `379` |
| III | `courseIII:spin-six-and-the-framing-comparison:eq:2.5` | `380` |
| III | `courseIII:spin-six-and-the-framing-comparison:eq:2.6` | `381` |
| III | `courseIII:spin-six-and-the-framing-comparison:eq:2.7` | `382` |
| III | `courseIII:spin-six-and-the-framing-comparison:eq:2.8` | `383` |
| III | `courseIII:spin-six-and-the-framing-comparison:eq:3.1` | `384` |
| III | `courseIII:spin-six-and-the-framing-comparison:eq:3.2` | `385` |
| III | `courseIII:spin-six-and-the-framing-comparison:eq:3.3` | `386` |
| III | `courseIII:spin-six-and-the-framing-comparison:eq:3.4` | `387` |
| III | `courseIII:spin-six-and-the-framing-comparison:eq:3.5` | `388` |
| III | `courseIII:spin-six-and-the-framing-comparison:eq:4.1` | `389` |
| III | `courseIII:spin-six-and-the-framing-comparison:eq:4.2` | `390` |
| III | `courseIII:spin-six-and-the-framing-comparison:eq:4.3` | `391` |
| III | `courseIII:spin-six-and-the-framing-comparison:eq:4.4` | `392` |
| III | `courseIII:spin-six-and-the-framing-comparison:eq:4.5` | `393` |
| III | `courseIII:spin-six-and-the-framing-comparison:eq:4.6` | `394` |
| III | `courseIII:spin-six-and-the-framing-comparison:eq:4.7` | `395` |
| III | `courseIII:spin-six-and-the-framing-comparison:eq:5.1` | `396` |
| III | `courseIII:spin-six-and-the-framing-comparison:eq:5.2` | `397` |
| III | `courseIII:spin-six-and-the-framing-comparison:eq:5.3` | `398` |
| III | `courseIII:spin-six-and-the-framing-comparison:eq:5.4` | `399` |
| III | `courseIII:spin-six-and-the-framing-comparison:eq:6.1` | `400` |
| III | `courseIII:spin-six-and-the-framing-comparison:eq:6.2` | `401` |
| III | `courseIII:spin-six-and-the-framing-comparison:eq:6.3` | `402` |
| III | `courseIII:spin-six-and-the-framing-comparison:eq:6.4` | `403` |
| III | `courseIII:spin-six-and-the-framing-comparison:eq:7.1` | `404` |
| III | `courseIII:spin-six-and-the-framing-comparison:eq:7.2` | `405` |
| III | `courseIII:spin-six-and-the-framing-comparison:eq:7.3` | `406` |
| III | `courseIII:spin-six-and-the-framing-comparison:eq:7.4` | `407` |
| III | `courseIII:spin-six-and-the-framing-comparison:eq:7.5` | `408` |
| III | `courseIII:spin-six-and-the-framing-comparison:exercise-7.1` | `H.7.1` |
| III | `courseIII:spin-six-and-the-framing-comparison:exercise-7.2` | `H.7.2` |
| III | `courseIII:spin-six-and-the-framing-comparison:framing-euler-comparison` | `H.4` |
| III | `courseIII:spin-six-and-the-framing-comparison:framing-exercises` | `H.7` |
| III | `courseIII:spin-six-and-the-framing-comparison:framing-family-index` | `H.1` |
| III | `courseIII:spin-six-and-the-framing-comparison:framing-loop-periodicity` | `H.2` |
| III | `courseIII:spin-six-and-the-framing-comparison:framing-original-sphere` | `H.6` |
| III | `courseIII:spin-six-and-the-framing-comparison:framing-so7` | `H.5` |
| III | `courseIII:spin-six-and-the-framing-comparison:framing-su4-so6` | `H.3` |
| III | `courseIII:spin-six-and-the-framing-comparison:section` | `H` |
| III | `courseIII:spin-six-and-the-framing-comparison:section-1` | `H.1` |
| III | `courseIII:spin-six-and-the-framing-comparison:section-2` | `H.2` |
| III | `courseIII:spin-six-and-the-framing-comparison:section-3` | `H.3` |
| III | `courseIII:spin-six-and-the-framing-comparison:section-4` | `H.4` |
| III | `courseIII:spin-six-and-the-framing-comparison:section-5` | `H.5` |
| III | `courseIII:spin-six-and-the-framing-comparison:section-6` | `H.6` |
| III | `courseIII:spin-six-and-the-framing-comparison:section-7` | `H.7` |
| III | `courseIII:spin-six-and-the-framing-comparison:spin-six-diagram` | `H.6` |
| III | `courseIII:spin6:1` | `H.1` |
| III | `courseIII:spin6:2` | `H.2` |
| III | `courseIII:spin6:3` | `H.3` |
| III | `courseIII:spin6:4` | `H.4` |
| III | `courseIII:spin6:5` | `H.5` |
| III | `courseIII:spin6:6` | `H.6` |
| III | `courseIII:spin6:7.1` | `H.7.1` |
| III | `courseIII:spin6:7.2` | `H.7.2` |
| III | `courseIII:the-actual-mod-two-adams-resolution-and-cooperation-maps:cooperation-actual-coalgebra` | `Y.2` |
| III | `courseIII:the-actual-mod-two-adams-resolution-and-cooperation-maps:cooperation-chain-comparison` | `Y.5` |
| III | `courseIII:the-actual-mod-two-adams-resolution-and-cooperation-maps:cooperation-degree-range` | `Y.7` |
| III | `courseIII:the-actual-mod-two-adams-resolution-and-cooperation-maps:cooperation-full-contraction` | `Y.4` |
| III | `courseIII:the-actual-mod-two-adams-resolution-and-cooperation-maps:cooperation-original-diagonal` | `Y.6` |
| III | `courseIII:the-actual-mod-two-adams-resolution-and-cooperation-maps:cooperation-original-factors` | `Y.1` |
| III | `courseIII:the-actual-mod-two-adams-resolution-and-cooperation-maps:cooperation-original-resolution` | `Y.3` |
| III | `courseIII:the-actual-mod-two-adams-resolution-and-cooperation-maps:cooperation-scope` | `Y.9` |
| III | `courseIII:the-actual-mod-two-adams-resolution-and-cooperation-maps:cooperation-worked-exercises` | `Y.8` |
| III | `courseIII:the-actual-mod-two-adams-resolution-and-cooperation-maps:eq:1.1` | `1350` |
| III | `courseIII:the-actual-mod-two-adams-resolution-and-cooperation-maps:eq:1.2` | `1351` |
| III | `courseIII:the-actual-mod-two-adams-resolution-and-cooperation-maps:eq:1.3` | `1352` |
| III | `courseIII:the-actual-mod-two-adams-resolution-and-cooperation-maps:eq:1.4` | `1353` |
| III | `courseIII:the-actual-mod-two-adams-resolution-and-cooperation-maps:eq:1.5` | `1354` |
| III | `courseIII:the-actual-mod-two-adams-resolution-and-cooperation-maps:eq:1.6` | `1355` |
| III | `courseIII:the-actual-mod-two-adams-resolution-and-cooperation-maps:eq:1.7` | `1356` |
| III | `courseIII:the-actual-mod-two-adams-resolution-and-cooperation-maps:eq:2.1` | `1357` |
| III | `courseIII:the-actual-mod-two-adams-resolution-and-cooperation-maps:eq:2.2` | `1358` |
| III | `courseIII:the-actual-mod-two-adams-resolution-and-cooperation-maps:eq:2.3` | `1359` |
| III | `courseIII:the-actual-mod-two-adams-resolution-and-cooperation-maps:eq:2.4` | `1360` |
| III | `courseIII:the-actual-mod-two-adams-resolution-and-cooperation-maps:eq:2.5` | `1361` |
| III | `courseIII:the-actual-mod-two-adams-resolution-and-cooperation-maps:eq:2.6` | `1362` |
| III | `courseIII:the-actual-mod-two-adams-resolution-and-cooperation-maps:eq:2.7` | `1363` |
| III | `courseIII:the-actual-mod-two-adams-resolution-and-cooperation-maps:eq:3.1` | `1364` |
| III | `courseIII:the-actual-mod-two-adams-resolution-and-cooperation-maps:eq:3.10` | `1373` |
| III | `courseIII:the-actual-mod-two-adams-resolution-and-cooperation-maps:eq:3.11` | `1374` |
| III | `courseIII:the-actual-mod-two-adams-resolution-and-cooperation-maps:eq:3.12` | `1375` |
| III | `courseIII:the-actual-mod-two-adams-resolution-and-cooperation-maps:eq:3.2` | `1365` |
| III | `courseIII:the-actual-mod-two-adams-resolution-and-cooperation-maps:eq:3.3` | `1366` |
| III | `courseIII:the-actual-mod-two-adams-resolution-and-cooperation-maps:eq:3.4` | `1367` |
| III | `courseIII:the-actual-mod-two-adams-resolution-and-cooperation-maps:eq:3.5` | `1368` |
| III | `courseIII:the-actual-mod-two-adams-resolution-and-cooperation-maps:eq:3.6` | `1369` |
| III | `courseIII:the-actual-mod-two-adams-resolution-and-cooperation-maps:eq:3.7` | `1370` |
| III | `courseIII:the-actual-mod-two-adams-resolution-and-cooperation-maps:eq:3.8` | `1371` |
| III | `courseIII:the-actual-mod-two-adams-resolution-and-cooperation-maps:eq:3.9` | `1372` |
| III | `courseIII:the-actual-mod-two-adams-resolution-and-cooperation-maps:eq:4.1` | `1376` |
| III | `courseIII:the-actual-mod-two-adams-resolution-and-cooperation-maps:eq:4.2` | `1377` |
| III | `courseIII:the-actual-mod-two-adams-resolution-and-cooperation-maps:eq:4.3` | `1378` |
| III | `courseIII:the-actual-mod-two-adams-resolution-and-cooperation-maps:eq:4.4` | `1379` |
| III | `courseIII:the-actual-mod-two-adams-resolution-and-cooperation-maps:eq:4.5` | `1380` |
| III | `courseIII:the-actual-mod-two-adams-resolution-and-cooperation-maps:eq:4.6` | `1381` |
| III | `courseIII:the-actual-mod-two-adams-resolution-and-cooperation-maps:eq:4.7` | `1382` |
| III | `courseIII:the-actual-mod-two-adams-resolution-and-cooperation-maps:eq:4.8` | `1383` |
| III | `courseIII:the-actual-mod-two-adams-resolution-and-cooperation-maps:eq:4.9` | `1384` |
| III | `courseIII:the-actual-mod-two-adams-resolution-and-cooperation-maps:eq:5.1` | `1385` |
| III | `courseIII:the-actual-mod-two-adams-resolution-and-cooperation-maps:eq:5.2` | `1386` |
| III | `courseIII:the-actual-mod-two-adams-resolution-and-cooperation-maps:eq:5.3` | `1387` |
| III | `courseIII:the-actual-mod-two-adams-resolution-and-cooperation-maps:eq:5.4` | `1388` |
| III | `courseIII:the-actual-mod-two-adams-resolution-and-cooperation-maps:eq:5.5` | `1389` |
| III | `courseIII:the-actual-mod-two-adams-resolution-and-cooperation-maps:eq:5.6` | `1390` |
| III | `courseIII:the-actual-mod-two-adams-resolution-and-cooperation-maps:eq:5.7` | `1391` |
| III | `courseIII:the-actual-mod-two-adams-resolution-and-cooperation-maps:eq:5.8` | `1392` |
| III | `courseIII:the-actual-mod-two-adams-resolution-and-cooperation-maps:eq:6.1` | `1393` |
| III | `courseIII:the-actual-mod-two-adams-resolution-and-cooperation-maps:eq:6.2` | `1394` |
| III | `courseIII:the-actual-mod-two-adams-resolution-and-cooperation-maps:eq:6.3` | `1395` |
| III | `courseIII:the-actual-mod-two-adams-resolution-and-cooperation-maps:eq:6.4` | `1396` |
| III | `courseIII:the-actual-mod-two-adams-resolution-and-cooperation-maps:eq:6.5` | `1397` |
| III | `courseIII:the-actual-mod-two-adams-resolution-and-cooperation-maps:eq:6.6` | `1398` |
| III | `courseIII:the-actual-mod-two-adams-resolution-and-cooperation-maps:eq:6.7` | `1399` |
| III | `courseIII:the-actual-mod-two-adams-resolution-and-cooperation-maps:eq:6.8` | `1400` |
| III | `courseIII:the-actual-mod-two-adams-resolution-and-cooperation-maps:eq:7.1` | `1401` |
| III | `courseIII:the-actual-mod-two-adams-resolution-and-cooperation-maps:eq:7.2` | `1402` |
| III | `courseIII:the-actual-mod-two-adams-resolution-and-cooperation-maps:eq:7.3` | `1403` |
| III | `courseIII:the-actual-mod-two-adams-resolution-and-cooperation-maps:eq:7.4` | `1404` |
| III | `courseIII:the-actual-mod-two-adams-resolution-and-cooperation-maps:eq:8.1` | `1405` |
| III | `courseIII:the-actual-mod-two-adams-resolution-and-cooperation-maps:eq:8.2` | `1406` |
| III | `courseIII:the-actual-mod-two-adams-resolution-and-cooperation-maps:eq:8.3` | `1407` |
| III | `courseIII:the-actual-mod-two-adams-resolution-and-cooperation-maps:eq:8.4` | `1408` |
| III | `courseIII:the-actual-mod-two-adams-resolution-and-cooperation-maps:eq:8.5` | `1409` |
| III | `courseIII:the-actual-mod-two-adams-resolution-and-cooperation-maps:eq:8.6` | `1410` |
| III | `courseIII:the-actual-mod-two-adams-resolution-and-cooperation-maps:eq:8.7` | `1411` |
| III | `courseIII:the-actual-mod-two-adams-resolution-and-cooperation-maps:exercise-8.1` | `Y.8.1` |
| III | `courseIII:the-actual-mod-two-adams-resolution-and-cooperation-maps:exercise-8.2` | `Y.8.2` |
| III | `courseIII:the-actual-mod-two-adams-resolution-and-cooperation-maps:section` | `Y` |
| III | `courseIII:the-actual-mod-two-adams-resolution-and-cooperation-maps:section-1` | `Y.1` |
| III | `courseIII:the-actual-mod-two-adams-resolution-and-cooperation-maps:section-2` | `Y.2` |
| III | `courseIII:the-actual-mod-two-adams-resolution-and-cooperation-maps:section-3` | `Y.3` |
| III | `courseIII:the-actual-mod-two-adams-resolution-and-cooperation-maps:section-4` | `Y.4` |
| III | `courseIII:the-actual-mod-two-adams-resolution-and-cooperation-maps:section-5` | `Y.5` |
| III | `courseIII:the-actual-mod-two-adams-resolution-and-cooperation-maps:section-6` | `Y.6` |
| III | `courseIII:the-actual-mod-two-adams-resolution-and-cooperation-maps:section-7` | `Y.7` |
| III | `courseIII:the-actual-mod-two-adams-resolution-and-cooperation-maps:section-8` | `Y.8` |
| III | `courseIII:the-actual-mod-two-adams-resolution-and-cooperation-maps:section-9` | `Y.9` |
| III | `courseIII:the-actual-mod-two-cooperation-comparison-through-degree-eight:actual-eight-bar-comparison` | `X.2` |
| III | `courseIII:the-actual-mod-two-cooperation-comparison-through-degree-eight:actual-eight-bijectivity` | `X.7` |
| III | `courseIII:the-actual-mod-two-cooperation-comparison-through-degree-eight:actual-eight-chain-models` | `X.1` |
| III | `courseIII:the-actual-mod-two-cooperation-comparison-through-degree-eight:actual-eight-exercises` | `X.9` |
| III | `courseIII:the-actual-mod-two-cooperation-comparison-through-degree-eight:actual-eight-exterior-bar` | `X.3` |
| III | `courseIII:the-actual-mod-two-cooperation-comparison-through-degree-eight:actual-eight-graded-dimensions` | `X.5` |
| III | `courseIII:the-actual-mod-two-cooperation-comparison-through-degree-eight:actual-eight-nonzero-powers` | `X.6` |
| III | `courseIII:the-actual-mod-two-cooperation-comparison-through-degree-eight:actual-eight-original-suspension` | `X.4` |
| III | `courseIII:the-actual-mod-two-cooperation-comparison-through-degree-eight:actual-eight-receiving-cobar` | `X.8` |
| III | `courseIII:the-actual-mod-two-cooperation-comparison-through-degree-eight:eq:0.1` | `1306` |
| III | `courseIII:the-actual-mod-two-cooperation-comparison-through-degree-eight:eq:1.1` | `1307` |
| III | `courseIII:the-actual-mod-two-cooperation-comparison-through-degree-eight:eq:1.2` | `1308` |
| III | `courseIII:the-actual-mod-two-cooperation-comparison-through-degree-eight:eq:1.3` | `1309` |
| III | `courseIII:the-actual-mod-two-cooperation-comparison-through-degree-eight:eq:2.1` | `1310` |
| III | `courseIII:the-actual-mod-two-cooperation-comparison-through-degree-eight:eq:2.2` | `1311` |
| III | `courseIII:the-actual-mod-two-cooperation-comparison-through-degree-eight:eq:2.3` | `1312` |
| III | `courseIII:the-actual-mod-two-cooperation-comparison-through-degree-eight:eq:2.4` | `1313` |
| III | `courseIII:the-actual-mod-two-cooperation-comparison-through-degree-eight:eq:2.5` | `1314` |
| III | `courseIII:the-actual-mod-two-cooperation-comparison-through-degree-eight:eq:2.6` | `1315` |
| III | `courseIII:the-actual-mod-two-cooperation-comparison-through-degree-eight:eq:2.7` | `1316` |
| III | `courseIII:the-actual-mod-two-cooperation-comparison-through-degree-eight:eq:2.8` | `1317` |
| III | `courseIII:the-actual-mod-two-cooperation-comparison-through-degree-eight:eq:2.9` | `1318` |
| III | `courseIII:the-actual-mod-two-cooperation-comparison-through-degree-eight:eq:3.1` | `1319` |
| III | `courseIII:the-actual-mod-two-cooperation-comparison-through-degree-eight:eq:3.2` | `1320` |
| III | `courseIII:the-actual-mod-two-cooperation-comparison-through-degree-eight:eq:3.3` | `1321` |
| III | `courseIII:the-actual-mod-two-cooperation-comparison-through-degree-eight:eq:3.4` | `1322` |
| III | `courseIII:the-actual-mod-two-cooperation-comparison-through-degree-eight:eq:4.1` | `1323` |
| III | `courseIII:the-actual-mod-two-cooperation-comparison-through-degree-eight:eq:4.2` | `1324` |
| III | `courseIII:the-actual-mod-two-cooperation-comparison-through-degree-eight:eq:4.3` | `1325` |
| III | `courseIII:the-actual-mod-two-cooperation-comparison-through-degree-eight:eq:4.4` | `1326` |
| III | `courseIII:the-actual-mod-two-cooperation-comparison-through-degree-eight:eq:4.5` | `1327` |
| III | `courseIII:the-actual-mod-two-cooperation-comparison-through-degree-eight:eq:4.6` | `1328` |
| III | `courseIII:the-actual-mod-two-cooperation-comparison-through-degree-eight:eq:5.1` | `1329` |
| III | `courseIII:the-actual-mod-two-cooperation-comparison-through-degree-eight:eq:5.2` | `1330` |
| III | `courseIII:the-actual-mod-two-cooperation-comparison-through-degree-eight:eq:5.3` | `1331` |
| III | `courseIII:the-actual-mod-two-cooperation-comparison-through-degree-eight:eq:6.1` | `1332` |
| III | `courseIII:the-actual-mod-two-cooperation-comparison-through-degree-eight:eq:6.2` | `1333` |
| III | `courseIII:the-actual-mod-two-cooperation-comparison-through-degree-eight:eq:6.3` | `1334` |
| III | `courseIII:the-actual-mod-two-cooperation-comparison-through-degree-eight:eq:6.4` | `1335` |
| III | `courseIII:the-actual-mod-two-cooperation-comparison-through-degree-eight:eq:6.5` | `1336` |
| III | `courseIII:the-actual-mod-two-cooperation-comparison-through-degree-eight:eq:7.1` | `1337` |
| III | `courseIII:the-actual-mod-two-cooperation-comparison-through-degree-eight:eq:7.2` | `1338` |
| III | `courseIII:the-actual-mod-two-cooperation-comparison-through-degree-eight:eq:7.3` | `1339` |
| III | `courseIII:the-actual-mod-two-cooperation-comparison-through-degree-eight:eq:8.1` | `1340` |
| III | `courseIII:the-actual-mod-two-cooperation-comparison-through-degree-eight:eq:8.2` | `1341` |
| III | `courseIII:the-actual-mod-two-cooperation-comparison-through-degree-eight:eq:8.3` | `1342` |
| III | `courseIII:the-actual-mod-two-cooperation-comparison-through-degree-eight:eq:9.1` | `1343` |
| III | `courseIII:the-actual-mod-two-cooperation-comparison-through-degree-eight:eq:9.2` | `1344` |
| III | `courseIII:the-actual-mod-two-cooperation-comparison-through-degree-eight:eq:9.3` | `1345` |
| III | `courseIII:the-actual-mod-two-cooperation-comparison-through-degree-eight:eq:9.4` | `1346` |
| III | `courseIII:the-actual-mod-two-cooperation-comparison-through-degree-eight:eq:9.5` | `1347` |
| III | `courseIII:the-actual-mod-two-cooperation-comparison-through-degree-eight:eq:9.6` | `1348` |
| III | `courseIII:the-actual-mod-two-cooperation-comparison-through-degree-eight:eq:9.7` | `1349` |
| III | `courseIII:the-actual-mod-two-cooperation-comparison-through-degree-eight:exercise-9.1` | `X.9.1` |
| III | `courseIII:the-actual-mod-two-cooperation-comparison-through-degree-eight:exercise-9.2` | `X.9.2` |
| III | `courseIII:the-actual-mod-two-cooperation-comparison-through-degree-eight:section` | `X` |
| III | `courseIII:the-actual-mod-two-cooperation-comparison-through-degree-eight:section-1` | `X.1` |
| III | `courseIII:the-actual-mod-two-cooperation-comparison-through-degree-eight:section-2` | `X.2` |
| III | `courseIII:the-actual-mod-two-cooperation-comparison-through-degree-eight:section-3` | `X.3` |
| III | `courseIII:the-actual-mod-two-cooperation-comparison-through-degree-eight:section-4` | `X.4` |
| III | `courseIII:the-actual-mod-two-cooperation-comparison-through-degree-eight:section-5` | `X.5` |
| III | `courseIII:the-actual-mod-two-cooperation-comparison-through-degree-eight:section-6` | `X.6` |
| III | `courseIII:the-actual-mod-two-cooperation-comparison-through-degree-eight:section-7` | `X.7` |
| III | `courseIII:the-actual-mod-two-cooperation-comparison-through-degree-eight:section-8` | `X.8` |
| III | `courseIII:the-actual-mod-two-cooperation-comparison-through-degree-eight:section-9` | `X.9` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:adams-actual-convergence` | `AC.11` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:adams-degree-five-cobar` | `AC.5` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:adams-finite-convergence` | `AC.4` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:adams-original-cocycles` | `AC.8` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:adams-original-spectrum` | `AC.9` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:adams-original-tower` | `AC.1` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:adams-source-corrections` | `AC.6` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:adams-stable-homology` | `AC.10` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:adams-worked-exercises` | `AC.7` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:eq:1.1` | `1568` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:eq:1.2` | `1569` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:eq:1.3` | `1570` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:eq:1.4` | `1571` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:eq:1.5` | `1572` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:eq:10.1` | `1618` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:eq:10.2` | `1619` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:eq:10.3` | `1620` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:eq:10.4` | `1621` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:eq:10.5` | `1622` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:eq:10.6` | `1623` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:eq:10.7` | `1624` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:eq:11.1` | `1625` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:eq:11.2` | `1626` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:eq:11.2a` | `1627` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:eq:11.3` | `1628` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:eq:11.4` | `1629` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:eq:11.5` | `1630` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:eq:11.6` | `1631` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:eq:11.7` | `1632` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:eq:11.7a` | `1633` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:eq:11.8` | `1634` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:eq:2.1` | `1573` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:eq:2.2` | `1574` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:eq:2.3` | `1575` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:eq:3.1` | `1576` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:eq:3.2` | `1577` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:eq:3.3` | `1578` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:eq:3.4` | `1579` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:eq:3.5` | `1580` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:eq:4.0` | `1581` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:eq:4.1` | `1582` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:eq:4.2` | `1583` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:eq:4.3` | `1584` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:eq:4.4` | `1585` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:eq:4.5` | `1586` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:eq:5.1` | `1587` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:eq:5.2` | `1588` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:eq:5.3` | `1589` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:eq:5.4` | `1590` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:eq:5.5` | `1591` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:eq:5.6` | `1592` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:eq:6.1` | `1593` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:eq:7.1` | `1594` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:eq:7.2` | `1595` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:eq:7.3` | `1596` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:eq:7.4` | `1597` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:eq:7.5` | `1598` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:eq:7.6` | `1599` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:eq:7.7` | `1600` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:eq:8.1` | `1601` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:eq:8.2` | `1602` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:eq:8.3` | `1603` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:eq:8.4` | `1604` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:eq:8.5` | `1605` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:eq:8.6` | `1606` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:eq:8.7` | `1607` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:eq:8.8` | `1608` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:eq:8.9` | `1609` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:eq:9.1` | `1610` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:eq:9.2` | `1611` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:eq:9.3` | `1612` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:eq:9.4` | `1613` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:eq:9.5` | `1614` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:eq:9.6` | `1615` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:eq:9.7` | `1616` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:eq:9.8` | `1617` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:exercise-7.1` | `AC.7.1` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:exercise-7.2` | `AC.7.2` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:section` | `AC` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:section-1` | `AC.1` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:section-10` | `AC.10` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:section-11` | `AC.11` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:section-2` | `AC.2` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:section-3` | `AC.3` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:section-4` | `AC.4` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:section-5` | `AC.5` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:section-6` | `AC.6` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:section-7` | `AC.7` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:section-8` | `AC.8` |
| III | `courseIII:the-adams-tower-and-exact-inverse-limits:section-9` | `AC.9` |
| III | `courseIII:the-degree-six-milnor-cobar-calculation:eq:1.1` | `1412` |
| III | `courseIII:the-degree-six-milnor-cobar-calculation:eq:1.2` | `1413` |
| III | `courseIII:the-degree-six-milnor-cobar-calculation:eq:1.3` | `1414` |
| III | `courseIII:the-degree-six-milnor-cobar-calculation:eq:1.4` | `1415` |
| III | `courseIII:the-degree-six-milnor-cobar-calculation:eq:1.5` | `1416` |
| III | `courseIII:the-degree-six-milnor-cobar-calculation:eq:1.6` | `1417` |
| III | `courseIII:the-degree-six-milnor-cobar-calculation:eq:1.7` | `1418` |
| III | `courseIII:the-degree-six-milnor-cobar-calculation:eq:1.8` | `1419` |
| III | `courseIII:the-degree-six-milnor-cobar-calculation:eq:2.1` | `1420` |
| III | `courseIII:the-degree-six-milnor-cobar-calculation:eq:2.2` | `1421` |
| III | `courseIII:the-degree-six-milnor-cobar-calculation:eq:2.3` | `1422` |
| III | `courseIII:the-degree-six-milnor-cobar-calculation:eq:2.4` | `1423` |
| III | `courseIII:the-degree-six-milnor-cobar-calculation:eq:2.5` | `1424` |
| III | `courseIII:the-degree-six-milnor-cobar-calculation:eq:2.6` | `1425` |
| III | `courseIII:the-degree-six-milnor-cobar-calculation:eq:2.7` | `1426` |
| III | `courseIII:the-degree-six-milnor-cobar-calculation:eq:2.8` | `1427` |
| III | `courseIII:the-degree-six-milnor-cobar-calculation:eq:3.1` | `1428` |
| III | `courseIII:the-degree-six-milnor-cobar-calculation:eq:3.2` | `1429` |
| III | `courseIII:the-degree-six-milnor-cobar-calculation:eq:3.3` | `1430` |
| III | `courseIII:the-degree-six-milnor-cobar-calculation:eq:3.4` | `1431` |
| III | `courseIII:the-degree-six-milnor-cobar-calculation:eq:3.5` | `1432` |
| III | `courseIII:the-degree-six-milnor-cobar-calculation:eq:3.6` | `1433` |
| III | `courseIII:the-degree-six-milnor-cobar-calculation:eq:3.7` | `1434` |
| III | `courseIII:the-degree-six-milnor-cobar-calculation:eq:3.8` | `1435` |
| III | `courseIII:the-degree-six-milnor-cobar-calculation:eq:3.9` | `1436` |
| III | `courseIII:the-degree-six-milnor-cobar-calculation:eq:4.1` | `1437` |
| III | `courseIII:the-degree-six-milnor-cobar-calculation:eq:4.10` | `1446` |
| III | `courseIII:the-degree-six-milnor-cobar-calculation:eq:4.11` | `1447` |
| III | `courseIII:the-degree-six-milnor-cobar-calculation:eq:4.2` | `1438` |
| III | `courseIII:the-degree-six-milnor-cobar-calculation:eq:4.3` | `1439` |
| III | `courseIII:the-degree-six-milnor-cobar-calculation:eq:4.4` | `1440` |
| III | `courseIII:the-degree-six-milnor-cobar-calculation:eq:4.5` | `1441` |
| III | `courseIII:the-degree-six-milnor-cobar-calculation:eq:4.6` | `1442` |
| III | `courseIII:the-degree-six-milnor-cobar-calculation:eq:4.7` | `1443` |
| III | `courseIII:the-degree-six-milnor-cobar-calculation:eq:4.8` | `1444` |
| III | `courseIII:the-degree-six-milnor-cobar-calculation:eq:4.9` | `1445` |
| III | `courseIII:the-degree-six-milnor-cobar-calculation:eq:5.1` | `1448` |
| III | `courseIII:the-degree-six-milnor-cobar-calculation:eq:5.2` | `1449` |
| III | `courseIII:the-degree-six-milnor-cobar-calculation:eq:5.3` | `1450` |
| III | `courseIII:the-degree-six-milnor-cobar-calculation:eq:5.4` | `1451` |
| III | `courseIII:the-degree-six-milnor-cobar-calculation:eq:6.1` | `1452` |
| III | `courseIII:the-degree-six-milnor-cobar-calculation:eq:6.2` | `1453` |
| III | `courseIII:the-degree-six-milnor-cobar-calculation:eq:6.3` | `1454` |
| III | `courseIII:the-degree-six-milnor-cobar-calculation:eq:6.4` | `1455` |
| III | `courseIII:the-degree-six-milnor-cobar-calculation:eq:6.5` | `1456` |
| III | `courseIII:the-degree-six-milnor-cobar-calculation:eq:6.6` | `1457` |
| III | `courseIII:the-degree-six-milnor-cobar-calculation:eq:6.7` | `1458` |
| III | `courseIII:the-degree-six-milnor-cobar-calculation:eq:6.8` | `1459` |
| III | `courseIII:the-degree-six-milnor-cobar-calculation:eq:6.9` | `1460` |
| III | `courseIII:the-degree-six-milnor-cobar-calculation:eq:7.1` | `1461` |
| III | `courseIII:the-degree-six-milnor-cobar-calculation:eq:7.2` | `1462` |
| III | `courseIII:the-degree-six-milnor-cobar-calculation:eq:7.3` | `1463` |
| III | `courseIII:the-degree-six-milnor-cobar-calculation:eq:7.4` | `1464` |
| III | `courseIII:the-degree-six-milnor-cobar-calculation:eq:7.5` | `1465` |
| III | `courseIII:the-degree-six-milnor-cobar-calculation:exercise-1` | `Z.7.1` |
| III | `courseIII:the-degree-six-milnor-cobar-calculation:exercise-2` | `Z.7.2` |
| III | `courseIII:the-degree-six-milnor-cobar-calculation:section` | `Z` |
| III | `courseIII:the-degree-six-milnor-cobar-calculation:section-1` | `Z.1` |
| III | `courseIII:the-degree-six-milnor-cobar-calculation:section-2` | `Z.2` |
| III | `courseIII:the-degree-six-milnor-cobar-calculation:section-3` | `Z.3` |
| III | `courseIII:the-degree-six-milnor-cobar-calculation:section-4` | `Z.4` |
| III | `courseIII:the-degree-six-milnor-cobar-calculation:section-5` | `Z.5` |
| III | `courseIII:the-degree-six-milnor-cobar-calculation:section-6` | `Z.6` |
| III | `courseIII:the-degree-six-milnor-cobar-calculation:section-7` | `Z.7` |
| III | `courseIII:the-degree-six-milnor-cobar-calculation:six-cobar-all-lengths` | `Z.3` |
| III | `courseIII:the-degree-six-milnor-cobar-calculation:six-cobar-exact-corrections` | `Z.4` |
| III | `courseIII:the-degree-six-milnor-cobar-calculation:six-cobar-exercises` | `Z.7` |
| III | `courseIII:the-degree-six-milnor-cobar-calculation:six-cobar-finite-filtration` | `Z.2` |
| III | `courseIII:the-degree-six-milnor-cobar-calculation:six-cobar-odd-primes` | `Z.6` |
| III | `courseIII:the-degree-six-milnor-cobar-calculation:six-cobar-original-complex` | `Z.1` |
| III | `courseIII:the-degree-six-milnor-cobar-calculation:six-cobar-source-use` | `Z` |
| III | `courseIII:the-degree-six-milnor-cobar-calculation:six-cobar-survival` | `Z.5` |
| III | `courseIII:the-degree-six-milnor-cobar-calculation:source-theorem-1.1` | `Z.1` |
| III | `courseIII:the-degree-six-milnor-cobar-calculation:source-theorem-6.1` | `Z.2` |
| III | `courseIII:the-exact-characteristic-two-coordinate-calculation:eq:1.1` | `1251` |
| III | `courseIII:the-exact-characteristic-two-coordinate-calculation:eq:1.2` | `1252` |
| III | `courseIII:the-exact-characteristic-two-coordinate-calculation:eq:1.3` | `1253` |
| III | `courseIII:the-exact-characteristic-two-coordinate-calculation:eq:1.4` | `1254` |
| III | `courseIII:the-exact-characteristic-two-coordinate-calculation:eq:1.5` | `1255` |
| III | `courseIII:the-exact-characteristic-two-coordinate-calculation:eq:1.6` | `1256` |
| III | `courseIII:the-exact-characteristic-two-coordinate-calculation:eq:2.1` | `1257` |
| III | `courseIII:the-exact-characteristic-two-coordinate-calculation:eq:2.2` | `1258` |
| III | `courseIII:the-exact-characteristic-two-coordinate-calculation:eq:2.3` | `1259` |
| III | `courseIII:the-exact-characteristic-two-coordinate-calculation:eq:2.4` | `1260` |
| III | `courseIII:the-exact-characteristic-two-coordinate-calculation:eq:2.5` | `1261` |
| III | `courseIII:the-exact-characteristic-two-coordinate-calculation:eq:2.6` | `1262` |
| III | `courseIII:the-exact-characteristic-two-coordinate-calculation:eq:2.7` | `1263` |
| III | `courseIII:the-exact-characteristic-two-coordinate-calculation:eq:3.1` | `1264` |
| III | `courseIII:the-exact-characteristic-two-coordinate-calculation:eq:3.2` | `1265` |
| III | `courseIII:the-exact-characteristic-two-coordinate-calculation:eq:3.3` | `1266` |
| III | `courseIII:the-exact-characteristic-two-coordinate-calculation:eq:4.1` | `1267` |
| III | `courseIII:the-exact-characteristic-two-coordinate-calculation:eq:4.2` | `1268` |
| III | `courseIII:the-exact-characteristic-two-coordinate-calculation:eq:4.3` | `1269` |
| III | `courseIII:the-exact-characteristic-two-coordinate-calculation:eq:4.4` | `1270` |
| III | `courseIII:the-exact-characteristic-two-coordinate-calculation:eq:4.5` | `1271` |
| III | `courseIII:the-exact-characteristic-two-coordinate-calculation:eq:4.6` | `1272` |
| III | `courseIII:the-exact-characteristic-two-coordinate-calculation:exercise-4.1` | `V.4.1` |
| III | `courseIII:the-exact-characteristic-two-coordinate-calculation:exercise-4.2` | `V.4.2` |
| III | `courseIII:the-exact-characteristic-two-coordinate-calculation:formal-two-additive-series` | `V.3` |
| III | `courseIII:the-exact-characteristic-two-coordinate-calculation:formal-two-cocycles` | `V.1` |
| III | `courseIII:the-exact-characteristic-two-coordinate-calculation:formal-two-inverse-exercises` | `V.4` |
| III | `courseIII:the-exact-characteristic-two-coordinate-calculation:formal-two-linearization` | `V.2` |
| III | `courseIII:the-exact-characteristic-two-coordinate-calculation:section` | `V` |
| III | `courseIII:the-exact-characteristic-two-coordinate-calculation:section-1` | `V.1` |
| III | `courseIII:the-exact-characteristic-two-coordinate-calculation:section-2` | `V.2` |
| III | `courseIII:the-exact-characteristic-two-coordinate-calculation:section-3` | `V.3` |
| III | `courseIII:the-exact-characteristic-two-coordinate-calculation:section-4` | `V.4` |
| III | `courseIII:the-original-adams-tower-and-arithmetic-completion:arithmetic-adams-equivalence` | `AD.5` |
| III | `courseIII:the-original-adams-tower-and-arithmetic-completion:arithmetic-extension-length` | `AD.3` |
| III | `courseIII:the-original-adams-tower-and-arithmetic-completion:arithmetic-homotopy-groups` | `AD.7` |
| III | `courseIII:the-original-adams-tower-and-arithmetic-completion:arithmetic-moore-tower` | `AD.1` |
| III | `courseIII:the-original-adams-tower-and-arithmetic-completion:arithmetic-original-presentation` | `AD.6` |
| III | `courseIII:the-original-adams-tower-and-arithmetic-completion:arithmetic-source-comparison` | `AD.9` |
| III | `courseIII:the-original-adams-tower-and-arithmetic-completion:arithmetic-universal-map` | `AD.2` |
| III | `courseIII:the-original-adams-tower-and-arithmetic-completion:arithmetic-vanishing-transitions` | `AD.4` |
| III | `courseIII:the-original-adams-tower-and-arithmetic-completion:arithmetic-worked-examples` | `AD.8` |
| III | `courseIII:the-original-adams-tower-and-arithmetic-completion:eq:1.1` | `1635` |
| III | `courseIII:the-original-adams-tower-and-arithmetic-completion:eq:1.2` | `1636` |
| III | `courseIII:the-original-adams-tower-and-arithmetic-completion:eq:1.3` | `1637` |
| III | `courseIII:the-original-adams-tower-and-arithmetic-completion:eq:1.4` | `1638` |
| III | `courseIII:the-original-adams-tower-and-arithmetic-completion:eq:1.5` | `1639` |
| III | `courseIII:the-original-adams-tower-and-arithmetic-completion:eq:1.6` | `1640` |
| III | `courseIII:the-original-adams-tower-and-arithmetic-completion:eq:1.7` | `1641` |
| III | `courseIII:the-original-adams-tower-and-arithmetic-completion:eq:1.8` | `1642` |
| III | `courseIII:the-original-adams-tower-and-arithmetic-completion:eq:2.1` | `1643` |
| III | `courseIII:the-original-adams-tower-and-arithmetic-completion:eq:2.2` | `1644` |
| III | `courseIII:the-original-adams-tower-and-arithmetic-completion:eq:2.3` | `1645` |
| III | `courseIII:the-original-adams-tower-and-arithmetic-completion:eq:2.4` | `1646` |
| III | `courseIII:the-original-adams-tower-and-arithmetic-completion:eq:2.5` | `1647` |
| III | `courseIII:the-original-adams-tower-and-arithmetic-completion:eq:2.6` | `1648` |
| III | `courseIII:the-original-adams-tower-and-arithmetic-completion:eq:2.7` | `1649` |
| III | `courseIII:the-original-adams-tower-and-arithmetic-completion:eq:3.1` | `1650` |
| III | `courseIII:the-original-adams-tower-and-arithmetic-completion:eq:3.2` | `1651` |
| III | `courseIII:the-original-adams-tower-and-arithmetic-completion:eq:3.3` | `1652` |
| III | `courseIII:the-original-adams-tower-and-arithmetic-completion:eq:3.4` | `1653` |
| III | `courseIII:the-original-adams-tower-and-arithmetic-completion:eq:3.5` | `1654` |
| III | `courseIII:the-original-adams-tower-and-arithmetic-completion:eq:3.6` | `1655` |
| III | `courseIII:the-original-adams-tower-and-arithmetic-completion:eq:3.7` | `1656` |
| III | `courseIII:the-original-adams-tower-and-arithmetic-completion:eq:3.8` | `1657` |
| III | `courseIII:the-original-adams-tower-and-arithmetic-completion:eq:4.1` | `1658` |
| III | `courseIII:the-original-adams-tower-and-arithmetic-completion:eq:4.2` | `1659` |
| III | `courseIII:the-original-adams-tower-and-arithmetic-completion:eq:4.3` | `1660` |
| III | `courseIII:the-original-adams-tower-and-arithmetic-completion:eq:4.4` | `1661` |
| III | `courseIII:the-original-adams-tower-and-arithmetic-completion:eq:4.5` | `1662` |
| III | `courseIII:the-original-adams-tower-and-arithmetic-completion:eq:4.6` | `1663` |
| III | `courseIII:the-original-adams-tower-and-arithmetic-completion:eq:4.7` | `1664` |
| III | `courseIII:the-original-adams-tower-and-arithmetic-completion:eq:4.8` | `1665` |
| III | `courseIII:the-original-adams-tower-and-arithmetic-completion:eq:4.9` | `1666` |
| III | `courseIII:the-original-adams-tower-and-arithmetic-completion:eq:5.1` | `1667` |
| III | `courseIII:the-original-adams-tower-and-arithmetic-completion:eq:5.2` | `1668` |
| III | `courseIII:the-original-adams-tower-and-arithmetic-completion:eq:5.3` | `1669` |
| III | `courseIII:the-original-adams-tower-and-arithmetic-completion:eq:5.4` | `1670` |
| III | `courseIII:the-original-adams-tower-and-arithmetic-completion:eq:5.5` | `1671` |
| III | `courseIII:the-original-adams-tower-and-arithmetic-completion:eq:5.6` | `1672` |
| III | `courseIII:the-original-adams-tower-and-arithmetic-completion:eq:5.7` | `1673` |
| III | `courseIII:the-original-adams-tower-and-arithmetic-completion:eq:5.8` | `1674` |
| III | `courseIII:the-original-adams-tower-and-arithmetic-completion:eq:6.1` | `1675` |
| III | `courseIII:the-original-adams-tower-and-arithmetic-completion:eq:6.2` | `1676` |
| III | `courseIII:the-original-adams-tower-and-arithmetic-completion:eq:6.3` | `1677` |
| III | `courseIII:the-original-adams-tower-and-arithmetic-completion:eq:6.4` | `1678` |
| III | `courseIII:the-original-adams-tower-and-arithmetic-completion:eq:6.5` | `1679` |
| III | `courseIII:the-original-adams-tower-and-arithmetic-completion:eq:6.6` | `1680` |
| III | `courseIII:the-original-adams-tower-and-arithmetic-completion:eq:6.7` | `1681` |
| III | `courseIII:the-original-adams-tower-and-arithmetic-completion:eq:6.8` | `1682` |
| III | `courseIII:the-original-adams-tower-and-arithmetic-completion:eq:7.1` | `1683` |
| III | `courseIII:the-original-adams-tower-and-arithmetic-completion:eq:7.10` | `1692` |
| III | `courseIII:the-original-adams-tower-and-arithmetic-completion:eq:7.11` | `1693` |
| III | `courseIII:the-original-adams-tower-and-arithmetic-completion:eq:7.12` | `1694` |
| III | `courseIII:the-original-adams-tower-and-arithmetic-completion:eq:7.13` | `1695` |
| III | `courseIII:the-original-adams-tower-and-arithmetic-completion:eq:7.2` | `1684` |
| III | `courseIII:the-original-adams-tower-and-arithmetic-completion:eq:7.3` | `1685` |
| III | `courseIII:the-original-adams-tower-and-arithmetic-completion:eq:7.4` | `1686` |
| III | `courseIII:the-original-adams-tower-and-arithmetic-completion:eq:7.5` | `1687` |
| III | `courseIII:the-original-adams-tower-and-arithmetic-completion:eq:7.6` | `1688` |
| III | `courseIII:the-original-adams-tower-and-arithmetic-completion:eq:7.7` | `1689` |
| III | `courseIII:the-original-adams-tower-and-arithmetic-completion:eq:7.8` | `1690` |
| III | `courseIII:the-original-adams-tower-and-arithmetic-completion:eq:7.9` | `1691` |
| III | `courseIII:the-original-adams-tower-and-arithmetic-completion:eq:8.1` | `1696` |
| III | `courseIII:the-original-adams-tower-and-arithmetic-completion:eq:8.2` | `1697` |
| III | `courseIII:the-original-adams-tower-and-arithmetic-completion:eq:8.3` | `1698` |
| III | `courseIII:the-original-adams-tower-and-arithmetic-completion:eq:8.4` | `1699` |
| III | `courseIII:the-original-adams-tower-and-arithmetic-completion:eq:8.5` | `1700` |
| III | `courseIII:the-original-adams-tower-and-arithmetic-completion:eq:8.6` | `1701` |
| III | `courseIII:the-original-adams-tower-and-arithmetic-completion:exercise-8.1` | `AD.8.1` |
| III | `courseIII:the-original-adams-tower-and-arithmetic-completion:exercise-8.2` | `AD.8.2` |
| III | `courseIII:the-original-adams-tower-and-arithmetic-completion:section` | `AD` |
| III | `courseIII:the-original-adams-tower-and-arithmetic-completion:section-1` | `AD.1` |
| III | `courseIII:the-original-adams-tower-and-arithmetic-completion:section-2` | `AD.2` |
| III | `courseIII:the-original-adams-tower-and-arithmetic-completion:section-3` | `AD.3` |
| III | `courseIII:the-original-adams-tower-and-arithmetic-completion:section-4` | `AD.4` |
| III | `courseIII:the-original-adams-tower-and-arithmetic-completion:section-5` | `AD.5` |
| III | `courseIII:the-original-adams-tower-and-arithmetic-completion:section-6` | `AD.6` |
| III | `courseIII:the-original-adams-tower-and-arithmetic-completion:section-7` | `AD.7` |
| III | `courseIII:the-original-adams-tower-and-arithmetic-completion:section-8` | `AD.8` |
| III | `courseIII:the-original-adams-tower-and-arithmetic-completion:section-9` | `AD.9` |
| III | `courseIII:the-original-integral-stable-group-and-its-completion-maps:eq:1.1` | `1702` |
| III | `courseIII:the-original-integral-stable-group-and-its-completion-maps:eq:1.2` | `1703` |
| III | `courseIII:the-original-integral-stable-group-and-its-completion-maps:eq:1.3` | `1704` |
| III | `courseIII:the-original-integral-stable-group-and-its-completion-maps:eq:1.4` | `1705` |
| III | `courseIII:the-original-integral-stable-group-and-its-completion-maps:eq:1.5` | `1706` |
| III | `courseIII:the-original-integral-stable-group-and-its-completion-maps:eq:1.6` | `1707` |
| III | `courseIII:the-original-integral-stable-group-and-its-completion-maps:eq:1.7` | `1708` |
| III | `courseIII:the-original-integral-stable-group-and-its-completion-maps:eq:2.1` | `1709` |
| III | `courseIII:the-original-integral-stable-group-and-its-completion-maps:eq:2.2` | `1710` |
| III | `courseIII:the-original-integral-stable-group-and-its-completion-maps:eq:2.3` | `1711` |
| III | `courseIII:the-original-integral-stable-group-and-its-completion-maps:eq:2.4` | `1712` |
| III | `courseIII:the-original-integral-stable-group-and-its-completion-maps:eq:2.5` | `1713` |
| III | `courseIII:the-original-integral-stable-group-and-its-completion-maps:eq:2.6` | `1714` |
| III | `courseIII:the-original-integral-stable-group-and-its-completion-maps:eq:3.1` | `1715` |
| III | `courseIII:the-original-integral-stable-group-and-its-completion-maps:eq:3.2` | `1716` |
| III | `courseIII:the-original-integral-stable-group-and-its-completion-maps:eq:3.3` | `1717` |
| III | `courseIII:the-original-integral-stable-group-and-its-completion-maps:eq:3.4` | `1718` |
| III | `courseIII:the-original-integral-stable-group-and-its-completion-maps:eq:3.5` | `1719` |
| III | `courseIII:the-original-integral-stable-group-and-its-completion-maps:eq:3.6` | `1720` |
| III | `courseIII:the-original-integral-stable-group-and-its-completion-maps:eq:3.7` | `1721` |
| III | `courseIII:the-original-integral-stable-group-and-its-completion-maps:eq:3.8` | `1722` |
| III | `courseIII:the-original-integral-stable-group-and-its-completion-maps:eq:3.9` | `1723` |
| III | `courseIII:the-original-integral-stable-group-and-its-completion-maps:eq:4.1` | `1724` |
| III | `courseIII:the-original-integral-stable-group-and-its-completion-maps:eq:4.2` | `1725` |
| III | `courseIII:the-original-integral-stable-group-and-its-completion-maps:eq:4.3` | `1726` |
| III | `courseIII:the-original-integral-stable-group-and-its-completion-maps:eq:4.4` | `1727` |
| III | `courseIII:the-original-integral-stable-group-and-its-completion-maps:eq:4.5` | `1728` |
| III | `courseIII:the-original-integral-stable-group-and-its-completion-maps:eq:4.6` | `1729` |
| III | `courseIII:the-original-integral-stable-group-and-its-completion-maps:eq:5.1` | `1730` |
| III | `courseIII:the-original-integral-stable-group-and-its-completion-maps:eq:5.10` | `1739` |
| III | `courseIII:the-original-integral-stable-group-and-its-completion-maps:eq:5.2` | `1731` |
| III | `courseIII:the-original-integral-stable-group-and-its-completion-maps:eq:5.3` | `1732` |
| III | `courseIII:the-original-integral-stable-group-and-its-completion-maps:eq:5.4` | `1733` |
| III | `courseIII:the-original-integral-stable-group-and-its-completion-maps:eq:5.5` | `1734` |
| III | `courseIII:the-original-integral-stable-group-and-its-completion-maps:eq:5.6` | `1735` |
| III | `courseIII:the-original-integral-stable-group-and-its-completion-maps:eq:5.7` | `1736` |
| III | `courseIII:the-original-integral-stable-group-and-its-completion-maps:eq:5.8` | `1737` |
| III | `courseIII:the-original-integral-stable-group-and-its-completion-maps:eq:5.9` | `1738` |
| III | `courseIII:the-original-integral-stable-group-and-its-completion-maps:eq:6.1` | `1740` |
| III | `courseIII:the-original-integral-stable-group-and-its-completion-maps:eq:6.10` | `1749` |
| III | `courseIII:the-original-integral-stable-group-and-its-completion-maps:eq:6.11` | `1750` |
| III | `courseIII:the-original-integral-stable-group-and-its-completion-maps:eq:6.2` | `1741` |
| III | `courseIII:the-original-integral-stable-group-and-its-completion-maps:eq:6.3` | `1742` |
| III | `courseIII:the-original-integral-stable-group-and-its-completion-maps:eq:6.4` | `1743` |
| III | `courseIII:the-original-integral-stable-group-and-its-completion-maps:eq:6.5` | `1744` |
| III | `courseIII:the-original-integral-stable-group-and-its-completion-maps:eq:6.6` | `1745` |
| III | `courseIII:the-original-integral-stable-group-and-its-completion-maps:eq:6.7` | `1746` |
| III | `courseIII:the-original-integral-stable-group-and-its-completion-maps:eq:6.8` | `1747` |
| III | `courseIII:the-original-integral-stable-group-and-its-completion-maps:eq:6.9` | `1748` |
| III | `courseIII:the-original-integral-stable-group-and-its-completion-maps:eq:7.1` | `1751` |
| III | `courseIII:the-original-integral-stable-group-and-its-completion-maps:eq:7.2` | `1752` |
| III | `courseIII:the-original-integral-stable-group-and-its-completion-maps:eq:7.3` | `1753` |
| III | `courseIII:the-original-integral-stable-group-and-its-completion-maps:eq:7.4` | `1754` |
| III | `courseIII:the-original-integral-stable-group-and-its-completion-maps:eq:8.1` | `1755` |
| III | `courseIII:the-original-integral-stable-group-and-its-completion-maps:eq:8.10` | `1764` |
| III | `courseIII:the-original-integral-stable-group-and-its-completion-maps:eq:8.11` | `1765` |
| III | `courseIII:the-original-integral-stable-group-and-its-completion-maps:eq:8.12` | `1766` |
| III | `courseIII:the-original-integral-stable-group-and-its-completion-maps:eq:8.2` | `1756` |
| III | `courseIII:the-original-integral-stable-group-and-its-completion-maps:eq:8.3` | `1757` |
| III | `courseIII:the-original-integral-stable-group-and-its-completion-maps:eq:8.4` | `1758` |
| III | `courseIII:the-original-integral-stable-group-and-its-completion-maps:eq:8.5` | `1759` |
| III | `courseIII:the-original-integral-stable-group-and-its-completion-maps:eq:8.6` | `1760` |
| III | `courseIII:the-original-integral-stable-group-and-its-completion-maps:eq:8.7` | `1761` |
| III | `courseIII:the-original-integral-stable-group-and-its-completion-maps:eq:8.8` | `1762` |
| III | `courseIII:the-original-integral-stable-group-and-its-completion-maps:eq:8.9` | `1763` |
| III | `courseIII:the-original-integral-stable-group-and-its-completion-maps:exercise-8.1` | `AE.8.1` |
| III | `courseIII:the-original-integral-stable-group-and-its-completion-maps:exercise-8.2` | `AE.8.2` |
| III | `courseIII:the-original-integral-stable-group-and-its-completion-maps:integral-coefficient-spaces` | `AE.2` |
| III | `courseIII:the-original-integral-stable-group-and-its-completion-maps:integral-completion-exercises` | `AE.8` |
| III | `courseIII:the-original-integral-stable-group-and-its-completion-maps:integral-degree-six-answer` | `AE.7` |
| III | `courseIII:the-original-integral-stable-group-and-its-completion-maps:integral-finite-chain-models` | `AE.1` |
| III | `courseIII:the-original-integral-stable-group-and-its-completion-maps:integral-finite-range` | `AE.4` |
| III | `courseIII:the-original-integral-stable-group-and-its-completion-maps:integral-original-completion` | `AE.6` |
| III | `courseIII:the-original-integral-stable-group-and-its-completion-maps:integral-original-suspension` | `AE.5` |
| III | `courseIII:the-original-integral-stable-group-and-its-completion-maps:integral-stable-sources` | `AE.9` |
| III | `courseIII:the-original-integral-stable-group-and-its-completion-maps:integral-unstable-finiteness` | `AE.3` |
| III | `courseIII:the-original-integral-stable-group-and-its-completion-maps:section` | `AE` |
| III | `courseIII:the-original-integral-stable-group-and-its-completion-maps:section-1` | `AE.1` |
| III | `courseIII:the-original-integral-stable-group-and-its-completion-maps:section-2` | `AE.2` |
| III | `courseIII:the-original-integral-stable-group-and-its-completion-maps:section-3` | `AE.3` |
| III | `courseIII:the-original-integral-stable-group-and-its-completion-maps:section-4` | `AE.4` |
| III | `courseIII:the-original-integral-stable-group-and-its-completion-maps:section-5` | `AE.5` |
| III | `courseIII:the-original-integral-stable-group-and-its-completion-maps:section-6` | `AE.6` |
| III | `courseIII:the-original-integral-stable-group-and-its-completion-maps:section-7` | `AE.7` |
| III | `courseIII:the-original-integral-stable-group-and-its-completion-maps:section-8` | `AE.8` |
| III | `courseIII:the-original-integral-stable-group-and-its-completion-maps:section-9` | `AE.9` |
| III | `courseIII:the-original-odd-prime-cooperations-and-degree-six-adams-calculation:eq:2.1` | `1531` |
| III | `courseIII:the-original-odd-prime-cooperations-and-degree-six-adams-calculation:eq:2.2` | `1532` |
| III | `courseIII:the-original-odd-prime-cooperations-and-degree-six-adams-calculation:eq:2.3` | `1533` |
| III | `courseIII:the-original-odd-prime-cooperations-and-degree-six-adams-calculation:eq:2.4` | `1534` |
| III | `courseIII:the-original-odd-prime-cooperations-and-degree-six-adams-calculation:eq:3.1` | `1535` |
| III | `courseIII:the-original-odd-prime-cooperations-and-degree-six-adams-calculation:eq:3.2` | `1536` |
| III | `courseIII:the-original-odd-prime-cooperations-and-degree-six-adams-calculation:eq:3.3` | `1537` |
| III | `courseIII:the-original-odd-prime-cooperations-and-degree-six-adams-calculation:eq:4.1` | `1538` |
| III | `courseIII:the-original-odd-prime-cooperations-and-degree-six-adams-calculation:eq:4.2` | `1539` |
| III | `courseIII:the-original-odd-prime-cooperations-and-degree-six-adams-calculation:eq:4.3` | `1540` |
| III | `courseIII:the-original-odd-prime-cooperations-and-degree-six-adams-calculation:eq:5.1` | `1541` |
| III | `courseIII:the-original-odd-prime-cooperations-and-degree-six-adams-calculation:eq:5.2` | `1542` |
| III | `courseIII:the-original-odd-prime-cooperations-and-degree-six-adams-calculation:eq:5.3` | `1543` |
| III | `courseIII:the-original-odd-prime-cooperations-and-degree-six-adams-calculation:eq:5.4` | `1544` |
| III | `courseIII:the-original-odd-prime-cooperations-and-degree-six-adams-calculation:eq:5.5` | `1545` |
| III | `courseIII:the-original-odd-prime-cooperations-and-degree-six-adams-calculation:eq:5.6` | `1546` |
| III | `courseIII:the-original-odd-prime-cooperations-and-degree-six-adams-calculation:eq:5.7` | `1547` |
| III | `courseIII:the-original-odd-prime-cooperations-and-degree-six-adams-calculation:eq:5.8` | `1548` |
| III | `courseIII:the-original-odd-prime-cooperations-and-degree-six-adams-calculation:eq:6.1` | `1549` |
| III | `courseIII:the-original-odd-prime-cooperations-and-degree-six-adams-calculation:eq:6.10` | `1558` |
| III | `courseIII:the-original-odd-prime-cooperations-and-degree-six-adams-calculation:eq:6.11` | `1559` |
| III | `courseIII:the-original-odd-prime-cooperations-and-degree-six-adams-calculation:eq:6.12` | `1560` |
| III | `courseIII:the-original-odd-prime-cooperations-and-degree-six-adams-calculation:eq:6.13` | `1561` |
| III | `courseIII:the-original-odd-prime-cooperations-and-degree-six-adams-calculation:eq:6.2` | `1550` |
| III | `courseIII:the-original-odd-prime-cooperations-and-degree-six-adams-calculation:eq:6.3` | `1551` |
| III | `courseIII:the-original-odd-prime-cooperations-and-degree-six-adams-calculation:eq:6.4` | `1552` |
| III | `courseIII:the-original-odd-prime-cooperations-and-degree-six-adams-calculation:eq:6.5` | `1553` |
| III | `courseIII:the-original-odd-prime-cooperations-and-degree-six-adams-calculation:eq:6.6` | `1554` |
| III | `courseIII:the-original-odd-prime-cooperations-and-degree-six-adams-calculation:eq:6.7` | `1555` |
| III | `courseIII:the-original-odd-prime-cooperations-and-degree-six-adams-calculation:eq:6.8` | `1556` |
| III | `courseIII:the-original-odd-prime-cooperations-and-degree-six-adams-calculation:eq:6.9` | `1557` |
| III | `courseIII:the-original-odd-prime-cooperations-and-degree-six-adams-calculation:eq:7.1` | `1562` |
| III | `courseIII:the-original-odd-prime-cooperations-and-degree-six-adams-calculation:eq:7.2` | `1563` |
| III | `courseIII:the-original-odd-prime-cooperations-and-degree-six-adams-calculation:eq:7.3` | `1564` |
| III | `courseIII:the-original-odd-prime-cooperations-and-degree-six-adams-calculation:eq:7.4` | `1565` |
| III | `courseIII:the-original-odd-prime-cooperations-and-degree-six-adams-calculation:eq:7.5` | `1566` |
| III | `courseIII:the-original-odd-prime-cooperations-and-degree-six-adams-calculation:eq:7.6` | `1567` |
| III | `courseIII:the-original-odd-prime-cooperations-and-degree-six-adams-calculation:exercise-7.1` | `AB.7.1` |
| III | `courseIII:the-original-odd-prime-cooperations-and-degree-six-adams-calculation:exercise-7.2` | `AB.7.2` |
| III | `courseIII:the-original-odd-prime-cooperations-and-degree-six-adams-calculation:odd-actual-adams` | `AB.6` |
| III | `courseIII:the-original-odd-prime-cooperations-and-degree-six-adams-calculation:odd-actual-cobar` | `AB.5` |
| III | `courseIII:the-original-odd-prime-cooperations-and-degree-six-adams-calculation:odd-exercises` | `AB.7` |
| III | `courseIII:the-original-odd-prime-cooperations-and-degree-six-adams-calculation:odd-full-induction` | `AB.3` |
| III | `courseIII:the-original-odd-prime-cooperations-and-degree-six-adams-calculation:odd-original-bar` | `AB.1` |
| III | `courseIII:the-original-odd-prime-cooperations-and-degree-six-adams-calculation:odd-original-chains` | `AB.2` |
| III | `courseIII:the-original-odd-prime-cooperations-and-degree-six-adams-calculation:odd-source-context` | `AB.8` |
| III | `courseIII:the-original-odd-prime-cooperations-and-degree-six-adams-calculation:odd-stable-cooperations` | `AB.4` |
| III | `courseIII:the-original-odd-prime-cooperations-and-degree-six-adams-calculation:section` | `AB` |
| III | `courseIII:the-original-odd-prime-cooperations-and-degree-six-adams-calculation:section-1` | `AB.1` |
| III | `courseIII:the-original-odd-prime-cooperations-and-degree-six-adams-calculation:section-2` | `AB.2` |
| III | `courseIII:the-original-odd-prime-cooperations-and-degree-six-adams-calculation:section-3` | `AB.3` |
| III | `courseIII:the-original-odd-prime-cooperations-and-degree-six-adams-calculation:section-4` | `AB.4` |
| III | `courseIII:the-original-odd-prime-cooperations-and-degree-six-adams-calculation:section-5` | `AB.5` |
| III | `courseIII:the-original-odd-prime-cooperations-and-degree-six-adams-calculation:section-6` | `AB.6` |
| III | `courseIII:the-original-odd-prime-cooperations-and-degree-six-adams-calculation:section-7` | `AB.7` |
| III | `courseIII:the-original-odd-prime-cooperations-and-degree-six-adams-calculation:section-8` | `AB.8` |
| III | `courseIII:the-original-projective-coordinate-and-actual-cooperations:eq:1.1` | `1273` |
| III | `courseIII:the-original-projective-coordinate-and-actual-cooperations:eq:1.2` | `1274` |
| III | `courseIII:the-original-projective-coordinate-and-actual-cooperations:eq:1.3` | `1275` |
| III | `courseIII:the-original-projective-coordinate-and-actual-cooperations:eq:1.4` | `1276` |
| III | `courseIII:the-original-projective-coordinate-and-actual-cooperations:eq:1.5` | `1277` |
| III | `courseIII:the-original-projective-coordinate-and-actual-cooperations:eq:2.1` | `1278` |
| III | `courseIII:the-original-projective-coordinate-and-actual-cooperations:eq:2.2` | `1279` |
| III | `courseIII:the-original-projective-coordinate-and-actual-cooperations:eq:2.3` | `1280` |
| III | `courseIII:the-original-projective-coordinate-and-actual-cooperations:eq:2.4` | `1281` |
| III | `courseIII:the-original-projective-coordinate-and-actual-cooperations:eq:2.5` | `1282` |
| III | `courseIII:the-original-projective-coordinate-and-actual-cooperations:eq:3.1` | `1283` |
| III | `courseIII:the-original-projective-coordinate-and-actual-cooperations:eq:3.2` | `1284` |
| III | `courseIII:the-original-projective-coordinate-and-actual-cooperations:eq:3.3` | `1285` |
| III | `courseIII:the-original-projective-coordinate-and-actual-cooperations:eq:3.4` | `1286` |
| III | `courseIII:the-original-projective-coordinate-and-actual-cooperations:eq:4.1` | `1287` |
| III | `courseIII:the-original-projective-coordinate-and-actual-cooperations:eq:4.2` | `1288` |
| III | `courseIII:the-original-projective-coordinate-and-actual-cooperations:eq:4.3` | `1289` |
| III | `courseIII:the-original-projective-coordinate-and-actual-cooperations:eq:4.4` | `1290` |
| III | `courseIII:the-original-projective-coordinate-and-actual-cooperations:eq:4.4a` | `1291` |
| III | `courseIII:the-original-projective-coordinate-and-actual-cooperations:eq:4.5` | `1292` |
| III | `courseIII:the-original-projective-coordinate-and-actual-cooperations:eq:5.1` | `1293` |
| III | `courseIII:the-original-projective-coordinate-and-actual-cooperations:eq:5.2` | `1294` |
| III | `courseIII:the-original-projective-coordinate-and-actual-cooperations:eq:5.3` | `1295` |
| III | `courseIII:the-original-projective-coordinate-and-actual-cooperations:eq:5.4` | `1296` |
| III | `courseIII:the-original-projective-coordinate-and-actual-cooperations:eq:5.5` | `1297` |
| III | `courseIII:the-original-projective-coordinate-and-actual-cooperations:eq:5.6` | `1298` |
| III | `courseIII:the-original-projective-coordinate-and-actual-cooperations:eq:6.1` | `1299` |
| III | `courseIII:the-original-projective-coordinate-and-actual-cooperations:eq:6.2` | `1300` |
| III | `courseIII:the-original-projective-coordinate-and-actual-cooperations:eq:6.3` | `1301` |
| III | `courseIII:the-original-projective-coordinate-and-actual-cooperations:eq:6.4` | `1302` |
| III | `courseIII:the-original-projective-coordinate-and-actual-cooperations:eq:6.5` | `1303` |
| III | `courseIII:the-original-projective-coordinate-and-actual-cooperations:eq:6.6` | `1304` |
| III | `courseIII:the-original-projective-coordinate-and-actual-cooperations:eq:6.7` | `1305` |
| III | `courseIII:the-original-projective-coordinate-and-actual-cooperations:exercise-6.1` | `W.6.1` |
| III | `courseIII:the-original-projective-coordinate-and-actual-cooperations:exercise-6.2` | `W.6.2` |
| III | `courseIII:the-original-projective-coordinate-and-actual-cooperations:projective-actual-coordinate` | `W.3` |
| III | `courseIII:the-original-projective-coordinate-and-actual-cooperations:projective-actual-coproduct` | `W.4` |
| III | `courseIII:the-original-projective-coordinate-and-actual-cooperations:projective-coefficient-limit` | `W.2` |
| III | `courseIII:the-original-projective-coordinate-and-actual-cooperations:projective-original-cochains` | `W.1` |
| III | `courseIII:the-original-projective-coordinate-and-actual-cooperations:projective-original-two` | `W.5` |
| III | `courseIII:the-original-projective-coordinate-and-actual-cooperations:projective-scope` | `W.7` |
| III | `courseIII:the-original-projective-coordinate-and-actual-cooperations:projective-worked-exercises` | `W.6` |
| III | `courseIII:the-original-projective-coordinate-and-actual-cooperations:section` | `W` |
| III | `courseIII:the-original-projective-coordinate-and-actual-cooperations:section-1` | `W.1` |
| III | `courseIII:the-original-projective-coordinate-and-actual-cooperations:section-2` | `W.2` |
| III | `courseIII:the-original-projective-coordinate-and-actual-cooperations:section-3` | `W.3` |
| III | `courseIII:the-original-projective-coordinate-and-actual-cooperations:section-4` | `W.4` |
| III | `courseIII:the-original-projective-coordinate-and-actual-cooperations:section-5` | `W.5` |
| III | `courseIII:the-original-projective-coordinate-and-actual-cooperations:section-6` | `W.6` |
| III | `courseIII:the-original-projective-coordinate-and-actual-cooperations:section-7` | `W.7` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:1.1` | `1767` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:1.10` | `1776` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:1.11` | `1777` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:1.12` | `1778` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:1.13` | `1779` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:1.14` | `1780` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:1.15` | `1781` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:1.2` | `1768` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:1.3` | `1769` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:1.4` | `1770` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:1.5` | `1771` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:1.6` | `1772` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:1.7` | `1773` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:1.8` | `1774` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:1.9` | `1775` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:10.1` | `1905` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:10.10` | `1914` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:10.11` | `1915` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:10.12` | `1916` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:10.13` | `1917` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:10.2` | `1906` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:10.3` | `1907` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:10.4` | `1908` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:10.5` | `1909` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:10.6` | `1910` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:10.7` | `1911` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:10.8` | `1912` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:10.9` | `1913` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:2.1` | `1782` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:2.2` | `1783` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:2.3` | `1784` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:2.4` | `1785` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:2.5` | `1786` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:2.6` | `1787` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:2.7` | `1788` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:2.8` | `1789` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:2.9` | `1790` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:3.1` | `1791` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:3.10` | `1800` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:3.11` | `1801` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:3.12` | `1802` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:3.13` | `1803` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:3.14` | `1804` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:3.15` | `1805` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:3.16` | `1806` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:3.17` | `1807` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:3.18` | `1808` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:3.2` | `1792` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:3.3` | `1793` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:3.4` | `1794` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:3.5` | `1795` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:3.6` | `1796` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:3.7` | `1797` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:3.8` | `1798` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:3.9` | `1799` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:4.1` | `1809` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:4.10` | `1818` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:4.11` | `1819` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:4.12` | `1820` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:4.13` | `1821` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:4.14` | `1822` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:4.15` | `1823` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:4.16` | `1824` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:4.17` | `1825` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:4.18` | `1826` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:4.2` | `1810` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:4.3` | `1811` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:4.4` | `1812` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:4.5` | `1813` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:4.6` | `1814` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:4.7` | `1815` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:4.8` | `1816` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:4.9` | `1817` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:5.1` | `1827` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:5.10` | `1836` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:5.11` | `1837` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:5.12` | `1838` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:5.13` | `1839` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:5.14` | `1840` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:5.15` | `1841` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:5.16` | `1842` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:5.17` | `1843` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:5.18` | `1844` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:5.19` | `1845` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:5.2` | `1828` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:5.20` | `1846` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:5.21` | `1847` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:5.22` | `1848` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:5.23` | `1849` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:5.24` | `1850` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:5.25` | `1851` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:5.26` | `1852` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:5.27` | `1853` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:5.28` | `1854` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:5.3` | `1829` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:5.4` | `1830` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:5.5` | `1831` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:5.6` | `1832` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:5.7` | `1833` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:5.8` | `1834` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:5.9` | `1835` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:6.1` | `1855` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:6.10` | `1864` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:6.11` | `1865` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:6.12` | `1866` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:6.13` | `1867` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:6.14` | `1868` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:6.15` | `1869` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:6.16` | `1870` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:6.17` | `1871` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:6.18` | `1872` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:6.19` | `1873` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:6.2` | `1856` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:6.20` | `1874` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:6.21` | `1875` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:6.22` | `1876` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:6.23` | `1877` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:6.24` | `1878` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:6.25` | `1879` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:6.3` | `1857` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:6.4` | `1858` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:6.5` | `1859` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:6.6` | `1860` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:6.7` | `1861` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:6.8` | `1862` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:6.9` | `1863` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:7.1` | `1880` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:7.2` | `1881` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:7.3` | `1882` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:7.4` | `1883` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:7.5` | `1884` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:7.6` | `1885` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:7.7` | `1886` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:8.1` | `1887` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:8.10` | `1896` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:8.11` | `1897` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:8.12` | `1898` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:8.13` | `1899` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:8.2` | `1888` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:8.3` | `1889` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:8.4` | `1890` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:8.5` | `1891` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:8.6` | `1892` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:8.7` | `1893` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:8.8` | `1894` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:8.9` | `1895` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:9.1` | `1900` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:9.2` | `1901` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:9.3` | `1902` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:9.4` | `1903` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:eq:9.5` | `1904` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:exercise-1` | `AF.10.1` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:exercise-2` | `AF.10.2` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:framed-six-bordism-invariance` | `AF.8` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:framed-six-embedded-obstruction` | `AF.2` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:framed-six-embedded-representatives` | `AF.7` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:framed-six-exercises` | `AF.10` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:framed-six-homotopy-defects` | `AF.5` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:framed-six-original-nullbordism` | `AF.9` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:framed-six-original-values` | `AF.3` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:framed-six-quadratic-algebra` | `AF.4` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:framed-six-quadratic-law` | `AF.6` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:framed-six-rank-three` | `AF.1` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:framed-six-sources` | `AF.11` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:section` | `AF` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:section-1` | `AF.1` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:section-10` | `AF.10` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:section-11` | `AF.11` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:section-2` | `AF.2` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:section-3` | `AF.3` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:section-3.1` | `AF.3.1` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:section-3.2` | `AF.3.2` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:section-3.3` | `AF.3.3` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:section-4` | `AF.4` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:section-4.1` | `AF.4.1` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:section-4.2` | `AF.4.2` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:section-5` | `AF.5` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:section-5.1` | `AF.5.1` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:section-5.2` | `AF.5.2` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:section-5.3` | `AF.5.3` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:section-5.4` | `AF.5.4` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:section-5.5` | `AF.5.5` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:section-5.6` | `AF.5.6` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:section-6` | `AF.6` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:section-6.1` | `AF.6.1` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:section-6.2` | `AF.6.2` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:section-6.3` | `AF.6.3` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:section-6.4` | `AF.6.4` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:section-7` | `AF.7` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:section-8` | `AF.8` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:section-8.1` | `AF.8.1` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:section-8.2` | `AF.8.2` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:section-8.3` | `AF.8.3` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:section-8.4` | `AF.8.4` |
| III | `courseIII:the-original-six-dimensional-framing-invariant:section-9` | `AF.9` |
| III | `courseIII:thom-euler-for-lesson11:CG-S6-CHAIN-LEMMA-5.1` | `C.1` |
| III | `courseIII:thom-euler-for-lesson11:CG-S6-CHAIN-PROPOSITION-6.1` | `C.3` |
| III | `courseIII:thom-euler-for-lesson11:CG-S6-CHAIN-PROPOSITION-8.1` | `C.5` |
| III | `courseIII:thom-euler-for-lesson11:CG-S6-CHAIN-PROPOSITION-8.2` | `C.6` |
| III | `courseIII:thom-euler-for-lesson11:CG-S6-CHAIN-THEOREM-5.2` | `C.2` |
| III | `courseIII:thom-euler-for-lesson11:CG-S6-CHAIN-THEOREM-7.1` | `C.4` |
| III | `courseIII:thom-euler-for-lesson11:section` | `C` |
| III | `courseIII:thom-euler-for-lesson11:section-6` | `C.1` |
| III | `courseIII:thom-euler-for-lesson11:section-7` | `C.2` |
| III | `courseIII:thom-euler-for-lesson11:section-8` | `C.3` |
| III | `courseIII:trajectory-lowering:1` | `L.1` |
| III | `courseIII:trajectory-lowering:2` | `L.2` |
| III | `courseIII:trajectory-lowering:3` | `L.3` |
| III | `courseIII:trajectory-lowering:4` | `L.4` |
| III | `courseIII:trajectory-lowering:5` | `L.5` |
| III | `courseIII:trajectory-lowering:6.1` | `L.6.1` |
| III | `courseIII:trajectory-lowering:6.2` | `L.6.2` |
| III | `courseIII:whitney-move-with-controlled-support:eq:1.1` | `882` |
| III | `courseIII:whitney-move-with-controlled-support:eq:1.10` | `891` |
| III | `courseIII:whitney-move-with-controlled-support:eq:1.11` | `892` |
| III | `courseIII:whitney-move-with-controlled-support:eq:1.2` | `883` |
| III | `courseIII:whitney-move-with-controlled-support:eq:1.3` | `884` |
| III | `courseIII:whitney-move-with-controlled-support:eq:1.4` | `885` |
| III | `courseIII:whitney-move-with-controlled-support:eq:1.5` | `886` |
| III | `courseIII:whitney-move-with-controlled-support:eq:1.6` | `887` |
| III | `courseIII:whitney-move-with-controlled-support:eq:1.7` | `888` |
| III | `courseIII:whitney-move-with-controlled-support:eq:1.8` | `889` |
| III | `courseIII:whitney-move-with-controlled-support:eq:1.9` | `890` |
| III | `courseIII:whitney-move-with-controlled-support:eq:2.1` | `893` |
| III | `courseIII:whitney-move-with-controlled-support:eq:2.2` | `894` |
| III | `courseIII:whitney-move-with-controlled-support:eq:2.3` | `895` |
| III | `courseIII:whitney-move-with-controlled-support:eq:2.4` | `896` |
| III | `courseIII:whitney-move-with-controlled-support:eq:3.1` | `897` |
| III | `courseIII:whitney-move-with-controlled-support:eq:3.10` | `906` |
| III | `courseIII:whitney-move-with-controlled-support:eq:3.11` | `907` |
| III | `courseIII:whitney-move-with-controlled-support:eq:3.2` | `898` |
| III | `courseIII:whitney-move-with-controlled-support:eq:3.3` | `899` |
| III | `courseIII:whitney-move-with-controlled-support:eq:3.4` | `900` |
| III | `courseIII:whitney-move-with-controlled-support:eq:3.5` | `901` |
| III | `courseIII:whitney-move-with-controlled-support:eq:3.6` | `902` |
| III | `courseIII:whitney-move-with-controlled-support:eq:3.7` | `903` |
| III | `courseIII:whitney-move-with-controlled-support:eq:3.8` | `904` |
| III | `courseIII:whitney-move-with-controlled-support:eq:3.9` | `905` |
| III | `courseIII:whitney-move-with-controlled-support:eq:4.1` | `908` |
| III | `courseIII:whitney-move-with-controlled-support:eq:4.10` | `917` |
| III | `courseIII:whitney-move-with-controlled-support:eq:4.11` | `918` |
| III | `courseIII:whitney-move-with-controlled-support:eq:4.12` | `919` |
| III | `courseIII:whitney-move-with-controlled-support:eq:4.13` | `920` |
| III | `courseIII:whitney-move-with-controlled-support:eq:4.14` | `921` |
| III | `courseIII:whitney-move-with-controlled-support:eq:4.15` | `922` |
| III | `courseIII:whitney-move-with-controlled-support:eq:4.16` | `923` |
| III | `courseIII:whitney-move-with-controlled-support:eq:4.17` | `924` |
| III | `courseIII:whitney-move-with-controlled-support:eq:4.18` | `925` |
| III | `courseIII:whitney-move-with-controlled-support:eq:4.2` | `909` |
| III | `courseIII:whitney-move-with-controlled-support:eq:4.3` | `910` |
| III | `courseIII:whitney-move-with-controlled-support:eq:4.4` | `911` |
| III | `courseIII:whitney-move-with-controlled-support:eq:4.5` | `912` |
| III | `courseIII:whitney-move-with-controlled-support:eq:4.6` | `913` |
| III | `courseIII:whitney-move-with-controlled-support:eq:4.7` | `914` |
| III | `courseIII:whitney-move-with-controlled-support:eq:4.8` | `915` |
| III | `courseIII:whitney-move-with-controlled-support:eq:4.9` | `916` |
| III | `courseIII:whitney-move-with-controlled-support:eq:5.1` | `926` |
| III | `courseIII:whitney-move-with-controlled-support:eq:5.10` | `935` |
| III | `courseIII:whitney-move-with-controlled-support:eq:5.11` | `936` |
| III | `courseIII:whitney-move-with-controlled-support:eq:5.12` | `937` |
| III | `courseIII:whitney-move-with-controlled-support:eq:5.13` | `938` |
| III | `courseIII:whitney-move-with-controlled-support:eq:5.14` | `939` |
| III | `courseIII:whitney-move-with-controlled-support:eq:5.15` | `940` |
| III | `courseIII:whitney-move-with-controlled-support:eq:5.16` | `941` |
| III | `courseIII:whitney-move-with-controlled-support:eq:5.17` | `942` |
| III | `courseIII:whitney-move-with-controlled-support:eq:5.2` | `927` |
| III | `courseIII:whitney-move-with-controlled-support:eq:5.3` | `928` |
| III | `courseIII:whitney-move-with-controlled-support:eq:5.4` | `929` |
| III | `courseIII:whitney-move-with-controlled-support:eq:5.5` | `930` |
| III | `courseIII:whitney-move-with-controlled-support:eq:5.6` | `931` |
| III | `courseIII:whitney-move-with-controlled-support:eq:5.7` | `932` |
| III | `courseIII:whitney-move-with-controlled-support:eq:5.8` | `933` |
| III | `courseIII:whitney-move-with-controlled-support:eq:5.9` | `934` |
| III | `courseIII:whitney-move-with-controlled-support:eq:6.1` | `943` |
| III | `courseIII:whitney-move-with-controlled-support:eq:6.2` | `944` |
| III | `courseIII:whitney-move-with-controlled-support:eq:6.3` | `945` |
| III | `courseIII:whitney-move-with-controlled-support:eq:6.4` | `946` |
| III | `courseIII:whitney-move-with-controlled-support:eq:6.5` | `947` |
| III | `courseIII:whitney-move-with-controlled-support:eq:6.6` | `948` |
| III | `courseIII:whitney-move-with-controlled-support:eq:6.7` | `949` |
| III | `courseIII:whitney-move-with-controlled-support:eq:6.8` | `950` |
| III | `courseIII:whitney-move-with-controlled-support:eq:6.9` | `951` |
| III | `courseIII:whitney-move-with-controlled-support:eq:7.1` | `952` |
| III | `courseIII:whitney-move-with-controlled-support:eq:7.10` | `961` |
| III | `courseIII:whitney-move-with-controlled-support:eq:7.2` | `953` |
| III | `courseIII:whitney-move-with-controlled-support:eq:7.3` | `954` |
| III | `courseIII:whitney-move-with-controlled-support:eq:7.4` | `955` |
| III | `courseIII:whitney-move-with-controlled-support:eq:7.5` | `956` |
| III | `courseIII:whitney-move-with-controlled-support:eq:7.6` | `957` |
| III | `courseIII:whitney-move-with-controlled-support:eq:7.7` | `958` |
| III | `courseIII:whitney-move-with-controlled-support:eq:7.8` | `959` |
| III | `courseIII:whitney-move-with-controlled-support:eq:7.9` | `960` |
| III | `courseIII:whitney-move-with-controlled-support:exercise-7.1` | `Q.7.1` |
| III | `courseIII:whitney-move-with-controlled-support:exercise-7.2` | `Q.7.2` |
| III | `courseIII:whitney-move-with-controlled-support:move-collar-extension` | `Q.3` |
| III | `courseIII:whitney-move-with-controlled-support:move-exercises` | `Q.7` |
| III | `courseIII:whitney-move-with-controlled-support:move-full-derivative` | `Q.2` |
| III | `courseIII:whitney-move-with-controlled-support:move-model-flow` | `Q.1` |
| III | `courseIII:whitney-move-with-controlled-support:move-original-disk` | `Q.4` |
| III | `courseIII:whitney-move-with-controlled-support:move-receiving-attachments` | `Q.6` |
| III | `courseIII:whitney-move-with-controlled-support:move-sheet-coordinates` | `Q.5` |
| III | `courseIII:whitney-move-with-controlled-support:move-sources` | `Q.8` |
| III | `courseIII:whitney-move-with-controlled-support:section` | `Q` |
| III | `courseIII:whitney-move-with-controlled-support:section-1` | `Q.1` |
| III | `courseIII:whitney-move-with-controlled-support:section-2` | `Q.2` |
| III | `courseIII:whitney-move-with-controlled-support:section-3` | `Q.3` |
| III | `courseIII:whitney-move-with-controlled-support:section-4` | `Q.4` |
| III | `courseIII:whitney-move-with-controlled-support:section-4.1` | `Q.4.1` |
| III | `courseIII:whitney-move-with-controlled-support:section-4.2` | `Q.4.2` |
| III | `courseIII:whitney-move-with-controlled-support:section-4.3` | `Q.4.3` |
| III | `courseIII:whitney-move-with-controlled-support:section-5` | `Q.5` |
| III | `courseIII:whitney-move-with-controlled-support:section-5.1` | `Q.5.1` |
| III | `courseIII:whitney-move-with-controlled-support:section-5.2` | `Q.5.2` |
| III | `courseIII:whitney-move-with-controlled-support:section-5.3` | `Q.5.3` |
| III | `courseIII:whitney-move-with-controlled-support:section-6` | `Q.6` |
| III | `courseIII:whitney-move-with-controlled-support:section-6.1` | `Q.6.1` |
| III | `courseIII:whitney-move-with-controlled-support:section-7` | `Q.7` |
| III | `courseIII:whitney-move-with-controlled-support:supported-move-diagram` | `Q.7.2` |
| III | `courseIII:whitney-moves-in-the-receiving-dimensions:eq:1.1` | `962` |
| III | `courseIII:whitney-moves-in-the-receiving-dimensions:eq:1.10` | `971` |
| III | `courseIII:whitney-moves-in-the-receiving-dimensions:eq:1.2` | `963` |
| III | `courseIII:whitney-moves-in-the-receiving-dimensions:eq:1.3` | `964` |
| III | `courseIII:whitney-moves-in-the-receiving-dimensions:eq:1.4` | `965` |
| III | `courseIII:whitney-moves-in-the-receiving-dimensions:eq:1.5` | `966` |
| III | `courseIII:whitney-moves-in-the-receiving-dimensions:eq:1.6` | `967` |
| III | `courseIII:whitney-moves-in-the-receiving-dimensions:eq:1.7` | `968` |
| III | `courseIII:whitney-moves-in-the-receiving-dimensions:eq:1.8` | `969` |
| III | `courseIII:whitney-moves-in-the-receiving-dimensions:eq:1.9` | `970` |
| III | `courseIII:whitney-moves-in-the-receiving-dimensions:eq:2.1` | `972` |
| III | `courseIII:whitney-moves-in-the-receiving-dimensions:eq:2.2` | `973` |
| III | `courseIII:whitney-moves-in-the-receiving-dimensions:eq:2.3` | `974` |
| III | `courseIII:whitney-moves-in-the-receiving-dimensions:eq:2.4` | `975` |
| III | `courseIII:whitney-moves-in-the-receiving-dimensions:eq:3.1` | `976` |
| III | `courseIII:whitney-moves-in-the-receiving-dimensions:eq:3.10` | `985` |
| III | `courseIII:whitney-moves-in-the-receiving-dimensions:eq:3.11` | `986` |
| III | `courseIII:whitney-moves-in-the-receiving-dimensions:eq:3.12` | `987` |
| III | `courseIII:whitney-moves-in-the-receiving-dimensions:eq:3.2` | `977` |
| III | `courseIII:whitney-moves-in-the-receiving-dimensions:eq:3.3` | `978` |
| III | `courseIII:whitney-moves-in-the-receiving-dimensions:eq:3.4` | `979` |
| III | `courseIII:whitney-moves-in-the-receiving-dimensions:eq:3.5` | `980` |
| III | `courseIII:whitney-moves-in-the-receiving-dimensions:eq:3.6` | `981` |
| III | `courseIII:whitney-moves-in-the-receiving-dimensions:eq:3.7` | `982` |
| III | `courseIII:whitney-moves-in-the-receiving-dimensions:eq:3.8` | `983` |
| III | `courseIII:whitney-moves-in-the-receiving-dimensions:eq:3.9` | `984` |
| III | `courseIII:whitney-moves-in-the-receiving-dimensions:eq:4.1` | `988` |
| III | `courseIII:whitney-moves-in-the-receiving-dimensions:eq:4.10` | `997` |
| III | `courseIII:whitney-moves-in-the-receiving-dimensions:eq:4.11` | `998` |
| III | `courseIII:whitney-moves-in-the-receiving-dimensions:eq:4.12` | `999` |
| III | `courseIII:whitney-moves-in-the-receiving-dimensions:eq:4.13` | `1000` |
| III | `courseIII:whitney-moves-in-the-receiving-dimensions:eq:4.14` | `1001` |
| III | `courseIII:whitney-moves-in-the-receiving-dimensions:eq:4.15` | `1002` |
| III | `courseIII:whitney-moves-in-the-receiving-dimensions:eq:4.16` | `1003` |
| III | `courseIII:whitney-moves-in-the-receiving-dimensions:eq:4.17` | `1004` |
| III | `courseIII:whitney-moves-in-the-receiving-dimensions:eq:4.18` | `1005` |
| III | `courseIII:whitney-moves-in-the-receiving-dimensions:eq:4.19` | `1006` |
| III | `courseIII:whitney-moves-in-the-receiving-dimensions:eq:4.2` | `989` |
| III | `courseIII:whitney-moves-in-the-receiving-dimensions:eq:4.20` | `1007` |
| III | `courseIII:whitney-moves-in-the-receiving-dimensions:eq:4.21` | `1008` |
| III | `courseIII:whitney-moves-in-the-receiving-dimensions:eq:4.22` | `1009` |
| III | `courseIII:whitney-moves-in-the-receiving-dimensions:eq:4.23` | `1010` |
| III | `courseIII:whitney-moves-in-the-receiving-dimensions:eq:4.24` | `1011` |
| III | `courseIII:whitney-moves-in-the-receiving-dimensions:eq:4.25` | `1012` |
| III | `courseIII:whitney-moves-in-the-receiving-dimensions:eq:4.26` | `1013` |
| III | `courseIII:whitney-moves-in-the-receiving-dimensions:eq:4.27` | `1014` |
| III | `courseIII:whitney-moves-in-the-receiving-dimensions:eq:4.28` | `1015` |
| III | `courseIII:whitney-moves-in-the-receiving-dimensions:eq:4.3` | `990` |
| III | `courseIII:whitney-moves-in-the-receiving-dimensions:eq:4.4` | `991` |
| III | `courseIII:whitney-moves-in-the-receiving-dimensions:eq:4.5` | `992` |
| III | `courseIII:whitney-moves-in-the-receiving-dimensions:eq:4.6` | `993` |
| III | `courseIII:whitney-moves-in-the-receiving-dimensions:eq:4.7` | `994` |
| III | `courseIII:whitney-moves-in-the-receiving-dimensions:eq:4.8` | `995` |
| III | `courseIII:whitney-moves-in-the-receiving-dimensions:eq:4.9` | `996` |
| III | `courseIII:whitney-moves-in-the-receiving-dimensions:eq:5.1` | `1016` |
| III | `courseIII:whitney-moves-in-the-receiving-dimensions:eq:5.2` | `1017` |
| III | `courseIII:whitney-moves-in-the-receiving-dimensions:eq:5.3` | `1018` |
| III | `courseIII:whitney-moves-in-the-receiving-dimensions:eq:5.4` | `1019` |
| III | `courseIII:whitney-moves-in-the-receiving-dimensions:eq:5.5` | `1020` |
| III | `courseIII:whitney-moves-in-the-receiving-dimensions:eq:5.6` | `1021` |
| III | `courseIII:whitney-moves-in-the-receiving-dimensions:eq:5.7` | `1022` |
| III | `courseIII:whitney-moves-in-the-receiving-dimensions:exercise-1` | `R.5.1` |
| III | `courseIII:whitney-moves-in-the-receiving-dimensions:exercise-2` | `R.5.2` |
| III | `courseIII:whitney-moves-in-the-receiving-dimensions:receiving-rank-four-frame` | `R.3` |
| III | `courseIII:whitney-moves-in-the-receiving-dimensions:receiving-whitney-exercises` | `R.5` |
| III | `courseIII:whitney-moves-in-the-receiving-dimensions:receiving-whitney-flow` | `R.4` |
| III | `courseIII:whitney-moves-in-the-receiving-dimensions:receiving-whitney-levels` | `R.1` |
| III | `courseIII:whitney-moves-in-the-receiving-dimensions:receiving-whitney-normal-blocks` | `R.2` |
| III | `courseIII:whitney-moves-in-the-receiving-dimensions:receiving-whitney-sources` | `R.6` |
| III | `courseIII:whitney-moves-in-the-receiving-dimensions:section` | `R` |
| III | `courseIII:whitney-moves-in-the-receiving-dimensions:section-1` | `R.1` |
| III | `courseIII:whitney-moves-in-the-receiving-dimensions:section-2` | `R.2` |
| III | `courseIII:whitney-moves-in-the-receiving-dimensions:section-3` | `R.3` |
| III | `courseIII:whitney-moves-in-the-receiving-dimensions:section-4` | `R.4` |
| III | `courseIII:whitney-moves-in-the-receiving-dimensions:section-4.1` | `R.4.1` |
| III | `courseIII:whitney-moves-in-the-receiving-dimensions:section-4.2` | `R.4.2` |
| III | `courseIII:whitney-moves-in-the-receiving-dimensions:section-4.3` | `R.4.3` |
| III | `courseIII:whitney-moves-in-the-receiving-dimensions:section-5` | `R.5` |
| III | `courseIII:whitney-moves-in-the-receiving-dimensions:section-6` | `R.6` |
| III | `courseIII:whitney-receiving:1` | `R.1` |
| III | `courseIII:whitney-receiving:2` | `R.2` |
| III | `courseIII:whitney-receiving:3` | `R.3` |
| III | `courseIII:whitney-receiving:4` | `R.4` |
| III | `courseIII:whitney-receiving:5.1` | `R.5.1` |
| III | `courseIII:whitney-receiving:5.2` | `R.5.2` |
| III | `courseIII:whitney-support:1` | `Q.1` |
| III | `courseIII:whitney-support:2` | `Q.2` |
| III | `courseIII:whitney-support:3` | `Q.3` |
| III | `courseIII:whitney-support:4` | `Q.4` |
| III | `courseIII:whitney-support:5` | `Q.5` |
| III | `courseIII:whitney-support:6` | `Q.6` |
| III | `courseIII:whitney-support:7.1` | `Q.7.1` |
| III | `courseIII:whitney-support:7.2` | `Q.7.2` |
| III | `courseIII:zero-top:1` | `N.1` |
| III | `courseIII:zero-top:2` | `N.2` |
| III | `courseIII:zero-top:3` | `N.3` |
| III | `courseIII:zero-top:4` | `N.4` |
| III | `courseIII:zero-top:5` | `N.5` |
| III | `courseIII:zero-top:6.1` | `N.6.1` |
| III | `courseIII:zero-top:6.2` | `N.6.2` |
| III | `fam:src:E.2.2` | `8.1` |
| III | `fam:src:E.2.3` | `8.2` |
| III | `famIII:eq:E10` | `{E10}` |
| III | `famIII:eq:E9` | `{E9}` |
| III | `maps:eq:B.1.1` | `{B.1.1}` |
| III | `maps:eq:B.1.2` | `{B.1.2}` |
| III | `maps:eq:B.1.3` | `{B.1.3}` |
| III | `maps:eq:B.2.1` | `{B.2.1}` |
| III | `maps:eq:B.3.1` | `{B.3.1}` |
| III | `maps:eq:B.3.2` | `{B.3.2}` |
| III | `maps:eq:B.3.3` | `{B.3.3}` |
| III | `maps:eq:B.3.4` | `{B.3.4}` |
| III | `maps:eq:B.3.5` | `{B.3.5}` |
| III | `maps:eq:B.4.1` | `{B.4.1}` |
| III | `maps:eq:B.4.2` | `{B.4.2}` |
| III | `maps:eq:B.4.3` | `{B.4.3}` |
| III | `maps:eq:B.5.1` | `{B.5.1}` |
| III | `maps:eq:B.5.10` | `{B.5.10}` |
| III | `maps:eq:B.5.11` | `{B.5.11}` |
| III | `maps:eq:B.5.12` | `{B.5.12}` |
| III | `maps:eq:B.5.13` | `{B.5.13}` |
| III | `maps:eq:B.5.14` | `{B.5.14}` |
| III | `maps:eq:B.5.15` | `{B.5.15}` |
| III | `maps:eq:B.5.16` | `{B.5.16}` |
| III | `maps:eq:B.5.17` | `{B.5.17}` |
| III | `maps:eq:B.5.18` | `{B.5.18}` |
| III | `maps:eq:B.5.2` | `{B.5.2}` |
| III | `maps:eq:B.5.3` | `{B.5.3}` |
| III | `maps:eq:B.5.4` | `{B.5.4}` |
| III | `maps:eq:B.5.5` | `{B.5.5}` |
| III | `maps:eq:B.5.6` | `{B.5.6}` |
| III | `maps:eq:B.5.7` | `{B.5.7}` |
| III | `maps:eq:B.5.8` | `{B.5.8}` |
| III | `maps:eq:B.5.9` | `{B.5.9}` |
| III | `maps:eq:B.6.1` | `{B.6.1}` |
| III | `maps:eq:B.6.10` | `{B.6.10}` |
| III | `maps:eq:B.6.11` | `{B.6.11}` |
| III | `maps:eq:B.6.12` | `{B.6.12}` |
| III | `maps:eq:B.6.13` | `{B.6.13}` |
| III | `maps:eq:B.6.14` | `{B.6.14}` |
| III | `maps:eq:B.6.15` | `{B.6.15}` |
| III | `maps:eq:B.6.16` | `{B.6.16}` |
| III | `maps:eq:B.6.17` | `{B.6.17}` |
| III | `maps:eq:B.6.18` | `{B.6.18}` |
| III | `maps:eq:B.6.19` | `{B.6.19}` |
| III | `maps:eq:B.6.2` | `{B.6.2}` |
| III | `maps:eq:B.6.20` | `{B.6.20}` |
| III | `maps:eq:B.6.21` | `{B.6.21}` |
| III | `maps:eq:B.6.22` | `{B.6.22}` |
| III | `maps:eq:B.6.23` | `{B.6.23}` |
| III | `maps:eq:B.6.24` | `{B.6.24}` |
| III | `maps:eq:B.6.25` | `{B.6.25}` |
| III | `maps:eq:B.6.26` | `{B.6.26}` |
| III | `maps:eq:B.6.27` | `{B.6.27}` |
| III | `maps:eq:B.6.28` | `{B.6.28}` |
| III | `maps:eq:B.6.29` | `{B.6.29}` |
| III | `maps:eq:B.6.3` | `{B.6.3}` |
| III | `maps:eq:B.6.30` | `{B.6.30}` |
| III | `maps:eq:B.6.31` | `{B.6.31}` |
| III | `maps:eq:B.6.32` | `{B.6.32}` |
| III | `maps:eq:B.6.33` | `{B.6.33}` |
| III | `maps:eq:B.6.34` | `{B.6.34}` |
| III | `maps:eq:B.6.35` | `{B.6.35}` |
| III | `maps:eq:B.6.36` | `{B.6.36}` |
| III | `maps:eq:B.6.37` | `{B.6.37}` |
| III | `maps:eq:B.6.38` | `{B.6.38}` |
| III | `maps:eq:B.6.39` | `{B.6.39}` |
| III | `maps:eq:B.6.4` | `{B.6.4}` |
| III | `maps:eq:B.6.40` | `{B.6.40}` |
| III | `maps:eq:B.6.41` | `{B.6.41}` |
| III | `maps:eq:B.6.42` | `{B.6.42}` |
| III | `maps:eq:B.6.43` | `{B.6.43}` |
| III | `maps:eq:B.6.44` | `{B.6.44}` |
| III | `maps:eq:B.6.5` | `{B.6.5}` |
| III | `maps:eq:B.6.6` | `{B.6.6}` |
| III | `maps:eq:B.6.7` | `{B.6.7}` |
| III | `maps:eq:B.6.8` | `{B.6.8}` |
| III | `maps:eq:B.6.9` | `{B.6.9}` |
| III | `maps:eq:B.C1` | `{B.C1}` |
| III | `maps:eq:B.C2` | `{B.C2}` |
| III | `maps:eq:B.C3` | `{B.C3}` |
| III | `maps:eq:B.C4` | `{B.C4}` |
| III | `maps:eq:B.P1` | `{B.P1}` |
| III | `maps:eq:B.P2` | `{B.P2}` |
| III | `maps:eq:B.P3` | `{B.P3}` |
| III | `maps:eq:B.P4` | `{B.P4}` |
| III | `maps:eq:B.Q1` | `{B.Q1}` |
| III | `maps:eq:B.Q2` | `{B.Q2}` |
| III | `maps:eq:B.Q3` | `{B.Q3}` |
| III | `maps:eq:B.Q4` | `{B.Q4}` |
| III | `maps:eq:B.Q5` | `{B.Q5}` |
| III | `maps:eq:B.Q6` | `{B.Q6}` |
| III | `maps:eq:B.Q7` | `{B.Q7}` |
| III | `maps:eq:B.Q8` | `{B.Q8}` |
| III | `maps:eq:B.Q9` | `{B.Q9}` |
| III | `maps:eq:B.T1` | `{B.T1}` |
| III | `maps:eq:C.1.1` | `{C.1.1}` |
| III | `maps:eq:C.1.2` | `{C.1.2}` |
| III | `maps:eq:C.1.3` | `{C.1.3}` |
| III | `maps:eq:C.1.4` | `{C.1.4}` |
| III | `maps:eq:D.AF1` | `{D.AF1}` |
| III | `maps:eq:D.AF2` | `{D.AF2}` |
| III | `maps:eq:D.AF3` | `{D.AF3}` |
| III | `maps:eq:D.AF4` | `{D.AF4}` |
| III | `maps:eq:D.AF5` | `{D.AF5}` |
| III | `maps:eq:D.AF6` | `{D.AF6}` |
| III | `maps:eq:D.AF7` | `{D.AF7}` |
| III | `maps:eq:D.AF8` | `{D.AF8}` |
| III | `maps:eq:D.AF9` | `{D.AF9}` |
| III | `maps:eq:D.BC1` | `{D.BC1}` |
| III | `maps:eq:D.BC10` | `{D.BC10}` |
| III | `maps:eq:D.BC11` | `{D.BC11}` |
| III | `maps:eq:D.BC12` | `{D.BC12}` |
| III | `maps:eq:D.BC13` | `{D.BC13}` |
| III | `maps:eq:D.BC14` | `{D.BC14}` |
| III | `maps:eq:D.BC15` | `{D.BC15}` |
| III | `maps:eq:D.BC2` | `{D.BC2}` |
| III | `maps:eq:D.BC3` | `{D.BC3}` |
| III | `maps:eq:D.BC4` | `{D.BC4}` |
| III | `maps:eq:D.BC5` | `{D.BC5}` |
| III | `maps:eq:D.BC6` | `{D.BC6}` |
| III | `maps:eq:D.BC7` | `{D.BC7}` |
| III | `maps:eq:D.BC8` | `{D.BC8}` |
| III | `maps:eq:D.BC9` | `{D.BC9}` |
| III | `maps:eq:D.C1` | `{D.C1}` |
| III | `maps:eq:D.C21` | `{D.C21}` |
| III | `maps:eq:D.C210` | `{D.C210}` |
| III | `maps:eq:D.C211` | `{D.C211}` |
| III | `maps:eq:D.C212` | `{D.C212}` |
| III | `maps:eq:D.C213` | `{D.C213}` |
| III | `maps:eq:D.C214` | `{D.C214}` |
| III | `maps:eq:D.C215` | `{D.C215}` |
| III | `maps:eq:D.C216` | `{D.C216}` |
| III | `maps:eq:D.C22` | `{D.C22}` |
| III | `maps:eq:D.C23` | `{D.C23}` |
| III | `maps:eq:D.C24` | `{D.C24}` |
| III | `maps:eq:D.C25` | `{D.C25}` |
| III | `maps:eq:D.C26` | `{D.C26}` |
| III | `maps:eq:D.C27` | `{D.C27}` |
| III | `maps:eq:D.C28` | `{D.C28}` |
| III | `maps:eq:D.C29` | `{D.C29}` |
| III | `maps:eq:D.CI1` | `{D.CI1}` |
| III | `maps:eq:D.F1` | `{D.F1}` |
| III | `maps:eq:D.F2` | `{D.F2}` |
| III | `maps:eq:D.FG1` | `{D.FG1}` |
| III | `maps:eq:D.FG2` | `{D.FG2}` |
| III | `maps:eq:D.FG3` | `{D.FG3}` |
| III | `maps:eq:D.FI1` | `{D.FI1}` |
| III | `maps:eq:D.FI2` | `{D.FI2}` |
| III | `maps:eq:D.FI3` | `{D.FI3}` |
| III | `maps:eq:D.FI4` | `{D.FI4}` |
| III | `maps:eq:D.FI5` | `{D.FI5}` |
| III | `maps:eq:D.GC1` | `{D.GC1}` |
| III | `maps:eq:D.GC10` | `{D.GC10}` |
| III | `maps:eq:D.GC11` | `{D.GC11}` |
| III | `maps:eq:D.GC12` | `{D.GC12}` |
| III | `maps:eq:D.GC13` | `{D.GC13}` |
| III | `maps:eq:D.GC14` | `{D.GC14}` |
| III | `maps:eq:D.GC2` | `{D.GC2}` |
| III | `maps:eq:D.GC3` | `{D.GC3}` |
| III | `maps:eq:D.GC4` | `{D.GC4}` |
| III | `maps:eq:D.GC5` | `{D.GC5}` |
| III | `maps:eq:D.GC6` | `{D.GC6}` |
| III | `maps:eq:D.GC7` | `{D.GC7}` |
| III | `maps:eq:D.GC8` | `{D.GC8}` |
| III | `maps:eq:D.GC9` | `{D.GC9}` |
| III | `maps:eq:D.GI1` | `{D.GI1}` |
| III | `maps:eq:D.GI10` | `{D.GI10}` |
| III | `maps:eq:D.GI11` | `{D.GI11}` |
| III | `maps:eq:D.GI2` | `{D.GI2}` |
| III | `maps:eq:D.GI3` | `{D.GI3}` |
| III | `maps:eq:D.GI4` | `{D.GI4}` |
| III | `maps:eq:D.GI5` | `{D.GI5}` |
| III | `maps:eq:D.GI6` | `{D.GI6}` |
| III | `maps:eq:D.GI7` | `{D.GI7}` |
| III | `maps:eq:D.GI8` | `{D.GI8}` |
| III | `maps:eq:D.GI9` | `{D.GI9}` |
| III | `maps:eq:D.HY1` | `{D.HY1}` |
| III | `maps:eq:D.HY2` | `{D.HY2}` |
| III | `maps:eq:D.HY3` | `{D.HY3}` |
| III | `maps:eq:D.HY4` | `{D.HY4}` |
| III | `maps:eq:D.HY5` | `{D.HY5}` |
| III | `maps:eq:D.HY6` | `{D.HY6}` |
| III | `maps:eq:D.HY7` | `{D.HY7}` |
| III | `maps:eq:D.I1` | `{D.I1}` |
| III | `maps:eq:D.I2` | `{D.I2}` |
| III | `maps:eq:D.I3` | `{D.I3}` |
| III | `maps:eq:D.I4` | `{D.I4}` |
| III | `maps:eq:D.IC1` | `{D.IC1}` |
| III | `maps:eq:D.IC2` | `{D.IC2}` |
| III | `maps:eq:D.IC3` | `{D.IC3}` |
| III | `maps:eq:D.IC4` | `{D.IC4}` |
| III | `maps:eq:D.IC5` | `{D.IC5}` |
| III | `maps:eq:D.IC6` | `{D.IC6}` |
| III | `maps:eq:D.IC7` | `{D.IC7}` |
| III | `maps:eq:D.IC8` | `{D.IC8}` |
| III | `maps:eq:D.IC9` | `{D.IC9}` |
| III | `maps:eq:D.IS1` | `{D.IS1}` |
| III | `maps:eq:D.IS2` | `{D.IS2}` |
| III | `maps:eq:D.MP1` | `{D.MP1}` |
| III | `maps:eq:D.MP10` | `{D.MP10}` |
| III | `maps:eq:D.MP2` | `{D.MP2}` |
| III | `maps:eq:D.MP3` | `{D.MP3}` |
| III | `maps:eq:D.MP4` | `{D.MP4}` |
| III | `maps:eq:D.MP5` | `{D.MP5}` |
| III | `maps:eq:D.MP6` | `{D.MP6}` |
| III | `maps:eq:D.MP7` | `{D.MP7}` |
| III | `maps:eq:D.MP8` | `{D.MP8}` |
| III | `maps:eq:D.MP9` | `{D.MP9}` |
| III | `maps:eq:D.MT1` | `{D.MT1}` |
| III | `maps:eq:D.MT2` | `{D.MT2}` |
| III | `maps:eq:D.MT3` | `{D.MT3}` |
| III | `maps:eq:D.O1` | `{D.O1}` |
| III | `maps:eq:D.O2` | `{D.O2}` |
| III | `maps:eq:D.O3` | `{D.O3}` |
| III | `maps:eq:D.O4` | `{D.O4}` |
| III | `maps:eq:D.O5` | `{D.O5}` |
| III | `maps:eq:D.O6` | `{D.O6}` |
| III | `maps:eq:D.O7` | `{D.O7}` |
| III | `maps:eq:D.O8` | `{D.O8}` |
| III | `maps:eq:D.O9` | `{D.O9}` |
| III | `maps:eq:D.OC1` | `{D.OC1}` |
| III | `maps:eq:D.OC2` | `{D.OC2}` |
| III | `maps:eq:D.OC3` | `{D.OC3}` |
| III | `maps:eq:D.OC4` | `{D.OC4}` |
| III | `maps:eq:D.OC5` | `{D.OC5}` |
| III | `maps:eq:D.OC6` | `{D.OC6}` |
| III | `maps:eq:D.OC7` | `{D.OC7}` |
| III | `maps:eq:D.OD1` | `{D.OD1}` |
| III | `maps:eq:D.OD2` | `{D.OD2}` |
| III | `maps:eq:D.OD3` | `{D.OD3}` |
| III | `maps:eq:D.OD4` | `{D.OD4}` |
| III | `maps:eq:D.OD5` | `{D.OD5}` |
| III | `maps:eq:D.OF1` | `{D.OF1}` |
| III | `maps:eq:D.OF10` | `{D.OF10}` |
| III | `maps:eq:D.OF11` | `{D.OF11}` |
| III | `maps:eq:D.OF12` | `{D.OF12}` |
| III | `maps:eq:D.OF13` | `{D.OF13}` |
| III | `maps:eq:D.OF14` | `{D.OF14}` |
| III | `maps:eq:D.OF15` | `{D.OF15}` |
| III | `maps:eq:D.OF16` | `{D.OF16}` |
| III | `maps:eq:D.OF17` | `{D.OF17}` |
| III | `maps:eq:D.OF18` | `{D.OF18}` |
| III | `maps:eq:D.OF19` | `{D.OF19}` |
| III | `maps:eq:D.OF2` | `{D.OF2}` |
| III | `maps:eq:D.OF3` | `{D.OF3}` |
| III | `maps:eq:D.OF4` | `{D.OF4}` |
| III | `maps:eq:D.OF5` | `{D.OF5}` |
| III | `maps:eq:D.OF6` | `{D.OF6}` |
| III | `maps:eq:D.OF7` | `{D.OF7}` |
| III | `maps:eq:D.OF8` | `{D.OF8}` |
| III | `maps:eq:D.OF9` | `{D.OF9}` |
| III | `maps:eq:D.OL1` | `{D.OL1}` |
| III | `maps:eq:D.OL10` | `{D.OL10}` |
| III | `maps:eq:D.OL11` | `{D.OL11}` |
| III | `maps:eq:D.OL12` | `{D.OL12}` |
| III | `maps:eq:D.OL2` | `{D.OL2}` |
| III | `maps:eq:D.OL3` | `{D.OL3}` |
| III | `maps:eq:D.OL4` | `{D.OL4}` |
| III | `maps:eq:D.OL5` | `{D.OL5}` |
| III | `maps:eq:D.OL6` | `{D.OL6}` |
| III | `maps:eq:D.OL7` | `{D.OL7}` |
| III | `maps:eq:D.OL8` | `{D.OL8}` |
| III | `maps:eq:D.OL9` | `{D.OL9}` |
| III | `maps:eq:D.OM1` | `{D.OM1}` |
| III | `maps:eq:D.OM10` | `{D.OM10}` |
| III | `maps:eq:D.OM2` | `{D.OM2}` |
| III | `maps:eq:D.OM3` | `{D.OM3}` |
| III | `maps:eq:D.OM4` | `{D.OM4}` |
| III | `maps:eq:D.OM5` | `{D.OM5}` |
| III | `maps:eq:D.OM6` | `{D.OM6}` |
| III | `maps:eq:D.OM7` | `{D.OM7}` |
| III | `maps:eq:D.OM8` | `{D.OM8}` |
| III | `maps:eq:D.OM9` | `{D.OM9}` |
| III | `maps:eq:D.OP1` | `{D.OP1}` |
| III | `maps:eq:D.OP10` | `{D.OP10}` |
| III | `maps:eq:D.OP11` | `{D.OP11}` |
| III | `maps:eq:D.OP2` | `{D.OP2}` |
| III | `maps:eq:D.OP3` | `{D.OP3}` |
| III | `maps:eq:D.OP4` | `{D.OP4}` |
| III | `maps:eq:D.OP5` | `{D.OP5}` |
| III | `maps:eq:D.OP5a` | `{D.OP5a}` |
| III | `maps:eq:D.OP6` | `{D.OP6}` |
| III | `maps:eq:D.OP7` | `{D.OP7}` |
| III | `maps:eq:D.OP8` | `{D.OP8}` |
| III | `maps:eq:D.OP9` | `{D.OP9}` |
| III | `maps:eq:D.OS1` | `{D.OS1}` |
| III | `maps:eq:D.OS2` | `{D.OS2}` |
| III | `maps:eq:D.OS3` | `{D.OS3}` |
| III | `maps:eq:D.OS4` | `{D.OS4}` |
| III | `maps:eq:D.OS5` | `{D.OS5}` |
| III | `maps:eq:D.OS6` | `{D.OS6}` |
| III | `maps:eq:D.OS7` | `{D.OS7}` |
| III | `maps:eq:D.OS8` | `{D.OS8}` |
| III | `maps:eq:D.OW1` | `{D.OW1}` |
| III | `maps:eq:D.OW2` | `{D.OW2}` |
| III | `maps:eq:D.OW3` | `{D.OW3}` |
| III | `maps:eq:D.OW4` | `{D.OW4}` |
| III | `maps:eq:D.OW5` | `{D.OW5}` |
| III | `maps:eq:D.OW6` | `{D.OW6}` |
| III | `maps:eq:D.OW7` | `{D.OW7}` |
| III | `maps:eq:D.PC1` | `{D.PC1}` |
| III | `maps:eq:D.PC10` | `{D.PC10}` |
| III | `maps:eq:D.PC11` | `{D.PC11}` |
| III | `maps:eq:D.PC12` | `{D.PC12}` |
| III | `maps:eq:D.PC13` | `{D.PC13}` |
| III | `maps:eq:D.PC14` | `{D.PC14}` |
| III | `maps:eq:D.PC2` | `{D.PC2}` |
| III | `maps:eq:D.PC3` | `{D.PC3}` |
| III | `maps:eq:D.PC4` | `{D.PC4}` |
| III | `maps:eq:D.PC5` | `{D.PC5}` |
| III | `maps:eq:D.PC6` | `{D.PC6}` |
| III | `maps:eq:D.PC7` | `{D.PC7}` |
| III | `maps:eq:D.PC8` | `{D.PC8}` |
| III | `maps:eq:D.PC9` | `{D.PC9}` |
| III | `maps:eq:D.R1` | `{D.R1}` |
| III | `maps:eq:D.R2` | `{D.R2}` |
| III | `maps:eq:D.R3` | `{D.R3}` |
| III | `maps:eq:D.R4` | `{D.R4}` |
| III | `maps:eq:D.S1` | `{D.S1}` |
| III | `maps:eq:D.S10` | `{D.S10}` |
| III | `maps:eq:D.S11` | `{D.S11}` |
| III | `maps:eq:D.S12` | `{D.S12}` |
| III | `maps:eq:D.S13` | `{D.S13}` |
| III | `maps:eq:D.S14` | `{D.S14}` |
| III | `maps:eq:D.S2` | `{D.S2}` |
| III | `maps:eq:D.S3` | `{D.S3}` |
| III | `maps:eq:D.S4` | `{D.S4}` |
| III | `maps:eq:D.S5` | `{D.S5}` |
| III | `maps:eq:D.S6` | `{D.S6}` |
| III | `maps:eq:D.S7` | `{D.S7}` |
| III | `maps:eq:D.S8` | `{D.S8}` |
| III | `maps:eq:D.S9` | `{D.S9}` |
| III | `maps:eq:D.SC1` | `{D.SC1}` |
| III | `maps:eq:D.SC2` | `{D.SC2}` |
| III | `maps:eq:D.SC3` | `{D.SC3}` |
| III | `maps:eq:D.SC4` | `{D.SC4}` |
| III | `maps:eq:D.SC5` | `{D.SC5}` |
| III | `maps:eq:D.SC6` | `{D.SC6}` |
| III | `maps:eq:D.SC7` | `{D.SC7}` |
| III | `maps:eq:D.SC8` | `{D.SC8}` |
| III | `maps:eq:D.SL1` | `{D.SL1}` |
| III | `maps:eq:D.SL10` | `{D.SL10}` |
| III | `maps:eq:D.SL11` | `{D.SL11}` |
| III | `maps:eq:D.SL12` | `{D.SL12}` |
| III | `maps:eq:D.SL13` | `{D.SL13}` |
| III | `maps:eq:D.SL14` | `{D.SL14}` |
| III | `maps:eq:D.SL15` | `{D.SL15}` |
| III | `maps:eq:D.SL16` | `{D.SL16}` |
| III | `maps:eq:D.SL17` | `{D.SL17}` |
| III | `maps:eq:D.SL18` | `{D.SL18}` |
| III | `maps:eq:D.SL19` | `{D.SL19}` |
| III | `maps:eq:D.SL2` | `{D.SL2}` |
| III | `maps:eq:D.SL20` | `{D.SL20}` |
| III | `maps:eq:D.SL21` | `{D.SL21}` |
| III | `maps:eq:D.SL22` | `{D.SL22}` |
| III | `maps:eq:D.SL23` | `{D.SL23}` |
| III | `maps:eq:D.SL24` | `{D.SL24}` |
| III | `maps:eq:D.SL3` | `{D.SL3}` |
| III | `maps:eq:D.SL4` | `{D.SL4}` |
| III | `maps:eq:D.SL5` | `{D.SL5}` |
| III | `maps:eq:D.SL6` | `{D.SL6}` |
| III | `maps:eq:D.SL7` | `{D.SL7}` |
| III | `maps:eq:D.SL8` | `{D.SL8}` |
| III | `maps:eq:D.SL9` | `{D.SL9}` |
| III | `maps:eq:D.ST1` | `{D.ST1}` |
| III | `maps:eq:D.ST10` | `{D.ST10}` |
| III | `maps:eq:D.ST11` | `{D.ST11}` |
| III | `maps:eq:D.ST12` | `{D.ST12}` |
| III | `maps:eq:D.ST13` | `{D.ST13}` |
| III | `maps:eq:D.ST2` | `{D.ST2}` |
| III | `maps:eq:D.ST3` | `{D.ST3}` |
| III | `maps:eq:D.ST4` | `{D.ST4}` |
| III | `maps:eq:D.ST5` | `{D.ST5}` |
| III | `maps:eq:D.ST6` | `{D.ST6}` |
| III | `maps:eq:D.ST7` | `{D.ST7}` |
| III | `maps:eq:D.ST8` | `{D.ST8}` |
| III | `maps:eq:D.ST9` | `{D.ST9}` |
| III | `maps:eq:D.T1` | `{D.T1}` |
| III | `maps:eq:D.T10` | `{D.T10}` |
| III | `maps:eq:D.T2` | `{D.T2}` |
| III | `maps:eq:D.T3` | `{D.T3}` |
| III | `maps:eq:D.T31` | `{D.T31}` |
| III | `maps:eq:D.T32` | `{D.T32}` |
| III | `maps:eq:D.T33` | `{D.T33}` |
| III | `maps:eq:D.T34` | `{D.T34}` |
| III | `maps:eq:D.T35` | `{D.T35}` |
| III | `maps:eq:D.T36` | `{D.T36}` |
| III | `maps:eq:D.T37` | `{D.T37}` |
| III | `maps:eq:D.T38` | `{D.T38}` |
| III | `maps:eq:D.T39` | `{D.T39}` |
| III | `maps:eq:D.T4` | `{D.T4}` |
| III | `maps:eq:D.T5` | `{D.T5}` |
| III | `maps:eq:D.T6` | `{D.T6}` |
| III | `maps:eq:D.T7` | `{D.T7}` |
| III | `maps:eq:D.T8` | `{D.T8}` |
| III | `maps:eq:D.T9` | `{D.T9}` |
| III | `maps:eq:D.TP1` | `{D.TP1}` |
| III | `maps:eq:D.TP2` | `{D.TP2}` |
| III | `maps:eq:D.TP3` | `{D.TP3}` |
| III | `maps:eq:D.TP4` | `{D.TP4}` |
| III | `maps:eq:D.TP5` | `{D.TP5}` |
| III | `maps:eq:D.TP6` | `{D.TP6}` |
| III | `maps:eq:D.TP7` | `{D.TP7}` |
| III | `maps:eq:D.TP8` | `{D.TP8}` |
| III | `maps:eq:D.UF1` | `{D.UF1}` |
| III | `maps:eq:D.UF10` | `{D.UF10}` |
| III | `maps:eq:D.UF2` | `{D.UF2}` |
| III | `maps:eq:D.UF3` | `{D.UF3}` |
| III | `maps:eq:D.UF4` | `{D.UF4}` |
| III | `maps:eq:D.UF5` | `{D.UF5}` |
| III | `maps:eq:D.UF6` | `{D.UF6}` |
| III | `maps:eq:D.UF7` | `{D.UF7}` |
| III | `maps:eq:D.UF8` | `{D.UF8}` |
| III | `maps:eq:D.UF9` | `{D.UF9}` |
| III | `maps:eq:D.V1` | `{D.V1}` |
| III | `maps:eq:D.V2` | `{D.V2}` |
| III | `maps:eq:D.V3` | `{D.V3}` |
| III | `maps:eq:D.V4` | `{D.V4}` |
| III | `maps:eq:D.V5` | `{D.V5}` |
| III | `maps:eq:D.VC1` | `{D.VC1}` |
| III | `maps:eq:D.VC10` | `{D.VC10}` |
| III | `maps:eq:D.VC2` | `{D.VC2}` |
| III | `maps:eq:D.VC3` | `{D.VC3}` |
| III | `maps:eq:D.VC4` | `{D.VC4}` |
| III | `maps:eq:D.VC5` | `{D.VC5}` |
| III | `maps:eq:D.VC6` | `{D.VC6}` |
| III | `maps:eq:D.VC7` | `{D.VC7}` |
| III | `maps:eq:D.VC8` | `{D.VC8}` |
| III | `maps:eq:D.VC9` | `{D.VC9}` |
| III | `maps:eq:D.WE1` | `{D.WE1}` |
| III | `maps:eq:D.WE10` | `{D.WE10}` |
| III | `maps:eq:D.WE11` | `{D.WE11}` |
| III | `maps:eq:D.WE12` | `{D.WE12}` |
| III | `maps:eq:D.WE13` | `{D.WE13}` |
| III | `maps:eq:D.WE14` | `{D.WE14}` |
| III | `maps:eq:D.WE2` | `{D.WE2}` |
| III | `maps:eq:D.WE3` | `{D.WE3}` |
| III | `maps:eq:D.WE4` | `{D.WE4}` |
| III | `maps:eq:D.WE5` | `{D.WE5}` |
| III | `maps:eq:D.WE6` | `{D.WE6}` |
| III | `maps:eq:D.WE7` | `{D.WE7}` |
| III | `maps:eq:D.WE8` | `{D.WE8}` |
| III | `maps:eq:D.WE9` | `{D.WE9}` |
| III | `maps:eq:D.WI1` | `{D.WI1}` |
| III | `maps:eq:D.WI10` | `{D.WI10}` |
| III | `maps:eq:D.WI11` | `{D.WI11}` |
| III | `maps:eq:D.WI12` | `{D.WI12}` |
| III | `maps:eq:D.WI13` | `{D.WI13}` |
| III | `maps:eq:D.WI14` | `{D.WI14}` |
| III | `maps:eq:D.WI15` | `{D.WI15}` |
| III | `maps:eq:D.WI16` | `{D.WI16}` |
| III | `maps:eq:D.WI17` | `{D.WI17}` |
| III | `maps:eq:D.WI18` | `{D.WI18}` |
| III | `maps:eq:D.WI19` | `{D.WI19}` |
| III | `maps:eq:D.WI2` | `{D.WI2}` |
| III | `maps:eq:D.WI20` | `{D.WI20}` |
| III | `maps:eq:D.WI21` | `{D.WI21}` |
| III | `maps:eq:D.WI22` | `{D.WI22}` |
| III | `maps:eq:D.WI3` | `{D.WI3}` |
| III | `maps:eq:D.WI4` | `{D.WI4}` |
| III | `maps:eq:D.WI5` | `{D.WI5}` |
| III | `maps:eq:D.WI6` | `{D.WI6}` |
| III | `maps:eq:D.WI7` | `{D.WI7}` |
| III | `maps:eq:D.WI8` | `{D.WI8}` |
| III | `maps:eq:D.WI9` | `{D.WI9}` |
| III | `maps:eq:D.WP1` | `{D.WP1}` |
| III | `maps:eq:D.WP10` | `{D.WP10}` |
| III | `maps:eq:D.WP11` | `{D.WP11}` |
| III | `maps:eq:D.WP12` | `{D.WP12}` |
| III | `maps:eq:D.WP2` | `{D.WP2}` |
| III | `maps:eq:D.WP3` | `{D.WP3}` |
| III | `maps:eq:D.WP4` | `{D.WP4}` |
| III | `maps:eq:D.WP5` | `{D.WP5}` |
| III | `maps:eq:D.WP6` | `{D.WP6}` |
| III | `maps:eq:D.WP7` | `{D.WP7}` |
| III | `maps:eq:D.WP8` | `{D.WP8}` |
| III | `maps:eq:D.WP9` | `{D.WP9}` |
| III | `maps:eq:D44.0a` | `{D44.0a}` |
| III | `maps:eq:D44.0b` | `{D44.0b}` |
| III | `maps:eq:D44.1` | `{D44.1}` |
| III | `maps:eq:D44.10` | `{D44.10}` |
| III | `maps:eq:D44.11` | `{D44.11}` |
| III | `maps:eq:D44.12` | `{D44.12}` |
| III | `maps:eq:D44.13` | `{D44.13}` |
| III | `maps:eq:D44.14` | `{D44.14}` |
| III | `maps:eq:D44.2` | `{D44.2}` |
| III | `maps:eq:D44.3` | `{D44.3}` |
| III | `maps:eq:D44.4` | `{D44.4}` |
| III | `maps:eq:D44.5` | `{D44.5}` |
| III | `maps:eq:D44.6` | `{D44.6}` |
| III | `maps:eq:D44.7` | `{D44.7}` |
| III | `maps:eq:D44.8` | `{D44.8}` |
| III | `maps:eq:D44.9` | `{D44.9}` |
| III | `maps:eq:D45.1` | `{D45.1}` |
| III | `maps:eq:D45.10` | `{D45.10}` |
| III | `maps:eq:D45.11` | `{D45.11}` |
| III | `maps:eq:D45.12` | `{D45.12}` |
| III | `maps:eq:D45.13` | `{D45.13}` |
| III | `maps:eq:D45.14` | `{D45.14}` |
| III | `maps:eq:D45.15` | `{D45.15}` |
| III | `maps:eq:D45.16` | `{D45.16}` |
| III | `maps:eq:D45.17` | `{D45.17}` |
| III | `maps:eq:D45.18` | `{D45.18}` |
| III | `maps:eq:D45.19` | `{D45.19}` |
| III | `maps:eq:D45.2` | `{D45.2}` |
| III | `maps:eq:D45.20` | `{D45.20}` |
| III | `maps:eq:D45.21` | `{D45.21}` |
| III | `maps:eq:D45.22` | `{D45.22}` |
| III | `maps:eq:D45.3` | `{D45.3}` |
| III | `maps:eq:D45.4` | `{D45.4}` |
| III | `maps:eq:D45.5` | `{D45.5}` |
| III | `maps:eq:D45.6` | `{D45.6}` |
| III | `maps:eq:D45.7` | `{D45.7}` |
| III | `maps:eq:D45.8` | `{D45.8}` |
| III | `maps:eq:D45.9` | `{D45.9}` |
| III | `maps:eq:D47.1` | `{D47.1}` |
| III | `maps:eq:D47.10` | `{D47.10}` |
| III | `maps:eq:D47.11` | `{D47.11}` |
| III | `maps:eq:D47.12` | `{D47.12}` |
| III | `maps:eq:D47.13` | `{D47.13}` |
| III | `maps:eq:D47.2` | `{D47.2}` |
| III | `maps:eq:D47.3` | `{D47.3}` |
| III | `maps:eq:D47.4` | `{D47.4}` |
| III | `maps:eq:D47.5` | `{D47.5}` |
| III | `maps:eq:D47.6` | `{D47.6}` |
| III | `maps:eq:D47.7` | `{D47.7}` |
| III | `maps:eq:D47.8` | `{D47.8}` |
| III | `maps:eq:D47.9` | `{D47.9}` |
| III | `maps:eq:E.1` | `{E.1}` |
| III | `maps:eq:E.10` | `{E.10}` |
| III | `maps:eq:E.11` | `{E.11}` |
| III | `maps:eq:E.12` | `{E.12}` |
| III | `maps:eq:E.13` | `{E.13}` |
| III | `maps:eq:E.14` | `{E.14}` |
| III | `maps:eq:E.15` | `{E.15}` |
| III | `maps:eq:E.16` | `{E.16}` |
| III | `maps:eq:E.17` | `{E.17}` |
| III | `maps:eq:E.2` | `{E.2}` |
| III | `maps:eq:E.20` | `{E.20}` |
| III | `maps:eq:E.3` | `{E.3}` |
| III | `maps:eq:E.4` | `{E.4}` |
| III | `maps:eq:E.5` | `{E.5}` |
| III | `maps:eq:E.6` | `{E.6}` |
| III | `maps:eq:E.7` | `{E.7}` |
| III | `maps:eq:E.8` | `{E.8}` |
| III | `maps:eq:E.9` | `{E.9}` |
| III | `maps:eq:E.B1` | `{E.B1}` |
| III | `maps:eq:E.B2` | `{E.B2}` |
| III | `maps:eq:E.B3` | `{E.B3}` |
| III | `maps:eq:E.B4` | `{E.B4}` |
| III | `maps:eq:E.B5` | `{E.B5}` |
| III | `maps:eq:E.B6` | `{E.B6}` |
| III | `maps:eq:E.B7` | `{E.B7}` |
| III | `maps:eq:E.C1` | `{E.C1}` |
| III | `maps:eq:E.C10` | `{E.C10}` |
| III | `maps:eq:E.C11` | `{E.C11}` |
| III | `maps:eq:E.C12` | `{E.C12}` |
| III | `maps:eq:E.C13` | `{E.C13}` |
| III | `maps:eq:E.C14` | `{E.C14}` |
| III | `maps:eq:E.C15` | `{E.C15}` |
| III | `maps:eq:E.C16` | `{E.C16}` |
| III | `maps:eq:E.C17` | `{E.C17}` |
| III | `maps:eq:E.C18` | `{E.C18}` |
| III | `maps:eq:E.C19a` | `{E.C19a}` |
| III | `maps:eq:E.C19b` | `{E.C19b}` |
| III | `maps:eq:E.C2` | `{E.C2}` |
| III | `maps:eq:E.C20` | `{E.C20}` |
| III | `maps:eq:E.C21` | `{E.C21}` |
| III | `maps:eq:E.C3` | `{E.C3}` |
| III | `maps:eq:E.C4` | `{E.C4}` |
| III | `maps:eq:E.C5` | `{E.C5}` |
| III | `maps:eq:E.C6` | `{E.C6}` |
| III | `maps:eq:E.C7` | `{E.C7}` |
| III | `maps:eq:E.C8` | `{E.C8}` |
| III | `maps:eq:E.C9` | `{E.C9}` |
| III | `maps:eq:E.H0` | `{E.H0}` |
| III | `maps:eq:E.H1` | `{E.H1}` |
| III | `maps:eq:E.H10` | `{E.H10}` |
| III | `maps:eq:E.H11` | `{E.H11}` |
| III | `maps:eq:E.H12` | `{E.H12}` |
| III | `maps:eq:E.H13` | `{E.H13}` |
| III | `maps:eq:E.H2` | `{E.H2}` |
| III | `maps:eq:E.H3` | `{E.H3}` |
| III | `maps:eq:E.H4` | `{E.H4}` |
| III | `maps:eq:E.H5` | `{E.H5}` |
| III | `maps:eq:E.H6` | `{E.H6}` |
| III | `maps:eq:E.H7` | `{E.H7}` |
| III | `maps:eq:E.H8` | `{E.H8}` |
| III | `maps:eq:E.H9` | `{E.H9}` |
| III | `maps:eq:E.H9a` | `{E.H9a}` |
| III | `maps:eq:E.I1` | `{E.I1}` |
| III | `maps:eq:E.I2` | `{E.I2}` |
| III | `maps:eq:E.I3` | `{E.I3}` |
| III | `maps:eq:E.I4` | `{E.I4}` |
| III | `maps:eq:E.I5` | `{E.I5}` |
| III | `maps:eq:E.MV1` | `{E.MV1}` |
| III | `maps:eq:E.MV2` | `{E.MV2}` |
| III | `maps:eq:E.MV3` | `{E.MV3}` |
| III | `maps:eq:E.MV4` | `{E.MV4}` |
| III | `maps:eq:E.MV5` | `{E.MV5}` |
| III | `maps:eq:E.MV6` | `{E.MV6}` |
| III | `maps:eq:E.MV7` | `{E.MV7}` |
| III | `maps:eq:E.MV8` | `{E.MV8}` |
| III | `maps:eq:E.MV9` | `{E.MV9}` |
| III | `maps:eq:E.P1` | `{E.P1}` |
| III | `maps:eq:E.P10` | `{E.P10}` |
| III | `maps:eq:E.P11` | `{E.P11}` |
| III | `maps:eq:E.P12` | `{E.P12}` |
| III | `maps:eq:E.P13` | `{E.P13}` |
| III | `maps:eq:E.P14` | `{E.P14}` |
| III | `maps:eq:E.P15` | `{E.P15}` |
| III | `maps:eq:E.P16` | `{E.P16}` |
| III | `maps:eq:E.P17` | `{E.P17}` |
| III | `maps:eq:E.P2` | `{E.P2}` |
| III | `maps:eq:E.P3` | `{E.P3}` |
| III | `maps:eq:E.P4` | `{E.P4}` |
| III | `maps:eq:E.P5` | `{E.P5}` |
| III | `maps:eq:E.P6` | `{E.P6}` |
| III | `maps:eq:E.P7` | `{E.P7}` |
| III | `maps:eq:E.P8` | `{E.P8}` |
| III | `maps:eq:E.P9` | `{E.P9}` |
| III | `maps:eq:E.Q1` | `{E.Q1}` |
| III | `maps:eq:E.Q10` | `{E.Q10}` |
| III | `maps:eq:E.Q11` | `{E.Q11}` |
| III | `maps:eq:E.Q12` | `{E.Q12}` |
| III | `maps:eq:E.Q2` | `{E.Q2}` |
| III | `maps:eq:E.Q3` | `{E.Q3}` |
| III | `maps:eq:E.Q4` | `{E.Q4}` |
| III | `maps:eq:E.Q5` | `{E.Q5}` |
| III | `maps:eq:E.Q6` | `{E.Q6}` |
| III | `maps:eq:E.Q7` | `{E.Q7}` |
| III | `maps:eq:E.Q8` | `{E.Q8}` |
| III | `maps:eq:E.Q9` | `{E.Q9}` |
| III | `maps:eq:E.S1` | `{E.S1}` |
| III | `maps:eq:E.S10` | `{E.S10}` |
| III | `maps:eq:E.S11` | `{E.S11}` |
| III | `maps:eq:E.S12` | `{E.S12}` |
| III | `maps:eq:E.S13` | `{E.S13}` |
| III | `maps:eq:E.S14` | `{E.S14}` |
| III | `maps:eq:E.S15` | `{E.S15}` |
| III | `maps:eq:E.S16` | `{E.S16}` |
| III | `maps:eq:E.S17` | `{E.S17}` |
| III | `maps:eq:E.S18` | `{E.S18}` |
| III | `maps:eq:E.S19` | `{E.S19}` |
| III | `maps:eq:E.S2` | `{E.S2}` |
| III | `maps:eq:E.S20` | `{E.S20}` |
| III | `maps:eq:E.S21` | `{E.S21}` |
| III | `maps:eq:E.S22` | `{E.S22}` |
| III | `maps:eq:E.S23` | `{E.S23}` |
| III | `maps:eq:E.S24` | `{E.S24}` |
| III | `maps:eq:E.S25` | `{E.S25}` |
| III | `maps:eq:E.S26` | `{E.S26}` |
| III | `maps:eq:E.S27` | `{E.S27}` |
| III | `maps:eq:E.S28` | `{E.S28}` |
| III | `maps:eq:E.S29` | `{E.S29}` |
| III | `maps:eq:E.S3` | `{E.S3}` |
| III | `maps:eq:E.S30` | `{E.S30}` |
| III | `maps:eq:E.S31` | `{E.S31}` |
| III | `maps:eq:E.S32` | `{E.S32}` |
| III | `maps:eq:E.S33` | `{E.S33}` |
| III | `maps:eq:E.S34` | `{E.S34}` |
| III | `maps:eq:E.S35` | `{E.S35}` |
| III | `maps:eq:E.S36` | `{E.S36}` |
| III | `maps:eq:E.S37` | `{E.S37}` |
| III | `maps:eq:E.S38` | `{E.S38}` |
| III | `maps:eq:E.S39` | `{E.S39}` |
| III | `maps:eq:E.S4` | `{E.S4}` |
| III | `maps:eq:E.S40` | `{E.S40}` |
| III | `maps:eq:E.S41` | `{E.S41}` |
| III | `maps:eq:E.S42` | `{E.S42}` |
| III | `maps:eq:E.S43` | `{E.S43}` |
| III | `maps:eq:E.S44` | `{E.S44}` |
| III | `maps:eq:E.S45` | `{E.S45}` |
| III | `maps:eq:E.S46` | `{E.S46}` |
| III | `maps:eq:E.S47` | `{E.S47}` |
| III | `maps:eq:E.S48` | `{E.S48}` |
| III | `maps:eq:E.S49` | `{E.S49}` |
| III | `maps:eq:E.S5` | `{E.S5}` |
| III | `maps:eq:E.S50` | `{E.S50}` |
| III | `maps:eq:E.S51` | `{E.S51}` |
| III | `maps:eq:E.S52` | `{E.S52}` |
| III | `maps:eq:E.S53` | `{E.S53}` |
| III | `maps:eq:E.S54` | `{E.S54}` |
| III | `maps:eq:E.S55` | `{E.S55}` |
| III | `maps:eq:E.S6` | `{E.S6}` |
| III | `maps:eq:E.S7` | `{E.S7}` |
| III | `maps:eq:E.S8` | `{E.S8}` |
| III | `maps:eq:E.S9` | `{E.S9}` |
| III | `maps:eq:E.T1` | `{E.T1}` |
| III | `maps:eq:E.T2` | `{E.T2}` |
| III | `maps:eq:E.T3` | `{E.T3}` |
| III | `maps:eq:E.T4` | `{E.T4}` |
| III | `maps:eq:E.T5` | `{E.T5}` |
| III | `maps:eq:E.T6` | `{E.T6}` |
| III | `maps:eq:E.T7` | `{E.T7}` |
| III | `maps:eq:E.T8` | `{E.T8}` |
| III | `maps:eq:E.T9` | `{E.T9}` |
| III | `maps:eq:E.U1` | `{E.U1}` |
| III | `maps:eq:E.U10` | `{E.U10}` |
| III | `maps:eq:E.U11` | `{E.U11}` |
| III | `maps:eq:E.U2` | `{E.U2}` |
| III | `maps:eq:E.U3` | `{E.U3}` |
| III | `maps:eq:E.U4` | `{E.U4}` |
| III | `maps:eq:E.U5` | `{E.U5}` |
| III | `maps:eq:E.U6` | `{E.U6}` |
| III | `maps:eq:E.U7` | `{E.U7}` |
| III | `maps:eq:E.U8` | `{E.U8}` |
| III | `maps:eq:E.U9` | `{E.U9}` |
| III | `maps:eq:F.1` | `{F.1}` |
| III | `maps:eq:F.10` | `{F.10}` |
| III | `maps:eq:F.11` | `{F.11}` |
| III | `maps:eq:F.12` | `{F.12}` |
| III | `maps:eq:F.13` | `{F.13}` |
| III | `maps:eq:F.14` | `{F.14}` |
| III | `maps:eq:F.15` | `{F.15}` |
| III | `maps:eq:F.16` | `{F.16}` |
| III | `maps:eq:F.17` | `{F.17}` |
| III | `maps:eq:F.18` | `{F.18}` |
| III | `maps:eq:F.19` | `{F.19}` |
| III | `maps:eq:F.2` | `{F.2}` |
| III | `maps:eq:F.20` | `{F.20}` |
| III | `maps:eq:F.21` | `{F.21}` |
| III | `maps:eq:F.22` | `{F.22}` |
| III | `maps:eq:F.23` | `{F.23}` |
| III | `maps:eq:F.24` | `{F.24}` |
| III | `maps:eq:F.25` | `{F.25}` |
| III | `maps:eq:F.26` | `{F.26}` |
| III | `maps:eq:F.27` | `{F.27}` |
| III | `maps:eq:F.28` | `{F.28}` |
| III | `maps:eq:F.29` | `{F.29}` |
| III | `maps:eq:F.3` | `{F.3}` |
| III | `maps:eq:F.30` | `{F.30}` |
| III | `maps:eq:F.31` | `{F.31}` |
| III | `maps:eq:F.32` | `{F.32}` |
| III | `maps:eq:F.33` | `{F.33}` |
| III | `maps:eq:F.34` | `{F.34}` |
| III | `maps:eq:F.35` | `{F.35}` |
| III | `maps:eq:F.36` | `{F.36}` |
| III | `maps:eq:F.37` | `{F.37}` |
| III | `maps:eq:F.38` | `{F.38}` |
| III | `maps:eq:F.39` | `{F.39}` |
| III | `maps:eq:F.4` | `{F.4}` |
| III | `maps:eq:F.40` | `{F.40}` |
| III | `maps:eq:F.5` | `{F.5}` |
| III | `maps:eq:F.6` | `{F.6}` |
| III | `maps:eq:F.7` | `{F.7}` |
| III | `maps:eq:F.8` | `{F.8}` |
| III | `maps:eq:F.9` | `{F.9}` |
| III | `maps:eq:F.CA1` | `{F.CA1}` |
| III | `maps:eq:F.CA2` | `{F.CA2}` |
| III | `maps:eq:F.CA3` | `{F.CA3}` |
| III | `maps:eq:F.CA4` | `{F.CA4}` |
| III | `maps:eq:F.CA5` | `{F.CA5}` |
| III | `maps:eq:F.CK1` | `{F.CK1}` |
| III | `maps:eq:F.CK2` | `{F.CK2}` |
| III | `maps:eq:F.CN1` | `{F.CN1}` |
| III | `maps:eq:F.CN2` | `{F.CN2}` |
| III | `maps:eq:F.CN3` | `{F.CN3}` |
| III | `maps:eq:F.G1` | `{F.G1}` |
| III | `maps:eq:F.G10` | `{F.G10}` |
| III | `maps:eq:F.G11` | `{F.G11}` |
| III | `maps:eq:F.G2` | `{F.G2}` |
| III | `maps:eq:F.G3` | `{F.G3}` |
| III | `maps:eq:F.G4` | `{F.G4}` |
| III | `maps:eq:F.G5` | `{F.G5}` |
| III | `maps:eq:F.G6` | `{F.G6}` |
| III | `maps:eq:F.G7` | `{F.G7}` |
| III | `maps:eq:F.G8` | `{F.G8}` |
| III | `maps:eq:F.G9` | `{F.G9}` |
| III | `maps:eq:F.GC1` | `{F.GC1}` |
| III | `maps:eq:F.GC2` | `{F.GC2}` |
| III | `maps:eq:F.GC3` | `{F.GC3}` |
| III | `maps:eq:F.GC4` | `{F.GC4}` |
| III | `maps:eq:F.GC5` | `{F.GC5}` |
| III | `maps:eq:F.GC5a` | `{F.GC5a}` |
| III | `maps:eq:F.GC6` | `{F.GC6}` |
| III | `maps:eq:F.GC7` | `{F.GC7}` |
| III | `maps:eq:F.GC8` | `{F.GC8}` |
| III | `maps:eq:F.GC9` | `{F.GC9}` |
| III | `maps:eq:F.HC1` | `{F.HC1}` |
| III | `maps:eq:F.HC10` | `{F.HC10}` |
| III | `maps:eq:F.HC11` | `{F.HC11}` |
| III | `maps:eq:F.HC12` | `{F.HC12}` |
| III | `maps:eq:F.HC13` | `{F.HC13}` |
| III | `maps:eq:F.HC2` | `{F.HC2}` |
| III | `maps:eq:F.HC3` | `{F.HC3}` |
| III | `maps:eq:F.HC4` | `{F.HC4}` |
| III | `maps:eq:F.HC5` | `{F.HC5}` |
| III | `maps:eq:F.HC6` | `{F.HC6}` |
| III | `maps:eq:F.HC7` | `{F.HC7}` |
| III | `maps:eq:F.HC8` | `{F.HC8}` |
| III | `maps:eq:F.HC9` | `{F.HC9}` |
| III | `maps:eq:F.IC1` | `{F.IC1}` |
| III | `maps:eq:F.IC2` | `{F.IC2}` |
| III | `maps:eq:F.IC3` | `{F.IC3}` |
| III | `maps:eq:F.IV1` | `{F.IV1}` |
| III | `maps:eq:F.IV2` | `{F.IV2}` |
| III | `maps:eq:F.IV3` | `{F.IV3}` |
| III | `maps:eq:F.IV4` | `{F.IV4}` |
| III | `maps:eq:F.L1` | `{F.L1}` |
| III | `maps:eq:F.L10` | `{F.L10}` |
| III | `maps:eq:F.L2` | `{F.L2}` |
| III | `maps:eq:F.L3` | `{F.L3}` |
| III | `maps:eq:F.L4` | `{F.L4}` |
| III | `maps:eq:F.L5` | `{F.L5}` |
| III | `maps:eq:F.L6` | `{F.L6}` |
| III | `maps:eq:F.L7` | `{F.L7}` |
| III | `maps:eq:F.L8` | `{F.L8}` |
| III | `maps:eq:F.L9` | `{F.L9}` |
| III | `maps:eq:F.LT1` | `{F.LT1}` |
| III | `maps:eq:F.LT2` | `{F.LT2}` |
| III | `maps:eq:F.LT3` | `{F.LT3}` |
| III | `maps:eq:F.LT4` | `{F.LT4}` |
| III | `maps:eq:F.LT5` | `{F.LT5}` |
| III | `maps:eq:F.LT6` | `{F.LT6}` |
| III | `maps:eq:F.LT7` | `{F.LT7}` |
| III | `maps:eq:F.LT8` | `{F.LT8}` |
| III | `maps:eq:F.LT9` | `{F.LT9}` |
| III | `maps:eq:F.O1` | `{F.O1}` |
| III | `maps:eq:F.O2` | `{F.O2}` |
| III | `maps:eq:F.O3` | `{F.O3}` |
| III | `maps:eq:F.O4` | `{F.O4}` |
| III | `maps:eq:F.O5` | `{F.O5}` |
| III | `maps:eq:F.O6` | `{F.O6}` |
| III | `maps:eq:F.O7` | `{F.O7}` |
| III | `maps:eq:F.R1` | `{F.R1}` |
| III | `maps:eq:F.R10` | `{F.R10}` |
| III | `maps:eq:F.R11` | `{F.R11}` |
| III | `maps:eq:F.R12` | `{F.R12}` |
| III | `maps:eq:F.R13` | `{F.R13}` |
| III | `maps:eq:F.R14` | `{F.R14}` |
| III | `maps:eq:F.R2` | `{F.R2}` |
| III | `maps:eq:F.R3` | `{F.R3}` |
| III | `maps:eq:F.R4` | `{F.R4}` |
| III | `maps:eq:F.R5` | `{F.R5}` |
| III | `maps:eq:F.R6` | `{F.R6}` |
| III | `maps:eq:F.R7` | `{F.R7}` |
| III | `maps:eq:F.R8` | `{F.R8}` |
| III | `maps:eq:F.R9` | `{F.R9}` |
| III | `maps:eq:F.S1` | `{F.S1}` |
| III | `maps:eq:F.S2` | `{F.S2}` |
| III | `maps:eq:F.S3` | `{F.S3}` |
| III | `maps:eq:F.S4` | `{F.S4}` |
| III | `maps:eq:F.S5` | `{F.S5}` |
| III | `maps:eq:F.S6` | `{F.S6}` |
| III | `maps:eq:F.S7` | `{F.S7}` |
| III | `maps:eq:F.S8` | `{F.S8}` |
| III | `maps:eq:F.S9` | `{F.S9}` |
| III | `maps:eq:F.SY1` | `{F.SY1}` |
| III | `maps:eq:F.T1` | `{F.T1}` |
| III | `maps:eq:F.T10` | `{F.T10}` |
| III | `maps:eq:F.T11` | `{F.T11}` |
| III | `maps:eq:F.T12` | `{F.T12}` |
| III | `maps:eq:F.T13` | `{F.T13}` |
| III | `maps:eq:F.T2` | `{F.T2}` |
| III | `maps:eq:F.T3` | `{F.T3}` |
| III | `maps:eq:F.T4` | `{F.T4}` |
| III | `maps:eq:F.T5` | `{F.T5}` |
| III | `maps:eq:F.T6` | `{F.T6}` |
| III | `maps:eq:F.T7` | `{F.T7}` |
| III | `maps:eq:F.T8` | `{F.T8}` |
| III | `maps:eq:F.T9` | `{F.T9}` |
| III | `maps:eq:F.U1` | `{F.U1}` |
| III | `maps:eq:F.U10` | `{F.U10}` |
| III | `maps:eq:F.U11` | `{F.U11}` |
| III | `maps:eq:F.U12` | `{F.U12}` |
| III | `maps:eq:F.U2` | `{F.U2}` |
| III | `maps:eq:F.U3` | `{F.U3}` |
| III | `maps:eq:F.U4` | `{F.U4}` |
| III | `maps:eq:F.U5` | `{F.U5}` |
| III | `maps:eq:F.U6` | `{F.U6}` |
| III | `maps:eq:F.U7` | `{F.U7}` |
| III | `maps:eq:F.U8` | `{F.U8}` |
| III | `maps:eq:F.U9` | `{F.U9}` |
| III | `maps:eq:F.X1` | `{F.X1}` |
| III | `maps:eq:F.X2` | `{F.X2}` |
| III | `maps:eq:F.X3` | `{F.X3}` |
| III | `maps:eq:F.X4` | `{F.X4}` |
| III | `maps:eq:F.X5` | `{F.X5}` |
| III | `maps:eq:FT.1` | `{FT.1}` |
| III | `maps:mapsF:repair:cyclic-inclusion` | `6.38` |
| III | `maps:mapsF:repair:log-cylinder-scope` | `6.39` |
| III | `maps:src:A.2.2` | `2.1` |
| III | `maps:src:B.1.1` | `2.2` |
| III | `maps:src:B.1.2` | `2.3` |
| III | `maps:src:B.2.1` | `2.4` |
| III | `maps:src:B.3.1` | `2.5` |
| III | `maps:src:B.3.2` | `2.6` |
| III | `maps:src:B.3.3` | `2.7` |
| III | `maps:src:B.4.1` | `2.8` |
| III | `maps:src:B.5.1` | `2.9` |
| III | `maps:src:B.5.2` | `2.10` |
| III | `maps:src:B.6.1` | `2.11` |
| III | `maps:src:B.6.10` | `2.19` |
| III | `maps:src:B.6.11` | `2.20` |
| III | `maps:src:B.6.12` | `2.21` |
| III | `maps:src:B.6.13` | `2.22` |
| III | `maps:src:B.6.14` | `2.23` |
| III | `maps:src:B.6.15` | `2.24` |
| III | `maps:src:B.6.16` | `2.25` |
| III | `maps:src:B.6.17` | `2.26` |
| III | `maps:src:B.6.18` | `2.27` |
| III | `maps:src:B.6.19` | `2.28` |
| III | `maps:src:B.6.2` | `2.12` |
| III | `maps:src:B.6.20` | `2.29` |
| III | `maps:src:B.6.21` | `2.30` |
| III | `maps:src:B.6.22` | `2.31` |
| III | `maps:src:B.6.23` | `2.32` |
| III | `maps:src:B.6.24` | `2.33` |
| III | `maps:src:B.6.25` | `2.34` |
| III | `maps:src:B.6.3` | `2.13` |
| III | `maps:src:B.6.4` | `2.14` |
| III | `maps:src:B.6.5` | `2.15` |
| III | `maps:src:B.6.6` | `2.16` |
| III | `maps:src:B.6.7` | `2.17` |
| III | `maps:src:B.6.8` | `2.18` |
| III | `maps:src:B.6.9` | `A.3` |
| III | `maps:src:C.1.1` | `3.1` |
| III | `maps:src:C.1.2` | `3.2` |
| III | `maps:src:C.1.3` | `3.3` |
| III | `maps:src:C.1.4` | `3.4` |
| III | `maps:src:C.1.5` | `3.5` |
| III | `maps:src:D.1.1` | `4.1` |
| III | `maps:src:D.1.10` | `4.10` |
| III | `maps:src:D.1.11` | `A.4` |
| III | `maps:src:D.1.12` | `4.11` |
| III | `maps:src:D.1.2` | `4.2` |
| III | `maps:src:D.1.3` | `4.3` |
| III | `maps:src:D.1.4` | `4.4` |
| III | `maps:src:D.1.5` | `4.5` |
| III | `maps:src:D.1.6` | `4.6` |
| III | `maps:src:D.1.7` | `4.7` |
| III | `maps:src:D.1.8` | `4.8` |
| III | `maps:src:D.1.9` | `4.9` |
| III | `maps:src:D.2.1` | `A.5` |
| III | `maps:src:D.2.10` | `4.19` |
| III | `maps:src:D.2.11` | `4.20` |
| III | `maps:src:D.2.12` | `4.21` |
| III | `maps:src:D.2.13` | `4.22` |
| III | `maps:src:D.2.14` | `4.23` |
| III | `maps:src:D.2.15` | `4.24` |
| III | `maps:src:D.2.16` | `4.25` |
| III | `maps:src:D.2.17` | `4.26` |
| III | `maps:src:D.2.18` | `4.27` |
| III | `maps:src:D.2.19` | `4.28` |
| III | `maps:src:D.2.2` | `4.12` |
| III | `maps:src:D.2.20` | `4.29` |
| III | `maps:src:D.2.21` | `4.30` |
| III | `maps:src:D.2.22` | `4.31` |
| III | `maps:src:D.2.23` | `4.32` |
| III | `maps:src:D.2.24` | `4.33` |
| III | `maps:src:D.2.25` | `4.34` |
| III | `maps:src:D.2.26` | `4.35` |
| III | `maps:src:D.2.27` | `4.36` |
| III | `maps:src:D.2.28` | `4.37` |
| III | `maps:src:D.2.29` | `4.38` |
| III | `maps:src:D.2.3` | `4.13` |
| III | `maps:src:D.2.30` | `4.39` |
| III | `maps:src:D.2.31` | `4.40` |
| III | `maps:src:D.2.32` | `4.41` |
| III | `maps:src:D.2.33` | `4.42` |
| III | `maps:src:D.2.34` | `4.43` |
| III | `maps:src:D.2.35` | `4.44` |
| III | `maps:src:D.2.36` | `4.45` |
| III | `maps:src:D.2.37` | `4.46` |
| III | `maps:src:D.2.38` | `4.47` |
| III | `maps:src:D.2.39` | `4.48` |
| III | `maps:src:D.2.4` | `AL.1` |
| III | `maps:src:D.2.40` | `4.49` |
| III | `maps:src:D.2.41` | `4.50` |
| III | `maps:src:D.2.42` | `4.51` |
| III | `maps:src:D.2.43` | `4.52` |
| III | `maps:src:D.2.44` | `4.53` |
| III | `maps:src:D.2.45` | `4.54` |
| III | `maps:src:D.2.46` | `4.55` |
| III | `maps:src:D.2.47` | `4.56` |
| III | `maps:src:D.2.48` | `4.57` |
| III | `maps:src:D.2.49` | `4.58` |
| III | `maps:src:D.2.5` | `4.14` |
| III | `maps:src:D.2.50` | `4.59` |
| III | `maps:src:D.2.51` | `4.60` |
| III | `maps:src:D.2.52` | `4.61` |
| III | `maps:src:D.2.53` | `4.62` |
| III | `maps:src:D.2.6` | `4.15` |
| III | `maps:src:D.2.7` | `4.16` |
| III | `maps:src:D.2.8` | `4.17` |
| III | `maps:src:D.2.9` | `4.18` |
| III | `maps:src:D.3.1` | `4.63` |
| III | `maps:src:D.3.2` | `A.6` |
| III | `maps:src:D.3.3` | `4.64` |
| III | `maps:src:D.3.4` | `A.7` |
| III | `maps:src:E.1.1` | `5.1` |
| III | `maps:src:E.1.2` | `5.2` |
| III | `maps:src:E.1.3` | `5.3` |
| III | `maps:src:E.1.4` | `5.4` |
| III | `maps:src:E.1.5` | `5.5` |
| III | `maps:src:E.2.1` | `5.6` |
| III | `maps:src:E.2.10` | `5.14` |
| III | `maps:src:E.2.11` | `5.15` |
| III | `maps:src:E.2.12` | `5.16` |
| III | `maps:src:E.2.13` | `5.17` |
| III | `maps:src:E.2.14` | `5.18` |
| III | `maps:src:E.2.15` | `5.19` |
| III | `maps:src:E.2.16` | `5.20` |
| III | `maps:src:E.2.17` | `5.21` |
| III | `maps:src:E.2.18` | `5.22` |
| III | `maps:src:E.2.19` | `5.23` |
| III | `maps:src:E.2.2` | `A.8` |
| III | `maps:src:E.2.20` | `5.24` |
| III | `maps:src:E.2.21` | `5.25` |
| III | `maps:src:E.2.3` | `5.7` |
| III | `maps:src:E.2.4` | `5.8` |
| III | `maps:src:E.2.5` | `5.9` |
| III | `maps:src:E.2.6` | `5.10` |
| III | `maps:src:E.2.7` | `5.11` |
| III | `maps:src:E.2.8` | `5.12` |
| III | `maps:src:E.2.9` | `5.13` |
| III | `maps:src:F.1.1` | `6.1` |
| III | `maps:src:F.1.2` | `A.9` |
| III | `maps:src:F.1.3` | `A.10` |
| III | `maps:src:F.1.4` | `6.2` |
| III | `maps:src:F.2.1` | `6.3` |
| III | `maps:src:F.2.10` | `6.16` |
| III | `maps:src:F.2.11` | `6.17` |
| III | `maps:src:F.2.12` | `6.18` |
| III | `maps:src:F.2.13` | `6.19` |
| III | `maps:src:F.2.14` | `6.20` |
| III | `maps:src:F.2.15` | `6.13` |
| III | `maps:src:F.2.16` | `6.21` |
| III | `maps:src:F.2.17` | `6.22` |
| III | `maps:src:F.2.18` | `6.23` |
| III | `maps:src:F.2.19` | `6.24` |
| III | `maps:src:F.2.2` | `6.4` |
| III | `maps:src:F.2.20` | `6.25` |
| III | `maps:src:F.2.21` | `6.26` |
| III | `maps:src:F.2.22` | `6.27` |
| III | `maps:src:F.2.23` | `6.28` |
| III | `maps:src:F.2.24` | `6.29` |
| III | `maps:src:F.2.25` | `6.30` |
| III | `maps:src:F.2.26` | `6.31` |
| III | `maps:src:F.2.27` | `6.32` |
| III | `maps:src:F.2.28` | `6.33` |
| III | `maps:src:F.2.29` | `6.34` |
| III | `maps:src:F.2.3` | `6.5` |
| III | `maps:src:F.2.30` | `6.35` |
| III | `maps:src:F.2.31` | `6.36` |
| III | `maps:src:F.2.32` | `6.37` |
| III | `maps:src:F.2.33` | `6.38` |
| III | `maps:src:F.2.34` | `6.39` |
| III | `maps:src:F.2.35` | `6.40` |
| III | `maps:src:F.2.36` | `6.41` |
| III | `maps:src:F.2.37` | `6.42` |
| III | `maps:src:F.2.38` | `6.43` |
| III | `maps:src:F.2.39` | `6.44` |
| III | `maps:src:F.2.4` | `6.53` |
| III | `maps:src:F.2.5` | `6.8` |
| III | `maps:src:F.2.6` | `6.10` |
| III | `maps:src:F.2.7` | `6.12` |
| III | `maps:src:F.2.8` | `6.14` |
| III | `maps:src:F.2.9` | `6.15` |
| III | `maps:src:F.3.1` | `6.6` |
| III | `maps:src:F.3.10` | `6.50` |
| III | `maps:src:F.3.11` | `6.51` |
| III | `maps:src:F.3.2` | `6.7` |
| III | `maps:src:F.3.3` | `6.54` |
| III | `maps:src:F.3.4` | `6.11` |
| III | `maps:src:F.3.5` | `6.45` |
| III | `maps:src:F.3.6` | `6.46` |
| III | `maps:src:F.3.7` | `6.47` |
| III | `maps:src:F.3.8` | `6.48` |
| III | `maps:src:F.3.9` | `6.49` |
| III | `maps:src:F.4.1` | `6.52` |
| III | `mapsD:repair:50-weierstrass` | `226` |
| III | `mapsD:repair:canonical-matrices` | `224` |
| III | `mapsD:repair:cocycle-relation` | `223` |
| III | `mapsD:repair:collision-realization` | `B.1` |
| III | `mapsD:repair:free-peripherals` | `225` |
| III | `mapsD:repair:height-formula` | `227` |
| III | `mapsD:repair:modular-collisions` | `B` |
| III | `mapsIII:angle-forgotten-one-copy-null` | `9.43` |
| III | `mapsIII:carrier-extension-lemma` | `9.42` |
| III | `mapsIII:carrier-extension-section` | `9.8` |
| III | `mapsIII:carrier-radial-prerequisites` | `9.2` |
| III | `mapsIII:carrier-real-periods` | `9.4` |
| III | `mapsIII:carrier-three-complex-wedge` | `9.40` |
| III | `mapsaudit:almost-complex-homotopy` | `A.2` |
| III | `mapsaudit:finite-degree-three` | `9.41` |
| III | `mapsaudit:order-four-torsion-transgression` | `6.9` |
| III | `part:III:open` | `I` |
| III | `push:eq:C12-limiting-identification` | `2` |
| III | `push:eq:C12-u-flow` | `1` |
| III | `push:eq:C13-cusp-gauge` | `5` |
| III | `push:eq:C13-real-overlap` | `3` |
| III | `push:eq:C13-weighted-map` | `4` |
| III | `push:eq:c-spin-c` | `222` |
| III | `push:src:C.1.1` | `A.11` |
| III | `push:src:C.1.2` | `A.12` |
| III | `push:src:C.2.1` | `A.13` |
| III | `push:src:C.2.2` | `7.1` |
| III | `push:src:C.2.3` | `7.2` |
| III | `push:src:C.3.1` | `A.14` |
| III | `push:src:C.3.10` | `7.9` |
| III | `push:src:C.3.11` | `7.10` |
| III | `push:src:C.3.12` | `7.11` |
| III | `push:src:C.3.13` | `7.12` |
| III | `push:src:C.3.14` | `7.13` |
| III | `push:src:C.3.15` | `7.14` |
| III | `push:src:C.3.16` | `7.15` |
| III | `push:src:C.3.17` | `7.17` |
| III | `push:src:C.3.18` | `7.19` |
| III | `push:src:C.3.19` | `7.21` |
| III | `push:src:C.3.2` | `7.3` |
| III | `push:src:C.3.20` | `7.23` |
| III | `push:src:C.3.21` | `7.25` |
| III | `push:src:C.3.22` | `7.26` |
| III | `push:src:C.3.23` | `7.27` |
| III | `push:src:C.3.24` | `7.28` |
| III | `push:src:C.3.25` | `7.29` |
| III | `push:src:C.3.26` | `7.31` |
| III | `push:src:C.3.27` | `7.32` |
| III | `push:src:C.3.3` | `A.15` |
| III | `push:src:C.3.4` | `7.4` |
| III | `push:src:C.3.6` | `7.5` |
| III | `push:src:C.3.7` | `7.6` |
| III | `push:src:C.3.8` | `7.7` |
| III | `push:src:C.3.9` | `7.8` |
| III | `push:src:C.4.1` | `7.35` |
| III | `push:src:C.4.2` | `7.36` |
| III | `push:src:C.5.1` | `7.37` |
| III | `qa:III:coefficient-weight-0` | `AA.8` |
| III | `qa:III:coefficient-weight-1` | `AA.8` |
| III | `qa:III:coefficient-weight-2` | `AA.8` |
| III | `qa:III:coefficient-weight-3` | `AA.8` |
| III | `qa:III:coefficient-weight-4` | `AA.8` |
| III | `qa:III:layout:1` | `9.5` |
| III | `qa:III:layout:10` | `AI.11.6` |
| III | `qa:III:layout:11` | `9.3.1` |
| III | `qa:III:layout:12` | `2` |
| III | `qa:III:layout:13` | `AA.5` |
| III | `qa:III:layout:14` | `AC.9` |
| III | `qa:III:layout:2` | `B` |
| III | `qa:III:layout:3` | `B` |
| III | `qa:III:layout:4` | `B` |
| III | `qa:III:layout:5` | `D.1` |
| III | `qa:III:layout:6` | `K.1` |
| III | `qa:III:layout:7` | `W.7` |
| III | `qa:III:layout:8` | `AA.1` |
| III | `qa:III:layout:9` | `AA.7.2` |
| III | `sec:III:carriers` | `9` |
| III | `sec:III:conventions` | `1` |
| III | `sec:III:maps` | `2` |
| III | `wb:cusp-cone-A-definition` | `71` |
| III | `wb:cusp-cone-A-homology` | `79` |
| III | `wb:cusp-cone-A-smash-homology` | `80` |
| III | `wb:cusp-cone-A-smash-wedge` | `133` |
| III | `wb:cusp-cone-A-suspension` | `72` |
| III | `wb:cusp-cone-B-definition` | `81` |
| III | `wb:cusp-cone-B-homology` | `85` |
| III | `wb:cusp-cone-B-smash-homology` | `86` |
| III | `wb:cusp-cone-C-definition` | `90` |
| III | `wb:cusp-cone-C-homology` | `97` |
| III | `wb:cusp-cone-C-smash-homology` | `98` |
| III | `wb:cusp-cone-C-smash-wedge` | `134` |
| III | `wb:cusp-cone-D12-embedding` | `128` |
| III | `wb:cusp-cone-D12-slice` | `130` |
| III | `wb:cusp-cone-D24-embedding` | `129` |
| III | `wb:cusp-cone-D24-slice` | `131` |
| III | `wb:cusp-cone-E12-fibres` | `135` |
| III | `wb:cusp-cone-E24-fibres` | `136` |
| III | `wb:cusp-cone-M-H1` | `100` |
| III | `wb:cusp-cone-M-boundary` | `89` |
| III | `wb:cusp-cone-M-boundary-map` | `101` |
| III | `wb:cusp-cone-M-definition` | `88` |
| III | `wb:cusp-cone-S12-Borel-Serre-specialization` | `217` |
| III | `wb:cusp-cone-S12-P1-exact` | `218` |
| III | `wb:cusp-cone-S12-P1-lower-ideal` | `219` |
| III | `wb:cusp-cone-S12-Pontryagin-contradiction` | `221` |
| III | `wb:cusp-cone-S12-R4-limit` | `78` |
| III | `wb:cusp-cone-S12-S4-radial-map` | `111` |
| III | `wb:cusp-cone-S12-almost-complex-obstruction` | `A.1` |
| III | `wb:cusp-cone-S12-exact-collapsed-locus` | `113` |
| III | `wb:cusp-cone-S12-fibre-map` | `77` |
| III | `wb:cusp-cone-S12-lower-Chern-zero` | `215` |
| III | `wb:cusp-cone-S12-map` | `75` |
| III | `wb:cusp-cone-S12-onto-exact-ball` | `118` |
| III | `wb:cusp-cone-S12-route` | `9.8` |
| III | `wb:cusp-cone-S12-source` | `76` |
| III | `wb:cusp-cone-S12-sphere-map-null` | `9.16` |
| III | `wb:cusp-cone-S12-stable-trivialization` | `220` |
| III | `wb:cusp-cone-S12-top-Chern-two` | `216` |
| III | `wb:cusp-cone-S24-R4-limit` | `96` |
| III | `wb:cusp-cone-S24-S4-radial-map` | `112` |
| III | `wb:cusp-cone-S24-exact-collapsed-locus` | `114` |
| III | `wb:cusp-cone-S24-fibre-map` | `95` |
| III | `wb:cusp-cone-S24-local-fibre-map` | `84` |
| III | `wb:cusp-cone-S24-local-route` | `9.9` |
| III | `wb:cusp-cone-S24-map` | `93` |
| III | `wb:cusp-cone-S24-null-maps` | `120` |
| III | `wb:cusp-cone-S24-null-special-cases` | `121` |
| III | `wb:cusp-cone-S24-onto-exact-ball` | `119` |
| III | `wb:cusp-cone-S24-route` | `9.10` |
| III | `wb:cusp-cone-S24-sixfold-suspension` | `123` |
| III | `wb:cusp-cone-S24-smash-square-factorization` | `122` |
| III | `wb:cusp-cone-S24-source` | `94` |
| III | `wb:cusp-cone-S24-sphere-map-null` | `9.17` |
| III | `wb:cusp-cone-Seifert-meridians` | `99` |
| III | `wb:cusp-cone-U12-homeomorphism` | `126` |
| III | `wb:cusp-cone-U24-homeomorphism` | `127` |
| III | `wb:cusp-cone-ambient-collapse` | `102` |
| III | `wb:cusp-cone-angle-forgotten-sphere-carriers` | `9.15` |
| III | `wb:cusp-cone-carrier-local-homology` | `132` |
| III | `wb:cusp-cone-disc` | `64` |
| III | `wb:cusp-cone-distance-to-skeleton` | `117` |
| III | `wb:cusp-cone-exact-decompactification-space` | `9.23` |
| III | `wb:cusp-cone-explicit-carriers` | `9.21` |
| III | `wb:cusp-cone-fibre-H4-nonzero` | `109` |
| III | `wb:cusp-cone-finite-index-orbit` | `108` |
| III | `wb:cusp-cone-fourth-stable-stem` | `124` |
| III | `wb:cusp-cone-intrinsic-expansion` | `103` |
| III | `wb:cusp-cone-join-dimensions` | `106` |
| III | `wb:cusp-cone-kernel-contained` | `107` |
| III | `wb:cusp-cone-literal-R4-open-cells` | `9.18` |
| III | `wb:cusp-cone-metric-scope` | `9.12` |
| III | `wb:cusp-cone-monodromy-image` | `70` |
| III | `wb:cusp-cone-moving-S4-R4-limits` | `115` |
| III | `wb:cusp-cone-moving-S4-null-homotopy` | `9.19` |
| III | `wb:cusp-cone-native-descent` | `9.7` |
| III | `wb:cusp-cone-native-family-map` | `66` |
| III | `wb:cusp-cone-native-restriction` | `68` |
| III | `wb:cusp-cone-native-systole` | `69` |
| III | `wb:cusp-cone-obstructions` | `9.13` |
| III | `wb:cusp-cone-optimal-exponents` | `9.14` |
| III | `wb:cusp-cone-optimal-strengthening` | `9.3.1` |
| III | `wb:cusp-cone-pair-of-pants` | `87` |
| III | `wb:cusp-cone-products-not-spheres` | `105` |
| III | `wb:cusp-cone-q1` | `91` |
| III | `wb:cusp-cone-q1-cusp-formula` | `92` |
| III | `wb:cusp-cone-q1-local` | `82` |
| III | `wb:cusp-cone-q1-local-formula` | `83` |
| III | `wb:cusp-cone-q2` | `73` |
| III | `wb:cusp-cone-q2-formula` | `74` |
| III | `wb:cusp-cone-quotient-lattice` | `65` |
| III | `wb:cusp-cone-radial-isometry` | `67` |
| III | `wb:cusp-cone-rank-bound` | `104` |
| III | `wb:cusp-cone-section` | `9.3` |
| III | `wb:cusp-cone-sharp-global-R4-scope` | `9.24` |
| III | `wb:cusp-cone-sphere-map-homotopy-status` | `9.20` |
| III | `wb:cusp-cone-sphere-to-sphere-maps` | `110` |
| III | `wb:cusp-cone-target-homotopy-types` | `9.22` |
| III | `wb:cusp-cone-target-slice-embeddings` | `9.11` |
| III | `wb:cusp-cone-transported-skeleton-collapse` | `116` |
| III | `wb:cusp-cover-additive-fibre-map` | `26` |
| III | `wb:cusp-cover-base-change` | `7` |
| III | `wb:cusp-cover-base-changed-target` | `13` |
| III | `wb:cusp-cover-basechange-local-ring` | `21` |
| III | `wb:cusp-cover-completed-map` | `11` |
| III | `wb:cusp-cover-direct-ramification` | `12` |
| III | `wb:cusp-cover-double-fibre-length` | `25` |
| III | `wb:cusp-cover-equivariance-computation` | `20` |
| III | `wb:cusp-cover-extension-theorem` | `9.1` |
| III | `wb:cusp-cover-global-scope` | `9.3` |
| III | `wb:cusp-cover-invariant-ring` | `22` |
| III | `wb:cusp-cover-maximal-chart-map` | `17` |
| III | `wb:cusp-cover-monodromy-conjugacy` | `16` |
| III | `wb:cusp-cover-naive-action-failure` | `9.2` |
| III | `wb:cusp-cover-normalization-diagram` | `15` |
| III | `wb:cusp-cover-relative-factorization` | `14` |
| III | `wb:cusp-cover-section` | `9.1` |
| III | `wb:cusp-cover-source-action` | `9` |
| III | `wb:cusp-cover-source-factor` | `8` |
| III | `wb:cusp-cover-target-action` | `6` |
| III | `wb:cusp-cover-toric-power-map` | `10` |
| III | `wb:cusp-cover-triple-fibre-length` | `24` |
| III | `wb:cusp-null:eq:J` | `153` |
| III | `wb:cusp-null:eq:J0` | `155` |
| III | `wb:cusp-null:eq:P` | `156` |
| III | `wb:cusp-null:eq:action` | `143` |
| III | `wb:cusp-null:eq:actual-frame` | `154` |
| III | `wb:cusp-null:eq:bordism` | `158` |
| III | `wb:cusp-null:eq:chart` | `145` |
| III | `wb:cusp-null:eq:extended-frame` | `159` |
| III | `wb:cusp-null:eq:g` | `144` |
| III | `wb:cusp-null:eq:invertibility` | `147` |
| III | `wb:cusp-null:eq:moduli` | `146` |
| III | `wb:cusp-null:eq:nearby-moduli` | `152` |
| III | `wb:cusp-null:eq:periods` | `142` |
| III | `wb:cusp-null:eq:q` | `157` |
| III | `wb:cusp-null:eq:spatial-bound` | `151` |
| III | `wb:cusp-null:eq:straightening` | `149` |
| III | `wb:cusp-null:eq:torus` | `150` |
| III | `wb:cusp-null:thm` | `9.29` |
| III | `wb:cusp-s12-all-higher-smashes-null` | `9.26` |
| III | `wb:cusp-s12-carrier-homotopy` | `9.4` |
| III | `wb:cusp-s12-full-carrier-null` | `9.25` |
| III | `wb:cusp-s12-nullity-scope` | `9.28` |
| III | `wb:cusp-s12-one-copy-invariant` | `9.27` |
| III | `wb:cusp-s12-regular-inverse-image` | `141` |
| III | `wb:cusp-s12-sixfold-suspension-class` | `140` |
| III | `wb:cusp-s12-smash-factorization` | `137` |
| III | `wb:cusp-s12-three-stem-groups` | `139` |
| III | `wb:cusp-s12-toda-smash-formula` | `138` |
| III | `wb:cusp-spec-circle-dual-vector` | `54` |
| III | `wb:cusp-spec-cusp-kernel` | `51` |
| III | `wb:cusp-spec-cusp-nonextension-character` | `62` |
| III | `wb:cusp-spec-cusp-nonextension-chart` | `63` |
| III | `wb:cusp-spec-cusp-nonextension-position` | `61` |
| III | `wb:cusp-spec-doubled-local-quotient` | `40` |
| III | `wb:cusp-spec-finite-Seifert-target` | `43` |
| III | `wb:cusp-spec-finite-affine-action` | `41` |
| III | `wb:cusp-spec-finite-character-shift` | `42` |
| III | `wb:cusp-spec-finite-fibre-product-branches` | `60` |
| III | `wb:cusp-spec-finite-fourfold-normalization` | `44` |
| III | `wb:cusp-spec-finite-fourfold-target` | `45` |
| III | `wb:cusp-spec-finite-normalization-map` | `46` |
| III | `wb:cusp-spec-finite-overlap-identity` | `59` |
| III | `wb:cusp-spec-finite-target-cocycle` | `58` |
| III | `wb:cusp-spec-finite-target-conjugacy` | `57` |
| III | `wb:cusp-spec-four-circle-fibre` | `38` |
| III | `wb:cusp-spec-four-circle-limit` | `39` |
| III | `wb:cusp-spec-four-product-not-sphere` | `48` |
| III | `wb:cusp-spec-fourfold-circle-map` | `37` |
| III | `wb:cusp-spec-fourfold-fibre-product` | `36` |
| III | `wb:cusp-spec-full-inverse-transpose` | `29` |
| III | `wb:cusp-spec-global-circle-circumference` | `35` |
| III | `wb:cusp-spec-global-circle-coordinate` | `32` |
| III | `wb:cusp-spec-global-circle-map` | `30` |
| III | `wb:cusp-spec-global-circle-quotient` | `31` |
| III | `wb:cusp-spec-global-kernel-family` | `33` |
| III | `wb:cusp-spec-globalization-obstruction` | `9.6` |
| III | `wb:cusp-spec-holomorphic-errors` | `28` |
| III | `wb:cusp-spec-invariant-character-lattice` | `53` |
| III | `wb:cusp-spec-invariant-flag-calculation` | `52` |
| III | `wb:cusp-spec-native-quotient` | `9.5` |
| III | `wb:cusp-spec-no-finite-cover-matrix` | `55` |
| III | `wb:cusp-spec-no-finite-cover-orbit` | `56` |
| III | `wb:cusp-spec-product-not-sphere` | `47` |
| III | `wb:cusp-spec-radial-circle-character` | `34` |
| III | `wb:cusp-spec-radial-notation` | `27` |
| III | `wb:cusp-spec-smash-spheres` | `49` |
| III | `wb:cusp-spec-target-smash-map` | `50` |
| III | `wb:cusp_s12_carrier_homotopy:L567` | `9.30` |
| III | `wb:h24:ret:chart-lemma` | `9.36` |
| III | `wb:h24:ret:eq:A` | `183` |
| III | `wb:h24:ret:eq:A-homotopy` | `207` |
| III | `wb:h24:ret:eq:A-target` | `189` |
| III | `wb:h24:ret:eq:Arf` | `213` |
| III | `wb:h24:ret:eq:D` | `209` |
| III | `wb:h24:ret:eq:D-homotopy` | `211` |
| III | `wb:h24:ret:eq:F` | `196` |
| III | `wb:h24:ret:eq:Finv` | `197` |
| III | `wb:h24:ret:eq:H` | `191` |
| III | `wb:h24:ret:eq:LQ` | `202` |
| III | `wb:h24:ret:eq:M` | `198` |
| III | `wb:h24:ret:eq:actual-Arf` | `214` |
| III | `wb:h24:ret:eq:chosen-value` | `193` |
| III | `wb:h24:ret:eq:deck` | `184` |
| III | `wb:h24:ret:eq:derivative-on-M` | `201` |
| III | `wb:h24:ret:eq:differential-table` | `206` |
| III | `wb:h24:ret:eq:exact-u` | `199` |
| III | `wb:h24:ret:eq:four-cell` | `192` |
| III | `wb:h24:ret:eq:full-derivative` | `200` |
| III | `wb:h24:ret:eq:full-frame` | `210` |
| III | `wb:h24:ret:eq:invertibility` | `186` |
| III | `wb:h24:ret:eq:logx` | `185` |
| III | `wb:h24:ret:eq:native` | `187` |
| III | `wb:h24:ret:eq:normal-first` | `204` |
| III | `wb:h24:ret:eq:normal-u` | `205` |
| III | `wb:h24:ret:eq:original-periods` | `182` |
| III | `wb:h24:ret:eq:q2` | `190` |
| III | `wb:h24:ret:eq:quadratic` | `212` |
| III | `wb:h24:ret:eq:sign` | `208` |
| III | `wb:h24:ret:eq:tangents` | `203` |
| III | `wb:h24:ret:eq:two-skeleton` | `188` |
| III | `wb:h24:ret:eq:units` | `195` |
| III | `wb:h24:ret:eq:z-chart` | `194` |
| III | `wb:h24:ret:framing-proposition` | `9.38` |
| III | `wb:h24:ret:orientation-lemma` | `9.37` |
| III | `wb:h24:ret:q2-detected-quotient` | `9.39` |
| III | `wb:h24:ret:section` | `9.7` |
| III | `wb:sphere-metric-A-fixed-metric` | `164` |
| III | `wb:sphere-metric-A-slice-exact` | `166` |
| III | `wb:sphere-metric-BC-fixed-metric` | `165` |
| III | `wb:sphere-metric-BC-slice-exact` | `167` |
| III | `wb:sphere-metric-C-boundary-quotient-homeomorphism` | `180` |
| III | `wb:sphere-metric-C-smash-local-homology` | `179` |
| III | `wb:sphere-metric-Hausdorff-collapse` | `163` |
| III | `wb:sphere-metric-ambient-fixed-blowups` | `171` |
| III | `wb:sphere-metric-arbitrary-unrolling-ambient-bubbles` | `177` |
| III | `wb:sphere-metric-boundary-link-local-shift` | `181` |
| III | `wb:sphere-metric-fixed-realization` | `9.32` |
| III | `wb:sphere-metric-intrinsic-ambient-agreement` | `174` |
| III | `wb:sphere-metric-intrinsic-ambient-ball-comparison` | `175` |
| III | `wb:sphere-metric-limit-note` | `9.6` |
| III | `wb:sphere-metric-normalized-Q-limit` | `160` |
| III | `wb:sphere-metric-outward-shortcut-exclusion` | `178` |
| III | `wb:sphere-metric-scaling-trichotomy` | `9.33` |
| III | `wb:sphere-metric-scaling-trichotomy-result` | `172` |
| III | `wb:sphere-metric-slice-fixed-blowups` | `169` |
| III | `wb:sphere-metric-tangent-scope` | `9.35` |
| III | `wb:sphere-metric-uniform-collapse` | `9.31` |
| III | `wb:sphere-metric-unit-volume` | `9.34` |
| III | `wb:sphere-metric-vertex-distance` | `173` |
