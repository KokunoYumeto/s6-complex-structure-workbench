# The actual first physical excitation band of the open SU(2) box

8 September 2026. The calculation below concerns the eigenvalues of the full
interacting Hamiltonian, not only the energy of a chosen trial state. It retains
all spatial links and plaquettes, the two shared-link spin channels, the actual
vacuum energy, and the original physical coefficients. Its finite-box error
bound is explicit. The large-box limit computed here is a limit of a Taylor
coefficient, not an interchange of the volume and coupling limits.

## 1. Hamiltonian and the result

Fix an integer \(L\geq2\). The vertices are
\(\mathsf V_L=\{-L,\ldots,L\}^3\). Let \(\mathsf E_L\) contain
each positively oriented nearest-neighbor link \(e=(n,i)\) whose endpoints
belong to this set, and let \(\mathsf P_L\) contain every elementary square
\(p=(n;i,j)\), \(i<j\), including the boundary squares. Write
\[
 m=2L,\qquad N=3m(m+1)^2,\qquad M=3m^2(m+1).
\tag{1.1}
\]
For \(U_e\in SU(2)\), inverse traversal means \(U_e^{-1}\), and
\[
 W_p(U)=\operatorname{tr}\!left(
 U_i(n)U_j(n+\mathbf e_i)U_i(n+\mathbf e_j)^{-1}U_j(n)^{-1}\right).
\tag{1.2}
\]
The trace is real. Use product Haar probability measure on \(SU(2)^N\),
\(T_a=-i\sigma_a/2\), and
\[
 X_{e,a}f=\left.\frac{d}{dt}f(\ldots,e^{tT_a}U_e,\ldots)\right|_{t=0},
 \qquad E_e=-\sum_{a=1}^3X_{e,a}^2.
\tag{1.3}
\]
The spin-\(j\) eigenvalue of \(E_e\) is \(j(j+1)\). In particular the
fundamental value is \(3/4\). The original Lie metric
\(c(A,B)=-\operatorname{tr}(AB)/2\) has orthonormal basis \(2T_a\),
so \(-\Delta_e^c=4E_e\); this factor is retained in
\[
 \begin{split}
 H&=\kappa H_0+b\sum_p(2-W_p)
    =\kappa K_\xi+2bM I,\qquad H_0=\sum_eE_e,\\
 K_\xi&=H_0-\xi S,\qquad S=\sum_pW_p,\\
 \kappa&=\frac{2g_{\rm YM}^2}{a},\qquad
 b=\frac{1}{2g_{\rm YM}^2a},\qquad
 \xi=\frac b\kappa=\frac{1}{4g_{\rm YM}^4}.
 \end{split}
\tag{1.4}
\]
Here \(a>0\) is spatial lattice spacing. There are three spatial dimensions
and Hamiltonian time. No spatial dimension, link, or interaction is removed.

The physical Hilbert space \(\mathcal H_{\rm phys}\) is the closed subspace
of \(L^2(SU(2)^N,dU)\) invariant under
\(U_e\mapsto g_{s(e)}U_eg_{t(e)}^{-1}\) at every vertex. Both \(H_0\) and
\(S\) preserve it. The full operator has Sobolev domain \(H^2\) and form
domain \(H^1\); on the physical subspace use their intersections with
\(\mathcal H_{\rm phys}\). Bounded smooth multiplication by \(S\) preserves
self-adjointness and compact resolvent. The heat kernel of the link Laplacian
is strictly positive on the connected compact configuration space, and the
bounded real potential preserves positivity improvement by its heat-kernel
product formula. Consequently the lowest eigenfunction can be chosen
strictly positive and is unique up to a scalar. Alternatively, its modulus
minimizes the form, elliptic regularity and the maximum principle make it
strictly positive, and integration by parts gives
\[
 \langle\psi f,(H-\mathcal E)\psi f\rangle
   =\kappa\sum_{e,a}\int|X_{e,a}f|^2\psi^2dU.
\tag{1.5}
\]
Any other lowest eigenfunction divided by \(\psi\) is therefore constant.
Gauge transformations fix this positive unit vector. Thus the full and
physical bottoms agree. Write
\(\mathcal E(\xi)=2bM+\kappa e(\xi)\), and let
\(\operatorname{gap}_L\) be the least strictly positive physical eigenvalue
of \(H-\mathcal E(\xi)I\).

