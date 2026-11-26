"""Publication edit of the wholly read vertical-correction unit."""
import csv
from datetime import datetime, timezone
from pathlib import Path

import S6_SERIES_PUBLISH_c8_integrate_presentation as presentation

root = Path(__file__).resolve().parent.parent
path = root / "agents/continuation8_iii_integration/units/weighted/vertical_corrections.tex"
lane = root / "agents/continuation8_iii_weighted_units"
original = path.read_text()
text = original
edits = []


def replace(old, new, kinds, reason, count=1):
    global text
    assert text.count(old) == count, (old[:160], count, text.count(old))
    for _ in range(count):
        start = text.index(old)
        edits.append((kinds, text.count("\n", 0, start) + 1, old, new, reason))
        text = text[:start] + new + text[start + len(old):]


opening_end = original.index("Some such $D$ makes")
replace(original[:opening_end], r"""\begin{definition}[Vertical correction data]\hypertarget{tag-Q202}{}\label{maps:def:vertical-correction-data}
{\normalfont\scriptsize tag Q202}\par
Let $f:S\to\mathbb P^1$ be one of the twenty-one marked rational
elliptic surfaces of \ref{maps:src:D.2.19}, with zero section $O$,
Mordell--Weil group $\mathbb ZG$ and height
$\langle G,G\rangle=1/d_0$.
For integers $a,b$, put $P=aG$ and $Q=bG$.
For an integral divisor $D$ supported on fibre components, define
\[
 M_D=\mathcal O_S(P-O+D),\qquad
 J_D=M_D\otimes T_Q^*M_D^{-1},
\]
where $T_Q:S\to S$ is section translation. A \emph{vertical correction}
is such a divisor $D$ for which $J_D$ is a pullback from the base.
\end{definition}

\begin{theorem}[Vertical corrections and fillings]\hypertarget{tag-02LS}{}\label{maps:src:D.2.50}
{\normalfont\scriptsize tag 02LS}\par
For the data of Definition~\ref{maps:def:vertical-correction-data},
""", "D04;D05;D10;D13;D14;D16", "Put the complete signed-integer input domain in Q202 and retain the single theorem at02LS; replace the production header by small tags. All old identities remain.")
replace("Some such $D$ makes\n$J_D$ the pullback of a base line bundle if and only if\n$d_0\\mid ab$.", "a vertical correction exists precisely when $d_0\\mid ab$.", "D08;D11", "Use the newly defined mathematical term without restating its definition.")
replace("Thus the compatible initial line bundles are not exhausted\nby requiring $P$ or $Q$ narrow at every fibre.\n", "", "D02;D11", "The full divisibility criterion and the actual I4 example prove the wider domain; remove the redundant contrastive summary.")
replace("All corrections are determined by the integral local equations\nbelow, with precisely the invariant component orbit sums as ambiguity.", "The local equation \\eqref{maps:eq:D.VC3} determines every correction;\nits ambiguity is the invariant component-orbit lattice\n\\eqref{maps:eq:D.VC4}.", "D06;D08", "Give the exact existing equation locators for the complete correction lattice.")
replace("\\eqref{maps:eq:D.GI2}. This does not identify its newly permitted original caps.\n\nThere are additional explicitly marked simply connected examples.", "\\eqref{maps:eq:D.GI2}.\n\nThe following OS45 fillings are simply connected.", "D01;D02;D08;D11", "State the proved punctured-family scope and the subsequent actual filling construction directly, with no open-work commentary.")
replace("Use the actual\nvertical corrections specified in the proof.", "Use the\nvertical corrections \\eqref{maps:eq:D.VC10} with the cap origins\nand affine boundary maps defined by the tensor transport in the proof.", "D06;D20;D22;D26", "Keep the exact original coefficient choices together with their transported origin marking; no untransported gluing is identified.")
replace("These are new initial and marked filling data beyond the earlier\nnarrowness condition. Their smooth diffeomorphism classes are not\ninferred from these groups.\n", "", "D01;D02;D11", "The theorem asserts the construction and displayed groups. Remove a chronology claim and a trailing scope disclaimer without adding a smooth-classification claim.")

