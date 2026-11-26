"""One full ruled-equality conductor argument and its exact local-type applications."""
from S6_SERIES_PUBLISH_c3_edit import *

s=SOURCE.read_text()
def block(label,kind='proposition'):
    i=s.index('\\label{'+label+'}',s.index('\\begin{document}'))
    a=s.rfind('\\begin{'+kind+'}',0,i)
    b=s.index('\\end{proof}',i)+len('\\end{proof}')
    return s[a:b]
p29=block('night:P4.29');p31=block('night:P4.31');p32=block('night:P4.32')
p33=block('night:P4.33');r10=block('night:P4R.10');r11=block('night:P4R.11')
assert 'tag-P253' not in s

# Make the already-proved scheme and ruling maps available in the statement.
p33new=p33
old=r'''For the scheme-theoretic image conductor $C_{\rm sch}$ we have
\[
 \chi(\mathcal O_{C_{\rm sch}})
   =-\chi(\mathcal O_N)=h^1(N,\mathcal O_N)-1.
\]'''
new=r'''Let $C_{\rm sch}\subset S$ and $D_{\rm sch}\subset N$ be the image and inverse-image conductor schemes. The nonempty $C_{\rm sch}$ is Cohen--Macaulay of pure dimension one, and
\[
 \chi(\mathcal O_{D_{\rm sch}})=0,\qquad
 \chi(\mathcal O_{C_{\rm sch}})
   =-\chi(\mathcal O_N)=h^1(N,\mathcal O_N)-1.
\]'''
assert p33new.count(old)==1;p33new=p33new.replace(old,new,1)
old=r'''A noncontracted $H$ gives $p=0$ and
$h^1(N,\mathcal O_N)=g$.'''
new=r'''For a noncontracted $H$, write $a:T\to E$ for the ruling and $h:E\simeq H\hookrightarrow T$ for the section. There is a holomorphic map $q:N\to E$ and a section $s=\rho_N\circ h$ satisfying
\[
 q\circ\rho_N=a,\qquad q\circ s=\operatorname{id}_E.
\]
Here $p=0$, $R^1\rho_{N*}\mathcal O_T=0$, and $h^1(N,\mathcal O_N)=g$.'''
assert p33new.count(old)==1;p33new=p33new.replace(old,new,1)
a=p33new.index('\\item Write $I_S=');b=p33new.index('The dualizing line bundle',a)
oldduality=p33new[a:b]
newduality=r'''\item Apply \cref{lem:II:conductor-duality} to the finite normalization $\eta=\nu:N\to S$. The hypersurface $S\subset Y$ is Gorenstein, and the normal surface $N$ is Cohen--Macaulay. The lemma identifies the conductor $I_S$ with $\mathcal Hom_{\mathcal O_S}(\nu_*\mathcal O_N,\mathcal O_S)$ by evaluation at $1$, whose inverse is multiplication by that value. Its finite-duality map and the projection formula give
\[
 \nu_*\omega_N=I_S\otimes\omega_S.
\]
It also makes the image conductor scheme $C_{\rm sch}$ Cohen--Macaulay of pure dimension one.
'''
p33new=p33new[:a]+newduality+p33new[b:]
old=r'''$h^1(N,\mathcal O_N)=g$ and $p=0$.'''
new=r'''$h^1(N,\mathcal O_N)=g$ and $p=0$. The sheaf $R^1\rho_{N*}\mathcal O_T$ has finite support, so its zero space of global sections makes the sheaf itself zero.'''
assert p33new.count(old)==1;p33new=p33new.replace(old,new,1)

