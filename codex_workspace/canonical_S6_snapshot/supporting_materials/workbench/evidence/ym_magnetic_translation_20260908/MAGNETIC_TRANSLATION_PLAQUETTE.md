# Exact gauge-projected magnetic translation in a full Wilson box

8 September 2026. All links and all elementary spatial plaquettes are retained. The vacuum below is the actual normalized positive ground state, not the one-time Wilson density. This proof is a finite-box calculation; the geometric diagonal in Section 9 concerns its explicitly computed strong-coupling coefficient, not an interchange of quantum and volume limits.

## 1. Original objects, constants, and operators

For an integer \(L\ge2\), take the open vertex box \(\{-L,\ldots,L\}^3\), all positively directed physical links \(e=(n,i)\) from \(n\) to \(n+\mathbf e_i\) contained in the box, and all elementary faces \(p=(n;i,j)\), \(i<j\). Write these sets as \(\mathsf E_L,\mathsf P_L\). Their complete counts are

\[
N=3(2L)(2L+1)^2,\qquad M=3(2L)^2(2L+1).
\tag{1.1}
\]

A negative traversal uses the inverse of the same physical link, not an independent variable. The face word and its real \(SU(2)\) trace are

\[
U_p=U_i(n)U_j(n+\mathbf e_i)U_i(n+\mathbf e_j)^{-1}U_j(n)^{-1},
\qquad W_p=\operatorname{tr}U_p.
\tag{1.2}
\]

Work in \(\mathcal H=L^2(SU(2)^{\mathsf E_L},dU)\), with product Haar probability measure and inner product conjugate-linear in its first entry. Put

\[
T_a=-i\sigma_a/2,\quad -2\operatorname{tr}(T_aT_b)=\delta_{ab},\qquad
X_{e,a}f=\left.\frac{d}{dt}f(\ldots,e^{tT_a}U_e,\ldots)\right|_{t=0},
\quad \Delta_e^T=\sum_aX_{e,a}^2.
\tag{1.3}
\]

For \(\kappa,b>0\), define

\[
H_0=-\sum_{e\in\mathsf E_L}\Delta_e^T,\quad
\mathcal V=\sum_{p\in\mathsf P_L}W_p,\quad \xi=b/\kappa,
\]
\[
H_{\kappa,b}=\kappa H_0+b\sum_p(2-W_p)
=\kappa(H_0-\xi\mathcal V)+2bM I.
\tag{1.4}
\]

The exact Wilson constant is \(2bM\). The original metric and physical parameter dictionary remain

\[
c(X,Y)=-\tfrac12\operatorname{tr}(XY),\quad
\Delta_e^c=4\Delta_e^T,\quad
\kappa=\frac{2g_{\mathrm{YM}}^2}{a},\quad
b=\frac1{2g_{\mathrm{YM}}^2a},\quad
\xi=\frac1{4g_{\mathrm{YM}}^4}.
\tag{1.5}
\]

Thus the kinetic term is also \(-g_{\mathrm{YM}}^2(2a)^{-1}\sum_e\Delta_e^c\). Nothing is absorbed into a redefined coupling.

For fixed \(h=(h_e)\in SU(2)^{\mathsf E_L}\), set

\[
(\mathcal T_hf)(U)=f((h_e^{-1}U_e)_e).
\tag{1.6}
\]

This is unitary and preserves Haar integrals. Its adjoint is \(\mathcal T_{h^{-1}}\). At each vertex use an independent gauge variable \(g_v\), acting by
\[
(\alpha_gU)_e=g_{s(e)}U_eg_{t(e)}^{-1},\qquad
(\Pi f)(U)=\int f(\alpha_gU)\prod_vdg_v.
\tag{1.7}
\]

Haar invariance proves \(\Pi^2=\Pi=\Pi^*\); its range consists precisely of invariant functions. The original convention \(U_e\mapsto h_{s(e)}^{-1}U_eh_{t(e)}\) is the same action with vertex variables \(g_v=h_v^{-1}\); these vertex variables are distinct from the fixed link assignments in (1.6).

Both \(\mathcal T_h\) and gauge transformations commute with \(H_0\). For the first assertion, differentiation replaces the basis \(T_a\) by \(\operatorname{Ad}(h_e^{-1})T_a\), another orthonormal basis, leaving the sum of squares unchanged. Right multiplication in a gauge transformation commutes with left derivatives, and its left multiplication has the same orthonormal-basis argument. Consequently \(\mathcal T_h\) is an isometry and \(\Pi\) a contraction on every Sobolev space defined by \(H_0+1\). Since each \(W_p\) is invariant, \(\Pi\) commutes with \(H_{\kappa,b}\).

## 2. Full vertex integral, with the shared-source factor retained

For \(p=(n;i,j)\), abbreviate

\[
\begin{array}{llll}
U=U_i(n),&V=U_j(n+\mathbf e_i),&
Z=U_i(n+\mathbf e_j),&Y=U_j(n),\\
a_0=h_i(n),&d_0=h_j(n+\mathbf e_i),&
c_0=h_i(n+\mathbf e_j),&b_0=h_j(n).
\end{array}
\tag{2.1}
\]

These subscripted matrices are not the scalar couplings or mesh. The translated word is exactly

\[
\mathcal T_hW_p=
\operatorname{tr}(a_0^{-1}U\,d_0^{-1}V\,Z^{-1}c_0\,Y^{-1}b_0).
\tag{2.2}
\]

In particular, an inverse physical link contributes \((h_e^{-1}U_e)^{-1}=U_e^{-1}h_e\); its insertion must remain on that side.

Denote the four vertex variables by \(g_0,g_i,g_{ij},g_j\). Substituting (1.7) into (2.2), cancelling adjacent factors, and cyclically rotating the trace gives

