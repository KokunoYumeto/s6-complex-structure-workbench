# P3K.16. Proved: the actual Seifert base and its integral sphere restrictions

For the whole-fibre \(I_1\) cusp construction of P3F.9, together
with the actual nonzero-linearization affine caps of P3K.15, the
delta orbit has a global map to a closed Seifert three-manifold
over the original base \(\mathbb P^1\).  Its regular fibres are
connected elliptic tori.  Every sphere member has at most two
nontrivial effective gamma multiplicities.  For two such
multiplicities, write the marked local pairs as
\((m_1,n_1),(m_2,n_2)\), with each pair primitive, and let
\(b\) be the remaining integral gamma clutch.  The exact restriction is
\[
       m_1m_2b+m_2n_1+m_1n_2=\pm1.                 \tag{P3K.16.1}
\]
In particular \(\gcd(m_1,m_2)=1\).  Order-one clutches and the
finite zero-gamma subgroups are retained in the source and line
data; this restriction does not remove them.

**Proof: construction of the map.** On an ordinary source disc,
the delta orbit of the contracting line quotient is the source
mapping torus of P3K.13.  Projection of that source surface to
its disc, together with the suspension coordinate, gives the
map to the disc times the gamma circle.  Straightening the norm
roof is over the source and its base.  On the whole-fibre \(I_1\)
cusp, the actual product of P3F.9 preserves the Seifert gamma
coordinate, so its map is exactly
\[
       E_{I_1}\times S^1_\gamma\longrightarrow
                    \Delta_q\times S^1_\gamma.
\]
This includes the nodal fibre and the circle-fixed sphere.
The specified annular period maps intertwine these projections;
their integral gamma shifts are their recorded Seifert clutches.

