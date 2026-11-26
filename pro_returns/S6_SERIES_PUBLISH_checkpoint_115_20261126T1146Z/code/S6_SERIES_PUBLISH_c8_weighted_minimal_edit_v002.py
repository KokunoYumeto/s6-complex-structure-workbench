"""Publication edits of wholly read minimal-primary statements and proofs.

All mathematical decisions and substitutions are explicit below.  The
presentation helper only changes numbered-display syntax; it supplies no
mathematical or publication-criterion credit.
"""
import csv
from datetime import datetime, timezone
import hashlib
from pathlib import Path
import re
import S6_SERIES_PUBLISH_c8_integrate_presentation as presentation
import S6_SERIES_PUBLISH_c8_integrate_units as units

root = Path(__file__).resolve().parent.parent
path = root / "agents/continuation8_iii_integration/units/weighted/minimal_primary_types.tex"
lane = root / "agents/continuation8_iii_weighted_units"
original = path.read_text()
assert hashlib.sha256(path.read_bytes()).hexdigest() == "37c84ece7eb59c6aee9d0d13016fd3e98d9c9d70db5af3ad6ade427c2b39f8ff"
text = original
edits = []
numbers = {"LB": "35", "LC": "36", "LE": "38"}

def replace(unit, old, new, kinds, reason, count=1):
    global text
    assert text.count(old) == count, (unit, old[:160], count, text.count(old))
    for _ in range(count):
        at = text.index(old)
        edits.append((unit, kinds, text.count("\n", 0, at) + 1, old, new, reason))
        text = text[:at] + new + text[at + len(old):]

def block(unit, start, stop):
    a = text.index(start)
    b = text.index(stop, a)
    return text[a:b]

# The complete existing LB input table and the actual framed models move
# into one numbered definition; the conclusion remains one theorem.
lb_end = text.index(r"\end{theorem}") + len(r"\end{theorem}")
old = text[:lb_end]
models_a = old.index("Let $M_1=M_{")
result_a = old.index("Every simply connected output")
table_a = old.index("The zero positions")
table_end = old.index(r"\]", old.index(r"\label{maps:eq:D.C22}")) + 2
table = old[table_a:table_end]
models = old[models_a:result_a]
result = old[result_a:table_a]
result = result.replace("Every simply connected output $X$,\nfor every allowed finite multiplicity and affine twist, satisfies",
    "Every simply connected threefold $X$ determined by\nDefinition~\\ref{maps:def:minimal-two-data}, with any permitted finite\nmultiplicity and affine twist, satisfies")
tail = old[table_end:]
definition = r"""\subsection{Minimal primary smooth types}

\subsubsection{Order two}

\begin{definition}[Minimal order-two data]\hypertarget{tag-Q205}{}\label{maps:def:minimal-two-data}
{\normalfont\scriptsize tag Q205}\par
Use the marked elliptic data of
Definition~\ref{mapsIII:def:elliptic-marked-data} and choose one
of the patterns below. Use the prescribed primitive Mumford fan
at each multiplicative site, the listed original or logarithmic
additive cap, and the ordinary clutching $e\gamma$ of
\eqref{maps:eq:D.HY3}. The logarithmic sites are exactly those
listed in the pattern. The selected zero's cocycle is $\kappa u$,
with primitive $u$ whose first nonzero coordinate is positive;
put $\varepsilon=1+\kappa\pmod2$.

""" + table + "\n\n" + models + r"""These choices constitute the \emph{minimal order-two data}.
\end{definition}

\begin{theorem}[Order-two smooth types]\hypertarget{tag-02LB}{}\label{maps:src:D.2.35}
{\normalfont\scriptsize tag 02LB}\par
""" + result + tail
replace("LB", old, definition, "D04;D05;D10;D11;D13;D14;D16;D26",
    "Place the complete15-pattern table, prescribed fans, additive choices, ordinary clutch, exact cocycle sign and actual framed models in Q205. Keep every parameter and the cubic/classification conclusion in the single theorem; preserve C21/C22 identities.")

