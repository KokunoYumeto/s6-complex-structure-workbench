# T1 exact Koide enumeration receipt

This directory preserves the exact bounded Koide--Narain enumeration from
the supplied research packet.  The two computational files are copied
byte-for-byte from the archive paths
`verification/verify_koide_narain_root_density.py` and
`verification/koide_verification_200000.json`.

## Source archive

- Archive filename: `S6_Koide_MassGap_Research_Packet (1).zip`
- Archive byte count: `1,085,772`
- Archive SHA-256:
  `302909e18ed3930515256a05449c2b122e10e788a0aabc3e299b724cf4a89379`

The source archive's own `SHA256SUMS.txt` records the same two file hashes
listed below.

## Integrated files

| File | Bytes | SHA-256 |
|---|---:|---|
| `verify_koide_narain_root_density.py` | 13,318 | `e4bf2982b26b07add6057b5d2d5c771a52ef52c629b5ad5f0aab24e440e41986` |
| `koide_verification_200000.json` | 4,311 | `b907f0ee5bdd3ad80622b669722d218b79a11a5baab0d4571e141936100706b7` |

## Exact regeneration

Run from this directory:

```text
python verify_koide_narain_root_density.py --max-z 200000 --first 15 --checkpoints 10000 20000 30000 40000 50000 75000 100000 125000 150000 175000 200000
```

The command's standard output must equal
`koide_verification_200000.json`.  The stored result reports 7,109 reduced
roots through height 200,000; every candidate is rechecked with Python
integers in the original defect equation, and the forward and inverse
integral coordinate transformations are checked on every enumerated root.

Integration verification on 3 September 2026 reran that exact command with
Python, obtained exit code `0`, and compared all 219 output lines against the
stored JSON with `0` differing lines.

## Scope

This is finite exact-arithmetic evidence, not a replacement for the
asymptotic counting proof.  Its role is to make the numerical table and the
coordinate-bijection checks independently reproducible while preserving the
upstream bytes and provenance.
