# 01GN / E16: derivation before the target proof is opened

Checker: restore_build. The E16 proof, including its equation E.16.3, and
the complete E_checks.py file remain closed during this derivation.
The supplied E16 statement and cited-input statements have been read.
The GK proof was independently derived, released and compared earlier;
its actual bundle identifications are used here as an established input.
The supplied GL packet contains three construction equations isolated by
root, together with primary construction definitions. No GL target proof
or old E14 computation has been opened by this checker. The E8 statement
is used as a stated input. The general rank assertion E7 is not used to
prove any of the ranks below. The comb calculation uses the primary
construction and its tautological sequence, rather than the asserted E15
tangent-cohomology result.

All period-coordinate identifications used below are explicit maps. In
particular the coarse extension at a finite quotient is transported to
the root cover by its displayed character matrix; the two extensions are
not identified merely from their ranks or degrees.

## 1. The morphism being calculated

For a smooth family of two-dimensional complex tori, let H be its flat
rank-four cohomology bundle and F the holomorphic rank-two subbundle of
holomorphic one-forms. Put E=H/F and V=F*. Projection of the flat
connection gives the actual second fundamental form

    kappa: F -> E tensor Omega_B,

or, equivalently, a section of V tensor E tensor Omega_B. This is the
Kodaira--Spencer tensor. On a logarithmic extension replace Omega_B by
Omega_B(log D); the operator acting on a local section is the logarithmic
base vector. On the finite smooth torus cover use its ordinary base
vector. Pullback through t=s^n changes these vectors by

    d/ds = n s^(n-1) d/dt,       t d/dt = (s/n) d/ds.

These identities will be used together with the changes of fibre frames.

There is an elementary expression valid for every marked period section,
without a symmetry assumption. In a local decomposition H=C^2+C^2 write
F as the columns of (I; Z), and write the connection matrix in four
blocks A_ij. The quotient map is (u,v) -> v-Zu. Applying this map to
the derivative of (I;Z) gives

    K = Z' + A21 + A22 Z - Z A11 - Z A12 Z.                 (GN-fresh-1)

For a logarithmic vector the prime and the A_ij denote contraction with
that vector. This derives all four entries directly from the specified
section. Its determinant vanishes precisely where its rank is below two;
at a zero of that determinant its rank is zero precisely when all four
entries vanish. Multiplication on either side by an invertible frame
matrix preserves this conclusion. The fresh program checks the graph
projection identity as a polynomial identity in all entries of Z, Z'
and A, without invoking a target formula.

## 2. Original affine twists and higher multiplicities

The cited E8 statement supplies the original marked period calculation:
the ordinary tensor on the smooth root cover has rank one at the
order-three point, determinant order two there, and rank two at every
other finite point, including the order-four point. Its logarithmic
hexagonal tensor has rank two. The general theta identity in that input
and its actual AC branch are not re-proved or counted as a new E8 check.

For an affine attachment translation a, the local map on the universal
cover is z -> z+a. Its differential is the identity. Its induced map on
singular cohomology is also the identity, by the explicit homotopy
z -> z+r a for 0<=r<=1 on the real torus. The induced maps on invariant
one-forms and on the quotient H/F are therefore the identity. Thus the
same actual local period plane and second fundamental form are carried
through the affine attachment. This applies to the fixed admissible
affine twists, including their |p|>1 members. At the hexagonal filling,
translation changes the affine attachment but not the two logarithmic
period vectors or their full-rank residue. This is a map of the local
cohomology/period data; no isomorphism of the global total spaces is
asserted.

For the (3k,4l) construction the map of root bases from the higher to the
original root curve is

    [X:Y] -> [X^l:Y^k],

with weights (3k,4l) and (3,4), respectively. The pullback of O(1) is
O(kl). This is the same map derived and explicitly bound in the GI
prereading record. Locally at the first multiple value it is u=s^k and
at the second it is u=s^l, up to a nonzero coordinate unit. On the full
smooth torus covers the pullback maps on invariant forms and H^1(O) are
the ones described above; the extra affine translations act by the
identity. Hence the tensors are, in the transported frames,

    k s^(k-1) K_original(s^k),
    l s^(l-1) K_original(s^l).

