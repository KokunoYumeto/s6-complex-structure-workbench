# E6 selected I3 generators at w=+1 and w=-1

Working exact maps. This note starts with the actual datum M6=O(6G-O),
translation by -G, quadratic cap m=2, norm n=1, and its retained finite
line character. It has not assigned a completed return. The two local
ordered-node markings and the full selected-height factor are kept.

## SI3.1. Source, parameter and selected height

In the original source
\[
 y^2=x^3+rx^2+tx+t^2,\qquad G=(0,t),
\]
put
\[
 v=w^2-1,\quad D=v-2,\quad r=(1-2v)/D^2,
 \quad (X,Y,T)=(D^2x,D^3y,D^3t).
\]
The inverse divides by these same units near either w=+1 or w=-1.
The source and selected height are exactly
\[
 Y^2=X^3+(1-2v)X^2+DTX+T^2,
 \qquad q=T-v=D^3q_{\rm old}.
 \tag{SI3.1}
\]
Here s=1/4-r=v(v+4)/(4D^2), so ds/dv=1/4 at zero.
Each positive small w-loop has local degree one over this original
source meridian. There is no division of a return class in this statement.

Set s0=v+v^2/4 and
\[
 U=Y-T-DX/2,\qquad V_s=Y+T+DX/2.
\]
Then UV_s=X^2(X-s0). In the actual smooth chart obtained from the
ordered source resolution, write
\[
 U=Xz,\quad V_s=X\omega,\quad
 X=s0+z\omega,\quad Y=X(z+\omega)/2,
 \quad T=X(\omega-z-D)/2.                 \tag{SI3.2}
\]
The selected node is z=-v/2, omega=v/2, X=v,Y=0,T=v.
These are the same functions as the selected normalization
X=S^2-1,Y=S(S^2-1-v), at S=+w and S=-w.

## SI3.2. An explicit full selected-node tube

Write a=z+v/2 and b=omega-v/2. Direct substitution gives
\[
 q=-\tfrac14\{(2b+v)a^2-2b(b+v+2)a+vb^2\}.
 \tag{SI3.3}
\]
Choose R_b=((b+2)^2+4v)^{1/2}, with value 2 at the origin, and put
K=b+v+2+R_b. Both are analytic units on a sufficiently small fixed
bidisc. The literal coordinate map is
\[
 x=a-vb/K,\qquad y=\{bK-(2b+v)a\}/4,
 \qquad q=xy.                              \tag{SI3.4}
\]
The identity follows by multiplying out: the numerator of q-xy is
a b[-R_b^2+(b+2)^2+4v]. The parameter v is unchanged. Its normal
Jacobian at a=b=0 is sqrt(1+v), with the branch equal to one. To
write the inverse without dropping the q dependence, solve
\[
 b=\frac{4y+vx}{2(R_b(b,v)-x)},\qquad
 a=x+vb/K(b,v).                            \tag{SI3.5}
\]
On a smaller compact v-disc the denominators are units. The derivative
in b of the right side of the first equation is bounded by a constant
times |4y+vx|. After shrinking the x,y ball it is less than 1/2 and
maps a fixed small b-disc into itself. Its convergent successive
substitution supplies the unique holomorphic inverse; substituting
it into SI3.4 proves both inverse identities. This is the full tube
map, including the actual selected height and its normal derivatives.

## SI3.3. Actual Tate and point-line arrows at the collision

Use the original-source Tate isomorphism E81.1--5, with its fourth-root
unit equal to +1 at (s,t)=(0,0). Retain its convergent inverse Tate
series, actual point P=Z_T(G), and R=Q/P^2. They give analytic source
coordinates
\[
 Q=P^2R,\quad P=t u_P,\quad R-P=s u_s,
 \quad u_P(0)=2,\ u_s(0)=1.
\]
The colliding discriminant factor is exactly
Q=t^2 q_old u_Q, with u_Q(0)=8. Consequently
\[
 q_{\rm old}=R c_q,\qquad c_q=u_P^2/u_Q,
 \qquad c_q(0)=1/2.                       \tag{SI3.6}
\]
All these are equalities of the actual inverse Weierstrass functions.
In particular the selected-height zero is the R divisor.