Here is the map at an arbitrary supplied cap, including its
finite kernel.  Use the actual maps \(A,B,C,H\) of P3K.15,
and write \(g=\gcd(m,n)\), \(m'=m/g\), \(n'=n/g\).
The root source has coordinate \(z\), with original base
coordinate \(q=z^m\).  The finite map \(C\) has faithful
base character of order \(g\).  Hence the smooth source
quotient \(\bar S=S'/\langle C\rangle\) has base coordinate
\(u=z^g\), and \(q=u^{m'}\).  If
\(rn'+sm'=1\), then \(\bar H\) acts on this base by
\[
                 u\longmapsto e^{2\pi i r/m'}u.
\]
Projecting the actual mapping torus of \(\bar S\) to the
mapping torus of this disc rotation gives the cap map.
The target is a solid torus: the explicit map
\((u,t)\mapsto(e^{2\pi i rt/m'}u,e^{2\pi it})\)
trivializes its disc bundle.  The regular Seifert gamma orbit
has multiplicity \(m'\), and its primitive marked meridian
relation is
\[
                     m'a-n'\gamma=0.             \tag{P3K.16.2}
\]
Indeed these two loops are the actual \(\bar A=\bar H^{n'}\)
and \(\bar B=\bar H^{m'}\) of P3K.15, not an inferred
replacement for their affine lifts.  This transports the stated
outer meridians and glues the target solid torus to the ordinary
target charts.  Doing so at all sites constructs the closed
three-manifold \(B\) and the map \(p:Y\to B\).

Off the finitely many discriminant and cap-core circles, the
map is a smooth proper submersion with connected elliptic
fibres.  Connectedness at a cap can be checked before any
topological conclusion: the \(g\) roots of a nonzero \(u\)
are permuted transitively by \(C\), so their quotient fibre
is one elliptic curve.  The same fact is preserved by the
suspension.  The finite-root and ordinary maps above agree
with the annular source maps, so there is no disconnected
generic-fibre substitution in this construction.

**Proof: fundamental groups and the number of sites.** Every
loop in the smooth three-manifold \(B\) can be moved off the
finite union of discriminant and core circles: perturb its
finitely many smooth arcs transversely to these curves, whose
dimension sum is two, less than three.  Over the resulting
loop, a choice of horizontal complement to the submersion
kernel lifts the loop from a chosen point of its fibre.  The
lift exists for the whole compact interval because the
submersion is proper over that interval.  Its endpoint lies
in the same connected elliptic fibre as its starting point.
Join them by a path in that fibre.  The resulting closed loop
projects to the original loop followed by a constant path.
Thus \(p_*:\pi_1(Y)\to\pi_1(B)\) is surjective.
For a sphere member, P3F.8 gives \(Y=S^5\), so
\(\pi_1(B)=1\).

Remove discs around the nontrivial effective Seifert sites.
The gamma-circle bundle over the remaining punctured sphere
is trivial, since its base retracts onto a graph.  Choose a
section, retain the marked boundary loops \(a_i\), and write
its integer discrepancy from the actual cap framings as \(b\).
Van Kampen applied to the actual meridians (P3K.16.2) gives
\[
 \pi_1(B)=\left\langle a_1,\ldots,a_s,\gamma\ \middle|\
 [a_i,\gamma]=1,\quad a_i^{m_i}=\gamma^{n_i},\quad
                 a_1\cdots a_s\gamma^b=1\right\rangle.
                                                        \tag{P3K.16.3}
\]
Order-one sites can be included in this presentation and
eliminated using their actual relation \(a_i=\gamma^{n_i}\).
Their integers are then added to \(b\); their source and
line lifts are still retained in P3K.15.

Quotient (P3K.16.3) by \(\gamma\).  With at least three
nontrivial multiplicities, further killing all but three
generators maps this quotient onto
\[
       \langle x,y,z\mid x^{m_1}=y^{m_2}=z^{m_3}=xyz=1\rangle.
\]
This group is nontrivial for every \(m_i\ge2\), as the
following explicit real matrix representation proves.  On
\(\mathbb R^3\), take the symmetric bilinear form with matrix
\[
 G=\begin{pmatrix}
 1&-\cos(\pi/m_3)&-\cos(\pi/m_2)\\
 -\cos(\pi/m_3)&1&-\cos(\pi/m_1)\\
 -\cos(\pi/m_2)&-\cos(\pi/m_1)&1
 \end{pmatrix},
\]
and set \(R_i(v)=v-2(v,e_i)_G e_i\).  Direct substitution
gives \(R_i^2=I\).  The span of each pair \(e_i,e_j\)
has positive definite Gram matrix, since its determinant is
\(\sin^2(\pi/m_k)>0\).  It therefore has a one-dimensional
orthogonal complement even when \(G\) itself is degenerate.
On the pair span the two reflections have angle \(\pi/m_k\),
and their product has characteristic polynomial
\(z^2-2\cos(2\pi/m_k)z+1\); on the complement it is
the identity.  Thus \(R_2R_3,R_3R_1,R_1R_2\) have
orders exactly \(m_1,m_2,m_3\), and their product is
exactly the identity by cancellation of adjacent reflections.
Their first member is nonidentity.  This gives the promised
nontrivial representation, contradicting
\(\pi_1(B)=1\).  Thus \(s\le2\).

**Proof: the exact determinant and the marked base.** For two
sites eliminate \(a_2\) from (P3K.16.3).  The remaining
generators \(a_1,\gamma\) commute, and their relation matrix is
\[
 \begin{pmatrix}
      m_1&-n_1\\
      -m_2&-m_2b-n_2
 \end{pmatrix}.
                                                        \tag{P3K.16.4}
\]
Triviality of the group is therefore exactly (P3K.16.1).
Any common divisor of \(m_1,m_2\) divides its left-hand
side, which proves their coprimality.  With one exceptional
site the same calculation is \(|m_1b+n_1|=1\); with none
it is \(|b|=1\).  Equivalently one may insert multiplicity-one
solid tori and use the displayed two-site matrix in all cases.

The resulting target is the actual marked Hopf three-sphere,
with both signs retained.  Here is an explicit Heegaard
comparison, rather than an appeal to a classification by
fundamental group.  In the middle torus with basis
\((a_1,\gamma)\), its two meridians are
\[
 \mu_1=(m_1,-n_1),\qquad
 \mu_2=(-m_2,-m_2b-n_2).
\]
Put \(\delta=\det(\mu_1,\mu_2)=\pm1\).
The integer matrix with columns \(\mu_1,\delta\mu_2\)
has determinant one and sends these meridians to the two
coordinate meridians after inversion.  This torus map
extends across each solid torus, because in meridian-longitude
coordinates every required boundary shear extends by
\[
 (\rho e^{i\theta},e^{i\varphi})\longmapsto
 (\rho e^{i(\varepsilon\theta+k\varphi)},
                         e^{i\varepsilon'\varphi}),
 \qquad \varepsilon,\varepsilon'\in\{\pm1\}.
\]
The two target solid tori are the standard decomposition of
\(S^3\subset\mathbb C^2\).  In these coordinates the
original gamma vector is exactly \((\delta m_2,m_1)\).
Consequently its signed weighted Hopf action and its two
exceptional orders have both been transported explicitly.

Finally the replacement \(a_i\mapsto a_i\gamma^{k_i}\)
changes the integer records by
\[
         n_i\mapsto n_i+m_i k_i,\qquad
         b\mapsto b-\sum_i k_i.
\]
This is also an identity of actual cap quotients: replace
\(A_i\) by \(A_iB_i^{k_i}\), which generates the same
group with \(B_i\).  Its cyclic norm changes by
\(m_i k_i\gamma\); its finite kernel \(C_i\) is unchanged.
Thus residue representatives for \(n_i\) can be chosen
without deleting the recorded finite kernel, delta character,
or source-line map.  The determinant is invariant under
exactly these transformations.
**End of proof.**

The scope of this reduction is the actual whole-fibre cusp
projection specified at the start.  It does not extend the old
gamma coordinate through the component-supported OS49 cusp;
that construction uses its separate mixed \(K\) marking.
The Seifert projection also does not recover the finite-kernel
source quotient or the line character from \(B\) alone.
Those data remain part of every cap in the enumeration.

An arbitrary periodic unimodular fan need not have this fixed-sphere
model.  The present map and its use of P3F.8 are not asserted for
such a fan without its separate orbit comparison.
