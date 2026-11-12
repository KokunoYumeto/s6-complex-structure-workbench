# The exact center-disorder endpoint of the native magnetic translation

8 September 2026. This note calculates the relation between the continuous
native magnetic translation, discrete center transformations, Wilson loops,
and actual quantum spectral moments. It uses the full original open SU(2)
Wilson box. In particular a discrete transformation is not identified with
a nonzero excitation merely because it is not the identity on link variables.
Its action on the actual vacuum and its energy are calculated explicitly.

## 1. Original operator and all center cochains

Fix the open cubical complex with vertices \(\{-L,\ldots,L\}^3\),
\(L\geq2\), positive physical links \(\mathsf E_L\), and all elementary
faces \(\mathsf P_L\). Reverse traversal uses the inverse of the same link.
For \(p=(n;i,j)\), \(i<j\), set
\[
 W_p=\operatorname{tr}\{U_i(n)U_j(n+\mathbf e_i)
                  U_i(n+\mathbf e_j)^{-1}U_j(n)^{-1}\}.
\]
Work in product Haar probability \(L^2(SU(2)^{\mathsf E_L},dU)\), with
\(T_a=-i\sigma_a/2\), left derivatives \(X_{e,a}\), and
\(E_e=-\sum_aX_{e,a}^2\). Retain
\[
 H=\kappa\sum_eE_e+b\sum_p(2-W_p),\qquad
 \kappa=\frac{2g^2}{a},\quad b=\frac1{2g^2a},\quad
 \xi=\frac b\kappa=\frac1{4g^4},\quad a,g>0.
\tag{1}
\]
Its domain is the product Sobolev space \(H^2\), its form domain is
\(H^1\), and its potential is bounded and smooth. The positive unit vacuum
\(\psi\) exists and is unique: modulus decreases form energy, elliptic
regularity and the maximum principle give strict positivity, and the
identity
\[
 q_{H-\mathcal E}(\psi F)=\kappa\sum_{e,a}\int\psi^2|X_{e,a}F|^2dU
\tag{2}
\]
proves uniqueness by dividing another bottom eigenvector by \(\psi\).
The gauge action \(U_e\mapsto g_{s(e)}U_eg_{t(e)}^{-1}\) preserves the
operator and hence fixes \(\psi\). Put \(A=H-\mathcal E\).

Let \(z=(z_e)\), \(z_e\in\{+1,-1\}\), be any real center one-cochain
on the original physical edges; assign the same sign to the reverse edge,
which is its inverse in this group. Define
\[
 (D_zF)(U)=F((z_eU_e)_e),\qquad
 (\delta z)_p=\prod_{e\in\partial p}z_e,
 \quad\mathcal T_z=\{p:(\delta z)_p=-1\},
 \quad S_z=\sum_{p\in\mathcal T_z}W_p.
\tag{3}
\]
Here \(z_eU_e\) means multiplication by \(z_e I_2\). Haar invariance
gives \(D_z^*=D_z=D_z^{-1}\). These diffeomorphisms preserve all integer
Sobolev domains, commute with all link Casimirs, and commute with every
vertex gauge transformation because \(z_eI_2\) is central. They obey
\(D_zD_w=D_{zw}\).

Each face word gains exactly its four central factors, so, as operator
identities on \(H^2\),
\[
 D_zW_pD_z=(\delta z)_pW_p,\qquad
 \boxed{D_zHD_z=H+2bS_z.}
\tag{4}
\]
All faces outside \(\mathcal T_z\) remain present in both Hamiltonians.
The scalar \(2b|\mathsf P_L|\) is identical on both sides and has not
been suppressed. Equation (4) is a unitary relation to an explicitly
sign-twisted potential, not permission to erase that potential change.

## 2. Exact native magnetic endpoint and its Wilson algebra

