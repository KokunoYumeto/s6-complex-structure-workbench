# Weighted local energy: independent complete second-order calculation

8 September 2026. The full finite open Wilson box and its actual positive
ground state are retained. The calculation below proves the exact
commutator and centered-state maps, the first surviving vacuum coefficient,
its complete channel norms, and the exact finite-volume coefficient for
unshifted affine midpoint weights. No infinite-volume or continuum spectral
conclusion is assumed.

## 1. Original state space, coefficients and weighted-operator domains

Fix an integer \(L\geq2\). Vertices are
\(\mathsf V_L=\{-L,\ldots,L\}^3\). Every positive physical edge
\(e=(n,i)\) from \(n\) to \(n+\mathbf e_i\) lying in this box is present.
Every elementary face \(p=(n;i,j)\), \(i<j\), is present. Write
\[
N=3(2L)(2L+1)^2,\qquad M=3(2L)^2(2L+1).
\]
There is one independent \(U_e\in SU(2)\) for each physical edge;
negative traversal uses its inverse. On
\(\mathcal H=L^2(SU(2)^{\mathsf E_L},dU)\), with product Haar probability
measure and inner product conjugate-linear in the first argument, retain
\[
T_a=-i\sigma_a/2,\qquad
X_{e,a}F(U)=\left.\frac{d}{dt}\right|_0
F(\ldots,e^{tT_a}U_e,\ldots),\qquad E_e=-\sum_aX_{e,a}^2.
\]
Each \(X_{e,a}\) is skew on smooth functions. The face observable is
\[
W_p=\operatorname{tr}\bigl[
U_i(n)U_j(n+\mathbf e_i)
U_i(n+\mathbf e_j)^{-1}U_j(n)^{-1}\bigr].
\]
It is real and invariant under \(U_e\mapsto g_sU_eg_t^{-1}\).
Put
\[
V_p=b(2-W_p),\quad H_0=\sum_eE_e,\quad
S=\sum_pW_p,\quad
H=\kappa H_0+\sum_pV_p
=\kappa(H_0-\xi S)+2bM,\qquad \xi=b/\kappa .
\tag{1.1}
\]
Here \(\kappa,b>0\). The original physical dictionary is
\[
c(A,B)=-\tfrac12\operatorname{tr}(AB),\qquad
\Delta_e^c=4\Delta_e^T,\qquad
\kappa=\frac{2g_{\rm YM}^2}{a},\quad
b=\frac1{2g_{\rm YM}^2a},\quad
\xi=\frac1{4g_{\rm YM}^4}.
\]
No scalar Wilson term is deleted from \(H\).

For arbitrary fixed real edge weights \(f_e\), choose exactly
\[
f_p=\frac14\sum_{e\in\partial p}f_e,\qquad
D_f=\kappa\sum_ef_eE_e+\sum_pf_pV_p .
\tag{1.2}
\]
Set \(F_f=\sum_ef_eE_e\), \(S_f=\sum_pf_pW_p\), and
\(F_\Sigma=\sum_pf_p\). Thus the full weighted operator is
\[
D_f=\kappa(F_f-\xi S_f)+2bF_\Sigma I.
\tag{1.3}
\]

Signed weights require an explicit domain. The joint Peter--Weyl
decomposition has edge eigenvalues \(\lambda_e=j_e(j_e+1)\).
The real diagonal multiplier \(\sum_ef_e\lambda_e\) defines a
self-adjoint \(F_f\) on
\[
\mathcal D(F_f)=
\left\{u:\sum_{\boldsymbol j,\nu}
\left|\sum_ef_ej_e(j_e+1)\right|^2
|u_{\boldsymbol j,\nu}|^2<\infty\right\}.
\tag{1.4}
\]
Finite joint-spin sums form a core: their truncations converge to any
domain vector both in Hilbert norm and after multiplication by that
diagonal eigenvalue. Smooth functions contain this core and lie in
the domain. The bounded real multiplication operator
\(\sum_pf_pV_p\) preserves self-adjointness on the same domain and
preserves the core property, since the two graph norms are equivalent.
Thus \(D_f\) is self-adjoint on \(\mathcal D(F_f)\). This domain is
not asserted to equal \(H^2\) for signed or vanishing weights.

