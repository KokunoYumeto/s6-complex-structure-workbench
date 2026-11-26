#!/usr/bin/env python3
"""Prepare the bounded later part; never modify the shared manuscript.

The --reviewed switch records exposed comparisons only after the complete
receiving statement/proof blocks have actually been read.
"""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import csv
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
TMP = ROOT.parents[1] / "tmp"
OUT = ROOT / "agents" / "continuation3_provenance" / "later_part"
OUT.mkdir(parents=True, exist_ok=True)
MAIN = (ROOT / "S6_SERIES_PUBLISH_II.tex").read_text()
old13 = (TMP / "c3_provenance_section13_old.tex").read_text()
old14 = (TMP / "c3_provenance_section14_old.tex").read_text()
old12proposal = (ROOT / "agents/continuation3_provenance/section12/S6_SERIES_PUBLISH_section12_proposed.tex").read_text()
units = {"12": old12proposal, "13": old13, "14": old14}
rows = []

def digest(s):
    return hashlib.sha256(s.encode()).hexdigest()

def write_tsv(path, data, fields=None):
    if fields is None:
        fields = list(data[0])
    with path.open("w", newline="") as f:
        w = csv.DictWriter(f, fields, delimiter="\t")
        w.writeheader()
        w.writerows(data)

def record(old, new, owner, types, reason, where="complete statement/proof block"):
    rows.append(dict(change_id=f"II-C3-LATER-{len(rows)+1:03d}",
        type=types, statement_id=owner, old_location=where,
        old_page="cp35; final page concordance pending",
        new_location=where, new_page="integrated build pending",
        old_text=old, new_text=new, reason=reason,
        review_status="Complete old and receiving proof comparison pending --reviewed."))

def edit(which, old, new, owner, types, reason, where="complete statement/proof block", all_matches=False):
    unit = units[which]
    count = unit.count(old)
    assert count == 1 or (all_matches and count > 0), (owner, count, old[:100])
    for i in range(count if all_matches else 1):
        record(old, new, owner, types, reason, where + (f"; occurrence {i+1}" if count > 1 else ""))
    units[which] = unit.replace(old, new) if all_matches else unit.replace(old, new, 1)

def statement_block(text, label):
    p = text.index(r"\label{" + label + "}")
    start = max(text.rfind(r"\begin{" + e + "}", 0, p)
                for e in ("proposition", "lemma", "theorem", "corollary", "remark", "example", "definition", "cited"))
    assert start >= 0, label
    env = re.match(r"\\begin\{([^}]+)\}", text[start:]).group(1)
    env_end = text.index(r"\end{" + env + "}", p) + len(r"\end{" + env + "}")
    next_proof = text.find(r"\begin{proof}", env_end)
    next_owner = re.search(r"\\begin\{(?:proposition|lemma|theorem|corollary|remark|example|definition|cited)\}", text[env_end:])
    if next_proof < 0 or (next_owner and env_end + next_owner.start() < next_proof):
        end = env_end
    else:
        end = text.index(r"\end{proof}", next_proof) + len(r"\end{proof}")
    return text[start:end]

def statement_only(text, label):
    b = statement_block(text, label)
    env = re.search(r"\\begin\{([^}]+)\}", b).group(1)
    return b[:b.index(r"\end{" + env + "}") + len(r"\end{" + env + "}")]

# Exact primary locators and neutral proof language.
for old, new, owner, reason in [
    ("For $c\\in\\Sigma$ retain the entire Cartier fibre $F_c$, including its multiplicities, and put",
     "For $c\\in\\Sigma$, write $F_c$ for the full Cartier fibre with its multiplicities, and put",
     "cdp:st:C4c", "Define the full fibre positively; all multiplicities and the exact cohomology test remain."),
    ("gives an actual line bundle", "gives a line bundle", "cdp:st:C4c",
     "The explicit base twist constructs the required line; remove the process adjective."),
    ("with every Cartier layer and connecting map retained", "including every Cartier layer and connecting map",
     "cdp:st:C4c", "Keep the full filtration scope in direct mathematical language."),
    ("ideal layer of the full fibre is an actual subsheaf", "ideal layer of the full fibre is a subsheaf",
     "cdp:st:C4f", "The displayed injection proves the subsheaf assertion."),
    ("In the second case use instead the actual twists", "In the second case use the twists",
     "cdp:st:C4f", "The explicit Lr formula identifies the required parameter family."),
    (r"Retain the fixed marked functions $\tau,\mu,\beta_c$ and put", r"Use the fixed marked functions $\tau,\mu,\beta_c$ and put",
     "cdp:st:C5c", "Refer to the defined marked functions without retention vocabulary.")
]:
    edit("12", old, new, owner, "D08", reason)
edit("13", r"\cite[Theorem~1.6]{BierstoneMilman1997}",
     r"\cite[Theorem~1.6 and Remarks~1.7, arXiv v2, pp.~5--6]{BierstoneMilman1997}",
     "cdp:st:D.2.5", "D18",
     "The opened arXiv v2 theorem and remarks give analytic embedded resolution by locally finite smooth-centre blowups; compactness of the central fibre makes the local construction finite here.",
     all_matches=True)
edit("13", r"the finite \emph{\'etale} map of A.3.4:",
     r"the finite \emph{\'etale} map of \cref{cdp:st:A.3.4}:",
     "cdp:st:D.2.5", "D04;D06", "Resolve the precise root-cover owner by its Paper II number.")
edit("13", r"This proof uses only the rational version of \ref{cdp:st:D.1.9}.",
     "", "cdp:st:D.2.5", "D02;D11",
     "The statement already specifies rational Betti numbers and rational monodromy; the proof explicitly applies D.1.9 to that setting.")
edit("13", "by the actual Picard family", "by the Picard family",
     "cdp:st:D.2.5", "D08", "State the analytic-family semicontinuity premise directly.")
edit("13", " No classification of the surface $Z$ is used in this step.", "",
     "cdp:st:D.2.5", "D02",
     "The preceding Gauduchon-degree argument is complete; remove the defensive comparison.")
edit("13",
     r"homology vanishing and algebraic dimension one. The monodromy obstruction of \ref{cdp:st:D.2.3} gives the normal-crossings equality in \ref{cdp:st:D.2.4}.",
     "homology vanishing and algebraic dimension one.",
     "cdp:st:D.2.2", "D12;D14",
     "The normal-crossing specialization follows immediately after this general equality; remove its duplicate forward preview.")

old_nc = statement_block(units["13"], "cdp:st:D.2.4")
new_nc = old_nc[:old_nc.index(r"\begin{proof}")]
new_nc = new_nc.replace(r"\begin{proposition}", r"\begin{corollary}", 1).replace(r"\end{proposition}", r"\end{corollary}", 1)
new_nc = re.sub(r"\\StatementRecord\{cdp:st:D\.2\.4\}[^\n]*",
    lambda _: r"\StatementRecord{cdp:st:D.2.4}{proved}{01GB}{\SeriesRef{cdp:st:D.2.2}, \SeriesRef{cdp:st:D.2.7}}", new_nc)
