"""Exact corrections after the complete 3146-line minimal-unit readback."""
import csv
from datetime import datetime, timezone
import hashlib
from pathlib import Path
import re
import S6_SERIES_PUBLISH_c8_integrate_units as units

root = Path(__file__).resolve().parent.parent
path = root / "agents/continuation8_iii_integration/units/weighted/minimal_primary_types.tex"
lane = root / "agents/continuation8_iii_weighted_units"
original = path.read_text()
assert len(original.splitlines()) == 3146
text = original
edits = []
numbers = {"LB": "35", "LC": "36", "LE": "38"}

def replace(unit, old, new, kinds, reason, count=1):
    global text
    assert text.count(old) == count, (unit, old[:160], count, text.count(old))
    for _ in range(count):
        at = text.index(old)
        edits.append((unit, kinds, text.count("\n", 0, at)+1, old, new, reason))
        text = text[:at] + new + text[at+len(old):]

def scoped(unit, start, stop, transform, kinds, reason):
    a = text.index(start)
    b = text.index(stop, a)
    old = text[a:b]
    new = transform(old)
    assert old != new
    replace(unit, old, new, kinds, reason)

replace("LE", r"\gamma_3\eqref{maps:eq:MP_local_1}", r"\gamma_3(1)",
        "D19;D20", "Restore the two mathematical arguments misparsed by this publication editor as literal equation references. Full readback caught both before admission; the receiving proof was correct. There are57 actual reference conversions, not59.", 2)
replace("LB", "listed in the pattern. The selected zero's cocycle is", "listed in the pattern. At a finite site of linear monodromy order\n$d_i$, take $m=d_i k$ with $k>0$, and any free affine lift.\nThe ordinary clutch parameter is $e\\in\\mathbb Z$. The selected zero's cocycle is",
        "D04;D05;D26", "Spell out the complete parameter domain already proved by the finite-cap and Seifert calculations.")
replace("LE", "exactly the listed additive sites. Allow every positive finite\nmultiplicity and every free affine twist.", "exactly the listed additive sites. At a finite site of linear\nmonodromy order $d_i$, allow every multiplicity $m=d_i k$, $k>0$,\nand every free affine twist. The ordinary parameter is $e\\in\\mathbb Z$.",
        "D04;D05;D26", "State the actual allowed multiples and unrestricted ordinary clutch, without enlarging or reducing the admitted domain.")
replace("LB", "If the generator height is\n$1/d$,", "Write the generator height as\n$1/d$;", "D04;D22", "Name the actual input height used in the following equations.")

def lb_matrix(block):
    block = block.replace("SC", "SC_0")
    return re.sub(r"(?<![A-Za-z_])C(?![A-Za-z0-9_])", "C_0", block)
scoped("LB", " C=\\begin{pmatrix}\\nu", "At rank one write the valuation columns as", lb_matrix,
       "D20", "Reserve C for the fixed curve and call its previously displayed cusp matrix C0 throughout this matrix-only span. C0 inverse and every coordinate identity are unchanged; SC becomes SC0.")
replace("LB", r"$d=C^{-1}\delta=(-b\kappa,\nu)$", r"$d_\delta=C_0^{-1}\delta=(-b\kappa,\nu)$", "D20", "Separate the physical scalar vector from the height denominator, using the same exact matrix inverse.")
replace("LB", r"\epsilon^td/2", r"\epsilon^td_\delta/2", "D20", "Use the declared scalar vector in its Gaussian phase.", 2)
replace("LB", "+md\n       =(K_{11}d_1+K_{22}d_2)/2", "+m d_\\delta\n       =(K_{11}(d_\\delta)_1+K_{22}(d_\\delta)_2)/2", "D20", "Use the scalar vector consistently in the exact character pairing.")
replace("LB", " d=(-2,1),\\qquad m=(3,13).", " d_\\delta=(-2,1),\\qquad m=(3,13).", "D20", "Keep the example in the same declared vector notation.")
scoped("LB", "Here are the global line and its explicit comparison", r"\subsubsection{Orders five and seven}",
       lambda s: s.replace("Q(", r"\mathcal Q(").replace("preserves $Q$", r"preserves $\mathcal Q$"),
       "D20", "Name the quadratic refinement mathcal Q, leaving the section Q=bG unchanged; all values and factors agree term by term.")
