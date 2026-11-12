# Public corpus catalogue

`CORPUS_CATALOGUE_V2_PUBLIC.sqlite.gz` is a deterministic gzip stream of the V2.1 SQLite catalogue. Decompress it before issuing the read-only queries in [CATALOGUE_GUIDE.md](../CATALOGUE_GUIDE.md):

```bash
python unpack_catalogue.py
```

The unpacker verifies the resulting `CORPUS_CATALOGUE_V2_PUBLIC.sqlite` against the byte length and SHA-256 recorded in the receipt.

`ARCHIVE_MEMBER_COVERAGE_V2_PUBLIC.jsonl.gz` contains one JSON record for every one of the 71,426 direct outer-archive entries. The public derivative retains archive identity by SHA-256, central-directory ordinal, byte counts, CRC32, content hashes, package identities, and status. Archive labels are aliases. Account-specific roots are removed, and routes to private operational material are represented by stable SHA-256-based route identifiers.

The catalogue contains metadata and routing evidence. It does not contain the source text blobs, custody ZIP payloads, or private dialogue content. A route, span, reference, cue line, or topic label does not certify a theorem.