new_nc += r"""\begin{proof}
Apply \cref{cdp:st:D.2.2} to the identical threefold $Y$ and map
$f$, which satisfy all its hypotheses. Its equality holds for the same
full fibres with their given multiplicities. This gives both
displayed equalities. The example in \cref{cdp:st:D.2.7} has
normal-crossing reduced supports and realizes this subclass.
\end{proof}"""
edit("13", old_nc, new_nc, "cdp:st:D.2.4", "D12;D14",
     "The former two-step proof is a specialization of the general D.2.2 equality: the comparison is identity on Y, the base and the full Cartier fibres. Keep the narrower corollary, its tag and its realization, and cite the general proof once.")

edit("14", "Its correct\nimage is", "Its\nimage is", "cdp:st:E5", "D01;D08",
     "The critical-image ideal is a mathematical assertion, stated without draft-correction vocabulary.")
edit("14",
     "These formulas type the comparison at the special fibres.\nThe proof above only uses the genuine smooth-locus boundary and\nthe globally locally free source, so it makes no assumption about\nlocal freeness of $R^2g_*T_{Y/C}$ at a special value.",
     "These formulas describe the image at the special fibres.",
     "cdp:st:E5", "D02;D11;D12",
     "Keep all three critical ideals and the logarithmic quotient; the smooth-locus proof already identifies its locally free source.")
edit("14",
     r"""\item We prove the lifting assertion at every Artin order; this is more
than the tangent-space assertion of \ref{cdp:st:E5}. The obstruction calculations
below use the Cech construction of holomorphic-map deformations""",
     r"""\item We use the \v{C}ech construction of holomorphic-map deformations""",
     "cdp:st:E6", "D02;D12;D23",
     "Remove the comparison against a weaker assertion while preserving the exact cited obstruction construction and all Artin-lifting steps.")
edit("14", "as can be checked without a comparison\nof obstruction theories:", "by the following equality of cocycles:",
     "cdp:st:E6", "D02",
     "The displayed restricted cocycle and coboundary are the exact comparison.")
edit("14", "To check this without assuming a\nreduced parameter space, represent", "Over the full analytic germ, represent",
     "cdp:st:E6", "D02",
     "State positively that the free-complex and unit-splitting argument applies to the full analytic germ, including nilpotents.")
edit("14", "the graph of an actual map", "the graph of a holomorphic map",
     "cdp:st:E6", "D08", "Name the map's analytic structure.")
edit("14", r"\cite[Theorem 11]{Buchdahl1999}", r"\cite[Theorem~11, p.~297]{Buchdahl1999}",
     "cdp:st:E6", "D18", "Opened the theorem giving Kählerness of a compact complex surface with even b1.", all_matches=True)
while "Cech" in units["14"]:
    p = units["14"].index("Cech")
    owner = re.findall(r"\\StatementRecord\{([^}]+)\}", units["14"][:p])[-1]
    edit("14", "Cech", r"\v{C}ech", owner, "D23",
         "Restore the accent in the cocycle terminology.", where="Čech occurrence in this owner's full proof",
         all_matches=False) if units["14"].count("Cech") == 1 else None
    if "Cech" in units["14"] and units["14"].count("Cech") > 1:
        record("Cech", r"\v{C}ech", owner, "D23", "Restore the accent in the cocycle terminology.",
               "Čech occurrence in this owner's full proof")
        units["14"] = units["14"].replace("Cech", r"\v{C}ech", 1)
for old, new, owner, reason in [
    (r"\cite[Proposition~6.1]{Viaclovsky2026Combs}", r"\cite[Proposition~6.1, pp.~19--21]{Viaclovsky2026Combs}", "cdp:st:E7", "The opened proposition gives the toric hexagonal quotient, logarithmic periods and coherent extension."),
    (r"\cite[Proposition~3.1]{Viaclovsky2026Two}", r"\cite[Proposition~3.1, pp.~6--7]{Viaclovsky2026Two}", "cdp:st:E7", "The opened proposition identifies the nodal fillings and their valuation directions."),
    (r"\cite[Proposition~2.5]{LiuRollenske2026}", r"\cite[Proposition~2.5, p.~5]{LiuRollenske2026}", "cdp:st:E7", "The opened proposition gives the hexagonal compactification and two independent lattice directions."),
    (r"\cite[Proposition~4.1, case~(i)]{Viaclovsky2026Combs}", r"\cite[Proposition~4.1, case~(i), pp.~11--12]{Viaclovsky2026Combs}", "cdp:st:E7", "The opened local frame has ei=αi+ℓβi and fi=βi, so the graph period changes by the stated logarithmic identity matrix."),
    (r"\cite[Section~10(1)]{Viaclovsky2026Combs}", r"\cite[Section~10(1), p.~33]{Viaclovsky2026Combs}", "cdp:st:E7", "Locate the published fibration-retention question precisely."),
    (r"\cite[Proposition~2.1]{LiuRollenske2026}", r"\cite[Proposition~2.1, pp.~3--4]{LiuRollenske2026}", "cdp:st:E14", "The opened equation, section and line-homomorphism computation are the inputs to the displayed coordinate isomorphism."),
    (r"\cite[Theorem~5.1]{LiuRollenske2026}", r"\cite[Theorem~5.1, p.~21]{LiuRollenske2026}", "cdp:st:E14", "Use the opened topology theorem at its exact page."),
]:
    edit("14", old, new, owner, "D18", reason, all_matches=True)
edit("14", "For the actual AC period branch", "For the AC period branch",
     "cdp:st:E8", "D08", "State the defining equation of the period branch directly.")
edit("14",
     r"""\eqref{cdp:eq:E-theta-general}. Thus the square identity in Lead~9
uses the equation $\wp(\mu)=0$; a general section requires the
displayed additional term unless its other period terms cancel it.""",
     r"""\eqref{cdp:eq:E-theta-general}. On the branch $\wp(\mu)=0$
its second term is zero.""",
     "cdp:st:E8", "D03;D05;D08",
     "Delete the prompt reference. The general determinant identity and its explicit restriction to wp=0 give the complete mathematical comparison.")
edit("14",
     r"$E_2'=(\pi i/6)(E_2^2-E_4)$, yields at $\wp=0$",
     r"$E_2'=(\pi i/6)(E_2^2-E_4)$ from"+"\n"+r"\cite[eq.~(3.5), p.~8]{AtkinGarvan2002}, yields at $\wp=0$",
     "cdp:st:E8", "D18",
     "The opened primary q-derivative identity converts by d/dτ=2πi q d/dq to the stated modular derivative.")
edit("14",
     r"\item The equation $j(\tau)=1728t$ shows",
     r"\item The equation $j(\tau)=1728t$ in"+"\n"+r"\cite[Remark~3.12, p.~19]{AC26} shows",
     "cdp:st:E8", "D18",
     "Locate the marked algebraic-base identification used to compute root orders.")

edit("14",
     "The assertion that every small deformation of a fibration extends\n"
     "over its original fixed positive-genus target curve $C$ is false even for a torus\n"
     "fibration with Kodaira--Spencer rank two at a regular value.",
     r"""There is a smooth projective family of compact threefolds
$Y_s$ with connected-fibre torus fibrations $g_s:Y_s\to C_s$
over smooth genus-two curves, whose Kodaira--Spencer tensors
have rank two at a regular value, such that the central map
$g_0$ has no holomorphic extension from this deformation to
the fixed curve $C_0$.""",
     "cdp:st:E10", "D03;D11",
     "State the proved projective family and its obstruction as a concrete result; the full Hesse-pencil, moving-branch and cohomology proof remains.")
