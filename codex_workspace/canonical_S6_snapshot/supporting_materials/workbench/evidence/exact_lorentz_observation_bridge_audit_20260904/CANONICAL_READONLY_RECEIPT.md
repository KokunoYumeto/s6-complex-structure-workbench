# Canonical comparison tree: read-only receipt

Canonical root:

`C:\Users\user\Documents\math\output\s6_consolidated_canonical_2026-08-26`

Audit-output root:

`C:\Users\user\Documents\math\agent_work\lorentz_bridge_intake_20260904`

## Scope of this receipt

This audit issued only read operations against the canonical root.  Every file created or modified by this audit is under the audit-output root above.  The canonical tree was simultaneously being changed by other active work lanes, so equality of whole-tree snapshots is neither observed nor claimed.  The purpose of the snapshots is to disclose that concurrent drift and to show separately whether the Lorentz sources actually used by this audit remained stable.

## Deterministic tree-digest algorithm

For every regular file recursively below the canonical root, compute the lowercase SHA-256 of its bytes and form the UTF-8 record

`relative/path NUL decimal-byte-length NUL lowercase-sha256 LF`.

Replace path separators by `/`, sort records ordinally by relative path, concatenate them, and SHA-256 the concatenation.  File count and total byte count are recorded separately.

## Whole-tree snapshots

| Snapshot | Files | Bytes | Deterministic SHA-256 |
|---|---:|---:|---|
| Intake | 597 | 95,305,581 | `c0bda7b261fbcc34dc4ac9db8c2a666c8cb1c68486e68d2d5397214eab6b438d` |
| Mid-audit | 614 | 96,627,417 | `7561efc9032c1edcdf17bc3cedcc65d1566fd0c64182c2a5098ba8bf03aed236` |
| Closure, 2026-09-04T03:58:12Z | 630 | 102,789,955 | `d9350770e7e87b7359fbee120d9c5ab8987daba0f9405c3d03d930b1ed89f4f7` |

The changes include newly generated build artifacts and concurrent Koide/status/overview work.  They are outside this audit's write scope.  Accordingly, the whole-tree drift must not be misreported as a mutation by this intake audit or as an immutable-tree checksum match.

## Lorentz sources used for the comparison

| Relative canonical path | Closure bytes | Closure SHA-256 | Stability during audit |
|---|---:|---|---|
| `workbench.tex` | 56,782 | `c8a755efc9e95b4d090ab17c06a11cd0816d1c269c21ebd88fab1dcb8d8ad6b2` | unchanged from intake hash |
| `supporting_materials/workbench/research/higher_rung_lorentz_observation_bridge.tex` | 31,339 | `68bdb0825113d61836cb8dab494b25be5159b35094d3fac2522d24508f7b287c` | unchanged from intake hash |
| `supporting_materials/workbench/research/higher_rung_toroidal_elliptic_bridge.tex` | 36,927 | `c9cf123c5fa6cd3fb562e9ece981bdcb24289d4727039068a6f01b5ff6a8aaf7` | closure hash recorded; no earlier per-file hash was taken |
| `supporting_materials/workbench/research/worldline_presymplectic_reduction.tex` | 34,868 | `c3b36ed5688e915eeb18c1d3543c72c558e2974af2ef11dafb57e3a3852998b8` | unchanged from intake hash |
| `supporting_materials/workbench/evidence/worldline_presymplectic_reduction_20260904/exact_lorentz_observation_bridge.tex` | 53,061 | `2be16e1dc71b2e5dc04238f0fbe440138258d0825a4841ab2f29662587681599` | unchanged; still byte-identical to packet TeX |
| `workbench_and_manuscript_overview.tex` | 86,029 | `802e89ba3f84b37a8b19ea57f728fb434127c596db114d114dd1baa2078b5f5e` | changed concurrently from intake hash `e8cf3244dc6c5c08f199dec97c562ac0b1be358bce84352979acc1b5045b555d` |

The exact packet-duplication and principal Lorentz/worldline comparisons therefore rest on files whose hashes stayed stable.  The overview was used only as a secondary index; its concurrent change does not affect any proof or novelty verdict in this audit.
