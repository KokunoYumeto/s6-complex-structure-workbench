# Clean prerelease derivation: 01FC / cdp:st:C.3.6

Checker: i_provenance_recovery.

The original safe 01FC statement and its empty supplement have been read.
The target proof, its internal C.H.1 formula, the former C reconstruction,
and E_checks.py remain unopened. The separate 02WI construction was written
and frozen before either target was released; its target proof also remains
unopened. Earlier Paper I geometry and SS2002's primary diagonal-Hopf
classification are disclosed background. This proof constructs the required
algebraic-dimension-one examples directly.

## Primary Hopf bundle

Let c1=1 and c2=sqrt(2). On
U=(C^2 minus {0})_z x (C^2 minus {0})_w use the holomorphic additive C-action

  lambda . (z,w1,w2)
    = (exp(lambda)z, exp(i c1 lambda)w1, exp(i c2 lambda)w2).

The action is free. Fixing z forces lambda=2 pi i k. Every nonzero w
coordinate would then be multiplied by exp(-2 pi cj k), and this equals
one only for k=0.

Write lambda=x+i y. The z norm is multiplied by exp(x), and the squared
w norm becomes

  exp(-2 c1 y)|w1|^2 + exp(-2 c2 y)|w2|^2.

For a nonzero w this expression is strictly decreasing from infinity to
zero as y increases from minus infinity to infinity; its derivative is
strictly negative. Given any point of U there is therefore a unique real
pair (x,y) making both norms one. The implicit-function theorem makes this
choice smooth. It is invariant under the original action in the same
orbit-normalization sense as in the separate WI derivation. Thus each orbit
meets S3 x S3 exactly once, and the quotient Y is diffeomorphic to S3 x S3.

For properness, compact bounds above and away from zero on the z norms
bound x. The two positive constants cj bound the scaling of the w norm
between the corresponding exponentials of y. If y tends to plus infinity
the transformed norm tends uniformly to zero on compact subsets; if y
tends to minus infinity it tends uniformly to infinity. Compact bounds on
the transformed point therefore bound y as well. The action map is proper.
The free proper holomorphic quotient is a smooth complex threefold; local
holomorphic slices are obtained by fixing a nonzero z coordinate using a
local logarithm. The explicit smooth slice proves compactness, connectedness,
H1(Y,Z)=H2(Y,Z)=0, and e(Y)=0.

The invariant map (z,w)->[z] descends to f:Y->P1. It is a holomorphic
submersion. Over a local choice of representative z0(t), write z=v z0(t).
The holomorphic fibre map is

  (v,w1,w2) -> [exp(-i c1 log(v))w1, exp(-i c2 log(v))w2].

Changing the logarithm by 2 pi i k multiplies coordinate j by
exp(2 pi cj k), a power of the inverse of the diagonal contraction

  Q(w1,w2)=(q1 w1,q2 w2),  qj=exp(-2 pi cj).

The map is therefore well-defined into
H=(C^2 minus {0})/<Q>. Its inverse sends [w] to the orbit class of (z0(t),w).
These maps give a local holomorphic product f^{-1}(V)=V x H, so f is a
smooth holomorphic bundle with connected primary Hopf fibre H. The deck
group on the simply connected cover C^2 minus {0} is infinite cyclic.

## Algebraic dimension of the fibre

The positive real numbers q1,q2 are multiplicatively independent:
q1^a q2^b=1 for integers a,b means a+sqrt(2)b=0, hence a=b=0.

Let h be a meromorphic function on H. Its lift is a Q-invariant meromorphic
function on C^2 minus {0}. Meromorphic Hartogs extension gives a meromorphic
germ at zero, representable as f/g for coprime convergent power-series
germs f,g in the factorial local ring C{w1,w2}. The invariance equation is

  f(Qw)g(w)=f(w)g(Qw).

Coprimality gives f(Qw)=u(w)f(w) and g(Qw)=u(w)g(w), with the same unit
u. Indeed divisibility follows from that equation in the factorial local
ring, and composition with the invertible linear Q preserves the order at
zero, so the quotients have order zero and are units.

