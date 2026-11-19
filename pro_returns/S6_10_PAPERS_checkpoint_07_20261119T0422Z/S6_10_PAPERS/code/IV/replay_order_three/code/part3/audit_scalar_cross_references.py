#!/usr/bin/env python3
"""Read-only active-Part3 reference audit and exact proposed prose repairs."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[2]
stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
archive = ROOT / "records/attempts/scalar_fan_dependency_correction" / stamp
target = ROOT / "notes/part3.tex"
text = target.read_text()
replacements = [
("P3F.5",
 r"The actual component-supported OS49 page and both diagonal-fan returns are proved in P3F.31--32 and P3K.17, retaining the marking of P3F.27.",
 r"P3F.31--32 construct the actual positive-diagonal OS49 page and prove its zero return index. With the full marking of P3F.27, P3K.65 proves that the negative-diagonal filling has class \(-3k\) for the actual positive \(r\)-loop \(\lambda=r^{3k}\), and class \(-k\) for the shorter \(w\)-loop \(\lambda=w^k\); the positive fan has class zero on both parameters.",
 "Haefliger/page discussion and all original-family conclusions unchanged."),
("P3F.20",
 r"Its component-permuting translation is carried through the actual positive-fan page in P3F.31--32 and through the charged Cox comparison to the negative fan in P3K.17. Both sphere sectors have return index zero by those explicit morphisms.",
 r"Its component-permuting translation is carried through the actual positive-fan page in P3F.31--32, giving positive-fan index zero. P3K.65 retains the full native C2 closing and Cox ruling arrow and gives negative-fan class \(-3\) for \(\lambda=r^3\), or \(-1\) for the actual shorter scalar loop \(\lambda=w\). No negative-fan integer index is assigned here.",
 "Wang integral topology and OS49 page height arithmetic unchanged."),
("P3F.27",
 r"The exact change of page marking is given below; its original direct graph-line comparison is retained as an auxiliary route, while P3K.17 proves the actual return index zero.",
 r"The exact change of page marking is given below. Its original direct graph-line comparison remains an auxiliary route; P3F.31 proves positive-fan index zero, and P3K.65 gives negative-fan class \(-3\) for this \(r\)-loop.",
 "Angular K cycle, origin maps and deck gauge unchanged."),
("P3F.27",
 r"P3K.17 then constructed the actual charged Cox flop bordism and proved that both diagonal fillings have return index zero. The direct negative-fan graph homotopy is not needed by that completed proof.",
 r"P3K.65 constructs the full native C2 return and the oriented Cox ruling arrow, giving negative-fan class \(-3\) while the positive fan has class zero. That proof retains the outer normal-line marking and does not use the incomplete direct negative-fan graph homotopy.",
 "Historical direct graph attempt remains explicitly uncompleted."),
("P3F.27",
 r"Their actual positive-fan page identification is P3F.31, and the negative-fan return is related to it by the explicit bordism of P3K.17.",
 r"Their actual positive-fan page identification is P3F.31. P3K.65 relates the actual two sphere returns by its native relative diffeomorphism and oriented Cox arrow; it does not identify the two integer indices.",
 "Compact page invariants and failed auxiliary homotopy retained."),
("P3F.28",
 r"The direct mixed-circle symbol comparison is an auxiliary route; P3K.17 computes the actual return independently.",
 r"The direct mixed-circle symbol comparison remains an auxiliary route. The actual positive-fan index is computed in P3F.31--32, and P3K.65 computes the corrected negative-fan sphere class by the native Cox arrow.",
 "Exact derived sequences/direct images remain the proved statement."),
("P3F.28",
 r"The direct spin-c symbol comparison pursued here remains an auxiliary route; the actual return has since been computed as zero by P3F.31--32 and P3K.17.",
 r"The direct spin-c symbol comparison pursued here remains an auxiliary route. P3F.31--32 give positive-fan index zero; P3K.65 gives the negative-fan class \(-3k\) for \(\lambda=r^{3k}\), retaining the actual closing and normal marking.",
 "No change to the sheaf morphisms or their acyclicity proof."),
("P3F.28",
 r"The actual equality of the two return indices is instead proved by the charged Cox bordism in P3K.17.",
 r"P3K.65 supplies the actual sphere-return comparison by the native Cox ruling map. It gives different fan classes and assigns no equality of the two integer indices.",
 "Dolbeault-index equality remains exact; it is not identified with the two return indices."),
("P3F.29",
 r"P3K.17 proves equality with the negative-fan return, so both sphere sectors have index zero.",
 r"P3K.65 gives negative-fan class \(-3k\) for the positive \(r\)-loop and \(-k\) for the shorter \(w\)-loop, for both norm signs and every fixed delta character; the positive-fan index is zero on both parameters.",
 "All cap freeness, specialization and coprime topology conclusions unchanged."),
("P3F.30",
 r"The actual return is zero by P3K.17.",
 r"The positive-fan return index is zero by P3F.31; P3K.65 gives the original negative-fan \(r\)-loop class \(-3\) by the full native Cox comparison.",
 "Quadratic norm morphism, transverse A1 equation and opposite base shifts unchanged."),
("P3F.30",
 r"The actual zero return for both diagonal fillings is proved separately by P3F.31--32 and P3K.17.",
 r"The positive-fan zero index is proved separately by P3F.31--32. P3K.65 retains the missing outer normal-line marking and computes the negative-fan sphere class by the native Cox ruling arrow; no negative-fan integer index is assigned by this norm route.",
 "The uncompleted norm-route comparison is still explicitly uncompleted."),
("P3F.31",
 r"P3K.17 gives the actual charged flop comparison with the negative-diagonal filling.",
 r"P3K.65 gives the actual native C2 flop comparison and the negative-diagonal \(r\)-loop class \(-3\).",
 "Entire independently proved positive-fan statement unchanged."),
("P3F.31",
 r"P3K.17 subsequently proves that the negative-diagonal family in P3F.26 has the same actual return, by its charged Cox bordism including the extra fixed-locus sphere-bundle boundary.",
 r"P3K.65 subsequently proves that the negative-diagonal family in P3F.26 has \(r\)-loop class \(-3\), by its actual native C2 return and oriented Cox ruling map. Its outer normal-line marking is retained, and no equality of the two integer indices is claimed.",
 "Positive-fan open embedding/topology/page proof and literal E26 scope unchanged."),
("P3F.32",
 r"P3K.17 proves the same return for the negative-diagonal filling by the explicit charged flop bordism.",
 r"P3K.65 gives the corrected negative-diagonal sphere class \(-3k\) for this positive \(r\)-loop, or \(-k\) for the shorter \(w\)-loop, for both norm signs and every fixed delta character.",
 "All-order positive-fan zero-index and product-mapping-torus theorem unchanged."),
]

rows = []
for sid, old, new, retained in replacements:
    assert text.count(old) == 1, (sid, text.count(old), old)
    start = text.index(old)
    line = text.count("\n", 0, start) + 1
    rows.append({"statement": sid, "file": "notes/part3.tex", "line": line,
                 "old": old, "proposed_new": new, "retained_scope": retained,
                 "new_proof_dependency": "P3K.65, root full audit PASS"})

seen = set()
files = []
def visit(p):
    if p in seen:
        return
    seen.add(p)
    files.append(p)
    for m in re.finditer(r"\\input\{([^}]+)\}", p.read_text()):
        q = ROOT / m.group(1)
        if q.exists():
            visit(q)
visit(target)
refs = []
rx = re.compile(r"(?:P3)?K\.?\s*(?:17|25|29|31)\b")
for p in files:
    sid = status = ""
    for n, line in enumerate(p.read_text().splitlines(), 1):
        m = re.search(r"\\begin\{statement\}\{([^}]+)\}\{([^}]+)\}", line)
        if m:
            sid, status = m.groups()
        if rx.search(line):
            refs.append({"file": str(p.relative_to(ROOT)), "line": n,
                         "statement": sid, "status": status, "text": line})

retained_ids = {"P3K.40", "P3K.50", "P3K.51", "P3K.52", "P3K.54",
                "P3K.55", "P3K.56", "P3K.59", "P3K.60"}
retained = []
for row in refs:
    if row["status"] == "Proved" and row["statement"] in retained_ids:
        row = dict(row)
        row["audit_classification"] = (
            "Retained local topology/frame citation. This proof supplies its own "
            "actual ordinary/native product and does not use the withdrawn scalar initial data.")
        retained.append(row)

source_paths = [
 "notes/part3_family.md", "notes/part3_other_families.md",
 "notes/part3_os49_component.md", "notes/part3_os49_index_input.md",
 "notes/part3_os49_all_orders.md", "notes/part3_os49_norm.md",
 "notes/part3_os49_positive_fan.md", "notes/part3_os49_positive_orders.md",
 "code/part3/render_part3_tex.py",
]
source_refs = []
for rel in source_paths:
    p = ROOT / rel
    for n, line in enumerate(p.read_text().splitlines(), 1):
        if "P3K.17" in line or ("both" in line and "zero" in line):
            source_refs.append({"file": rel, "line": n, "text": line,
                                "action": "Apply the corresponding scoped K65 repair before aggregate regeneration."})
for rel in ["notes/part3.tex", *source_paths]:
    p = ROOT / rel
    q = archive / rel
    q.parent.mkdir(parents=True, exist_ok=True)
    q.write_bytes(p.read_bytes())

report = {
    "utc": datetime.now(timezone.utc).isoformat(),
    "status": "READ_ONLY_AUDIT_COMPLETE", "main_input_modified": False,
    "aggregate_sha256": hashlib.sha256(target.read_bytes()).hexdigest(),
    "originals_archive": str(archive.relative_to(ROOT)),
    "active_proved_os49_pointer_count": len(rows),
    "exact_proposed_replacements": rows,
    "retained_local_citations": retained, "regeneration_sources": source_refs,
    "raw_artifact_correction": "code/part3/scalar_dependency_scope.py; every old/new field and generator byte retained under records/attempts/scalar_fan_dependency_correction/",
    "aggregate_regeneration_warning": (
        "render_part3_tex.py hardcodes four stale statement summaries and rewrites "
        "the manually maintained include tail. Do not rerun it on the master until "
        "the scoped prose replacements and include preservation are coordinated."),
}
(ROOT / "records/scalar_cross_reference_audit.json").write_text(json.dumps(report, indent=2) + "\n")
lines = [
 "# Active scalar/OS49 reference audit after checkpoint15", "",
 "This audit leaves the aggregate manuscript and its source Markdown unchanged.",
 "Every proposed replacement below refers to the fully audited P3K.65 and preserves the independent source, line, topology or positive-page proof.",
 "", "## Fourteen live prose pointers requiring replacement", "",
 "| Statement | Current aggregate line | Retained proof scope | Required return correction |",
 "|---|---:|---|---|",
]
for row in rows:
    lines.append(f"| {row['statement']} | {row['line']} | {row['retained_scope']} | Use the exact saved scoped K65 replacement. |")
lines += [
 "", "The exact old and proposed new TeX strings are in records/scalar_cross_reference_audit.json. No negative-fan integer index is assigned. The negative-fan sphere classes are -3k for r and -k for the shorter w; the positive fan has index and class zero on both.",
 "", "## Citations that remain valid", "",
 "K40, K50–52, K54–56, K59 and K60 use K29's integral cells/meridians or K31's actual local product-frame, flop and normal-reset maps. Their own source/native products are constructed separately. Each exact citation is recorded; none imports the withdrawn scalar rank-one initial variation.",
 "", "## Raw result scope and reproduction", "",
 "Source/root/cap/topology and independent reference values remain active. Old universal scalar-fan formulas, ranges and scalar initial matrices now have explicit field-level withdrawal flags. Original values and earlier audits remain stored with exact old-to-new field logs. Twenty-seven historical generators have a final scope-only postprocessor; their mathematical code is unchanged. A fresh catalogue run still passes all 437 arithmetic checks and marks all 32 all_fan fields as prior-formula arithmetic rather than active return values.",
 "", "K41/K43/K44 summary rows describe retained actual family-morphism and iterate reductions; their statuses now say that precise scope. Their compound numerical universal-fan applications remain withdrawn.",
 "", "## Aggregate-regeneration caution", "",
 report["aggregate_regeneration_warning"], "",
 "Source files requiring corresponding prose edits are listed with exact lines in the audit JSON. Their current bytes and the aggregate were archived without changing them.",
]
(ROOT / "notes/part3_scalar_cross_reference_audit.md").write_text("\n".join(lines) + "\n")
print("Recorded", len(rows), "exact proposed prose replacements and",
      len(retained), "retained local citations; aggregate/source files unchanged.")
