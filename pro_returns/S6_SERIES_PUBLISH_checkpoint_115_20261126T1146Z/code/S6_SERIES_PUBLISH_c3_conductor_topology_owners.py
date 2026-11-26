from S6_SERIES_PUBLISH_c3_edit import *

# P4R.1 has no dependency on the normalization section. Its exact full-fibre
# maps supply P210 and the subsequent conductor applications.
text=SOURCE.read_text();a=text.index(r'\subsection{The specialization fundamental group}')
b=text.index(r'\subsection{',a+15);block=text[a:b]
anchor=r'\subsection{Euler localization}\label{subsec:II:euler-localization}'
assert text.count(anchor)==1
new=text[:a]+text[b:]
new=new.replace(anchor,block+anchor,1)
preserve_identifiers(text,new)
SOURCE.write_text(new,newline='\n')
append_rows(ROOT/'S6_SERIES_PUBLISH_defects_II.tsv',[{
    'change_id':'II-C3-MERIDIAN-EARLY-PLACEMENT','type':'D14',
    'statement_id':'night:P4R.1','old_location':'irreducible-support topology',
    'new_location':'Euler identities: before Euler localization',
    'old_text':block,'new_text':block,
    'reason':'Place the complete existing meridian subsection before normalization applications. It uses only the proper torus degeneration and the opened neighbourhood-retraction theorem; no normalization or sign result is a premise.',
    'review_status':'Complete unchanged transferred statement/proof already read; exact block identity verified.'}], 'change_id')

