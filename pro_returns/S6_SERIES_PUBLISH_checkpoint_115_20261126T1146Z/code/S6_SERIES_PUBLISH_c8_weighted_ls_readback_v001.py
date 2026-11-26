"""Exact mathematical and typography edits after the whole LS readback."""
import csv
from datetime import datetime, timezone
from pathlib import Path
import S6_SERIES_PUBLISH_c8_integrate_units as units

root = Path(__file__).resolve().parent.parent
lane = root / "agents/continuation8_iii_weighted_units"
path = root / "agents/continuation8_iii_integration/units/weighted/vertical_corrections.tex"
old = path.read_text()
text = old
table = lane / "S6_SERIES_PUBLISH_LS_publication_defects.tsv"
with table.open(newline="") as stream:
    reader = csv.DictReader(stream, delimiter="\t")
    fields = reader.fieldnames
    rows = list(reader)
number = max(int(row["change_id"].split("-")[-2]) for row in rows)
edits = [
    ("Its basis consists of the literal sums", "The kernel has the basis consisting of the sums", "D20", "The displayed solution set is an affine translate; its underlying invariant kernel has the orbit-sum basis."),
    ("For orders2 and3", "For orders $2$ and $3$", "D23", "Separate the two mathematical component orders from the surrounding text."),
    ("where $r=5$ or7.", "where $r=5$ or $7$.", "D23", "Typeset both root-rank values in math mode."),
    ("The multiplicities are1 on the four leaves and2 on the chain.", "The multiplicities are $1$ on the four leaves and $2$ on the chain.", "D23", "Separate the actual multiplicities from their prose."),
    ("translation by class2", "translation by class $2$", "D23", "Typeset the component class."),
    ("Thus the physical pairs are", "Thus the pairs in the Tate labels are", "D20", "Name the target convention of the actual reflection F explicitly."),
    ("gives the physical choices", "gives the Tate coefficient choices", "D20", "Use the same explicit frame name for the computed divisor coefficients."),
    ("invariant under shifts4 and2 respectively.", "invariant under shifts $4$ and $2$, respectively.", "D23", "Typeset the two exact shift integers."),
    ("determinant1", "determinant $1$", "D23", "Separate the determinant value from its prose."),
    ("where $f$ is0\nnear one pole and1 near the other", "where $f$ is $0$\nnear one pole and $1$ near the other", "D23", "Typeset the endpoint values of the actual pole-translation isotopy."),
    ("characteristic0", "characteristic $0$", "D23", "Separate the Euler characteristic value from its prose."),
    ("vertices contribute2, so this cap has Euler characteristic2.", "vertices contribute $2$, so this cap has Euler characteristic $2$.", "D23", "Typeset both Euler contributions."),
    ("lattice and the origin disc fixes its affine lift. \n\\item", "lattice and the origin disc fixes its affine lift.\n\n\\item", "D23", "Restore a paragraph break before the next proof step after deletion of redundant commentary."),
    ("of rank17. If $U_DDV_D$ is its tracked Smith form, columns4\nthrough20", "of rank $17$. If $U_DDV_D$ is its Smith form, columns $4$\nthrough $20$", "D09;D23", "These are mathematical basis coordinates of the Smith transformation, not saved-array indices; format them and remove the execution adjective."),
    ("fifth modulo2", "fifth modulo $2$", "D23", "Typeset the torsion coefficient modulus."),
    ("where $J_i$ inserts $u$ in the $i$-th graph block. There is no\nsecond subtraction of $z(k)$. This specifies the full integral", "where $J_i$ inserts $u$ in the $i$-th graph block. The displayed\n$f_{T_i}(u)$ already includes the polygon correction. This specifies the integral", "D02;D20", "State positively how the exact fixed-normal coordinates use the proved bar splitting; retain the order-two fibre class."),
    ("the same correction: the difference has its retained integral\npreimage under $R$.", "the same correction modulo $\\operatorname{im}R$: the signed\ncentral group law expresses the difference as a sum of columns of $R$.", "D08;D09;D22", "Identify the mathematical reason for the integral relation instead of storage vocabulary."),
    ("of its meridian, not by a rank substitution.", "of its meridian.", "D02", "The displayed boundary map and Thom construction already prove the sign and columns."),
    ("Use six free fibre coordinates and17 graph coordinates. The\nfull matrix $B$ has23 rows and59 columns, in this exact order:\nthe30 columns of $R$, the ten cap fibre-kernel columns, the14", "Use six free fibre coordinates and $17$ graph coordinates. The\nmatrix $B$ has $23$ rows and $59$ columns, ordered as follows:\nthe $30$ columns of $R$, the ten cap fibre-kernel columns, the $14$", "D08;D23", "Typeset the exact presentation sizes and state the mathematical column order directly."),
    ("from the displayed raw\nmatrices", "from the matrices in \\eqref{maps:eq:D.VC9}", "D04;D06", "Point directly to the actual five monodromy matrices."),
    ("On the23 generators", "On the $23$ generators", "D23", "Typeset the exact ambient generator count."),
    ("triangular cap contributes2", "triangular cap contributes $2$", "D23", "Typeset the final nonzero Euler contribution."),
]
for before, after, kinds, reason in edits:
    assert before in text, before
    while before in text:
        at = text.index(before)
        number += 1
        for kind in kinds.split(";"):
            rows.append(dict(zip(fields, [f"III-C8-LS-PUB-{number:03}-{kind}", kind, "maps:src:D.2.50",
                f"vertical_corrections.tex, readback edit at line {text.count(chr(10), 0, at)+1}", "pending page concordance",
                "weighted/vertical_corrections.tex", "pending final build", before, after, reason,
                "whole source read; root admission and global integration pending"])))
        text = text[:at] + after + text[at + len(before):]
units.check_permanent_identifiers(old, text)
assert "\r" not in text
path.write_text(text, newline="\n")
with table.open("w", newline="") as stream:
    writer = csv.DictWriter(stream, fieldnames=fields, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
print("UTC", datetime.now(timezone.utc).isoformat())
print("LS_LINES", len(old.splitlines()), "->", len(text.splitlines()), "SEQUENTIAL_EDITS", number, "DEFECT_ROWS", len(rows))
print("IDENTITIES_PRESERVED; SHARED_WRITES0; ADDITIONAL_CHECK_CREDIT0")
