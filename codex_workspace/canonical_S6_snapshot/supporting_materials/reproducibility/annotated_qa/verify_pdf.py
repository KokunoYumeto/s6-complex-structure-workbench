#!/usr/bin/env python3
"""Verify the annotated PDF without changing either source PDF."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import pdfplumber
from pypdf import PdfReader


SOURCE_PAGES = 108
FRONT_MATTER_PAGES = 8
APPENDIX_PAGES = 12
EXPECTED_TOTAL_PAGES = FRONT_MATTER_PAGES + SOURCE_PAGES + APPENDIX_PAGES
LETTER = (612.0, 792.0)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def normalized_words(page, *, remove_badge: bool):
    words = page.extract_words(
        x_tolerance=1,
        y_tolerance=1,
        keep_blank_chars=False,
        use_text_flow=False,
    )
    result = []
    for word in words:
        is_badge = word["x0"] >= 575.0 and word["top"] <= 30.0
        if remove_badge and is_badge:
            continue
        result.append(
            (
                word["text"],
                round(float(word["x0"]), 3),
                round(float(word["top"]), 3),
                round(float(word["x1"]), 3),
                round(float(word["bottom"]), 3),
            )
        )
    return result


def badge_link_targets(page):
    targets = []
    for reference in page.get("/Annots", []):
        annotation = reference.get_object()
        if annotation.get("/Subtype") != "/Link":
            continue
        rectangle = annotation.get("/Rect")
        if not rectangle or len(rectangle) != 4:
            continue
        x0, y0, x1, y1 = map(float, rectangle)
        if x0 >= 570.0 and y0 >= 755.0 and x1 <= 612.5 and y1 <= 792.5:
            action = annotation.get("/A") or {}
            targets.append(str(action.get("/D", "")))
    return targets


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("canonical", type=Path)
    parser.add_argument("annotated", type=Path)
    parser.add_argument("--standalone", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    failures = []
    details = {}

    canonical_reader = PdfReader(str(args.canonical))
    annotated_reader = PdfReader(str(args.annotated))
    details["canonical_pages"] = len(canonical_reader.pages)
    details["annotated_pages"] = len(annotated_reader.pages)
    if len(canonical_reader.pages) != SOURCE_PAGES:
        failures.append(
            f"canonical page count is {len(canonical_reader.pages)}, expected {SOURCE_PAGES}"
        )
    if len(annotated_reader.pages) != EXPECTED_TOTAL_PAGES:
        failures.append(
            f"annotated page count is {len(annotated_reader.pages)}, "
            f"expected {EXPECTED_TOTAL_PAGES}"
        )

    bad_page_sizes = []
    guide_badge_targets = []
    badge_link_targets_by_page = []
    for index, page in enumerate(annotated_reader.pages, start=1):
        width = round(float(page.mediabox.width), 3)
        height = round(float(page.mediabox.height), 3)
        if (width, height) != LETTER:
            bad_page_sizes.append({"page": index, "size": [width, height]})
        if index <= FRONT_MATTER_PAGES:
            guide_badge_targets.extend(badge_link_targets(page))
        if FRONT_MATTER_PAGES < index <= FRONT_MATTER_PAGES + SOURCE_PAGES:
            badge_link_targets_by_page.append(badge_link_targets(page))
    if bad_page_sizes:
        failures.append(f"non-letter page sizes: {bad_page_sizes[:5]}")
    if guide_badge_targets:
        failures.append(f"reader guide unexpectedly carries an audit badge: {guide_badge_targets}")
    wrong_badges = [
        index + 1
        for index, targets in enumerate(badge_link_targets_by_page)
        if targets != [f"audit-page-{index + 1}"]
    ]
    if wrong_badges:
        failures.append(f"source pages without the expected audit badge target: {wrong_badges}")

    named_destinations = annotated_reader.named_destinations
    missing_audit_destinations = [
        page for page in range(1, SOURCE_PAGES + 1) if f"audit-page-{page}" not in named_destinations
    ]
    missing_source_destinations = [
        page
        for page in range(1, SOURCE_PAGES + 1)
        if f"s6-source-page-{page:03d}" not in named_destinations
    ]
    if missing_audit_destinations:
        failures.append(f"missing audit destinations: {missing_audit_destinations}")
    if missing_source_destinations:
        failures.append(f"missing source-page destinations: {missing_source_destinations}")

    text_mismatches = []
    badge_word_counts = []
    with pdfplumber.open(args.canonical) as canonical_pdf, pdfplumber.open(args.annotated) as annotated_pdf:
        for index in range(SOURCE_PAGES):
            canonical_words = normalized_words(canonical_pdf.pages[index], remove_badge=False)
            annotated_index = FRONT_MATTER_PAGES + index
            annotated_words = normalized_words(
                annotated_pdf.pages[annotated_index], remove_badge=True
            )
            all_annotated_words = normalized_words(
                annotated_pdf.pages[annotated_index], remove_badge=False
            )
            badge_word_counts.append(len(all_annotated_words) - len(annotated_words))
            if canonical_words != annotated_words:
                first_difference = None
                for position, pair in enumerate(zip(canonical_words, annotated_words)):
                    if pair[0] != pair[1]:
                        first_difference = {
                            "position": position,
                            "canonical": pair[0],
                            "annotated": pair[1],
                        }
                        break
                text_mismatches.append(
                    {
                        "page": index + 1,
                        "canonical_word_count": len(canonical_words),
                        "annotated_word_count": len(annotated_words),
                        "first_difference": first_difference,
                    }
                )
    if text_mismatches:
        failures.append(f"source-page text/coordinate mismatches: {text_mismatches[:3]}")
    missing_badge_text = [index + 1 for index, count in enumerate(badge_word_counts) if count < 1]
    if missing_badge_text:
        failures.append(f"source pages without visible badge text: {missing_badge_text}")

    metadata = annotated_reader.metadata or {}
    title = str(metadata.get("/Title", ""))
    if "Annotated peer-review edition" not in title:
        failures.append(f"unexpected PDF title metadata: {title!r}")

    hashes = {
        "canonical": sha256(args.canonical),
        "annotated": sha256(args.annotated),
    }
    if args.standalone:
        hashes["standalone"] = sha256(args.standalone)
        if hashes["standalone"] != hashes["annotated"]:
            failures.append("multi-file and standalone builds are not byte-identical")

    details.update(
        {
            "page_sizes_all_letter": not bad_page_sizes,
            "front_matter_pages": FRONT_MATTER_PAGES,
            "source_physical_page_span": [
                FRONT_MATTER_PAGES + 1,
                FRONT_MATTER_PAGES + SOURCE_PAGES,
            ],
            "reader_guide_has_no_audit_badge": not guide_badge_targets,
            "badge_links_target_the_matching_appendix_entry": not wrong_badges,
            "all_audit_destinations_present": not missing_audit_destinations,
            "all_source_page_destinations_present": not missing_source_destinations,
            "badge_word_count_min": min(badge_word_counts) if badge_word_counts else 0,
            "source_text_and_coordinates_identical_after_badge_filter": not text_mismatches,
            "metadata_title": title,
            "hashes": hashes,
        }
    )
    result = {"passed": not failures, "failures": failures, "details": details}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
