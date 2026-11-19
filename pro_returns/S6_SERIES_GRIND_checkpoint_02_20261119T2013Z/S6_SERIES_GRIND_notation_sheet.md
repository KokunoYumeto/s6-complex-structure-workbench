# S6_SERIES_GRIND — common notation and exact transports

This sheet fixes the five-paper convention. The tag table gives the current paper, number, page and permanent destination for each statement. Section 6 of former Paper III is now in Paper V; former Paper VI is the second part of Paper II. Source labels preserve their identities through those moves.

## Current adapters

| Source convention | Exact transport | Receiving location |
|---|---|---|
| AC original cubic $y_0^2=4x_0^3-3Cx_0-D$ | $(x,y)=(-x_0,y_0/(2i))$ gives $y^2=x^3-3Cx/4+D/4$ | I, `I:weierstrass-comparison` |
| Arithmetic cubic to geometric cubic | $(X,Y)=(2x,-2\sqrt2y)$ gives $Y^2=X^3-3CX+2D$ | I, same statement |
| Original to geometric cubic | $(X,Y)=(-2x_0,i\sqrt2y_0)$ | I, same statement |
| Invariant differentials and lattices | Original-to-arithmetic pullback of $dx/(2y)$ is $-i\,dx_0/y_0$; geometric lattice is $-\Lambda_{\rm ar}/\sqrt2$ | I, same proof |
| Standard additive to multiplicative parameter | $w=\exp(-\pi i c)$, $u=w^2$, $q_2=iw/216$, $0<|w|<216$ | I |
| Standard beta splitting to DGKX splitting | $a=c+\delta$, $\delta=\beta^{\rm part}-\beta_0$; the descended holomorphic function on $\mathbb P^1$ is constant, and $\Omega_a=\Pi_c$ | I, `night:P5.7` |
| Physical point line and dual line | $U=M^{-1}$; for a Hermitian metric linear in its first entry, the unit-circle map $v\mapsto h(\,\cdot\,,v)$ has weight $-1$ | IV, `night:P3K.68` and its exact cap maps |
| Physical characteristic-number evaluation | $\mu(\lambda(k,\ell))=(4k-\ell)/672$; $(k,\ell)=(8,8)$ gives $+1/28$ | IV, `night:P3F.22` |
| Rank-six algebraic splitting | $\xi_b=\xi_{\rm original}-a_{\rm split}$; the full complex constant is retained and $\Im\xi_b>c_*$ | V, `night:P1.18` |

The symbol $M$ in the physical line convention refers to the stated line bundle. A local admissibility bound is written $M_{\rm adm}$ in comparisons; a fibre-product fourfold is $M_c$; the elliptic point line is $L_E=\mathcal O(P-O)$. Each of these is connected to its source notation by its displayed definition at the point of use. The ordinary period upper half-plane is $\mathbb H$; local source symbols $\mathcal H$ retain the explicitly defined object of their section.

The following detailed convention maps are retained from the attached mathematical dictionary. Current destinations are obtained from [the tag table](S6_SERIES_GRIND_tags.tsv); obsolete printed-number annotations have been removed. The source-to-label aliases are retained in the attached base and in the exact reference-resolution receipts.

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

Thus coherent restriction to a **full fibre** retains its nilpotent normal directions; restriction to $S_j$ means its reduction. In topological Euler localization the fibre is reduced because nilpotents do not change its underlying space. In higher multiplicity families, replace $3,4$ by the stated $3k,4l$, retaining the specified root characters. These conventions are fixed in FAMILY `sections/conventions.tex`, Paper I, `inv:A1.0`, and Paper II, `cdp:st:C2a`.

### 1.2. Positive meridians and analytic deck generators

A positive base meridian is counterclockwise in a holomorphic local coordinate. The analytic root-deck generator is clockwise:

$$
s_j(g_jz)=e^{-2\pi i/m_j}s_j(z),\qquad g_1g_2g_0=1.
$$

The lift of a positive base loop ends at the inverse deck translate. Identifying that endpoint with the starting fibre applies $g_j$; its homology monodromy is consequently $A_j$. The clockwise boundary of a deleted disc, used in a Stokes or collar calculation, has its own boundary orientation. The collar convention is recorded in Paper I, `inv:C3.2`. A matrix conjugacy alone changes neither of these loop orientations.

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

The exact transition is proved in Paper I, `inv:B1.0` and the family comparison statements. The symbol $Q_{\mathrm{mark}}$ here is unrelated to a quotient surface, the cotangent quotient $Q$, or the real torus $Q_T$.

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

where $H$ is parallel transport along that lifted path. On fibre homology $F_{n,c}$ acts by $I-nE$, $E=\widehat\delta\otimes\gamma$. This convention is used in Paper III, `fam:src:E.2.2` and Paper I, `push:src:C.3.5`.

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

