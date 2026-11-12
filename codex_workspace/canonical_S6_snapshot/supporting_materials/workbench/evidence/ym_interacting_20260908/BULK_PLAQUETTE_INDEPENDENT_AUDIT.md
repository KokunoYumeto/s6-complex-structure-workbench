# Independent audit: full-box adjacent-plaquette correction

8 September 2026. Verdict: PASS for every fixed open box with \(L\geq2\)
and sufficiently small positive \(\xi=b/\kappa\). No mathematical error
was found. The two leading coefficients \(1/12\) and \(1951/81675\)
extend as stated, with box-dependent remainders. No mathematical source,
PDF, canonical artifact or remote content was changed by this audit.

The full initial 735-line BULK_PLAQUETTE_EXTENSION.md and complete
check_bulk_plaquette_incidence.py were read. The subsequent 11-line
exact basis-convention paragraph was also read and verified; removing
only that paragraph recovers the initial source hash exactly. The final
746-line source is therefore covered in full. Final audited SHA-256 values:

- Proof: 64a67b4ac63f197f3eced7099164ce320c980496b04c3b5c8a438f24c76562f6.
- Checker: 8b61f5f43db983fb9a4fbdf73a376e7538149be4443204493dd73908e9a52f22.

The checker replay passed for every complete graph and face set at
\(L=2,3,4,5\):

| \(L\) | All physical links \(N\) | All faces \(M\) | Neumann radius |
| --- | --- | --- | --- |
| 2 | 300 | 240 | \(1/1280\) |
| 3 | 882 | 756 | \(1/4032\) |
| 4 | 1944 | 1728 | \(1/9216\) |
| 5 | 3630 | 3300 | \(1/17600\) |

These enumerations and exact rational tests corroborate the following
all-\(L\) proof; they are not substitutes for its analytic estimates.

## 1. Exact convention map and original Hamiltonian

The bulk source uses \(T_a^{\rm bulk}=-i\sigma_a/2\), whereas the previously
audited two-face calculation used \(T_a^{\rm prior}=+i\sigma_a/2\).
The exact map is

\[
T_a^{\rm bulk}=-T_a^{\rm prior},\qquad
X_{e,a}^{\rm bulk}=-X_{e,a}^{\rm prior},\qquad
\sigma_{e,a}^{\rm bulk}=-\sigma_{e,a}^{\rm prior}.
\]

