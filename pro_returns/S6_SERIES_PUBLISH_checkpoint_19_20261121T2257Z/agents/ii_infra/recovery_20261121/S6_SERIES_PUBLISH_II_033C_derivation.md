# 033C — push:src:E.2.4 — derivation before opening the target proof

Checker: GPT-6 Astra (OpenAI), ChatGPT Pro mode | restore_build.
Only the statement/input packet and its immutable cited-input supplement have been read. The target printed proof remains closed. The relevant allowed input statements are push:src:E.2.23 and push:src:E.2.24. Their proofs have not been opened. Metadata inspection shows that E.2.23 cites E.2.22 rather than using E.2.4 as a proof input, so the corollary-to-theorem reference is not being treated as a circular deduction.

## Proper smooth families and chains

Let pi:X->B be the proper smooth holomorphic family in the target statement, and let b_0 have a constructed sphere fibre with ordered coprime multiplicities (3k,4l). For a possibly nonreduced analytic base, form the precise base-change map

    X_redbase = X x_B B_red -> B_red.

Reduction B_red has the same points and topology as B, hence is connected. Properness and smoothness are stable under this base change. At a point b, both fibre spaces are the identical fibre product with Spec(C), so every complex fibre is unchanged. The statement E.2.23 applies to this reduced-base family and asserts that every fibre is a constructed member with the same ordered pair. Transporting this statement along the equality of point fibres proves the assertion for B itself. No claim that the two total complex spaces are isomorphic is required or made.

For a finite chain of connected families, apply the preceding conclusion to its first family. The common member joining the first and second families has the first pair, so the same argument fixes that pair throughout the second family. Induction over the finite number of joins fixes the pair throughout the chain. Thus deformation equivalence by these chains implies equality of the ordered pairs.

For the converse, E.2.23 explicitly supplies deformation equivalence of two constructed members having the same ordered pair. This is a permitted input conclusion of the theorem to which the target is a corollary. This check does not substitute local miniversality alone for global connectedness of a parameter domain, nor does it silently identify two different discrete logarithmic data sets.

## Continuous families

For a fixed pair, E.2.24 states that I_(k,l) is open and closed in the C-infinity space I(S^6) of smooth integrable almost-complex structures. Given a continuous map J:P->I(S^6) from a connected topological parameter space P, its inverse image of I_(k,l) is open and closed. When one parameter has a constructed member with this pair, that inverse image is nonempty, so connectedness makes it all of P. Distinct constructed ordered pairs have disjoint such loci, as follows already from the ordered multiplicities of the same intrinsic fibration in E.2.23. Consequently the family cannot contain two different pairs. No regularity or local path connectedness of P is needed.

All conclusions of the target have now been obtained from the explicitly permitted input statements and elementary base-change, induction, and connectedness arguments. This is a check of the corollary; the deeper closure and propagation theorems remain separate required owners. No program or numerical approximation is involved.

## Immutable evidence bindings before freeze

- agents/ii_infra/recovery_20261121/S6_SERIES_PUBLISH_II_SX_033C_033O_primary_inputs.json — SHA256 `343d8f24b8129b9ba403c472618454a47f998cfa2f288c3f519c5864ee62a6ce`.
- agents/ii_infra/recovery_20261121/S6_SERIES_PUBLISH_II_citation_search_exposure_2059.json — SHA256 `ce712d0d916420f6fed07b91273b88e69120efc25452ce8ec254d2bd9d1c04c9`.
- agents/ii_infra/recovery_20261121/S6_SERIES_PUBLISH_II_citation_search_exposure_2059.txt — SHA256 `5f8128705845bb67c6374f42582d5297d774a9a8ed450ccea04370a3517c8e44`.
