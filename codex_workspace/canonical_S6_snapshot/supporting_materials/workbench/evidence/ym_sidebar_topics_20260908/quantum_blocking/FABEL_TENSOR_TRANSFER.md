# Material-tensor transfer into interacting local-energy states

Complete section of the cumulative manuscript, 9 September 2026.

 

This section retains the original Wilson Hamiltonian, vacuum, gauge action, spacing and coupling from Section 1. It constructs a particular observable map from the full Fabel material tensor. No equality between fluid evolution and quantum Hamiltonian evolution is asserted. The map and its exact spectral measures are calculated below; the remaining infinite-volume spectral question is not replaced by the value of a coordinate.

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

## Coordinate-level cubic symmetries and the full covector map

Write $m(e)=n+\mathbf e_i/2$ for edge midpoints. A signed permutation matrix $R$ maps the vertex box to itself. If $R\mathbf e_i=\epsilon\mathbf e_j$, then the positive image edge of $e=(n,i)$ is $(Rn,j)$ for $\epsilon=1$, and $(Rn-\mathbf e_j,j)$ for $\epsilon=-1$. Define $\Gamma_R(U)$ at this image edge to be $U_e^\epsilon$. The inverse is $\Gamma_{R^{-1}}$; composing the signs and endpoints verifies both inverse compositions. Every midpoint is mapped to $Rm(e)$. Each face becomes a face, possibly with its orientation reversed. Its SU(2) trace is unchanged under reversal. Inversion of a group variable is Haar preserving and takes the left Casimir to the equal right Casimir, since the metric is bi-invariant. Thus the pullback unitary $\mathsf T_RF=F\circ\Gamma_R^{-1}$ preserves $H$, $H^1$ and $H^2$ and intertwines the full gauge actions by $h'(Rn)=h(n)$. Uniqueness of the positive unit vacuum gives $\mathsf T_R\psi=\psi$. For weights transported by $f_R(e')=f(e)$ it follows that $\mathsf T_RD_f\mathsf T_R^{-1}=D_{f_R}$ and $\mathsf T_R\Xi_f=\Xi_{f_R}$. Spectral projections of $\mathcal A$ commute with $\mathsf T_R$.

Let $\Xi_r=\Xi_{m_r}$. Reflection in coordinate $r$ changes $\Xi_r$ to $-\Xi_r$ and fixes $\Xi_s$ for $s\ne r$; permutations exchange the three. Consequently, for every real $t\in\mathbb R^3$ and $c_0\in\mathbb R$, 

$$
\qquad\text{(101)}
 \Xi_{c_0+t\cdot m}=\sum_rt_r\Xi_r,\quad
 \langle D_{c_0+t\cdot m}\rangle=c_0\mathcal E,\quad
 \nu_{c_0+t\cdot m}(B)=|t|^2\nu_{m_1}(B).
$$

 Indeed a reflection negates each off-diagonal matrix element $\langle\Xi_r,1_B(\mathcal A)\Xi_s\rangle$ while leaving it invariant; it is therefore zero. Permutations equate the diagonal elements. This proof applies at every positive coupling, including when a state or a measure vanishes.

For the retained Fabel time parameter $z=\sqrt{1-8\tau}>0$, $\tau=(1-z^2)/8$, the full inverse material derivative is computed from the unchanged real polynomial map 

$$
\begin{aligned}
 F_1(x,y,w)&=(1+xy)^3w+y^2(1+xy)(4+3xy),\\
 F_2(x,y,w)&=y+3x(1+xy)^2w+3xy^2(4+3xy),\\
 F_3(x,y,w)&=2x-3x^2y-x^3w .
\end{aligned}
$$

 Here $w$ denotes the original third spatial coordinate, not time. Expanding the three-by-three determinant of its differentiated matrix gives $\det DF=-2$. At the retained points the full matrices are 

$$
J_0=\begin{pmatrix}-9/16&-3/8&-1/8\\3/8&25/4&3/4\\-17/2&-3&-1\end{pmatrix},
 \quad
 J_\gamma=\begin{pmatrix}
 -9z^3/16&-3z/8&-1/8\\3z^2/8&25/4&3/(4z)\\-17/2&-3/z^2&-1/z^3
 \end{pmatrix}.
$$

 Direct matrix multiplication gives 

