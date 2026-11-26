from S6_SERIES_PUBLISH_c3_edit import *

s=SOURCE.read_text()
def block(label,kind='proposition'):
    i=s.index('\\label{'+label+'}',s.index('\\begin{document}'))
    a=s.rfind('\\begin{'+kind+'}',0,i)
    b=s.index('\\end{proof}',i)+len('\\end{proof}')
    return s[a:b]
r3=block('night:P4R.3');r7=block('night:P4R.7');r9=block('night:P4R.9');e22=block('night:P4.22')
plane=block('lem:II:plane-branch-conductor','lemma')
assert 'tag-P252' not in s
lemma=r'''\begin{lemma}[Numerically anticanonical boundaries on irrational ruled surfaces]\hypertarget{tag-P252}{}\label{lem:II:irrational-ruled-boundary}
\StatementRecord{lem:II:irrational-ruled-boundary}{proved}{P252}{\cref{lem:II:canonical-boundary-blowup,lem:II:boundary-blowup-groups}; \cite[III.10, p.~40; III.18, pp.~46--47]{Beauville1978}}
Let $r_0:T_0\to B$ be a minimal ruled surface over a smooth compact curve of genus $g\ge1$, let $\beta:T\to T_0$ be a sequence of point blowups, and let $D$ be an effective integral divisor with $K_T+D\equiv0$. Put $D_0=\beta_*D$ and $A=D_{\rm red}$.

The horizontal part of $D_0$ has ruling degree two, counted with coefficients. Its reduced case has $g=1$: $D_0$ is one smooth elliptic bisection or two disjoint smooth elliptic sections, unramified over $B$. It has no vertical component, and $A$ consists of their disjoint strict transforms, without any blowup-exceptional component.

The other case is
\[
 D_0=2H+\sum_j a_jF_j,\qquad a_j>0,
\]
where $H$ is a smooth section and the $F_j$ are distinct ruling fibres. Here $A$ is the strict transform of $H$ with trees of smooth rational curves attached, with only ordinary double intersections. Inclusion $j:A\hookrightarrow T$ induces an isomorphism on fundamental groups. This isomorphism commutes with the maps induced by each blowdown and with the section and ruling maps on $T_0$.
\end{lemma}
\begin{proof}
The projective-bundle and canonical formulas of \cite[III.10, p.~40; III.18, pp.~46--47]{Beauville1978} write $T_0=\mathbb P_B(V)$ and
\[
 h^2=\deg V,\quad hF=1,\quad F^2=0,\qquad
 K_{T_0}=-2h+(\deg V+2g-2)F.
\]
Apply \cref{lem:II:canonical-boundary-blowup} along $\beta$ to $D$ and its successive pushforwards. It gives $K_{T_0}+D_0\equiv0$, hence $D_0F=2$. It also gives exceptional coefficient $\mu-1$ at every reverse blowup, where $\mu$ is the multiplicity of the current divisor. Effectiveness puts every centre on its support.

For an irreducible horizontal component $H_i$ of coefficient one, adjunction gives
\[
 2p_a(H_i)-2=-(D_0-H_i)H_i\le0.
\]
Its normalization maps finitely to $B$, with degree $d\ge1$, so Riemann--Hurwitz gives $2g(H_i^{\rm norm})-2\ge d(2g-2)$. Since $p_a(H_i)\ge g(H_i^{\rm norm})$, these inequalities force $g=1$, $p_a(H_i)=g(H_i^{\rm norm})=1$ and $(D_0-H_i)H_i=0$. Thus $H_i$ is smooth elliptic, its map to $B$ is unramified, and every other horizontal component is disjoint from it. Every vertical fibre meets it positively, so the vertical part vanishes. The degree-two possibilities are exactly the stated bisection or two sections. A reverse blowup at a smooth coefficient-one point has exceptional coefficient zero and leaves its strict transform smooth. This proves the entire reduced case by induction.

Otherwise the horizontal degree two is twice a single degree-one component $H$. Its normalization maps isomorphically to $B$; composing the inverse with the normalization map into $T_0$ gives a section whose closed image is $H$. Hence $H$ is smooth. Every vertical component on $T_0$ is a fibre, giving the displayed divisor. Initially its reduced support is $H$ with transverse rational fibres attached. Under reverse blowup, a smooth point of coefficient at least two adds a rational leaf, a smooth coefficient-one point adds no boundary component, and a node subdivides its edge. Thus only rational trees are attached to the strict transform of $H$.

On $T_0$, the ruling and its section induce inverse maps on fundamental groups because the ruling fibres are simply connected. Attaching the rational fibres to $H$ adds no generators or relations. At every blowup, \cref{lem:II:boundary-blowup-groups} gives the two fundamental-group isomorphisms induced by that same blowdown and makes their square with the boundary inclusion commute. Their composition gives the asserted isomorphism $j_*$ and its precise compatibility.
\end{proof}

'''

