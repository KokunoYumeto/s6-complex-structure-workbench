"""Add requested descriptive subsection headings to three completed units."""
import csv
from datetime import datetime, timezone
from pathlib import Path
import S6_SERIES_PUBLISH_c8_integrate_units as units

root = Path(__file__).resolve().parent.parent
lane = root / "agents/continuation8_iii_weighted_units"
for key, name, title, label in [
    ("LN", "whole_fibre_initial_pairs", "Whole-fibre initial pairs", "maps:src:D.2.46"),
    ("LQ", "canonical_star_logs", "Canonical star logarithms", "maps:src:D.2.49"),
    ("LS", "vertical_corrections", "Vertical corrections", "maps:src:D.2.50"),
]:
    path = root / "agents/continuation8_iii_integration/units/weighted" / (name + ".tex")
    old = path.read_text()
    assert old.startswith(r"\begin{definition}")
    heading = "\\subsection{" + title + "}\n\n"
    text = heading + old
    units.check_permanent_identifiers(old, text)
    table = lane / ("S6_SERIES_PUBLISH_" + key + "_publication_defects.tsv")
    with table.open(newline="") as stream:
        reader = csv.DictReader(stream, delimiter="\t")
        fields = reader.fieldnames
        rows = list(reader)
    number = max(int(row["change_id"].split("-")[-2]) for row in rows) + 1
    for kind in ["D14", "D16"]:
        rows.append(dict(zip(fields, [f"III-C8-{key}-PUB-{number:03}-{kind}", kind, label,
            name + ".tex, beginning", "pending page concordance", "weighted/" + name + ".tex", "pending final build",
            "", heading, "Add the requested descriptive subsection heading so the fragment is an actual publication unit in its final position. No mathematical or identity change.",
            "exact heading read; root admission and global numbering pending"])))
    path.write_text(text, newline="\n")
    with table.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    review = lane / ("S6_SERIES_PUBLISH_" + key + "_unit_review.md")
    if review.exists():
        with review.open("a", newline="") as stream:
            stream.write("\n## Final-position heading\n\nThe exact subsequent edit adds `" + heading.strip() + "` before the input definition. "
                         "This supplies the descriptive subsection requested by root, adds no permanent identity, and preserves every mathematical line. "
                         "The current fragment has " + str(len(text.splitlines())) + " lines and the record has " + str(number) + " sequential edits in " + str(len(rows)) + " single-type rows. "
                         "Both heading lines and their immediate context were read. Root's global section numbering and reference expansion remain open.\n")
    print(key, "HEADING", title, "LINES", len(text.splitlines()), "SEQUENTIAL_EDITS", number, "DEFECT_ROWS", len(rows))
print("UTC", datetime.now(timezone.utc).isoformat(), "SHARED_WRITES0; AUTOMATIC_CRITERION_CREDIT0")
