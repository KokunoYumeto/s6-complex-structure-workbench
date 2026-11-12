# Retained complete proof inputs from the volume-uniform lane

Exact sections 1, 10, 11, 12, and 15 from VOLUME_UNIFORM_LOCAL_VACUUM_ESTIMATES.md. The copied mathematical text below is unchanged; source SHA-256: 07df08ef2c5a7f0d9620a811dedf0e2ba1fa5dd9d0f28f3d16440c3d89dc57ca.

The blocking manuscript uses the Hamiltonian and vacuum definitions in Section 1, the conditional operator construction in Section 10, the complete fixed-point proof in Section 11, the similarity/resolvent proof (12.1)–(12.8), and the physical projection/support/resolvent proof (15.1)–(15.13) with its conditional consequence (15.22)–(15.23). Other retained statements belong to their original context and are not additional claims imported into the blocking manuscript. Its source g_YM is exactly our g; its energy Ecal is our E_0. The source scalar alpha in (12.7) is denoted c_vac in our dictionary and is not our single-link density bound alpha.

# 1. Original Hamiltonian, physical state, and geometric input

Fix an integer \(L\ge2\). The vertices are
\(\mathsf V_L=\{-L,\ldots,L\}^3\). A physical link
\(e=(n,i)\) is oriented from \(n\) to \(n+\mathbf e_i\) whenever
both endpoints are vertices. Its independent variable is \(U_e\in SU(2)\);
an inverse traversal contributes \(U_e^{-1}\). Every contained elementary
face \(p=(n;i,j)\), \(i<j\), is included, with
\[
W_p=\operatorname{tr}\left[
 U_i(n)U_j(n+\mathbf e_i)U_i(n+\mathbf e_j)^{-1}U_j(n)^{-1}
\right].                                                    \tag{1.1}
\]
Write \(\mathsf E_L,\mathsf P_L\) for these complete sets, and
\[
N=3(2L)(2L+1)^2,\qquad M=3(2L)^2(2L+1).
\]
The Hilbert space is \(\mathcal H_L=L^2(SU(2)^{\mathsf E_L},dU)\),
with product Haar probability measure and inner product conjugate-linear
in its first entry. The differential operators and all physical constants are
\[
T_a=-i\sigma_a/2,\quad
X_{e,a}f=\left.\frac{d}{dt}f(\ldots,e^{tT_a}U_e,\ldots)\right|_{t=0},
\quad E_e=-\sum_{a=1}^3X_{e,a}^2,
\]
\[
H=\kappa\sum_{e\in\mathsf E_L}E_e
       +b\sum_{p\in\mathsf P_L}(2-W_p),\qquad
\kappa=\frac{2g_{\rm YM}^2}{a},\quad
b=\frac{1}{2g_{\rm YM}^2a},\quad
\xi=\frac b\kappa=\frac1{4g_{\rm YM}^4},\quad a,g_{\rm YM}>0.       \tag{1.2}
\]
In the original metric \(c(X,Y)=-\operatorname{tr}(XY)/2\), the
orthonormal frame is \(2T_a\), so \(\Delta_e^c=4\Delta_e^T\).
Thus the electric term in (1.2) also equals
\(-g_{\rm YM}^2\sum_e\Delta_e^c/(2a)\). No coefficient or energy
origin is changed. In particular the scalar \(2bM\) remains in \(H\).

The original geometric condition remains
\[
\operatorname{Im}\tau
\left(\operatorname{Im}\beta-
\frac{6(\operatorname{Im}\mu)^2}{\operatorname{Im}\tau}\right)\ne0.
                                                               \tag{1.3}
\]
The input magnetic patch uses
\(L_T=\operatorname{Im}\tau_T,\ q_T=-\operatorname{Im}\beta_T,
m_T=\operatorname{Im}\mu_T,\ D=L_Tq_T+6m_T^2>0\) and
\(\theta=2\pi a^2/D\). Its exact projected small-angle state, proved
in the parent source, is
\[
\chi_\theta=-\frac23\theta^2 v_{w^{\rm nat}}+O_{H^1}(\theta^4),
\qquad w^{\rm nat}_{(n,1)}=n_2^2,\quad
w^{\rm nat}_{(n,2)}=w^{\rm nat}_{(n,3)}=0.                         \tag{1.4}
\]
The angle remainder in (1.4) is a fixed-regulator input, not a bound
claimed uniform here. The result below concerns its actual electric
state with the exact original weights.

The product Laplacian on this compact connected manifold has domain
\(H^2\), form domain \(H^1\), and compact resolvent. Its smooth bounded
potential preserves these domains. A lowest form minimizer can be
chosen nonnegative by the gradient inequality for the modulus, obtained
at its zeros by approximation with \(\sqrt{|f|^2+\epsilon^2}\).
Elliptic regularity and the strong maximum principle make it smooth and
strictly positive. Write it as \(\psi>0\), with
\(\int\psi^2dU=1\), and write its physical energy as \(\mathcal E\).
Integration by parts using \(H\psi=\mathcal E\psi\) gives
\[
\mathfrak q_{H-\mathcal E}[\psi F]
 =\kappa\sum_{e,a}\int\psi^2|X_{e,a}F|^2dU.                    \tag{1.5}
\]
A second ground eigenfunction divided by \(\psi\) would have all
derivatives zero in (1.5), hence be constant. This proves simplicity.
The gauge action \(U_e\mapsto g_{s(e)}U_eg_{t(e)}^{-1}\) preserves
the operator, form, and positive unit vector; consequently \(\psi\)
is gauge invariant. All states below are formed from this same vacuum.

For each link set
\[
r_e=\#\{p:e\in\partial p\},\quad
W_e^{\star}=\sum_{p\ni e}W_p,\quad
t_{ef}=\#\{p:e,f\in\partial p\},\quad
\gamma_e=\langle\psi,E_e\psi\rangle,\quad v_e=(E_e-\gamma_e)\psi.
\]
Here \(2\le r_e\le4\), including boundary links. Define the actual matrices
\[
C_{ef}=\langle v_e,v_f\rangle,\qquad
\mathcal N_{ef}=\langle v_e,(H-\mathcal E)v_f\rangle.             \tag{1.6}
\]
They are real symmetric positive-semidefinite matrices. Smoothness of
\(\psi\) supplies every operator and form domain used in (1.6).



# 10. A uniform score bound and coercivity of the actual conditional operator

The full vacuum equation also controls the conditional density without a
small-coupling expansion. This gives a second volume-independent estimate
useful in the exact elimination construction. It does not presuppose a
spectral gap for the full interacting system.

Use the product Riemannian metric for which the three \(T_a\) fields at
each link are orthonormal; write \(\nabla_e,\Delta_e\) for its link
gradient and Laplacian, and \(\Delta=\sum_e\Delta_e=-\sum_eE_e\).
This is precisely the metric already used in (1.2), not a new physical
metric. In quaternion coordinates \(U=u_0I+i\sum_a u_a\sigma_a\), its
metric is four times the metric of the unit three-sphere: the tangent
vector \(T_a\) at the identity has quaternion Euclidean length \(1/2\),
while its specified Riemannian length is 1. Left multiplication is
orthogonal on quaternions, so this identity holds at every point.
Consequently a link factor is isometric to the round sphere of radius 2.
Its sectional curvature is \(1/4\), Ricci tensor is \(g/2\), and diameter
is \(2\pi\). The curvature coefficient also follows from the second
fundamental form of the radius-2 sphere: its normal derivative has
magnitude \(1/2\), the Gauss equation gives sectional curvature \(1/4\),
and summing the two transverse sectional curvatures gives \(1/2\).
These computations retain the factor four relative to \(c\).