\[
\operatorname{tr}\!\left[
(g_0^{-1}b_0a_0^{-1}g_0)\,
U(g_i^{-1}d_0^{-1}g_i)\,VZ^{-1}
(g_j^{-1}c_0g_j)\,Y^{-1}
\right].
\tag{2.3}
\]

The \(g_{ij}\) factors cancel completely. The two links with common canonical source \(n\) produce the one product \(b_0a_0^{-1}\), conjugated by the one variable \(g_0\). They cannot be averaged as independent insertions.

For every complex \(2\times2\) matrix \(C\),

\[
\int g^{-1}Cg\,dg=\tfrac12\operatorname{tr}(C)I.
\tag{2.4}
\]

Indeed the Haar integral commutes with every \(SU(2)\) matrix. Commutation with all three Pauli one-parameter groups forces it to be scalar, and taking the trace fixes that scalar. Apply (2.4) independently to the three remaining variables in (2.3). The exact answer for every face is

\[
\boxed{\Pi\mathcal T_hW_{n;i,j}=\alpha_{n;i,j}(h)W_{n;i,j},}
\]
\[
\boxed{\alpha_{n;i,j}(h)=
\frac{
\operatorname{tr}[h_j(n)h_i(n)^{-1}]
\operatorname{tr}[h_j(n+\mathbf e_i)^{-1}]
\operatorname{tr}[h_i(n+\mathbf e_j)]
}{8}.}
\tag{2.5}
\]

The three traces are real and lie in \([-2,2]\), so \(\alpha_p\in[-1,1]\). The factor \(2^{-3}\) is one dimension factor for each nonempty vertex insertion. The fourth vertex contributes 1.

This applies without modification to every coordinate plane and boundary face. Four vertices and four physical edges are distinct in this open box. A cyclic change of the starting point leaves the Wilson function unchanged. Reversing the traversal gives the same function because \(\operatorname{tr}C^{-1}=\operatorname{tr}C\) on \(SU(2)\). The \(h_e\) remain attached to canonical physical sources, not to sources invented by reorienting the traversal.

Two exact checks show what would go wrong with different prescriptions.

- If \(a_0=b_0=k\) and \(c_0=d_0=I\), then \(\alpha_p=1\). Independently twirling the two shared-source factors would instead give \((\operatorname{tr}k/2)^2\).
- If all four matrices are \(k\), then \(\alpha_p=(\operatorname{tr}k/2)^2\), whereas their background face word \(kkk^{-1}k^{-1}\) is \(I\). At \(k=i\sigma_3\), the two alleged coefficients are 0 and 1.

Thus the projected translated face is not generally the original face times half the trace of a background holonomy.

We shall also need the exact inverse relation

\[
\alpha_p(h^{-1})=\alpha_p(h).
\tag{2.6}
\]

For the first factor, \(\operatorname{tr}(h_j^{-1}h_i)=
\operatorname{tr}[(h_jh_i^{-1})^{-1}]=\operatorname{tr}(h_jh_i^{-1})\), using cyclicity and the \(SU(2)\) inverse-trace identity. The other two factors have the same inverse-trace identity separately. This proves (2.6), including noncommuting assignments.

## 3. The true all-plaquette vacuum and its analytic expansion

The compact product Laplacian has compact resolvent. Adding the smooth bounded real potential preserves self-adjointness on its operator domain and compact resolvent. A ground minimizer can be taken nonnegative by \(|\nabla|f||\le|\nabla f|\), with zeros treated by the approximation \(\sqrt{|f|^2+\varepsilon^2}\). Elliptic regularity makes the ground eigenfunction smooth, and the strong maximum principle makes it strictly positive on the connected configuration manifold. If \(\psi>0\) is a ground eigenfunction, integration by parts and its eigen-equation give

\[
\langle\psi F,(H-E)\psi F\rangle
=\kappa\sum_{e,a}\int\psi^2|X_{e,a}F|^2\,dU.
\tag{3.1}
\]

The identity extends from smooth \(F\) to the form domain by density; the positive smooth function \(\psi\) and its reciprocal are bounded on this finite compact manifold. A second ground eigenfunction divided by \(\psi\) would make every derivative on the right zero, and thus be constant. Hence the normalized positive vacuum \(\psi_\xi\) is unique. Gauge invariance of \(H\) gives \(\Pi\psi_\xi=\psi_\xi\).

Here the needed local expansion follows from the full potential, as can be proved directly. A fundamental matrix coefficient has free Casimir \(3/4\) since \(-\sum_aT_a^2=3I/4\). On spin \(j\), the usual matrices \(J_3v_m=mv_m\), \(J_\pm v_m=\sqrt{(j\mp m)(j\pm m+1)}v_{m\pm1}\) give Casimir \(j(j+1)\) by multiplication. The Peter--Weyl decomposition and its tensor products give the full product spectrum: a simple constant eigenfunction at zero and first nonzero eigenvalue \(3/4\). Each \(W_p\) uses four distinct fundamental links, so

\[
H_0W_p=3W_p,\qquad
\int W_p\,dU=0,\qquad
\int W_pW_q\,dU=\delta_{pq}.
\tag{3.2}
\]

For the Haar assertions, integration over a singly occurring physical link kills its fundamental entries: multiplication by the center \(-I\) changes their signs. Different elementary squares have different four-edge supports, so one can integrate an edge occurring in one but not the other. A four-edge support determines the two coordinate directions and the lower corner of an elementary square, proving the asserted difference of supports. For equal faces, Haar invariance reduces the integral to \(\int(\operatorname{tr}U)^2dU=1\): Haar \(SU(2)\) is the unit sphere in \(\mathbb R^4\), and its scalar coordinate has second moment \(1/4\).

The interaction norm is exactly \(\|\mathcal V\|_\infty=2M\). The upper bound follows from \(|W_p|\le2\); equality follows at the all-identity configuration and then for the essential supremum by continuity and positive measure of neighborhoods. On \(|z|=3/8\), the free resolvent norm is at most \(8/3\). Its Neumann series under perturbation by \(-\xi\mathcal V\) therefore converges for

