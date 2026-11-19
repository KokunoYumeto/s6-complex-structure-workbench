# Marked infinity source, Cartier line, caps, and collision periods

This working note records actual maps for the infinity puncture of the marked
source cover. The completed IF.1--12 maps and the relative regularization in
IF.8a have passed root audit. The matching real circle-quotient excision and
actual return transfer are proved in the companion
`notes/part3_source_infinity_excision_working.md`, IE.1--7, also root-audited.
The combined result is reserved for K57 after checkpoint14; this file remains
working proof material until that full export. The calculations retain the
source, divisor lines, and primitive chord lift fixed in K39's working note.

Initial scope, retained as attempt history: this note originally assigned no
completed-family return, and the collision quotient, cap/selected attachment
and oriented boundary were separate remaining maps. Statements of that local
scope in the earlier sections are completed by IF.8--12 and IE.1--7; no
source-zero collision return is supplied by this update.

## IF.1. The marked infinity chart and selected-node units

On the cover \(\rho^2=1+v\), put \(\epsilon=\rho^{-1}\). The source map is
\[
 v=\epsilon^{-2}-1,\qquad
 X=\epsilon^{-2}x,\quad Y=\epsilon^{-3}y,\quad T=\epsilon^{-4}t.
\]
It carries the actual marked equation and section to
\[
 y^2=x^3+(-2+3\epsilon^2)x^2+t x
                     +\epsilon^2(1-\epsilon^2)^2,\qquad
 G=(0,g),\quad g=\epsilon(1-\epsilon^2).                 \tag{IF.1}
\]
Write \(A=1-\epsilon^2\), \(t_*=A(1-3\epsilon^2)\), and \(q_*=t-t_*\).
The selected fibre factors and normalizes by the literal formulas
\[
 (x-A)^2(x+\epsilon^2),\qquad
 x=s^2-\epsilon^2,\quad y=s(s^2-1).                     \tag{IF.2}
\]
Its double preimages are \(s=\pm1\), independent of the parameter. The marked
section has \(s=-\epsilon\). The normalization derivative has first coordinate
\(2s\); at \(s=0\) its second coordinate is \(-1\). It is therefore an immersion
through the full parameter disc, with its two double sections disjoint.

Choose the nodal multiplicative coordinate \(Z=(s-1)/(s+1)\). Its marked point
is
\[
 P_G=-\frac{1+\epsilon}{1-\epsilon},\qquad
 P_G(-\epsilon)=P_G(\epsilon)^{-1}.                    \tag{IF.3}
\]
The selected Tate parameter satisfies
\[
 \left.\frac{Q}{q_*}\right|_{q_*=0}
       =-\frac{1-\epsilon^2}{64}.                       \tag{IF.4}
\]
Indeed the cubic discriminant has \(t\)-derivative \(-4A\) at \(t_*\), its
elliptic discriminant is sixteen times that cubic discriminant, and \(c_4=16\)
there. The first term of \(j(Q)^{-1}\) is \(Q\), which gives (IF.4).

Retain the actual two chord factors
\[
 F_{21}=\frac{y+g+t x/(2g)}x,\qquad
 F_{12}=\frac{y-g-t x/(2g)}x .
\]
At the selected node they are \(A/(2\epsilon)\) and
\(-A/(2\epsilon)\). The transported actual Hom map is
\[
 \phi_{ab}=\frac{q_*}{g F_{ab}},\qquad
 \left.\frac{\phi_{21}}{q_*}\right|_{\rm node}=\frac2{A^2},
 \quad
 \left.\frac{\phi_{12}}{q_*}\right|_{\rm node}=-\frac2{A^2}.       \tag{IF.5}
\]
All three units (IF.3)--(IF.5) extend and are nonzero on a sufficiently small
full \(\epsilon\)-disc. Their full-disc parameter windings are zero. This is
an actual selected-cusp chart statement; it does not trivialize the exterior
suspension at the other singular fibres.

## IF.2. The complete suspension keeps the scalar

Use the canonical meromorphic divisor sections to identify the old Cartier
line with the line of (IF.1). Translation by \(G\) commutes with the displayed
source isomorphism. The primitive chord lift \(U_a\), covering \(-G\), has
target multiplier \(X(p-G)^{-a}\); consequently
\[
 I_\epsilon U_{a,\rm old}I_\epsilon^{-1}
       =\epsilon^{2a}U_{a,\rm new},\qquad
 q_{\rm old}=\epsilon^{-4}q_* .                         \tag{IF.6}
\]
The actual suspension is
\[
 B_{a,b}=2(-1)^{b+1}\lambda q_{\rm old}U_{a,\rm old}^{\,b},
 \qquad ab=2 .
\]
Thus its transported map is exactly
\[
 I_\epsilon B_{a,b}I_\epsilon^{-1}
       =2(-1)^{b+1}\lambda q_*U_{a,\rm new}^{\,b}.       \tag{IF.7}
\]
The exponent \(2ab-4\) is zero. In degree two the Cartier multiplier has the
same scalar factor at source and target; these factors cancel in the
conjugation as well. Therefore \(\lambda_{\rm new}=\lambda_{\rm old}\).

An earlier proposed \(\epsilon^4\) change counted only the \(U_a\) factor.
Equation (IF.6) locates its omitted \(q\) factor and (IF.7) corrects that
attempt. No scalar convention is changed.

## IF.3. The finite root comparison retains its endpoint and lattice period

