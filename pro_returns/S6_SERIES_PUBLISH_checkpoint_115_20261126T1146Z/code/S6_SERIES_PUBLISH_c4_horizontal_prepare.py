#!/usr/bin/env python3
"""Prepare the guarded horizontal-tail integration; never modify shared files."""
from pathlib import Path
import csv
import re
from collections import Counter

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'agents/continuation3_provenance/sec07_tail'
OUT = ROOT / 'agents/continuation4_horizontal'
OUT.mkdir(exist_ok=True)
csv.field_size_limit(10_000_000)
with (BASE / 'S6_SERIES_PUBLISH_sec07_guards.tsv').open() as f:
    guards = list(csv.DictReader(f, delimiter='\t'))

edits = []
def change(text, old, new, owner, kind='D08', reason='State the mathematical assertion directly.'):
    n = text.count(old)
    assert n == 1, (owner, n, old[:140])
    edits.append(dict(owner=owner, type=kind, old=old, new=new, reason=reason))
    return text.replace(old, new, 1)

def read(name):
    return (BASE / f'S6_SERIES_PUBLISH_{name}_proposed.tex').read_text()

def proof_contents(text):
    return text.split(r'\begin{proof}', 1)[1].rsplit(r'\end{proof}', 1)[0].strip()

def statement(text):
    return text.split(r'\end{proposition}', 1)[0] + r'\end{proposition}'

body = guards[0]['new_text']

# A single Euler owner receives exactly the six special-case statement labels.
aliases = [
    ('cdp:st:C.2.RAT.4', '01CG'),
    ('cdp:st:C.2.RAT.5', '01CH'),
    ('cdp:st:C.2.RAT.7', '01CJ'),
    ('cdp:st:C.2.RAT.8', '01CK'),
    ('cdp:st:C.2.RAT.9', '01CL'),
    ('cdp:st:C.2.D4.3', '01BY'),
]
p360 = (BASE / 'S6_SERIES_PUBLISH_P360.tex').read_text()
alias_text = ''.join(
    '\\hypertarget{tag-' + tag + '}{}\\label{' + label + '}\n'
    + '\\StatementRecord{' + label + '}{proved}{' + tag + '}{}\n'
    for label, tag in aliases
)
p360 = change(p360, r'\hypertarget{tag-P360}{}\label{prop:II:rational-torus-fibre-euler}',
    r'\hypertarget{tag-P360}{}\label{prop:II:rational-torus-fibre-euler}' + '\n' + alias_text.rstrip(),
    'prop:II:rational-torus-fibre-euler', 'D12',
    'The six compact rational-normalization sign statements specialize the proper-family result by identical full fibre, normalization and resolution maps.')
p360 = change(p360, '\\end{enumerate}\n\\end{proof}', r'''\item For a compact family, restriction to a disc $\Delta$ about
$b=f(S)$ identifies the full fibre and its normalization-resolution
diagram with those of $f|_{f^{-1}(\Delta)}$. On the three reduced
spaces the maps are
\[
 S\times_B\Delta\longrightarrow S,\qquad
 T\times_B\Delta\longrightarrow T,\qquad
 Z\times_B\Delta\longrightarrow Z,
 \qquad (x,b)\longmapsto x,
\]
with inverses $x\mapsto(x,b)$. They commute with $\eta$ and
$\pi$, and the Cartier divisor remains $f^*(b)=mS$.
Consequently the same bound applies to every rational ruled-boundary
configuration, including a degree-two tacnode conductor or a
degree-two or degree-three ordinary-triple conductor, with all
common cubic zeros and their multiplicities.
\end{enumerate}
\end{proof}''', 'prop:II:rational-torus-fibre-euler', 'D12',
    'Give the explicit fibre-product projections and their inverses for all consolidated compact specializations.')
body = change(body, (BASE / 'S6_SERIES_PUBLISH_P360.tex').read_text().strip(), p360.strip(),
              'prop:II:rational-torus-fibre-euler', 'D12', 'Consolidate the rational-normalization Euler conclusion.')

