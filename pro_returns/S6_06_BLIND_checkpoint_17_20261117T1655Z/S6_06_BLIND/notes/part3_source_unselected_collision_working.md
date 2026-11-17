# The actual unselected-collision disc and its zero return

Proved after root and independent fourfold audits: P3K.53.
The result concerns the global marked-source loop route following K49.
The source parameter is \(v\), and \(v_*=1/8\). The construction has
one III-star cap, the selected whole-zero I1 cusp, and no additional
logarithmic disc on the two unselected fibres that coalesce here.
The line, norm, finite character, annular integer and chosen fan are
the full marked data of K49. We retain the scalar
\(\lambda(v)=v^N\lambda_0\), \(N=km\).

The result proved below is the zero positive return of the actual
canonical continuation around \(v_*\). An independently inserted
cap-data or scalar loop is not included in that statement.

## UI.1. The source and selected cusp extend as actual maps

Use the literal Weierstrass model
\[
 Y^2=X^3+(1-2v)X^2+TX+v^2,\qquad G=(0,v),
 \qquad T_0=v^2-2v.
\]
The other two critical values are
\[
 T_\pm=\frac{1+4v\pm(1-8v)^{3/2}}8.
\]
At \(v_*=1/8\) they coalesce at \(T_*=3/16\). Their singular
point is \((X,Y)=(-1/4,0)\). Write the equation as \(F=0\), with
\[
 F=Y^2-X^3-(1-2v)X^2-TX-v^2.
\]
Then \(F_T=1/4\) at that point. The total source near the
collision is literally the graph
\[
 T=\frac{Y^2-X^3-(1-2v)X^2-v^2}{X},
\]
in the coordinates \((X,Y,v)\), with \(X\ne0\). Its map to the
\(v\)-disc is therefore a submersion, including the type-II fibre.
No separate labels or separate discs for \(T_+\) and \(T_-\) are
used in this neighbourhood.

The selected value is \(T_0(v_*)=-15/64\), which is distinct
from \(T_*\). Its nodal equation is exactly
\[
 Y^2=(X-v)^2(X+1).
\]
Choose the holomorphic branch \(\rho(v)=\sqrt{1+v}\) on a small
disc \(D\) around \(v_*\), with its reference value fixed. The node
preimages are \(s=\pm\rho(v)\) in the actual normalization
\(X=s^2-1\), \(Y=s(s^2-1-v)\). The branch does not exchange on
\(D\). The physical selected height is
\(q_1=T-T_0(v)\); the parameter Morse map and the Tate coordinate
retain the holomorphic nonzero unit \(q_T/q_1\). The marked point
\[
 P_G=\frac{1+\rho(v)}{1-\rho(v)}
\]
is finite and nonzero on this disc. The actual theta/Cartier map,
including its integral reindexing, consequently extends on the
selected cusp charts. A fixed periodic fan gives the same toric
coordinate charts over \(D\), with holomorphic nonzero unit
transitions. There is no reflection or additional height winding.

The sections \(G\) and \(O\) remain smooth and avoid the colliding
point. Thus their actual Cartier line
\(M_a=\mathcal O(aG-O)\) extends over the entire source family.

## UI.2. Uniform minimal source and cap roots

