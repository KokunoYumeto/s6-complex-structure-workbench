# The actual source-zero associated-node chart and its Tate fan label

Working local comparison, 17 November 2026. This note supplies the
full source bidisc and Cartier map at the selected node. The compact
radial attachment remains owned by the separate EA/RT construction;
no individual source-zero return is assigned here.

We retain the source and every marked function from K49/K60:
\[
 Y^2=X^3+(1-2v)X^2+TX+v^2,\qquad G=(0,v),
\]
\[
 q_1=T-(v^2-2v),\qquad
 q_2=T-\frac{1+4v-(1-8v)^{3/2}}8.
\]
The square root is its holomorphic branch equal to one at the origin.
The actual line sectors are \((a,b)=(1,2),(2,1)\). In the latter
sector the explicit Cartier arrow \(r\) of SZ.16 is applied before
using the tensor line \(\mathcal O(G-O)^{\otimes2}\), and its inverse
is retained at the other end. The original degree-two line is not
silently replaced by that tensor line.

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

## TL.4. Period, closing, and remaining attachment scope

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

