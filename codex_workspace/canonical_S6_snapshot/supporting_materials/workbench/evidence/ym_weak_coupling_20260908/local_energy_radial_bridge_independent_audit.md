# Compact local energy, radial electric observables, and a full-mode low-energy lower bound

8 September 2026.

The compact local-energy state and the global radial electric observable admit an exact finite-regulator double-commutator relation and an exact common lowest-mode quadratic representation. Their different raw powers are computed below with the original coefficients and measures. For a nonnegative nonzero compact profile, a growing family of the original transverse modes then gives a strictly positive lower bound for the unprojected local-energy spectral weight in every window \((0,\epsilon)\), \(\epsilon>0\). A specified refinement of the positive-coupling diagonal transfers that bound to the nonlinear finite-box Hamiltonians. These statements do not identify an interacting continuum theory or verify a Navier--Stokes singularity.

## 1. Original objects and operator domains

Vertices remain the integer points of \(\{-L,\ldots,L\}^3\), with all positively oriented links whose endpoints belong to this cube and all its elementary faces. Physical coordinates are \(x=an\), edge midpoints are \(am(e)\), and
\[
 N=2L+1,\qquad \ell=aN.
\]
The endpoint distance in each coordinate is \(2La=\ell-a\). No formula below replaces this distance by \(\ell\); the latter is the length appearing in the exact open difference basis.

On product Haar probability measure, with \(T_\alpha=-i\sigma_\alpha/2\) and the original left fields \(X_{e,\alpha}\), retain
\[
 E_e=-\sum_{\alpha=1}^3X_{e,\alpha}^2,\qquad
 H=\kappa\sum_eE_e+b\sum_p(2-\operatorname{tr}U_p),\qquad
 \kappa=\frac{2g^2}{a},\quad b=\frac1{2g^2a}.
\tag{A1}
\]
The complete Wilson scalar is \(2b|\mathsf P_L|\). The physical Hilbert space is the vertex-gauge invariant subspace, with the full residual simultaneous colour rotation constraint after the exact rooted-tree quotient. The two source gauge conventions are identical under \(k_v=h_v^{-1}\), with the identity map on link configurations and wavefunctions.

The Hamiltonian has domain \(H^2\) and form domain \(H^1\) on the compact product group, restricted to the invariant subspace. Its positive unit vacuum is \(\psi_g\), its energy is \(\mathcal E_g\), and its excitation operator is \(A_g=H-\mathcal E_g\). For real edge weights,
\[
 f_p=\frac14\sum_{e\in\partial p}f_e,\qquad
 D_f=\kappa\sum_ef_eE_e+b\sum_pf_p(2-\operatorname{tr}U_p),
 \quad C_{g,f}=D_f-\langle D_f\rangle_{\psi_g},\quad
 \Xi_f=C_{g,f}\psi_g.
\tag{A2}
\]
The self-adjoint domain of the signed kinetic sum is its Peter--Weyl diagonal domain: the squared coefficients times
\(\kappa^2(\sum_e f_ej_e(j_e+1))^2\) must be summable. It need not be \(H^2\). Adding the bounded real Wilson multiplier preserves this domain. Smooth physical functions belong to it and are preserved by every operator in the commutator identities below. Thus those identities have a specified common domain without an assertion that every signed \(D_f\) is elliptic.

The comparison oscillator uses all transverse modes and all three colours:
\[
 H_{\rm osc}=\frac1a\sum_{\nu,\alpha}
 \left(-2\partial_{z_{\nu,\alpha}}^2+
       \frac{\sigma_\nu^2z_{\nu,\alpha}^2}{8}\right),\qquad
 A_0=\sum_{\nu,\alpha}\frac{\sigma_\nu}{a}
                         a_{\nu,\alpha}^\dagger a_{\nu,\alpha}.
\tag{A3}
\]
The tree, Haar-density, dilation and constant-Jacobian linear-coordinate maps are the source isometries, not replacements of the counting or Haar measures. Colour-contracted creation pairs are invariant under the residual gauge group.

Let \(V\) be an orthonormal transverse edge eigenbasis and
\(Y=d_1V\Sigma^{-1}\), \(\Sigma=\operatorname{diag}(\sigma_\nu)\). Both \(V\) and \(Y\) are isometries for the original counting inner products. Define
\[
 A^f=V^{\mathsf T}\operatorname{diag}(f_e)V,\qquad
 F^f=Y^{\mathsf T}\operatorname{diag}(f_p)Y.
\]
The source full matrices can equivalently be written
\[
 \mathsf R_f=\Sigma^{1/2}(F^f-A^f)\Sigma^{1/2},\qquad
 \mathsf Q_f=\Sigma^{1/2}(F^f+A^f)\Sigma^{1/2}.
\tag{A4}
\]
In particular both electric and magnetic contributions remain in \(\mathsf R_f\). For constant \(f\), \(F^f=A^f=fI\), and its vacuum creation matrix vanishes exactly, as required by \(D_f=fH\).

## 2. Compact-support powers and constants