Define the finite face graph as follows. Two distinct faces are adjacent
exactly when they share a physical edge. Its adjacency matrix is
\(A_L\), its face degrees are \(d_p\), and
\[
 D_L^{\rm face}=\operatorname{diag}(d_p),\qquad
 Q_L=D_L^{\rm face}+A_L,\qquad q_L=\lambda_{\max}(Q_L),\qquad
 \nu_L=\frac7{15}-\frac{q_L}{21}.
\tag{1.6}
\]
The superscript distinguishes this degree matrix from any original cusp
determinant. No cusp coordinate or determinant has been identified with it.

The result is
\[
 \boxed{\operatorname{gap}_L
   =\kappa\left(3+\nu_L\xi^2+\mathcal R_L(\xi)\right),\qquad
 |\mathcal R_L(\xi)|\leq
 \frac73\left(\frac{64M}{3}\right)^4|\xi|^4,
 \quad |\xi|\leq\frac{3}{128M}.}
\tag{1.7}
\]
The error bound concerns the actual physical eigenvalue. Moreover
\[
 \boxed{0<\nu_L+\frac{71}{105}
       \leq\frac{4(6L+1)}{21L(2L+1)},\qquad
       \lim_{L\to\infty}\nu_L=-\frac{71}{105}.}
\tag{1.8}
\]
In particular \(\nu_L<0\) for every \(L\geq2\). The original coefficients
in (1.7) are equivalently
\[
 \operatorname{gap}_L=
 \frac{6g_{\rm YM}^2}{a}
 +\frac{\nu_L}{8g_{\rm YM}^6a}
 +\frac{2g_{\rm YM}^2}{a}\mathcal R_L\!\left(\frac1{4g_{\rm YM}^4}\right).
\tag{1.9}
\]
Thus no change of energy units or coupling is hidden in the negative second
coefficient. Sections 2--6 prove all parts of these statements.

## 2. The free physical eigenspace and its isolation

Peter--Weyl decomposition on each link gives an orthogonal decomposition by
spin assignments \((j_e)\). Gauge invariance is imposed by taking the invariant
tensor space at each vertex, with dual representations on oppositely oriented
indices. This is an orthogonal projection because it is the integral of the
unitary vertex action. Tensor products of the resulting invariant contractions
span the physical subspace, by applying that bounded projection to the dense
product Peter--Weyl span. Their free energies are exactly
\(\sum_ej_e(j_e+1)\).

The support of a nonconstant such contraction is the graph of links with
\(j_e>0\). It cannot have a vertex of degree one: its tensor factor there
would be a single nontrivial irreducible representation, which has no
invariant vector. Every nonempty finite graph of minimum degree at least two
contains a cycle, by continuing an edge path until a vertex repeats. The
cubic lattice graph is simple and bipartite, so every cycle has length at
least four. Each support edge contributes at least \(3/4\). Hence every
nonzero physical energy is at least \(3\).

If the energy is strictly below \(9/2\), there are at most five support
edges. A cycle in this bipartite graph must then have length four. A fifth
edge cannot form a separate component of minimum degree two, cannot have an
endpoint outside the four-cycle without producing degree one, and cannot
be a chord: the possible new chords join vertices in the same bipartition
class. Therefore the support is just that four-cycle. Every four-cycle in
the cubic nearest-neighbor graph is one elementary square: closing a
four-step simple path requires one positive and one negative step in each
of two distinct coordinate directions.

At a degree-two vertex, Schur orthogonality implies that an invariant
contraction exists only when the two incident spins agree; it is then
one-dimensional. Thus a square has the same spin \(j\) on all four edges,
with energy \(4j(j+1)\). Below \(9/2\), only \(j=1/2\) occurs, giving
energy \(3\) and the fundamental Wilson trace \(W_p\). The next possible
physical energy is exactly \(9/2\), realized by the fundamental trace on a
six-edge \(1\)-by-\(2\) rectangle in the box.