# The full plane-conductor owner precedes its earlier ruled and rational applications.
after=s.replace(plane,'',1)
p=after.index('\\label{lem:II:hypersurface-branch-conductor}')
q=after.index('\\end{proof}',p)+len('\\end{proof}')
after=after[:q]+'\n\n'+plane+after[q:]

# R3 retains its strict-positivity conclusion and its exact smooth/high-genus domain.
p=r3.index('Let $\\pi:T\\to T_0$')
q=r3.index('\\item The normalization $\\nu:T\\to S$',p)
oldr3=r3[p:q]
newr3=r'''Let $\beta:T\to T_0$ contract the ruling blowups, and put $D_0=\beta_*D$. Apply \cref{lem:II:irrational-ruled-boundary} with these same $T,T_0,D$ and the ruling base of genus $g\ge2$. The lemma's adjunction and Riemann--Hurwitz inequalities exclude its reduced-horizontal case. Thus $D_0=2H+\sum a_jF_j$, and $D_{\rm red}$ is the section with rational trees. Its inclusion $j:D_{\rm red}\hookrightarrow T$ induces the precise fundamental-group isomorphism given there.

'''
r3new=r3[:p]+newr3+r3[q:]
assert after.count(r3)==1;after=after.replace(r3,lemma+r3new,1)

# One proper-resolution theorem for the two positive ruling-genus ranges.
combined=r'''\begin{proposition}[Euler numbers with an irrational ruled resolution]\hypertarget{tag-02YJ}{}\label{night:P4R.7}\label{stmt:P4R.7}
\StatementRecord{night:P4R.7}{proved}{02YJ}{\cref{lem:II:irrational-ruled-boundary,lem:II:proper-conductor-pushout,lem:II:curve-normalization-graph,night:P4.13,night:P4R.1,night:P4R.6}}
\hypertarget{tag-02YL}{}\label{night:P4R.9}\label{stmt:P4R.9}
\StatementRecord{night:P4R.9}{proved}{02YL}{}
Let $f:Y\to B$ satisfy the torus-fibration hypotheses of \cref{night:P4.12}, and let $mS$ be a fibre with irreducible, reduced, singular support. Write $\nu:N\to S$ for its normalization and $\pi:T\to N$ for its minimal resolution. Suppose that $T$ is birationally ruled over a curve of positive genus. Then $e(S)\ge0$.

Let $D$ be the pole divisor of \cref{night:P4R.6}, let $\beta:T\to T_0$ contract to a minimal ruled model, and put $D_0=\beta_*D$. A reduced horizontal part of $D_0$ makes the ruling genus one and $N$ smooth and minimal, with $e(S)=0$.
\end{proposition}
\begin{proof}
\begin{enumerate}[label=\arabic*.,leftmargin=*]
\item Put $\rho=\nu\circ\pi$, $A=D_{\rm red}$ and $C=\operatorname{Sing}(S)_{\rm red}$. Proposition~\ref{night:P4R.6} gives $K_T+D$ torsion and $A=\rho^{-1}(C)_{\rm red}$. Apply \cref{lem:II:irrational-ruled-boundary} to the identical minimal ruling $T_0$, blowdown sequence $\beta$ and divisor $D$.

\item In its reduced-horizontal case, the ruling genus is one, and $A$ consists of one or two disjoint smooth elliptic strict transforms with coefficient one. Every exceptional curve of $\pi$ belongs to $A$ by \cref{night:P4R.6}. A connected exceptional configuration would therefore be one of these disjoint elliptic components, disjoint from the strict conductor, contrary to the same proposition. Thus $\pi$ is an isomorphism and $N=T$ is smooth. Apply \cref{lem:II:plane-branch-conductor} to each generic reduced transverse plane equation of $S$: coefficient one makes the two branches smooth and transverse. The differential of $T\to S\hookrightarrow Y$ therefore has rank two away from finitely many points. Proposition~\ref{night:P4.15}, on this same smooth elliptic ruled normalization, makes $T$ minimal and gives $e(S)=0$.

\item In the double-section case, the boundary lemma makes $A$ connected and gives an isomorphism $j_*:\pi_1(A)\to\pi_1(T)$ for its inclusion. The image $C$ is connected, and $\rho$ identifies $T\setminus A$ with $S_{\rm reg}$. A triangulation of the analytic pair makes $A\subset T$ a subcomplex \cite[Theorem~2, p.~464]{Lojasiewicz1964}. Apply \cref{lem:II:proper-conductor-pushout} with $(X,Y,A,C,h)=(T,S,A,C,\rho)$, including every exceptional curve of $\pi$. It gives
\[
 \pi_1(S)\simeq\pi_1(T)*_{\pi_1(A)}\pi_1(C)\simeq\pi_1(C).
\]
The last isomorphism is induced by $C\hookrightarrow S$, with inverse equal to the identity on $\pi_1(C)$ and to $(\rho|_A)_*j_*^{-1}$ on $\pi_1(T)$. Proposition~\ref{night:P4R.1} makes this group virtually abelian. Apply \cref{lem:II:curve-normalization-graph} to the same connected curve $C$; it gives $e(C)\ge0$, and its displayed genus and graph formula identifies the equality case. Proposition~\ref{night:P4.13}, applied to this fibre $mS$, gives $e(S_{\rm reg})\ge0$. Thus $e(S)=e(S_{\rm reg})+e(C)\ge0$.
\end{enumerate}
\end{proof}'''
assert after.count(r7)==after.count(r9)==1
after=after.replace(r7,combined,1).replace(r9,'',1)