Retain \(L_j=j^2\), \(a_j=1/(100j)\), \(N_j=2j^2+1\), and
\[
 \ell_j=\frac{2j^2+1}{100j},\quad
 \sigma_j=\sqrt8\sin\frac{\pi}{2N_j},\quad
 \Delta_j=\frac{2\sigma_j}{a_j},\quad
 \frac{\ell_j\sigma_j}{a_j}\longrightarrow\sqrt2\pi,\quad
 \frac{\ell_j}{j}\longrightarrow\frac1{50}.
\tag{A5}
\]
For \(h\in C_c(\mathbb R^3;\mathbb R)\), let
\(f_{h,j}(e)=h(a_jm(e))\), with the full quarter-face average, and put
\[
 H_h=\int h(x)\,dx,\qquad H_{h,ik}=\int x_ix_kh(x)\,dx.
\]
The three source lowest modes \(V_i\) have the original cyclic signs. On the face plane normal to \(i\), their unit curls obey exactly
\[
 Y_i(n)^2=\frac4{N_j^3}
 \cos^2\frac{\pi a_j(n_p+1/2)}{\ell_j}
 \cos^2\frac{\pi a_j(n_q+1/2)}{\ell_j}.
\tag{A6}
\]
Different \(Y_i\) have disjoint face-plane supports. A face-center Riemann sum therefore gives
\[
 \ell_j^3F^h_{ii}\longrightarrow4H_h,\qquad F^h_{ik}=0\ (i\ne k).
\tag{A7}
\]
The face weight differs from the value at its center by at most the modulus of continuity of \(h\) at \(a_j/2\). Its support is enlarged by at most that distance. Multiplication by the number of nonzero samples and by \(a_j^3\) bounds this error by a constant times that modulus. The limiting cosine factors are uniformly one on that enlarged compact support. These statements justify (A7) with the open endpoint grids and the quarter-face average intact.

The two electric directional squares for \(V_i\) each have coefficient \(2/N_j^3\), one cosine square and one sine square. The same Riemann argument, using
\(\ell_j\sin(\pi x/\ell_j)\to\pi x\) uniformly on a compact set, proves the additional exact leading electric moments
\[
 \ell_j^5 A^h_{ii}\longrightarrow
 2\pi^2\int(x_p^2+x_q^2)h(x)\,dx.
\tag{A8}
\]
For \(i\ne k\), only the remaining edge direction is shared. The original product is negative:
\[
 V_i(n,d)V_k(n,d)=-\frac2{N_j^3}
 \sin\frac{\pi a_jn_i}{\ell_j}
 \sin\frac{\pi a_jn_k}{\ell_j}
 \cos^2\frac{\pi a_j(n_d+1/2)}{\ell_j}.
\]
Consequently
\[
 \ell_j^5A^h_{ik}\longrightarrow-2\pi^2H_{h,ik}.
\tag{A9}
\]
Since the lowest frequencies coincide, (A4) gives the exact identities
\(\mathsf R_h^{\min}=\sigma_j(F^h-A^h)\) and
\(\mathsf Q_h^{\min}=\sigma_j(F^h+A^h)\). Combining (A5)--(A9) proves
\[
 \frac{\ell_j^4}{a_j}\mathsf R_h^{\min},\quad
 \frac{\ell_j^4}{a_j}\mathsf Q_h^{\min}
 \longrightarrow4\sqrt2\pi H_h I_3,
\qquad
 \frac{\ell_j^6}{a_j}(\mathsf R_h^{\min})_{ik}
 \longrightarrow2\sqrt2\pi^3H_{h,ik}\ (i\ne k).
\tag{A10}
\]
The leading compact-support contribution in (A10) is magnetic. The electric term is present and has its explicit two-power smaller contribution (A8)--(A9). Its smallness for these global lowest modes does not say that local electric observables vanish on all modes.

For a symmetric lowest-mode matrix \(B\), retain the raw vector
\[
 \Phi(B)=\sum_{i,k,\alpha}B_{ik}
     a_{i,\alpha}^\dagger a_{k,\alpha}^\dagger\Phi_0,
 \qquad \langle\Phi(B),\Phi(E)\rangle=6\operatorname{tr}(B^*E).
\tag{A11}
\]
The source lowest-band vector is \(\Phi(\mathsf R_h^{\min}/(4a_j))\). Its raw mass is exactly
\[
 d_{L_j,a_j}(f_{h,j})=\frac3{8a_j^2}
                      \operatorname{tr}((\mathsf R_h^{\min})^2).
\]
Thus
\[
 \ell_j^8d_{L_j,a_j}(f_{h,j})\longrightarrow36\pi^2H_h^2.
\tag{A12}
\]
The source actual Gram frame has \(G_{g_j}\to I\) and the chosen error is smaller than every amplification used here. Hence for its actual projected state \(v_{h,j}=P_{g_j}\Xi_{f_{h,j}}\),
\[
 \ell_j^4M_{g_j}^{-1}v_{h,j}\longrightarrow
 (0,\sqrt2\pi H_h I_3),\quad
 \ell_j^8\|v_{h,j}\|^2\longrightarrow36\pi^2H_h^2.
\tag{A13}
\]
Its raw mass tends to zero. Its raw first moment, keeping the original physical Hamiltonian, satisfies
\[
 \ell_j^9\langle v_{h,j},A_{g_j}v_{h,j}\rangle
 \longrightarrow72\sqrt2\pi^3H_h^2.
\tag{A14}
\]
The finite-band energy is \(\Delta_j\), up to the stipulated error; \(\ell_j\Delta_j\to2\sqrt2\pi\). Therefore fixed physical-time correlations have the rescaled limit \(36\pi^2H_hH_k\), and at \(t=\ell_j\theta\) they acquire the factor \(e^{-2\sqrt2\pi\theta}\). These are precisely the source powers. No division of a state by its norm is involved.

When \(H_h=0\), (A12) has zero right side; it supplies no positive leading mass. The mixed moments (A9)--(A10), the other moments (A8), and the full matrices are still retained. In particular vanishing integral does not imply that \(\Xi_f\) is zero.

