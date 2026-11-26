"""Assemble the complete fresh LS proof from preserved notes and new geometry.

This writes a new proof file only. The earlier incomplete notes, mathematical
program, mathematical stdout/JSON, and both lossless readbacks are preserved.
The new prose proves the actual local maps and the full relative conclusion.
"""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256

ROOT = Path(__file__).resolve().parents[1]
LANE = ROOT / "agents/continuation7_iii_vertical_correction"
old = (LANE / "S6_SERIES_PUBLISH_III_02LS_fresh_vertical_notes.md").read_text()
period = (LANE / "S6_SERIES_PUBLISH_III_02LS_period_and_star_maps.md").read_text()
vertical = old[old.index("## 2. Root's local equation"):old.index("## 6. New OS45 computation")]
pending = """The present bounded computation checks these literal blocks and their
product for OS45. A complete all-profile period-coefficient verification
and the final local-map exposition remain to be finalized with root.
"""
assert vertical.count(pending) == 1
vertical = vertical.replace(pending, """Sections 6--7 below complete the actual punctured tensor/period maps,
their all-integer integrality, and the all-profile ordered identity.
The preserved earlier working note retains its then-incomplete wording.
""")
period_part = period[period.index("## 2. The exact punctured tensor"):period.index("## 4.")]
period_part = period_part.replace("## 2. The exact punctured tensor", "## 6. The exact punctured tensor")
period_part = period_part.replace("## 3. Unbounded integrality", "## 7. Unbounded integrality")

header = r"""# 02LS complete fresh derivation: vertical corrections and sixteen OS45 fillings

Checker: ChatGPT Pro mode; numerical reasoning effort is not separately
exposed. The LS original, old packet and historical target programs and
outputs remain closed. The LT and LU originals and historical target
algorithms likewise remain closed. This is the fresh proof before any
individual LS original release. Its final rereading and completion time
are recorded separately after this file has actually been read.

## 1. Claim, attribution, and exact input scope

The sole LS target exposure is the entire clean 47-line statement
agents/continuation7_iii_ls_statement/S6_SERIES_PUBLISH_III_02LS_statement_only.tex,
canonical lines20713--20759, SHA256
28e06fb3201b629a38501827be2c6f05963e9034c5c68c1d716d05b29894bcc3.
The permanent identity is maps:src:D.2.50, tag02LS, with displays
maps:eq:D.VC1/tag026E and maps:eq:D.VC7/tag026L.

For every one of the21 recorded rational elliptic surfaces, with
MW=ZG and height(G)=1/d0, the precise conclusion proved here is:
an integral vertical D makes
J_D=O(P-O+D) tensor T_Q^*O(P-O+D)^(-1) a base pullback exactly
when d0 divides ab, where P=aG,Q=bG are arbitrary signed multiples.
Its base degree is exactly ab/d0, and the ambiguity is the full
invariant component-orbit lattice. For positive a,b, all prescribed
nonnegative whole-fibre zero weights of this total give the stated
marked punctured period matrices. The sixteen OS45/default fillings
specified below are simply connected, have H2=H3=Z/b, and have the
other integral groups stated in Section13.

Root supplied the local/global vertical proof before any LS original
exposure. Sections2--5 preserve that proof with attribution and its
component/sign details. This lane supplied the punctured tensor/period
transport, the literal IC8 comparison, and the genuinely new OS45
calculation in the full integral six-coordinate fibre presentation.
The integral bar construction itself is the admitted LI input; its
natural coprime closed formula for the fibre quotient is not used.

Authorized inputs actually read for this task:

* The complete294-line admitted KT receiver in
  agents/continuation6_iii_d2/S6_SERIES_PUBLISH_III_02KT_receiving.tex:
  marked defining profiles, component maps, Poincare line maps,
  actual section-translation and logarithmic period construction.
* The complete499-line admitted LI receiver in
  agents/continuation7_iii_all_parity_receiving/S6_SERIES_PUBLISH_III_02LI_receiving.tex,
  and the complete270-line fresh bar core in its all_parity_root lane:
  the integral graph/bar inverse, peripheral words and all Thom columns.
  The earlier core's final unfinished paragraph is a historical scope
  statement; the admitted receiver supplies its completed scope.
* This lane's admitted LJ receiver, wholly read before its admission
  at08:51:05.219879 UTC, with Sections4--6 reread here: the general
  primitive rank-one/cusp chart and specialization maps. Their actual
  application to the new OS45 periods is proved below, rather than
  transferred from a natural-row coprimality assertion.
* The admitted KM fresh derivation, bounded rereading of lines289--408
  and1048--1075: the exact ruled normalization, its flat gauges,
  the primitive cusp specialization, fixed-sweep disc chains and
  Euler count. Admitted KQ receiver lines365--460 and708--725, and
  KO receiver lines92--145, were also reread at their actual
  primitive marked cap/chart scope. No claim of a new whole reading
  of these three large dependencies is made in this LS continuation.
* The raw fixture
  agents/continuation6_iii_d2/S6_SERIES_PUBLISH_III_02KY_raw_profiles.json,
  SHA256 6bda97b01ba63c0a796e3141609ca12e163791b626024b79104817ec5defc522;
  its defining OS45/default entry is reproduced in the new stdout.
* The complete newly written190-line LN markings source and all89
  actual output lines: all21 symbolic period products, component orders
  and explicit primitive periods. This computation was read, not rerun.
  Its authorship is attributed to the graph lane. LN was subsequently
  admitted at09:08:51 UTC. Only the raw symbolic identity and denominator
  scope are needed in the present proof.

For the separate bounded LU support, this lane read root's original
259-line h=1 cone note, all254 new cone-source lines and all33 stdout
lines, and subsequently all appended Sections9--12. Its local maps
are not needed as unproved premises for the sixteen all-Mumford
examples. The only LT exposure is its clean112-line statement; the
literal IC8 comparison remains in the separate preserved support note.

Primary support is Schuett--Shioda, Elliptic surfaces,
arXiv:0907.0298v3, 9July2010, https://arxiv.org/pdf/0907.0298v3 .
The PDF is retained outside W at
/workspace/scratch/bd22a44d51b1/primary_c7_ks/schuett_shioda_0907.0298.pdf,
SHA256 eeac47d53b52e96a1d2457a131dcce474332dd6b226e4dcd944575e995aa44b1.
Root actually visually read all of printed pp.25,32--34,50--52:
component groups/actual translation and the negative inverse-Cartan
height formula. This lane read root's entire exact primary scope note,
not those images anew in this continuation. That distinction is retained.

No Library, Space, prior-chat or held-canonical-source search was made.
No LS/LT/LU original or historical target calculation has been opened.

"""

