from pathlib import Path
import re
from collections import Counter
from S6_SERIES_PUBLISH_c3_foundations_sec11_helpers import ROOT, OUT, Package, block

main = (ROOT / 'S6_SERIES_PUBLISH_II.tex').read_text()
pkg = Package('canonical_flat', 'subsec:II:canonical-flat-reduction')
owner = 'cdp:st:C.2.UN.75'
old = block(main, owner)
old335 = block(main, 'prop:II:section-fibre-contraction')
for suffix, text in [('UN75_input', old), ('P335_input', old335)]:
    (OUT / ('S6_SERIES_PUBLISH_II_sec11_canonical_flat_' + suffix + '.tex')).write_text(text + '\n', newline='\n')

p343 = r'''\subsection{Canonical forms under bimeromorphic maps}\label{subsec:II:canonical-bimeromorphic-maps}

\begin{lemma}[Canonical direct images and surviving divisor orders]\hypertarget{tag-P343}{}\label{lem:II:canonical-bimeromorphic-direct-image}
\StatementRecord{lem:II:canonical-bimeromorphic-direct-image}{proved}{P343}{\cref{cdp:st:C.2.UN.17}}
Let $f:X\to\Delta$ and $f':X'\to\Delta$ be proper degenerations
of connected complex two-tori from smooth complex threefolds.
Let $\phi:X\dashrightarrow X'$ be a bimeromorphic map over the disc.
Meromorphic pullback induces an isomorphism of canonical direct images
\begin{equation}
                f'_*K_{X'}\xrightarrow{\ \phi^*\ } f_*K_X.
\hypertarget{tag-00PE}{}\label{cdp:eq:C.KG.6}
\end{equation}
The inverse is the pullback by $\phi^{-1}$. It identifies local
generators up to a holomorphic base unit. For a prime divisor which
survives as a prime divisor under $\phi$, the orders of corresponding
generators along the two divisors are equal.
\end{lemma}
\begin{proof}
A holomorphic top form on $f'^{-1}(A)$, for an open subdisc $A$,
pulls back holomorphically on the domain of $\phi$ in $f^{-1}(A)$.
The indeterminacy set of a meromorphic map from a smooth space
has codimension at least two. In smooth coordinate volume frames,
Hartogs extension of its coefficient therefore gives a holomorphic
top form on all of $f^{-1}(A)$. These extensions agree on chart
overlaps by uniqueness, and commute with restriction in $A$.
Apply the same construction to $\phi^{-1}$. Both composites are
the identity on the common biholomorphic dense open set, hence
on the whole smooth spaces. This proves the displayed sheaf
isomorphism. By \cref{cdp:st:C.2.UN.17}, the canonical direct images
are rank-one torsion-free coherent sheaves on the smooth disc
and thus line bundles, so two
local generators differ by a base unit. At the generic points of
corresponding surviving divisors, the bimeromorphic map identifies
their divisorial local rings and is a biholomorphism on dense open
subsets of those divisors. Its Jacobian is a unit there. Pullback
therefore preserves the vanishing order of the top form.
\end{proof}
'''

old335paragraph = r'''\item Apply \cref{cdp:st:C.2.UN.17} to the descended proper
torus family. Ordinary pullback gives
$f'_*K_{U'}\to f_*K_U$. Its inverse restricts a form on $U$
to $U\setminus T$, transports it through the isomorphism
$U\setminus T\simeq U'\setminus B$, and extends its coefficients
in smooth volume frames across $B$ by Hartogs' theorem.
Both compositions are the identity on the common open set
and hence everywhere. Thus a generator downstairs pulls back to a
generator upstairs. Restrict its vertical canonical line to
$B$; the resulting isomorphism is'''
new335paragraph = r'''\item Apply \cref{cdp:st:C.2.UN.17} to the descended proper
torus family and \cref{lem:II:canonical-bimeromorphic-direct-image}
to $(X,X',f,f',\phi)=(U,U',f,f',\pi)$.
The pullback in \eqref{cdp:eq:C.KG.6} is ordinary pullback by
this blowdown; its inverse uses exactly the isomorphism
$U\setminus T\simeq U'\setminus B$ and extension across $B$.
Thus a generator downstairs pulls back to a generator upstairs.
Restrict its vertical canonical line to $B$; the resulting isomorphism is'''
new335 = pkg.edit(old335, old335paragraph, new335paragraph, 'D12,D17,D20', 'prop:II:section-fibre-contraction', 'The complete earlier general owner supplies precisely the ordinary-blowup canonical direct-image map. All weighted line, Jacobian and order-one calculations remain here.')
new335 = pkg.edit(new335, r'\cref{cdp:st:C.2.UN.17,lem:II:blowup-topology}', r'\cref{cdp:st:C.2.UN.17,lem:II:blowup-topology,lem:II:canonical-bimeromorphic-direct-image}', 'D04,D12', 'prop:II:section-fibre-contraction', 'Declare the same exact earlier canonical map in the hidden input record.')