The coefficients in source (144)--(145) also agree with its frame and metric. In particular
\(\operatorname{tr}S_*=337/64\) and
\(\operatorname{tr}B_*=-8425\sqrt2/(32\pi)\) give
\(6\sqrt2\pi H_h\operatorname{tr}B_*=-25275H_h/8\).
These equations concern \(w_j=P_{g_j}\Xi_{f_{S_j}}\), defined in source (127). They do not compute the expectation in the unprojected vector \(\Xi_{f_{S_j}}\), although the weight retains the entire original material tensor.

## 3. Exact finite-regulator relation to the radial electric observable

For a selected original lowest mode \(i\), let \(Q_{g,i}=g^{-2}F_i\) be the Section 22 cutoff quadratic. It is a globally smooth bounded gauge-invariant multiplier for every fixed \(g>0,L,a\). Define
\[
 R_{g,i}=\frac12[Q_{g,i},[A_g,Q_{g,i}]]
        =\kappa\sum_{e,\alpha}(X_{e,\alpha}Q_{g,i})^2.
\tag{A15}
\]
Every derivative of the cutoff remains in the right side. The full Wilson multiplication commutes with \(Q_{g,i}\); this explains its zero commutator without removing it from \(A_g\).

There is an exact weighted version involving the unchanged full local energy:
\[
 \boxed{\frac12[Q_{g,i},[D_f,Q_{g,i}]]
       =\kappa\sum_{e,\alpha} f_e(X_{e,\alpha}Q_{g,i})^2
       =:R_{g,i;f}.}
\tag{A16}
\]
For its proof, on a smooth physical function \(u\),
\[
 [E_e,Q]u=-\sum_\alpha\{(X_{e,\alpha}^2Q)u
                    +2(X_{e,\alpha}Q)X_{e,\alpha}u\}.
\]
Commuting \(Q\) with this expression leaves precisely
\(2\sum_\alpha(X_{e,\alpha}Q)^2u\). Multiplication by \(\kappa f_e/2\) and summation proves (A16). The magnetic term in (A2) commutes with \(Q\) exactly. The right side extends to a bounded multiplier at each fixed regulator. For \(f_e\ge0\), it is nonnegative; for arbitrary real weights,
\[
 |R_{g,i;f}|\le\|f\|_\infty R_{g,i}
\tag{A17}
\]
as a pointwise inequality of functions. This supplies an exact relation on the original physical Hilbert space before any projection or limit.

The cutoff is a configuration-space cutoff in all chord logarithms. It is not a compact physical-space support condition. The selected transverse cochain is global; taking a derivative square does not by itself convert this phase coordinate into a local field. Conversely (A16) gives its exact local energy-weighted derivative distribution, so global dependence is not a claim of unrelatedness.

At fixed box the Section 22 tail proof gives, with the cutoff and its derivative terms retained,
\[
 \mathcal B_g(R_{g,i}^m\psi_g)\longrightarrow
 (\lambda q_i)^m\Phi_0,\qquad
 \lambda=\frac{2\sigma}{a},\quad q_i=\frac\sigma4|z_i|^2.
\tag{A18}
\]
It uses the global bound \(S\le C_SW\), all actual vacuum moments of \(W/g^2\), and the weighted chart-tail inequality; its constants depend on the fixed box and cutoff. It is not a volume-uniform estimate.

The same explicit tangent metric computation and (A17) give the fixed-box weighted limit
\[
 R_{g,i;f}\quad\leadsto\quad A^f_{ii}\lambda q_i
\tag{A19}
\]
on the vacuum, with strong transport of this multiplier times the vacuum. Indeed \(\nabla q_i=(\sigma/2)z_i\) in the selected kinetic mode, the weighted tangent Gram entry is \(A^f_{ii}\), and the unchanged kinetic coefficient is \(2/a\). Their product is
\((2/a)(\sigma^2/4)A^f_{ii}|z_i|^2=A^f_{ii}\lambda q_i\).
The tails follow by (A17) and the already proved tails of \(R_{g,i}\psi_g\). For compact \(h\), (A8) specifies the \(\ell^{-5}\) factor in this weighted radial distribution. That factor differs from the leading full local-energy factor because (A16) measures the electric phase-gradient contribution, whereas (A2) includes the magnetic energy as well.

## 4. Exact oscillator bridge, including its raw vacuum image

This section proves an operator relation before taking the compact-support asymptotic. It is confined to the common lowest-mode oscillator factor and its projection; it is not an assertion about arbitrary full operator words.

Let \(B\) be any real symmetric \(3\)-by-\(3\) matrix and define on the three lowest modes
\[
 q_B=\frac\sigma4\sum_\alpha z_\alpha^{\mathsf T}Bz_\alpha,
 \qquad \mathcal N_B=\sum_{i,k,\alpha}B_{ik}
                         a_{i,\alpha}^\dagger a_{k,\alpha}.
\]
The polynomial multiplier \(q_B\) has expectation
\(\langle q_B\rangle=(3/2)\operatorname{tr}B\).
On the invariant Schwartz core, the creation formulas give
\[
 \lambda\left(q_B-\frac32\operatorname{tr}B\right)
 =\frac\sigma a\sum_{i,k,\alpha}B_{ik}
       (a_{i,\alpha}a_{k,\alpha}
          +a_{i,\alpha}^\dagger a_{k,\alpha}^\dagger)
   +\frac{2\sigma}a\mathcal N_B.
\tag{A20}
\]
For signed \(B\), this is the equality of the indicated polynomial operators on that core; no positivity of \(B\) is assumed. The multiplier has its maximal multiplication domain. The finite-mode creation expressions are well-defined on every polynomial times Gaussian used below.