The first central matrix has rank one for k=1 and is zero for k>1. The
second has rank two for l=1 and is zero for l>1. Away from these branch
points the base derivative is a unit, so the original ranks are retained.
At the logarithmic cusp the map is unramified and the rank remains two.
This proves both displayed cases of E.16.1 and the asserted remaining
locus, with the ordinary/full-root and logarithmic vector conventions
accounted for explicitly.

## 3. Two-parameter family: the complete divisor from the actual bundles

The GK derivation gives, by its connection transitions and the explicit
flat alternating-form map, both V and E isomorphic to O+O(-1) on the
root curve B=P(1,4). These are actual bundle maps, recorded in that
derivation and its comparison, rather than an inference from the tangent
cohomology dimensions. Write x,y for weights 1,4; x=0 is the order-four
point. The canonical bundle is O(-5). There are three ordinary critical
values, so Omega_B(log D)=O(7). Consequently the four entries of K are
sections of O(7), O(6), O(6), O(5), respectively. They have the forms

    [ x^3(a x^4+b y)    x^2(c x^4+d y) ]
    [ x^2(e x^4+f y)    x  (g x^4+h y) ].              (GN-fresh-2)

All four entries vanish at x=0. Direct multiplication gives

 det K = x^4 [(ag-ce)x^8+(ah+bg-cf-de)x^4 y+(bh-df)y^2].

The primary two-parameter source, equation `periods` in its subsection
on the three nodal values, gives the two multiplicative identifications

    (z,v) -> (q alpha z, beta v),
    (z,v) -> (gamma z, lambda q^epsilon delta v),

where the four functions are units, epsilon=0 at p1,p2, and epsilon=1
at p3. Taking logarithms gives an actual period matrix with logarithmic
part (log q)/(2 pi i) diag(1,epsilon). Thus its logarithmic second
fundamental form at the central point has rank one at p1,p2 and rank
two at p3. The quotient/normalization calculation in the primary source
identifies these period quotient frames with the coherent central
cohomology frames; no monodromy rank is substituted without this period
calculation.

The bracket in (GN-fresh-2) is a homogeneous quadratic in x^4,y. It
vanishes at the two distinct nodal values p1,p2. It is nonzero at p3,
where the logarithmic matrix has rank two. Therefore that quadratic is
a nonzero scalar times the product of the two distinct linear factors
of p1,p2. Neither factor vanishes at x=0. The determinant has a simple
coarse zero at each nodal value and order exactly four in x at the
order-four point. There are no additional zeros. The matrix is zero
at the order-four point, has rank one at the two nodal values, and rank
two everywhere else, including p3. This proves the full two-parameter
assertion.

## 4. LR central family: explicit coordinate and lattice maps

Use q for the base coordinate of the supplied LR primary equation

 y^2=x^3+(27/4)q^3(1-q)x+(27/4)q^5(1-q),  P=(-q^2,i q^3).

On the overlap q!=0,infinity set

    X=x/q^2,  Y=y/q^3,  t=27(1-q)/(4q).

The inverse is q=27/(4t+27), x=q^2 X, y=q^3 Y. Substitution gives

    Y^2=X^3+t X+t,       P=(-1,i).                    (GN-fresh-3)

The old cusp q=1 maps to t=0, the old hexagonal point q=infinity maps
to t=-27/4, and the old order-four point q=0 maps to t=infinity. The
sections P and O are transported by the displayed map, hence so is
O(P-O). The divisor of the primary linearization is the old fibre at
q=infinity and becomes t=-27/4. Its lift still covers translation by
-2P. These facts determine the same contracting quotient under this
coordinate transport. No normalization is used without its inverse.

The primary LR global-monodromy proposition supplies, on homology in
its e basis,

 T0=[[-1,-1,-1,0],[2,1,1,0],[0,0,1,0],[0,0,0,1]],
 T1=[[1,1,0,1],[-2,0,-1,-1],[0,-1,1,-1],[0,0,0,1]],
 Ti=[[1,0,0,-1],[-2,0,-1,1],[2,1,2,1],[0,0,0,1]].

The explicit alternating form

 J_e=[[0,2,0,0],[-2,0,-1,0],[0,1,0,-1],[0,0,1,0]]

