# The cubic color singlet and the first vacuum-energy correction

9 September 2026. All formulas refer to the original open-box SU(2)
Hamiltonian, including every edge and plaquette. This calculation evaluates
its first interaction coefficients; it does not replace that Hamiltonian
by a three-mode model. A sum over three distinct modes below ranges over
all such triples in the complete finite box.

## 1. Original operator and the coordinate dictionary

Vertices are \(n\in\{-L,\ldots,L\}^3\), \(L\ge2\), and edges are all
positive contained nearest-neighbor edges. Faces carry the oriented word
\(U_i(n)U_j(n+e_i)U_i(n+e_j)^{-1}U_j(n)^{-1}\), \(i<j\).
Use \(T_\alpha=-i\sigma_\alpha/2\), Haar probability measure, and
\[
 H_g={2g^2\over a}\sum_e E_e+
       {1\over2g^2a}\sum_p(2-\operatorname{tr}U_p),\qquad
 E_e=-\sum_\alpha X_{e,\alpha}^2,\quad g,a>0.
 \tag{1}
\]
The physical Hilbert space is the invariant subspace under all vertex
gauge transformations. Its vacuum is the positive unit eigenfunction.
No trial state is divided by its norm in this calculation.

Use the rooted tree whose parent decreases the first available coordinate
in the order \(1,2,3\). Write \(\mathcal C\) for its chords and
\(r=|\mathcal C|=2(2L)^3+3(2L)^2\). For a vertex \(v\), \(t_v\)
is its ordered root-to-vertex holonomy. The exact chord variable is
\(Z_c=t_{s(c)}U_ct_{t(c)}^{-1}\). Tree links and these chord variables
give a Haar-measure-preserving bijection, by independent left/right
translations of the chord factors for fixed tree links. Vertex gauge
reduction leaves simultaneous conjugation of all \(Z_c\).

For an edge cochain \(u\), let \(p_v(u)\) be its additive integral on the
same tree path and define the full-row-rank matrix
\[
 (\mathsf T u)_c=p_{s(c)}(u)+u_c-p_{t(c)}(u),\qquad
 G=\mathsf T\mathsf T^*,\qquad C=d_1j.
 \tag{2}
\]
Here \(j\) inserts chord values and zero tree values; \(d_1\) is the
oriented face sum in (1). The kernel of \(\mathsf T\) consists exactly of
gradients: path telescoping proves one inclusion and the vertex potentials
\(p_v(u)\) prove the converse. Likewise \(\ker d_1=\operatorname{im}d_0\),
by interchanging adjacent coordinate steps in a monotone path. Consequently
\(G>0\), \(C\) is injective, and the eigenvalues of
\(G^{1/2}C^*CG^{1/2}\) are strictly positive.

Choose an orthogonal diagonalization
\[
 O^*G^{1/2}C^*CG^{1/2}O=\Sigma^2,\qquad
 \Sigma=\operatorname{diag}(\sigma_1,\ldots,\sigma_r),\quad \sigma_\mu>0.
 \tag{3}
\]
This is the complete spectrum, not a selection of low modes. Explicitly
\(\sigma^2=4\sum_{i=1}^3\sin^2(\pi j_i/[2(2L+1)])\), with
\(j_i\in\{0,\ldots,2L\}\), at least two positive indices, and
multiplicity one less than their number of positive indices.
Tensoring the interval cosine vertex modes and sine edge modes proves
this formula: the gradient at each triple is the vector of its three
positive square roots, and the curl squared is their squared norm times
the projection perpendicular to that gradient.

Set
\[
 \mathsf A=G^{1/2}O,\quad
 B={1\over4}G^{-1/2}O\Sigma O^*G^{-1/2},\quad
 \mathsf N=B\mathsf A={1\over4}G^{-1/2}O\Sigma,\quad M={1\over2}B^{-1}.
 \tag{4}
\]
These matrices act on chord indices, identically in each of the three
color coordinates. The exact local maps are \(Z_c=\exp(gx_c^\alpha
T_\alpha)\) and \(x=\mathsf A z\). The Haar density is
\[
 \mathcal J(y)=(16\pi^2)^{-r}
  \prod_c\left({\sin(|y_c|/2)\over |y_c|/2}\right)^2.
 \tag{5}
\]
The local norm-preserving map is
\(F(\exp(gx))=g^{-3r/2}\mathcal J(gx)^{-1/2}f(x)\);
the linear \(x=\mathsf A z\) map retains the absolute Jacobian
\(\det(G)^{3/2}\). The comparison vacuum in \(x\) is
\[
 \Phi(x)=\det(B)^{3/4}\pi^{-3r/4}
           \exp\!\left(-{1\over2}\sum_\alpha(x^\alpha)^*Bx^\alpha\right).
 \tag{6}
\]
Thus \(\partial_{x_c^\alpha}\Phi=-(Bx)_c^\alpha\Phi\).
Its exact covariance is
\(\langle x_c^\alpha x_d^\beta\rangle=M_{cd}\delta_{\alpha\beta}\).
In \(z\), the covariance of each color component of mode \(\mu\) is
\(2/\sigma_\mu\). The comparison operator and its vacuum energy are
\[
 H_0=\sum_{\mu=1}^r
       \left(-{2\over a}\Delta_{z_\mu}
                    +{\sigma_\mu^2\over8a}|z_\mu|^2\right),\qquad
 e_0={3\over2a}\sum_\mu\sigma_\mu.
 \tag{7}
\]

## 2. All tree incidence and first kinetic coefficients

