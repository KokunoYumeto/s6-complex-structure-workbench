# The adjacent-plaquette quantum correction in a full finite three-dimensional Wilson box

8 September 2026. All links and all elementary spatial plaquettes of the box are retained in the Hamiltonian. The only integration used to define the conditional projection eliminates one specified link from the **actual ground-state density**. This calculation neither replaces that density by a one-time Wilson density nor takes a spatial continuum or infinite-volume limit.

## 1. Exact statement, lattice, metric, and coupling dictionary

Let \(L\geq2\) be an integer. The vertices are

\[
\mathsf V_L=\{-L,-L+1,\ldots,L\}^3.
\]

There is one positively directed physical link \((n,i)\), from \(n\) to \(n+\mathbf e_i\), whenever both endpoints belong to \(\mathsf V_L\). Its variable is \(U_i(n)\in SU(2)\). A negatively traversed link contributes \(U_i(n)^{-1}\), not an independent variable. The set \(\mathsf E_L\) contains every such link. The set \(\mathsf P_L\) contains every elementary square \((n;i,j)\), \(1\leq i<j\leq3\), whose four vertices belong to \(\mathsf V_L\), with holonomy

\[
U_{n;i,j}=U_i(n)U_j(n+\mathbf e_i)
 U_i(n+\mathbf e_j)^{-1}U_j(n)^{-1},
\qquad W_{n;i,j}=\operatorname{tr}U_{n;i,j}.
\tag{1.1}
\]

Every \(W_p\) is real. There are

\[
N=|\mathsf E_L|=3(2L)(2L+1)^2,
\qquad M=|\mathsf P_L|=3(2L)^2(2L+1).
\tag{1.2}
\]

Indeed, a link direction has \(2L\) initial coordinates in that direction and \(2L+1\) choices in either transverse direction. A face plane has \(2L\) choices in each of its two directions and \(2L+1\) in the third. The three choices of direction, or plane, give (1.2). Boundary conditions are open; there are no periodic identifications.

Use \(T_a=-i\sigma_a/2\), \(a=1,2,3\), where \(\sigma_a\) are the Pauli matrices. Thus

\[
-2\operatorname{tr}(T_aT_b)=\delta_{ab},\quad
X_{e,a}f=\left.\frac{d}{dt}f(\ldots,e^{tT_a}U_e,\ldots)\right|_{t=0},
\quad \Delta_e^T=\sum_aX_{e,a}^2.
\tag{1.3}
\]

The companion two-plaquette calculation uses the opposite basis
\(T_a^{\mathrm{pair}}=+i\sigma_a/2\). The exact dictionary is
\(T_a=-T_a^{\mathrm{pair}}\), hence
\(X_{e,a}=-X_{e,a}^{\mathrm{pair}}\). It leaves
\(\sum_aX_{e,a}^2\) unchanged. Both factors in each derivative
contraction change sign: in particular
\(G=\sum_a(X_{e,a}W_P)(X_{e,a}W_Q)\) is unchanged, and the score
\(\sigma_{e,a}\) defined in (4.5) changes sign together with
\(X_{e,a}f\). Thus the operator B in (4.5), its norm, and the
Rayleigh coefficients below agree exactly with that convention.

The Hilbert space is \(\mathcal H=L^2(SU(2)^{\mathsf E_L},dU)\), where \(dU\) is product Haar probability measure. For \(\kappa,b>0\), the full nonlinear Wilson Hamiltonian is

\[
H_{\kappa,b}=-\kappa\sum_{e\in\mathsf E_L}\Delta_e^T
 +b\sum_{p\in\mathsf P_L}(2-W_p).
\tag{1.4}
\]

No term in either sum is dropped. Put \(\xi=b/\kappa\), \(H_0=-\sum_e\Delta_e^T\), and \(\mathcal V=\sum_{p\in\mathsf P_L}W_p\). Then the exact, including constant, identity is

\[
\boxed{H_{\kappa,b}=\kappa(H_0-\xi\mathcal V)+2bM\,I.}
\tag{1.5}
\]

The original metric is \(c(X,Y)=-\tfrac12\operatorname{tr}(XY)\), which is one quarter of the metric in (1.3). Its orthonormal basis is \(2T_a\), so \(X_{e,a}^c=2X_{e,a}\) and \(\Delta_e^c=4\Delta_e^T\). The original physical parameters are retained without substitution:

\[
\kappa=\frac{2g_{\mathrm{YM}}^2}{a},\qquad
b=\frac{1}{2g_{\mathrm{YM}}^2a},\qquad
\xi=\frac{1}{4g_{\mathrm{YM}}^4}.
\tag{1.6}
\]

Consequently the kinetic term in (1.4) is also

\[
-\frac{g_{\mathrm{YM}}^2}{2a}\sum_e\Delta_e^c.
\]

Let \(\psi_\xi>0\) be the normalized ground state of (1.4), \(\rho_\xi=\psi_\xi^2\), and \(E_\xi\) its ground energy. Define the particular faces and links

\[
Q=((0,0,0);1,2),\quad P=((-1,0,0);1,2),
\quad e=((0,0,0),2),\quad s=((-1,0,0),2).
\tag{1.7}
\]

Eliminate \(S=\{s\}\); retain \(R=\mathsf E_L\setminus\{s\}\). Write the retained centered observable as

\[
f_\xi=W_Q-\int W_Q\rho_\xi\,dU.
\tag{1.8}
\]

The conditional projection, the operator \(B_\xi\), the eliminated form operator \(C_\xi\), and the corrected physical vector \(u_\xi\) are defined in Sections 4 and 7 below, with their domains. The conclusions are

\[
\boxed{\|B_\xi f_\xi\|_{L^2(\rho_\xi dU)}^2
=\frac{b^2}{12}+O_L\!\left(\frac{b^3}{\kappa}\right),}
\tag{1.9}
\]

and