Put \(u=\log\psi\), a globally smooth real function because \(\psi>0\).
Dividing the eigen-equation by the same positive \(\psi\), with its
original unit norm left unchanged, yields the exact nonlinear equation
\[
\Delta u+|\nabla u|^2=\frac{V-\mathcal E}{\kappa},
\qquad V=b\sum_{p\in\mathsf P_L}(2-W_p).                         \tag{10.1}
\]
For each fixed link \(e\) define \(w_e=|\nabla_eu|^2\), and let
\(\nabla_f\nabla_eu\) denote the covariant derivative, in factor \(f\),
of the factor-\(e\) gradient. On the product manifold the partial
Bochner identity is
\[
\Delta w_e
=2\sum_f|\nabla_f\nabla_eu|_{\rm HS}^2
 +2\langle\nabla_eu,\nabla_e\Delta u\rangle+w_e.                  \tag{10.2}
\]
Here is its coordinate derivation. Take orthonormal geodesic frames
in every factor at the point under consideration. Applying each
second derivative in \(\Delta_f\) to the sum of squares of the three
components of \(\nabla_eu\) gives twice their squared first derivatives
plus twice their contraction with the second derivative of the vector.
For \(f\ne e\), the product connection has zero mixed curvature, so that
second derivative commutes with \(\nabla_e\). For \(f=e\), commuting
the covariant derivatives of the differential \(du\) gives
\[
\Delta_e^{\rm rough}\nabla_eu
=\nabla_e\Delta_eu+\operatorname{Ric}_e(\nabla_eu).
\]
This sign can equally be read from the positive sectional-curvature
Gauss formula above. The Ricci contraction in the differentiated norm
is \(2\operatorname{Ric}_e(\nabla_eu,\nabla_eu)=w_e\).
Adding the factor equations proves (10.2).
The scalar smooth Bochner identity, with the same sign of \(\Delta\),
is given in C. Villani, *Optimal Transport: Old and New*, Chapter 14,
equation (14.28), printed p.388 (PDF p.394 in the indexed local edition).
The partial-factor and vacuum substitutions used here are calculated
explicitly, rather than inferred from a dimension-independent constant
not stated there.

Let \(\mathcal D_u=\Delta+2\langle\nabla u,\nabla\,\cdot\,\rangle\).
Differentiating (10.1) and using the symmetry of the full Hessian gives
\[
\mathcal D_u w_e
=2\sum_f|\nabla_f\nabla_eu|_{\rm HS}^2+w_e
 +\frac2\kappa\langle\nabla_eu,\nabla_eV\rangle.                 \tag{10.3}
\]
In detail, the derivative of \(|\nabla u|^2\) in factor \(e\)
is \(2(\nabla^2u\,\nabla u)_e\). Its contraction with \(2\nabla_eu\)
in (10.2) is minus \(4\nabla^2u(\nabla u,\nabla_eu)\).
The drift applied to \(w_e\) is plus that same quantity. This proves
the cancellation with every mixed factor \(f\) included.

**Theorem 10.1.** For all \(L\ge2\), \(a,g_{\rm YM}>0\), and each link,
\[
\|\nabla_e\log\psi\|_\infty\le2r_e\xi,\qquad
\|\nabla_e\log\rho\|_\infty\le4r_e\xi,\qquad \rho=\psi^2.        \tag{10.4}
\]
In particular
\[
0\le\gamma_e\le4r_e^2\xi^2.                                   \tag{10.5}
\]
This improves the constant in the earlier valid bound (3.1).
All estimates (4.1)--(8.2) remain valid with their displayed constants.

**Proof.** Equation (6.2) gives \(|\nabla_eW_p|\le1\) for every
face at \(e\), and all other face derivatives vanish. Thus
\(|\nabla_eV|\le br_e\), without any factor \(M\).
The smooth nonnegative function \(w_e\) attains its maximum on the
compact product. At that point its full gradient vanishes and
\(\Delta w_e\le0\). Equation (10.3) therefore gives
\[
0\ge w_e-2r_e\xi\sqrt{w_e}.
\]
If the maximum is zero the conclusion is immediate. Otherwise dividing
by its positive square root gives \(\sqrt{w_e}\le2r_e\xi\).
This proves the first bound everywhere. Since \(\log\rho=2u\), the
second follows with its exact factor two. Finally integration by parts
gives
\(\gamma_e=\int|\nabla_e\psi|^2dU=\int\rho|\nabla_eu|^2dU\);
its probability integral and (10.4) prove (10.5). \(\square\)

To apply this to the actual conditional operator, fix a nonempty set
\(S\) of eliminated links and write \(r=U_{S^c}\), \(s=U_S\). Define
\[
\rho_{S^c}(r)=\int\rho(s,r)\,ds,\qquad
p_S(s\mid r)=\frac{\rho(s,r)}{\rho_{S^c}(r)},\qquad
\omega_S=8\pi\xi\sum_{e\in S}r_e.                              \tag{10.6}
\]
These are the marginal and conditional density of the same vacuum,
not a postulated Wilson Gibbs density. Holding \(r\) fixed and joining
two \(S\)-configurations one link at a time by minimizing geodesics,
(10.4) and the diameter \(2\pi\) give
\[
\sup_s\log p_S(s\mid r)-\inf_s\log p_S(s\mid r)\le\omega_S.      \tag{10.7}
\]
The denominator in (10.6) cancels from this oscillation. No differentiability
or uniform limit of the exterior marginal is assumed.

The product Haar Poincare inequality on \(S\), with its exact
single-link spectral coefficient, is
\[
\inf_{c\in\mathbb C}\int|F-c|^2ds
\le\frac43\sum_{e\in S}\int|\nabla_eF|^2ds.                     \tag{10.8}
\]
To prove it, expand \(F\) in the complete product matrix-coefficient
basis used in Section 2. Removing the constant leaves at least one
nonzero spin, so its total electric eigenvalue is at least \(3/4\).
Parseval gives (10.8) first for finite sums and then by form closure
for every \(H^1\) function.
For each exterior \(r\), let \(p_{\max},p_{\min}\) be the maximum
and minimum of its smooth positive conditional density on \(S\).
Minimize over \(c\), first bound the density above, apply (10.8), and
then bound it below in the energy integral. This gives the full
comparison calculation
\[
\begin{split}
\operatorname{Var}_{p_S(\cdot\mid r)}(F)
&\le p_{\max}\inf_c\int|F-c|^2ds\\
&\le\frac{4p_{\max}}3\sum_{e\in S}\int|\nabla_eF|^2ds\\
&\le\frac43 e^{\omega_S}
       \sum_{e\in S}\int|\nabla_eF|^2p_S(s\mid r)\,ds .
\end{split}                                                   \tag{10.9}
\]
The minimum characterization of variance is valid for complex functions
as well, with the complex mean as minimizer. This proof records the
entire density ratio; it is the bounded-density perturbation argument,
not a replacement of either measure.

Let \(\mathscr H_\rho=L^2(\rho\,dU)\), and define the exact isometry
\[
J_S:L^2(\rho_{S^c}\,dr)\longrightarrow\mathscr H_\rho,\qquad
(J_SF)(s,r)=F(r).
\]
Its adjoint is
\[
(J_S^*G)(r)=\int G(s,r)p_S(s\mid r)\,ds.
\]
Fubini verifies the inner-product identity for the adjoint and
\(J_S^*J_S=I\). Thus
\(P_S^\rho=J_SJ_S^*\) and \(Q_S^\rho=I-P_S^\rho\) are
orthogonal projections; \(\mathscr K_S^\rho=\ker J_S^*\)
is the conditional-mean-zero space. The multiplication map
\(U_\psi:G\mapsto\psi G\) is a unitary \(\mathscr H_\rho\to\mathcal H_L\).
The exact ground-state transform and its closed form are
\[
\mathscr L_\rho=U_\psi^{-1}(H-\mathcal E)U_\psi
 =-\kappa(\Delta+\langle\nabla\log\rho,\nabla\,\cdot\,\rangle),
\qquad
q_\rho[G]=\kappa\sum_e\int|\nabla_eG|^2\rho\,dU.                 \tag{10.10}
\]
At each fixed box the density and its reciprocal are smooth and bounded
on a compact space. Differentiating the conditional integral shows that
\(P_S^\rho,Q_S^\rho\) preserve \(H^1\): a retained derivative gives the
conditional integral of the input derivative and a bounded smooth
derivative of the conditional kernel; an eliminated derivative of the
output is zero. The constants in this domain-preservation statement
need not be uniform, and are not used for the coercivity bound below.
Applying \(Q_S^\rho\) to smooth \(H^1\) approximants proves that
\(H^1\cap\mathscr K_S^\rho\) is the form closure of its smooth elements
and dense in \(\mathscr K_S^\rho\).

