# Literature comparison: CDP98/CDP20 and the full S6 manuscript

## Disposition

The formal conclusions are incompatible. CDP20 Theorem 2.2(c) prints `c_3(X) <= 0` under `H^1(X,Z)=H^2(X,Z)=0`, `a(X)=1`, and holomorphic algebraic reduction. CDP20 Corollary 2.3 prints `a(X)=0` for a compact complex threefold homeomorphic to `S^6`. The manuscript claims those hypotheses together with `c_3(X)=2` and `a(X)=1`.

The complete manuscript, unlike the earlier packet-only material, gives a proposed mathematical reason the printed proof does not apply.

## Place 1: nonnormal cotangent reduction

Source: manuscript Section 10.2--10.4, source PDF pp. 86--90, canonical-source lines approximately 4480--4667.

For a reduced normal-crossing fibre `S` in a smooth threefold, the defining differential `dg|_S` is nonzero away from the conductor and vanishes on the conductor. If a line bundle `A` pulls back trivially to the normalization, then the pair `(eta^*dg tensor e, 0)` descends through the normalization/conductor Mayer--Vietoris sequence to a nonzero ambient cotangent section

`H^0(S, Omega_X^1|_S tensor A)`.

Its image in `Omega_S^1 tensor A` is conductor-supported torsion, so it disappears in the torsion-free quotient `tilde Omega_S^1 tensor A`. Thus vanishing of the latter does not imply vanishing of the ambient cotangent group at a nonnormal fibre. The local calculation is coherent and directly targets the reduction quoted from CDP20 Section 7.

For the manuscript's fibre `W`, pullbacks of line bundles from `X` to the normalization `dP_6` are trivial. Analytic Serre duality therefore yields nonzero top cohomology on `W`; top-degree base change is then used to conclude `R^2 f_*(T_X tensor L) != 0` for every `L`.

Audit status: no local algebraic defect found. The exact analytic duality and base-change theorems should be stated with complete hypotheses and independently checked by specialists.

## Place 2: monodromy coinvariants

Source: manuscript Section 10.5, source PDF pp. 90--94.

For a split exact sequence `1 -> K -> G -> Q -> 1`, the correct formula is

`G^ab = Q^ab direct_sum (K^ab)_Q`,

not `Q^ab direct_sum K^ab` unless the action is trivial. The manuscript's unipotent torus monodromy has coinvariant rank one rather than fibre first-Betti rank four. The group-theoretic correction is correct. It changes the rank count used in the cited CDP98/CDP20 route.

The manuscript separately proves by a countability argument that a line bundle non-torsion on every fibre exists, so this monodromy gap can be repaired for the example. The nonnormal cotangent reduction cannot be repaired in the same manner.

## Referee conclusion

The prior packet-only rejection rationale is superseded. CDP20 cannot be invoked as an unexamined black-box refutation after Section 10 is read. Conversely, this review does not establish that the published theorem is false: acceptance of the manuscript would require independent adjudication of the construction and the Section 10 counterexample mechanism.

## Primary references

Campana, F., Demailly, J.-P., & Peternell, T. (1998). The algebraic dimension of compact complex threefolds with vanishing second Betti number. *Compositio Mathematica, 112*, 77--91.

Campana, F., Demailly, J.-P., & Peternell, T. (2020). Corrigendum: The algebraic dimension of compact complex threefolds with vanishing second Betti number. *Compositio Mathematica, 156*, 679--696.