Let \(C^{\rm low}_{0,f}\) mean the terms in the source full centered oscillator whose two mode indices both belong to the three lowest modes. With the entire full vacuum scalar already subtracted, the exact identity is
\[
 \boxed{
 C^{\rm low}_{0,f}
 =\frac14\lambda\left(q_{F^f-A^f}
                 -\frac32\operatorname{tr}(F^f-A^f)\right)
       +\frac\sigma a\mathcal N_{A^f}.}
\tag{A21}
\]
Here \(F^f,A^f\) denote their lowest blocks. To prove it, the pair coefficient from (A20) is
\(\sigma(F^f-A^f)/(4a)\), and the number coefficient is
\(\sigma(F^f-A^f)/(2a)+\sigma A^f/a
 =\sigma(F^f+A^f)/(2a)\).
These are exactly source (134), with \(\mathsf R=\sigma(F-A)\) and \(\mathsf Q=\sigma(F+A)\). Thus (A21) has retained both contributions and the number-preserving term.

Terms with indices outside these three modes vanish after compression on both sides to vacuum plus the lowest band; their uncompressed action is the source higher-mode map (147)--(148). In particular \(\mathcal N_{A^f}\Phi_0=0\), so the exact lowest-band vacuum state is already the radial quadratic image
\[
 P_{\min}C_{0,f}\Phi_0
 =\frac14\lambda\left(q_{F^f-A^f}
             -\frac32\operatorname{tr}(F^f-A^f)\right)\Phi_0.
\tag{A22}
\]
Every such symmetric quadratic is a real linear combination of single-mode radial quadratics: an orthogonal eigenbasis \(b_r\) of its coefficient matrix gives
\(q_B=\sum_r\beta_r(\sigma/4)|\sum_i(b_r)_iz_i|^2\).
This is a proved map within the degenerate lowest transverse space, preserving the three colour coordinates and the displayed raw coefficients.

For the compact weights, (A7)--(A9) imply on the finite vacuum-plus-band space
\[
 \ell_j^4C^{\rm comp}_{0,h,j}
 -H_h\ell_j\sum_{i=1}^3
     \left(R^{\rm comp}_{0,i}-\langle R_{0,i}\rangle\right)
 \longrightarrow0,
 \qquad R_{0,i}=\lambda_jq_i.
\tag{A23}
\]
Indeed the leading coefficient of \(F^h-A^h\) is
\(4H_h\ell_j^{-3}I\); the factor \(1/4\) in (A21) cancels this four. The number correction has size
\(\ell_j^4(\sigma_j/a_j)O(\ell_j^{-5})=O(\ell_j^{-2})\).
The remaining matrix error tends to zero by (A7) and
\(\ell_j\lambda_j\to2\sqrt2\pi\). The same proof applies to every component of the finite compressed operator, not only its vacuum vector.

Write
\[
 \mathcal K=\mathbb C\oplus\operatorname{Sym}_3(\mathbb C),\qquad
 \langle(c,B),(d,E)\rangle=\overline c d+6\operatorname{tr}(B^*E),
 \quad E_{ii}=\text{the matrix unit},\quad c_\Gamma=100\sqrt2\pi.
\]
The limiting compressed centered radial operator associated to \(jR_{g,i}\), whenever all relevant finite-box tests are included on the same diagonal, is
\[
 \mathcal R_i(c,B)=c_\Gamma\left(
       3B_{ii},\ \frac c2E_{ii}+E_{ii}B+BE_{ii}\right).
\tag{A24}
\]
Its vacuum creation coefficient is \(c_\Gamma E_{ii}/2\). Pair annihilation contributes \(3c_\Gamma B_{ii}\) because of the factor-six inner product (A11); the number commutator gives the final two terms. Consequently the source compact operator has the precise relation
\[
 \boxed{\mathcal T_h=\frac{H_h}{50}\sum_{i=1}^3\mathcal R_i,
 \qquad
 \mathcal T_h(c,B)=\sqrt2\pi H_h(6\operatorname{tr}B,cI_3+4B).}
\tag{A25}
\]
The coefficient \(1/50\) is the actual limit \(\ell_j/j\). Formula (A25) would have a wrong coefficient if \(a_j\), \(N_j\), or the amplitude \(jR_g\) were replaced without recording that change.

Section 22 explicitly writes one selected radial mode. Formula (A25) uses the three exact lowest modes. Each of the other two cutoff quadratics is defined by (279) with its corresponding selected row of the same orthogonal mode matrix. The fixed-box cutoff, potential-moment and finite spectral arguments apply separately to these two smooth invariant functions. There are only three functions at a fixed stage. Their proved tests, the source compact-energy tests, and mixed finite-frame tests can therefore be included together in a refined positive dyadic sequence. This is not a claim that either earlier least-dyadic choice already satisfies their union.

