# Source-moduli loops: exact E7 marked-node parameter and local transport

Working record after P3F.51. The exact marked source and local closure
claims in SM.1--3 and SM.5 are proved as P3F.54 after root's full
independent audit. No return class for a source-moduli loop
is assigned here. The scalar-return results retain their specified
fixed source and parameter. The purpose of this note is to identify
the additional actual transport problem, using literal coordinate
maps.

## SM.1. The complete selected-node cover for the E7 marked form

Use the full F51 source
\[
 y^2=P(x,t,r)=x^3+3rx^2+tx+1,\qquad G=(0,1).
\]
A singular finite fibre has a double root \(u\ne0\). The equations
\(P(u,t,r)=P_x(u,t,r)=0\) give the exact maps
\[
 r(u)=\frac{1-2u^3}{3u^2},\qquad
 t_0(u)=u^2-\frac2u,\qquad
 P(x,t_0(u),r(u))=(x-u)^2(x+u^{-2}).
 \tag{SM.1}
\]
Conversely these displayed functions give every marked finite
singular fibre of the normalized E7 source. A double root
determines \(u\), so this is its normalization parameter, with
no unmarked choice of a discriminant branch.

The selected fibre is nodal exactly when \(u^3\ne-1\). At
\(u^3=-1\) the displayed polynomial has a triple root, and
the selected fibre is the type II cusp. Thus the explicit
parameter for the marked source together with a selected
whole-zero \(I_1\) is
\[
                         U=\mathbb C^*\setminus\{u:u^3=-1\}.
 \tag{SM.2}
\]
The other finite fibres are allowed to coalesce to the II
fibre of F51 while the selected one stays nodal.
For example \(r=1,u=1/2\) selects the separate nodal
fibre \(t_0=-15/4\), whereas \(u=-1\) selects the cusp.
The maps (SM.1), not an equality of fibre profiles, distinguish
these two situations.

Their derivatives are
\[
 r'(u)=-\frac{2(1+u^3)}{3u^3},\qquad
 t_0'(u)=\frac{2(1+u^3)}{u^2}.
 \tag{SM.3}
\]
In particular the selected-node normalization is ramified
over a cusp parameter of the \(r\)-line.

The remaining constant marked coordinate equivalence is also
explicit. For \(s^3=1\), the map
\[
 x=s^2X,\quad y=s^3Y=Y,\quad t=s^4T
\]
sends \(r\) to \(r/s^2\) and \(u\) to \(u/s^2\), while
retaining \(G=(0,1)\). Hence its finite quotient on (SM.2)
is described by \(u^3\in\mathbb C^*\setminus\{-1\}\).
No monodromy of the total threefold is inferred from this
finite source-coordinate quotient.

## SM.2. Actual local extension in the permitted source parameters

Fix a point of \(U\), its selected zero and a proved E7
datum whose only cap is at \(III^*\). Over a sufficiently small disc in
\(U\), retain the displayed functions \(r(u),t_0(u)\) and
the actual section \(G\). The finite Weierstrass total source
is smooth at a nodal or cuspidal fibre: at a singular point
of the cubic, its derivative with respect to \(t\) is the
nonzero root \(x\). Thus the source family is a submersion
to this small parameter disc. At infinity the full root
equations of F51, their relative quotient charts and their
actual marked section resolutions give the simultaneous
minimal-source map.

The cap division section is holomorphic in this parameter
disc. Indeed it is the inverse branch of multiplication by
the cap order at the recorded central point; on a reduced
root both the identity group and component norm are the
ones already checked in F41. Every finite-character
averaging is the same explicit finite sum, and its remaining
unit has a holomorphic logarithm after shrinking the disc.
Its analytic root therefore gives the literal family of
commuting norm lifts. The Cartier correspondence of F51
uses the same invariant ideals in these relative charts.

At the selected node the exact holomorphic Morse chart is
the one in SM.3 below; at a point of \(U\) its square-root
branches are fixed on the small disc. The chosen fan and
the physical line character therefore have fixed marked
charts. Their monomial face maps and all cap annular maps
remain holomorphic in the source parameter. A fixed
sufficiently small scalar works uniformly on the compact
closure of this disc, by the strict norm estimate on the
common ordinary complement. The resulting glued family
is proper and is a holomorphic submersion on that disc.

Consequently the return around the boundary of such a
disc is isotopic to the identity by the actual smooth
bundle over the disc: choose a smooth horizontal complement
to the vertical tangent bundle and lift radial paths from
its centre. Properness makes these lifts complete on the
closed disc, giving a smooth fibre trivialization there.
Its restriction contracts the boundary return. This
includes a collision of two
unselected nodal fibres to a type II fibre: the source
surface remains smooth, the selected nodal chart persists,
and the starred cap maps remain the same full-coefficient
maps. It does not include a puncture \(u^3=-1\) of (SM.2),
where the selected zero itself ceases to be nodal.
This local extension keeps the finite source fibres unmodified.
The joint \(III^*+II\) cap belongs to the locus \(r^3=1\);
no extension of its II cap across a deformation to two
separate nodal fibres is asserted here.

## SM.3. The exact nodal-coordinate transport at a selected cusp

