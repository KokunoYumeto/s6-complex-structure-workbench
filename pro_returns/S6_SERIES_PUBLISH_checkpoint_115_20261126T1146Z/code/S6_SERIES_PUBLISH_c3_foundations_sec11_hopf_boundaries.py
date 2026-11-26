from S6_SERIES_PUBLISH_c3_foundations_sec11_helpers import *

name = 'hopf_boundaries'
unit = 'subsec:II:maximal-hopf-leaves'
pkg = Package(name, unit)
main = (ROOT / 'S6_SERIES_PUBLISH_II.tex').read_text()
assert r'\label{prop:II:section-fibre-contraction}' in main
old64 = block(main, 'cdp:st:C.2.UN.64')
old325 = block(main, 'lem:II:reduced-anticanonical-hopf')
old82 = block(main, 'cdp:st:C.2.UN.82')
for suffix, value in [('UN64_input', old64), ('P325_input', old325), ('UN82_input', old82)]:
    (OUT / ('S6_SERIES_PUBLISH_II_sec11_hopf_boundaries_' + suffix + '.tex')).write_text(value + '\n', newline='\n')

p338 = r'''\subsection{Anticanonical elliptic bisections}\label{subsec:II:anticanonical-bisections}

\begin{lemma}[The residue obstruction to an elliptic anticanonical bisection]\hypertarget{tag-P338}{}\label{lem:II:anticanonical-bisection}
\StatementRecord{lem:II:anticanonical-bisection}{proved}{P338}{}
Let $q:V\to B$ be a holomorphic projective-line bundle over a smooth
compact elliptic curve. Let $C\subset V$ be a smooth connected
elliptic curve such that $h=q|_C:C\to B$ has degree two.
Then $K_V(C)$ is nontrivial.
\end{lemma}
\begin{proof}
The fibre cohomology of a local projective-line bundle chart gives
$q_*\OO_V=\OO_B$ and $R^1q_*\OO_V=0$. Thus Leray identifies
$q^*:H^1(B,\OO_B)\to H^1(V,\OO_V)$ with an isomorphism.
For the inclusion $i:C\hookrightarrow V$, the restriction map is
\begin{equation}
 H^1(V,\OO_V)\xrightarrow{\ i^*\ }H^1(C,\OO_C),
 \qquad i^*q^*=h^*.
\hypertarget{tag-00G6}{}\label{cdp:eq:C.EL.7}
\end{equation}
Riemann--Hurwitz makes $h$ unramified. The finite trace satisfies
$\operatorname{Tr}_h\circ h^*=2\operatorname{id}$, so this
restriction map is nonzero.

Suppose $K_V(C)\simeq\OO_V$. Its divisor residue sequence is
\begin{equation}
\hypertarget{tag-00DO}{}\hypertarget{tag-00QY}{}\SsixEquationAliases{\label{cdp:eq:C.CZ.10}\label{cdp:eq:C.ML.7}}
 0\longrightarrow K_V\longrightarrow K_V(C)
       \xrightarrow{\operatorname{res}}K_C\longrightarrow0.
\hypertarget{tag-00G7}{}\label{cdp:eq:C.EL.8}
\end{equation}
The restriction of $K_V$ to a ruling fibre has degree $-2$, so
$H^0(V,K_V)=0$. The assumed trivialization gives
$H^0(V,K_V(C))=\C$, and $H^0(C,K_C)=\C$ because $C$ is elliptic.
The residue is nonzero: locally a frame of $K_V(C)$ is
$dv/v\wedge du$ with $C=(v=0)$, and its residue is the
nonzero form $du$ along $C$. Hence the residue map on these
one-dimensional spaces is an isomorphism and its connecting
map $H^0(C,K_C)\to H^1(V,K_V)$ is zero. Serre duality for
this residue sequence identifies that connecting map with
the dual of the restriction in \eqref{cdp:eq:C.EL.7}.
This contradicts the nonzero finite pullback proved above.
\end{proof}
'''
pkg.record('D12,D14,D20', 'lem:II:anticanonical-bisection', 'UN64 EL7/EL8 and UN82 ML7 repeat the same residue/finite-trace comparison.', p338, 'The full common proof is placed at the general surface owner, with the exact Leray pullback, trace and Serre-dual residue maps; no ambient degeneration hypothesis is added to this surface calculation.')
for tag, label in [('C.EL.7', 'cdp:eq:C.EL.7'), ('C.EL.8', 'cdp:eq:C.EL.8'), ('C.CZ.10', 'cdp:eq:C.CZ.10'), ('C.ML.7', 'cdp:eq:C.ML.7')]:
    pkg.equations.append(dict(old_tag=tag, label=label, owner='lem:II:anticanonical-bisection'))
