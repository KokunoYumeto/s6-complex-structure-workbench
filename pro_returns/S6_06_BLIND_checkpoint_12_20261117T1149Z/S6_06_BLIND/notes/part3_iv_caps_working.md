# Actual IV cap maps for the two I1* + IV source pairs

Status: working construction note, 2026-11-17 after checkpoint 07.
The statements below retain the source correspondence and line lift.
They do not assign a total-space sphere or a parameter-return class.
The joint integral topology is being checked in the I1* calculation.

## IV.1. The two root choices

Write the original reduced IV equation as
\[
 y^2=x^3+q^2 a(q)x+q^2 b(q),\qquad b(0)\ne0.
\]
The coefficient of x may vanish to higher order; the formulas still
retain that actual coefficient. The marked generator G has nonzero
component in Z/3. For the pair (a,b)=(6,2), where the first entry is
the line point and the second the translation, take m=3l+1 and put
q=z^m, x=z^{2l}X, y=z^{3l}Y. This gives
\[
 Y^2=X^3+z^{2l+2}a(z^m)X+z^2 b(z^m).
\]
Its resolved central fibre is IV. The deck is
\[
 D(X,Y,z)=(\zeta_m^{-2l}X,\zeta_m^{-3l}Y,\zeta_mz).
\]
In the blowup chart X=zX_1,Y=zY_1, the two nonidentity
component labels are Y_1=+sqrt(b(0)) and Y_1=-sqrt(b(0)).
The character on Y_1 is zeta_m^{-(3l+1)}=1. Thus D fixes
each component label. The section Q'=2G' has component 2 and
the line N=O(6G'-O) has degree zero on every component.

Multiplication by m is an analytic local isomorphism on the smooth
Neron group: its derivative on the additive identity component is
m, and it is invertible on Z/3. There is a unique local section R
with mR=Q' and the selected central point. The deck preserves it.
For every integer n, the actual source map
\[
                    a_0=t_{-nR}D
\]
therefore satisfies a_0^m=t_{-nQ'}. Its component action together
with t_{-Q'} is transitive. The root line is compared with the
original line by pullback to the resolved fibre product followed by
the actual contractions: its degree on every contracted curve is
zero. The two section divisors then differ only by a whole fibre.
This is the same explicit degree-zero descent used for the reduced
III cap, with the reduced IV intersection matrix in place of III.

For (a,b)=(2,6), take m=3l, l>=1, q=z^m, x=z^{2l}X,
y=z^{3l}Y. The central fibre of
\[
 Y^2=X^3+z^{2l}a(z^m)X+b(z^m)
\]
is the smooth curve E_0: Y^2=X^3+b(0). Its deck is
\[
 D(X,Y,z)=(\zeta_m^{-2l}X,\zeta_m^{-3l}Y,\zeta_mz).
\]
On E_0 this is (X,Y)->(zeta_3 X,Y). Its three fixed points
are P_0=O, P_1, P_2, with P_1 and P_2 the two nonzero
three-torsion points. The marked section 2G' limits to P_2 after
choosing the label P_1=G'_0. The section Q'=6G' limits to O.
The unique local m-division R of Q' with R_0=O is deck-invariant.
The same source map a_0=t_{-nR}D has a_0^m=t_{-nQ'}.

## IV.2. The actual good-root line correspondence

It is enough first to give the minimal cubic root q=s^3. Let
S_root be its smooth elliptic surface, with deck
\[
                   (X,Y,s)\longmapsto(\zeta X,Y,\zeta s).
\]
At all three fixed points P_i, the tangent weights are (1,1).
Blow up those points, with beta: S_hat -> S_root and exceptional
curves E_i. The deck fixes each E_i pointwise and acts on its
normal coordinate by zeta. Thus the quotient pi: S_hat -> S_tilde
is smooth in the explicit blowup coordinates: if (w,s) has weights
(1,1), use (eta=w/s,s), and the quotient coordinates are
(eta,s^3). The image L_i of E_i has square -3, since
pi^*L_i=3E_i and the degree of pi is three.

The proper transform of E_0 in S_hat has square -3. Its image C
in S_tilde has square -1, because pi^*C is that proper transform.
It meets the three L_i at distinct points. Contract C by the actual
smooth point contraction alpha: S_tilde -> S. Each image L_i then
has square -2, and the three meet at one point with distinct tangent
directions. This is the minimal regular IV fibre. The invariant
functions q=s^3, x=s^2X, y=s^3Y give the displayed original
Weierstrass equation away from the exceptional curves; the resolved
map and this contraction identify S with its minimal regular model.
Both surfaces have no vertical (-1)-curve, so the graph comparison
of the minimal models gives an isomorphism over the disc.

The section curves avoid C. Indeed a source section is transverse
to the base, and its proper transform meets E_i away from the
intersection with the proper central elliptic curve. Let
M=O(2G-O) on S and N=O(2G'-O) on S_root. Pullback of the actual
two section divisors gives the exact identity
\[
       \boxed{\ \beta^*N=\pi^*\alpha^*M+E_2-E_0\ }.       \tag{IV.1}
\]
The notation is additive in the Picard group. This equation keeps
the two exceptional corrections; it does not replace the original
line by its degree-zero restriction without a map.

The natural deck lift on N has weights zeta^{-1},1,zeta on
the fibres at P_0,P_1,P_2, respectively, up to one common
character. To check the signs, for O(P_2) a local equation w of
the point transforms by zeta and the canonical section is w times
the local line frame; equivariance makes the line-frame weight
zeta. For O(-P_0) the inverse local equation gives zeta^{-1}.
These are also exactly the weights of O(E_2-E_0) in (IV.1),
while the pullback quotient line has trivial isotropy weights.

The original translation Q=6G has root limit O, so its lifted map
fixes each P_i and each exceptional E_i. The exceptional correction
E_2-E_0 is invariant. The actual B_0 line map therefore pulls to
S_hat, acts on that correction by its canonical divisor lift, and
descends through beta to N. This is an extending map on N, agrees
with the original one off the central fibre, and commutes exactly
with the descended deck. Thus IV.1 also compares the actual
suspension lift, not only its line-bundle class.

For m=3l, first take q=s^3 and then s=z^l. Pull the entire
correspondence (IV.1) through this latter base change and resolve
the fibre product. Pullback preserves the displayed line identity.
This supplies the actual line comparison for the general good root;
the extra exceptional divisors are retained as the pullbacks of
E_2-E_0. On the central elliptic curve the characters remain those
just calculated.

## IV.3. The norm lift and the Euler torsion

First lift t_{-R}, before taking its n-th power. Its Hom line has
an actual meromorphic chord section. After
resolving coincidences, its vertical correction is an integral whole
fibre: on the reduced root the component intersection matrix has
kernel generated by the full fibre, and on the smooth root there is
only one component. Multiplication by the corresponding base power
gives an invertible holomorphic line lift F. Use the descended deck
lift from IV.1 on the smooth root, or the degree-zero descended lift
on the reduced root.

The finite weighted average in the deck-conjugation action produces
an invertible eigen-lift, still denoted F, with
\[
 DFD^{-1}=\chi F,\qquad\chi^m=1.
\]
Since mR=Q', the maps F^m and B_0 cover the same actual source
translation. Their ratio is a nonvanishing holomorphic base unit:
B_0=beta(z)F^m. The equality DB_0D^{-1}=B_0, already retained in
the descended line comparison, now gives beta(zeta_m z)=beta(z),
because chi^m=1. Thus beta is a function of q. In particular F
commutes with B_0, and so does D. The actual preliminary lift
A_pre=F^nD therefore commutes with B_0 and satisfies
\[
 A_{\rm pre}^m/B_0^n
       =\chi^{nm(m-1)/2}\beta(q)^{-n}.
\]
This is a deck-invariant nonvanishing base unit, including its full
character factor when m is even. Dividing A_pre by an analytic
m-th root of that unit produces A_0 with
\[
                 A_0^m=B_0^n,\qquad[A_0,B_0]=1.        \tag{IV.2}
\]
Here B_0 is the actual nonzero-linearization line map covering
t_{-Q'}, in the suspension convention used above. With
lambda=r^m and A_r=r^n A_0, the full equality is
A_r^m=B_lambda^n. The finite-cap group and its prescribed gamma
meridian are the ones obtained from this equality, not from a
separately selected source-root cover. The family parameter in this
presentation is r.

When gcd(m,n)=1 choose integers u,v with nu+mv=1. The actual
commuting line map H=A_r^u B_lambda^v has the form rH_0,
where H_0 and its inverse have bounded norm ratios on a smaller
compact source tube. It satisfies H^m=B_lambda and H^n=A_r.
For small |r| it is strictly contracting, and the cap is exactly
N^times/<H>. This proves smoothness and properness by its compact
norm shell. It proves freeness of delta too: a unit line rotation
equal to H^j forces j=0 by the strict norm inequality, then the
rotation is the identity. In the positive outward norm convention
h=H^{-1}, the marked incoming meridians are
q->-nh and gamma->mh. The actual killed meridian is m q+n gamma.

For the good root, the cap orbit retracts onto the mapping torus
of the order-three automorphism of E_0. The line N has central
Picard class P_2, a nonzero fixed point of that automorphism.
This gives a generator of the order-three summand in H^2 of that
mapping torus. Explicitly, write the Picard torus as V/Lambda.
Since D-1 is invertible on V, the connecting map is an isomorphism
\[
 (V/\Lambda)^D \longrightarrow \Lambda/(D-1)\Lambda,
 \qquad [v]\longmapsto[(D-1)v].
\]
The target has order det(D-1)=3. The mapping-torus clutch of the
degree-zero line realizes exactly this connecting class. It is
nonzero because P_2 is nonzero. A common deck character only tensors
by a flat line coming from the free parameter circle, so it has zero
absolute first Chern class; the character itself remains in the
actual lift for later parameter-return comparisons.

The reduced root has three rational components, and both the source
component permutation and the line map extend over their triple
point. In the good-root case the exact exceptional correction in
IV.1 supplies the line comparison needed for the joint I1*/IV
boundary maps. No return class is inferred here solely from this
Euler-torsion calculation.
