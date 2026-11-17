# P3K.80. Proved: the actual reduced-source zero return

## Statement

Retain the marked source
\[
 E_v:\quad Y^2=X^3+(1-2v)X^2+TX+v^2,\qquad G=(0,v),
\]
the actual Cartier line \(M_2=O([2G]-[O])\), the suspension
over \(-G\), and the selected whole-zero fibre at
\(T_0(v)=v^2-2v\). Retain the reduced III cap of order
\(m=4p-1\), \(p\ge1\), either norm sign \(n=\pm1\),
and every admitted integral \(d\delta\) character. These
are the sphere families and exact cap markings of P3K.24,
with the physical line convention of P3K.68.

For a fixed sufficiently small nonzero scalar, the positive
\(v\)-loop has physical Jin integer \(0\) in the initial
negative-square fan \(T_0\). Its actual oriented clutched-sphere
class is \(0\in\Theta_7\simeq\mathbb Z/28\). The literal
reflected fan \(JT_0\) has actual class \(2\). For the
actual coupled family \(r=v^k r_0\), \(\lambda=r^m\),
\(k\ge1\), the two classes are
\[
 (Z_{T_0},Z_{JT_0})
   =\bigl(k(3p-1),\ 2+k(3p-1)\bigr)\pmod {28}.
 \tag{RA.1}
\]
The reflected value uses the actual directed relative flop.
This statement treats the reduced \(a=2,b=1\) branch.

## Proof

The proof constructs a finite real bordism carrying the
actual physical circle, its associated line, and the
canonical complex spin-c arrows on every local overlap.
The fixed-scalar loop is separated from the scalar winding
by the actual two-parameter family before the cut is made.
All local source, line, node and finite-root maps needed
for the cut are reproduced below. The local equation
prefixes identify the component calculations within this
single proof. In this proof \(a=2,b=1\), except in the
displayed weight identities which retain \(a\) to show
the actual character. The Tate period is denoted
\(H_T=(Q,P^2)\); the finite-cap unit is
\(h_\infty=1-T_0(v)q_\infty\). They are distinct
explicit maps/functions throughout.

## RA.2. Source, Cartier and actual Tate data

Put \(q=T-(v^2-2v)\).  On the source threefold set
\[
 A=Y-v,\quad B=Y+v,\quad C=X,\quad
 D=T+X^2+(1-2v)X .
\]
The source equation is literally \(AB=CD\).  Its marked small
resolution has the chart
\[
 A=Dz,\qquad C=Bz,\qquad v=(B-Dz)/2.
\]
The chosen section \(G\) has \(z=0\).  The actual closure of
\(2G\) has Cartier equation
\[
 F_2=1-Bz^3-(1-2v)z^2=0.
\]
Indeed the doubling formula gives \(z=-2v/T\) and
\(zT+2v=BF_2\); the factor \(B=0\) is the other section
\(-G\), so the strict closure is \(F_2=0\).
Define the actual target-point primitive on \(O(G-O)\) by
\[
 U:(p,w)\longmapsto\left(p-G,\frac{w}{X(p-G)}\right).
 \tag{SZ.7}
\]
The identity
\((G)-O-t_G^*((G)-O)=\operatorname{div}X\)
makes this the indicated line map; its tensor-square is the
primitive on \(O(2G-2O)\).  The Cartier conjugation below
identifies that tensor-square with the specified actual
line \(M_2\).  In that conjugation the retained rational
function is
\[
 F_{21}=\frac{Y+v+(T/(2v))X}{X}.
\]
Its displayed poles are carried by the rational line map;
the resolved Cartier arrows below are the extensions used
on the finite cut.


### The source graph and its Cartier coefficient