heading = r'\subsection{Terminal ruled contractions}\label{subsec:II:terminal-ruled-contractions}'
pkg.guard('P338-before-UN64', heading, p338 + '\n' + heading, 'The general surface residue owner precedes UN64, retaining every old equation alias and permanent target.')

new64 = old64
a = old64.index('We exclude the latter by the cohomology maps.')
b = old64.index('Thus $B=\\PP^1$ and', a)
residue64 = old64[a:b]
application64 = r'''For $g(B)=1$, apply \cref{lem:II:anticanonical-bisection}
with $(V,B,q,C,h)=(T,B,q,C,q|_C)$. The preceding degree and
adjunction calculations give a smooth connected elliptic
degree-two curve with $K_T(C)\simeq\OO_T$, contradicting that
lemma. Under these identity maps, \eqref{cdp:eq:C.EL.7} is the
same Leray-identified finite pullback and \eqref{cdp:eq:C.EL.8}
is the residue sequence of $C\subset T$.
'''
new64 = pkg.edit(new64, residue64, application64, 'D12,D14,D20', 'cdp:st:C.2.UN.64', 'The general P338 domain is checked on the identical T,C,q,B. Preserve the following Hirzebruch negative-section calculation and every other UN64 clause.')
old_record64 = next(x for x in new64.splitlines() if x.startswith(r'\StatementRecord'))
new_record64 = old_record64.replace('prop:II:section-fibre-contraction,', 'prop:II:section-fibre-contraction,lem:II:anticanonical-bisection,')
new64 = pkg.edit(new64, old_record64, new_record64, 'D12,D14', 'cdp:st:C.2.UN.64', 'Declare the newly earlier general surface input; retain P335 and every other admitted input.')
pkg.guard('UN64-residue-application', old64, new64, 'Based on the admitted P335 receiver. The mathematical statement is unchanged, and only its common residue proof and hidden input record change.')

