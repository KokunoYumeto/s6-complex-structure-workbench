# Magnetic continuation, Gauss projection, and the interacting vacuum

8 September 2026. Complete finite-regulator calculation. The connection to
the original cusp is a map of its magnetic background into the full Wilson
Hilbert space. Every spatial plaquette and the original electric coefficient
are retained. No continuum vacuum or mass-gap conclusion is assumed.
Only the explicit regular-fibre period and magnetic-bundle data are used;
the claimed identification of a completed complex threefold with S6 is
not an input to this calculation.

## 1. Original objects and the reference-frame map

Let \(L\ge2\) be an integer. Vertices are \(n\in\{-L,\ldots,L\}^3\);
a physical edge \(e=(n,i)\) has positive direction i and exists whenever
n and \(n+e_i\) lie in the box. Its independent variable is
\(U_i(n)\in SU(2)\). Negative traversal uses its inverse. Every
elementary face \(p=(n;i,j)\), \(i<j\), is present, with
\[
 W_p(U)=\operatorname{tr}\bigl(U_i(n)U_j(n+e_i)
                 U_i(n+e_j)^{-1}U_j(n)^{-1}\bigr).
\]
There are \(N=3(2L)(2L+1)^2\) links and \(M=3(2L)^2(2L+1)\) faces.
The configuration manifold is \(Q=SU(2)^N\) and dU is product Haar
probability measure. The Hilbert inner product is conjugate-linear in
its first argument. Put \(T_a=-i\sigma_a/2\) and define
\[
 X_{e,a}f(U)=\left.\frac{d}{dt}\right|_{t=0}
 f(\ldots,e^{tT_a}U_e,\ldots),\qquad
 \Delta_e^T=\sum_{a=1}^3X_{e,a}^2.
\]
Haar invariance proves X is skew-adjoint. The original Lie metric is
\(c(A,B)=-\operatorname{tr}(AB)/2\): its orthonormal frame is 2T_a,
so \(\Delta_e^c=4\Delta_e^T\). The Hamiltonian is
\[
 H=-\kappa\sum_e\Delta_e^T+V,\qquad
 V=b\sum_p(2-W_p),\qquad
 \kappa=\frac{2g_{\rm YM}^2}{a},\quad
 b=\frac{1}{2g_{\rm YM}^2a},\quad \xi=\frac b\kappa.
\tag{1.1}
\]
Equivalently its kinetic coefficient in the original metric is
\(-g_{\rm YM}^2/(2a)\) times \(\sum_e\Delta_e^c\).
The full constant 2bM is part of H.

Gauge transformations act as
\((g\cdot U)_e=g_{s(e)}U_eg_{t(e)}^{-1}\).
Let \(R_gf(U)=f(g^{-1}\cdot U)\), and
\(\Pi=\int_{SU(2)^{\mathsf V}}R_g\,dg\).
Haar invariance gives \(R_g^*=R_{g^{-1}}\); averaging proves
\(\Pi^*=\Pi^2=\Pi\). Its range is the gauge-invariant Hilbert space.
The kinetic energy is bi-invariant on each link and the face traces are
invariant, so H and its closed quadratic form commute with Pi.

It is important to specify what is translated. Let M_e and R_e be,
respectively, the original magnetic and a fixed reference parallel
transport, in the same endpoint frames. Define
\[
 h_e=M_eR_e^{-1},\qquad (T_hf)(U)=f((h_e^{-1}U_e)_e).
\tag{1.2}
\]
Here the reference symbol R_e is not the gauge-representation operator R_g.
Under a frame change both transports change by endpoint conjugation;
therefore
\[
 M'_e=g_sM_eg_t^{-1},\quad R'_e=g_sR_eg_t^{-1},\quad
 h'_e=g_sh_eg_s^{-1},\quad R_gT_hR_g^{-1}=T_{h'}.
