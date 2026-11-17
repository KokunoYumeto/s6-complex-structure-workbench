# The separate good-branch source-zero cut and its two primitive maps

Working calculation, 17 November 2026. This note treats a=1,b=2,
m=4p. It retains the fixed scalar supplied by RT.12, the actual
Cartier primitive U1, and the good-root cap. The reduced a=2
positive chamber is not used for this construction. No individual
source-zero return is assigned here.

## GC.1. The actual positive quotient and a proper weighted cut

Use the full bilinear node coordinates of EA.42--46. The primary
associated resolution has coordinates (S0,S1,T1,z,V), with auxiliary
weights (1,1,-1,0,-1) and physical weights (0,0,0,1,-1). Its positive
auxiliary quotient is literally

\[
 W_1=\operatorname{Tot}\bigl(O(-1)_{T_1}\oplus O(-1)_V
                  \longrightarrow P^1_{[S_0:S_1]}\bigr)\times C_z.
 \tag{GC.1}
\]

The transition functions are the actual inverse powers of the two
homogeneous source coordinates. The source functions are
q1=S0 z V and q2=S1 T1. The original parameter v is the analytic
inverse of the base coordinate q1-q2, with the unit retained as in
EA.17. This is the exact morphism from the original source, not
its homogeneous approximation.

Let H=|S0| squared plus |S1| squared, and define invariant functions

\[
 b=H|T_1|^2,\qquad c=H|V|^2,\qquad d=|z|^2,
 \qquad \rho^4=b+c^2+d^2,\qquad R^2=b+cd.          \tag{GC.2}
\]

The function rho is proper on the vector-bundle neighbourhood of
the compact zero section. Every positive rho level is smooth:
the derivative in T1 is nonzero when T1 is nonzero; otherwise a
nonzero V or z gives a nonzero derivative of its fourth power.
This is the weighted radial function with weights 2,1,1 on
(T1,V,z), respectively. R is exactly the source product radius
||S|| ||T|| for T=(zV,T1).

The physical fixed locus is exactly z=V=0. To see this without
discarding auxiliary stabilizers, the nonzero positive auxiliary
coordinates S force the auxiliary compensating phase to be one.
The remaining physical phase therefore fixes a point precisely
when both z and V vanish. This fixed locus is O(-1) over P1, the
same exceptional trace disk as in RT.1. There is no isolated
positive-chamber fixed point in (GC.1). On z nonzero the function
z is an actual equivariant nonzero coordinate of physical weight
one; it supplies the physical line trivialization there.

Choose radii satisfying epsilon positive and
r1^4>4 epsilon squared, with r1<rho0. Retain the actual compact
domain

\[
 D_1=\{\rho\le r_1\}\ \cup
 \{r_1\le\rho\le\rho_0,\ R\ge\epsilon\}\ \cup
 \{r_1\le\rho\le\rho_0,\ d\ge c\}.              \tag{GC.3}
\]

Every union and intersection is in the same quotient (GC.1), by
the identity source, line and tangent map. At d=c one has
R squared=b+c squared and rho fourth=b+2c squared, so
R squared is at least rho fourth divided by two. Hence the
artificial d=c seam above r1 lies strictly in R>epsilon and
supplies no boundary face. The entire zero section is in the
first piece. On the fixed trace c=d=0, R=rho squared, so the
whole trace remains in (GC.3), including its exceptional disk.
The upper z arm is filled inside this same smooth quotient.

The removed horn is exactly r1<rho<=rho0, c>d and R<epsilon.
It has V nonzero throughout. The two functions rho and R have
regular transverse level faces there. Here is the check in the
actual complex fibre coordinates. At a point with T1 nonzero,
proportionality of their gradients would force the multiplier
between d(R squared) and d(rho fourth) to be one. The nonzero
V coordinate would then give d=2c, contradicting c>d. At a
point with T1 zero and R=epsilon positive, both z and V are
nonzero. The ordered two-gradient determinant is
2(c squared-d squared)>0. If z is zero and T1 is nonzero,
the corresponding determinant is 2c>0. In the fully positive
case the T1 equation fixes the proportionality multiplier
to one, and the two others would force c=d=0. This handles zero
fibre coordinates without treating their squared norms as
smooth coordinates there. Invariant corner rounding retains
the specified outward normals.

