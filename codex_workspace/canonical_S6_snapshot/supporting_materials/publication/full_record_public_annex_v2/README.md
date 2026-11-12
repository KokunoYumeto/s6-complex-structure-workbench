# Full typed-record provenance annex

This optional supplement is the machine-ingestible audit trail for the S6
verification task.  It derives from a frozen newline-complete prefix of the
private active root record; the private raw record is not deposited.

For direct use, read
`s6_full_record_public_annex_v2.jsonl` or its byte-identical deterministic gzip
form `s6_full_record_public_annex_v2.jsonl.gz`.  The stream contains 20,977
ordered typed events: 1,011 conversation messages, 9,570 tool calls, 9,567 tool
outputs, and 829 metadata-only internal-agent markers.  Safe conversation text
is retained after redaction; 37 user turns are represented by neutral,
source-hash-anchored summaries.  Tool events retain names, types, ordering,
pairing, sizes, hashes, structural profiles, and safe status scalars, but not
raw commands, prompts, paths, identifiers, output text, images, or credentials.

The immutable generator output still says `PARENT_REVIEW_REQUIRED`, because
that was its correct status when the bounded subtask ended.  The parent task
subsequently reran the validator against the exact 1,483,338,786-byte frozen
prefix, verified every row of `SHA256SUMS.txt`, reviewed the schema and sample
redactions, and authorized inclusion.  That decision and its limitations are
recorded in `PARENT_REVIEW.json`.

This annex is provenance, not a substitute for the mathematical proofs or
their independent adjudication.  The smaller
`../complete_sanitized_conversation_v1.jsonl` remains the convenient
human/assistant-only edition.