Let \(\ell_{ec},r_{ec}\) be the coefficients of the left and right chord
derivatives in the exact tree-reduced edge field. For a chord edge \(e\),
\(\ell_{ec}=\delta_{ec},r_{ec}=0\). For a tree edge, they are respectively
\(\epsilon(s(c),e)\) and \(-\epsilon(t(c),e)\), where \(\epsilon(v,e)\)
records membership in the root-to-\(v\) path. Put
\[
 t_{ec}=\ell_{ec}+r_{ec},\qquad s_{ec}=\ell_{ec}-r_{ec}.
 \tag{8}
\]
In particular \(\sum_e t_{ec}t_{ed}=G_{cd}\).
Differentiating \(\log(e^{uT_\alpha}e^y)\) and
\(\log(e^ye^{uT_\alpha})\) at \(u=0\) gives
\(I-\operatorname{ad}_y/2+\operatorname{ad}_y^2/12+O(|y|^3)\)
and \(I+\operatorname{ad}_y/2+\operatorname{ad}_y^2/12+O(|y|^3)\),
respectively. The signs follow by differentiating the exponential series
and solving its tangent equation order by order, using
\([v^\alpha T_\alpha,w^\beta T_\beta]=(v\times w)^\gamma T_\gamma\).

For the principal matrix after \(y=gx\), write
\(A(gx)=G\otimes I_3+gA_1(x)+g^2A_2(x)+O(g^3)\). Squaring all
the preceding edge fields gives
\[
 (A_1)^{c\beta,d\gamma}
 ={1\over2}\sum_e\epsilon_{\eta\beta\gamma}
   \{s_{ec}t_{ed}x_c^\eta-t_{ec}s_{ed}x_d^\eta\},
 \tag{9}
\]
\[
 \begin{split}
 (A_2)^{c\beta,d\gamma}=\sum_e\{&
 {s_{ec}s_{ed}\over4}
 [\delta_{\beta\gamma}x_c\cdot x_d-x_d^\beta x_c^\gamma]\\
 &+{t_{ec}t_{ed}\over12}
 [x_c^\beta x_c^\gamma+x_d^\beta x_d^\gamma
                 -( |x_c|^2+|x_d|^2)\delta_{\beta\gamma}]\}.
 \end{split}
 \tag{10}
\]
The cross-product identity
\(\sum_\alpha(x_c\times e_\alpha)_\beta
(x_d\times e_\alpha)_\gamma
=\delta_{\beta\gamma}x_c\cdot x_d-x_d^\beta x_c^\gamma\)
proves the first term of (10). The identity
\(x\times(x\times e_\alpha)=x(x\cdot e_\alpha)-|x|^2e_\alpha\)
proves its second term.

The derivative contraction \(\partial_i(A_1)^{ij}\) is zero:
each derivative identifies two indices in the alternating tensor in
(9). Also \(\operatorname{tr}(A_1(B\otimes I_3))=0\), because
that trace identifies the two color indices.
Put \(p_c=(Bx)_c\). Substitution in (9), followed by exchanging \(c,d\)
in its second summand, yields the exact polynomial identity
\[
 p^*A_1p=\sum_{e,c,d}s_{ec}t_{ed}
                  x_c\cdot(p_c\times p_d).
 \tag{11}
\]
No integration or parity argument is needed for this identity.

## 3. Retained ordered Wilson terms

For each original face retain its four signed chord letters
\(v_{p,i}=\varepsilon_{p,i}x_{c(p,i)}\); a tree letter is the zero
vector, and an inverse chord has sign \(-1\). Write
\(W(gx)=g^2W_2+g^3W_3+g^4W_4+O(g^5)\). Direct multiplication gives
\[
 W_2={1\over4}\sum_p\left|\sum_{i=1}^4v_{p,i}\right|^2,\qquad
 W_3={1\over4}\sum_p\sum_{i<j<k}
                   \det(v_{p,i},v_{p,j},v_{p,k}).
 \tag{12}
\]
For a single face, its quartic contribution is the negative of
\[
 \begin{split}
 &\sum_i {|v_i|^4\over192}
 +\sum_{i<j}{(|v_i|^2+|v_j|^2)(v_i\cdot v_j)\over48}
 +\sum_{i<j}{|v_i|^2|v_j|^2\over32}\\
 &+\sum_{i<j<k}
 { |v_i|^2(v_j\cdot v_k)+|v_j|^2(v_i\cdot v_k)
                         +|v_k|^2(v_i\cdot v_j)\over16}\\
 &+{(v_1\cdot v_2)(v_3\cdot v_4)
       -(v_1\cdot v_3)(v_2\cdot v_4)
       +(v_1\cdot v_4)(v_2\cdot v_3)\over8}.
 \end{split}
 \tag{13}
\]
Indeed \(V_i=v_i^\alpha T_\alpha\) satisfies
\(V_i^2=-|v_i|^2I/4\). Moreover
\(\operatorname{tr}V_iV_j=-v_i\cdot v_j/2\),
\(\operatorname{tr}V_iV_jV_k=-\det(v_i,v_j,v_k)/4\), and the
four-factor trace is the last bracket in (13) divided by \(8\).
The degree-four distributions among ordered letters are
\(4\), \(3+1\), \(2+2\), \(2+1+1\), and \(1+1+1+1\).
Their exponential factorials give precisely (13).