This $D_{\mathrm{orig}}$ is a holomorphic residual function, not the real determinant $D_c$. The actual cusp logarithm is computed in Paper I, `mapsI:src:A.3.2`; direct subtraction of the displayed quadratic primitive gives the stated coherent origin. The scoped check is retained in `work/maps_audit/closing_origin_check.tex`. The scalar representative $t_B^4/(t_B-1)^3$ and the holomorphic cusp-unit representative of the closing translation differ by a deck period; they are compared in the complete closing-cocycle proof rather than equated as scalar functions.

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

Thus $12m_P$ is the probability measure in torsion equidistribution. The letter $L$ here denotes a scalar logarithm, while the fourfold construction uses $L$ for a line bundle. See Paper I, `ari:C.8.9` and Paper I, `ari:C.8.10`.

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

Thus $k$ is a constant, and $\chi$ is the Cayley coordinate. The separately named cusp constant $\beta_{\mathrm{cusp}}=\log(5+2\sqrt6)/(2\pi)$ is unrelated to $\beta_c$. The underlying exact definitions are in Paper I, `ari:C.8.14`.

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

The metric is the induced, **unscaled** Euclidean quotient metric. In particular $\operatorname{sys}(Q_T)\ge T-C$, and radius-$R$ balls are Euclidean once $T-C>4R$. A parameter-dependent rescaling would describe a different metric assertion. The full formulas and their proofs are Paper III, `mapsIII:carrier-real-periods` and Paper III, `wb:cusp-spec-native-quotient`.

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
Paper III, `wb:cusp-spec-globalization-obstruction`.

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
Paper III, `wb:cusp-spec-global-circle-quotient` and
Paper III, `wb:cusp-spec-global-circle-circumference`.

The angle-forgotten rank-two carrier has the local expression $[r,c(\alpha)]$, where $c$ collapses the coordinate one-skeleton of the quotient two-torus. The circle carrier is $[r,\chi_\gamma^{\mathrm{quot}}(\alpha)]$. Their completed maps and the retained-angle collapse have different targets and boundary identifications. The complete new extension proof makes both angle-forgotten one-copy carriers based nullhomotopic; it does not extend the literal flat character pointwise across the cusp. The retained-angle map $H:X\to S^4$ keeps the base-angle direction and represents the nonzero stable second-stem class. Its source theorem is consolidated at Paper III, `maps:src:B.3.1`. These maps are never identified merely because they use the same torus or the same radial coordinate.

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

The maps $\delta_A:H^0(T_{\Omega}\otimes A)\to H^1(N^*\otimes A)$ and $\partial_A:H^0(Q_{\Omega}\otimes A)\to H^1(K_{\Omega}\otimes A)$ are connecting maps for these different exact sequences. Here $A$ is an invertible analytic sheaf on $S$. A vanishing for the torsion-free quotient does not by itself remove the torsion kernel. The canonical criterion is Paper II, `cdp:st:A.1.1`.

For a local reduced equation $F$, the Jacobian ideal is $\mathcal J=(F_{x_0},\ldots,F_{x_n})\subset\mathcal O_S$. Its inverse is the fractional ideal

$$
\mathcal J^{-1}=\{q\in\mathcal M_S:q\mathcal J\subset\mathcal O_S\},
$$

inside the total quotient sheaf, not an inverse line bundle asserted to be locally free. The identifications are $K_{\Omega}=N^*\otimes\mathcal J^{-1}$ and $T_{\Omega}=N^*\otimes(\mathcal J^{-1}/\mathcal O_S)$; see Paper II, `cdp:st:A.2.1`.

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

The inverse-Jacobian simple-pole statements for cusp, tacnode and ordinary-triple transverse types use respectively $x^2-y^3$, $x^2-y^4$, and $xy(x-y)$. Under the genus-one and constant-type hypotheses of Paper II, `cdp:st:C2d`, normalization along the double curve has one branch, an étale two-branch cover, or an étale three-branch cover. Those covers need not split globally. In the tacnode jet the invariant numerator is $ac-b^2/4$, not an expression divided by the leading quadratic coefficient. The inverse-Jacobian convention is Paper II, `cdp:st:A.2.2`.

### 5.3. Euler numbers, ranks and analytic categories

