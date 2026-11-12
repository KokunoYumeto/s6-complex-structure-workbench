# The actual first physical excitation band: independent derivation

8 September 2026. This calculation retains the full finite open three-
dimensional spatial Wilson box, every plaquette, the actual ground energy,
and all virtual channels. It computes the degenerate first physical
excitation cluster, not a single trial quotient. All perturbative
statements are at a fixed finite box unless an explicit coefficient
limit is separately stated.

## 1. Original Hamiltonian and physical Hilbert space

Fix an integer \(L\geq2\), vertices
\(\mathsf V_L=\{-L,\ldots,L\}^3\), and every positive physical link
\(e=(n,i)\) whose endpoints lie in the box. A negative traversal uses
the inverse of that same variable \(U_e\in SU(2)\). Every elementary
face \(p=(n;i,j)\), \(i<j\), is retained, with
\[
W_p=\operatorname{tr}\bigl[
U_i(n)U_j(n+\mathbf e_i)
U_i(n+\mathbf e_j)^{-1}U_j(n)^{-1}\bigr].
\]
The numbers of links and faces are
\[
N=3(2L)(2L+1)^2,\qquad M=3(2L)^2(2L+1).
\]
Use product Haar probability measure on \(SU(2)^N\), an inner product
conjugate-linear in its first argument, and the original derivatives
\[
T_a=-i\sigma_a/2,\qquad
X_{e,a}F=\left.\frac{d}{dt}\right|_0
F(\ldots,e^{tT_a}U_e,\ldots),\qquad
E_e=-\sum_aX_{e,a}^2,\qquad H_0=\sum_eE_e .
\]
The metric \(c(A,B)=-\operatorname{tr}(AB)/2\) has orthonormal basis
\(2T_a\), hence \(-\Delta_e^c=4E_e\). Retain
\[
H=\kappa(H_0-\xi S)+2bM I,\qquad
S=\sum_pW_p,\quad \xi=b/\kappa,\quad
\kappa=\frac{2g_{\rm YM}^2}{a},\quad
b=\frac1{2g_{\rm YM}^2a}.
\tag{1.1}
\]
Both \(\kappa,b\) are positive in the physical model.

Let \(\Pi\) be product vertex Haar projection for
\(U_e\mapsto g_sU_eg_t^{-1}\), and let
\(\mathcal H_{\rm phys}=\Pi L^2(SU(2)^N)\).
Every link Casimir is bi-invariant and every face trace is gauge
invariant. Thus \(H_0,S,H\) reduce this physical subspace. On it,
the operator domain is \(H^2\cap\mathcal H_{\rm phys}\) and the
form domain is \(H^1\cap\mathcal H_{\rm phys}\).
The bounded smooth multiplication by \(S\), of norm \(2M\), preserves
self-adjointness and compact resolvent. The strictly positive smooth
normalized full ground state \(\psi_\xi\) is unique: a ground form
minimizer can be replaced by its modulus; elliptic regularity and the
strong maximum principle give positivity; integration by parts gives
\[
\mathfrak q_{H-\mathcal E_0}[\psi_\xi F]
=\kappa\sum_{e,a}\int\psi_\xi^2|X_{e,a}F|^2\,dU .
\]
A second ground eigenfunction divided by \(\psi_\xi\) must therefore
be constant. Gauge transformations fix the unique positive normalized
ground state, so it belongs to \(\mathcal H_{\rm phys}\).

## 2. Exact free physical eigenspace and upward gap

The product Peter--Weyl decomposition labels each edge by
\(j_e\in\{0,\tfrac12,1,\ldots\}\), with Casimir \(j_e(j_e+1)\).
The fundamental value is \(3/4\), since
\(-\sum_aT_a^2=3I/4\). At each vertex, the Haar projection is the
projection onto invariant tensors of the incident representation
indices, with duals chosen according to edge orientation.

Ignore spin-zero edges and call the remaining edge graph the active
support. A vertex of degree one in this graph has a single nontrivial
irreducible representation and no invariant tensor. Its Haar projector
is zero. Thus every nonempty active component of a physical coefficient
has minimum degree at least two. Such a finite component contains a
cycle. The open cubic graph is simple and bipartite, with parity
\(n_1+n_2+n_3\bmod2\), so every cycle has length at least four.

