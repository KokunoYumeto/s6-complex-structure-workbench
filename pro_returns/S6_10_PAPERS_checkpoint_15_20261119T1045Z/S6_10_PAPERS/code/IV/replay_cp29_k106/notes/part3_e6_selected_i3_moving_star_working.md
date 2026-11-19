# Selected-I3: the actual moving fixed-face star and its normal lines

This is the selected face in the executed p=0 corner of SI3.9, for
the M6,b=1,m=2,n=1 family with scalar root s^2 r0. The local charts,
their normal derivatives and their integral compact divisor classes are
computed here. The original parameter closing and the reference Hopf
cap are retained in MS3.5; their completed characteristic pairing is
still being assembled.

## MS3.1. The full selected face and its quotient coordinates

Use the actual lattice (Z,V_pt,ord p,ord P), with physical circle
delta=(0,1,0,0). The selected face is
\[
 F_-=(0,0,1,0),\qquad F_+=(0,1,1,0).
 \tag{MS3.1}
\]
Its normal weights are -1,+1 in that order. For every final corner
chart the certificate computes the full inverse matrix, selects its
nonzero physical weights, and applies the unique period carrying
those two rays to MS3.1. There are exactly 36 resulting charts. Their
period words are (0,0) except for the one negative horizontal chart,
whose word is (1,0). That word is the actual h map
\[
 (Z,V_{\rm pt},p,P)\longmapsto(pP^3Z,P^6V_{\rm pt},p,P).
 \tag{MS3.2}
\]
Both its monomials and its inverse are retained. No B word or c0
factor occurs in this particular selected-star alignment. A period
fixing MS3.1 must have both integral components zero: on their sum
the lower period matrix is twice the identity. Thus the aligned
charts have no residual period identification along the surface.

The lattice quotient by the saturated span of F_-,F_+ is explicitly
\[
 (z,v,r,h)\longmapsto(z,h).
 \tag{MS3.3}
\]
Every aligned chart has two tangent columns and their images have
determinant of absolute value one. The resulting 36 two-cones have
37 rays. Their ordered boundary rays are (1,0),(-1,0); every other
ray has positive second coordinate. Each consecutive determinant is
one, and the union is the closed upper half-plane. The exact list and
each original four-cone are saved in the companion JSON.

Consequently these are the usual affine charts of a smooth toric
surface F_star over D_P, with dense functions Z,P. The projection to
P1_Z times D_P is the identity on these two dense characters. On
each chart it is the explicit nonnegative monomial map in the
chosen Z or Z^-1 chart. Its inverse on the dense open set is that
same pair of characters. The common-face localizations glue them.
The support equality proves properness: every arc valuation in a
coarse upper half-plane cone belongs to one of the saved refined
cones, where its monomial map extends uniquely.

## MS3.2. The chronological ordinary blowups

The original product fan has rays (1,0),(0,1),(-1,0). The certificate
removes, in its saved order, every added ray r whose current neighbours
r_minus,r_plus satisfy r=r_minus+r_plus. It retains all three product
rays and ends at that product fan after 34 removals. Reversing this
list is an actual sequence of ordinary complex blowups. In the
current source coordinates each step is given by
\[
 (x,y)=(a,ab),\qquad (x,y)=(cd,d).
 \tag{MS3.4}
\]
The inverse localizations are b=y/x and c=x/y. Composition gives the
full saved monomial matrix of every selected surface chart. Every
centre lies in P=0, so this modification is identity on the whole
outer parameter collar. This proves the stated 34-fold modification
as an actual morphism, including all infinitely near centres.