On \(D\), choose the actual nonzero holomorphic cube root
\(u(v)^3=v\). The map
\[
 (X,Y,T)\longmapsto(x,y,t)=(u^{-2}X,u^{-3}Y,u^{-4}T)
\]
gives
\[
 y^2=x^3+3r(v)x^2+tx+1,\qquad G=(0,1),\qquad
 3r(v)=\frac{1-2v}{u(v)^2}.
\]
At \(v_*\), \(u=1/2\), \(r=1\), and \(r'(v_*)=-8\) in this
reference branch. These are the full source-coordinate maps of
F51, specialized to a parameter disc through its E7-B member.
They do not discard the \(x^2\) term. The selected node is
\(t=-15/4\), while the type-II collision is \(t=3\).

An alternate fixed cube-root reference is also retained. Replacing
\(u\) by \(\zeta u\), \(\zeta^3=1\), gives the literal constant
coordinate map
\[
 (x,y,t)\longmapsto(\zeta x,y,\zeta^2t),\qquad
 3r\longmapsto\zeta\,3r.
\]
It fixes the marked zero and generator sections. The root coordinate
is carried by its chosen constant lift \(z\mapsto c z\), where
\(c^m=\zeta\). Since \(q_{\rm new}=\zeta q_{\rm old}\),
the two infinity coordinates \(x_0=q^2x\), \(y_0=q^3y\) are
unchanged. Thus the full minimal-root map is
\[
 (z,x',y')\longmapsto(cz,c^{-2k_0}x',c^{-3k_0}y'),
 \qquad k_0=3p\ \hbox{or}\ 3p-1
\]
in the good or reduced case. The actual Cartier map transports
the divisors \(aG-O\), and the root-line map retains this chosen
constant character.
The primitive source lift contributes \(\zeta^a\), and the old
selected height expressed in the new coordinate contributes
\(\zeta\). Their factor in the suspension is
\(\zeta^{1+ab}=1\). Thus this actual constant map transports an
alternate reference to the one just displayed without creating a
parameter winding or changing the literal scalar.

The III-star source resolution is uniform here. In the actual
infinity coordinates \(q=1/T\), \(x_0=q^2X\), \(y_0=q^3Y\), its
equation is
\[
 y_0^2=x_0^3+(1-2v)q^2x_0^2+q^3x_0+v^2q^6.
\]
For the good cap \(m=4p\), put \(q=z^m\) and divide \(x_0,y_0\)
by \(z^{6p},z^{9p}\). The exact root equation is
\[
 y'^2=x'^3+(1-2v)z^{2p}x'^2+x'+v^2z^{6p}.
\]
For the reduced cap \(m=4p-1\), divide by
\(z^{6p-2},z^{9p-3}\). Its equation is
\[
 y'^2=x'^3+(1-2v)z^{2p}x'^2+zx'+v^2z^{6p}.
\]
In both cases the actual section is \(G'=(0,vz^{3p})\), and
the root deck is
\[
 D:(z,x',y')\longmapsto
       (\zeta_m z,\zeta_m^{2p}x',\zeta_m^{3p}y').
\]
The good central elliptic curve, reduced central III model,
resolution ideals and section-leading coefficients are exactly
those of F51. All coefficients above are holomorphic on \(D\),
and \(v\) is a unit there. The actual equivariant blowup ideals
and their Cartier support functions therefore give the same
source/root/line correspondence over this disc. The section does
not cross an additional centre. The minimal source is smooth
over \(D\): near the finite collision this was the graph in
UI.1, and at infinity these are the uniform resolved charts.

The cap division branch, norm lift and finite character also
extend. On the good-root atlas, multiplication by \(m\) is
locally invertible at the specified division point. In the
reduced case use the actual good-root atlas and its retained
finite descent. The inverse branch selected at the reference
point continues holomorphically across \(D\), with its finite
kernel label unchanged. The norm-ratio is a nonzero base unit;
its root and the finite averaging cochain are taken on the
polydisc with that reference value. Thus the literal
\(A^m=B^n\), the finite character and every root-line Cartier
correction are preserved as maps, not only as fibrewise classes.

## UI.3. Translation, line lift and annular continuation

The source translation extends through the unselected type-II
point. A direct local verification uses the holomorphic vertical
vector field
\[
 W=2Y\,\partial_X+
       (3X^2+2(1-2v)X+T)\,\partial_Y.
\]
It is tangent to the displayed equation at fixed \(T,v\). Its
local expressions near \(O\) are the invariant elliptic vector
field. On the smooth part of the central cuspidal fibre the
group law can be checked directly. Its normalization is
\[
 X=s^2-\tfrac14,\qquad Y=s^3,
\]
with \(O\) at \(s=\infty\), the cusp at \(s=0\), and
\(G\) at \(s=1/2\). The invariant additive coordinate is
\(\tau=1/s\), with \(\tau(O)=0\) and \(\tau(G)=2\).
Hence \(Q=bG\) has \(\tau=2b\), or \(s=1/(2b)\), for
\(b=1,2\). In particular it is a smooth point and
\(2Y(Q)=1/(4b^3)\ne0\), so \(W(Q)\ne0\). Since
\(dX/(2Y)=-d\tau\), the displayed vector field takes \(O\)
to \(Q\) at the exact central time \(\beta_*=-2b\).
The time parameter \(\beta(T,v)\) taking \(O\) to \(Q\)
is holomorphic near the collision: at the central value the
time derivative is \(W(Q)\ne0\), so the analytic inverse
function theorem gives that branch. Its flow is an actual
holomorphic translation on nearby smooth fibres and extends
through the cusp, with inverse the flow of \(-\beta\). The
flow stays on compact fibres; the finite time interval is
covered by finitely many ordinary analytic flow charts. This
also proves the parameter-holomorphic extension.

The canonical Cartier/Hom map has its already specified whole
fibre divisor at \(q_1=0\), which is disjoint from this
collision. It has no new parameter divisor at \(v_*\): evaluate
its rational source formula at one ordinary point where all
Cartier frames are units. Its value is holomorphic and nonzero
there, and \(v\) is a unit. The total minimal source is smooth,
so a zero or pole supported only at the type-II curve would
have codimension two and cannot be a Cartier divisor. The map
therefore extends invertibly across this curve in the actual
line frames. This is the same source/line map used in the
suspension, not a new linearization.

The normalizing coordinate arrow in UI.2 preserves its literal
scalar. In the direction from \(E_v\) to the \(G=(0,1)\) model,
the primitive lift changes by \(u^{-2a}\), while the selected
height changes by \(q_{1,E}=u^4q_{1,\mathrm{norm}}\). Since
\(ab=2\), the factors in \(q_1U_a^b\) cancel exactly. The
remaining powers of the nonzero function \(u(v)\) are retained
in the root/line coordinate maps; their logarithms extend on
\(D\).

For the annular arrow, use a fixed cap-overlap annulus in the
\(T\)-plane outside all these finite critical values. This is
the same type of fixed annulus used to define the full \(F_0\)
in RCZ.5. Its source fibres are smooth over annulus times \(D\).
On its fixed angular charts, the actual source/root/Cartier
maps and their finite deck powers just constructed are
holomorphic over \(D\). Continue their Lie logarithms from
the full reference overlap, with the integer \(d\delta\),
finite characters and all ordinary and cyclic lattice
cochains included. Each discrepancy is integral and locally
constant in \(v\); it keeps its full reference value. The
fixed-contour Cauchy splitting in RCZ.5 preserves parameter
holomorphy and this reference. This gives the actual annular
map over \(D\).

This continuation uses the same fixed contours and source/line
root expressions as the continuation along the preceding
regular parameter path. Their inputs have no singularity at
\(v_*\). Thus it extends that canonical continuation itself;
no independent \(q^j\delta\) or parameter-scalar winding is
inserted at the endpoint. Extra prescribed cap-data loops
would be the separate loops of K41 and are outside this
statement.

Finally \(\lambda(v)=v^N\lambda_0\) is nonzero on \(D\) and
has the logarithm fixed by its reference value. Its actual
root multipliers and the scalar term in the ordinary-to-cap
cochain extend with that logarithm. This does not replace
\(\lambda(v)\) by a constant.

## UI.4. The compact family and its actual positive return

Choose the scalar in the common contracting range on the compact
parameter disc and the finitely many retained source/base charts.
The line maps in UI.3 have bounded operator norms in a fixed
Hermitian metric on these compact pieces. The usual inner and
outer norm shells therefore give a uniform compact fundamental
region for the suspension. At the finite cap use its actual free
root quotient and the root-line norm shell; at the selected cusp
use the fixed toric charts of UI.1. All their transitions are
the maps just displayed, holomorphic on \(D\). Each total chart
is smooth and its projection to \(D\) is a submersion.

The resulting family is proper over \(D\). Indeed each local
model is proper over its fixed base chart times \(D\), the
overlaps are the actual fibre isomorphisms above, and a finite
cover of the compact base by relatively compact such charts
gives compact inverse images of compact subsets of \(D\).
This is the actual compact suspension/cap/cusp family, including
the prescribed physical circle and fan.

A smooth connection for this proper submersion, averaged over
the physical circle, gives an actual smooth trivialization
over the contractible disc by transport along its radial paths.
Its restriction to the positive boundary loop has an endpoint
isotopy to the identity. Hence this unselected-collision loop
has oriented class zero and its mapping torus is
\(S^1\times S^6\). The comparison uses the actual inverse
closing arrow, which is intertwined by this disc trivialization;
there is no loop reversal.

For a smaller reference scalar within the same contracting
region, the radial scalar path gives the same smooth family
construction over the path times \(D\); its transport conjugates
the two boundary returns. This records the actual comparison
used when choosing a uniform small scalar for the global
source-loop construction.

## UI.5. Scope in the global loop relation

The proof supplies the disc-extending unselected-collision
branch of the marked global family. It does not identify the
two source-zero lifts on \(\rho^2=1+v\), discard their J-fan
transition, or compute the infinity endpoint. Those exact
maps remain the separate global-relation inputs.

## Audit record

Root completed the UI.1–5 review and the explicit additive-group and
alternate-root refinements. Fourfold independently checked all five
sections, including the actual source flow, Cartier extension,
root/annular characters and properness. Both audits passed. The
certificate source_unselected_collision.json records 104 exact
source/root/scalar identities. The first formatting attempt is
preserved in records; repairing its math delimiters did not change
the proof.
