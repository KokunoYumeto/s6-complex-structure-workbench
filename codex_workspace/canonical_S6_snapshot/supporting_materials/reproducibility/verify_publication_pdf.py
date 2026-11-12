#!/usr/bin/env python3
"""Fail-closed structural audit for the publication PDFs.

The verifier checks page geometry, rotations, content streams, text extraction,
link destinations, and font embedding.  It writes a deterministic JSON report
when ``--report`` is supplied and exits nonzero if any structural defect is
found.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

from pypdf import PdfReader
from pypdf.generic import ArrayObject, DictionaryObject, IndirectObject


PAGE_STANDARDS = {
    "US Letter": (612.0, 792.0),
    "A4": (595.276, 841.89),
}
GEOMETRY_TOLERANCE = 0.1


def page_standard(width: float, height: float) -> str | None:
    """Return the exact supported page standard within the stated tolerance."""
    for name, (standard_width, standard_height) in PAGE_STANDARDS.items():
        if (
            abs(width - standard_width) <= GEOMETRY_TOLERANCE
            and abs(height - standard_height) <= GEOMETRY_TOLERANCE
        ):
            return name
    return None


def dereference(value: Any) -> Any:
    return value.get_object() if isinstance(value, IndirectObject) else value


def object_key(value: Any) -> str:
    if isinstance(value, IndirectObject):
        return f"{value.idnum}:{value.generation}"
    return f"direct:{id(value)}"


def font_descriptor(font: DictionaryObject) -> DictionaryObject | None:
    subtype = str(font.get("/Subtype", ""))
    if subtype == "/Type3":
        return None
    if subtype == "/Type0":
        descendants = dereference(font.get("/DescendantFonts", []))
        if descendants:
            descendant = dereference(descendants[0])
            descriptor = dereference(descendant.get("/FontDescriptor"))
            return descriptor if isinstance(descriptor, DictionaryObject) else None
        return None
    descriptor = dereference(font.get("/FontDescriptor"))
    return descriptor if isinstance(descriptor, DictionaryObject) else None


def embedded_font(font: DictionaryObject) -> bool:
    subtype = str(font.get("/Subtype", ""))
    if subtype == "/Type3":
        return bool(font.get("/CharProcs"))
    descriptor = font_descriptor(font)
    if descriptor is None:
        return False
    return any(descriptor.get(name) is not None for name in ("/FontFile", "/FontFile2", "/FontFile3"))


def audit_pdf(path: Path, display_path: str | None = None) -> dict[str, Any]:
    data = path.read_bytes()
    reader = PdfReader(path, strict=True)
    named_destinations = reader.named_destinations
    named_destination_names = set(named_destinations)

    geometry_errors: list[dict[str, Any]] = []
    rotation_errors: list[dict[str, Any]] = []
    content_errors: list[dict[str, Any]] = []
    text_errors: list[dict[str, Any]] = []
    bad_destinations: list[dict[str, Any]] = []
    link_annotations = 0
    external_links = 0
    unique_fonts: dict[str, dict[str, Any]] = {}
    geometry_standard_counts = {name: 0 for name in PAGE_STANDARDS}

    for page_number, page in enumerate(reader.pages, start=1):
        width = float(page.mediabox.width)
        height = float(page.mediabox.height)
        standard = page_standard(width, height)
        if standard is None:
            geometry_errors.append({"page": page_number, "width": width, "height": height})
        else:
            geometry_standard_counts[standard] += 1

        rotation = int(page.get("/Rotate", 0) or 0) % 360
        if rotation:
            rotation_errors.append({"page": page_number, "rotation": rotation})

        try:
            contents = page.get_contents()
            if contents is None:
                content_errors.append({"page": page_number, "error": "missing content stream"})
            else:
                contents.get_data()
        except Exception as exc:  # pragma: no cover - diagnostic boundary
            content_errors.append({"page": page_number, "error": f"{type(exc).__name__}: {exc}"})

        try:
            page.extract_text()
        except Exception as exc:  # pragma: no cover - diagnostic boundary
            text_errors.append({"page": page_number, "error": f"{type(exc).__name__}: {exc}"})

        resources = dereference(page.get("/Resources", {}))
        fonts = dereference(resources.get("/Font", {})) if isinstance(resources, DictionaryObject) else {}
        if isinstance(fonts, DictionaryObject):
            for resource_name, font_reference in fonts.items():
                key = object_key(font_reference)
                if key in unique_fonts:
                    continue
                font = dereference(font_reference)
                if not isinstance(font, DictionaryObject):
                    continue
                unique_fonts[key] = {
                    "resource_name": str(resource_name),
                    "base_font": str(font.get("/BaseFont", "")),
                    "subtype": str(font.get("/Subtype", "")),
                    "embedded": embedded_font(font),
                }

        annotations = dereference(page.get("/Annots", []))
        for annotation_reference in annotations or []:
            annotation = dereference(annotation_reference)
            if not isinstance(annotation, DictionaryObject) or str(annotation.get("/Subtype", "")) != "/Link":
                continue
            link_annotations += 1
            destination = annotation.get("/Dest")
            action = dereference(annotation.get("/A"))
            if destination is None and isinstance(action, DictionaryObject):
                action_type = str(action.get("/S", ""))
                if action_type == "/URI":
                    external_links += 1
                    continue
                if action_type == "/GoTo":
                    destination = action.get("/D")
            destination = dereference(destination)
            if isinstance(destination, str) and destination not in named_destination_names:
                bad_destinations.append({"page": page_number, "destination": destination})
            elif destination is not None and not isinstance(destination, (str, ArrayObject)):
                bad_destinations.append({"page": page_number, "destination_type": type(destination).__name__})

    unembedded_fonts = sorted(
        (font for font in unique_fonts.values() if not font["embedded"]),
        key=lambda font: (font["base_font"], font["resource_name"]),
    )
    errors = {
        "geometry": geometry_errors,
        "rotation": rotation_errors,
        "content": content_errors,
        "text_extraction": text_errors,
        "link_destinations": bad_destinations,
        "unembedded_fonts": unembedded_fonts,
    }
    return {
        "path": display_path or path.name,
        "bytes": len(data),
        "sha256": hashlib.sha256(data).hexdigest(),
        "pages": len(reader.pages),
        "encrypted": reader.is_encrypted,
        "metadata": {
            "title": str(reader.metadata.title or "") if reader.metadata else "",
            "author": str(reader.metadata.author or "") if reader.metadata else "",
        },
        "named_destinations": len(named_destinations),
        "link_annotations": link_annotations,
        "external_links": external_links,
        "unique_fonts": len(unique_fonts),
        "page_geometry_standards": {
            name: count for name, count in geometry_standard_counts.items() if count
        },
        "errors": errors,
        "passed": not reader.is_encrypted and not any(errors.values()),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("pdf", type=Path)
    parser.add_argument("--report", type=Path)
    parser.add_argument(
        "--display-path",
        help="Public path label stored in the report (defaults to the PDF filename)",
    )
    args = parser.parse_args()
    result = audit_pdf(args.pdf, args.display_path)
    serialized = json.dumps(result, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(serialized, encoding="utf-8", newline="\n")
    print(serialized, end="")
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
