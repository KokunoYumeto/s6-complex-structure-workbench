# K39 working: the v=0 marked source, Cartier line and completed-family transport

The source coordinates are those of SM.7:
\[
 Y^2=X^3+(1-2v)X^2+TX+v^2,\qquad G=(0,v),\qquad
 T_0=v^2-2v,\qquad q=T-T_0.
\]
This note retains the original normalized E7 source
\(y^2=x^3+3rx^2+tx+1\), its actual line and its chord-normalized
linearization. No completed-family return is assigned yet.

## 1. Literal simultaneous resolution selected by G

Set
\[
 A=Y-v,\quad B=Y+v,\quad C=X,\quad
 D=T+X^2+(1-2v)X.
\]
The equation is exactly \(AB=CD\), and the inverse is
\[
 X=C,\quad Y=(A+B)/2,\quad v=(B-A)/2,\quad
 T=D-C^2-(1-B+A)C.
\]
The two small resolutions are the two rank-one matrix factorizations.
The one retaining the marked section is
\[
 A=Dz,\qquad C=Bz.
\]
On its displayed affine chart,
\[
 v=(B-Dz)/2,\quad X=Bz,\quad Y=(Dz+B)/2,\quad
 T=D-B^2z^2-(1-B+Dz)Bz.
\]
The complementary chart is \(D=Aw,\ B=Cw\), with \(w=1/z\);
its parameter is \(v=(Cw-A)/2\). Each chart is smooth, and projection
to v is a submersion because its derivative in B, respectively A, is
\(1/2\), respectively \(-1/2\). The actual section is
\[
 G:\quad z=0,\quad B=2v,\quad D=T.
\]
It extends across the central node. In the other small resolution
\(A=Cz,\ D=Bz\), the same section has \(z=T/(2v)\); its closure
is the blowup of the base ideal \((T,v)\), not a section at the
origin. This is the actual marked morphism choosing the first resolution.

At \(v=0\), \(B=Dz\) and
\[
 T=D(1-z^2-Dz^4).
\]
Thus the central I2 consists of the exceptional component
\(C_1:D=0\) and the proper component
\(C_0:1-z^2-Dz^4=0\). The marked section meets C1 at z=0;
the zero section meets C0. Their intersections are z=+1 and z=-1.
The selected critical curve is
\[
 z=1,\qquad B=v,\qquad D=-v,
\]
which maps to \(X=v,Y=0,T=T_0\). Hence it extends to the z=+1
intersection. The other node of the central I2 is the z=-1 intersection.

## 2. The actual 2G Cartier specialization

The exact doubling formula is
\[
 X(2G)=\frac{T^2}{4v^2}-(1-2v),\qquad
 Y(2G)=-v-\frac{T}{2v}X(2G).
\]
Consequently its lift has \(z=-2v/T\). In the small-resolution chart,
the equation \(zT+2v=0\) factors as
\[
 zT+2v
   =B\bigl(1-Bz^3-(1-2v)z^2\bigr).
\]
The B=0 factor is the extraneous -G section, introduced when the
formula \(z=X/(Y+v)\) is cleared of denominators. The actual 2G
closure has the Cartier equation
\[
                  1-Bz^3-(1-2v)z^2=0.
\]
It restricts at v=0 to \(1-z^2-Dz^4=0\), with multiplicity one,
and it does not contain C1. It misses G because at z=0 its defining
function is 1. Away from T=0, the displayed doubling formula tends
to O. Therefore the relative divisor \(2G-O\) specializes to C0
on this local source.

This also gives the global specialization on the compact minimal
source. The III* component degrees of \(2G-O\) are zero on every
nearby source and remain zero on its unchanged simultaneous root
charts. Any extra vertical divisor there is an integral whole
fibre, by the component intersection kernel. At the other finite
fibres the section tends to O and no component is added. Finally
\((2G-O)\cdot O=1=C_0\cdot O\), so the possible additional whole
fibre coefficient is zero. Thus the actual line for (a,b)=(2,1)
has limit \(O(C_0)\). Its class is retained even though the generic
Picard point 2G tends to zero.

