# Selected-I3: the actual p-one Cayley corner

This construction uses the M6, b=1, quadratic norm-one datum and the
selected-height periods of SI3.19. It retains the chosen scalar root,
the original point-line arrow and the full unit c. Its output is the
four-dimensional corner atlas and its shared generic boundary; the
compact exterior, finite-cap attachment and return are not evaluated
in this note.

## I3P.1. Native charts and all period coefficients

Put v=p-1 and use the actual torus coordinates (Z,W_C,P,v), with
W_C=s Delta Z V_T. The periods are
\[
 h:(Z,W_C)\longmapsto(P^3pZ,p^{-2}W_C),\qquad
 B:(Z,W_C)\longmapsto(P^{-1}Z,P^4p v^4cW_C),
 \tag{I3P.1}
\]
where c=lambda_0 c_q K u_s^{-4} is the full analytic unit of SI3.19.
They fix P,v,p and c. On source and line cells (i,j), take
\[
 x_i=Z/P^i,\quad y_i=P^{i+1}/Z,\qquad
 U_j=W_C/(P^4v^4)^j,\quad
 V_j=(P^4v^4)^{j+1}/W_C.
 \tag{I3P.2}
\]
Thus x_i y_i=P and U_jV_j=x_i^4y_i^4v^4. The directed period maps are
\[
 \begin{array}{c|c|c|c}
 & (i,j)\text{ target}&(x,y)\text{ factors}&(U,V)\text{ factors}\\
 h&(i+3,j)&(p,p^{-1})&(p^{-2},p^2)\\
 B&(i-1,j+1)&(1,1)&(pc,(pc)^{-1}).
 \end{array}
 \tag{I3P.3}
\]
Each row follows by substitution into I3P.2, including the original
selected-height P factor in B. Opposite powers give the inverse arrows.

For j=0 the ordered list of four x, four y and four v factors has
twelve free-coordinate charts. For 0<=k<=3 these are
\[
 \begin{array}{c|c|c}
 \text{free coordinates}&U&V\\
 (a,b,y,v),\ x=ab&x^k a&x^{3-k}y^4v^4b\\
 (x,a,b,v),\ y=ab&x^4y^k a&y^{3-k}v^4b\\
 (x,y,a,b),\ v=ab&x^4y^4v^k a&v^{3-k}b.
 \end{array}
 \tag{I3P.4}
\]
The products in all three rows are x^4y^4v^4. In the lattice
(ord Z,ord W_C,ord P,ord v) put
\[
 I_k=(i+1,k,1,0),\quad J_k=(i,k,1,0),\quad E_k=(0,k,0,1).
\]
The ray matrices in precisely the free-coordinate order of I3P.4 are
\[
 (I_{k+1},I_k,J_0,E_0),\qquad
 (I_4,J_{k+1},J_k,E_0),\qquad
 (I_4,J_4,E_{k+1},E_k).
 \tag{I3P.5}
\]
Their determinants have absolute value one. The three source cells
i=0,1,2 give 36 parent charts. The last four charts join the upper edge
I_4J_4 to the four consecutive lower intervals E_kE_{k+1}.

## I3P.2. Pullback of the executed common generic fan

The input is the full 4264-cone generic common fan in
code/part3/e6_selected_i3_common_fan.json, with its exact one-parent
instances and period words. Its common torus is
\[
 (V_{\rm reg},Z_{\rm common},R,v)
       =(p^{-6}Z^{-1}W_C,Z,pP,v).
 \tag{I3P.6}
\]
For a common upper ray (A,B,h) whose saved parent has translate K^rJ^s,
where K=hB^2 and J=hB, set
\[
 A_0=A-(7r+2s)h,\quad B_0=B-(r+2s)h.
\]
Its native ray is (B_0,A_0+B_0,h,0). This is the actual inverse
character map followed by the inverse of that saved period translation.
The complete four-dimensional forward matrix is
\[
 F_{r,s}=\begin{pmatrix}
 -1&1&7r+2s&8r+4s\\
 1&0&r+2s&0\\
 0&0&1&0\\
 0&0&0&1
 \end{pmatrix},
 \tag{I3P.7}
\]
with coefficient vectors
\[
 p^{(-6-r-2s,\ r+s,\ 1,\ 0)},\qquad
 c^{(2r+s,\ 0,\ 0,\ 0)}.
 \tag{I3P.8}
\]
In particular the third p power is the literal R=pP equality. The
v exponent 8r+4s is a retained divisor at this corner. Equations
I3P.7--8 follow from the complete I3P.1 maps, since K has native
factors (Pp,P^8v^8c^2) and J has (P^2p,P^4p^{-1}v^4c).
No unit with nonzero v order is treated as invertible at v=0.