\[
\boxed{|\xi|<\frac3{16M}.}
\tag{3.3}
\]

The contour projection is analytic and rank one on this disk, since its rank is locally constant and is one at zero. For real \(\xi\), the bottom eigenvalue of \(H_0-\xi\mathcal V\) lies in \([-2M|\xi|,0]\), while the next is at least \(3/4-2M|\xi|>3/8\); the contour thus contains the actual ground eigenvalue \(e(\xi)\).

A Haar-mean-one analytic eigenvector \(\phi_\xi\) exists locally at zero. Explicitly, if \(q=16M|\xi|/3\), the contour resolvent difference bounds the projection difference by \(q/(1-q)\); for \(q<1/2\), the projection of 1 has nonzero Haar mean and supplies this normalization. Differentiating the eigen-equation gives

\[
e(0)=e'(0)=0,\qquad \phi'_0=\mathcal V/3,\qquad
\int\phi_\xi^2dU=1+(M/9)\xi^2+O_L(\xi^3).
\tag{3.4}
\]

In the derivative equation the Haar mean forces \(e'(0)=0\), and (3.2) solves the mean-zero equation \(H_0\phi'_0=\mathcal V\). The squared normalization follows because all higher coefficients of \(\phi_\xi\) have zero Haar mean and \(\|\mathcal V\|_2^2=M\).

Analyticity and bounded Taylor remainders hold in every fixed Sobolev norm. The equation
\[
\phi_\xi=(H_0+1)^{-1}[(e(\xi)+1+\xi\mathcal V)\phi_\xi]
\]
upgrades analyticity by two derivatives at a time; multiplication by the fixed smooth \(\mathcal V\) is bounded on each integer Sobolev space. Sobolev embedding in the fixed dimension \(3N\) also gives \(C^k\) expansions for every fixed \(k\). Normalize positively for real \(\xi\). The actual vacuum then has

\[
\psi_\xi=1+\xi A+\xi^2D+O_L(\xi^3),\qquad
A=\frac13\sum_pW_p,\qquad \int D\,dU=-\frac12\|A\|_2^2=-\frac M{18}.
\tag{3.5}
\]

The last identity follows exactly from \(\|\psi_\xi\|_2=1\). The coefficient \(D\) here is a function, not an assumed truncation of the interacting vacuum. The physical ground energy is exactly
\[
E_\xi=\kappa e(\xi)+2bM.
\tag{3.6}
\]

All constants in these local analytic estimates may depend on the full box. The disk (3.3) is the guaranteed spectral-projection disk, not a uniform-volume bound on every Taylor remainder.

## 4. Exact physical state, norm, energy, and vanishing criterion

Define

\[
F_{\xi,h}=\Pi\mathcal T_h\psi_\xi,\quad
c_{\xi,h}=\langle\psi_\xi,\mathcal T_h\psi_\xi\rangle,\quad
\chi_{\xi,h}=F_{\xi,h}-c_{\xi,h}\psi_\xi.
\tag{4.1}
\]

These functions are real; the first two uncentered functions and the vacuum are strictly positive. Hence \(0<c_{\xi,h}\le1\), the upper bound following from unitarity. Since \(\Pi\psi_\xi=\psi_\xi\),

\[
\langle\psi_\xi,\chi_{\xi,h}\rangle=0,\qquad
\|\chi_{\xi,h}\|_2^2=\|F_{\xi,h}\|_2^2-c_{\xi,h}^2.
\tag{4.2}
\]

The state is smooth and invariant. Its exact excitation quotient when it is nonzero is

\[
\boxed{\mathcal Q_{\xi,h}
=\frac{\|(H_{\kappa,b}-E_\xi)^{1/2}\chi_{\xi,h}\|_2^2}
{\|\chi_{\xi,h}\|_2^2}
=\frac{\displaystyle\kappa\sum_{e,a}\int\psi_\xi^2
\left|X_{e,a}\left(\frac{F_{\xi,h}}{\psi_\xi}\right)\right|^2dU}
{\displaystyle\|F_{\xi,h}\|_2^2-c_{\xi,h}^2}.}
\tag{4.3}
\]

Apply (3.1) to \(F_{\xi,h}/\psi_\xi-c_{\xi,h}\) to prove this; the derivative of the centering constant vanishes. Smoothness and strict positivity on a compact configuration space justify the form domain and all displayed integrals. The true vacuum is kept in every factor.

Write the finite real coefficients

\[
\mathcal S_h=\sum_p(1-\alpha_p),\qquad
\mathcal R_h=\sum_p(1-\alpha_p^2),\qquad
\mathcal D_h=\sum_p(1-\alpha_p)^2.
\tag{4.4}
\]

All three are nonnegative and \(\mathcal D_h=2\mathcal S_h-\mathcal R_h\).

For every \(b>0\), not just perturbatively, the following complete classification holds:

\[
\boxed{
\chi_{\xi,h}=0
\ \Longleftrightarrow\ \mathcal T_h\psi_\xi=\psi_\xi
\ \Longleftrightarrow\ \mathcal T_h\mathcal V=\mathcal V
\ \Longleftrightarrow\ (\alpha_p=1\text{ for every }p)
\ \Longleftrightarrow\ \mathcal D_h=0.}
\tag{4.5}
\]

If \(\chi=0\), then \(F=c\psi\). Haar integration, preserved by both \(\Pi\) and \(\mathcal T_h\), yields \(\int\psi=c\int\psi\); strict positivity forces \(c=1\). Equality \(\|\Pi\mathcal T_h\psi\|=\|\mathcal T_h\psi\|=1\) in an orthogonal projection norm implies \((I-\Pi)\mathcal T_h\psi=0\) by Pythagoras. Thus \(\mathcal T_h\psi=\psi\).