Retain the full rational Miller factors f2,f3,f6 and r6=f6^-1 from
EN.3 and E68--73. The actual suspension is
\[
 B_{\rm sel}=(q_{\rm old}/t^3)f_2^6
                  f_6(p-G)/f_6(p).
\]
The D source scaling gives f2_old=D^-1 f2_new,
f6_old=D^-5 f6_new, hence B6_old=D^-6 B6_new. Thus its transformed
coefficient is exactly q B6_new/T^3, with the original scalar retained.

In the balanced Tate coefficient
\[
 V_T=Z_T^{-3}f_P(Z_T)^6 r_6(p)v_M
\]
the literal periods are
\[
 h:(Z_T,V_T)\mapsto(P^2R Z_T,R^{-3}V_T),\qquad
 B:(Z_T,V_T)\mapsto(P^{-1}Z_T,\lambda R c_q K V_T),
 \quad K=(P/t)^3\eta^6,
 \tag{SI3.7}
\]
where eta is the full theta expression E81.6; K(0)=8. The ordered
source extension is the full s Delta V_T of E73/E90. Its actual
point-theta comparison is
\[
 s\Delta V_T=P^6U_6(P,R)Z_T^{-3}V_{\rm pt},\qquad U_6(0)=-1.
 \tag{SI3.8}
\]
Every s, Delta, P and Z_T factor is retained; this is not an assertion
that either meromorphic frame extends through its displayed divisor.
At s=0 the actual norm from E81.9 is
\[
 hB^3:(Z_T,V_T)\mapsto(Z_T,(4\lambda)^3V_T),
 \tag{SI3.9}
\]
since the selected original height is then t itself.

For the explicit coupled scalar lambda=s^N lambda0, put R=pP and
W=Z_TV_T. The exact periods become
\[
 h:(Z_T,W)\mapsto(P^3p Z_T,p^{-2}W),
\quad B:(Z_T,W)\mapsto(P^{-1}Z_T,
                  P^N p(p-1)^N c(P,p)W),
\]
where c=lambda0 c_q K u_s^-N is an actual extending unit, with
central value 4lambda0. This retains the additional selected-height
factor R relative to E88's unselected calculation. For m=2 take the
literal scalar root s^{N/2}r0 when N is even. No completed common fan
or characteristic count has yet been extracted from these periods.

## SI3.4. The two ordered branch markings

The full chosen Tate Weierstrass unit has value +1 on the original
source at the collision. On the selected normalization its coordinate
is (2tau-1)/(2tau+1) at the central fibre, where tau=S/D. The marked
root 2w/D is +1 at w=-1 and -1 at w=+1. The two analytic fourth/sixth
root choices therefore differ exactly by the constant sign throughout
the corresponding bidisc. The full Tate inversion, not just its
central restriction, gives
\[
 Z_T=Z_w\quad(w\hbox{ near }-1),\qquad
 Z_T=Z_w^{-1}\quad(w\hbox{ near }+1).
\]
Their no-period-shift choice is fixed on the selected punctured nodal
normalization: at w=-1 the point P_G has order +1 in v; at w=+1 its
inverse has order +1. A nonzero Q shift would not have that finite
nonzero nodal value for each nonzero v.

In the genuine point-theta frame the complete theta identity gives
\[
 (Z,V_{\rm pt})\mapsto(Z^{-1},P^6V_{\rm pt}).
\]
Composing with the actual target source period (Q,P^-6) gives
(Q/Z,V_pt). It acts on every Cox character by the literal substitution,
and sends the fan to its reflected fan J. Both original source/target
r6 arrows in SI3.8 remain part of this map. The two local marked
generators are therefore compared with this transported fan.

## SI3.5. The unchanged quadratic root and remaining attachment

On the actual infinity cap the source maps are E70--71, now with the
colliding selected root t_coll(s). The analytic factor is
h=1-t_coll(s)z^2, so h(0,z)=1. The root equation, its three A2 charts,
the four fixed-point blowups, the point-line ratio v0/(v0-L6(s,z^2)),
and the formal half S with 2S=-3G' all extend on this same source disc.
The full root line coefficient is h z^-2 B6', with central value 4.
The odd-log finite averaging and actual analytic norm root of E71 give
A0^2=Bsel', commuting with Bsel'; its prescribed (-1)^d character is
retained. The scalar root multiplies this A0, with both norm factors
on their actual annular domains.