\[
\boxed{\mathcal R_{\mathrm{ret}}(\xi)-\mathcal R_{\mathrm{corr}}(\xi)
=\frac{1951}{81675}\frac{b^2}{\kappa}
 +O_L\!\left(\frac{b^3}{\kappa^2}\right).}
\tag{1.10}
\]

Here both quotients are exact quadratic-form Rayleigh quotients for \(H_{\kappa,b}-E_\xi\), the latter on a corrected full-system, gauge-invariant, vacuum-orthogonal vector. For each fixed \(L\), the remainders mean bounds by constants depending on that box for sufficiently small positive \(\xi\). The statements follow from convergent analytic perturbation locally at zero, not a formal substitution for the vacuum. In particular \(B_\xi f_\xi\ne0\) and the improvement is strict on an actual nonempty interval \(0<\xi<\epsilon_L\). No lower bound on \(\epsilon_L\) uniform in \(L\) is asserted.

The explicit resolvent Neumann disk supplied by the all-plaquette potential is

\[
\boxed{|\xi|<\frac{3}{16M}.}
\tag{1.11}
\]

It controls the isolated ground spectral projection as proved below. It is not an assertion that every local remainder estimate or strict-positivity test has the entire disk as its optimal radius.

## 2. Literal full-box incidence and orientations

A face containing the direction-2 link \(s=((-1,0,0),2)\) must lie in plane \(12\) or \(23\). In plane \(12\), it must extend from that link either in the positive or the negative direction 1. In plane \(23\), it must extend either in the positive or the negative direction 3. Thus its complete incidence star is

\[
\begin{split}
\mathsf I(s)=\{&((-1,0,0);1,2),\;((-2,0,0);1,2),\\
              &((-1,0,0);2,3),\;((-1,0,-1);2,3)\}.
\end{split}
\tag{2.1}
\]

All four faces exist when \(L\geq2\). This enumeration exhausts the possibilities because an elementary square has two coordinate directions, one of which must be the direction of its specified boundary link, and its unit transverse extent has only the two stated choices.

The last three faces in (2.1) have first coordinate at most \(-1\) at every vertex. Every vertex of \(Q\) has first coordinate 0 or 1. Hence each of those three faces has no vertex, and therefore no physical edge, in common with \(Q\). The remaining face is \(P\), and direct inspection of (1.1) gives

\[
\partial P\cap\partial Q=\{e\},\qquad
\{(p,i):p\in\mathsf I(s),\ i\in\partial p\cap\partial Q\}
=\{(P,e)\}.
\tag{2.2}
\]

The intersection here is of unoriented physical edges. The occurrence of \(e\) in \(P\) is positive, while its occurrence in \(Q\) is negative. The occurrence of \(s\) in \(P\) is negative. This proves the asserted incidence with no implicit exclusion of any other box plaquette.

For the based calculations, let

\[
\begin{split}
A&=U_1(-1,1,0)^{-1}U_2(-1,0,0)^{-1}U_1(-1,0,0),\\
B&=U_1(0,0,0)U_2(1,0,0)U_1(0,1,0)^{-1}.
\end{split}
\tag{2.3}
\]

Coordinates displayed as arguments are triples. Cyclically rotating the corresponding plaquette words in (1.1) gives the exactly equal Wilson traces of the based matrices

\[
P_*=U_eA,\qquad Q_*=U_e^{-1}B,\qquad Q'_*=BU_e^{-1}.
\tag{2.4}
\]

The products \(A,B\) use six distinct outer physical links and neither uses \(e\). The link \(s\) appears once, inversely, in \(A\), and does not appear in \(B\). The union of the two plaquette boundaries has exactly seven physical links. Every other link of the full box is still present in (1.4).

## 3. The actual all-plaquette vacuum and its controlled expansion

### 3.1 Free spectrum, bounded interaction, and the exact radius

On a single \(SU(2)\) factor with (1.3), the spin-\(j\) matrix coefficients have \(-\Delta^T\) eigenvalue \(j(j+1)\), for \(j=0,\tfrac12,1,\ldots\). To fix its normalization directly, \(T_a=-i\sigma_a/2\) gives \(-\sum_aT_a^2=\tfrac34I\) on the fundamental representation. On the spin-\(j\) representation the corresponding angular momenta satisfy \(J_3v_m=mv_m\) and \(J_\pm v_m=\sqrt{(j\mp m)(j\pm m+1)}v_{m\pm1}\); therefore \(J_3^2+(J_+J_-+J_-J_+)/2=j(j+1)I\). The matrix coefficients form the complete Peter--Weyl orthogonal decomposition. Taking their tensor products gives the complete product spectrum as sums of these eigenvalues. The free eigenvalue 0 is simple, represented by the constant 1, and the first nonzero eigenvalue on the full, not gauge-reduced, Hilbert space is \(3/4\).

Since \(W_p\in[-2,2]\), one has \(\|\mathcal V\|_\infty\leq2M\). At the all-identity configuration \(\mathcal V=2M\). Continuity and positive Haar measure of every neighborhood of that configuration give the reverse essential-supremum inequality. Thus

\[
\|\mathcal V\|_{\mathcal H\to\mathcal H}=2M.
\tag{3.1}
\]

For \(z\) on \(|z|=3/8\), the distance from \(z\) to the free spectrum is at least \(3/8\), so

\[
\|(z-H_0)^{-1}\|\leq\frac83.
\]

Factoring \(z-H_0+\xi\mathcal V\) gives a norm-convergent resolvent Neumann series whenever

\[
q:=\frac{16M}{3}|\xi|<1.
\tag{3.2}
\]

The contour projection

\[
\Pi_\xi=\frac{1}{2\pi i}\oint_{|z|=3/8}
 (z-H_0+\xi\mathcal V)^{-1}\,dz
\tag{3.3}
\]