## GC.2. The complete charge-one lower shape

In the actual V=1 chart there is no residual finite quotient.
The physical weights on (S0,S1,T1,z) are (-1,-1,+1,+1). Put

\[
 \sigma^2=\|S\|^2+|T_1|^2+|z|^2,\quad
 x=\|S\|^2/\sigma^2,\quad \zeta=|z|^2/\sigma^2.
\]

Direct substitution, with no radial coordinate map, gives

\[
 \rho^4=\sigma^4\bigl(x(1-\zeta)+\zeta^2\bigr),
 \qquad R^2=\sigma^4 x(1-x).                       \tag{GC.4}
\]

On the lower horn c>d says x>zeta. Its angular denominator
f0 squared=x(1-zeta)+zeta squared is at most x. Consequently

\[
 1-x\le {R^2\over\rho^4}
       <{\epsilon^2\over r_1^4}<\frac14,
 \qquad 0\le\zeta\le1-x.                          \tag{GC.5}
\]

Thus x>3/4 and zeta<1/4 on the closed horn. The square root f0 is therefore a positive
smooth angular function on a neighbourhood of that entire horn.
Choose an invariant cutoff equal to one there and supported in
x>1/2, and extend f=1+chi(f0-1) to the whole charged sphere.
On that support zeta<=1-x<x and f0 squared>=x squared>1/4.
Together with the upper bound below this gives 1/2<f0<=1.
The cutoff support avoids every zero of f0; f is positive.
On the horn the exact defining-function equality is

\[
                         \rho^2=\sigma^2 f.         \tag{GC.6}
\]

Thus the complete outer charged shape sigma squared times f
equal rho0 squared agrees literally with the old radial face
on its lower rim. Since x+zeta<=1, f0 squared is at most
(1-zeta) squared plus zeta squared, hence at most one. Our
cutoff therefore has f<=1. Take the round inner link with
sigma squared equal to r1 squared divided by two. This lies
strictly below the entire horn, where sigma squared>=rho squared.
The interval region between that inner sphere and the full
outer shape is a compact free-circle annulus, with all source
functions carried by ambient inclusion. No radial map is
asserted to preserve q1 or q2.

Removing the horn from that charged annulus and gluing the
opposite resulting piece to D1 along its floor and side gives
the same explicit boundary-chain identity as EA.50--52. The
face maps here are the a=1 versions of EA.26 and EA.39, with
their actual node coefficient and scalar normalization. The
remaining complete charged boundary has physical line O(-1)
over CP3: conjugating the two negative complex coordinates
preserves real eight-dimensional orientation, and its actual
coefficient map is [u,w] to w u in the tautological line.
Its physical pair is (-1,-4), so its characteristic index is
zero. This is the specified lower boundary calculation; it
does not count how the two primitive source steps occur in
the whole B strip.

The upper z region does not produce a charge-zero projective
substitution. It remains the actual region (GC.1), with the
equivariant nonzero function z on its free upper arm. Its line
and both boundary maps are retained in the ordinary source
gluing. The source functions satisfy
|q1|+|q2|<=R, so the same quantitative separation from the
outer source and parameter boundaries used in EA.19 applies.

## GC.3. Two primitive cap steps with the full character and divisor

Write m=4p. The actual primitive and suspension are

\[
 U_1:(p,w)\longmapsto(p-G,w/X(p-G)),\qquad
 B=-2\lambda q_1 U_1^2.                            \tag{GC.7}
\]

On the root q_infty=z_infty^m the actual normalization from
EA.7 is

\[
 U_{\rm cap}=z_\infty^{-m/2}U_1,\quad
 F_0U_1=z_\infty^{m/2}U_{\rm cap}F_0,\quad
 q_1=z_\infty^{-m}h,\quad
 F_0B=-2\lambda h\,U_{\rm cap}^2F_0.              \tag{GC.8}
\]

All source and line factors of F0 are retained. The root map
Ucap is the literal translation with target coefficient
1/X'(p-G'), not an uncorrected tensor frame. The canonical
deck sends X' to -X', and the exact finite relation is
Ucap A0 Ucap inverse=-A0. Hence a single primitive step changes
the finite physical character by m/2; it is not declared a
self-map of the unchanged cap data.