If this last equality holds, apply \(\mathcal T_h\) to the eigen-equation. It commutes with \(H_0\), and translates multiplication by \(\mathcal V\) to multiplication by \(\mathcal T_h\mathcal V\). Subtracting the original equation gives
\(b(\mathcal T_h\mathcal V-\mathcal V)\psi=0\).
Since \(b>0\) and \(\psi>0\), the potentials agree. Project that equality by \(\Pi\), use (2.5), and pair with \(W_q\) in (3.2); every \(\alpha_q\) is 1.

Conversely, if every \(\alpha_p=1\), then
\(\|\Pi\mathcal T_hW_p\|_2=\|W_p\|_2=\|\mathcal T_hW_p\|_2\).
Projection norm equality gives \(\mathcal T_hW_p=W_p\), in \(L^2\) and hence pointwise by smoothness. Therefore \(\mathcal T_h\) preserves \(\mathcal V\), commutes with the full Hamiltonian, and fixes its unique positive normalized vacuum. This gives \(\chi=0\). A sum of real squares is zero exactly when each square is zero, completing (4.5). At \(b=0\) the vacuum is constant and every such centered state is zero; this explains why \(b>0\) is required in the classification.

There is also a compact exact unprojected energy identity, expressed in the true moments \(m_{p,\xi}=\int W_p\psi_\xi^2dU\):

\[
\boxed{\langle\mathcal T_h\psi_\xi,
(H_{\kappa,b}-E_\xi)\mathcal T_h\psi_\xi\rangle
=b\sum_p(1-\alpha_p)m_{p,\xi}.}
\tag{4.6}
\]

The kinetic expectation is unchanged by \(\mathcal T_h\), so subtracting the vacuum energy leaves
\(b\sum_p(m_{p,\xi}-\langle\psi_\xi,
(\mathcal T_h^{-1}W_p)\psi_\xi\rangle)\).
The density \(\psi_\xi^2\) is invariant, so the last multiplication function may be averaged by \(\Pi\). Equations (2.5)--(2.6) replace it exactly by \(\alpha_pW_p\), proving (4.6). No sign of any individual moment is assumed. The aggregate is nonnegative because \(H-E_\xi\) is nonnegative.

## 5. First nonzero norm and excitation quotient, with exact coupling parity

Equations (2.5) and (3.5) give the actual first-order vector

\[
\chi_{\xi,h}=\xi V_h+O_L(\xi^2),\qquad
V_h=\frac13\sum_p(\alpha_p-1)W_p.
\tag{5.1}
\]

The error is valid in \(H^2\) and every fixed higher Sobolev space. At this stage its constant may be chosen independently of \(h\) on the fixed box, because translations are Sobolev isometries and \(\Pi\) a Sobolev contraction. Equation (3.2) gives

\[
\|V_h\|_2^2=\mathcal D_h/9,\qquad H_0V_h=3V_h.
\tag{5.2}
\]

The second vacuum coefficient is not needed as a function to compute the scalar centering, but its exact normalization mean is needed. From (3.5), Haar preservation, and (3.2),

\[
\begin{split}
c_{\xi,h}
&=1+\xi^2\big(\langle A,\mathcal T_hA\rangle-\|A\|_2^2\big)+O_L(\xi^3)
=1-\frac{\xi^2}{9}\mathcal S_h+O_L(\xi^3),\\
\|F_{\xi,h}\|_2^2
&=1+\xi^2\big(\|\Pi\mathcal T_hA\|_2^2-\|A\|_2^2\big)+O_L(\xi^3)
=1-\frac{\xi^2}{9}\mathcal R_h+O_L(\xi^3).
\end{split}
\tag{5.3}
\]

For example, invariance of \(A\) gives
\(\langle A,\mathcal T_hA\rangle=\langle A,\Pi\mathcal T_hA\rangle
=\sum_p\alpha_p/9\). The loss of norm under Gauss projection, measured here by \(\mathcal R_h\), is not the same as the overlap loss \(\mathcal S_h\); both enter (4.2).

An exact central link transformation eliminates all odd terms of these scalar expansions. Define

\[
z_i(n)=(-1)^{\sum_{k<i}n_k}I,\qquad \mathcal Z=\mathcal T_z.
\tag{5.4}
\]

For a face \(i<j\), shifting \(n\) by \(\mathbf e_i\) changes \(z_j\) by a sign, whereas shifting by \(\mathbf e_j\) does not change \(z_i\). Multiplying the four link signs around the face therefore gives \(-1\). Each inverse sign equals the sign itself. Thus **every** face in **every** plane satisfies

\[
\mathcal ZW_p=-W_p,\qquad
\mathcal Z(H_0-\xi\mathcal V)\mathcal Z^{-1}=H_0+\xi\mathcal V.
\tag{5.5}
\]

The central translation \(\mathcal Z\) is a real unitary involution. Centrality implies it commutes with every gauge transformation and every \(\mathcal T_h\), hence with \(\Pi\). For the real analytic auxiliary family near zero, uniqueness of its positive normalized vacuum gives

\[
e(-\xi)=e(\xi),\quad
\psi_{-\xi}=\mathcal Z\psi_\xi,\quad
c_{-\xi,h}=c_{\xi,h},\quad
F_{-\xi,h}=\mathcal ZF_{\xi,h},\quad
\chi_{-\xi,h}=\mathcal Z\chi_{\xi,h}.
\tag{5.6}
\]

Negative \(\xi\) is only an analytic device here; the physical statements have \(b>0\). The exact excitation operator is
\(\kappa(H_0-\xi\mathcal V-e(\xi))\), since the scalar in (3.6) cancels exactly. It is conjugated to its negative-\(\xi\) version by \(\mathcal Z\). Therefore the squared norm of \(\chi\), its excitation quadratic form, the centering scalar, and the squared norm of the uncentered projection are even real-analytic scalar functions of \(\xi\). In particular their cubic coefficients vanish. Equations (4.2), (5.2), and (5.3) prove