Here is the full restored annular reference and parameter arrow. Write
rho for the logarithmic scalar-root parameter, ell_alpha for the actual
chosen logarithm of q_infty on its sector, and J_alpha for the integer
sector cochain from E77. With the full base reference map retained, put
\[
 \Phi_{\rho,\alpha}
 =e^{2\pi i\rho\ell_\alpha}B_\rho^{J_\alpha}
       (B_{\rm base}^{-J_\alpha}\Phi_{{\rm base},\alpha}).
 \tag{SI3.9a}
\]
The equality J_beta-J_alpha=j_alpha,beta retains the original source
period Pi and line-lattice Lambda on every sector overlap. The root
r_sc=s^2 r0 makes two positive scalar-root turns on a positive s-loop.
Thus Phi_(rho+2)=q_infty^2 Phi_rho and, because
q_infty q_old=h, its exact forward square is
\[
 \Phi_{\rho+2}q_{\rm old}^{\,2}
       =h^2\Phi_\rho.                     \tag{SI3.9b}
\]
The endpoint-to-initial arrows are q_old^-2 and h^-2. At the selected
zero of q_old the ordinary forward arrow is expressed using the actual
B^2 reindex and its complete source/line coefficient. Its zero remains
the selected-height divisor. Replacing the previous cap height factor
by h changes E71's normalized lift by the fixed analytic invariant
square root of h_new/h_old. This carries its norm and finite character
exactly. The independent cap audit retains both arrows in this square.

The remaining work is the actual common selected-fan/chronological
source-strip/point-line attachment for SI3.7, its reference-relative
cap cochain and compact exterior, followed by the oriented return.
The source, line, root and branch maps above assign no such return.

## SI3.6. Two literal periodic parent fans

Take the particular even scalar exponent N=4 and keep its root
s^2 r0. On p=R/P the unit c in SI3.3 has value 4lambda0. On the
other base chart u=P/R retain f=(1-u)^4 lambda0 c_q K u_s^-4.
Writing V_C=s Delta V_T, the exact point-line arrows from E93 are
\[
 V_C=-U_6u^{-6}R^{-3}V_{{\rm pt},R},\qquad
 V_{\rm reg}=u^6V_C=-U_6R^{-3}V_{{\rm pt},R},
\]
\[
 T_{\rm reg}=V_{\rm reg}^{-1}
       =-U_6^{-1}R^3 V_{{\rm pt},R}^{-1}.       \tag{SI3.10}
\]
The direct and dual arrows are separately typed. The period words
K=hB^2 and J=hB act on the direct coefficient by
\[
 K:(V_{\rm reg},Z)\mapsto(R^7f^2V_{\rm reg},RZ),\qquad
 J:(V_{\rm reg},Z)\mapsto(R^2fV_{\rm reg},R^2uZ).
 \tag{SI3.11}
\]
They recover h=J^2K^-1 and B=KJ^-1 with the full f factors.
For r=ord R,z=ord u the exact matrix is
\[
 M(r,z)=\begin{pmatrix}7r&2r\\r&2r+z\end{pmatrix},
 \qquad\det M=12r^2+7rz.                    \tag{SI3.12}
\]
The linear inspection map (X,Y)->(X,2Y) carries the original
integer lattice isomorphically onto Z times 2Z; that target lattice
is retained. In these inspection coordinates the matrix is
symmetric, [[7r,2r],[2r,4r+2z]]. The actual integral quadratic
function on the period labels is
7r binom(n1,2)+(4r+2z) binom(n2,2)+2r n1 n2.
Its negative-square affine interpolation has the nonnegative
transverse jumps 2r,5r,2r+2z. The exact difference under a period
label is n^t diag(1,2)M ell. Its dual cells therefore translate
by that same matrix; pulling them back by the specified lattice
isomorphism gives the original-lattice hexagon
\[
 (0,0),(-5r,0),(-7r,-r),(-7r,-2r-z),
                 (-2r,-2r-z),(0,-r-z).       \tag{SI3.13}
\]
The opposite faces are glued by K,J,KJ^-1, respectively. This
constructs their whole periodic support and common faces.