For (a,b)=(1,2), G itself extends as the marked section above, so
the actual central line is \(O(G_0-O)\); it has component degrees
(-1,+1) on (C0,C1), and its generic point is nonzero two-torsion.

## 3. Exact global Hom sections and their source-parameter winding

In the original normalized coordinates, put
\[
 f_{21}=\frac{y+1+(t/2)x}{x},\qquad
 f_{12}=\frac{y-1-(t/2)x}{x}.
\]
For (a,b)=(2,1), the numerator is the tangent line at -G;
for (a,b)=(1,2), it is the tangent line at +G. The denominator
is the vertical chord through G and -G. Their horizontal divisors
are exactly
\[
 D_{21}=(2G)-O-G+(-G),\qquad
 D_{12}=G-O-(-G)+(-2G).
\]
These are the actual lines of target-point linearizations for the
forward suspension by -bG. At III* the component contributions
cancel, because G and -G have the same nonidentity component and
2G,-2G,O have the identity component. At finite fibres the displayed
functions have no whole-fibre zero or pole. Their vertical divisor
is therefore a multiple of the infinity fibre. Intersecting with O,
using the explicit polynomial coordinates of 2G, gives
\[
                \operatorname{div}(f_{ab})=D_{ab}-F_\infty.
\]
Hence in the canonical meromorphic divisor frame the actual
linearization with selected simple whole zero is
\[
                       \phi_{ab}=\frac{t-t_0}{f_{ab}}.
\]
This fixes a concrete normalization of its scalar parameter.

Under \(X=u^2x,Y=u^3y,T=u^4t,v=u^3\), define
\[
 F_{21}=\frac{Y+v+(T/(2v))X}{X},\qquad
 F_{12}=\frac{Y-v-(T/(2v))X}{X}.
\]
Literal substitution gives \(f_{ab}=u^{-1}F_{ab}\). Consequently
\[
                      \phi_{ab}=\frac{q}{vF_{ab}}.              \tag{SZ.1}
\]
This is invariant under the marked mu3 coordinate quotient because v
is invariant. At the selected node \(X=v,Y=0,T=T_0\),
\[
 F_{21}=v/2,\qquad F_{12}=-v/2.
\]
In the local canonical line frame the Hom factor divided by q is
therefore exactly \(+2/v^2\), respectively \(-2/v^2\). It winds
twice negatively on a positive source-v loop.

The actual selected nodal Tate point of G is SM.7's
\[
 P_G=\frac{1+\sqrt{1+v}}{1-\sqrt{1+v}},\qquad vP_G\longrightarrow-4.
\]
The Tate base factor satisfies
\[
 q_T/q=-\frac{v}{64(1+v)^3}+O(q).
\]
Thus the three recorded source-parameter windings are respectively
qT/q:+1, PG:-1, and Hom/q:-2. In a sufficiently small selected collar,
the theta ratio identifying the actual Cartier line has a nonzero
limit 1 at the chosen nodal branch, so it does not change the latter
Hom-unit winding. This last branch comparison must also be retained
on the other node branch when the completion is glued.

## 4. Exact logarithmic winding matrix and the remaining completion map

Order the local torus coordinates by (source Tate, line Tate), and the
two q-periods by (source, suspension). The linear part of the positive
source-loop unit winding is
\[
 W_{ab}=\begin{pmatrix}1&b\\-a&-2\end{pmatrix}
       =\binom1{-a}(1\ \ b),\qquad ab=2.
\]
It has rank one. The literal integral basis
\[
 P=\begin{pmatrix}1&-b\\-a&1\end{pmatrix},\qquad\det P=-1
\]
diagonalizes it: \(P^{-1}W_{ab}P=\operatorname{diag}(-1,0)\).
The physical delta cocharacter becomes \(P^{-1}(0,1)^t=(-b,-1)^t\);
it must not be replaced by a new unit vertical character.

