# Mathematical correction — 8 September 2026

This corrected edition supersedes the earlier draft at this path. It is extracted from the complete Section 13 of extensive_quantum_blocking.tex/.md. The full proof, source inputs, boundary derivation and scope are in [FABEL_TENSOR_TRANSFER.md](FABEL_TENSOR_TRANSFER.md). Equation numbers refer to the cumulative manuscript. No four-dimensional mass-gap disproof is claimed.

## Transport conventions and the vacuum-moment correction

For the column-section connection $d+\mathcal A$, ordinary parallel transport along an oriented edge $e:[0,a]\to\mathbb R^3$ solves 

$$
P_e'(s)=-\mathcal A(e(s))(\dot e(s))P_e(s),\qquad P_e(0)=I.
$$

 Its gauge transform is $P_e^h(s)=h(e(s))^{-1}P_e(s)h(e(0))$. Differentiating this formula verifies the transformed ODE and its initial value; uniqueness gives the assertion. The links in Section 1 have the opposite endpoint convention and are therefore *inverse* transports: 

$$
\qquad\text{(94)}
 U_e=P_e(a)^{-1},\quad
 U_e^h=h(e(0))^{-1}U_eh(e(a)),\quad U'(s)=U(s)\mathcal A(e(s))(\dot e(s)).
$$

 Inverses and concatenations follow by multiplication of the corresponding transport maps. Thus this is an exact gauge-equivariant map for arbitrary noncommuting connection components. It is not a global inverse from finite links to connections.

The Cartan specialization $\mathcal A_i=\lambda u_iT$, $T=-i\sigma_3/2$, has 

$$
U_e=\exp\left(\lambda T\int_e u\cdot dx\right),\qquad
 U_p=\exp(\vartheta_pT),\quad
 \vartheta_p=\lambda\oint_{\partial p}u\cdot dx .
$$

 With positively oriented $(i,j)$ faces, Stokes' theorem gives $\vartheta_p=\lambda\int_p(\partial_i u_j-\partial_j u_i)\,dx^i dx^j$. For a fixed smooth field on a compact region it equals $a^2\lambda(\partial_i u_j-\partial_j u_i)+O(a^3)$. In the general non-Abelian case the four edge expansions to second order give $U_p=I+a^2F_{ij}+O(a^3)$: the differentiated terms are $\partial_i\mathcal A_j-\partial_j\mathcal A_i$ and the four products give $[\mathcal A_i,\mathcal A_j]$, with this positive sign. For uniform $C^2$ bounds the remainder is uniform on that compact region. As $\operatorname{tr}e^{\vartheta T}=2\cos(\vartheta/2)$, the exact magnetic value is 

$$
\qquad\text{(95)}
 b(2-W_p)=\frac{2-2\cos(\vartheta_p/2)}{2g^2a}
       =\frac{\vartheta_p^2}{8g^2a}
          +O_g(\vartheta_p^4/a).
$$

 For fixed $g,\lambda$ and a fixed smooth field, summation on a regular mesh of a bounded region yields $\lambda^2(8g^2)^{-1}\int|\operatorname{curl}u|^2dx$. This follows by a Riemann sum; each leading cell term is $a^3$ times the displayed density and each uniform cell error is $O(a^4)$. Pointwise curvature growth alone does not imply growth of this integral: the volume of the concentrating region must also be accounted for.

In Lorentzian coordinates $X^0=ct,X^i=x^i$, the same Cartan field with $\mathcal A_0=0$ has the complete conserved current 

$$
\begin{aligned}
 j_0&=0,\\
 j_i&=\frac{\lambda}{g^2}
       (\Delta u_i-c^{-2}\partial_t^2u_i)T\\
 &=\frac{\lambda}{g^2}\left[
 \Delta u_i-c^{-2}\left(\nu\Delta w_i
 -\sum_jw_j\partial_ju_i-\sum_ju_j\partial_jw_i
 -\partial_i\partial_tp+\partial_tf_i\right)\right]T,\qquad w_i=\partial_tu_i.
\end{aligned}
$$

 This is obtained by differentiating the original Navier--Stokes equation, not by changing its viscosity or force. $D^\nu j_\nu=0$ follows from incompressibility and the common Cartan factor. The field solves that sourced classical equation. It can be used as data for a quantum trial state without claiming it solves source-free Yang--Mills. Proving source-free classical dynamics is not a prerequisite for defining a trial state; its physical Hilbert and spectral properties must instead be proved.

There is a separate important correction concerning Wilson observables. Evaluating $W_C$ at the links of a background gives a number $W_C(U[\mathcal A])$. The functional $W_C(U)$ on the full configuration space has no dependence on the chosen background until an additional prescription supplies it. The generic centered state $\psi(W_C-\mu W_C)$ is physical and nonzero, but naming a background does not make it a background-dependent state map. Moreover $r_C=\mu(W_C^2)$ is the actual quantum second moment. It is not $W_C(U[\mathcal A])^2$.

Keep the exact bound from Section 7, $\alpha\le r_C\le4-3\alpha$, with $\alpha=(9\,12^{16/g^4})^{-1}>0$. Then 

