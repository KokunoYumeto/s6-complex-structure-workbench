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

## EU.1. The precise completed datum and the retained earlier stage

The preceding text is the preserved initial local calculation. The
following sections complete its marked datum; no previously unspecified
scalar normalization is silently chosen. The whole earlier source is
also saved in `records/attempts/e6_unselected_iii/pre_full_attachment.md`.

Take a small closed complex parameter disc \(\Delta_r\) about zero.
Choose the analytic branch \(\rho^2=1-3r\) with \(\rho(0)=-1\), and put
\[
 t_c(r)=\frac{1-3\rho(r)^2+2\rho(r)^3}{27},\qquad
 q=t-t_c(r),\qquad s=\tfrac14-r.
 \tag{EU.1}
\]
The source is the simultaneous minimal regular model of \(S_r\)
constructed above, with its literal map to the \((t,r)\)-bidisc. Its
line is \(M_6=\mathcal O(6G-O)\). The source map of the suspension is
\(T:p\mapsto p-G\). Fix the quadratic reduced \(IV^*\) cap at infinity,
either signed primitive norm \(n=\pm1\), its prescribed character
\((-1)^d\), and the entire ordinary-to-cap reference map at a nonzero
\(r_*\in\Delta_r\). The selected cusp is the whole \(I_1\) fibre at
\(t_c(r)\), with any specified lattice-basis fan and the physical line
circle. There is no extra logarithmic disc at the colliding fibres.

The exact global suspension section is specified next. This defines a
marked scalar family rather than a generic Picard class. The completed
family extends over \(\Delta_r\) with this actual scalar held fixed and
small. Therefore its positive boundary loop has return class zero on
every such fan. The proof below constructs that extension and its
identity parameter closing before using smooth bundle triviality.
This result is submitted for independent audit; no numbered statement
or manuscript promotion is made here.

## EU.2. The complete rational Cartier multiplier at the collision

Write \(D_j=(jG)-(O)\). In the actual Weierstrass rational frames let
\(f_{2,G}\) be the tangent-over-vertical Miller function, and construct
\(f_{3,G}\), then \(f_{6,G}=f_{3,G}^2f_{2,3G}\), by their actual chord
and tangent functions. The convention is
\[
 \operatorname{div}_{\rm generic}(f_{j,G})=jD_1-D_j,
 \qquad r_6=f_{6,G}^{-1}:M_6\longrightarrow M_1^{\otimes6}.
\]
The arrow includes both source and target factors at every chart; it
does not identify the two line bundles by their generic classes. With
\(U=y-t-x/2\), the full rational functions and transported lift are
\[
 f_{2,G}=\frac{U}{x-s},\qquad
 B_6(p)=f_{2,G}(p)^6\frac{f_{6,G}(Tp)}{f_{6,G}(p)},\qquad
 B_{\rm sel}(p)=\frac{q}{t^3}B_6(p).
 \tag{EU.2}
\]
Thus \(B_{\rm sel}:M_{6,p}\to M_{6,Tp}\) is a typed rational line map.
The denominator \(t^3\) is retained, not absorbed into a source-
parameter scalar.

Here is its complete divisor calculation near the present parameter
disc. For \(r\ne0\), the generic identity component of the \(I_2\)
fibre is described by \(w=z+1\) and
\(x_0=s+w^2-w\). The actual inverse-translation chart gives
\[
 \frac{B_6}{t^3}\bigg|_{t=0}
       =\frac{8((1-s)w-s)}{s^3}
 \tag{EU.3}
\]
at its generic point, in the rational source/target frames away from
their horizontal divisors. Here are the full factors establishing it.
Put \(\lambda_3=-2t/s-1/2\),
\(L_\pm=y\mp t\mp\lambda_3x\), and
\(x_3=2t(2t+s)/s^2\). The source equation gives
\[
 L_+L_-=x(x-s)(x-x_3),\qquad
 f_3=\frac{UL_+}{(x-s)(x-x_3)}
     =\frac{s xU}{sV-(s+2t)x}.
\]
The actual inverse translation has
\(x(Tp)/t\to2w/x_0\), \(y(Tp)/t\to(s-w^2)/x_0\).
The tangent of \(3G\) has limiting slope
\((1-3s)/(2(1-s))\) and \(x(6G)\to s^3/(1-s)^2\).
Direct substitution therefore gives
\[
\begin{aligned}
 f_2(p)&\to x_0/w,& f_3(p)&\to x_0,\\
 f_3(Tp)/t&\to\frac{2w^3}{x_0(w-s)},&
 f_{2,3G}(p)&\to\frac{x_0(1-s)}{(1-s)w-s},\\
 f_{2,3G}(Tp)/t&\to
       \frac{2(1-s)(w-s)^2}{s^3x_0}.
\end{aligned}
\]
Their literal product in EU.2 is EU.3. The denominators
\(s\) and \(1-s\) are units on the present disc. The line \(M_6\)
has degree zero on both \(I_2\) components. The Hom divisor consequently
has zero component intersections, and the primitive kernel of the
\(I_2\) matrix is the whole fibre. Hence its exact vertical divisor
there is \(3F_0\), on both components.

