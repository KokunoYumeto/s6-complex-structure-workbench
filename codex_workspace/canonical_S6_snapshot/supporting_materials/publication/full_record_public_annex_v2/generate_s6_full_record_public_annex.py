#!/usr/bin/env python3
"""Generate a conservative typed public ledger from a frozen S6 rollout prefix.

The raw rollout is never copied. User and assistant conversation messages are
redacted under a fail-closed policy. Relevant tool calls and outputs are retained
as typed, source-hash-anchored evidence profiles: tool names, pairing, sizes,
safe execution scalars, structural shapes, and risk flags survive, while raw
commands, prompts, local paths, identifiers, images, and output text do not.
"""

from __future__ import annotations

import argparse
from collections import Counter
import gzip
import hashlib
import json
from pathlib import Path
import re
import shutil
import tempfile
from typing import Any, BinaryIO, Iterable
from urllib.parse import parse_qsl, urlsplit


VERSION = "2.0.0"
SCHEMA = "s6-full-record-public-annex-v2"
SUMMARY_SCHEMA = "s6-complete-conversation-editorial-summaries-v1"
EDITION_NAME = "s6_full_record_public_annex_v2.jsonl"
GZIP_NAME = EDITION_NAME + ".gz"
QUEUE_NAME = "s6_full_record_public_annex_v2_unresolved_queue.jsonl"
SUMMARY_NAME = "s6_full_record_public_annex_v2_editorial_summaries.json"
RECEIPT_NAME = "s6_full_record_public_annex_v2_receipt.json"
INVENTORY_NAME = "s6_full_record_public_annex_v2_inventory.json"
STATUS_NAME = "s6_full_record_public_annex_v2_status.txt"
README_NAME = "README_PUBLIC_ANNEX_V2.md"
GENERATOR_COPY_NAME = "generate_s6_full_record_public_annex.py"
VALIDATOR_COPY_NAME = "validate_s6_full_record_public_annex.py"

TEXT_BLOCK_TYPES = frozenset({"input_text", "output_text", "text"})
ALLOWED_MESSAGE_ROLES = frozenset({"user", "assistant"})
SUMMARY_CERTIFICATIONS = (
    "all_actionable_directives_preserved",
    "all_mathematical_content_preserved",
    "neutral_language",
    "not_a_source_quotation",
    "privacy_reviewed",
)


def canonical_json_bytes(value: Any) -> bytes:
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"), sort_keys=True).encode("utf-8")


def pretty_json_bytes(value: Any) -> bytes:
    return json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True).encode("utf-8") + b"\n"


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(8 * 1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def write_jsonl(handle: BinaryIO, value: Any) -> None:
    handle.write(canonical_json_bytes(value) + b"\n")


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
    r"(?is)<(?:" + "|".join(re.escape(tag) for tag in EMBEDDED_BLOCK_TAGS)
    + r")\b[^>]*>.*?</(?:" + "|".join(re.escape(tag) for tag in EMBEDDED_BLOCK_TAGS) + r")\s*>"
)
AGENTS_CONTEXT_RE = re.compile(
    r"(?ims)^#\s*AGENTS\.md instructions for[^\r\n]*\r?\n(?:<INSTRUCTIONS>.*?</INSTRUCTIONS>\s*)?"
)
ORPHAN_CONTEXT_TAG_RE = re.compile(
    r"(?is)</?(?:" + "|".join(re.escape(tag) for tag in EMBEDDED_BLOCK_TAGS) + r")\b[^>]*>"
)
RAW_PLATFORM_MARKER_RE = re.compile(
    r"(?im)(?:</?(?:" + "|".join(re.escape(tag) for tag in EMBEDDED_BLOCK_TAGS)
    + r")\b|^#\s*AGENTS\.md instructions for)"
)


def strip_embedded_nonconversation(text: str) -> tuple[str, int]:
    count = 0

    def remove(_: re.Match[str]) -> str:
        nonlocal count
        count += 1
        return "\n"

    text = EMBEDDED_BLOCK_RE.sub(remove, text)
    text = AGENTS_CONTEXT_RE.sub(remove, text)
    text, orphan_count = ORPHAN_CONTEXT_TAG_RE.subn("", text)
    return text.strip(), count + orphan_count


def decoded_terms(hex_values: Iterable[str]) -> tuple[str, ...]:
    return tuple(bytes.fromhex(value).decode("ascii") for value in hex_values)


