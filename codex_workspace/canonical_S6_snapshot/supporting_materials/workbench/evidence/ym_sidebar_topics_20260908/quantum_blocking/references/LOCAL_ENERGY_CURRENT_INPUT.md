# Local energy currents and the first surviving quantum state

8 September 2026. This calculation keeps every link and every elementary
plaquette of the interacting three-dimensional spatial Wilson box. Time
is the Hamiltonian time; no fourth spatial coordinate is added. The
weighted electric operator from the magnetic continuation is extended by
the matching magnetic energy, with the extension written explicitly.
The first plaquette contribution then cancels. The next contribution is
calculated below, rather than inferred to have zero norm or zero energy.

## 1. Full Hamiltonian, state space, and weighted operator

Fix an integer \(L\ge2\). Vertices are
\(\{-L,\ldots,L\}^3\). A positively oriented physical link
\(e=(n,i)\) exists when both \(n\) and \(n+\mathbf e_i\) are
vertices. Its variable is \(U_e\in SU(2)\); inverse traversal uses
\(U_e^{-1}\). For every elementary face \(p=(n;i,j)\), \(i<j\), put
\[
 W_p=\operatorname{tr}\{U_i(n)U_j(n+\mathbf e_i)
                  U_i(n+\mathbf e_j)^{-1}U_j(n)^{-1}\}.
\tag{1.1}
\]
The full link and face sets are denoted \(\mathsf E_L,\mathsf P_L\).
Their cardinalities are
\[
 N=3(2L)(2L+1)^2,\qquad M=3(2L)^2(2L+1).
\]
All sums below use these sets, including boundary links and faces in all
three planes. On \(\mathcal H=L^2(SU(2)^N,dU)\), with product Haar
probability measure, use
\[
 T_a=-i\sigma_a/2,\quad
 X_{e,a}F=\left.\frac{d}{dt}F(\ldots,e^{tT_a}U_e,\ldots)\right|_{t=0},
 \quad E_e=-\sum_{a=1}^3X_{e,a}^2.
\]
These conventions give fundamental Casimir \(3/4\). The original metric
\(c(A,B)=-\operatorname{tr}(AB)/2\) has orthonormal basis \(2T_a\),
so \(-\Delta_e^c=4E_e\). Retain
\[
 H=\kappa H_0+V,\quad H_0=\sum_e E_e,\quad
 V=\sum_p V_p,\quad V_p=b(2-W_p),
 \quad \kappa=\frac{2g_{\rm YM}^2}{a},\quad
 b=\frac{1}{2g_{\rm YM}^2a},\quad \xi=\frac b\kappa.
\tag{1.2}
\]
In particular \(\xi=1/(4g_{\rm YM}^4)\), and the constant \(2bM\)
is part of H. It is not removed from the energy origin.

Gauge transformations act by \(U_e\mapsto g_{s(e)}U_eg_{t(e)}^{-1}\).
Each \(E_e\) is bi-invariant and each \(W_p\) is gauge invariant.
Hence every operator used below preserves the gauge-invariant subspace.

The compact connected configuration space, elliptic kinetic operator,
and bounded smooth V give a compact-resolvent self-adjoint H with domain
\(H^2\) and form domain \(H^1\). Its bottom eigenvector \(\psi>0\)
is smooth and unique after fixing \(\int\psi^2dU=1\). Here is the
argument needed below. Taking the modulus of a form minimizer does not
increase its gradient energy, by approximation with
\(\sqrt{|u|^2+\varepsilon^2}\). Elliptic regularity and the strong
maximum principle make a nonnegative minimizer smooth and strictly
positive. If its eigenvalue is \(\mathcal E\), integration by parts
gives, for smooth F,
\[
 \mathfrak q_{H-\mathcal E}[\psi F]
 =\kappa\sum_{e,a}\int |X_{e,a}F|^2\psi^2dU.
\tag{1.3}
\]
A second bottom eigenvector divided by \(\psi\) would have every
derivative zero and hence be constant. This proves uniqueness, and gauge
transformations therefore fix \(\psi\). Write \(\mathcal A=H-\mathcal E\).