At a finite irreducible fibre \(F_c\), \(c\ne0\), write the actual
function \(f_{6,G}=(t-c)^e u\) in its component DVR. The displayed
base-preserving translation fixes \(t-c\), so the ratio in EU.2 is
literally \(u(Tp)/u(p)\). Neither \(U\) nor \(x-s\) contains an
entire such fibre. This proves the absence of every other finite
vertical divisor, including a fibre where a horizontal section
meets \(O\). At infinity the line has degree zero on every \(IV^*\)
component and its Hom degree is \(6h(G)=1\). Thus the exact remaining
vertical order is \(-2F_\infty\). Multiplication by \(q/t^3\), whose
divisor is \(F_c-3F_0+2F_\infty\), leaves exactly \(F_c\). This is
the selected whole-zero-one map of F41, with its rational scalar now
specified by EU.2.

The same map extends across \(r=0\) without a parameter factor. The
resolved source threefold is smooth by its exact \(A_1\) product
coordinates. The actual \(T\) and its inverse extend by the preceding
addition charts. Hence the relevant Hom sheaf is an invertible sheaf
on that smooth threefold. Outside the curve \(\{r=t=0\}\), EU.2 is
already invertible, except for its prescribed selected zero. To check
the divisor \(\{r=0\}\), evaluate on one ordinary local source
section with \(t\ne0,t_c\) avoiding the finitely many horizontal
divisors of the rational functions. There \(s=1/4\) and every actual
factor and its inverse is holomorphic and nonzero. Thus no component
of the parameter divisor occurs. The remaining omitted curve has
complex codimension two. In regular local rings a rational section
of an invertible sheaf that has valuation zero at every height-one
prime is a unit. Apply this to EU.2 and its inverse. It supplies the
actual extending line morphism on the whole collision neighbourhood.
No new rigidification or scalar depending on a punctured parameter
disc has been inserted.

For comparison with a specified local Hom frame, take the value of
EU.2 on that same ordinary section. Its ratio to the frame is an
explicit holomorphic unit on \(\Delta_r\); multiplying the frame by
that ratio makes it exactly EU.2. Its logarithm on the disc is fixed
by its value at \(r_*\), so this typed comparison introduces no
parameter winding. The central conductor-jet calculation above gives
the same fibrewise Hom line and independently checks this extension.

## EU.3. The whole quadratic root, translation and line charts

