#!/usr/bin/env python3
"""Build a privacy-safe, complete conversation-provenance candidate.

The private Codex JSONL is streamed only through a byte-exact, newline-ended
prefix.  Only user/assistant message text is considered.  Structural context
embedded in a message is removed, and system, developer, tool, reasoning, and
state records are never copied.  Every retained event is anchored by source
ordinal, timestamp, role, and hashes of the exact decoded source text.

The program is deliberately fail closed.  A source turn containing profanity
or abusive language is withheld unless an independently prepared editorial
summary, anchored to the source-text hash and carrying explicit adequacy
certifications, is present.  Unresolved turns remain represented by metadata
only, and the receipt is marked NOT_RELEASE_READY.
"""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
import os
from pathlib import Path
import re
import tempfile
from typing import Any, BinaryIO, Iterable
from urllib.parse import parse_qsl, urlsplit


VERSION = "1.0.0"
SCHEMA = "s6-complete-conversation-provenance-v1"
RECEIPT_SCHEMA = "s6-complete-conversation-provenance-receipt-v1"
SUMMARY_SCHEMA = "s6-complete-conversation-editorial-summaries-v1"

EDITION_NAME = "complete_sanitized_conversation_v1.jsonl"
QUEUE_NAME = "complete_sanitized_conversation_unresolved_queue_v1.jsonl"
RECEIPT_NAME = "complete_sanitized_conversation_receipt_v1.json"
STATUS_NAME = "complete_sanitized_conversation_release_status_v1.txt"
SUMMARY_NAME = "complete_sanitized_conversation_editorial_summaries_v1.json"
VALIDATOR_NAME = "validate_complete_conversation_provenance.py"

