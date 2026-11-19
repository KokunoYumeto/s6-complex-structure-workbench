# Exact E6 order-three source generator at r=1/4

Working calculations by checks and root during the execution outage,
reconstructed here. No completed quotient, attachment or return is
assigned. The smallest retained whole-I1 datum is (a,b)=(6,1), cap
m=2,n=1; every actual Cartier and root character remains to be carried.

## E61. Actual source equation and group additions

For
\[
 S_r:\quad y^2=x^3+r x^2+t x+t^2,\qquad G=(0,t),
 \qquad s=\tfrac14-r,
\]
the tangent at G has slope 1/2, hence
\[
 2G=(s,-t-s/2).
\]
At s=0 it is -G, so 3G=O on every smooth source fibre. The exact
third section is
\[
 x(3G)=2t(2t+s)/s^2,\quad
 y(3G)=t(8t^2+6ts+s^2-s^3)/s^3,
\]
\[
 \tau(3G)=-2s(2t+s)/(8t^2+6ts+s^2-s^3).
\]
The normal-cone path t=s u has nonconstant central limit
\(x=2u(2u+1)\), \(y=u(2u+1)(4u+1)\). Thus the formal vanishing
at fixed nonzero t does not identify the complete source reset at t=s=0.

## E62. Literal cA2 resolution charts

Set
\[
 U=y-t-x/2,\qquad V=y+t+x/2.
\]
Then
\[
 UV=x^2(x-s),\qquad y=(U+V)/2,\quad t=(V-U-x)/2.
\]
Blow up the actual ideal (U,x). In U=xz the strict transform is
\[
 zV=x(x-s).
\]
Its remaining node is z=V=x=s=0. The two small resolutions retain
q1=x,q2=x-s and s=q1-q2. Their common Cox chart has
q1=S0T0,q2=S1T1 and s=S0T0-S1T1; the source differential never
vanishes on either stable resolution. The three marked root-order
models of UV=x*x*(x-s) retain the position of the distinct root x-s.
The third is obtained by first blowing up (U,x-s) and then resolving
the remaining x^2 A1 family. No translation action on those chambers
is inferred merely from their exceptional graphs.

## E63. Exact translation and its proper graph

On z nonzero, translation by +G has
\[
 x_+=s-x+z(z+1),\qquad
 z_+=x/z-z-1,\qquad V_+=-z x_+.
\]
These follow directly from the chord slope (y-t)/x=z+1/2.
In particular
\[
 V_+/x_+=(x_+-s)/z_+=-z.
\]
Thus its proper graph maps to the target small resolution with
\[
 [S0':S1']=[1:-z],\qquad T0'=x_+,\quad T1'=z_+.
\]
At s=0 the old exceptional component x=V=0 maps to
\(x_+=z(z+1),z_+=-z-1\) on the nodal normalization.
That normalization, x=z(z+1), maps to the remaining partial-model
node. The target resolution retains its limiting direction by the
displayed projective pair. This is the located chamber transition.

A useful full chart is
\[
 z=U/x,\quad w=V/x,\quad x=s+zw,\quad
 y=x(z+w)/2,\quad t=x(w-z-1)/2.
\]
It is smooth and retains the actual source morphism. Translation is
\[
 (z,w)\longmapsto(s/z+w-z-1,-z),
\]
and its inverse is
\[
 (z,w)\longmapsto(-w,s/w+z-w+1).
\]
At s=0 the first map has order three. Put
\(z_0=z,z_1=w-z-1,z_2=-w\), so \(z_0+z_1+z_2=-1\).
Then \(2t=z_1(s-z_0z_2)\), and translation is exactly
\[
 (z_0,z_1,z_2)\longmapsto
 (z_1+s/z_0,\ z_2-s/z_0,\ z_0).
\]
At s=0 this cyclically permutes the three components z_i=0.
Its unresolved graph at z_0=s=0 is the explicit flop graph
\(z z_+=s+z(w-z-1), w_+=-z\); both endpoint projective coordinates
must be retained.

## E64. Selected-node period and first Cartier arrow

Let rho^2=1-3r and retain rho near +1/2. The selected node is
\[
 t_+=(1-3\rho^2+2\rho^3)/27,
\]
which equals 1/54 at s=0. Its double x root and remaining simple root are
\[
 e=(2\rho+1)(\rho-1)/9,\qquad f=-(1-\rho)^2/9.
\]
In normalization y=zeta(x-e), one has
\(\zeta_G=(1-\rho)/3\) and
\(d^2=e-f=-\rho(1-\rho)/3\).
The marked multiplicative point is the literal ratio
\(P=(\zeta_G-d)/(\zeta_G+d)\), with the chosen node order.
At rho=1/2 it is a primitive cube root (the stated order gives
exp(-2pi i/3)). It is a nonzero analytic unit around this parameter
circle, of winding zero. The selected Tate node remains nondegenerate;
its source period unit also extends there. This does not yet determine
the actual M6 line multiplier through the unselected collision.

For the elementary Cartier comparison,
\[
 f_{2,G}=\frac{U}{x-s},\qquad r_2=f_{2,G}^{-1}
       =\frac{x-s}{U}=\frac{V}{x^2}.
\]
Its divisor is (2G)+(O)-2(G). These are typed rational maps between
the point line O(2G-O) and the tensor square O(G-O)^2. The M6 map
requires the full iterated Miller/Cartier arrows and all three
chambers; no scalar factor in s is discarded.

## E65. Remaining exact work

Carry translation through every source-resolution chart, construct the
actual r6 Cartier comparison with its s/t divisors, and intertwine the
m=2 root cap and the genuine ordinary closing map. The formal order-three
torsion and the local cyclic map do not supply a completed return before
those maps and the finite attachment are constructed.

## E66. Full three-point Miller factor and the retained base divisor

Put \(\lambda=-2t/s-1/2\), and define
\[
 L_+=y-t-\lambda x,\qquad L_-=y+t+\lambda x,\qquad
 x_3=2t(2t+s)/s^2 .
\]
The literal source equation gives
\[
 L_+L_-=x(x-s)(x-x_3).
\]
Consequently the three-point Miller arrow is exactly
\[
 f_{3,G}=\frac{U L_+}{(x-s)(x-x_3)}
        =\frac{xU}{L_-}
        =\frac{s xU}{sV-(s+2t)x}.
\]
On each generic elliptic fibre its divisor is \(3(G)-(3G)-2(O)\).
The full rational formula retains every vertical base factor as well;
its inverse has the opposite bundle direction.

On a fixed chart with \(t\ne0\), the formula gives
\(f_{3,G}/s\to-U/(2t)\). The actual formal coordinate of \(3G\) is
\(\tau_3=-s/(2t)+O(s^2)\). For a point \(P\) near \(O\), the tangent
line divided by the vertical line at \(2P\) has leading term
\(f_{2,P}=2/\tau_P+O(1)\); this follows directly from
\(x(P)=\tau_P^{-2}+O(1)\), \(y(P)=-\tau_P^{-3}+O(\tau_P^{-1})\),
and tangent slope \(-3/(2\tau_P)+O(\tau_P)\).
Therefore the literal iterated arrow
\[
 f_{6,G}=f_{3,G}^{\,2}f_{2,3G}
\]
has \(f_{6,G}/s\to-U^2/t\) on this fixed-\(t\) chart. Its inverse
has an actual base pole \(s^{-1}\). The section frame near \(6G\),
where \(\tau_6=-s/t+O(s^2)\), must be carried before comparing the
point line with the tensor line. No factor of \(s\) is removed here.
The full bidisc \(t=s u\) still has the retained vertical closure
described in E62; this fixed-\(t\) limit does not extend that chart.

## E67. Literal quadratic root source map

At infinity put \(q=1/t,\ X=q^2x,\ Y=q^3y\). Then
\[
Y^2=X^3+r q^2X^2+q^3X+q^4.
\]
Under \(q=z^2,\ X=z^2X',\ Y=z^3Y'\), the actual root equation is
\[
Y'^2=X'^3+z^2(rX'^2+X'+1),\qquad G'=(0,z).
\]
Its deck is \(D(z,X',Y')=(-z,X',-Y')\), and its reduced central
fibre is IV. The section \(3G'\) lies in the identity formal group.
Let \(S\) be its unique formal half satisfying \(2S=-3G'\), and put
\(R=2G'+S\). This is an actual analytic section with \(2R=G'\);
it is deck invariant by uniqueness. Therefore
\[
 A_0=t_{-R}D,\qquad A_0^2=t_{-G'}.
\]
This proves the source norm arrow for the requested \(m=2,n=1\)
cap. The M6 line lift and its full ordinary/root closing square
remain the explicitly outstanding work. No return is assigned.

## E68. The transported M6 lift and its generic I2 divisor

Write \(D_1=(G)-(O)\), \(D_6=(6G)-(O)\), and
\(r_6=f_{6,G}^{-1}\). With the convention that multiplication by
a rational function \(r\), \(\operatorname{div}r=D-E\), maps
\(\mathcal O(D)\) to \(\mathcal O(E)\), multiplication by \(r_6\)
is the actual meromorphic point-to-tensor map
\(L_6\to L_1^{\otimes6}\); its full vertical divisor is retained.
It is an invertible map on the generic elliptic fibre.
The map on \(L_1\) covering \(T:p\mapsto p-G\) has coefficient
\(f_{2,G}(p)\). The transported map is therefore exactly
\[
 B_6(p)=r_6(Tp)^{-1}f_{2,G}(p)^6r_6(p)
       =f_{2,G}(p)^6\,\frac{f_{6,G}(Tp)}{f_{6,G}(p)}.
 \tag{E68.1}
\]
Its generic-fibre coefficient divisor is \(D_6-T^*D_6\).
The additional vertical divisor of this particular meromorphic map
is computed below; it is not removed by this generic-fibre equality.

At \(s=0,\ t\ne0\), the literal inverse source map is
\((z,w)\mapsto(-w,z-w+1)\), with \(x=zw\) and
\(2t=zw(w-z-1)\). Thus \(f_2=z\) and
\[
 \frac{U(Tp)}{U(p)}=-\frac{2t}{z^3},\qquad B_6\longrightarrow4t^2.
 \tag{E68.2}
\]
This retains its nonconstant base factor.

For the generic I2 fibre fix \(s\ne0\), near the collision but
away from the other exceptional source parameters. At its generic
identity-component point put \(w=z+1\) and
\(x_0=s+w^2-w\). All limits in the following display are limits
as the actual base coordinate \(t\) tends to zero, with the
chosen smooth point varying in the source chart:
\[
 \frac{x(Tp)}t\to\frac{2w}{x_0},\qquad
 \frac{y(Tp)}t\to\frac{s-w^2}{x_0}.
\]
The exact tangent data of \(3G\) have limits
\[
 \lambda_{3,0}=\frac{1-3s}{2(1-s)},\qquad
 x_{6,0}=\frac{s^3}{(1-s)^2}.
\]
Writing \(f_{2,3G}\) for its tangent-over-vertical Miller factor,
direct substitution gives
\[
\begin{split}
f_2(p)&\to x_0/w,\qquad f_3(p)\to x_0,\\
f_3(Tp)/t&\to 2w^3/[x_0(w-s)],\\
f_{2,3G}(p)&\to x_0(1-s)/[(1-s)w-s],\\
f_{2,3G}(Tp)/t&\to
       2(1-s)(w-s)^2/(s^3x_0).
\end{split}
\]
Hence the full, unaltered coefficient has the precise leading term
\[
 \frac{B_6(p)}{t^3}\longrightarrow
          \frac{8((1-s)w-s)}{s^3}.
 \tag{E68.3}
\]
It is nonzero at the generic point. The two coefficient frames
used here are the actual rational frames of \(L_6\) at the source
identity component and target nonidentity component, away from
their horizontal section divisors. Thus the order is three.

The line \(L_6\) has degree zero on each I2 component, since
\(6G\) and \(O\) both meet the identity component. The map covers
the actual component exchange. Its Hom divisor has zero
intersection with both components; the kernel of
\(\left(\begin{smallmatrix}-2&2\\2&-2\end{smallmatrix}\right)\)
is generated integrally by the whole fibre. Equation (E68.3)
therefore gives precisely \(3F_0\) there.

## E69. Cancellation of every other finite Miller base factor

This cancellation uses the full unaltered rational function
\(f_6=f_3^2f_{2,3G}\), not merely its generic-fibre divisor.
At a finite irreducible fibre \(F_c,\ c\ne0\), the actual
translation \(T\) preserves its generic point and its component
DVR. For a smooth fibre this is its group translation; for I1 it
is the literal Tate map \(Z\mapsto P^{-1}Z\). Both fix the base
uniformizer \(t-c\). Write in that DVR
\[
 f_6=(t-c)^e u
\]
with its actual integer \(e\) and actual unit \(u\). Then
\[
 \frac{f_6(Tp)}{f_6(p)}=\frac{u(Tp)}{u(p)}
 \tag{E69.1}
\]
is a DVR unit. This explicitly cancels the same scalar and its
leading coefficient even at a fibre where \(y(3G)=0\) or
\(6G=O\). No chosen normalization of the Miller function is
being used to erase it. The equality is the pullback of the
same function under the displayed base-preserving map.

Also neither \(U\) nor \(x-s\) vanishes identically on any
finite fibre \(c\ne0\): substituting \(U=0\) gives the
intersection equation \(x^2(x-s)=0\), not that entire fibre.
Thus \(f_2\) has order zero there. Equation (E68.1) now proves
the absence of every other finite vertical factor of \(B_6\).

At IV* the line point \(6G\) meets the identity component, so
the Hom line again has zero degree on every component; its
vertical divisor is an integral whole-fibre multiple by the
primitive component-kernel calculation. The actual Hom degree
is one: P3K.14 gives \(ab\,h(G)=6\cdot1\cdot(1/6)=1\),
and pulling its map by \(T\) is the literal arrow from that
positive Hom line to the bundle-map convention of (E68.1).
Together with E68.3 and E69.1 this determines
\[
 \operatorname{div}_{\rm vertical}(B_6)=3F_0-2F_\infty.
 \tag{E69.2}
\]

Retain \(q=t-t_{\rm selected}(s)\) literally. The explicit
selected-zero section determined by these rational frames is
\[
 B_{\rm sel}=\frac{q}{t^3}\,B_6,
 \qquad \operatorname{div}_{\rm vertical}(B_{\rm sel})
             =F_{\rm selected}.
 \tag{E69.3}
\]
It has central coefficient \(4q/t\) on \(s=0,\ t\ne0\).
Dividing \(B_6\) by \(t^2\) instead retains a generic I2 zero.
The ratio of a separately prescribed linearization \(B_0\)
with \(B_{\rm sel}\) is a scalar depending on the source
parameter. Its exact parameter normalization must be carried
before identifying their named source loops. Equation E69.3
specifies a concrete rational-frame choice and does not
declare an unexamined scalar to have zero winding.

The remaining full attachment must carry this meromorphic
central limit, the three ordered-root models, and the finite
quadratic cap. The selected Tate unit \(P\) and source unit
extend at \(s=0\), by E64's explicit normalization ratio; they
are retained through their common exterior maps.

## E70. The full quadratic root Cartier correspondence

Put \(a(X')=(1+X'+rX'^2)^{1/2}\), taking its branch equal to one
at \(X'=0\). On the actual root equation introduce
\[
u=Y'+za(X'),\qquad v=Y'-za(X').
\]
Then \(uv=X'^3\), and \(z=(u-v)/(2a(X'))\). The three ordinary
minimal-resolution charts of this A2 equation are
\[
\begin{array}{c|ccc}
 &X'&u&v\\ \hline
C_{\rm mid}&ab&a^2b&ab^2\\
C_u&ab&a&a^2b^3\\
C_v&ab&a^2b^3&a .
\end{array}
\]
For example \(a_{\rm mid}=b_u^{-1}\) and
\(b_{\rm mid}=a_u b_u^2\) on their actual common open chart.
These maps retain \(z\) by the displayed inverse formula, and are
uniform in the source parameter. The deck is \((a,b)\mapsto(-a,-b)\)
in each of these charts. In the middle chart its fibre is
\(ab(a-b)=0\), up to the extending unit \(2a(ab)\).

There are exactly four deck fixed points on this resolved IV
fibre: the common triple point, the two outer-chart origins, and
the zero section O on the remaining component. Each has derivative
\((-1,-1)\). Blow up those four literal points and call the map
\(\beta\). On the exceptional curves the lifted deck is the identity
and its normal derivative is minus one; its quotient \(\pi\) is
smooth. The three old fibre components had square minus two and
each passes through the triple point and its own other fixed point.
Their strict transforms have square minus four before the degree-two
quotient and square minus two afterward. The four exceptional images
also have square minus two. The quotient fibre has three old
components of multiplicity two, triple exceptional of multiplicity
three, and three outer exceptionals of multiplicity one. These
multiplicities follow by pulling back the actual equation \(q=z^2\),
rather than by identifying a Kodaira name alone.

The invariant generic-fibre coordinate map
\[
q=z^2,\quad X=z^2X',\quad Y=z^3Y'
\]
is the original IV* Weierstrass equation. The just constructed smooth
quotient resolves it; every exceptional curve displayed has square
minus two. Its resulting birational map to the actual minimal
regular source is the unique relatively minimal resolution map over
that Weierstrass surface. Thus \(\pi\), together with this map, is
the source morphism used here.

Let \(w'=-X'/Y'\) at O. The exact formula for the section \(3G'\) is
\[
 w'(3G')=
 -\frac{2sz(2+sz^2)}
 {8+6sz^2+(s^2-s^3)z^4}.
\]
In particular it is in the identity formal group jointly in \((s,z)\).
Applying its actual formal doubling gives
\[
 w'(6G')=zL_6(s,z^2),\qquad L_6(s,0)=-s .
\]
The oddness follows also from the displayed deck, which preserves
the marked relative section. In the blowup chart \(w'=zv_0\),
the two actual section equations are
\[
 w'=zv_0,\qquad w'-w'(6G')=z(v_0-L_6(s,q)).
\]
Both acquire exactly the same exceptional factor. The point-line
frame therefore pulls back by the literal equality
\[
 \frac{w'}{w'-w'(6G')}=
 \frac{v_0}{v_0-L_6(s,q)}.                         \tag{E70.1}
