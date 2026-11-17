# The individual rotating integers for the ten primitive-source families

Working proof submitted for root audit; the manuscript remains frozen.

For the K22 family with \(M=\mathcal O(dG-O)\), \(Q=G\),
retain the actual one-site cap-to-ordinary gluing and positive
scalar loop. In the transported rotating normal framing of
P3K.9, its integers are
\[
                         k=-3d,\qquad \ell=-24.
\]
Thus the four denominator groups \(d=8,14,20,30\) give
\[
\begin{array}{c|r|r|r}
d&k&\ell&A=(4k-\ell)/24\\ \hline
8&-24&-24&-3\\
14&-42&-24&-6\\
20&-60&-24&-9\\
30&-90&-24&-14.
\end{array}
\]
The statement specifies this actual framing; it does not identify
it with another uncomputed Cox or gauge normalization.

## The actual frame comparison

P3K.22 identifies the page as the original rational elliptic
source minus a regular fibre, with its original line \(M\).
The page boundary has binding degree one along the positive
inward gamma circle. The actual K6 graph boundary is
\(\gamma=\theta+g_\epsilon(p)\), where \(p\in T^2\) and
\(\theta\) is the positive physical scalar-parameter direction.
The cap-to-ordinary arrow and the two extending origins in K22.3
give exactly this positive direction; no parameter cover is used.

Use the graph normal consisting of its oriented normal in the
orbit \(Y\) and the two Cartesian parameter directions.
Use on the compression the actual rank-three normal frame
transported by \(R_\theta\). The compression is the same solid
torus minus a ball as in K6. Its normal bundle has \(w_2=0\):
its tangent bundle is trivial, and \(TY\oplus\mathbb R\) is
trivial for the actual orbit \(Y=S^5\). Obstruction theory on
this three-dimensional compression gives a normal framing.
Its restriction at the fixed-sphere end differs from the
positive-Hopf frame by a map \(S^2\to SO(3)\), which extends
over the fixed \(D^3\). Transport that extension by the same
\(R_\theta\). This defines the rotating compression-cap
framing, including its fixed-sphere attachment.

Let \(\phi\) be the fixed outward page-collar phase in radians.
The actual degree-one binding gives
\[
                  \alpha=\phi-\gamma
                         =\phi-\theta-g_\epsilon(p).
\]
The four-dimensional quotient used to compare the graph and
compression normals has the actual collar tangent
\[
             u=(\cos\alpha,\sin\alpha,\rho,0),
             \qquad \rho>0.
\]
Its quotient map is
\[
 (v_q,v_r,v_\eta)\longmapsto
       \bigl(v_q-\rho^{-1}v_r(\cos\alpha,\sin\alpha),v_\eta\bigr).
\]
It kills \(u\). Project the Cartesian parameter vectors
with radial-angular coefficients
\((\cos\theta,-\sin\theta)\), \((\sin\theta,\cos\theta)\),
reverse both of these vectors, and apply the positive
rescalings of K9. The resulting actual graph normal matrix is
\[
 G(\alpha,\theta)=
 \begin{pmatrix}
 -\sin\alpha&\cos\theta\cos\alpha&\sin\theta\cos\alpha\\
 \cos\alpha&\cos\theta\sin\alpha&\sin\theta\sin\alpha\\
 0&\sin\theta&-\cos\theta
 \end{pmatrix}\in SO(3).
\]
Source derivatives of \(g_\epsilon\) are removed by the
explicit triangular shear before taking this quotient.
The outward-page and inward-compression tangent remain
in the same positive radial half-space during the actual
rounding; that half-space is contractible.

Write the compression frame in the same transported product
coordinates as \(h(p)\). It is independent of \(\theta\).
The full clutch is therefore homotopic, through these actual
invertible quotient maps and collar homotopies, to
\[
\begin{aligned}
 h(p)^{-1}G(\phi-\theta-g_\epsilon(p),\theta)
   &=[h(p)^{-1}R_z(-g_\epsilon(p))]\\
   &\quad\cdot[R_z(\phi-\theta)G(0,\theta)].
\end{aligned}
\]
The first factor is pulled back from \(T^2\), and the second
from \(S^1_\theta\). The cubic Maurer--Cartan form of their
product differs from the sum of the two cubic forms by an
exact form, by direct expansion of
\((ab)^{-1}d(ab)=b^{-1}a^{-1}(da)b+b^{-1}db\).
Both factor cubic forms vanish by dimension. Integrating
the collar Chern--Weil transgression over the marked \(T^3\)
therefore proves
\[
                     \int_{\bar X}p_1(\bar\nu)=0.
\]
This retains all one-dimensional frame classes and does not
replace the actual normal bundle with a trivial bundle.

## Characteristic numbers in this framing

The K22 graph-to-line comparison gives
\(b^2=4M_{\mathrm{rel}}^2=-4d\).
The marked regular-cap comparison gives
\(\int p_1(T\bar X)=-24\), since the capped source is the
rational elliptic surface. The signed meridian calculation
of K7 has \(\pi_*x=1\) for this actual positive inward
gamma turn. Its exact sphere-bundle identities give
\[
 k=\frac{\int p_1(\bar\nu)+3\int b^2}{4}=-3d,
 \qquad
 \ell=\int p_1(T\bar X)+\int p_1(\bar\nu)=-24.
\]
Consequently \(A=1-d/2\), in agreement with the independent
K22 page calculation. There is no descent step here because
the scalar loop is already one positive gamma turn.

Changing the tubular framing by its free gauge integer \(n\)
changes the pair by \((n,4n)\), as in P3F.11. The auxiliary
source-root line-gauge winding \(+2\) does not determine that
normal-frame gauge integer. In particular it was not used
to infer \(k\).

The exact quotient, orthogonality, rotation-factorization,
and arithmetic are executed in
code/part3_fourfold/primitive_normal_clutch.py.
