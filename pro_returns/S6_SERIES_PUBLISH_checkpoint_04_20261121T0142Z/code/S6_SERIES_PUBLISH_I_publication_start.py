#!/usr/bin/env python3
"""Apply the first presentation pass, preserving every mathematical anchor."""
from pathlib import Path
import csv, json, re
from S6_SERIES_PUBLISH_editing import Editor, ROOT
from S6_SERIES_PUBLISH_engine_baseline import portable

e=Editor('I')
_, changes=portable(e.text)
for old,new in changes:
    e.replace(old,new,'D23','Use the standard pdfLaTeX font packages; the mathematical document body is unchanged.','preamble')
a=e.text.index('\\newcommand{\\StatementRecord}')
b=e.text.index('\\newcommand{\\ExternalPaperRef}',a)
e.replace(e.text[a:b],r'\newcommand{\StatementRecord}[4]{{\upshape\footnotesize[tag~\texttt{#3}]}\enspace\ignorespaces}'+'\n',
          'D10','Print only the permanent tag; keep all event, dependency and back-link data in the check records.','preamble')
old=r'\AfterEndEnvironment{proof}{\par\begingroup\footnotesize\noindent\hyperref[sec:results]{Return to \S1.}\par\endgroup\smallskip}'
e.replace(old,'','D10','Remove repeated proof-navigation footers; retain the existing section and proof anchors.','preamble')
e.replace(r'\crefname{corollary}{corollary}{corollarys}',r'\crefname{corollary}{corollary}{corollaries}',
          'D23','Use the correct plural in generated cross-references.','preamble')
for m in list(re.finditer(r'\\hyperlink\{main-I-([A-G])\}\{Return to Theorem \1\}\.',e.text)):
    e.replace(m[0],'','D10','Remove repeated return navigation after the outline; its forward links and anchor remain.','outline-I-'+m[1])
old=r'label={$\langle1\rangle$\arabic*.}'
count=e.text.count(old)
if count:e.replace(old,r'label=\arabic*.','D10','Use ordinary proof-step numbering while preserving the full order and content of every item.','proof enumeration',count)

v=(ROOT/'S6_SERIES_PUBLISH_V.tex').read_text()
start='\\subsection{The series and this paper}'
end='\\subsection{The main theorems}'
a=e.text.index(start);b=e.text.index(end,a)
va=v.index(start);vb=v.index(end,va)
e.replace(e.text[a:b],v[va:vb],'D15','Use the same concise mathematical series paragraph and dependency table as the completed Paper V.','sec:results')

a=e.text.index('\\begin{abstract}');b=e.text.index('\\end{abstract}',a)+len('\\end{abstract}')
abstract=r'''\begin{abstract}
We determine the periods, moduli and two limiting regimes of the
$(3,4,\infty)$ family of complex six-spheres. A theta expression for
its elliptic period gives the exact parameter disc $0<|w|<216$.
Integral affine and cusp comparison maps classify the discrete data,
parameter identifications and real structures, including the fixed
three-spheres. We compute the integral monodromy group, its maximal
domain of proper discontinuity and the algebraic dimension of every
smooth fibre. Logarithmic direct images and explicit relative
differential modules determine the Dolbeault, Bott--Chern, Aeppli
and tangent cohomology, all Picard twists and the deformation parameter.
Global Dolbeault representatives extend through the multiple fibres
and cusp. At the puncture, the corner monodromy obstructs every
proper Hausdorff analytic filling after any finite parameter cover;
the analogous obstruction holds for the coprime higher-multiplicity
sphere families. At the outer boundary, the intrinsic Albanese
invariant obstructs continuation, while the dual period lattices
determine the local Hausdorff reflection and all additive limits.
The arithmetic norm satisfies exact division and height identities;
we describe its torsion values, critical points and level curves.
\end{abstract}'''
e.replace(e.text[a:b],abstract,'D15','State the mathematical conclusions directly and remove narration of credited appendices and re-derivation history.','abstract')
e.replace('\\date{19 November 2026}','\\date{21 November 2026}','D15','Date the publication revision.','title block')

# The inherited table supplies identities only, with no mathematical account.
# Its exact content is retained in the edit record and registry.
a=e.text.index('\\paragraph{Further results.}')
b=e.text.index('\\subsection{The proofs in outline}',a)
further=r'''\subsubsection*{Further results}
\begin{itemize}[leftmargin=*]
\item \Cref{ari:C.4.2,ari:C.4.3,ari:C.4.4}: division polynomials give the exact torsion loci and their norm values.
\item \Cref{ari:C.6.3,ari:C.6.T2}: local heights give the rational CM factors and the stated central derivative calculation.
\item \Cref{mapsI:src:A.1.1,mapsI:src:A.2.1}: the integral circle quotient has an explicit cusp replacement and relative uniqueness.
\item \Cref{inv:C3.8}: holomorphic cocycles and a locally finite coordinate partition give global coefficient representatives.
\item \Cref{ari:C.8.15,push:src:D.4.8}: the theta norm has one maximum and strictly star-shaped lower level curves.
\end{itemize}

'''
e.replace(e.text[a:b],'','D10','Move the inherited further-result tag inventory to the records; replace it by a short mathematical list after the organization section.','further results')
anchor='\\clearpage\n\\section{Common conventions and the marked construction}'
e.replace(anchor,further+anchor,'D15','Give each further result a statement reference and a mathematical description.','further results')

# In this paper the main letters have not moved; references still become
# label-based so the later series pass can regenerate them without guesses.
start=e.text.index('\\begin{document}')
body=e.text[start:]
newbody=re.sub(r'Theorem[~ ]([A-G])(?=\b|:)',lambda m:'Theorem~\\ref{series:I:'+m[1]+'}',body)
e.replace(body,newbody,'D06','Resolve every literal introductory main-theorem letter through its preserved stable label.','main theorem references')
e.save()

# Apply the independently reviewed parser guard exactly, without recounting.
p=ROOT/'agents/i_provenance/S6_SERIES_PUBLISH_I_shared_parser_guard.json'
guard=json.loads(p.read_text());target=Path(guard['source']);s=target.read_text()
for c in guard['changes']:
    assert s.count(c['old'])==1
    s=s.replace(c['old'],c['new'],1)
target.write_text(s)
print('Added cited environments to the current-statement metadata parser; no events added.')
