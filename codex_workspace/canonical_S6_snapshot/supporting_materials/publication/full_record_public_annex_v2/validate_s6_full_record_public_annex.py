#!/usr/bin/env python3
"""Replay and aggressively validate the S6 full-record public annex v2."""

from __future__ import annotations

import argparse
from collections import Counter
import gzip
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile
from typing import Any

import generate_s6_full_record_public_annex as generator


VERSION = "2.0.0"
REPORT_NAME = "s6_full_record_public_annex_v2_validation_report.json"
HASHES_NAME = "SHA256SUMS.txt"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(8 * 1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


OPAQUE_IDENTIFIER_RE = re.compile(r"(?i)(?<![0-9a-f])[0-9a-f]{24,40}(?![0-9a-f])")
FORBIDDEN_EVENT_KEYS = {
    "arguments", "author", "call_id", "encrypted_content", "id", "image_url",
    "input", "internal_chat_message_metadata_passthrough", "output", "recipient",
}


def walk_strings(value: Any, path: tuple[str, ...] = ()):
    if isinstance(value, dict):
        for key, child in value.items():
            yield from walk_strings(child, path + (str(key),))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from walk_strings(child, path + (str(index),))
    elif isinstance(value, str):
        yield path, value


def all_keys(value: Any):
    if isinstance(value, dict):
        for key, child in value.items():
            yield str(key)
            yield from all_keys(child)
    elif isinstance(value, list):
        for child in value:
            yield from all_keys(child)


def scan_event(event: dict[str, Any]) -> list[str]:
    hits: set[str] = set()
    forbidden_keys = FORBIDDEN_EVENT_KEYS.intersection(all_keys(event))
    hits.update(f"forbidden_key:{key}" for key in forbidden_keys)
    for path, text in walk_strings(event):
        for hit in generator.scan_public_text(text):
            hits.add(f"{'.'.join(path)}:{hit}")
        if not path or not path[-1].endswith("sha256"):
            if OPAQUE_IDENTIFIER_RE.search(text):
                hits.add(f"{'.'.join(path)}:opaque_identifier")
    return sorted(hits)


def canonical_line(event: Any) -> bytes:
    return generator.canonical_json_bytes(event) + b"\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("source_jsonl", type=Path)
    parser.add_argument("output_directory", type=Path)
    parser.add_argument("--prefix-bytes", type=int, required=True)
    parser.add_argument("--prefix-sha256", required=True)
    parser.add_argument("--summaries", type=Path, required=True)
    args = parser.parse_args()

    output_dir = args.output_directory.resolve()
    receipt_path = output_dir / generator.RECEIPT_NAME
    inventory_path = output_dir / generator.INVENTORY_NAME
    edition_path = output_dir / generator.EDITION_NAME
    gzip_path = output_dir / generator.GZIP_NAME
    queue_path = output_dir / generator.QUEUE_NAME
    for path in (receipt_path, inventory_path, edition_path, gzip_path, queue_path):
        if not path.is_file():
            raise RuntimeError(f"required candidate artifact missing: {path.name}")

    receipt = json.loads(receipt_path.read_bytes())
    inventory = json.loads(inventory_path.read_bytes())
    if receipt.get("schema") != "s6-full-record-public-annex-receipt-v2":
        raise RuntimeError("unexpected receipt schema")
    if inventory.get("schema") != "s6-full-record-public-annex-inventory-v2":
        raise RuntimeError("unexpected inventory schema")
    if receipt["source"]["prefix_bytes"] != args.prefix_bytes or receipt["source"]["prefix_sha256"] != args.prefix_sha256:
        raise RuntimeError("receipt source prefix mismatch")

    generated_hash_checks: dict[str, bool] = {}
    for filename, metadata in receipt["outputs"].items():
        path = output_dir / filename
        ok = path.is_file() and path.stat().st_size == metadata["bytes"] and sha256_file(path) == metadata["sha256"]
        generated_hash_checks[filename] = ok
    if not all(generated_hash_checks.values()):
        raise RuntimeError("one or more receipt output hashes failed")

    with gzip.open(gzip_path, "rb") as compressed:
        decompressed = compressed.read()
    gzip_matches_jsonl = decompressed == edition_path.read_bytes()
    if not gzip_matches_jsonl:
        raise RuntimeError("gzip member does not reproduce JSONL")
    gzip_header = gzip_path.read_bytes()[:10]
    gzip_mtime_zero = len(gzip_header) >= 8 and gzip_header[4:8] == b"\x00\x00\x00\x00"
    if not gzip_mtime_zero:
        raise RuntimeError("gzip header has nonzero mtime")

    event_kind_counts: Counter[str] = Counter()
    mode_counts: Counter[str] = Counter()
    role_counts: Counter[str] = Counter()
    privacy_hits: list[dict[str, Any]] = []
    ordinals: list[int] = []
    seen_calls: set[str] = set()
    paired_outputs = 0
    orphan_outputs = 0
    canonical_jsonl = True
    with edition_path.open("rb") as handle:
        for line_number, raw in enumerate(handle, 1):
            event = json.loads(raw)
            if canonical_line(event) != raw:
                canonical_jsonl = False
            if event.get("schema") != generator.SCHEMA:
                raise RuntimeError(f"event schema mismatch at line {line_number}")
            ordinal = event.get("ordinal")
            if not isinstance(ordinal, int):
                raise RuntimeError(f"invalid ordinal at line {line_number}")
            ordinals.append(ordinal)
            event_kind = str(event.get("event_kind") or "")
            event_kind_counts[event_kind] += 1
            mode_counts[str(event.get("mode") or "")] += 1
            if event_kind == "conversation_message":
                role_counts[str(event.get("role") or "")] += 1
                public_text = event.get("public_text")
                if event.get("mode") != "unresolved-withheld" and not isinstance(public_text, str):
                    raise RuntimeError(f"nonwithheld conversation event lacks text at line {line_number}")
            elif event_kind == "tool_call":
                call_ref = event.get("call_ref")
                if not isinstance(call_ref, str) or not re.fullmatch(r"call-\d{6}", call_ref) or call_ref in seen_calls:
                    raise RuntimeError(f"invalid or duplicate public call reference at line {line_number}")
                seen_calls.add(call_ref)
            elif event_kind == "tool_output":
                call_ref = event.get("call_ref")
                if call_ref is None:
                    orphan_outputs += 1
                elif call_ref not in seen_calls:
                    raise RuntimeError(f"tool output precedes or misses call at line {line_number}")
                else:
                    paired_outputs += 1
            elif event_kind != "internal_agent_message_marker":
                raise RuntimeError(f"unknown event kind at line {line_number}")
            hits = scan_event(event)
            if hits:
                privacy_hits.append({"line": line_number, "ordinal": ordinal, "hits": hits})

    if not canonical_jsonl:
        raise RuntimeError("JSONL is not canonical")
    if ordinals != sorted(set(ordinals)):
        raise RuntimeError("public event ordinals are not strictly increasing and unique")

    queue_lines = [line for line in queue_path.read_bytes().splitlines() if line]
    unresolved_count = len(queue_lines)
    if unresolved_count != receipt["counts"]["unresolved_events"]:
        raise RuntimeError("unresolved queue count mismatch")

    replay_hash_checks: dict[str, bool] = {}
    with tempfile.TemporaryDirectory(prefix="s6-public-annex-v2-replay-") as replay_name:
        replay_dir = Path(replay_name)
        command = [
            sys.executable, str(Path(generator.__file__).resolve()), str(args.source_jsonl), str(replay_dir),
            "--prefix-bytes", str(args.prefix_bytes), "--prefix-sha256", args.prefix_sha256,
            "--summaries", str(args.summaries),
        ]
        completed = subprocess.run(command, capture_output=True, text=True, check=False)
        if completed.returncode not in (0, 2):
            raise RuntimeError("deterministic replay generator failed")
        for filename in receipt["outputs"]:
            replay_path = replay_dir / filename
            original_path = output_dir / filename
            replay_hash_checks[filename] = replay_path.is_file() and sha256_file(replay_path) == sha256_file(original_path)
    deterministic_replay = all(replay_hash_checks.values())
    if not deterministic_replay:
        raise RuntimeError("deterministic derivation replay mismatch")

    counts_match_inventory = (
        dict(sorted(event_kind_counts.items())) == inventory["counts"]["selected_event_kinds"]
        and len(ordinals) == inventory["counts"]["selected_events"]
        and paired_outputs == inventory["counts"]["paired_tool_outputs"]
        and orphan_outputs == inventory["counts"]["orphan_tool_outputs"]
    )
    if not counts_match_inventory:
        raise RuntimeError("event counts do not match inventory")

    # The scan is run on parsed values so source SHA-256 anchors remain allowed,
    # while non-hash opaque identifiers are rejected. No raw content is emitted.
    privacy_passed = not privacy_hits
    automated_checks_passed = bool(
        privacy_passed and deterministic_replay and gzip_matches_jsonl and gzip_mtime_zero
        and canonical_jsonl and counts_match_inventory and all(generated_hash_checks.values())
        and unresolved_count == 0
    )
    report = {
        "schema": "s6-full-record-public-annex-validation-v2",
        "validator": {"version": VERSION, "sha256": sha256_file(Path(__file__).resolve())},
        "source": {
            "prefix_bytes": args.prefix_bytes, "prefix_sha256": args.prefix_sha256,
            "raw_source_deposited": False,
        },
        "checks": {
            "automated_checks_passed": automated_checks_passed,
            "canonical_jsonl": canonical_jsonl,
            "counts_match_inventory": counts_match_inventory,
            "deterministic_derivation_replayed": deterministic_replay,
            "generated_output_hashes_verified": all(generated_hash_checks.values()),
            "gzip_decompresses_exactly_to_jsonl": gzip_matches_jsonl,
            "gzip_mtime_zero": gzip_mtime_zero,
            "ordinals_strictly_increasing_unique": ordinals == sorted(set(ordinals)),
            "privacy_scan_passed": privacy_passed,
            "unresolved_queue_empty": unresolved_count == 0,
        },
        "counts": {
            "events": len(ordinals), "event_kinds": dict(sorted(event_kind_counts.items())),
            "modes": dict(sorted(mode_counts.items())), "conversation_roles": dict(sorted(role_counts.items())),
            "paired_tool_outputs": paired_outputs, "orphan_tool_outputs": orphan_outputs,
            "privacy_findings": len(privacy_hits), "unresolved_events": unresolved_count,
        },
        "privacy_scan": {
            "scope": "every parsed field of the decompressed JSONL; first-name, local-path, private-link/protocol, credential, token, environment-secret, identifier, encoded-blob, contact, profanity, abusive-language, and embedded-platform-context patterns",
            "findings": privacy_hits,
        },
        "replay_file_matches": replay_hash_checks,
        "receipt_file_hash_checks": generated_hash_checks,
        "publication_authorized": False,
        "status": "PARENT_REVIEW_REQUIRED" if automated_checks_passed else "NOT_READY",
    }
    report_path = output_dir / REPORT_NAME
    report_path.write_bytes(generator.pretty_json_bytes(report))

    hash_paths = sorted(
        path for path in output_dir.iterdir()
        if path.is_file() and path.name != HASHES_NAME
    )
    hashes_text = "".join(f"{sha256_file(path)}  {path.name}\n" for path in hash_paths)
    (output_dir / HASHES_NAME).write_text(hashes_text, encoding="utf-8", newline="\n")

    print(json.dumps({
        "automated_checks_passed": automated_checks_passed,
        "events": len(ordinals), "privacy_findings": len(privacy_hits),
        "report": str(report_path), "status": report["status"],
    }, sort_keys=True))
    return 0 if automated_checks_passed else 3


if __name__ == "__main__":
    raise SystemExit(main())