has determinant 4, and direct multiplication gives T^t J_e T=J_e
for all three displayed matrices. The primary marking change is

 e1=2 f1+f3, e2=f2, e3=f1+f3, e4=f2+f4.

Its column matrix C has determinant one, and

    C^t J_f C=J_e,       J_f=( [0,1;-1,0] ) direct-sum
                                  ( [0,-2;2,0] ).

Thus the flat form used here has an exact integral transport in the
primary named markings. The fresh program checks every multiplication
and both determinants using integer arithmetic and Leibniz expansion.

Locally normalize an elliptic A-period to one, write tau for its
B-period, and let mu be the Abel coordinate of P. The meromorphic
section theta(z-mu)/theta(z) of O(P-O) multiplies by exp(2 pi i mu)
under z -> z+tau. In a logarithmic fibre coordinate the four periods,
ordered f1,f2,f3,f4, can therefore be written

    Pi=[[1,tau,0,-2 mu],[0,mu,1,nu]].                 (GN-fresh-4)

The fourth period is the quotient generator covering -2P; nu records
its nonzero contraction. Directly Pi J_f^{-1} Pi^t=0. This is also
verified with polynomial coefficients by the fresh program. The sign
of the mu in the second row is fixed by the displayed theta factor.

The form J_f on homology induces its inverse on cohomology. For the
Lagrangian Hodge plane F, restriction of that nondegenerate form gives
an exact isomorphism H/F -> F*: its kernel on H is F, and both the
quotient and the dual have rank two. This is the fibrewise map between
E and V used below. Its extensions at the three critical values are
checked with the actual frames in the next two paragraphs.

### 4.1 The bundles and extensions on P(1,4)

The fibre Euler field is a nowhere-zero abstract invariant Lie
generator. A second invariant generator is the horizontal lift, for
the relative line-bundle connection, of the vector dual to
dX/(2Y). The connection with third-kind divisor P-O changes by the
logarithmic derivative of the line-bundle transition, so its horizontal
lift and the Euler field give the intrinsic Lie bundle. Translation by
-2P and the lifted linearization carry this connection by the same
exact logarithmic derivative; the two invariant generators descend.

At the order-four point put t=r^-4, X=r^-2 U, Y=r^-3 V. The good
reduction equation is

    V^2=U^3+U+r^2,        P'=(-r^2,i r^3).

The primary finite covering construction and free affine modification
give the smooth torus cover at r=0. The elliptic differential satisfies
dX/(2Y)=r dU/(2V) on each fibre. Its dual invariant vector therefore
has transition r^-1. The relative third-kind connection has expression
(V+i r^3)/(U+r^2) times dU/(2V), up to the fixed convention for its
residues; this is the same connection after the coordinate substitution,
so the lift has the same transition, possibly plus the Euler generator.
Thus V fits into 0 -> O -> V -> O(-1) -> 0 on P(1,4).
The extension splits because H^1(O(1))=H^0(O(-6))^*=0. This supplies
V=O+O(-1), with its precise order-four character.

The isomorphism H/F -> F* just constructed extends over this root
point: it is the nondegenerate pairing on the smooth torus cover and
is equivariant for the displayed finite monodromy. At the hexagonal
point the primary multiplicative periods are
(c1 q,c2),(c3,c4 q); their constant logarithmic boundary classes give
the coherent H^1(O) frame. The corresponding invariant Lie and Hodge
frames have a constant nonsingular pairing, so the map extends there
without a determinant zero. At the remaining cusp the explicit frame
calculation below proves the same assertion. Consequently E=O+O(-1)
as well. This proves the bundle input used in the global divisor
calculation, including its extensions, rather than importing it from
the unverified-summary paragraph of the LR source.

### 4.2 The cusp logarithmic matrix

At t=0 in (GN-fresh-3), make the exact base change t=s^6 and set
X=s^2 u, Y=s^3 v. The smooth reduction has equation

    v^2=u^3+s^2 u+1,       P_s=(-s^-2,i s^-3).

Its central elliptic curve is smooth. At its origin the formal
parameter z=-u/v satisfies z(P_s)=-i s. To check the differential
normalization directly put w=-1/v. Its equation is

    w=z^3+s^2 z w^2+w^3,