replace("LB", "The zero positions in the following table are numbered from zero in\nthe given ordered profiles.",
    "The selected positions in the following table are $i-1$, where $i$\nis the peripheral index in Definition~\\ref{mapsIII:def:elliptic-marked-data}.",
    "D04;D06;D20", "Give the exact index transport from the created ordered input definition, with inverse i=position+1.")
replace("LB", "These are the ordered elliptic matrix and section cocycle of\n\\ref{maps:src:D.2.23}.",
    "These are the ordered elliptic matrix and section cocycle of\nDefinition~\\ref{mapsIII:def:elliptic-marked-data}.",
    "D06;D20", "Use the actual relocated input table; A,g and the two period generators are unchanged.")
lb_proof_a = text.index(r"\begin{proof}")
lb_proof_b = text.index(r"\end{proof}", lb_proof_a)
lb_proof = text[lb_proof_a:lb_proof_b]
heads = re.findall(r"(?m)^\\emph\{[^\n]+\}\n", lb_proof)
assert len(heads) == 7
for index, head in enumerate(heads):
    replace("LB", head, ("\\begin{enumerate}\n" if index == 0 else "") + "\\item " + head,
        "D13;D14", "Make each of the seven complete proof stages an ordered proof item; the mathematical content and its scope are unchanged.")
at = text.index(r"\end{proof}")
replace("LB", text[at-75:at+len(r"\end{proof}")], text[at-75:at] + "\\end{enumerate}\n\\end{proof}",
    "D13;D14", "Close the single ordered proof after both complete recognition maps.")

replace("LB", "Normalize the elliptic short period to one, write its long period\nas $\\tau_E$, and choose a local logarithm $\\zeta_G$ of $G$.\nThe ratio $\\vartheta(z-a\\zeta_G)/\\vartheta(z)$",
    "For the actual nonzero short period $\\omega_s$, use the additive\ncoordinate $z_E=z_{\\rm add}/\\omega_s$, with inverse\n$z_{\\rm add}=\\omega_s z_E$. Put $\\tau_E=\\omega_l/\\omega_s$\nand choose $\\zeta_G=G_{\\rm lift}/\\omega_s$ for a local lift of $G$.\nThe multiplicative coordinate is $z=e^{2\\pi i z_E}$, with inverse\nlogarithm modulo the same short period.\nThe ratio $\\vartheta(z_E-a\\zeta_G)/\\vartheta(z_E)$",
    "D20;D22;D27", "State the actual additive-coordinate division and inverse multiplication, and separate the theta variable from its multiplicative exponential. The periods, divisor and unit functions are identical.")

# Historical execution assertions are records, not steps of these proofs.
old = block("LB", "The exact extraction program \\path{code/III/manifolds_tate_markings.py}", r"\begin{theorem}[the residual")
replace("LB", old, "\n\n", "D01;D07;D08;D09;D21",
    "Move the historical program/output assertions to the local review and proposed final program table. The symbolic all-parameter proof above remains; no unopened historical source or output receives credit.")