The literal source coordinates at infinity are
\(q_\infty=1/t,x_0=q_\infty^2x,y_0=q_\infty^3y\). The quadratic
root has \(q_\infty=z^2,x_0=z^2X,y_0=z^3Y\), and hence
\[
 Y^2=X^3+z^2(rX^2+X+1),\quad G'=(0,z),\quad
 D(z,X,Y)=(-z,X,-Y).
\]
With \(c(X,r)=\sqrt{1+X+rX^2}\), put \(U=Y-zc,V=Y+zc\).
Then \(UV=X^3\) and \(z=(V-U)/(2c)\); this is an exact
parameter-preserving \(A_2\) product. Near its common central
component point use the middle toric chart
\[
 X=ab,\quad U=a^2b,\quad V=ab^2,\quad
 c=\sqrt{1+ab+ra^2b^2},\quad
 z=\frac{ab(b-a)}{2c},\quad Y=\frac{ab(a+b)}2.
 \tag{EU.4}
\]
The deck is \((a,b,z)\mapsto(-a,-b,-z)\). Define the following
analytic units, all with value one at \(a=b=0\):
\[
\begin{aligned}
 K&=1+\frac{b(b-a)(1+rab)}{2c(c+1)},\\
 F&=1-\frac{ab(1+rab)(K+1)}{2c(c+1)}
           -\frac{ra b^2(a-b)}{4c^2},\\
 X'&=a(a-b)F,\qquad c'=\sqrt{1+X'+rX'^2},\\
 H&=K+\frac{b(a-b)(1+rX')}{2c(1+c')}.
\end{aligned}
 \tag{EU.5}
\]
The literal chord formula for translation by \(G'=(0,z)\) is
\(\kappa=(Y-z)/X=aK\),
\(X'=\kappa^2-rz^2-X\), \(Y'=-z-\kappa X'\).
Substitution into the target toric chart gives exactly
\[
                 a'=(b-a)F/H,\qquad b'=-aH.
 \tag{EU.6}
\]
Indeed \(V'=Y'+zc'=-aX'H\), so \(b'=V'/X'\) and
\(a'=X'^2/V'\). This retains \(z\), hence the actual base
\(q_\infty\), and its derivative at the central point is
\(\left(\begin{smallmatrix}-1&1\\-1&0\end{smallmatrix}\right)\),
of determinant one. It carries the three actual branches cyclically.
The units in EU.5 are invariant under \((a,b)\mapsto(-a,-b)\), so
this translation commutes with the full root deck.

The complement of this chart in the central root fibre is its smooth
Neron group locus. There the chord law in the actual resolved
Weierstrass charts is holomorphic in \((z,r)\). The displayed map and
the analogous inverse, obtained by \(Y\mapsto-Y\), agree with that
law on their overlaps. They therefore construct the complete source
automorphism through the central root, not only its tangent action.

The unique root division section can be constructed by an explicit
identity-component inverse:
\[
             R=2G'-[2]^{-1}(3G'),\qquad 2R=G'.
 \tag{EU.7}
\]
The section \(3G'\) lies in the small formal group at the central
fibre. The inverse of \([2]\) there is its convergent formal-group
inverse, with derivative \(1/2\). Translation by that section is
the time map of the actual invariant vertical vector field on the
resolved root, with its analytic Lie coefficient. That vector field
extends through EU.4; it is the derivative of the identity-component
addition law and vanishes at the component intersection. Its small
flow exists uniformly on a compact root tube. Together with the
twice-iterated map EU.6 it gives translation by \(R\) and its inverse.
The central component of \(R\) is the nonidentity label two. Formula
EU.7 is deck-invariant, by uniqueness of the identity-component
inverse and the actual deck action on \(G'\).

The actual section-line comparison also varies holomorphically over
the whole parameter disc. To specify its complete common graph,
blow up the four literal deck fixed points on the resolved root:
the triple point, the two outer toric-chart origins, and \(O\).
Each has derivative \((-1,-1)\). The deck fixes each exceptional
curve and negates its normal coordinate, so its quotient is smooth.
Each old component meets two centres and has strict square \(-4\)
before quotient, and square \(-2\) afterward. The four exceptional
images also have square \(-2\). Pulling back the actual equation
\(q_\infty=z^2\) gives multiplicities two on the three old
components, three on the triple exceptional image, and one on the
three outer images. The generic map
\((z,X,Y)\mapsto(q_\infty,x_0,y_0)=(z^2,z^2X,z^3Y)\)
therefore yields the minimal regular resolution of the original
Weierstrass equation. Denote the root blowup by \(\beta\) and this
quotient/source map by \(\pi\). These are the actual morphisms
in EU.9, with every exceptional curve retained.

In source coordinates at infinity let
\(\tau_0=-x_0/y_0\); in the root let \(\tau'=-X/Y=z\tau_0\).
The exact chord calculation gives
\[
 x_0(3G)\big|_{q_\infty=0}=4/s^2,\quad
 y_0(3G)\big|_{q_\infty=0}=8/s^3,\quad
 \tau_0(6G)\big|_{q_\infty=0}=-s.
 \tag{EU.8}
\]
Thus \(\tau'(6G')=z[-s+O(z)]\). In the actual graph blowup
\(\tau'=z u\), the source point is \(\tau_0=u\); \(O\) and
\(6G'\) have distinct directions \(0\) and \(-s\). Their two
pulled-back divisor equations both contain the same factor \(z\),
which cancels in their difference. Every further resolution centre
is away from these two marked sections. Consequently on the full
common resolved graph the actual equality is
\[
       \beta^*\mathcal O(6G'-O)=\pi^*\mathcal O(6G-O).
 \tag{EU.9}
\]
This is equivariant for the source and deck maps already constructed;
both rational \(r_6\) factors are carried on source and target. It
transports precisely EU.2 to the root line \(N\).

For completeness, the pulled-back multiplier is an actual unit before
the norm is chosen. The root scaling is
\(x=z^{-2}X,y=z^{-3}Y,t=z^{-2}\); hence the literal Miller factors
have weights \(z^{-1},z^{-2},z^{-5}\) for \(f_2,f_3,f_6\), respectively.
Writing \(B'_6\) for the same full Miller ratio on the root, this gives
\[
 B_0=B'_{\rm sel}=h z^{-2}B'_6,\qquad
 h=1-t_c(r)z^2.
 \tag{EU.9a}
\]
The graph Cartier map EU.9 and the already computed whole-fibre divisor
give order two for \(B'_6\) on each reduced-IV component. Its leading
coefficient can also be read directly. At a generic point on the
identity component write \(X=w^2,Y=w^3+O(z^2)\). The exact root formula
\[
 f'_3=\frac{s zX(Y-z-zX/2)}
              {s z(Y+z+zX/2)-(s z^2+2)X}
\]
and the actual inverse translation yield
\[
 f'_2\to w,\quad f'_3(p)/z\to-s w^3/2,\quad
 f'_3(Tp)/z^2\to s,\quad
 z f'_{2,3G'}(p),\ z f'_{2,3G'}(Tp)\to-4/s.
\]
Indeed \(z^2X(3G')\to4/s^2\),
\(z^3Y(3G')\to8/s^3\), and \(z^2X(6G')\to1/s^2\),
which give the last two tangent-over-vertical limits. Their product
is \(B'_6/z^2\to4\). In the trivial central line of EU.9 this is
the same constant on the connected reduced fibre. Thus EU.9a has
central coefficient \(4h\), and its full rational coefficient and
inverse extend as units by the height-one-prime argument used in EU.2.

On the central reduced IV fibre the two horizontal divisors of
\(N=\mathcal O(6G'-O)\) coincide and its component degrees vanish.
Thus \(N\) is actually trivial there. Choose a lift \(F\) of
translation by \(-R\) using the transported Hom evaluation. Compact
connected fibres make every ratio of two such lifts a base unit.
Both central commuting source maps act by constant multipliers on
the trivial central line, so the finite commutator character is one.
More explicitly,
\[
 DFD^{-1}=c_F(z,r)F,\qquad
 c_F(z,r)c_F(-z,r)=1,\qquad c_F(0,r)=1.
\]
Choose \(\ell=\log c_F\) with \(\ell(0,r)=0\). Then
\(\ell(-z,r)=-\ell(z,r)\), so the literal replacement
\(F_1=\exp(\ell/2)F\) satisfies
\[
 DF_1D^{-1}=\exp(-\ell/2)c_FF=F_1.
\]
The actual root suspension lift is
\(B_0=\beta(z,r)F_1^2\), where \(\beta\) is a nonzero
deck-invariant base unit by EU.9a. Its analytic square root with
the prescribed value at \(r_*\) exists on the full root disc times
\(\Delta_r\) and is deck invariant: the ratio of its deck transform
to itself is a constant sign, equal to one at \(z=0\).
Put \(\widetilde F=\beta^{1/2}F_1\). For either sign and every retained
character the actual cap action is
\[
 A_0=(-1)^d\widetilde F^{\,n}D,\qquad
 A_0^2=B_0^n,\qquad [A_0,B_0]=1.
 \tag{EU.10}
\]
All operations are equalities of the source/Cartier maps, not just
of their central values.

## EU.4. The complete annular reference, scalar and closing

Use an auxiliary scalar root \(R_\lambda\) with
\(\lambda=R_\lambda^2\), fixed nonzero and small. It is independent
of the source parameter \(r\). The actual actions are
\[
 B_\lambda=\lambda B_{\rm sel},\qquad
 A_{\lambda}=R_\lambda^{\,n}A_0,\qquad
 A_\lambda^2=B_\lambda^n.
 \tag{EU.11}
\]
Fix a cap annulus \(C\) in \(q_\infty\), uniform over
\(\Delta_r\), whose source fibres are smooth. Cover it by two angular
sectors \(C_\alpha\); their overlap has two components and no triple
overlap is needed. Write
\[
 s_\alpha=\frac{\log_\alpha q_\infty}{2\pi i},\quad
 z_\alpha=\exp(\pi i s_\alpha),\quad
 c_\lambda=\frac{n\log R_\lambda}{2\pi i}+\frac d2.
 \tag{EU.11a}
\]
Let \(I_{z_\alpha}\) be the actual source/root and Cartier map
EU.9 on this smooth annulus. In particular
\(I_{-z}=D I_z\). The rigidified degree-zero line gives its actual
commutative extension of the elliptic group by the line scalar group.
Use its Lie cover and period lattice, with
\(\delta=(0,1)\) exponentiating to one turn of the physical line.
In this cover choose the logarithm
\[
 f_\alpha=(-a_\alpha(R),\ell_\alpha)
       =\operatorname{Log}_\alpha\widetilde F,
 \qquad b_\alpha=\operatorname{Log}_\alpha B_\lambda.
 \tag{EU.11b}
\]
Here \(a_\alpha(R)\) is the actual Abel integral from \(O\) to
\(R\); \(\ell_\alpha\) is the logarithm of the lifted line action
in the same rigidified extension, including both \(r_6\) factors,
\(h\), and the chosen square root of \(\beta\). The displayed
ordered pair is a Lie-cover coordinate, so its exponential is the
full source/line map, not independent multiplication in an arbitrary
Cartier chart. Compactness of the elliptic fibre makes the commutator
of rigidified translation lifts a constant scalar; its value at the
identity is one. These are consequently commuting Lie translations,
and their exponentials commute with \(B_\lambda\).

The literal sector formula is
\[
 \Phi_\alpha
   =\operatorname{Exp}\!\left(
       n s_\alpha f_\alpha+s_\alpha c_\lambda\delta
                         +h_\alpha\right)I_{z_\alpha}.
 \tag{EU.11c}
\]
Thus its source Abel displacement is
\(-n s_\alpha a_\alpha(R)\), its scalar factor includes
\(R_\lambda^{n s_\alpha}\exp(\pi i d s_\alpha)\), and its
root changes by the displayed \(D\). The correction \(h_\alpha\)
is now specified relative to the entire reference map, with no
invariant logarithm of a central nonidentity component presumed.

On an overlap let \(s_\beta=s_\alpha+k_{\alpha\beta}\) and write
\[
 f_\beta=D_*^{k_{\alpha\beta}}f_\alpha+
                         \Pi_{\alpha\beta}.
\]
The vector \(\Pi_{\alpha\beta}\) is an actual integral combination
of the transported source/line periods. Its coefficients, the
reference suspension deck integers \(j_{\alpha\beta}\), and the
reference full period vectors \(\Lambda_{\alpha\beta}\) are fixed
by the given reference map at \(r_*\). The period functions themselves
vary holomorphically in \(r\). Set
\[
 h_\beta-D_*^{k_{\alpha\beta}}h_\alpha
  =-n s_\alpha\Pi_{\alpha\beta}
          +j_{\alpha\beta}b_\beta+\Lambda_{\alpha\beta}.
 \tag{EU.11d}
\]
The actual reference logarithms satisfy exactly this equation at
\(r_*\). It retains the scalar period \(d\delta\), every elliptic
period and every suspension deck used by that reference. In a
reference lifted with no additional suspension deck one has
\(j_{\alpha\beta}=0\); the formula does not impose that choice.

Here is an explicit holomorphic solution retaining that reference.
Use \(I_z\) to express the Lie vectors in the ordinary Lie bundle
over \(C\), and fix a holomorphic frame of that bundle, including
the scalar vector \(\delta\). Such a frame is obtained from the
actual invariant differential and the rigidified line splitting;
the latter is the same additive annulus splitting described next.
Extend the reference \(h_\alpha(r_*)\) in this frame to initial
vectors \(h^0_\alpha\). Subtract their difference from the right
side of EU.11d, obtaining a holomorphic additive overlap vector
\(E_{\alpha\beta}\) that is zero at \(r_*\).
Choose a smooth partition \(\chi_\beta\) subordinate to the fixed
sectors and put \(k_\alpha=-\sum_\beta\chi_\beta
E_{\alpha\beta}\). Then \(k_\beta-k_\alpha=E_{\alpha\beta}\),
and \(\bar\partial k_\alpha\) is a single vector-valued form
\(\omega\). After a fixed cutoff on a slightly larger annulus,
the literal Cauchy--Green operator is
\[
 v(q_\infty,r)=\frac1\pi\int
            \frac{\omega(w,r)}{q_\infty-w}\,dA(w),\qquad
 h_\alpha=h^0_\alpha+k_\alpha-v.
 \tag{EU.11e}
\]
On the smaller fixed annulus \(\bar\partial v=\omega\).
The formula is holomorphic in \(r\), and its corrections are zero
at \(r_*\). It solves EU.11d exactly. Finite averaging, where
needed in the root atlas, is applied to these vector cochains only;
the lattice and finite-character cocycles remain the prescribed
ones. Their cyclic relation is the literal norm
\(A_\lambda^2=B_\lambda^n\), already proved in EU.10--11.

Substitute EU.11d into EU.11c. The difference of its two Lie
arguments after subtracting the \(k_{\alpha\beta}\)-fold cap
action is \(j_{\alpha\beta}b_\beta+\Lambda_{\alpha\beta}\).
Exponentiating therefore gives the exact squares
\[
 \Phi_\beta=A_\lambda^{k_{\alpha\beta}}
                   B_\lambda^{j_{\alpha\beta}}\Phi_\alpha,
 \qquad \Phi_\alpha B_\lambda=B_\lambda\Phi_\alpha.
 \tag{EU.12}
\]
In the chosen single-sheet lift this is
\(\Phi(s+1,r)=A_\lambda\Phi(s,r)\), with the full root deck
included. The inverse is given by the negative Lie argument and
\(I_z^{-1}\), so these are actual annular isomorphisms. The finite
cap charts and their actions extend over its central fibre by
EU.4--10; EU.12 is their exact overlap with the ordinary model.
No extension of an annular logarithm across that central fibre is
asserted or needed. This supplies the complete source, Cartier,
norm, scalar and reference-cochain attachment over \(\Delta_r\).

All maps are single valued in \(r\) on \(\Delta_r\). Traversing
its positive boundary therefore has source, line, finite-root and
annular forward closing equal to the identity. There is no scalar
winding: the scalar in EU.11 was held fixed, and every additional
base unit has its fixed disc logarithm. This closing assertion is
made for the complete quotient atlas, not inferred from a
fibrewise conjugacy.

## EU.5. Every selected fan and the proper disc family

The selected node remains disjoint from the collision and from both
marked sections. Its branch parameter, inverse-j coordinate, Tate
period and actual theta/Cartier multipliers are holomorphic on the
selected disc times \(\Delta_r\). Their leading units are nonzero
there. The selected branch marking is fixed by its value at \(r_*\);
the parameter disc admits no branch exchange. For every specified
periodic fan, each absolute cone character has the form
\(Z^uV^v q^h\). The full source/line maps multiply it by the actual
holomorphic base units to their integral powers. Those factors and
their inverses extend on the affine cone. The resulting chart maps
agree on faces as the same character maps. All periods and the
physical circle are retained. Hence this construction works for
every prescribed lattice-basis fan with the identical closing.

On the compact source parameter disc and finitely many source/cap
charts, the actual line multipliers and their inverses are bounded
away from the selected zero. The source translation maps have the
same compact bounds. Choose \(|\lambda|\) smaller than their common
contracting threshold. The ordinary norm shells, root norm shells
and selected periodic toric fundamental regions are then compact
uniformly in \(r\). In the finite cap, choose integers \(u,v\) with
\(nu+2v=1\); its actual generator
\(H=A_\lambda^uB_\lambda^v\) satisfies \(H^2=B_\lambda\), and its
scalar factor is \(R_\lambda\). Strict contraction proves freeness
and properness of the quotient. These are the same full quotient
maps as F41/F46. The explicit product resolutions above and the
source/cap charts show that projection to \(\Delta_r\) is a smooth
submersion. The compact fundamental regions show it is proper.

At \(r=0\) its source is the E6-B source of F46. Its two cap orders
are \((m_6,m_2)=(2,1)\), with \((n_6,n_2)=(n,0)\), so the actual
determinant is \(n=\pm1\). F46's integral maps prove that this
central reference-fan fibre is the constructed oriented sphere.
For a prescribed lattice-basis fan \(P\), take its finite canonical
fan word. At each step the actual common blowup and its two ruling
maps of F35 identify the unchanged complement and the two attaching
boundaries. F35's primitive integral Gysin maps and its van Kampen
maps preserve the sphere homology and simple connectivity through
that literal surgery. Following this finite word therefore supplies
the sphere fibre on \(P\), with the period and physical-circle
markings carried by those maps. The toric parameter maps above are
defined on that same \(P\) throughout the disc. All its other
fibres are consequently the same smooth sphere type by the proper
disc submersion. Choose a smooth horizontal distribution on this actual
proper family, and use radial paths on \(\Delta_r\) to trivialize
it. The identity atlas closing in EU.12 gives a boundary return
isotopic to the identity. Its clutched class is thus zero in
\(\Theta_7\), on every fan just constructed. No integer division
or source-moduli winding formula is used.

## EU.6. Exact dictionary to the marked w-cover

The global marked-source cover found by root is
\[
 D=w^2-3,\quad r=\frac{3-2w^2}{D^2},\quad
 X=D^2x,\ Y=D^3y,\ T=D^3t,
\]
\[
 Y^2=X^3+(3-2w^2)X^2+DTX+T^2,\quad
 G=(0,T),\quad T_c=w^2-1.
 \tag{EU.13}
\]
At either \(w_*^2=3/2\), \(D=-3/2\) is a unit and
\(dr/dw=-16w_*/9\ne0\). These are positive complex local
parameter coordinates on the present \(r\)-disc. The canonical
source/Cartier map carries every section and its actual divisor.
Its Miller functions have the exact homogeneous factors
\[
 f_{2,\rm old}=D^{-1}f_{2,\rm new},\quad
 f_{3,\rm old}=D^{-2}f_{3,\rm new},\quad
 f_{6,\rm old}=D^{-5}f_{6,\rm new}.
 \tag{EU.14}
\]
For example, the target tangent at \(G\) has slope \(D/2\), so
\(U_{\rm old}=D^{-3}[Y-T-(D/2)X]\) and
\((x-s)_{\rm old}=D^{-2}[X-D^2s]\), proving the first identity.
The chord-over-vertical factor has weight one; its actual Miller
recursion proves the other two identities, with all constants kept.
Their source and target \(f_6\) factors cancel in the ratio, so
\[
 B_{6,\rm old}=D^{-6}B_{6,\rm new},\qquad
 (q/t^3)_{\rm old}=D^6\frac{T-T_c}{T^3}.
\]
Consequently \(B_{\rm sel,old}=B_{\rm sel,new}\) under the
canonical divisor line map. This fixes the exact suspension scalar
in the global marked cover. The finite-root coordinate changes use
analytic roots of the unit \(D\) on this local disc; their reference
values and full finite characters are retained. They close as the
identity. The selected Tate branch and full theta/Cartier map are
transported by the same source isomorphism, so the fan is unchanged.
Thus the two unselected-III generators on this marked cover have
the zero return just proved, with their actual root and line closing.