The half-density map (5) contributes the scalar
\(-\operatorname{tr}G/(2a)\) at order \(g^2\).
For clarity, \(\log\mathcal J(gx)=\mathrm{constant}
-g^2\sum_c|x_c|^2/12+O(g^4|x|^4)\).
In the exact kinetic quadratic form its shifted derivative is
\(\partial+g^2x/12+O(g^4)\).
The two cross terms with \(G\otimes I_3\), integrated by parts, give
\(-(2/a)g^2\operatorname{tr}(G\otimes I_3)/12
=-g^2\operatorname{tr}G/(2a)\).
There is no order-\(g\) density term.

Consequently the two interaction coefficients are
\[
 H_1=-{2\over a}\partial_i(A_1)^{ij}\partial_j+{W_3\over2a},
 \qquad
 H_2=-{2\over a}\partial_i(A_2)^{ij}\partial_j
                  -{\operatorname{tr}G\over2a}+{W_4\over2a}.
 \tag{14}
\]
They preserve simultaneous SO(3) color rotations. Simultaneous inversion
\(x\mapsto-x\) changes the sign of \(H_1\), not of \(H_2\).
Inversion is not an adjoint SU(2) rotation; its parity does not remove
the odd rotation singlets.

## 4. Evaluated three-mode singlets, not an unspecified inverse

Equations (6),(9),(11),(12),(14) give
\[
 {H_1\Phi\over\Phi}
 =-{2\over a}\sum_{e,c,d}s_{ec}t_{ed}\det(x_c,p_c,p_d)
     +{1\over8a}\sum_{p,i<j<k}\det(v_{p,i},v_{p,j},v_{p,k}).
 \tag{15}
\]
Define \(a_{p,i,\mu}=\varepsilon_{p,i}\mathsf A_{c(p,i),\mu}\)
for a chord letter and zero for a tree letter. The fully specified tensor
\[
 Q_{\mu\nu\rho}=
 -{2\over a}\sum_{e,c,d}s_{ec}t_{ed}
                      \mathsf A_{c\mu}\mathsf N_{c\nu}\mathsf N_{d\rho}
 +{1\over8a}\sum_{p,i<j<k}
                         a_{p,i,\mu}a_{p,j,\nu}a_{p,k,\rho}
 \tag{16}
\]
uses only the original incidences and the complete eigenbasis (3).
For \(\mu<\nu<\rho\) set
\[
 \Theta_{\mu\nu\rho}
       =\sum_{\pi\in S_3}\operatorname{sgn}(\pi)
                   Q_{\pi(\mu,\nu,\rho)}.
 \tag{17}
\]
This is the six-term sum, with no factor \(1/6\).
Multilinearity of determinant proves
\[
 H_1\Phi=\sum_{\mu<\nu<\rho}
              \Theta_{\mu\nu\rho}\det(z_\mu,z_\nu,z_\rho)\Phi.
 \tag{18}
\]
Repeated spatial indices vanish because the corresponding determinant
has two equal vector arguments. Equation (18) is not a claim that every
coefficient is nonzero; coefficients are exactly (16)--(17).

Put \(D_{\mu\nu\rho}=\det(z_\mu,z_\nu,z_\rho)\Phi\).
It is an SO(3) singlet and is orthogonal to \(\Phi\). Applying (7) to
a polynomial times \(\Phi\) gives the exact conjugated operator
\[
 (H_0-e_0)(P\Phi)
 =\left[-{2\over a}\sum_\eta\Delta_{z_\eta}P
       +{1\over a}\sum_\eta\sigma_\eta z_\eta\cdot\nabla_{z_\eta}P\right]\Phi.
 \tag{19}
\]
Each determinant is linear in each of its three distinct vector
arguments, hence its Laplacian vanishes in every mode. Thus
\[
 (H_0-e_0)D_{\mu\nu\rho}
      ={\sigma_\mu+\sigma_\nu+\sigma_\rho\over a}D_{\mu\nu\rho},
 \qquad
 \|D_{\mu\nu\rho}\|^2={48\over\sigma_\mu\sigma_\nu\sigma_\rho}.
 \tag{20}
\]
For the norm, expand both determinants as alternating sums.
Independence of the three modes forces matching color indices; six
permutations remain, each contributing \(8/(\sigma_\mu\sigma_\nu
\sigma_\rho)\). Different unordered spatial triples are orthogonal:
a mode occurring in only one triple has one centered coordinate factor.
This also proves \(\langle\Phi,H_1\Phi\rangle=0\).

Let \(R_0\) be the reduced inverse of \(H_0-e_0\). Its value on (18)
is therefore explicitly
\[
 R_0H_1\Phi=\sum_{\mu<\nu<\rho}
 {a\Theta_{\mu\nu\rho}\over\sigma_\mu+\sigma_\nu+\sigma_\rho}
                         D_{\mu\nu\rho},
 \tag{21}
\]
and
\[
 \langle H_1\Phi,R_0H_1\Phi\rangle
 =\sum_{\mu<\nu<\rho}
 {48a\,\Theta_{\mu\nu\rho}^2\over
      \sigma_\mu\sigma_\nu\sigma_\rho(\sigma_\mu+\sigma_\nu+\sigma_\rho)}.
 \tag{22}
\]
The first vacuum-vector coefficient is minus (21). Its squared norm has
the same summands with \(a\) replaced by \(a^2\) and the last frequency
sum squared. These are sums over the entire graph, not three chosen
oscillators.

## 5. The evaluated quartic and measure contributions