Single-link Haar integration gives
\[
 \int W_p\,dU=0,\qquad \langle W_p,W_q\rangle=\delta_{pq},\qquad
 H_0W_p=3W_p.
\tag{2.1}
\]
For distinct squares a link in only one boundary makes the integral zero
under multiplication of that link by \(-I\). For equal squares their
holonomy is Haar distributed and the fundamental character has squared norm
one. This last identity also follows by writing a Haar element as
\(u_0I+i\sum_au_a\sigma_a\) on the unit three-sphere and using
\(\int u_0^2=1/4\). Consequently
\[
 \ker H_0=\mathbb C1,\qquad
 \ker(H_0-3)=\mathcal P:=\operatorname{span}\{W_p:p\in\mathsf P_L\},
 \qquad\operatorname{spec}(H_0)\cap(3,9/2)=\varnothing.
\tag{2.2}
\]
In this section spectra and kernels are physical ones. Let \(P\) be the
orthogonal projection onto \(\mathcal P\), let \(Q=I-P\) on the physical
space, and set
\[
 R_3=Q\bigl(Q(H_0-3)Q\bigr)^{-1}Q.
\tag{2.3}
\]
The inverse is bounded, since zero is excluded by (2.2). It acts by
\(-1/3\) on constants. Omitting this negative denominator would give an
incorrect excitation matrix.

## 3. Every virtual channel, with its exact Haar map

The elementary central link map
\[
 U_{(n,i)}\longmapsto z_i(n)U_{(n,i)},\qquad
 z_i(n)=(-1)^{\sum_{j<i}n_j}I
\tag{3.1}
\]
induces a Haar unitary involution \(\mathcal Z\). Around an \(ij\) face
with \(i<j\), the exponent in \(z_j(n+\mathbf e_i)\) differs by one
from that in \(z_j(n)\), while the other pair agrees. Thus every
\(W_p\) changes sign. The map commutes with every link Casimir and every
vertex gauge action, fixes the constant function, and is \(-I\) on
\(\mathcal P\). It follows in particular that \(PSP=0\).

Resolve the product of two face traces as follows. For a repeated face put
\(Y_p=W_p^2-1\). The character identity
\(\chi_{1/2}^2=\chi_0+\chi_1\) gives
\[
 H_0Y_p=8Y_p,\qquad\|Y_p\|^2=1.
\tag{3.2}
\]
For two distinct edge-disjoint faces, \(W_pW_q\) has energy \(6\) and
squared norm one, even if their boundaries meet at a vertex. Each of the
eight links has fundamental spin; integration of one independent link of
each face establishes the norm.

If distinct \(p,q\) share one edge \(e\), define the exact orthogonal
Haar projection and its complement
\[
 Z_{pq,0}=\int_{SU(2)}W_pW_q\,dU_e,\qquad
 Z_{pq,1}=W_pW_q-Z_{pq,0}.
\tag{3.3}
\]
Reverse one face traversal if needed, which preserves its real SU(2) trace,
and cyclically write the traces as \(\operatorname{tr}(U_eA)\) and
\(\operatorname{tr}(U_e^{-1}B)\). The six outer link variables in A,B
are distinct. The identity
\(\int U_{ij}\overline U_{kl}\,dU=\delta_{ik}\delta_{jl}/2\) gives
\[
 Z_{pq,0}=\tfrac12\operatorname{tr}(AB).
\tag{3.4}
\]
This is the fundamental trace on their six-edge boundary with its actual
factor \(1/2\), not a trace rescaled to unit norm. The shared-edge tensor
product decomposes into spin zero and spin one. Hence
\[
 \begin{array}{c|cc}
 &Z_{pq,0}&Z_{pq,1}\\ \hline
 H_0\text{ eigenvalue}&9/2&13/2\\
 \text{squared norm}&1/4&3/4\\
 R_3\text{ multiplier}&2/3&2/7
 \end{array}
\tag{3.5}
\]
The first norm follows from (3.4). The total product norm is one by
integrating the outer independent Haar words A and B first, and the two
channels are orthogonal because (3.3) is an orthogonal projection.