In contrast, the full \(H\) is elliptic with operator domain \(H^2\)
and form domain \(H^1\). Its bounded smooth potential preserves compact
resolvent. The ground variational principle, the inequality
\(|\nabla|u||\leq|\nabla u|\), elliptic regularity and the strong maximum
principle give a normalized smooth strictly positive ground state
\(\psi\), of energy \(E\). Integration by parts in its eigen-equation
gives
\[
\mathfrak q_{H-E}(\psi A,\psi B)
=\kappa\sum_{e,a}\int\psi^2
\overline{X_{e,a}A}\,X_{e,a}B\,dU .
\tag{1.5}
\]
This holds first for smooth functions and then on the form domain by
density; \(\psi\) and \(\psi^{-1}\) are bounded smooth functions on the
compact manifold. A second ground state divided by \(\psi\) has zero
gradient by (1.5), hence is constant. This proves simplicity.
Gauge transformations preserve the normalized positive vacuum, so
\(\psi\) is invariant.

All vectors \(D_f\psi\) and every differential product below are smooth.
Consequently they belong to the full form and operator domains
regardless of the possible degeneracy of (1.4).

## 2. Exact commutator, covariance and excitation energy

Distinct edge Casimirs commute, and the face potentials commute as
multiplication operators. On the common smooth core,
\[
\boxed{[H,D_f]
=\kappa\sum_{\substack{e,p\\e\in\partial p}}
(f_p-f_e)[E_e,V_p].}
\tag{2.1}
\]
Indeed the kinetic-to-potential cross term has coefficient \(f_p\);
the potential-to-kinetic cross term has coefficient \(-f_e\).
For \(e\notin\partial p\), the commutator vanishes. The original
derivative signs are, for smooth \(A\),
\[
[E_e,V_p]A
=-\sum_a\bigl[(X_{e,a}^2V_p)A
             +2(X_{e,a}V_p)X_{e,a}A\bigr]
=b\sum_a\bigl[(X_{e,a}^2W_p)A
             +2(X_{e,a}W_p)X_{e,a}A\bigr].
\tag{2.2}
\]
This is the product rule with \(E_e=-\sum_aX_{e,a}^2\).

Define the real scalar \(d_f=\langle\psi,D_f\psi\rangle\) and
the physical centered vector
\[
u_f=(D_f-d_f)\psi .
\tag{2.3}
\]
It is real, smooth, invariant and vacuum-orthogonal. Its exact squared
norm and excitation energy are
\[
\|u_f\|^2=\langle\psi,D_f^2\psi\rangle-d_f^2,
\tag{2.4}
\]
\[
\begin{split}
\mathfrak q_{H-E}[u_f]
&=\langle D_f\psi,[H,D_f]\psi\rangle\\
&=\frac12\langle\psi,[D_f,[H,D_f]]\psi\rangle .
\end{split}
\tag{2.5}
\]
To prove the first equality in (2.5), use
\((H-E)D_f\psi=[H,D_f]\psi\); the removed vacuum scalar contributes
zero. For the second, expand the double commutator as
\(2D_fHD_f-D_f^2H-HD_f^2\) and apply \(H\psi=E\psi\).
All products are defined on the smooth vector being used.

