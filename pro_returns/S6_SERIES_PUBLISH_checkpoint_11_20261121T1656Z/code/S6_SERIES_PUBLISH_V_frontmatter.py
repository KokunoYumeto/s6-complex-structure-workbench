#!/usr/bin/env python3
"""Reorder Paper V's introduction and align its exact mathematical dependencies."""
import re
from S6_SERIES_PUBLISH_editing import Editor,ROOT,block
E=Editor('V')
# Full parameter convention, used by every main statement.
a=E.text.index('Theorem~A concerns the fibre product')
b=E.text.index('\\hypertarget{main-V-A}',a)
E.replace(E.text[a:b],r'''\begin{definition}[The period parameter]
\hypertarget{tag-PV14}{}\label{pub:V:parameter}
We use the algebraic splitting $\sigma_b$, invariant vector $e$ and
functional $\alpha$ with the exact normalization of
\cref{def:hb,night:P1.15}. For the rank-three bundle $P$ of
\cref{night:P1.5}, put
\[
 F_\xi=(\sigma_b+\xi\alpha e)(P),\qquad
 c_*=-\min h_b,\qquad
 \mathcal U=\{\xi\in\mathbb C:\operatorname{Im}\xi>c_*\},
\]
where $h_b$ is the real-intersection function of \cref{def:hb}.
We write $M_\xi$ for the compact filling of these periods with the
base and fibre conjugation of \cref{rem:V:conjugation-parameter}.
For the imaginary ray we write $M_c=M_{ic}$, with $c>c_*$.
The positive Kuhn fan is fixed throughout this family.
\end{definition}

''','D20','State the single algebraically normalized parameter and the exact real subfamily before the main results.','pub:V:parameter')
old=block(E.text,'series:V:D',False)
start=old.index('The period planes extend')
new=old[:start]+r'''For every $\xi\in\mathcal U$, the genus-two periods of
\cref{series:V:C}, with the integral datum of
\cref{pub:V:rank-six-data}, extend over the finite root charts
and the positive marked Kuhn cusp. They give a compact complex
fourfold $M_\xi$ and an orientation-preserving diffeomorphism
\[
 M_\xi\ \cong\ 3\mathbb{HP}^2\#(-\mathbb{HP}^2).
\]
The fourfolds form a holomorphic family over $\mathcal U$.
Their smooth middle lattice and spin characteristic vector are
isometric to $\bigl(I_{3,1},(1,1,1,1)\bigr)$.
\end{maintheorem}'''
E.replace(old,new,'D15','State the headline compact construction with its precise parameter domain and marked inputs first.','series:V:D')
old=block(E.text,'series:V:A',False)
start=old.index('The explicit crepant small resolution')
new=old[:start]+r'''Let $X$ be a canonical marked member of the $(3,4,\infty)$
family, with reduced multiple fibres $S_1,S_2$ of multiplicities
three and four, and put $L=\mathcal O_X(S_1-S_2)$.
Let $S\to\mathbb P^1$ be the elliptic surface in
\cref{maps:src:E.1.2}, with its cusp over the cusp of $X$.
The fibre product $X\times_{\mathbb P^1}S$ has the small
crepant resolution $\Pi:Z\to X$ of that theorem.
It is a compact complex fourfold with
$K_Z=\Pi^*L^{-5}$, algebraic dimension two,
$b_1(Z)=0$, and $h^{0,1}(Z)=1$.
Its signature is two and its middle intersection form is
$\langle1\rangle\oplus\langle1\rangle$.
It lies outside Fujiki's class $\mathcal C$.
\end{maintheorem}'''
E.replace(old,new,'D15','Specify the resolved-product inputs, line bundle, and conclusions in the main theorem.','series:V:A')
E.replace('The rank-six integral monodromy of \\cref{maps:src:F.2.5}', 'The rank-six integral monodromy of \\cref{pub:V:rank-six-data}', 'D24','Point to the definition that now contains the matrices.','series:V:B')
E.replace('each order-two torsion class coming from the order-four filling is hit by a differential from the cusp, so the homology is free', 'each order-two suspension class from the order-four filling transgresses to the corresponding nonzero global coinvariant, so the resulting homology is free', 'D24','State the proved direction and source of the torsion transgressions.','series:V:B')
E.replace('For input entry height $H$, the finite stopping bound is', 'For input entry height $H$, the finite stopping bound is', 'D15','Read the classification scope without altering its input-dependent bound.','series:V:F')
# Short status lines; the exact locators are collected once in the table.
status={
'A':r'The global small crepant resolution and its computed invariants are new; the cited six-sphere, elliptic and toroidal constructions are the inputs listed in \S\ref{pub:V:known-new}.',
'B':r'The integral rank-six datum and its global homology calculation are new; the toroidal filling is the cited construction listed in \S\ref{pub:V:known-new}.',
'C':r'The pencil, its integral exterior-square comparison and its normalized lifted planes are new.',
'D':r'The compact complex realization is new; the smooth classification and absorption results used to identify its underlying manifold are listed in \S\ref{pub:V:known-new}.',
'E':r'The exact parameter domain and the family invariants are new; the cited direct-image and torus-deformation inputs are listed in \S\ref{pub:V:known-new}.',
'F':r'The classification and bounded-cusp period theorem are new; their cited lattice-isomorphism and Oka inputs are listed in \S\ref{pub:V:known-new}.',
}
for c in 'ABCDEF':
 a=E.text.index('\\hypertarget{main-V-'+c+'}')
 s=E.text.index('\\textit{Relation to literature.}',a)
 end=E.text.index('\\hyperlink{outline-V-'+c+'}',s)
 E.replace(E.text[s:end], '\\textit{Relation to literature.} '+status[c]+'\n', 'D12','Give a one-line literature status and collect exact primary-source locators once in the known-and-new table.','series:V:'+c)