# Separate the local component coefficients from the global height denominator.
local_start = text.index(r"\item \emph{Actual component maps")
local_end = text.index(r"\item \emph{The punctured tensor")
local_old = text[local_start:local_end]
local_new = local_old
substitutions = [
    ("$(Sz)_i=z_{\\sigma(i)}$", "$(\\mathsf S z)_i=z_{\\sigma(i)}$"),
    ("write $S$ for pullback", "write $\\mathsf S$ for pullback"),
    ("$CS=SC$, $S\\mu=\\mu$, and $S^{-1}=S^t$", "$C\\mathsf S=\\mathsf S C$, $\\mathsf S\\mu=\\mu$, and $\\mathsf S^{-1}=\\mathsf S^t$"),
    ("m=m_P+Cd", "m=m_P+Cz"),
    ("(S-I)Cd=-(S-I)", "(\\mathsf S-I)Cz=-(\\mathsf S-I)"),
    ("$S^{-1}$", "$\\mathsf S^{-1}$"),
    ("$-S^{-1}$", "$-\\mathsf S^{-1}$"),
    ("$-S$", "$-\\mathsf S$"),
    ("$d,d'$", "$z,z'$"),
    ("$C(S-I)(d-d')=0$", "$C(\\mathsf S-I)(z-z')=0$"),
    ("$(S-I)(d-d')=k\\mu$", "$(\\mathsf S-I)(z-z')=k\\mu$"),
    ("d+\\ker(S-I)", "z+\\ker(\\mathsf S-I)"),
    ("under $S$", "under $\\mathsf S$"),
    ("d_q-d_0", "z_q-z_0"),
    ("d_0-d_q", "z_0-z_q"),
    (r"\quad d_0=0,\quad d_i=\sum_{k=1}^{i}r_k.", r"\quad z_0=0,\quad z_i=\sum_{k=1}^{i}r_k."),
    ("$(Cd)_i", "$(Cz)_i"),
    ("coefficient $d_0$", "coefficient $z_0$"),
    ("$m=e_p-e_0+Cd$", "$m=e_p-e_0+Cz$"),
    ("take $d=0$", "take $z=0$"),
    ("and $d=0$ works", "and $z=0$ works"),
    ("Taking $d=e_1$", "Taking $z=e_1$"),
]
for old, new in substitutions:
    assert old in local_new, old
    local_new = local_new.replace(old, new)
