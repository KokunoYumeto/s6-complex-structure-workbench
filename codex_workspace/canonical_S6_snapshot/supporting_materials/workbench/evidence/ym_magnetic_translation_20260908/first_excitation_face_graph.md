# The full open-box face graph, its bulk symbol, and the first-band coefficient limit

8 September 2026. This calculation retains every boundary face of the original open spatial box. The infinite and periodic graphs are defined independently, and their relation to the open graph is an explicit zero-extension identity. The interior sine function is a trial vector in the actual finite open graph, not a change of boundary conditions.

## 1. Original open box, physical orientations, and the face operator

Let \(L\ge2\) be an integer, put \(m=2L\), and take vertices in \(\{-L,\ldots,L\}^3\). A physical edge \(e=(n,i)\) runs from \(n\) to \(n+\mathbf e_i\), whenever both endpoints belong to the box. The face \(p=(n;i,j)\), \(i<j\), has the canonical oriented edge word

\[
(n,i)^+\,(n+\mathbf e_i,j)^+\,
(n+\mathbf e_j,i)^-\,(n,j)^-.
\tag{1.1}
\]

Its underlying set of four physical edges is denoted \(\partial p\); signs in (1.1) do not create additional edges. All contained elementary faces are included in \(\mathsf P_L\). The number of faces is

\[
M_L=|\mathsf P_L|=3m^2(m+1)=12L^2(2L+1).
\tag{1.2}
\]

Indeed each of the three face planes has \(m\) base choices in each plane direction and \(m+1\) in its normal direction.

Two distinct faces are adjacent exactly when their physical edge sets intersect. Two distinct elementary squares in the open box share at most one physical edge: coplanar unit squares can meet along only one side, while perpendicular coordinate squares intersect in at most a single unit coordinate segment. Thus the adjacency matrix \(\mathsf A_L\) is a simple unweighted symmetric matrix:
\[
(\mathsf A_L)_{pq}=\mathbf1_{\{p\ne q,\ \partial p\cap\partial q\ne\varnothing\}}.
\]
Let \(d_p=\sum_q(\mathsf A_L)_{pq}\), and define the actual open signless face Laplacian

\[
\boxed{\mathsf Q_L=\operatorname{diag}(d_p)+\mathsf A_L.}
\tag{1.3}
\]

For every complex face vector \(x\),
\[
\langle x,\mathsf Q_Lx\rangle
=\sum_{\{p,q\}\text{ adjacent}}|x_p+x_q|^2.
\tag{1.4}
\]
This follows by expanding each square: each diagonal \(|x_p|^2\) occurs \(d_p\) times, and every cross term agrees with the adjacency quadratic form. In particular \(\mathsf Q_L\) is positive semidefinite. This is the signless operator, not \(\operatorname{diag}(d)-\mathsf A_L\).

If \(\mathsf I_{pe}=\mathbf1_{\{e\in\partial p\}}\) is the original unsigned face-edge incidence matrix, the same one-edge intersection fact gives
\[
\mathsf I\mathsf I^T=4I+\mathsf A_L,\qquad
\mathsf Q_L=\mathsf I\mathsf I^T+\operatorname{diag}(d_p-4).
\tag{1.5}
\]
The diagonal 4 in this incidence product is not the adjacency degree, which varies at the boundary.

## 2. Exact degrees, all boundary multiplicities, and connectedness

For an edge \(e=(n,i)\), let \(r_e\) be the number of contained elementary faces incident on it. If \(j,k\) are its two transverse directions, then

\[
r_e=\delta(n_j)+\delta(n_k),\qquad
\delta(t)=
\begin{cases}
1,&t=-L\text{ or }L,\\
2,&-L<t<L.
\end{cases}
\tag{2.1}
\]

In each transverse direction a face can extend on both sides in the interior and only inward at the boundary. Thus \(2\le r_e\le4\). Every neighbor of a fixed face is counted at its unique shared edge, so
\[
d_p=\sum_{e\in\partial p}(r_e-1).
\tag{2.2}
\]