# LC has one complete input definition, one statement and one proof.  The
# ten-row subset in the old statement duplicates the complete36-row table.
old = r"""\begin{theorem}[the residual five- and seven-primary smooth types]\hypertarget{tag-02LC}{}\label{maps:src:D.2.36}
\textnormal{\small tag02LC.}
Consider the $36$ marked additive-filling patterns on the $30$ initial
rows of Theorem~\ref{maps:src:D.2.26} with residual $c=5$ or $7$ and
no orbifold obstruction. Use the primitive Mumford cap at every
multiplicative position, its prescribed fan at the selected zero,
the specified minimal original or finite cap at each additive
position, and no additional regular logarithmic transformation.
Allow every positive multiple of each finite monodromy order and
every free affine twist for which the completed manifold is simply
connected.

Put $p=c$, let $I_\nu$ be the selected zero, and set $Q_f=b/p$.
Let $s$ be the primitive fibre generator with the marking of
Theorem~\ref{maps:src:D.2.26}. Every such manifold has, in its complex
orientation, the following complete marked data:
"""
new = r"""\subsubsection{Orders five and seven}

\begin{definition}[Minimal odd-primary data]\hypertarget{tag-Q206}{}\label{maps:def:minimal-odd-data}
{\normalfont\scriptsize tag Q206}\par
Use the ordered profiles of Definition~\ref{mapsIII:def:elliptic-marked-data}
and the natural initial pairs of \ref{maps:src:D.2.22}. Choose the
minimal additive fillings of \ref{maps:src:D.2.26} with residual
$c=5$ or $7$ and trivial orbifold obstruction. Use the primitive
Mumford cap at every multiplicative position and its prescribed fan
at the selected zero. The logarithmic sites are exactly the chosen
additive sites. At every finite site allow each positive multiple
of its monodromy order and every free affine twist; retain the
ordinary clutch $e\gamma$ of \eqref{maps:eq:D.HY3}.
Put $p=c$, let $I_\nu$ be the selected zero, and set $Q_f=b/p$.
Selected positions are $i-1$ in the input definition's peripheral
order. In the tables, $O$ and $F$ denote the original and finite
additive caps, and a dash denotes an absent additive site.
These choices are the \emph{minimal odd-primary data}.
\end{definition}

\begin{theorem}[Five- and seven-primary smooth types]\hypertarget{tag-02LC}{}\label{maps:src:D.2.36}
{\normalfont\scriptsize tag 02LC}\par
The data of Definition~\ref{maps:def:minimal-odd-data} give $36$
patterns on $30$ marked initial rows. Every simply connected output
$X$ has, in its complex orientation, the following complete marked
data, where $s$ is the primitive fibre generator of
\ref{maps:src:D.2.26}:
"""
replace("LC", old, new, "D04;D05;D06;D10;D11;D13;D14;D16;D26",
    "Define the entire natural minimal-input range, prescribed fans, finite orders, affine twists, ordinary clutch and index map in Q206. The theorem still covers every simply connected choice and derives36patterns/30rows.")
old = block("LC", "For clarity, the following order-five assignments use zero-based", "Among all $36$ patterns")
replace("LC", old, "", "D11;D12;D17",
    "Remove only the duplicate10-row subset: its rows21,22,25,26,27,28,29,30,33,34 and their exact profile,a,b,zero,cap,nu,w,P coordinates remain in the complete36-row table in the same proof. The universal formula and every marked assignment remain.")
replace("LC", "Use the ordered elliptic matrices and section cocycles of\nTheorem~\\ref{maps:src:D.2.22}.",
    "Use the ordered elliptic matrices and section cocycles of\nDefinition~\\ref{mapsIII:def:elliptic-marked-data}.",
    "D06;D20", "Point the matrix/cocycle input to its complete live definition; retain KX for the natural-row criterion itself.")
replace("LC", "The last column is calculated in parts 9--12.",
    "The last column is computed by the Borel comparison and Pontryagin\nevaluation below.", "D06;D19", "Replace a brittle proof-item-number range by the named complete calculations retained in this proof.")
replace("LC", "Dividing coordinates by $C$ gives", "Applying $C_0^{-1}$ to the period coordinates gives",
    "D20;D22", "Use the actual cusp matrix C0 with its displayed inverse; C denotes the fixed curve and is not a coordinate matrix.")
replace("LC", "The ratio $\\theta(z-a\\zeta_G)/\\theta(z)$ representing",
    "For the additive coordinate $z_E=z_{\\rm add}/\\omega_s$, division\nby the nonzero short period has inverse multiplication by $\\omega_s$;\nthe physical coordinate is $z=e^{2\\pi i z_E}$.\nThe ratio $\\theta(z_E-a\\zeta_G)/\\theta(z_E)$ representing",
    "D20;D22;D27", "Give the exact short-period coordinate map and inverse and separate the theta coordinate from its multiplicative exponential.")
