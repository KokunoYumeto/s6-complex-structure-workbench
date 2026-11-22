# Prerelease derivation: 03IY / wbII:thm:cartier-duality

Checker: i_provenance_recovery. The exact safe statement and empty supplement were read before writing this proof. No target proof, historical result or another checker's target reconstruction was opened. The related general duality background and Paper I exposure are disclosed. Ramis–Ruget's primary absolute-duality article, Theorem 1 and its proof on pp.81–82, was also read as a general input; this derivation can use the ordinary compact-manifold form of Serre duality alone.

Write i:W->X, F=E|_W, and let s be the canonical section of O_X(W) defining the effective Cartier divisor. The exact locally free resolution on X is

    0 -> E(-W) --s--> E -> i_*F -> 0.

It remains exact for a nonreduced divisor because its local equation is a nonzerodivisor and E is locally free. Apply sheaf Hom(-,omega_X). The resulting two-term complex is

    E^vee tensor omega_X --s--> E^vee tensor omega_X(W)

in Ext degrees 0,1. Its first map is injective for the same nonzerodivisor reason. Its cokernel is i_*(F^vee tensor (omega_X(W)|_W)), by the tensor-quotient map. Hence sheaf Ext^j(i_*F,omega_X) vanishes unless j=1, and sheaf Ext^1 equals that displayed cokernel. This identifies omega_W=(omega_X tensor O_X(W))|_W, including its exact transition: replacing a defining equation h by u h changes the generator of the conormal by u and its dual by u^{-1}, which is precisely the O(W) factor.

Serre duality for the bounded locally free resolution on the compact smooth threefold pairs H^q(X,i_*F) with Ext^{3-q}_X(i_*F,omega_X). One can form this pairing directly by the evaluation of the resolution and its dual, followed by the trace H^3(X,omega_X)->C. Ordinary Serre pairings on E and E(-W) give a quasi-isomorphism between the dual cohomology complex and this derived Hom complex; thus the pairing is perfect and functorial in E. The local-to-global Ext spectral sequence has the single nonzero row j=1 and gives

    Ext^{3-q}_X(i_*F,omega_X)
       = H^{2-q}(W,F^vee tensor omega_W).

The closed embedding i has exact direct image, and its cohomology equals cohomology on W. These maps give the stated perfect pairings for q=0,1,2. For q=3 the dual group is Hom_X(i_*F,omega_X)=0: locally a section in the image would be annihilated by the nonzerodivisor h in the locally free target. For q>3 the cohomology vanishes on the threefold; this also follows from its Dolbeault resolution with the two-term locally free resolution and the same duality complex. Thus H^q(W,F)=0 for q>2. At no point was W replaced by its reduction or normalization.

Exact primary PDF: `agents/ii_checks_provenance/recovery_20261121T2000Z/primary_inputs/Ramis_Ruget_1970.pdf`, SHA256 `283dbde1ce597b2cdd7ae4110e3f0f991aeee23a6086568cc10e6e5e720c674b`; receipt `agents/ii_checks_provenance/recovery_20261121T2000Z/primary_inputs/Ramis_Ruget_1970_receipt.json`, SHA256 `01cc336d13d3d83fc2c4b03155393ce722f91c576cb0652ea4b0b6eb5a582bc9`.