Let the old cap use \(z_{\rm old}^m=T^{-1}\), and the new cap use
\(z_{\rm new}^m=t^{-1}\). On the universal \(\epsilon\)-cover the literal arrow is
\[
 z_{\rm old}=\epsilon^{4/m}z_{\rm new}.                 \tag{IF.8}
\]
The admitted branches are the existing good III-star root
\((a,b,m)=(1,2,4p)\), and reduced III root
\((a,b,m)=(2,1,4p-1)\), with their actual norm sign \(n=\pm1\).
The comparison of minimal-root coordinates is
\[
 \begin{array}{c|cc}
  m&X'_{\rm new}&Y'_{\rm new}\\ \hline
 4p&x'_{\rm old}&y'_{\rm old}\\
 4p-1&\epsilon^{-2/m}x'_{\rm old}&\epsilon^{-3/m}y'_{\rm old}.
 \end{array}                                           \tag{IF.9}
\]
This follows directly by writing \(X'=z_{\rm new}^{2p}x\) and
\(Y'=z_{\rm new}^{3p}y\) and substituting (IF.8). A full positive
\(\epsilon\)-turn has endpoint \(D_{\rm new}^{-4}\). In the reduced case its
factors on \((z_{\rm new},X',Y')\) are
\((\zeta_m^{-4},\zeta_m^{-2},\zeta_m^{-3})\), since \(4p=m+1\).
In the good case the last two factors are one.

The reduced branch retains the actual central nonidentity division section.
On the transported square good-root lattice its chosen logarithm tends to
\((1+i)/2\), and
\[
                   4\log R-\log(4R)=2(1+i).             \tag{IF.10}
\]
The second logarithm is the small identity logarithm. Equation (IF.10)
remains a lattice term in the annular affine cochain. It is not replaced by
zero or multiplied by \(\log\epsilon\) with an assertion of central
holomorphic extension.

The actual full reference overlap is fixed by transporting the prescribed
old ordinary-to-cap overlap at one nonzero parameter, including its integral
delta term and finite line character. The K49 relative source/Hom atlas
comparison then continues that full cocycle on the cap annulus. Its finite
averaging retains the central character and its Cauchy splitting retains the
annular integer. These maps identify the two punctured parameter families.
They do not yet attach a central collision model.

## IF.4. Half-loop endpoint at the selected cusp

The source equation is even in \(\epsilon\), while \(G\) changes sign. Its
actual endpoint isomorphism is
\[
                  \iota(x,y)=(x,-y).                    \tag{IF.11}
\]
For \(\Theta(QZ)=-Z^{-1}\Theta(Z)\) and
\(\Theta(Z^{-1})=-Z^{-1}\Theta(Z)\), write
\(f_P(Z)=\Theta(Z/P)/\Theta(Z)\). The exact identity
\[
 f_{P^{-a}}(Z^{-1})=P^a f_{P^a}(Z)
\]
gives the selected-cusp line map
\[
                  (Z,V)\longmapsto(Z^{-1},P^a V).       \tag{IF.12}
\]
Here \(P\) is a bounded unit and \(P(-\epsilon)=P^{-1}\). This map squares
to the identity. It sends \(h\) to \(h_{\rm target}^{-1}\), \(g\) to
\(g_{\rm target}\), and preserves the physical delta circle.
Its selected-cusp valuation map is \(\operatorname{diag}(-1,1)\); it sends
the two specified diagonal fans to one another by that actual map.

The cap endpoint of a half \(\epsilon\)-turn is
\(\iota D_{\rm new}^{-2}\). In the reduced case its literal factors from
(IF.9) are \(\zeta_m^{-1}\) on \(X'\) and
\(\exp(-3\pi i/m)\) on \(Y'\); the latter includes the \(y\)-sign of
\(\iota\). Thus the source inversion and cap root rotation are both retained.
The full \(\epsilon\)-turn closes the selected source reflection twice.
In the global rho marking the same arrow is
\(\mathcal R_\rho(Z,V)=(Q/Z,V)\). This is literally
\(h_{\rm target}\circ\mathcal I_\epsilon\), because the target
source period is \((Q,P^{-a})\). Thus the integral height
translation and the factor \(P^a\) in (IF.12) are carried by an
actual period map; neither is dropped from a six-chart closing.

The root coordinate used in the other infinity chart is
\(\zeta=\epsilon/\sqrt{1-\epsilon^2}\), with the square root equal to one
at zero. The ratio is a nonzero unit and has zero winding. A positive
\(\epsilon\)-turn covers a negative double \(v\)-turn. The original
\(u^3=v\) endpoint is further discrete data; it is not closed by
discarding this covering degree.

## IF.5. The unselected collision and its actual period orders

At \(\epsilon=0\) the cubic discriminant is \(4t^2(1-t)\). The selected
simple zero remains at \(t=1\); the unselected pair meets at \(t=0\).
The exact other two critical values are the analytic branches
\[
 t_\pm=\frac{\epsilon}{8}
 \left\{\epsilon(4-3\epsilon^2)
          \pm\sqrt{(9\epsilon^2-8)^3}\right\}.           \tag{IF.13}
\]
Choose the square root and the labels once. They have distinct first
derivatives \(\pm2i\sqrt2\) and are exchanged by \(\epsilon\mapsto-\epsilon\).
Set \(q_A=t-t_+\), \(q_B=t-t_-\), with the choice agreeing with the marked
sectional small resolution. In its retained theta/Cartier gauge,
\[
 Q=q_Aq_Bu_Q,\qquad P=q_B^{-1}u_P,\qquad
 c_X=q_Bu_X,                                           \tag{IF.14}
\]
where the units are retained as actual functions. The source and
Cartier derivation is the literal chord/theta calculation reproduced
in IF.5a through the unit Weierstrass coordinate map described below.
It retains the degree-two Cartier divisor and its central component.
The leading coefficients in the transported marking are
\[
               u_Q(0)=1/4096,\qquad u_P(0)=64,\qquad u_X(0)=1/8 .
\]

For completeness, a literal source map to the marked local model exists.
Choose either unit root \(\kappa\) of
\[
 \kappa^3-(-2+3\epsilon^2)\kappa-2\epsilon(1-\epsilon^2)
 =(\kappa-\epsilon)(\kappa^2+\epsilon\kappa+2-2\epsilon^2).
\]
Its central value is \(i\sqrt2\) or \(-i\sqrt2\).
Then \(x=\kappa^2 X_0\), \(y=\kappa^3Y_0\),
\(t=\kappa^4T_0\), \(v_0=g/\kappa^3\) sends (IF.1) to
\[
 Y_0^2=X_0^3+(1-2v_0)X_0^2+T_0X_0+v_0^2,\qquad G_0=(0,v_0).
\]
This map also carries the marked small resolution and the canonical
Cartier sections. The whole-zero site is carried to the other, distant
simple discriminant value. It is not changed to one of the colliding sites.
More explicitly, the two source heights are divided by \(\kappa^4\);
the earlier units \(u_Q^0,u_P^0,u_X^0\) become
\(\kappa^{-8}u_Q^0,\kappa^4u_P^0,\kappa^{-2}u_X^0\).
Their previous central values \(1/256,16,-1/4\), together with
\(\kappa^2=-2\), give the displayed constants. This also fixes the signs
of the two node labels by the chosen \(\kappa\) branch.

The actual periods for \(\lambda=\epsilon^N\lambda_0\) are
\[
 h=(Q,P^a),\qquad
 g=(P^{-b},\,2(-1)^{b+1}\lambda_0\epsilon^N q_*c_X^{-2}).
                                                               \tag{IF.15}
\]
Because \(q_*(0,0)=-1\), its collision order is zero. Their divisor matrices
at the two strict transforms, the parameter direction, and their sum are
\[
 P_A=\begin{pmatrix}1&0\\0&0\end{pmatrix},\quad
 P_B=\begin{pmatrix}1&b\\-a&-2\end{pmatrix},\quad
 E=\begin{pmatrix}0&0\\0&N\end{pmatrix},\quad
 H_\infty=\begin{pmatrix}2&b\\-a&N-2\end{pmatrix}.
                                                               \tag{IF.16}
\]
In particular \(\det H_\infty=2N-2\). These are period-order identities,
not a count of fixed strata, links, or characteristic numbers.

### IF.5a. Exact source, theta and Cartier derivation of the periods

We give the local derivation used in (IF.14)--(IF.15), so no
unpromoted source-zero construction is needed. Work first in the
unit source coordinates \((X_0,Y_0,T_0,v_0)\) just displayed and
write \(a_2=1-2v_0\). Its discriminant and \(c_4\) give
\[
 j^{-1}=\frac{a_2^2T_0^2-4T_0^3-4a_2^3v_0^2-27v_0^4
                         +18a_2T_0v_0^2}
                   {256(a_2^2-3T_0)^3}.                 \tag{IF.16a}
\]
The convergent inverse of the \(j\)-series therefore gives
\(Q=q_1q_2u_Q^0\), with \(u_Q^0(0)=1/256\), on a
smaller two-node polydisc. Here \(q_1,q_2\) are its two
actual discriminant heights, with the chosen small-resolution
label. All the following unit logarithms are fixed on that
full polydisc.

The node map is explicit. Put
\[
 x_c=\frac{-a_2+\sqrt{a_2^2-3T_0}}3,\qquad
 R=(X_0-x_c)\sqrt{a_2+3x_c+X_0-x_c},
\]
using the square roots tending to one. If
\(f(X)=X^3+a_2X^2+T_0X+v_0^2\), then
\(f(X_0)=f(x_c)+R^2\). Thus
\((Y_0-R)(Y_0+R)=f(x_c)\), with
\(f(x_c)=q_1q_2\upsilon\), \(\upsilon(0)=-1/4\).
Dividing one factor by this actual unit gives the literal
node equation \(AB=q_1q_2\). The derivative in \(X_0\)
of \(R\) at the origin is one, so the displayed map is
invertible by the holomorphic inverse theorem.

The convergent Tate sums extend over their node chart
\(Q=Z_0W_0\), with leading terms
\(x_T=Z_0+W_0+\cdots\),
\(y_T=-W_0+\cdots\). Rewriting negative-index terms in
\(W_0\) and \(Q\), and positive-index terms in \(Z_0\)
and \(Q\), proves normal convergence there. After the
specified \(c_4\)-root scaling and Weierstrass translation,
this is the invertible node map above. The actual section
\(G_0=(0,v_0)\) has node factors with linear terms
\(v_0+T_0/2\) and \(v_0-T_0/2\). Its two Tate
coordinates therefore vanish simply on opposite
discriminant branches. Analytic division gives
\[
 Z_0(G_0)=q_1u_G,\quad W_0(G_0)=q_2u'_G,\qquad
 P=Z_0(G_0)/Q=q_2^{-1}u_P^0.                         \tag{IF.16b}
\]
The selected nodal normalization gives the exact value
\(P=(1+\sqrt{1+v_0})/(1-\sqrt{1+v_0})\) on
\(q_1=0\). Since \(q_2=-4v_0+O(v_0^2)\) there,
\(u_P^0(0)=16\). This selects the actual period lift
of the section, including its integral reindexing.

Write \(f_P(Z)=\Theta(Z/P)/\Theta(Z)\). Its divisor
and exact multiplier \(f_P(QZ)=P f_P(Z)\) identify
it with the canonical meromorphic section of the
actual degree-zero line. The source function \(X_0\)
has divisor \([G_0]+[-G_0]-2[O]\), and consequently
\[
 X_0(Z)=c_X^0 f_P(Z)f_{P^{-1}}(Z),\qquad
                     c_X^0=q_2u_X^0.                   \tag{IF.16c}
\]
The coefficient is fixed by evaluating at the ordinary
Tate point \(Z=-1\). The theta shift identity shows
that \(q_2f_P(-1)f_{P^{-1}}(-1)\) is a nonzero
holomorphic unit; so is the actual \(X_0(-1)\).
At the central nodal cubic the retained coordinate
is \(X_0=4Z/(1-Z)^2\), hence \(c_X^0\sim-4/P\)
and \(u_X^0(0)=-1/4\). The unit map by \(\kappa\)
then gives exactly the three constants and functions
in (IF.14).

The primitive source lift covering \(-G\) has target
Cartier multiplier \(X(p-G)^{-1}\). The identity
\(f_P(Z)f_{P^{-1}}(Z/P)=1\) cancels every
\(Z\)-dependent factor in its source and target
Cartier coefficients. On the tensor-power line the
literal resulting map is
\[
          U_a:(Z,V)\longmapsto(P^{-1}Z,c_X^{-a}V).
                                                               \tag{IF.16d}
\]
For \(a=2\), retain the actual Cartier comparison
before using that tensor-power coordinate. With
\(F_2=1-Bz^3-(1-2v_0)z^2\) in the small-resolution
chart of IE.3, the addition formula gives
\[
 r(p)=X_0(p-G_0)=\frac{2v_0F_{21}(p)}{X_0(p)}
                         =\frac{F_2}{z^2}.             \tag{IF.16e}
\]
Its divisor is \([2G_0]+[O]-2[G_0]\). Multiplication
by \(r\) is therefore the actual map
\(\mathcal O([2G_0]-[O])\to
\mathcal O([G_0]-[O])^{\otimes2}\). The last
expression retains its central component and has no
extra factor of \(v_0\). In these unit coordinates the
actual selected height is \(q_0=\kappa^{-4}q_*\).
At \(p'=p-G_0\),
\(F_{21}(p')=r(p')r(p)/(2v_0)\), so its conjugation
of the suspension is the exact identity
\[
 \frac{r(p')}{r(p)}\frac{\lambda q_0}{v_0F_{21}(p')}
                   =\frac{2\lambda q_0}{X_0(p')^2}.
                                                               \tag{IF.16f}
\]
The scalar unit source change is carried on both sides.
This proves (IF.15) for the actual degree-two divisor
line, as well as the degree-one line. It does not
replace that Cartier line by its generic Picard class.

## IF.6. The half-loop Cartier arrow through the collision

The representative \(P\sim q_B^{-1}\) in (IF.14) requires a different
integral Tate reindexing after the two branches are exchanged. The actual
target representative is
\[
                       P'=(QP)^{-1}.                   \tag{IF.17}
\]
It represents \(-G\), has the required \(q_A^{-1}\) leading order, and
retains the integral period omitted by the bounded selected-cusp expression.
Applying the theta shift identity \(a\) times gives
\[
 f_{(P')^a}(Z^{-1})
   =c_a Z^a f_{P^a}(Z),\qquad
 c_a=(-1)^aQ^{-a(a-1)/2}P^{a(1-a)}.                    \tag{IF.18}
\]
Thus the actual collision line map is
\[
              \mathcal I(Z,V)=(Z^{-1},c_a Z^aV).        \tag{IF.19}
\]
It preserves delta and squares literally to the identity:
\(c_a(P)c_a(P')=1\).
Applying the same two theta identities to the divisor of \(x\) gives
\[
                   c_X'=(QP^2)c_X .                    \tag{IF.20}
\]
Consequently the complete source and suspension periods satisfy
\[
 \mathcal I h=h'^{-1}\mathcal I,\qquad
 \mathcal I g=h'^{-b}g'\mathcal I.                      \tag{IF.21}
\]
For the second equality, its source coordinate has factor
\(P^b=Q^{-b}(P')^{-b}\). Its line coordinate has factor
\(P^{-ab}g_V=(P')^{-ab}(QP^2)^{-2}g_V\), since \(ab=2\).
This proves the full line equality including the scalar, rather than only
the generic Picard-point equality.

Let \(c=a(a-1)/2\). In the ordered valuation lattice
\((Z,V,q_A,q_B)\), (IF.19) and the branch exchange give
\[
 S=\begin{pmatrix}
 -1&0&0&0\\ a&1&-c&c\\0&0&0&1\\0&0&1&0
 \end{pmatrix},\qquad S^2=1,\qquad S\delta=\delta.       \tag{IF.22}
\]
Its fibre block and period relabelling are
\[
 J=\begin{pmatrix}-1&0\\a&1\end{pmatrix},\qquad
 R=\begin{pmatrix}-1&-b\\0&1\end{pmatrix}.
\]
The exact identities
\[
 JP_A=P_BR,\quad JP_B=P_AR,\quad JE=ER,\quad
 JH_\infty=H_\infty R                                  \tag{IF.23}
\]
prove compatibility with every retained period order. The nonconstant
unit factors in \(c_a\) stay in (IF.18); (IF.22) records only their divisors.
Equations (IF.18)--(IF.21) are the actual morphism relating the
selected-cusp and collision half-loop descriptions.

## IF.7. Remaining attachment and executed scope

The scalar origin on the ordinary source uses \(\log q_*\). Near the
unselected collision \(q_*\) is a nonzero unit on the full bidisc, so this
logarithm is single valued there. Its \(q_A\) and \(q_B\) continuations do
not insert the extra \(v^{-nk}\) deck found at the selected source-zero
collision. Its parameter endpoint is the extending unit \(q_*^{nk}\).
The finite cap still carries its full norm generator and root arrow
(IF.8)--(IF.10).

This removes that particular local annular-deck mismatch. It does not
construct a compact global bordism: the rank-one faces of (IF.16) need
their actual quotient atlas, the finite-cap attachment must be written,
and the separate selected I1 scalar trace must be joined with its physical
Euler line and oriented boundary. Fixed \(\lambda\) is not asserted to
give uniform contraction through \(\epsilon=0\).

The executed script
\(\texttt{code/part3\_fourfold/source\_infinity\_exact.py}\) checks the
source equations, discriminant branches, selected units, full scalar
cancellation, all root-coordinate exponents, and the complete half-loop
source/line/period identities. Its JSON retains the explicit cap rows
and has global-bordism and return fields false.

## IF.8. Literal rank-one sector fans and protected boundary chains

All three lower matrices in (IF.16) have rank one. The following is an
actual construction of their cone collections. It is kept in the original
integer lattice, with the physical cocharacter \(\delta=(0,1,0,0)\).
For \(P_0=P_A,P_B,E\), put
\[
 R_0(n)=(P_0n,1,0),\quad R_1(n)=(H_\infty n,0,1),\qquad
 T_j(x,r,s)=(x+(rP_0+sH_\infty)j,r,s).                 \tag{IF.24}
\]
Use the basis \(u=e_1,v=-e_2\) on A, the basis
\(u=e_1,v=e_2-be_1\) on B, and \(u=-e_2,v=e_1\) on E.
In each case \(P_0v=0\). Start with the two labelled
triangles \((0,u,u+v)\), \((0,v,u+v)\). The three
nondegenerate maximal cones in one prism cell are
\[
 \begin{split}
 &\operatorname{cone}(R_0(0),R_1(0),R_1(u),R_1(u+v)),\\
 &\operatorname{cone}(R_0(0),R_1(0),R_1(v),R_1(u+v)),\\
 &\operatorname{cone}(R_0(0),R_0(u),R_1(u),R_1(u+v)).
 \end{split}                                             \tag{IF.24a}
\]
Take all their literal \(T_j\)-translates. The other
three tetrahedra of the two triangular prisms collapse
to the lower-dimensional faces identified below.
In each case \(P_0v=0\). Start with the two triangles
\((0,u,u+v),(0,v,u+v)\) and their three usual staircase tetrahedra
between the \(R_0\) and \(R_1\) copies. Omit their collapsed
four-dimensional cones and retain every ordinary face.

Here is a direct common-face and support proof. Set
\(p=P_0u,\ A_1=H_\infty u,\ B_1=H_\infty v\).
The rational inspection map with basis \((A_1,B_1)\) sends \(p\) to
\((c,d)\), with
\[
 \begin{array}{c|cc}
 &c&d\\ \hline
 A&(N-2)/(2N-2)&-a/(2N-2)\\
 B&(N-2)/(2N-2)&-a/(2N-2)\\
 E&N/(N-1)&bN/(2N-2).
 \end{array}                                           \tag{IF.25}
\]
Every \(c\) is positive for the admitted \(N>2\). At fixed \(r,s>0\)
the two top cones give the square \([0,s]^2\), split along its
diagonal. The third surviving cone gives
\[
          (s,0)+[0,r](c,d)+[0,s](0,1).
\]
Their union is the strip
\[
 0\le x\le L=s+rc,\qquad f(x)\le y\le f(x)+s,\quad
 f(x)=0\ (x\le s),\quad f(x)=(d/c)(x-s)\ (x\ge s).
\]
The actual period vectors are \((L,rd)\) and \((0,s)\).
Reducing \(x\) uniquely modulo \(L\), then reducing
\(y-i rd-f(x-iL)\) uniquely modulo \(s\), assigns every point
off a boundary to exactly one of these strip cells.
The square and parallelogram share their entire vertical edge;
the far edge is the next square's near edge; and the upper
piecewise linear boundary is the lower one translated by \((0,s)\).
Thus all intersections are full common faces. The two collapsed
bottom tetrahedra have the already existing face
\(\operatorname{cone}(R_0(0),R_0(u),R_1(u+v))\), and the collapsed
mixed tetrahedron has
\(\operatorname{cone}(R_0(0),R_1(v),R_1(u+v))\).
No image of a collapsed cone is omitted from the face complex.
This proves the fan and support statements with the exact translations
(IF.24), including the rank-one height boundary.

On the H boundary the A and E constructions give the negative
unit-square triangulation in \(H_\infty^{-1}\) coordinates; B gives
the shear with basis \((e_1,e_2-be_1)\). Their literal polygonal
overlay is a common rational periodic refinement. Intersections
are common faces because their supporting equalities are those of
the two original complexes. It has finitely many cells modulo
\(\mathbb Z^2\). All rays are then replaced by their primitive
integer vectors on the same ray, preserving their true heights.
For \(b=2\) the added H-edge midpoint ray is the primitive multiple
of \((2,N-2,0,2)\).

The A boundary retains every primitive ray \((j,0,1,0)\); the B
boundary retains \((j,-aj,1,0)\). They are exactly the actual source
line chains: on B the literal coordinate \(Y=Z^aV\) has no vanishing
line character along that lower face. The E boundary retains all
primitive rays \((0,j,1,0)\), not only the raw step-\(N\) rays.
Its adjacent coordinates are
\[
       X_j=V\xi_E^{-j},\quad Y_j=\xi_E^{j+1}/V,\qquad
                       X_jY_j=\xi_E .                    \tag{IF.26}
\]
The actual scalar period shifts \(j\) by \(N\), retaining its
nonzero multiplier in the two chart maps.

Extend these boundary refinements by coning already subdivided
faces from their primitive ray sum, face by face in increasing
dimension. This gives common faces and commutes with every
unimodular map (IF.24). The relative regularization then uses a
nonzero lattice point in each singular cone's half-open
parallelepiped, subdividing all occurrences of its minimal face
simultaneously. The incident determinants strictly decrease;
the relative separator prevents two translates of that centre
in one cone. The protected boundary faces are already regular
and hence never contain a resolution centre.

The executable \(\texttt{source\_infinity\_regular\_fan.py}\) is a
separate saved adaptation of the earlier complete algorithm.
Its derivation file records every changed matrix, rank-one
canonical representative, stabilizer and protected-face dimension.
It exports every actual primitive ray, determinant-one cone,
period, face permutation and higher parameter order. Its legacy
tags I,W,E mean the present A,B,E faces; they do not identify A
with the earlier full-rank I face.

### IF.8a. Relative separator and terminating integral resolution

Here is the complete relative regularization argument for the
present infinity matrices. Protect all the actual A, B and E
lower-face chains listed above. The adjacent primitive rays
have a unit two-dimensional minor; their span lattices are
saturated, with equations respectively \(V=0\),
\(V=-aZ\), and \(Z=0\). Hence every protected cone is
regular in its actual lattice. In each sector the protected
subfan is exactly its lower face \(s=0\). A nonprotected
ray has positive H height. Its period stabilizer is zero:
\[
 \begin{aligned}
 \det(rP_A+sH_\infty)&=\det(rP_B+sH_\infty)\\
                    &=(N-2)rs+(2N-2)s^2,\\
 \det(rE+sH_\infty)&=2Nrs+(2N-2)s^2.
 \end{aligned}                                         \tag{IF.26a}
\]
Both are positive for \(r\ge0,s>0,N>2\). Thus
\(T_\nu(x,r,s)=(x,r,s)\) on such a ray implies
\(\nu=0\). The lower-face kernel stabilizers fix those
faces pointwise; their actual analytic unit actions are
retained in IF.9 and are not replaced by identity maps.

First take the relative barycentric subdivision outside
the protected subfan. Process old faces in increasing
dimension, insert the primitive ray on the sum of their
primitive generators, and cone the already subdivided
boundary from that ray. A convex transverse section gives
the literal radial coverage and common-face map. The
same choices are made on the common H faces in all three
sectors. Every period map is unimodular, preserves face
dimension, and takes a generator sum to the corresponding
generator sum; hence this subdivision is exactly equivariant.

Each resulting cone consists of a protected face and a
strictly increasing chain of nonprotected old faces. It
therefore contains at most one ray in any nonprotected
period orbit: two rays in an orbit would arise from old
faces of the same dimension, whereas a strict face chain
contains only one of that dimension. An inserted ray is
interior to its named face, so equality of rays also gives
equality of their named faces. Every singular face contains
a nonprotected ray, because a cone generated entirely by
protected rays is a face of one of the regular protected
cones. Two distinct period translates of a singular face
cannot lie in one cone: their nonprotected rays would
violate this orbit separation, and the ray stabilizer is
trivial by (IF.26a).

For a singular maximal cone let \(B\) be its primitive
column matrix and \(D=|\det B|>1\). Some column
\(B^{-1}e_j\) is nonintegral, since otherwise \(B^{-1}\)
would be integral and its determinant would force \(D=1\).
Take its coordinatewise fractional part \(\alpha\) and set
\[
 p=B\alpha=e_j-B\lfloor B^{-1}e_j\rfloor,
 \qquad 0\le\alpha_i<1.                              \tag{IF.26b}
\]
This is a nonzero integral point. Divide \(p\) and every
\(\alpha_i\) by the positive gcd of its coordinates, so
\(p\) is primitive and the same strict inequalities hold.
Its minimal face \(F\), generated by the rays with
\(\alpha_i>0\), is singular. Indeed on a regular face
an integral vector with all these coefficients in
\([0,1)\) is zero in the saturated span lattice, which
contradicts \(p\ne0\). Thus \(F\) is outside the
protected subfan and has trivial period stabilizer.

Insert \(T_\nu p\) simultaneously on every translated
face \(T_\nu F\). Orbit separation proves that no old
cone receives two distinct centres from this orbit.
For a point \(x=\sum t_i r_i\) of a containing cone,
subtract \(\tau p\), where
\(\tau=\min_{\alpha_i>0}t_i/\alpha_i\). The remaining
coefficients are nonnegative and at least one is zero,
which gives precisely a cone of the star subdivision.
Ties are precisely the shared faces; the same formula
on an old shared face proves compatibility. For each
affected maximal cone and each replaced ray,
\[
                        D_{
m new}=\alpha_i D_{
m old},
                 \qquad 0<\alpha_i<1.                  \tag{IF.26c}
\]
These are positive integers. Every affected determinant
strictly decreases, and no protected cone is subdivided.

Orbit separation survives the star: a new cone lies in
an old cone and contains at most one new ray of the chosen
orbit. This new orbit was not an old ray orbit, since its
point was interior to a face of dimension at least two.
Its positive H height gives trivial stabilizer again.
There are initially finitely many cone orbits, and every
star introduces finitely many new ones. At each stage
choose a maximal-determinant cone orbit. The pair
\((D_{\max},\#\{\text{maximal orbits of determinant }D_{\max}\})\)
strictly decreases lexicographically: no new orbit has
the old maximal determinant. There are finitely many
stages at each first entry and finitely many decreases
of that entry. Hence the process terminates with every
maximal determinant one. If the centre lies on H, perform
the identical star in all incident sectors; formula
(IF.26c) applies to each. This proves a compatible
period-equivariant regular refinement relative to all
three actual chains, in the original integral lattice,
with every higher parameter height retained.

## IF.9. Exact face kernels and the remaining real attachment

Put \(C=2(-1)^{b+1}\lambda_0\). On the A face the kernel period is
\(g\). Its transverse line coordinate is \(V\), and its multiplier is
\[
                  C\epsilon^N q_*q_B^{-2}u_X^{-2}.       \tag{IF.27}
\]
On the B face the kernel is \(k=g h^{-b}\). Its source multiplier
and its multiplier on the literal transverse coordinate \(Y=Z^aV\)
are
\[
 (q_Au_Qu_P)^{-b},\qquad
          C\epsilon^N q_*q_A^{-2}u_Q^{-2}u_P^{-4}u_X^{-2}.       \tag{IF.28}
\]
These equalities follow directly from (IF.15): the second line is
\(g_V/(QP^2)^2\). Since the two critical values differ by
\(\epsilon\) times a nonzero unit, both raw transverse kernel
multipliers have order \(N-2\) at their corresponding strict face.
All constants and source multipliers remain in (IF.27)--(IF.28).
They are not replaced by a formal valuation.

Audit correction, 2026-11-17 after checkpoint14: the previous
sentence called these raw order-\(N-2\) multipliers
``contractions'' without yet including the nodal line metric
and the source reindexing. That wording and the earlier short
norm-shell argument remain preserved in immutable checkpoint14.
The actual operator estimate below includes the losses three
and four, respectively. The proof uses \(N=8\) and \(N=6\),
so its two executed geometric comparisons remain within that
estimate; the smaller fan computations supply arithmetic only.

At E the source period \(h\) retains the actual compact elliptic
source fibre and its line holonomy. The scalar period has order \(N\)
and acts on the primitive chain (IF.26). Near H, both previously
kernel directions have nonzero image under the full-rank matrix
\(H_\infty\). Thus the period separation in the full-rank cones
controls the closures of both face norm shells; no additional
kernel is lost at that overlap.

Here is the complete analytic quotient argument, including the
norm bound for the actual nodal lines. The analytic charts are
the affine semigroup charts of the regular fan, pulled back by
the stated base-blowup maps. The full period indexed by
\(\nu\in\mathbb Z^2\) has lattice map \(T_\nu\) from
(IF.24), followed by the actual extending base units from
(IF.15). Multiplication by these units acts on every character
by its literal integer powers, and therefore extends to the
corresponding semigroup chart. The units form a homomorphism
in \(\nu\), since they are products of the two commuting
periods. This proves the group law, its inverse, and the
common-H overlap law on the analytic atlas.

For a nonzero base value, let \(r,s\) be the positive logarithmic
radii of the two sector coordinates. The full real matrix of
the logarithmic magnitudes of its two actual periods is
\[
                       L=-rP_0-sH_\infty+C,             \tag{IF.28a}
\]
where \(C\) is bounded; the fixed \(\lambda_0\) belongs
to that bound. By (IF.26a) the determinant of the leading
matrix is bounded below by a positive multiple of
\(s(r+s)\), and its norm is bounded above by a multiple
of \(r+s\). Its least singular value is therefore at
least a positive multiple of \(s\). Shrinking the corner
polydisc makes the bounded perturbation harmless. Use the
actual parallelogram \(L([0,1]^2)\), with its compact
angular torus. It differs from the leading parallelogram
by a uniformly bounded set.

The strip construction in IF.8 places that set in finitely
many adjacent chart types, uniformly in \(r/s\). Indeed
its width is \(s+rc\), its height is \(s\), and its
periods are \((s+rc,rd)\), \((0,s)\). Compare the
linear function \(rd\,x/(s+rc)\) with the two pieces
of \(f(x)\). Their difference divided by \(s\) is
bounded uniformly, so only a bounded number of vertical
translates is required. A bounded perturbation changes
both assigned strip integers by a bounded amount.
Consequently one fixed finite collection of adjacent
cone charts covers the quotient. Its monomial coordinate
magnitudes are uniformly bounded above and its angles
lie in compact tori. Closing those regions, including
their toric faces, gives compact chart sets over a
closed smaller base polydisc. Away from the three
marked H points the same argument uses the full-rank
matrix \(H_\infty\) alone.

At the strict B face, restrict to
\(|q_B|\le\eta|q_A|\), with a fixed small \(\eta\).
Then \(|\epsilon|\) is comparable with \(|q_A|\).
The nodal line in the character \(Y=Z^aV\) has source
period multiplier \(c=(QP)^a=(q_Au_Qu_P)^a\).
On \(|Q|\le|Z|\le1\), interpolate a positive metric
between its two actual endpoint values. Its ratio is
bounded by \(C|q_A|^{-a}\). The same interpolation on
the plumbing annuli extends to the nodal normalization
with the prescribed gluing at both node preimages.
The source multiplier of the kernel is bounded by
\(C|q_A|^{-b}\). Reindexing its image to the Tate
fundamental annulus uses at most two source periods
for \((a,b)=(1,2)\), and at most one for \((2,1)\).
Each period changes the line norm by at most
\(C|q_A|^{-a}\). Combining these bounds with the
raw multiplier of order \(N-2\) gives
\[
 \|k\|\le
 \begin{cases}
 C|\lambda_0|\,|\epsilon|^{N-5},&(a,b)=(1,2),\\
 C|\lambda_0|\,|\epsilon|^{N-6},&(a,b)=(2,1).
 \end{cases}                                            \tag{IF.28b}
\]
At A restrict instead to \(|q_A|\le\eta|q_B|\).
Here \(|\epsilon|\) is comparable with \(|q_B|\),
the literal line character is \(V\), and its source
period multiplier is \(P^a\), of norm comparable
with \(|q_B|^{-a}\). Choose its endpoint metric
with the prescribed ratio \(|P|^a\), and interpolate
on the source annulus and plumbing charts. Its
maximum-to-minimum norm ratio is at most
\(C|q_B|^{-a}\), including both preimages of the
nodal point. The source part of \(g\) is
\(P^{-b}\), of norm comparable with \(|q_B|^b\).
Since \(|Q|\le C|q_B|^2\), returning the image of
\(|Q|\le|Z|\le1\) to that same annulus uses at most
two source periods for \(b=2\) and at most one for
\(b=1\), after fixing \(\eta\) and shrinking.
Each positive or negative reindex changes the line
norm by at most \(C|q_B|^{-a}\). The raw multiplier
has order \(N-2\); adding this metric loss and those
reindex losses gives exactly (IF.28b) for \(g\).

These estimates include all their face overlaps.
For fixed \(\eta<1\), the strict A and B regions
are disjoint; the intervening sector is covered by
the full-rank H parallelograms already constructed.
On each strict face its middle annulus and two node
charts use the same endpoint metric and transition
multiplier, so no further norm ratio is introduced
on their overlaps. Away from H the relevant
source/line maps lie in compact families and have
a common finite norm bound. At E the kernel is
the actual source Tate period, with its complete
elliptic fundamental annulus and its line holonomy.
The common H charts retain the nonzero images of
all these kernel vectors, which controls the
closures of their norm shells as described below.

We use the analytic construction at the two executed
orders \(N=8\) and \(N=6\), respectively. In the first
case (IF.28b) tends to zero; in the second it is
uniformly less than one after choosing \(|\lambda_0|\)
small. For an arbitrary admitted cap, take a sufficiently
large multiple of its order; IE.6 compares these orders
by an actual scalar pair of pants. The additional
\(N=3,4\) fan executions are finite arithmetic checks,
not an assertion of this norm bound at those orders.
The actual line-norm shells prove freeness and proper
discontinuity of the retained kernels on the nonzero
nodal lines. On E use the actual Tate shell for
\(Z\mapsto QZ\) together with the primitive chain.
Near H the two kernel vectors have nonzero H images,
so an unbounded sequence of their translates cannot
accumulate in a fixed H-cone chart. The full-rank
separation controls the closures of the face shells.

Finally a nonzero period cannot stabilize a bounded
cell on a full-rank face, and only finitely many
translates of a compact chart meet it. On a rank-one
face the only possible stabilizer is the specified
kernel, whose strict norm contraction has the same
finite-intersection property on a compact shell.
The equivalence relation is locally a finite union
of closed graphs on these compact covers. Its quotient
is Hausdorff, and inverse images of compact smaller
base sets are compact. On A and B its boundary charts
are precisely the actual Tate source chain and
Cartier line with their retained kernel maps; on E
they are (IF.26). Thus the punctured-parameter part
is the prescribed family under the displayed theta
and Cartier maps, with the stated boundary charts.

The global E-chain monodromy still carries its actual source-base
data. A small loop around the unselected collision has zero winding
of \(q_*\), so it fixes all \(N\) chain labels. A loop around the
separate selected value shifts labels by \(-nk\), and the inverse
cap cut at infinity shifts them by \(+nk\), for \(N=km\).
The latter two have \(k\) cycles of length \(m\). This is a
compatible list of branch locations; it does not itself construct
the missing selected-cusp attachment.

To complete the source return one still needs a real bordism
joining this collision/cap partial filling to the actual selected
I1 scalar trace, with its physical Euler line and normal
orientation. No full holomorphic selected corner, compact global
fourfold, signature, or return value is asserted in this note.

## IF.10. The changed-origin partial attachment away from the selected disc

Fix disjoint source-base discs around the unselected collision at \(t=0\),
the selected value \(t=t_*(\epsilon)\), and the cap at infinity. The first
and last closures are disjoint from the selected disc for all sufficiently
small \(\epsilon\). Put \(N=km\), retain the actual \(n=\pm1\), and use
\[
 \tau=\frac{\log\epsilon}{2\pi i},\quad
 s_*=\frac{\log q_*}{2\pi i},\quad
 s_\infty=\frac{\log q_\infty}{2\pi i},\quad
 h=1-t_*(\epsilon)q_\infty,\qquad
 s_*=-s_\infty+\frac{\log h}{2\pi i}.                   \tag{IF.29}
\]
On the unselected collision bidisc \(q_*\) is a nonzero unit, so \(s_*\)
has one holomorphic branch on that full bidisc. On the cap polydisc \(h\)
is likewise a nonzero unit, with its chosen reference logarithm.

On the universal parameter cover the actual ordinary-to-cap map and
the actual positive parameter-deck square are
\[
 F_\tau=F_0+nk\,\tau s_\infty\delta,\qquad
 R_{\rm ord}=q_*^{nk},\quad R_{\rm cap}=h^{nk},\qquad
 F_{\tau+1}R_{\rm ord}=R_{\rm cap}F_\tau.               \tag{IF.30}
\]
These are the admitted cap's norm and cochain formulas, with the current
source and the transported full \(F_0\) of IF.3. The source and line
characters are not changed. Define
\[
 o_{\rm ord}=nk\,\tau s_*\delta,\qquad
 o_{\rm cap}=nk\,\tau\frac{\log h}{2\pi i}\delta,\qquad
 \eta=\zeta-o_{\rm ord}.
\]
The exact overlap is
\[
                F_\tau+o_{\rm ord}-o_{\rm cap}=F_0.    \tag{IF.31}
\]
After a positive parameter turn the old ordinary chart is identified
by \(R_{\rm ord}\). Its change is exactly the change of \(o_{\rm ord}\);
therefore \(\eta\) has identity parameter deck. The cap coordinates
have the same property. This retains the closing arrow: neither
\(R_{\rm ord}\) nor \(R_{\rm cap}\) is silently set equal to one in
the old chart.

Every source period and line lift commutes with these base-only scalar
translations. Hence in the new ordinary coordinate the full periods
are exactly (IF.15), including all their units. Moreover positive
\(q_A\) or \(q_B\) continuation in the collision bidisc leaves \(s_*\)
unchanged. Thus the new collision coordinate has no additional
source-base chain deck there. The fan of IF.8 may therefore be
constructed directly in \(\eta\), and its quotient of IF.9 has the
pure parameter deck just proved. On its punctured parameter part
this is an actual isomorphism to the prescribed family, using
(IF.30), not an assertion that a fractional scalar power extends in
the old \(V\) coordinate.

The cap chain is constructed in \(\zeta_{\rm cap}-o_{\rm cap}\).
The actual primitive generator is
\[
 H=A^uB^w=\epsilon^k r_0H_0,\qquad nu+mw=1,
 \qquad H^m=B,\quad H^n=A ,
\]
with the actual admitted source and line maps. The displayed Bezout
equation is the literal exponent identity for \(A=H^n,B=H^m\).
Thus its node chart shift is
\(k\), and \(A\) has signed shift \(nk\). The source and finite
root maps in \(H_0\) are retained. The chain equations and all line
frame transitions are (IF.26), with \(H\) acting by that shift and
by its actual source/line map. A nonzero iterate changes the index,
so the action is free and properly discontinuous also at
\(\epsilon=0\).

On the cap annulus positive \(q_\infty\) continuation changes
\(s_*\) by \(-1\); the new ordinary vertical coordinate consequently
has the factor \(\epsilon^{nk}\). This is exactly \(A\)'s chain
shift and its retained \(A_0\) arrow. The cap unit \(h^{nk}\) acts
on a node chart by
\((X_j,Y_j)\mapsto(h^{nk}X_j,h^{-nk}Y_j)\); it is an extending
unit even though its central value is now \(1-q_\infty\), rather
than the constant one of the source-zero calculation. Its origin
change has been retained in (IF.30)--(IF.31).

On each remaining ordinary source-base chart, away from the selected
disc and these two special pieces, the source and Cartier line are
smooth over the full parameter disc. Use their full chain with the
actual source/line period. On angular overlaps the affine cochains
are exactly those already prescribed by \(F_0\); the only nonzero
integral base continuation is the signed cap shift just displayed.
The collision overlap has zero such continuation. Consequently
the ordinary chains, the collision fan in \(\eta\), and the cap
chain glue by literal extending source/line maps. This constructs
the partial family over the complement of the selected source-base
disc.

The relative regularization is by primitive determinant-one cones,
and the protected face charts are the actual smooth source/chain
charts. The total complex fourfold is therefore smooth. The map
to the epsilon disc may have a singular central fibre; smoothness
here refers to the total space and does not replace that map by a
submersion.

Properness over a closed smaller parameter disc follows from the
finite compact fundamental covers already described: collision
cones and face shells in IF.9, finitely many node/middle chain
charts on every ordinary compact source patch, and one finite
fundamental chain segment for \(H\) on the cap. A finite source-base
cover suffices. Every overlap is the actual biholomorphic map
(IF.31), so these compact covers produce a compact inverse image.
The only retained real boundary is over the boundary circle of the
deleted selected disc.

This is the partial attachment used in the next step. It provides
no filling of that last boundary and no return invariant. The exact
remaining morphism is its gluing to the selected-cusp scalar trace
with the physical Euler line and its normal orientation.

## IF.11. Executed local fixed-stratum data

The two independently saved regular fans have respectively
\[
 \begin{array}{c|r|r|rrr}
 (a,b,N)&\text{checks}&\text{stars}&A&B&E\\ \hline
 (1,2,8)&220943&1289&1838&1838&1818\\
 (2,1,6)&222609&1381&1748&1768&2021
 \end{array}
\]
maximal cone orbits. Every exported ordered cone has determinant \(+1\).
The fixed components are determined by the minimal face containing
the actual \(\delta\), with every recorded period and vertex
permutation used. In particular neither rank-one A nor rank-one B
contains a fixed component on its protected boundary.

The compact interior and H-normal calculations use the local
normal-link convention and formula (IE.16). On H the full unit
factors, with \(w=q_B/q_A\), are
\[
 h:(Z,V)\mapsto(wZ,w^{-a}V),\qquad
 g:(Z,V)\mapsto(w^bZ,w^{-2}(1-w)^NV)
\]
after the \(H_\infty\) normal powers are separated; the nonzero
constants remain part of the atlas. Thus the three normal-degree
orders at \(w=0,1,\infty\) are the same literal expressions
(IE.22), with the actual \(H_\infty\) used when unwrapping
the recorded periods.

The executed values, verified component by component using two
independent auxiliary circles, are
\[
 \begin{array}{c|rrr}
 (a,b,N)&\text{compact interior}&H&\text{sum}\\ \hline
 (1,2,8)&9333/16&-9301/16&2\\
 (2,1,6)&739&-734&5 .
 \end{array}                                           \tag{IF.32}
\]
All H surface tangent Euler numbers, canonical squares,
signatures and holomorphic Euler numbers satisfy their exact
integrality checks.

Each E fixed surface has the actual unmodified local I2 cycle
with intersection matrix \(\left(\begin{smallmatrix}-2&2\\2&-2\end{smallmatrix}\right)\).
The relative determinant marking \(Z^aV^2/\xi_E^{2j+1}\)
has divisor zero on both components, as the unwrapped cone
characters show. The local tangent marking
\(\Omega=d\log Z\wedge dt\) gives relative
\(p_1=-4\). Indeed the actual source-period change adds
\(d\log Q(t)\wedge dt=0\), so \(\Omega\) descends.
On a node chart \(xy=t\), it is \(dx\wedge dy\).
The vertical vector is \(x\partial_x-y\partial_y\);
it has one simple complex zero at each of the two nodes.
Together with the boundary vector normalized by
\(\Omega(W,H)=1\), this gives relative \(c_1=0\)
and \(c_2=2\), hence \(p_1=c_1^2-2c_2=-4\).
Thus the annular normal-link residue is \(-1/6\) per
E surface. These local numbers are retained with their
boundary frames. IE.3 constructs the actual E double,
and IE.4--6 assemble its completed-family contribution.

All programs and their full exact outputs are saved with the prefix
`code/part3_fourfold/source_infinity_`.
The source-family return uses the complete IE.1--7 comparison,
including its actual boundary frames and parameter orientation.

## IF.12. Full old-v / new-epsilon annular family comparison

Fix an integer root-scalar winding \(j\), and use
\[
 r(\epsilon)=\epsilon^j u(\epsilon)r_0,\qquad
 \lambda=r^m ,
\]
where the specified nonzero unit \(u\) has an extending
logarithm. The comparison in this section is over the
punctured epsilon annulus carrying this actual path.
It does not assume a trivial Isom torsor over a product
of two independent punctured parameter discs.

The source map (IF.1), the canonical divisor-line map,
and (IF.6)--(IF.7) identify the full ordinary suspension.
The selected Tate \(Q,P\) agree under this source
isomorphism. Their physical heights differ by
\(q_{\rm old}=\epsilon^{-4}q_*\), an actual single-valued
integer-power unit on this annulus. Its powers act on
the toric character charts and preserve the chosen
periodic fan and physical delta. Its winding is retained.

On each simply connected parameter chart use the actual
root map (IF.8)--(IF.9). It carries the marked source
section, the resolution ideals and the corrected Cartier
line. The finite source/line map has the form \(A=LD\),
where \(L\) covers \(-nR\). Its central commutator
character is one: in the good branch \(R=O\) centrally
and \(L\) is a scalar; in the reduced branch the
corrected root line is trivial on the compact reduced
III fibre, so the multipliers of \(D,L\) are constants,
and their source maps commute. The finite averaging
conjugation of the actual norm-one unit gives
\[
 DLD^{-1}=L,\qquad A^4D^{-4}=L^4 .
\]
The source part of \(L^4\) specializes to the identity
in both branches. Divide its central scalar and take
its small extending Lie logarithm. The actual annular
difference from four times the logarithm of \(L\)
retains the period (IF.10), with its full line factor
and signed \(n\). No multiple of that period is
asserted to be an extending reduced-root logarithm.

Choose one reference \(\epsilon_*\) and transport the
entire old ordinary-to-cap overlap through these
source/root/Cartier arrows, including \(d\delta\),
the chosen root cut, norm and finite character.
Use this full map as the reference of the new
\(F_0\). On a fixed new cap annulus the source and
root families are smooth through epsilon zero.
Restriction to a chosen root sheet identifies
the ordinary line quotient with the cap quotient:
an element \(A^hB^\ell\) fixing that sheet has
\(h=mk\), so is exactly \(B^{nk+\ell}\).
Thus the local comparisons are literal source
and line maps, and their sheet changes are the
retained powers of \(A\).

Correct those maps at \(\epsilon_*\) to the full
reference overlap. On two angular base charts
their overlap translations have Lie logarithms
zero at that reference. Lift along the simply
connected epsilon disc. Every ordinary and
finite-group discrepancy is an integral period
and is zero at the reference, hence stays zero.
The fixed-contour Cauchy splitting in the base
variable therefore glues the actual local maps
to \(F_0\), holomorphically in epsilon. This
retains its full annular integer and the
doubled reduced period. It is the explicit
Hom/source-period torsor construction of
RCZ.5, with the present displayed root maps
as its input.

Now compare the two completed families on a
small simply connected parameter chart.
Their total ordinary/root/cusp lattice
two-cocycles agree under the actual source
period identification: they agree at the
reference, and their integral discrepancies
are continuous in the parameter. The reduced
component translations are first removed by
their actual suspension powers. The remaining
Lie bundle has the literal coarse-base exact
sequence
\[
     0\longrightarrow\mathcal O\delta
       \longrightarrow V\longrightarrow\mathcal O(-1)
       \longrightarrow0 .
\]
The source dualizing vector and physical delta
give its relative frames. Split the extension
and its one-cocycles by the fixed-circle
Cauchy/Laurent operators for \(\mathcal O(1)\),
\(\mathcal O\), and \(\mathcal O(-1)\).
Finite averaging preserves the full root
cocycles. Exponentiation then gives actual
local family isomorphisms extending on the
chosen cusp and root charts.

On two parameter charts their ratio is a
global extending translation. The actual
source/rational-divisor endpoint argument
of RCZ.4 identifies that group with the
physical \(\mathcal O^*\), including all
finite-kernel choices. To glue the local
maps, take logarithms \(\ell\) of their
scalar ratio on the two angular overlap
components, choose \(\chi_++\chi_-=1\),
and set \(b_+=\chi_-\ell,b_-=-\chi_+\ell\).
Their common \(\bar\partial\) is solved on
a smaller annulus by
\[
 v(\epsilon)=\frac1\pi\int_{\mathbb C}
       \frac{\widetilde f(w)}{\epsilon-w}\,dA(w).
\]
Then \(h_\pm=\exp(b_\pm-v)\) have ratio
equal to the actual scalar transition,
and \(h_\pm^{-1}I_\pm\) glue literally.
The cutoff is supported in the larger
annulus and equals one on the loop.
This construction retains both overlap
components and any integral scalar winding.

There is a concrete forward-endpoint
factor before this last scalar splitting.
For the root winding \(j\), the old and
new ordinary forward decks have ratio
\[
      q_{\rm old}^{nj}/q_*^{nj}
                         =\epsilon^{-4nj}.
\]
With \(\tau=\log\epsilon/(2\pi i)\), retain
the actual compensating cochain
\[
 c_0(\tau)=\exp\{2\pi i\,2nj\,\tau(\tau-1)\},
 \qquad
 c_0(\tau+1)/c_0(\tau)=\epsilon^{4nj}.                 \tag{IF.33}
\]
This is not declared single valued by
itself. It belongs to the forward
parameter-deck square, alongside the
\(D^{-4}\) root endpoint and the
retained period above.

All constructed maps and inverses are
source/Cartier coordinate maps,
extending translations on their stated
charts, or physical scalars. Thus they
give a holomorphic delta-equivariant
family isomorphism on the epsilon
annulus, carrying the actual line,
fan, normal circle and closing arrows.
A connection transported through
this family map identifies the physical
returns by conjugacy; there is no
loop reversal or numerical class division.

For the old global scalar
\(r=\epsilon^{-2k}(1-\epsilon^2)^kr_0\),
one has \(j=-2k\). Formula (IF.33) is
\(\exp\{-2\pi i\,4nk\,\tau(\tau-1)\}\),
whose one-step ratio is
\(\epsilon^{-8nk}\). The nonzero unit
\((1-\epsilon^2)^k\) is retained and
can be homotoped to its reference value
through its extending logarithm.
The local rescaling
\(r=\epsilon^{k_\infty}r_\infty\)
is instead \(j=k_\infty\). Their
root-winding difference is
\(-2k-k_\infty\), as in RG.5.
These are two explicitly compared
loops, not two notations for one scalar.
