# Exact-check rerun — 28 August 2026

All archived programs were rerun from fresh temporary copies so that retained
review evidence in this project was not rewritten. The six programs completed
**127/127 exact assertions**:

| Evidence stream | Command within its retained directory | Result |
|---|---|---:|
| Reviewer A full audit | `python audit/exact_checks.py` | 28/28 |
| Reviewer A corrective audit | `python checks/codex_integration_checks.py` | 14/14 |
| Reviewer B full audit | `python scripts/reproduce_core_checks.py --json evidence/codex_rerun.json --text evidence/codex_rerun.txt` | 38/38 |
| Reviewer B corrective audit | `python checks/reproduce_integration_checks.py` | 17/17 |
| Reviewer B candidate validation | `python scripts/check_exact_identities.py` | 8/8 |
| Superseded packet-06 review | `python computational_checks/verify_packet06.py` | 22/22 |

Reviewer B's candidate wrapper also passed under Git Bash: eight exact
identities, its sixteen-claim fail-closed ledger, the seven-page report gate,
required-text extraction, and replacement-character rejection all passed. The
Reviewer B full-audit program was rerun again in a temporary environment with
its specified SymPy 1.14.0; it again returned 38/38.

The Reviewer A corrective script assumes an `audit/` output directory that is
not retained in its curated subtree. Creating that empty directory in the
temporary copy allowed the unchanged program to run; this was an execution
precondition, not a mathematical patch.

## Retained-package integrity boundary

Passing arithmetic does not imply that every historical package ledger still
describes the curated subset retained here. A fresh, non-mutating manifest
audit gave:

| Retained ledger | Verified rows |
|---|---:|
| Reviewer A `bundle_manifest.json` | 24/24 |
| Reviewer A `MANIFEST.sha256` | 22/25 |
| Reviewer B full `MANIFEST.txt` path inventory | 25/25 paths present |
| Reviewer B candidate original-archive checksum ledger | 12/22 |
| Packet-06 `SHA256SUMS.txt` | 21/21 |
| Packet-06 `bundle_manifest.json` | 20/20 |
| Reviewer B corrective source ledger | 28/169 |
| Reviewer B corrective integrated ledger | 46/259 |
| Reviewer B corrective update ledger | 14/86 |
| Reviewer B corrective progress-record hash | 0/1 |

The incomplete rows are not silently reported as corruption of the current
canonical release. They arise because several frozen ledgers describe the
larger source archives from which these public evidence subtrees were curated:
listed files are absent, and a few public README/verification files changed
during consolidation. Reviewer A's JSON bundle manifest and both packet-06
manifests are complete for their retained scopes. Reviewer B full retains all
25 paths in its inventory but not the separately referenced checksum file.

The canonical release's own generated manifest and SHA-256 ledger cover every
retained file and are independently checked by
`supporting_materials/reproducibility/deterministic_release_roundtrip.py`.
