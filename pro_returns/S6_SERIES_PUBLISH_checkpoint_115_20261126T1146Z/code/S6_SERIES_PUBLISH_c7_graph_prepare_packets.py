#!/usr/bin/env python3
"""Prepare exact S8/S9 repair packets; never alter the canonical manuscript."""
from __future__ import annotations
import csv
import hashlib
import re
import subprocess
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "agents/continuation7_iii_graph"
RELEASE = ROOT / "agents/continuation6_iii_finite"
MAIN = ROOT / "S6_SERIES_PUBLISH_III.tex"
NOW = datetime.now(timezone.utc).isoformat()
WHO = ("GPT-6 Astra (OpenAI), ChatGPT Pro mode; numerical reasoning effort "
       "not separately exposed; seventh-continuation graph/cap review")
EVENT_FIELDS = ["statement_id","date","who","type","outcome","event_id","phase",
                "source_file","source_row","source_event_type","evidence_group",
                "publish_input_file","publish_input_row","date_utc","where"]
DEFECT_FIELDS = ["change_id","type","statement_id","old_location","old_page",
                 "new_location","new_page","old_text","new_text","reason","review_status"]

def write_text(path: Path, text: str) -> None:
    with path.open("w", encoding="utf-8", newline="\n") as f:
        f.write(text)

def write_tsv(path: Path, fields: list[str], rows: list[dict]) -> None:
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(rows)

def block(text: str, env: str) -> str:
    start = text.index("\\begin{" + env + "}")
    end = text.index("\\end{" + env + "}", start) + len("\\end{" + env + "}")
    return text[start:end]

def span(text: str, start: str, end: str) -> str:
    i = text.index(start)
    return text[i:text.index(end, i)].rstrip()

def anchors(text: str) -> Counter:
    answer = Counter()
    for typ, expr in [
        ("label", r"\\label\{([^}]+)\}"),
        ("target", r"\\hypertarget\{([^}]+)\}"),
        ("equation-tag", r"\\tag\{([^}]+)\}")]:
        answer.update((typ, v) for v in re.findall(expr, text))
    return answer

def check_braces(text: str) -> None:
    level = 0
    for m in re.finditer(r"(?<!\\)[{}]", text):
        level += 1 if m.group() == "{" else -1
        assert level >= 0, ("unmatched closing brace", m.start())
    assert level == 0, ("unmatched opening braces", level)

canonical = MAIN.read_text()
bib = (ROOT / "S6_SERIES_PUBLISH_references.bib").read_text()
bib += (OUT / "S6_SERIES_PUBLISH_III_graph_references.bib").read_text()
bibkeys = set(re.findall(r"@\w+\s*\{\s*([^,\s]+),", bib))
with (ROOT / "S6_SERIES_PUBLISH_tags.tsv").open() as f:
    labelkeys = {r["label"] for r in csv.DictReader(f, delimiter="\t")}

existing_defects = []
for name in ["S6_SERIES_PUBLISH_III_graph_line_core_defects.tsv",
             "S6_SERIES_PUBLISH_III_graph_boundary_defects.tsv"]:
    with (ROOT / "agents/continuation6_iii_root" / name).open() as f:
        existing_defects.extend(csv.DictReader(f, delimiter="\t"))

