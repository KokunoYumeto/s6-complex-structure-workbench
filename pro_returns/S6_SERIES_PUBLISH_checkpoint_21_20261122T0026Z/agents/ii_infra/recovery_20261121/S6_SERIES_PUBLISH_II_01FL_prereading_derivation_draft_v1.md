# 01FL / cdp:st:C4b: derivation before target-proof release

Status: complete argument on the smooth total-space domain required by the current C.1.3 input; original domain wording is separately unresolved. Target proof closed. Common analytic arguments are in S6_SERIES_PUBLISH_II_C4_prereading_common_arguments_v1.md.

1. Fix an arbitrary L in Pic(Y). Suppose all full fibres had H2(F,(T_Y L)|F)=0. The top-degree base-change map and Nakayama would give R2f_*(T_Y L)=0. For sufficiently large k, Leray, projection formula and Serre vanishing on P1 give H2(Y,T_Y L f^*O(k))=0. But current C.1.3 applies to the smooth compact Y, the nonzero effective Cartier divisor supplied by a fibre, and this actual twist; b3=0 makes its pointwise lower bound at least one. This contradiction proves the asserted existence of a full fibre for each L. This proof does not infer global nonvanishing merely from a normalization target.

2. Full-fibre adjunction, with the frame [t] of I/I^2, and Gorenstein Serre duality identify the dual of that nonzero H2 group with H0(F,Omega_Y^1|F tensor (K_Y L^-1)|F). Thus both groups in the statement are nonzero on the same full scheme-theoretic fibre.

3. For a general two-torus, the regular fibre Euler characteristic is zero. Poincare duality for the closed oriented smooth six-manifold, with b1=b2=b3=0, gives e(Y)=2. Additivity of Euler characteristic over the regular locus and the finitely many critical values gives the sum of reduced-support Euler contributions equal to two.

4. In the fibre class of C4a, a full smooth multiple support contributes zero, and current A.4.6 gives two for a rational-normalization irreducible normal-crossings fibre and zero for the Hopf/elliptic-ruled alternatives. Hence the number r of rational-normalization fibres satisfies 2r=2, so r=1.

5. Write eta:tildeS->Y for this unique normalization. For every L on Y, c1(K_Y^-1 L) is torsion because H2(Y,Z) is finite. Its pullback to a smooth rational surface is zero: H2(tildeS,Z) is torsion free. H1(tildeS,O)=0, and the exponential sequence makes a line with zero c1 trivial. Therefore eta^*(K_Y^-1 L) is isomorphic to O_tildeS. After choosing such a trivialization, Serre duality identifies
H2(tildeS,K_tildeS tensor eta^*(K_Y^-1 L))
with H0(tildeS,O)^dual=C. The dimension is one independently of that scalar choice. This identifies the actual line and cohomology map, rather than confusing the normalization target with the image of global tangent cohomology.

The original singular-domain reading has not been proved false and is not claimed checked by this draft.