Define \(C_S^\rho\) as the self-adjoint operator of the restricted
closed form \(q_\rho|_{H^1\cap\mathscr K_S^\rho}\). Explicitly its
domain consists of those \(G\) in that form space for which there is
\(h\in\mathscr K_S^\rho\) satisfying
\(q_\rho(F,G)=\langle F,h\rangle_\rho\) for every \(F\) in the form
space, and \(C_S^\rho G=h\). This definition makes no unproved claim
about the domain of a formal operator product.

**Theorem 10.2.** For every positive coupling and every finite box,
\[
C_S^\rho\ge\frac{3\kappa}{4}e^{-\omega_S}I,\qquad
\|(C_S^\rho)^{-1}\|\le\frac4{3\kappa}e^{\omega_S}.              \tag{10.11}
\]
In particular for a single eliminated link \(e\),
\[
C_{\{e\}}^\rho\ge\frac{3\kappa}{4}e^{-8\pi r_e\xi}I
\ge\frac{3\kappa}{4}e^{-32\pi\xi}I.                            \tag{10.12}
\]
These single-link bounds are independent of all exterior volume and
valid for the actual interacting conditional density.

**Proof.** A vector \(G\in\mathscr K_S^\rho\) has zero conditional
mean for almost every \(r\). Apply (10.9) to its conditional slices
and multiply by \(\rho_{S^c}(r)\); integrate in \(r\). Fubini gives
\[
\|G\|_\rho^2\le\frac43 e^{\omega_S}
       \sum_{e\in S}\int|\nabla_eG|^2\rho\,dU
\le\frac4{3\kappa}e^{\omega_S}q_\rho[G].
\]
Smooth approximation extends this inequality to the entire restricted
form domain. The form representation and spectral theorem yield
(10.11); \(r_e\le4\) gives (10.12).
The unitary \(U_\psi\) carries this form onto the full physical
excitation form restricted to \(U_\psi\mathscr K_S^\rho\), so the
constant has not been transferred between different operators without
a domain map. Gauge transformations preserve the density and intertwine
conditional integration by endpoint Haar invariance. Consequently these
projections, forms, and inverses preserve the physical gauge-invariant
subspaces as well. \(\square\)

For comparison with the original parameters, the last bound in (10.12) is
\[
\frac{3g_{\rm YM}^2}{2a}
       \exp\!\left(-\frac{8\pi}{g_{\rm YM}^4}\right).
\]
For larger eliminated sets the bound is also explicit, but its dependence
on \(\sum_{e\in S}r_e\) is retained. No volume-independent extensive-block
bound is inferred by deleting that sum.
Nor does a uniform conditional one-link gap alone tensorize into a
uniform gap for the correlated full density. The proof has established
an inverse for the actual eliminated operator, not a separated-correlation
estimate or the Millennium spectral conclusion.
The full finite-box spectral bound proved in Section 12 uses an
independently convergent cluster construction, not an assumed
tensorization of these conditional inequalities.

The indexed Villani PDF has stable unit ID
\nolinkurl{PUBUNIT-3B56736161C0B49850EA7433}, SHA-256
\nolinkurl{3AE2DB61CBFFADFEEF0DE738742F4F3CE81B21874DACB1AD2991A7000434675D}.
Its contents and the complete printed pp.387--389, including equation
(14.28), were read directly; the book is cited, not copied into this
repository. The page reference is to that exact local edition rather
than an assumed page number in every edition.



# 11. An explicit convergent cluster coordinate construction for the full vacuum

