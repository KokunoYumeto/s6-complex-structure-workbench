# 03IZ: wbII:thm:corrected-cdp-fibrewise

Author: i_provenance_recovery. Written 2026-11-21T21:36:41.214737+00:00.

Scope: independent derivation of the exact named target from the safe statement and cited inputs, before opening its target printed proof. Related Paper I and previously released/checked Paper II results are declared inputs, not claimed to be unseen. No target historical check record has been consulted.

Work in the clarified smooth J0 setting. The nonconstant proper map from the smooth threefold to the smooth curve is flat and its full fibres W_c are pure Cartier surfaces; each is reduced by the displayed additional assumption. For a fixed c set V=Omega_X|W_c, T=ker(Omega_W_c->j_*Omega_reg), Q=Omega_W_c/T, N*=I/I^2, and K=ker(V->Q). The IF quotient map [omega]->omega restricted to the smooth locus identifies Q with the sheaf denoted tildeOmega. A.1.1 gives 0->N*->K->T->0 and 0->K->V->Q->0, with precisely the displayed connecting map delta_c after tensoring by A_c.

The hypotheses H0(N* tensor A_c)=H0(Q tensor A_c)=0 identify H0(V tensor A_c) with ker(delta_c), by the map s->rho(s). Injectivity of delta_c makes this group zero. Cartier adjunction gives omega_W_c=omega_X|W_c tensor T_cC; choose a nonzero vector in that one-dimensional factor. Serre duality identifies H2(W_c,(T_X tensor L)|W_c)^vee with H0(V tensor A_c), hence the full-fibre H2 vanishes for every c.

The checked DV top-degree base-change isomorphism identifies (R2 f_*(T_X tensor L))_c tensor C(c) with that zero space. Proper coherence and local Nakayama give zero stalk at every c; therefore R2 f_*(T_X tensor L)=0. Apply DT, whose exact twisting argument supplies a line bundle with global H2=0, then J0 to obtain the displayed generic global vanishings and both Euler inequalities. All quotients, kernels, adjunction normal-line factors and fibre maps are specified. No extra normality assumption or numerical test is substituted for a map.

## Bound inputs

- `agents/ii_infra/statement_packets_v2/S6_SERIES_PUBLISH_II_03IZ_statement_inputs.tex` — SHA256 `ee9f63f0733bb6754d384be6559199e8f1784c5945832734a1ed273ff8138b41`.
- `agents/ii_infra/statement_supplements_v1/S6_SERIES_PUBLISH_II_03IZ_cited_input_supplement.tex` — SHA256 `abd46b0beee125036c490abb09c738fef4586c7c17d2cdd08a96bc623c6d29cb`.
- `agents/ii_checks_provenance/recovery_20261121T2000Z/S6_SERIES_PUBLISH_II_global_vanishing_scope_inputs.tex` — SHA256 `5cc7f587f255d98fd1e45c2f88a033314bf4eecd4dac4cfcebb0e87dd93271f1`.
- `agents/ii_infra/S6_SERIES_PUBLISH_II_01AQ_setup_supplement.tex` — SHA256 `c4aec734c1468d2b6d9b397e5bd9170b494d4e57823d9cee550d0b2e45c16751`.
- `records/S6_SERIES_PUBLISH_II_analytic_primary_inputs_01/Douady1974.pdf` — SHA256 `4fd29bf08b01c94d22c7fb4bcac67d3dd31b0754ea20d210e8c897dc3bb7cbbd`.
- `agents/ii_checks_provenance/recovery_20261121T2000Z/primary_inputs/Ramis_Ruget_1970.pdf` — SHA256 `283dbde1ce597b2cdd7ae4110e3f0f991aeee23a6086568cc10e6e5e720c674b`.