\]
At the other three blowup centres both section divisors are absent.
Consequently, on the full common surface,
\[
 \beta^*\mathcal O(6G'-O)
       =\pi^*\mathcal O(6G-O)                     \tag{E70.2}
\]
with its specified coefficient arrow E70.1. This equality includes
all exceptional curves and remains valid at \(s=0\); the sections
coincide there but their two divisor pullbacks still have the same
exceptional coefficient. No untyped pullback of a point line is
used.

## E71. The line lift and its exact norm on that root

Under the literal root coordinate scaling, a tangent or chord line
has weight \(z^{-3}\) and a vertical line has weight \(z^{-2}\).
The actual factors therefore satisfy
\[
 f_{2,\mathrm{old}}=z^{-1}f_2',\qquad
 f_{3,\mathrm{old}}=z^{-2}f_3',\qquad
 f_{6,\mathrm{old}}=z^{-5}f_6'.
\]
The same base factor appears at the source and target of the last
factor, so E68.1 gives
\[
 B_{6,\mathrm{old}}=z^{-6}B_6',\qquad
 B_{\rm sel}'=h\,z^{-2}B_6',
 \qquad h=1-t_{\rm selected}(s)z^2.                \tag{E71.1}
\]
This retains the complete selected-height unit \(h\).
The Cartier map E70.2 pulls the generic source Hom divisor to
the actual root line. Equation E69.2 and \(q=z^2\) then give
order two for \(B_6'\) on every reduced-IV component, so the
coefficient \(z^{-2}B_6'\) is an invertible line map there.
On \(s=0,z\ne0\), E68.2 and the exact weights in E71.1 give
\[
 B_6'=4z^2,\qquad B_{\rm sel}'=4h.                 \tag{E71.2}
\]

These are statements about the actual line frames of E70.1.
They extend jointly over \(s=z=0\): in any local Hom-line frame
the rational map and its inverse have order zero at every
codimension-one prime. Horizontal divisors cancel by the typed
generic-fibre comparison, the \(z=0\) component orders were just
computed, and the \(s=0\) order is zero by E71.2. The root total
space is smooth in the explicit uniform charts above. Its local
normal ring is the intersection of these height-one DVRs, which
extends both the map and its inverse. This supplies the full
invertible root lift, rather than only its central value.

The source half-translation is also literal. Let \(S\) be the
unique formal section satisfying \(2S=-3G'\), and put \(R=2G'+S\).
The formal inverse of multiplication by two is analytic over the
displayed bidisc, since its linear coefficient is two. Then
\(2R=G'\), and \(D(R)=R\) by this uniqueness and the invariance of
the actual section \(G'\). The source map
\[
 A_{\rm src}=t_{-R}D
\]
has square \(t_{-G'}\).

For the line square use the actual extending lift \(F\) of
\(t_{-R}\) on \(N_6=\mathcal O(6G'-O)\). It is constructed by the
chord/vertical ratio for \((6G',R)\), followed by the actual
integral whole-fibre divisor map. The vertical divisor is a
whole fibre because N6 has zero degree on every root component;
the retained formal/Cartier chart E70.1 fixes its local frame.
As in the explicit finite-character norm construction of F44,
this yields an invertible lift on the bidisc, with its actual
base scalar retained.

Here the character can be read without dropping it. The line N6
on the reduced IV fibre is trivial because both point divisors
restrict to O. At the O chart E70.1 its deck weight is one, and
it is one in the other three trivial divisor charts. Thus
\[
 DFD^{-1}=c(s,z)F,\quad
 c(s,-z)c(s,z)=1,\quad c(s,0)=1.
\]
Put \(\gamma=\log c\), with zero value at \(z=0\), and replace
F by \(F_1=e^{\gamma/2}F\). The displayed map has
\(D F_1D^{-1}=F_1\), since
\(e^{\gamma(s,-z)/2}c/e^{\gamma(s,z)/2}=1\).
The ratio
\[
 a(s,z)=F_1^2/B_{\rm sel}'
\]
is an invertible base function, invariant under D. Its actual
analytic square root on the bidisc rescales F1 to
\(F_2=a^{-1/2}F_1\), giving exactly
\[
 A_0=F_2D,\qquad A_0^2=B_{\rm sel}',\qquad
 [A_0,B_{\rm sel}']=1.                              \tag{E71.3}
\]
The permitted finite line character multiplies A0 by
\((-1)^d\) and remains in the boundary marking. Its square is
one, so E71.3 is unchanged. For the literal scalar root
\(\lambda=r_{\rm sc}^2\), put
\(A=r_{\rm sc}A_0,\ B=r_{\rm sc}^2B_{\rm sel}'\).

This proves the actual quadratic cap source and line norm through
the source-parameter disc, with the full Cartier map and selected
unit. The ordinary-to-cap overlap still must be matched to the
prescribed reference cochain and to the unselected cA2 chambers
before a completed source-loop return is assigned.

## E72. The marked global source rescaling

The parent's exact global marked-node coordinates use
\[
D=w^2-3,\quad \rho=w^2/D,\quad r=(3-2w^2)/D^2,\quad
X=D^2x,\ Y=D^3y,\ T=D^3t .
\]
The source is
\[
Y^2=X^3+(3-2w^2)X^2+DTX+T^2,\quad G=(0,T),\quad
T_{\rm selected}=w^2-1.
\]
Here write
\(S=(w^2-1)(w^2+3)/4=D^2s\).
The exact common local equations are
\[
U=Y-T-DX/2,\quad V=Y+T+DX/2,\quad UV=X^2(X-S).
\]
In \(U=Xz,\ V=Xw_{\rm loc}\), the inverse source translation is
\[
(z,w_{\rm loc})\mapsto
(-w_{\rm loc},S/w_{\rm loc}+z-w_{\rm loc}+D).
\]
The E68 calculation has the general coefficient
\[
 \frac{B_6}{T^3}\ \longrightarrow\
 \frac{8((D^2-S)w_{\rm loc}-DS)}{S^3}
\]
at the generic I2 component. At \(D=0,S=3\) this is
\(-8w_{\rm loc}/9\), nonzero at its generic point.

The full Miller maps scale
\(f_{2,\rm old}=D^{-1}f_{2,\rm new}\) and
\(f_{6,\rm old}=D^{-5}f_{6,\rm new}\). Thus
\(B_{6,\rm old}=D^{-6}B_{6,\rm new}\), whereas
\(q_{\rm old}/t_{\rm old}^3=D^6q_{\rm new}/T^3\).
Their product cancels these precise powers:
\[
 B_{\rm sel,old}=q_{\rm new}B_{6,\rm new}/T^3 .
\]
No winding of D has been removed by a logarithm. The complete
parameter-generator catalogue and its coordinate domains are
being checked separately by root.

## E73. The two retained Miller fibres and the complete central line

The tangent at the actual third section has the following exact
coefficient. Define
\[
\Delta=8t^2+6st+s^2-s^3,\qquad
N=48t^3+48st^2+2s^2(7-4s)t+s^3(1-3s).
\]
Then \(y_3=t\Delta/s^3\), and
\[
\lambda_3=\frac{3x_3^2+2rx_3+t}{2y_3}
          =\frac{N}{2s\Delta}.
\]
In particular the full, unrescaled tangent factor is
\[
 f_{2,3G}=
 \frac{2s\Delta\{2s\Delta(y-y_3)-N(x-x_3)\}}
 {4s^2\Delta^2(x+r+2x_3)-N^2}.                    \tag{E73.1}
\]
The two polynomials satisfy
\[
 \operatorname{disc}_t\Delta=4s^2(1+8s),\qquad
 \operatorname{Res}_t(\Delta,N)=-256s^9.          \tag{E73.2}
\]
Thus for every sufficiently small nonzero \(s\), the two distinct
\(\Delta\)-fibres each occur with coefficient one in the vertical
divisor of the literal function \(f_6=f_3^2f_{2,3G}\).
They are exactly the two ordinary fibres at which \(3G\) is
two-torsion and \(6G=O\). At such a fibre the denominator in
E73.1 is \(-N^2\), while its remaining numerator is
\(-N(x-x_3)\), both nonzero at the generic point. No scalar
leading coefficient has been suppressed.

At a finite fibre with \(t\Delta\ne0\), \(3G\) is a finite
point with nonzero \(y_3\); the displayed tangent and vertical
functions specialize to a nonzero rational function. The same
holds for the chord formula E66. The only remaining finite
vertical valuation is the one on the nonidentity component of
the generic \(I_2\). E68's actual component charts give
order three for \(f_6\) there and order zero on the identity
component. If \(C_{\rm old}\) denotes that component, this proves
on the finite-base surface the full equality
\[
 \operatorname{div}(\Delta r_6)
       =D_6-6D_1-3C_{\rm old}.                  \tag{E73.3}
\]
It gives a typed invertible Cartier map
\[
 \Delta r_6:\ M_6\longrightarrow
             M_1^{\otimes6}\otimes\mathcal O(3C_{\rm old}).
 \tag{E73.4}
\]
In the joint source family the coefficient of \(r_6\) has
parameter order minus one by E66. The precise annular map used
to extend E73.4 is therefore \(s\Delta r_6\), not \(r_6\) or
\(sr_6\). The two \(\Delta\)-fibres remain in that arrow. Their
scalar factors cancel literally between source and target in
E68.1 because the translation fixes \(s,t\).

For the row resolution of E63, \(C_{\rm old}\) is the Cartier
surface \(T_0=0\). Its central divisor is \(C_1+C_2\), where
\[
 C_0:\ w=z+1,\qquad C_1:\ z=0,\qquad C_2:\ w=0
 \quad (s=0).
\]
The central parameter limit of the full annular map is
\[
                  s\Delta r_6\longrightarrow
                         -\,\frac{8t^3}{U^2}.   \tag{E73.5}
\]
On the finite central source the actual flex function has
\(\operatorname{div}U=3D_1+2C_1+C_2\).
Adding the target divisor in E73.4 to the divisor of E73.5
therefore gives, coefficient by coefficient,
\[
\begin{split}
 \operatorname{div}(-8t^3/U^2)
       +6D_1+3(C_1+C_2)
 &=3F_0-C_1+C_2\\
 &=3C_0+2C_1+4C_2.                              \tag{E73.6}
\end{split}
\]
This is an equality of actual Cartier frames. At infinity its
completion is the E70 point-line map: the source and root
equations \(v_0\) and \(v_0-L_6(s,q)\) coincide at \(s=0\).
Hence no additional component correction is inserted at that
cap. As an independent check of the whole-fibre coefficient,
\(\tau(6G)=2s\Delta/N+O(\Delta^2)\) at each of the two
\(\Delta\)-fibres. Both intersections with \(O\) are simple;
there are no others, since the resolved \(I_2\) value and the
infinity value \(-s\) are nonzero. Thus \(M_6\cdot O=2-(-1)=3\).
This degree is retained by the above Cartier gluing and agrees
with the coefficient three in E73.6.

Consequently the completed central line in these exact frames is
\[
 M_6|_{s=0}=\mathcal O(3F_0-C_1+C_2),\qquad
 (M_6|_{s=0})^2=-6.                              \tag{E73.7}
\]
The component degrees are \((0,3,-3)\). Translation \(T=-G\)
carries \(C_0\) to \(C_2\), \(C_1\) to \(C_0\), and the
flopped \(C_2\) to \(C_1\). With the ordered coefficients
\((3,2,4)\), the pullback target coefficients are \((4,3,2)\).
The literal central coefficient \(4q/t\) in E69.3 therefore
has Hom divisor
\[
 F_{\rm selected}-F_0+
  \bigl((4,3,2)-(3,2,4)\bigr)
       =F_{\rm selected}-3C_2.                 \tag{E73.8}
\]
In particular its pole is located on the actual compact curve
which is resolved in the next chart comparison.

## E74. Both endpoint charts of the actual translation flop

Use the source coordinates \((z,w,x)\) of E63, with
\[
        s=x-zw,\qquad t=x(w-z-1)/2.
\]
The compact curve \(C_2\) is \(w=x=0\). In the other chart of
the first blowup put \(a=1/z\). Its actual normal coordinates
are
\[
       w_\infty=zw,\qquad x_\infty=zx,\qquad
       s=a x_\infty-w_\infty.                   \tag{E74.1}
\]
Indeed the \(U\)-chart of that blowup has
\(x=Ua\), \(V=Ua^2(Ua-s)\); hence
\(x_\infty=U\), \(w_\infty=Ua-s\). Equation E74.1
is the full transition of \(\mathcal O(-1)\oplus\mathcal O(-1)\),
including both base functions \(s,t\).

The standard opposite ruling has finite chart
\[
       h=x/w,\qquad \alpha=w,\qquad \beta=zw.
\]
Its exact map into the target resolved source is
\[
\begin{split}
 z_{\rm new}&=-\alpha,\\
 w_{\rm new}&=h-\alpha+1,\\
 x_{\rm new}&=\alpha^2-\alpha-\beta,\\
 s&=h\alpha-\beta,\qquad
 t=h(\alpha^2-\alpha-\beta)/2.                  \tag{E74.2}
\end{split}
\]
The inverse on this target chart is
\[
 \alpha=-z_{\rm new},\quad
 h=w_{\rm new}-z_{\rm new}-1,\quad
 \beta=h\alpha-s.
\]
Thus it is precisely translation by \(-G\), with the original
source parameter and elliptic-base coordinate retained.

To include \(h=\infty\), put
\[
       k=1/h,\qquad A=h\alpha,\qquad B=h\beta,
       \qquad D=1+k-k^2A.
\]
The target \(S_1=1\) source chart has coordinates
\((a,b,c)=(S_0,T_0,T_1)\), so that
\(x_{\rm new}=ab,z_{\rm new}=ac,V_{\rm new}=b\)
and \(s=ab-c\). The exact map and inverse are
\[
\begin{aligned}
 a&=k/D,& b&=D(-B-A+kA^2),& c&=-DA,\\
 E&=1-a-a^2c,&
 k&=a/E,& A&=-cE,& B&=(c+ac^2-b)E .
\end{aligned}                                  \tag{E74.3}
\]
Here \(D\) and \(E\) are units near the whole missing endpoint,
and \(DE=1\). Direct substitution proves that the two displayed
maps are inverse, preserve \(s,t\), and agree with E74.2.
This chart carries the point at which \(G\) meets the target
component. No division by a vanishing \(w\) or projective
coordinate is left at that endpoint.

## E75. The full weight-minus-three line and associated-node arrow

On the source finite chart a local frame of
\(M_1^{\otimes6}\otimes\mathcal O(3C_{\rm old})\)
is \(x^{-3}\). Near \(z=\infty\) it is
\((zx)^{-3}\), with the literal \(M_1\) divisor frames
carried on their overlaps. Its degree on \(C_2\) is minus
three. For a coefficient \(v\) in the original point-line
rational frame define
\[
             \xi=(s\Delta r_6)(p)\,x^3v.        \tag{E75.1}
\]
Use the same typed definition at the target. With the scalar
\(\lambda\) retained, the actual suspension is
\[
 v'=\lambda\,\frac q{t^3}\,
       f_2(p)^6\,\frac{r_6(p)}{r_6(Tp)}\,v .
\]
The exact source formulas give
\(f_2=x/w\) and \(x_{\rm new}=2tw/x\). Therefore
\[
                        \xi'=8\lambda q\,w^{-3}\xi .
 \tag{E75.2}
\]
Every factor \(s,\Delta,t,x\) in this calculation has been
substituted; none is replaced by a scalar normalization.
On the target endpoint chart E74.3 the section \(G\) has
equation \(a=0\). Its \(M_1^{\otimes6}\) frame is \(a^{-6}\);
together with the old-component frame \(b^{-3}\), its ratio
to \((ab)^{-3}\) is \(a^{-3}\). This is the exact positive
degree-three target line transition, including the unit
\(D\) relating \(a\) and \(k\).

There is a literal common Cox description of E75.2. Write
\[
 u=(u_0,u_1),\quad t_{\rm Cox}=(t_0,t_1),\qquad
 (z,w,x)=(u_1/u_0,u_0t_0,u_0t_1),
\]
with auxiliary weights \(+1,+1,-1,-1\) and line coefficient
of weight minus three. The source chart is \(u_0=1\);
the target chart is \(t_0=1\). Passing between them uses
the auxiliary scalar \(w\) and sends the line coefficient
to \(w^{-3}\xi\). Thus the primitive map is the actual
identity in the common Cox coordinates, from the source
ruling with line degree minus three to the target ruling
with line degree plus three. Its multiplying base factor
is exactly \(8\lambda q\), as in E75.2.

For the corresponding associated node introduce \(\xi^\vee\)
with \(\xi\xi^\vee=q\), carrying the opposite auxiliary and
physical weights. The same chart arrow preserves that
equation and the physical line circle, with \(\xi^\vee\)
multiplied by the reciprocal factor. This supplies the
actual weight-three local model with its source parameters
and scalar. A compact period strip, its finite-root end,
and the oriented free boundary still have to be attached
before any characteristic pair or return is assigned.

## E76. The actual charged chart and its two finite norm faces

At this collision the selected height
\(q=t-t_{\rm selected}(s)\) is a unit: \(q(0,0)=-1/54\).
Thus the last associated-line equation in E75 has both line
coordinates nonzero. In particular it introduces no additional
zero of the selected height at the unselected collision.

In the common Cox coordinates of E75 the two original source
functions are the invariant polynomials
\[
 s=u_0t_1-u_1t_0,\qquad
 2t_{\rm base}=t_1(u_0^2t_0-u_1-u_0).           \tag{E76.1}
\]
The source stable open set is \(u\ne0\); the target stable
open set is \(t_{\rm Cox}\ne0\). With the nonzero line
coefficient \(\xi\) of auxiliary weight minus three, set
\(\xi=1\). The required auxiliary scalar is a cube root of
\(\xi\); its three choices give precisely
\[
 (\mathbb C^2_u\oplus\mathbb C^2_t)/\mu_3,\qquad
 \zeta\cdot(u,t)=(\zeta u,\zeta^{-1}t).
 \tag{E76.2}
\]
Both stable open sets embed by this actual gauge map and their
union is the complement of the origin. All source functions
in E76.1 descend, including at either coordinate plane.

The physical line scalar \(\xi\mapsto d\xi\), in this chart,
is exactly
\[
 (u,t)\longmapsto(d^{1/3}u,d^{-1/3}t)
                     \pmod{\mu_3}.             \tag{E76.3}
\]
Different cube roots give the same quotient map. The actual
finite end has \(d=8\lambda q(s,t_{\rm base})\), retaining
its selected-height unit and scalar. E76.1 is invariant under
E76.3, so the parameter and source-base functions are unchanged,
also for this nonconstant \(d\). The physical circle is the
same formula with \(d=e^{i\phi}\), not a separately chosen
circle on the charged link.

The source and target Fubini--Study norms, before setting
\(\xi=1\), are
\[
 N_u=|\xi|\,\|u\|^3,\qquad
 N_t=|\xi|/\|t\|^3,\qquad
 R=\|u\|\,\|t\|,\qquad N_u=R^3N_t.              \tag{E76.4}
\]
Every displayed expression is invariant under the actual
auxiliary action. For a radius \(r_0>0\), the full finite faces
\[
\begin{array}{ll}
 N_u=r_0^3,\ R\le r_0^2:
       &S^3_u(r_0)\times D^4_t(r_0)\,/\,\mu_3,\\
 N_t=r_0^{-3},\ R\le r_0^2:
       &D^4_u(r_0)\times S^3_t(r_0)\,/\,\mu_3
\end{array}                                    \tag{E76.5}
\]
are literal in the \(\xi=1\) gauge. On their common stable
portion the positive physical rescaling
\[
                       d=(R/r_0^2)^3          \tag{E76.6}
\]
carries the first norm equation to the second, preserving
both E76.1 functions. It is smooth and invertible for \(R>0\).
The two cores \(t=0\) and \(u=0\) are retained as boundary
faces; E76.6 is not extended through them. The actual
\(8\lambda q\) factor is compared on that same free collar
by the explicit positive ratio of the two Hermitian norms;
its phase is retained by E76.3.

For \(|8\lambda q|<1\), the forward real action in E76.3
decreases \(\|u\|\) and increases \(\|t\|\).
It enters the product ball through the first face of E76.5
and exits through the second. This specifies the chronological
source and target faces; the signed global period-strip
boundary must still carry the outside source and the
quadratic-root end before it is identified with the completed
return.

The union of the two entire product faces is the round
charged link \(S^7/\mu_3\), after the explicit positive
corner rounding. Its physical quotient is described without
changing its circle: conjugate the two \(t\) coordinates.
Then E76.3 is common multiplication by \(e^{i\phi/3}\)
on the four complex coordinates \((u,\bar t)\).
The two conjugations preserve real orientation, and the
physical associated line on the quotient is
\(\mathcal O_{\mathbb P^3}(-3)\): the explicit map sends a
charged point \(p=(u,\bar t)\) to \(p^{\otimes3}\) in the
cube of its tautological line. It is independent of the
\(\mu_3\) representative and sends the physical action to
multiplication by \(e^{i\phi}\) on that vector. On this local, positively
oriented charged link its characteristic integrals are
\[
                 (x^3,p_1x)=(-27,-12).          \tag{E76.7}
\]
Here the Euler sequence gives \(p_1(T\mathbb P^3)=4H^2\)
and the actual physical representation gives \(x=-3H\).
Equation E76.7 evaluates this specified boundary only.
Its sign and multiplicity in the global source return
are not assigned by this calculation.

## E77. The reference-relative quadratic-cap annular square

The source parameter in this section is \(s\); the cap base is
\(q_\infty=1/t_{\rm base}\). Choose a fixed annulus in
\(q_\infty\) on which every source fibre is smooth, uniformly
for \(s\) in its small disc. The cap data of E70--71 extend
on that full disc. In particular the actual point-line map
\(I_z\) in E70 is available on each root sheet, with
\(I_{-z}=D I_z\), and the extending line translation \(F_2\)
satisfies \(F_2^2=B'_{\rm sel}\) and commutes with \(D\).
Fix the scalar root \(r_{\rm sc}\), \(\lambda=r_{\rm sc}^2\),
and the prescribed character \((-1)^d\). The cap action is
\[
 A=(-1)^d r_{\rm sc}F_2D,\qquad
 B=\lambda B'_{\rm sel},\qquad A^2=B.            \tag{E77.1}
\]
These are the actual maps from E71; the full \(h\), Miller
factors and point-line frames remain in them.

Cover the annulus by two angular sectors and write
\[
 \ell_\alpha=\frac{\log_\alpha q_\infty}{2\pi i},
 \quad z_\alpha=e^{\pi i\ell_\alpha},\quad
 c=\frac{\log r_{\rm sc}}{2\pi i}+\frac d2 .
\]
Use the Lie cover of the rigidified degree-zero line
extension on these smooth elliptic fibres. Its physical
scalar period is denoted by \(\delta\). Let
\(f_\alpha=\operatorname{Log}_\alpha F_2\) and
\(b_\alpha=\operatorname{Log}_\alpha B\). These logarithms
are logarithms of the full lifted source translations;
their scalar coordinates include the exact line morphisms,
rather than an independently chosen fibre scalar.

On an overlap write
\[
 \ell_\beta=\ell_\alpha+k_{\alpha\beta},\qquad
 f_\beta=D_*^{k_{\alpha\beta}}f_\alpha+
                                      \Pi_{\alpha\beta}.
\]
The actual period vector \(\Pi_{\alpha\beta}\), suspension
integer \(j_{\alpha\beta}\), and full period vector
\(\Lambda_{\alpha\beta}\) have the integer coefficients of
the prescribed reference annular map at \(s=s_*\). Their
period functions vary holomorphically with \(s\). Define
\[
\begin{split}
 \Phi_\alpha&=
 \operatorname{Exp}\bigl(\ell_\alpha f_\alpha+
                \ell_\alpha c\delta+h_\alpha\bigr)I_{z_\alpha},\\
 h_\beta-D_*^{k_{\alpha\beta}}h_\alpha
   &=-\ell_\alpha\Pi_{\alpha\beta}
         +j_{\alpha\beta}b_\beta+\Lambda_{\alpha\beta}.
\end{split}                                                   \tag{E77.2}
\]
The reference logarithms satisfy this equation at \(s_*\).
It includes both components of the angular overlap, the
finite character, every elliptic period and the complete
suspension deck of that reference.

For an explicit solution, identify the Lie bundles by
\(I_z\) on the ordinary annulus and take a holomorphic
frame there. Extend the reference vectors in that frame.
Subtract their differences from the right-hand side of
E77.2 to obtain the holomorphic additive cocycle
\(E_{\alpha\beta}\), zero at \(s_*\). With a fixed sector
partition \(\chi_\beta\), put
\[
 k_\alpha=-\sum_\beta\chi_\beta E_{\alpha\beta},
 \qquad \omega=\bar\partial k_\alpha,\qquad
 v(q_\infty,s)=\frac1\pi\int
                  \frac{\omega(w,s)}{q_\infty-w}\,dA(w).
 \tag{E77.3}
\]
A cutoff on a slightly larger annulus makes this literal
integral available. On the smaller fixed annulus
\(\bar\partial v=\omega\).
Adding \(k_\alpha-v\) to the extended reference logarithm
solves E77.2, is holomorphic in \(s\), and is zero at the
reference parameter. Finite averaging acts on these vector
corrections only; it leaves the specified integral periods
and finite character in place.

Subtracting \(k_{\alpha\beta}\) times the target-sheet cap
logarithm from the two arguments in E77.2 leaves precisely
\(j_{\alpha\beta}b_\beta+\Lambda_{\alpha\beta}\).
Exponentiation gives the exact, directed squares
\[
 \Phi_\beta=A^{k_{\alpha\beta}}
                      B^{j_{\alpha\beta}}\Phi_\alpha,\qquad
 \Phi_\alpha B=B\Phi_\alpha .                    \tag{E77.4}
\]
The negative Lie argument followed by \(I_z^{-1}\) is its
inverse. This constructs the whole reference-relative
ordinary/root overlap over the source-parameter disc.
It does not extend an annular logarithm through the cap
centre; E70--71 provide the separate extending cap charts.
Every function of \(s\) here is defined on its disc, so this
part of the source-parameter closing is the identity.

The remaining attachment is now specifically the finite
period strip through the unselected translation flop. It
must use E74--76 at its two ends, E77.4 at infinity, and
the selected-node point-line and fan charts from E64.
The \(u=0\) and \(t_{\rm Cox}=0\) core faces and their
chronological identification must be counted before the
local oriented charged boundary of E76 is inserted into
the completed-return characteristic equation.

## E78. The exact central cyclic norm and the located compactness wall

On \(s=0,\ t_{\rm base}\ne0,t_{\rm selected}\), the actual
source translation satisfies \(T^3=\mathrm{Id}\). In the
central point-line trivialization of E73 its coefficient is
\(4\lambda q/t_{\rm base}\), independent of the source
point. Hence the chronological three-step norm is exactly
\[
             B^3=(4\lambda q/t_{\rm base})^3,\qquad
             q=t_{\rm base}-t_{\rm selected}(0).
 \tag{E78.1}
\]
Equivalently the primitive common-Cox line arrow in E75
has three-step scalar \((2t_{\rm base})^{-3}\); multiplying
its three retained factors \(8\lambda q\) gives E78.1.
This equality retains the graph-to-next-graph reset and
cannot be replaced by three copies of a constant chart
identification.

There is a concrete obstruction to the naive central
infinite-cyclic quotient at fixed nonzero \(\lambda\).
For a unit complex number \(c\), put
\[
        t_{\rm base}
          =\frac{-4\lambda\,t_{\rm selected}(0)}
                         {c-4\lambda}.
 \tag{E78.2}
\]
For sufficiently small fixed \(\lambda\) these are smooth
base values near zero and different from zero and the
selected node. They satisfy
\(4\lambda q/t_{\rm base}=c\).
Choose \(c^3\) with irrational angular coordinate.
Then \(B^3\) fixes the elliptic source point and multiplies
its nonzero line coefficient by \(c^3\). Its orbit is dense
in the physical line circle and is not closed. The orbit
quotient therefore is not \(T_1\), hence is not Hausdorff.
This uses the actual action in E78.1, not a model obtained
by discarding its base factor.

The located wall does not assign a parameter return.
It records the additional requirement on the finite real
strip: the three chronological source charts and their
cyclic norm must be carried through its cut, together with
the local charged face and the root overlap E77.
No compact constant-scalar central quotient is claimed.

## E79. The chronological graph-to-next-graph reset

The target finite chart in E74 is an actual source chart
for the next period. Its next common Cox representative is
\[
\begin{split}
 u_{\rm next}&=(1,-\alpha),\\
 t_{\rm next}&=(h-\alpha+1,\ \alpha^2-\alpha-\beta),\\
 \xi_{\rm next}&=\xi_{\rm target}.
\end{split}                                                     \tag{E79.1}
\]
The equality for the line coefficient uses the same target
frame \((s\Delta r_6)x_{\rm new}^3\) in E75.1.
At the missing projective endpoint the reset instead uses
the actual \(S_1=1\) chart E74.3 and its \(a^{-6}b^{-3}\)
frame. Thus E79.1 does not discard the endpoint unit \(D\).

The centre of the next flop, in the first target chart, is
\[
 h-\alpha+1=0,\qquad \alpha^2-\alpha-\beta=0.
 \tag{E79.2}
\]
It lies on \(s=0\). Pulled through the first graph on its
common open set, it is the original component
\(C_0:\ w=z+1\). Its projective completion includes the
ordinary zero-section chart of the global source.
The third chronological centre is the remaining component
\(C_1\). Consequently the full three-step strip must
retain all three global component charts and their actual
point-line frames. A repeated identification of only the
single local \(C_2\) chart does not implement E79.1.
The explicit scalar obstruction E78 is the independently
computed norm of that complete chronological cycle.

## E80. The complete central two-step core coefficient

Put \(d=8\lambda q(0,0)\). Start on \(C_1\) with its
finite coordinate \(w\). The two regular translations
through \(C_0\) have the actual coordinates
\[
 (0,w)\longmapsto(-w,1-w)
            \longmapsto(w-1,0).
\]
On their common open set their full line coefficient is
\[
 \xi_{\rm final}
       =\frac{d^2}{w^3(1-w)^3}\,\xi_{\rm initial}.
 \tag{E80.1}
\]
The target \(C_1\) core of the first flop has coordinate
\(h=w-1\). Consequently the two-step outside map closes
its base to the original \(C_2\) by \(z_{\rm final}=h\),
with coefficient
\[
                   -\,\frac{d^2}{h^3(h+1)^3}.  \tag{E80.2}
\]
The two poles occur at the actual component-intersection
points. They remain in the next chronological charts.

The \(w=\infty\) endpoint has no unresolved scalar.
On \(C_1\), E75's actual \(a^{-6}b^{-3}\) frame gives
\(\xi_{1,\infty}=w^{-3}\xi_{1,\rm finite}\).
On \(C_2\), E74.1 gives
\(\xi_{2,\infty}=(w-1)^3\xi_{2,\rm finite}\).
Equation E80.1 becomes exactly
\[
                      \xi_{2,\infty}
                             =-d^2\xi_{1,\infty}.              \tag{E80.3}
\]
This includes the zero-section chart lying on the
intermediate component \(C_0\).

In the charged gauge \(\xi=1\), write the target core
vector as \(t=(t_0,t_1)\), with \(h=t_1/t_0\).
Its target ruling coefficient is \(t_0^{-3}\); the
source ruling coefficient at \(u=(u_0,u_1)\) is \(u_0^3\).
Substitution in E80.2 gives the exact lifted core map
\[
 u=\kappa_d\,\frac{(t_0,t_1)}{t_1(t_0+t_1)},
              \qquad \kappa_d^3=-d^2.           \tag{E80.4}
\]
Changing the chosen cube root changes the representative
by the actual \(\mu_3\) action. The formula is equivariant
both for that action and for the physical circle in
E76.3. Its two excluded hyperplanes are precisely the
two retained intersection poles of E80.2. Thus it gives
a directed seam with its full divisor, not a constant
identification of the two charged cores.

## E81. An actual two-parameter Tate morphism with the full point line

This section concerns the smooth source annulus near the unselected
fibre. Its extension to the ordered model retains the Cartier
factors below. Define the analytic Tate parameter \(Q\) by the
inverse of the Tate \(j\)-series, with its branch tending to zero.
The original Weierstrass invariants are
\[
 c_4=16(r^2-3t),\quad
 c_6=-64r^3+288rt-864t^2,\quad
 \Delta_{\rm W}=-16t^2
       \{r^2(4r-1)+(4-18r)t+27t^2\}.             \tag{E81.1}
\]
Here \(\Delta_{\rm W}\) is the Weierstrass discriminant;
it is distinct from the retained Miller polynomial \(\Delta\)
of E73. Since \(c_4\) is a unit, the inverse series is analytic
and
\[
 Q=t^2(t-t_-(s))\,u_Q(s,t),\qquad u_Q(0,0)\ne0.
\]
This follows from E81.1 and the simple unselected discriminant
branch \(t_-(0)=0,\ t_-'(0)=-1/2\); the other discriminant
branch remains the selected node.

Let \((x_{\rm T},y_{\rm T})\) be the actual Tate Weierstrass
coordinates, with
\(y_{\rm T}^2+x_{\rm T}y_{\rm T}
 =x_{\rm T}^3+a_4(Q)x_{\rm T}+a_6(Q)\).
Write \(E_4(Q),-E_6(Q)\) for their invariants and choose
the analytic unit \(a\), \(a(0,0)=1\), with
\(a^4=c_4/E_4(Q)\). The equality of \(j\) and the value
at the origin give \(a^6=c_6/(-E_6(Q))\).
The complete Weierstrass map is
\[
 x=a^2(x_{\rm T}+1/12)-r/3,\qquad
 y=a^3(y_{\rm T}+x_{\rm T}/2).                  \tag{E81.2}
\]
Both coordinates and their inverse are holomorphic with unit
Jacobian; this is the actual source isomorphism used here.

In the nodal Tate chart \((Z,W)\), \(Q=ZW\), the convergent
Tate series give
\[
 x_{\rm T}=Z+W+O((Z,W)^2),\qquad
 y_{\rm T}=-W+O((Z,W)^2).
\]
Their Jacobian is minus one, so they have an analytic inverse.
Apply that inverse to the actual section \(G=(0,t)\), and
define \(P=Z(G)\). Direct differentiation of E81.2 at \(t=0\)
gives the full leading coefficient
\[
 \frac Pt\bigg|_{t=0}
       =\frac{1+2\sqrt r}{16r^2},
 \quad
 \frac{W(G)}t\bigg|_{t=0}
       =\frac{1-2\sqrt r}{16r^2}.               \tag{E81.3}
\]
The square root is the one near \(1/2\). Consequently
\[
 R=\frac{Q}{P^2}=\frac{W(G)}P
\]
is analytic on the full bidisc, and
\[
 R(s,0)=\frac{1-2\sqrt r}{1+2\sqrt r},\qquad
 P=2t+\text{higher terms},\quad
 R=s+2t+\text{higher terms}.                    \tag{E81.4}
\]
The last \(t\) derivative also follows from the exact identity
\(P^3=Q\) on \(s=0\): the actual section has order three,
and the valuations \(\operatorname{ord}_tP=1\),
\(\operatorname{ord}_tQ=3\) select precisely that period.
Thus \((P,R)\) has Jacobian two in \((t,s)\) and is an
analytic coordinate system. The inverse functions retain
the original \(s,t\); in particular
\[
 Q=P^2R,\qquad R-P=s\,u_s(P,R),\quad u_s(0,0)=1.
 \tag{E81.5}
\]
No fixed source-parameter level is replaced by another
one: all later appearances of \(s,t,q\) use these inverse
functions.

Use the convergent theta product
\[
 \Theta_Q(Z)=(1-Z)\prod_{\nu\ge1}
                       (1-Q^\nu Z)(1-Q^\nu/Z),
 \qquad f_P(Z)=\frac{\Theta_Q(Z/P)}{\Theta_Q(Z)}.
\]
Its exact identities give \(f_P(QZ)=P f_P(Z)\). The
actual meromorphic point-line section of \(M_1\) is
represented by \(f_P\). Thus multiplication by the full
Weierstrass Miller function \(f_2\), covering \(Z\mapsto
P^{-1}Z\), has Tate coefficient
\[
 \eta=f_2(Z)\frac{f_P(P^{-1}Z)}{f_P(Z)}
      =a\,\Theta'_Q(1)
                  \frac{\Theta_Q(P^2)}{\Theta_Q(P)^2}.
 \tag{E81.6}
\]
The first expression is a holomorphic function on the compact
smooth elliptic fibre with no divisor, hence is constant.
Its exact value follows at \(O\) from
\(f_2=-\tau^{-1}+O(1)\), \(\tau=-x/y\), and
\((Z-1)/\tau=a\) in E81.2. The theta inversion identity
\(\Theta_Q(Z^{-1})=-Z^{-1}\Theta_Q(Z)\) gives the displayed
sign.

Every factor in the right side of E81.6 extends as a unit
in \((P,R)\). For example the potentially nontrivial first
factor of \(\Theta_Q(P^2)\) is \(1-Q/P^2=1-R\);
all later factors and all factors of \(\Theta_Q(P)\)
are units as well. The derivative \(\Theta'_Q(1)\) is a
unit with value minus one. In particular \(\eta(0,0)=-1\).

In the actual point-line rational coefficient \(v\), the
full meromorphic Tate frame for \(M_6\) is
\[
 V_{\rm T}=Z^{-3}f_P(Z)^6 r_6(p)\,v.            \tag{E81.7}
\]
Its horizontal divisor is exactly the marked divisor
\((6G)-(O)\), since the \(6D_1\) factors cancel by the
typed Miller arrow. In the ordered-model extension the
actual frame comparison is \(s\Delta V_{\rm T}\);
both the parameter factor and the two Miller fibres
are retained as in E73, rather than deleted from E81.7.
They are base functions and cancel only in the following
source/target coefficient ratio.

Direct substitution into the actual source period and the
map E68.1 gives their complete Tate actions
\[
\begin{split}
 h:(Z,V_{\rm T})&\longmapsto
                     (QZ,R^{-3}V_{\rm T}),\\
 B:(Z,V_{\rm T})&\longmapsto
                     (P^{-1}Z,\lambda q\,K V_{\rm T}),\\
 K&=(P/t)^3\eta^6 .
\end{split}                                                   \tag{E81.8}
\]
The same equations hold in \(s\Delta V_{\rm T}\).
Here \(K\) is a full nonzero analytic unit with \(K(0,0)=8\);
the selected height \(q=t-t_{\rm selected}(s)\) remains
the original one. Equations E81.7--8 identify the annular
line and both period generators, including every base
factor, with the ordered-resolution calculation.

More explicitly, on the common source chart E75.1 their
coefficient comparison is exactly
\[
       s\Delta V_{\rm T}
          =\frac{Z^{-3}f_P(Z)^6}{x^3}\,\xi .     \tag{E81.10}
\]
The full \(r_6\) factors cancel in this equation by their
literal types. Both \(s\Delta\) and the actual \(x\)
divisor have already been retained in the two definitions.
This is the common-exterior arrow between the Cox multiplier
\(8\lambda q\) and the Tate multiplier \(\lambda qK\);
it does not set their extending unit ratio equal to one.

On \(s=0\), the actual three-step \(f_2\) coefficient is
\(-2t\). Reindexing its three Tate translations by \(h\)
therefore gives \(P\eta^3=-2t\). Hence
\[
 K|_{s=0}=4P/t,\qquad
 hB^3|_{s=0}:(Z,V_{\rm T})\longmapsto
                    (Z,(4\lambda q/t)^3V_{\rm T}).             \tag{E81.9}
\]
This recovers the exact central norm wall E78 through an
actual source/Cartier/period morphism. It does not remove
that wall or complete the chronological strip.

## E82. Exact period properness and an admitted coupled punctured sector

On the ordinary two-torus chart of E81 put
\[
 A=-\log|P|,\quad C=-\log|R|,\quad
 D=-\log|\lambda qK|.
\]
Take the coordinate bidisc small enough that \(A,C>0\).
The real logarithmic period matrix, with columns \(h,B\),
is exactly
\[
 {\cal L}=
 \begin{pmatrix}-2A-C&A\\3C&-D\end{pmatrix},
 \qquad \det{\cal L}=(2A+C)D-3AC.               \tag{E82.1}
\]
On the open set where this determinant is nonzero, the two real
translations form a lattice in the real logarithmic plane. Together with
the two literal angular periods, they act freely and
properly on the ordinary chart and have a compact real
four-torus quotient. Indeed a compact set in the logarithmic
plane meets only finitely many translates of an invertible
real lattice; the angular directions are already compact.
The contracting component containing small \(\lambda\)
is the explicit inequality
\[
                         D>\frac{3AC}{2A+C}.   \tag{E82.2}
\]
At \(s=0\), \(A=C\), and E82.2 reduces to the norm wall
already calculated in E78.

The inverse coordinate map E81.5 gives a uniform constant
\(C_0\) such that
\[
 \min(A,C)\le-\log|s|+C_0
\]
on a smaller punctured bidisc: at least one of \(|P|\)
and \(|R|\) is bounded below by a fixed multiple of
\(|s|\). Also \(3AC/(2A+C)\le3\min(A,C)\), directly
in both orders of \(A,C\).
Since \(qK\) is a nonzero analytic unit, choose a small
constant \(r_0\) and set the actual scalar and root to
\[
                  \lambda=r_0^2s^4,\qquad
                  r_{\rm sc}=r_0s^2.           \tag{E82.3}
\]
Then
\[
 D-3\min(A,C)\ge-\log|s|
      -\log|r_0|^2-\sup\log|qK|-3C_0>0
\]
after fixing \(r_0\) and the bidisc. This proves E82.2
uniformly for the ordinary punctured sector, retaining
the original source parameter.
At the \(P=0\) and \(R=0\) ends its limiting strict
inequalities are \(2D>3C\) and \(D>3A\), respectively.
For the latter end the actual line-frame change
\(V\mapsto Z^3V\) changes the periods to
\((Q,P^6)\) and \((P^{-1},P^{-3}\lambda qK)\);
it is the explicit component frame used there.
No full central quotient is asserted by this properness
calculation.

The coupled scalar has an exact annular endpoint square.
Use E77 with \(\log r_{\rm sc}=\log r_0+2\log s\).
A positive source-parameter turn adds \(2\delta\) to its
scalar coefficient \(c\). Consequently
\[
                 \Phi_{\rm end}
                         =q_\infty^2\Phi_{\rm start}.
\]
The globally defined ordinary and cap forward parameter-deck
maps are therefore the following initial-to-endpoint line arrows:
\[
 C_{\rm ord}=q^2,\qquad C_{\rm cap}=h^2,\qquad
 h=1-t_{\rm selected}(s)q_\infty,
\]
\[
       \Phi_{\rm end}C_{\rm ord}
                        =C_{\rm cap}\Phi_{\rm start},
       \qquad q_\infty^2q^2=h^2.                \tag{E82.4}
\]
The inverse endpoint-to-initial closing maps are
\(C_{\rm ord}^{-1}=q^{-2}\) and
\(C_{\rm cap}^{-1}=h^{-2}\). Their typed square is
\[
 \Phi_{\rm start}C_{\rm ord}^{-1}
       =C_{\rm cap}^{-1}\Phi_{\rm end}.
\]
Both directions are actual base scalars commuting with the retained
source, norm and character maps. At the selected fan,
the apparent \(q^2\) is carried by the actual period
reindex \(B^2\). Write its actual generator in the selected Tate
coordinates as
\(B=(P_{\rm sel}^{-1}Z,\lambda q\beta V)\). Direct composition gives
\[
 C_{\rm ord}
       =B^2\circ(P_{\rm sel}^{\,2}Z,
                            \lambda^{-2}\beta^{-2}V).          \tag{E82.5}
\]
The second map is the full bounded-unit torus map on a
fixed parameter annulus, and its integer cone characters
give the actual selected-fan arrow. Its factors are not
dropped. The finite root map in E82.4 uses \(h^2\), not
an identity substituted for that extending cap unit.
Equations E82.3--5 specify this admitted coupled
punctured family, its forward deck, and its inverse closing. Its central filling
and return remain part of the chronological strip problem.

## E83. The actual local canonical and Spin comparison

The common chart also fixes the determinant arrow, rather than only
the weights of its normal planes. With the original source residue
form \(\Omega=dx\wedge dt_{\rm base}/(2y)\), direct differentiation
of E63 gives
\[
       2\Omega\wedge ds=dz\wedge dw\wedge dx.     \tag{E83.1}
\]
Consequently the punctured-line canonical four-form is
\[
 {\cal V}=dz\wedge dw\wedge dx\wedge d\log\xi
             =2\Omega\wedge ds\wedge d\log v.    \tag{E83.2}
\]
The second equality substitutes the full
\(\xi=s\Delta r_6x^3v\). Its logarithmic difference is a
source one-form and wedges to zero with the displayed
source three-form. It does not remove the original Cartier
factor from any line coefficient.

The literal translation in E74 has determinant one in
\((z,w,x)\). Its line arrow is \(d w^{-3}\xi\), and its
logarithmic derivative differs from \(d\log\xi\) by
\(d\log d-3d\log w\), again a source one-form.
Thus it carries \({\cal V}\) exactly, on the common open
set and then in both endpoint charts by their explicit
holomorphic maps.

The coefficient gauge \(\xi=1\) in E76 can be checked
before taking its finite quotient. Put \(c^3=\xi\); its
actual source chart map is
\[
 (z,w,x,\xi)\longmapsto
       (u_0,u_1,t_0,t_1)=(c,cz,w/c,x/c).
\]
It has the exact determinant-form equality
\[
 du_0\wedge du_1\wedge dt_0\wedge dt_1
                       =-\tfrac13{\cal V}.     \tag{E83.3}
\]
On the target \(t_0=1\) chart the same calculation gives
\((1/3)d\alpha\wedge d\beta\wedge dh\wedge d\log\xi_{\rm target}\).
The target source map E74.2 has determinant minus one in
\((\alpha,\beta,h)\), so this is again
\(-{\cal V}/3\). The same canonical arrow therefore reaches
both charged product faces.

The \(\mu_3\) deck in E76.2 has complex determinant one.
It preserves the explicit form E83.3 and the induced
complex canonical Spin structure. The physical circle
has weights \((1,1,-1,-1)/3\) on that cover, also of sum
zero; its endpoint is precisely this \(\mu_3\) deck.
The determinant-trivial lift is the one induced by the
displayed canonical form. Since the charged link has
\(H^1(S^7/\mu_3;\mathbb Z/2)=0\), there is no second
Spin character on that link. The source/line transition
and its retained logarithmic derivative supply this
specific lift through the two chronological endpoint
charts. This remains a local determinant/Spin statement;
the full period-strip boundary equation is still open.

## E84. The literal cube in the Cox--Tate coefficient comparison

The full common-exterior map E81.10 has a prescribed cube
root, with no new branch choice:
\[
 \varphi=\frac{Z^{-1}f_P(Z)^2}{x},\qquad
          s\Delta V_{\rm T}=\varphi^3\xi.        \tag{E84.1}
\]
The actual source-period and suspension transformations give
\[
 \frac{\varphi(hp)}{\varphi(p)}=R^{-1},\qquad
 \frac{\varphi(Bp)}{\varphi(p)}
                  =u_B\,w,\qquad
 u_B=\frac{P\eta^2}{2t},\qquad K=8u_B^3.        \tag{E84.2}
\]
For the second equality substitute
\(f_P(P^{-1}Z)/f_P(Z)=\eta/f_2\),
\(f_2=x/w\), and \(x_{\rm new}=2tw/x\).
For the first equality use \(Q=P^2R\) and the literal
period identity for \(f_P\). These prove both relations
without selecting a cube root after the calculation.

The base unit \(u_B\) extends on the entire collision
bidisc and has value one at its origin. On the whole
central curve it instead satisfies
\(u_B=-\eta^{-1}\), by E81.9; its full value remains in
the finite strip. The scalar cube roots in the Tate
and Cox charged charts differ by this precise unit.

On their common open set the charged representative map
is
\[
       (u,t_{\rm Cox})\longmapsto
              (\varphi u,\varphi^{-1}t_{\rm Cox}).             \tag{E84.3}
\]
It preserves the original source polynomials, the
physical circle and the invariant product norm \(R\)
of E76.4. At a marked section its coefficient is read
in the actual point-line frame of E74.3; the formula
does not assert that the meromorphic \(\varphi\) is a
unit in a chart containing its section divisor.
The endpoint coefficient maps in EP.18 carry those
zeros and poles literally. The extra logarithmic
derivative in E84.3 is a source one-form, and hence
its determinant comparison is precisely E83.
Thus the cube fixes the same canonical finite lift
on the two side collars; it leaves their global
boundary ownership to the chronological strip.

## E85. Exact exceptional periods and a finite open-cell atlas

For an integer \(N\ge4\) divisible by two, keep the actual
coupled scalar \(\lambda=s^N\lambda_0\), with its quadratic
cap root \(s^{N/2}r_0\). Blow up the actual coordinate
ideal \((P,R)\) from E81. In its chart \(R=pP\) the
original parameter remains
\[
       s=P(p-1)/u_s,\qquad
       \lambda qK=P^N(p-1)^N c,\qquad
       c=\lambda_0 qK\,u_s^{-N}.               \tag{E85.1}
\]
The unit \(c\) is retained on this chart. Its value at
\(P=0\) is \(\lambda_0q(0,0)\,8\), independent of finite
\(p\); the factors \(p\) and \(p-1\) are kept separately.

The following is a unimodular change of the actual
period generators:
\[
 H_1=B^{-1},\qquad H_2=hB^3,\qquad
 \begin{pmatrix}0&1\\-1&3\end{pmatrix}\in
                {\rm SL}_2(\mathbb Z).
\]
Use the actual line coordinate \(Y=Z^NV_{\rm T}\).
On the open exceptional curve \(p\ne0,1,\infty\),
direct substitution gives
\[
\begin{split}
 H_1:(Z,Y)&\longmapsto(PZ,bY),&
       b&=(p-1)^{-N}c^{-1},\\
 H_2:(Z,Y)&\longmapsto(pZ,P^L aY),&
       L&=3(N-1),\\
 a&=p^{N-3}(p-1)^{3N}c^3,&
                 ab^3&=p^{N-3}.              \tag{E85.2}
\end{split}
\]
The source and line functions of E85.1 have not been
replaced by their leading terms. The physical scalar
acts on \(Y\) as on \(V_{\rm T}\), since \(Z\) is a
source coordinate.

The ordinary source and line chain coordinates are
\[
 Z_i=Z/P^i,\quad W_i=P^{i+1}/Z,\qquad
 U_j=Y/P^j,\quad V_j=P^{j+1}/Y,
 \qquad Z_iW_i=U_jV_j=P.                         \tag{E85.3}
\]
Their exact period label arrows are
\[
 H_1:(i,j)\longmapsto(i+1,j),\qquad
 H_2:(i,j)\longmapsto(i,j+L).
\]
The accompanying coefficient maps are respectively
\[
 (Z_i,W_i,U_j,V_j)\mapsto
           (Z_i,W_i,bU_j,b^{-1}V_j)
\]
and
\[
 (Z_i,W_i,U_j,V_j)\mapsto
           (pZ_i,p^{-1}W_i,aU_j,a^{-1}V_j).
\]
They preserve both equations in E85.3. The usual two
toric refinements of this fibre product are obtained
by their literal common-node blowups; each period
acts by these same integral character maps on every
cone. This gives a finite \(L\)-cell fundamental
atlas over a compact subannulus of the open \(p\)-curve.
All coefficients there and their inverses are bounded.
There is no finite covering in this construction:
the displayed generator change has determinant one.

The valuation matrices of the same maps, with the
original columns \(h,B\), are
\[
 W_P=\begin{pmatrix}2&-1\\0&0\end{pmatrix},\quad
 W_R=\begin{pmatrix}1&0\\-3&0\end{pmatrix},\quad
 W_s=\begin{pmatrix}0&0\\0&N\end{pmatrix}.
\]
On the exceptional divisor their sum is
\(\left(\begin{smallmatrix}3&-1\\-3&N\end{smallmatrix}\right)\),
of determinant \(3(N-1)\).
The \(P\)-face primitive source kernel is \((1,2)\),
and its actual residual map is
\[
                   hB^2=(R,\lambda^2q^2K^2R^{-3}).            \tag{E85.4}
\]
The \(R\)-face primitive source kernel is the original
\(B\) column. These exact endpoint maps, the
\(p=1\) factor in E85.1, and the full reference cap
square are the three unfilled ends of this open
atlas. No compact central quotient or characteristic
return is assigned by its cell count or determinant.

## E86. The first-period coefficient in one charged ball

E80.4 compares the two independently gauged actual ruling
coefficients specified there. For a finite cut in one common
charged ball, the first primitive period must be inserted
before the two outside periods. Its coefficient is fixed by
E75.2, rather than by a new choice of target frame.

In the common gauge \(\Xi=1\), the source ruling coefficient
is \(u_0^3\). The target ruling coefficient after the actual
first period is \(d\,t_0^{-3}\), where
\(d=8\lambda q(0,0)\) on the central core. E80.2 therefore
gives the exact three-step coefficient equation
\[
 u_{0,\mathrm{final}}^3
 =-\frac{d^2}{h^3(h+1)^3}\,d\,t_0^{-3}
 =-\frac{d^3t_0^3}{t_1^3(t_0+t_1)^3},\qquad h=t_1/t_0.
 \tag{E86.1}
\]
The resulting common-ball core map has the literal lift
\[
 u_{\mathrm{final}}
       =-d\,\frac{(t_0,t_1)}{t_1(t_0+t_1)}.
 \tag{E86.2}
\]
Its coefficient is already the cube of the function \(-d\).
Changing its representative by a cube root of unity is
exactly the existing auxiliary \(\mu_3\) action. The map
commutes with the physical circle because the two sides
have respective weights \(+1/3\) and \(-1/3\). It retains
both component-intersection poles and the actual projective
endpoint maps of EP.16--18.

Equivalently, applying E76.3 to the first target representative
gives \((u,t)\mapsto(d^{1/3}u,d^{-1/3}t)\); substitution in
the two-actual-gauge formula E80.4 yields E86.2. Thus both
coefficient conventions are related by the prescribed first
period, including its phase.

The invariant product norm on this same-ball core is
\[
 R=|d|\frac{|t_0|^2+|t_1|^2}{|t_1(t_0+t_1)|}
   =|d|\frac{1+|h|^2}{|h(h+1)|}
   \ge \frac{2|d|}{1+\sqrt2}.                 \tag{E86.3}
\]
Indeed, for \(a=|t_0|\) and \(b=|t_1|\),
\(|t_1(t_0+t_1)|\le b(a+b)\). The quadratic form
\(ab+b^2\) has matrix
\(\left(\begin{smallmatrix}0&1/2\\1/2&1\end{smallmatrix}\right)\)
and largest eigenvalue \((1+\sqrt2)/2\). Equality is
attained with aligned phases and \(b/a=1+\sqrt2\).
Consequently a common-ball cut with radius satisfying
\(r_0^2<2|d|/(1+\sqrt2)\) misses the entire continued
central core. The earlier two-actual-gauge coefficient
\(-d^2\) is not the coefficient of this common-ball cut;
E86.1 gives their complete comparison. The continuation
through the two poles is the actual graph atlas EP.7--18.
This local separation does not count the unpaired faces
of the full chronological period strip.

## E87. The full marked scalar square on an admissible parameter torus

Fix a small positive \(\epsilon\) and put
\(r_{\rm base}=r_0\epsilon^2\), with the actual constant
\(r_0\) of E82.3. On
\[
 s=\epsilon e^{2\pi i\theta},\qquad
 r_{\rm sc}=r_{\rm base}e^{2\pi i\rho},
 \qquad (\theta,\rho)\in\mathbb R^2/\mathbb Z^2,
 \tag{E87.1}
\]
the modulus of \(\lambda=r_{\rm sc}^2\) is exactly the
modulus used in E82.3. Its strict logarithmic period
inequality holds uniformly. The ordinary outside, the
selected fan charts, and the quadratic cap are the actual
charts already retained in E64 and E70--77. Their coefficients
are bounded on this parameter torus. They give the compact
punctured family there with the same physical circle.

Here is the reference-cochain verification needed for its
scalar closing. The actual primitive cap generator is
\(H=A\), with \(H^2=B\). Choose a \(\delta\)-invariant
Hermitian norm for which \(H\) is uniformly strictly
contracting. Let \(\chi\) be zero for small norm and one
for large norm, and fix a point \(x_0\) in the punctured
root line. The locally finite difference sum
\[
 \upsilon(x)=-\sum_{k\in\mathbb Z}
 \{\chi(\|H^kx\|)-\chi(\|H^kx_0\|)\}
 \tag{E87.2}
\]
satisfies \(\upsilon(Hx)=\upsilon(x)+1\). Local finiteness
follows from the uniform contraction at the two ends of
the sum. Thus \(d\upsilon\) defines the integral cap
evaluation sending \([A]\) to one. It evaluates to zero
on the physical circle and every actual lifted source
cycle, because each is a closed loop in the cover on
which \(\upsilon\) is a single-valued real function.

Use \(\alpha_\infty=\arg q_\infty/(2\pi)\), and retain
\(\gamma_{\rm out}=-[B]\). The literal root cut of K28.3,
carried by the point-line arrow E70.1 and norm E71.3, is
\((z,u_{\rm out})\mapsto(-z,u_{\rm out}-1)\).
Its ordinary boundary coordinate is
\(u_{\rm out}=2\gamma_{\rm out}-\alpha_\infty\).
The cap evaluation, in the full ordered boundary basis,
is therefore
\[
 \begin{array}{c|ccccc}
       &\alpha_\infty&a&b&\gamma_{\rm out}&\delta\\ \hline
 \operatorname{ev}&1&0&0&-2&0 .
 \end{array}                                      \tag{E87.3}
\]
The retained physical character is in the last column.
In particular the actual norm meridian
\(2\alpha_\infty+\gamma_{\rm out}+\Lambda\), with its
source/physical period vector \(\Lambda\), is killed.
This is the full marked reference meridian of norm one.

In E77, let \(\nu\) be the integer total of the suspension
cocycle \(j_{\alpha\beta}\) around this ordinary annulus.
The same lifted meridian is represented by
\(AB^\nu\) together with the explicit source/physical
periods in E77.2. Evaluation gives \(1+2\nu\).
Comparing with E87.3 for this same reference map gives
\(\nu=0\). On the two angular sectors choose actual
integers \(J_\alpha\) with
\(J_\beta-J_\alpha=j_{\alpha\beta}\): take zero on the
first sector and the value of \(j\) on one overlap on
the second; the other overlap agrees because \(\nu=0\).
The representative change
\[
 \widetilde\Phi_{0,\alpha}=B_0^{-J_\alpha}\Phi_{0,\alpha}
 \tag{E87.4}
\]
is a literal target deck, with inverse \(B_0^{J_\alpha}\).
It leaves the quotient map unchanged and retains its
integer cochain. Here subscript zero denotes the actual
reference scalar \(r_{\rm base}\), so \(B_0\) in E87.4
includes that scalar; it is not a newly rigidified lift.

On the cut \(\rho\)-plane put
\(A_\rho=e^{2\pi i\rho}A_0\) and
\(B_\rho=e^{4\pi i\rho}B_0\). Restore every reference
deck by the explicit formula
\[
 \Phi_{\rho,\alpha}
 =e^{2\pi i\rho\ell_\alpha}
       B_\rho^{J_\alpha}\widetilde\Phi_{0,\alpha}.
 \tag{E87.5}
\]
The scalar acts in the physical line. The full source
and line logarithms, finite character, and period vectors
of E77 remain in \(\widetilde\Phi_0\). Direct substitution
on the two overlaps gives
\[
 \Phi_{\rho,\beta}
  =A_\rho^{k_{\alpha\beta}}
       B_\rho^{j_{\alpha\beta}}\Phi_{\rho,\alpha},
 \qquad
 \Phi_{\rho+1,\alpha}=q_\infty\Phi_{\rho,\alpha}.
 \tag{E87.6}
\]
The second equality uses the actual equality
\(B_{\rho+1}=B_\rho\), including the restored integer
sector powers. This also proves the scalar dependence
claimed in E82 with the complete reference cochain.

For an integer \(j\), the forward initial-to-endpoint
parameter arrows and their inverse closings are
\[
 D_{\rm ord}^{(j)}=q^j,\quad D_{\rm cap}^{(j)}=h^j,
 \qquad
 C_{\rm ord}^{(j)}=q^{-j},\quad C_{\rm cap}^{(j)}=h^{-j}.
 \tag{E87.7}
\]
Their two typed squares are
\[
 \Phi_{\rho+j}D_{\rm ord}^{(j)}
     =D_{\rm cap}^{(j)}\Phi_\rho,\qquad
 \Phi_\rho C_{\rm ord}^{(j)}
     =C_{\rm cap}^{(j)}\Phi_{\rho+j}.
 \tag{E87.8}
\]
They are the identity \(q_\infty q=h\), with all full
functions retained. The cap unit \(h\) extends and
commutes with \(A_\rho\), including \((-1)^d\).

At the selected node the apparent zero of \(q^j\) is
carried by the actual period reindex
\[
 D_{\rm ord}^{(j)}=B^jR_j,
 \quad R_j:(Z,V)\mapsto(P_{\rm sel}^jZ,
                          \lambda^{-j}\beta^{-j}V).
 \tag{E87.9}
\]
Write \(a=P_{\rm sel}^j\), \(b=\lambda^{-j}\beta^{-j}\).
On the actual plus and minus selected-node charts its
maps are respectively
\[
 (x_0,x_1,x_2)\mapsto((ab)^{-1}x_0,ax_1,bx_2),
 \quad
 (y_0,y_1,y_2)\mapsto(ab y_0,b^{-1}y_1,a^{-1}y_2).
 \tag{E87.10}
\]
These preserve the height monomial and induce exactly
\((Z,V)\mapsto(aZ,bV)\). Both full units and their
derivatives are carried on every translated cone.
Replacing \(j\) by \(-j\) gives the inverse arrows.
Thus the square retains the source translation,
normal line, physical circle and both fan endpoints.

All source-parameter coefficients of the outside and
root maps are single-valued on the source disc, and
the reference integer cochain is constant there.
Consequently the \(\theta=0,1\) faces of E87.1 use the
identical maps. Their corner squares commute literally
with E87.7--10. The coupled loop is \((1,2)\) on this
actual parameter torus; the fixed-scalar source loop
is \((1,0)\), and the two positive scalar-root loops
are \((0,2)\). In the cut parameter plane, linear
interpolation between the diagonal path from \((0,0)\)
to \((1,2)\) and its horizontal-then-vertical path is
endpoint fixed. Pulling back this family and its full
displayed arrows gives their marked bundle comparison.
A circle-averaged horizontal connection transports
the same physical line along that homotopy, and its
boundary endpoint map is E87.8. This establishes the
actual punctured-family loop composition. Its use to
evaluate a return still requires the completed coupled
bordism and its boundary ownership.

## E88. The actual p=1 end away from the exceptional corner

Keep E85's full \(c\), put \(v=p-1\), and restrict \(P\)
to a closed annulus avoiding zero. The exact frame
\(W=Z^{-(N-1)}Y=ZV_{\rm T}\) gives
\[
\begin{split}
 h:(Z,W)&\mapsto(P^3pZ,p^{-2}W),\\
 B:(Z,W)&\mapsto(P^{-1}Z,P^{N-1}v^N cW),\\
 H_2=hB^3:(Z,W)&\mapsto(pZ,
             P^{3N-3}p^{-2}v^{3N}c^3W).
\end{split}                                                \tag{E88.1}
\]
In the preceding \(Y\)-frame the line coefficient of
\(h=H_1^3H_2\) is \(P^{3N-3}p^{N-3}\). The displayed
frame arrow carries its entire \(P\) factor; it does
not delete that parameter winding.

The actual extending point-line coordinate on this
end is fixed by E73 and E84:
\[
 W_{\rm C}=s\Delta W
          =v e(P,v)W,
 \qquad e=P\Delta/u_s .                          \tag{E88.2}
\]
On the chosen \(P\)-annulus, \(\Delta(0,t)=8t^2\) is
nonzero, so \(e\) and its inverse extend on a sufficiently
small \(v\)-disc. E88.2 is the typed Cartier coefficient
arrow from E84, with its full \(s\Delta\). All periods
preserve the source-base functions, so E88.1 acts on
\(W_{\rm C}\) by the same line coefficients.

Use the complete line chain
\[
 U_j=W_{\rm C}/v^j,\qquad
 V_j=v^{j+1}/W_{\rm C},\qquad U_jV_j=v,
 \qquad j\in\mathbb Z.                          \tag{E88.3}
\]
Its adjacent chart arrow on \(V_j\ne0\) is
\((U_{j+1},V_{j+1})=(V_j^{-1},U_jV_j^2)\).
Writing \(a_0=P^{3N-3}p^{-2}c^3\) and
\(b_0=P^{N-1}c\), the full period arrows are
\[
\begin{array}{c|c|c|c}
 &Z&j&(U_j,V_j)\\ \hline
 h&P^3pZ&j&(p^{-2}U_j,p^2V_j)\\
 B&P^{-1}Z&j+N&(b_0U_j,b_0^{-1}V_j)\\
 H_2&pZ&j+3N&(a_0U_j,a_0^{-1}V_j).
\end{array}                                                \tag{E88.4}
\]
These arrows preserve \(U_jV_j=v\), commute with the
physical action \((U_j,V_j)\mapsto(e^{i\phi}U_j,e^{-i\phi}V_j)\),
and satisfy the full relation \(H_2=hB^3\).
They preserve the original \((s,t_{\rm base})\) obtained
from the actual inverse \((P,R)\) map, with \(R=pP\).

First quotient by \(h\). Since \(P\ne0\), its source
period \(Q=P^3p\) defines the actual compact elliptic
curve, and its full line multiplier is \(p^{-2}\).
The chain charts are therefore the indicated degree-zero
line charts over that elliptic source. The quotient by
\(H_2\) closes the chain after \(3N\) labels. Its exact
source multiplier \(p\) and line multiplier \(a_0\)
extend at \(v=0\). On the punctured disc this is the
original period quotient; at zero the translation of
the infinite chain by \(3N\) is free and proper and has
a compact finite chain quotient. The charts
\(U_jV_j=v\) and all their displayed unit overlaps
give its smooth total space on this end.

The remaining actual \(B\) has order three on this
quotient because \(B^3=h^{-1}H_2\). At zero it moves
every component and node label by \(N\) modulo \(3N\),
so it has no fixed point. Compactness on the chosen
\(P\)-annulus keeps this action free after shrinking
the \(v\)-disc. Its quotient gives \(N\) central
component orbits and \(N\) physical-circle fixed
node-section orbits. At each such section the source
is the actual elliptic curve with period \(P^3\).
These are statements about this local end, with all
normal multipliers in E88.4 retained.

For comparison with chains written in the uncorrected
ordinary coordinate \(W\), E88.2 gives the exact arrow
\[
 (j,U_j^{\rm ord},V_j^{\rm ord})
 \longmapsto(j+1,eU_j^{\rm ord},e^{-1}V_j^{\rm ord}).
 \tag{E88.5}
\]
Thus the Cartier factor includes an actual label shift
and its full unit. This end construction leaves the
corner \(P=0,v=0\), and the \(p=0,\infty\) ends,
for the remaining compact attachment. No characteristic
integral is obtained by counting these components.

## E89. The precise obstruction to shrinking the fixed-scalar ball

The complete EP.6 face map includes the first period and
has coefficient \(d=8\lambda q\). For a fixed nonzero
scalar its sufficient full-face separation condition is
\[
 r^2(\sqrt2+r^2)<\inf|d|.
 \tag{E89.1}
\]
Both normal directions and all source functions are
retained in that estimate. In the coupled family
\(\lambda=\lambda_0s^N\), \(N\ge4\), however, the
same charged product ball satisfies the exact inequality
\[
 |s|=|u_0t_1-u_1t_0|\le\|u\|\|t\|\le r^2.
 \tag{E89.2}
\]
On the fixed small source neighbourhood, \(|8\lambda_0q|\)
is bounded by a constant \(C\). A nonzero coupled fibre
meeting a ball satisfying E89.1 would therefore give
\[
 \sqrt2|s|\le\sqrt2r^2<|d|\le C|s|^N.
 \tag{E89.3}
\]
This fails for all sufficiently small nonzero \(|s|\).
Thus shrinking the separated fixed-scalar product ball
does not supply the coupled central attachment. The
open exceptional period atlas and its actual end charts,
including E88, are required for those fibres. This
obstruction concerns precisely the displayed ball and
separation inequality; it does not assign a return or
rule out a completed period-end construction.

## E90. Both full Miller fibres and the rigidified point-theta constant

The actual Tate coordinates of E81 satisfy \(Q=P^2R\),
with \(G\) represented by \(P\). They locate both
\(\Delta\)-fibres exactly. On \(R=P^4\), one has
\(Q=P^6\), and \(3G\) is the nonzero half-period
represented by \(P^3\). On \(R=-P\), one has
\(Q=-P^3\), and \(3G\) is represented by \(-1\) after one literal source period. In both cases
\(y(3G)=0\), with \(3G\ne O\). For nonzero small
\(P\), the original \(s,t\) are nonzero on these
two curves; the full equality
\(y(3G)=t\Delta/s^3\) therefore makes \(\Delta\)
vanish there.

The first-order inverse coordinate map is
\(t=P/2+O(2)\), \(s=R-P+O(2)\). Consequently
\[
 \Delta=R(R+P)+O(3).
\]
The two smooth curve equations \(R-P^4\) and
\(R+P\) have distinct tangent lines and consume this
entire quadratic divisor. Analytic division thus gives
the exact equality
\[
 \Delta=(R+P)(R-P^4)u_\Delta(P,R),\qquad
 u_\Delta(0,0)=1,
 \tag{E90.1}
\]
where \(u_\Delta\) and its inverse are holomorphic.
The equality retains the full function \(\Delta\);
it does not replace its two fibres by their tangent
lines. The separate branch \(R=P\) has \(3G=O\) and is already the actual \(s=0\) branch, not one
of these two finite nonzero half-period branches.

Use the full theta product of E81. Directly separating
its first two backward factors gives
\[
\begin{split}
 P^6\Theta_Q(P^6)
   &=(R-P^4)(R-P)(R+P)E_6(P,R),\\
 E_6&=(1-P^6)
       \prod_{\nu\ge1}(1-P^{2\nu+6}R^\nu)
       \prod_{\nu\ge3}(1-P^{2\nu-6}R^\nu).
\end{split}                                                 \tag{E90.2}
\]
All exponents in the remaining products are nonnegative,
and the \(\nu=3\) backward factor is \(1-R^3\).
Thus \(E_6\) is a convergent analytic unit with value
one at the origin. In particular
\[
 s\Delta=\frac{u_\Delta}{u_sE_6}
                    P^6\Theta_Q(P^6).
 \tag{E90.3}
\]
On the exceptional chart \(R=pP\), the same exact
factorization is
\[
 s\Delta=P^3(p-1)(p+1)(p-P^3)\frac{u_\Delta}{u_s}.
 \tag{E90.4}
\]
It locates the two full Miller curves at \(p=-1\) and \(p=P^3\), including their actual corner contact.

The scalar relating the point and tensor theta frames
is determined by the specified origin, without any
additional normalization. Let \(a_{\rm T}\) be the
actual Weierstrass scale in E81 and set
\(\theta_1=\Theta'_Q(1)\). At \(O\), the coordinate
\(\tau=-x/y\) obeys
\[
 Z-1=a_{\rm T}\tau+O(\tau^2),\qquad
 f_6=-\tau^{-5}+O(\tau^{-4}).
 \tag{E90.5}
\]
The latter follows directly from the full Miller
formula: \(f_3=\tau^{-2}+O(\tau^{-1})\), and the
actual tangent-over-vertical factor of \(3G\) has
leading term \(-\tau^{-1}\).
The exact inversion identity
\(\Theta_Q(P^{-1})=-P^{-1}\Theta_Q(P)\) then gives
\[
 \frac{f_P(Z)^6}{f_6(p)f_{P^6}(Z)}
 =\frac{\Theta_Q(P)^6}
 {a_{\rm T}^5\theta_1^5\Theta_Q(P^6)}.
 \tag{E90.6}
\]
The ratio is independent of the elliptic point because
its divisor and automorphy factor are zero. E90.5
fixes its entire base value, including its sign and
both \(\Delta\)-fibres.

For the genuine point-line coefficient
\(V_{\rm pt}=f_{P^6}(Z)v_M\), equations E81 and
E90.3--6 now give the typed line arrow
\[
 s\Delta V_{\rm T}
 =P^6U_6(P,R)Z^{-3}V_{\rm pt},\qquad
 U_6=\frac{u_\Delta\Theta_Q(P)^6}
 {u_sE_6a_{\rm T}^5\theta_1^5},\quad U_6(0,0)=-1.
 \tag{E90.7}
\]
Every factor in \(U_6\) is an extending unit. The
displayed \(P^6\) is retained as a Cartier factor.
The inverse arrow is the reciprocal map between
these specified line frames.

There are two useful literal period reindexings of
the point lift. Put \(b_1=P^6/Q=P^3/p\) and
\(b_2=P^6/Q^2=p^{-2}\). The full theta identities
give
\[
\begin{split}
 f_{P^6}(Z)&=-ZP^{-6}f_{b_1}(Z),\\
 f_{P^6}(Z)&=Z^2Q^{-3}b_2^{-2}f_{b_2}(Z).
\end{split}                                                 \tag{E90.8}
\]
Hence the same actual coefficient has both forms
\[
 s\Delta V_{\rm T}
 =-U_6Z^{-2}f_{b_1}(Z)v_M
 =P^{-3}pU_6Z^{-1}f_{b_2}(Z)v_M.
 \tag{E90.9}
\]
The first carries the full \(p=P^3\) point/O
coincidence. The second carries the \(p=-1\) and
\(p=1\) coincidences and the full vertical
\(P^{-3}\) frame. They are equal through the
specified source-period and theta arrows.

## E91. The actual point-section graph at p=P cubed

Near \(P=p=0\), the first period reindex in E90.8
represents \(6G\) by the exact point
\(b_1=P^3/p\), while \(O\) is represented by one.
The graph of this point parameter is the normalized
graph of the actual ideal \((P^3,p)\). In the
ordered valuation coordinates \((v_P,v_p)\), its
new ray is \((1,3)\). A regular refinement has rays
\[
 (1,0),(1,1),(1,2),(1,3),(0,1),
 \tag{E91.1}
\]
with adjacent determinants one. Its three intermediate
charts, indexed by \(j=0,1,2\), are the literal maps
\[
 P=x_jy_j,\qquad p=x_j^j y_j^{j+1},\qquad
 b_1=x_j^{3-j}y_j^{2-j}.
 \tag{E91.2}
\]
On their ordinary common open set the inverse monomials
are \(x_j=P^{j+1}/p\), \(y_j=p/P^j\).
The last chart is
\[
 P=x,\qquad p=x^3a,\qquad b_1=a^{-1}.
 \tag{E91.3}
\]
It retains the reciprocal point chart. These are
proper graph projections to the original \((P,p)\)
base, and therefore retain the exact original
\(s,t\) through their inverse Tate functions.

The universal point-line map through the coincidence
is equally explicit. On a chart where \(b_1\) is
near one, use the source coordinate \(Z\) near one.
The two Cartier sections have equations \(Z-b_1\)
and \(Z-1\), and
\[
 f_{b_1}(Z)=\frac{Z-b_1}{b_1(Z-1)}
       \frac{\prod_{\nu\ge1}(1-Q^\nu Z/b_1)
                              (1-Q^\nu b_1/Z)}
            {\prod_{\nu\ge1}(1-Q^\nu Z)
                              (1-Q^\nu/Z)}.
 \tag{E91.4}
\]
The displayed product ratio is an extending unit
on this chart. To specify the line-map types, write
\(e=(Z-1)/(Z-b_1)\) for the displayed meromorphic
generator of \(\mathcal O(D_{6G}-D_O)\). Multiplication
by E91.4 takes \(e\) to \(b_1^{-1}\) times that
extending unit in the flat Tate-line frame whose
source-deck multiplier is \(b_1\). The reciprocal
unit gives its inverse. This is a holomorphic
isomorphism between these two specified line bundles,
including the points on either Cartier divisor.
At \(b_1=1\) both Cartier equations coincide,
and the arrow restricts to the identity in these
frames. On the blowup of their intersection ideal
\((Z-1,b_1-1)\), both pullback section divisors
have exceptional coefficient one; their difference
therefore retains the two strict transforms with
no exceptional coefficient. The same statement
holds after pulling this exact map to the base
graph E91.1--3; no scalar factor is chosen on the
point/O coincidence.
This is the actual Poincare/Cartier comparison at
\(p=P^3\), with the \(-U_6Z^{-2}\) factor of
E90.9 retained. At \(p=-1\), the same formula
uses \(b_2=p^{-2}\) and the second coefficient
in E90.9; no graph reindex is suppressed there.

The graph construction resolves the point-parameter
ratio and supplies its line arrow. It does not by
itself resolve the full two-period corner or count
the boundary faces of that corner.

## E92. The full p=0 period corner and its generic point-line chart

Keep \(N=4\) and put \(v=p-1\). Use the actual corrected
coefficient, including both Miller curves,
\[
 Y_C=s\Delta Z^4V_{\rm T},\qquad X_C=Z/Y_C,\qquad
 b=v^{-4}c^{-1},\quad d_0=v^{24}c^6.             \tag{E92.1}
\]
On the ordinary common open set its change from E85 is
\((X,Y)\mapsto((s\Delta)^{-1}X,(s\Delta)Y)\).
Thus \(X_CY_C=Z\) is the same source coordinate.
The actual line and its inverse are carried by E90.7--9;
\(s\Delta\) is retained on its displayed divisors.

Take \(H_1=B^{-1}\) and \(K=H_1^9H_2=hB^{-6}\).
Multiplication of the full E85 periods gives
\[
\begin{split}
 H_1(X_C,Y_C)&=(Pb^{-1}X_C,bY_C),\\
 K(X_C,Y_C)&=(d_0X_C,P^9p\,d_0^{-1}Y_C).
\end{split}                                                   \tag{E92.2}
\]
The character matrix from \((Z,V_{\rm T})\) has rows
\((-3,-1),(4,1)\), and the period columns in \((h,B)\)
are \((0,-1),(1,-6)\); both determinants are one.
The full Cartier factor in E92.1 is included separately
from this integral character matrix. The physical action
has weights \((-1,+1)\) on \((X_C,Y_C)\).

Define the actual two infinite sets of charts by
\[
 x_i=X_C/P^i,\quad y_i=P^{i+1}/X_C,\qquad
 U_j=Y_C/(P^9p)^j,\quad V_j=(P^9p)^{j+1}/Y_C.   \tag{E92.3}
\]
Their equations and all period arrows are
\[
 x_iy_i=P,\qquad U_jV_j=P^9p=x_i^9y_i^9p,        \tag{E92.4}
\]
\[
\begin{split}
 H_1:(i,j;x,y,U,V)&\longmapsto
 (i+1,j;b^{-1}x,by,bU,b^{-1}V),\\
 K:(i,j;x,y,U,V)&\longmapsto
 (i,j+1;d_0x,d_0^{-1}y,d_0^{-1}U,d_0V).
\end{split}                                                   \tag{E92.5}
\]
Every coefficient is a holomorphic unit near \(p=0\),
including \(P=0\). These maps preserve the literal
original source functions obtained from \(R=pP\) and
the inverse map \((P,R)\mapsto(s,t_{\rm base})\).
They commute with the physical action on each chart.

On a closed \(P\)-annulus avoiding zero, agreement
with the actual source node can be given before taking
any quotient. Put \(V'_C=Z^3s\Delta V_{\rm T}\), so
\(X_C=(V'_C)^{-1}\), \(Y_C=ZV'_C\).
For the actual source-node chart \(z_0w_0=Q=P^3p\),
the normal-coordinate arrow is
\[
 U=z_0V'_C,\qquad V=P^6w_0/(V'_C),\qquad
 UV=P^9p.                                      \tag{E92.6}
\]
Its inverse is \(V'_C=X_C^{-1}\), \(z_0=X_CU\),
\(w_0=P^{-6}X_C^{-1}V\). The factor \(P^6\) is
retained in both directions. On this annulus it is an
extending unit; at \(P=0\) the two-period binomial
E92.4 retains it instead of using that inverse there.
The point-line coefficient through \(p=P^3\) is
E91.4. Hence the generic period charts carry the actual
point-line and source node simultaneously.

For small nonzero \(P\), the multiplier \(Pb^{-1}\)
is strictly contracting uniformly on a small \(p\)-disc.
Quotienting by \(H_1\) gives the actual compact elliptic
\(X_C\)-direction. Quotienting the \(U_jV_j=P^9p\)
chain by \(K\) closes one component and its two node
ends with the full displayed multipliers. This fills
the generic \(p=0\) end. The physical circle is free
there: a stabilizer must preserve the chain label,
hence use no nonzero \(K\) power, and the modulus of
the \(H_1\) multiplier excludes a nonzero \(H_1\)
power. E92.4 retains the remaining \(P=p=0\) corner.

## E93. The p=infinity point-line generator and generic end

Write \(u=P/R\) and
\[
 f=(1-u)^4c,\qquad c=\lambda_0qK u_s^{-4}.        \tag{E93.1}
\]
All factors in \(c\) are the full units of E81--85;
\(K\) inside this scalar denotes the E81 line multiplier.
Denote the two periods here by \(\mathcal K=hB^2\)
and \(\mathcal L=h^{-1}B^{-3}\). With
\(V_C=s\Delta V_{\rm T}\), direct multiplication gives
\[
\begin{split}
 h:(Z,V_C)&\longmapsto(u^2R^3Z,R^{-3}V_C),\\
 B:(Z,V_C)&\longmapsto(u^{-1}R^{-1}Z,R^4fV_C),\\
 \mathcal K:(Z,V_C)&\longmapsto(RZ,R^5f^2V_C),\\
 \mathcal L:(Z,V_C)&\longmapsto(uZ,R^{-9}f^{-3}V_C).
\end{split}                                                   \tag{E93.2}
\]
The identities \(h=\mathcal K^3\mathcal L^2\) and
\(B=\mathcal K^{-1}\mathcal L^{-1}\) retain every
unit. The period-basis determinant is minus one;
the raw character change \((Z,V)\mapsto(Z,Z^5/V)\)
also has determinant minus one. Both changes are retained.

The point-line frame at the generic \(u=0\) end is
determined by E90. Here \(Q=u^2R^3\), \(P=uR\), and
the actual point lift after three source periods is
\(c_6=P^6/Q^3=R^{-3}\). The full theta shift is
\[
 f_{P^6}(Z)=-\frac{Z^3}{Q^6c_6^3}f_{c_6}(Z).     \tag{E93.3}
\]
For \(V_{{\rm pt},R}=f_{R^{-3}}(Z)v_M\), it follows that
\[
 V_C=-U_6u^{-6}R^{-3}V_{{\rm pt},R},\qquad
 T_{\rm reg}=u^{-6}V_C^{-1}
       =-U_6^{-1}R^3 V_{{\rm pt},R}^{-1}.        \tag{E93.4}
\]
Thus \(T=V_C^{-1}=u^6T_{\rm reg}\) is the exact
Cartier generator on the overlap. The regular coefficient
\(T_{\rm reg}\) is a nonzero coefficient of the actual
dual point line on a closed \(R\)-annulus avoiding zero;
the \(u^6\) factor is retained as a vertical divisor.
The reciprocal of E93.4 is the specified inverse line
map. Its physical weight is minus one.

Put \(W=Z\). Since both periods fix \(u\), they act
on this regular coefficient by
\[
\begin{split}
 \mathcal K^{-1}(T_{\rm reg},W)
   &=(R^5f^2T_{\rm reg},R^{-1}W),\\
 \mathcal L(T_{\rm reg},W)
   &=(R^9f^3T_{\rm reg},uW).
\end{split}                                                   \tag{E93.5}
\]
In particular \(h\) acts by \(R^3\) and \(B\) by
\(R^{-4}f^{-1}\) on the regular dual coefficient,
exactly as required by the point represented by \(R^{-3}\).

Use \(W_j=W/u^j\), \(W_j^\vee=u^{j+1}/W\), so
\(W_jW_j^\vee=u\). The period \(\mathcal K^{-1}\)
leaves \(j\) fixed and acts by \(R^{-1},R\) on the
normal coordinates. The period \(\mathcal L\) takes
\(j\) to \(j+1\) and is the identity on those two
coordinates, retaining its full multiplier \(R^9f^3\)
on \(T_{\rm reg}\). First quotient by the contracting
period \(R^5f^2\) of the nonzero \(T_{\rm reg}\)
coordinate, and then by the one-step chain translation.
This constructs the generic \(u=0\) end. The original
source \(I_2\) has \(h\)-shift two and \(B\)-shift minus
one by E93.2. The physical circle is free: it translates
\(T_{\rm reg}\), and a stabilizer is excluded first
by the chain label and then by the strict modulus of
\(R^5f^2\). The \(R=0\) extension, including the
genuine divisor in the \(\mathcal L\) source factor,
still requires the full corner atlas and its attachment.

## E94. A smooth proper graph resolution of the p=0 binomial

This section resolves the specific binomial in E92.4.
It retains its source projection and the two periods;
it does not identify the completed global boundary.
Write its ordered factors as nine copies of \(x\),
nine copies of \(y\), and one copy of \(p\).
Successively blow up the actual ideal \((U,x)\) and,
in its continuing chart \(U=xa_1\), the next ideal
\((a_1,x)\). Continue through all nine \(x\) factors
and all nine \(y\) factors, always taking the strict
transform. Each blowup is projective over the preceding
space. The entire finite composition is therefore proper
over \(UV=x^9y^9p\).

For \(k=0,\ldots,8\), its \(x\)-factor charts are
\[
 x=ab,\qquad U=x^k a,\qquad
 V=x^{8-k}y^9p\,b,
 \qquad\hbox{coordinates }(a,b,y,p).             \tag{E94.1}
\]
Its \(y\)-factor charts are
\[
 y=ab,\qquad U=x^9y^k a,\qquad
 V=y^{8-k}p\,b,
 \qquad\hbox{coordinates }(x,a,b,p).             \tag{E94.2}
\]
The last chart is
\[
 p=ab,\qquad U=x^9y^9a,\qquad V=b,
 \qquad\hbox{coordinates }(x,y,a,b).             \tag{E94.3}
\]
These nineteen charts cover the strict transform:
at each step the chart with the chosen factor equal
to the current numerator times a new coordinate is
one displayed chart; the other chart continues to the
next step. All displayed free coordinates are ordinary
complex coordinates. In particular the morphism is
smooth on its domain, including repeated factors.

The actual source map on every chart is still
\(P=xy\), \(R=pP\), followed by the full inverse
Tate map to \((s,t_{\rm base})\). Every chart therefore
preserves those original functions. The source-normal
and line factors of E92.1, E90 and E91 are carried
by their pullback, with no replacement of \(s\Delta\)
by a leading monomial.

The physical weights, in the displayed coordinate
orders, are respectively
\[
 (k+1,-k-2,1,0),\qquad
 (-1,10-k,k-9,0),\qquad (-1,1,1,-1).             \tag{E94.4}
\]
All sums are zero. The first eighteen charts have a
fixed \(p\)-axis; the final chart has an isolated
semifree fixed point. This description is local to
the charts and does not count their eventual orbits.

Let \(\beta=b\) in E92.1 denote the full unit period
coefficient, distinct from the free coordinate \(b\)
in E94.1--3. The lifted \(H_1\) is multiplication by
\(\beta\) with each weight in E94.4, together with
the source index shift \(i\mapsto i+1\).
The lifted \(K\) is multiplication by \(d_0^{-1}\)
with those same weights, together with the line index
shift \(j\mapsto j+1\). For example, E94.1 gives
\[
 H_1:(a,b,y,p)\longmapsto
 (\beta^{k+1}a,\beta^{-k-2}b,\beta y,p),
\]
\[
 K:(a,b,y,p)\longmapsto
 (d_0^{-k-1}a,d_0^{k+2}b,d_0^{-1}y,p).         \tag{E94.5}
\]
The other two chart formulas follow by direct
substitution in E94.2--3, with precisely the weights
already displayed. These are also the unique lifts
of the actual blowup ideals, since each generator is
multiplied by a holomorphic unit.

There are literal arrows across adjacent source-chain
charts. On \(y\ne0\),
\[
 x'=y^{-1},\qquad y'=xy^2,\qquad U'=U,\quad V'=V.
 \tag{E94.6}
\]
The \(x\)-factor chart \(k\) maps to the next
\(y'\)-factor chart \(k\) by
\[
 a'=y^{9-2k}a,\qquad b'=y^{2k-7}b.              \tag{E94.7}
\]
Indeed \(a'b'=xy^2=y'\), and both displayed
expressions for \(U,V\) agree exactly. In the last
chart \(a'=a,b'=b\). The remaining factor charts
where the relevant \(x\) or \(y\) is a unit reduce
to these same arrows: their blowup ideal is principal.
The inverse of E94.7 is obtained by its reciprocal
powers and \(y=(x')^{-1}\). Across line-chain overlaps
the original \(U\) or \(V\) is already a unit, so
every blowup is the identity there. Thus this ordered
resolution glues through the actual infinite source
and line chains and carries both full period maps.

On the dense torus use the canonical form
\[
 \Omega=dx\wedge dy\wedge dp\wedge dU/U.          \tag{E94.8}
\]
Its pullbacks to E94.1, E94.2 and E94.3 are
\[
 -da\wedge db\wedge dy\wedge dp,\qquad
 dx\wedge da\wedge db\wedge dp,\qquad
 -dx\wedge dy\wedge da\wedge db,
\]
respectively. They extend without a zero or pole.
For a variable full unit \(g(P,p)\), the derivative
of its weight action is the constant diagonal action
times \(I+\eta\otimes d\log g\), where \(\eta\)
is the physical weight vector field. Since \(P,p\)
are invariant, \(d\log g(\eta)=0\); the latter
factor has determinant one and the explicit
contraction \(I+t\eta\otimes d\log g\).
This calculation retains the full derivative of the
actual units in E94.5 in the local canonical frame
\(\Omega_0=\Omega\). The original source canonical
form has an additional factor, which is also retained.
Let
\[
 J_{ts}=\det\frac{\partial(t_{\rm base},s)}
                     {\partial(P,R)},\qquad J_{ts}(0,0)=\tfrac12 .
\]
The actual invariant differential of E81 satisfies
\(dx_{\rm orig}/(2y_{\rm orig})
=a_{\rm T}^{-1}d\log Z\) modulo base forms. Hence
E83's original four-form is exactly
\[
 \mathcal V_{\rm orig}
 =\frac{2J_{ts}}{a_{\rm T}}\,
       dP\wedge dR\wedge d\log Z\wedge d\log V_{\rm T}
 =\frac{2J_{ts}}{a_{\rm T}}\,P\,\Omega_0.         \tag{E94.9}
\]
For the last equality, the character determinant in
E92 is one, the base-dependent Cartier differentials
wedge to zero, \(dP\wedge dR=P\,dP\wedge dp\),
and \(dP\wedge dp\wedge d\log x\wedge d\log U
=+\Omega_0\). The coefficient \(2J_{ts}/a_{\rm T}\)
is an extending unit with value one. Thus the pullback
of the original canonical form has the full divisor
\(P=xy=0\). On E94.1 this is \(aby=0\), on E94.2
it is \(xab=0\), and on E94.3 it is \(xy=0\).
The local determinant-one derivative contractions
preserve \(\Omega_0\); the actual comparison to the
inherited original spin frame additionally carries
this \(P\) phase and the specified unit. No spin
identification across \(P=0\) is made by dropping them.

The graph of \((P^3,p)\) in E91 and the other
exceptional ends still have to be glued to this
resolution with their actual fan and line markings.
The chart construction proves the stated proper local
resolution and its period/source/line arrows; no
characteristic integral or global face count is
deduced from E94.4.

## E95. An integral regular period fan at the p=infinity corner

Use the regular point-line coefficient of E93,
\[
 V_{\rm reg}=u^6V_C,\qquad \mathcal K=hB^2,\qquad
 \mathcal J=hB.
\]
Their exact actions, before taking any logarithm, are
\[
 \mathcal K:(V_{\rm reg},Z)\longmapsto
       (R^5f^2V_{\rm reg},RZ),\qquad
 \mathcal J:(V_{\rm reg},Z)\longmapsto
       (RfV_{\rm reg},R^2uZ).                  \tag{E95.1}
\]
The identities \(h=\mathcal J^2\mathcal K^{-1}\),
\(B=\mathcal K\mathcal J^{-1}\) recover E93.2 with
every factor of \(f\). The character order
\((V_{\rm reg},Z)\) and the period order
\((\mathcal K,\mathcal J)\) both have determinant
minus one relative to the original orders. The
physical cocharacter is exactly \((1,0)\).

Let \(r,z\) denote the nonnegative valuations of
\(R,u\). The full valuation matrix of E95.1 is
\[
 M(r,z)=r\begin{pmatrix}5&1\\1&2\end{pmatrix}
       +z\begin{pmatrix}0&0\\0&1\end{pmatrix},
 \qquad \det M=9r^2+5rz.                       \tag{E95.2}
\]
Its first matrix is
\(4e_1e_1^{t}+e_2e_2^{t}+(e_1+e_2)(e_1+e_2)^t\).
The integral quadratic refinement is
\[
 \phi(n_1,n_2)=5r\binom{n_1}{2}
             +(2r+z)\binom{n_2}{2}+rn_1n_2.   \tag{E95.3}
\]
For the two standard triangles in each lattice square
with diagonal \(e_1-e_2\), the three transverse slope
increments of its affine interpolation are \(r\),
\(4r\), and \(r+z\). They are nonnegative, and
positive when \(r>0\). This proves convexity of
that interpolation, including every lattice square.
Its dual cell at zero is the following literal hexagon:
\[
\begin{gathered}
 -5r\le X_1\le0,\qquad -2r-z\le X_2\le0,\\
 -4r\le X_1-X_2\le r+z,\\
 (0,0),\ (-4r,0),\ (-5r,-r),\
 (-5r,-2r-z),\ (-r,-2r-z),\ (0,-r-z).
\end{gathered}                                                  \tag{E95.4}
\]
The area is \(9r^2+5rz\). The exact identity
\[
 \phi(n+\ell)-\phi(n)-\phi(\ell)=n^tM(r,z)\ell
\]
proves that the other cells are its translates by
\(M(r,z)\ell\), with the same face intersections.
Thus the cones over these cells, with the base
quadrant retained, form the specified period fan.

Here is a regular refinement with all primitive
vectors given explicitly. Order the lattice coordinates
as \((X_1,X_2,r,z)\). At \(r+z=1\), the lower edge
has vertices
\[
 A=(0,0,0,1),\qquad B=(0,-1,0,1).
\]
The upper polygon is the six vertices in E95.4
with \(r=1,z=0\), embedded at \((r,z)=(1,0)\).
Triangulate that polygon by the eighteen contained
unit triangles of the integer square grid with
slope-one diagonals. Cone each to \(A\). Add
\[
 \langle A,B,(j,-2,1,0),(j+1,-2,1,0)\rangle,
       \quad j=-5,-4,-3,-2,
\]
and
\[
 \langle A,B,(-1,-2,1,0),(0,-1,1,0)\rangle.       \tag{E95.5}
\]
These are the twenty-three cones of the refinement.
They triangulate the full Cayley polytope: the
facets not containing \(A\) are the upper polygon,
the lower horizontal edge joined to \(B\), and
the one remaining diagonal edge joined to \(B\).
Every displayed four-column determinant has absolute
value one.

The exact shared-face maps are
\[
\begin{split}
 T_{\mathcal K}(X_1,X_2,r,z)
   &=(X_1+5r,X_2+r,r,z),\\
 T_{\mathcal J}(X_1,X_2,r,z)
   &=(X_1+r,X_2+2r+z,r,z).
\end{split}                                                   \tag{E95.6}
\]
Across the vertical face the two lower endpoints
are unchanged and both cells use the same \(A\)
diagonal. Across the horizontal face,
\(T_{\mathcal J}\) takes the other cell's \(B\)
to the present \(A\) and takes its four unit edge
pieces to these same four pieces. Across the
diagonal face \(T_{\mathcal K}T_{\mathcal J}^{-1}\)
takes the other \(A\) to this \(B\) and identifies
the single unit edge. The exact certificate compares
the complete three-ray face sets under these maps.
Thus all translated regular cones meet through the
same regular faces.

For a cone with primitive column matrix \(N_\sigma\),
its actual affine chart has coordinates
\[
 z_i=V_{\rm reg}^{a_i}Z^{b_i}R^{c_i}u^{d_i},
 \qquad
 (a_i,b_i,c_i,d_i)=\text{row}_i(N_\sigma^{-1}).
 \tag{E95.7}
\]
The inverse monomial map is given by \(N_\sigma\);
there is no finite quotient because its determinant
is a unit. On a common face the ring arrow is the
literal inclusion of the corresponding dual-cone
semigroups, equivalently these monomial identities
after the face characters are inverted. The actual
\(\mathcal K,\mathcal J\) arrows multiply E95.7
by the full integer powers of \(f\) specified by
E95.1, as well as the displayed \(R,u\) monomials.
Since \(f\) is a base unit, these are holomorphic
unit factors on the charts. Their inverses are the
reciprocal full factors. This lifts the actual
periods, not only their valuations.

All twenty-three charts have zero total physical
weight. Twenty-two have two zero weights and normal
weights \(1,-1\); the remaining chart has
\((-1,1,-1,1)\), in its stored ray order. These
are chartwise statements, before any global orbit
or fixed-component count. The base characters
\(R,u\) pull back to the products specified by the
third and fourth rows of \(N_\sigma\), so the
original functions \(P=uR\) and
\((s,t_{\rm base})\) are retained exactly.

The source-node morphism can also be given on the
whole fundamental cell before further section
refinements. Use the literal source period and put
\[
 Z'=QZ,\qquad W'=Z^{-1},\qquad Z'W'=Q=R^3u^2.
 \tag{E95.8}
\]
Every cone ray has \(b+3r+2z\ge0\) and \(-b\ge0\),
so both expressions are regular monomials on every
chart. The source period is \(h\), with its actual
line factor \(R^{-3}\); this factor remains in
the point-line comparison below.

One literal lift of the actual point \(6G\) in the source-node cover is
\[
 (Z'_6,W'_6)=(u^2,R^3).                         \tag{E95.9}
\]
This lift need not lie in the chosen fundamental cone. The
second lift and its full source/line transition are E99 below.
The full theta identity, with both source point and
section shifted by the same \(Q\), gives
\[
 V_{\rm reg}
   =U_6\,\frac{u^2}{Z'}\,f_{u^2}(Z')v_M.         \tag{E95.10}
\]
In E95.10, \(V_{\rm reg}\) is the original coefficient
pulled into that source-node expression; the actual \(h\)
target coefficient is \(R^{-3}V_{\rm reg}\). Both are
retained. Near \(Z'=W'=R=u=0\),
\[
 u^2 f_{u^2}(Z')=(u^2-Z')\mathcal E,\qquad
 \mathcal E=
 \frac{\prod_{\nu\ge1}
 (1-R^{3\nu}u^{2\nu-2}Z')
 (1-Q^{\nu-1}u^2W')}
 {(1-Z')\prod_{\nu\ge1}
 (1-Q^\nu Z')(1-Q^{\nu-1}W')}.                  \tag{E95.11}
\]
This is a convergent analytic unit with value one.
Thus the point graph is the actual blowup ideal
\((Z',u^2)\), whose two strict-transform charts
are
\[
 Z'=u^2\sigma,\quad \sigma W'=R^3;\qquad
 u^2=Z'\tau,\quad W'=R^3\tau.                   \tag{E95.12}
\]
The section has \(\sigma=1\), respectively
\(\tau=1\). In the second chart its Cartier
generator \(1/(\tau-1)\) is sent by E95.10
to the nonzero frame \(U_6\mathcal E\).
In the first chart \(1/(\sigma-1)\) is sent
to \(-U_6\mathcal E/\sigma\), and the reciprocal
\(\sigma=\tau^{-1}\) is the exact transition.
The full vertical \(\sigma\) factor is retained.
These equations specify the Poincare/Cartier arrow
through the node; resolving the remaining \(A_2\)
and \(A_1\) charts in E95.12 and matching their
period translates is part of the remaining line-graph
attachment, not a discarded base scalar.

Finally the original source volume retains its
exceptional factor here too. Changing from
\((P,R;Z,V_{\rm T})\) to
\((R,u;V_{\rm reg},Z)\) reverses both displayed
orders, while base-dependent Cartier differentials
wedge to zero. Consequently
\[
 \mathcal V_{\rm orig}
  =\frac{2J_{ts}}{a_{\rm T}}\,R\,
        dR\wedge du\wedge d\log V_{\rm reg}
                         \wedge d\log Z.       \tag{E95.13}
\]
The regular cones have canonical height \(r+z=1\).
They retain this additional \(R\) divisor and its
phase in comparison with the original spin frame.
The full inherited spin/cap arrow and the global
compact boundary ledger have not been evaluated
from this local fan.

## E96. The p=1 corner with both actual periods

Put \(v=p-1\) and retain the actual E88 coefficient
\(W_C=s\Delta ZV_{\rm T}\). For \(N=4\), the full
periods are
\[
 h:(Z,W_C)\longmapsto(P^3pZ,p^{-2}W_C),\qquad
 B:(Z,W_C)\longmapsto(P^{-1}Z,P^3v^4cW_C).
 \tag{E96.1}
\]
Their ordinary source/line functions are the same
functions as in E81; the annular cap map is E77.
The actual point coefficient is
\[
 P^3W_C=pU_6 f_{p^{-2}}(Z)v_M.                 \tag{E96.2}
\]
This is E90.9 multiplied by \(P^3Z\).
Its full \(P^3\) Cartier factor is retained; on
\(p=1\) the specified point/O arrow is E91.4 with
\(b_2=p^{-2}\), whose restriction is the identity.
No logarithm is used to discard this factor.

For the source chain and line chain set
\[
 x_i=Z/P^i,\quad y_i=P^{i+1}/Z,\qquad
 U_j=W_C/(P^3v^4)^j,\quad
 V_j=(P^3v^4)^{j+1}/W_C.
\]
They have the exact equations and period maps
\[
 x_iy_i=P,\qquad U_jV_j=P^3v^4=x_i^3y_i^3v^4,
 \tag{E96.3}
\]
\[
\begin{split}
 h:(i,j;x,y,U,V)&\longmapsto
     (i+3,j;px,p^{-1}y,p^{-2}U,p^2V),\\
 B:(i,j;x,y,U,V)&\longmapsto
     (i-1,j+1;x,y,cU,c^{-1}V).
\end{split}                                                   \tag{E96.4}
\]
The finite index of these two index vectors is three.
These are the actual chronological periods, including
the source component movement; no period has been
replaced by its third power.

Resolve the binomial in E96.3 by its ordered factors:
three copies of \(x\), three of \(y\), and four of
\(v\). The same explicit successive blowup construction
as E94 yields ten smooth charts. For \(k=0,1,2\),
the first six charts are
\[
\begin{split}
 x=ab,\quad U=x^ka,\quad
 V=x^{2-k}y^3v^4b
   &\quad(a,b,y,v),\\
 y=ab,\quad U=x^3y^ka,\quad
 V=y^{2-k}v^4b
   &\quad(x,a,b,v).
\end{split}                                                   \tag{E96.5}
\]
For \(k=0,1,2,3\), the remaining four charts are
\[
 v=ab,\quad U=x^3y^3v^ka,\quad V=v^{3-k}b
        \quad(x,y,a,b).                        \tag{E96.6}
\]
Each is a strict-transform chart of a specified
projective blowup, so their union is a smooth proper
graph over E96.3. On all charts the physical action
has exactly two zero weights and normal weights
\(1,-1\).

The lifted \(h\) unit multipliers in the coordinate
orders displayed in E96.5--6 are
\[
 (p^{-k-2},p^{k+3},p^{-1},1),\qquad
 (p,p^{k-5},p^{4-k},1),\qquad
 (p,p^{-1},p^{-2},p^2),
 \tag{E96.7}
\]
respectively. The lifted \(B\) multiplies \(a,b\)
by \(c,c^{-1}\) and fixes the other two coordinates,
besides its index shift in E96.4. Every map is
obtained by substitution in the displayed monomials;
the inverse uses the reciprocal units and opposite
index shift. In particular the full \(H_2=hB^3\)
square is retained.

On the source overlap \(x'=1/y,\ y'=xy^2\), the
first type \(k\) maps to the next second type \(k\)
by
\[
 a'=y^{3-2k}a,\qquad b'=y^{2k-1}b.             \tag{E96.8}
\]
On each \(v\)-factor chart \(a'=a,b'=b\).
The \(U,V\) expressions agree exactly. As in E94,
all remaining overlap centres are principal ideals;
line-chain overlaps are unchanged. Thus these are
actual period-equivariant graph charts on the full
two-chain cover.

In the source representatives \(i=0,1,2\), the
underlying Tate node map is
\[
 Z_0=P^ix_i,\qquad
 W_0=P^{2-i}p\,y_i,\qquad Z_0W_0=Q=P^3p.
 \tag{E96.9}
\]
Both coordinates are regular monomials on the graph
charts. The three representatives and the actual
\(B\) arrow retain every source component.
The point and tensor line frames on their common
open sets are E96.2 and E91.4; their vertical \(P\)
divisors remain part of the line comparison.

For the normalized local volume
\(\Omega_1=dx\wedge dy\wedge dv\wedge dU/U\),
the three chart types again have signs minus, plus,
minus in their displayed complex coordinate orders.
The original volume is
\[
 \mathcal V_{\rm orig}
     =(2J_{ts}/a_{\rm T})\,P\,\Omega_1.          \tag{E96.10}
\]
Both the actual \(P\) canonical divisor and the full
\(P^3\) point-line factor in E96.2 remain in the
inherited spin and Euler-line comparison. The graph
charts provide the local corner and its exact maps;
the period-invariant common refinement with the other
exceptional charts and the compact cap/normal ledger
are still required before evaluating a global pair.

## E97. Every p=0 point-graph chart and its full line coefficient

The base graph E91 admits a point-section description
on all four types of charts. For \(j=0,1,2\),
\[
 P=xy,\quad p=x^jy^{j+1},\quad
 b=P^3/p=x^{3-j}y^{2-j},\quad
 e=p^2=x^{2j}y^{2j+2},\quad be=Q.
 \tag{E97.1}
\]
In the last chart,
\[
 P=x,\quad p=x^3a,\quad b=P^6=x^6,\quad e=a,
 \quad be=Q.                                  \tag{E97.2}
\]
These are the actual lifts of the point \(6G\)
to a Tate source-node chart \(ZW=Q\). Their
common-open transition is the single source period
\(b_{\rm last}=Qb_{\rm previous}\), with the exact
theta/line factor
\[
 f_{P^6}(Z)=-ZP^{-6}f_{P^3/p}(Z).               \tag{E97.3}
\]
Both directions are therefore specified, including
the vertical \(P^{-6}\) factor.

For any of these displayed point pairs \((b,e)\),
the complete product identity near the source node is
\[
 b f_b(Z)=(b-Z)\mathcal E_{b,e},
\]
\[
 \mathcal E_{b,e}=
 \frac{\prod_{\nu\ge1}
 (1-Q^{\nu-1}eZ)(1-Q^{\nu-1}bW)}
 {(1-Z)\prod_{\nu\ge1}
 (1-Q^\nu Z)(1-Q^{\nu-1}W)}.                   \tag{E97.4}
\]
All factors are holomorphic and nonzero on the
indicated node neighbourhood; the product converges
there and has value one at its central node.
The actual section graph is obtained by blowing up
\((Z,b)\). Its strict-transform charts are
\[
 Z=b\sigma,\quad \sigma W=e;\qquad
 b=Z\tau,\quad W=e\tau.                        \tag{E97.5}
\]
Inserting E97.1 gives, respectively, the literal
binomials
\[
\begin{array}{c|c|c}
 j&\sigma W=e& Z\tau=b\\ \hline
 0&\sigma W=y^2&Z\tau=x^3y^2\\
 1&\sigma W=x^2y^4&Z\tau=x^2y\\
 2&\sigma W=x^4y^6&Z\tau=x
\end{array}
\]
and the last chart has \(\sigma W=a\) and
\(Z\tau=x^6\). These equations, together with
the inverse base monomials in E91, are proper graph
projections preserving the exact original \(s,t\).
They locate every remaining section-node direction.
Repeated-factor resolutions use the specified
successive coordinate ideals, just as in E94.

The point section is \(\sigma=1\), respectively
\(\tau=1\). Use its meromorphic Cartier generators
\(e_\sigma=1/(\sigma-1)\) and
\(e_\tau=1/(\tau-1)\); the old \(O\) section is
outside this node chart. For the first three charts
the actual coefficient is
\(V_C=-U_6Z^{-2}f_b(Z)v_M\). Thus its precise
values on these generators are
\[
\begin{split}
 e_\sigma&\longmapsto
       U_6b^{-2}\sigma^{-2}\mathcal E_{b,e},\\
 e_\tau&\longmapsto
       -U_6Z^{-2}\tau^{-1}\mathcal E_{b,e}.
\end{split}                                                   \tag{E97.6}
\]
For the last chart \(V_C=bU_6Z^{-3}f_b(Z)v_M\),
and the two values are
\[
 e_\sigma\longmapsto
       -U_6b^{-2}\sigma^{-3}\mathcal E_{b,e},
 \qquad
 e_\tau\longmapsto U_6Z^{-2}\mathcal E_{b,e}.
 \tag{E97.7}
\]
All powers in E97.6--7 are retained as Cartier
divisors. Their reciprocal maps have the opposite
specified line types. On the common open set,
\(\sigma=\tau^{-1}\), together with E97.3, makes
the two coefficient expressions identical. At the
point/O coincidence \(p=P^3\), the separate smooth
source chart of E91.4 gives the full extending
Cartier isomorphism; the node charts in E97.5 do
not replace that chart.

The actual suspension line map on these charts is
also fixed without choosing a base scalar. In a
first-three-chart point frame put
\(\mu(Z)=-U_6Z^{-2}f_b(Z)\), so \(V_C=\mu(Z)v_M\).
The source arrow is \(Z\mapsto P^{-1}Z\), and
the full E81 suspension is \(V_C\mapsto\lambda qK V_C\).
Its point-frame coefficient is consequently
\[
 v_M\longmapsto
 \lambda qK\,P^{-2}
        \frac{f_b(Z)}{f_b(P^{-1}Z)}\,v_M.
 \tag{E97.8}
\]
This is a typed map from the source line to its
line at the translated point, with the reciprocal
formula as inverse. In the last chart it is obtained
from the same \(\lambda qK\,\mu(Z)/\mu(P^{-1}Z)\)
formula using \(\mu=bU_6Z^{-3}f_b\); thus the
power there is \(P^{-3}\). Equation E97.3 supplies
the literal equality of the two frame descriptions.
The numerator and denominator are the actual target
and source Cartier sections, with their full theta
units in E97.4.

The table supplies local source and line graph maps.
Their compatibility with every translated total-line
corner chart still requires the total-space graph,
including the \(V_C\) powers in E97.6--8.
Blowing up only the source ideals \((Z,b)\) does
not supply that total-line attachment; no global
equivariant quotient of those source graph charts
is asserted here.

## E98. The chosen semifree p=0 resolution and its actual pullback

For the compact comparison choose the following alternative
local resolution of E92.4. The ordered-factor resolution
E94 is retained with all of its verified formulas.
In the cocharacter order \((X_C,Y_C,r,t)\), where
\(r=v(P)\), \(t=v(p)\), take the cone
\[
 -r\le X_C\le0,\qquad -9r-t\le Y_C\le0,
 \qquad r,t\ge0.                               \tag{E98.1}
\]
At height \(r+t=1\) its upper rectangle is
\([-1,0]\times[-9,0]\) and its lower edge is
\(A=(0,0,0,1)\), \(B=(0,-1,0,1)\).
For \(k=-9,\ldots,-1\), its eighteen upper triangles are
\[
 ((-1,k),(0,k),(-1,k+1)),\qquad
 ((0,k),(-1,k+1),(0,k+1)).
\]
Cone each to \(A\), and add
\[
 \langle A,B,(-1,-9,1,0),(0,-9,1,0)\rangle.
 \tag{E98.2}
\]
These nineteen cones are unimodular and triangulate
the cone E98.1. Their exact dual matrices are saved
in the certificate. E92's periods identify their
shared faces: \(H_1\) translates the valuation by
\((r,0)\), and \(K_0=K\) by \((0,9r+t)\);
the actual full units are still those of E92.2.
The physical cocharacter is \((-1,1,0,0)\).
The first eighteen charts have weights \(0,0,1,-1\)
in an appropriate displayed order, and the last
has \(1,-1,1,-1\). These are local chart weights.

The morphism to the original binomial is explicit.
This cell uses the original chain representatives
\((i,j)=(-1,-1)\):
\[
 x=PX_C,\quad y=X_C^{-1},\qquad
 U=P^9pY_C,\quad V=Y_C^{-1}.
 \tag{E98.3}
\]
All four characters have nonnegative pairing with
every cone ray. Therefore the dual-semigroup maps
give holomorphic chart maps satisfying
\[
 xy=P,\qquad UV=P^9p=x^9y^9p.
\]
The fan support is exactly the normal affine
binomial cone defined by these inequalities.
Thus the chart maps are a proper toric refinement;
the valuation of a map from a discrete valuation
ring lies in a displayed cone, giving its extension
there, and the common face maps give the unique
extension. This also gives the inverse on the
dense torus.

The exact change of fundamental cell is
\(H_1^{-1}K_0^{-1}\), whose full coefficient arrow is
\[
 (X_C,Y_C)\longmapsto
 \bigl(P^{-1}b^7X_C,(P^9p)^{-1}b^{-7}Y_C\bigr),
 \qquad d_0=b^{-6}.                            \tag{E98.4}
\]
Thus the period translate includes genuine unit
powers as well as the two index shifts. On the
original source and full corrected line it becomes
\[
 Z\longmapsto P^{-10}p^{-1}Z,\qquad
 V_C\longmapsto P^{31}p^3b^{-7}V_C.
 \tag{E98.5}
\]
This is also the literal word \(B^7h^{-1}\):
\(B\) has source multiplier \(P^{-1}\) and line
multiplier \(P^4/b\), while \(h^{-1}\) has source
multiplier \(Q^{-1}\) and line multiplier \(R^3\).

In the binomial coordinates E98.3 the original
source and line coefficients themselves are
\[
 Z=(yV)^{-1},\qquad V_C=s\Delta V_{\rm T}=y^4V^3.
 \tag{E98.6}
\]
Consequently the full point-line arrows of E97
pull back to
\[
 v_M=-\frac{y^2V}{U_6f_{P^3/p}(Z)}
 \quad\hbox{on the first three base charts},
 \qquad
 v_M=\frac{y}{P^6U_6f_{P^6}(Z)}
 \quad\hbox{on the last}.
 \tag{E98.7}
\]
These are meromorphic coefficient expressions in
the specified Cartier frames, whose section-node
generators and reciprocal maps are E97.5--7.
Their vertical powers have not been deleted.

The actual source-node reindex is also finite on
this fundamental cell. Put \(Q=P^3p\) and
\[
 Z_k=Q^k/(yV),\qquad W_k=Q^{1-k}yV,\qquad
 Z_kW_k=Q.                                     \tag{E98.8}
\]
On E98.1 one has
\(-10r-t\le v(Z)\le0\), while \(v(Q)=3r+t\).
The inequalities
\[
 0\le-v(Z)\le10r+t\le4(3r+t)
\]
show that the five indices \(k=0,\ldots,4\)
suffice: choose \(k=\lceil-v(Z)/v(Q)\rceil\)
when \(v(Q)>0\). Its two node characters then
have nonnegative valuation. The case \(r=t=0\)
is the original torus. A whole four-cone may
require subdivision by the displayed source-height
inequalities; a single \(k\) is not imposed across
a cone whose endpoint rays require different values.
The source \(h^k\) arrow includes the actual line
factor \(R^{-3k}\).

For completeness, every point/source period reindex
used with E98.8 is governed by the full identity
\[
 f_{Q^j b}(Q^kZ)
 =(-1)^jQ^{\,kj-j(j+1)/2}Z^j b^{\,k-j}f_b(Z),
 \qquad j,k\in\mathbb Z.                        \tag{E98.9}
\]
It follows directly from the theta product, with
an integer exponent \(j(j+1)/2\). Together with
E97.4 it fixes the Cartier arrow on each of the
resulting source-node graphs, including all base
powers and signs.

The actual map relating the two p=0 resolutions is
the closure of the identity torus graph in their
fibre product over E92.4, with its toric normalization.
Its two projections are the corresponding
dual-semigroup inclusions and are proper. The
period and physical maps commute with those
projections because their full unit multipliers
agree on the dense torus. No diffeomorphism or
characteristic equality between the two resolutions
is inferred from this birational graph.

The normalized local canonical form in the new
charts is the pullback of
\(dP\wedge dp\wedge d\log X_C\wedge d\log Y_C\);
all cone rays have canonical height \(r+t=1\).
The original volume still contains the full
factor \((2J_{ts}/a_{\rm T})P\), as in E94.9.
The total-line source-height refinement, the
inherited spin/line frames and the other-end
common refinement remain part of the compact
attachment. The local semifree weights in this
section have not been used as a global count.

## E99. The two point lifts on the generic common fan

The root's exact three-fan common refinement is recorded
in code/part3_root/e6_common_period_fan.json; the
independent audit is
records/checks_audit_e6_common_period_fan.json.
Its common character order is \((V_{\rm reg},Z,P)\).
The infinity charts retain the additional unit
\(R=pP\) in their parent monomial maps. Every
common cone has the actual source characters
\[
 Z_1=pP^3Z=QZ,\qquad W_1=Z^{-1},\qquad
 Z_1W_1=Q.
 \tag{E99.1}
\]
Both exponent rows are nonnegative on all 510 regular
cones, and the \(p\) coefficient in \(Z_1\) is
retained. The primitive heights, physical weights
and original canonical orders \(2h-1\) are stored
cone by cone. This is a generic exceptional-annulus
comparison; the full four-dimensional corner graph
is not assigned by that count.

There are two useful lifts of the point \(6G\).
Writing \(b=p^{-2}\), they are
\[
\begin{array}{c|c|c}
 \hbox{old }Z\hbox{ representative}
     &Z_1&W_1\\ \hline
 R^{-3}=P^6/Q^3 &p^{-2}&R^3\\
 p^{-2}=P^6/Q^2 &P^3/p&p^2 .
\end{array}                                                   \tag{E99.2}
\]
The second is the representative on the \(v(Z)=0\)
edge of the common fundamental cell. The first and
second are related by the literal \(h\) arrow
\[
 (Z_1,W_1,V_{\rm reg})\longmapsto
       (QZ_1,Q^{-1}W_1,R^{-3}V_{\rm reg}).
 \tag{E99.3}
\]
This includes its full physical line coefficient.

The point/O graph on the second branch is therefore
the actual ideal
\[
 (W_1-1,p^2-1),                               \tag{E99.4}
\]
which carries both \(p=1\) and \(p=-1\).
The exact theta inversion is
\[
 f_b(W_1^{-1})=b^{-1}f_{b^{-1}}(W_1).
 \tag{E99.5}
\]
Using E90.9 and \(V_{\rm reg}=p^{-6}V_C\), it gives
\[
 V_{\rm reg}
    =R^{-3}U_6\,W_1 f_{p^2}(W_1)\,v_M.
 \tag{E99.6}
\]
No \(R^{-3}\), \(p\), or source-period coefficient
has been placed in an unspecified unit.

Near \(W_1=1\), write the full theta unit as
\[
 f_{p^2}(W_1)
  =\frac{W_1-p^2}{p^2(W_1-1)}\,\mathcal E_O .
\]
The actual Cartier generator
\((W_1-1)/(W_1-p^2)\) is taken by E99.6 to
\[
 R^{-3}U_6\,W_1p^{-2}\mathcal E_O.              \tag{E99.7}
\]
The factor \(R^{-3}\) is the retained vertical
generator. The remaining factor and its reciprocal
extend through both point/O coincidences. Under
\(Z=W_1^{-1}\), the original smooth-section
generator transforms by
\[
 \frac{Z-1}{Z-b}
   =p^2\frac{W_1-1}{W_1-p^2},                 \tag{E99.8}
\]
so the source inversion and its Cartier unit are
specified separately. This proves the complete
local line-arrow dictionary on the generic common
fan, without putting the other node-branch lift
inside its fundamental cell.

The endpoint of the present construction remains
the total-line graph at the four-dimensional
corners, with the original canonical factors and
the finite-isotropy normal pieces introduced by
a regular common refinement. No global return
has been inferred from the local fan counts.

## E100. Actual Cayley corner refinements of the generic common fan

This section extends the audited generic common fan to the native zero and infinity corner domains. The input is the final root certificate with SHA256
\(931e4f8325b7dbc8a795e8b8ff4f0e2a2557bff1a83ae97505de2ec437f77175\).
Its generic lattice is ordered by \((V_{\mathrm{reg}},Z,P)\), and its two positive periods have valuation columns \((5,1)\) and \((1,2)\). The construction below uses the actual native corner coordinate first, then carries its complete map into these common characters.

For a generic cone with zero-parent translate \((i,j)\), subtract
\(((5i+j)h,(i+2j)h)\) from each ray \((X,Y,h)\) and apply
\[
 A_{\infty0}^{-1}=
 \begin{pmatrix}-1&-3\\1&4\end{pmatrix}.
 \tag{E100.1}
\]
The resulting primitive rays lie in their specified E98 upper triangle. Exact deduplication gives 510 regular three-cones, with total upper area \(9\). The source of the common-coordinate map is the native torus \((X_C,Y_C,P,p)\). Its full character matrix is
\[
 \begin{pmatrix}
 -4&-3&5i+j&-6-3i-3j\\
 1&1&i+2j&i+j\\
 0&0&1&0\\
 0&0&0&1
 \end{pmatrix},
 \qquad
 \text{unit column for }b=
 \begin{pmatrix}-2i-j\\0\\0\\0\end{pmatrix}.
 \tag{E100.2}
\]
Thus the powers of the actual corner coordinate \(p\) remain monomials, while
\(b=(p-1)^{-4}c^{-1}\) is the stated nonzero unit on this native zero-end domain. Formula (E100.2) is the complete forward map of the recorded \(K^iJ^j\) parent translate; its inverse is the inverse integral matrix with the corresponding inverse unit. It restricts on \(v(p)=0\) to the exact generic parent arrow.

Put
\[
 A=(0,0,0,1),\qquad B=(0,-1,0,1).
\]
Cone every zero-end upper three-cone with this same native \(A\).
The subdivided bottom edge \(Y=-9h\) has ten two-cones; cone each with \(A,B\).
The result has \(510+10=520\) four-cones. Every determinant is \(\pm1\).
For an upper cone this determinant is, up to sign, the determinant of its three upper rays. For a bottom edge with primitive rays \(v,w\), the four-determinant equals, up to sign,
\(\det((v_X,v_h),(w_X,w_h))\). The actual ten outputs all have absolute value one. Each new cone lies in the recorded original E98 cone: the exact parent coordinate matrix \(N_{\mathrm{old}}^{-1}N_{\mathrm{new}}\) has nonnegative integral entries.

These maps give a proper toric refinement of the complete E98 corner fan. One can check support without a drawing: intersect every cone with \(h+t=1\), and give a four-cone the exact volume
\[
 \frac{|\det(v_1,v_2,v_3,v_4)|}
 {6\prod_{\nu=1}^{4}(h_\nu+t_\nu)}.
 \tag{E100.3}
\]
The new volumes sum to the old volume separately in each of the nineteen original cones. Upper interiors are disjoint by the generic common-fan audit; the ten lower pieces are the subdivisions of the same original \(AB\)-edge cone. The common facets are precisely the shared subdivisions. The complete facet incidence is 708 interior facets and 664 boundary facets.

The native periods extend to these corners by the literal lattice maps
\[
 H_1:(X,Y,h,t)\longmapsto(X+h,Y,h,t),\qquad
 K_0:(X,Y,h,t)\longmapsto(X,Y+9h+t,h,t).
 \tag{E100.4}
\]
The full shared three-facet sets agree under these maps: the \(X=-h\) face maps to \(X=0\), and the \(Y=-9h-t\) face maps to \(Y=0\). The nonzero coefficients are exactly the \(b,d_0=b^{-6}\) coefficients of E92. Every chart map is therefore a monomial map with these retained units, followed by the written period label; this proves its actual equivariant gluing.

For the infinity corner, retain the 510 common upper cones directly in native coordinates \((V_{\mathrm{reg}},Z,R,u)\). Cone them with the E95 lower ray \(A\). The five lower strips of E95 have respective subdivisions of sizes \(1,1,1,1,10\); coning their upper edges with \(A,B\) gives 14 further four-cones. All 524 cones are regular and have nonnegative integral maps into their respective original E95 charts. Exact volume equality holds separately in all 23 parent cones. The incidence is 772 interior facets and 552 boundary facets. The full native-to-common coordinate map, including the height coordinate, is
\[
 (V_{\mathrm{reg}},Z,R,u)\longmapsto
 (V_{\mathrm{reg}},Z,P=Ru,p=u^{-1}),
 \tag{E100.5}
\]
whose character matrix is
\[
 \begin{pmatrix}
 1&0&0&0\\0&1&0&0\\0&0&1&1\\0&0&0&-1
 \end{pmatrix}.
\]
In particular, the \(p\)-unit of the generic infinity comparison is here the actual inverse corner coordinate; it has not been removed.

The complete infinity period maps on these four-lattices are
\[
 \begin{split}
 K(X,Y,r,z)&=(X+5r,Y+r,r,z),\\
 J(X,Y,r,z)&=(X+r,Y+2r+z,r,z),\\
 KJ^{-1}(X,Y,r,z)&=(X+4r,Y-r-z,r,z).
 \end{split}
 \tag{E100.6}
\]
All three paired facet sets agree exactly. Their coefficient maps retain \(f^2,f\), with \(f=(1-u)^4c\), as in E95; this is a unit on the native infinity domain. These formulas supply the actual holomorphic period maps on the new charts.

The physical cocharacters are \((-1,1,0,0)\) at zero and \((1,0,0,0)\) at infinity. For every cone matrix \(N\), its displayed chart action is the integral vector \(N^{-1}\delta\); the certificate stores this complete vector and makes no semifree assertion. The original volume from E94/E95 is a unit times \(P\,dP\,dp\) or \(R\,dR\,du\), multiplied by the two logarithmic torus differentials. Consequently the actual original canonical order on a ray \((X,Y,h,t)\) is
\[
 2h+t-1.
 \tag{E100.7}
\]
Every value is retained. In particular, regularity of a fan chart does not erase the original exceptional canonical divisor or its determinant lift.

There is a complete source projection on every new infinity chart:
\[
 Z_1=R^3u^2 Z,\qquad W_1=Z^{-1}.
 \tag{E100.8}
\]
The exponents \(Y+3r+2z\) and \(-Y\) are nonnegative on all 524 cones, and \(Z_1W_1=R^3u^2=Q\) literally. At zero the five actual source charts are
\[
 Z_k=Q^kX_CY_C,\qquad
 W_k=Q^{1-k}(X_CY_C)^{-1},\qquad 0\leq k\leq4,
 \quad Q=P^3p.
 \tag{E100.9}
\]
Every ray lies in at least one of these source-height sectors. Exactly 144 of the 520 whole cones lie in a single sector; the remaining 376 require the explicit source-height subdivisions. Their cut equations are
\[
 X+Y+k(3h+t)=0,\qquad
 X+Y+(k-1)(3h+t)=0.
 \tag{E100.10}
\]
These obligations are recorded together with the whole-cone source exponents. The source/point-line graph of E97 must also be pulled through these subdivisions with its displayed generators and powers; the present fan construction alone does not complete that total-line graph.

The exact executable record is code/part3/e6_common_corner_lift.py with its JSON, stdout and empty stderr. It passes 9929 checks, including the old-chart support volumes, all parent semigroup arrows, the full four-dimensional periodic facets, physical weights, original canonical orders and source exponents. The first metadata-output attempt shadowed the input path by a source-chart list; its code and output are preserved under records/attempts/e6_common_corner_source_variable. Renaming that local list leaves every geometric check unchanged.

The native \(p=1\) corner refinement, the remaining zero-end source-height cuts and point-line graphs, and the finite-isotropy and compact boundary contributions remain explicit tasks. No total characteristic pair or return is assigned by this corner construction.

## E101. The marked boundary source maps and the stronger periodic-source obstruction

The source comparison required for the collision boundary is the actual Tate/point-line map on its finite marked charts. The following calculation locates a stronger extension requirement that cannot be imposed on the completed periodic atlas.

Fix positive base valuations \(r,t\), with
\[
 Q_{\mathrm{val}}=3r+t,\qquad (3r+t)/r\notin\mathbb Q.
\]
For the zero-end characters the source valuation is \(z=X+Y\). A single actual source node chart has coordinates \(Q^kZ,Q^{1-k}/Z\), and hence its valuation sector is
\[
             -kQ_{\mathrm{val}}\le z\le(1-k)Q_{\mathrm{val}}.
 \tag{E101.1}
\]
The complete period cover contains the literal map
\(H_1:(X,Y)\mapsto(X+r,Y)\). Its action on the source is \(Z\mapsto PZ\). A periodic fan that mapped, on every translate, into one of the unchanged source sectors would have to contain every line \(z=kQ_{\mathrm{val}}\) as a subdivision boundary: a full-dimensional cell crossing such a line lies in no sector (E101.1). Period invariance then forces all lines
\[
                z=kQ_{\mathrm{val}}+nr,\qquad k,n\in\mathbb Z.
 \tag{E101.2}
\]
These parallel lines are dense modulo \(Q_{\mathrm{val}}\). To verify the density directly, apply the pigeonhole principle to \(N+1\) multiples of \(r/Q_{\mathrm{val}}\) modulo one. Two are within \(1/N\), producing a nonzero subgroup element of absolute value at most \(1/N\). Its successive multiples approximate every point of the circle within that distance. As \(N\) increases, the subgroup generated by \(r/Q_{\mathrm{val}}\) is dense. A locally finite polyhedral subdivision has an open two-dimensional cell away from its locally finite boundary faces; the dense family (E101.2) crosses every such cell. This is a contradiction. Thus no locally finite periodic fan has this stronger global map to one unchanged source resolution.

This obstruction preserves the actual addition map rather than replacing it. The \(H_1\) source arrow is \(Z\mapsto PZ\), the \(K_0\) source arrow is \(Z\mapsto P^9pZ\), and the source period itself is \(h=K_0H_1^{-6}\), with multiplier \(Q=P^3p\). The completed total-line atlas retains all these maps. Its comparison with the original family is the literal source and point-line map on the punctured collision boundary and the finite marked source/Cartier graphs E90--E99. No morphism of every added central stratum into one unchanged source resolution is used in that boundary comparison.

The direct coordinate-blowup attempt is retained under records/attempts/e6_p_zero_periodic_source_blowups. Every executed step inserts the sum of the two primitive rays of a regular two-face and the corresponding period-boundary partners. The greedy sequence stopped at its stated 3000-step bound with 12890 cones; it did not complete the source refinement. This is an incomplete attempt, and none of its cones replaces the authoritative E100 completion. Its failure to terminate within that bound is separate from the proved obstruction above.

The actual \(p=1\) corner completion is now also explicit: the common 510 upper cones join the lower \(E_0\) ray, and the four consecutive lower intervals join each of the four subdivided top edges in each of the three source cells. There are 558 regular cones. The full \(p,c,v\) map, in particular \(b=v^{-4}c^{-1}\), is retained before taking any normal derivative. The independent certificate code/part3/e6_p_one_cayley_peer.py passes 6322 checks on all persisted matrices, localized period maps, source exponents and parent support volumes. The proof and full data are in the sibling p-one Cayley note and certificate. Together with E100 this supplies the actual three native corner models with their common generic boundary.

## E102. The actual weighted normal-link and physical line dictionary

Use the same finite-chart construction as SZ.57--60 and IE.9--20. On the complement of invariant fixed tubes the physical circle is locally free. A stabilizer of order \(d\) gives a finite slice chart \(\widetilde U/\mu_d\). Circle averaging and finite averaging give compatible metrics and connections; each chart is integrated as \(d^{-1}\int_{\widetilde U}\). The actual stable tangent map is
\[
 TW|_{\rm locally\ free}\cong\pi^*TZ\oplus\mathbb R_\delta.
 \tag{E102.1}
\]
Therefore the basic form
\[
              \frac{4x^3-p_1(TZ)x}{24}
 \tag{E102.2}
\]
is closed, and Stokes on the finite covers cancels every interior face with its displayed multiplicity. Finite stabilizers remain interior orbifold strata; they do not produce an additional excised boundary. This argument uses the actual quotient line and tangent splitting. It requires no extension of the original boundary Spin structure over the central fourfold.

The sign of the line in this calculation is explicit. Write \(U\) for the positive hyperplane line on the weighted normal quotient, \(u=c_1(U)\). Write \(M\) for the actual physical associated line, in the nonzero-vector convention of K68. The vector in the original normal line gives the map
\[
                         M=U^*,\qquad x=c_1(M)=-u.
 \tag{E102.3}
\]
This is the tautological duality map, with its inverse pairing. Negative-weight normal factors are conjugated only with their stated real orientation reversal, as in SZ.57. The same duality (E102.3) is carried on every finite slice and on its overlaps; no generator is selected by a previously computed residue.

Let a compact fixed component \(F\) have complex normal roots \(x_i\) and signed nonzero physical weights \(w_i\). In the positive-hyperplane notation the two normal-link numbers are
\[
 k_U(F)=[u^{-1}]\int_F\frac{u^3}{\prod_i(x_i+w_i u)},\qquad
 \ell_U(F)=[u^{-1}]\int_F
 \frac{u\{p_1(TF)+\sum_i(x_i+w_i u)^2\}}
      {\prod_i(x_i+w_i u)}.
 \tag{E102.4}
\]
The actual physical line gives
\[
                       (k_M,\ell_M)=(-k_U,-\ell_U).
 \tag{E102.5}
\]
The quotient orientation here is the quotient of the original complex-normal sphere by the positive physical orbit. Removing the fixed tube and taking the circle-first boundary convention give the same inner-face orientation: the two boundary/orbit reversals cancel. The subsequent identification of the outer family with its Jin completion is kept as a separate parameter arrow.

For the charge-three chart of E75, conjugating the two negative normal coordinates preserves the real eight-orientation. The physical quotient is \(\mathbb C^4/\mu_3\) with scalar weight \(1/3\). Its finite-chart normalization gives
\[
 (k_U,\ell_U)=(27,12),\qquad
 (k_M,\ell_M)=(-27,-12).
 \tag{E102.6}
\]
Indeed its positive projective class is \(H\), the actual line is \(\mathcal O(-3)\), and \(p_1(\mathbb P^3)=4H^2\). Thus its physical local expression is \(-4\), agreeing with the direct E75 line and orientation map. Equation (E102.6) verifies the dual-line arrow directly; it is still only that local inner face.

For a compact curve with normal degrees \(d_i=\int_Fx_i\), set
\[
 P_w=\prod_iw_i,\quad S_w=\sum_iw_i^2,\quad A_d=\sum_i d_i/w_i.
\]
The two numbers in (E102.4) are
\[
 k_U=-A_d/P_w,\qquad
 \ell_U=\{2\sum_iw_id_i-S_wA_d\}/P_w.
 \tag{E102.7}
\]
Their combination is exactly the curve residue SZ.58. The entire integer weight vectors, every finite stabilizer denominator and the original complex-normal orientation remain in these formulas.

The original volume orders \(2h+t-1\) from E100 and PC.8 are retained in the actual determinant comparison. They do not need to vanish for the finite-chart Stokes argument. Their role at the external boundary is supplied by the original source/Cartier volume and the full period Jacobians, rather than by choosing a new central determinant trivialization.

## E103. Full three-end normal clutches of the compact generic fixed curves

Let \(N\) be an ordered generic common cone, with columns
\((X_i,Y_i,h_i)\). Its three physical weights are
\[
                        w=N^{-1}(1,0,0)^{\mathsf T}.
\]
There are 276 cones for which every entry is nonzero. The fixed locus in each of the corresponding upper corner stars is the lower-coordinate axis. At zero it is the \(p\)-axis, at one the \(v=p-1\) axis, and at infinity the \(u=p^{-1}\) axis. The generic locus is the same curve with coordinate \(p\). All three maps are the already specified native-to-common character maps, so they glue to one copy of \(\mathbb P^1_p\).

There is no additional period quotient of this curve. A nonzero period translate moves the normalized full-dimensional generic triangle by a nonzero vector in \(M\mathbb Z^2\). It cannot preserve its bounded triangle. Thus its period stabilizer is zero. Distinct generic full cones give distinct fixed curves, and the fixed-set dimension at each endpoint remains one because the same three normal weights remain nonzero. No further fixed branch meets this curve.

Let \((i_0,j_0)\) be its recorded zero-parent period translate, and let \((i_1,j_1)\) be its one-parent translate. In the common character order \((V_{\rm reg},Z,P)\), the three lower-ray exponents are
\[
 \begin{split}
 d_0&=(-6-3i_0-3j_0,\ i_0+j_0,\ 0)^{\mathsf T},\\
 d_1&=(4(2i_1+j_1),\ 0,\ 0)^{\mathsf T},\\
 d_\infty&=(0,0,1)^{\mathsf T}.
 \end{split}
 \tag{E103.1}
\]
These are obtained by applying the full four-dimensional character matrix to the actual lower ray of each end chart. In particular, the \(p=1\) exponent is computed after substituting \(b=v^{-4}c^{-1}\), and the infinity exponent is the actual height arrow \(P=Ru\).

In the normal coordinate order dual to \(N\), put
\[
 a_0=N^{-1}d_0,\qquad a_1=N^{-1}d_1,\qquad
 a_\infty=N^{-1}d_\infty.
\]
The literal coefficient maps are
\[
 \theta_{\rm common}
   =p^{a_0}\,g_0\,\theta_0,\qquad
 \theta_{\rm common}
   =v^{a_1}\,g_1\,\theta_1,\qquad
 \theta_{\rm common}
   =u^{a_\infty}\,g_\infty\,\theta_\infty.
 \tag{E103.2}
\]
Each \(g_\nu\) is the complete nonzero unit from the corresponding parent map. These equations include the fixed matched permutation of the three normal coordinates. They are exactly diagonal on the normal linearization: the common upper-ray matrices agree, and differentiation of a base-dependent coefficient multiplies a vanishing normal coordinate. Hence such derivatives add no unrecorded normal mixing.

The coefficients \(c,U_6\) extend as nonzero functions of the original bidisc \((P,R)\); their restrictions to its exceptional curve are nonzero constants. The other factors in \(g_\nu\) are the displayed powers of \(p\), \(p-1\) that are units on their respective local discs. All zeros and poles on \(\mathbb P^1\) are therefore those in (E103.1). No scalar with unrecorded winding is inserted.

For the \(i\)-th normal line, the vector-frame equation is
\(e_\nu=p_\nu^{a_{\nu,i}}g_{\nu,i}e_{\rm common}\).
The meromorphic common frame has order \(-a_{\nu,i}\) at that endpoint. Consequently the actual normal degrees are
\[
                         \deg L_i=-a_{0,i}-a_{1,i}-a_{\infty,i}.
 \tag{E103.3}
\]
This derives their sign from the coefficient-to-vector-frame map. As a separate check of the full determinant, every one of the 276 curves satisfies
\[
 \sum_i h_i\deg L_i=-1,\qquad
 \sum_i(2h_i-1)\deg L_i=-2-\sum_i\deg L_i.
 \tag{E103.4}
\]
The second equation is exactly adjunction with \(K_{\mathbb P^1}\), using the original canonical orders of the common atlas. It retains the original exceptional determinant factor.

Substituting these individual degrees and weights into (E102.7) gives the following sums over precisely these compact generic curves:
\[
 \sum(k_U,\ell_U)=\left(\frac{1895}{18},\frac{50}{3}\right),
 \qquad
 \sum(k_M,\ell_M)=\left(-\frac{1895}{18},-\frac{50}{3}\right).
 \tag{E103.5}
\]
Their positive-hyperplane residue is \(455/27\); their physical inner-face residue is \(-455/27\). These rational sums retain the finite normal-weight denominators. They omit the fixed surfaces, corner-interior components, external reference pieces and outer-boundary transfer.

The complete certificate code/part3/e6_generic_fixed_curve_normals.py independently recomputes every lower-ray exponent from all three persisted corner maps. It passes 5229 checks, stores every line degree and each separate characteristic pair, and verifies (E103.4) component by component. This is a completed calculation of the specified compact curves, and gives no total return.


## E104. The exact scalar-chain boundary of the collision completion

Choose a small closed source-base disc \(U=\{|t|\leq\eta\}\) around the order-three collision, disjoint from the selected I1 value and the quadratic cap. On a collar of \(\partial U\), for every sufficiently small source parameter, the functions \(P,R,u_s\) and the source coordinate on each marked Tate chart are nonzero. Keep the actual functions \(R-P=s u_s\), \(v=p-1=s u_s/P\), \(c=\lambda_0qK u_s^{-4}\), and \(W_C=ZV_C\). No source-period representative is changed without its displayed line multiplier.

For \(j\in\mathbb Z\), \(0\leq l\leq3\), put \(k=4j+l\). The four lower factor charts of E96 have the exact coordinates
\[
 a=\frac{W_C}{P^{3(j+1)}v^k},\qquad
 b=\frac{P^{3(j+1)}v^{k+1}}{W_C},\qquad ab=v.
 \tag{E104.1}
\]
They are carried to the ordinary scalar chain by
\[
 \begin{split}
 U_k=V_C/s^k
    &=P^{3(j+1)-k}u_s^kZ^{-1}a,\\
 V_k=s^{k+1}/V_C
    &=ZP^{k+1-3(j+1)}u_s^{-k-1}b,
 \qquad U_kV_k=s.
 \end{split}
 \tag{E104.2}
\]
On this boundary collar the displayed coefficient factors and their reciprocals are smooth holomorphic units. The inverse map divides by exactly these factors. Both maps commute with the physical action, which has weights \((+1,-1)\) on either pair. The identity \(ab=v\) is sent to \(U_kV_k=(P/u_s)v=s\), retaining the original degeneration parameter.

The actual source period is
\[
 h:(Z,a,b)\longmapsto(P^3pZ,p^{-2}a,p^2b).
\]
After substituting in E104.2 its normal arrow is
\[
          h:(U_k,V_k)\longmapsto(R^{-3}U_k,R^3V_k).
 \tag{E104.3}
\]
The actual suspension is
\[
 B:(j,k,Z,a,b)\longmapsto
       (j+1,k+4,P^{-1}Z,ca,c^{-1}b).
\]
Its complete transformed arrow is
\[
 (U_{k+4},V_{k+4})(Bz)
       =(\lambda_0qK\,U_k(z),(\lambda_0qK)^{-1}V_k(z)),
 \tag{E104.4}
\]
where the target labels mean the coordinates of the transported point in the target chart. Indeed the extra factors are \(u_s^4c\) and its inverse, and \(u_s^4c=\lambda_0qK\) literally. Thus this is the chain of the original suspension \(s^4\lambda_0qK\), including its full source translation. There is no bounded-unit replacement of that translation.

The coordinate \(V_C=s\Delta V_T\) in E104.2 is the actual typed point-line coordinate from E90 and E99. Its comparison with the uncorrected ordinary line is E88.5, including the label shift by one and the complete unit \(e=P\Delta/u_s\). At a point/O coincidence its extending arrow is the module map E99.7 on the Cartier generator E99.8. It is not defined by setting \(s\Delta\) equal to a nonzero scalar at the central parameter.

The root and cap labels are also retained. On the actual quadratic cap the scalar root is \(r_0s^2\); its primitive root map shifts a scalar-chain label by two, and its square shifts it by four and equals the actual \(B_0\) norm. Write \(\tau_s=\log s/(2\pi i)\), \(s_\infty=\log q_\infty/(2\pi i)\), and keep \(q=q_\infty^{-1}h\). The complete annular origin square is
\[
 \begin{split}
 F&=F_0+2\tau_s s_\infty\delta,\\
 o_{\mathrm{ord}}&=2\tau_s\frac{\log q}{2\pi i}\delta,
 \qquad
 o_{\mathrm{cap}}=2\tau_s\frac{\log h}{2\pi i}\delta,\\
                  F+o_{\mathrm{ord}}-o_{\mathrm{cap}}&=F_0.
 \end{split}
 \tag{E104.5}
\]
Its initial-to-endpoint maps are \(q^2\) and \(h^2\), and its endpoint-to-initial maps are their inverses. The equality \(q_\infty^2q^2=h^2\) is the directed closing square, with the full root character and reference integral cochain of E77 and E87. The equality of these full annular maps, rather than equality of only their norms, is used at the cap.

The executable certificate code/part3/e6_collision_boundary_chain.py checks E104.1--5, their inverse exponents, every chart-index formula and both physical weights. The initial exact arithmetic run passes 291 checks; the full point-frame and all-integer additions through E106 raise the current count to 299. It establishes these boundary morphisms; it assigns no characteristic integral to the four lower surface patches.

## E105. The relative exterior comparison and the retained lower surfaces

The source resolution itself has an actual smooth family across this collision. In the first blowup chart \(U=xU_1\), its remaining equation is \(U_1V=x(x-s)\). The marked small resolution has
\[
 x=S_0T_0,\qquad x-s=S_1T_1,
 \qquad s=S_0T_0-S_1T_1,
 \qquad (S_0,S_1)\ne(0,0).
 \tag{E105.1}
\]
The differential of the last function has a nonzero \(T_0\) or \(T_1\) coefficient. In the other first-blowup chart \(x=Ux_1\), the equation gives \(V=Ux_1^2(Ux_1-s)\) and \(s\) is an independent coordinate. These are the two actual source-resolution charts; together they prove that projection to the source parameter is a submersion. Shrink \(U\) so that its boundary contains no moving singular source fibre. Its source family is then a proper smooth family with boundary. The original section, point-line Cartier data and the full root/cap maps remain those of E61--E77.

Fix a nonzero reference source parameter \(s_*\). Use an independent real variable \(a\in[0,1]\), put
\[
                         \sigma_a(s)=(1-a)s+a s_*,
 \tag{E105.2}
\]
and retain \(s\) as the scalar-chain parameter. Thus the chain equation is always \(U_kV_k=s\), and the scalar is always \(s^4\lambda_0\). The actual source parameter is \(\sigma_a(s)\). On the collar of \(\partial U\) its source surface is smooth, its full point line and translation extend, and the actual invertible suspension lift is \(B_0(\sigma_a(s))\). Its chain action shifts \(k\) by four, with that complete source and line map. The root chart has the actual two-step map and the exact square E104.5.

Projection to \(a\) on this chain family is a submersion, including its central nodes. To give the local lift explicitly, choose a source-family chart and a frame of its actual point line, lift \(\partial_a\) in that source chart, and take zero derivatives of the two chain coordinates. The equation \(U_kV_k=s\) is preserved because \(s\) is fixed. Across a change of line frame by \(g\), the same vector field has the opposite additional normal terms \((\partial_a\log g)U_k\) and \(- (\partial_a\log g)V_k\). Across a suspension overlap one applies the derivative of the complete source and line map \(B_0(\sigma_a(s))\). These are typed lifts on the quotient charts, including all unit derivatives. No lift in the degeneration direction \(\partial_s\) at a node is used.

Take a finite partition of unity on the compact quotient collar, keep the prescribed E104 maps on its boundary, and average the resulting field over the physical circle and the finite root group. Its \(a\)-component remains one and its \(s,t\)-components remain zero. A fundamental cover has four consecutive chain labels over the compact source collar; the nonzero suspension shifts this finite cover into successive labels. This makes the flow complete for \(0\leq a\leq1\). It gives an actual equivariant boundary diffeomorphism between the collision scalar-chain collar and the fixed-source scalar-chain collar, with the source, physical line and normal derivatives transported by the displayed formulas.

The same construction on the complement of \(U\) uses the original full cap and annular cochain of E104.5. On the outer parameter circle the selected I1 remains disjoint from this collision. Its source-node, Picard and Hom coefficients are the actual extending coefficients on the full source-parameter disc. Near the selected tube, prescribe their literal Cox-coordinate map with the physical height character \(q\) unchanged. On an overlap the opposite weight-normal gauges and the complete period label are retained. The resulting normal arrow transports the physical Hopf line, and its fixed three-ball extension is the product arrow of K42/K68. Thus the selected conifold replacement is carried on both sides of the exterior comparison, with the first-to-second clutch direction from K68. This comparison uses only the outer smooth family and the collar chain construction above; it does not construct an additional holomorphic selected central corner.

There are four lower fixed surface patches in the collision completion and four in the fixed-source scalar chain. Their boundaries are paired by this actual flow. The scalar-chain labels are reduced modulo four only after applying the full source/line suspension; the root labels reduce by two through the specified quadratic cap. The relative comparison closes each collision patch with an oppositely oriented reference patch. The normal bundles on those closed doubles are glued by the actual derivative of the boundary flow, including E104.2 and the point-line generator map. Their relative characteristic classes must therefore be calculated in those prescribed frames.

The four collision normal bundles have explicit local holomorphic frames in the p=1 lower-factor charts: the adjacent source-chart map leaves \(a\) unchanged, \(h\) multiplies it by \(p^{-2}=1\), and \(B\) carries \((j,a)\) to \((j+1,ca)\). Hence
\[
                a_{\rm ref}=c^{-j}a,\qquad
                b_{\rm ref}=c^j b
 \tag{E105.3}
\]
are invariant frames on each lower surface. The exact comparison to the original chain on the boundary is still
\[
 U_k=P^{3(j+1)-k}u_s^kZ^{-1}c^j a_{\rm ref},
 \tag{E105.4}
\]
with its inverse counterpart. Formula E105.3 alone does not compute the relative normal square in this boundary marking. In particular E105.4 contains the source period and the entire Cartier divisor. The reference line class already retained in E73 is \(D=3F-C_1+C_2\), with \(D^2=-6\); its conjugated determinant is \(2D\), with square \(-24\). The boundary map, any connecting class, the tangent double and the selected-tube completion are kept in the final ledger before using those numbers.

The completed compact generic strata of E103 and the independent 117-surface calculation give the separate subtotal
\[
 (k_M,\ell_M)_{\rm compact}=(-45,120),
 \qquad \frac{4k_M-\ell_M}{24}=-\frac{25}{2}.
 \tag{E105.5}
\]
This includes both distinct ten-point corner blocks, one at zero and one at infinity. It excludes all four lower/reference doubles and the external completion. The arithmetic diagnostic obtained by substituting only four formal \((18,0)\) doubles is \((27,120)\), with expression \(-1/2\). That substitution has not established the final relative normal and external boundary map, and no return is assigned to it. It is retained to expose the precise remaining integral consistency check rather than to choose a missing term from a desired residue.


## E106. The whole point-frame map at the lower boundary

The scalar chain in E104 is written in the completed coefficient \(V_C\). To compare its normal frame with the original physical point line, one must compose E90's entire typed coefficient map. Put \(V_{\rm pt}=f_{P^6}(Z)v_M\), in the actual point-theta frame. Then
\[
 V_C=P^6U_6Z^{-3}V_{\rm pt},\qquad
 H:(V_C\longmapsto V_{\rm pt})=P^{-6}U_6^{-1}Z^3V_C.
 \tag{E106.1}
\]
Its inverse has the reciprocal displayed factor. These are coefficient arrows between their specified line frames; the source-period multipliers on the two sides differ and are explicitly intertwined below. On the collar of \(\partial U\) every factor in H is nonzero. At a point/O coincidence the extension is by E99.7 on its stated Cartier generator, rather than by treating a meromorphic theta ratio as a nonzero function.

For the representative \(j=0\), \(k=l\), the complete reference point-frame scalar normal is
\[
 U_l^{\rm pt}=V_{\rm pt}/s^l
   =P^{-3-l}u_s^l U_6^{-1}Z^2a_{\rm ref}.
 \tag{E106.2}
\]
For arbitrary \(j,k=4j+l\) it is
\[
 U_k^{\rm pt}
  =P^{3(j+1)-k-6}u_s^kU_6^{-1}Z^2c^j a_{\rm ref}.
 \tag{E106.3}
\]
The inverse negative normal coefficient is exactly its reciprocal times \(s\). Consequently the source-coordinate exponent in the reference normal map is \(+2\), after the full point-line comparison. E105.4 remains the correct \(V_C\)-chain map; using it directly as an original point-line frame would omit H.

The actual period arrows verify the type of H. Since \(Q=P^2R\),
\[
 H\circ h_C=h_{\rm pt}\circ H,
 \qquad h_{\rm pt}:(Z,V_{\rm pt})\longmapsto(QZ,P^6V_{\rm pt}).
 \tag{E106.4}
\]
Indeed \(Q^3R^{-3}=P^6\). The suspension arrow is
\[
 H\circ B_C=B_{\rm pt}\circ H,
 \qquad B_{\rm pt}:(Z,V_{\rm pt})\longmapsto
       (P^{-1}Z,\lambda qK P^{-3}V_{\rm pt}).
 \tag{E106.5}
\]
All \(P,R,U_6\) are source-base functions fixed by these translations. The factor \(P^{-3}\) in E106.5 is therefore the literal result of the source translation in \(Z^3\); it is not a new bounded scalar. In the point-frame scalar chain the four-step arrow has coefficient \(\lambda_0qK P^{-3}\), with its reciprocal on the negative normal coordinate.

The annular map F0 in E77 is the original point-line/root map. On a boundary chart written in \(V_C\), the actual map into that annular comparison is consequently \(F_{\rm pt}\circ H\). Its inverse is \(H^{-1}\circ F_{\rm pt}^{-1}\). E104.5 and the \(q^2/h^2\) closing square apply to \(F_{\rm pt}\); these physical scalars commute with H. Hence the composed map has the same directed closing, while retaining all of H's source and line powers. This supplies the missing typing in the provisional reference paragraph E105: the collar flow must be prescribed after E106.1, not after an identity between the two differently marked line coefficients.

The remaining relative calculation must use E106.2--5 at the lower surfaces, the actual finite-cap character in E77, and the selected Cox/physical Hopf coefficient at its exterior end. Neither the compact subtotal E105.5 nor the formal four-double substitution is asserted to be the completed characteristic expression.


To keep the complete lower representative, apply the literal deck \(B^{-j}\) before comparing the fixed-source chart. It sends the source-cell label to \(I=i+j\), the source coordinate to \(Z_*=P^jZ\), and the normal coordinates to \(a_{\rm ref}=c^{-j}a\), \(b_{\rm ref}=c^jb\). The inverse is the stated \(B^j\) with its full source and line multipliers. Formula E106.3 then becomes
\[
 U_k^{\rm pt}
 =P^{-3-l}u_s^lU_6^{-1}Z_*^2
       (\lambda_0qK P^{-3})^j a_{\rm ref}.
 \tag{E106.6}
\]
Thus the remaining \(j\)-factor is precisely the point-frame suspension coefficient E106.5; it is not absorbed into a reference logarithm. This equality also verifies that the point-frame comparison commutes with the actual source-cell and chain representative, including the full \(c\) factor.


## E107. The executed lower-source blowups and the relative tangent term

The lower surface's native source charts in E105 are its blowdown parent. The actual 558-cone refinement introduces three specified source blowups in each of its three node quadrants. This correction is read from the executed matrices, independently of any characteristic subtotal.

For each fixed lower label \(l\), each of the three parent source quadrants \(xy=P\) has four charts. In their recorded tangent-coordinate orders they map to the parent by
\[
 (x,y)=(rt,r^2t),\quad(rt^2,rt),\quad(rt^2,t),\quad(t,rt^2).
 \tag{E107.1}
\]
Their complete source fan has rays
\[
       (1,0),(2,1),(1,1),(1,2),(0,1).
 \tag{E107.2}
\]
First add \((1,1)=(1,0)+(0,1)\), then add \((2,1)=(1,0)+(1,1)\) and \((1,2)=(1,1)+(0,1)\). The two coordinate maps at each step are \((r,t)\mapsto(r,rt)\) and \((r,t)\mapsto(rt,t)\), with their literal reciprocal overlap. They factor every map E107.1. Thus this is the proper composition of three ordinary point blowups at the node and its two specified infinitely near points. The blowdown is the identity on the protected source boundary.

All 48 full parent matrices have zero source exponents in the two physical normal coordinates, and their two normal rows are exactly \(a,b\), up to the recorded permutation. No tangent monomial appears in a normal row. Their source two-by-two determinants are \(\pm1\), and their supports are the complete quadrant E107.2. The actual source period carries the three quadrants cyclically. Hence every one of the four lower fixed surface patches is the ninefold blowup of its minimal I3 parent, and its physical normal bundle is the literal pullback of E105.3.

In strict exceptional order \((2,1),(1,1),(1,2)\), the intersection matrix at one node is
\[
 I_E=\begin{pmatrix}-1&1&0\\1&-3&1\\0&1&-1\end{pmatrix}.
 \tag{E107.3}
\]
The total-transform vectors \((1,1,1),(1,0,0),(0,0,1)\) give an integral basis with determinant \(-1\), carrying this matrix to \(-I_3\). The actual relative canonical divisor has strict coefficients \((2,1,2)\), from the Jacobians
\(-r^2t,-rt^2,t^2,-t^2\) of E107.1. Its square is \(-3\). The three exceptional replacements increase the Euler number by three. Consequently each node changes the relative tangent Pontryagin number by \(-3-2\cdot3=-9\), and each lower surface changes it by
\[
                \Delta\langle p_1(TF),[F,\partial F]\rangle=-27.
 \tag{E107.4}
\]
The boundary identification here is the identity of the proper blowdown. The remaining parent source family is the explicit submersion E105.1. All original volume factors, including the coefficient \(-(2J_{ts}/a_T)P\) in the lower chart and the above Jacobians, remain in the actual determinant arrow.

The independent audit code/part3/e6_lower_surface_blowups_peer.py checks all 48 persisted parent matrices and the complete three-step fan, passing 412 checks. Its first JSON serialization attempt failed only after the geometric checks, because a SymPy integer had not been converted to a Python integer; that code and output are retained. The corrected run changes no matrix or geometric assertion. The full native source, point-line, normal and boundary proof is notes/part3_e6_order_three_lower_surfaces_working.md, LS.1--4, with its separate 238-check certificate.

This fixes the tangent omission in the earlier minimal-parent diagnostic E105.5. It does not select a missing contribution from that diagnostic: the nine blowups and all their normal derivatives were extracted first from the executed atlas. The full relative normal squares still use E106's point-frame arrow, and the actual outer comparison retains the finite cap and the selected physical Hopf line.

The relative outer object is also fixed here to avoid subtracting the scalar reference twice. The actual relative filling is the collision completion with \(\lambda=s^4\lambda_0\) glued to the oppositely oriented fixed-source completion with the same scalar. Their parameter words are \((1,2)\) and \((0,2)\) in the E87 source/quadratic-scalar-root torus. The exact E87 map therefore gives the difference word \((1,0)\), the fixed-scalar source loop. An absolute coupled characteristic pair would additionally include the actual scalar reference; it is not the relative pair constructed here. No scalar baseline is inserted to decide the remaining boundary or line arrow.


## E108. The actual closed lower-double normal classes

The reference normal lines in this section are the original point line and its inverse. This is fixed by E106, not by identifying its coefficient with \(V_C\). On the reference scalar chain the coordinates are \(V_{\rm pt}/s^k\) and \(s^{k+1}/V_{\rm pt}\); a point-line frame change by \(g\) acts as \((g,g^{-1})\). Thus the two reference complex normal bundles, with their physical characters \((+1,-1)\), are literally
\[
                      M_6\oplus M_6^{-1}.
 \tag{E108.1}
\]
The comparison from the executed collision chart is the complete map E106.6 and its negative counterpart in LS.13b. It commutes with both full source periods by E106.4--5, and its cap composition is \(F_{\rm pt}\circ H\), with the stated inverse. These equations specify the reference line whose class is evaluated below.

The parent source in LS.7 is the actual Tate minimal source with \(Q=P^3\). The source-base change is \(t=t(P,P)\), with nonzero derivative \(1/2\) at the origin. The full E81 Tate/Weierstrass morphism therefore identifies it with the central minimal I3 source of E63, preserving the ordered source cycle and O. One may verify the extension by the three literal charts \(x_Iy_I=P\) and their adjacent inverses in LS.7; they resolve the same actual Weierstrass nodal equation and have no exceptional \((-1)\)-curve over that equation. The marked source small-resolution family E105.1 transports this source with boundary to the chosen fixed-source reference.

The actual Cartier family is E73.3--7. Transporting its point line through that source family gives the reference class
\[
 D=3F-C_1+C_2=(3,2,4),\quad
 D^2=-6,\quad D\cdot F=0,
 \tag{E108.2}
\]
where \(F=C_0+C_1+C_2\). Its intersection matrix in the ordered primitive component basis is
\[
 I_{I_3}=\begin{pmatrix}-2&1&1\\1&-2&1\\1&1&-2\end{pmatrix}.
 \tag{E108.3}
\]
All three components are actual source curves. The canonical divisor section of \(\mathcal O(D)\) is nonzero on the outer boundary, since its divisor is contained in the central fibre. E73's full \(s\Delta r_6\) Cartier map and E106's point-frame map carry this section to the original point line. Hence the boundary restriction of this reference Chern class vanishes integrally, not only rationally. The nine blowups on the collision side are interior and their two normal rows are unchanged; no exceptional normal-line coefficient is added.

Here is the full boundary-gauge calculation. The three actual node charts \(xy=P\) give three Lefschetz handles with the same primitive vanishing cycle \(a\). The loop through the three components is denoted \(b\). Thus the source patch has \(H_1=\mathbb Z\langle b\rangle\). Its boundary has the literal torus-mapping-torus presentation
\[
 [a,b]=1,\qquad \alpha a\alpha^{-1}=a,\qquad
 \alpha b\alpha^{-1}=a^3b.
 \tag{E108.4}
\]
The exponent three is the actual period \(Q=P^3\); it is also the product of the three node-chart monodromies. Abelianization gives
\[
 H_1(\partial S;\mathbb Z)
   =\mathbb Z\langle b,\alpha\rangle\oplus
     \mathbb Z/3\langle a\rangle.
 \tag{E108.5}
\]
The source inclusion keeps \(b\). The primitive vanishing-cycle handles kill \(a\), and the actual O-section disc kills \(\alpha\). Therefore the quotient of integral boundary \(H^1\) by the image of source \(H^1\) is generated by the primitive base-circle class \(\alpha^*\). There is no missing homomorphism from the torsion cycle to \(\mathbb Z\).

On the doubled source, the clutch with actual frame relation
\[
                    e_R=(t/\eta)e_L
 \tag{E108.6}
\]
has the meromorphic section \((t/\eta)e_L\) on the left and \(e_R\) on the right. It has precisely the fibre divisor \(F\). Hence the Mayer--Vietoris connecting map sends the actual \(\alpha^*\) to the class of \(F\), with this direction and coefficient one. The source coordinate \(P\) has the same positive boundary winding as \(t\), because their actual ratio extends nonzero.

Apply this map to the two actual boundary coefficient gauges in E106.6 and LS.13b, after using the reference divisor frame of E108.2. Their \(b^*\) components extend over the source. Their remaining components are integral multiples \(\nu_+\alpha^*,\nu_-\alpha^*\), with \(\nu_\pm\) defined by the degree of those full coefficient ratios on the oriented base circle. Thus their actual effect on the glued normal classes is addition of \(\nu_+F,\nu_-F\). This retains the full powers of \(P,Z_*,u_s,U_6\), the suspension unit and the cap arrow; it does not replace their logarithms by zero. The equalities
\[
                        F^2=0,\qquad D\cdot F=0
 \tag{E108.7}
\]
follow by moving a smooth nearby fibre away from the central components. They also follow directly from E108.3. Consequently those actual connecting classes change none of the two normal squares or their mixed product.

The normal boundary flow can be chosen to retain the two original complex normal lines. In every source/line chart its normal linearization multiplies the positive line by the actual complex frame coefficient and the negative line by its reciprocal. Derivatives of the source parameter \(s=U_kV_k\) vanish in either normal direction along the fixed surface. A physical-circle-invariant partition has no linear term in either nonzero-weight normal coordinate. Thus the patched field of E105 has the same complex diagonal normal linearization. Its flow and the point-frame map H preserve the two signed complex eigenlines. The finite root and cap maps are complex-linear on the physical line and preserve these signs as well.

Let \(x_+,x_-\) be the two complex normal Chern classes on one closed collision-minus-reference lower double. The collision classes are zero by LS.8, the reference classes are \(D,-D\) by E108.1, and the reference surface has the opposite orientation. Equations E108.6--7 therefore give the actual equalities
\[
 \int x_+^2=6,\qquad \int x_+x_-=-6,\qquad
 \int x_-^2=6.
 \tag{E108.8}
\]
In particular the positive-spinor determinant \(x_+-x_-\) has square 24, while \(x_++x_-\) has square zero. The tangent comparison is E107.4: the parent source family is a boundary-preserving diffeomorphism, and its nine actual blowups contribute \(-27\). For normal weights \((+1,-1)\), the E102 expansion, with physical \(M=U^*\), is
\[
 k_M=\int(x_+^2+x_-^2-x_+x_-),\qquad
 \ell_M=\int\{p_1(TF)+(x_++x_-)^2\}.
 \tag{E108.9}
\]
Thus each of the four closed lower doubles has the physical inner pair
\[
                             (k_M,\ell_M)=(18,-27).
 \tag{E108.10}
\]
Adding precisely the four doubles to the compact subtotal of E105.5 gives the complete fixed-inner pair for this relative filling,
\[
                         (k_M,\ell_M)_{\rm inner}=(27,12).
 \tag{E108.11}
\]
This is the inner boundary calculation, with its actual physical line and all reference gauges. The outer family and Jin parameter reversal are separate maps. The exact integral arithmetic and gauge independence are recorded in code/part3/e6_order_three_relative_double.py; its current 16 checks do not substitute for the source, normal, Cartier and cap morphisms just specified.


## E109. The compact relative filling and actual outer physical transfer

The three native corner models are the complete 520, 558 and 524 chart models of E100--101 and PC. Their generic overlap is the actual 510-cone period comparison, including all \(p,b,c,f\) coefficients. They construct the completion of the total physical line over the blowup of the actual \((P,R)\) bidisc. The original base functions \(s,t\) are the E81 analytic functions of \(P,R\); they remain functions on this completion. A central map to a single unchanged source resolution is neither introduced nor used: E101 proves the obstruction to that stronger requirement. The comparison with the original family is the actual source/Cartier map on every required marked boundary chart, E90--99 and E104--106.

Here are the properness and face identifications for the compact cut. On the three native valuation planes the two lattice matrices are respectively
\[
 \begin{pmatrix}r&0\\0&9r+t\end{pmatrix},\qquad
 \begin{pmatrix}3r&-r\\0&3r+4t\end{pmatrix},\qquad
 \begin{pmatrix}5r&r\\r&2r+t\end{pmatrix}.
 \tag{E109.1}
\]
Their determinants are \(r(9r+t)\), \(9r^2+12rt\), and \(9r^2+5rt\). For positive heights these are positive. The native polytopes of E98, E96 and E95 are finite fundamental domains for these literal lattice translations; their shared faces are paired by the saved full period maps. E100 and PC verify the support equality separately in every parent cone, all primitive multiplicities and all nonnegative integral monomial maps. The common refinements are proper toric refinements of those same supports.

On the lower rank-one ends, the remaining period is not replaced by the identity. At zero it acts on the source unit by \(Z\mapsto PZ\); at one it is \(Z\mapsto P^3pZ\); at infinity it is \(Z\mapsto RZ\). On each corresponding source annulus it is an actual contraction with modulus bounded away from one. The chain indices and the full source period make its quotient the actual compact Tate source, with the three-node closure in LS.7 at the one-end. A nonzero period either moves a positive-height cell or acts by this contracting source period on the lower unit chart. It therefore has no new fixed point in the quotient atlas. The finite physical-circle stabilizers computed from the primitive chart weights are separate from these period identifications.

For an analytic compactness check, use the exact logarithmic period matrix E82.1 on the ordinary part, with its uniform strict gap E82.3. Its inverse sends the two logarithmic norms to the actual real period coefficients. Taking both coefficients in a closed unit interval gives a fundamental norm cut. The angular variables are compact. The full units in all native face maps have bounded logarithms on their respective closed small base charts. The strict gap and E109.1 bound the resulting finite shifts in the norm cuts; at a lower rank-one face the remaining bound is the explicit source contraction just described. In the regular monomial charts these cuts lie in finitely many closed coordinate polydiscs, with their recorded finite face identifications. Their closure is therefore compact. The nonzero-period translates of an ordinary compact chart are locally finite by E82.1; the same statement in a lower chart follows from the retained contraction or chain-index shift. These two checks prove Hausdorff proper gluing at the cut. The base blowup is proper, and the native subdivisions do not add another boundary face.

Cut this completed collision fourfold over the actual closed source disc \(U\) and scalar disc \(|s|\leq\epsilon\), rounding corners equivariantly. Call the result \(W_c\). Its protected side boundary is E104, and its outer parameter boundary is the actual coupled family. Let \(W_r\) be the fixed-source scalar chain with the same \(s^4\lambda_0\), four consecutive node labels and actual point line \(M_6\). Glue \(W_c\) to \(-W_r\) using E105's completed side flow, prescribed in the point frame by E106. This gives the compact oriented relative eight-manifold \(W_{\rm rel}\), with its physical circle. Its fixed set consists exactly of the 276 compact curves, 117 compact surfaces, two separate ten-point blocks, and four lower/reference doubles already calculated. The minimal-face/period extraction covers every regular chart and every paired facet, so no further fixed component is omitted.

The exterior extension of the boundary flow retains the actual finite cap word. On the root cap it is the same scalar factor \(r_0s^2\) multiplying the full map \((-1)^dF_2(\sigma)D\); its square is the same \(s^4\lambda_0 B_0(\sigma)\). The source/line maps of E70--71 extend on the entire source-parameter disc. The ordinary/root overlap is the full reference-cochain map E77, and its source dependence extends on that disc. In the \(V_C\) chart its actual input is \(F_{\rm pt}\circ H\), not \(F_{\rm pt}\) applied to an untyped coefficient. The two forward parameter arrows remain \(q^2,h^2\), and the inverse closings remain \(q^{-2},h^{-2}\). They satisfy E87.8 on both sides of the comparison, including every restored integer sector deck and the fixed finite character.

On the selected I1 collar, the source node remains nondegenerate throughout the source-parameter disc. The actual selected period unit, the point-line coefficient and the normalized Hom coefficient \(B_{\rm sel}/q\) extend and are nonzero there. At the central source parameter the last coefficient is \(4/t_{\rm selected}\), from E69 and the literal selected height; it is nonzero. The selected marked Picard coordinate is the analytic unit of E64. The point/O Cartier arrow remains a map of line modules when the two sections meet: its local generator \(w/(w-w_6(\sigma))\) is carried to the corresponding nonzero line frame. Thus the original point-line family, rather than the bare torus function H, supplies the selected normal coefficient.

Prescribe the exterior source flow to keep \(q=t-t_{\rm selected}(\sigma)\) fixed on this collar; its base component there is the derivative of the written selected-value function. On \(\partial U\) it keeps \(t\) fixed, and at the cap it keeps \(q_\infty\) fixed. These collars are disjoint. A relative partition of unity extends these prescribed base lifts, together with the actual source and point-line lifts, over the smooth compact exterior. Circle averaging and finite root averaging preserve the prescriptions and the full groupoid equations. This is the actual outside diffeomorphism used below.

The selected Cox charts are
\[
 q=Zc_0c_1=Z'c'_0c'_1,\qquad
 Z'=Z^{-1},\qquad c'_i=Zc_i,
 \tag{E109.2}
\]
with physical weights \((-1,+1,0)\). The node/source and Cartier maps above carry these equations and the height \(q\) literally. After the normalization coordinate of the compact fixed \(\mathbb P^1\) is fixed, each of the two signed normal lines has scalar automorphism depending only on the source parameter; its nonzero value and reciprocal extend through that parameter disc. Their product is prescribed by the retained height equation. The remaining opposite factors \((g,g^{-1})\) induce the physical Hopf arrow \(q_H\mapsto q_Hg/|g|\). The actual logarithm exists on the source disc; any common scalar-parameter winding is carried unchanged on both sides.

The parameter endpoint comparison makes that last statement literal. E87.9 at this collar has the same period reindex \(B^2\) on both sides and the full bounded maps
\[
 R_{2,\sigma}=(P_{{\rm sel},\sigma}^2Z,
                    \lambda^{-2}\beta_\sigma^{-2}V),\qquad
 R_{2,*}=(P_{{\rm sel},*}^2Z,
                    \lambda^{-2}\beta_*^{-2}V).
 \tag{E109.3}
\]
Their comparison has factors \(P_{{\rm sel},\sigma}^2/P_{{\rm sel},*}^2\) and \(\beta_*^2/\beta_\sigma^2\), with the complete source-coordinate change carried as above. These are extending source-disc units. The factor \(\lambda^{-2}\), with its actual winding, is identical in both expressions and is retained by the same reindex and closing square. It is not set equal to one in either family.

The induced fixed-sphere base map is a Möbius map with determinant nonzero on the entire source disc. Its ball extension is the actual positive-Hermitian formula \(P\mapsto APA^*/\operatorname{tr}(APA^*)\). Hold the transported Cox quaternion fixed in this product extension; apply the written physical phase on its Hopf line. Its inverse uses \(A^{-1}\) and the inverse phase. This gives the normal three-ball cap map of K42/K68 with the same physical line. It does not replace that product map by the derivative of the Möbius transformation. Consequently the two selected tube removals and their conifold caps match through the exterior flow, including their full normal frames, the anti-linear \(M=U^*\) map and the first-to-second clutch direction.

The orbit hypotheses are the actual ones of EC.25a--b in the proved E6 reference theorem. The full source/Cartier/cap interval to the F41 reference transports each present outer member to \(S^6\). The physical circle is free off the one selected fixed \(\mathbb P^1\), by the original fan weights and the strictly contracting primitive cap generator. The explicit Hopf boundary map and the primitive normal \(H_3\) map give the same orbit/conifold six-manifold and its physical Euler line as in K68. Choosing the horizontal connection to be product on the matched selected tube makes the actual return identity there; its physical Hopf lift uses the same complementary free bundle and the same tube identity. Thus K68's literal piece maps and inverse-clutch relation apply to this completed outer boundary. No separate normal twist is inserted.

Finally keep the two orientation reversals distinct. Write \(Y\) for the positive-parameter orbit five-manifold. The complex orientation of the original family is
\[
 \operatorname{or}(W)=d\phi_\delta\wedge\operatorname{or}(Y)
                       \wedge dr\wedge d\theta.
 \tag{E109.4}
\]
After the circle-first quotient, the outward outer boundary has orientation \(-\operatorname{or}(Y)\wedge d\theta\), because its radial normal crosses five directions. The inner fixed links have the physical orientation of E102. On the free part of \(W_{\rm rel}\), the line is the actual physical associated line \(M\), and the stable tangent splitting is E102.1. Match its connections through the actual derivative and line maps of the exterior flow; this uses transported connections, not an equality of two unrelated constant gauges. Finite-chart Stokes, with multiplicity \(1/d\) on a stabilizer chart, therefore gives
\[
 \operatorname{Pair}_{M,+}(c)-\operatorname{Pair}_{M,+}(r)
       =\operatorname{Pair}_{M,\rm inner}=(27,12).
 \tag{E109.5}
\]
The parameter reversal is the following literal map, with the same full lifted return \(f\) on both sides:
\[
 Q_f^+=(Y\times[0,1])/((y,1)\sim(f(y),0))
 \longrightarrow
 M_f=(Y\times[0,1])/((y,0)\sim(f(y),1)),
 \qquad [y,t]\longmapsto[y,1-t].
 \tag{E109.5a}
\]
The physical-line map is \([v,t]\mapsto[v,1-t]\). At either endpoint its two identifications agree because the same full lift of \(f\) is used: the source relation \((v,1)\sim(\widetilde f(v),0)\) is sent to the target relation \((v,0)\sim(\widetilde f(v),1)\). Its inverse is the identical formula. This reverses the parameter orientation and preserves the physical line without an additional gauge. Consequently
\[
 \operatorname{Pair}_{M,\rm Jin}(c)-\operatorname{Pair}_{M,\rm Jin}(r)
                              =(-27,-12).
 \tag{E109.6}
\]
For the characteristic-pair composition, use the actual family over the E87 parameter torus. Its endpoint-fixed path square compares the diagonal path \((1,2)\) to the source path followed by the two scalar-root paths. The usual interval-concatenation pair of pants is obtained by thickening those two successive intervals and rounding their common corner. Pull back the actual family, its physical line and the selected tube along that map. Equations E87.8--10 and E109.3 give the same full lifted maps on the four parameter edges and their corner. The selected Hopf product extends across this pair of pants by the ball map just specified. It therefore gives an oriented seven-dimensional bordism of the completed six-manifolds with their actual physical lines. Closedness of \(x^3\) and \(p_1x\) makes the pair additive as integers on that bordism; no division or equality only in \(\Theta_7\) is used.

The actual E87 parameter-torus square identifies this relative boundary with the fixed-scalar source loop \((1,0)\). Thus the computed physical pair of that loop on the retained initial selected fan is \((-27,-12)\), and its K68 index is
\[
                   \frac{4(-27)-(-12)}{24}=-4.
 \tag{E109.7}
\]
This is obtained from the entire relative boundary and its full line/cap/parameter arrows. The earlier isolated charge-three value and the formal half-integer subtotal played no role in selecting it. No other-fan value or unproved native free coordinate is assigned by this calculation.
