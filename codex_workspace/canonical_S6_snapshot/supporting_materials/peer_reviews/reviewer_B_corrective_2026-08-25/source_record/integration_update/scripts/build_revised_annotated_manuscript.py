#!/usr/bin/env python3
"""Build the dated revised page-level proof-audit overlay.

The canonical manuscript pages are not altered.  Each page receives a narrow
right-margin status label and a popup annotation recording the revised audit
classification after the nearby-cycle/Leray reconstruction.
"""
from __future__ import annotations

import csv
from pathlib import Path

import fitz

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "source" / "s6_canonical_108_pages.pdf"
OUTDIR = ROOT / "integration_update" / "evidence" / "annotations"
OUTPUT = OUTDIR / "S6_REVISED_AUDIT_ANNOTATED_MANUSCRIPT.pdf"
INDEX = OUTDIR / "S6_REVISED_ANNOTATION_INDEX.csv"

RANGES = [
    (1, 7, "RECONSIDERED-PROVISIONAL",
     "The main theorem is no longer classified as blocked by cusp collapse: Appendix B plus the independent Leray route and based van Kampen survive reconstruction. The construction and external formalism remain focused review targets.",
     "Revised audit §§2–7; B1, V1, L1, G1, E1"),
    (8, 13, "VERIFIED-EXACT",
     "Monodromy, lattice, invariant/coinvariant, Smith-normal-form, exterior-power, and alternating-form calculations were reproduced exactly.",
     "Prior 38-check harness; revised exact checks"),
    (14, 23, "REVIEWED-NO-DEFECT",
     "The period family and transformation arguments were reread; exact identities used later were reproduced, and no load-bearing analytic defect was identified.",
     "G1; period exact checks"),
    (24, 31, "REVIEWED-CONSTRUCTION",
     "The toric filling, quotient, and central-fibre construction were reviewed without an identified contradiction. The later explicit collapse map is classified separately.",
     "G1; C1"),
    (32, 35, "VERIFIED-LOCAL/EXACT",
     "Finite-order actions, invariant sections, freeness arithmetic, and lattice indices were checked; the local quotient construction was reviewed without a concrete defect.",
     "Prior core checks; G1"),
    (36, 39, "REVIEWED-NO-DEFECT",
     "Global holomorphic gluing, properness, compactness, and overlap sections were reread. No concrete defect was identified; a formal analytic verification is not claimed.",
     "G1"),
    (40, 50, "OPEN-NONBLOCKING",
     "The explicit equivariant cusp-collapse and its stratum-by-stratum descent remain open audit work. This route is not a premise of the Appendix B/Leray topology proof.",
     "C1"),
    (51, 53, "MIXED-COLLAPSE-DEPENDENT",
     "The printed collapse-induced cohomology maps are coherent and their finite algebra passes, but equality with the intrinsic nearby-cycle specialization remains tied to the open collapse route.",
     "C2"),
    (54, 57, "VERIFIED-RECONSTRUCTED",
     "The based van Kampen computation was reconstructed from the explicit deck transformations, invariant sections, meridian conventions, cusp drift, and same-sign lemma; p=-1 gives a trivial group.",
     "V1; revised audit §6"),
    (58, 60, "OPEN-REDUNDANT",
     "The first Mayer–Vietoris matrices pass exact rank and Smith checks, but their complete chain-level derivation remains coupled to the explicit collapse route. The second topology route does not use them.",
     "MV1; C1–C2"),
    (61, 63, "VERIFIED-RECONSTRUCTED",
     "Using the Appendix B stalk isomorphism, the three Leray transgressions are derived from local lift discrepancies and multiplicativity; all are multiplication by p=-1.",
     "B1; L1; revised audit §5"),
    (64, 64, "VERIFIED-RECONSTRUCTED",
     "The recognition step follows from the reconstructed simple-connectivity and integral-homology calculations, then Hurewicz/Whitehead and the smooth six-dimensional homotopy-sphere classification.",
     "V1 + B1 + L1; revised audit §7"),
    (65, 65, "REVIEWED-DOWNSTREAM",
     "The stated complex-analytic invariants are downstream of the construction and topology. Exact characteristic-number consistency checks pass; individual cohomological arguments are tracked in the theorem ledger.",
     "Revised theorem ledger"),
    (66, 69, "VERIFIED-INDEPENDENT",
     "The direct period, Néron–Severi, torus algebraic-reduction, and meromorphic-descent argument proves a(X)=1 and M(X)=f^*C(t), independently of Section 7 and the CDP comparison.",
     "A1; revised audit §8"),
    (70, 83, "REVIEWED-NO-DEFECT",
     "Canonical bundle, direct-image, automorphism, and Hodge-theoretic arguments were reviewed and exact finite subclaims checked. No new load-bearing defect was identified.",
     "Revised theorem ledger"),
    (84, 86, "CONTEXT/REFERENCE-AUDIT",
     "These pages formulate the CDP comparison and identify where the candidate differs. The historical and source-by-source literature comparison remains an external reference audit.",
     "E1; revised audit §9"),
    (87, 90, "VERIFIED-LOCAL",
     "The normalization/conductor sequence and the conductor-supported ambient differential were checked in the xy and xyz normal-crossing models. The global application uses earlier topology/Picard inputs.",
     "D1; revised exact checks"),
    (91, 94, "REVIEWED-WITH-DEPENDENCIES",
     "The analytic duality, base-change, Picard, and direct-image chain is coherent. Publication-level review should map each invoked external theorem to its precise hypotheses.",
     "D1; E1"),
    (95, 100, "SUPPORTING-EXACT",
     "Appendix A's matrix, lattice, homology, and finite-fibre calculations were reproduced by exact scripts. Collapse-dependent geometric identifications retain their route-specific status.",
     "Prior 38-check harness; C2/MV1 where applicable"),
    (101, 105, "VERIFIED-RECONSTRUCTED",
     "Appendix B's intrinsic nearby-cycle specialization was reconstructed through local Milnor fibres, the sheaf V, triple-point signs, normalization/conductor cohomology, rank bookkeeping, degree-three Gysin, and saturation.",
     "B1; revised audit §4"),
    (106, 108, "EXTERNAL-REFERENCE-CHECK",
     "Bibliographic sources are preserved. The revised audit has not completed a source-by-source theorem/page/hypothesis verification of all cited external results.",
     "E1"),
]

