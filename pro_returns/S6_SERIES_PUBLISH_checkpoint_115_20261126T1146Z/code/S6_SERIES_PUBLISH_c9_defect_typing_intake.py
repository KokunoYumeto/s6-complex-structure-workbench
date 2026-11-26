#!/usr/bin/env python3
"""Apply the prompt's bounded defect-type corrections and exact intake merge.

Run in the merged checkpoint directory. Existing mathematical text, check
outcomes, defect descriptions and review states are preserved. This records
no new proof check: the eight appended events retain their source attribution.
"""
from __future__ import annotations

import csv
import io
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
csv.field_size_limit(2**30)


def read_table(path: Path):
    with path.open(encoding="utf-8", newline="") as stream:
        reader = csv.DictReader(stream, delimiter="\t")
        fields = reader.fieldnames
        rows = list(reader)
    assert fields is not None
    assert all(None not in row for row in rows)
    return fields, rows


def write_table(path: Path, fields, rows):
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=fields, delimiter="\t",
                            lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    data = stream.getvalue()
    assert "\r" not in data
    path.write_text(data, encoding="utf-8", newline="\n")


def tokens(value: str):
    return tuple(part.strip() for part in re.split(r"[;,/]", value))


def prior_guard_types(tag: str, folder: str, cutoff: int, statement: bool):
    path = ROOT / f"agents/continuation7_iii_{folder}/S6_SERIES_PUBLISH_III_{tag}_defects.tsv"
    _, rows = read_table(path)
    selected = []
    for row in rows:
        match = re.search(r":(\d+)", row["old_location"])
        assert match, row["change_id"]
        in_statement = int(match[1]) <= cutoff
        if in_statement == statement:
            selected.append(row)
    assert selected
    types = sorted({kind for row in selected for kind in tokens(row["type"])})
    return ";".join(types), path.relative_to(ROOT).as_posix(), [r["change_id"] for r in selected]


