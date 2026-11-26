from S6_SERIES_PUBLISH_c3_edit import *

old=r'''At a point blowup the canonical identity has exceptional
coefficient $1+a-\mu$, where $a$ is the new divisor coefficient
and $\mu$ the multiplicity at the centre. Intersecting with the
exceptional curve gives $a=\mu-1$, as in the proof of
\cref{night:P4R.3}.'''
new=r'''At each point blowup, apply
\cref{lem:II:canonical-boundary-blowup} to the pushed-forward
conductor and its strict transform with exceptional coefficient
$a$. Its multiplicity $\mu$ at the centre gives $a=\mu-1$.'''
apply_edit(old,new,'II-C3-HOPF-BOUNDARY-APPLICATION',['D12'],
    'night:P4R.5','second proof item',
    'The same effective integral conductor has torsion canonical-boundary line; apply P232 with m=mu and retain every subsequent local graph operation and Euler count.')
apply_edit('The\nnormalization formula gives\n\\[\n e(C)=c+s-2g-b.',
    'Apply \\cref{lem:II:curve-normalization-graph} to each of the\n$s$ connected components. Since exactly $g$ normalized components\nhave genus one and the rest have genus zero, its Euler formula gives\n\\[\n e(C)=c+s-2g-b.',
    'II-C3-HOPF-CURVE-APPLICATION',['D12'],'night:P4R.5','third proof item',
    'The disconnected-curve Euler formula is exactly the sum of P245 over its connected components, with the same c,s,g,b.')

text=SOURCE.read_text();mid=text.index(r'\label{night:P4.21}')
a=text.index(r'\item On $\mathbb P^2$',mid)
b=text.index(r'\item We follow these alternatives through the blowups.',a)
old=text[a:b]
new=r'''\item Apply the minimal-boundary enumeration in
\eqref{cdp:eq:A.RT.13}--\eqref{cdp:eq:A.RT.16} to this same
$(T_0,D_0)$. On $\mathbb P^2$ its divisor is the listed plane
cubic. On $\mathbb F_n$ the tautological class $h$ and minimal
section $C_0$ are related by $h=C_0+nF$; thus
$2h+(2-n)F=2C_0+(n+2)F$, exactly the anticanonical class
in that enumeration. The ruling and fibre class are unchanged.

A smooth elliptic cubic or bisection has fundamental group
$\mathbb Z^2$. Every other listed support has rational
normalization components. The graph formula in
\cref{lem:II:curve-normalization-graph} gives $\mathbb Z$ for
a nodal cubic, a triangle of lines, a transverse conic and line,
a rational cycle formed by two sections and their vertical
components, or a rational bisection and a fibre meeting at two
distinct points. These are reduced nodal divisors. The section
intersection and vertical-degree equality $k+d=2$ in
\cref{prop:II:minimal-boundary-complements} makes every coefficient
in such a cycle one. Coincident intersections, a vertical fibre
through a section-intersection point, a tangency, a cusp, and
the multiple-component cases have tree incidence graph. Their
supports are simply connected. Thus the only nontrivial groups
are $\mathbb Z$ and $\mathbb Z^2$, and both occur only for
reduced nodal conductor.

'''
apply_edit(old,new,'II-C3-RATIONAL-BOUNDARY-ENUMERATION',['D12','D20'],
    'night:P4.21','minimal-boundary cases in proof',
    'Use the earlier complete P210 enumeration for the identical (T0,D0); give the exact basis conversion h=C0+nF. Retain all old fundamental-group alternatives and identify their actual incidence configurations through P245.')

old=r'''For each reversed point blowup $q$ with exceptional curve $E$,
the canonical formula $K_{\mathrm{new}}=q^*K_{\mathrm{old}}+E$
gives $D_{\mathrm{new}}=q^*D_{\mathrm{old}}-E$.
Its exceptional coefficient is $\mu-1$, where $\mu$ is the
conductor multiplicity at the centre. Effectivity therefore puts
every centre on the conductor.'''
new=r'''At each reversed point blowup $q$, apply
\cref{lem:II:canonical-boundary-blowup} with the anticanonical
divisors $D_{\rm new},D_{\rm old}$ and centre multiplicity $\mu$.
It gives $D_{\rm new}=q^*D_{\rm old}-E$ and exceptional
coefficient $\mu-1$, so every centre lies on the conductor.'''
apply_edit(old,new,'II-C3-RATIONAL-BOUNDARY-BLOWUP',['D12'],
    'night:P4.21','first proof item',
    'Apply the same intrinsic canonical line-bundle identity and effectivity conclusion from P232 to the anticanonical rational-boundary data.')
