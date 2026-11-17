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

**Physical-line convention correction (17 November, after P3K.68).**
The positively oriented Hopf line denoted by \(a h\) in (SZ.13) is
the meridian-positive dual \(U=M^{-1}\). The actual nonzero-vector
line has \(c_1(M)=-a h\), so its characteristic value on this same
oriented local quotient is \(-a(a^2-1)/6\). This corrects the label
of the local model calculation below; it does not determine the
orientation with which that model occurs in a global boundary. Both
the finite residual \(\mu_a\) and the retained ruling arrow remain.


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

## 13. The two Cox frame systems at their exceptional curves

The node-adapted and Cartier-adapted Cox frames can be compared
without identifying them implicitly. At the linear level of the
conifold, the actual analytic map in Section 10 has
\[
 \begin{aligned}
 \alpha&=(A'+B'-C'-D')/2,&
 \beta&=-2(A'+B'+C'+D'),\\
 q_1&=-A'+B'-C'+D',&
 q_2&= A'-B'-C'+D'.
 \end{aligned}                                             \tag{SZ.25}
\]
Substitute the common Cartier matrix
\(\left(\begin{smallmatrix}A'&C'\\D'&B'\end{smallmatrix}\right)
 =(s_0,s_1)^t(t_0,t_1)\). The literal factorization is
\[
 \begin{aligned}
 S_0&=s_1-s_0,&S_1&=s_0+s_1,\\
 T_0&=t_0+t_1,&T_1&=t_0-t_1,
 \end{aligned}
\qquad
 \begin{aligned}
 q_1&=S_0T_0,&q_2&=S_1T_1,\\
 \alpha&=-S_0T_1/2,&\beta&=-2S_1T_0 .
 \end{aligned}                                             \tag{SZ.26}
\]
Both constant two-by-two changes are invertible and preserve the
auxiliary weights. The Cartier marked point is retained by
\[
                            s_0=(S_1-S_0)/2.                \tag{SZ.27}
\]
It is an interior point of the exceptional component, not one of
the node-adapted coordinate axes. Thus using \(q_1=S_0T_0\) does
not replace the actual marked divisor by \(S_0=0\).

These formulas are the restriction of the analytic map of Section
10 to the exceptional curve, because terms of order at least two
in the conifold coordinates have higher normal order after the
small resolution. The analytic map lifts to the corresponding
small resolution by the displayed ruling; the degree-\(a\) line
pulls back to the same degree-\(a\) line on its exceptional \(P^1\).
The comparison of their local line frames is a nowhere-zero
holomorphic unit after the full analytic image of the Cartier
divisor is retained. Formula (SZ.27) specifies its restriction to
the exceptional curve; its higher normal terms are carried by the
actual analytic map of Section 10 and are not set to zero.
One way to verify this last statement directly is to use the two
standard \(P^1\) charts and expand the ratio in the two normal
coordinates. Its degree-zero restriction to \(P^1\) is constant;
the higher overlap terms have coefficients in \(O(n)\), \(n\ge1\),
whose Laurent overlap is an additive coboundary. The convergent
holomorphic overlap solves on a sufficiently small tubular
neighbourhood by splitting the positive and negative Laurent
parts. Exponentiating gives the unit comparison.

Such a unit is constant on the exceptional \(P^1\) and descends
through the proper small resolution to the normal conifold germ.
After dividing its constant value it has a holomorphic logarithm.
It therefore contributes no source-parameter winding. The exact
conjugation by these source and target units must nevertheless be
kept in the period map: consecutive factors telescope, and their
remaining endpoint ratio is part of the cyclic reset still under
study. This comparison supplies the line-frame arrow between the
two coordinate systems; it does not finish that reset.

## 14. The associated Tate-node chart with its line character

The selected Tate-node attachment must retain the line character;
the untwisted fibre product over the conifold would not do so.
In the node-adapted variables \(q_1=S_0T_0\), its actual associated
local chart is
\[
 UV=S_0T_0,\qquad
 (S_0,S_1,T_0,T_1,U,V)/\mathbb C^*,
\]
where the auxiliary weights and physical delta weights are
\[
 \begin{array}{c|rrrrrr}
       &S_0&S_1&T_0&T_1&U&V\\ \hline
 {\rm auxiliary}&1&1&-1&-1&a&-a\\
 {\rm physical\ delta}&0&0&0&0&1&-1 .
 \end{array}                                                \tag{SZ.28}
\]
The two node coordinates are associated respectively to the
degree-\(a\) line and its inverse; their product is exactly \(q_1\).
The constant scalar unit in (SZ.18) can be placed in one coordinate
by its chosen nonvanishing root, without changing the equation or
forgetting its period.

Resolve the displayed node in the chart
\[
                      U=S_0z,\qquad T_0=zV.
\]
The remaining coordinates are \(S_0,S_1,T_1,z,V\), with auxiliary
weights \((1,1,-1,a-1,-a)\) and physical weights
\((0,0,0,1,-1)\). In the \(V\ne0\) quotient chart, fixing \(V=1\)
requires the \(a\)-th root and leaves \(\mu_a\). Compensating the
physical action by the auxiliary parameter \(-\theta/a\) gives
the exact four normal weights
\[
                       (-1/a,-1/a,+1/a,+1/a).               \tag{SZ.29}
\]
Thus this chart recovers the charged \(C^4/\mu_a\) origin of
Sections 8 and 11, with the physical circle unchanged. On the
source-stable chart the locus \(z=V=0\) instead describes the
fixed surface with the source ruling retained.

This gives an explicit selected Tate-boundary chart in which both
the fixed-surface branch and the charged-origin chart can be
compared. Its appropriate stable open sets, the consecutive \(U_a\)
chambers and the periodic identification must still be assembled.
No assertion that all these charts already form a compact quotient
is made here. The certificate verifies every weight and the
effective quotient action in (SZ.29).

## 15. Which selected periodic fan the node resolution actually gives

The square diagonal in Section 14 can be read off from the actual
torus characters. On \(q_2\ne0\), choose \(S_1=1\), use the source
coordinate \(Z=S_0\), and retain the line coordinate \(U\).
In the chart \(U=S_0z,\ T_0=zV\),
\[
                   (Z,U,q_1)=(S_0,S_0z,S_0zV).
\]
The three rays, in the order \((Z,U,q_1)\), are
\[
                       (1,1,1),\quad(0,1,1),\quad(0,0,1).
\]
The complementary chart \(S_0=Uw,\ V=wT_0\) has the rays
\((1,1,1),(0,0,1),(1,0,1)\). Hence this resolution has the positive
square diagonal \(0\)--\(e_1+e_2\), with edge directions
\(e_2,e_1,e_1+e_2\). It is the \(j=-1\) vertical-edge fan of
P3K.25, rather than its default \(j=0\) fan.

The other small resolution is
\[
                U=T_0z,\ S_0=zV,
       \qquad\text{or}\qquad T_0=Uw,\ V=wS_0.               \tag{SZ.30}
\]
Its first chart has rays
\((0,1,1),(1,1,1),(1,0,1)\), and its second has
\((0,1,1),(1,0,1),(0,0,1)\). These are the default negative-diagonal
triangles with edge directions \(e_2,e_1,e_1-e_2\).
All four matrices are unimodular. This is an actual dense-torus
character computation, so the two source-loop fan choices are
explicitly distinguished by their morphisms.

The fixed-trace determinant for each of these two choices follows
from the same associated line chart. In the positive-diagonal chart
of Section 14, the fixed locus \(z=V=0\) is the \(O(-1)\) surface
with coordinates \((S_0,S_1,T_1)\) of weights \((1,1,-1)\).
Along its exceptional \(P^1\), the two normal degrees are
\(a-1\) and \(-a\), with physical weights \(+1,-1\).
Conjugating the latter gives determinant degree \(2a-1\), hence
the actual determinant class \((1-2a)E\).

For the default negative-diagonal fan use the second chart of
(SZ.30). Its coordinates \((U,S_0,S_1,T_1,w)\) have auxiliary
weights
\[
                       (a,1,1,-1,-a-1)
\]
and physical weights \((1,0,0,0,-1)\). The fixed surface \(U=w=0\)
is the same \(O(-1)\) source surface. The normal degrees are
\(a,-a-1\); after conjugating the negative-weight coordinate the
determinant degree is \(2a+1\). Its actual class is therefore
\[
                           -(2a+1)E.                       \tag{SZ.31}
\]
Thus the two ordered determinant formulas of Section 5 are now
attached to literal fan charts. The scalar-loop invariance proved
in P3K.25 does not supply a source-loop comparison: the latter
must retain the parameter-dependent source units and the periodic
boundary map under study here. No return value is assigned from
the determinant calculation.

## 16. The exact two-step normal-cone reset

