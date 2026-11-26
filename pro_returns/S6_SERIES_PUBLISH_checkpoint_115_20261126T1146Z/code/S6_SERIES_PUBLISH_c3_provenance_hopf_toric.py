#!/usr/bin/env python3
"""Prepare complete bounded Hopf/group/toric units; never edit shared source."""
from pathlib import Path
from collections import Counter
import csv
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
TMP = ROOT.parents[1] / 'tmp'
OUT = ROOT / 'agents/continuation3_provenance/hopf_toric'
OUT.mkdir(parents=True, exist_ok=True)
main = (ROOT / 'S6_SERIES_PUBLISH_II.tex').read_text()
old = {'hopf': (TMP/'c3_hopf_unit_old.tex').read_text(),
       'toric': (TMP/'c3_toric_unit_old.tex').read_text()}
texts = old.copy()
changes = []


def edit(unit, before, after, kinds, reason, owner=''):
    assert texts[unit].count(before) == 1, (unit, before[:100], texts[unit].count(before))
    texts[unit] = texts[unit].replace(before, after)
    changes.append(dict(change_id=f'II-C3-HOPF-{len(changes)+1:03d}', type=kinds,
        statement_id=owner, old_location=f'{unit}: complete bounded original unit',
        old_page='final concordance pending', new_location=f'{unit}: receiving unit/application',
        new_page='integrated build pending', old_text=before, new_text=after,
        reason=reason, review_status='Draft; full receiving read pending'))


def between(unit, first, last, after, kinds, reason, owner=''):
    text=texts[unit]; a=text.index(first); b=text.index(last,a)
    edit(unit,text[a:b],after,kinds,reason,owner)


edit('hopf',r'\subsection{Hopf components and fibre boundaries}\label{subsec:II:hopf-component-boundaries}',
     r'\subsection{Hopf curves in the fibre boundary}\label{subsec:II:hopf-component-boundaries}',
     'D14','Give UN38 its own descriptive unit; retain the existing subsection label.', 'cdp:st:C.2.UN.38')
titles={38:'Hopf curves in the fibre boundary',39:'Resolution index and Euler number',
        44:'Fundamental groups and dual complexes',47:'Component groups and geometric genus'}
for n,title in titles.items():
    pat=rf'\\begin\{{proposition\}}\[[^\n]*\]\\hypertarget\{{tag-[^}}]+\}}\{{\}}\\label\{{cdp:st:C\.2\.UN\.{n}\}}'
    m=re.search(pat,texts['hopf']); assert m
    line=m.group(); new=re.sub(r'\[[^\n]*\]',lambda _: '['+title+']',line,count=1)
    if n!=38:
        label={39:'resolution-euler-index',44:'fibre-fundamental-groups',47:'component-geometric-genus'}[n]
        new='\\subsection{'+title+'}\\label{subsec:II:'+label+'}\n\n'+new
    edit('hopf',line,new,'D14;D08','Separate the complete owner and proof into a descriptive subsection; shorten the title without changing its mathematical assertion.',f'cdp:st:C.2.UN.{n}')

# UN38: same canonical evaluation and the complete axis obstruction.
between('hopf',r'\item The proper direct image $f_*K_U$',r'\[\n                   \operatorname{div}(\omega)'.replace('\\n','\n'),
    r'''\item Apply the canonical-evaluation assertion of
\cref{cdp:st:C.2.UN.17} to this map $f:U\to\Delta$.
Its generator $\omega$ of $f_*K_U$, evaluated on $U$, has divisor
''','D12','Use the same proper torus family and canonical evaluation section as UN17; retain its divisor and the distinct neighbourhood adjunction application.','cdp:st:C.2.UN.38')
edit('hopf',r'\cite[Theorem~2.1]{Khaled2024Hopf}'+ '\nand '+r'\cite[\S1.1]{Nakamura2008VII}.',
    r'\cite[Theorem~2.1, arXiv v2 p.~5; normal forms (1), p.~3]{Khaled2024Hopf}'+ '\nand '+r'\cite[\S1.1, Theorem~1.1.2, p.~2]{Nakamura2008VII}.',
    'D18','Identify the opened normal-form version and the precise finite primary-cover theorem.','cdp:st:C.2.UN.38')