for old, new, why in [
    ("Retain $d_0,n_i,A'_i$ from part 5", "Retain $d_0,n_i,A'_i$ from the primitive vanishing vector $l_i$", "Use the actual already-defined vector and its coefficients."),
    ("as constructed in part 7", "in the nodal basis constructed below", "Use the named exact basis construction."),
    ("With the cusp matrix $C_0$ of part 4", "With the displayed cusp period matrix $C_0$", "Reference the declared matrix itself."),
    ("the generators of part 3", "the exterior generators and their section sweeps", "Retain the exact free generators identifying cohomology."),
    ("and part 7, using", "and the nodal degree $-2Q_f$, using", "State the actual numerical degree supporting the evaluation."),
    ("accounted for in parts 2--3\nand in the global comparison above", "accounted for by the complete finite and ordinary cap kernels\nand the global comparison above", "Identify the actual uneliminated kernels, not a positional item range."),
    ("use\n$\\psi_s,\\phi_s$ from part 11", "use\nthe already defined inverse marking maps $\\psi_s,\\phi_s$", "Reference the exact maps by their mathematical symbols."),
    ("These hypotheses hold by part 2;", "The integral homology calculation gives these hypotheses;", "Keep the proven zero-free-rank and spin scope."),
    ("The equality of $P$ and $h$ follows from parts 10--12 and the\ndisplayed markings", "The equality of $P$ and $h$ follows from\n\\eqref{maps:eq:D.OP10}--\\eqref{maps:eq:D.OP11} and the displayed markings", "Use live equation references for the actual complete invariants."),
]:
    replace("LC", old, new, "D06;D19", why)
old = block("LC", "The complete Tate markings are reconstructed by", r"\begin{theorem}[the mixed ten-")
replace("LC", old, "\n\n", "D01;D07;D08;D09;D21;D25",
    "Move the historical certificate/JSON paragraph to records. Its stale curve coefficient(w²-1)/2 is an already-admitted LC assignment error: the retained proof gives(w²/nu²-1)/2, with simultaneous subgroup rescaling and inverse marking. No additional mathematical refutation or independent credit is claimed.")

# LE uses the already constructed models, named once in Q207.  Its complete
# parameter theorem, invariant table and marked recognition stay together.
old = block("LE", r"\begin{theorem}[the mixed ten-", "The twelve patterns below satisfy")
new = r"""\subsubsection{Orders ten and fourteen}

\begin{definition}[Minimal mixed-primary data]\hypertarget{tag-Q207}{}\label{maps:def:minimal-mixed-data}
{\normalfont\scriptsize tag Q207}\par
Use the ordered profiles of Definition~\ref{mapsIII:def:elliptic-marked-data}
and a pattern in \eqref{maps:eq:D.MP2}. Use the prescribed primitive
Mumford fan at every multiplicative position, its listed additive
choice and the ordinary clutch $e\gamma$. The logarithmic sites are
exactly the listed additive sites. Allow every positive finite
multiplicity and every free affine twist. A selected position is
$i-1$ in the input definition's peripheral order.

Use the framed models $M_0,M_1$ of
Definition~\ref{maps:def:minimal-two-data}. Define the marked models
$Z_{5,0},Z_{5,1},Z_{7,1}$ by the respective constructions
$\mathrm{OS56}$ with $(a,b)=(2,5)$ and selected position $1$,
$\mathrm{OS55}$ with $(a,b)=(1,5)$ and selected position $1$,
and $\mathrm{OS47}$ with $(a,b)=(1,7)$ and selected position $1$.
In each case take $e=1$ and its listed multiplicative caps.
Their marking sends the odd generator $e_p$ to $s,s,3s$,
respectively; the inverse evaluations are $\alpha,\alpha,3^{-1}\alpha$,
where $\alpha(s)=1$. Theorem~\ref{maps:src:D.2.36} proves
$H_2=\mathbb Z/p$, $b_3=0$, $\mu=0$ and
$\mathfrak p=\epsilon e_p$ for these actual models.
The preceding filling choices constitute the \emph{minimal mixed-primary data}.
\end{definition}

\begin{theorem}[Ten- and fourteen-torsion smooth types]\hypertarget{tag-02LE}{}\label{maps:src:D.2.38}
{\normalfont\scriptsize tag 02LE}\par
Every simply connected output $X$ of
Definition~\ref{maps:def:minimal-mixed-data} satisfies
"""
replace("LE", old, new, "D04;D05;D06;D10;D11;D13;D14;D16;D22;D26;D27",
    "Put the exact twelve-pattern cap and unbounded parameter scope in Q207. Name the odd models by actual LC members and their explicit inverse markings. Use the already constructed order-two embeddings without redefining them; keep MP1/MP2 and every complete invariant.")