# The tacnode owner states its additional attachment bounds and smooth refinement.
tacnode = read('RAT_2_4')
old_tacnode_statement = statement(tacnode)
new_tacnode_statement = r'''\begin{proposition}[Attachment bounds for rational tacnode covers]
\hypertarget{tag-01CE}{}\label{cdp:st:C.2.RAT.2}
\StatementRecord{cdp:st:C.2.RAT.2}{proved}{01CE}{}
Use the torus-fibre, rational-normalization and ruled-boundary
morphism of \cref{cdp:st:C.2.RAT.1}. Suppose $C$ is not
contracted, $H=h(C)_{\rm red}$ has generic transverse type
$A_3$, and $C\to H^\nu$ has degree two. For the selected
vertical trees of \cref{cdp:st:C.2.RAT.3}, no tree dominates
$H$ and the attachment loss satisfies $\ell\le1$.
This includes singular and non-lci image curves.

For a smooth image $H$, the number $r$ of distinct vertical
fibres in the minimal boundary satisfies $r\le2$, and
\begin{equation}
e(S)\ge2+N_0.\hypertarget{tag-00WZ}{}\label{cdp:eq:C.RA.18}
\end{equation}
\end{proposition}'''
tacnode = change(tacnode, old_tacnode_statement, new_tacnode_statement,
    'cdp:st:C.2.RAT.2', 'D12',
    'State the already proved zero-dominating-tree and loss-at-most-one bounds; retain the entire smooth r≤2 and e≥2+N0 refinement. RAT4’s weaker Euler statement is owned by P360.')
body = change(body, read('RAT_2_4').strip(), tacnode.strip(), 'cdp:st:C.2.RAT.2', 'D12',
              'The generic attachment proof and the smooth refinement have one statement and one proof.')

# All distinct ordinary-triple root and attachment calculations form one result.
root = proof_contents(read('RAT_5'))
root = change(root, r'''\item The nonzero cubic has three distinct roots over the generic
point and is never identically zero on a projective fibre.
It therefore defines a reduced finite divisor $R_3$.''', r'''\item The cubic has three distinct roots over the generic point.
On a base disc divide its coefficients by their common factor.
The resulting primitive cubic is nonzero on every projective fibre
and defines the horizontal root divisor $R_h$. On overlaps the
two primitive cubics differ by a unit, so their zero schemes agree.
Thus $R_h\to H$ is proper with finite fibres, and is finite of
degree three. Its generic roots are distinct, so it is reduced.''',
    'prop:II:cubic-root-attachments', 'D12',
    'Use the same root-field map for the horizontal divisor after dividing by the common coefficient factor; units on overlaps give the same finite cover.')
root = change(root, r'''Thus two distinct points of $C$ over one point $p\in H$
give distinct root points of $R_d$, because normalization
of a locally unibranch reduced curve is bijective on its
underlying points.''', r'''At a locally unibranch point of $R_d$, normalization has one
point in its fibre. Thus two distinct points of $C$ above the
same $p\in H$ give distinct root points whenever $R_d$ is
locally unibranch along that fibre.''', 'prop:II:cubic-root-attachments', 'D12',
    'The finite-cover identification is general; bijectivity on points is applied precisely on the locally-unibranch locus.')
root = change(root, 'The function-field algebra of its roots agrees with that of',
    'Let $R_d$ be the root component corresponding to $C$.\nThe function-field algebra of its roots agrees with that of',
    'prop:II:cubic-root-attachments', 'D12', 'Retain the definition of the root component from the consolidated statement.')
root = change(root, r'''\item At a simple tangent root, choose coordinates''',
    r'''\item Over $H\setminus\operatorname{Supp}A$, at a simple tangent
root of $q_3$, choose coordinates''', 'prop:II:cubic-root-attachments', 'D12',
    'The derivative and conductor calculation is used precisely where the cubic is primitive.')
root = change(root, r'''\item At most $3-d$ generic normalization branches are
supplied by vertical strict conductor components,
so $r_{\rm dom}\le3-d$.
Apply''', r'''\item At most $3-d$ generic normalization branches belong to
vertical strict conductor components, so $r_{\rm dom}\le3-d$.
Under the hypotheses $A=0$ and $R_d$ locally unibranch, apply''',
    'prop:II:cubic-root-attachments', 'D12', 'State explicitly the scope of the zero-loss specialization.')
root = change(root, r'''\item Two distinct $C$-points over $p$ cannot both receive a
vertical boundary attachment.''', r'''\item Suppose $A=0$ and $R_d$ is locally unibranch everywhere.
Two distinct $C$-points over $p$ cannot both receive a
vertical boundary attachment.''', 'prop:II:cubic-root-attachments', 'D12',
    'Keep the primitive and locally-unibranch hypotheses at the exact attachment argument.')