There are no missing cross terms between different unordered pairs.
Indeed a product associated with \(\{p,q\}\) has odd central-link parity
precisely on \(\partial p\mathbin\triangle\partial q\), in either channel.
If two different unordered pairs had the same boundary parity, the symmetric
difference of their face sets would be a nonempty closed mod-two collection
of at most four squares. Any square in it would need another square on each
of its four edges. Distinct elementary squares share at most one edge, so
four distinct other squares would be necessary, contradicting the maximum
of four squares in the collection. Thus some link has unequal parity and
its Haar integration kills every mixed inner product. The repeated-face
vectors have even parity everywhere, so are orthogonal to these pairs;
different repeated-face vectors are orthogonal by their different joint
link-spin assignments. All these orthogonalities remain true after applying
\(H_0\) or \(R_3\).

For \(v=\sum_pa_pW_p\), the entire first-order dressing of the spectral
subspace is consequently
\[
 \begin{split}
 R_3Sv={}&-\frac13\sum_pa_p
 +\frac15\sum_pa_pY_p\\
 &+\frac13\sum_{\{p,q\}\ {m edge\!\!-\!\!disjoint}}
                      (a_p+a_q)W_pW_q\\
 &+\sum_{\{p,q\}\ {\rm adjacent}}(a_p+a_q)
                  \left(\frac23Z_{pq,0}+\frac27Z_{pq,1}\right).
 \end{split}
\tag{3.6}
\]
The sums over distinct pairs are unordered. This is an exact map from each
free physical face vector into all of its first-order virtual states.

## 4. Degenerate perturbation and the vacuum subtraction

The second effective coefficient before subtracting the bottom energy is
\[
 K^{(2)}=-PSR_3SP.
\tag{4.1}
\]
For completeness, this follows directly by writing the analytically
transported vector as \(v+\xi v_1+\xi^2v_2+\cdots\) with
\(Pv_1=0\). The first coefficient of the eigen-equation or spectral
intertwining equation gives \((H_0-3)v_1=QSv\), hence \(v_1=R_3Sv\).
Projecting the next coefficient onto \(\mathcal P\) gives (4.1).
This works for the whole degenerate subspace; no individual face is assumed
to remain an eigenvector. The exact analytic subspace map used here is
constructed in Section 5.

The vacuum intermediate state contributes \(+1/3\) to every matrix entry
in the \(W_p\) basis. A distinct edge-disjoint pair contributes
\(-1/3\) to its two diagonal entries and its two mutual off-diagonal
entries. An adjacent pair contributes the same pattern with value
\[
 -\left(\frac{1/4}{9/2-3}+\frac{3/4}{13/2-3}\right)
       =-\left(\frac16+\frac3{14}\right)=-\frac8{21}.
\tag{4.2}
\]
A repeated-face channel contributes \(-1/5\) to its diagonal. Therefore
\[
 \begin{split}
 K^{(2)}_{pp}
  &=\frac13-\frac15-\frac{M-1-d_p}{3}-\frac8{21}d_p
    =\frac7{15}-\frac M3-\frac{d_p}{21},\\
 K^{(2)}_{pq}
  &=\begin{cases}-1/21,&p,q\text{ adjacent},\\0,&p\ne q\text{ not adjacent}.
    \end{cases}
 \end{split}
\tag{4.3}
\]
In particular the nonlocal rank-one vacuum contribution cancels the
edge-disjoint off-diagonal contribution, rather than either one being omitted.

