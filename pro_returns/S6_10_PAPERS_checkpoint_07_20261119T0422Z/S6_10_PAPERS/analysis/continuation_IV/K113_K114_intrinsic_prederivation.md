# Intrinsic quotient and base rigidity before EB/EBR/EBP and III proofs

19 November 2026. GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro.
The full EF proof of K109 has now been read. The EB, EBR, EBP, and
K114 III proof files have not been opened. This derives the strengthened
base-rigidity substep from the statements and the explicit EF lattice.

The monodromy-invariant rational vector line is Qδ and the invariant
rational covector line is Qψ. Their primitive integral generators have
no unspecified finite index: δ is the physical circle and ψ sends the
suspension generator to1. Any endpoint isomorphism, including one over
a base permutation, transports invariant vectors and covectors through
the induced permutation of monodromy loops. It therefore sends the two
primitive integral lines to the corresponding target lines, with signs.

The isomorphism of rank-four integral lattices sends kerψ onto the
target kerψ, with an inverse. Covering space lifting then gives an
isomorphism of the actual cyclic covers M_a^×. On universal covers its
linear part is complex linear. Since δ is sent to ±δ, its complex span
is preserved. The induced map on the quotient by that complex span is
an affine map of the original elliptic source. Its integral lattice is
kerψ/Zδ, and the integral inverse makes its degree exactly1. Thus an
endpoint over h gives a genuine elliptic isomorphism E_t→E_{h(t)}, so
j(t)=j(h(t)); this conclusion does not assume beforehand that the
endpoint preserves an elliptic source chosen extrinsically.

For the original E6 equation,

    c4=16(r²−3t),
    Δ=−16t²[27t²+(4−18r)t+r²(4r−1)],
    j=−256(r²−3t)³/[t²(27t²+(4−18r)t+r²(4r−1))].

For r outside {0,1/4,1/3}, t=0 is the unique double pole; the two
simple nodes are simple poles. The nonzero finite point t=r²/3 is
the unique triple zero, because the node quadratic there equals
r²(3r−1)²/3≠0. Infinity is a simple zero (j~256/t) and also the
unique base critical value with a non-unipotent order-three elliptic
block. Hence h fixes 0, infinity, and r²/3. The unique Möbius map
fixing these three distinct points is the identity. An explicit
proof is that fixing0 and infinity gives h(t)=ct, and fixing r²/3
gives c=1. This covers the P_rQ_r=0 values omitted by K109.

At the III source r=0, cancellation of the actual common factors gives
j(t)=6912/(27t+4). This rational map has degree1, with explicit inverse
t=(6912/j−4)/27. Consequently j∘h=j directly gives h=id.

After base rigidity, the EF centralizer argument applies to the
unchanged full period module and the nonzero Abel cocycle; the generic
I1 and the order-three infinity block still occur. It reduces the
linear part to ±I with the rank-one shear excluded by complex rank.
For an automorphism of one completed object, −I would give a finite
étale fixed curve over the regular base. Its proper analytic closure
is a horizontal curve. Its normalization has positive degree over P1,
but the pullback of the base area class is zero in H²(X), a
contradiction by integration. This is an actual closure argument in
the compact completed threefold. It does not by itself exclude a
negative endpoint between distinct scalar objects; that further claim
still needs the annular deck comparison of K110.

To finish K113/K114 the printed proof must still carry the actual
Cartier, source section, root, reference, and selected-fan maps across
the enlarged locus, with all finite characters and both signed norms.
The rational j identity alone does not establish those extensions.

## Additional III-source derivation before its proof is opened

At r=0 put t=z⁴, x=z²X, y=z³Y. The exact good-root equation is
Y²=X³+X+z², with deck (z,X,Y)↦(iz,−X,iY). Its central
differential dX/(2Y) has eigenvalue i, so the elliptic period module
has no nonzero invariant vector at this additive fibre. The affine
original differential is z^(−1) times the good differential.

Here s=1/4. The explicit doubled point is
2G=(1/4,−t−1/8); on the smooth part of the central cusp its
additive coordinate −x/y is2, which is nonzero. On the root the
formal logarithm has leading term2z; division byz is the extending
original Lie coefficient. Thus integer multiples of this point do
not vanish. The same global O(−1) Lie-line argument proves that the
Abel cocycle remains nonzero; the local III invariant-period
ambiguity is zero by the displayed order-four deck.

The exact rational chart U=y−t−x/2, V=y+t+x/2 gives
UV=x²(x−1/4), now with t=(V−U−x)/2. Its central total-space
singularity is A1, with exceptional component of self-intersection−2.
The G-section tangent is [x:U:V]=[0:0:1], whereas the strict central
fibre lies in V−U−x=0, so G meets the exceptional component away
from the component intersection. Together with the unchanged infinity
E6 components, O and F, the same ten-class Gram matrix used in EF
therefore gives the source section generator. The finite Euler numbers
are III=3 and I1=1; adding IV*=8 gives12.

The full finite-point-line formulas depend on s and remain defined
at s=1/4. In the exact source chart x=s+(w−1)(w+h),
t=xh/2, y=x(2w+h−1)/2, the M2 coefficient remains
B_(2,1)/t=2(w+h)/(s−(w+h)h). The generic coefficient is nonzero
on each relevant component; after its vertical order is removed,
the actual numerator/denominator Cartier Hom divisor is zero.
The original point/O modules retain their possible intersections.
The same M6 generic coefficient 8((1−s)w−s)/s³ is nonzero as a
function ofw at s=1/4. Its component order propagates through the
actual A1 intersection matrix. The zero additional norm at this
order-one III attachment changes no scalar-reference exponent.
These give the explicit substeps by which the EF/SEF maps can extend
to the III source. The printed proof will be checked for these precise
arrows and the remaining complete root/annular extensions.
