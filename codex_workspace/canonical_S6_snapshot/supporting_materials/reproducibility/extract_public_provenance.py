#!/usr/bin/env python3
"""Derive a publication-safe mathematical chronology from a private JSONL prefix.

The selection file contains no raw conversation.  It names retained source
events by ordinal and source-text hash and supplies the edited public text.
This program verifies those anchors against a byte-exact, newline-terminated
prefix of the private session record, writes the public Markdown edition, and
writes a redaction receipt.  It never copies unselected message text.
"""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
from typing import Any


VERSION = "1.0.0"


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(8 * 1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def message_text(payload: dict[str, Any]) -> str:
    parts: list[str] = []
    for block in payload.get("content") or []:
        if block.get("type") in {"input_text", "output_text", "text"}:
            text = block.get("text")
            if isinstance(text, str):
                parts.append(text)
    return "\n".join(parts)


def canonical_event_hash(event: dict[str, Any]) -> str:
    public_anchor = {
        "channel": event.get("channel") or "",
        "ordinal": event["ordinal"],
        "role": event["role"],
        "text_sha256": event["text_sha256"],
        "timestamp": event["timestamp"],
    }
    encoded = json.dumps(
        public_anchor, ensure_ascii=False, separators=(",", ":"), sort_keys=True
    ).encode("utf-8")
    return sha256_bytes(encoded)


def scan_public_text(text: str) -> list[str]:
    patterns = {
        "windows_absolute_path": r"(?i)(?:^|[\s`'\"])[a-z]:[\\/]",
        "private_posix_path": r"/(?:Users|home|mnt/data)/",
        "agent_or_sandbox_uri": r"(?i)(?:sandbox:|codex://)",
        "opaque_overleaf_endpoint": r"(?i)overleaf\.com/(?:project|read)/",
        "credential_assignment": r"(?i)(?:bearer|api[_ -]?key|password|secret)\s*[:=]",
        "raw_tool_protocol": r"(?i)(?:custom_tool_call|function_call_output|tool_schema)",
        "informal_abuse": r"(?i)\b(?:fuck|fucking|retard|retarded|shit)\b",
    }
    return [name for name, pattern in patterns.items() if re.search(pattern, text)]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("source_jsonl", type=Path)
    parser.add_argument("selection_json", type=Path)
    parser.add_argument("edition_markdown", type=Path)
    parser.add_argument("receipt_json", type=Path)
    parser.add_argument("--prefix-bytes", type=int, required=True)
    parser.add_argument("--prefix-sha256", required=True)
    args = parser.parse_args()

    selection = json.loads(args.selection_json.read_text(encoding="utf-8"))
    requested = selection.get("events") or []
    requested_by_ordinal = {int(item["ordinal"]): item for item in requested}
    if len(requested_by_ordinal) != len(requested):
        raise RuntimeError("duplicate retained-event ordinal in selection")

    source_size = args.source_jsonl.stat().st_size
    if source_size < args.prefix_bytes:
        raise RuntimeError("private source is shorter than the frozen prefix")

    prefix_digest = hashlib.sha256()
    total_records = 0
    event_types: Counter[str] = Counter()
    message_roles: Counter[str] = Counter()
    selected_events: dict[int, dict[str, Any]] = {}
    consumed = 0

    with args.source_jsonl.open("rb") as handle:
        while consumed < args.prefix_bytes:
            raw = handle.readline(args.prefix_bytes - consumed)
            if not raw:
                raise RuntimeError("short read inside frozen prefix")
            consumed += len(raw)
            prefix_digest.update(raw)
            if not raw.endswith(b"\n"):
                raise RuntimeError("frozen prefix ends inside a JSONL record")
            record = json.loads(raw)
            total_records += 1
            record_type = str(record.get("type") or "")
            event_types[record_type] += 1
            if record_type != "response_item":
                continue
            payload = record.get("payload") or {}
            if payload.get("type") != "message":
                continue
            role = str(payload.get("role") or "")
            message_roles[role] += 1
            ordinal = int(record.get("ordinal"))
            if ordinal not in requested_by_ordinal:
                continue
            text = message_text(payload)
            anchor = {
                "ordinal": ordinal,
                "timestamp": str(record.get("timestamp") or ""),
                "role": role,
                "channel": str(payload.get("channel") or ""),
                "text_sha256": sha256_bytes(text.encode("utf-8")),
            }
            expected = requested_by_ordinal[ordinal]
            for key in ("timestamp", "role", "text_sha256"):
                if anchor[key] != expected[key]:
                    raise RuntimeError(
                        f"retained event {ordinal} {key} mismatch: "
                        f"{anchor[key]!r} != {expected[key]!r}"
                    )
            anchor["event_hash"] = canonical_event_hash(anchor)
            selected_events[ordinal] = anchor

    if consumed != args.prefix_bytes:
        raise RuntimeError("prefix byte count mismatch")
    actual_prefix_sha = prefix_digest.hexdigest()
    if actual_prefix_sha != args.prefix_sha256.lower():
        raise RuntimeError(
            f"frozen prefix SHA-256 mismatch: {actual_prefix_sha} != "
            f"{args.prefix_sha256.lower()}"
        )
    missing = sorted(set(requested_by_ordinal) - set(selected_events))
    if missing:
        raise RuntimeError(f"retained ordinals not found: {missing}")

    lines = [
        "# Public mathematical provenance edition",
        "",
        f"Edition: {selection['edition']}",
        f"Coverage: {selection['coverage']}",
        "",
        "This chronology records selected mathematical and release milestones",
        "from a private Codex session. Entries are edited for clarity, privacy,",
        "and removal of conversational or operational material. The complete",
        "proofs, not this chronology, are authoritative; each entry therefore",
        "points to stable project-relative mathematical evidence.",
        "",
        "The private JSONL is not deposited. The accompanying receipt records a",
        "byte-exact frozen-prefix hash and a source-event hash for every retained",
        "entry, permitting an authorized holder of the private source to verify",
        "the derivation without disclosing excluded text.",
        "",
        "## Chronology",
        "",
    ]
    retained_receipt: list[dict[str, Any]] = []
    for item in requested:
        ordinal = int(item["ordinal"])
        anchor = selected_events[ordinal]
        date = anchor["timestamp"][:10]
        lines.extend(
            [
                f"### {date} — {item['heading']}",
                "",
                item["edited_text"].strip(),
                "",
                "Canonical evidence: "
                + "; ".join(f"`{path}`" for path in item["evidence"])
                + ".",
                "",
                f"Provenance anchor: source event {ordinal}; "
                f"event SHA-256 `{anchor['event_hash']}`. "
                "[Edited for clarity and privacy.]",
                "",
            ]
        )
        retained_receipt.append(
            {
                "ordinal": ordinal,
                "timestamp": anchor["timestamp"],
                "role": anchor["role"],
                "source_text_sha256": anchor["text_sha256"],
                "source_event_sha256": anchor["event_hash"],
                "public_text_sha256": sha256_bytes(
                    item["edited_text"].strip().encode("utf-8")
                ),
            }
        )

    lines.extend(
        [
            "## Status at the edition boundary",
            "",
            selection["status_at_boundary"].strip(),
            "",
            "The status labels are defined in the workbench. External specialist",
            "replication and community adjudication remain distinct from the",
            "internal proof status recorded there.",
            "",
        ]
    )
    edition_text = "\n".join(lines)
    privacy_hits = scan_public_text(edition_text)
    if privacy_hits:
        raise RuntimeError(f"public-edition privacy scan failed: {privacy_hits}")

    args.edition_markdown.parent.mkdir(parents=True, exist_ok=True)
    args.edition_markdown.write_text(edition_text, encoding="utf-8")
    edition_sha = sha256_file(args.edition_markdown)

    user_assistant_messages = message_roles["user"] + message_roles["assistant"]
    receipt = {
        "schema": "s6-public-mathematical-provenance-receipt-v1",
        "edition": selection["edition"],
        "source": {
            "label": selection["source_label"],
            "frozen_prefix_bytes": args.prefix_bytes,
            "frozen_prefix_sha256": actual_prefix_sha,
            "newline_terminated": True,
            "raw_source_deposited": False,
        },
        "extractor": {
            "version": VERSION,
            "sha256": sha256_file(Path(__file__)),
        },
        "selection": {
            "sha256": sha256_file(args.selection_json),
            "retained_event_count": len(retained_receipt),
        },
        "counts": {
            "source_jsonl_records": total_records,
            "response_message_roles": dict(sorted(message_roles.items())),
            "retained_user_assistant_events": len(retained_receipt),
            "excluded_user_assistant_events": user_assistant_messages
            - len(retained_receipt),
            "excluded_developer_or_system_messages": sum(
                count
                for role, count in message_roles.items()
                if role not in {"user", "assistant"}
            ),
            "excluded_nonmessage_structural_tool_and_state_records": total_records
            - sum(message_roles.values()),
            "malformed_records": 0,
        },
        "retained_events": retained_receipt,
        "public_edition": {
            "path": args.edition_markdown.name,
            "bytes": args.edition_markdown.stat().st_size,
            "sha256": edition_sha,
        },
        "confirmations": {
            "credential_pattern_present": False,
            "private_absolute_path_present": False,
            "opaque_access_endpoint_present": False,
            "raw_tool_payload_present": False,
            "informal_abuse_present": False,
            "raw_session_jsonl_present_in_public_outputs": False,
            "third_party_document_present": False,
            "privacy_scan_patterns_triggered": [],
        },
    }
    args.receipt_json.parent.mkdir(parents=True, exist_ok=True)
    args.receipt_json.write_text(
        json.dumps(receipt, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "edition": str(args.edition_markdown),
                "edition_sha256": edition_sha,
                "receipt": str(args.receipt_json),
                "retained_events": len(retained_receipt),
                "source_records": total_records,
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
