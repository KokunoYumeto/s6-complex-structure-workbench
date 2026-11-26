#!/usr/bin/env python3
"""Prepare exact code replacements for the later final-layout derivation.

This program writes only a guarded review proposal. It does not import or
run the final derivation, change its source, or refresh any derived record.
"""
import ast
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET = "code/S6_SERIES_PUBLISH_c8_III_derive_final.py"
OUT = ROOT.parent.parent / "tmp/c9_counts_provenance/S6_SERIES_PUBLISH_c9_III_derive_integration.json"


def proposals():
    source = (ROOT / TARGET).read_text(encoding="utf-8")
    assert "\r" not in source
    changes = []

    def add(name, old, new, reason):
        assert old != new and source.count(old) == 1, name
        changes.append(dict(change_id=name, path=TARGET, old_text=old,
                            new_text=new, reason=reason))

    add("C9-III-DERIVE-AUTHORITY",
        "The approved c8 III count selector is the sole event-selection authority.",
        "The approved c9 wrapper retains the c8 selection rules and adds only the\n"
        "eight literal intake associations verified against their original rows.",
        "Name the selector actually used below, without changing the mathematical or page-reading scope.")
    add("C9-III-DERIVE-INTAKE-INPUT",
        '    inputs.read(ROOT / TAGS)\n    data = selector.current_data(ROOT)\n',
        '    inputs.read(ROOT / TAGS)\n'
        '    inputs.read(ROOT.parent / "CLAUDE_INTAKE_CHECK_EVENTS_cp92_100.tsv")\n'
        '    data = selector.current_data(ROOT)\n',
        "The original intake table is now an input to the verified finite association; register its exact bytes with the existing unchanged-input guard.")
    add("C9-III-DERIVE-INTAKE-FREEZE",
        '    require(set(frozen["recorded_evidence_groups"]) == data["groups"], "Evidence groups changed")\n',
        '    require(set(frozen["recorded_evidence_groups"]) == data["groups"], "Evidence groups changed")\n'
        '    require(frozen["literal_intake_associations"] == data["exact_intake_details"],\n'
        '            "The eight verified intake associations changed after the count freeze")\n',
        "Compare the exact event-ID/full-subject/owner/tag map against the frozen count result, alongside the existing selected-ID, type and group checks.")
    add("C9-III-DERIVE-EVENT-MAP",
        'def event_map(data):\n'
        '    result = defaultdict(list)\n'
        '    for event in data["events"]:\n'
        '        result[data["tag_aliases"].get(event["statement_id"], event["statement_id"])].append(event)\n'
        '    return result',
        'def event_map(data, selector):\n'
        '    result = defaultdict(list)\n'
        '    for event in data["events"]:\n'
        '        result[selector.resolved_subject(data, event)].append(event)\n'
        '    return result',
        "Attach each unchanged event object once using the validated event-ID map or the existing exact tag rule.")
    add("C9-III-DERIVE-INVENTORY-CALL",
        '    events = event_map(data)\n',
        '    events = event_map(data, selector)\n',
        "Use the same subject resolver for inventory event lists and the selected statement totals.")
    add("C9-III-DERIVE-INVENTORY-SCOPE",
        'current_event_scope="Exact original subject, including retained withdrawn records. Only IDs selected by the approved III selector enter current statement counts; events are not transferred as independent checks."',
        'current_event_scope="Every event retains its exact original fields, including retained withdrawn records. The approved selector resolves exact tag aliases and eight individually verified intake associations. Only its selected IDs enter current statement counts; this association adds no independent-check credit."',
        "Record the actual finite association rule while preserving original subject fields in canonical_check_events.")
    add("C9-III-DERIVE-INVENTORY-SUMMARY",
        'f"{len(direct)} retained exact-subject event rows; {len(live)} selected current statement associations; "',
        'f"{len(direct)} retained event rows attached by the reviewed subject resolver; {len(live)} selected current statement associations; "',
        "Eight raw subjects are descriptive strings; the generator must describe their reviewed association accurately.")
    add("C9-III-DERIVE-CHECK-DOCUMENT",
        '        subject = data["tag_aliases"].get(event["statement_id"], event["statement_id"])\n',
        '        subject = selector.resolved_subject(data, event)\n',
        "Display all eight selected intake events under their verified formal owners; the printed raw Subject field is unchanged.")
    add("C9-III-DERIVE-CHECK-DOCUMENT-SCOPE",
        'Every event keeps its original subject, type, who, outcome and evidence group. The designated withdrawn event is retained below and excluded from the counts.',
        'Every event keeps its original subject, type, who, outcome and evidence group. Eight intake rows use the exact event-ID, full-subject and tag associations verified by S6_SERIES_PUBLISH_c9_III_check_counts.py; their original five intake fields remain verbatim. The designated withdrawn event is retained below and excluded from the counts.',
        "Explain why the displayed owner can differ from the unchanged raw subject, using precisely the authorized finite map.")
    add("C9-III-DERIVE-EMPTY-ENTRY",
        'No authoritative event has an exact subject assigned to this entry. Its cited inputs retain their own records.',
        'No authoritative event is attached to this entry by the reviewed subject resolver. Its cited inputs retain their own records.',
        "Keep the empty-entry description consistent with the same explicit subject resolver.")
    add("C9-III-DERIVE-SCOPE-COUNTS",
        '    resolve = lambda event: data["tag_aliases"].get(event["statement_id"], event["statement_id"])\n',
        '    resolve = lambda event: selector.resolved_subject(data, event)\n',
        "Use the same eight exact associations in each existing scope, retaining the current-scope equality assertion against selected IDs.")
    add("C9-III-DERIVE-PER-STATEMENT-CALL",
        '    by_subject = event_map(data)\n',
        '    by_subject = event_map(data, selector)\n',
        "Use the same resolver for per-statement summaries; their historical row domain remains unchanged.")
    add("C9-III-DERIVE-SELECTOR-IMPORT",
        '    selector = load_helper("S6_SERIES_PUBLISH_c8_III_check_counts.py", "s6_iii_count_authority")\n',
        '    selector = load_helper("S6_SERIES_PUBLISH_c9_III_check_counts.py", "s6_iii_count_authority")\n',
        "Load the reviewed c9 wrapper, which exports the unchanged c8 type, evidence-group and prose helpers.")

    candidate = source
    for item in changes:
        assert candidate.count(item["old_text"]) == 1, item["change_id"]
        candidate = candidate.replace(item["old_text"], item["new_text"], 1)
    ast.parse(candidate, filename=TARGET)
    assert 'data["tag_aliases"].get(event["statement_id"], event["statement_id"])' not in candidate
    assert candidate.count("selector.resolved_subject(data, event)") == 3
    assert candidate.count("event_map(data, selector)") == 3  # definition and two callers
    assert candidate.count('require(event["event_id"] not in displayed, "Event displayed twice")') == 1
    assert candidate.count('require(selected <= displayed, "A selected event is absent from the check document")') == 1
    assert 'Subject: `{event[\'statement_id\']}`' in candidate
    assert "\r" not in candidate
    return changes


def main():
    changes = proposals()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(changes, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(f"Prepared {len(changes)} exact guarded code replacements in {OUT}.")
    print("All three subject-resolution paths use the reviewed c9 resolver; raw event subjects and uniqueness/coverage guards remain.")
    print("Candidate parsed as Python. No final-layout derivation was imported or run; no master or derived table was written.")


if __name__ == "__main__":
    main()