replace("LE", "The twelve patterns below satisfy\n", "", "D11", "The defined-input theorem lead now states this conclusion once.")
replace("LE", r"\begin{enumerate}[label={$\langle1\rangle$\arabic*.},leftmargin=*]", r"\begin{enumerate}",
    "D08;D13;D14", "Use the publication proof-step counter in the one complete proof.")
old = block("LE", "Let $M_1=M_{\\mathrm{conic}}$, with its positive conic-surgery orientation.", "Here $e_2$ is the unique")
new = r"""The two order-two models of Definition~\ref{maps:def:minimal-two-data}
have the following full marked invariants, by
Theorem~\ref{maps:src:D.2.35} and its reduced spin-bordism quotient:
\[
 H_2=H_3=\mathbb Z/2,\quad b_3=0,\quad
 \mathfrak p(M_t)=t e_2,\quad
 \mu(M_t)=t\gamma_3(e_2),\qquad t=0,1.                 \qquad\textup{(1)}
\]

"""
replace("LE", old, new, "D11;D12;D17", "Apply the identical framed embeddings and orientations already defined and proved for LB. Keep the full order-two invariant display, whose P coordinate is supplied by that same CP3 quotient, and its marking.")
replace("LE", "be the marked realized odd-primary models of \\ref{maps:src:D.2.36}.",
    "be the marked odd-primary models of Definition~\\ref{maps:def:minimal-mixed-data}.",
    "D06;D11", "Point to the named actual realizations and inverse markings rather than defining the models a second time.")
replace("LE", "These are the defining ordered data of \\ref{maps:src:D.2.22}.",
    "These are the ordered data of Definition~\\ref{mapsIII:def:elliptic-marked-data}.",
    "D06;D20", "Bind every raw profile matrix,cocycle,component and height to the complete mathematical input definition; the KX criterion remains separately cited.")
replace("LE", "The per-profile counts, in raw order, are", "The per-profile counts, in the order of that definition, are",
    "D01;D04;D06", "Use the mathematical peripheral/profile order, not an implementation-array order.")
replace("LE", "The raw profiles relevant to their indices are", "The ordered profiles determining these positions are",
    "D01;D04;D20", "State the actual mathematical index convention.")
replace("LE", "Normalize the elliptic short period to one,\nwrite $\\tau_E$ for its long period and $\\zeta_G$ for the local\nlogarithm of $G$. The theta ratio\n$\\vartheta(z-a\\zeta_G)/\\vartheta(z)$, with reciprocal inverse,",
    "For the actual nonzero short period $\\omega_s$, use\n$z_E=z_{\\rm add}/\\omega_s$, with inverse\n$z_{\\rm add}=\\omega_s z_E$. Put $\\tau_E=\\omega_l/\\omega_s$\nand $\\zeta_G=G_{\\rm lift}/\\omega_s$; the physical coordinate\nis $z=e^{2\\pi i z_E}$, with inverse logarithm modulo that period.\nThe theta ratio $\\vartheta(z_E-a\\zeta_G)/\\vartheta(z_E)$,\nwith reciprocal inverse,",
    "D20;D22;D27", "Give the exact coordinate map and inverse at the actual short period, separate additive theta and multiplicative coordinates, and keep all unit functions.")
