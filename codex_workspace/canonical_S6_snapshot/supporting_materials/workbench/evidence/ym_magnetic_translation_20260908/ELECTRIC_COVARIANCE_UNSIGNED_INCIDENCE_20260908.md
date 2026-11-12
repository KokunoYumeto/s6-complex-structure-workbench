# Actual-vacuum electric covariance, the full unsigned incidence kernel, and its first surviving states

8 September 2026. The Hamiltonian contains every link and every elementary plaquette of the full open three-dimensional \(SU(2)\) spatial box. This proof computes its true-vacuum covariance and energy matrices, gives the entire finite unsigned incidence kernel, and calculates the first nonzero interacting vacuum state for every nonzero real weight in that leading kernel. The kernel is not identified with an exact all-coupling zero-state space.

## 1. Complete finite model and domains

Fix an integer \(L\ge2\), put \(m=2L\), and let the vertices be \(n\in\{-L,\ldots,L\}^3\). The physical links are all \(e=(n,i)\), directed from \(n\) to \(n+\mathbf e_i\) when both endpoints are in the box. A reversed traversal uses \(U_e^{-1}\). The elementary faces \(p=(n;i,j)\), \(i<j\), have Wilson functions

\[
W_p=\operatorname{tr}\big[
U_i(n)U_j(n+\mathbf e_i)U_i(n+\mathbf e_j)^{-1}U_j(n)^{-1}
\big].
\tag{1.1}
\]

The full edge and face sets are \(\mathsf E_L,\mathsf P_L\), with

\[
N=3m(m+1)^2,\qquad M=3m^2(m+1).
\tag{1.2}
\]

These counts follow by choosing the direction of a link, or plane of a face, then its allowed coordinate ranges. There are no periodic identifications.

Use product Haar probability measure \(dU\) on \(SU(2)^{\mathsf E_L}\), and

\[
T_a=-i\sigma_a/2,\quad -2\operatorname{tr}(T_aT_b)=\delta_{ab},\qquad
X_{e,a}f=\left.\frac{d}{dt}f(\ldots,e^{tT_a}U_e,\ldots)\right|_{t=0},
\]
\[
E_e=-\Delta_e^T=-\sum_aX_{e,a}^2,\quad
H_0=\sum_eE_e,\quad \mathcal V=\sum_pW_p,\quad \xi=b/\kappa,
\]
\[
H_{\kappa,b}=\kappa H_0+b\sum_p(2-W_p)
=\kappa(H_0-\xi\mathcal V)+2bM I,\qquad \kappa,b>0.
\tag{1.3}
\]

All \(E_e\) are nonnegative self-adjoint link Casimirs and commute with one another on the common smooth core and in their joint product spectral decomposition. The original metric and physical constants remain

\[
c(X,Y)=-\tfrac12\operatorname{tr}(XY),\quad
\Delta_e^c=4\Delta_e^T,\quad
\kappa=\frac{2g_{\mathrm{YM}}^2}{a},\quad
b=\frac1{2g_{\mathrm{YM}}^2a},\quad
\xi=\frac1{4g_{\mathrm{YM}}^4}.
\tag{1.4}
\]

The exact Wilson scalar \(2bM\) is retained in (1.3).

Let \(\psi_\xi>0\) be the normalized positive vacuum and \(E_\xi\) its physical ground energy. Compactness and ellipticity give a smooth ground eigenfunction and compact resolvent; the bounded smooth potential preserves the free operator domain. The ground minimizer can be taken nonnegative by the form inequality \(|\nabla|f||\le|\nabla f|\), with zeros handled by \(\sqrt{|f|^2+\varepsilon^2}\). The strong maximum principle makes it strictly positive. Integration by parts against its eigen-equation gives

\[
\mathfrak q_\xi(\psi_\xi F,\psi_\xi G)
=\kappa\sum_{e,a}\int\psi_\xi^2\,
\overline{X_{e,a}F}X_{e,a}G\,dU,
\tag{1.5}
\]

where \(\mathfrak q_\xi\) is the closed form of \(H_{\kappa,b}-E_\xi\). A second ground state divided by \(\psi_\xi\) would make every derivative in (1.5) zero, hence would be constant. This proves uniqueness. Gauge transformations act by \(U_e\mapsto g_{s(e)}U_eg_{t(e)}^{-1}\); link Casimirs and Wilson traces intertwine this action. Uniqueness makes \(\psi_\xi\) invariant. The original convention \(U_e\mapsto h_{s(e)}^{-1}U_eh_{t(e)}\) is exactly this action with \(g_v=h_v^{-1}\).

Define smooth invariant, vacuum-orthogonal vectors and finite real matrices by

\[
\gamma_{e,\xi}=\langle\psi_\xi,E_e\psi_\xi\rangle,\qquad
v_{e,\xi}=(E_e-\gamma_{e,\xi})\psi_\xi,
\]
\[
C_{ef}(\xi)=\langle v_{e,\xi},v_{f,\xi}\rangle,\qquad
\mathcal N_{ef}(\xi)=\mathfrak q_\xi(v_{e,\xi},v_{f,\xi}).
\tag{1.6}
\]

Both matrices are positive semidefinite and real symmetric by their Gram definitions and reality of every operator and state. Smoothness ensures all vectors belong to the physical form and operator domains. All perturbation remainders below are on the fixed finite box and may depend on \(L\); no volume-uniform estimate is asserted.

## 2. True-vacuum expansion and the leading matrices

The free single-link spin-\(j\) Casimir is \(j(j+1)\). Its normalization is fixed by \(-\sum_aT_a^2=3I/4\) on the fundamental representation; the general value follows from the angular-momentum raising/lowering matrices. The Peter--Weyl tensor decomposition gives a simple free constant eigenvector and full-space first nonzero eigenvalue \(3/4\). Each elementary face uses four distinct fundamental links, so