For arbitrary real link weights \(f_e\), including signed weights, define
\[
 f_p=\frac14\sum_{e\in\partial p}f_e,\quad
 D_f=\kappa\sum_e f_eE_e+\sum_p f_pV_p,
 \quad \zeta_f=(D_f-\langle\psi,D_f\psi\rangle)\psi.
\tag{1.4}
\]
Thus the coefficient \(1/4\) distributes each *same* face energy among
its four boundary links. The magnetic extension is explicit: if
\(\Gamma=\sum_{e=(n,1)}n_2^2E_e\) is the original magnetic-translation
operator, take \(f_{(n,1)}=n_2^2\), \(f_{(n,2)}=f_{(n,3)}=0\).
Then \(D_f=\kappa\Gamma+\sum_p f_pV_p\); it is a new physical trial
operator in the original Hamiltonian, not an assertion that its magnetic
term was already present in \(\Gamma\).

The signed kinetic sum in (1.4) is self-adjoint on its diagonal
Peter--Weyl spectral domain: a coefficient with spins \(j_e\) has
eigenvalue \(\kappa\sum_e f_ej_e(j_e+1)\). Its domain is the set
whose squared coefficients times this eigenvalue squared are summable.
This domain need not equal \(H^2\) when weights are signed. Adding the
bounded real potential in (1.4) preserves self-adjointness on that domain.
All smooth vectors lie in it, and D_f maps smooth vectors to smooth
vectors. Thus \(\zeta_f\) is a well-defined smooth, gauge-invariant,
vacuum-orthogonal state. Every product and commutator below is evaluated
on smooth vectors; no bounded-operator claim about D_f is needed.

## 2. Exact energy current and spectral moments at arbitrary positive coupling

The product rule with the above sign of \(E_e\) gives
\[
 [E_e,V_p]F=-\sum_a\{(X_{e,a}^2V_p)F
                       +2(X_{e,a}V_p)X_{e,a}F\}.
\tag{2.1}
\]
It vanishes when \(e\notin\partial p\). Since all link Casimirs
commute and all potential multiplication operators commute,
\[
 [H,D_f]=\kappa\sum_{p}\sum_{e\in\partial p}
                         (f_p-f_e)[E_e,V_p].
\tag{2.2}
\]
This is an exact weighted-difference formula, not an expansion in the
background angle or coupling. All derivatives of every V_p in (2.1)
remain, including the first-derivative terms acting on F.

Define local energy operators and antisymmetric currents by
\[
 h_e=\kappa E_e+\frac14\sum_{p\ni e}V_p,\qquad
 J_{ef}=i[h_e,h_f]
       =\frac{i\kappa}{4}\sum_{p:\ e,f\in\partial p}
                         ([E_e,V_p]-[E_f,V_p]).
\tag{2.3}
\]
For \(e=f\) both sides of the last formula are zero. Each face is
counted four times in \(\sum_e h_e\), so \(\sum_e h_e=H\).
The exact Heisenberg derivative and its weighted form are therefore
\[
 i[H,h_e]=-\sum_fJ_{ef},\qquad
 i[H,D_f]=\frac12\sum_{e,f}(f_f-f_e)J_{ef}.
\tag{2.4}
\]
The second equality follows by exchanging e and f in one of the two
terms, using \(J_{ef}=-J_{fe}\). Expanding (2.3) also gives (2.2).
Currents between links that share no face vanish exactly. A constant
weight gives D_f equal to that constant times H and \(\zeta_f=0\)
exactly, not merely to a computed order.

