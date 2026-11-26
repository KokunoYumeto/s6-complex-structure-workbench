"""Admit six defects actually seen in the root's fixed-PDF page reading.

Prepared after viewing every page 1–100. Run with --apply after the fixed
candidate's whole image pass. These are typography changes only; they add
no mathematical CHECK_EVENTS and do not close a final page-reading gate.
"""
from S6_SERIES_PUBLISH_c4_edit import *
import sys

items = [
    ("II-C4-VISUAL-ROOT-026", "cdp:st:C.1.1", "26",
     r"\part{Cotangent obstructions and fibre geometry}\label{part:II:cotangent-fibre-geometry}",
     "\\Needspace{13\\baselineskip}\n" + r"\part{Cotangent obstructions and fibre geometry}\label{part:II:cotangent-fibre-geometry}",
     "The Part I and section 3 opening ended with the Proposition 3.1 heading alone; its statement began on the following page. Reserve room for the opening and first statement lines."),
    ("II-C4-VISUAL-ROOT-035", "cdp:st:D.1.12", "35",
     r"\begin{proposition}[Cup products and cohomological flatness]\hypertarget{tag-01FX}{}\label{cdp:st:D.1.12}",
     "\\Needspace{5\\baselineskip}\n" + r"\begin{proposition}[Cup products and cohomological flatness]\hypertarget{tag-01FX}{}\label{cdp:st:D.1.12}",
     "Proposition 5.7's heading and tag were alone at the page foot; reserve room for its first statement lines."),
    ("II-C4-VISUAL-ROOT-039", "cdp:st:D.1.13", "39",
     r"\subsection{Coherent splitting in explicit torus families}\label{sec:II:coherent-splitting}",
     "\\Needspace{8\\baselineskip}\n" + r"\subsection{Coherent splitting in explicit torus families}\label{sec:II:coherent-splitting}",
     "Subsection 5.3 and Proposition 5.12's heading ended the page without any statement text; keep the opening and first statement lines together."),
    ("II-C4-VISUAL-ROOT-044", "cdp:st:C.3.4", "43–44",
     "This contradiction proves the assertion for every component.\n\n\\end{enumerate}\n\\end{proof}",
     "This contradiction proves the assertion for every component.\\qedhere\n\n\\end{enumerate}\n\\end{proof}",
     "The end-of-proof square was alone at the top of page 44, separated from the proof on page 43. Place it at the last proof line inside the list."),
    ("II-C4-VISUAL-ROOT-072", "cdp:st:B2", "72",
     r"the restriction of $M_E$ is a nontrivial $A_\lambda$. \cref{cdp:st:B1} gives the two vanishings",
     r"the restriction of $M_E$ is a nontrivial $A_\lambda$. \Cref{cdp:st:B1} gives the two vanishings",
     "The sentence-initial reference name printed lowercase. Capitalize that name while retaining its exact reference target."),
    ("II-C4-VISUAL-ROOT-078", "cdp:st:A.3.3", "78",
     r"\begin{proposition}[Finite Picard translations for multiple fibres]\hypertarget{tag-01AN}{}\label{cdp:st:A.3.3}",
     "\\Needspace{5\\baselineskip}\n" + r"\begin{proposition}[Finite Picard translations for multiple fibres]\hypertarget{tag-01AN}{}\label{cdp:st:A.3.3}",
     "Proposition 7.19's heading and tag were alone at the page foot; reserve room for its first statement lines."),
]

text = SOURCE.read_text()
for change, sid, page, old, new, reason in items:
    assert text.count(old) == 1, (change, text.count(old))
    preserve_identifiers(old, new)

if "--apply" in sys.argv:
    for change, sid, page, old, new, reason in items:
        apply_edit(old, new, change, ["D23"], sid,
                   "Final-candidate rendered page " + page,
                   reason,
                   old_page=page + " in PDF e5856a7a707d681f89712150d4f1b100554f29a08bc5a843c5d52aa1d7ca2871",
                   review="Root viewed the full old page image and read the exact old/new source context. Only spacing, proof-mark placement or initial capitalization changes; formulas, statements, reference targets and labels remain identical. Rebuilt-page inspection remains open.")
    print("Admitted six root image findings; no mathematical event or final-page closure.")
else:
    print("Validated six exact typography guards; no source or record was changed.")
