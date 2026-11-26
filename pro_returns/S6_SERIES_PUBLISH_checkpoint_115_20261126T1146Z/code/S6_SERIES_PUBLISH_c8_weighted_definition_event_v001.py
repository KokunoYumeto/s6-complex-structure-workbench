"""Append an explicitly scoped used-and-rechecked input-definition event."""
import argparse
import csv
from datetime import datetime, timezone
from pathlib import Path

parser = argparse.ArgumentParser(description=__doc__)
for arg in ["unit", "tag", "label", "stem", "scope"]:
    parser.add_argument("--" + arg, required=True)
args = parser.parse_args()
root = Path(__file__).resolve().parent.parent
lane = root / "agents/continuation8_iii_weighted_units"
path = root / "agents/continuation8_iii_integration/units/weighted" / (args.stem + ".tex")
source = path.read_text()
label_at = source.index("\\label{" + args.label + "}")
start = source.rindex(r"\begin{definition}", 0, label_at)
end = source.index(r"\end{definition}", label_at) + len(r"\end{definition}")
definition = source[start:end]
assert "\\hypertarget{tag-" + args.tag + "}" in definition
print("WHOLE_DEFINITION", args.tag, args.label)
print(definition)
print("END_WHOLE_DEFINITION")
table = lane / ("S6_SERIES_PUBLISH_" + args.unit + "_CHECK_EVENTS.tsv")
with table.open(newline="") as stream:
    reader = csv.DictReader(stream, delimiter="\t")
    fields = reader.fieldnames
    rows = list(reader)
event_id = "III-C8-" + args.unit + "-" + args.tag + "-INPUT-READBACK"
assert not any(row["event_id"] == event_id for row in rows)
review = "agents/continuation8_iii_weighted_units/S6_SERIES_PUBLISH_" + args.unit + "_unit_review.md"
who = "GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; numerical reasoning effort not separately exposed; continuation eight weighted-unit editor"
now = datetime.now(timezone.utc).isoformat()
rows.append(dict(zip(fields, [args.label, "2026-11-25", who, "used and rechecked in this run",
    args.scope + " Whole definition read in the complete source and individually displayed again; input-definition scope only, no independent-proof credit or global-reference closure.",
    event_id, "continuation-eight-publication", review, "whole numbered input definition", "used and rechecked in this run", event_id,
    "", "", now, str(path.relative_to(root))])))
with table.open("w", newline="") as stream:
    writer = csv.DictWriter(stream, fieldnames=fields, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
with (root / review).open("a", newline="") as stream:
    stream.write("\n## Individual input-definition event\n\n" + args.tag + " / `" + args.label + "` has a separate `used and rechecked in this run` event at the whole-definition scope. " + args.scope + " No independent-proof credit or final-reference closure is added.\n")
print("UTC", now, "INDIVIDUAL_DEFINITION_EVENT", event_id, "SHARED_WRITES0")
