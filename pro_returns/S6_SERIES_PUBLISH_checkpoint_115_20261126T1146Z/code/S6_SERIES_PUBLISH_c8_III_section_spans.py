#!/usr/bin/env python3
"""Regroup three observed long sections at complete existing unit boundaries."""
import argparse
from collections import Counter
import csv
from datetime import datetime, timezone
import io
from pathlib import Path
import re
from S6_SERIES_PUBLISH_c8_III_derive_final import RawTable

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "S6_SERIES_PUBLISH_III.tex"
FRAGMENTS = ROOT / "agents/continuation8_iii_integration/units"
csv.field_size_limit(16 * 1024 * 1024)

LONG_SECTIONS = [
    ("Sphere maps, framings and homotopy classes", "Sphere maps, coverings and framings", 19, "19–90"),
    ("Logarithmic families from rational elliptic surfaces", "Logarithmic elliptic profiles", 15, "116–215"),
    ("Sphere fillings of elliptic profiles", "Sphere fillings and primitive finite caps", 24, "250–548"),
]
BREAKS = [
    ("Angle-forgetting and cusp-core quotient maps", "Cusp quotient maps and cell attachments", "37"),
    ("The local Kummer cover and its global obstruction", "Local Kummer maps and cyclic cover invariants", "67"),
    ("Seven elliptic profiles with unbounded logarithmic multiplicity", "Unbounded multiplicities and logarithmic modifications", "147"),
    ("Marked elliptic profiles and whole-fibre linearizations", "Section-line families and elliptic catalogues", "176"),
    ("All finite additive lattices and affine twists", "Finite cap lattices and natural catalogues", "298"),
    ("All positive weights of the Engel construction", "Weighted profiles and saturated cap maps", "329"),
    ("Integral bar coordinates at every positive weight", "Integral bar coordinates and initial pairs", "379"),
    ("Invariant-Chern additive caps", "Invariant-Chern caps and height-integral pairs", "417"),
    ("Three-primary smooth types", "Three-primary and residual smooth types", "472"),
    ("Weighted Engel smooth types", "Weighted Engel and OS45 manifolds", "521"),
]


def require(value, reason):
    if not value:
        raise RuntimeError(reason)