\[
E_eW_p=\tfrac34\,\mathbf1_{\{e\in\partial p\}}W_p,\qquad
H_0W_p=3W_p,\qquad
\int W_pW_q\,dU=\delta_{pq},\qquad \int W_p\,dU=0.
\tag{2.1}
\]

For the Haar identities, a singly occurring link can be multiplied by \(-I\) to reverse the sign of its fundamental entries. Distinct elementary faces have distinct four-edge supports, so one integrates an edge in only one of the supports. Equal faces reduce to \(\int(\operatorname{tr}U)^2dU=1\), since the scalar component of a uniformly distributed unit quaternion has second moment \(1/4\). A square's two directions and coordinate minima can be recovered from its edge support, justifying the distinct-support assertion.

The potential norm is exactly \(\|\mathcal V\|_\infty=2M\), by \(|W_p|\le2\) and the all-identity configuration. The free resolvent on \(|z|=3/8\) has norm at most \(8/3\), giving the explicit spectral-projection Neumann disk

\[
|\xi|<\frac3{16M}.
\tag{2.2}
\]

Its contour projection has rank one analytically near zero and throughout that disk. For real \(\xi\) in it, the lowest eigenvalue of \(H_0-\xi\mathcal V\) lies in \([-2M|\xi|,0]\), while the next is at least \(3/4-2M|\xi|>3/8\), so it is the actual ground projection. A local analytic Haar-mean-one eigenvector \(\phi_\xi\) is obtained by projecting 1 and dividing by its nonzero Haar mean. Differentiating its eigen-equation and then normalizing in \(L^2\) gives

\[
\psi_\xi=1+\xi A+\xi^2D+O_L(\xi^3),\qquad
A=\tfrac13\mathcal V,\qquad
\int D\,dU=-M/18.
\tag{2.3}
\]