edit("14", "therefore gives the actual bundles", "therefore identifies the bundles",
     "cdp:st:E11", "D08", "The explicit cyclic-cover and cusp comparison identifies the same equivariant bundles.")
edit("14",
     r"""Euler field $\Xi$. The integral marking of \SeriesRef{push:src:E.1.1}
gives $\gamma=-\psi$, where $\psi$ counts the forward generator
$\Phi_u=u\phi$ covering translation by $-6P$.""",
     r"""Euler field $\Xi$. Let $\psi$ count the forward generator
$\Phi_u=u\phi$ covering translation by $-6P$, and let
$\gamma=-\psi$. The inverse generator counts the clockwise
deck direction: inversion induces $n\mapsto-n$ on its deck
group $\mathbb Z$, which is its own inverse. For the $(3,4)$
family this is the marking of
\cref{def:II:marked-Picard-parameter}.""",
     "cdp:st:E11", "D14;D20",
     "Replace the later marking premise by the explicit isomorphism of deck character groups and its inverse; the scale derivative remains the same tensor.")

# Give every retained piece of the old unnumbered comparisons an owner.
start = units["14"].index("In the supplied CDP98 arXiv source")
end = units["14"].index(r"\begin{proposition}[The Kuranishi germ", start)
old_after_e12 = units["14"][start:end]
edit("14", old_after_e12, "", "cdp:st:E12", "D01;D04;D06;D12;D13;D17",
     "The exact counterexample to CDP98 Lemma1.5 and the full parameter base-change sequence remain in E12. Remove the source-use inventory and CompendiumRef; the known non-holomorphic theorem is restored at 01GR with its primary source and component map, and the degree-one structure-sheaf theorem is already cited at E5.",
     "unnumbered paragraph after E12")
edit("14", "All sufficiently small deformations\nretain a torus fibration", "All sufficiently small deformations\nadmit a torus fibration",
     "cdp:st:E14", "D08", "Use a direct mathematical existence statement.")
edit("14", "The rank-two hypothesis in \\ref{cdp:st:E6} is supplied for this",
     "The rank-two hypothesis in \\ref{cdp:st:E6} holds for this",
     "cdp:st:E14", "D08", "Use the already-proved rank condition directly.")
edit("14", "small deformations retain their torus fibration.", "small deformations admit torus fibrations.",
     "cdp:st:E14", "D08", "State the result positively.")
edit("14", "A locally miniversal family is supplied by all sufficiently nearby",
     "A locally miniversal family is parametrized by all sufficiently nearby",
     "cdp:st:E15", "D08", "Identify the parameter space mathematically.")
edit("14", r"\cite{Viaclovsky2026Combs}", r"\cite[Theorem~1.1, p.~2]{Viaclovsky2026Combs}",
     "cdp:st:E15", "D18",
     "The opened theorem states the m≥12 construction, topology, coherent dimensions and lower bound; the subsequent proof here computes the full tangent cohomology and Kuranishi germ.",
     all_matches=True)
edit("14", "This description does not require a global\nmanifold cover of the root curve.", "",
     "cdp:st:E15", "D02",
     "The preceding coarse Grassmannian charts, exact root lifting conditions and H1(A)=0 already give the complete section-germ construction.")
edit("14", "all $8m+1$ period directions and the specified central member.",
     "all $8m+1$ period directions and central member $X_m$.",
     "cdp:st:E15", "D08", "Name the central fibre.")
start = units["14"].index(r"\paragraph{Comparison with the constructed parameter space.}")
end = units["14"].index(r"\begin{proposition}[Rank divisors", start)
old_comb_comparison = units["14"][start:end]
comb_comparison = r"""\begin{corollary}[The inclusion of the comb germ with fixed period values]\hypertarget{tag-P264}{}\label{cor:II:comb-fixed-value-inclusion}
\StatementRecord{cor:II:comb-fixed-value-inclusion}{proved}{P264}{\SeriesRef{cdp:st:E15}; \cite[Lemma~8.2 and Proposition~8.3, pp.~27--28]{Viaclovsky2026Combs}}
For a positive comb of degree parameter $m$ in \cref{cdp:st:E15},
the germ of period sections whose values at the three critical
points are fixed embeds in the root-period germ of that proposition.
The differential is the inclusion in
\[
0\longrightarrow H^0\bigl(B,N(-p_0-p_1-p_2)\bigr)
\longrightarrow H^0(B,A)
\longrightarrow \mathbb C^4\oplus\mathbb C^3\oplus\mathbb C^2
\longrightarrow0,
\]
where $N=(\rho_*F)^*\otimes G_c$ and $A$ is the admissible
period-variation sheaf in the proof of \cref{cdp:st:E15}.
The respective dimensions are $8m-8$, $8m+1$ and $9$.
\end{corollary}

\begin{proof}
The fixed-value germ is constructed in
\cite[Lemma~8.2 and Proposition~8.3, pp.~27--28]{Viaclovsky2026Combs}.
The inclusion sends a marked period section to the same section
on the root curve. Its inverse on its image forgets the root
description and takes the coarse period plane. The local graph
conditions in \cref{cdp:st:E15} identify its differential with
the sheaf inclusion
\[
0\longrightarrow N(-p_0-p_1-p_2)\longrightarrow A
\longrightarrow
 \mathbb C_{p_0}^{4}\oplus\mathbb C_{p_1}^{3}
                     \oplus\mathbb C_{p_2}^{2}
\longrightarrow0.
\]
The first sheaf sets all four graph entries to zero at each
point. The sheaf $A$ imposes respectively zero, one and two
conditions, so the three quotient lengths are $4,3,2$.
The cited Lemma~8.2 gives
$H^1(B,N(-p_0-p_1-p_2))=0$ and the dimension formula
$4+4c_m-2h-4r$, where $c_m=\deg G_c$,
$h=\deg(\rho_*F)+\deg G_c$ and $r=3$.
By \cref{cdp:st:E15}, $c_m=2m-1$ and
$h=(-2m-1)+(2m-1)=-2$. Substitution gives $8m-8$.
The long cohomology sequence is therefore
the asserted exact sequence; its quotient has dimension nine,
and $8m-8+9=8m+1$.
\end{proof}

"""
edit("14", old_comb_comparison, comb_comparison, "cor:II:comb-fixed-value-inclusion", "D01;D08;D13;D14;D18",
     "Give the full morphism of parameter germs and its differential their own numbered corollary. Retain the exact sheaf quotient and all nine directions. Replace internal source labels by opened Lemma8.2/Proposition8.3 pp27–28; delete dated search history and unsupported novelty wording.",
     "unnumbered comparison after E15")

edit("14", "at the specified degenerate fibres", "at the degenerate fibres",
     "cdp:st:E16", "D08", "The statement immediately identifies the fibre types.")
edit("14", "For a specified positive comb section", "For a positive comb section",
     "cdp:st:E16", "D08", "The section itself is the mathematical input.")

old_e17 = statement_block(units["14"], "cdp:st:E17")
example_start = old_e17.index(r"\item Let $C=\mathbb P^1$")
example_end = old_e17.index(r"\item The descending spaces", example_start)
example_body = old_e17[example_start:example_end].replace(r"\item ", "", 1).rstrip()
new_e17 = old_e17[:example_start] + old_e17[example_end:]
new_e17 = new_e17.replace(
    "associated components and $D$ meets every irreducible component.",
    "associated components and $D$ meets every irreducible component,\n"
    r"as in \cite[Lemma~3.5, p.~10]{LRS2019}.", 1)