# Encoded so public scripts do not reproduce the words the public data forbids.
PROFANITY_TERMS = decoded_terms(
    (
        "617373686f6c65", "62617374617264", "6269746368", "62756c6c73686974",
        "63726170", "63756e74", "64616d6e", "6469636b", "6675636b", "6675636b6564",
        "6675636b6572", "6675636b657273", "6675636b696e67", "676f6464616d6e",
        "68656c6c", "6d6f746865726675636b6572", "6d6f746865726675636b657273",
        "70697373", "726574617264", "7265746172646564", "73686974", "736869747479",
    )
)
PROFANITY_RE = re.compile(
    r"(?i)(?<![A-Za-z0-9_])(?:" + "|".join(re.escape(term) for term in sorted(PROFANITY_TERMS, key=len, reverse=True))
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

EMAIL_RE = re.compile(r"(?i)(?<![A-Z0-9._%+-])[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}(?![A-Z0-9.-])")
MARKDOWN_WINDOWS_PATH_RE = re.compile(r"(?i)\((?:\\\\\?\\)?[A-Z]:[\\/][^\r\n)]*\)")
QUOTED_WINDOWS_PATH_RE = re.compile(r"(?i)(?P<q>[`\"'])(?:\\\\\?\\)?[A-Z]:[\\/].*?(?P=q)")
WINDOWS_PATH_RE = re.compile(r"(?i)(?<![A-Z0-9_])(?:\\\\\?\\)?[A-Z]:[\\/][^\s<>\"'`|]+")
UNC_PATH_RE = re.compile(r"(?<![\\/])\\\\[^\\/\s]+[\\/][^\s<>\"'`|]+")
POSIX_LOCAL_PATH_RE = re.compile(r"(?<![A-Za-z0-9])/(?:Users|home|root|mnt|tmp|private|workspace)(?:/[^\s<>\"'`]+)+")
PRIVATE_OVERLEAF_RE = re.compile(r"(?i)(?:https?://)?(?:www\.)?overleaf\.com/(?:project|read|join)/[^\s<>\"'`]+")
PRIVATE_EDIT_URL_RE = re.compile(r"(?i)https?://[^\s<>\"'`]+/(?:edit|join|project|deposit|uploads?)(?:[/?#][^\s<>\"'`]*)?")
LOCAL_URL_RE = re.compile(r"(?i)https?://(?:localhost|127(?:\.\d{1,3}){3}|0\.0\.0\.0|\[?::1\]?)(?::\d+)?[^\s<>\"'`]*")
PRIVATE_PROTOCOL_RE = re.compile(r"(?i)(?:codex|session|thread|sandbox|app)://[^\s<>\"'`]+")
UUID_RE = re.compile(r"(?i)(?<![0-9a-f])[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}(?![0-9a-f])")
OPAQUE_IDENTIFIER_RE = re.compile(r"(?i)(?<![0-9a-f])[0-9a-f]{24,40}(?![0-9a-f])")
LABELED_ID_RE = re.compile(
    r"(?i)\b(?:client[_ -]?thread|conversation|operation|session|thread|host|project|call|idempotency)"
    r"[_ -]?(?:id|key)?\s*[:=]\s*[\"']?[A-Za-z0-9._:-]{6,}[\"']?"
)
PEM_RE = re.compile(r"(?is)-----BEGIN [A-Z0-9 ]*(?:PRIVATE KEY|CERTIFICATE)-----.*?-----END [A-Z0-9 ]*(?:PRIVATE KEY|CERTIFICATE)-----")
BEARER_RE = re.compile(r"(?i)\bBearer\s+[A-Za-z0-9._~+/=-]{8,}")
CREDENTIAL_ASSIGNMENT_RE = re.compile(
    r"(?i)\b(?:api[_ -]?key|access[_ -]?token|auth[_ -]?token|password|passwd|secret|"
    r"client[_ -]?secret|private[_ -]?key|idempotency[_ -]?key)\s*[:=]\s*[^\s,;]+"
)
ENV_SECRET_RE = re.compile(
    r"(?im)\b[A-Z][A-Z0-9_]*(?:TOKEN|SECRET|PASSWORD|PASSWD|API_KEY|PRIVATE_KEY)[A-Z0-9_]*\s*=\s*[^\s;]+"
)
PHONE_RE = re.compile(r"(?<!\d)\+\d[\d .()-]{8,}\d(?!\d)")
PRIVATE_IP_RE = re.compile(r"(?<!\d)(?:10(?:\.\d{1,3}){3}|192\.168(?:\.\d{1,3}){2}|172\.(?:1[6-9]|2\d|3[01])(?:\.\d{1,3}){2})(?!\d)")
LONG_BASE64_RE = re.compile(r"(?<![A-Za-z0-9+/=])[A-Za-z0-9+/]{128,}={0,2}(?![A-Za-z0-9+/=])")
TOKEN_SHAPE_RES = (
    re.compile(r"(?<![A-Za-z0-9])sk-[A-Za-z0-9_-]{16,}"),
    re.compile(r"(?<![A-Za-z0-9])gh[pousr]_[A-Za-z0-9]{20,}"),
    re.compile(r"(?<![A-Za-z0-9])AKIA[0-9A-Z]{16}(?![A-Za-z0-9])"),
    re.compile(r"(?<![A-Za-z0-9])AIza[0-9A-Za-z_-]{30,}"),
    re.compile(r"(?<![A-Za-z0-9_-])eyJ[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}(?![A-Za-z0-9_-])"),
)
HTTP_URL_RE = re.compile(r"(?i)https?://[^\s<>\"'`]+")
FIRST_NAME_RE = re.compile(bytes.fromhex("466c6f726973").decode("ascii"), re.IGNORECASE)


def url_has_private_query(url: str) -> bool:
    try:
        parsed = urlsplit(url.rstrip(".,;:!?)]}"))
        keys = {key.casefold() for key, _ in parse_qsl(parsed.query, keep_blank_values=True)}
    except ValueError:
        return True
    private_keys = {"access_token", "api_key", "auth", "authorization", "code", "key", "password", "project", "secret", "session", "share", "sig", "signature", "token"}
    return bool(keys & private_keys) or "@" in parsed.netloc


def source_requires_summary(text: str) -> bool:
    return bool(PROFANITY_RE.search(text) or OBFUSCATED_PROFANITY_RE.search(text) or ABUSIVE_PHRASE_RE.search(text))


def materially_private_source(text: str) -> bool:
    return bool(
        PEM_RE.search(text) or BEARER_RE.search(text) or CREDENTIAL_ASSIGNMENT_RE.search(text)
        or ENV_SECRET_RE.search(text) or any(pattern.search(text) for pattern in TOKEN_SHAPE_RES)
    )


def redact_text(text: str, redact_profanity: bool = False) -> tuple[str, Counter[str]]:
    counts: Counter[str] = Counter()
    text, embedded = strip_embedded_nonconversation(text)
    counts["embedded_operational_payload"] += embedded
    substitutions: tuple[tuple[str, re.Pattern[str], str], ...] = (
        ("private_overleaf_url", PRIVATE_OVERLEAF_RE, "[REDACTED PRIVATE URL]"),
        ("private_edit_url", PRIVATE_EDIT_URL_RE, "[REDACTED PRIVATE URL]"),
        ("local_url", LOCAL_URL_RE, "[REDACTED LOCAL URL]"),
        ("private_protocol", PRIVATE_PROTOCOL_RE, "[REDACTED PRIVATE PROTOCOL]"),
        ("pem_material", PEM_RE, "[REDACTED CREDENTIAL MATERIAL]"),
        ("bearer_credential", BEARER_RE, "[REDACTED CREDENTIAL]"),
        ("credential_assignment", CREDENTIAL_ASSIGNMENT_RE, "[REDACTED CREDENTIAL]"),
        ("environment_secret", ENV_SECRET_RE, "[REDACTED CREDENTIAL]"),
        ("email", EMAIL_RE, "[REDACTED EMAIL]"),
        ("markdown_windows_path", MARKDOWN_WINDOWS_PATH_RE, "([REDACTED LOCAL PATH])"),
        ("quoted_windows_path", QUOTED_WINDOWS_PATH_RE, "[REDACTED LOCAL PATH]"),
        ("windows_absolute_path", WINDOWS_PATH_RE, "[REDACTED LOCAL PATH]"),
        ("unc_path", UNC_PATH_RE, "[REDACTED LOCAL PATH]"),
        ("posix_local_path", POSIX_LOCAL_PATH_RE, "[REDACTED LOCAL PATH]"),
        ("labeled_private_identifier", LABELED_ID_RE, "[REDACTED PRIVATE IDENTIFIER]"),
        ("uuid", UUID_RE, "[REDACTED PRIVATE IDENTIFIER]"),
        ("opaque_private_identifier", OPAQUE_IDENTIFIER_RE, "[REDACTED PRIVATE IDENTIFIER]"),
        ("private_ip", PRIVATE_IP_RE, "[REDACTED PRIVATE NETWORK ADDRESS]"),
        ("phone", PHONE_RE, "[REDACTED PHONE]"),
        ("long_encoded_blob", LONG_BASE64_RE, "[REDACTED ENCODED DATA]"),
    )
    for category, pattern, replacement in substitutions:
        text, amount = pattern.subn(replacement, text)
        counts[category] += amount
    for pattern in TOKEN_SHAPE_RES:
        text, amount = pattern.subn("[REDACTED CREDENTIAL]", text)
        counts["credential_shape"] += amount

    def redact_private_query(match: re.Match[str]) -> str:
        return "[REDACTED PRIVATE URL]" if url_has_private_query(match.group(0)) else match.group(0)

    text, examined = HTTP_URL_RE.subn(redact_private_query, text)
    counts["urls_examined"] += examined
    text, amount = FIRST_NAME_RE.subn("the user", text)
    counts["user_first_name"] += amount
    if redact_profanity:
        text, amount = PROFANITY_RE.subn("[REDACTED PROFANITY]", text)
        counts["profanity"] += amount
        text, amount = OBFUSCATED_PROFANITY_RE.subn("[REDACTED PROFANITY]", text)
        counts["obfuscated_profanity"] += amount
        text, amount = ABUSIVE_PHRASE_RE.subn("[REDACTED ABUSIVE PHRASE]", text)
        counts["abusive_phrase"] += amount
    return text.strip(), +counts


PUBLIC_SCAN_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("user_first_name", FIRST_NAME_RE), ("windows_absolute_path", WINDOWS_PATH_RE),
    ("unc_path", UNC_PATH_RE), ("posix_local_path", POSIX_LOCAL_PATH_RE),
    ("private_overleaf_url", PRIVATE_OVERLEAF_RE), ("private_edit_url", PRIVATE_EDIT_URL_RE),
    ("local_url", LOCAL_URL_RE), ("private_protocol", PRIVATE_PROTOCOL_RE), ("email", EMAIL_RE),
    ("uuid", UUID_RE), ("labeled_private_identifier", LABELED_ID_RE), ("pem_material", PEM_RE),
    ("opaque_private_identifier", OPAQUE_IDENTIFIER_RE),
    ("bearer_credential", BEARER_RE), ("credential_assignment", CREDENTIAL_ASSIGNMENT_RE),
    ("environment_secret", ENV_SECRET_RE), ("private_ip", PRIVATE_IP_RE), ("phone", PHONE_RE),
    ("long_encoded_blob", LONG_BASE64_RE), ("profanity", PROFANITY_RE),
    ("obfuscated_profanity", OBFUSCATED_PROFANITY_RE), ("abusive_phrase", ABUSIVE_PHRASE_RE),
    ("embedded_platform_context", RAW_PLATFORM_MARKER_RE),
)


