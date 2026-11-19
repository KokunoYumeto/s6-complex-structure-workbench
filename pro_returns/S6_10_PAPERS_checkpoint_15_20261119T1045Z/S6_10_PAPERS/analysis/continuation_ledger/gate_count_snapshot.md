# Renewal gate snapshot

As of 2026-11-19T10:30:51.157594+00:00. Requested baseline: 19 November 2026, 03:37 UTC.

**75 distinct printed labels have all three explicit renewal receipts.** The restored baseline has zero receipts for this newly requested renewal. Historical reviews remain preserved separately.

| Paper | Printed labels | New printed proof rows | Complete proof receipts | Remaining proof rows | Partial proof scope | All three complete |
|---|---:|---:|---:|---:|---:|---:|
| I | 256 | 256 | 5 | 251 | 2 | 5 |
| II | 262 | 261 | 6 | 255 | 5 | 6 |
| III | 161 | 161 | 0 | 161 | 0 | 0 |
| IV | 257 | 225 | 0 | 225 | 42 | 0 |
| V | 79 | 79 | 49 | 30 | 5 | 48 |
| VI | 119 | 119 | 27 | 92 | 27 | 16 |
| **Total** | **1134** | **1101** | **87** | **1014** | **81** | **75** |

There are 1524 inventory rows and 1493 distinct receiving labels. The 1160 printed inventory rows represent 1134 distinct labels. Alias rows do not multiply completed work.

The 1014 remaining proof rows include 81 with a recorded bounded proof check and 933 with no continuation proof event or complete owner proof receipt. A complete proof receipt with another gate pending occurs on 12 printed rows. The latter rows are not counted as three-gate complete.

## Exact labels newly closed since the requested baseline

- **I:** `ari:C.2.1`, `ari:C.3.1`, `ari:C.3.2`, `ari:C.7.3`, `ari:C.7.4`.
- **II:** `cdp:st:A.1.1`, `cdp:st:A.1.2`, `cdp:st:A.2.1`, `cdp:st:A.2.4`, `cdp:st:A.3.1`, `cdp:st:A.3.3`.
- **III:** none.
- **IV:** none.
- **V:** `maps:src:F.1.1`, `maps:src:F.1.4`, `maps:src:F.2.1`, `maps:src:F.2.10`, `maps:src:F.2.11`, `maps:src:F.2.12`, `maps:src:F.2.13`, `maps:src:F.2.14`, `maps:src:F.2.15`, `maps:src:F.2.16`, `maps:src:F.2.2`, `maps:src:F.2.3`, `maps:src:F.2.37`, `maps:src:F.2.38`, `maps:src:F.2.5`, `maps:src:F.2.6`, `maps:src:F.2.7`, `maps:src:F.2.8`, `maps:src:F.2.9`, `maps:src:F.3.1`, `maps:src:F.3.2`, `maps:src:F.3.4`, `maps:src:F.3.5`, `maps:src:F.3.6`, `maps:src:F.3.7`, `maps:src:F.3.8`, `maps:src:F.3.9`, `maps:src:F.4.1`, `mapsaudit:order-four-torsion-transgression`, `night:P1.1`, `night:P1.10`, `night:P1.11`, `night:P1.12`, `night:P1.13`, `night:P1.17`, `night:P1.18`, `night:P1.2`, `night:P1.3`, `night:P1.5`, `night:P1.7`, `night:P1.8`, `night:P1.9`, `night:P1A.1`, `night:P1A.2`, `night:P1A.3`, `night:P1A.4`, `night:P1A.5`, `night:P1A.6`.
- **VI:** `cdp:st:C.2.CR.1`, `cdp:st:C.2.CR.4`, `cdp:st:C.2.CR.5`, `cdp:st:C.2.IRR.1`, `cdp:st:C.2.RAT.1`, `cdp:st:C.2.RAT.3`, `cdp:st:C.2.UN.13`, `cdp:st:C.2.UN.24`, `cdp:st:C.2.UN.32`, `cdp:st:C.2.UN.5`, `cdp:st:C.2.UN.74`, `cdp:st:C.2.UN.9`, `cdp:st:C.2.VII.1`, `cdp:st:C.2.VII.2`, `cdp:st:C.2.VII.3`, `cdp:st:C.2.VII.4`.

The exact owner text, file hashes and source-row mappings are in `completed_three_gate_rows.tsv` and `gate_count_snapshot.json`. Every unlisted gate remains pending.

## Compendium source verification and historical refutations

| Paper | Compendium-only labels | Source-verification queue | Explicit renewed source receipts | Historical false labels |
|---|---:|---:|---:|---:|
| I | 81 | 78 | 0 | 0 |
| II | 12 | 12 | 0 | 1 |
| III | 261 | 261 | 0 | 0 |
| IV | 1 | 1 | 0 | 32 |
| V | 4 | 4 | 0 | 0 |
| VI | 0 | 0 | 0 | 0 |

The 359 compendium-only labels are outside the new printed-proof queue. Their source dispositions remain in `compendium_source_verification.tsv`, including bounded older citations and any actual continuation source events. The 33 printed original false assertions retain their refutations and corrected-conclusion links; their original claims are not treated as proved conclusions.

The two printed known-input applications `night:P3F.19` and `night:P3F.20` remain in the receiving proof/application queue. Their external input credit does not close the source-specific local application gate.

## Mathematical status changes

- `ari:C.7.4`: open to proved under hypotheses H. Restored and freshly checked exact source implication with named BPSS Conjecture4.7 hypothesis H. H, including conductor361, and the unconditional question remain open. This is no proof of H.

Thirty-three corrected consequences now have separate receiving labels and explicit corollary proofs; the original thirty-three false assertions retain that status. These splits expose already established corrected conclusions and their dependencies. The eleven new cp36 source-Proved rows remain receiving-open. Statement/reference refinements and proof replacements that preserve a conclusion are reported through their exact receipts, rather than counted as a change from open to proved.

Receiving counterexample assertions whose old Refuted source tags referred to the rejected positive claims have their negative/corrected conclusions labelled proved. These exact assertion/status repairs are recorded separately in `receiving_status_metadata_changes.tsv`; they add no mathematical settlement or renewal receipt.

## Reading the remaining work

`remaining_new_printed_proofs.tsv` is the per-label routing list. `partial_printed_proof_scopes.tsv` retains every relevant current event outcome so a reviewer can identify the steps actually derived and the whole-proof gap. K116 retains its open receiving status and its remaining complete input-chain/topology review; its checked source/Cartier/theta coefficients alone do not close that row.

Counts use explicit owner receipts and recorded scopes. They do not count status-vocabulary reconciliation, incoming source proofs, layout repairs, metadata application or successful builds as renewed mathematical checking.

Refresh with `python code/continuation_ledger/gate_count_snapshot.py` after the event union and owner receipts are current. This report changes no canonical record or gate.
