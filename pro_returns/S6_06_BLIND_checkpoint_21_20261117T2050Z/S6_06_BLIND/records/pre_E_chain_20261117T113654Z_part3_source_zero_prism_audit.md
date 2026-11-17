# Independent audit of the three source-zero prism fans

This is a separate working audit of the explicit local cone collections
in `notes/part3_source_zero_prism_working.md`. It does not promote a
global K39 filling or assign a source-loop return. The calculation uses
only the current explicit matrices, rays, and staircase tetrahedra.

The degree/support argument passes. In addition, the noncollapsed
cones, together with all their faces, already form a fan in each of
the three sectors. The collapsed cones in either rank-one sector are
existing faces of the noncollapsed cones. A periodic common refinement
of the three H-boundary fans, with compatible rational integral-sector
refinements, is constructed below. The unit action, quotient properness,
and analytic cap attachment remain separate steps.

## PF.1. Exact domain, slice map, and the degree argument

Keep the actual integer pairs \((a,b)=(1,2),(2,1)\), the integer
\(N>1\), and
\[
 I=\begin{pmatrix}1&0\\0&1\end{pmatrix},\quad
 W=\begin{pmatrix}1&b\\-a&-2\end{pmatrix},\quad
 E=\begin{pmatrix}0&0\\0&N\end{pmatrix},\quad
 H=\begin{pmatrix}2&b\\-a&N-1\end{pmatrix}.
\]
For each pair \((P_0,H)\), the original rays and action are
\[
 R_0(n)=(P_0n,1,0),\quad R_1(n)=(Hn,0,1),\quad
 T_m(x,r,s)=(x+rP_0m+sHm,r,s).                         \tag{PF.1}
\]
All geometric inspection changes below leave these integral vectors
unchanged; they are explicitly rational linear maps used to inspect
their cones.

Start with the same staircase cones for \(P_0=P_1=I\). On
\(r+s=1\) they are exactly the standard triangulation of
\(\mathbb R^2\times[0,1]\). The two unit-square triangles
have ordered vertices \((0,u,u+v)\), \((0,v,u+v)\), and
the three tetrahedra on each are those in the root note. The common
diagonal of every vertical rectangle agrees on adjacent prisms, so
this is a face-to-face domain triangulation.

Linearly map its vertices to (PF.1). At height \(s=t\), the
map is \(F_t\), with literal periodicity
\[
 F_t(x+m)=F_t(x)+P(t)m,\qquad P(t)=(1-t)P_0+tH.          \tag{PF.2}
\]
Its difference from \(P(t)x\) is periodic and bounded. The
three determinants, at arbitrary positive \(r,s\), are
\[
 \begin{array}{ll}
 P_0=I:&r^2+(N+1)rs+2Ns^2,\\
 P_0=W:&(N-1)rs+2Ns^2,\\
 P_0=E:&2Nrs+2Ns^2.
 \end{array}                                             \tag{PF.3}
\]
They are positive. Hence (PF.2) descends to the stated two-torus
map and the straight-line periodic homotopy gives degree one.
On every noncollapsed slice piece its Jacobian is the signed
four-dimensional determinant ratio. These are exactly
\[
 \begin{array}{c|cc}
  & (0,u,u+v)&(0,v,u+v)\\ \hline
 (I,H)&(1,N-1,2N)&(1,2,2N)\\
 (W,H)&(0,N-1,2N)&(0,0,2N)\\
 (E,H)&(0,0,2N)&(0,2N,2N).
 \end{array}                                             \tag{PF.4}
\]
Here each determinant is divided by the determinant of the same
domain cone, so its orientation sign is fixed rather than inferred
from an absolute determinant.

Outside the finite polygonal images of lower-dimensional and collapsed
pieces on the quotient torus, every preimage lies in a noncollapsed
piece and has positive local degree. Degree one therefore gives one
preimage. It follows that distinct noncollapsed image interiors do
not overlap. Their closures cover each slice: their finite union on
the quotient is closed and contains the dense set of these regular
values. Lifting and using the bounded periodic difference proves full
support in the whole plane. This verifies exactly the root note's
degree/support statement. It does not claim raw injectivity in a
rank-one sector.

## PF.2. The I,H sector has exact common faces