The full source reset is already nontrivial on the normal cone of
\(C_1\). Retain the marked resolution coordinates
\((z,B,D)\), and scale \(B,D\) by a common positive parameter
\(\epsilon\). The first translation has limit
\[
              U:C_1\longrightarrow C_0,\qquad s=-1/z.
\]
The exact addition formulas, applied twice before taking the limit,
give the target curve coordinate
\[
 z_{\rm out}=
 -\frac{(z^2+1)B-2zD}{(z^2+1)D-2zB}.                       \tag{SZ.32}
\]
In particular it is not the bare normal ruling \(B/D\).
Let
\[
             w=\frac{z-1}{z+1},\qquad
             \eta=\frac{B+D}{B-D}.
\]
Then (SZ.32) says \(w_{\rm out}=w^2\eta\).
The first-order base functions are
\[
                      2v=B-Dz,\qquad T=D-Bz .
\]
They are preserved by the translation. Solving for the target
normal coordinates gives
\[
 B_{\rm out}=\frac{2v+Tz_{\rm out}}{1-z_{\rm out}^2},
 \qquad
 D_{\rm out}=\frac{T+2vz_{\rm out}}{1-z_{\rm out}^2}.
\]
Substitution yields the exact second coordinate
\(\eta_{\rm out}=w^{-1}\). Thus the normal-cone torus map is
\[
               (w,\eta)\longmapsto(w^2\eta,w^{-1}),\qquad
               \begin{pmatrix}2&1\\-1&0\end{pmatrix}.       \tag{SZ.33}
\]
The matrix is integral unimodular and its difference from the
identity has square zero. The product \(w\eta\), which is the
retained projective base direction up to its fixed sign, is
invariant.

The compactification data at both nodes are visible in this map.
The projective matrix in (SZ.32) has determinant
\(-(z^2-1)^2\). At \(z=1,B=D\), and at \(z=-1,B=-D\), its base
ideal is analytically \((h,u^2)\): write \(u=z-1,h=B-D\) in
the first chart, and use the corresponding signed variables in
the second. Each is a length-two ideal, retaining the two
successive elementary modifications. They cannot be suppressed
when comparing the actual boundary \(K\) with a product marking.

The exact two-step rational map and this normal-cone calculation
are saved in code/part3_fourfold/source_zero_translation_normal.py
and its JSON/output. The initial proposed bare-ruling formula
failed the symbolic check; its code and output are retained in
attempts/source_zero_normal_simple_guess. The successful
certificate keeps both coordinates in (SZ.33). It still leaves
the periodic real-normal clutch, the actual line multiplier and
the selected Tate-boundary attachment to be composed.

## 17. The line multiplier in the normal-cone reset

The projective reset of Section 16 also has an exact retained line
coefficient. In the \((a,b)=(1,2)\) sector use
\(B=-2\lambda q\,U_1^2\), and let \(V_{\rm reg}\) be the regular
\(O(1)\) fibre coordinate on the \(z\)-chart of \(C_1\). Its relation
to the canonical meromorphic line coefficient is
\(V_{\rm reg}=z\,w_{\rm Cartier}\). Define
\[
 \widehat V=(1-w)V_{\rm reg},\qquad
 p=w\eta,\qquad r=\frac{B-D}{1-w}.
\]
Here \(w=(z-1)/(z+1)\) is the curve coordinate from Section 16;
it is not the meromorphic line coefficient.
The exact translation multiplier is \(-2\lambda q/(X_1X_2)\).
Taking its normal-cone limit only after multiplying the target
and source regular-frame factors gives
\[
 (w,p,r,\widehat V)\longmapsto
                  (pw,p,r,-2\lambda p\,\widehat V).         \tag{SZ.34}
\]
The base functions are retained:
\[
                       2v=r(1-p),\qquad T=-r(1+p).         \tag{SZ.35}
\]
The certificate verifies (SZ.34) from the full rational translation,
not from the projective map alone.

The node-divisor frame change in \(\widehat V\) is explicit. On the
nonzero \(O(1)\) line, use the two vector coordinates
\[
                       A=1/\widehat V,\qquad C=w/\widehat V .
\]
The reset is literally
\[
       (A,C)\longmapsto
       \bigl((-2\lambda p)^{-1}A,\;(-2\lambda)^{-1}C\bigr). \tag{SZ.36}
\]
Thus on a compact annulus of \(p\)-values the inverse period is a
diagonal Hopf contraction for sufficiently small \(\lambda\).
This names the actual normal-cone end, including its two
multipliers. The nodes \(p=0,\infty\) and the global periodic
attachment are still the charts from Sections 14--16; they have
not been deleted by this diagonal description.

## 18. Rescaling the scalar with the source parameter

A direct fixed-\(\lambda\) central quotient retains the
zero-displacement period of Section 11. An alternative relative
comparison is to use the actual rescaling
\[
                          \lambda=v^N\lambda_0.
\]
On the two-node valuation ray, the source and suspension columns
then are
\[
                h=(2,-a)^t,\qquad g=(b,N-1)^t,\qquad ab=2.
                                                               \tag{SZ.37}
\]
The source Tate parameter has order two, the source-line multiplier
has order \(-a\), the translated point has order \(b\), and the
selected Hom coefficient has order \(-1\) before this scalar
rescaling. These are exactly the valuations retained in
Sections 3, 6 and 10. The determinant is \(2N\).

For \(a=1,b=2\), use
\[
 U_N=\begin{pmatrix}1&0\\-2&1\end{pmatrix}
     \begin{pmatrix}-1&0\\0&1\end{pmatrix}
     \begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
 V_N=\begin{pmatrix}1&N-1\\0&1\end{pmatrix}.
\]
For \(a=2,b=1\), use
\[
 U_N=\begin{pmatrix}1&0\\0&-1\end{pmatrix}
     \begin{pmatrix}1&0\\-(N-1)&1\end{pmatrix},\qquad
 V_N=\begin{pmatrix}0&1\\1&0\end{pmatrix}
     \begin{pmatrix}1&-2\\0&1\end{pmatrix}.
\]
All these matrices are unimodular and give
\[
 U_N\begin{pmatrix}2&b\\-a&N-1\end{pmatrix}V_N
                         =\operatorname{diag}(1,2N).       \tag{SZ.38}
\]
Consequently the lattice quotient for \(N>0\) is
\(\mathbb Z/(2N)\); for \(N=0\) it has the residual free
\(\mathbb Z\). These are lattice statements. The finite quotient
has not yet been identified with a collection of origin-link
boundary components.

For the currently marked varying-source family, use the stronger
choice \(N=M\), or a positive multiple of \(M\), and take the
literal one-gamma parameter \(r=v^{N/M}r_0\). All finite-cap powers
are then integral in \(v\). The rescaled loop contains \(N/M\)
full one-gamma scalar turns in addition to the source turn. At
the fixed comparison source these are \(bN/M\) of the proved
shorter loops of P3K.35. No class in \(\Theta_7\) is divided.

Divisibility by \(M/b\) is the arithmetic lower requirement at a
fixed source. It is not used here as a global varying-source
endpoint theorem: the rational \(b\)-th root \(g_0(t,v)\) in
P3K.35 must still be tracked around the source puncture before
that smaller rescaling can be asserted. The actual finite-cap
root maps and their source-parameter units remain part of the
relative comparison.

The symbolic Smith identities and512 positive-\(N\) evaluations
are saved in code/part3_fourfold/source_zero_rescaled_periods.py
and its JSON/output. The remaining work is the compact relative
periodic chart construction and its oriented boundary map.

## 19. Exact Tate units on the two-node base

The period matrices used in Section 18 can be obtained from actual
Tate coordinates on the full two-node base. The source has
\[
 c_4=16((1-2v)^2-3T).
\]
This is a unit at the origin. Its discriminant has the two simple
factors \(q_1q_2\) of Section 10. Inverting the convergent \(j\)-series
therefore gives
\[
 Q=q_T=q_1q_2u_Q,\qquad u_Q(0)=1/256.                 \tag{SZ.39}
\]
The indicated value follows directly from
\[
 j^{-1}=
 \frac{(1-2v)^2T^2-4T^3-4(1-2v)^3v^2-27v^4+
          18(1-2v)Tv^2}
 {256((1-2v)^2-3T)^3}.
\]
All units in this section are holomorphic and nonvanishing on a
smaller two-node polydisc; their logarithms are fixed there.

Here is the marked section map, including its lift rather than just
its class in the Tate group. The convergent Tate Weierstrass sums
extend over the node chart with coordinates \(Z_0,W_0\) and
\(Q=Z_0W_0\). In these coordinates their first terms are
\(x_T=Z_0+W_0+\text{higher terms}\) and
\(y_T=-W_0+\text{higher terms}\). They consequently give the
invertible analytic node map to the Weierstrass node, after the
chosen \(c_4\)-root scaling and the Weierstrass translation. This is
also seen directly by writing each negative-index summand as a
power series in \(W_0\) and \(Q\); the positive-index summands are
power series in \(Z_0\) and \(Q\).

