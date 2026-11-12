# Mathematical correction — 8 September 2026

This corrected edition supersedes the earlier draft at this path. It is extracted from the complete Section 13 of extensive_quantum_blocking.tex/.md. The full proof, source inputs, boundary derivation and scope are in [FABEL_TENSOR_TRANSFER.md](FABEL_TENSOR_TRANSFER.md). Equation numbers refer to the cumulative manuscript. No four-dimensional mass-gap disproof is claimed.

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

