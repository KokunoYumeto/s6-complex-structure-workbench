# Input Archive and Checksum Audit

## Archive integrity

All ten supplied ZIP archives pass a complete `unzip -t` test. No archive is truncated or structurally corrupt.

## Internal SHA-256 ledgers

| Packet | Ledger entries checked | Entries OK | Hash failures | Other ledger defect | Disposition |
|---:|---:|---:|---:|---|---|
| 01 | 66 | 66 | 0 | none | pass |
| 02 | 63 | 63 | 0 | none | pass |
| 03 | 62 | 62 | 0 | none | pass |
| 04 | 63 | 63 | 0 | none | pass |
| 05 | 63 | 63 | 0 | none | pass |
| 06 | 60 | 56 | 4 | one ledger-listed empty-assets README is absent | metadata defect documented |
| 07 | 62 | 62 | 0 | none | pass |
| 08 | 62 | 62 | 0 | none | pass |
| 09 | 57 | 52 | 5 | none | metadata defect documented |
| 10 | 59 | 59 | 0 | none | pass |

### Packet 6

The authority PDF, page PNGs, extracted text, and coordinate evidence pass their recorded hashes. Four completed deliverable files have hashes different from the stale ledger, and one ledger-listed optional file is absent:

| File | Ledger value | Actual value |
|---|---|---|
| `deliverable/assets/README.md` | `f627e0e7e39731c8a832bd7e4f104cd1cf194899fe141d6b7ed2475e2988355c` | absent; `assets/` is intentionally empty according to the QA ledger |
| `deliverable/packet_06_body.tex` | `30b761a92f9dbd80fd11ff7914438a3f6f354104a357d226903bb135daf5a3ff` | `f5fc2460fb8ddd3b65559224c8bdc056a6980ab14b8100ff212d842242aa0457` |
| `deliverable/packet_06_completion.json` | `5974ec54a4270a777da6b05684894c2a3715ab8f5e436379318c397c2eb51bb4` | `f715dc271ce0efcf44032cd319ed3666b1967524d9236287e1c5eb31fe8df0e2` |
| `deliverable/packet_06_qa.md` | `9928531d058815a9dd77e6e357a35351fdd7024c15267d1612d5a7ed3f1ac5f5` | `7033fa3ca47947d8994bfe5b633a24709df1ebf89ec7222c0800a7fd944edda4` |
| `deliverable/packet_06_standalone.tex` | `298b412eb535e6fb853b934f394f85867d6be921fd7278250c259fcb09fd0784` | `fc983dabd4262e0e2e8a24671586ff1dc93e47124045b8ec298fee2f89bf833e` |

### Packet 9

The authority PDF, page PNGs, extracted text, and coordinate evidence pass their recorded hashes. Five completed deliverable/template files have hashes different from the stale ledger:

| File | Ledger value | Actual value |
|---|---|---|
| `deliverable/packet_09_body.tex` | `2487436b064d2964542570654686a1bd27096ab6770997df5ce59483fe26b694` | `8c311d789e1bee1dbe2b1ea7933aa4bf1dc75fe5e5e58c1755e4c66c8f03a093` |
| `deliverable/packet_09_completion.json` | `3647dd1e143b9c254fe085280201377f5a493f09373d42b4cc9e59dfcfc8668b` | `323bbfa6559e4a14fbadf3da6e997a536a707ad1be9cd99e3d69372d259d1774` |
| `deliverable/packet_09_qa.md` | `1a0dc5f2abb768723a1c8d510d65e30e0b5a6b37ce5cbacbe998e5565d60dc89` | `bf899ad8e688409ce2706bfc1321953c2a9a269e780c477ac9fc971a8018619c` |
| `deliverable/packet_09_standalone.tex` | `c834597179481318802b57ac8e99eb1d084621435394870a496857e6b3d1bdcf` | `1e32727aeaa4d2ef4465a089f84b211b013e7239f8d8dad03fcca823e6e20505` |
| `templates/shared_preamble.tex` | `658b56cd0ee750f0a65dcf5e4d198d17762146be68ff787ba60ebe5e6f59647b` | `0e1593667a1728f891c293dc6938a83abb275882d1bd808aa1ac2fc58d1c3cad` |

## Interpretation

These are internal packet-ledger maintenance defects, not authority corruption. The consolidation uses the actual completed files, verifies their page receipts, rebuilds them in the canonical document, compares the result against the authority at 200 dpi, and generates a new release-wide `SHA256SUMS.txt` after all files are finalized.