TEXT_BLOCK_TYPES = frozenset({"input_text", "output_text", "text"})
ALLOWED_ROLES = frozenset({"user", "assistant"})


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(8 * 1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def canonical_json_bytes(value: Any) -> bytes:
    return json.dumps(
        value,
        ensure_ascii=False,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")


def write_jsonl(handle: BinaryIO, value: Any) -> None:
    handle.write(canonical_json_bytes(value))
    handle.write(b"\n")


def text_blocks(payload: dict[str, Any]) -> list[str]:
    result: list[str] = []
    content = payload.get("content")
    if not isinstance(content, list):
        return result
    for block in content:
        if not isinstance(block, dict) or block.get("type") not in TEXT_BLOCK_TYPES:
            continue
        text = block.get("text")
        if isinstance(text, str):
            result.append(text)
    return result


def joined_source_text(blocks: Iterable[str]) -> str:
    """Match the existing selected-chronology extractor's text convention."""

    return "\n".join(blocks)


# Platform-supplied context may be serialized inside a user-role message.  It
# is not conversation and must not be reproduced.  Tags are deliberately
# named rather than accepting arbitrary XML, so mathematical angle brackets
# remain intact.
EMBEDDED_BLOCK_TAGS = (
    "app-context",
    "apps_instructions",
    "codex_delegation",
    "codex_internal_context",
    "environment_context",
    "in-app-browser-context",
    "INSTRUCTIONS",
    "permissions instructions",
    "plugins_instructions",
    "recommended_plugins",
    "skills_instructions",
    "tool_call",
    "tool_result",
    "function_call",
    "function_call_output",
    "custom_tool_call",
    "custom_tool_call_output",
)
EMBEDDED_BLOCK_RE = re.compile(
    r"(?is)<(?:"
    + "|".join(re.escape(tag) for tag in EMBEDDED_BLOCK_TAGS)
    + r")\b[^>]*>.*?</(?:"
    + "|".join(re.escape(tag) for tag in EMBEDDED_BLOCK_TAGS)
    + r")\s*>"
)
AGENTS_CONTEXT_RE = re.compile(
    r"(?ims)^#\s*AGENTS\.md instructions for[^\r\n]*\r?\n"
    r"(?:<INSTRUCTIONS>.*?</INSTRUCTIONS>\s*)?"
)
ORPHAN_CONTEXT_TAG_RE = re.compile(
    r"(?is)</?(?:"
    + "|".join(re.escape(tag) for tag in EMBEDDED_BLOCK_TAGS)
    + r")\b[^>]*>"
)
RAW_PLATFORM_MARKER_RE = re.compile(
    r"(?i)(?:<\/?(?:"
    + "|".join(re.escape(tag) for tag in EMBEDDED_BLOCK_TAGS)
    + r")\b|^#\s*AGENTS\.md instructions for)",
    re.MULTILINE,
)


def strip_embedded_nonconversation(text: str) -> tuple[str, int]:
    count = 0

    def remove_block(match: re.Match[str]) -> str:
        nonlocal count
        count += 1
        return "\n"

    text = EMBEDDED_BLOCK_RE.sub(remove_block, text)

    def remove_agents(match: re.Match[str]) -> str:
        nonlocal count
        count += 1
        return "\n"

    text = AGENTS_CONTEXT_RE.sub(remove_agents, text)
    text, orphan_count = ORPHAN_CONTEXT_TAG_RE.subn("", text)
    count += orphan_count
    # Only outer whitespace is editorially removed.  Internal layout survives.
    return text.strip(), count


# Source-content gate.  Terms are bounded to avoid false positives such as the
# mathematical words "class", "assumption", or "cockle".  The phrase patterns
# cover common direct abuse even when no conventional profanity is present.
PROFANITY_TERMS = (
    "asshole",
    "bastard",
    "bitch",
    "bullshit",
    "crap",
    "cunt",
    "damn",
    "dick",
    "fuck",
    "fucked",
    "fucker",
    "fuckers",
    "fucking",
    "goddamn",
    "hell",
    "motherfucker",
    "motherfuckers",
    "piss",
    "retard",
    "retarded",
    "shit",
    "shitty",
)
PROFANITY_RE = re.compile(
    r"(?i)(?<![A-Za-z0-9_])(?:"
    + "|".join(re.escape(term) for term in sorted(PROFANITY_TERMS, key=len, reverse=True))
    + r")(?![A-Za-z0-9_])"
)
OBFUSCATED_PROFANITY_RE = re.compile(
    r"(?i)(?<![A-Za-z0-9])(?:f\W*u\W*c\W*k|s\W*h\W*i\W*t)(?![A-Za-z0-9])"
)
ABUSIVE_PHRASE_RE = re.compile(
    r"(?i)\b(?:you\s+are\s+(?:an?\s+)?(?:idiot|moron|incompetent|useless)|"
    r"shut\s+up|screw\s+you|what\s+an?\s+(?:idiot|moron)|"
    r"(?:idiotic|moronic|stupid)\s+(?:answer|response|thing|model|agent))\b"
)


def source_requires_summary(text: str) -> bool:
    return bool(
        PROFANITY_RE.search(text)
        or OBFUSCATED_PROFANITY_RE.search(text)
        or ABUSIVE_PHRASE_RE.search(text)
    )


EMAIL_RE = re.compile(
    r"(?i)(?<![A-Z0-9._%+-])[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}(?![A-Z0-9.-])"
)
MARKDOWN_WINDOWS_PATH_RE = re.compile(
    r"(?i)\((?:\\\\\?\\)?[A-Z]:[\\/][^\r\n)]*\)"
)
QUOTED_WINDOWS_PATH_RE = re.compile(
    r"(?i)(?P<q>[`\"'])(?:\\\\\?\\)?[A-Z]:[\\/].*?(?P=q)"
)
WINDOWS_PATH_RE = re.compile(
    r"(?i)(?<![A-Z0-9_])(?:\\\\\?\\)?[A-Z]:[\\/][^\s<>\"'`|]+"
)
UNC_PATH_RE = re.compile(r"(?<![\\/])\\\\[^\\/\s]+[\\/][^\s<>\"'`|]+")
POSIX_LOCAL_PATH_RE = re.compile(
    r"(?<![A-Za-z0-9])/(?:Users|home|root|mnt|tmp|private|workspace)(?:/[^\s<>\"'`]+)+"
)
PRIVATE_OVERLEAF_RE = re.compile(
    r"(?i)(?:https?://)?(?:www\.)?overleaf\.com/(?:project|read|join)/[^\s<>\"'`]+"
)
LOCAL_URL_RE = re.compile(
    r"(?i)https?://(?:localhost|127(?:\.\d{1,3}){3}|0\.0\.0\.0|\[?::1\]?)(?::\d+)?[^\s<>\"'`]*"
)
PRIVATE_PROTOCOL_RE = re.compile(
    r"(?i)(?:codex|session|thread|sandbox|app)://[^\s<>\"'`]+"
)
UUID_RE = re.compile(
    r"(?i)(?<![0-9a-f])[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-"
    r"[89ab][0-9a-f]{3}-[0-9a-f]{12}(?![0-9a-f])"
)
SESSION_ID_RE = re.compile(
    r"(?i)\b(?:client[_ -]?thread|conversation|operation|session|thread|host)"
    r"[_ -]?(?:id)?\s*[:=]\s*[\"']?[A-Za-z0-9._:-]{6,}[\"']?"
)
PEM_RE = re.compile(
    r"(?is)-----BEGIN [A-Z0-9 ]*(?:PRIVATE KEY|CERTIFICATE)-----.*?"
    r"-----END [A-Z0-9 ]*(?:PRIVATE KEY|CERTIFICATE)-----"
)
BEARER_RE = re.compile(r"(?i)\bBearer\s+[A-Za-z0-9._~+/=-]{8,}")
CREDENTIAL_ASSIGNMENT_RE = re.compile(
    r"(?i)\b(?:api[_ -]?key|access[_ -]?token|auth[_ -]?token|password|passwd|"
    r"secret|client[_ -]?secret|private[_ -]?key)\s*[:=]\s*[^\s,;]+"
)
TOKEN_SHAPE_RES = (
    re.compile(r"(?<![A-Za-z0-9])sk-[A-Za-z0-9_-]{16,}"),
    re.compile(r"(?<![A-Za-z0-9])gh[pousr]_[A-Za-z0-9]{20,}"),
    re.compile(r"(?<![A-Za-z0-9])AKIA[0-9A-Z]{16}(?![A-Za-z0-9])"),
    re.compile(r"(?<![A-Za-z0-9])AIza[0-9A-Za-z_-]{30,}"),
    re.compile(
        r"(?<![A-Za-z0-9_-])eyJ[A-Za-z0-9_-]{8,}\."
        r"[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}(?![A-Za-z0-9_-])"
    ),
)
HTTP_URL_RE = re.compile(r"(?i)https?://[^\s<>\"'`]+")
# The private source spelling is encoded so the public generator itself does
# not reintroduce the identifier that it is required to redact.
FIRST_NAME_RE = re.compile("\x46\x6c\x6f\x72\x69\x73", re.IGNORECASE)


def replace_count(
    pattern: re.Pattern[str], replacement: str, text: str
) -> tuple[str, int]:
    return pattern.subn(replacement, text)


def url_has_private_query(url: str) -> bool:
    try:
        parsed = urlsplit(url.rstrip(".,;:!?)]}"))
        keys = {key.casefold() for key, _ in parse_qsl(parsed.query, keep_blank_values=True)}
    except ValueError:
        return True
    private_keys = {
        "access_token",
        "api_key",
        "auth",
        "authorization",
        "code",
        "key",
        "password",
        "project",
        "secret",
        "session",
        "share",
        "sig",
        "signature",
        "token",
    }
    return bool(keys & private_keys) or "@" in parsed.netloc


def redact_private_query(match: re.Match[str]) -> str:
    url = match.group(0)
    if not url_has_private_query(url):
        return url
    return "[REDACTED PRIVATE URL]"


def redact_text(text: str) -> tuple[str, Counter[str]]:
    redactions: Counter[str] = Counter()
    text, n = strip_embedded_nonconversation(text)
    redactions["embedded_operational_payload"] += n

    substitutions: tuple[tuple[str, re.Pattern[str], str], ...] = (
        ("private_overleaf_url", PRIVATE_OVERLEAF_RE, "[REDACTED PRIVATE OVERLEAF URL]"),
        ("local_url", LOCAL_URL_RE, "[REDACTED LOCAL URL]"),
        ("private_protocol", PRIVATE_PROTOCOL_RE, "[REDACTED PRIVATE PROTOCOL]"),
        ("pem_material", PEM_RE, "[REDACTED CREDENTIAL MATERIAL]"),
        ("bearer_credential", BEARER_RE, "[REDACTED CREDENTIAL]"),
        ("credential_assignment", CREDENTIAL_ASSIGNMENT_RE, "[REDACTED CREDENTIAL]"),
        ("email", EMAIL_RE, "[REDACTED EMAIL]"),
        ("markdown_windows_path", MARKDOWN_WINDOWS_PATH_RE, "([REDACTED LOCAL PATH])"),
        ("quoted_windows_path", QUOTED_WINDOWS_PATH_RE, "[REDACTED LOCAL PATH]"),
        ("windows_absolute_path", WINDOWS_PATH_RE, "[REDACTED LOCAL PATH]"),
        ("unc_path", UNC_PATH_RE, "[REDACTED LOCAL PATH]"),
        ("posix_local_path", POSIX_LOCAL_PATH_RE, "[REDACTED LOCAL PATH]"),
        ("session_or_thread_id", SESSION_ID_RE, "[REDACTED PRIVATE IDENTIFIER]"),
        ("uuid", UUID_RE, "[REDACTED PRIVATE IDENTIFIER]"),
    )
    for category, pattern, replacement in substitutions:
        text, n = replace_count(pattern, replacement, text)
        redactions[category] += n

    for pattern in TOKEN_SHAPE_RES:
        text, n = replace_count(pattern, "[REDACTED CREDENTIAL]", text)
        redactions["credential_shape"] += n

    text, n = HTTP_URL_RE.subn(redact_private_query, text)
    # subn counts all URL matches, so count only actual replacement markers.
    if n:
        redactions["urls_examined"] += n
    redactions["private_url_query"] += text.count("[REDACTED PRIVATE URL]")

    text, n = FIRST_NAME_RE.subn("the user", text)
    redactions["user_first_name"] += n

    return text.strip(), +redactions


PUBLIC_SCAN_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("user_first_name", FIRST_NAME_RE),
    ("windows_absolute_path", WINDOWS_PATH_RE),
    ("unc_path", UNC_PATH_RE),
    ("posix_local_path", POSIX_LOCAL_PATH_RE),
    ("private_overleaf_url", PRIVATE_OVERLEAF_RE),
    ("local_url", LOCAL_URL_RE),
    ("private_protocol", PRIVATE_PROTOCOL_RE),
    ("email", EMAIL_RE),
    ("uuid", UUID_RE),
    ("session_or_thread_id", SESSION_ID_RE),
    ("pem_material", PEM_RE),
    ("bearer_credential", BEARER_RE),
    ("credential_assignment", CREDENTIAL_ASSIGNMENT_RE),
    ("profanity", PROFANITY_RE),
    ("obfuscated_profanity", OBFUSCATED_PROFANITY_RE),
    ("abusive_phrase", ABUSIVE_PHRASE_RE),
    ("embedded_platform_context", RAW_PLATFORM_MARKER_RE),
)


def scan_public_text(text: str) -> list[str]:
    hits = [name for name, pattern in PUBLIC_SCAN_PATTERNS if pattern.search(text)]
    if any(pattern.search(text) for pattern in TOKEN_SHAPE_RES):
        hits.append("credential_shape")
    for match in HTTP_URL_RE.finditer(text):
        if url_has_private_query(match.group(0)):
            hits.append("private_url_query")
            break
    return sorted(set(hits))


SUMMARY_CERTIFICATIONS = (
    "all_actionable_directives_preserved",
    "all_mathematical_content_preserved",
    "neutral_language",
    "not_a_source_quotation",
    "privacy_reviewed",
)


def load_editorial_summaries(path: Path) -> tuple[dict[int, dict[str, Any]], str]:
    raw = path.read_bytes()
    data = json.loads(raw)
    if data.get("schema") != SUMMARY_SCHEMA:
        raise RuntimeError(f"unexpected editorial-summary schema in {path.name}")
    items = data.get("summaries")
    if not isinstance(items, list):
        raise RuntimeError("editorial summaries must be a list")
    result: dict[int, dict[str, Any]] = {}
    for item in items:
        if not isinstance(item, dict):
            raise RuntimeError("each editorial summary must be an object")
        ordinal = item.get("ordinal")
        if not isinstance(ordinal, int) or ordinal < 0:
            raise RuntimeError("editorial summary ordinal must be a nonnegative integer")
        if ordinal in result:
            raise RuntimeError(f"duplicate editorial summary ordinal: {ordinal}")
        anchor = item.get("source_text_sha256")
        if not isinstance(anchor, str) or not re.fullmatch(r"[0-9a-f]{64}", anchor):
            raise RuntimeError(f"invalid source-text hash for editorial summary {ordinal}")
        summary = item.get("summary")
        if not isinstance(summary, str) or not summary.strip():
            raise RuntimeError(f"empty editorial summary for source event {ordinal}")
        certifications = item.get("certifications")
        if not isinstance(certifications, dict) or any(
            certifications.get(key) is not True for key in SUMMARY_CERTIFICATIONS
        ):
            raise RuntimeError(
                f"editorial summary {ordinal} lacks all required true certifications"
            )
        result[ordinal] = item
    return result, sha256_bytes(raw)


def phase_of(payload: dict[str, Any]) -> str:
    value = payload.get("phase")
    return value if isinstance(value, str) else ""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("source_jsonl", type=Path)
    parser.add_argument("output_directory", type=Path)
    parser.add_argument("--prefix-bytes", type=int, required=True)
    parser.add_argument("--prefix-sha256", required=True)
    parser.add_argument("--summaries", type=Path)
    args = parser.parse_args()

    if args.prefix_bytes <= 0:
        raise RuntimeError("prefix byte count must be positive")
    expected_prefix_sha = args.prefix_sha256.casefold()
    if not re.fullmatch(r"[0-9a-f]{64}", expected_prefix_sha):
        raise RuntimeError("prefix SHA-256 must be 64 lowercase hexadecimal characters")
    if args.source_jsonl.stat().st_size < args.prefix_bytes:
        raise RuntimeError("private source is shorter than the frozen prefix")

    output_dir = args.output_directory.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    summaries_path = (args.summaries or output_dir / SUMMARY_NAME).resolve()
    editorial, summaries_sha = load_editorial_summaries(summaries_path)

    generator_path = Path(__file__).resolve()
    validator_path = generator_path.with_name(VALIDATOR_NAME)
    validator_sha = sha256_file(validator_path) if validator_path.exists() else None

    total_records = 0
    event_types: Counter[str] = Counter()
    response_message_roles: Counter[str] = Counter()
    natural_events_by_role: Counter[str] = Counter()
    phase_counts: Counter[str] = Counter()
    mode_counts: Counter[str] = Counter()
    source_summary_required_by_role: Counter[str] = Counter()
    excluded_role_messages: Counter[str] = Counter()
    redaction_counts: Counter[str] = Counter()
    unresolved_reason_counts: Counter[str] = Counter()
    unresolved_by_role: Counter[str] = Counter()
    used_editorial: set[int] = set()
    ordinal_seen: set[int] = set()
    prior_ordinal = -1
    consumed = 0
    prefix_digest = hashlib.sha256()
    natural_event_count = 0
    nontext_allowed_role_messages = 0
    embedded_only_allowed_role_messages = 0
    unresolved_count = 0

    with tempfile.TemporaryDirectory(
        prefix="complete-conversation-build-", dir=str(output_dir.parent)
    ) as temp_name:
        temp_dir = Path(temp_name)
        edition_tmp = temp_dir / EDITION_NAME
        queue_tmp = temp_dir / QUEUE_NAME

        with (
            args.source_jsonl.open("rb") as source,
            edition_tmp.open("wb") as edition_out,
            queue_tmp.open("wb") as queue_out,
        ):
            while consumed < args.prefix_bytes:
                remaining = args.prefix_bytes - consumed
                raw = source.readline(remaining)
                if not raw:
                    raise RuntimeError("short read inside frozen prefix")
                consumed += len(raw)
                prefix_digest.update(raw)
                if not raw.endswith(b"\n"):
                    raise RuntimeError("frozen prefix ends inside a JSONL record")
                total_records += 1
                try:
                    record = json.loads(raw)
                except (UnicodeDecodeError, json.JSONDecodeError) as exc:
                    raise RuntimeError(
                        f"malformed JSONL record at frozen-prefix record {total_records}"
                    ) from exc
                if not isinstance(record, dict):
                    raise RuntimeError(f"JSONL record {total_records} is not an object")
                record_type = str(record.get("type") or "")
                event_types[record_type] += 1
                if record_type != "response_item":
                    continue
                payload = record.get("payload")
                if not isinstance(payload, dict) or payload.get("type") != "message":
                    continue
                role = str(payload.get("role") or "")
                response_message_roles[role] += 1
                if role not in ALLOWED_ROLES:
                    excluded_role_messages[role or "(empty)"] += 1
                    continue
                blocks = text_blocks(payload)
                if not blocks:
                    nontext_allowed_role_messages += 1
                    continue
                source_text = joined_source_text(blocks)
                natural_text, embedded_count = strip_embedded_nonconversation(source_text)
                if not natural_text or not re.search(r"\w", natural_text, re.UNICODE):
                    embedded_only_allowed_role_messages += 1
                    continue

                ordinal = record.get("ordinal")
                if not isinstance(ordinal, int) or ordinal < 0:
                    raise RuntimeError(
                        f"natural-language message at record {total_records} has invalid ordinal"
                    )
                if ordinal in ordinal_seen or ordinal <= prior_ordinal:
                    raise RuntimeError(f"duplicate or non-increasing source ordinal {ordinal}")
                ordinal_seen.add(ordinal)
                prior_ordinal = ordinal
                timestamp = record.get("timestamp")
                if not isinstance(timestamp, str) or not timestamp:
                    raise RuntimeError(f"source event {ordinal} lacks an exact timestamp string")

                source_sha = sha256_bytes(source_text.encode("utf-8"))
                block_hashes = [sha256_bytes(block.encode("utf-8")) for block in blocks]
                requires_summary = source_requires_summary(natural_text)
                if requires_summary:
                    source_summary_required_by_role[role] += 1
                entry = editorial.get(ordinal)
                reasons: list[str] = []
                mode: str
                public_text: str | None
                event_redactions: Counter[str] = Counter()

                if entry is not None:
                    used_editorial.add(ordinal)
                    if entry["source_text_sha256"] != source_sha:
                        reasons.append("editorial_summary_source_hash_mismatch")
                        public_text = None
                        mode = "unresolved-withheld"
                    else:
                        public_text, event_redactions = redact_text(entry["summary"])
                        mode = "summarized-redacted"
                elif requires_summary:
                    reasons.append("adequate_neutral_summary_required")
                    public_text = None
                    mode = "unresolved-withheld"
                else:
                    # Redact from the full text so embedded-payload removal is
                    # counted consistently; only natural text reaches output.
                    public_text, event_redactions = redact_text(source_text)
                    mode = "verbatim-redacted"

                if public_text is not None:
                    hits = scan_public_text(public_text)
                    if hits:
                        reasons.extend(f"public_scan:{hit}" for hit in hits)
                        public_text = None
                        mode = "unresolved-withheld"
                    elif not public_text or not re.search(r"\w", public_text, re.UNICODE):
                        reasons.append("empty_after_redaction")
                        public_text = None
                        mode = "unresolved-withheld"

                event = {
                    "mode": mode,
                    "ordinal": ordinal,
                    "phase": phase_of(payload),
                    "public_text": public_text,
                    "role": role,
                    "schema": SCHEMA,
                    "source_text_block_count": len(blocks),
                    "source_text_block_sha256": block_hashes,
                    "source_text_sha256": source_sha,
                    "timestamp": timestamp,
                }
                if reasons:
                    event["withheld_reason_codes"] = sorted(set(reasons))
                write_jsonl(edition_out, event)

                natural_event_count += 1
                natural_events_by_role[role] += 1
                phase_counts[f"{role}:{phase_of(payload) or '(empty)'}"] += 1
                mode_counts[mode] += 1
                redaction_counts.update(event_redactions)
                # Account for the first structural pass used only to decide if
                # the event was natural language.  The second pass is the one
                # actually represented in per-event/public redaction totals.
                if embedded_count and not event_redactions["embedded_operational_payload"]:
                    redaction_counts["embedded_operational_payload"] += embedded_count

                if mode == "unresolved-withheld":
                    unresolved_count += 1
                    unresolved_by_role[role] += 1
                    for reason in sorted(set(reasons)):
                        unresolved_reason_counts[reason] += 1
                    queue_item = {
                        "ordinal": ordinal,
                        "reason_codes": sorted(set(reasons)),
                        "role": role,
                        "schema": "s6-complete-conversation-unresolved-queue-v1",
                        "source_text_sha256": source_sha,
                        "timestamp": timestamp,
                    }
                    write_jsonl(queue_out, queue_item)

        if consumed != args.prefix_bytes:
            raise RuntimeError("prefix byte count mismatch")
        actual_prefix_sha = prefix_digest.hexdigest()
        if actual_prefix_sha != expected_prefix_sha:
            raise RuntimeError(
                f"frozen prefix SHA-256 mismatch: {actual_prefix_sha} != {expected_prefix_sha}"
            )

        unused_editorial = sorted(set(editorial) - used_editorial)
        if unused_editorial:
            raise RuntimeError(
                "editorial summaries did not match natural-language source events: "
                + ", ".join(str(value) for value in unused_editorial)
            )

        edition_sha = sha256_file(edition_tmp)
        queue_sha = sha256_file(queue_tmp)
        status = "RELEASE_READY" if unresolved_count == 0 else "NOT_RELEASE_READY"
        safe_to_include = unresolved_count == 0
        status_text = (
            f"{status}\n"
            f"safe_to_include={'true' if safe_to_include else 'false'}\n"
            f"natural_language_events={natural_event_count}\n"
            f"unresolved_events={unresolved_count}\n"
            f"candidate_sha256={edition_sha}\n"
            f"unresolved_queue_sha256={queue_sha}\n"
        )
        status_tmp = temp_dir / STATUS_NAME
        status_tmp.write_bytes(status_text.encode("utf-8"))

        receipt = {
            "counts": {
                "embedded_only_user_assistant_messages_excluded": embedded_only_allowed_role_messages,
                "event_types": dict(sorted(event_types.items())),
                "excluded_developer_or_system_messages": dict(sorted(excluded_role_messages.items())),
                "modes": dict(sorted(mode_counts.items())),
                "natural_language_events": natural_event_count,
                "natural_language_events_by_role": dict(sorted(natural_events_by_role.items())),
                "nontext_user_assistant_messages_excluded": nontext_allowed_role_messages,
                "phases": dict(sorted(phase_counts.items())),
                "redactions": dict(sorted((+redaction_counts).items())),
                "response_message_roles": dict(sorted(response_message_roles.items())),
                "source_records": total_records,
                "source_summary_required_by_role": dict(
                    sorted(source_summary_required_by_role.items())
                ),
                "unresolved_by_role": dict(sorted(unresolved_by_role.items())),
                "unresolved_events": unresolved_count,
                "unresolved_reason_codes": dict(sorted(unresolved_reason_counts.items())),
            },
            "editorial_summaries": {
                "anchored_summary_count": len(editorial),
                "required_certifications": list(SUMMARY_CERTIFICATIONS),
                "sha256": summaries_sha,
            },
            "generator": {
                "filename": generator_path.name,
                "sha256": sha256_file(generator_path),
                "version": VERSION,
            },
            "outputs": {
                "candidate": {
                    "bytes": edition_tmp.stat().st_size,
                    "filename": EDITION_NAME,
                    "sha256": edition_sha,
                },
                "release_status": {
                    "bytes": status_tmp.stat().st_size,
                    "filename": STATUS_NAME,
                    "sha256": sha256_file(status_tmp),
                },
                "unresolved_queue": {
                    "bytes": queue_tmp.stat().st_size,
                    "filename": QUEUE_NAME,
                    "sha256": queue_sha,
                },
            },
            "privacy_confirmations": {
                "candidate_contains_no_private_source_jsonl": True,
                "candidate_public_text_scan_passed_for_all_nonwithheld_events": True,
                "raw_system_developer_tool_and_state_payloads_excluded": True,
                "unresolved_queue_contains_source_text": False,
            },
            "release": {
                "safe_to_include": safe_to_include,
                "status": status,
                "unresolved_event_count": unresolved_count,
                "validator_must_pass_before_inclusion": True,
            },
            "schema": RECEIPT_SCHEMA,
            "source": {
                "frozen_prefix_bytes": args.prefix_bytes,
                "frozen_prefix_sha256": actual_prefix_sha,
                "label": "private Codex session; frozen newline-terminated prefix",
                "newline_terminated": True,
                "raw_source_deposited": False,
                "source_text_hash_definition": (
                    "SHA-256 of UTF-8 encoding of decoded text blocks joined in source order "
                    "by one U+000A; per-block hashes are also retained"
                ),
            },
            "validator": {
                "filename": validator_path.name,
                "sha256": validator_sha,
            },
        }
        receipt_tmp = temp_dir / RECEIPT_NAME
        receipt_tmp.write_bytes(
            json.dumps(receipt, ensure_ascii=False, indent=2, sort_keys=True).encode("utf-8")
            + b"\n"
        )

        for name in (EDITION_NAME, QUEUE_NAME, STATUS_NAME, RECEIPT_NAME):
            os.replace(temp_dir / name, output_dir / name)

    print(
        json.dumps(
            {
                "candidate_sha256": edition_sha,
                "natural_language_events": natural_event_count,
                "safe_to_include": safe_to_include,
                "status": status,
                "unresolved_events": unresolved_count,
            },
            sort_keys=True,
        )
    )
    return 0 if safe_to_include else 2


if __name__ == "__main__":
    raise SystemExit(main())
