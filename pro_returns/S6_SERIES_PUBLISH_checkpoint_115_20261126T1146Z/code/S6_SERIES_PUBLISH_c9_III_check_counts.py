#!/usr/bin/env python3
"""Read-only Paper III count selector with eight literal intake associations.

Retain the c8 current-owner, historical-statement, exact-tag, six-type,
unique-event and whole-withdrawal rules unchanged. Add only the eight
root-reviewed intake rows listed below, verifying their complete original
subjects, exact event IDs, original five fields and current primary tag.
No raw event, manuscript, tag table or other master is changed.
"""
from pathlib import Path
from collections import Counter
import argparse
import importlib.util
import json
import sys

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("s6_c8_iii_count_selector", ROOT / "code/S6_SERIES_PUBLISH_c8_III_check_counts.py")
C8 = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = C8
SPEC.loader.exec_module(C8)

# The final-layout derivation can use the unchanged c8 presentation helpers
# while resolving the eight intake associations through resolved_subject.
TYPES = C8.TYPES
group_key = C8.group_key
count_prose = C8.count_prose

INTAKE = (
    ("01", "maps:src:D.2.4 (tag 02LG), the D27 refinement c8-III-02LG-residual-models (event publish:c8:III:02LG:residual-refinement)", "maps:src:D.2.4", "02LG"),
    ("02", "maps:src:C.1.4 (tag 02K5, Proposition 5.5)", "maps:src:C.1.4", "02K5"),
    ("03", "mapsIII:rem:kummer-finite-values (tag Q018, Remark 5.7)", "mapsIII:rem:kummer-finite-values", "Q018"),
    ("04", "mapsD:repair:collision-realization (tag 02OG, Theorem 6.4)", "mapsD:repair:collision-realization", "02OG"),
    ("05", "maps:src:D.2.43 (tag 02LK, Theorem 6.7)", "maps:src:D.2.43", "02LK"),
    ("06", "maps:src:D.2.10 (tag 02KK, Theorem 7.12)", "maps:src:D.2.10", "02KK"),
    ("07", "maps:src:D.2.11 (tag 02KL, Theorem 7.14)", "maps:src:D.2.11", "02KL"),
    ("08", "maps:src:D.2.12 (tag 02KM, Theorem 8.2)", "maps:src:D.2.12", "02KM"),
)
ORIGINAL_FIELDS = ("statement_id", "date", "who", "type", "outcome")


def current_data(root=ROOT):
    root = Path(root)
    data = C8.current_data(root)
    event_by_id = {row["event_id"]: row for row in data["events"]}
    source = C8.read_rows(root.parent / "CLAUDE_INTAKE_CHECK_EVENTS_cp92_100.tsv")
    assert len(source) == len(INTAKE) == 8
    primary = {owner.statement_id: owner for owner in data["statements"]}
    associations = {}
    details = []
    for original, (suffix, literal, subject, tag) in zip(source, INTAKE):
        event_id = "publish:c9:claude-intake-cp92-100:" + suffix
        row = event_by_id[event_id]
        assert row["statement_id"] == original["statement_id"] == literal, event_id
        assert {key: row[key] for key in ORIGINAL_FIELDS} == original, event_id
        assert subject in primary and data["owners"][subject] == subject, subject
        assert primary[subject].tag == tag, (subject, tag)
        assert data["tag_aliases"]["tag:" + tag] == subject, (subject, tag)
        assert row["type"] in C8.TYPES, event_id
        associations[event_id] = subject
        details.append({"event_id": event_id, "literal_recorded_subject": literal,
                        "current_primary_subject": subject, "verified_primary_tag": tag})
    base_ids = {row["event_id"] for row in data["selected"]}
    assert not base_ids.intersection(associations), "The c8 selector already selects a listed literal intake row; review this wrapper before counting."
    selected = [row for row in data["events"] if row["event_id"] in base_ids or row["event_id"] in associations]
    assert len(selected) == len(base_ids) + 8
    assert len({row["event_id"] for row in selected}) == len(selected)
    data.update(selected=selected, counts=Counter(row["type"] for row in selected),
                groups={C8.group_key(row) for row in selected},
                exact_intake_associations=associations, exact_intake_details=details,
                base_selected_event_associations=len(base_ids))
    return data


def resolved_subject(data, event):
    return data["exact_intake_associations"].get(event["event_id"],
        data["tag_aliases"].get(event["statement_id"], event["statement_id"]))


def summary(data):
    result = C8.summary(data)
    result.update(selector="c8 current_data plus eight exact c9 intake associations",
                  base_selected_event_associations=data["base_selected_event_associations"],
                  literal_intake_associations=data["exact_intake_details"])
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", nargs="?", choices=("inspect", "derive"), default="inspect")
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--show-selected", action="store_true")
    args = parser.parse_args()
    data = current_data(args.root.resolve())
    result = summary(data)
    if args.mode == "derive":
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return
    print("Paper III current-statement count inspection; exact eight-row intake association")
    print("Current formal owners:", result["current_formal_owners"])
    print("Current statement subject identifiers:", result["current_statement_subject_identifiers"])
    print("Retained historical statement aliases:", result["retained_historical_statement_aliases"])
    print("Base selected event associations:", data["base_selected_event_associations"])
    print("Additional literal intake associations:", len(data["exact_intake_associations"]))
    print("Selected event associations:", result["selected_event_associations"])
    print("Declared evidence groups:", result["declared_evidence_groups"])
    print("Event-ID group fallbacks:", result["events_using_event_id_group_fallback"])
    for kind in C8.TYPES:
        print(kind, result["counts"][kind], sep="\t")
    print("Excluded whole-event withdrawal:", C8.WITHDRAWN_EVENT)
    print("Replacement Euler event retained:", C8.REPLACEMENT_EVENT)
    print("Literal intake associations; original fields unchanged:")
    for item in data["exact_intake_details"]:
        print(item["event_id"], item["literal_recorded_subject"], item["current_primary_subject"], item["verified_primary_tag"], sep=" | ")
    print("PROPOSED SECTION 1.5 PARAGRAPH")
    print(C8.count_prose(data))
    if args.show_selected:
        print("SELECTED: event_id | original subject | resolved subject | current owner | type | group")
        for event in data["selected"]:
            subject = resolved_subject(data, event)
            print(event["event_id"], event["statement_id"], subject, data["owners"][subject], event["type"], C8.group_key(event), sep=" | ")
    print("No raw event, manuscript, tag table, inventory, count record or provenance master was written.")


if __name__ == "__main__":
    main()