$$
\qquad\text{(102)}
 C_\tau=
 \begin{pmatrix}
 (17-9z^3)/8&(3-3z^3)/(4z^2)&(1-z^3)/(4z^3)\\
 (51-24z^2-27z^3)/16&(9+8z^2-9z^3)/(8z^2)&(3-3z^3)/(8z^3)\\
 (-153+36z^2+117z^3)/8&(-27-12z^2+39z^3)/(4z^2)&(-9+13z^3)/(4z^3)
 \end{pmatrix}.
$$

 It is $J_0^{-1}B_\tau^{-1}J_\gamma$, where $J=DF$ for the original polynomials and 

$$
q_0=(1,-3/2,13/2),\quad
\gamma=(z^{-1},-3z/2,13z^2/2),\quad B_\tau=I+6\tau E_{23}.
$$

 The factorization gives the inverse $A_\tau=J_\gamma^{-1}B_\tau J_0$ and determinant one. The source matrix entries are reproduced and independently rederived by the companion checker from $F$.

The covector $\zeta_\tau=C_\tau^{\mathsf T}e_3$ has the three entries in the last row of (102). Choose the explicit affine weight $f_\tau(e)=\zeta_\tau\cdot m(e)$. Then 

$$
\nu_{f_\tau}(B)=Q(z)\nu_{m_1}(B),
$$

 where the entire, unmodified scalar is 

$$
\begin{aligned}
 Q(z)={}&\frac{(-153+36z^2+117z^3)^2}{64}
 +\frac{(-27-12z^2+39z^3)^2}{16z^4}
 +\frac{(-9+13z^3)^2}{16z^6},\\
 &\lim_{z\downarrow0}z^6Q(z)=81/16 .
\end{aligned}
$$

 Thus the full covector, with its changing direction, is realized by this specified parameter-to-state map. Its raw norm, energy, and second spectral moment all have the same factor $Q(z)$; their ratio does not depend on $\tau$ whenever the state is nonzero. This is not an identification of the Fabel cotangent space with the whole quantum state space.

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

## The first surviving state and exact open-boundary coefficients

The full local-energy source proof is retained unchanged as . We reproduce the coefficient argument needed here. Set $H_0=\sum_eE_e$ and $\mathcal W=\sum_pW_p$. On a fixed box, $\|\mathcal W\|_\infty=2M$ and the nonconstant free gap is $3/4$. The circle $|\zeta|=3/8$ has free resolvent norm at most $8/3$, so the Neumann series for $H_0-\xi\mathcal W$ converges for $|\xi|<3/(16M)$. The simple ground projection persists there. For real $\xi$ near zero its positive unit vacuum is real analytic in each Sobolev space, by the eigen-equation and elliptic regularity. Keep its unit-vacuum scalar: 

$$
\begin{aligned}
 \psi_\xi&=1+\xi\mathcal W/3+\xi^2 B+O_{H^k,L}(\xi^3),\\
 H_0B&=(\mathcal W^2-M)/3,\qquad \int B=-M/18.
\end{aligned}
$$

 For two faces sharing one edge, decompose $W_pW_q=P_{pq,0}+P_{pq,1}$ by Haar averaging that edge. The first term is one half the six-edge boundary trace, by the fundamental matrix-element identity $\int U_{ij}\overline U_{kl}
=\delta_{ik}\delta_{jl}/2$. The shared-edge spins are zero and one, and all six outer spins are $1/2$. Hence their free energies are $9/2,13/2$ and their squared norms are $1/4,3/4$. Repeated faces give $W_p^2-1$ of energy $8$; edge-disjoint distinct faces give $W_pW_q$ of energy $6$. All unordered pairs are thus retained in 

$$
B=-M/18+\sum_p\frac{W_p^2-1}{24}
  +\sum_{\partial p\cap\partial q=\varnothing}\frac{W_pW_q}{9}
  +\sum_{|\partial p\cap\partial q|=1}
       \left(\frac4{27}P_{pq,0}+\frac4{39}P_{pq,1}\right).
$$

 Inserting this expression in (97), the first-order electric term equals the first-order magnetic term because $E_f(\mathcal W/3)=\sum_pf_pW_p$, where $E_f=\sum_ef_eE_e$. Centering subtracts the expectation of the same vacuum. Repeated and edge-disjoint face pairs cancel at order two. For an adjacent pair with shared edge $e$, the weighted electric eigenvalues are $3(f_p+f_q)-3f_e/2$ and $3(f_p+f_q)+f_e/2$. The remaining second-order state is therefore 