\[
\boxed{\begin{split}
c_{\xi,h}&=1-\frac{\xi^2}{9}\mathcal S_h+O_L(\xi^4),\\
\|F_{\xi,h}\|_2^2&=1-\frac{\xi^2}{9}\mathcal R_h+O_L(\xi^4),\\
\|\chi_{\xi,h}\|_2^2&=\frac{\xi^2}{9}\mathcal D_h+O_L(\xi^4).
\end{split}}
\tag{5.7}
\]

To compute the energy, use the \(H^2\) expansion (5.1) in the exact excitation operator and \(e(\xi)=O_L(\xi^2)\). The first term is
\(\kappa\xi^2\langle V_h,H_0V_h\rangle\), and evenness removes the cubic term. Hence

\[
\boxed{\|(H_{\kappa,b}-E_\xi)^{1/2}\chi_{\xi,h}\|_2^2
=\frac{\kappa\xi^2}{3}\mathcal D_h+O_L(\kappa\xi^4).}
\tag{5.8}
\]

For each fixed \(h\) with \(\mathcal D_h>0\), the vector is nonzero for every \(b>0\) by (4.5). Its first nonzero norm and leading exact excitation quotient as \(\xi\downarrow0\) are

\[
\boxed{
\|\chi_{\xi,h}\|_2=\frac{\xi}{3}\sqrt{\mathcal D_h}+O_{L,h}(\xi^3),
\qquad \mathcal Q_{\xi,h}=3\kappa+O_{L,h}(\kappa\xi^2).}
\tag{5.9}
\]

The dependence after division must not be discarded near zero \(\mathcal D_h\). More explicitly, take a fixed-box constant \(C_L\) bounding both remainders in the last line of (5.7) and in (5.8), after extraction of \(\xi^4\) and \(\kappa\xi^4\), on a sufficiently small real interval. Such a constant can be chosen uniformly in \(h\): the previous Sobolev and analytic bounds hold uniformly for the compact family of translations, and the spectral expansion is the same vacuum. If \(C_L\xi^2\le\mathcal D_h/18\), then

\[
|\mathcal Q_{\xi,h}-3\kappa|
\le\frac{72C_L}{\mathcal D_h}\,\kappa\xi^2.
\tag{5.10}
\]

Indeed write the quotient as
\(\kappa(\mathcal D_h/3+\xi^2r_1)/(\mathcal D_h/9+\xi^2r_2)\)
with \(|r_i|\le C_L\). Subtracting \(3\kappa\) gives a numerator of magnitude at most \(4C_L\kappa\xi^2\); the denominator is at least \(\mathcal D_h/18\).

In the original physical constants, the leading squared norm is
\(\mathcal D_h/(144g_{\mathrm{YM}}^8)\), the leading unnormalized excitation form is \(\mathcal D_h/(24g_{\mathrm{YM}}^6a)\), and the leading quotient is \(6g_{\mathrm{YM}}^2/a\). The exact remainder scale of the quotient before its dimensionless constant is
\(\kappa\xi^2=1/(8g_{\mathrm{YM}}^6a)\). These are substitutions into the proved finite-box expressions, not claims about weak coupling or a continuum limit.

## 6. Native nonwrapping flux: exact coefficients for all three planes

Now take precisely

\[
h_1(n)=\exp(-\theta n_2H_c),\qquad h_2(n)=h_3(n)=I,\qquad
H_c=i\sigma_3=-2T_3,\qquad \theta\in\mathbb R.
\tag{6.1}
\]

Here \(c(H_c,H_c)=1\) and its squared norm in (1.3) is 4. Its eigenvalues are \(i,-i\), giving
\(\operatorname{tr}\exp(-tH_c)/2=\cos t\).
No integer coordinate has been wrapped or rescaled, and no factor of 2 has been absorbed into \(\theta\).

Substitution into the exact full-vertex formula (2.5), with \(m=n_2\), yields

\[
\boxed{
\begin{array}{ll}
\alpha_{n;1,2}=\cos(m\theta)\cos((m+1)\theta),&-L\le m\le L-1,\\
\alpha_{n;1,3}=\cos^2(m\theta),&-L\le m\le L,\\
\alpha_{n;2,3}=1.&
\end{array}}
\tag{6.2}
\]

The \(13\)-coefficient is not always one, despite the trivial background holonomy in that plane. The \(12\)-coefficient is not generally the background normalized trace \(\cos\theta\). Both facts follow from the actual independent vertex twirls, rather than from a curvature substitution.

For each permitted \(m\), the number of \(12\)-faces is \(2L(2L+1)\): \(n_1\) has \(2L\) choices and \(n_3\) has \(2L+1\). The number of \(13\)-faces for each \(m\) is \(4L^2\). Thus the exact coefficient entering (5.7)--(5.10) is

\[
\boxed{\begin{split}
\mathcal D_L(\theta)
={}&2L(2L+1)\sum_{m=-L}^{L-1}
[1-\cos(m\theta)\cos((m+1)\theta)]^2\\
&+4L^2\sum_{m=-L}^{L}\sin^4(m\theta).
\end{split}}
\tag{6.3}
\]

The separately relevant overlap coefficient is

\[
\begin{split}
\mathcal S_L(\theta)
={}&2L(2L+1)\sum_{m=-L}^{L-1}
[1-\cos(m\theta)\cos((m+1)\theta)]\\
&+4L^2\sum_{m=-L}^{L}\sin^2(m\theta).
\end{split}
\tag{6.4}
\]

The projection loss is exactly \(\mathcal R_L=2\mathcal S_L-\mathcal D_L\). The first-order vector itself is

\[
\begin{split}
V_\theta=\frac13\bigg[
&\sum_{p=(n;1,2)}(\cos(n_2\theta)\cos((n_2+1)\theta)-1)W_p\\
&-\sum_{p=(n;1,3)}\sin^2(n_2\theta)W_p
\bigg],\qquad \chi_{\xi,\theta}=\xi V_\theta+O_L(\xi^2).
\end{split}
\tag{6.5}
\]