Let \(d_f=\|\zeta_f\|^2\), \(n_f=\mathfrak q_{\mathcal A}[\zeta_f]\).
The vacuum eigen-equation and expansion of the double commutator give
\[
 \mathcal A\zeta_f=[H,D_f]\psi,\qquad
 n_f=\frac12\langle\psi,[D_f,[H,D_f]]\psi\rangle,
 \qquad
 \|\mathcal A\zeta_f\|^2=\|i[H,D_f]\psi\|^2.
\tag{2.5}
\]
For example the double commutator expands to
\(2D_fHD_f-D_f^2H-HD_f^2\); its expectation is twice
\(\langle D_f\psi,(H-\mathcal E)D_f\psi\rangle\).
There is no change of vacuum in these formulas.

To specify their spectral content, choose a complete orthonormal
eigenbasis \(u_0=\psi,u_1,u_2,\ldots\) of the physical Hamiltonian,
with \(\mathcal A u_\ell=\lambda_\ell u_\ell\),
\(\lambda_\ell>0\) for \(\ell\ge1\). Set
\[
 d\mu_f(\lambda)=\sum_{\ell\ge1}
 |\langle u_\ell,D_f\psi\rangle|^2\delta_{\lambda_\ell}(d\lambda).
\]
Completeness, smoothness, and (2.5) prove
\[
 d_f=\int d\mu_f,\quad n_f=\int\lambda\,d\mu_f,\quad
 \|i[H,D_f]\psi\|^2=\int\lambda^2d\mu_f.
\tag{2.6}
\]
Thus a small current matrix element is accompanied by a specified state
norm, rather than being identified with an excitation energy on its own.

## 3. The second coefficient of the actual all-plaquette vacuum

Put \(S=\sum_pW_p\). The exact Hamiltonian is
\(H=\kappa(H_0-\xi S)+2bM\). The first nonzero full-Hilbert-space
eigenvalue of H_0 is \(3/4\). Also \(\|S\|_\infty=2M\): the upper
bound follows from \(|W_p|\le2\), and the all-identity configuration
and its positive-measure neighborhoods give equality. On the circle
\(|z|=3/8\), the free resolvent has norm at most \(8/3\). Factoring
\(z-H_0+\xi S\) therefore yields a convergent Neumann series when
\[
 |\xi|<\frac{3}{16M}.
\tag{3.1}
\]
The contour spectral projection is analytic and rank one there, by
continuity from \(\xi=0\). For real \(\xi\) in this interval,
min--max bounds place the lowest eigenvalue in
\([-2M|\xi|,0]\) and every other eigenvalue above
\(3/4-2M|\xi|>3/8\), so this is the actual ground projection.
Its positive unit-norm eigenvector is real analytic in a neighborhood
of zero. Elliptic regularity applied successively to the eigen-equation
gives analyticity in each fixed Sobolev space. Neighborhood and remainder
constants here may depend on L; no volume-uniform disk is asserted.

Integrating a single boundary link proves
\[
 \int W_p=0,\qquad \int W_pW_q=\delta_{pq},\qquad H_0W_p=3W_p.
\tag{3.2}
\]
For distinct faces there is an edge in only one of them; multiplication
of that link by \(-I\) changes the integrand's sign. For equal faces,
Haar invariance reduces the integral to
\(\int_{SU(2)}(\operatorname{tr}U)^2dU=1\). The latter follows from
\(U=u_0I+i\sum_au_a\sigma_a\), uniform on the unit 3-sphere,
where \(\int u_0^2=1/4\). Four fundamental Casimirs give the last
identity in (3.2).

Write the positive unit-norm vacuum and dimensionless bottom energy as
\[
 \psi_\xi=1+\xi A+\xi^2B+O_{H^k,L}(\xi^3),\quad
 A=\frac13S,\quad e(\xi)=-\frac M3\xi^2+O_L(\xi^3).
\]
Coefficient comparison in \((H_0-\xi S)\psi_\xi=e(\xi)\psi_\xi\)
and the retained unit-norm condition give
\[
 H_0B=\frac13(S^2-M),\qquad \int B=-\frac M{18}.
\tag{3.3}
\]
Let \(R_0\) act as zero on constants and as the inverse of H_0 on
their orthogonal complement. Then B is the completely specified finite
polynomial \(R_0(S^2-M)/3-M/18\). Its fully resolved terms are as follows.