Put \(X=x-u\), \(q=t-t_0(u)\), and
\[
                         a(u)=u+u^{-2}.
\]
In the actual smooth source near its selected singular
point the equation becomes
\[
 y^2=X^2(X+a(u))+q(X+u),\qquad
 q=\frac{y^2-X^2(X+a(u))}{X+u}.
 \tag{SM.4}
\]
For \(a(u)\ne0\), choose a small chart
\(|X|<c|a(u)|\), with \(c<1\), and choose the displayed
square roots. Define
\[
 \xi=\frac{y-X\sqrt{X+a(u)}}{\sqrt{X+u}},\qquad
 \eta=\frac{y+X\sqrt{X+a(u)}}{\sqrt{X+u}}.
 \tag{SM.5}
\]
These are actual holomorphic coordinates near \(X=y=0\):
their Jacobian in \((X,y)\) is
\(-2\sqrt{a(u)}/u\), which is nonzero. Their product is
exactly \(q\), so (SM.5) is a base-preserving node chart.

At \(u_*\) with \(u_*^3=-1\), \(a'(u_*)=3\). On a small
positive loop about \(u_*\), the square root of \(X+a(u)\)
changes sign, while that of \(X+u\) can be retained on a
single analytic branch. The exact final chart map is
\[
                              (\xi,\eta)\longmapsto(\eta,\xi).
 \tag{SM.6}
\]
Thus the two normalization branches of the selected nodal
fibre are exchanged. Their ordered Picard gluing map is
reversed: an identification \(L_{p_+}\to L_{p_-}\) is
replaced by its inverse \(L_{p_-}\to L_{p_+}\). This is an
explicit source and line-branch transport, not yet the
clutch of the completed threefold.

## SM.4. Exact remaining comparison

Historical status of the first draft, retained verbatim. SM.5 below
now supplies the Tate/Cartier transition and marked double-cover
closure. The smooth relative return and the other global punctures
remain open.

For a global loop in \(U\), the source and cap data must
be transported together with the ordered node branches,
the source Picard character, the period marking and the
chosen periodic fan. Formula (SM.6) is the specific
transition at the three selected-cusp punctures. To close
a family over such a loop one must extend its resulting
torus map over the actual chosen toric completion, and
retain the finite-cap line lifts and their annular maps.

Those full toric/cap endpoint maps have not been computed
in this note. In particular no return in \(\Theta_7\) is
assigned from the equality of the fixed-source scalar
formulas, from the two-branch exchange alone, or from
divisibility of a known scalar-return integer. The
punctures \(u=0,\infty\) also require their actual
source-coordinate and completion comparison. This is
the separate source-moduli transport problem left by
the scalar-scope audit.

## SM.5. Exact Tate, Cartier-line and fan transition

The source-line transition in SM.3 can be identified on the
actual Tate model, retaining the line frame. In the selected
node chart let \(\Delta(t,r)\) denote the discriminant
polynomial (S51.3), without its factor 16. The exact identities
are
\[
 f(t_0)=-a(u)^2/3,\qquad
 \Delta_t(t_0)=-4u\,a(u)^3,\qquad
 j=-\frac{64a(u)^3}{u\,q}+O(1).
 \tag{SM.7}
\]
The actual Tate parameter \(q_T\), obtained from the inverse
of its \(j\)-series, is consequently
\[
                q_T=-\frac{u}{64a(u)^3}q+O(q^2).
 \tag{SM.8}
\]
For a sufficiently small fixed loop about \(u_*\), choose the
base collar with \(|q|\) uniformly small relative to \(|a|^3\).
Then \(q_T/q\) is an invertible holomorphic base function
throughout that collar.

The Tate Weierstrass model has \(c_4\) a unit with value one.
The source has \(c_4=16a^2+O(q)\). Its actual marked
Weierstrass scaling is therefore \(h=2\sqrt a\) times a
holomorphic unit with a fixed fourth-root branch. On one
positive loop about \(u_*\), that unit has no monodromy and
\(h\) changes sign. The source coordinate isomorphism
\(x=h^2x_T+\text{translation},y=h^3y_T\), in short form,
therefore changes by the marked elliptic inversion.
Since the zero section is fixed, there is no translation
factor. In the multiplicative Tate coordinate this is
literally \(Z\mapsto Z^{-1}\), with \(q_T\) unchanged.
The normalized period has the retained change \(-3\),
as follows also from (SM.8).

Here is its line map. Write \(P\) for the actual multiplicative
point of \(aG\). The line \(\mathcal O(aG-O)\) is represented by
\[
       (Z,V)\sim(q_T Z,P V).
 \tag{SM.9}
\]
The convergent Tate theta product has the exact identities
\[
 \Theta(q_TZ)=-Z^{-1}\Theta(Z),\qquad
 \Theta(Z^{-1})=-Z^{-1}\Theta(Z).
 \tag{SM.10}
\]
Its ratio \(f_P(Z)=\Theta(Z/P)/\Theta(Z)\) has divisor
\((P)-(O)\) and multiplier \(P\). It identifies (SM.9)
with the actual source Cartier line and its canonical
meromorphic section. On the continued chart \(P'=P^{-1}\),
and
\[
 f_{P^{-1}}(Z^{-1})=P f_P(Z).
 \tag{SM.11}
\]
Thus the divisor-compatible line transition is exactly
\((Z,V)\mapsto(Z^{-1},PV)\). Reindex once by the new
Tate deck \((Z',V')\mapsto(q_TZ',P^{-1}V')\).
The two line factors cancel, giving the literal
node-annulus transition
\[
                (Z,V,q_T)\longmapsto(q_T/Z,V,q_T).
 \tag{SM.12}
\]
Its square is the identity. The root of \(a\) exchanges
the two local branches; every finite multiple of \(G\)
avoids the critical point at the limiting cusp because a
section cannot meet a critical point of the elliptic
map. Hence this Cartier frame extends across that local
source neighbourhood. No component-supported line shear
has been inserted.

The source translation and its Hom lift are also transported:
their Tate form is
\((Z,V)\mapsto(g^{-1}Z,\lambda q C\,V)\), with actual
nonzero base units \(g,C\). Equation (SM.12) changes
\(g\) to \(g^{-1}\) and leaves its scalar factor fixed.
It intertwines the old and continued suspension maps
literally. The \(III^*\) cap data have holomorphic
coefficients on the full small \(u\)-disc, including
\(u_*\); their division section, unit root and finite
character can be chosen there by the exact constructions
of F41/F51. Their annular comparison remains part of
this transport, rather than being replaced by a different
cap.

On the cone-height lattice (SM.12) is
\[
             (v_Z,v_V,h)\longmapsto(-v_Z+h,v_V,h).
 \tag{SM.13}
\]
Its action on edge directions is
\(J=\operatorname{diag}(-1,1)\). It admits no invariant
index-one unimodular periodic three-edge triangulation,
even allowing an affine translation. Indeed the three
unoriented primitive edge directions have the three
distinct nonzero reductions in \(\mathbb F_2^2\).
Since \(J\) is the identity modulo two, an invariant
triangulation would require it to preserve each edge
line separately. A reflection has only two eigenspaces,
whereas these are three distinct lines.

Thus one loop about this selected-cusp puncture does not
close the chosen one-vertex toroidal completion under this
specified marked source, line and annular transport. Its
second iterate has the identity lattice and Cartier-line
transition (SM.12), and the finite cap coefficient
charts return as above. Using these literal transition maps
in the construction gives the marked holomorphic family
on the double cover \(a=\rho^2\). The actual return of that
closed double source loop remains the smooth relative
transport problem described next. An identity endpoint
coordinate transition alone does not compute a
mapping-class return.

## SM.6. The exact weighted source chart on the double cover

Set \(a(u)=\rho^2\), with \(u(\rho)\) the inverse branch
through \(u_*\), and use the literal maps
\[
              X=\rho^2\widetilde X,\quad
              y=\rho^3\widetilde Y,\quad
              q=\rho^6Q.
 \tag{SM.14}
\]
Equation (SM.4), divided by \(\rho^6\), becomes
\[
 \widetilde Y^2=\widetilde X^2(\widetilde X+1)
                  +Q\bigl(u(\rho)+\rho^2\widetilde X\bigr).
 \tag{SM.15}
\]
Its central source chart is
\(\widetilde Y^2=\widetilde X^3+\widetilde X^2+u_*Q\).
The discriminant is
\(-u_*Q(4+27u_*Q)\), and its compact minimal
Weierstrass model has a \(II^*\) fibre at infinity and
two \(I_1\) fibres at the displayed finite values.
The scalar source factor has become
\(\lambda\rho^6Q\), with its actual sixth winding
retained.

Every finite section multiple \(aG\) tends to \(O\)
in this chart. For example at \(u_*=-1\), the limiting
cuspidal fibre is \(y^2=(x+1)^3\); its smooth-group
coordinate is \(1/s\) in \(x+1=s^2,y=s^3\).
Thus \(aG\) has \(s=1/a\), and (SM.14) sends it to
infinity with formal parameter of order \(\rho\).
This is an actual section map. It does not by itself
identify the complete fixed-sphere trace or its line
with a compact page on that limiting source.

The remaining step is the relative smooth map from the
actual source-loop exterior and its moving toroidal
collar to this weighted chart, including the induced
circle line and boundary framing. Its Pontryagin and
line-square pairings have not been assigned here.

The expanded exact certificate
code/part3/source_moduli_nodes.py verifies (SM.1), (SM.3),
(SM.4)--(SM.8), the Tate-deck and suspension intertwining
in (SM.12), its square, the cone-height reflection, all six
unimodular mod-two edge bases, and (SM.14)--(SM.15).
Its algebraic checks pass; no source-loop index is encoded.

Root's independent full SM.5 audit PASS verifies the inverse-j
coefficient, square-root Weierstrass scaling, canonical theta
Cartier map, exact node reindex cancellation, actual suspension
and cap transport, and the mod-two fan obstruction. The export
of F54 contains only SM.1--3 and SM.5. SM.4 and SM.6 remain
working comparisons; the closed double-loop return is unassigned.
