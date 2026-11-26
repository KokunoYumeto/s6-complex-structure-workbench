"""Publication edit of the wholly read repaired canonical-star unit."""
import csv
from datetime import datetime, timezone
from pathlib import Path

import S6_SERIES_PUBLISH_c8_integrate_presentation as presentation

root = Path(__file__).resolve().parent.parent
path = root / "agents/continuation8_iii_integration/units/weighted/canonical_star_logs.tex"
lane = root / "agents/continuation8_iii_weighted_units"
original = path.read_text()
text = original
edits = []


def replace(old, new, kinds, reason, count=1):
    global text
    assert text.count(old) == count, (old[:120], count, text.count(old))
    for _ in range(count):
        start = text.index(old)
        edits.append((kinds, text.count("\n", 0, start) + 1, old, new, reason))
        text = text[:start] + new + text[start + len(old):]


replace(r"""\begin{theorem}[unbounded canonical star logs with the full integral boundary map]\hypertarget{tag-02LQ}{}\label{maps:src:D.2.49}
\textnormal{\small tag 02LQ.}


Let a marked zero-free star boundary have the integral basis
""", r"""\begin{definition}[Canonical star data]\hypertarget{tag-Q201}{}\label{maps:def:canonical-star-data}
{\normalfont\scriptsize tag Q201}\par
Let a marked star boundary with nonvanishing line linearization have
the integral basis
""", "D10;D13;D14;D16;D20", "Put the complete marked input in a numbered definition before its realization theorem; zero-free means the line linearization is nonvanishing.")
replace(r"""There are twelve marked star positions of this type
in the natural catalogue: the eight primitive-gamma $I_1^*$
positions of \ref{maps:src:D.2.27} and the four primitive-gamma $I_3^*$
positions. Their unimodular bases are given in the proof.
The conclusions hold for every marked boundary with the displayed basis.

Take a root of order $m=2k$, with $k>0$. Its rank-one
semistable Mumford cap has $q=nk$ components. Let its affine
deck action on their cyclic labels be
$i\mapsto j-i$, with a marked integer lift $j\in\mathbb Z$.
The component labels use $j$ modulo $q$; its integer lift is
part of the peripheral marking. Write its collapsed
power as
""", r"""Choose integers $k>0$, $j,r,N$, set $m=2k$ and $q=nk$, and
prescribe the component action $i\mapsto j-i$ on $\mathbb Z/q$.
The integer lift $j$ is part of the peripheral marking.
The prescribed collapsed power is
""", "D11;D13;D14;D26", "Place all root-order, integer-lift and affine-power input together. Move the proved twelve-position count into the theorem, without altering the arbitrary-boundary domain.")
replace(r"""Every $j,r$ and every such $N$ is realized by a free
affine root action. Its maps include the holomorphic unit factors
and integer affine twists. Put
""", r"""These choices constitute \emph{canonical star data}.
\end{definition}

\begin{theorem}[Canonical star logarithms]\hypertarget{tag-02LQ}{}\label{maps:src:D.2.49}
{\normalfont\scriptsize tag 02LQ}\par
Every datum of Definition~\ref{maps:def:canonical-star-data} is realized
by a free affine root action on a rank-one semistable Mumford cap with
$q=nk$ components. The action has the prescribed component reflection
and collapsed power, with its holomorphic unit factors and integer twists.

There are twelve such marked star positions in the natural catalogue:
the eight primitive-gamma $I_1^*$ positions of
\ref{maps:src:D.2.27} and the four primitive-gamma $I_3^*$ positions.
Their unimodular bases are given in the proof.
Put
""", "D10;D13;D14;D16", "Give one realization theorem after its input definition, retaining all twelve natural positions and the larger marked-boundary scope.")
replace(r"the \emph{full} boundary kernel is as follows:", "the boundary kernel is", "D08", "State the exact kernel directly; every torsion coordinate remains in its three-row formula.")
old_scope = r"""The sole-log clause uses a minimal filling at every
other site. At $50/IV,(a,b_0)=(1,12)$ the nonzero-Chern
original $IV$ cap is not that choice; its minimal alternative
introduces another finite logarithm, handled by the full
insertion formula above. All six stated default examples
have their required other minimal multiplicative caps.

"""
replace(old_scope, "", "D11;D14;D22;D26", "Move this exact admitted cap-scope explanation next to the sole-log result, where the case is first used; its mathematical content is retained there.")
replace(r"""There is also a closed all-order result when this is the
sole logarithmic cap and every other cap has the minimal
natural marking of \ref{maps:src:D.2.26}, with no extra regular logs.
Write the initial coefficient as $b_0=4B$, and let $e$
""", r"""At a natural position, take this as the sole logarithmic cap
and use the minimal natural marking of \ref{maps:src:D.2.26} at
every other site, with no additional regular logarithms.
For the $\mathrm{OS50/IV}$ position with $(a,b_0)=(1,12)$, the
minimal $IV$ filling is a second finite logarithm; the general
bar insertion above computes that construction. The six default
examples below use minimal multiplicative fillings at their other sites.

For the sole-logarithm construction write $b_0=4B$, with
$B\in\mathbb Z_{>0}$, and let $e$
""", "D08;D11;D14;D22;D26", "State the existing sole-logarithm domain and its already admitted OS50/IV minimal-cap exception at the point of use. The general insertion remains applicable there; no new restriction or theorem is introduced. B is positive integral because the displayed natural data have b0=4 or12.")
replace("the six default natural rows with $b_0=4$ admit the", "the six default natural positions with $b_0=4$ admit the", "D04;D08", "Use the mathematical marked positions rather than input-row terminology.")
replace(r"simply connected choice $s=\pm1$, $k=2h$, $j$ even.", r"simply connected choice $s=\pm1$, $k=2h$ with $h>0$, and $j$ even.", "D22;D26", "Expose the positive h range already equivalent to k=2h and k>0.")
replace("Selected positions in the table are numbered from one.", r"The selected fibre labels are their positions, starting at one, in the ordered fibre lists of \ref{maps:src:D.2.19}.", "D04;D09;D20", "Identify the positions as mathematical fibre labels in the marked ordered lists, with the exact same indexing convention.")
replace(r"""46&2,3,4&(1,4)&3\\
46/II&3&(1,4)&3\\
50&2&(1,4)&1\\
50&3,4&(1,12),(3,4)&1\\
50/II&2&(1,4)&1\\
50/IV&3&(1,12),(3,4)&1 .
""", r"""\mathrm{OS46}&2,3,4&(1,4)&3\\
\mathrm{OS46/II}&3&(1,4)&3\\
\mathrm{OS50}&2&(1,4)&1\\
\mathrm{OS50}&3,4&(1,12),(3,4)&1\\
\mathrm{OS50/II}&2&(1,4)&1\\
\mathrm{OS50/IV}&3&(1,12),(3,4)&1 .
""", "D04;D20", "Use the catalogue's full mathematical profile names; the underlying profiles and marked positions are unchanged.")
replace("At $50/II$ apply", r"At $\mathrm{OS50/II}$ apply", "D04;D20", "Use the same profile name as the marked-position table.")
replace(r"""We distinguish the geometric complex-oriented classes from the
following transported homology coordinates:
""", r"""Use the following integral change from the complex-oriented classes
to homology coordinates:
""", "D02;D08;D20", "Introduce the explicit involution directly; its relation transport and inverse are retained in full.")
replace(r"""presentation, with no omitted degree-one bridge.
""", "presentation.\n", "D02", "The preceding injectivity proof already proves exactness, so remove the defensive clause.")
replace("Their literal origin-normal tori give the Wang section", "Their marked origin-normal tori give the Wang section", "D08", "Identify the positive geometric origin marking without a contrastive adjective.")
replace(r"\rm old", r"\rm red", "D01;D20", "Rename the j0 reduced-component frame by red. The map D=D_red, L=L_red−hnw and inverse addition already prove the exact transport.", count=2)
replace(r"{0,\rm old}", r"{0,\rm red}", "D01;D20", "Use the same reduced-component-frame notation for the conductor class; its exact order-two change and inverse are retained.", count=2)
replace("Thus \\eqref{maps:eq:D.SL22}, in the old conductor marking,", "Thus \\eqref{maps:eq:D.SL22}, in the reduced-component conductor marking,", "D01;D20", "Name the geometric frame by its defined j0 component representative, rather than a temporal adjective.")
replace("This proves all three asserted indices without saturation.", "These are the three projected indices in \\eqref{maps:eq:D.SL5}.", "D02;D08", "The surjective residue rows prove the exact integral indices; remove redundant defensive wording.")
replace("a literal normal at the site has coordinates", "a marked origin normal at the site has coordinates", "D08", "Use the already defined origin-normal marking.")
replace("Hence all other proved cap and finite", "Hence the other cap and finite", "D08", "Cite mathematical cap maps without proof-status vocabulary.")
replace("For the six default $b_0=4$ rows choose", "For the six default $b_0=4$ positions choose", "D04;D08", "Use the marked-position terminology consistently in the specialization proof.")
replace("\n\n\n\n\n", "\n", "D23", "Remove the extra blank lines inherited at the end of the extracted unit.")

