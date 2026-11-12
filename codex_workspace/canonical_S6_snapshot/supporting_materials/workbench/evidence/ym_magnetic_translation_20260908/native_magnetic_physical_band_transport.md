# Native magnetic state: exact physical band transport and spectral weights

8 September 2026. This proof uses the actual interacting vacuum of the full
open three-dimensional spatial SU(2) box. The angular limit is taken first,
at each fixed box and coupling; the coupling limit is taken afterwards.
All statements about spectral measures retain their unnormalized mass.
Time is Hamiltonian time. The original spatial spacing, magnetic angle,
electric coefficient, and both shared-edge spin channels remain explicit.

## 1. Configuration, domains, and the actual native state

Fix an integer \(L\geq2\). The vertex set is
\(\mathsf V_L=\{-L,\ldots,L\}^3\). Include every positive link
\(e=(n,i)\) whose two endpoints lie in the box and every elementary face
\(p=(n;i,j)\), \(i<j\), whose four vertices lie there. Denote these sets
by \(\mathsf E_L,\mathsf P_L\). Their cardinalities are
\[
 N=3(2L)(2L+1)^2,\qquad M=3(2L)^2(2L+1).
\tag{1.1}
\]
Negative traversal uses the inverse of the same link variable. On the
compact connected configuration manifold \(\mathsf Q_L=SU(2)^N\), use
product Haar probability measure and an inner product conjugate-linear in
its first entry. Define
\[
\begin{split}
 W_{n;i,j}(U)&=\operatorname{tr}\bigl[
 U_i(n)U_j(n+\mathbf e_i)U_i(n+\mathbf e_j)^{-1}U_j(n)^{-1}\bigr],\\
 T_a&=-i\sigma_a/2,\qquad
 X_{e,a}f=\left.\frac{d}{dt}f(\ldots,e^{tT_a}U_e,\ldots)\right|_{t=0},\\
 E_e&=-\sum_{a=1}^3X_{e,a}^2,\qquad H_0=\sum_eE_e,\qquad S=\sum_pW_p,\\
 K_\xi&=H_0-\xi S,\qquad H=\kappa K_\xi+2bM I,\\
 \kappa&=\frac{2g_{\rm YM}^2}{a},\qquad
 b=\frac1{2g_{\rm YM}^2a},\qquad
 \xi=\frac b\kappa=\frac1{4g_{\rm YM}^4}.
\end{split}
\tag{1.2}
\]
Here \(a>0\), \(g_{\rm YM}>0\). In particular the Lie metric
\(c(A,B)=-\operatorname{tr}(AB)/2\) has orthonormal frame \(2T_a\),
so \(-\Delta_e^c=4E_e\). This factor is included in \(\kappa\).
The traces are real on SU(2).

Let \(\Pi\) be the Haar average of the vertex gauge action
\(U_e\mapsto g_{s(e)}U_eg_{t(e)}^{-1}\). Haar invariance proves
\(\Pi^* =\Pi^2=\Pi\); its range \(\mathcal H_{\rm phys}\) is the
physical Hilbert space. Each \(E_e\) is bi-invariant and every \(W_p\)
is gauge invariant, so these operators preserve this subspace. All
subsequent spectral projections are on \(\mathcal H_{\rm phys}\).

The elliptic product Laplacian has operator domain \(H^2\), form domain
\(H^1\), and compact resolvent. We use the intersections with
\(\mathcal H_{\rm phys}\). Multiplication by the bounded smooth real
function \(S\) leaves these domains and self-adjointness unchanged. A
ground minimizer may be taken nonnegative because taking absolute value
does not increase the gradient form; this follows by differentiating
\(\sqrt{|f|^2+\varepsilon^2}\) and passing to the limit. Elliptic
regularity and the strong maximum principle make the minimizer smooth
and strictly positive. For such a unit vector \(\psi_\xi\), with
\(K_\xi\psi_\xi=e(\xi)\psi_\xi\), integration by parts gives
\[
 \langle\psi_\xi F,(H-\mathcal E_\xi)\psi_\xi F\rangle
 =\kappa\sum_{e,a}\int\psi_\xi^2|X_{e,a}F|^2dU,
 \qquad\mathcal E_\xi=\kappa e(\xi)+2bM.
\tag{1.3}
\]
The positive smooth function and its reciprocal are bounded on this
compact manifold. The identity therefore extends to the form domain by
density. A second ground eigenvector divided by \(\psi_\xi\) would
have all derivatives zero and hence be constant. Thus the positive unit
vacuum is unique, and gauge transformations fix it. The full and physical
bottoms coincide. Write the exact physical excitation operator as
\[
 \mathscr A_\xi=H-\mathcal E_\xi I
       =\kappa(K_\xi-e(\xi)I).
\tag{1.4}
\]
This equality subtracts the same \(2bM\) present in both energies.

The native nonwrapping links and their translation are
\[
 h_1(n)=\exp(-\theta n_2H_c),\quad h_2(n)=h_3(n)=I,
 \quad H_c=i\sigma_3=-2T_3,\quad
 (\mathcal T_\theta f)(U)=f((h_e^{-1}U_e)_e).
\tag{1.5}
\]
The original geometric dictionary is \(\theta=2\pi a^2/D\), with
the original positive determinant \(D\). No integer coordinate is wrapped,
translated to a different origin, or rescaled here. Define
\[
 c_{\xi,\theta}=\langle\psi_\xi,\mathcal T_\theta\psi_\xi\rangle,
 \qquad
 \chi_{\xi,\theta}=\Pi\mathcal T_\theta\psi_\xi
                      -c_{\xi,\theta}\psi_\xi.
\tag{1.6}
\]
This is a smooth physical vector orthogonal to the same actual vacuum:
\(\langle\psi_\xi,\Pi\mathcal T_\theta\psi_\xi\rangle
=c_{\xi,\theta}\) since \(\Pi\psi_\xi=\psi_\xi\).

For completeness the exact full-representation projection in (1.6) is
as follows. There is only one nonidentity translated edge at a given
source. Gauge conjugation conjugates its left translation by the gauge
variable at that source. Independent source averages therefore give,
on invariant inputs,
\[
 \Pi\mathcal T_\theta\Pi=\mathcal C_\theta\Pi,
 \qquad \mathcal C_\theta=\prod_{e=(n,1)}C_{e,\theta n_2}.
\tag{1.7}
\]
The operator \(C_{e,s}\) averages left translation by conjugates of
\(e^{sH_c}\). On an edge-spin-\(j\) matrix coefficient Schur's lemma
and its trace give exactly
\[
 c_j(s)=\frac1{2j+1}\sum_{m=-j}^j e^{2ims}.
\tag{1.8}
\]
Indeed the averaged representation matrix commutes with all matrices of
the irreducible representation and its trace is the character. The finite
sum defines it at every angle, including zeros of the alternative sine
denominator. All link-spin sectors and all invariant multiplicities are
retained. This proves that \(\mathcal C_\theta\) is even, self-adjoint,
a contraction, and commutes with every link Casimir, with \(\Pi\), and
with Sobolev powers of \(1+H_0\). Conjugacy under \(i\sigma_1\) sends
\(s\) to \(-s\), which also directly proves evenness and self-adjointness.

