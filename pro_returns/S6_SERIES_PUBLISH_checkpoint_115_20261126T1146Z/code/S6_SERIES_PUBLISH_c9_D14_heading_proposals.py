#!/usr/bin/env python3
"""Prepare three exact D14 heading changes; never write manuscript or ledgers."""
from pathlib import Path
import csv
from datetime import datetime, timezone
import re

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / "agents/continuation9_findings"
source = (ROOT / "S6_SERIES_PUBLISH_III.tex").read_text()
section_start = source.index(r"\section{Minimal primary smooth types}")
section_end = source.index(r"\section{Three-primary and residual smooth types}", section_start)
section = source[section_start:section_end]
assert not re.search(r"(?m)^\\subsection\*?\{", section)
titles = ("Order two", "Orders five and seven", "Orders ten and fourteen")
candidate = source
edits = []
for index, title in enumerate(titles, 1):
    old = r"\subsubsection{" + title + "}"
    new = r"\subsubsection*{" + title + "}"
    assert source.count(old) == 1 and section.count(old) == 1
    assert new not in source
    candidate = candidate.replace(old, new, 1)
    edits.append((index, title, old, new))

inverse = candidate
for _, _, old, new in reversed(edits):
    assert inverse.count(new) == 1
    inverse = inverse.replace(new, old, 1)
assert inverse == source
for command in ("label", "hypertarget"):
    pattern = r"\\" + command + r"\{[^}]+\}"
    assert re.findall(pattern, source) == re.findall(pattern, candidate)
assert len(re.findall(r"(?m)^\\section\{", source)) == len(re.findall(r"(?m)^\\section\{", candidate))
assert len(re.findall(r"(?m)^\\subsection\{", source)) == len(re.findall(r"(?m)^\\subsection\{", candidate))

now = datetime.now(timezone.utc).isoformat()
fields = ["change_id", "type", "statement_id", "old_location", "old_page", "new_location", "new_page", "old_text", "new_text", "reason", "review_status"]
rows = []
for index, title, old, new in edits:
    rows.append(dict(
        change_id=f"III-C9-D14-MINIMAL-PRIMARY-HEADING-{index}",
        type="D14", statement_id="maps:src:D.2.35",
        old_location=f"Paper III, Minimal primary smooth types; {title}",
        old_page="Current source; next PDF not yet read",
        new_location=f"Paper III, Minimal primary smooth types; {title}",
        new_page="Pending current build and actual page-image reading",
        old_text=old, new_text=new,
        reason=("The c8 promotion made this unit a section without subsections, but retained three numbered level-three headings. "
                "The article class resets subsection to zero at a section and prints thesubsubsection as section.subsection.subsubsection at secnumdepth=3; "
                "the manuscript has no overriding counter or format definition. An unnumbered subsubsection preserves this heading and the single established unit. "
                "The forward transformation inserts one star and its inverse removes that star. Reversing all three changes recovers every original source byte. "
                "All labels, targets, section and subsection commands, statement/proof text, mathematical expressions and section-based theorem/equation counters are unchanged. "
                "The existing tocdepth=2 and bookmarksdepth=2 already exclude level-three headings. The next PDF must show the three readable headings with no zero-middle subsection number."),
        review_status="Prepared after bounded D14 source review; canonical admission and actual PDF verification pending."
    ))
with (DEST / "S6_SERIES_PUBLISH_c9_D14_heading_defects.tsv").open("w", newline="") as handle:
    writer = csv.DictWriter(handle, fields, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)

event_fields = ["statement_id", "date", "who", "type", "outcome", "event_id", "phase", "source_file", "source_row", "source_event_type", "evidence_group", "publish_input_file", "publish_input_row", "date_utc", "where"]
event_id = "ce:c9-iii-d14-source-structure"
event = dict.fromkeys(event_fields, "")
event.update(
    statement_id="III:section-structure", date=now[:10],
    who="GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; numerical effort not separately exposed",
    type="used and rechecked in this run", event_id=event_id,
    phase="publication continuation 9", source_event_type="used and rechecked in this run", evidence_group=event_id,
    source_file="agents/continuation9_findings/S6_SERIES_PUBLISH_c9_D14_structural_review.md",
    source_row="58 existing units; 14 affected sections; 3 orphan subheading corrections",
    publish_input_file="agents/continuation9_findings/S6_SERIES_PUBLISH_c9_D14_heading_defects.tsv",
    publish_input_row="1-3", date_utc=now,
    where="Paper III affected sections3-5,7-9,11-18; c8 regrouping and current source",
    outcome=("Read the current placement of all58 reopened D14 units, their opening contexts, all14 affected section boundaries, "
             "the organization paragraph and the three cross-section forward-reference contexts. Prepared three reversible heading-only corrections "
             "for the section without subsections. Recorded the actual TOC, page-span, heading and proof-continuity evidence needed from the next PDF. "
             "This is a structural source reread after exposure, with no independent mathematical proof credit, new manifest, final page-span claim or PDF-reading claim. "
             "All58 D14 rows remain open pending the current build and actual images.")
)
with (DEST / "S6_SERIES_PUBLISH_c9_D14_CHECK_EVENTS.tsv").open("w", newline="") as handle:
    writer = csv.DictWriter(handle, event_fields, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerow(event)

for index, title, old, new in edits:
    print(f"D14 heading {index}: {title}")
    print(old)
    print(new)
print("Three guarded changes prepared; exact inverse recovers source; literal labels/targets and existing unit boundaries preserved.")
print("Canonical manuscript and all master records untouched; all58 D14 rows remain open for PDF review.")