def scan_public_text(text: str) -> list[str]:
    hits = [name for name, pattern in PUBLIC_SCAN_PATTERNS if pattern.search(text)]
    if any(pattern.search(text) for pattern in TOKEN_SHAPE_RES):
        hits.append("credential_shape")
    if any(url_has_private_query(match.group(0)) for match in HTTP_URL_RE.finditer(text)):
        hits.append("private_url_query")
    return sorted(set(hits))


def source_risk_flags(text: str) -> list[str]:
    checks = (
        ("contains_first_name", FIRST_NAME_RE), ("contains_local_path", WINDOWS_PATH_RE),
        ("contains_local_path", POSIX_LOCAL_PATH_RE), ("contains_private_url", PRIVATE_OVERLEAF_RE),
        ("contains_private_url", PRIVATE_EDIT_URL_RE), ("contains_private_protocol", PRIVATE_PROTOCOL_RE),
        ("contains_private_identifier", UUID_RE), ("contains_credential_shape", CREDENTIAL_ASSIGNMENT_RE),
        ("contains_private_identifier", OPAQUE_IDENTIFIER_RE),
        ("contains_environment_secret", ENV_SECRET_RE), ("contains_email", EMAIL_RE),
        ("contains_profanity", PROFANITY_RE), ("contains_encoded_blob", LONG_BASE64_RE),
    )
    flags = {name for name, pattern in checks if pattern.search(text)}
    if any(pattern.search(text) for pattern in TOKEN_SHAPE_RES):
        flags.add("contains_credential_shape")
    return sorted(flags)