The saved exact fan has the following finite construction. Its
upper polygon at r=1,z=0 is triangulated into all 24 primitive
lattice triangles. Cone those to A=(0,0,0,1); cone A and
B=(0,-1,0,1) to the five consecutive bottom horizontal edges and
the remaining diagonal edge. The latter tetrahedron has determinant
two. The primitive ray (-1,-2,1,1) is half the sum of its four
generators; its four stars have determinant one. This gives 33
regular four-cones. The certificate checks every inverse monomial
matrix, the physical vector (1,0,0,0), and all three complete sets
of period facets with the respective full f powers 2,1,1.
The source monomials QZ and Z^-1 have nonnegative exponent rows
Y+3r+2z and -Y on every cone. The original volume is the full
E95.13 expression (2J_ts/a_T) R dR du dlog(V_reg) dlog Z, so its
retained canonical order is 2r+z-1 on each primitive ray.

At the selected p=0 boundary use the genuine point-theta frame
V_pt. Keep the local analytic unit
\[
 c_0=(p-1)^4c,\qquad c=\lambda_0c_qK u_s^{-4}.
 \tag{SI3.13a}
\]
The factor p-1 is nonzero on this selected neighbourhood. On the
common overlap the full c_0 power is expanded as the displayed
(p-1)^4 and c powers; its central value is 4lambda0. Its actual periods are
\[
 h:(Z,V_{\rm pt})\mapsto(P^3pZ,P^6V_{\rm pt}),\qquad
 B:(Z,V_{\rm pt})\mapsto(P^{-1}Z,P^2p c_0V_{\rm pt}).
 \tag{SI3.14}
\]
The valuation matrix is p I+P H, H=[[3,-1],[6,2]]. Its determinant
is p^2+5pP+12P^2. Thus the p-boundary is the literal prescribed
negative-square fan. For the two triangles in basis e1,-e2, the
three staircase prism cones have oriented determinants
(1,2,12) and (1,3,12). The full piecewise-linear prism map retains
the base coordinates and intertwines translation by the displayed
matrix. On each fixed positive base slice it is a bounded periodic
perturbation of the invertible linear period map. It is proper and
has degree one. At every point its local fibre is isolated because
each incident full linear cone is nonsingular. Its local degree is
positive: a nearby regular value in any incident open cone has a
positive preimage, and local degree is constant in the small target
ball. The sum of these positive local degrees is one. It follows
that the whole map is one-to-one and onto. Boundary slice maps are
the explicitly invertible I and H maps. This proves common faces
and full support for this uncollapsed six-cone parent fan.

On the generic common overlap its complete line comparison is
\[
 V_{\rm reg}=p^{-6}P^6U_6 Z^{-3}V_{\rm pt}.    \tag{SI3.15}
\]
In particular its common cocharacter map is
(zeta,nu,h)->(-3zeta+nu+6h,zeta,h); the P^6 height translation
and p^-6 U6 unit are retained. Reindexing periods by (K,J) gives
exactly SI3.12. This supplies the two actual parent arrows. A
simultaneous refinement with the p=1 charts and all finite Cartier
graphs is the next attachment task, not a consequence of the
33-cone count alone.

## SI3.7. The moving normalization's two source blowups

The selected normalization has the exact resolved coordinates
\[
 z=S+1-\frac{v(S+1)}{2(S-1)},\qquad
 \omega=S-1+\frac{v(S-1)}{2(S+1)}.             \tag{SI3.16}
\]
At S=1 its graph is Bl_(S-1,v); at S=-1 it is Bl_(S+1,v).
In S-1=r,v=r k the first map becomes
z=(r+2)(1-k/2), omega=r(1+rk/(2(r+2))). In S+1=r,v=r k
the second becomes z=r(1-rk/(2(r-2))), omega=(r-2)(1+k/2).
The projective reciprocal charts are the other charts of these
same blowups. They preserve SI3.1--2. The exceptional curves map
to omega=0 and z=0, while the strict central normalization maps
to omega=z-2. The two selected preimages S=+w and S=-w lift to
the two retained endpoints over z=omega=0.