For a proper surjective holomorphic map $g:Y\to C$ from a connected compact complex manifold of dimension three to a compact Riemann surface, with connected general fibre a complex two-torus, let $\Sigma$ be a finite set containing the critical values. Then $e(Y)=\sum_{c\in\Sigma}e((Y_c)_{\mathrm{red}})$. In the stipulated unimodular periodic rank-two toric model, the quotient triangulation has $V-E+F=0$, $3F=2E$, and $e(S)=F=2V$; rank-one elliptic-ruled models have Euler number zero. These hypotheses do not imply that every singular fibre in an unrestricted torus fibration has nonnegative Euler number. The exact theorem, counterexample and model class are Paper II, `cdp:st:C2a`, Paper II, `cdp:st:C2b`, and Paper II, `cdp:st:C2c`.

Throughout Paper II, a proper analytic map, an algebraic morphism and a formal degeneration are used with their stated categories. The analytic realization and compactness arguments printed for the toric models supply the comparison when a source theorem begins over a complete discrete valuation ring. A numerical divisor class, a holomorphic line bundle, a topologically trivial line bundle and an element of $\operatorname{Pic}^0$ remain different data.

## 6. Papers III and V: marked lattices, chains and normal orientations

### 6.1. Rank-six transpose and inverse conventions

The matrices printed as $A,B$ in the non-self-dual candidate Paper III, `maps:src:F.2.5` are used through

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

Its additive notation on the covering cylinder is $m\theta-v$. Sweeping a fibre loop $\lambda$ produces the norm coordinate $N_m\lambda$ and fibre bivector $-\lambda\wedge v$; the minus sign is the marked normal-orientation convention. The affine generator contributes the torus of the commuting words $c$ and $c^m v^{-1}$. These are the full integral Thom columns of Paper III, `maps:src:D.2.29`, including torsion cycles.

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

This short differential does not replace the full projection or boundary inclusion: their higher finite perturbation terms remain in the certificate. The finite-cap mapping-torus convention uses $M_i$, while the complement right-action convention uses $M_i^{-1}$; the recorded comparison maps connect them. The complete construction is Paper III, `maps:src:F.2.35`.

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

It is an integral equation. The height-integral condition, corrected punctured monodromy and additional fully filled examples have their separate statements; no unsupplied original cap is inferred from the existence of a corrected line bundle. See Paper III, `maps:src:D.2.50` and Paper III, `maps:src:D.2.52`.

## 7. Stable framings, spin structures and seven-dimensional invariants

### 7.1. Orientation and Pontryagin–Thom convention

Complex manifolds carry their complex orientation. A boundary uses the outward-normal-first convention. In a Pontryagin–Thom comparison the ordered normal frame precedes the tangent frame; outward stabilization is retained. A constant permutation of frame vectors is corrected once so the full frame has the stipulated orientation. Comparing a chart frame with the sphere frame is done on the actual contractible chart, not by assuming the whole complex tangent bundle is trivial.

At the fixed sphere, conjugating one complex normal coordinate reverses the real normal orientation. The surgery comparison simultaneously reverses the model $S^2$ orientation so that the ambient six-dimensional orientation is preserved; see Paper III, `maps:src:D.2.14` and the explicit local tubular model in that proof. Normal-frame changes and homology basis changes are different operations.

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

The map $\eta_n:S^{n+1}\to S^n$ is the $(n-2)$-fold suspension of the complex Hopf map. The Lie-framed circle represents stable $\eta$, the Lie-framed two-torus represents $\eta^2\ne0\in\pi_2^{\mathrm S}=\mathbb Z/2$, and the Lie-framed three-torus represents $\eta^3=12\nu$. Consequently the order-two unstable class in the Engel-map calculation is $6\nu'$, with stable class $12\nu$. Source or target orientation reversal does not change these order-two classes. The real Adams invariant used here is not silently replaced by the complex Adams invariant. See Paper III, `maps:src:B.1.2` and Paper III, `maps:src:B.3.1`; the exact original reference scopes are recorded under `Pontryagin1950Root`, `Pontryagin1955Root`, `Johnson1980Root`, `DebrayGunningham2018Root`, and `Hatcher2002`.

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

The published Crowley–Nordström convention is converted by dividing its invariant by $28$ and substituting $\widehat p=(p_1+z^2)/2$, with its original hypotheses retained. Boundary orientation reversal negates $\mu_{EK}$. The exact normalizations and mapping-torus comparison are Paper III, `push:src:C.1.1`, Paper III, `push:src:C.1.2`, and Paper III, `push:src:C.2.1`. A framing integer, an orbit-knot integer and this residue class are related only by the explicitly proved comparison; equivariance alone does not determine the residue.


## Current generated concordance

The complete result placement is in [the inventory](S6_SERIES_GRIND_inventory.csv). The exact numerical-to-label migration is in `analysis/numeric_reference_resolution.json`; aliases and immutable targets are in `analysis/label_tags.json` and `S6_SERIES_GRIND_tags.tsv`. These files are regenerated from current TeX labels and compiled auxiliary records.
