# Frozen-before-target derivation: 01F4 / cdp:st:C.3.1

I read the target statement and all supplied statement-only inputs, but not its target proof. The smooth ambient scope is necessary for the tangent/normal bundle and duality calculations below; the source calls Y a compact complex threefold without explicitly naming smoothness. As in 01FA, this must be made explicit before claiming completion of the printed wording. I derive the intended smooth statement here.

## Base and characteristic classes

The holomorphic algebraic reduction has connected fibres. Indeed, its Stein factorization has a normal finite intermediate curve, and the algebraic-reduction equality of meromorphic function fields makes the finite map to the normal base birational, hence an isomorphism. Pullback H^1(C;Q)→H^1(Y;Q) is therefore injective, by the degree-one beginning of the Leray sequence with f_*Q=Q. The vanishing b1(Y)=0 forces the compact Riemann surface C to have genus zero, so C is P1.

For a smooth fibre inclusion i:F→Y, the normal line bundle is F×T_cC and is holomorphically trivial. The actual tangent sequence is 0→T_F→i^*T_Y→O_F→0. Thus c1(K_F)=i^*c1(K_Y). The right side is zero in rational cohomology because b2(Y)=0. Poincare duality on the smooth compact oriented real six-manifold Y also gives H^4(Y;Q)=0. The same exact tangent sequence gives c2(T_F)=i^*c2(T_Y), which is rationally zero. Since the connected smooth compact surface F has H^4(F;Z)=Z, this top integral class is zero integrally. Surface Riemann–Roch then gives chi(F,O_F)=(c1(K_F)^2+c2(F))/12=0.

An exceptional curve of the first kind would be a smooth rational curve E with E^2=-1. Adjunction on F gives K_F.E=-1, contradicting the rationally trivial first Chern class. Thus each smooth fibre is minimal.

## Very general Kodaira dimension

For each positive integer m, consider the coherent direct image of the relative pluricanonical bundle K_{Y/C}^m on the projective curve C. Away from a proper analytic subset it has fibre H^0(F,K_F^m). Twisting the direct image by O_C(n) for sufficiently large n makes it globally generated. Two independent fibrewise pluricanonical sections would therefore arise as restrictions of global sections of the same line bundle K_{Y/C}^m tensor f^*O_C(n). Their ratio would be a meromorphic function on Y whose restriction to a general fibre is nonconstant. Such a function cannot be pulled back from C, contrary to the defining equality of meromorphic function fields for the algebraic reduction.

Consequently the generic m-th plurigenus is at most one for every m. Remove the union of the proper jumping sets over all positive integers m. At a point outside this countable union, all plurigenera are at most one. The characterization of Kodaira dimension by growth of plurigenera gives kappa(F)≤0 for this very general fibre. This argument uses the actual relative line bundle and global sections on the base; it does not identify algebraic dimension of a fibre with that of the total space.

## Classification and the stated inputs

The known classification input has been opened directly: Peters, Compact Complex Surfaces, Theorem3.1, printedp10, lists the minimal surface classes; the invariant identities are on printedpp5–6. Teleman's author PDF, printedpp1–2, gives the definitions of Kodaira surfaces and the direct classVII,b2=0 conclusion Hopf/Inoue. BBK arXiv1709.00062v3, Theorem1,p1, has also been opened, with its actual finite-etale-cover conclusion recorded separately rather than silently identified with the stronger direct statement. The primary-source receipt is agents/ii_infra/primary_inputs/S6_SERIES_PUBLISH_C31_classification_primary_receipt.json, SHA256 a89b7cf7a0aa98b59bf0907a82d77737a93c79456560ed110e80d37bbf4b4822.

For the already minimal very general F with kappa≤0, rational and ruled surfaces are excluded because the canonical class has nonzero pairing with a line in P2 or with the rational ruling fibre (respectively -3 and -2), whereas c1(K_F) is rationally zero. In the Kodaira-dimension-zero classes, K3 and Enriques surfaces have Euler numbers24 and12, contradicting c2(F)=0. The remaining dimension-zero classes are complex two-tori, bielliptic surfaces, and primary/secondary Kodaira surfaces. In classVII, b1=1 and e(F)=0 give b2=0, so the opened direct classification gives Hopf or Inoue surfaces. The Hopf class includes primary and secondary quotients. This yields exactly the preliminary list stated, all with Euler number zero.

The stronger final list in the last part of the target statement is a composition of supplied result statements: C.3.7 excludes bielliptic fibres; C.3.8 forces very general Hopf algebraic dimension zero; C.3.9/C.3.10 exclude both Kodaira classes; C.3.12 excludes Inoue. C.3.6 supplies both Hopf occurrences and D.2.7 supplies a torus occurrence. These are treated here as the allowed named inputs, not as newly verified proofs. Their checks have their own owners. The actual hypotheses of each exclusion match the stated smooth algebraic-reduction setting. The resulting final very general types are the two-torus and the two Hopf classes of algebraic dimension zero.

The comparison must confirm the source's characteristic-class maps, plurigenus argument, exact classification locators, and explicit smoothness scope. No target proof has been opened, and this file adds no event.