Put
\[
 w_{(n,1)}=n_2^2,\qquad w_{(n,2)}=w_{(n,3)}=0,
 \quad \Gamma=\sum_e w_eE_e,
 \quad\gamma_\xi=\langle\psi_\xi,\Gamma\psi_\xi\rangle,
 \quad v_\xi=(\Gamma-\gamma_\xi)\psi_\xi.
\tag{1.9}
\]
In joint Peter--Weyl coordinates, \(\Gamma\) is the nonnegative diagonal
self-adjoint operator with eigenvalues \(\sum_ew_ej_e(j_e+1)\). Its
domain consists precisely of coefficient families square summable after
multiplication by these eigenvalues. It contains \(H^2\); equality is
not needed because some weights vanish. Since \(0\leq w_e\leq L^2\),
the diagonal comparison \(\Gamma\leq L^2H_0\) proves boundedness
\(\Gamma:H^{k+2}\to H^k\). In particular all applications to smooth
vacua, and all products below on such vectors, have their stated domains.

Taylor's formula for the smooth translation flow, averaged over the
compact gauge group, is valid as a map \(H^{k+4}\to H^k\).
The Haar average of an adjoint-vector pair is its scalar inner product
times \(\delta_{ab}/3\), since rotational invariance makes the average
scalar and its trace fixes that scalar. The native generator at an edge
has coefficient \(2n_2T_3\). Distinct translated sources average
independently. Its averaged second derivative is therefore
\(-4\Gamma/3\). Evenness removes the odd derivatives. Consequently
\[
\begin{split}
 \mathcal C_\theta\psi_\xi
  &=\psi_\xi-\frac23\theta^2\Gamma\psi_\xi+O_{H^k,L,\xi}(\theta^4),\\
 \chi_{\xi,\theta}
  &=-\frac23\theta^2v_\xi+O_{H^k,L,\xi}(\theta^4).
\end{split}
\tag{1.10}
\]
This is a Sobolev vector expansion; it does not regard \(\Gamma\) as
a bounded operator on \(L^2\). We will first use (1.10) at fixed \(\xi\).

The vector \(v_\xi\) is nonzero for every \(b>0\). If
\(\Gamma\psi_\xi=\gamma_\xi\psi_\xi\), Haar integration gives
\(0=\gamma_\xi\int\psi_\xi\), so \(\gamma_\xi=0\). Its quadratic
form then implies that \(\psi_\xi\) is independent of every
direction-1 edge with \(n_2\ne0\). Choose \(e=((0,1,0),1)\),
which has four incident faces for \(L\ge2\). Fix all other link
variables at the identity. The kinetic terms and \(\psi_\xi\) are
independent of \(U_e\), whereas the potential in the ground equation
is \(4b(2-\operatorname{tr}U_e)\). Smoothness permits this evaluation
and positivity makes the fixed value of \(\psi_\xi\) nonzero. The
equation is impossible for \(b>0\). This also proves that (1.10) has a
strictly positive leading squared norm at every fixed positive coupling.

## 2. The exact first-band isometry

Here are the spectral isolation and transport facts with their proof.
Peter--Weyl decomposition followed by the bounded gauge projection gives
a complete physical decomposition into link spins and invariant vertex
contractions. A nonempty support graph of such a contraction has no
degree-one vertex: a single nontrivial irreducible representation has no
invariant vector. Thus it contains a cycle. The cubic nearest-neighbor
graph is bipartite, so such a cycle has at least four edges, each costing
at least \(3/4\). If total energy is below \(9/2\), there are at most
five support edges. A four-cycle must then occur. A fifth edge could
neither have a new endpoint without a degree-one vertex nor be a chord,
since the potential chords have endpoints of the same bipartition class.
The support is a four-cycle, which is one elementary square. At its
degree-two vertices the two spins must agree and the invariant contraction
is unique by Schur's lemma. Thus its energy is \(4j(j+1)\). Below
\(9/2\) only \(j=1/2\) occurs. A six-edge rectangular loop realizes
\(9/2\). Single-link Haar integration also gives
\[
 \langle W_p,W_q\rangle=\delta_{pq},\quad
 H_0W_p=3W_p,\quad
 \ker H_0=\mathbb C1,\quad
 \ker(H_0-3)=\mathcal P=\operatorname{span}\{W_p\},
 \quad \operatorname{spec}(H_0)\cap(3,9/2)=\varnothing.
\tag{2.1}
\]
For unequal faces a link occurring in just one kills the integral by
central multiplication by \(-I\). For equal faces their holonomy is
Haar and the fundamental character has norm one: writing
\(U=u_0I+i\sum_au_a\sigma_a\) on the unit three-sphere gives
\(\int(2u_0)^2=1\). The same parity proves \(\int W_p=0\).

Let \(P\) be the projection onto \(\mathcal P\), and define
\[
 R_3=(I-P)\bigl((H_0-3)|_{\operatorname{ran}(I-P)}\bigr)^{-1}(I-P).
\tag{2.2}
\]
It acts by \(-1/3\) on constants; that channel is retained. Set
\[
 r_L=\frac3{64M},\qquad \mathcal C_3=\{z:|z-3|=3/4\},\qquad
 P_\xi=\frac1{2\pi i}\int_{\mathcal C_3}(z-K_\xi)^{-1}\,dz.
\tag{2.3}
\]
The identity \(\|S\|=2M\) follows from its pointwise bound and the
identity configuration with positive-measure neighborhoods. On
\(\mathcal C_3\), the free resolvent has norm at most \(4/3\).
For complex \(|\xi|\le r_L\) the Neumann factor is at most \(1/8\),
and hence
\[
 \|(z-K_\xi)^{-1}\|\le\frac{32}{21},\qquad
 \|P_\xi-P\|\le\frac17.
\tag{2.4}
\]
The latter follows by integrating the resolvent difference:
\((3/4)(4/3)^2(2Mr_L)/(1-1/8)=1/7\). These analytic idempotents
have rank \(M\) by continuous deformation from \(P\). On \(\mathcal P\),
let
\[
 T_\xi=PP_\xi P|_{\mathcal P},\qquad
 V_\xi=P_\xi P T_\xi^{-1/2}:\mathcal P\longrightarrow\operatorname{ran}P_\xi.
\tag{2.5}
\]
The convergent binomial series at \(I\) defines the inverse square root
since \(\|T_\xi-I\|\le1/7\). With
\(U_\xi=T_\xi^{-1/2}PP_\xi\) on \(\operatorname{ran}P_\xi\),
idempotence gives \(U_\xi V_\xi=I\), and equal dimensions give the
reverse identity. For real \(\xi\), \(P_\xi\) is orthogonal and
\(U_\xi=V_\xi^*\), so \(V_\xi\) is an isometry onto the actual
spectral subspace. The full Gram factor is part of this exact coordinate
map. Its range is smooth by elliptic regularity and finite rank.
The contour also makes \(K_\xi P_\xi\) bounded via the integral with
integrand \(z(z-K_\xi)^{-1}\); all intertwining products are thus defined.