$$
\qquad\text{(96)}
 \frac{3\alpha}{4}\kappa\ell\le
 a_C=\kappa\ell(1-r_C/4)
 \le(1-\alpha/4)\kappa\ell .
$$

 For physical perimeter $P_C=a\ell$ this bounds the *bare* loop numerator between the displayed constants times $2g^2P_C/a^2$ at fixed $g$; it does not give asymptotic ratio one. The reconstructed numerator and norm remain $a_C-M_1(0)$ and $d_C+M_2(0)$. The lower bound $\Delta_{\rm sc}$ for these reconstructed states is used only for $\xi\le1/49152$. In a spatial continuum path $a\downarrow0$, $\kappa\to0$ would imply $g^2=(a/2)\kappa\to0$ and thus $\xi\to\infty$. Without $a\downarrow0$ the latter implication is not valid.

## The full weighted local-energy operator

For arbitrary real weights $f=(f_e)_{e\in\mathsf E_L}$ define 

$$
\qquad\text{(97)}
 f_p=\frac14\sum_{e\in\partial p}f_e,\quad
 V_p=b(2-W_p),\quad
 D_f=\kappa\sum_ef_eE_e+\sum_pf_pV_p,\quad
 \Xi_f=(D_f-\langle\psi,D_f\psi\rangle)\psi .
$$

 All sums include the boundary edges and faces. The electric-only operator $\sum f_eE_e$ is a different operator. On a Peter--Weyl product sector with edge spins $j_e$, the signed electric sum in $D_f$ has eigenvalue $\kappa\sum_ef_ej_e(j_e+1)$. Its domain consists of square-summable coefficients with the squares of these eigenvalues as weights. Addition of the bounded real magnetic multiplication preserves that self-adjoint domain. Smooth functions lie in the domain, and $D_f$ maps smooth functions to smooth functions. In particular $\Xi_f$ is smooth and belongs to every power domain of $H$. Gauge invariance of each link Casimir and each face trace gives gauge invariance of $\Xi_f$. Its definition proves $\langle\psi,\Xi_f\rangle=0$ with no rescaling.

Put $\mathcal E=E_0$ and $\mathcal A=H-\mathcal E$. The product rule, including both derivative terms, gives 

$$
\begin{aligned}
 [E_e,V_p]F&=-\sum_a\bigl[(X_{e,a}^2V_p)F+
                           2(X_{e,a}V_p)X_{e,a}F\bigr],\qquad\text{(98)}\\
 [H,D_f]&=\kappa\sum_p\sum_{e\in\partial p}(f_p-f_e)[E_e,V_p].
 \qquad\text{(99)}
\end{aligned}
$$

 The first expression vanishes when $e\notin\partial p$. The second identity follows by expanding the commutator: electric terms commute with electric terms, magnetic multiplications commute, and the two remaining electric--magnetic sums have the stated coefficient. It proves 

$$
\mathcal A\Xi_f=[H,D_f]\psi,\qquad
 q_{\mathcal A}[\Xi_f]=\tfrac12
 \langle\psi,[D_f,[H,D_f]]\psi\rangle .
$$

 For the raw positive measure $\nu_f(B)=\|1_B(\mathcal A)\Xi_f\|^2$, $B\subset(0,\infty)$, spectral integration yields 

$$
\qquad\text{(100)}
 \|\Xi_f\|^2=\int d\nu_f,\quad
 q_{\mathcal A}[\Xi_f]=\int E\,d\nu_f,\quad
 \|[H,D_f]\psi\|^2=\int E^2d\nu_f .
$$

 All moments are finite by smoothness. For a constant $f_e=c_0$, $D_f=c_0H$, so its expectation is $c_0\mathcal E$ and $\Xi_f=0$. This is an exact cancellation, not a zero-energy nonzero state.

## A non-affine map using every entry of the material tensor

Set $K_\tau=C_\tau C_\tau^{\mathsf T}$ and keep all six independent entries. For any real symmetric matrix $S$ define 

$$
\qquad\text{(103)}
 f_S(e)=m(e)^{\mathsf T}S\,m(e),\qquad
 \mathfrak M_{L,a,g}(S)=\Xi_{f_S}\in
 C^\infty(\mathcal Q)^{\mathcal G}\cap\{\psi\}^{\perp}.
$$

 This is a linear, typed map on the six-dimensional real matrix space. It does not change the Hamiltonian metric: $S$ is the spatial weight of the observable $D_f$, not a replacement kinetic tensor in $H$. Using physical midpoints $a\,m(e)$ multiplies $f_S$ and $\Xi_{f_S}$ by $a^2$, and every raw spectral measure by $a^4$. Those factors remain present if physical midpoint units are chosen.

Use the three unchanged seed functions 

$$
f_0=m_1^2+m_2^2+m_3^2,\quad
 f_{\rm d}=m_1^2-m_2^2,\quad f_{\rm o}=2m_1m_2,
$$

 and write $\nu_0,\nu_{\rm d},\nu_{\rm o}$ for their actual centered-state spectral measures. These are positive measures of the full interacting Hamiltonian, not free-channel approximations.

