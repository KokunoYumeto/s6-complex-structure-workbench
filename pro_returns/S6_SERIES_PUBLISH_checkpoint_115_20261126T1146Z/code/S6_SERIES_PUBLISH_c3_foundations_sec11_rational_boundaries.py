from S6_SERIES_PUBLISH_c3_foundations_sec11_helpers import *
from collections import Counter

main = (ROOT / 'S6_SERIES_PUBLISH_II.tex').read_text()
p = Package('rational_boundaries', 'subsec:II:rational-boundaries-maxima')
old69 = block(main, 'cdp:st:C.2.UN.69')
old81 = block(main, 'cdp:st:C.2.UN.81')
old85 = block(main, 'cdp:st:C.2.UN.85')
for number, original in [(69, old69), (81, old81), (85, old85)]:
    assert (OUT / f'S6_SERIES_PUBLISH_II_sec11_reductions_UN{number}_input.tex').read_text().rstrip() == original

new69 = p.clean(old69, 'cdp:st:C.2.UN.69')
for m in list(re.finditer(r'\\ref\{(cdp:[^{}]+)\}', new69)):
    a = m.group(0)
    if a in new69:
        new69 = p.edit(new69, a, r'\cref{' + m.group(1) + '}', 'D04', 'cdp:st:C.2.UN.69', 'Use the type and current number of the unchanged statement owner.')

a = new69.index(r'\par\medskip\noindent\textbf{A positive-square rational curve on a component.}')
b = new69.index(r'\par\medskip\noindent\textbf{A maximum with a rational boundary is already minimal.}', a)
transferred69 = new69[a:b]
new69 = new69[:a] + new69[b:]

a81 = old81.index('Here rationality does not require')
b81 = old81.index('\n\n\n\\begin{enumerate}', a81)
transferred81 = old81[a81:b81]
application81 = r'''Apply \cref{lem:II:positive-rational-curve} to the smooth normalization with $(T,C)=(Q,E)$. Its hypotheses hold at this full reduced NC stage, and $E^2=1$. It gives rationality and the complete-linear-system morphism \eqref{cdp:eq:C.AP.9}, with the same pair $(Q,E)$ in place of $(T,C)$. This morphism is an isomorphism near $E$, maps $E$ isomorphically to the line $\ell$, and contracts every other boundary because it is disjoint from $E$.'''
new81 = old81[:a81] + application81 + old81[b81:]

