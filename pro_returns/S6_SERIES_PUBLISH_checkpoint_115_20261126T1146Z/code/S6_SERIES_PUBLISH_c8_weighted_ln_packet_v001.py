"""Write LN's local source-review proposals, without shared-table mutations."""
import csv
from datetime import datetime, timezone
from pathlib import Path

root = Path(__file__).resolve().parent.parent
lane = root / "agents/continuation8_iii_weighted_units"
defects = lane / "S6_SERIES_PUBLISH_LN_publication_defects.tsv"
with defects.open(newline="") as stream:
    reader = csv.DictReader(stream, delimiter="\t")
    fields = reader.fieldnames
    rows = list(reader)
assert len(rows) == 64
expanded = []
for row in rows:
    for kind in row["type"].split(";"):
        if kind == "structure":
            continue
        assert kind in {f"D{i:02}" for i in range(1, 28)}
        item = dict(row)
        item["type"] = kind
        item["change_id"] += "-" + kind
        item["review_status"] = "source edit and whole-proof comparison complete; root admission, global integration and page concordance pending"
        expanded.append(item)
with defects.open("w", newline="") as stream:
    writer = csv.DictWriter(stream, fieldnames=fields, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(expanded)

review = (lane / "S6_SERIES_PUBLISH_LN_unit_review.md").read_text()
criteria = []
for line in review.splitlines():
    if line.startswith("| D") or line.startswith("| Structure |"):
        parts = [x.strip() for x in line.strip("|").split("|")]
        if parts[0] in {f"D{i:02}" for i in range(1, 28)} | {"Structure"}:
            assert len(parts) == 2
            criteria.append([parts[0], "source-local complete; root admission pending", parts[1]])
assert len(criteria) == 28
assert len({row[0] for row in criteria}) == 28
with (lane / "S6_SERIES_PUBLISH_LN_unit_criteria.tsv").open("w", newline="") as stream:
    writer = csv.writer(stream, delimiter="\t", lineterminator="\n")
    writer.writerow(["criterion", "proposed_state", "evidence"])
    writer.writerows(criteria)

now = datetime.now(timezone.utc).isoformat()
with (lane / "S6_SERIES_PUBLISH_LN_CHECK_EVENTS.tsv").open("w", newline="") as stream:
    writer = csv.writer(stream, delimiter="\t", lineterminator="\n")
    writer.writerow(["statement_id", "date", "who", "type", "outcome", "event_id", "phase", "source_file", "source_row", "source_event_type", "evidence_group", "publish_input_file", "publish_input_row", "date_utc", "where"])
    writer.writerow(["maps:src:D.2.46", "2026-11-25",
        "GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; numerical reasoning effort not separately exposed; continuation eight weighted-unit editor",
        "used and rechecked in this run",
        "Read the whole repaired1193-line LN unit, all released original statement/proof/following auxiliary, complete comparison/source/admission notes, and whole1113-line publication candidate plus exact readback changes to1115 lines. One numbered input definition Q200, one theorem/proof; all12 old labels/targets preserved. Compared every local cap and global group/homology map and parameter scope. Consolidated the earlier bar/freeness derivation through identity lattice/peripheral maps, explicit period inverses and exact index conversion; retained all five Thom columns by their existing identities and every torsion/sign convention. Preserved admitted support-map D25 repair. This is a publication rewrite comparison; no independent-proof credit and no historical program rerun. Source-local28-criterion proposal only; root admission, global references/bibliography, build and rendered-page gates remain separate.",
        "III-C8-LN-PUBLICATION-READBACK", "continuation-eight-publication",
        "agents/continuation8_iii_weighted_units/S6_SERIES_PUBLISH_LN_unit_review.md", "whole note",
        "used and rechecked in this run", "III-C8-LN-PUBLICATION", "", "", now,
        "agents/continuation8_iii_integration/units/weighted/whole_fibre_initial_pairs.tex"])

prefix = "pro_returns/S6_10_PAPERS_checkpoint_15_20261119T1045Z/S6_10_PAPERS/code/III/"
programs = [
    ["code/III/manifolds_general_initial.py", prefix + "manifolds_general_initial.py",
     "f581acf2eaef5e40001ad8b27d6f93be7b213e9b42831853213e6dc227c5d669",
     "Whole-fibre integral presentations; historical source consultation and comparisons are scoped in the admitted LN source note."],
    ["code/III/manifolds_general_initial_audit.py", prefix + "manifolds_general_initial_audit.py",
     "2e39ea4d080e73586b1be6500c930fd705ce0434940fcfc2c42638baafebeb",
     "Recorded whole-fibre examples and integer closure data; exact source hash and archive-reading scope from the admitted LN source note."],
]
# The second historical hash is copied exactly from that record, not inferred
# from a similarly named source elsewhere in the attached tree.
programs[1][2] = "2e39ea4d080e73586b1be6500c930fd705cdce0434940fcfc2c42638baafebeb"
paths = (root.parent / "REPOSITORY_PROGRAM_PATHS.txt").read_text().splitlines()
for _, repository_path, digest, _ in programs:
    assert repository_path in paths and len(digest) == 64
with (lane / "S6_SERIES_PUBLISH_LN_program_table_proposals.tsv").open("w", newline="") as stream:
    writer = csv.writer(stream, delimiter="\t", lineterminator="\n")
    writer.writerow(["printed_path", "repository_path", "sha256", "description"])
    writer.writerows(programs)
for path in lane.glob("S6_SERIES_PUBLISH_LN_*"):
    if path.suffix in {".md", ".tsv", ".out", ".err"}:
        assert b"\r" not in path.read_bytes()
print("UTC", now)
print("SEQUENTIAL_EDITS", len(rows), "DEFECT_ROWS_BY_SINGLE_TYPE", len(expanded))
print("SOURCE_CRITERIA", len(criteria), "PROPOSED_USED_RECHECKED_EVENTS", 1, "PROGRAM_PROPOSALS", len(programs))
print("SHARED_WRITES", 0, "AUTOMATIC_CRITERION_CREDIT", 0, "INDEPENDENT_CHECK_CREDIT", 0)