For each face define the real symmetric four-letter covariance
\[
 m_{ij}=\varepsilon_{p,i}\varepsilon_{p,j}
                             M_{c(p,i),c(p,j)};
 \tag{23}
\]
a tree letter makes that entry zero. Define the following polynomial:
\[
 \begin{split}
 \mathcal W_4(m)=-\bigg\{&
 {15\over192}\sum_i m_{ii}^2
 +{15\over48}\sum_{i<j}(m_{ii}+m_{jj})m_{ij}\\
 &+{1\over32}\sum_{i<j}(9m_{ii}m_{jj}+6m_{ij}^2)\\
 &+{1\over16}\sum_{i<j<k}
 [9(m_{ii}m_{jk}+m_{jj}m_{ik}+m_{kk}m_{ij})
       +6(m_{ij}m_{ik}+m_{ij}m_{jk}+m_{ik}m_{jk})]\\
 &+{9m_{12}m_{34}-3m_{13}m_{24}+9m_{14}m_{23}\over8}
 \bigg\}.
 \end{split}
 \tag{24}
\]
Then \(\langle W_4\rangle=\sum_p\mathcal W_4(m^{(p)})\).
To verify it directly, Gaussian integration gives
\[
 \begin{split}
 \langle |v_i|^4\rangle&=15m_{ii}^2,\\
 \langle |v_i|^2(v_i\cdot v_j)\rangle&=15m_{ii}m_{ij},\\
 \langle |v_i|^2|v_j|^2\rangle&=9m_{ii}m_{jj}+6m_{ij}^2,\\
 \langle |v_i|^2(v_j\cdot v_k)\rangle
                         &=9m_{ii}m_{jk}+6m_{ij}m_{ik},\\
 \langle(v_i\cdot v_j)(v_k\cdot v_l)\rangle
                         &=9m_{ij}m_{kl}+3m_{ik}m_{jl}+3m_{il}m_{jk}.
 \end{split}
 \tag{25}
\]
These identities follow by differentiating the exact Gaussian generating
function \(\langle e^{u\cdot v}\rangle=e^{u^*\operatorname{Cov}(v)u/2}\)
four times; the three pairings are all retained. Applying (25) to each
term of (13) proves (24), including its middle negative coefficient.

The kinetic expectation can also be evaluated, without differentiating
an unspecified Gaussian integral. Put \(p=Bx\); then
\(\langle p_c^\alpha p_d^\beta\rangle=B_{cd}\delta_{\alpha\beta}/2\)
and \(\langle x_c^\alpha p_d^\beta\rangle=
\delta_{cd}\delta_{\alpha\beta}/2\). Substitution in (10) gives
\[
 \begin{split}
 \langle p^*A_2p\rangle=\sum_{e,c,d}\bigg[
 &s_{ec}s_{ed}\left({3\over4}B_{cd}M_{cd}-{3\over8}\delta_{cd}\right)\\
 +&t_{ec}t_{ed}\left({1\over4}\delta_{cd}
                       -{1\over4}B_{cd}(M_{cc}+M_{dd})\right)\bigg].
 \end{split}
 \tag{26}
\]
For example the first bracket is one quarter of the difference between
\(\langle(p_c\cdot p_d)(x_c\cdot x_d)\rangle\) and
\(\langle(p_c\cdot x_d)(p_d\cdot x_c)\rangle\).
Its two Wick expansions give respectively
\(9B_{cd}M_{cd}/2+3/4+3\delta_{cd}/4\) and
\(3B_{cd}M_{cd}/2+3/4+9\delta_{cd}/4\).
For either \(v=x_c\) or \(v=x_d\), the difference
\(\langle(p_c\cdot v)(p_d\cdot v)-|v|^2(p_c\cdot p_d)\rangle\)
is \(3\delta_{cd}/2-3B_{cd}M_{vv}\).
Adding these and dividing by twelve proves the second bracket.

Integration by parts in (14) now yields the fully evaluated coefficient
\[
 \boxed{\begin{split}
 e_2={}&{2\over a}\langle p^*A_2p\rangle
             -{\operatorname{tr}G\over2a}
             +{1\over2a}\sum_p\mathcal W_4(m^{(p)})\\
 &-\sum_{\mu<\nu<\rho}
 {48a\,\Theta_{\mu\nu\rho}^2\over
 \sigma_\mu\sigma_\nu\sigma_\rho(\sigma_\mu+\sigma_\nu+\sigma_\rho)} .
 \end{split}}
 \tag{27}
\]
In (27), (26),(24),(16),(17) are finite explicitly specified sums;
there is no uncomputed reduced resolvent or intermediate-state symbol.
The separate Haar scalar is displayed, not absorbed into the energy origin.
It contributes to the absolute vacuum energy although scalar shifts cancel
in vacuum-subtracted spectral differences.

## 6. What coefficient has been calculated

At a fixed finite box, the exact chart expansion with Gaussian cutoffs
gives the actual vacuum expansion
\(\mathcal E_g=e_0+g^2e_2+O_{L,a}(g^3)\).
Here is a direct proof with the cutoff and actual spectral projection.
The coefficient equations follow by inserting
\(\Phi+g\phi_1+g^2\phi_2\) and \(e_0+g^2e_2\):
\[
 \phi_1=-R_0H_1\Phi,\qquad
 (H_0-e_0)\phi_2=-(H_1\phi_1+(H_2-e_2)\Phi).
 \tag{28}
\]
Its right side is perpendicular to \(\Phi\) precisely for (27).
The unit-vacuum convention fixes
\(\langle\Phi,\phi_2\rangle=-\|\phi_1\|^2/2\).
All vectors in (28) are finite Gaussian polynomials; (19) determines
the inverse coefficient by coefficient in the complete Hermite basis.
In particular the odd cubic singlet changes the vacuum at order \(g\),
even though its vacuum-energy expectation vanishes at that order.