For an unordered pair of distinct faces sharing an edge e, define
\[
 P_{pq,0}=\int_{SU(2)}W_pW_q\,dU_e,\qquad
 P_{pq,1}=W_pW_q-P_{pq,0}.
\tag{3.4}
\]
The first expression is a function of the other links. It is one half
of the fundamental trace around the six-edge boundary, with either
orientation giving the same SU(2) trace. To see the coefficient, reverse
one of the face words if necessary so the shared link is oppositely
traversed, and cyclically write the traces as
\(\operatorname{tr}(U_eA)\) and \(\operatorname{tr}(U_e^{-1}B)\).
The fundamental Haar identity
\(\int U_{ij}\overline{U}_{kl}dU=\delta_{ik}\delta_{jl}/2\)
gives \(P_{pq,0}=\operatorname{tr}(AB)/2\). A,B use six distinct
outer links. Their products are independent Haar variables when those
links are integrated. The shared-link tensor product has spins 0 and 1,
while every outer link has spin \(1/2\). Consequently
\[
 H_0P_{pq,0}=\frac92P_{pq,0},\quad
 H_0P_{pq,1}=\frac{13}2P_{pq,1},\quad
 \|P_{pq,0}\|^2=\frac14,\quad \|P_{pq,1}\|^2=\frac34.
\tag{3.5}
\]
The total squared norm of \(W_pW_q\) is 1 by integrating A and B
first; the Haar projection is orthogonal, proving the last norm.

A repeated face gives \(W_p^2-1\), the spin-1 character, with
H_0 eigenvalue 8. An edge-disjoint pair gives \(W_pW_q\) with
H_0 eigenvalue 6, even if its faces share a vertex. These statements
exhaust the face pairs. Thus no term is hidden in the inverse:
\[
 \boxed{B=-\frac M{18}
 +\sum_p\frac{W_p^2-1}{24}
 +\sum_{\{p,q\}:\partial p\cap\partial q=\varnothing}\frac{W_pW_q}{9}
 +\sum_{\{p,q\}:|\partial p\cap\partial q|=1}
       \left(\frac4{27}P_{pq,0}+\frac4{39}P_{pq,1}\right).}
\tag{3.6}
\]
Each sum over distinct pairs is unordered. Every independent link of
the full Hamiltonian is still present; (3.6) is a coefficient of its
vacuum, not a replacement by separate two-face Hamiltonians.

## 4. Cancellation and the first surviving state, with all constants

Set \(F_f=\sum_pf_p\), \(S_f=\sum_pf_pW_p\),
\(E_f=\sum_ef_eE_e\). Equation (1.4) is exactly
\[
 D_f=\kappa\{E_f-\xi S_f+2\xi F_fI\}.
\tag{4.1}
\]
The link Casimir gives \(E_fA=S_f\), since
\(E_fW_p=(3/4)\sum_{e\in\partial p}f_eW_p=3f_pW_p\).
Thus the first-order vector of the centered state cancels for *every*
chosen weight profile. Its scalar expectation, retaining its origin, is
\[
 \langle\psi_\xi,D_f\psi_\xi\rangle
 =\kappa\left(2\xi F_f-\frac{\xi^2}3F_f\right)+O_L(\kappa\xi^3),
\]
because \(\langle A,E_fA\rangle=F_f/3\) and
\(\langle S_f\rangle_{\psi_\xi^2}=2\xi F_f/3+O_L(\xi^2)\).
Subtracting this scalar times the same vacuum gives
\[
 \zeta_f=\kappa\xi^2 Z_f+O_{H^k,L,f}(\kappa\xi^3),\qquad
 Z_f=E_fB-S_fA+\frac{F_f}{3}.
\tag{4.2}
\]