For a face \(p=(n;i,j)\), write \(k\) for its normal direction and define, on the plane base-coordinate range \(-L\le t\le L-1\),
\[
\beta(t)=\mathbf1_{\{t=-L\}}+\mathbf1_{\{t=L-1\}}.
\tag{2.3}
\]
Since \(\delta(t)+\delta(t+1)=4-\beta(t)\), summing (2.1) over the four edges in (2.2) gives the exact boundary formula

\[
\boxed{
d_{n;i,j}=
\begin{cases}
12-\beta(n_i)-\beta(n_j),&-L<n_k<L,\\
8-\beta(n_i)-\beta(n_j),&n_k=-L\text{ or }L.
\end{cases}}
\tag{2.4}
\]

This produces all six degree classes, with no excluded faces:

| Degree | Exact number of faces |
|---:|---:|
| \(12\) | \(3(m-1)(m-2)^2\) |
| \(11\) | \(12(m-1)(m-2)\) |
| \(10\) | \(12(m-1)\) |
| \(8\) | \(6(m-2)^2\) |
| \(7\) | \(24(m-2)\) |
| \(6\) | \(24\) |

To verify the table, there are \(m-1\) interior normal-coordinate values or two boundary values. In either plane direction there are \(m-2\) bases with \(\beta=0\) and two with \(\beta=1\). Their products give respectively \((m-2)^2\), \(4(m-2)\), and 4 plane-coordinate pairs with sum of the two \(\beta\)'s equal to 0, 1, or 2. Multiply by the three planes and the appropriate normal-coordinate count. Summing the table gives (1.2).

The exact number \(a_L\) of unordered adjacent pairs can be obtained either by summing this degree table and dividing by 2, or directly by the incident edge stars. For each edge direction, hold its \(m\) longitudinal bases fixed. There are \((m-1)^2\) transverse interior positions with \(r_e=4\), \(4(m-1)\) positions with exactly one boundary coordinate and \(r_e=3\), and 4 positions with two boundary coordinates and \(r_e=2\). Each contributes \(\binom{r_e}{2}\), with no pair counted twice. Therefore

\[
\boxed{a_L=3m[6(m-1)^2+12(m-1)+4]
=18m^3-6m=144L^3-12L.}
\tag{2.5}
\]

In particular
\[
\sum_pd_p=2a_L,\qquad
\sum_p(12-d_p)=12m(3m+1).
\tag{2.6}
\]

The whole face graph is connected. First, the \(12\)-faces in any fixed \(n_3\) layer form a connected rectangular face grid, by coplanar edge adjacency. Consecutive \(n_3\) layers are joined through a \(13\)-face: its bottom and top direction-1 edges belong to \(12\)-faces in the two layers. For instance choose fixed permissible \(n_1,n_2\) and the \(13\)-face between the two layers; both neighboring \(12\)-faces exist. Hence all \(12\)-layers lie in one connected component. Every \(13\)-face has a direction-1 edge which belongs to a \(12\)-face, choosing the latter's direction-2 extension inward if that edge is on a boundary. Every \(23\)-face likewise has a direction-2 edge belonging to a \(12\)-face, with direction-1 extension chosen inward. Thus every face belongs to that one component.

## 3. Full open-box bounds and strict inequality at finite volume

Let \(\Lambda_L=\lambda_{\max}(\mathsf Q_L)\). The unchanged constant face vector has squared norm \(M_L\) and, by (1.4), quadratic form \(4a_L\). Hence

\[
\boxed{
\frac{48L^2-4}{L(2L+1)}
=\frac{4a_L}{M_L}\le\Lambda_L.}
\tag{3.1}
\]

The boundary formula gives \(d_p\le12\). A particularly useful exact deficit identity is

\[
\boxed{
\langle x,(24I-\mathsf Q_L)x\rangle
=\sum_{\{p,q\}\text{ adjacent}}|x_p-x_q|^2
+2\sum_p(12-d_p)|x_p|^2.}
\tag{3.2}
\]

Indeed the first sum is the quadratic form of \(\operatorname{diag}(d)-\mathsf A_L\), and adding the second term gives \(24I-\operatorname{diag}(d)-\mathsf A_L\). Both terms are nonnegative. Equality would force \(x_p=x_q\) on every adjacency and \(x_p=0\) on every degree-deficient face. Connectedness makes \(x\) constant, and the nonempty degree-6 boundary class forces that constant to be zero. Therefore, in this finite-dimensional space,

