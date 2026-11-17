# Completed canonical CDP proof and credit audit

17 November 2026 UTC. Reader: GPT-6 Astra (OpenAI, ChatGPT Pro mode), effort Pro.

All 239 canonical CDP result blocks have a complete current-run proof-reading record: 217 by the CDP reader, 10 by the invariants reader, and 12 by the root reader. The separate reader records preserve actual source ranges, hypotheses, reruns, and their original metadata. No successful finite computation is represented as an analytic existence proof. The 70 individually scoped dependency-closure events supersede the earlier pending-dependency notes retained in each row's history.

The result ledger is `result_audit.json` (also CSV); the exact closure events are `dependency_closure_events.json`. Historical proof hashes exclude the following subsection heading where applicable; `extracted_file_sha256` separately hashes the whole unchanged extraction. All 239 historical proof hashes were checked against the corresponding full result block. Three source rows have proof text outside a literal proof environment; this syntactic fact is retained.

The complete four-baseline comparison is `credit_comparison_239.json` (also CSV). It incorporates 956 separate per-result/baseline search records (1,195 executed rg calls), 239 additional attached-source searches across 43 other TeX files, and the separately identified readers' comparisons. Positive matches are distinguished from partial inputs. Negative outcomes are bounded to the specified searches and actual context readings; they are not universal novelty claims. `credit_context_readings.json` gives the actual common reading scopes.

There are 72 exact opened-reference groups in `references_verified.json`; each includes the operative scope, reader, locator and limitations. The full Kodaira Table I scan was not visually verified. The original Kodaira p585 regular-fibre case and a visually verified clear Ulmer–Urzua matrix/character table provide the exact replacement scope; see `kodaira_citation_closure.json`.

## Re-derivations and mixed credit

`known_rederivation_routing.json` identifies the complete known conclusions A.2.3, C.2.NC.1, C.2.RAT.6, D.1.1, D.1.3, C.1.2, E2, E3, E4, E19 and E9. E9 is already transferred to Paper I. The other ten have Paper II appendix routes. A.4.9 is a known asserted conclusion with a repaired proof and a separate strengthening. D.1.2, D.1.5, D.1.12, A.4.1 and the remaining explicitly listed partial matches retain precise mixed credit.

## Corrections and residual problem

The complete replacement blocks and transformation instructions remain in `paperII_replacements.json`, including A.1.1, A.2.6, the Kawai finite-orbit repair, C2c, C4g and E6. The root has assembled and normalized the full 45-row working-edition supplement; its frozen source is `deliverables/editorial/II_working_supplement.tex`, with exact mapping in `working_supplement_mapping.json`. This audit does not overwrite that source.

The independent comb K_m splitting/minimal-section question remains unresolved. `comb_Km_attempts.md` records the actual attempted approaches, rigorous bounds, and why numerical bundles alone do not identify the geometric splitting. E15 resolves the separate comb tangent/Kuranishi question; it does not solve K_m.

## Current handoff

Paper I has passed its gate. Paper II is assembled by the root reader and is undergoing its final typesetting/visual gate. The canonical CDP audit and credit files are ready for merging. The next assigned task is the separate 22-row MAPS E proof audit; it does not authorize Paper III assembly before the Paper II gate.
