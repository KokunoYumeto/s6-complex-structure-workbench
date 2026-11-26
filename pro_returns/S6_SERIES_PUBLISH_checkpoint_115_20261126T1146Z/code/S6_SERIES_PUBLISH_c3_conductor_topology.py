from S6_SERIES_PUBLISH_c3_edit import *

text = SOURCE.read_text()
a = text.index('The branch permutations in P4.14 have explicit local realizations.')
b = text.index('\\begin{proposition}[Finite rank drop of a normalization]', a)
old = text[a:b]
new = r"""\begin{remark}[Local threefolds with permuted conductor branches]
\hypertarget{tag-P242}{}\label{rem:II:permuted-conductor-branches}
\StatementRecord{rem:II:permuted-conductor-branches}{proved}{P242}{\SeriesRef{night:P4.14}}
The branch permutations in \cref{night:P4.14} give local smooth
threefolds with irreducible divisors. Take an elliptic curve $C$
with a free translation $\tau$ of order two or three. The map
$(x,y)\mapsto(x,x^2-y)$ exchanges the two tacnode branches and
preserves $y(y-x^2)$. The order-three map
$(x,y)\mapsto(-y,x-y)$ cycles the three branches and preserves
$xy(x-y)$. The diagonal action on $C$ times a small invariant
neighbourhood of the origin is free. Its quotient is a smooth
threefold, and the divisor is irreducible because the action
permutes its branches transitively. Its normalization conductor
is one elliptic curve mapping to $C/\langle\tau\rangle$ with
degree two or three.
\end{remark}

"""
apply_edit(old, new, 'II-C3-CONDUCTOR-BRANCH-OWNER',
    ['D02','D04','D13'], 'rem:II:permuted-conductor-branches',
    'Finite conductor covers and the normalization differential',
    'The exact free diagonal actions, invariant equations and degree-two/three conductor maps remain. Assign the local construction a numbered owner and replace internal P4.14 prose with its live reference; remove only the non-assertion about compact smoothing.')

apply_edit(r'\subsection{The specialization group and the unibranch case}',
    r'\subsection{The specialization fundamental group}',
    'II-C3-SPECIALIZATION-HEADING', ['D14'], 'night:P4R.1',
    'The specialization fundamental group',
    'The subsection proves the fundamental-group assertion. Its unibranch application has its own later subsection and proof.')
text = SOURCE.read_text()
a = text.index('Write the degeneration as $f:X\\to\\Delta$.', text.index('\\label{night:P4R.1}'))
b = text.index('Write $U^*=U\\setminus S$.', a)
old = text[a:b]
new = r"""Write the degeneration as $f:X\to\Delta$.
The neighbourhood-retraction statement immediately after
Definition~1 of \cite[p.~85]{BobadillaKollar2012} applies to
this proper holomorphic map of complex spaces. It gives an
open neighbourhood $V$ of $0$ and a retraction
$r_V:f^{-1}(V)\to S$. Choose a disc $\Delta_\epsilon\subset V$
and put $U=f^{-1}(\Delta_\epsilon)$.
For the inclusion $i:S\to U$ and the restriction
$r=r_V|_U$, the equality $r\circ i=\operatorname{id}_S$ holds.

"""
apply_edit(old,new,'II-C3-SPECIALIZATION-RETRACTION',['D17'],
    'night:P4R.1','Fundamental group of an irreducible fibre, opening proof',
    'Opened the exact published p.85 after Definition1. Its proper-complex-space neighbourhood retraction applies directly; restriction to the smaller disc supplies exactly the left inverse used at the proof end. The explicit triangulation proof of that known input is removed; the meridian and group quotient arguments remain in full.')

text = SOURCE.read_text()
a = text.index('Its exceptional\nintersection matrix $M$', text.index('\\label{night:P4.12}'))
b = text.index('\nAdjunction gives', a)
apply_edit(text[a:b], r"""By \cref{lem:II:exceptional-intersection},
applied to this resolution $\pi:T\to S$, the exceptional
intersection matrix $M$ is negative definite and $-M^{-1}$
has positive entries.
""", 'II-C3-CANONICAL-MATRIX-OWNER', ['D12'], 'night:P4.12',
    'Irreducible fibres of torus fibrations, Step2',
    'Transport the common analytic intersection-matrix proof to the earlier lemma P243. Here its normal surface N is the present S and its resolution is this same pi; no change of the discrepancy equation or minimality hypothesis.')
