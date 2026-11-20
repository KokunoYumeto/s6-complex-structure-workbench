# Exact degree-six polyhedral computation and the remaining comparison gate

This supplement supersedes the **degree-six paragraph** proposed in `receiving_guards_08.json`. It does not supersede the independently checked S-locator correction or plus-convention correction. The earlier frozen text and guard files are retained as historical records.

## 1. Exact orientation adapter

Orient the original torus by `e_1 wedge ... wedge e_6`. For a five-vector `z` define its Poincare-dual covector by

\[
J(z)(u)=\operatorname{vol}(u\wedge z).
\]

The cooriented coordinate five-torus `H_i={x_i=0}` has exterior class

\[
[H_i]=(-1)^{i-1}e_1\wedge\cdots\widehat{e_i}\cdots\wedge e_6.
\]

In the usual increasing lexicographic exterior basis, the exact adapter is

\[
J=\begin{pmatrix}
0&0&0&0&0&1\\
0&0&0&0&-1&0\\
0&0&0&1&0&0\\
0&0&-1&0&0&0\\
0&1&0&0&0&0\\
-1&0&0&0&0&0
\end{pmatrix},\qquad J^{-1}=-J,\qquad\det J=1.
\]

For each actual monodromy `M_i`, whose determinant is one,

\[
J\bigwedge^5M_i=M_i^{-t}J.
\tag{1.1}
\]

In particular `1^t J=(-1,1,-1,1,-1,1)`. Thus the row in the increasing exterior basis is alternating, rather than the all-one row.

## 2. The integral filling and its exact volume

For a primitive integral covector `l`, let `H_l` be the oriented codimension-one subtorus `l(x)=0 mod 1`, cooriented by `l`. Subdivide the fundamental cube `[0,1]^6` by the finitely many hyperplanes `l(x)=m`, `m in Z`. Give each resulting six-dimensional polyhedron the integer coefficient `floor(l(x))` on its interior. Its projection to the torus is a finite integral polyhedral chain `D_l`.

On each internal cut the jump in the coefficient is one; on opposite cube faces the coefficient difference is `l_i`. With the preceding coorientations this gives the exact boundary identity

\[
\partial D_l=\sum_i l_i H_i-H_l.
\tag{2.1}
\]

Let `omega=dx_1 wedge ... wedge dx_6`. Its integral on this chain is

\[
\int_{D_l}\omega=\frac{\sum_i l_i-1}{2}.
\tag{2.2}
\]

Indeed the mean of `l(x)` on the cube is `sum l_i/2`, and the fractional part has mean `1/2`: integrating in any coordinate with nonzero `l_i` traverses an integral number of complete periods. Both the integer-chain identity and this rational value include negative coordinates of `l`.

Write `C(c)=sum_i c_i H_i` for a column of cooriented coordinates. For an orientation-preserving torus automorphism `M`, define

\[
D_M(c)=\sum_i c_i D_{M^{-t}e_i}.
\]

Equations (2.1)--(2.2) give

\[
\partial D_M(c)=C(M^{-t}c)-M_*C(c),
\qquad
\int_{D_M(c)}\omega=\tfrac12\mathbf1^t(M^{-t}-I)c.
\tag{2.3}
\]

An actual geometric edge prism `P_M(c)` has boundary `M_*C(c)-C(c)` in the graph's vertex torus. Therefore

\[
P_M(c)+D_M(c)
\tag{2.4}
\]

has exactly the boundary `C((M^{-t}-I)c)` specified by the minimal graph differential. The prism has zero fibre-volume integral; the filling contributes precisely (2.3). These are explicit integral chains, despite the rational half-integral values of their volumes.

This construction specifies a degree-six map from the **polyhedral realization** of the minimal graph complex to actual chains of the graph bundle. It is identity on the fibre top class and on the quotient edge coordinates. The graph Wang exact sequence therefore identifies the corresponding degree-six homology groups. This statement alone does not identify every marked attaching map of the finite-cap diagram.

## 3. Cancellation for the actual inverse word

Let `X` be the three columns in the original lattice representing

\[
x_j=a_1\wedge a_2\wedge a_3\wedge
b_1\wedge\cdots\widehat{b_j}\cdots\wedge b_3.
\]

With the actual integral `S` from P1.1,

\[
X=(\bigwedge^5S)[e_3,e_2,e_1]
\]

in one-based increasing exterior coordinates. It satisfies `(W_{0,5}-I)X=0`. The exact inverse-word columns are

\[
X_1=-W_{2,5}W_{0,5}X,\qquad
X_2=-W_{0,5}X.
\]

The displayed monodromy word gives

\[
(W_{1,5}-I)X_1+(W_{2,5}-I)X_2
=(W_{0,5}-I)X=0.
\tag{3.1}
\]

Using the actual orientation adapter, the sum of the two polyhedral volume terms is consequently

\[
\frac12\mathbf1^tJ(W_{1,5}-I)X_1
+\frac12\mathbf1^tJ(W_{2,5}-I)X_2=0.
\tag{3.2}
\]

The program `polyhedral_volume_check.py` verifies (1.1), the literal columns `X,X_1,X_2`, both boundary terms in (3.1), and both volume terms in (3.2) using the raw matrices from the frozen fresh reconstruction. Its JSON contains all these matrices.

The geometric invariant-subtorus mapping tori also have zero volume: their transported fibre tangent support has dimension five, and their final closing chain can be taken within the invariant five-torus. Their edge coordinates agree with `X_1,X_2`. Thus their difference from the polyhedral lifts lies in the integral fibre summand of the graph Wang sequence. Volume takes value one on its generator and zero on the difference, so this difference is zero. This proves the comparison with the specifically constructed polyhedral model.

## 4. The finite norms and the genuine outstanding gate

For each finite monodromy and its actual order `m_i`, the volume row

\[
\eta_i=\tfrac12\mathbf1^tJ(W_{i,5}-I)
\]

annihilates the norm matrix:

\[
\eta_i\sum_{j=0}^{m_i-1}W_{i,5}^j
=\tfrac12\mathbf1^tJ(W_{i,5}^{m_i}-I)=0.
\tag{4.1}
\]

This identity is checked exactly. It handles the linear norm columns, but it does not by itself identify the actual affine finite meridian or the entire boundary-to-cap chain map.

The remaining obligation is an **integral comparison of diagrams** from this polyhedral prism/filling realization to the exact minimal graph/Wang model used with the finite-cap maps (1.12.5), including its based affine meridian. The comparison must give actual source and target chain maps and their inverses or chain homotopies, and must show how `j_Y` transforms. The rows `eta_i` can have half-integral entries on arbitrary chains; they are not, by themselves, integral chain automorphisms. Matching the norm columns or cancelling their volumes cannot supply the missing integral adapter.

The earlier statement that relative cellular approximation by itself preserves the prescribed graph Wang representative was too strong: a common subdivision and its reduction to the specified minimal model can carry a six-dimensional comparison term. Equations (2.1)--(3.2) now compute that term for an explicit model. They do not yet prove that this model is the same marked diagram used by every literal finite-cap map in the receiving arrays.

Accordingly, the algebraic chain isomorphism between the fresh and receiving saved arrays remains valid, as do all 140 checks and the local odd secondary-class calculation. The full **geometric-to-literal-global-diagram** gate remains open at this specific compatibility step. The previous high whole-row closure proposal is superseded by this narrower assessment. No finished replacement paragraph claiming that this last gate has closed is supplied.
