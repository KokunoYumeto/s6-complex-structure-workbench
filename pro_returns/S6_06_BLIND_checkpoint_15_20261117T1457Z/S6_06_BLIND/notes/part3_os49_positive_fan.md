# P3F.31. The OS49 positive-diagonal filling and its actual page

**Proved.** This statement concerns the positive-diagonal filling
defined below. It leaves the negative-diagonal family of P3F.26 intact.
The two fans have the common torus family and are related by the
specified toric flop; they are not identified as the same family.

This positive-diagonal filling gives an actual sphere family over
\(\lambda=r^3\), with zero positive-loop return index. The actual
page, circle-line comparison, boundary support, and cap marking
are constructed below. Root and fourfold independently audited
these maps and the relative cohomology argument before this
statement was marked proved.

## 1. The exact line subfan

Keep the periods \(h=(2,1)\), \(g=(-3,-1)\) of P3F.26 and use
the periodic triangulation whose two triangles in a unit square are
\[
 (0,0),(1,0),(1,1),\qquad (0,0),(0,1),(1,1).          \tag{P3F.31.1}
\]
All cones at height one are unimodular, and the full period lattice
has index one. The compact fundamental domains of P3F.26 prove
smoothness, compactness and properness of this actual new filling.
The finite cap and the type-II line-complement quotient are unchanged.
Its integral topology can be compared by actual morphisms. Put
\(u_j\) for the height-one rays over the four corners of a unit
square. The common refinement adds the ray
\[
 v=u_1+u_2=u_0+u_4=(1,1,2).
\]
It is the blowup of the diagonal \(\mathbb P^1\) in either
small resolution. The normal bundle of each centre is
\(\mathcal O(-1)^{\oplus2}\), and the exceptional divisor is
\(\mathbb P^1\times\mathbb P^1\), with the two morphisms
contracting its two rulings. The equivariant period identifications
give these global morphisms on the two compact fillings; there is
one orbit of diagonal curves.

For this blowup, integral cohomology is the direct sum of pullback
cohomology and the Gysin image of \(H^{q-2}(\mathbb P^1;\mathbb Z)\).
One can verify the splitting by the long exact sequence of the
complement of the centre and the Thom isomorphism; integration
on the exceptional ruling, whose exceptional-divisor degree is
\(-1\), proves that the added generator is primitive. Thus the
only additional groups are one free generator in degrees two and
four. Van Kampen preserves the fundamental group: both local
pieces and their sphere-bundle boundary are simply connected.
Apply these facts to the two morphisms from the same refinement.
Since the negative-diagonal filling of P3F.26 is a simply connected
integral homology sphere, so is this positive-diagonal filling.
It is therefore the standard smooth six-sphere. This comparison
does not identify the two families' return maps.

Here is the additional property needed for the page. On the infinite
Tate chain of the source \(I_2\), put
\[
 h_j=\lceil j/2\rceil,
 \qquad h_{j+2}=h_j+1.
\]
The fan of the actual line complement \(M^\times\) has rays
\((j,h_j,1)\) and cones on consecutive pairs of these rays.
Projection to \((j,1)\) is the source Tate-chain projection. On
each such cone the total space is \(\mathbb C^2\times\mathbb C^*\);
the last factor is the delta circle's complexification. The line
degree on component \(j\) is
\[
 -(h_{j-1}+h_{j+1}-2h_j).
\]
The minus sign follows directly from fibre-coordinate transitions:
if the two adjacent slopes are \(s_-,s_+\), the fibre coordinates
on the two component charts differ by \(Z^{s_--s_+}\), which is
the inverse of the line-frame transition. The degrees are therefore
\((-1,+1)\), exactly those of \(M=\mathcal O(G-O)\).
The edges are alternately \((1,1)\) and \((1,0)\), so this is a
literal subfan of (P3F.31.1). Its quotient by \(h\) is the actual
\(M^\times\) over the whole source \(I_2\) neighbourhood,
including both nodes. This identifies its map into the filling by
toric charts, not merely by a boundary lattice.

It also checks the direction of the lift. Under \(g\), the graph
height defect is
\[
 h_j-1-h_{j-3}=0\quad(j\text{ even}),\qquad
 h_j-1-h_{j-3}=1\quad(j\text{ odd}).
\]
Thus the lift is invertible over source \(C_0\) and acquires its
simple zero over source \(C_1\), which is sent to target \(C_0\).
This is precisely the target-point linearization
\(\phi:T^*M\to M\) of P3F.28. Holomorphic units are retained
in the line frames and in both periods; they do not change any of
these chart inclusions.