between('hopf',r'\item Finally let $\nu:H\to S$',r'\item We also verify the curve assertion',
    r'''\item Let $\nu:H\to S$ be the smooth minimal Hopf
normalization. Apply the conductor purity in
\cref{lem:II:conductor-duality} to the reduced hypersurface $S$:
its nonnormal locus $C\subset S$ is a curve wherever nonempty.
Its finite inverse image in $H$, together with the pullbacks of
all other central components, defines $B\subset H$. Each of the
latter pullbacks is a Cartier divisor on the smooth $H$, so $B$
is a union of compact curves.
On $H\setminus B$, the normalization map is an isomorphism onto
the regular locus of the reduced fibre: normalization is an
isomorphism over the normal locus, and $H$ is smooth.

''','D12;D02','Apply the earlier conductor-purity owner to the same hypersurface component; state the exact isomorphism on the complementary regular locus.','cdp:st:C.2.UN.38')
between('hopf',r'\item We also verify the curve assertion',r'For a secondary\nHopf surface'.replace('\\n','\n'),
    r'''\item Apply \cref{lem:II:hopf-curves} to $H$ and to its
primary cover. It identifies all compact curves on the diagonal
algebraic-dimension-zero cover with its two axes, and all compact
curves on the non-diagonal cover with its single axis; these curves
are disjoint. Hence an axis not contained in $B$ is disjoint from
$B$. The neighbourhood canonical trivialization
\eqref{cdp:eq:C.HB.3}, pulled back by the normalization isomorphism
there, contradicts the diagonal normal-line calculation or the
non-diagonal higher-jet calculation above. Thus every axis lies in $B$.
''','D12;D17','Replace the repeated complete Hopf curve classification by the earlier opened and proved P248 owner, with the exact cover, boundary and neighbourhood-trivialization maps. Preserve the distinct higher-jet obstruction.','cdp:st:C.2.UN.38')
edit('hopf','The\ncovering has the same\nalgebraic dimension:\nmeromorphic functions\ndescend through their\nelementary symmetric\npolynomials.',
    'The cover also has algebraic dimension zero: if a meromorphic\nfunction upstairs were nonconstant, its finitely many conjugates\nover the downstairs function field have elementary symmetric\nfunctions downstairs. If all those coefficients were constant, the\nfunction would take values in the finite root set of a constant\npolynomial and would be constant on the connected cover. Thus a\nnonconstant upstairs function would give a nonconstant downstairs\ncoefficient.',
    'D20;D22','Spell out the finite-function-field comparison used to transfer algebraic dimension zero to the primary cover.','cdp:st:C.2.UN.38')

# UN39: keep every monodromy value and both geometric index calculations.
between('hopf','The statement classifies\nthis numerical property of actual fibres;',r'\end{proposition}',
    '', 'D02;D11','The proper family, full divisor and chosen embedded resolution already give the precise domain of the numerical assertion.','cdp:st:C.2.UN.39')
between('hopf',"The proper analytic A'Campo comparison",'says for every positive $k$ that',
    r'''Apply \cref{night:P4.13} with its map $f$, resolution $\pi$
and cohomology monodromy $T$ equal to those here. The cup-product isomorphisms
$\bigwedge^qH^1(F,\Z)\simeq H^q(F,\Z)$ intertwine its exterior
powers with monodromy on every degree. Thus
\eqref{cdp:eq:C.MS.6} ''','D12;D04','Use the identical family/resolution and cohomology monodromy in the single trace owner; name the exterior-power map.','cdp:st:C.2.UN.39')
between('hopf',r'\item We now compare the original support and',r'\item Iterating the actual proper maps in',
    r'''\item For each blowup $\sigma:U'\to U_0$ in $\pi$, let
$Z\subset S_0$ be its connected smooth centre and
$S'=(\sigma^{-1}S_0)_{\rm red}$. Apply
\cref{lem:II:blowup-topology} with
$(Y,Z,S,Y',S',r)=(U_0,Z,S_0,U',S',c)$, where
$c=\operatorname{codim}_{\C}(Z,U_0)$. Its full-inverse-image formula
\eqref{cdp:eq:C.ZC.8} gives $e(S')-e(S_0)=(c-1)e(Z)$.
This is $2$ for a point and $2-2g(Z)$ for a smooth connected
curve. The local exceptional factor of order
$\mu=\operatorname{ord}_Z(f_0)$, where $f_0$ is the pullback of $f$
to $U_0$, changes the full divisor coefficient;
the reduced inverse image still contains the entire projective
fibre $\PP^{c-1}$ used in that formula.

''','D12','Transfer the identical Euler formula and its legacy target to P234, with the complete source/target substitution and full-fibre multiplicity map.','cdp:st:C.2.UN.39')
edit('hopf','This proves independence\nby the actual blowup comparisons;\nno comparison between unrelated\nfillings is required.',
    'This proves independence for every embedded resolution of the\ngiven family.',
    'D02;D11','Keep the positive fixed-family scope of resolution independence.','cdp:st:C.2.UN.39')
between('hopf','The exact integer-matrix calculation in\n',r'\item For a concrete check of the geometric',
    r'''For each characteristic polynomial, use the direct sum $A_0$
of its integral cyclotomic companion matrices. If $\lambda_1,
\ldots,\lambda_4$ are the eigenvalues with their multiplicities,
triangularization gives
$\det(I-T^k)=\prod_{i=1}^4(1-\lambda_i^k)=\det(I-A_0^k)$.
The finite average in \eqref{cdp:eq:C.ZC.2} therefore gives the
displayed values for the full monodromy, including its unipotent
part. Summing the M\"obius coefficients in
\cref{cdp:st:C.2.UN.11} gives the same averages by
\eqref{cdp:eq:C.ZC.6}.

''','D09;D20','Move both code/output paths to program158/157 destinations as appropriate; preserve the complete determinant method and exact companion-to-monodromy eigenvalue comparison.','cdp:st:C.2.UN.39')
edit('hopf',r'\item For a concrete check of the geometric'+ '\nterms, start from',
    r'\item Starting from', 'D08;D21','Present the two explicit geometric index computations as applications of the formula.','cdp:st:C.2.UN.39')