replace("LE", "The primitive short basis\nof the stipulated fan is $SC$, not the physical basis $S$.",
    "The prescribed fan's primitive short basis is $SC$; the map\nfrom its coordinates to physical short coordinates is $v\\mapsto Cv$,\nwith inverse $x\\mapsto C^{-1}x$.",
    "D02;D20;D27", "State the exact fan-coordinate map and inverse directly; both descriptions concern the same actual cap.")
replace("LE", "These explicit gauges, inverses and actual theta factors provide the\ngeometric comparison; equality of period matrices alone is not used.",
    "These gauges, reciprocal inverses and theta factors identify the\nactual line and all its period gluings.", "D02;D08;D22",
    "State the proved geometric comparison positively, retaining every specified map.")
replace("LE", "They retain all holomorphic units. In particular this\nis not just a matrix conjugacy used as a germ identification.",
    "They retain all holomorphic units in these inverse germ maps.",
    "D02;D08;D22", "State the established period-exponential/logarithm germ map directly.")
replace("LE", "These calculations\nare on the given fan. No local or global flop is invoked.",
    "These calculations use the prescribed fan under $C$ and $C^{-1}$.",
    "D02;D08;D26", "Keep the precise fan scope and exact coordinate morphism without a process exclusion.")
# Move the full coprime CW and bordism proof before its first use.  Its
# final connected-sum paragraph duplicates the later explicit neck proof.
coprime_start = text.index(r"\item \emph{The full coprime homotopy and bordism maps.}")
coprime_end = text.index(r"\end{enumerate}", coprime_start)
coprime = text[coprime_start:coprime_end]
duplicate_a = coprime.index("For the connected sum, contract the classifying maps")
duplicate = coprime[duplicate_a:]
coprime = coprime[:duplicate_a]
replace("LE", duplicate, "", "D11;D12;D17",
    "The connected-sum paragraph repeats the later complete constant-ball/neck map and oriented spin one-handle bordism. That proof retains inclusions/collapse inverses, P addition, full h addition and every concrete Phi/Phi-inverse coordinate; the coprime CW equivalence is kept here in full.")
replace("LE", coprime, "", "D14", "Move this whole coprime CW,CRT and Thom-spectrum proof before its first use in the integral fundamental-class calculation; no sentence or permanent identity is discarded.")
replace("LE", r"\item \emph{The full fundamental-class invariant.}", coprime + r"\item \emph{The full fundamental-class invariant.}",
    "D14", "Insert the complete prerequisite proof immediately before its first application, preserving MP9/MP10 and all inverse maps.")

old = block("LE", "The construction of $M_0$ in \\ref{maps:src:D.2.35} uses an oriented sphere", "The oriented connected sum $M_t")
replace("LE", old, r"""The surgery traces of Theorem~\ref{maps:src:D.2.35} use exactly
the embeddings and orientations in Definition~\ref{maps:def:minimal-two-data}.
Their incoming generator maps to $e_2$ and their outgoing second-homology
map is an isomorphism. The respective incoming cubes are zero and one.
The reduced CP$^3$ spin-bordism quotient above therefore gives the
full marked invariants (1), including the refined coordinate.

""", "D11;D12;D17;D22",
    "Remove the second derivation of the same two surgery models only after mapping the identical embeddings,framings,orientations,incoming/outgoing generator maps and cubic detector to the earlier complete LB proof. Keep the full even refined invariant application.")
