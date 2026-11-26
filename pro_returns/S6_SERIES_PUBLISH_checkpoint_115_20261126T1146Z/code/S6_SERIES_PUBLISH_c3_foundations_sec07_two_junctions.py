from S6_SERIES_PUBLISH_c3_foundations_sec07_helpers import *

s=(ROOT/'S6_SERIES_PUBLISH_II.tex').read_text()
p=Package('two_junctions','night:P4.57')
owner=r'''\begin{lemma}[Genus of residual cubic covers]
\hypertarget{tag-P323}{}\label{lem:II:cubic-spectral-genus}
\StatementRecord{lem:II:cubic-spectral-genus}{proved}{P323}{\cite[III.17--III.18, pp.~45--47]{Beauville1978}}
Let $E$ be a holomorphic rank-two bundle of degree $e$
on $\PP^1$, and let $q\in H^0(\PP^1,\operatorname{Sym}^3E)$
have three distinct generic roots. Use the quotient
projective bundle $p:\PP(E)\to\PP^1$, with tautological
class $\xi$ and fibre class $F$. Remove the common zero
divisor of the coefficients of $q$, of degree $b\ge0$.
Its residual zero divisor $\Gamma$ is reduced, has class
$3\xi-bF$, and satisfies
\begin{equation}
                    p_a(\Gamma)=3e-2-2b.
\label{eq:II:refined-4-55d}
\end{equation}
For irreducible $\Gamma$ with normalization $H$, this is
$g(H)+\delta(\Gamma)$, where $\delta$ is the normalization
colength.

For $\Gamma=\Gamma_H\cup\Gamma_R$, with $\Gamma_H$
irreducible of ruling degree two and $\Gamma_R$ a section,
let $H$ normalize $\Gamma_H$, put
$\delta_H=\delta(\Gamma_H)$ and
$n=\Gamma_H\cdot\Gamma_R$. There is an integer $t$ with
\[
 \Gamma_R=\xi-tF,\qquad
 \Gamma_H=2\xi+(t-b)F,
 \qquad g(H)+\delta_H+n=3e-1-2b.
\]
In degree $e=2$ the individual formulas are
\[
 \begin{split}
       g(H)+\delta_H&=p_a(\Gamma_H)=1+t-b,\\
       n&=4-t-b,\\
       g(H)+\delta_H+n&=5-2b.
 \end{split}\tag{R20.1}\label{eq:one-junction-spectral-bound}
\]
For $e=2$ and $g(H)\ge1$ they give $b\le2$.
When also $b\ge2$,
\[
 b=2,\qquad g(H)=1,\qquad\delta_H=0,
                 \qquad\Gamma_H\cdot\Gamma_R=0.\tag{4.57a}
\]
Thus the double component is smooth and disjoint from
the section.
\end{lemma}
\begin{proof}
The tautological quotient $p^*E\twoheadrightarrow\OO(1)$
and its kernel $L$ are the bundles in
\cite[III.17--III.18, pp.~45--47]{Beauville1978}.
Their holomorphic exact sequence gives
$L=p^*\det E\otimes\OO(-1)$ and
$T_{\PP(E)/\PP^1}=\mathcal Hom(L,\OO(1))$.
Consequently
\[
 \xi^2=e,\quad \xi F=1,\quad F^2=0,
 \qquad K_{\PP(E)}=-2\xi+(e-2)F.
\]
Here the first equality is the degree-two Chern identity
$c_2(p^*E)=c_1(L)\xi=0$; the relative tangent formula
gives the canonical equality by determinants. The
tautological class and the fibre class give the integral
cohomology basis, as in the sphere-bundle argument in
the proof of III.18. These computations use the stated
holomorphic bundles and their maps.

Applying the tautological quotient to $q$ gives a section
of $\OO(3)$. Removing its vertical common zero divisor
leaves $3\xi-bF$. Distinct generic roots make every
horizontal component reduced. Adjunction gives
\[
 (3\xi-bF)(\xi+(e-2-b)F)=6e-6-4b,
\]
and hence \eqref{eq:II:refined-4-55d}. Normalization
of an irreducible curve gives $p_a=g+\delta$.

The section has fibre degree one, so its class is
$\xi-tF$ in this same integral basis; subtraction gives
the class of $\Gamma_H$. Adjunction and intersection give
\[
 p_a(\Gamma_H)=e-1+t-b,\qquad n=2e-t-b.
\]
Equivalently, the exact union sequence
\[
 0\longrightarrow\OO_\Gamma\longrightarrow
 \OO_{\Gamma_H}\oplus\OO_{\Gamma_R}
 \longrightarrow\OO_{\Gamma_H\cap\Gamma_R}
 \longrightarrow0
\]
gives $p_a(\Gamma)=g(H)+\delta_H+n-1$, because the
section is a smooth rational curve. Setting $e=2$ proves
\eqref{eq:one-junction-spectral-bound}. Since
$\delta_H,n\ge0$, positive genus gives $b\le2$.
For $b\ge2$, the same identity reads
\[
 (g(H)-1)+\delta_H+n+2(b-2)=0.
\]
All terms are nonnegative, so all vanish. This proves
\eqref{eq:II:manual:4.57a} and the asserted smoothness
and disjointness.
\end{proof}
'''
owner=p.clean(owner,'lem:II:cubic-spectral-genus')
anchor=r'\subsection{The conductor graph and the horizontal spectral cover}'
assert s.count(anchor)==1
p.guard('P323-before-horizontal-cover',anchor,owner+'\n'+anchor,
 'One earlier proved spectral-genus owner for the exact e=0/e=2 applications. It carries the existing 4.55d,4.57a,R20.1 labels and their complete calculation.')
