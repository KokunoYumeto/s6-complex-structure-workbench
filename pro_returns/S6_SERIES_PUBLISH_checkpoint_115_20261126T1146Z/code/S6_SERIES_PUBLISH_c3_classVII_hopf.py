from S6_SERIES_PUBLISH_c3_edit import *
import re

before = SOURCE.read_text()
def statement(text, label):
    p = text.index(r'\label{' + label + '}')
    a = list(re.finditer(r'^\\begin\{proposition\}', text[:p], re.M))[-1].start()
    b = text.index(r'\end{proposition}', p) + len(r'\end{proposition}')
    return text[a:b]
protected = {x: statement(before, x) for x in ['night:P4.23', 'night:P4.24']}

apply_edit(r'''\item Let $D$ be the conductor. Proposition~\ref{night:P4.12} makes $K_T+D$ torsion;
pushing down the point blowups gives $K_{T_0}+D_0$ torsion,
with $D_0$ effective and nonzero. This is a numerically
anticanonical divisor in the sense of Dloussky,
Definition~2.20 of \cite[arXiv v3, p.~14]{Dloussky2006}.
His Theorem~0.2 (p.~2)
therefore gives a global spherical shell. Proposition~2.27 (pp.~17--19)
and the square-zero-divisor paragraph after Lemma~2.22 (p.~15)
leave the parabolic Inoue or Inoue--Hirzebruch cases,
or a connected rational cycle with attached rational
trees. The latter configuration and $\pi_1(T_0)=\mathbb Z$
are stated explicitly in \cite[\S1, pp.~284--285]{DOT2003}.
We verify the consequences needed
for our conductor.''', r'''\item Let $\beta:T\to T_0$ be the blowdown map, let $D$ be the
conductor, and put $D_0=\beta_*D$. Proposition~\ref{night:P4.12}
makes $K_T+D$ torsion; its pushforward makes
$L=\mathcal O_{T_0}(K_{T_0}+D_0)$ torsion. The divisor $D_0$
is effective and nonzero, since $D_0=0$ would make a positive
power of $K_{T_0}$ trivial, contrary to $\kappa(T_0)=-\infty$.
In \cite[arXiv v3, Definition~2.20, p.~14]{Dloussky2006}, take
the integer to be one and the flat line bundle to be $L^{-1}$.
The resulting identity $K_{T_0}+D_0+L^{-1}=0$ in
$\operatorname{Pic}(T_0)$ is precisely the numerically
anticanonical datum of that definition.
Theorem~0.2 (p.~2) gives a global spherical shell.
Proposition~2.29 (p.~19), together with Proposition~2.27
(pp.~17--19) and the square-zero-divisor paragraph after
Lemma~2.22 (p.~15), gives the parabolic Inoue and
Inoue--Hirzebruch cases, and the case of a connected rational
cycle with attached rational trees. The latter configuration
and $\pi_1(T_0)=\mathbb Z$ are described in
\cite[\S1, pp.~284--285]{DOT2003}.''',
    'II-C3-CLASSVII-NAC', ['D18','D17','D08'], 'night:P4.23', 'Step 1',
    'Opened the complete cited Dloussky v3 loci, including Proposition2.29. Specified the exact flat line bundle L inverse and integer one in Definition2.20, and justified nonempty support from Kodaira dimension. Retains the same minimal-model alternatives and the DOT fundamental group input.')

apply_edit(r'''\item The blowup coefficient $\mu-1$ preserves the reduced
nodal property, as in the proof of Proposition~\ref{night:P4.21}.''',
    r'''\item At every point blowup, \cref{lem:II:canonical-boundary-blowup}
gives the exceptional conductor coefficient $\mu-1$ for the same
pushed-forward boundary. Its reduced-nodal clause preserves that property.''',
    'II-C3-CLASSVII-BOUNDARY', ['D12'], 'night:P4.23', 'Step 3',
    'Uses the earlier single canonical-boundary owner for the identical blowdown and conductor divisors.')

apply_edit(r'''Its fundamental group is $\mathbb Z$.
The blowups preserve this group by the quotient argument
in the proof of Proposition~\ref{night:P4.21}, and preserve the surface fundamental group.''',
    r'''The normalization graph in \cref{lem:II:curve-normalization-graph}
has rational vertices and one cycle, so its fundamental group is
$\mathbb Z$. Apply \cref{lem:II:boundary-blowup-groups} at each
point blowup, with the same boundary divisor as in the preceding
step. The boundary and surface maps both induce isomorphisms on
fundamental groups, commuting with the boundary inclusions.''',
    'II-C3-CLASSVII-GROUPS', ['D12'], 'night:P4.23', 'Step 4',
    'Replaces a repeated quotient argument by the earlier curve-graph and boundary-blowup owners, retaining both induced maps and their commuting inclusion square.')