For the actual positive unit vacuum, coefficient comparison yields
\[
 \psi_\xi=1+\frac\xi3S+O_{H^2,L}(\xi^2),\qquad
 e(\xi)=-\frac M3\xi^2+O_L(\xi^4).
\tag{4.4}
\]
The first equation follows because \(H_0S=3S\). Pairing the second-order
equation with constants gives \(-\langle S,S\rangle/3=-M/3\).
The error is even by (3.1), as proved below. Thus the physical excitation
coefficient is
\[
 \boxed{F_L=K^{(2)}+\frac M3I
          =\frac7{15}I-\frac1{21}(D_L^{\rm face}+A_L).}
\tag{4.5}
\]
The first term in (3.6) also explicitly checks the vacuum-orthogonality
sign. Pairing \(v+\xi R_3Sv\) with (4.4) gives at order \(\xi\)
the two cancelling scalars \(-\sum_pa_p/3\) and \(+\sum_pa_p/3\).
The exact transported subspace is orthogonal to the exact vacuum at real
coupling, since their spectral contours are disjoint.

## 5. Exact spectral transport, evenness, and an explicit remainder

This section supplies the operator error bound in (1.7). Work throughout in
\(\mathcal H_{\rm phys}\). Put
\[
 r=\frac{3}{64M},\qquad \mathcal C_3=\{z:|z-3|=3/4\}.
\tag{5.1}
\]
On \(\mathcal C_3\), equation (2.2) gives
\(\|(z-H_0)^{-1}\|\leq4/3\). Since \(\|S\|=2M\), the Neumann
factor is at most \(1/8\) for complex \(|\xi|\leq r\). Equality in
\(\|S\|=2M\) follows from the all-identity link configuration and its
positive-measure neighborhoods. Consequently the analytic resolvent
\(R_\xi(z)=(z-K_\xi)^{-1}\) satisfies
\[
 \|R_\xi(z)\|\leq\frac{32}{21},\qquad
 P_\xi=\frac1{2\pi i}\int_{\mathcal C_3}R_\xi(z)\,dz,
 \qquad \|P_\xi-P\|\leq\frac17.
\tag{5.2}
\]
For the last bound, integrate the resolvent difference, using
\((3/4)(4/3)^2(2Mr)/(1-1/8)=1/7\). The contour integral is an
idempotent of rank M, by its continuous deformation from P.