The full point divisor is not dropped at those endpoints. On the
normalization f6=(S+1)^6/(S-S6), where
\[
 S6=-\frac{32+48v+18v^2+v^3}{32+32v+6v^2}.
\]
Its contact with the actual branch -sqrt(1+v) has order six.
The original full s Delta r6 arrow therefore remains part of the
point-line comparison through the blowups. This section records
the source graph only; its completed normal determinant and the
moving cap have not yet been evaluated.

## SI3.8. Executed generic three-parent common refinement

On the base annulus where p and p-1 are units use the common torus
(V_reg,Z,R). Its physical cocharacter is (1,0,0), and its actual K,J
period matrix at R-order one is
\[
 M=\begin{pmatrix}7&2\\1&2\end{pmatrix},\qquad\det M=12.
 \tag{SI3.17}
\]
The fundamental hexagon is SI3.13 at r=1,z=0. Retain the full
unit f=p^-4(p-1)^4 c in SI3.11.

After the full point-line map SI3.15, the first parent's two raw
upper triangles are
\[
 ((6,0),(3,3),(-2,4)),\qquad
 ((6,0),(1,1),(-2,4)).                    \tag{SI3.18}
\]
Insert every integer point in these triangles in the saved order.
Each insertion replaces the containing triangles by joins to their
edges; all shared edge points are inserted on both sides. The resulting
24 triangles have determinant one. Their period translates are the
actual H-upper fan: SI3.18 is the image of the negative-square triangles
under H and the full affine height-one point-frame map.

At p=1 write v_1=p-1 and W_C=Z V_C. The exact periods are
\[
 h:(Z,W_C)\mapsto(P^3pZ,p^{-2}W_C),\qquad
 B:(Z,W_C)\mapsto(P^{-1}Z,P^4p v_1^4cW_C).
 \tag{SI3.19}
\]
On x_i y_i=P, x_i=Z/P^i, the line-chain equation is
U_j V_j=P^4v_1^4=x_i^4 y_i^4 v_1^4, with
U_j=W_C/(P^4v_1^4)^j. On the v_1-unit face the four x_i and four
y_i ordered factors give 24 upper triangles. For i=0,1,2 and
k=0,1,2,3 their native (ord Z,ord W_C) vertices are
\[
 ((i+1,k+1),(i+1,k),(i,0)),\qquad
 ((i+1,4),(i,k+1),(i,k)).                 \tag{SI3.20}
\]
The common cocharacter arrow is (a,b,h)->(-a+b,a,h), together with
V_reg=p^-6 Z^-1 W_C and R=pP. The source period changes i by three;
B changes i by minus one and j by one, carrying all units in SI3.19.
These are the complete labelled upper fans. The third parent is the
24-triangle upper fan already saved in SI3.6.

Intersect all translated first-parent triangles with the infinity
triangles, then with every translated SI3.20 triangle. Rational
half-plane clipping gives 634 positive-area cells of total area 12.
Insert all intersection points on both sides of every common edge,
including their periodic images on the hexagon boundary. Exact ear
triangulation gives 1068 primitive integral three-cones. For each
nonregular cone of determinant D the saved nonzero residue in its
half-open fundamental parallelepiped gives a primitive stellar ray.
Insert all its period images in the hexagon. The program explicitly
checks that a cone contains at most one nontrivial centre in this
orbit; every new determinant is a positive integer below its parent's.
The 1598 recorded steps produce 4264 regular cones.

The initial cells are intersections of three actual fans. The listed
edge subdivisions, triangulations and stellar subdivisions preserve
all common faces. The final exact edge incidence is also checked:
6361 interior edges occur twice and 70 boundary edges once. Each
complete pair of boundary ray/facet sets is carried by K,J,KJ^-1.
The sum of the final rational slice areas remains 12. Thus the
constructed fan has full support and the literal period gluing in
the original lattice.