embedded_example = r"""\begin{example}[An embedded point surviving every divisor twist]\hypertarget{tag-P267}{}\label{ex:II:embedded-point-divisor-twist}
\StatementRecord{ex:II:embedded-point-divisor-twist}{proved}{P267}{\cite[Proposition~1.1, p.~78]{CDP98}}
There is a compact connected one-dimensional complex space $Z$
with one embedded associated point and an effective Cartier
divisor $D$ meeting its irreducible component such that
\[
h^0(Z,\mathcal O_Z(-kD))=\max(1-k,0)+1,\qquad
h^1(Z,\mathcal O_Z(-kD))=\max(k-1,0)
\]
for every integer $k$, and every higher cohomology group is zero.
\end{example}

\begin{proof}
""" + example_body + "\n" + r"\end{proof}" + "\n\n"
edit("14", old_e17, new_e17 + "\n\n" + embedded_example, "cdp:st:E17", "D13;D14;D17;D18",
     "Separate the complete square-zero example into owner P267. E17 retains the finite-dimensional stabilization, Krull intersection, associated-support criterion and the inverse analytic maps identifying every graph fibre with its full Cartier divisor. Cite the opened LRS Lemma3.5 for the no-embedded-component specialization; the complete support statement is the additional form proved here. No local ring or cohomology calculation is removed.")

audit_start = units["14"].index(r"\paragraph{Audit of the printed non-holomorphic proof.}")
audit_end = units["14"].index(r"\begin{proposition}[Theta determinants", audit_start)
old_audit = units["14"][audit_start:audit_end]
pencil_lemma = r"""\begin{lemma}[Higher images of the exceptional divisor of a pencil]\hypertarget{tag-P265}{}\label{lem:II:pencil-exceptional-thickenings}
\StatementRecord{lem:II:pencil-exceptional-thickenings}{proved}{P265}{}
Let $Y$ be a smooth compact complex threefold, and resolve a
meromorphic pencil without a fixed divisorial component by a
composition of blowups with smooth centres
$\sigma:\widehat Y\to Y$. Write $h:\widehat Y\to\mathbb P^1$
for the resolved map, $P$ for the line of the pencil, and $E$
for the effective divisor of its pulled-back base ideal, so that
\[
h^*\mathcal O_{\mathbb P^1}(1)
 =\sigma^*P\otimes\mathcal O_{\widehat Y}(-E).
\]
For every positive integer $t$ one has
\[
R^1\sigma_*\mathcal O_{tE}=R^2\sigma_*\mathcal O_{tE}=0.
\]
For every holomorphic vector bundle $W$ on $Y$,
$H^2(tE,\sigma^*W|_{tE})=0$.
\end{lemma}

\begin{proof}
A smooth blowup has structure-sheaf derived image equal to
the original structure sheaf; composition gives
$R\sigma_*\mathcal O_{\widehat Y}=\mathcal O_Y$.
Pull back the evaluation sequence for
$\mathcal O_{\mathbb P^1}(t)$ and tensor by $\sigma^*P^{-t}$.
It gives
\[
\begin{split}
0\longrightarrow&\bigl(\mathcal O_{\widehat Y}(E)\otimes
              \sigma^*P^{-(t+1)}\bigr)^{\oplus t}
 \longrightarrow(\sigma^*P^{-t})^{\oplus(t+1)}\\
 &\longrightarrow\mathcal O_{\widehat Y}(-tE)
 \longrightarrow0.
\end{split}
\]
Pullback preserves exactness because the evaluation sequence
has locally free quotient. The middle term has zero
$R^2\sigma_*$ by the projection formula. Every coherent sheaf
has zero $R^3\sigma_*$ since the fibres have dimension at most
two. The resulting direct-image sequence gives
$R^2\sigma_*\mathcal O_{\widehat Y}(-tE)=0$. Applying it to
\[
0\to\mathcal O_{\widehat Y}(-tE)\to
\mathcal O_{\widehat Y}\to\mathcal O_{tE}\to0
\]
gives the asserted degree-one and degree-two vanishings.
The support of $\sigma_*\mathcal O_{tE}$ is contained in the
base locus of the pencil, which has dimension at most one
because the pencil has no fixed divisorial component. The
projection formula identifies
$R\sigma_*(\mathcal O_{tE}\otimes\sigma^*W)$ with
$\sigma_*\mathcal O_{tE}\otimes W$ in degree zero. Leray and
the dimension of that support give the asserted second-cohomology
vanishing.
\end{proof}

"""
exceptional_example = r"""\begin{example}[An elliptic exceptional higher image]\hypertarget{tag-P266}{}\label{ex:II:exceptional-elliptic-direct-image}
\StatementRecord{ex:II:exceptional-elliptic-direct-image}{proved}{P266}{\cite[Example~3.4(2), p.~10]{LRS2019}}
Blow up a point $p\in\mathbb P^3$, then blow up a smooth
plane cubic $C$ in the exceptional $\mathbb P^2$. For the
second exceptional divisor $S$ and the composite map
$\sigma$ to $\mathbb P^3$, one has
\[
h^\bullet(S,\mathcal O_S)=(1,1,0),\qquad
R^1\sigma_*\mathcal O_S=\mathbb C_p.
\]
\end{example}

\begin{proof}
This construction is \cite[Example~3.4(2), p.~10]{LRS2019}.
The exceptional divisor is the projectivization of the rank-two
normal bundle of $C$ in the first blowup. Its projection
$r:S\to C$ is a $\mathbb P^1$-bundle, with
$r_*\mathcal O_S=\mathcal O_C$ and higher direct images zero.
The restriction of $\sigma$ to $S$ is the composite of $r$,
the map $C\to\{p\}$ and the closed inclusion
$\{p\}\hookrightarrow\mathbb P^3$. Since $C$ has genus one,
Leray gives the displayed cohomology and the length-one
skyscraper in degree one.
\end{proof}

"""
adjunction_remark = r"""\begin{remark}[Adjunction on a full Cartier fibre]\hypertarget{tag-P272}{}\label{rem:II:full-fibre-adjunction}
\StatementRecord{rem:II:full-fibre-adjunction}{proved}{P272}{\cite[p.~14, line following (3.5)]{LRS2019}}
For an effective Cartier divisor $F$ in a smooth threefold $Y$,
including a full nonreduced fibre, its dualizing line is
\[
\omega_F=(K_Y\otimes\mathcal O_Y(F))|_F.
\]
This corrects the sign of $F$ in the formula following
equation~(3.5) on p.~14 of \cite{LRS2019}.
\end{remark}

\begin{proof}
Apply $\mathcal Hom_Y(-,K_Y)$ to
$0\to\mathcal O_Y(-F)\to\mathcal O_Y\to\mathcal O_F\to0$.
Its degree-one cokernel is
$(K_Y\otimes\mathcal O_Y(F))|_F$.
Cartier duality identifies this cokernel
$\mathcal Ext^1_Y(\mathcal O_F,K_Y)$ with $\omega_F$.
The calculation uses the full nonzerodivisor equation of $F$.
\end{proof}

"""
edit("14", old_audit, pencil_lemma + exceptional_example + adjunction_remark,
     "lem:II:pencil-exceptional-thickenings", "D01;D02;D04;D06;D08;D12;D13;D17;D18",
     "Replace the unnumbered audit narrative by its three mathematical owners: the complete evaluation-sequence proof for pencil divisors, the opened exceptional-divisor example with its precise projective-bundle contraction, and Cartier adjunction with the Ext morphism proving the published sign correction. The known generic-vanishing proof is cited at restored E2; no CompendiumRef remains.",
     "unnumbered audit after E17")