owners=r'''\begin{lemma}[Topology of a normalized compact curve]
\hypertarget{tag-P245}{}\label{lem:II:curve-normalization-graph}
\StatementRecord{lem:II:curve-normalization-graph}{proved}{P245}{}
Let $C$ be a connected compact reduced complex curve, with normalization
$\coprod_{i=1}^c C_i^{\rm norm}\to C$. Write $g_i$ for the genus of
$C_i^{\rm norm}$. Form the incidence graph with one vertex for each
normalization component, one vertex for each singular point, and one
edge for each normalization preimage of a singular point. Let $b$ be
its cycle rank. Base points and paths along a spanning tree give
\[
 \pi_1(C)\simeq
 \Bigl(*_{i=1}^c\pi_1(C_i^{\rm norm})\Bigr)*F_b,
 \qquad e(C)=c+1-2\sum_i g_i-b.
\]
For a virtually abelian $\pi_1(C)$, the possibilities are all $g_i=0$
with $b\le1$, or exactly one $g_i=1$, all other $g_i=0$, and $b=0$.
Consequently $e(C)\ge0$, with equality precisely when $c=1$, $g_1=1$
and $b=0$. The group and Euler formulas apply separately to every
connected component of a disconnected compact reduced curve.
\end{lemma}
\begin{proof}
Join the finitely many points in each singular normalization fibre
by a new star. Collapsing each star identifies exactly that fibre
and gives the topological curve $C$. Compatible triangulations make
these contractible stars subcomplexes, so their collapse is a
homotopy equivalence by \cite[Proposition~0.17, p.~15]{Hatcher2002}.
A spanning tree of the incidence graph joins the normalized surfaces;
the remaining $b$ edges add $b$ circles. Van Kampen gives the displayed
free product with the indicated component maps. If $r_p$ is the number
of normalization preimages of a singular point, then
\[
 b=\sum_p r_p-c-\#\operatorname{Sing}(C)+1,
 \qquad e(C)=\sum_i(2-2g_i)-\sum_p(r_p-1),
\]
which gives the Euler formula. A unibranch singular point has $r_p=1$
and contributes zero to the subtraction.

A surface factor of genus at least two maps onto $F_2$: in the
presentation $\prod_j[a_j,b_j]=1$, send every $b_j$ and all but two
$a_j$ to the identity. Two nontrivial surface factors, two free
generators, or one elliptic factor and a free generator contain
$F_2$ by the free-product normal form. A finite-index subgroup of
index $d$ in $F_2$ is represented by a connected cover of the
two-circle bouquet with $d$ vertices and $2d$ edges, so has rank
$d+1\ge2$. Thus $F_2$ has no finite-index abelian subgroup. Every
subgroup and quotient of a virtually abelian group is virtually
abelian, as follows by intersecting with, or mapping, a finite-index
abelian subgroup. This proves the stated alternatives. Substitution
in the Euler formula proves its nonnegativity and equality assertion.
\end{proof}

\begin{lemma}[Fundamental groups under a canonical-boundary blowup]
\hypertarget{tag-P246}{}\label{lem:II:boundary-blowup-groups}
\StatementRecord{lem:II:boundary-blowup-groups}{proved}{P246}{\SeriesRef{lem:II:canonical-boundary-blowup}}
Use the blowup $\sigma:Z_1\to Z_2$ and divisors $D_1,D_2$ of
\cref{lem:II:canonical-boundary-blowup}. For each connected component
$C_2$ of $(D_2)_{\rm red}$, let $C_1$ be its inverse image in
$(D_1)_{\rm red}$. The maps $\sigma|_{C_1}:C_1\to C_2$ and
$\sigma:Z_1\to Z_2$ induce isomorphisms on fundamental groups.
With base points chosen away from the centre and its exceptional
curve, these isomorphisms commute with the homomorphisms induced
by $C_i\hookrightarrow Z_i$.
\end{lemma}
\begin{proof}
For a component avoiding the centre the boundary map is an
isomorphism. At multiplicity one, \cref{lem:II:canonical-boundary-blowup}
identifies the strict boundary isomorphically with the old boundary.
At multiplicity at least two its inverse image contains the exceptional
$E\simeq\mathbb P^1$, and $C_1/E\to C_2$ is a continuous bijection
from a compact space to a Hausdorff space. It is a homeomorphism.
A compatible triangulation makes $E\subset C_1$ a subcomplex;
van Kampen identifies the quotient group with
$\pi_1(C_1)/\langle\!\langle\pi_1(E)\rangle\!\rangle=\pi_1(C_1)$.
For the surfaces, the blowup replaces a four-ball by the disc bundle
of $\mathcal O_{\mathbb P^1}(-1)$, along their common boundary $S^3$.
Both inserted pieces and the boundary are simply connected, so van
Kampen gives the surface isomorphism. The original inclusions and
$\sigma$ commute as continuous maps, proving the last assertion.
\end{proof}

'''
text=SOURCE.read_text();anchor=r'\begin{lemma}[A square-zero elliptic section and its conductor]'
assert text.count(anchor)==1
apply_edit(anchor,owners+anchor,'II-C3-TOPOLOGY-OWNERS',['D12','D13','D14'],
    'lem:II:curve-normalization-graph; lem:II:boundary-blowup-groups',
    'normalization genus, after canonical-boundary blowups',
    'Extract the existing complete P4R.3/P4R.5 curve graph formulas and P4.21/P4R.3 blowup fundamental-group arguments into single earlier owners. The actual normalization quotient, spanning-tree component maps, exceptional contraction and commuting inclusion maps are explicit. No original conclusion is discarded.')

# Replace the exact duplicate canonical formula and surface-group proof.
old=r'''Write $D'=D''_{\rm strict}+aE$. The canonical blowup formula
\cite[II.3(iv), pp.~17--18]{Beauville1978} gives
\[
 K_{T'}+D'
   =\beta^*(K_{T''}+D'')+(1+a-\mu)E.
\]
Intersection with $E$ and numerical triviality give
$a=\mu-1$. Effectiveness therefore places every centre
on the conductor.'''
new=r'''Write $D'=D''_{\rm strict}+aE$. Apply
\cref{lem:II:canonical-boundary-blowup} with
$(Z_1,Z_2,D_1,D_2,\sigma,m)=(T',T'',D',D'',\beta,\mu)$.
Its canonical line-bundle identity gives $a=\mu-1$ and
places every centre on the conductor.'''
apply_edit(old,new,'II-C3-RULED-BOUNDARY-APPLICATION',['D12'],
    'night:P4R.3','conductor topology proof, third item',
    'Use exactly P232 under the displayed variable identification and the already proved c1(K+D)=0. Keep every subsequent local leaf/subdivision argument.')