# The smooth elliptic case applies the same numerical and group owners.
p=e22.index('Push $D$ to the minimal ruled surface')
q=e22.index('The coefficient-one branch conductors',p)
olde22a=e22[p:q]
newe22a=r'''Push $D$ through its ruling blowdowns $\beta:T\to T_0$ to $D_0$ on the minimal elliptic ruled surface. Apply \cref{lem:II:irrational-ruled-boundary} to these same data. Its reduced-horizontal alternative gives one elliptic bisection or two disjoint elliptic sections, no vertical component, and no exceptional component in $D$ after the blowups. '''
e22new=e22[:p]+newe22a+e22[q:]
a=r'''The coefficient-one branch conductors give two smooth
transverse branches at a general point of each image curve:
the sum of the branch exponents is $2\delta$, while
$\delta\ge q-1$ for $q$ branches, so $q=2$ and $\delta=1$.'''
b=r'''Apply \cref{lem:II:plane-branch-conductor} to each generic transverse plane equation of $S$. Its coefficient-one conclusion gives two smooth transverse branches at the general point of each conductor image.'''
assert a in e22new;e22new=e22new.replace(a,b,1)
p=e22new.index('At each point blowup, \\cref{lem:II:canonical-boundary-blowup}')
q=e22new.index('Proposition~\\ref{night:P4R.1} makes this group virtually abelian.',p)
olde22b=e22new[p:q]
newe22b=r'''Apply the double-section alternative of \cref{lem:II:irrational-ruled-boundary} to this same divisor. It makes $D_{\rm red}$ the elliptic section with rational trees and its inclusion $j:D_{\rm red}\hookrightarrow T$ an isomorphism on fundamental groups. The finite normalization identifies the complementary open sets. Thus \cref{lem:II:proper-conductor-pushout}, with $(X,Y,A,C,h)=(T,S,D_{\rm red},C,\nu)$, gives $\pi_1(S)\simeq\pi_1(C)$, with inverse on $\pi_1(T)$ equal to $(\nu|_{D_{\rm red}})_*j_*^{-1}$.
'''
e22new=e22new[:p]+newe22b+e22new[q:]
a=r'''The branch exponent equals
its intrinsic conductor exponent plus the sum of its
intersections with the other branches.'''
b=r'''Apply \cref{lem:II:plane-branch-conductor} to that same transverse plane equation. It identifies the branch exponent with twice the intrinsic delta invariant plus the sum of its intersections with the other branches.'''
assert a in e22new;e22new=e22new.replace(a,b,1)
assert after.count(e22)==1;after=after.replace(e22,e22new,1)
olditem=r'\item \SeriesRef{night:P4R.9}\quad Euler number with an elliptic ruled resolution.'
assert after.count(olditem)==1;after=after.replace(olditem+'\n','',1)
after=after.replace(r'\item \SeriesRef{night:P4R.7}\quad Euler number with a higher-genus ruled resolution.',r'\item \SeriesRef{night:P4R.7}\quad Nonnegative Euler number for an irrational ruled normalization resolution.',1)
# Two surviving references now point to the same theorem; their exact case data stay in prose.
after=after.replace(r'\cref{night:P4R.7,night:P4R.9}',r'\cref{night:P4R.7}')
preserve_identifiers(s,after)
for before,current in zip(identifiers(s),identifiers(after)):
    for name,count in before.items():assert current[name]==count,name