lemma=r'''\subsection{Conductor curves at ruled Euler equality}\label{subsec:II:zero-euler-ruled-conductor}

\begin{lemma}[Conductor curves of ruled supports with Euler number zero]\hypertarget{tag-P253}{}\label{lem:II:zero-euler-ruled-conductor}
\StatementRecord{lem:II:zero-euler-ruled-conductor}{proved}{P253}{\cref{lem:II:irrational-ruled-boundary,lem:II:proper-conductor-pushout,lem:II:curve-normalization-graph,lem:II:plane-branch-conductor,night:P4.13,night:P4R.1,night:P4R.6,night:P4.33}}
Let $f:Y\to B$ satisfy the torus-fibration hypotheses of \cref{night:P4.12}, and let $mS$ be a fibre with irreducible, reduced, singular support and $e(S)=0$. Write $\nu:N\to S$ for its normalization, $\pi:T\to N$ for its minimal resolution, $\rho=\nu\circ\pi$, and $D$ for the pole divisor of \cref{night:P4R.6}. Let $\beta:T\to T_0$ contract to a minimal ruled surface over a smooth curve $B_0$ of genus $g\ge1$. Suppose the horizontal part of $D_0=\beta_*D$ is $2H_0$, where $H_0$ is a section. Put
\[
 A=D_{\rm red},\qquad C=\operatorname{Sing}(S)_{\rm red},
\]
and let $H\subset T$ be the strict transform of $H_0$.

The curve $C$ is irreducible, has elliptic normalization $\eta_C:E\to C$, and is unibranch at every point. Every rational component of $A$ is contracted by $\pi$, and $H$ is the sole strict conductor component. The ruling $r:T\to B_0$ descends to $r_N:N\to B_0$. With $h:B_0\simeq H\hookrightarrow T$ and $s=\pi\circ h$ one has
\[
 r_N\circ\pi=r,\qquad r_N\circ s=\operatorname{id}_{B_0},
 \qquad (\nu^{-1}C)_{\rm red}=s(B_0).
\]
In particular $s$ is a closed holomorphic embedding. The finite map $\nu\circ s:B_0\to C$ factors uniquely through $\eta_C$.

All singularities of $N$ are rational, and
\[
 h^1(N,\mathcal O_N)=g,\qquad
 \chi(\mathcal O_{C_{\rm sch}})=g-1,\qquad
 \chi(\mathcal O_{D_{\rm sch}})=0,
\]
where $C_{\rm sch}$ and $D_{\rm sch}$ are the conductor schemes on $S$ and $N$. The image scheme $C_{\rm sch}$ is Cohen--Macaulay of pure dimension one. The generic transverse germ along $C$ is a cusp, a tacnode or an ordinary plane triple point. The degree of $B_0\to E$ is respectively one, two or three.
\end{lemma}
\begin{proof}
\begin{enumerate}[label=\arabic*.,leftmargin=*]
\item Apply \cref{lem:II:irrational-ruled-boundary} to the identical data $(T,T_0,\beta,D)$. It makes $A$ the section $H$ with rational trees attached and identifies the map on fundamental groups induced by $j:A\hookrightarrow T$. Proposition~\ref{night:P4R.6} gives $A=\rho^{-1}(C)_{\rm red}$, and $\rho$ identifies the complementary smooth loci. A compatible analytic triangulation makes $A\subset T$ a subcomplex. Apply \cref{lem:II:proper-conductor-pushout} with $(X,Y,A,C,h)=(T,S,A,C,\rho)$. The connected image $C$ satisfies
\[
 \pi_1(S)\simeq\pi_1(T)*_{\pi_1(A)}\pi_1(C)\simeq\pi_1(C).
\]
The final isomorphism is induced by $C\hookrightarrow S$; its inverse is the identity on $\pi_1(C)$ and $(\rho|_A)_*j_*^{-1}$ on $\pi_1(T)$. Proposition~\ref{night:P4R.1}, applied to the same full fibre $mS$, makes this group virtually abelian.

\item Apply \cref{lem:II:curve-normalization-graph} to this connected curve $C$. With $c$ components, normalization genera $g_i$ and incidence-graph cycle rank $b$, it gives
\[
 \pi_1(C)=\bigl(*_i\pi_1(C_i^{\rm norm})\bigr)*F_b,
 \qquad e(C)=c+1-2\sum_i g_i-b\ge0.
\]
Proposition~\ref{night:P4.13} gives $e(S_{\rm reg})\ge0$, so $e(S)=0$ makes $e(C)=0$. In the all-rational alternative of the graph lemma, $b\le1$ and $e(C)\ge c\ge1$. Its other alternative has one elliptic normalization, $b=0$, and $e(C)=c-1$. Thus $c=1$ and the normalization $E$ is elliptic. For one component the same graph has $b=\sum_p(r_p-1)$, where $r_p$ counts the normalized preimages of $p$. Hence every point of $C$ is unibranch.

\item A nonconstant map from a normalized rational component of $A$ to $C$ would lift through the normalization $\eta_C:E\to C$. Its resulting finite map $\mathbb P^1\to E$ contradicts Riemann--Hurwitz. Every rational component of $A$ is therefore contracted by $\rho$ and, since $\nu$ is finite, by $\pi$. Surjectivity onto the curve $C$ makes $H$ noncontracted and the sole strict conductor component. Its map to $C$ is finite and factors uniquely through $E$.

The section and vertical trees now satisfy the noncontracted clause of \cref{night:P4.33}, with its $(E,a,h,q,s,\rho_N)$ equal to $(B_0,r,h,r_N,s,\pi)$ here. That clause supplies the displayed ruling identities, rationality of all normalization singularities, and $h^1(N,\mathcal O_N)=g$. The same proposition supplies the two conductor Euler characteristics and the Cohen--Macaulay image scheme. The identity $r_Ns=\operatorname{id}_{B_0}$ makes $s$ a closed holomorphic embedding: $s$ is proper and its local restriction map $s^*$ is surjective, with right inverse $r_N^*$. Every connected exceptional configuration of $\pi$ meets the strict conductor by \cref{night:P4R.6}; since the strict conductor is $H$, each exceptional image lies on $s(B_0)$. This proves $(\nu^{-1}C)_{\rm red}=s(B_0)$.

\item The strict-transform coefficient of $H$ in $D$ is two, the coefficient of $H_0$ in $D_0$. At every general point of $C$, all its normalized transverse branches are the points of this same $H$, so all their conductor exponents are two. Apply \cref{lem:II:plane-branch-conductor} to the reduced transverse equation $F=\prod_iF_i$ at that point. For every branch it gives
\[
 2=2\delta(F_i)+\sum_{j\ne i}I(F_i,F_j).
\]
A singular branch therefore has delta invariant one and is the only branch. Its conductor is $t^2\mathbb C\{t\}$. Its ring has no element with nonzero linear term in $t$, since the inverse function theorem would make such an element a local parameter and make the branch smooth. Thus its ring is exactly
\[
 \mathbb C+t^2\mathbb C\{t\}
   =\mathbb C\{t^2,t^3\}
   \simeq\mathbb C\{X,Y\}/(Y^2-X^3),
\]
where the last map sends $(X,Y)$ to $(t^2,t^3)$. Lifting these two generators from the maximal ideal modulo its square to the transverse plane gives an invertible cotangent map, hence ambient holomorphic coordinates. This is the cusp germ.

For smooth branches the formula leaves two branches of intersection multiplicity two, or three with all pairwise intersections one. In the first case write them as $y=0$ and $y=x^2u(x)$, with $u(0)\ne0$. The coordinates $X=x\sqrt{u(x)}$, $Y=2y-X^2$ carry their reduced union to $Y^2-X^4=0$; the inverse uses the inverse of $x\mapsto x\sqrt{u(x)}$ and $y=(Y+X^2)/2$. In the second case write two as $x=0,y=0$ and the third as $y=xu(x)$, $u(0)\ne0$. The coordinates $X=xu(x)$, $Y=y$, with inverse given by the one-variable inverse of $x\mapsto xu(x)$, carry the union to $XY(Y-X)=0$. Four branches would give an intersection sum at least three; a sole smooth branch has conductor exponent zero. These cases exhaust the formula. The generic number of transverse normalization branches is the degree of $H\to C$, hence the degree of $B_0\to E$, giving one, two or three as asserted.
\end{enumerate}
\end{proof}

'''