This is an exact statement about the recorded logarithmic winding,
not yet an isomorphism to a globally split product of Tate curves.
The required remaining map is the relative completion over the
source-v loop, with all bounded q/v units, the selected-node Cartier
frame, the physical delta character and every finite-cap norm retained.
The tentative diagonal parameters q/v and q must be justified by that
actual map before their degeneration can be used to compute the return.
The source resolution alone does not supply it: the generic suspension
translations acquire nontrivial behaviour on the central components,
and their source-Picard limits do not identify the relative line maps.

The exact algebraic identities in Sections1--3, and the winding-matrix
factorization, pass in code/part3_fourfold/source_zero_resolution.py,
with its JSON and captured outputs. No value of the completed-family
source-loop return is encoded in that certificate.

## 5. Normalization blowup and the retained Cartier line

The normalization of the selected nodal fibre has the exact map
\[
 X=s^2-1,\qquad Y=s(s^2-1-v),\qquad T=v^2-2v.
\]
Its lift into the marked small resolution is
\[
                    z=\frac{s+1}{s^2+s-v}.                    \tag{SZ.2}
\]
The unique indeterminacy is \((s,v)=(-1,0)\). Blow up this point of
\(P^1_s\times D_v\). On the chart \(s=r-1,\ v=rt\), the lift is
\[
                         z=(r-1-t)^{-1}.                     \tag{SZ.3}
\]
Thus the exceptional divisor \(E:r=0\) maps to \(C_1\), while the strict
central fibre \(t=0\) maps to \(C_0\). The complementary blowup chart
extends the marked point \(G:s=-1\) to \(z=0\) on \(E\). This is the
literal source normalization lift; no choice of an abstract blowup
identification is used.

Put \(c=\sqrt{1+v}\), using the single-valued unit branch with \(c(0)=1\),
and let \(D_\pm\) be the strict transforms of \(s=\pm c\). Only \(D_-\)
passes through the centre. The exceptional valuation of \(s+c\) is one
and that of \(s-c\) is zero. Consequently
\[
 \operatorname{div}\frac{s-c}{s+c}=D_+-D_--E,\qquad
                         O(D_+-D_-)=O(E).                   \tag{SZ.4}
\]
For example, on the displayed chart
\(s+c=r(1+t/2)+O(r^2)\), whereas \(s-c=-2+O(r)\).
At the intersection of \(D_-\) with \(E\), \(t=-2\), and (SZ.3)
gives the selected node \(z=1\).

The actual source line restricts to
\[
                           M_S=O(-aE),\qquad a=1,2.          \tag{SZ.5}
\]
For \(a=1\), the divisor of the marked section \(G\) is its strict
transform through the blowup centre, while \(O\) misses that centre;
their difference has class \(-E\). For \(a=2\), the generic normalized
point \(2G\) alone does not compute the Cartier restriction. Section 2
shows that its actual closure adds \(C_0\). On the blown-up
normalization \(C_0\) is the strict central fibre, with class \(-E\);
the strict marked-section part contributes the other \(-E\).
Equivalently the restriction has degree \(+2\) on \(E=C_1\), whereas
both sides have degree zero on every generic normalization fibre.
The Picard group of the blowup over the contractible disc is generated
by the generic-fibre degree and \(E\). These two degrees determine the
displayed line, including its sign.

There is also an exact local line map at the two branches. In the
unimodular Cox charts a change of source line frame \(V\mapsto gV\)
acts on the two complex normal coordinates by
\[
                       (c_0,c_1)\longmapsto(g^{-1}c_0,gc_1).
\]
After the prescribed conjugation of the negative-weight coordinate,
the unitary part of \(g\) multiplies both spinor coordinates. The
positive real part contracts through positive diagonal maps and does
not change that clutch. Thus the spinor bundle on this source
normalization model is literally
\[
 \bigl(O(D_+)\oplus O(-D_-)\bigr)\otimes M_S,\qquad
             c_1(\det)=(1-2a)E.                             \tag{SZ.6}
\]
Here the untwisted normal line is \(O(-D_+-D_-)\), obtained by taking
the cross product of the normalization derivatives in the
canonically trivialized ambient source determinant. The two branch
zeros are simple, as the transverse nodal equation directly shows.
Formula (SZ.6) records the actual Cartier-frame effect. It does not
assert that this local source model has already been embedded as the
fixed trace in a product orbit bordism.