SOURCE.write_text(after,newline='\n')

rows=[]
items=[
 ('NUMERICAL',['D12','D14'],'lem:II:irrational-ruled-boundary; night:P4R.3; night:P4.22',oldr3+'\n'+olde22a+'\n'+olde22b,lemma+'\n'+newr3+'\n'+newe22a+'\n'+newe22b,'The common proof uses only the identical minimal ruled bundle, point-blowup map and effective integral numerically anticanonical divisor. Its reduced case forces g=1 by the written adjunction/Riemann–Hurwitz inequalities; its double case supplies the same section, rational trees and commuting fundamental-group maps. Smooth high-genus strict positivity and smooth elliptic equality arguments remain in their original scope.'),
 ('PROPER',['D12','D14'],'night:P4R.7; night:P4R.9',r7+'\n'+r9,combined,'Union the original g≥2 and g=1 cases on identical f,Y,B,mS,nu,pi,beta,D data. Retain both tags/labels, the complete reduced-horizontal smoothness/minimality conclusion, and the one proper-pushout proof for the double-section case, with every map explicit.'),
 ('PLANE-ORDER',['D12','D14'],'lem:II:plane-branch-conductor; night:P4.22',plane+'\n'+a,plane+'\n'+b,'Move the complete unchanged plane-conductor owner immediately after the common branch-conductor lemma, before its rational/ruled applications. Replace their repeated generic branch calculation by the exact reduced transverse equation application.'),
 ('NAVIGATION',['D12','D24'],'night:P4R.7; night:P4R.9',olditem,r'\item \SeriesRef{night:P4R.7}\quad Nonnegative Euler number for an irrational ruled normalization resolution.','Keep one further-results entry and replace paired references to the same theorem by its one owner label; all single legacy labels still resolve.')]
for key,types,stmt,before,current,reason in items:
    for i,kind in enumerate(types,1):
        rows.append(dict(change_id=f'II-C3-RULED-BOUNDARY-{key}-{i:02}',type=kind,statement_id=stmt,
          old_location='Smooth and resolved irrational ruled normalizations',old_page='working source; final concordance pending',
          new_location='Common numerical boundary owner and exact ruling applications',new_page='integrated build pending',
          old_text=before,new_text=current,reason=reason,
          review_status='Root complete original proofs read; complete receiving comparison follows; no independent credit.'))
print('Defects',append_rows(ROOT/'S6_SERIES_PUBLISH_defects_II.tsv',rows,'change_id'))
for unit in ['night:P4R.3','night:P4.21','night:P4R.7']:
    set_unit_status(unit,'D12','open','Shared ruled-boundary calculation and two proper-resolution cases have been consolidated on identical maps; complete receiving-unit comparison remains pending.','code/S6_SERIES_PUBLISH_c3_ruled_boundary_owner.py')
add_event('lem:II:irrational-ruled-boundary; night:P4R.3; night:P4.22; night:P4R.7; night:P4R.9; lem:II:plane-branch-conductor',
 'II-C3-ROOT-RULED-BOUNDARY-TRANSFER','used and rechecked in this run',
 'Complete original R3,P4.22,R7,R9 and plane-conductor proofs read. P252 collects the same projective-bundle, adjunction, Riemann–Hurwitz, coefficient μ−1, incidence-tree and commuting blowdown-group calculations. The two proper-resolution cases share one statement/proof with both legacy tags. Their old domains map identically into the union g≥1, and every retained stronger conclusion is stated. The smooth-case strict-positivity/equality arguments remain. All old label/target multiplicities are preserved. Full receiving readings follow; no final or independent credit.',
 'S6_SERIES_PUBLISH_II.tex: irrational ruled normalizations',source='code/S6_SERIES_PUBLISH_c3_ruled_boundary_owner.py')
print('Ruled-boundary owner and proper-resolution union admitted; receiving reads pending.')