for old, new, reason in [
    ("For the theta expression in", "For the theta expression in", ""),
    ("The determinant for the specified theta expression", "The determinant for this theta expression", "The preceding equation fixes the expression."),
    ("specified change of theta argument", "change of theta argument", "The equality ϑ(z,τ)=θ(πz|τ) is the explicit conversion."),
    ("the actual meromorphic section", "the meromorphic section", "The section and its divisor are explicitly displayed."),
    ("There is a specified relation to the symmetric period matrix", "We compare with the symmetric period matrix", "The following lattice inclusion and its index prove the comparison."),
    ("direct image. This specifies every cohomological degree without\nassigning finite dimensions to the holomorphic-function spaces\non a disc.",
     "direct image. These groups are the indicated spaces of\nholomorphic sections on the disc.",
     "State the complete cohomology description positively; the section spaces remain unchanged."),
    ("nonzero there. Extra holomorphic terms\nin a different linearization contribute their derivatives to\nthe determinant; they must be retained, just as the $\\wp$ term\nmust be retained when the section is not a zero of $\\wp$.",
     "nonzero there. Adding a holomorphic function $a(\\tau)$ to\nthe lower-right entry of $\\Omega$ adds $a'(\\tau)$ to\n$\\det\\Omega'$, because its upper-left derivative is one.",
     "Replace the repeated warning by the exact affine change Ω22↦Ω22+a and the induced determinant change.")
]:
    if old != new:
        edit("14", old, new, "cdp:st:E18", "D02;D08;D11", reason)

# Convert each inherited manual equation number, preserving every label/target.
for which in ("13", "14"):
    for match in list(re.finditer(r"\\\[(.*?)\\\]", units[which], re.S))[::-1]:
        old = match.group()
        if r"\tag{" not in old:
            continue
        body = re.sub(r"\s*\\tag\{[^}]+\}", "", match.group(1))
        new = r"\begin{equation}" + body + r"\end{equation}"
        prior = units[which][:match.start()]
        owners = re.findall(r"\\StatementRecord\{([^}]+)\}", prior)
        owner = owners[-1] if owners else "sec:II:" + which
        edit(which, old, new, owner, "D04;D19",
             "Use the paper's section equation counter and retain the exact mathematical payload, label and permanent hypertarget.")
    assert r"\tag{" not in units[which]

# Move the determinant before the integral and nonintegral resonance results.
e8 = statement_block(units["14"], "cdp:st:E8")
edit("14", e8, "", "cdp:st:E8", "D14",
     "Transport the complete theta-determinant statement and all four proof steps to the marked-period subsection before C5b/C5c.")
anchor = r"\begin{proposition}[Integral twists and the normalization-map exception]"
edit("12", anchor, e8 + "\n\n" + anchor, "cdp:st:E8", "D14",
     "Receive the complete determinant proof after the marked Picard definition and before the resonance calculations. Its degree-six identity-induced isogeny explicitly identifies the Kodaira–Spencer ranks.")
edit("12",
     r"""The weight-five section space is zero. The ranks in
\ref{cdp:st:E16} give $ab\ne0$ at the cusp and $c_0\ne0$ at
$p_1$.""",
     r"""The weight-five section space is zero. The isogeny in
\cref{cdp:st:E8} is induced by the identity on $\mathbb C^2$;
its differential and pullback on first complex cohomology
identify the Kodaira--Spencer tensors. At the cusp that
proposition gives rank two, so
$\det\kappa=-ab\,y^2\ne0$ and $ab\ne0$. At $p_1$ one has
$y=0$ and $x\ne0$; its rank-one conclusion gives
$c_0x\ne0$, hence $c_0\ne0$.""",
     "cdp:st:C5b", "D14;D22",
     "Replace the forward E16 premise by the earlier E8 isogeny/rank theorem. Evaluate the displayed weighted matrix at the cusp and at p1 to prove the exact nonzero constants used by its invertible frame maps.")

# Restore the missing full theorem owner from the opened primary source.
compendium = (ROOT.parent / "S6_GRIND_4_s6_09_compendium/S6_09_PAPERS_II.tex").read_text()
old_e2 = statement_block(compendium, "cdp:st:E2")
e2 = r"""\begin{cited}[The non-holomorphic reduction theorem]\hypertarget{tag-01GR}{}\label{cdp:st:E2}
\StatementRecord{cdp:st:E2}{proved}{01GR}{\cite[Theorem~3.1, arXiv v1, p.~9]{LRS2019}}
Let $Y$ be a smooth compact connected complex threefold with
$b_2(Y)=0$, and let $g:Y\dashrightarrow C$ be a nonconstant
meromorphic map to a compact nonsingular curve which does
not extend holomorphically. For every holomorphic vector
bundle $V$ on $Y$, a dense open subset of each component of
$\operatorname{Pic}(Y)$ satisfies
\[
H^q(Y,V\otimes L)=0\qquad(0\leq q\leq3).
\]
Consequently $\chi(Y,V\otimes L)=0$ for every
$L\in\operatorname{Pic}(Y)$, and $\int_Yc_3(Y)=0$.
\end{cited}

\begin{proof}
The vanishing on $\operatorname{Pic}^0(Y)$, the Euler-index
conclusion for every line in that component, and the third-Chern
conclusion are \cite[Theorem~3.1, arXiv v1, p.~9]{LRS2019}.
For a component represented by $L_*$, tensoring defines the
holomorphic isomorphism
\[
\operatorname{Pic}^0(Y)\longrightarrow
L_*\operatorname{Pic}^0(Y),\qquad Q\longmapsto L_*\otimes Q,
\]
with inverse $L\mapsto L_*^{-1}\otimes L$.
Apply the cited theorem to the holomorphic vector bundle
$V\otimes L_*$. The tensor associativity isomorphism
$(V\otimes L_*)\otimes Q\simeq V\otimes(L_*\otimes Q)$
identifies every cohomology group and every Euler index.
The component isomorphism carries the theorem's dense open
set to the claimed dense open set and proves the assertion
for every line in that component.
\end{proof}

"""
record(old_e2, e2, "cdp:st:E2", "D04;D06;D17;D18",
       "Read the complete attached compendium statement and graph proof and LRS arXiv v1 Theorem3.1/proof pp9–14. Restore its full theorem owner at the existing tag01GR. Cite the known proof and retain the exact extra Picard-component step via tensor translation and its inverse; the source applies to the arbitrary twisted vector bundle.",
       "../S6_GRIND_4_s6_09_compendium/S6_09_PAPERS_II.tex: former E2 owner; missing in current source")

# Assemble complete sections in premise order, retaining original header tags.
header13 = units["13"][:units["13"].index(r"\begin{proposition}")].strip()
order13 = ["cdp:st:D.2.1", "cdp:st:D.2.3", "cdp:st:D.2.5", "cdp:st:D.2.2", "cdp:st:D.2.4",
           "cdp:st:D.2.6", "rem:II:extended-torus-groups", "cdp:st:D.2.8"]