replace("LB", "F_{r-1}", "F_{r_B-1}", "D20", "Separate the unfilled-disc count from the primitive long vector r.", 2)
replace("LB", "where $r$ counts", "where $r_B$ counts", "D20", "Define the distinct disc-count symbol.")
replace("LB", "Here $r=1$ or $2$.", "Here $r_B=1$ or $2$.", "D20", "Use the declared disc count.")
replace("LB", "$N-(N-r)=r=b_1(W)$", "$N-(N-r_B)=r_B=b_1(W)$", "D20", "Retain the exact rank calculation with its distinct disc-count variable.")

replace("LC", "$\\kappa_i$ in part 1", "$\\kappa_i$ in the ordered input", "D06;D19", "Point to the actual ordered cocycle instead of a brittle proof-step number.")
replace("LC", "Each coefficient is a unit, and evaluation of its inverse on", "Each coefficient multiplying $s$ in the first column is a unit,\nand evaluation of its inverse on", "D20;D22", "Identify the marking coefficients; the displayed refined-invariant coefficients can be zero.")
replace("LC", "period with determinant one. Let $\\tau_E,\\zeta_G,\\rho_L$ be the\nlogarithms of the elliptic period, the point $G$, and the forward\nline multiplier.", "period with determinant one. For its short period $\\omega_s$ and\nlong period $\\omega_l$, put $\\tau_E=\\omega_l/\\omega_s$ and\n$\\zeta_G=G_{\\rm lift}/\\omega_s$. Let $\\rho_L$ be the logarithm\nof the forward line multiplier in this period coordinate.",
        "D20;D22;D27", "Give the exact period and section-lift division used by the theta formula, together with the inverse multiplication already displayed.")
scoped("LC", "On the real period cover define\n", r"\item \emph{Nodal extension", lambda s:s.replace("(x,z)", r"(x,\zeta_R)").replace("(T_i x,z)", r"(T_i x,\zeta_R)").replace("(\\lambda,x)}z)", r"(\lambda,x)}\zeta_R)").replace("(\\tau,x)}z)", r"(\tau,x)}\zeta_R)"),
       "D20", "Reserve physical z for the multiplicative coordinate and name the real prequantum fibre coordinate zeta_R; all forward and inverse line maps are the same.")
replace("LC", r"$z_\sigma=\chi^{m_\sigma}z$; the opposite exponents give", r"$\zeta_\sigma=\chi^{m_\sigma}\zeta_C$, with inverse $\zeta_C=\chi^{-m_\sigma}\zeta_\sigma$; the opposite exponents give", "D20;D27", "Name the line coordinate independently of physical z and display its reciprocal inverse.")
replace("LC", "F_t", "F_{r_Y}", "D20", "Separate the free-group rank from the subsequent Borel character.")
replace("LC", r"\qquad t=0\ \text{or }1.", r"\qquad r_Y=0\ \text{or }1.", "D20", "Use the declared free-group rank.")

replace("LE", "Exhaustion from the raw defining profiles.", "Exhaustion of minimal fillings.", "D08;D16", "Use a descriptive mathematical proof heading.")
replace("LE", "In raw component coordinates", "In the marked component coordinates", "D08;D22", "Identify the actual retained component marking.")
replace("LE", "F_h", "F_{r_B}", "D20", "Separate the free-group rank from the deck transformation h.", 2)
replace("LE", r"\qquad h=0\text{ or }1.", r"\qquad r_B=0\text{ or }1.", "D20", "Use the declared free-group rank.")
scoped("LE", " J_\\lambda(x,z)=", "Its commutator with", lambda s:s.replace("(x,z)", r"(x,\zeta_R)").replace("(T_i x,z)", r"(T_i x,\zeta_R)").replace("(\\lambda,x)}z)", r"(\lambda,x)}\zeta_R)").replace("(\\tau,x)}z)", r"(\tau,x)}\zeta_R)"),
       "D20", "Name the real prequantum line coordinate zeta_R, retaining the same matrix, lattice and scalar lifts and their inverses.")