The choice (1.2) has an exact local-energy decomposition:
\[
\ell_e=\kappa E_e+\frac14\sum_{p\ni e}V_p,\qquad
D_f=\sum_ef_e\ell_e,\qquad \sum_e\ell_e=H .
\tag{2.6}
\]
For \(u_e=(\ell_e-\langle\ell_e\rangle)\psi\), define the complete
real symmetric Gram matrices
\[
C_{ef}=\langle u_e,u_f\rangle,\qquad
N_{ef}=\mathfrak q_{H-E}(u_e,u_f).
\]
Here the subscript \(f\) in a matrix entry denotes an edge, not the
weight function. Then
\[
\|u_f\|^2=\sum_{e,e'}f_ef_{e'}C_{ee'},\qquad
\mathfrak q_{H-E}[u_f]=\sum_{e,e'}f_ef_{e'}N_{ee'}.
\tag{2.7}
\]
No covariance is removed. Both matrices are positive semidefinite and
have row sums zero, because \(\sum_eu_e=(H-E)\psi=0\).
In particular a constant weight gives the exact zero centered state.

## 3. True-vacuum coefficients and cancellation of first order

The exact free Casimir on a fundamental edge is \(3/4\), since
\(-\sum_aT_a^2=3I/4\). Thus
\[
H_0W_p=3W_p,\qquad
\int W_p\,dU=0,\qquad
\int W_pW_q\,dU=\delta_{pq}.
\tag{3.1}
\]
For distinct faces, an edge occurring in one face but not the other
annihilates the mixed integral by its central transformation
\(U_e\mapsto-U_e\). Equal-face integration reduces by Haar invariance
to \(\int(\operatorname{tr}U)^2dU=1\).

For completeness the true vacuum has a convergent local expansion,
not an independent vacuum ansatz. The full interaction has norm
\(\|S\|_\infty=2M\), attained at the all-identity configuration.
The product free spectrum is a sum of \(j_e(j_e+1)\), with simple
constant eigenvalue zero and first nonzero eigenvalue \(3/4\).
On \(|z|=3/8\), the free resolvent norm is at most \(8/3\).
The Neumann resolvent series therefore converges for
\(|\xi|<3/(16M)\), and its contour projection is analytic of rank
one. For real \(\xi\) near zero it is the actual ground projection:
the bottom lies in \([-2M|\xi|,0]\), while the next eigenvalue is
at least \(3/4-2M|\xi|>3/8\).

Normalize the analytic eigenfunction to Haar mean one locally:
\[
\phi_\xi=1+\xi\phi_1+\xi^2\phi_2+O_L(\xi^3),\qquad
\int\phi_1=\int\phi_2=0 .
\]
The nonzero Haar-mean normalization follows by continuity of the
projection of 1 at zero. Differentiating
\((H_0-\xi S)\phi_\xi=e(\xi)\phi_\xi\) gives exactly
\[
\phi_1=S/3,\qquad e_1=0,\qquad e_2=-M/3,\qquad
H_0\phi_2=(S^2-M)/3.
\tag{3.2}
\]
Thus
\[
\phi_2=\frac13H_0^{-1}(S^2-M),
\tag{3.3}
\]
where the inverse is on the Haar-mean-zero subspace.
The actual unit-norm positive vacuum is
\[
\psi_\xi=1+\xi A+\xi^2B+O_L(\xi^3),\qquad
A=S/3,\quad B=\phi_2-M/18 .
\tag{3.4}
\]
The constant follows from \(\|A\|^2=M/9\).
The elliptic identity
\(\phi_\xi=(H_0+1)^{-1}[(e(\xi)+1+\xi S)\phi_\xi]\)
upgrades analyticity by two Sobolev derivatives at a time.
Hence (3.2)--(3.4) have controlled remainders in every fixed Sobolev
norm at this fixed box.

Because a face has four fundamental edges,
\[
F_fW_p=\frac34\sum_{e\in\partial p}f_eW_p=3f_pW_p .
\tag{3.5}
\]
Thus \(F_fA=S_f\), and the order-\(\xi\) nonconstant term in
\((F_f-\xi S_f)\psi_\xi\) cancels exactly. Its expectation is
\[
\langle\psi_\xi,(F_f-\xi S_f)\psi_\xi\rangle
=\xi^2\bigl(\langle A,F_fA\rangle-2\langle A,S_f\rangle\bigr)
+O_L(\xi^3)
=-\frac{\xi^2}{3}F_\Sigma+O_L(\xi^3).
\tag{3.6}
\]
After subtracting the full expectation, the original state therefore is
\[
\boxed{u_f=\kappa\xi^2R_f+O_{L,f,H^k}(\kappa|\xi|^3),}
\tag{3.7}
\]
for every fixed Sobolev index \(k\), where
\[
R_f=\frac13\left[
F_fH_0^{-1}(S^2-M)-S_fS+F_\Sigma\right].
\tag{3.8}
\]
The full scalar \(2bF_\Sigma\) cancels between \(D_f\) and \(d_f\);
it has not been omitted from either operator.

## 4. Exact connected two-face reduction and denominators

The commuting Casimir sums \(F_f,H_0\) also commute with the
mean-zero free inverse. Since \(\int W_pW_q=\delta_{pq}\), one may
write (3.8), retaining every ordered pair, as
\[
R_f=\frac13\sum_{p,q}
\left[F_fH_0^{-1}-\frac{f_p+f_q}{2}\right]
(W_pW_q-\delta_{pq}).
\tag{4.1}
\]
This is a finite sum. It has the following exact cancellations.

For \(p=q\), \(W_p^2-1\) is the adjoint character of the face.
Each of its four edges has spin 1 and Casimir 2, so \(H_0\) has
eigenvalue 8 and \(F_f\) eigenvalue
\(2\sum_{\partial p}f_e=8f_p\). Thus that summand is zero.

For distinct faces with no common physical edge, each of the eight
edges in \(W_pW_q\) is fundamental. Hence its \(H_0\) eigenvalue is
6 and \(F_f\) eigenvalue \(3(f_p+f_q)\). This summand is also zero,
whether or not the two faces have a common vertex.

Distinct elementary faces can share at most one edge. Fix an unordered
adjacent pair \(\{p,q\}\) with unique shared physical edge \(e\), and
put
\[
s_{pq}=f_p+f_q,\qquad \delta_{pq}=f_p+f_q-2f_e.
\tag{4.2}
\]
One may invert one whole face traversal, which leaves its \(SU(2)\)
trace unchanged, and rotate each trace so that
\[
W_p=\operatorname{tr}(U_eA),\qquad
W_q=\operatorname{tr}(U_e^{-1}B).
\]
Here \(A,B\) are products on the two three-edge outer paths, using
six distinct physical links. Their original positive or inverse
occurrences are retained.

Let \(P_e\) integrate only \(U_e\) against Haar, and define
\[
Z_{0,pq}=P_e(W_pW_q)=\frac12\operatorname{tr}(AB),\qquad
Z_{1,pq}=W_pW_q-Z_{0,pq}.
\tag{4.3}
\]
The identity follows by expanding the traces and applying
\(\int U_{ab}\overline{U_{cd}}\,dU=\delta_{ac}\delta_{bd}/2\).
The shared edge is in the scalar channel for \(Z_0\), and in the
traceless conjugation channel for \(Z_1\). This latter channel has
Casimir 2: on traceless \(2\times2\) matrices,
\(-\sum_a[T_a,[T_a,C]]=2C\), as follows directly from the Pauli
products. Equivalently this is the exact \(0\oplus1\) decomposition
of the two fundamental occurrences on the shared edge.

Each outer edge has Casimir \(3/4\) on both channels. Therefore
\[
\begin{array}{c|cc}
 & Z_{0,pq}&Z_{1,pq}\\ \hline
H_0&9/2&13/2\\
F_f&3s_{pq}-3f_e/2&3s_{pq}+f_e/2 .
\end{array}
\tag{4.4}
\]
For \(F_f\), the six outer edges have total weight
\(4f_p+4f_q-2f_e\), while the shared triplet contributes \(2f_e\).
Consequently
\[
\left(F_fH_0^{-1}-s_{pq}/2\right)Z_{0,pq}
=\delta_{pq}Z_{0,pq}/6,
\]
\[
\left(F_fH_0^{-1}-s_{pq}/2\right)Z_{1,pq}
=-\delta_{pq}Z_{1,pq}/26 .
\]
Both orders of \((p,q)\) occur in (4.1). The complete surviving
coefficient is thus
\[
\boxed{
R_f=\sum_{\{p,q\}:\,\partial p\cap\partial q=\{e\}}
\delta_{pq}\left(\frac{Z_{0,pq}}9-\frac{Z_{1,pq}}{39}\right).}
\tag{4.5}
\]
In terms of the unhalved outer-loop trace
\(R_{pq}^{\rm loop}=\operatorname{tr}(AB)\), the summand is
\(\delta_{pq}(R_{pq}^{\rm loop}/18-Z_{1,pq}/39)\).

There is also an exact derivative form. Put
\(G_{e,pq}=\sum_a(X_{e,a}W_p)(X_{e,a}W_q)\).
The product rule gives
\[
H_0(W_pW_q)=6W_pW_q-2G_{e,pq}.
\]
Using (4.4) yields
\[
G_{e,pq}=\frac34Z_{0,pq}-\frac14Z_{1,pq},\qquad
R_f=\frac23\sum_{\{p,q\}}\delta_{pq}H_0^{-1}G_{e,pq}.
\tag{4.6}
\]
Writing \(d_{pq}=(f_p+f_q)/2-f_e\) instead gives
\((4/3)\sum d_{pq}H_0^{-1}G_{e,pq}\).
This records both factor conventions exactly.

## 5. Complete pair-support orthogonality and leading norm/energy

For a fixed pair, \(P_e\) is an orthogonal projection, so
\(\langle Z_0,Z_1\rangle=0\). The two three-edge path products
\(A,B\) are independent Haar variables after integrating their
distinct physical edges. Hence
\[
\|Z_0\|^2=\frac14\int(\operatorname{tr}(AB))^2\,dA\,dB=\frac14.
\]
Conditional on \(U_e\), the two full face products are independent
Haar variables, so \(\|W_pW_q\|^2=1\). Pythagoras gives
\[
\boxed{\|Z_0\|^2=\frac14,\qquad
\|Z_1\|^2=\frac34,\qquad \langle Z_0,Z_1\rangle=0.}
\tag{5.1}
\]

Distinct unordered adjacent pairs are orthogonal, including all their
channel combinations. Here is the complete incidence argument.
The edge set where either channel is odd under \(U_e\mapsto-U_e\)
is precisely the six-edge symmetric difference
\(\partial p\mathbin{\triangle}\partial q\). The shared edge is even
and other edges are absent. Integration over the shared edge preserves
these parity statements for \(Z_0\), hence also for \(Z_1\).

Suppose two distinct unordered adjacent pairs had the same six-edge
parity set. Over \(\mathbb F_2\), the symmetric difference of their
face sets would be a nonempty 2-chain with at most four elementary
faces and zero boundary. Choose one face in it. Each of its four
different boundary edges would have to occur in another face of the
chain. Any other distinct elementary face shares at most one edge
with the chosen face: coplanar unit squares have at most a unit-side
intersection, nonparallel face planes intersect in a line and contain
at most one edge of the square there, and parallel distinct planes
have no intersection. Therefore four different additional faces
would be necessary, requiring at least five faces. This contradicts
the bound of four.

Thus two distinct pairs have different parity sets. Choose an edge
in exactly one set. Its central Haar-preserving transformation flips
one channel function and leaves the other fixed. Their inner product
is its own negative, hence zero. This proves complete cross-pair
orthogonality without an independence approximation.

Let
\[
\mathcal J_L(f)=\sum_{\{p,q\}:\,\partial p\cap\partial q=\{e\}}
(f_p+f_q-2f_e)^2 .
\tag{5.2}
\]
Using (4.4)--(5.1), all cross terms vanish and one gets exactly
\[
\begin{split}
\|R_f\|^2
&=\left(\frac1{4\cdot9^2}+\frac3{4\cdot39^2}\right)
\mathcal J_L(f)
=\boxed{\frac{49}{13689}\mathcal J_L(f)},\\
\langle R_f,H_0R_f\rangle
&=\left(\frac{9}{2}\frac1{4\cdot9^2}
       +\frac{13}{2}\frac3{4\cdot39^2}\right)
\mathcal J_L(f)
=\boxed{\frac2{117}\mathcal J_L(f)} .
\end{split}
\tag{5.3}
\]

The exact central cochain
\(z_i(n)=(-1)^{\sum_{k<i}n_k}I\) flips every face trace in every
plane and commutes with all Casimirs. Its unitary translation
\(\mathcal Z\) therefore sends \(H_0-\xi S\) to \(H_0+\xi S\),
and \(F_f-\xi S_f\) to \(F_f+\xi S_f\).
Uniqueness gives \(\psi_{-\xi}=\mathcal Z\psi_\xi\) and
\(e(-\xi)=e(\xi)\). Centering cancels the odd scalar in (1.3), so
\[
u_f(-\xi)=\mathcal Z u_f(\xi).
\]
Both its squared norm and its excitation form are even real-analytic
functions near zero. The first surviving state order is \(\xi^2\),
so their order-\(\xi^5\) terms vanish. Equations (3.7) and (5.3) give
\[
\boxed{\|u_f\|^2
=\kappa^2\xi^4\frac{49}{13689}\mathcal J_L(f)
+O_{L,f}(\kappa^2\xi^6),}
\tag{5.4}
\]
\[
\boxed{\mathfrak q_{H-E}[u_f]
=\kappa^3\xi^4\frac2{117}\mathcal J_L(f)
+O_{L,f}(\kappa^3\xi^6).}
\tag{5.5}
\]
For any fixed weights with \(\mathcal J_L(f)>0\), these convergent
expansions prove nontriviality on an actual interval of sufficiently
small positive \(\xi\), and
\[
\boxed{\frac{\mathfrak q_{H-E}[u_f]}{\|u_f\|^2}
=\frac{234}{49}\kappa+O_{L,f}(\kappa\xi^2).}
\tag{5.6}
\]
The coefficient is larger than zero and does not decrease with \(L\).
This is a fixed-box perturbative statement; its remainder constants
are not claimed uniform as the box grows. If \(\mathcal J_L(f)=0\),
(5.4) alone does not classify all higher orders. Constant weights,
in particular, give \(D_f=fH\) and the exact zero vector.

## 6. Unshifted affine midpoint coordinate: exact full-box sum

Fix \(r\in\{1,2,3\}\) and take the literal integer-coordinate midpoint
weight
\[
\boxed{f_{(n,i)}=x_r(n,i)=n_r+\frac12\delta_{ir}.}
\tag{6.1}
\]
No coordinate shift, division by \(L\), mesh absorption or boundary
identification is performed. Averaging the four edge midpoints gives
exactly the face-center coordinate
\[
f_{(n;i,j)}=n_r+\frac12(\delta_{ir}+\delta_{jr}).
\tag{6.2}
\]

For a shared edge \(e=(n,i)\), let its midpoint vector be
\(x(e)=n+\mathbf e_i/2\). Every incident face extends from this edge
in one of the transverse directions \(j\ne i\), with a sign
\(s=\pm1\) allowed by the boundary. Its center is
\(x(e)+s\mathbf e_j/2\).
For two incident faces with transverse data \((j,s)\) and \((k,t)\),
\[
\delta_{pq}=\frac12(s\delta_{jr}+t\delta_{kr}).
\tag{6.3}
\]
If they are coplanar and distinct, then \(j=k\) and \(s=-t\),
so \(\delta_{pq}=0\).
If they are hinged, \(j\ne k\) are the two transverse directions.
For \(i=r\), neither equals \(r\), so the difference is zero.
For \(i\ne r\), exactly one of \(j,k\) equals \(r\), giving
\(\delta_{pq}=\pm1/2\) and \(\delta_{pq}^2=1/4\).
Thus affine weights do not annihilate the hinged-pair coefficient.

To count every boundary contribution, for a transverse coordinate
\(m\in\{-L,\ldots,L\}\) define
\[
a(m)=
\begin{cases}
1,&m=-L\text{ or }m=L,\\
2,&-L<m<L.
\end{cases}
\qquad \sum_{m=-L}^{L}a(m)=4L .
\tag{6.4}
\]
For a fixed direction-\(i\) edge, the number of unordered hinged pairs
in its face star is \(a(n_j)a(n_k)\): choose one allowed face from
each transverse direction. There is no factor of two, because the
two transverse directions specify the unordered pair uniquely.
There are \(2L\) choices of \(n_i\). Thus the complete hinged-pair
count for each direction is
\[
(2L)\left(\sum_{n_j=-L}^{L}a(n_j)\right)
     \left(\sum_{n_k=-L}^{L}a(n_k)\right)
=32L^3 .
\tag{6.5}
\]
Each adjacent pair has exactly one shared edge, so it is counted
once. Two edge directions satisfy \(i\ne r\), each with squared
coefficient \(1/4\). Hence
\[
\boxed{\mathcal J_L(x_r)=2\cdot\frac14\cdot32L^3=16L^3.}
\tag{6.6}
\]
This is the exact sum for the full box, not an interior-only
asymptotic. Inserting it into (5.4)--(5.6) gives
\[
\boxed{\|u_{x_r}\|^2
=\frac{784}{13689}\kappa^2\xi^4L^3
+O_L(\kappa^2\xi^6),}
\]
\[
\boxed{\mathfrak q_{H-E}[u_{x_r}]
=\frac{32}{117}\kappa^3\xi^4L^3
+O_L(\kappa^3\xi^6),\qquad
\mathcal Q_{x_r}=\frac{234}{49}\kappa+O_L(\kappa\xi^2).}
\tag{6.7}
\]
Equivalently the leading squared norm is
\((784/13689)(b^4/\kappa^2)L^3\), and the leading excitation form
is \((32/117)(b^4/\kappa)L^3\). Both grow with the same explicit
volume coefficient \(L^3\); their ratio does not become small at
this order.

## 7. Exact affine centering by the original box reflection

The scalar \(d_{x_r}\) vanishes exactly at every \(\kappa,b>0\),
not only through the preceding perturbative order. Let \(\rho_r\)
reflect vertex coordinate \(n_r\mapsto-n_r\), fixing the other two.
Its configuration map sends a direction-\(i\ne r\) physical link
to the link at \((\rho_r n,i)\) with the same orientation, and a
direction-\(r\) link to the inverse of the link at
\((\rho_r n-\mathbf e_r,r)\). This is a permutation of independent
edge factors together with group inversion. Product Haar measure
is invariant, and the resulting pullback \(\mathcal R_r\) is a real
unitary involution.

Bi-invariance of the Casimir preserves each transported kinetic
term. Elementary faces are permuted, with a possibly reversed
traversal; their traces are unchanged under inversion in \(SU(2)\).
Thus \(\mathcal R_r H\mathcal R_r^{-1}=H\), and uniqueness gives
\(\mathcal R_r\psi=\psi\).

The midpoint of every transported edge is the reflected original
midpoint. In direction \(r\), its \(r\)-coordinate is
\(-n_r-1+1/2=-(n_r+1/2)\); in the other directions it is \(-n_r\).
The same statement holds for each face center. Therefore both
weights in (1.2) change sign and
\[
\mathcal R_rD_{x_r}\mathcal R_r^{-1}=-D_{x_r}.
\]
Taking the invariant-vacuum expectation gives
\(d_{x_r}=-d_{x_r}\), hence
\[
\boxed{d_{x_r}=0,\qquad u_{x_r}=D_{x_r}\psi}
\tag{7.1}
\]
for all positive original couplings. Positivity of (6.6) proves that
this vector is nonzero on a genuine small-\(\xi\) interval for every
fixed \(L\). No all-coupling nontriviality or massless limit is
inferred from that local expansion.

## 8. Bounded checks and scope

The companion check_local_energy_independent.py independently enumerates
the complete edge and face sets, every adjacent pair, its parity support,
all three unshifted affine midpoint averages, and the exact sum (6.6)
for \(L=2,3,4,5\). It also verifies the rational channel coefficients
and the quotient \(234/49\). The proof of pair orthogonality and the
all-\(L\) boundary count are the analytic incidence arguments above,
not extrapolations from finite tests.

The actual full vacuum enters every exact identity and the convergent
finite-box expansion. Only after computing its coefficient were all
self-face and edge-disjoint terms proved to cancel. Every neighboring
face interaction remains in (4.5). The original constant and physical
coefficients are preserved. The finite-volume coefficients do not by
themselves construct a changing-volume quantum state or justify a
four-dimensional continuum spectral conclusion.

## 9. Independent check of the companion current and moment formulas

The entire companion ../local_energy_current_true_vacuum.md was read
at SHA-256
37282d06541c0def4f76814d97c9c170487719d4f4cd2072e6ec0a01950fbf16.
Its exact current formulas agree with this independent derivation.
With the local operators \(\ell_e\) in (2.6),
\[
J_{ee'}=i[\ell_e,\ell_{e'}]
=\frac{i\kappa}{4}
\sum_{p:\,e,e'\in\partial p}
\bigl([E_e,V_p]-[E_{e'},V_p]\bigr).
\]
This includes \(J_{ee}=0\) and \(J_{ee'}=-J_{e'e}\).
Since \(\sum_e\ell_e=H\),
\[
i[H,\ell_e]=-\sum_{e'}J_{ee'},\qquad
i[H,D_f]=\frac12\sum_{e,e'}(f_{e'}-f_e)J_{ee'}.
\]
For the second equality, exchange \(e,e'\) in the term with
\(f_{e'}\) and use antisymmetry. The result is
\(-\sum_{e,e'}f_eJ_{ee'}\), precisely the weighted sum of the
first identity. The signs and factor \(1/2\) therefore check.

The current norm is the next exact spectral moment. For a complete
orthonormal physical eigenbasis \(v_0=\psi,v_1,\ldots\) with
\((H-E)v_\ell=\lambda_\ell v_\ell\), \(\lambda_\ell>0\) for
\(\ell\geq1\), define
\[
\mu_f=\sum_{\ell\geq1}
|\langle v_\ell,D_f\psi\rangle|^2\delta_{\lambda_\ell}.
\]
Smoothness of \(D_f\psi\) puts it in every power domain of \(H\).
The spectral theorem, after subtracting its vacuum component, gives
\[
\|u_f\|^2=\int d\mu_f,\qquad
\mathfrak q_{H-E}[u_f]=\int\lambda\,d\mu_f,\qquad
\|i[H,D_f]\psi\|^2=\int\lambda^2\,d\mu_f.
\]
There is no division by an unproved nonzero norm in these identities.

The companion's fully resolved unit-norm vacuum coefficient is also
correct:
\[
B=-\frac M{18}
+\sum_p\frac{W_p^2-1}{24}
+\sum_{\{p,q\}:\partial p\cap\partial q=\varnothing}\frac{W_pW_q}{9}
+\sum_{\{p,q\}\ {\rm adjacent}}
\left(\frac4{27}Z_{0,pq}+\frac4{39}Z_{1,pq}\right).
\]
Each distinct pair is unordered, so its factor 2 from \(S^2\)
is included. The self-face denominator is \(3\cdot8=24\);
the disjoint coefficient is \(2/(3\cdot6)=1/9\);
the adjacent coefficients are \(2/(3\cdot9/2)=4/27\) and
\(2/(3\cdot13/2)=4/39\). This verifies all original constants.
Its physical conversions are
\[
\kappa^2\xi^4=\frac1{64g_{\rm YM}^{12}a^2},\qquad
\kappa^3\xi^4=\frac1{32g_{\rm YM}^{10}a^3},\qquad
\frac{234}{49}\kappa=\frac{468g_{\rm YM}^2}{49a}.
\]

No mathematical discrepancy was found in the companion. A single
typesetting corruption in the adjacent-pair sum subscript, immediately
before its (4.4), was reported to the source owner; this audit did not
edit that source or any canonical or remote artifact.

### 9.1 Bounded primary citation verification

The companion cites R. P. Feynman, *Atomic Theory of the Two-Fluid Model
of Liquid Helium*, Physical Review 94, issue 2 (15 April 1954),
pages 262--277, DOI 10.1103/PhysRev.94.262. The title, author, date and
starting page were checked against the
[APS article page](https://journals.aps.org/pr/abstract/10.1103/PhysRev.94.262).
The complete page range was independently verified in the
[APS-deposited Crossref record](https://api.crossref.org/works/10.1103/PhysRev.94.262),
whose page field is exactly 262-277 and publisher is American Physical
Society. The article's abstract explicitly relates a trial excitation
to its ground-state wave function. The comparison is variational
provenance only; no helium structure factor or dynamical result is
used in this finite gauge-theory proof. The broken APS citation-export
link was not used as evidence.