owner = r'''\begin{lemma}[Positive-square rational curves on fibre components]\hypertarget{tag-P365}{}\label{lem:II:positive-rational-curve}
\StatementRecord{lem:II:positive-rational-curve}{proved}{P365}{\cref{lem:II:cyclic-component-cover,cdp:st:C.2.UN.15,cdp:st:C.2.UN.19,cdp:st:C.2.UN.31,lem:II:negative-kodaira-models}; \eqref{eq:II:quasibundle-canonical}; \cite[Proposition~3.12, p.~20]{PopescuPampu2016}}
Let $f:U\to\Delta$ be a proper degeneration of connected complex two-tori from a smooth complex threefold, with full reduced normal-crossing central fibre and smooth component normalizations. Let $T$ be one such normalization, and let $C\subset T$ be a smooth rational curve with $C^2>0$. Then $T$ is rational.

For $C^2=s\in\{1,2\}$, blow up any $s$ distinct points of $C$, writing $\mu:T'\to T$ and $C'$ for its strict transform. The complete system $|C'|$ gives a proper map $q:T'\to\PP^1$ with connected rational general fibre and $q^*\OO_{\PP^1}(1)=\OO_{T'}(C')$. Every irreducible curve on $T$ disjoint from $C$ is unchanged by $\mu$ and is a rational vertical curve for $q$.

For $C^2=1$, the complete system $|C|$ gives a birational morphism $\rho:T\to\PP^2$, isomorphic on a neighbourhood of $C$, with $\rho^*\OO_{\PP^2}(1)=\OO_T(C)$ and $\rho|_C:C\xrightarrow{\sim}\ell$ for a line $\ell$. It factors into point blowdowns away from $C$ and contracts every irreducible curve disjoint from $C$.
\end{lemma}
\begin{proof}
Take a minimal-model map $\pi:T\to Z$. The possible minimal models are given by \cref{cdp:st:C.2.UN.15,cdp:st:C.2.UN.19,lem:II:negative-kodaira-models}. On a nonrational ruled $Z$, every rational curve maps constantly to the positive-genus ruling base. A nonexceptional rational curve on $T$ is therefore the strict transform of a ruling fibre and has nonpositive square; every exceptional curve has negative square. On a Hopf $Z$, every compact curve is elliptic by \cref{lem:II:hopf-curves}, so every rational curve on $T$ is exceptional. These alternatives exclude $C^2>0$.

For the remaining case $\kappa(Z)\ge0$, apply \cref{lem:II:cyclic-component-cover} to the same central component with $m_i=1$. Its root map is $t=s$, its group is $G=\{1\}$ and its degree-one component map $E\to T$ is proper bimeromorphic. Thus the minimal surface $E_0$ in \cref{cdp:st:C.2.UN.31} is this same $Z$. It is a torus or the fixed-Jacobian elliptic model there, with full fibres $m_bC_b$ and identity monodromy. In the torus case $K_Z$ is trivial. In the elliptic case take $\ell_0>0$ divisible by every $m_b$. The canonical map \eqref{eq:II:quasibundle-canonical} and $q_0^*(b)=m_bC_b$ give
\[
 K_Z^{\otimes\ell_0}\simeq q_0^*L,\qquad
 L=K_B^{\otimes\ell_0}\otimes\OO_B\Bigl(\sum_b\ell_0(1-1/m_b)b\Bigr),
\]
with
\begin{equation}
 \frac{\deg L}{\ell_0}=2g(B)-2+\sum_b(1-1/m_b)\ge0.
 \hypertarget{tag-00SW}{}\label{cdp:eq:C.NM.5}
\end{equation}
Indeed a nonzero pluricanonical section has a nonzero power of exponent divisible by $\ell_0$, and $q_{0*}\OO_Z=\OO_B$ identifies it with a section of a positive power of $L$. Hence $\deg L\ge0$, and $K_Z$ is nef. The point-blowup Jacobians give $K_T=\pi^*K_Z+\sum_Eb_EE$ with $b_E>0$. A nonexceptional $C$ then has $K_T\cdot C\ge0$, whereas adjunction gives $K_T\cdot C=-2-C^2<0$. An exceptional $C$ has negative square. The remaining minimal model is rational, proving
\begin{equation}
 \text{a smooth rational curve of positive square on }T
 \quad\Longrightarrow\quad T\text{ is rational}.
 \hypertarget{tag-00SV}{}\label{cdp:eq:C.NM.4}
\end{equation}

For $s=1$ or $2$, the specified point blowups give $C'^2=0$ and leave every curve disjoint from $C$ unchanged. The rational surface $T'$ has $H^1(T',\OO_{T'})=0$. The restriction sequence for $\OO_{T'}(C')$, with $\OO_{C'}(C')\simeq\OO_{\PP^1}$, gives a second section nonzero everywhere on $C'$. Together with the section cutting out $C'$, it generates $\OO_{T'}(C')$ and defines
\begin{equation}
 q:T'\longrightarrow\PP^1,\qquad
 q^*\OO_{\PP^1}(1)=\OO_{T'}(C').
 \hypertarget{tag-00SX}{}\label{cdp:eq:C.NM.6}
\end{equation}
The fibre $C'$ is reduced and connected. In the Stein factorization a finite map of degree greater than one would give either several points over this value or multiplicity greater than one on $C'$. Hence $q$ has connected fibres, and adjunction gives genus zero on its smooth general fibre. Each selected exceptional curve meets $C'$ once and is a section of $q$. On the rational projective surface $T'$, a fibre coordinate using one such section gives a birational map over $\PP^1$ to $\PP^1\times\PP^1$: on the generic genus-zero fibre its degree-one section divisor has two independent sections and defines that coordinate. Normalize and resolve its graph. The two resulting maps are compositions of point blowups by \cite[Propositions~3.10 and~3.12, p.~20]{PopescuPampu2016}. Every vertical component on this common resolution is a strict transform of a rational fibre or an exceptional rational curve. Its image on $T'$ is therefore rational. An irreducible curve disjoint from $C$ has intersection zero with $C'$, so is vertical for the same $q$.

Finally suppose $C^2=1$. The exact sequence
\begin{equation}
 0\longrightarrow\OO_T\longrightarrow\OO_T(C)
 \longrightarrow\OO_C(1)\longrightarrow0
 \hypertarget{tag-009Y}{}\label{cdp:eq:C.AP.8}
\end{equation}
and $H^1(T,\OO_T)=0$ give three sections. They generate the line on $C$, and the section defining $C$ is nonzero off $C$. Thus the complete system gives
\begin{equation}
 \rho:T\longrightarrow\PP^2,\qquad
 \rho^*\OO_{\PP^2}(1)=\OO_T(C),\qquad
 \rho|_C:C\xrightarrow{\sim}\ell.
 \hypertarget{tag-009Z}{}\label{cdp:eq:C.AP.9}
\end{equation}
Its image is a surface since $C^2=1$; the degree formula gives degree one, so $\rho$ is birational. The section cutting out $C$ is the pullback of a linear equation of $\ell$, so $\rho^*\ell=C$ as divisors. Apply \cite[Proposition~3.12, p.~20]{PopescuPampu2016} to this proper morphism of smooth surfaces. Every exceptional curve has zero intersection with $\rho^*\OO(1)=\OO_T(C)$, so is disjoint from $C$, and the displayed divisor equality places its image off $\ell$. The factorization is consequently by point blowdowns away from $C$ and is an isomorphism near $C$. Every irreducible curve disjoint from $C$ has degree zero under $\rho^*\OO(1)$ and is contracted.
\end{proof}
'''