root = change(root, r'''\[
 e(S)\ge2-r_{\rm dom}\ge d-1 .
\]
This proves the assertion.''', r'''\begin{equation}
 e(S)\ge2-r_{\rm dom}\ge d-1>0.
 \hypertarget{tag-00XZ}{}\label{cdp:eq:C.RD.1}
\end{equation}''', 'prop:II:cubic-root-attachments', 'D12',
    'Keep the original RD1 quantitative formula with the attachment calculation; its sign statement is the P360 specialization.')
root = root.replace(r'y\,A(\lambda,y,z)', r'y\,\Phi(\lambda,y,z)')
root = root.replace(r'Put $P(w,y,z)=q_3(w,1,z)+yA(w,y,z)$.', r'Put $\Psi(w,y,z)=q_3(w,1,z)+y\Phi(w,y,z)$.')
root = root.replace(r'\partial_wP(\lambda(y,z),y,z)', r'\partial_w\Psi(\lambda(y,z),y,z)')

# The general conductor/root-field map must precede D4.2's genus argument.
root_start=root.index(r'\item The cubic has three distinct roots')
root_stop=root.index('At a locally unibranch point of $R_d$')
root_field_proof=root[root_start:root_stop]
rd2_start=root_field_proof.index(r'\begin{equation}')
rd2_end=root_field_proof.index(r'\end{equation}',rd2_start)+len(r'\end{equation}')
rd2_equation=root_field_proof[rd2_start:rd2_end]
root_field_proof=root_field_proof[:rd2_start]+r'\eqref{cdp:eq:C.RD.2}.'+'\n'+root_field_proof[rd2_end:]
root_field_proof=root_field_proof.replace('gives the finite-cover identification\n\\eqref', 'gives the finite-cover identification \\eqref')
p361_original=(BASE/'S6_SERIES_PUBLISH_P361.tex').read_text()
p361=p361_original.replace('[Compact cycles of the normal cubic]','[Normal cubic covers and compact cycles]',1)
root_clause=r'''Let $R_h\subset\PP(N)$ be the horizontal root divisor of $P$.
For a connected normalized conductor cover $C\to H$ of degree
$d$, let $R_d$ be its generic tangent-root component. There is
a finite-cover isomorphism over $H$:
'''+rd2_equation+'\n'
p361=change(p361,'The surface $U_P$ is smooth and has a compact smooth core.',
    root_clause+'The surface $U_P$ is smooth and has a compact smooth core.',
    'lem:II:normal-cubic-compact-core','D12','State the exact conductor/root normalization isomorphism before its D4.2 application; the cover C may have any genus.')
p361=change(p361,r'\item Write $f=u s_0^m$ locally, with $s_0$ a reduced',
    root_field_proof+'\n'+r'\item Write $f=u s_0^m$ locally, with $s_0$ a reduced',
    'lem:II:normal-cubic-compact-core','D12','Transfer the common-factor gluing, generic tangent-ratio field map and integral-closure inverse from RAT5 to the earlier proper normal-cubic owner.')
body=change(body,p361_original.strip(),p361.strip(),'lem:II:normal-cubic-compact-core','D12',
    'Place the exact field and normalization map before D4.1/D4.2; keep the entire compact-cycle proof.')
root=change(root,root[root_start:root_stop],r'''\item Apply the root-cover clause of
\cref{lem:II:normal-cubic-compact-core} to this same full fibre,
curve $H$ and tensor $P=q_3$. Its normalized conductor cover
is the present smooth section $C$, and its horizontal root
component is the present $R_d$. Thus \eqref{cdp:eq:C.RD.2}
identifies the two covers over $H$.
''','prop:II:cubic-root-attachments','D12','Use the same finite-cover map from the complete earlier owner; only the attachment calculation remains here.')

r7 = proof_contents(read('RAT_7'))
r7_start = r7.index(r'\item By \cref{cdp:st:A.5.19}')
r7_stop = r7.index('The assumed absence')
r7 = change(r7, r7[r7_start:r7_stop], r'''\item Suppose $d=2$ and $A=0$.
The cubic is a section of $\OO_W(3)$.
''', 'prop:II:cubic-root-attachments', 'D12', 'The common image and normal-bundle setup precedes every case.')
r7 = change(r7, 'This completes the proof.\n', '', 'prop:II:cubic-root-attachments', 'D08', 'Remove the closing recap.')