Choose a smooth invariant cutoff \(\chi(y)\), equal to one for
\(|y|\le\rho/2\) and zero for \(|y|\ge\rho\), with \(0<\rho<1\).
On the support of \(\chi_g(x)=\chi(gx)\), the exact field formulas
give the pointwise remainder bound
\[
 |(\widetilde H_g-H_0-gH_1-g^2H_2)f(x)|
 \le C_{L,a}g^3(1+|x|)^8
                    \sum_{|\alpha|\le2}|\partial^\alpha f(x)|.
 \tag{28a}
\]
To verify its polynomial degree, the exact logarithmic-field remainder
is \(g^4F_g\); its coefficients and first derivatives are bounded by
\(C(1+|x|)^4\) when \(g|x|<1\). Squaring the fields leaves products
of degrees at most eight, with powers of \(g\) at least three after
subtracting the first three coefficients. The Wilson fifth derivative
is bounded by \(2(\sum_i|v_i|/2)^5\), since each exponential is
unitary on the real integration interval. Its Taylor remainder,
multiplied by \(1/(2g^2a)\), obeys the same bound. These are finitely
many original graph terms, so their constants sum to \(C_{L,a}\).

Every derivative through order two of
\(\chi_g(\Phi+g\phi_1+g^2\phi_2)\) is bounded by a fixed polynomial
times \(e^{-\lambda_{\min}(B)|x|^2/2}\), uniformly for \(g\le1\).
This follows from the product rule, the finite Gaussian-polynomial
form of \(\phi_1,\phi_2\), and the factor \(g^{|\alpha|}\) in each
cutoff derivative. Integrating (28a) therefore gives an \(O(g^3)\)
norm remainder with no growing logarithmic cutoff factor.
Commutators of \(H_0,H_1,H_2\) with \(\chi_g\) are supported on
\(|x|\ge\rho/(2g)\); their coefficients and derivatives grow only
polynomially. In polar coordinates each such Gaussian tail is
bounded by \(C_Ng^N\) for every fixed \(N\), since a polynomial
times \(e^{-c/g^2}\) is smaller than every power of \(g\).
This proves the cutoff error as well as the coefficient error.

Let \(U_g\) be the inverse of the exact tree/Haar/dilation map on this
chart, and set
\[
 q_g=U_g\chi_g(\Phi+g\phi_1+g^2\phi_2),\qquad
 \lambda_g=e_0+g^2e_2.
 \tag{28b}
\]
The original vectors \(q_g\) are smooth and physical. The coefficient
equations, the preceding bounds, and odd/even parity give
\[
 \|(H_g-\lambda_g)q_g\|=O_{L,a}(g^3),\qquad
                     \|q_g\|^2=1+O_{L,a}(g^4).
 \tag{28c}
\]
The full fixed-box physical eigenvalue convergence isolates its
actual ground state \(\psi_g\) from the rest of the physical spectrum
by a positive fixed-box constant for small \(g\).
The spectral theorem applied to the residual in (28c) thus gives
\(\|(I-|\psi_g\rangle\langle\psi_g|)q_g\|=O(g^3)\).
The real coefficient \(\beta_g=\langle\psi_g,q_g\rangle\) has
absolute value \(1+O(g^4)\). It is positive: the leading chart
vector \(U_g\chi_g\Phi\) is nonnegative and its difference from
\(q_g\) has norm \(O(g)\), excluding a coefficient near \(-1\).
Taking the vacuum component of the residual proves
\(|\mathcal E_g-\lambda_g|=O(g^3)\), and its orthogonal component
proves
\[
 \|\psi_g-q_g\|+\|H_g(\psi_g-q_g)\|=O_{L,a}(g^3).
 \tag{28d}
\]
For the graph term explicitly use
\((H_g-\mathcal E_g)q_g=(H_g-\lambda_g)q_g+
(\lambda_g-\mathcal E_g)q_g\) and boundedness of \(\mathcal E_g\)
at this fixed box. No differentiability assumption at \(g=0\)
or self-adjointness of a global cubic-polynomial truncation was used.

The graph estimate controls the original weighted energies too.
Write \(K=\sum E_e\) and \(W=\sum_p(2-\operatorname{tr}U_p)\).
Each face trace is a fundamental matrix coefficient in each of its
four independent edge variables. Its Casimir sum is three times
that trace, so \(KW=3W-6|P|\). Integration by parts gives, for
every smooth original \(u\),
\[
 \begin{split}
 \|H_gu\|^2={}&\|(2g^2/a)Ku\|^2+\|Wu/(2g^2a)\|^2\\
 &+{2\over a^2}\sum_{e,\alpha}\int W|X_{e,\alpha}u|^2
                 +{1\over a^2}\int(3W-6|P|)|u|^2.
 \end{split}
 \tag{28e}
\]
Indeed
\(\operatorname{Re}\langle Ku,Wu\rangle
=\sum\int W|Xu|^2+\tfrac12\int(KW)|u|^2\);
the product of the two original Hamiltonian coefficients is \(a^{-2}\).
The sum of the first two squared norms in (28e) is at most
\(\|H_gu\|^2+6|P|\|u\|^2/a^2\).
Simultaneous Peter--Weyl diagonalization of the commuting nonnegative
\(E_e\) proves
\(\|\sum h_eE_eu\|\le\|h\|_\infty\|Ku\|\), and pointwise
\(|W_h|\le\|h\|_\infty W\), with the original face average.
Thus
\[
 \|D_{h,g}u\|\le\sqrt2\,\|h\|_\infty
          [\|H_gu\|^2+6|P|\|u\|^2/a^2]^{1/2}.
 \tag{28f}
\]
Smooth approximation in the \(H_g\) graph extends this inequality
to that domain. In particular (28d) supplies an \(O(g^3)\) error
for each fixed weighted energy vector, without an unproved tail
interpolation or a loss of \(g^{-2}\).