\[
\boxed{\frac{48L^2-4}{L(2L+1)}\le\Lambda_L<24.}
\tag{3.3}
\]

This already proves \(\Lambda_L\to24\). It also records why the constant vector is not an eigenvector at the open boundary: its row values are \(2d_p\), which are not constant.

## 4. Independently defined bulk and periodic graphs, with full translations

The infinite graph has vertices \((n;\alpha)\), where \(n\in\mathbb Z^3\) and the plane type \(\alpha\) is one of \(12,13,23\). Its physical edges and oriented faces use (1.1) on the entire infinite cubic lattice. Two faces are adjacent by the same shared-physical-edge rule. Every edge has four incident faces, every face has twelve distinct neighbors, and its signless operator on
\(\ell^2(\mathbb Z^3;\mathbb C^3)\) is
\[
\mathsf Q_\infty=12I+\mathsf A_\infty.
\tag{4.1}
\]

Here is its entire translation list. Within plane \(ij\), the four neighbors of \((n;ij)\) are \((n\pm\mathbf e_i;ij)\) and \((n\pm\mathbf e_j;ij)\). Between different planes, for \(a,b\in\{0,1\}\),

| Source plane | Target plane | Shared direction | Target base |
|---|---|---:|---|
| \(12\) | \(13\) | \(1\) | \(n+a\mathbf e_2-b\mathbf e_3\) |
| \(12\) | \(23\) | \(2\) | \(n+a\mathbf e_1-b\mathbf e_3\) |
| \(13\) | \(23\) | \(3\) | \(n+a\mathbf e_1-b\mathbf e_2\) |

Each row has four distinct offsets, including the zero offset, and the reverse neighbors have their negatives.

To prove the list with orientations retained, the two direction-\(i\) edges of a face \(ij\) lie at \(n\) and \(n+\mathbf e_j\) with signs \(+,-\); its two direction-\(j\) edges lie at \(n\) and \(n+\mathbf e_i\) with signs \(-,+\). A common physical edge between two planes is obtained by equating one of their two bases in the shared direction. For the first row this equates \(n+a\mathbf e_2\) with the target base plus \(b\mathbf e_3\), yielding the displayed offset. The other two rows follow by equating the direction-2 or direction-3 bases. The traversal signs in the three rows are respectively \(((-1)^a,(-1)^b)\), \((-(-1)^a,(-1)^b)\), and \((-(-1)^a,-(-1)^b)\). The graph is unsigned and so includes all four sign combinations; none is discarded or counted twice. This proves both the exact translations and the multiplicity 12.

A separate finite periodic graph can be defined by taking base coordinates in
\[
\mathbb Z/N_1\mathbb Z\times\mathbb Z/N_2\mathbb Z\times\mathbb Z/N_3\mathbb Z,
\qquad N_i\ge3,
\tag{4.2}
\]
and using the same physical edge labels and face words modulo those periods. The condition \(N_i\ge3\) prevents the \(+\mathbf e_i\) and \(-\mathbf e_i\) neighbors from coinciding and prevents two elementary faces sharing multiple physical edges. The neighbor list above is then valid modulo the periods, still with twelve distinct neighbors per face. This definition is independent of the original open box; it is not imposed on \(\mathsf P_L\).

## 5. Exact three-plane Fourier symbol and the mode attaining 24

For a finitely supported infinite face field, define
\[
\widehat f_\alpha(k)=\sum_{n\in\mathbb Z^3}f_\alpha(n)e^{-ik\cdot n},
\qquad k\in[-\pi,\pi]^3,
\tag{5.1}
\]
with inverse measure \(dk/(2\pi)^3\). Orthogonality of the exponentials proves the isometry on finite sums, which extends by density to a unitary map from \(\ell^2(\mathbb Z^3;\mathbb C^3)\) onto the corresponding \(L^2\) space. The translation \(f_\beta(n+\delta)\) gives the multiplier \(e^{ik\cdot\delta}\). In the order \(12,13,23\), the neighbor list therefore gives the exact Hermitian symbol