Every \(23\)-plaquette is still present in the full potential and actual vacuum; only its displayed first-order coefficient is zero.

### 6.1 Finite Fourier form with no undefined resonances

Define the finite trigonometric polynomials

\[
\mathcal O_L(t)=\sum_{m=-L}^{L-1}\cos((2m+1)t),\qquad
\mathcal K_L(t)=\sum_{m=-L}^{L}\cos(mt).
\tag{6.6}
\]

Finite geometric summation gives, whenever their denominators are nonzero,

\[
\mathcal O_L(t)=\frac{\sin(2Lt)}{\sin t},\qquad
\mathcal K_L(t)=\frac{\sin((L+\tfrac12)t)}{\sin(t/2)}.
\tag{6.7}
\]

At all other arguments, their values are the finite sums (6.6), equivalently the continuous extensions. In particular
\(\mathcal O_L(k\pi)=2L(-1)^k\) and
\(\mathcal K_L(2k\pi)=2L+1\).

With \(a_\theta=1-\tfrac12\cos\theta\), product-to-sum and the identity
\(\sin^4x=(3-4\cos2x+\cos4x)/8\) give exactly

\[
\begin{split}
\sum_{m=-L}^{L-1}[1-\cos(m\theta)\cos((m+1)\theta)]^2
&=2L(a_\theta^2+\tfrac18)-a_\theta\mathcal O_L(\theta)
+\tfrac18\mathcal O_L(2\theta),\\
\sum_{m=-L}^{L}\sin^4(m\theta)
&=\tfrac38(2L+1)-\tfrac12\mathcal K_L(2\theta)
+\tfrac18\mathcal K_L(4\theta).
\end{split}
\tag{6.8}
\]

Multiplying by the respective face counts in (6.3) gives the exact closed Fourier form of \(\mathcal D_L\). The two unsquared sums in (6.4) are respectively

\[
2La_\theta-\tfrac12\mathcal O_L(\theta),\qquad
\tfrac12(2L+1)-\tfrac12\mathcal K_L(2\theta).
\tag{6.9}
\]

These expressions are finite polynomial identities and remain valid at every resonance with (6.6); they introduce no singular angles.

### 6.2 Exact zero angles, special values, and elementary bounds

The coefficient \(\mathcal D_L\) is even and \(2\pi\)-periodic. Its \(m=0,-1\) terms in the first sum give

\[
4L(2L+1)(1-\cos\theta)^2\le\mathcal D_L(\theta).
\tag{6.10}
\]

Each term in that sum is at most 4 and each sine fourth power at most 1, giving the nonoptimal but explicit full-box upper bound

\[
\mathcal D_L(\theta)\le5(2L)^2(2L+1)=5M/3.
\tag{6.11}
\]

At \(\theta\in2\pi\mathbb Z\), every \(h_e=I\). Together with (6.10), this proves

\[
\mathcal D_L(\theta)=0\ \Longleftrightarrow\ \theta\in2\pi\mathbb Z.
\tag{6.12}
\]

The exact all-coupling classification (4.5) therefore gives

\[
\boxed{\chi_{\xi,\theta}=0\ \Longleftrightarrow\
\theta\in2\pi\mathbb Z,\qquad b>0.}
\tag{6.13}
\]

At those angles the quotient of this zero vector is undefined, not zero. At every other angle it is the quotient of a nonzero, invariant, vacuum-orthogonal physical vector.

Two explicit nonzero values are

\[
\mathcal D_L(\pi)=16L^2(2L+1),\qquad
\mathcal D_L(\pi/2)=4L^2(3L+1+\varepsilon_L),\quad
\varepsilon_L=L\bmod2.
\tag{6.14}
\]

At \(\pi\), every \(12\)-coefficient is \(-1\) and the \(13,23\) coefficients are 1, proving the first value by counting faces. At \(\pi/2\), consecutive cosine factors have zero product, giving contribution 1 from every \(12\)-face. Among \(-L,\ldots,L\) there are \(L+\varepsilon_L\) odd integers, which are exactly the nonzero fourth-power sine terms. This proves the second value with its parity dependence.

## 7. Exact small-angle polynomial and a signed explicit remainder

For each integer \(m\), put \(r_m=m^2+m+\tfrac12\). Elementary Taylor expansion gives

\[
1-\cos(m\theta)\cos((m+1)\theta)=r_m\theta^2+O_L(\theta^4),
\qquad \sin^2(m\theta)=m^2\theta^2+O_L(\theta^4)
\tag{7.1}
\]

uniformly over the finite index ranges of the fixed box. Thus

\[
\mathcal D_L(\theta)=\mathcal A_L\theta^4+O_L(\theta^6),
\]
\[
\begin{split}
\mathcal A_L
&=2L(2L+1)\sum_{m=-L}^{L-1}r_m^2+4L^2\sum_{m=-L}^{L}m^4\\
&=\boxed{\frac{L^2(2L+1)}{15}
(24L^4+24L^3+8L^2-4L+3)}\\
&=\frac{16}{5}L^7+\frac{24}{5}L^6+\frac83L^5+\frac2{15}L^3+\frac15L^2.
\end{split}
\tag{7.2}
\]

Here are the exact finite sums needed to verify every coefficient:

\[
\sum_{m=-L}^{L-1}r_m^2=\frac{L(4L^4+1)}{10},\qquad
\sum_{m=-L}^{L}m^4
=\frac{L(L+1)(2L+1)(3L^2+3L-1)}{15}.
\tag{7.3}
\]