p.record('D12,D20,D25', 'lem:II:positive-rational-curve', transferred69 + '\n' + transferred81, owner,
         'One earlier owner preserves both complete curve arguments and all five transferred equation targets. The full reduced NC normalization scope is checked through m_i=1 and G={1} in P240/UN31; no no-triple hypothesis enters this argument. The selected s=1 or 2 blowups, square-zero pencil, s=1 complete plane system and their exact morphisms remain. The canonical degree identity is the same P351 general quasibundle map, independently of its star clauses.')
for equation in p.equations:
    if equation['old_tag'] in ['C.NM.4', 'C.NM.5', 'C.NM.6']:
        equation['owner'] = 'lem:II:positive-rational-curve'
for old_tag in ['C.AP.8', 'C.AP.9']:
    p.equations.append(dict(old_tag=old_tag, label='cdp:eq:' + old_tag, owner='lem:II:positive-rational-curve'))
    old_display = next(m.group(0) for m in re.finditer(r'\\\[([\s\S]*?)\\\]', transferred81) if r'\tag{' + old_tag + '}' in m.group(0))
    new_display = next(m.group(0) for m in re.finditer(r'\\begin\{equation\}([\s\S]*?)\\end\{equation\}', owner) if r'\label{cdp:eq:' + old_tag + '}' in m.group(0))
    p.record('D19', 'lem:II:positive-rational-curve', old_display, new_display, 'Move this exact sequence or plane-map identity to P365 under (T,C)=(Q,E), using the section equation counter and preserving its old label and hypertarget.')

new69 = p.edit(new69, 'Equation \\eqref{cdp:eq:C.NM.4} first makes $T$ rational; no rational\npencil is used before this conclusion. The pencil\n\\eqref{cdp:eq:C.NM.6} then makes every other disjoint boundary rational.',
              'Apply \\cref{lem:II:positive-rational-curve} to this $(T,C_e)$, with the value $s=C_e^2$ in \\eqref{cdp:eq:C.NM.8}. It gives rationality and the pencil \\eqref{cdp:eq:C.NM.6}; every other disjoint boundary is a rational vertical curve.',
              'D02,D12,D20', 'cdp:st:C.2.UN.69', 'Apply the same curve and its selected point blowups to the single earlier owner; retain the exact s=1 or 2 alternatives and the conclusion for every disjoint boundary.')
new69 = p.edit(new69, 'By\n\\eqref{cdp:eq:C.NM.4} the endpoint surface is rational. The pencil\n\\eqref{cdp:eq:C.NM.6} makes every other boundary on it rational.',
              'Apply \\cref{lem:II:positive-rational-curve} to this higher endpoint and its incoming curve, whose square is $1$ or $2$. The resulting pencil \\eqref{cdp:eq:C.NM.6} makes every other disjoint boundary rational.',
              'D12,D20', 'cdp:st:C.2.UN.69', 'The rational-edge path uses the same specific curve and selected-blowup pencil as the earlier owner, without a maximum assumption.')

for a, b, kinds, reason in [
    ('No minimality assumption is made on any $T_v$.', 'The components $T_v$ may be nonminimal.', 'D02,D11', 'State the full nonminimal domain positively.'),
    ('give the same line maps as \\eqref{cdp:eq:C.MR.3}--\\eqref{cdp:eq:C.MR.4}, without a\nminimality assumption:', 'give the line maps \\eqref{cdp:eq:C.MR.3}--\\eqref{cdp:eq:C.MR.4} on these possibly nonminimal components:', 'D02', 'Use the full domain already stated in the proposition.'),
    ('These formulas retain the meromorphic section and\ndual-normal trivialization.', 'These are the meromorphic-section and dual-normal line maps.', 'D08', 'Name the mathematical maps directly.'),
    ('This is a statement about the surface\nmorphism; no ambient contraction of $E$ is invoked.', 'These are point blowdowns of the surface $T$.', 'D02', 'Keep the exact surface-morphism domain positively.'),
    ('The exact restrictions at an edge.', 'Canonical restrictions at an edge.', 'D08', 'Use a mathematical heading.'),
    ('Following rational edges gives point contractions.', 'Point contractions along rational edges.', 'D08', 'Use a mathematical heading.'),
    ('the recorded\nordinary-blowup reconstruction follow.', 'the inverse ordinary-blowup reconstruction follow.', 'D08', 'State the inverse geometric construction.'),
    ('an nearby fibre', 'a nearby fibre', 'D23', 'Correct the article after removal of the process qualifier.'),
    ('so it is an \\cref{cdp:st:C.2.UN.64} leaf.', 'so it is a terminal leaf classified in \\cref{cdp:st:C.2.UN.64}.', 'D23', 'Use a grammatical typed reference to the same terminal-pair classification.'),
]:
    if a in new69:
        new69 = p.edit(new69, a, b, kinds, 'cdp:st:C.2.UN.69', reason)