For one selected mode, \(q_i\) has Gamma law with shape \(k=3/2\), so its centered raw vacuum mass is
\[
 \|(R_{0,i}-\langle R_{0,i}\rangle)\Phi_0\|^2
   =\frac32\lambda_j^2,
 \qquad
 \|j(R_{0,i}-\langle R_{0,i}\rangle)\Phi_0\|^2
   \longrightarrow\frac32c_\Gamma^2=30000\pi^2.
\tag{A26}
\]
The three centered radial vectors are orthogonal, since the oscillator factors are independent and each is centered. Thus their summed limiting mass is \(90000\pi^2\). Multiplying by \((H_h/50)^2\) gives \(36\pi^2H_h^2\), exactly (A12), and verifies the raw-mass compatibility of (A25). The mixed limiting Gram entry for one radial mode is
\[
 6\operatorname{tr}\left((\sqrt2\pi H_hI_3)^*
                                      \frac{c_\Gamma}2E_{ii}\right)
 =600\pi^2H_h.
\tag{A27}
\]
On an actual common refined diagonal this is the limit of
\(\ell_j^4\langle P_{g_j}\Xi_{f_{h,j}},
 j(R_{g_j,i}-\langle R_{g_j,i}\rangle)\psi_{g_j}\rangle\),
once its finite-frame and weighted-vector tests are included. The unprojected radial vector may have a small remainder at each fixed coupling; the fixed-box strong limit and included mixed tests control that remainder. No unsupported rate on the earlier diagonal is used.

The radial centered vacuum vector tends spectrally to a positive atom at zero after multiplication by \(j\), while its high-amplitude phase-carrier family has the continuous Gamma excitation limit. Those are two explicitly different state images of the same multiplier and phase construction. Neither is identical to the compact local energy state without the maps and factors in (A21)--(A27).

## 5. A full-mode low-energy calculation from the actual open-box matrices

The full comparison raw spectral measure of the unprojected compact-energy state is
\[
 \nu_{h,0,j}
 =\frac3{8a_j^2}\sum_\mu (\mathsf R_h)_{\mu\mu}^2
                         \delta_{2\sigma_\mu/a_j}
 +\frac3{4a_j^2}\sum_{\mu<\nu}(\mathsf R_h)_{\mu\nu}^2
                         \delta_{(\sigma_\mu+\sigma_\nu)/a_j}.
\tag{A28}
\]
For any Borel energy set \(I\), the equivalent ordered sum is
\[
 \nu_{h,0,j}(I)=\frac38\sum_{\mu,\nu}
 \frac{\sigma_\mu\sigma_\nu}{a_j^2}
 \left[
   \sum_pf_{h,j}(p)Y_\mu(p)Y_\nu(p)
  -\sum_ef_{h,j}(e)V_\mu(e)V_\nu(e)
 \right]^2
 \mathbf1_I\left(\frac{\sigma_\mu+\sigma_\nu}{a_j}\right).
\tag{A29}
\]
This finite sum includes every original transverse mode and both terms before squaring. Restricting the two indices gives a valid lower bound because each summand is nonnegative. An orthogonal change of basis inside a degenerate frequency space preserves this ordered Hilbert--Schmidt sum and the energy test. Thus one may choose the explicit transverse eigenvectors below and extend them to the complete eigenbasis without changing the full quantity.

Here is an evaluated lower bound for (A29), rather than only a proposed spectral test. It applies to any fixed nonnegative nonzero \(h\in C_c(\mathbb R^3)\). Put \(H_h=\int h>0\). Choose \(R\ge1\) so that \(\operatorname{supp}h\subset[-R+1,R-1]^3\), increasing \(R\) if necessary, and fix any \(\epsilon>0\). Define
\[
 \delta=\min\left\{\frac\epsilon{4\sqrt3},\frac1{1000R}\right\}>0.
\tag{A30}
\]
All inequalities below hold for all sufficiently large \(j\), with this fixed \(h,R,\epsilon,\delta\).

### 5.1. Exact mode family and its gauge constraint

For \(1\le m\le N-1\), define the full open one-dimensional basis
\[
 v_m(n)=\sqrt{\frac2N}\cos\left(\frac{\pi m}2+\frac{\pi mn}N\right),
 \quad -L\le n\le L,
\]
\[
 w_m(n)=-\sqrt{\frac2N}\sin\left(\frac{\pi m}2+
                                      \frac{\pi m(n+1/2)}N\right),
 \quad -L\le n<L,
 \qquad s_m=2\sin\frac{\pi m}{2N}.
\tag{A31}
\]
Here are the complete difference and counting-inner-product checks. Set \(u=n+L\) and \(\theta_m=\pi m/N\). The vertex expression becomes \(\sqrt{2/N}\cos(\theta_m(u+1/2))\), while the edge expression is \(-\sqrt{2/N}\sin(\theta_m(u+1))\). The cosine subtraction identity therefore gives \(dv_m=s_mw_m\). At an interior vertex,
\[
 (d^*w_m)(u)=w_m(u-1)-w_m(u)
 =2\sqrt{2/N}\sin(\theta_m/2)\cos(\theta_m(u+1/2))
 =s_mv_m(u).
\]
At the first vertex \((d^*w_m)(0)=-w_m(0)=\sqrt{2/N}\sin\theta_m=s_mv_m(0)\); at the last vertex
\((d^*w_m)(N-1)=w_m(N-2)=(-1)^m\sqrt{2/N}\sin\theta_m=s_mv_m(N-1)\). These retain both open endpoint terms.

