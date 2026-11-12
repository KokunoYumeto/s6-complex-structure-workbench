# A nonzero quantum elimination correction on two adjacent Wilson plaquettes

8 September 2026. This is an explicit finite interacting calculation, not
a four-dimensional continuum mass-gap result. It evaluates a vacuum-dependent
elimination correction on a genuine gauge-invariant retained observable.

## 1. Original coefficients, graph and operator

Take two adjacent square plaquettes, P and Q, with a single common edge e,
six other distinct edges, and open boundary. This finite cell complex has
seven physical links; no link outside this specified complex is presumed
to have been integrated without its interaction. Choose orientations so
their ordered holonomies, after cyclic changes of their base vertices, are
\[
 P=U_e A,\qquad Q=U_e^{-1}B,
\]
where A and B are the ordered products of the respective three outer links.
Set \(W_P=\operatorname{tr}P\), \(W_Q=\operatorname{tr}Q\). These are real
for SU(2). Each Haar measure has total mass one; the total configuration
space is \(\mathcal Q=SU(2)^7\), with product measure \(d\lambda\).
Use the anti-Hermitian basis \(T_a=i\sigma_a/2\),
\(-2\operatorname{tr}T_aT_b=\delta_{ab}\), and the actual Hamiltonian
\[
 H= -\kappa\sum_{f=1}^7\Delta_f^T
       +b(4-W_P-W_Q),\qquad \kappa>0,\quad b>0.
\]
Every plaquette of this complex is retained. Its relation to the original
action convention \(c=-\operatorname{tr}/2\) is
\[
 \Delta^c=4\Delta^T,\qquad
 \kappa=\frac{2g_{\rm YM}^2}{a},\quad
 b=\frac1{2g_{\rm YM}^2a},\quad
 \xi:=\frac b\kappa=\frac1{4g_{\rm YM}^4}.
\]
Thus the small parameter below is a specified strong-coupling parameter,
not a removal of the interaction at the positive values under study.

The compact elliptic operator H has a unique strictly positive smooth
ground state. One proof is the strictly positive heat kernel for the
product Laplacian and its Feynman--Kac formula with the bounded real
potential. Compactness gives a lowest eigenfunction; replacing it by its
absolute value does not increase its form, and positivity improvement
makes the lowest eigenspace one-dimensional. Gauge transformations commute
with H and preserve positivity, so this ground state is gauge invariant.
Write its unit-L2 representative as \(\psi_\xi\), its eigenvalue as
\(E_\xi\), and \(d\mu_\xi=\rho_\xi d\lambda=\psi_\xi^2d\lambda\).
The unit-L2 convention fixes the state only: all scalar factors below are
retained explicitly.

## 2. Controlled first derivative of the actual vacuum

Let \(H_0=-\sum_f\Delta_f^T\). The exact operator identity is
\[
 H=\kappa[H_0-\xi(W_P+W_Q)]+4bI.
\]
The scalar \(4bI\) is not discarded from H; it changes its ground energy
by exactly 4b and leaves its ground vector and excitation differences
unchanged. The constant function is the simple zero eigenvector of H0,
and the next eigenvalue on the full link Hilbert space is 3/4, from the
spin-1/2 Casimir on one link. On the complex circle \(|z|=3/8\), the
resolvent of H0 has norm at most 8/3. Since \(|W_P+W_Q|\leq4\), its
resolvent Neumann series converges uniformly when \(|\xi|<3/32\).
The Riesz integral therefore gives an analytic rank-one eigenprojection
near zero. For real sufficiently small xi this is the ground projection;
the remainder of the spectrum stays separated by bounded perturbation.

Choose its analytic eigenvector \(\phi_\xi\) with
\(\int\phi_\xi d\lambda=1\). This fixes a representative, not the
physical state norm. Put
\[
 Z_\xi=\int\phi_\xi^2d\lambda,\qquad
 \psi_\xi=\phi_\xi/Z_\xi^{1/2},\qquad
 \rho_\xi=\phi_\xi^2/Z_\xi.
\]
Haar integration of a link appearing once gives \(\int W_P=\int W_Q=0\).
Each plaquette uses four links, each with Casimir 3/4, so
\(H_0W_P=3W_P\) and \(H_0W_Q=3W_Q\). Differentiating the eigen-equation
at xi=0, including its scalar eigenvalue, now gives
\[
 \phi_\xi=1+\frac\xi3(W_P+W_Q)+O(\xi^2),\qquad
 \log\rho_\xi=\frac{2\xi}3(W_P+W_Q)+O(\xi^2).
\]
The remainders hold in every fixed Ck norm. To justify this regularity,
start with the L2 analytic Riesz vector. The eigen-equation expresses H0
applied to that vector as multiplication by a fixed smooth function times
the vector, plus its scalar eigenvalue times the vector. The elliptic
estimate for the product Laplacian gains two Sobolev derivatives at each
iteration. Multiplication by the fixed Wilson polynomial is bounded in
each such Sobolev norm. Iterating also on the differentiated equations
gives analytic dependence in each fixed Sobolev norm; Sobolev embedding
then gives the stated fixed Ck bounds. Strict positivity near 1 permits
the ordinary logarithm with these same local analytic bounds.