new = r"""
### 7.1 All weights, signed endpoints, and the literal star choice

The full component-order table, in the recorded order within each
profile, is as follows. Each entry is the order of the G component.

|OS/profile|component orders|d0|
|--|--|--|
|43/default|2,1,1,1|2|
|43/II|2,1,1|2|
|45/default|8,1,1,1,1|8|
|45/II|8,1,1,1|8|
|46/default|4,1,1,1|4|
|46/II|4,1,1|4|
|47/default|7,2,1,1,1|14|
|47/II|7,2,1,1|14|
|47/III|7,1,1,2|14|
|49/default|2,3,1,1|6|
|49/II|1,3,2|6|
|49/III|3,2,1|6|
|50/default|4,3,1,1|12|
|50/II|1,3,4|12|
|50/IV|4,3,1|12|
|55/default|5,4,1,1,1|20|
|55/II|5,4,1,1|20|
|56/default|5,3,2,1,1|30|
|56/II|2,1,5,3|30|
|56/III|5,3,2,1|30|
|56/IV|5,2,3,1|30|

The symbolic LN source inserts independent weights at its recorded
multiplicative positions. Setting them all to zero proves the raw
ordered product I-(ab/d0)E_delta,gamma in every row. The elementary
matrix E=E_delta,gamma has E^2=0 and commutes with every displayed T:
all T fix delta and the gamma covector. Therefore inserting any
whole-fibre weight w at any chosen puncture multiplies the ordered
product by I+wE. A new regular puncture has B=I,g=0 and return
I+wE. Thus every nonnegative weight distribution allowed by the
claim has product I+(sum w-ab/d0)E, including distributions not
literally used as variables in that source. This extension is the
displayed matrix identity, not a new bounded numerical extrapolation.

For a=0 or b=0 the local equations admit d=0 and J_D has degree zero.
The group-law function can be taken to be1. For nonzero P=Q it is
the vertical function x-x(P); for P=-Q it is the tangent-line
function at P divided by the vertical function through2P.
In the other cases it is the line through P,-Q divided by the
vertical line through P-Q. These divisors are all
P-O-(P-Q)+(-Q). MW=ZG has no nonzero torsion, so these cases also
settle the possible coincident-point endpoints. Negative a,b use
the same functions, actual sections and component residues; no
positivity was used in the divisor, lattice or height proof.
Positivity is used only for the subsequent prescribed effective
zero divisor and contracting-family construction.

At the odd-star pair(2,2), one may use the root choice d_root=e1
in Section4. For the clean LT statement's literal IC8 convention
choose instead d_can=-e0. Then

    m_can=e0+e1-e2,       d_can-d_root=-(e0+e1).

The difference is the actual invariant near-leaf orbit divisor.
In D5 change the component coordinate order by
(0,1,4,5,2,3), whose inverse is itself. In D7 use
(0,1,6,7,2,3,4,5), with inverse(0,1,4,5,6,7,2,3).
If P is the row-selection matrix for this permutation, the exact
maps are x_new=P x_old and x_old=P^t x_new, with C_new=P C P^t
and S_new=P S P^t. The resulting multiplicities are
(1,1,1,1,2,...,2), the permutation is(01)(23), and the degree
is exactly(1,1,0,0,-1,0,...,0). Its multiplicity pairing is zero.
The invariant vector eta=-e4 satisfies m_can^t eta=1.
The separate star-order source/output displays every entry of
C,d_can,d_root,m_P,P,P^(-1),S,S^(-1),m,mu,eta in both cases.

The punctured tensor map for this change is multiplication by
the canonical section of O(-C0-C1), with division as inverse.
Section6 gives its full arrow ratio. No extension of that map
across the two different completed original caps is asserted.

## 8. The new OS45 data and the two literal vertical corrections

Number the five singular sites0,...,4, with0 the I8 site. The
raw defining elliptic returns and G cocycles are

    B0=[[1,8],[0,1]],       g0=(3,0),
    B1=[[1,1],[0,1]],       g1=(0,0),
    B2=[[3,4],[-1,-1]],     g2=(2,-1),
    B3=[[3,1],[-4,-1]],     g3=(1,-2),
    B4=[[0,1],[-1,2]],      g4=(0,0).

The positive primitive choices below satisfy
B_i-I=nu_i u_i(u_i^t J), u_i^t J v_i=1, and g_i=kappa_i u_i:

|i|nu|kappa|u|v|
|--|--|--|--|--|
|0|8|3|(1,0)|(0,1)|
|1|1|0|(1,0)|(0,1)|
|2|1|1|(2,-1)|(1,0)|
|3|1|1|(1,-2)|(1,-1)|
|4|1|0|(1,1)|(-1,0)|

Set the weight to one at a selected j in{1,2,3,4} and to zero
elsewhere. The height is1/8 and ab=8 in both pairs, so its total
is precisely the required one. At I8 the physical positive-valuation
component residues and the exact chosen corrections are

|a,b|p,q|d|m=e_p-e0+C d|
|--|--|--|--|
|2,4|2,4|(0,0,1,1,1,0,0,0)|(-1,1,0,0,-1,1,0,0)|
|4,2|4,2|(0,0,1,1,2,1,1,0)|(-1,1,-1,1,-1,1,-1,1)|

Both vectors satisfy S m=m, and d_q-d0=1 is the mixed local
height correction. The raw coefficient vector is d_raw,j=d_(-j),
with the same reflection as its inverse. Thus the first raw vector
is(0,0,0,0,1,1,1,0); the second raw vector is unchanged. All
irreducible I1 fibres need no component correction. At I8 both
P and Q are nonnarrow in these two examples, so the literal
component maps demonstrate the enlargement of the earlier
narrowness-OR input condition.

In the physical basis(e1,e2,delta,gamma), the local period return is

    T_i=[[B_i,0,b g_i],
         [-a g_i^t J B_i,1,c_i],
         [0,0,1]],
    c_i=w_i-ab*kappa_i^2/nu_i.

It is integral in every case, has determinant1, and the ordered
product T0 T1 T2 T3 T4 is I. Section6 gives its literal block
inverse and actual line/period provenance. These are also checked
exactly in the new program, before any filling calculation.

## 9. Actual primitive cap maps, with every inverse

Write S=(u,delta), L=(v,gamma) for the actual short and long
period columns. Their ambient order is interleaved as(u,v,delta,gamma).
The equality (T-I)L=S C and (T-I)S=0 has

    C=[[nu,b*kappa],[-a*kappa,c]].

### 9.1 The four unselected sites

At w=0 put d=gcd(nu,a*kappa), n=nu/d, A=a*kappa/d,
B=b*kappa/n. For the present rows B is integral and gcd(d,B)=1.
At I8 the triples(d,n,B) are(2,4,3) and(4,2,3).
At every I1 unselected site d=n=1. Choose

    n theta+A sigma=1,       d x+B y=1,
    C_S=[[n,sigma],[-A,theta]],
    C_L=[[x,-B],[y,d]].

Their inverse matrices are

    C_S^(-1)=[[theta,-sigma],[A,n]],
    C_L^(-1)=[[d,B],[-y,x]].

The equality
C=(n,-A)^t(d,B) gives C C_L=C_S diag(1,0).
Consequently the actual period basis

    (l,p0)=S C_S,   (h,w0)=L C_L,   H=(l,h,p0,w0)

has determinant1, with return h->h+l and all other columns fixed.
This argument explicitly proves primitivity for the even pair;
it uses no assumption gcd(a,b)=1. At I8 the matrices are

    (a,b)=(2,4):
      C_S=[[4,-1],[-3,1]], C_L=[[-1,-3],[1,2]];
    (a,b)=(4,2):
      C_S=[[2,1],[-3,-1]], C_L=[[1,-3],[-1,4]].

The coordinate changes act on the actual periods and unit
multipliers. Integer powers of the original long multipliers give
the h,w0 multipliers; C_L^(-1) recovers the originals. C_S acts
on the short algebraic torus by its integral monomial map:
on characters it is inverse transpose, and C_S^t is the inverse
character map. In universal logarithms these are the linear maps
C_S and C_S^(-1), followed by the original exponential and its
logarithm modulo the transported period lattice.

More concretely, exponentiate the primitive toric l coordinate to z.
The consecutive actual node charts and their inverses are

    X=z/q^j, Y=q^(j+1)/z, XY=q;
    z=X q^j, q=XY.

The primitive h period sends a chart to the next chart, with the
integer product of its original nowhere-zero unit multipliers.
Its inverse uses their reciprocals and the inverse period change.
The fixed p0,w0 periods give the elliptic base. Their multipliers
on the z line are constants on the universal cover of that base.
With logarithms of those constants, multiplication by
exp(-t1 log(mu1)-t2 log(mu2)) gives a smooth product frame;
multiplication by the positive exponent is its inverse. This is
an actual flat-line trivialization. It leaves all multipliers
in the formula instead of identifying them only by valuation.

The normalization is consequently a degree-zero ruled surface over
that elliptic curve. Its two pole sections are identified by a
translation a0. Choose a real lift of a0 and a function f on P1
with f(0)=0,f(infinity)=1. The two inverse maps
(z,x)->(z,x-f(z)a0) and(z,x)->(z,x+f(z)a0) give
(P1/(0~infinity)) times T2. The arc between the pole sections
supplies the graph circle h, and its products with the two
elliptic loops split the conductor sequence. Thus

    pi1=Z<h,p0,w0>,
    H1=Z^3, H2=Z^4, H3=Z^3, H4=Z.

In H coordinates and ordered wedge coordinates(12,13,14,23,24,34),
the exact fibre maps, with their indicated integral right sections, are

    f1(x)=(x2,x3,x4),
      s1(r,s,t)=H(0,r,s,t);
    f2(z)=(z12,z23,z24,z34),
      s2(r,s,t,u)=(wedge2 H)(r,0,0,s,t,u).

For physical input first apply H^(-1), or wedge2 H^(-1).
The H2 kernel is generated by e13,e14. These are the images
of e23,e24 under wedge2(I+E12)-I. Their physical preimages
are (wedge2 H)e23 and (wedge2 H)e24. This proves the exact
integral kernel, its saturation, and the specialization marking.

### 9.2 The selected cusp

Here nu=1,w=1 and

    C=[[1,b*kappa],[-a*kappa,1-ab*kappa^2]],
    C^(-1)=[[1-ab*kappa^2,-b*kappa],[a*kappa,1]].

The determinant is1, including kappa=0 and kappa=1. Use
H=(S C e1,L e1,S C e2,L e2); then
H^(-1)T H=I+E12+E34. The prescribed Mumford fan is taken
in this actual Jordan short lattice S C, with every triangle
and its unit multipliers retained. This is the monomial map
on characters induced by C^(-t), with inverse C^t, followed
by the period logarithm/exponential already specified. Thus
the map identifies both the punctured family and its prescribed
toric charts, not just their homology return matrices.

The fan has rays(v,1), v in Z2, and the two unimodular triangle
types(v,v+e1,v+e2) and(v+e1+e2,v+e1,v+e2). For each cone,
the three characters dual to its ray-column matrix are the
local coordinates; multiplying the ray matrix back recovers
the original characters. Long periods translate the cells and
multiply by the retained unit functions. The inverse uses the
inverse cell translation and the reciprocal functions. The
period translation lattice here is all Z2. It has one vertex
orbit, three edge orbits and two triangle orbits. A nonzero
translation fixes no finite nonempty cell. Hence the central
surface is irreducible, with its single hexagonal toric
normalization, its three paired conductor curves, and two
triple points. This also fixes its normal-disc multiplicity one.

The primitive specialization maps established in the admitted
Mumford cap input, now transported by these actual charts, are

    f1(x)=(x2,x4),       s1(r,s)=H(0,r,0,s),
    f2(z)=(z12,z14-z23,z24,z34),
      s2(r,s,t,u)=(wedge2 H)(r,0,s,0,t,u).

The two exact kernel vectors are e13 and e14+e23. Their
monodromy-cylinder preimages are e23 and e24-e23, since

    (wedge2(I+E12+E34)-I)e23=e13,
    (wedge2(I+E12+E34)-I)(e24-e23)=e14+e23.

The four section columns and these two kernel columns form
an integral basis. In particular no unsaturated rational
kernel is used. The toric cover and its contractible cell
charts give pi1=Z<h,w0>; the two long translations are its
generators, with their coordinate reading as inverse.
The primitive conductor calculation gives H2=Z4,H3=Z2,H4=Z.
Its H4 generator is the one oriented central component.

### 9.3 Full boundary kernels and extending normal markings

The unit-valued chart maps send the period origin to the
section with torus characters1, transported by those same
units. At a smooth point of the vertex-zero chart it extends
as a disc with positive base normal q. No affine boundary
translation has been inserted. The coordinate q and its
inverse chart map give the actual reduced meridian mu_i.
If one changes a temporary Cartier frame, its winding is
transported along with the meridian; the present marking
is the one specified by these extending origin discs.

Every fixed circle extends to the cap: in the rank-one case
these are l,p0,w0, and at the cusp they are the two toric
rotations. On a fixed vector the logarithmic terms cancel;
the retained unit factors give a time-one period and hence
the identity on the central fibre too. Apply this circle
action to the extending section disc. The negative of
circle times the oriented disc is a three-chain whose
boundary is the positive fibre-then-base sweep. Thus every
literal fixed sweep bounds, with this precise boundary
section and sign.

The Wang sequence reads a boundary H2 class first by its
fixed-loop sweep coordinate. Subtract the just described
bounding sweeps. The remainder is a fibre class, and the
f2 maps and their sections give its complete image and
kernel. Therefore the cap fibre kernels and those fixed
sweeps generate the entire integral H2 boundary kernel.
All these maps are onto H2 of the cap.

Likewise the fibre H1 kernel equals (T-I)Lambda in both
primitive models. Boundary H1 therefore splits as cap H1
plus the single extending meridian mu_i. The forward map
is the fibre specialization plus mu_i->0; its inverse on
cap H1 is the displayed fibre section. This exact fact
will determine the global relative kernel.

## 10. Full integral exterior coordinates and ordered normal columns

Let Lambda=Z4, B=wedge2 Lambda=Z6 in the physical wedge order,
and let V be the exterior with its five independent singular
base loops theta0,...,theta4. The ordinary sixth boundary is
theta_o=(theta0...theta4)^(-1). Its return is I. The origin
section and the actual period exponential identify V with
this linear torus bundle; the group logarithm modulo its
transported periods is the inverse. Put

    R=[wedge2 T0-I | ... | wedge2 T4-I],
    C=B/im R,
    D=[T0-I | ... | T4-I],
    K=ker D in Lambda^5.

The graph-of-mapping-cylinders sequence is
0->C->H2(V)->K->0 over the integers. Its first map is the
oriented fibre torus; its last map reads the loop on each
mapping cylinder. The new computation retains all six
coordinates of B and all thirty columns of R. In every
geometry the Smith factors of R are(1,1,1,1,2), so C has
a free generator and a genuine Z/2 generator. Those are
both kept throughout the calculation.

If U_R R V_R=D_R is the saved Smith factorization, its
literal quotient map is

    [z] -> ((U_R z)_5, [(U_R z)_4] modulo2),
    (n,[t]) -> [U_R^(-1)(n e5+t e4)].

The unit coordinates are removed by their saved V_R columns.
The same construction for D gives three unit factors and
seventeen zero columns. The last seventeen columns of V_D
are the primitive K basis; the last seventeen rows of
V_D^(-1) are its inverse on K. There is no coprime
shortcut in either construction.

Here are the full integral chain coordinates used for
the normal maps. Set p(x,y)=sum_(alpha<beta)x_alpha y_beta e_alpha,beta.
The central group has law

    (x,z)(y,w)=(x+y,z+w+p(x,y)),
    (x,z)^(-1)=(-x,-z+p(x,x)).

The difference
D_T(x,y)=p(Tx,Ty)-(wedge2 T)p(x,y) is symmetric. The
integer function

    f_T(x)=-sum_alpha D_T(e_alpha,e_alpha) binom(x_alpha,2)
           -sum_(alpha<beta)D_T(e_alpha,e_beta)x_alpha x_beta

satisfies f_T(x)+f_T(y)-f_T(x+y)=D_T(x,y) for all signed
integer vectors. Thus

    L_T(x,z)=(Tx,(wedge2 T)z-f_T(x)),
    L_T^(-1)(x,z)=(T^(-1)x,
          (wedge2 T)^(-1)(z+f_T(T^(-1)x)))

are inverse group maps. The new implementation obtains f_T
first from the actual ordered signed generator word in
this central group and then checks the displayed polynomial
separately. It uses signed integer powers and exact inverses.

For k=(u0,...,u4) in K list the ten vectors
v=(T0u0,-u0,...,T4u4,-u4) and partial sums s_j.
The integral bar cycle and its central value are

    Z(k)=sum_i([T_i u_i|theta_i]-[theta_i|u_i])
         -sum_j[s_(j-1)|v_j]+sum_i[u_i|-u_i],
    z(k)=sum_i f_Ti(u_i)-sum_j p(s_(j-1),v_j)
         +sum_i p(u_i,-u_i).

Its boundary is zero by telescoping. Subtract from Z(k)
the fibre class z(k) on each chosen K basis vector and
extend linearly. This supplies an integral section s of
the graph map with central coordinate zero. Evaluation
of the central cocycle gives rho:H2(V)->C, and the inverse
maps are

    H2(V) -> C+K, x -> (rho(x),graph(x)),
    (c,k) -> fibre(c)+s(k).

Their composites are identity because rho is identity
on fibre tori, rho(s)=0 and graph(s)=id. The saved
bar_section_z matrix is exactly the correction used in
this section. One must not subtract it again from a
fixed-sweep coordinate.

The actual fixed sweep of u at site i therefore has
coordinates(f_Ti(u),J_i u), where J_i is block inclusion.
Its graph part is converted by the saved K inverse.
For the ordinary last boundary put

    P_i=T_(i+1)...T4,
    J_o u=(-P0u,...,-P4u),
    c_o(u)=-sum_i f_Ti(P_i u) modulo im R.

The reversed ordered peripheral walk gives J_o; multiplying
D J_o=0 verifies it. Composition of the inverse lifted
actions L_Ti^(-1) gives the actual last-word central
coordinate. The saved difference and its R preimage
identify that actual coordinate with the displayed c_o.
Both are additive in C because the total return is I.
Their agreement on the four integer basis vectors therefore
gives agreement on every signed vector; the binomial identity
supplies the corresponding integral correction chains.
All R columns and their exact preimages remain in the full
presentation, so none of these changes erase two-torsion.

## 11. The ordinary clutch and the full 23 by59 matrix

For e=+1 or-1 the ordinary cap has primitive meridian
mu_o+e gamma. In the standard power notation its vector
is v=-e gamma and its multiplicity is one. The core is
the ordinary four-torus; the exact covering formula

    (x,tau) -> (x+tau v, exp(2pi i tau))

and its inverse, obtained by choosing the sheet and
subtracting tau v, give the marked normal solid torus.
This is also the m=1 case of the admitted LI Thom map.
The four fibre-normal columns and the root column are

    (c_o(u)-u wedge v, J_o u),   u=e1,e2,delta,gamma,
    (c_o(v),J_o v).

The positive meridian is mu_o-v=mu_o+e gamma, fixing
the signs. The root column respects the relation root=v
in the core H1 and is retained even though at m=1 the
four fibre classes already generate. No affine lift is
inserted at another site.

Represent C+K by the free lattice Z6+Z17 with the R
columns as relations. Add, for every singular cap, its
two physical fibre-kernel columns from Section9 and
all its fixed-sweep columns from Section10. There are
four rank-one caps, each with three fixed generators,
and one cusp with two. Add the five ordinary columns
just displayed. The complete matrix therefore has

    rows = 6+17=23,
    columns = 30+10+14+5=59.

Every column is labelled in the retained output as a
fibre relation, cap fibre kernel, actual fixed normal,
ordinary normal, or ordinary root. The ten cap fibre
kernel columns have the displayed Wang preimages and
are allowed to duplicate existing R relations; keeping
them makes the local-to-global map explicit.

For all sixteen cases the newly computed, fully retained
integer matrices satisfy

    U B_full V = diag(1,...,1,b),   with22 unit entries,
    U^(-1)U=I23,   V^(-1)V=I59.

All off-diagonal entries are zero. The exact quotient
map and inverse are

    [z] -> (Uz)_22 modulo b,
    [t] -> [t U^(-1)e22].

The order is exact, since
B_full V e22=b U^(-1)e22 and the Smith last coordinate
of every relation is divisible by b. The saved V columns
also give every bounding chain for the other22 unit
coordinates. Thus the matrix calculation is accompanied
by its complete integral generator and relation maps.

## 12. The geometric relative kernel and the fundamental group

It remains to prove that this cokernel is all of H2(X).
This uses the actual cap maps, not the Smith ranks alone.
Every boundary map onto H2 of a cap is surjective, by the
right sections in Section9 and the ordinary fibre section.
The degree-two Mayer--Vietoris sequence may therefore
eliminate the cap H2 groups. It gives

    0 -> coker B_full -> H2(X) -> K_rel -> 0,

where K_rel is the kernel of the direct-sum H1 boundary
map into H1(V) plus all cap H1 groups.

At each singular site Section9.3 proves that the boundary
H1 kernel toward its cap is exactly Z mu_i. In particular
there is no extra surviving short-period kernel in H1
of the boundary: it has already been divided by
(T_i-I)Lambda. At the ordinary site the kernel is the
single primitive class mu_o+e gamma. Hence K_rel is
the kernel of these six literal normal-disc classes
mapping to H1(V).

The Smith factors of D are three units and its gamma
row is zero. Consequently

    H1(V)=Z<gamma> + Z<mu0,...,mu4>.

Using the positive boundary orientation,
mu_o=-(mu0+...+mu4). Reversing that one normal-disc
generator if necessary expresses the six boundary
columns as

    A_e=[(e,1,1,1,1,1)^t | e1 | e2 | e3 | e4 | e5].

This reversal is a change of the relative generator,
not a deletion of a boundary sign; the program uses
this exact convention and records its inverse.
For y=(y0,...,y5), the inverse map is

    t0=y0/e,       ti=yi-y0/e, i=1,...,5.

Since e=+1 or-1 these are integers. Direct substitution
gives A_e t=y and recovers every t. Thus K_rel=0,
and H2(X)=coker B_full exactly, with no additional
free summand or torsion extension.

For the nonabelian assertion start with
pi1(V)=Lambda semidirect F(theta0,...,theta4), with
the literal conjugations T_i and the reversed ordinary
peripheral word. Each rank-one cap kills its primitive
l, and the cusp kills its two primitive short periods.
The new source prints these six physical vanishing
columns and an integral right inverse onto
Z<e1,e2,delta>. Their gamma coordinates are zero.
Therefore their normal closure kills precisely this
whole commuting rank-three fibre subgroup; the
remaining fibre group is Z<gamma>.

The extending origin disc at each singular cap kills
its mu_i, with the actual cap sections just specified.
All the remaining conjugations on gamma are trivial.
The ordinary meridian relation mu_o+e gamma then
becomes gamma^e=1. Its inverse group map is the map
from the cyclic presentation that sends its generator
to the actual gamma loop; all deleted fibre and base
generators bound the exhibited discs or their integer
products. The two composites agree on every original
generator. For e=+1,-1 this is the trivial group.

This proves pi1(X)=1 in the full marked gluing, rather
than deriving it merely from the abelianized matrix.

## 13. Euler number, all integral groups, and the sixteen cases

The exterior and all boundary mapping tori have Euler
number zero. The four rank-one central fibres have the
explicit nodal-curve times elliptic-curve model of
Section9.1, so their Euler numbers are zero. The ordinary
cap has a four-torus core and Euler number zero. At
the cusp, the actual period cell of the prescribed
unimodular fan contains two triangle orbits. They
give the two zero-dimensional strata; every open
toric surface and open double curve has a C* factor.
Thus its Euler number, and therefore chi(X), is two.

The gluing is closed and oriented by the complex
charts and the prescribed boundary clutch; all
displayed period bases have determinant one.
We proved b1=b2=0. Rational duality gives b4=b5=0,
and chi=2 now gives b3=0. Integral UCT and duality
give

    H0=H6=Z,
    H1=H4=H5=0,
    H2=H3=Z/b.

For completeness the H3 torsion map is explicit.
Take the H2 generator U^(-1)e22 with its bounding
relation column V e22. The character sending this
generator to1/b in Q/Z has integral Bockstein in
H3(X;Z); oriented cap product sends it to H3(X;Z)
homology. The inverse reads the torsion linking
coefficient modulo b against the recorded H2
generator. The two-term integer resolution with
differential b verifies both inverse composites.
The point and complex fundamental cycle give the
H0 and H6 generators and their usual degree maps.

Here is the complete finite table, with site numbers
as in Section8 and no unlisted parameter restriction.

|a|b|weight-one I1 site|ordinary e|pi1|H2|H3|
|--|--|--|--|--|--|--|
|2|4|1|-1|1|Z/4|Z/4|
|2|4|1|1|1|Z/4|Z/4|
|2|4|2|-1|1|Z/4|Z/4|
|2|4|2|1|1|Z/4|Z/4|
|2|4|3|-1|1|Z/4|Z/4|
|2|4|3|1|1|Z/4|Z/4|
|2|4|4|-1|1|Z/4|Z/4|
|2|4|4|1|1|Z/4|Z/4|
|4|2|1|-1|1|Z/2|Z/2|
|4|2|1|1|1|Z/2|Z/2|
|4|2|2|-1|1|Z/2|Z/2|
|4|2|2|1|1|Z/2|Z/2|
|4|2|3|-1|1|Z/2|Z/2|
|4|2|3|1|1|Z/2|Z/2|
|4|2|4|-1|1|Z/2|Z/2|
|4|2|4|1|1|Z/2|Z/2|

Every row has H0=H6=Z and H1=H4=H5=0. These are
the asserted marked filling and homology conclusions.
No smooth diffeomorphism classification is inferred
from the groups.

## 14. Exact new computation and reading record

The mathematical calculation is
code/S6_SERIES_PUBLISH_c7_ls_os45_bar_v001.py,
381 lines, SHA256
34b5fdd2dc759ca3292a806979fee138266f024c98d1df4b9c1baffbacc081c1.
It ran successfully once from07:57:37.244837 to
07:57:49.491090 UTC. Its only mathematical file input
is the raw defining fixture. The tracked Euclidean
Smith helper is reused from this lane's newly written
LJ helper; all OS45 geometry, vertical solutions,
full six-coordinate bar construction and word
evaluation were newly written.

Its actual stdout has88 long lines and290433 bytes,
SHA256 faa7f25973790a72a84677de93bc0cb9a0bd13c314387404467ac01adfdb078f.
Its separate stderr exists and has zero bytes. The
full16-case JSON has SHA256
33d83e7e9f255e029670f18d8718aa43060c5d247b86fdb38dbf45938cba9b70
and retains every local T,T^(-1),H,H^(-1),both fibre
maps and sections, saturated kernels and preimages,
fixed bases, graph basis/inverse, all central words,
full B,U,V,D,U^(-1),V^(-1), and all normal-disc inverses.

The full source was read. To read the long repeated
data without dropping any unique entry, two new
lossless readers were saved, run and wholly read:

* code/S6_SERIES_PUBLISH_c7_ls_output_readback_v001.py:
  117 lines, SHA256
  90addc9c40ff807398e267981e1cd2a4bbd16ecae9b11d6c8d84b2c7e31a57df.
  Its594-line267064-byte stdout has SHA256
  6430ee7422a982cdea4635f1f5d691fe1e45d57622afca1b209a141af88a0dde.
  Its explicit reference decoder reconstructs all88 original
  stdout lines byte-for-byte, including their order, scalars,
  blanks and metadata, and matches all16 full JSON records.
* code/S6_SERIES_PUBLISH_c7_ls_output_readback_v002.py:
  90 lines, SHA256
  b6604b0d8e5cebce47d0d4220e37ce716fb5c521de87a80b1ccda6cfd5f0b188.
  Its600-line154870-byte stdout has SHA256
  a31483058929a8f816d0a42e622bda93f4089390adced56d51ece858a3ecc07a.
  Its inverse copies the named earlier same-shape matrix or
  vector and replaces the explicitly stated entries. This
  reconstructs all594 v001 lines byte-for-byte. All369 unique
  matrices,130 vectors,6528 replacements and every other
  record, scalar, order and metadata line were read.

Both reader stderr files exist and are empty. Their
completion times are08:53:34.719114 and08:55:34.602866 UTC.
Neither reader reruns or changes the mathematical
calculation or its source/output/JSON. This is an exact
lossless mathematical-content reading; no manual
rereading of every repeated JSON byte is claimed.
An attempted oversized display of v002 lines206--305
was truncated and earned no credit. Those lines were
then actually read in the complete206--255 and256--305
chunks, followed by every remaining line through600.

Root separately wholly read both reader sources, all600
final stdout lines and both actual empty stderr files,
and retained the exact scope in
agents/continuation7_iii_root/S6_SERIES_PUBLISH_III_02LS_root_lossless_reading.md.
The main computation source and all unique output data
have therefore received that disclosed independent
root reading too. This record does not claim a second
independent mathematical computation.

The bounded literal IC8 source is
code/S6_SERIES_PUBLISH_c7_ls_star_order_v001.py,
SHA256 2a691d08f73dbe0049c6ee465398952c5e6fddd6b6fefccad261803805b9fdf3.
Its entire five-line stdout was read, SHA256
8debbe55995cd2973eb41f0c9281312616f5e21cb11d863412274c1c1d54a9a2;
its separate stderr is empty. It ran at09:00:38 UTC.
The complete input matrices, permutations and inverses
are retained in that output and the separate support note.

All preceding partial LS notes and actual execution
streams are preserved. This final assembly writes a
new proof file, not a replacement of those historical
states. No LS historical target program was read or
executed, and no canonical manuscript, required table,
global defect/event register, seal or manifest was
created or changed by this lane.
"""

text = header + vertical.rstrip() + "\n\n" + period_part.rstrip() + "\n\n" + new.lstrip()
assert "\r" not in text
out = LANE / "S6_SERIES_PUBLISH_III_02LS_fresh_derivation.md"
assert not out.exists(), "Preserve any prior complete proof instead of overwriting it."
out.write_text(text)
print("ASSEMBLED", datetime.now(timezone.utc).isoformat())
print("PATH", out.relative_to(ROOT))
print("LINES", len(text.splitlines()), "BYTES", len(text.encode()))
print("SHA256", sha256(out.read_bytes()).hexdigest())
print("SCOPE: new completed proof draft; final whole-proof rereading follows this assembly.")