\tag{1.3}
\]
This proves the exact background-to-state covariance. Translating by
the magnetic transport while changing its frames but not those of the
reference would not be the same construction. In the original fixed
frames the flat reference is R_e=I. All statements below retain that
reference; no assertion that left multiplication is addition of arbitrary
non-Abelian connections is needed.

The original nonwrapping magnetic links, in the physical plane identified
explicitly below, are
\[
 h_1(n)=\exp(-\theta n_2 H_c),\quad h_2(n)=h_3(n)=I,
 \qquad H_c=i\sigma_3=-2T_3,\qquad
 \theta=\frac{2\pi a^2}{D},\quad D=L_Tq_T+6m_T^2.
\tag{1.4}
\]
The period parameters are \(L_T=\operatorname{Im}\tau_T\),
\(q_T=-\operatorname{Im}\beta_T\), \(m_T=\operatorname{Im}\mu_T\),
and D>0. The box is a nonwrapping physical patch; it is not the entire
periodic fibre with transition edges removed. In the original periodic
coordinates u, the underlying connection and transition are
\[
 d+2\pi u_1H_c\,du_2,\qquad
 G_k(u)=\exp(-2\pi k_1u_2H_c).
\]
Its exact finite-vertex frame change is
\(h(n)=\exp(-2\pi H_cn_1n_2/N_0^2)\), where N_0 is the number of
subdivisions in each original compact direction, not the number N of
links. It gives U_1=exp(-2pi H_c n_2/N_0^2) and U_2=I on nonwrapping
edges; on n_2=N_0-1 the second-direction link is exp(2pi H_c n_1/N_0).
These wrap factors and the full period-matrix map are retained in the
companion cusp calculation. The physical-coordinate dictionary for the
patch used here can also be written exactly. In original real coordinates
\((x_1,x_2,x_3,x_4)=(\operatorname{Re}z_1,\operatorname{Im}z_1,
\operatorname{Re}z_2,\operatorname{Im}z_2)\), the imaginary period block is
\[
 B=\begin{pmatrix}6m_T&L_T\\-q_T&m_T\end{pmatrix},\qquad
 \begin{pmatrix}u_1\\u_2\end{pmatrix}
 =\frac1D\begin{pmatrix}m_T&-L_T\\q_T&6m_T\end{pmatrix}
       \begin{pmatrix}x_2\\x_4\end{pmatrix}.
\]
The real period block and the covered real periods are not set to zero:
they determine the other coordinates in the full period map; they do not
enter this displayed exact inverse for u_1,u_2. Choose Euclidean temporal
coordinate y_0=x_3 and spatial coordinates
\((y_1,y_2,y_3)=(x_2,x_4,x_1)\). The full permutation
\((y_0,y_1,y_2,y_3)=(x_3,x_2,x_4,x_1)\) has determinant +1 and
preserves the Euclidean metric; thus no scale or orientation is suppressed.
Direct exterior multiplication gives
\(du_1\wedge du_2=D^{-1}dy_1\wedge dy_2\).

The original connection on this patch is exactly
\[
 A_{\rm orig}=\frac{2\pi H_c}{D^2}
 (m_Ty_1-L_Ty_2)(q_Tdy_1+6m_Tdy_2).
\]
Set \(\mathfrak b=2\pi/D\) and
\[
 f(y)=\frac{2\pi}{D^2}
 \left(\frac{m_Tq_T}{2}y_1^2-L_Tq_Ty_1y_2-3m_TL_Ty_2^2\right).
\]
Expanding both components proves
\(A_{\rm orig}=\mathfrak bH_c y_1dy_2+H_cdf\).
The frame change exp(-H_c f), under
\(A\mapsto g^{-1}Ag+g^{-1}dg\), therefore gives
\(A_0=\mathfrak bH_c y_1dy_2\). The further frame change
\(\exp(-\mathfrak bH_c y_1y_2)\) gives
\(A_1=-\mathfrak bH_c y_2dy_1\). These are exact frame maps of the
same magnetic connection, with all m_T,L_T,q_T terms shown. Using the
stated inverse-parallel-transport convention, integrating A_1 over
the edge from y=a n to y+a e_i gives precisely (1.4).
The reference R_e=I in (1.2) is chosen in this final displayed frame;
subsequent frame changes act on it as well as on M_e by (1.3).
The 12-face holonomy is exp(theta H_c); the 13 and 23 holonomies are I.