Here is the full unit dictionary in this finite export. A first-parent
chart translated by K^i J^j has its translated common matrix P_0 and
common torus coefficient vector equal to the product
\[
 p^{(-6-i-2j,\ i+j,\ 1)}\,
 v_1^{(8i+4j,0,0)}\,
 c^{(2i+j,0,0)}\,U_6^{(1,0,0)}.
 \tag{SI3.21}
\]
The second parent has exactly the first three factors and its own
matrix P_1. The infinity parent already uses the common torus. In
particular the third p component is the actual R=pP equality and is
included before the inverse map. If T=u y^P=z^N is the common torus
map, the literal child-to-parent arrow is
\[
 y=u^{-P^{-1}}z^{P^{-1}N}.                \tag{SI3.22}
\]
Every entry of P^-1 N is a nonnegative integer. All three parent
matrices and all inverse unit exponent vectors are saved per child.
Their maps agree on each common-face localization because they give
the same torus functions. An arc valuation in a parent cone lies in a
child cone, so its nonnegative monomial map extends the arc; the common
face arrow proves uniqueness. This proves properness of the displayed
common modification. The unit functions remain analytic and invertible
on this precise generic annulus, with all parameter derivatives.

The actual source functions recorded for every child are
\[
 QZ=p^{-2}R^3Z,\qquad Z^{-1}.             \tag{SI3.23}
\]
Both exponent rows are nonnegative on the common hexagon. The original
source volume retains the full E95.13 expression
(2J_ts/a_T)R dR du dlog(V_reg)dlog Z, u=p^-1. Thus its original
canonical order on a ray (x,y,h) is 2h-1, with the full derivative unit
and the sign du=-p^-2dp retained. No Spin trivialization is assigned.

The reproducible code/part3/e6_selected_i3_common_fan.py and JSON
save every cell, ray, star, parent matrix, period, physical weight and
unit arrow. A console-only Fraction serialization failure is preserved
under records/attempts/e6_selected_i3_common_output_fraction: it occurred
after all geometric assertions and the full JSON export. The corrected
complete execution exits successfully with empty stderr. The remaining
stage is the four-dimensional corner extension relative to the selected
boundary and its full finite source, Cartier and cap attachment; this
section assigns no return.

## SI3.9. The two executed relative corner lifts

For the p=0 corner use lattice (Z,V_pt,ord p,ord P) and the
actual period matrices I,H of SI3.14. Its six raw prism cones are
the two unit-square triangles joined by the three literal staircase
tetrahedra of SI3.6. The upper common rays (X,Y,h) are carried into
this lattice by the exact inverse of SI3.15:
\[
 (X,Y,h)\longmapsto(Y,X+3Y-6h,0,h).
 \tag{SI3.24}
\]
Before this map, every common cone is translated by the inverse of
its saved first-parent K,J label. Thus it lies in precisely its
original raw upper triangle; the inverse period and its full unit
factors remain part of the common-face arrow.

For each raw four-cone, subdivide its upper face by this common
fan and join every resulting face with the unchanged complementary
lower face. On an upper edge take exactly the common edges lying
on that edge, with their primitive ray heights retained; on an upper
ray retain that ray. All adjacent joins agree because the upper
subdivisions agree on their common faces. Each join fills its original
cone, so this is a proper subdivision with the same support. It has
4330 full cones. Every determinant is one or two. Apply the saved
periodic residue-star algorithm only to its nonregular cones. All 21
chosen primitive centres have both base coordinates strictly positive.
Each affected cone meets at most one translated centre, and its child
determinants strictly decrease. The resulting 4402 cones are regular.
The full 4264-cone generic boundary and the literal two-triangle
selected T0 boundary remain unchanged.

At infinity use lattice (V_reg,Z,ord u,ord R). Its lower period
matrix is [[0,0],[0,1]] and its upper matrix is SI3.17. Apply the
same upper-face joins to the actual 33-cone fan of SI3.6. This yields
4308 cones, all already regular, with the same generic boundary.
Its lower primitive chain is unchanged. The lower kernel generated
by the first period is recorded; it is not removed by a finite cover.