def content_profile(text: str) -> dict[str, Any]:
    return {
        "characters": len(text),
        "lines": text.count("\n") + (1 if text else 0),
        "source_content_sha256": sha256_bytes(text.encode("utf-8")),
        "utf8_bytes": len(text.encode("utf-8")),
        "source_risk_flags": source_risk_flags(text),
    }


SAFE_SCALAR_KEYS = frozenset(
    {
        "archived", "bytes", "count", "detail", "duration", "error_count", "exit_code",
        "fn", "includeoutputs", "kind", "limit", "max_output_chars", "max_output_tokens",
        "mode", "model", "notificationpolicy", "num_games", "original_token_count", "passed",
        "placement", "reasoning_effort", "recency", "response_length", "safe_to_include", "status",
        "thinking", "timeoutms", "turnlimit", "type", "wall_time_seconds", "yield_time_ms",
    }
)
SENSITIVE_KEY_RE = re.compile(r"(?i)(?:id|key|token|secret|pass|path|url|prompt|message|command|cmd|input|output|text|content|data|image|audio|target|project|thread|host|session)")
SAFE_ENUM_RE = re.compile(r"[A-Za-z0-9_.:-]{1,64}")


def safe_scalar_projection(value: Any, depth: int = 0) -> Any:
    if depth > 6:
        return None
    if isinstance(value, dict):
        result: dict[str, Any] = {}
        for raw_key in sorted(value, key=lambda item: str(item)):
            key = str(raw_key)
            child = value[raw_key]
            folded = key.casefold()
            if folded in SAFE_SCALAR_KEYS and not SENSITIVE_KEY_RE.search(key):
                if isinstance(child, bool) or child is None:
                    result[key] = child
                elif isinstance(child, (int, float)) and not isinstance(child, bool):
                    result[key] = child
                elif isinstance(child, str) and SAFE_ENUM_RE.fullmatch(child) and not scan_public_text(child):
                    result[key] = child
            elif isinstance(child, (dict, list)) and not SENSITIVE_KEY_RE.search(key):
                projected = safe_scalar_projection(child, depth + 1)
                if projected not in (None, {}, []):
                    result[key] = projected
        return result
    if isinstance(value, list):
        projected_items = [safe_scalar_projection(item, depth + 1) for item in value[:64]]
        return [item for item in projected_items if item not in (None, {}, [])]
    return None


def safe_structure(value: Any) -> dict[str, Any]:
    if isinstance(value, dict):
        safe_keys = [
            str(key) for key in sorted(value, key=lambda item: str(item))
            if re.fullmatch(r"[A-Za-z_][A-Za-z0-9_.-]{0,63}", str(key))
            and not FIRST_NAME_RE.search(str(key))
        ]
        return {"container": "object", "key_count": len(value), "keys": safe_keys[:128]}
    if isinstance(value, list):
        return {"container": "array", "item_count": len(value)}
    return {"container": type(value).__name__}


NESTED_TOOL_RE = re.compile(r"\btools\.([A-Za-z_][A-Za-z0-9_]*)")
SHELL_TAG_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("archive", re.compile(r"(?i)\b(?:Compress-Archive|zip|tar)\b")),
    ("browser_or_web", re.compile(r"(?i)\b(?:web__run|Invoke-WebRequest|curl)\b")),
    ("file_hash", re.compile(r"(?i)\b(?:Get-FileHash|sha256|hashlib)\b")),
    ("file_inventory", re.compile(r"(?i)\b(?:Get-ChildItem|rg\s+--files)\b")),
    ("file_read", re.compile(r"(?i)\b(?:Get-Content|read_text|read_bytes)\b")),
    ("file_search", re.compile(r"(?i)(?:\brg\b|Select-String)")),
    ("git", re.compile(r"(?i)\bgit\b")),
    ("python", re.compile(r"(?i)\bpython(?:3)?\b")),
    ("tex_build", re.compile(r"(?i)\b(?:latexmk|pdflatex|xelatex|lualatex)\b")),
    ("workspace_edit", re.compile(r"(?i)\bapply_patch\b")),
)


