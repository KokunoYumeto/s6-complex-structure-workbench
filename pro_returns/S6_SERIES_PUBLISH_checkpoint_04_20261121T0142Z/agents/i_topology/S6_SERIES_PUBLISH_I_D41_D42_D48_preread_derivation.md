# Preread derivation — push:src:D.4.1 [032J], D.4.2 [032K], D.4.8 [032Q]

All three target proofs remain unopened. Statements of D.2.1, fam:C.1.1, fam:C.2.3, fam:C.3.1–2, D.4.4–5, and ari:C.8.15 have been read from the proof-masked source. The global critical-factor/radial theorem ari:C.8.15 is an input, not independently re-proved or numerically certified in this check. D.4.3 has a separate preread derivation and subsequent comparison.

## D.4.1: first supercritical curve and its coefficient

Put H*=−M=(3/π)log6. At H=H*+epsilon the stated local expansion is D=epsilon−3|h|²+O(|h|⁴), with real-analytic remainder in the root coordinate. In polar coordinates its radial derivative is −6r+O(r³), uniformly in angle, so for epsilon>0 sufficiently small there is exactly one positive radial zero r(theta). Applying the real analytic implicit theorem to r²/epsilon near1/3 yields r²=epsilon/3+O(epsilon²), uniformly. This is one simple closed real-analytic root curve. The order-four deck rotation preserves D and acts freely on the curve; the coarse quotient maps this circle to one embedded real-analytic circle around t=1.

The unique-global-maximum input and D_part→−infinity at the cusp make D_part bounded below its maximum by a positive gap outside any sufficiently small root neighbourhood of1. Thus no additional level component occurs for small epsilon. The inside has D>0 and the cusp side D<0.

For the leading coarse coefficient, D.2.1 gives δ=τ−i=−(3πi/2)h²+O(h⁴). The modular identities t−1=E6²/(1728Delta0), 1728Delta0(i)=E4(i)³, and E6'(i)=−πi E4(i)² yield
 t−1=−π²E4(i)δ²+O(δ³)=(9π⁴E4(i)/4)h⁴+O(h⁶).
Taking absolute values and substituting r² gives |t−1|=(π⁴E4(i)/4)epsilon²(1+O(epsilon)), with the same uniformity. The sign follows from the two factors i²; this coefficient will be checked with fresh exact rational arithmetic.

## D.4.2: all heights, connected negative region, and the domain

The exact norm identity is D_part=(6/π)log(N/(2sqrt3)). Thus D_c=0 is exactly N=2sqrt3 exp(−πH/6). The theta norm is invariant under the integral elliptic-period changes and modular transport; its expression on the retained wp-zero section therefore gives a function on the stated coarse base. The cusp asymptotic tends to minus infinity, so a fixed finite level stays in a compact part of the finite plane. The root-chart periods and the norm are real analytic, hence the zero set is real analytic there and the usual implicit theorem gives smooth real curves at regular points.

For connectedness no global critical-locus certificate is necessary. Let y=Imτ>0 and m=Imμ. On any holomorphic root coordinate z, both y,m,Imβ are harmonic. Direct differentiation gives
 ∂z∂barz(m²/y)=|μ_z−(m/y)τ_z|²/(2y),
 ∂z∂barz D_part=−3|μ_z−(m/y)τ_z|²/y≤0.
Thus D_part is superharmonic. Its invariant finite-root extension is superharmonic downstairs as well: on the root cover a minimum principle applies to the lifted component, or equivalently the invariant subharmonic distribution pushes down under the finite quotient. A component of {D_c<0} that avoids the connected negative cusp neighbourhood would have compact closure and boundary value0, hence a negative interior minimum, contrary to the minimum principle. Consequently the entire negative region, with the cusp added, is connected.

Where D is nonzero, the real period matrix is invertible; on each relatively compact base neighbourhood its inverse is bounded, giving a uniform lower bound on the lengths of nonzero integral periods. The lattice action is therefore free and properly discontinuous there. The prescribed finite affine fillings extend whenever their root torus remains nondegenerate; the original toric cusp filling is available for every constant c because its correction is holomorphic. Thus this gives the asserted construction over B\Z_H.

At a zero, the last three columns are independent (Imτ>0), while the determinant vanishes, so rank=3. D.4.3 describes the central quotient. If its kernel is irrational, the central quotient is already non-Hausdorff. If it is rational, choose a nonzero primitive integral kernel vector v. The holomorphic period Π(z)v vanishes at that point and is not identically zero on a neighbourhood (nearby nondegenerate periods exist). Write its first nonzero term a(z-z0)^r. With z_j-z0 chosen as an rth root of alpha/j, jΠ(z_j)v→alpha a. This constructs nonseparated central representatives differing by a sufficiently small nonperiodic multiple of a. Hence the full attempted quotient across that point is not a Hausdorff complex-manifold extension of this construction, even where the central rank-three quotient alone is a complex Lie group. This argument supplies the exact local map and sequences behind the word “precisely”.

## D.4.8: translate the established global level theorem

Let L=logN and c(H)=log(2sqrt3)−πH/6. Then H>H* is exactly c(H)<log sqrt2. The input ari:C.8.15 states that on each ray from1, L decreases strictly from log sqrt2 to−infinity, with a single Jordan level and the stated regularity. For a fixed H, solving L(1+r e^(i theta))=c(H) gives the unique positive radius. Its radial derivative is nonzero at ordinary points; the global theorem and D.4.5 give a nonzero coarse C1 derivative at0. Thus the curve is embedded C1 and analytic except at the stated possible crossing point. The bounded disc is {L>c(H)}={D_c>0}; the unbounded one is {D_c<0}, with the cusp adjoined.

At0, L=(1/4)log3. The exact threshold is
 H0=(6/π)(log(2sqrt3)−(1/4)log3)=(3/(2π))log48.
It exceeds H* by (3/(2π))log(4/3). D.4.5 gives D_t(0)=7/(64π), hence the zero at H0 is a regular C1 arc tangent to the imaginary axis, rather than a singular coarse level. The sign at0 increases with H, giving exactly the three stated positions.

Since c(H) decreases strictly, the bounded superlevel discs increase strictly. Their intersection as H decreases to H* is the unique maximum point1; the compactness-away-from-cusp argument makes this actual shrinking. Every finite point has finite L, so it belongs to a bounded disc for H large enough; this proves exhaustion. D.4.1 supplies the small-height shape. The two open complement discs are exactly the maximal base locus just checked in D.4.2.

Finally the real period determinant in the fixed row order is y Imβ−6(Imμ)²=y D_c. Its absolute value is the Euclidean covolume; as one approaches a fixed boundary point y is finite and positive in a root marking, and D_c tends to0. Thus the covolume tends to0 and rank falls exactly to3. The precise limiting quotient is D.4.3's one; a Chabauty limit is not silently substituted for it.

## Independence and pending computation

These are new derivations from the stated inputs, saved before the target proofs. The exact local coefficient, logarithmic threshold identity, real determinant and superharmonic derivative will be recomputed by a fresh polynomial/rational program. The existing global radial certificate and the numerical value of E4(i) are not recomputed here, and no claim will be made that they are.

Saved UTC: 2026-11-21T01:18:06.924922+00:00