p325 = r'''\begin{lemma}[Effective anticanonical Hopf boundaries]\hypertarget{tag-P325}{}\label{lem:II:reduced-anticanonical-hopf}
\StatementRecord{lem:II:reduced-anticanonical-hopf}{proved}{P325}{\cref{lem:II:central-primary-hopf-cover}; \cite[arXiv v1, \S2.2.2, p.~4; \S2.3.1, p.~8]{AbashevaDeev2024AB}; \cite[arXiv v2, normal forms (1), p.~3; Theorem~2.1 and Remark~2.2, p.~5]{Khaled2024Hopf}}
Let $H$ be a compact Hopf surface and let $D$ be a nonempty
effective integral divisor whose support consists of disjoint smooth
elliptic curves. Suppose $K_H(D)\simeq\OO_H$. Exactly one of the
following alternatives holds:
\begin{enumerate}
\item $D$ is reduced. The pair $(H,D)$ is a diagonal primary or
secondary Hopf surface with its two axes individually marked.
There are coordinates on $W=\C^2\setminus\{0\}$ in which the
full deck group of $W\to H$ is diagonal and the inverse image
of $D$ is $\{zw=0\}\cap W$. The two axes have distinct images
on $H$, and $dz/z\wedge dw/w$ descends to a nowhere-zero
section of $K_H(D)$.
\item $D=dC$ for one smooth elliptic curve $C$ and an integer $d\ge2$.
\end{enumerate}
In particular, a coefficient-one component of $D$ forces the
first alternative.
\end{lemma}
\begin{proof}
Write $H=W/\Gamma$ and apply
\cref{lem:II:central-primary-hopf-cover}. It gives a central
contraction $F$ and a finite unramified primary cover
$\pi:P=W/\langle F\rangle\to H$.
Put $D_P=\pi^*D$. The local unramified differential preserves
each divisor coefficient and gives
$K_P(D_P)\simeq\pi^*(K_H(D))\simeq\OO_P$.

Use the complete primary normal-form list in
\cite[arXiv v2, formula~(1), p.~3; Theorem~2.1, p.~5]{Khaled2024Hopf}.
In the nonlinear case write
$F(z,w)=(\beta^a z+w^a,\beta w)$, $a\ge1$.
Its unique curve is $C_P=\{w=0\}/\langle F\rangle$ by
\cite[arXiv v1, \S2.2.2, p.~4]{AbashevaDeev2024AB},
so $D_P=dC_P$ for a positive integer $d$.
The determinant of $dF$ is $\beta^{a+1}$; thus
$w^{a+1}\partial_z\wedge\partial_w$ is an anticanonical
section with divisor $(a+1)C_P$.
The line $\OO_P(C_P)$ has infinite order: a trivial positive
power would turn its canonical section into a holomorphic
function with a nonempty zero divisor on the compact connected
surface. Therefore $K_P(D_P)\simeq\OO_P$ forces $d=a+1\ge2$.
Unramified descent gives the second alternative on $H$.

In diagonal coordinates $F(z,w)=(\alpha z,\beta w)$,
an anticanonical section lifts to
$g(z,w)\partial_z\wedge\partial_w$. Hartogs extends $g$
across zero, and equivariance gives
\begin{equation}
                        g(\alpha z,\beta w)
                                      =\alpha\beta g(z,w).
\hypertarget{tag-00DP}{}\label{cdp:eq:C.CZ.11}
\end{equation}
If there is no positive multiplicative relation between
$\alpha$ and $\beta$, comparison of monomials gives only $zw$.
Indeed a nonzero coefficient of $z^iw^j$ requires
$\alpha^{i-1}\beta^{j-1}=1$; since both multipliers contract,
any solution other than $(i,j)=(1,1)$ gives such a relation.

Otherwise choose positive integers $u,v$ with
$\alpha^u=\beta^v$, and write $u=dq$, $v=dp$ with $(p,q)=1$.
The central power $F^d$ has multipliers
$\alpha_1=\alpha^d$, $\beta_1=\beta^d$ satisfying
$\alpha_1^q=\beta_1^p$.
Choose integers $s,t$ with $sp+tq=1$ and put
$\gamma=\alpha_1^s\beta_1^t$.
Then $\gamma^p=\alpha_1$, $\gamma^q=\beta_1$, and $0<|\gamma|<1$.
The quotient map $W/\langle F^d\rangle\to W/\langle F\rangle$
is finite unramified, and $F^d$ is still central in $\Gamma$.
Pullback to this cover retains every coefficient of $D_P$.
The monomials of $g$ now have weight $p+q$.
The equation $pi+qj=p+q$ is equivalent to
$i=1+q\ell$, $j=1-p\ell$, with $\ell\in\Z$.
For $p,q>1$, nonnegative exponents force $\ell=0$.
For $p>1,q=1$, the full section is
\begin{equation}
                        g=w(az+bw^p).
\hypertarget{tag-00R0}{}\label{cdp:eq:C.ML.9}
\end{equation}
When $a=0$, its divisor is $(p+1)$ times the single axis.
When $a\ne0$, the two factors are distinct and simple;
$z'=z+(b/a)w^p$, $w'=w$ sends them to the axes and commutes
with the contraction. Its inverse is
$z=z'-(b/a)(w')^p$, $w=w'$.
For $p=1,q>1$ use the exchanged coordinates and the exchanged
triangular map. For $p=q=1$, $g$ is a nonzero quadratic.
A repeated linear factor gives twice one curve; two distinct
linear factors give an invertible linear coordinate map,
with inverse its matrix inverse, commuting with the scalar contraction.
Thus on this finite unramified primary cover the divisor is
either reduced with two curves, or a positive multiple of one
curve with coefficient at least two. Since the cover is
surjective and unramified, the same reducedness alternative
and each coefficient descend to $H$; in the latter case the
image of that single curve is all of the support of $D$.
In particular a coefficient-one component excludes the latter case.

It remains to retain the full marking in the reduced case.
Use the coordinates just constructed, so the pulled-back
boundary is the two axes and the central contraction is diagonal.
Every deck lift preserves their union and commutes with that
central contraction. A lift preserving each axis has form
$(zU(z,w),wV(z,w))$ with holomorphic units $U,V$.
Commutation makes both units invariant under the contraction;
iteration to zero makes them constant.
A lift interchanging the axes has form $(wU,zV)$.
Comparison of linear terms forces the two multipliers of the
central contraction to agree, and the same iteration makes
$U,V$ constant. It is a diagonal map followed by interchange.
The logarithmic form $dz/z\wedge dw/w$ is a nowhere-zero
section of the pulled-back canonical-boundary line, and spans
its section space because the primary surface is compact and connected.
Diagonal lifts fix it; interchange negates it.
The nonzero section pulled back from $K_H(D)$ is invariant,
so every deck lift preserves each axis. The full group
$\Gamma$ is diagonal and the two images are distinct.

A diagonal group containing an infinite cyclic subgroup of finite
index is finitely generated abelian, so
$\Gamma=\langle f\rangle\oplus T$ with $T$ finite.
Choose the sign of $f$ so that a positive power is a positive
power of the central contraction times an element of $T$.
Both multipliers of $f$ then have modulus less than one.
The finite group $T$ acts freely on $W$, so each coordinate
character is injective; consequently $T$ is cyclic.
The equality $H=(W/\langle f\rangle)/T$ gives the stated
diagonal primary or secondary presentation with its marked axes.
The logarithmic form descends through this free quotient.
\end{proof}
'''
pkg.record('D12,D20,D25', 'lem:II:reduced-anticanonical-hopf', old325, p325, 'Expose the full effective-divisor alternatives already calculated across P325/UN82, with the complete nonlinear coefficient, positive-power lattice map, all weight cases and unramified descent. The original reduced clause and every diagonal-axis/log-form map remain verbatim in scope.')
old325heading = r'\subsection{Reduced anticanonical boundaries on Hopf surfaces}\label{subsec:II:anticanonical-hopf-boundaries}'
new325heading = r'\subsection{Effective anticanonical boundaries on Hopf surfaces}\label{subsec:II:anticanonical-hopf-boundaries}'
old325unit = old325heading + '\n\n' + old325
new325unit = new325heading + '\n\n' + p325
pkg.record('D14,D16', 'lem:II:reduced-anticanonical-hopf', old325heading, new325heading, 'The existing actual subsection now names its complete effective-divisor calculation; its stable unit label is retained.')
pkg.equations.append(dict(old_tag='C.ML.9', label='cdp:eq:C.ML.9', owner='lem:II:reduced-anticanonical-hopf'))
pkg.guard('P325-effective-owner', old325unit, new325unit, 'The complete receiving owner retains the original reduced conclusion and proves every coefficient alternative before UN82; ML9 moves here with its original identity.')