Every entry in its determinant row is strictly positive. Triangulate
the slice parallelograms by a diagonal, without changing their affine
maps. In the resulting planar triangulation, an edge cannot fold:
the two positively oriented adjacent triangles map to opposite sides
of its image. At a vertex, the images of successive positively
oriented sectors turn through strictly positive angles less than
\(\pi\). Their closed link has positive integral winding, so
the local degree is a positive integer. The same is true in an edge
or face interior.

The global degree is one. The sum of these positive local degrees
over any fibre is consequently one, including values on the images
of edges and vertices. Equivalently one can take a small regular
value in the link disc. Thus every point has exactly one preimage
and local degree one. Properness follows from (PF.2); the slice map
is a homeomorphism. The endpoint slice maps are the invertible
linear maps \(I\) and \(H\), and the same conclusion holds
there.

The full map preserves the two heights and is homogeneous. It is
therefore injective on the union of the original cones. For two
domain cones \(C,D\),
\[
                    F(C)\cap F(D)=F(C\cap D).            \tag{PF.5}
\]
Their original intersection is a common face, and each cone map is
linear and invertible. Thus (PF.5) is a common face of the two image
cones. This proves the fan property for the I,H sector without an
additional refinement.

## PF.3. A literal strip model for both rank-one sectors

For W use the prescribed basis
\(u=e_1,v=e_2-be_1\). Then \(P_0v=0\). For E exchange the
two basis vectors, so \(u=e_2,v=e_1\), and again \(P_0v=0\).
Exchanging these vectors only exchanges the two triangles in the
given collection; it does not change its cones. Put
\[
                   p=P_0u,\qquad A=Hu,\qquad B=Hv.
\]
Apply the rational inspection map with basis \((A,B)\) in the
two fibre coordinates. It sends \(A\) to \((1,0)\),
\(B\) to \((0,1)\), and \(p\) to \((c,d)\), where
\[
 \begin{array}{c|cc}
       &c&d\\ \hline
 W&(N-1)/(2N)&-a/(2N)\\
 E&1&-b/2.
 \end{array}                                             \tag{PF.6}
\]
In each case \(c>0\). This map is not declared unimodular;
all actual rays remain (PF.1) in their original lattice.

At fixed \(r,s>0\), the two top-triangle cones give precisely
the square
\[
                Q=[0,s](1,0)+[0,s](0,1),
\]
split along its diagonal from \((0,0)\) to \((s,s)\).
The one noncollapsed mixed cone gives the parallelogram
\[
           J=(s,0)+[0,r](c,d)+[0,s](0,1).                \tag{PF.7}
\]
These are the three noncollapsed maximal slice cells of the original
prism collection, not a replacement collection. Their union is
exactly
\[
 \begin{split}
 0\le x\le L:=s+rc,&\qquad f(x)\le y\le f(x)+s,\\
 f(x)&=\begin{cases}
       0,&0\le x\le s,\\
       (d/c)(x-s),&s\le x\le s+rc.
       \end{cases}
 \end{split}                                             \tag{PF.8}
\]
The actual periods in these coordinates are
\[
                 rP_0u+sHu=(L,rd),\qquad
                 rP_0v+sHv=(0,s).                        \tag{PF.9}
\]
They are exactly the translations used to tile by (PF.8).

Here is an explicit inverse cell assignment. For a point off the
displayed boundaries, choose the unique integer \(i\) with
\(0<x-iL<L\), then the unique integer \(j\) with
\[
  f(x-iL)<y-i rd-js<f(x-iL)+s.
\]
The point belongs to the cell labelled \(iu+jv\). Within that
cell, \(x-iL<s\) places it in Q, where the single diagonal
chooses one of the two triangles. For \(x-iL>s\), its actual
parallelogram coordinates are
\[
 \alpha=\frac{x-iL-s}{rc},\qquad
 \beta=\frac{y-i rd-js-(d/c)(x-iL-s)}s,
                 \qquad 0<\alpha,\beta<1.                \tag{PF.10}
\]
This proves both uniqueness and coverage with the exact period maps.

All boundary identifications in this tiling are whole faces. The
square and J share their full vertical edge. The right edge of J
is the left edge of the next square, under \((L,rd)\).
The top piecewise-linear boundary is the bottom boundary translated
by \((0,s)\), and the break at \(x=s\) occurs at exactly the
same place on both sides. The square's diagonal meets these edges
only at its two endpoints. Thus no T-junction or partial-edge
intersection remains. This explicitly proves common faces for all
positive height ratios, not merely disjoint interiors.

