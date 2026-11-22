# Prerelease derivation: 03IO / wbII:prop:pic0-pullback

Checker: i_provenance_recovery. I read the safe statement and empty supplement. The target proof and historical check outcomes are unopened. The exact common-conventions statement supplied for 01AQ identifies W as the reduced distinguished fibre and eta:dP6->W as its normalization. This is statement-only input. The target's stipulated local canonical trivialization is retained.

Let T=dP6. This is the blowup of P2 at the three marked points. For a blowup of a smooth point, the direct image of O is O and its higher direct images vanish: the fibres are a point or P1 with H^1(O)=0, and the local two-chart blowup calculation gives the same vanishing and constants. Repeating the blowups and using Leray therefore gives H^1(T,O_T)=H^1(P2,O)=0. Equivalently, the standard smooth complete toric charts give the same calculation. Only the blowup argument is needed here.

The exponential sequence O_T -> O_T^* -> H^2(T,Z), with its factor 2*pi*i in the exponential, shows that the first Chern map Pic(T)->H^2(T,Z) is injective because H^1(T,O_T)=0. Every L in Pic^0(X) has c1(L)=0: the Chern class is constant on a connected family of line bundles and equals zero at the identity. Naturality of the exponential sequence under the actual maps i:W->X and eta:T->W gives

    c1(eta^*i^*L)=eta^*i^*c1(L)=0.

Injectivity on T proves eta^*i^*L is holomorphically trivial. Restrict the chosen nowhere-zero local section k of omega_X to W and pull it back. The tensor map

    eta^*((L^vee tensor omega_X)|_W)
      -> (eta^*i^*L)^vee,
    ell^vee tensor (a k) -> a ell^vee

is a specific line-bundle isomorphism. Its target is trivial by the preceding Chern argument, proving the stated conclusion. All uses of H^2 are on the normalization or on the actual Chern class of L; no value of H^2(X,Z) is assumed.

Exact common-conventions input: `agents/ii_infra/S6_SERIES_PUBLISH_II_01AQ_common_setup.tex`, SHA256 `ec3a30d05b478a8bedb02d57d49b851f7f836cc21c5112f7f5ba787194c89ded`.