r8 = proof_contents(read('RAT_8'))
r8_start = r8.index(r'\item The image-classification')
r8_stop = r8.index('Write the complete root divisor as')
r8 = change(r8, r8[r8_start:r8_stop], r'''\item Suppose $d=2$ and $\deg A=1$.
''', 'prop:II:cubic-root-attachments', 'D12', 'Use the common setup for the single common-zero case.')
r8 = change(r8, r'''the end of \cref{cdp:st:C.2.RAT.7} makes each duplicate''',
    r'''equations \eqref{cdp:eq:C.RD.3}--\eqref{cdp:eq:C.RD.4} make each duplicate''',
    'prop:II:cubic-root-attachments', 'D06', 'The simple-root calculation is now earlier in this same proof.')
r8 = change(r8, r'''$p$, the cubic is primitive. The argument at
equations \eqref{cdp:eq:C.RD.3}--\eqref{cdp:eq:C.RD.4} make each duplicate
attachment there a multibranch point of $R_2$,''', r'''$p$, the cubic is primitive. Equations
\eqref{cdp:eq:C.RD.3}--\eqref{cdp:eq:C.RD.4} show that each duplicate
attachment there gives a multibranch point of $R_2$,''',
    'prop:II:cubic-root-attachments', 'D23', 'Make the grammatical subject agree with the exact simple-root implication.')

r9 = proof_contents(read('RAT_9'))
degree_start = r9.index(r'We first verify that $v\le2$.')
degree_end = r9.index('\n\n\\item It remains to consider $v=2$.')
degree = r9[degree_start:degree_end]
degree = degree.replace(r'We first verify that $v\le2$.', r'For $d=2$ we have $v\le2$.', 1)
degree = degree.replace('$(1,d)$ and $(2,3-v-d)$, with $d\\ge0$', '$(1,b)$ and $(2,3-v-b)$, with $b\\ge0$')
degree = degree.replace('$3-v-d\\ge1$', '$3-v-b\\ge1$')
r9_prefix_end = r9.index(r'\item It remains to consider $v=2$.')
r9 = change(r9, r9[r9.index(r'\item \cref{cdp:st:A.5.19}'):r9_prefix_end], '',
    'prop:II:cubic-root-attachments', 'D12', 'Prove the common-zero degree bound once before the double-cover cases.')
r9 = change(r9, r'''\item It remains to consider $v=2$. With the notation
of \cref{cdp:st:C.2.RAT.7}, the horizontal divisor is''', r'''\item Suppose $d=2$ and $v=2$. The horizontal divisor is''',
    'prop:II:cubic-root-attachments', 'D12', 'Use the common root-divisor notation.')
r9 = change(r9, r'''The local analysis in the proof of \cref{cdp:st:C.2.RAT.8}
applies at each of the two fibres.''', r'''The local analysis of \eqref{cdp:eq:C.RD.19} and its
intersection-three cases applies at each of the two fibres.''',
    'prop:II:cubic-root-attachments', 'D06', 'Point to the precise earlier local calculation within the companion proof.')
r9 = change(r9, r'''proof of \cref{cdp:st:C.2.RAT.8} are $D_4,D_5,D_6$;''',
    r'''intersection calculations above are $D_4,D_5,D_6$;''',
    'prop:II:cubic-root-attachments', 'D06', 'Use the same local models after consolidation.')
r9 = change(r9, r'''case and, together with \cref{cdp:st:C.2.RAT.7} and \cref{cdp:st:C.2.RAT.8} and''',
    r'''case. Together with the cases $v=0,1$ and''',
    'prop:II:cubic-root-attachments', 'D12', 'Combine the three common-zero cases in one proof.')
r9 = change(r9, r'''This proves the degree-two-common-divisor
case. Together with the cases $v=0,1$ and
the degree bound at the start, every case
in the statement.
''', '', 'prop:II:cubic-root-attachments', 'D08', 'Remove the closing recap after the exact loss calculation.')

d3 = proof_contents(read('D4_3'))
d3 = change(d3, r'''\item At a point where the cubic is primitive, a simple tangent
root gives a smooth normalization branch with conductor
exactly twice the horizontal curve. Indeed the ambient
blowup chart divides the reduced equation by the third
power of its normal coordinate; the nonzero root derivative
solves the remaining coordinate holomorphically. The
remaining quadratic factor has nonzero value at the chosen
simple root. Its restriction therefore gives the conductor
factor $y^2$ times a unit, even when its own two roots coincide. This is the explicit
factorization and conductor comparison of \cref{cdp:st:C.2.RAT.5}.
Such a point cannot carry a vertical boundary attachment.
If the horizontal root curve is locally unibranch, a
multiple root has just one point on its normalization.
A cubic has at most one multiple root unless all its roots
are simple. Thus off the common divisor each image value
receives at most one attachment when that root curve is
locally unibranch.''', r'''\item Equations \eqref{cdp:eq:C.RD.2}--\eqref{cdp:eq:C.RD.4}
identify the normalization cover and the conductor ideal at every
simple root outside $A$. The locally-unibranch attachment argument
therefore bounds the loss outside $A$ by zero whenever the
horizontal root curve is locally unibranch.''',
    'prop:II:cubic-root-attachments', 'D12', 'Use the one complete root-field, inverse-coordinate and conductor calculation.')
