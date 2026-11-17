# E6 unselected III collision: actual source and root maps

Active work recovered from orchestration after the checkpoint19 restore.
No return theorem is promoted by this note. The source and translation
maps below are explicit; the global Cartier/cap attachment is being audited.

Use
\[
 S_r:\quad y^2=x^3+r x^2+t x+t^2,\qquad G=(0,t).
\]
Its discriminant is
\(-16t^2[r^2(4r-1)+(4-18r)t+27t^2]\). Put
\(\rho^2=1-3r\) and select
\(t_+=(1-3\rho^2+2\rho^3)/27\). Near \(\rho=-1\),
the selected node stays at \(-4/27\), while the I2 at zero and
the other I1 merge to III. At infinity the source is IV-star.
The smallest whole-I1 datum to test is \(M_6=O(6G-O),Q=G\),
reduced IV-star cap \(m=2,n=1,d=0\). This is the actual
source-moduli loop under investigation.

Set \(U=y-t-x/2,V=y+t+x/2\). Exactly
\[
 UV=x^2(x+r-1/4),\quad t=(V-U-x)/2,\quad y=(U+V)/2.
\]
On the bidisc at r=0 the factor is a unit. Choose
\(c=\sqrt{x+r-1/4}\) and \(X=xc\). This is a parameter-preserving
analytic isomorphism to \(UV=X^2\); x is its analytic inverse
\(x(X,r)\), and t is the displayed actual base function. The
two minimal-resolution charts are \(X=Uz,V=Uz^2\) and
\(X=Vw,U=Vw^2\), with z=1/w. They give a simultaneous smooth
source resolution over the entire r-disc.

The +G formula has slope \(\kappa=(y-t)/x\),
\(x'=\kappa^2-r-x\), \(y'=-t-\kappa x'\).
In the x-blowup chart y=xv,t=xu, set \(\kappa=v-u\). Then
\[
 x=\kappa^2-r+(2\kappa-1)u,\quad
 u'=x/(1-2\kappa),\quad \kappa'=-\kappa-2u',\quad
 x'=u(1-2\kappa).
\]
Near the III component intersection the denominator is a unit.
At r=0 the two component maps are
\(\kappa_C\mapsto-\kappa_C/(1-2\kappa_C)\) into E and
\(\kappa_E\mapsto-\kappa_E\) into C; both first derivatives
are -1. At \(\kappa=1/2\), x=1/4-r is a unit and the target
t-chart is instead
\[
 x'/t=(1-2\kappa)/x,\qquad y'/t=-1-\kappa(1-2\kappa)/x.
\]
This is the actual strict -G chart and has no pole.

On the source t-chart x=ta,y=tb, the equation is
\(b^2=ta^3+ra^2+a+1\). Near G, use
\(\kappa=(ta^2+ra+1)/(b+1)\), which follows by cancelling
the literal factor a in (b-1)(b+1). The output x',y' above is
ordinary and regular, with x'(G)=1/4-r at t=0. Near -G put
\(N=(b-1)^2-ra^2-ta^3\); then
\[
 x'=N/a^2,\quad y'=-[ta^3+(b-1)N]/a^3,
 \quad \tau'=-x'/y'=aN/[ta^3+(b-1)N].
\]
The last denominator is a unit at a=0,b=-1, so this is the actual
O chart. At source O use \(\tau=-x/y\), \(p=1/x=\tau^2v\)
with v an analytic unit satisfying
\(v=1+r\tau^2v+t\tau^4v^2+t^2\tau^6v^3\). Its target
t-chart has
\[
 a'=p(1+2/\tau+2tp),\qquad
 b'=-1+(1/\tau+tp)a',
\]
which extends with (a',b')=(0,1). These charts cover the central
fibre; the inverse is the same construction for -G, or conjugation
by y->-y. The two maps compose to the identity on a dense open
set and hence everywhere. Thus the actual translation extends as
a holomorphic source automorphism through r=0, fixing t and r.

For the line, M6 is the actual section divisor 6G-O. At III, 2G
lies on the identity component at (1/4,-1/8); its additive coordinate
\(-x/y\) is 2, so that of 6G is 6. Thus 6G and O remain
distinct smooth points there, on the same component, and M6 has
degree zero on each component. On the conductor of the two tangent
components a degree-zero line has gluing jet 1+c kappa modulo
kappa^2. Translation swaps the components, inverting this jet, and its actual derivative is -1 on both branches. These two
operations retain c, proving that the central Hom line is trivial.
On smooth, I1 and I2 fibres the same Hom line is trivial by the
actual group translation. Proper direct-image evaluation therefore
gives the invertible relative line lift on this whole bidisc;
rigidification at a fixed ordinary source section fixes its base
unit. Its relation to a globally specified suspension multiplier
must retain that unit and its parameter order.

The reduced IV-star root at infinity has q=z^2,
x0=z^2X,y0=z^3Y and exact equation
\[
 Y^2=X^3+z^2(rX^2+X+1),\quad G'=(0,z),\quad
 D(z,X,Y)=(-z,X,-Y).
\]
With \(c(X,r)=\sqrt{1+X+rX^2}\), the coordinates
\(U=Y-zc,V=Y+zc\) satisfy \(UV=X^3\), and
\(z=(V-U)/(2c)\). This is an exact parameter-preserving A2
product; the fixed toric minimal resolution carries the original
q=z^2, deck (U,V)->(-U,-V), and marked section. For 6G the
source/root formal coordinate relation is \(\tau'=z\tau\).
The original section 6G has a nonzero finite identity-component
coordinate at q=0 near r=0 (its leading value is proportional to
1/4-r). The single graph blowup \(\tau'=zu\) separates it from
O, and the two exceptional coefficients cancel in their divisor
difference. This is the retained reduced-root Cartier comparison,
not a replacement by a tensor power of O(G-O).

The actual inverse of [2] in the central IV Neron group exists on
both its additive part and its component group Z/3. It gives the
unique extending D-invariant R with 2R=G'. The degree-zero root
line is centrally trivial; finite averaging of its norm-one line
unit and the prescribed analytic norm root give the actual
source/line cap A=t_{-R}D with A^2=B. All finite characters and
ordinary-to-cap annular cochains must be retained in the final
global family comparison.

The selected I1 and its section/Cartier neighbourhood stay disjoint
from the collision. The selected Tate and line units extend over
the r-disc, so their logarithms can be chosen on that disc without
parameter winding. The remaining task is to fix the complete
global suspension/annular normalization, prove its compact uniform
properness, and type the identity closing through these exact
source, Cartier, root and toric charts. No return is assigned yet.