receivers = []
for tag, sid in [("02S8", "night:P3F.31"), ("02S9", "night:P3F.32")]:
    receiver_path = OUT / f"S6_SERIES_PUBLISH_III_{tag}_receiving.tex"
    old_statement = block((RELEASE / f"S6_SERIES_PUBLISH_III_{tag}_released_statement.tex").read_text(), "theorem")
    old_proof = block((RELEASE / f"S6_SERIES_PUBLISH_III_{tag}_released_proof.tex").read_text(), "proof")
    rec0 = receiver_path.read_text()
    new_statement, new_proof = block(rec0, "theorem"), block(rec0, "proof")
    receiver = new_statement + "\n\n" + new_proof + "\n"
    assert rec0.rstrip("\n") == receiver.rstrip("\n")
    # Only terminal blank lines are removed from this staged receiver.
    write_text(receiver_path, receiver)
    receivers.append(receiver)
    assert canonical.count(old_statement) == 1
    assert canonical.count(old_proof) == 1
    assert anchors(old_statement + old_proof) == anchors(receiver), (
        tag, anchors(old_statement + old_proof), anchors(receiver))
    check_braces(receiver)
    refs = set(re.findall(r"\\SeriesRef\{([^}]+)\}", receiver))
    assert refs <= labelkeys, (tag, "unknown series labels", refs - labelkeys)
    cites = set()
    for value in re.findall(r"\\cite(?:\[[^]]*\])?\{([^}]+)\}", receiver):
        cites.update(value.split(","))
    assert cites <= bibkeys, (tag, "unknown bibliography keys", cites - bibkeys)
    for bad in ["\\StatementRecord", "agents/", "code/", ".py", ".json",
                "fresh derivation", "checkpoint", "historical checks"]:
        assert bad not in receiver, (tag, "process residue", bad)

    replacements = [
        dict(statement_id=sid, old_text=old_statement, new_text=new_statement),
        dict(statement_id=sid, old_text=old_proof, new_text=new_proof)]
    write_tsv(OUT / f"S6_SERIES_PUBLISH_III_{tag}_replacements.tsv",
              ["statement_id","old_text","new_text"], replacements)
    applied = canonical.replace(old_statement, new_statement, 1).replace(old_proof, new_proof, 1)
    assert applied.count(new_statement) == 1 and applied.count(new_proof) == 1
    assert applied.replace(new_statement, old_statement, 1).replace(new_proof, old_proof, 1) == canonical
    assert replacements[0]["new_text"] + "\n\n" + replacements[1]["new_text"] + "\n" == receiver

    if tag == "02S8":
        core_new = span(new_proof, r"\textit{The compatible core arc.}",
                        r"\textit{The cap sphere and its normal Euler number.}")
        cap_new = span(new_proof, "On the capped normal sphere bundle, define b",
                       r"\textit{The cap sphere and its normal Euler number.}")
        directed_old = span(old_proof, "The different incoming torus marking is retained:",
                            "Their closed difference")
        directed_new = span(new_proof, "For the tangent Pontryagin number compare",
                            "Their common-boundary gluing")
    else:
        core_new = span(new_proof, "For \\(d=0,n=1\\), the m-sheet construction",
                        "We transport the full normal problem")
        cap_new = core_new
        directed_old = span(old_proof, "The cap marking still has",
                            "Thus the actual sphere-bundle bordism")
        directed_new = span(new_proof, "The same conclusion has an explicit page-line boundary map.",
                            "It remains to transport")
    rows = []
    for old_row in existing_defects:
        if old_row["statement_id"] != sid:
            continue
        row = dict(old_row)
        row["new_location"] = str(receiver_path.relative_to(ROOT))
        row["new_text"] = core_new if "interior-core" in row["change_id"] else cap_new
        row["reason"] += (" The complete corrected graph/cap derivation now gives old "
                         "cochain 2a, cap coefficient -1, b²=-8k and p1=-24k; "
                         "the original final conclusions are proved with their exact "
                         "return and product maps. This updates the original change ID.")
        row["review_status"] = ("confirmed D25; complete corrected receiver compared with "
                                "original and passed independent root mathematical reading; "
                                "guarded application and final page concordance pending")
        row["new_page"] = "pending final typeset page concordance"
        rows.append(row)

    def defect(code: str, suffix: str, old: str, new: str, reason: str) -> None:
        rows.append(dict(
            change_id=f"c7-III-{tag}-{suffix}", type=code, statement_id=sid,
            old_location=f"{tag} released statement/proof, exact guarded block",
            old_page="pending final page concordance",
            new_location=str(receiver_path.relative_to(ROOT)),
            new_page="pending guarded application and final page concordance",
            old_text=old, new_text=new, reason=reason,
            review_status="complete original/receiver comparison; staged for root admission"))

    defect("D25", "directed-cap-meridian", directed_old, directed_new,
           "The admitted e_u period is -u_h plus two invariant integral shears. "
           "The exact coordinate and affine conjugacy carries the ordinary killed "
           "meridian to beta_0=H_*. The old geometric gamma cap was not that marked cap. "
           "The correction retains the inverse point maps and extending cap character.")
    defect("D10", "statement-header", old_statement, new_statement,
           "Replace the machine StatementRecord header by the mathematical title and "
           "small permanent tag; preserve every statement label and hypertarget.")
    defect("D16", "mathematical-title", r"\begin{theorem}", new_statement.split("\n")[0],
           "Give the main-chain theorem its short mathematical title without changing scope.")
    defect("D04", "resolved-series-references", old_proof, new_proof,
           "All printed run-number references in this complete guarded proof are replaced "
           "by resolving SeriesRef calls or exact primary-source citations. Every original "
           "reference and auxiliary claim is accounted for in the comparison table.")
    defect("D14", "single-proof-structure",
           r"\begin{enumerate}[label={$\langle1\rangle$\arabic*.},leftmargin=*]",
           new_proof,
           "Remove the machine-numbered item structure and place the construction before its "
           "graph and return calculation. S8 develops the universal handle calculation once; "
           "S9 supplies the full finite-parameter and transport scope.")
    if tag == "02S8":
        historical = ("The named historical checks of these maps and of the relative "
                      "cohomology argument are retained in the statement record.")
        assert historical in old_proof
        defect("D01", "historical-check-prose", historical, "[deleted]",
               "A production-history sentence has no mathematical content in the proof.")
        prompt_piece = ("the additional configuration separately requested by the prompt, "
                        "rather than an instance of that particular hypothesis.")
        assert prompt_piece in old_proof
        defect("D05", "prompt-reference", prompt_piece,
               "The construction above supplies its component\n"
               "divisor directly.",
               "Replace the prompt comparison by the exact component-degree obstruction "
               "to the whole-fibre hypothesis and the constructed divisor.")
        defect("D08", "workflow-wording",
               "The supplied E26 Mumford proposition permits arbitrary periodic unimodular "
               "triangulations and does not select one of these diagonals.",
               span(new_proof, "The fan construction of", "For the whole-fibre hypothesis"),
               "State the exact periodic-fan hypothesis with a resolving primary citation, "
               "without workflow qualifiers.")
    write_tsv(OUT / f"S6_SERIES_PUBLISH_III_{tag}_defects.tsv", DEFECT_FIELDS, rows)

    events = []
    def event(kind: str, suffix: str, source: str, evidence: str, outcome: str) -> None:
        packet = f"agents/continuation7_iii_graph/S6_SERIES_PUBLISH_III_{tag}_CHECK_EVENTS.tsv"
        events.append(dict(
            statement_id=sid, date=NOW[:10], who=WHO, type=kind, outcome=outcome,
            event_id=f"publish:c7:III:{tag}:{suffix}",
            phase="after individual original-proof exposure; corrected graph/cap review",
            source_file=source, source_row="1", source_event_type=kind,
            evidence_group=evidence, publish_input_file=packet,
            publish_input_row=str(len(events)+2), date_utc=NOW,
            where=f"agents/continuation7_iii_graph/S6_SERIES_PUBLISH_III_{tag}_comparison.md; "
                  f"agents/continuation7_iii_graph/S6_SERIES_PUBLISH_III_{tag}_receiving.tex"))
    event("used and rechecked in this run", "corrected-graph-cap-proof",
          "agents/continuation7_iii_graph/S6_SERIES_PUBLISH_III_cap_geometry_independent_review.md",
          "publish:c7:III:OS49:corrected-global-graph-cap",
          "Post-exposure full derivation/review of the actual graph class, compatible arc, "
          "all-sheet disjoint cap ball, normal Euler orientation, H-circuit homology, "
          "integral cap coefficient, ordered intersection form and all-k dual cycle. "
          "The component degrees remain (0,0), the incoming cap class remains "
          "2m[dh_* wedge d tau_*], and the corrected closed square is -8k. "
          "Closed-boundary signature additivity gives p1=-24k, hence A_U=A_M=0; "
          "the actual Hopf/closing conventions give oriented sphere class zero and "
          "the explicit identity-to-return isotopy gives the product mapping torus. "
          "The d and n transport maps are retained in full. Root independently read "
          "the complete replacement; no old withdrawn graph proof credit is revived.")
    event("computation or formal certificate", "cap-normal-exterior-algebra",
          "code/S6_SERIES_PUBLISH_c7_graph_cap_orientation.py",
          "publish:c7:III:OS49:cap-normal-exterior-algebra",
          "New sparse exterior-algebra calculation, importing no former determinant program: "
          "the full normal-first wedge has sign -2pi r c_phi(U²+V²)² with all additional "
          "height/radius derivatives cancelling; the projected section first jet has "
          "positive determinant. The program also checks the source cubic substitution "
          "and symbolic positive-fan reflection. Complete successful output was read. "
          "Shared evidence for S8/S9, not two independent computations.")
    event("computation or formal certificate", "integral-global-pairing",
          "code/S6_SERIES_PUBLISH_c7_graph_integral_pairing.py",
          "publish:c7:III:OS49:integral-global-pairing",
          "Root's new exact integer program derives the vanishing vectors and affine physical "
          "coefficients, verifies the all-k symbolic dual-cycle recurrence U^t x=b+V^t(1,0), "
          "Vx=0 and b(x)=-8k, and checks dense integral forms for k=1,2,3 using rational "
          "domain-matrix rank. This checker independently obtained the same dual cycle before "
          "reading that program, then read the full derivation and successful output. "
          "The finite cases are consistency checks; the universal conclusion uses the "
          "symbolic recurrence. Shared evidence is counted once per mathematical computation.")
    event("used and rechecked in this run", "full-original-comparison",
          f"agents/continuation7_iii_graph/S6_SERIES_PUBLISH_III_{tag}_comparison.md",
          f"publish:c7:III:{tag}:full-original-comparison",
          "Complete released statement and every original proof item read against the new "
          "receiver, including all auxiliary fan, line, compact-page, boundary, finite-cap, "
          "clutch, root-winding, orientation, negative-C2 and product-torus assertions. "
          "All original permanent anchors and equation tags are preserved. Exact guards "
          "are unique and reversible in the canonical source. The punctured parameter "
          "domain makes the already admitted scope explicit; no new D26 is proposed. "
          "The separately proved negative side of P3K65 is invoked at its admitted scope; "
          "its positive side is not a circular input, and no new IV check is claimed.")
    write_tsv(OUT / f"S6_SERIES_PUBLISH_III_{tag}_CHECK_EVENTS.tsv", EVENT_FIELDS, events)

    print(tag, "old proof SHA256", hashlib.sha256(old_proof.encode()).hexdigest())
    print(tag, "receiver SHA256", hashlib.sha256(receiver.encode()).hexdigest())
    print(tag, "unique exact guards 2; reversible application PASS; "
          "permanent identities", len(anchors(receiver)), "PASS; "
          "known SeriesRef labels", len(refs), "PASS; citation keys", len(cites), "PASS")
    print(tag, "proposed defect rows", len(rows), "(includes 2 existing-ID updates); "
          "proposed event rows", len(events))
    print(tag, "no D26 row; no canonical mutation")

