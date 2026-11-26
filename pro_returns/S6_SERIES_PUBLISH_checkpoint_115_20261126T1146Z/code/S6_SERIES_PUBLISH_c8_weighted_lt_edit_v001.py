"""Publication edit of the wholly read invariant-Chern cap unit."""
import csv
import re
from datetime import datetime, timezone
from pathlib import Path
import S6_SERIES_PUBLISH_c8_integrate_presentation as presentation

root = Path(__file__).resolve().parent.parent
path = root / "agents/continuation8_iii_integration/units/weighted/invariant_chern_caps.tex"
lane = root / "agents/continuation8_iii_weighted_units"
original = path.read_text()
text = original
edits = []


def replace(old, new, kinds, reason, count=1):
    global text
    assert text.count(old) == count, (old[:160], count, text.count(old))
    for _ in range(count):
        at = text.index(old)
        edits.append((kinds, text.count("\n", 0, at) + 1, old, new, reason))
        text = text[:at] + new + text[at+len(old):]


replace(r"""\begin{theorem}[invariant-Chern additive caps]\hypertarget{tag-02LT}{}\label{maps:src:D.2.51}
\textnormal{\small tag 02LT.}


Let $K$ be the reduced central fibre of an original additive
Kodaira neighbourhood, of type
""", r"""\subsection{Invariant-Chern additive caps}

\begin{definition}[Invariant-Chern cap data]\hypertarget{tag-Q203}{}\label{maps:def:invariant-chern-data}
{\normalfont\scriptsize tag Q203}\par
Let $K$ be the reduced central fibre of an original additive
Kodaira neighbourhood with its line bundle $M$, section $Q$
and original six-dimensional cap $U$. The fibre type is
""", "D05;D10;D13;D14;D16", "Give the publication unit its descriptive subsection and place the complete actual cap input before the single theorem. Q203 adds no restriction on the given original line arrow.")
replace("Let the original line bundle have invariant component degrees\n$c_i$, so that", "The component degrees $c_i$ of $M$ satisfy", "D08;D11", "Use the line bundle just named in the input definition.")
replace("These include every corrected line bundle in \\ref{maps:src:D.2.50}.\nLet the component orbits be $O_1,\\ldots,O_\\rho$, with\nlengths $l_j$ and common degrees $c_j$ on $O_j$.", "The corrected line bundles of \\ref{maps:src:D.2.50} give these\ndata at the listed additive fibres. Let the component orbits be\n$O_1,\\ldots,O_\\rho$, with lengths $l_j$, common degrees $c_j$\nand common multiplicities $\\mu_j$ on $O_j$.", "D20;D26", "Make the existing additive-fibre domain explicit and define the orbit multiplicity used in IC6. Translation preserves the multiplicity column; no subset of the stated additive types or invariant degrees is removed.")
replace("where both gcds are positive. For the resulting original\nsix-dimensional cap $U$, there is an exact integral cellular\ncone, with its actual circle-fibre and regular-area classes,", "where both gcds are positive. These are the \\emph{invariant-Chern\ncap data}.\n\\end{definition}\n\n\\begin{theorem}[Invariant-Chern additive caps]\\hypertarget{tag-02LT}{}\\label{maps:src:D.2.51}\n{\\normalfont\\scriptsize tag 02LT}\\par\nThe cap $U$ of Definition~\\ref{maps:def:invariant-chern-data} has\nthe following integral cellular cone, with its scalar-circle and\nregular-area classes:", "D10;D13;D14;D16", "Retain the single realization and homology theorem at02LT after its actual input, moving IC1/IC2 with their unchanged labels and targets into Q203.")
replace("and a positive long circle $\\gamma$. In particular", "and a positive long circle $\\gamma$. For $c\\ne0$,", "D20", "Specify the already intended nonzero-degree branch of the g,h homology table.")
replace(r"\emph{all} of the cyclic torsion", "the cyclic torsion", "D08", "The complete generator statement is precise without emphasis.")
replace("If $h=1$, these facts determine the complete marked\nlocal kernels.", "In the sector $c\\ne0$, $h=1$, the complete marked local kernels\nare as follows.", "D20;D26", "Expose the exact marked-kernel sector; h was defined only for nonzero c, so this is the same range and does not absorb the separate zero-Chern branch.")
replace("where the six coordinates have their usual increasing\nexterior order.", "where the six coordinates are ordered as\n$(12,13,14,23,24,34)$ in that basis.", "D20", "State the actual exterior-coordinate order of the kernel row.")
replace("For $h>1$, the cone determines a torsion coordinate from the\ncellular representative of a marked torus. The individual torsion\ncoordinates of the two mixed elliptic--long tori and the second\nfixed-normal torus require those representatives. The image and\ncokernel assertions above hold for every invariant degree vector;\nthe complete marked-kernel assertion is in the sector $h=1$.", "For $h>1$, the torsion coordinate of a specified cellular\nrepresentative is given by \\eqref{maps:eq:IC_local_15}. This\nrepresentative includes the line-frame contributions of the mixed\nelliptic--long and fixed-normal tori. The image and cokernel formulas\napply to every invariant degree vector; the marked kernels\n\\eqref{maps:eq:D.IC7} apply in the sector $h=1$.", "D02;D06;D20;D26", "Replace a requirement/status sentence by the exact cellular-coordinate formula while preserving its representative dependence and the h=1 marked-kernel scope.")