orphan_start = main.rfind('An \\emph{overlap-compatible modification record}', 0, main.index(old))
assert orphan_start >= 0
orphan = main[orphan_start:main.index(old)]
p340 = r'''\subsection{Local modifications and overlap maps}\label{subsec:II:modification-records}

\begin{definition}[Modifications with specified overlap maps]\hypertarget{tag-P340}{}\label{def:II:overlap-compatible-modification}
\StatementRecord{def:II:overlap-compatible-modification}{proved}{P340}{\cite[\S4.10.8, pp.~980--982; \S4.14.5, p.~985]{Kulikov1977}; \cite[\S\S2,8, pp.~339,341]{Kulikov1981}}
An \emph{overlap-compatible modification record} consists of finite
analytic chart data, centres with their ideals, local blowup or
contraction maps, and overlap isomorphisms, all over the same base.
In each local replacement $X=U\cup V$, the modified chart $U'$
has an overlap $W'\simeq W=U\cap V$ identified by the restriction
of the specified composite of local maps; the resulting space is
$X'=U'\cup_W V$. The record includes these neighbourhoods and
maps. Its inverse reverses each arrow and each overlap isomorphism.
For degenerations over a disc the centres are central and the
maps restrict to isomorphisms over the punctured disc. The local
$\sigma$-constructions used here are those in the cited sections,
including the additional fibre blowups of \cite[\S8, p.~341]{Kulikov1981}.
\end{definition}
'''
pkg.record('D02,D08,D13,D14,D17,D18', 'def:II:overlap-compatible-modification', orphan, p340, 'Number the entire existing analytic operation datum at its first use. Exact opened English source loci identify the composite overlap maps and the missing-fibre additions; no new admissibility premise is inserted.')

new = old
generator_start = new.index('The proper direct image $f_*K_X$')
generator_end = new.index(r'\par\medskip\noindent\textbf{Why every Hopf-birational component is retained.}')
generator_old = new[generator_start:generator_end]
generator_new = r'''Apply \cref{cdp:st:C.2.UN.17} to this proper torus family.
Its canonical evaluation gives the vertical effective divisor in
\eqref{cdp:eq:C.KG.1}. Since the full fibre is reduced, positivity
of every $k_i$ would make $\Omega/f$ holomorphic on the smooth
total space. That would contradict primitivity of the generator,
so $\min_i k_i=0$. Multiplication by a holomorphic base unit
does not change these orders.

'''
new = pkg.edit(new, generator_old, generator_new, 'D08,D12,D23', owner, 'Use the earlier canonical-generator owner, retain the full reduced-fibre primitivity argument, and move the complete bimeromorphic comparison with its equation to P343. This also removes the spurious Step1/full insertion.')
pkg.record('D12,D13,D14,D20', 'lem:II:canonical-bimeromorphic-direct-image', generator_old[generator_old.index('For later comparison,'):], p343, 'One earlier numbered owner retains the complete general direct-image proof, generic surviving-divisor order statement and C.KG.6/tag00PE, for P335, UN75 and the later root construction.')