new82 = old82
old_record82 = next(x for x in new82.splitlines() if x.startswith(r'\StatementRecord'))
new_record82 = r'''\StatementRecord{cdp:st:C.2.UN.82}{proved}{01EU}{\cref{cdp:st:C.2.UN.75,cdp:st:C.2.UN.77,cdp:st:C.2.UN.70,cdp:st:C.2.UN.19,lem:II:negative-kodaira-models,lem:II:canonical-boundary-blowup,lem:II:hopf-curves,lem:II:anticanonical-bisection,lem:II:reduced-anticanonical-hopf}; \eqref{cdp:eq:C.ML.3}, \eqref{cdp:eq:C.ML.5}, \eqref{cdp:eq:C.ML.6}, \eqref{cdp:eq:C.ML.8}}'''
new82 = pkg.edit(new82, old_record82, new_record82, 'D12,D14', 'cdp:st:C.2.UN.82', 'Declare the complete earlier surface owners and retained local canonical equations.')
new82 = pkg.edit(new82, 'The surface classification\nand the actual component restriction \\ref{cdp:st:C.2.UN.19} give the\nstated ruled or Hopf alternatives.', 'Apply \\cref{lem:II:negative-kodaira-models} to the compact smooth\nminimal model. Its ruled/class-VII alternatives and the component\nrestriction \\cref{cdp:st:C.2.UN.19} give the stated ruled or Hopf cases.', 'D12,D14,D20', 'cdp:st:C.2.UN.82', 'Identify the earlier negative-Kodaira owner on the same compact smooth minimal model; the torus-component restriction supplies the Hopf case.')
a = new82.index('This connected anticanonical bisection is impossible')
b = new82.index('This contradiction excludes\nthe bisection.', a) + len('This contradiction excludes\nthe bisection.')
old_residue82 = new82[a:b]
new_residue82 = r'''Apply \cref{lem:II:anticanonical-bisection} with
$(V,B,q,C,h)=(T_0,B,p,C_0,p|_{C_0})$.
The same surface divisor $D_{T_0}=C_0$ gives
$K_{T_0}(C_0)\simeq\OO_{T_0}$, while $C_0$ is smooth,
connected, elliptic and of degree two over the elliptic base.
Under these identifications \eqref{cdp:eq:C.ML.7} is its residue
sequence and \eqref{cdp:eq:C.EL.7} is the Leray-identified finite
pullback. The nonzero trace composite and zero Serre-dual
connecting map exclude this bisection.''' 
new82 = pkg.edit(new82, old_residue82, new_residue82, 'D12,D14,D20', 'cdp:st:C.2.UN.82', 'Use the general surface owner directly on the specified minimal ruled surface; no assertion that this minimal model remains an ambient component is needed.')
a = new82.index(r'\par\medskip\noindent\textbf{Hopf surfaces:')
b = new82.index(r'\item The same point-map induction following', a)
old_hopf82 = new82[a:b]
new_hopf82 = r'''\par\medskip\noindent\textbf{The effective divisor on the Hopf minimal model.}
For the same point map $\pi:T\to T_0$, the pushed-forward
divisor $D_{T_0}$ is nonempty and effective, and
$K_{T_0}(D_{T_0})\simeq\OO_{T_0}$ through the pushed meromorphic
canonical section. Its support consists of disjoint smooth
elliptic curves by \cref{lem:II:hopf-curves}.
The preceding point-map comparison preserves the coefficient-one
curve $C_0$. Apply \cref{lem:II:reduced-anticanonical-hopf} to
$(H,D)=(T_0,D_{T_0})$. Its effective-divisor dichotomy and this
coefficient one force the reduced alternative: every component
of $D_{T_0}$ has coefficient one. The finite unramified cover,
positive-power cover and weight equation used here are exactly
those of that owner, with \eqref{cdp:eq:C.ML.9} its resonant factorization.

'''
new82 = pkg.edit(new82, old_hopf82, new_hopf82, 'D12,D14,D20,D25', 'cdp:st:C.2.UN.82', 'The complete repeated nonlinear/diagonal coefficient calculation moves to P325. Check every effective-divisor hypothesis and the surviving coefficient-one curve on the identical Hopf minimal model.')
old_last = r'''\item The eigenfunction classification just proved
also shows that an effective anticanonical divisor
on a minimal Hopf surface either is reduced or
is supported on one elliptic curve: the nonlinear
form is a pure power, and the only nonreduced
diagonal alternatives above are pure powers of
one smooth factor. This conclusion descends
through the finite unramified primary cover.
Thus the nonempty boundary here is exactly one
curve \(C\), with coefficient \(a\ge2\).
Its unique neighbour has order \(M-a+1\).'''
new_last = r'''\item Apply \cref{lem:II:reduced-anticanonical-hopf} to
the same minimal Hopf $H$ and the effective anticanonical
divisor $D_H=-K_H$ from \eqref{cdp:eq:C.ML.3}.
Its support is the nonempty disjoint elliptic boundary.
The first assertion has excluded coefficient one for $M>0$,
so the reduced alternative is impossible. The other alternative
gives exactly $D_H=aC$ with $a\ge2$.
The coefficient formula then gives the unique neighbour's
order $k_P=M-a+1$.'''
new82 = pkg.edit(new82, old_last, new_last, 'D12,D20', 'cdp:st:C.2.UN.82', 'Use the full proved effective-divisor alternative on the original maximal Hopf component, after the first assertion has ruled out coefficient one.')
old_tail = r'''The argument uses only the
retained normalized branches, actual surface
point maps, and finite primary covers. It
does not prune a Hopf neighbourhood or assert
a different smoothing of the remaining support.
The exact weight spaces, polynomial factor cases,
nonlinear translation kernels, labelled point-map
forests and maximal-leaf order identities are
independently checked in
\path{code/root_maximal_hopf_leaf.py}; its executed
output is retained beside it. The proof above supplies
the general maps and unbounded arguments.'''
new_tail = r'''All these identifications use the retained normalized
branches and the specified point maps. In particular the
adjunction isomorphism on $C$ and the full reduced-fibre
normal product are the ones on the given endpoint. The finite
modification record of \cref{cdp:st:C.2.UN.77} supplies its
comparison with the original family.'''
new82 = pkg.edit(new82, old_tail, new_tail, 'D02,D07,D08,D09,D11', 'cdp:st:C.2.UN.82', 'Retain the actual mathematical comparison and remove workflow/independence/program claims from the proof. No check count or independent credit is added.')
old_blow = r'''At a reverse point blowup \(\sigma\), their exact
comparison is'''
new_blow = r'''At a reverse point blowup $\sigma$, apply
\cref{lem:II:canonical-boundary-blowup} to the effective
divisors before and after the map. Their canonical-boundary
lines are trivial; its Jacobian comparison, for the pushed
meromorphic section, gives the divisor identity'''
new82 = pkg.edit(new82, old_blow, new_blow, 'D12,D20', 'cdp:st:C.2.UN.82', 'Use P232 on the identical point blowup and effective boundary. The retained ML5 identity specifies the actual meromorphic section, not merely its numerical class.')