apply_edit(r'''The curve is connected. Write $\pi_1(C)=F_b$
for the free group of its point-identification graph.''',
    r'''The curve is connected. Apply \cref{lem:II:curve-normalization-graph}
to its rational normalized components. With $b$ the cycle rank
of that incidence graph, the induced decomposition is $\pi_1(C)=F_b$.''',
    'II-C3-CLASSVII-IMAGE', ['D12'], 'night:P4.23', 'Step 4',
    'Specifies the exact curve input and graph rank of the common normalization owner.')

apply_edit(r'''and $w$ records its map to $\pi_1(C)$. Neither map is
assumed to be an isomorphism.''',
    r'''and $w$ is the image of its generator under the induced map
to $\pi_1(C)$.''',
    'II-C3-CLASSVII-MAPS', ['D02'], 'night:P4.23', 'Step 4',
    'States both homomorphisms directly; the subsequent complete amalgam case analysis is retained.')

apply_edit(r'''\item For the number $c\ge1$ of components of $C$, we obtain
\[
 e(C)=c+1-b\ge c\ge1.
\]''', r'''\item For the number $c\ge1$ of components of $C$, the Euler
formula of \cref{lem:II:curve-normalization-graph} gives
\[
 e(C)=c+1-b\ge c\ge1.
\]''',
    'II-C3-CLASSVII-EULER', ['D12'], 'night:P4.23', 'Step 6',
    'Uses the Euler formula of the same connected rational normalization graph; the strict positivity conclusion is unchanged.')

apply_edit(r'''minimal Hopf model. At each step the conductor
coefficient on the exceptional curve is $\mu-1$,
where $\mu$ is the multiplicity of the conductor
at the centre. Effectiveness therefore puts every
centre on the current conductor.''',
    r'''minimal Hopf model. At each step apply
\cref{lem:II:canonical-boundary-blowup} to the conductor and
its pushforward. The exceptional coefficient is $\mu-1$,
where $\mu$ is the multiplicity of the pushed-forward conductor
at the centre. Effectiveness therefore puts every centre on
that conductor.''',
    'II-C3-HOPF-BOUNDARY', ['D12'], 'night:P4.24', 'Step 1',
    'The common canonical-boundary lemma gives the identical coefficient comparison on each surface blowup.')

apply_edit(r'''The
argument below applies to this finite map, without
requiring it to be a normalization. Proving
minimality of $T'$ proves $k=0$.''',
    r'''For this finite map the Chern calculation uses precisely
immersivity off the conductor and nonconstant restrictions to
its components. Proving minimality of $T'$ proves $k=0$.''',
    'II-C3-HOPF-COVER-SCOPE', ['D02'], 'night:P4.24', 'Step 2',
    'States the properties of the pulled-back map used in the unchanged Chern calculation positively.')

apply_edit(r'''where $0<|\alpha|\le|\beta|<1$ and
$\lambda(\alpha-\beta^n)=0$. We verify the needed
curve statement from these coordinates. Every
compact irreducible curve is smooth elliptic:
adjunction and $b_2(T_0)=0$ give arithmetic genus
one, and a rational normalization would lift to
$\mathbb C^2\setminus\{0\}$ and have constant
coordinate functions.''',
    r'''where $0<|\alpha|\le|\beta|<1$ and
$\lambda(\alpha-\beta^n)=0$. Applied to this same minimal
Hopf surface $T_0$, the first step of
\cref{night:P4R.5} proves that its compact irreducible curves
are smooth elliptic and that distinct such curves are disjoint.''',
    'II-C3-HOPF-CURVES', ['D12','D08'], 'night:P4.24', 'Step 3',
    'The earlier full adjunction and universal-cover proof applies to the identical T0; it is retained once there.')

apply_edit(r'''Thus every branch of its image is
smooth. At an image point, two different
curve germs would have to come from two
different normalization points. Their
surface branches in the smooth threefold
intersect in a curve germ. This germ is
contained in the conductor image of both
branches; the unique conductor germ at
each normalization point forces the two
image germs to be equal. Therefore the
image conductor is locally a single smooth
curve.''',
    r'''Thus each branch of its image is smooth. Apply the
hypersurface-branch argument in the proof of \cref{night:P4R.5}
to the finite normalization $\nu:T\to S\subset Y$: its domain
has exactly one reduced conductor germ at each point, and the
two surface branches over a putative pair of image germs
intersect in a curve germ contained in both images. That
argument identifies the two image germs. Consequently the
image conductor is locally a single smooth curve.''',
    'II-C3-HOPF-IMAGE-GERMS', ['D12'], 'night:P4.24', 'Step 13',
    'Uses the earlier exact normalization/hypersurface branch argument with the same finite map and the established unique conductor germ; the differential nonvanishing and unramified conclusion remain.')