## 2. Actual vacuum and exact finite-translation identities

The product Laplacian on this compact connected manifold is elliptic,
with domain \(H^2\) and closed form domain \(H^1\). V is smooth and bounded, so
H has the same domains and compact resolvent. Its bottom eigenvector
can be chosen nonnegative: taking the absolute value does not increase
the gradient form, as follows by differentiating
\(\sqrt{|u|^2+\varepsilon^2}\) and passing to the limit. Elliptic
regularity and the strong maximum principle give a smooth strictly
positive eigenvector psi. Choose \(\int\psi^2dU=1\), let E be its
eigenvalue, and put \(\mathcal A=H-E\).

For a smooth function F, integration by parts and H psi=E psi give
\[
 \mathfrak q_{\mathcal A}[\psi F]
 =\kappa\sum_{e,a}\int |X_{e,a}F|^2\psi^2\,dU.
\tag{2.1}
\]
The same formula after polarization holds on H1 by density. If another
ground eigenfunction existed, its quotient by the positive psi would
make the right hand side zero, hence be constant on Q. This proves
simplicity. Gauge transformations preserve the positive normalized
ground state, so \(\Pi\psi=\psi\). Compactness and simplicity give
a positive finite-regulator first excited energy, but no uniform bound
as L or a varies is asserted here.

Translation T_h is unitary by Haar invariance, preserves smooth functions
and all Sobolev spaces, and commutes with the full electric Laplacian.
Define
\[
 c_h=\langle\psi,T_h\psi\rangle,
 \qquad \chi_h=\Pi T_h\psi-c_h\psi.
\tag{2.2}
\]
The scalar c_h is real and positive, since both pointwise functions in
the integral are positive. The state is gauge invariant, smooth, and
vacuum orthogonal. Its exact norm and excitation form energy are
\[
 d_h=\|\chi_h\|^2
 =\langle T_h\psi,\Pi T_h\psi\rangle-c_h^2,
\qquad
 n_h=\mathfrak q_{\mathcal A}[\Pi T_h\psi].
\tag{2.3}
\]
When d_h>0 its Rayleigh quotient is n_h/d_h. No division by a presumed
nonzero norm is made.

There is also an exact comparison with the unprojected state:
\[
 0\le n_h\le\mathfrak q_{\mathcal A}[T_h\psi]
 =\int\psi(U)^2\,[V((h_eU_e)_e)-V(U)]\,dU.
\tag{2.4}
\]
Indeed Pi commutes with the nonnegative operator A, so its retained and
orthogonal components have additive nonnegative energies. The last
identity follows from
\(T_h^*HT_h=H+V(hU)-V(U)\) and H psi=E psi. Thus even the
unprojected magnetic energy is an average in the actual vacuum, not
the action of the magnetic configuration alone. Formula (2.4) supplies
an energy numerator, not a lower bound on d_h.

## 3. General infinitesimal projection, with the zero branch resolved

For real coefficients alpha_{e,a}, set
\(A_e=\sum_a\alpha_{e,a}T_a\),
\(Y=\sum_{e,a}\alpha_{e,a}X_{e,a}\), and
\(h_e(t)=\exp(tA_e)\). Then \(T_t=\exp(-tY)\) exactly.
All expansions in this section are applied to smooth psi in any fixed
Sobolev norm. Taylor's formula for the smooth translation flow, with
its bounded integral remainder on the compact group, justifies every
term and its form-domain use.