and du/(2v)=(z w_z-w)/(2w) dz= (1+O(z)) dz at the origin.
Thus, with A(s) a nonzero holomorphic A-period of this differential,
the normalized Abel coordinate has

    mu(s)=c s+O(s^2),       c=-i/A(0) != 0.

The central elliptic equation depends holomorphically on s^2, so its
period tau(s) is tau(0)+O(s^2). The pulled-back line bundle has divisor
P_s-O; these sections coalesce at the origin, so its central restriction
is trivial. The linearization is a unit near the original cusp (its
only zero is the hexagonal fibre). Pullback and the displayed divisor
extension therefore give a unit central scalar for its lift. Taking a
local logarithm of the nonzero contraction gives a holomorphic nu(s).
This yields a smooth torus period family (GN-fresh-4) across s=0.

The original relative dualizing differential is

    dX/(2Y)=s^-1 du/(2v).

Consequently its dual invariant Lie generator is s times the good
reduction generator. Relative duality gives exactly the same factor s
for the elliptic coherent H^1(O) generator: the duality pairing of
s^-1 omega_good with s e_good is one. The second Lie generator and the
cyclic-quotient H^1(O) class have unit frames at the cusp. This latter
class is the constant cocycle of the contracting Z quotient; its
restriction on the elliptic curve over the cusp is nonzero. Equivalently
the nonzero additive class of M on the cuspidal cubic has no nonzero
multiple equal to zero, so all nonzero Laurent characters have zero
degree-zero cohomology, while the zero character gives the elliptic
H^1 class and the quotient cocycle. These are the two coherent frames.

In these original coherent frames and for the logarithmic vector
t d/dt=(s/6)d/ds, the matrix coming from (GN-fresh-4) is, up to the
nonzero normalization units already specified,

    [ tau'(s)/(6s)    -mu'(s)/3 ]
    [ mu'(s)/6        s nu'(s)/6 ].                    (GN-fresh-5)

All entries extend holomorphically: tau'=O(s), and mu,nu are
holomorphic. Equivariance supplies their descent to the original
coherent frames on t. Its determinant at s=0 is c^2/18, which is
nonzero. This proves logarithmic rank two at the actual cusp. It also
shows that the flat pairing map between V and E has no determinant
zero there: the elliptic factors on its two sides are both s, and the
quotient factors are units. The ordinary good-reduction matrix and
the original logarithmic matrix are related by (GN-fresh-5); neither
rank convention is silently substituted for the other.

### 4.3 Exhaustion of the LR divisor

On P(1,4) the logarithmic divisor has the two ordinary points, the
cusp and the hexagonal point. Therefore Omega(log D)=O(3). Since
V=E=O+O(-1), its four entries have weights 3,2,2,1. With x=0 at the
order-four point they must have the form

    [ a x^3   b x^2 ]
    [ c x^2   d x   ],       det=(ad-bc)x^4.

Every entry is zero at the root point. The logarithmic matrix is
nondegenerate at the cusp by (GN-fresh-5) and at the hexagonal point
by its two independent logarithmic periods. Thus ad-bc is nonzero.
The determinant has order exactly four at the root point, and has no
other zeros. Its rank is two everywhere else. This proves all of the
LR assertion with the required cusp extension supplied explicitly.

## 5. Positive combs: transport of the tautological sequence

The primary comb construction starts with the marked cohomology bundle
H' and a period section of Gr(2,H'). Its specified extension over the
coarse base P1 is H, and its tautological exact sequence is

    0 -> F_sigma -> H -> E_sigma -> 0.

The original and smoothed sections have the same value at each of the
three critical points. On the finite cover t=w^n, the primary source
gives the invariant frames

    D3(w)=diag(1,1,w,w^2),
    D4(w)=diag(1,1,w,w^3).

The columns are interpreted in the flat covering cohomology frame.
For a local change of plane Psi(t)=I+O(t), its actual lift is

    Psi_sharp(w)=D_n(w) Psi(w^n) D_n(w)^-1.