# UN44: all fundamental-group presentations and the quantitative estimates remain.
between('hopf','These are constraints and exact group formulas\n',r'\end{proposition}',
    '', 'D02;D11','The proper degeneration and arbitrary positive divisor multiplicities are already the full statement domain.','cdp:st:C.2.UN.44')
edit('hopf',r'\begin{proof}\leavevmode\par',r'\begin{proof}',
    'D23','Remove redundant paragraph controls at the proof opening.','cdp:st:C.2.UN.44')
between('hopf',r'\item \par\medskip\noindent\textbf{The actual small-tube retraction.}',
    'Put $\\varphi=|f|^2$',
    r'''\item Apply \cref{lem:II:compact-analytic-tube} to $f$ and
choose a sufficiently small compact closed tube
$U_\epsilon=f^{-1}(|z|\le\epsilon)$. Its inclusion of $S$ is a
homotopy equivalence and has a strong deformation retraction.
For the quantitative gradient construction, ''',
    'D12;D08','Use P233 for the shared tube/retraction conclusion while retaining the separate quantitative gradient bounds and their exact construction below.','cdp:st:C.2.UN.44')
edit('hopf','This also proves the needed retraction\nfor every later resolved or covered tube. No invariant-cycle\nsurjectivity is involved.',
    'For every later resolved or covered tube,\n\\cref{lem:II:compact-analytic-tube} applies to its proper map to\nthe disc.',
    'D12;D02','State the exact repeated family-level application of the single tube owner.','cdp:st:C.2.UN.44')
edit('hopf','In particular\nthis construction does not presume that the cover of an individual\n$S_i$ is connected or that it has degree one.',
    'The inverse image of an individual $S_i$ is the finite cover\ninduced by restricting this connected covering of the whole tube.',
    'D02','State the restriction morphism while retaining the full, possibly disconnected component scope.','cdp:st:C.2.UN.44')
edit('hopf','Thus no choice of the connected components over $S_i$\nhas omitted a meridian.',
    'These cosets enumerate all lifts over every component $S_i$.',
    'D02','Express completeness through the stated coset enumeration.','cdp:st:C.2.UN.44')
between('hopf','The Smith-normal-form comparisons in\n',r'\end{enumerate}',
    '', 'D09','Move the finite presentation-test program to appendix158; the displayed mutually inverse lattice maps prove the entire integral assertion.','cdp:st:C.2.UN.44')
between('hopf','A smooth vertical point or curve blowup induces an isomorphism on',r'\[\n              \pi_1(S^{\rm res})'.replace('\\n','\n'),
    r'''Apply \cref{lem:II:blowup-topology} to each smooth point or
curve centre of $\pi:U^{\rm res}_\epsilon\to U_\epsilon$.
The blowdown induces an isomorphism of total-space fundamental
groups. The inclusions $S^{\rm res}\hookrightarrow U^{\rm res}_\epsilon$
and $S\hookrightarrow U_\epsilon$ are homotopy equivalences by
\cref{lem:II:compact-analytic-tube}. They form a commutative square
with the blowdown and its restriction to the full inverse image.
Consequently the latter restriction gives
''','D12','Replace the repeated disc-bundle/van-Kampen proof by P234, preserving the blowdown-induced map through the exact inclusion square.','cdp:st:C.2.UN.44')
between('hopf',r'\cite[\S3, Theorem~2]{Lojasiewicz1964}. The map $p$ is a homotopy',
    r'\item  Van Kampen',
    r'''\cite[\S3, Theorem~2, p.~464]{Lojasiewicz1964}. Apply
\cref{lem:II:proper-conductor-pushout} successively to
$(E_1\cup\cdots\cup E_{k-1})\sqcup E_k\to E_1\cup\cdots\cup E_k$,
with closed image locus $C=(E_1\cup\cdots\cup E_{k-1})\cap E_k$
and inverse image the two copies of $C$. Its double-mapping-cylinder
comparison applies to these closed subcomplex inclusions. Applying
the same comparison to the intersections gives exactly the
double-curve cylinders and triple-point triangles in $P$.
Thus $p:P\to E$ is a homotopy equivalence; choose a homotopy
inverse $p^{-1}:E\to P$.

''','D12;D17;D18','Use the exact closed-pushout/cofibration maps of P294, with the compatible triangulation theorem at its opened printed page.','cdp:st:C.2.UN.44')
edit('hopf','This also bounds the rank of its finite-index abelian subgroup,\nrather than only the rank of its abelianization.',
    'The following finite-cover comparison bounds the rank of its\nfinite-index abelian subgroup.',
    'D02','Introduce the specific finite-cover rank argument directly.','cdp:st:C.2.UN.44')
edit('hopf',r'\item  Finally, for the original support already SNC with no triple',
    r'''\item Under the evaluation pairing $H^1(F,\Z)=H_1(F,\Z)^\vee$,
pullback by the homology action $T$ has matrix $T^{\mathsf t}$.
Thus $\det(I-(T^{\mathsf t})^k)=\det(I-T^k)$, as in
\cref{night:P4.13}. The dual parallel-transport convention gives
$T^\vee=(T^{-1})^{\mathsf t}$, and
$\det(I-(T^\vee)^k)=\det(I-T^{-k})=
\det(T)^{-k}\det(T^k-I)=\det(I-T^k)$.
Here $\det T=1$ by preservation of the complex orientation and
$\operatorname{rank}\Lambda=4$ supplies the positive last sign.
For the original support already SNC with no triple''',
    'D20;D22','Prove the precise H1/H¹ inverse-transpose comparison asserted in the statement, including determinant and rank signs.','cdp:st:C.2.UN.44')

