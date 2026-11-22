# Prerelease derivation: 03IG / wbII:prop:all-pic-restriction

Checker: i_provenance_recovery. The exact safe statement, its cited statement/formula inputs and the supplement were read. No target proof or other checker's target reconstruction was opened. The dP6 normalization is bound by the same exact common-conventions statement used for 03IO; this is a geometric statement input, not a proof excerpt.

Fix the stated nowhere-zero section k of omega_X near W. Restriction and pullback are tensor functors. For every line bundle L the exact evaluation map

    eta^*((L^vee tensor omega_X)|_W)
       -> (eta^*i^*L)^vee,
    ell^vee tensor (a k) -> a ell^vee

is compatible with all transition functions and has inverse ell^vee -> ell^vee tensor k. It gives the specified eta^*A_L=r(L)^vee, where r=eta^*i^* is the homomorphism of Picard groups. The dual of a line bundle is trivial exactly when the bundle itself is trivial: dualizing any trivialization supplies the inverse implication. Hence the condition eta^*A_L=O for every L is equivalent, element by element, to r having only the identity value. This is the claimed r=0 criterion; it is exactly the trivial-pullback assumption of the cited conductor statement, with the identical line bundle and identical map eta.

For Pic^0, naturality of Chern classes gives c1(r(L))=eta^*i^*c1(L)=0. The normalization T=dP6 has H^1(T,O_T)=0 by the blowup-of-P2 calculation. The exponential sequence therefore makes c1:Pic(T)->H^2(T,Z) injective. Thus r(L)=O for every L in Pic^0(X). This independently supplies the last assertion while the 03IO target proof remains unopened. It uses no assumption that r vanishes on the other components of Pic(X).

Exact common-conventions input: `agents/ii_infra/S6_SERIES_PUBLISH_II_01AQ_common_setup.tex`, SHA256 `ec3a30d05b478a8bedb02d57d49b851f7f836cc21c5112f7f5ba787194c89ded`.