The normalization factor is
\(Z_\xi=1+2\xi^2/9+O(\xi^3)\): the linear coefficient has zero mean,
its squared norm is 2/9, and every higher coefficient of phi has zero
mean by the chosen representative. This records rather than hides the
first state-normalization correction.

## 3. Eliminated link and the true conditional score

Let S consist of one outer edge of P which is not in Q, and let R contain
the other six edges. Use lower-case s and r for their configuration
variables. Define the actual marginal and lift
\[
 \rho_{R,\xi}(r)=\int\rho_\xi(s,r)d\lambda_S(s),\qquad Jf(s,r)=f(r).
\]
J is an isometry from \(L^2(\rho_{R,\xi}d\lambda_R)\) into
\(L^2(\mu_\xi)\). Its adjoint is the literal conditional integral
\[
 (J_\xi^*u)(r)=\rho_{R,\xi}(r)^{-1}
             \int u(s,r)\rho_\xi(s,r)d\lambda_S(s).
\]
Put \(P_\xi=JJ_\xi^*\) and \(Q_\xi=I-P_\xi\). These symbols denote
orthogonal Hilbert-space projections, not the two plaquette holonomies.
In particular the formula specifies every dependence of the projection
on the true vacuum.

The ground-state transformed nonnegative operator is
\[
 L_\xi=\psi_\xi^{-1}(H-E_\xi)\psi_\xi
       =-\kappa\sum_{f,a}\rho_\xi^{-1}X_{f,a}(\rho_\xi X_{f,a}).
\]
For a smooth retained function f, direct differentiation and conditional
integration give
\[
 L_\xi Jf=JA_\xi f+B_\xi f,
\]
\[
 A_\xi f=-\kappa\sum_{f'\in R,a}
       \rho_{R,\xi}^{-1}X_{f',a}(\rho_{R,\xi}X_{f',a}f),
\]
\[
 B_\xi f=-\kappa\sum_{f'\in R,a}
 (X_{f',a}\log\rho_\xi-X_{f',a}\log\rho_{R,\xi})X_{f',a}f.
\]
The last function has zero conditional mean, since differentiating the
marginal integral gives
\(J_\xi^*(X\log\rho_\xi)=X\log\rho_{R,\xi}\). Thus it is the actual
component in the eliminated subspace. No independent-link vacuum is used.

Choose the gauge-invariant retained observable
\(f_\xi=W_Q-\mu_\xi(W_Q)\). Haar integration over S annihilates WP
and all its derivatives on R, while leaving WQ unchanged. Therefore
\[
 B_\xi f_\xi=-\frac{2b}{3}\,G+O(b^2/\kappa),\qquad
 G:=\sum_{a=1}^3(X_{e,a}W_P)(X_{e,a}W_Q).
\]
Only the common edge contributes: all other derivatives of the two
plaquettes have disjoint supports. The remainder is in any fixed Sobolev
norm on this finite compact configuration space, at fixed kappa.

## 4. Exact color contraction and two eliminated eigencomponents

Set \(Q'=BU_e^{-1}\). Then trace Q'=trace Q and
\[
 X_{e,a}W_P=\operatorname{tr}(T_aP),\qquad
 X_{e,a}W_Q=-\operatorname{tr}(T_aQ').
\]
The SU(2) Fierz identity in this exact basis is
\[
 \sum_a\operatorname{tr}(T_aC)\operatorname{tr}(T_aD)
 =-\tfrac12[\operatorname{tr}(CD)-\tfrac12\operatorname{tr}C\operatorname{tr}D].
\]
It follows by substituting the three Pauli matrices, or equivalently their
entry identity \(\sum_a(T_a)_{ij}(T_a)_{kl}
=-\tfrac12(\delta_{il}\delta_{jk}-\tfrac12\delta_{ij}\delta_{kl})\).
Let
\[
 R_0=\operatorname{tr}(AB),\quad D_0=W_PW_Q,\quad
 D_1=D_0-\tfrac12R_0.
\]
R0 is the outer six-edge Wilson loop and is independent of the shared edge.
The contraction, with its opposite shared-edge orientation retained, is
\[
 G=\tfrac12R_0-\tfrac14D_0
   =\tfrac38R_0-\tfrac14D_1.
\]
To check all Haar inner products explicitly, for fixed Ue the products
P and Q' are independent Haar SU(2) matrices because A and B are products
of disjoint independent Haar edges. Write
\(P=p_0I+i\sum p_a\sigma_a\), \(Q'=q_0I+i\sum q_a\sigma_a\).
Each p or q is uniform on the unit three-sphere, so
\(\mathbb E p_\alpha p_\beta=\delta_{\alpha\beta}/4\), and the same
holds for q. Direct substitution gives
\[
 G=-\sum_{a=1}^3p_aq_a,\quad
 R_0=2(p_0q_0-\sum_ap_aq_a),\quad
 D_1=3p_0q_0+\sum_ap_aq_a.
\]
Consequently
\[
 \|R_0\|_\lambda^2=1,\qquad \|D_1\|_\lambda^2=\tfrac34,
 \quad\langle R_0,D_1\rangle_\lambda=0,
 \quad\|G\|_\lambda^2=\tfrac3{16}.
\]
Each of the six outer-link Laplacians acts on R0 and D1 by -3/4.
For the common edge, the product rule gives
\[
 \Delta_e^T D_0=-\tfrac32D_0+2G=R_0-2D_0=-2D_1,
 \qquad \Delta_e^T R_0=0.
\]
Therefore
\[
 \kappa H_0R_0=\tfrac{9\kappa}{2}R_0,\qquad
 \kappa H_0D_1=\tfrac{13\kappa}{2}D_1.
\]
Both have zero conditional mean over S, so these are also their
eigenvalues in the eliminated subspace at xi=0. In particular
\[
 B_\xi f_\xi=-\frac b4R_0+\frac b6D_1+O(b^2/\kappa),\qquad
 \|B_\xi f_\xi\|_{\mu_\xi}^2
      =\frac{b^2}{12}+O(b^3/\kappa).
\]
This proves that the eliminated quantum coupling on an actual retained
Wilson observable is nonzero for all sufficiently small positive b/kappa.
It is not a nonzero coupling assumed for an unspecified observable.

## 5. A full-system trial state with a strictly lower excitation energy

Let Cxi be the nonnegative self-adjoint operator associated to the closed
form of Lxi restricted to \(\ker J_\xi^*\). The form domain is the
intersection of that closed subspace with H1. The smooth positive density
and its derivatives are bounded above and below on the compact product.
The explicit conditional integral above is a bounded map on H1; therefore
the domain is closed in the form norm and dense in the eliminated
subspace, by applying Qxi to smooth approximations. This constructs Cxi
without assuming a domain for a formal operator product.

For z>0, define
\[
 w_{\xi,z}=(C_\xi+z)^{-1}B_\xi f_\xi,\qquad
 u_{\xi,z}=\psi_\xi(Jf_\xi-w_{\xi,z}).
\]
All conditional projections, operators and vectors here commute with the
vertex gauge action; hence u is a physical gauge-invariant state. Its
inner product with the vacuum is zero, since f is centered and w has
zero conditional mean. Put
\[
 d_\xi=\|f_\xi\|_{\rho_{R,\xi}}^2,\quad
 a_\xi=\kappa\sum_{f'\in R,a}\mu_\xi(|X_{f',a}f_\xi|^2),
 \quad I_{\xi,z}=\langle B_\xi f_\xi,w_{\xi,z}\rangle,
 \quad J_{\xi,z}=\|w_{\xi,z}\|^2.
\]
I is real and nonnegative. Testing the resolvent equation by w gives
\(\mathfrak c_\xi(w,w)=I_{\xi,z}-zJ_{\xi,z}\). The cross form between
Jf and w is exactly \(\langle B_\xi f,w\rangle\). Expanding the full
form and norm, with their cross terms, gives the exact two Rayleigh values
\[
 \mathcal R_{\rm retained}=\frac{a_\xi}{d_\xi},\qquad
 \mathcal R_{\rm full}(z)=
 \frac{a_\xi-I_{\xi,z}-zJ_{\xi,z}}{d_\xi+J_{\xi,z}},
\]
and the exact decrease
\[
 \mathcal R_{\rm retained}-\mathcal R_{\rm full}(z)
 =\frac{I_{\xi,z}+(z+\mathcal R_{\rm retained})J_{\xi,z}}
        {d_\xi+J_{\xi,z}}>0
\]
whenever Bxi fxi is nonzero. This is a constructed improved vector in the
original seven-link interacting Hilbert space, not an assignment of an
effective classical potential to a quantum energy.

For completeness the expansions of this resolvent as xi tends to zero
are controlled on the fixed compact complex. The densities and their
first derivatives differ from their xi=0 values by O(xi), uniformly.
The conditional integral formula implies
\(P_\xi-P_0=O(\xi)\) both on L2 and on H1. All Pxi have exactly the
same range, the functions of the retained links. Thus
\(P_\xi P_0=P_0\), \(P_0P_\xi=P_\xi\), and consequently
\(Q_0Q_\xi=Q_0\), \(Q_\xi Q_0=Q_\xi\).
On \(\ker P_0\), the map \(T_\xi=Q_\xi|_{\ker P_0}\)
therefore has the exact inverse \(Q_0|_{\ker P_\xi}\).
Both preserve H1 by the conditional integral bounds. This is an exact
identification of the moving form domains, not an assumption that the
conditional projections are independent of xi. After this
identification, the forms Cxi+z are uniformly coercive in H1 and differ
from the xi=0 form by O(xi) in H1 form norm. Subtracting their weak
resolvent equations and using coercivity proves an O(xi) difference of
solution maps from the dual of H1 to H1. Applying this to the already
proved \(B_\xi f_\xi=b(-R_0/4+D_1/6)+O(b\xi)\) justifies, without
an unproved interchange of spectra or projections,
\[
 w_{\xi,z}=-\frac{b}{4(9\kappa/2+z)}R_0
             +\frac{b}{6(13\kappa/2+z)}D_1+O(\xi^2)
\]
at fixed positive kappa and z. The error is in H1 and includes the
variation of the conditional projection and state density.

In particular, with the retained choice z=kappa,
\[
 I_{\xi,\kappa}=\frac{b^2}{\kappa}
           \left(\frac1{88}+\frac1{360}\right)+O(b^3/\kappa^2)
           =\frac{7b^2}{495\kappa}+O(b^3/\kappa^2),
\]
\[
 J_{\xi,\kappa}=\frac{b^2}{\kappa^2}
           \left(\frac1{484}+\frac1{2700}\right)+O(b^3/\kappa^3)
           =\frac{199b^2}{81675\kappa^2}+O(b^3/\kappa^3).
\]
Haar integration gives \(d_0=1\) and \(a_0=3\kappa\); their changes
are O(xi) with the respective retained scales. Substitution in the exact
decrease formula therefore proves the explicit positive coefficient
\[
 \boxed{\mathcal R_{\rm retained}-\mathcal R_{\rm full}(\kappa)
     =\frac{1951}{81675}\frac{b^2}{\kappa}
          +O(b^3/\kappa^2).}
\]
In the original coupling and spatial spacing this coefficient is
\(1951/[653400\,g_{\rm YM}^6a]\), with remainder of order
\(1/(g_{\rm YM}^{10}a)\) in the stated strong-coupling regime.

### 5.1 Absolute excitation energies, not only their difference

The absolute trial-state energies can also be computed to this order. Let
\(F=W_P+W_Q\), and write the mean-one vacuum representative as
\(\phi_\xi=1+\xi F/3+\xi^2\phi_2+O(\xi^3)\). Its eigen-equation and
mean constraint give
\[
 H_0\phi_2=(F^2-2)/3,\qquad \int\phi_2d\lambda=0.
\]
The subtracted 2 is the exact \(\int F^2d\lambda\), not a removed
plaquette. The identity \(W_Q^2=1+\chi_{\rm ad}(Q)\) follows by
\(2\cos\theta\) squared, with
\(\chi_{\rm ad}=1+2\cos2\theta\). The adjoint Casimir is 2 on each
of Q's four links, so \(H_0\chi_{\rm ad}(Q)=8\chi_{\rm ad}(Q)\).
The independent Haar holonomies P and Q satisfy
\[
 \int W_Q^2=1,\qquad\int W_Q^4=2,\qquad
 \int F^2W_Q^2=3,\qquad\int F^2\chi_{\rm ad}(Q)=1.
\]
For the fourth moment, \(W_Q=2q_0\) and the S3 marginal used above gives
\(\int q_0^4=1/8\), either by its beta integral or the corresponding
even moment recurrence. Cross terms vanish by Haar symmetry of P and Q.
Self-adjointness of H0 now yields
\[
 \int\phi_2 W_Q^2d\lambda
 =\int\phi_2\chi_{\rm ad}(Q)d\lambda=\frac1{24}.
\]
Using the full state-density expansion, including Zxi,
\[
 \rho_\xi=1+\frac{2\xi}3F
     +\xi^2\left(\frac{F^2}{9}+2\phi_2-\frac29\right)+O(\xi^3),
\]
therefore gives
\[
 r_\xi:=\mu_\xi(W_Q^2)=1+\frac7{36}\xi^2+O(\xi^3),\qquad
 \mu_\xi(W_Q)=\frac23\xi+O(\xi^2),
\]
\[
 d_\xi=r_\xi-\mu_\xi(W_Q)^2=1-\frac14\xi^2+O(\xi^3).
\]
For a single edge of the SU(2) loop,
\(\sum_a|X_{e,a}W_Q|^2=(4-W_Q^2)/4\), by the displayed Pauli
coordinates. Summing its four edges gives exactly
\(a_\xi=\kappa(4-r_\xi)\). Hence the absolute excitation Rayleigh
values relative to the same actual vacuum are
\[
 \boxed{\mathcal R_{\rm retained}
    =3\kappa+\frac59\frac{b^2}{\kappa}+O(b^3/\kappa^2),}
\]
\[
 \boxed{\mathcal R_{\rm full}(\kappa)
    =3\kappa+\frac{43424}{81675}\frac{b^2}{\kappa}
         +O(b^3/\kappa^2).}
\]
The latter coefficient is precisely
\(5/9-1951/81675=43424/81675\). The elimination correction decreases
the variational energy at the same positive coupling, but both trial
energies increase from their common zero-b value to this order. Neither
the decrease nor the positive second-order coefficients determine the
full spectrum or a limiting four-dimensional gap.

For completeness the energy origin is explicit as well. Taking the Haar
mean of the second-order eigen-equation gives
\(e(\xi)=-2\xi^2/3+O(\xi^3)\). The actual, unsubtracted Hamiltonian
therefore has vacuum energy
\[
 E_\xi=4b-\frac{2b^2}{3\kappa}+O(b^3/\kappa^2).
\]
Adding this same scalar to each excitation quotient gives the two trial
quotients for H itself:
\[
 3\kappa+4b-\frac19\frac{b^2}{\kappa}+O(b^3/\kappa^2),\qquad
 3\kappa+4b-\frac{11026}{81675}\frac{b^2}{\kappa}
       +O(b^3/\kappa^2),
\]
respectively. The mass-gap question concerns energies above the vacuum,
so the preceding excitation quotients, not this common scalar shift,
are the quantities used in the variational comparison.

## 6. Meaning and sources

The correction is already present in a nonlinear gauge-invariant quantum
calculation: it comes from covariance between a retained loop and the
eliminated link through their common plaquette edge. Its two explicit
Casimir channels, 9kappa/2 and 13kappa/2, supply the coefficient above.
The improved state still has an excitation Rayleigh value near 3kappa in
this regime. No small-energy continuum state or four-dimensional quantum
mass-gap disproof is inferred from this finite-complex result.

The exact general marginal, resolvent and trial-state identities are
proved in the companion source `spatial_vacuum_elimination.tex`; the
calculation above evaluates its nonzero coupling rather than assuming it.
The original coefficient dictionary is proved from the temporal Wilson
integral in `temporal_transfer.tex`. The compact-ground-state and Fierz
identities are expanded in `wilson_finite_lattice.tex`.

The general elimination method is established literature, not claimed as
a new discovery: G. Dusson, I. M. Sigal and B. Stamm,
*The Feshbach–Schur map and perturbation theory*, pp. 65–88 (2021),
<https://doi.org/10.4171/ECR/18-1/5>,
<https://arxiv.org/abs/2105.02058>.
The lattice Hamiltonian context is J. Kogut and L. Susskind,
*Hamiltonian formulation of Wilson's lattice gauge theories*,
Physical Review D 11 (1975), 395–408,
<https://doi.org/10.1103/PhysRevD.11.395>.
