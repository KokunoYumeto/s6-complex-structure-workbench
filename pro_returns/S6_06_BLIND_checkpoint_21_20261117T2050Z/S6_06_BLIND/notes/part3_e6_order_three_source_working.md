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
Its divisor is \(3(G)-(3G)-2(O)\). Thus this is a typed Cartier
comparison, including its base divisor; its inverse has the opposite
bundle direction.

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