# UN47: retain the full finite-cover and subgroup-separability proof.
between('hopf','The assertion \\eqref{cdp:eq:C.PF.3} is a restriction',r'\end{proposition}',
    '', 'D02;D11','The statement already fixes the actual proper family and induced component maps.','cdp:st:C.2.UN.47')
between('hopf','Use the strong deformation retraction of \\ref{cdp:st:C.2.UN.44}',
    'Given a finite quotient',
    r'''Use \cref{lem:II:compact-analytic-tube} on a sufficiently
small tube. Its central inclusion and radial annulus comparison
identify the fundamental groups of the open tube, a smaller
closed tube and $S$ with $\Gamma$. ''',
    'D12','Apply the earlier P233 owner to the same open/closed tube inclusions used by the finite étale cover construction.','cdp:st:C.2.UN.47')
edit('hopf','This comparison\ndoes not require the original cover to be a pure base cover.',
    'The degree-$a$ Stein base cover and the fibre lattice cover\n$\\C^2/\\Lambda^\\prime\\to\\C^2/\\Lambda$ are the two maps in this\ncomparison.', 'D02;D20','State both exact finite maps in place of the negative scope clause.','cdp:st:C.2.UN.47')
edit('hopf','No residual-finiteness assertion for a general degeneration\ngroup is being imported.','',
    'D02','The proof already establishes residual finiteness from the displayed finite-index finitely generated abelian subgroup.','cdp:st:C.2.UN.47')
edit('hopf','The same blowup maps induce isomorphisms on\n$\\pi_1$, by the $S^3$ and $\\PP^1$ neighbourhood comparison.',
    'The same point-blowup maps induce isomorphisms on $\\pi_1$\nby \\cref{lem:II:blowup-topology}, applied to each smooth surface\nand its point centre.',
    'D12','Use P234 with the precise common-resolution surface blowups.','cdp:st:C.2.UN.47')
edit('hopf','the K3 is simply connected and the point blowups do not change\nits fundamental group.',
    'the K3 is simply connected by\n\\cite[author draft, Chapter~7, Corollary~1.4, pp.~127--128]{HuybrechtsK3Draft},\nand \\cref{lem:II:blowup-topology} gives the fundamental-group\nisomorphisms for its point blowups.',
    'D17;D18','Open the exact complete K3 simply-connectedness corollary and proof in the named author-draft pagination; apply it to the given minimal model.','cdp:st:C.2.UN.47')
edit('hopf','By (C.FG.14),',r'By \eqref{cdp:eq:C.FG.14},','D04','Replace a printed legacy number by its preserved equation label.','cdp:st:C.2.UN.47')
edit('hopf','By (C.FG.16),',r'By \eqref{cdp:eq:C.FG.16},','D04','Replace a printed legacy number by its preserved equation label.','cdp:st:C.2.UN.47')
edit('hopf','For a component with $\\chi(\\OO_{Z_i})=1$, its fundamental-group\nimage in $\\Gamma$ is zero, with just the following possible\ngroup configuration:',
    'For a component with $\\chi(\\OO_{Z_i})=1$, its fundamental-group\nimage in $\\Gamma$ is either trivial or satisfies\n',
    'D22','State the two precise group alternatives directly; the nontrivial alternative and all its consequences remain unchanged.','cdp:st:C.2.UN.47')

# Receiving comparison: state the precise cover before using its a=0 curve list.
between('hopf',r'\item Apply \cref{lem:II:hopf-curves} to $H$ and to its',
    r'\end{enumerate}',r'''\item Let $\pi:H'\to H$ be a finite unramified primary cover,
using the identity map when $H$ is primary, and put $B'=\pi^{-1}B$.
The surface $H'$ has algebraic dimension zero. Indeed the elementary
symmetric functions of the finitely many local sheets of any
meromorphic function on $H'$ glue to meromorphic functions on $H$.
If all these coefficients were constant, that function would take
values in the finite root set of a constant polynomial and would
be constant on connected $H'$. Thus a nonconstant function on $H'$
would give a nonconstant coefficient on $H$.

Apply \cref{lem:II:hopf-curves} to $H'$. Its compact curves are
the two axes in the diagonal case and the single axis in the
non-diagonal case, and distinct curves are disjoint. Therefore
an axis not contained in $B'$ is disjoint from $B'$.
Since $\pi$ is unramified, $K_{H'}\simeq\pi^*K_H$;
the normalization isomorphism over $H\setminus B$ and this
pullback give the canonical-neighbourhood trivialization
\eqref{cdp:eq:C.HB.3} along that axis. It contradicts the diagonal
normal-line calculation or the non-diagonal higher-jet calculation.
Hence every axis lies in $B'$. A curve on $H$ outside $B$ would
have a compact curve component in its finite inverse image outside
$B'$. The same axis list excludes it. Thus every curve on $H$
lies in the fibre boundary.

''','D12;D20;D22','Order the finite-cover premises before the curve classification, explicitly identify the pulled-back canonical line, and retain the complete primary and secondary conclusions.','cdp:st:C.2.UN.38')
edit('hopf','Its normal line has torsion, so \\eqref{cdp:eq:C.HB.1}\nalone gives no contradiction. Instead,',
    'The normal-line quotient has multiplier $\\beta$ over\n$z\\mapsto\\beta^r z$; the function $z$ trivializes its $r$th\ntensor power. The obstruction uses the canonical line on a\nneighbourhood:',
    'D02;D20','Replace the negative contrast by the exact normal-power trivialization and the distinct canonical-neighbourhood morphism used in the proof.','cdp:st:C.2.UN.38')
