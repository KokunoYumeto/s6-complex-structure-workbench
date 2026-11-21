# Prerelease derivation: 03IJ / wbII:prop:cartier-duality-absolute

Checker: i_provenance_recovery. The exact safe target statement and empty supplement were read. Neither the target proof nor any other checker's target reconstruction was opened. I also read the primary absolute analytic duality input: Ramis–Ruget, Complexe dualisant et théorèmes de dualité en géométrie analytique complexe, Publ. Math. IHES 38 (1970), Theorem 1 with its complete proof, pp.81–82; primary URL https://www.numdam.org/item/PMIHES_1970__38__77_0.pdf. The following records the exact normal-line factor and the coordinate choice needed for the scalar-valued formulation.

The local regular ring of the smooth threefold has a nonzerodivisor h defining W. The quotient is a Cohen–Macaulay Gorenstein ring of dimension two. The local resolution [O_X(-W)->O_X], dualized into omega_X, has its sole sheaf Ext in degree one, equal to omega_X(W)|_W. These local maps glue, including a nonreduced h, to the dualizing sheaf omega_W. Therefore the absolute analytic dualizing complex of the compact surface W is omega_W[2]. This is the exact Cartier-adjunction calculation; it does not require a compact ambient X.

The primary absolute analytic duality theorem on the compact space W pairs H^2(W,E|_W) with H^0(W,(E|_W)^vee tensor omega_W). Its trace and evaluation maps are functorial. Compactness gives finite-dimensional coherent cohomology and the Hausdorff topologies, so its perfect duality on separated cohomology is the ordinary finite-dimensional perfect pairing here. Thus

    H^2(W,E|_W)^vee = H^0(W,E^vee|_W tensor omega_W).

Let c be the base point whose full scheme-theoretic fibre is W. Shrink B to a coordinate disc about c and X to its inverse image; this changes none of the sheaves or cohomology on W. Choose a coordinate t with t(c)=0. The function f^*t defines W, hence the section 1/(f^*t) trivializes O_X(W) on this neighbourhood. Tensoring this generator with omega_X gives a specified isomorphism omega_X|_W -> omega_W, and composing its induced map on H^0 with the preceding trace pairing gives exactly the scalar-valued perfect pairing in the target. It is functorial in the bundle E and its homomorphisms for this fixed choice.

The coordinate-independent factor is explicit. There is a canonical identification O_B(c)|_c=T_cB: the principal part 1/t corresponds to partial_t. Therefore

    omega_W = omega_X|_W tensor T_cB,
    H^2(W,E|_W)^vee
       = H^0(W,E^vee|_W tensor omega_X|_W) tensor T_cB.

Replacing t by u=a t+O(t^2) changes 1/(f^*t) to a^{-1}/(f^*t) on W, and partial_t to partial_u=a^{-1}partial_t. These are the exact matching transition maps. The scalar pairing without the normal-line factor consequently uses a chosen nonzero vector in T_cB; it scales by a^{-1} under this coordinate change. The target's existence of a pairing functorial in E is proved. A claim that this particular scalar pairing were canonical under arbitrary base-coordinate changes would require retaining the T_cB factor or specifying the choice. I will inspect the printed proof only after freezing this derivation and make that scope explicit in the comparison. This is a scope qualification, not an assumption of a missing trivialization.

Exact primary PDF: `agents/ii_checks_provenance/recovery_20261121T2000Z/primary_inputs/Ramis_Ruget_1970.pdf`, SHA256 `283dbde1ce597b2cdd7ae4110e3f0f991aeee23a6086568cc10e6e5e720c674b`; receipt `agents/ii_checks_provenance/recovery_20261121T2000Z/primary_inputs/Ramis_Ruget_1970_receipt.json`, SHA256 `01cc336d13d3d83fc2c4b03155393ce722f91c576cb0652ea4b0b6eb5a582bc9`.