d3 = change(d3, 'zero. The three cases exhaust $v=1,2$, proving $e(S)\\ge1$.',
    'zero.', 'prop:II:cubic-root-attachments', 'D12', 'The proof establishes the final root-divisor exclusion; its Euler specialization has one owner at P360.')

companion_statement = r'''\begin{proposition}[Cubic root divisors and vertical attachments]
\hypertarget{tag-P380}{}\label{prop:II:cubic-root-attachments}
\StatementRecord{prop:II:cubic-root-attachments}{proved}{P380}{\cref{cdp:st:C.2.RAT.3,lem:II:normal-cubic-compact-core,lem:II:cyclic-cubic-boundary,cdp:st:C.2.D4.1,cdp:st:C.2.D4.2}}
Use the torus-fibre, rational-normalization and ruled-boundary
morphism of \cref{cdp:st:C.2.RAT.1}. Suppose the horizontal
section $C$ is not contracted, its image $H$ has generic
ordinary-triple transversal, and $C\to H^\nu$ has degree
$d\in\{2,3\}$. Then $H\simeq\PP^1$.
Put $N=N_{H/Y}$, $W=\PP(N)$ with the convention of lines,
and let $q_3$ be the cubic normal tensor. Its coefficient
line $\OO_Y(S)|_H$ is trivial and $\deg N=-2$.
Let $A$ be the common zero divisor of its coefficients,
let $B_{\rm red}$ be the reduced support of its full root
divisor on $W$, and write
\[
 \nu=\sum_x\bigl(r_x(B_{\rm red})-1\bigr),
\]
where $r_x$ counts local normalization branches. Use the
selected-tree counts and loss $\ell=K-k$ of
\cref{cdp:st:C.2.RAT.3} for this same ruling and $C\to H$.
The dominating-tree count satisfies $r_{\rm dom}\le3-d$.
The following bounds hold:
\[
\begin{array}{c|c|c|c}
d&A&\nu&\ell\\\hline
2&0&\le1&\le1\\
2&\deg A=1&\le3&\le1\\
2&p+q,\ p\ne q&\le5&\le1\\
2&2p&2&0\\
3&\deg A=1&1&0\\
3&p+q,\ p\ne q&3\text{ or }2&\le\nu-2.
\end{array}
\]
These exhaust the possible common divisors. In degree three,
$N\simeq\OO(-1)^{\oplus2}$; the last row has respectively
one or two contacts of order three between the horizontal root
curve and the two vertical fibres. For $A=0$ and a locally
unibranch root component corresponding to $C$, the sharper
bound is $\ell=0$. This applies to a degree-two root component
whose only singularities are one $A_4$ cusp or two $A_2$ cusps.

At every simple root away from $A$, the corresponding
normalization branch is smooth and has conductor ideal $(y^2)$
in the coordinates of \eqref{cdp:eq:C.RD.3}--\eqref{cdp:eq:C.RD.4}.
\end{proposition}'''

