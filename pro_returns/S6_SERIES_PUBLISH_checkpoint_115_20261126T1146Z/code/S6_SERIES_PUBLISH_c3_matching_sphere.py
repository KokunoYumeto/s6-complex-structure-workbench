from S6_SERIES_PUBLISH_c3_edit import *
import re

before=SOURCE.read_text()
ident='cdp:st:A.5.21'
p=before.index(r'\StatementRecord{'+ident+'}')
a=list(re.finditer(r'^\\begin\{proposition\}',before[:p],re.M))[-1].start()
b=before.index(r'\end{proof}',p)+len(r'\end{proof}')
original=before[a:b]
left=original.index(r'\item The function $v$ on $B$ has exactly $d$ distinct')
right=original.index(r'\item The weighted homothety',left)
transferred=original[left:right]
equation=next(m.group() for m in re.finditer(r'\\begin\{equation\}.*?\\end\{equation\}',transferred,re.S)
              if r'\label{cdp:eq:A.BP.3}' in m.group())
lemma=r'''\begin{lemma}[A matching sphere in a conic bundle]\hypertarget{tag-P247}{}\label{lem:II:conic-bundle-matching-sphere}
\StatementRecord{lem:II:conic-bundle-matching-sphere}{proved}{P247}{}
Let $B\subset\mathbb C^2_{x,v}$ be a connected smooth complex curve
such that $v|_B$ has two distinct simple zeros. Put
\[
 X_B=\{(x,y,z)\in\mathbb C^3:(x,yz)\in B\}.
\]
The smooth locus of $X_B$ contains a smoothly embedded two-sphere
whose compact homology class has self-intersection $-2$.
\end{lemma}
\begin{proof}
Choose an embedded arc $\gamma:[0,1]\to B$ between two simple
zeros of $v$, avoiding every other zero. Since $v$ is a local
coordinate at the endpoints, choose the arc radial in that coordinate
there. Over $v\ne0$, the coordinates $(b,y)\in B\times\mathbb C^*$
give the map $(b,y)\mapsto(x(b),y,v(b)/y)$, with inverse
$(x,y,z)\mapsto((x,yz),y)$. At an endpoint write $x=\chi(v)$;
then $(y,z)\mapsto(\chi(yz),y,z)$ is a holomorphic chart, with
inverse projection to $(y,z)$. Thus $X_B$ is smooth near the inverse
image of the arc.

On its interior choose a continuous argument of $v(\gamma(t))$
and functions $A(t),B_0(t)$ with $AB_0=v(\gamma(t))$ and
$|A|=|B_0|=|v(\gamma(t))|^{1/2}$. The map
'''+equation+r'''
lies in $X_B$ and collapses both boundary circles of
$[0,1]\times S^1$ to points. Projection to $(x,yz)$ recovers the
base arc, and $y/A(t)$ recovers the circle coordinate on its
interior. At an endpoint with $v=e^{\mathrm i\phi}|y|^2$, the disk is
\[
 y\longmapsto
 \bigl(\chi(e^{\mathrm i\phi}|y|^2),y,
                         e^{\mathrm i\phi}\overline y\bigr),
\]
with inverse disk coordinate given by projection to $y$.
Consequently the collapsed cylinder is a smoothly embedded sphere.

A parallel-arc isotopy with the same endpoints gives a homologous
sphere meeting the first only at the endpoints. In the holomorphic
chart $(y,z)$ there, rotating $z$ makes their oriented disks
$z=\overline y$ and $z=\eta\overline y$, with
$\eta=a+\mathrm i b\ne1$. In coordinates
$(\Re y,\Im y,\Re z,\Im z)$ their tangent-frame determinant is
$-((a-1)^2+b^2)<0$. Thus their local intersection, or the linking
number of their boundary curves, is $-1$. The relative-chain
comparison in \cref{cdp:st:A.5.15} identifies this with the
intersection of the coned cycles. Both sphere orientations reverse
at the second endpoint, leaving that intersection sign unchanged.
The two local intersections sum to $-2$.
\end{proof}

'''
receiving_steps=r'''\item The function $v$ on $B$ has exactly $d$ distinct simple
zeros: $P(x,0)=P(1,0)x^d$, and $P_x(x,0)=d/x$ at those points.
Apply \cref{lem:II:conic-bundle-matching-sphere} to this smooth
connected curve $B=\{P(x,v)=1\}$. Its surface $X_B$ is exactly
$\{P(x,yz)=1\}$ through the identity map on $(x,y,z)$. The
sphere of \eqref{cdp:eq:A.BP.3} therefore has square $-2$ in $h=1$.

'''
receiving=original[:left]+receiving_steps+original[right:]
after=before[:a]+lemma+receiving+before[b:]
preserve_identifiers(before,after)
for old,new in zip(identifiers(before),identifiers(after)):
    for name,count in old.items():assert new[name]==count,name
