# Paper V analytic check: derivations recorded before the printed proof

UTC: 2026-11-20T22:45:44.030674+00:00

Source read so far: main Theorems E and F and theorem statements (not their proofs) bearing labels night:P1.15, night:P1.18, night:P1A.1--6, night:P1.17, maps:src:F.2.39, maps:src:F.3.4, maps:src:F.3.8, maps:src:F.3.10, maps:src:F.3.11.

## Cohomology and root line
The specified effective root curve has orders 5 at infinity and 4 at zero. Its orbifold canonical degree is -2+4/5+3/4=-9/20. The line L has degree 4/5-3/4=1/20, so K_B has the same degree as L^{-9}; equality of line classes must also be checked using the local characters. The vertical cotangent determinant from O+L+L^2 is L^3, giving K_M=h^*(K_B tensor L^3)=h^*L^{-6}, before the local cusp extension is checked.

For an integral power n, the invariant coarse divisor of L^n is floor(4n/5)[infinity]+floor(-3n/4)[zero]. Its degree d_n gives h^0=max(d_n+1,0), h^1=max(-d_n-1,0). For q=0,1,2,3, the exterior powers of G=O+L^{-1}+L^{-2} have exponent multisets {0},{0,-1,-2},{-1,-2,-3},{-3}. Direct cohomology therefore gives h^q(O_M)=(1,1,0,0,0), subject to the asserted extension/base-change identification at the cusp. This last identification needs inspection: smooth-fibre torus formulas alone do not prove it.

Serre duality in dimension four requires h^{p,q}=h^{4-p,4-q}, which the displayed table satisfies. Alternating row sums are 0, -1, 4, -1, 0. Total alternating sum is 6, matching the asserted Euler number. The first Froelicher page has degree sums 1,1,2,2,6,2,2,1,1. A simply connected manifold with b2=b3=0 therefore requires nontrivial differentials; Hodge numbers by themselves do not give those ranks. The printed proof must provide actual maps, not only Euler-number constraints.

A one-dimensional Kuranishi germ with a nonzero Kodaira--Spencer map from a smooth one-dimensional parameter space has a local holomorphic section of its embedding in H^1(T). In a minimal analytic germ inside C, an image containing an open disc forces the defining ideal to vanish. Thus h^1(T)=1 plus the claimed nonzero parameter derivative yields smoothness. Tangent dimensions still require independent map calculations.

## Punctured-disc parameter
A holomorphic classifying parameter xi:Delta* -> {Im xi>c*} becomes a bounded map to the unit disc by a Cayley transform. The removable-singularity theorem extends it across zero. Its limit lies in the open disc: a boundary value would force constancy by the maximum principle. This also rules out an infinite xi limit. Gluing local marked families requires local completeness and the automorphism group; after a degree-at-most-two cover, the Z/2 torsor disappears. The remaining additive C torsor on Delta* is holomorphically trivial since H^1(Delta*,O)=0. The actual isomorphism and local-completeness assertions need checking against the printed argument.

## Punctured-base period assertion
The space D_3=GL^+(6,R)/GL(3,C) retracts onto SO(6)/U(3), a simply connected compact homogeneous space isomorphic to CP^3. The base punctured sphere retracts to a graph. Thus a D_3-bundle has no obstruction to a continuous section, and a prescribed local cusp section can be extended continuously over the graph. A holomorphic section requires the stated LSAP/Oka argument, including interpolation at the puncture after a logarithmic modification. Merely approximating on annuli is insufficient to retain a bounded holomorphic cusp correction. The proof must establish a holomorphic section problem with an open fibre over the added cusp point and an exact finite-jet interpolation statement.

## Period constant
The theorem specifies a scalar from a rational connection, an integral intertwiner X and a normalized fundamental solution limit H_infinity. An independent numerical result requires the full X, the continuation branches, the Frobenius gauge and a real-structure convention. The displayed decimal is not independently verified by consistency of formulas. The proof of a global minimum requires a global sign or interval argument, including root and cusp charts and the interior; a high-precision evaluation at infinity alone is insufficient.
