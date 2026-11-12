# Mathematical consolidation reader

This directory is the current reader for the preserved S6, selector, cusp, quaternionic, measured-fibre, quantum, and zeta-adjacent material. It joins exact custody, a queryable corpus catalogue, a proved mathematical note, a claim-correction ledger, and an ordered queue for material that has not received a semantic audit.

The reader does not turn an archived assertion into a theorem merely because the assertion was found, indexed, compiled in an earlier session, or repeated in several versions. Every status is one of the following:

- **proved here**: a complete argument appears in `MATHEMATICAL_NOTE.md`, with verification that supports but does not replace the proof;
- **bounded source reading**: the exact source version and read lines are recorded in `../ledgers/actual_source_readings.jsonl`;
- **routed source claim**: the catalogue identifies the file or lexical span, but no new proof acceptance follows;
- **unmined**: exact bytes or decoded text are retained, but the mathematical content has not yet received a semantic audit;
- **missing original history**: a projected record exists while the source JSONL has not been located.

## Reading order

1. `MASTER_MAP.md` gives the object-level map and the status of every major mathematical lane.
2. `MATHEMATICAL_NOTE.md` contains the complete current proofs R1--R8, with the finite determinant calculation for R7 in `TOMOGRAPHY_DESIGN.md`.
3. `CLAIM_LEDGER.md` records corrections, strengthenings, propagation, and scope boundaries.
4. `AUDIT_LIMITATIONS.md` states what the catalogue and current audit can and cannot establish.
5. `UNMINED_QUEUE.md` orders the remaining material and specifies the next exact calculations.
6. `BUILD_STATUS.md` records source generation, successful structural parsing, and the unavailable compiler environment.
7. `CATALOGUE_GUIDE.md` documents the SQLite schema, evidence rules, and read-only queries for future mining.
8. `UNCLASSIFIED_TRANCHE_2026-09-30.md` records the first bounded semantic-routing tranche, including every source hash, cue line, and sample custody route.
9. `CORPUS_CATALOGUE_V2.sqlite` and `ARCHIVE_MEMBER_COVERAGE_V2.jsonl.gz` provide machine-readable access to every registered text version, direct archive entry, package version, package placement, containment edge, recursively expanded logical member occurrence, lexical span, reference, and unsupported member record. The V1 files remain for provenance and are superseded for occurrence claims.
10. `CONSOLIDATION_RECEIPT_V2.json` hashes the corrected reader, database, evidence streams, verification data, figures, scripts, source-reading ledger, result bulletin, and durable continuity records.

## Current corpus receipt

The V2.1 catalogue recomputes the SHA-256 of all nine custody ZIPs and registers all 71,426 direct entries. It records 214 direct nested-package placements, 56 distinct nested-package byte versions, 12,822 file definitions across those distinct versions, and 29,324 logical nested entry occurrences after every placement and containment edge is expanded with multiplicity. Those logical occurrences include 24,564 text occurrences. The outer archives contain 41,695 direct text occurrences and 29,517 direct opaque occurrences. There are 7,637 distinct retained text byte versions, including 1,282 TeX versions. The structural index contains 55,659 spans or routing locators and 87,272 literal label, reference, include, and citation records.

The first catalogue collapsed repeated package placements and mislabeled 12,822 file definitions as occurrences. It also assigned a nested 4,078-byte `MANIFEST.json` hash to a later 52,910,440-byte direct file with the same member name. V2.1 separates definitions from placements and logical occurrences, checks all 41,695 direct text assignments against the ZIP byte count and CRC32, rereads the single mismatch from the outer archive, and retains its exact SHA-256. `CATALOGUE_V2_RECEIPT.json` and `DIRECT_TEXT_MAPPING_AUDIT.json` record the correction; no direct-text metadata mismatch remains.

Two TeX versions that failed strict UTF-8 decoding were recovered without changing a source byte. One round-trips exactly as CP932 and one as CP1252. `ENCODING_RECOVERY_RECEIPT.json` records the hashes, byte lengths, evidence, encodings, and extracted locators. No registered text version remains undecoded.

The first evidence-backed routing tranche inspected an exact cue line in each of the 40 largest previously unclassified TeX versions. It routes 2 Navier--Stokes constructions, 7 GCT/arithmetic sources, 23 primary S6 constructions, and 8 Yang--Mills spectral sources while retaining every byte version and occurrence. This reduces the conservative unclassified lane from 4,268 to 4,228 versions. The tranche is routing evidence and does not certify any theorem in those sources.

These totals measure coverage and routing. They do not measure the number of distinct mathematical works, correct proofs, or independent results. Duplicate editions, historical alternatives, inactive TeX branches, generated material, and conversation records can all contribute separate occurrences or versions.

## New mathematics

`MATHEMATICAL_NOTE.md` keeps the original quaternionic Moore cubic, all Gaussian constants, both marking conventions, the actual residual action, the complete observed/conditional split, and the original time and coupling parameters. It proves:

- the full quaternionic Gaussian mass and covariance;
- the exact morphism between the Jordan marking and sample-precision marking, including Jacobians and the three distinct fibres;
- the exact residual-orbit integrability threshold and averaged mass;
- every positive residual exponent's sharp simple-zero and tangency thresholds, with exact no-crossing moments;
- the common-Hilbert-space affinity and Fisher coefficient;
- a finite-dimensional completely positive phase channel and its exact observed/conditional factorization;
- the distinction between static Gaussian dephasing, CP-divisibility, and a separately defined integrated-phase Brownian GKLS semigroup with exact units;
- a level-minimal six-level reconstruction of the full quaternionic precision from fifteen pair coherences, a level-minimal four-level observed reconstruction, and the exact nine-dimensional observation ambiguity.

Four retained figures show the exact maps, time laws, residual exponent thresholds, and minimal tomography designs in PNG, SVG, and PDF. Their source is `verify_consolidation_v2.py`; `MATHEMATICAL_CHECKS_V2.json` records twenty exact check groups and five separately identified numerical evidence groups. The non-diagonal stress sample has maximum relative cubic error below `1.9e-15`. The proofs remain the authority, and the earlier 42-check receipt is superseded because it counted repeated samples and tested only diagonal tomography.

## Scope boundary

The current work does not certify the historical global S6 candidate, an S6 sphere recognition, a bosonic field model, redundant environmental records, a decoherent-histories functional, a Yang--Mills mass gap, a Navier--Stokes theorem, or an original-zeta proof. Those materials remain routed and preserved. The zeta-related queue expressly requires reconstruction from the original zeta function with every completion factor, pole, zero, derivative term, and endpoint contribution retained.

The standalone TeX source is `CONSOLIDATION.tex`. The built-in compiler could not locate its standard platform directories, so no successful PDF build is claimed. The Markdown proof, TeX source, figures, source archives, exact checks, and compilation limitation are all retained.

## GitHub publication - 2026-09-30

The [public corrected edition](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/tree/5f358fb5b277e882e9b83df06367fe4145b7d242/s6/consolidation/20260930) is published on `main` at commit `5f358fb5b277e882e9b83df06367fe4145b7d242`. `GITHUB_PUBLICATION_2026-09-30.json` records the remote tree and anonymous byte verification. The earlier V2 receipt describes the prepublication correction snapshot; the public edition has its own manifest and validation receipt.