The finite geometric identities
\[
 \sum_{u=0}^{N-1}\cos((u+1/2)\theta)
 =\frac{\sin(N\theta)}{2\sin(\theta/2)},
\qquad
 \sum_{v=1}^{N-1}\cos(\pi r v/N)
 =-\frac{1+(-1)^r}{2}
\tag{A31a}
\]
hold respectively when the displayed denominator is nonzero and when \(r\) is a nonzero integer with \(|r|<2N\). For the first, multiply the sum of \(e^{i(u+1/2)\theta}\) by \(1-e^{i\theta}\) and take real parts. For the second, sum \(e^{i\pi rv/N}\) from \(v=0\) to \(N-1\), take real parts, and subtract the \(v=0\) term; even \(r\) gives \(-1\), and odd \(r\) gives zero. The vertex cosine product identity with \(r=m-n,m+n\) now proves orthogonality for distinct \(m,n\) and squared norm one for each \(v_m\). In the equal-index case the constant part sums to \(N/2\) and the \(r=2m\) part vanishes. For the edges, use
\(2\sin A\sin B=\cos(A-B)-\cos(A+B)\): for distinct \(m,n\), the two sums in (A31a) cancel because \(m-n\) and \(m+n\) have the same parity; for equal indices the sum is \(((N-1)-(-1))/2=N/2\). Thus every \(w_m\) also has squared counting norm one. The vertex function \(v_0=N^{-1/2}\) is orthogonal to every \(v_m\) by the first identity. The \(N\) vertex and \(N-1\) edge functions are consequently complete orthonormal bases by their respective dimensions. At \(m=1\), (A31) is exactly the source signed pair \(v_1=-\sqrt{2/N}\sin(\pi n/N)\), \(w_1=-\sqrt{2/N}\cos(\pi(n+1/2)/N)\).

Select triples \(\mathbf m=(m_1,m_2,m_3)\) such that
\[
 m_1\equiv0\pmod4,\quad m_2\equiv m_3\equiv1\pmod4,\qquad
 \frac\delta2\le p_r:=\frac{\pi m_r}{\ell_j}\le\delta
 \quad(r=1,2,3).
\tag{A32}
\]
Write \(s_r=s_{m_r}\), \(t_{\mathbf m}=\sqrt{s_2^2+s_3^2}\), and
\(\sigma_{\mathbf m}=\sqrt{s_1^2+s_2^2+s_3^2}\). Define a cochain with the three original edge directions by
\[
 (V_{\mathbf m})_1=0,\quad
 (V_{\mathbf m})_2=\frac{s_3}{t_{\mathbf m}}v_{m_1}w_{m_2}v_{m_3},
 \quad
 (V_{\mathbf m})_3=-\frac{s_2}{t_{\mathbf m}}v_{m_1}v_{m_2}w_{m_3}.
\tag{A33}
\]
The factors are evaluated on their respective original vertex or edge grids. Its divergence is zero because the two terms are
\((s_2s_3/t_{\mathbf m})v_{m_1}v_{m_2}v_{m_3}\) and its negative. Its squared counting norm is
\((s_3^2+s_2^2)/t_{\mathbf m}^2=1\). Distinct triples are orthogonal by the tensor basis orthogonality. To check its eigenvalue, for one fixed positive index triple write \(e_r\) for the tensor edge cochain with the factor \(w_{m_r}\) in direction \(r\) and the other two vertex factors. The curl of \(\sum_rb_re_r\) has plane-\(rs\) coefficient \(s_rb_s-s_sb_r\). Expanding its squared norm gives
\[
 \sum_{r<s}|s_rb_s-s_sb_r|^2
 =\left(\sum_rs_r^2\right)\left(\sum_r|b_r|^2\right)
                       -\left|\sum_rs_rb_r\right|^2.
\tag{A33a}
\]
The relations \(dv_m=s_mw_m\) and \(d^*w_m=s_mv_m\) show that \(d_1\) and \(d_1^*\) preserve this same tensor-index block between edge and face components. Polarization therefore identifies the complete block of \(d_1^*d_1\) as \(|s|^2I-ss^{\mathsf T}\). The coefficient vector in (A33) is \((0,s_3/t_{\mathbf m},-s_2/t_{\mathbf m})\), whose dot product with \(s\) is zero. Hence
\(d_1^*d_1V_{\mathbf m}=\sigma_{\mathbf m}^2V_{\mathbf m}\), with the asserted actual frequency.
Explicitly, the three positively ordered face components are
\[
 (d_1V_{\mathbf m})_{23}=-t_{\mathbf m}v_{m_1}w_{m_2}w_{m_3},
\]
\[
 (d_1V_{\mathbf m})_{12}=\frac{s_1s_3}{t_{\mathbf m}}w_{m_1}w_{m_2}v_{m_3},
 \qquad
 (d_1V_{\mathbf m})_{13}=-\frac{s_1s_2}{t_{\mathbf m}}w_{m_1}v_{m_2}w_{m_3}.
\tag{A34}
\]
These also give its curl squared norm \(\sigma_{\mathbf m}^2\). The cochain is therefore an actual transverse mode. Its two-quantum colour-contracted creation states in (A28) satisfy the residual gauge constraint: simultaneous orthogonal rotation of the three creation-operator colour indices leaves their contracted sum unchanged.

### 5.2. Signs and lower bounds before the electric--magnetic subtraction

Put \(c_N=\sqrt{2/N}\). The congruences in (A32) preserve definite original trigonometric signs:
\[
 v_{m_1}=c_N\cos(p_1x_1),\quad w_{m_1}=-c_N\sin(p_1x_1),
\]
\[
 v_{m_r}=-c_N\sin(p_rx_r),\quad w_{m_r}=-c_N\cos(p_rx_r)
 \quad(r=2,3).
\tag{A35}
\]
Here \(x_r\) is the appropriate physical vertex or midpoint coordinate in each factor. For all edges or faces with nonzero weight, \(|x_r|\le R\) once \(a_j<1\); the enlarged face support is included by the margin in the definition of \(R\). Hence \(|p_rx_r|\le\delta R\le1/1000\). In particular every cosine is at least \(1/2\), and the sign of every sine is the sign of \(x_r\).

