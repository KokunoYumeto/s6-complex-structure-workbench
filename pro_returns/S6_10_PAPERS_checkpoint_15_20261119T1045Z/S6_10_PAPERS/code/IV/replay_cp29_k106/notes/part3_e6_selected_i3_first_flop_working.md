# Selected-I3: the actual diagonal native product and first flop

Working proof, 18 November 2026. This note uses the complete original
source, point line, quadratic cap and reference maps of SI3 and ASI3.
The source is y^2=x^3+r x^2+t x+t^2, with G=(0,t), M6=O(6G-O),
translation -G, s=1/4-r, m=2 and norm n=1. The finite line character
is unchanged. The scalar root is the actual fixed r_base chosen in
ASI3, so lambda_base=r_base^2. The positive loop is a single positive
s-circle. Its initial fan is T0 in the unit-+1 original Tate marking.

The two relative integers below are evaluated on the actual exterior
of C2. Their map to the central flop coordinate is displayed in
IF3.5. The physical characteristic pair of the completed fixed-C0
quotient has its own displayed map to the same absolute return in
IF3.6. Every coefficient in the two maps is retained.

## IF3.1. The full fixed-scalar family and its identity closing

On a uniform selected q_old-disc over this parameter circle, use the
actual point-theta coefficient V=V_pt. SI3.7--8 gives

\[
 h:(Z,V,q)\mapsto(\kappa qZ,\alpha V,q),\qquad
 B:(Z,V,q)\mapsto(gZ,\eta qV,q),\qquad q=q_{\rm old},
 \tag{IF3.1}
\]
\[
 \kappa=P^2/c_q,\qquad \alpha=P^6,\qquad
 g=P^{-1},\qquad \eta=\lambda_{\rm base}K P^{-3}.
 \tag{IF3.2}
\]

These are equalities of holomorphic functions of q and the cut source
parameter. Indeed Q=P^2R and q=R c_q. The balanced line coordinate
has h multiplier R^-3 and B multiplier lambda_base R c_q K.
The actual point comparison is
s Delta V_T=P^6 U6 Z^-3 V. Multiplying its Z^3 factor after h gives
Q^3 R^-3=P^6; after B it gives P^-3. This proves both line
coefficients in IF3.2 with the full U6 and source/target r6 factors
carried by the same comparison. On the selected circle P has winding
one. The complete units c_q and K extend and are nonzero on the
original small bidisc, so their based logarithms have winding zero.
The single winding matrix, in the displayed h,B order, is therefore

\[
                    \begin{pmatrix}2&-1\\6&-3\end{pmatrix}.
 \tag{IF3.3}
\]

All original source and point-line charts are single-valued in s on
this circle. The infinity cap is the actual SI3.5 cap: its source
equation, three A2 charts, four fixed-point blowups and point ratio
v0/(v0-L6(s,z^2)) are holomorphic in s. Its lift has norm
A0^2=B_sel', commutes with B_sel', and retains (-1)^d. The full
sector reference at the fixed scalar is the restriction at rho=0
of ASI3.8. Its Pi, Lambda and integer J_alpha are carried throughout
the source circle. Those data were constructed on the source disc
in SI3.5, including the actual height h=1-t_coll(s)z^2 and its
chosen invariant analytic norm root. Thus the original source,
line, root and cap endpoint maps on this fixed-scalar loop are the
identity in those original charts. The integral q-sector arrows
remain the same on both endpoint sheets. No scalar-period reindex
is inserted in this closing.

The local Tate coordinates are periodic as well: their marked
Weierstrass unit and the section P are the specified analytic
choices on the selected punctured bidisc. The original q and the
identity closing are retained under that coordinate arrow. Each
conifold cell has trivial period stabilizer. Work on one quotient
representative and extend all maps below to its translates by the
literal h,B maps IF3.1.

The six-chart overlaps in coordinates (a,b,c), (u,v,w), with
q=abc=uvw, are exactly

\[
\begin{array}{c|ccc}
 &u&v&w\\\hline
 C_0&\kappa\alpha bc&\alpha^{-1}ab&\kappa^{-1}b^{-1}\\
 C_1&g\eta bc&\eta^{-1}c^{-1}&g^{-1}ac\\
 C_2&a^{-1}&ab&ac.
\end{array}
\tag{IF3.4}
\]