def summarize_tool_argument(tool_name: str, value: Any) -> dict[str, Any]:
    if not isinstance(value, str):
        encoded = canonical_json_bytes(value)
        profile = content_profile(encoded.decode("utf-8", errors="replace"))
        profile["encoding"] = "json-value"
        return profile
    profile = content_profile(value)
    parsed: Any = None
    try:
        parsed = json.loads(value)
    except json.JSONDecodeError:
        pass
    if parsed is not None:
        profile["encoding"] = "json"
        profile["structure"] = safe_structure(parsed)
        projection = safe_scalar_projection(parsed)
        if projection not in (None, {}, []):
            profile["safe_scalar_projection"] = projection
    else:
        profile["encoding"] = "source-text"
    if tool_name == "exec" or "tools." in value:
        profile["nested_tool_names"] = sorted(set(NESTED_TOOL_RE.findall(value)))
        profile["operation_tags"] = [name for name, pattern in SHELL_TAG_PATTERNS if pattern.search(value)]
    return profile


def summarize_output_value(value: Any) -> dict[str, Any]:
    if isinstance(value, str):
        profile = content_profile(value)
        profile["representation"] = "text"
        try:
            parsed = json.loads(value)
        except json.JSONDecodeError:
            parsed = None
        if parsed is not None:
            profile["parsed_structure"] = safe_structure(parsed)
            projection = safe_scalar_projection(parsed)
            if projection not in (None, {}, []):
                profile["safe_scalar_projection"] = projection
        return profile
    if isinstance(value, list):
        blocks: list[dict[str, Any]] = []
        for block in value:
            if not isinstance(block, dict):
                blocks.append({"block_type": type(block).__name__})
                continue
            block_type = str(block.get("type") or "(empty)")
            public_block: dict[str, Any] = {"block_type": block_type}
            text = block.get("text")
            if isinstance(text, str):
                public_block.update(content_profile(text))
                try:
                    parsed = json.loads(text)
                except json.JSONDecodeError:
                    parsed = None
                if parsed is not None:
                    public_block["parsed_structure"] = safe_structure(parsed)
                    projection = safe_scalar_projection(parsed)
                    if projection not in (None, {}, []):
                        public_block["safe_scalar_projection"] = projection
            image_url = block.get("image_url")
            if isinstance(image_url, str):
                public_block["image_reference_characters"] = len(image_url)
                public_block["image_reference_sha256"] = sha256_bytes(image_url.encode("utf-8"))
                public_block["media_type"] = image_url[5:].split(";", 1)[0] if image_url.startswith("data:") else "redacted-reference"
            blocks.append(public_block)
        return {"representation": "content-block-list", "block_count": len(value), "blocks": blocks}
    encoded = canonical_json_bytes(value)
    return {
        "representation": type(value).__name__, "utf8_bytes": len(encoded),
        "source_content_sha256": sha256_bytes(encoded), "structure": safe_structure(value),
    }


def load_summaries(paths: list[Path]) -> tuple[dict[int, dict[str, Any]], bytes]:
    merged: dict[int, dict[str, Any]] = {}
    for path in paths:
        data = json.loads(path.read_bytes())
        if data.get("schema") != SUMMARY_SCHEMA or not isinstance(data.get("summaries"), list):
            raise RuntimeError(f"invalid editorial summary file: {path}")
        for item in data["summaries"]:
            if not isinstance(item, dict):
                raise RuntimeError("summary entry is not an object")
            ordinal = item.get("ordinal")
            anchor = item.get("source_text_sha256")
            summary = item.get("summary")
            certifications = item.get("certifications")
            if not isinstance(ordinal, int) or ordinal < 0 or ordinal in merged:
                raise RuntimeError(f"invalid or duplicate summary ordinal: {ordinal}")
            if not isinstance(anchor, str) or not re.fullmatch(r"[0-9a-f]{64}", anchor):
                raise RuntimeError(f"invalid summary anchor: {ordinal}")
            if not isinstance(summary, str) or not summary.strip() or scan_public_text(summary):
                raise RuntimeError(f"unsafe or empty editorial summary: {ordinal}")
            if not isinstance(certifications, dict) or any(certifications.get(key) is not True for key in SUMMARY_CERTIFICATIONS):
                raise RuntimeError(f"incomplete summary certification: {ordinal}")
            merged[ordinal] = item
    merged_value = {"schema": SUMMARY_SCHEMA, "summaries": [merged[key] for key in sorted(merged)]}
    return merged, pretty_json_bytes(merged_value)