assert original[:original.index(r'\end{proposition}')]==receiving[:receiving.index(r'\end{proposition}')]
SOURCE.write_text(after,newline='\n')
rows=[]
for index,kind in enumerate(['D12','D14'],1):
    rows.append(dict(change_id=f'II-C3-MATCHING-OWNER-{index:02}',type=kind,
        statement_id='lem:II:conic-bundle-matching-sphere; cdp:st:A.5.21',
        old_location='A.5.21 proof steps3–4',old_page='source comparison',
        new_location='P247 immediately before A.5.21',new_page='integrated PDF pending',
        old_text=transferred,new_text=lemma+receiving_steps,
        reason='Transfers the complete compact matching-sphere construction and both signed endpoint intersections to one earlier owner. The old binary-product surface is identified by the identity on(x,y,z); its equation label and permanent target move once with the same displayed parameterization. The statement of A.5.21 remains unchanged.',
        review_status='Root read the complete original A.5.21 proof, the full extracted proof and the receiving application; exposed comparison.'))
print('Transfer rows',append_rows(ROOT/'S6_SERIES_PUBLISH_defects_II.tsv',rows,'change_id'))

apply_edit(r'''Any such germ is excluded
in our family: a small generic linear
perturbation $h-c\cdot z$ has Morse critical points.
Their number is the positive multiplicity of the gradient map
\cite[Appendix~B, Lemmas~B.1--B.3 and the positivity proof,
pp.~111--114]{Milnor1968}. It is also the colength of the gradient ideal:
the map $\mathbb C\{u\}\to\mathbb C\{z\}$,
$u_i\mapsto h_{z_i}$, is finite; its three parameters form a regular
sequence, so its target is a free module of that colength. A regular
nearby fibre consists of that many reduced points, each of local degree
one. The boundary degree is unchanged under the small perturbation. A constant perturbation
puts their critical values away from zero.
The original zero divisor is smooth near
a small transverse boundary sphere, so it
retains that boundary property under these
perturbations. The proper boundary
transport in the proof of Proposition~\ref{night:P4.20} carries a
vanishing sphere of square $-2$ into a
nearby torus fibre, which is impossible.''',
    r'''Apply the isolated-hypersurface clause of \cref{cdp:st:A.5.17}
to this same local map $f=h^m$. That clause gives a vanishing sphere
of square $-2$ in the nearby torus fibre and excludes the germ.''',
    'II-C3-SLC-ISOLATED-OWNER',['D12','D17'],'night:P4.25','Step 2',
    'The complete earlier A.5.17 statement and12-step proof were read. Its isolated-hypersurface clause has exactly f=h^m with the chosen unit root, so the full repeated gradient-degree, Morse and boundary-transport proof is replaced by that exact application.')

apply_edit(r'''The last equation has $a'+b'\ge2$ simple nonzero
zeros in its right-hand side. Over an arc joining two of them,
the circles $|y|=|z|$ collapse at the endpoints and form a smooth
embedded sphere. The circle action $(y,z)\mapsto(e^{i\theta}y,
e^{-i\theta}z)$ has moment map proportional to $|y|^2-|z|^2$,
so the sphere is Lagrangian. Its oriented normal Euler number is
$-\chi(S^2)=-2$: the order $(e_1,e_2,Je_1,Je_2)$ differs by one
transposition from the complex orientation $(e_1,Je_1,e_2,Je_2)$.''',
    r'''Define
\[
 x(t)=\frac{t^{b'}+t^{-a'}}2,\qquad
 v(t)=\frac{t^{-a'}-t^{b'}}{2i}.
\]
The map $t\mapsto(x(t),v(t))$ embeds $\mathbb C^*$ as a smooth
connected curve $B$. Its holomorphic inverse is
$t=(x-iv)^r(x+iv)^s$, by the same B\'ezout identity.
The function $v$ has $a'+b'\ge2$ distinct simple zeros:
they satisfy $t^{a'+b'}=1$, and at each of them
$v'(t)=-(a'+b')t^{-a'-1}/(2i)\ne0$.
The surface $X_B$ of \cref{lem:II:conic-bundle-matching-sphere}
is this component of $U_1^aU_2^b=1$ through the identity map
on $(x,y,z)$. That lemma gives the embedded sphere and its
self-intersection $-2$.''',
    'II-C3-SLC-MATCHING-OWNER',['D12'],'night:P4.25','Step 3',
    'Retains unequal component multiplicities a,b and the exact Bezout parameterization. Identifies the base curve by an explicit holomorphic embedding and inverse, counts its simple zeros, and applies the shared matching-sphere proof to exactly the same level component; no uniform-multiplicity hypothesis is imported.')

add_event('lem:II:conic-bundle-matching-sphere; cdp:st:A.5.21; night:P4.25',
    'II-C3-ROOT-MATCHING-SPHERE-TRANSFER','used and rechecked in this run',
    'Read the full original A.5.21 and P4.25 proofs and the complete P247 receiving proof. Compared every chart and inverse, the same compact sphere parameterization and its unchanged equation tag, both negative endpoint determinants, and the isotopy sign. The A.5.21 statement is byte-identical. P4.25 keeps arbitrary a,b, its original full-fibre weighting and all subsequent double/triple deformation cases. Its isolated-germ paragraph applies the already fully read A.5.17 to exactly f=h^m. This is exposed restructuring, not an independent check.',
    'S6_SERIES_PUBLISH_II.tex',source='code/S6_SERIES_PUBLISH_c3_matching_sphere.py')
print('P247 owns the matching sphere; both precise applications admitted.')
