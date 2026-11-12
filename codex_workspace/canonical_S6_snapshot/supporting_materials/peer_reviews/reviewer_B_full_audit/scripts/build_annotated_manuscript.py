#!/usr/bin/env python3
"""Add a non-destructive page-status margin label and popup note to the manuscript."""
from __future__ import annotations

import csv
from pathlib import Path

import fitz

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source" / "s6_canonical_108_pages.pdf"
OUTDIR = ROOT / "evidence" / "annotations"
OUTPUT = OUTDIR / "S6_AUDIT_ANNOTATED_MANUSCRIPT.pdf"
INDEX = OUTDIR / "ANNOTATION_INDEX.csv"

RANGES = [
    (1, 7, "CRITICAL-DEPENDENCY", "The overview and main claim depend on the unresolved integral topology package in Section 7 and Appendix B.", "R1-R4"),
    (8, 13, "VERIFIED-EXACT", "Monodromy, lattice, Smith-normal-form, invariant-lattice, exterior-power, and alternating-form calculations were reproduced exactly.", "core checks"),
    (14, 23, "REVIEWED-NO-ERROR-FOUND", "Period-family and analytic transformation arguments were reviewed for coherence; no formal analytic verification is claimed.", "report section 1"),
    (24, 31, "REVIEWED-NO-ERROR-FOUND", "Toric cusp construction and local models were reviewed; the later integral collapse and specialization maps remain separate obligations.", "report section 1"),
    (32, 35, "VERIFIED-LOCAL/EXACT", "Finite-order fixed-point and twist arithmetic was reproduced exactly; local quotient arguments were reviewed without a concrete defect.", "core checks"),
    (36, 39, "REVIEWED-NO-ERROR-FOUND", "Global complex gluing was reviewed without a concrete local defect.", "report section 1"),
    (40, 50, "CRITICAL-UNRESOLVED", "The cusp-collapse construction requires an independently checkable global equivariant chain-level proof across all toric strata.", "R1"),
    (51, 62, "CRITICAL-UNRESOLVED", "Integral specialization, van Kampen inclusion maps, orientations, and geometric identification of the homology matrices remain uncertified.", "R2-R4"),
    (63, 66, "CONDITIONAL-PASS", "Recognition and characteristic-number deductions are sound only after the unresolved simple-connectivity and integral-homology inputs are established.", "R5"),
    (67, 86, "CONDITIONAL/CONSISTENCY", "The complex-analytic calculations are internally consistent; topology-dependent conclusions retain the Section 7 dependency.", "report sections 2.5 and 4.2"),
    (87, 94, "SECONDARY", "These results are not needed to establish existence or the S6 identification and were reviewed only for consistency.", "theorem ledger"),
    (95, 97, "SUPPORTING-EXACT", "Appendix A matrix and lattice calculations are reproduced by the exact-check script; geometric cell identifications are not certified by the algebra alone.", "core checks"),
    (98, 100, "CONDITIONAL/SUPPORTING", "Cell and homology computations are useful evidence after their printed cells and maps are identified with the actual geometry.", "R2-R4"),
    (101, 108, "CRITICAL-UNRESOLVED", "Nearby-cycle ranks are coherent, but the exact integral identification with the geometric specialization map remains uncertified.", "R2"),
]

COLORS = {
    "VERIFIED": (0.0, 0.45, 0.15),
    "REVIEWED": (0.0, 0.25, 0.65),
    "CRITICAL": (0.75, 0.05, 0.05),
    "CONDITIONAL": (0.75, 0.35, 0.0),
    "SECONDARY": (0.35, 0.35, 0.35),
    "SUPPORTING": (0.25, 0.35, 0.55),
}


def status_for(page_number: int) -> tuple[str, str, str]:
    for start, end, status, note, pointer in RANGES:
        if start <= page_number <= end:
            return status, note, pointer
    raise ValueError(page_number)


def color_for(status: str) -> tuple[float, float, float]:
    for prefix, color in COLORS.items():
        if status.startswith(prefix):
            return color
    return (0.2, 0.2, 0.2)


def main() -> None:
    OUTDIR.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(SOURCE)
    rows = []
    for index, page in enumerate(doc):
        physical_page = index + 1
        status, note, pointer = status_for(physical_page)
        color = color_for(status)
        short_label = f"MATH AUDIT: {status}"
        # Narrow vertical label in the outer right margin. It does not cover body text.
        page.insert_text(
            fitz.Point(page.rect.width - 5, page.rect.height - 24),
            short_label,
            fontsize=5,
            fontname="helv",
            color=color,
            rotate=90,
            overlay=True,
        )
        annotation_text = (
            f"Status: {status}\n"
            f"Page: {physical_page}\n"
            f"Audit note: {note}\n"
            f"Evidence pointer: {pointer}\n\n"
            "This annotation records the proof-audit classification. It does not alter the manuscript text."
        )
        annot = page.add_text_annot(fitz.Point(page.rect.width - 28, 18), annotation_text)
        annot.set_info(title="Independent mathematical proof audit", subject=status)
        annot.set_colors(stroke=color)
        annot.update()
        rows.append({
            "physical_page": physical_page,
            "status": status,
            "audit_note": note,
            "evidence_pointer": pointer,
        })

    metadata = doc.metadata
    metadata.update({
        "title": "S6 manuscript - mathematical proof-audit annotated copy",
        "subject": "Page-level audit status; main theorem not certified",
        "keywords": "S6, proof audit, mathematics, annotations",
    })
    doc.set_metadata(metadata)
    doc.set_toc([
        [1, "Exact finite algebra: pages 8-13", 8],
        [1, "Critical topology: pages 40-62", 40],
        [1, "Conditional recognition: pages 63-66", 63],
        [1, "Appendix matrix evidence: pages 95-100", 95],
        [1, "Critical nearby cycles: pages 101-108", 101],
    ])
    doc.save(OUTPUT, garbage=4, deflate=True)
    doc.close()

    with INDEX.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {OUTPUT} with {len(rows)} page annotations")


if __name__ == "__main__":
    main()