# The certified interval stays in the body; the introductory decimal is short.
E.replace('\\[c_*=1.0945402503114027801162682630549457037\\ldots.\\]', '\\[c_*\\approx1.09454.\\]', 'D15','Use a short introductory approximation; preserve the full certified interval in the body.','series:V:E')
# Exact proof outline replacements, retaining every old step anchor.
repl={
'B-1':r'''The matrices of \cref{pub:V:rank-six-data} have orders five and four. The square-zero cusp has primitive rank-three image, and its explicit unimodular marking is proved in \cref{night:P1.1}. The invariant covector $x\mapsto x_0$ detects every nonidentity affine power, proving the freeness used in \cref{pub:V:smooth-gluing}.''',
'B-2':r'''The cusp and finite quotient charts give the marked smooth gluing. Its van Kampen relations reduce to $5a=h$, $4b=-h$ and $a+b=0$; their integral relation matrix is unimodular. Hence the manifold is simply connected, by \cref{pub:V:smooth-gluing}.''',
'B-3':r'''The signed-orbit bases at the finite cores, their norm maps, and the primitive cusp collapse give the integral restriction sheaves and their point kernels. Determinant minors compute their cohomology in \cref{pub:V:integral-restrictions}, using the collapse of \cref{night:P1.11}.''',
'B-4':r'''For the order-four core, the loops $v=g^4h^{-1}$ and $t=g$ form an integral basis. A torsion representative pulls back to $(0,w)$, so its transgression is $\pm[w]$ by \cref{mapsaudit:order-four-torsion-transgression}. The three nonzero global images are proved in \cref{pub:V:integral-restrictions}.''',
'B-5':r'''The three torsion differentials are isomorphisms onto $\mathbb Z/2$. The remaining cusp kernel is free of rank one. The Leray filtration, universal coefficients, duality and Hurewicz then give free integral homology and three-connectivity in \cref{maps:src:F.2.6}.''',
'B-6':r'''The almost complex structure has $c_1=c_3=0$. The index and signature identities of \cref{sec:V-known-inputs} force $c_2^2=2$, $\sigma=2$ and the middle form $I_{3,1}$. The Pontryagin identities and characteristic vector are computed in \cref{night:P1.13}.''',
'C-4':r'''The root-line decomposition of $P$ has $H^1(P^*)=0$ and a one-dimensional space of functionals by \cref{night:P1.5}. Its extension therefore splits holomorphically. The exact contraction and period comparison in \cref{def:hb} identify the normalization of $\alpha$ and $\sigma_b$.''',
'C-5':r'''For the real-intersection line, the normalized lift has transversality exactly when $h_b+\operatorname{Im}\xi\ne0$. The cusp has $Z=(\log q)/(2\pi i)I_3+C(q)$ and $h_b\to+\infty$. Thus the complete parameter domain is the half-plane above $-\min h_b$, by \cref{night:P1.8,night:P1.18}.''',
'D-3':r'''The characteristic vector has odd coordinates and norm two in $I_{3,1}$. The integral reflection in $(1,1,1,1)$ strictly decreases the absolute negative coordinate until all four coordinates have absolute value one. The resulting explicit isometry is proved in \cref{night:P1.13}.''',
'E-1':r'''The infinity-root symmetry makes the differential of the normalized height vanish at zero. Its positive Hessian proves a strict local minimum. Convergent root and cusp expansions, with interval continuation over finite closed covers, prove the height is strictly larger on their complements; the positive cusp graph treats the remaining inner disc. This proves the unique global minimum and the exact domain in \cref{night:P1.18}.'''
}
for key,newbody in repl.items():
 pat=r'(\\item\\hypertarget\{step-V-'+re.escape(key)+r'\}\{\})(.*?)(?=\n\\item|\n\\end\{enumerate\})'
 m=re.search(pat,E.text,re.S)
 assert m,key
 E.replace(m.group(0),m.group(1)+' '+newbody+'\n','D24','Align the outline with the consolidated proof and its actual dependencies.','step-V-'+key)