# The cusp proof uses the exact common topological/cohomological data.
a=p29.index('\\begin{proof}');b=p29.index('\\end{proof}')+len('\\end{proof}')
p29new=p29[:a]+r'''\begin{proof}
\begin{enumerate}[label=\arabic*.,leftmargin=*]
\item Write $\nu:N\to S$, $\pi:T\to N$ and $\rho=\nu\circ\pi$. Proposition~\ref{night:P4.26} excludes a rational resolution from $e(S)=0$, so the ruling base has genus $g\ge1$. Apply \cref{lem:II:zero-euler-ruled-conductor} to this same full fibre, normalization resolution and double horizontal pole divisor. Its notation gives the sole strict conductor $H$, the irreducible image $C$ with elliptic normalization $E$, and the descended ruling and section.

The generic cusp has normalization $v\mapsto(v^3,-v^2)$ and one branch. Thus the finite map $H\to E$ has degree one. A finite degree-one map between these smooth compact curves is an isomorphism, so $g=1$. The common lemma gives $\chi(\mathcal O_{C_{\rm sch}})=0$ and makes $C_{\rm sch}$ Cohen--Macaulay of pure dimension one.

\item At a generic cusp, the conductor is $v^2\mathbb C\{v\}$, the image of $(x,y)$ under $x=v^3,y=-v^2$. Hence the image conductor scheme is generically the reduced curve $C$. Its nilradical is supported at finitely many points and vanishes by the depth-one property. Therefore $C_{\rm sch}=C$ at every point, including images of exceptional curves.

The normalization sequence for $\eta_C:E\to C$ gives
\[
 0=\chi(\mathcal O_C)=\chi(\mathcal O_E)-\sum_p\delta(C,p)
   =-\sum_p\delta(C,p).
\]
Every delta invariant is zero, so $C$ is smooth.

\item Apply \cref{night:P4.28} at every point of this smooth reduced singular curve, with the same local reduced equation of $S$ and generic cusp germ. Its product coordinates give normalization
\[
 (t,v)\longmapsto(t,v^3,-v^2)
\]
and identify the reduced conductor $v=0$ with $C$. Thus $N$ is smooth along $C$ and equals $S_{\rm reg}$ away from it. Proposition~\ref{night:P4.22}, applied to this same smooth elliptic ruled normalization with $e(S)=0$, makes it minimal.
\end{enumerate}
\end{proof}'''+p29[b:]
p29new=p29new.replace(r'\StatementRecord{night:P4.29}{proved}{02X1}{}',r'\StatementRecord{night:P4.29}{proved}{02X1}{\cref{lem:II:zero-euler-ruled-conductor,night:P4.28,night:P4.22}}',1)