p.record('D12,D14,D17,D20,D25','lem:II:cubic-spectral-genus',
 'P455 general ruled genus; P457 e=2 equality; R20 individual double-plus-section formulas.',owner,
 'Consolidate the identical tautological/adjunction calculation with all formulas and equality conclusions. The full P455 normal-direction maps stay at their owner. The holomorphic tautological sequence and relative tangent map justify the exact analytic form of the opened Beauville III.17–18 formulas.')

old55=block(s,'night:P4.55')
a=old55.index(r'\item For a rank-two bundle of degree $e$')
b=old55.index('Both alternatives are impossible.',a)
oldpara=old55[a:b]
newpara=r'''\item Apply \cref{lem:II:cubic-spectral-genus} to this
$E_0$, the pulled-back normal cubic and its common zero
divisor of degree $b$. The preceding derivative maps
identify the same $H$ with the normalization of
$\Gamma_H$, and in degree two identify the third sheet
with $\Gamma_R$. The lemma gives
\eqref{eq:II:refined-4-55d} for this residual divisor.
With \eqref{eq:II:refined-4-55c}, it equals $-2-2b$.
In degree three the normalization formula gives
$p_a(\Gamma)\ge g\ge1$. In degree two the lemma's
union formula gives $p_a(\Gamma)\ge g-1\ge0$.
'''
new55=old55.replace(oldpara,newpara)
p.guard('P455-spectral-genus-application',oldpara,newpara,
 'Only the repeated genus calculation moves. The full refined P455 statement/domain, both normal-direction maps, common-zero divisor and e=0/e=2 applications remain.')
p.record('D12,D14,D17,D20','night:P4.55',oldpara,newpara,
 'Apply P323 to the identical pulled-back bundle, cubic and residual spectral components. The old general equation label moves with its sole proof; both later uses keep their exact e value.')

start=s.index(r'\subsection',s.rfind(r'\subsection',0,s.index(r'\label{night:P4.57}')))
stop=s.index(r'\subsection',start+12)
oldunit=s[start:stop]
old=block(oldunit,'night:P4.57')
new=old
new=new.replace(r'\StatementRecord{night:P4.57}{proved}{02XW}{}',r'\StatementRecord{night:P4.57}{proved}{02XW}{\cref{night:P4.55,night:P4.56,night:P4R.19,lem:II:cubic-spectral-genus,lem:II:smooth-curve-intersection,cdp:st:A.5.17}}')
new=p.edit(new,r'''The remaining degree-two configuration of \cref{night:P4.55,night:P4.56}
cannot have its image-conductor graph cycle realized at''',r'''In the degree-two configuration of \cref{night:P4.55,night:P4.56},
the image-conductor graph cycle cannot be realized at''',
 'D01,D08','night:P4.57','Retain the exact full P455/P456 domain in direct mathematical wording.')