edit('hopf',r'\item We first compute the resolved support without'+ '\nany reduction of its multiplicities. Put',
    r'\item For the full resolved divisor, put',
    'D02;D08','State the full divisor scope directly.','cdp:st:C.2.UN.39')
edit('hopf','The surface Euler numbers have disappeared:\nthe open surface contribution is the finite\nmonodromy average computed in \\eqref{cdp:eq:C.ZC.6}.',
    'The open surface contribution is the finite monodromy average\n\\eqref{cdp:eq:C.ZC.6}.',
    'D08','State the computed contribution without narrating its elimination.','cdp:st:C.2.UN.39')
edit('hopf','Summing the M\\"obius coefficients in\n\\cref{cdp:st:C.2.UN.11} gives the same averages by\n\\eqref{cdp:eq:C.ZC.6}.',
    'With $a_n=\\sum_{N_j=n}e(E_j^\\circ)$ as in\n\\cref{cdp:st:C.2.UN.11}, equation \\eqref{cdp:eq:C.ZC.6}\nalso gives $j(T)=\\sum_n a_n$.',
    'D20;D21','Identify the exact coefficient grouping whose sum equals the average; retain the mathematical identity rather than reporting agreement.','cdp:st:C.2.UN.39')
edit('hopf','\\item Starting from a smooth torus support\nwith identity monodromy. A point blowup',
    '\\item Start from a smooth torus support with identity monodromy.\nA point blowup',
    'D23','Correct the receiving sentence fragment.','cdp:st:C.2.UN.39')
edit('hopf','Its inclusion of $S$ is a\nhomotopy equivalence and has a strong deformation retraction.\nFor the quantitative gradient construction, Put $\\varphi=|f|^2$',
    'Its inclusion $i:S\\hookrightarrow U_\\epsilon$ is a\nhomotopy equivalence. Let $H$ be the strong deformation retraction\nprovided there. The quantitative gradient estimates for this tube\nare as follows. Put $\\varphi=|f|^2$',
    'D12;D23','Use the single earlier retraction owner for the later covering maps; retain the separately labelled gradient estimates.','cdp:st:C.2.UN.44')
between('hopf','It consequently has a limit in $S$. Let $H(x,q)$',
    r'\end{enumerate}',
    r'''The bound tends uniformly to zero with $b$. The group maps
below use the retraction $H$ and the inverse of the inclusion
$i_*:\pi_1(S)\to\pi_1(U_\epsilon)$ supplied by
\cref{lem:II:compact-analytic-tube}.

''','D12','Keep the exact analytic gradient inequality, normalized vector field and length bound. Transfer the second complete retraction proof to this exposed comparison record: its time-q*phi map and limiting retraction induce the same inverse of i_* as P233. Explicitly, r_P233 composed with the old gradient homotopy joins r_P233 to r_gradient and fixes S. Thus all later based group/cover maps agree, while the paper has one topological retraction owner.','cdp:st:C.2.UN.44')

# UN68: the same component classification, now with an exact toric-model application.
edit('toric',r'\subsection{Rational toric components}',
    r'\subsection{Rational toric components and the dual torus}\label{subsec:II:rational-toric-components}',
    'D14','Give the entire rational-toric owner a descriptive stable subsection destination.','cdp:st:C.2.UN.68')
edit('toric','[Rational toric component pairs and the exact dual torus]',
    '[Toric components and the dual torus]', 'D08;D14','Shorten the mathematical title without changing its statement.','cdp:st:C.2.UN.68')
between('toric','Together with \\ref{cdp:st:C.2.UN.65} this identifies',r'\end{proposition}',
    '', 'D02;D11','Keep the given full reduced canonical-flat degeneration as the single statement domain; remove its repeated closing scope disclaimer.','cdp:st:C.2.UN.68')
edit('toric','A rational curve on a Hopf surface\nwould lift to $\\C^2\\setminus\\{0\\}$, where\nits coordinate functions are constant. It\nhas no rational cycle either.',
    '\\Cref{lem:II:hopf-curves} identifies every compact irreducible\ncurve on that Hopf minimal model as smooth elliptic. Thus a\nrational cycle cannot persist there.',
    'D12;D17','Use the full Hopf curve owner on the precise class-VII minimal model already supplied by UN19.','cdp:st:C.2.UN.68')
edit('toric','We prove\n\\[\n Q(V,D)\\ge0,',
    'The toric-model comparison below gives\n\\[\n Q(V,D)\\ge0,',
    'D17','Attribute the charge criterion to the exact toric-model morphisms used in its application.','cdp:st:C.2.UN.68')