The chamber overlap is the following literal map.
Write \(p'=p-G\), and let \(F_2=1-Bz^3-(1-2v)z^2\) be the actual
Cartier equation just displayed. The addition formula gives
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
The finite construction below uses these actual chambers, the full selected factor, and their finite-root maps.
Its outside boundary is identified with the actual family by the mixed-face maps below.

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

### The exact two-node base coordinates

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



### The full Tate periods and units

The periods used in the finite construction are obtained from the actual
Tate coordinates on the full two-node base. The source has
\[
 c_4=16((1-2v)^2-3T).
\]
This is a unit at the origin. Its discriminant has the two simple
factors \(q_1q_2\) just defined. Inverting the convergent \(j\)-series
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
the preceding two-node chart are \(v+T/2\) and \(v-T/2\); hence those two vanishing
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

The target-point primitive lift (SZ.7) is now exactly
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

## TL.1. The full marked source map

Use the convergent Tate node map from SZ.39--40, with its chosen
Weierstrass scaling, both inverse branches, and marked lift:
\[
 Z_0W_0=Q=q_1q_2u_Q,\qquad
 P=P_G=q_2^{-1}u_P,\qquad u_G=u_Qu_P,
\tag{TL.1}
\]
where \(u_Q,u_P\) are actual nonvanishing holomorphic functions on
the full two-node base and
\[
 u_Q(0)=1/256,\qquad u_P(0)=16,
\qquad Z_0(G)=q_1u_G,\quad W_0(G)=q_2/u_P.
\]
The source small-resolution chart is given by the literal maps
\[
 S=P W_0,\qquad T_0=Z_0/u_G,
\]
\[
 Z_0=u_GT_0,\qquad W_0=q_2S/u_P,
\qquad q_1=ST_0.                                    \tag{TL.2}
\]
This is the chart of the resolution of \((W_0,q_2)\) in which the
ratio \(W_0/q_2\) is finite. Its other projective chart retains
\(S'=S^{-1}\), \(T'_0=ST_0=q_1\), and \(T'_1=S q_2\), so
\[
 q_2=S'T'_1,\qquad
 Z_0=u_G S'T'_0,\qquad W_0=T'_1/u_P.
\tag{TL.3}
\]
These are inverse coordinate charts of the same proper small
resolution; they agree by the displayed substitutions. In particular
\(S(G)=1\) holds exactly on the whole section, not only to first
order. The two branches in the selected source bidisc are
\(S=0\) and \(T_0=0\). Both are retained in (TL.2).

Here is the arrow from the earlier node-adapted Morse chart. In
SZ.20--21 put \(A_M=(Y-R)/\upsilon\), \(B_M=Y+R\), so
\(A_MB_M=q_1q_2\). Write
\(A_M(G)=q_2a_G\), with \(a_G\) an extending unit. The actual
base-unit change
\[
 \alpha_M=-A_M/(2a_G),\qquad
 \beta_M=-2a_GB_M                                  \tag{TL.4}
\]
has product \(q_1q_2\), and sends the marked section to
\(\alpha_M(G)=-q_2/2\), \(\beta_M(G)=-2q_1\). The analogous
Tate functions are
\[
 \alpha_T=-u_PW_0/2,\qquad \beta_T=-2Z_0/u_G,
 \qquad \alpha_T\beta_T=q_1q_2.                     \tag{TL.5}
\]
They are literal holomorphic functions of the Weierstrass point by
the convergent Tate inverse map.

The selected branches in SZ.40 choose \(W_0\) to match the
\(\alpha_M\) branch. More explicitly the two maps preserve the
nodal point on each of the smooth punctured discriminant branches;
their nonsingular linear normal maps match \(\alpha_M\) with
\(W_0\), rather than with \(Z_0\). Hence the Cartier zero divisors
of \(\alpha_T\) and \(\alpha_M\) have the same two irreducible
components and multiplicity one. They have no further zero divisor
on a smaller conifold neighbourhood. The exact quotient
\[
                      b_T=\alpha_T/\alpha_M          \tag{TL.6}
\]
is therefore a holomorphic unit on the normal conifold: both the
quotient and its inverse have nonnegative valuation at every
prime divisor. The chosen linear maps give \(b_T(0)=1\), and
the marked evaluations give \(b_T(G)=1\).

In the earlier projective chart
\(\alpha_M=-q_2S_M/2\), \(\beta_M=-2T_M\), this supplies the
actual resolution lift
\[
             (S_M,T_M,q_2)\longmapsto
                    (b_TS_M,b_T^{-1}T_M,q_2).        \tag{TL.7}
\]
Its inverse is the inverse of the already specified analytic
Weierstrass/Tate maps; the ideal \((\alpha_M,q_2)\) is carried
to \((\alpha_T,q_2)\) because their ratio is a unit. Thus the
map lifts on both projective charts. On the exceptional projective
line its unit is one. After shrinking, its logarithm is the actual
holomorphic logarithm near one. No parameter winding has been
removed by this lift.

For the original Cartesian section equation, the precise additional
Cartier factor is its pullback divided by \((1-S)/2\). Both have
the same marked divisor with multiplicity one under the full map,
so this quotient is an extending unit. It is retained on the source
side, with its inverse on the target side. This defines its full
higher-normal terms; none is replaced by its exceptional value.

## TL.2. The exact line map on both source branches

Use the same theta convention as SZ.41:
\[
 f_P(Z)=\Theta_Q(Z/P)/\Theta_Q(Z),\qquad
 \Theta_Q(z^{-1})=-z^{-1}\Theta_Q(z),\quad
 \Theta_Q(Qz)=-z^{-1}\Theta_Q(z).
\]
The Tate representative on the source chart (TL.2) is
\[
                         Z=P/S=1/W_0.                \tag{TL.8}
\]
It is the original representative obtained from \(Z_0\) by the
literal inverse source period. Theta inversion gives the exact
identity
\[
 f_P(P/S)=P^{-1}\frac{\Theta_Q(S)}{\Theta_Q(S/P)}.
\tag{TL.9}
\]
The tensor Cartier coefficient in the actual marked divisor frame
is
\[
       \xi=\left(\frac{1-S}{2}\right)^a
                      \frac{V}{f_P(P/S)^a}.          \tag{TL.10}
\]
Applying the actual source period
\(h:(Z,V)\mapsto(QZ,P^aV)\) yields
\[
 Z_0=QP/S=u_GT_0,\qquad
 V_0=P^aV=E_+(S,T_0,q_2)^a\xi,
\]
\[
 E_+=\frac{2\Theta_Q(S)}{(1-S)\Theta_Q(S/P)}.        \tag{TL.11}
\]
Every function in this equality is the full function, including
the actual \(P\) and the source-period line factor \(P^a\).

The factor in (TL.11) is a holomorphic unit on the entire source
bidisc, including both branches. Indeed the convergent product
for \(\Theta_Q(S)/(1-S)\) has factors in \(Q^rS\) and
\(Q^r/S\), and
\[
 Q^r/S=S^{r-1}T_0^r q_2^r u_Q^r\quad(r\ge1).
\]
For the denominator use
\[
 S/P=W_0=q_2S/u_P,\qquad Q/(S/P)=Z_0=u_GT_0.
\]
Thus its product factors are holomorphic in \(Z_0,W_0,Q\).
On a sufficiently small fixed bidisc all of them are nonzero,
and the products converge normally. On \(q_2=0\), the numerator ratio equals one, whereas the
denominator retains its factor \(1-Z_0\). Thus the exact restrictions
are
\[
 E_+(S,T_0,0)=\frac{2}{1-u_G(ST_0,0)T_0},\qquad
 E_+(S,0,0)=2.                                       \tag{TL.12}
\]
This also handles the removable zero at the marked section
\(S=1\). In particular the source line map and its inverse
extend; a logarithm of \(E_+/2\) extends through the full collision
base. Equation (TL.11), rather than only its value (TL.12), is the
line map used on the collar.

On the other projective source chart the coefficient is
\(\xi'=S^{-a}\xi\), because the marked equation becomes
\((S'-1)/2\). Substitution of \(S=1/S'\) in (TL.9)--(TL.11)
gives the same Cartier map wherever the two charts overlap.
This is a statement about the two line charts of the actual
degree-\(a\) line. It does not declare the constant-factor Tate
frame to extend unchanged over that entire projective line.

## TL.3. The actual fan label

For fixed nonzero \(q_2\), the selected node has source coordinates
\((S,T_0)\) with \(ST_0=q_1\). Its associated node and first
small resolution are the actual equations
\[
 U V_{\rm node}=S T_0,\qquad U=S z,\quad T_0=zV_{\rm node},
\]
with \(U=\xi\) after the Cartier arrow just written. In the
characters \((S,U,q_1)\) its two cones have positive-square
triangles
\[
 \{0,e_1,e_1+e_2\},\qquad\{0,e_2,e_1+e_2\}.
\]
The exact map (TL.11) has valuation map
\[
         (x,y,h)\longmapsto(h-x,y,h).                 \tag{TL.13}
\]
The units \(u_G,E_+\), and the preceding Morse/Cartier units
are nonvanishing on the full source bidisc. Hence their pullbacks
are nonvanishing on all of these toric charts. A monomial generator
of each cone semigroup is carried to its stated monomial times an
explicit such unit, and the inverse has the same property. This
proves extension of the character map to the full matched cones.

On height one the two triangle images are
\[
 \{e_1,0,e_2\},\qquad\{e_1,e_1+e_2,e_2\}.
\]
They are precisely the two triangles of current Tate \(T_0\),
the negative diagonal. The opposite associated resolution maps
to current Tate \(T_1\). The terminology \(j=-1\) in the
earlier SZ.15 uses its earlier square convention; (TL.13) supplies
the actual character map and does not identify those index symbols.
The physical circle acts on \(\xi\) and \(V_0\) with the same
positive weight. The analytic map preserves the complex orientation.

## TL.4. Full period and closing arrows

The source change above is the actual identity of the marked
Weierstrass source expressed by two specified analytic coordinate
systems. The Cartier ratio is the canonical theta/divisor ratio.
Consequently the primitive translation is transported to precisely
\(U_a:(Z,V)\mapsto(P^{-1}Z,c_X^{-a}V)\) of SZ.43, and the
full suspension is still
\[
 B=2(-1)^{b+1}\lambda q_1 U_a^b,\qquad ab=2.
\]
The equality follows on the common smooth torus from the exact
theta identity used in SZ.43 and extends wherever both charts are
defined. The source period in (TL.11) is an actual quotient deck,
including its line factor, not a replacement of the period by a
valuation vector.

On a source-parameter annulus the full functions in (TL.1)--(TL.11)
are single valued. The functions \(P\) and \(P^a\) retain their
nonzero windings before the displayed period reindexing. The
remaining factors have extending logarithms. An ordinary parameter
closing \(q_1^{\nu k}\) commutes with these source/line maps and
is retained literally. At \(a=2\), the same assertion includes
the source and target \(r\) factors. Thus the calculation labels
the selected boundary chart with its actual parameter arrow.

The separate cyclic reset of EA.18--23 enters the complementary
charge-\(a\) chart, retains the physical normalization
\(c_\lambda=2\lambda\), and uses an adjacent Tate-node overlap.
The present local comparison does not remove that reset, its
parameter winding, or any transported truncation. In particular
neither a compact collision-to-cap attachment nor an absolute
source-zero return is inferred from the fan label alone.

## RT.1. The horizontal trace immersion

The marked small-resolution coordinates are
\[
 A=Dz,\qquad C=Bz,\qquad v=(B-Dz)/2.
\]
On the normalization of the selected nodal fibre,
\[
 X=s^2-1,\quad Y=s(s^2-1-v),\quad T=v^2-2v,\quad
 z=(s+1)/(s^2+s-v).
\]
Put \(x=s+1,v=xr\). The blowup chart has the exact map
\[
 z=(x-1-r)^{-1},\quad B=x(x-2)(x-1-r),\quad
 D=(B-2xr)/z.
\]
The Jacobian of \((z,B)\) with respect to \((x,r)\) is
\(-2(x-1)/(x-1-r)\), hence is nonzero on the exceptional curve wherever
this chart is finite. At its missing point use
\(w=x-1-r,C=x(x-2)\); the Jacobian is \(2x-2\), again a unit there.
The second blowup chart \(v=y,x=yh\) has
\(z=h/(-1-h+yh^2)\), whose h derivative at y=0 is
\(-1/(-1-h)^2\). These formulas give the actual immersion of the complete
horizontal normalization trace through the exceptional curve.

Let \(F=\operatorname{Bl}_{(-1,0)}(\mathbb P^1_s\times D_v)\) and let E
be its exceptional curve. The Cartier ratio
\((s-\sqrt{1+v})/(s+\sqrt{1+v})\) has divisor
\(D_+-D_--E\). The actual source line restricts as \(O(-aE)\).
Consequently the retained spinor determinant on this trace is
\((1-2a)E\); reversing the two selected branches gives
\(-(1+2a)E\).
The complete fixed and cap contributions are calculated in RT.16--17 below.


## RT.2. Exact q factorization on the Cox bridge

Use the actual Cox coordinates
\[
 A'=s_0t_0,\quad B'=s_1t_1,\quad C'=s_0t_1,\quad D'=s_1t_0,
\]
with physical weights \((-1,-1,+1,+1)\) on
\((s_0,s_1,t_0,t_1)\), divided by the retained \(\mu_a\) when appropriate.
The actual base functions, before any quotient completion, are
\[
 v=(s_1t_1-s_0t_0)/2,\qquad
 q=(s_1-s_0)(t_0+t_1)-(s_0t_1-v)^2.
\]
Set \(x=s_0,y=t_1,k=s_1-s_0,l=t_0+t_1\), and choose the analytic unit
\(\sigma=\sqrt{1+xy}\) with value 1 at the origin. Define
\[
 F_+=\frac{(\sigma+1)k-x^2l/(\sigma+1)}2,\qquad
 F_-=\frac{(\sigma+1)l-y^2k/(\sigma+1)}2.
\]
Then
\[
 q=F_+F_-,\qquad
 \det\frac{\partial(F_+,F_-)}{\partial(k,l)}=\sigma.
\]
Thus this is an actual analytic coordinate change over \((x,y)\), with inverse
\[
 k=\frac{(\sigma+1)F_++x^2F_-/(\sigma+1)}{2\sigma},\quad
 l=\frac{y^2F_+/(\sigma+1)+(\sigma+1)F_-}{2\sigma}.
\]
The weights of \(F_+,F_-\) are respectively \(-1,+1\). No physical
character is changed. The source parameter becomes
\[
 v=xy+\frac{yF_+-xF_-}{2\sigma}.
\]
On the chart with invariant coordinates \(u=x/F_+,z=y/F_-\), this reads
\[
 v=q\left(uz+\frac{z-u}{2\sqrt{1+uzq}}\right).
\]
These formulas retain both actual branches of q=0. The finite domain below retains the quotient strata over both branches.

## EA.17. Full two-node refinement of the Morse-Cox pairs

The parameter formula in the exact two-node chart is
\(\widetilde v=q_1-q_2=v u_v(v)\). To retain it together with
the primitive Cartier frame, use the actual analytic source
functions from SZ.20--21 and TL.4. Explicitly, put
\[
 A_0=1-2v,\qquad x_c=\frac{-A_0+\sqrt{A_0^2-3T}}3,
\]
\[
 R_c=(X-x_c)\sqrt{A_0+2x_c+X},\quad
 \upsilon=\frac{v^2-A_0x_c^2-2x_c^3}{q_1q_2},
\]
where both square roots and the extending unit upsilon are the
specified analytic branches. Define
\[
 A_M=(Y-R_c)/\upsilon,\quad B_M=Y+R_c,\quad
 a_G=A_M(G)/q_2,
\]
\[
             \alpha=-A_M/(2a_G),\qquad
             \beta=-2a_GB_M.
 \tag{EA.42}
\]
They satisfy \(\alpha\beta=q_1q_2\),
\(\alpha(G)=-q_2/2\), and \(\beta(G)=-2q_1\).
All functions are pulled back through the actual Cartesian source
map of SZ.19; no linear approximation is used in (EA.42).

Keep the exact selected factors F+,F- of RT.2 and define
\[
 S_0=F_+,\qquad T_0=F_-,\qquad
 S_1=-\frac{\beta}{2F_-},\qquad
 T_1=-\frac{2\alpha}{F_+}.
 \tag{EA.43}
\]
The quotients extend holomorphically. For example F+=0 is an
irreducible coordinate hypersurface of the RT.2 chart. The
restriction of beta to it is not identically zero, as its leading
term is \(-2(s_0+s_1)(t_0+t_1)\). Since alpha beta vanishes
there, alpha vanishes identically there and is divisible by F+.
The analogous argument gives divisibility of beta by F-. The
leading maps are exactly
\[
 (S_0,S_1)=(s_1-s_0,s_0+s_1)+O(\|(s,t)\|^3),
\]
\[
 (T_0,T_1)=(t_0+t_1,t_0-t_1)+O(\|(s,t)\|^3).
\]
Their complex Jacobian at the origin is 4. Thus (EA.43) is an
actual auxiliary-equivariant analytic isomorphism on a small
neighbourhood. It has
\[
                 q_1=S_0T_0,\qquad q_2=S_1T_1,
                 \widetilde v=S_0T_0-S_1T_1
 \tag{EA.44}
\]
as literal equations. It preserves the two ruling ideals and
therefore lifts both small resolutions, with their actual source
coordinate maps. This is the full higher-normal comparison behind
the linear display SZ.26.

The marked section is retained as well. On the old divisor s0=0,
the exact evaluations in (EA.42) give S1=S0. Hence
\[
                \kappa=\frac{S_1-S_0}{2s_0}
 \tag{EA.45}
\]
is holomorphic; its value at the origin is one, so it is a unit.
The actual line coefficient is carried by
\[
                    \xi_{\rm node}=\kappa^a\xi_{\rm Cartier}.
 \tag{EA.46}
\]
This follows by equating the meromorphic coefficients with
denominators \(s_0^a\) and \(((S_1-S_0)/2)^a\).
The source and target r maps are applied before and after this
formula when a=2. The full reset is consequently conjugated by
the actual kappa factors at its two ends; they are not replaced
by their value on the exceptional curve. The same conjugation
is made in the F0 root square.

The unit kappa and the normalized Jacobian of (EA.43) have
extending logarithms. Their exact logarithms carry the line and
canonical spin-c determinant lifts, while the nonunit
\((-1)^a z_s^{-2a}\) reset and its explicit root in EA.27
remain. Thus (EA.43)--(EA.46) connect the full finite-face proof
to the bilinear source map in RT.13--15 and to TL's actual Tate
label. They do not identify the intermediate nonlinear v formula
with the bilinear formula without this morphism.

## RT.12. Removing the scalar winding by an actual parameter homotopy

This step concerns the punctured family only. It supplies the exact
reason a constant-scalar local attachment can be studied separately;
it does not replace v^(km) by a unit over the origin.

Fix a small source circle |v|=rho and its annular neighbourhood. Choose
the branch of sqrt(1+v) which extends across the source disc and the
same root and Cartier data as RG.1 and RCZ.5--7. On this compact
annulus introduce an independent nonzero root-scalar r. The actual
maps, in the existing full annular marking, are
\[
 B=r^mB_0(v),\qquad A=r^nA_0(v),\qquad
 F=F_0(v)+n\frac{\log r}{2\pi i}s_\infty\delta.
                                                        \tag{RT.17}
\]
The reference F0 here is the actual extending cap-annulus map
constructed in RCZ.5, with its complete integral period, d-delta
cochain and reduced Cartier correction. Its construction is over
the full v-disc on that cap annulus. Source and root equations and
A0 are also holomorphic there, as RG.1 records. The ordinary toric
charts are the same fixed fan over the source annulus; all their
coefficient functions are retained. Compactness of the parameter
annulus permits one sufficiently small scalar annulus on which
these quotients and caps give the proper smooth family.

The positive r deck has the literal ordinary and cap arrows
q1^n and h^n, with h=1-T0(v)q_infinity. They commute with the
retained period maps and finite groupoid arrows. Their coefficients
are single-valued in v on this annulus. Thus (RT.17) is the same
independent-scalar construction used in RG.5, now on the source-zero
annulus; no scalar or source closing is replaced by an unmarked map.

Take r0^m=lambda0 and retain the actual base amplitude \(r_{\rm base}=v_*^k r_0\). The original loop is
\[
 v(t)=v_*e^{2\pi it},\qquad r(t)=r_{\rm base}e^{2\pi ikt}.
\]
On the real phase cover its path (t,kt) has the same endpoints as
the broken path
\[
 (\min(2t,1),\ k\max(2t-1,0)).
\]
Their straight interpolation, with the corner smoothed relative
the endpoints, is an explicit based homotopy in the actual parameter
torus of (RT.17). The first part of the broken path is the source
loop at constant \(r_{\rm base}\); the second is k root-scalar loops at the same
source basepoint. Their complete endpoint arrows compose to
q1^(kn),h^(kn), exactly the original forward arrows. The given root
norm A0^m=B0^n and the full F0 square remain in this homotopy.

Any further comparison to a different fixed scalar reference uses
a separate zero-winding radial path inside the common contracting
range, carrying the actual norm root and F0. No such amplitude change
is hidden in the phase-cover homotopy above.

Consequently the actual oriented sphere-return classes satisfy
\[
 Z_{\mathcal T}(k)=Z_{\mathcal T}(0)
                      +k A^{\rm scalar}_{\mathcal T}.   \tag{RT.18}
\]
This follows from the constructed family homotopy and the clutch
composition, before using the abelian identification with Z/28.
For the two reference/reflected vertical fans the current physical
scalar values are 0 in the good branch and 3p-1 in the reduced
branch, by K69/K72. Their equality on those two fans is the literal
n=0,1 comparison in that integer scalar proof.

Thus the factor c*lambda in a local constant-scalar study is
constant only after (RT.17)--(RT.18) separate its k actual scalar
turns. In the original family c*v^(km)*lambda0 still has its full
winding and zero. No extending logarithm for that factor is asserted,
and the unknown source-zero class Z_T(0) is not evaluated here.

## EA.12. The actual fixed-scalar exterior, finite root and inverse square

The scalar split uses the actual basepoint from RT.12:
\(r_{\rm base}=v_*^k r_0\), \(r_0^m=\lambda_0\).
The fixed-scalar piece is studied at \(r=r_{\rm base}\), and the
additional k canonical scalar turns are retained by the explicit
based homotopy in RT.12. A subsequent zero-winding radial change of
the scalar is a separate path in the common contracting range.

Here is the proper exterior available before the inner attachment.
Choose a source-base disc \(|T|<\epsilon\) containing both fibres
which collide at \((T,v)=(0,0)\), and shrink the source-parameter
disc so that their closures stay inside it. On its compact complement,
the resolved marked source, the section G, and the actual Cartier line
are smooth families through v=0. The selected factor q is nonzero
there. Consequently the actual nonzero-line lift B0 is an invertible
line map on this complement. A Hermitian metric on the compact
source complement bounds its norm by one finite constant C. Taking
\(|r_{\rm base}|^m C<1\) makes B a uniform contraction. Its
nonzero-line quotient has a compact fundamental annulus: the region
between a unit norm hypersurface and its B-image. This construction
retains the source boundary \(|T|=\epsilon\), the physical circle,
and the actual B endpoint; no quotient at the colliding source point
is used.

At the finite root cap retain \(A=r_{\rm base}^n A_0\),
\(B=r_{\rm base}^mB_0\), and \(A_0^m=B_0^n\).
Choose integers u,w with \(nu+mw=1\). The literal common generator
\(H=A^uB^w=r_{\rm base}H_0\) satisfies \(H^m=B\) and
\(H^n=A\). Its norm is bounded on the compact resolved root source,
so a further decrease within the same scalar range gives the same
compact fundamental-annulus construction. This applies to both
norm signs. The actual finite character and corrected root line are
carried by H0, not replaced by an unmarked root. The ordinary/cap
overlap is the full F0 of RCZ.5--7. Its lifted source/line maps commute
with B0 and physical scalars, so they identify the two actual quotient
boundaries. This gives a proper smooth exterior over the full v-disc,
with its only new source-base boundary \(|T|=\epsilon\).

For the inner finite strip, write \(J_j\) for the actual associated
node chart at chain label j. The following maps and equations are
already fixed:

1. The forward suspension is the actual map
   \(B_j:J_j\to J_{j+1}\), carrying the source by \(-G\) in
   the reduced branch and the line by its Cartier coefficient. In
   the common graph frame its node coordinates satisfy (EA.11).
2. Between consecutive source graphs the reset is (EA.18)--(EA.20),
   including \(\widetilde\xi=\xi/z_s^4\). This enters the
   complementary positive U=1 chart; it does not remain in the
   primary charge-one chart.
3. The adjacent-node arrow \(J_{j+1}\to J_j\) is (EA.23).
   Its physical normalization at fixed scalar is
   \((U,V)\mapsto((2\lambda)^{-1}U,2\lambda V)\).
   In the charged gauges this is (EA.22), with the chambers in EA.11.
   Thus the U=1 and V=1 descriptions are one charge-a boundary point.
4. The full ordinary-to-cap square on each chosen root sheet is
   \[
      F_0 U_a^{\rm Cartier}
         =z_\infty^{ma/2}U_{\rm cap}F_0,
      \qquad
      F_0B=2(-1)^{b+1}\lambda h_\infty\,U_{\rm cap}^{b}F_0.
   \]
   The root character and the good-branch sign cancel as in EA.4;
   the reduced branch commutes. These are equations of actual line
   maps, with \(q=q_\infty^{-1}h_\infty\), not merely source-point equations.
5. The full node-to-Tate map TL.1--4 carries the
   actual h reindex, \(P=q_2^{-1}u_P\), the theta units and the
   degree-two Cartier map. Its positive associated square is the
   current Tate fan T0. It must be used on the \(|T|=\epsilon\)
   collar rather than the earlier normalization-stratum formula EA.8.



## EA.5. The finite stable-end metric arrow and its fixed boundary

This section works with a fixed nonzero scalar, chosen small after the
compact source-origin neighbourhood has been cut out. It does not use the
nonproper infinite central quotient from SZ.29. On the compact exterior
the actual source/line multiplier is bounded, so this scalar gives a
uniform finite contracting cut. The selected divisor is retained by its
node charts, rather than by a limit of a zero scalar in one chart.

For the reduced primitive period write the nonzero constant as
\(c_\lambda=2\lambda\). The actual arrow is
\[
 (p,w)\longmapsto(p-G,c_\lambda q\,\rho(p)w),
\]
where \(\rho\) is precisely the Cartier line arrow (EA.6). On the
logarithmic Tate chain put
\[
 U_j=\frac{w}{c_\lambda^j q^j},\qquad
 V_j=\frac{c_\lambda^j q^{j+1}}w,
 \qquad U_jV_j=q.
\]
The period sends \(j\) to \(j+1\) and
\[
 (U_j,V_j)\longmapsto(\rho U_j,\rho^{-1}V_j).
 \tag{EA.11}
\]
In the common Cartier/Cox line frame, \(\rho\) is the identity
arrow between the two source rulings. Thus its node extension is
literally the associated chart \(UV=S_0T_0\), with the weights in
SZ.28. The factor \(q\) has been removed by the stated chain-index
change, not by a limiting argument. The two finite cap arrows in
EA.4 still accompany this chart.

Here is the needed change of the finite cut hypersurfaces on the stable
locus. Let \(\xi\) be the common line coordinate of auxiliary weight
\(a\), with \(s\) of weight \(+1\) and \(t\) of weight \(-1\).
The actual Fubini--Study divisor metrics give
\[
 N_t=|\xi|\,\|t\|^a,\qquad
 N_s=\frac{|\xi|}{\|s\|^a},\qquad
 R=\|s\|\|t\|,\qquad N_t=R^aN_s.
 \tag{EA.12}
\]
These are auxiliary-invariant functions. The arrow from the domain end
\(H_t=\{N_t=1\}\) to the target end \(H_s=\{N_s=1\}\) is the
physical positive rescaling
\[
 (\xi,\xi_{\rm dual})\longmapsto
 (R^a\xi,R^{-a}\xi_{\rm dual}).
 \tag{EA.13}
\]
It preserves the product \(\xi\xi_{\rm dual}=q\), the source
coordinates and the physical circle. On \(R\ge\varepsilon>0\)
it is smooth and bounded and extends both node branches. At
\(R=\varepsilon\) its factor is the constant
\(\varepsilon^a\). Only after (EA.13) is the auxiliary positive
normalization used to choose a representative. Auxiliary normalization
alone does not change (EA.12), and was not an end-to-end map.

On the reduced moment graph of RT.8,
\(\mu_{\rm aux}+K\mu_\delta=c\), with \(K,c>0\), the derivative
along the positive auxiliary orbit has the five coefficients
\[
             1,\quad1,\quad1,\quad1+K,\quad4+2K.
\]
It is therefore strictly positive away from the origin. The unique
normalizing arrow is smooth on the displayed stable overlaps and
preserves the full functions \(q,v\), because they are auxiliary
invariants. The actual cap metric is transported by \(U_{\rm cap}\);
on the overlap it is joined to (EA.12) by the logarithm of the positive
metric ratio. Averaging that real function over the finite root group
makes the interpolation equivariant and retains its original character.

The inner boundary also meets the fixed surface. In the positive node
chart it is
\[
 z=V=0,\qquad (S_0,S_1,T_1)/\mathbb C^*,
 \qquad \text{weights }(1,1,-1).
\]
The invariant radius on this surface is
\(R=\|(S_0,S_1)\||T_1|\). Its level \(R=\varepsilon\) is the
circle bundle of \(O(-1)\), with the following literal \(S^3\)
coordinate. Use the unique positive auxiliary gauge \(\|S\|=1\),
write \(T_1=\varepsilon e^{i\phi}\), and set
\[
                  p=e^{i\phi}(S_0,S_1)\in S^3.
 \tag{EA.14}
\]
The positive-weight spinor is \((z,\overline V)\). In this same
gauge its actual boundary frame is
\[
 \left(e^{i(a-1)\phi}z,e^{ia\phi}\overline V\right).
 \tag{EA.15}
\]
Before positive normalization the first component is
\(T_1^{a-1}z/\varepsilon^{a-1}\), and the second is
\(\|S\|^{2a}T_1^a\overline V/\varepsilon^a\).
The displayed positive factor in the second component is required for
full auxiliary invariance; no phase has been suppressed.

Consequently the inner end is not identified here with the bare ruling
mapping torus. Its stable portion has the precise (EA.13) arrow and
the ruling change of EA.4, while its fixed portion has the \(S^3\)
and normal frame (EA.14)--(EA.15). The complete mixed-face construction below joins these portions with their actual boundary orientations.
The certificate \path{code/part3_fourfold/source_zero_cap_end.py}
checks the admitted finite characters and the exact metric/frame weights.

## EA.9. The actual cyclic graph reset and its charged-chart continuation

The common graph identity of EA.4 does not identify consecutive graph
coordinates. Here is the missing reset, with its line map. Use the
marked source-resolution coordinates
\[
 A=Dz_s,\quad C=Bz_s,\quad
 v=(B-Dz_s)/2,\quad X=Bz_s,
\]
and set
\[
 F_2=1-Bz_s^3-(1-2v)z_s^2.
\]
The next negative-G translation has the exact source coordinates
\[
 X'=F_2/z_s^2,\quad A'=-F_2/z_s^3,\quad
 B'=B-Dz_s-F_2/z_s^3,\quad D'=-B'/z_s.
 \tag{EA.18}
\]
They satisfy \(A'B'=X'D'\), preserve \(v\), and preserve the full
source base coordinate
\(T=D-X^2-(1-2v)X\). In the next common Cox gauge take
\[
 (\widetilde t_0,\widetilde t_1)=(1,-z_s),\qquad
 (\widetilde s_0,\widetilde s_1)=(A',D').
 \tag{EA.19}
\]
In the current target gauge \((s_0,s_1)=(z_s,1)\), the meromorphic
line coefficient is \(\xi/z_s^a\). In the next domain gauge it is
\(\widetilde\xi(-z_s)^a\). Therefore the exact coefficient arrow is
\[
            \widetilde\xi=(-1)^a z_s^{-2a}\xi.
 \tag{EA.20}
\]
For the actual reduced line, this reads
\(\widetilde\xi=\xi/z_s^4\), after the retained Cartier map
\(r\) at both ends. Equations (EA.18)--(EA.20) give the reset,
rather than replacing it by the bare projective ruling.

Its effect on the associated-node chart is already nontrivial on the
central proper component. Write
\[
 X=s^2-1,\quad Y=s(s^2-1),\quad z_s=1/s,\quad
 B=s(s^2-1),\quad D=s^2(s^2-1).
\]
Near its \(s=-1\) node, the analytic square root in RT.2 is
\(\sigma=-s\). Substitution in the literal functions
\[
 F_+=\frac{(\sigma+1)(s_1-s_0)
                -s_0^2(t_0+t_1)/(\sigma+1)}2,
\]
\[
 F_-=\frac{(\sigma+1)(t_0+t_1)
                -t_1^2(s_1-s_0)/(\sigma+1)}2
\]
gives \(F_+=2,F_-=0\). Thus the finite associated coordinate
\(z_n=\xi/F_+\) is nonzero. At the next target, (EA.18) has
\(\widetilde s_0=\widetilde s_1=0\), whereas
\(\widetilde\xi=\xi s^4\ne0\). Its analytic square root has
value one, and
\[
             \widetilde F_+=0,\qquad
             \widetilde F_-=1-1/s.
\]
Consequently \(z_n\) goes to infinity. The reset enters the
complementary \(U\ne0\) charge-a chart. It does not close inside
the finite nonzero charge-\((a-1)\) chart. This is the exact reason
the Euler sequence \(2M\oplus2M^{-1}\) from that chart alone has
not been descended over the entire cyclic end.

There is nevertheless a literal continuation from the resulting
charged chart. Use the complementary small-resolution equations
\[
                  S_0=Uw,\qquad V=wT_0.
\]
In its \(U=1\) gauge the remaining coordinates are
\((w,S_1,T_1,T_0)\), and the full source functions from RT.2 are
\[
 q=wT_0,\qquad
 v=S_1T_1+\frac{T_1w-S_1T_0}{2\sqrt{1+S_1T_1}}.
 \tag{EA.21}
\]
The primary \(V=1\) chart has coordinates
\((S_0,S_1,T_1,z_n)\). Its source functions are exactly (EA.21)
under
\[
                (S_0,S_1,T_1,z_n)=(w,S_1,T_1,T_0).
 \tag{EA.22}
\]
This map has a specific chain meaning. On \(U_j\ne0\), the
actual adjacent node overlap is
\[
 U_{j-1}=c_\lambda qU_j,\qquad
 V_{j-1}=(c_\lambda U_j)^{-1},\qquad c_\lambda=2\lambda.
 \tag{EA.23}
\]
At \((U_j,V_j)=(1,q)\), apply the retained source-fibre scalar
normalization \((U,V)\mapsto(c_\lambda^{-1}U,c_\lambda V)\).
The result is \((q,1)\), precisely (EA.22). Thus this is a node
chart overlap with index \(j\mapsto j-1\), not an additional
cap or an extra charged point. In a forward B cut its index cancels
the preceding \(j\mapsto j+1\) in (EA.11). In particular the
charged origin in these two descriptions is one point, and must
not be counted twice.

Both gauges retain the same effective physical weights, in the
ordered coordinates of (EA.22),
\[
                   (-1,-1,+1,+1)/a,
\]
and the same residual \(\mu_a\) action. The displayed coordinate
arrow is complex linear on these charged coordinates and preserves
their real eight-dimensional orientation. Conjugating its two
negative physical-weight coordinates gives the same positive Hopf
projection at both ends. Its physical line is \(O(-a)\), with
the outward-meridian dual \(O(a)\). A charged ball is carried by
(EA.22), with this full normalization retained; its transported
truncation is used if the original radii differ. This fixes the
boundary orientation against the local charged model of RT.10.

The source functions \(q,v\) in (EA.21) are unchanged throughout.
On the finite cap, (EA.7)--(EA.10) carry the same primitive map,
including \(q=q_\infty^{-1}h_\infty\), the actual \(z_\infty^m\)
factor in the reduced line, and its trivial commutator with
\(A_0\). The physical normalization in (EA.23) commutes
with this full root/line square. Both norm signs and every retained
finite character remain.

These are the cyclic chart transition and local charged orientation used in the complete finite-domain attachment below.
The exact source, line, and charged-chart identities are executed in
\path{code/part3_fourfold/source_zero_associated_reset.py}.

## EA.10. The retained scalar winding in the adjacent-node arrow

The finite-cut construction in EA.5 starts at fixed nonzero
\(\lambda\). For the original rescaled source loop, the exact same
overlap has
\[
 c_\lambda(v)=2\lambda_0v^{km},\qquad
 (U,V)\longmapsto(c_\lambda(v)^{-1}U,c_\lambda(v)V).
 \tag{EA.24}
\]
Thus its two characters have source-parameter windings \(-km\)
and \(+km\). This map is not asserted to extend at \(v=0\) in
those old coordinates. Its full collar derivative is retained: it is
the diagonal character map followed by a rank-one factor
\(I-\eta\otimes d\log c_\lambda\), where \(\eta\) is the
physical complex orbit field and
\(d\log c_\lambda(\eta)=0\). The latter factor is invertible
through the explicit homotopy
\(I-t\eta\otimes d\log c_\lambda\); the diagonal character and
its winding are not removed by this homotopy.

The comparison with a fixed-scalar boundary uses the actual two-parameter
family, not an extension of (EA.24). Write \(\lambda=r^m\). Its
cap generator is \(A(v,r)=r^nA_0(v)\), and the ordinary-to-cap
map on the logarithmic r cover is
\[
 F(v,\nu)=F_0(v)+n\nu s_\infty\delta,\qquad
 \nu=\log r/(2\pi i).
\]
Here \(F_0(v)\) is the complete extending annular map of RCZ.5--7,
with its integral cochain fixed at the reference fibre. The positive
r deck has the full arrows \(q_1^n\) and \(h_\infty^n\), since
\(q_1=q_\infty^{-1}h_\infty\), and
\[
          F(v,\nu+1)\,q_1^n=h_\infty^n F(v,\nu).
 \tag{EA.25}
\]
The equation retains both norm signs, the fixed finite character,
and every source/line unit. The same source and line Cartier maps
are used over both parameter directions; the base-only physical
scalars commute with them. The cap division and \(F_0\) have their
stated holomorphic source-parameter extensions, so their source-loop
endpoint is retained literally.

On the boundary, \(r=v^k r_0\). In this actual product-parameter
family the diagonal loop is homotopic to the source loop at fixed r
followed by k scalar-root loops at the comparison source. The based
homotopy carries all the endpoint squares (EA.25). Hence its return
class is the fixed-scalar source return plus the actual
\(kA_{\rm scalar}\) term, in the same transported fan. This is
the geometric parameter-loop relation already used in K58; no
class in \(\Theta_7\) is divided. The fixed-scalar attachment is constructed by the complete domains and collar maps below.

## EA.11. Chamber ownership of the two charged descriptions

The coordinate identification (EA.22) is retained together with its two
auxiliary chambers. For the primary resolution
\(U=S_0z,T_0=zV\), the auxiliary and physical weights on
\((S_0,S_1,T_1,z,V)\) are respectively
\[
 (1,1,-1,a-1,-a),\qquad(0,0,0,1,-1).
\]
For the complementary resolution \(S_0=Uw,V=wT_0\), the weights
on \((U,w,S_1,T_1,T_0)\) are
\[
 (a,1-a,1,-1,-1),\qquad(1,-1,0,0,0).
\]
Thus, for a=2, the primary positive chamber is the actual
\(\operatorname{Tot}(O(-1)\oplus O(-2)\to\mathbb P^2)\)
of RT.9. Its z=1 origin has charge one. The primary V=1 origin
instead lies in the negative auxiliary chamber and has charge two.
The complementary U=1 origin lies in its positive chamber and also
has charge two. Equation (EA.22) identifies the last two charts;
it does not place a charge-two origin in the primary positive chamber.

In either charged gauge, maintaining U=1 or V=1 under the physical
circle uses the auxiliary factor of exponent \(-1/a\). The ordered
remaining coordinates therefore have the same physical weights
\((-1,-1,+1,+1)/a\). Their residual auxiliary \(\mu_a\)
characters agree modulo a. The map (EA.22) is complex linear in
those coordinates, preserves their real eight-dimensional orientation,
and carries the physical line \(M=O(-a)\) literally.

The ungauged continuation, on the complementary chart U nonzero,
is the explicit map
\[
 (U,w,S_1,T_1,T_0)\longmapsto
 (S'_0,S'_1,T'_1,z',V')=(Uw,S_1,T_1,UT_0,U^{-1}).
 \tag{EA.26}
\]
Its inverse is \(U=(V')^{-1},w=S'_0V',T_0=z'V'\), with
S1,T1 unchanged. It preserves the auxiliary action and the physical
circle separately. It also preserves q and the full v in (EA.21).
At U=1 it is exactly (EA.22). It is the adjacent-node arrow with
the full scalar normalization already specified, not the naive
exchange of U and V on the ungauged associated-node space. A
radial defining function on either charged quotient chart can be
transported by (EA.26), with its entire derivative. Choosing the
retained or excised side of that transported function remains part
of the compact-cut construction.

Chamber names alone do not determine the boundary normal. On the
normalized charged gauges the two actual moment functions are
\[
 \mu_{\rm comp}=a+(1-a)|w|^2+|S_1|^2-|T_1|^2-|T_0|^2,
\]
\[
 \mu_{\rm prim}=|w|^2+|S_1|^2-|T_1|^2
                         +(a-1)|T_0|^2-a.
\]
Their sum is
\[
 (2-a)|w|^2+2|S_1|^2-2|T_1|^2+(a-2)|T_0|^2,
\]
and is not identically zero. The sign of a charged boundary in a
compact bordism must therefore be taken from the explicitly retained
or excised ball, with its outward radial normal. It is not obtained
by negating one moment function. These weight and moment identities
are checked in \path{code/part3_fourfold/source_zero_chamber_ledger.py}.

## EA.13. Canonical complex spin-c and the explicit determinant lifts

The lower charged arm carries the canonical complex spin-c structure,
with its actual physical associated line. It is not assigned a spin
structure by its rational characteristic classes. In particular, the
two possible lifts over the fundamental group of an RP3 collar are
kept distinct until the actual chart maps have been carried.

There are explicit determinant arrows for those maps. In the source
reset (EA.18), use source coordinates \((B,D,z_s)\) on the first
small-resolution chart, and \((A',D',w')\), \(w'=-z_s\), on
the second. Direct differentiation gives
\[
 \det\frac{\partial(A',D',w')}{\partial(B,D,z_s)}=-1.
\]
Including the exact coefficient (EA.20), with the Cartier r map at
both ends for a=2, the four-dimensional complex Jacobians are
\[
  J_1=z_s^{-2},\qquad J_2=-z_s^{-4}.
 \tag{EA.27}
\]
The determinant square roots used to transport the spin reduction
in these coordinate trivializations are the literal functions
\(z_s^{-1}\) and \(i z_s^{-2}\), respectively. Their inverses
are used on the reverse arrow. These functions retain the full
source winding; no choice of a small logarithm of z_s is made.

For (EA.26), in the displayed ordered five coordinates the complex
Jacobian is the constant -1. The map intertwines the auxiliary
Euler vector field, so contraction of the five-form with that
field gives the same constant -1 on the quotient canonical
four-form. The fixed square root i carries its spin reduction.
On the normalized charged covers, the four-coordinate arrow is
the identity; its residual mu-a character is the one in EA.11.
These two descriptions agree by the actual auxiliary gauge and
its determinant. They do not permit an additional sign character
of the RP3 fundamental group.

More explicitly, on the lower arm the normal bundle is
\((S^3\times\mathbb C^2)/\{\pm1\}\), with the indicated
minus action on both normal coefficients. Its complex determinant
is trivialized by their ordered wedge. The canonical complex
spin-c lift selects a specific spin lift with respect to that
trivialization. With Clifford convention \(e_i^2=-1\), follow
\(\operatorname{diag}(e^{it},e^{it})\), \(0\le t\le\pi\).
Its canonical spin-c endpoint is
\[
 [e_1e_2e_3e_4,-1]=[-e_1e_2e_3e_4,1].
 \tag{EA.27a}
\]
Thus the normal mu2 lift is the specified \(-\omega_4\), not an
arbitrary choice between \(\omega_4\) and \(-\omega_4\).
The other complex two-plane block has the same canonical lift;
their product is \(+\omega_8\), in agreement with the full
charged-cover computation below. Equation (EA.22) is the identity
on these ordered cover blocks. The reset carries their embedded
collars and normal derivative by (EA.27), so this local lift is
transported together with the physical line.

The physical normalization is also carried at the level of its
lift. At a=2, along a chosen path of nonzero scalars d from one
to its actual value, the charged-cover derivative has diagonal
characters
\[
 (d^{-1/2},d^{-1/2},d^{1/2},d^{1/2}).
 \tag{EA.28}
\]
The square roots here are continued along that very path. A full
positive phase turn gives the endpoint -I4. Its canonical complex
spin-c action on \(\Lambda^{0,*}\mathbb C^4\) is
\((-1)^{\deg}\). The determinant-one path in (EA.28), whose
four angles are \((-\pi,-\pi,\pi,\pi)\), has exactly that
spin endpoint: on an occupation vector \((n_1,n_2,n_3,n_4)\)
its sign is
\[
 (-1)^{-n_1-n_2+n_3+n_4}=(-1)^{n_1+n_2+n_3+n_4}.
\]
It therefore closes through the specified canonical residual mu2
action. Replacing the root by its other branch is this same deck
map with this specified lift, not an unrecorded alternative spin
structure. The physical line remains M, not its dual; its charged
Hopf class is \(O(-a)\).

For a nonconstant scalar the full derivative also contains the
rank-one factor in EA.10. Its displayed homotopy is based at the
actual diagonal arrow and carries the chosen lift. The theta and
Morse units in TL.1--2 have extending logarithms on the complete
bidisc; their determinant and line maps are carried by those
logarithms. The actual h period and the Cartier r factors precede
this unit homotopy, so their integral characters are not removed.
On the finite cap the canonical complex spin-c maps are those of
the full root/line F0 square in EA.12; its finite character remains
part of the map.

The exact determinant computations and the sixteen spinor endpoint
checks are in \path{code/part3_fourfold/source_zero_spin_chart.py}.
These are the actual local lift data carried on the complete finite attachment below.

## EA.14. A full charged shape matching the lower arm

The regular part RT.20 has its two explicit arms; the actual complete retained domain is EA.48, which also retains its upper fibre and charge-one point. In its lower arm use the primary V=1 gauge and write
\(x=(S_0,S_1,z)\),
\[
 H=\|x\|^2,\quad b=H|T_1|^2,\quad c=H^2,
 \quad u=\frac b{b+c},\quad
 \sigma^2=\|x\|^2+|T_1|^2.
\]
The actual disk-bundle defining function satisfies the exact identity
\[
                  \rho=\sigma^2\sqrt{1-u}.
 \tag{EA.29}
\]
Indeed its square is \(b+c\), and
\(\sigma^4(1-u)=H(H+|T_1|^2)=b+c\).
On the lower small-R arm, u is at most the chosen ratio
\(\varepsilon^2/r_0^2<1/4\). Choose a smooth invariant angular
cutoff chi equal to one on a neighbourhood of that closed arm and
supported in \(u<1/2\). Set
\[
             f=1-\chi(1-\sqrt{1-u})>0.
\]
Then the full charged hypersurface \(\sigma^2f=\rho_0\)
agrees literally with \(\rho=\rho_0\) near the arm. It is a
complete smooth star-shaped hypersurface on the charged cover,
invariant under the residual mu2 and the physical circle. The
normal equality on that neighbourhood is an equality of defining
functions, including their derivatives, not only an equality of
zero sets.

Use the positive-width compact annulus
\[
 \mathcal A_f=\{\rho_0/2\le\sigma^2\le\rho_0/f\}/\mu_2.
 \tag{EA.30}
\]
It is a smooth interval bundle with disjoint boundary faces. Its
inner boundary is a round charged link; its outer boundary is the
full transported shape. All q and v functions, the physical line,
and the canonical complex spin-c structure are their restrictions
from the actual charged chart. No radial map is asserted to
preserve q or v. The physical circle is free on this annulus:
its nonzero coordinate weights are all plus or minus one after
the retained residual mu2 is accounted for. Product connections
on its collars therefore show that the outer shape and round
charged link have equal physical characteristic integrals.

Equation (EA.26) pulls the entire outer defining function to the
complementary U chart. It transports the outward radial normal
and the retained/excised side exactly, and it carries the lifts
in EA.13. The earlier coincident-face proposal with inner radius
rho0 is not used: (EA.30) uses rho0/2 everywhere, including where
f=1.

This shape comparison still respects the chamber distinction.
The lower arm itself lies in the common stable overlap with the
primary positive chamber. The charge-two origin filling the full
shape belongs to the primary negative chamber. The complete domain and horn chain EA.48--52 specify where the complement of the lower arm lies among the boundary faces. The charged shape is not
glued as an additional positive GIT chart. Thus (EA.29)--(EA.30)
fix the radial normal and its spin-c/line data for the full mixed-face attachment EA.21--22.

## EA.15. The native finite-strip quaternion and the charged seam

The native ruling coordinates are taken after the actual analytic
Morse-Cox map of RT.2 and the full two-node refinement in EA.17 below.
To make the first arrow explicit, write its old
pairs as s=(s0,s1), t=(t0,t1), and put
\[
       S=(F_+,s_0),\qquad T=(F_-,t_1).
 \tag{EA.31}
\]
This is an auxiliary-equivariant analytic isomorphism with the
inverse already displayed in RT.2. It preserves both ruling
ideals. Indeed, writing \(d=(\sigma+1)/2\),
\[
 F_+=d s_1+s_0\left(-d-
                  \frac{s_0(t_0+t_1)}{2(\sigma+1)}\right),
\]
\[
 F_-=d t_0+t_1\left(d-
                  \frac{t_1(s_1-s_0)}{2(\sigma+1)}\right).
\]
The two coefficient determinants are -d and d, both units.
Consequently (F+,s0)=(s0,s1) and (F-,t1)=(t0,t1) as ideals,
so the map lifts both projective rulings. It keeps the common
line coefficient xi, with the actual r maps in the degree-two
sector. Its full complex Jacobian is -sigma, an extending unit.
The source functions are exactly those of RT.2, expressed in
these coordinates. This is the first source-preserving chart arrow,
not a substitution based only on matching weights. Its displayed
pairs are intermediate selected-node coordinates. EA.17 carries
them to the full two-node pairs; the S,T in the norm and quaternion
formulas below denote those final pairs. The extra source/line
units and their inverses are kept in every reset and cap composition.

Use the divisor metrics transported by (EA.31) for the finite
end. In these metrics the exact EA.12 ratio is
\(N_T=R^aN_S\), \(R=\|S\|\|T\|\). On the stable collar
the old and transported metrics have a bounded positive ratio;
its actual real logarithm, and its transported cap average, give
the metric interpolation. No phase or period map is changed.
The positive scaling in EA.13 leaves the unit directions of S
and T unchanged.

Set, in these actual pairs,
\[
 u=S_0+jS_1,\qquad c=T_0+j\overline{T_1},\qquad
 \widehat u=u/\|S\|,\quad\widehat c=c/\|T\|,
\]
\[
 q_H=\widehat u\widehat c,\qquad
 h=\widehat u i\widehat u^{-1},\qquad
 k=\widehat c^{-1}i\widehat c.
 \tag{EA.32}
\]
Thus the actual t-ruling to s-ruling map is
\(h=q_H k q_H^{-1}\), with its full normal coordinate qH.

In the primary V=1 charged chart, T0=z. Conjugate the two
negative physical-weight coordinates and choose the explicit
constant unitary target coordinates
\[
 p=\overline{S_0}+j\overline{S_1}=j u j^{-1},\qquad
 q_{\rm alt}=z-jT_1=j\overline c j^{-1}.
\]
Both have the same positive right physical-circle action, with
the retained common mu-a quotient. The exact projective ratio is
\[
 w_{\rm alt}=p q_{\rm alt}^{-1}
       =\frac{j(u c)j^{-1}}{\|T\|^2},\qquad
 g_{\rm alt}=\frac{w_{\rm alt}}{|w_{\rm alt}|}
       =j q_H j^{-1}.
 \tag{EA.33}
\]
Its two Hopf base coordinates are
\[
 h_{\rm alt}=-j k j^{-1},\qquad
 h'_{\rm alt}=-j h j^{-1}.
 \tag{EA.34}
\]
Therefore \(h'_{\rm alt}=g_{\rm alt}h_{\rm alt}
g_{\rm alt}^{-1}\) is precisely the native inverse ruling
map with the stated constant arrows. Each minus in (EA.34)
is the antipodal map of S2, of degree -1; neither is discarded.
The exact Hopf lift is
\[
       g_{\rm alt}\frac{q_{\rm alt}}{|q_{\rm alt}|}
                           =\frac p{|p|}.
 \tag{EA.35}
\]

A second explicit charged atlas uses instead
\(q_{\rm root}=T_1+jz=j q_{\rm alt}\).
This is the literal constant complex-linear map
\((z,-T_1)\mapsto(T_1,z)\), with complex determinant one.
In that exact coordinate choice the dictionary becomes
\[
 g_{\rm root}=-j q_H,\qquad h_{\rm root}=-k,
 \qquad h'_{\rm root}=-j h j^{-1},
 \qquad
 g_{\rm root}\frac{q_{\rm root}}{|q_{\rm root}|}
                               =\frac p{|p|}.
 \tag{EA.36}
\]
This gives the literal comparison between the two charged atlases. The other quaternion
hemisphere always retains \(w'=w^{-1}\), including its actual
four-dimensional base orientation. The identity reconstructing
the same charged point is
\((p,q)=(rwu,ru)=(r'u',r'w'u')\), with \(r'=|w|r\),
and the positive radius is the actual solution on the transported
shape of EA.14. Hence every q-source and v function is literally
unchanged on the overlap. The inverse of (EA.31) carries that
statement back to the original Weierstrass/Cox chart.

For a=2 the associated physical line map is
\([u,z]\mapsto z u^{\otimes2}\) into O(-2); the Hopf arrow
(EA.35) intertwines it and its normal coefficient frame. The
canonical spin-c and determinant lifts are those of EA.13;
the analytic Morse unit -sigma has its extending logarithm
after its fixed constant sign is retained. The full F0 cap
square and the scalar factor in EA.23 accompany this seam.
The exact quaternion and ideal identities are executed in
\path{code/part3_fourfold/source_zero_native_charged_seam.py}.

This is the charged/native seam map. Its hemisphere inversion and both sphere antipodal maps are retained in the complete finite-strip boundary calculation EA.47 below.

## EA.16. Entire finite faces and the retained line coefficient

The norm inequalities are first imposed on the complementary
charged chart, after the literal chain-index change and the source
reset. Its common line coefficient is \(\xi=U_j\). Fixing
\(U_j=1\) gives the residual mu-a cover with actual source pairs
\[
                 S=(w,S_1),\qquad T=(T_0,T_1).
\]
The invariant norm functions in this gauge are exactly
\[
                  N_t=\|T\|^a,\qquad
                  N_s=\|S\|^{-a},\qquad R=\|S\|\|T\|.
 \tag{EA.37}
\]
This gauge is taken only after the actual node reindex; it is not
an assertion that the primary line coordinate U equals one.
Indeed (EA.26) sends it to the primary chart V'=1, with the same
ordered pairs \(S'=(w,S_1)\), \(T'=(T_0,T_1)\). Before that
gauge the transported common coefficient is
\[
                         \xi=(V')^{-1},
 \tag{EA.38}
\]
whereas the primary node coefficient is \(U'=q/(V')\).
Consequently the transported norms there are
\(|V'|^{-1}\|T'\|^a\) and
\(|V'|^{-1}/\|S'\|^a\). This retains the q-factor and is the
exact reason the bare inequalities in (EA.37) apply after the
specified arrow. The source-fibre constant c-lambda, its phase,
and the index j to j-1 are those in (EA.23); they precede (EA.38).

Choose a sufficiently small charged radius r. The two entire
closed finite faces are
\[
 H_t(r)=\{N_t=r^a,\ R\le r^2\}
       =(D^4_S(r)\times S^3_T(r))/\mu_a,
\]
\[
 H_s(r)=\{N_s=r^{-a},\ R\le r^2\}
       =(S^3_S(r)\times D^4_T(r))/\mu_a.
 \tag{EA.39}
\]
In the positive charged quaternion coordinates of EA.15 these
are respectively \(|p|\le|q|=r\) and
\(|q|\le|p|=r\). Their common face is
\(|p|=|q|=r\), with the exact quaternion and Hopf-line
transition (EA.33)--(EA.36). Thus the comparison specifies the
full two orbit charts, not only their unit-quaternion seam.
Rounding the product-ball corner uses its two actual norm defining
functions. Its charged shape is then compared with the prescribed
lower radial arm by EA.14, by ambient inclusion with q,v retained.

On R positive the end normalization from Ht to Hs is
\[
             d=(R/r^2)^a,\qquad
             (S,T)\longmapsto(d^{-1/a}S,d^{1/a}T).
 \tag{EA.40}
\]
It sends \((\|S\|,\|T\|)=(s,r)\) to \((r,s)\),
preserves all source auxiliary invariants and hence q,v, and is
the actual positive physical scaling of the common line before
refixing its gauge. It leaves the unit directions used in qH
unchanged. At a positive inner cut R=epsilon the factor is a
single positive constant. No extension of (EA.40) at R=0 is
claimed: the two cores remain the distinct full-face boundary
pieces in (EA.39).

The oriented side follows from the actual contracting direction.
Let eta denote the positive physical real-orbit field on this
charged cover, up to its positive factor 1/a:
\[
                       \eta=-S\partial_S+T\partial_T.
\]
The forward suspension is contracting in its physical line, so
its normalized real direction is -eta. The retained constant
phase acts tangentially and carries the lift in EA.13. On Ht,
-eta differentiates \(\|T\|^2-r^2\) to \(-2r^2\): it
enters the product ball. On Hs it differentiates
\(\|S\|^2-r^2\) to \(+2r^2\): it exits. If each end is
oriented by contraction with the forward direction, the target
minus source end chain therefore equals the positively oriented
boundary of
\[
                       (D^4_S(r)\times D^4_T(r))/\mu_a.
 \tag{EA.41}
\]
This comparison uses the full real eight-dimensional coordinate
arrow. The two negative complex conjugations preserve that
orientation; the S2 antipodal maps and the hemisphere inversion
in EA.15 are retained within it. Thus no side is selected merely
from the name of a ruling or an auxiliary chamber.

All maps on these faces are the node-chart maps in EA.9, followed
by the source/Cartier map of TL and the full F0 cap square of
EA.12. The physical associated line and its canonical spin-c
lift are transported by those same maps. The exact finite-face
norm and side computations are in
\path{code/part3_fourfold/source_zero_full_faces.py}.
The complete domain and mixed-face maps in EA.19--22 insert these full faces into the compact period strip and retain the whole fixed cap.

## EA.6. The reduced positive moment model as an actual bundle

For \(a=2\), the positive auxiliary coordinates of the associated node
chart are \((S_0,S_1,z)\), each of weight one. The negative coordinates
\((T_1,V)\) have weights \((-1,-2)\). The strict derivative in EA.5
shows that the level \(\mu_{\rm aux}+K\mu_\delta=c>0\) meets each
positive-stable auxiliary complex orbit exactly once modulo its compact
circle. It therefore has the literal smooth quotient map to
\[
 \operatorname{Tot}\bigl(O(-1)\oplus O(-2)\longrightarrow
                         \mathbb P^2_{[S_0:S_1:z]}\bigr).
 \tag{EA.16}
\]
Its physical action is the one induced by weight one on \(z\), weight
minus one on \(V\), and weight zero on the remaining coordinates. This
keeps the fixed \(O(-1)\) surface over \(z=0\) and the isolated point
\([0:0:1]\), rather than replacing them by a putative free end.

In the exact node-adapted source coordinates, \(q_1-q_2=v u_v(v)\),
where \(u_v(0)\ne0\). The parameter change
\(\widetilde v=v u_v(v)\) is an actual biholomorphism of discs.
On (EA.16) its map is
\[
                    \widetilde v=S_0zV-S_1T_1.
 \tag{EA.17}
\]
The two coefficients of the two fibre coordinates vanish together only
at \([1:0:0]\) and \([0:0:1]\). In each corresponding affine base
chart, (EA.17) is exactly a nondegenerate four-variable form
\(xw-yz\). Thus both critical points and their actual circle actions
remain explicit. The physical fixed surface meets the first of these
points; the second is the isolated fixed point.


The actual radial and product cuts are compared by the complete domain EA.19, rather than by identifying their defining functions.


## RT.13. A compact cut region with its two actual corner arms

We specify the compact region before making any end identification.
In the positive reduced chart put
\[
 H=|S_0|^2+|S_1|^2+|z|^2,\quad
 \rho^2=H|T_1|^2+H^2|V|^2,\quad
 R^2=(|S_0|^2+|S_1|^2)(|T_1|^2+|zV|^2).
                                                        \tag{RT.19}
\]
All three displayed combinations used below are invariant under
the full auxiliary complex action; rho is the actual Fubini--Study
disk-bundle norm on W. Choose r0>0 and epsilon>0 with
0<epsilon2/r0^2<1/4 and take
\[
       \mathcal A_{\varepsilon,r_0}
       =\{\rho\le r_0,\ R\ge\varepsilon\}\subset W.   \tag{RT.20}
\]
This is compact because it is closed in the proper disk bundle over
CP2. It is circle invariant. Its maps q and vtilde are the restrictions
of the actual invariant polynomials; the region makes no change to
those maps or the physical line.

Here is a direct regularity and corner calculation. Set
\[
 A=|z|^2/H,\qquad b=H|T_1|^2,\qquad c=H^2|V|^2.
\]
Then rho2=b+c and R2=(1-A)(b+Ac). On the sphere rho=r0 put
t=b/(b+c). Thus
\[
 \frac{R^2}{r_0^2}=(1-A)\{A+(1-A)t\}=:f(A,t).       \tag{RT.21}
\]
The derivative in the simultaneous fibre radial direction is
2R2, so R=epsilon is regular. On the radial sphere, the only
nonzero critical ratios of R2/r0^2 are 1/4 and 1. Indeed
partial_t f=(1-A)^2, so an interior critical point cannot occur.
On T1=0 the function is A(1-A), whose interior critical value is
1/4. On V=0 it is 1-A, with only endpoint critical values 0,1.
The remaining coordinate endpoints give 0 or 1. Consequently the
two faces in (RT.20) meet transversely. Their corner has the literal
equations rho=r0,R=epsilon, and may be smoothed by an invariant
rounding in these two regular defining functions.

The portion \(\rho=r_0,\ R\le\varepsilon\) has exactly two disjoint components.
Write \(\eta=\varepsilon^2/r_0^2\) and
\[
 A_\pm=(1\pm\sqrt{1-4\eta})/2,
\]
the inequality f(A,t)<=eta permits only A<=A_- or A>=A_+.
For A>=A_+, increasing A to one decreases f; this component is a
tubular neighbourhood of the core over [0:0:1], with T1,V on their
unit three-sphere. For A<=A_-, decreasing both A and t decreases
f. To check the latter assertion on the allowed sublevel, substitute
t<=(eta-A+A2)/(1-A)^2 in partial_A f; its lower bound is
(1-A-2eta)/(1-A)>0. This component is a tubular neighbourhood of
z=T1=0, with V on the circle bundle O(-2) over P1.

The two core total spaces and their normal arrows are explicit.
At the first core, fix z=1. The core is S3 in (T1,V), the normal
coordinates are (S0,S1), and the physical weights are respectively
(+1,+1) and (-1,-1). At the second core, use V=1 with its actual
residual mu2. Its core is S3_(S0,S1)/mu2=RP3 and its normal disk
bundle is
\[
 (S^3\times D^4)/\{(S,c)\sim(-S,-c)\}.             \tag{RT.22}
\]
The physical weights in that gauge are -1/2 on the core coordinates
and +1/2 on the two normal coordinates (T1,z). Its principal circle
and physical line therefore retain charge two. No free quotient by
mu2 is removed from this description. The first core retains charge
one. Both corner arms are thus part of the compact comparison;
neither is silently replaced by an ordinary sphere cap.



## EA.19. Explicit upper-arm filling in the retained positive chamber

The region RT.20 alone excludes the primary charge-one point.
The finite construction uses the following additional actual
domain in the same positive quotient W. Choose
\(2\varepsilon<r_1<\rho_0\) and put
\[
 \mathcal D=\{\rho\le r_1\}\ \cup\
 \{r_1\le\rho\le\rho_0,\ R\ge\varepsilon\}\ \cup\
 \{r_1\le\rho\le\rho_0,\ A\ge1/2\},
 \qquad A=|z|^2/H.
 \tag{EA.48}
\]
This is a compact subset of the actual disk bundle W. On A=1/2,
RT.21 gives \(R^2/\rho^2\ge1/4\). For rho at least r1 the
artificial A boundary therefore lies strictly in R>epsilon,
already retained by the middle piece. It supplies no additional
boundary face. Below rho=r1 the entire disk bundle is retained.
All intersections are identity intersections in the same smooth
positive quotient, not identifications of different GIT limits.

The added upper portion is in the literal z=1 chart. There
\(A\ge1/2\) means \(|S_0|^2+|S_1|^2\le1\), and
\[
 \rho^2=(1+\|S\|^2)|T_1|^2
                 +(1+\|S\|^2)^2|V|^2,
 \qquad R^2=\|S\|^2(|T_1|^2+|V|^2),
\]
\[
             q_1=S_0V,\qquad
             \widetilde v=S_0V-S_1T_1.
 \tag{EA.49}
\]
Thus the full upper fibre S=0 with rho at most rho0 is present,
including its unique charge-one origin. A sufficiently small
round ball around that origin lies entirely in rho<r1 and in
this single chart; it is the one ball deleted in EA.47. Its
physical weights and canonical spin-c maps are exactly those of
RT.15. No second origin is introduced by an overlap.

The entire zero section, and hence the exceptional disk of the
fixed surface, also lies in rho<r1. On the fixed surface z=V=0
one has R=rho. Its part above r1 therefore belongs to the
R>=epsilon piece; the whole fixed surface inside rho<=rho0
is retained. It is attached to the rest of F and capped only by
the global C0 construction. There is no separate RT.10 handle.

The sole removed horn of (EA.48) is
\(r_1<\rho\le\rho_0,\ A<1/2,\ R<\varepsilon\).
At every rho in this interval it is the lower arm, since
\(\varepsilon^2/\rho^2<1/4\). Its boundary consists of the
two specified rho cuts and the actual R=epsilon side. The
charged defining-function and full-face maps EA.29--41 are
applied to those cuts and this side, with their transported
functions. They retain q,v, the physical line and the stated
spin lift. Invariant rounding uses only these regular defining
functions, with the A-boundary absent as just proved.

Finally the outside separation is quantitative in the final
two-node pairs:
\[
 |q_1|+|q_2|=|S_0T_0|+|S_1T_1|
                       \le\|S\|\|T\|=R.
\]
Since \(q_1-q_2=v u_v(v)\) is the actual base-coordinate
change, on the chosen fixed bidisc
\(|v|\le C R\) and \(|T|\le C'R\).
The R<=epsilon modification can consequently be chosen disjoint
from both the prescribed outer source-parameter circle and the
outer source-base boundary. Their actual family maps remain
unchanged. This gives the upper-domain ownership in the complete boundary ledger.

## EA.20. The complete lower-horn boundary chain

Let H be the closure of the lower horn removed in EA.48. Its
three seven-dimensional faces are the outer rim Hr at rho=rho0,
the floor Hf at rho=r1, and the side Hs at R=epsilon. Orient H
by the ambient complex orientation. With positive rho and R
coordinate conventions its boundary chain is
\[
                       \partial H=H_r-H_f+H_s.
 \tag{EA.50}
\]
The retained domain D consequently has
\[
              \partial D=\Sigma_{\rho_0}-H_r+H_f-H_s.
 \tag{EA.51}
\]
The rim is removed from its outer radial face; the floor and
side are actual remaining boundary faces, not extra copies of
the charged end. The artificial A=1/2 face is absent by EA.19.

The entire horn has V nonzero, since its lower-arm parameter
u is at most \((\varepsilon/r_1)^2<1/4\). Apply the actual
EA.26 charged map, retaining the c-lambda normalization, to all
of H. Choose the angular cutoff to be one for
\(u\le(\varepsilon/r_1)^2\) and supported in u<1/2.
Then the full outer shape of EA.14 has sigma squared times f
equal to rho on the entire horn, not only on its rim. Take the
inner round charged link with squared radius r1/2. It is
strictly below H because sigma squared is at least rho, hence
at least r1 there.
The resulting full charged annulus A_f contains the whole H,
and its outer boundary meets H exactly along the prescribed
rim. The same explicit positive shape function applies.
No radial map is used to identify source functions.

Put \(C=\mathcal A_f\setminus\operatorname{int}H\).
It is a compact free-circle domain with its inherited source
functions and physical line. Its complete boundary is
\[
           \partial C=Y_f-Y_{\rm round}-H_r+H_f-H_s.
 \tag{EA.52}
\]
Glue D to the oppositely oriented C along their floor and side
faces, using EA.26 and the exact defining functions, line maps
and spin-c lifts already specified. Their identical face
orientations before reversal are precisely why C is reversed.
The two common faces cancel. The remaining outer face is
\[
 (\Sigma_{\rho_0}\setminus\operatorname{int}H_r)
       \cup_{\partial H_r}
       -(Y_f\setminus\operatorname{int}H_r),
\]
and the only additional full face is the positively oriented
\(Y_{\rm round}\). The latter is a single charge-a link.
This is an equality of cut manifolds with their actual collars,
not a subtraction of local characteristic numbers.

The charged free portions of this outer face use the full
source and target maps in EA.39, with transition EA.33--36
and transported coefficient V inverse from EA.38. The outer
face also contains its fixed S3 tube and its upper z=1 arm.
Those pieces must be retained in their own actual charts:
EA.39 is not an identification of this entire mixed face.
The exact fixed-tube and upper-chart maps are recorded in
EA.21 below. The ordinary and root face agreements are the actual B and F0 arrows in EA.22.

All fixed strata lie in D. C and its glued faces are free.
The exceptional disk remains in the whole F, and the one
primary charge-one point remains in the upper domain of EA.19.
Thus this construction neither adds a second fixed cap nor
counts the two U/V descriptions of the charge-a end twice.

The gluing uses product collars obtained from the specified
invariant boundary functions and an averaged connection on
the actual line. Source functions agree on every glued face.
For a smooth real map after collar gluing, use the common face
value on a smaller product collar and interpolate to each
ambient function with an even cutoff flat at the gluing face.
This is the explicit real collar extension; it is not asserted
to be a holomorphic radial normalization. It is supported in
the inner source neighbourhood, disjoint from the actual
outer parameter family and the finite-cap annulus by EA.19.
The physical line and its derivative lift are glued by the
actual face map, constant in this product collar. The opposite
orientation on C uses the opposite spin-c collar obtained by
reflection in its specified outward real normal. That normal
is a global collar vector, so this reflection is a fixed map
and inserts no sign character on the RP3 fundamental group.
The resulting endpoint is therefore the one already carried
in EA.13, not an independently chosen RP3 lift.

The chain (EA.50)--(EA.52) supplies the lower-face counting
and the sign of the full residual charged boundary in EA.47.
The complete finite-strip and outside comparison is the one established in EA.21--22.

## EA.21. The fixed tube and free parts of the mixed outer face

The explicit fixed points z=V=0 on the outer radial sphere are retained separately from the charged product faces by the following full chart decomposition.
The following chart decomposition retains the fixed part in
the normal bundle of the whole surface F.

On an invariant neighbourhood of its fixed S3, use the unique
positive auxiliary gauge ||S||=1 and write T1=t exp(i phi),
with t positive. Put
\[
 p=e^{i\phi}S,\qquad \zeta=e^{i\phi}z,\qquad
 \nu=e^{2i\phi}\overline V,\qquad \|p\|=1 .
 \tag{EA.53}
\]
These are invariant under the remaining auxiliary circle.
On rho=rho0 the exact inverse is obtained from
\[
 t^2=\frac{\rho_0^2}{1+|\zeta|^2}
                  -(1+|\zeta|^2)|\nu|^2 ,
 \tag{EA.54}
\]
followed by any Hopf representative phi; changing that
representative is exactly the auxiliary identification.
For a sufficiently small normal disk the right side is positive.
Thus (EA.53) is a literal product of the fixed S3 with its
small real normal disk, including the zero vector. Its source
functions are
\[
 q_1=p_0\zeta\overline\nu,\qquad q_2=p_1t,\qquad
 \widetilde v=q_1-q_2 .
 \tag{EA.55}
\]
The compact physical circle multiplies both zeta and nu by
the same phase. They are precisely the positive-weight
spinor coefficients in EA.15; the second coefficient retains
the conjugation of the negative original normal. The
original complex normal and this positive spinor are related
by that displayed real-linear arrow, with the orientation
and physical tautological line of K68.

The radius on this tube satisfies
\[
 R^2=\frac{\rho_0^2}{1+|\zeta|^2}-|\nu|^2 .
 \tag{EA.56}
\]
Choose its normal radius so that R>rho0/2>epsilon throughout.
Its punctured part consequently meets the R>0 free norm
strip. On that overlap the physical positive end map is
the same coefficient map
(U,V) -> (d U,d^{-1}V), with d=(R/r^2)^a.
In the primary chart it is
(z,V) -> (d z,d^{-1}V); it extends over z=V=0,
fixes the source invariants, and has the stated positive
diagonal derivative there. Its full variable derivative is
the base-preserving rank-one extension from EA.10. This
specifies the overlap of the fixed-tube arrow and the free
norm arrow; no independent normal framing is selected.

The local fixed S3 first glues to the rest of the horizontal
normalization surface by the actual RT.1 source immersion,
the two-node map EA.42--46 and the retained Cartier r map.
It receives no local D4 cap. At the global boundary
S2 times S1, the entire resulting normal tube is carried
by the actual Cox quaternion product RT.33a and its ball
extension RT.33b to the single outside cap C0.
The normal clutch on its comparison with C is retained in
RT.29--34. In particular the local S3 and the global
S2 times S1 are connected by this actual trace, not
identified as boundary manifolds.

The upper arm has its own chart. In z nonzero take z=1 and
write
\[
 s_i=S_i/z,\qquad t=zT_1,\qquad w=z^2V .
 \tag{EA.57}
\]
The physical weights are (-1,-1,+1,+1) on
(s0,s1,t,w), and
\[
 q_1=s_0w,\qquad q_2=s_1t,\qquad
 \rho^2=(1+\|s\|^2)|t|^2+(1+\|s\|^2)^2|w|^2 .
 \tag{EA.58}
\]
These are the literal upper chart of the same positive
quotient, including s=0. Its origin belongs once to D;
the deleted charge-one ball and its source functions are
those of EA.19.

On the overlap w nonzero the complete map to the primary
charged V=1 chart is
\[
 (s_0,s_1,t,w)\longmapsto
 (\sqrt w\,s_0,\sqrt w\,s_1,\ t/\sqrt w,\ \sqrt w)
 \tag{EA.59}
\]
in the ordered coordinates (S0,S1,T1,z). The two roots
differ by the actual residual mu2 action. This map preserves
q1 and q2, is equivariant for the same physical circle,
and carries its canonical complex spin-c map through the
specified auxiliary gauge. Its full determinant and line
characters, including this residual action, are retained.
It is the overlap of the upper chart and the lower charged
chart, not a map between their origins.

At w=0,t nonzero the upper chart is still free and has R=0
when s=0. The following actual T1 chart and Tate-period map
retain this endpoint without using an R>0 flow.

On T1 nonzero take the auxiliary gauge T1=1, with coordinates
\[
 (A,B,C,D)=(T_1S_0,T_1S_1,T_1z,T_1^{-2}V).
 \tag{EA.60}
\]
Its physical weights are (0,0,+1,-1), and
q1=A C D, q2=B. The upper-chart arrow is
\[
 (s_0,s_1,t,w)\longmapsto
                   (ts_0,ts_1,t,w/t^2).
 \tag{EA.61}
\]
Thus it includes the entire w=0,t nonzero core.
The radial face rho=rho0 is covered by this chart and V
nonzero, since rho>0 implies (T1,V) is not (0,0).
On their overlap choose h with h squared equal to D. The
map to the ordered V=1 cover coordinates is
\[
 (S_0,S_1,T_1,z)=(hA,hB,h^{-1},hC).
 \tag{EA.62}
\]
Both choices of h give the same point of the specified mu2
quotient. The determinant of this four-coordinate map,
in the ordered variables (A,B,C,D), is +1/2. Consequently
the actual charged contraction volume
-2 dS0 wedge dS1 wedge dT1 wedge dz pulls back to
-dA wedge dB wedge dC wedge dD, which is the contraction
volume in the T1=1 chart. This is the full canonical
spin-c overlap, including its root deck, rather than an
orientation assigned from the coordinate names.

Here is the exact additional free-line chart. On the dense
overlap used by TL take its source coordinate S=s0/s1
and its tensor-Cartier coefficient \(\xi=s_0/s_1^2\).
The latter denominator is required by auxiliary weight two.
The full TL formulas give
\[
 W_0=s_0t/u_P,\quad Z_0=u_Gs_1w,\quad
 V_0=E_+^2s_0/s_1^2,\quad
 Q=q_1q_2u_Q,\quad P=u_P/q_2,\quad u_G=u_Qu_P .
 \tag{EA.63}
\]
Apply the actual inverse period h inverse to all coordinates,
then the indicated integral toric character map:
\[
 (Z_0,V_0)\longmapsto(Z_0/Q,V_0/P^2)=(1/W_0,V_0/P^2),
 \qquad (Z,V)\longmapsto(Z^{-1},ZV).
 \tag{EA.64}
\]
The resulting coordinates extend as
\[
 Z_t=s_0t/u_P,\qquad T_t=u_Pw/t,\qquad
 L_t=E_+^2t/u_P,\qquad q_2=s_1t .
 \tag{EA.65}
\]
In particular q1=Zt Tt and Lt is nonzero when t is nonzero.
Every theta and Cartier unit in E+ is retained in (EA.65).
The full inverse is
\[
 t=u_PL_t/E_+^2,\qquad w=T_tL_t/E_+^2,\qquad
 s_0=E_+^2Z_t/L_t,\qquad
 s_1=E_+^2q_2/(u_PL_t).
 \tag{EA.66}
\]
Here uP and E+ are evaluated on the recovered full source
chart (Zt,Tt,q2). They are independent of Lt. For example,
S=P Zt and Q/S=Tt q2 squared uQ/uP in the full theta
product, while S/P=Zt and Q/Zt=Tt q2 uQ. All factors
after the extracted 1-S have extending unit logarithms on
the chosen t-dominant collar. Thus (EA.65)--(EA.66) give
a holomorphic free-line chart through w=0,t nonzero, not
only formulas on the dense source torus.

The character map in (EA.64) has the literal lattice matrix
\[
 J=\begin{pmatrix}-1&0\\1&1\end{pmatrix},\qquad
 \widehat J(x,y,h)=(-x,x+y,h).
 \tag{EA.67}
\]
For the actual negative-square T0 fan, J sends
{0,e1,e2} to {e1,e2,e1+e2}-e1, and sends the latter
triangle to {0,e1,e2}-e1+e2. The full integral height
translations are retained in these statements. The preceding
inverse h period in (EA.64) is the actual period (Q,P squared),
not just its valuation. All period maps on this new chart are
its literal conjugates through (EA.64).

The source marking in this chart is explicit:
\[
 W_0=Z_t,\qquad Z_0=u_Q q_2 T_t,\qquad q_1=Z_tT_t .
 \tag{EA.68}
\]
It is the (Z0,q2) small-resolution chart. TL's original
chart used (W0,q2). The two source projections are the two
projections of the actual common translation graph, and
their comparison must use the source -G map and its
Cartier reset EA.18--20. This resolution arrow, with the
full r map, is retained in the endpoint audit. It is not
replaced by an identification of central Picard classes.


## EA.22. The actual upper closing arrow and the indexed ordinary end

The opposite-resolution arrow in EA.68 is supplied by the
literal inverse suspension. Retain the fixed nonzero scalar
\(c_\lambda=2\lambda\), \(c_X=q_2u_X\), and the full
SZ.43 Cartier-normalized primitive. In the original torus
coordinates the forward map and its inverse are
\[
 B:(Z,V)\longmapsto
       (P^{-1}Z,c_\lambda q_1c_X^{-2}V),\qquad
 B^{-1}:(Z,V)\longmapsto
       (PZ,c_X^2V/(c_\lambda q_1)).
 \tag{EA.69}
\]
This is the reduced a=2,b=1 map. The cX square in the
inverse is the actual source/target r-conjugated line
map proved in SZ.41--43; it is not an inferred action
on generic Picard classes.

Write (W,T,L) for (Zt,Tt,Lt). Before the inverse
suspension, the full target torus coefficients recovered
from EA.63--66 are
\[
 Z_0=q_2u_QT,\qquad V_0=P^2WL
                  =\frac{u_P^2}{q_2^2}WL .
 \tag{EA.70}
\]
Applying EA.69 gives the exact expressions
\[
 Z_{\rm pre}=u_GT,\qquad
 W_{\rm pre}=Q/Z_{\rm pre}=q_2W/u_P,\qquad
 V_{\rm pre}=\frac{u_P^2u_X^2}{c_\lambda T}\,L.
 \tag{EA.71}
\]
The source is now precisely the marked TL resolution:
its coordinate S=P Wpre is W and its other node
coordinate is T. Thus the source part of B inverse,
which is the actual +G map, carries the opposite
(Z0,q2) resolution of EA.68 to the prescribed
(Wpre,q2) resolution. This is also the actual inverse
of the graph formulas SZ.14 and EA.18. Both projections
retain the same q1,q2 and the chosen v coordinate.

The last expression of EA.71 is read in its actual
toric edge chart. The edge is
\[
 \{(0,0,1),(1,-1,1)\}
       =\{(1,0,1),(0,1,1)\}-(0,1,0).
 \tag{EA.72}
\]
It is the negative diagonal of the square translated
by (0,-1). Its coordinates are
\[
 x=Z_{\rm pre},\qquad y=q_1/Z_{\rm pre},\qquad
 L_{\rm pre}=Z_{\rm pre}V_{\rm pre},
 \qquad xy=q_1,\quad L_{\rm pre}\ne0.
 \tag{EA.73}
\]
The invertible character on this indexed edge is ZV.
On the unshifted edge it would be ZV/q1. The actual
height translate in EA.72 therefore retains precisely
the adjacent-node j to j-1 change in the inverse
suspension; it is not applied a second time.

In the marked source coordinates (W,T,q2), the
complete upper closing map is now
\[
 (W,T,q_2,L)\longmapsto
           (W,T,q_2,F(WT,q_2)L),\qquad
 F=\frac{u_Gu_P^2u_X^2}{c_\lambda}.
 \tag{EA.74}
\]
Every factor is the full extending unit from SZ.39--43.
The retained constants uQ(0)=1/256, uP(0)=16 and
uX(0)=-1/4 give F(0)=1/c_lambda. The quotient
F/F(0) has an extending logarithm on the source
bidisc. The actual fixed scalar and its chosen phase
remain in F(0). Equation EA.74 is invertible, with
complex determinant F. It extends through T=0 and
W=0 and includes the entire t-dominant upper core.
Its inverse is the forward finite-face pairing.
The line is the physical weight-one line in both
charts. In particular no dual circle is introduced
by the source inversion in EA.64.

Here is the complete pairwise collar comparison.
The radial face has the open cover V nonzero and
T1 nonzero, since rho is positive. On the T1 chart
the free locus is C nonzero or D nonzero. The part
D nonzero is the V-chart overlap EA.62. The part
C nonzero is the upper z=1 chart with t=C nonzero,
and is carried by EA.65--74 to the actual indexed
next end. The remaining set C=D=0 is exactly the
fixed-tube locus. Thus these named charts cover
the entire mixed face, including its R=0 free
points and its fixed S3.

On the fixed-tube chart EA.53 the map to EA.60 is
the literal formula
\[
 (A,B,C,D)=(t p_0,t p_1,t\zeta,\overline\nu/t^2).
 \tag{EA.75}
\]
It gives q1=p0 zeta conjugate(nu), q2=t p1.
Its normal map is the actual positive spinor
with the retained negative-coordinate conjugation.
On z nonzero EA.61 is its inverse change to the
upper chart; on V nonzero EA.62 is its change
to the charged chart. Therefore the fixed tube,
upper free chart and charged chart agree on all
their pairwise and triple overlaps by the displayed
coefficient maps. The source functions agree
literally. The original r and kappa maps precede
these formulas; their full coefficients enter E+
and the cX square in EA.69.

The R>0 finite norm strips are attached with their
actual transported norms from EA.37--41. Their
overlap with the upper and fixed charts can be
chosen inside R>=epsilon. On that overlap the
same positive scalar d=(R/r^2)^a is used on both
maps. To define the cut on the upper chart down
to R=0, take
\[
 \widetilde d(R)=
 \exp\!\left(\chi(R)\,a\log(R/r^2)\right),
 \tag{EA.76}
\]
where chi is one for R>=epsilon and zero on a
neighbourhood of R<=epsilon/2. Set dtilde=1 on
that neighbourhood. This is a positive smooth
coefficient, applied only to transport the cut.
It preserves q1,q2 because R is invariant along
the physical real orbit. It agrees with the
specified finite norm map on its entire attachment
collar and with the exact upper endpoint near its
core. The full charged cores in EA.39 remain their
own source/target faces; EA.76 is not an extension
of the interchange EA.40 across those cores.

The finite-cap compatibility follows from the
same actual inverse arrow:
\[
 F_0 B^{-1}=(c_\lambda h_\infty)^{-1}
                         U_{\rm cap}^{-1}F_0,
 \qquad q_1=q_\infty^{-1}h_\infty .
 \tag{EA.77}
\]
This is obtained by inverting the full square in
EA.12, with its root source, r correction, norm sign,
and finite character retained. The full Tate period H_T in
EA.64 is carried as its full lattice arrow through
F0. The positive cut functions are transported
through F0 on its overlap and averaged over its
actual finite group, as in EA.5. The small-R
modification is disjoint from that annulus by
EA.19, so it introduces no new cap face.

For the spin-c comparison, the upper map is the
canonical complex map EA.69 followed by the
actual toric chart EA.73. Its extending unit in
EA.74 has the specified fixed scalar and the
extending logarithm of F/F(0). On the V overlap
the two square roots in EA.62 differ by precisely
the canonical residual mu2 action of EA.13/RT.15.
On the fixed tube EA.75 uses the actual original
complex normal and its written real positive
spinor map. Thus the maps on a triple overlap
are lifts of the same actual composite, with
the determinant factors already fixed in EA.27,
EA.62 and EA.74. There is no additional choice
of an RP3 sign character. The local fixed tube
joins the rest of F before the single global
C0 cap of RT.33a--b is attached.

These are the full upper endpoint and mixed-face overlaps used in the finite boundary identity EA.47.

## EA.18. Finite cut-and-paste ledger for the reduced branch

This section assembles the finite reduced-branch attachment.
It uses a=2,b=1. It does not copy the different a=1 moment picture.
All scalar windings have first been separated by the actual based
homotopy RT.12, so the scalar in this construction is the fixed
nonzero value at r_base. The unscaled infinite central quotient of
SZ.29 is not used.

Take the actual compact source translation graph. Its domain and
target maps outside the central curve are the literal addition
formula and the Cartier line map of SZ.7 and SZ.14--17. At that
curve use both projective charts of the common Cox graph: the
domain t-ruling includes its t1=0 chart at the zero section, and
the target s-ruling includes both divisor charts of G. Thus the
whole proper central component and the whole exceptional component
are retained, not only their affine node points. On a small graph
neighbourhood use the analytic node map (EA.42)--(EA.46). Outside
it the actual source/line map is an isomorphism between the two
graph projections; choose the ordinary norm cut and transport its
target face by that map. The finite-root source/line map is the
actual U_cap of EA.4, with F0 on its annulus. Compactness of the
remaining source and root pieces gives one common contracting
scalar range.

Cut before taking the period quotient. On the compact complement
of the graph neighbourhood this is the ordinary fundamental
annulus between a norm hypersurface and its actual B-image. On
the stable graph collar use the finite region between Ht and Hs
from EA.39, with R bounded below by a positive epsilon. The
actual end scalar and its phase are retained before the positive
normalization EA.40. The change of norm cut is an explicit
monotone interpolation of the two logarithmic norm coordinates,
fixed at their transported endpoints; on the node charts its
extension is the positive diagonal map in EA.13. Thus no raw
logarithm of q is extended through q=0. The q factor is absorbed
by the literal j to j+1 node arrow, and the actual cyclic graph
reset and j to j-1 overlap are EA.18--26.

The selected node is completed in the primary positive associated
chart. TL.1--4 identifies its boundary, through the full theta,
Cartier and h-period map, with current Tate T0. On the positive
moment piece use the complete retained domain EA.48 and its invariant
corner rounding. It includes the upper fibre and charge-one point. Its defining functions are the actual R and
rho, and q,v are retained by ambient inclusion. The lower arm
is the transported shape EA.29--30. Its full two faces are
EA.39, with their actual source/target line coefficient EA.38;
their full orbit transition is EA.33--36. The upper arm stays
in the primary positive piece. It is not relabelled as a
charge-two arm or silently capped by a second copy of the
lower chart.

The following face pairings are the ledger for this finite
construction. They specify maps, not merely a cancellation of
numbers.

* Ordinary source and target norm faces are paired by the actual
  B map, with its Cartier coefficient. Their boundary normals
  are opposite. On the graph collar this is the same pairing
  after the explicit positive norm interpolation just described.
* Every finite-root face is paired by the literal H or A map of
  EA.12. The F0 square identifies it with the ordinary B pairing;
  both norm signs, all finite characters, and the root-component
  translations remain. There is no residual cap face from replacing
  a finite root by its generic source point.
* The inner source collar and the ordinary source exterior are
  glued by TL's full source/line map. On every node chart its
  monomial factors and units are the actual ones, including the
  h reindex. The two source-base normals are opposite. The
  source functions and their parameter arrow agree literally.
* In the chosen finite B strip the complementary U and primary
  V descriptions are one charged end. They are related by EA.26,
  not added as two positive GIT charts. After all other period
  faces have been paired, the target-minus-source finite face
  cycle is the single positive charged boundary Sigma_a of
  EA.41. The q reindex, scalar phase and determinant root are
  retained. In particular the lower charged origin is not
  quotiented by its infinite central stabilizer.
* The fixed surface is the entire
  F=Bl(P1 times D), including its exceptional disk. Its annular
  part in RT.20 carries the same two normal frames on both
  sides. It is capped only by the actual outside cap C0=D3
  times S1. No separate local D4 cap from RT.10 is inserted.

Every gluing is between disjoint closed collar faces by the
specified diffeomorphism. The construction is finite: it uses a
compact norm interval, both charts of each projective ruling,
the finite root atlas and the two compact corner arms. Thus the
resulting glued space is compact and Hausdorff; it is not obtained
by gluing two open GIT quotients with distinct limits. Invariant
rounding of the stated regular boundary functions gives its smooth
collars. On the outer nonzero v circle the cuts are simply cuts
of the original proper family: choose epsilon so small that the
R-epsilon region lies strictly inside that parameter circle.
The full TL and F0 maps therefore identify the completed outside
boundary with that actual parameter return.

The spin-c and physical-line identifications on these face
pairings are the actual coefficient and derivative maps. The
ordinary and finite-cap maps are holomorphic. The norm
interpolations have the explicit positive and rank-one derivative
homotopies in EA.10 and RT.15. The graph reset has the exact
determinant root i*z_s^(-2), conjugated by the full extending
kappa units; the charged overlap has its constant root i.
The mu2 endpoint is the canonical +omega8 in EA.13/RT.15.
These are composed in the same order as the actual face maps.
On an ordinary triple overlap their composition is the
canonical complex spin-c lift of the actual coordinate identity;
on a root overlap it is the specified finite-character action.
No additional sign character is inserted at the RP3 face.

The complete face maps give the following oriented boundary equation.
Let N7 be the actual free-circle total boundary obtained by the
outside conifold/Hopf completion, and let N6=N7/S1. Delete the
entire capped fixed tube and the primary positive chart's
charge-one ball. Replace the fixed cap C0 by C=P1 times D2
with the actual normal-map triangle of RT.17. Give C and C0
the same boundary orientation as partial F. Then
\[
 [F-C_0]=[F-C]+[C-C_0],\qquad C-C_0=S^4.
\]
Write B_F and B_4 for their actual projectivized normal sphere
bundles, with physical tautological line. The finite free
circle quotient has boundary cycle
\[
       -N_6-\mathbb P^3_a-B_F-B_4+\mathbb P^3_1.
 \tag{EA.47}
\]
Here P3_a denotes the charged boundary with M=O(-a), not a
discarded residual quotient; P3_1 is the primary positive
isolated-point boundary. The sign of P3_a is fixed by the
positive total-space end chain EA.41 and the circle-first
boundary reversal. The deleted fixed tube contributes -B_F
and -B_4 by the literal cap identity. The two negative normal
conjugations at the isolated point give +P3_1, as in RT.13.
The exceptional disk belongs to F once and never to a separate
local fixed-S3 handle.

The physical line and stable tangent bundle on this cycle are
the ones carried by the actual free circle action. The S4
normal clutch is retained; no value of its c2 is imposed.
RT.16--17 computes its index and the full fixed-surface term
with both actual parameter windings. The complete outside and cyclic endpoint maps in EA.19--22 establish this boundary identity for the actual family.

## RT.16. The whole fixed trace, its actual cap clutches, and the index

We keep the whole surface F=Bl(P1_s times D_v), including its
exceptional disk. No copy of the local fixed-S3 handle of RT.9 is
inserted in this calculation. Let Y=boundary F=S2 times S1, with
its complex boundary orientation. Put c(v)=sqrt(1+v), on the actual
branch equal to one at zero. The marked coordinate

\[
 Z=(s-c(v))/(s+c(v))
\]

is induced by the full matrix ((1,-c),(1,c)); its determinant 2c
is nonzero on the whole parameter disk. Thus this is an extending
Mobius map on the unblown P1 family, not a replacement of its
parameter loop by a constant matrix. It takes D+ to zero and D-
to infinity. The blowup centre lies on D- and not on D+.

Cap by a second P1 times disk using this actual boundary coordinate.
Write C for this cap with orientation chosen so that its boundary
is Y. Equivalently, -C has the complex orientation of the second
parameter chart w=constant/v. The closed oriented surface F-C is
the complex blowup of P1 times P1. Let H and B be respectively the
two factor classes, and retain E for the exceptional class. Then

\[
 H^2=B^2=0,\quad H B=1,\quad E^2=-1,\quad
 H E=B E=0,\qquad \sigma(F-C)=-1.                 \tag{RT.27}
\]

In the first parameter disk the actual divisors have classes
D+=H and D-=H-E. The positive spinor of the physical normal
model is the same tensor sum carried in RT.1 and RT.9:

\[
 O(D_+)\otimes O(-aE)\ \oplus\
 O(-D_-)\otimes O(-aE).                           \tag{RT.28}
\]

The tensor factor is the actual source line. At a=2 this statement
includes the source and target Cartier r maps, not just the tensor
line's divisor class. The full F0 cap maps act on its nonzero
coefficients. The negative normal coefficient is conjugated by the
same physical positive-weight arrow as in K68; no line dual is
silently substituted.

Here is how all parameter and cap clutches are retained on the
second disk. Give its two summands the reference divisor frames
of O(H) and O(-H), in the displayed Z coordinate. On Y compare
them with (RT.28), transported by the actual source/Cartier/F0
maps and the actual Cox normal frame. Denote the resulting two
nonzero coefficient ratios by g+ and g-. They are functions on
Y because the common O(1) and O(-1) point transitions cancel.
In a finite s chart these are the ratios of the reference frames
1/(s-c) and s+c to the actual frames of (RT.28), including their
full source-line coefficient and normal units. At their divisor
points the same ratios are taken in the alternate Cartier chart;
the ratios agree, so no zero or pole is introduced at D+ or D-.
The finite character of the cap is part of these ratios. Its
constant value is not replaced by one.

Use the frame convention e_cap=g e_F. Define the two actual
integers by

\[
 w_\pm=\frac{1}{2\pi i}\int_{\{p_*\}\times S^1}
                              g_\pm^{-1}dg_\pm .   \tag{RT.29}
\]

Here p* is a regular point in the marked sphere, away from the
Cartier charts' divisor points. The integer is independent of p*
because g is a nonzero function on the connected product Y.
The direction of (RT.29) is fixed as follows: e_cap=v e_F is
the actual transition of O(1) on the doubled parameter sphere,
so a winding w contributes +w B. This also fixes the sign of
the base classes below.

There is an exact smooth line map reducing this clutch to its
displayed integer without losing the rest of the map. The ratio
g exp(-i w theta) has zero class in H1(S2 times S1;Z), and
therefore has a single-valued smooth logarithm h. Extend h over
S2 times the cap disk by the parameter-disk Poisson extension,
with a collar interpolation preserving its boundary value. Changing
the cap frame by exp(-h) gives precisely exp(i w theta) on Y.
This is a nonvanishing frame change on that specified cap. It
does not change the original F0, source or normal map on the first
piece. In particular it does not declare either w to be zero.

It follows that the actual capped spinor is isomorphic, with these
boundary arrows retained, to the sum of lines with Chern classes

\[
 l_+=H-aE+w_+B,\qquad
 l_-=-H+(1-a)E+w_-B.                               \tag{RT.30}
\]

Consequently, for b=c1(E_spin) and c2=c2(E_spin),

\[
 b=(1-2a)E+(w_++w_-)B,\qquad b^2=-(1-2a)^2,
\]
\[
 c_2=-a(a-1)+(w_--w_+).                            \tag{RT.31}
\]

Thus even the unequal normal-clutch windings have been retained;
their cross term occurs in c2. The determinant has no H term,
which is the precise reason there is no B cross term in b squared.
The local canonical complex spin-c arrows, their determinant
lifts on the charged collars, and the physical line are those
of RT.15 and EA.13. The cap construction carries those actual
bundle maps. It makes no additional choice of a spin character
on the lower RP3 arm.

For completeness the characteristic cancellation is obtained from
the physical line itself. On P(E_spin) put h=c1(O(1)); the actual
physical nonzero-vector line is M=O(-1), hence x=-h. The same
Hopf coefficient map on both caps gives this line arrow. The
projective relation and fibre integrals are

\[
 h^2+b h+c_2=0,\quad \pi_*h=1,\quad
 \pi_*h^2=-b,\quad\pi_*h^3=b^2-c_2.
\]

The vertical complex tangent has Chern class 2h+b, so its first
Pontryagin class is b squared minus 4c2, pulled back from the base.
Thus the two physical characteristic numbers, with the stated
base and complex fibre orientations, are

\[
 k=c_2-b^2,\qquad
 \ell=-\langle p_1(F-C),[F-C]\rangle-b^2+4c_2,
\]
\[
 \frac{4k-\ell}{24}
 =\frac{\langle p_1(F-C),[F-C]\rangle-3b^2}{24}
 =\frac{\sigma(F-C)-b^2}{8}=\frac{a(a-1)}{2}.           \tag{RT.32}
\]

Neither the normal c2 nor either actual clutch integer was set to
zero in this computation. The full source and finite-cap maps
enter (RT.29); their possible cross terms cancel by (RT.32).

## RT.17. The two actual caps and the fixed-boundary correction

The outside Jin completion uses its actual product cap
C0=D3 times S1, with boundary Y and the retained Cox/Hopf normal
coefficient frame. Its normal bundle and its physical line are
the ones specified by that frame. They are not replaced by the
reference divisor frame used to calculate (RT.30).

The actual boundary arrow defining this cap is the following.
Use the full TL.1--3 node/Cartier map to the selected fixed-edge
charts of current Tate T0. In the boundary parameter annulus their
native coordinate is the displayed Z, and their two linear normal
coordinates have overlap c_i'=Z c_i and physical weights (-1,+1).
The units in TL.11 and the degree-two r arrow are included in
these coefficient maps. This is the literal two-cone fixed-star
chart, not a statement obtained from its normal degrees alone.
An actual nonzero chart unit on this annulus has the exact form
v^d exp(h); its integer d and its full coefficient are retained.
On each of the two physical weight lines, the linear normal
automorphism over the compact fixed P1 is a scalar function of
the parameter, because H0(P1,O)=C. The higher normal terms are
carried to their linear maps by equivariant normal rescaling on
a common smaller tube. The rescaling is the identity on the zero
section and is followed by its collar isotopy, so it carries the
original line and annular maps rather than discarding them.

In homogeneous unit Cox factors put

\[
 u=a_0+j a_1,\qquad v_N=c_0+j\overline{c_1},\qquad
 h=u i u^{-1},\qquad q_H=u v_N.                    \tag{RT.33a}
\]

The auxiliary circle cancels in q_H. Choosing a Hopf representative
of h and putting v_N=u^{-1}q_H is its explicit inverse. On the
finite Z chart it is the normalized expression
(1+jZ)(c0+j conjugate(c1)). These are exactly the first-resolution
products of K23, equations SF.5--6 of
part3_source_cusp_fixed_edge_working.md, applied here to the actual
TL fixed-star coefficient maps. Their formulas are independent of
which source supplied those maps. At nonunit normal radius the
same expression is real linear in the normal vector and sends
zero to zero. Thus it identifies the entire small normal tube,
not just its link. The physical action is
q_H -> q_H exp(-i phi), with its actual character.

All parameter powers act through their actual Cox coefficients
in (RT.33a). They are single-valued integer powers on this annulus.
This yields a periodic normal product over the parameter circle;
it does not claim that its comparison to a different product
extends over the cap. That comparison is the normal clutch on
the S4 in (RT.33), and is retained below. The underlying sphere
coordinate change has the literal extension

\[
 P\longmapsto A_{c(v)}P A_{c(v)}^*/
                    \operatorname{tr}(A_{c(v)}P A_{c(v)}^*),
 \qquad A_c=\begin{pmatrix}1&-c\\1&c\end{pmatrix},  \tag{RT.33b}
\]

on the trace-one positive-Hermitian three-ball. Its denominator
is positive, its inverse uses A_c inverse, and its boundary map
is exactly Z. Holding the actual q_H coordinate fixed gives the
product cap arrow (P,q_H,v)->(B_c(P),q_H,v). It is the explicit
K42 SP.13/K68 physical-circle cap arrow, now with the extending
c(v) and the actual TL/Cox coefficient product. It preserves
the physical line and normal orientation. No tangent derivative
is substituted for this product arrow.

The positive spinor on this cap is typed explicitly: its two
complex coefficients are the conjugates of the right-complex
coefficients of q_H. They have positive physical weight because
q_H has the negative right phase. If e denotes the positive
Cartier spinor on F, K68's actual arrow is q_H=G_Z conjugate(e),
including its fixed ordering and constant normal comparison.
It therefore becomes the complex-linear arrow
conjugate(q_H)=conjugate(G_Z)e to the cap's positive spinor.
The physical associated line is its O(-1), with the original
circle character. The normal antipodal/meridian reversal in
the first arrow is retained by this coefficient choice. It is
not replaced by a complex-linear swap of e and q_H. Thus the
bundle used on the cap and on the S4 below is an actual complex
rank-two bundle with the displayed line morphism.

The two cap choices have the exact closed base

\[
 S_4=C-C_0
     =(S^2\times D^2)\cup_{S^2\times S^1}
                        -(D^3\times S^1)\cong S^4, \tag{RT.33}
\]

with the orientations chosen above. The last map is the rounded
boundary of D3 times D2; its two product faces are precisely the
two written caps, with their opposite boundary orientations.
Their actual normal coefficient maps along Y define the normal
bundle on this S4 by gluing, including every difference of the
Cartier and Cox frames. The induced physical Hopf line is the
tautological O(-1) on its projectivization. There is no unrecorded
circle gauge: the coefficient ratios on Y are the same g functions
as above, and a circle gauge's S1 degree extends on C0 because
H1(C0;Z) maps isomorphically to H1(Y;Z).

There is an explicit bordism implementing this cap replacement.
Take the products of F,C,C0 with intervals and join their boundary
collars by Y times a triangle, one interval product on each edge.
Use the three boundary identifications furnished by the actual
normal frames; the third is the inverse composite of the first
two. They therefore extend over this collar triangle. Rounding
its product corners gives a compact oriented five-dimensional
base bordism with the three closed four-dimensional faces
F-C0, F-C and C-C0. The normal bundles glue on the same products,
and projectivizing gives the required sphere-bundle bordism with
the physical line. This proves the literal cycle identity

\[
 [B_{F-C_0}]=[B_{F-C}]+[B_{S_4}]                 \tag{RT.34}
\]

with the retained normal maps, rather than only an equality of
intersection forms. A nonzero third-class normal clutch may be
present on S4. Its c2 is carried by this construction. Applying
the same formula (RT.32) gives index zero, because H2(S4)=0
and its signature is zero. The c2 term cancels explicitly.

Deleting the entire fixed tube in the global orbit construction
therefore supplies -B_(F-C)-B_(S4). The exceptional E remains
in the first base. This is the fixed-cap part of the boundary
ledger; it must be combined with the finite-period face chain
and the actual outside/Jin arrow before a global return is assigned.

The additional exact certificates are
code/part3/source_zero_cut_spin.py (67 local cut, charged-overlap,
Clifford and spinor identities) and
code/part3/source_zero_fixed_cap.py (462 whole-cap identities,
including arbitrary retained w+ and w-). Their JSON and captured
outputs retain these local scopes. The fixed-cap program's first
JSON serialization error is preserved under
records/attempts/source_zero_fixed_cap_json_types; all its
mathematical assertions had completed, and the repair converts
only SymPy output integers to native JSON integers.


## RA.3. The physical characteristic equation and actual return

Let \(N_7\) be the actual completed outside boundary of the
finite construction. The physical circle is free after
the conifold/Hopf replacement on its selected fixed tube.
Let \(N_6=N_7/S^1\), with the Jin orientation of P3K.68.
On every free part of the seven-dimensional quotient
bordism the associated line is the actual nonzero-vector
line \(M\), and \(x=c_1(M)\). The tangent splitting is the
quotient tangent plus the oriented physical circle. Thus
\(p_1\) is the pullback of the quotient \(p_1\).
Choose invariant product connections on the named collars
and patch them on the compact interior. Stokes applied
to the closed Chern--Weil polynomial gives the exact
oriented characteristic identity
\[
 -A(N_6)-A(\mathbb P^3_2)
       -A(B_{F-C})-A(B_{S^4})+A(\mathbb P^3_1)=0,
 \qquad
 A(X)=\int_X\frac{4x^3-p_1(TX)x}{24}.             \tag{RA.3}
\]
The boundary signs are those of EA.47. The full charged
end occurs once by the horn chain, the exceptional disk
belongs to the whole \(F\), and the sole fixed cap is \(C_0\).
The two auxiliary charged descriptions are related by
EA.26 and contribute one boundary.

On a positively oriented charged projective boundary the
physical line is \(O(-a)\). Hence, writing \(h\) for the
positive generator, \(x=-a h\) and \(p_1=4h^2\), so
\[
 A(\mathbb P^3_a)=-\frac{a(a^2-1)}6.
\]
For \(a=2\) this is \(-1\); for the isolated charge-one
boundary it is zero. The whole capped surface calculation
RT.27--32 retains both actual normal clutches and gives
\(A(B_{F-C})=1\). The actual comparison cap \(S^4\) has
\(A(B_{S^4})=0\), independently of its retained normal
\(c_2\). Therefore (RA.3) gives
\[
                     A(N_6)=-(-1)-1-0+0=0.      \tag{RA.4}
\]
This is a calculation on the specified compact finite
bordism. The physical line and canonical spin-c overlap
maps, including the residual \(\mu_2\) endpoint, have
already been carried through every face.

For the actual return, take a delta-averaged connection on
the original completed family, product on the selected
tube in the exact RT.33a--b coordinates. Its quotient after
the conifold replacement is a diffeomorphism
\(f:S^2\times S^3\to S^2\times S^3\), fixed on that tube.
The preserved Euler class generates \(H^2\), and the
orientation then preserves \(H^3\); thus \(f\) belongs to
the required homology-trivial relative group.
The Hopf lift in P3F.22 is literally the physical return
lift on the complement and uses the same identity
extension on the selected tube. P3K.68 supplies the full
piece and inverse-clutch arrow
\[
       \lambda_M(f)=-\Sigma(f^{-1})=\Sigma(f).
\]
Consequently its class in \(\Theta_7\) is the physical
integer (RA.4), namely zero. This step selects the
actual parameter return by its source, cap, tube and
line maps, rather than only by its characteristic polynomial.

For the literal reflected fan, the already proved single
native directed flop of P3K.60 has the actual pair
\((1-a,a)=(-1,2)\). Its signed relative Cox conjugation
adds the right exponent \(a=2\) to the central class.
The complex normal orientation and the physical transfer
are precisely those retained in P3K.68--69. Thus the
reflected fixed-scalar class is \(2\). No division of a
covered \(\Theta_7\) class is made.

Finally the actual scalar-root loop has physical index
\(3p-1\) in these two fans: P3K.24 with the physical
correction P3K.68 gives the initial value, and the narrow
actual C2 comparison P3K.62 gives their equality.
The exact based parameter homotopy RT.12 adds \(k\) such
loops, with basepoint \(r_{\rm base}=v_*^k r_0\).
It therefore gives (RA.1), retaining either norm sign
and all prescribed finite characters.

## RA.4. Exact certificates and proof scope

The full source/Cartier, node and shape calculations are
executed in the following retained certificates:
\path{code/part3_fourfold/source_zero_two_node_cox.json},
\path{code/part3/source_zero_tate_label.json},
\path{code/part3_fourfold/source_zero_associated_reset.json},
\path{code/part3_fourfold/source_zero_chamber_ledger.json},
\path{code/part3_fourfold/source_zero_spin_chart.json},
\path{code/part3_fourfold/source_zero_charged_shape.json},
\path{code/part3_fourfold/source_zero_native_charged_seam.json},
\path{code/part3_fourfold/source_zero_full_faces.json},
\path{code/part3_fourfold/source_zero_upper_domain.json},
\path{code/part3_fourfold/source_zero_boundary_ledger.json},
and \path{code/part3_fourfold/source_zero_mixed_outer.json}.
They retain the full units and exact integer/normal
characters. The analytic extension and compact-face proofs
are given above; numerical identities do not replace those
maps. The chronological attempts and withdrawn shortcuts
remain in the working notes and attempt records. This
theorem proves the reduced branch only.

