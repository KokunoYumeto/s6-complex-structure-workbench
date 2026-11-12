# Exact source-archive receipts

These small archive containers are retained exactly as downloaded or previously released:

| File | Bytes | SHA-256 |
|---|---:|---|
| `reviewer_a_full_package.zip` | 225,788 | `4fb028a8e9377fefdfb6ed25c2b7784d5f4e13170d379ff3449dd1612bb16600` |
| `earlier_packet06_review.zip` | 226,909 | `759b18122ded84a3ac17e8dbf85e3c7df428ac9976f7975cbd4f411bc2903703` |
| `codex_integrated_review.zip` | 277,824 | `2d79e759fcc1879d73fa615019a824b7ae805c95bc7386d72dfa27729cc97cc9` |
| `reviewer_b_candidate_specific_validation_update.zip` | 513,043 | `94c1d1e134718e8978ecf7ad691c8e7a0f0d96fa9a46bcb51bfacc4d1659e7d4` |
| `webpro_corrective_integrated_review_2026-08-25.zip` | 996,972 | `1255bfef814671b4c56b516e379ab364ea2872d3ebe0b812518868eabf6cd62b` |

The 69 MB canonical audit ZIP is recorded in
`supporting_materials/project_documentation/EXCLUSIONS.md`; its substantive
contents are unpacked in this project instead of duplicating the oversized
container.

The earlier annotated-release ZIP is also recorded rather than embedded: it has SHA-256 `8280c5c04239e000142132a77834856f97eb4164fbc858b3d0375b3b44e5b084`, but its raw build logs expose local absolute user paths. The public tree contains the same substantive source/PDF/QA material without those logs.