# Retain the full triple-conductor ideal and local-branch proofs.
a=p31.index('\\item Write $\\nu:N\\to S$');b=p31.index('\\item Let $I_S$ and $I_N$',a)
old31setup=p31[a:b]
new31setup=r'''\item Write $\nu:N\to S$, $\pi:T\to N$ and $\rho=\nu\circ\pi$. Proposition~\ref{night:P4.26} excludes rational resolution at Euler number zero. Apply \cref{lem:II:zero-euler-ruled-conductor} to this same positive-genus ruling and double horizontal pole divisor. It gives the irreducible, everywhere unibranch image curve $C$ with elliptic normalization $E$, the sole strict conductor $H$ of genus $g\ge1$, and the ruling maps $r_N,s$ satisfying $r_Ns=\operatorname{id}$. The generic ordinary triple point has three normalization branches, so the finite map $H\to E$ has degree three. The lemma also gives rational normalization singularities and
\[
 \chi(\mathcal O_{C_{\rm sch}})=g-1.
\]
'''
p31new=p31[:a]+new31setup+p31[b:]
old=r'''The finite-duality and depth
argument in \cref{night:P4.29} makes
$\mathcal O_{C_{\rm sch}}$ Cohen--Macaulay of
pure dimension one.'''
new=r'''The conductor clause of \cref{lem:II:zero-euler-ruled-conductor}, applied to this same $\nu$, makes $\mathcal O_{C_{\rm sch}}$ Cohen--Macaulay of pure dimension one.'''
assert p31new.count(old)==1;p31new=p31new.replace(old,new,1)
a=p31new.index('\\item Put $L=\\nu^*\\omega_S$');b=p31new.index('Proposition~\\ref{night:P4.30} applies',a)
old31chi=p31new[a:b]
p31new=p31new[:a]+r'''\item The conductor Euler characteristic from the first step is $\chi(\mathcal O_{C_{\rm sch}})=g-1$ for this same scheme, now identified with $\mathcal O_Y/P^{(2)}$.
'''+p31new[b:]
old=r'''the section identity
$\bar r\pi h=\operatorname{id}_H$ makes $\pi|_H$
injective.'''
new=r'''the section identity $r_N\pi h=\operatorname{id}_{B_0}$ in \cref{lem:II:zero-euler-ruled-conductor} makes $\pi|_H$ a closed embedding.'''
assert p31new.count(old)==1;p31new=p31new.replace(old,new,1)
p31new=p31new.replace(r'\StatementRecord{night:P4.31}{proved}{02X4}{}',r'\StatementRecord{night:P4.31}{proved}{02X4}{\cref{lem:II:zero-euler-ruled-conductor,night:P4.30,night:P4.22}}',1)