is analytic throughout (1.11). Its rank is locally constant because it is a norm-continuous family of projections; the disk is connected, and its rank at zero is one. It therefore has rank one throughout that disk. This establishes (1.11) with the full \(2M\) potential norm and with no two-face replacement.

For real \(\xi\) in that interval, the bottom eigenvalue \(e(\xi)\) of \(H_0-\xi\mathcal V\) lies between \(-2M|\xi|\) and 0. The upper bound uses the constant trial vector and \(\int\mathcal V\,dU=0\). By the min--max principle the second eigenvalue is at least \(3/4-2M|\xi|>3/8\), whereas \(-3/8<e(\xi)\leq0\). Consequently (3.3) is the actual ground projection for every such real \(\xi\). The energy of (1.4) is exactly

\[
E_\xi=\kappa e(\xi)+2bM.
\tag{3.4}
\]

Existence of a smooth ground eigenfunction follows from compact resolvent and elliptic regularity of the compact product Laplacian with smooth bounded potential. It can be taken nonnegative: the local identity \(|\nabla|u||\leq|\nabla u|\), obtained first away from \(u=0\) and then by approximating \(|u|\) by \(\sqrt{|u|^2+\varepsilon^2}\), shows that replacing a minimizer by its modulus does not increase its form energy. The strong maximum principle for the resulting elliptic eigen-equation on this connected manifold makes that nonnegative eigenfunction strictly positive. Simplicity can also be checked directly: for a positive ground state \(\psi\), integration by parts and its eigen-equation give

\[
\langle\psi F,(H-E)\psi F\rangle
=\kappa\sum_{i,a}\int |X_{i,a}F|^2\psi^2\,dU
\tag{3.5}
\]

for smooth \(F\). Polarization and density extend this to the form domain. A second ground eigenfunction divided by \(\psi\) would make every derivative on the right vanish and hence would be constant. This also proves uniqueness of the positive normalized state used here.

### 3.2 Haar orthogonality and the first derivative

For each face \(p\), Haar integration over any one of its four distinct edges annihilates \(W_p\). Indeed, \(\int_{SU(2)}U\,dU=0\): multiplying the integration variable by the central element \(-I\) changes this integral to its negative. The same statement holds for \(U^{-1}\), and it remains true after multiplication by matrices independent of that edge. Thus \(\int W_p=0\).

For distinct elementary faces in an open box, their sets of four boundary edges differ. Choose an edge in one set absent from the other and integrate it first. This proves \(\int W_pW_q=0\) when \(p\ne q\). To justify the asserted difference of boundary sets without a geometric assumption, two adjacent perpendicular coordinate directions and the minima of the vertex coordinates are recovered from the four-edge set of an elementary square; this recovers its plane and lower corner uniquely. Finally \(\int W_p^2=1\): integrate three edges first or fix them and use Haar invariance on the fourth to reduce to \(\int_{SU(2)}(\operatorname{tr}U)^2dU\). With \(U=u_0I+i\sum_{a=1}^3u_a\sigma_a\), Haar measure is uniform on the unit sphere in \(\mathbb R^4\), so \(\int u_0^2=1/4\), and this integral is 1. We have proved

\[
\int W_pW_q\,dU=\delta_{pq},\qquad
\|\mathcal V\|_2^2=M,\qquad H_0W_p=3W_p.
\tag{3.6}
\]

The last identity uses four fundamental edge Casimirs \(3/4\), with all other edges acting trivially.

Choose the analytic ground representative \(\phi_\xi\) near zero by \(\int\phi_\xi dU=1\) and \(\phi_0=1\). This is a legitimate local analytic normalization: the resolvent bound gives

\[
\|\Pi_\xi-\Pi_0\|\leq\frac{q}{1-q},
\tag{3.7}
\]

by integrating the Neumann-series difference over a circle of length \(2\pi(3/8)\). For \(q<1/2\), \(\langle1,\Pi_\xi1\rangle\ne0\), and \(\phi_\xi=\Pi_\xi1/\langle1,\Pi_\xi1\rangle\) supplies the normalization. The spectral-projection disk (1.11) itself did not require this auxiliary choice of vector normalization on the full complex disk.