Every cone has an exact map to its original raw quotient chart. If
P is the original integer matrix of a raw cone, its cover is C^4
with finite group of order abs(det P). For a nonnegative exponent
vector a, the invariant condition is that a^t P^-1 is integral.
All invariant monomials with 1<=sum a_i<=abs(det P) are retained.
They generate the invariant ring: in a longer zero-sum sequence of
characters, two of the first |G|+1 partial sums agree, yielding a
nonempty zero-sum subword of length at most |G|; remove it and repeat.
For a regular child N the full arrow on each retained generator is
\[
 x^a\longmapsto z^{\,a^tP^{-1}N}.        \tag{SI3.25}
\]
All entries are nonnegative integers, and every generator arrow is
saved. The maps satisfy every relation because their common torus
characters agree. Common-face localization glues them. Their support
and the preceding arc-valuation argument give properness. No cover
chart is substituted for its finite quotient in this construction.

The periods on all final facets are exact. With n=(n1,n2), the p=0
torus map is
\[
 (Z,V_{\rm pt},p,P)\mapsto
 (p^{n1}P^{3n1-n2}Z,\ p^{n2}P^{6n1+2n2}c_0^{n2}V_{\rm pt},p,P).
 \tag{SI3.26}
\]
At infinity it is
\[
 (V_{\rm reg},Z,u,R)\mapsto
 (R^{7n1+2n2}f^{2n1+n2}V_{\rm reg},
             R^{n1+2n2}u^{n2}Z,u,R).
 \tag{SI3.27}
\]
For each paired facet the export retains its integral period vector,
vertex permutation and target inverse-matrix powers of c_0 or f. The
zero-corner output names that function c0 and records its full identity
c0=(p-1)^4c; the earlier c slot and proof are preserved under
records/attempts/e6_selected_i3_before_c0_dictionary. Thus
these formulas give actual full-function maps, including their normal
jets, in every resolved chart. Internal facets occur twice; protected
generic and selected facets occur once. The complete facet table is
checked, not only its number.

The original base functions are also retained. At zero they are
s=P(p-1)/u_s, t=P/u_P, q_old=Pp c_q and Q=P^3p. At infinity they
are s=R(1-u)/u_s, t=Ru/u_P, q_old=R c_q and Q=R^3u^2. The full
volume in SI3.8 gives logarithmic character (0,0,1,2) in either
of the displayed corner orders. At zero, for example,
R dR du=-P dP dp and the line map is SI3.15, so the unit and its
minus sign remain in that exact wedge. Every final ray therefore
carries its original canonical order r+2s-1, without a Spin claim.

The complete output code/part3/e6_selected_i3_corner_lifts.json
retains both corner fans, all 830858 executed assertions, original
quotient-generator maps, physical weights, full facets and period
units. Its earlier formatted JSON is preserved losslessly under
records/attempts/e6_selected_i3_corner_pre_volume_export. A separate
initial parenthesis typo and its failed execution are retained under
records/attempts/e6_selected_i3_corner_syntax. These two exact toric
lifts do not replace the remaining finite source/Cartier attachment
and cap-reference proof.

## SI3.10. A retained source-line class on the normalization graph

Let F be the actual source graph in SI3.7, with exceptional curves
Eplus over S=1 and Eminus over S=-1. These curves map with degree one
to C2 and C1, respectively; the strict central normalization maps to
C0. The original coordinate relation is z_old=z/D,
omega_old=omega/D, so this identification includes the sign D(0)=-2.
The full E73 Cartier arrow s Delta r6, pulled back by SI3.16 and its
other projective charts, is the line map being used here.

The integral Picard lattice of F is freely generated by the pullback
of O_P1(1), Eplus and Eminus. This follows directly from the two
ordinary blowup charts and the exponential sequence: H1(O)=H2(O)=0
on P1 times the disc and remains zero under each point blowup. Its
intersection matrix on the exceptional summand is diag(-1,-1).
The generic degree of the actual M6 pullback is zero, so its first
Chern class has no O_P1(1) coefficient. The E73 component degrees
(0,3,-3), transported by the preceding actual source maps, imply
\[
 c_1(M_6|_F)=3[Eplus]-3[Eminus],\qquad
 c_1(M_6|_F)^2=-18.                       \tag{SI3.28}
\]
The strict central component has degree zero because it intersects
both exceptionals once. This computes the Chern class of the stated
source-line pullback. Its complete Cartier coefficients remain those
of s Delta r6. The fixed-graph lift, normal spinor/Cox comparison and
moving Hopf cap still have to be constructed before this class enters
any fixed-surface or return calculation.