apply_edit(r'''\newblock URL \url{https://arxiv.org/pdf/2310.05265}.''',
    r'''\newblock Cited version: arXiv:2310.05265v2, 4 December 2023.
\newblock URL \url{https://arxiv.org/abs/2310.05265v2}.''',
    'II-C3-HOPF-BIB', ['D18'], 'Khaled2024Hopf', 'Bibliography',
    'Downloaded and opened the actual v2 PDF at formula(1) p3 and Theorem2.1(1) p5; preserves the journal reference and identifies the version supplying the cited pagination.')
apply_edit(r'''\newblock URL \url{https://arxiv.org/pdf/math/0406387}.''',
    r'''\newblock Cited version: arXiv:math/0406387v3, 13 April 2005.
\newblock URL \url{https://arxiv.org/abs/math/0406387v3}.''',
    'II-C3-CLASSVII-BIB', ['D18'], 'Dloussky2006', 'Bibliography',
    'Downloaded and read the exact v3 classification/NAC loci; preserves the journal reference and identifies the version supplying the cited pagination.')

after = SOURCE.read_text()
for label, content in protected.items():
    assert statement(after, label) == content, label
for label in protected:
    add_event(label, 'II-C3-ROOT-' + label.split(':')[-1] + '-CANONICAL-COMPARISON',
        'used and rechecked in this run',
        'Read the complete original proof and every receiving replacement. Statement bytes unchanged. Repeated canonical-boundary, graph and Hopf-curve steps now cite the earlier owners with the same divisor, blowdown, finite normalization and induced group maps. The class-VII amalgam alternatives and the entire Hopf foliation, saddle count, sheaf-length calculation and Chern inequalities remain. Exact Khaled v2 and Dloussky v3 primary loci read; final full receiving-unit pass and rendered-page reading remain to follow.',
        'S6_SERIES_PUBLISH_II.tex', source='code/S6_SERIES_PUBLISH_c3_classVII_hopf.py')

readings = [
    dict(source='Khaled 2023 v2', url='https://arxiv.org/pdf/2310.05265', version='arXiv:2310.05265v2, 4 December 2023',
         locus='Complete printed pp.3 and5: formula(1), Definition1.3, Theorem2.1 and its normal-form table',
         sha256='7ec7b5917163b8d11ca97866b76a67aa81d3db5e3b1876b3abf9d4cbdb210383',
         own_word_summary='Primary Hopf surfaces are quotients by the listed contractions; the resonant triangular and diagonal normal forms have the stated parameters. Only this normal-form input is taken here; the foliation and curve calculations are the paper proof.',
         use='night:P4.24, exact contraction coordinates and parameters'),
    dict(source='Dloussky 2005 v3', url='https://arxiv.org/pdf/math/0406387', version='arXiv:math/0406387v3, 13 April 2005',
         locus='Complete printed pp.2–4,14–15,17–19: Theorem0.2, Remark0.6, Definition2.20, Lemma2.22, Lemma2.26, Propositions2.27 and2.29 and their proofs',
         sha256='f461b07b3bb60a6c1433172a5514fa6e90a41e43dac6f23396a4713d99f5c3f9',
         own_word_summary='A numerically anticanonical datum gives a spherical shell; the divisor classification gives connected rational cycle-and-tree configurations and the stated Inoue alternatives. The source defines the flat-bundle datum and states the anticanonical relation in the square-zero case.',
         use='night:P4.23: set m=1 and F=O(K+D0) inverse, then apply the exact listed classification alternatives'),
    dict(source='Dloussky–Oeljeklaus–Toma 2003', url='https://www.jstage.jst.go.jp/article/tmj/55/2/55_2_283/_pdf/-char/en', version='Tohoku Mathematical Journal55(2003),283–309, publisher PDF',
         locus='Section1, complete printed pp.284–285',
         sha256='b1b66ca42a4765dc3242dd68342cb62d414f45527486932fe425b6a8fe8cc962',
         own_word_summary='The intermediate surface curve configuration is a rational cycle with attached trees; the deformation description gives infinite cyclic surface fundamental group.',
         use='night:P4.23: the connected remaining curve configuration and pi1(T0)=Z')
]
for row in readings:
    row['date_utc'] = now()
print('Primary reading rows', append_rows(ROOT / 'S6_SERIES_PUBLISH_c3_primary_readings.tsv', readings, 'source'))
print('Class-VII and smooth-Hopf substitutions complete; both statements unchanged.')