between('toric',r'\item Follow any sequence of ordinary',r'\item On $\PP^2$',
    r'''\item The point-contraction sequence above identifies $V$ as
a sequence of point blowups of $\PP^2$ or a Hirzebruch surface;
in particular it is projective. Hence $(V,D)$ is a Looijenga pair
in \cite[Definition~1.1, pp.~75--76]{GHK2015}. Apply
\cite[Definition~1.2 and Proposition~1.3, pp.~76--77]{GHK2015}
to obtain the proper birational maps
\[
 (V,D)\xleftarrow{\ \rho\ }(\widetilde V,\widetilde D)
       \xrightarrow{\ \tau\ }(\overline V,\overline D),
\]
where $\rho$ is a toric blowup, $(\overline V,\overline D)$ is a
smooth complete toric pair, and $\tau|_{\widetilde D}$ is an
isomorphism onto $\overline D$.
Factor the two morphisms into ordinary smooth point blowdowns.
For the first $(-1)$-curve $E$ contracted by $\rho$, the identity
$\widetilde D=(\rho^{-1}D)_{\rm red}$ implies that $E$ outside
$\widetilde D$ would map outside $D$ and be disjoint from
$\widetilde D$. This contradicts $\widetilde D\cdot E=1$ in
\eqref{cdp:eq:C.TC.3}. Thus $E$ lies in $\widetilde D$, and its
contraction is the boundary-node blowdown described there.
The full reduced inverse-image identity and the anticanonical
nodal pair persist after that contraction, so induction gives
this description for every step of $\rho$.
Each curve contracted by $\tau$ is outside
the boundary, since $\tau|_{\widetilde D}$ is an isomorphism; the
other case after \eqref{cdp:eq:C.TC.3} identifies each step with
the blowdown of an exceptional curve meeting one smooth boundary
point. These descriptions persist at every intermediate pair.
The first kind of step decreases both $e(V)$ and the number of
boundary components by one, while the second decreases only $e(V)$.
The toric orbit decomposition gives $e(\overline V)=\#\overline D$.
Consequently $Q(V,D)=Q(\widetilde V,\widetilde D)$ is the
nonnegative number of point blowdowns in $\tau$.

If this number is zero, $\tau$ is an isomorphism and $\widetilde V$
has its toric action. The action descends along every step of $\rho$:
for the boundary $(-1)$-curve with primitive fan ray $v_i$, the
self-intersection equation is $v_i=v_{i-1}+v_{i+1}$. Deleting
$v_i$ gives a smooth cone because
$\det(v_{i-1},v_{i+1})=\det(v_{i-1},v_i)=1$.
The associated toric morphism is the ordinary point blowdown in
the two charts $y=xu$ and $x=yv$. Its target identifies with the
given blowdown target by the unique isomorphism agreeing off the
exceptional curve and in these local point-blowup charts.
Thus its full boundary is the image of the specified boundary.
Iteration gives the algebraic two-torus action on the original
pair $(V,D)$. Conversely the orbit decomposition of any smooth
complete toric pair gives $Q=0$. This proves
\eqref{cdp:eq:C.TC.8} with its maps to the given pair.

For the ordinary contraction sequence to a minimal rational pair,
the same two Euler changes give
\[
 Q(V,D)=Q(V_{\min},D_{\min})+a,
\tag{C.TC.9}\hypertarget{tag-012N}{}\label{cdp:eq:C.TC.9}
\]
where $a$ counts the contracted curves outside the successive
boundaries. The minimal equality pairs have the following explicit
coordinates.

''','D17;D20','Replace the repeated general charge proof by the opened GHK toric-model theorem, with complete source/target hypotheses and exact boundary/interior blowdown factorization. Preserve the minimal contraction identity and the explicit original equality coordinates.','cdp:st:C.2.UN.68')
between('toric',r'\item The two minimal computations prove',r'\par\medskip\noindent\textbf{The global charge is zero.}',
    r'''\item Reversing a boundary-node contraction lifts the torus
action through the invariant ideal $(x,y)$; the charts $y=xu$
and $x=yv$ identify its full reduced inverse-image boundary with
the toric boundary. Thus the coordinates above and the maps $\rho,\tau$
describe the action on every charge-zero pair in
\eqref{cdp:eq:C.TC.8}.

''','D17;D12','Keep the explicit action-lifting charts as an application, with the charge criterion owned by the preceding exact GHK comparison.','cdp:st:C.2.UN.68')