The native smooth field in the retained cusp coordinates has link transports
\[
 h_1(n)=\exp(-\theta n_2H_c),\qquad h_2=h_3=I,
 \qquad H_c=i\sigma_3=-2T_3,\qquad
 \theta=\frac{2\pi a^2}{D_T},\quad
 D_T=L_Tq_T+6m_T^2>0.
\tag{5}
\]
Its translation is \((T_\theta F)(U)=F((h_e^{-1}U_e)_e)\), and
its physical translated state is obtained by vertex Haar projection
\(\Pi\). At the specified parameter value \(\theta=\pi\),
\[
 h_1(n)=(-1)^{n_2}I,
 \quad z^{\rm nat}_{(n,1)}=(-1)^{n_2},
 \quad z^{\rm nat}_{(n,2)}=z^{\rm nat}_{(n,3)}=1,
 \quad T_\pi=D_{z^{\rm nat}}.
\tag{6}
\]
Thus \(\Pi T_\pi\psi=T_\pi\psi\) exactly. Its face coboundary is
\[
 (\delta z^{\rm nat})_{12}=-1,\qquad
 (\delta z^{\rm nat})_{13}=(\delta z^{\rm nat})_{23}=1.
\tag{7}
\]
The two direction-1 signs on a 12 face are \((-1)^{n_2}\) and
\((-1)^{n_2+1}\), whereas they agree on a 13 face. There are
\((2L)^2(2L+1)\) twisted 12 faces, not all M faces. At \(\theta=2\pi\)
every h is the identity. Equations (5)--(7) keep both the continuous path
and its discrete endpoints. The endpoint \(\theta=\pi\) means precisely
\(D_T=2a^2\); it is not an assertion that the small-angle cusp exhaustion
reaches that endpoint with its original spacing and determinant.

For any closed oriented edge word C, allowing repeated traversals, let
\(W_C\) be the fundamental trace of its ordered holonomy and put
\(z(C)=\prod_{e\text{ traversed in }C}z_e\), with multiplicities.
Centrality and inversion give
\[
 \boxed{D_zW_C=z(C)W_CD_z.}
\tag{8}
\]
If a mod-two face chain \(\Sigma\) has boundary C modulo two, every
internal edge occurs twice, so
\[
 z(C)=\prod_{p\in\Sigma}(\delta z)_p
     =(-1)^{|\Sigma\cap\mathcal T_z|}.
\tag{9}
\]
This proves the discrete Wilson--disorder commutation pairing, including
its multiplicities and sign, directly in the original Hilbert space.
For (6), a rectangular 12 loop of integer side lengths r,s has
\(z^{\rm nat}(C)=(-1)^{rs}\). Its sign does not involve a rescaled area:
the physical area is \(a^2rs\), and (5) at \(\theta=\pi\) gives the
same phase \(\exp(\pi rsH_c)=(-1)^{rs}I\).

## 3. Vacuum overlap, both spectral moments, and the exact zero branch

For every center cochain set
\[
 c_z=\langle\psi,D_z\psi\rangle,\qquad
 \chi_z=D_z\psi-c_z\psi,\qquad d_z=\|\chi_z\|^2=1-c_z^2.
\tag{10}
\]
Strict positivity of \(\psi\) implies \(0<c_z\leq1\). All vectors in
(10) are smooth and gauge invariant, and \(\chi_z\perp\psi\).
Using (4), without replacing the vacuum, gives
\[
 \boxed{q_A(\chi_z)=2b\langle S_z\rangle_\psi,\qquad
        A\chi_z=-2bS_zD_z\psi,\qquad
        \|A\chi_z\|^2=4b^2\langle S_z^2\rangle_\psi.}
\tag{11}
\]
The first formula follows from
\(\langle D_z\psi,HD_z\psi\rangle-mathcal E
=\langle\psi,(D_zHD_z-H)\psi\rangle\); centering has no effect on
the form since \(A\psi=0\). For the second,
\(H D_z\psi-D_zH\psi=(H-D_zHD_z)D_z\psi=-2bS_zD_z\psi\).
Finally \(D_zS_zD_z=-S_z\), hence \(D_zS_z^2D_z=S_z^2\), proving
the last formula after Haar substitution.