Differentiating \((H_0-\xi\mathcal V)\phi_\xi=e(\xi)\phi_\xi\) at zero and taking its Haar mean yields \(e'(0)=-\int\mathcal V=0\). The remaining equation and the normalization give

\[
H_0\phi'_0=\mathcal V,\qquad \int\phi'_0=0,
\qquad \phi'_0=\frac13\mathcal V.
\tag{3.8}
\]

These are expansions of the actual eigenvector. Their remainders hold in every fixed \(C^k\) norm, not only in \(L^2\). Here is the regularity argument. Define Sobolev norms on the compact product group by the elliptic operator \(H_0+1\). Multiplication by the fixed smooth function \(\mathcal V\) is bounded in each integer Sobolev norm, and \((H_0+1)^{-1}:H^m\to H^{m+2}\) is bounded. The equation

\[
\phi_\xi=(H_0+1)^{-1}\big[(e(\xi)+1+\xi\mathcal V)\phi_\xi\big]
\]

therefore upgrades analyticity successively from \(L^2\) to \(H^2,H^4,\ldots\). Sobolev embedding in the fixed dimension \(3N\) then gives analytic \(C^k\) representatives and bounded Taylor remainders on a sufficiently small disk. All constants may depend on \(L,k\). On the real interval, the chosen ground vector is positive by the preceding ground-state argument.

Set \(Z_\xi=\int\phi_\xi^2dU\) and \(\psi_\xi=\phi_\xi/\sqrt{Z_\xi}\), taking the square root that is positive for real \(\xi\) near zero. Because every higher Taylor coefficient of \(\phi_\xi\) has zero Haar mean, (3.6)--(3.8) give

\[
\begin{split}
\phi_\xi&=1+\frac\xi3\sum_{p\in\mathsf P_L}W_p+O_{L,k}(\xi^2),\\
Z_\xi&=1+\frac M9\xi^2+O_L(\xi^3),\\
\psi_\xi&=1+\frac\xi3\sum_{p\in\mathsf P_L}W_p+O_{L,k}(\xi^2),\\
\log\rho_\xi&=\frac{2\xi}{3}\sum_{p\in\mathsf P_L}W_p+O_{L,k}(\xi^2).
\end{split}
\tag{3.9}
\]

The \(M/9\) normalization coefficient explicitly records all the box plaquettes. Logarithms are taken of the actual positive density, which is uniformly close to 1 for sufficiently small real \(\xi\) in any fixed box.

## 4. Exact conditional projection and the surviving quantum coupling

Write \(U=(u,r)\), with \(u=U_s\), and define

\[
\rho_{R,\xi}(r)=\int_{SU(2)}\rho_\xi(u,r)\,du,
\quad p_\xi(u\mid r)=\frac{\rho_\xi(u,r)}{\rho_{R,\xi}(r)}.
\tag{4.1}
\]

Let \(Jf(u,r)=f(r)\), and let

\[
(J_\xi^*v)(r)=\int v(u,r)p_\xi(u\mid r)\,du.
\tag{4.2}
\]

Direct integration shows that \(J\) is an isometry from \(L^2(\rho_{R,\xi}dr)\) into \(L^2(\rho_\xi dU)\), and (4.2) is its adjoint. Define \(P_\xi=JJ_\xi^*\) and \(Q_\xi=I-P_\xi\). Then \(P_\xi\) is the orthogonal projection onto functions independent of \(u\), and \(\mathcal K_\xi=\operatorname{ran}Q_\xi=\ker J_\xi^*\).

Conjugating by the true vacuum gives the nonnegative operator

\[
\mathscr L_\xi=\psi_\xi^{-1}(H_{\kappa,b}-E_\xi)\psi_\xi
=-\kappa\sum_{i\in\mathsf E_L,a}
 \big[X_{i,a}^2+(X_{i,a}\log\rho_\xi)X_{i,a}\big],
\tag{4.3}
\]

with closed form

\[
q_\xi(v,w)=\kappa\sum_{i,a}\int
 \overline{X_{i,a}v}\,X_{i,a}w\,\rho_\xi dU,
\quad D(q_\xi)=H^1(SU(2)^{\mathsf E_L}).
\tag{4.4}
\]

The form domain equality follows because \(\rho_\xi\) is smooth, strictly positive, and bounded above and below on the finite compact configuration manifold. Formula (4.3) is obtained by the Leibniz rule, cancellation of the ground-state eigen-equation, and \(2X\log\psi=X\log\rho\); it retains the exact kinetic coefficient \(\kappa\).

For a retained smooth \(f\), the \(s\) derivatives vanish. Differentiating (4.1) under its finite compact integral gives

\[
X_{i,a}\log\rho_{R,\xi}
=\int (X_{i,a}\log\rho_\xi)p_\xi\,du
\quad(i\in R).
\]

It follows from (4.3) that the exact eliminated coupling is

\[
\begin{split}
B_\xi f&:=Q_\xi\mathscr L_\xi Jf
 =-\kappa\sum_{i\in R,a}\sigma_{i,a,\xi}X_{i,a}f,\\
\sigma_{i,a,\xi}&=X_{i,a}\log\rho_\xi-X_{i,a}\log\rho_{R,\xi},
\qquad J_\xi^*\sigma_{i,a,\xi}=0.
\end{split}
\tag{4.5}
\]

In particular second derivatives of \(f\) cancel exactly; no second-order term has been discarded in (4.5).

If \(p\in\mathsf I(s)\), integration over \(u\) kills \(W_p\), and also kills each \(X_{i,a}W_p\), \(i\in R\), since that derivative commutes with integration over \(u\). If \(p\notin\mathsf I(s)\), \(W_p\) is independent of \(u\). Consequently (3.9) gives, with \(C^k\) remainders,

\[
\begin{split}
\log\rho_{R,\xi}
 &=\frac{2\xi}{3}\sum_{p\notin\mathsf I(s)}W_p+O_{L,k}(\xi^2),\\
\sigma_{i,a,\xi}
 &=\frac{2\xi}{3}\sum_{p\in\mathsf I(s)}X_{i,a}W_p
   +O_{L,k}(\xi^2).
\end{split}
\tag{4.6}
\]

Since \(Xf_\xi=XW_Q\), its only nonzero derivatives belong to edges of \(Q\). Combining (2.2), (4.5), and (4.6) therefore leaves exactly one face-edge pair:

\[
B_\xi f_\xi=-\frac{2b}{3}G+O_{L,k}\!\left(\frac{b^2}{\kappa}\right),
\qquad G=\sum_{a=1}^3(X_{e,a}W_P)(X_{e,a}W_Q).
\tag{4.7}
\]

Every other face in the Hamiltonian contributed to (3.9) and (4.6); it disappears from the displayed first derivative only by the proved conditional cancellation or the proved edge-disjointness. Higher orders still contain the full interacting box.

## 5. Exact Fierz contraction, Haar norms, and free electric modes

Under \(U_e\mapsto e^{tT_a}U_e\), (2.4) yields

\[
X_{e,a}W_P=\operatorname{tr}(T_aP_*),\qquad
X_{e,a}W_Q=-\operatorname{tr}(T_aQ'_*).
\tag{5.1}
\]

The Pauli completeness identity

\[
\sum_a(\sigma_a)_{ij}(\sigma_a)_{kl}
=2\delta_{il}\delta_{jk}-\delta_{ij}\delta_{kl}
\]

gives, by multiplying by matrix entries and summing indices,

\[
\sum_a\operatorname{tr}(T_aC)\operatorname{tr}(T_aD)
=-\frac12\operatorname{tr}(CD)+\frac14\operatorname{tr}C\operatorname{tr}D.
\tag{5.2}
\]

Define functions on the **full** configuration space by

\[
R_0=\operatorname{tr}(AB),\qquad D_0=W_PW_Q,
\qquad D_1=D_0-\frac12R_0.
\tag{5.3}
\]

Since \(\operatorname{tr}(P_*Q'_*)=\operatorname{tr}(U_eABU_e^{-1})=R_0\), equations (5.1)--(5.2) give

\[
G=\frac12R_0-\frac14D_0
=\frac38R_0-\frac14D_1.
\tag{5.4}
\]

These functions are gauge invariant: \(W_P,W_Q\) are traces of closed holonomies, and \(AB\) is the closed six-edge outer loop after cancellation of the common edge. They have zero Haar conditional mean over \(s\). In fact \(R_0\) contains \(U_s^{-1}\) once, \(D_0\) contains it once in \(W_P\), and \(W_Q\) is independent of it; the Haar annihilation used in Section 3 proves each assertion.

For their norms, condition on \(U_e\). The disjoint outer-link products \(A,B\) are independent Haar-distributed matrices: for any fixed values of the other factors, a product containing a single Haar factor or its inverse is Haar by left/right invariance. Thus \(P_*=U_eA\) and \(Q'_*=BU_e^{-1}\) are independent Haar matrices even conditionally on \(U_e\). Write

\[
P_*=p_0I+i\sum_ap_a\sigma_a,\qquad
Q'_*=q_0I+i\sum_aq_a\sigma_a.
\]

The vectors \(p,q\) are independent uniform unit vectors in \(\mathbb R^4\). Their second moments are \(\mathbb E[p_\alpha p_\beta]=\delta_{\alpha\beta}/4\), and likewise for \(q\): off-diagonal moments vanish by sign symmetries, diagonal moments agree by rotational symmetry, and their sum is 1. Matrix multiplication and (5.1) now give

\[
G=-\sum_{a=1}^3p_aq_a,\quad
R_0=2\left(p_0q_0-\sum_{a=1}^3p_aq_a\right),\quad
D_1=3p_0q_0+\sum_{a=1}^3p_aq_a.
\tag{5.5}
\]

Set \(x=p_0q_0\), \(y=\sum_{a=1}^3p_aq_a\). The moments just proved give \(\mathbb E x^2=1/16\), \(\mathbb E y^2=3/16\), and \(\mathbb E xy=0\). Hence

\[
\|R_0\|_0^2=1,\quad \|D_1\|_0^2=\frac34,
\quad\langle R_0,D_1\rangle_0=0,
\quad\|G\|_0^2=\frac3{16}.
\tag{5.6}
\]

The subscript 0 denotes Haar inner product on the entire box. All additional link integrals are integrals of 1, so (5.6) contains no omitted factor depending on the number of additional links.

On any of the six outer links, \(R_0,D_0,D_1\) are linear combinations of fundamental matrix entries or inverse fundamental matrix entries. Each consequently has eigenvalue \(-3/4\) for that link Laplacian. On \(e\), \(R_0\) is independent of \(U_e\). The product rule, (5.4), and the fundamental plaquette Casimirs give

\[
\begin{split}
\Delta_e^T D_0
&=-\frac32D_0+2G
=R_0-2D_0=-2D_1,\\
\Delta_e^T R_0&=0,\qquad \Delta_e^T D_1=-2D_1.
\end{split}
\tag{5.7}
\]

On every link outside these seven, both \(R_0\) and \(D_1\) are constant. Such a link is in spin zero, with Casimir zero. Summing over **all** \(N\) links therefore gives the exact full-box identities

\[
H_0R_0=\frac92R_0,\qquad H_0D_1=\frac{13}{2}D_1.
\tag{5.8}
\]

Combining (4.7) and (5.4) yields

\[
B_\xi f_\xi=b\left(-\frac14R_0+\frac16D_1\right)
 +O_{L,k}(\kappa\xi^2).
\tag{5.9}
\]

As \(\rho_\xi=1+O_L(\xi)\), (5.6) proves

\[
\begin{split}
\|B_\xi f_\xi\|_\xi^2
&=b^2\left(\frac1{16}+\frac1{36}\frac34\right)
 +O_L(\kappa^2\xi^3)\\
&=\frac{b^2}{12}+O_L\!\left(\frac{b^3}{\kappa}\right).
\end{split}
\tag{5.10}
\]

In particular the positive leading coefficient is independent of the fixed box size, although the remainder is not.

## 6. The exact retained form and its first vacuum moments

For the centered \(f_\xi\), put

\[
m_\xi=\int W_Q\rho_\xi dU,\quad
r_\xi=\int W_Q^2\rho_\xi dU,\quad
d_\xi=\|Jf_\xi\|_\xi^2=r_\xi-m_\xi^2,
\]

and

\[
a_\xi=q_\xi(Jf_\xi,Jf_\xi)
=\kappa\sum_{i\in\partial Q,a}\int
 |X_{i,a}W_Q|^2\rho_\xi dU.
\tag{6.1}
\]

For any used edge of a simple \(SU(2)\) loop, its derivative is, up to an orientation sign, \(\operatorname{tr}(T_aC)\), with \(C\) a based version of its holonomy. Writing \(C=c_0I+i\sum_ac_a\sigma_a\) gives \(\operatorname{tr}(T_aC)=c_a\), so

\[
\sum_a|X_{i,a}W_Q|^2=\sum_ac_a^2
=1-\frac14W_Q^2.
\]

The four edges of \(Q\) give the exact identities

\[
a_\xi=\kappa(4-r_\xi),\qquad
\mathcal R_{\mathrm{ret}}(\xi)=\frac{a_\xi}{d_\xi}
=\kappa\frac{4-r_\xi}{r_\xi-m_\xi^2}.
\tag{6.2}
\]

The true vacuum is present in both moments. Equations (3.6) and (3.9) give \(m_\xi=2\xi/3+O_L(\xi^2)\). They also give \(r_\xi=1+O_L(\xi^2)\). For the latter claim, the linear term is \(\tfrac23\sum_p\int W_Q^2W_p\). If \(p\ne Q\), an edge of \(p\) outside \(Q\) annihilates the integral; if \(p=Q\), multiplying any one \(Q\)-edge by \(-I\) changes \(W_Q^3\) to its negative. Thus every summand is zero. Consequently

\[
d_\xi=1+O_L(\xi^2),\qquad
a_\xi=3\kappa+O_L(\kappa\xi^2),\qquad
\mathcal R_{\mathrm{ret}}(\xi)=3\kappa+O_L(\kappa\xi^2).
\tag{6.3}
\]

Strict positivity of \(d_\xi\) follows directly as well: the density has full support and the continuous nonconstant function \(W_Q\) cannot have zero variance.

## 7. Eliminated form domain and a genuine improved quantum vector

The definition of the eliminated operator does not assume that a formal product \(Q_\xi\mathscr L_\xi Q_\xi\) has any particular operator domain. First note that \(P_\xi,Q_\xi\) preserve \(H^1\). For \(i\in R\), differentiating (4.2) yields

\[
X_{i,a}J_\xi^*v
=J_\xi^*(X_{i,a}v)+J_\xi^*(\sigma_{i,a,\xi}v).
\tag{7.1}
\]

Conditional Cauchy--Schwarz bounds each right-hand term in \(L^2(\rho_{R,\xi})\) by the corresponding full \(L^2(\rho_\xi)\) norm, with the bounded score coefficient on the second term. The \(s\) derivative of \(P_\xi v\) is zero. This proves the \(H^1\) assertion. It also shows that \(P_\xi,Q_\xi\) preserve smooth functions. Smooth functions are dense in \(H^1\); applying \(Q_\xi\) to smooth approximants proves that

\[
\mathcal D_\xi=H^1\cap\mathcal K_\xi
\]

is dense in \(\mathcal K_\xi\), and is the form closure of its smooth elements. It is closed for the \(H^1\) norm because \(\mathcal K_\xi\) is closed in the weighted \(L^2\) norm. Thus \(q_\xi|_{\mathcal D_\xi}\) is a densely defined closed nonnegative form. Define \(C_\xi\) to be its self-adjoint operator by the explicit representation condition

\[
\begin{split}
D(C_\xi)=\{w\in\mathcal D_\xi: &\text{there is }h\in\mathcal K_\xi
\text{ with }q_\xi(v,w)=\langle v,h\rangle_\xi\text{ for all }v\in\mathcal D_\xi\},\\
C_\xi w&=h.
\end{split}
\tag{7.2}
\]

Put \(g_\xi=B_\xi f_\xi\in\mathcal K_\xi\), and define

\[
w_\xi=(C_\xi+\kappa)^{-1}g_\xi,
\qquad u_\xi=\psi_\xi(Jf_\xi-w_\xi).
\tag{7.3}
\]

Existence and uniqueness of \(w_\xi\) follow already by applying the coercive-form representation to \(q_\xi+\kappa\langle\cdot,\cdot\rangle_\xi\) on \(\mathcal D_\xi\). In particular \(w_\xi\in\mathcal D_\xi\). Since multiplication by the smooth positive \(\psi_\xi\) maps \(H^1\) to itself, \(u_\xi\) belongs to the full quadratic-form domain of \(H_{\kappa,b}\).

Moreover, \(\langle1,w_\xi\rangle_\xi=0\), since the constant belongs to the retained range. Centering (1.8) therefore proves \(\langle\psi_\xi,u_\xi\rangle=0\). The denominator \(d_\xi+\|w_\xi\|_\xi^2\) is positive, so the physical vector is nonzero.

All operators and this vector respect the Gauss constraint. In the convention \(U_e\mapsto g_{s(e)}U_eg_{t(e)}^{-1}\), Wilson traces, Haar measure, and the product kinetic energy are invariant. Uniqueness of the positive normalized vacuum makes \(\psi_\xi\) invariant. In (4.2), changing the eliminated variable by the corresponding left/right multiplications proves that conditional expectation intertwines the induced action on retained variables. Thus \(J,P_\xi,Q_\xi\), the closed forms, and their uniquely defined resolvents intertwine gauge transformations; \(f_\xi,g_\xi,w_\xi,u_\xi\) are invariant. The original convention \(U_e\mapsto h_{s(e)}^{-1}U_eh_{t(e)}\) is the same action with \(g_v=h_v^{-1}\) at every vertex. No gauge convention or coefficient is changed.

Set

\[
I_\xi=\langle g_\xi,w_\xi\rangle_\xi,
\qquad J_\xi^{\mathrm{num}}=\|w_\xi\|_\xi^2.
\tag{7.4}
\]

The superscript distinguishes this scalar from the lift \(J\). Testing the weak resolvent equation with \(w_\xi\) shows

\[
I_\xi=q_\xi(w_\xi,w_\xi)+\kappa J_\xi^{\mathrm{num}}\geq0.
\tag{7.5}
\]

For smooth \(Jf_\xi\), integration by parts against \(w_\xi\in H^1\), followed by (4.5) and \(P_\xi w_\xi=0\), gives \(q_\xi(Jf_\xi,w_\xi)=\langle g_\xi,w_\xi\rangle_\xi=I_\xi\). Orthogonality of the retained and eliminated ranges and (3.5) now give the **exact** corrected quotient

\[
\mathcal R_{\mathrm{corr}}(\xi)
:=\frac{\|(H_{\kappa,b}-E_\xi)^{1/2}u_\xi\|^2}{\|u_\xi\|^2}
=\frac{a_\xi-I_\xi-\kappa J_\xi^{\mathrm{num}}}{d_\xi+J_\xi^{\mathrm{num}}}.
\tag{7.6}
\]

Only form-domain membership is needed; an unproved operator-domain assertion about \(u_\xi\) is not used. Subtracting (7.6) from (6.2) gives

\[
\mathcal R_{\mathrm{ret}}-\mathcal R_{\mathrm{corr}}
=\frac{I_\xi+(\kappa+\mathcal R_{\mathrm{ret}})J_\xi^{\mathrm{num}}}
 {d_\xi+J_\xi^{\mathrm{num}}}.
\tag{7.7}
\]

If \(g_\xi\ne0\), then \(w_\xi\ne0\), and (7.5) gives \(I_\xi>0\). Since the retained form is nonnegative, (7.7) is then strictly positive. This is a correction of an actual excitation estimate in the full interacting Hilbert space, not the energy of a separately postulated marginal dynamics.

## 8. Resolvent expansion with the moving conditional kernel controlled

It remains to prove that the free modes (5.8) really determine the displayed second-order coefficient despite the changing density and the changing eliminated subspace. We work on a fixed Sobolev space and prove that step explicitly.

At \(\xi=0\), conditional expectation is ordinary Haar integration over \(s\), denoted \(P_0\). Integration commutes with every retained derivative and annihilates the integral of every \(s\) derivative by Haar invariance. Thus \(P_0\) commutes with \(H_0\) on smooth functions and, by the spectral or closed-form extension, on its natural domains. From (5.3) and Haar annihilation, \(R_0,D_1\in\mathcal K_0\). Equations (5.8) are therefore also the eigenvalue equations for \(C_0=\kappa H_0|_{\mathcal K_0}\).

Regard functions and projections for small real \(\xi\) on the same underlying unweighted \(L^2(dU)\) and \(H^1\) spaces. Equation (3.9) gives \(\rho_\xi=1+O_{L,1}(\xi)\), \(\rho_{R,\xi}=1+O_{L,1}(\xi)\), and \(p_\xi(u\mid r)=1+O_{L,1}(\xi)\). The integral formula (4.2) and Cauchy--Schwarz imply

\[
\|P_\xi-P_0\|_{L^2\to L^2}=O_L(|\xi|),\qquad
\|P_\xi-P_0\|_{H^1\to H^1}=O_L(|\xi|).
\tag{8.1}
\]

For the second bound, differentiate the kernel formula: its derivative is the integral of the differentiated input against \(p_\xi-1\), plus the input against a derivative of \(p_\xi\); both kernels have the stated \(O_L(|\xi|)\) supremum bound. Derivatives in the eliminated variable of the output are zero. This proves the bound in all first-derivative directions.

All \(P_\xi\) have exactly the same range, namely functions independent of \(s\), and act as the identity on that range. As operators on the common function space this gives

\[
P_\xi P_0=P_0,\quad P_0P_\xi=P_\xi,
\quad Q_0Q_\xi=Q_0,\quad Q_\xi Q_0=Q_\xi.
\tag{8.2}
\]

In particular

\[
T_\xi:=Q_\xi|_{\mathcal K_0}:\mathcal K_0\longrightarrow\mathcal K_\xi
\]

is a bounded bijection with inverse \(Q_0|_{\mathcal K_\xi}\). The same holds between the form spaces \(\mathcal D_0\) and \(\mathcal D_\xi\), and \(T_\xi-I=O_L(|\xi|)\) as a map from \(\mathcal D_0\) into \(H^1\), by (8.1).

On the fixed Hilbert form space \(\mathcal D_0=H^1\cap\mathcal K_0\), pull back the dimensionless resolvent form:

\[
\mathfrak a_\xi(v,h)
=\kappa^{-1}q_\xi(T_\xi v,T_\xi h)
 +\langle T_\xi v,T_\xi h\rangle_\xi.
\tag{8.3}
\]

Choose the explicit equivalent first-order Sobolev norm

\[
\|v\|_{H^1}^2=\|v\|_0^2+\sum_{i,a}\|X_{i,a}v\|_0^2.
\]

Then \(\mathfrak a_0(v,v)=\|v\|_{H^1}^2\). Density boundedness, (8.1), and Cauchy--Schwarz give

\[
|\mathfrak a_\xi(v,h)-\mathfrak a_0(v,h)|
\leq C_L|\xi|\|v\|_{H^1}\|h\|_{H^1}.
\tag{8.4}
\]

For sufficiently small \(|\xi|\), this also yields \(\mathfrak a_\xi(v,v)\geq\tfrac12\|v\|_{H^1}^2\). No estimate is required uniformly in \(L\).

Write

\[
g_1=-\frac14R_0+\frac16D_1,
\qquad g_\xi=\kappa\xi g_1+O_L(\kappa\xi^2)
\quad\hbox{in }L^2.
\tag{8.5}
\]

If \(h_\xi=T_\xi^{-1}w_\xi\), its exact weak equation is

\[
\mathfrak a_\xi(v,h_\xi)
=\kappa^{-1}\langle T_\xi v,g_\xi\rangle_\xi
=\xi\langle v,g_1\rangle_0
 +O_L(\xi^2)\|v\|_{H^1}.
\tag{8.6}
\]

The last remainder follows from (8.1), (8.5), and \(\rho_\xi-1=O_L(\xi)\). By (5.8), the unique vector satisfying \(\mathfrak a_0(v,h_1)=\langle v,g_1\rangle_0\) is

\[
h_1=(H_0+1)^{-1}g_1
=-\frac1{22}R_0+\frac1{45}D_1.
\tag{8.7}
\]

Subtract \(\xi\mathfrak a_\xi(v,h_1)\) from (8.6) and use (8.4). The resulting functional is \(O_L(\xi^2)\|v\|_{H^1}\). Test it with \(v=h_\xi-\xi h_1\); coercivity gives

\[
\|h_\xi-\xi h_1\|_{H^1}=O_L(\xi^2).
\]

Finally \(T_\xi h_1=h_1+O_L(\xi)\) in \(H^1\). We have proved the genuine moving-domain resolvent expansion

\[
\boxed{w_\xi=\xi\left(-\frac1{22}R_0+\frac1{45}D_1\right)
 +O_L(\xi^2)\quad\hbox{in }H^1.}
\tag{8.8}
\]

This argument uses no unverified derivative of an operator with changing domain and no finite-mode approximation to the interacting vacuum. The two modes suffice for the leading coefficient because the exact forcing has the leading term (8.5) and their free eigenvalues are known; every other box mode remains in the exact resolvent and in its proved remainder.

## 9. The exact second-order coefficient and its meaning

Equations (5.6), (8.5), (8.8), and \(\rho_\xi=1+O_L(\xi)\) give

\[
\begin{split}
I_\xi
&=\kappa\xi^2\left(\frac1{88}+\frac1{360}\right)
 +O_L(\kappa\xi^3)
=\frac7{495}\frac{b^2}{\kappa}
 +O_L\!\left(\frac{b^3}{\kappa^2}\right),\\
J_\xi^{\mathrm{num}}
&=\xi^2\left(\frac1{484}+\frac1{2700}\right)+O_L(\xi^3)
=\frac{199}{81675}\frac{b^2}{\kappa^2}
 +O_L\!\left(\frac{b^3}{\kappa^3}\right).
\end{split}
\tag{9.1}
\]

For example, the \(D_1\) contribution to \(I_\xi/(\kappa\xi^2)\) is \(\tfrac16\cdot\tfrac1{45}\cdot\tfrac34=1/360\); its contribution to \(J_\xi^{\mathrm{num}}/\xi^2\) is \(\tfrac1{45^2}\cdot\tfrac34=1/2700\). Thus the multiplicity and normalization of this second mode have not been suppressed.

Substituting (6.3) and (9.1) into the exact quotient difference (7.7), and using \(d_\xi+J_\xi^{\mathrm{num}}=1+O_L(\xi^2)\), yields

\[
\begin{split}
\mathcal R_{\mathrm{ret}}-\mathcal R_{\mathrm{corr}}
&=\kappa\xi^2\left(\frac7{495}+4\frac{199}{81675}\right)
 +O_L(\kappa\xi^3)\\
&=\frac{1951}{81675}\frac{b^2}{\kappa}
 +O_L\!\left(\frac{b^3}{\kappa^2}\right).
\end{split}
\tag{9.2}
\]

This proves (1.10). Together with (5.10) and (7.7), it proves the actual strict improvement for every sufficiently small positive \(\xi\) in each fixed full box. More explicitly, the proved remainder in (5.10) has an upper bound \(C_L\kappa^2\xi^3\) on some interval. Restricting that interval so \(C_L\xi<1/24\) gives \(\|g_\xi\|_\xi^2\geq\kappa^2\xi^2/24>0\). This deduction requires no sign assumption about any unknown higher coefficient.

In the original physical parameters (1.6), the leading difference is

\[
\frac{1951}{653400}\frac{1}{g_{\mathrm{YM}}^6a},
\qquad O_L\!\left(\frac{1}{g_{\mathrm{YM}}^{10}a}\right)
\tag{9.3}
\]

for the remainder. The exact Wilson constant shift is \(2bM=M/(g_{\mathrm{YM}}^2a)\). It contributes to \(E_\xi\) in (3.4) and cancels from the excitation operator \(H-E_\xi\), not from the Hamiltonian definition by omission.

The parameter conversion of the remainder scale, including its fixed numerical factor, is \(b^3/\kappa^2=1/(32g_{\mathrm{YM}}^{10}a)\); the corresponding leading scale is \(b^2/\kappa=1/(8g_{\mathrm{YM}}^6a)\).

The correction is an upper-bound improvement for the finite-box physical excitation gap: the spectral theorem and vacuum orthogonality give \(\operatorname{gap}(H|_{\mathrm{Gauss}})\leq\mathcal R_{\mathrm{corr}}<\mathcal R_{\mathrm{ret}}\) on the stated small-coupling interval. The retained quotient approaches \(3\kappa\), not zero, as \(\xi\to0\) at fixed \(\kappa\). A positive improvement of that quotient does not assert a vanishing gap. The explicit Neumann disk shrinks as \(M^{-1}\), and no other bound here removes that volume dependence. Thus the calculation establishes a genuinely full, finite, interacting three-dimensional spatial-lattice excitation correction without asserting a four-dimensional continuum mass-gap conclusion.

## 10. Provenance and exact checker

This extension supplies the full-box incidence, the all-plaquette vacuum expansion and norm/radius, and the controlled passage to the two leading free modes. The corresponding two-face calculation is in `../adjacent_plaquette_quantum_correction.md`; the general infinite-rank conditional-form construction is in `spatial_vacuum_elimination.tex`. All specific form-domain and coefficient arguments needed for this extension are reproduced above. The Schur/projection correction is not claimed as a new general method; primary-source attribution for that method is given in the companion proof (including Dusson--Sigal--Stamm, *The Feshbach--Schur map and perturbation theory*, arXiv:2105.02058v1, DOI `10.4171/ECR/18-1/5`). No new remote source retrieval was used for this bounded extension.

`check_bulk_plaquette_incidence.py` enumerates the entire open cubical graph and every face for \(L=2,3,4,5\). It checks the counts (1.2), face-edge containment, oriented occurrences of \(e,s\), the complete four-face star, the unique surviving pair (2.2), injectivity of elementary-face edge supports, and the exact rational Neumann-bound identity. Using rational arithmetic only, it checks the two free eigenvalues, \(1/12\), \(7/495\), \(199/81675\), \(1951/81675\), and the physical factor \(1951/653400\). These finite checks diagnose incidence and algebra; the continuum-free analytic and operator-domain proofs are Sections 3--9, not inferred from numerical computation.