for old, new, reason in [
    ("By item~3 and the sweep values", "By the exterior quotient and the sweep values", "Use the actual retained quotient maps."),
    ("The exact tensor comparison of item~7", "The exact tensor-square comparison above", "Reference the proved fibre tensor and reciprocal Cartier monomials."),
    ("The full coprime homotopy maps of item~13 then give", "The preceding coprime homotopy maps then give", "The full CW proof now precedes its use."),
    ("These are the actual integral cylinder coordinates in that exterior sequence.", "The columns of $R$ give the integer cylinder chains in that exterior sequence.", "State explicitly how the right inverse supplies actual bounding chains."),
    ("The proof uses the actual", "The proof uses the actual", "No-op")
]:
    if old != new:
        replace("LE", old, new, "D06;D20;D22", reason)
old = text[text.index("The exact certificate \\path{code/III/manifolds_mixed_prime_AH.py}"):]
replace("LE", old, "", "D01;D07;D08;D09;D21",
    "Move the historical certificate locator and finite check claims to records/program proposals. The full integral coprime homotopy and spin-bordism maps remain proved; no historical execution is newly credited.")

# Format every OS name as the actual catalogue name, preserving each
# profile and zero-position tuple literally.
matches = list(re.finditer(r"(?m)^(?P<row>\d+&)?(?P<os>43|45|46|47|49|50|55|56)(?P<suffix>/(?:II|III|IV|\\mathrm\{(?:II|III|IV)\}))?&", text))
for match in reversed(matches):
    old = match[0]
    osname = r"\mathrm{OS" + match["os"] + "}"
    suffix = match["suffix"] or ""
    if suffix and r"\mathrm" not in suffix:
        suffix = r"/\mathrm{" + suffix[1:] + "}"
    new = (match["row"] or "") + osname + suffix + "&"
    owner = "LE" if match.start() > text.index(r"\label{maps:def:minimal-mixed-data}") else ("LC" if match.start() > text.index(r"\label{maps:def:minimal-odd-data}") else "LB")
    # Equal row prefixes occur repeatedly; edit this exact occurrence by offset.
    edits.append((owner, "D04;D20", text.count("\n", 0, match.start()) + 1, old, new,
        "Spell out the mathematical OS profile name; every ordered row, component and parameter remains identical."))
    text = text[:match.start()] + new + text[match.end():]