Every \(\sigma_\mu,\mathsf A,B,M,s,t\) is independent of \(a\).
The tensor \(\Theta\) carries exactly one factor \(1/a\), so
\(e_2=a^{-1}\mathfrak e_2(L)\) with \(\mathfrak e_2(L)\) given by (27)
after retaining that factor. No boundedness of \(\mathfrak e_2(L)\)
as \(L\to\infty\), or of the fixed-box remainder along a continuum
trajectory, is asserted. Their dependence is the next calculation,
not a permission to discard this coefficient. A vacuum-energy coefficient
alone is not an excitation-gap coefficient: local centered states and
the vacuum-subtracted semigroup must be expanded too.

## 7. The first physical gap: a specified six-by-six interaction matrix

The vacuum coefficient is not enough for a gap calculation. The same
full graph gives a finite explicit matrix for the first physical cluster.
Let \(\sigma_*=\min_\mu\sigma_\mu\) and \(I_*\) be its three spatial
modes. Write \(\delta_*=2\sigma_*/a\). For \(\mu,\nu\in I_*\), define
the following six real polynomials:
\[
 P_{\mu\mu}={\sigma_*\over2\sqrt6}
                 (|z_\mu|^2-6/\sigma_*),\qquad
 P_{\mu\nu}={\sigma_*\over2\sqrt3}z_\mu\cdot z_\nu\quad(\mu<\nu).
 \tag{29}
\]
The vectors \(S_I=P_I\Phi\) are an orthonormal basis for the full first
physical cluster. Indeed their norms and mutual inner products follow
from the independent covariance \(2I_3/\sigma_*\); (19) gives excitation
\(\delta_*\). A one-quantum vector has no SO(3) invariant component.
Every state with at least two quanta has excitation at least
\(\delta_*\), with equality only for two lowest-mode quanta. The invariant
bilinear color tensor is a multiple of \(\delta_{\alpha\beta}\):
half-turns remove off-diagonal entries and quarter-turns equate the
diagonal entries. Symmetry in the mode pair then gives precisely (29).

The formulas below compute every matrix element using the original
coefficients, with no numerical cutoff on intermediate oscillator modes.
In \(x\) coordinates, write \(\widehat P_I(x)=P_I(\mathsf A^{-1}x)\).
Let \(P_3(x)\) denote the cubic polynomial on the right of (15). Define
\[
 F_I(x)={4\over a}(A_1(x)p)\cdot\nabla\widehat P_I(x)
                                      +\widehat P_I(x)P_3(x).
 \tag{30}
\]
Then \(H_1S_I=F_I\Phi\). Expanding \(H_1(\widehat P_I\Phi)\)
with (14) proves this: the omitted-looking term
\(-2A_1:\nabla^2\widehat P_I/a\) is identically zero, not discarded.
The Hessian of each polynomial (29), after the chord-index map, is a
spatial matrix times the color identity; (9) contracts it to zero.
The divergence and trace contractions already proved after (10) remove
the other two terms.

For a multi-index \(n=(n_{\mu\alpha})\), let
\[
 h_n(z)=\prod_{\mu,\alpha}
 {\operatorname{He}_{n_{\mu\alpha}}(\sqrt{\sigma_\mu/2}\,
                                          z_\mu^\alpha)
          \over\sqrt{n_{\mu\alpha}!}},\qquad
 \omega_n={1\over a}\sum_{\mu,\alpha}\sigma_\mu n_{\mu\alpha}.
 \tag{31}
\]
Here the probabilists' Hermite polynomial has the explicit expansion
\[
 \operatorname{He}_k(u)
 =k!\sum_{j=0}^{\lfloor k/2\rfloor}
                  {(-1)^j u^{k-2j}\over2^j j!(k-2j)!}.
 \tag{32}
\]
The complete Hermite eigenbasis is \(h_n\Phi\), with excitation
\(\omega_n\). Put
\[
 c_{I,n}=\langle h_n,F_I(\mathsf A z)\rangle_{\Phi^2}.
 \tag{33}
\]
This is an evaluated finite prescription: substitute (30),(32) and
take moments by pairing coordinates with
\(\langle z_\mu^\alpha z_\nu^\beta\rangle
=2\delta_{\mu\nu}\delta_{\alpha\beta}/\sigma_\mu\).
For degree \(2q\) a monomial moment is the sum over all
\((2q-1)!!\) pairings of its coordinate slots, of the products of these
displayed covariances. Odd moments are zero. Thus (33) hides neither
an integral requiring a new measure nor an unspecified state-space
truncation.

Only \(|n|=3\) and \(|n|=5\) occur. Polynomial (30) has degree at most
five and odd parity, so the only other possible degree is one.
Its projection to one-quantum states is zero: (30) is invariant under
simultaneous color rotation, that projection commutes with the rotations,
and the one-quantum subspace contains no invariant vector.
This proves the exclusion of degree one, independently of any accidental
frequency equality elsewhere in the unrestricted oscillator spectrum.
In particular every remaining denominator below satisfies
\(\omega_n-\delta_*\ge\sigma_*/a>0\).

