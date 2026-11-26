"""Describe the seven current parts and identify the exact dependency lemma."""
from S6_SERIES_PUBLISH_c3_edit import *

s=SOURCE.read_text();a=s.index(r'\subsection{How the paper is organized}');b=s.index(r'\begin{figure}',a)
old=s[a:b]
new=r'''\subsection{How the paper is organized}
\Cref{part:II:cotangent-fibre-geometry} develops the index,
Picard and direct-image calculations, the smooth-fibre classification,
and the cotangent and conductor arguments. It ends with the full
normalization criterion of Theorem~A in
\cref{sec:II:global-normalization-criterion}.
\Cref{part:II:irreducible-euler} treats irreducible supports:
normalization topology, canonical boundaries, local transverse
singularities and the equality cases for their Euler numbers.

\Cref{part:II:periods-tangent-deformations} computes period ranks,
Picard resonance, tangent cohomology and deformation spaces for the
marked families. It also gives the conductor nonvanishing arguments
and the Liu--Rollenske parameter covering.
\Cref{part:II:component-geometry} studies component covers,
meromorphic fields, normalization lattices and reduced boundaries.
\Cref{part:II:compact-occurrence} constructs compact torus fibrations
with the stated component types and classifies marked Hopf, ruled
and elliptic supports with their full multiplicities.

\Cref{part:II:canonical-reduction} develops the component contractions,
canonical-order reduction and finite rooted generation, ending with
the Euler sign and equality criterion for arbitrary torus fibres in
\cref{sec:II:all:12}. The comb bundle splitting problem and its
established reduction occupy \cref{part:II:remaining-splitting}.
The figure identifies five premise uses in the proof of Theorem~A.

'''
apply_edit(old,new,'II-C3-ORGANIZATION-SEVEN-PARTS',['D14','D15','D24'],
 'how-the-paper-is-organized','Section1.6',
 'Describe the seven parts now present in the manuscript, including the earlier placement of the headline normalization criterion and the separate component, occurrence and canonical-reduction developments.',
 'Root read the entire old/new organization text, all seven current part headings and the actual section boundaries. Final global placement remains open while the three body remainders are being revised.')

s=SOURCE.read_text();a=s.index(r'\begin{figure}',s.index(r'\subsection{How the paper is organized}'));b=s.index(r'\end{figure}',a)+len(r'\end{figure}')
old=s[a:b]
new=r'''\begin{figure}[htbp]\centering
\begin{tikzpicture}[>=stealth,every node/.style={font=\small,align=center}]
\node[draw,rounded corners,text width=4.1cm,minimum height=1cm] (SB) at (0,0)
 {Smooth general fibres\\\hyperref[cdp:st:C.3.11]{\ref*{cdp:st:C.3.11}}};
\node[draw,rounded corners,text width=4.1cm,minimum height=1cm] (TV) at (6,0)
 {Twisted cotangent vanishing\\\hyperref[cdp:st:A.4.9]{\ref*{cdp:st:A.4.9}}};
\node[draw,rounded corners,text width=4.1cm,minimum height=1cm] (NT) at (3,-2)
 {Persistent normalization pullback\\\hyperref[lem:II:persistent-normalization-pullback]{\ref*{lem:II:persistent-normalization-pullback}}};
\node[draw,rounded corners,text width=4.1cm,minimum height=1cm] (GV) at (3,-4)
 {Generic-vanishing criterion\\\hyperref[cdp:st:C4f]{\ref*{cdp:st:C4f}}};
\draw[->,semithick] (SB) -- (NT);
\draw[->,semithick] (TV) -- (NT);
\draw[->,semithick] (NT) -- (GV);
\draw[->,semithick] (SB.west) -- ++(-.5,0) |- (GV.west);
\draw[->,semithick] (TV.east) -- ++(.5,0) |- (GV.east);
\end{tikzpicture}
\caption{The smooth-fibre and normalization premises of Theorem~A.}
\par\medskip
\begingroup\small
\begin{tabularx}{\textwidth}{@{}p{.25\textwidth}X@{}}
\toprule Arrow & Supplying and receiving arguments\\\midrule
\ref{cdp:st:C.3.11}$\to$\ref{lem:II:persistent-normalization-pullback} &
The torus and Hopf alternatives give the smooth-fibre cohomology
used in the conductor bound.\\
\ref{cdp:st:A.4.9}$\to$\ref{lem:II:persistent-normalization-pullback} &
The full-fibre filtration and twisted quotient vanishing turn
persistent ambient sections into inverse-Jacobian sections.\\
\ref{lem:II:persistent-normalization-pullback}$\to$\ref{cdp:st:C4f} &
Persistent sections on a fixed full fibre force its normalization
Picard pullback to vanish.\\
\ref{cdp:st:C.3.11}$\to$\ref{cdp:st:C4f} &
The two smooth-fibre types select the torus and Hopf direct-image
arguments in the criterion.\\
\ref{cdp:st:A.4.9}$\to$\ref{cdp:st:C4f} &
On the Hopf branch, the transgression vanishings make the second
direct image torsion. The full-fibre obstruction and analytic
continuation give nonvanishing for every twist.\\
\bottomrule\end{tabularx}\endgroup\end{figure}'''
apply_edit(old,new,'II-C3-DEPENDENCY-EXACT-OWNER',['D06','D14','D22','D24'],
 'how-the-paper-is-organized;lem:II:persistent-normalization-pullback;cdp:st:C4f',
 'Section1.6 dependency figure and its premise-use table',
 'The general criterion invokes P263, whose statement assumes persistent sections on one full fibre, and C3.11 for its two cohomological cases. C4e instead assumes c3>0 and uses P263. Replace the diagram\'s C4e intermediary by the actual common lemma, and its necessary-list node by C3.11, with exactly the five displayed receiving uses. No body statement or proof changes.',
 'Root read the complete C4e/C4f blocks, P263 statement and its complete proof in the earlier admission, and reread the receiving passages. The full original/new figure and table were read; the next integrated build must verify its layout.')

add_event('how-the-paper-is-organized','II-C3-ORGANIZATION-EXACT-DEPENDENCIES','used and rechecked in this run',
 'Root compared all seven current parts with the complete old/new organization prose. The dependency figure now names P263 as the persistent-pullback premise used by C4f, and C3.11 as its torus/Hopf classification premise. C4e is a positive-c3 application of P263; its complete statement/proof and C4f were reread, with the previously full-read P263 receiver. Each of the five arrows has an explicit corresponding receiving use. This corrects the front-matter dependency owner without changing any mathematical body text. Whole organization-unit closure, all Further-results entries, final placement and rendered figure layout remain open.',
 'Section1.6 prose, dependency figure and five-row map table',source=__file__)
print('Seven-part organization and exact five-arrow dependency diagram integrated; final front/structure/layout rows remain open.')
