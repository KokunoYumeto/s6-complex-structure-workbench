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

## Attribution and scope

The explicit candidate and its original claims remain attributed to their
reported Claude/Fabel source.  The present Codex work is described as an
AI-produced verification aid: it makes maps and calculations explicit,
reproduces and repairs arguments, and isolates open adjudication boundaries so
that human experts need not reconstruct every intermediate step from scratch.
That is a substantive contribution, but it is not a claim of priority for the
candidate and does not constitute independent specialist certification.
