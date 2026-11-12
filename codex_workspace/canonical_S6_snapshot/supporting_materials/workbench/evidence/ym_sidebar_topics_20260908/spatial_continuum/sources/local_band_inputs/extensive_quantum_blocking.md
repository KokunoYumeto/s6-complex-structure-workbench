# Extensive true-vacuum quantum blocking in the full spatial Wilson box

Exact path-product maps, associative memory, and physical spectral channels. 8 September 2026.

## Original objects and the finite interacting operator

Let $L\geq2$ be an integer. The vertex set is $\mathsf V_L=\{-L,-L+1,\ldots,L\}^3$. For each $i\in\{1,2,3\}$, the physical edge $e=(n,i)$ goes from $n$ to $n+\mathbf e_i$ when both vertices are present. Its variable is $U_i(n)\in\operatorname{SU}(2)$. Inverse traversal uses $U_i(n)^{-1}$. Every such edge belongs to $\mathsf E_L$. Every elementary face $p=(n;i,j)$, $i<j$, with four vertices in the box belongs to $\mathsf P_L$; its ordered holonomy and trace are 

$$
\qquad\text{(1)}
 U_p=U_i(n)U_j(n+\mathbf e_i)U_i(n+\mathbf e_j)^{-1}U_j(n)^{-1},
 \qquad W_p=\operatorname{tr}U_p.
$$

 The counts are $N=3(2L)(2L+1)^2$ and $M=3(2L)^2(2L+1)$: fix a direction or a face plane and count its initial and transverse coordinates. The configuration space is $\mathcal Q=\operatorname{SU}(2)^{\mathsf E_L}$ with product Haar probability measure $\lambda$. Put 

$$
\begin{gathered}
 T_a=-i\sigma_a/2,\qquad
 X_{e,a}f=\left.\frac{d}{dt}f(\ldots,e^{tT_a}U_e,\ldots)\right|_{t=0},
 \qquad E_e=-\sum_{a=1}^3X_{e,a}^2,\qquad\text{(2)}\\
 H=\kappa\sum_{e\in\mathsf E_L}E_e+b\sum_{p\in\mathsf P_L}(2-W_p),\qquad
 \kappa=\frac{2g^2}{a},\quad b=\frac{1}{2g^2a},\quad
 \xi=\frac b\kappa=\frac1{4g^4},\quad a,g>0.\qquad\text{(3)}
\end{gathered}
$$

 Here $a$ in $a,g>0$ denotes spatial spacing; the color index in (2) is summed only when indicated. Haar integration by parts makes $X_{e,a}$ skew-adjoint. The Pauli identities give $-2\operatorname{tr}(T_aT_b)=\delta_{ab}$ and $-\sum_aT_a^2=3I/4$. The original metric $c(A,B)=-\operatorname{tr}(AB)/2$ has orthonormal basis $2T_a$; hence $X^c=2X$, $\Delta^c=4\Delta^T$, and the same kinetic term is $-(\kappa/4)\sum_e\Delta_e^c$. All faces, including boundary faces and faces in every plane, remain in (3). In particular the exact scalar term $2bM=M/(g^2a)$ is part of $H$.

Gauge transformations are $(h\cdot U)_e=h_{s(e)}^{-1}U_eh_{t(e)}$. The form of $H$ on $H^1(\mathcal Q)$ is 

$$
q_H(u,v)=\kappa\sum_{e,a}\int\overline{X_{e,a}u}X_{e,a}v\,\mathrm d\lambda
        +b\sum_p\int(2-W_p)\overline uv\,\mathrm d\lambda.
$$

 It is closed, since the smooth potential is bounded between $0$ and $4bM$. Its associated self-adjoint operator has domain $H^2$ by elliptic regularity; smooth functions are operator and form cores. Compact Sobolev embedding gives compact resolvent. Taking the modulus of a minimizing vector does not increase its form: apply the chain rule first to $(|u|^2+\epsilon^2)^{1/2}$ and then let $\epsilon$ decrease to zero. The resulting nonnegative lowest eigenfunction is smooth by elliptic regularity and strictly positive by the elliptic strong maximum principle. Write it as $\psi>0$, with $H\psi=E_0\psi$ and $\int\psi^2\,\mathrm d\lambda=1$. This fixes the state norm; none of the physical coefficients is changed.

Set $\rho=\psi^2$, $\mu=\rho\lambda$, and $\mathscr H=L^2(\mu)$. Multiplication $\mathcal Uu=\psi u$ is a unitary $\mathscr H\to L^2(\lambda)$, with inverse division by $\psi$. The product rule and $H\psi=E_0\psi$ give 

$$
\begin{aligned}
 \mathscr L&=\mathcal U^{-1}(H-E_0)\mathcal U
 =-\kappa\sum_{e,a}\bigl[X_{e,a}^2+(X_{e,a}\log\rho)X_{e,a}\bigr],
 \qquad\text{(4)}\\
 q(u,v)&=\kappa\sum_{e,a}\int\overline{X_{e,a}u}X_{e,a}v\,\mathrm d\mu,
 \qquad D(q)=\mathscr V=H^1(\mathcal Q).\qquad\text{(5)}
\end{aligned}
$$

 Integration by parts proves the form identity. Multiplication and division by the smooth positive $\psi$ preserve every integer Sobolev space, so the form and operator domains are respectively $H^1,H^2$. If $q(u,u)=0$, all its derivatives vanish and connectedness makes $u$ constant. This proves uniqueness of $\psi$, and its gauge invariance follows because gauge transformations preserve $H$, positivity and norm. It also proves that the finite first nonzero eigenvalue $\delta$ of $\mathscr L$ is strictly positive. No uniform lower bound for $\delta$ is used in the uniform estimates below. Inner products are conjugate-linear in their first arguments.

## A uniform single-link estimate for the actual vacuum

This section supplies estimates independent of $L$, with every $b>0$ allowed. Define the constants 

$$
\qquad\text{(6)}
 D=16b,\quad d=D/\kappa=16\xi=4/g^4,\quad
 t_0=\frac{2\log12}{\kappa},\quad
 R=3e^{Dt_0}=3\,12^{2d},\quad \alpha=R^{-2},
$$

 and 

$$
\qquad\text{(7)}
 G=R\exp\!\left(\frac d{1+d}\right)
       \left(1+\frac{2d}{1+d}\right)\sqrt{\frac{1+d}{2}},
 \qquad C_*=\frac32+2G.
$$

 Here $D$ has units of energy and $t_0$ of inverse energy. The constants $d,R,\alpha,G,C_*$ are dimensionless and depend on the original coupling $g$, but not on the number of links, the blocking length, or $a$ separately.

### Lemma 2.1.

For the single-link heat operator $P_t=e^{-t\kappa E}$, its kernel at $t=t_0$ lies between $1/2$ and $3/2$. For every real smooth $f$, 

$$
\qquad\text{(8)}
 2\kappa t\sum_a|X_aP_tf|^2
 \leq P_t(f^2)-(P_tf)^2,\qquad
 \|\nabla P_tf\|_\infty\leq\frac{\|f\|_\infty}{\sqrt{2\kappa t}}.
$$

### Proof.

The spin-$j$ representation has dimension $2j+1$ and Casimir $j(j+1)$ in (2). One can verify the latter by the eigenvalues $m=-j,\ldots,j$ of $iT_3$ and the raising/lowering coefficients $\sqrt{(j\mp m)(j\pm m+1)}$; their quadratic sum is $j(j+1)$. Peter--Weyl completeness therefore gives the heat kernel $p_t(U)=\sum_{j\geq0}(2j+1)e^{-\kappa tj(j+1)}\chi_j(U)$. This series is absolutely uniformly convergent for $t>0$, since $|\chi_j|\leq2j+1$. Writing $k=2j$, using $j(j+1)=k(k+2)/4\geq k/2$ and $(k+1)^2\leq4^k$ for $k\geq1$, gives 

$$
|p_{t_0}-1|\leq\sum_{k\geq1}4^k e^{-\kappa t_0k/2}
 =\sum_{k\geq1}3^{-k}=\frac12.
$$

 For the gradient assertion, the bi-invariant Casimir commutes with each $X_a$: the commutator of its sum of squares with $X_b$ contracts antisymmetric Lie structure constants with $X_aX_c+X_cX_a$ and is zero. Thus $X_aP_s=P_sX_a$ on smooth functions, and Jensen's inequality gives $\Gamma(P_sf)\leq P_s\Gamma(f)$ for $\Gamma(f)=\sum_a|X_af|^2$. Differentiate $P_s[(P_{t-s}f)^2]$ and use the product rule: 

$$
P_t(f^2)-(P_tf)^2=2\kappa\int_0^tP_s\Gamma(P_{t-s}f)\,\mathrm ds
 \geq2\kappa t\Gamma(P_tf).