The source method used here is the commuting creation-coordinate construction
in D. A. Yarotsky, *Quasi-particles in weak perturbations of non-interacting
quantum lattice systems*, arXiv:math-ph/0411042v1, Section 2, equations
labelled mmo, c1, vsum, thl and sumj in the retained source TeX
([primary source](https://arxiv.org/abs/math-ph/0411042)).
That section explicitly permits infinite-dimensional single-site spaces
and unbounded on-site operators. Its smallness constants are not numerical.
The following proof derives its own constants for the complete four-link
Wilson interaction. The method is not claimed new. No finite-spin
truncation is made, and no rescaling of the original Hamiltonian or
vacuum is made.

Write
\[
H_0=\kappa\sum_eE_e,\qquad V_p=-bW_p,\qquad
H=H_0+2bM+\sum_pV_p,\qquad \gamma=\frac{3\kappa}{4}.
                                                               \tag{11.1}
\]
Thus \(\|V_p\|\le J:=2b\), each face has \(s=4\) distinct links,
and each link belongs to at most \(d=4\) faces. The scalar \(2bM\)
remains in (11.1) and in the eigenvalue equation below. It commutes with
every coordinate transformation and has zero nonconstant component;
these facts, not deletion of its value, account for its absence from
the nonconstant fixed-point equation.

Let \(\Omega=1\) in the original product Haar probability space. For
\(I\subset\mathsf E_L\), put
\[
\mathcal H'_I=\bigotimes_{e\in I}
       \bigl(L^2(SU(2))\ominus\mathbb C1\bigr),\qquad
\mathcal H'_\varnothing=\mathbb C.
\]
The canonical orthogonal tensor decomposition gives a unitary map
\[
\mathcal T:\bigoplus_{I\subset\mathsf E_L}\mathcal H'_I
 \longrightarrow\mathcal H_L,\qquad
\mathcal T(z)=\sum_I z_I\otimes1_{I^c}.                         \tag{11.2}
\]
Its inverse component \(\Pi_I\) is obtained by Haar integration over
\(I^c\) and application of the nonconstant projection in every link
of \(I\). Product projections prove both inverse identities in (11.2).
For nonempty \(I\), set \(H_I=\kappa\sum_{e\in I}E_e\) on
\(\mathcal H'_I\). The separate nonzero spins prove
\[
H_I\ge\gamma |I|,\qquad
\|H_I^{-1}\|\le(\gamma |I|)^{-1}.                              \tag{11.3}
\]

For \(z_I\in\mathcal H'_I\), define the bounded operator, on the \(I\)
factor and tensored with the exterior identity, by
\[
\widehat z_I f=z_I\langle1_I,f\rangle_{L^2(SU(2)^I)}.
                                                               \tag{11.4}
\]
The inner product is the one fixed in Section 1, so (11.4) is linear
in \(f\). Its norm is \(\|z_I\|\). Integration of any one common
nonconstant link proves
\[
\widehat z_I\widehat y_K=
\begin{cases}
0,&I\cap K\ne\varnothing,\\
\widehat{z_I\otimes y_K},&I\cap K=\varnothing.
\end{cases}                                                   \tag{11.5}
\]
For entangled vectors the same calculation follows by approximation
by finite elementary tensors in \(\mathcal H'_I,\mathcal H'_K\);
operator norms converge by (11.4). In particular all these operators
commute. A product of more than \(N=|\mathsf E_L|\) nonempty
creation operators is zero.

Use the graph whose vertices are physical links and whose distinct
vertices are adjacent precisely when they share a face. For nonempty
\(I\), let \(\ell(I)\) be the smallest number of edges of a connected
subgraph containing \(I\); extra vertices are allowed. The finite
full-box graph is connected. Define
\[
\omega(I)=2^{\ell(I)+1}.
\]
Monotonicity under inclusion holds. For a face support \(p=\partial p\)
the induced graph is a four-vertex clique, so \(\ell(p)=3\) and
\(\omega(p)=16\). If each \(I_j\) meets \(p\), connected minimizing
subgraphs and a tree on \(p\) have connected union. Therefore
\[
\omega\left(p\cup\bigcup_{j=1}^n I_j\right)
 \le16\prod_{j=1}^n\omega(I_j).                               \tag{11.6}
\]
No replacement of physical coordinates is involved in this graph.

Take the Banach space of collections \(z=(z_I)_{I\ne\varnothing}\),
\(z_I\in\operatorname{Dom}(H_I)\), with norm
\[
\|z\|_*=\max_x\sum_{I\ni x}
     \omega(I)\frac{\|H_Iz_I\|}{\gamma}.
                                                               \tag{11.7}
\]
There are finitely many \(I\), and each energy norm is complete by
the bounded inverse in (11.3), so (11.7) is complete. In particular,
writing \(a_I=\omega(I)\|z_I\|\), one has
\[
\sup_x\sum_{I\ni x}|I|a_I\le\|z\|_*,
\qquad
\sum_{I:I\cap p\ne\varnothing}a_I\le s\|z\|_* .                \tag{11.8}
\]
Let \(C(z)=\sum_{I\ne\varnothing}\widehat z_I\).
It is bounded in each finite box. Its exponential and inverse are
the finite polynomials \(e^{C(z)}\) and \(e^{-C(z)}\) by (11.5).
On the full domain of \(H_0\),
\[
[H_0,\widehat z_I]=\widehat{H_Iz_I},\qquad
e^{-C(z)}H_0e^{C(z)}
 =H_0+\sum_{I\ne\varnothing}\widehat{H_Iz_I}.                  \tag{11.9}
\]
To check domains, the exterior part of \(H_0\) commutes with (11.4);
the local part annihilates the Haar bra, and its action on the ket
is \(H_Iz_I\). This first proves the commutator on finite spectral
tensors. Its bounded right-hand side extends it to the full graph
domain by approximation. Thus \(C(z)\), its powers, and both
exponentials preserve that domain. The second commutator in (11.9)
vanishes by (11.5), proving the exact conjugation formula.

The fixed-point map is
\[
\mathcal F(z)_I=-H_I^{-1}\Pi_I
  e^{-C(z)}\left(\sum_pV_p\right)e^{C(z)}\Omega,
       \qquad I\ne\varnothing.                              \tag{11.10}
\]
The projection output is an arbitrary vector of \(\mathcal H'_I\);
(11.3) places \(\mathcal F(z)_I\) in the correct operator domain.
We now bound (11.10), including all clusters, rather than assuming
the convergence estimate quoted in the source.

For a fixed face \(p\), expand
\[
e^{-C(z)}V_pe^{C(z)}
 =\sum_{n\ge0}\frac1{n!}
    [\cdots[[V_p,C(z)],C(z)],\ldots,C(z)].
                                                               \tag{11.11}
\]
Only indices \(I_j\) meeting \(p\) contribute: a creation operator
disjoint from \(p\) commutes with \(V_p\) and with all other creation
operators. Every \(n\)-fold nested commutator expands into \(2^n\)
ordered words. A nonzero word has disjoint creation supports on
each side of \(V_p\). Since they all meet the four-link support of
\(V_p\), there are at most four on either side. Thus (11.11)
actually ends at \(n=8\). Infinite exponential sums used below are
upper bounds for this finite exact polynomial.

There is a dimension-independent bound on the tensor-sector sum of
each word acting on \(\Omega\). Outside \(p\), \(V_p\) acts as
identity. A common outside link of two creation supports annihilates
the word, by integrating a nonconstant factor. Otherwise the outside
excitation set is exactly \((\bigcup_jI_j)\setminus p\).
Only the choice of excited links inside \(p\) varies in the output.
There are at most \(2^s=16\) such orthogonal sectors. Cauchy--Schwarz
and (11.4) give
\[
\sum_K\|\Pi_K(\hbox{word})\Omega\|
 \le2^{s/2}J\prod_{j=1}^n\|z_{I_j}\|
 =4J\prod_{j=1}^n\|z_{I_j}\|.                                \tag{11.12}
\]
The argument is unchanged for entangled creation vectors by the
elementary-tensor approximation already used in (11.5).

Each nonempty output sector \(K\) is contained in
\(p\cup\bigcup_jI_j\). To bound the anchored sum for \(x\in K\),
cover its possibilities by \(x\in p\) and \(x\in I_j\).
For the first possibility there are at most \(d\) choices of \(p\);
(11.8) bounds each remaining index sum by \(sR\), where
\(R=\|z\|_*\). For the second, choose \(j\), then \(I_j\ni x\).
At most \(d|I_j|\) faces meet that set; the first inequality in
(11.8) absorbs this full factor \(|I_j|\). Thus the respective
anchored bounds for the product sums are
\[
d(sR)^n,\qquad ndR(sR)^{n-1}.                                \tag{11.13}
\]
The second quantity is zero for \(n=0\).
Combining (11.6), (11.10)--(11.13), and the exact cancellation of
\(H_I\) against its inverse yields
\[
\|\mathcal F(z)\|_*
\le\frac{4Jd\,16}{\gamma}
 \sum_{n\ge0}\frac{2^n}{n!}
       \bigl[(sR)^n+nR(sR)^{n-1}\bigr]
=\frac{2048}{3}\xi(1+2R)e^{8R}.                              \tag{11.14}
\]
This anchor counting, rather than the norm of the full perturbation,
removes the factor \(M\).

For two collections in a ball of radius \(R\), telescope each
multilinear word in (11.11), inserting their difference in one
position at a time. The counting (11.13) holds with the norm of that
difference in its position, whether the anchor is there or elsewhere.
For the homogeneous degree-\(n\) bound this multiplies its coefficient
by \(nR^{n-1}\) instead of \(R^n\). Differentiating the positive
majorant series in (11.14) proves
\[
\|\mathcal F(z)-\mathcal F(y)\|_*
 \le\frac{2048}{3}\xi(10+16R)e^{8R}\|z-y\|_* .                \tag{11.15}
\]
This is a bound on the exact finite commutator map, not on a
truncated approximation to the vacuum.

Set \(R_*=1/16\). Since
\(\sum_{n\ge0}(1/2)^n/n!<\sum_{n\ge0}(1/2)^n=2\), (11.14)--(11.15)
give, on the explicit nonempty interval
\[
0<\xi\le\frac1{49152},                                      \tag{11.16}
\]
\[
\|\mathcal F(z)\|_*\le1536\xi\le\frac1{32}<R_*,
\qquad
\operatorname{Lip}(\mathcal F)\le\frac{45056}{3}\xi
 \le\frac{11}{36}<1.                                       \tag{11.17}
\]
Iteration from zero therefore converges in the complete ball to a
unique fixed point \(z\). More explicitly, successive increments
are bounded by a geometric series of ratio \(11/36\); the limit
solves (11.10) by continuity, and applying (11.15) to two fixed
points proves uniqueness. Complex conjugation preserves the real
Wilson potential, the Haar projections and the inverses \(H_I^{-1}\).
It commutes with the iteration, so \(z\), \(e^{C(z)}\Omega\), and
the eigenvalue below are real.

Equations (11.9)--(11.10) show that
\[
\phi=e^{C(z)}\Omega,\qquad
H\phi=\varepsilon\phi,\qquad
\varepsilon=2bM+
 \Pi_\varnothing e^{-C(z)}\left(\sum_pV_p\right)e^{C(z)}\Omega.
                                                               \tag{11.18}
\]
Every nonempty creation product has zero Haar integral, hence
\(\langle\Omega,\phi\rangle=1\), so \(\phi\ne0\).
The next section proves that \(\varepsilon=\mathcal E\), and identifies
the exact scalar relating \(\phi\) to the unchanged physical unit
vacuum. No equality of these differently specified vectors is presumed.



# 12. Uniform full spectral estimate and the extensive electric covariance

In this section (11.16) holds. Fix its constructed \(z\) and abbreviate
\(C=C(z)\). The bounded invertible similarity
\[
\widetilde H=e^{-C}(H-\varepsilon)e^C=H_0+\mathcal K,\qquad
\widetilde H\Omega=0                                       \tag{12.1}
\]
has the full domain of \(H_0\), by (11.9).
It is not asserted unitary. Both similarities and the exact physical
Hamiltonian, including its ground energy, remain explicit.

Give the finite orthogonal sector decomposition the additional norm
\[
\|f\|_{\oplus,1}=\sum_I\|\Pi_If\|,\qquad
\|f\|\le\|f\|_{\oplus,1}\le2^{N/2}\|f\|.                     \tag{12.2}
\]
The second inequality is Cauchy--Schwarz over all \(2^N\) sectors.
Thus the norm has exactly the same vectors and topology in each
fixed box. The equivalence constant depends on volume; no uniform
claim about that equivalence is used.

For \(u_I\in\operatorname{Dom}(H_I)\), (11.5), (11.9), (12.1)
and \(\widetilde H\Omega=0\) give exactly
\[
\mathcal K\,\widehat u_I\Omega
=e^{-C}\left[\sum_pV_p,\widehat u_I\right]e^C\Omega .
                                                               \tag{12.3}
\]
In detail, commute \(\widetilde H\) with \(\widehat u_I\);
the \(H_0\) commutator supplies \(H_Iu_I\), while the creation
sum in (11.9) commutes with \(\widehat u_I\). For the remaining
term, \(e^C\) commutes with \(\widehat u_I\), proving (12.3).
Faces disjoint from \(I\) have zero commutator, so at most
\(d|I|\) faces remain.

Expand each remaining conjugation as in (11.11). All additional
creation indices still have to meet \(p\): the derivation identity
and commutation with \(\widehat u_I\) allow the nested commutators
to be written as the commutator with \(\widehat u_I\) of the
corresponding conjugated \(V_p\).
The output outside \(p\) now has the fixed excited support
\((I\cup\bigcup_jI_j)\setminus p\), or the word vanishes.
Thus (11.12) applies with an extra factor \(\|u_I\|\).
The commutator with \(\widehat u_I\) contributes two words.
Using \(\sum_{K:K\cap p\ne\varnothing}\|z_K\|\le sR_*\) gives
\[
\|\mathcal K\widehat u_I\Omega\|_{\oplus,1}
\le 8Jd\,|I|\,e^{8R_*}\|u_I\|.
                                                               \tag{12.4}
\]
The bound also applies to the empty component with value zero.
Summing (12.4) and using (11.3) proves the relative operator bound
\[
\|\mathcal Kf\|_{\oplus,1}
\le c_\xi\|H_0f\|_{\oplus,1},\qquad
c_\xi=\frac{512}{3}\xi\le\frac1{288}<1,
       \quad f\in\operatorname{Dom}(H_0).                    \tag{12.5}
\]
Indeed \(8Jd/\gamma=256\xi/3\), and \(e^{8R_*}=e^{1/2}<2\).
The bound on finite spectral tensors extends in the graph norm;
all factors in (12.3) preserve the required domain as proved above.

Here is the resolvent argument with no appeal to a missing uniform
perturbation theorem. On every nonempty sector \(I\),
\(\operatorname{Spec}(H_I)\subset[\gamma|I|,\infty)\).
For real \(t<0\), functional calculus gives
\[
\|\mathcal K(H_0-t)^{-1}\|_{\oplus,1}
 \le c_\xi\sup_{\lambda\ge\gamma}
          \frac{\lambda}{\lambda-t}\le c_\xi<1.
\]
For \(0<t<(1-c_\xi)\gamma\), it gives instead
\[
\|\mathcal K(H_0-t)^{-1}\|_{\oplus,1}
 \le\frac{c_\xi\gamma}{\gamma-t}<1.                           \tag{12.6}
\]
The empty sector causes no term because \(\mathcal K\Omega=0\).
The geometric Neumann series for
\((I+\mathcal K(H_0-t)^{-1})^{-1}\), followed by
\((H_0-t)^{-1}\), is a bounded inverse of \(\widetilde H-t\).
The domain is verified by the resolvent's graph-domain image.
Norm equivalence (12.2) makes it also a bounded inverse in the
original Hilbert space, without changing the numerical spectral
exclusion (12.6). Similarity (12.1) transfers this inverse to
\(H-\varepsilon-t\).

The original \(H\) is self-adjoint, \(\varepsilon\) is its real
eigenvalue, and no spectrum lies below it by the \(t<0\) argument.
Thus \(\varepsilon=\mathcal E\). Its simple positive ground vector
was proved in Section 1. The exact identification is therefore
\[
\psi=\alpha e^C\Omega,\qquad
\alpha=\langle\Omega,\psi\rangle>0,\qquad
\alpha^2\|e^C\Omega\|^2=1.                                  \tag{12.7}
\]
This records the physical scalar and preserves the original unit
vacuum rather than replacing it with a coefficient-normalized vector.
The spectrum above it obeys the explicit volume-independent estimate
\[
(H-\mathcal E)\big|_{\psi^\perp}
 \ge\gamma(1-c_\xi)I
 =\frac{3\kappa}{4}\left(1-\frac{512}{3}\xi\right)I
 \ge\frac{287\kappa}{384}I .                                \tag{12.8}
\]
This follows from (12.6) and the spectral theorem, since the ground
eigenvalue is simple. Restricting the same inequality to the
gauge-invariant subspace retains it, because that closed subspace
reduces \(H\) and contains \(\psi\).
Section 15 proves that the cluster similarity itself intertwines this
constraint. Its restricted free threshold is exactly \(3\kappa\), so
(15.13) improves the physical restriction of (12.8), not the full-space
inequality or the numerical fixed-point constants.
In original parameters its range and last lower bound are
\[
g_{\rm YM}^4\ge12288,\qquad
\frac{287g_{\rm YM}^2}{192a}.
                                                               \tag{12.9}
\]
This is a strong-coupling, fixed-spatial-regulator theorem for the
full interacting finite boxes. No spatial continuum limit or
Millennium conclusion follows by deleting its coupling range.

The spectral estimate has an immediate quantitative consequence for
the previously unresolved extensive covariance upper bound.
Every \(v_w\) in Section 7 is perpendicular to \(\psi\), so the
spectral theorem and (12.8) imply
\[
\|v_w\|^2\le
\frac{4}{3\kappa(1-c_\xi)}\,\mathfrak q_{H-\mathcal E}[v_w].
\]
Combining this with the already proved all-weight estimate (7.2)
gives, for every real weight vector and every box,
\[
0\le w^TCw\le
\frac{\xi^2\|\mathsf Iw\|_2^2/4
             +468000\xi^3\|w\|_2^2}{1-512\xi/3}.
                                                               \tag{12.10}
\]
The norm of \(\mathsf I\) is at most 4: on each face,
\((\sum_{e\in\partial p}w_e)^2\le4\sum_{e\in\partial p}w_e^2\);
summing faces and retaining \(r_e\le4\) proves
\(\|\mathsf Iw\|_2^2\le16\|w\|_2^2\).
Consequently the fully extensive matrix upper bound is
\[
0\le C\le
\frac{4\xi^2+468000\xi^3}{1-512\xi/3}\,I_{\mathbb R^{\mathsf E_L}}.
                                                               \tag{12.11}
\]
This removes the \(\ell^1\)-squared volume loss from an upper bound
on the exact covariance. This argument alone does not assert the entrywise absolute
row summability of \(C\), or an \(\ell^2\) remainder of order
\(\xi^3\) around \(\xi^2\mathsf I^T\mathsf I/16\).
Positive-semidefinite order and absolute-value entry sums are not
interchanged.
Sections 13--14 prove the separate absolute-row and two-sided claims by
an explicit locality and spectral-filter calculation.

For the original native weights the exact substitution is
\[
\|v_{w^{\rm nat}}\|^2\le
\frac{\xi^2\mathcal A_L+468000\xi^3S_{2,L}}{1-512\xi/3}.
                                                               \tag{12.12}
\]
Using \(S_{2,L}\le2\mathcal A_L\), proved in Section 8, yields
\[
\|v_{w^{\rm nat}}\|^2\le
\xi^2\mathcal A_L
\frac{1+936000\xi}{1-512\xi/3}.
                                                               \tag{12.13}
\]
Unlike (8.1), this upper control has no \(L^3\) relative loss.
Equation (8.1) remains a valid two-sided remainder with its original
constants; (12.13) supplies a different, stronger extensive upper
control on the nonempty range (11.16).
On the entire leading kernel \(\mathsf Iw=0\), (12.10) also yields
\[
\|v_w\|^2\le\frac{468000\xi^3}{1-512\xi/3}\|w\|_2^2.
                                                               \tag{12.14}
\]
This complements, and does not discard, the fourth-order
\(\ell^1\)-weighted bound (7.3) and the parent's exact fourth-order
calculation. The upper bounds (12.10)--(12.14) alone do not give
a two-sided estimate for the minimum over all signed actual states.
The uniform minimum, as opposed to every individual signed quotient,
is obtained in (15.21) by the gauge-restricted spectral argument.
Equations (15.15)--(15.17) also strengthen these PSD upper bounds by a
factor of four. The original fourth-order kernel coefficients are
retained; (16.21) supplies their uniform covariance and energy remainders.

Finally the same result improves exact extensive elimination, not only
the electric variational family. For every nonempty eliminated set
\(S\), a vector \(G\in\ker J_S^*\) satisfies
\[
\int G\rho\,dU=\int (J_S^*G)(r)\rho_{S^c}(r)\,dr=0.
\]
Thus \(U_\psi G=\psi G\) is perpendicular to the actual ground
vector. Apply (12.8) to its form and use (10.10), first on smooth
vectors and then by the proved form closure. This yields
\[
C_S^\rho\ge\frac{3\kappa}{4}(1-512\xi/3)I
 \ge\frac{287\kappa}{384}I
 \quad\left(0<\xi\le\frac1{49152}\right),                    \tag{12.15}
\]
\[
\|(C_S^\rho)^{-1}\|
 \le\frac{4}{3\kappa(1-512\xi/3)}
 \le\frac{384}{287\kappa}.                                  \tag{12.16}
\]
Every constant in (12.15)--(12.16) is independent of the size,
shape and location of \(S\), as well as the exterior volume.
The operator is precisely the restricted full form \(C_S^\rho\)
defined in Section 10, containing derivatives in all link directions.
It is not replaced by a conditional-fibre differential operator
containing only eliminated derivatives. The all-positive-coupling
bound (10.11) remains available outside (11.16). On their common
range both lower bounds hold, so the larger of the two constants
may be used. The unitary and gauge maps remain exactly those
proved in Section 10.

For the reducing gauge-invariant conditional-complement space,
(15.22)--(15.23) prove the sharper inverse constant \(96/(287\kappa)\).
The projection and unitary supplying that restriction are explicit.



# 15. The gauge-restricted threshold and the full signed electric minimum

The physical constraint improves the full-space estimate (12.8) by a
factor of four, without changing the interaction or the interval (11.16).
We prove the gauge maps, the free threshold, and the restricted resolvent
before using the improvement for the actual interacting states.

The literature source for the finite-graph gauge Hilbert space and its
vertex-invariant representation is John C. Baez, *Spin Network States in
Gauge Theory*, arXiv:gr-qc/9411007v1, the section *Gauge Theory on a
Graph*, Lemmas 1, 2, and the lemma labelled lem2.5 in the original TeX
([primary source](https://arxiv.org/abs/gr-qc/9411007v1);
*Advances in Mathematics* 117 (1996), 253--272,
DOI 10.1006/aima.1996.0012). The retained source is
\nolinkurl{literature/Baez-spin-network-states.tex}, lines 174--321.
The source constructs the invariant Hilbert space from edge
representations and vertex intertwiners. The leaf argument below proves
the particular free spectral bound directly, including the original
open boundary and every endpoint gauge transformation.

## 15.1. Exact gauge projection, source convention, and support sectors

Retain the entire vertex set and define
\[
\mathcal G_L=SU(2)^{\mathsf V_L},\qquad
(\alpha_gU)_e=g_{s(e)}U_eg_{t(e)}^{-1},\qquad
(\mathsf T_g f)(U)=f(\alpha_{g^{-1}}U).                       \tag{15.1}
\]
There is no restriction of \(g_v\) to the identity at boundary vertices
and no external charged representation at a vertex. These are precisely
the gauge transformations of Section 1. Group multiplication gives
\(\alpha_g\alpha_h=\alpha_{gh}\), hence
\(\mathsf T_g\mathsf T_h=\mathsf T_{gh}\).
Left and right Haar invariance on each link prove
\(\|\mathsf T_g f\|=\|f\|\) and
\(\mathsf T_g^*=\mathsf T_{g^{-1}}\).
Translations of continuous functions are continuous in \(g\), and
density extends this to strong continuity on \(\mathcal H_L\).
Thus the strong Haar integral
\[
\mathsf P_{\mathcal G}=\int_{\mathcal G_L}\mathsf T_g\,dg,
\qquad
\mathcal H_{\mathrm{phys}}
 =\{f:\mathsf T_gf=f\text{ for every }g\}
 =\operatorname{Ran}\mathsf P_{\mathcal G}                    \tag{15.2}
\]
exists and is bounded. Haar invariance gives
\(\mathsf T_h\mathsf P_{\mathcal G}=\mathsf P_{\mathcal G}\);
inversion invariance gives
\(\mathsf P_{\mathcal G}^*=\mathsf P_{\mathcal G}\).
Integrating the first identity proves
\(\mathsf P_{\mathcal G}^2=\mathsf P_{\mathcal G}\).
Conversely the integral fixes every invariant vector, proving both
range identities in (15.2).

Baez uses the coordinate action
\(A_e\mapsto g_{t(e)}A_eg_{s(e)}^{-1}\).
The exact dictionary, on the same directed graph, is
\[
\jmath:SU(2)^{\mathsf E_L}\longrightarrow SU(2)^{\mathsf E_L},
\qquad
A_e=\jmath(U)_e=U_e^{-1},\qquad \jmath^{-1}=\jmath.             \tag{15.3}
\]
Indeed \((g_sU_eg_t^{-1})^{-1}=g_tU_e^{-1}g_s^{-1}\).
The pullback \(\mathsf Jf=f\circ\jmath\), from the source's Haar
Hilbert space to ours, is therefore a unitary intertwiner with
inverse the same pullback. Haar measure is invariant under inversion.
Inversion is an isometry for the bi-invariant metric with the
\(T_a\) frame of (1.2), so it preserves the Sobolev domains and
intertwines every \(E_e\). This proves the gauge-space dictionary;
it does not silently reverse a Wilson traversal in (1.1).

Each \(\mathsf T_g\) is a product of link isometries, so it preserves
\(H^1,H^2\) and commutes with \(E_e\) on its operator domain.
In (1.1) the endpoint factors cancel at the four consecutive vertices,
leaving conjugation by \(g_n\) inside the trace. Thus every \(W_p\),
and consequently \(H,H_0,V_p\), is gauge invariant on its stated
domain. The gauge projection also preserves these domains, by
integrating in the corresponding graph norm.

Let \(P_e\) be Haar averaging in the one link \(e\), followed by the
constant lift. Endpoint Haar invariance gives
\(P_e\mathsf T_g=\mathsf T_gP_e\). In Section 11 notation,
the embedded sector projection is exactly
\[
\mathsf Q_I=
 \prod_{e\in I}(I-P_e)\prod_{f\notin I}P_f,
\qquad
\mathsf Q_If=(\Pi_If)\otimes1_{I^c}.                         \tag{15.4}
\]
Products commute, so \(\mathsf Q_I\) commutes with the gauge
representation and with \(\mathsf P_{\mathcal G}\).
The finite sum of all \(\mathsf Q_I\) is the identity, by expanding
\(\prod_e[(I-P_e)+P_e]\).
Restricting the unitary (11.2) consequently gives the exact
orthogonal decomposition
\[
\mathcal H_{\mathrm{phys}}
 =\bigoplus_{I\subset\mathsf E_L}
     \bigl(\mathcal H'_I\otimes1_{I^c}\bigr)^{\mathcal G_L}.
                                                               \tag{15.5}
\]
The inverse map remains the collection of Haar projections (15.4).
The action on the \(I\) factor is the restriction of the product
link representation, not a gauge group with its boundary removed.

## 15.2. Leaf annihilation and the exact free physical threshold

For a nonempty set \(I\) of links, consider the undirected graph
with these edges and their endpoints. Suppose a vertex \(v\)
has exactly one incident edge \(e\) in \(I\). For
\[
f\in\bigl(\mathcal H'_I\otimes1_{I^c}\bigr)^{\mathcal G_L},
\]
vary only \(g_v\). On the \(I\) factors this translates only the
variable \(U_e\), on the left or the right according to its
original orientation. On the exterior factors it acts on constants.
Since \(f\) is invariant, integration over this single \(SU(2)\)
gauge variable gives
\[
f=\int_{SU(2)}\mathsf T_{g_v}f\,dg_v=P_ef=0.                 \tag{15.6}
\]
The second equality is exactly left or right Haar averaging; the
last equality follows from the \(I-P_e\) factor in (15.4).
For arbitrary, possibly entangled \(L^2\) vectors the identity
follows first on elementary tensors, then by density and the
boundedness of the two averages. Thus no pointwise representative
or unstated smoothness is used in the leaf argument.

It follows that every nonempty support of a nonzero invariant sector
has degree at least two at every one of its incident vertices.
Such a finite graph contains a cycle: choose a simple path of
maximal length; at its last vertex there is a neighbor other than
the preceding vertex. Maximality places that neighbor earlier in
the path, and the resulting segment closes a simple cycle.
The original cubic graph has no loops or multiple edges.
The coloring \(n\mapsto(-1)^{n_1+n_2+n_3}\) changes sign along
every edge, so every cycle has even length. Its length is therefore
at least four. In particular,
\[
\bigl(\mathcal H'_I\otimes1_{I^c}\bigr)^{\mathcal G_L}
 \ne\{0\},\quad I\ne\varnothing
\quad\Longrightarrow\quad |I|\ge4.                          \tag{15.7}
\]
This proof includes vertices on faces, edges, and corners of the
open box. Omitting a boundary gauge transformation would invalidate
the corresponding step (15.6); no such omission has been made.

On a nonempty support (11.3) gives
\(H_I\ge(3\kappa/4)|I|\), on its full domain and hence on its
invariant subspace. Combining (15.5)--(15.7) and summing the
orthogonal nonempty sectors yields the form inequality
\[
H_0\big|_{\mathcal H_{\mathrm{phys}}\cap\Omega^\perp}
 \ge 3\kappa I.                                             \tag{15.8}
\]
The constant is attained. For any elementary face \(p\), its
unchanged \(W_p\) is gauge invariant and is a fundamental
matrix coefficient in each of its four distinct link variables,
including the two inverse traversals. Bi-invariance of the
Casimir gives
\[
E_eW_p=\tfrac34W_p\quad(e\in\partial p),\qquad
E_eW_p=0\quad(e\notin\partial p).
\]
Integration in one participating link, with all others held fixed,
gives \(\int W_p\,dU=0\) and \(\int |W_p|^2dU=1\).
For the latter, the product inside the trace is Haar distributed
under that integral, also for an inverse occurrence, and the
fundamental matrix-coefficient identity
\(\int U_{ij}\overline{U_{k\ell}}\,dU
 =\delta_{ik}\delta_{j\ell}/2\) gives the unit norm of its trace.
Consequently
\[
H_0W_p=3\kappa W_p,\qquad
W_p\in\mathcal H_{\mathrm{phys}}\cap\Omega^\perp,\qquad
\|W_p\|=1.                                                   \tag{15.9}
\]
This proves the exact free physical threshold \(3\kappa\), rather
than merely a lower estimate. No free vector is substituted for
the interacting vacuum in the argument that follows.

## 15.3. Gauge-equivariance of the interacting cluster similarity

The fixed-point construction of Section 11 may be performed within
the invariant sector collections. To prove that statement, assume
each \(z_I\otimes1_{I^c}\) is gauge invariant. The gauge operator
factorizes as \(\mathsf T_{g,I}\otimes\mathsf T_{g,I^c}\).
Both \(z_I\) and \(1_I\) are fixed by the first factor. Hence
the rank-one creation operator (11.4) satisfies
\[
\mathsf T_g\widehat z_I\mathsf T_g^{-1}
 =|\mathsf T_{g,I}z_I\rangle
   \langle\mathsf T_{g,I}1_I|\otimes I_{I^c}
 =\widehat z_I.                                             \tag{15.10}
\]
The projections \(\Pi_I\) intertwine the full representation with
its sector action by (15.4). The operator \(H_I^{-1}\) commutes
with this action by the reducing property and functional calculus.
Since \(V_p\) and \(\Omega\) are invariant, (11.10) therefore sends
invariant collections to invariant collections.

Iteration starts at zero. Every iterate is invariant, and the
limit in the energy norm (11.7) is invariant because fixed
subspaces of bounded representations are closed. Thus the actual
fixed point has the claimed invariance. Its creation sum \(C(z)\)
and the two finite polynomial exponentials commute with
\(\mathsf T_g\) and \(\mathsf P_{\mathcal G}\).
The domain preservation proved in (11.9) also holds upon restriction.
In particular the exact relation remains
\[
\psi=\alpha e^{C(z)}\Omega,\qquad
\alpha=\langle\Omega,\psi\rangle>0,
\]
with the scalar and unit physical vacuum specified in (12.7).

Write \(\widetilde H=H_0+\mathcal K\) as in (12.1).
All three operators preserve the physical subspace; the bounded
invertible similarity and its inverse do as well. The restriction
of the sector norm (12.2) is still equivalent to the Hilbert norm,
with its same explicitly volume-dependent upper comparison.
The relative estimate is unchanged:
\[
\|\mathcal K f\|_{\oplus,1}
 \le c_\xi\|H_0 f\|_{\oplus,1},\qquad
c_\xi=\frac{512}{3}\xi\le\frac1{288},
\quad
f\in\operatorname{Dom}(H_0)\cap\mathcal H_{\mathrm{phys}}.
                                                               \tag{15.11}
\]
We do not replace the per-link bound used to prove this estimate
by a larger value or alter its numerical contraction.

On every nonempty invariant sector, the spectral parameter
\(\lambda\) of \(H_I\) satisfies \(\lambda\ge3\kappa\)
by (15.7). Therefore, for \(0<t<3\kappa(1-c_\xi)\),
\[
\|\mathcal K(H_0-t)^{-1}\|_{\oplus,1;\mathrm{phys}}
 \le c_\xi\sup_{\lambda\ge3\kappa}
               \frac{\lambda}{\lambda-t}
 =\frac{3\kappa c_\xi}{3\kappa-t}<1.                         \tag{15.12}
\]
The constant sector contributes zero because
\(\mathcal K\Omega=0\), exactly as in Section 12.
The Neumann series therefore gives a bounded inverse for
\(\widetilde H-t\) on the physical subspace. Its image is in the
restricted \(H_0\) domain: factor the inverse as
\((H_0-t)^{-1}[I+\mathcal K(H_0-t)^{-1}]^{-1}\).
Norm equivalence and the invariant similarities transfer that
inverse to \(H-\mathcal E-t\) on the original physical Hilbert
space. No form positivity is claimed for the nonunitary similarity
itself. Applying the spectral theorem to the original self-adjoint
restriction, with its simple ground eigenvalue, proves
\[
(H-\mathcal E)\big|_{\mathcal H_{\mathrm{phys}}\cap\psi^\perp}
 \ge 3\kappa\left(1-\frac{512}{3}\xi\right)I
 \ge\frac{287\kappa}{96}I,
\qquad 0<\xi\le\frac1{49152}.                                \tag{15.13}
\]
In original parameters the last constant is
\(287g_{\rm YM}^2/(48a)\) and the range is
\(g_{\rm YM}^4\ge12288\).
The full, not necessarily invariant Hilbert-space bound remains
(12.8), with constant \(287\kappa/384\). The fourfold improvement
is asserted exactly on the physical restriction just proved.

## 15.4. Covariance order, signed states, and an attained uniform minimum

Every \(E_e\) commutes with the gauge representation, so each
centered vector \(v_e\) is in
\(\mathcal H_{\mathrm{phys}}\cap\psi^\perp\).
There is no sign restriction on the coefficients in a real linear
combination. Applying (15.13) to every \(v_w\), including a zero
vector, gives the matrix inequality
\[
\mathcal N\ \ge\
3\kappa(1-c_\xi)C\ \ge\ 0
\quad\hbox{on }\mathbb R^{\mathsf E_L}.                       \tag{15.14}
\]
Combining it with the upper side of (7.2) yields
\[
0\le w^{\mathsf T}Cw
 \le\frac{\xi^2\|\mathsf Iw\|_2^2/16
               +117000\xi^3\|w\|_2^2}{1-512\xi/3}.           \tag{15.15}
\]
Here \(351000/3=117000\); the leading coefficient is \(1/16\).
The exact facewise estimate \(\|\mathsf Iw\|_2^2\le16\|w\|_2^2\)
from Section 12 gives
\[
0\le C\le
\frac{\xi^2+117000\xi^3}{1-512\xi/3}
 I_{\mathbb R^{\mathsf E_L}}.                                \tag{15.16}
\]
On \(\ker\mathsf I\) the numerator of (15.15) is exactly
\(117000\xi^3\|w\|_2^2\). This is an upper bound, not a
fourth-order identification or a discarded null direction.
For the unchanged native weights,
\[
\|v_{w^{\rm nat}}\|^2
 \le\frac{\xi^2\mathcal A_L/4+117000\xi^3 S_{2,L}}
              {1-512\xi/3}
 \le\frac{\xi^2\mathcal A_L}{4}
       \frac{1+936000\xi}{1-512\xi/3}.                       \tag{15.17}
\]
The last step uses \(S_{2,L}\le2\mathcal A_L\), without changing
the coefficients or coordinates in the original state.

To define the signed minimum without dividing by an unproved
denominator, let \(\mathcal H_{\mathrm{phys},\mathbb R}\) denote
the real-valued invariant functions and define
\[
\mathsf V_\xi:\mathbb R^{\mathsf E_L}
 \longrightarrow\mathcal H_{\mathrm{phys},\mathbb R}\cap\psi^\perp,
\qquad
\mathsf V_\xi w=v_w,\qquad
\mathscr W_\xi=\operatorname{Ran}\mathsf V_\xi.               \tag{15.18}
\]
Its Gram identity is
\(\langle\mathsf V_\xi w,\mathsf V_\xi z\rangle=w^{\mathsf T}Cz\).
Thus
\(\ker\mathsf V_\xi=\ker C\): \(Cw=0\) implies zero norm of
\(\mathsf V_\xi w\); conversely a zero vector has zero inner
product with every \(\mathsf V_\xi z\).
The induced map
\[
\overline{\mathsf V}_\xi:
\bigl(\mathbb R^{\mathsf E_L}/\ker C,\,
       \langle[w],[z]\rangle_C=w^{\mathsf T}Cz\bigr)
 \longrightarrow\mathscr W_\xi                              \tag{15.19}
\]
is an isometric linear bijection. The bilinear form is well-defined
because \(C\) annihilates its kernel, and it is positive on every
nonzero equivalence class by the Gram identity.
The inverse sends a vector \(v_w\) to its class \([w]\);
two preimages differ by \(\ker C\), which proves independence of
choice. The same identity for the energy form shows that
\(\mathcal N\) annihilates \(\ker C\) and descends to the quotient.
This records the exact information loss. No equality
\(\ker C=\ker\mathsf I\), or \(\ker C=\{0\}\), is assumed.

On \(0<\xi\le1/680000\), (7.5)--(7.6) give a nonzero
\(v_e\) for every link, so \(\mathscr W_\xi\ne\{0\}\).
It is finite dimensional and consists of smooth vectors.
The energy form is a continuous quadratic form on this finite
dimensional space. Its restriction to the unit sphere attains a
minimum by compactness. Through (15.19) this number is exactly
\[
\mathfrak m_L(\xi)
 =\min_{\substack{w\in\mathbb R^{\mathsf E_L}\\
                  w^{\mathsf T}Cw>0}}
       \frac{w^{\mathsf T}\mathcal N w}{w^{\mathsf T}Cw}.
                                                               \tag{15.20}
\]
Write \(\Delta_{\mathrm{phys},L}(\xi)\) for the first positive
spectral value of \(H-\mathcal E\) on
\(\mathcal H_{\mathrm{phys}}\).
Its existence follows from compact resolvent, the simple ground
eigenvalue, and the nonzero physical excited subspace; this is the
same excitation operator as in (15.13).
The spectral variational principle, (15.14), and the actual
single-link trial bound (7.6) prove the complete chain
\[
\begin{split}
3\kappa-512\kappa\xi
 &=3\kappa(1-c_\xi)\\
 &\le\Delta_{\mathrm{phys},L}(\xi)
 \le\mathfrak m_L(\xi)
 \le3\kappa+2472000\kappa\xi ,
\qquad 0<\xi\le\frac1{680000}.
\end{split}                                                \tag{15.21}
\]
Every \(L\ge2\) is covered by these same constants and coupling
interval. In particular the estimate permits weights that depend
on \(L,\xi\), have arbitrary signs, or lie in \(\ker\mathsf I\),
whenever they represent a nonzero actual state. Such a state is
included in the minimization, not excluded by a leading-coefficient
test. The quotient construction retains all zero actual states as
the explicitly identified kernel, where an energy quotient has no
defined value.

Equation (15.21) proves both uniform statements
\(\Delta_{\mathrm{phys},L}(\xi)=3\kappa+O(\kappa\xi)\) and
\(\mathfrak m_L(\xi)=3\kappa+O(\kappa\xi)\), with the displayed
two-sided constants as their meaning. It does not assert that
every signed state's quotient is near \(3\kappa\).
In particular it does not replace the parent's fixed-box
fourth-order kernel quotient or prove its remainder uniform.
The separate calculation (16.17)--(16.24) supplies that uniform
remainder on the entire original incidence kernel.
The earlier two-sided nonnegative/native estimate (14.7) also
remains valid with its original range.
In physical parameters the range of (15.21) is
\(g_{\rm YM}^4\ge170000\) and its central scale is
\(3\kappa=6g_{\rm YM}^2/a\).
No lattice-spacing limit or coupling continuation is taken.

## 15.5. The physical conditional-complement operator

Retain \(J_S,Q_S^\rho,\mathscr K_S^\rho,U_\psi,q_\rho\) and their
domains from Section 10. Let the gauge group act on
\(\mathscr H_\rho\) by the same pullback (15.1). It is unitary
because \(\rho=\psi^2\) is invariant. The retained-variable space
has the induced endpoint action on its retained links.
Under a simultaneous transformation of \((s,r)\), invariance of
\(\rho(s,r)\) and Haar measure in \(s\) proves invariance of the
marginal \(\rho_{S^c}(r)\). Changing variables in the conditional
integral then gives
\[
J_S^*\mathsf T_g=\mathsf T_{g,S^c}J_S^*,\qquad
\mathsf T_gJ_S=J_S\mathsf T_{g,S^c}.                          \tag{15.22}
\]
It follows that \(Q_S^\rho\) and the gauge projection commute.
They preserve the form domain as proved in Section 10 and by
the isometric gauge action. Averaging smooth approximants over
the compact gauge group and then applying \(Q_S^\rho\) proves
form density of the smooth invariant conditional-mean-zero
vectors in
\[
\mathscr K_{S,\mathrm{phys}}^\rho
 =\mathscr K_S^\rho\cap\mathscr H_\rho^{\mathcal G_L}.
\]
The closed form restricted to
\(H^1\cap\mathscr K_{S,\mathrm{phys}}^\rho\) therefore defines a
self-adjoint operator \(C_{S,\mathrm{phys}}^\rho\) by exactly
the variational domain rule given for \(C_S^\rho\) in Section 10.
Equations (15.22) and invariance of \(q_\rho\) also show that this
is the reducing physical restriction of \(C_S^\rho\).

The exact unitary \(U_\psi G=\psi G\) intertwines the gauge
representations. For a conditional-mean-zero \(G\), Fubini gives
\(\int G\rho\,dU=0\); consequently \(U_\psi G\) is physical and
perpendicular to \(\psi\) when \(G\) is invariant.
Apply (15.13) under this unitary and the form identity (10.10):
\[
C_{S,\mathrm{phys}}^\rho
 \ge3\kappa(1-512\xi/3)I\ge\frac{287\kappa}{96}I,
\qquad
\|(C_{S,\mathrm{phys}}^\rho)^{-1}\|
 \le\frac1{3\kappa(1-512\xi/3)}
 \le\frac{96}{287\kappa}.                                    \tag{15.23}
\]
This holds for every nonempty eliminated set \(S\), independently
of its size and the exterior volume, on (11.16). It concerns the
full form with derivatives in all link directions, not a
differential operator containing only the eliminated derivatives.
For noninvariant conditional-mean-zero vectors the previously
proved constants (12.15)--(12.16), not (15.23), remain the stated
bounds. The mathematical distinction is implemented by the
proved reducing projection and unitary, not by declaring the
two constructions unrelated.