If a physical free energy is below \(9/2\), it has at most five active
edges, since each contributes at least \(3/4\). There can be only
one active component: two components would each require at least
four edges. A connected simple bipartite graph with minimum degree
two and at most five edges must be a four-cycle. To prove this,
its number of vertices is at most its number of edges. Three or
fewer vertices cannot support a bipartite cycle. With four vertices
the bipartite graph has at most four edges, so it is a four-cycle.
With five vertices and at most five edges, minimum degree two
forces every degree to be two, giving a five-cycle, impossible
in a bipartite graph.

At a degree-two vertex, an invariant tensor between two incident
irreducible representations exists only when their spins agree;
its dimension is then one by Schur's lemma and self-duality of
\(SU(2)\) representations. Thus the spin is the same around this
four-cycle. Its energy is \(4j(j+1)\), equal to 3 for \(j=1/2\)
and at least 8 for the next nonzero spin. Every simple four-cycle
in the unit cubic graph is an elementary square: its closed
four-step displacement uses two different coordinate directions,
each once positively and once negatively. Its invariant fundamental
contraction is precisely \(W_p\).

The Haar identities are
\[
\int W_p\,dU=0,\qquad
\langle W_p,W_q\rangle=\delta_{pq}.
\tag{2.1}
\]
Distinct faces have different edge supports; central multiplication
of an edge in only one face by \(-I\) annihilates the mixed integral.
For equal faces Haar invariance reduces the norm to
\(\int(\operatorname{tr}U)^2dU=1\).
Consequently the free physical spectrum starts with
\[
\boxed{\lambda_0=0\text{ simple},\qquad
\lambda_1=\cdots=\lambda_M=3,\qquad
\operatorname{span}\{W_p:p\in\mathsf P_L\}
=\ker(H_0-3)\cap\mathcal H_{\rm phys}.}
\tag{2.2}
\]
There is no other physical eigenvalue in \((0,9/2)\).
A fundamental trace around a \(1\times2\) rectangle uses six distinct
edges and is gauge invariant, with energy \(6(3/4)=9/2\).
Such a rectangle exists in every stated box. Hence the next distinct
physical eigenvalue is exactly \(9/2\); the upward isolation of the
first cluster is exactly \(3/2\).

## 3. Fixed-box analytic cluster and exact even effective matrix

Let \(P\) be the physical orthogonal projection onto the span in (2.2),
and \(Q=I-P\) on the physical Hilbert space. Define
\[
K_\xi=H_0-\xi S .
\]
On the circle \(|z-3|=3/4\), the free physical resolvent norm is at
most \(4/3\). Since \(\|S\|=2M\), its Neumann parameter is
\(q=8M|\xi|/3\). The perturbed spectral projection \(P_\xi\) around
this circle is analytic for \(|\xi|<3/(8M)\). In the smaller disk
\[
|\xi|<\frac3{16M},
\tag{3.1}
\]
the contour bound gives
\(\|P_\xi-P\|\leq q/(1-q)<1\). For real \(\xi\), \(P_\xi\) is
orthogonal of rank \(M\). The bounded-perturbation min--max bound
moves each ordered free eigenvalue by at most \(2M|\xi|<3/8\).
Thus this cluster is still precisely the first \(M\) physical excited
eigenvalues: the ground remains separated below, and the next
physical free level remains above \(9/2-3/8\).

On \(\operatorname{ran}P\), put
\[
B_\xi=PP_\xi P,\qquad
V_\xi=P_\xi P B_\xi^{-1/2}.
\tag{3.2}
\]
For real \(\xi\) satisfying (3.1), \(B_\xi\) is positive invertible,
and \(V_\xi\) is an isometry from \(\operatorname{ran}P\) onto
\(\operatorname{ran}P_\xi\). Indeed
\(V_\xi^*V_\xi=B_\xi^{-1/2}B_\xi B_\xi^{-1/2}=I_P\);
the two spaces have equal finite dimension. Analytic matrix
functional calculus near \(B_0=I_P\) gives a real-analytic family.
The finite Hermitian matrix
\[
\mathsf A_\xi=V_\xi^*K_\xi V_\xi
\tag{3.3}
\]
has exactly the actual cluster eigenvalues. Its definition uses the
operator domain: the range of \(P_\xi\) consists of smooth eigenvectors.
Analyticity into \(H^2\), and then higher fixed Sobolev spaces, follows
from the contour resolvent and the elliptic eigen-equation.

