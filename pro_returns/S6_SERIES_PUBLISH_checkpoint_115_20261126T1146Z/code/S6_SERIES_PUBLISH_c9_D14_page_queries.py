#!/usr/bin/env python3
"""Locate the 58 reopened D14 units in one completed Paper III build.

Only source, build and PDF navigation data are read. Output is a set of page
queries for later image reading; no ledger, status or visual credit is written.
"""
from pathlib import Path
import argparse
import csv
import hashlib
import re

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / "agents/continuation9_findings"


def group(text, start):
    """Read one balanced TeX group, respecting escaped braces."""
    while start < len(text) and text[start].isspace():
        start += 1
    assert start < len(text) and text[start] == "{", (start, text[start:start + 80])
    depth = 1
    index = start + 1
    while index < len(text):
        char = text[index]
        if char == "\\":
            index += 2
            continue
        if char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                return text[start + 1:index], index + 1
        index += 1
    raise ValueError("Unterminated TeX group")


def groups(text):
    values = []
    index = 0
    while index < len(text) and text[index:].strip():
        value, index = group(text, index)
        values.append(value)
    return values


def write_tsv(path, fields, rows):
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run", required=True, help="Completed current-kernel run, such as candidate02")
    args = parser.parse_args()
    assert re.fullmatch(r"[a-z0-9_]+", args.run)
    build_out = ROOT / "code" / f"S6_SERIES_PUBLISH_c9_build_III_current_{args.run}.out"
    completion = build_out.read_text(errors="replace")
    assert "UTC complete " in completion, "Wait for the requested build's completion marker."
    work = ROOT / "agents/continuation9_build_III/current"
    pdf_path = work / "S6_SERIES_PUBLISH_III.pdf"
    aux_path = work / "S6_SERIES_PUBLISH_III.aux"
    toc_path = work / "S6_SERIES_PUBLISH_III.toc"
    source_path = ROOT / "S6_SERIES_PUBLISH_III.tex"
    source = source_path.read_text()
    aux = aux_path.read_text()
    toc = toc_path.read_text()
    pdf_identity = re.search(r"(?m)^PDF .* SHA-256 ([0-9a-f]{64})$", completion)
    source_identity = re.search(r"(?m)^Source SHA-256 ([0-9a-f]{64}) kernel current$", completion)
    assert pdf_identity and hashlib.sha256(pdf_path.read_bytes()).hexdigest() == pdf_identity.group(1), "The live PDF is no longer this completed run."
    assert source_identity and hashlib.sha256(source_path.read_bytes()).hexdigest() == source_identity.group(1), "The live source is no longer this completed run."
    # The log's own page count and completion marker identify a completed build.
    # Root controls the frozen source and final admission; this tool creates no seal.
    page_count_match = re.search(r"(?m)^Pages:\s+(\d+)\s*$", completion)
    assert page_count_match, "The completed build must retain pdfinfo's page count."

    headings = []
    section = subsection = 0
    for match in re.finditer(r"(?m)^\\(section|subsection)\{", source):
        level = match.group(1)
        title, _ = group(source, match.end() - 1)
        if level == "section":
            section += 1
            subsection = 0
            number = str(section)
        else:
            subsection += 1
            number = f"{section}.{subsection}"
        headings.append(dict(start=match.start(), source_line=source.count("\n", 0, match.start()) + 1,
                             level=level, section=section, number=number,
                             source_title=title, anchor=f"{level}.{number}"))

    contents = {}
    for line in toc.splitlines():
        if not line.startswith(r"\contentsline"):
            continue
        index = len(r"\contentsline")
        entry = []
        for _ in range(4):
            value, index = group(line, index)
            entry.append(value)
        level, title, page, anchor = entry
        if level not in ("section", "subsection"):
            continue
        assert anchor not in contents
        assert title.startswith(r"\numberline")
        number, title_index = group(title, len(r"\numberline"))
        contents[anchor] = dict(level=level, number=number, title=title[title_index:], printed_page=page)
    for heading in headings:
        item = contents[heading["anchor"]]
        assert item["level"] == heading["level"] and item["number"] == heading["number"]

    labels = {}
    for line in aux.splitlines():
        if not line.startswith(r"\newlabel"):
            continue
        key, index = group(line, len(r"\newlabel"))
        payload, _ = group(line, index)
        parts = groups(payload)
        if key.endswith("@cref"):
            continue
        assert key not in labels
        labels[key] = parts

    import fitz
    from pypdf import PdfReader
    reader = PdfReader(str(pdf_path))
    assert len(reader.pages) == int(page_count_match.group(1))
    destinations = reader.named_destinations
    printed_labels = reader.page_labels

    def physical(anchor):
        assert anchor in destinations, f"Missing PDF destination: {anchor}"
        return reader.get_destination_page_number(destinations[anchor]) + 1

    def heading_page(heading):
        page = physical(heading["anchor"])
        assert str(printed_labels[page - 1]) == contents[heading["anchor"]]["printed_page"], (
            heading["anchor"], page, printed_labels[page - 1], contents[heading["anchor"]])
        return page

    with (ROOT / "S6_SERIES_PUBLISH_unit_progress.tsv").open(newline="") as handle:
        progress = list(csv.DictReader(handle, delimiter="\t"))
    rows = [row for row in progress if row["paper"] == "III" and row["defect_type"] == "D14" and row["status"] == "open"]
    assert len(rows) == 58, "The scoped query expects the 58 still-open restructuring rows."
    located = []
    for row in rows:
        needle = "\\label{" + row["unit_id"] + "}"
        assert source.count(needle) == 1
        position = source.index(needle)
        owner_index = max(i for i, heading in enumerate(headings) if heading["start"] <= position)
        owner = headings[owner_index]
        following = headings[owner_index + 1]
        first = heading_page(owner)
        next_first = heading_page(following)
        label = labels[row["unit_id"]]
        assert len(label) >= 4
        label_physical = physical(label[3])
        assert first <= label_physical <= next_first
        label_page_matches = [i + 1 for i, value in enumerate(printed_labels) if str(value) == label[1]]
        assert len(label_page_matches) == 1
        printed_label_physical = label_page_matches[0]
        located.append(dict(
            build_run=args.run, unit_id=row["unit_id"], source_heading_line=owner["source_line"],
            source_heading_number=owner["number"], source_heading_tex=owner["source_title"],
            toc_heading_tex=contents[owner["anchor"]]["title"], toc_anchor=owner["anchor"],
            heading_printed_page=contents[owner["anchor"]]["printed_page"], heading_physical_page=first,
            aux_label_number=label[0], aux_label_printed_page=label[1], aux_label_anchor=label[3],
            aux_label_physical_page=printed_label_physical, aux_anchor_physical_page=label_physical,
            aux_anchor_printed_page=str(printed_labels[label_physical - 1]),
            aux_anchor_page_difference=label_physical - printed_label_physical,
            next_heading_anchor=following["anchor"],
            next_heading_title=following["source_title"], next_heading_printed_page=contents[following["anchor"]]["printed_page"],
            next_heading_physical_page=next_first, inclusive_review_window=f"{first}-{next_first}",
            status="navigation query only; actual image reading pending"
        ))
    located.sort(key=lambda row: int(row["source_heading_line"]))
    assert len({row["toc_anchor"] for row in located}) == 58
    fields = list(located[0])
    unit_path = DEST / f"S6_SERIES_PUBLISH_c9_D14_{args.run}_unit_page_queries.tsv"
    write_tsv(unit_path, fields, located)

    section_rows = []
    selected_sections = sorted({int(row["source_heading_number"].split(".")[0]) for row in located})
    section_headings = [heading for heading in headings if heading["level"] == "section"]
    assert len(selected_sections) == 14
    for number in selected_sections:
        heading = section_headings[number - 1]
        following = section_headings[number]
        first, next_first = heading_page(heading), heading_page(following)
        section_rows.append(dict(
            build_run=args.run, section_number=number, source_heading_tex=heading["source_title"],
            heading_printed_page=contents[heading["anchor"]]["printed_page"], heading_physical_page=first,
            next_section_printed_page=contents[following["anchor"]]["printed_page"],
            next_section_physical_page=next_first, inclusive_boundary_window=f"{first}-{next_first}",
            special_attention="actual long-section proportion" if number in (11, 13, 17) else ("three unnumbered internal headings" if number == 16 else ""),
            status="boundary query only; actual final content page and proportion pending images"
        ))
    section_path = DEST / f"S6_SERIES_PUBLISH_c9_D14_{args.run}_section_page_queries.tsv"
    write_tsv(section_path, list(section_rows[0]), section_rows)

    doc = fitz.open(pdf_path)
    first = heading_page(section_headings[15])
    next_first = heading_page(section_headings[16])
    star_rows = []
    for title in ("Order two", "Orders five and seven", "Orders ten and fourteen"):
        assert source.count(r"\subsubsection*{" + title + "}") == 1
        hits = []
        for page_number in range(first, next_first + 1):
            for rect in doc[page_number - 1].search_for(title):
                hits.append(dict(build_run=args.run, source_heading_tex=title, physical_page=page_number,
                                 printed_page=printed_labels[page_number - 1],
                                 pdf_search_rectangle=" ".join(f"{value:.3f}" for value in rect),
                                 status="PDF text locator only; heading appearance pending image reading"))
        assert hits, f"No PDF text locator for {title}"
        star_rows.extend(hits)
    star_path = DEST / f"S6_SERIES_PUBLISH_c9_D14_{args.run}_internal_heading_queries.tsv"
    write_tsv(star_path, list(star_rows[0]), star_rows)
    print("Completed build:", args.run, "PDF pages:", len(reader.pages))
    print("58 existing unit queries:", unit_path.relative_to(ROOT))
    print("14 section boundary queries:", section_path.relative_to(ROOT))
    print("Internal-heading text locators:", star_path.relative_to(ROOT))
    for row in section_rows:
        print("SECTION", row["section_number"], row["inclusive_boundary_window"], row["source_heading_tex"], row["special_attention"])
    for row in star_rows:
        print("INTERNAL HEADING", row["source_heading_tex"], "physical", row["physical_page"], "printed", row["printed_page"])
    for row in located:
        if row["aux_anchor_page_difference"]:
            print("LABEL/ANCHOR PAGE QUERY", row["unit_id"], "label page", row["aux_label_physical_page"], "anchor page", row["aux_anchor_physical_page"])
    print("Inclusive windows retain a potentially shared next-heading page; they do not assert the preceding unit's final content page.")
    print("No source/ledger mutation, disposition, independent-check credit, page-reading credit or final manifest is produced.")


if __name__ == "__main__":
    main()
