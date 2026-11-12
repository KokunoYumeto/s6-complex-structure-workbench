#!/usr/bin/env python3
"""Independently replay and validate the complete conversation candidate.

The validator re-streams the frozen private prefix, verifies one-for-one event
coverage and exact source anchors, confirms deterministic editorial derivation,
checks the receipt and output hashes, and scans every published text field.  It
returns status 2 for a structurally valid but editorially unresolved candidate.
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
from typing import Any, BinaryIO, Iterator

import generate_complete_conversation_provenance as core


VERSION = "1.0.0"
REPORT_NAME = "complete_sanitized_conversation_validation_v1.json"
REPORT_SCHEMA = "s6-complete-conversation-validation-report-v1"


def jsonl_items(path: Path) -> Iterator[tuple[bytes, dict[str, Any]]]:
    with path.open("rb") as handle:
        for line_number, raw in enumerate(handle, 1):
            if not raw.endswith(b"\n"):
                raise RuntimeError(f"{path.name} is not newline terminated at line {line_number}")
            try:
                value = json.loads(raw)
            except (UnicodeDecodeError, json.JSONDecodeError) as exc:
                raise RuntimeError(f"{path.name} has invalid JSON at line {line_number}") from exc
            if not isinstance(value, dict):
                raise RuntimeError(f"{path.name} line {line_number} is not an object")
            if raw != core.canonical_json_bytes(value) + b"\n":
                raise RuntimeError(f"{path.name} line {line_number} is not canonical JSON")
            yield raw, value


def next_or_none(iterator: Iterator[tuple[bytes, dict[str, Any]]]) -> dict[str, Any] | None:
    try:
        return next(iterator)[1]
    except StopIteration:
        return None


def assert_equal(actual: Any, expected: Any, label: str) -> None:
    if actual != expected:
        raise RuntimeError(f"validation mismatch: {label}")


def file_description(path: Path) -> dict[str, Any]:
    return {
        "bytes": path.stat().st_size,
        "filename": path.name,
        "sha256": core.sha256_file(path),
    }


def validate_artifact_hashes(
    output_dir: Path, receipt: dict[str, Any]
) -> dict[str, dict[str, Any]]:
    mapping = {
        "candidate": output_dir / core.EDITION_NAME,
        "release_status": output_dir / core.STATUS_NAME,
        "unresolved_queue": output_dir / core.QUEUE_NAME,
    }
    result: dict[str, dict[str, Any]] = {}
    for key, path in mapping.items():
        actual = file_description(path)
        expected = receipt.get("outputs", {}).get(key)
        assert_equal(actual, expected, f"receipt output descriptor {key}")
        result[key] = actual
    return result


def scan_decoded_json_value(value: Any) -> list[str]:
    """Scan the semantic strings in decoded JSON, not JSON escape syntax.

    A raw JSON serialization doubles backslashes.  Scanning those serialized
    bytes would therefore misclassify ordinary LaTeX such as ``\\(S^6\\)`` as
    a UNC filesystem path.  Decode first, then scan every key and string value;
    this keeps the privacy gate strict without treating serialization escapes
    as public content.
    """

    hits: set[str] = set()
    if isinstance(value, str):
        hits.update(core.scan_public_text(value))
    elif isinstance(value, list):
        for item in value:
            hits.update(scan_decoded_json_value(item))
    elif isinstance(value, dict):
        for key, item in value.items():
            hits.update(core.scan_public_text(str(key)))
            hits.update(scan_decoded_json_value(item))
    return sorted(hits)


def scan_whole_generated_file(path: Path) -> list[str]:
    if path.suffix.casefold() == ".jsonl":
        hits: set[str] = set()
        for _, value in jsonl_items(path):
            hits.update(scan_decoded_json_value(value))
        return sorted(hits)
    if path.suffix.casefold() == ".json":
        value = json.loads(path.read_text(encoding="utf-8"))
        return scan_decoded_json_value(value)
    return core.scan_public_text(path.read_text(encoding="utf-8"))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("source_jsonl", type=Path)
    parser.add_argument("output_directory", type=Path)
    parser.add_argument("--prefix-bytes", type=int, required=True)
    parser.add_argument("--prefix-sha256", required=True)
    parser.add_argument("--summaries", type=Path)
    args = parser.parse_args()

    expected_prefix_sha = args.prefix_sha256.casefold()
    if args.prefix_bytes <= 0 or not re.fullmatch(r"[0-9a-f]{64}", expected_prefix_sha):
        raise RuntimeError("invalid frozen-prefix arguments")
    if args.source_jsonl.stat().st_size < args.prefix_bytes:
        raise RuntimeError("private source is shorter than the frozen prefix")

    output_dir = args.output_directory.resolve()
    receipt_path = output_dir / core.RECEIPT_NAME
    receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
    if receipt.get("schema") != core.RECEIPT_SCHEMA:
        raise RuntimeError("unexpected redaction-receipt schema")
    assert_equal(
        receipt.get("source", {}).get("frozen_prefix_bytes"),
        args.prefix_bytes,
        "receipt frozen-prefix byte count",
    )
    assert_equal(
        receipt.get("source", {}).get("frozen_prefix_sha256"),
        expected_prefix_sha,
        "receipt frozen-prefix hash",
    )

    summaries_path = (args.summaries or output_dir / core.SUMMARY_NAME).resolve()
    editorial, summaries_sha = core.load_editorial_summaries(summaries_path)
    assert_equal(
        receipt.get("editorial_summaries", {}).get("sha256"),
        summaries_sha,
        "editorial-summary file hash",
    )
    assert_equal(
        receipt.get("editorial_summaries", {}).get("anchored_summary_count"),
        len(editorial),
        "editorial-summary count",
    )

    generator_path = Path(core.__file__).resolve()
    validator_path = Path(__file__).resolve()
    assert_equal(
        receipt.get("generator", {}).get("sha256"),
        core.sha256_file(generator_path),
        "generator hash",
    )
    assert_equal(
        receipt.get("validator", {}).get("sha256"),
        core.sha256_file(validator_path),
        "validator hash",
    )
    output_descriptions = validate_artifact_hashes(output_dir, receipt)

    candidate_path = output_dir / core.EDITION_NAME
    queue_path = output_dir / core.QUEUE_NAME
    candidate_iter = jsonl_items(candidate_path)
    queue_iter = jsonl_items(queue_path)

    total_records = 0
    consumed = 0
    prefix_digest = hashlib.sha256()
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
    natural_event_count = 0
    nontext_allowed_role_messages = 0
    embedded_only_allowed_role_messages = 0
    unresolved_count = 0
    prior_ordinal = -1

    with args.source_jsonl.open("rb") as source:
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
            if role not in core.ALLOWED_ROLES:
                excluded_role_messages[role or "(empty)"] += 1
                continue
            blocks = core.text_blocks(payload)
            if not blocks:
                nontext_allowed_role_messages += 1
                continue
            source_text = core.joined_source_text(blocks)
            natural_text, embedded_count = core.strip_embedded_nonconversation(source_text)
            if not natural_text or not re.search(r"\w", natural_text, re.UNICODE):
                embedded_only_allowed_role_messages += 1
                continue

            ordinal = record.get("ordinal")
            timestamp = record.get("timestamp")
            if not isinstance(ordinal, int) or ordinal <= prior_ordinal:
                raise RuntimeError("invalid or non-increasing natural-message ordinal")
            if not isinstance(timestamp, str) or not timestamp:
                raise RuntimeError(f"source event {ordinal} lacks a timestamp")
            prior_ordinal = ordinal
            source_sha = core.sha256_bytes(source_text.encode("utf-8"))
            block_hashes = [core.sha256_bytes(block.encode("utf-8")) for block in blocks]
            requires_summary = core.source_requires_summary(natural_text)
            if requires_summary:
                source_summary_required_by_role[role] += 1

            event = next_or_none(candidate_iter)
            if event is None:
                raise RuntimeError(f"candidate ends before source event {ordinal}")
            expected_anchor = {
                "ordinal": ordinal,
                "phase": core.phase_of(payload),
                "role": role,
                "schema": core.SCHEMA,
                "source_text_block_count": len(blocks),
                "source_text_block_sha256": block_hashes,
                "source_text_sha256": source_sha,
                "timestamp": timestamp,
            }
            for key, expected in expected_anchor.items():
                assert_equal(event.get(key), expected, f"source event {ordinal} field {key}")
            if set(event) - {
                "mode",
                "ordinal",
                "phase",
                "public_text",
                "role",
                "schema",
                "source_text_block_count",
                "source_text_block_sha256",
                "source_text_sha256",
                "timestamp",
                "withheld_reason_codes",
            }:
                raise RuntimeError(f"candidate source event {ordinal} has unexpected fields")

            mode = event.get("mode")
            public_text = event.get("public_text")
            if mode not in {
                "verbatim-redacted",
                "summarized-redacted",
                "unresolved-withheld",
            }:
                raise RuntimeError(f"source event {ordinal} has invalid public mode")
            entry = editorial.get(ordinal)
            event_redactions: Counter[str] = Counter()
            expected_reasons: list[str] = []
            expected_public: str | None
            expected_mode: str

            if entry is not None:
                used_editorial.add(ordinal)
                if entry["source_text_sha256"] != source_sha:
                    expected_reasons.append("editorial_summary_source_hash_mismatch")
                    expected_public = None
                    expected_mode = "unresolved-withheld"
                else:
                    expected_public, event_redactions = core.redact_text(entry["summary"])
                    expected_mode = "summarized-redacted"
            elif requires_summary:
                expected_reasons.append("adequate_neutral_summary_required")
                expected_public = None
                expected_mode = "unresolved-withheld"
            else:
                expected_public, event_redactions = core.redact_text(source_text)
                expected_mode = "verbatim-redacted"

            if expected_public is not None:
                hits = core.scan_public_text(expected_public)
                if hits:
                    expected_reasons.extend(f"public_scan:{hit}" for hit in hits)
                    expected_public = None
                    expected_mode = "unresolved-withheld"
                elif not expected_public or not re.search(r"\w", expected_public, re.UNICODE):
                    expected_reasons.append("empty_after_redaction")
                    expected_public = None
                    expected_mode = "unresolved-withheld"

            assert_equal(mode, expected_mode, f"source event {ordinal} mode")
            assert_equal(public_text, expected_public, f"source event {ordinal} public text")
            if public_text is not None:
                hits = core.scan_public_text(public_text)
                if hits:
                    raise RuntimeError(f"source event {ordinal} fails public-text scan")
                if "withheld_reason_codes" in event:
                    raise RuntimeError(f"published source event {ordinal} has withholding reasons")
            else:
                expected_reason_set = sorted(set(expected_reasons))
                assert_equal(
                    event.get("withheld_reason_codes"),
                    expected_reason_set,
                    f"source event {ordinal} withholding reasons",
                )
                queue_item = next_or_none(queue_iter)
                expected_queue_item = {
                    "ordinal": ordinal,
                    "reason_codes": expected_reason_set,
                    "role": role,
                    "schema": "s6-complete-conversation-unresolved-queue-v1",
                    "source_text_sha256": source_sha,
                    "timestamp": timestamp,
                }
                assert_equal(queue_item, expected_queue_item, f"source event {ordinal} queue item")
                unresolved_count += 1
                unresolved_by_role[role] += 1
                for reason in expected_reason_set:
                    unresolved_reason_counts[reason] += 1

            natural_event_count += 1
            natural_events_by_role[role] += 1
            phase_counts[f"{role}:{core.phase_of(payload) or '(empty)'}"] += 1
            mode_counts[mode] += 1
            redaction_counts.update(event_redactions)
            if embedded_count and not event_redactions["embedded_operational_payload"]:
                redaction_counts["embedded_operational_payload"] += embedded_count

    if consumed != args.prefix_bytes:
        raise RuntimeError("frozen-prefix byte-count mismatch")
    actual_prefix_sha = prefix_digest.hexdigest()
    assert_equal(actual_prefix_sha, expected_prefix_sha, "frozen-prefix SHA-256")
    if next_or_none(candidate_iter) is not None:
        raise RuntimeError("candidate contains events beyond the frozen source prefix")
    if next_or_none(queue_iter) is not None:
        raise RuntimeError("unresolved queue contains extra entries")
    assert_equal(sorted(used_editorial), sorted(editorial), "used editorial summaries")

    counts = {
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
    }
    assert_equal(receipt.get("counts"), counts, "receipt counts")

    status = "RELEASE_READY" if unresolved_count == 0 else "NOT_RELEASE_READY"
    safe_to_include = unresolved_count == 0
    assert_equal(receipt.get("release", {}).get("status"), status, "receipt status")
    assert_equal(
        receipt.get("release", {}).get("safe_to_include"),
        safe_to_include,
        "receipt inclusion gate",
    )
    assert_equal(
        receipt.get("release", {}).get("unresolved_event_count"),
        unresolved_count,
        "receipt unresolved count",
    )

    expected_status_text = (
        f"{status}\n"
        f"safe_to_include={'true' if safe_to_include else 'false'}\n"
        f"natural_language_events={natural_event_count}\n"
        f"unresolved_events={unresolved_count}\n"
        f"candidate_sha256={output_descriptions['candidate']['sha256']}\n"
        f"unresolved_queue_sha256={output_descriptions['unresolved_queue']['sha256']}\n"
    )
    assert_equal(
        (output_dir / core.STATUS_NAME).read_text(encoding="utf-8"),
        expected_status_text,
        "release-status text",
    )

    whole_file_scan_hits: dict[str, list[str]] = {}
    for path in (
        candidate_path,
        queue_path,
        receipt_path,
        output_dir / core.STATUS_NAME,
        summaries_path,
    ):
        hits = scan_whole_generated_file(path)
        if hits:
            whole_file_scan_hits[path.name] = hits
    if whole_file_scan_hits:
        raise RuntimeError("one or more generated public files failed the privacy scan")

    report = {
        "counts": counts,
        "files": {
            "candidate": output_descriptions["candidate"],
            "editorial_summaries": file_description(summaries_path),
            "generator": file_description(generator_path),
            "receipt": file_description(receipt_path),
            "release_status": output_descriptions["release_status"],
            "unresolved_queue": output_descriptions["unresolved_queue"],
            "validator": file_description(validator_path),
        },
        "privacy_scan": {
            "files_checked": 5,
            "forbidden_pattern_hits": {},
            "passed": True,
        },
        "release": {
            "safe_to_include": safe_to_include,
            "status": status,
            "unresolved_event_count": unresolved_count,
        },
        "schema": REPORT_SCHEMA,
        "source": {
            "frozen_prefix_bytes": args.prefix_bytes,
            "frozen_prefix_sha256": actual_prefix_sha,
            "newline_terminated": True,
            "raw_source_deposited": False,
        },
        "validation": {
            "canonical_jsonl": True,
            "complete_natural_language_event_coverage": True,
            "deterministic_derivation_replayed": True,
            "exact_source_anchors_verified": True,
            "output_hashes_verified": True,
            "receipt_counts_verified": True,
        },
        "validator": {"version": VERSION},
    }
    report_bytes = (
        json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True).encode("utf-8")
        + b"\n"
    )
    with tempfile.NamedTemporaryFile(
        mode="wb",
        prefix="complete-conversation-validation-",
        dir=str(output_dir),
        delete=False,
    ) as handle:
        temporary_report = Path(handle.name)
        handle.write(report_bytes)
    os.replace(temporary_report, output_dir / REPORT_NAME)

    print(
        json.dumps(
            {
                "candidate_sha256": output_descriptions["candidate"]["sha256"],
                "natural_language_events": natural_event_count,
                "safe_to_include": safe_to_include,
                "status": status,
                "unresolved_events": unresolved_count,
                "validation_passed": True,
            },
            sort_keys=True,
        )
    )
    return 0 if safe_to_include else 2


if __name__ == "__main__":
    raise SystemExit(main())
