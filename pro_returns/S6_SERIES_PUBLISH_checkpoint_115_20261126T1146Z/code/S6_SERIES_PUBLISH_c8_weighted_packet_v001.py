"""Serialize an editor's completed unit review into local proposal tables.

This copies human-readable criterion evidence from the completed review and
the explicitly supplied check outcome.  It does not inspect mathematics or
award a check automatically.  No shared table or canonical source is written.
"""
import argparse
import csv
from datetime import datetime, timezone
from pathlib import Path

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--unit", required=True)
parser.add_argument("--statement", required=True)
parser.add_argument("--fragment", required=True)
parser.add_argument("--outcome", required=True)
parser.add_argument("--program", action="append", default=[], help="printed path|repository path|sha256|description")
args = parser.parse_args()
root = Path(__file__).resolve().parent.parent
lane = root / "agents/continuation8_iii_weighted_units"
prefix = "S6_SERIES_PUBLISH_" + args.unit
review_path = lane / (prefix + "_unit_review.md")
review = review_path.read_text()
criteria = []
expected = {f"D{i:02}" for i in range(1, 28)} | {"Structure"}
for line in review.splitlines():
    if not line.startswith("| "):
        continue
    fields = [field.strip() for field in line.strip("|").split("|")]
    if fields[0] in expected:
        assert len(fields) == 2
        criteria.append([fields[0], "source-local complete; root admission and global integration pending", fields[1]])
assert len(criteria) == 28 and {row[0] for row in criteria} == expected
with (lane / (prefix + "_unit_criteria.tsv")).open("w", newline="") as stream:
    writer = csv.writer(stream, delimiter="\t", lineterminator="\n")
    writer.writerow(["criterion", "proposed_state", "evidence"])
    writer.writerows(criteria)
now = datetime.now(timezone.utc).isoformat()
event_id = "III-C8-" + args.unit + "-PUBLICATION-READBACK"
with (lane / (prefix + "_CHECK_EVENTS.tsv")).open("w", newline="") as stream:
    writer = csv.writer(stream, delimiter="\t", lineterminator="\n")
    writer.writerow(["statement_id", "date", "who", "type", "outcome", "event_id", "phase", "source_file", "source_row", "source_event_type", "evidence_group", "publish_input_file", "publish_input_row", "date_utc", "where"])
    writer.writerow([args.statement, "2026-11-25",
        "GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; numerical reasoning effort not separately exposed; continuation eight weighted-unit editor",
        "used and rechecked in this run", args.outcome, event_id,
        "continuation-eight-publication", str(review_path.relative_to(root)),
        "whole note", "used and rechecked in this run", event_id, "", "", now, args.fragment])
programs = []
repository_paths = (root.parent / "REPOSITORY_PROGRAM_PATHS.txt").read_text().splitlines()
for spec in args.program:
    row = spec.split("|", 3)
    assert len(row) == 4 and len(row[2]) == 64
    assert row[1] in repository_paths or (root / row[1]).is_file()
    programs.append(row)
with (lane / (prefix + "_program_table_proposals.tsv")).open("w", newline="") as stream:
    writer = csv.writer(stream, delimiter="\t", lineterminator="\n")
    writer.writerow(["printed_path", "repository_path", "sha256", "description"])
    writer.writerows(programs)
for path in lane.glob(prefix + "_*"):
    if path.suffix in {".md", ".tsv", ".out", ".err"}:
        assert b"\r" not in path.read_bytes()
print("UTC", now)
print("UNIT", args.unit, "CRITERION_EVIDENCE_ROWS", len(criteria), "PROPOSED_USED_RECHECKED_EVENTS1")
print("PROGRAM_PROPOSALS", len(programs), "SHARED_WRITES0; AUTOMATIC_CRITERION_CREDIT0; INDEPENDENT_CHECK_CREDIT0")