blocks13 = {key: statement_block(units["13"], key) for key in order13}
unowned13 = units["13"].replace(header13, "", 1)
for text in blocks13.values():
    unowned13 = unowned13.replace(text, "", 1)
assert not unowned13.strip(), "unowned material in section13"
section13 = header13 + "\n\n"
for i, key in enumerate(order13):
    if i == 0:
        section13 += r"\subsection{Components and the logarithmic period obstruction}" + "\n\n"
    if i == 2:
        section13 += r"\subsection{Euler equality and the normal-crossing subclass}" + "\n\n"
    if i == 5:
        section13 += r"\subsection{Extension of periods and coherent direct images}" + "\n\n"
    section13 += blocks13[key] + "\n\n"
record(units["13"], section13, "sec:II:13", "D14",
       "Put the logarithmic obstruction before the Euler upper bound, the general equality before its normal-crossing corollary, and the period-extension results together. Each complete statement and receiving proof is transported verbatim at this ordering step.",
       "complete section13 order")

all14owners = re.findall(r"\\StatementRecord\{([^}]+)\}", units["14"])
blocks14 = {key: statement_block(units["14"], key) for key in all14owners}
old14header = old14[:old14.index(r"\begin{proposition}")].strip()
unowned14 = units["14"].replace(old14header, "", 1)
for text in blocks14.values():
    unowned14 = unowned14.replace(text, "", 1)
assert not unowned14.strip(), "unowned material in section14"
groups = [
 ("section14_stability", r"\section{Fibration stability}\hypertarget{tag-034A}{}\label{sec:II:14}",
  ["cdp:st:E5", "cdp:st:E6", "cdp:st:E7", "cdp:st:E10"]),
 ("explicit_deformations", r"\section{Deformations of explicit torus fibrations}\hypertarget{tag-P268}{}\label{sec:II:explicit-deformations}",
  ["cdp:st:E11", "cdp:st:E13", "cdp:st:E14", "cdp:st:E15", "cor:II:comb-fixed-value-inclusion"]),
 ("period_rank", r"\section{Rank divisors and theta comparisons}\hypertarget{tag-P269}{}\label{sec:II:period-rank}",
  ["cdp:st:E16", "cdp:st:E18"]),
 ("direct_image_comparisons", r"\section{Direct images and divisor vanishing}\hypertarget{tag-P270}{}\label{sec:II:direct-image-comparisons}",
  ["cdp:st:E2", "cdp:st:E12", "cdp:st:E17", "ex:II:embedded-point-divisor-twist",
   "lem:II:pencil-exceptional-thickenings", "ex:II:exceptional-elliptic-direct-image",
   "rem:II:full-fibre-adjunction"])
]
blocks14["cdp:st:E2"] = e2.strip()
group_texts = {}
for name, header, keys in groups:
    group_texts[name] = header + "\n\n" + "\n\n".join(blocks14[key] for key in keys) + "\n\n"
all_sections14 = "".join(group_texts.values())
record(units["14"], all_sections14, "sec:II:14", "D14",
       "Divide the long deformation section into stability, explicit Kuranishi germs, rank divisors/theta comparison, and direct-image/divisor results. The complete E8 block has already moved before resonance; E13 precedes E14/E15, which precede E16; the restored E2 is a cited owner. Every remaining proof is transported in full.",
       "complete section14 order and section division")
part_header = r"""\part{Periods, tangent cohomology and deformations}\hypertarget{tag-P271}{}\label{part:II:periods-tangent-deformations}
The Euler-sign theorem determines the global topological
constraint on the fibrations considered here. We next study
their coherent cohomology and variation: fixed-fibre sections
and normalization maps, period extension under trivial
monodromy, resonance of Picard twists, and local deformation
spaces. These computations identify the cohomological
mechanisms of the constructed families and the hypotheses
needed for their direct-image comparisons.

"""
whole = part_header + units["12"].rstrip() + "\n\n" + section13 + all_sections14
record("", part_header, "part:II:periods-tangent-deformations", "D14;D24",
       "Create the clearly titled later part with one paragraph explaining its relation to the Euler-sign theorem. Root places the entire fragment after the sign-theorem development, so D.2.2's general lower bound is already available.",
       "new later-part header after the Euler-sign development")

# Bounded structural guards are not a manuscript census or a mathematical check.
old_targets = re.findall(r"\\hypertarget\{(tag-[^}]+)\}", old12proposal + old13 + old14)
old_labels = re.findall(r"\\label\{([^}]+)\}", old12proposal + old13 + old14)
new_targets = re.findall(r"\\hypertarget\{(tag-[^}]+)\}", whole)
new_labels = re.findall(r"\\label\{([^}]+)\}", whole)
assert all(new_targets.count(x) == old_targets.count(x) for x in old_targets), "lost or duplicated old target"
assert all(new_labels.count(x) == old_labels.count(x) for x in old_labels), "lost or duplicated old label"
assert len(new_targets) == len(set(new_targets)), "duplicate target"
assert len(new_labels) == len(set(new_labels)), "duplicate label"
assert r"\CompendiumRef" not in whole
assert r"\tag{" not in whole
assert whole.count(r"\label{cdp:st:E8}") == 1
assert whole.count(r"\label{cdp:st:E2}") == 1
assert whole.index(r"\label{cdp:st:E8}") < whole.index(r"\label{cdp:st:C5b}") < whole.index(r"\label{cdp:st:C5c}")
assert whole.index(r"\label{cdp:st:D.2.2}") < whole.index(r"\label{cdp:st:D.2.4}")
assert not re.search(r"P4R\.13|P4\.40", old12proposal + old13 + old14 + whole)
guard_rows = [dict(statement_id=key, statement_sha256=digest(statement_only(MAIN, key)),
    status="Outside all receiving fragments; statement untouched by this proposal.")
    for key in ("push:src:E.5.2", "push:src:E.5.3")]
write_tsv(OUT / "S6_SERIES_PUBLISH_later_statement_guards.tsv", guard_rows)

(OUT / "S6_SERIES_PUBLISH_section12_final_proposed.tex").write_text(units["12"])
(OUT / "S6_SERIES_PUBLISH_section13_proposed.tex").write_text(section13)
for name, text in group_texts.items():
    (OUT / f"S6_SERIES_PUBLISH_{name}_proposed.tex").write_text(text)
(OUT / "S6_SERIES_PUBLISH_later_part_proposed.tex").write_text(whole)

reviewed = argparse.ArgumentParser()
reviewed.add_argument("--reviewed", action="store_true")
reviewed = reviewed.parse_args().reviewed
if reviewed:
    for row in rows:
        row["review_status"] = "Complete original and receiving owner proofs read; exposed editorial comparison, not an independent derivation."
write_tsv(OUT / "S6_SERIES_PUBLISH_later_defects.tsv", rows)