def main():
    defect_path = ROOT / "S6_SERIES_PUBLISH_defects_III.tsv"
    fields, defects = read_table(defect_path)
    original = [dict(row) for row in defects]
    by_id = {row["change_id"]: row for row in defects}
    assert len(by_id) == len(defects)
    decisions = []

    guards = [
        ("III-C8-APPLY-087-02L1-1", "D26;D27", "02L1", "nonstar", 12835, True),
        ("III-C8-APPLY-088-02L1-1", "D26;D27", "02L1", "nonstar", 12835, False),
        ("III-C8-APPLY-091-02L3-1", "D25;D26;D27", "02L3", "profile_synthesis", 13416, True),
        ("III-C8-APPLY-092-02L3-1", "D25;D26;D27", "02L3", "profile_synthesis", 13416, False),
        ("III-C8-APPLY-103-02LA-1", "D25;D26;D27", "02LA", "weighted_engel", 14837, True),
        ("III-C8-APPLY-104-02LA-1", "D25;D26;D27", "02LA", "weighted_engel", 14837, False),
    ]
    for change_id, previous, tag, folder, cutoff, statement in guards:
        replacement, source, detailed_ids = prior_guard_types(tag, folder, cutoff, statement)
        basis = (f"Union of the admitted detailed {tag} "
                 f"{'statement' if statement else 'proof'} defect types at the original guard's "
                 f"line range in {source}: " + ", ".join(detailed_ids) + ".")
        decisions.append((change_id, previous, replacement, basis))

    decisions.extend([
        ("III-C8-APPLY-127-02LM-1", "D45", "D27",
         "The guard changes eight of eleven smooth assignments using P=-K/2 mod b; "
         "the existing 02LM D27 refinement and its refuted event already record this finding. "
         "D45 is an equation-prefix string and is absent from the defect register."),
        ("III-C8-APPLY-128-02LM-1", "D45", "D27",
         "The proof supplies the actual critical-chain K, spin invariant P and refined "
         "models for the existing 02LM D27 finding; no additional finding is created."),
        ("III-C8-THREE-PUB-047-D27", "D27", "D20;D22",
         "The edit specifies z_E=z_add/omega_s, its inverse, tau, zeta_G and the "
         "exponential coordinate, making the period convention and its maps explicit. "
         "Its recorded reason preserves every unit and lattice."),
        ("III-C8-THREE-READBACK-019-D27", "D27", "D18;D20;D22",
         "The edit states Thomas's coefficient groups, the odd-prime cochain formula, "
         "its p=3,m=1 specialization and the relative/suspension argument, and adds the "
         "exact cited locators. These are citation, convention and explanatory fixes; "
         "the recorded general and specialized conclusions are both retained."),
        ("III-C8-LV-PUB-038-D27", "D27", "D02;D22",
         "The edit replaces the defensive 'not merely' clause with the full cross-product "
         "basis, coordinate map and inverse detectors for mu. Its recorded reason "
         "preserves the classification and coefficient scope."),
        ("c8-III-regular-025", "D06/D14/D20/D27", "D14;D22",
         "The edit replaces dependence on later cone constructions with a defined "
         "cone, projection p, section and two paths proving the nonextension at the "
         "vertex. It fixes forward dependence and supplies the explicit reason/maps. "
         "Neither old nor new passage asserts a smooth classification."),
    ])

    changed_decisions = []
    for change_id, previous, replacement, basis in decisions:
        row = by_id[change_id]
        assert row["type"] in (previous, replacement), (change_id, row["type"])
        if row["type"] != replacement:
            row["type"] = replacement
            changed_decisions.append(change_id)

    separator_changes = []
    for row in defects:
        before = row["type"]
        parts = tokens(before)
        assert parts and all(re.fullmatch(r"D\d{2}", part) for part in parts)
        after = ";".join(parts)
        # Parsing the output recovers exactly the input's ordered type list.
        assert tokens(after) == parts
        if before != after:
            separator_changes.append((row["change_id"], before, after))
            row["type"] = after
    register = {row["type_id"] for row in csv.DictReader((ROOT / "S6_DEFECT_REGISTER.csv").open())}
    assert all(set(tokens(row["type"])) <= register for row in defects)
    assert len(defects) == len(original)
    for before, after in zip(original, defects):
        assert all(before[key] == after[key] for key in fields if key != "type")
    write_table(defect_path, fields, defects)
    assert read_table(defect_path) == (fields, defects)

    intake_path = ROOT.parent / "CLAUDE_INTAKE_CHECK_EVENTS_cp92_100.tsv"
    intake_fields, intake = read_table(intake_path)
    assert intake_fields == ["statement_id", "date", "who", "type", "outcome"]
    assert len(intake) == 8
    event_path = ROOT / "CHECK_EVENTS.tsv"
    event_fields, events = read_table(event_path)
    old_events = [dict(row) for row in events]
    keys = set(tuple(row[k] for k in intake_fields) for row in events)
    added = []
    for number, source in enumerate(intake, 1):
        key = tuple(source[k] for k in intake_fields)
        matches = [row for row in events if tuple(row[k] for k in intake_fields) == key]
        assert len(matches) <= 1
        if matches:
            continue
        event_id = f"publish:c9:claude-intake-cp92-100:{number:02d}"
        assert not any(row["event_id"] == event_id for row in events)
        target = {field: "" for field in event_fields}
        target.update(source)
        target.update(event_id=event_id, phase="continuation9-intake",
                      source_file=intake_path.name, source_row=str(number + 1),
                      source_event_type=source["type"], evidence_group=event_id,
                      publish_input_file=intake_path.name, publish_input_row=str(number + 1))
        assert all(target[field] == source[field] for field in intake_fields)
        events.append(target)
        keys.add(key)
        added.append(event_id)
    assert events[:len(old_events)] == old_events
    write_table(event_path, event_fields, events)
    assert read_table(event_path) == (event_fields, events)
    for source in intake:
        assert sum(all(row[k] == source[k] for k in intake_fields) for row in events) == 1

    review = ROOT / "agents/continuation9_defect_records/S6_SERIES_PUBLISH_III_defect_typing_review.md"
    review.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Paper III defect typing and intake, 26 November 2026",
        "",
        "The twelve requested defect cells were reviewed against their old/new passages, "
        "recorded reasons, the 27-type register and the cited detailed comparison rows. "
        "The type field alone changes. All other fields, including the historical "
        "identifiers with D27 in their names, remain exactly as received.",
        "",
        "## Exact type decisions", "",
        "| Change id | Previous type | Corrected type | Reason |",
        "| --- | --- | --- | --- |",
    ]
    for change_id, previous, replacement, basis in decisions:
        lines.append(f"| {change_id} | {previous} | {replacement} | {basis} |")
    lines.extend([
        "", "## Mathematical scope", "",
        "The 02L1 proof row retains the already recorded D25 physical-circle counterexample "
        "and the same smooth conclusion. Its exact event is "
        "`publish:c7:III:02L1:physical-fan-assertion-corrected`. The 02LA statement row "
        "retains D26 at the weight-one endpoint. The 02L3 comparison preserves all "
        "twenty-one counts and its smooth conclusion. The 02LM rows record the same "
        "existing D27 refinement. This review creates no new D27 instance and awards "
        "no proof-check or unit-completion credit.",
        "", "## Type separator", "",
        "Every multiple-type field now uses a semicolon. The program splits each input "
        "on comma, slash or semicolon and joins the identical ordered token list with "
        "semicolons. Parsing that output recovers exactly the same list. All resulting "
        "tokens are members of the register. No other field is changed.",
        "", "## Intake", "",
        "All eight supplied rows from `CLAUDE_INTAKE_CHECK_EVENTS_cp92_100.tsv` occur "
        "exactly once in `CHECK_EVENTS.tsv`. Each of the five supplied fields is "
        "identical to its source value. Existing events remain unchanged. Event ids "
        "`publish:c9:claude-intake-cp92-100:01` through `:08` and source-row metadata "
        "identify the additions. The attribution, event types, limited scopes and "
        "explicit limits of the original outcomes are preserved. No reading-only "
        "event from the later five-paper merge is added here.",
        "", "The applying program and its actual output are "
        "`code/S6_SERIES_PUBLISH_c9_defect_typing_intake.py` and its `.out` file.", "",
    ])
    review.write_text("\n".join(lines), encoding="utf-8", newline="\n")
    print(f"Reviewed type decisions: {len(decisions)}; changed this execution: {len(changed_decisions)}")
    print(f"Separator-only cells changed this execution: {len(separator_changes)}")
    print(f"Defect rows: {len(defects)}; all other fields preserved; all types registered")
    print(f"Intake rows: {len(intake)}; added this execution: {len(added)}")
    print(f"Check-event rows before/after: {len(old_events)}/{len(events)}")
    print("Every source intake row occurs exactly once with all five fields unchanged")
    print("All written text is LF; no new mathematical check or D27 finding")
    print(review.relative_to(ROOT))


if __name__ == "__main__":
    main()
