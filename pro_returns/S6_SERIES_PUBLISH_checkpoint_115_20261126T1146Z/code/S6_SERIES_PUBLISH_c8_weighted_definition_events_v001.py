"""Record individually scoped reading of the four completed input definitions."""
import csv
from datetime import datetime, timezone
from pathlib import Path

root = Path(__file__).resolve().parent.parent
lane = root / "agents/continuation8_iii_weighted_units"
who = "GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; numerical reasoning effort not separately exposed; continuation eight weighted-unit editor"
items = [
    ("LN", "Q200", "maps:def:whole-fibre-data", "whole_fibre_initial_pairs", "All21 marked profiles, positive section multiples and complete local narrowness-OR condition, total whole-fibre weights and specified filling/marking data were read and compared with the complete original and receiving theorem; GI1 remains at the identical input equation."),
    ("LQ", "Q201", "maps:def:canonical-star-data", "canonical_star_logs", "The full marked star basis and return, n=1 or3, positive integral k, order2k, all integer j,r,N, component reflection, marked j lift, R=2r−j and coprimality were read and compared against the complete original and receiver; SL1/SL2 retain their exact identities."),
    ("LS", "Q202", "maps:def:vertical-correction-data", "vertical_corrections", "The complete21-profile input, height denominator, all signed and zero a,b, actual section translation, integral component divisor and both line bundles were read; base pullback defines exactly the theorem correction property with no added positivity or narrowness."),
    ("LT", "Q203", "maps:def:invariant-chern-data", "invariant_chern_caps", "All seven additive types, actual original cap/line/section, invariant degrees with zero multiplicity pairing, orbit lengths/degrees/multiplicities and positive g,h for c nonzero were read; c=0 remains included and IC1/IC2 keep their exact identities."),
]
for key, tag, label, stem, scope in items:
    path = root / "agents/continuation8_iii_integration/units/weighted" / (stem + ".tex")
    text = path.read_text()
    start = text.index(r"\begin{definition}")
    end = text.index(r"\end{definition}", start) + len(r"\end{definition}")
    definition = text[start:end]
    assert "\\label{" + label + "}" in definition
    assert "\\hypertarget{tag-" + tag + "}" in definition
    print(key, tag, "BEGIN_WHOLE_DEFINITION", text.count("\n", 0, start)+1, text.count("\n", 0, end)+1)
    print(definition)
    print("END_WHOLE_DEFINITION")
    table = lane / ("S6_SERIES_PUBLISH_" + key + "_CHECK_EVENTS.tsv")
    with table.open(newline="") as stream:
        reader = csv.DictReader(stream, delimiter="\t")
        fields = reader.fieldnames
        rows = list(reader)
    event_id = "III-C8-" + key + "-" + tag + "-INPUT-READBACK"
    assert not any(row["event_id"] == event_id for row in rows)
    now = datetime.now(timezone.utc).isoformat()
    review = "agents/continuation8_iii_weighted_units/S6_SERIES_PUBLISH_" + key + "_unit_review.md"
    rows.append(dict(zip(fields, [label, "2026-11-25", who, "used and rechecked in this run",
        scope + " The whole definition was read as part of the complete publication source and individually displayed again; input-definition scope only, no independent-proof credit or global-reference closure.",
        event_id, "continuation-eight-publication", review, "whole numbered input definition", "used and rechecked in this run", event_id,
        "", "", now, str(path.relative_to(root))])))
    with table.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    with (root / review).open("a", newline="") as stream:
        stream.write("\n## Individual input-definition event\n\n" + tag + " / `" + label + "` has its own `used and rechecked in this run` event at the complete-definition scope: " + scope + " It adds no independent-proof credit; final numbering and links remain root's gates.\n")
print("FOUR_INDIVIDUAL_DEFINITION_EVENTS; SHARED_WRITES0; INDEPENDENT_CHECK_CREDIT0")
