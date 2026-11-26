#!/usr/bin/env python3
"""Recompute exact current Paper III statement-event associations.

The default ``inspect`` mode is read-only. ``derive`` emits the same result
as JSON on stdout for the final records writer; it also writes no file.
Neither mode edits a manuscript, event, tag, inventory, count or provenance
table. Run again after the last admitted events before adopting the totals.

Selection follows the statement/current_data precedent in
S6_SERIES_PUBLISH_c4_derive_II.py, restricted to Paper III. The current
formal owner and its immediate proof provide ownership; an owned equation
label alone never becomes a statement subject. Historical aliases require
the literal historical kind ``statement``. Event types and evidence-group
strings are retained exactly. A single explicitly withdrawn event is
excluded by its exact event_id, never by an outcome substring.
"""

from __future__ import annotations

import argparse
from collections import Counter
import csv
from dataclasses import dataclass
from datetime import datetime, timezone
import io
import json
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
PAPER = "III"
TYPES = (
    "targeted proof check",
    "independent re-proof",
    "computation or formal certificate",
    "used and rechecked in this run",
    "carried as background without fault found",
    "refuted, with the refined statement's id",
)
WITHDRAWN_EVENT = "III-C4-02L5-FRESH-TARGETED-ASTRA"
REPLACEMENT_EVENT = "III_C4_FRESH_EULER_02L5_20261123"
WITHDRAWAL_MARKER = "WITHDRAWN on 2026-11-23 at 14:49 UTC"
WITHDRAWAL_CREDIT = "It receives no live completion or substantive-count credit."
LABEL = re.compile(r"\\label\s*\{([^}]+)\}")
TAG = re.compile(r"\\hypertarget\s*\{tag-([^}]+)\}")
HEADING = re.compile(r"\\(?:part|chapter|section|subsection|subsubsection)\*?\s*(?:\[[^]]*\])?\s*\{")


@dataclass(frozen=True)
class Owner:
    statement_id: str
    kind: str
    tag: str
    line: int
    start: int
    statement_stop: int
    stop: int
    labels: tuple[str, ...]
    owned_labels: tuple[str, ...]


def read_text(path: Path) -> str:
    """Read one unchanged input image; no hash or derived file is made."""
    before = path.stat()
    data = path.read_text(encoding="utf-8")
    after = path.stat()
    if (before.st_size, before.st_mtime_ns) != (after.st_size, after.st_mtime_ns):
        raise ValueError(f"Input changed during reading; rerun: {path}")
    return data


def read_rows(path: Path) -> list[dict[str, str]]:
    csv.field_size_limit(100_000_000)
    reader = csv.DictReader(io.StringIO(read_text(path)), delimiter="\t")
    rows = list(reader)
    if any(None in row or any(value is None for value in row.values()) for row in rows):
        raise ValueError(f"Malformed TSV row: {path}")
    return rows


def without_comments(text: str) -> str:
    """Blank unescaped TeX comments, preserving every offset and newline."""
    chars = list(text)
    pos = 0
    while pos < len(text):
        if text[pos] == "%":
            left = pos - 1
            while left >= 0 and text[left] == "\\":
                left -= 1
            if (pos - left - 1) % 2 == 0:
                end = text.find("\n", pos)
                if end < 0:
                    end = len(text)
                chars[pos:end] = " " * (end - pos)
                pos = end
        pos += 1
    return "".join(chars)