Inserting (3.6) resolves every cancellation. For a repeated face,
\(E_f(W_p^2-1)=8f_p(W_p^2-1)\), so its contribution in (4.2) is
\(f_p(W_p^2-1)/3-f_pW_p^2/3+f_p/3=0\).
For an edge-disjoint pair, \(E_f(W_pW_q)=3(f_p+f_q)W_pW_q\);
its B term cancels the two corresponding ordered terms of S_fA.

For an adjacent pair with shared edge e, all six outer edges have
Casimir \(3/4\) and the shared edge has Casimir 0 or 2. Therefore
\[
 E_fP_{pq,0}=\left(3(f_p+f_q)-\frac32f_e\right)P_{pq,0},\qquad
 E_fP_{pq,1}=\left(3(f_p+f_q)+\frac12f_e\right)P_{pq,1}.
\]
Define \(\delta_{pq}(f)=f_p+f_q-2f_e\). Subtracting the two terms
from S_fA leaves the exact finite sum
\[
 \boxed{Z_f=\sum_{\{p,q\}:\partial p\cap\partial q=\{e\}}
 \delta_{pq}(f)\left(\frac{P_{pq,0}}9-\frac{P_{pq,1}}{39}\right).}
\tag{4.3}
\]
The denominators 9 and 39 arise from the distinct \(9/2\) and
\(13/2\) electric channels, not from dropping their interaction.

Different unordered adjacent pairs are orthogonal in both channels.
Here is a direct proof covering coplanar and hinged pairs. Both channel
functions are odd under \(U_l\mapsto -U_l\) on each of the six
outer boundary edges and even on the shared edge. Two distinct pairs
have different six-edge boundaries: otherwise the symmetric difference
of their two face sets would be a nonempty mod-2 two-cycle with at most
four faces. Choose a face in that cycle. Each of its four boundary
edges needs another face. Two distinct elementary square faces share
at most one edge, so four distinct other faces would be needed, at
least five in total, a contradiction. Multiplication by \(-I\) on
an edge in just one of the boundaries now annihilates the cross integral.
The same holds with H_0 applied, because of (3.5).

Put \(\mathcal D_f=\sum_{\{p,q\}\ \text{adjacent}}\delta_{pq}(f)^2\).
Using both norms and both electric eigenvalues in (3.5) gives
\[
 \boxed{\|Z_f\|^2=\frac{49}{13689}\mathcal D_f,\qquad
 \langle Z_f,H_0Z_f\rangle=\frac{2}{117}\mathcal D_f.}
\tag{4.4}
\]
Explicitly the first coefficient is
\(1/(4\cdot9^2)+3/(4\cdot39^2)=49/13689\); the second is
\((9/2)/(4\cdot9^2)+3(13/2)/(4\cdot39^2)=2/117\).

All odd scalar powers vanish. Indeed the central link transformation
\(z_i(n)=(-1)^{\sum_{j<i}n_j}I\) gives an involutive Haar unitary
\(\mathcal Z\) sending *every* W_p to \(-W_p\), and commuting with
every E_e. It sends \(H_0-\xi S\) to \(H_0+\xi S\), so uniqueness
gives \(\psi_{-\xi}=\mathcal Z\psi_\xi\). Equation (4.1) gives
\(D_{f,-\xi}=\mathcal ZD_{f,\xi}\mathcal Z-4\kappa\xi F_fI\).
This scalar is exactly removed by centering, and hence
\(\zeta_{f,-\xi}=\mathcal Z\zeta_{f,\xi}\). The centered H transforms
in the same way. Consequently the squared norm and excitation form
are even real-analytic functions locally at zero. Combining this with
(4.2)--(4.4) proves
\[
 d_f=\kappa^2\xi^4\frac{49}{13689}\mathcal D_f
                         +O_{L,f}(\kappa^2\xi^6),\qquad
 n_f=\kappa^3\xi^4\frac{2}{117}\mathcal D_f
                         +O_{L,f}(\kappa^3\xi^6).
\tag{4.5}
\]
For each fixed profile with \(\mathcal D_f>0\), this proves a
nonzero state for a genuine sufficiently small positive interval of
\(\xi\), and
\[
 \frac{n_f}{d_f}=\frac{234}{49}\kappa+O_{L,f}(\kappa\xi^2).
\tag{4.6}
\]
The squared norm, not the unsquared norm, is analytic in the preceding
statement. When \(\mathcal D_f=0\), formula (4.3) says exactly that
this coefficient vanishes; it does not by itself assert the full state
vanishes. Constant f was resolved exactly in Section 2.