# Remove workflow emphases occurrence by occurrence in the remaining source.
for unit in texts:
    for m in list(re.finditer(r'\bactual\b\s*',texts[unit]))[::-1]:
        a,b=m.span(); before=texts[unit][max(0,a-42):min(len(texts[unit]),b+42)]
        # The contextual row records this specific occurrence, not a global token count.
        after=before[:a-max(0,a-42)]+before[b-max(0,a-42):]
        if texts[unit].count(before)!=1:
            before=texts[unit][max(0,a-100):min(len(texts[unit]),b+100)]
            after=before[:a-max(0,a-100)]+before[b-max(0,a-100):]
        edit(unit,before,after,'D08','Remove workflow emphasis; the displayed map, object and hypotheses identify the mathematical construction.')
    # Article agreement after removing the adjective above.
    for m in list(re.finditer(r'\ban\s+(?=(?:trivial|proper|compact|connected|simple|finite|continuous|topological|projective|smooth|birational|torus|toric|two|normal|positive|point|blowup|blowdown)\b)',texts[unit]))[::-1]:
        a,b=m.span(); before=texts[unit][max(0,a-35):min(len(texts[unit]),b+60)]
        after=before[:a-max(0,a-35)]+'a '+before[b-max(0,a-35):]
        edit(unit,before,after,'D23','Restore article agreement after removing workflow emphasis.')

# Flatten the nested proof lists and eliminate internal proof headings.
for unit in texts:
    s=texts[unit]
    for m in list(re.finditer(r'\\par\\medskip\\noindent\\textbf\{[^\n]*\}\s*',s))[::-1]:
        value=m.group()
        if texts[unit].count(value)==1:
            edit(unit,value,'','D14;D08','Use the continuous proof and its numbered steps instead of an internal production-style heading.')
    for line in [r'\begin{enumerate}[label=(\arabic*),leftmargin=1.3em,labelsep=.5em]']:
        while line in texts[unit]:
            pos=texts[unit].index(line)
            # Its matching end is found with balanced enumerate depth.
            depth=0; end=None
            for mm in re.finditer(r'\\(begin|end)\{enumerate\}',texts[unit][pos:]):
                depth += 1 if mm.group(1)=='begin' else -1
                if depth==0:
                    end=pos+mm.end(); break
            assert end
            before=texts[unit][pos:end]
            after=before.replace(line,'',1)
            k=after.rfind(r'\end{enumerate}')
            after=after[:k]+after[k+len(r'\end{enumerate}'):]
            edit(unit,before,after,'D14','Flatten this complete nested proof list into the surrounding numbered argument; all mathematical paragraphs remain in order.','cdp:st:C.2.UN.44')
    texts[unit]=texts[unit].replace('leftmargin=0pt,labelsep=.5em','leftmargin=*')

# Convert exactly the labelled display blocks; keep every equation target.
for unit in texts:
    for m in list(re.finditer(r'\\\[([\s\S]*?)\\\]',texts[unit]))[::-1]:
        if r'\tag{' not in m.group(): continue
        before=m.group(); inside=m.group(1)
        inside=re.sub(r'\\tag\{[^{}]*\}', '', inside)
        inside=re.sub(r'\n[ \t]*\n', '\n', inside)
        after='\\begin{equation}'+inside+'\\end{equation}'
        edit(unit,before,after,'D19;D23','Use section-numbered equation counters and preserve every permanent target and label; remove paragraph breaks inside the display.')
    for m in list(re.finditer(r'\\begin\{equation\}([\s\S]*?)\\end\{equation\}',texts[unit]))[::-1]:
        before=m.group(); after=re.sub(r'\n[ \t]*\n','\n',before)
        if before!=after: edit(unit,before,after,'D23','Remove a blank paragraph inside a displayed-math environment; mathematical tokens are unchanged.')
    texts[unit]=re.sub(r'\n(?:[ \t]*\n){2,}','\n\n',texts[unit]).strip()+'\n\n'

# Keep the complete primary axis list at its exact opened source locus.
edit('hopf',r'''Apply \cref{lem:II:hopf-curves} to $H'$. Its compact curves are
the two axes in the diagonal case and the single axis in the
non-diagonal case, and distinct curves are disjoint. Therefore
an axis not contained in $B'$ is disjoint from $B'$.
''',r'''In the diagonal case, a relation $\alpha^q=\beta^p$ with
positive integers $p,q$ would make $z^q/w^p$ descend to a
nonconstant meromorphic function on $H'$. Since $a(H')=0$,
there is no such relation. Both multipliers have absolute value
less than one, so every relation with nonzero integer exponents
can be inverted to have positive exponents. The curve descriptions in
\cite[arXiv v1, \S2.2.2, p.~4; \S2.2.6, p.~5]{AbashevaDeev2024AB}
therefore give exactly the two axis curves in the diagonal case
and the single axis curve in the non-diagonal case.
Apply \cref{lem:II:hopf-curves} to $H'$ for the disjointness of
distinct curves. An axis not contained in $B'$ is thus disjoint
from $B'$.
''','D12;D18;D20','P248 states smooth ellipticity, square zero and disjointness. Obtain the complete primary axis list from the freshly reopened arXiv-v1 paragraphs instead. The invariant function z^q/w^p supplies the exact map excluding every positive diagonal resonance at algebraic dimension zero. Because both multipliers have absolute value below one, any nonzero-integer resonance can be inverted to have positive exponents. The primary cover and all original boundary conclusions are unchanged.','cdp:st:C.2.UN.38')