graph_start = new.index(r'\par\medskip\noindent\textbf{The source\'s actual overlap maps glue global graphs.}') if False else new.index("\\par\\medskip\\noindent\\textbf{The source's actual overlap maps glue global graphs.}")
graph_end = new.index(r'\par\medskip\noindent\textbf{Endpoint classification and the converse record.}', graph_start)
graph_old = new[graph_start:graph_end]
graph_new = r'''\par\medskip\noindent\textbf{The composite graphs and canonical pullback.}
In \cite[\S4.10.8, pp.~980--982]{Kulikov1977}, the finite
contractions in $U$ and inverse-order restorations produce $U'$
whose overlap $W'$ is identified with $W$ by their composite.
Section~4.14.5, p.~985, gives the same comparison at the local
singular charts. The additional fibre blowups in
\cite[\S8, p.~341]{Kulikov1981} leave this overlap unchanged.
These are the data of \cref{def:II:overlap-compatible-modification}.

For a finite $\sigma$-chain, take the closure of the common
biholomorphic graph in the proper image of the fibre product of
its arrow graphs. Both projections are proper. Over $W$ it is
the graph of the specified overlap isomorphism. Glue it to the
identity graph over $V$. The two graphs agree on their overlap,
and properness is local on each projection target; thus the
glued graph is proper over $U\cup V$ and $U'\cup_W V$.
It defines mutually inverse bimeromorphic maps. Iteration gives
\eqref{cdp:eq:C.KG.2}, since all maps are over the disc and are
isomorphisms away from the central fibre. The open covers,
normalization branches and any singular restoration charts
remain part of this finite sequence.

For its smooth endpoints apply
\cref{lem:II:canonical-bimeromorphic-direct-image} with this
glued map as $\phi$. Its pullback \eqref{cdp:eq:C.KG.6} identifies
the primitive canonical generators up to a base unit, and
preserves the orders of all surviving prime divisors.

'''
new = pkg.edit(new, graph_old, '', 'D02,D08,D12,D14,D17,D18', owner, 'Place the exact proper-graph construction before its uses in canonical pullback and divisor survival; retain the full proof and replace Russian-edition locators with the opened English loci.')
new = new.replace(generator_new, generator_new + graph_new, 1)

survival_start = new.index(r'\par\medskip\noindent\textbf{Why every Hopf-birational component is retained.}')
survival_end = new.index(r'\par\medskip\noindent\textbf{The finite reduction and the actual allowed charts.}', survival_start)
survival_old = new[survival_start:survival_end]
survival_new = r'''\par\medskip\noindent\textbf{Preservation of the Hopf components.}
A map $\PP^1\to H$ to a Hopf surface lifts to
$\C^2\setminus\{0\}$ and is constant. Thus every rational curve
on a point blowup of $H$ is one of the finitely many curves
exceptional over $H$, and these surfaces are not uniruled.
Apply \cref{lem:II:nonuniruled-divisors} to the resulting proper
bimeromorphic comparison between the smooth endpoints $X$ and $X_0$
and these compact component
divisors. It preserves their strict-transform primes and their
Hopf birational classes. Its generic-point comparison is exactly
the one used in \eqref{cdp:eq:C.KG.6}; hence their canonical
orders are unchanged. At a canonical-flat endpoint a nowhere-zero
three-form generates $f_{0*}K_{X_0}$, so every order is zero.
This proves $k_i=0$ for every $i\in\mathcal H$, including all
point-blown-up Hopf components.

'''
new = pkg.edit(new, survival_old, survival_new, 'D02,D08,D12,D17,D23', owner, 'Apply the already fully read P236 proper-graph non-uniruled-divisor theorem on the identical compact prime and generic-point map. Keep the Hopf non-uniruled verification and all necessary minimum conclusions; remove the repeated projective/ruled exceptional-divisor proof and the spurious Step2/VII0 insertion.')

oldsource = r'''\ref{cdp:st:C.2.UN.19} identifies every actual class-VII minimal
model in a torus degeneration as Hopf. Thus the
minimum condition just stated implies the
condition in \cite[Theorem~1']{Kulikov1981}.
That theorem applies to proper analytic good
degenerations with trivial fibre canonical
class; its hypotheses do not include
projectivity. The definition of good in
\cite[original Russian ed., pp.~1008--1009]{Kulikov1977} is exactly the smooth
total space and full reduced NC fibre with
smooth components used here.'''
newsource = r'''By \cref{cdp:st:C.2.UN.19}, every class-VII minimal model
of a component of this torus degeneration is Hopf. Hence every
component to which condition~b) of \cite[Theorem~1$'$, p.~340]{Kulikov1981}
applies has canonical coefficient zero. With the source's map
$\pi:X\to\Delta$ equal to $f$ and its coefficients $r_i=k_i$,
that theorem gives a canonical-flat modification. Its good
degenerations are the proper smooth-total analytic families with
reduced normal-crossing fibre and smooth components defined in
\cite[\S1, pp.~957--958]{Kulikov1977}; the general torus has
trivial canonical line. These are precisely the hypotheses here.'''
new = pkg.edit(new, oldsource, newsource, 'D02,D08,D17,D18,D20', owner, 'The complete 1981 theorem/proof and 1977 definition were opened. The explicit f=source pi, ri=ki map establishes sufficiency; necessity remains the separate divisor-survival argument.')

