# 03IA: wbII:lem:generic-endpoints

Author: i_provenance_recovery. Written 2026-11-21T21:36:41.214737+00:00.

Scope: independent derivation of the exact named target from the safe statement and cited inputs, before opening its target printed proof. Related Paper I and previously released/checked Paper II results are declared inputs, not claimed to be unseen. No target historical check record has been consulted.

Use the exact parameter space P and its supplied Poincare line bundle. Projection Y x P -> P is proper, and the locally free family B tensor Poincare is flat over P. In a neighbourhood of each parameter, the finite-degree free-complex realization of proper flat cohomology computes fibre cohomology. The dimension formula dim H^q = dim K^q-rank d^(q-1)-rank d^q expresses the jumping loci by holomorphic minors. Hence Z0={P':H0(Y,B tensor P') nonzero} is closed analytic. The given point P0 has H0=0, so Z0 is proper. Since P is irreducible and reduced, its open complement U0 is dense.

Apply the same construction to B^vee tensor omega_Y. Its nonzero-H0 jumping locus Zdual is proper because Q0 is a zero-section point supplied in the statement. Inversion inv:P->P is the restriction of the holomorphic line-bundle dualization map, preserves P by hypothesis, and satisfies inv composed with inv=id. Thus Un=inv(P minus Zdual) is dense open. The intersection U0 intersect Un is dense open in the irreducible parameter space. For P' in that intersection, H0(Y,B tensor P')=0 and H0(Y,B^vee tensor omega_Y tensor (P')^vee)=0. The functorial compact-manifold Serre pairing identifies the latter with H^n(Y,B tensor P')^vee, hence gives the asserted endpoint vanishings.

The negative divisor powers are used through the exact two zero-section points already assumed. No assertion that an arbitrary subspace P contains all divisor powers is made. This proves the statement's precise parameter-space form.

## Bound inputs

- `agents/ii_infra/statement_packets_v2/S6_SERIES_PUBLISH_II_03IA_statement_inputs.tex` — SHA256 `da6bef92220ea47d01c90edc40a788183bbd9e6c517af2dff1890e95f9673e7e`.
- `agents/ii_infra/statement_supplements_v1/S6_SERIES_PUBLISH_II_03IA_cited_input_supplement.tex` — SHA256 `29399cb28ff626c6ed05ee3e060c2ba98b03e1eef8e45af3178f7b08dbe4a35d`.
- `agents/ii_checks_provenance/recovery_20261121T2000Z/S6_SERIES_PUBLISH_II_global_vanishing_scope_inputs.tex` — SHA256 `5cc7f587f255d98fd1e45c2f88a033314bf4eecd4dac4cfcebb0e87dd93271f1`.
- `agents/ii_infra/S6_SERIES_PUBLISH_II_01AQ_setup_supplement.tex` — SHA256 `c4aec734c1468d2b6d9b397e5bd9170b494d4e57823d9cee550d0b2e45c16751`.
- `records/S6_SERIES_PUBLISH_II_analytic_primary_inputs_01/Douady1974.pdf` — SHA256 `4fd29bf08b01c94d22c7fb4bcac67d3dd31b0754ea20d210e8c897dc3bb7cbbd`.
- `agents/ii_checks_provenance/recovery_20261121T2000Z/primary_inputs/Ramis_Ruget_1970.pdf` — SHA256 `283dbde1ce597b2cdd7ae4110e3f0f991aeee23a6086568cc10e6e5e720c674b`.