\[
\boxed{
\widehat{\mathsf Q}(k)=12I+
\begin{pmatrix}
2\cos k_1+2\cos k_2&
(1+e^{ik_2})(1+e^{-ik_3})&
(1+e^{ik_1})(1+e^{-ik_3})\\
(1+e^{-ik_2})(1+e^{ik_3})&
2\cos k_1+2\cos k_3&
(1+e^{ik_1})(1+e^{-ik_2})\\
(1+e^{-ik_1})(1+e^{ik_3})&
(1+e^{-ik_1})(1+e^{ik_2})&
2\cos k_2+2\cos k_3
\end{pmatrix}.}
\tag{5.2}
\]

No common translation phases have been suppressed. If one instead uses each face center as its Fourier origin, define the explicit unitary fiber change
\[
\mathsf D(k)=\operatorname{diag}
\big(e^{i(k_1+k_2)/2},e^{i(k_1+k_3)/2},e^{i(k_2+k_3)/2}\big),
\qquad \widehat f=\mathsf D(k)\,u.
\tag{5.3}
\]
Writing \(c_i=\cos(k_i/2)\), one obtains the real centered symbol

\[
\boxed{
\mathsf D(k)^*\widehat{\mathsf Q}(k)\mathsf D(k)
=
\begin{pmatrix}
12+2\cos k_1+2\cos k_2&4c_2c_3&4c_1c_3\\
4c_2c_3&12+2\cos k_1+2\cos k_3&4c_1c_2\\
4c_1c_3&4c_1c_2&12+2\cos k_2+2\cos k_3
\end{pmatrix}.}
\tag{5.4}
\]

For example the phase of the \(12,13\) entry in (5.2) is \(e^{i(k_2-k_3)/2}\), which cancels exactly with the two center phases in (5.3). Thus (5.4) is a unitary change of fiber coordinates, not a replacement of physical translation phases.

At zero momentum,
\[
\widehat{\mathsf Q}(0)=12I+4\mathbf1\mathbf1^T,
\tag{5.5}
\]
with eigenvalues 24 on the equal-plane vector \((1,1,1)\), and 12 twice on its orthogonal complement.

This is the only Bloch mode at eigenvalue 24, modulo reciprocal-lattice momenta. To prove it, for an original-base amplitude \(\eta\in\mathbb C^3\), the exact quadratic form of \(24I-\widehat{\mathsf Q}(k)=12I-\widehat{\mathsf A}(k)\) is
\[
\sum_{\alpha=ij}\sum_{r\in\{i,j\}}
|\eta_\alpha-e^{ik_r}\eta_\alpha|^2
+\sum_{\alpha<\beta}\sum_{\delta\in\mathsf T_{\alpha\beta}}
|\eta_\alpha-e^{ik\cdot\delta}\eta_\beta|^2,
\tag{5.6}
\]
where \(\mathsf T_{\alpha\beta}\) is the four-offset set in Section 4. Expanding this expression recovers (5.2): each component receives four units of same-plane diagonal contribution and eight from the cross-plane rows. It is nonnegative. Each cross-plane offset set includes zero, so equality forces all three amplitudes to agree. If they are nonzero, the same-plane terms force \(e^{ik_1}=e^{ik_2}=e^{ik_3}=1\). Conversely that momentum and equal amplitudes give (5.5). Hence
\[
\lambda_{\max}(\widehat{\mathsf Q}(k))\le24,
\]
with equality exactly at \(k\in(2\pi\mathbb Z)^3\) and the stated equal-plane eigenvector.

On the independently defined periodic graph (4.2), the same proof uses the discrete momenta \(k_i=2\pi r_i/N_i\). Its maximum eigenvalue is exactly 24, achieved only by the constant equal-plane field. On the infinite graph, the constant Bloch field is not in \(\ell^2\). The symbol implies operator norm 24: its continuous eigenvalue near zero gives fields supported in arbitrarily small momentum neighborhoods with Rayleigh values arbitrarily close to 24. There is no nonzero \(\ell^2\) eigenvector at 24, because equality in (5.6) would require its Fourier transform to be supported at the measure-zero momentum \(k=0\).

