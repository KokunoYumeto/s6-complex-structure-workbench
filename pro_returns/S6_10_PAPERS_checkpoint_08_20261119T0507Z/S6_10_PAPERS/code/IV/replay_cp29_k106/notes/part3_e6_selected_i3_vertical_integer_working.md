# Selected I3: the complete signed vertical integer pair

Working proof, 18 November 2026. We retain the original source
`y²=x³+r x²+t x+t²`, section G=(0,t), M6=O(6G−O), translation −G,
s=1/4−r, cap m=2,n=1, every finite line character and the full
annular reference of SI3, ASI3, MC3 and IC2. The scalar root is the
fixed original r_base. The parameter orientation is one positive
s-circle. The fan is T_j=T(e1+j e2,e2), for every integer j, in the
original unit-+1 Tate marking. We evaluate the actual completed
fixed-C0 quotient, with the K68 physical line and Jin parameter
reversal. IC2 supplies its initial pair (k_0,ell_0)=(47,−4).

The conclusion, before any reduction modulo28, is

    k_j=47−2j³+18j²−52j,    ell_j=−4,
    mu_j=−1,               nu_j=48−2j³+18j²−52j.

Here mu=ell/4 and nu=k−ell/4 are the actual fixed-C0 free coordinates.
We give the nonperiodic source comparison explicitly. The complete
VZ.1–7 source-zero argument supplies the local constructions used
below; BW.2 supplies its relative calibration. All their maps are
specialized to the displayed I3 units and retained boundary marking.

## IVP.1. The full source map and both deck squares

On the protected selected q-disc let

    Q(q,s)=q kappa(q,s), kappa=P²/c_q,
    alpha=P⁶, g=P^−1, eta=lambda_base K P^−3.