Here the auxiliary dimensionless eigenvalue has \(e(0)=e'(0)=0\), and \(E_\xi=\kappa e(\xi)+2bM\) exactly. Analyticity and its remainders hold in every fixed Sobolev space: from
\[
\phi_\xi=(H_0+1)^{-1}[(e(\xi)+1+\xi\mathcal V)\phi_\xi]
\]
one gains two derivatives at a time, because multiplication by the fixed smooth potential is bounded on those spaces. Thus applying any fixed number of the differential operators below is justified on the actual analytic vacuum.

Let \(r_e=|\{p:e\in\partial p\}|\), and
\[
\mathsf I_{pe}=\mathbf1_{\{e\in\partial p\}},\qquad
t_{ef}=\sum_p\mathsf I_{pe}\mathsf I_{pf}.
\tag{2.4}
\]
Thus \(t_{ef}\) is the number of elementary faces containing both physical edges; \(t_{ee}=r_e\). Equation (2.1) gives

\[
E_eA=\tfrac14\sum_{p\ni e}W_p,\qquad
\gamma_{e,\xi}=\frac{\xi^2}{12}r_e+O_L(\xi^3),\qquad
v_{e,\xi}=\frac{\xi}{4}\sum_{p\ni e}W_p+O_L(\xi^2).
\tag{2.5}
\]

For the expectation coefficient, all terms pairing an \(E_e\)-derivative against the constant vanish by Haar integration, and
\(\langle A,E_eA\rangle=(3/4)r_e/9=r_e/12\). Equation (2.5) holds in every fixed sufficiently high Sobolev norm, not merely weakly.

The exact parity that improves all scalar remainders is the central link cochain

\[
z_i(n)=(-1)^{\sum_{k<i}n_k}I,\qquad
(\mathcal Zf)(U)=f((z_e^{-1}U_e)_e).
\tag{2.6}
\]

For a face \(i<j\), the factor \(z_j(n+\mathbf e_i)\) has the opposite sign from \(z_j(n)\), while \(z_i(n+\mathbf e_j)=z_i(n)\). Thus the product of its four center factors is \(-1\), on every face in all three planes. Therefore
\[
\mathcal Z\mathcal V=-\mathcal V,\quad
\mathcal Z(H_0-\xi\mathcal V)\mathcal Z^{-1}=H_0+\xi\mathcal V.
\]
The real unitary involution \(\mathcal Z\) commutes with every \(E_e\). Uniqueness of the positive vacuum gives
\[
\psi_{-\xi}=\mathcal Z\psi_\xi,\quad e(-\xi)=e(\xi),\quad
\gamma_{e,-\xi}=\gamma_{e,\xi},\quad
v_{e,-\xi}=\mathcal Zv_{e,\xi}.
\tag{2.7}
\]
Negative \(\xi\) is used only in this finite analytic argument. The physical coupling is positive. Both matrix entries in (1.6) are even real-analytic functions of \(\xi\), because the excitation operator \(\kappa(H_0-\xi\mathcal V-e(\xi))\) is conjugated to its negative-\(\xi\) version by \(\mathcal Z\).

Using (2.1), (2.5), and this evenness now proves, with all constants,

\[
\boxed{
C_{ef}(\xi)=\frac{\xi^2}{16}\,t_{ef}+O_L(\xi^4),\qquad
\mathcal N_{ef}(\xi)=\frac{3\kappa\xi^2}{16}\,t_{ef}
+O_L(\kappa\xi^4).}
\tag{2.8}
\]

The expectation in (2.5) likewise has remainder \(O_L(\xi^4)\). There are finitely many entries, so the matrix remainder bounds also hold in any fixed matrix norm, with a box-dependent constant. In particular \(\mathcal N=3\kappa C+O_L(\kappa\xi^4)\), but this does not justify taking their quotient along a weight on which the leading matrix vanishes.

For completeness the numerator has the exact, not perturbative, finite-range identity

\[
\mathcal N_{ef}
=\tfrac12\langle\psi_\xi,[E_e,[H_{\kappa,b},E_f]]\psi_\xi\rangle
=\frac b2\sum_{p:\,e,f\in\partial p}
\langle\psi_\xi,[E_e,[2-W_p,E_f]]\psi_\xi\rangle.
\tag{2.9}
\]

Expand the double commutator into four terms, use the vacuum equation on the two endpoint \(H\)'s, and use commutation of \(E_e,E_f\). Reality and symmetry turn the result into twice (1.6). The electric Hamiltonian commutes with each \(E_f\). If \(f\notin p\), its derivatives commute with multiplication by \(W_p\); if \(f\in p\) but \(e\notin p\), the resulting differential coefficients involve only \(p\)'s variables, and commute with \(E_e\). This proves the support in (2.9). No comparable all-coupling finite-range claim is made for \(C\).

## 3. Entire kernel of the unsigned edge-to-face map

For real or complex weights \(w=(w_e)\), define

\[
(\mathsf Iw)_{n;i,j}
=w_i(n)+w_j(n+\mathbf e_i)+w_i(n+\mathbf e_j)+w_j(n).
\tag{3.1}
\]

The leading covariance kernel in (2.8) is exactly \(\ker\mathsf I\), because
\(\sum_{e,f}\overline{w_e}t_{ef}w_f=\sum_p|(\mathsf Iw)_p|^2\).
We now give all such weights, with unique finite parameters.

Let \(\ell=-L\), and put \(\varepsilon(n)=(-1)^{n_1+n_2+n_3}\). Write
\[
w_i(n)=\varepsilon(n)a_i(n),\qquad
D_iF(n)=F(n+\mathbf e_i)-F(n).
\tag{3.2}
\]
Substituting into (3.1) gives
\[
\mathsf Iw=0\quad\Longleftrightarrow\quad
D_ja_i+D_ia_j=0\quad (i\ne j)
\tag{3.3}
\]
on every contained face. These are equations on the actual edge arrays; their differences are taken only where all displayed points exist.

Choose freely:

- one function \(f_i(x)\) for each \(i\), with \(\ell\le x\le L-1\);
- one function \(\varphi_{ij}(x,y)\) for each \(i<j\), on \(\ell\le x,y\le L\), with the two exact anchor conditions
\[
\varphi_{ij}(\ell,y)=0,\qquad \varphi_{ij}(x,\ell)=0.
\tag{3.4}
\]

Then every kernel weight is represented uniquely by

\[
\boxed{
a_i(n)=f_i(n_i)
+\sum_{j>i}D_i\varphi_{ij}(n_i,n_j)
-\sum_{j<i}D_i\varphi_{ji}(n_j,n_i),\qquad
w_i(n)=\varepsilon(n)a_i(n).}
\tag{3.5}
\]

In the last sum, \(D_i\) differentiates the second argument, namely the coordinate \(n_i\); in the first it differentiates the first argument. All parameters have their stated edge or vertex domains, so (3.5) is defined at every physical link.

First, (3.5) satisfies (3.3). For a pair \(i<j\), all unrelated summands have zero cross derivative; its two relevant terms are \(D_jD_i\varphi_{ij}\) and \(-D_iD_j\varphi_{ij}\), which cancel. Thus every choice of parameters gives a kernel weight.

To prove completeness, take any solution of (3.3). For three distinct indices \(i,j,k\), the equations and commuting finite differences on every contained cube give
\[
D_kD_ja_i=-D_kD_ia_j
=D_iD_ja_k=-D_jD_ka_i.
\]
Therefore \(D_kD_ja_i=0\). For each fixed \(n_i\), the array \(a_i\) has zero mixed difference in its two transverse coordinates. Summing that mixed-difference equation across a transverse rectangle gives
\[
a_i(n)=f_i(n_i)+u_{ij}(n_i,n_j)+u_{ik}(n_i,n_k),
\tag{3.6}
\]
where
\[
f_i(x)=a_i(x\mathbf e_i+\ell\mathbf e_j+\ell\mathbf e_k),\qquad
u_{ij}(x,y)=a_i(x\mathbf e_i+y\mathbf e_j+\ell\mathbf e_k)-f_i(x).
\]
In particular \(u_{ij}(x,\ell)=0\). The original pair equation reduces to
\[
D_ju_{ij}+D_iu_{ji}=0.
\tag{3.7}
\]
For \(i<j\), define the anchored potential explicitly by the finite sum
\[
\varphi_{ij}(x,y)=\sum_{r=\ell}^{x-1}u_{ij}(r,y).
\tag{3.8}
\]
The empty sum is zero. This satisfies both (3.4) anchors and \(D_i\varphi_{ij}=u_{ij}\). Summing (3.7) in the first coordinate gives
\(D_j\varphi_{ij}=-u_{ji}\), because \(u_{ji}(y,\ell)=0\). Equations (3.6) and (3.8) now give exactly (3.5). They also reconstruct all its parameters uniquely from \(a\), proving uniqueness.

There are \(3m\) free \(f_i\) values and \(3m^2\) free anchored potential values. Thus

\[
\boxed{\dim\ker\mathsf I=3m(m+1)=N-M,\qquad
\operatorname{rank}\mathsf I=M.}
\tag{3.9}
\]

In particular this unsigned incidence map is onto the full face array space. This conclusion follows from the proved parametrization and rank-nullity, not from a numerical rank test.

A useful explicit family in the kernel is

\[
w_1(n)=(-1)^{n_2+n_3}F(n_1),\qquad w_2(n)=w_3(n)=0
\tag{3.10}
\]
for any prescribed function \(F\) on the direction-1 edge coordinate. Its opposite direction-1 edges cancel on every \(12\) and \(13\) face, while every \(23\) face has zero weight. In (3.5) it corresponds to \(f_1(n_1)=(-1)^{n_1}F(n_1)\), other \(f_i=0\), and all potentials zero.

The actual state for a real weight is
\[
\Gamma_w=\sum_ew_eE_e,\quad
\gamma_{w,\xi}=\langle\psi_\xi,\Gamma_w\psi_\xi\rangle,\quad
v_{w,\xi}=(\Gamma_w-\gamma_{w,\xi})\psi_\xi=\sum_ew_ev_{e,\xi}.
\tag{3.11}
\]
Equations (2.5) and (3.1) give
\[
v_{w,\xi}=\frac{\xi}{4}\sum_p(\mathsf Iw)_pW_p+O_{L,w}(\xi^2).
\tag{3.12}
\]
For \(w\in\ker\mathsf I\), this merely removes its order-\(\xi\) state. The next sections compute, rather than assume, what remains.

## 4. Exact adjacent-face modes and the complete second vacuum coefficient

Let \(\mathscr P_2\) be the set of unordered pairs of distinct elementary faces sharing an edge. Distinct faces in this open cubical box share at most one edge. For \(\{p,q\}\in\mathscr P_2\), denote that edge by \(e=e(p,q)\). Reverse one face traversal if necessary and cyclically base both words at an endpoint of \(e\), so they have the form

\[
P_*=U_eA,\qquad Q_*=U_e^{-1}B,\qquad Q'_*=BU_e^{-1}.
\tag{4.1}
\]

This does not change either \(SU(2)\) trace: trace is cyclic and \(\operatorname{tr}U^{-1}=\operatorname{tr}U\). The outer words \(A,B\) use three physical links each, disjoint from one another and from \(e\), with their actual inherited orientations. Define

\[
R_{pq}=\operatorname{tr}(AB),\qquad
D_{pq,0}=W_pW_q,\qquad
D_{pq,1}=D_{pq,0}-\tfrac12R_{pq}.
\tag{4.2}
\]

The first is the six-edge outer boundary Wilson loop. Its trace is independent of the choice of starting endpoint or total reversal, as is the definition of \(D_{pq,1}\).

The normalization (1.3) gives the Pauli completeness contraction

\[
\sum_a\operatorname{tr}(T_aC)\operatorname{tr}(T_aD)
=-\tfrac12\operatorname{tr}(CD)+\tfrac14\operatorname{tr}C\operatorname{tr}D.
\tag{4.3}
\]

This follows by multiplying the elementary matrix identity
\(\sum_a(\sigma_a)_{ij}(\sigma_a)_{kl}
=2\delta_{il}\delta_{jk}-\delta_{ij}\delta_{kl}\)
by the two matrices' entries and summing. On the shared edge the two derivatives are respectively
\(\operatorname{tr}(T_aP_*)\) and \(-\operatorname{tr}(T_aQ'_*)\), since the second occurrence is inverse. Therefore

\[
G_{pq}:=\sum_a(X_{e,a}W_p)(X_{e,a}W_q)
=\tfrac12R_{pq}-\tfrac14D_{pq,0}
=\tfrac38R_{pq}-\tfrac14D_{pq,1}.
\tag{4.4}
\]

Each outer edge acts with Casimir \(3/4\) on both functions in (4.2), because its fundamental or inverse fundamental matrix entries occur linearly. On \(e\), \(R_{pq}\) is constant. The product rule and (4.4) give
\[
\Delta_e^TD_{pq,0}=-\tfrac32D_{pq,0}+2G_{pq}
=R_{pq}-2D_{pq,0}=-2D_{pq,1}.
\]
Consequently the joint edge-Casimir labels and full electric eigenvalues are

\[
\begin{array}{c|ccc|c}
 &\text{six outer edges}&\text{shared edge }e&\text{all other edges}&H_0\\ \hline
R_{pq}&3/4&0&0&9/2\\
D_{pq,1}&3/4&2&0&13/2.
\end{array}
\tag{4.5}
\]

This retains every additional box link as spin zero, rather than deleting it from the Hamiltonian.

For their norms, condition on \(U_e\). The disjoint outer words \(A,B\) are independent Haar matrices by left/right Haar invariance and independence of their link variables. Thus \(P_*,Q'_*\) are independent Haar matrices. Write them as
\(p_0I+i\sum_ap_a\sigma_a\) and \(q_0I+i\sum_aq_a\sigma_a\). The two coefficient vectors are independent uniform points on the unit sphere in \(\mathbb R^4\), with second moments \(\mathbb E p_\alpha p_\beta=\delta_{\alpha\beta}/4\). Matrix multiplication gives
\[
R_{pq}=2(x-y),\qquad D_{pq,1}=3x+y,\qquad
x=p_0q_0,\quad y=\sum_{a=1}^3p_aq_a.
\]
Here \(\mathbb E x^2=1/16\), \(\mathbb E y^2=3/16\), and \(\mathbb E xy=0\). It follows that

\[
\|R_{pq}\|_0^2=1,\qquad
\|D_{pq,1}\|_0^2=3/4,\qquad
\langle R_{pq},D_{pq,1}\rangle_0=0.
\tag{4.6}
\]

All norms are full-box Haar norms; every extra link contributes the integral of 1.

The modes belonging to different unordered pairs are orthogonal as well. We give the geometry needed for that claim. The outer boundary of two coplanar adjacent unit faces is the edge set of a \(2\)-by-\(1\) rectangle. Its plane, bounding rectangle, and its unique two unit squares can be read from that edge set. For two perpendicular adjacent faces, their bounding box is a unit cube. Their outer six-edge boundary contains exactly six of its vertices; the two absent vertices form the edge opposite the shared edge. The missing edge and the cube determine the shared edge and its two incident faces uniquely. The coplanar and perpendicular cases have respectively two and three nonzero coordinate spans and cannot coincide. Therefore distinct unordered adjacent pairs have distinct six-edge outer supports.

Two \(R\)-modes with different outer supports have different eigenvalues for at least one \(E_f\) (fundamental versus zero), so self-adjointness makes them orthogonal. An \(R\)-mode and any \(D_1\)-mode are orthogonal because the latter has shared-edge eigenvalue 2 while the former has only eigenvalues 0 or \(3/4\). Two \(D_1\)-modes with different shared edges differ in the eigenvalue-2 location; if the shared edge is equal, the distinct outer supports give a \(3/4\)-versus-zero location. They are therefore also orthogonal. This proves full pairwise orthogonality of the displayed family on the whole box.

We can now write the actual complete second vacuum coefficient \(D\) in (2.3). The Haar-mean-one vacuum equation gives
\[
e(\xi)=-\frac M3\xi^2+O_L(\xi^3),\qquad
H_0\phi_2=\tfrac13(\mathcal V^2-M),\qquad \int\phi_2\,dU=0.
\tag{4.7}
\]
The first equality follows by pairing the second-order equation with 1 and using \(\langle\mathcal V,A\rangle=M/3\). The normalized coefficient is \(D=\phi_2-M/18\).

For a repeated face, \(W_p^2-1\) is the adjoint character: in eigenvalues \(e^{it},e^{-it}\), it equals \(e^{2it}+1+e^{-2it}\), the spin-1 character. On each of its four links its Casimir is 2, so its full eigenvalue is 8. For two faces without a common physical edge, the product has eight distinct fundamental link factors and full eigenvalue 6, even if the faces share a vertex. For adjacent faces use (4.2), (4.5). Inverting \(H_0\) on its mean-zero eigenfunctions in (4.7) gives

\[
\boxed{\begin{split}
D={}&-\frac M{18}+\frac1{24}\sum_p(W_p^2-1)\\
&+\frac19\sum_{\substack{\{p,q\}\\p\ne q,\ \partial p\cap\partial q=\varnothing}}W_pW_q\\
&+\sum_{\{p,q\}\in\mathscr P_2}
\left(\frac2{27}R_{pq}+\frac4{39}D_{pq,1}\right).
\end{split}}
\tag{4.8}
\]

The second and third sums are over unordered face pairs; the factor 2 for each distinct pair in \(\mathcal V^2\) is included in their coefficients. All cases of the full square \((\sum_pW_p)^2\) occur in (4.8). It is an exact Taylor coefficient of the true vacuum, not a two-face model for that vacuum.

## 5. First surviving state for every leading-null real weight

Take \(w\in\ker\mathsf I\), real. Then
\(\Gamma_w1=0\), \(\Gamma_wW_p=(3/4)(\mathsf Iw)_pW_p=0\), and hence \(\Gamma_wA=0\). It follows from the normalized analytic expansion that
\[
\gamma_{w,\xi}=O_{L,w}(\xi^4).
\tag{5.1}
\]
Indeed every term paired against a constant vanishes by self-adjointness and \(\Gamma_w1=0\). The order-\(\xi^2\) expectation is \(\langle A,\Gamma_wA\rangle=0\). The expectation is even by (2.7), so the cubic coefficient also vanishes.

Every repeated-face term in (4.8) is annihilated by \(\Gamma_w\): all its used edges have eigenvalue 2, giving \(2(\mathsf Iw)_p=0\). A pair without a shared edge is annihilated because its weighted Casimir is \((3/4)[(\mathsf Iw)_p+(\mathsf Iw)_q]=0\).

For an adjacent pair with shared edge \(e\), the sum of its six outer weights is
\[
\sum_{f\text{ outer}}w_f=(\mathsf Iw)_p+(\mathsf Iw)_q-2w_e=-2w_e.
\]
The joint Casimirs (4.5) therefore give exactly

\[
\Gamma_wR_{pq}=-\tfrac32w_eR_{pq},\qquad
\Gamma_wD_{pq,1}=\tfrac12w_eD_{pq,1}.
\tag{5.2}
\]

Apply these identities to the full expression (4.8), and then use (5.1) in the centered state (3.11). The actual first surviving term is

\[
\boxed{
v_{w,\xi}=\xi^2S_w+O_{L,w}(\xi^3),\qquad
S_w=\sum_{\{p,q\}\in\mathscr P_2}
w_{e(p,q)}\left(-\frac19R_{pq}+\frac2{39}D_{pq,1}\right).}
\tag{5.3}
\]

The error holds in every fixed Sobolev norm after applying \(\Gamma_w\), because the vacuum remainder was established in every sufficiently high Sobolev norm. Centering affects no term in (5.3).

Let

\[
\mathcal K_L(w,z)=\sum_{e\in\mathsf E_L}\binom{r_e}{2}w_ez_e,\qquad
\mathcal K_L(w)=\mathcal K_L(w,w).
\tag{5.4}
\]

Each unordered adjacent pair has a unique shared edge. Thus summing its shared-edge weight product is exactly (5.4). The pairwise mode orthogonality and norms (4.5)--(4.6) give, for real \(w,z\in\ker\mathsf I\),

\[
\begin{split}
\langle S_w,S_z\rangle_0
&=\left(\frac1{81}+\frac34\frac4{1521}\right)\mathcal K_L(w,z)
=\frac{196}{13689}\mathcal K_L(w,z),\\
\langle S_w,H_0S_z\rangle_0
&=\left(\frac{9/2}{81}+\frac{13}2\frac34\frac4{1521}\right)\mathcal K_L(w,z)
=\frac8{117}\mathcal K_L(w,z).
\end{split}
\tag{5.5}
\]

Every box edge has at least two incident faces: if \(e\) is direction \(i\), each of its two transverse coordinate directions supplies at least one face extending inward from the box boundary. Explicitly,
\[
r_{(n,i)}=d(n_j)+d(n_k),\qquad
d(x)=\begin{cases}1,&x=-L\text{ or }L,\\2,&-L<x<L,\end{cases}
\quad \{i,j,k\}=\{1,2,3\}.
\tag{5.6}
\]
Thus \(2\le r_e\le4\) and \(\mathcal K_L(w)>0\) for every nonzero real weight. In particular \(S_w\ne0\): all leading-null nonzero weights have a genuinely surviving second-order state.

Evenness (2.7) applies to every fixed real linear combination \(v_w\) and to its polarized norm and energy forms. The leading state in (5.3) is order \(\xi^2\); its scalar products therefore have leading order \(\xi^4\), and their possible \(\xi^5\) terms vanish. The exact excitation operator is \(\kappa(H_0-\xi\mathcal V-e(\xi))\). Equations (5.3)--(5.5) prove the complete restricted leading forms

\[
\boxed{\begin{split}
\langle v_{w,\xi},v_{z,\xi}\rangle
&=\frac{196}{13689}\xi^4\mathcal K_L(w,z)+O_{L,w,z}(\xi^6),\\
\mathfrak q_\xi(v_{w,\xi},v_{z,\xi})
&=\frac{8\kappa}{117}\xi^4\mathcal K_L(w,z)+O_{L,w,z}(\kappa\xi^6).
\end{split}}
\tag{5.7}
\]

For each fixed nonzero \(w\) in the kernel, its squared norm is positive for all sufficiently small positive \(\xi\), and division yields

\[
\boxed{
\frac{\mathfrak q_\xi(v_{w,\xi},v_{w,\xi})}{\|v_{w,\xi}\|_2^2}
=\frac{234}{49}\kappa+O_{L,w}(\kappa\xi^2).}
\tag{5.8}
\]

This quotient is the energy of the actual smooth invariant, vacuum-orthogonal vector in (3.11), not of a substituted free vacuum. Its leading value is between the two displayed free energies \(9\kappa/2\) and \(13\kappa/2\). The leading incidence kernel raises the first surviving order and removes the one-face energy \(3\kappa\); it does not make the normalized energy vanish.

One can make the distinction from an exact zero-state kernel stronger on each fixed box. Decompose the real edge space as \((\ker\mathsf I)^\perp\oplus\ker\mathsf I\). On the first summand (2.8) has a strictly positive \(\xi^2\) leading form, because \(\mathsf I\) is injective there. On the second, (5.7) has a strictly positive \(\xi^4\) leading form. Mixed matrix entries have zero \(\xi^2\) term and, by evenness, zero \(\xi^3\) term, hence are \(O_L(\xi^4)\). All are fixed finite matrices. If \(u,z\) belong respectively to these summands, their mixed contribution is bounded by \(B_L\xi^4\|u\|\|z\|\). The elementary inequality \(2ab\le a^2+b^2\), scaled by the positive \(\xi^2\) lower bound on the first summand, absorbs it into a portion of that bound plus \(O_L(\xi^6)\|z\|^2\). For sufficiently small positive \(\xi\), the latter is smaller than a portion of the positive \(\xi^4\) bound on the second summand. Thus the entire actual covariance matrix \(C(\xi)\) is positive definite on the real edge space for all sufficiently small positive \(\xi\), with a box-dependent interval. No assertion about arbitrary \(b/\kappa\) is inferred from this local result.

## 6. Explicit alternating family and the original native weight

For (3.10), the first surviving term is given explicitly by (5.3). Take first \(F(n_1)=1\). Only pairs whose shared edge is in direction 1 contribute, with the signed coefficient \((-1)^{n_2+n_3}\). The squared weight of each is 1. To count them exactly, hold \(n_1\) fixed. If both transverse coordinates are interior there are \((m-1)^2\) such edges with \(r_e=4\); if exactly one is on the boundary there are \(4(m-1)\) with \(r_e=3\); if both are on the boundary there are 4 with \(r_e=2\). Therefore

\[
\sum_{n_2,n_3}\binom{r_{(n,1)}}2
=6(m-1)^2+12(m-1)+4=6m^2-2.
\]
There are \(m\) possible \(n_1\), giving

\[
\boxed{\mathcal K_L(w)=m(6m^2-2)=48L^3-4L.}
\tag{6.1}
\]

For the complete family with arbitrary real \(F\),
\[
\mathcal K_L(w)=(6m^2-2)\sum_{n_1=-L}^{L-1}F(n_1)^2.
\tag{6.2}
\]
If \(F\ne0\), this is strictly positive. Substitution into (5.3), (5.7), and (5.8) gives the exact first surviving actual-vacuum state, its norm and energy coefficients, and its leading quotient for that specified family, with all faces retained.

The original native weights are instead

\[
w^{\mathrm{nat}}_{(n,1)}=n_2^2,\qquad
w^{\mathrm{nat}}_{(n,2)}=w^{\mathrm{nat}}_{(n,3)}=0.
\tag{6.3}
\]

Their unsigned sums, with \(t=n_2\), are
\[
(\mathsf Iw^{\mathrm{nat}})_{n;1,2}=t^2+(t+1)^2=2(t^2+t+\tfrac12),
\]
\[
(\mathsf Iw^{\mathrm{nat}})_{n;1,3}=2t^2,\qquad
(\mathsf Iw^{\mathrm{nat}})_{n;2,3}=0.
\tag{6.4}
\]
They are not in the leading kernel: in particular the \(12\) sum is strictly positive for every integer \(t\). Keeping each face multiplicity gives

\[
\sum_p|(\mathsf Iw^{\mathrm{nat}})_p|^2=4\mathcal A_L,
\]
\[
\begin{split}
\mathcal A_L
&=2L(2L+1)\sum_{t=-L}^{L-1}(t^2+t+\tfrac12)^2+
4L^2\sum_{t=-L}^{L}t^4\\
&=\frac{L^2(2L+1)}{15}(24L^4+24L^3+8L^2-4L+3).
\end{split}
\tag{6.5}
\]

The finite sum formulas are
\(\sum_{t=-L}^{L-1}(t^2+t+\tfrac12)^2=L(4L^4+1)/10\) and
\(\sum_{t=-L}^{L}t^4=L(L+1)(2L+1)(3L^2+3L-1)/15\).
They follow by expansion, or by checking \(L=1\) and the two added endpoint terms under \(L\mapsto L+1\). Substitution gives the polynomial in (6.5).

Equations (2.8), (3.12), and (6.5) therefore yield, for the actual native state,

\[
\|v_{w^{\mathrm{nat}},\xi}\|^2=\frac{\xi^2}{4}\mathcal A_L+O_L(\xi^4),
\qquad
\mathfrak q_\xi(v_{w^{\mathrm{nat}},\xi},v_{w^{\mathrm{nat}},\xi})
=\frac{3\kappa\xi^2}{4}\mathcal A_L+O_L(\kappa\xi^4),
\tag{6.6}
\]
and quotient \(3\kappa+O_L(\kappa\xi^2)\) on this fixed box. This agrees with the native projected magnetic-translation coefficient: its fixed-state small-angle leading vector is \(-\tfrac23\theta^2v_{w^{\mathrm{nat}},\xi}\), so the \(\xi^2\theta^4\) squared-norm coefficient is \((4/9)(\mathcal A_L/4)=\mathcal A_L/9\).

The exact comparison is therefore: native nonnegative \(n_2^2\) weights retain the one-face modes at order \(\xi\), whereas transverse alternating weights cancel those modes and reveal two-face modes at order \(\xi^2\). This is a proved state-space distinction and does not assert a favorable infinite-volume scaling of either actual quotient.

## 7. The minimum over all real electric weights, including coupling-dependent ones

The fixed-weight conclusions do not by themselves control weights approaching the leading kernel as \(\xi\to0\). We now close that possibility by inequalities valid simultaneously for every real edge weight on the fixed box, without changing any physical state, coefficient, or denominator.

Write the original real edge space as the orthogonal direct sum
\[
\mathbb R^{\mathsf E_L}=\mathscr R_L\oplus\mathscr Z_L,\qquad
\mathscr Z_L=\ker\mathsf I,\quad \mathscr R_L=(\ker\mathsf I)^\perp,
\qquad w=u+z.
\tag{7.1}
\]
Orthogonality here is the ordinary coordinate inner product on the finite list of physical edge weights. It is used to state estimates, not as a replacement for the actual covariance denominator \(w^TC(\xi)w\).

Because \(\mathsf I\) is injective on \(\mathscr R_L\), finite-dimensional compactness gives the strictly positive constant
\[
\lambda_L=\min_{\substack{u\in\mathscr R_L\\\|u\|=1}}\|\mathsf Iu\|^2>0.
\tag{7.2}
\]
Set \(r_0=\lambda_L/16\) and \(d_0=196/13689\). The proved matrix remainders in (2.8) and (5.7), together with evenness of the mixed block, give on some fixed-box interval \(0<\xi<\epsilon_L\)
\[
u^TCu\ge\tfrac12r_0\xi^2\|u\|^2,\qquad
z^TCz\ge\tfrac12d_0\xi^4\|z\|^2,\qquad
|u^TCz|\le B_L\xi^4\|u\|\|z\|,
\tag{7.3}
\]
where \(B_L<\infty\). The second inequality uses
\(\mathcal K_L(z)\ge\|z\|^2\) from \(r_e\ge2\). Every bound is between fixed finite matrix blocks and therefore holds for all their vectors with one common box-dependent constant.

The elementary inequality
\[
2B_L\xi^4\|u\|\|z\|
\le\tfrac14r_0\xi^2\|u\|^2+
\frac{4B_L^2}{r_0}\xi^6\|z\|^2
\tag{7.4}
\]
follows by expanding the square of
\(\sqrt{r_0}\xi\|u\|/2-(2B_L/\sqrt{r_0})\xi^3\|z\|\).
Shrink the already nonempty interval so
\((4B_L^2/r_0)\xi^2\le d_0/4\); if \(B_L=0\) this step is unnecessary. Adding the three blocks in (7.3) then proves the simultaneous physical denominator bound
\[
\boxed{w^TC(\xi)w\ge c_L\xi^2\|u\|^2+
\tfrac14d_0\xi^4\|z\|^2,\qquad c_L=r_0/4=\lambda_L/64>0.}
\tag{7.5}
\]
In particular the actual centered state is nonzero for every nonzero real \(w\) on this interval. No component has been scaled by a power of \(\xi\) in this argument.

Now define the actual matrix difference
\[
\mathcal B(\xi)=\kappa^{-1}\mathcal N(\xi)-3C(\xi).
\tag{7.6}
\]
Its \(\mathscr R_L\)-block and mixed block are \(O_L(\xi^4)\) by (2.8). Its restriction to \(\mathscr Z_L\) has the strictly positive leading form
\[
z^T\mathcal Bz=\delta_0\xi^4\mathcal K_L(z)+O_L(\xi^6)\|z\|^2,
\qquad
\delta_0=\frac8{117}-3\frac{196}{13689}
=\frac{348}{13689}=\frac{116}{4563}>0.
\tag{7.7}
\]
Hence, on a possibly smaller nonempty interval, there are finite \(A_L,B'_L\) such that simultaneously
\[
u^T\mathcal Bu\ge-A_L\xi^4\|u\|^2,\quad
|u^T\mathcal Bz|\le B'_L\xi^4\|u\|\|z\|,\quad
z^T\mathcal Bz\ge\tfrac12\delta_0\xi^4\|z\|^2.
\tag{7.8}
\]
Complete the square in the last two terms, or use
\[
\tfrac12\delta_0\|z\|^2-2B'_L\|u\|\|z\|
\ge-\frac{2(B'_L)^2}{\delta_0}\|u\|^2.
\]
It follows that
\[
w^T\mathcal Bw\ge-K_L\xi^4\|u\|^2,\qquad
K_L=A_L+\frac{2(B'_L)^2}{\delta_0}.
\tag{7.9}
\]
The retained physical denominator (7.5) now gives the uniform-in-weight lower estimate
\[
\boxed{
\frac{w^T\mathcal N(\xi)w}{w^TC(\xi)w}
=3\kappa+\kappa\frac{w^T\mathcal B(\xi)w}{w^TC(\xi)w}
\ge3\kappa-\frac{K_L}{c_L}\kappa\xi^2
\quad\text{for every real }w\ne0.}
\tag{7.10}
\]
This includes arbitrary \(\xi\)-dependent weights, including ones whose component ratio \(\|u\|/\|z\|\) tends to zero or infinity.

For the matching upper estimate on the minimum, choose one fixed face \(p_0\) in the box and its original edge-indicator weight
\[
(u_0)_e=\mathbf1_{\{e\in\partial p_0\}}.
\tag{7.11}
\]
For every \(z\in\mathscr Z_L\), \(\langle u_0,z\rangle=(\mathsf Iz)_{p_0}=0\), so \(u_0\in\mathscr R_L\). Its actual four entries equal 1 and \(\|u_0\|^2=4\). The absolute \(\mathscr R_L\)-block bound on \(\mathcal B\), together with (7.5), gives
\[
\left|\frac{u_0^T\mathcal N u_0}{u_0^TCu_0}-3\kappa\right|
\le\frac{A_L}{c_L}\kappa\xi^2,
\tag{7.12}
\]
enlarging \(A_L\) to bound that entire block in absolute value if necessary. Both numerator and denominator in (7.12) are the original state forms; no rescaled state norm has replaced either.

Since \(C(\xi)\) is positive definite, this continuous homogeneous quotient attains its minimum on the nonzero real weight rays: equivalently one applies finite-dimensional compactness on a coordinate unit sphere while keeping the denominator \(w^TCw\) unchanged. Combining (7.10) and (7.12) proves
\[
\boxed{
\min_{w\in\mathbb R^{\mathsf E_L}\setminus\{0\}}
\frac{\mathfrak q_\xi(v_{w,\xi},v_{w,\xi})}{\|v_{w,\xi}\|^2}
=3\kappa+O_L(\kappa\xi^2),\qquad \xi\downarrow0.}
\tag{7.13}
\]
This is uniform over all weights on the fixed box, not uniform in \(L\). It uses the actual positive fourth-order form on the leading kernel; deleting that form would leave the degenerating denominator uncontrolled.

## 8. Verification and limits of the result

The companion check_electric_covariance_incidence_20260908.py enumerates all links and all elementary faces for \(L=2,3,4\). It verifies edge and face counts, the incident-face numbers \(r_e\), uniqueness of the six-edge support for every unordered adjacent pair, the full anchored kernel construction and reconstruction, and every individual parameter basis vector for the entire \(L=2\) box. These boxes have respectively kernel dimensions 60, 126, 216 and adjacent-pair counts 1128, 3852, 9168. It verifies both the alternating family and the native \(n_2^2\) coefficient, along with exact rational arithmetic for the two-face vacuum coefficients, the norm coefficient \(196/13689\), the energy coefficient \(8/117\), and quotient \(234/49\).

The rank and kernel theorem itself is proved for every \(L\) in Section 3; it is not inferred from those finite checks. Likewise the checks do not replace the actual-vacuum analytic and domain arguments in Sections 1, 2, 4, and 5. No floating-point vacuum approximation, numerical Haar sampling, continuum replacement, remote action, PDF generation, new agent, or heavy job is used.

The parent finite-range matrix construction is in magnetic_translation_true_vacuum.md, Section 8; the standalone full-vertex projection and native angular coefficient are in MAGNETIC_TRANSLATION_PLAQUETTE.md; the adjacent-mode normalization is consistent with BULK_PLAQUETTE_EXTENSION.md. All constants and the specific proofs needed for the present calculation are given above. Every conclusion concerns a fixed finite, full interacting box with a controlled local expansion in \(b/\kappa\). The guaranteed disk \(3/(16M)\) and all stated remainder constants are retained; no uniform-volume, fixed-coupling joint-limit, or four-dimensional continuum gap conclusion is claimed.

For historical convention context, see J. Kogut and L. Susskind, “Hamiltonian formulation of Wilson's lattice gauge theories,” *Physical Review D* **11**, 395–408 (1975), [doi:10.1103/PhysRevD.11.395](https://doi.org/10.1103/PhysRevD.11.395). This is a convention reference, not a substitution of its coupling normalization for (1.3)--(1.4). The full incidence kernel, its mode coefficients, and the all-weight estimates used here are proved in this source.