Write u0=u(0). Choose the convergent logarithm L=log(u/u0), whose constant
coefficient is zero. For each nonzero multi-index I, let q^I=q1^I1 q2^I2
and set the I coefficient of v to L_I/(1-q^I). These coefficients define a
convergent germ: |1-q^I| is at least 1-max(q1,q2)>0. Then

  v(Qw)-v(w)=-L(w).

Multiplying f and g by exp(v) gives germs f1,g1 satisfying
f1(Qw)=u0 f1(w) and g1(Qw)=u0 g1(w). A nonzero coefficient of either
eigenfunction must have q^I=u0. Multiplicative independence makes that
multi-index unique. Both germs are therefore scalar multiples of the same
monomial. Their ratio h is constant. This proves M(H)=C and a(H)=0 by
the actual germ and deck transformations.

## Algebraic reduction of the total space

Every meromorphic function on Y restricts to a meromorphic function on a
general fibre and hence is constant there. One can express the resulting
descent without choosing fibrewise constants: take the closure of its graph
in Y x P1, project by (f,id) to P1 x P1, and use properness. The image is a
compact analytic curve with generically one point over the first P1. Its
normalization is birational to that P1, so it is the graph of a meromorphic
function on the base. The original meromorphic function is its pullback,
because they agree on a dense open subset. Conversely all base rational
functions pull back. Thus

  M(Y)=f^*M(P1),

and a(Y)=1. The map f has connected fibres and is already holomorphic, so
it is the stated holomorphic algebraic reduction.

## Secondary Hopf bundle

Fix m=2 and let the finite group mu_2 act on U by
(z,w1,w2)->(z,-w1,-w2). It commutes with the C-action and preserves [z].
Its induced action on Y is free. A fixed orbit would require a parameter
lambda fixing z, hence lambda=2 pi i k, and would give
exp(-2 pi cj k)=-1 on a nonzero coordinate. The left side is positive
real, so this equation has no solution.

The quotient Y2=Y/mu_2 is a smooth compact complex threefold and Y->Y2 is
a finite unramified cover of degree two. The descended map f2:Y2->P1 is a
holomorphic bundle whose fibre is H2=H/mu_2. Its universal cover remains
C^2 minus {0}; its deck group is generated by Q and -I. The only relation
between the two generators is (-I)^2=I, since a nonzero power of Q has
positive eigenvalues of modulus different from one. Hence pi1(H2) is
Z x Z/2. This Hopf surface is secondary: the exact degree-two cover H->H2
has primary Hopf source, and the deck group of H2 is not infinite cyclic.

Transfer for the finite unramified map injects H^j(Y2,Q) into H^j(Y,Q).
The latter vanishes for j=1,2, so b1(Y2)=b2(Y2)=0. Euler characteristic
multiplies by the degree of a finite cover, hence e(Y2)=e(Y)/2=0.
Meromorphic functions pull back injectively to M(Y)=f^*M(P1), and all base
functions already descend through f2. Thus M(Y2)=f2^*M(P1), a(Y2)=1, and
f2 is its holomorphic algebraic reduction.

Each primary Hopf fibre is a mapping torus of its diagonal contraction on
the punctured C^2 and has Euler number zero. Equivalently its logarithmic
radial coordinate gives a compact fundamental annulus with boundaries
identified, a bundle over S1 with fibre S3. The secondary fibre has Euler
number zero by its finite primary cover. Both total spaces are smooth
compact complex threefolds, so the complex-oriented Chern--Gauss--Bonnet
identity gives c3=e=0. These constructions establish every requested
existence, topology, algebraic-dimension and Euler assertion.

No target proof or inherited computation has been read. The numeric choices
are exact; irrationality of sqrt(2) is used algebraically, without numerical
sampling. Full printed-proof and earlier-method comparisons remain pending
until this complete derivation is frozen.