For the first identity, expand \(r_m^2=m^4+2m^3+2m^2+m+\tfrac14\). Each polynomial identity in (7.3) is proved directly by its value at \(L=1\) and by subtracting its value at \(L\) from its value at \(L+1\): the left side adds exactly the two new endpoint terms, and expansion of the displayed right side gives those same terms. Substituting (7.3) and multiplying gives (7.2), so its degree-seven dependence has not been hidden in a remainder.

The unsquared overlap coefficient has the distinct exact leading polynomial

\[
\mathcal S_L(\theta)=\mathcal B_L\theta^2+O_L(\theta^4),\qquad
\mathcal B_L=\frac{2L^2(2L+1)(4L^2+2L+1)}3.
\tag{7.4}
\]

In fact
\(\sum_{m=-L}^{L-1}r_m=L(2L^2+1)/3\) and
\(\sum_{m=-L}^{L}m^2=L(L+1)(2L+1)/3\);
the same endpoint-increment proof establishes both identities. Multiplication by the respective face counts in (6.4) proves (7.4).

We now replace the unspecified remainder in (7.2) by an explicit bound. For every real \(t\),

\[
0\le\tfrac12t^2-(1-\cos t)\le t^4/24.
\tag{7.5}
\]

The lower bound is \(1-\cos t=2\sin^2(t/2)\le t^2/2\); the upper bound is Taylor's theorem with the fourth derivative of cosine bounded by 1. For real \(x,y\), set
\[
u=1-\cos x\cos y,\qquad q=(x^2+y^2)/2.
\]
Using \(u=\tfrac12[(1-\cos(x+y))+(1-\cos(x-y))]\) in (7.5) gives

\[
0\le u\le q,\quad
0\le q-u\le\frac{(x+y)^4+(x-y)^4}{48}
=\frac{x^4+6x^2y^2+y^4}{24}\le q^2/3.
\tag{7.6}
\]

The last inequality is equivalent to \((x^2-y^2)^2\ge0\). It follows that

\[
0\le q^2-u^2=(q-u)(q+u)\le\tfrac23q^3.
\tag{7.7}
\]

Similarly, with \(u=\sin^2x=(1-\cos2x)/2\) and \(q=x^2\), (7.5) gives \(0\le q-u\le q^2/3\), hence (7.7) again. Substituting \(x=m\theta,y=(m+1)\theta\) in the first case and \(x=m\theta\) in the second proves the signed exact bound

\[
\boxed{0\le\mathcal A_L\theta^4-\mathcal D_L(\theta)
\le\mathcal E_L|\theta|^6,}
\]
\[
\mathcal E_L=\frac23\left[
2L(2L+1)\sum_{m=-L}^{L-1}r_m^3+
4L^2\sum_{m=-L}^{L}m^6\right].
\tag{7.8}
\]

This proof is valid for every real \(\theta\), in particular for the requested regime \(|\theta|(L+1)\le1\).

The finite polynomial sum in (7.8) can be written exactly as

\[
\mathcal E_L=
\frac{L^2(2L+1)}{315}
(240L^6+360L^5+156L^4-120L^3-10L^2+40L-1).
\tag{7.9}
\]

For explicit verification, the two sums before multiplication are

\[
\begin{split}
\sum_{m=-L}^{L-1}r_m^3
&=\frac27L^7-\frac15L^5+\frac16L^3-\frac1{420}L,\\
\sum_{m=-L}^{L}m^6
&=\frac{L(L+1)(2L+1)(3L^4+6L^3-3L+1)}{21}.
\end{split}
\tag{7.10}
\]

The first polynomial has value \(1/4\) at \(L=1\), and its increment from \(L\) to \(L+1\) is \(2(L^2+L+\tfrac12)^3\), exactly the new two terms. The second has value 2 at \(L=1\) and increment \(2(L+1)^6\). This proves both formulas by induction, and substitution into (7.8) gives (7.9).

A simpler upper bound needs no signed polynomial comparison. On \(-L\le m\le L-1\), \(0<r_m\le L^2\); on \(-L\le m\le L\), \(m^6\le L^6\). Thus
\[
\begin{split}
\mathcal E_L
&\le\frac23\big[2L(2L+1)(2L)L^6+
4L^2(2L+1)L^6\big]\\
&=\frac{16}{3}L^8(2L+1)\le16L^9
\end{split}
\]
for \(L\ge1\). We have established the fully explicit form

\[
\boxed{|\mathcal D_L(\theta)-\mathcal A_L\theta^4|
\le16L^9|\theta|^6,\qquad L\ge2,\ \theta\in\mathbb R,}
\tag{7.11}
\]
with the stronger sign information in (7.8).

## 8. The order of the finite-box quantum and angular statements

For each fixed box and angle, the proved actual-vacuum expansion gives

\[
\lim_{\xi\downarrow0}\frac{\|\chi_{\xi,\theta}\|_2^2}{\xi^2}
=\frac{\mathcal D_L(\theta)}9.
\tag{8.1}
\]

Combining it with (7.2) gives the iterated, and therefore unambiguous, small-angle statement

\[
\lim_{\theta\to0}\frac1{\theta^4}
\left(\lim_{\xi\downarrow0}\frac{\|\chi_{\xi,\theta}\|_2^2}{\xi^2}\right)
=\frac{\mathcal A_L}{9}.
\tag{8.2}
\]

For every fixed \(\theta\notin2\pi\mathbb Z\), the quotient tends to \(3\kappa\) as \(\xi\downarrow0\), by (5.9). Its leading angular coefficient cancels because the entire first-order vector lies in the proved free eigenvalue-3 eigenspace (5.2). The coefficient has not vanished from the norm, the overlap, or the explicit denominator-sensitive error estimate (5.10).

The smallness of a centered state's norm is not by itself smallness of the energy quotient after normalization. In particular (8.2) is not a zero-gap conclusion. No fixed-\(b\) small-angle theorem is inferred by interchanging the limits in (8.2); the parent operator calculation treats that separate order directly.

## 9. Original admissible cusp diagonal: exact coefficient scaling