replace("LE", "The total line character is\n", "Write $d_\\delta=(d_1,d_2)^t$. The total line character is\n", "D20", "Define the displayed scalar-vector components before their character pairing.")
replace("LE", "choose integers $t,\\sigma,x,y$", "choose integers $\\theta_N,\\sigma,x,y$", "D20", "Separate the nodal Bezout coefficient from the cubic-model index and Borel character.")
replace("LE", " n_0t+A_0\\sigma=1", " n_0\\theta_N+A_0\\sigma=1", "D20", "Use the nodal Bezout coefficient.")
replace("LE", r"-A_0&t\end{pmatrix}", r"-A_0&\theta_N\end{pmatrix}", "D20", "Use the same Bezout coefficient in the primitive matrix.")
replace("LE", r"C_S^{-1}=\begin{pmatrix}t&-\sigma", r"C_S^{-1}=\begin{pmatrix}\theta_N&-\sigma", "D20", "Use the same coefficient in its exact inverse.")
replace("LE", "$2t+a\\kappa\\sigma=1$", "$2\\theta_N+a\\kappa\\sigma=1$", "D20", "Use the same nodal Bezout identity in the I2 specialization.")
replace("LE", "Choose the unimodular short matrix with first column $v_0$.\nThe difference from the Gaussian support is the integral linear form\n$(a\\operatorname{row}_1B-\\epsilon_N^t)/2$.", "Take $B_S=C_S$, whose first column is\n$v_0=(n_0,-A_0)^t$ and whose inverse is displayed in\n\\eqref{maps:eq:MP_local_46}. The difference from the Gaussian\nsupport is the integral linear form\n$(a\\operatorname{row}_1B_S-\\epsilon_N^t)/2$.",
        "D20;D22;D27", "Bind the previously unnamed primitive matrix to the actual displayed nodal basis and its inverse; B elsewhere denotes a real long coordinate.")
replace("LE", "The square of \\eqref{maps:eq:MP_local_39} differs from it", "The tensor-square support $2\\psi(v)$ from\n\\eqref{maps:eq:MP_local_39} differs from it", "D20;D22", "Specify additive support under tensor product, rather than suggesting the polynomial square psi(v)^2.")
replace("LE", r"$t\in H^2(BC_p;\mathbb F_p)$", r"$t_p\in H^2(BC_p;\mathbb F_p)$", "D20", "Reserve t for the order-two model index and name the odd Borel character tp.")
replace("LE", "$-\\lambda^2t^2$", "$-\\lambda^2t_p^2$", "D20", "Use the declared odd Borel character in its Euler class.")
replace("LE", "inverting $t$. The same free-complement", "inverting $t_p$. The same free-complement", "D20", "Use the same character in localization.")
replace("LE", "$x_1+\\lambda t,x_2-\\lambda t$", "$x_1+\\lambda t_p,x_2-\\lambda t_p$", "D20", "Use the same Borel character in both eigenroots.")
replace("LE", "$2\\lambda^2t^2+2\\lambda t(x_1-x_2)$", "$2\\lambda^2t_p^2+2\\lambda t_p(x_1-x_2)$", "D20", "Keep the exact Pontryagin/Euler identity in one Borel variable.")
replace("LE", "Here $\\Omega^{\\mathrm{Spin}}_6(\\mathrm{pt})=0$, also a consequence\nof the injective pair $(P,h)$ for coefficient group zero.", "Here $\\Omega^{\\mathrm{Spin}}_6(\\mathrm{pt})=0$, by\n\\ref{maps:src:D.1.11} for coefficient group zero: its injective pair\n$(P,h)$ has zero target.", "D06;D20", "Cite the earlier exact classification coefficient statement rather than a not-yet-local definition.")
old = """For the complete integral class, the order-two calculation in
\\ref{maps:src:D.2.35} gives $H_6(K(\\mathbb Z/2,2);\\mathbb Z)=\\mathbb Z/2$
with generator the reduced positive complex $\\mathbb{CP}^3$ and
detector its mod-two cube. For $p=5,7$, \\ref{maps:src:D.1.10}
gives the corresponding cyclic group and cube detector.
"""
new = r"""For the complete integral class at order two, Cartan's elementary
complex has basic factor $\Gamma(x_2)\otimes\Lambda(y_3)$ with
$dy=2x$. Its degree-six boundary is
$d(y\gamma_2(x))=6\gamma_3(x)$, so its two-primary degree-six
group has order two. The next elementary factor is
$\Lambda(z_5)\otimes\Gamma(v_6)$ with $dv=2z$; it has no
degree-six homology. Products with a positive basic class begin
in degree seven, and their Tor terms begin in degree eight.
All further factors begin later. This is the complete integral
model in \cite[Theorem~1, pp.~11-09--11-10; Theorem~4 and its
corollary, p.~11-13; Appendix~1, pp.~11-22--11-23]{manCartan1955EML}.
Thus $H_6(K(\mathbb Z/2,2);\mathbb Z)=\mathbb Z/2$, generated
by $\gamma_3(1)$. Reduction of the positive complex
$\mathbb{CP}^3$ represents this divided-power generator:
the positive degree-two generator of $\mathbb{CP}^{\infty}$ has
third divided power equal to its positive degree-six generator,
and integer reduction induces the divided-power map.
The mod-two cube evaluates to one on this image. Evaluation
therefore has inverse $a\mapsto a\gamma_3(1)$.
For $p=5,7$, \ref{maps:src:D.1.10} gives the corresponding
cyclic group and cube detector.
"""
replace("LE", old, new, "D06;D20;D25;D27", "Repair the H6 locator: LB explicitly proves the Spin-bordism/cubic detector, not this integral H6 assertion. Supply the exact admitted Cartan low-degree chain calculation, positive reduction map and inverse evaluation. No enlargement of the earlier prime-to-six result and no new independent-check credit.")