The full functions P,c_q,K are those of IF3.1–2. They are nonzero
on this disc over the compact s-annulus. Their parameter windings
are (2,6,−1,−3) in the order(kappa,alpha,g,eta). For each fixed j
shrink the q-disc uniformly over that annulus. The equation

    Q(q',s)=Q(q,s)g(q,s)^j

then has a unique holomorphic solution q'=a_j(q,s)q, with
`a_j(0,s)=g(0,s)^j`, and a holomorphic inverse on the chosen image
collar. This follows by applying the holomorphic inverse function
theorem to Q at q=0, whose derivative is the nonzero kappa(0,s).
Compactness gives one radius for that fixed j. Uniqueness makes
this map single-valued on the s-circle. We use its actual image
boundary; no replacement radial cut is inserted.

Set c(q,s)=g(q',s)/g(q,s). It is one at q=0. Its unique holomorphic
logarithm zero there is single-valued in s. The marked source
coordinate map on the suspension cover is

    (q,Z,gamma_j) -> (q',c(q,s)^gamma_j Z,gamma_j).

The source h_j period on the first side is Qg^j, exactly Q(q',s).
For the B square, the identity

    c^(gamma_j+1)g(q,s)=g(q',s)c^gamma_j

holds as a full holomorphic coefficient identity. Thus this is a
smooth source map between the actual suspended quotients, with
holomorphic maps on each source fibre. Its inverse uses the stated
inverse q-map and reciprocal c factor. Near the node its two branch
multipliers are reciprocal units. They extend over xy=Q, preserving
the two branches and the node. The factor c−1 vanishes with q.

The actual character and period maps are

    Z_j=Z, V_j=Z^−j V, h_j=hB^j, B_j=B,
    kappa_j=kappa g^j,
    alpha_j=alpha eta^j kappa^−j g^−j²,
    eta_j=eta g^−j.

Their inverses are V=Z_j^j V_j and h=h_j B_j^−j. Substitution
cancels the q^j from hB^j against that from Z^−j, as in VI3.1.
The map carries the full source, point-theta line and both source
and target r6 factors. The scalar root and every outside cap chart
are the fixed ones of IF3.1.

## IVP.2. The actual fixed graph and its normal arrow

Use the real coefficient gamma_j of B. The F9 increasing outward
moment direction is −gamma_j. If L_Q,L_alpha,L_g,L_eta are the
logarithms of the positive norms of Q_j,alpha_j,g,q eta_j, then
on the regular torus

    gamma_j=(L_Q log|V_j|−L_alpha log|Z_j|)
                   /(L_Q L_eta−L_alpha L_g).

The denominator has leading term(log|q|)²; the bounded full units
give a common nonzero denominator on the chosen small disc.
The literal h_j adds(L_Q,L_alpha) and has gamma_j lift0. The
literal B adds(L_g,L_eta) and has lift1. These statements retain
the full units. In particular the h_j^−1 identifying the second
fixed-C0 chart has lift0.

In the two F9 conifold charts the exact moment equations are

    2b=r−|y|²/r,  2b'=|x|²r−1/r,
    db'/db=(|x|²+r^−2)/(1+|y|²r^−2)>0.

The exceptional interval has representatives
`z=sqrt(r), v=u=0, w=1/sqrt(r)`. Its contracting-period height
`gamma_j=1/2−epsilon(r−1)/(r+1)`, with0<epsilon<1/4, has endpoint
lifts1/2+epsilon and1/2−epsilon and derivatives−4epsilon in both
endpoint moment coordinates. The two source-branch endpoints are
therefore distinct in the same short real arc. Extend this height
properly on both half-lines, repeat by gamma_j->gamma_j+1 under B,
and interpolate with the displayed exterior coefficient by the
relative positive-vector-field construction. The full positive
unit norms remain in the coordinate map.

The source map of IVP.1 preserves the normalization and its two
marked points. Transport its fixed graph and interpolate its height
with the reference height in this same arc. Their endpoint order
stays strict. Away from the pair of node preimages the normalization
is injective, so this interpolation remains an embedded sphere.
Extend its velocity to a tube and then by a cutoff to the quotient.
The construction is periodic in s because q',c and the positive
norms are periodic. It supplies the actual graph isotopy relative
to the exterior. It requires no logarithm of g around that circle.

In the fixed-star coordinates q=ZAB, the source-normal arrow is

    (Z,A,B) -> (Z,a_j(q,s)A,B).

It intertwines the second native chart A_1=ZA,B_1=ZB exactly.
Its inverse first recovers q by the inverse q-map. The c^gamma_j
source correction is1+O(q), so its base derivative has no extra
normal linear term. The character shear has the typed Cartier
map from the new spinor line to the old one, multiplication by Z^j.
With x/y=Z, its local generators
`x^(−j−1)y^j, x^−j y^(j+1)` go to`1/x,y`; their determinant
frames match. Consequently its Hom line and adjoint normal bundle
are carried by that exact map. The residual normal factor is
precisely g(0,s)^j, whose winding is−j. The graph-normal derivative
is the positive triangular derivative of the constructed isotopy.
Its base sphere map extends over D³ by the same boundary velocity
and a collar cutoff. We retain the adjoint normal arrow on the Hopf
sphere and the whole physical principal-circle lift.

## IVP.3. The theta-cut line morphism with its outer gauge

Write(u,v,d,gamma) for the real coefficients of the source vanishing
period, h, physical delta and B. The character map gives exactly

    u_j=u, v_j=v, gamma_j=gamma−jv, d_j=d−ju.

A positive q turn has old deck(u,d)->(u−v,d−gamma).
A positive s turn has old deck

    u->u−2v+gamma, d->d−6v+3gamma.

Conjugating by the displayed character map gives the full new decks

    q: u->u−v, d_j->d_j−gamma_j,
    s: u->u+(j−2)v+gamma_j,
       d_j->d_j−(j−2)(j−3)v−(j−3)gamma_j.

This verifies the theta seam even though g winds−1. Let alpha_q
and theta have period1. The integral parts of the actual coefficient
connections for U=M* are

    A_0=dd+(alpha_q−3theta)d gamma+6theta dv,
    A_j=dd_j+(alpha_q+(j−3)theta)d gamma_j
                         +(j−2)(j−3)theta dv.

The full zero-winding unit terms are the derivatives of the actual
period logarithms after their displayed angular factors are removed.
They are retained in these coefficient frames. The difference in
original coefficients is

    A_j−A_0=−j[du+(alpha_q+2theta)dv−theta d gamma]
                         + the full unit correction.

The target q' angle is alpha_q−j theta plus its full unit term.
The pulled-back reference connection in the new coefficients is

    A_(0,q')=dd_j+(alpha_q−(j+3)theta)d gamma_j+6theta dv.

Subtracting gives the exact residual integral expression

    (j²−5j)theta dv+2j theta d gamma_j.

Make the graph maps b,gamma, whose outer values are v,gamma_j,
constant on a tube U2 around the fixed sphere, using their real
lifts there. Choose nested tubes U0 inside U1 inside U2, with all
surgeries and connection changes inside U1. They extend constantly
over the same cap. The theta-cut coefficient arrows
`w->exp(2pi i b)w` and`w->exp(2pi i gamma)w` define actual lines
T_b,T_gamma with curvatures Xi=dtheta∧db and Psi=dtheta∧dgamma.
Their squares and their product vanish. The displayed coefficient
arrows, meridian-one value and regular b×gamma value give

    U_j ~= U_(0,q') tensor T_b^(j²−5j) tensor T_gamma^(2j).

This is a relative line morphism with the prescribed outer arrow.
Here are its boundary normalization and extension. The q-monodromy
kills u primitively; theta,b,gamma extend over the piece. The sole
remaining boundary degree is the q angle. At one theta choose an
actual free section disc |Z_*|=1,v=gamma_j=0, away from the marked
sections and fixed graph. The prescribed Z_*^−j coefficient arrow,
both tensor frames and the q' source map extend over this disc, so
that degree is0. For the residual line choose vector frames with
transitions exp(2pi i r_il). Remove their zero integral two-cocycle
and use a partition of unity to write r_il=a_l−a_i. The frames
exp(−2pi i a_i)e_i trivialize the ratio. Remove the extending
theta,b,gamma characters and extend its remaining real boundary
logarithm by a collar cutoff. This gives exactly the stated outer
arrow, including its unit factors. Its inner cap arrow is the one
computed in IVP.6.

## IVP.4. The tangent collar retains the nonperiodic source phase

Let tau=log Q/(2pi i), G=log g/(2pi i), deltaG=log c/(2pi i).
The first two are cut logarithms; the last is the unique periodic
one zero at q=0. In the covariant real source coframe

    omega=du+Re(tau)dv+Re(G)d gamma

(the base derivatives of tau,G are retained in the complementary
base block), the full comparison is

    omega'=omega+Re(deltaG)(d gamma−j dv),
    dv'=dv, d gamma'=d gamma−j dv.

Its base map is r'=r+log|a_j|,
alpha_q'=alpha_q+arg(a_j)/(2pi),theta'=theta. Its derivatives are
single-valued and retain winding−j. The source block, in order
(omega,v,gamma), is

    [[1,−j Re(deltaG),Re(deltaG)], [0,1,0], [0,−j,1]].

In order(omega,gamma,v) it is upper triangular with diagonal1.
The full matrix is block triangular; all base-to-source derivatives
lie in its off-diagonal block. Use the connection along the actual
collar with strictly upper triangular source connection matrix.
Its curvature is strictly upper triangular and has trace of its
square0. The base interpolation depends on the two boundary angles
and one collar coordinate, so its curvature square also vanishes.
The trace for the full block triangular matrix is the sum of these
two diagonal-block traces. Thus the whole tangent comparison has
zero Pontryagin transgression. This argument retains the g phase
in the invariant coframe and uses a periodic logarithm only for c.
The line phases remain in IVP.3.

## IVP.5. Four relative pairings on this actual piece

Use the carried dual-line curvature F and orientation
`Omega_+=dr∧d alpha_q∧du∧dv∧d gamma∧dtheta`. The relative boundary
connections are those just specified. Their pairings are

    integral F² Xi=1, integral F² Psi=0,
    integral p1 Xi=0, integral p1 Psi=2.

For the first, freeze theta. Each full unit has a holomorphic
logarithm on the q-disc. The BW.2 explicit logarithmic path between
these units, its node horizontal field, prescribed real-period
boundary field, F9 height flow, Cartier/Hopf normal map and invariant
line lift give the relative calibration with the same closing
exponent and boundary coefficient frame. The actual SCN.9/K62
common-link comparison has both outer normal arrows and its common
inner physical gauge extending. Its separate characteristic terms
vanish, and its complete collar is3 integral F² Xi−3. Hence this
integral is1. The carried connection makes the slice value constant
in theta. This construction takes logarithms on each frozen source
disc; it retains the theta decks of IVP.3.

For the second, choose the gamma level outside the fixed graph's
short arc. Its neighbourhood is the actual selected I1 source E,
disjoint from the surgery and cap. Retain the full coefficient
phase on this source level,

    phi_alpha(q',s)=6theta+(2pi)^−1 Im Log[alpha(q',s)exp(−12pi i theta)].

Its logarithm is the actual winding-zero coefficient logarithm.
At frozen theta the boundary connection is dd+phi_alpha dv.
The q-deck's d change is−gamma, hence its q holonomy on gamma=0
is0. The line has degree0 on E's normalization sphere. E retracts
to that sphere with its node graph. The graph b extends over the
vanishing handle by its constant attaching-circle lift. Extend
the connection as `dd+phi_alpha db` on this actual source level;
its curvature is the decomposable form dphi_alpha∧db, whose square
vanishes. This retains the entire q'-dependent unit and its actual
graph holonomy. The free disc Z_*=-1,gamma=0 carries the full
Cartier arrow and q' map, proving that the comparison boundary
has zero q degree. The Cech and real boundary logarithm construction
of IVP.3 gives the relative line isomorphism with exactly that
boundary connection. All terms with dtheta vanish when wedged
with Psi, giving the asserted0.

For p1 Xi take a regular graph level outside U2. It is relatively
cobordant to the original three-dimensional source level times
gamma, with its source-pulled tangent connection. The four-form
integrates to0 there. IVP.4 gives zero tangent transgression on the
comparison collar. The nested tubes ensure that this cobordism
stays away from the surgery.

For p1 Psi retain the node xy=q and Omega=dx∧dy. Put
`V=(x,−y), H=(bar y,bar x)/R²`, R²=|x|²+|y|².
Then dq(H)=Omega(V,H)=1. The actual Tate horizontals are

    H_x=H−bar y/(xR²)V=(0,1/x),
    H_y=H+bar x/(yR²)V=(1/y,0).

Scaling those coefficients gives determinant-one shear homotopies.
The normalized frame(V/R,RH) is
`R^−1 [[x,bar y],[−y,bar x]]`, of degree1 on the node sphere.
Thus its relative c2 is1. The q-polar frame(V,qH) has determinantq;
its relative c1 is the fibre, whose square is0 by two disjoint
parallel fibres. Its relative p1 is−2. The marked real period frame
differs by the stated shears, a positive lattice matrix and a polar
rotation factoring through the angle circle. Their third
transgressions vanish by those explicit homotopies and factorization.
Finally Psi=dtheta∧dgamma reverses the last two factors of Omega_+,
so the required pairing is+2.

## IVP.6. The complete Hopf cap and exterior Euler collar

On the fixed tube use

    u=(1+j_quat Z)/sqrt(1+|Z|²), h=u i u^−1,
    Q_N=A+j_quat bar B, q_H=u Q_N.

Carry the full initial factor g(0,s_*)^j into both reference
normal products, and remove the positive modulus by the same
positive Cox path. In these carried frames the remaining phase
is that of g(0,s)^j/g(0,s_*)^j. On a cut interval write it as
exp(i alpha), with alpha(0)=0 and increment−2pi j. The original
constant phase alpha0 is retained by its explicit cap extension
`v->exp(v alpha0/2)exp(−i alpha0/2)` for v in the pure-imaginary
three-ball D³_h; its boundary is the corresponding constant-phase
clutch. Thus the based phase comparison carries both original
endpoint frames. Let H=exp(i alpha/2). The actual normal map is

    Q_N'=H Q_N H,
    q_H'=exp(h alpha/2)q_H exp(i alpha/2).

Both half-phase endpoints are(−1)^j, so the physical map closes.
The constant-in-h map C(q_H)=H q_H H extends over the D³_h cap.
Compose the actual map on the right with C^−1. The remaining
coordinate clutch is left multiplication by

    A_j(h,theta)=exp(h alpha/2)exp(−i alpha/2).

Its zero-winding part contracts through the specified real
logarithm with both endpoints retained. The resulting map is
`exp(−pi j theta h)exp(pi j theta i)`. For N=−j its preimages of−1
occur at h=−i,theta=(2r+1)/(2N), with the directed choices in the
unit interval. In outward basis(j_quat,−k_quat,partial_theta), its
differential has target components(k_quat,j_quat,2pi N i).
The positive target basis at−1 is(i,j_quat,−k_quat). The local
determinant is2pi N, so the total degree is N=−j; j=0 is the
constant identity map.

The complex fixed sphere is−S²_h. The quotient's fixed-tube
orientation is−S²_h∧dr∧S²_eta, so the inserted cap is−D³_h×S²_eta.
With coordinate clutch v_ref=A_j v_j its difference base is
`−(D³_j union −D³_ref)×S¹_theta`. The radial connection
f(r)A_j^−1 dA_j, or equivalently−f(r)dA_j A_j^−1 in the other
frame, gives c1(E)=0,c2(E)=j and p1(ad E)=−4j. This uses
`integral tr(A^−1dA)^3=−24pi² deg A` in the positive-spinor
representation and the stated boundary direction. The physical
tautological line has fibre value−1. Its projective relation gives
positive-parameter pair(j,4j); K68's actual parameter reversal
therefore gives cap contribution

    (Delta k,Delta ell)_cap=(−j,−4j).

The full constant C map, unit homotopies, base sphere flow and
positive normal factors extend as specified, so this is the cap
of the actual line comparison.

In the original exterior, expressed in the piece coordinates
`gamma=gamma_j`, the full integral connection and primitive are

    A_ext=dd_j+(alpha_q−3theta)d gamma+j du
                          +[j alpha_q+(6−3j)theta]dv,
    beta=−j[du+(alpha_q+(2−j)theta)dv−theta d gamma].

All zero-winding corrections are the derivatives of the retained
coefficient maps and deform with their prescribed endpoint
primitive. For
`Omega_B=d alpha_q∧du∧dv∧d gamma∧dtheta`, direct exterior algebra
on these actual forms gives

    3 integral_0^1 beta(F_ext+s d beta)^2 ds
                         =(36j−15j²+2j³)Omega_B.

The actual outward interpolation runs from piece1 to exterior0.
Its Euler contribution is consequently−36j+15j²−2j³. IVP.4 gives
its zero Pontryagin contribution. This uses the original boundary
primitive, including its j du term and its theta seam.

## IVP.7. Integer assembly and the signed native checks

Because Xi²=Xi Psi=Psi²=0, IVP.3 and IVP.5 give the interior changes

    Delta k_int=3j²−15j, Delta ell_int=4j.

Adding the actual cap and exterior collar yields

    Delta ell=4j−4j=0,
    Delta k=(3j²−15j)−j+(−36j+15j²−2j³)
           =−2j³+18j²−52j.

The physical/dual-line comparison and Jin reversal are exactly K68,
with the same fixed scalar, finite character, source cap and original
outer reference. Adding IC2's evaluated pair(47,−4) proves the
integers stated at the beginning. In particular

    nu_j/6=8−2 binom(j,3)+4 binom(j,2)−6j
          =8−j(j²−9j+26)/3

is an integer for every signed j. Its forward and backward
increments are respectively−(j−2)(j−3) and(j−3)(j−4), which are
exactly the two native VI3 products. This is an independent check
using their actual relative-product maps. Reduction modulo28 gives
the already proved VI3 class; the present integer values have been
evaluated before that reduction.

For the actual ordinary double, VI3 has t=−1. Its fixed-C0 native
map gives

    V00=−2(mu_j+nu_j)−2, delta0=V00+4nu_j.

The remaining entries and both full Cox reset maps are those of
VI3.3–5, with no change to their source or cap marking. These exact
integer seeds are the ones used for subsequent fan paths.

The fresh executable certificate is
`code/part3_root/e6_selected_i3_vertical_integer.py`; it independently
checks the two deck conjugations, full multiplier identities,
coefficient connections, the exterior five-form, tangent unipotence,
normal chart square, cap degree sign and every signed integer
assembly identity used here. Its finite signed evaluations supplement
the symbolic identities. The proof's geometric extensions are the
explicit source/node/graph/line/tangent/cap constructions above.
