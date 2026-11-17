# Exact nodal tangent frames for the arbitrary-fan comparison

This working note supplies the actual chart map requested in the
arbitrary-fan relative Pontryagin calculation.  It proves the local
relative bundle comparison; the final global gluing and relative square
remain assigned to the common exterior calculation.  In particular it
does not replace that calculation by the absolute identity
\(\pi_4SO=0\).

## 1. The actual smooth chart and its adapted frame

At a retained open critical edge the smooth threefold chart is
\[
 (x,y,z)\in\mathbb C^2\times\mathbb C^*,\qquad q=xy.
\]
Let \(\rho=(|x|^2+|y|^2)^{1/2}\).  On the complement of
the critical curve \(x=y=0\), the two columns of
\[
 U(x,y)=\frac1\rho
       \begin{pmatrix}x&\overline y\\-y&\overline x\end{pmatrix}
       \in SU(2)                                                    \tag{NFrame.1}
\]
are the normalized vertical vector and the normalized Hermitian lift
of the base direction.  Indeed
\[
 dq(x,-y)=0,\qquad dq(\overline y,\overline x)=\rho^2,
 \qquad U^*U=I,\quad\det U=1.
\]
Adding \(z\partial_z\) gives the adapted frame relative to the
smooth Cartesian frame
\((\partial_x,\partial_y,z\partial_z)\).  Formula (NFrame.1)
is the actual transition, including its nonzero degree on a small
normal three-sphere.  No extension of this adapted frame through the
critical curve is asserted.  The Cartesian frame already extends
through it.

## 2. Exact parameter equivariance and the relative bundle map

After the actual integral period reindexing, a compact torus parameter
loop on this chart preserving the base coordinate has the form
\[
 R_\theta(x,y,z)=
   (e^{ia\theta}x,e^{-ia\theta}y,e^{ib\theta}z),
 \qquad a,b\in\mathbb Z,\quad0\le\theta\le2\pi.
\]
Put \(D_\theta=\operatorname{diag}(e^{ia\theta},e^{-ia\theta})\).
Then
\[
 U(e^{ia\theta}x,e^{-ia\theta}y)=D_\theta U(x,y),
 \qquad
 U(R_\theta(x,y))^{-1}D_\theta U(x,y)=I.                \tag{NFrame.2}
\]
The third vector \(z\partial_z\) is invariant.  Thus the
derivative comparison in the adapted frame is literally the identity.
In the smooth Cartesian frame the comparison is
\(D_\theta\oplus1\).  It is a closed \(SU(2)\) loop;
its real spin lift is consequently closed as well.

Here is the bundle map in overlap coordinates.  Parametrize the
moving nodal chart by \((p,\theta)\mapsto(R_\theta p,\theta)\).
The adapted-to-Cartesian transition in these coordinates is
\(D_\theta U(p)\oplus1\).  Change the Cartesian frame by
\(D_\theta^{-1}\oplus1\), over the entire chart including
\(x=y=0\).  Its transition becomes \(U(p)\oplus1\), independent
of the parameter, and the map is the identity on the prescribed
adapted frame on the punctured overlap.  Since
\(D_0=D_{2\pi}=I\), this is an actual bundle isomorphism on the
parameter circle, not a map only on its interval cover.  The same
closed spin lift makes it an isomorphism of the specified spin
bundles.  This proves the local relative comparison through the node.

## 3. Bounded units and monomial overlaps

The units in the actual toric frame changes are retained.  A
base-preserving unit map is
\[
 (x,y,z)\longmapsto
   (u(q,\theta)x,u(q,\theta)^{-1}y,v(q,\theta)z),        \tag{NFrame.3}
\]
where \(u,v\) are nonvanishing.  Its inverse uses the same unchanged
\(q\) and the reciprocal units, so it is an actual chart
isomorphism.  On a sufficiently small common disc, the ratios
\(u(q,\theta)/u(0,\theta)\) and
\(v(q,\theta)/v(0,\theta)\) have their unique logarithms
vanishing at \(q=0\).  Replacing those logarithms by their scalar
multiples gives a homotopy through the actual isomorphisms
(NFrame.3), fixed on the central critical curve.  The central unit
loops split into their integral windings and periodic logarithms;
contracting the latter gives the compact loop of Section 2.

At the differential level the additional entries are multiples of
\(x\,d\log u\), \(-y\,d\log u\), and
\(z\,d\log v\).  Since \(dq=y\,dx+x\,dy\), all these
base-to-vertical entries extend smoothly and vanish at the node.
They are precisely the off-diagonal entries in the marked vertical
and base filtration, so its usual affine contraction is also a
smooth bundle homotopy through this chart.

An annular monomial overlap such as
\((x,y,z)\mapsto(z^k x,z^{-k}y,z)\), \(k\in\mathbb Z\),
is retained as its actual invertible coordinate map.  It changes
the compact weight \(a\) to \(a+kb\), but the two normal weights
remain opposite and (NFrame.2) still holds in the new coordinates.
In logarithmic vertical frames the overlap is the fixed integral
shear \(z\partial_z\mapsto z\partial_z+k(x\partial_x-y\partial_y)\).
Thus there is no omitted winding from replacing such an annular
monomial by a nonexistent global logarithm.

## 4. Exact scope of the remaining global check

These formulas extend the ordinary marked-lattice tangent comparison
across each retained open nodal critical curve.  They preserve the
adapted frame on the overlap and keep the actual period reindexing,
central shear, and annular monomial.  For the full exterior one must
still identify the resulting relative bundle cocycle on all the
overlaps with the boundary marking used in the twistor-capped master
space.  In particular a statement about absolute cohomology of the
exterior does not determine its boundary-relative Pontryagin lift.
The exact chart comparison above supplies that missing local input;
it does not assert the final global relative square without this
last gluing identification.

The identities in Sections 1--2 and the annular weight transformation
are checked symbolically in `code/part3_fourfold/nodal_frames.py`.