# These are steps of the sole proof; their equation identities all remain.
headings = re.findall(r"\\paragraph\{([^{}]+)\}", text)
assert len(headings) == 13, headings
for heading in headings:
    title = heading
    if title == "Explicit integer completions used below.":
        title = "Integral bases and their inverses."
    if title == "The actual long cover and the free component image of the fibre.":
        title = "The long cover and the component image."
    if title == "Full fibre image, full boundary image, and their inverse quotients.":
        title = "Fibre and boundary images."
    if title == "Orbit maps and an explicit inverse to the augmentation kernel.":
        title = "Orbit maps and the augmentation kernel."
    if title == "Complete $H_2$ quotient and its two inverse identities.":
        title = "$H_2$ and its quotient maps."
    replace("\\paragraph{" + heading + "}", "\\item \\emph{" + title + "}", "D13;D16", "Use a numbered step within the single proof, with a mathematical title. All displayed maps and local equation labels remain at their proof loci.")
replace("positive roof direction; the scalar circle has its complex orientation.\n\\item", "positive roof direction; the scalar circle has its complex orientation.\n\\begin{enumerate}\n\\item", "D13", "Open the ordered proof steps after fixing the common return and circle conventions.")
replace("\\end{proof}\n\n\n", "\\end{enumerate}\n\\end{proof}\n", "D13;D23", "Close the proof steps and remove extraction-only trailing blank lines.")
replace("\n\n\n\\begin{proof}", "\n\n\\begin{proof}", "D23", "Remove the extraction-only blank line between theorem and proof.")
replace("These maps identify the cap, up to homotopy with its marked cell maps,", "The displayed homotopy inverses identify the cap, with its marked cell maps,", "D08;D20", "Point to the actual homotopy maps rather than leaving the equivalence's scope implicit.")
replace("For clarity, the resulting statement about the kernel is constructive.\nGiven an integral fixed class,", "For an integral fixed class,", "D08;D11", "Introduce the actual lift directly; its scalar subtraction and unchanged Wang projection provide the proof.")
replace("We now check the full boundary for the whole invariant-Chern scope.", "To compute the boundary image for every invariant degree vector,", "D08", "Use a direct mathematical lead for the complete boundary calculation.")
replace("To compute the boundary image for every invariant degree vector,\nForget the scalar circle", "To compute the boundary image for every invariant degree vector,\nforget the scalar circle", "D23", "Join the revised sentence grammatically.")
replace("The integer or residue $b$ is read from the specified cellular\nrepresentative; these choices retain all line-frame contributions.\n\n", "", "D11", "The preceding paragraph already reads b from the explicit formula and the prior paragraph retains every frame prism; remove the repeated conclusion.")
replace("Here $g=1$, $t=0$, and $H_2(U)=\\ker d^t$ is free.\nTherefore \\eqref{maps:eq:IC_local_39} is the complete fibre map, not just its component\nprojection. Its kernel is precisely\n\\begin{equation}\n \\ker\\bigl(q_0(1,0,z_2,0,-z_1,0):\n                         \\mathbb Z^6\\to\\mathbb Z\\bigr).\n \\label{maps:eq:IC_local_45}\n\\end{equation}\nApply \\eqref{maps:eq:IC_local_31} to this six-entry primitive row.", "Here $g=1$, the homology class $t$ is zero, and\n$H_2(U)=\\ker d^t$ is free. Formula~\\eqref{maps:eq:IC_local_39}\ntherefore gives the complete fibre map\n\\begin{equation}\n F_2:\\mathbb Z^6\\longrightarrow\\ker d^t,\\qquad\n F_2(y)=q_0(y_{12}+z_2y_{14}-z_1y_{24})\\,w.\n \\label{maps:eq:IC_local_45}\n\\end{equation}\nThe vector $w$ is primitive, so its integral span embeds in\n$\\ker d^t$ with inverse given by the first coordinate of $L^{-1}$.\nThus $\\ker F_2$ is exactly \\eqref{maps:eq:D.IC7}.\nApply \\eqref{maps:eq:IC_local_31} to its six-entry primitive row.", "D02;D11;D12;D20;D22", "Replace the repeated kernel display by the actual complete map at its retained local identity. The map Z→Zw, n→nw, has inverse the first coordinate of L inverse, proving that its kernel is exactly the single theorem row IC7. Distinguish the vanishing homology class t from the later chain coordinate t.")
replace("fibre kernel \\eqref{maps:eq:IC_local_45}, these give", "kernel of the fibre map \\eqref{maps:eq:IC_local_45}, these give", "D06;D20", "Update the local reference to the retained equation's full-map form; its kernel is proved immediately there.")
replace("Order the new components by the following new-to-old map:", "Pass from the chain order to the outer-components-first order\nby the index map", "D01;D20", "Name the two actual component orders geometrically. The given permutation and inverse remain.")
replace("Reading \\eqref{maps:eq:IC_local_47} through this permutation gives\n\\begin{equation}\n \\begin{array}{c|c}\n I_1^*&(1,1,0,0,-1,0),\\\\\n I_3^*&(1,1,0,0,-1,0,0,0).\n \\end{array}\n \\label{maps:eq:IC_local_49}\n\\end{equation}\nThe new permutation is", "Let $\\mathsf P e_k=e_{p(k)}$ map outer-first coordinates to\nchain coordinates. With $c_{\\rm ch}$ as in\n\\eqref{maps:eq:IC_local_47}, the degree and return maps are\n\\begin{equation}\n c_{\\rm out}=\\mathsf P^{-1}c_{\\rm ch},\\qquad\n \\sigma_{\\rm out}=\\mathsf P^{-1}\\sigma_{\\rm ch}\\mathsf P,\\qquad\n \\mathsf P^{-1}=\\mathsf P^t.\n \\label{maps:eq:IC_local_49}\n\\end{equation}\nThese give the two degree vectors in \\eqref{maps:eq:D.IC8}.\nThe outer-first permutation is", "D01;D11;D12;D20;D22", "Replace the duplicate degree table by its exact coordinate and return transport, with inverse. Applying the displayed p to e0+e1−e2 gives the theorem's unchanged star vectors, whose permanent IC8 identity stays at the single table.")
replace("Thus the splitting behaviour is determined by the stated\ninteger criterion, while the homology groups are always as displayed.\n", "", "D11", "The exact two extension sequences, splitting maps and both concrete examples already establish this conclusion.")