$$
\begin{aligned}
 \Xi_f&=\kappa\xi^2 Z_f+O_{H^k,L,f}(\kappa\xi^3),\\
 Z_f&=\sum_{\{p,q\}\ {\rm adjacent}}\delta_{pq}(f)
         (P_{pq,0}/9-P_{pq,1}/39),\quad
 \delta_{pq}(f)=f_p+f_q-2f_e. \qquad\text{(107)}
\end{aligned}
$$

 Different adjacent pairs have different six-edge outer boundaries. Otherwise their symmetric difference would be a nonempty mod-two two-cycle with at most four elementary faces. A face in that cycle needs four distinct other faces to cancel its four edges (two distinct square faces share at most one edge), a contradiction. Central sign reversal of a boundary link present in only one pair therefore kills the cross integral. It also kills the cross integral with $H_0$ inserted. Both spin channels remain orthogonal. Thus 

$$
\begin{aligned}
 \|Z_f\|^2&=\frac{49}{13689}\mathcal D_f,&
 \langle Z_f,H_0Z_f\rangle&=\frac2{117}\mathcal D_f,&
 \mathcal D_f&=\sum_{\{p,q\}\ {\rm adjacent}}\delta_{pq}(f)^2 .
 \qquad\text{(108)}
\end{aligned}
$$

 The constants are respectively $1/(4\cdot9^2)+3/(4\cdot39^2)$ and $(9/2)/(4\cdot9^2)+3(13/2)/(4\cdot39^2)$. The central transformation $U_i(n)\mapsto(-1)^{\sum_{j<i}n_j}U_i(n)$ negates every $W_p$ and preserves the link Casimirs. It identifies the centered problems at $\xi$ and $-\xi$, including the centered weighted state. Consequently norm and energy are even: 

$$
\qquad\text{(109)}
 \|\Xi_f\|^2=\frac{49}{13689}\kappa^2\xi^4\mathcal D_f+
 O_{L,f}(\kappa^2\xi^6),\quad
 q_{\mathcal A}[\Xi_f]=\frac2{117}\kappa^3\xi^4\mathcal D_f+
 O_{L,f}(\kappa^3\xi^6).
$$

Here are complete all-box counts for the new quadratic profiles. For $e=(n,i)$, put $m=n+\mathbf e_i/2$. A face in transverse direction $j$ on side $\epsilon$ has center $m+\epsilon\mathbf e_j/2$. Averaging its four edge-midpoint quadratic values gives 

$$
f_p=f_S(e)+\epsilon(Sm)_j+(S_{ii}+3S_{jj})/8.
$$

 Indeed its midpoint displacements from its center are $\pm\mathbf e_i/2,\pm\mathbf e_j/2$; the average correction to the center value is $(S_{ii}+S_{jj})/8$. Consequently opposite coplanar faces give $\delta=(S_{ii}+3S_{jj})/4$. Two hinged faces in directions $j,k$ on sides $\epsilon,\eta$ give 

$$
\delta=\epsilon(Sm)_j+\eta(Sm)_k+c_i,\qquad
 c_i=(2S_{ii}+3S_{jj}+3S_{kk})/8 .
$$

 For each longitudinal coordinate the count and second midpoint moment are $N_i=2L$ and $I_2=L(4L^2-1)/6$. For each oriented transverse pair $(n,\epsilon)$ satisfying $-L\le n,n+\epsilon\le L$, the sums are 

$$
N=4L,\quad \sum n=\sum\epsilon=0,\quad
 N_2=\sum n^2=\frac{2L(2L^2+1)}3,\quad
 E_n=\sum\epsilon n=-2L .
$$

 These follow from the sums over $n=-L,\ldots,L-1$ at $\epsilon=1$ and $n=-L+1,\ldots,L$ at $\epsilon=-1$. Expansion of every square now yields the exact finite formula 

$$
\begin{aligned}
 \mathcal D_S^{\rm cop}&=N_i(2L-1)(2L+1)
                  \sum_{i\ne j}(S_{ii}+3S_{jj})^2/16,\\
 \mathcal D_S^{\rm hinge}
 &=\sum_i\bigl[
 I_2N^2(S_{ij}^2+S_{ik}^2)
 +N_iNN_2(S_{jj}^2+S_{kk}^2+2S_{jk}^2)\\
 &\hspace{12mm}+2N_iE_n^2(S_{jj}S_{kk}+S_{jk}^2)
 +2c_iN_iNE_n(S_{jj}+S_{kk})+c_i^2N_iN^2\bigr].
