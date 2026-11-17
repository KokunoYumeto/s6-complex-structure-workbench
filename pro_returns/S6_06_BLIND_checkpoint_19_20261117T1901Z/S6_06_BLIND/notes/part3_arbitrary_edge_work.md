# Retained relative coordinates for further fan changes

Working exact reduction after P3K.23, 17 November 2026.
The remaining cross-edge comparison is explicitly retained.

For the one marked exterior \(D^3_y\times S^3_q\), record the actual
relative return as \(L^mR^n{\cal C}^s\), where the last coordinate is
taken modulo 28. P3K.23 proves the exact map
\[
 (m,n,s)\longmapsto(-n,m+2n,s+n)
\]
under its actual forward flop. The inverse map is
\[
 (m,n,s)\longmapsto(2m+n,-m,s+m).
\]
This is a literal inverse computation in the established relative
group, retaining both infinite coordinates. In particular, the
original fixed-edge coordinates can be recorded as
\[
 (m,n,s)=(-k+6A,-6A,A).
\]
The flopped coordinates are
\[
 (m',n',s')=(6A,-k-6A,-5A).
\]
The reverse flop adds \(m'=6A\) to its central coordinate and
recovers \(A\), as the inverse local family must. Applying the
fixed-edge index formula a second time to \(-5A\) would discard
these two infinite coordinates; that operation is not the inverse
local family comparison.

For completeness, the exact algebraic iterate of the same exterior
map is
\[
 T^r(L^mR^n{\cal C}^s)T^{-r}
 =L^{m-r(m+n)}R^{n+r(m+n)}
  {\cal C}^{\,s+rn+\frac{r(r-1)}2(m+n)}.
\]
The integer matrix is unipotent with square-zero nilpotent part.
This identity does not identify a sequence of different toric edges
with powers of one exterior map.

The integer \(n\) also has a direct Pontryagin interpretation without
requiring a circle action at the selected curve. Kill the variation
\(m+n\) by the explicitly extending \(L\) map. The resulting relative
class is \({\cal B}^{-n}{\cal C}^s\), where
\({\cal B}=LR^{-1}\). On the doubled mapping torus, place the central
support away from \(S^3_y\times\{q=1\}\). The normal clutch along
\(S^3_y\times S^1\) is \(\operatorname{Ad}_{\zeta^{-n}}\); the exact
Jin-direction connection computation in P3K.23 gives
\[
 \left\langle p_1,\,[S^3_y\times S^1]\right\rangle=4n.
\]
This is an actual relative derivative evaluation in the chosen
normal product. It does not replace the geometric identification
of that product for a different cusp curve.

For a further edge, the remaining map is therefore precise:
identify the actual local Cox normal product and parameter
trivialization of that edge with the marked exterior product used
to represent the same global return. The common logarithmic frame
and the node charts of notes/part3_nodal_frames.md give local
transition maps; they do not yet provide this integral global
relative identification across the other two critical curves.
Until that map is computed, the new edge's two infinite coordinates
are not assigned numerical values here.

All algebraic forward, inverse and power identities are executed
exactly in code/part3_fourfold/flop_relative_coordinates.py and its
JSON output. They leave the stated geometric comparison open.

## An exact local fan shear for the two nonvertical edges

The vertical-edge fan has unoriented edge directions
\[
       e_2,\qquad e_1,\qquad e_1-e_2 .
\]
The two triangles adjacent to the edge from \(0\) to \(e_1\) have
third vertices \(e_2\) and \(e_1-e_2\). Its flop replaces this edge
by the diagonal from \(e_2\) to \(e_1-e_2\), of direction
\(e_1-2e_2\). The resulting edge directions are
\[
       e_2,\qquad e_1-e_2,\qquad e_1-2e_2 .
\]
They are the image of the original fan under the integral shear
\[
        S=\begin{pmatrix}1&0\\-1&1\end{pmatrix}.
\]
The torus-coordinate map is the literal monomial isomorphism
\[
                      (Z,V)\longmapsto(Z,V/Z).
\]
The homogeneous lattice map fixes the height coordinate, so it
extends over the height-one toric models, preserving the base
coordinate \(q\). It also preserves the physical delta circle.

The period group transforms as well. For actual multiplicative
generators written
\[
 h:(Z,V)\mapsto(qZ,\alpha V),\qquad
 \gamma:(Z,V)\mapsto(gZ,q\lambda\beta V),
\]
the conjugated generators are
\[
 ShS^{-1}:(Z',V')\mapsto(qZ',(\alpha/q)V'),\qquad
 S\gamma S^{-1}:(Z',V')\mapsto(gZ',(q\lambda\beta/g)V').
\]
Thus the monomial map descends to an exact isomorphism with the
target model carrying these transformed periods. The requested
flop family retains the original period group in its common
exterior. Comparing its relative return with this shear therefore
requires the actual outer-period identification; the displayed
monomial map records exactly the transformation that such an
identification must carry. It does not by itself assign a return
value to the nonvertical-edge flop.