## 5. An exact spatial profile and its full boundary count

Take a fixed coordinate direction r and the link-midpoint weights
\[
 f_{(n,i)}=n_r+\frac12\delta_{ir}.
\tag{5.1}
\]
These are the original lattice coordinates, without replacing the
signed profile by its absolute value. Their face average is the face
center coordinate
\(f_{(n;i,j)}=n_r+(\delta_{ir}+\delta_{jr})/2\).
If physical midpoint length is wanted, it is exactly a times (5.1);
then D_f and \(\zeta_f\) are multiplied by a and both (4.5) scalars
by \(a^2\). The Rayleigh quotient is unchanged by this stated map.

For an edge of direction i, the centers of two incident faces are
\(x(e)+s\mathbf e_j/2\) and \(x(e)+t\mathbf e_k/2\), where
j,k differ from i and the signs indicate which available side is used.
For coplanar distinct faces j=k and s=-t, so \(\delta_{pq}=0\).
For hinged pairs j differs from k,
\[
 \delta_{pq}=\frac12(s\delta_{jr}+t\delta_{kr}).
\]
It is zero when i=r and has squared value \(1/4\) when i differs
from r. At a transverse coordinate \(n_j\), the number of available
incident j-faces is \(a_j(n_j)=1\) at either endpoint \(\pm L\)
and 2 otherwise. Its sum over \(-L,\ldots,L\) is \(4L\).
Thus the complete number of hinged pairs sharing direction-i edges is
\((2L)(4L)^2=32L^3\). There are two directions i differing from r.
This proves, including every boundary case,
\[
 \mathcal D_f=\frac14\cdot2\cdot32L^3=16L^3.
\tag{5.2}
\]
The explicit leading results are therefore
\[
 d_f=\frac{784}{13689}\kappa^2\xi^4L^3
                         +O_L(\kappa^2\xi^6),\qquad
 n_f=\frac{32}{117}\kappa^3\xi^4L^3
                         +O_L(\kappa^3\xi^6).
\tag{5.3}
\]
The profile's energy expectation is actually zero for every positive b.
Reflection \(n_r\mapsto-n_r\) induces a Haar-preserving link-variable
map; links whose orientation reverses are inverted. It preserves H,
every link Casimir, and the unique positive vacuum, and changes all
the midpoint and face-center weights in (5.1) to their negatives.
Thus its unitary conjugates D_f to \(-D_f\). Taking the vacuum
expectation proves \(\langle D_f\rangle=0\) exactly. This does not
assert the nonzero-state conclusion uniformly at every coupling.