Consequently \(\Delta^T\), each product
\((XW_P)(XW_Q)\), every Dirichlet form and
\(-\kappa\sum\sigma_{e,a}X_{e,a}f\) are exactly unchanged. This proves
the convention correspondence rather than silently identifying the two
individual derivatives. In the bulk convention
\(\operatorname{tr}(T_aP_*)=p_a\) and
\(-\operatorname{tr}(T_aQ'_*)=-q_a\); their product still gives
\(G=-\sum_ap_aq_a\).

For \(c(X,Y)=-\operatorname{tr}(XY)/2\), the orthonormal frame is
\(2T_a^{\rm bulk}\), so \(\Delta^c=4\Delta^T\).
All coefficients and the full scalar are preserved:

\[
H_{\kappa,b}=\kappa(H_0-\xi\mathcal V)+2bM I,\qquad
\mathcal V=\sum_{p\in\mathsf P_L}W_p,\qquad
\kappa=\frac{2g_{\rm YM}^2}{a},\quad b=\frac1{2g_{\rm YM}^2a}.
\]

Thus the kinetic coefficient with \(\Delta^c\) is \(g_{\rm YM}^2/(2a)\),
and \(E_\xi=\kappa e(\xi)+2bM\). No potential term or constant has
been dropped from the Hamiltonian.

## 2. Literal incidence and based orientations

Counting initial coordinates along a link gives
\(N=3(2L)(2L+1)^2\). Counting the two varying coordinates of an
elementary face gives \(M=3(2L)^2(2L+1)\).
For the direction-2 edge \(s=((-1,0,0),2)\), the only transverse
directions are 1 and 3, each with positive or negative unit extension.
Therefore its complete star is precisely

\[
\{((-1,0,0);1,2),((-2,0,0);1,2),
  ((-1,0,0);2,3),((-1,0,-1);2,3)\}.
\]

All four faces exist for \(L\geq2\). The last three have first
coordinate at most \(-1\) at every vertex; every vertex of
\(Q=((0,0,0);1,2)\) has first coordinate 0 or 1. They cannot share
an edge with \(Q\). For the remaining face \(P\), the boundary formula
gives exactly

\[
\partial P\cap\partial Q=\{e\},\qquad e=((0,0,0),2),
\]

with positive occurrence in \(P\), negative occurrence in \(Q\), and
negative occurrence of \(s\) in \(P\).

Expanding the source's elementary-face word and cyclically moving its
initial factors gives its literal products

\[
A=U_1(-1,1,0)^{-1}U_2(-1,0,0)^{-1}U_1(-1,0,0),\qquad
B=U_1(0,0,0)U_2(1,0,0)U_1(0,1,0)^{-1},
\]

\[
P_*=U_eA,\qquad Q_*=U_e^{-1}B,\qquad Q'_*=BU_e^{-1}.
\]

The six outer physical edges are distinct. They include \(s\) once
inversely in \(A\), never in \(B\), and exclude \(e\). These equalities
prove the orientation and seven-link support used in the contraction;
they do not change the full box on which the functions are defined.

## 3. The all-face vacuum, its radius and normalization

Product Peter-Weyl decomposition gives a simple free zero eigenvector
and first nonzero eigenvalue \(3/4\) on the entire link Hilbert space.
Every \(W_p\) has free eigenvalue 3 because its four edges each carry
the fundamental Casimir \(3/4\).

The uniform bound \(|W_p|\leq2\) gives \(\|\mathcal V\|_\infty\leq2M\).
The all-identity configuration attains \(2M\); continuity and positive
Haar measure of each open neighborhood prove the essential supremum is
also exactly \(2M\). On \(|z|=3/8\),
\(\|(z-H_0)^{-1}\|\leq8/3\). The full perturbation norm bound is thus
\(q=16M|\xi|/3\), giving exactly

\[
|\xi|<\frac3{16M}.
\]

The contour resolvent series converges there. Its norm-continuous
projection has rank one throughout this connected disk because rank
is unchanged between projections whose norm difference is below one.
For real \(\xi\), min-max gives the second eigenvalue at least
\(3/4-2M|\xi|>3/8\), while the constant trial and operator lower
bound give \(-3/8<e(\xi)\leq0\). This contour therefore selects the
actual ground state, not the ground state of a two-face truncation.

The projection estimate \(\|\Pi_\xi-\Pi_0\|\leq q/(1-q)\) follows by
integrating the resolvent difference on the circle; its radius \(3/8\)
cancels the factor \(8/3\). For \(q<1/2\), the denominator
\(\langle1,\Pi_\xi1\rangle\) is nonzero. The source accordingly makes
its mean-one eigenvector choice locally, without asserting that this
particular coordinate works on the entire complex projection disk.

Haar integration over an edge appearing only in one face proves
\(\int W_pW_q=0\) for distinct elementary faces. Such an edge exists:
the boundary-edge set recovers the two coordinate directions and lower
corner of a unit square, hence distinct faces have distinct edge sets.
Single-face integration gives \(\int W_p^2=1\), so
\(\|\mathcal V\|_2^2=M\). Differentiating the ground equation yields

\[
e'(0)=0,\qquad \phi'_0=\mathcal V/3,\qquad
\phi_\xi=1+\xi\mathcal V/3+O_{L,k}(\xi^2).
\]

The elliptic equation
\(\phi_\xi=(H_0+1)^{-1}[(e(\xi)+1+\xi\mathcal V)\phi_\xi]\)
upgrades analytic \(L^2\) dependence to every fixed Sobolev order,
then to every fixed \(C^k\) norm by embedding in dimension \(3N\).
Constants and the smaller disks may depend on \(L,k\).
Mean-one higher coefficients have zero integral; hence

\[
Z_\xi=1+\frac M9\xi^2+O_L(\xi^3),\qquad
\log\rho_\xi=\frac{2\xi}{3}\sum_pW_p+O_{L,k}(\xi^2).
\]

The modulus argument, elliptic regularity and strong positivity give
the actual unique positive vacuum on the real interval. Its local
uniform closeness to 1 permits the stated logarithm expansion.
In particular the all-face normalization coefficient is \(M/9\), not
the coefficient of the isolated two-face complex.

## 4. Why the extra faces do not alter the leading coupling

The literal marginal and conditional density are
\(\rho_{R,\xi}=\int\rho_\xi\,dU_s\) and
\(p_\xi=\rho_\xi/\rho_{R,\xi}\). Their exact conditional expectation is
the adjoint of the retained lift and is orthogonal for the true weighted
inner product. Differentiation under the compact integral proves

\[
J_\xi^*(X_{i,a}\log\rho_\xi)
=X_{i,a}\log\rho_{R,\xi},
\]

which makes the exact off-diagonal map
\(B_\xi f=-\kappa\sum_{i\in R,a}\sigma_{i,a,\xi}X_{i,a}f\).
The second derivatives cancel exactly.

At first order, every face incident on \(s\) is annihilated by that
link's Haar integral, including its retained derivatives. Every other
face survives identically in both the full and marginal scores.
Consequently

\[
\sigma_{i,a,\xi}
=\frac{2\xi}{3}\sum_{p\ni s}X_{i,a}W_p+O_{L,k}(\xi^2).
\]

All nonzero derivatives of \(f_\xi\) lie on \(\partial Q\).
The incidence calculation in Section 2 therefore reduces the double
sum to the single pair \((P,e)\), proving

\[
B_\xi f_\xi=-\frac{2b}{3}G+O_{L,k}(\kappa\xi^2).
\]

Extra faces are thus accounted for by an exact first-order conditional
cancellation or by exact disjointness of derivative supports. They
remain in the full density and in every controlled remainder.

## 5. Full-space Haar channels and the \(1/12\) coefficient

The Pauli entry identity gives the same Fierz contraction with the
bulk basis:

\[
G=\frac12R_0-\frac14D_0=\frac38R_0-\frac14D_1,\qquad
R_0=\operatorname{tr}(AB),\quad D_0=W_PW_Q,\quad D_1=D_0-R_0/2.
\]

Conditionally on \(U_e\), the disjoint products \(A,B\) are independent
Haar matrices. The same is true of \(P_*,Q'_*\). For their independent
unit quaternions \(p,q\), set \(x=p_0q_0\),
\(y=\sum_{a=1}^3p_aq_a\). Invariance and the unit-sphere equation give

\[
\mathbb E x^2=1/16,\quad \mathbb E y^2=3/16,\quad \mathbb E xy=0,
\quad R_0=2(x-y),\quad D_1=3x+y,\quad G=-y.
\]

Therefore \(\|R_0\|^2=1\), \(\|D_1\|^2=3/4\),
\(\langle R_0,D_1\rangle=0\) and \(\|G\|^2=3/16\).
All additional box-link integrals are integrals of 1 against probability
Haar measure, so there is no additional volume factor in these norms.

The six outer edges contribute \(6(3/4)=9/2\) to both modes. On \(e\),
\(\Delta_eR_0=0\) and
\(\Delta_eD_0=-3D_0/2+2G=-2D_1\). Every other box-edge Laplacian
annihilates both functions. Thus the eigenvalue equations on the
entire box are exactly

\[
H_0R_0=\frac92R_0,\qquad H_0D_1=\frac{13}{2}D_1.
\]

Both modes have zero Haar conditional mean over \(s\). Writing
\(g_1=-R_0/4+D_1/6\), the complete forcing is
\(g_\xi=B_\xi f_\xi=\kappa\xi g_1+O_L(\kappa\xi^2)\).
Since \(\rho_\xi=1+O_L(\xi)\),

\[
\|g_\xi\|_\xi^2
=\kappa^2\xi^2\left(\frac1{16}+\frac{3}{4\cdot36}\right)
+O_L(\kappa^2\xi^3)
=\frac{b^2}{12}+O_L(b^3/\kappa).
\]

## 6. Actual moving form domain and the corrected vector

The exact derivative identity for \(J_\xi^*\) is
\(XJ_\xi^*v=J_\xi^*(Xv)+J_\xi^*(\sigma_Xv)\).
Conditional Cauchy-Schwarz and bounded scores prove that \(P_\xi,Q_\xi\)
preserve \(H^1\), as well as smooth functions. Thus
\(\mathcal D_\xi=H^1\cap\ker J_\xi^*\) is dense in the conditional kernel
and closed in form norm. The restriction of \(q_\xi\) is a closed
nonnegative form and defines \(C_\xi\) through precisely the weak
representation domain in the source. No formal compression domain is
assumed.

The density and its first derivatives differ from Haar by \(O_L(\xi)\).
Differentiating the conditional kernel proves
\(P_\xi-P_0=O_L(\xi)\) on \(L^2\) and \(H^1\).
All projections have the same retained range, so their exact algebra is

\[
Q_0Q_\xi=Q_0,\qquad Q_\xi Q_0=Q_\xi,\qquad
T_\xi=Q_\xi|_{\mathcal K_0},\qquad
T_\xi^{-1}=Q_0|_{\mathcal K_\xi}.
\]

These maps identify the full form domains, not merely a finite-dimensional
subspace. Pulling back \(\kappa^{-1}q_\xi+\langle\cdot,\cdot\rangle_\xi\)
gives the source's dimensionless form \(\mathfrak a_\xi\) on
\(\mathcal D_0\), with

\[
\mathfrak a_0(v,v)=\|v\|_{H^1}^2,\qquad
|\mathfrak a_\xi(v,h)-\mathfrak a_0(v,h)|
\leq C_L|\xi|\|v\|_{H^1}\|h\|_{H^1}.
\]

The last bound gives coercivity at least \(1/2\) on a smaller interval.
For \(w_\xi=(C_\xi+\kappa)^{-1}g_\xi\) and
\(h_\xi=T_\xi^{-1}w_\xi\), its exact weak equation becomes

\[
\mathfrak a_\xi(v,h_\xi)
=\xi\langle v,g_1\rangle_0+O_L(\xi^2)\|v\|_{H^1}.
\]

Haar conditional expectation commutes with the complete free Laplacian.
Thus the two full-space eigenmodes above are also eliminated eigenmodes,
and the free solution is

\[
h_1=(H_0+1)^{-1}g_1=-R_0/22+D_1/45.
\]

Subtracting \(\xi\mathfrak a_\xi(v,h_1)\) and testing with
\(v=h_\xi-\xi h_1\) bounds the difference by \(O_L(\xi^2)\) in \(H^1\).
Transport back contributes the same order. Therefore

\[
w_\xi=\xi(-R_0/22+D_1/45)+O_L(\xi^2)\quad\text{in }H^1.
\]

This proves, rather than assumes, that other modes and the changing
vacuum do not affect the leading coefficient.

## 7. Exact energy identity, second coefficient and scope

The full-state vector \(u_\xi=\psi_\xi(Jf_\xi-w_\xi)\) belongs to the
original form domain, is nonzero, and is orthogonal to the actual vacuum.
Haar changes of the eliminated variable prove gauge equivariance of
the projections; invariant forms and uniqueness of the resolvent then
prove gauge invariance of this vector. The two occurrences of the
gauge convention are related by \(g_v=h_v^{-1}\).

The exact retained numerator is \(a_\xi=\kappa(4-r_\xi)\), because each
of the four simple-loop edges has squared gradient \(1-W_Q^2/4\).
Haar edge annihilation gives \(m_\xi=2\xi/3+O_L(\xi^2)\), while every
linear moment \(\int W_Q^2W_p\) vanishes: for \(p\ne Q\) integrate an
edge unique to \(p\), and for \(p=Q\) use an edge-center sign change.
Hence \(r_\xi=1+O_L(\xi^2)\), \(d_\xi=1+O_L(\xi^2)\), and
\(\mathcal R_{\rm ret}=3\kappa+O_L(\kappa\xi^2)\).
The source uses these justified full-box moment bounds, not an
unproved transfer of the isolated two-face second-order moments.

Set \(I_\xi=\langle g_\xi,w_\xi\rangle_\xi\) and
\(J_\xi^{\rm num}=\|w_\xi\|_\xi^2\). The exact weak resolvent equation
gives \(q_\xi(w_\xi,w_\xi)=I_\xi-\kappa J_\xi^{\rm num}\).
The cross form with \(Jf_\xi\) is \(I_\xi\); orthogonality gives the
denominator \(d_\xi+J_\xi^{\rm num}\). Therefore

\[
\mathcal R_{\rm ret}-\mathcal R_{\rm corr}
=\frac{I_\xi+(\kappa+\mathcal R_{\rm ret})J_\xi^{\rm num}}
 {d_\xi+J_\xi^{\rm num}}.
\]

The free norms and the proved resolvent expansion give

\[
I_\xi=\frac7{495}\kappa\xi^2+O_L(\kappa\xi^3),\qquad
J_\xi^{\rm num}=\frac{199}{81675}\xi^2+O_L(\xi^3),
\]

where the unsuppressed second-channel contributions are \(1/360\)
and \(1/2700\), respectively. Consequently

\[
\mathcal R_{\rm ret}-\mathcal R_{\rm corr}
=\kappa\xi^2\left(\frac7{495}
+4\frac{199}{81675}\right)+O_L(\kappa\xi^3)
=\frac{1951}{81675}\frac{b^2}{\kappa}
+O_L(b^3/\kappa^2).
\]

The \(1/12\) norm remainder implies actual nonvanishing for sufficiently
small positive \(\xi\): shrinking the proven interval to make
\(C_L\xi<1/24\) gives
\(\|g_\xi\|_\xi^2\geq\kappa^2\xi^2/24>0\).
The exact resolvent form then has \(I_\xi>0\), which makes the improvement
strict without a sign assumption on unknown higher coefficients.

The physical conversions are
\(b^2/\kappa=1/(8g_{\rm YM}^6a)\) and
\(b^3/\kappa^2=1/(32g_{\rm YM}^{10}a)\). The leading difference is
therefore \(1951/(653400g_{\rm YM}^6a)\), with the stated remainder order.
The all-face shift \(2bM\) remains in the ground energy and cancels only
in \(H-E_\xi\).

The resulting inequality is a genuine improved variational upper bound
on the full finite-box gauge-invariant excitation gap. Neither a vanishing
gap nor a continuum result follows from the positive decrease: the trial
quotient approaches \(3\kappa\), the explicit perturbation disk scales as
\(M^{-1}\), and all further bounds are allowed to depend on the box.
The extension is mathematically justified within exactly that scope.