The central cochain
\[
z_i(n)=(-1)^{\sum_{j<i}n_j}I,\qquad
\mathcal ZF(U)=F((z_eU_e)_e)
\]
is a real Haar-unitary involution commuting with \(H_0\) and \(\Pi\).
Every face sign is \(-1\): for \(i<j\), shifting \(z_j\) in direction
\(i\) changes its sign, while shifting \(z_i\) in direction \(j\)
does not. Thus \(\mathcal ZS\mathcal Z=-S\) and
\[
\mathcal Z|_{\operatorname{ran}P}=-I_P,\qquad
P_{-\xi}=\mathcal ZP_\xi\mathcal Z,\quad
B_{-\xi}=B_\xi,\quad
V_{-\xi}=-\mathcal ZV_\xi .
\]
Substituting in (3.3) proves the exact matrix equality
\[
\boxed{\mathsf A_{-\xi}=\mathsf A_\xi.}
\tag{3.4}
\]
In particular all its odd Taylor coefficients vanish; this is a
matrix identity, not an assumption about labels of crossing eigenvalues.
It also proves \(PSP=0\) directly: \(S\) is odd under \(\mathcal Z\),
while both external vectors belong to its negative eigenspace.

Define the bounded reduced free resolvent
\[
R_3=Q(H_0-3)^{-1}Q .
\tag{3.5}
\]
It is well-defined on the physical complement by (2.2), and equals
\(-1/3\) on the vacuum. Differentiating the invariant-subspace equation
at zero gives
\[
V_1:=V_\xi'|_0=R_3SP,\qquad PV_1=0.
\tag{3.6}
\]
For example \(Q(H_0-3)V_1=QSP\); differentiating the isometry and
its explicit positive-overlap convention in (3.2) gives the zero
in-cluster first derivative. Writing
\(V_\xi=P+\xi V_1+\xi^2V_2+\cdots\), normalization gives
\(PV_2+V_2^*P=-V_1^*V_1\).
The quadratic coefficient of (3.3) is therefore
\[
V_1^*(H_0-3)V_1-PSV_1-V_1^*SP
=-PSR_3SP .
\]
Together with (3.4),
\[
\boxed{\mathsf A_\xi=3I_P+\xi^2\mathsf K+O_L(\xi^4),\qquad
\mathsf K=-PSR_3SP.}
\tag{3.7}
\]
The remainder is in finite-matrix operator norm and follows from
convergent real-analytic Taylor expansion.

## 4. Every virtual channel, with complete orthogonality

For each external face \(p\),
\[
SW_p=W_p^2+\sum_{q\ne p}W_pW_q
=1+C_p+\sum_{q\ne p}W_pW_q,\qquad C_p=W_p^2-1 .
\tag{4.1}
\]
The repeated-face function \(C_p\) is the spin-1 character of the
face, with \(H_0C_p=8C_p\), Haar mean zero and squared norm 1.
Its norm follows from character orthogonality, or directly from
\(\int W_p^4=2\), \(\int W_p^2=1\).
Different repeated-face functions are orthogonal: an edge in one
face but not the other carries a nontrivial spin-1 matrix coefficient
with zero Haar integral.

For an edge-disjoint pair of distinct faces, \(W_pW_q\) has eight
fundamental edges, \(H_0\) eigenvalue 6, squared norm 1 and zero
mean. Sharing a vertex but no edge does not change these facts.