Every off-identity exponent is at least n-(n-1)=1. Hence this is
holomorphic, equals I at the centre, and is equivariant because
D_n(zeta w)=rho D_n(w). It carries the entire original covering
Hodge subbundle to the new one. This constructs the root Hodge bundle
and quotient, with exactly the original finite characters. Applying
finite pushforward and invariants recovers the given coarse exact
sequence, as in the primary source's finite-filling proof. The root
bundles have therefore been constructed through explicit maps.

At the hexagonal point the primary frame is e_i=alpha_i+ell(t) beta_i,
f_i=beta_i, ell=(log t)/(2 pi i). It has connection
nabla e_i=f_i dt/(2 pi i t), nabla f_i=0. Its determinant transition
from the flat frame is one. The Hodge plane is the graph (I,H_sigma(t)).
This also constructs the root/coherent extension at that point.

The constant integral volume on H' extends without a zero on the root
curve: the two finite monodromies have determinant one and the full
root cover removes their fractional character factors; at the cusp
the displayed logarithmic frame has determinant one and trace-zero
residue. Thus det H_root is the trivial line, with this explicit volume.
Taking determinants in the root tautological sequence gives an actual
isomorphism

    det V_sigma = det(F_sigma*) = det E_sigma.

It does not require a polarization on a general comb section.

Let m be the number of teeth. The primary tautological calculation
has E|tooth=O(1)+O(1); smoothing the comb therefore changes the
coarse degree of E by exactly 2m. The root finite characters are
unchanged by the Psi_sharp map. Hence the difference of determinant
line bundles descends to the coarse O(2m). On B=P(3,4), the current
I root-bundle definition gives rho*O_coarse(1)=O_root(12), while the
original determinant is O_root(-1). It follows, with these exact
descent maps, that

    det E_sigma = O_root(24m-1).

The logarithmic differential line with the one hexagonal point is
O_root(-7+12)=O_root(5). Consequently

    det kappa_sigma belongs to H^0(O_root(48m+8)).

A monomial x^a y^b of this weight satisfies 3a+4b=48m+8. Modulo four
one obtains a=4i; modulo three, b=3j+2. Substitution gives i+j=4m.
Conversely every i,j>=0 with this sum gives a monomial of that weight.
Therefore the determinant has exactly the expression

    y^2 P_sigma(x^4,y^3),       deg P_sigma=4m.

This is an all-m integer proof. The fresh program also enumerates the
exponent solutions for m=0,...,80 as an arithmetic cross-check; this
finite enumeration is not used to infer the universal statement.

At the hexagonal point the quotient of nabla(e+H_sigma f) evaluated
on t d/dt is (1/(2 pi i)) I+t H_sigma'(t). At t=0 it is the nonzero
scalar matrix (1/(2 pi i)) I. Thus the logarithmic determinant is
nonzero there. In particular P_sigma is nonzero and has no zero at
that cusp. A choice of the marked volume and the fixed root
coordinates specifies the determinant line isomorphism; changing that
isomorphism multiplies it by a global invertible function on the
compact root curve, hence by a nonzero scalar. This proves the claimed
uniqueness up to scalar.

Finally (GN-fresh-1) calculates the actual matrix for each specified
section. The determinant and all four entries therefore give precisely
the rank test in the statement. The argument makes no choice of a
particular zero set for an unspecified period section.

## 6. Arithmetic certificate and scope of completion

The companion prereading program proves by exact coefficient operations:
the LR coordinate substitution, the primary lattice change and all three
monodromy invariances, the isotropy of the displayed period matrix, the
nonzero symbolic cusp determinant, the weighted two-parameter and LR
determinants, and the general graph-projection formula. It also checks
the finite range of comb exponent solutions stated above. Its output
must be bound before release; failures would keep this derivation open.

All five parts of the given E16 statement have now been derived from its
stated input and the explicitly read primary constructions. The
two-parameter calculation uses the earlier independently checked GK
bundle maps. The original-family part uses the cited E8 result as input.
No independent check of those inputs is claimed a second time. The
remaining task after the freeze is to read the complete E16 target,
compare each step and its actual conventions, inspect any associated
old computation under a bounded release, and prepare complete guarded
publication pairs. This document makes no claim that those later tasks
have already occurred.