text=SOURCE.read_text();mid=text.index(r'\label{night:P4.21}')
a=text.index(r'\item We follow these alternatives through the blowups.',mid)
b=text.index(r'If the initial group was nontrivial,',a)
old=text[a:b]
new=r'''\item At every blowup, \cref{lem:II:boundary-blowup-groups}
identifies the boundary fundamental groups through the actual
blowdown map. Thus $\pi_1(D_{\rm red})$ is unchanged along the
chosen sequence.
'''
apply_edit(old,new,'II-C3-RATIONAL-BOUNDARY-GROUPS',['D12'],
    'night:P4.21','blowup topology in proof',
    'Transfer this existing exceptional-sphere quotient proof to P246 and use its identical boundary map; the remaining reduced-nodal preservation argument stays here.')
apply_edit('For a connected curve\nwith rational normalized components, this is the free\ngroup $F_b$ of its point-identification graph, so\n$b\\le1$.',
    'Apply \\cref{lem:II:curve-normalization-graph} to this\nconnected rationally normalized curve. It identifies the group\nwith $F_b$ and gives $b\\le1$.',
    'II-C3-RATIONAL-IMAGE-GRAPH',['D12'],'night:P4.21','final proof item',
    'Use the same conductor curve C and its already established virtually abelian group in the earlier graph formula.')

old=r'''The canonical blowup
formula in \cite[II.3, pp.~17--18]{Beauville1978}, together with
$K+D\equiv0$, gives conductor coefficient $\mu-1$ on the exceptional
curve.'''
new=r'''At each point blowup, \cref{lem:II:canonical-boundary-blowup}
applies to the same effective conductor with $c_1(K+D)=0$
and gives exceptional coefficient $\mu-1$.'''
apply_edit(old,new,'II-C3-ELLIPTIC-BOUNDARY-APPLICATION',['D12'],
    'night:P4.22','double-section proof item',
    'Use P232 with the same conductor, centre multiplicity and ruled surface, retaining the local tree construction.')
apply_edit('and every point blowup preserves this inclusion map. Hence\n$\\pi_1(D_{\\mathrm{red}})\\to\\pi_1(T)$ is an isomorphism.',
    'and \\cref{lem:II:boundary-blowup-groups} preserves both groups\nand their inclusion homomorphism at every point blowup. Hence\n$\\pi_1(D_{\\mathrm{red}})\\to\\pi_1(T)$ is an isomorphism.',
    'II-C3-ELLIPTIC-BLOWUP-GROUP-APPLICATION',['D12'],'night:P4.22',
    'double-section proof item','Apply the commuting group maps of P246 to the exact section/ruling inclusion used here.')
apply_edit('The curve-graph formula gives $e(C)\\ge0$.',
    'The formula in \\cref{lem:II:curve-normalization-graph} gives $e(C)\\ge0$.',
    'II-C3-ELLIPTIC-CURVE-APPLICATION',['D12'],'night:P4.22','double-section proof item',
    'Identify the common owner of the curve formula for the same connected C, with its proved virtual abelianness.')
for label in ['night:P4R.5','night:P4.21','night:P4.22']:
    add_event(label,'II-C3-ROOT-SMOOTH-CONDUCTOR-'+label.split(':')[-1],
        'used and rechecked in this run',
        'Complete original and receiving statement/proof read. Repeated canonical-boundary, blowup-group and normalization-graph arguments now apply P232/P246/P245 with the exact same maps and hypotheses. The rational-boundary enumeration uses the precise h=C0+nF change; all geometric cases, finite conductor pushouts, local branches, signs and equality arguments remain. Exposed comparison, no independent or final-PDF credit.',
        'S6_SERIES_PUBLISH_II.tex',source='code/S6_SERIES_PUBLISH_c3_smooth_conductor_applications.py')
print('Hopf, rational and elliptic-ruled smooth-normalization proofs use the common earlier topology owners.')