replacements = [
('Here is the exact Euler bookkeeping for these records.', 'The Euler changes are defined as follows.', 'D08'),
('The normal-cone formula also applies to auxiliary\nsingular-centre charts; their contribution is not\nreplaced by a smooth-curve formula.', 'The same normal-cone formula applies to every auxiliary\nsingular-centre chart.', 'D02'),
('using the corrected contraction theorem in\n\\ref{cdp:st:C.2.UN.64}.', 'by \\cite[\\S2, Theorem~2$\'$, pp.~640--642]{FujikiNakano1971}.\nThe source data are $(\\widetilde X,S,M,r)=(\\operatorname{Bl}_A X,\n\\PP^1\\times\\PP^1,\\PP^1,2)$, with the second projection as\nthe ruling; the normal line has degree $-1$ on each of its fibres.', 'D01,D04,D17,D18,D20'),
("\\cite[\\S4.4]{Kulikov1977}. One does not\ndiscard that self-incidence or call this\nintermediate fibre embedded simple NC.", "\\cite[\\S4.4, p.~970]{Kulikov1977}. This intermediate\nfibre has the two indicated normalization branches over its\nself-double curve.", 'D02,D18'),
(r'\cite[\S\S4.10.7--4.10.8,4.14.5]{Kulikov1977}', r'\cite[\S4.10.7--4.10.8, pp.~980--982; \S4.14.5, p.~985]{Kulikov1977}', 'D18'),
('The corrected proof in\n\\cite[\\S8]{Kulikov1981}', 'The construction in\n\\cite[\\S8, p.~341]{Kulikov1981}', 'D01,D18'),
('Here termination is an actual finite\ninduction, rather than a decrease of an\nunspecified complexity.', 'For termination, apply the finite-level argument in\n\\cite[\\S9, pp.~341--342]{Kulikov1981} with minimum zero\nand increment one. The following comparison specifies its levels.', 'D02,D17,D18'),
('The corrected endpoint\nargument in \\cite[\\S10]{Kulikov1981}, using\n\\cite[\\S4.17]{Kulikov1977}', 'The endpoint\nargument in \\cite[\\S10, p.~342]{Kulikov1981}, using\n\\cite[\\S4.17, p.~988]{Kulikov1977}', 'D01,D18'),
('types1\nand2', 'types~1 and~2', 'D23'),
('In this statement the endpoint is an\nactual analytic family. The maps do\nnot replace its neighbourhood by a\ndifferent realization merely because\ntheir central log spaces agree.', 'The endpoint is the analytic family with precisely the\nneighbourhood and overlap maps used in this construction.', 'D02,D08'),
('Euler numbers\nof arbitrary analytic open covers\nare not used.', 'All Euler terms are evaluated on this finite\nsubanalytic subdivision.', 'D02'),
('described and sums; no boundary\npiece is counted twice.', 'described and sums over its disjoint strata.', 'D02'),
('The last defect\nis two rather than one. This\nillustrates why the full normal\ncone was retained.', 'The fibre algebra at the origin is the polynomial algebra\nin the three degree-one classes of $xy,xz,yz$, so its\nprojectivization is $\\PP^2$ and its local defect is two.', 'D02,D08,D22'),
]
for a,b,k in replacements:
    new = pkg.edit(new, a,b,k,owner,'State the exact mathematical comparison positively, preserving its maps and numerical conclusions; use the freshly opened primary locus where cited.')