For real \(|\xi|\le r_L/2\), min--max moves each ordered physical
eigenvalue by at most \(2M|\xi|\le3/64\). There is one bottom, then
exactly \(M\) eigenvalues near 3, and every other eigenvalue is at least
\(9/2-3/64\). Thus \(P_\xi\) is precisely the first physical band,
and \(P_\xi\psi_\xi=0\) exactly. Define its exact matrix
\[
 B_\xi=U_\xi K_\xi V_\xi,
 \qquad \mathscr A_\xi V_\xi
      =V_\xi\kappa(B_\xi-e(\xi)I).
\tag{2.6}
\]
For every bounded Borel function \(f\), functional calculus gives
\[
 f(\mathscr A_\xi)P_\xi
 =V_\xi f\bigl(\kappa(B_\xi-e(\xi)I)\bigr)V_\xi^*.
\tag{2.7}
\]
Indeed an orthonormal eigenbasis of the finite Hermitian matrix is mapped
by \(V_\xi\) to an orthonormal eigenbasis of its invariant subspace;
both sides act by the same scalar on those vectors and vanish on its
orthogonal complement. This proves the exact observable map as well as
the exact state-space map.

The bottom projection near zero has the analogous isolated contour, so
\(e(\xi)\) and the positively chosen unit \(\psi_\xi\) are analytic
near zero. The equation
\[
 \psi_\xi=(H_0+1)^{-1}[(1+e(\xi)+\xi S)\psi_\xi]
\tag{2.8}
\]
and boundedness of smooth multiplication in each Sobolev space upgrade
analyticity by two derivatives at a time. Thus every fixed Sobolev
Taylor expansion used below is justified at fixed \(L\).

## 3. Every second-order channel and the coefficient energies

For a repeated face and for an unordered adjacent pair with shared edge
\(e\), put
\[
 Y_p=W_p^2-1,\qquad
 Z_{pq,0}=\int W_pW_q\,dU_e,\qquad Z_{pq,1}=W_pW_q-Z_{pq,0}.
\tag{3.1}
\]
An adjacent pair means two distinct faces sharing one physical edge,
including coplanar and hinged pairs. All other unordered distinct pairs
are called edge-disjoint, even when they share a vertex. Reverse one face
traversal if necessary and cyclically write its pair of traces as
\(\operatorname{tr}(U_eA)\operatorname{tr}(U_e^{-1}B)\).
The identity \(\int U_{ij}\overline U_{kl}\,dU
=\delta_{ik}\delta_{jl}/2\) gives
\(Z_{pq,0}=\operatorname{tr}(AB)/2\). The six outer links are distinct.
The shared-edge tensor product has spins 0 and 1, while every outer edge
has spin \(1/2\). Repeated-face character multiplication gives spin 1
on its four edges. Consequently the complete table is
\[
\begin{array}{c|ccccc}
 \text{vector}&1&Y_p&W_pW_q\ (\text{edge-disjoint})&Z_{pq,0}&Z_{pq,1}\\\hline
 H_0\text{ eigenvalue}&0&8&6&9/2&13/2\\
 \text{squared norm}&1&1&1&1/4&3/4.
\end{array}
\tag{3.2}
\]
For the last two norms the Haar projection in (3.1) is orthogonal,
its image is half a norm-one character, and the original product has
squared norm one by integrating the independent outer Haar words first.
The other norms follow from the same character integration.

Vectors belonging to different unordered distinct pairs are orthogonal.
Their odd link parity is exactly \(\partial p\mathbin\triangle\partial q\),
in either shared-edge channel. If different pairs had the same parity,
their symmetric difference would be a nonempty closed mod-two set of at
most four squares. Any square in that set needs another square on each
of its four edges. Distinct elementary squares share at most one edge,
so at least four *other* squares would be necessary, a contradiction.
Integrating a link of unequal parity proves orthogonality. Repeated-face
vectors have even parity everywhere and so are orthogonal to distinct
pairs; distinct \(Y_p\)'s have different link-spin assignments. Constants
are orthogonal to all these nonconstant vectors. All orthogonalities
remain valid after applying \(H_0\), \(R_3\), or \(\Gamma\), since
the displayed vectors have definite joint link spins.

Comparing coefficients in the vacuum equation and its unit norm gives
\[
\begin{split}
 \psi_\xi&=1+\xi A+\xi^2 B^{\rm vac}+O_{H^k,L}(\xi^3),
   \qquad A=S/3,\\
 H_0B^{\rm vac}&=(S^2-M)/3,
   \qquad \int B^{\rm vac}=-M/18,\\
 B^{\rm vac}&=-\frac M{18}+\sum_p\frac{Y_p}{24}
 +\sum_{\{p,q\}\,\text{edge-disjoint}}\frac{W_pW_q}{9}
 +\sum_{\{p,q\}\,\text{adjacent}}
       \left(\frac4{27}Z_{pq,0}+\frac4{39}Z_{pq,1}\right),\\
 e(\xi)&=-\frac M3\xi^2+O_L(\xi^4).
\end{split}
\tag{3.3}
\]
The third line follows by expanding \(S^2-M\) into the repeated-face
terms and twice every distinct unordered pair, and dividing by the
energies in (3.2). The bottom coefficient is
\(-\langle S,A\rangle=-M/3\). The even remainder follows from the
parity proved below.

