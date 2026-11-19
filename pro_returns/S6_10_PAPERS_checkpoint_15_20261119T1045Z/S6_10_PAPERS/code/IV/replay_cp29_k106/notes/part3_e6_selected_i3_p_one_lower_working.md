# Selected-I3: the four lower surfaces with their actual normal coefficients

This note reads the executed 4,392-cone atlas I3P.1--4. It identifies
its 128 lower charts, their actual source blowups and the full
point-line comparison on the marked collar. The global cap and outer
return are not evaluated here.

## I3L.1. Source charts and the actual normal rows

For lower interval k=0,1,2,3 in source cell i, the factor-parent chart is
\[
 U_j=P^4v^k a,\qquad V_j=v^{3-k}b,\qquad
 v=ab,\quad P=x_i y_i.
 \tag{I3L.1}
\]
The physical weights of (x_i,y_i,a,b) are (0,0,1,-1). In each of the
128 child charts the complete parent matrix has its last two rows
equal to the two distinct coordinate rows for a and b. Its first two
rows vanish in those columns. Thus the fixed surface is exactly
a=b=0; its two normal directions are the actual parent a,b directions,
without a source-dependent monomial factor from this refinement.

The source rows on the remaining two columns give the monomial map
\[
 (x_i,y_i)=
 (t_1^{r_1}t_2^{r_2},\ t_1^{s_1}t_2^{s_2}).
 \tag{I3L.2}
\]
Each matrix has determinant of absolute value one and nonnegative
entries. All four lower intervals have exactly the same source fan
in each source cell. The executed chart numbers are 16,7,9 for
i=0,1,2. Their rays run from (1,0) to (0,1), all consecutive
determinants equal +1 in that order. The certificate stores every
ray and both source rows of each of the 128 original parent matrices.

To give the actual modification, repeatedly remove an interior ray
r whose immediate neighbours r_-,r_+ satisfy r=r_-+r_+. The saved
sequence ends at ((1,0),(0,1)). Reversing the sequence inserts exactly
15,6,8 ordinary stars in the three source quadrants. Each insertion
is the usual two affine charts x=A,y=AB and x=CD,y=D in its current
source coordinates. Composing these literal maps gives exactly I3L.2.
All centres lie over the original node points, so these maps are
identity off those points and on the fixed outer source boundary.

After the actual period reindex described next, each of the four
surfaces is therefore the minimal I3 source surface with exactly
29 interior point blowups. This statement is the factorization of
the executed chart map, including infinitely near centres.

## I3L.2. The complete period representative and its normal frames

The full directed periods I3P.3 act on this chart by
\[
 h:(x,y,a,b)\mapsto(px,p^{-1}y,p^{-2}a,p^2b),
 \qquad
 B:(x,y,a,b)\mapsto(x,y,pc\cdot a,(pc)^{-1}b).
 \tag{I3L.3}
\]
The target cell labels are respectively (i+3,j) and (i-1,j+1).
Use the literal B^{-j} representative and put
\[
 I=i+j,\quad Z_*=P^j Z,\quad
 W_*=(P^4p v^4c)^{-j}W_C,\quad
 a_*=(pc)^{-j}a,\quad b_*=(pc)^j b.
 \tag{I3L.4}
\]
Substitution gives W_*=P^4v^k a_* and
P^4v^4/W_*=v^{3-k}b_*. In particular a_*b_*=v exactly.
On the fixed surface v=0, p=1, and these normal frames are
c^{-j}a and c^j b. The remaining h arrow has I mapped to I+3;
its source factors are (1,1) and its two normal factors are (1,1).
The source is thus the literal three-chart I3 model x_Iy_I=P,
with source period Q=P^3. The same invariant unit c(P,1) is retained
in the B^{-j} arrow before this restriction.

There is no first-order tangent-normal mixing: v=a_*b_* has zero
normal differential at a_*=b_*=0. Both p=1+v and every full unit
c(P,p),U_6(P,pP),u_s(P,pP) consequently have zero normal derivative
there. Thus the normal arrows in I3L.3--4 are the actual derivative
maps of the full family, with their displayed coefficient functions.

## I3L.3. Point-line coefficients and the retained boundary determinant

The full I3P.13 identity is applied after the same B^{-j} representative:
\[
 V_{{\rm pt},*}=P^{-6}U_6^{-1}Z_*^2W_*
          =P^{-2}v^kU_6^{-1}Z_*^2a_*.
 \tag{I3L.5}
\]
Its inverse line coefficient, using the opposite node branch, is
\[
 V_{{\rm pt},*}^{-1}
      =P^2v^{-k-1}U_6Z_*^{-2}b_*.
 \tag{I3L.6}
\]
Their product is a_*b_*/v=1 on the full torus. These are typed
coefficients of the original genuine point line and its dual; the
meromorphic P and Z_* factors remain part of their Cartier maps.

On the actual marked source collar, s=Pv/u_s. Taking the explicit
chain coefficients s^{-k}V_pt and s^{k+1}V_pt^{-1} gives the two
normal comparison scalars
\[
 H_{+,k}=P^{-2-k}u_s^kU_6^{-1}Z_*^2,\qquad
 H_{-,k}=P^{3+k}u_s^{-k-1}U_6Z_*^{-2}.
 \tag{I3L.7}
\]
They satisfy H_{+,k}H_{-,k}=P/u_s exactly. This keeps the original
point-line unit U_6, source unit u_s, the full Z_* exponent and the
source-normal product. These are boundary maps on the stated marked
charts; this note does not replace them by a trivial boundary gauge
or assign their closed-double normal Chern numbers.

## I3L.4. The relative tangent calculation

For each chart I3L.2 the source differential is
\[
 dx_i\wedge dy_i=
 \det\begin{pmatrix}r_1&r_2\\s_1&s_2\end{pmatrix}
 t_1^{r_1+s_1-1}t_2^{r_2+s_2-1}
 dt_1\wedge dt_2.
 \tag{I3L.8}
\]
The certificate stores this sign and both orders for every chart.
The original four-dimensional form still carries the I3P factor P;
its ray order 2h+t-1 is retained separately. No determinant phase
or divisor is discarded when identifying the tangent modification.

Each of the 29 actual interior complex blowups changes c1 squared
by -1 and c2 by +1, using the exceptional line of square -1 in the
pulled-back integral basis. Since the map is identity on the outer
source boundary, its relative tangent p1 difference is
\[
 \int(p_1(TF_{\rm refined})-p_1(TF_{\rm minimal}))
       =29(-1-2)=-87.
 \tag{I3L.9}
\]
This is the relative tangent number for each one of the four specified
surfaces. The normal boundary maps I3L.7, their closed-double pairings,
the finite cap and the global outer transfer remain separate data.
No total characteristic pair or return is asserted.

The complete source fans, chronological blowups, normal rows and full
coefficient identities are saved by
code/part3/e6_selected_i3_p_one_lower.py in its same-name JSON.