notes = {
 "cdp:st:C4c": "Recompared the complete finite-fibre criterion proof while replacing three process phrases. The full Cartier-fibre definition, base twist in the same Picard component, endpoint loci, Leray converse and fixed-fibre irreducibility argument are unchanged.",
 "cdp:st:C4f": "Recompared the complete criterion proof while deleting two process adjectives. The same full-thickening subsheaf injection, normalization submodule, torsion R2 sheaf and Picard-line continuation prove the same two implications and all-twist nonvanishing.",
 "cdp:st:D.2.1": "Compared the full component-count and Kähler-resolution proof: base genus by pullback, rank-four invariants, r=s+3 and C.3.4; its hypotheses and conclusions are unchanged.",
 "cdp:st:D.2.3": "Compared all twelve logarithmic-period steps, including the analytic Steenbrink hypotheses, zero residue, branch residue subtraction, annular L2 divergence, J/(t) monomial eigenvalues, hypercohomology endomorphism, division by t, full multiplicities and Λ2H1→H2. The proof is retained verbatim.",
 "cdp:st:D.2.5": "Compared all seven steps: positive index gives b3=0; C4c gives a fixed full fibre; root cover and irrational unitary class exclude smooth support; finite ideal layers and analytic Picard loci give fixed j; the Gauduchon bound and effective conductor give pg=0; analytic embedded resolution preserves pg=0 of every component; D.2.3 contradicts identity monodromy. The source version and exact root-cover owner are now explicit.",
 "cdp:st:D.2.2": "Compared the full proof: C.2.G.1 lower bound and D.2.5 upper bound imply c3=0; Poincaré duality gives b3=2; the sum of nonnegative fibre Euler numbers gives each equality case; D.2.7 supplies the integral example. Only a duplicate forward preview is removed.",
 "cdp:st:D.2.4": "Compared both complete old steps with the receiving corollary proof. The identity maps on Y, its base and each full Cartier fibre take its normal-crossing hypotheses into D.2.2. D.2.2 therefore proves the same Euler and b3 equalities with all multiplicities; D.2.7 realizes the subclass.",
 "cdp:st:D.2.6": "Compared all five steps of the admitted period-extension proof, including embedded resolution, positivity/L2 bounds, the invariant lattice and the limiting Hodge plane. It is transported intact.",
 "rem:II:extended-torus-groups": "Compared the complete admitted remark and its proof: the Hodge quotient defines the extended compact torus group; its explicit lattice quotient and the contradiction to the stated Albanese morphism remain unchanged.",
 "cdp:st:D.2.8": "Compared the entire coherent-direct-image proof: local freeness, the framed period quotient, integral annular gluing, torsion representatives and avoidance of the countably many Picard exceptional loci. The proof is transported intact.",
 "cdp:st:E5": "Compared both proof steps: Leray edge map, cup product with κ, the rank-two boundary, locally free R1 source and all three critical-image ideals. The mathematics is unchanged; the ending defensive restatement is removed.",
 "cdp:st:E6": "Compared all eleven steps, including the torus Beltrami lift, surjective H1 embedding map, map-obstruction cocycle, Cartier-divisor restriction, rank-two dense locus, absolute Douady graphs over nilpotents, free-complex unit splitting, isomorphism open locus, formal-to-analytic smoothness and torus identification. Opened Horikawa pp649,660–661, Douady §§9–10 pp83–87 and Buchdahl Theorem11 p297 at their used scopes.",
 "cdp:st:E7": "Compared the full four-step rank and stability proof. The flat-to-logarithmic frame gives qZ′→B/(2πi), and all cited fillings have the explicit independent valuation columns. Added exact opened proposition/page locators.",
 "cdp:st:E8": "Compared all four theta-determinant steps before moving them: identity-induced index-six lattice isogeny, heat/product/quasiperiod equations, zero-branch modular derivative, exact root orders and the rank-two logarithmic limit. Removed Lead9 and opened every cited DLMF equation, Atkin–Garvan eq3.5 p8 and AC Remark3.12 p19. The rank result now precedes its resonance uses.",
 "cdp:st:C5b": "Recompared all six receiving steps after changing the rank premise. E8's isogeny induces isomorphisms on Lie and H1; detκ=−ab y² at the cusp gives ab≠0 and κ at y=0,x≠0 gives c0≠0. Every subsequent frame inverse, module quotient, cusp extension, stabilizer invariant, Leray and semigroup calculation is retained.",
 "cdp:st:E10": "Compared all four steps of the projective example: the disjoint Hesse critical sets, moving sixth branch value, nonzero genus-two Kodaira–Spencer class, direct-image table and injective target obstruction. The statement now names exactly this family and obstruction.",
 "cdp:st:E11": "Compared all four steps for every coprime 3k,4l and the affine twists: weighted root morphism, equivariant E/G pullback, cohomology and monomial degree argument, explicit scale tensor and zero Kuranishi ideal. The later marking reference is replaced by the involution n↦−n of the deck group and γ=−ψ.",
 "cdp:st:E12": "Compared both full steps: the Poincaré line's moving simple zero, Rp*P=C0[−1], P1 degree−2 tensor shift, all fibre cohomology and the exact parameter base-change sequence. The unnumbered source-use inventory is removed; the exact published correction remains in the theorem.",
 "cdp:st:E13": "Compared all nine steps of the two-parameter Kuranishi proof, including the connection/residues, order-four frame, E=G pairing, logarithmic tangent cohomology, rank-two residue matrix, independent cross-ratio and scale derivatives, and the zero Kuranishi ideal. The complete proof is transported intact.",
 "cdp:st:E14": "Compared all thirteen steps: the invertible Weierstrass coordinate comparison, ε-family and contraction, canonical/root frames, local freeness over (t,ε), cusp module, critical double cover, explicit jet map of determinant i, independent scale/transverse derivatives and Kuranishi ideal. Exact LR source pages added; the proof remains complete.",
 "cdp:st:E15": "Compared all nine steps for positive combs, including root characters, coarse degrees, product defects, cohomology, period-variation sheaf, unobstructed section germ, holomorphic fillings with varying limiting planes, annular gluing, injective Kodaira–Spencer map and zero Kuranishi ideal. The full comparison to the published germ is assigned to P264.",
 "cor:II:comb-fixed-value-inclusion": "Compared the complete original comparison and receiving corollary: identity on marked sections and coarse descent give the germ inclusion and inverse on its image; local graph conditions give quotient lengths4,3,2; opened Lemma8.2 gives H1=0 and dimension8m−8, hence exactly nine additional tangent directions.",
 "cdp:st:E16": "Compared all five rank-divisor steps: chain rule for higher root covers, degree12 determinant for the two-parameter family, fourth-order LR determinant, comb character/degree formula y²P(x4,y3), and full Grassmann-frame covariance. Manual equation numbers become section numbers with labels/tags preserved.",
 "cdp:st:E17": "Compared the complete old owner and both receiving owners. The proposition keeps the stabilization/support theorem and exact graph-fibre ring isomorphism; all square-zero construction and cohomology data move to P267.",
 "ex:II:embedded-point-divisor-twist": "Compared the entire transported square-zero example: local ring C{z,e}/(ze,e²), Cartier point away from the embedded point, split twist and every cohomology dimension. The exact CDP98 Proposition1.1 correction remains.",
 "lem:II:pencil-exceptional-thickenings": "Compared the entire old pencil-divisor calculation with the numbered lemma. Pullback of the O(t) evaluation sequence with its locally free quotient gives R2O(−tE)=0; the divisor sequence gives R1/R2O_tE=0; the base-ideal image has dimension≤1 and the projection formula gives H2(tE,σ*W)=0.",
 "ex:II:exceptional-elliptic-direct-image": "Opened LRS Example3.4(2) p10 and compared the full old example with the receiving one. The explicit composition S=P(N_C)→C→p identifies its cohomology and length-one R1 skyscraper. No unsupported category comparison is asserted.",
 "rem:II:full-fibre-adjunction": "Compared the published p14 sign error and the receiving correction. Applying Hom(−,K_Y) to the full Cartier divisor sequence identifies Ext1 with K_Y(F)|F and then with ωF; the calculation includes nilpotents and multiplicities.",
 "cdp:st:E2": "Read the complete attached compendium owner and LRS v1 Theorem3.1/proof pp9–14. Its arbitrary-vector-bundle theorem proves the Pic0 conclusions; tensoring by L* and its inverse is the explicit holomorphic map transporting all cohomology groups to each Picard component. The restored cited owner retains tag01GR and the entire statement.",
 "cdp:st:E18": "Compared all six steps: theta half-period multipliers, degree-zero line and contracting quotient, index-six isogeny, positive theta-constant determinant, direct-image boundary ranks and all holomorphic section-space cohomology. The variation Ω22↦Ω22+a gives the exact determinant correction a′."
}
event_fields = next(csv.reader((ROOT / "CHECK_EVENTS.tsv").open(), delimiter="\t"))
events = []
date = datetime.now(timezone.utc)
if reviewed:
    for owner, note in notes.items():
        row = {field:"" for field in event_fields}
        row.update(statement_id=owner, date=date.date().isoformat(),
            who="GPT-6 Astra (OpenAI), ChatGPT Pro mode; inherited effort not separately exposed; continuation3 provenance",
            type="used and rechecked in this run",
            outcome=note + " This is an exposed complete-proof/editorial comparison, not an independent derivation or final PDF reading.",
            event_id="publish:c3:later:" + owner, phase="publication text and proof comparison",
            source_file="agents/continuation3_provenance/later_part/S6_SERIES_PUBLISH_later_CHECK_EVENTS.tsv",
            source_event_type="used and rechecked in this run",
            evidence_group="publish:c3:later:" + owner,
            date_utc=date.isoformat(),
            where="sec:II:12/13/14 receiving later part; complete old and receiving owner comparison")
        events.append(row)
