# Exact cubic-box symmetry of the first physical gap correction

9 September 2026. The original open box, physical spacings, all SU(2)
edge links and the full Wilson Hamiltonian are retained. This note proves
that its six-by-six order-\(g^2\) first-gap matrix has three independent
entries. It is a symmetry of the original operator, not an approximation
to that matrix or a removal of spatial modes.

## 1. The original graph automorphisms

Let \(V=\{-L,\ldots,L\}^3\), with all contained positive unit edges
and elementary square faces. For a signed permutation matrix \(R\),
\(n\mapsto Rn\) is a bijection of \(V\). If \(e=(n,n+e_i)\) is a
positive edge, its image is the directed segment from \(Rn\) to
\(Rn+Re_i\). Store its original link if this direction is positive,
and the inverse original link if it is negative. Equivalently extend
link configurations to both orientations by \(U_{-e}=U_e^{-1}\),
and define
\[
 (\alpha_R U)_{Re}=U_e
 \quad\hbox{for every directed edge }e .
 \tag{1}
\]
The convention on reversed edges makes (1) a bijection of the original
positive-link configuration space, with inverse \(\alpha_{R^{-1}}\).
Define the unitary on functions by
\[
 (\mathscr S_R F)(U)=F(\alpha_{R^{-1}}U).
 \tag{2}
\]
It is unitary for product Haar probability: it permutes the factors
and possibly applies inversion, each of which preserves Haar measure.
Composition is exactly \(\mathscr S_R\mathscr S_Q=\mathscr S_{RQ}\).

Link inversion interchanges left and right Casimirs, which coincide
on SU(2): the adjoint matrix relating their three derivatives is
orthogonal, or equivalently both are the bi-invariant group Laplacian.
Thus (2) preserves \(\sum_e E_e\).
The image of an original face is the boundary of another contained
square, with a possible cyclic change of base vertex and orientation
reversal. Cyclic reordering preserves the trace; reversal takes the
inverse of its holonomy. For SU(2),
\(\operatorname{tr}U^{-1}=\operatorname{tr}U\), since the eigenvalues
are \(e^{i\theta},e^{-i\theta}\). Therefore (2) also preserves
\(\sum_p(2-\operatorname{tr}U_p)\).

Vertex gauge transformations are carried to vertex gauge transformations
by \(h_{Rn}=h_n\); substitution in (1) proves the compatibility for
both edge orientations. Consequently \(\mathscr S_R\) preserves the
physical Hilbert space and commutes with the exact original operator
\[
 H_g={2g^2\over a}\sum_e E_e+
                 {1\over2g^2a}\sum_p(2-\operatorname{tr}U_p).
 \tag{3}
\]
The positive unique unit vacuum is fixed by every \(\mathscr S_R\).
Neither \(g\) nor \(a\) is changed.

## 2. The exact linear action on the three lowest modes

Write \(m=2L\), \(N=m+1\). For the one-dimensional interval with
vertices \(l=0,\ldots,m\) and edges \(l=0,\ldots,m-1\), retain
\[
 v_0(l)=N^{-1/2},\quad
 v_1(l)=\sqrt{2/N}\cos{\pi(l+1/2)\over N},\quad
 w_1(l)=-\sqrt{2/N}\sin{\pi(l+1)\over N}.
 \tag{4}
\]
The difference operator obeys \(Dv_1=s w_1\), where
\(s=2\sin(\pi/(2N))\).
For \(i<j\), take the two orthonormal edge tensors at the frequency
triple with ones in positions \(i,j\) and zero elsewhere:
\(b_i^{ij}\) uses \(w_1\) in direction \(i\), \(v_1\) in direction
\(j\), and \(v_0\) in the remaining direction; \(b_j^{ij}\) is the
corresponding tensor with \(i,j\) interchanged. Define the unit
transverse cochain
\[
 V_{ij}={b_i^{ij}-b_j^{ij}\over\sqrt2},\qquad
                  V_{ji}=-V_{ij}.
 \tag{5}
\]
The gradient at this triple has components \((s,s)\), so (5) is
perpendicular to it. The oriented curl squared on this perpendicular
line is \(2s^2\). Thus these are the three lowest modes, with
\(\sigma_*=\sqrt2\,s\). Completeness of the original interval
tensor bases proves that there are no additional modes at this value.