Here is the complete intermediate two-step groupoid. For
epsilon=0,1,2 set

\[
 A_\epsilon=(-1)^\epsilon A_0,\qquad
 F_\epsilon=z_\infty^{-\epsilon m/2}F_0.
 \tag{GC.9}
\]

Then the actual equalities are

\[
 U_{\rm cap} A_\epsilon U_{\rm cap}^{-1}
       =A_{\epsilon+1},\qquad
 F_{\epsilon+1}U_1=U_{\rm cap}F_\epsilon.
 \tag{GC.10}
\]

The first equality retains the full root generator, including
its source translation and chosen finite delta character.
The scalar z_infty to the m/2 power has root character -1,
which cancels exactly that of Ucap on the ordinary overlap.
After two steps A2=A0, but F2=z_infty inverse-m times F0.
This vertical divisor is not removed as a unit. It is
compensated only by the actual q1 factor in B, giving the last
square in (GC.8), with h still present. Both norm signs n and
every original finite character remain throughout.

## GC.4. The retained derivative and spin maps of the two steps

For one graph reset EA.18--20 gives the full complex-four
determinant z_s inverse-squared in this branch. Its chosen
determinant root is the literal function z_s inverse. Thus two
consecutive reset charts carry the product
(z_s,0 z_s,1) inverse as their determinant root, evaluated at
the actual consecutive source points. Neither source coordinate
is replaced by its value on a central component. On another
projective source chart the canonical volume and this root are
transported by that chart's actual transition; these are bundle
arrows, not an assertion that z_s inverse extends as a function
through zero.

The charged overlap EA.26 has complex determinant -1 and the
fixed root i before the normalized charged gauges; it is the
identity on their ordered complex-four coefficients. For a=1
there is no residual mu2 character at this lower link. The
canonical complex spin-c lifts are the exterior-algebra lifts
of these actual derivatives. Their compositions are the lift
of the displayed composed coordinate arrow, with the stated
determinant roots. The positive norm changes have the exact
diagonal and nilpotent derivative homotopies of RT.15, based
at these arrows.

The vertical factor z_infty to the m/2 power in (GC.8) is also
kept as a typed root-line map. In an ordinary nonzero line
coefficient w its derivative has determinant z_infty to the
m/2 power: the source coordinates are fixed and the additional
base derivative is triangular. Since m/2=2p, the corresponding
determinant root is the single-valued z_infty to the p power
on this annulus. This statement is in the dw coefficient frame.
In the logarithmic line frame dw/w the same map has determinant
one and the extra derivative is unipotent; the frame arrow
dw=w dlog(w) is retained. In an associated node pair (U,V)
the simultaneous map is (z_infty^(m/2) U,z_infty^(-m/2) V),
whose two normal determinants cancel. None of these different
frames is equated without its displayed coefficient arrow.
At the root centre the scalar powers are maps of the
corresponding divisor lines, not nonvanishing scalar units.

The canonical complex spin-c lift of the one-line character
-1 has the literal representative [e1 e2,i], using the
positive half-rotation in that complex line and e_i squared
equal to -1. Its square is [-1,-1], the identity in Spin-c.
On the exterior-algebra spinors the first character acts as
plus one in degree zero and minus one in degree one. Thus the
two character changes in (GC.10) compose to the original
character with its canonical lift, not merely as bare signs
on the underlying line. The determinant frames of the source
reset are still the chronological roots stated above. The full
second-step norm is exactly the B square in (GC.8), so no
additional independent sign or unrecorded ruling reset is
inserted at the cap.

The remaining task is to place this entire two-object sequence
in the actual finite source strip, matching the upper z arm,
the two local charged collars and the whole fixed trace.
The present note proves the separate good-branch cut and the
displayed local/cap composition. It does not replace that
global pairing by the reduced branch's one-step ledger.


## GC.5. The entire upper free product, with its coefficient arrow

The a=1 upper region z nonzero has a literal product map that
also retains its R=0 exceptional curve. Set W=zV. In the actual
positive auxiliary quotient the map and its inverse are

\[
 (S,T_1,V,z)\longmapsto(S,T_1,W=zV,z),\qquad
 (S,T_1,W,z)\longmapsto(S,T_1,W/z,z).
 \tag{GC.11}
\]