a=new.index(r'\paragraph{The global spectral equality.}')
b=new.index(r'\paragraph{The graph support at a junction.}',a)
oldgenus=new[a:b]
newgenus=r'''\paragraph{The spectral equality.}
Let $p,q$ be the two distinct junctions. Their cubic
vanishing gives a common zero divisor of degree $b\ge2$.
Use the bundle $E=N_{A/Y}^*$ of degree two and the
normal-direction maps of \cref{night:P4.55}. They identify
this same $H$ with the normalization of $\Gamma_H$ and
the rational third sheet with the section $\Gamma_R$.
Apply \cref{lem:II:cubic-spectral-genus} to this cubic,
$e=2$, and its residual divisor $3\xi-bF$.
Since $g(H)\ge1$, it gives \eqref{eq:II:manual:4.57a}.
The two common cubic zeros are simple, the double spectral
cover is smooth, and it is disjoint from the third section.

'''
new=p.edit(new,oldgenus,newgenus,'D03,D12,D14,D17,D20','night:P4.57',
 'The complete genus and union-sequence calculation has one earlier owner at P323. Match the exact normal-direction curves, e=2, positive genus and two distinct zeros; preserve all equality conclusions and move4.57a with its proof.')
new=p.edit(new,'The length calculation in \\cref{night:P4.56} makes it smooth, contradicting its',
 'Apply \\cref{lem:II:smooth-curve-intersection} to that branch and\nthe indicated $H$ branch, with $\\Gamma=A$ and $r=1$ or\n$r=2$. It makes the branch smooth, contradicting its',
 'D12,D20','night:P4.57','Use the exact earlier length-one/two owner on the same two hypersurface branches, including the normal-order-two identification at r=2.')
new=p.edit(new,'Branches carrying\nonly $B$ have been retained in this conclusion.',
 'This conclusion includes branches carrying only $B$.',
 'D08','night:P4.57','Express the included branch support positively.')
new=p.edit(new,r'''The ruling descends to $r_N:N\to H$. Its restriction
to $H$ is the identity, and $R$ maps to a fixed point
$b_0\in H$.''',r'''Write $B_H$ for the ruling base, and use the maps
$q:N\to B_H$ and $h:B_H\simeq H$ in
\cref{night:P4.55}. Put $r_N=h\circ q:N\to H$.
Via its embedded image in $N$, the restriction to $H$
is the identity. The rational curve $R$ maps to a fixed
point $b_0\in H$.''',
 'D20','night:P4.57','Define the descended ruling by the exact previously proved section/base identification; preserve every coincidence through exceptional chains.')
a=new.index('The nonzero quadratic form of $F_H$ has a double root.')
b=new.index(r'\item For $F_R$',a)
oldnorm=new[a:b]
newnorm=r'''The nonzero quadratic form of $F_H$ has a double root.
Choose a complementary normal coordinate $X$ so that,
for $A=\{X=Y=0\}$, the restriction $F_H|_{X=0}$ is
$Y^2$ times a unit. Apply
\cref{lem:II:smooth-curve-intersection} with
$(\phi,\psi,\Gamma)=(X,F_H,A)$ and $r=2$.
Here $X=0$ is the auxiliary smooth hypersurface used
for this calculation. The lemma's coordinate map keeps
$X,z$ and gives the exact equation
\[
                         F_H=Y^2+X^2k(X,z).
\]
Its spectral curve is $u^2+k(0,z)=0$. By
\eqref{eq:II:manual:4.57a} this curve is smooth, and its
double cover ramifies at $p$. Hence $k_z(0,0)\ne0$.
The last clause of \cref{lem:II:smooth-curve-intersection}
identifies its smooth normalization with
$\{u^2+k(X,z)=0\}\to\{F_H=0\}$ by $Y=Xu$,
with inverse $u=Y/X$ off $A$. Thus $F_H$ supplies
one generic $B$ branch.

'''
new=p.edit(new,oldnorm,newnorm,'D12,D17,D20,D25','night:P4.57',
 'The exact auxiliary smooth hypersurface X=0 meets F_H only in A with length2, so P299 applies even though F_R may be singular. Its full function coordinate map and finite normalization, together with P323 smooth ramified spectral curve, give the same single B branch.')