The conjugation rule obtained by differentiating (1.3) is
\[
 R_gX_e(A)R_g^{-1}=X_e(\operatorname{Ad}_{g_{s(e)}}A).
\tag{3.1}
\]
The adjoint SU(2) representation acts by all rotations on the three real
coefficients in the chosen orthonormal Lie basis. Haar averaging of a
vector is zero. Averaging a pair gives
\(\int(\operatorname{Ad}_g u)_a(\operatorname{Ad}_g v)_b,dg
=(u\cdot v)\delta_{ab}/3\): invariance makes the matrix scalar, and
its trace is u dot v. Different vertices have independent Haar variables.
Applying these identities to invariant psi proves
\[
 \Pi Y\psi=0,\qquad
 K_2\psi:=\Pi Y^2\psi
 =\frac13\sum_v\sum_{s(e)=s(f)=v}
 (\alpha_e\cdot\alpha_f)\sum_a X_{e,a}X_{f,a}\psi.
\tag{3.2}
\]
The second sum is ordered: e=f terms and both orders of unequal edges
are retained. The grouping is by the sources of the chosen positive
edges, not by an unrecorded change to incoming-edge derivatives.

Since Y is skew-adjoint and psi is real, its overlap has
\(c'(0)=\langle\psi,-Y\psi\rangle=0\) and
\(c''(0)=\langle\psi,Y^2\psi\rangle=-\|Y\psi\|^2\).
Define
\[
 S=\|Y\psi\|^2,\qquad \eta=K_2\psi+S\psi.
\]
Then the exact centered physical state obeys
\[
 \chi_t=\frac{t^2}{2}\eta+O_{H^1}(t^3),\qquad
 \|\chi_t\|^2=\frac{t^4}{4}\|\eta\|^2+O(t^5),
\quad
 \mathfrak q_{\mathcal A}[\chi_t]
 =\frac{t^4}{4}\mathfrak q_{\mathcal A}[\eta]+O(t^5).
\tag{3.3}
\]
The energy remainder follows from continuity of the form on H1;
it is not obtained by treating an unbounded Hamiltonian as bounded.

There is no unexamined branch where eta vanishes but a later derivative
is the first excitation. The Haar integral of every X derivative is zero,
so \(\int K_2\psi\,dU=0\). If eta=0, integrating its defining
identity gives \(S\int\psi\,dU=0\); positivity of psi gives S=0.
Hence Y psi=0, the translation flow fixes psi, and chi_t=0 for every t.
Conversely that identity implies eta=0. Therefore a translation either
fixes the vacuum exactly or has strictly positive quartic leading norm.
In the nontrivial case the finite-regulator limiting excitation quotient is
\[
 \lim_{t\to0}\frac{\mathfrak q_{\mathcal A}[\chi_t]}{\|\chi_t\|^2}
 =\frac{\mathfrak q_{\mathcal A}[\eta]}{\|\eta\|^2}>0.
\tag{3.4}
\]
Strict positivity follows because eta is nonzero, gauge invariant and
orthogonal to psi, whose eigenvalue is simple. This statement holds at
fixed regulator and arbitrary positive original coupling. It does not
take L to infinity or a to zero.

## 4. Exact class-convolution map for the native magnetic translation

For (1.4), there is at most one nonidentity translated edge with any given
source vertex. Conjugating T_h by R_g and averaging therefore factorizes
into independent averages for these edges. On invariant inputs,
\[
 \Pi T_h\Pi=K_\theta\Pi,\qquad
 K_\theta=\prod_{e=(n,1)}C_{e,\theta n_2},
\tag{4.1}
\]
where the full single-edge operator is
\[
 C_{e,s}f(U)=\int_{SU(2)}
 f(\ldots,(g e^{-sH_c}g^{-1})^{-1}U_e,\ldots)\,dg.
\tag{4.2}
\]
Different link factors commute. Every C is a contraction and preserves
positive functions, since it averages unitary translations with a
probability measure. Its conjugacy-class measure is central and invariant
under inversion: in SU(2), e^{sH_c} and e^{-sH_c} are conjugate, for example
by i sigma_1. Consequently C is self-adjoint and even in s. These facts
do not claim it has nonnegative spectral eigenvalues.

Here is its exact Peter--Weyl action, including all representations. On
a spin-j matrix coefficient on edge e, j=0,1/2,1,..., averaging the
conjugated representation matrix commutes with the irreducible SU(2)
representation. It is scalar by Schur's lemma, and its trace fixes that
scalar to the character divided by the dimension. The weights
m=-j,-j+1,...,j give
\[
 c_j(s)=\frac{1}{2j+1}\sum_{m=-j}^j e^{2ims}
 =\frac{\sin((2j+1)s)}{(2j+1)\sin s}.
\tag{4.3}
\]
The sum is the definition at sin s=0 and gives its continuous value;
no singular denominator is used there. Since the product coefficients
are a complete orthogonal basis, (4.3) defines K_theta on the entire
Hilbert space. It commutes with each left and right link translation,
with Pi, and with the full electric energy.

Thus (2.2)--(2.3) become the exact full-vacuum formulas
\[
 c_\theta=\langle\psi,K_\theta\psi\rangle,\quad
 d_\theta=\langle\psi,K_\theta^2\psi\rangle-c_\theta^2,
\quad n_\theta=\mathfrak q_{\mathcal A}[K_\theta\psi].
\tag{4.4}
\]
On smooth psi the numerator also has the exact double-commutator form
\[
 n_\theta=\frac12\langle\psi,
 [K_\theta,[H,K_\theta]]\psi\rangle
 =\frac12\langle\psi,[K_\theta,[V,K_\theta]]\psi\rangle.
\tag{4.5}
\]
Expanding the first double commutator gives
2KHK-K^2H-HK^2, and applying H psi=E psi proves the first equality.
The second uses the proved commutation with the electric Laplacian.
No magnetic term disappears: V is still the sum over all M faces.

## 5. Leading physical state for the magnetic angle, at every b>0

In (3.2) the native generator has
\(\alpha_{(n,1),3}=2n_2\) and all other components zero. Indeed
\(-n_2H_c=2n_2T_3\) in h_1=exp(-theta n_2 H_c), and T_theta
uses the inverse translation exp(-theta Y). Since a source has only
one such edge, (3.2) yields
\[
 K_2=\frac43\sum_{e=(n,1)}n_2^2\Delta_e^T
 =-\frac43\Gamma,
\qquad \Gamma=\sum_{e=(n,1)}n_2^2(-\Delta_e^T).
\tag{5.1}
\]
The same coefficient follows from the retained character sum: symmetry
gives sum m=0 and
\(\sum_{m=-j}^jm^2=(2j+1)j(j+1)/3\), so
\(c_j(s)=1-2j(j+1)s^2/3+O_j(s^4)\).
For the full operator the correct expansion is on smooth vectors, or
as a map H^{k+4} to H^k:
\[
 K_\theta\psi=\psi-\frac23\theta^2\Gamma\psi
                  +O_{H^k}(\theta^4).
\tag{5.2}
\]
One need not sum unbounded representation-wise errors to justify it.
Apply Taylor's integral formula to the averaged link-translation flow:
four derivatives are bounded H^{k+4} to H^k, uniformly over the compact
averaging group and small theta. Evenness of each C, hence of their
product, removes the odd terms. There is no same-Sobolev-space bounded
operator expansion with the unbounded Gamma silently treated as bounded.

Put
\[
 \gamma=\langle\psi,\Gamma\psi\rangle,\qquad
 v=(\Gamma-\gamma)\psi.
\]
Equations (4.4) and (5.2), with the actual vacuum scalar retained, give
\[
 \chi_\theta=-\frac23\theta^2v+O_{H^1}(\theta^4),
\quad d_\theta=\frac49\theta^4\|v\|^2+O(\theta^6),
\quad n_\theta=\frac49\theta^4\mathfrak q_{\mathcal A}[v]
                         +O(\theta^6).
\tag{5.3}
\]
In particular \(\|v\|^2=\langle\psi,\Gamma^2\psi\rangle-\gamma^2\)
is the actual quantum variance of this specified weighted electric
operator, not a variance in an independently postulated link measure.

For this native translation v is nonzero for every b>0. To prove it,
suppose Gamma psi=gamma psi. Integrate against Haar, not psi: every
Laplacian has zero Haar integral, and \(\int\psi>0\), so gamma=0.
Taking its inner product with psi yields
\[
 0=\langle\psi,\Gamma\psi\rangle
   =\sum_{e=(n,1),a}n_2^2\|X_{e,a}\psi\|^2.
\]
Thus psi is independent of each direction-1 link with n_2 nonzero;
the three derivative fields span that connected SU(2) factor. Select
e=((0,1,0),1). It exists in every box L>=2 and has exactly four incident
faces. In the eigen-equation, after this independence is proved, all
kinetic terms and the factor psi are independent of U_e. Fix all other
link variables to I; smoothness permits this pointwise evaluation and
strict positivity makes the fixed value of psi nonzero. The potential
as a function of U_e is precisely
\[
 V(U_e,I_{\ne e})=4b(2-\operatorname{tr}U_e).
\]
Nonincident faces have trace 2; every incident face has trace tr U_e
or tr U_e^{-1}, which are equal in SU(2). This nonconstant potential
contradicts the eigen-equation for b>0. We have proved v!=0, without a
small-b assumption and without calculating the full vacuum by Haar
substitution.

Consequently for every fixed box, a, and g_YM>0,
\[
 \lim_{\theta\to0}\frac{n_\theta}{d_\theta}
 =\frac{\mathfrak q_{\mathcal A}[v]}{\|v\|^2}>0.
\tag{5.4}
\]
The original magnetic angle and scale are still theta=2pi a^2/D.
Both numerator and norm tend to zero at the same fourth order, so a
small classical magnetic action does not by itself determine this
physical Rayleigh quotient. Formula (5.4) does not bound that quotient
uniformly when L, a, g_YM and D vary together. Those joint dependences
remain to be calculated rather than inferred from the fixed-box limit.

## 6. Exact derivatives retaining every magnetic plaquette

For completeness the numerator in (5.4) has no hidden electric-operator
commutator. Gamma commutes with the full electric part of H, and hence
\[
 (H-E)\Gamma\psi=[V,\Gamma]\psi,
\qquad
 [V,\Gamma]F
 =\sum_{e=(n,1),a}n_2^2
       \bigl[(X_{e,a}^2V)F+2(X_{e,a}V)X_{e,a}F\bigr].
\tag{6.1}
\]
The formula is the product rule for each original derivative. Thus
\[
 \mathfrak q_{\mathcal A}[v]
 =\langle\Gamma\psi,[V,\Gamma]\psi\rangle
 =\frac12\langle\psi,[\Gamma,[V,\Gamma]]\psi\rangle.
\tag{6.2}
\]
All functions are smooth, so these unbounded-operator products are
well-defined on the vector being used. Defining
\(q_p=(3/4)\sum_{e\in\partial p,\ e=(n,1)}n_2^2\), the four-edge
fundamental Casimir gives
\[
 \Gamma W_p=q_pW_p,\quad
 \Gamma V=-b\sum_pq_pW_p,\quad
 X_{e,a}V=-b\sum_{p\ni e}X_{e,a}W_p.
\tag{6.3}
\]
These are exact expressions over the same full face set, including the
13-plane faces for which the chosen background has identity curvature.
They provide explicit coefficients for calculating the vacuum moments;
they do not assign those moments their free-Haar values.

## 7. Exact map to the discrete electric representation variables

Choose an orthonormal product Peter--Weyl basis with a spin j_e on each
edge. The electric eigenvalue is \(\kappa\sum_ej_e(j_e+1)\).
Each joint edge-spin subspace is finite dimensional and invariant under
vertex gauge transformations, since left and right multiplication do
not change the edge representation. Applying Pi in that subspace and
choosing an orthonormal basis of its range gives vectors \(\Phi_s\),
where the index s records all edge spins and the invariant multiplicity
label. Their union is a complete orthonormal basis of the physical
Hilbert space: the full Peter--Weyl expansion is complete, Pi is bounded,
and its finite-spin images are dense in its range.

Expand the actual vacuum, without changing it, as
\[
 \psi=\sum_s a_s\Phi_s,\quad \sum_s|a_s|^2=1,\qquad
 k_s(\theta)=\prod_{e=(n,1)}
 \frac{\sin((2j_e+1)\theta n_2)}{(2j_e+1)\sin(\theta n_2)}.
\tag{7.1}
\]
Each factor has the finite-sum interpretation of (4.3) at a zero
denominator. K acts by k_s on the entire invariant multiplicity space,
because it already acts by that scalar on the surrounding full joint
edge-spin subspace. Hence the exact vacuum overlap and physical state
norm become
\[
 c_\theta=\sum_s|a_s|^2k_s(\theta),\quad
 \chi_\theta=\sum_s a_s(k_s(\theta)-c_\theta)\Phi_s,
\quad
 d_\theta=\sum_s|a_s|^2(k_s(\theta)-c_\theta)^2.
\tag{7.2}
\]
The scalar sums converge absolutely since |k_s|<=1; the vector sum
converges in Hilbert norm. It also converges in the form domain because
psi is smooth and K commutes with the electric Sobolev operator. Thus
(7.2) is a unitary coordinate map, not an identification of the
unknown coefficients a_s with independent free-field weights.

Retain the entire magnetic matrix
\[
 V_{st}=\langle\Phi_s,V\Phi_t\rangle
 =2bM\delta_{st}-b\sum_p\langle\Phi_s,W_p\Phi_t\rangle.
\]
For a growing sequence of finite joint-spin cutoffs F_R tending to the
identity, (4.5) gives the exact convergent expression
\[
 n_\theta=-\frac12\lim_{R\to\infty}
 \sum_{s,t\in F_R}\overline{a_s}a_t\,
 (k_s(\theta)-k_t(\theta))^2 V_{st}.
\tag{7.3}
\]
Here the notation s in F_R means basis indices in that cutoff. To
justify the limit, expand the finite sum as the expectation on F_R psi
of the bounded operator \([K,[V,K]]/2\). Explicitly,
the matrix entry of \([K,[V,K]]\) is
\(-(k_s-k_t)^2V_{st}\). Thus the finite sum is the expectation of
\([K,[V,K]]/2\) on F_R psi. The operator is bounded because K and V
are bounded, and F_R psi tends to psi. No unproved absolute convergence
of an infinite double matrix sum is required. The full scalar 2bM has
zero contribution in (7.3), since its matrix is diagonal and the displayed
difference then vanishes; it remains in H and in E.

Equations (7.1)--(7.3) retain the exact relation between the continuous
magnetic angle and all discrete electric channels. The non-Abelian
plaquettes couple those channels through the specified V_st. Their
individual summands are not assumed nonnegative and are not dropped.
A conclusion about arbitrarily low physical energies requires the
limiting ratio of these two actual-vacuum expressions, not only the
smallness of each change in k_s or of the classical field strength.

## 8. A finite-range energy kernel and the full covariance denominator

The same state can be expressed directly through local electric operators,
without knowing their vacuum expectations in advance. For each physical
edge let \(E_e=-\Delta_e^T\),
\(\gamma_e=\langle\psi,E_e\psi\rangle\), and
\(v_e=(E_e-\gamma_e)\psi\). These are smooth gauge-invariant vectors
orthogonal to psi. Define the two exact finite matrices
\[
 C_{ef}=\langle v_e,v_f\rangle,
 \qquad N_{ef}=\mathfrak q_{\mathcal A}(v_e,v_f).
\tag{8.1}
\]
They are positive semidefinite by their Gram definitions, with no
assumption about signs of individual entries. Because psi, E_e and
H preserve real functions, both matrices are real and symmetric.
Different link Casimirs commute, and an operator commutes with itself,
so \([E_e,E_f]=0\) for every pair. Expanding the double commutator
on the smooth vacuum gives
\[
 \boxed{N_{ef}=\frac12\langle\psi,[E_e,[H,E_f]]\psi\rangle
              =\frac12\langle\psi,[E_e,[V,E_f]]\psi\rangle.}
\tag{8.2}
\]
Indeed its four terms have expectation
\(\langle E_e\psi,HE_f\psi\rangle+
\langle E_f\psi,HE_e\psi\rangle-
2E\langle E_e\psi,E_f\psi\rangle\).
Reality and symmetry make this exactly twice the centered form in (8.1).
The second equality retains the original kinetic coefficient: every E_e
commutes with its whole electric sum, so that commutator is identically
zero, not approximated by zero.

This gives an exact finite-range support statement for the numerator:
\[
 N_{ef}=\frac b2\sum_{p:\ e,f\in\partial p}
 \langle\psi,[E_e,[2-W_p,E_f]]\psi\rangle.
\tag{8.3}
\]
To prove it, if f does not belong to p then E_f differentiates a
different group variable and commutes with multiplication by W_p.
If f belongs but e does not, the first commutator differentiates only
f and has coefficients depending only on p's variables; it therefore
commutes with E_e. These statements follow term by term from the product
rule, including all first-derivative terms. Thus a term can remain only
when both edges belong to the same face, including the diagonal case
e=f. No vacuum-factorization or correlation-decay assumption is involved.

For the native state set w_e=n_2^2 on e=(n,1), and w_e=0 otherwise.
Equations (5.1) and (8.1) imply exactly
\[
 v=\sum_e w_ev_e,\qquad
 \|v\|^2=\sum_{e,f}w_ew_fC_{ef},\qquad
 \mathfrak q_{\mathcal A}[v]=\sum_{e,f}w_ew_fN_{ef}.
\tag{8.4}
\]
The denominator is positive by Section 5. The small-angle physical
excitation quotient (5.4) is therefore the fully specified ratio
\[
 \boxed{\frac{\sum_{e,f}w_ew_fN_{ef}}
              {\sum_{e,f}w_ew_fC_{ef}}.}
\tag{8.5}
\]
Its numerator couples only edges sharing an elementary plaquette;
its denominator retains all electric correlations of the actual
interacting vacuum, including separated edges. This is an exact
local-energy/global-covariance relation. It neither asserts that the
denominator grows faster nor rules that out. Estimating these two sums
along the original geometric and coupling sequence is the precise
remaining spectral calculation for this family of physical states.

## 9. Context, sources, and scope

This uses the Hamiltonian formulation of lattice gauge theory of J. Kogut
and L. Susskind, *Physical Review D* 11 (1975), 395--408,
<https://doi.org/10.1103/PhysRevD.11.395>. The coefficient dictionary from
the original anisotropic Wilson transfer and the full compact-group
ground-state form are proved in the companion temporal-transfer and
interacting-Wilson sources. Haar projection and Schur averaging are
established compact-group tools; no novelty of those general tools is
claimed here. The particular original background, its reference-frame
map, all orientations, the physical state, and the nonzero all-b magnetic
variance are explicitly calculated above.

The four-dimensional target includes construction of the interacting
quantum theory and a statement about its physical spectrum; see
A. Jaffe and E. Witten, *Quantum Yang--Mills Theory*,
<https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf>.
The present theorem tests an explicit background-to-quantum-state map at
a finite spatial regulator. It neither assumes a uniform volume estimate
nor claims a construction or disproof of the continuum theory. The next
calculation evaluates the actual vacuum coefficients of this state with
all box plaquettes present; its full derivation accompanies this note.