# The Hessian argument needs only the common CM conductor lemma.
old=r'''The conductor depth argument of \cref{night:P4.29} gives a
Cohen--Macaulay quotient $\mathcal O_Y/I$ of pure dimension one.'''
new=r'''Apply \cref{lem:II:conductor-duality} to the finite normalization of this reduced hypersurface $S$. Its image conductor scheme has structure sheaf $\mathcal O_Y/I$, which the lemma makes Cohen--Macaulay of pure dimension one.'''
assert r10.count(old)==1;r10new=r10.replace(old,new,1)
r10new=r10new.replace(r'\SeriesRef{night:P4.29}, \SeriesRef{night:P4.30}',r'\SeriesRef{lem:II:conductor-duality}, \SeriesRef{night:P4.30}',1)

# The tacnode proof retains every local analytic factorization step.
r11new=r11.replace('an irreducible singular support in Part~4.2','an irreducible singular support in \\cref{def:II:standing-torus-fibration}',1)
a=r11new.index('\\item Use $T\\to N\\to S$');b=r11new.index('\\item We verify the local analytic conclusion.',a)
old11setup=r11new[a:b]
new11setup=r'''\item Write $\nu:N\to S$ and $\pi:T\to N$ for normalization and its minimal resolution. Proposition~\ref{night:P4.26} excludes rational resolution. Apply \cref{lem:II:zero-euler-ruled-conductor} to this same positive-genus ruling and double horizontal pole divisor. It supplies the sole strict conductor $H$ of genus $g\ge1$, the irreducible unibranch image $C$ with elliptic normalization, and the descended ruling $r_N:N\to B_0$ with section $s=\pi h$. Its conductor-scheme equality is
\[
 \chi(\mathcal O_{C_{\rm sch}})=g-1.
\]
Apply \cref{night:P4R.10} to this same $S\subset Y$ and $C$, whose generic transverse germ is the stated tacnode. It gives $g-1\le0$. Thus $g=1$ and equality holds; the same proposition makes $C$ smooth and gives rank one for the reduced equation's transverse Hessian everywhere on $C$. The finite map $H\to C$ has degree two, the generic number of normalization branches. Riemann--Hurwitz between the two elliptic curves makes it unramified.

'''
r11new=r11new[:a]+new11setup+r11new[b:]
r11new=r11new.replace('by P4R.6.','by \\cref{night:P4R.6}.').replace('and P4.22 makes','and \\cref{night:P4.22} makes')
r11new=r11new.replace(r'\StatementRecord{night:P4R.11}{proved}{02Y4}{\SeriesRef{night:P4.12}, \SeriesRef{night:P4.22}, \SeriesRef{night:P4.29}, \SeriesRef{night:P4R.10}, \SeriesRef{night:P4R.6}, \SeriesRef{night:P4R.9}}',r'\StatementRecord{night:P4R.11}{proved}{02Y4}{\cref{lem:II:zero-euler-ruled-conductor,night:P4R.10,night:P4.22}}',1)