Since z has auxiliary weight zero, these maps commute with every
auxiliary chart transition. Thus this region is exactly

\[
 \operatorname{Tot}\bigl(O(-1)_{T_1}\oplus O(-1)_W
          \longrightarrow P^1_S\bigr)\times C^*_z.
 \tag{GC.12}
\]

The physical circle acts only on the z factor. The full source
functions are q1=S0 W and q2=S1 T1, independent of that factor;
the original source parameter is carried by the same analytic
inverse of q1-q2 as in GC.1. In particular T1=W=0 is the entire
exceptional P1 times C*, carried by (GC.11), not a point removed
from its domain. Its R=0 locus needs no positive-norm flow to
make this product map defined.

The physical line on this piece has a specified trivialization.
Use the convention that a physical positive circle frame p and
its coefficient w represent the vector wp; consequently
(gp,g inverse w) represents that same vector. The actual
weight-one coordinate z gives

\[
                  [p,w]\longmapsto z(p)w.             \tag{GC.13}
\]

The formula is invariant and invertible because z is nowhere
zero on this piece. It is the coefficient arrow in this chart,
not an assertion about its extension through z=0 or through the
next source reset. The complex derivative of (GC.11) in the
ordered (V,z) block is

\[
              \begin{pmatrix}z&V\\0&1\end{pmatrix},
 \tag{GC.14}
\]

with all source coordinates retained. This carries the canonical
complex spin-c structure by its actual exterior-algebra map.
Its determinant z is retained; no single-valued square root on
the z circle is asserted. The chart's physical line trivialization
alone does not discard a transition contribution at its boundary.

The marked G divisor in the final node coordinates is S1-S0=0,
by EA.45. In particular the coordinate S0=F+ in (GC.11) is not
the old Cartesian coefficient s0. Any next-source transition
uses the actual EA.43--46 unit and the chronological reset,
before one assigns a marked source section to an upper point.
The full two-step outside attachment remains the next map to
be checked; (GC.11)--(GC.14) establish the complete upper chart
without assigning that attachment or an individual return.


## GC.6. The proper upper graph and its actual primitive endpoint

Put T0=W=zV in (GC.11), and use the four invariant conifold
functions

\[
 q_1=S_0T_0,\quad q_2=S_1T_1,\quad
 C=S_0T_1,\quad D=S_1T_0,\qquad q_1q_2=CD.
 \tag{GC.15}
\]

The rational opposite source ruling [T0:T1] is retained by its
actual graph, not made into a coordinate at T0=T1=0. Its proper
common resolution has homogeneous coordinates [S0:S1], [t0:t1],
a coefficient eta of O(-1,-1), and the nonzero z. Its two
projections are

\[
 ([S],[t],\eta,z)\longmapsto
       ([S],T_0=\eta t_0,T_1=\eta t_1,z),
\]
\[
 ([S],[t],\eta,z)\longmapsto
       ([t],A_0=\eta S_0,A_1=\eta S_1,z).
 \tag{GC.16}
\]

Explicitly the two auxiliary scalings multiply S and t by
alpha and beta and eta by (alpha beta) inverse. This gives
both inverse ordinary blowup charts wherever t0 or t1 is
nonzero. The first projection is precisely the blowup of the
normal ideal (T0,T1) of the upper exceptional P1; the second
contracts the other projective factor. Both retain the source
functions q1=eta S0 t0 and q2=eta S1 t1. The physical circle
acts only on z, so the graph and both proper source products
are free on this entire upper piece. Their physical coefficient
arrow is the pullback of (GC.13), including eta=0.

Here the full theta unit has a useful exact extension. Retain
Q=q1 q2 uQ, P=uP/q2 and uG=uQ uP. In the S1 chart TL uses
S=S0/S1 and

\[
 E=\frac{2\Theta_Q(S)}{(1-S)\Theta_Q(S/P)}.
 \tag{GC.17}
\]

This unit descends to the full conifold (GC.15). Indeed its
normally convergent product factors are expressed by

\[
 QS=u_Qq_1C,\quad Q/S=u_Qq_2D,\quad
 S/P=C/u_P,\quad Q/(S/P)=u_GD.
 \tag{GC.18}
\]