## 6. Exact map from the infinite graph to the unchanged open graph

Let \(J_L:\mathbb C^{\mathsf P_L}\to\ell^2(\mathbb Z^3;\mathbb C^3)\) extend a face vector by zero on every face outside the open box. This is an isometry in the original counting inner products. The open face graph is the induced subgraph of the infinite one: two contained faces share a physical edge in the finite box exactly when they do so in the infinite lattice. Consequently

\[
\boxed{
J_L^*\mathsf Q_\infty J_L=12I+\mathsf A_L,\qquad
\mathsf Q_L=J_L^*\mathsf Q_\infty J_L
-\operatorname{diag}(12-d_p).}
\tag{6.1}
\]

This is the exact comparison, including the boundary correction. Replacing the open operator by its bulk compression would add the nonzero boundary diagonal \(\operatorname{diag}(12-d_p)\); replacing it by a periodic graph would also add different adjacency edges. Neither operation is performed here.

The following stronger bound is a trial calculation in \(\mathsf Q_L\) itself. Put
\[
\ell=2L-2,\qquad t=\frac{\pi}{2L-1}=\frac{\pi}{\ell+1},\qquad c=\cos t,
\]
and define on the integer line
\[
f_r=
\begin{cases}
\sin(rt),&1\le r\le\ell,\\
0,&\text{otherwise}.
\end{cases}
\tag{6.2}
\]
For a face of any of the three plane types with base \(n\), set
\[
x_{n;\alpha}=g(n),\qquad
g(n)=\prod_{i=1}^3f_{n_i+L}.
\tag{6.3}
\]
This is a vector on every face of the original open box, with zero entries whenever any base coordinate is outside \([-L+1,L-2]\). Every face in its support has degree exactly 12 by (2.4). Thus the boundary diagonal in (6.1) vanishes on the support, and
\[
\langle x,\mathsf Q_Lx\rangle
=\langle J_Lx,\mathsf Q_\infty J_Lx\rangle.
\tag{6.4}
\]
No outer face or boundary interaction is deleted from the finite operator: its trial amplitude is simply zero. Equation (6.4) proves the required map of this particular interior trial to the actual open signless graph.

To calculate its quotient exactly, let
\[
S=\sum_{r=1}^{\ell}f_r^2>0,\qquad
T=\sum_{r=1}^{\ell-1}f_rf_{r+1}.
\]
The discrete sine equation \(f_{r-1}+f_{r+1}=2cf_r\), with \(f_0=f_{\ell+1}=0\), multiplied by \(f_r\) and summed, gives \(T=cS\). Direct product factorization gives
\[
\sum_ng(n)^2=S^3,\quad
\sum_ng(n)g(n+\mathbf e_i)=TS^2,\quad
\sum_ng(n)g(n+\mathbf e_i-\mathbf e_j)=T^2S\quad(i\ne j).
\tag{6.5}
\]
All sums are over the zero-extended integer lattice and hence are finite.

The squared norm of (6.3) is \(3S^3\). The diagonal contribution of \(\mathsf Q_\infty\) is \(36S^3\). The same-plane adjacency contribution, from two directions in each of three planes and both signs of each shift, is \(12TS^2\). For each of three unordered plane pairs, the four shifts in Section 4 contribute \(S^3+2TS^2+T^2S=S(S+T)^2\); the reverse matrix entries double this, giving total \(6S(S+T)^2\). Thus (6.4) yields the exact open-graph trial quotient

\[
\boxed{
\frac{\langle x,\mathsf Q_Lx\rangle}{\|x\|^2}
=\frac{36S^3+12TS^2+6S(S+T)^2}{3S^3}
=14+8c+2c^2.}
\tag{6.6}
\]

In particular the full open-box estimates can be sharpened to

\[
\boxed{
\max\left\{\frac{48L^2-4}{L(2L+1)},\
14+8\cos\frac{\pi}{2L-1}+2\cos^2\frac{\pi}{2L-1}\right\}
\le\Lambda_L<24.}
\tag{6.7}
\]