For comparison, the negative-diagonal fan of P3F.26 has horizontal,
vertical, and negative-diagonal edges, and does not contain this
positive-diagonal line subfan. Flipping the diagonal of each unit
square gives the actual toric birational comparison, through the
common refinement. No diffeomorphism or equality of return indices
is concluded from that comparison here.

## 2. A page carrying the actual source line

Choose a Hermitian norm on the source line which, on the regular
annulus bounding the cusp neighbourhood, is unitary flat on every
elliptic fibre. Such fibrewise metrics vary smoothly on that annulus;
interpolate their logarithms to any smooth metric on a smaller
neighbourhood of the central fibre. No flat extension across the
nonzero component degrees is imposed. The lift covering
\(-Q\), before the zero is removed, is a global holomorphic line
map on the compact source. Its operator norm is bounded. After
choosing \(|\lambda|\) sufficiently small, it decreases every
nonzero norm on its domain by a factor bounded above by a constant
\(c<1\). On a source cusp neighbourhood choose three radii
\(R_1<R_2<R_3\) with \(cR_3<R_1\). The three norm shells
\(\|v\|=R_j\) map to the filling through the actual line subfan.
No nonzero iterate of the contracting lift identifies two points
of those shells: every forward iterate that stays in the line
complement has norm at most \(cR_3\), and the inverse case is
the same assertion reversed. A zero cannot leave this open subset
and re-enter it through a later toric translate. Indeed the exact
height defect of \(g^N\), for \(N>0\), is
\[
 h_j-N-h_{j-3N}=
 \begin{cases}\lfloor N/2\rfloor&j\text{ even},\\
 \lceil N/2\rceil&j\text{ odd}.
 \end{cases}
\]
It is positive after the first zero; the same cone calculation
at a source node uses both endpoint defects. Thus no later
positive translate is a point of the line-complement subfan.
The period \(h\) has already been divided out in the
source line bundle. The resulting maps are therefore injective
immersions. On a compact closed cusp neighbourhood the shells
are compact, so these maps are embeddings.

Their delta quotients are three embedded copies of the actual
source \(I_2\) neighbourhood. Each misses the fixed sphere,
because the delta action on \(M^\times\) is free and the toric
open subset just specified misses the vertical fixed edge. On
each copy the actual delta bundle is exactly the chosen unit
circle bundle of \(M\), by the displayed map. This gives the
line identification through both nodes and both components.

Away from the cusp use the marked regular-binding page of the
affine circle quotient. The order-three finite cap has gamma
displacement \(1/3\); the corresponding circle base is the
weighted Hopf three-sphere of weights \((1,3)\). Its regular
binding page projects with degree three to the elliptic base,
branched at the order-three value and at the regular binding.
The type-II neighbourhood uses the original line-complement
quotient, so its source surface is retained. On the cubic root
of \(IV^*\), the source has the already verified smooth good
reduction. These are the same explicit root-chart and affine
translations as in P3F.26.

On this regular annulus the norm multiplier \(c(q)\) of the
lift is constant on each elliptic fibre. Indeed translation
pulls its unitary flat metric to another flat metric, and the
logarithm of the norm ratio of the holomorphic line isomorphism
is harmonic on the compact elliptic fibre, hence constant.
Consequently \(\log\|v\|/\log c(q)\pmod1\) is the actual
real suspension height, with the marked gamma cycle. The norm
shells can be interpolated to levels \(\|v\|=c(q)^{a_j}\),
where the three distinct \(a_j\) have the prescribed cyclic
order. Choose them in a sufficiently small interval that all
shell-separation inequalities remain strict on this compact
annulus. An orientation-preserving reparametrization of the
suspension circle then carries these levels to the three
regular-binding page levels. This reparametrization is over the
unchanged source and base coordinates, so it is a graph isotopy
of the actual suspension charts. There is an exact lift: put
\(t=\log\|v\|/\log c(q)\), lift the circle reparametrization to
\(F_q:\mathbb R\to\mathbb R\) with
\(F_q(t+1)=F_q(t)+1\), and send
\[
 v\longmapsto c(q)^{F_q(t)-t}v.
\]
Its multiplier is positive and one-periodic in \(t\). It commutes
with the contracting lift, keeps the source and base coordinates
fixed, and is delta-equivariant. Thus it carries the actual circle
line, including its gluing. Keep the inner norm shells and the outer page fixed
during the interpolation. This glues the three source cusp
neighbourhoods to the outside page with the stated boundary maps.

