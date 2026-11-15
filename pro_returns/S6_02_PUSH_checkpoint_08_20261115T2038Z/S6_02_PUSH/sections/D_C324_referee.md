# Independent referee: C.3.24, actual smooth monodromy

**Result:** pass. Referee: boundary_d. This audit uses the actual geometric proofs C.3.18--C.3.23, not just their numerical outputs.

## Integer cancellation

C.3.18 gives the actual affine-framed relative Pontryagin number minus 24. C.3.21 identifies the actual delta-line mixed class and proves its relative square is minus two. The connection normalization in C.3.22 makes the same cap-orientation sign occur in both pairings. Therefore the cap integer is

`epsilon_cap * (-24 - 12*(-2))/24 = 0`

as an integer. No unknown orientation or Wall--Davis generator sign affects zero. The earlier wrong-sign diagnostic was resolved by the inverse between a boundary-frame change and a coordinate clutch, checked directly with connections.

## Equivariant sixth-power comparison

For a positive w loop, c decreases by two. After six loops the actual path runs from c0 to c0 minus 12 and closes by the positive shift F12 at c0 minus 12. Six positive-shift F2 maps compose in ascending c order from that endpoint. Since the gamma column changes by h times e, direct substitution in the displayed b formula gives `b_(h,c)+b_(k,c+h)=b_(h+k,c)`. Thus these six maps give exactly F12 with the required source and target.

A circle-invariant connection on the descended w-family gives the same equivariant return map on every repetition of the loop. Its sixfold return is the sixth power. Interpolation with the invariant connection used for C.3.10 is an equivariant isotopy. The finite-root transport, cusp unit multiplication, global real C-star flow, and logarithmic gauge comparison in C.3.6 are all equivariant. Changing the coherent closings to the originally stipulated R2 closings is also equivariant, since the scalar difference belongs to the connected C-star action centralizing delta.

Therefore the actual annular lift and the sixth power agree in the equivariant component group, not merely after forgetting the circle action.

## Consequences

C.3.23 makes the orbit-knot coordinate an integer homomorphism. The preceding calculation gives `6 q(Phi)=0` in Z, so q(Phi)=0. Its fixed signed reduction modulo 28 is the ordinary monodromy class, hence that class is zero. This avoids dividing by six in Z/28 and removes its possible order-two ambiguity.

An ordinary isotopy of the return map to the identity gives the oriented product mapping torus. Positive powers, hence all finite cyclic base changes, remain trivial. The twist-data consequence is restricted exactly to the family comparison proved in C.4.1.

This referee record makes no assertion about an analytic extension of the complex family. Trivial smooth monodromy is compatible with the analytic nonextension and degeneration obstructions elsewhere in the manuscript.