All quartic cluster matrix elements are equally explicit. For real
polynomials \(P_I,P_J\), put
\[
 u_I(x)=\nabla\widehat P_I(x)-p\,\widehat P_I(x).
 \tag{34}
\]
Integration by parts in the full \(H_2\) gives
\[
 V_{IJ}={2\over a}\langle u_I^*A_2u_J\rangle_{\Phi^2}
       -{\operatorname{tr}G\over2a}\delta_{IJ}
       +{1\over2a}\langle\widehat P_I W_4\widehat P_J\rangle_{\Phi^2}.
 \tag{35}
\]
Every expectation in (35) is a polynomial moment of degree at most
eight, computed by the same complete pairing prescription, now using
\(M_{cd}\delta_{\alpha\beta}\) in \(x\). The full order-two physical
gap matrix is
\[
 \boxed{\mathsf K_{IJ}=
 V_{IJ}-\sum_{\substack{n:\ |n|=3\ {\rm or}\ 5}}
              {c_{I,n}c_{J,n}\over\omega_n-\delta_*}
                                      -e_2\delta_{IJ}.}
 \tag{36}
\]
The sum in (36) ranges over all \(3r\) real oscillator coordinates.
It is finite because its total degree is fixed, not because high spatial
modes have been removed. Formula (36), together with (8)--(17),(24),
(26),(29)--(35), is a complete finite algorithm in the actual graph
matrices, signs and frequencies. It has not been replaced by an
undetermined perturbation matrix.

Here is the spectral meaning and its fixed-box error justification.
First omit the last \(-e_2I\) in (36), calling the resulting matrix
\(\mathsf K^{\rm abs}\). With \(R_*\) the reduced inverse of
\(H_0-e_0-\delta_*\) off the six-dimensional physical cluster, set
\[
 \eta_I=-R_*H_1S_I,\qquad
 (H_0-e_0-\delta_*)\zeta_I
 =-H_1\eta_I-H_2S_I+\sum_JS_J\mathsf K^{\rm abs}_{JI}.
 \tag{37}
\]
Equation (33) explicitly evaluates \(\eta_I\) through its positive
denominators; orthogonality of the right side in the second equation
follows from (35)--(36). The right side is a finite Gaussian polynomial.
The inverse on its orthogonal complement is obtained by dividing its
Hermite coefficients by their nonzero excitation differences. Physical
invariance removes any nonphysical resonant components; in the physical
space the eigenspace at this energy is precisely the six vectors (29).
Add the cluster component
\(-\tfrac12\sum_JS_J\langle\eta_J,\eta_I\rangle\) to \(\zeta_I\).
The Gram matrix of \(S_I+g\eta_I+g^2\zeta_I\) is then \(I+O(g^3)\).

Apply a fixed original-chart radial cutoff and the exact map (5) to
these six polynomial Gaussians. The compact coefficient remainder and
Gaussian-tail argument (28a)--(28c) apply to this finite
list exactly as to the vacuum: its residual as a six-column map is
\(O_{L,a}(g^3)\) for the matrix
\((e_0+\delta_*)I+g^2\mathsf K^{\rm abs}\).
The previously proved physical eigenvalue convergence isolates a
six-dimensional actual cluster with positive distance from the rest
of the fixed-box physical spectrum. Projecting the six columns to that
cluster changes them by \(O(g^3)\): first diagonalize the real symmetric
\(\mathsf K^{\rm abs}\) by an orthogonal six-by-six matrix, retain this
change in the six columns, and apply the off-cluster resolvent at each
corresponding \((e_0+\delta_*)+g^2\lambda_I(\mathsf K^{\rm abs})\)
to its residual. All six spectral separations remain positive at this
fixed box for sufficiently small \(g\). The projected Gram
matrix is still \(I+O(g^3)\). Multiplication by its explicitly retained
positive inverse square root makes a unitary identification with
\(\mathbb R^6\) and changes the represented energy matrix by \(O(g^3)\).
The finite-dimensional min--max principle bounds each eigenvalue error
by that matrix norm. Subtracting the actual vacuum expansion in (28)
therefore proves
\[
 \boxed{\Delta_L(g,a)=
       {2\sigma_*\over a}+g^2\lambda_{\min}(\mathsf K)
                                     +O_{L,a}(g^3).}
 \tag{38}
\]
This is the actual first physical gap at a fixed box. It is not a
uniform claim as the lattice and volume change. In particular (36)
must still be analyzed, rather than assigned a sign or neglected, to
decide what its correction does along a specified physical-scale
trajectory. The Haar scalar cancels between (35) and the same scalar
in \(e_2\), as it must for a gap; it remains present in the absolute
vacuum and absolute cluster energies.

## 8. Exact cancellation of spectator vacuum contributions

There is a further cancellation that is relevant before estimating any
large-box limit. It can be proved with the full mode set retained.
Factor the oscillator Hilbert space into the three lowest spatial modes
and all remaining modes, with vacua \(\Phi_*\) and \(\Phi_{\rm out}\).
This is only a tensor-factor identification of the complete comparison
space. The original Hamiltonian is not restricted to either factor.

To specify its operator coefficients in this identification, introduce
\[
 z_\mu^\alpha=\sqrt{2/\sigma_\mu}\,
                  (a_{\mu\alpha}+a_{\mu\alpha}^\dagger),\qquad
 \partial_{z_\mu^\alpha}=\sqrt{\sigma_\mu/8}\,
                  (a_{\mu\alpha}-a_{\mu\alpha}^\dagger).
 \tag{39}
\]
Substitute \(x=\mathsf A z\) and
\(\partial_x=\mathsf A^{-*}\partial_z\) in (14), then use (39).
Order every creation operator to the left with the exact identity
\[
 a_i a_j^\dagger=a_j^\dagger a_i+\delta_{ij}.
 \tag{40}
\]
This is a terminating finite algorithm: each interchange reduces the
number of out-of-order pairs, and its additional contraction has two
fewer operator factors. No contraction is omitted. Each scalar left
by this procedure is retained. The resulting \(H_1\) has degrees
at most three and odd parity. A degree-one term would be a
color-invariant vector operator. Its coefficient must vanish under all
color rotations, just as a one-quantum invariant vector must vanish.
Thus the nonzero normal-ordered terms of \(H_1\) have degree three.
The normal-ordered \(H_2\) has degrees zero, two and four.