It follows directly from (A34)--(A35) that for any two selected triples \(\mu,\nu\),
\[
 Y_\mu(p)Y_\nu(p)\ge0
\tag{A36}
\]
on every weighted face, in all three face planes. On plane 23 the two curls are negative multiples of products of three positive cosines. On plane 12 their signs are both minus the sign of \(x_1x_3\); on plane 13 their signs are both the sign of \(x_1x_2\). This proves (A36) even when the support crosses a coordinate plane.

For large \(j\), \(a_j\delta\le\pi\), and
\[
 \frac{2}{\pi}p_r\le\frac{s_r}{a_j}\le p_r.
\]
These inequalities follow from \((2/\pi)x\le\sin x\le x\) on \([0,\pi/2]\). Consequently
\[
 \frac{\sigma_{\mathbf m}}{a_j}\ge\frac\delta4,
 \qquad \frac{\sigma_{\mathbf m}}{a_j}\le\sqrt3\delta,
 \qquad \frac{t_{\mathbf m}}{\sigma_{\mathbf m}}\ge\frac18.
\tag{A37}
\]
For the first and third bounds it suffices to use \(\pi<4\), one of the lower bounds \(s_r/a_j\ge\delta/\pi\), and \(\sqrt3<2\). They are deliberately weak inequalities with the exact frequency still specified by (A31)--(A34).

On plane 23, (A34)--(A37) give
\[
 |Y_{\mathbf m}(p)|\ge\frac{c_N^3}{64},\qquad
 Y_\mu(p)Y_\nu(p)\ge\frac1{512N_j^3}.
\tag{A38}
\]
For each edge direction \(r\), its shifted Riemann sum satisfies
\(a_j^3\sum_{e\parallel r}f_{h,j}(e)\to H_h\).
Thus it lies between \(H_h/2\) and \(2H_h\) for large \(j\). The support is eventually away from the open spatial boundary. Each weighted direction-2 or direction-3 edge then belongs to two plane-23 faces, so the exact quarter-average gives
\[
 \sum_{p\parallel23}f_{h,j}(p)
 =\frac12\left(\sum_{e\parallel2}f_{h,j}(e)
                   +\sum_{e\parallel3}f_{h,j}(e)\right)
 \ge\frac{H_h}{2a_j^3}.
\tag{A39}
\]
Combining (A36), (A38), and (A39), the full magnetic matrix entry obeys
\[
 F^h_{\mu\nu}\ge\frac{H_h}{1024\ell_j^3}.
\tag{A40}
\]

For each of the two nonzero edge directions in (A33), the magnitude of a cochain factor is at most \(c_N^3\delta R\): one sine occurs and the polarization coefficient is at most one. Therefore
\[
 |A^h_{\mu\nu}|
 \le\frac{8\delta^2R^2}{N_j^3}
          \left(\sum_{e\parallel2}f_{h,j}(e)
                     +\sum_{e\parallel3}f_{h,j}(e)\right)
 \le\frac{32H_h\delta^2R^2}{\ell_j^3}.
\tag{A41}
\]
This explicitly bounds the full electric contribution before subtracting it. Since \(\delta R\le1/1000\) and \(32/10^6<1/2048\), (A40)--(A41) imply
\[
 F^h_{\mu\nu}-A^h_{\mu\nu}
 \ge\frac{H_h}{2048\ell_j^3},\qquad
 \frac{(\mathsf R_h)_{\mu\nu}}{a_j}
 \ge\frac{\delta H_h}{8192\ell_j^3}.
\tag{A42}
\]
Every retained selected pair has physical energy at most
\(2\sqrt3\delta\le\epsilon/2\), by (A30), (A37). Its energy is strictly positive.

### 5.3. Counting the growing family and its raw mass

The interval of allowed integers for each component in (A32) has length
\(\delta\ell_j/(2\pi)\). The count in any one residue class modulo four is at least one fourth of this length minus one. Once its length is at least eight, this is at least \(\delta\ell_j/(16\pi)\). All such integers belong to \(1,\ldots,N_j-1\) for large \(j\), since \(a_j\delta\to0\). There are therefore at least
\[
 M_j\ge\left(\frac{\delta\ell_j}{16\pi}\right)^3
\tag{A43}
\]
selected orthonormal modes. Applying (A42) to all \(M_j^2\) ordered pairs in the exact full mass formula (A29) proves
\[
 \boxed{
 \nu_{h,0,j}((0,\epsilon))
 \ge\nu_{h,0,j}((0,\epsilon/2])
 \ge \frac{3\delta^8H_h^2}{2^{53}\pi^6}>0
 \quad\text{for all sufficiently large }j.}
\tag{A44}
\]
The coefficient follows from
\((3/8)(16\pi)^{-6}8192^{-2}=3/(2^{53}\pi^6)\).
This is a lower bound on the full raw measure, not on a state divided by its norm. It comes from a number of mode pairs of order \(\ell_j^6\), each of squared amplitude of order \(\ell_j^{-6}\). The lowest three modes alone do not have that growing count and instead have the exact \(\ell_j^{-8}\) mass in (A12). These are compatible statements about two explicitly included parts of (A29).

Nonnegativity of \(h\) is used in (A36)--(A41). This proof does not assert (A44) for arbitrary signed \(h\). It covers the nonzero nonnegative compact curvature profiles described in the source without using a singular time or asserting anything about their fluid evolution.

