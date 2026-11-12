# Corpus catalogue guide

`catalogue/CORPUS_CATALOGUE_V2_PUBLIC.sqlite` is the canonical query layer over the preserved custody corpus. It is read-only evidence for future audits; mutations should be made through a reproducible catalogue edition or additive repair script with a receipt. The V1 database is retained in private custody and is superseded for occurrence claims. The public gzip archive must be unpacked with `catalogue/unpack_catalogue.py` before these queries can be run. Source-text routes identify local custody objects; the text blobs themselves are not part of this public edition.

## Tables

| Table | Key fields | Meaning |
|---|---|---|
| `versions` | `sha256`, `corpus_file`, `bytes`, `suffix`, `lines`, `lexical_status` | One row for each distinct retained text byte version. |
| `archives` | `sha256`, `archive_path`, `archive_bytes`, `expected_direct_entries`, `verified_sha256` | The nine outer custody archives after a fresh full-file SHA-256 pass. |
| `archive_members` | archive hash, ordinal, member, byte/CRC fields, class, content/text/package links | Every outer ZIP central-directory entry, retaining duplicate names by ordinal. |
| `direct_text_occurrences` | text hash, archive hash, ordinal, member, source root, origin | Every direct text placement in an outer archive. |
| `package_versions` | package hash, bytes, entry/file/directory counts, status | One definition for each distinct nested ZIP byte version. |
| `direct_package_occurrences` | archive hash, ordinal, member, package hash | Every nested-package placement in an outer archive. |
| `package_members` | package hash, ordinal, member metadata, class, text hash, child package hash | Every entry definition while each distinct package version is opened once. |
| `package_edges` | parent package hash, member ordinal, child package hash | Exact containment edges between package versions. |
| `expanded_package_member_occurrences` | direct package placement, depth, package/member identity, logical path | Every logical nested entry reached after all placements and containment edges are expanded with multiplicity. |
| `logical_nested_text_occurrences` | view over expanded occurrences | Every logical nested text placement. |
| `spans` | `sha256`, `kind`, `name`, line/offset bounds, `span_sha256`, `status` | Literal TeX environments, headings, or routing-only manual theorem/proof headings. |
| `references_found` | `sha256`, `kind`, `target`, `line` | Literal `label`, `ref`, `input`, `include`, and citation targets. |
| `topics` | `sha256`, `lane`, `basis` | Overlapping routing lanes and the reason for each route. |
| `classification_tranches` | `tranche_id`, selector, reading scope, version count | Reproducible bounds for semantic-routing tranches. |
| `classification_evidence` | tranche, version, cue line/text/pattern, assigned lanes | Exact inspected cue supporting each tranche route. |
| `direct_text_mapping_audit` | archive hash, ordinal, V1 hash, actual hash, reason | The exact correction of the one V1 direct-member name collision. |
| `legacy_text_occurrences`, `legacy_opaque_members`, `legacy_nested_packages` | V1 fields | Superseded relations retained for provenance and comparison only. |

## Useful read-only queries

Find every direct and logical nested occurrence of a version:

```sql
SELECT 'direct' AS occurrence_kind,
       a.archive_path,
       d.member AS logical_path,
       d.archive_member_ordinal AS direct_ordinal
FROM direct_text_occurrences AS d
JOIN archives AS a ON a.sha256=d.archive_sha256
WHERE d.sha256=:sha256
UNION ALL
SELECT 'nested' AS occurrence_kind,
       a.archive_path,
       n.logical_path,
       d.archive_member_ordinal AS direct_ordinal
FROM logical_nested_text_occurrences AS n
JOIN direct_package_occurrences AS d ON d.id=n.direct_package_occurrence_id
JOIN archives AS a ON a.sha256=d.archive_sha256
WHERE n.text_sha256=:sha256
ORDER BY archive_path, direct_ordinal, logical_path;
```

List proof environments in one exact version:

```sql
SELECT name, start_line, end_line, span_sha256, status
FROM spans
WHERE sha256 = :sha256 AND kind = 'proof'
ORDER BY start_offset;
```

Route a lane to exact source paths:

```sql
SELECT DISTINCT t.lane, v.sha256, v.corpus_file, t.basis
FROM topics AS t
JOIN versions AS v ON v.sha256 = t.sha256
WHERE t.lane = :lane
ORDER BY v.sha256;
```

Find every literal reference to a label:

```sql
SELECT r.sha256, r.kind, r.line, v.corpus_file
FROM references_found AS r
JOIN versions AS v ON v.sha256=r.sha256
WHERE r.target = :target
ORDER BY r.sha256, r.line;
```

Start the unclassified audit with the largest TeX versions:

```sql
SELECT v.sha256, v.bytes, v.lines, v.corpus_file
FROM versions AS v
JOIN topics AS t ON t.sha256 = v.sha256
WHERE t.lane = 'unclassified' AND v.suffix = '.tex'
ORDER BY v.bytes DESC;
```

Inspect unsupported direct placements by size and suffix:

```sql
SELECT archive_sha256, ordinal, member, uncompressed_bytes, suffix, status
FROM archive_members
WHERE member_class='opaque'
ORDER BY uncompressed_bytes DESC;
```

Distinguish package definitions from logical occurrences:

```sql
SELECT 'distinct package file definitions' AS quantity, COUNT(*) AS value
FROM package_members WHERE is_directory=0
UNION ALL
SELECT 'logical nested entry occurrences', COUNT(*)
FROM expanded_package_member_occurrences
UNION ALL
SELECT 'logical nested text occurrences', COUNT(*)
FROM logical_nested_text_occurrences;
```

## Interpretation rules

A `proof` row means that the exact text contains a lexically matched proof environment. It does not certify the proof. A `manual_proof_locator` identifies only a source heading; no body boundary was inferred. A topic lane is a route, can overlap other lanes, and does not accept a claim. A logical occurrence can be historical, generated, inactive, or duplicated. A package definition is not an occurrence count. Use the source-reading ledger before saying that a passage was read, and use `CLAIM_LEDGER.md` before saying that a mathematical statement is accepted.

`catalogue/CATALOGUE_V2_PUBLIC_RECEIPT.json` gives the current totals, hashes, validation, and supersession record. `checks/DIRECT_TEXT_MAPPING_AUDIT.json` gives the direct-member collision evidence. `checks/ENCODING_RECOVERY_RECEIPT.json` gives the two non-UTF-8 recovery details. `PUBLICATION_MANIFEST.json` hashes the corrected principal reader artifacts. The V1 receipts remain historical records.