$$

 The last inequality applies the preceding gradient contraction with input $P_{t-s}f$. The supremum estimate follows because $P_t(f^2)\leq\|f\|_\infty^2$. This is the exact single-group version of the reverse Poincare inequality [\[2, Eq. (1.7)\]](https://doi.org/10.4171/RMI/470), with the time and generator coefficient displayed explicitly.

### Theorem 2.2.

Fix one physical link $e$ and write all other variables as $y$. For all $u,u'\in\operatorname{SU}(2)$ and $y$, 

$$
\qquad\text{(9)}
 R^{-1}\leq\frac{\psi(u,y)}{\psi(u',y)}\leq R,\qquad
 \alpha\leq\frac{\rho(u,y)}{\int\rho(v,y)\,\mathrm dv}\leq\alpha^{-1}.
$$

 Moreover, 

$$
\qquad\text{(10)}
 \left(\sum_a|X_{e,a}\log\psi|^2\right)^{1/2}\leq G,
 \qquad |\nabla_e\log\rho|\leq2G.
$$

 All bounds are uniform in $e$ and $L$ at the fixed positive $a,g$.

### Proof.

Let $V_e=b\sum_{p\ni e}(2-W_p)$ and let $H_{\neg e}$ contain all other kinetic terms and all faces not incident to $e$. There are at most four incident faces in the full three-dimensional box, including the boundary cases with fewer faces. Therefore $0\leq V_e\leq D$, and the exact operator is 

$$
H=A_e+V_e,\qquad A_e=\kappa E_e+H_{\neg e},\qquad
 T_t=e^{-tA_e}=P_t^{(e)}\otimes e^{-tH_{\neg e}}.
$$

 The two factors of $T_t$ commute because $H_{\neg e}$ is independent of $u$. They have positive kernels. The parabolic comparison principle with the bounded multiplication $0\leq V_e\leq D$ gives, for $f\geq0$, 

$$
\qquad\text{(11)}
 e^{-Dt}T_tf\leq e^{-tH}f\leq T_tf.
$$

 For example $T_tf$ is a supersolution for $\partial_t+A_e+V_e$, while $e^{-Dt}T_tf$ is a subsolution; their initial data agree. The maximum principle gives (11). This proves the comparison for this compact group product directly; no Euclidean configuration-space identification is needed.

Apply it to $\psi$. At $t_0$, positivity of the other-link kernel and Lemma 2.1 imply 

$$
\frac{(T_{t_0}\psi)(u,y)}{(T_{t_0}\psi)(u',y)}\leq3.
$$

 Since $e^{-tH}\psi=e^{-tE_0}\psi$, comparison at both $u,u'$ gives $\psi(u,y)/\psi(u',y)\leq3e^{Dt_0}=R$. Interchanging $u,u'$ proves both sides. Squaring and averaging the denominator over $u'$ proves the conditional density bounds. The extensive energy $E_0$ cancels from this ratio exactly.

Here is a derivative proof that does not differentiate an unknown vacuum estimate. If a positive function $F(u,y)$ satisfies the first ratio bound, so does $f_t(u)=(e^{-tH_{\neg e}}F(u,\cdot))(y)$ at each fixed $y$, by positivity. Hence $\|f_t\|_\infty\leq R\min f_t\leq RP_t f_t(u)$. Lemma 2.1 yields 

$$
|\nabla_e T_t\psi|\leq\frac{R}{\sqrt{2\kappa t}}T_t\psi.
$$

 The function $(e^{-tH_{\neg e}}(V_e\psi))(u,y)$ is nonnegative and bounded above by $D(e^{-tH_{\neg e}}\psi)(u,y)$. Its supremum in $u$ is consequently at most $DR\min_u(e^{-tH_{\neg e}}\psi)(u,y)$. The same heat estimate gives 

$$
|\nabla_e T_t(V_e\psi)|\leq\frac{DR}{\sqrt{2\kappa t}}T_t\psi.
$$

 The exact Duhamel identity on the smooth eigenvector is 

$$
\qquad\text{(12)}
 \psi=e^{E_0t}T_t\psi-\int_0^t e^{E_0\tau}T_\tau(V_e\psi)\,\mathrm d\tau.
$$

 It follows either by differentiating $e^{E_0t}T_t\psi$ and using $A_e\psi=(E_0-V_e)\psi$, or by the bounded-potential Duhamel formula. Comparison gives $e^{E_0\tau}T_\tau\psi\leq e^{D\tau}\psi$. The two gradient estimates, whose $\tau^{-1/2}$ singularity is integrable, justify differentiation of (12) and give 

$$
\frac{|\nabla_e\psi|}{\psi}
 \leq R\left[\frac{e^{Dt}}{\sqrt{2\kappa t}}
       +D\int_0^t\frac{e^{D\tau}}{\sqrt{2\kappa\tau}}\,\mathrm d\tau\right]
 \leq\frac{Re^{Dt}(1+2Dt)}{\sqrt{2\kappa t}}.
$$

 Choose the actual time $t=(\kappa+D)^{-1}$. This last expression is exactly $G$ in (7). Finally $X\log\rho=2X\log\psi$. No gap bound, perturbation disk, or correlation factorization was used.

## A specified extensive spatial blocking sequence

Let $m\geq1$ divide $2L$, and put $q_m=2L/m$. Retain as skeleton links those direction-$i$ fine edges whose two transverse coordinates lie in $-L+m\{0,1,\ldots,q_m\}$. Every longitudinal fine edge on each such line is included. Denote this subset by $R_m$ and its complement by $S_m$. Its exact count is 

$$
\qquad\text{(13)}
 |R_m|=3(2L)(q_m+1)^2,\qquad
 |S_m|=3(2L)\bigl[(2L+1)^2-(q_m+1)^2\bigr].
$$

 Thus a fixed $m>1$ eliminates an extensive number of links as the box increases. If $m\mid n\mid2L$, then $R_n\subset R_m$. In particular $m=1,2,4,\ldots,2^k$ gives a repeated blocking sequence whenever $2^k\mid2L$. The Hamiltonian still has all $N$ link and $M$ face terms.

The coarse vertices are the points $x\in[-L,L]^3$ whose coordinates all lie in $-L+m\mathbb Z$. A coarse direction-$i$ edge $\gamma=(x,i)$ is the ordered path of $m$ fine edges from $x$ to $x+m\mathbf e_i$. The number of coarse edges is 

$$
N_m=3q_m(q_m+1)^2,\qquad |R_m|=mN_m.
$$

 The chains have disjoint physical-edge supports and meet only at coarse vertices. Write their variables as $u_{\gamma,1},\ldots,u_{\gamma,m}$ in positive order, and define 

$$
\qquad\text{(14)}
 z_\gamma=u_{\gamma,1}\cdots u_{\gamma,m},\qquad
 \pi_m:\mathcal Q\longrightarrow\mathcal Q_m:=\operatorname{SU}(2)^{N_m}.
$$

 No original coordinate was replaced by a unit coarse spacing: the physical coarse spacing is $ma$, while the original coordinates remain $x$.

For every chain put $v_{\gamma,k}=u_{\gamma,k}$ for $k<m$. Let $y$ comprise all $v$ and all untouched variables on $S_m$. The full typed coordinate map is 

$$
\Phi_m:\mathcal Q\longrightarrow\mathcal Y_m\times\mathcal Q_m,
 \quad U\longmapsto(y,z),\qquad
 \mathcal Y_m=\operatorname{SU}(2)^{S_m}\times
                \prod_{\gamma=1}^{N_m}\operatorname{SU}(2)^{m-1}.
$$

 It is a global smooth bijection. Its inverse $\Phi_m^{-1}:\mathcal Y_m\times\mathcal Q_m\to\mathcal Q$ uses 

$$
u_{\gamma,m}=(v_{\gamma,1}\cdots v_{\gamma,m-1})^{-1}z_\gamma,
$$

 and keeps every other variable. Substituting the original ordered product cancels its prefix on the left and recovers $u_{\gamma,m}$. Conversely multiplying the retained prefix by the displayed last link recovers $z_\gamma$. Every $v$ and every $S_m$ coordinate is fixed, so both compositions are the identity on their respective full spaces. There are $|S_m|+(m-1)N_m=N-N_m$ factors in $\mathcal Y_m$; none of those coordinates is omitted from $\Phi_m$. Integrating $u_{\gamma,m}$ last, left invariance of Haar proves the exact measure identity 

$$
\qquad\text{(15)}
 \,\mathrm d\lambda(U)=\,\mathrm d\lambda_y(y)\,\mathrm d\lambda_m(z).
$$

 This proves the map and its measure factor, rather than postulating independent coarse links in the interacting vacuum.

The complete kinetic operator in these coordinates is as follows. Define the prefix and the real orthogonal matrix $O_{\gamma,k}$ by 

$$
p_{\gamma,k}=v_{\gamma,1}\cdots v_{\gamma,k-1},\qquad
 p_{\gamma,k}T_a p_{\gamma,k}^{-1}
   =\sum_b O_{\gamma,k;ba}T_b.
$$

 Orthogonality follows by applying $-2\operatorname{tr}(AB)$ to both conjugated factors; its determinant is $1$ by connectedness. Let $D_{\gamma,b}$ be left multiplication differentiation on $z_\gamma$, with the same $T_b$. For $k<m$ the transformed fine vector field is 

$$
X_{\gamma,k,a}=X_{v_{\gamma,k},a}
            +\sum_bO_{\gamma,k;ba}D_{\gamma,b};
$$

 for $k=m$ it is $\sum_bO_{\gamma,m;ba}D_{\gamma,b}$. The prefix $p_{\gamma,k}$ does not involve $v_{\gamma,k}$, and no $O$ depends on $z$. The full sum of squares is consequently 

$$
\begin{aligned}
\qquad\text{(16)}
 \sum_{e,a}X_{e,a}^2
 ={}&\sum_{e\in S_m,a}X_{e,a}^2
 +\sum_{\gamma}\left[\sum_{k<m,a}X_{v_{\gamma,k},a}^2
                      +m\sum_bD_{\gamma,b}^2\right]\\
 &+2\sum_{\gamma,k<m,a,b}O_{\gamma,k;ba}
                    X_{v_{\gamma,k},a}D_{\gamma,b}.
\end{aligned}
$$

 Each square before expansion is the square of the displayed original field, so this formula includes all mixed derivatives with their signs and coefficients. Every original $W_p$ in (3) is evaluated at the explicit inverse coordinate map. It is not replaced by a coarse face trace or truncated to selected words.

Gauge transformations on a chain cancel at its internal vertices and give $z_\gamma\mapsto h_x^{-1}z_\gamma h_{x+m\mathbf e_i}$. The marginal density on $R_m$ is invariant under the internal gauge transformations, by gauge invariance of $\rho$ and Haar substitution on $S_m$. A non-coarse skeleton vertex is bivalent in the skeleton. For a fixed chain with endpoints fixed, set successively $h_{x+k\mathbf e_i}=(u_1\cdots u_k)^{-1}$, $k<m$. This sends its first $m-1$ links to the identity and its last to $z_\gamma$. Different chain interiors are disjoint, so these choices are simultaneous. It follows that this skeleton marginal is a function of $z$ alone. This statement concerns the marginal; the full conditional distribution of $y$ given $z$ need not factorize.

## The actual coarse density, domains, and conditional coupling

Let $\widetilde\rho_m(y,z)=\rho(U(y,z))$ and define 

$$
\begin{gathered}
 r_m(z)=\int\widetilde\rho_m(y,z)\,\mathrm d\lambda_y,
 \quad \mu_m=r_m\lambda_m,\quad
 p_m(y\mid z)=\widetilde\rho_m(y,z)/r_m(z),\qquad\text{(17)}\\
 \mathscr K_m=L^2(\mu_m),\quad J_m f=f\circ\pi_m,\quad
 P_m=J_mJ_m^*,\quad Q_m=I-P_m,\\
 (J_m^*u)(z)=\int p_m(y\mid z)u(U(y,z))\,\mathrm d\lambda_y.\qquad\text{(18)}
\end{gathered}
$$

 In particular the types are $J_m:\mathscr K_m\to\mathscr H$ and $J_m^*:\mathscr H\to\mathscr K_m$. Their full coordinate expressions are $J_mf(U)=f(z(U))$ and the fibre integral (18); the operator $P_m:\mathscr H\to J_m\mathscr K_m\subset\mathscr H$ is their composition. Smoothness and strict positivity follow from compact integration. Fubini proves the adjoint formula and $J_m^*J_m=I$; Jensen proves that $J_m^*$ is a contraction. Thus $P_m$ is the true-vacuum orthogonal projection. All these maps intertwine the stated fine and coarse gauge actions. The restriction of the conditional projection onto skeleton functions, on the fine invariant Hilbert space, equals this path projection: its output is internally gauge invariant, hence depends only on $z$, as proved in the preceding section. The exact invariant Hilbert-space unitary, its almost-everywhere inverse and the equality of the full complementary operator domains are proved in Proposition 10.1.

For each chain and color set, in the original coordinates, 

$$
\qquad\text{(19)}
 Y_{\gamma,b}=\frac1m\sum_{k=1}^m\sum_a
                   O_{\gamma,k;ba}X_{\gamma,k,a}.
$$

 Then $Y_{\gamma,b}J_mf=J_mD_{\gamma,b}f$. Indeed each summand differentiates $z_\gamma$ in the direction $\operatorname{Ad}_{p_{\gamma,k}}T_a$, and orthogonality of $O$ gives one copy of $D_{\gamma,b}$ per $k$. Also $Y_{\gamma,b}$ has zero Haar divergence: every coefficient $O_{\gamma,k;ba}$ is independent of its own differentiated fine edge. Consequently integration by parts against a coarse smooth test function gives the exact derivative identities 

$$
\begin{aligned}
 D_{\gamma,b}\log r_m&=J_m^*(Y_{\gamma,b}\log\rho),\qquad\text{(20)}\\
 D_{\gamma,b}J_m^*u
   &=J_m^*(Y_{\gamma,b}u)+J_m^*(\beta_{\gamma,b}u),\qquad\text{(21)}\\
 \beta_{\gamma,b}&=Y_{\gamma,b}\log\rho
                       -J_mD_{\gamma,b}\log r_m,\qquad J_m^*\beta_{\gamma,b}=0.
 \qquad\text{(22)}
\end{aligned}
$$

 For example integrate $Y_{\gamma,b}(J_m\varphi\,\rho)$ over the full configuration space; its integral is zero. The resulting identity is $\int(D_{\gamma,b}\varphi)r_m=-\int\varphi J_m^*(Y_{\gamma,b}\log\rho)r_m$, which proves (20). Apply the same calculation to $u\rho$ to prove (21). This also avoids differentiating fibre coordinates while holding an incompatible fine coordinate fixed.

Theorem 2.2, the average in (19), and conditional Jensen give 

$$
\qquad\text{(23)}
 |Y_\gamma\log\rho|\leq2G,\qquad
 |D_\gamma\log r_m|\leq2G,\qquad |\beta_\gamma|\leq4G.
$$

 Here each absolute value is the Euclidean norm of its three color components. The first inequality uses the average of $m$ rotated vectors, each with norm at most $2G$; it does not assume independence.

### Proposition 4.1.

The exact lifted form and its generator are 

$$
\begin{aligned}
 a_m(f,g)&=q(J_mf,J_mg)
    =\kappa m\sum_{\gamma,b}\int\overline{D_{\gamma,b}f}D_{\gamma,b}g\,\mathrm d\mu_m,
       &D(a_m)&=\mathscr V_m=H^1(\mathcal Q_m),\qquad\text{(24)}\\
 A_m&=-\kappa m\,r_m^{-1}\sum_{\gamma,b}D_{\gamma,b}(r_mD_{\gamma,b}),
       &D(A_m)&=H^2(\mathcal Q_m).\qquad\text{(25)}
\end{aligned}
$$

 The maps $J_m,J_m^*$ preserve all integer Sobolev spaces, and $P_m,Q_m$ preserve $\mathscr V$. On $\mathscr V_m$ the full eliminated coupling is 

$$
\qquad\text{(26)}
 B_mf=-\kappa m\sum_{\gamma,b}\beta_{\gamma,b}J_mD_{\gamma,b}f,
 \quad J_m^*B_mf=0,\quad \mathscr LJ_mf=J_mA_mf+B_mf\quad(f\in H^2).
$$

 In particular the retained kinetic coefficient is exactly $\kappa m$.

### Proof.

The fine derivative of $J_mf$ on edge $(\gamma,k)$ is the orthogonal rotation $O_{\gamma,k}^TD_\gamma f$; on $S_m$ it is zero. Summing the squared derivatives over the $m$ edges proves (24). The smooth positive weight gives closedness and the $H^2$ elliptic domain of (25). The compact smooth coordinate bijection (15) preserves each integer Sobolev class with finite norm bounds, since its derivatives and inverse derivatives are bounded. The fibre integral with smooth positive kernel $p_m$ has bounded derivatives of every finite order. This proves the Sobolev mapping claims.

There is also a useful explicit first-order estimate. Define 

$$
\eta_m=\kappa m\left\|\sum_{\gamma,b}\beta_{\gamma,b}^2\right\|_\infty
             \leq16\kappa mN_mG^2.
$$

 Orthogonality of the rotations and Cauchy--Schwarz in the $k$ sum give the pointwise inequality 

$$
m\sum_{\gamma,b}|Y_{\gamma,b}u|^2
 \leq\sum_{e\in R_m,a}|X_{e,a}u|^2.
$$

 Conditional Jensen and (21) consequently give 

$$
\qquad\text{(27)}
 a_m(J_m^*u,J_m^*u)\leq2q(u,u)+2\eta_m\|u\|_\mu^2.
$$

 This extends by smooth approximation. The same derivative identities show that $J_mf\in H^1$ implies $f\in H^1$, so the retained form space has exactly the claimed domain. On a lifted smooth $f$, (16) gives $\sum_{e,a}X_{e,a}^2J_mf=mJ_m\sum_{\gamma,b}D_{\gamma,b}^2f$. The drift in (4) is $-\kappa m\sum_{\gamma,b}(Y_{\gamma,b}\log\rho)J_mD_{\gamma,b}f$. Subtract (25), and use (22); this proves (26) for smooth $f$. Density gives the stated $H^2$ identity and the bounded map $B_m:\mathscr V_m\to Q_m\mathscr H$, with 

$$
\qquad\text{(28)}
 \|B_mf\|_\mu^2\leq\eta_m a_m(f,f).
$$

The full correlation tensor of the induced first-order terms is 

$$
\qquad\text{(29)}
 I_{\gamma b,\eta c}(z)=J_m^*(\beta_{\gamma,b}\beta_{\eta,c})(z),\quad
 \|B_mf\|^2=(\kappa m)^2\int
 \sum_{\gamma,b,\eta,c}I_{\gamma b,\eta c}
              \overline{D_{\gamma,b}f}D_{\eta,c}f\,\mathrm d\mu_m.
$$

 Every off-diagonal index is retained. This is the conditional covariance of the vectors $Y_{\gamma,b}\log\rho$. It is positive semidefinite because its quadratic form is a conditional expectation of a squared absolute value. Positivity does not assert that its different entries vanish or that it is uniformly diagonal-dominant.

There is an exact Haar-space description of the instantaneous marginal operator. Multiplication $f\mapsto\sqrt{r_m}f$ is a unitary $\mathscr K_m\to L^2(\lambda_m)$, with inverse $v\mapsto v/\sqrt{r_m}$. Both maps preserve $H^1$ and $H^2$, since $r_m$ is smooth and strictly positive on the compact group product. Direct product differentiation gives 

$$
\qquad\text{(30)}
 \sqrt{r_m}A_m r_m^{-1/2}
 =-\kappa m\sum_{\gamma,b}D_{\gamma,b}^2
       +\kappa m\frac{\sum_{\gamma,b}D_{\gamma,b}^2\sqrt{r_m}}{\sqrt{r_m}}.
$$

 The last scalar function equals $\kappa m\sum_{\gamma,b}[D_{\gamma,b}^2\log r_m/2
 +(D_{\gamma,b}\log r_m)^2/4]$. It depends on the entire induced density. No equality with a sum of one-plaquette Wilson terms is asserted. Moreover (30) is only the instantaneous compression; the next section gives the rest of the physical operator relation.

## Exact memory, resolvent reconstruction, and physical norms

Set $\mathscr H_{Q_m}=Q_m\mathscr H$ and $\mathscr V_{Q_m}=\mathscr V\cap\mathscr H_{Q_m}$. The restriction $c_m(h,k)=q(h,k)$ on $\mathscr V_{Q_m}$ is closed and densely defined. Closedness uses the $L^2$-closed subspace, and density follows by applying $Q_m$ to smooth approximants, using (27). Define its self-adjoint operator $C_m$ by 

$$
\begin{aligned}
\qquad\text{(31)}
 D(C_m)=\{h\in\mathscr V_{Q_m}:&\ \exists v\in\mathscr H_{Q_m}\ \text{such that}
 \ c_m(k,h)=\langle k,v\rangle\ \forall k\in\mathscr V_{Q_m}\},
 \qquad C_mh=v.
\end{aligned}
$$

 For smooth $h\in\mathscr H_{Q_m}$ this is $Q_m\mathscr Lh$. Every such $h$ is orthogonal to $1=J_m1$, so $C_m\geq\delta I>0$. For form-domain arguments no formal compression domain is substituted for (31).

For $f,g\in\mathscr V_m$ and $h,k\in\mathscr V_{Q_m}$, integration by parts on a smooth core, followed by continuity, gives 

$$
\qquad\text{(32)}
 q(J_mf+h,J_mg+k)=a_m(f,g)+\langle B_mf,k\rangle
                         +\langle h,B_mg\rangle+c_m(h,k).
$$

 For smooth $h\in\mathscr H_{Q_m}$ the adjoint coupling is 

$$
\qquad\text{(33)}
 B_m^*h=\kappa m\,r_m^{-1}\sum_{\gamma,b}
           D_{\gamma,b}\bigl(r_mJ_m^*(\beta_{\gamma,b}h)\bigr).
$$

 To prove the sign, integrate the negative derivative in (26) against $h$ using Haar integration by parts in $z$. Differentiating the conditional integral by (21) expands each derivative in (33) into terms with $Yh$, $Y\beta$, $\beta^2h$ and $(D\log r_m)\beta h$. All coefficients are smooth and bounded in a fixed box, so $B_m^*:\mathscr V_{Q_m}\to\mathscr K_m$ is bounded. Without that regularity the adjoint is the bounded dual map $\mathscr H_{Q_m}\to\mathscr V_m^*$.

For $z>0$ define on $\mathscr V_m$ the sesquilinear form 

$$
\qquad\text{(34)}
 s_{m,z}(f,g)=a_m(f,g)+z\langle f,g\rangle
             -\langle B_mf,(C_m+z)^{-1}B_mg\rangle.
$$

 The use of $z$ as a positive spectral shift here is distinct from the tuple $z_\gamma$ of coarse link variables. The argument of a resolvent always denotes the scalar shift.

### Theorem 5.1.

The form $s_{m,z}$ is closed with domain $\mathscr V_m$, and its associated operator $S_{m,z}$ satisfies $S_{m,z}\geq zI$. Its exact full resolvent and reconstruction maps are 

$$
\begin{aligned}
 J_m^*(\mathscr L+z)^{-1}J_m&=S_{m,z}^{-1},\qquad\text{(35)}\\
 (\mathscr L+z)^{-1}J_mg
 &=\bigl[J_m-(C_m+z)^{-1}B_m\bigr]S_{m,z}^{-1}g.\qquad\text{(36)}
\end{aligned}
$$

 Every product in these formulas is defined by the displayed form domains.

### Proof.

Completing the square in (32) gives 

$$
\begin{aligned}
\qquad\text{(37)}
 q(J_mf+h,J_mf+h)+z(\|f\|^2+\|h\|^2)
 =s_{m,z}(f,f)+\|(C_m+z)^{1/2}[h+(C_m+z)^{-1}B_mf]\|^2.
\end{aligned}
$$

 Its unique minimizing $h$ is $-(C_m+z)^{-1}B_mf$, which lies in $D(C_m)\subset\mathscr V_{Q_m}$. Nonnegativity of $q$ proves $s_{m,z}(f,f)\geq z\|f\|^2$. Apply (27) to $u=J_mf+h$. It gives 

$$
a_m(f,f)+\kappa\|f\|^2\leq2q(u,u)+(2\eta_m+\kappa)\|u\|^2
 \leq K_{m,z}\,[q(u,u)+z\|u\|^2],
$$

 where $K_{m,z}=\max\{2,(2\eta_m+\kappa)/z\}$ in the form norm with reference energy $\kappa$. This constant is dimensionless. Taking the minimizing $h$ proves a lower form-norm bound. The upper bound $s_{m,z}(f,f)\leq a_m(f,f)+z\|f\|^2$ follows by choosing $h=0$. Their equivalence proves closedness. For $v=(\mathscr L+z)^{-1}J_mg$, its form-domain decomposition $v=J_mf+h$ is legitimate. Testing the weak resolvent equation against $k\in\mathscr V_{Q_m}$ gives $h=-(C_m+z)^{-1}B_mf$; testing against $J_mf'$ gives $s_{m,z}(f',f)=\langle f',g\rangle$. This proves both identities.

The notation in (34) is a closed-form implementation of the Feshbach--Schur map. The general method and reconstruction are established in [\[1, Theorem 1.2, Eqs. (1.10)--(1.16)\]](https://doi.org/10.4171/ECR/18-1/5). That theorem's bounded effective operator assumption is not silently applied to our infinite-rank projection; the coercivity and domain proof above supplies the needed extension for this particular operator.

For smooth initial $f_0$, define $K_m(t)=J_m^*e^{-t\mathscr L}J_m$, $f(t)=K_m(t)f_0$. The full evolution and (32) give 

$$
\begin{aligned}
 f'(t)&=-A_m f(t)+\int_0^t B_m^*e^{-(t-s)C_m}B_m f(s)\,\mathrm ds,
       &f(0)&=f_0,\qquad\text{(38)}\\
 K_m(t)&=J_m^*e^{-t\mathscr L}J_m,\qquad
 \int_0^\infty e^{-zt}K_m(t)\,\mathrm dt=S_{m,z}^{-1}.\qquad\text{(39)}
\end{aligned}
$$

 Here is the domain justification and the sign calculation. Smooth initial data lie in all powers of the compact elliptic $\mathscr L$. Spectral calculus and elliptic regularity keep $v(t)=e^{-t\mathscr L}J_mf_0$, $f(t)=J_m^*v(t)$ and $h(t)=Q_mv(t)$ smooth, continuously in the required Sobolev norms. They satisfy $f'=-A_mf-B_m^*h$, $h'=-B_mf-C_mh$, $h(0)=0$. Variation of constants gives $h(t)=-\int_0^te^{-(t-s)C_m}B_mf(s)\,\mathrm ds$. Since $\sup_{x\geq0}\sqrt{x}e^{-\tau x}=(2e\tau)^{-1/2}$, $e^{-\tau C_m}$ maps $\mathscr H_{Q_m}$ to its form space with norm at most $\sqrt\kappa+(2e\tau)^{-1/2}$ when the squared form norm is $c_m(h,h)+\kappa\|h\|^2$. The singularity is integrable; the bounded form-space map (33) makes (38) a Bochner integral in $\mathscr K_m$. The positive sign follows from the two negative cross terms. The Laplace identity follows by the spectral theorem and Theorem 5.1. This explicitly realizes projection memory of the kind introduced in [\[4\]](https://doi.org/10.1143/PTP.33.423), with this Euclidean generator.

For every smooth $f$, orthogonality of the two components of $\mathscr LJ_mf$ gives the full second moment 

$$
\qquad\text{(40)}
 \|\mathscr LJ_mf\|^2=\|A_mf\|^2+\|B_mf\|^2.
$$

 Thus $K_m(t)$ is replaced by $e^{-tA_m}$ for all $t$ only when $B_m$ vanishes: compare their scalar second derivatives at $t=0$ on a smooth core. Conversely $B_m=0$ makes (32) a direct-sum form and proves that replacement exactly. We do not make that replacement.

The dependence on energy also records the actual reconstructed norm. For fixed $0\ne f\in\mathscr V_m$ with $\mu_m(f)=0$ and scalar $z\geq0$, put 

$$
\qquad\text{(41)}
 w_z=(C_m+z)^{-1}B_mf,\quad
 u_z=\psi(J_mf-w_z),\quad d_f=\|f\|^2.
$$

 The $z=0$ case exists because $C_m\geq\delta>0$ in every fixed box. The vector is in the original form domain, is orthogonal to $\psi$, and is gauge invariant when $f$ is. Its exact norm and energy are 

$$
\begin{aligned}
 \|u_z\|_\lambda^2&=d_f+\|w_z\|_\mu^2
                  =\partial_z s_{m,z}(f,f),\qquad\text{(42)}\\
 \mathfrak q_{H-E_0}[u_z]
 &=a_m(f,f)-\langle B_mf,w_z\rangle-z\|w_z\|^2
   =s_{m,z}(f,f)-z\partial_zs_{m,z}(f,f).\qquad\text{(43)}
\end{aligned}
$$

 To verify these, orthogonality gives the norm; differentiation of the bounded resolvent gives $\partial_z(C_m+z)^{-1}=-(C_m+z)^{-2}$. Testing $(C_m+z)w_z=B_mf$ against $w_z$ gives $c_m(w_z,w_z)=\langle B_mf,w_z\rangle-z\|w_z\|^2$; insert it in (32). Nonnegativity of $q$ proves the numerator is nonnegative. For $B_mf\ne0$ the quotient in (43) divided by (42) is strictly below $a_m(f,f)/d_f$. These are energies of actual full-system vectors; no artificial effective vacuum norm has replaced their eliminated components.

## Associativity of repeated blocking with all prior memory

Let $m\mid n\mid2L$. A coarse $n$-edge is the ordered concatenation of $n/m$ coarse $m$-edges along its line. Let $\pi_{m,n}$ take these products and discard the other $m$-coarse edges. Literal ordered multiplication gives 

$$
\qquad\text{(44)}
 \pi_n=\pi_{m,n}\circ\pi_m,\quad J_n=J_m I_{m,n},\quad
 \mu_n=(\pi_{m,n})_*\mu_m,\quad
 J_n^*=I_{m,n}^*J_m^*.
$$

 Here $I_{m,n}f=f\circ\pi_{m,n}$ is an isometry $\mathscr K_n\to\mathscr K_m$; its adjoint is conditional integration using $r_m$, not Haar integration in place of that weight. Fubini proves each equality, including the adjoint identity. In the full Hilbert space $P_nP_m=P_mP_n=P_n$. All maps preserve the relevant Sobolev spaces by the same compact path-product coordinate construction. Coefficient composition in the instantaneous forms is exactly $\kappa m(n/m)=\kappa n$.

Let $\widehat Q=I-I_{m,n}I_{m,n}^*$ on $\mathscr K_m$. On $\widehat Q\mathscr K_m\cap\mathscr V_m$, let $t_{22,z}$ be the restriction of the already completed form $s_{m,z}$. Define its other block forms by 

$$
\begin{aligned}
 t_{11,z}(f,g)&=s_{m,z}(I_{m,n}f,I_{m,n}g),\\
 t_{21,z}(h,f)&=s_{m,z}(h,I_{m,n}f),\\
 t_{12,z}(f,h)&=s_{m,z}(I_{m,n}f,h).
\end{aligned}
$$

 The operator $T_{22,z}$ associated to $t_{22,z}$ is positive with lower bound $z$. Its inverse also acts from its form dual to its form space, by the coercive weak equation. In that sense the next eliminated component is $h_f=-T_{22,z}^{-1}t_{21,z}(\cdot,f)$, and the next form is 

$$
\qquad\text{(45)}
 s_{n,z}(f,g)=t_{11,z}(f,g)
       -t_{12,z}\bigl(f,T_{22,z}^{-1}t_{21,z}(\cdot,g)\bigr).
$$

 This notation means substitution of the unique weak solution, so does not require multiplying unspecified unbounded compressions.

### Theorem 6.1.

Equation (45) equals the direct fine-to-$n$ form (34). In particular 

$$
\qquad\text{(46)}
 S_{n,z}^{-1}=I_{m,n}^*S_{m,z}^{-1}I_{m,n}
            =J_n^*(\mathscr L+z)^{-1}J_n.
$$

 No memory generated at an earlier level is lost in the next level.

### Proof.

For prescribed $f\in\mathscr V_n$, every $u\in\mathscr V$ with $J_n^*u=f$ has a unique orthogonal decomposition $u=J_n f+J_mh+k$, where $h\in\widehat Q\mathscr K_m\cap\mathscr V_m$ and $k\in\mathscr H_{Q_m}\cap\mathscr V$; obtain it by the nested projections in (44). Put $v_h=J_m(I_{m,n}f+h)$ to keep both arguments of the sesquilinear form explicit. The exact variational identity (37) gives 

$$
\begin{aligned}
 s_{n,z}(f,f)
 &=\inf_{J_n^*u=f}[q(u,u)+z\|u\|^2]\\
 &=\inf_h\inf_k[q(v_h+k,v_h+k)+z\|v_h+k\|^2]\\
 &=\inf_h s_{m,z}(I_{m,n}f+h,I_{m,n}f+h).
\end{aligned}
$$

 The infima have unique minimizers by coercivity and the closed form-space constraints. The weak equation for the last minimizer is precisely the $T_{22,z}$ equation above. Expanding the last form and polarizing proves (45). Alternatively compress (35) by $I_{m,n}$ and use (44); this proves (46) directly and confirms the same unique closed form. Both arguments include all intermediate eliminated components.

To display the generated terms explicitly, write $\mathcal M_{m,z}(f,g)=\langle B_mf,(C_m+z)^{-1}B_mg\rangle$. Then each of $t_{11,z},t_{12,z},t_{21,z},t_{22,z}$ is the corresponding block of $a_m+z\langle\cdot,\cdot\rangle-\mathcal M_{m,z}$. In particular the two off-diagonal blocks contain the corresponding off-diagonal terms of $-\mathcal M_{m,z}$, and $T_{22,z}$ contains its entire diagonal term. Setting these terms to zero would change (45). The exact recursion is independent of the order of the specified nested eliminations; it does not reinitialize the dynamics at each marginal $A_m$.

## A large-block Wilson channel with uniform norm and spectral bounds

Let $C$ be a closed coarse edge word using each coarse physical edge at most once. Its fine path then uses each of its fine physical edges once; let $r$ be its number of coarse edges and $\ell=mr$ its number of fine edges. For example, every elementary coarse face has $r=4$, fine perimeter $\ell=4m$, and physical side length $ma$. Keep its original ordered word, with inverses on the negative traversals, and set 

$$
\begin{gathered}
 W_C(z)=\operatorname{tr}\prod_{(\gamma,\epsilon)\in C}z_\gamma^\epsilon,\quad
 \overline W_C=\mu_m(W_C),\quad r_C=\mu_m(W_C^2),\\
 f_C=W_C-\overline W_C,\quad u_C=\psi J_mf_C,\quad
 d_C=\|u_C\|_\lambda^2=r_C-(\overline W_C)^2.\qquad\text{(47)}
\end{gathered}
$$

 SU(2) traces are real. The fine and coarse gauge actions both fix the closed trace, so $u_C$ is a physical invariant vector, orthogonal to $\psi$. The subtraction is the actual interacting mean.

### Lemma 7.1.

For every such loop, at arbitrary positive coupling, 

$$
\qquad\text{(48)}
 \alpha\leq d_C\leq4,\qquad
 \alpha\leq r_C\leq4-3\alpha.
$$

 The exact unnormalized excitation energy and bounds are 

$$
\qquad\text{(49)}
 \mathfrak q_{H-E_0}[u_C]
   =\kappa\ell\left(1-\frac{r_C}{4}\right),\qquad
 \frac34\alpha\kappa\ell\leq\mathfrak q_{H-E_0}[u_C]\leq\kappa\ell.
$$

 Consequently 

$$
\qquad\text{(50)}
 \frac{3\alpha}{16}\kappa\ell\leq
 \frac{\mathfrak q_{H-E_0}[u_C]}{d_C}
 =\kappa\ell\frac{1-r_C/4}{r_C-(\overline W_C)^2}
 \leq\frac{\kappa\ell}{\alpha}.
$$

### Proof.

Fix any one fine edge used by the loop and condition on all other fine variables. The ordered holonomy is $A u^{\pm1}B$ for fixed group matrices $A,B$, so its Haar distribution is Haar by invariance and inversion. Writing $U=u_0I+i\sum_a u_a\sigma_a$ identifies Haar measure with the uniform measure on the unit sphere in $\mathbb R^4$. Its coordinate second moments are $1/4$ by sign and permutation symmetry and $\sum_{a=0}^3u_a^2=1$. Thus $\int W_C\,\mathrm du=0$, $\int W_C^2\,\mathrm du=1$, and $\int(1-W_C^2/4)\,\mathrm du=3/4$. The conditional density is bounded below by $\alpha$ from Theorem 2.2. Integrating the two nonnegative functions $W_C^2$ and $4-W_C^2$ proves the two bounds on $r_C$. For every real constant $c$, conditional integration gives $\int(W_C-c)^2p(u\mid y)\,\mathrm du\geq\alpha\int(W_C-c)^2\,\mathrm du
=\alpha(1+c^2)\geq\alpha$. Taking $c$ to be that conditional mean proves conditional variance at least $\alpha$. The law of total variance, obtained by expanding around the conditional mean and integrating the cross term to zero, proves $d_C\geq\alpha$. Since $|W_C|\leq2$, $d_C\leq4$.

For a positive occurrence, a based form of the derivative is $\operatorname{tr}(T_aA_C)$ with $A_C\in\operatorname{SU}(2)$ having trace $W_C$; for a negative occurrence it is $-\operatorname{tr}(T_aA_C')$. This follows from $X_a u^{-1}=-u^{-1}T_a$ and cyclic trace invariance. The Pauli expression above gives $\sum_a|\operatorname{tr}(T_aA_C)|^2=1-W_C^2/4$. There are exactly $\ell$ used fine edges. Insert this identity in (5); centering leaves derivatives unchanged. The exact energy and its lower and upper bounds follow. Divide using $\alpha\leq d_C\leq4$ to obtain (50).

These bounds are for the same density used by the block projection. For an additional consistency check, that coarse density itself has a single-coarse-link conditional lower bound $\alpha$, independent of $m$. Indeed change only the last fine edge of a specified chain, holding all $y$ and all other coarse links fixed in (15). Theorem 2.2 bounds the ratio of the two full densities by $R^2$. Integrating the same $y$ on both sides bounds the ratio $r_m(z_\gamma,z_{\ne\gamma})/r_m(z'_\gamma,z_{\ne\gamma})$ by $R^2$. Averaging over $z'_\gamma$ proves the assertion. This exact argument does not equate single-link conditional bounds with independence or a global Poincare inequality.

### Theorem 7.2.

Define the unnormalized actual full-Hamiltonian spectral measure 

$$
\qquad\text{(51)}
 \mathsf M_C(B)=\langle u_C,\mathbf1_B(H-E_0)u_C\rangle,\qquad
 \mathsf M_C([0,\infty))=d_C.
$$

 No division by $d_C$ is made in this measure. It has no atom at zero. Its full first and second moments satisfy 

$$
\begin{gathered}
 \int\omega\,\mathrm d\mathsf M_C=\kappa\ell(1-r_C/4),\\
 \int\omega^2\,\mathrm d\mathsf M_C
 =\|A_mf_C\|^2+\|B_mf_C\|^2
 \leq C_*^2\kappa^2\ell^2.\qquad\text{(52)}\\
 \Omega_C=\frac{3\alpha}{32}\kappa\ell,\qquad
 c_H=\frac{9\alpha^3}{1024C_*^2}>0,\qquad
 \boxed{\mathsf M_C([\Omega_C,\infty))\geq c_Hd_C.}\qquad\text{(53)}
\end{gathered}
$$

 In particular $c_H$ is independent of the increasing blocking length $m$ and of total box volume. The full compressed resolvent, including its memory, obeys at the scalar shift $z=\kappa\ell$ 

$$
\qquad\text{(54)}
 z\langle f_C,S_{m,z}^{-1}f_C\rangle
 \leq d_C\left[1-c_H\frac{3\alpha/32}{1+3\alpha/32}\right].
$$

### Proof.

The state is smooth and orthogonal to the unique vacuum. Spectral calculus and (49) prove the first moment and the absence of a zero atom. Every used edge has fundamental Casimir $3/4$, including inverse occurrences, so $-\sum_{e,a}X_{e,a}^2W_C=3\ell W_C/4$. Combining (4) with (10) and $|\nabla_e W_C|\leq1$ gives the pointwise bound 

$$
|\mathscr LJ_mf_C|=|\mathscr LJ_mW_C|
 \leq\kappa\ell\left(\frac32+2G\right)=\kappa\ell C_*.
$$

 The second-moment bound follows by integration and (40). In particular the term $\|B_mf_C\|^2$ has not been deleted from this spectral measure.

Put $A=3\alpha/16$. The first moment is at least $A\kappa\ell d_C$ by (50). With $\Omega_C=A\kappa\ell/2$, its part on $[\Omega_C,\infty)$ is at least $A\kappa\ell d_C/2$, since the integral over $[0,\Omega_C)$ is at most $\Omega_C d_C$. Cauchy--Schwarz against the unnormalized $\mathsf M_C$ gives 

$$
(A\kappa\ell d_C/2)^2
 \leq\left(\int\omega^2\,\mathrm d\mathsf M_C\right)
                       \mathsf M_C([\Omega_C,\infty)).
$$

 Using (52) gives the stronger intermediate bound $\mathsf M_C([\Omega_C,\infty))\geq A^2d_C^2/(4C_*^2)$. Since $d_C\geq\alpha$, this is at least $A^2\alpha d_C/(4C_*^2)=c_Hd_C$, with the state mass retained. Finally (35) gives $z\langle f_C,S_{m,z}^{-1}f_C\rangle
=\int z/(\omega+z)\,\mathrm d\mathsf M_C$. On $[\Omega_C,\infty)$ its integrand is at most $z/(\Omega_C+z)$, and elsewhere it is at most $1$. Its upper bound is therefore $d_C-\Omega_C\mathsf M_C([\Omega_C,\infty))/(\Omega_C+z)$. Insert (53) and $z=\kappa\ell$ to obtain (54).

The same channel can be dressed by the complete eliminated resolvent with a quantitative bound that continues to hold for growing $m$. Define 

$$
\qquad\text{(55)}
 \tau_* =\frac{8G}{\sqrt{\alpha c_H}},\qquad
 z_C=\tau\kappa\ell,\quad\tau\geq\tau_*.
$$

 For $f=f_C$ use the full $u_{z_C}$ of (41), with all fine eliminated degrees of freedom in $C_m$.

### Corollary 7.3.

This is a nonzero physical vector with exact norm and energy (42)--(43). Quantitatively, 

$$
\begin{gathered}
 d_C\leq\|u_{z_C}\|^2\leq d_C+\alpha c_H/4,\\
 \|\mathbf1_{[\Omega_C,\infty)}(H-E_0)u_{z_C}\|^2
 \geq\frac{c_H}{4+c_H}\|u_{z_C}\|^2,\qquad\text{(56)}\\
 \frac{\Omega_Cc_H}{4+c_H}
 \leq\frac{\mathfrak q_{H-E_0}[u_{z_C}]}{\|u_{z_C}\|^2}
 \leq\kappa\ell\frac{1-r_C/4}{d_C}.
\end{gathered}
$$

### Proof.

By (23), each used coarse edge contributes at most $4G\kappa m$ to the pointwise absolute value of $B_mf_C$; there are $r$ such edges and $|D_\gamma W_C|\leq1$. Thus $\|B_mf_C\|\leq4G\kappa\ell$. Since $C_m\geq0$, its shifted inverse has norm at most $1/z_C$. Consequently 

$$
\|w_{z_C}\|\leq4G/\tau\leq\tfrac12\sqrt{\alpha c_H}
                              \leq\tfrac12\sqrt{d_Cc_H}.
$$

 Orthogonality gives the norm bound. Multiplication by $\psi$ is unitary, and an orthogonal spectral projection is contractive. Hence the triangle inequality and (53) give 

$$
\|\mathbf1_{[\Omega_C,\infty)}(H-E_0)u_{z_C}\|
 \geq\sqrt{d_Cc_H}-\|w_{z_C}\|
 \geq\tfrac12\sqrt{d_Cc_H}.
$$

 The retained norm satisfies $\|u_{z_C}\|^2=d_C+\|w_{z_C}\|^2\leq d_C(1+c_H/4)$, so the squared lower bound $d_Cc_H/4$ is at least $c_H\|u_{z_C}\|^2/(4+c_H)$. Integrating $\omega\geq\Omega_C$ over this weight proves the lower energy bound; (43) proves the upper bound. The large positive shift here is explicitly fixed in (55); this argument does not assert the same lower bound for the separately defined vector minimizing the energy numerator at $z=0$. Its full Rayleigh variational problem is calculated in Section 8.

## Zero-shift reconstruction and affine physical states 

We now calculate the zero-shift channel without transferring the positive-shift estimate by assertion. Gauge invariance is imposed throughout this section. Let $\mathscr H^{\rm G}$ be the closed subspace of gauge-invariant functions in $\mathscr H$, and let $\mathscr K_m^{\rm G}$ be the corresponding coarse subspace. The gauge group is the compact product $\operatorname{SU}(2)^{\mathsf V_L}$; its Haar average is an orthogonal projection. The intertwining of the path products and the gauge descent of the conditional density show that $J_m,J_m^*,P_m,Q_m$ commute with the corresponding gauge actions. Consequently $B_m,C_m$ and their resolvents preserve these subspaces. All physical vectors below are obtained by the same unitary multiplication by $\psi$.

Take $m\geq2$ dividing $2L$. In this section write $C$ for the restriction of $C_m$ to $\mathscr H_{Q_m}^{\rm G}$, retaining precisely its form domain $\mathscr V_{Q_m}\cap\mathscr H^{\rm G}$. This is a reducing restriction of the operator, not a change of interaction. Put 

$$
c=\inf\sigma(C),\qquad
 \delta_{\rm G}=\inf_{\substack{0\ne u\in\mathscr V\cap\mathscr H^{\rm G}\\\mu u=0}}
                   \frac{q(u,u)}{\|u\|^2}.
$$

 This complementary physical space is nonzero. For example, the fine face at $n=(-L,-L,-L)$ in the first two directions contains the direction-2 edge with first coordinate $-L+1$, which is outside $R_m$. Varying that edge with every other fine edge fixed leaves every coarse product unchanged and changes the fine face trace. Positivity of the conditional density implies $Q_mW_p\ne0$, and this function is gauge invariant. Compact embedding of the restricted form domain into $L^2$ gives compact resolvent for $C$: a bounded sequence in its form norm is bounded in the original $H^1$ norm. Thus $c$ is an eigenvalue.

### Proposition 8.1.

With the original number of fine edges $N=3(2L)(2L+1)^2$, define 

$$
\qquad\text{(58)}
 \Delta_L=\frac{3\kappa}{4}\alpha^N
          =\frac{3g^2}{2a}\alpha^{\,3(2L)(2L+1)^2}.
$$

 Then $\delta_{\rm G}\geq\delta\geq\Delta_L>0$ and $c\geq\delta_{\rm G}$. For mean-zero $f\in\mathscr V_m\cap\mathscr K_m^{\rm G}$, define the linear map 

$$
\qquad\text{(59)}
 \mathcal R_m f=J_mf-C^{-1}B_mf,\quad
 s_{m,0}(f,g)=a_m(f,g)-\langle B_mf,C^{-1}B_mg\rangle.
$$

 The form $s_{m,0}$ is closed on the indicated retained form space, with 

$$
\qquad\text{(60)}
 \Delta_L\|f\|^2\leq s_{m,0}(f,f)\leq a_m(f,f),\qquad
 a_m(f,f)\leq2(1+\eta_m/\Delta_L)s_{m,0}(f,f).
$$

 The map $\mathcal R_m$ takes this space into the original physical mean-zero form domain and satisfies $J_m^*\mathcal R_mf=f$. For every $h\in\mathscr V_{Q_m}\cap\mathscr H^{\rm G}$, 

$$
\qquad\text{(61)}
 q(\mathcal R_m f,h)=0,\qquad
 q(\mathcal R_m f,\mathcal R_m g)=s_{m,0}(f,g).
$$

 For its associated mean-zero operator $S_{m,0}$, the exact domain map is 

$$
\qquad\text{(62)}
 f\in D(S_{m,0})\ \Longleftrightarrow
 \mathcal R_m f\in D(\mathscr L),\qquad
 \mathscr L\mathcal R_m f=J_mS_{m,0}f.
$$

 The equivalence in (62) is for $f$ already in the retained mean-zero form domain.

### Proof.

Change fine variables one at a time between any two configurations. Theorem 2.2 gives $\rho_{\max}/\rho_{\min}\leq R^{2N}=\alpha^{-N}$. The product Haar Laplacian has first positive eigenvalue $3/4$: tensor products of the complete matrix-coefficient bases in Lemma 2.1 have eigenvalues $\sum_e j_e(j_e+1)$, whose least positive value is $3/4$. Expanding a smooth function in that basis, and then using $H^1$ density, gives the Haar Poincare inequality. Hence 

$$
\operatorname{Var}_\mu u
 \leq\rho_{\max}\operatorname{Var}_\lambda u
 \leq\frac{4\rho_{\max}}3\sum_{e,a}\int|X_{e,a}u|^2\,\mathrm d\lambda
 \leq\frac{4\rho_{\max}}{3\kappa\rho_{\min}}q(u,u).
$$

 The first inequality evaluates the infimum over constants defining $\operatorname{Var}_\mu$ at the Haar mean. This proves (58) for all mean-zero functions, and restricting to gauge-invariant functions preserves the lower bound. Every complementary physical function has zero mean, so $c\geq\delta_{\rm G}$.

The bounded resolvent $C^{-1}$ maps its Hilbert space to $D(C)$ and therefore to the form domain. Completing the square at zero gives 

$$
q(J_mf+h,J_mf+h)
 =s_{m,0}(f,f)+c_m(h+C^{-1}B_mf,h+C^{-1}B_mf).
$$

 The unique minimizer is $\mathcal R_m f$, proving (61) and the upper bound in (60). Its mean is zero and its squared norm is $\|f\|^2+\|C^{-1}B_mf\|^2$. The already proved full Poincare inequality gives the lower bound and $\|\mathcal R_m f\|^2\leq s_{m,0}(f,f)/\Delta_L$. Apply (27) to $\mathcal R_m f$ for the second inequality in (60). These two-sided form-norm bounds prove closedness with exactly the retained $H^1$ domain.

If $f\in D(S_{m,0})$, decompose any physical form test vector as $J_mg+h$. Equations (61) give 

$$
q(J_mg+h,\mathcal R_m f)=s_{m,0}(g,f)
                       =\langle J_mg+h,J_mS_{m,0}f\rangle .
$$

 Constants give zero on both sides. This is the defining weak operator identity. It also holds against arbitrary, noninvariant test vectors: average that test vector over the gauge group, since the operator and the vector being tested are invariant. Thus $\mathcal R_m f$ belongs to the full $D(\mathscr L)=H^2$ and has the displayed image. Conversely if $\mathcal R_m f\in D(\mathscr L)$, tests in the complementary space show $Q_m\mathscr L\mathcal R_m f=0$; retained tests then prove $f\in D(S_{m,0})$ and the claimed image.

The exponential dependence on $N$ in (58) is explicit. It provides a proved finite-box inverse bound, not a volume-uniform gap.

Fix a nonzero, mean-zero, gauge-invariant $f\in\mathscr V_m$. Keep its norm unchanged and set 

$$
d_f=\|f\|^2,\quad a_f=a_m(f,f),\quad b_f=B_mf,\quad
 \sigma_f(I)=\|\mathbf1_I(C)b_f\|^2 .
$$

 This $\sigma_f$ is a finite positive measure on $[c,\infty)$ of total mass $\|b_f\|^2$, with no division by that mass. For every real $z>-c$, put 

$$
\qquad\text{(63)}
 M_j(z)=\int_{[c,\infty)}(t+z)^{-j}\,\mathrm d\sigma_f(t),\quad j=1,2,3,
 \qquad v_z=J_mf-(C+z)^{-1}b_f .
$$

 All these moments are finite by $t+z\geq c+z>0$.

### Theorem 8.2.

The actual physical state $\psi v_z$ has exact squared norm, excitation energy and Rayleigh quotient 

$$
\qquad\text{(64)}
 N_f(z)=d_f+M_2(z),\quad
 e_f(z)=a_f-M_1(z)-zM_2(z),\quad
 Q_f(z)=\frac{e_f(z)}{N_f(z)}.
$$

 For all $z>-c$, 

$$
\qquad\text{(65)}
 Q_f'(z)=\frac{2M_3(z)}{N_f(z)}[z+Q_f(z)].
$$

 In particular $Q_f$ is strictly increasing on $[0,\infty)$ whenever $b_f\ne0$. Its zero-shift value is strictly smaller than the lifted quotient $a_f/d_f$, and some negative shifts give a quotient strictly smaller still. Zero shift minimizes the energy numerator at fixed retained data, but it does not minimize the physical quotient when $b_f\ne0$.

The full affine variational problem, with all physical eliminated states allowed, is determined as follows: 

$$
\begin{gathered}
 \chi_f=\inf_{h\in\mathscr V_{Q_m}\cap\mathscr H^{\rm G}}
           \frac{q(J_mf+h,J_mf+h)}{d_f+\|h\|^2},\\
 F_f(E)=a_f-E d_f-M_1(-E),\qquad 0\leq E<c,\qquad
 F_f'(E)=-d_f-M_2(-E)<0,\qquad\text{(66)}\\
 F_f(0)>0,\quad
 \mathfrak l_f=\lim_{E\uparrow c}F_f(E)\in[-\infty,\infty).
\end{gathered}
$$

 If $\mathfrak l_f<0$, there is exactly one root $E_f\in(0,c)$ and 

$$
\begin{gathered}
 \chi_f=E_f,\qquad
 h_f=-(C-E_f)^{-1}b_f,\qquad
 \|\psi(J_mf+h_f)\|^2=-F_f'(E_f),\\
 \mathfrak q_{H-E_0}[\psi(J_mf+h_f)]=-E_fF_f'(E_f).
 \qquad\text{(67)}
\end{gathered}
$$

 This is the unique affine minimizer. If $\mathfrak l_f\geq0$, then $\chi_f=c$. In this case $b_f$ is orthogonal to $\ker(C-c)$. The value $c$ is attained exactly when $\mathfrak l_f=0$, and all minimizers are 

$$
\qquad\text{(68)}
 h=-(C-c)^\dagger b_f+k,\qquad k\in\ker(C-c).
$$

 Here the dagger is the inverse on $\ker(C-c)^\perp$ and zero on the kernel. When $\mathfrak l_f>0$, no finite affine vector attains $c$; the infimum is approached by $h=t k$, $t\to\infty$, for a nonzero $k\in\ker(C-c)$. These alternatives are exhaustive for the actual interacting $C$ and $b_f$, including $b_f=0$.

### Proof.

The spectral theorem identifies $M_1$ with $\langle b_f,(C+z)^{-1}b_f\rangle$ and $M_2$ with $\|(C+z)^{-1}b_f\|^2$. The orthogonal decomposition of $v_z$ and the block form (32) prove (64) for negative as well as positive $z$. Differentiating these bounded resolvents gives $M_1'=-M_2$, $M_2'=-2M_3$, $N_f'=-2M_3$, and $e_f'=2zM_3$. The quotient rule proves (65). Each $v_z$ is nonzero and mean-zero, so $Q_f(z)\geq\delta_{\rm G}>0$. For $b_f\ne0$, $M_3>0$ and the derivative is positive at zero and at every positive shift. Also 

$$
\frac{a_f}{d_f}-Q_f(0)
 =\frac{M_1(0)+(a_f/d_f)M_2(0)}{d_f+M_2(0)}>0 .
$$

 Continuity of the derivative at zero proves strict improvement for sufficiently small negative shifts. The statement about the numerator follows independently from (61); increasing the norm is part of the exact quotient calculation.

For $0\leq E<c$, complete the shifted square for arbitrary $h$: 

$$
\qquad\text{(69)}
 q(J_mf+h,J_mf+h)-E(d_f+\|h\|^2)
 =F_f(E)+\|(C-E)^{1/2}[h+(C-E)^{-1}b_f]\|^2.
$$

 No discarded term or approximation enters this identity. The sign and derivative statements in (66) follow from Proposition 8.1 and the spectral derivative. Monotonicity bounds the limit above by $F_f(0)$ and allows the value $-\infty$ below. The intermediate value theorem proves the unique root when the limit is negative. At this root (69) bounds every quotient below by $E_f$, and equality holds precisely for the stated $h_f$. The norm and energy in (67) follow from (64) and $F_f(E_f)=0$.

If the limit is nonnegative, $F_f(E)>0$ for every $E<c$. Equation (69), followed by $E\uparrow c$, bounds every affine quotient below by $c$. A complementary eigenvector $k$ of eigenvalue $c$ yields 

$$
\frac{a_f+2t\operatorname{Re}\langle b_f,k\rangle+t^2c\|k\|^2}
      {d_f+t^2\|k\|^2}\longrightarrow c,
$$

 proving equality of the infimum. If $b_f$ had a nonzero projection on that eigenspace, its contribution to $M_1(-E)$ would diverge as $(c-E)^{-1}$, contradicting $\mathfrak l_f\geq0$. Compact resolvent isolates $c$ from the rest of $\sigma(C)$, so $(C-c)^\dagger$ is bounded on the complementary eigenspaces and maps into $D(C)$. Completing the square at $E=c$ now gives 

$$
q(J_mf+h,J_mf+h)-c(d_f+\|h\|^2)
 =\mathfrak l_f+
 \|(C-c)^{1/2}[h+(C-c)^\dagger b_f]\|^2 .
$$

 It proves both the attainment criterion and every vector in (68).

The scalar root in (66) solves the affine problem for this fixed retained direction. It is not, in general, an eigenvalue of the full operator: a full eigenvector also requires the weak equation $s_{m,-E}(g,f)=0$ for every retained test direction $g$. Here $s_{m,-E}$ denotes the sesquilinear expression (34) at $z=-E$, restricted to physical retained functions; it is well defined on $\mathscr V_m\cap\mathscr K_m^{\rm G}$ because $E<c$. Indeed complementary testing gives $h=-(C-E)^{-1}B_mf$, and retained testing gives exactly that additional equation. Conversely these equations imply the full weak eigenvector equation and its $H^2$ operator domain. This proves the exact map in both directions, and explains precisely which test directions the affine minimization uses. The energy-dependent eigenvalue and reconstruction principle agrees with [\[1, Theorem 1.2 and Corollary 1.3\]](https://doi.org/10.4171/ECR/18-1/5); the affine classification and the physical domains above were proved directly.

### Corollary 8.3.

For the loop $f=f_C$, the zero-shift state $u_0=\psi\mathcal R_m f_C$ obeys the exact identities 

$$
\begin{aligned}
 \|u_0\|^2&=d_C+M_2(0),\\
 \mathfrak q_{H-E_0}[u_0]&=\kappa\ell(1-r_C/4)-M_1(0).
 \qquad\text{(70)}
\end{aligned}
$$

 

$$
\begin{gathered}
 \alpha\leq d_C\leq\|u_0\|^2
 \leq d_C+\min\left\{
       \frac{\kappa\ell(1-r_C/4)}{\Delta_L},
       \frac{16G^2\kappa^2\ell^2}{\Delta_L^2}\right\},
 \qquad\text{(71)}\\
 \|u_0\|^2\leq4+\frac{4\ell}{3\alpha^N},\\
 \Delta_L\leq
 \frac{\mathfrak q_{H-E_0}[u_0]}{\|u_0\|^2}
 \leq\frac{\kappa\ell(1-r_C/4)}{d_C}.\qquad\text{(72)}
\end{gathered}
$$

 For an elementary coarse face, the last norm bound is $4+16m/(3\alpha^N)$, and its energy numerator is exactly $8g^2m(1-r_C/4)/a-M_1(0)$. The same $\Delta_L=3g^2\alpha^N/(2a)$ bounds the quotient below. These bounds are finite and explicit; their volume dependence is retained.

### Proof.

The identities are (64) at zero. Positivity gives $M_1(0)\leq a_f$, and the spectral inequality $t^{-2}\leq c^{-1}t^{-1}$ gives $M_2(0)\leq a_f/c\leq a_f/\Delta_L$. The other estimate uses $M_2(0)\leq\|B_mf_C\|^2/\Delta_L^2$ and the already proved $\|B_mf_C\|\leq4G\kappa\ell$. Insert $a_f=\kappa\ell(1-r_C/4)\leq\kappa\ell$ and $d_C\leq4$. The lower quotient bound is the full Poincare inequality, and the upper one follows from the exact numerator and norm. Finally use $\ell=4m$ and $\kappa=2g^2/a$.

## Exact comparison of all physical low-energy states 

The previous section treated a fixed retained observable. We now give a quantitative relation encompassing all physical states, with no assumed complementary gap uniform in volume. Define the actual zero-shift reconstructed infimum 

$$
\qquad\text{(73)}
 \lambda_m^{\rm R}
 =\inf_{\substack{0\ne f\in\mathscr V_m\cap\mathscr K_m^{\rm G}\\\mu_m f=0}}
 \frac{s_{m,0}(f,f)}
      {\|f\|^2+\|C^{-1}B_mf\|^2}.
$$

 This denominator is the full physical norm. In every fixed box it is positive, and $\lambda_m^{\rm R}\geq\delta_{\rm G}\geq\Delta_L$.

### Theorem 9.1.

For every allowed $L,m,a,g$ with $m\geq2$, the following comparison holds with numerical constants independent of all four parameters: 

$$
\qquad\text{(74)}
 \frac{\lambda_m^{\rm R}c}{\lambda_m^{\rm R}+c}
 \leq\delta_{\rm G}\leq\min\{\lambda_m^{\rm R},c\},\qquad
 \frac12\min\{\lambda_m^{\rm R},c\}\leq\delta_{\rm G}.
$$

 It has the following explicit state map. For every mean-zero physical $u\in\mathscr V$, put 

$$
\qquad\text{(75)}
 f=J_m^*u,\quad v=\mathcal R_m f,\quad
 k=u-v=Q_mu+C^{-1}B_mf .
$$

 Then $k\in\mathscr V_{Q_m}\cap\mathscr H^{\rm G}$ and 

$$
\qquad\text{(76)}
 q(u,u)=s_{m,0}(f,f)+c_m(k,k),\qquad
 \|u\|^2=\|v\|^2+\|k\|^2+2\operatorname{Re}\langle v,k\rangle .
$$

 At least one of the nonzero components $v,k$ has physical Rayleigh quotient at most $2q(u,u)/\|u\|^2$. Conversely each such component is an actual admissible physical state under multiplication by $\psi$.

For every sequence of allowed boxes, block lengths, positive spacings and couplings, $\delta_{\rm G}$ tends to zero if and only if $\min\{\lambda_m^{\rm R},c\}$ tends to zero. Uniform positive lower bounds for $\delta_{\rm G}$ are equivalent to simultaneous uniform positive lower bounds for these two actual sector infima. These are equivalences proved by (74), not assumed estimates for either sector.

### Proof.

Sobolev preservation of $J_m^*$ and Proposition 8.1 make all components in (75) well defined in their stated form domains. The identity $J_m^*v=f$ puts $k$ in the complement. Equation (61) gives $q(v,k)=0$, which proves the energy identity; the norm identity retains its cross term. Cauchy--Schwarz in two scalar components gives 

$$
\|u\|\leq\|v\|+\|k\|
 \leq\sqrt{\frac{q(v,v)}{\lambda_m^{\rm R}}}
      +\sqrt{\frac{c_m(k,k)}c}
 \leq\sqrt{\left(\frac1{\lambda_m^{\rm R}}+\frac1c\right)q(u,u)}.
$$

 Zero components contribute zero. Taking the infimum over $u$ proves the first lower bound. The upper bound follows because the full variational set contains both the reconstructed vectors and all complementary physical vectors. For positive $x,y$, $xy/(x+y)\geq\min(x,y)/2$, proving the last bound.

For the explicit factor-two state assertion, $\|u\|^2\leq2(\|v\|^2+\|k\|^2)$ and the energy identity show 

$$
\min_{\substack{w\in\{v,k\}\\w\ne0}}
       \frac{q(w,w)}{\|w\|^2}
 \leq\frac{q(v,v)+q(k,k)}{\|v\|^2+\|k\|^2}
 \leq2\frac{q(u,u)}{\|u\|^2}.
$$

 This construction changes no physical coefficient or state norm. All assertions about sequences and uniform bounds follow directly from the two-sided inequalities for each member of the sequence.

This comparison calculates how a putative collective low-energy sector must appear under the exact block map: it appears either among the full zero-shift reconstructed states, with their eliminated norm retained, or among physical states in the complementary sector. The decomposition (75) exhibits the vectors and controls their energy quotients by the numerical factor two. It does not assert which alternative occurs in the interacting large-volume limit, or that either one actually becomes soft. The fixed-loop high-energy fraction in Theorem 7.2 continues to hold in its full scope. Equations (70)--(72) and Theorem 9.1 now supply the proved zero-shift and all-state relations without extending that fraction to an unsupported family of vectors. For $m=1$, $J_1$ is the identity, $Q_1=B_1=0$, and reconstruction is the identity; the physical gap relation is then exactly $\lambda_1^{\rm R}=\delta_{\rm G}$ with no complementary sector.

## Physical skeleton morphism and uniform complementary inverse 

This section uses the complete fixed-point and physical-resolvent proof retained in `references/LANE_A_ELIMINATION_INPUTS.md`, Sections 1, 10, 11, 12 and 15. The input concerns the identical open box, every original link and face, and the actual positive unit vacuum. Here is its exact dictionary. Its $g_{\rm YM}$ is our $g$, its $\mathcal E$ is our $E_0$, and its coordinate action $\alpha_h(U)_e=h_{s(e)}U_eh_{t(e)}^{-1}$ obeys 

$$
(h\cdot U)_e=h_{s(e)}^{-1}U_eh_{t(e)}
                  =(\alpha_{h^{-1}}U)_e.
$$

 Thus its Hilbert-space representation $\mathsf T_hu=u\circ\alpha_{h^{-1}}$ is exactly $\mathsf T_hu(U)=u(h\cdot U)$ here. The identity map on functions intertwines these representations, on $L^2$, $H^1$ and $H^2$; no assertion that parameter inversion is a group homomorphism is needed. The two Hamiltonians and their domains coincide. Uniqueness of the positive unit vacuum then proves equality of the two $\psi$, of $\rho=\psi^2$, and of the ground energies. The source scalar in its (12.7) will be written $c_{\rm vac}=\langle1,\psi\rangle$ here; it is not the density constant $\alpha$ in (58).

For precision, the proved input is 

$$
\qquad\text{(77)}
 \delta_{\rm G}\geq\Delta_{\rm sc}
 :=3\kappa\left(1-\frac{512}{3}\xi\right)
 =\kappa(3-512\xi)\geq\frac{287\kappa}{96},
 \qquad 0<\xi\leq\frac1{49152}.
$$

 Its entire proof is retained, not a proposed additional hypothesis. The exact source construction maps a collection of nonconstant Haar sectors $z_I$ to $\phi=e^{\mathfrak C}1$, where $\mathfrak C=\sum_{I\ne\varnothing}|z_I\rangle\langle1_I|
\otimes I_{I^c}$ is bounded and nilpotent in each finite box. The inverse is $e^{-\mathfrak C}$, with both exponentials finite polynomials preserving $D(H_0)=H^2$. Its full fixed-point proof gives 

$$
\psi=c_{\rm vac}\phi,\quad
 c_{\rm vac}>0,\quad c_{\rm vac}^2\|\phi\|^2=1,\quad
 e^{-\mathfrak C}(H-E_0)e^{\mathfrak C}=H_0+\mathcal K,
 \qquad H_0=\kappa\sum_eE_e.
$$

 These maps preserve the vacuum scalar and all of $2bM$ in the eigenvalue equation. The source proves that every iterate, hence both similarities, commutes with every vertex gauge transformation. In the orthogonal sector decomposition a physical nonempty support has no degree-one vertex: averaging at such a vertex would give both the same invariant vector and its zero one-link Haar average. Every nonempty surviving support therefore contains at least four edges of this open bipartite cubic graph. With the original $E_e$ Casimir, $H_0\geq3\kappa$ on the physical nonconstant sectors. The complete interaction estimate proved there is $\|\mathcal K f\|_{\oplus,1}\leq(512\xi/3)\|H_0f\|_{\oplus,1}$, where $\|f\|_{\oplus,1}=\sum_I\|\Pi_If\|$ and $\|f\|\leq\|f\|_{\oplus,1}\leq2^{N/2}\|f\|$. The retained proof supplies every commutator and counting estimate and the contraction on $\|z\|_*\leq1/16$, with constant at most $11/36$ in the displayed range. The sector norm equivalence is explicitly volume dependent. The physical Neumann resolvent excludes every $0<t<3\kappa(1-512\xi/3)$, transfers under the displayed domain-preserving similarity, and proves (77) for the original self-adjoint operator. No form positivity of a nonunitary similarity or deletion of its norm factors is used.

The retained proof derives numerical constants for the creation method of Yarotsky [\[7\]](https://arxiv.org/abs/math-ph/0411042v1), Section 2, source equations `mmo`, `c1`, `vsum`, `thl`, `sumj`. Its physical-space reference is Baez [\[8\]](https://arxiv.org/abs/gr-qc/9411007v1), the section "Gauge Theory on a Graph," Lemmas 1, 2 and the source lemma `lem2.5`. Baez's link convention $A_e\mapsto h_{t(e)}A_eh_{s(e)}^{-1}$ is related to the input's $U_e\mapsto h_{s(e)}U_eh_{t(e)}^{-1}$ by the involution $\jmath(U)_e=U_e^{-1}$: direct multiplication gives $\jmath(\alpha_hU)_e=h_{t(e)}\jmath(U)_eh_{s(e)}^{-1}$. The pullback is a Haar-unitary map with itself as inverse, preserves $H^1,H^2$ because inversion is a bi-invariant metric isometry, and intertwines each $E_e$. The raw Wilson products in our Hamiltonian are unchanged. Both original TeX sources are retained.

The source conditional complement retains individual fine links. Our complement retains their ordered products. The following proves the exact relation, including the Hilbert and operator domains.

### Proposition 10.1.

Let $2\leq m\mid2L$, $s=(U_e)_{e\in S_m}$, $r=(U_e)_{e\in R_m}$, and define 

$$
\mathcal A_m=\operatorname{SU}(2)^{R_m},\quad
 \bar\rho_R(r)=\int\rho(s,r)\,\mathrm d\lambda_{S_m}(s),\quad
 \mathcal K_R=L^2(\mathcal A_m,\bar\rho_R\lambda_R).
$$

 Let $J_S:\mathcal K_R\to\mathscr H$ be $J_SF(s,r)=F(r)$, with 

$$
(J_S^*u)(r)=\frac{1}{\bar\rho_R(r)}
                \int\rho(s,r)u(s,r)\,\mathrm d\lambda_{S_m}(s),
 \qquad P_S=J_SJ_S^*.
$$

 Write $\mathcal K_R^{\rm G}$ for invariance under the endpoint action of all original vertices. There is a unitary map of physical spaces 

$$
\qquad\text{(78)}
 \iota_m:\mathscr K_m^{\rm G}\longrightarrow\mathcal K_R^{\rm G},
 \qquad (\iota_m f)(r)=f((u_{\gamma,1}\cdots u_{\gamma,m})_\gamma).
$$

 Its inverse on arbitrary $L^2$ classes is 

$$
\qquad\text{(79)}
 (\iota_m^{-1}F)(z)=\int F(\Theta_m^{-1}(v,z))\,\mathrm d\lambda_v(v),
 \quad
 \Theta_m:\mathcal A_m\longrightarrow
 \left(\prod_\gamma\operatorname{SU}(2)^{m-1}\right)\times\mathcal Q_m,
 \quad r\longmapsto(v,z).
$$

 The inverse coordinates are $u_{\gamma,k}=v_{\gamma,k}$ for $k<m$ and $u_{\gamma,m}=(v_{\gamma,1}\cdots v_{\gamma,m-1})^{-1}z_\gamma$. Both maps identify the invariant $H^1$ and $H^2$ spaces, and 

$$
\qquad\text{(80)}
 J_S\iota_m=J_m,
 \qquad J_S^*|_{\mathscr H^{\rm G}}=\iota_mJ_m^*|_{\mathscr H^{\rm G}},
 \qquad P_S|_{\mathscr H^{\rm G}}=P_m|_{\mathscr H^{\rm G}}.
$$

 Consequently the identity on functions is an isometry from the source physical conditional complement for $S=S_m$ onto $\mathscr H_{Q_m}^{\rm G}$. It identifies their full form domains, their complementary operator domains, their operators and their resolvents. In the range (77), 

$$
\qquad\text{(81)}
 C\geq\Delta_{\rm sc} I,\qquad
 \|C^{-1}\|\leq\Delta_{\rm sc}^{-1}
                  \leq\frac{96}{287\kappa}.
$$

### Proof.

The two inverse coordinate compositions and the Haar identity for $\Theta_m$ follow by the exact prefix cancellations already proved for $\Phi_m$, with all $S_m$ factors omitted from both sides of this particular map. Integrating those factors in the density gives 

$$
\bar\rho_R(\Theta_m^{-1}(v,z))=r_m(z),\qquad
 \bar\rho_R\,\mathrm d\lambda_R=r_m(z)\,\mathrm d\lambda_v\,\mathrm d\lambda_m.
$$

 To prove the first equality, perform simultaneously the internal vertex transformations with fixed coarse endpoints as in Section 3; they send $(v,z)$ to $(1,z)$, preserve the marginal by substitution on $S_m$, and leave $z$ unchanged. Integrating in $v$ then identifies the remaining function with the definition of $r_m$.

There is also an $L^2$ proof of the descent, without evaluation on a measure-zero section. For a chain with endpoints fixed, the internal gauge action is $v'_1=u_1h_1$ and $v'_k=h_{k-1}^{-1}u_kh_k$ for $1<k<m$. For fixed input $r$, Haar integration successively over $h_1,\ldots,h_{m-1}$ makes the variables $v'_1,\ldots,v'_{m-1}$ product Haar; the chain product remains $z$. Applying this to every disjoint interior shows that the compact internal gauge average on $L^2(\bar\rho_R\lambda_R)$ is precisely fibre integration in $v$ followed by constant lift. Hence every invariant $F$ equals that lift almost everywhere. The remaining coarse endpoint action is $z_\gamma\mapsto h_x^{-1}z_\gamma h_{x+m\mathbf e_i}$; this proves the full coarse invariance of (79) and the fine invariance of (78). Substitution proves both inverse identities. Moreover 

$$
\|\iota_m f\|_{\mathcal K_R}^2
 =\int |f(z)|^2r_m(z)\,\mathrm d\lambda_v\,\mathrm d\lambda_m
 =\|f\|_{\mathscr K_m}^2.
$$

 No vector is divided by its mass. Smooth coordinate pullback on these compact products preserves each Sobolev order. Differentiating under the compact fibre integral and applying Cauchy--Schwarz bounds the inverse in $H^1$ and $H^2$. Smooth positive weights give the same Sobolev sets in each finite box. Approximation, followed by compact gauge averaging, proves the claimed domain identifications.

The first identity in (80) follows from the coordinate product. For physical $u$, substitution in the conditional integral shows that $J_S^*u$ is invariant under every skeleton endpoint action. In $(v,z)$ coordinates it is therefore independent of $v$ almost everywhere. Its $v$ integral equals $r_m(z)^{-1}\int\rho(s,\Theta_m^{-1}(v,z))
u(s,\Theta_m^{-1}(v,z))\,\mathrm d\lambda_{S_m}\,\mathrm d\lambda_v$, which is exactly $J_m^*u$. This proves the second identity and then the third. It does not assert equality of the projections on all noninvariant vectors.

Thus the two physical complements are the same closed subspace of $\mathscr H$, with the same form $q$, including derivatives in every fine link. Both have form domain $H^1$ intersected with that space. The weak operator-domain rule is, in both presentations, 

$$
\begin{aligned}
 D(C)=\bigl\{u\in H^1\cap\mathscr H_{Q_m}^{\rm G}:{}&
 \text{ there exists }w\in\mathscr H_{Q_m}^{\rm G}\text{ such that}\\
 &q(v,u)=\langle v,w\rangle
 \text{ for every }v\in H^1\cap\mathscr H_{Q_m}^{\rm G}\bigr\},\\
 Cu={}&w.
\end{aligned}
$$

 Equality of the tests, inner products and forms proves equality of the operators and their resolvents, not merely of their formal differential expressions. Finally every vector in the complement has $\mu u=0$, and $\mathcal Uu=\psi u$ is physical and perpendicular to $\psi$. The already-proved (77) applied under this unchanged unitary gives (81).

### Theorem 10.2.

In the range (77), for every mean-zero $f\in\mathscr V_m\cap\mathscr K_m^{\rm G}$, put $b_f=B_mf$, $d_f=\|f\|^2$, $a_f=a_m(f,f)$ and retain the raw measure $\sigma_f(I)=\|1_I(C)b_f\|^2$. Then 

$$
\qquad\text{(82)}
 s_{m,0}(f,f)\geq\Delta_{\rm sc}
              (d_f+\|C^{-1}b_f\|^2),\qquad
 \lambda_m^{\rm R}\geq\Delta_{\rm sc},\quad c\geq\Delta_{\rm sc}.
$$

 For the unchanged mean-centered simple loop $f_C$, let $\ell$ be its fine perimeter and $d_C,r_C$ retain their earlier definitions. The physical zero-shift state $u_0=\psi\mathcal R_m f_C$ has the exact mass and energy 

$$
\begin{aligned}
 \|u_0\|^2&=d_C+\int t^{-2}\,\mathrm d\sigma_{f_C}(t),\qquad\text{(83)}\\
 \mathfrak q_{H-E_0}[u_0]
 &=\kappa\ell(1-r_C/4)-\int t^{-1}\,\mathrm d\sigma_{f_C}(t)
 \geq\Delta_{\rm sc}\|u_0\|^2.\qquad\text{(84)}
\end{aligned}
$$

 Its quantitative upper mass bound is 

$$
\qquad\text{(85)}
 \|u_0\|^2\leq d_C+
 \min\left\{\frac{\kappa\ell(1-r_C/4)}{\Delta_{\rm sc}},
             \frac{16G^2\kappa^2\ell^2}{\Delta_{\rm sc}^2}\right\}
 \leq4+\frac{96\ell}{287}.
$$

 For every $z\geq0$, define $w_z=(C+z)^{-1}b_f$, $N_f(z)=d_f+\|w_z\|^2$ and $e_f(z)=a_f-\int(t+z)^{-1}\,\mathrm d\sigma_f
                    -z\int(t+z)^{-2}\,\mathrm d\sigma_f$. These are the full physical mass and excitation energy of $\psi(J_mf-w_z)$. The exact differences are 

$$
\begin{aligned}
 w_0-w_z&=zC^{-1}(C+z)^{-1}b_f,\qquad\text{(86)}\\
 e_f(z)-e_f(0)&=\int\frac{z^2}{t(t+z)^2}\,\mathrm d\sigma_f(t),
                                                        \qquad\text{(87)}\\
 N_f(0)-N_f(z)&=\int\left(\frac1{t^2}-\frac1{(t+z)^2}\right)
                                      \,\mathrm d\sigma_f(t),    \qquad\text{(88)}\\
 s_{m,z}(f,f)-s_{m,0}(f,f)-zd_f
 &=\int\frac{z}{t(t+z)}\,\mathrm d\sigma_f(t).    \qquad\text{(89)}
\end{aligned}
$$

 Writing $\theta=z/(\Delta_{\rm sc}+z)$, their estimates are 

$$
\begin{aligned}
 \|w_0-w_z\|&\leq\theta\sqrt{a_f/\Delta_{\rm sc}},\\
 0\leq e_f(z)-e_f(0)&\leq\theta^2a_f,\\
 0\leq N_f(0)-N_f(z)&\leq
 \left[1-\left(\frac{\Delta_{\rm sc}}{\Delta_{\rm sc}+z}\right)^2\right]
 \frac{a_f}{\Delta_{\rm sc}},\\
 0\leq s_{m,z}(f,f)-s_{m,0}(f,f)-zd_f&\leq\theta a_f.
                                                        \qquad\text{(90)}
\end{aligned}
$$

 The constants controlling the inverse do not depend on box or block size. The displayed $a_f$, $\ell$, $G$, $\kappa$, raw norms and spectral measures keep their full dependence.

### Proof.

The map $\mathcal R_m$ and its exact domain and energy identities were proved in Proposition 8.1. Its image under $\mathcal U$ is physical and perpendicular to $\psi$. Applying (77) proves (82), including the infimum inequality. The previous exact inverse-moment formulas give (83)--(84). Positivity of $s_{m,0}$ gives $\int t^{-1}\,\mathrm d\sigma_f\leq a_f$. Since $\operatorname{supp}\sigma_f\subset[\Delta_{\rm sc},\infty)$, 

$$
\int t^{-2}\,\mathrm d\sigma_f\leq
 \min\{a_f/\Delta_{\rm sc},\|b_f\|^2/\Delta_{\rm sc}^2\}.
$$

 Insert the original loop identities $a_f=\kappa\ell(1-r_C/4)$, $\|b_f\|\leq4G\kappa\ell$, $d_C\leq4$, $a_f\leq\kappa\ell$ and (77) to prove (85).

The resolvent identity proves (86). Subtraction of the complete energy integrands gives $t^{-1}-(t+z)^{-1}-z(t+z)^{-2}=z^2/[t(t+z)^2]$. The norm subtraction and the definition of $s_{m,z}$ give the remaining exact differences. On the support of the raw measure, $z/(t+z)\leq\theta$ and $1-[t/(t+z)]^2\leq1-[\Delta_{\rm sc}/(\Delta_{\rm sc}+z)]^2$. Apply these inequalities to the corresponding nonnegative integrands and use the preceding inverse-moment bounds. Squaring (86) first proves its norm estimate. This proves every inequality in (90), with no removal of the measure or its total mass $\|B_mf\|^2$.

For an elementary coarse face $\ell=4m$, the last mass bound is $4+384m/287$, and its physical side length remains $ma$. In original parameters the new lower energy scale and range are 

$$
\Delta_{\rm sc}=\frac{2g^2}{a}\left(3-\frac{128}{g^4}\right)
 \geq\frac{287g^2}{48a},\qquad g^4\geq12288.
$$

 The expectation of $H$ is still $E_0N_f(z)+e_f(z)$. This is a statement for the interacting finite boxes, uniform as their sizes vary within this explicit coupling range. It takes no spatial continuum limit and provides no small-$g$ continuation. Every induced score covariance and the full resolvent and time memory remain those of Sections 4--6.

## Original scales and the exact scope of the spectral conclusion

For an elementary coarse face $\ell=4m$. The actual state has 

$$
\begin{aligned}
 \|u_C\|^2&=r_C-(\overline W_C)^2\in[\alpha,4],\qquad\text{(91)}\\
 \mathfrak q_{H-E_0}[u_C]
 &=\frac{8g^2m}{a}\left(1-\frac{r_C}{4}\right)
       \in\left[\frac{6\alpha g^2m}{a},\frac{8g^2m}{a}\right],\qquad\text{(92)}\\
 \frac{\mathfrak q_{H-E_0}[u_C]}{\|u_C\|^2}
 &\in\left[\frac{3\alpha g^2m}{2a},\frac{8g^2m}{a\alpha}\right],
 \qquad \Omega_C=\frac{3\alpha g^2m}{4a}.\qquad\text{(93)}
\end{aligned}
$$

 Here $\alpha=1/(9\,12^{16/g^4})$, and $G,C_*,c_H$ are the explicit functions (7), (53) of $d=4/g^4$. The physical length is $ma$, so $g^2m/a=g^2(ma)/a^2$ as an exact rewriting with no coordinate change. The expectation of the unsubtracted Hamiltonian is 

$$
\langle u_C,Hu_C\rangle
 =E_0(r_C-(\overline W_C)^2)
       +\frac{8g^2m}{a}(1-r_C/4).
$$

 The same scalar $E_0\|u_{z_C}\|^2$ is added to the dressed excitation energy. Also $0\leq E_0\leq2bM$ follows from $H\geq0$ and the constant unit Haar trial vector, whose plaquette means vanish. The original $2bM$ term has not been omitted from $H$.

The exact instantaneous kinetic term has the two metric expressions 

$$
-\kappa m\Delta^T=-(\kappa m/4)\Delta^c,\qquad \kappa m=2g^2m/a.
$$

 If its coefficient is written solely as $2g_m^2/(ma)$, algebra forces $g_m^2=m^2g^2$. This is only the coefficient dictionary for this marginal kinetic form. It does not make (30) and the energy-dependent memory into the original one-plaquette Hamiltonian at a claimed running coupling.

The map from the spatial coarse observable to the quantum theory is exactly $f\mapsto\psi J_mf$, followed by (51); the retained resolvent is (35), and sequential eliminations obey (45). Theorems 7.2 and Corollary 7.3 are statements about that full quantum spectral measure, with no omission of generated interactions. For fixed $g>0$, these particular large-loop channels retain a positive fraction of weight at energies proportional to $g^2m/a$, including the specified fully dressed channels. Their unnormalized spectral mass above the displayed threshold is bounded below by the stated positive multiple of their unchanged squared norm, at every increasing $m$ and fixed $a,g$.

This assertion does not give a lower bound on the support of the whole measure: some weight can lie below $\Omega_C$. Nor does a lower bound on the quotient of this family bound the infimum over all physical states. At variable $g=g(a)$ the constants $\alpha$ and $c_H$ have the explicit coupling dependence above and can tend to zero. The calculation therefore proves neither a continuum mass gap nor a four-dimensional mass-gap counterexample. It supplies an exact extensive block map and an all-positive-coupling, volume-independent quantitative channel result; Theorem 9.1 additionally relates every physical low-energy state to the zero-shift reconstructed and complementary sectors, with parameter-independent comparison constants and explicit state maps. Section 10 now supplies the proved physical lower bound $\Delta_{\rm sc}=\kappa(3-512\xi)$, uniform in box and block size for $0<\xi\leq1/49152$, together with the exact skeleton/complement morphism and full-memory zero-shift bounds. The all-positive-coupling finite bound (58) remains valid with its displayed volume dependence. Neither the comparison nor the exhaustive affine calculation in Theorem 8.2 presumes which sector becomes soft or an answer for the joint spatial continuum limit.

## Primary-source map and reproducibility

The general Feshbach--Schur construction is attributed to its established literature. The locally retained source of Dusson, Sigal and Stamm was read at Theorem 1.2, its reconstruction map, and Eqs. (1.10)--(1.16). Their Corollary 1.3 is the energy-dependent fixed-point formulation. Its full eigenvalue condition tests all retained directions; the scalar affine root (66) tests the fixed retained direction only, as proved after Theorem 8.2. Their operator $H-\lambda$ corresponds here to $\mathscr L+z$, with $\lambda=-z$, their complementary inverse to $(C_m+z)^{-1}$, and their reconstruction to (36). Their effective interaction has the negative sign in (34). The infinite-rank form argument and the conditional coefficients are proved in this paper.

Bakry and Ledoux's reverse Poincare estimate is their Eq. (1.7), with $d(t)=2t$ at curvature bound zero, on pp. 686--687. Our single-edge Markov generator is $\kappa\Delta^T$ and its carré du champ is $\kappa\sum_a(X_af)^2$, giving precisely (8). Its full compact-group proof was included. Simon's locally retained Theorem 1.1 uses the Euclidean generator $-\Delta/2$ and its Brownian-bridge formula. It is a primary reference for positive potential weights, not a theorem identifying Euclidean space with this compact configuration product; the compact parabolic comparison needed here was proved in (11). Mori's projection-memory method provides the historical comparison: its projection is Eq. (2.13) and its exact memory equations are Eqs. (3.1)--(3.10), pp. 430--431. Our evolution uses $-\mathscr L$ on functions with the vacuum inner product; Mori's evolution uses a Liouville operator on dynamical variables. Equation (38) derives the corresponding Euclidean block identity here, including its signs and domains.

The companion exact checker verifies the entire open-box skeleton and path counts on several finite boxes, chain disjointness, nested product paths, every retained loop orientation, exact Pauli rotations and the mixed derivative tensor in explicit noncommuting samples, and exact rational Schur associativity and spectral constants. The zero-shift checker separately verifies physical norm and quotient derivatives, all six interior/boundary and coupled/uncoupled affine examples, the complete energy and norm decomposition, and the harmonic gap comparison in 81 rational interacting block examples. The physical-complement checker additionally verifies noncommuting chain gauge actions, their inverse compositions, the exact original strong-coupling constants, and the full inverse-moment continuity identities and inequalities. These finite checks diagnose algebra; they do not stand in for the all-box proofs above or compute a substitute vacuum. No Lean run or large parallel job is used.

## Material-tensor transfer into interacting local-energy states 

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

## The exact lowest-energy image of the full Fabel tensor 

This section continues the actual tensor map of Section 13 through a spectral projection of the original interacting Hamiltonian. The resulting states are explicitly derived from the full material tensor. Their positive-coupling finite-regulator energy quotients tend to zero. The construction does not identify their changing Hilbert spaces with an interacting four-dimensional continuum theory.

## Full weighted weak-coupling state map

The source proofs retained with this manuscript are *The original finite-box SU(2) Hamiltonian at small positive coupling*, *Actual weak-coupling vacuum, observable and spectral maps*, and *Full-vacuum potential moments and the electric-state graph limit*. We retain their full proofs as authored reference files. Here is the complete dictionary and the additional weighted magnetic calculation.

The original vertex gauge law is $U_e\mapsto h_s^{-1}U_eh_t$. Setting $k_v=h_v^{-1}$ gives exactly the same transformation written $U_e\mapsto k_sU_ek_t^{-1}$ in those sources. Thus their invariant function space is identical, with the identity map on link configurations and wavefunctions. Root the specified tree at $(-L,-L,-L)$, using the first coordinate, in order $1,2,3$, that exceeds $-L$ to select each vertex's parent. If $t_v$ is its ordered root-to-vertex holonomy, put $Z_c=t_{s(c)}U_ct_{t(c)}^{-1}$ for each non-tree chord $c$. The inverse keeps the tree variables and sets $U_c=t_s^{-1}Z_ct_t$. For each fixed tree configuration these chord changes are independent left/right Haar translations. Fubini gives the exact product measure identity. Based gauge invariance removes the tree variables; the remaining gauge action is simultaneous conjugation of every $Z_c$. This constructs the same physical Hilbert space, including the residual constraint.

On real cochains with counting inner products let $d_0$ be the original vertex difference and $d_1$ the oriented four-edge curl. Let $p_v(x)$ be the additive tree integral and 

$$
(Tx)_c=p_{s(c)}(x)+x_c-p_{t(c)}(x),\quad
 G=TT^{\mathsf T},\quad C=d_1\iota,\quad
 R=T^{\mathsf T}G^{-1/2},
$$

 where $\iota$ inserts chords with zero tree entries. Square interchanges of monotone paths prove $\ker T=\ker d_1=\operatorname{im}d_0$ and $T\iota=I$. Consequently $R^{\mathsf T}R=I$, its range is $\ker d_0^{\mathsf T}$, and $d_1R=CG^{1/2}$. Choose an orthogonal matrix $O$ with 

$$
O^{\mathsf T}G^{1/2}C^{\mathsf T}CG^{1/2}O=\Sigma^2,\qquad
 \Sigma=\operatorname{diag}(\sigma_\nu),\quad \sigma_\nu>0.
$$

 Thus the columns of $RO$ are an orthonormal transverse edge basis with curl frequencies $\sigma_\nu$. None of $T,G,C,R,O$ changes the original edge or face inner products.

Write $Z_c=\exp(y_c^\alpha T_\alpha)$, $|y_c|<2\pi$. Outside a Haar-null set these logarithms are unique. For $\Omega_g=\{x:|x_c|<2\pi/g\}$ the exact Hilbert map is 

$$
\qquad\text{(112)}
 (\mathcal B_gF)(x)=
 g^{3r/2}\mathcal J(gx)^{1/2}F(\exp(gx)),\qquad
 \mathcal J(y)=(16\pi^2)^{-r}
 \prod_c\left(\frac{\sin(|y_c|/2)}{|y_c|/2}\right)^2,
$$

 extended by zero off $\Omega_g$, where $r=|\mathsf E_L|-|\mathsf V_L|+1$. Change of variables proves that it is an isometry onto the supported subspace; its adjoint includes the reciprocal density and dilation. Both commute with simultaneous colour rotations.

Fix $L,a,f$ before sending $g$ to zero. Put $W_p= \operatorname{tr}U_p$ as before, $w_p=2-W_p$, $W=\sum_pw_p$, and $W_f=\sum_pf_pw_p$. The vacuum and spectral source proofs give 

$$
\mathcal B_g\psi_g\longrightarrow\Phi_0,\qquad
 \mathcal B_gP_g(I)\mathcal B_g^*\longrightarrow P_0(I)
 \quad\hbox{in operator norm}
$$

 for bounded excitation intervals $I$ whose endpoints avoid the comparison spectrum. Here $P_g(I)=\mathbf1_I(H_g-\mathcal E_g)$ on the physical space and 

$$
H_{\mathrm{osc}}=\frac1a\sum_{\nu,\alpha}
 \left(-2\partial_{z_{\nu,\alpha}}^2+
             \frac{\sigma_\nu^2z_{\nu,\alpha}^2}{8}\right),
 \qquad z^\alpha=O^{\mathsf T}G^{-1/2}x^\alpha .
$$

 The density and constant Jacobian in this linear coordinate map remain part of the unitary representation. In $z$ coordinates the unit Gaussian has variance $2/\sigma_\nu$ in each real coordinate and ground energy $\mu_0=3\sum_\nu\sigma_\nu/(2a)$.

For specificity, these convergence statements follow from the full operator, as follows. The full potential has a unique zero at all $Z_c=I$, by the contained-square path argument, and its Taylor term is $\frac14\sum_\alpha\|Cy^\alpha\|^2$. It bounds $c|y|^2$ from below in a fixed small chart and has positive minimum $c_\rho$ outside that chart. A vector with bounded original energy has chart-tail mass bounded by $2aK/(cR_0^2)+2aKg^2/c_\rho$ outside $|x|\le R_0$. Local ellipticity gives a local $H^1$ bound, so Rellich compactness and that tail estimate give global $L^2$ compactness. Cut-off invariant oscillator eigenfunctions give the min--max upper bound. The exact partition-of-unity identity for the full kinetic form has error $O_{L,\rho}(g^2)$; the exterior potential and interior quadratic comparison give the lower bound on each finite eigenvalue. The bounded-energy compactness identifies every subsequential eigenvector limit. Equality of finite ranks then proves the stated finite spectral projection convergence. Positivity fixes the vacuum phase. The retained source files contain the complete form estimates, domains, cutoffs and min--max calculation.

The electric graph result for arbitrary real $f_e$ is 

$$
\mathcal B_g\left(g^2\sum_ef_eE_e\psi_g\right)
 \longrightarrow
 -\sum_{\alpha,c,d}(T\operatorname{diag}(f_e)T^{\mathsf T})_{cd}
              \partial_{x_c^\alpha}\partial_{x_d^\alpha}\Phi_0 .
$$

 Its derivative control comes from the vacuum equation and all potential moments, not vacuum $L^2$ convergence alone. Indeed $\sum_{e,\alpha}|X_{e,\alpha}W|^2\le16W$ follows from $\sum_\alpha|X_{e,\alpha}w_p|^2=w_p-w_p^2/4$ and at most four incident faces. The ground-state transform applied to $W^{k/2}$, with positive regularization, gives 

$$
b\langle W^{k+1}\rangle
 \le\mathcal E_g\langle W^k\rangle+4\kappa k^2\langle W^{k-1}\rangle.
$$

 At fixed $L,a$, $\mathcal E_g$ is bounded. Hence every $\langle(W/g^2)^k\rangle$ is bounded. This proves strong convergence of $(W/g^2)\psi_g$ by local Taylor expansion and its third-moment tail bound. The vacuum equation gives the strong graph limit for $g^2\sum_eE_e\psi_g$. The strongly commuting nonnegative link Casimirs obey $\|\sum_ef_eE_eF\|\le\|f\|_\infty\|\sum_eE_eF\|$. Apply this inequality to $\psi_g-\mathcal B_g^*(\chi_{R_0}\Phi_0)$, use convergence of all differentiated coefficients on the fixed compact support, and then let $R_0$ grow. Gaussian graph decay proves the displayed arbitrary-weight limit.

The missing magnetic-weight extension is also strong: 

$$
\qquad\text{(113)}
 \mathcal B_g((W_f/g^2)\psi_g)
 \longrightarrow \frac14\sum_\alpha
 (Cx^\alpha)^{\mathsf T}\operatorname{diag}(f_p)Cx^\alpha\Phi_0.
$$

 To prove it, use the exact inequality $|W_f|\le\max_p|f_p|\,W$. The same third-moment tail estimate controls its squared norm outside every chart ball. On a fixed ball every face word has its full Taylor limit; finite summation, strong vacuum convergence and bounded local multipliers give the limit there. The limiting quadratic Gaussian has an integrable squared tail. These statements prove (113) globally, for signed weights as well as positive weights.

Define the full matrices 

$$
\begin{aligned}
 A_f&=O^{\mathsf T}R^{\mathsf T}\operatorname{diag}(f_e)RO,
 \qquad
 M_f=O^{\mathsf T}R^{\mathsf T}d_1^{\mathsf T}
                  \operatorname{diag}(f_p)d_1RO, \\
 \mathsf R_f&=\Sigma^{-1/2}M_f\Sigma^{-1/2}
                   -\Sigma^{1/2}A_f\Sigma^{1/2}. \qquad\text{(114)}
\end{aligned}
$$

 All magnetic edge averages are the original $f_p=\frac14\sum_{\partial p}f_e$. Combining both graph limits with $\kappa=2g^2/a$ and $b=1/(2g^2a)$ proves the actual raw centered-vector limit 

$$
\qquad\text{(115)}
 \mathcal B_g\Xi_f\longrightarrow
 V_f=\frac1{4a}\sum_{\nu,\eta}(\mathsf R_f)_{\nu\eta}
       \sum_{\alpha=1}^3
       a_{\nu,\alpha}^\dagger a_{\eta,\alpha}^\dagger\Phi_0 .
$$

 Here $z_{\nu,\alpha}=\sqrt{2/\sigma_\nu}
(a_{\nu,\alpha}+a_{\nu,\alpha}^\dagger)$, with the usual commutator equal to $\delta_{\nu\eta}\delta_{\alpha\beta}$. To check the coefficient, differentiating the Gaussian makes the electric centered creation coefficient $-\Sigma^{1/2}A_f\Sigma^{1/2}/(4a)$. The magnetic quadratic is $\sum_\alpha z_\alpha^{\mathsf T}M_fz_\alpha/(8a)$; its centered creation coefficient is $\Sigma^{-1/2}M_f\Sigma^{-1/2}/(4a)$. The scalar expectations converge by inner products with the converging unit vacuum. This retains both terms and their cancellation; for constant $f$ the matrices give $\mathsf R_f=0$, agreeing with $D_f=fH$.

A diagonal colour contraction has squared norm $6$, and an off-diagonal contraction has squared norm $3$. Commuting its two annihilators through its two creators proves these values, with different unordered pairs orthogonal. Thus the full limiting raw measure is 

$$
\qquad\text{(116)}
 \nu_{f,0}=\frac3{8a^2}\sum_\nu(\mathsf R_f)_{\nu\nu}^2
                       \delta_{2\sigma_\nu/a}
 +\frac3{4a^2}\sum_{\nu<\eta}(\mathsf R_f)_{\nu\eta}^2
                       \delta_{(\sigma_\nu+\sigma_\eta)/a}.
$$

 Its total mass is $3\operatorname{tr}(\mathsf R_f^2)/(8a^2)$ and its first moment is $3\operatorname{tr}(\Sigma\mathsf R_f^2)/(4a^3)$. Strong vector convergence and finite spectral projection convergence, followed by a finite comparison-energy cutoff, prove weak convergence of the actual raw measures with total-mass convergence. We do not infer convergence of an unbounded energy test from weak convergence. For the bounded spectral intervals used below, the projected energy moments do converge.

## All open-boundary coefficients in the lowest mode block

Put $N=2L+1$, $h=\pi/(2N)$, $s=2\sin h$, and $\sigma=\sqrt2s$. The one-dimensional vertex and edge functions, in the original coordinates, are 

$$
\begin{aligned}
 v_0(n)&=N^{-1/2},\quad
 v_1(n)=-\sqrt{2/N}\sin(\pi n/N), &&-L\le n\le L,\\
 w_1(n)&=-\sqrt{2/N}\cos(\pi(n+\tfrac12)/N), &&-L\le n<L.
\end{aligned}
$$

 Finite geometric sums prove their unit norms, orthogonality of $v_0,v_1$, and $dv_1=sw_1$, $d^*w_1=sv_1$ with the open endpoints. For each cyclic triple $(i,p,q)=(1,2,3),(2,3,1),(3,1,2)$ define the edge cochain $V_i$ by its only two nonzero directional components: 

$$
\qquad\text{(117)}
 (V_i)_p(n)=\frac{v_0(n_i)w_1(n_p)v_1(n_q)}{\sqrt2},\qquad
 (V_i)_q(n)=-\frac{v_0(n_i)v_1(n_p)w_1(n_q)}{\sqrt2}.
$$

 The exact vertex divergence cancels between the two components. Tensor products give $\langle V_i,V_j\rangle=\delta_{ij}$. Their curls have disjoint face-plane supports and squared norms $\sigma^2$. For example $d_1V_1$ on plane $23$ is $-\sigma v_0(n_1)w_1(n_2)w_1(n_3)$; the other two signs follow from the same original positive face ordering. These are precisely the three lowest transverse modes: the full frequency list is $\sigma_{\mathbf j}^2=\sum_i4\sin^2(\pi j_i/(2N))$, $0\le j_i\le N-1$, with multiplicity $k-1$ for $k\ge2$ positive indices. It follows by tensoring the one-dimensional difference bases; curl on a fixed index triple has squared form $|s|^2|v|^2-|s\cdot v|^2$. This also proves completeness and all endpoint counts.

Retain $f_S(e)=m(e)^{\mathsf T}S m(e)$ for real symmetric $S$, $m(e)=n+\mathbf e_i/2$. Define 

$$
\qquad\text{(118)}
 \delta_L=\frac{1-\cot^2h}{8},\qquad
 \mathfrak m_L^2=\frac{\cos^2h}{2N^2\sin^4h}.
$$

### Theorem 14.1.

On the three-mode basis (117), the exact block $\mathsf R_S^{\min}$ of (114) is 

$$
\qquad\text{(119)}
 (\mathsf R_S^{\min})_{ii}=\sigma\delta_L(\operatorname{tr}S-S_{ii}),
 \qquad
 (\mathsf R_S^{\min})_{ij}=\sigma\mathfrak m_L^2S_{ij}\quad(i\ne j).
$$

 The linear map from real symmetric $S$ to this real symmetric block is injective. Its full raw first-physical-band mass is 

$$
\qquad\text{(120)}
 d_{L,a}(S)=\frac{3\sigma^2}{8a^2}
 \left[
 \delta_L^2\sum_i(\operatorname{tr}S-S_{ii})^2+
 2\mathfrak m_L^4\sum_{i<j}S_{ij}^2
 \right].
$$

 It is strictly positive for every $S\ne0$.

### Proof.

Let 

$$
A=\sum_{n=-L}^Ln^2v_1(n)^2,\quad
 B=\sum_{n=-L}^{L-1}(n+\tfrac12)^2w_1(n)^2,\quad
 M=\sum_{n=-L}^Ln\,v_1(n)v_0(n).
$$

 These exact finite sums obey 

$$
\qquad\text{(121)}
 B-A=-\tfrac14\cot^2h,\qquad
 M=-\frac{\sqrt2\cos h}{2N\sin^2h},\qquad M^2=\mathfrak m_L^2.
$$

 Here is a derivation including the endpoint terms. Put 

$$
D_N(t)=\sum_{n=-L}^Le^{int}=\frac{\sin(Nt/2)}{\sin(t/2)},
 \qquad D_{N-1}(t)=\sum_{n=-L}^{L-1}e^{i(n+1/2)t}.
$$

 The second sum equals $D_N(t)\cos(t/2)-\cos(Nt/2)$. Using $\sin^2u=(1-\cos2u)/2$ and $\cos^2u=(1+\cos2u)/2$ gives 

$$
B-A=\frac1N\left[
 -\frac{N(N-1)}4-D_N''(2\pi/N)-D_{N-1}''(2\pi/N)\right].
$$

 Direct differentiation of the displayed quotient and identity yields 

$$
D_N''(2\pi/N)+D_{N-1}''(2\pi/N)
 =\frac{N}{4\sin^2h}-\frac{N^2}4.
$$

 Substitution gives the first equality in (121). The first derivative at $\pi/N$ is 

$$
D_N'(\pi/N)=-\frac{\cos h}{2\sin^2h}.
$$

 This gives the displayed $M$. Thus neither endpoint lattice has been replaced by an integral.

For a face in plane $pq$ its four edge midpoints have mean $c=n+(\mathbf e_p+\mathbf e_q)/2$, and averaging the four full quadratics gives 

$$
f_p=c^{\mathsf T}S c+(S_{pp}+S_{qq})/8 .
$$

 For the mode normal to $i$, parity removes the mixed-coordinate terms in both diagonal expectations. The electric expectation is $(S_{pp}+S_{qq})(A+B)/2+S_{ii}C_0$ and the unit-curl face expectation is $(S_{pp}+S_{qq})(B+1/8)+S_{ii}C_0$, where $C_0=\sum n^2v_0(n)^2$ is retained in both and cancels exactly. Their difference is $(S_{pp}+S_{qq})((B-A)/2+1/8)$, which is $\delta_L(\operatorname{tr}S-S_{ii})$. The common frequency factors in (114) give the diagonal part of (119).

For distinct normal indices $i,j$, the two cochains share one edge direction. The product of their two signed components is minus one half of the squared $w_1$ factor times one $v_0v_1$ factor in each of the other directions. Only the term $2S_{ij}n_in_j$ in the full edge quadratic survives the two odd sums. The electric matrix entry is therefore $-S_{ij}M^2$. Their curls have disjoint face-plane supports, so the magnetic matrix entry is zero even with arbitrary face weights. The negative electric sign in (114) gives the positive off-diagonal entry in (119).

Since $L\ge2$, $0<h\le\pi/10$; hence $\delta_L<0$ and $\mathfrak m_L^2>0$. A zero block first forces every off-diagonal $S_{ij}$ to vanish and then $S_{ii}=\operatorname{tr}S$ for all $i$. Summing gives $\operatorname{tr}S=3\operatorname{tr}S$, so all entries vanish. For an explicit inverse, if $B=\mathsf R_S^{\min}/\sigma$, then $\operatorname{tr}S=\operatorname{tr}B/(2\delta_L)$, $S_{ii}=\operatorname{tr}B/(2\delta_L)-B_{ii}/\delta_L$, and $S_{ij}=B_{ij}/\mathfrak m_L^2$. Finally the six colour contractions at energy $2\sigma/a$ and their squared norms in (116) give (120).

The first physical energy is $\Delta=2\sigma/a$ with multiplicity six. Every one-quantum state transforms as a colour vector and has no invariant component. Among two-quanta states the only energy $\Delta$ comes from the three lowest modes, and rotation invariance of a bilinear tensor forces the scalar colour contraction. The next transverse frequency is $\sqrt3s$: triples $(1,1,1)$ give it, whereas a triple including $2$ has squared frequency at least $(1+4\cos^2h)s^2>3s^2$. All other two-quanta energies are at least $(\sqrt2+\sqrt3)s/a>(11/10)\Delta$. Every state with three or more quanta has energy at least $3\sigma/a>(11/10)\Delta$. Consequently 

$$
I_{L,a}=(\Delta/2,11\Delta/10)
$$

 isolates precisely the first six-dimensional physical comparison space. For $S\ne0$, (115) and spectral projection convergence prove 

$$
\qquad\text{(122)}
 \|P_g(I_{L,a})\Xi_{f_S}\|^2\longrightarrow d_{L,a}(S)>0.
$$

 This is a conclusion for the actual positive-coupling vector, not an assignment of the comparison Gaussian as its vacuum.

## The entire raw state and its lowest-band fraction

Set 

$$
\mathcal N_{L,a}(S)=\frac3{8a^2}\operatorname{tr}(\mathsf R_{f_S}^2).
$$

 This is the limiting squared norm of the entire unchanged tensor state, including all higher mode pairs in (116). It is positive for $S\ne0$, since its lowest block is nonzero. The exact limiting fraction in the first physical band is therefore 

$$
\qquad\text{(123)}
 \rho_{L,a}(S)=
 \frac{d_{L,a}(S)}{\mathcal N_{L,a}(S)}
 =\frac{\operatorname{tr}((\mathsf R_S^{\min})^2)}
        {\operatorname{tr}(\mathsf R_{f_S}^2)}.
$$

 This ratio records two separately retained raw masses; it does not change the vector. Both strong vector and projection convergence prove that the corresponding fraction for $\Xi_{f_S}$ at positive $g$ tends to (123).

There is an explicit lower bound retaining all original modes: 

$$
\qquad\text{(124)}
 1\ge\rho_{L,a}(S)\ge
 \frac{\sigma^2\delta_L^2}{432rL^4}>0,\qquad
 r=4L^2(4L+3).
$$

 To prove it, let $V=RO$ and $Y=d_1V\Sigma^{-1}$. Both are isometries into the original edge and face spaces, respectively. Equation (114) becomes 

$$
\mathsf R_{f_S}=\Sigma^{1/2}
  [Y^{\mathsf T}\operatorname{diag}(f_p)Y
             -V^{\mathsf T}\operatorname{diag}(f_e)V]\Sigma^{1/2}.
$$

 Every original midpoint has squared length at most $B_L=2L^2+(L-\tfrac12)^2<3L^2$. Thus $|f_e|,|f_p|\le B_L\|S\|_{\mathrm{op}}$. Since $\sigma_{\max}^2\le12$, compression and finite-rank Hilbert--Schmidt estimates give 

$$
\operatorname{tr}(\mathsf R_{f_S}^2)
 \le 4\sigma_{\max}^2rB_L^2\|S\|_{\mathrm{op}}^2
 \le432rL^4\|S\|_{\mathrm{op}}^2.
$$

 On the lowest block, $\sum_i(\operatorname{tr}S-S_{ii})^2
=\sum_iS_{ii}^2+(\operatorname{tr}S)^2$. Moreover 

$$
\frac{\mathfrak m_L^2}{|\delta_L|}
 =\frac{4\cos^2h}{N^2\sin^2h\cos(2h)}
 >\frac{16}{\pi^2}>1.
$$

 Here $\cos(2h)>0$, $\cos^2h>\cos(2h)$ and $\sin h<h$ give the strict inequalities. Consequently $\operatorname{tr}((\mathsf R_S^{\min})^2)
\ge\sigma^2\delta_L^2\|S\|_{\mathrm F}^2$. Use $\|S\|_{\mathrm F}\ge\|S\|_{\mathrm{op}}$ to obtain (124). The upper bound follows because the full Hilbert--Schmidt sum contains the lowest block. The displayed lower bound tends to zero at large $L$; it is not an asserted positive volume-uniform spectral fraction.

## The original material endpoint and an actual diagonal

For integers $j\ge2$ retain the original full matrices from Section 13 and set 

$$
\qquad\text{(125)}
 L_j=j^2,\quad a_j=\frac1{100j},\quad z_j=\frac1j,\quad
 \tau_j=\frac{1-j^{-2}}8,\quad S_j=K_{\tau_j}=C_{\tau_j}C_{\tau_j}^{\mathsf T}.
$$

 These times stay on the regular material orbit; no singular matrix is inserted at its endpoint. Each $S_j$ is positive definite because $C_{\tau_j}$ is invertible. In particular the preceding theorem applies. Section 13 proves $j^{-6}S_j\to S_*=\eta\eta^{\mathsf T}$, $\eta=(1/4,3/8,-9/4)^{\mathsf T}$, with every matrix entry retained. Define $d_j=d_{L_j,a_j}(S_j)$, $\Delta_j=2\sigma_j/a_j$, and 

$$
\qquad\text{(126)}
 \mathcal C_*=
 \frac{204976875}{512\pi^2}+\frac{3982500}{\pi^6}>0 .
$$

### Theorem 14.2.

There is a definite sequence of strictly positive dyadic couplings $g_j<1/j$ and actual smooth physical vectors 

$$
\qquad\text{(127)}
 w_j=\mathbf1_{(\Delta_j/2,\,11\Delta_j/10)}
        (H_{g_j,L_j,a_j}-\mathcal E_{g_j,L_j,a_j})
        \,\Xi_{f_{S_j}},
$$

 orthogonal to the actual vacuum, for which 

$$
\begin{aligned}
 j^{-18}\|w_j\|^2&\longrightarrow\mathcal C_*,
 \qquad\text{(128)}\\
 j^{-17}\langle w_j,(H_{g_j,L_j,a_j}-\mathcal E_{g_j,L_j,a_j})w_j\rangle
 &\longrightarrow100\sqrt2\pi\,\mathcal C_*,
 \qquad\text{(129)}\\
 j\,\frac{\langle w_j,(H_{g_j,L_j,a_j}-\mathcal E_{g_j,L_j,a_j})w_j\rangle}
               {\|w_j\|^2}
 &\longrightarrow100\sqrt2\pi .
 \qquad\text{(130)}
\end{aligned}
$$

 No vector is divided by its norm in this construction.

### Proof.

For each fixed $j$, fixed-box eigenvalue convergence and (122) imply that every sufficiently small $g>0$ satisfies the following finite set of strict inequalities. The first six physical excitation energies lie within $\Delta_j/(10j)$ of $\Delta_j$, the seventh exceeds $11\Delta_j/10$, and 

$$
\left|\frac{\|P_g(I_{L_j,a_j})\Xi_{f_{S_j}}\|^2}{d_j}-1\right|<\frac1j.
$$

 Also require $|\|\Xi_{f_{S_j}}\|^2/\mathcal N_{L_j,a_j}(S_j)-1|<1/j$, which follows from the proved full-vector norm convergence. Let $n_j$ be the least positive integer for which $g_j=2^{-n_j}<1/j$ and all these inequalities hold. Their established fixed-box limits prove existence of this integer. This definition asserts no unproved volume-uniform convergence rate or prescribed renormalized coupling law.

The projection in (127) has rank six. Its range consists of smooth physical eigenvectors; it excludes the vacuum, since its energy interval is strictly positive. The norm inequality gives $\|w_j\|^2>(1-1/j)d_j>0$. On that range every excitation eigenvalue differs from $\Delta_j$ by at most $\Delta_j/(10j)$. Expansion in its actual orthonormal eigenbasis therefore gives the exact two-sided bound 

$$
\left|
 \frac{\langle w_j,(H-\mathcal E)w_j\rangle}{\Delta_j\|w_j\|^2}-1
 \right|<\frac1{10j}.
$$

 The basis is used to evaluate the original vector, not to rescale it.

It remains to compute the unchanged raw scale $d_j$. For $N_j=2j^2+1$ and $h_j=\pi/(2N_j)$, the limit $\sin h_j/h_j\to1$ gives 

$$
\frac{\sigma_j^2}{2\pi^2/N_j^2}\to1,\qquad
 \frac{\delta_{L_j}}{N_j^2}\to-\frac1{2\pi^2},\qquad
 \frac{\mathfrak m_{L_j}^2}{N_j^2}\to\frac8{\pi^4},
 \qquad \frac{N_j^2}{a_j^2j^6}\to40000.
$$

 The exact tensor entries give 

$$
\sum_i(\operatorname{tr}S_*-S_{*,ii})^2
 =\frac{333^2+328^2+13^2}{64^2}=\frac{109321}{2048},
 \qquad
 \sum_{i<j}S_{*,ij}^2=\frac{531}{512}.
$$

 Insert these into the full expression (120), using $j^{-6}S_j\to S_*$, to obtain 

$$
j^{-18}d_j\to
 \frac{7500}{\pi^2}\frac{109321}{2048}
 +\frac{3840000}{\pi^6}\frac{531}{512}=\mathcal C_* .
$$

 Moreover $j\Delta_j=400\sqrt2\,j^2\sin(\pi/(4j^2+2))
\to100\sqrt2\pi$. The norm and energy inequalities above now prove all three limits. The additionally retained whole-state norm gives the actual positive-coupling fraction bound 

$$
\frac{\|w_j\|^2}{\|\Xi_{f_{S_j}}\|^2}
 \ge\frac{j-1}{j+1}\,
 \frac{\sigma_j^2\delta_{L_j}^2}{432r_jL_j^4}.
$$

 Its right side is asymptotic to $j^{-10}/(3456\pi^2)$. No limit of the full fraction is inferred from this lower estimate. Every finite Hamiltonian still has $\kappa_j=200jg_j^2$, $b_j=50j/g_j^2$ and $\xi_j=1/(4g_j^4)$, including the full scalar $2b_j|\mathsf P_{L_j}|$. No strong-coupling inverse estimate was used.

If the chosen observable uses physical midpoints $am(e)$ instead, its exact state is $a_j^2w_j$ by linearity of $D_f$, centering and spectral projection. Its raw norm and energy are multiplied by $a_j^4$. Thus their powers become $j^{14}$ and $j^{13}$ with constants $\mathcal C_*/10^8$ and $100\sqrt2\pi\,\mathcal C_*/10^8$. The quotient is identical. This is the full coordinate/unit dictionary, not a silent change of weight.

The construction proves the full morphism from each material tensor through the energy-current state and the actual physical spectral projection. The six-dimensional coefficient map has the explicit inverse in Theorem 14.1. The spectral projection itself is global in space and depends on the full Hamiltonian. It has not been proved to be a local observable map between the changing regulators, nor a dynamical intertwiner of the forced Navier--Stokes solution and source-free Yang--Mills. The compactly supported Navier--Stokes profile is not replaced here by the stationary Fabel material orbit. The next unresolved part of the original objective is a common interacting continuum state/observable construction preserving this low-energy image. The finite-regulator sequence alone does not supply that identification. Section 15 constructs the next common vacuum-plus-band frame with its exact Gram tensor, calculates compact local-energy and Navier--Stokes curvature-state matrix elements, and retains the explicit higher-mode leakage in products. The common full local interacting continuum representation remains unresolved.

## Local energy, curvature profiles, and the common lowest-band map 

The global spectral projection of Section 14 now receives local weighted-energy states and observables. We calculate its entire vacuum-plus-first-band operator, its raw matrix elements against the full Fabel state, and its two physical time scales. We also retain the exact terms that leave this band. A compressed product is not substituted for a product of the original local operators.

## Graph convergence on the actual excited space

All definitions and coefficients of Sections 1, 13 and 14 remain in force. We first extend the vacuum graph calculation to the actual finite physical eigenspaces. At fixed $L,a$, let $u_g$ be an original physical eigenvector, with eigenvalue $e_g$ in a bounded interval and bounded squared norm. Positivity of $u_g$ is not required. For a real smooth multiplier $F$, expand the full kinetic product and use the eigenvalue equation, taking its real part. The exact identity is 

$$
\qquad\text{(131)}
 q_H[Fu_g]-e_g\|Fu_g\|^2
 =\kappa\sum_{e,\alpha}\int |u_g|^2|X_{e,\alpha}F|^2\,dU.
$$

 The terms $F^2|Xu_g|^2$ and $2F\operatorname{Re}(\overline{u_g}Xu_g)XF$ occur on both sides of the integration-by-parts eigenvalue identity; their cancellation proves the formula also for complex $u_g$.

Put $M_k(u_g)=\int W^k|u_g|^2\,dU$. The same regularized powers and the exact bound $\sum|XW|^2\le16W$ used in Section 14 give 

$$
bM_{k+1}(u_g)\le e_gM_k(u_g)+4\kappa k^2M_{k-1}(u_g),
 \qquad bM_1(u_g)\le e_gM_0(u_g).
$$

 Thus for every fixed $k$, $M_k(u_g)/g^{2k}$ is bounded at fixed $L,a$. The constants are uniform over a bounded-energy unit eigenspace. If $\mathcal B_gu_g\to u_0$ strongly and $e_g\to e_0$, the third moment gives the same chart-tail estimate for $(W/g^2)u_g$ as for the vacuum. Local Taylor convergence proves 

$$
\mathcal B_g((W/g^2)u_g)\to V_2u_0,\qquad
 \mathcal B_g(g^2H_0u_g)\to
          (ae_0/2-V_2/4)u_0=Du_0 .
$$

 The second identity is the full eigenvalue equation $g^2H_0u_g=(ae_g/2)u_g-(W/(4g^2))u_g$. For every fixed real edge weight $f$, the strongly commuting Casimir inequality $\|\sum_ef_eE_eF\|\le\|f\|_\infty\|H_0F\|$ and compactly supported Gaussian-polynomial graph approximations prove the arbitrary electric-weight graph limit, exactly as in Section 14. The weighted magnetic limit follows from $|W_f|\le\max_p|f_p|W$. These arguments prove 

$$
\qquad\text{(132)}
 \mathcal B_gD_fu_g\longrightarrow D_f^{\mathrm{osc}}u_0
$$

 in full $L^2$, with the original factors $2/a$ and $1/(8a)$, for every eigenvector limit in any fixed finite physical spectral range.

To obtain this result for a finite spectral frame, choose an eigenbasis of that range along an arbitrary sequence $g\downarrow0$. The retained compactness and projection theorem gives a subsequence on which every basis vector converges. Apply the preceding moment and graph estimates to each vector; bounded finite linear combinations preserve them. The limit identifies the same operator matrix independently of the chosen subsequence and eigenbasis. Therefore the graph conclusion holds for the original finite spectral projections, including degenerate bands, not merely a chosen eigenvector subsequence.

## Exact common coordinates and the whole compressed operator

Let 

$$
\mathcal K=\mathbb C\oplus\operatorname{Sym}_3(\mathbb C),\qquad
 \langle(c,B),(d,E)\rangle_{\mathcal K}
 =\overline c\,d+6\operatorname{tr}(B^*E).
$$

 The factor $6$ is the unchanged creation-vector norm: 

$$
\Phi(B)=\sum_{i,k=1}^3B_{ik}
            \sum_{\alpha=1}^3a_{i,\alpha}^\dagger
                            a_{k,\alpha}^\dagger\Phi_0,
 \qquad \langle\Phi(B),\Phi(E)\rangle=6\operatorname{tr}(B^*E).
$$

 Commuting two annihilators through two creators proves this formula for complex symmetric matrices; off-diagonal entries occur twice in the displayed sum and twice in the matrix trace. Define the comparison isometry $I_{L,a}(c,B)=c\Phi_0+\Phi(B)$ using the three exact lowest modes of Section 14.

Write $P_g$ for the first-band projection on $(\Delta/2,11\Delta/10)$ and $\Pi_g=|\psi_g\rangle\langle\psi_g|+P_g$. For sufficiently small positive $g$ define 

$$
\qquad\text{(133)}
 M_g(c,B)=c\psi_g+P_g\mathcal B_g^*\Phi(B),\qquad G_g=M_g^*M_g.
$$

 Here every adjoint on $\mathcal K$ uses its displayed factor-$6$ inner product. Projection convergence proves $G_g\to I$ in operator norm. In particular $G_g$ is positive definite for small $g$, $M_g$ is a bijection onto the actual seven-dimensional range of $\Pi_g$, and its exact inverse there is 

$$
M_g^{-1}=G_g^{-1}M_g^*,\qquad
 M_g^{-1}M_g=I,\qquad M_gM_g^{-1}=\Pi_g.
$$

 The last equality on the full Hilbert space means the indicated orthogonal projection. These identities follow by multiplication and the equality of the range dimensions. No original vector or frame column is divided by its norm. The complete finite-$g$ Gram tensor $G_g$ is retained.

Put $C_{g,f}=D_f-\langle\psi_g,D_f\psi_g\rangle$. Let $J_f=\Sigma^{1/2}A_f\Sigma^{1/2}$ and $K_f=\Sigma^{-1/2}M_f\Sigma^{-1/2}$ in the notation of (114); here the face matrix $M_f$ is not the Hilbert frame $M_g$. Set 

$$
\mathsf R_f=K_f-J_f,\qquad \mathsf Q_f=K_f+J_f.
$$

 The full centered oscillator operator is 

$$
\qquad\text{(134)}
 C_{0,f}=\frac1{4a}\sum_{\nu,\eta,\alpha}
 \left[(\mathsf R_f)_{\nu\eta}
 (a_{\nu,\alpha}a_{\eta,\alpha}
       +a_{\nu,\alpha}^\dagger a_{\eta,\alpha}^\dagger)
       +2(\mathsf Q_f)_{\nu\eta}
                      a_{\nu,\alpha}^\dagger a_{\eta,\alpha}\right].
$$

 Expand $\partial_z=\sqrt{\sigma}/(2\sqrt2)(a-a^\dagger)$ and $z=\sqrt{2/\sigma}(a+a^\dagger)$ in the full electric and magnetic quadratic forms to obtain this identity. Their vacuum scalar is $3\operatorname{tr}(\mathsf Q_f)/(4a)$; subtracting that scalar gives exactly (134). No magnetic or number-preserving term is discarded.

Use superscript $\min$ for the three-lowest-mode blocks. The resulting exact compressed operator on $\mathcal K$ is 

$$
\qquad\text{(135)}
 \mathcal D_{0,f}(c,B)=
 \left(\frac{3}{2a}\operatorname{tr}(\mathsf R_f^{\min}B),
 \ \frac{c}{4a}\mathsf R_f^{\min}
       +\frac1{2a}(\mathsf Q_f^{\min}B+B\mathsf Q_f^{\min})\right).
$$

 Indeed the pair annihilation gives $6\operatorname{tr}(\mathsf R_f^{\min}B)/(4a)$ in the vacuum, pair creation from the vacuum gives the second component, and the commutator of $\sum Q_{\nu\eta}a_\nu^\dagger a_\eta$ with $\Phi(B)$ is $\Phi(QB+BQ^{\mathsf T})$. Higher-mode terms are outside the compressed range; they will be retained below. The graph result (132) proves 

$$
\qquad\text{(136)}
 \mathcal D_{g,f}:=
 G_g^{-1}M_g^*\Pi_gC_{g,f}\Pi_gM_g
 \longrightarrow\mathcal D_{0,f}
$$

 in the finite-dimensional operator norm. The original compressed operator is self-adjoint for the Gram inner product $G_g$: $G_g\mathcal D_{g,f}=\mathcal D_{g,f}^*G_g$.

## Compact physical supports and all leading spatial factors

For real $h\in C_c(\mathbb R^3)$ use the exact local weights 

$$
f_{h,j}(e)=h(a_jm(e)),\qquad
 f_{h,j}(p)=\frac14\sum_{e\in\partial p}h(a_jm(e)),
 \quad L_j=j^2,\quad a_j=\frac1{100j}.
$$

 These define a finite sum of the original local electric and magnetic operators. A face adjacent to the sampled support is retained whenever its four-edge average is nonzero. Put 

$$
N_j=2L_j+1,\quad \ell_j=a_jN_j,\quad
 H_h=\int_{\mathbb R^3}h(x)\,dx,\quad
 H_{h,ik}=\int_{\mathbb R^3}x_ix_kh(x)\,dx.
$$

 The vertex endpoints remain at $\pm L_ja_j$; $\ell_j$ is the specified difference-basis length $a_j(2L_j+1)$, not a replacement for the endpoint distance.

### Theorem 15.1.

For the full comparison matrices of these local weights, 

$$
\begin{aligned}
 \frac{\ell_j^4}{a_j}\mathsf R_{h,j}^{\min}
 &\longrightarrow4\sqrt2\pi H_h I_3,
 &
 \frac{\ell_j^4}{a_j}\mathsf Q_{h,j}^{\min}
 &\longrightarrow4\sqrt2\pi H_h I_3, \qquad\text{(137)}\\
 \frac{\ell_j^6}{a_j}(\mathsf R_{h,j}^{\min})_{ik}
 &\longrightarrow2\sqrt2\pi^3 H_{h,ik}
 &&(i\ne k). \qquad\text{(138)}
\end{aligned}
$$

 In particular the complete raw first-band mass obeys 

$$
\qquad\text{(139)}
 \ell_j^8d_{L_j,a_j}(f_{h,j})\longrightarrow36\pi^2 H_h^2.
$$

 Here $d(f)$ denotes $3\operatorname{tr}((\mathsf R_f^{\min})^2)/(8a^2)$ for arbitrary weights, extending the quadratic-weight notation of (120).

### Proof.

Let $V_i$ be the original edge functions (117) and $Y_i=d_1V_i/\sigma_j$. Put 

$$
A^h_{ik}=\sum_ef_{h,j}(e)V_i(e)V_k(e),\qquad
 F^h_{ik}=\sum_pf_{h,j}(p)Y_i(p)Y_k(p).
$$

 Then, exactly, $\mathsf R_h^{\min}=\sigma_j(F^h-A^h)$ and $\mathsf Q_h^{\min}=\sigma_j(F^h+A^h)$. Different $Y_i$ have disjoint face-plane supports, so $F^h_{ik}=0$ for $i\ne k$ with any face weight. For the plane $(p,q)$ normal to $i$, 

$$
Y_i(n)^2=\frac4{N_j^3}
 \cos^2\left(\frac{\pi a_j(n_p+1/2)}{\ell_j}\right)
 \cos^2\left(\frac{\pi a_j(n_q+1/2)}{\ell_j}\right).
$$

 The sign of the ordered curl disappears here by squaring; it was not changed. On every fixed physical compact set the two cosine factors tend uniformly to one. The quarter-face sample differs uniformly from $h$ at the face center by at most its modulus of continuity at distance $a_j/2$. The support increases by at most that distance. The face-center Riemann sums with volume factor $a_j^3$ consequently give 

$$
\ell_j^3 F^h_{ii}\longrightarrow4H_h.
$$

 For clarity, uniform continuity bounds each sample error, the number of nonzero samples times $a_j^3$ stays bounded in a fixed enlarged compact cube, and the ordinary shifted cubic partition proves convergence of the remaining Riemann sum. Thus the four edges and the open endpoints contribute no unrecorded limit term.

For $V_i$ on direction $p$ its squared factor is 

$$
\frac2{N_j^3}
 \cos^2\left(\frac{\pi a_j(n_p+1/2)}{\ell_j}\right)
 \sin^2\left(\frac{\pi a_jn_q}{\ell_j}\right),
$$

 and there is the other directional term with $p,q$ interchanged. On a fixed support, $|\sin(\pi x/\ell_j)|\le\pi|x|/\ell_j$. The same sample-count estimate gives $A^h_{ii}=O_h(\ell_j^{-5})$. Cauchy--Schwarz with $|h|$ also bounds every $A^h_{ik}=O_h(\ell_j^{-5})$.

More precisely, distinct normal indices $i,k$ share only the remaining edge direction $d$. On that edge the exact product is 

$$
V_i(n,d)V_k(n,d)=
 -\frac2{N_j^3}
 \sin\left(\frac{\pi a_jn_i}{\ell_j}\right)
 \sin\left(\frac{\pi a_jn_k}{\ell_j}\right)
 \cos^2\left(\frac{\pi a_j(n_d+1/2)}{\ell_j}\right).
$$

 Keeping the two original signs and using uniform convergence $\ell_j\sin(\pi x/\ell_j)\to\pi x$ on the fixed support proves 

$$
\ell_j^5 A^h_{ik}\longrightarrow-2\pi^2H_{h,ik}.
$$

 Finally $\ell_j\sigma_j/a_j=N_j\sqrt8\sin(\pi/(2N_j))
\to\sqrt2\pi$. These identities prove both matrix limits. Insert the first into the exact raw mass formula to get $3\cdot3(4\sqrt2\pi)^2H_h^2/8=36\pi^2H_h^2$.

This calculation retains spatial information beyond the leading integral: (138) is an explicit map to three mixed spatial moments. A vanishing integral does not imply that the original weighted state or these next coefficients vanish.

## One positive-coupling diagonal and its raw common representation

The finite-regulator convergence can be enforced for every bounded edge weight at once at each fixed $j$. There are finitely many original edges. Let $b^{(e)}$ be the weight one at $e$ and zero elsewhere, with its prescribed face averages. Both the actual centered operator and its comparison matrix are linear in this weight. Choose 

$$
\epsilon_j=j^{-40}(1+\ell_j)^{-10}.
$$

 At each fixed $j$, take the least positive integer $n_j$ such that $g_j=2^{-n_j}<1/j$ satisfies the finite inequalities of Theorem 14.2, $\|G_{g_j}-I\|<\epsilon_j$, and 

$$
\|\mathcal D_{g_j,b^{(e)}}-\mathcal D_{0,b^{(e)}}\|
       <\epsilon_j/|\mathsf E_{L_j}|\quad(e\in\mathsf E_{L_j}).
$$

 Also require the exact frame energy matrix to differ from $0\oplus\Delta_jI$ by less than $\epsilon_j$, and the frame coefficient of the full projected Fabel state to differ from $(0,\mathsf R_{S_j}^{\min}/(4a_j))$ by less than $\epsilon_j$. Projection, graph and eigenvalue convergence prove existence for this finite list. This is a defined stricter coupling sequence; it does not silently reuse a previously chosen $g_j$ for new inequalities. All conclusions of Section 14 persist.

For every real edge weight $f$, finite linearity now gives the uniform bound 

$$
\|\mathcal D_{g_j,f}-\mathcal D_{0,f}\|
 \le\epsilon_j\|f\|_\infty.
$$

 The energy and Fabel coordinate requirements also follow from the fixed-box frame and vector convergence already proved. All actual states and operators retain their original coefficients $\kappa_j=200jg_j^2$, $b_j=50j/g_j^2$, and full Wilson scalar.

### Theorem 15.2.

For every real $h\in C_c(\mathbb R^3)$, the actual Gram and compressed operator coordinates satisfy 

$$
G_{g_j}\to I,\qquad
 \ell_j^4\mathcal D_{g_j,f_{h,j}}\to\mathcal T_h
$$

 in operator norm on the fixed space $\mathcal K$, where 

$$
\qquad\text{(140)}
 \mathcal T_h(c,B)=
 \sqrt2\pi H_h\bigl(6\operatorname{tr}B,\ cI_3+4B\bigr).
$$

 The actual excitation matrix $\mathcal A_j$ satisfies 

$$
\qquad\text{(141)}
 \mathcal A_j\to0,\qquad
 \ell_j\mathcal A_j\to
       \mathcal A_*:=0\oplus2\sqrt2\pi I.
$$

 These limits include all finite products of the displayed compressed operators and their compressed time evolution.

### Proof.

Apply (137) to each term of (135), and use $\ell_j^4\epsilon_j\|h\|_\infty\to0$. The first component becomes $6\sqrt2\pi H_h\operatorname{tr}B$; the other two become $\sqrt2\pi H_hcI$ and $4\sqrt2\pi H_hB$. This proves (140), including its adjoint relation in the original factor-$6$ metric. The exact energy frame is block diagonal because the vacuum and excited range are invariant and orthogonal. Its specified error and $\ell_j\Delta_j\to2\sqrt2\pi$ give (141). Operator-norm convergence in a fixed finite-dimensional space preserves finite products. The exponential power series, uniformly bounded on each fixed compact time interval, gives convergence of the displayed time evolutions.

The map $h\mapsto\mathcal T_h$ is explicitly the integral functional times the single displayed operator. On the traceless matrices its eigenvalue is $4\sqrt2\pi H_h$; on the vacuum/trace coordinates its matrix is $\sqrt2\pi H_h\left(\begin{smallmatrix}0&18\\1&4\end{smallmatrix}\right)$ in the basis $(1,0),(0,I)$, whose squared norms are $1,18$. Its characteristic roots are $\sqrt2\pi H_h(2+\sqrt{22})$ and $\sqrt2\pi H_h(2-\sqrt{22})$. This is a finite-dimensional self-adjoint compressed observable with all raw metric factors, not an assertion that the full local-energy algebra has collapsed.

Let $v_{h,j}=P_{g_j}\Xi_{f_{h,j}}$. The exact vacuum component of $\Xi$ vanishes. Equations (133)--(140) therefore give its coordinate limit 

$$
\ell_j^4M_{g_j}^{-1}v_{h,j}
 \longrightarrow(0,\sqrt2\pi H_hI).
$$

 This equation records the raw amplitude $\ell_j^{-4}$. It defines no unit-vector rescaling. In particular, for real compact $h,k$ and fixed physical Euclidean time $t\ge0$, 

$$
\begin{aligned}
 \ell_j^8\langle v_{h,j},e^{-t(H_j-\mathcal E_j)}v_{k,j}\rangle
 &\longrightarrow36\pi^2H_hH_k,\qquad\text{(142)}\\
 \ell_j^8\langle v_{h,j},
       e^{-\ell_j\theta(H_j-\mathcal E_j)}v_{k,j}\rangle
 &\longrightarrow36\pi^2H_hH_k e^{-2\sqrt2\pi\theta}
 \quad(\theta\ge0).\qquad\text{(143)}
\end{aligned}
$$

 These follow by inserting the exact Gram $G_{g_j}$ and the exact energy matrix in the inner product. The second equation records the explicit time change $t=\ell_j\theta$; it is not used to replace the original Hamiltonian or its physical energy quotient. At fixed physical time this particular finite band becomes a zero-energy sector. At times proportional to the box length its nontrivial dynamics are the explicitly displayed finite matrix. The same actual energy matrix gives the raw first-moment limit 

$$
\ell_j^9\langle v_{h,j},(H_j-\mathcal E_j)v_{h,j}\rangle
 \longrightarrow72\sqrt2\pi^3H_h^2.
$$

 When $H_h\ne0$, the raw norm limit is strictly positive after its displayed $\ell_j^8$ factor, so $v_{h,j}\ne0$ eventually and 

$$
\ell_j\frac{\langle v_{h,j},(H_j-\mathcal E_j)v_{h,j}\rangle}
                   {\|v_{h,j}\|^2}\longrightarrow2\sqrt2\pi.
$$

 The vectors themselves retain their vanishing raw norms.

For the unchanged Fabel states $w_j$ of Section 14 let $S_*=\eta\eta^{\mathsf T}$ as there, and define the full fixed matrix 

$$
(B_*)_{ii}=-\frac{25\sqrt2}{\pi}
                    (\operatorname{tr}S_*-S_{*,ii}),\qquad
 (B_*)_{ik}=\frac{400\sqrt2}{\pi^3}S_{*,ik}\quad(i\ne k).
$$

 The exact lowest-mode coefficients give $M_{g_j}^{-1}w_j=j^9(0,B_*+o(1))$ and $6\operatorname{tr}(B_*^2)=\mathcal C_*$. Consequently the original raw matrix elements obey 

$$
\begin{aligned}
 \frac{\ell_j^4}{j^{18}}
 \langle w_j,C_{g_j,f_{h,j}}w_j\rangle
 &\longrightarrow4\sqrt2\pi H_h\mathcal C_*,
 \qquad\text{(144)}\\
 \frac{\ell_j^4}{j^9}
 \langle\psi_j,C_{g_j,f_{h,j}}w_j\rangle
 &\longrightarrow-\frac{25275}{8}H_h.
 \qquad\text{(145)}
\end{aligned}
$$

 The first follows from the band component $4\sqrt2\pi H_hB$ of (140). For the sign and constant in the second, $\operatorname{tr}S_*=337/64$ and $\operatorname{tr}B_*=-8425\sqrt2/(32\pi)$; multiplication by $6\sqrt2\pi H_h$ yields the result. Thus the quotient of the first raw expectation by $\|w_j\|^2$ decays as $4\sqrt2\pi H_h/\ell_j^4$ when $H_h\ne0$, even though the unscaled raw expectation itself grows. Neither conclusion is inferred by dropping the Fabel amplitude.

## The map from a compact Navier--Stokes curvature profile

Take any actual smooth compactly supported incompressible velocity profile $u(s,\cdot)$ at a regular time $s$ in the Navier--Stokes construction under study. Its viscosity, force, pressure and time interval remain the ones of that construction. Set 

$$
\mathcal A_0=0,\quad\mathcal A_i=\lambda u_iT,\quad
 T=-i\sigma_3/2,\qquad
 h_s(x)=\sum_{i<k}-2\operatorname{tr}(F_{ik}(s,x)^2)
                =\lambda^2|\operatorname{curl}u(s,x)|^2.
$$

 Here $F_{ik}=\lambda(\partial_iu_k-\partial_ku_i)T$ and $-2\operatorname{tr}(T^2)=1$ prove the equality. The weighted local-energy operator uses the full profile: $f_{s,j}(e)=h_s(a_jm(e))$, with all prescribed face averages. The composition 

$$
u(s,\cdot)\longmapsto h_s\longmapsto D_{f_{s,j}}
 \longmapsto\Xi_{f_{s,j}}\longmapsto P_{g_j}\Xi_{f_{s,j}}
$$

 is now a specified map into the actual physical Hilbert space. Its raw first-band masses and mixed-time spectral matrix elements are (139), (142) and (143), with 

$$
H_{h_s}=\lambda^2\|\operatorname{curl}u(s,\cdot)\|_2^2,
 \qquad
 H_{h_s,ik}=\lambda^2\int x_ix_k|\operatorname{curl}u(s,x)|^2\,dx.
$$

 For $\lambda\ne0$ and a nonzero compact smooth incompressible profile, $H_{h_s}>0$. Indeed integration by parts gives $\int|\nabla u|^2=\int|\operatorname{curl}u|^2+
\int|\operatorname{div}u|^2$; if its curl vanishes, all derivatives vanish and compact support forces $u=0$. Thus this particular local-curvature state has nonzero first-band mass at sufficiently late regulators, with all norm powers explicit.

This is a regular-time profile map. It does not assert that $H_{h_s}$ diverges as a blowup time is approached: pointwise concentration and its spatial integral remain distinct quantities in the displayed exact map. The full sourced current $j_i=(\lambda/g^2)(\Delta u_i-c^{-2}\partial_s^2u_i)T$ from Section 13 is unchanged. No equality between evolution in the fluid parameter $s$ and the quantum time $t$ or $\theta$ is used or claimed. The limits above apply to every fixed regular profile; a simultaneous singular-fluid-time limit is not exchanged with the regulator limits. Only the nonzero compact incompressible profile, rather than its singular endpoint, was used to prove positive band mass. The gap-closing projected sequence therefore does not establish an implication specific to Navier--Stokes breakdown.

## All terms leaving the seven-dimensional range

Let $\widehat Q_g=I-\Pi_g$. On the original smooth spectral range, the exact identity is 

$$
\qquad\text{(146)}
 \Pi_g C_{g,h}C_{g,k}\Pi_g
 =\Pi_gC_{g,h}\Pi_gC_{g,k}\Pi_g+
       (\widehat Q_gC_{g,h}\Pi_g)^*
                        (\widehat Q_gC_{g,k}\Pi_g).
$$

 Each finite-range eigenvector is smooth, each weighted differential operator preserves smoothness, and its formal adjoint is its self-adjoint realization there. Inserting $I=\Pi_g+\widehat Q_g$ therefore proves the identity with no domain omission. For $h=k$ the last term is positive. Products of the compressed limits alone do not determine this term.

The fixed-box graph limit proves the exact comparison for every leakage matrix element as well. Here are its full coordinates. Extend a lowest-mode symmetric $B$ by zero to all modes and put $\mathcal S_B= \sum_{\nu,\eta,\alpha}
B_{\nu\eta}a_{\nu,\alpha}^\dagger a_{\eta,\alpha}^\dagger$. Let $\mathsf P_\perp$ remove the lowest $3$-by-$3$ block of a symmetric mode matrix. From (134), 

$$
\begin{aligned}
 \widehat Q_0C_{0,f}\Phi_0
 &=\frac1{4a}\Phi(\mathsf P_\perp\mathsf R_f),
 \qquad\text{(147)}\\
 \widehat Q_0C_{0,f}\Phi(B)
 &=\frac1{4a}\mathcal S_{\mathsf R_f}\mathcal S_B\Phi_0
 +\frac1{2a}
 \Phi\!\left(\mathsf P_\perp(\mathsf Q_fB+B\mathsf Q_f)\right).
 \qquad\text{(148)}
\end{aligned}
$$

 In these equations $\Phi$ on a full mode matrix uses the same colour-contracted formula over every spatial mode. The two terms on the right in (148) have respectively four and two creation operators, hence are orthogonal. The annihilation term has landed in the vacuum and is included in $\Pi_0$, so it is absent for that exact reason. In particular 

$$
\|\widehat Q_0C_{0,f}\Phi_0\|^2
 =\frac3{8a^2}\left[
 \operatorname{tr}(\mathsf R_f^2)
           -\operatorname{tr}((\mathsf R_f^{\min})^2)\right].
$$

 The four-creation contraction also has a completely explicit finite sum. With combined indices $I=(\nu,\alpha)$ define $T_{I_1I_2I_3I_4}
=(\mathsf R_f)_{\nu_1\nu_2}B_{\nu_3\nu_4}
\delta_{\alpha_1\alpha_2}\delta_{\alpha_3\alpha_4}$. For another pair of matrices producing coefficients $U$, 

$$
\left\langle\mathcal S_{\mathsf R_f}\mathcal S_B\Phi_0,
              \mathcal S_{\mathsf R_k}\mathcal S_E\Phi_0\right\rangle
 =\sum_{I_1,\ldots,I_4}\sum_{J_1,\ldots,J_4}
 \overline{T_{I_1I_2I_3I_4}}U_{J_1J_2J_3J_4}
 \sum_{\pi\in S_4}\prod_{r=1}^4\delta_{I_rJ_{\pi(r)}}.
$$

 Repeatedly commute the four annihilators through the four creators; every surviving vacuum term is one of these $24$ pairings, proving the formula with its multiplicities and colour factors. The two-creation term has the already-proved factor-$6$ trace inner product. These equations give every omitted-intermediate covariance in (146) at fixed box and coupling limit.

We have constructed a common finite-dimensional representation of the exact compressed local-energy maps, including their raw coupling to Fabel and compact Navier--Stokes profiles. Its fixed physical-time energy is zero and its leading spatial functional is the integral, with explicitly retained next mixed moments. The full higher-mode leakage, the products without intermediate projection, and their joint infinite-volume continuum limit have not been evaluated by that compression. They are represented by the explicit maps and contractions above. Their continuum behavior is the next calculation needed before this sequence can identify a local interacting four-dimensional Yang--Mills theory.

## References 

### \[1\]

G. Dusson, I. M. Sigal, and B. Stamm, *The Feshbach--Schur map and perturbation theory*, in *Partial Differential Equations, Spectral Theory, and Mathematical Physics*, EMS Series of Congress Reports (2021), pp. 65--88. [doi:10.4171/ECR/18-1/5](https://doi.org/10.4171/ECR/18-1/5); [arXiv:2105.02058v1](https://arxiv.org/abs/2105.02058v1), Theorem 1.2 and Eqs. (1.10)--(1.16).

### \[2\]

D. Bakry and M. Ledoux, *A logarithmic Sobolev form of the Li--Yau parabolic inequality*, Revista Matemática Iberoamericana **22** (2006), no. 2, 683--702. [doi:10.4171/RMI/470](https://doi.org/10.4171/RMI/470), Eq. (1.7) and its proof, pp. 686--687.

### \[3\]

B. Simon, *A Feynman--Kac Formula for Unbounded Semigroups*, [arXiv:math-ph/9907022v1](https://arxiv.org/abs/math-ph/9907022v1) (1999), Theorem 1.1 and Eqs. (1.1)--(1.3).

### \[4\]

H. Mori, *Transport, Collective Motion, and Brownian Motion*, Progress of Theoretical Physics **33** (1965), 423--455. [doi:10.1143/PTP.33.423](https://doi.org/10.1143/PTP.33.423).

### \[5\]

J. Kogut and L. Susskind, *Hamiltonian formulation of Wilson's lattice gauge theories*, Physical Review D **11** (1975), 395--408. [doi:10.1103/PhysRevD.11.395](https://doi.org/10.1103/PhysRevD.11.395).

### \[6\]

F. Peter and H. Weyl, *Die Vollständigkeit der primitiven Darstellungen einer geschlossenen kontinuierlichen Gruppe*, Mathematische Annalen **97** (1927), 737--755. [doi:10.1007/BF01447892](https://doi.org/10.1007/BF01447892).

### \[7\]

D. A. Yarotsky, *Quasi-particles in weak perturbations of non-interacting quantum lattice systems*, [arXiv:math-ph/0411042v1](https://arxiv.org/abs/math-ph/0411042v1) (2004), Section 2.

### \[8\]

J. C. Baez, *Spin Network States in Gauge Theory*, Advances in Mathematics **117** (1996), 253--272. [doi:10.1006/aima.1996.0012](https://doi.org/10.1006/aima.1996.0012); [arXiv:gr-qc/9411007v1](https://arxiv.org/abs/gr-qc/9411007v1).