common_setup = r'''Riemann--Hurwitz for $C\simeq\PP^1\to H^\nu$ gives
$-2=d(2g(H^\nu)-2)+\deg\operatorname{Ram}(C/H^\nu)$,
so $g(H^\nu)=0$. By \cref{cdp:st:A.5.19}, a singular
rational ordinary-triple image has only degree-one connected
normalization covers. The degree $d\ge2$ therefore makes $H$
smooth, and $H\simeq\PP^1$. The ambient rational Chern-class
vanishing gives $\deg N=-2$ and
$\OO_Y(S)|_H\simeq\OO_H$. Put $\xi=c_1(\OO_W(1))$
and write $F$ for the class of a fibre of $W\to H$.
The tautological clause of \cref{lem:II:cyclic-cubic-boundary}
gives $\xi^2=2$, $\xi F=1$ and $K_W=-2\xi$.
Set $v=\deg A$. For $d=2$, write the horizontal root divisor
as $R_h=R_1+R_2$, where $R_2$ corresponds to $C$ and the
remaining degree-one component $R_1$ is a section. For $d=3$
the horizontal divisor is the integral curve $R_3$.
'''
companion = companion_statement + '\n\n\\begin{proof}\n' + common_setup
companion += '\n\\paragraph{Root covers and simple-root attachments.}\n' + root
companion += '\n\n\\paragraph{The degree of the common divisor.}\n' + degree
companion += r'''
For $d=3$, \cref{cdp:st:C.2.D4.1} gives
$N=\OO(-1)^{\oplus2}$ and $v\in\{1,2\}$ for the same
normal tensor and connected normalization cover.
'''
companion += '\n\\paragraph{A primitive degree-two root component.}\n' + r7
companion += '\n\n\\paragraph{A degree-two component and one simple common zero.}\n' + r8
companion += '\n\n\\paragraph{A degree-two component and a common divisor of degree two.}\n' + r9
companion += '\n\n\\paragraph{A connected degree-three root component.}\n' + d3
companion += '\n\\end{proof}\n'

for name in ['RAT_5', 'RAT_7', 'RAT_8', 'RAT_9']:
    body = change(body, read(name).strip(), '', 'prop:II:cubic-root-attachments', 'D12',
                  'The sign statement is at P360; the distinct geometric calculation belongs to the single cubic-root companion.')
body = change(body, read('D4_3').strip(), companion.strip(), 'prop:II:cubic-root-attachments', 'D12',
              'Combine the complete ordinary-triple root and attachment calculations into one result and proof after both genus exclusions.')

# Remove process vocabulary only where it has no mathematical force.
for old,new,owner,kind,reason in [
    ('to lie on the current divisor:', 'to lie on the divisor at that step:', 'cdp:st:C.2.IRR.1', 'D08', 'Name the divisor in the blowup sequence.'),
    ('Coefficient-zero ruling exceptional curves have not yet been discarded.\n', '', 'cdp:st:C.2.IRR.1', 'D02', 'The following exceptional-curve argument already covers these curves.'),
    ('This excludes the two non-lci reduced image germs; the conductor-image scheme retains its full structure throughout.', 'This excludes the two non-lci reduced image germs.', 'cdp:st:C.2.RAT.1', 'D11', 'The conductor scheme was already fixed and is used through its explicit ideal.'),
    ('Among the other fibres retain those with a component', 'Among the other fibres select those with a component', 'cdp:st:C.2.RAT.3', 'D08', 'Describe the defined selection of vertical trees.'),
    ('The retained number satisfies', 'The number of selected fibres satisfies', 'cdp:st:C.2.RAT.3', 'D08', 'Use the attachment-count definition.'),
    ('The retained fibres have a surviving strict conductor', 'The selected fibres have a noncontracted strict conductor', 'cdp:st:C.2.RAT.3', 'D08', 'State the geometric property of the selected fibres.'),
    ('After identifying the retained points with the same', 'After identifying the selected points with the same', 'cdp:st:C.2.RAT.3', 'D08', 'Use the attachment-count definition.'),
    ('The $k$ retained edges give a connected', 'The $k$ selected edges give a connected', 'cdp:st:C.2.RAT.3', 'D08', 'Use the incidence edges defined in the proof.'),
    ('A compact spherical class of nonzero square\nin $U_P$ is impossible without a restriction on $b_1(U_P)$.', 'Every compact spherical class\nin $U_P$ has square zero.', 'lem:II:normal-cubic-compact-core', 'D02', 'State the spherical conclusion positively; its proof uses π2 of the torus.'),
    ('without any first-Betti hypothesis.', 'by the spherical clause of that lemma.', 'cdp:st:C.2.D4.1', 'D02', 'Name the exact spherical clause already proved.'),
    ("Thus the shared owner's parameters are", 'Thus the parameters of \\cref{lem:II:cyclic-cubic-boundary} are', 'cdp:st:C.2.D4.1', 'D08', 'Identify the mathematical result receiving the parameters.'),
    ("The shared owner's complete resolution therefore", 'The resolution in \\cref{lem:II:cyclic-cubic-boundary} therefore', 'cdp:st:C.2.D4.2', 'D08', 'Identify the resolution and its proved local charts.'),
    ('cup-product identification in that owner give', 'cup-product identification in that proposition give', 'cdp:st:C.2.UN.7', 'D08', 'Refer to the proposition.'),
    ('The precise replacements for the earlier ambient $b_2=0$\nuses are the torsion canonical and normal lines, the', 'On this tube the inputs are the torsion canonical and normal\nlines, the', 'cdp:st:C.2.UN.12', 'D01', 'State the proper-tube inputs without draft history.'),
    ('its current strict transform, and the new', 'its strict transform, and the', 'cdp:st:C.2.INT.2', 'D08', 'Describe the blowup geometry.'),
    ('proves item~4 and completes the proof.', 'proves item~4.', 'cdp:st:C.2.UN.7', 'D08', 'Remove the closing recap.'),
    ('torus smoothing, with its unit and full multiplicity\nretained.', 'torus smoothing with its full equation, unit and multiplicity.', 'cdp:st:C.2.IRR.1', 'D08', 'Name the full function to which the local obstruction applies.'),
    ('This proves \\eqref{cdp:eq:C.RA.18} with its full vertical\nboundary and normalization scope.\n', '', 'cdp:st:C.2.RAT.2', 'D08', 'The preceding inequality is the claimed quantitative conclusion.'),
]:
    if old in body:
        body = change(body, old, new, owner, kind, reason)