Retain the original geometric sequence, with no alteration of its units or integer coordinates:

\[
L_j=j^2,\qquad a_j=\frac1{100j},\qquad
T_j^{\mathrm{cusp}}=j^2,\qquad M_j^{\mathrm{cover}}=j,
\qquad D_j^{\mathrm{geom}}=j^4(1+O(j^{-2})).
\tag{9.1}
\]

The determinant \(D_j^{\mathrm{geom}}\) and its asymptotic in (9.1) are the original retained-cusp geometric data from the parent calculation, not the number \(M\) of lattice faces and not the function \(\mathcal D_L\). Their map to the native link parameter is

\[
\theta_j=\frac{2\pi a_j^2}{D_j^{\mathrm{geom}}}
=Cj^{-6}(1+O(j^{-2})),\qquad C=\frac{2\pi}{10^4}.
\tag{9.2}
\]

The second equality follows by substituting \(a_j^2=1/(10^4j^2)\) and inverting \(1+O(j^{-2})\), which is bounded away from zero for all sufficiently large \(j\). Consequently
\(|\theta_j|(L_j+1)=O(j^{-4})\), so the requested small-angle box regime holds eventually.

The exact polynomial (7.2) gives

\[
\mathcal A_{j^2}=\frac{16}{5}j^{14}(1+O(j^{-2})).
\tag{9.3}
\]

Meanwhile (7.11), with its explicit constant rather than a box-dependent Taylor symbol, gives

\[
0\le j^{10}\big(\mathcal A_{j^2}\theta_j^4
-\mathcal D_{j^2}(\theta_j)\big)
\le16j^{28}|\theta_j|^6=O(j^{-8}).
\tag{9.4}
\]

The fourth power in (9.2) and (9.3) gives
\(j^{10}\mathcal A_{j^2}\theta_j^4
=(16/5)C^4(1+O(j^{-2}))\).
Squeezing with (9.4) proves the exact geometric coefficient limit

\[
\boxed{\lim_{j\to\infty}j^{10}\mathcal D_{j^2}(\theta_j)
=\frac{16}{5}\left(\frac{2\pi}{10^4}\right)^4.}
\tag{9.5}
\]

In particular the sequential true-vacuum coefficient has
\[
\lim_{j\to\infty}j^{10}
\left(\lim_{\xi\downarrow0}
\frac{\|\chi_{\xi,\theta_j}\|_2^2}{\xi^2}\right)
=\frac{16}{45}\left(\frac{2\pi}{10^4}\right)^4.
\tag{9.6}
\]
The inner limit in (9.6) is taken separately on each finite box \(L_j\), exactly as in (8.1). Equation (9.6) is not a simultaneous quantum limit.

Indeed the number of all faces on this diagonal is
\[
M_j^{\mathrm{faces}}=12j^4(2j^2+1),
\]
so the explicit spectral-projection disk (3.3) is exactly

\[
|\xi|<\frac1{64j^4(2j^2+1)}
\sim\frac1{128j^6}.
\tag{9.7}
\]

The Sobolev/Taylor constants \(C_{L_j}\) in (5.7)--(5.10) also remain box-dependent, and (5.10) further divides by \(\mathcal D_{j^2}(\theta_j)\), which is of order \(j^{-10}\). These facts are displayed to prevent use of an unproved uniform remainder.

For the original mesh and fixed \(g_{\mathrm{YM}}>0\),
\[
\kappa_j=200g_{\mathrm{YM}}^2j,\qquad
b_j=\frac{50j}{g_{\mathrm{YM}}^2},\qquad
\xi_j=\frac1{4g_{\mathrm{YM}}^4},\qquad
3\kappa_j=600g_{\mathrm{YM}}^2j.
\tag{9.8}
\]

The ratio \(\xi_j\) is fixed, not shrinking, and eventually exceeds the sufficient disk (9.7). Consequently neither the leading quotient \(3\kappa_j\) nor its fixed-box remainder justifies a fixed-\(g_{\mathrm{YM}}\), growing-box quantum limit. Equations (9.5)--(9.6) concern the explicit coefficient and the displayed order of limits only. They neither prove nor refute a four-dimensional continuum gap.

## 10. Exact verification and provenance

The companion checker, check_magnetic_translation.py, uses integer and rational quaternion arithmetic. The four conjugations by \(I,-i\sigma_1,-i\sigma_2,-i\sigma_3\) average every \(2\times2\) matrix exactly to its scalar part: each imaginary coefficient has two positive and two negative conjugation signs, while the scalar coefficient is fixed. Thus their discrete average is precisely (2.4), not a numerical Haar sample. After the cancellations in (2.3), each independent vertex appears in only one such matrix twirl. The checker's full \(4^4=256\)-term vertex average is therefore exact for the original plaquette integrand. It evaluates the original translated, gauge-transformed word before using the projected formula, including noncommuting rational assignments, shared-source cancellation, and the explicit failure of the background-holonomy rule.

For \(L=2,\ldots,7\), the checker tests the whole-box angular sums at the rational-cosine angles \(0,\pi/2,\pi,\pi/3\), the Fourier identities, special angles, both leading \(L\)-polynomials, and the sign of the central cochain on every face in every plane. It also tests the sixth-order error polynomial and its explicit upper bound. These are exact algebra/incidence diagnostics, not a vacuum simulation or a continuum computation.

The full-box vacuum construction and metric dictionary agree with BULK_PLAQUETTE_EXTENSION.md; the ground-state form agrees with spatial_vacuum_elimination.tex. All specific definitions and proofs used in this calculation are written above. Standard compact-group and elliptic spectral facts are used with the displayed compact state space, exact Casimir, domain, and bounded potential; no external numerical claim or unproved marginal closure enters. No remote action, new agent, PDF generation, or heavy job was used. The result is an exact full-vertex projection and a controlled finite interacting quantum excitation calculation, together with the explicit geometric coefficient limit (9.5).