COLORS = {
    "VERIFIED": (0.0, 0.42, 0.15),
    "RECONSIDERED": (0.15, 0.25, 0.72),
    "REVIEWED": (0.0, 0.28, 0.66),
    "OPEN": (0.78, 0.30, 0.0),
    "MIXED": (0.72, 0.35, 0.0),
    "SUPPORTING": (0.25, 0.35, 0.55),
    "CONTEXT": (0.38, 0.38, 0.38),
    "EXTERNAL": (0.48, 0.20, 0.55),
}


def status_for(page_number: int) -> tuple[str, str, str]:
    for start, end, status, note, pointer in RANGES:
        if start <= page_number <= end:
            return status, note, pointer
    raise ValueError(f"No revised status for page {page_number}")


def color_for(status: str) -> tuple[float, float, float]:
    for prefix, color in COLORS.items():
        if status.startswith(prefix):
            return color
    return (0.2, 0.2, 0.2)


def main() -> None:
    OUTDIR.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(SOURCE)
    if len(doc) != 108:
        raise RuntimeError(f"Expected 108 pages, found {len(doc)}")
    rows: list[dict[str, object]] = []
    for index, page in enumerate(doc):
        physical_page = index + 1
        status, note, pointer = status_for(physical_page)
        color = color_for(status)
        page.insert_text(
            fitz.Point(page.rect.width - 5, page.rect.height - 24),
            f"REVISED MATH AUDIT: {status}",
            fontsize=5,
            fontname="helv",
            color=color,
            rotate=90,
            overlay=True,
        )
        annotation_text = (
            f"Revised status: {status}\n"
            f"Physical page: {physical_page}\n"
            f"Audit note: {note}\n"
            f"Evidence pointer: {pointer}\n\n"
            "Dated correction: 25 August 2026. This annotation records the revised proof-audit classification and does not alter the manuscript text."
        )
        annot = page.add_text_annot(fitz.Point(page.rect.width - 28, 18), annotation_text)
        annot.set_info(title="Revised independent mathematical proof audit", subject=status)
        annot.set_colors(stroke=color)
        annot.update()
        rows.append({
            "physical_page": physical_page,
            "status": status,
            "audit_note": note,
            "evidence_pointer": pointer,
        })

    metadata = dict(doc.metadata)
    metadata.update({
        "title": "S6 manuscript - revised mathematical proof-audit annotated copy",
        "subject": "Dated corrective page-level audit after nearby-cycle/Leray reconstruction",
        "keywords": "S6, complex threefold, proof audit, revised annotations, nearby cycles, Leray",
    })
    doc.set_metadata(metadata)
    doc.set_toc([
        [1, "Reconsidered main claim and construction: pages 1-39", 1],
        [1, "Open explicit collapse route: pages 40-53", 40],
        [1, "Reconstructed van Kampen route: pages 54-57", 54],
        [1, "Redundant first Mayer-Vietoris route: pages 58-60", 58],
        [1, "Reconstructed nearby-cycle/Leray topology: pages 61-64 and 101-105", 61],
        [1, "Independent algebraic reduction: pages 66-69", 66],
        [1, "CDP local mechanism and reference audit: pages 84-94", 84],
        [1, "Appendices and references: pages 95-108", 95],
    ])
    doc.save(OUTPUT, garbage=4, deflate=True)
    doc.close()

    with INDEX.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {OUTPUT} with {len(rows)} revised page annotations")


if __name__ == "__main__":
    main()