# Reorder theorem blocks and matching outlines, preserving the stable identifiers.
order='DECBFA'
a=E.text.index('\\hypertarget{main-V-A}')
b=E.text.index('\\subsection{The proofs in outline}',a)
chunk=E.text[a:b]
starts=list(re.finditer(r'\\hypertarget\{main-V-([A-F])\}\{\}',chunk))
parts={m[1]:chunk[m.start():(starts[i+1].start() if i+1<len(starts) else len(chunk))] for i,m in enumerate(starts)}
E.replace(chunk,''.join(parts[c] for c in order),'D14','Present the compact complex realization first, followed by its family, period and topology theorems, classification and resolved product.','sec:results')
a=E.text.index('\\hypertarget{outline-V-A}')
b=E.text.index('\\subsection{Known and new}',a)
chunk=E.text[a:b]
starts=list(re.finditer(r'\\hypertarget\{outline-V-([A-F])\}\{\}',chunk))
parts={m[1]:chunk[m.start():(starts[i+1].start() if i+1<len(starts) else len(chunk))] for i,m in enumerate(starts)}
E.replace(chunk,''.join(parts[c] for c in order),'D14','Order the proof outlines exactly as the main theorems while retaining every old outline anchor.','sec:results')
# Replace repeated status table with concise, precise locators.
a=E.text.index('\\subsection{Known and new}')
b=E.text.index('\\subsection{Methodology}',a)
known=r'''\subsection{Known and new}\label{pub:V:known-new}
\begin{center}\small
\begin{tabularx}{\textwidth}{@{}lX@{}}\toprule
Theorem & Status and principal cited inputs\\\midrule
\ref{series:V:D} & New compact complex realization. Smooth classification: \cite[Definition~3.6 and Theorem~3.7(1), arXiv v3, pp.~12--14]{IVVWallForm}; sphere absorption: \cite[Theorem~A, p.~178]{IVVKramerStolz}; almost complex compatibility: \cite[Corollary~1.4, p.~4]{ffMandal}.\\
\ref{series:V:E} & New parameter domain and invariants. Direct images: \cite[Lemmas~6.1--6.2, pp.~74--75, Proposition~6.10, pp.~79--80]{DGKX2026v1}; torus deformations: \cite[Theorem~2.1, p.~264]{Catanese2004}.\\
\ref{series:V:C} & New genus-two pencil and integral lifted-period construction. The cusp model is \cite[Theorem~8.7, arXiv v1, pp.~57--59]{Yang2026}.\\
\ref{series:V:B} & New integral rank-six gluing and homology. Toroidal filling and Euler number: \cite[Theorem~8.7 and Corollary~8.8, arXiv v1, pp.~57--59]{Yang2026}; integral specialization: \cite[\S7.7, pp.~60--64]{AC26}.\\
\ref{series:V:F} & New integral classification and period theorem. Lattice isomorphism: \cite[Theorem~3.4, p.~6, Algorithm~8.3, p.~21]{rootBHJ22}; local-spray approximation: \cite[Theorem~2.1 and Corollary~2.4, arXiv v5]{IVVOkaOneV5}.\\
\ref{series:V:A} & New small crepant resolution and its invariants. Six-sphere: \cite[Theorems~7.17 and~7.22, pp.~57 and~60]{AC26}; elliptic surface: \cite[\S2]{E26}; characteristic identities: \cite[(1.2)--(1.4), pp.~3--4]{ffEsoleKang}; class-$\mathcal C$ criterion: \cite[Theorem~1.1, Remark~1.2, p.~2]{ffJiaMeng}.\\
\bottomrule\end{tabularx}\end{center}
'''
E.replace(E.text[a:b],known,'D15','Provide one concise status row per main theorem and precise opened-source locators.','pub:V:known-new')
a=E.text.index('\\subsection{Methodology}')
b=E.text.index('\\subsection{How the paper is organized}',a)
method=(ROOT/'agents/provenance/S6_SERIES_PUBLISH_V_methodology_proposal.tex').read_text()
method=method[method.index('\\subsection{Methodology}'):]
E.replace(E.text[a:b],method+'\n','D15','Correct the method/count scope, preserve historical attribution, and identify the pinned records as historical. Counts are a provisional recomputation until final events are merged.','sec:results')
# Add section/part labels for regenerated references.
heads={'The marked rank-six construction and its family':'pub:V:part-rank-six','Integral monodromy and marked gluings':'pub:V:part-classification','The resolved fibre product':'pub:V:part-resolved','Shifted fibre products':'pub:V:part-shifted'}
for title,label in heads.items():
 E.replace('\\part{'+title+'}', '\\part{'+title+'}\\label{'+label+'}', 'D24','Use a stable label for the actual part.','sec:results')