def append_rows(raw, fields, rows):
    require(raw.endswith(b"\n") and b"\r" not in raw, "Existing table line endings")
    stream = io.StringIO(newline="")
    csv.DictWriter(stream, fields, delimiter="\t", lineterminator="\n").writerows(rows)
    return raw + stream.getvalue().encode()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    source = SOURCE.read_text()
    fragments = {p: p.read_text() for p in FRAGMENTS.rglob("*.tex")}
    progress_path = ROOT / "S6_SERIES_PUBLISH_unit_progress.tsv"
    progress_raw = progress_path.read_bytes()
    progress_table = RawTable(progress_raw, "\t", str(progress_path))
    progress = progress_table.iii
    affected = set()
    edits = []
    for old_title, new_title, count, pages in LONG_SECTIONS:
        old = "\\section{" + old_title + "}"
        new = "\\section{" + new_title + "}"
        require(source.count(old) == 1, "Old section identity")
        start = source.index(old)
        end = source.index("\\section{", start + len(old))
        block = source[start:end]
        labels = set(re.findall(r"\\label\{([^{}]+)\}", block))
        units = [r for r in progress if r["defect_type"] == "D14" and r["unit_id"] in labels]
        require(len(units) == count, "Actual units in the long section")
        require(len(re.findall(r"(?m)^\\subsection\{", block)) == count, "Subsection count")
        affected.update(r["unit_id"] for r in units)
        edits.append(("retitle-" + str(len(edits) + 1), old, new, pages))
    for i, (subsection, section, page) in enumerate(BREAKS, 1):
        old = "\\subsection{" + subsection + "}"
        new = "\\section{" + section + "}\n" + old
        edits.append((f"boundary-{i:02d}", old, new, page))
    old = r"\subsection{Minimal primary smooth types}"
    new = r"\section{Minimal primary smooth types}"
    edits.append(("promote-minimal-primary", old, new, "434–471"))
    candidate = source
    changed = dict(fragments)
    locations = {}
    for name, old, new, pages in edits:
        require(source.count(old) == 1, f"Unique old heading: {name}")
        paths = [p for p, value in fragments.items() if old in value]
        require(len(paths) == 1 and fragments[paths[0]].count(old) == 1, f"Fragment heading: {name}")
        locations[name] = str(paths[0].relative_to(ROOT))
        candidate = candidate.replace(old, new, 1)
        changed[paths[0]] = changed[paths[0]].replace(old, new, 1)
        print("HEADING", name, "PASS08_PAGES", pages, "FRAGMENT", locations[name])
        print("EXACT_OLD\n" + old + "\nEXACT_NEW\n" + new)
    inverse = candidate
    for name, old, new, pages in reversed(edits):
        require(inverse.count(new) == 1, f"Unique inverse heading: {name}")
        inverse = inverse.replace(new, old, 1)
    require(inverse == source, "The exact reverse replacements did not recover every original byte")
    for command in ("label", "hypertarget"):
        pattern = r"\\" + command + r"\{([^{}]+)\}"
        require(Counter(re.findall(pattern, candidate)) == Counter(re.findall(pattern, source)),
                f"Literal {command} multiplicities changed")
    require(len(affected) == 58 and len(edits) == 14, "Expected exact review domain")
    require(len(re.findall(r"(?m)^\\section\{", source)) == 17
            and len(re.findall(r"(?m)^\\section\{", candidate)) == 28, "Section map")
    print("EXACT_INVERSE_RECOVERS_SOURCE; 58_EXISTING_UNITS; 14_HEADING_EDITS; 17_TO_28_SECTIONS")
    if not args.apply:
        print("INSPECT_ONLY; NO_WRITES")
        return
    now = datetime.now(timezone.utc).isoformat()
    defect_path = ROOT / "S6_SERIES_PUBLISH_defects_III.tsv"
    event_path = ROOT / "CHECK_EVENTS.tsv"
    defect_raw, event_raw = defect_path.read_bytes(), event_path.read_bytes()
    dr = csv.DictReader(io.StringIO(defect_raw.decode()), delimiter="\t")
    defects, defect_fields = list(dr), dr.fieldnames
    er = csv.DictReader(io.StringIO(event_raw.decode()), delimiter="\t")
    events, event_fields = list(er), er.fieldnames
    new_defects = []
    for name, old, new, pages in edits:
        ident = "III-C8-D14-SECTION-SPANS-" + name
        require(ident not in {r["change_id"] for r in defects}, "Repeated D14 repair")
        new_defects.append(dict(change_id=ident, type="D14", statement_id="III:section-structure",
            old_location=locations[name], old_page="pass08 physical/printed " + pages,
            new_location=locations[name], new_page="pending structural rebuild and actual TOC/page reading",
            old_text=old, new_text=new,
            reason="Root read all four actual TOC pages. Former sections3,5,7 span72,100,299pages. The cuts are complete existing unit boundaries reviewed by lg_fresh/lv_compare. Each recorded replacement has the exact inverse new-to-old; reversing all14 recovers the entire prior source byte for byte. Every unit remains in the same order, with its statement/proof/formulas and literal labels/hypertarget multiplicities unchanged. The sole promoted subsection remains the same actual unit under the section-without-subsections rule.",
            review_status="Exact heading transformation and source inverse checked by root at " + now + "; source D14 and final rendered spans remain open."))
    for row in progress:
        if row["defect_type"] == "D14" and row["unit_id"] in affected:
            row.update(status="open", date_utc=now,
                       evidence="code/S6_SERIES_PUBLISH_c8_III_section_spans.py; pass08 TOC physical2–5",
                       detail="The actual long section was divided at complete existing unit boundaries. Unit content/order are preserved by the exact inverse source transformation. New section spans and final page images require the structural rebuild and actual reading.")
    event_id = "publish:c8:III:section-span-restructuring"
    require(event_id not in {r["event_id"] for r in events}, "Repeated structure event")
    event = dict.fromkeys(event_fields, "")
    event.update(statement_id="III:section-structure", date=now[:10],
                 who="GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; numerical effort not separately exposed; root with lg_fresh and lv_compare boundary reviewers",
                 type="used and rechecked in this run", event_id=event_id,
                 phase="continuation8 rendered structure repair", source_file="code/S6_SERIES_PUBLISH_c8_III_section_spans.py",
                 source_event_type="used and rechecked in this run", evidence_group=event_id, date_utc=now,
                 where="pass08 TOC physical2–5; exact old/new headings and inverse in this source",
                 outcome="Root read the actual TOC and confirmed72/100/299-page section spans. Reviewers checked contiguous complete-unit boundaries. Fourteen heading-only replacements regroup58 existing units into shorter sections while preserving every mathematical byte and unit order, certified by the exact inverse replacement equality and unchanged literal identifier multiplicities. No new proof, independent derivation, event count, required disposition or final page-reading credit is added. D14 rows and the build gate reopen for the new layout.")
    build_path = ROOT / "S6_SERIES_PUBLISH_build_progress.tsv"
    build_raw = build_path.read_bytes()
    build_table = RawTable(build_raw, "\t", str(build_path))
    build = build_table.iii
    require(len(build) == 1, "One III build row")
    build[0].update(status="open", date_utc=now,
                    detail="Pass08 build completed for its recorded PDF. The D14 heading regrouping changes current source/numbering; a new converged build and changed-page readings remain.")
    outputs = {SOURCE: candidate.encode(), progress_path: progress_table.replace_iii(progress),
               defect_path: append_rows(defect_raw, defect_fields, new_defects),
               event_path: append_rows(event_raw, event_fields, [event]),
               build_path: build_table.replace_iii(build)}
    outputs.update({p: value.encode() for p, value in changed.items() if value != fragments[p]})
    require(SOURCE.read_text() == source and progress_path.read_bytes() == progress_raw
            and defect_path.read_bytes() == defect_raw and event_path.read_bytes() == event_raw
            and build_path.read_bytes() == build_raw, "An input changed during preparation")
    for p, value in outputs.items():
        p.write_bytes(value)
        require(p.read_bytes() == value, "Write mismatch")
    print("APPLIED_UTC", now, "D14_ROWS_REOPENED", len(affected), "BUILD_REOPENED", 1)


if __name__ == "__main__":
    main()