For an adjacent unordered pair with shared edge \(e\), invert and
cyclically rotate whole face traversals if needed, keeping their
unchanged \(SU(2)\) traces, to write
\[
W_p=\operatorname{tr}(U_eA),\qquad
W_q=\operatorname{tr}(U_e^{-1}B).
\]
The two outer three-edge paths \(A,B\) use six distinct physical
links. Fundamental Haar integration gives
\[
Z_{pq,0}=\int W_pW_q\,dU_e=\frac12\operatorname{tr}(AB),\qquad
Z_{pq,1}=W_pW_q-Z_{pq,0}.
\tag{4.2}
\]
The shared-edge channels are spins 0 and 1, while the six outer
edges are fundamental. Thus
\[
H_0Z_{pq,0}=\frac92Z_{pq,0},\qquad
H_0Z_{pq,1}=\frac{13}2Z_{pq,1}.
\tag{4.3}
\]
The projection integrating \(U_e\) is orthogonal. Independent Haar
integration of the outer paths gives
\[
\|Z_{pq,0}\|^2=\frac14,\qquad
\|W_pW_q\|^2=1,\qquad
\|Z_{pq,1}\|^2=\frac34,\qquad
\langle Z_{pq,0},Z_{pq,1}\rangle=0 .
\tag{4.4}
\]
These are the original normalizations; no channel is replaced by
the unhalved outer-loop trace.

All different unordered pair sectors are orthogonal. For any pair
of distinct faces, its odd-edge parity support is
\(\partial p\mathbin{\triangle}\partial q\), containing eight edges
for a disjoint pair and six for an adjacent pair. Each adjacent
channel has that same support: the shared edge is even, and the
six outer edges are odd. Distinct unordered pairs have distinct
parity supports. Otherwise their symmetric difference as face
chains would be a nonempty mod-2 2-cycle with at most four faces.
Choose a face in that cycle. Each of its four boundary edges
requires another face. Distinct elementary faces share at most
one edge, so four distinct additional faces would be needed,
at least five faces in total, a contradiction.

A central Haar transformation \(U_e\mapsto-U_e\) on an edge in
exactly one of two parity supports therefore kills their cross
inner product. It also makes every pair sector orthogonal to the
vacuum and all \(C_p\), which are even on every edge. The repeated-
face sectors are mutually orthogonal as proved above. These
arguments remain valid with \(R_3\) applied, since all listed
components are exact free eigenvectors. They exhaust (4.1).

The complete virtual data are consequently
\[
\begin{array}{c|c|c|c}
\text{sector}&H_0& H_0-3&\text{squared norm}\\ \hline
1&0&-3&1\\
C_p&8&5&1\\
W_pW_q\text{ edge-disjoint}&6&3&1\\
Z_{pq,0}\text{ adjacent}&9/2&3/2&1/4\\
Z_{pq,1}\text{ adjacent}&13/2&7/2&3/4
\end{array}
\tag{4.5}
\]
In particular the pair resolvent expectations are
\[
r_{\rm dis}=\frac13,\qquad
r_{\rm adj}=\frac{1/4}{3/2}+\frac{3/4}{7/2}
=\frac16+\frac3{14}=\frac8{21}.
\tag{4.6}
\]

For any \(v=\sum_pa_pW_p\), the first dressing (3.6) is explicitly
\[
\begin{split}
R_3Sv={}&-\frac13\sum_pa_p
+\frac15\sum_pa_pC_p\\
&+\frac13\sum_{\{p,q\}\ {\rm disjoint}}(a_p+a_q)W_pW_q\\
&+\sum_{\{p,q\}\ {\rm adjacent}}(a_p+a_q)
\left(\frac23Z_{pq,0}+\frac27Z_{pq,1}\right).
\end{split}
\tag{4.7}
\]
The negative vacuum component is essential. Since the actual ground
state begins \(1+\xi S/3+O_L(\xi^2)\), the order-\(\xi\) overlap
of \(V_\xi v\) with it is
\(-\sum_pa_p/3+\sum_pa_p/3=0\), as required.

## 5. The effective matrix and actual vacuum subtraction