For a permutation \(\pi\) of coordinate axes, the induced oriented
cochain action sends
\[
 V_{ij}\longmapsto V_{\pi(i)\pi(j)}.
 \tag{6}
\]
This includes the sign in (5) if the new indices are reversed.
For a reflection in coordinate \(r\), a vertex index becomes \(m-l\)
and an edge index becomes \(m-1-l\), with a minus sign for an oriented
edge component in that direction. Directly from (4),
\[
 v_1(m-l)=-v_1(l),\quad v_0(m-l)=v_0(l),\quad
 w_1(m-1-l)=w_1(l).
 \tag{7}
\]
Thus a reflected direction in \(\{i,j\}\) changes both terms of (5)
by a minus sign: the sine edge term acquires its orientation minus,
and the other term acquires the cosine minus. A reflection in the
remaining direction does not change either. For
\(\operatorname{diag}(\eta_1,\eta_2,\eta_3)\), this is
\[
 V_{ij}\longmapsto \eta_i\eta_j V_{ij}.
 \tag{8}
\]
Equations (6),(8) identify the full three-dimensional lowest spatial
mode representation with the exterior square of the original signed
permutation action on the coordinate axes. This is an explicit
intertwining map \(e_i\wedge e_j\mapsto V_{ij}\), including every sign.
It does not identify spatial modes with color coordinates.

In the complete transverse mode construction, choose the first three
orthonormal mode columns to be (5), in the order \(12,13,23\), and
keep the full orthogonal complement as well. The tree-coordinate map
\(x=\mathsf A z\), \(\mathsf A=G^{1/2}O\), is the one in the cubic
singlet companion: choose \(O\) by applying the exact transverse
isometry \(G^{-1/2}\mathsf T\) to this full mode basis.
Hence these first three \(z_\mu\) are actual coefficients of the
original cochains (5), not independently rescaled chord coordinates.
Every color component follows the same spatial matrix.

## 3. Transport of the symmetry through the nonlinear tree chart

The original rooted tree is not assumed to be invariant under \(R\).
There is instead an exact induced chord map. Given the tree-\(I\)
representative for chord configuration \(Z\), apply (1) and then
recompute every root-to-vertex holonomy and every rooted chord
\(t_sU_ct_t^{-1}\). Call the result \(\beta_R(Z)\).
It is a finite ordered product of the original chord variables and
their inverses. On full physical functions it implements (2).
The distinction matters: a graph symmetry may move the chosen root,
so the root-fixing gauge subgroup by itself need not be preserved.
Full vertex-gauge invariance, proved in Section 1, is what makes
the re-rooted representative implement the original unitary.
Together with the retained Haar/dilation map \(\mathcal B_g\), the
exact chart operator is
\[
 \mathscr S_{R,g}=\mathcal B_g\mathscr S_R\mathcal B_g^* .
 \tag{9}
\]
This formula defines its density and inverse, not only its argument
map. On a smaller identity chart its argument has expansion
\[
 {1\over g}\log\beta_R(\exp(gx))
                 =D\beta_R(I)x+O(g|x|^2).
 \tag{10}
\]
The product rule proves the linear part directly by replacing each
link with its additive cochain. Modulo the full gradient subspace it
is the oriented cochain transformation already computed in (6),(8).
The exact Gaussian Hilbert map keeps the determinant and Haar factors.
At \(g=0\) it therefore gives the orthogonal full transverse cochain
representation, with its induced action on the oscillator functions.

For clarity, convergence on every fixed polynomial Gaussian follows
from (10), not from assuming that the nonlinear chart is an
orthogonal transformation. On a fixed compact \(x\)-set its analytic
argument and density derivatives converge to the linear ones.
Inside a sufficiently small fixed \(y=gx\) chart, the induced map
and its inverse have bounded derivatives and Jacobians, with
\(|\log\beta_R(\exp y)|\) bounded above and below by positive
constants times \(|y|\); its derivative at zero is the invertible
linear tree representative of the oriented cochain map modulo
gradients. The inverse function theorem supplies these local
bounds. Polynomial Gaussian tails on both sides are
then bounded by a polynomial times \(e^{-c|x|^2}\).
Dominated convergence, followed by removing the fixed compact
\(x\)-set, proves strong convergence on those vectors. Smooth
cutoffs give the same assertion for the globally defined chart
vectors used in the companion's actual spectral projection.

In particular the representation on the first physical comparison
cluster is the symmetric square of the spatial representation
(6),(8). In the orthonormal six-vector basis, write
\[
 D_\mu={\sigma_*\over2\sqrt6}
           (|z_\mu|^2-6/\sigma_*)\Phi,\qquad
 O_{\mu\nu}={\sigma_*\over2\sqrt3}(z_\mu\cdot z_\nu)\Phi,\quad\mu<\nu .
 \tag{11}
\]
Spatial signed permutations send \(D_\mu\) to the corresponding
diagonal basis vector and \(O_{\mu\nu}\) to the corresponding
off-diagonal basis vector with the product of its two mode signs.
No normalization of an excitation energy or coupling is involved.

