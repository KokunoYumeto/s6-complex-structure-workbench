"""Apply root-authored Paper III unit edits and log each change in defects.

This program edits the active source fragments. It does not refresh any derived
inventory, assign review credit, or close a publication criterion.
"""
from __future__ import annotations

import argparse
import csv
csv.field_size_limit(16 * 1024 * 1024)
from datetime import datetime, timezone
from pathlib import Path
import re

import S6_SERIES_PUBLISH_c8_integrate_units as units

ROOT = units.ROOT
WORK = units.WORK / "root"
DEFECTS = ROOT / "S6_SERIES_PUBLISH_defects_III.tsv"

COMMON = r"""\section{Conventions and the marked family}\hypertarget{tag-034J}{}\label{sec:III:conventions}

\begin{definition}[The marked family]
\hypertarget{tag-Q000}{}\label{mapsIII:def:marked-family}
{\normalfont\scriptsize tag Q000}\par
We use the marked $(3,4,\infty)$ family over
$B=\mathbb P^1_t$, with $(p_1,p_2,p_0)=(0,1,\infty)$.
Its regular-fibre lattice is
\[
 \Lambda=\mathbb Z\langle\widehat\gamma,\widehat u,
                              \widehat w,\widehat\delta\rangle,
\]
and $\gamma$ is the covector dual to $\widehat\gamma$.
The homology transport matrices are $A_1,A_2,M_0$, with
$A_1A_2M_0=I$. Base meridians are counterclockwise; the analytic
root generators satisfy
\[
 s_j(g_jz)=e^{-2\pi i/m_j}s_j(z),\qquad
 (m_1,m_2)=(3,4),\qquad g_1g_2g_0=1.
\]
The multiple fibres have $f^*p_j=m_jS_j$, and
$W=f^{-1}(p_0)$ is the reduced cusp. The standard twists are
\[
 v_1=(1,2,-4,0)^t,\qquad v_2=(-1,-3,3,0)^t.
\]
For general twists we write $p=12\ell_0-4\ell_1-3\ell_2$.
Admissibility requires $3\nmid\ell_1$ and $2\nmid\ell_2$;
hence $p$ is prime to six.
All homology and cohomology groups have integral coefficients
unless another coefficient group is displayed. Orientations are
the complex orientation, outward stabilization, and the stated
order of normal coordinates.
\end{definition}

\begin{remark}[Transport and dual coordinates]
\hypertarget{tag-Q001}{}\label{mapsIII:rem:dual-transport}
{\normalfont\scriptsize tag Q001}\par
For a homology transport $x\mapsto Ax$, parallel transport of
a covector column is $\alpha\mapsto T\alpha$, where
$T=A^{-t}$: the identity
\[
 (T\alpha)^t(Ax)=\alpha^tx
\]
preserves evaluation, and the inverse transport is $\alpha\mapsto
A^t\alpha$. The pullback by the map inducing $A$ on homology
is also written explicitly as $\alpha\mapsto A^t\alpha$.
In fibre calculations, a coordinate tuple $(g,u,w,d)$ denotes
$g\widehat\gamma+u\widehat u+w\widehat w+d\widehat\delta$;
its inverse sends a cycle to its four coefficients in this basis.
\end{remark}

\begin{definition}[Period parameters]
\hypertarget{tag-Q002}{}\label{mapsIII:def:period-parameters}
{\normalfont\scriptsize tag Q002}\par
The period matrix and its scalar parameter are
\[
 \Pi_c=\begin{pmatrix}6\mu&\tau&1&0\\
             \beta^{\rm part}+c&\mu&0&1\end{pmatrix},
 \qquad w=e^{-\pi i c}.
\]
We use the normalization $(\beta^{\rm part}+\tau)(p_0)=0$ and set
\[
 D_{\rm part}=\operatorname{Im}\beta^{\rm part}
       -\frac{6(\operatorname{Im}\mu)^2}{\operatorname{Im}\tau},
 \qquad M=-\frac{3\log6}{\pi},\qquad
 D=D_{\rm part}+\operatorname{Im}c.
\]
The period calculation in
\SeriesRef{wb:prop:period-exact-admissible-constants} gives
$\max D_{\rm part}=M$; the admissible range is
$\operatorname{Im}c<-M$. A positive loop in the $w$-plane lifts
to $c(r)=c_0-2r$, since
$e^{-\pi i(c_0-2r)}=e^{-\pi i c_0}e^{2\pi i r}$.
\end{definition}

\begin{definition}[The change of marking]
\hypertarget{tag-Q003}{}\label{mapsIII:def:engel-marking}
{\normalfont\scriptsize tag Q003}\par
Engel's indices $(0,1,\infty)$ correspond to $(1,2,0)$ here
\cite[Remark~8.3, pp.~22--23]{mapsEngel}. We denote his line
bundle by $M_S=\mathcal O_S(P-O)$. The coordinate change is
$x\mapsto P_Ex$, where
\[
 P_E=\begin{pmatrix}0&-2&-1&-2\\2&-1&0&-1\\
                      0&2&1&3\\-1&0&0&0\end{pmatrix},
 \qquad
 P_E^{-1}=\begin{pmatrix}0&0&0&-1\\-1&-1&-1&-2\\
                         -1&2&0&4\\1&0&1&0\end{pmatrix}.
\]
Matrix multiplication gives $P_EP_E^{-1}=P_E^{-1}P_E=I$.
For $\psi=(0,0,0,1)$ the character and twist coordinates are
\[
 \psi P_E=-\gamma,\qquad
 a_{j-1}=-P_Ev_j/m_j,\qquad
 v_j=-m_jP_E^{-1}a_{j-1}.
\]
\end{definition}

"""