# Compile only the two owned receivers, using a temporary display harness.
# It is a syntax/width check, not a final-paper pagination or page-reading claim.
qa = Path("/workspace/scratch/bd22a44d51b1/temporary_literature/c7_graph_receiver_qa")
qa.mkdir(parents=True, exist_ok=True)
preamble = r"""\documentclass[11pt]{article}
\usepackage[T1]{fontenc}
\usepackage[margin=1in]{geometry}
\usepackage{amsmath,amssymb,amsthm,hyperref}
\newtheorem{theorem}{Theorem}
\newcommand{\SeriesRef}[1]{\textup{\texttt{\detokenize{#1}}}}
\renewcommand{\cite}[2][]{[citation]}
\begin{document}
"""
write_text(qa / "receivers.tex", preamble + "\n\\clearpage\n".join(receivers) + "\n\\end{document}\n")
result = subprocess.run(
    ["pdflatex","-interaction=nonstopmode","-halt-on-error","receivers.tex"],
    cwd=qa, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=False)
log_path = qa / "receivers.log"
log = log_path.read_text(errors="replace") if log_path.exists() else ""
errors = [line for line in log.splitlines() if line.startswith("!")]
overfull = re.findall(r"Overfull \\hbox \(([\d.]+)pt too wide\).*", log)
print("Standalone receiver syntax check return code", result.returncode)
print("Standalone receiver errors", errors)
print("Standalone receiver overfull widths", overfull)
if (result.returncode != 0 and "I can't find the format file" in result.stdout
        and "pdflatex.fmt" in result.stdout):
    print("Standalone syntax compile BLOCKED: pdflatex exists, but its format "
          "pdflatex.fmt is unavailable and mktexfmt has no entry for it.")
    print("No format provisioning performed. This staged syntax check gives "
          "no build or final-page-reading credit. The later whole-paper "
          "pdfLaTeX build and page-reading gate remains open.")
else:
    assert result.returncode == 0, result.stdout[-5000:]
    print("Standalone syntax compilation passed; this is not final-paper pagination.")
print("All exact packet checks passed. Canonical manuscript unchanged.")

