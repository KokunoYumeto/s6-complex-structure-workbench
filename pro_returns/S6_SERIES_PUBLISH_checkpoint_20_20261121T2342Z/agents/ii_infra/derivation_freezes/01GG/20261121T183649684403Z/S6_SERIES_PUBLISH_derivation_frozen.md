# Derivation before target proof: 01GG

Owner: `cdp:st:E1`. Checker: `i_provenance`.
Only the statement packet and safe front conventions have been read for this
target. Earlier Paper I background exposure is retained; no earlier target
proof, derivation, or program has been consulted.

Take an effective divisor D on Y. Its analytic irreducible components are
finite in number by compactness. A component dominating C would meet a general
smooth Kahler fibre F properly in a nonempty effective divisor D_F. Choose a
Kahler form omega on F. Since dim_C F=n-1, the integral of the current [D_F]
against omega^(n-2) is strictly positive, including the n=2 case where it is
the positive degree of the effective zero-cycle. But this integral is the
pairing of c_1(O_Y(D)|_F) with [omega]^(n-2). The restriction of this real
Chern class is zero because H^2(Y,R)=0, a contradiction. Thus no component
dominates C. Properness then makes its image a point. Hence D is supported on
a finite union of fibres. The argument uses a smooth Kahler fibre only in the
given nonempty open set and requires no reducedness of the other fibres.

The pullback g^*:M(C)->M(Y) is injective by surjectivity of g. For surjectivity,
let h be meromorphic on Y. Its polar divisor has vertical support by the first
part. Away from finitely many base points h is holomorphic; it is constant on
each compact connected fibre there. Properness, normality of the smooth total
space and the normal curve, and connected fibres give g_*O_Y=O_C by the Stein
factorization. Consequently these values define a holomorphic function on that
base open set, with pullback h.

This function extends meromorphically at every deleted base point b. Indeed,
choose a local coordinate t vanishing at b. The full Cartier divisor g^*b has
strictly positive multiplicity on every component over b. A sufficiently large
integer N makes div((g^*t)^N h) effective near that fibre. On the smooth (hence
normal) total space a meromorphic function with no codimension-one poles is
holomorphic. It therefore descends by g_*O_Y=O_C to a holomorphic function h_b,
and h=t^{-N}h_b on the punctured base neighbourhood. This is the required finite
pole extension. The descended meromorphic functions agree on overlaps by
surjectivity. Thus g^* is the stated isomorphism of fields.

A compact connected Riemann surface has meromorphic function field of
transcendence degree one, so a(Y)=1. No computational step requires a program:
the argument consists of the explicit restriction/pullback maps, positivity,
Stein factorization, and the normal-space pole criterion. Proof comparison and
event qualification remain pending.