def read(path):
    return path.read_text(encoding="utf-8")


def table(path):
    with path.open(encoding="utf-8", newline="") as stream:
        reader = csv.DictReader(stream, delimiter="\t")
        return reader.fieldnames, list(reader)


def write_table(path, fields, rows):
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("unit", choices=("common", "common_finish", "preamble"))
    args = parser.parse_args()
    key = "common_conventions" if args.unit in ("common", "common_finish") else "preamble"
    path = WORK / (key + ".tex")
    before = read(path)
    fields, rows = table(DEFECTS)
    ids = {row["change_id"] for row in rows}
    changes = []
    after = before

    def record(suffix, kind, old, new, reason, statement="sec:III:conventions"):
        ident = "III-C8-UNIT-" + key.upper() + "-" + suffix
        if ident in ids:
            raise ValueError("Edit already recorded: " + ident)
        changes.append(dict(change_id=ident, type=kind, statement_id=statement,
                            old_location=key + " before publication restructuring",
                            old_page="pending page concordance", new_location=key,
                            new_page="pending final PDF", old_text=old, new_text=new,
                            reason=reason, review_status="source change applied; final page review open"))

    def replace(suffix, kind, old, new, reason):
        nonlocal after
        if after.count(old) != 1:
            raise ValueError("Stale or nonunique exact guard: " + suffix)
        after = after.replace(old, new, 1)
        record(suffix, kind, old, new, reason, "preamble:III")

    if args.unit == "common_finish":
        old = r"\SeriesRef{wb:prop:period-exact-admissible-constants}"
        new = r"\SeriesRef{fam:src:C.2.3}"
        if after.count(old) != 1:
            raise ValueError("Stale maximum-reference guard")
        after = after.replace(old, new, 1)
        record("LIVE-MAXIMUM-TARGET", "D04", old, new,
               "The current attached tags/inventory identifies 03BR as a historical target absent from Paper I. Its printed maximum theorem is fam:src:C.2.3, tag01QL, I.6.6 p40; the complete statement in the inventory has the same cusp normalization and exact maximum. Cite that live result; no Paper I proof is reopened.", "mapsIII:def:period-parameters")
        heading = r"\section{Conventions and the marked family}\hypertarget{tag-034J}{}\label{sec:III:conventions}"
        new_heading = heading + "\n\\subsection{Markings and period parameters}\n\\hypertarget{tag-Q004}{}\\label{mapsIII:sec:marked-conventions}"
        if after.count(heading) != 1:
            raise ValueError("Stale common heading")
        after = after.replace(heading, new_heading, 1)
        record("SUBSECTION-UNIT", "D14", heading, new_heading,
               "Give the conventions a complete subsection before the radial-coordinate subsection, making both actual source units in their final order.")
        allowed_labels = ["mapsIII:sec:marked-conventions"]
        allowed_targets = ["tag-Q004"]
    elif args.unit == "common":
        if "tag-Q000" in before:
            raise ValueError("Common unit already edited")
        after = COMMON
        record("NUMBERED-CONVENTIONS", "D13", before, after,
               "Place all definitions and transport commentary in three numbered definitions and one numbered remark; preserve the existing section identity. No assertion of the marked family is removed without the specific duplicate/off-topic disposition below.")
        record("DUAL-TRANSPORT", "D20",
               "T_j=A_j^{-t}; an action of A_j on a cohomology class means its induced pullback",
               "(A^{-t} alpha)^t(Ax)=alpha^t x; transport A^{-t}, inverse and pullback A^t",
               "Give the evaluation-preserving map and its inverse explicitly, with both source and target variance. This resolves the ambiguous use of action in the convention.", "mapsIII:rem:dual-transport")
        rank_six = before[before.index(r"\paragraph{Rank-six matrices.}"):before.index("All homology and cohomology")]
        record("RANK-SIX", "D14", rank_six, "",
               "Remove the shared fourfold-only convention from this six-manifold paper. Its symbols and Kuhn-cap declaration supply no premise of the Paper III statements; the exact phrase/symbol-use search is recorded in the unit review. No other paper is edited.")
        record("CYCLIC-GROUP", "D12", r"$\pi_1(X_p)=\mathbb Z/|p|$",
               r"For general twists we write $p=12\ell_0-4\ell_1-3\ell_2$.",
               "The complete group presentation, inverse cyclic maps, nonzero scope and proof remain in maps:src:D.1.1. Remove their uncited duplicate assertion from the conventions.", "maps:src:D.1.1")
        record("ADMISSIBLE-RANGE", "D26", "For general twists p=12l_0-4l_1-3l_2",
               r"$3\nmid\ell_1$, $2\nmid\ell_2$, hence $p$ is prime to six",
               "Expose the already used admissibility restrictions proved in maps:src:D.1.1, so the conventions do not suggest a p=0 member of this family.", "mapsIII:def:marked-family")
        record("MARKING-INVERSE", "D22", r"P_E; \psi P_E=-\gamma; a_{j-1}=-P_Ev_j/m_j",
               r"P_E^{-1}; P_EP_E^{-1}=P_E^{-1}P_E=I; v_j=-m_jP_E^{-1}a_{j-1}",
               "Give the inverse integral marking and inverse twist map at their first occurrence; exact multiplication verifies both composites.", "mapsIII:def:engel-marking")
        record("MAXIMUM-REFERENCE", "D17", r"$M=\max D_{\rm part}=-3\log(6)/\pi$",
               r"\SeriesRef{wb:prop:period-exact-admissible-constants}",
               "Cite the existing series period-constant result for the maximum rather than leaving an unproved assertion in a conventions paragraph. The numerical value, period normalization and allowed c range are unchanged.", "mapsIII:def:period-parameters")
        allowed_labels = ["mapsIII:def:marked-family", "mapsIII:rem:dual-transport", "mapsIII:def:period-parameters", "mapsIII:def:engel-marking"]
        allowed_targets = ["tag-Q000", "tag-Q001", "tag-Q002", "tag-Q003"]
    else:
        old = "".join(r"\pdfextension mapfile{+" + name + ".map}\n" for name in ("cm", "cmextra", "symbols", "euler", "latxfont", "rsfs"))
        replace("ENGINE-MAPS", "D23", old, "", "Use the current TeX Live pdfLaTeX font maps loaded by standard packages.")
        replace("FONT-PACKAGES", "D23", "\\usepackage{fontspec}\n\\setmainfont{Latin Modern Roman}\n",
                "\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{lmodern}\n",
                "Make the single source build with pdfLaTeX using standard T1 Latin Modern fonts.")
        replace("MONO-FONT", "D23", "\\setmonofont[BoldFont=lmmonolt10-bold.otf,ItalicFont=lmmono10-italic.otf]{lmmono10-regular.otf}\n", "",
                "Latin Modern Type 1 monospaced fonts are selected by lmodern in pdfLaTeX.")
        replace("EQUATION-COUNTER", "D19", "\\allowdisplaybreaks[2]\n", "\\allowdisplaybreaks[2]\n\\numberwithin{equation}{section}\n",
                "Number equations by section; individual manual equation tags are reviewed and removed in their units.")
        replace("COROLLARIES", "D23", "\\crefname{corollary}{corollary}{corollarys}", "\\crefname{corollary}{corollary}{corollaries}", "Correct the plural cross-reference name.")
        hook = "\\AfterEndEnvironment{proof}{\\par\\begingroup\\footnotesize\\noindent\\hyperref[sec:results]{Return to \\S1.}\\par\\endgroup\\smallskip}\n"
        replace("RETURN-HOOK", "D10", hook, "", "Remove the automatic production-navigation sentence after every proof.")
        start = after.index(r"\newcommand{\StatementRecord}[4]")
        end = after.index(r"\newcommand{\ExternalPaperRef}", start)
        old_record = after[start:end]
        replace("RECORD-MACRO", "D10", old_record,
                "\\newcommand{\\StatementRecord}[4]{{\\normalfont\\scriptsize tag #3}\\par}\n",
                "Existing calls print only their permanent small tag while each body unit is reviewed; process links and use lists are removed.")
        allowed_labels, allowed_targets = [], []

    units.check_permanent_identifiers(before, after, allowed_labels, allowed_targets)
    path.write_text(after, encoding="utf-8", newline="\n")
    rows.extend(changes)
    write_table(DEFECTS, fields, rows)
    print("APPLIED", key, "UTC", datetime.now(timezone.utc).isoformat())
    print("DEFECT_ROWS", len(changes))
    print("NEW_LABELS", ",".join(allowed_labels))
    print("NEW_TARGETS", ",".join(allowed_targets))
    print("All pre-existing label and hypertarget multiplicities preserved.")
    print("Publication criteria and check events unchanged; no derived files refreshed.")


if __name__ == "__main__":
    main()