old=r'''A point blowup replaces a four-ball by the disc bundle
of $\OO_{\mathbb P^1}(-1)$, with common boundary $S^3$.
Van Kampen therefore shows that it leaves $\pi_1(T)$ unchanged. The preceding
description also proves, at every blowup, that the
inclusion of the reduced conductor induces the same
isomorphism to the fundamental group of the surface.'''
new=r'''At each point blowup,
\cref{lem:II:boundary-blowup-groups} identifies both fundamental
groups and commutes with the conductor inclusion. It therefore
preserves the isomorphism given by the section and ruling.'''
apply_edit(old,new,'II-C3-RULED-BLOWUP-GROUP-APPLICATION',['D12'],
    'night:P4R.3','conductor topology proof, fourth item',
    'Apply the one point-blowup group comparison to the same boundary and surface maps, with the previous canonical-boundary hypotheses.')
text=SOURCE.read_text();a=text.index(r'\item Proposition~\ref{night:P4R.1} makes this group virtually abelian. Let $c$ be')
b=text.index(r'\item Finally equality is impossible here.',a)
old=text[a:b]
new=r'''\item Proposition~\ref{night:P4R.1} makes $\pi_1(C)$ virtually
abelian. Apply \cref{lem:II:curve-normalization-graph} to this same
connected reduced curve. Its component genera $g_i$ and incidence
cycle rank $b$ therefore have the alternatives stated there, and
$e(C)\ge0$. Additivity and \cref{night:P4.13} give
\[
 e(S)=e(S_{\rm reg})+e(C)\ge0.
\]

'''
apply_edit(old,new,'II-C3-RULED-CURVE-GRAPH-APPLICATION',['D12'],
    'night:P4R.3','conductor topology proof, curve graph and group alternatives',
    'Move precisely this general curve calculation to P245 and apply it to the same C. Its equality case remains available to the following strict-positivity argument.')

# The existing minimal-boundary result has exactly the proper degeneration
# with irreducible full fibre mS required by P4R.1.
text=SOURCE.read_text();a=text.index(r'\item That free group is a quotient of a metabelian group.')
b=text.index(r'\begin{equation}',a)
old=text[a:b]
new=r'''\item Restrict the proper map in \cref{cdp:st:A.5.16} to a disc
about this full fibre $mS$. Its total space is smooth, its other
fibres are two-tori, and $S$ is irreducible and reduced.
Thus \cref{night:P4R.1} applies to the same degeneration and makes
$\pi_1(S)$ virtually abelian. Through \eqref{cdp:eq:A.RT.19},
\cref{lem:II:curve-normalization-graph} applies to the same rationally
normalized conductor image and bounds its free-group rank by one.
We obtain
'''
apply_edit(old,new,'II-C3-P210-MERIDIAN-APPLICATION',['D12','D14'],
    'prop:II:minimal-boundary-complements','fifth proof item',
    'Use the earlier exact meridian owner on the same irreducible torus degeneration and the earlier curve graph owner. The existing displayed group possibilities, nonzero-class exclusion and all following one-component arguments are unchanged.')

add_event('lem:II:curve-normalization-graph; lem:II:boundary-blowup-groups; night:P4R.3; prop:II:minimal-boundary-complements',
    'II-C3-ROOT-CURVE-BLOWUP-OWNERS','used and rechecked in this run',
    'Read the complete original P4R.3, P4R.5, P4.21, P4.22 and P210 proofs before extracting their shared arguments; read both receiving lemmas and the complete receiving P4R.3/P210 proofs. All quotient and blowup maps, genus/cycle formulas and virtual-abelian group exclusions are retained with explicit application hypotheses. P4R.1 moved verbatim before every normalization application. Exposed proof comparison, no independent or final-page credit.',
    'S6_SERIES_PUBLISH_II.tex',source='code/S6_SERIES_PUBLISH_c3_conductor_topology_owners.py')
print('P245 and P246 placed after P232; meridian subsection moved earlier; P4R.3 and P210 use the single owners.')