# Keep the entire zero-Euler classification statement and use its earlier owners.
a=p32.index('\\begin{proof}');b=p32.index('\\end{proof}')+len('\\end{proof}')
p32new=p32[:a]+r'''\begin{proof}
\begin{enumerate}[label=\arabic*.,leftmargin=*]
\item Proposition~\ref{night:P4.12} makes every normal irreducible support smooth. Apply the cyclic base-change construction in the proof of \cref{night:P4.8} to this full fibre $mS$. Its local map is $t=uz^m=w^m$ with $w=u^{1/m}z$, followed by $t=s^m$ and the normalized charts $w=\zeta s$. The resulting finite unramified central cover $S'\to S$ is a torus by the torus-deformation theorem applied there to this proper submersion. Thus $e(S)=e(S')/\deg(S'\to S)=0$. This equality also proves the converse for a support with any finite unramified torus cover.

For singular $S$, write $\nu:N\to S$ and $\pi:T\to N$ for normalization and its minimal resolution. Proposition~\ref{night:P4.12} gives $\kappa(T)=-\infty$, so \cref{lem:II:negative-kodaira-models} applies to a minimal model. Proposition~\ref{night:P4.26} excludes a rational resolution from $e(S)=0$. On a class-VII resolution, \cref{night:P4.37}, applied to these same $\nu,\pi$ and full fibre, makes $N$ a smooth minimal Hopf surface. Conversely \cref{night:P4.36} gives $e(S)=0$ on every such Hopf normalization.

\item The remaining resolution is ruled over a curve of genus $g\ge1$. Let $D$ be its pole divisor and $D_0$ its pushforward to the minimal ruling. Apply \cref{lem:II:irrational-ruled-boundary} to these same data. Its reduced-horizontal alternative has $g=1$, and \cref{night:P4R.7} makes $N$ smooth and minimal with $e(S)=0$.

In the double-horizontal alternative, apply \cref{lem:II:zero-euler-ruled-conductor} to the identical $mS,\nu,\pi,D$ and ruling. It gives the irreducible image curve $C$ with elliptic normalization, the noncontracted section $H$ as the sole strict conductor, and the complete list of generic transverse cusp, tacnode and ordinary-triple germs, with degrees one, two and three. Every exceptional component remains included in the resolved pole divisor used by that lemma.

\item Propositions~\ref{night:P4.29}, \ref{night:P4R.11} and~\ref{night:P4.31} apply, respectively, to these three transverse germs on this same support. They make $N$ smooth minimal elliptic ruled, $C$ smooth elliptic, and every local germ a product with a disc. Their degree-one, degree-two and degree-three reduced conductor maps are respectively an isomorphism and the two stated unramified coverings. Conversely \cref{night:P4.22}, on any smooth minimal elliptic ruled normalization in the original setting, gives $e(S)=0$. This proves both directions of the irreducible classification.

\item The Euler-additivity calculation in the proof of \cref{night:P4.26}, for this same $f:Y\to B$, writes $c_3(Y)=e(Y)$ as the finite sum of exceptional reduced-support Euler numbers. Propositions~\ref{night:P4.26} and~\ref{night:P4.6} make every summand nonnegative. The sum is zero precisely when each summand is zero. The irreducible summands have just been classified. For a reducible normal-crossing support, apply the single-support component calculation in the proof of \cref{night:P4.8} to that divisor in this same $Y$: zero triple points give minimal Hopf or non-K\"ahler elliptic normalization components with smooth elliptic double curves and unramified branch maps. Conversely this form has Euler number zero by \cref{night:P4.6}. This proves the final assertion.
\end{enumerate}
\end{proof}'''+p32[b:]
p32new=p32new.replace(r'\StatementRecord{night:P4.32}{proved}{02X5}{}',r'\StatementRecord{night:P4.32}{proved}{02X5}{\cref{lem:II:zero-euler-ruled-conductor,night:P4.26,night:P4.29,night:P4R.11,night:P4.31,night:P4.37,night:P4.36}}',1)

