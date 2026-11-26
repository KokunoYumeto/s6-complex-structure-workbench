"""Record the actually completed current10 source admission in the root narrative."""
from pathlib import Path
import csv
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
csv.field_size_limit(100_000_000)
with (ROOT / "S6_SERIES_PUBLISH_findings_III.tsv").open(newline="") as stream:
    rows = list(csv.DictReader(stream, delimiter="\t"))
row, = [r for r in rows if r["id"] == "P15"]
assert row["status"] == "done"
stamp = row["date_utc"]
source_sha = hashlib.sha256((ROOT / "S6_SERIES_PUBLISH_III.tex").read_bytes()).hexdigest()
assert source_sha == "5c03702c24467c3f471009cecd748be5e2d8138082c9fbc9abd13ddfe77372fe"
counts = json.loads((ROOT / "records/S6_SERIES_PUBLISH_III_current_check_counts.json").read_text())
assert counts["selected_event_associations"] == 1253 and counts["declared_evidence_groups"] == 964
assert not (ROOT / "code/S6_SERIES_PUBLISH_c9_candidate10_admission_apply.err").read_bytes()
actual = (ROOT / "code/S6_SERIES_PUBLISH_c9_candidate10_admission_apply.out").read_text()
assert "Actual canonical selector after admission: 1253 associations; 964 groups." in actual
assert "Admitted source/events/exact status rows and matching count/provenance fields." in actual
header = "## Current10 complete source admission — " + stamp
text = "\n\n" + header + "\n\n" + (
    "Root executed the fully reviewed admission successfully and read its complete actual output and empty error file. "
    "The accepted source SHA256 is " + source_sha + ". All106 source guards and three count/provenance edits are recorded in109 exact defect rows. "
    "Ten exposed use/rechecking associations in eight evidence groups were appended once, giving1253 associations in964 groups and category counts422/2/58/651/90/30. "
    "No independent-proof or computation category was incremented.\n\n"
    "The ten exact D20 naming criteria and the supplied P15 source finding are done. Six D23 criteria reopen for successor layout review, with all prior image history retained. "
    "The already-open main-theorem punctuation criterion remains open. Actual PaperIII unit state is3139done/109open:58D14,43D23,2D04 and6D18. "
    "All128 required checks remain done. The build is open pending currentcandidate11 and legacycandidate10; both compiler runs have begun. "
    "Source is frozen for the build and subsequent actual changed-page reading.\n\n"
    "This is qualifying source-criterion movement after the11:30:22UTC review80 boundary; it does not revise that review\'s historical no-movement interval or assign image credit. "
    "Final source/PDF agreement, all remaining exact image and provenance gates, PaperIV and the joint five-paper step remain. "
    "The report remains INCOMPLETE. Next scheduled checkpoint115:11:45:22UTC; review81:12:30:22UTC.\n")
for name in ("PROGRESS_LEDGER.md", "S6_SERIES_PUBLISH_report.md", "agents/continuation9_root/S6_SERIES_PUBLISH_c9_candidate10_packet_comparison.md"):
    path = ROOT / name
    original = path.read_text()
    assert header not in original
    path.write_text(original + text, newline="\n")
print(header)
print("Actual source admission recorded; build and all successor-image gates remain open.")
print("No new mathematical-check event or count refresh is performed by this narrative record.")