text = SOURCE.read_text()
a = text.index('The inverse of a negative definite', text.index('\\label{night:P4.12}'))
b = text.index('The discrepancy equations', a)
apply_edit(text[a:b], '', 'II-C3-CANONICAL-INVERSE-OWNER', ['D12'],
    'night:P4.12','Irreducible fibres of torus fibrations, Step2',
    'The spectral-series inverse argument is included once in P243, with connectedness giving strict positivity. The receiving discrepancy inequality follows by multiplying the same nonnegative right side by M inverse.')

text = SOURCE.read_text()
a = text.index('\\item Let $E_1,\\ldots,E_r$', text.index('\\label{night:P4R.6}'))
b = text.index('\\item Write $D=D_{\\rm str}', a)
old = text[a:b]
new = r"""\item Let $E_1,\ldots,E_r$ be the exceptional curves over a
singular point $p\in N$, and put $M_{ij}=E_i\cdot E_j$.
Apply \cref{lem:II:exceptional-intersection} to the given
resolution $\pi:T\to N$. The matrix $M$ is negative definite,
and every entry of $-M^{-1}$ is positive. Thus $Md=-b$ with
$b_i\ge0$ gives $d_i\ge0$, with strict positivity of every
$d_i$ when $b\ne0$.

"""
apply_edit(old,new,'II-C3-POLE-MATRIX-OWNER',['D12'],
    'night:P4R.6','Conductor and exceptional pole divisor, item2',
    'The connectedness, local-principal-divisor weighted identity and inverse positivity now have one complete earlier proof in P243. The map pi, surface N, exceptional curves and equation Md=-b are exactly those of that lemma. The conductor coefficients, adjunction and local sphere exclusion remain unchanged.')

apply_edit(r'\subsection{Normalization cohomology for the remaining positive cases}',
    r'\subsection{Normalization cohomology and conductor schemes}',
    'II-C3-NORMALIZATION-COHOMOLOGY-HEADING',['D08','D14'],
    'night:P4.33','Normalization cohomology and conductor schemes',
    'The title names the two proved cohomological formulas without a process-dependent remaining-case description.')
old = r"""In the ruled double-horizontal case, with section $H$ of genus
$g\ge1$, a contracted $H$ gives $h^1(N,\mathcal O_N)=0$ and
$p=g$. A noncontracted $H$ gives $p=0$ and
$h^1(N,\mathcal O_N)=g$."""
new = r"""For the ruled case, suppose that $T$ is obtained by point blowups
from a $\mathbb P^1$-bundle over a curve $E$ of genus $g\ge1$,
that the induced ruling has a section $H$, and that the pole
divisor of \cref{night:P4R.6} has horizontal part $2H$ and
rational vertical trees as its remaining support. A contracted
$H$ gives $h^1(N,\mathcal O_N)=0$ and $p=g$.
A noncontracted $H$ gives $p=0$ and
$h^1(N,\mathcal O_N)=g$."""
apply_edit(old,new,'II-C3-NORMALIZATION-RULED-SCOPE',['D22'],
    'night:P4.33','Normalization cohomology and the conductor Euler characteristic, last clause',
    'Expand the formerly implicit ruled double-horizontal case into the exact ruling, section, point-blowup and rational-vertical-tree data used by the unchanged last proof item. These are the same case hypotheses; the general formulas in the first three items and all conclusions are unchanged.')
apply_edit('and the actual point blowups\npreserve these groups.',
    'and the point blowups\npreserve these groups.',
    'II-C3-NORMALIZATION-BLOWUPS',['D08'],'night:P4.33',
    'Normalization cohomology, item4',
    'The same blowup pullbacks and restriction isomorphism are retained; remove the process adjective.')
print('Complete old proofs were read; receiving proof rereading and unit closure follow separately.')
