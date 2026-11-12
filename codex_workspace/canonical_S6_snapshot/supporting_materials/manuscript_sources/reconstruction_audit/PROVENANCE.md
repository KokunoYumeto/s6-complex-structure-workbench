# Provenance

## Nature of the source

The canonical LaTeX is an independent reconstruction from the supplied PDF authority and packet evidence. It is not the author's original source code.

Every packet completion receipt records the same original full-PDF SHA-256:

`283bba102dd1d5dc346af81b28145bdaaea6654398d5032e76e97bafb9a858f2`

The original full PDF itself was not supplied as one file in this consolidation turn; the ten packet authority slices were supplied and were reassembled, in order, into `authority/s6_authority_reassembled.pdf`.

## Packet coverage

| Packet | Physical pages | Count | Completion status | Upstream page checks |
|---:|---:|---:|---|---:|
| 01 | 001–011 | 11 | COMPLETE | 11 clear |
| 02 | 012–022 | 11 | COMPLETE | 11 clear |
| 03 | 023–033 | 11 | COMPLETE | 11 clear |
| 04 | 034–044 | 11 | COMPLETE | 11 clear |
| 05 | 045–055 | 11 | COMPLETE | 11 clear |
| 06 | 056–066 | 11 | COMPLETE | 11 clear |
| 07 | 067–077 | 11 | COMPLETE | 11 clear |
| 08 | 078–088 | 11 | COMPLETE | 11 clear |
| 09 | 089–098 | 10 | COMPLETE | 10 clear |
| 10 | 099–108 | 10 | COMPLETE | 10 clear |

Coverage is exactly pages 1–108, with no gap, overlap, duplicate, or omitted page.

## Input archive SHA-256 values

| Packet | Archive SHA-256 |
|---:|---|
| 01 | `38f6ee9a5b40f9b90c0c8517ad1ba28352b83fe77a79640ed1ebdfb49c4dcbd7` |
| 02 | `267bae338759e47906fb5236c51309ad9bd8fa5eeafa9f97e795864e50fde19f` |
| 03 | `e7b8f8e7d2c109d5b44d52be30e3436c883944e133c6aee605186f93c6bb3e59` |
| 04 | `2ed89ec5bf302b64e4037ea168b6269bd0a7c416283a44f57557f1b1c0dfb86c` |
| 05 | `38274288e50c4e7500682a5c305c45fe82bdd3b96bce51c0c80d180f90c17da1` |
| 06 | `f6f1666c5c6d77d911fe30a53532e98ec7e4a604e3671acbf4b45295ba6d30d0` |
| 07 | `5821e6561cc2ee6272fff5cb42b8c535edabb0f31b85e19b6fb84b05d9b1bbdc` |
| 08 | `188c3f7f23df82338ae2f957aacfcbe320c7ae182f7c4e8237e92546b4b6ec69` |
| 09 | `5b58f8771b68d7319b0c3cf68fda5ef091f7954d8b5589f984c3f159bb78d0d3` |
| 10 | `7d7fb2f622c947f27ae3c89d90ed3c0720e6850c354cb7ea0658eef95b67cc87` |

All ten ZIP archives pass `unzip -t`. Internal ledger defects in packets 6 and 9 are detailed in `audit/INPUT_ARCHIVE_AUDIT.md`.

## Canonical-part inheritance

Packets 2–10 are byte-identical to the actual completed packet body files. Packet 1 differs by only two audited page-2 layout parameters: horizontal margins and local font size/leading. No prose, symbol, equation, citation, tag, or page boundary was changed. Exact hashes and dispositions are in `audit/part_provenance.tsv`.