split = new82.index(r'\begin{proof}')
new82 = pkg.clean(new82[:split], 'cdp:st:C.2.UN.82', prose=False) + '\n' + pkg.clean(new82[split:], 'cdp:st:C.2.UN.82')
new82 = new82.replace(r'\ref{', r'\cref{')
new82 = pkg.edit(new82, 'Take an sequence of point blowdowns', 'In the remaining cases, take a sequence of point blowdowns', 'D20,D23', 'cdp:st:C.2.UN.82', 'The rational case was completed in the preceding paragraph; identify the remaining ruled/Hopf point maps and correct the article after prose cleanup.')
new82 = pkg.edit(new82, 'the principal full-fibre trivialization; it retains\nthe line isomorphism, rather than just intersections.', 'the principal full-fibre trivialization; together these maps\nfix the line isomorphism and the displayed divisor.', 'D02,D20', 'cdp:st:C.2.UN.82', 'State the exact divisor and line maps directly, preserving both conclusions.')
new82unit = r'\subsection{Maximal canonical order and Hopf leaves}\label{subsec:II:maximal-hopf-leaves}' + '\n\n' + new82
remainder = r'\subsection{Reduction at negative-coefficient interfaces}\label{subsec:II:negative-interface-reduction}'
pkg.guard('UN82-complete-unit', old82, new82unit + '\n' + remainder, 'Replace the complete UN82 unit, transferring only the exact common residue and Hopf coefficient proofs; preserve its full NC/labelled-branch domain and every conclusion. The following unreviewed remainder has a separate open subsection.')