On \(\mathcal P\) set \(T_\xi=PP_\xi P|_{\mathcal P}\). The convergent
binomial series at I defines \(T_\xi^{-1/2}\) analytically, since
\(\|T_\xi-I\|\leq1/7\), with
\(\|T_\xi^{-1/2}\|\leq\sqrt{7/6}\). Define exact maps
\[
 V_\xi=P_\xi P T_\xi^{-1/2}:\mathcal P\longrightarrow
                    \operatorname{ran}P_\xi,\qquad
 U_\xi=T_\xi^{-1/2}PP_\xi:\operatorname{ran}P_\xi\longrightarrow
                    \mathcal P.
\tag{5.3}
\]
Idempotence gives \(U_\xi V_\xi=I\); equal finite dimensions give
the reverse identity on \(\operatorname{ran}P_\xi\). For real \(\xi\),
\(P_\xi\) is orthogonal, \(U_\xi=V_\xi^*\), and \(V_\xi\) is an
isometry. Formula (5.3) retains the whole Gram factor; it is not a removal
of a physical field amplitude or scale. Its derivative at zero has
\(PV'_0=0\), as differentiating \(P_\xi^2=P_\xi\) gives
\(PP'_0P=0\). Differentiating its spectral intertwining equation then
gives exactly \(V'_0=R_3SP\), as used in (3.6) and (4.1).

The exact finite matrix representing the cluster is
\[
 B_\xi=U_\xi K_\xi V_\xi
      =T_\xi^{-1/2}P(K_\xi P_\xi)P T_\xi^{-1/2}.
\tag{5.4}
\]
The products are bounded because \(K_\xi P_\xi\) is its contour integral
\((2\pi i)^{-1}\int zR_\xi(z)dz\). In particular
\[
 \begin{split}
 \|B_\xi-3I\|
 &\leq\frac76\left\|\frac1{2\pi i}
       \int_{\mathcal C_3}(z-3)R_\xi(z)\,dz\right\|\\
 &\leq\frac76\left(\frac34\right)^2\frac{32}{21}=1.
 \end{split}
\tag{5.5}
\]
The corresponding contour \(|z|=3/4\) around the physical free bottom
has the same resolvent bounds and rank one. Its unique eigenvalue e(ξ)
is analytic and lies within that circle, so \(|e(\xi)|\leq3/4\).

Equation (3.1) gives \(K_{-\xi}=\mathcal ZK_\xi\mathcal Z\),
\(P_{-\xi}=\mathcal ZP_\xi\mathcal Z\), and
\(T_{-\xi}=T_\xi\), since \(\mathcal ZP=-P\). Thus
\(V_{-\xi}=-\mathcal ZV_\xi\), \(U_{-\xi}=-U_\xi\mathcal Z\), and
\[
 B_{-\xi}=B_\xi,\qquad e(-\xi)=e(\xi).
\tag{5.6}
\]
These are analytic identities, not a choice of labels at a degenerate
eigenvalue. Therefore the matrix
\(G_\xi=B_\xi-e(\xi)I-3I\) is even analytic on \(|\xi|\leq r\),
has \(G_0=0\), has second coefficient F_L by (4.5), and has norm at
most \(7/4\). Cauchy's coefficient estimate followed by the geometric
series gives, for \(|\xi|\leq r/2\),
\[
 \|G_\xi-\xi^2F_L\|
 \leq\frac74\sum_{k\geq2}\left(\frac{|\xi|}{r}\right)^{2k}
 \leq\frac73r^{-4}|\xi|^4.
\tag{5.7}
\]
There is a neighborhood beyond the closed radius r where the contours and
series above exist, since each displayed Neumann and Gram bound is strict
at its analytic threshold, so Cauchy's estimate at r is legitimate.

For real \(|\xi|\leq r/2\), the perturbation norm is at most
\(2M|\xi|\leq3/64\). The min--max principle moves each ordered physical
eigenvalue of H_0 by no more than this number. There is one bottom, M
eigenvalues near 3, and all remaining eigenvalues are at least
\(9/2-3/64\); hence the first positive physical excitation is precisely
the lowest eigenvalue of \(\kappa(B_\xi-e(\xi)I)\). For Hermitian
matrices the min--max principle bounds the change of every ordered
eigenvalue by the perturbation norm. Applying it to (5.7), and observing
that \(\lambda_{\min}(F_L)=7/15-q_L/21\), proves (1.7), including its
absolute error bound.

The constant \(2bM\) has not disappeared by fiat: both the ground energy
and every physical cluster eigenvalue of H are their K_ξ counterparts
multiplied by κ and then increased by \(2bM\). Their difference is (1.7).

## 6. The unchanged open-box graph and its coefficient limit

For a link in direction i, let j,k be the other directions and put
\[
 a_j(n_j)=\begin{cases}1,&n_j=\pm L,\\2,&-L<n_j<L.\end{cases}
 \qquad r_e=a_j(n_j)+a_k(n_k).
\tag{6.1}
\]
This is exactly the number of faces incident to e. The face degree is
\(d_p=\sum_{e\in\partial p}(r_e-1)\), since two different squares
share at most one edge. Hence \(d_p\leq12\), with strict inequality
for some boundary faces. The number \(\mathcal A_L\) of unordered
adjacent face pairs is
\[
 \mathcal A_L=\sum_e\binom{r_e}{2}=144L^3-12L.
\tag{6.2}
\]
Here are the finite sums establishing the coefficient. For either transverse
coordinate, \(\sum a_j=2m\) and \(\sum a_j^2=4m-2\). For one direction
i, summing \(r_e(r_e-1)\) over the two transverse coordinates gives
\[
 2(m+1)(4m-2)+2(2m)^2-2(m+1)(2m)=12m^2-4.
\]
There are m positions along i, three choices of i, and the factor \(1/2\)
in (6.2), giving \(18m^3-6m=144L^3-12L\). In particular
\(\sum_pd_p=2\mathcal A_L\).

The constant face vector gives the Rayleigh lower bound
\[
 q_L\geq\frac{4\mathcal A_L}{M}
       =\frac{48L^2-4}{L(2L+1)},\qquad q_L\leq24.
\tag{6.3}
\]
The upper bound follows from the maximum absolute row sum of Q_L, equal
to \(2\max_pd_p\leq24\). It is strict. The face graph is connected:
within a coordinate plane the square tiling is connected by edge adjacency;
neighboring parallel layers connect through a square in a transverse plane,
and that same adjacency joins the three plane orientations. A maximizing
eigenvector of the real symmetric nonnegative Q_L can be chosen nonnegative,
because replacing its entries by their absolute values does not decrease
its quadratic form. Connectedness and the eigen-equation make all entries
positive. If its eigenvalue were 24, an entry of maximum size would force
its degree to equal 12 and every neighboring entry to have the same size.
Propagation through the connected graph would force every face degree to
equal 12, contradicting the boundary faces. Thus \(q_L<24\).

Subtracting (6.3) from 24 gives
\[
 0<24-q_L\leq\frac{24L+4}{L(2L+1)}.
\tag{6.4}
\]
Equations (1.6) and (6.4) prove (1.8). Also
\(24-(24L+4)/(L(2L+1))\geq24-14/L\geq17\) for \(L\geq2\).
Since \(17>49/5\), (6.3) gives \(\nu_L<7/15-(49/5)/21=0\).
This proof used the actual open incidence sets, not periodic boundaries.

## 7. Meaning of the coefficient and relation to previous states

At each fixed box, the interacting first physical eigenvalue decreases from
\(3\kappa\) at second order in ξ. This statement is stronger than a
change in one proposed Rayleigh quotient: Sections 2 and 5 isolate the
entire first physical cluster, and Section 4 diagonalizes its full
second-order operator. Its neighbor coefficient \(-1/21\) and the
degree contribution are exact effects of both retained spin channels.

The earlier electric and magnetic-translation trial families have leading
energy \(3\kappa\) in their non-kernel directions. The exact map from
that leading face space to the actual first spectral subspace is V_ξ in
(5.3), with the first correction (3.6). It includes the vacuum subtraction,
repeated-face spin-one terms, all edge-disjoint pairs, and all hinged or
coplanar adjacent pairs. Thus this calculation supplies their full first
spectral dressing rather than claiming those trial families and the
physical spectrum are unrelated.

No zero of a truncated polynomial is asserted to be a zero of the physical
gap. The guaranteed interval in (1.7) shrinks as \(M^{-1}\), while its
explicit fourth-order bound grows as \(M^4\). Equation (1.8) is a
coefficient limit and does not prove a fixed-positive-coupling infinite-volume
limit of (1.7). The state-space and spectral transport are exact at each
finite box; extending the spectral estimates to the original interacting
spatial continuum remains a mathematical calculation not supplied by this
coefficient alone.

## 8. Primary literature and attribution of this calculation

The Hamiltonian lattice framework is that of J. Kogut and L. Susskind,
*Hamiltonian formulation of Wilson's lattice gauge theories*, Physical
Review D **11** (1975), 395--408,
<https://doi.org/10.1103/PhysRevD.11.395>. Equations (1.3)--(1.4) give
the complete conventions actually used here, rather than borrowing a
coefficient from a differently parametrized Hamiltonian.

Strong-coupling scalar-gap series in three spatial dimensions already have
an extensive literature, including A. C. Irving, T. E. Preece, and C. J.
Hamer, *Cluster expansion approach to non-abelian lattice gauge theory in
(3+1)D (I). SU(2)*, Nuclear Physics B **270** (1986), 536--552,
<https://doi.org/10.1016/0550-3213(86)90567-5>. The publisher's abstract
identifies its vacuum-energy, string-tension and scalar-gap expansions.
The present derivation is self-contained and does not claim historical
novelty for a strong-coupling coefficient; no unread coefficient table from
that article is used as a proof or as a claimed numerical match.

The interacting four-dimensional continuum target is the construction and
spectral assertion in A. Jaffe and E. Witten, *Quantum Yang--Mills Theory*,
<https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf>.
Neither that continuum construction nor a counterexample to its mass-gap
assertion is claimed by the finite-box result (1.7).
