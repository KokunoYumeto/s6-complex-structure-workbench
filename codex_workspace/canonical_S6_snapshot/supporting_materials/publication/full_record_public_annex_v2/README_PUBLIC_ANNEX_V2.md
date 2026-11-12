# S6 full-record public annex v2 candidate

This optional machine-ingestible annex is a deterministic public evidence ledger derived from one frozen, newline-terminated prefix of the private active S6 root rollout. The private rollout is not included.

Conversation messages retain safe text after public redaction; certified neutral summaries replace user turns that require them. Tool calls and outputs retain typed sequence, pairing, tool names, sizes, hashes, structural profiles, safe execution scalars, and risk flags. Raw commands, prompts, local paths, identifiers, images, and output text are not copied. Internal agent coordination is represented only by metadata markers. Platform, system, developer, compaction, state, and encrypted reasoning payloads are excluded.

The gzip member is deterministic (`mtime=0`) and decompresses byte-for-byte to the JSONL file. Every public event retains its exact source ordinal, timestamp, and private-source record hash. This is a review candidate, not publication authorization.
