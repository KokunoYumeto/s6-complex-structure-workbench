# Tightening the degree-six coordinate argument

This note leaves the frozen derivation and its receipt unchanged.

The degree-six argument needs a coordinate calculation for the specified invariant-subtorus cycles. It does not need a claim that flat fibre volume has integral periods on every six-cycle of the whole two-edge graph bundle, nor that mapping tori of invariant subtori of the individual edges form an integral basis of that entire graph homology group. The subsidiary sentence near the end of frozen Section 4, and its restatement in the first after-reading note, gave more than was justified about a whole graph splitting.

The exact argument used in `receiving_guards_08.json` is narrower. The two compared lifts have the same edge coordinates in the integral graph Wang sequence. Their difference therefore belongs to the image of the fibre top class, a copy of `Z`. The closed flat fibre-volume form evaluates as one on that generator. On the particular transported five-torus prisms both representatives have zero integral: the fibre tangent support has dimension five, and the comparison chains can be kept in the finitely many transported five-tori and their intersections by relative cellular approximation. Hence the integer coefficient of their difference is zero. This establishes the precise integral morphism on the chosen cycles without a statement about the periods on unrelated graph cycles.

The edge coordinates remain exactly `(-W_2W_0 x_j,-W_0 x_j)`, and the fibre coordinate is zero. The toric forgetful map preserves `b`, so its image of the cycle lies over `b_j=0` with total dimension at most five. That proves its zero cusp homology image. The filler identities `d_Y F_k=J_k` supply the other degrees as recorded in the frozen derivation.

The guard file is the exact version proposed to the parent for the printed proof. This tightening removes an unnecessary broad claim; it does not alter any differential, basis adapter, computed group, or the local secondary-class argument.