The actual section \(G\) lifts through this node chart. Its two
coordinates vanish on opposite discriminant branches. Choose the
branch which, on the selected \(q_1=0\) normalization, represents
the lift \(Q P_G\). The linear terms of the explicit Morse map in
Section 10 are \(v+T/2\) and \(v-T/2\); hence those two vanishing
orders are one. Analytic division gives
\[
 Z_0(G)=q_1u_G,\qquad W_0(G)=q_2u'_G,\qquad
 P=P_G=\frac{Z_0(G)}Q=q_2^{-1}u_P.                   \tag{SZ.40}
\]
The branch is checked against the exact selected nodal value
\((1+\sqrt{1+v})/(1-\sqrt{1+v})\). Since
\(q_2|_{q_1=0}=-4v+O(v^2)\), it gives \(u_P(0)=16\).
Thus (SZ.40) retains the actual section and the marked period
lift, including its integral reindexing.

The line and its primitive translation have an equally direct
formula. Set
\[
 f_P(Z)=\frac{\Theta(Z/P)}{\Theta(Z)}.
\]
The exact divisor and multiplier identify \(f_P\) with the
canonical meromorphic section of the actual Cartier line. The
function \(X\), whose divisor is \(G+(-G)-2O\), consequently has
the literal expression
\[
 X(Z)=c_X f_P(Z)f_{P^{-1}}(Z).                       \tag{SZ.41}
\]
To see its scalar at the collision, evaluate at a fixed ordinary
Tate point, for example \(Z=-1\). The identity
\(\Theta(QZP)=-(ZP)^{-1}\Theta(ZP)\) shows that
\(q_2 f_P(-1)f_{P^{-1}}(-1)\) is a nonzero holomorphic
unit. The actual value \(X(-1)\) is a holomorphic unit there.
Hence
\[
                         c_X=q_2u_X,\qquad u_X(0)=-1/4 .
                                                               \tag{SZ.42}
\]
For the last value, the limiting source is
\(Y^2=X^3+X^2\), so the retained scaling is
\(X=4Z/(1-Z)^2\), and (SZ.41) gives \(c_X\sim-4/P\).
No rational frame is discarded in this evaluation.

The target-point primitive lift of Section 6 is now exactly
\[
 U_a:(Z,V)\longmapsto(P^{-1}Z,c_X^{-a}V).             \tag{SZ.43}
\]
Indeed
\[
 f_P(Z)f_{P^{-1}}(Z/P)=1,
\]
so substituting (SZ.41) into the source and target Cartier
coefficients cancels every \(Z\)-dependent factor. For \(a=2\)
the literal map (SZ.16) is applied first. The resulting identity
retains its central Cartier component.

Combining (SZ.18) and (SZ.43), the two actual periods are
\[
 \begin{split}
 h:(Z,V)&\longmapsto
       (QZ,P^aV),\\
 g:(Z,V)&\longmapsto
       (P^{-b}Z,\,
        2(-1)^{b+1}\lambda_0v^Nq_1c_X^{-2}V).
 \end{split}                                                   \tag{SZ.44}
\]
Their valuation matrices along \(q_1=0,q_2=0,v=0\) are precisely
\[
 I,\qquad W=\begin{pmatrix}1&b\\-a&-2\end{pmatrix},
 \qquad E=NE_{22}.
\]
Every remaining factor in (SZ.44) extends as a unit. This proves
the actual period/unit input to the sector fan construction; the
earlier winding calculation alone was not used as that input.

## 20. Residual periods on the two rank-one faces

The rank-one face actions retain nontrivial units. At the
\(q_2=0\) face use the integral target character
\[
                         Y=Z^aV
\]
and the period basis \(h,\ k=gh^{-b}\). The kernel of \(W\)
is generated by \((-b,1)\), and (SZ.44) gives exactly
\[
 \begin{split}
  k:Z&\longmapsto (q_1u_Qu_P)^{-b}Z,\\
  k:Y&\longmapsto
   \frac{2(-1)^{b+1}\lambda_0v^N}
        {q_1u_Q^2u_P^4u_X^2}\,Y.                    \tag{SZ.45}
 \end{split}
\]
The other period has source multiplier \(Q\) and line multiplier
\[
                         c=(QP)^a=(q_1u_Qu_P)^a .
\]
Thus its actual central source is the nodal quotient of the Tate
chain, with the degree-zero line glued by \(c\). The kernel map
(SZ.45) acts on that line, including the source automorphism
on the normalization. It has not been replaced by the identity.

One can verify a uniform contraction on this retained line near
the strict \(q_2\) face. Restrict to
\(|q_2|\leq\eta|q_1|\), with fixed sufficiently small \(\eta\).
Then \(|v|\) is comparable with \(|q_1|\).
Use the usual Tate fundamental annulus
\(|Q|\leq|Z|\leq1\), and interpolate a positive line metric
between its two end values, whose ratio is \(|c|\).
Its maximum-to-minimum ratio is at most
\(C|q_1|^{-a}\). The same interpolation on the plumbing annuli
extends to the nodal normalization, with its prescribed gluing
at the two preimages of the node.

The source multiplier in (SZ.45) has magnitude bounded by
\(C|q_1|^{-b}\), whereas \(|Q|\leq C|q_1|^2\).
For sufficiently small \(|q_1|\), reindexing its image into the
fundamental annulus uses at most two source periods when
\((a,b)=(1,2)\), and at most one when \((a,b)=(2,1)\).
Each reindexing contributes at most \(C|q_1|^{-a}\)
to the line norm ratio. Formula (SZ.45) consequently gives the
operator bounds
\[
 \|k\|\leq
 \begin{cases}
 C|\lambda_0|\,|q_1|^{N-4},&(a,b)=(1,2),\\
 C|\lambda_0|\,|q_1|^{N-5},&(a,b)=(2,1).
 \end{cases}                                                   \tag{SZ.46}
\]
For \(N\ge6\) these are strict contractions after shrinking.
On compact subsets away from the exceptional intersection,
the same conclusion follows by decreasing \(|\lambda_0|\).
The norm shell therefore proves freeness and proper
discontinuity of the retained kernel period on its nonzero
line. At \(q_2=0\) this is a statement on the actual normalized
nodal line with its node gluing, not on a substitute product.

At the strict \(v=0\) face the kernel of \(E\) is generated by
the source period \(h\). Its transverse character is \(Z\),
and its exact multiplier is \(Q=q_1q_2u_Q\). On that face,
away from the collision, \(q_1=q_2=T\) and
\(0<|Q|<1\) on a small source tube. Hence this residual action
is the actual Tate contraction in \(Z\). Its other component,
the line multiplier \(P^a\), is retained on the component
chain. These two kernel actions supply the required proper
rank-one face quotients. The common-face subdivisions and
their collision quotient are still separate geometric work.

## 21. Finite-cap chain attachment with both deck directions

This subsection concerns the actual E7 cap away from the collision
neighbourhood. Write its order as \(m\), its signed norm as \(n\),
and take \(N=km\) with \(k>0\). For the sphere markings here
\(n=\pm1\). The same Bezout argument below retains every
coprime signed norm. Write
\[
 A=v^{kn}r_0^nA_0,\qquad B=v^{km}r_0^mB_0,\qquad
 A_0^m=B_0^n,\quad[A_0,B_0]=1.                      \tag{SZ.47}
\]
Choose \(u,w\in\mathbb Z\) with \(nu+mw=1\). The actual
positive chain generator is
\[
 H=A^uB^w=v^kr_0H_0,\qquad H^m=B,\quad H^n=A.        \tag{SZ.48}
\]
In particular \(A\) shifts a chain index by \(kn\), including
the negative shift for \(n=-1\). It is not replaced by \(H\)
when retaining the finite root character.

