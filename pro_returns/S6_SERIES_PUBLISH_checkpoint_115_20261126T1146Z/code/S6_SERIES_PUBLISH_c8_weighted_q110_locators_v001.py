"""Propose exact LN/LQ citations to the created, wholly read Q110 input."""
import csv
from datetime import datetime, timezone
from pathlib import Path
import S6_SERIES_PUBLISH_c8_integrate_units as units

root = Path(__file__).resolve().parent.parent
lane = root / "agents/continuation8_iii_weighted_units"
directory = root / "agents/continuation8_iii_integration/units/weighted"
definition = (root / "agents/continuation8_iii_integration/units/foundations/elliptic_catalogue.tex").read_text()
assert definition.count(r"\label{mapsIII:def:elliptic-marked-data}") == 1
changes = [
    ("LQ", "canonical_star_logs", "maps:src:D.2.49",
     r"The selected fibre labels are their positions, starting at one, in the component-data table in the proof of \ref{maps:src:D.2.23}.",
     r"The selected fibre labels are their positions, starting at one, in the ordered table of Definition~\ref{mapsIII:def:elliptic-marked-data}.",
     "Q110 now contains the exact ordered table. All twelve selected positions, fibre types and component data are unchanged; its peripheral index is one-based here."),
    ("LN", "whole_fibre_initial_pairs", "maps:src:D.2.46",
     "Choose one of the $21$ marked rational elliptic profiles with\n$\\operatorname{MW}=\\mathbb ZG$ in \\ref{maps:src:D.2.19}, and write\n$\\langle G,G\\rangle=1/d_0$. Let",
     "Choose one of the $21$ marked rational elliptic profiles of\nDefinition~\\ref{mapsIII:def:elliptic-marked-data}. Write\n$\\langle G,G\\rangle=1/d_0$, so $d_0$ is its height denominator $d$. Let",
     "The same21 profiles,G,P,Q,line and forward period are retained; d in Q110 maps to d0 by the identity integer. This replaces the former catalogue-theorem locator with its actual input definition."),
    ("LN", "whole_fibre_initial_pairs", "maps:src:D.2.46",
     "The marked elliptic monodromies are $B_i$, and the section\n$G$ has integral cocycle $g_i$. Put $p_i=ag_i$, $q_i=bg_i$,",
     "Write $B_i$ for the elliptic matrices $A_i$ of\nDefinition~\\ref{mapsIII:def:elliptic-marked-data}, and retain its\ncocycles $g_i$ in the identical ordered basis $(e_1,e_2)$.\nPut $p_i=ag_i$, $q_i=bg_i$,",
     "This is the literal identity of the two-dimensional period lattice, with inverse renaming B_i to that definition's A_i. It distinguishes those elliptic matrices from the four-dimensional A_i defined here without changing any monodromy."),
]
fields = ["change_id", "type", "statement_id", "old_location", "old_page", "new_location", "new_page", "old_text", "new_text", "reason", "review_status"]
rows = []
for index, (unit, stem, statement, old, new, reason) in enumerate(changes, 1):
    path = directory / (stem + ".tex")
    source = path.read_text()
    assert source.count(old) == 1
    candidate = source.replace(old, new)
    units.check_permanent_identifiers(source, candidate)
    path.write_text(candidate, newline="\n")
    for kind in ("D06", "D20"):
        rows.append(["III-C8-" + unit + "-Q110-LOCATOR-" + str(index) + "-" + kind, kind, statement,
            "weighted/" + stem + ".tex exact citation", "pending page concordance",
            "weighted/" + stem + ".tex exact citation", "pending final build", old, new, reason,
            "bounded source readback complete; root applies separately after Q110 enters canonical"])
    print("CHANGE", unit, index)
    print("OLD", old)
    print("NEW", new)
    review = lane / ("S6_SERIES_PUBLISH_" + unit + "_unit_review.md")
    with review.open("a", newline="") as stream:
        stream.write("\n## Q110 input-table locator readback\n\n" + reason + " The actual created Q110 definition was wholly read at lines3–143 of the foundations fragment. This exact edit is recorded separately in S6_SERIES_PUBLISH_Q110_locator_proposals.tsv; previously merged rows are not resubmitted. Global expansion and canonical application remain root's gate.\n")
with (lane / "S6_SERIES_PUBLISH_Q110_locator_proposals.tsv").open("w", newline="") as stream:
    writer = csv.writer(stream, delimiter="\t", lineterminator="\n")
    writer.writerow(fields)
    writer.writerows(rows)
event_fields = ["statement_id", "date", "who", "type", "outcome", "event_id", "phase", "source_file", "source_row", "source_event_type", "evidence_group", "publish_input_file", "publish_input_row", "date_utc", "where"]
now = datetime.now(timezone.utc).isoformat()
with (lane / "S6_SERIES_PUBLISH_Q110_locator_CHECK_EVENTS.tsv").open("w", newline="") as stream:
    writer = csv.writer(stream, delimiter="\t", lineterminator="\n")
    writer.writerow(event_fields)
    for unit, number in [("LN", 46), ("LQ", 49)]:
        event = "III-C8-" + unit + "-Q110-LOCATOR-READBACK"
        writer.writerow(["maps:src:D.2." + str(number), "2026-11-25",
            "GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; numerical reasoning effort not separately exposed; continuation eight weighted-unit editor",
            "used and rechecked in this run",
            "Bounded readback of the exact Q110 locator transport after wholly reading its143-line source prefix, including the complete definition/table. LN maps d to d0 and its elliptic A_i to B_i by identity; LQ retains the same one-based peripheral positions. No new theorem or independent-check credit; global expansion pending.",
            event, "continuation-eight-publication", "agents/continuation8_iii_weighted_units/S6_SERIES_PUBLISH_Q110_locator_proposals.tsv",
            unit + " exact changes", "used and rechecked in this run", event, "", "", now,
            "Q110 locators only; original theorem labels/targets unchanged"])
print("UTC", now, "EXACT_EDITS", len(changes), "SINGLE_TYPE_ROWS", len(rows), "BOUNDED_EVENTS2; SHARED_WRITES0")