The ordered branches in (SZ.6) are part of that formula's data.
Interchanging their roles gives instead
\[
 \bigl(O(D_-)\oplus O(-D_+)\bigr)\otimes M_S,\qquad
                         c_1(\det)=-(1+2a)E.                 \tag{SZ.6a}
\]
The single-valued choice of \(c=\sqrt{1+v}\) does not itself identify
either ordering with the physical gamma ordering in the completed
family. That identification remains part of the suspension comparison.

## 6. The exact primitive suspension square

Let \(U\) denote the rational target-point lift of translation by
\(-G\) on \(O(G-O)\):
\[
                 (p,w)\longmapsto
                 \left(p-G,\frac{w}{X(p-G)}\right).          \tag{SZ.7}
\]
The divisor identity making this a line map is
\[
 (G)-O-t_G^*((G)-O)=(G)+(-G)-2O=\operatorname{div}X
\]
on each ordinary elliptic fibre. The displayed factor is evaluated
at the target point. This convention is the same convention as the
actual coefficient \(\phi=q/(vF_{12})\) in Section 3.

For a point \(r=(X,Y)\) on the source curve, the addition formula gives
\[
 X(r+G)=\left(\frac{Y-v}{X}\right)^2-(1-2v)-X,
\]
and the source equation then gives the exact identity
\[
                         X(r+G)X(r)=-2vF_{12}(r).            \tag{SZ.8}
\]
Therefore the suspension in the \((a,b)=(1,2)\) family is
\[
                    B_\lambda=-2\lambda q\,U^2.             \tag{SZ.9}
\]
This is an equality of actual rational line maps, not just of their
generic Picard points. It retains the scalar and the selected
whole-fibre factor.

The local nonzero line above the exceptional source component also
has a literal Cox presentation. Write
\[
 D=s_0t_0,\quad A=s_1t_0,\quad B=s_0t_1,\quad C=s_1t_1,
\]
where the auxiliary action has weights \((1,1,-1,-1)\). Since
\(O(G-O)|_{C_1}=O(1)\), the nonzero line coordinate has auxiliary
weight \(+1\). Fixing it to one leaves the actual coordinates
\[
  (s_0,s_1,t_0,t_1),\qquad (s_0,s_1)\ne(0,0),\qquad
                   v=\frac{s_0t_1-s_1t_0}{2}.               \tag{SZ.10}
\]
The Hessian determinant of this quadratic is \(1/16\), so this map
is explicitly nondegenerate. The physical delta action is retained:
it has weights \((-1,-1,+1,+1)\) after this gauge choice. For the
degree-two line the same gauge has the residual \(\mu_2\) action;
it must not be discarded.

Equations (SZ.7)--(SZ.10) identify the component exchange whose graph
must be resolved. They do not yet identify the quotient of its
relative completion with the original compact family: \(U\) has
component poles, and its chosen source model changes by a flop at
the central curve. A generic translation logarithm across \(v=0\)
has therefore not been used.

## 7. Finite-root units and the remaining comparison

