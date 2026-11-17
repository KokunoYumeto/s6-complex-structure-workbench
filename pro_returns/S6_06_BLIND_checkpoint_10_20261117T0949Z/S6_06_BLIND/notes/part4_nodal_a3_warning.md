# Local nodal-critical-curve warning

This is a local calculation, not a counterexample to the global Part 4 theorem.
It prevents a blanket local exclusion of a critical curve with two branches.

Take

\[
 f(x,y,z)=xz^2+x^2y^4=x(z^2+xy^4).
\]

Its gradient is \((z^2+2xy^4,4x^2y^3,2xz)\). Its reduced critical
curve is \(\{z=0,xy=0\}\). Along either punctured axis, the transverse
germ is a tacnode: along the x-axis this follows by extracting the unit
coefficient of \(z^2\); along the y-axis complete the square in x to obtain
a nonzero multiple of a square minus a unit times \(z^4\).

For \(t\ne0\), the affine fibre has \(x\ne0\). The finite étale
double cover and its inverse coordinates are

\[
 x=s^2,\quad U=sz,\quad V=sy,
 \qquad y=V/s,\quad z=U/s.
\]

They identify the cover exactly with
\[
 \{U^2+V^4=t\}\times\mathbb C^*.
\]
Its deck involution is \((s,U,V)\mapsto(-s,-U,-V)\), which acts
freely. The affine curve factor is a punctured elliptic curve, and therefore
has contractible universal cover; the product is aspherical. For any small-ball fibre, its inclusion into this affine fibre sends every
spherical class to zero, because the affine fibre has vanishing second
homotopy group. Self-intersection of a compact class is unchanged by this
open inclusion, so every such spherical class has square zero already
locally. This is the exact open-inclusion comparison used in P4.19; no
claim about a local/global homotopy equivalence is needed. The polynomial
also has positive weights \((4,1,4)\), weighted degree 12, as checked below.

The nonplane branch has the finite birational normalization
\[
 (u,y)\longmapsto(-u^2,y,u y^2).
\]
Its inverse rational parameter is \(u=z/y^2\); its source is smooth.
The intrinsic conductor along \(y=0\) has exponent two. Multiplication
by the equation x of the other branch adds the divisor \(2\{u=0\}\),
so the full conductor on this normalization is
\(2\{y=0\}+2\{u=0\}\). On the plane branch x=0 it is
\(2\{z=0\}\).

Over the two branches of the critical node, the conductor map has one
ramified degree-two part \(u\mapsto x=-u^2\), and two unramified parts
mapping to the other branch. This odd local ramification contribution is
a useful global bookkeeping datum. It is not by itself an existence
construction of a compact fibre or threefold.

The cover identity, normalization equation, weighted Euler identity, and
planar curve-defect examples are executed in `code/part4/conductor_gap.py`.