after=s
for old,new in [(p33,p33new),(p29,p29new),(p31,p31new),(r10,r10new),(r11,r11new),(p32,p32new)]:
    assert after.count(old)==1;after=after.replace(old,new,1)
anchor=r'\subsection{Cuspidal equality on a ruled normalization}'
assert after.count(anchor)==1;after=after.replace(anchor,lemma+anchor,1)
oldheading=r'\subsection{Complete zero-Euler classification in the requested classes}'
newheading=r'\subsection{Zero-Euler fibre supports}'
assert after.count(oldheading)==1;after=after.replace(oldheading,newheading,1)
preserve_identifiers(s,after)
for before,current in zip(identifiers(s),identifiers(after)):
    for name,count in before.items():assert current[name]==count,name
SOURCE.write_text(after,newline='\n')

records=[
 ('COHOMOLOGY',['D12','D18','D22'],'night:P4.33',p33,p33new,'Expose the already-proved conductor scheme, vanishing higher image, ruling descent and section identities in the statement. Apply the existing conductor-duality owner to the identical finite normalization instead of repeating its local duality proof; retain all cohomology, Leray and Euler calculations.'),
 ('EQUALITY',['D12','D14','D22'],'lem:II:zero-euler-ruled-conductor',p29+'\n'+p31+'\n'+p32,lemma,'The exact common domain is the same irreducible full fibre with e(S)=0 and double horizontal pole section over positive genus. The proper pushout, graph equality, rational-component contraction, noncontracted ruling and conductor Euler calculations are proved once with every map identified. The complete exponent-two transverse enumeration is transferred from P4.32 and applies the already-proved branch-conductor formula.'),
 ('CUSP',['D12','D18','D22'],'night:P4.29',p29,p29new,'Keep the full original cusp-equality statement. The earlier common lemma supplies precisely its original T,N,S,D,H,C maps, CM conductor and Euler equality. Retain the cusp conductor ideal, finite-support nilradical argument, delta calculation, complete product normalization and minimality endpoint. Replace the old smooth/high-genus R3 pointer by the applicable R1 full-fibre group result inside the common owner.'),
 ('TRIPLE',['D12','D22'],'night:P4.31',p31,p31new,'Keep the full original statement and complete transverse conductor ideal, symbolic square, conormal inequality, local normal-branch regularity, coordinate inverses and minimality proof. The preceding common owner supplies only the identical topology, ruling and conductor Euler quantities, with its section identity explicitly matched.'),
 ('HESSIAN',['D12','D18','D22'],'night:P4R.10',r10,r10new,'The same full Hessian and conormal-colength proof remains. Its conductor depth assertion applies P222 to the exact finite normalization, replacing a pointer into the cusp specialization.'),
 ('TACNODE',['D04','D12','D22'],'night:P4R.11',r11,r11new,'Keep the original zero-Euler tacnode domain, replacing its run-coded standing-setting pointer. Use the common exact conductor maps and Euler identity; retain the Hessian equality application, finite covering degree and all local analytic factorization/unit-coordinate steps.'),
 ('CLASSIFICATION',['D12','D18','D22'],'night:P4.32',p32,p32new,'The full classification statement is unchanged. Every normal, rational, class-VII and ruled case applies its preceding owner on identical maps. The complete generic transverse enumeration has one owner P253; every local specialization and converse remains, and the global equality uses the same nonnegative support sum.'),
 ('TITLE',['D01','D24'],'night:P4.32',oldheading,newheading,'Replace the production-scope heading by the mathematical classification it contains.')]