### Theorem 13.1.

For every fixed $L\ge2$, $a,g>0$, every real symmetric $S$ and every Borel $B\subset(0,\infty)$, 

$$
\begin{aligned}
 \nu_{f_S}(B)&=w_0(S)\nu_0(B)+w_{\rm d}(S)\nu_{\rm d}(B)
                         +w_{\rm o}(S)\nu_{\rm o}(B),\qquad\text{(104)}\\
 w_0(S)&=(\operatorname{tr}S)^2/9,\\
 w_{\rm d}(S)&=\tfrac12\sum_{i=1}^3(S_{ii}-\operatorname{tr}S/3)^2,\quad
 w_{\rm o}(S)=\sum_{i<j}S_{ij}^2.
\end{aligned}
$$

 The same identity holds after integration against $1,E,E^2$ and $e^{-sE}$ for $s\ge0$, retaining the corresponding raw norms, excitation energies, current norms, and time correlations.

### Proof.

Put $u_i=\Xi_{m_i^2}$ and $v_{ij}=\Xi_{2m_im_j}$. A coordinate reflection fixes each $u_i$ and negates $v_{ij}$ if it reflects just one of $i,j$. Thus every spectral inner product between a $u$ and a $v$ vanishes. For two different off-diagonal pairs there is a reflection negating exactly one, so their cross term also vanishes. Permutations give the same diagonal spectral norm, equal to $\nu_{\rm o}(B)$, for the three $v_{ij}$.

For the three $u_i$, permutations equate diagonal elements, denoted $d(B)$, and equate off-diagonal elements, denoted $h(B)$. A permutation exchanging two indices shows that $h(B)$ equals its complex conjugate; it is real. The diagonal contribution for $s_i=S_{ii}$ is 

$$
d\sum_i s_i^2+2h\sum_{i<j}s_is_j
 =(d-h)\sum_i(s_i-\bar s)^2+(d+2h)(\operatorname{tr}S)^2/3,
 \qquad\bar s=\operatorname{tr}S/3.
$$

 But $\nu_0=3d+6h$ and $\nu_{\rm d}=2(d-h)$ by the definitions of the unchanged seed states. Substitution gives (104). All identities are identities of finite positive measures. Integration against the listed nonnegative functions is justified by monotone convergence; smoothness makes the moments finite.

Let $\eta=(1/4,3/8,-9/4)^{\mathsf T}$. Every entry of (102) yields $z^3C_\tau\to\eta e_3^{\mathsf T}$ and hence 

$$
z^6K_\tau\longrightarrow S_*=\eta\eta^{\mathsf T}
 =\frac1{64}\begin{pmatrix}4&6&-36\\6&9&-54\\-36&-54&324\end{pmatrix}.
$$

 Consequently the full nonlinear spatial profile $m^{\mathsf T}K_\tau m$ has the following exact endpoint: 

$$
\qquad\text{(105)}
 z^{12}\nu_{f_{K_\tau}}\longrightarrow
 \frac{113569}{36864}\nu_0+
 \frac{100825}{12288}\nu_{\rm d}+
 \frac{531}{512}\nu_{\rm o}.
$$

 This is convergence in total variation at each fixed regulator and convergence of the first two moments. To prove it, note that each $w_j$ is homogeneous of degree two and continuous in $S$, and apply (104). The total variation of the difference is bounded by the sum of the three coefficient errors times the finite masses of the seed measures; the moment versions use their finite moments. The constants follow by substituting $S_{*,ii}=4/64,9/64,324/64$ and $S_{*,12}=6/64,S_{*,13}=-36/64,S_{*,23}=-54/64$. Equivalently $z^6\Xi_{f_{K_\tau}}\to\Xi_{f_{S_*}}$ in every Sobolev norm at a fixed regulator, by the linear six-state expression. These displayed rescaled limits record the growth of the raw state; the state itself has not been divided by its norm.

All three coefficients in (105) are positive. For sufficiently small $z>0$, each $w_j(K_\tau)$ is positive as well. Then the positive-energy support of $\nu_{f_{K_\tau}}$ equals the union of the supports of the nonzero seed measures: a Borel neighborhood has zero mass in the sum precisely when it has zero mass in each seed. Write $d_j=\int d\nu_j$, $n_j=\int E\,d\nu_j$. If at least one $d_j$ is nonzero, the limiting quotient is exactly 

$$
\qquad\text{(106)}
 \lim_{\tau\uparrow1/8}
 \frac{q_{\mathcal A}[\Xi_{f_{K_\tau}}]}{\|\Xi_{f_{K_\tau}}\|^2}
 =
 \frac{\frac{113569}{36864}n_0+
       \frac{100825}{12288}n_{\rm d}+\frac{531}{512}n_{\rm o}}
      {\frac{113569}{36864}d_0+
       \frac{100825}{12288}d_{\rm d}+\frac{531}{512}d_{\rm o}} .
$$

 This is an evaluated relation between actual moments, not an estimate that any unknown moment is small. If all $d_j=0$, every state in this quadratic family is zero. The next calculation proves that this latter case does not occur for sufficiently small positive $\xi$ on any fixed box.