local_new = local_new.replace("The degree column of the section line and its correction are", "Write $z_i$ for the coefficient of $C_i$ in $D$. The degree column\nof the section line and its correction are")
replace(local_old, local_new, "D20", "Rename the local component coefficient column d to z by the identity z_i=d_i, with inverse d_i=z_i, and the pullback matrix S to mathsf S by identity. This separates z_0 from the global height denominator d_0 and the matrix from the surface S; every equation and inverse is transported entry by entry.")
replace(r"see \cite[Sections 7, 8 and 11.8, especially pp.32--34 and51--52]{manSS10}.", r"see \cite[author version arXiv:0907.0298v3, Sections 7, 8 and 11.8, pp.32--34 and 51--52]{manSS10}.", "D18;D20", "Bind the locator to the exact author version already read in the admitted primary-source review; these are its printed pages, not unversioned journal page numbers.")
replace("The recorded component coordinates of $G$ are units", "The marked component coordinates of $G$ are units", "D04;D08", "Use the mathematical marking rather than record-status wording.")
replace("Every recorded collision profile retains these marked component", "Every collision profile in \\ref{maps:src:D.2.19} retains these marked component", "D04;D06", "Identify the profile domain by its existing theorem locator.")
replace("The recorded82 pairs $(B,g)$\ngive exactly the stated component orders; the integer preimage\nof that order times $g$ is retained.", "For each marked pair $(B,g)$ this gives the stated component order $h$.\nAn integral preimage of $hg$ is $Vx$, where\n$x_j=h(Ug)_j/D_{jj}$ on the nonzero Smith rows and $x_j=0$\non the zero rows.", "D09;D20;D22", "Replace an archived-record count by the explicit integer preimage supplied by the already stated Smith matrices. D x=h U g proves the map on every profile.")
replace("All signed integers are included by reduction to the component\nresidues. There are227 distinct local pairs and5696 pairs over\nthe21 full residue squares. Their exhaustive integral checks\nretain the actual affine matrices, all Smith maps and inverses,\nall chosen solutions, and the invariant-orbit basis with inverse.\nThe additional positive height-one initial pairs are", "Reduction to the component residues includes every signed integer.\nThe positive height-one pairs for which neither section is narrow\nat every fibre are", "D01;D08;D09", "The proof already constructs all integral local solutions. Move finite execution counts to the review and describe the actual additional-pair table mathematically.")
replace("This table has sixteen initial rows. The sixteen filled spaces\nbelow have a different explicit parameterization: two pairs,\nfour zero positions, and two clutch signs on OS45/default.", "The table gives sixteen choices of profile and initial pair.\nThe OS45/default filling parameter set in the theorem is\n$\\{(2,4),(4,2)\\}\\times\\{1,2,3,4\\}\\times\\{-1,1\\}$,\nwhere the last two coordinates specify the nodal zero position\nand ordinary clutch.", "D04;D20;D22", "State both finite parameter sets directly and give the exact product coordinates of the sixteen filled constructions.")
replace("For general corrections the original-cap multidegrees can be\nnonprimitive or permuted. The present argument makes no\nidentification of those completed caps.\n", "", "D02;D11", "The first theorem clause concerns the punctured family; remove a repeated open-scope disclaimer after the complete actual example.")
replace("When denominators\noccur they are integral maps on the transported lattices, or on\nthe corresponding denominator cover; they are not asserted to be\nautomorphisms of a fixed untransported lattice.", "When denominators\noccur, the domain and range are the transported lattices, equivalently\nthe lattices on the corresponding denominator cover. The displayed\nmatrices are inverse integral maps between those lattices.", "D02;D20", "Give the exact domain and range of the existing inverse maps positively; no fixed-lattice automorphism or cap cover is introduced.")
replace("The ordered raw products, including every defining profile, give", "For each defining profile the ordered product is", "D04;D08", "State the actual ordered identity without record-status wording.")
replace("For the original iterated description, choose $h$ such that $hQ$", "Choose a positive integer $h$ such that $hQ$", "D01;D08;D20", "Introduce the finite period inclusion by its mathematical parameter and preserve its exact telescope.")
replace("parameter. No covering of a completed cap is inferred.", "parameter of the punctured quotient.", "D02;D20", "State the actual domain of the constructed circle map directly.")
replace("The raw defining data, with the raw component convention, are", "The defining matrices and component labels are", "D04;D08", "Introduce the concrete OS45 data without production terminology; the later Tate-label reflection retains the marking convention.")
replace("Retain the following literal raw-component coefficient choices:", "Use the following component coefficients:", "D08", "State the actual selected divisor coefficients directly.")
replace("raw shifts4 and6. No correction is needed at the four irreducible\nfibres. Both height pairings are1.", "shifts $4$ and $6$. At the four irreducible fibres take $D=0$.\nBoth height pairings are $1$.", "D20;D23", "Make the invariant multidegree action and the irreducible-fibre divisor choices explicit with readable mathematical spacing.")
replace("ones by $j\\mapsto-j\\pmod8$", "stated ones by $j\\mapsto-j\\pmod8$", "D08", "Use the retained concrete marking as the reflection's domain.")
replace("d^{\\rm new}_{2,4}", "z^{\\rm Tate}_{2,4}", "D01;D20", "Name the physical coefficient vector by its Tate labeling; the identity renaming and the existing reflection/tensor inverse preserve it.")
replace("d^{\\rm new}_{4,2}", "z^{\\rm Tate}_{4,2}", "D01;D20", "Use the same Tate-frame coefficient notation for the second vector.")
replace("Subtracting these from the reflected original choices gives", "Subtracting these from the reflected choices in \\eqref{maps:eq:D.VC10} gives", "D01;D06", "Replace chronological wording by the exact retained divisor locator.")
replace("The following filling computation applies directly to the choices\n\\eqref{maps:eq:D.VC10} with their specified marking. It does not\nassert an identification obtained by changing $D$ while fixing an\nuntransported affine gluing.", "We now compute the fillings of \\eqref{maps:eq:D.VC10} with these\ncap origins and affine boundary maps.", "D02;D08;D11", "The preceding tensor map and inverse already specify exactly which gluing is transported; state the computation's marked scope once.")
replace("Primitive rank-one cap maps without a coprimality shortcut.", "Rank-one cap maps.", "D02;D16", "Use a mathematical proof-step title; the full Bezout construction remains.")
replace("This calculation uses $\\gcd(a,b)=2$ exactly; a natural-row\ncoprimality formula has not been substituted.", "For both initial pairs, $\\gcd(a,b)=2$; the displayed B\\'ezout\nrelations give the required primitive period bases.", "D02;D08;D22", "State why the explicit period bases work in these actual pairs.")
replace("All maps have\nbeen specified on the actual period coordinates, not only by\ntheir rational ranks.\n", "", "D02;D11", "The explicit matrices, sections and Thom chains already prove this; remove the repeated defensive conclusion.")
replace("The integer computation retains $U,B,V,D_B=UBV$ and\n$U^{-1},V^{-1}$, verifies both inverse products and every\ndivisibility step, and reads all sixteen outputs.", "Write $D_B=UBV$ for the integral Smith reduction, with $U,V$\nunimodular. The resulting quotient map and inverse use\n$U^{-1}$ and $V^{-1}$ as follows.", "D09;D20", "Replace execution history by the exact mathematical Smith maps used in the proof; all finite input choices and factors remain.")
replace("The quotient isomorphism and its inverse are explicitly\n", "", "D11", "Avoid repeating the immediate introduction to the same displayed quotient map.")
replace("For clarity concerning the older retained computation, its\n23 by70 presentation includes six zero ordinary fibre columns\nand five redundant triangular-cap fibre columns. The actual\nfree-group change from", "Taking the ordinary word as the first graph generator and retaining\nall triangular-cap fibre columns gives a $23\\times70$ presentation\n$B_o$. It has six zero ordinary fibre columns and five redundant\ntriangular-cap fibre columns. The free-group change from", "D01;D04;D08;D20", "Retain the complete 70/59 comparison as a mathematical change of graph generators and relation columns, named by ordinary-first versus singular-first bases.")
replace("has the inverse words specified\nabove.", "has inverse word $\\theta_4=(\\theta_o\\theta_0\\cdots\\theta_3)^{-1}$.", "D06;D20;D22", "Write the exact inverse word at its point of use; it follows by cancellation from theta_o=(theta_0...theta_4)^(-1).")
replace(r"D_{\rm new}J=D_{\rm old}", r"D_sJ=D_o", "D01;D20", "Rename singular-first and ordinary-first boundary rows by s and o, with the same actual graph map J.")
replace(r"K_{\rm old}", "K_o", "D01;D20", "Use the ordinary-first primitive kernel basis name; all entries and maps stay fixed.", count=5)
replace(r"K_{\rm new}", "K_s", "D01;D20", "Use the singular-first primitive kernel basis name; all entries and maps stay fixed.", count=3)
replace("The two composites cancel term by term, and the ordered product\nidentity gives $D_sJ=D_o$.", "The two composites cancel term by term. Let $D_o,D_s$ denote the\nboundary maps in the ordinary-first and singular-first graph bases.\nThe ordered product identity gives $D_sJ=D_o$.", "D20;D22", "Define the two renamed boundary rows before using their intertwining identity.")
replace("and $E_o$ selects the old ordinary block.", "and $E_o$ selects the ordinary block in the ordinary-first basis.", "D01;D20", "Identify the exact block selector by its geometric graph basis.")
replace("Both are integral. The retained comparison supplies exact\nrelation maps $B C=M B_{\\rm old}$ and\n$B_{\\rm old}D=M^{-1}B$, proving equality of the marked\nquotients and explaining the relation count. The chosen proof\nof the groups is the59-column computation just given.", "Both are integral. Applying the bar lift to these words and\nincluding the zero and redundant fibre columns gives integral\nrelation matrices $C_r,D_r$ with\n$B C_r=M B_o$ and $B_oD_r=M^{-1}B$. These identities make\nthe quotient maps induced by $M$ and $M^{-1}$ well-defined\nand inverse. The $59$-column presentation above therefore computes\nthe same marked quotient in the singular-first graph basis.", "D01;D02;D09;D20;D22", "Keep both integral relation inclusions and the exact inverse quotient conclusion, with constructive word/column origins instead of historical-comparison prose. Do not assert inverses between free relation modules of unequal ranks.")
replace("Changing all five peripheral row and disc signs gives the\nprinted computational matrix with first column $(e,1,1,1,1,1)$;", "Changing all five peripheral row and disc signs gives the\nmatrix with first column $(e,1,1,1,1,1)$;", "D04;D09", "The sign involution is mathematical; remove the printed-output descriptor.")
replace("Equivalently, the literal finite-first exterior matrix has\n$H_1=\\mathbb Z^5$ and there are five whole-fibre component\nclasses, but the inverse above proves the full integral claim.\n", "", "D11;D12", "The complete six-disc inverse immediately proves the vanishing relative kernel. The finite-first rank check is redundant checking evidence, retained in the admitted comparison.")
replace("Their nongamma coordinates have a retained integer right inverse", "Their nongamma coordinates have an integer right inverse", "D08;D09", "State the integral right-inverse result without storage vocabulary.")
replace("The remaining homology and the computation scope.", "The remaining homology.", "D09;D16", "Keep the final proof step mathematical; computational attribution moves to the separate review and program-table proposals.")
tail_start = text.index("The complete fresh calculation is retained in")
tail_end = text.index(r"\end{enumerate}", tail_start)
replace(text[tail_start:tail_end], "", "D01;D02;D07;D09;D11", "Move all four code paths, execution counts, output-reading history and scope disclaimers to the review/program records. The complete cap, bar, relative, group and duality proof already precedes this paragraph.")
replace("\n\n\n\\begin{proof}", "\n\n\\begin{proof}", "D23", "Remove an extraction-only blank line between the theorem and its proof.")
replace("\\end{proof}\n\n\n", "\\end{proof}\n", "D23", "Remove extraction-only trailing blank lines.")