rows=[]
for key,kinds,stmt,old,new,reason in records:
    for i,kind in enumerate(kinds,1):
        rows.append(dict(change_id=f'II-C3-RULED-EQUALITY-{key}-{i:02}',type=kind,statement_id=stmt,
          old_location='Ruled equality, normalization cohomology and local transverse cases',old_page='working source; final concordance pending',
          new_location='Common zero-Euler conductor owner and exact local-type applications',new_page='integrated build pending',
          old_text=old,new_text=new,reason=reason,
          review_status='Root read every complete original proof and all common input owners; complete receiving comparison follows. No independent credit.'))
print('Defects',append_rows(ROOT/'S6_SERIES_PUBLISH_defects_II.tsv',rows,'change_id'))
path=ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv';fields,progress=read_tsv(path)
for row in progress:
    if row['paper']=='II' and row['unit_id']=='night:P4.33':row['unit_title']='Normalization cohomology and conductor schemes'
    if row['paper']=='II' and row['unit_id']=='night:P4.32':row['unit_title']='Zero-Euler fibre supports'
unit='subsec:II:zero-euler-ruled-conductor'
assert not any(row['paper']=='II' and row['unit_id']==unit for row in progress)
for kind in [f'D{i:02}' for i in range(1,26)]+['structure']:
    progress.append(dict(paper='II',unit_id=unit,unit_title='Conductor curves at ruled Euler equality',
      row_kind='structure' if kind=='structure' else 'defect',defect_type='' if kind=='structure' else kind,
      status='done' if kind in ['D10','D16'] else 'open',date_utc=now(),evidence='code/S6_SERIES_PUBLISH_c3_ruled_equality_owner.py',
      detail='Transferred exact original proofs from P4.29/P4.31/P4.32 into one preceding owner. Complete receiving reading pending; unit creation earns no movement credit.'))
write_tsv(path,fields,progress)
for unit in ['night:P4.33','night:P4.29','night:P4.30','night:P4R.10','night:P4.32']:
    set_unit_status(unit,'D12','open','Common ruled-equality conductor owner admitted; complete receiving-unit comparison pending.','code/S6_SERIES_PUBLISH_c3_ruled_equality_owner.py')
add_event('night:P4.33; lem:II:zero-euler-ruled-conductor; night:P4.29; night:P4.31; night:P4R.10; night:P4R.11; night:P4.32',
 'II-C3-ROOT-RULED-EQUALITY-TRANSFER','used and rechecked in this run',
 'Root read all complete original proofs and the common P222/P282/P252/R7/P433 input owners. The common topology, noncontracted ruling, CM conductor, cohomology and transverse enumeration are now earlier P253 on the exact same maps. P4.33 exposes only conclusions and maps already proved in its full proof. Every old label/target multiplicity remains. Complete receiving-unit comparison is next; no independent or final credit.',
 'S6_SERIES_PUBLISH_II.tex: ruled equality and conductor schemes',source='code/S6_SERIES_PUBLISH_c3_ruled_equality_owner.py')
print('Admitted P253 and exact ruled-equality applications; receiving readings pending.')