def parse_statements(text: str) -> tuple[list[Owner], dict[str, str], set[str]]:
    """Find formal printed owners and labels in their immediate proofs.

    The parser reads structural tokens only. It does not derive dependencies,
    refresh an inventory or supply a whole-proof reading. An ambiguity in
    formal ownership is reported instead of choosing a label by similarity.
    """
    clean = without_comments(text)
    start = clean.index(r"\begin{document}")
    finish = clean.index(r"\end{document}", start)
    kinds = set(re.findall(r"\\newtheorem\*?\s*\{([^}]+)\}", clean[:start]))
    if not kinds or "proof" in kinds:
        raise ValueError("Missing or ambiguous formal statement environment declarations")
    names = "|".join(re.escape(name) for name in sorted(kinds | {"proof"}))
    token = re.compile(r"\\(begin|end)\s*\{(" + names + r")\}")
    stack: list[tuple[str, int, int]] = []
    statements: list[tuple[str, int, int]] = []
    proofs: list[tuple[int, int]] = []
    for match in token.finditer(clean, start, finish):
        action, kind = match.groups()
        if action == "begin":
            if kind in kinds and any(open_kind in kinds for open_kind, _, _ in stack):
                raise ValueError(f"Nested formal owners at source line {text.count(chr(10), 0, match.start()) + 1}")
            stack.append((kind, match.start(), match.end()))
        else:
            if not stack or stack[-1][0] != kind:
                raise ValueError(f"Unmatched {kind} end at character {match.start()}")
            _, left, header_end = stack.pop()
            if kind == "proof":
                proofs.append((left, match.end()))
            else:
                statements.append((kind, left, match.end()))
    if stack:
        raise ValueError(f"Unclosed formal/proof environments: {stack}")
    statements.sort(key=lambda item: item[1])
    proofs.sort()
    result: list[Owner] = []
    label_owners: dict[str, str] = {}
    primary: set[str] = set()
    for number, (kind, left, statement_stop) in enumerate(statements):
        labels = tuple(match[1] for match in LABEL.finditer(clean, left, statement_stop))
        if not labels:
            raise ValueError(f"Unlabelled {kind} at line {text.count(chr(10), 0, left) + 1}")
        sid = labels[0]
        if sid in primary:
            raise ValueError(f"Repeated primary statement identifier: {sid}")
        primary.add(sid)
        limit = statements[number + 1][1] if number + 1 < len(statements) else finish
        heading = HEADING.search(clean, statement_stop, limit)
        if heading:
            limit = heading.start()
        immediate = [(a, b) for a, b in proofs if statement_stop <= a < limit]
        if len(immediate) > 1:
            # Nested proof environments would otherwise appear twice.
            outer = [(a, b) for a, b in immediate if not any(c < a and b < d for c, d in immediate)]
            if len(outer) != 1:
                raise ValueError(f"Multiple immediate proofs for {sid}: {outer}")
            immediate = outer
        stop = immediate[0][1] if immediate else statement_stop
        if stop > limit:
            raise ValueError(f"Immediate proof crosses the next formal owner/heading: {sid}")
        owned_labels = tuple(match[1] for match in LABEL.finditer(clean, left, stop))
        first_tag = TAG.search(clean, left, statement_stop)
        row = Owner(sid, kind, first_tag[1] if first_tag else "",
                    text.count("\n", 0, left) + 1, left, statement_stop, stop,
                    labels, owned_labels)
        result.append(row)
        for label in owned_labels:
            former = label_owners.get(label)
            if former is not None and former != sid:
                raise ValueError(f"Multiple owners for label {label}: {former}, {sid}")
            label_owners[label] = sid
    all_labels = {match[1] for match in LABEL.finditer(clean, start, finish)}
    return result, label_owners, all_labels


def group_key(event: dict[str, str]) -> str:
    return event.get("evidence_group") or event["event_id"]


def current_data(root: Path = ROOT) -> dict:
    source = root / "S6_SERIES_PUBLISH_III.tex"
    statements, owners, all_labels = parse_statements(read_text(source))
    events = read_rows(root / "CHECK_EVENTS.tsv")
    event_ids = [event["event_id"] for event in events]
    if any(not value for value in event_ids) or len(set(event_ids)) != len(event_ids):
        raise ValueError("CHECK_EVENTS event IDs must be nonempty and unique")
    by_event_id = {event["event_id"]: event for event in events}
    if WITHDRAWN_EVENT not in by_event_id or REPLACEMENT_EVENT not in by_event_id:
        raise ValueError("The exact withdrawn/replacement Euler records must both remain present")
    withdrawn = by_event_id[WITHDRAWN_EVENT]
    if WITHDRAWAL_MARKER not in withdrawn["outcome"] or WITHDRAWAL_CREDIT not in withdrawn["outcome"]:
        raise ValueError("The designated exclusion no longer has the reviewed whole-event withdrawal outcome")
    tags = [row for row in read_rows(root / "S6_SERIES_PUBLISH_tags.tsv") if row["paper"] == PAPER]
    historical = {row["label"] for row in tags if row["kind"] == "statement"}
    active = {row.statement_id for row in statements}
    subjects = active | (historical & owners.keys())
    tag_aliases: dict[str, str] = {}
    for row in tags:
        key, label = "tag:" + row["tag"], row["label"]
        if key in tag_aliases and tag_aliases[key] != label:
            raise ValueError(f"Ambiguous historical tag alias: {key}")
        tag_aliases[key] = label
    for row in statements:
        if not row.tag:
            continue
        key = "tag:" + row.tag
        if key in tag_aliases and tag_aliases[key] != row.statement_id:
            raise ValueError(f"Current primary tag mismatch: {key}, {row.statement_id}, {tag_aliases[key]}")
        tag_aliases[key] = row.statement_id
    resolve = lambda event: tag_aliases.get(event["statement_id"], event["statement_id"])
    eligible = [event for event in events if resolve(event) in subjects]
    selected = [event for event in eligible if event["event_id"] != WITHDRAWN_EVENT]
    if withdrawn not in eligible:
        raise ValueError("The withdrawn event's statement must still be a current III subject")
    if by_event_id[REPLACEMENT_EVENT] not in selected:
        raise ValueError("The replacement Euler event must be retained")
    bad_types = {event["type"] for event in selected} - set(TYPES)
    if bad_types:
        raise ValueError(f"Selected event types outside the six prompt types: {sorted(bad_types)}")
    counts = Counter(event["type"] for event in selected)
    groups = {group_key(event) for event in selected}
    historical_aliases = sorted(subjects - active)
    unselected_source_events = [event for event in events
        if resolve(event) in all_labels and resolve(event) not in subjects]
    # This diagnostic has no role in selection or exclusion.
    retained_mentions = [event for event in selected
        if re.search(r"\bwithdrawn\b", event["outcome"], re.IGNORECASE)]
    return dict(statements=statements, owners=owners, all_labels=all_labels,
                events=events, active=active, subjects=subjects,
                historical_aliases=historical_aliases, tag_aliases=tag_aliases,
                selected=selected, counts=counts, groups=groups,
                withdrawn=withdrawn, retained_mentions=retained_mentions,
                unselected_source_events=unselected_source_events)