\end{aligned}
$$

 In each summand $\{j,k\}=\{1,2,3\}\setminus\{i\}$ and $\mathcal D_S=\mathcal D_S^{\rm cop}+\mathcal D_S^{\rm hinge}$. There is no periodic boundary replacement.

Substitution of the three seed matrices gives 

$$
\begin{aligned}
 \mathcal D_0&=4L(2L-1)(2L+1)(4L^2+3),\\
 \mathcal D_{\rm d}&=L(256L^4+74L^2-21)/6,\\
 \mathcal D_{\rm o}&=64L^3(2L^2+1)/3.\qquad\text{(110)}
\end{aligned}
$$

 All are positive for $L\ge2$. The same substitution for $S_*=\eta\eta^{\mathsf T}$, or the already proved cubic decomposition of the coefficient Gram matrix, gives 

$$
\qquad\text{(111)}
 \mathcal D_{S_*}
 =\frac{L(14536832L^4+5453566L^2-1614327)}{24576}>0 .
$$

 Equation (109) proves nonzero seed states for sufficiently small positive $\xi$ on each fixed box and proves 

$$
\frac{q_{\mathcal A}[\Xi_{f_{S_*}}]}{\|\Xi_{f_{S_*}}\|^2}
       =\frac{234}{49}\kappa+O_L(\kappa\xi^2).
$$

 This is an ordered fixed-box coefficient result, not a volume-uniform remainder bound. In original variables $\kappa^2\xi^4=1/(64g^{12}a^2)$ and $\kappa^3\xi^4=1/(32g^{10}a^3)$. The $L^5$ growth in (111) belongs to the computed Taylor coefficient of both raw moments. Their common spatial and material growth does not by itself reduce the quotient.

## Full Schur map and the remaining collective spectral question

For a physical state $\Xi_f$ in the original Haar space set $h_f=\Xi_f/\psi$, which is smooth at each finite regulator, and retain 

$$
F_f=J_m^*h_f,\quad
 v_f=\mathcal R_mF_f,\quad
 k_f=Q_mh_f+C^{-1}B_mF_f.
$$

 These are the exact maps and domains of Theorem 9.1. The identity $h_f=v_f+k_f$ has 

$$
\begin{aligned}
 q(h_f,h_f)&=s_{m,0}(F_f,F_f)+c_m(k_f,k_f),\\
 \|\Xi_f\|^2&=\|v_f\|^2+\|k_f\|^2
                         +2\operatorname{Re}\langle v_f,k_f\rangle,\\
 \|v_f\|^2&=\|F_f\|^2+\int t^{-2}\,d\sigma_{F_f}(t),\\
 s_{m,0}(F_f,F_f)&=a_m(F_f,F_f)-\int t^{-1}\,d\sigma_{F_f}(t).
\end{aligned}
$$

 No interaction or norm term has been removed. The signed permutations above preserve the skeleton with $m\mid2L$: the transverse coarse coordinates $-L+m\{0,\ldots,2L/m\}$ are invariant under sign reversal, and chain products reverse by group inversion. Vacuum conditional averaging therefore intertwines these symmetries by change of variables in its defining integral. So do $B_m,C$ and the full memory kernels; for the latter use functional calculus for $e^{-sC}$ or $(C+z)^{-1}$. Their spectral matrix elements have the same symmetry-forced vanishing cross terms. This does not evaluate the remaining same-sector measures by a free approximation.

In the proved regime $\xi\le1/49152$, every nonzero constructed physical state obeys $q/\|\Xi\|^2\ge\kappa(3-512\xi)\ge287\kappa/96$. Outside that regime the exact three-measure formula remains valid but does not compute the unknown seed measures. On any regulator sequence, at least one of the nonzero three seed states has quotient no larger than the quadratic combination, since (104) makes its quotient a weighted mean with weights $w_jd_j\ge0$. Thus a vanishing quotient in this full-tensor quadratic family would also give a vanishing quotient in a selected seed sector along that sequence. At fixed regulator (106) instead gives the precise endpoint measure and ratio. No exchange of the material endpoint, infinite-volume limit, or spatial continuum limit has been made. The calculation leaves those three interacting seed-sector limits as substantive research, not as assumed estimates. Section 14 now calculates their complete fixed-box weak-coupling pair measures, proves an injective lowest-band tensor map, and constructs an actual positive-coupling projected Fabel sequence with a vanishing energy quotient. It retains the whole-state raw norm and band fraction. The common interacting continuum identification remains unresolved.