candidate, changes, issues = presentation.statement_records_to_small_tags(text)
assert not changes and not issues
candidate, changes, issues, aliases = presentation.remove_manual_equation_tags(candidate)
assert not changes and not issues
assert not presentation.unresolved_literal_equation_references(candidate, aliases)
presentation.units.check_permanent_identifiers(original, candidate,
    allowed_labels=("maps:def:invariant-chern-data",), allowed_targets=("tag-Q203",))
assert candidate.count(r"\begin{definition}") == 1
assert candidate.count(r"\begin{theorem}") == candidate.count(r"\begin{proof}") == 1
assert candidate.count(r"\begin{enumerate}") == candidate.count(r"\end{enumerate}") == 1
assert "\r" not in candidate
fields = ["change_id", "type", "statement_id", "old_location", "old_page", "new_location", "new_page", "old_text", "new_text", "reason", "review_status"]
rows = []
for number, (kinds, line, old, new, reason) in enumerate(edits, 1):
    for kind in kinds.split(";"):
        rows.append([f"III-C8-LT-PUB-{number:03}-{kind}", kind, "maps:src:D.2.51",
            f"invariant_chern_caps.tex, sequential edit at line {line}", "pending page concordance",
            "weighted/invariant_chern_caps.tex", "pending final build", old, new, reason,
            "source edit; whole publication readback and root admission pending"])
with (lane / "S6_SERIES_PUBLISH_LT_publication_defects.tsv").open("w", newline="") as stream:
    writer = csv.writer(stream, delimiter="\t", lineterminator="\n")
    writer.writerow(fields)
    writer.writerows(rows)
path.write_text(candidate, newline="\n")
print("UTC", datetime.now(timezone.utc).isoformat())
print("LT_LINES", len(original.splitlines()), "->", len(candidate.splitlines()), "SEQUENTIAL_EDITS", len(edits), "DEFECT_ROWS", len(rows))
print("NEW_ID Q203 / maps:def:invariant-chern-data; OLD_IDENTIFIERS_PRESERVED; HELPERS0; UNRESOLVED0")
print("SHARED_WRITES0; AUTOMATIC_CRITERION_CREDIT0; INDEPENDENT_CHECK_CREDIT0")