## 6. What is proved at positive coupling, and what the current diagonal does not supply

At each fixed \(j\), the source full-vector and finite-projection theorems prove convergence of the entire actual raw measure of \(\Xi_{f_{h,j}}\) to (A28), including its total mass. A continuous compactly supported spectral test therefore converges, regardless of degeneracies in the comparison spectrum.

For a concrete transfer of (A44), choose a continuous function \(\varphi_\epsilon\) on \([0,\infty)\) with values in \([0,1]\), equal to one on \([0,\epsilon/2]\), and zero on \([3\epsilon/4,\infty)\). Both actual and comparison centered measures have no vacuum atom at zero at each fixed regulator. Thus
\[
 \nu_{h,g,j}((0,\epsilon))
 \ge\int\varphi_\epsilon(E)\,d\nu_{h,g,j}(E),\qquad
 \int\varphi_\epsilon\,d\nu_{h,0,j}
 \ge\frac{3\delta^8H_h^2}{2^{53}\pi^6}
\tag{A45}
\]
for large \(j\). The exact finite calculation to preserve on the nonlinear side is the Gram entry
\[
 \left\langle\Xi_{f_{h,j}},
       \varphi_\epsilon(H_{g,L_j,a_j}-\mathcal E_{g,L_j,a_j})
                         \Xi_{f_{h,j}}\right\rangle.
\tag{A46}
\]
Its fixed-box comparison is the full finite sum (A29) with \(\mathbf1_I\) replaced by \(\varphi_\epsilon\). This test does not insert the first-band projection.

The Section 15 dyadic conditions control its seven-dimensional compressed operators, frame energies, and projected Fabel coordinates. They do not contain (A46). Section 22 contains its own weighted radial tests. Neither displayed finite list alone proves the joint full-mode compact-energy conclusion on the other section's already chosen least dyadic.

There is nevertheless a proved explicit continuation, with no missing fixed-box theorem: for this fixed \(h\), at stage \(j\) include in the union of the existing tests
\[
 \left|\int\varphi_{1/n}\,d\nu_{h,g,j}
             -\int\varphi_{1/n}\,d\nu_{h,0,j}\right|<\frac1j,
 \qquad 1\le n\le j.
\tag{A47}
\]
There are finitely many added scalar tests, and each converges at fixed box by the proved raw-measure theorem. Hence they hold for every sufficiently small positive coupling. Taking the least positive dyadic exponent satisfying their union defines a refined sequence \(g_j^{\sharp}\). This establishes existence rather than postulating a rate. It retains
\(\kappa_j=200j(g_j^{\sharp})^2\),
\(b_j=50j/(g_j^{\sharp})^2\),
\(\xi_j=1/(4(g_j^{\sharp})^4)\), and the complete Wilson scalar.

For each fixed positive integer \(n\), (A44)--(A47) then prove the actual nonlinear raw bound
\[
 \liminf_{j\to\infty}\nu_{h,g_j^{\sharp},j}((0,1/n))
 \ge\frac{3\delta_{1/n}^8H_h^2}{2^{53}\pi^6}>0,
 \qquad
 \delta_{1/n}=\min\left\{\frac1{4\sqrt3n},\frac1{1000R}\right\}.
\tag{A48}
\]
Every window \((0,\epsilon)\), \(\epsilon>0\), contains one of these windows \((0,1/n)\). Thus the same refined sequence has strictly positive raw low-energy liminf in each such window. The refinement in (A47) is a construction proved here; it is not asserted to coincide with either section's earlier least-dyadic definition. Its existence uses proved fixed-box convergence and does not provide a numerical convergence rate or a numerical value of the exponent.

The construction can preserve any fixed finite collection of profiles by including their finite scalar tests. A simultaneous assertion for an unspecified uncountable profile class requires its own uniform or dense-family argument; it is not inferred merely from the separately available fixed-profile selections.

## 7. Consequences and remaining continuum limits

The compact lowest-band raw mass is \(36\pi^2H_h^2\ell_j^{-8}+o(\ell_j^{-8})\); the radial centered raw mass after multiplication by \(j\) tends to \((3/2)c_\Gamma^2\). Their exact common quadratic map (A21)--(A27) accounts for both powers. The domain of signed weighted energy remains the Peter--Weyl domain, with the smooth common core used for the commutators; it is not asserted to be \(H^2\).

The precise relations established here are the original nonlinear weighted double commutator (A16), its weighted oscillator image (A19), the exact three-mode decomposition (A21), the compact/radial compression map (A25), its raw mass and mixed Gram checks (A26)--(A27), and the full-mode low-energy lower bound (A44) with the explicit actual-coupling refinement (A47)--(A48). The electric, magnetic, number-preserving, gauge, orientation, endpoint, and raw-amplitude factors have all been retained in those calculations.

The remaining continuum issue is not removed by either a positive radial Gamma measure or the stronger local raw bound (A48). No common limiting representation of the full local observables, vacuum, time evolution, and all required domains has been constructed here. No uniform full-state norm or ultraviolet limit is supplied by (A44). The unprojected products and higher-mode insertions still need their own continuum analysis; the compression formulas do not determine them. The spatially global phase coordinate and its configuration-space cutoff remain as specified. Neither a prescribed renormalized running-coupling law nor an interacting four-dimensional continuum theory is identified by choosing sufficiently small positive finite-box couplings. No claim about a Navier--Stokes singular endpoint follows from the regular-time profile map.