The source-parameter pole of the selected Hom coefficient is not a
pole of every cap coefficient. For the good III* root of the
\((a,b)=(1,2)\) case, put \(T=z^{-4},X=z^{-2}X',Y=z^{-3}Y'\).
Then literal substitution in (SZ.1) gives
\[
 \phi_{12}=
 \frac{1-(v^2-2v)z^4}
 {-1/2+vz^3Y'/X'-v^2z^6/X'}.
                                                               \tag{SZ.11}
\]
Its generic central-component value is \(-2\), with no winding in
\(v\). For a reduced III root \(m=4p-1\) in the \((a,b)=(2,1)\)
case, the analogous substitution gives
\[
 \phi_{21}=
 \frac{1-(v^2-2v)z^m}
 {1/2+vz^{m-p}Y'/X'+v^2z^{m+2p}/X'}.
                                                               \tag{SZ.12}
\]
The generic central-component value is \(+2\). The certificate checks
the good root and the basic reduced root literally. Extension through
all resolved root components still belongs to the required completed
family comparison; the generic values alone do not supply it.

The present exact remaining map is the relative graph completion of
the suspension (SZ.9), or its degree-two-line counterpart, through
the central flop, with the chosen finite-root line maps and physical
delta kept. Rescaling \(\lambda=v^2\lambda_0\) cancels the selected
Hom-unit pole, but changes the actual scalar loop by two turns.
The scalar-loop contribution and every cap gluing must consequently
be retained in any argument using that rescaling. No numerical
source-loop return follows merely from the signature of the blown-up
normalization or from (SZ.6).

All displayed algebraic identities in Sections 5--7 are checked in
code/part3_fourfold/source_zero_trace.py, with JSON and captured
outputs. Its status explicitly stops at the source, Cartier and
suspension identities.

## 8. The local origin link, with its actual circle charge

The nonzero degree-\(a\) line gauge in (SZ.10) has the residual scalar
group \(\mu_a\). Its origin link is \(S^7/\mu_a\); after conjugating
the two negative delta weight coordinates, the orbit map is literally
the positive Hopf projection
\[
                  S^7/\mu_a\longrightarrow \mathbb{CP}^3.
\]
Its principal-circle Euler class is \(a h\): the original unit Hopf
transition function is raised to the \(a\)-th power by the quotient of
its fibre by \(\mu_a\). In particular the degree-two line has charge
two, not one. With \(h\) positive and \(\int h^3=1\), the oriented
characteristic value of this actual link is
\[
 \frac{4(ah)^3-p_1(T\mathbb{CP}^3)(ah)}{24}
                    =\frac{a(a^2-1)}6.                     \tag{SZ.13}
\]
Here \(p_1(T\mathbb{CP}^3)=4h^2\) follows directly from the Euler
sequence. These values are zero for \(a=1\), and one for \(a=2\).

For comparison, the sphere-bundle expression belonging to the ordered
local determinant in (SZ.6), on the blowup whose intersection form is
\(E^2=-1\), is \(-a(a-1)/2\). The reversed order (SZ.6a) instead gives
\(-a(a+1)/2\). These are computations on the specified local bundles.
No global equality between their sum and the actual source return is
asserted: the relative graph quotient must determine which ordered
trace occurs, how many origin-link boundary components occur, and
their boundary orientations.

The remaining geometry is now localized more precisely. Translation
by \(-G\) contracts the central component \(C_0\) in the marked total
source and replaces it by the other small-resolution curve. The
Cartier multiplier in (SZ.7) must be carried through that graph.
The successive source models for \(U^b\) form the actual component
flop chain; only its quotient by the suspension gives a candidate
compact orbit bordism. A construction using the two moment chambers
of (SZ.10) must exhibit the same overlap map as (SZ.7), retain the
bounded line units and the finite-cap characters, and identify the
physical gamma ordering. This is the precise uncompleted map.

## 9. The actual Cartier overlap of the two source flop chambers

The chamber overlap in the preceding paragraph can be made literal.
Write \(p'=p-G\), and let \(F_2=1-Bz^3-(1-2v)z^2\) be the actual
Cartier equation from Section 2. The addition formula gives
\[
 X'=\frac{F_2}{z^2},\qquad Y'=v-\frac{X'}z.
\]
Set \(A'=Y'-v,\ B'=Y'+v,\ C'=X'\), and
\(D'=T+X'^2+(1-2v)X'\). Direct substitution gives
\[
                   A'=-C'/z,\qquad D'=-B'/z.                \tag{SZ.14}
\]
These are exactly the equations of the other small resolution of
\(A'B'=C'D'\). In particular the map contracts the proper component
\(C_0\), where \(F_2=0\), and the ratio of the other ruling is
\(-1/z\). The marked target small resolution uses the first ruling.
This identifies the graph of translation by \(-G\) with the actual
Atiyah flop in these coordinates.

Use its common Cox coordinates
\[
 A'=s_0t_0,\quad B'=s_1t_1,\quad C'=s_0t_1,\quad D'=s_1t_0,
\]
with auxiliary weights \(+1\) on the \(s_i\) and \(-1\) on the
\(t_i\). The target ruling has coordinate \(s_0/s_1\), and its marked
section \(G\) has \(s_0=0\). The domain ruling has coordinate
\(t_0/t_1=-1/z\), and its zero section \(O\) has \(t_1=0\).
Let \(V\) have auxiliary weight \(+1\). On the target chart the
canonical meromorphic coefficient of the line \(O(G-O)\) is
\[
                             w_{\rm target}=V/s_0;
\]
on the domain chart it is
\[
                             w_{\rm source}=Vt_1.
\]
For clarity, on \(s_1=1\) the regular line frame is the divisor
frame \(1/(s_0/s_1)\), whereas on \(t_0=1\) it is the divisor
frame \(t_1/t_0\). These two displayed coefficients are exactly
their expressions in the canonical meromorphic frame. Hence
\[
                 \frac{w_{\rm target}}{w_{\rm source}}
                       =\frac1{s_0t_1}=\frac1{X'},           \tag{SZ.15}
\]
which is the actual multiplier in (SZ.7). Thus the source line map
through the flop is the identity in the common Cox coordinate \(V\),
not merely an abstract equality of line degrees. Fixing the nonzero
\(V\) gives the two moment chambers of the same \(C^4\) model.
For the \(a\)-th tensor power it gives the same two chambers of
\(C^4/\mu_a\), retaining the physical delta action already recorded.

The actual degree-two line has a compatible explicit Cartier map
to the square of the degree-one line. Namely
\[
 r(p)=X(p-G)=\frac{2vF_{21}(p)}{X(p)}
              =\frac{F_2}{z^2}.                            \tag{SZ.16}
\]
Its divisor is the difference between the actual \(2G-O\) divisor
and twice \(G-O\), on this collision neighbourhood. Multiplication
by \(r\) is consequently the line isomorphism
\(O(2G-O)\longrightarrow O(G-O)^{\otimes2}\). The expression
\(F_2/z^2\) retains the central component and has no extra factor of
\(v\). At a target point \(p'=p-G\),
\[
 F_{21}(p')=\frac{r(p')r(p)}{2v}.
\]
Transporting the actual suspension through (SZ.16) therefore gives
\[
 \frac{r(p')}{r(p)}\frac{\lambda q}{vF_{21}(p')}
                         =\frac{2\lambda q}{X(p')^2}.       \tag{SZ.17}
\]

Let \(U_a\) denote the tensor-power version of (SZ.7), with target
multiplier \(X(p-G)^{-a}\). Both allowed source/line sectors now have
the exact common form
\[
           B_{a,b}=2(-1)^{b+1}\lambda q\,U_a^b,
                       \qquad ab=2.                        \tag{SZ.18}
\]
The source Cox chamber overlap for every factor \(U_a\) is (SZ.15).
The only remaining comparison is consequently the periodic quotient
of these chambers with the exact scalar and selected \(q\)-factor
in (SZ.18), including its Mumford boundary and finite-root caps.
Its boundary must be matched with the original completed family
before the local link numbers of Section 8 can be summed.

In these same target Cox coordinates the two base functions are
explicit:
\[
 v=\frac{s_1t_1-s_0t_0}{2},\qquad
 q=(s_1-s_0)(t_0+t_1)-(s_0t_1-v)^2.                         \tag{SZ.19}
\]
Both are invariant under the physical delta action. In particular
the \(q\)-factor in (SZ.18) is the actual invariant polynomial
(SZ.19); a product construction replacing it by an independent
disc coordinate would omit its singular central divisor.
The certificate checks this identity as well as the two chamber
line frames. This retained equation is the local input for the
periodic Mumford-boundary comparison.

## 10. Exact two-node base coordinates

There is a direct analytic coordinate map to the two-node conifold,
without dropping any parameter unit. Put \(A_0=1-2v\) and
\[
 \xi(T,v)=\frac{-A_0+\sqrt{A_0^2-3T}}3 ,
\]
where the square root is the unit branch equal to one at the origin.
It satisfies \(3\xi^2+2A_0\xi+T=0\). For \(x=X-\xi\), define
\[
 R=x\sqrt{A_0+3\xi+x},\qquad
 h(T,v)=v^2-A_0\xi^2-2\xi^3 .
\]
Both square roots are actual holomorphic units on a sufficiently
small polydisc. The source equation becomes exactly
\[
                         (Y-R)(Y+R)=h(T,v).                \tag{SZ.20}
\]
The two local critical-value curves are
\[
 T_0=v^2-2v,\qquad
 T_1=\frac{1+4v-(1-8v)^{3/2}}8 .
\]
The latter is the small root of the remaining discriminant factor.
Their tangent slopes are \(-2\) and \(+2\); hence
\[
                 q_1=T-T_0(v),\qquad q_2=T-T_1(v)
\]
are actual analytic coordinates on the base near the origin.
The function \(h\) vanishes simply along both curves away from their
intersection. The explicit formula shows its quadratic term is
\(-\tfrac14(T^2-4v^2)\). Analytic division therefore gives
\[
                       h=\upsilon(q_1,q_2)q_1q_2,
                         \qquad\upsilon(0,0)=-1/4,          \tag{SZ.21}
\]
with \(\upsilon\) holomorphic and nowhere zero after shrinking.
Replacing \(Y-R\) by \((Y-R)/\upsilon\) in (SZ.20) gives the literal
equation \(AB=q_1q_2\). This is an explicit local isomorphism, including
the selected \(q_1\) direction, the other \(q_2\) direction and the
unit \(\upsilon\). The unit has a holomorphic logarithm on the
polydisc, so its restriction to a source-parameter loop has zero
winding.

This supplies the two-node base chart for the chamber quotient in
Section 9. The global periodic quotient is still not replaced by the
affine conifold: its actual \(q_1\) period and the physical delta
character remain the data in (SZ.18).

## 11. Effective scaling and the residual period at the omitted origins

For the actual degree-\(a\) line, the common Cox coordinate \(V\) has
auxiliary weight \(a\). Multiplication \(V\mapsto dV\), where
\(d=2(-1)^{b+1}\lambda q_1\), is represented after fixing \(V=1\) by
\[
 (s_0,s_1,t_0,t_1)\longmapsto
 (d^{-1/a}s_0,d^{-1/a}s_1,d^{1/a}t_0,d^{1/a}t_1).             \tag{SZ.22}
\]
For \(a=2\) the square-root ambiguity is exactly the retained
\(\mu_2\) quotient, so the effective map is single-valued. Its
associated principal-circle line still has charge two. Replacing
this map by the \(a=1\) scaling would change that line.

The component labels alone do not determine the quotient links.
The source two-node chain has source-period displacement two, while
the primitive translation has displacement one. The candidate finite
label set is consequently
\(\mathbb Z/(2\mathbb Z+b\mathbb Z)\), of size \(b\) for \(b=1,2\).
However a combination with zero label displacement remains. Its
actual line action must be retained before these labels can be
regarded as separate ordinary origin-link boundary components.

This residual action can already be seen directly at \(v=0\), away
from \(T=0\). The two-torsion addition formula gives
\[
                  X(p+G_0)X(p)=T,\qquad U_1^2=T^{-1}.
\]
Since \(q_1=T\) there, the actual suspension restricts to
\[
 B_{1,2}=-2\lambda,\qquad B_{2,1}^2=4\lambda^2.              \tag{SZ.23}
\]
These are actual nontrivial constant line scalings for a contracting
choice of scalar. Thus the zero-displacement period has an infinite
stabilizer at the omitted Cox origin. The punctured chamber quotient
and its Mumford stable locus must be analyzed with this scaling;
counting component labels does not identify its compact boundary.
This is an additional explicit part of the remaining comparison,
not a proof that the desired real bordism cannot be constructed.

The infinity dictionary supplied by root preserves the same actual
period, rather than merely its Picard point. With
\(v=\zeta^{-2}\), \(X_{\rm old}=\zeta^{-2}X_\infty\), and
\(q_{\rm old}=\zeta^{-4}q_\infty\), the target-point formula gives
\[
 U_{a,\rm old}=\zeta^{2a}U_{a,\infty},\qquad
 q_{\rm old}U_{a,\rm old}^{\,b}
       =q_\infty U_{a,\infty}^{\,b}\quad(ab=2).               \tag{SZ.24}
\]
For \(a=2\), the Cartier multiplier satisfies
\(r_{\rm old}=\zeta^{-2}r_\infty\); its source and target factors
cancel in the conjugation (SZ.17). Thus the original scalar
\(\lambda\) is retained in the unified formula at infinity.
This check is independent of any eventual periodic-quotient index.

## 12. The stable-locus end of the residual contraction

The nontrivial residual scaling has an exact real cross-section
before any source-flop boundary identification is imposed. On the
locus \(s\ne0,\ t\ne0\), put
\[
 R=|s||t|,\qquad L=\log(|t|/|s|).
\]
For the effective degree-\(a\) scaling (SZ.22), \(R\) is fixed and
\[
                         L\longmapsto
                         L+\frac2a\log|d|.
\]
Its unitary phase is the physical delta action and disappears in
the orbit quotient. Thus at \(R=\epsilon\) the orbit cross-section
before the residual period is
\[
 K\times\mathbb R_L,\qquad
       K=(S^3_s\times S^3_t)/S^1_\delta\cong S^2\times S^3.
\]
For a constant residual \(d\), its quotient is literally
\(K\times S^1_L\). The Euler line is the charge-\(a\) line retained
by the nonzero-line gauge. This provides the actual stable-locus
alternative to treating an origin with infinite stabilizer as an
ordinary isolated quotient point.

There are two comparisons still to do. First this cross-section
must be embedded as an end of the full periodic quotient with its
selected \(q_1=0\) boundary. Second the successive source-flop
chambers must be identified on \(K\) in their actual common normal
framing. The literal boundary flop from P3K.23 is
\(\tau(h,q)=(q^{-1}hq,q)\); using it here requires computing the
arrow from the Cox frames in (SZ.15), not importing a flop count.
The scalar stage just computed has identity monodromy on \(K\).
Any nontrivial mapping torus must come from that additional chamber
identification. No characteristic value of the global return is
inferred from this cross-section.

For a single common Cox chamber, the ruling arrow is explicit.
Use the same quaternion representatives as P3K.23: \(u\) represents
the \(s\)-ruling, \(c\) the conjugated \(t\)-normal coordinate, and
\(q=uc\). Then
\[
 h=uiu^{-1},\qquad k=c^{-1}ic=q^{-1}hq.
\]
The identity of the common Cox coordinates therefore sends the
first-ruling product to the second-ruling product by \(\tau\).
The actual \(U\) in (SZ.15) goes from the domain \(t\)-ruling to the
target \(s\)-ruling, so its single-chamber arrow is the inverse one.
This local arrow does not yet give a power of \(\tau\) around the
periodic quotient: the cyclic reset between successive marked
source models and the source-period identification must still be
included. In particular no bare count of chamber crossings is
substituted for that composite.