for suffix, value in [('P338', p338), ('P325', new325unit), ('UN64_receiving', new64), ('UN82', new82unit)]:
    (OUT / ('S6_SERIES_PUBLISH_II_sec11_hopf_boundaries_' + suffix + '.tex')).write_text(value + '\n', newline='\n')
for row in pkg.rows:
    if row['statement_id'] == 'cdp:st:C.2.UN.64':
        row['old_location'] = row['new_location'] = 'subsec:II:terminal-ruled-contractions / cdp:st:C.2.UN.64'
    elif row['statement_id'] == 'lem:II:reduced-anticanonical-hopf':
        row['old_location'] = row['new_location'] = 'subsec:II:anticanonical-hopf-boundaries / lem:II:reduced-anticanonical-hopf'
    elif row['statement_id'] == 'lem:II:anticanonical-bisection':
        row['new_location'] = 'subsec:II:anticanonical-bisections / lem:II:anticanonical-bisection'
pkg.write(new82unit)
receiving = main
for g in pkg.guards:
    assert receiving.count(g['old']) == 1, (g['key'], receiving.count(g['old']))
    receiving = receiving.replace(g['old'], g['new'], 1)
for pattern in [r'\\label\{([^{}]+)\}', r'\\hypertarget\{([^{}]+)\}']:
    for x in set(re.findall(pattern, old64 + old325 + old82)):
        assert re.findall(pattern, receiving).count(x) == re.findall(pattern, main).count(x), x
print('Four guards replay once; all old labels and permanent targets preserved. No shared write.')
