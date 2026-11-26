"""Prepare exact P339 applications for P336 and the complete UN6 receiver."""
from S6_SERIES_PUBLISH_c3_edit import *
import json

folder=ROOT/'agents/continuation3_occurrence_root'
prefix='S6_SERIES_PUBLISH_c3_root_ambient_'
text=SOURCE.read_text()
start=text.index('\\subsection{Signed root fibrations}')
end=text.index('\\subsection{Elliptic root fillings}',start)
p339=text[start:end]
start=text.index('\\begin{lemma}[An elliptic root surface and its distinguished fibre]')
end=text.index('\\end{proof}',start)+len('\\end{proof}')
p336=text[start:end]
start=text.index('\\begin{proposition}[Zero-Euler product fillings with essential Kodaira-dimension-one components]')
end=text.index('\\end{proof}',start)+len('\\end{proof}')
un6=text[start:end]
new339=p339
for label,alias,tag in [('C.PE.5','C.ER.4','00IZ'),('C.PE.7','C.ER.5','00J0'),('C.PE.8','C.ER.7','00J2'),('C.PE.9','C.ER.8','00J3')]:
    needle='\\label{cdp:eq:'+label+'}'
    assert new339.count(needle)==1
    new339=new339.replace(needle,needle+'\n \\hypertarget{tag-'+tag+'}{}\\SsixEquationAliases{\\label{cdp:eq:'+alias+'}}',1)
oldchart='In the positive chart put $x=z^m$, $b=w^m$ and $a=z/w$.\n'
newchart=r'''In the positive chart the coordinate map is
\begin{equation}
 (z,w,y)\longmapsto(x=z^m,y;\ b=w^m,\ a=z/w),
 \qquad w\in\C^*.
 \hypertarget{tag-00J1}{}\label{cdp:eq:C.ER.6}
\end{equation}
'''
assert new339.count(oldchart)==1
new339=new339.replace(oldchart,newchart,1)
start=p336.index('Choose a coordinate $x$ at $0$')
end=p336.index('Choose a nowhere-zero holomorphic one-form',start)
newintro=r'''Apply \cref{lem:II:signed-root-fibration} to
$V=B\times\Delta$, $D_+=\{0\}\times\Delta$, $D_-=\varnothing$,
the line $\operatorname{pr}_B^*L$ and section
$\operatorname{pr}_B^*\sigma$, with its $(m,q)=(m,\beta)$.
The positive chart is defined on all of $V$. The maps
\[
 [(v,y,\ell,a)]\longmapsto([(v,\ell,a)],y),\qquad
 ([(v,\ell,a)],y)\longmapsto[(v,y,\ell,a)]
\]
are inverse holomorphic maps between that threefold and
$P_m(B,\beta)\times\Delta$: the equations and the deck
transformations are identical on every line-bundle chart.
Restricting its projection to $y=0$ therefore gives the map
$p:P\to B$ in the statement. The cyclic chart
\eqref{cdp:eq:C.ER.6} restricts to
$(z,w)\mapsto(x=z^m,b=w^m,a=z/w)$, with the same free
$\boldsymbol\mu_m$ action and infinite map $w\mapsto\beta w$.
It proves smoothness of $P$ and identifies its full fibre as
$mJ$, where $J=\C^*/\beta^{m\Z}$ through $[w]\mapsto[w^m]$.
Properness is preserved by this base change, and $B$ is compact,
so $P$ is compact. The product map and inverse are the restrictions
of \eqref{cdp:eq:C.PE.9}:
$(v,[c])\mapsto[(v,\sigma(v)c^m,c^{-1})]$ and
$[(v,\ell,a)]\mapsto(v,[a^{-1}])$.

'''
new336=p336[:start]+newintro+p336[end:]
start=un6.index('\\item The occurrence of a Kodaira-dimension-one component')
end=un6.index('\\item Let $E_0',start)
newambient=r'''\item The occurrence of a Kodaira-dimension-one component in an abelian-surface degeneration appears in
\cite[Example~3.4(1), p.~99]{Fujimoto1988Log}. Let
\begin{equation}
 V=\operatorname{Bl}_{(0,0)}(E\times\Delta),\quad
 R=\operatorname{Exc}(V\to E\times\Delta),\quad
 L=\OO_V(R),\quad \sigma\in H^0(V,L)
 \hypertarget{tag-00IY}{}\label{cdp:eq:C.ER.3}
\end{equation}
with $\sigma$ the canonical section. Apply
\cref{lem:II:signed-root-fibration} to this smooth surface $V$,
its smooth divisor $D_+=R$, the empty divisor $D_-$, and the
same $m,q$. Its line and section are exactly the displayed
$L,\sigma$. Because $D_-$ is empty, its positive chart
\eqref{cdp:eq:C.ER.4} is defined on all of $V$; denote that
space by $W_m$ and its quotient by $U_m$. The identity
$(v,\ell,a)\mapsto(v,\ell,a)$ identifies its equation
$\sigma(v)=a^m\ell$ and generator \eqref{cdp:eq:C.ER.5}
with this construction. Thus the lemma gives a smooth
threefold $U_m$ and a proper map $\rho_m:U_m\to V$ with
connected elliptic reductions.

In a frame $\sigma=xe$, $\ell=be$, the cyclic map
\eqref{cdp:eq:C.ER.6} is the same map
$(z,w,y)\mapsto(x=z^m,y;b=w^m,a=z/w)$.
Its simultaneous $\boldsymbol\mu_m$ action and the lift
$w\mapsto qw$ of the infinite generator give exactly the
local projection \eqref{cdp:eq:C.ER.7}. In particular the
proper local models and full multiplicity $m$ are the
ones supplied by that lemma. Compose $\rho_m$ with the
blowdown $V\to E\times\Delta$ and the projection
$E\times\Delta\to\Delta$. All three maps are proper
with connected fibres, so their composite is the required
proper map $f_m$ with connected fibres.

Over $V\setminus R$ the product isomorphism
\eqref{cdp:eq:C.ER.8} is
$(v,[c])\mapsto[(v,\sigma(v)c^m,c^{-1})]$, with inverse
$[(v,\ell,a)]\mapsto(v,[a^{-1}])$.
The blowdown identifies $V|_{\Delta^*}$ with
$E\times\Delta^*$ by its unchanged coordinates, so this
same map identifies the punctured filling with the fixed
$(E\times E)\times\Delta^*$ for every $m$.

'''
new6=un6[:start]+newambient+un6[end:]
guards=[dict(key='P339-root-chart-owners',old=p339,new=new339),
        dict(key='P336-positive-product-base-change',old=p336,new=new336),
        dict(key='UN6-positive-ambient-application',old=un6,new=new6)]
after=text
for row in guards:
    assert after.count(row['old'])==1,row['key']
    after=after.replace(row['old'],row['new'],1)
preserve_identifiers(text,after)
for old,new in zip(identifiers(text),identifiers(after)):
    assert old==new
assert p336[:p336.index('\\begin{proof}')]==new336[:new336.index('\\begin{proof}')]
assert un6[:un6.index('\\begin{proof}')]==new6[:new6.index('\\begin{proof}')]
for name,data in [('P339',new339),('P336',new336),('UN6',new6)]:
    (folder/(prefix+name+'.tex')).write_text(data,newline='\n')
(folder/(prefix+'guards.json')).write_text(json.dumps(guards,ensure_ascii=False,indent=2)+'\n',newline='\n')
print('Three exact guards prepared; all identifiers and both receiving statements unchanged.')