Join each pulled-back upper triangle to E_0. On the upper edge I_4J_4
of each native cell retain all subdivided intervals in the common fan,
and join each one to all four intervals E_kE_{k+1}. This is a subdivision
of the explicit parent cones I3P.5. The absolute determinant of each
upper star equals the absolute determinant of its upper three-cone.
For a top-edge pair with
coordinates (z_0,4h_0,h_0),(z_1,4h_1,h_1), the lower-join determinant
has absolute value |z_0h_1-z_1h_0|. The executable checks these primitive
determinants for every resulting cone.

For a child matrix N and its parent matrix N_0, the chart arrow is
\[
 x_{0,a}=\prod_b t_b^{(N_0^{-1}N)_{ab}}.
 \tag{I3P.9}
\]
All entries are nonnegative integers. The inverse torus arrow is
given by N^{-1}N_0 and agrees on localized common faces. The child
cones cover each parent: their rational volumes on ord P+ord v=1,
\[
 \frac{|\det N|}{6\prod_a(N_{P,a}+N_{v,a})},
 \tag{I3P.10}
\]
sum exactly to its volume. Disjoint interiors and shared faces are
inherited from the same generic subdivision and the interval joins.
The valuative chart maps I3P.9 consequently give the proper toric
modification of these actual factor charts, with their full source and
line functions retained.

## I3P.3. Period facets, source maps and original determinant

The full native lattice maps of h and B are
\[
 H=\begin{pmatrix}1&0&3&0\\0&1&0&0\\0&0&1&0\\0&0&0&1\end{pmatrix},\quad
 B_*=\begin{pmatrix}1&0&-1&0\\0&1&4&4\\0&0&1&0\\0&0&0&1\end{pmatrix}.
 \tag{I3P.11}
\]
For h^rB^s the full coefficient is p^(r,-2r+s,0,0)c^(0,s,0,0).
For a paired boundary facet with source matrix N_s and target matrix
N_t, the exact local arrow is
\[
 t'_a=p^{[N_t^{-1}(r,-2r+s,0,0)^t]_a}
 c^{[N_t^{-1}(0,s,0,0)^t]_a}
 \prod_b t_b^{[N_t^{-1}H^rB_*^sN_s]_{ab}}.
 \tag{I3P.12}
\]
The certificate retains every facet, word and exponent. Its columns
along the shared face are nonnegative, and the recorded complementary
coordinate is inverted. The inverse period gives the actual inverse
morphism there. Equality of both source and line expressions follows
by substituting the full torus expressions I3P.1--2; these identities
extend over the localized chart because every factor is holomorphic.

The source functions on each native child are Z and pP^3/Z. Their
exponent rows (1,0,0,0)N and (-1,0,3,0)N are nonnegative, and their
product is the actual Q=pP^3. The physical cocharacter is
delta=(0,1,0,0); its four chart weights are exactly N^{-1}delta.
The actual point-line identity remains
\[
 P^3W_C=pU_6 f_{p^{-2}}(Z)v_M.
 \tag{I3P.13}
\]
It follows from SI3.8 and the full theta shift
f_{P^6}=Z^2/(Q^3p^{-4}) f_{p^{-2}}. The P^3 Cartier factor is
retained even on P=0. The coincidence of the point section with O
continues to use this actual point-line graph and its marked modules.

The original canonical form is the unit 2J_ts/a_T times
P dP wedge dv wedge dlog Z wedge dlog W_C. Its order on a ray
(z,w,h,t) is 2h+t-1. This is the original determinant, including
the base-blowup factor P; it is not replaced by the residue form of
the binomial equation. The complete ray heights, physical weights,
canonical orders, common unit maps and parent arrows are exported.
The finite-cap and global boundary comparison remains a further
geometric construction and is not assigned a characteristic value here.

## I3P.4. Executed coverage and exact output

The complete execution gives 4,264 upper stars and 128 lower joins,
hence 4,392 regular four-cones. The subdivided upper edges have 16,
7 and 9 primitive intervals in source cells 0,1 and 2 respectively;
each is joined to all four lower intervals. Each parent volume is
verified separately in all 36 original charts. The generic boundary
has precisely the 4,264 input cones. The other 90 boundary facets
have their full native period partners, including their p and c
coefficient vectors. Every internal facet occurs twice.

The executable code/part3/e6_selected_i3_p_one_cayley.py exports the
complete ray and chart lists to the same-name JSON. It records the
input SHA, this proof SHA, every oriented column permutation, all
parent and localized-period monomial maps, source functions, original
determinant orders, physical weights and complete common character
coefficients. It recomputes each persisted common matrix from that
individual cone's rays, so a reference shared by two upper-edge
records cannot silently overwrite either chart map.