This constructs an embedded four-dimensional page \(V\subset Y\)
which misses the fixed sphere and has the original marked binding
\(T^3\). Its projection to the degree-three base page is still
the source elliptic fibration: the annular interpolation is over
the unchanged base coordinate. Its compact regular-fibre cap
has three \(II\) and three \(I_2\) fibres. The actual delta
line on \(V\) is the pullback section line \(M\), up to a base
line. To see the last assertion without discarding component
data, the comparison is the exact norm-shell map at each \(I_2\),
the original quotient map at each \(II\), and the good-reduction
root map at the finite cap. On the smooth pieces normalize the
fibrewise line isomorphism at the zero section; its overlap ratios
are base functions. The base page has boundary, so its line is
topologically trivial. The affine torsor origins can be chosen
over this base because its punctured-cell model is a graph and
the obstruction has no degree-two cochains.

## 3. The full graph-to-page comparison by regular bands

Use the relative cusp product with primitive source cycles \((H,w)\)
and angular cycle \(K\). Its fixed-edge charts again have the
opposite normal weights and bundle \(\mathcal O(-1)^{\oplus2}\).
In detail, the two positive-fan charts along a vertical edge have
coordinates
\[
 (A,B,Z)=(q/V,V/Z,Z),\qquad
 (A',B',Z')=(qZ/V,V,1/Z),
\]
with \((A',B')=(ZA,ZB)\), and delta weights \((-1,+1,0)\).
For the opposite small resolution the orbit-product calculation
of P3F.9 is obtained by exchanging the two moving conifold
coordinates. Both local orbit coordinates change sign, so their
transition derivative stays positive. The same relative
line-coordinate construction therefore supplies the product over
the unchanged nodal elliptic factor, with boundary marking
\((H,w,K)\).
The exact real handle of P3K.6 gives a compression \(W\) from a
regular \((H,w)\)-torus at \(q=\epsilon\) to the fixed sphere,
whose projection lies over the real segment \([0,\epsilon]\).
Choose the regular binding at \(q=\epsilon\), outside the region
where the cusp page was modified above. The K-rotation of this
compression gives the same actual trace as the angular clutch
\(\theta K+3\theta(\theta-1)\delta\) of P3F.27.

The incoming map \(E'_\epsilon\times S^1_K\to T^3\) is the
actual diffeomorphism with the unimodular boundary marking
\(u=2H+K\), \(\gamma=-3H-K\). On the page boundary its inverse
angle is \(b-g_\epsilon(p)\), where \(g_\epsilon\) is the
real-valued incoming graph of the compression. Multiplying the
corresponding circle-valued function by a radial cutoff gives a
map from \(V\) to the inner parameter disc. The graph of that
map is embedded, and attaches to the rotating compression exactly
as in P3K.6. This gives the actual trace four-manifold \(X\).

The page need not miss the entire projected compression. The
following argument controls every remaining intersection. At
\(q=0\) the compression is the fixed sphere, and the constructed
page is disjoint from it. Compactness therefore gives \(q_a>0\)
such that their intersection has no point over \([0,q_a]\).
All remaining base values lie in \([q_a,\epsilon]\) and are
regular values of the source elliptic fibration. The three lifts
of this interval to the base page are disjoint regular bands
ending on its boundary.

Here is the boundary check for a normal pushoff, which is needed
because the incoming torus meets the whole binding. Near the
unchanged binding write the page collar as
\[
 q-\epsilon=\rho e^{i\alpha(\gamma)},\qquad \rho\geq0,
\]
where \(\alpha\) winds three times. Choose its normal pushoff
inside these unchanged base-coordinate annular and binding charts,
with base coordinate
\[
 q-\epsilon=(\rho+i\eta)e^{i\alpha(\gamma)},
 \qquad\eta>0.
\]
Intersection with the real compression requires
\(\rho=-\eta\cot\alpha\geq0\) and
\(q-\epsilon=-\eta/\sin\alpha\leq0\). Thus it is confined
to the three closed boundary arcs where
\(\pi/2\leq\alpha\leq\pi\). They are proper arcs of the
boundary circle. Enlarge the three lifted regular bands to contain
slightly larger arcs than the actual finite-collar intersections;
\(\alpha=\pi\) is only a limiting endpoint of the displayed
formula, and the three enlarged arcs still have disjoint gaps.
Each enlarged band is a half-disc attached to the
boundary, and it still contains no critical source value. The
pushoff can be taken small enough that the remainder of the page
misses the entire projected compression. More explicitly, on the
complement of the three bands the original page and the compact
projected compression are disjoint; retain a positive separation
there and make the pushoff smaller than this separation. Near the
binding the displayed formula gives the required separation
outside the three proper arcs. The radial homotopy keeps this
pushoff's \(Y\)-coordinate fixed, so its only possible
outer-annulus intersection is with the unrotated compression at
parameter angle zero. All such points lie in the three bands.
This gives actual neighbourhoods
\[
 U_i\cong T^2\times D_i,
 \qquad U_i\cap\overline{V\setminus U_i}
       \cong T^2\times A_i,
\]
where \(D_i\) is a half-disc and \(A_i\) its inner semicircle.

Let \(x\) be the unique meridian-one class on the complement of
the embedded trace in \(Y\times D^2\), as in P3K.6. Pull it back
by the framed graph-normal section. Outside the displayed bands
the exact radial homotopy of P3K.6 reaches the original parameter-zero
page pushoff without meeting the trace. Hence this pullback equals
the actual page-line Chern class there. But
\[
 H^2(T^2\times D_i,T^2\times A_i;\mathbb Z)=0,
\]
because \(A_i\hookrightarrow D_i\) is a homotopy equivalence.
Excision and the relative long exact sequence therefore make
restriction to the complement of all these bands injective in
degree two. The two line classes agree on the whole page. Possible
differences of relative lifts are boundary gauges; their squares
and their products with the page line vanish because its boundary
Chern class is zero. This proves the actual graph-normal line
comparison, including the boundary restriction.

## 4. Characteristic calculation and the scope of the result

The compact elliptic page has \(\chi=1\), signature \(-8\),
and \(G\cdot O=0\). Consequently its section line has relative
square \(-2\), and the relative Pontryagin pairing is \(-24\).
Cap the trace as in P3K.7. The different incoming torus marking is
retained: the compression cap kills the primitive vanishing cycle
\(w\), while the regular elliptic cap kills the old gamma cycle.
The exact change of the remaining two cycles is
\[
 \begin{pmatrix}u&\gamma\end{pmatrix}
 =\begin{pmatrix}H&K\end{pmatrix}
   \begin{pmatrix}2&-3\\1&-1\end{pmatrix},
 \qquad\det\begin{pmatrix}2&-3\\1&-1\end{pmatrix}=1.
\]
It extends as a diffeomorphism of the two-torus factor of the
compression cap. With the original marked boundary the two caps
are exactly
\[
 H_w=D^2_w\times S^1_u\times S^1_\gamma,\qquad
 H_\gamma=S^1_w\times S^1_u\times D^2_\gamma.
\]
Their closed difference is \(S^1_u\times S^3\), by the two
solid-torus decomposition in the \((w,\gamma)\) coordinates.
In particular both caps have signature zero. The restriction
\(H^2(H_w;\mathbb Z)\to H^2(T^3;\mathbb Z)\) is injective,
so the zero boundary Chern class forces the cap line class to be
zero. A change of its gluing to the page is the image of a boundary
gauge; its square and product with the page line vanish by the
relative cup-product formula of P3K.5. Novikov additivity and the
signature theorem compute the Pontryagin pairing while retaining
both cap markings. The exact graph-normal comparison above
therefore gives
\[
 b^2=4(-2)=-8,\qquad p_1(T\bar X)=-24.
\]
The sphere-bundle calculation of P3K.7, with both return-orientation
reversals retained, gives
\[
 A=\frac{3b^2-p_1(T\bar X)}{24}=0.
\]
The positive \(r\)-loop has the actual K-clutch of P3F.27 for
this fan as well: its integer fan translations preserve
(P3F.31.1), and its bounded origin extends in these charts.
P3F.22 consequently gives zero class in \(\Theta_7\), and
P3F.24 gives the product mapping torus.

This calculation constructs the explicit positive-diagonal family.
P3K.17 subsequently proves that the negative-diagonal family in
P3F.26 has the same actual return, by its charged Cox bordism
including the extra fixed-locus sphere-bundle boundary. The supplied E26
Mumford proposition permits arbitrary periodic unimodular
triangulations and does not select one of these diagonals. Its
literal Remark8.5 requires a whole-fibre divisor, so bare OS49
with component divisor \(C_0\) is the additional configuration
separately requested by the prompt, rather than an instance of that
particular hypothesis.