units.check_permanent_identifiers(original, text)
assert text.count(r"\begin{definition}") == text.count(r"\end{definition}") == 3
assert text.count(r"\begin{theorem}") == text.count(r"\end{theorem}") == 3
assert text.count(r"\begin{proof}") == text.count(r"\end{proof}") == 3
assert r"\gamma_3\eqref" not in text
assert "\r" not in text
table = lane / "S6_SERIES_PUBLISH_MINIMAL_publication_defects.tsv"
with table.open(newline="") as stream:
    reader = csv.DictReader(stream, delimiter="\t")
    fields = reader.fieldnames
    rows = list(reader)
assert len(rows) == 756
new_rows = []
for index, (unit, kinds, line, old, new, reason) in enumerate(edits, 1):
    for kind in kinds.split(";"):
        new_rows.append(dict(zip(fields, [
            f"III-C8-MINIMAL-READBACK-{index:03d}-{kind}", kind,
            "maps:src:D.2."+numbers[unit],
            "minimal_primary_types.tex, sequential readback edit at line "+str(line),
            "pending page concordance", "weighted/minimal_primary_types.tex",
            "pending final build", old, new, reason,
            "whole3146-line candidate read; exact readback edit read; global gates open"])))
for row in rows:
    row["review_status"] = "whole3173-line repaired input and whole3146-line candidate read; exact readback corrections recorded; global gates open"
path.write_text(text, newline="\n")
with table.open("w", newline="") as stream:
    writer = csv.DictWriter(stream, fieldnames=fields, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows+new_rows)
print("UTC", datetime.now(timezone.utc).isoformat())
print("READBACK_EDITS", len(edits), "NEW_SINGLE_TYPE_ROWS", len(new_rows), "TOTAL_ROWS", len(rows+new_rows))
print("LINES", len(original.splitlines()), "TO", len(text.splitlines()), "SHA256", hashlib.sha256(path.read_bytes()).hexdigest())
print("OLD_IDENTITIES_PRESERVED; TRUE_LITERAL_REF_CONVERSIONS57; NEW_EQUATIONS67; NO_NEW_INDEPENDENT_CREDIT; SHARED_WRITES0")