There is also an exact all-coupling statement for *all* affine profiles,
not only their computed Taylor coefficient. Write
\[
 f_e=c+\sum_{r=1}^3t_r x_r(e),\qquad
 x_r((n,i))=n_r+\frac12\delta_{ir},\qquad t_r,c\in\mathbb R.
\]
Let \(\zeta_r=D_{x_r}\psi\); the reflection argument just proved its
expectation is zero. Since the constant-weight operator is cH,
\(\zeta_f=\sum_rt_r\zeta_r\) exactly. For every Borel set
\(B\subset(0,\infty)\), let \(P_B=1_B(\mathcal A)\). Reflection in
coordinate r commutes with \(P_B\), changes \(\zeta_r\) to its negative,
and fixes \(\zeta_s\) when \(s\ne r\). Consequently
\(\langle\zeta_r,P_B\zeta_s\rangle=0\) for \(r\ne s\).
Coordinate permutations also preserve the box and H and exchange the
three midpoint profiles, so the three diagonal expectations agree.
Thus the *entire* spectral measures, not only their first moments, obey
\[
 \boxed{\mu_f(B)=(t_1^2+t_2^2+t_3^2)\,\mu_{x_1}(B)}
 \qquad\text{for every }b>0.
\tag{5.4}
\]
The group-variable inversion needed on an orientation-reversed link
is Haar preserving and preserves its Casimir; reversed face traces
equal the original traces in SU(2). These facts justify both symmetry
actions on the actual Hilbert space. All original affine coefficients
are retained in (5.4). Its content is that varying a slope's direction,
size or constant term within this specified family changes the spectral
weight by the displayed scalar, not its positive-energy support.
It makes no assertion that a non-affine profile has the same measure.
In particular \(\mathcal D_f=16L^3(t_1^2+t_2^2+t_3^2)\), also obtained
by taking the coefficient of \(\xi^4\) in this exact identity.

The physical coefficient dictionary remains
\[
 \kappa^2\xi^4=\frac{1}{64g_{\rm YM}^{12}a^2},\quad
 \kappa^3\xi^4=\frac{1}{32g_{\rm YM}^{10}a^3},\quad
 \frac{234}{49}\kappa=\frac{468g_{\rm YM}^2}{49a}.
\tag{5.5}
\]
The common \(L^3\) in (5.3) is a computed Taylor coefficient, not
a statement that the all-coupling remainder is uniform in L. The
proved disk (3.1) itself shrinks with M. Sending L to infinity at a
fixed positive coupling cannot be justified by inserting that limit
in (5.3).

## 6. Relation to the spectral target and literature

Equations (2.2)--(2.6) give the exact energy-current map and spectral
measure for these physical states at arbitrary positive coupling.
Equations (3.6)--(5.5) calculate the actual first surviving coefficient
after the local electric/magnetic cancellation. In this explicit regime
the cancellation produces the two adjacent-face channels, with quotient
\(234\kappa/49\), rather than an arbitrarily small excitation energy.
It does not decide the joint large-volume, small-spacing quantum limit.
That limit requires control of the actual spectral measure (2.6) with
the original coupling and geometry retained; neither the smoothness of
a classical background nor the exact constant-weight zero state
supplies its nonzero low-energy weight.

The Hamiltonian conventions are those of J. Kogut and L. Susskind,
*Hamiltonian formulation of Wilson's lattice gauge theories*, Physical
Review D **11** (1975), 395--408,
<https://doi.org/10.1103/PhysRevD.11.395>, with the explicit metric and
coefficient dictionary in (1.2). The use of an observable applied to
the true vacuum and a ratio of its spectral moments belongs to the
variational tradition exemplified by R. P. Feynman, *Atomic Theory of
the Two-Fluid Model of Liquid Helium*, Physical Review **94** (1954),
262--277, <https://doi.org/10.1103/PhysRev.94.262>. No helium structure
factor or helium dispersion is imported into this gauge theory.

For compact-graph gauge projection, a primary comparison is B. Bahr
and T. Thiemann, *Gauge-invariant coherent states for loop quantum
gravity. II. Non-Abelian gauge groups*, Classical and Quantum Gravity
**26** (2009), 045012, <https://doi.org/10.1088/0264-9381/26/4/045012>,
<https://arxiv.org/abs/0709.4636>. Its product-Haar vertex projection
acts on the same kind of compact link Hilbert space. Here the seed
is the actual interacting Wilson vacuum, not a heat-kernel coherent
state; no gravitational dynamics is identified with H.

The four-dimensional quantum target is the construction and spectral
statement in A. Jaffe and E. Witten, *Quantum Yang--Mills Theory*,
<https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf>.
No continuum construction or mass-gap disproof is claimed in this note.