Let D0,Dinfty be the strict divisors of Z=0 and Z=infinity. Write
C_r for each vertical ray r=(a,h), h>0, in its actual ray order. The
line overlap in two adjacent charts gives
\[
 C_r^2=-\det(r_{\rm prev},r_{\rm next}),\qquad
 C_r C_{r'}=1
 \tag{MS3.5}
\]
for consecutive vertical rays; all other off-diagonal intersections
are zero. These formulas follow by substituting the two inverse
monomial charts and reading the normal coefficient on C_r. The
complete integral matrix I is stored. The principal divisors of the
actual functions Z and P give the two full relations
\[
 \operatorname{div}(Z)=D0-Dinfty+\sum_r aC_r,\qquad
 \operatorname{div}(P)=\sum_r hC_r.
 \tag{MS3.6}
\]
The matrix check is I(h_r)=0. The compact representative of D0-Dinfty
is therefore -sum aC_r, and its square, computed by this integral
matrix, is -3. This also follows from the same chronological maps:
three centres lie on the successive strict Z=0 section and no centre
lies on the Z=infinity section.

## MS3.3. The two actual derivative line maps

Define the following meromorphic functions in the aligned torus:
\[
 F_+=V_{\rm pt}/Z^2,\qquad
 F_-=pZ^2/V_{\rm pt},\qquad F_+F_-=p.
 \tag{MS3.7}
\]
Their characters are (-2,1,0,0) and (2,-1,1,0). The first has
order one on F_+ in MS3.1 and zero on F_-; the second has the reverse
orders. Thus in each of the 36 charts their full expressions are
\[
 F_+=n_+ g_+(t_1,t_2),\qquad
 F_-=n_- g_-(t_1,t_2),
 \tag{MS3.8}
\]
where n_plus,n_minus are the actual physical normal coordinates and
the two g functions are the explicitly saved tangent monomials.
There is no second normal coordinate in either factor. Their full
normal derivatives are g_plus dn_plus and g_minus dn_minus.

Every vertical tangent ray has the actual four-dimensional lift
(a,2a,0,h). Hence both derivatives in MS3.8 have zero vertical order.
The positive horizontal lift is (1,0,1,0), with orders (-2,3) for
(F_plus,F_minus). The negative horizontal lift is (-1,1,1,0), with
orders (3,-2). These are obtained from the original matrices after
the complete h arrow MS3.2; they are not chosen extension frames.

The derivative dF_plus is a meromorphic section of N_plus^*, so its
displayed divisor represents c1(N_plus^*). The analogous statement
holds for dF_minus. This fixes the frame-versus-coefficient sign and
gives the integral classes
\[
 c_1(N_+)=2[D0]-3[Dinfty],\qquad
 c_1(N_-)=-3[D0]+2[Dinfty].
 \tag{MS3.9}
\]
Both have degree -1 on the generic fixed P1. The actual
positive-weight spinor is E=conjugate(N_minus) direct-sum N_plus;
conjugating the negative physical coordinate reverses its Chern
class. Consequently
\[
 c_1(E)=5([D0]-[Dinfty])=-5\sum_r a[C_r],\qquad
 \langle c_1(E)^2,[F_{\rm star}]\rangle=-75.
 \tag{MS3.10}
\]
The pairing uses the stated compact representative. It is an integral
intersection of the saved exceptional classes, with the whole central
fibre relation retained.

## MS3.4. The source height and the point-to-tensor boundary arrow

The original source parameter and selected height remain
\[
 s=P(p-1)/u_s(P,pP),\qquad q_{\rm old}=Pp c_q(P,pP).
 \tag{MS3.11}
\]
On F_star one has p=0, so s=-P/u_s(P,0). Its derivative at zero is
-1 and its inverse is holomorphic on a smaller disc. It therefore
carries a positive P meridian to the positive original s meridian.
All unit derivatives in this coordinate change remain part of the
original determinant comparison of SI3.9.

On the outer parameter collar use the ordinary fixed-edge native
coordinates (Z,a_N,c_N), with q_old=Z a_N c_N and V_pt=c_N.
The exact map from MS3.7 is
\[
 a_N=P c_q Z^{-3}F_-,\qquad c_N=Z^2F_+.
 \tag{MS3.12}
\]
Its product with Z is precisely q_old. Its inverse divides by the
displayed nonzero factors on each common localized chart. The second
source chart has Z'=Z^-1, a_N'=Za_N, c_N'=Zc_N, preserving the
ordinary O(-1) coefficient convention at both endpoints.

The original M6 point-to-tensor function is also retained. On the
selected normalization its actual value, including the D-source
scaling, is
\[
 \chi_6(P)=\frac{D^5}{6+20w^2+6w^4},\qquad
 w=\frac{P-1}{P+1},\quad D=w^2-3.
 \tag{MS3.13}
\]
Indeed f6_old=D^-5 f6_new and the full Miller/theta identity EG.12
is f_P^6/f6_new=f_(P^6)/(6+20w^2+6w^4). Thus the positive native
normal is multiplied by chi6 and the negative one by chi6^-1.
Its value at P=0 is -1. Off the selected fixed surface the factor is
the entire source/Miller/theta quotient on the actual annulus, with
its inverse; its restriction MS3.13 supplies the normal derivative
because q_old has zero first normal derivative on the fixed sphere.
The prescribed finite character and both original r6 arrows remain
in the separate cap square SI3.9a--b.

Each blowup MS3.4 has Jacobian a or d. It gives the actual integral
exceptional class of square -1, changes c1 squared by -1 and Euler
number by +1. The maps are identity on the outer collar, so the
relative tangent Pontryagin number of F_star compared with the
product P1 times D is exactly 34(-1-2)=-102. This relative number
does not yet use a reference cap.

## MS3.5. The retained parameter closing

The ordinary forward endpoint of the coupled root s^2r0 is
q_old^2; the finite-cap forward endpoint is h^2, and their complete
sector square is SI3.9b. On the selected corner one may reindex by
the actual B^-2, with c0=(p-1)^4c. Substitution into the entire torus
map gives the exact quotient representative
\[
 E:(Z,V_{\rm pt})\longmapsto
 \left(P^2 Z,\ P^{-2}(c_q/c_0)^2 V_{\rm pt}\right).
 \tag{MS3.14}
\]
The inverse has the reciprocal coefficients, evaluated on the same
base functions. Both maps commute with the actual periods and the
physical circle. On each nonzero parameter fibre they extend through
every fixed selected fan chart by its full torus character, including
the normal jets. Their P powers have winding (2,-2); the unit ratio
is retained with its chosen analytic logarithm on the selected disc.

The source Möbius arrow of MS3.14 and its normal spinor arrow are
therefore part of the required parameter/cap gluing. No extension of
that P-winding through the central fourfold is asserted here. The
completed Hopf-cap map, the resulting closed E bundle and its second
Chern number, the remaining fixed components and the outer physical
return are still being evaluated. MS3.10 and the relative tangent
number are local geometric inputs to that subsequent construction.

The companion code/part3/e6_selected_i3_moving_star.py saves all36
four-cone matrices, their actual period words and normal derivatives,
the 37 quotient rays, all34 chronological blowups, the complete
integral intersection matrix and the full forward endpoint identity.
