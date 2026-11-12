#!/usr/bin/env python3
"""Extract the load-bearing manuscript pages and matching TeX source blocks."""
from __future__ import annotations

import csv
import re
import subprocess
from pathlib import Path

from pypdf import PdfReader, PdfWriter

ROOT = Path(__file__).resolve().parents[1]
SOURCE_TEX = ROOT / "source" / "s6_canonical_full_108_pages.tex"
SOURCE_PDF = ROOT / "source" / "s6_canonical_108_pages.pdf"
OUT = ROOT / "evidence" / "critical_pages"
EXTRACTS = ROOT / "evidence" / "source_extracts"
RANGES = [(40, 62, "section_7_topology"), (95, 108, "appendices_A_B")]


def extract_tex_pages(start: int, end: int) -> str:
    text = SOURCE_TEX.read_text(encoding="utf-8", errors="replace")
    chunks = []
    for page in range(start, end + 1):
        pattern = re.compile(
            rf"% ===== SOURCE PDF PAGE {page:03d} START =====.*?% ===== SOURCE PDF PAGE {page:03d} END =====",
            re.S,
        )
        match = pattern.search(text)
        if not match:
            raise RuntimeError(f"Could not find source block for page {page}")
        chunks.append(match.group(0))
    return "\n\n".join(chunks) + "\n"


def write_pdf(page_numbers: list[int], output: Path, bookmark_groups: list[tuple[str, int]] | None = None) -> None:
    reader = PdfReader(str(SOURCE_PDF))
    writer = PdfWriter()
    for page_num in page_numbers:
        writer.add_page(reader.pages[page_num - 1])
    if bookmark_groups:
        for title, output_index in bookmark_groups:
            writer.add_outline_item(title, output_index)
    with output.open("wb") as f:
        writer.write(f)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    EXTRACTS.mkdir(parents=True, exist_ok=True)

    combined_pages: list[int] = []
    bookmarks: list[tuple[str, int]] = []
    index_rows = []

    for start, end, slug in RANGES:
        pages = list(range(start, end + 1))
        tex_path = EXTRACTS / f"source_pages_{start:03d}_{end:03d}.tex"
        tex_path.write_text(extract_tex_pages(start, end), encoding="utf-8")
        pdf_path = OUT / f"manuscript_pages_{start:03d}_{end:03d}.pdf"
        write_pdf(pages, pdf_path)
        text_path = EXTRACTS / f"pdf_text_pages_{start:03d}_{end:03d}.txt"
        subprocess.run(["pdftotext", "-f", str(start), "-l", str(end), "-layout", str(SOURCE_PDF), str(text_path)], check=True)
        bookmarks.append((f"Pages {start}-{end}: {slug.replace('_', ' ')}", len(combined_pages)))
        for p in pages:
            index_rows.append({
                "physical_page": p,
                "critical_region": slug,
                "combined_pdf_page": len(combined_pages) + 1,
                "source_extract": tex_path.name,
                "pdf_text_extract": text_path.name,
            })
            combined_pages.append(p)

    combined = OUT / "S6_CRITICAL_EVIDENCE_PAGES.pdf"
    write_pdf(combined_pages, combined, bookmarks)

    index_path = OUT / "CRITICAL_PAGE_INDEX.csv"
    with index_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(index_rows[0].keys()))
        writer.writeheader()
        writer.writerows(index_rows)

    print(f"Wrote {combined} with {len(combined_pages)} pages")


if __name__ == "__main__":
    main()