for old,new in [
    ('actual ', ''), ('actual\n', ''), ('specified ', 'fixed '), ('specified\n', 'fixed\n'), ('Cited result~\\cref', '\\cref'),
    ('cited result~\\cref', '\\cref'), ('retained attachment counts', 'selected attachment counts'),
]:
    while old in body:
        at=body.index(old)
        lo=max(body.rfind('\n\n',0,at)+2,0)
        hi=body.find('\n\n',at)
        if hi<0: hi=len(body)
        fragment=body[lo:hi]
        prior=body[:at]
        owners=re.findall(r'\\label\{((?:cdp:st:|prop:II:|lem:II:)[^}]+)\}',prior)
        owner=owners[-1] if owners else 'subsec:II:reduced-horizontal-boundaries'
        body=change(body,fragment,fragment.replace(old,new,1),owner,'D08','Remove process vocabulary while preserving all mathematical terms and maps.')

for old,new in [
    ('now gives', 'gives'), ('now give', 'give'), (': now $', ': $'),
    ('argument, now for', 'argument for'), ('now with', 'with'),
    ('now yields', 'yields'), ('It now gives', 'It gives'),
    ('There are now no rational curves', 'There are no rational curves'),
]:
    while old in body:
        at=body.index(old);lo=max(body.rfind('\n\n',0,at)+2,0);hi=body.find('\n\n',at)
        if hi<0:hi=len(body)
        fragment=body[lo:hi]
        labels=re.findall(r'\\label\{((?:cdp:st:|prop:II:|lem:II:)[^}]+)\}',body[:at])
        body=change(body,fragment,fragment.replace(old,new,1),labels[-1],'D08','Remove a process transition from the mathematical inference.')

body = re.sub(r'\n{4,}', '\n\n\n', body)
guards[0]['change_id']='II-C4-HORIZONTAL-TAIL'
guards[0]['new_text']=body

for g in guards[1:]:
    g['change_id']=g['change_id'].replace('II-C3-SEC07','II-C4-HORIZONTAL')
    if 'A516-SCOPE' in g['change_id']:
        for old,new in [
            ('coefficient zero in $D$; they are not to be counted as conductor\nbranches.', 'coefficient zero in $D$.'),
            ('Thus $\\chi(\\OO_S)=0$. These are exactly the two input\ncalculations in the proof of \\cref{cdp:st:A.5.12}; the\nPicard-map hypothesis of its later conclusion is not used\nin either calculation.', 'Thus $\\chi(\\OO_S)=0$. These are the canonical-evaluation\nand Cartier-sequence calculations of \\cref{cdp:st:A.5.12}.'),
            ('actual ', ''),
        ]:
            if old in g['new_text']:
                g['new_text']=change(g['new_text'],old,new,'cdp:st:A.5.16','D02','Keep the proved scope and calculations; remove defensive framing.')