for title,label in {'The genus-two pencil and the lifted period planes':'pub:V:sec-periods','The integral eight-manifold':'pub:V:sec-integral','The oriented diffeomorphism type':'pub:V:sec-diffeomorphism','The normalized connection and the exact parameter domain':'pub:V:sec-parameter','Cohomology, deformations and isomorphisms':'pub:V:sec-cohomology','The boundary of the family':'pub:V:sec-boundary','Admissible data and local restrictions':'pub:V:sec-admissible','Source obstructions and the punctured-base period decision':'pub:V:sec-oka','The resolved fibre-product fourfold':'pub:V:sec-resolved'}.items():
 E.replace('\\section{'+title+'}', '\\section{'+title+'}\\label{'+label+'}', 'D24','Make organization references follow the current section numbering.','sec:results')
a=E.text.index('\\subsection{How the paper is organized}')
b=E.text.index('\\clearpage\n\\part{',a)
org=r'''\subsection{How the paper is organized}
Part~\ref{pub:V:part-rank-six} constructs the marked rank-six family.
The local monodromy and cusp in \S\ref{pub:V:sec-local} precede the
period planes in \S\ref{pub:V:sec-periods}, the integral homology in
\S\ref{pub:V:sec-integral}, and the oriented smooth classification
in \S\ref{pub:V:sec-diffeomorphism}. Sections
\ref{pub:V:sec-parameter}--\ref{pub:V:sec-boundary} determine its
parameter domain, invariants and boundary.
Part~\ref{pub:V:part-classification} classifies the integral data and
constructs punctured-base periods. Part~\ref{pub:V:part-resolved}
gives the resolved elliptic fibre product. Part~\ref{pub:V:part-shifted}
uses the sphere fibrations to construct shifted fivefolds and determines
their integral homotopy and smooth topology.

\begin{figure}[htbp]\centering
\begin{tikzpicture}[>=stealth,every node/.style={font=\small,align=center}]
\node[draw,rounded corners,text width=3cm] (local) at (0,0) {Marked datum and cusp\\\cref{pub:V:rank-six-data,night:P1.9}};
\node[draw,rounded corners,text width=2.7cm] (period) at (-4,-1.6) {Periods\\Theorem~\ref{series:V:C}};
\node[draw,rounded corners,text width=2.7cm] (topology) at (0,-1.6) {Integral topology\\Theorem~\ref{series:V:B}};
\node[draw,rounded corners,text width=2.7cm] (resolved) at (4,-1.6) {Resolved product\\Theorem~\ref{series:V:A}};
\node[draw,rounded corners,text width=3cm] (compact) at (-2,-3.3) {Compact complex fourfold\\Theorem~\ref{series:V:D}};
\node[draw,rounded corners,text width=3cm] (family) at (-2,-4.8) {Exact family and boundary\\Theorem~\ref{series:V:E}};
\draw[->] (local)--(period);\draw[->] (local)--(topology);\draw[->] (local)--(resolved);
\draw[->] (period)--(compact);\draw[->] (topology)--(compact);\draw[->] (compact)--(family);
\end{tikzpicture}
\caption{The shared marked cusp and the main construction. The general classification of Theorem~\ref{series:V:F} is developed separately in Part~\ref{pub:V:part-classification}.}
\end{figure}

\subsubsection*{Further results}
\begin{itemize}[leftmargin=*]
\item \Cref{maps:src:E.2.3,maps:src:E.2.6}: the shifted fivefold has a torus-knot peripheral presentation and explicitly computed integral homology.
\item \Cref{maps:src:E.2.7,maps:src:E.2.9}: all transverse shifts have one oriented smooth type and are framed null-bordant over their fundamental group.
\item \Cref{maps:src:E.2.11,maps:src:E.2.17}: the cusp and peripheral maps determine the full second-homotopy module and its coinvariants.
\item \Cref{maps:src:E.2.13,maps:src:E.2.14}: a circle fibration has an infinite-order return map given by the separating torus twist.
\item \Cref{maps:src:E.2.19,maps:src:E.2.21}: the relative cusp model gives an explicit smooth framed-handle presentation.
\end{itemize}

'''
E.replace(E.text[a:b],org,'D24','Describe the four actual parts, replace obsolete main-theorem dependencies by the shared cusp, and add a concise further-results list.','sec:results')
# Main theorem letters now come from their labels; never hard-code a moved letter.
a=E.text.index('\\begin{document}')
old=E.text[a:]
new=re.sub(r'Theorem[~ ]([A-F])(?=\b|:)',lambda m:'Theorem~\\ref{series:V:'+m[1]+'}',old)
E.replace(old,new,'D24','Regenerate every literal main-theorem letter from its preserved stable label after reordering.','sec:results')
# One pin definition; all known identical commit strings refer to it.
pin='83d76022bcd442278b760db9ff438afceed6c6ea'
old=E.text
E.text=E.text.replace(pin,'\\SsixRepositoryCommit')
E.text=E.text.replace('\\begin{document}', '\\newcommand{\\SsixRepositoryCommit}{'+pin+'}\n\\begin{document}',1)
E.record('D09',pin,'\\SsixRepositoryCommit','Define the historical repository pin once for all program and record citations.','sec:results')
E.save()