## 4. Why the actual order-two matrix must commute with this action

The companion gives an exact unitary identification
\(J_g:\mathbb R^6\to\operatorname{ran}P_g\) with the actual first
physical spectral cluster and
\[
 J_g^*(H_g-\mathcal E_g)J_g
          =\delta_*I+g^2\mathsf K+O_{L,a}(g^3),\qquad
                         \delta_*={2\sigma_*\over a}.
 \tag{12}
\]
It is constructed from cutoff quasimodes, the actual spectral projector
\(P_g\), and the positive square root of their Gram matrix.
Each column converges under the chart map to (11). Since
\(\mathscr S_R\) commutes with (3), it preserves \(\operatorname{ran}P_g\).
The exact finite matrix
\[
 D_g(R)=J_g^*\mathscr S_RJ_g
 \tag{13}
\]
is orthogonal and commutes with the matrix on the left of (12).
By Section 3 and column convergence, \(D_g(R)\to D_0(R)\), where
\(D_0(R)\) is the explicitly signed permutation on (11).
Subtract \(\delta_*I\) from (12), divide the exact commutator by
\(g^2\), and pass to the limit. The remainder tends to zero in
the finite matrix norm, yielding
\[
                     [\mathsf K,D_0(R)]=0
               \quad\hbox{for every signed permutation }R.
 \tag{14}
\]
This proves invariance of the correction even though the selected
tree chart itself is not invariant. No order-\(g\) chart symmetry
has been omitted: the leading energy matrix is scalar and its
first-order correction is zero, so the limiting commutator is
precisely (14).

## 5. Three retained numbers and all six corrections

In the order \(D_1,D_2,D_3,O_{12},O_{13},O_{23}\), the reflections
(8) fix every \(D_\mu\) and give three distinct nontrivial sign
characters to the three \(O_{\mu\nu}\). Consequently (14) forces
all diagonal/off-diagonal mixing entries and all entries between
different off-diagonal basis vectors to vanish. Coordinate
permutations act transitively on the three diagonal vectors,
on their distinct pairs, and on the three off-diagonal vectors,
with possible signs in the last action. Therefore (14) and
real symmetry of \(\mathsf K\) imply exactly
\[
 \boxed{\mathsf K=
 \begin{pmatrix}
 d&o&o&0&0&0\\
 o&d&o&0&0&0\\
 o&o&d&0&0&0\\
 0&0&0&c&0&0\\
 0&0&0&0&c&0\\
 0&0&0&0&0&c
 \end{pmatrix}.}
 \tag{15}
\]
Here \(d=\mathsf K_{D_1D_1}\), \(o=\mathsf K_{D_1D_2}\),
and \(c=\mathsf K_{O_{12}O_{12}}\) are the full finite sums from
equations (35)--(36), or equivalently (44), of the companion.
The symbol \(c\) in this note is a matrix coefficient, not a
speed-of-light constant.

The vector \((1,1,1,0,0,0)/\sqrt3\) has eigenvalue \(d+2o\).
The two-dimensional subspace
\(\{(x_1,x_2,x_3,0,0,0):x_1+x_2+x_3=0\}\) has eigenvalue \(d-o\).
The three-dimensional off-diagonal subspace has eigenvalue \(c\).
These statements follow by multiplying (15), without invoking
an undeclared representation-theoretic decomposition. Thus
\[
 \boxed{\Delta_L(g,a)={2\sigma_*\over a}
             +g^2\min\{d+2o,\ d-o,\ c\}+O_{L,a}(g^3).}
 \tag{16}
\]
All three entries carry their original factor \(a^{-1}\).
The three numbers still involve all spatial-mode interactions.
Nothing here decides their signs or large-\(L\) asymptotics.
It does reduce the original complete \(L=2\) numerical-certificate
task to three specified entries while proving all other entries
and degeneracies exactly.

The conclusion uses the full symmetric open box and the global
Hamiltonian. Arbitrary local weights \(h\) need not possess these
spatial symmetries; their state coordinates are still projected
against the complete matrix (15), not declared symmetric.

## Dependencies

The included original finite-box source proves the tree/Haar
isometry and complete mode basis. The included cubic singlet,
vacuum-energy and first-gap note proves (12) with its controlled
fixed-box residual and exact all-mode expression for \(\mathsf K\).
This note constructs the original graph symmetries and their
nonlinear-chart and limiting-cluster intertwiners explicitly.
It uses neither a conjectural continuum theory nor an assertion
that different coordinate presentations are unrelated.
