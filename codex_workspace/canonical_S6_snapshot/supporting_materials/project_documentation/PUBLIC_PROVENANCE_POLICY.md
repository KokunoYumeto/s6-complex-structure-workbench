# Public mathematical provenance policy

## Purpose and source boundary

The Codex session record is useful for reconstructing when a mathematical
objection, repair, calculation, citation, or release decision entered the
work.  The raw session JSONL is not suitable for publication: it contains
system and tool traffic, repeated or fragmentary conversation, unrelated
operational material, local-machine details, and informal language that adds
no mathematical evidence.

The immutable source remains private and unmodified.  At the final release
freeze, the exact JSONL byte count and SHA-256 will be recorded.  The DOI may
contain only a derived **public mathematical provenance edition** and its
redaction receipt.  Neither file is a substitute for the proofs, source code,
or exact certificates in the monograph.

## What the public edition retains

An event is retained only when it materially records at least one of the
following:

1. the provenance or attribution of the candidate manuscript and review
   packages;
2. a mathematically specific request, objection, lemma, counterexample,
   correction, proof strategy, or status change;
3. an exact calculation, script result, source citation, or independent-review
   finding used in the final paper;
4. a decision that changed the mathematical exposition, theorem statement,
   hypotheses, or evidence boundary; or
5. a release fact needed to reproduce a public artifact, such as a checksum,
   page count, compiler result, or canonical-project identifier.

Retained entries preserve chronological order, mathematical notation, named
hypotheses, conclusions, and the distinction among source claims, reviewer
claims, Codex proofs, and open outside adjudication.  Obvious spelling and
grammar errors may be corrected for readability, and repeated fragments may
be consolidated, but no mathematical content may be strengthened, weakened,
or silently reassigned.  Edited entries are labelled as edited for clarity;
direct quotations remain verbatim.

## What is excluded

The derived public edition excludes:

- profanity, insults, interpersonal remarks, and conversational filler;
- duplicate prompts, false starts, typing fragments, acknowledgements, and
  status requests that introduce no mathematical or release information;
- system, developer, compaction, ambient-UI, permission, and tool-schema text;
- hidden reasoning, raw tool calls, voluminous command output, and temporary
  build chatter when a compact signed receipt already records the result;
- unrelated tasks, model-cap and resource-management discussion, crash and
  cleanup traffic, and other operational material without release relevance;
- credentials, tokens, cookies, private URLs, account data, machine-unique
  absolute paths, and security-sensitive configuration;
- third-party text that cannot be redistributed, except for bibliographic
  identification and short quotation within applicable limits; and
- any event whose relevance or publication status remains uncertain.

Private local paths are replaced by stable project-relative paths or public
citations.  Secrets are omitted rather than masked in a way that might permit
reconstruction.  The raw JSONL is never bundled, uploaded, or linked.

## Audit and receipt

Sanitization is a two-stage derivation.  A streaming structural pass first
extracts only conversation events and computes event hashes without copying
system prompts, tool payloads, or outputs.  A content pass then admits only
events satisfying the retention rule above, performs the permitted editorial
normalization, and checks every mathematical statement against the canonical
workbench, research ledger, or a cited review record.

The public receipt records:

- the frozen source JSONL byte count and SHA-256;
- the extraction script version and SHA-256;
- source ordinals and hashes for retained events;
- counts excluded under each category, without reproducing excluded text;
- the hash of the public provenance edition; and
- confirmation that no credential pattern, private absolute path, raw tool
  payload, or unlicensed third-party document is present.

This method provides traceability without turning informal session traffic
into publication content.  The mathematical paper remains primary.

## Optional complete sanitized conversation edition

The short mathematical chronology is the canonical provenance surface.  A
second, machine-readable conversation edition may be included as an optional
audit supplement only if it independently passes a stricter complete-record
pipeline.  That edition contains every natural-language user and assistant
message event in the frozen prefix, but never any system, developer, tool,
reasoning, state, or raw JSONL record.  Each public event retains its source
ordinal, timestamp, role, and exact private-source text hash.

Non-abusive turns may be reproduced after deterministic redaction.  A turn
containing profanity or abusive wording is withheld unless a neutral editorial
summary, anchored to the exact source-text hash, has been checked to preserve
every actionable directive and every mathematical statement.  Every role is
redacted for personal names, local paths, private links, credentials, account
or task identifiers, and internal protocols.  The edition is admitted only
when the unresolved-event count is zero and both the generator and independent
validator report `RELEASE_READY`.  Otherwise it remains private working
material and cannot delay or block the core DOI release.

For version 1.0 this gate passed: after structurally excluding 166
platform-injected context-only user-role records, the frozen prefix contains
976 qualifying human/assistant natural-language events, of which 940 are
verbatim-redacted and 36 are summarized-redacted.  All 36 summaries are
anchored to exact source-text
SHA-256 values and carry the five required editorial certifications.  The
unresolved-event count is zero.  The generator and an independent replaying
validator both report `RELEASE_READY`, and their signed receipts accompany the
edition.  The private 1.4 GB source record itself is not deposited.

## Optional full typed-record annex

A third provenance surface may preserve the wider workflow without depositing
the private raw record. It retains conversation text only under the same
redaction and summary rules as the complete conversation edition. For tool
calls and outputs it retains typed sequence, tool names, call/output pairing,
sizes, hashes, structural profiles, and safe execution or status scalars, but
never raw arguments, prompts, output bodies, images, paths, credentials, or
private identifiers. Internal-agent traffic is represented only by metadata
markers; system, developer, compaction, state, and hidden-reasoning records are
excluded.

Admission requires deterministic replay from an exact newline-complete source
prefix, canonical JSONL, strict unique chronology, exact gzip decompression,
complete hash-ledger verification, an empty unresolved queue, and a zero-finding
privacy scan over every parsed public field. Because the automated generator
cannot authorize its own publication, a separate parent review must rerun the
validator, record the frozen source identity and residual limitations, and
authorize inclusion explicitly.

For version 2.0 this gate passed on a 1,483,338,786-byte prefix with SHA-256
`d9991d392c62c9c898cb80ff64db6c1cc822909e24c1e0e885864ba87070880a`.
The public stream contains 20,977 typed events, including 1,011 conversation
messages, 9,570 tool calls, 9,567 tool outputs, and 829 metadata-only
internal-agent markers; 37 user turns are neutral source-hash-anchored
summaries. Seven legacy orphan outputs and ten unpaired calls at legacy or
frozen boundaries are recorded rather than hidden. The deterministic gzip and
parent-review receipt accompany the stream under
`supporting_materials/publication/full_record_public_annex_v2/`.

## Attribution and scope

The explicit candidate and its original claims remain attributed to their
reported Claude/Fabel source.  The present Codex work is described as an
AI-produced verification aid: it makes maps and calculations explicit,
reproduces and repairs arguments, and isolates open adjudication boundaries so
that human experts need not reconstruct every intermediate step from scratch.
That is a substantive contribution, but it is not a claim of priority for the
candidate and does not constitute independent specialist certification.