For every higher power of Q multiply the first two expressions
by that power minus one. The apparent marked-section factor
1-S is already divided out. All numerator and denominator
factors are therefore holomorphic and nonzero on a sufficiently
small full conifold neighbourhood, including both S charts and
both target t charts. Their product converges normally there.
The value at the vertex is exactly two. This supplies an
extending logarithm of E/2 on that neighbourhood, without
replacing E by its vertex value. In particular

\[
                              L=E z
 \tag{GC.19}
\]

is the same actual nonzero physical coefficient over the whole
upper graph. It descends through each projection in (GC.16),
since E is a function of the four common invariant functions.

The endpoint is the actual inverse primitive. On the original
Tate torus, with the precise source/Cartier map of TL and SZ.43,
its input coefficients are

\[
              Z_0=u_GD,\qquad V_0=P(C/u_P)L.
 \tag{GC.20}
\]

The identity is first read in the S1 chart, where it is TL.11
with the actual U=S0 z coefficient. The homogeneous line-frame
arrow on the other S chart is exactly TL's retained Cartier
transition; (GC.18) gives its extension. Applying U1 inverse,
which has the literal torus map (Z,V) to (PZ,c_X V), gives

\[
 Z_1=Pu_GD,\qquad V_1=u_X C L,
                  \qquad c_X=q_2u_X .
 \tag{GC.21}
\]

No q2 factor or source translation has been discarded. On the
t1 chart of (GC.16), with t=t0/t1 and coordinates (A0,A1),
these formulas read

\[
 q_1=A_0t,\quad q_2=A_1,\quad C=A_0,\quad D=A_1t,
\]
\[
 Z_1=u_Gu_Pt,\qquad V_1=u_XA_0L,\qquad
 L_1=Z_1V_1/q_1=(u_Gu_Pu_X)L .
 \tag{GC.22}
\]

The last expression is interpreted in its actual toric edge
chart. The unit character on the unshifted negative diagonal
{e1,e2} is ZV/q1. Thus L1 is an extending nonzero coefficient
at A0=0 and t=0, rather than a division performed only after
restricting to that divisor. The source node coordinate
q1/Z1 is A0/(uG uP), with its full unit.

On the t0 chart put p=t1/t0, so q1=A0, q2=A1 p,
C=A0 p and D=A1. Carry the actual source period
h:(Z,V) to (QZ,PV), including P. Then

\[
 Z_2=QZ_1=q_1u_G^2D,\qquad
 V_2=PV_1=u_Pu_X(A_0/A_1)L,
\]
\[
             L_2=Z_2V_2/q_1^2=u_G L_1.
 \tag{GC.23}
\]

These are the other indexed node/edge coordinates. Relative to
the first q1 fan chart the h arrow translates the edge by e1;
its unit character is ZV/q1 squared. The full q2-dependent
period P is still in (GC.23). The corresponding marked source
infinite chart is also literal: S'=1/(uG A1), so its reciprocal
coordinate is uG A1, its q1 coordinate is A0 and its second
normal coordinate S' q2 is p/uG. These are regular coordinates
with invertible unit factors at p=0 and A0=A1=0. Thus both
projective target charts are retained, with their actual source
and line arrows. Their line overlap L2=uG L1 is an extending
unit; its logarithm is carried with the original Cartier map.
It is not a free change of the suspension marking.

The inverse primitive belongs to the two-object cap sequence
(GC.9)--(GC.10). In the direction used above its root square is

\[
                    F_\epsilon U_1^{-1}
                         =U_{\rm cap}^{-1}F_{\epsilon+1}.
 \tag{GC.24}
\]

Both finite characters are retained. The complete B inverse is
U1 inverse twice followed by the scalar (minus2 lambda q1)
inverse, and its cap square is the inverse of (GC.8).
Equations (GC.16)--(GC.24) give the full upper proper graph and
its one-primitive endpoint through the intermediate object.
They do not replace that composite by its normal-cone limit or
assert that one primitive is an automorphism of the original
cap object. The remaining finite-strip assembly must glue its
two chronological primitive graphs with this intermediate object
and the single whole fixed trace; that assembly is not inferred
solely from the local upper line trivialization.
