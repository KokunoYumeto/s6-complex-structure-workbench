# Derivation before target proof: 01AQ

Owner `cdp:st:A.4.1`; checker `i_provenance`. The exact target and A.1.1/A.1.2
statements are read, together with the safe common setup and root's exact
01AQ setup supplement. The latter binds the standard (3,4,infinity)
six-sphere member X to the imported III maps:src:B.5.2 statement. No target
proof or previous check has been read. Prior Paper I construction/topology
exposure is explicitly disclosed. Arbitrary finite-affine twists are not
included in the scope certified here.

The supplied integral homology statement has H1(X,Z)=H2(X,Z)=0. Universal
coefficients therefore give H2(X,Z)=0 in cohomological degree two as well.
For every holomorphic line B on X, c1(B)=0, and naturality of the Chern class
gives c1(eta^*(B|W))=0 on the normalization T=dP6. This rational surface is
the blowup of P2 at three points; H1(T,O_T)=H2(T,O_T)=0, for example by the
blowup direct image of O and the P2 groups. The exponential sequence thus
identifies Pic(T) with H2(T,Z). Consequently eta^*(B|W) is holomorphically
trivial. This is the exact restriction/Chern/exponential map, not an
assumption that every line on W itself is trivial.

The full reduced fibre W has conormal N*=O_W: a local coordinate at p0 on
the smooth base supplies its global defining function on a neighbourhood.
The normal-crossings formula A.1.2 identifies K with eta_*O_T by the map
(a_i) -> sum_i a_i product_(j!=i)x_j dx_i in a crossing chart. Tensoring by
B|W and projection formula give
H0(W,K tensor B|W)=H0(T,eta^*(B|W)), a one-dimensional vector space.

The natural pullback of Kahler differentials to the smooth normalization
kills exactly the generically zero torsion in its kernel, so it injects the
torsion-free quotient Q into eta_*Omega_T^1. After tensoring with B|W, the
normalization line is trivial and H0(T,Omega_T^1)=0 by rationality. Therefore
H0(W,Q tensor B|W)=0. The exact filtration 0->K->Omega_X^1|W->Q->0 gives
the actual isomorphism from the preceding one-dimensional section space to
H0(W,Omega_X^1|W tensor B|W). A choice of a nonzero normalized line frame
identifies it with C. This proves both displayed conclusions for every B.

Finally B=K_X tensor L^-1 ranges over all of Pic(X) when L does, because
inversion followed by tensoring with fixed K_X is a bijection. This gives
the target's initial A formulation through this explicit Picard map.
The source presentation should name the standard six-sphere family in the
statement; the proof here certifies exactly that supplied topological scope.

No numerical computation is involved. All packet hashes and source witnesses
are retained in the safe setup receipts; target release follows this freeze.
