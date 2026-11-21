# Derivation before target proof: 01BP

Owner: `cdp:st:C.1.3`. Checker: `i_provenance`.
The original statement packet and the exact S6_09 Compendium II C.1.2/C.1.1
supplement have been read. The target proof remains unopened. The missing
CompendiumRef scope was requested and supplied before this derivation.

The hypotheses are a connected compact complex threefold Y with b_1=b_2=0,
and a nonzero effective Cartier divisor D with arbitrary positive
multiplicities. Fix one connected component P of Pic(Y), and apply the cited
Compendium C.1.2 with E=T_Y. On its dense open P_E the two endpoint dimensions
h^0(T_Y tensor L) and h^3(T_Y tensor L) vanish. Thus, on P_E,

1-b_3(Y)/2 = chi(T_Y tensor L) = -h^1(T_Y tensor L)+h^2(T_Y tensor L)
<=h^2(T_Y tensor L),

where the first equality is the separately derived current C.1.1 and also the
exact cited-compendium C.1.1 statement. Each dimension is nonnegative, so the
lower bound is max(0,1-b_3/2).

This same bound holds at every point of P. Locally a holomorphic family of line
bundles represents the Picard parameters, and proper analytic cohomology
semicontinuity makes {L : h^2(T_Y tensor L)>=N} closed for each integer N.
Taking N=max(0,1-b_3/2), this closed set contains the dense open P_E, hence all
of P. The integer N is well-defined because the middle odd-degree pairing in
oriented dimension six is alternating and nondegenerate, so b_3 is even.
The component P was arbitrary. Consequently b_3=0 forces h^2>=1 for every
twist. A twist with h^2=0 instead forces 1-b_3/2<=0, equivalently b_3>=2.

The divisor multiplicities enter only the cited endpoint-vanishing input and
are retained without reduction. This is a derivation from exact cited results,
not a rereading of their proofs. There is no separate computational program
needed for the two-term index inequality or the semicontinuity argument.
Prior Paper I cohomological exposure remains disclosed; event qualification
and whole-target-proof comparison are still pending.