If \(\mathcal T_z\) is empty, (4) commutes with H and uniqueness and
positivity of its unit vacuum imply \(D_z\psi=\psi\). Hence
\(c_z=1\) and \(\chi_z=0\) exactly. Conversely, if \(\chi_z=0\),
the norm and positive overlap force \(D_z\psi=\psi\). Apply (4) to
this vector and its original eigen-equation to get \(S_z\psi=0\).
Strict positivity makes \(S_z=0\) pointwise. Distinct elementary
\(W_p\)'s are orthonormal under product Haar measure: integrate a link
in only one boundary, and use \(\int(\operatorname{tr}U)^2dU=1\)
when the faces agree. Therefore
\(\|S_z\|_{L^2(dU)}^2=|\mathcal T_z|\), and the latter must be zero.
We have proved
\[
 \boxed{\chi_z=0\quad\Longleftrightarrow\quad\mathcal T_z=\varnothing.}
\tag{12}
\]
This also proves \(\langle S_z\rangle_\psi>0\) when
\(\mathcal T_z\ne\varnothing\): (11) is the strictly positive form of
a nonzero physical vacuum-orthogonal vector of a compact-resolvent
Hamiltonian with a unique bottom.

For a nonempty twist the full physical spectral probability is
\(\nu_z(B)=d_z^{-1}\langle\chi_z,\mathbf1_B(A)\chi_z\rangle\).
It has no zero atom, and (11) gives its exact moments
\[
 \boxed{\int\omega\,d\nu_z=
   \frac{2b\langle S_z\rangle_\psi}{1-c_z^2},\qquad
 \int\omega^2\,d\nu_z=
   \frac{4b^2\langle S_z^2\rangle_\psi}{1-c_z^2}.}
\tag{13}
\]
The second moment retains every mixed \(\langle W_pW_q\rangle_\psi\)
between twisted faces. No independence is assumed. The denominator is the
exact overlap loss, not an assumed unit excitation norm.

## 4. Small-coupling coefficient in the same vacuum

At each fixed box, the actual analytic positive vacuum of
\(H=\kappa(H_0-\xi\sum_pW_p)+2bM\) has
\[
 \psi_\xi=1+\frac\xi3\sum_pW_p+O_{H^2,L}(\xi^2).
\tag{14}
\]
One proof is to integrate the resolvent on \(|z|=3/8\) in the full
Hilbert space: the first free eigenvalue is \(3/4\),
\(\|\sum W_p\|=2M\), and a Neumann series converges for
\(|\xi|<3/(16M)\). Differentiating the eigen-equation gives (14),
because \(H_0W_p=3W_p\). Thus
\[
 (D_z-I)\psi_\xi=-\frac{2\xi}{3}S_z+O_{H^2,L,z}(\xi^2).
\]
For an involution and a real unit vector,
\(1-c_z=\tfrac12\|(D_z-I)\psi_\xi\|^2\). Consequently
\[
 \begin{split}
 1-c_z&=\frac{2|\mathcal T_z|}{9}\xi^2+O_L(\xi^4),\\
 d_z&=\frac{4|\mathcal T_z|}{9}\xi^2+O_L(\xi^4),\\
 q_A(\chi_z)&=\frac{4|\mathcal T_z|}{3}\kappa\xi^2
                         +O_L(\kappa\xi^4),\\
 \|A\chi_z\|^2&=4|\mathcal T_z|\kappa^2\xi^2
                         +O_L(\kappa^2\xi^4).
 \end{split}
\tag{15}
\]
To verify the even remainders, use the independent central cochain
\(\widetilde z_i(n)=(-1)^{\sum_{j<i}n_j}\), which changes every
elementary face sign. Its involution Z conjugates
\(H_0-\xi\sum W_p\) to \(H_0+\xi\sum W_p\), commutes with
\(D_z\), and sends \(S_z\) to \(-S_z\). Uniqueness gives
\(\psi_{-\xi}=Z\psi_\xi\). Thus c_z and
\(\langle S_z^2\rangle\) are even, whereas
\(\langle S_z\rangle\) is odd. Its first derivative from (14) is
\(2|\mathcal T_z|/3\), and its value at zero is zero. These facts
give precisely all errors in (15).

For a nonempty fixed twist, division of the displayed quantities proves
the leading first moment \(3\kappa+O_L(\kappa\xi^2)\) and second
moment \(9\kappa^2+O_L(\kappa^2\xi^2)\). Equivalently the spectral
probability in the energy variable \(\omega/\kappa\) tends to
\(\delta_3\) as \(\xi\to0\): its integral of \((\omega/\kappa-3)^2\)
tends to zero by these moments, and the resulting Chebyshev bound proves
weak convergence. This is a fixed-box limit. It supplies the complete
quantum dictionary for (6), not a large-volume gap assertion.