source=(ROOT/'S6_SERIES_PUBLISH_II.tex').read_text()
# The front list and program references name the new mathematical owners.
further_start=source.index(r'\item \cref{cdp:st:C.2.RAT.1}\quad Euler signs')
further_end=source.index('\n',source.index(r'\item \cref{cdp:st:C.2.D4.3}\quad',further_start))+1
old_further=source[further_start:further_end]
new_further=r'''\item \cref{prop:II:rational-torus-fibre-euler}\quad Positive Euler number for every irreducible rational-normalized torus fibre.
\item \cref{cdp:st:C.2.RAT.1}\quad Euler and attachment bounds for rational boundary classes.
\item \cref{cdp:st:C.2.RAT.3}\quad Vertical-tree attachment loss and the conductor Euler bound.
\item \cref{cdp:st:C.2.RAT.2}\quad Attachment bounds for rational tacnode covers.
\item \cref{lem:II:normal-cubic-compact-core}\quad Compact normal-cubic cycles and their transport into a nearby torus.
\item \cref{lem:II:cyclic-cubic-boundary}\quad Cyclic-cover character sheaves, boundary relations and compact intersection pairings.
\item \cref{cdp:st:C.2.D4.1}\quad Connected triple covers over a rational image.
\item \cref{cdp:st:C.2.D4.2}\quad Double covers over a rational ordinary-triple image.
\item \cref{prop:II:cubic-root-attachments}\quad Common cubic zeros, normalization branches and vertical attachments.
'''
guards.append(dict(change_id='II-C4-HORIZONTAL-FURTHER-RESULTS',old_text=old_further,new_text=new_further))
edits.append(dict(owner='further-results-II',type='D12',old=old_further,new=new_further,
    reason='One list entry for each consolidated result; descriptions and order match the receiving body.'))
for line in source.splitlines(keepends=True):
    if r'\nolinkurl{' not in line:
        continue
    for label,tag in aliases:
        old_ref=r'\cref{'+label+'}'
        if old_ref in line:
            new_ref=(r'\cref{cdp:st:C.2.RAT.2}' if label.endswith('RAT.4')
                     else r'\cref{prop:II:cubic-root-attachments}')
            new_line=line.replace(old_ref,new_ref)
            guards.append(dict(change_id=f'II-C4-HORIZONTAL-PROGRAM-{len(guards)+1:02d}',old_text=line,new_text=new_line))
            edits.append(dict(owner=label,type='D09',old=line,new=new_line,
                reason='Keep the program path and calculation description; point to the receiving geometric proof, rather than the consolidated Euler label.'))

# Verify the guarded application in memory and every original label/target.
receiver=source
for g in guards:
    assert receiver.count(g['old_text'])==1, (g['change_id'],receiver.count(g['old_text']))
    receiver=receiver.replace(g['old_text'],g['new_text'],1)
for regex in [r'\\label\{([^}]+)\}',r'\\hypertarget\{(tag-[^}]+)\}']:
    old=Counter(re.findall(regex,source)); new=Counter(re.findall(regex,receiver))
    assert not old-new, (regex,old-new)
    assert not {k:v for k,v in new.items() if v>old.get(k,1)}, (regex,'multiplied targets')
assert r'\tag{' not in body
assert '\r' not in body

with (OUT/'S6_SERIES_PUBLISH_horizontal_guards.tsv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['change_id','old_text','new_text'],delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(guards)
with (OUT/'S6_SERIES_PUBLISH_horizontal_local_edits.tsv').open('w',newline='') as f:
    small_edits=[]
    for e in edits:
        if e['type']=='D12' and max(len(e['old']),len(e['new']))>2400:
            continue
        x=dict(e)
        if max(len(x['old']),len(x['new']))>1200:
            a=x['old'];b=x['new'];lo=0
            while lo<min(len(a),len(b)) and a[lo]==b[lo]:lo+=1
            tail=0
            while tail<min(len(a)-lo,len(b)-lo) and a[-tail-1]==b[-tail-1]:tail+=1
            left=max(0,lo-100)
            x['old']=a[left:min(len(a),len(a)-tail+100)]
            x['new']=b[left:min(len(b),len(b)-tail+100)]
        small_edits.append(x)
    w=csv.DictWriter(f,fieldnames=['owner','type','old','new','reason'],delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(small_edits)
(OUT/'S6_SERIES_PUBLISH_horizontal_receiver.tex').write_text(body)
start=body.index(r'\begin{proposition}[Cubic root divisors and vertical attachments]')
stop=body.index(r'\end{proof}',start)+len(r'\end{proof}')
(OUT/'S6_SERIES_PUBLISH_cubic_companion.tex').write_text(body[start:stop]+'\n')
print(f'Prepared {len(guards)} unique guarded replacements, with all original labels and targets preserved.')
print(f'Tail: {len(guards[0]["old_text"])} -> {len(body)} characters. New companion tag P380.')
print(f'Reviewed local edit records: {len(edits)}. Main source and shared tables untouched.')