def count_prose(data: dict) -> str:
    counts = data["counts"]
    return (
        f"The records associate {len(data['selected']):,} entries with the current statements of this paper: "
        f"{counts[TYPES[0]]:,} examinations of proof steps, "
        f"{counts[TYPES[1]]:,} independent re-derivations, "
        f"{counts[TYPES[2]]:,} computations or formal certificates, "
        f"{counts[TYPES[3]]:,} readings of proofs and applications, "
        f"{counts[TYPES[4]]:,} uses of background results without a fault found, and "
        f"{counts[TYPES[5]]:,} refutation records associated with their corrected statements. "
        f"These entries belong to {len(data['groups']):,} recorded evidence groups. "
        "Each event is counted once; entries sharing an evidence group retain that common group. "
        "One argument or calculation can be associated with several statements and kinds of examination. "
        "Each outcome specifies its scope and prior proof exposure."
    )


def summary(data: dict) -> dict:
    compact = lambda event: {key: event[key] for key in
        ("event_id", "statement_id", "type", "evidence_group")}
    return dict(
        paper=PAPER,
        inspected_utc=datetime.now(timezone.utc).isoformat(),
        current_formal_owners=len(data["statements"]),
        owner_kinds=dict(sorted(Counter(row.kind for row in data["statements"]).items())),
        current_statement_subject_identifiers=len(data["subjects"]),
        retained_historical_statement_aliases={alias: data["owners"][alias] for alias in data["historical_aliases"]},
        usable_statement_tag_aliases=sum(label in data["subjects"] for label in data["tag_aliases"].values()),
        selected_event_associations=len(data["selected"]),
        declared_evidence_groups=len(data["groups"]),
        events_using_event_id_group_fallback=sum(not event.get("evidence_group") for event in data["selected"]),
        counts={kind: data["counts"][kind] for kind in TYPES},
        excluded_wholly_withdrawn_event=compact(data["withdrawn"]),
        retained_events_mentioning_withdrawal=[compact(event) for event in data["retained_mentions"]],
        excluded_nonstatement_source_subjects=sorted({event["statement_id"] for event in data["unselected_source_events"]}),
        proposed_section_1_5_paragraph=count_prose(data),
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", nargs="?", choices=("inspect", "derive"), default="inspect")
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--show-selected", action="store_true", help="Print exact selected associations on stdout")
    parser.add_argument("--show-owners", action="store_true", help="Print structural owner identifiers on stdout")
    args = parser.parse_args()
    data = current_data(args.root.resolve())
    result = summary(data)
    if args.mode == "derive":
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return
    print("Paper III current-statement count inspection — read-only")
    print("Formal owners:", result["current_formal_owners"], result["owner_kinds"])
    print("Exact statement subjects:", result["current_statement_subject_identifiers"])
    print("Retained historical statement aliases:", result["retained_historical_statement_aliases"])
    print("Usable exact tag aliases:", result["usable_statement_tag_aliases"])
    print("Event associations:", result["selected_event_associations"])
    print("Recorded evidence groups:", result["declared_evidence_groups"])
    print("Empty-group event-ID fallbacks:", result["events_using_event_id_group_fallback"])
    for kind in TYPES:
        print(f"{kind}\t{result['counts'][kind]}")
    print("Excluded whole-event withdrawal:", WITHDRAWN_EVENT)
    print("Replacement retained:", REPLACEMENT_EVENT)
    print("Other retained events mentioning withdrawal:")
    for event in result["retained_events_mentioning_withdrawal"]:
        print(" ", event["event_id"], "|", event["statement_id"], "|", event["type"], "|", event["evidence_group"])
    print("Excluded nonstatement labels present in the current source:", result["excluded_nonstatement_source_subjects"])
    print("PROPOSED SECTION 1.5 PARAGRAPH")
    print(count_prose(data))
    if args.show_owners:
        print("OWNER STRUCTURE: identifier | kind | primary tag | source line")
        for row in data["statements"]:
            print(row.statement_id, row.kind, row.tag, row.line, sep=" | ")
    if args.show_selected:
        print("SELECTED: event_id | original subject | resolved subject | owner | type | group key")
        for event in data["selected"]:
            subject = data["tag_aliases"].get(event["statement_id"], event["statement_id"])
            print(event["event_id"], event["statement_id"], subject, data["owners"][subject],
                  event["type"], group_key(event), sep=" | ")
    print("No input, manuscript, shared table or derived file was written.")


if __name__ == "__main__":
    main()