## 5. The original integer line flux and its adjoint center class

There is a second exact relation, now for the original smooth bundle rather
than the finite-link endpoint. On the marked two-torus let the original
Hermitian line bundle have transition phases \(e^{i\phi_{ab}}\), with
\(\phi_{ab}+\phi_{bc}+\phi_{ca}=2\pi n_{abc}\) on triple overlaps.
The canonical cusp connection on this line has integer curvature period
\((2\pi)^{-1}\int f=1\). Its embedded rank-two SU(2) bundle is
\(L\oplus L^{-1}\), with explicit transition matrices
\[
 g_{ab}=\operatorname{diag}(e^{i\phi_{ab}},e^{-i\phi_{ab}})
        =\exp(\phi_{ab}H_c),\qquad g_{ab}g_{bc}g_{ca}=I.
\tag{16}
\]
The product identity follows from the integer \(n_{abc}\); determinant
one is also exact. Under the adjoint representation,
\([!H_c,T_1!]=-2T_2\), \([!H_c,T_2!]=2T_1\), and H_c fixes
T_3. Hence
\[
 \begin{split}
 \operatorname{Ad}_{e^{\phi H_c}}T_1
   &=\cos(2\phi)T_1-\sin(2\phi)T_2,\\
 \operatorname{Ad}_{e^{\phi H_c}}T_2
   &=\sin(2\phi)T_1+\cos(2\phi)T_2.
 \end{split}
\tag{17}
\]
In the oriented real plane with complex coordinate \(v_1+iv_2\), this
is multiplication by \(e^{-2i\phi}\). Its winding/Chern number is
therefore \(-2c_1(L)\). More directly, the obstruction cocycle to lifting
the adjoint SO(3) transitions to SU(2) is identically \(+I\), because
(16) is already such a lift. Its \(\mathbb Z/2\) obstruction class is
zero. This proves the exact integer-to-center map for this particular
embedding, including the factor 2 and its orientation sign; it does not
erase the nonzero original integer curvature period.

The associated holonomy identities are
\(\exp(2\pi H_c)=I\) and \(\exp(\pi H_c)=-I\). Replacing (16)
by a half-angle lift would change its triple-overlap product to
\((-1)^{n_{abc}}I\), precisely the center obstruction. Such a change
is not the original line bundle with its original transition matrices.
The continuous field, its integer line data, the adjoint center class,
and the finite center-disorder endpoint are therefore related by the
explicit maps (5)--(9), (16)--(17), rather than by an assumed equality
of their flux labels.

## 6. Primary context and what the calculation establishes

Wilson--disorder pairing and center flux are established gauge-theory
constructions. A primary reference is G. 't Hooft, *On the phase transition
towards permanent quark confinement*, Nuclear Physics B **138** (1978),
1--25, DOI <https://doi.org/10.1016/0550-3213(78)90153-0>. The actual
compact-link operator and its pairing needed here are proved in (3)--(9).
For the SU(2) global-charge conventions, D. Tong, *Gauge Theory*, Sections
2.6.1--2.6.2, <https://www.damtp.cam.ac.uk/user/tong/gaugetheory.html>,
discusses the factor between adjoint and fundamental charge quantization;
(16)--(17) give it directly in the original H_c convention.

P. de Forcrand and L. von Smekal, *'t Hooft Loops, Electric Flux Sectors
and Confinement in SU(2) Yang--Mills Theory*, Physical Review D **66**
(2002), 011504, <https://doi.org/10.1103/PhysRevD.66.011504>,
<https://arxiv.org/abs/hep-lat/0107018v2>, study flux-sector free energies
at finite temperature. Their finite-temperature free energy is not
substituted for the vacuum excitation moment (13). The operator relation
and both moments used here were calculated directly in the full H.

The center endpoint gives a nonzero actual quantum state precisely for a
nonempty coboundary twist. A cocycle that commutes with H fixes its unique
finite-box vacuum and produces the zero centered vector. Nonempty twists
give the exact overlap-dependent moments (13), including every correlation.
These statements neither assume nor prove a continuum mass gap. They
identify the spectral quantities that the original magnetic path actually
reaches at its discrete endpoint, while retaining the smooth integer-flux
bundle and its explicit adjoint relation.