def copy_public_scripts(output_dir: Path) -> None:
    generator = Path(__file__).resolve()
    validator = generator.with_name(VALIDATOR_COPY_NAME)
    shutil.copyfile(generator, output_dir / GENERATOR_COPY_NAME)
    if not validator.exists():
        raise RuntimeError(f"validator not found beside generator: {validator.name}")
    shutil.copyfile(validator, output_dir / VALIDATOR_COPY_NAME)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("source_jsonl", type=Path)
    parser.add_argument("output_directory", type=Path)
    parser.add_argument("--prefix-bytes", type=int, required=True)
    parser.add_argument("--prefix-sha256", required=True)
    parser.add_argument("--summaries", type=Path, action="append", required=True)
    args = parser.parse_args()
    if args.prefix_bytes <= 0 or not re.fullmatch(r"[0-9a-f]{64}", args.prefix_sha256):
        raise RuntimeError("invalid frozen prefix specification")
    if args.source_jsonl.stat().st_size < args.prefix_bytes:
        raise RuntimeError("source shorter than frozen prefix")

    editorial, merged_summary_bytes = load_summaries([path.resolve() for path in args.summaries])
    output_dir = args.output_directory.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    generator_path = Path(__file__).resolve()
    validator_path = generator_path.with_name(VALIDATOR_COPY_NAME)

    record_types: Counter[str] = Counter()
    response_types: Counter[str] = Counter()
    selected_kinds: Counter[str] = Counter()
    excluded_reasons: Counter[str] = Counter()
    modes: Counter[str] = Counter()
    redactions: Counter[str] = Counter()
    risk_flags: Counter[str] = Counter()
    tool_names: Counter[str] = Counter()
    used_summaries: set[int] = set()
    unresolved: list[dict[str, Any]] = []
    call_id_to_ref: dict[str, str] = {}
    call_ref_counter = 0
    paired_outputs = 0
    orphan_outputs = 0
    source_records = 0
    selected_events = 0
    consumed = 0
    prefix_digest = hashlib.sha256()
    prior_selected_ordinal = -1
    source_first_timestamp = None
    source_last_timestamp = None
    source_max_record_bytes = 0

    with tempfile.TemporaryDirectory(prefix="s6-public-annex-v2-", dir=str(output_dir.parent)) as temp_name:
        temp_dir = Path(temp_name)
        edition_tmp = temp_dir / EDITION_NAME
        queue_tmp = temp_dir / QUEUE_NAME
        with args.source_jsonl.open("rb") as source, edition_tmp.open("wb") as edition:
            while consumed < args.prefix_bytes:
                raw = source.readline(args.prefix_bytes - consumed)
                if not raw or not raw.endswith(b"\n"):
                    raise RuntimeError("frozen prefix ends inside a JSONL record")
                consumed += len(raw)
                prefix_digest.update(raw)
                source_records += 1
                source_max_record_bytes = max(source_max_record_bytes, len(raw))
                try:
                    record = json.loads(raw)
                except (UnicodeDecodeError, json.JSONDecodeError) as exc:
                    raise RuntimeError(f"malformed source record {source_records}") from exc
                if not isinstance(record, dict):
                    raise RuntimeError(f"source record {source_records} is not an object")
                record_type = str(record.get("type") or "(empty)")
                record_types[record_type] += 1
                timestamp = record.get("timestamp")
                if isinstance(timestamp, str):
                    source_first_timestamp = source_first_timestamp or timestamp
                    source_last_timestamp = timestamp
                if record_type != "response_item":
                    excluded_reasons[f"record_type:{record_type}"] += 1
                    continue
                payload = record.get("payload")
                if not isinstance(payload, dict):
                    excluded_reasons["response_item_without_object_payload"] += 1
                    continue
                payload_type = str(payload.get("type") or "(empty)")
                response_types[payload_type] += 1
                if payload_type == "reasoning":
                    excluded_reasons["encrypted_or_private_reasoning"] += 1
                    continue
                ordinal = record.get("ordinal")
                if not isinstance(ordinal, int) or ordinal < 0:
                    raise RuntimeError(f"selected response record lacks valid ordinal at record {source_records}")
                if not isinstance(timestamp, str) or not timestamp:
                    raise RuntimeError(f"selected response record lacks timestamp at ordinal {ordinal}")
                source_record_hash = sha256_bytes(raw)
                event: dict[str, Any] | None = None

                if payload_type == "message":
                    role = str(payload.get("role") or "")
                    if role not in ALLOWED_MESSAGE_ROLES:
                        excluded_reasons[f"message_role:{role or '(empty)'}"] += 1
                        continue
                    blocks = text_blocks(payload)
                    if not blocks:
                        excluded_reasons["message_without_text"] += 1
                        continue
                    source_text = "\n".join(blocks)
                    natural_text, embedded_count = strip_embedded_nonconversation(source_text)
                    if not natural_text or not re.search(r"\w", natural_text, re.UNICODE):
                        excluded_reasons["embedded_platform_only_message"] += 1
                        continue
                    source_text_hash = sha256_bytes(source_text.encode("utf-8"))
                    summary_required = role == "user" and (
                        source_requires_summary(natural_text) or materially_private_source(natural_text)
                    )
                    summary_entry = editorial.get(ordinal)
                    reasons: list[str] = []
                    if summary_entry is not None:
                        used_summaries.add(ordinal)
                        if summary_entry["source_text_sha256"] != source_text_hash:
                            public_text = None
                            mode = "unresolved-withheld"
                            reasons.append("summary_source_hash_mismatch")
                        else:
                            public_text, event_redactions = redact_text(summary_entry["summary"], redact_profanity=False)
                            redactions.update(event_redactions)
                            mode = "summarized-redacted"
                    elif summary_required:
                        public_text = None
                        mode = "unresolved-withheld"
                        reasons.append("certified_neutral_summary_required")
                    else:
                        public_text, event_redactions = redact_text(source_text, redact_profanity=(role == "assistant"))
                        redactions.update(event_redactions)
                        mode = "verbatim-redacted"
                    if public_text is not None:
                        hits = scan_public_text(public_text)
                        if hits:
                            reasons.extend(f"public_scan:{hit}" for hit in hits)
                            public_text = None
                            mode = "unresolved-withheld"
                        elif not public_text or not re.search(r"\w", public_text, re.UNICODE):
                            public_text = None
                            mode = "unresolved-withheld"
                            reasons.append("empty_after_redaction")
                    event = {
                        "event_kind": "conversation_message",
                        "mode": mode,
                        "ordinal": ordinal,
                        "phase": payload.get("phase") if isinstance(payload.get("phase"), str) else "",
                        "public_text": public_text,
                        "role": role,
                        "schema": SCHEMA,
                        "source_record_sha256": source_record_hash,
                        "source_text_block_count": len(blocks),
                        "source_text_block_sha256": [sha256_bytes(block.encode("utf-8")) for block in blocks],
                        "source_text_sha256": source_text_hash,
                        "timestamp": timestamp,
                    }
                    if embedded_count:
                        event["embedded_platform_blocks_removed"] = embedded_count
                    if reasons:
                        event["withheld_reason_codes"] = sorted(set(reasons))
                    if mode == "unresolved-withheld":
                        unresolved.append({
                            "event_kind": "conversation_message", "ordinal": ordinal,
                            "reason_codes": sorted(set(reasons)), "role": role,
                            "source_record_sha256": source_record_hash,
                            "source_text_sha256": source_text_hash, "timestamp": timestamp,
                        })

                elif payload_type in {"function_call", "custom_tool_call"}:
                    raw_name = str(payload.get("name") or "(empty)")
                    public_name, name_redactions = redact_text(raw_name, redact_profanity=True)
                    if scan_public_text(public_name) or not re.fullmatch(r"[A-Za-z0-9_.:-]{1,160}", public_name):
                        public_name = "[REDACTED TOOL NAME]"
                        name_redactions["tool_name"] += 1
                    redactions.update(name_redactions)
                    argument_value = payload.get("arguments") if "arguments" in payload else payload.get("input")
                    argument_summary = summarize_tool_argument(public_name, argument_value)
                    for flag in argument_summary.get("source_risk_flags", []):
                        risk_flags[f"tool_call:{flag}"] += 1
                    call_ref_counter += 1
                    call_ref = f"call-{call_ref_counter:06d}"
                    raw_call_id = payload.get("call_id")
                    if isinstance(raw_call_id, str) and raw_call_id:
                        if raw_call_id in call_id_to_ref:
                            raise RuntimeError(f"duplicate private call identifier at ordinal {ordinal}")
                        call_id_to_ref[raw_call_id] = call_ref
                    event = {
                        "argument_evidence": argument_summary,
                        "call_ref": call_ref,
                        "event_kind": "tool_call",
                        "mode": "typed-metadata-redacted",
                        "ordinal": ordinal,
                        "schema": SCHEMA,
                        "source_record_sha256": source_record_hash,
                        "timestamp": timestamp,
                        "tool_call_type": payload_type,
                        "tool_name": public_name,
                    }
                    tool_names[public_name] += 1

                elif payload_type in {"function_call_output", "custom_tool_call_output"}:
                    output_summary = summarize_output_value(payload.get("output"))
                    output_flags: list[str] = []
                    if output_summary.get("representation") == "text":
                        output_flags.extend(output_summary.get("source_risk_flags", []))
                    for block in output_summary.get("blocks", []):
                        output_flags.extend(block.get("source_risk_flags", []))
                    for flag in sorted(set(output_flags)):
                        risk_flags[f"tool_output:{flag}"] += 1
                    raw_call_id = payload.get("call_id")
                    call_ref = call_id_to_ref.get(raw_call_id) if isinstance(raw_call_id, str) else None
                    if call_ref is None:
                        orphan_outputs += 1
                    else:
                        paired_outputs += 1
                    event = {
                        "call_ref": call_ref,
                        "event_kind": "tool_output",
                        "mode": "typed-metadata-redacted",
                        "ordinal": ordinal,
                        "output_evidence": output_summary,
                        "schema": SCHEMA,
                        "source_record_sha256": source_record_hash,
                        "timestamp": timestamp,
                        "tool_output_type": payload_type,
                    }

                elif payload_type == "agent_message":
                    profiles: list[dict[str, Any]] = []
                    content = payload.get("content")
                    if isinstance(content, list):
                        for block in content:
                            if not isinstance(block, dict):
                                continue
                            block_type = str(block.get("type") or "(empty)")
                            item: dict[str, Any] = {"block_type": block_type}
                            text_value = block.get("text")
                            if isinstance(text_value, str):
                                item.update(content_profile(text_value))
                            encrypted_value = block.get("encrypted_content")
                            if isinstance(encrypted_value, str):
                                item["encrypted_characters"] = len(encrypted_value)
                                item["encrypted_content_sha256"] = sha256_bytes(encrypted_value.encode("utf-8"))
                            profiles.append(item)
                    event = {
                        "content_evidence": profiles,
                        "event_kind": "internal_agent_message_marker",
                        "mode": "metadata-only-internal-coordination",
                        "ordinal": ordinal,
                        "schema": SCHEMA,
                        "source_record_sha256": source_record_hash,
                        "timestamp": timestamp,
                    }
                else:
                    excluded_reasons[f"response_item_type:{payload_type}"] += 1
                    continue

                if event is None:
                    continue
                if ordinal <= prior_selected_ordinal:
                    raise RuntimeError(f"selected source ordinals are not strictly increasing at {ordinal}")
                prior_selected_ordinal = ordinal
                write_jsonl(edition, event)
                selected_events += 1
                selected_kinds[event["event_kind"]] += 1
                modes[event["mode"]] += 1

        if consumed != args.prefix_bytes or prefix_digest.hexdigest() != args.prefix_sha256:
            raise RuntimeError("frozen prefix byte count or SHA-256 mismatch")
        unused_summaries = sorted(set(editorial) - used_summaries)
        if unused_summaries:
            raise RuntimeError("unused editorial summaries: " + ",".join(map(str, unused_summaries)))

        with queue_tmp.open("wb") as queue:
            for item in unresolved:
                write_jsonl(queue, item)
        gzip_tmp = temp_dir / GZIP_NAME
        with edition_tmp.open("rb") as source, gzip_tmp.open("wb") as raw_gzip:
            with gzip.GzipFile(filename="", mode="wb", fileobj=raw_gzip, compresslevel=9, mtime=0) as compressed:
                shutil.copyfileobj(source, compressed, length=8 * 1024 * 1024)

        summary_tmp = temp_dir / SUMMARY_NAME
        summary_tmp.write_bytes(merged_summary_bytes)
        copy_public_scripts(temp_dir)
        status = "PARENT_REVIEW_REQUIRED" if not unresolved else "UNRESOLVED_ITEMS_PRESENT"
        status_tmp = temp_dir / STATUS_NAME
        status_tmp.write_text(
            f"{status}\nautomated_generation_complete=true\npublication_authorized=false\n"
            f"selected_events={selected_events}\nunresolved_events={len(unresolved)}\n",
            encoding="utf-8", newline="\n",
        )
        readme_tmp = temp_dir / README_NAME
        readme_tmp.write_text(
            "# S6 full-record public annex v2 candidate\n\n"
            "This optional machine-ingestible annex is a deterministic public evidence ledger derived from one frozen, newline-terminated prefix of the private active S6 root rollout. The private rollout is not included.\n\n"
            "Conversation messages retain safe text after public redaction; certified neutral summaries replace user turns that require them. Tool calls and outputs retain typed sequence, pairing, tool names, sizes, hashes, structural profiles, safe execution scalars, and risk flags. Raw commands, prompts, local paths, identifiers, images, and output text are not copied. Internal agent coordination is represented only by metadata markers. Platform, system, developer, compaction, state, and encrypted reasoning payloads are excluded.\n\n"
            "The gzip member is deterministic (`mtime=0`) and decompresses byte-for-byte to the JSONL file. Every public event retains its exact source ordinal, timestamp, and private-source record hash. This is a review candidate, not publication authorization.\n",
            encoding="utf-8", newline="\n",
        )

        unpaired_calls = len(call_id_to_ref) - paired_outputs
        inventory = {
            "schema": "s6-full-record-public-annex-inventory-v2",
            "source_scope": {
                "kind": "single active S6 root rollout; frozen newline-terminated prefix",
                "prefix_bytes": args.prefix_bytes,
                "prefix_sha256": args.prefix_sha256,
                "raw_source_deposited": False,
                "approximate_1_4_gb_reference_assessment": "the single root rollout itself",
                "broader_completed_descendant_corpus_excluded": {"files": 2071, "bytes": 3057735167},
            },
            "counts": {
                "source_records": source_records,
                "record_types": dict(sorted(record_types.items())),
                "response_item_types": dict(sorted(response_types.items())),
                "selected_events": selected_events,
                "selected_event_kinds": dict(sorted(selected_kinds.items())),
                "modes": dict(sorted(modes.items())),
                "excluded_records": sum(excluded_reasons.values()),
                "excluded_reasons": dict(sorted(excluded_reasons.items())),
                "editorial_summaries_used": len(used_summaries),
                "unresolved_events": len(unresolved),
                "tool_calls_with_private_call_id": len(call_id_to_ref),
                "paired_tool_outputs": paired_outputs,
                "orphan_tool_outputs": orphan_outputs,
                "unpaired_tool_calls_at_frozen_boundary_or_legacy": unpaired_calls,
                "tool_names": dict(sorted(tool_names.items())),
                "redactions": dict(sorted((+redactions).items())),
                "source_risk_flags_summarized_not_copied": dict(sorted(risk_flags.items())),
            },
            "source_timestamps": {"first": source_first_timestamp, "last": source_last_timestamp},
            "source_max_record_bytes": source_max_record_bytes,
        }
        inventory_tmp = temp_dir / INVENTORY_NAME
        inventory_tmp.write_bytes(pretty_json_bytes(inventory))

        outputs_for_receipt = {}
        for name in (
            EDITION_NAME, GZIP_NAME, QUEUE_NAME, SUMMARY_NAME, STATUS_NAME, README_NAME,
            GENERATOR_COPY_NAME, VALIDATOR_COPY_NAME, INVENTORY_NAME,
        ):
            path = temp_dir / name
            outputs_for_receipt[name] = {"bytes": path.stat().st_size, "sha256": sha256_file(path)}
        receipt = {
            "schema": "s6-full-record-public-annex-receipt-v2",
            "generator": {"version": VERSION, "sha256": sha256_file(generator_path)},
            "validator": {"sha256": sha256_file(validator_path)},
            "source": {
                "label": "private active S6 root rollout; frozen newline-terminated prefix",
                "prefix_bytes": args.prefix_bytes, "prefix_sha256": args.prefix_sha256,
                "newline_terminated": True, "raw_source_deposited": False,
            },
            "derivation": {
                "conversation_text_policy": "safe verbatim-redacted text; certified source-hash-anchored summaries for user turns requiring them",
                "tool_evidence_policy": "typed metadata, source hashes, pairing, structure, sizes, safe scalars, and risk flags; raw arguments and outputs omitted",
                "gzip_determinism": {"compresslevel": 9, "filename": "", "mtime": 0},
                "publication_authorized": False,
                "status": status,
            },
            "counts": inventory["counts"],
            "outputs": outputs_for_receipt,
        }
        receipt_tmp = temp_dir / RECEIPT_NAME
        receipt_tmp.write_bytes(pretty_json_bytes(receipt))

        for path in temp_dir.iterdir():
            if path.is_file():
                (output_dir / path.name).write_bytes(path.read_bytes())

    print(json.dumps({
        "candidate": str(output_dir / GZIP_NAME), "prefix_bytes": args.prefix_bytes,
        "prefix_sha256": args.prefix_sha256, "selected_events": selected_events,
        "unresolved_events": len(unresolved), "status": status,
    }, sort_keys=True))
    return 0 if not unresolved else 2


if __name__ == "__main__":
    raise SystemExit(main())