Since \(24-(14+8c+2c^2)=2(1-c)(5+c)\) and
\(1-\cos t=2\sin^2(t/2)\le t^2/2\), the deficit satisfies

\[
\boxed{
0<24-\Lambda_L
\le\min\left\{
\frac{24L+4}{L(2L+1)},\
2(1-c)(5+c)\right\}
\le\frac{6\pi^2}{(2L-1)^2}.}
\tag{6.8}
\]

The last bound is quantitative \(O(L^{-2})\), obtained without imposing periodic conditions or dropping the actual boundary diagonal.

## 7. Exact consequence for the specified second-order coefficient matrix

Define the finite matrix requested by the excitation calculation, with its given constants, by

\[
\mathsf F_L=\frac7{15}I-\frac1{21}\mathsf Q_L.
\tag{7.1}
\]

This note proves the spectrum of this explicitly specified graph matrix. The derivation identifying (7.1) with the physical true-vacuum second-order excitation matrix is the separate parent band calculation; no replacement of that physical calculation is assumed here.

Because \(\mathsf F_L\) is an affine polynomial in the real symmetric \(\mathsf Q_L\), they have the same orthonormal eigenvectors, with the exact eigenvalue map \(q\mapsto7/15-q/21\). Therefore

\[
\lambda_{\min}(\mathsf F_L)=\frac7{15}-\frac{\Lambda_L}{21}.
\tag{7.2}
\]
Equations (6.8) and (7.2) give the strict and quantitative coefficient bounds

\[
\boxed{
0<\lambda_{\min}(\mathsf F_L)+\frac{71}{105}
\le\frac1{21}\min\left\{
\frac{24L+4}{L(2L+1)},\
2(1-c)(5+c)\right\}
\le\frac{2\pi^2}{7(2L-1)^2}.}
\tag{7.3}
\]
Here \(7/15-24/21=-71/105\) exactly. In particular
\[
\boxed{\lim_{L\to\infty}\lambda_{\min}(\mathsf F_L)=-\frac{71}{105}.}
\tag{7.4}
\]

The constant equal-plane bulk mode supplies the limiting edge of this coefficient matrix, while the finite open maximizer has the strictly smaller value in (6.7). These statements concern the explicit finite Taylor-coefficient matrices and their large-box limit. They do not control any remainder of the physical perturbation series uniformly in volume, and they do not establish an infinite-volume gap or a four-dimensional continuum limit.

## 8. Lightweight exact verification

The companion check_first_excitation_face_graph.py enumerates every face and adjacency of the full open boxes \(L=2,3,4,5\). It checks the six exact degree classes, connectedness, all edge-star multiplicities, the constant-vector quotient, and all boundary deficits. The four graph sizes are respectively:

| \(L\) | Faces | Unordered adjacencies |
|---:|---:|---:|
| 2 | 240 | 1128 |
| 3 | 756 | 3852 |
| 4 | 1728 | 9168 |
| 5 | 3300 | 17940 |

The checker directly computes the quadratic form of an integer-valued separable interior trial on the unchanged whole open graph and verifies the exact factorization in (6.6) before the sine substitution. For the sine itself it uses the exact polynomials \(f_r/\sin t=U_{r-1}(c)\), where \(U_r\) are the Chebyshev polynomials and \(U_\ell(c)=0\). It verifies \(T=cS\) and the full trial quotient by polynomial division with zero remainder, not by a numerical trigonometric eigenvalue estimate.

An independently generated periodic graph with periods \((3,4,5)\) checks the full translation list and twelve-neighbor multiplicity. Exact Laurent variables \(x_i=e^{ik_i/2}\) verify the Fourier symbol and center-phase change; at \(x_i=1\) the exact characteristic polynomial is \((\lambda-24)(\lambda-12)^2\). The rational coefficient \(-71/105\) is checked exactly.

The all-\(L\) graph statements, the infinite/periodic symbol, and both open variational bounds are proved above; finite checks are diagnostics, not a substitute for those proofs. No numerical eigenvalue, spatial continuum approximation, remote action, new agent, PDF, or heavy job was used.