# Each inherited local number gets its own new permanent equation tag.
# The old permanent D.MP numbers are handled separately by the bounded helper.
manual = list(re.finditer(r"\\qquad\\textup\{\((\d+)\)\}", text))
assert len(manual) == 67
assert len({match[1] for match in manual}) == 67
alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
new_equations = {}
for index, number in enumerate(sorted((int(m[1]) for m in manual)), 8):
    tag = "Q2" + alphabet[index // 36] + alphabet[index % 36]
    new_equations[number] = (tag, "maps:eq:MP_local_" + str(number))
for match in reversed(manual):
    number = int(match[1])
    tag, label = new_equations[number]
    a = text.rfind(r"\[", 0, match.start())
    b = text.index(r"\]", match.end()) + 2
    assert a >= 0 and r"\]" not in text[a:match.start()]
    old = text[a:b]
    new = old.replace(r"\[", r"\begin{equation}", 1)
    new = new[:new.rfind(r"\]")] + r"\end{equation}" + new[new.rfind(r"\]")+2:]
    new = new.replace(match[0], r"\hypertarget{tag-" + tag + r"}{}\label{" + label + "}")
    replace("LE", old, new, "D06;D10;D19",
        "Replace inherited local equation(" + str(number) + ") by automatic numbering with permanent tag" + tag + " and label" + label + "; preserve its whole mathematical display.")

# At this point parenthesized integers in LE are equation references,
# except the two SO(4) group names.  Inspect and replace each exact match.
le_begin = text.index(r"\label{maps:def:minimal-mixed-data}")
refs = list(re.finditer(r"\((\d+)\)", text[le_begin:]))
literal_reference_count = 0
for match in reversed(refs):
    a = le_begin + match.start()
    b = le_begin + match.end()
    number = int(match[1])
    if text[max(0, a-2):a] == "SO":
        assert number == 4
        continue
    assert number in new_equations, (number, text[max(0, a-80):b+80])
    label = new_equations[number][1]
    old = match[0]
    new = r"\eqref{" + label + "}"
    edits.append(("LE", "D06;D19", text.count("\n", 0, a) + 1, old, new,
        "Replace this literal local equation reference by its exact retained mathematical target; the source location distinguishes every occurrence."))
    text = text[:a] + new + text[b:]
    literal_reference_count += 1

text, header_changes, header_issues = presentation.statement_records_to_small_tags(text)
assert not header_changes and not header_issues
before_helpers = text
text, helper_changes, helper_issues, aliases = presentation.remove_manual_equation_tags(text)
assert not helper_issues
for change in helper_changes:
    before = before_helpers[:change.start]
    owner = "LE" if r"\label{maps:def:minimal-mixed-data}" in before else ("LC" if r"\label{maps:def:minimal-odd-data}" in before else "LB")
    edits.append((owner, change.kind, before_helpers.count("\n", 0, change.start)+1,
        change.old, change.new, change.reason))
issues = presentation.unresolved_literal_equation_references(text, aliases)
assert not issues, issues
allowed_labels = ["maps:def:minimal-two-data", "maps:def:minimal-odd-data", "maps:def:minimal-mixed-data"] + [pair[1] for pair in new_equations.values()]
allowed_targets = ["tag-Q205", "tag-Q206", "tag-Q207"] + ["tag-" + pair[0] for pair in new_equations.values()]
units.check_permanent_identifiers(original, text, allowed_labels, allowed_targets)
assert text.count(r"\begin{definition}") == text.count(r"\end{definition}") == 3
assert text.count(r"\begin{theorem}") == text.count(r"\end{theorem}") == 3
assert text.count(r"\begin{proof}") == text.count(r"\end{proof}") == 3
assert r"\path{" not in text and r"\tag{" not in text
assert "\r" not in text

fields = ["change_id", "type", "statement_id", "old_location", "old_page", "new_location", "new_page", "old_text", "new_text", "reason", "review_status"]
rows = []
for index, (unit, kinds, line, old, new, reason) in enumerate(edits, 1):
    for kind in kinds.split(";"):
        rows.append(["III-C8-MINIMAL-PUB-" + f"{index:03d}" + "-" + kind, kind,
            "maps:src:D.2." + numbers[unit], "minimal_primary_types.tex, sequential edit at line " + str(line),
            "pending page concordance", "weighted/minimal_primary_types.tex", "pending final build", old, new, reason,
            "whole input and exact edit read; candidate whole readback and root admission pending"])
path.write_text(text, newline="\n")
with (lane / "S6_SERIES_PUBLISH_MINIMAL_publication_defects.tsv").open("w", newline="") as stream:
    writer = csv.writer(stream, delimiter="\t", lineterminator="\n")
    writer.writerow(fields)
    writer.writerows(rows)
with (lane / "S6_SERIES_PUBLISH_MINIMAL_new_equation_identities.tsv").open("w", newline="") as stream:
    writer = csv.writer(stream, delimiter="\t", lineterminator="\n")
    writer.writerow(["former_local_number", "tag", "label", "scope"])
    for number, (tag, label) in new_equations.items():
        writer.writerow([number, tag, label, "same retained LE equation; automatic numbering; not an extra result"])
print("UTC", datetime.now(timezone.utc).isoformat())
print("MINIMAL_LINES", len(original.splitlines()), "TO", len(text.splitlines()), "EXACT_EDITS", len(edits), "SINGLE_TYPE_ROWS", len(rows))
print("NEW_DEFINITIONS", "Q205,Q206,Q207", "NEW_EQUATIONS", len(new_equations), "Q208-Q222", "LITERAL_REFERENCES", literal_reference_count)
print("NEXT_RESERVED_TAG", "Q223", "OLD_IDENTITIES_ALL_PRESERVED; UNRESOLVED_LITERALS0; SHARED_WRITES0; AUTOMATIC_CRITERION_CREDIT0")