header = r'\subsection{Rational boundaries and maximum components}\label{subsec:II:rational-boundaries-maxima}'
receiver = header + '\n\n' + owner + '\n' + new69
p.guard('Complete rational-boundary maximum unit', old69, receiver.rstrip(), 'Complete UN69 receiver with the single earlier P365 owner; every original maximum, point-contraction, Euler and inverse-neighbourhood conclusion remains.')
p.guard('UN81 positive-square curve and plane application', old81, new81, 'Only its repeated rationality/complete plane-map proof transfers to P365. Full statement and all other proof paragraphs are unchanged; AP8/AP9 targets now occur exactly once at P365.')
p.record('D12,D20', 'cdp:st:C.2.UN.81', transferred81, application81, 'Apply P365 with (T,C)=(Q,E) at the same full reduced NC stage. The plane morphism, marked line, neighbourhood isomorphism and contraction of disjoint boundaries are the same maps.')

new85 = old85
for a, b in [
    ('block (C.AP.8)--(C.AP.13). Each gives a strict', 'block: apply \\cref{lem:II:positive-rational-curve} with $T$ the receiving normalization and $C$ the image of this last curve, whose square is $1$, and then use the finite progress in \\eqref{cdp:eq:C.AP.10}--\\eqref{cdp:eq:C.AP.13}. Each gives a strict'),
    ('and (C.AP.8)--(C.AP.13) supply the finite\nplane progress block.', 'and the plane-map clause of \\cref{lem:II:positive-rational-curve}, applied to that receiving pair, followed by \\eqref{cdp:eq:C.AP.10}--\\eqref{cdp:eq:C.AP.13}, supplies the finite plane progress block.'),
]:
    new85 = p.edit(new85, a, b, 'D04,D12,D20', 'cdp:st:C.2.UN.85', 'After AP8/AP9 transfer, replace the old contiguous display range by the exact earlier plane-map clause and the unchanged later plane-progress block; the full receiving pair and its order are unchanged.')
p.guard('UN85 exact plane-map consumers', old85, new85, 'Complete original/receiving proof comparison for two bounded reference applications only; the statement and all other proof text remain byte-identical.')
p.record('D13,D14', 'cdp:st:C.2.UN.69', 'UN69 begins the section without a descriptive subsection and repeats the later plane-map input.', header, 'Give the complete rational-boundary/maximum unit its actual subsection, with its shared curve owner before every consumer.')

for name, text in [('P365', owner), ('UN69', new69), ('UN81_receiving', new81), ('UN85_receiving', new85)]:
    (OUT / f'S6_SERIES_PUBLISH_II_sec11_rational_boundaries_{name}.tex').write_text(text.rstrip() + '\n', newline='\n')
p.write(receiver)

state = main
for guard in p.guards:
    assert state.count(guard['old']) == 1, guard['key']
    state = state.replace(guard['old'], guard['new'], 1)
for pattern in [r'\\label\{([^{}]+)\}', r'\\hypertarget\{([^{}]+)\}']:
    before = Counter(re.findall(pattern, old69 + old81 + old85))
    after = Counter(re.findall(pattern, owner + new69 + new81 + new85))
    allowed = Counter(['lem:II:positive-rational-curve']) if 'label' in pattern else Counter(['tag-P365'])
    assert after - before == allowed and not before - after, (before - after, after - before)
for old, new in [(old81, new81), (old85, new85)]:
    assert old.split(r'\end{proposition}', 1)[0] == new.split(r'\end{proposition}', 1)[0]
for body in re.findall(r'\\begin\{equation\}([\s\S]*?)\\end\{equation\}', receiver):
    assert not re.search(r'\n[ \t]*\n', body)
    assert body.count(r'\SsixEquationAliases') <= 1
print('Three guards replay; P365 is the only new tag; every old identifier preserved; complete receiving proof reading pending.')