headers, changes, issues = presentation.statement_records_to_small_tags(text)
assert not changes and not issues
candidate, changes, issues, aliases = presentation.remove_manual_equation_tags(headers)
assert not changes and not issues
assert not presentation.unresolved_literal_equation_references(candidate, aliases)
presentation.units.check_permanent_identifiers(original, candidate,
    allowed_labels=("maps:def:canonical-star-data",), allowed_targets=("tag-Q201",))
assert candidate.count(r"\begin{definition}") == 1
assert candidate.count(r"\begin{theorem}") == candidate.count(r"\begin{proof}") == 1
assert "\r" not in candidate
fields = ["change_id", "type", "statement_id", "old_location", "old_page", "new_location", "new_page", "old_text", "new_text", "reason", "review_status"]
records = []
for number, (kinds, line, old, new, reason) in enumerate(edits, 1):
    for kind in kinds.split(";"):
        records.append([f"III-C8-LQ-PUB-{number:03}-{kind}", kind, "maps:src:D.2.49",
            f"canonical_star_logs.tex, sequential edit at line {line}", "pending page concordance",
            "weighted/canonical_star_logs.tex", "pending final build", old, new, reason,
            "source edit; whole publication readback and root admission pending"])
with (lane / "S6_SERIES_PUBLISH_LQ_publication_defects.tsv").open("w", newline="") as stream:
    writer = csv.writer(stream, delimiter="\t", lineterminator="\n")
    writer.writerow(fields)
    writer.writerows(records)
path.write_text(candidate, newline="\n")
print("UTC", datetime.now(timezone.utc).isoformat())
print("UNIT_LINES", len(original.splitlines()), "->", len(candidate.splitlines()))
print("SEQUENTIAL_EDITS", len(edits), "DEFECT_ROWS", len(records), "NEW_ID", "Q201 / maps:def:canonical-star-data")
print("ALL_OLD_IDENTIFIERS_PRESERVED; helper changes0; unresolved0")
print("SHARED_WRITES0; AUTOMATIC_CRITERION_CREDIT0; INDEPENDENT_CHECK_CREDIT0")