Define \(H_{n,\rm out}\) by collecting all these computed monomials
whose spatial mode indices lie outside \(I_*\); include the scalar term
in \(H_{2,\rm out}\). Define
\[
 H_{n,\rm touch}=H_n-H_{n,\rm out},\qquad n=1,2.
 \tag{41}
\]
Every monomial of \(H_{n,\rm touch}\) contains at least one operator
from a lowest mode. This decomposition specifies its coefficients by
(8)--(14),(39)--(40); it is not a discarded part of the calculation.
Because color rotations preserve the mode labels, each summand remains
an invariant operator.

For any first-cluster vector \(S_I=P_I\Phi_*\otimes\Phi_{\rm out}\),
\(H_{1,\rm out}S_I\) has exactly two lowest-mode quanta and three
outside quanta. Indeed only three-creation monomials of \(H_{1,\rm out}\)
survive on \(\Phi_{\rm out}\). Conversely \(H_{1,\rm touch}S_J\) has at
most two outside quanta, since every degree-three monomial has at least
one lowest-mode factor. These two vectors are orthogonal, even after
inserting the oscillator reduced inverse \(R_*\), because that inverse
is diagonal in the occupation-number basis. No energy estimate is
being substituted for this orthogonality.

On the first vector, \(R_*\) acts on its outside factor by the inverse
outside excitation energy: the two lowest-mode quanta have energy
\(\delta_*\), exactly canceled by the reference energy in \(R_*\).
Therefore
\[
 \langle H_{1,\rm out}S_I,R_*H_{1,\rm out}S_J\rangle
 =\delta_{IJ}\,
       \langle H_{1,\rm out}\Phi,R_0H_{1,\rm out}\Phi\rangle.
 \tag{42}
\]
In the vacuum, \(H_{1,\rm out}\Phi\) has no lowest-mode quanta,
whereas each surviving three-creation term of
\(H_{1,\rm touch}\Phi\) has at least one. Their \(R_0\)-inserted
cross terms vanish for the same occupation-number reason.

The quartic and density contributions cancel in the corresponding
way, without an inverse:
\[
 \langle S_I,H_{2,\rm out}S_J\rangle
       =\delta_{IJ}\langle\Phi,H_{2,\rm out}\Phi\rangle .
 \tag{43}
\]
This identity includes every scalar arising from (40) as well as the
original Haar scalar. Normal ordering also gives
\(\langle\Phi,H_{2,\rm touch}\Phi\rangle=0\): each of its monomials
contains a lowest-mode creation or annihilation operator, and the
normal-ordered vacuum expectation of such a monomial is zero.

Combining (42)--(43) with the full, unaltered gap matrix (36) proves
the alternative exact formula
\[
 \boxed{\begin{split}
 \mathsf K_{IJ}={}&
  \langle S_I,H_{2,\rm touch}S_J\rangle
       -\delta_{IJ}\langle\Phi,H_{2,\rm touch}\Phi\rangle\\
 &-\langle H_{1,\rm touch}S_I,R_*H_{1,\rm touch}S_J\rangle
       +\delta_{IJ}\langle H_{1,\rm touch}\Phi,
                                      R_0H_{1,\rm touch}\Phi\rangle .
 \end{split}}
 \tag{44}
\]
The first vacuum expectation displayed here is zero as just proved.
The last expectation is (22) with precisely those triples intersecting
\(I_*\), not the sum of every outside vacuum triple. The middle inverse
is still evaluated by (31)--(33), and now its vectors have at most two
outside quanta. This proves that contributions acting exclusively on
spectator modes cancel from the physical gap, including their full
denominators. It does not assert convergence of the remaining outside
mode sums or identify a renormalized coupling.

Equations (36) and (44) retain both sides of the cancellation explicitly.
They explain why a divergent absolute vacuum-energy coefficient cannot
by itself determine the gap correction, and give a more targeted exact
sum for the next volume and physical-scale estimates.

## Sources and proof dependencies

The included *The original finite-box SU(2) Hamiltonian at small positive
coupling* proves the global tree map, Haar identity, physical operator,
unique well and actual finite-box spectral convergence.
*Full graph operator coupling coefficients* supplies the exact chart
remainder and weighted versions of (14).
Sections 6--7 above promote the coefficients to the actual finite-box
vacuum, weighted graph vectors and first physical spectral cluster.

J. Kogut and L. Susskind, *Hamiltonian formulation of Wilson's lattice
gauge theories*, Physical Review D 11 (1975), 395–408,
[doi:10.1103/PhysRevD.11.395](https://doi.org/10.1103/PhysRevD.11.395),
is the foundational Hamiltonian reference. Its coupling conventions are
not substituted for the explicitly retained coefficients in (1).

S. Chatterjee, *Yang–Mills for probabilists*,
[arXiv:1803.01950](https://arxiv.org/abs/1803.01950), sections on
Wilson loops and defining the continuum limit. The preserved primary
TeX was read for the relation between lattice correlations, physical
scale and the continuum limit; it does not prove a volume-uniform
bound on the new finite-box sums (27).