Let \(\mathscr D=R_3SP:\mathcal P\to\mathcal P^\perp\). For any
\(x=\sum_px_pW_p\), table (3.2) gives its entire value:
\[
\begin{split}
 \mathscr D x={}&-\frac13\sum_px_p
 +\frac15\sum_px_pY_p
 +\frac13\sum_{\{p,q\}\,\text{edge-disjoint}}(x_p+x_q)W_pW_q\\
 &+\sum_{\{p,q\}\,\text{adjacent}}(x_p+x_q)
           \left(\frac23Z_{pq,0}+\frac27Z_{pq,1}\right).
\end{split}
\tag{3.4}
\]
Differentiating \(P_\xi^2=P_\xi\) gives \(PP'_0P=0\).
Differentiating (2.5) therefore gives \(PV'_0=0\). The derivative of
the intertwining equation \(K_\xi V_\xi=V_\xi B_\xi\), projected
onto \(\mathcal P^\perp\), gives \(V'_0=\mathscr D\). Its
second-order projection onto \(\mathcal P\) gives
\[
 B_\xi=3I-\xi^2PSR_3SP+O_L(\xi^3).
\tag{3.5}
\]
The first-order projected term vanishes: the central link cochain
\(z_i(n)=(-1)^{\sum_{j<i}n_j}I\) changes the sign of every face.
It defines a Haar unitary involution \(\mathcal Z\) commuting with all
\(E_e\), gauge transformations, and native translations. It fixes 1
and is \(-I\) on \(\mathcal P\); hence \(PSP=0\).
The same cochain proves
\[
\begin{gathered}
 K_{-\xi}=\mathcal ZK_\xi\mathcal Z,\quad
 \psi_{-\xi}=\mathcal Z\psi_\xi,\quad e(-\xi)=e(\xi),\quad
 P_{-\xi}=\mathcal ZP_\xi\mathcal Z,\\
 T_{-\xi}=T_\xi,\qquad V_{-\xi}=-\mathcal ZV_\xi,
 \qquad B_{-\xi}=B_\xi.
\end{gathered}
\tag{3.6}
\]
Thus the odd matrix coefficients in (3.5) vanish without choosing labels
inside a degenerate eigenspace.

Define the actual open-box face adjacency matrix \(A_L^{\rm face}\) by
shared-edge adjacency, its degrees \(d_p\), and
\[
 Q_L=\operatorname{diag}(d_p)+A_L^{\rm face},\qquad
 F_L=\frac7{15}I-\frac1{21}Q_L.
\tag{3.7}
\]
We identify matrices on \(\ell^2(\mathsf P_L)\) with matrices on
\(\mathcal P\) by the exact unitary
\(\mathcal Jx=\sum_px_pW_p\), justified by (2.1).
The constant channel in \(-PSR_3SP\) contributes \(+1/3\) to every
matrix entry. A repeated face contributes \(-1/5\) to its diagonal.
Each edge-disjoint pair contributes \(-1/3\) to its two diagonals and
two mutual off-diagonals. Each adjacent pair contributes to that same
four-entry pattern
\[
 -\frac{1/4}{9/2-3}-\frac{3/4}{13/2-3}
 =-\frac16-\frac3{14}=-\frac8{21}.
\tag{3.8}
\]
Hence its diagonal is
\(1/3-1/5-(M-1-d_p)/3-8d_p/21
=7/15-M/3-d_p/21\); its off-diagonal is \(-1/21\) for adjacent
faces and zero otherwise. Adding the actual vacuum subtraction \(M/3\)
in (3.3) proves
\[
 B_\xi-e(\xi)I=3I+\xi^2F_L+\mathcal R_\xi,
 \qquad \|\mathcal R_\xi\|\le\frac73 r_L^{-4}|\xi|^4
 \quad (|\xi|\le r_L/2).
\tag{3.9}
\]
Here is also the bound's proof. The binomial series in (2.5) bounds
\(\|T_\xi^{-1/2}\|\le\sqrt{7/6}\); the contour for
\(B_\xi-3I\) gives norm at most
\((7/6)(3/4)^2(32/21)=1\). The bottom contour \(|z|=3/4\) gives
\(|e(\xi)|\le3/4\). Thus the even analytic matrix
\(B_\xi-e(\xi)I-3I\) has norm at most \(7/4\) on \(|\xi|=r_L\).
Cauchy's estimate and a geometric series bound its terms of degree at
least four by \((7/4)\sum_{k\ge2}(|\xi|/r_L)^{2k}
\le(7/3)r_L^{-4}|\xi|^4\). The contour and binomial inequalities are
strict at their singularity thresholds, so analyticity extends to a
neighborhood of that circle and the Cauchy estimate is legitimate.

For every face vector \(x\),
\(\langle x,Q_Lx\rangle=\sum_{\{p,q\}\,\text{adjacent}}|x_p+x_q|^2\).
Every edge has at most four incident faces, so \(d_p\le12\).
Therefore \(0\le Q_L\le24I\) as quadratic forms, by
\(|x_p+x_q|^2\le2|x_p|^2+2|x_q|^2\). In particular
\(\operatorname{spec}(F_L)\subset[-71/105,7/15]\), with each exact
coefficient energy \(7/15-q/21\) corresponding to a spectral value
\(q\) of the same finite \(Q_L\).

## 4. Transport of the actual magnetic variance vector

Define the original face weights
\[
 a_p=\frac14\sum_{e\in\partial p}w_e,
 \qquad \mathbf a=\sum_pa_pW_p=\mathcal J(a_p)_p.
\tag{4.1}
\]
In all three planes their exact values are
\[
 a_{n;1,2}=\frac{n_2^2+(n_2+1)^2}{4},\qquad
 a_{n;1,3}=\frac{n_2^2}{2},\qquad a_{n;2,3}=0.
\tag{4.2}
\]
Since each boundary link of \(W_p\) has Casimir \(3/4\),
\(\Gamma W_p=3a_pW_p\), so \(\Gamma A=\mathbf a\).
The vacuum scalar in (1.9) is
\[
 \gamma_\xi=\frac{\xi^2}{3}\sum_pa_p+O_L(\xi^4),
\tag{4.3}
\]
because \(\Gamma1=0\),
\(\langle A,\Gamma A\rangle=\sum_pa_p/3\), and (3.6) makes the
scalar even. Let
\(\mathbf t=\Gamma B^{\rm vac}-(\sum_pa_p)/3\). Then
\[
 v_\xi=\xi\mathbf a+\xi^2\mathbf t+O_{H^k,L}(\xi^3).
\tag{4.4}
\]
To spell out every coefficient, put \(s_{pq}=a_p+a_q\) for a pair
and let \(w_e\) retain its original value on its shared edge. Its
weighted electric eigenvalues are
\[
\begin{array}{c|cccc}
 \text{vector}&Y_p&W_pW_q\ (\text{edge-disjoint})&Z_{pq,0}&Z_{pq,1}\\\hline
 \Gamma\text{ eigenvalue}&8a_p&3s_{pq}&3s_{pq}-3w_e/2&3s_{pq}+w_e/2.
\end{array}
\tag{4.5}
\]
For the shared edge, \(3s_{pq}\) counts its two fundamental values
as \(3w_e/2\). Replacing these by spin zero subtracts \(3w_e/2\);
replacing them by spin one adds \(w_e/2\). This proves the last two
entries, including direction-2 and direction-3 shared edges where
\(w_e=0\). Inserting (4.5) into (3.3) proves
\[
\begin{split}
 \mathbf t={}&-\frac13\sum_pa_p+\sum_p\frac{a_p}{3}Y_p
 +\sum_{\{p,q\}\,\text{edge-disjoint}}\frac{s_{pq}}3 W_pW_q\\
 &+\sum_{\{p,q\}\,\text{adjacent}}
 \left[\frac{4s_{pq}-2w_e}{9}Z_{pq,0}
       +\frac{12s_{pq}+2w_e}{39}Z_{pq,1}\right].
\end{split}
\tag{4.6}
\]

The exact transported magnetic coordinates and exact remainder are
\[
 y_\xi=V_\xi^*v_\xi=V_\xi^*\Gamma\psi_\xi\in\mathcal P,
 \qquad \rho_\xi=(I-P_\xi)v_\xi\in\mathcal H_{\rm phys},
 \qquad v_\xi=V_\xi y_\xi+\rho_\xi.
\tag{4.7}
\]
The equality dropping the scalar in \(y_\xi\) follows from the exact
identity \(V_\xi^*\psi_\xi=0\); no free-vacuum orthogonality is
substituted. Both summands are orthogonal to \(\psi_\xi\), and the
two summands are mutually orthogonal. The first lies in the actual band,
the second in its orthogonal complement with its ground-state component
exactly zero. These maps are defined on all smooth vectors here, and
\(V_\xi^*\) also extends boundedly to the whole Hilbert space.

Equations (3.4), (4.4), and \(P\mathbf t=0\) give
\[
\begin{split}
 y_\xi&=\xi\mathbf a+O_L(\xi^3),\\
 P_\xi v_\xi&=\xi\mathbf a+\xi^2\mathscr D\mathbf a
                             +O_{H^k,L}(\xi^3),\\
 \rho_\xi&=\xi^2\mathbf r+O_{H^k,L}(\xi^3),
 \qquad \mathbf r=\mathbf t-\mathscr D\mathbf a.
\end{split}
\tag{4.8}
\]
For the first line, \(V_\xi=I+\xi\mathscr D+O(\xi^2)\),
\(\mathscr D\mathbf a\perp\mathcal P\), and \(P\mathbf t=0\)
remove the quadratic term. Alternatively (3.6),
\(v_{-\xi}=\mathcal Z v_\xi\), and \(V_{-\xi}=-\mathcal ZV_\xi\)
give the exact odd identity \(y_{-\xi}=-y_\xi\). Every other
remainder assertion in (4.8) is in the fixed Sobolev norm indicated,
using (2.8) and finite-rank elliptic regularity for \(V_\xi\).

Subtracting the full expressions (3.4) and (4.6) gives
\[
\boxed{
 \mathbf r=\sum_p\frac{2a_p}{15}Y_p
 +\sum_{\{p,q\}\,\text{adjacent}}
   \left[-\frac{2(s_{pq}+w_e)}9Z_{pq,0}
         +\frac{2(3s_{pq}+7w_e)}{273}Z_{pq,1}\right].}
\tag{4.9}
\]
The two constants both equal \(-\sum_pa_p/3\) and cancel. The
edge-disjoint coefficients both equal \(s_{pq}/3\) and cancel.
The repeated coefficient is \(a_p(1/3-1/5)=2a_p/15\).
The adjacent coefficients are
\((4s-2w)/9-2s/3=-2(s+w)/9\) and
\((12s+2w)/39-2s/7=2(3s+7w)/273\).
These calculations prove every retained and cancelled channel.
In particular the exact physical band is not obtained by projecting with
the free \(P\): its constant, repeated-face, edge-disjoint, and both
adjacent-face dressings in (3.4) all enter before the subtraction.

Write the following exact nonnegative finite sums:
\[
\begin{split}
 \mathsf N_L&=\|\mathbf a\|^2=\sum_pa_p^2,\\
 \mathsf R_{8,L}&=\frac4{225}\mathsf N_L,\\
 \mathsf R_{9/2,L}&=\frac1{81}
      \sum_{\{p,q\}\,\text{adjacent}}(s_{pq}+w_e)^2,\\
 \mathsf R_{13/2,L}&=\frac1{24843}
      \sum_{\{p,q\}\,\text{adjacent}}(3s_{pq}+7w_e)^2,\\
 \mathsf R_L&=\mathsf R_{8,L}+\mathsf R_{9/2,L}+\mathsf R_{13/2,L}.
\end{split}
\tag{4.10}
\]
The coefficient \(1/24843\) is
\((3/4)\cdot4/273^2\). Orthogonality and (3.2) prove
\(\|\mathbf r\|^2=\mathsf R_L\). In particular
\(\mathsf R_L\ge4\mathsf N_L/225>0\), since (4.2) has positive
12-face entries. From coupling parity and (4.8),
\[
\begin{split}
 \|v_\xi\|^2&=\xi^2\mathsf N_L+O_L(\xi^4),\qquad
 \|P_\xi v_\xi\|^2=\xi^2\mathsf N_L+O_L(\xi^4),\\
 \|\rho_\xi\|^2&=\xi^4\mathsf R_L+O_L(\xi^6),
 \qquad \|\rho_\xi\|=\xi^2\sqrt{\mathsf R_L}+O_L(\xi^4),\\
 \frac{\|\rho_\xi\|^2}{\|v_\xi\|^2}
   &=\xi^2\frac{\mathsf R_L}{\mathsf N_L}+O_L(\xi^4)
       \quad (\xi\downarrow0).
\end{split}
\tag{4.11}
\]
Indeed \(\rho_{-\xi}=\mathcal Z\rho_\xi\); its squared norm is
even analytic, so its possible fifth coefficient vanishes. The square
root estimate follows because \(\mathsf R_L>0\). The divisions use
\(\mathsf N_L>0\) at this fixed box.

The mass \(\mathsf N_L\) retains the explicit original polynomial:
\[
\boxed{
 \mathsf N_L=\frac{L^2(2L+1)}{60}
       (24L^4+24L^3+8L^2-4L+3).}
\tag{4.12}
\]
To prove it directly, for each \(m=n_2\) there are \(2L(2L+1)\)
12-faces and \(4L^2\) 13-faces. Put \(r_m=m^2+m+1/2\), so the
two coefficients are \(r_m/2\) and \(m^2/2\). Hence
\[
 \mathsf N_L=\frac14\left[
 2L(2L+1)\sum_{m=-L}^{L-1}r_m^2
 +4L^2\sum_{m=-L}^Lm^4\right].
\tag{4.13}
\]
The exact sums are
\(\sum_{m=-L}^{L-1}r_m^2=L(4L^4+1)/10\) and
\(\sum_{m=-L}^Lm^4=L(L+1)(2L+1)(3L^2+3L-1)/15\).
The first polynomial has value \(1/2\) at \(L=1\) and increment
\(2(L^2+L+1/2)^2\); the second has value 2 and increment
\(2(L+1)^4\). These are exactly the endpoint increments of the
respective sums, proving them by induction. Substitution proves (4.12).
The distinct sum needed in (4.3) is
\[
 \sum_pa_p=\frac{L^2(2L+1)(4L^2+2L+1)}3.
\tag{4.14}
\]
Its proof uses the same counts and the sums
\(\sum_{m=-L}^{L-1}r_m=L(2L^2+1)/3\) and
\(\sum_{m=-L}^Lm^2=L(L+1)(2L+1)/3\), each verified by its value
at 1 and its two endpoint increments.

The full open-boundary evaluation of the leakage sum (4.10), proved by
the original adjacent-face classification in
[native_magnetic_leakage_volume_polynomial.md](native_magnetic_leakage_volume_polynomial.md),
is
\[
\boxed{\begin{split}
 \mathsf R_L=\frac1{251535375}\bigl(&153001392L^7+15594888L^6
 +129973560L^5-21634000L^4\\
 &-3201942L^3+4992787L^2-1917900L\bigr).
\end{split}}
\tag{4.15}
\]
That proof evaluates each of the two distinct shared-edge sums separately,
retaining their factors \(1/81\) and \(1/24843\). With
\(\mathsf N_L=\|\mathbf a\|^2\) exactly as in (4.12), it gives
\[
 \frac{\mathsf R_L}{\mathsf N_L}
 =\frac{12750116}{16769025}-\frac{54848}{51597L}
       +\frac{3233332}{2012283L^2}+O(L^{-3}).
\tag{4.16}
\]
This is a limit of the explicitly computed coefficient ratio in (4.11).
Its fixed-box quantum remainder is still \(O_L(\xi^4)\) there;
(4.16) does not assert a uniform estimate for that remainder.

## 5. Finite angles retain further nonlinear channels

The exact map (4.7) extends without a small-angle approximation:
\[
 z_{\xi,\theta}=V_\xi^*\chi_{\xi,\theta}
                =V_\xi^*\mathcal C_\theta\psi_\xi,
 \qquad
 \chi_{\xi,\theta}=V_\xi z_{\xi,\theta}
                     +(I-P_\xi)\chi_{\xi,\theta}.
\tag{5.1}
\]
Both terms are orthogonal to the actual vacuum. These exact expressions,
with (1.7)--(1.8), retain all higher electric representations of that
vacuum. In particular no replacement of \(\psi_\xi\) by its free
constant term is made in the map.

We can also exhibit every channel of its second coupling coefficient at
an arbitrary fixed angle. Set
\[
 \alpha_p=\prod_{e\in\partial p,\ e=(n,1)}\cos(\theta n_2),
 \qquad \beta_p=\prod_{e\in\partial p,\ e=(n,1)}c_1(\theta n_2),
 \qquad u_p(\theta)=\frac{\alpha_p-1}{3}.
\tag{5.2}
\]
Thus \(\alpha_{12}=\cos(n_2\theta)\cos((n_2+1)\theta)\),
\(\alpha_{13}=\cos^2(n_2\theta)\), and \(\alpha_{23}=1\).
For adjacent \(p,q\) sharing \(e\), let
\[
 k_{pq,j}(\theta)=
 \prod_{f\in\partial p\mathbin\triangle\partial q,\ f=(n,1)}
                     \cos(\theta n_2)
 \times
 \begin{cases}c_j(\theta n_2(e)),&e\text{ is direction 1},\\1,&\text{otherwise},\end{cases}
 \qquad j=0,1.
\tag{5.3}
\]
These are the exact multipliers of \(Z_{pq,j}\); (1.8) and their
joint spins prove this assertion. The multiplier of an edge-disjoint
product is \(\alpha_p\alpha_q\), and that of \(Y_p\) is \(\beta_p\).
Every product includes its original source coordinate.

The vacuum overlap has coefficient
\(c_{\xi,\theta}=1+\xi^2\sum_p(\alpha_p-1)/9+O_L(\xi^4)\),
as follows by inserting (3.3), using the mean of \(B^{\rm vac}\),
and \(\langle A,\mathcal C_\theta A\rangle=\sum_p\alpha_p/9\).
Therefore
\[
 z_{\xi,\theta}=\xi\sum_pu_p(\theta)W_p+O_{L,\theta}(\xi^3),
 \qquad
 (I-P_\xi)\chi_{\xi,\theta}
       =\xi^2\mathbf r_\theta+O_{H^k,L,\theta}(\xi^3),
\tag{5.4}
\]
where the complete finite sum is
\[
\begin{split}
 \mathbf r_\theta={}&
 \sum_p\left[\frac{\beta_p-1}{24}-\frac{u_p}{5}\right]Y_p\\
 &+\sum_{\{p,q\}\,\text{edge-disjoint}}
       \frac{(\alpha_p-1)(\alpha_q-1)}9 W_pW_q\\
 &+\sum_{\{p,q\}\,\text{adjacent}}
   \left[\frac4{27}(k_{pq,0}-1)-\frac23(u_p+u_q)\right]Z_{pq,0}\\
 &+\sum_{\{p,q\}\,\text{adjacent}}
   \left[\frac4{39}(k_{pq,1}-1)-\frac27(u_p+u_q)\right]Z_{pq,1}.
\end{split}
\tag{5.5}
\]
To prove it, the second centered coefficient is
\((\mathcal C_\theta-I)B^{\rm vac}
 -[\sum_p(\alpha_p-1)/9]1\). Subtract the entire dressing
\(\mathscr D\sum_pu_pW_p\) from (3.4). Its constant equals the same
\(-\sum_p(\alpha_p-1)/9\) and cancels. The other coefficients are
exactly those displayed. In particular the edge-disjoint coefficient is
\((\alpha_p\alpha_q-1)/9-(\alpha_p+\alpha_q-2)/9\), proving its
displayed product, which need not vanish at a finite angle.

Finally (1.10) applied to each of these finitely many smooth channels,
or the explicit character Taylor expansion, proves
\[
 \sum_pu_p(\theta)W_p=-\frac23\theta^2\mathbf a+O_{H^k,L}(\theta^4),
 \qquad \mathbf r_\theta=-\frac23\theta^2\mathbf r+O_{H^k,L}(\theta^4).
\tag{5.6}
\]
The finite-angle edge-disjoint terms are of order \(\theta^4\) here;
their absence in (4.9) follows from their proved angular order. They are
present in the exact state and in (5.5).

## 6. Full leading first-band spectral measure

For real \(0<\xi\le r_L/2\), define the exact first-band coefficient
matrix and the physical energy map
\[
 C_\xi=\frac{B_\xi-e(\xi)I-3I}{\xi^2},\qquad
 t_\xi(\lambda)=\frac{\lambda/\kappa-3}{\xi^2},\qquad
 s_\xi(c)=\kappa(3+\xi^2c).
\tag{6.1}
\]
These are mutually inverse affine maps between physical excitation
energy and its second coupling coefficient. Their \(\kappa\) is the
same coefficient in (1.2); no rescaled physical Hamiltonian is substituted.
Equation (3.9) gives the explicit norm estimate
\[
 \|C_\xi-F_L\|\le\frac73r_L^{-4}\xi^2.
\tag{6.2}
\]

Let \(E^{Q_L}_q\) be the orthogonal projection onto the eigenspace of
the finite real symmetric \(Q_L\) with eigenvalue \(q\), and define
the exact finite measures
\[
 \mu_L^a=\sum_{q\in\operatorname{spec}Q_L}
          \|E^{Q_L}_q(a_p)_p\|_{\ell^2}^2\,\delta_q,
 \qquad
 \eta_L^a=\left(q\mapsto\frac7{15}-\frac q{21}\right)_*\mu_L^a.
\tag{6.3}
\]
Repeated eigenvalues are handled by the entire eigenspace projection,
so these definitions do not depend on choices of eigenvectors. Their
total mass is \(\mathsf N_L\), not 1, by completeness. Formula (3.7)
and the unitary \(\mathcal J\) prove the exact coefficient-observable
identity
\[
 \int f(c)\,d\eta_L^a(c)
 =\langle\mathbf a,f(F_L)\mathbf a\rangle
 =\sum_q\|E^{Q_L}_q(a_p)_p\|^2f\!\left(\frac7{15}-\frac q{21}\right).
\tag{6.4}
\]

For the actual state define its physical first-band measure by
\[
 \mu^{\rm band}_{\xi,\theta}(J)
 =\langle P_\xi\chi_{\xi,\theta},
             1_J(\mathscr A_\xi)P_\xi\chi_{\xi,\theta}\rangle
 \quad (J\text{ Borel in }\mathbb R).
\tag{6.5}
\]
Equations (2.7) and (5.1) give its exact pushforward, at every angle,
\[
 (t_\xi)_*\mu^{\rm band}_{\xi,\theta}(J)
     =\langle z_{\xi,\theta},1_J(C_\xi)z_{\xi,\theta}\rangle,
 \qquad
 \mu^{\rm band}_{\xi,\theta}
     =(s_\xi)_*\mu_{C_\xi,z_{\xi,\theta}}.
\tag{6.6}
\]
Here \(\mu_{C,z}(J)=\langle z,1_J(C)z\rangle\). This is the exact
map of both the actual vector and all its first-band observables.

For every bounded continuous function \(f:\mathbb R\to\mathbb C\),
the complete leading statement in the requested order of limits is
\[
\boxed{
 \lim_{\xi\downarrow0}\frac1{\xi^2}
 \left[\lim_{\theta\to0}\frac9{4\theta^4}
  \int f\bigl(t_\xi(\lambda)\bigr)
             \,d\mu^{\rm band}_{\xi,\theta}(\lambda)\right]
 =\int f(c)\,d\eta_L^a(c).}
\tag{6.7}
\]
Indeed (1.10) and boundedness of the relevant finite-dimensional
functional calculus give the inner limit as
\(\langle y_\xi,f(C_\xi)y_\xi\rangle\). Dividing by \(\xi^2\),
the vector tends to \(\mathbf a\) by (4.8), and
\(f(C_\xi)\to f(F_L)\) in matrix norm by (6.2). To justify the last
assertion without a differentiability assumption on \(f\), all spectra
are eventually in one compact interval. Approximate the restriction of
the real and imaginary parts of \(f\) uniformly by polynomials. Polynomial
functional calculus is continuous in the matrix entries; spectral
calculus bounds each uniform approximation error by its scalar supremum.
First pass \(\xi\to0\), then let that error tend to zero. This proves
(6.7) for precisely the stated bounded-continuous class. No estimate of
order \(\xi^2\) for an arbitrary continuous \(f\) is asserted.

Equivalently, keeping the actual norm as the denominator gives
\[
 \lim_{\xi\downarrow0}\left[\lim_{\theta\to0}
 \frac{\displaystyle\int f(t_\xi(\lambda))
                     \,d\mu^{\rm band}_{\xi,\theta}(\lambda)}
      {\|\chi_{\xi,\theta}\|^2}\right]
       =\frac1{\mathsf N_L}\int f(c)\,d\eta_L^a(c).
\tag{6.8}
\]
This is an explicitly defined probability comparison derived by division
of (6.7) and the independently retained mass formula; it does not alter
the original state or discard its amplitude.

The physical coefficient locations, with every original scale substituted,
are
\[
 \kappa\left[3+\xi^2\left(\frac7{15}-\frac q{21}\right)\right]
 =\frac{6g_{\rm YM}^2}{a}
  +\frac1{8g_{\rm YM}^6a}\left(\frac7{15}-\frac q{21}\right).
\tag{6.9}
\]
Equation (6.6) is the exact physical pushforward; (6.7) resolves its
leading coefficient measure at every \(q\), including all its weights.
Individual eigenvalues of the actual band differ from the ordered
coefficient predictions by at most
\(\kappa(7/3)r_L^{-4}\xi^4\), by (3.9) and min--max. Within a
degenerate coefficient eigenspace higher orders may split eigenvalues;
the spectral measure formulation retains their aggregate limiting weight
without making an unsupported choice of split eigenvectors.

For fixed \(\kappa>0\), without coefficient resolution one also gets
\[
 \lim_{\xi\downarrow0}\frac1{\xi^2}
 \left[\lim_{\theta\to0}\frac9{4\theta^4}
            \int f(\lambda)\,d\mu^{\rm band}_{\xi,\theta}(\lambda)\right]
 =\mathsf N_L f(3\kappa).
\tag{6.10}
\]
If \(\kappa\) varies with the original \(g_{\rm YM},a\) while
\(\xi\to0\), (6.6)--(6.9) remain the applicable exact pushforward and
coefficient statements; (6.10) specifically requires fixed \(\kappa\).

## 7. Out-of-band order and its leading physical spectral measure

Set \(\chi^{\rm out}_{\xi,\theta}=(I-P_\xi)\chi_{\xi,\theta}\).
It is smooth, orthogonal to the actual vacuum and to the entire actual
first band. At each fixed positive \(\xi\) in the band interval,
(1.10) proves
\[
 \lim_{\theta\to0}\frac9{4\theta^4}
          \|\chi^{\rm out}_{\xi,\theta}\|^2=\|\rho_\xi\|^2,
 \qquad
 \lim_{\theta\to0}\frac9{4\theta^4}
          \|\chi_{\xi,\theta}\|^2=\|v_\xi\|^2.
\tag{7.1}
\]
Therefore the precise nonzero leading out-of-band norm is
\[
\boxed{
 \lim_{\xi\downarrow0}\frac1{\xi^4}
 \left[\lim_{\theta\to0}\frac9{4\theta^4}
               \|\chi^{\rm out}_{\xi,\theta}\|^2\right]=\mathsf R_L>0,}
\tag{7.2}
\]
and its retained fraction is
\[
 \lim_{\theta\to0}
   \frac{\|\chi^{\rm out}_{\xi,\theta}\|^2}{\|\chi_{\xi,\theta}\|^2}
  =\xi^2\frac{\mathsf R_L}{\mathsf N_L}+O_L(\xi^4).
\tag{7.3}
\]
In unsquared norms the ordered leading amplitude is
\((2/3)\theta^2\xi^2\sqrt{\mathsf R_L}\); for the whole state it
is \((2/3)\theta^2\xi\sqrt{\mathsf N_L}\), with \(\xi>0\).
More precisely, first
\(\lim_{\theta\to0}3\|\chi^{\rm out}_{\xi,\theta}\|/(2\theta^2)
=\|\rho_\xi\|\), and then use (4.11). These are ordered limits,
so no unstated uniformity in \(L,\theta,\xi\) is used.

Define \(\mu^{\rm out}_{\xi,\theta}\) by (6.5) with
\(P_\xi\chi\) replaced by \(\chi^{\rm out}\). For fixed \(\kappa\)
and every bounded continuous \(f\), its full leading measure is
\[
\boxed{
 \lim_{\xi\downarrow0}\frac1{\xi^4}
 \left[\lim_{\theta\to0}\frac9{4\theta^4}
     \int f(\lambda)\,d\mu^{\rm out}_{\xi,\theta}(\lambda)\right]
 =\mathsf R_{8,L}f(8\kappa)
  +\mathsf R_{9/2,L}f(9\kappa/2)
  +\mathsf R_{13/2,L}f(13\kappa/2).}
\tag{7.4}
\]
If physical \(\kappa\) varies, replace the test in the integrand by
\(f(\lambda/\kappa)\); the right side then has arguments
\(8,9/2,13/2\). This is its exact dimensionless-to-physical pushforward.

Here is a proof of the functional-calculus limit, including its high-energy
tail. Put \(u_\xi=\rho_\xi/\xi^2\). By (4.8),
\(u_\xi\to\mathbf r\) in \(H^2\), and
\((K_\xi-e(\xi))u_\xi\to H_0\mathbf r\) in Hilbert norm.
Thus these vectors have uniformly bounded norm and uniformly bounded
second spectral moment. For a real spectral cutoff \(R>0\), the
spectral mass at \(|\lambda|>R\) of either vector is bounded by its
second moment divided by \(R^2\). Also \(K_\xi-e(\xi)\) converges
in norm resolvent to \(H_0\): their difference
\(-\xi S-e(\xi)I\) is bounded with norm tending to zero, and the
resolvent identity proves convergence at a nonreal spectral parameter.
The algebra generated by resolvents and their conjugates is uniformly
dense in \(C_0(\mathbb R)\): it separates real points, is closed under
conjugation, and is nonzero at each real point. Uniform approximation
therefore proves norm convergence of \(f_0(K_\xi-e(\xi))\) for
every \(f_0\in C_0(\mathbb R)\). For a general bounded continuous
\(f\), multiply by a continuous compactly supported cutoff equal to 1
on \([-R,R]\). The discarded expectation is at most
\(\|f\|_\infty\) times the just-proved tail mass. First use
\(u_\xi\to\mathbf r\) and the \(C_0\) convergence, and then let
\(R\to\infty\). This proves convergence for the claimed class.
Finally (4.9), orthogonality, and (3.2) give exactly the three masses
and arguments in (7.4). The angular inner limit follows independently
from (1.10) and boundedness of \(f(\mathscr A_\xi)\).

Since the exact band projection commutes with the full Hamiltonian,
the full state measure is the sum
\(\mu^{\rm band}_{\xi,\theta}+\mu^{\rm out}_{\xi,\theta}\),
with no cross term for any Borel set. Equations (6.7) and (7.2) show
that its first-band coefficient limit also holds when the full state
measure is used on the left of (6.7): the absolute contribution of
the omitted component, after the displayed angular and \(\xi^2\)
divisions, is bounded by
\(\|f\|_\infty\|\rho_\xi\|^2/\xi^2=O_L(\xi^2)\).
This remains true although \(t_\xi\) sends its higher energies to
large coefficient values; boundedness of the test function is the
precise hypothesis controlling that contribution.

There is also a direct finite-box two-parameter norm estimate, without
taking a volume limit. On a sufficiently small rectangle of real
\((\xi,\theta)\) around zero,
\[
\begin{split}
 z_{\xi,\theta}
   &=-\frac23\xi\theta^2\mathbf a
      +O_L(|\xi|^3\theta^2+|\xi|\theta^4),\\
 \chi^{\rm out}_{\xi,\theta}
   &=-\frac23\xi^2\theta^2\mathbf r
      +O_{H^k,L}(|\xi|^3\theta^2+\xi^2\theta^4).
\end{split}
\tag{7.5}
\]
In particular its out-of-band norm is \(O_L(\xi^2\theta^2)\).
Here is the joint remainder justification. By (2.8), the vacuum and its
\(\xi\)-derivatives are bounded in each needed higher Sobolev space
on a smaller closed coupling interval. Averaged translation has bounded
derivatives through order four from \(H^{k+4}\) to \(H^k\), uniformly
on a closed angle interval. The expressions in (5.1) therefore have the
corresponding bounded mixed derivatives. They are even in \(\theta\)
and identically zero at \(\theta=0\). The out-of-band expression and
its first \(\xi\)-derivative vanish at \(\xi=0\) for every angle,
by (5.4). Taylor's integral formula in \(\xi\) factors out \(\xi^2\);
Taylor's formula in \(\theta\) then factors out \(\theta^2\), with
a fourth-order angular remainder. The remaining coefficient at
\(\xi=0\) is (5.5), whose second angular coefficient is (5.6).
This proves the second line, including its mixed remainder factors.
The transported coordinate is odd in \(\xi\), by (3.6), so the
same argument factors its coupling remainder as \(\xi^3\) and
proves the first line. All constants here still depend on the fixed
original box; (7.5) does not assert a uniform volume estimate.

The physical amplitude factors in (6.7) and (7.2) are respectively
\[
 \frac49\theta^4\xi^2=\frac{\theta^4}{36g_{\rm YM}^8},
 \qquad
 \frac49\theta^4\xi^4=\frac{\theta^4}{576g_{\rm YM}^{16}},
 \qquad \theta^4=\frac{16\pi^4a^8}{D^4}.
\tag{7.6}
\]
These multiply \(\mathsf N_L\) and \(\mathsf R_L\) in the respective
ordered leading squared norms. None of those factors is absorbed into
the graph vector or the physical energy scale.

## 8. Scope of the coefficient map

Equations (1.7), (2.5), (4.7), (5.1), and (6.6) give exact maps from
the specified continuous magnetic background to the actual physical
state, its first interacting spectral subspace, and all its spectral
observables. The full leading coefficient measure is precisely the
pushforward (6.3), with the original polynomial vector (4.2). The
out-of-band contribution has the explicitly positive coefficient (4.10)
and the three leading physical energies (7.4); all finite-angle nonlinear
channels are retained in (5.5) and in the exact class operator (1.7).

Every asymptotic assertion above fixes \(L\) first. The sufficient
spectral interval is \(0<\xi\le3/(128M)\), and the explicit matrix
remainder constant grows as \(M^4\). No joint continuum convergence,
fixed-positive-coupling infinite-volume convergence, or exchange of these
limits is used. A separate limit of the completely specified finite graph
measure \(\mu_L^a\) can be pushed through the affine map in (6.3);
the exact quantum statement established here is the displayed angular-first,
coupling-second limit at every fixed original box.

The companion exact checker
[check_native_magnetic_physical_band_transport.py](check_native_magnetic_physical_band_transport.py)
constructs the original link and face incidence sets, checks the plane
weights and polynomial mass, independently divides the vacuum channel
coefficients by their electric energies, subtracts every spectral dressing
denominator, and verifies both shared-edge coefficients and their angular
factors using rational arithmetic. It also evaluates all finite-angle
second-order channels at \(\theta=\pi/3\) for \(L=2\), including
the nonzero edge-disjoint terms. The analytic and spectral arguments are
the proofs above; these arithmetic checks supplement them.