In particular the single native C2 product is literal:
(z,c0,c1)=(a,b,c), (z',c0',c1')=(u,v,w),
z'=z^-1 and c_i'=z c_i. Its seam is the identity. Specify its
double to be the pullback of this very product under the degree-two
parameter map. At the intermediate and final cuts the coordinate
seams are again the identity. The full cap and q-sector arrows are
pulled back at the same time. This specifies the square before any
calculation of a free coordinate.

## IF3.2. The ordinary double product with all q-dependent inverses

Write the double circle as s=s_* exp(2i theta), 0<=theta<=2pi.
Keep the first vertex. At the second use
(u,eta(q,s)v,kappa(q,s)w), with the same reference transformation
at s_*. This is a full coordinate arrow: its new coordinate product
is H_s(q)=q eta(q,s)kappa(q,s). Recover q by H_s^-1 and then divide
the last two coordinates by their actual units evaluated there.
H_s'(0) is a unit. Compactness of the theta circle supplies one
smaller disc where this inverse is defined and injective.

In the ordered normal pairs (a,c), (a,b), (b,c), the complete
matrices are

\[
 D_0=\operatorname{diag}(\eta/\alpha,\kappa\alpha),\quad
 D_1=\operatorname{diag}(\kappa/g,g\eta),\quad
 D_2=\operatorname{diag}(\eta,\kappa).
 \tag{IF3.5}
\]

Their common determinant winding is 2t with t=-1. The first
diagonal windings are l=(-18,6,-6). For each full entry divide by
its reference value at the same q and its displayed angular factor.
The resulting winding-zero loop has its actual based periodic
logarithm on the uniform q-disc. Call the two logarithms k_i0,k_i1.
They retain every q-derivative of the original units.

For an integer d define the based quaternion path

\[
 H_d(x,\theta)=
 (\sin\vartheta(x)e^{id\theta}+j\cos\vartheta(x))
 (\sin\vartheta(x)+j\cos\vartheta(x))^{-1},
 \tag{IF3.6}
\]

where vartheta is endpoint-flat with values 0 and pi/2. Thus
H_d(0,theta)=1, H_d(1,theta)=exp(id theta), and both theta
endpoints are one. In Q=n0+j conjugate(n1), the real normal map
Q -> H_t Q H_(l_i-t) has angular endpoint factors
(exp(i l_i theta),exp(i(2t-l_i)theta)). Compose it with the two
diagonal exponentials of rho(x) k_ij(q,s), using the same full
source height. Its second radial end is exactly
D_i(q,s_*)^-1 D_i(q,s); its first end is the identity.

Here is an explicit inverse for the full interior arrow, including
the quaternion mixing. On a tube with bounded base z, write this
real map as F_(z,theta)(n)=A_(z,theta)n+G_(z,theta)(n), where A is
its invertible value at q=0 and G is the actual difference. Because
q=z n0 n1, the full unit dependence gives G=O(|n|^3), uniformly
with its first derivative on the compact base and parameter
collars. Choose the normal radius so that
||A^-1 D G||<1/2 there. The inverse is the unique fixed point of
n -> A^-1 n' - A^-1 G(n), obtained by its convergent iteration.
It depends smoothly on all the displayed variables. Its transported
height is exactly z n0 n1 evaluated at this recovered n. At the
second vertex it is the H_s inverse already specified. This
construction never identifies the new mixed normal product with
the old q.

The radial-end equality z D_i(q,s_*) K_i=z D_i(q,s) is an exact
equality in the two vertex charts. It glues these tube maps to
the vertex arrows. Restore the full nonlinear chart maps by the
normal rescaling R_tau(z,n)=(z,tau n) and the cutoff flow of the
velocity of R_tau^-1 F R_tau. Its invertible linear endpoint and
the same compact inverse bound give the uniform tube. The flow
fixes the protected vertex collars; the interiors of the three
curve tubes are disjoint. Carry the rounded boundary by that same
isotopy. All constructions are periodic in the specified doubled
charts. They give the actual based ordinary plumbing product with
the unchanged source/cap closing and full q-normal jets.

## IF3.3. The integral action and derivative prisms

The physical vertex weights are (-1,0,1) and (1,-1,0). In the
ordered curve normals, the tangent weights and differences are
w=(0,1,-1), d=(-2,-1,-1). The above product carries the action to

\[
 Q\mapsto(H_t e^{-iw_i\phi/2}H_t^{-1})Q
          (H_{l_i-t}^{-1}e^{id_i\phi/2}H_{l_i-t}).
 \tag{IF3.7}
\]

The retained logarithmic factors and nonlinear rescaling supply
the based homotopy of this formula to the original normal action.
For U=cos x+j sin x and E_i=exp(i w_i phi/2), the actual trace
at q_H=1 is

\[
 E_i^{-1}U E_i H_t E_i^{-1}H_t^{-1}U^{-1}
       H_{l_i-t}^{-1}e^{id_i\phi/2}H_{l_i-t}.
 \tag{IF3.8}
\]

Direct differentiation in IF3.6 gives degrees -d and d for
H_d i H_d^-1 and H_d^-1 i H_d in the oriented path-parameter
sphere. The positive quaternion volume pairs an axis degree e
and angle c phi/2 with c e. In the Maurer product formula the
radial endpoint terms are constant central-sign maps, and the
parameter terms cancel in the periodic charts. Consequently the
actual normal-meridian and stable-derivative path degrees are

\[
 I_i=t w_i+d_i(l_i-t),\qquad
 W_i=t w_i-d_i(l_i-t).
 \tag{IF3.9}
\]

The stable chain rule is in the universal covering group of
stable GL^+, whose integral third class is identified with Spin
by the lifted polar deformation. Left quaternion multiplication
contributes its degree and right multiplication its negative.
The base rotation depends only on phi. At phi=2pi its Spin sign
(-1)^w_i cancels the normal sign. To close each path trace, use
generic normal sections at the vertices, join them by paths in
the corresponding links, and cap the parameter-independent end
orbits by D_theta^2 times S_phi^1, constant in the disc variable.
The vertex maps factor through dimension two. The full coordinate
to ambient stable-frame arrow extends over each annulus times
D4, which has H3=0. Thus it contributes zero to these capped
three-cycles. These are the actual CT/ST/DZ prisms with the
explicit IF3.4--7 chart maps.

Substitution gives

\[
              I=(34,-8,6),\qquad W=(-34,6,-4).
 \tag{IF3.10}
\]

For gamma_j=a_j-a_0=boundary x_j, the positive-circle boundary
identity boundary Delta=-Delta boundary gives
Delta x_j=w_j D_j-w_0 D_0. Therefore the actual variation and
ambient stable derivative satisfy

\[
 V(w_j e_j-w_0 e_0)=I_j e_j-I_0 e_0,\qquad
 w_j\delta_j-w_0\delta_0=W_j-W_0.
 \tag{IF3.11}
\]

For C2, w0=0 and w2=-1 give V22=-6 and delta2=-30.
The ambient-to-single-star frame is the literal map
c=u^-1 q_H. Its derivative has shear
dc=-u^-1(du)u^-1 q_H, removed by the invertible triangular
homotopy. Its normal-meridian third class is +1, exactly as in
K31's retained frame proof. With the oriented relative disc
D2=-[D3_y], its correction is -V22. Thus the actual ordinary
relative generators satisfy

\[
 2n_2=\delta_2-V_{22}=-24,\qquad
 m_2=-V_{22}-n_2=18.
 \tag{IF3.12}
\]

This determines the ordinary doubled pair (18,-12) without
assigning V00 or delta0.

## IF3.4. The native product and the literal relative square

The C2 native quaternion is
q_H=U(z)(c0+j conjugate(c1)), U(z)=(1+jz)/sqrt(1+|z|^2).
The actual native-to-ordinary boundary arrow of IF3.5--6 is

\[
 q_H\mapsto(U H_t U^{-1})q_H H_{l_2-t}.
 \tag{IF3.13}
\]

The unit logarithms and higher terms are the same ones in IF3.2.
The left factor has degree 2t=-2 on the Hopf-oriented sphere
times parameter: substituting the path IF3.6 in the Maurer
boundary integral gives twice its angular winding. The right
factor has only radial and parameter variables and degree zero.
Extend the inverse factors over D3 times I by the explicit
boundary-cylinder retraction of OR.2. Its endpoint has degrees
(-2t,0)=(2,0). The factors extend over D3 times D4, so this
boundary change inserts no disc-supported central class. The
ordinary return is the native return followed by L^-2t.
Consequently the native doubled pair is

\[
                  (m_2^{\rm nat},n_2^{\rm nat})=(16,-12).
 \tag{IF3.14}
\]

Choose a family connection compatible with the single native C2
product of IF3.1. Its literal pullback to the double parameter
circle has endpoint f^2: both sheets have that same connection,
native product, identity original closing and cap-sector maps.
The ordinary connection used above, changed back by IF3.13, has
the same native boundary connection. Their affine interpolation
with that boundary fixed gives an isotopy of relative endpoints.
Hence IF3.14 computes the free coordinates of this actual f^2.
The K23 free-coordinate homomorphism to Z^2 sends f^2 to twice
those of f. Injectivity of multiplication by two in Z gives

\[
                         (m_{C2}(f),n_{C2}(f))=(8,-6).
 \tag{IF3.15}
\]

Only the free integral coordinates have been divided. The central
sphere coordinate is carried in the actual single family below.

## IF3.5. The full Cox flop and its oriented central coordinate

Use Cox coordinates (a0,a1,c0,c1) with auxiliary weights
(1,1,-1,-1), z=a1/a0 and native c_i^chart=a0 c_i. The height is
q=a0 a1 c0 c1. Any actual torus coefficient arrow (Z,V)->(AZ,DV)
has the complete lift

\[
 (a_0,a_1,c_0,c_1)\mapsto
 (a_0,(AD)^{-1}a_1,A c_0,D c_1).
 \tag{IF3.16}
\]

It preserves q, so its inverse uses reciprocal A,D at the same
q even for the full q-dependent units. It commutes with the
auxiliary action and the physical circle. Transport its Hermitian
metric and then take the common positive radial normalization.
The two small-resolution charts and their link are therefore
carried by one actual map, retaining the positive moduli.

For completeness let the four angular Cox weights be arbitrary
integers (A0,A1,C0,C1). Put
a=exp(i(A0-A1)theta/2), d=exp(i(A0+A1)theta/2),
e=exp(i(C0+C1)theta/2), b=exp(i(C0-C1)theta/2) and
S=A0+A1+C0+C1. With u=a0+j a1 and v=c0+j conjugate(c1),
q_H=uv, h=u i u^-1 and k=v^-1 i v, their literal changes are
u'=a u d, v'=e v b. Hence

\[
 h'=a h a^{-1},\quad k'=b^{-1}k b,\quad
 q_H'=a e^{hS\theta/2}q_H b=a q_H e^{kS\theta/2}b.
 \tag{IF3.17}
\]

Substitution proves (q_H')^-1 h' q_H'=k'. This retains all
four weights and both paired central endpoints. The positive
modulus and the full unit logarithm homotopies above carry the
same equality on the actual common conifold. The normal-rescaling
flow carries the higher germs on both resolutions simultaneously.

The actual common-link and exterior maps are thus

\[
 \tau(h,q_H)=(q_H^{-1}h q_H,q_H),\qquad
 T(y,q_H)=(q_H^{-1}yq_H,q_H),
 \quad T^{-1}(y,q_H)=(q_Hyq_H^{-1},q_H).
 \tag{IF3.18}
\]

They extend smoothly at y=0 and preserve the product exterior
orientation. Their two Hopf inverses choose one unit representative
u or v and use v=u^-1q_H or u=q_Hv^-1; changing that representative
is exactly the auxiliary circle. The six-sphere exterior and
unknot framing are the actual K23 products, transported by these
maps. The full period translates of the chosen cell use IF3.1.
The source, quadratic cap and annular maps off this small selected
neighbourhood remain the original maps.

Define the actual relative generators by a conjugation-equivariant
degree-one zeta:(D3,S2)->(S3,1), commuting with y:
L(y,q_H)=(y,zeta(y)q_H), R(y,q_H)=(y,q_H zeta(y)). Both extend
over D3 times D4. Let C be K23's oriented disc-supported generator,
whose central orientation is retained by the physical correction
K68. Its existing explicit commutator plumbing proof fixes that
sign. The literal identities T L T^-1=R and
T R T^-1=L^-1 R^2 C give, in these same relative products,

\[
 T(L^mR^n C^a)T^{-1}=L^{-n}R^{m+2n}C^{a+n}.
 \tag{IF3.19}
\]

The extension-by-identity injection of the relative group used in
K23 carries its exact doubled identity back to these marked
products. T fixes the oriented disc-supported subgroup. L and R
extend over the seven-disc and therefore have zero absolute
six-sphere return. Thus a is the actual absolute return of this
single family. Inserting IF3.15 sends its free pair to (6,-4)
and changes its central coordinate by exactly -6.

The periodic C2 flop changes the negative square triangles
{n,n+e1,n+e2}, {n+e1,n+e2,n+e1+e2} to
{n,n+e1,n+e1+e2}, {n,n+e2,n+e1+e2}. This is JT0.
It is also the complete fan T1=T(e1+e2,e2): its second
triangle is the first displayed positive triangle after the
literal translate n->n+e2. The source period and unit indexing
are those induced by IF3.16, without any additional closing.
The fixed reflection J(q_H)=k conjugate(q_H)k^-1 restoring the
first-resolution complex convention swaps the two free entries
and preserves the central entry, as in the full K23 chart arrow.

## IF3.6. The physical pair dictionary and the two ordered generators

The actual fixed-C0 normal product used in ASI3 is
q_H^0=U(b)(a+j conjugate(c)), whereas the C2 product above is
q_H^2=U(a)(b+j conjugate(c)). Both come from IF3.4. Their
ordinary-product comparison is the explicit D0 and D2 arrow
IF3.5, with the exact inverses and boundary changes IF3.2--4.
Their relative cycle and derivative evaluations are carried by
the common action prism IF3.11. In particular IF3.12 is the
coordinate map used for the C2 free pair.

For the fixed-C0 product, the actual K68 physical Hopf duality
and inverse-clutch map instead evaluates the completed physical
pair by

\[
 k_M=\mu_{C0}+\nu_{C0},\qquad
 \ell_M=4\mu_{C0},\qquad
 \frac{4k_M-\ell_M}{24}=\frac{\nu_{C0}}6.
 \tag{IF3.20}
\]

Here the underlying map is q_H^0 -> q_H^0 e^-i phi, with its
Hermitian dual on the quotient line and its adjoint normal
clutch; it is exactly the product Hopf cap retained in ASI3 and
MC3. In this numerical pair, MC3 defines
kappa=-75-c2(E_collision)+c2(E_reference), its actual
first-number difference. The actual fixed-star physical pair
from ASI3 is (-9-kappa,-228-4kappa). IF3.20 therefore gives
(mu_C0,nu_C0)=(-57-kappa,48) and index 8. This is the explicit
physical map used to obtain the base class. IF3.15 was obtained
by the distinct displayed C2 cycle/frame arrow IF3.12 and is
inserted into IF3.19, which gives its central change -6. These
two evaluations concern the same absolute return, carried
through the common chart and exterior maps above; neither
replaces the other's coordinate map.

Consequently the first reflected class is

\[
                 [\Phi_{T0}]=8,\qquad [\Phi_{JT0}]=2
                    \quad\text{in }\mathbb Z/28.
 \tag{IF3.21}
\]

The full source reflection SI3.4 sends (Z,V_pt) to
(Z^-1,P^6 V_pt); applying the actual target h gives
(Q/Z,V_pt). It retains both Miller r6 factors and the root/F0
maps and has positive local degree one on the s-meridian.
Since Z_T=Z_w near w=-1 and Z_T=Z_w^-1 near w=+1, the exact
global ordered w-generator table is therefore

\[
\begin{array}{c|cc}
 &T0\text{ in }Z_w&JT0\text{ in }Z_w\\\hline
 w=-1&8&2\\
 w=+1&2&8.
\end{array}
 \tag{IF3.22}
\]

The cap order, norm sign, finite character and scalar basepoint
remain those fixed at the start. This computes these actual
first diagonal flops and the transported opposite marking.
It does not assign an arbitrary-fan return or an individual
value to kappa.

## Exact certificate

The accompanying `code/part3/e6_selected_i3_first_flop.py` executes
1,004 exact checks. It retains the balanced-to-point frame squares,
all three six-chart unit arrows, the q-preserving Cox lift and
reciprocal inverse, each determinant and prism substitution, the
actual native free pair, and the fixed-C0 physical coordinate map.
Ninety-six independent rational quaternion samples check the full
unrestricted four-weight identity, paired endpoints and the literal
T L T^-1=R map. The exact integral fan triangles and K23 coordinate
conjugation are recorded separately. The coupled trace row is saved
only as the stated algebra diagnostic; the proof uses the direct
fixed-scalar family above. The smooth inverse, actual relative
square, frame and cap arguments are proved in IF3.1--6 and are not
inferred from finite sampling. Source, script and dependency hashes
are included in the output.
