# 01SX — inv:E2.4 — derivation before opening the target proof

Checker: GPT-6 Astra (OpenAI), ChatGPT Pro mode | restore_build.
The target printed proof is closed. I read its statement/input packet, including only the statements inv:E2.2 and cdp:st:E15. No proof of either input was opened in this check. The bibliography-key search exposed no sentence of the target proof.

## Exact inputs and deduction

The attached primary comb manuscript's theorem labelled `t:main` gives, for every integer m at least 12, a holomorphic fibration on a compact complex manifold X_m and a diffeomorphism Phi_m:X_0 -> X_m preserving the fibration. The attached AC manuscript's main theorem, printed page 4, item (4), states that X_0 is diffeomorphic to S^6. The composition Phi_m with that diffeomorphism is an explicit identification of the underlying differentiable manifold on which the complex structure of X_m is transported. No identification of its holomorphic structure with X_0 is asserted.

The permitted input cdp:st:E15 states the exact tangent cohomology of each such positive comb:

    (h^0(T_Xm),h^1(T_Xm),h^2(T_Xm),h^3(T_Xm))
       = (2m+1,8m+1,6m+1,0).

Choose the actual allowed integer m=12. Then h^0(X_12,T_X12)=25. These are 25 linearly independent global holomorphic vector fields on a complex manifold whose underlying differentiable manifold is S^6, and 25>2. This single concrete member contradicts the quantified bound h^0(T)<=2 for every complex structure on S^6. The input's assertion for all m>=12 supplies infinitely many further numerical counterexamples, but one is sufficient. This derivation checks the stated corollary from its cited theorem, and does not claim to reprove E15.

## Source attribution checked directly

The attached primary HKP preprint contains the corollary labelled Intro:Cor2: a complex structure X on S^6 carries at most two linearly independent holomorphic vector fields, h^0(TX)<=2. This is the exact quantified bound being tested, not a bound stated only for the original AC member.

The attached AC PDF, printed page 4, Remark 1.2, cites HKP Corollary 1.3 as the general constraint h^0(TX)=1<=2 for the original member. Printed page 83, Remark 9.26, explicitly restates the bound h^0(TX)<=2 for any complex structure on S^6. The present counterexample concerns that universal assertion. The independently stated equality h^0(T_X0)=1 for the original AC member is retained and is not contradicted by the new members.

There is no numerical approximation, finite search, target computation, or unstated deformation-invariance assumption in this deduction. The integer substitution and inequality are exact. This file is to be frozen before release and full comparison of inv:E2.4.

## Immutable evidence bindings before freeze

- agents/ii_infra/recovery_20261121/S6_SERIES_PUBLISH_II_SX_033C_033O_primary_inputs.json — SHA256 `343d8f24b8129b9ba403c472618454a47f998cfa2f288c3f519c5864ee62a6ce`.
- agents/ii_infra/recovery_20261121/S6_SERIES_PUBLISH_II_citation_search_exposure_2059.json — SHA256 `ce712d0d916420f6fed07b91273b88e69120efc25452ce8ec254d2bd9d1c04c9`.
- agents/ii_infra/recovery_20261121/S6_SERIES_PUBLISH_II_citation_search_exposure_2059.txt — SHA256 `5f8128705845bb67c6374f42582d5297d774a9a8ed450ccea04370a3517c8e44`.