candidate, changes, issues = presentation.statement_records_to_small_tags(text)
assert not changes and not issues
candidate, changes, issues, aliases = presentation.remove_manual_equation_tags(candidate)
assert not issues
for change in changes:
    edits.append(("D19", change.line, change.old, change.new, change.reason))
assert not presentation.unresolved_literal_equation_references(candidate, aliases)
presentation.units.check_permanent_identifiers(original, candidate,
    allowed_labels=("maps:def:vertical-correction-data",), allowed_targets=("tag-Q202",))
assert candidate.count(r"\begin{definition}") == 1
assert candidate.count(r"\begin{theorem}") == candidate.count(r"\begin{proof}") == 1
assert "\r" not in candidate
fields = ["change_id", "type", "statement_id", "old_location", "old_page", "new_location", "new_page", "old_text", "new_text", "reason", "review_status"]
records = []
for number, (kinds, line, old, new, reason) in enumerate(edits, 1):
    for kind in kinds.split(";"):
        records.append([f"III-C8-LS-PUB-{number:03}-{kind}", kind, "maps:src:D.2.50",
            f"vertical_corrections.tex, sequential edit at line {line}", "pending page concordance",
            "weighted/vertical_corrections.tex", "pending final build", old, new, reason,
            "source edit; whole publication readback and root admission pending"])
with (lane / "S6_SERIES_PUBLISH_LS_publication_defects.tsv").open("w", newline="") as stream:
    writer = csv.writer(stream, delimiter="\t", lineterminator="\n")
    writer.writerow(fields)
    writer.writerows(records)
path.write_text(candidate, newline="\n")
print("UTC", datetime.now(timezone.utc).isoformat())
print("UNIT_LINES", len(original.splitlines()), "->", len(candidate.splitlines()))
print("SEQUENTIAL_EDITS", len(edits), "DEFECT_ROWS", len(records), "NEW_ID", "Q202 / maps:def:vertical-correction-data")
print("ALL_OLD_IDENTIFIERS_PRESERVED; D19_HELPER_EDITS", len(changes), "UNRESOLVED0")
print("SHARED_WRITES0; AUTOMATIC_CRITERION_CREDIT0; INDEPENDENT_CHECK_CREDIT0")
