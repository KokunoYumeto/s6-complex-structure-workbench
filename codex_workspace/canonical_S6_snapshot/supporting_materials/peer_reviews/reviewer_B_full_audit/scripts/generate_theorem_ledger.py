#!/usr/bin/env python3
"""Generate the theorem-level audit ledger from the canonical TeX headings."""
from __future__ import annotations

import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source" / "s6_canonical_full_108_pages.tex"
OUTPUT = ROOT / "evidence" / "ledgers" / "S6_THEOREM_AUDIT_LEDGER.csv"

EXACT = {
    "Lemma 2.2", "Lemma 2.4", "Lemma 2.6", "Lemma 2.7", "Lemma 2.8",
    "Lemma 5.2", "Lemma 5.5", "Proposition 5.6", "Lemma 8.2", "Lemma A.1",
}
CRITICAL = {
    "Main Theorem", "Corollary 1.1", "Proposition 7.2", "Lemma 7.5", "Lemma 7.6",
    "Lemma 7.7", "Lemma 7.8", "Lemma 7.9", "Lemma 7.10", "Proposition 7.12",
    "Theorem 7.17", "Theorem 7.22", "Proposition 7.26", "Proposition 7.27",
    "Corollary 7.29", "Theorem B.1",
}
CONDITIONAL = {
    "Theorem 8.1", "Corollary 8.5",
}


def status_for(label: str, page: int) -> tuple[str, str, str]:
    if label in EXACT:
        return (
            "VERIFIED-EXACT",
            "Finite exact algebra or complete elementary argument reproduced independently.",
            "core_checks.json and reproduce_core_checks.py" if label != "Lemma 8.2" else "Direct review of the recognition lemma.",
        )
    if label in CRITICAL:
        return (
            "CRITICAL-UNRESOLVED",
            "Indispensable to the S6 identification; the required integral geometric map has not been independently certified at chain level.",
            "See proof-risk ledger R1-R4 and critical source extracts.",
        )
    if label in CONDITIONAL:
        return (
            "CONDITIONAL-PASS",
            "The displayed deduction is sound after the unresolved Section 7 topology inputs are supplied.",
            "Mathematical proof-audit report, Sections 3-4.",
        )
    if 14 <= page <= 23:
        return (
            "REVIEWED-NO-ERROR-FOUND",
            "Period-family and analytic transformation arguments were read for coherence; no concrete defect was found and no formal analytic verification is claimed.",
            "Canonical source pages 14-23.",
        )
    if 24 <= page <= 31:
        return (
            "REVIEWED-NO-ERROR-FOUND",
            "Toric construction and local cusp filling were reviewed; later integral collapse/specialization claims are classified separately.",
            "Canonical source pages 24-31.",
        )
    if 32 <= page <= 35:
        return (
            "REVIEWED-NO-ERROR-FOUND",
            "Local logarithmic-transform construction is coherent; its finite fixed-point arithmetic is reproduced exactly in the core checks.",
            "core_checks.json plus canonical source pages 32-35.",
        )
    if 36 <= page <= 39:
        return (
            "REVIEWED-NO-ERROR-FOUND",
            "Global complex gluing and manifold arguments were reviewed without a concrete local defect.",
            "Canonical source pages 36-39.",
        )
    if 40 <= page <= 62:
        return (
            "CONDITIONAL-PASS",
            "Finite algebra was checked where extractable, but the theorem depends on unresolved integral geometric identifications in Section 7.",
            "Critical source pages and proof-risk ledger.",
        )
    if 63 <= page <= 66:
        return (
            "CONDITIONAL-PASS",
            "Recognition and characteristic-number consequences rely on the unresolved simple-connectivity and integral-homology conclusions.",
            "Mathematical proof-audit report, Section 4.",
        )
    if 67 <= page <= 86:
        return (
            "CONDITIONAL-PASS",
            "Complex-analytic calculations are internally consistent; statements involving the S6 topology retain the earlier dependency.",
            "Mathematical proof-audit report, Sections 2.5 and 4.2.",
        )
    if 87 <= page <= 94:
        return (
            "SECONDARY",
            "Not required to establish existence or the S6 identification; reviewed only for consistency with the manuscript's earlier claims.",
            "Canonical source pages 87-94.",
        )
    if 95 <= page <= 97:
        return (
            "VERIFIED-EXACT" if label == "Lemma A.1" else "REVIEWED-NO-ERROR-FOUND",
            "Appendix matrix data are reproducible exactly; fan/topological identifications are reviewed rather than formally certified.",
            "core_checks.json and canonical source pages 95-97.",
        )
    if 98 <= page <= 100:
        return (
            "CONDITIONAL-PASS",
            "Cell and homology calculations are useful exact evidence after the printed cells and specialization maps are identified with the geometry.",
            "Canonical source pages 98-100 and proof-risk ledger R2-R4.",
        )
    if 101 <= page <= 108:
        return (
            "CRITICAL-UNRESOLVED",
            "Nearby-cycle ranks are coherent, but the exact integral identification with the geometric specialization maps remains uncertified.",
            "Critical source extract pages 101-108 and proof-risk ledger R2.",
        )
    return (
        "REVIEWED-NO-ERROR-FOUND",
        "Read for coherence; no concrete defect found.",
        "Canonical source.",
    )


def clean_heading(raw: str) -> str:
    text = raw.strip()
    text = re.sub(r"\\(?:medskip)?\\?noindent", "", text)
    text = re.sub(r"\\textbf\{", "", text)
    text = text.replace("}", "")
    text = re.sub(r"\\[A-Za-z]+", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def main() -> None:
    lines = SOURCE.read_text(encoding="utf-8", errors="replace").splitlines()
    rows = [{
        "label": "Main Theorem",
        "physical_page": 3,
        "source_line": "",
        "heading_excerpt": "The constructed compact complex threefold X is diffeomorphic to S^6.",
        "status": "CRITICAL-UNRESOLVED",
        "audit_basis": "Depends on the integral topology package in Section 7 and Appendix B.",
        "evidence_pointer": "Proof-risk ledger R1-R4; mathematical proof-audit report.",
        "main_theorem_dependency": "DIRECT",
    }]
    page = 0
    heading_re = re.compile(r"\\textbf\{((?:Theorem|Proposition|Lemma|Corollary)\s+[A-Z]?\d+(?:\.\d+)?)")
    for lineno, line in enumerate(lines, 1):
        m_page = re.search(r"SOURCE PDF PAGE (\d{3}) START", line)
        if m_page:
            page = int(m_page.group(1))
        m = heading_re.search(line)
        if not m:
            continue
        label_raw = m.group(1)
        label_match = re.match(r"((?:Theorem|Proposition|Lemma|Corollary)\s+[A-Z]?\d+(?:\.\d+)?)", label_raw)
        if not label_match:
            continue
        label = label_match.group(1)
        status, basis, pointer = status_for(label, page)
        rows.append({
            "label": label,
            "physical_page": page,
            "source_line": lineno,
            "heading_excerpt": clean_heading(line)[:700],
            "status": status,
            "audit_basis": basis,
            "evidence_pointer": pointer,
            "main_theorem_dependency": "DIRECT" if status == "CRITICAL-UNRESOLVED" else ("DOWNSTREAM" if status == "CONDITIONAL-PASS" else "SUPPORTING"),
        })

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {len(rows)} rows to {OUTPUT}")


if __name__ == "__main__":
    main()
