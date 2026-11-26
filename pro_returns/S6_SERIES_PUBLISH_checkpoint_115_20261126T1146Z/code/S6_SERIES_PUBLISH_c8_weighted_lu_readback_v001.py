"""Exact LU readback clarifications after the complete publication reading."""
import csv
from datetime import datetime, timezone
from pathlib import Path
import S6_SERIES_PUBLISH_c8_integrate_units as units

root = Path(__file__).resolve().parent.parent
lane = root / "agents/continuation8_iii_weighted_units"
path = root / "agents/continuation8_iii_integration/units/weighted/height_integral_pairs.tex"
original = path.read_text()
text = original
table = lane / "S6_SERIES_PUBLISH_LU_publication_defects.tsv"
with table.open(newline="") as stream:
    reader = csv.DictReader(stream, delimiter="\t")
    fields = reader.fieldnames
    rows = list(reader)
number = max(int(row["change_id"].split("-")[-2]) for row in rows)


def replace(old, new, kinds, reason, count=1):
    global text, number
    assert text.count(old) == count, (old, count, text.count(old))
    for _ in range(count):
        at = text.index(old)
        number += 1
        for kind in kinds.split(";"):
            rows.append(dict(zip(fields, [f"III-C8-LU-PUB-{number:03}-{kind}", kind, "maps:src:D.2.52",
                f"height_integral_pairs.tex, readback at line {text.count(chr(10),0,at)+1}", "pending page concordance",
                "weighted/height_integral_pairs.tex", "pending final build", old, new, reason,
                "whole source read; root admission and global integration pending"])))
        text = text[:at] + new + text[at+len(old):]


replace("there is a finite exact integral algorithm for the fundamental group\nand every integral homology group.", "a finite exact integral algorithm computes a fundamental-group\npresentation and every integral homology group.", "D20;D24", "State the precise output proved by the generator/relator algorithm: a finite presentation, together with all homology groups.")
replace("with $d_0\\mid ab$. Across all twenty-one profiles there\nare exactly $45$ additional residue pairs modulo $d_0$.", "with $d_0\\mid ab$. Across the twenty-one profiles, exactly $45$\nheight-integral residue pairs modulo $d_0$ have a fibre at which\nboth section classes are nonzero.", "D20;D22", "Give the exact local condition counted by the CRT difference H−N, rather than leaving additional without its reference condition.")
replace("Consequently the given boundary marking\n$(e_1,e_2,\\delta,\\gamma)$ has precisely the monodromy\n\\eqref{maps:eq:D.GI2},", "Let $B,g$ be the marked elliptic monodromy and cocycle of $G$,\nand put $J=\\left(\\begin{smallmatrix}0&1\\\\-1&0\\end{smallmatrix}\\right)$.\nThe given boundary marking $(e_1,e_2,\\delta,\\gamma)$ then has\nprecisely the monodromy $T_i$ of \\eqref{maps:eq:D.GI2},", "D20", "Restore the explicit B,g,J definitions at their first use after consolidation, with the same marked periods and alternating form as LS.")
replace("Thus every hypothesis of the integer bar construction is satisfied\nwith these actual periods and units.", "The integer bar construction therefore applies to this tuple\nwith its actual periods and units.", "D08", "State the proved application directly after integrality and the ordered product.")
replace("At an original additive site the weight is zero, the same line\n$M_D$ has invariant degree vector $c$, and the supplied orbit\ncondition is $h=1$.", "At an original additive site in the $h=1$ sector, the weight is\nzero and the same line $M_D$ has invariant degree vector $c$.", "D20;D26", "Make the local sector explicit at its first sentence; the unchanged zero-degree case remains handled by its specified frame later.")
replace("The return inversion carries the marked section cocycle and its\nlogarithm to $\\widehat q=-q$ and $\\widehat z=-z$.", "Write $\\mathbf q$ for the marked section cocycle in this return\nconvention. Return inversion carries it and its logarithm to\n$\\widehat{\\mathbf q}=-\\mathbf q$ and $\\widehat z=-z$.", "D20", "Separate the vector-valued section cocycle from the base coordinate q already used in the line units.")
replace("The corresponding fibre basis change is\n$\\operatorname{diag}(I_2,1,-1)$, its own inverse.", "The corresponding fibre basis change is\n$P_\\gamma=\\operatorname{diag}(I_2,1,-1)$, its own inverse;\nthe monodromy changes by $\\widehat T=P_\\gamma^{-1}TP_\\gamma$.\nIts elliptic--long column is therefore $-\\mathbf q$.", "D20;D22", "Give the exact conjugacy proving the section-cocycle sign under the actual based roof reversal, rather than an unbound sign convention.")
replace("Write $R$ for orbit sums and\n$w=R\\mu/q_0$.", "Use the orbit-sum map $R$, representative section $s$ and\npartial-sum inverse $\\mathcal K$ of\n\\eqref{maps:eq:IC_local_10}--\\eqref{maps:eq:IC_local_12}, and put\n$w=R\\mu/q_0$.", "D06;D20", "Give the precise earlier locators for every reused orbit map after removing the duplicated derivation.")
replace("T_1", "T_{H_1}", "D20", "Use T_H1 for Tor H1 to avoid collision with the current unit monodromy T_1. The group and both occurrences in the homology table are transported by the identity.", count=4)
for old, new in [
    (r"45/\mathrm{default},\mathrm{II}", r"\mathrm{OS45/default},\mathrm{OS45/II}"),
    (r"46/\mathrm{default},\mathrm{II}", r"\mathrm{OS46/default},\mathrm{OS46/II}"),
    (r"50/\mathrm{default},\mathrm{II},\mathrm{IV}", r"\mathrm{OS50/default},\mathrm{OS50/II},\mathrm{OS50/IV}"),
    (r"55/\mathrm{default},\mathrm{II}", r"\mathrm{OS55/default},\mathrm{OS55/II}"),
]:
    replace(old, new, "D04;D20", "Print the full marked profile names in the CRT count table; the data and multiplicities are unchanged.")
units.check_permanent_identifiers(original, text)
path.write_text(text, newline="\n")
with table.open("w", newline="") as stream:
    writer = csv.DictWriter(stream, fieldnames=fields, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
print("UTC", datetime.now(timezone.utc).isoformat())
print("LU_LINES", len(original.splitlines()), "->", len(text.splitlines()), "SEQUENTIAL_EDITS", number, "DEFECT_ROWS", len(rows))
print("IDENTITIES_PRESERVED; SHARED_WRITES0; ADDITIONAL_CHECK_CREDIT0")