The ray identifications are independent of \(r,s\). Writing
the cell label as zero, the two collapsed bottom tetrahedra both
have the image face
\[
       \operatorname{cone}(R_0(0),R_0(u),R_1(u+v)),        \tag{PF.11}
\]
because \(R_0(v)=R_0(0)\) and
\(R_0(u+v)=R_0(u)\). This is the upper face of J and the
lower face of its v-translate. The other collapsed mixed tetrahedron
has the image face
\[
       \operatorname{cone}(R_0(0),R_1(v),R_1(u+v)),        \tag{PF.12}
\]
the top edge of Q and the bottom edge of its v-translate. Equations
(PF.11)--(PF.12) show that omitting the collapsed maximal cones and
then adjoining the ordinary faces loses no ray or required face.

The remaining face incidences are also literal common-ray subsets:
the diagonal of Q uses \(R_0(0),R_1(0),R_1(u+v)\);
the Q/J edge uses \(R_0(0),R_1(u),R_1(u+v)\);
the J/next-Q edge uses \(R_0(u),R_1(u),R_1(u+v)\).
Together with their period translates they give every interior
facet. The rank-one base face has just the rays \(R_0(iu)\)
and intervals between consecutive such rays; the other base face
has the ordinary H-triangle fan. These are faces of the same cones.
This completes the common-face proof, including the height boundary.

## PF.4. A compatible periodic refinement on the common H boundary

Apply \(H^{-1}\) on the H-height-one slice, solely to describe
its geometry. The I and E sectors give the standard unit-square
triangulation \(\mathcal T\); W gives its integral shear
\(\mathcal T_b\), with basis \(e_1,e_2-be_1\). Both are
\(\mathbb Z^2\)-periodic, locally finite, rational triangulations.
Take their literal overlay
\[
       \mathcal P=\{\sigma\cap\tau:
                   \sigma\in\mathcal T,\ 
                   \tau\in\mathcal T_b\},              \tag{PF.13}
\]
including all its faces and omitting empty intersections. This is
an exact common polyhedral refinement. Indeed a face of a member
is obtained by an active supporting inequality from one of its
two factors; intersecting two members activates the corresponding
common faces in the two original complexes. Their intersection is
therefore a common face. Local finiteness follows because a compact
set meets finitely many triangles in each factor. The periodic
quotient has finitely many cells, and every vertex is rational.

The certificate computes this overlay with rational arithmetic for
both actual b values, on a fundamental square and its neighbouring
period translates. It checks area one and every common-face
intersection. It retains the rational vertices; they are not silently
replaced by lattice vertices.

Coning the cells of \(H\mathcal P\) in the H boundary gives
the common rational boundary fan. Replace each rational ray by its
primitive integral generator in the original four-dimensional
lattice. This is an exact equality of the ray, not a change of the
lattice. If a simplicial refinement is wanted, use the barycentre
of each polygonal cell and the induced boundary subdivisions,
periodically.

There is an explicit compatible extension to each sector fan.
Prescribe that common subdivision on its H subfan, retain the other
base subfan, and process the remaining original faces in increasing
dimension. Once the boundary of a face F is subdivided, choose the
interior ray equal to the sum of F's primitive ray generators and
cone its subdivided boundary from that ray. On the slice \(r+s=1\)
this is the usual radial decomposition of a convex polytope from
an interior point: each ray from that point meets the boundary
once, so it covers and has common faces. Shared faces were processed
first and hence receive the same subdivision from both sides.

Every period map in (PF.1) is unimodular and carries primitive ray
generators to primitive ray generators. Thus the chosen sums and
the entire inductive construction are period-equivariant. There
are finitely many face orbits, so the construction has finitely
many subdivision types. This proves compatibility on H while
retaining the actual integral period actions. It does not assert
that the resulting cones are unimodular; a separate lattice
resolution may be applied to them with its own proof.

## PF.5. Exact audit boundary

The local fan and common-H-refinement claims above pass the independent
geometric audit. The raw rank-one prism map still collapses whole
tetrahedra; no injectivity statement about that map is restored.
The fans are locally finite over compact subsets of the strictly
positive height sector and near the full-rank H face. On a rank-one
base face the kernel-period unit and the properness of its analytic
quotient remain exactly the separate issue identified in the root
note. This audit supplies no omitted filling point, global proper
family, link multiplicity, characteristic number, or return class.

Exact checks are saved in `code/part3/source_zero_prism_audit.py`,
its JSON and captured output. No earlier-run text is used.