Let two distinct faces be adjacent exactly when they share an edge.
Write \(\mathsf A_{\rm adj}\) for that zero-diagonal adjacency matrix,
\(r_e=\#\{p:e\in\partial p\}\), and
\[
d_p=\sum_{e\in\partial p}(r_e-1),\qquad
\mathsf D_{\rm adj}=\operatorname{diag}(d_p).
\tag{5.1}
\]
No other face is counted twice in \(d_p\), because distinct faces
share at most one edge.

For a diagonal matrix entry of \(\mathsf K\), (4.1)--(4.6) give
\[
\begin{split}
\mathsf K_{pp}
&=\frac13-\frac15-\frac{M-1-d_p}{3}
-\frac8{21}d_p\\
&=\frac7{15}-\frac M3-\frac{d_p}{21}.
\end{split}
\tag{5.2}
\]
The \(+1/3\) is the minus sign in (3.7) acting on the negative
vacuum denominator \(-3\). For distinct external faces \(p,q\),
the only shared virtual components in \(SW_p\) and \(SW_q\) are
the vacuum and the pair \(W_pW_q\). The orthogonality proof above
excludes every other mixed contribution. Thus
\[
\mathsf K_{pq}
=\frac13-r_{pq}
=\begin{cases}
0,&p,q\text{ not adjacent},\\
-1/21,&p,q\text{ adjacent}.
\end{cases}
\tag{5.3}
\]
Dropping vacuum mixing would incorrectly leave a nonlocal
off-diagonal \(-1/3\) for disjoint pairs.

The actual dimensionless ground energy is computed in the same full
Hilbert space. At first order its coefficient is zero since
\(\int S=0\). The first vacuum eigenvector coefficient is \(S/3\)
because \(H_0S=3S\). Integrating the next coefficient equation gives
\[
e_0(\xi)=-\frac13\langle S,S\rangle\xi^2+O_L(\xi^3)
=-\frac M3\xi^2+O_L(\xi^3).
\]
The central transformation \(\mathcal Z\) fixes the free vacuum
and conjugates \(\xi\) to \(-\xi\), so uniqueness makes this scalar
even. Hence
\[
\boxed{\mathcal E_0
=2bM-\kappa\frac M3\xi^2+O_L(\kappa\xi^4).}
\tag{5.4}
\]
The constant \(2bM\) remains in this absolute energy.

Subtracting this actual ground energy from the cluster (3.7),
the full effective excitation matrix is
\[
\boxed{
\mathsf F=\mathsf K+\frac M3I
=\frac7{15}I-\frac1{21}
(\mathsf D_{\rm adj}+\mathsf A_{\rm adj}).}
\tag{5.5}
\]
Thus the proposed signless-adjacency formula is correct with exactly
the stated face convention. It is not the ordinary graph Laplacian.

Let \(\nu_1\leq\cdots\leq\nu_M\) be the ordered eigenvalues of
\(\mathsf F\). Finite-dimensional min--max applied to the
operator-norm remainder in (3.7) yields all actual first-cluster
excitation energies, counted with multiplicity:
\[
\boxed{\mathcal E_j-\mathcal E_0
=3\kappa+\kappa\xi^2\nu_j+O_L(\kappa\xi^4),
\qquad 1\leq j\leq M.}
\tag{5.6}
\]
For fixed \(L\), the error is uniform over these finitely many
indices. This statement does not require unproved analyticity of
chosen eigenvectors through internal degeneracies.
The corresponding absolute energies are
\[
\mathcal E_j
=2bM+3\kappa
+\kappa\xi^2\left(\nu_j-\frac M3\right)
+O_L(\kappa\xi^4).
\tag{5.7}
\]
All original constants and the vacuum subtraction are visible.

## 6. Exact finite-box coefficient bounds

The face adjacency graph is connected. Coplanar edge-sharing steps
translate a face within its coordinate plane. To move a face one
step in its normal direction, use a hinged face joining an edge
of the original face to the corresponding edge at the next level;
the latter edge belongs to the translated parallel face. These
two adjacency steps are available whenever the target level is
inside the box. Hinged steps also connect the three face planes.
This connects every face to a fixed reference face.

Every edge belongs to at most four faces, so \(d_p\leq12\).
Interior faces attain 12, while boundary faces have smaller degree.
The nonnegative irreducible matrix
\(\mathsf Q=\mathsf D_{\rm adj}+\mathsf A_{\rm adj}\) consequently
has a simple largest eigenvalue \(q_{\max}\) and a strictly positive
eigenvector. Its row sums are \(2d_p\leq24\). They are not all 24.
The Perron eigenvalue is therefore strictly below 24: equality
would force every component adjacent to a maximum component of
its positive eigenvector to have that same maximum value, and
connectedness would then force all row sums to be 24.

The exact total degree can be counted by edge stars. For a
direction-\(i\) edge with transverse coordinates \(m,n\),
\[
r_e=a(m)+a(n),\qquad
a(t)=1\ \text{at }t=\pm L,\quad a(t)=2\ \text{otherwise}.
\]
Then
\(\sum a=4L\), \(\sum a^2=8L-2\), and
\(\sum(a^2-a)=4L-2\).
For each edge direction, summation over its \(2L\) initial longitudinal
coordinates and both transverse coordinates gives
\[
\sum_{e\text{ in that direction}}r_e(r_e-1)
=2L\bigl[2(2L+1)(4L-2)+2(4L)^2\bigr]
=96L^3-8L.
\]
Summing three directions,
\[
\boxed{\sum_pd_p=\sum_er_e(r_e-1)=288L^3-24L.}
\tag{6.1}
\]
The unit-vector Rayleigh quotient of \(\mathsf Q\) is
\[
\frac{2\sum_pd_p}{M}
=\frac{48L^2-4}{L(2L+1)}
\leq q_{\max}<24.
\tag{6.2}
\]
The least coefficient \(\nu_1=7/15-q_{\max}/21\) therefore satisfies
\[
\boxed{
0<\nu_1+\frac{71}{105}
\leq\frac{4(6L+1)}{21L(2L+1)}.}
\tag{6.3}
\]
In particular \(\nu_1\to-71/105\) as a finite-matrix coefficient
limit when \(L\to\infty\). This is not an interchange with the
fixed-box quantum expansion. The guaranteed disk (3.1) shrinks
with \(M\), and its remainder constants have not been made uniform.

Since \(q_{\max}\) is simple, \(\nu_1\) is simple. For every fixed
box, the gap from \(\nu_1\) to the next finite-matrix coefficient
is strictly positive. Equation (3.7), divided by \(\xi^2\), then
shows that the actual first excited eigenvalue is simple for
sufficiently small nonzero real \(\xi\), with a leading in-cluster
vector given by the positive Perron coefficient vector on the
literal basis \(W_p\). Its vacuum and two-face dressing is (4.7).
This simplicity is a local finite-box consequence, not an
all-coupling assertion.

## 7. Exact checks and scope

The accompanying check_first_excitation_band_independent.py verifies
every rational virtual denominator, the vacuum-energy subtraction,
the diagonal and off-diagonal matrix coefficients, complete face
incidence and degree sums, and the finite-box bound coefficients.
It also checks every unordered distinct face-pair parity support
in the \(L=2\) full box, including disjoint and adjacent pairs.
The proof of injectivity and the spectral/domain arguments are
given above; finite enumeration does not replace them.

No independent-link interacting vacuum, omitted face family, deleted
vacuum channel, or trial-state quotient substitutes for the actual
cluster. The second-order coefficient decreases the first excitation
energy from \(3\kappa\) in the stated finite strong-coupling regime.
It does not imply a vanishing finite energy or establish a
four-dimensional continuum limit.

## 8. Fully explicit finite-box fourth-order remainder

The preceding remainder can be made numerical without a
volume-uniform assumption. Put
\[
\boxed{r=\frac3{64M}.}
\tag{8.1}
\]
All resolvents and projections in this section act on the physical
Hilbert space. This qualifier is essential for the ground contour
used below: the unreduced free Hilbert space has an eigenvalue
exactly \(3/4\), whereas the physical next eigenvalue is 3.

For complex \(|\xi|\leq r\), on the cluster contour
\(|z-3|=3/4\), the free resolvent norm is at most \(4/3\), and
\[
\|\xi S(z-H_0)^{-1}\|
\leq r(2M)(4/3)=\frac18.
\]
Thus the Neumann series gives
\[
\|(z-K_\xi)^{-1}\|\leq\frac{4/3}{1-1/8}=\frac{32}{21}.
\]
The resolvent-difference contour bound gives
\[
\|P_\xi-P\|
\leq\frac{1/8}{1-1/8}=\frac17.
\tag{8.2}
\]
This uses contour radius times the free resolvent bound equal to 1.
On the finite space \(\operatorname{ran}P\), set
\(T_\xi=PP_\xi P\). Its holomorphic inverse square root is defined
by the convergent binomial series around the identity. Since
\(\|T_\xi-I_P\|\leq1/7\), its positive majorant gives
\[
\|T_\xi^{-1/2}\|^2\leq(1-1/7)^{-1}=\frac76.
\tag{8.3}
\]

The holomorphic extension of the real Hermitian effective matrix
(3.3) is
\[
\mathsf B_\xi
=T_\xi^{-1/2}P(K_\xi P_\xi)P T_\xi^{-1/2}.
\tag{8.4}
\]
For real \(\xi\), idempotence of \(P_\xi\), its commutation with
\(K_\xi\), and its orthogonality show that (8.4) equals
\(V_\xi^*K_\xi V_\xi=\mathsf A_\xi\).
For complex \(\xi\), (8.4) avoids introducing an antiholomorphic
adjoint and is the required analytic matrix for Cauchy's estimate.

Subtracting \(3I_P\) in (8.4) leaves
\(T_\xi^{-1/2}P((K_\xi-3)P_\xi)PT_\xi^{-1/2}\).
Contour functional calculus gives
\[
(K_\xi-3)P_\xi
=\frac1{2\pi i}\oint_{|z-3|=3/4}
(z-3)(z-K_\xi)^{-1}\,dz .
\]
Hence
\[
\|\mathsf B_\xi-3I_P\|
\leq\frac76\left(\frac34\right)^2\frac{32}{21}=1 .
\tag{8.5}
\]

For the ground energy, use the physical contour \(|z|=3/4\).
The free physical spectrum is zero and then at least 3, so its
resolvent bound is again \(4/3\); the same Neumann estimate applies.
Its analytic projection remains rank one throughout \(|\xi|\leq r\).
The enclosed eigenvalue \(e_0(\xi)\) is holomorphic and lies inside
this contour, so
\[
|e_0(\xi)|\leq\frac34.
\tag{8.6}
\]
For real \(\xi\), min--max identifies it with the actual ground
energy of \(K_\xi\). The central conjugation makes both
\(\mathsf B_\xi\) and \(e_0(\xi)\) even, also for complex \(\xi\).

Define
\(\mathsf C_\xi=\mathsf B_\xi-3I_P-e_0(\xi)I_P\).
It is even and holomorphic, with \(\mathsf C_0=0\),
quadratic coefficient \(\mathsf F\), and
\(\sup_{|\xi|\leq r}\|\mathsf C_\xi\|\leq7/4\).
Cauchy's coefficient estimate in this finite operator norm yields
\(\|\mathsf C_{2k}\|\leq(7/4)r^{-2k}\).
For real \(|\xi|\leq r/2\), summing every remaining even term gives
\[
\begin{split}
\|\mathsf C_\xi-\xi^2\mathsf F\|
&\leq\frac74\sum_{k\geq2}(|\xi|/r)^{2k}\\
&\leq\frac73r^{-4}\xi^4 .
\end{split}
\]
Finite-dimensional min--max therefore gives the fully explicit
error for every member of the actual first excitation band:
\[
\boxed{
\left|(\mathcal E_j-\mathcal E_0)
-3\kappa-\kappa\xi^2\nu_j\right|
\leq\kappa\frac73\left(\frac{64M}{3}\right)^4\xi^4,
\quad |\xi|\leq\frac3{128M},\quad 1\leq j\leq M.}
\tag{8.7}
\]
The bound is deliberately volume dependent. It neither asserts that
its radius covers fixed coupling at growing volume nor discards
the \(M^4\) remainder coefficient.