header_start = new.index(r'\StatementRecord')
header_end = new.index('\n\n', header_start)
header_old = new[header_start:header_end]
header_new = r'''\StatementRecord{cdp:st:C.2.UN.75}{proved}{01EM}{\cref{def:II:overlap-compatible-modification,lem:II:canonical-bimeromorphic-direct-image,lem:II:nonuniruled-divisors,cdp:st:C.2.UN.17,cdp:st:C.2.UN.19,cdp:st:C.2.UN.64,cdp:st:C.2.UN.65,cdp:st:C.2.UN.68,cdp:st:C.2.UN.71,cdp:st:C.2.UN.73,prop:II:section-fibre-contraction}; \cite[Theorem~1$'$, p.~340; \S\S5--10, pp.~340--342]{Kulikov1981}; \cite[\S1, pp.~957--958; \S\S4.2--4.4, pp.~968--970; \S4.10.7--4.10.8, pp.~980--982; \S4.14.5, p.~985; \S4.17, p.~988]{Kulikov1977}}'''
new = pkg.edit(new, header_old,header_new,'D04,D12,D18',owner,'Declare each exact earlier mathematical owner once and the opened English loci; stable identities are retained.')
new = pkg.clean(new, owner)
new = pkg.edit(new, 'an bimeromorphic map', 'a bimeromorphic map', 'D23', owner, 'Restore the article after removing the process adjective.')
new = pkg.edit(new, 'an compact core', 'a compact core', 'D23', owner, 'Restore the article after removing the process adjective.') if 'an compact core' in new else new
new = pkg.edit(new, 'For an blowup', 'For a blowup', 'D23', owner, 'Restore the article after removing the process adjective.')
new = pkg.edit(new, 'For typeI and typeII', 'For type~I and type~II', 'D23', owner, 'Restore the spacing in the two mathematical move names.')
new = pkg.edit(new, r'''For a double curve which is $(-1)$ on both
sides, the same normal bundle calculation
gives the same two-ruling construction.''', r'''For a double curve which is $(-1)$ on both sides,
the normal bundle is again $\OO(-1)\oplus\OO(-1)$.
On its ordinary blowup $\widetilde X$, the exceptional divisor
$E=\PP^1\times\PP^1$ has normal $\OO(-1,-1)$.
Apply the same normal-line contraction theorem with
$(\widetilde X,S,M,r)=(\widetilde X,E,\PP^1,2)$ and the
second projection as the ruling. It gives the ordinary smooth
curve contraction for these exact normal data. Its two
horizontal boundary sections are the two opposite branches
through the triple points.''', 'D12,D17,D20,D25', owner, 'The normal-line contraction is applied directly to the exact exceptional divisor and the other ruling for both moves, including globally repeated NC branches. The type-II exceptional divisor has two horizontal sections, so the one-section/SNC statement P335 is not used for that move; the complete already-opened analytic source covers its normal data. This is a receiving application-map clarification, with every original two-ruling conclusion retained.')
new = pkg.edit(new, r'''At a smooth full reduced final fibre
the argument following \eqref{cdp:eq:C.KG.6} shows
that every Hopf-birational component
has order zero.''', r'''For the resulting smooth total space, apply
\cref{lem:II:nonuniruled-divisors} to the inverse proper
bimeromorphic map and a compact Hopf-birational component.
It corresponds to a prime at the canonical-flat endpoint.
The order comparison of \cref{lem:II:canonical-bimeromorphic-direct-image}
therefore makes its canonical order zero.''', 'D04,D12,D20', owner, 'After C.KG.6 moves, give the exact inverse-map application rather than an ambiguous reference to an argument following that equation.')
new = pkg.edit(new, 'The finite reduction and the allowed charts.', 'The finite reduction and its local maps.', 'D08', owner, 'Name the local mathematical maps in the proof heading.')
pkg.equations.append(dict(old_tag='C.KG.6', label='cdp:eq:C.KG.6', owner='lem:II:canonical-bimeromorphic-direct-image'))

fragment = p340 + '\n\\subsection{Canonical-flat reduction}\\label{subsec:II:canonical-flat-reduction}\n\n' + new + '\n\\subsection{Maximal Hopf component reduction}\\label{subsec:II:maximal-hopf-reduction}\n'
pkg.guard('P343-before-P335', r'\subsection{Section and ruling-fibre contractions}\label{subsec:II:section-fibre-contractions}', p343 + '\n' + r'\subsection{Section and ruling-fibre contractions}\label{subsec:II:section-fibre-contractions}', 'Place the canonical direct-image owner before its first contraction application.')
pkg.guard('P335-canonical-map', old335, new335, 'Replace only the repeated canonical direct-image paragraph and hidden input, after complete proof comparison.')
pkg.guard('P340-UN75-unit', orphan + old, fragment, 'Number the complete existing overlap datum and replace the complete UN75 unit; the following open remainder has its own subsection.')

replayed = main
for g in pkg.guards:
    assert replayed.count(g['old']) == 1, g['key']
    replayed = replayed.replace(g['old'],g['new'],1)
for pattern in [r'\\label\{([^{}]+)\}',r'\\hypertarget\{([^{}]+)\}']:
    before=Counter(re.findall(pattern,main)); after=Counter(re.findall(pattern,replayed))
    assert all(after[k]==v for k,v in before.items()), [(k,v,after[k]) for k,v in before.items() if after[k]!=v]
pkg.write(fragment)
for suffix,text in [('P343',p343),('P335_receiving',new335),('UN75_receiving',new)]:
    (OUT / ('S6_SERIES_PUBLISH_II_sec11_canonical_flat_' + suffix + '.tex')).write_text(text + '\n',newline='\n')
print('Three guards replay once; every old label/target preserved. New tags P340/P343. No main write.')