edit('hopf',r'''Choose any embedded resolution of the central divisor.
The strict transform of $S_i$ is a smooth resolution of its
normalization, with the same geometric genus as $Z$.
For completeness, the graph of the birational correspondence
between these two smooth resolutions has a common resolution
by point blowups. Pullback and Hartogs extension of holomorphic
''',r'''Choose any embedded resolution of the central divisor and let
$V$ be the strict transform of $S_i$. Both $V$ and $Z$ resolve
the same normal surface $S_i^\nu$. At each of its singular points,
\cite[Proposition~3.10, p.~20]{PopescuPampu2016} factors these maps
through its unique minimal resolution. These local factorizations
glue with the identity over the smooth locus.
Resolve the closure of the graph of $V\dashrightarrow Z$ over
$S_i^\nu$, giving a smooth common resolution $W$.
Its projections $W\to V$ and $W\to Z$ are proper holomorphic
modifications of smooth complex surfaces. By
\cite[Proposition~3.12, p.~20]{PopescuPampu2016}, both are
compositions of point blowups. Pullback and Hartogs extension of holomorphic
''','D17;D18;D20','Apply the analytic minimal-resolution theorem to the common normal surface, with local maps glued over its smooth locus. Resolve the graph over that same surface; its two projections are exactly the proper holomorphic modifications to which Proposition3.12 applies. Retain the point-blowup pullbacks, common map to U and the precise image of the vertex group. Complete named primary statements/context were read; the source recalls their proofs rather than printing them.','cdp:st:C.2.UN.47')

# Alias the one removed duplicate Euler display to its identical full owner.
alias_old=r'\hypertarget{tag-015Z}{}\label{cdp:eq:C.VR.4}'
alias_new=alias_old+'\n '+r'\hypertarget{tag-0193}{}\SsixEquationAliases{\label{cdp:eq:C.ZC.8}}'
assert main.count(alias_old)==1
alias=dict(change_id='II-C3-HOPF-EULER-ALIAS',type='D12;D19',
    statement_id='lem:II:blowup-topology;cdp:st:C.2.UN.39',
    old_location='P234 equation C.VR.4; UN39 equation C.ZC.8',old_page='final concordance pending',
    new_location='P234 equation C.VR.4, with exact C.ZC.8 alias',new_page='integrated build pending',
    old_text=alias_old,new_text=alias_new,
    reason='The complete earlier P234 statement/proof was read. Substitute (Y,Z,S,Yprime,Sprime,r)=(U0,Z,S0,Uprime,Sprime,c): both formulas are e(Sprime)-e(S)=(r-1)e(Z), for the full reduced inverse image of a smooth-centre blowup. Preserve tag0193 and cdp:eq:C.ZC.8 at that identical owner; the UN39 proof retains the point/curve and full-divisor applications.',
    review_status='Draft; full receiving read pending')


def write(name,rows):
    with (OUT/name).open('w',newline='') as f:
        w=csv.DictWriter(f,list(rows[0]),delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)


guards=[]
for unit in texts:
    assert main.count(old[unit])==1,('current source guard',unit)
    (OUT/f'S6_SERIES_PUBLISH_{unit}_proposed.tex').write_text(texts[unit],newline='\n')
    guards.append(dict(change_id=f'II-C3-HOPF-UNIT-{unit}',old_text=old[unit],new_text=texts[unit]))
guards.append({k:alias[k] for k in ['change_id','old_text','new_text']})
write('S6_SERIES_PUBLISH_hopf_toric_guards.tsv',guards)
write('S6_SERIES_PUBLISH_hopf_toric_defects.tsv',changes+[alias])

oldlabels=Counter(re.findall(r'\\label\{([^}]+)\}', ''.join(old.values())))
newlabels=Counter(re.findall(r'\\label\{([^}]+)\}', ''.join(texts.values())+alias_new))
newlabels.subtract(Counter(re.findall(r'\\label\{([^}]+)\}',alias_old)))
oldtags=Counter(re.findall(r'\\hypertarget\{([^}]+)\}', ''.join(old.values())))
newtags=Counter(re.findall(r'\\hypertarget\{([^}]+)\}', ''.join(texts.values())+alias_new))
newtags.subtract(Counter(re.findall(r'\\hypertarget\{([^}]+)\}',alias_old)))
assert not oldlabels-newlabels, oldlabels-newlabels
assert oldtags==newtags,(oldtags-newtags,newtags-oldtags)
for unit,text in texts.items():
    assert not any(ord(c)<32 and c not in '\n\t' for c in text),(unit,'control character')
    assert not re.search(r'\\tag\{|\\path\{|\bactual\b',text),unit
    for env in ['proposition','proof','enumerate','equation','split','array','gathered']:
        assert text.count('\\begin{'+env+'}')==text.count('\\end{'+env+'}'),(unit,env)
    for m in re.finditer(r'\\begin\{equation\}([\s\S]*?)\\end\{equation\}',text):
        assert not re.search(r'\n\s*\n',m.group(1))
status=dict(defect_rows=len(changes)+1,guards=len(guards),old_lines={k:len(v.splitlines()) for k,v in old.items()},
    new_lines={k:len(v.splitlines()) for k,v in texts.items()},preserved_old_labels=sum(oldlabels.values()),
    preserved_old_targets=sum(oldtags.values()),new_statement_tags=[],
    shared_source_changed=False,complete_receiving_read='pending')
(OUT/'S6_SERIES_PUBLISH_hopf_toric_status.json').write_text(json.dumps(status,indent=2)+'\n',newline='\n')
print(json.dumps(status,indent=2))