write_tsv(OUT / "S6_SERIES_PUBLISH_later_CHECK_EVENTS.tsv", events, event_fields)
status = dict(unit="sec:II:12,sec:II:13,sec:II:14 and restored E2",
    original13_sha256=digest(old13), original14_sha256=digest(old14),
    prior12proposal_sha256=digest(old12proposal), receiving_part_sha256=digest(whole),
    proposal="S6_SERIES_PUBLISH_later_part_proposed.tex", edit_rows=len(rows),
    comparison_completed=reviewed, exposed_comparison_events=len(events),
    original_full_proofs_read=True, shared_files_written=False, final_pdf_read=False,
    required_check_gate_recounted=False, manuscript_census_refreshed=False,
    E52_E53="Both statements outside this proposal; exact source statement hashes recorded.",
    refined_P4R13_P440="No direct use in any of the three bounded original sections or receiving fragments.",
    new_tags={"P264":"cor:II:comb-fixed-value-inclusion", "P265":"lem:II:pencil-exceptional-thickenings",
      "P266":"ex:II:exceptional-elliptic-direct-image", "P267":"ex:II:embedded-point-divisor-twist",
      "P268":"sec:II:explicit-deformations", "P269":"sec:II:period-rank",
      "P270":"sec:II:direct-image-comparisons", "P271":"part:II:periods-tangent-deformations",
      "P272":"rem:II:full-fibre-adjunction"},
    restored_tag={"01GR":"cdp:st:E2"},
    remaining=["Root admits complete fragment after the Euler-sign development, updates organization/front references, regenerates series references and renders.",
      "Root computes final text/event counts and page concordance only at the final manuscript state."],
    source_files="All primary PDFs/HTML remain outside the checkpoint; metadata and own paraphrases only.")
class_notes = {
 "D01":"Delete the source-use audit narrative and dated novelty-search history; keep exact neutral corrections of published CDP/LRS claims.",
 "D02":"Replace defensive clauses by the actual image ideals, nilpotent-germ argument and explicit determinant variation.",
 "D03":"Remove Lead9; state the concrete Hesse/genus-two family and its exact obstruction.",
 "D04":"Remove all bounded CompendiumRefs and the bare A.3.4; existing tags and labels are preserved.",
 "D05":"Remove Lead9; all surviving inputs are defined mathematical objects or exact cited results.",
 "D06":"Restore the full missing E2 owner at01GR; its source and all component maps are explicit.",
 "D07":"No worker/model/run language occurs in the bounded receiving mathematical text.",
 "D08":"Replace process uses of actual, specified, supplied and retain; mathematical meanings such as an original lattice in an explicit inclusion remain.",
 "D09":"No program/file/hash/bookkeeping path occurs in these bounded mathematical sections; program139 is a separate appendix-only proposal.",
 "D10":"Closed gate preserved: StatementRecord remains the established tag-only renderer; no machine navigation restored.",
 "D11":"Remove repeated scope defences; the actual parameter domains, singularities, multiplicities and full analytic germs remain stated.",
 "D12":"Use the identity-map specialization for D.2.4; delete duplicate previews and known proof inventories; retain each substantive new proof once.",
 "D13":"Assign the comb germ, square-zero example, pencil-divisor calculation, elliptic exceptional example and adjunction correction numbered owners.",
 "D14":"Move E8 before C5b/C5c, general Euler equality before its specialization, E13 before E14/E15 before E16; divide the long deformation block and place the whole part after the sign theorem.",
 "D15":"Front methodology/literature edits001–134 already admitted separately; this bounded pass adds no process prose to the mathematical body.",
 "D16":"Closed gate preserved: existing result titles retained; every genuinely added owner has a mathematical title.",
 "D17":"E2 cites the opened known theorem and proves only its precise component extension. The previously unnumbered proof inventory is removed; retained primary comparisons give the form needed here.",
 "D18":"Opened the used primary loci and supplied precise pages/equations and arXiv versions where required.",
 "D19":"All inherited manual D.S/E.16 equation numbers replaced by section counters; exact labels, payloads and hypertargets retained.",
 "D20":"Clockwise and forward deck characters related by the explicit involution n↦−n; the theta and lattice conventions retain their exact conversion maps.",
 "D21":"All retained determinant, rank, cohomology and dimension results are exact analytic/algebraic calculations, with no numerical agreement offered as proof.",
 "D22":"The nonzero constants a,b,c0 are justified immediately from the earlier E8 tensor ranks and the exact weighted matrix evaluations.",
 "D23":"Restore Čech accent; typesetting of all receiving fragments remains for root's integrated PDF reading.",
 "D24":"The later-part paragraph describes the receiving order; root must update the global §1.6 to that order.",
 "D25":"Read the complete inference chains. The LRS adjunction sign correction is proved by Ext; no additional uncorrected mathematical defect was found in the bounded comparison."
}
status["all_class_pass"] = {key:dict(status=value, exact_edit_rows=sum(key in r["type"].split(";") for r in rows)) for key,value in class_notes.items()}
(OUT / "S6_SERIES_PUBLISH_later_status.json").write_text(json.dumps(status, indent=2)+"\n")
(ROOT / "code/S6_SERIES_PUBLISH_c3_provenance_later_part.out").write_text(json.dumps(status, indent=2)+"\n")
print(json.dumps({key:status[key] for key in ("edit_rows", "comparison_completed", "exposed_comparison_events", "receiving_part_sha256", "shared_files_written")},indent=2))