oldhess=r'''Its Hessian has rank at least two. Rank three gives an
isolated critical point. In rank two the holomorphic
Morse lemma with a parameter gives the exact equation
$U^2+V^2+h(W)$.'''
newhess=r'''Writing $L=\ell_X X+\ell_Y Y$, the Hessian minors
on $(X,z)$ and $(Y,z)$ are $-\ell_X^2$ and $-\ell_Y^2$.
At least one is nonzero, so its rank is at least two.
Rank three gives an isolated critical point. In rank two,
apply the square-completion coordinate construction in
the proof of \cref{cdp:st:A.5.17} to a nondegenerate
two-dimensional Hessian block, keeping the third coordinate
$W$ as parameter. Each step solves the corresponding
first derivative for its unique holomorphic centre and
uses $U=(w_1-\alpha)\sqrt A$, with the inverse given
by that equation's unique small solution. The nonzero
Schur complement permits the second step. This gives
the exact function $U^2+V^2+h(W)$.'''
new=p.edit(new,oldhess,newhess,'D12,D17,D20,D22,D25','night:P4.57',
 'Place both original Hessian minors at the rank claim. Apply the existing explicit holomorphic square-completion maps to precisely the nondegenerate 2-block, keeping W fixed; no torus or isolated-critical hypothesis is imposed on this coordinate construction.')
oldlast=r'''\item All allocations in (4.57b) have been excluded, proving
the assertion. The genus equality is equivalently
$(g(H)-1)+\delta(\Gamma_H)+\Gamma_H\cdot\Gamma_R+2(b-2)=0$.
Writing $L=\ell X+mY$, the Hessian minors on $(X,z)$
and $(Y,z)$ are $-\ell^2$ and $-m^2$. At least one
is nonzero because $L\ne0$.'''
new=p.edit(new,oldlast,'All allocations in (4.57b) have been excluded, proving\nthe assertion.',
 'D03,D12,D20,D22','night:P4.57',
 'The equivalent nonnegative genus sum is retained at P323 and the two Hessian minors at their exact rank step. The coefficient m is renamed ell_Y there, distinct from the standing full-fibre multiplicity.')
new=p.clean(new,'night:P4.57')
newunit=r'\subsection{Two distinct conductor junctions}\label{subsec:II:two-conductor-junctions}'+'\n\n'+new+'\n'
p.guard('P457-complete-subsection',oldunit,newunit,
 'Complete old/current and receiving P457 subsection comparison, retaining all Hessian, graph, cubic-content, three allocation and irreducible-factor arguments. Shared genus and quadratic-normalization proofs are exact earlier applications.')

old20=block(s,'night:P4R.20')
a=old20.index(r'\item Let $E=N_{A/Y}^*$')
b=old20.index(r'\par\medskip\noindent\textbf{The exact graph when $c\ge2$.}',a)
old20para=old20[a:b]
new20para=r'''\item Let $E=N_{A/Y}^*$, so $\deg E=2$ by
adjunction and $c_1(Y)\cdot A=0$. The line
$\OO_Y(S)|_A$ has degree zero and is trivial on
$A\simeq\PP^1$. Thus the normal cubic is a section
of $\operatorname{Sym}^3E$. Its derivative maps in
\cref{night:P4.55} identify this same $H$ with the
normalization of $\Gamma_H$ and the rational third
sheet with the section $\Gamma_R$. Let $b$ be the
degree of its common zero divisor. Apply
\cref{lem:II:cubic-spectral-genus} with $e=2$ and
these residual components. With its integer $t$,
$\Gamma_R=\xi-tF$ and $\Gamma_H=2\xi+(t-b)F$;
its $\delta_H$ is the normalization colength, and
$n=\Gamma_H\cdot\Gamma_R$. Formula
\eqref{eq:one-junction-spectral-bound} gives $b\le2$
because $g(H)\ge1$.

'''
new20=old20.replace(old20para,new20para)
p.guard('R20-spectral-genus-application',old20para,new20para,
 'Bounded application only, after complete old/current and receiving proof comparison. Preserve the exact E,q,H direction maps, residual classes and t,delta,n; move the duplicated R20.1 calculation with its label to P323. Whole R20 unit pass remains separate.')
p.record('D12,D14,D17,D20','night:P4R.20',old20para,new20para,
 'Apply the same P323 e=2 formula and b<=2 consequence; every subsequent graph, coefficient and normalization argument keeps its original variables and equation reference.')
p.write(newunit)
for key,text in [('P323',owner),('P455',new55),('R20',new20)]:
    (OUT/f'S6_SERIES_PUBLISH_II_sec07_two_junctions_{key}.tex').write_text(text+'\n',newline='\n')