The source/line/root pairings are exactly the existing catalogue
branches: the good III* root \(m=4p\) belongs to
\((a,b)=(1,2)\) in F41, and the reduced III root \(m=4p-1\)
belongs to \((a,b)=(2,1)\) in K24. No cross-pairing of these
two equations with the other source line is made. In the good
root, \(G'_0=(0,0)\) is the marked nonzero two-torsion point
on \(Y'^2=X'^3+X'\), so \(Q'_0=2G'_0=O\), and the recorded
division branch is the one through the identity. In the
reduced root, \(Q'=G'\) has the recorded nonidentity component
class of order two; the odd order \(m\) preserves this class,
and the source norm and division branch are precisely those
constructed on the resolved III source in K24/F37.

The root source and line extend through the source value \(v=0\).
For the good III* root \(m=4p\), the literal equation is
\[
 Y'^2=X'^3+X'+(1-2v)z^{2p}X'^2+v^2z^{6p},\qquad
 G'=(0,vz^{3p}).
\]
For the reduced III root \(m=4p-1\), it is
\[
 Y'^2=X'^3+zX'+(1-2v)z^{2p}X'^2+v^2z^{6p}.
\]
The smooth good-root family, and the simultaneous minimal
resolution of the reduced III root, retain the same marked
Cartier and invariant-ideal maps as F41 and K24. Their coefficients
are holomorphic in \(v\); the added terms have the displayed
higher \(z\)-orders. The division section and finite averaging
therefore extend on the same inverse multiplication branch.
The norm ratio is a holomorphic unit: its generic central
value is \(-2\) in the good-root case and \(+2\) in the reduced
case, by (SZ.11)--(SZ.12). Since it is a function on the base,
these values determine its nonvanishing on the full compact
central source fibre. Its chosen analytic root and the finite
character thus extend over a smaller \((z,v)\) polydisc.

On the actual root line use the full chain
\[
 X_j=V/v^j,\qquad Y_j=v^{j+1}/V,\qquad X_jY_j=v.
                                                               \tag{SZ.49}
\]
The transition is
\(X_{j+1}=Y_j^{-1},\ Y_{j+1}=vY_j\). Source and inverse
line frames make these equations invariant under every
transition of the actual line. The map \(H\) sends chart
\(j\) to chart \(j+k\), applying \(r_0H_0\) to \(X_j\)
and its inverse line map to \(Y_j\). Its source map is the
actual root translation and deck map contained in \(H_0\).
Thus \(A=H^n\) has its exact root character and signed shift.
The action is free and properly discontinuous also at \(v=0\):
a nonzero iterate changes the chain index, and a finite union
of consecutive node and middle charts has a compact
fundamental region over a closed smaller source tube.
For \(v\ne0\) this quotient is literally the original cap.

The ordinary-to-cap overlap requires its logarithmic origins;
one does not multiply a fractional power of \(v\) into a single
central chart. Put
\[
 t=\frac{\log v}{2\pi i},\quad
 s_1=\frac{\log q_1}{2\pi i},\quad
 s_\infty=\frac{\log q_\infty}{2\pi i},\quad
 h=1-T_0(v)q_\infty.
\]
Then \(q_1=q_\infty^{-1}h\), so
\[
 s_1=-s_\infty+\frac{\log h}{2\pi i}.
\]
The actual ordinary-to-cap translation at the rescaled parameter
is
\[
 F=F_0+nk\,t\,s_\infty\delta .
\]
Here \(F_0\) is the actual source, Cartier and cap comparison
at the fixed reference scalar. It is holomorphic in \(v\)
through zero on this annulus. Use the two origins
\[
 o_{\rm ord}=nk\,t\,s_1\delta,\qquad
 o_{\rm cap}=nk\,t\,\frac{\log h}{2\pi i}\delta .
\]
Their overlap is the literal identity
\[
                    F+o_{\rm ord}-o_{\rm cap}=F_0.   \tag{SZ.50}
\]
After a positive \(q_\infty\) continuation,
\(o_{\rm ord}\) changes by \(-nk\,t\delta\).
The coordinate \(\eta=\zeta-o_{\rm ord}\) therefore changes
by \(+nk\,t\delta\), which multiplies its line coordinate by
\(v^{nk}\). This is exactly the shift of the full chain by
\(nk\) in (SZ.47), together with the retained \(A_0\) map.
Only after that continuation is included is the chain
quotiented by its scalar period.

The parameter deck is equally explicit. It is
\[
 R_{\rm ord}=q_1^{nk},\qquad R_{\rm cap}=h^{nk},
\]
and the actual square is
\[
                        F_{t+1}R_{\rm ord}
                              =R_{\rm cap}F_t.       \tag{SZ.51}
\]
Indeed \(F_{t+1}/F_t=q_\infty^{nk}\).
The cap unit acts on each node chart by
\[
           (X_j,Y_j)\longmapsto(h^{nk}X_j,h^{-nk}Y_j)
\]
with unchanged index and unchanged finite root map. It extends
at \(v=0\), where \(h=1\). The origin \(o_{\rm cap}\) has
exactly the change \(nk\log(h)/(2\pi i)\delta\), so it
makes this actual deck pure. The ordinary origin does the
same for \(R_{\rm ord}\). Thus (SZ.50) descends in both
directions, with all units and signed cap characters retained.
Here subtraction of \(o_{\rm cap}\) defines the new periodic
coordinates on the punctured logarithmic cover. It does not
assert that \(\exp(t\log h)\) is holomorphic at \(v=0\) in
the old coordinates. The change is multiplication by a scalar
depending only on the invariant base \((q_\infty,v)\), so it
commutes with every actual source translation, line map and
finite root map in \(H_0\). Consequently the new chain atlas
carries exactly that same \(H_0\), extends in (SZ.49), and
has the literal extending overlap \(F_0\).
It is the precise chain/origin comparison used in P2.8,
applied here to the displayed varying source and line.

These charts give the finite-base partial attachment away
from the collision. They do not complete the collision fan,
identify its oriented boundary components, or assign a
source-loop return. The exact period and signed origin
identities are executed in
code/part3_fourfold/source_zero_units_caps.py and its JSON/output.

## 22. Analytic quotient of the period-equivariant collision atlas

This is the analytic assembly for the explicit sector fans in
the root's source-zero prism note and the independent
source-zero prism audit. The source-loop characteristic
calculation is still separate. For the default selected cusp,
the I-face uses the basis \(e_1,-e_2\), so its boundary
triangles have the required diagonal \(e_1-e_2\). The earlier
\(e_1,e_2\) choice gives the separately specified positive
fan of Section 15. These two boundary markings are not
identified by a source-loop assertion.

On the E face prescribe all rays
\((0,j,1,0)\), \(j\in\mathbb Z\), before extending the
common H refinement. The period \(g\) shifts \(j\) by \(N\).
These are precisely the primitive height-one rays of the
chain (SZ.49); the raw rays with \(j\) divisible by \(N\)
would omit its actual component charts. The W face already
has primitive consecutive rays in its image lattice, and
the I face is the retained unimodular cusp fan. The common
H overlay retains its primitive integral ray multiples.
In particular its rational height-one drawing does not
declare the resulting central divisor reduced.

The analytic toric charts are the affine semigroup charts
of that actual common fan, pulled back by the displayed
blowup coordinates on the base. A period indexed by
\(n\in\mathbb Z^2\) has the lattice map
\[
 (x,r,s)\longmapsto
          (x+rP_0n+sHn,r,s)
\]
on the \((P_0,H)\) sector. Its remaining factors are the
units in (SZ.44). Multiplication by an extending base unit
acts on every toric character and its inverse character
by the same literal unit powers, so it is an analytic
isomorphism of each corresponding semigroup chart.
The unit factors are homomorphisms in \(n\), because they
are products of the two commuting periods in (SZ.44).
Hence the full period maps, including their inverses,
give an honest action on this analytic atlas. The common
H refinement is period-equivariant, so these actions
agree on every overlap.

Here is a compact-fundamental-cover argument which also
retains the units. For a nonzero base value, let
\(L\) be the real two-by-two matrix of logarithmic
magnitudes of the actual two periods. On a corner
sector it has the form
\[
                        L=-rP_0-sH+C ,
\]
where \(r,s\) are the positive logarithmic radii of its
two base coordinates and \(C\) is bounded. This follows
from (SZ.44) and the extending base units. The fixed
constant \(\lambda_0\) is part of that bound.
On a sufficiently small corner polydisc \(r,s\) are
large. In the I sector the determinant polynomial and
the norm of \(rI+sH\) give a lower singular-value bound
by a positive constant times \(r+s\). In either rank-one
sector its determinant is a positive constant times
\(s(r+s)\), while its norm is bounded by a constant
times \(r+s\); its lower singular value is therefore
bounded below by a positive constant times \(s\).
Thus the bounded matrix \(C\) does not destroy
invertibility there.

Use the actual parallelogram
\(L([0,1]^2)\) for the logarithmic magnitudes, with
compact angular coordinates. The corresponding
parallelogram for \(-rP_0-sH\) differs from it by a
uniformly bounded set. In the I sector the inverse
piecewise-linear prism map has only finitely many
simplex types modulo periods; the determinant bounds
just given keep this bounded perturbation in finitely
many adjacent cell types. In the rank-one sectors this
same conclusion follows directly from the strip
assignment (PF.8)--(PF.10): its strip width is
\(s+rc\), its vertical height is \(s\), and the bounded
perturbation changes the two assigned integers by a
bounded amount. The parallelogram and strip differ
by only a bounded number of vertical translates,
independent of \(r/s\); this follows by comparing
the linear function \(rd\,x/(s+rc)\) with the two
linear pieces of the displayed \(f(x)\).

Consequently a fixed finite set of cone representatives
and their adjacent charts covers the actual quotient.
The logarithmic magnitudes in their monomial coordinate
charts have a uniform upper bound. Their angular parts
lie in compact tori. Closing these coordinate regions,
including their toric faces, therefore gives compact
sets over a closed smaller base polydisc. The same
argument near an interior point of the exceptional
base curve uses the full-rank matrix H alone.

At a rank-one boundary the remaining noncompact
direction is exactly its kernel period, rather than
an additional missing toric origin. In the W sector,
use the actual line-norm shell for (SZ.45), with the
uniform strict estimate (SZ.46). In the E sector,
use the Tate shell for \(Z\mapsto QZ\).
Adding these shells to the preceding finite toric
chart cover gives a compact fundamental cover at
the two rank-one faces as well.
At their intersections with H the same kernel
vectors have nonzero H image, because
\(\det H=2N\ne0\). Hence an unbounded sequence of
kernel translates cannot accumulate at a fixed
H-cone chart: the full-rank cone separation
controls the closures of the face shells.
This verifies compatibility of the shell cover
with the exceptional-face compact cover.

These same charts prove proper discontinuity and the
Hausdorff property. On a full-rank face, a nonzero
period cannot stabilize a bounded polyhedral cell,
because it translates that cell by the nonzero
vector \(P_0n\) or \(Hn\). Only finitely many
translates of a compact chart meet it. On a rank-one
face its possible stabilizer is the explicitly
identified kernel; its strict norm contraction
meets a compact shell only for finitely many
iterates. The estimates are uniform on the
neighbouring charts. Thus the full equivalence
relation is locally a finite union of closed
graphs on these compact covers. Its quotient is
Hausdorff, and inverse images of compact smaller
base sets are compact.

Over \(v\ne0\) the chart comparison is the specified
family, not only a birational torus comparison.
On the selected divisor the I-face is its chosen
fan. On the other nodal divisor the W-face is the
actual source Tate chain and degree-zero line
with gluing \(c=(QP)^a\), followed by the actual
kernel contraction (SZ.45). This is the ordinary
nonzero-line source filling under the explicit
theta/Cartier map of Section 19. The E face and
every H modification lie over \(v=0\).
The finite-base pieces have the two literal deck
squares (SZ.50)--(SZ.51) in their changed ordinary
coordinate \(\eta\). The collision fan above uses
the original Tate coordinate \(V\). Their common
physical delta character is retained, but the
coordinate change between these two central
atlases still has to be extended. Its exact deck
is recorded below.

This proves the local normal analytic collision
quotient. Section 21 proves the finite-base partial
attachment in its own chain coordinates. Their
global central attachment is a separate remaining
map. A
period-equivariant toric resolution can subsequently
be performed relative to the already smooth I,
W and primitive E boundary subfans. Its new ray
multiplicities must be retained. The resulting
oriented boundary, the fixed-stratum incidence
and the characteristic pairing have not been
computed in this subsection; none is replaced
by the determinant or fundamental-region count.

The base multiplicities are also literal. Since
\(q_1-q_2=T_1(v)-T_0(v)=v\,u_v(v)\), with
\(u_v(0)=4\), the I corner has
\(q_1=xy,q_2=y\) and
\(v=y(x-1)/u_v(v)\); the W corner has
\(q_2=xy,q_1=y\) and
\(v=y(1-x)/u_v(v)\). The E corner uses
\(v=xy,q_1=y\). Thus an integral ray with
base coordinates \((r,s)\) has \(v\)-order
\(s,s,r+s\) in the I, W, E sectors respectively.
These orders apply to the primitive integral
rays of the actual refinement. They retain
every higher H multiplicity. Each normal
toric chart is the closure of its dense
torus over the nonzero parameter, so no
total-space component is contained in the
central fibre, and its
parameter function is a nonzero divisor.
Its local rings are therefore torsion free
over the one-dimensional parameter ring,
which proves flatness of this local quotient over
the \(v\)-disc.

**Scope correction, recorded 2026-11-17 after the actual
chain-deck comparison.** The previous version of this
paragraph invoked \(F_0\) to assemble the collision
fan and finite caps globally. It had not supplied
the central transition from the Tate \(V\) atlas
to \(\eta=\zeta-o_{\rm ord}\). That invocation is
retained here as an identified incomplete step,
not as a proved compact global filling. At fixed
old \(\zeta\), positive \(q_1\) continuation gives
\[
 \eta\longmapsto\eta-nk\,t\,\delta,\qquad
       V_\eta\longmapsto v^{-nk}V_\eta .                    \tag{SZ.51a}
 \]
Its inverse overlap has \(v^{nk}\). Positive
\(q_\infty\) continuation instead gives \(v^{nk}\),
as in Section 21. These arrows retain their signs.
The literal \(h,g\) collision fan has not yet been
identified with a central atlas carrying (SZ.51a).
The local regularization and the compact interior/H
normal calculations below do not use that missing
global attachment. No compact global \(W\), its
signature, or a source-loop return is assigned here.

## 23. Remaining original-u cap-root endpoint dictionary

Sections 19--22 construct the literal marked \((v,T)\) family,
with its cap root defined by \(z_{\rm new}^m=T^{-1}\).
The comparison to a source loop in the original normalized
\((u,t)\) presentation retains a further root arrow. The exact
source map is
\[
 (X,Y,T,v)=(u^2x,u^3y,u^4t,u^3),\qquad
                   z_{\rm old}^m=u^4z_{\rm new}^m.     \tag{SZ.52}
\]
Thus a full positive original \(u\)-loop covers three positive
\(v\)-loops, and the continued root comparison has the
additional rotation \(z_{\rm old}\mapsto\zeta_m^4z_{\rm old}\).
This is an actual root-coordinate factor, rather than a bounded
unit with a chosen logarithm on the full puncture.

The generic suspension square is already exact. Under the
source and Cartier coordinate isomorphism \(I_u\),
\[
 I_u U_{a,\rm old}I_u^{-1}=u^{2a}U_{a,\rm new},\qquad
 q_{\rm old}=u^{-4}q_{\rm new}.
\]
Since \(ab=2\), the factors cancel in
\[
 2(-1)^{b+1}\lambda q_{\rm old}U_{a,\rm old}^{\,b}.
\]
Consequently this ordinary comparison retains the same scalar
\(\lambda\). The finite-cap character and its actual norm lift
must still be carried through the root rotation in (SZ.52).
No equality of their endpoint maps follows from the displayed
ordinary cancellation alone.

The remaining typed square has the old cap on the root
\(z_{\rm old}^m=t^{-1}\), the new cap on
\(z_{\rm new}^m=T^{-1}\), and the source/Cartier map (SZ.52).
It must intertwine the actual \(A_0\), its division-section
branch, and its finite line character, including the
\(\zeta_m^4\) endpoint. Until this square is written,
the audited analytic quotient in Section 22 retains its
specified \((v,T)\) marking. It assigns neither an original
\(u\)-loop return nor a numerical \(v\)-loop return.

### 23.1. Literal minimal-root coordinates and the retained reduced period

Write the actual minimal root coordinates as
\(X'=z_{\rm new}^{2p}X,\ Y'=z_{\rm new}^{3p}Y\), and use
the corresponding old coordinates \(x',y'\). On the universal
\(u\)-cover choose \(z_{\rm old}=u^{4/m}z_{\rm new}\).
Direct substitution in (SZ.52) gives
\[
 \begin{array}{c|cc}
 m&X'&Y'\\ \hline
 4p&x'&y'\\
 4p-1&u^{-2/m}x'&u^{-3/m}y'.
 \end{array}                                                   \tag{SZ.53}
 \]
These maps send the marked section to
\((0,vz_{\rm new}^{3p})\). The old-to-new arrow after a
positive \(u\)-turn has endpoint \(D_{\rm new}^{-4}\).
For the reduced case its literal coordinate factors are
\((\zeta_m^{-4},\zeta_m^{-2},\zeta_m^{-3})\) on
\((z_{\rm new},X',Y')\). They are the factors of \(D^{-4}\)
because \(4p=m+1\). The good case has the same base factor
and identity factors on \(X',Y'\).

In the reduced branch the division section has the nonidentity
component class. On the marked good fourth-root lattice, its
central logarithm can be chosen to tend to
\((1+i)/2\). The exact difference is then
\[
             4\log R-\log(4R)=2(1+i),                       \tag{SZ.54}
 \]
where the second logarithm is the small one at the identity.
The right-hand side is an actual transported lattice period.
It is retained in the annular affine cochain. In particular the
construction does not multiply it by \(\log u\) and assert that
the resulting reduced-root translation extends.

The reference overlap \(F_0\) in Section 21 also needs its full
annular integral marking. One concrete specification is to fix
one nonzero \(u_*\), transport the old literal overlap (including
its prescribed integral delta term) through the canonical
Cartier map \(I_{u_*}\), and continue that full affine overlap
on the cap annulus over the \(v\)-disc. That annulus avoids the
source collision. Its source, line and norm maps are the
extending maps of Section 21. This specifies the initial
annular integer rather than inferring it from the norm equation.
The relative atlas comparison retaining (SZ.54) is being written
separately by the blind-control branch; it has not been used to
assign a source-loop class here.

## 24. Actual fixed strata of the regular collision fan

The two executed regular fans are
\[
 (a,b,N)=(2,1,6),\qquad(1,2,8).
 \]
They retain the original lattice, the default I boundary,
the primitive E chain, the common H refinement, and every
period vector. Let a maximal cone have its ordered primitive
column matrix \(C\), with \(\det C=1\), and put \(A=C^{-1}\).
Its four holomorphic coordinates are the characters given by
the rows of \(A\). The physical circle is
\(\delta=(0,1,0,0)\), so its literal weights are
\[
                         w_i=A_{i2}.                         \tag{SZ.55}
 \]
Here the second column means the V coordinate, with indexing
starting at one. No height or base character is substituted for
the physical circle.

In this affine chart the fixed set is the coordinate space
where every coordinate of nonzero weight vanishes. Let
\(\tau\) be the cone generated by exactly those ray columns.
It is the unique smallest face whose real linear span contains
\(\delta\): the expression of \(\delta\) in a basis is unique.
In every adjacent regular cone containing this face the
coefficients on the face are the same, and all other
coefficients are zero. Thus these fixed charts glue to the
orbit closure \(V(\tau)\). Two different such minimal faces
cannot meet in one cone, again by uniqueness of the basis
expression. This gives the connected fixed components.

The recorded period maps fix \(\delta\). Their actual face
permutations therefore identify precisely the minimal-face
orbits used in the computation. In particular neither a
lattice determinant nor the number of subdivision centres is
being substituted for a component count.

The executable
\(\texttt{code/part3\_fourfold/source\_zero\_fixed\_charts.py}\)
exports \(C,A\), all four physical weights, the actual
parameter orders, the minimal face, its canonical period
and vertex permutation, and all component incidences.
Every chart satisfies
\[
 \sum_i w_i C_i=\delta,\qquad
 \sum_i w_i\operatorname{ord}_{D_i}(v)=0.                   \tag{SZ.56}
 \]
The local quotient contains the following fixed components:
\[
 \begin{array}{c|rrr|r}
 (a,b,N)&\text{points}&\text{curves}&\text{surfaces}&
       \text{maximal charts}\\ \hline
 (2,1,6)&1287&2000&1168&9851\\
 (1,2,8)&10122&8523&3523&41902.
 \end{array}
 \]
The I, E and H tags in the export remain part of every
component's data.

An interior minimal face projects into the interior of one
base sector. Its star modulo its span is complete: a large
positive multiple of a relative-interior point of that face
moves any representative vector into the full local support.
The resulting star is a complete smooth toric fan. Its
period stabilizer is trivial, so this compact component is
identified with one actual lift of that orbit closure.
All original-polydisc units restrict to nonzero constants
there. In the normal derivative, differentiating such a unit
produces a term multiplied by a vanishing normal coordinate;
the retained first-order transition is exactly its constant
multiple of the toric normal transition. Unwrapping by the
recorded period removes these constants coherently, since
there is no stabilizer. This proves the toric normal-bundle
description used below for interior components.

## 25. Compact interior normal-link characteristic residues

This section computes a precisely oriented local quantity.
Let \(F\) be one compact fixed component in the smooth
complex fourfold atlas, with its complex orientation.
Let its complex normal roots be \(x_i\), and retain the
nonzero physical circle weights \(w_i\). Orient its normal
sphere boundary by the original complex normal orientation,
then use the positive physical orbit to orient the quotient.
With \(u\) the corresponding degree-two circle variable,
the rational characteristic residue of that normal link is
\[
 {\cal R}(F)=
 [u^{-1}]\int_F
 \frac{4u^3-u\{p_1(TF)+\sum_i(x_i+w_i u)^2\}}
      {24\prod_i(x_i+w_i u)}.                              \tag{SZ.57}
 \]
The coefficient is taken in the Laurent expansion at infinity.
This formula retains finite circle stabilizers: its integral
is the rational orbifold pushforward, rather than an
unjustified smooth replacement of a weighted projective link.

Here is the actual bundle calculation. On the sphere bundle,
the tangent bundle together with the radial real line is
the pullback of \(TF\) and its complex normal bundle.
Quotienting the orbit removes the physical orbit line,
so the quotient tangent bundle has the same stable
Pontryagin class as the equivariant restriction of
\(TF\oplus\nu_F\). The equivariant Thom class restricts to
\(\prod_i(x_i+w_i u)\). Integrating on the normal sphere
quotient is therefore the coefficient of \(u^{-1}\) after
division by this Euler class. This can also be obtained by
applying the localized pushforward identity to the normal
disc and its sphere boundary. The exact primary integration
identity is Atiyah--Bott, *The moment map and equivariant
cohomology*, Topology 23 (1984), printed page 9, formula
(3.8), with normal Euler formula (3.7) and localization
Theorem (3.5).

The residue normalization has a direct fibre check. Conjugate
each negative-weight normal line, keeping the physical
circle orientation. For positive weights the fibre is the
weighted projective quotient and the circle class \(u\)
is the positive hyperplane class. Its projective-bundle
relation is \(\prod_i(x_i+w_i u)=0\), and its fibre
integral of \(u^{r-1}\) is \(1/\prod_iw_i\). The latter
follows from the actual power map
\([z_i]\mapsto[z_i^{w_i}]\), whose generic degree is
\(\prod_iw_i\) and whose pullback of \(u\) is the
ordinary hyperplane class. The relation then determines
all higher pushforwards recursively, exactly as the
coefficient of \(u^{-1}\) in the reciprocal Euler
polynomial. A conjugated negative line changes
\((x_i,w_i)\) to \((-x_i,-w_i)\) and reverses the
original normal orientation. Its denominator sign in
(SZ.57) is precisely that reversal. This proves both
the normalization and the signed-weight formula.

For a point (SZ.57) is
\[
       \frac{4-\sum_i w_i^2}{24\prod_i w_i}.
 \]
For a curve it is
\[
 -\frac1{24\prod_iw_i}
  \int_F\sum_i\left\{\frac{4-\sum_jw_j^2}{w_i}
                                 +2w_i\right\}x_i.        \tag{SZ.58}
 \]
For a surface put
\[
 P=w_1w_2,\quad c=4-w_1^2-w_2^2,\quad
 A=\frac{x_1}{w_1}+\frac{x_2}{w_2},\quad
 B=\frac{x_1^2}{w_1^2}
       +\frac{x_1x_2}{w_1w_2}+\frac{x_2^2}{w_2^2}.
 \]
Then it is
\[
 \int_F\frac{cB+2(w_1x_1+w_2x_2)A
                    -p_1(TF)-x_1^2-x_2^2}{24P}.           \tag{SZ.59}
 \]
For example weights \((1,-1)\) give
\((p_1(TF)-3(x_1-x_2)^2)/24\). Conjugating the
negative-weight normal line reverses the normal orientation
and changes this to the positive-Hopf expression. That
orientation reversal is retained; neither expression has
yet been identified with the completed family's Jin
boundary convention.

For an interior component choose an auxiliary cocharacter
\(\epsilon\) in its canonical unwrapped lattice. If a chart
occurs at period \(n\), its auxiliary tangent and normal
weights are exactly
\[
                  C^{-1}T_n\epsilon.                       \tag{SZ.60}
 \]
This is the dual of the literal map
\(C_{\rm unwrapped}=T_{-n}C\). The compact-component
pushforward (3.8) divides (SZ.58) or (SZ.59) at each
auxiliary fixed point by the product of its tangent
weights. All coefficients are rational numbers computed
from integer matrices.

The certificate
\(\texttt{source\_zero\_interior\_residues.py}\) uses two
independent generic auxiliary circles for every component.
It verifies equality component by component, and exports
every value, rather than using only agreement of totals.
The sums over the compact interior components are
\[
 \begin{array}{c|r|r}
 (a,b,N)&\text{components}&\sum{\cal R}(F)\\ \hline
 (2,1,6)&4420&1299\\
 (1,2,8)&21776&4893/8.
 \end{array}                                                \tag{SZ.61}
 \]
These sums do not include the components tagged H, E or I.

## 26. Exact H-base normal degrees, including all three marked points

Put \(w=q_2/q_1\) on the exceptional base curve H.
Its marked points are \(w=0,1,\infty\), belonging to W,
E and I respectively. Use \(q_1\) as a generic normal
coordinate to H. The exact periods (SZ.44) have normal
orders given by H, and their remaining nonconstant
factors on this base curve are
\[
 \begin{split}
 h:\ &(Z,V)\longmapsto
           (wZ,\ w^{-a}V),\\
 g:\ &(Z,V)\longmapsto
           (w^b Z,\ w^{-2}(1-w)^N V),
 \end{split}                                                \tag{SZ.62}
 \]
after the powers of \(q_1\) have been written separately.
All omitted factors here are the explicitly retained
nonzero constants \(u_Q(0),u_P(0),u_X(0),u_v(0)\),
and \(2(-1)^{b+1}\lambda_0\). In particular the
\((1-w)^N\) term is not removed.

Consider any regular rank-three face on H. Its three
primitive vectors, after dropping the zero first base
coordinate, form a unimodular \(3\)-by-\(3\) matrix
\(B_H\). Its orbit closure is a curve with the actual
base parameter \(w\), and hence is \(\mathbb P^1\).
For its \(j\)-th normal line use the generic meromorphic
coordinate
\[
              \eta_j=Z^{p_j}V^{q_j}q_1^{s_j},
       \qquad (p_j,q_j,s_j)=\text{row}_j(B_H^{-1}).          \tag{SZ.63}
 \]
The actual occurrence of this face in a sector chart has
a recorded period \(n=(n_1,n_2)\). Let
\((p,q,r,s)\) be the dual row of that chart belonging,
under the recorded permutation, to this normal ray.
The exact lattice checks are
\[
 (p,q)=(p_j,q_j),\qquad
       s+(p,q)Hn=s_j.                                      \tag{SZ.64}
 \]
Consequently its coordinate pulls back to \(\eta_j\)
times a rational unit on the base. Write
\[
 e_w=p(n_1+bn_2)+q(-an_1-2n_2),\qquad e_1=Nn_2q.
 \]
The additional base factors of the three sector charts
are literal:
\[
 \begin{array}{c|cc|c}
 \text{sector}&x&y&
       \text{order of the coefficient at its marked point}\\ \hline
 W&w&q_1&e_w+r\\
 E&(1-w)/u_v&q_1&e_1+r\\
 I&w^{-1}&wq_1&-e_w+r-s-e_1 .
 \end{array}                                                \tag{SZ.65}
 \]
The last row uses the order at infinity. For each normal
line, the sum of these three orders is its degree.
Indeed the generic normal vector with \(\eta_j\)
coefficient one has exactly these coefficients in the
three holomorphic normal frames, so their zero and pole
orders give its divisor. This fixes the line-bundle
sign without selecting a different normal convention.

The fibre circle with cocharacter \((1,K,0,0)\) commutes
with every exact period and all the units in (SZ.62).
It therefore acts on every compact H fixed component
and on its actual normal bundle. On an H fixed surface
its fixed set consists of the rank-three H curves just
described, together with isolated points in the
intervening regular charts. There are no omitted fixed
curves in a sector interior: a three-dimensional face
whose base image has rank two has only a one-dimensional
fibre kernel, already spanned by the physical delta;
the chosen independent fibre circle is not in that span.

For an auxiliary fixed curve in such a surface, let
\(\eta\) be its auxiliary normal weight, \(d_t\) the
degree of that normal line, \(\beta_i,d_i\) the
auxiliary weights and degrees of the two ambient
normal lines. Let \(R\) denote the polynomial in
(SZ.59). Substitute
\[
 x_i=\beta_i u+d_i h,\quad
 p_1(TF)=\eta^2u^2+2\eta d_t hu,\quad h^2=0.
 \]
Writing the result as \(R_0u^2+R_hhu\), the exact
curve contribution is
\[
                         R_h/\eta-R_0d_t/\eta^2.            \tag{SZ.66}
 \]
This is division by the actual auxiliary Euler class
\(\eta u+d_t h\). The tangent Pontryagin class of
the base \(\mathbb P^1\) is zero. Isolated points
use the two nonzero tangent weights in (3.8).

As independent arithmetic checks, this same localization
computes \(c_1(TF)^2,c_2(TF)\) for every H surface.
Each auxiliary point contributes
\((\beta_1+\beta_2)^2/(\beta_1\beta_2)\) and \(1\);
each auxiliary fixed curve contributes \(d_t+4\)
and \(2\). The resulting signature
\((c_1^2-2c_2)/3\) and holomorphic Euler number
\((c_1^2+c_2)/12\) are integral. Two independent
fibre circles give the same value for every surface
and for every normal-link residue.

The executed certificate
\(\texttt{code/part3\_fourfold/source\_zero\_h\_residues.py}\)
retains all three point orders, periods, permutations,
normal degrees, auxiliary weights and characteristic
values. Its exact totals are
\[
 \begin{array}{c|r|r|r}
 (a,b,N)&\text{H components}&\text{full-fibre fixed curves}
                &\sum_H{\cal R}(F)\\ \hline
 (2,1,6)&28&52&-5171/4\\
 (1,2,8)&383&516&-4873/8.
 \end{array}                                                \tag{SZ.67}
 \]
Thus the combined compact interior and H contributions
are \(25/4\) and \(5/2\), respectively. They are local
normal-link characteristic sums. The I and E continuations,
their cap chain-index identifications, the global oriented
boundary map, and the source-family return are not
assigned by this calculation.

## 27. The full cap fractional period and the remaining annular attachment

On the actual E annulus \(v=0,\ 0<|T|<\epsilon\), the
presently executed collision atlas has fixed nodes
\(j\pmod N\). The period \(h\) has zero \(v\)-order;
\(g\) shifts \(j\) by \(N\). The source and Cartier
units on this annulus have zero \(v\)-order. Thus
positive \(T\) continuation fixes all \(N\) labels.
In the cap atlas \(A=v^{kn}r_0^nA_0\) shifts \(j\)
by \(kn\) while rotating the root. Its fixed-component
permutation is \(j\mapsto j+kn\pmod N\), with \(k\)
cycles of length \(m\) when \(n=\pm1\). An equivariant
central overlap would identify these component local
systems. The recorded atlases therefore still require
the full changed-origin deck. This identifies the
attachment gap; it does not rule out another filling.

The source part of that deck can be calculated exactly.
At \(v=0\), \(G_0=(0,0)\) is two-torsion on every
smooth source fibre. Its marked Tate representative
satisfies
\[
                         P^2Q=1.                           \tag{SZ.68}
 \]
Indeed \(2G_0=O\) gives \(P^2=Q^j\) for a locally
constant integer \(j\); the retained asymptotics
\(P\sim16/T,\ Q\sim T^2/256\) give \(j=-1\).
The already proved chord identity \(U_1^2=T^{-1}\)
has in the theta gauge source multiplier \(P^{-2}=Q\)
and line multiplier \(c_X^{-2}\). Dividing by the
literal source period \((Q,P)\) gives
\[
                         c_X^2=T/P.                        \tag{SZ.69}
 \]
The exact central periods are consequently
\[
 h=(Q,P^a),\qquad
 g=(P^{-b},\,2(-1)^{b+1}\lambda P).                         \tag{SZ.70}
 \]
For \(a=2\) the central Cartier line is trivial because
the restricted horizontal divisors \(2G\) and \(O\)
coincide. Its Tate trivialization is \(ZV\), since
\(P^2=Q^{-1}\). In this frame the reference suspension
over translation \(-G\) has scalar \(+2\). In the
good \(a=1,b=2\) branch it is the scalar \(-2\).
These constants also follow directly from the Hom map:
\[
 F_{21}=T/(2v)+O(1),\quad F_{12}=-T/(2v)+O(1),\qquad
 q_1/(vF_{21})\to2,\quad q_1/(vF_{12})\to-2.                \tag{SZ.71}
 \]

Put \(\mathcal B=QP^2\), with central value one on
the E annulus. In the good \(m=4p\) branch the
identity division section has representative
\[
                         R=\mathcal B^{1/m},               \tag{SZ.72}
 \]
using the root tending to one. Its \(m\)-th power
represents \(2G\), with the retained \(Q\) period.
It equals the actual cap branch: both specialize
to the identity, and the local inverse of
multiplication by \(m\) is unique there.
This identity continues along the connected
smooth annulus.

In the reduced \(m=4p-1\) branch, \(R-G\) is
\(m\)-torsion at \(v=0\) and lies in the small
identity inverse branch at III. It is therefore
zero on that annulus. The actual representative is
\[
                R=P\,\mathcal B^{-(m-1)/(2m)}.              \tag{SZ.73}
 \]
Its \(m\)-th power is \(P Q^{-(m-1)/2}\), the
representative of \(G\) with its exact integral
period. This retains the period in (SZ.54).

On a chosen root sheet the actual theta/Cartier
cap map is
\[
 \begin{array}{c|c|c}
 \text{branch}& A\text{ in the }(h,g)\text{ periods}
                    &\text{line multiplier}\\ \hline
 a=1,\ b=2,\ m=4p&
 h^{-n/m}g^{n/m}&(g_V/P)^{n/m}\\
 a=2,\ b=1,\ m=4p-1&
 h^{\,n(m-1)/(2m)}g^{n/m}&
                       (P^{m-1}g_V)^{n/m}.
 \end{array}                                                \tag{SZ.74}
 \]
The specified constant finite character is retained.
The source multiplier in each row is translation
by \(-nR\). Its \(m\)-fold line norm agrees with
the constructed cap lift, since the extra \(h\)
exponent is an integral source-period identification.
The ratio of the line lifts initially is a base
unit with cyclic norm one. Retain its prescribed
central character \(\chi\), and put
\(f=\log(r/\chi)\) on the actual cap-root polydisc.
The norm gives \(\sum_{j=0}^{m-1}f(D^jz)=0\).
The explicit extending finite average
\[
 \psi(z)=\frac1m\sum_{j=0}^{m-1}j f(D^jz)
 \quad\text{satisfies}\quad
                  \psi(Dz)-\psi(z)=f(z).
\]
Conjugating by the actual scalar gauge
\(\exp(-\psi)\) removes this norm-one unit.
This gauge commutes with the suspension and
retains the physical delta circle; it changes
the annular overlap by its literal extending
unit. After this carried gauge the remaining
ratio is the constant character \(\chi\),
fixed by the prescribed cap marking. One
does not replace cyclic norm one by an
\(m\)-th-power equation before this conjugacy.
This verifies the actual line map.

The central scalars are
\((-2\lambda)^{n/m}\) in the good branch and
\((2\lambda)^{n/m}\) in the reduced frame \(ZV\).
The norms retain their full source periods:
\[
 A^m=h^{-n}g^n\quad\text{(good)},\qquad
 A^m=h^{\,n(m-1)/2}g^n\quad\text{(reduced)}.                 \tag{SZ.75}
 \]
Thus the inverse cap map has the full fractional
period
\[
 f_{\rm cap}=
 \begin{cases}
 (n/m,-n/m),&a=1,\ b=2,\\
 (-n(m-1)/(2m),-n/m),&a=2,\ b=1 .
 \end{cases}                                                \tag{SZ.76}
 \]
Its order modulo the period lattice is exactly
\(m\) for \(n=\pm1\). The scalar-only E deck has
fractional period
\[
                    f_{\rm sc}=(bn/(2m),-n/m).             \tag{SZ.77}
 \]
In the reduced branch their difference is
\((-n/2,0)\), retaining the actual half source
period. Direct multiplication gives
\[
 E f_{\rm cap}=-nk\,\delta,\qquad
 H(f_{\rm cap}-f_{\rm sc})=
 \begin{cases}
 (0,0),&a=1,\\
 (-n,n),&a=2 .
 \end{cases}                                                \tag{SZ.78}
 \]
The reduced vector is the source/Cartier valuation
of \(B_0^{-n}\), including its chamber change.

The executable
\(\texttt{source\_zero\_cap\_fractional\_period.py}\)
checks source representatives, integral norms,
both signs, central Cartier constants and the
full matrices for 576 admitted numerical rows.
The displayed formulas establish the same
identities for every positive \(p,k\).

The maps (SZ.74) are chosen-sheet maps.
Continuation of \(\mathcal B^{1/m}\) around
\(q_1=0\) changes the division section by an
actual \(m\)-torsion point. The successive
root-sheet deck and its cyclic norm must be
constructed before using this as a finite
action on the collision filling. The abstract
finite order of (SZ.76) does not itself identify
the protected noncentral cusp quotient or its
multiplicity. That exact root-sheet, fan and
Cartier arrow remains the next attachment step.

### 27.1. Successive root sheets and the protected cusp

The successive-sheet norm is recorded independently in
the blind-control note
\(\texttt{notes/part3\_source\_zero\_cyclic\_norm.md}\)
and its exact certificate. For a positive strict
\(q_1\) loop, \(\mathcal B\) and the line radicands
in (SZ.74) have winding one. Thus the continued
good maps satisfy
\[
       A_j/A_0=(\zeta_m^{-jn},\zeta_m^{jn})
                    \quad\text{on }(Z,V).
 \]
For \(m=4p,\ n=\pm1\), their cyclic product has
the residual map \((Z,V)\mapsto(-Z,-V)\), followed
by \(h^{-n}g^n\). This is an actual two-torsion
source and line map. The reduced ratios are
\[
       A_j/A_0=
       (\zeta_m^{jn(m-1)/2},\zeta_m^{jn}),
 \]
whose cyclic product has no residual for odd \(m\).
The strict \(q_2\) loop gives the inverse sheet
increments and the same good order-two residual.
A loop enclosing both nodes has
\(\operatorname{wind}\mathcal B=0\). These calculations
retain the distinction between the strict-node
continuations and the E annulus by their exact
maps; no finite action is inferred from them.

There is also an exact obstruction to one proposed
root quotient. On the natural \(q_1=\xi^m\) cover,
the protected I period lattice is \(m\mathbb Z^2\).
Its components are labelled by
\(\mathbb Z^2/m\mathbb Z^2\). The translation
\(mf_{\rm cap}\) is \((n,-n)\) in the good branch
and \((-n(m-1)/2,-n)\) in the reduced branch.
Its second coordinate is a unit modulo \(m\),
so every component orbit has length \(m\).
The extra good map \((-Z,-V)\), when retained,
also moves a generic torus point; it supplies
no divisorial inertia. Thus \(q_1\) still has
order \(m\) at a generic descended divisor.
The prescribed noncentral cusp has order one.
This root-translation quotient therefore does
not furnish the required attachment. The
obstruction concerns this actual proposed
quotient, and does not assign a global
nonexistence result.

## 28. The actual local E cycles and their determinant-normal marking

The E fixed surface with chain index \(j\) has minimal
face generated by
\[
       (0,j,1,0),\qquad(0,j+1,1,0).
 \]
Its stabilizer is the actual \(h\) period. Unwrap a
chart by its recorded face period before projecting
to the star lattice. For a remaining primitive ray
\((Z,V,r,s)\), the star ray is \((Z,s)\), and
\(h\) changes it to \((Z+2s,s)\). It also changes
\(V\) to \(V-as\). Thus the exact star period
has length two; it is the marked I2 source cycle.

The two normal coefficients of this ray relative
to the displayed minimal face are
\[
             n_-=(j+1)r-V,\qquad n_+=V-jr.
 \]
The physical normal weights are \(-1,+1\).
For a generic meromorphic normal frame the normal
vector divisor is minus its character valuation.
Consequently the divisor of the positive-weight
determinant line initially has coefficient
\(n_--n_+\). More explicitly, in the E coordinate
\(x=v/T\) its normal coefficient ratio is
\(V^2/x^{2j+1}\). Multiplying this ratio by
\(Z^a\), justified by \(QP^2=1\), gives the
meromorphic normal determinant frame
\(Z^aV^2/x^{2j+1}\). Replacing \(x\) by \(v\)
adds only the displayed integral power of \(T\),
whose divisor is a whole fibre and whose product
with every vertical degree-zero divisor is zero.
The retained frame has periodic divisor coefficient
\[
                   d_j=(2j+1)r-2V-aZ.                     \tag{SZ.79}
 \]
It is unchanged under the actual \(h\) shift,
including its V component. This fixes the line
extension used in this local computation.

Order the primitive star rays by \(Z/s\) modulo
two. Adjacent determinants are \(-1\), with
the closing ray translated by the length-two
period. The central rational curve associated
to a ray has self-intersection
\(\det(v_{\rm prev},v_{\rm next})\). Adjacent
curves meet once; for a two-curve cycle they
meet at both nodes, so the off-diagonal
intersection is two. The fibre multiplicities
are the ray heights \(s_i\), and their vector
is in the kernel of the resulting intersection
matrix. These are the literal toric divisor
intersection maps in the star quotient.

The executed E stars in both regular fans have
exactly two height-one rays per component.
Their matrix and determinant-normal divisor are
\[
       \begin{pmatrix}-2&2\\2&-2\end{pmatrix},
                  \qquad(d_j,d'_j)=(0,0).                 \tag{SZ.80}
 \]
In particular no extra source-surface blowup
was introduced in these E stars, although the
ambient fourfold resolution has many other
exceptional components.

The relative tangent marking in this calculation
is the actual Tate invariant form
\(d\log Z\wedge dT\). On a star ray of height
\(s_i\) its canonical divisor coefficient is
\(s_i-1\): the logarithmic two-form has a simple
pole at each toric divisor, and multiplication
by \(T\) adds \(s_i\). Its coefficient is
therefore zero in (SZ.80). The Euler number of
the two rational components with their two
nodes is two. Equivalently, the invariant
source tangent field has one local Lefschetz
zero at each node and no zero on the
punctured Tate annulus. With this retained
boundary tangent marking the relative
Pontryagin value is
\[
       c_1^2-2c_2=-4.
 \]
Together with the determinant-normal
trivialization (SZ.79), the local version
of (SZ.59) is \(-1/6\) per E component.
The sums in the two executed fans are
\(-1\) for \(N=6\) and \(-4/3\) for \(N=8\).

Every ray, its unwrapping period, the cyclic
intersection matrix, multiplicity vector,
canonical divisor and determinant-normal
divisor is exported by
\(\texttt{source\_zero\_e\_cycles.py}\).
This is a local relative marking. In
particular the trivialization in (SZ.79)
has not been transported through the cap
component permutation of Section 27. It
does not identify a compact E fixed
surface or assign its global index.

## 29. The exact failed contraction in the unscaled H atlas

For the alternative with the original scalar fixed,
\(N=0\), the H period matrix has rank one. In the
good branch its primitive kernel is \(gh^{-1}\).
The exact exceptional-base units of (SZ.62) give
\[
       Z\longmapsto wZ,\qquad
       V\longmapsto-2\lambda w^{-1}V.
 \]
The transverse character is \(Y=ZV^2\), and the
actual residual multiplier is
\[
                         Y\longmapsto
                         4\lambda^2w^{-1}Y.              \tag{SZ.81}
 \]
In the reduced branch the primitive kernel is
\(g^2h^{-1}\), and the transverse character is
\(Y=ZV\). Direct substitution gives the same
multiplier (SZ.81). These formulas retain
the constants \(u_Q(0)=1/256,u_P(0)=16\) and
\(u_X(0)=-1/4\); their ratios are exactly the
displayed constants.

As \(w\) ranges over the exceptional base,
the magnitude of (SZ.81) passes through one.
Thus this literal rank-one H atlas has no
uniform contracting quotient over that whole
base. At a value with unit-modulus multiplier
which is not a root of unity, its iterates
accumulate on the transverse circle, so
the action is not properly discontinuous
there. This proves the failure of this
particular unscaled quotient construction.
It does not assign a return from the
crossing, or obstruct a real orbit
bordism retaining its exact multiplier.
