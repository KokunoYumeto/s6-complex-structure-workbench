#!/usr/bin/env python3
"""Prepare elliptic alignment, torsors, UN66/67; root owns admission."""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import csv, re

root=Path(__file__).resolve().parents[1]
out=root/'agents/continuation3_conductor'
prefix='S6_SERIES_PUBLISH_c3_conductor_13'
old=(out/(prefix+'_input.tex')).read_text()
oldk=(out/(prefix+'_K3_input.tex')).read_text()
old61=(out/(prefix+'_UN61_input.tex')).read_text()
cut=old.index(r'\begin{proposition}[A torsion-normal')
old66=old[old.index(r'\begin{proposition}'):cut]
old67=old[cut:]
rows=[]
REVIEWED=True

def log(kind,a,b,reason,owner,where='UN66/UN67 complete original subsection'):
    rows.append(dict(change_id=f'II-C3-UNRESTRICTED13-{len(rows)+1:04d}',type=kind,statement_id=owner,
        old_location=where,old_page='exact source span supplied; original PDF page omitted',
        new_location='elliptic-alignment / elliptic-core-reduction / torsion-normal-rational-obstruction; exact remote owners named',
        new_page='pending integrated final PDF',old_text=a,new_text=b,reason=reason,
        review_status=('Complete original and receiving statements/proofs compared; exposed editorial rereading; final integrated PDF reading open.' if REVIEWED else 'Complete original read; receiving comparison pending.')))
def edit(s,a,b,kind,reason,owner,where='UN66/UN67 complete original subsection'):
    assert s.count(a)==1,(owner,a[:100],s.count(a))
    log(kind,a,b,reason,owner,where);return s.replace(a,b,1)
def between(s,a,b):
    i=s.index(a);j=s.index(b,i);return s[i:j]
def display(s,tag):
    ds=[m.group() for m in re.finditer(r'\\\[.*?\\\]|\\begin\{equation\}.*?\\end\{equation\}',s,re.S)
        if r'\tag{'+tag+'}' in m.group() or r'\label{cdp:eq:'+tag+'}' in m.group()]
    assert len(ds)==1,(tag,len(ds));return ds[0]

align=r'''\subsection{Elliptic fibrations with vertical boundary}\label{subsec:II:elliptic-alignment}

\begin{lemma}[Elliptic alignment on a component]\hypertarget{tag-P260}{}\label{lem:II:vertical-elliptic-alignment}
\StatementRecord{lem:II:vertical-elliptic-alignment}{proved}{P260}{\cref{cdp:st:C.2.UN.16,lem:II:elliptic-first-integral,cdp:st:C.2.UN.29,lem:II:identity-monodromy-elliptic,cdp:st:C.2.UN.28}; \cite[Chapter~1, Proposition~2.2 and the preceding point-blowup comparison, p.~8]{Peters1990}}
Let $f:U\to\Delta$ be a proper holomorphic degeneration of connected complex two-tori from a smooth threefold, with full reduced SNC central fibre $S$. Let $T$ be a component and let $D\subset T$ be its boundary, the union of its intersections with the other components. Let $q:T\to B$ be a proper holomorphic map to a smooth compact connected curve, with connected fibres and smooth elliptic general fibre. Suppose every component of $D$ is vertical for $q$.

The map $q$ has identity integral $H_1$ monodromy on its smooth base locus. Contracting its vertical exceptional $(-1)$-curves gives a morphism $\tau:T\to T_0$ and a relatively minimal map $q_0:T_0\to B$, with $q=q_0\circ\tau$. Every fibre of $q_0$ is a positive multiple of a smooth elliptic curve; its regular fibres are torsors under one fixed elliptic curve. Moreover
'''+display(old66,'C.MR.8')+r'''
and $\chi(\OO_T)=0$. The maps $q$ and $q_0$ have the same smooth fibres away from finitely many values. When $q$ is relatively minimal, $\tau$ is the identity.
\end{lemma}
\begin{proof}
The root change of \cref{cdp:st:C.2.UN.16} has degree one here, and the smooth total space with SNC support needs no further resolution. Thus its covering component is this same $T$. The saturation and restriction maps \eqref{cdp:eq:C.CF.3}--\eqref{cdp:eq:C.CF.7} give a complex basis $V_1,V_2$ of commuting meromorphic fields on $T$, every constant linear combination semicomplete on its holomorphic locus. Their ambient representatives are holomorphic relative fields multiplied by meromorphic functions of the base. Their only polar divisors lie over zero. Cancellation of the generic order along $T$ removes that polar divisor; away from the other components every coefficient is holomorphic in codimension one and extends across the remaining codimension-two set by Hartogs. Thus the poles of the restricted fields are contained in $D$.

Remove finitely many values of $B$ so that the fibres are smooth elliptic and miss $D$. The fields are holomorphic on each entire compact fibre. In a base coordinate, the coefficient of $dq(V_i)$ is therefore constant along that fibre. Proper connected-fibre descent gives meromorphic vector fields $Z_i$ on $B$ with $dq(V_i)=q^*Z_i$; their brackets vanish.

If $Z_1\ne0$, commutation makes the meromorphic ratio $Z_2/Z_1$ constant, say $c$. Put $Y=V_1$ and $V=V_2-cV_1$. Complex-linear independence makes $V\ne0$; it is vertical, while $Y$ is generically transverse, so $V\wedge Y\ne0$. Choose a nonconstant meromorphic function $h:B\to\PP^1$. The function $h\circ q$ is a first integral of $V$. Its graph is already defined on $T$, and its Stein factor is exactly
$T\xrightarrow{q}B\xrightarrow{h}\PP^1$: the first map has connected fibres and the second is finite. Apply \cref{lem:II:elliptic-first-integral} to this $T,V,Y$ and this Stein map. Its inverse-time continuation and period-injection proof gives identity monodromy on the full smooth base of this same $q$. The case $Z_2\ne0$ uses the exchanged basis.

If $Z_1=Z_2=0$, both fields are vertical. On a regular elliptic fibre they are translation fields, so their ratio is constant there. Proper descent gives
$V_2=(q^*H)V_1$ for a meromorphic function $H$ on $B$. It is nonconstant because the fields are independent over $\C$. The Stein factor of this ratio is again $T\xrightarrow q B\xrightarrow H\PP^1$, with identity graph resolution. Apply \cref{cdp:st:C.2.UN.29} to the same multiplicity-one component, its ambient saturated fields and this ratio. Its return-period identity \eqref{cdp:eq:C.RG.12} is proved on this Stein map before the relative contraction. The period-injection step there gives identity integral monodromy for this same $q$.

In either case, contract the vertical $(-1)$-curves successively. Each contraction lowers $b_2$, so the process is finite. The map descends at each step because its contracted curve maps to a point; the descended base coordinate is holomorphic through the equality of the direct image of the structure sheaf with the structure sheaf of the smooth blowdown. This gives $q=q_0\circ\tau$ and leaves all smooth fibres outside finitely many values unchanged. The map on fundamental groups from the base with these extra values removed to the smooth base of $q_0$ is surjective, since loops avoid finitely many additional points. Hence the monodromy of $q_0$ is still the identity. Apply \cref{lem:II:identity-monodromy-elliptic} to the compact smooth surface $T_0$, this proper connected-fibre relatively minimal $q_0$, and the full smooth base. It gives the fixed elliptic curve, all full smooth-multiple fibres, $R^1(q_0)_*\OO_{T_0}=\OO_B$, $p_g(T_0)=g(B)$ and $\chi(\OO_{T_0})=0$.

The structure-sheaf direct images of an ordinary point blowup $\mu$ satisfy $\mu_*\OO=\OO$ and $R^1\mu_*\OO=0$. The first equality is Hartogs extension at its smooth centre. For the second, use the two blowup charts $(x,v)$ and $(u,y)$, with $u=1/v$ and $y=xv$. The sets $|x|<\varepsilon,|v|<2$ and $|y|<\varepsilon,|u|<2$ are Stein; their Stein overlap has $1/2<|v|<2$, $|x|<\varepsilon$ and $|xv|<\varepsilon$. They form a cofinal family of neighbourhoods of the exceptional curve as $\varepsilon$ decreases. A holomorphic cocycle on the overlap has a normally convergent Laurent expansion in monomials $x^m v^n$, $m\ge0$. Terms with $n\ge0$ extend to the first chart after decreasing $\varepsilon$; terms with $n<0$ become $y^m u^{m-n}$ and extend to the second. Cauchy estimates on smaller closed annuli give normal convergence of both parts. This splitting makes every cohomology class zero on a smaller neighbourhood and proves the vanishing of the direct-image stalk at the centre. Iteration and the Leray spectral sequence give $R^1q_*\OO_T=R^1(q_0)_*\OO_{T_0}$. The point-blowup invariance of $p_g$ and $\chi$, \cite[Chapter~1, Proposition~2.2, p.~8]{Peters1990}, gives their stated values on $T$. Finally \cref{cdp:st:C.2.UN.28}, applied to this same smooth normalization component $T$, gives $p_g(T)\le1$.
\end{proof}

'''

kx13=display(oldk,'C.KX.13').replace(r'\label{cdp:eq:C.KX.13}',r'\label{cdp:eq:C.KX.13}'+'\n'+r'\hypertarget{tag-00WA}{}\SsixEquationAliases{\label{cdp:eq:C.PT.7}}')
kx14=display(oldk,'C.KX.14').replace(r'\label{cdp:eq:C.KX.14}',r'\label{cdp:eq:C.KX.14}'+'\n'+r'\hypertarget{tag-00WB}{}\SsixEquationAliases{\label{cdp:eq:C.PT.8}}')
torsor=r'''\subsection{Principal elliptic torsors with zero Chern class}\label{subsec:II:zero-chern-elliptic-torsors}

\begin{lemma}[Principal elliptic torsors with zero Chern class]\hypertarget{tag-P330}{}\label{lem:II:zero-chern-elliptic-torsor}
\StatementRecord{lem:II:zero-chern-elliptic-torsor}{proved}{P330}{}
Let $B=\C/\Gamma$ and $F_1=\C/\Lambda_{F_1}$ be elliptic curves, and let $q:E_1\to B$ be a holomorphic principal $F_1$-torsor. Let $\mathcal F_1$ be the sheaf of holomorphic maps to $F_1$. Its analytic torsor class lies in $H^1(B,\mathcal F_1)$, and its integral Chern class is its image in $H^2(B,\Lambda_{F_1})$ under the connecting map of
'''+kx13+r'''
Suppose this Chern class is zero. There is a number $a\in\C$ and an isomorphism of principal $F_1$-torsors over the given $B$
'''+kx14+r'''
The map to $B$ is induced by $(z,w)\mapsto z$, and the $F_1$-action is translation of the second coordinate. In particular $E_1$ is a complex two-torus. The isomorphism preserves the full analytic torsor class.
\end{lemma}
\begin{proof}
Exactness of \eqref{cdp:eq:C.KX.13} lifts the torsor class to $H^1(B,\OO_B)$. The Dolbeault description of this one-dimensional space represents its lift by a constant form $a\,d\overline z$. On the universal cover its primitive is $a\overline z$, whose changes under $z\mapsto z+\gamma$ are the constants $a\overline\gamma$. These are the additive translation cocycle of the displayed quotient, and their images under $\OO_B\to\mathcal F_1$ represent the original principal torsor.

To identify the total spaces over $B$, compare their translation cocycles $g_{ij}^{\rm mod}$ and $g_{ij}^{E_1}$ on a common base cover. Equality of their classes means that $g_{ij}^{E_1}-g_{ij}^{\rm mod}=c_j-c_i$ for a holomorphic $\mathcal F_1$-valued zero-cochain $(c_i)$. In the convention $w_j=w_i+g_{ij}$, the local translations $w_i\mapsto w_i+c_i$ therefore glue a holomorphic map from the displayed model to $E_1$. The translations by $-c_i$ give its inverse. Both maps commute with the projection to $B$ and the $F_1$-action. A different lift in $H^1(B,\OO_B)$ has the same image and yields the same type of explicit isomorphism.

Choose $\Z$-bases of $\Gamma$ and $\Lambda_{F_1}$. The corresponding four period vectors are real-linearly independent: projection to the first coordinate first kills the coefficients of the two base vectors, and then the two fibre vectors have zero coefficients. Their integral span is therefore a discrete rank-four lattice in $\C^2$ with a compact fundamental parallelepiped. The quotient in \eqref{cdp:eq:C.KX.14} is a complex two-torus.
\end{proof}

'''

oldkt=between(oldk,r'\item The sheaf sequence',r'\item The group $Q$ is')
newkt=r'''\item Apply \cref{lem:II:zero-chern-elliptic-torsor} to the principal map $q_1:E_1\to B$, its fixed curve $F_1$ and the Chern class $c=0$ just proved in \eqref{cdp:eq:C.KX.12}. Its isomorphism \eqref{cdp:eq:C.KX.14} uses this same base and fibre lattice, and preserves the full analytic torsor class through its local translation cochain. It therefore identifies this very $E_1$ with a complex two-torus over $B$.
'''
newk=edit(oldk,oldkt,newkt,'D12','Moves the complete general Chern-zero/cocycle/lattice proof to P330, before K3. The receiver retains the equivariant Chern-cocycle calculation and c=0, then names the identical q1,E1,B,F1 in the lemma application. All later cyclic K3, pencil and compact realization arguments are unchanged.','cdp:st:C.2.UN.24 / cdp:st:C.2.UN.32','Complete current K3 subsection')
oldpt=between(old61,r'\item  We record an exact principal-torsor comparison',r'\item  We now identify every marked elliptic curve')
newpt=r'''\item For a principal $F=\C/\Lambda_F$-torsor over an elliptic $B$, use \cref{lem:II:zero-chern-elliptic-torsor} with $F_1=F$ and $\Gamma=\Lambda_B$. The map in \eqref{cdp:eq:C.PT.7} is its integral Chern map, and for Chern class zero \eqref{cdp:eq:C.PT.8} is the resulting isomorphism over this same $B$, preserving the analytic torsor class. We apply this to the root fibration below and to the inverse torsor $T_0\to B$ after its Chern class is computed.

'''
new61=edit(old61,oldpt,newpt,'D12','Moves the complete repeated principal-torsor construction to P330. The same base, fixed elliptic group, Chern map, additive cocycle and period-action formula are identified explicitly. The original PT7/PT8 labels and targets become same-counter aliases of KX13/KX14 under this proved renaming.','cdp:st:C.2.UN.61','Complete current UN61 statement/proof')
a=r'''zero. Formula \eqref{cdp:eq:C.PT.8} then makes $P$ a torus,
already handled above.'''
b=r'''zero. Apply \cref{lem:II:zero-chern-elliptic-torsor} with total space $E_1=P$, base $B$ and fixed curve $F_1=F$. Its map \eqref{cdp:eq:C.PT.8} identifies this root torsor with a two-torus over $B$, giving the torus case above.'''
new61=edit(new61,a,b,'D12','Names the first concrete root-torsor receiver, after its horizontal elliptic curve makes the pulled-back Chern class zero and positive-degree injectivity proves the original class zero.','cdp:st:C.2.UN.61','Complete current UN61 statement/proof')
a=r'''Thus the Chern vector is zero. Formula
\eqref{cdp:eq:C.PT.8} identifies this very inverse
torsor, including its analytic class,
with a complex two-torus.'''
b=r'''Thus the Chern vector is zero. Apply \cref{lem:II:zero-chern-elliptic-torsor} with $(E_1,B,F_1)=(T_0,B,F)$ to this inverse torsor. Its local translation cochain and quotient map \eqref{cdp:eq:C.PT.8} preserve that torsor's analytic class and identify its total space with a complex two-torus over $B$.'''
new61=edit(new61,a,b,'D12','Names the second concrete inverse-torsor receiver after the injected lattice and commutator calculation prove its integral Chern class zero. The entire pruning and compact reconstruction remain unchanged.','cdp:st:C.2.UN.61','Complete current UN61 statement/proof')
for name,s in [('newk',newk),('new61',new61)]:
    key='cdp:st:C.2.UN.32' if name=='newk' else 'cdp:st:C.2.UN.61'
    a=next(x for x in s.splitlines() if x.startswith(r'\StatementRecord{'+key+'}'))
    b=a[:-1]+r'; \cref{lem:II:zero-chern-elliptic-torsor}}'
    s=edit(s,a,b,'D12','Adds the preceding common torsor owner to this unchanged statement identity and full proof dependencies.',key,'Bounded shared-owner application')
    if name=='newk':newk=s
    else:new61=s
log('D12',oldkt+'\n'+oldpt,torsor,'P330 contains both complete general constructions, with one exact principal F1-torsor/Chern-zero domain, the full cocycle/cochain isomorphism, the rank-four period proof and the map to the given B. The finite-sheet and group-action arguments proving c=0 remain at their consumers.','lem:II:zero-chern-elliptic-torsor','K3 KX13–14 and UN61 PT7–8 complete constructions')
log('D25',between(oldkt,r'Equality of the \v{C}ech classes',r'The displayed'),between(torsor,'To identify the total spaces','Choose $\\Z$-bases'),'The difference of two transition cocycles is the coboundary of a zero-cochain. The receiving proof states g_E-g_model=c_j-c_i and proves that w_i maps to w_i+c_i, with inverse translation, glues over the given base and commutes with the principal action. This repairs the original type-level wording while retaining its intended exact torsor isomorphism.','lem:II:zero-chern-elliptic-torsor','Complete K3 original torsor comparison')

new66=old66; owner66='cdp:st:C.2.UN.66'
a=r'''All components, intersection curves and neighbourhood maps refer
to this actual degeneration.
'''
new66=edit(new66,a,'','D11','The proper given degeneration and its named full central fibre already specify every component and map.',owner66)
a=r'''These are actual blowup maps on the chosen
neighbourhood. The reduction does not identify an arbitrary
other realization of the same core support with that
neighbourhood or discard the recorded normal extensions.'''
b=r'''The reverse maps reconstruct the chosen neighbourhood together with each normal extension.'''
new66=edit(new66,a,b,'D11','States the exact neighbourhood and extension content positively; all specified ordinary blowup maps and the full reconstruction remain.',owner66)
a=r'''There is also a complete extension with no initial minimality
or no-triple assumption. For any full reduced SNC torus fibre
whose connected double curves are all elliptic, $e(S)\ge0$.'''
b=r'''For every full reduced SNC torus fibre whose connected double curves are all elliptic, $e(S)\ge0$.'''
new66=edit(new66,a,b,'D02','The universal positive statement has precisely the original broader domain, including nonminimal components and triple points.',owner66)
a=r'''For the connected reducible case let $k_v$ be the orders of
a canonical evaluation generator. Its divisor is vertical,
and adjunction with the full principal fibre gives a
meromorphic canonical section on each component with exact
divisor'''
b=r'''For the connected reducible case, apply \cref{cdp:st:C.2.UN.17} to this same family. Every multiplicity is one; the smooth components have identity normalization and resolution and intrinsic conductor zero. Write $k_v$ for its canonical evaluation orders. The principal-fibre and adjunction maps \eqref{cdp:eq:C.CA.3}--\eqref{cdp:eq:C.CA.4} give the meromorphic canonical section with divisor'''
new66=edit(new66,a,b,'D12','Uses UN17 on the identical full reduced SNC family, retaining all MR3 coefficients, marked boundary curves and its exact meromorphic section. This specialization remains valid when the final extension allows triple points.',owner66)
olda=between(old66,r'\item \par\medskip\noindent\textbf{The actual field space aligns',r'\item \par\medskip\noindent\textbf{A torsion-normal elliptic boundary on a ruled')
newa=r'''\item Whenever $q:T\to B$ is a connected elliptic map with every boundary curve vertical, apply \cref{lem:II:vertical-elliptic-alignment} to this same component of the remaining full reduced SNC torus family. It gives identity integral monodromy and \eqref{cdp:eq:C.MR.8} for this $q,T,B$. Its relative contraction removes only vertical $(-1)$-curves. On a minimal $T$ there are none. On a projective-line bundle over an elliptic curve, every rational curve is a ruling fibre and has square zero, so there are none there either. For these components the relative contraction is the identity, and the lemma's full smooth-multiple conclusion applies to $q$ itself.

'''
new66=edit(new66,olda,newa,'D12','P260 is the one full owner of both ambient field cases and their exact Stein maps. The receiver keeps the same q,T,B and explicitly identifies the relative contraction with the identity on the minimal or elliptic-ruled component types used below. MR8 moves intact to that owner.',owner66)
log('D25',olda,align,'The original general alignment paragraph claimed smooth-multiple supports directly on any component. P260 proves them on the relatively minimal map q0; its direct-image and genus conclusions transfer back to T through the explicit point blowups. UN66 proves q=q0 on its relevant minimal/elliptic-ruled surfaces, while UN67 retains its genuine contraction.','lem:II:vertical-elliptic-alignment')
a=r'''Pull the bundle back along this actual map.
The diagonal copy of $C$ is a section whose
normal line is the original torsion line $L$.
Its relative degree-one line $\OO(C)$ has
rank-two direct image, and the actual
fibrewise evaluation identifies this
pulled-back surface with the corresponding
projective bundle. After twisting that
rank-two bundle by its section subline,
it has the exact form'''
b=r'''Pull the ruling back along this map and write $p:T'\to C$ for the resulting bundle. The diagonal section $C\subset T'$ has the same normal line $L$, since $T'\to T$ is finite unramified. Put $W=p_*\OO_{T'}(C)$. Fibrewise evaluation gives a surjection $p^*W\to\OO_{T'}(C)$ and hence, with the lines convention, an isomorphism $T'\simeq\PP_C(W^*)$. Pushing forward the section restriction sequence gives $0\to\OO_C\to W\to L\to0$, because $H^1(\PP^1,\OO)=0$ on every ruling fibre. Dualize and tensor by $L$: the bundle $V=W^*\otimes L$ has the exact sequence'''
new66=edit(new66,a,b,'D20','Proves the precise dual-evaluation and tensor map needed by the lines-projectivization convention. The section corresponds to the subline O in V, its normal is the given L, and the same MR10 extension is retained rather than switching quotient and subline conventions silently.',owner66)
a=display(old66,'C.MR.10')
b=a+r'''
The dual evaluation on the section is the inclusion $L^{-1}\hookrightarrow W^*$, so tensoring identifies the diagonal section with $\PP_C(\OO_C)\subset\PP_C(V)$.'''
new66=edit(new66,a,b,'D20','Identifies the marked diagonal section through the explicit dual evaluation and twist, so its normal quotient is exactly L.',owner66)
a=r'''The additive
torsor comparison (C.PT.7)--(C.PT.8)
identifies this very surface with
a complex two-torus.'''
b=r'''Apply \cref{lem:II:zero-chern-elliptic-torsor} with $(E_1,B,F_1)=(T,B_0,F)$ and this vanishing integral Chern class. Its cocycle/cochain isomorphism identifies this principal torsor, over the same $B_0$, with a complex two-torus.'''
new66=edit(new66,a,b,'D12','Applies the earlier general P330 to the same principal torsor after the finite étale horizontal curve and degree map prove c=0. No K3-specific theorem is applied to this arbitrary component.',owner66)
a=r'''The same trace/Chern argument
and (C.PT.8) make $T'$ an
actual two-torus.'''
b=r'''A component of that pullback maps unramifiedly to the elliptic $E$ and supplies a section after its base pullback. The Chern class of $T'\to E$ is therefore killed by its positive covering degree in the free lattice $H^2(E,\Lambda_F)$, hence is zero. Apply \cref{lem:II:zero-chern-elliptic-torsor} with $(E_1,B,F_1)=(T',E,F)$. Its isomorphism preserves this pulled-back torsor and proves that $T'$ is a two-torus.'''
new66=edit(new66,a,b,'D12','Names the second finite-étale principal torsor and proves its exact Chern-zero input, then applies the same general owner. The quotient map MR14 and all marked boundary curves remain unchanged.',owner66)
a=r'''For $B_0=\PP^1$, $\delta=0$ gives
exactly the four multiplicity lists'''
b=r'''For $B_0=\PP^1$, a vertical $C$ already makes every disjoint boundary vertical for $q_0$, since the fibres have smooth irreducible supports. It remains to treat a horizontal $C$. The equality $\delta=0$ gives exactly the four multiplicity lists'''
new66=edit(new66,a,b,'D25','Separates the already settled vertical case before using horizontal C to kill the pulled-back Chern class. This supplies the necessary hypothesis for the following torus T-prime and parallel-elliptic-translate argument; the original passage made that argument after only a conditional horizontal-C sentence.',owner66)
a=r'''If $C$ was horizontal, its
pullback components are elliptic
and map finitely to $E$.'''
b=r'''The pullback components of this horizontal $C$ are elliptic and map finitely to $E$.'''
new66=edit(new66,a,b,'D25','Carries the explicit horizontal-C case established immediately before the Euclidean base cover into its Chern-zero argument.',owner66)
a=r'''The field-space comparison
leading to \eqref{cdp:eq:C.MR.8} now applies
to this very descended map,
and removes any possible
nontrivial linear monodromy.
This completes the nonruled
alignment by actual finite
cover and quotient morphisms.'''
b=r'''Apply \cref{lem:II:vertical-elliptic-alignment} to this descended connected map on the same component $T$, with every boundary just proved vertical. The component is minimal, so the relative contraction is the identity. This proves identity integral monodromy and \eqref{cdp:eq:C.MR.8} for precisely the map \eqref{cdp:eq:C.MR.14}.'''
new66=edit(new66,a,b,'D12','The final quotient fibration is named explicitly in the shared alignment application; minimality identifies its relative model by the identity map.',owner66)
a=r'''No support-only inverse
logarithm has been used to
assert a new smoothing:
the intermediate degenerations
are the actual \ref{cdp:st:C.2.UN.64} blowdowns,
and \ref{cdp:st:C.2.UN.61}/62 are applied to
their actual final family.'''
b=r'''The intermediate families are the ordinary blowdowns of \cref{cdp:st:C.2.UN.64}. Apply \cref{cdp:st:C.2.UN.61,cdp:st:C.2.UN.62} to their final family, with the same components, connected elliptic maps, boundary fibres, normal lines and analytic torsors just identified.'''
new66=edit(new66,a,b,'D02','Replaces the defensive support-only contrast by the exact final-family maps and unchanged full torsors required by the two core criteria.',owner66)
a=between(old66,r'\item  The finite maximum partitions,',r'\end{enumerate}')
new66=edit(new66,a,'','D09','All degree partitions, elliptic intersection cases, multiplicity lists and Euler sums remain proved in text. Program A_minimal_reduction.py is mapped by separately prepared appendix158 to its pinned path and exact scope, with no execution credit.',owner66)
for a,b in [(r'\ref{cdp:st:C.2.UN.61}/62',r'\cref{cdp:st:C.2.UN.61,cdp:st:C.2.UN.62}'),(r'extended \ref{cdp:st:C.2.UN.61}',r'\cref{cdp:st:C.2.UN.61}')]:
    if a in new66:new66=edit(new66,a,b,'D04','Uses the actual numbered theorem targets, preserving both complete receiving domains.',owner66)

new67=old67;owner67='cdp:st:C.2.UN.67'
a=r'''It imposes neither a zero-Euler hypothesis nor a
minimality hypothesis on the other components.
'''
new67=edit(new67,a,'','D11','The full stated proper reduced-SNC domain already allows these cases. The explicit permission for triple points and rational double curves elsewhere remains.',owner67)
a=between(old67,'The obstruction is obtained on the actual component.',r'\end{proposition}')
new67=edit(new67,a,'','D12','Moves no conclusion out of the proof: this statement-ending mechanism summary repeats the complete pencil, monodromy, relative contraction and Euler contradiction proved immediately below. The obstruction and every interface consequence remain in the statement.',owner67)
a=r'''We check its connectedness through the Stein map,
rather than assuming that a pencil has connected
fibres.'''
b='Use the Stein factor to prove connectedness of the pencil.'
new67=edit(new67,a,b,'D02','States the connectedness proof directly while retaining the exact finite Stein map, multiplicity division and torsion-order argument.',owner67)
oldmiddle=between(old67,r'\par\medskip\noindent\textbf{The actual translation fields align this pencil.}',r'\par\medskip\noindent\textbf{The Hopf interface.}')
newmiddle=r'''\item Apply \cref{lem:II:vertical-elliptic-alignment} to the original component $T=P$, the connected pencil $q:P\to B=\PP^1$ in \eqref{cdp:eq:C.RH.4}, and its boundary. The preceding intersection computation makes every boundary curve vertical. The ambient family is the given smooth threefold with full reduced SNC fibre, so its degree-one component construction uses $P$ itself. The lemma proves identity integral monodromy for this precise pencil, in both the transverse/vertical and the two-vertical-field cases of its proof.

Write $\tau:P\to P_{\min}$ for the lemma's contraction of the vertical exceptional curves. It descends this same $q$ to
'''+display(old67,'C.RH.7')+r'''
Each step is an ordinary point blowdown, and it leaves the marked smooth fibres unchanged. The point-blowup comparison in \cref{lem:II:vertical-elliptic-alignment} gives $\chi(\OO_{P_{\min}})=\chi(\OO_P)=1$.

\item For a full fibre of multiplicity $a$, write its local function as $t=u h^a$, where $u$ is a unit and the divisor of $h$ is primitive. The root chart in the proof of \cref{lem:II:identity-monodromy-elliptic}, used by the alignment lemma on $(T_0,q_0,B)=(P_{\min},q_{\min},\PP^1)$, is
'''+display(old67,'C.RH.8')+r'''
with its exponent $m=a$, the same unit $u$ and the same primitive equation $h$. The root projection is finite \'etale, and the cited proof retains relative minimality by canonical intersection, the primitive smooth fibre, the free translation inertia and the invariant full-fibre coefficient functions. Consequently the conclusion of the alignment lemma for this $q_{\min}$ is
'''+display(old67,'C.RH.9')+r'''
Every full fibre is a positive multiple of a smooth elliptic curve. Coherent Leray gives $\chi(\OO_{P_{\min}})=1-1=0$, contradicting its preserved value one. This proves the asserted obstruction on the original nonminimal component.

\item '''
new67=edit(new67,oldmiddle,newmiddle,'D12','P260 owns the two complete ambient-field/Stein-map cases. Its explicit relative contraction is applied to the very pencil built by RH1–6. P306 owns the full proper-analytic root/minimality/classification/direct-image proof; RH7–9 remain the exact nonminimal rational-component specialization, with m=a and the same u,h,s,w. No hypothesis is weakened and no relative-minimal assertion is applied before contraction.',owner67)

for name,s,owner in [('new66',new66,owner66),('new67',new67,owner67)]:
    a=next(x for x in s.splitlines() if x.startswith(r'\StatementRecord'))
    if name=='new66':
        b=r'\StatementRecord{cdp:st:C.2.UN.66}{proved}{01EC}{\cref{cdp:st:C.2.UN.17,cdp:st:C.2.UN.64,cdp:st:C.2.UN.65,lem:II:vertical-elliptic-alignment,lem:II:zero-chern-elliptic-torsor,cdp:st:C.2.UN.19,cdp:st:C.2.UN.31,cdp:st:C.2.UN.28,cdp:st:C.2.UN.47,cdp:st:C.2.UN.44,cdp:st:C.2.UN.58,cdp:st:C.2.UN.50,cdp:st:C.2.UN.53,cdp:st:C.2.UN.54,cdp:st:C.2.UN.61,cdp:st:C.2.UN.62}}'
    else:
        b=r'\StatementRecord{cdp:st:C.2.UN.67}{proved}{01ED}{\cref{lem:II:vertical-elliptic-alignment,lem:II:identity-monodromy-elliptic,cdp:st:C.2.UN.37,cdp:st:C.2.UN.50,cdp:st:C.2.UN.53}; \eqref{cdp:eq:C.RH.1}--\eqref{cdp:eq:C.RH.10}}'
    s=edit(s,a,b,'D12','Names the exact common proved owners and complete remaining construction dependencies. The previously direct Kodaira/monodromy-table inputs are now at their single P306 proof owner.',owner)
    if name=='new66':new66=s
    else:new67=s

clean={}
for name,s,owner in [('new66',new66,owner66),('new67',new67,owner67)]:
    for m in list(re.finditer(r'\\par\\medskip\\noindent\\textbf\{[^}]+\}\n?',s))[::-1]:
        s=edit(s,m.group(),'','D13','The mathematical proof remains under its numbered owner and sequential steps; removes the unnumbered mini-heading.',owner)
    s=edit(s,r'\begin{proof}\leavevmode\par',r'\begin{proof}','D23','Uses the standard proof environment after removing inherited empty spacing commands.',owner) if r'\begin{proof}\leavevmode\par' in s else s
    ps=s.split('\n\n')
    for i,p in enumerate(ps):
        q=re.sub(r'\bactual\s+','',p)
        q=q.replace('a supplied quasi-bundle','a quasi-bundle').replace('every supplied','every given')
        q=q.replace('by its recorded','by its').replace('recorded ordinary','ordinary')
        q=q.replace('the original nonminimal surface','the nonminimal surface $P$')
        q=q.replace('etale',r"\'etale").replace(r"\'\'etale",r"\'etale").replace('Bezout',r"B\'ezout")
        q=q.replace('For completeness, a diagonal','A diagonal').replace(r'scope of the \cref',r'scope of \cref')
        q=re.sub(r'\b([Aa])n(\s+)(?=(?:map|proper|holomorphic|smooth|rank|circle|line|compact|finite|integral|meromorphic|bundle|two|torus|point)\b)',r'\1\2',q)
        if q!=p:
            log('D08' if 'actual' in p or 'supplied' in p or 'recorded' in p else 'D23',p,q,'Names the same proved component, field, curve, covering or blowup directly; every mathematical marking and full map remains. Articles and accents are corrected.',owner)
            ps[i]=q
    clean[name]='\n\n'.join(ps)
new66,new67=clean['new66'],clean['new67']

with (root/'agents/continuation2_B/D19/S6_SERIES_PUBLISH_II_B2_D19_v1_equation_map.tsv').open() as f:
    established={r['old_tag']:r['target_label'] for r in csv.DictReader(f,delimiter='\t') if r['old_tag']}
def refs(s,owner):
    for m in list(re.finditer(r'\((C\.[A-Za-z0-9.]+)\)',s))[::-1]:
        tag=m.group(1);assert tag in established,tag
        a=max(0,s.rfind('\n\n',0,m.start())+2);b=s.find('\n\n',m.end());b=len(s) if b<0 else b
        before=s[a:b];after=before[:m.start()-a]+r'\eqref{'+established[tag]+'}'+before[m.end()-a:]
        s=s[:a]+after+s[b:]
        log('D04',before,after,'Uses the permanent reader target from the established D19 map; all later construction inputs stay explicit in the dependency record.',owner)
    return s
new66=refs(new66,owner66);new67=refs(new67,owner67)
old_displays={lab:m.group() for m in re.finditer(r'\\\[.*?\\\]',old,re.S) for lab in re.findall(r'\\label\{([^}]+)\}',m.group())}
eq=[]
def number(s,owner):
    def conv(m):
        a=m.group();tags=re.findall(r'\\tag\{([^}]+)\}',a)
        if not tags:return a
        assert len(tags)==1;lab=re.findall(r'\\label\{([^}]+)\}',a)[0];assert established[tags[0]]==lab
        b=a.replace(r'\[',r'\begin{equation}',1);b=b[:-2]+r'\end{equation}';b=b.replace(r'\tag{'+tags[0]+'}','')
        log('D19',old_displays[lab],b,'Uses the section counter, preserving the exact formula and all permanent labels/targets. MR8 moves with its full alignment owner.',lab)
        eq.append(dict(old_tag=tags[0],target_label=lab,statement_id=owner));return b
    return re.sub(r'\\\[.*?\\\]',conv,s,flags=re.S)
align=number(align,'lem:II:vertical-elliptic-alignment');new66=number(new66,owner66);new67=number(new67,owner67)
for tag,kxtag in [('C.PT.7','C.KX.13'),('C.PT.8','C.KX.14')]:
    eq.append(dict(old_tag=tag,target_label='cdp:eq:'+tag,statement_id='lem:II:zero-chern-elliptic-torsor'))
    log('D19',display(old61,tag),display(torsor,kxtag),'Preserves the PT equation identity and permanent target as a same-counter alias of the identical sheaf sequence or quotient action under F=F1 and Lambda_B=Gamma. The coordinate map is the identity on (z,w), the base projection and the fibre action.','cdp:eq:'+tag,'UN61 complete torsor construction')
def spacing(s):return re.sub(r'\n{4,}','\n\n\n',s).rstrip()+'\n\n'
align,torsor,new66,new67=map(spacing,[align,torsor,new66,new67])
h66=r'\subsection{Contractions to elliptic cores}\label{subsec:II:elliptic-core-reduction}'+'\n\n'
h67=r'\subsection{Torsion-normal elliptic curves on rational components}\label{subsec:II:torsion-normal-rational-obstruction}'+'\n\n'
work=align+h66+new66+h67+new67
anchor=r'\subsection{Elliptic fibre configurations of component surfaces}\label{subsec:II:elliptic-configuration-list}'
log('D14',old.split('\n\n',1)[0],align.split('\n\n',1)[0]+'\n'+h66+h67,'Gives the shared alignment and the two complete receiving theorems their own actual subsections. P330 is inserted before the earliest K3 use; all root/PT applications then point backward. Root owns the final UN64–68 section placement after section10.','subsec:II:elliptic-alignment')
log('D14',anchor,torsor.split('\n\n',1)[0]+'\n\n'+anchor,'The single general zero-Chern torsor owner receives an actual subsection immediately after P319 and before the earliest K3 use. This isolated unit is fully read; the unchanged preceding cyclic-quotient owners are not assigned new full-reading credit.','subsec:II:zero-chern-elliptic-torsors','Immediately after P319 and before elliptic-configuration-list')

def payload(s):
    s=re.sub(r'\\SsixEquationAliases\{(?:\\label\{[^}]+\})+\}','',s)
    s=re.sub(r'\\tag\{[^}]+\}|\\label\{[^}]+\}|\\hypertarget\{[^}]+\}\{\}','',s)
    for x in [r'\[',r'\]',r'\begin{equation}',r'\end{equation}']:s=s.replace(x,'')
    return re.sub(r'\s+','',s)
new_displays={lab:m.group() for m in re.finditer(r'\\begin\{equation\}.*?\\end\{equation\}',work,re.S) for lab in re.findall(r'\\label\{([^}]+)\}',m.group())}
for lab,d in old_displays.items():assert payload(d)==payload(new_displays[lab]),lab
for lab in ['C.KX.13','C.KX.14']:assert payload(display(oldk,lab))==payload(display(torsor,lab)),lab
for kind in ['label','hypertarget']:
    pat=r'\\'+kind+r'\{([^}]+)\}'
    before=Counter(re.findall(pat,old+oldk+old61));after=Counter(re.findall(pat,work+torsor+newk+new61))
    assert all(after[k]==v for k,v in before.items()),(kind,before-after)
    assert max(after.values())==1,(kind,[k for k,v in after.items() if v>1])
for s in [work,torsor,newk,new61]:assert Counter(re.findall(r'\\begin\{([^}]+)\}',s))==Counter(re.findall(r'\\end\{([^}]+)\}',s))
assert not re.search(r'\\tag\{|night:P4R\.13|night:P4\.40|\r|\\path\{|\\textbf\{|\(C\.',work+torsor)
assert len(old_displays)==26,len(old_displays)
assert len(eq)==28,len(eq)
assert r"\'\'etale" not in work+torsor
assert 'an torus' not in work+torsor

def tsv(suffix,fields,data):
    with (out/(prefix+suffix)).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(data)
for suffix,text in [('_replacement.tex',work),('_P260.tex',align[align.index(r'\begin{lemma}'):]),('_P330.tex',torsor),('_K3_replacement.tex',newk),('_UN61_replacement.tex',new61)]:
    (out/(prefix+suffix)).write_text(text,newline='\n')
with (root/'S6_SERIES_PUBLISH_defects_II.tsv').open() as f:fields=next(csv.reader(f,delimiter='\t'))
tsv('_defects.tsv',fields,rows)
tsv('_equations.tsv',['old_tag','target_label','statement_id'],eq)
remote=[
dict(statement_id='lem:II:zero-chern-elliptic-torsor',old_text=anchor,new_text=torsor+anchor,reason='Insert the general principal elliptic torsor owner immediately after P319 and before the next elliptic-configuration subsection, hence before K3 and all later PT/UN66 uses.'),
dict(statement_id='cdp:st:C.2.UN.24 / cdp:st:C.2.UN.32',old_text=oldk,new_text=newk,reason='Full K3 guard: move only its general KX13–14 torsor construction to P330 and apply that exact principal E1→B,F1,c=0 owner. All other statement/proof text and targets are unchanged.'),
dict(statement_id='cdp:st:C.2.UN.61',old_text=old61,new_text=new61,reason='Full UN61 guard: move only the general PT7–8 construction and name its two exact P and T0 applications. All other complete root, height, inverse-torsor and compact-realization proof text remains. This is a bounded shared-owner transfer, not closure of the whole unreviewed section10 unit.')]
tsv('_remote_repairs.tsv',['statement_id','old_text','new_text','reason'],remote)

if not REVIEWED:
    print('13 PREPARED:',len(rows),'defects;26 unchanged main formula payloads;2 unchanged KX owner payloads;28 D19 identities;3 remote guards. Complete receiving review pending.')
    raise SystemExit

current=(root/'S6_SERIES_PUBLISH_II.tex').read_text()
assert current.count(old)==1,'The full main original guard has changed.'
assert all(current.count(r['old_text'])==1 for r in remote),'A bounded remote guard has changed.'

now=datetime.now(timezone.utc).isoformat()
maps=[
dict(old_owner='UN66 MR8 and UN67 field-alignment paragraphs',new_owner='P260 / lem:II:vertical-elliptic-alignment',conclusion='Identity integral monodromy, fixed Jacobian and smooth-multiple fibres on the relative minimal model; R1qO=OB, pg=g(B)<=1 and chi=0 on the original component.',map='Full reduced SNC family gives the identity root/resolution component E=T. Projected fields are Z_i; for Z1 nonzero use (V,Y)=(V2-cV1,V1), h composed with q and its identical Stein map. For both projections zero use V2=(q*H)V1 and the same q as Stein map. The vertical contraction tau satisfies q=q0 tau and ordinary point-blowup direct images compare coherent sheaves.'),
dict(old_owner='UN66 canonical-generator paragraph',new_owner='UN17 / cdp:st:C.2.UN.17',conclusion='MR3 with every coefficient k_w-k_v-1 and the same boundary curves.',map='Apply CA3/CA4 to the identical f:U->Delta with all m_i=1, identity normalization/resolution of T_v and intrinsic conductor divisor zero. This adjunction specialization also holds at triple points in the final extension.'),
dict(old_owner='UN67 full multiple-fibre classification and invariant coefficient descent',new_owner='P306 / lem:II:identity-monodromy-elliptic, through P260',conclusion='All full fibres of q_min are smooth multiples; q_min*O=O_P1 and R1q_min*O=O_P1.',map='First contract vertical (-1)-curves on P to P_min; then apply P306 with (E,q,B)=(P_min,q_min,P1). Its local equation t=u h^m has m=a, same u,h, w^a=u and s=wh, giving retained RH8. Full-fibre invariant coefficient functions give RH9, including multiple-fibre descent.'),
dict(old_owner='K3 UN24/UN32 KX13/KX14 and UN61 PT7/PT8',new_owner='P330 / lem:II:zero-chern-elliptic-torsor',conclusion='An exact principal-torsor isomorphism over its given elliptic base to the displayed complex two-torus.',map='F=F1, Lambda_B=Gamma, identity coordinates (z,w), same first-coordinate projection and second-coordinate F-action. Equality of cocycles is g_E-g_mod=c_j-c_i, so w_i maps to w_i+c_i with inverse translation. PT7/PT8 keep tags 00WA/00WB as aliases of KX13/KX14.'),
dict(old_owner='K3 UN24/UN32 c=0 consumer',new_owner='P330 application in unchanged K3 proof',conclusion='The specific E1=E0/H is a complex two-torus over the same B.',map='The equivariant lattice-cocycle proof c=beta c and beta-I invertible gives KX12 c=0. Apply P330 to (E1,B,F1)=(E0/H,B,F1); all remaining finite quotient, pencil and compact realization maps are unchanged.'),
dict(old_owner='UN61 root and inverse-torsor constructions',new_owner='P330 two explicit applications',conclusion='The root principal torsor P and the inverse principal torsor T0, whenever their respective proved Chern vectors vanish, are the given complex tori over B.',map='Root: horizontal elliptic base cover supplies a section and positive-degree pullback on H2(B,Lambda_F) gives c=0. Inverse torsor: PT11 pi1=Z4 and injected fibre lattice in PT12 make the clutching commutator c zero. Apply P330 to E1=P and E1=T0 respectively, keeping F1=F.'),
dict(old_owner='UN66 nonruled horizontal-boundary cases',new_owner='P330 applications and P260 final alignment',conclusion='The principal torsors T->B0 and Tprime->E are exact two-tori; the descended MR14 map has identity monodromy.',map='For elliptic B0, horizontal C->B0 is finite unramified and trivializes the pulled-back torsor. For B0=P1, settle vertical C directly and retain horizontal C; the Euclidean base cover removes every multiple fibre by the finite etale QT2 root chart. A pulled-back elliptic C then trivializes a finite base pullback. In both free H2 lattices positive degree forces c=0. Apply P330, then quotient the common elliptic subtorus Fprime in MR14 and apply P260 with tau=identity on minimal T.'),
dict(old_owner='UN66 ruled-bundle section comparison',new_owner='UN66 MR10 exact lines-projectivization map',conclusion='The diagonal marked section is P(O) in P(V), with extension 0->O->V->L->0 and normal L.',map='For p:Tprime->C put W=p_*O(C). Dual evaluation gives Tprime=P(W*); restriction gives 0->O->W->L->0. Dualize and tensor by L to V=W* tensor L. On the section, L^-1->W* becomes O->V. The canonical tensor map P(W*)=P(V) preserves the section and its normal quotient L.')]
tsv('_owner_transfers.tsv',['old_owner','new_owner','conclusion','map'],maps)
deps=[
dict(consumer='P260',input='UN16, P303, UN29, P306, UN28',map='Identity multiplicity-one component; same ambient saturated fields and both exact Stein maps; q=q0 tau; same full smooth base; same smooth normalization component for pg<=1.',status='All inputs precede the owner. Complete UN16 and UN28, and the complete current UN29 proof were read; P303/P306 full proof readings are the earlier exposed admitted readings. No independent credit.'),
dict(consumer='P330 and K3',input='P319 preceding subsection; KX12 principal torsor Chern-zero calculation',map='Place P330 immediately after P319 in its own subsection, before elliptic configurations and K3. K3 retains its full c=beta c proof before the exact P330 application.',status='Local order complete with bounded original/replacement guards.'),
dict(consumer='UN66',input='UN64, UN65, UN61, UN62, UN50, UN53, UN54, UN58; P260/P330',map='Apply the former to the same final ordinary blowdown family and all its components, boundary maps, normals and analytic torsors; shared owner maps are specified in owner_transfers.',status='Local owner order complete; current later-section construction inputs remain forward until root moves the UN64–68 block after sec10.'),
dict(consumer='UN67',input='P260/P306 and UN37/UN50/UN53 Hopf interface',map='Original P and connected RH4 pencil; every boundary vertical by intersection with mJ. Contract to P_min before all relative-minimal inputs. At the Hopf interface the same xy=t normal tensor map carries the finite normal order.',status='P260/P306 precede. Root whole-block move after sec10 resolves the later Hopf interface inputs.'),
dict(consumer='UN61 bounded guard',input='P330; unchanged UN60 inverse charts and PT13/PR13 compact realization',map='Full original and receiving statements/proofs read. Only general torsor owner transfer and its two exact applications are edited. All pruning, height, collar, compactness and reconstruction maps remain byte-identical outside those bounded spans.',status='Bounded transfer complete; the complete sec10 all-25-class rewrite remains assigned and open. Its remaining body paths and inherited tags are intentionally untouched in this bounded guard.'),
dict(consumer='Later UN46/UN57 collar uses',input='P326 normal-product collar owner',map='Root will move the existing P326 alone before the fibre-fundamental-groups subsection. Section10 applications will retain the same full reduced SNC/no-triple family and the same component normals and xy=t annuli.',status='Known later D12 transfer remains open and is not closed by package13.')]
tsv('_dependencies.tsv',['consumer','input','map','status'],deps)

events=[]
def ev(owner,key,where,outcome,source='_replacement.tex'):
    events.append(dict(statement_id=owner,date=now[:10],who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; inherited effort not separately exposed; continuation3 conductor agent',type='used and rechecked in this run',outcome=outcome+' Exposed editorial rereading only; no independent proof or program execution credit. All original permanent labels/targets are preserved. No refined night:P4R.13 or night:P4.40 use occurs in this package. Final integrated PDF reading remains open.',event_id='publish:c3:conductor13:'+key,phase='publication editorial comparison',source_file='agents/continuation3_conductor/'+prefix+source,source_row='',source_event_type='used and rechecked in this run',evidence_group='publish:c3:conductor13:elliptic-core-torsors',publish_input_file='',publish_input_row='',date_utc=now,where=where))
ev('lem:II:vertical-elliptic-alignment','P260','subsec:II:elliptic-alignment','Read both complete original alignment passages in UN66/UN67 and the entire receiving P260 statement/proof. Compared full proper smooth threefold, connected torus general fibre, reduced SNC, boundary verticality and connected elliptic-map hypotheses. Root/resolution degree one gives identical T. In the transverse case P303 uses V=V2-cV1,Y=V1 and h composed with q; in the vertical case the full current UN29 return-germ proof was reread and RG12 applies to the same ratio Stein map before contraction. Vertical blowdowns give q=q0 tau, and loops on the full smooth base are compared through the extra punctures. P306 applies only to T0,q0. The exact Stein two-chart Laurent split proves mu_*O=O and R1mu_*O=0; Peters p8 is used only for global pg/chi invariance. MR8 is unchanged and UN28 applies to the same T. The false unrestricted smooth-multiple assertion in the original paragraph is repaired by distinguishing q from q0.')
ev('cdp:st:C.2.UN.66','UN66','subsec:II:elliptic-core-reduction','Read the complete original and receiving statement/proof. Retained all four cores, neighbourhood reversal, normal extensions, negative Euler formula and complete all-elliptic-double-curve extension. UN17 supplies the same MR3 divisor with m_i=1 and identity normalization/resolution. Preserved every maximum-order partition, ruled and plane case, Hopf canonical-height case, finite-normal propagation, tree/unicycle and integral inverse-torsor inputs. The MR10 lines convention is proved by dual evaluation W=p_*O(C), V=W* tensor L and its marked subline. Both principal torsor cases apply P330 with their exact Chern-zero maps. The P1-base vertical case is now settled before the horizontal-C proof of Tprime being a torus; MR14 then applies P260 on minimal T through tau=identity. The rational-boundary exclusion, every higher-genus component counted once, Euler changes, converse ordinary elliptic blowups, nonminimal final extension and triple-point term remain complete. Program A_minimal_reduction.py moves only to appendix158. All26 main formula payloads remain unchanged.')
ev('cdp:st:C.2.UN.67','UN67','subsec:II:torsion-normal-rational-obstruction','Read the complete original and receiving statement/proof. The original broad nonminimal rational-component domain and allowance for triple points elsewhere are unchanged. Retained divisor restriction induction, basepoint-free mJ pencil, exact finite Stein factor with N^(m/d)=O and d=1, adjunction genus and verticality of every other boundary. P260 applies to this same P,q,B=P1; RH7 is the genuine vertical contraction. P306 applies to this relatively minimal map, with m=a and exactly w^a=u,s=wh in RH8. Its full multiple-fibre invariant cohomology supplies RH9 and the chi=1 versus chi=0 contradiction. Complete Hopf interface and terminal-parent exclusions retain the same xy=t dual-normal map and exact finite normal orders.')
ev('lem:II:zero-chern-elliptic-torsor','P330','subsec:II:zero-chern-elliptic-torsors','Read the complete old K3 KX13–14 and UN61 PT7–8 constructions and the entire receiving general lemma. The principal F1-torsor, integral Chern class, sheaf sequence, constant Dolbeault representative, additive period cocycle, exact base projection and fibre action are all retained. The cochain step now states the correct coboundary equation g_E-g_model=c_j-c_i and gives both inverse coordinate translations, proving the total-space identification over B. The four real period vectors are proved independent by base and fibre projection, so the lattice is discrete and cocompact. Under F=F1 and Lambda_B=Gamma the old PT formulas are exactly the KX maps, with both permanent tags retained as same-counter aliases. P330 has its own actual subsection before the earliest K3 consumer.','_P330.tex')
ev('cdp:st:C.2.UN.24 / cdp:st:C.2.UN.32','K3','subsec:II:k3-cyclic-components','Read all original and receiving K3 statements and proofs, including every unchanged finite cover, relative minimal-model map, canonical character, ramification/multiplicity argument, Chern cocycle, cyclic fixed-point calculation, elliptic pencil and compact realization. The only mathematical proof edit transfers the general KX13–14 construction to P330 and applies it after the unchanged KX12 c=0 proof, on the identical E1=E0/H over B with F1. The cocycle sign/convention in P330 is checked explicitly. All other proof text is unchanged under the full bounded guard.','_K3_replacement.tex')
ev('cdp:st:C.2.UN.61','UN61','bounded full UN61 guard in sec:II:10','Read all original and receiving UN61 statements and proofs. Compared root cohomology incidence, dualizing-form leaf elimination, unique canonical minimum, exact root fibration, finite normal orders and heights, full inverse logarithmic pruning, integral pi1/Chern commutator and complete PT13/PR13 compact reconstruction. The general PT7–8 proof moves to P330; its root P and inverse T0 uses now name the exact principal torsors and the preceding positive-degree or injected-lattice Chern-zero calculation. Formula aliases preserve all later uses. Outside these bounded owner/dependency/application spans the source is unchanged, including the as-yet-unrevised sec10 workflow prose and program paths. This event does not close the full sec10 unit.','_UN61_replacement.tex')
with (root/'CHECK_EVENTS.tsv').open() as f:eventfields=next(csv.reader(f,delimiter='\t'))
tsv('_CHECK_EVENTS.tsv',eventfields,events)

units=[('subsec:II:elliptic-alignment','Elliptic fibrations with vertical boundary','P260'),('subsec:II:elliptic-core-reduction','Contractions to elliptic cores','UN66'),('subsec:II:torsion-normal-rational-obstruction','Torsion-normal elliptic curves on rational components','UN67'),('subsec:II:zero-chern-elliptic-torsors','Principal elliptic torsors with zero Chern class','P330')]
statuses=[]
for unit,title,owner in units:
    for c in [f'D{i:02}' for i in range(1,26)]+['structure']:
        status='done';reason=f'Complete original and receiving {owner} statements/proofs compared. Every local instance found is recorded with its exact maps; this row concerns this actual subsection only.'
        if c in ['D10','D16']:reason='Prior done status preserved; hidden records and permanent labels/tags remain, and each numbered owner has a mathematical title.'
        elif c=='D12':reason='The shared proof has one numbered owner and each consumer names the identical objects, hypotheses and maps. All K3/UN61 transfers are supplied as complete bounded guards; specialized reconstruction arguments remain in their owners.'
        elif c in ['D14','structure']:
            if owner=='P330':reason='The general owner stands immediately after P319 in its own subsection, before its earliest K3 consumer. Both later UN61 uses and the UN66 cases point backward. Its local owner/order restructuring is complete.'
            else:status='open';reason='Local alignment/core/obstruction subsection order is complete. Root owns the approved UN64–68 relocation after sec10; later Hopf and complete reconstruction premises remain explicitly mapped until that move.'
        elif c=='D15':reason='This is a body subsection; no front-matter process claim is introduced.'
        elif c=='D17':reason='The exact common P303/UN29/P306 constructions are reused with full hypothesis maps. The short point-blowup sheaf calculation is retained because the freshly read Peters p8 states the global invariants, not that local sheaf assertion. The torsor proof retains its exact analytic class and coordinate maps.'
        elif c=='D18':status='open';reason='The exact Peters author-notes locator/version is recorded and bibliography155/156 is already admitted. Source-wide bibliography review remains separate.'
        elif c=='D19':reason='All26 main inherited equation payloads are unchanged under section numbering; the two PT targets alias the unchanged KX sheaf/period formulas through F=F1, Lambda_B=Gamma and identity (z,w). The complete old-tag map is supplied.'
        elif c=='D20':reason='The ruled-bundle lines convention is derived by dual evaluation and tensoring; the torsor notation conversion identifies the same base lattice, fibre lattice, action and projection.'
        elif c=='D23':status='open';reason='Source articles, accents and proof spacing are corrected. Final integrated PDF page reading remains open.'
        elif c=='D24':reason='No front-matter promise is changed; final organization prose is root-owned after the whole-block move.'
        elif c=='D25':reason='Every original and receiving inference was compared. The general alignment now distinguishes q from its relative model; the P1 torsor branch explicitly assumes horizontal C after settling the vertical case; and the cocycle difference is correctly a coboundary, with both gluing maps proved.'
        statuses.append(dict(unit=unit,title=title,criterion=c,status=status,reason=reason))
tsv('_unit_status.tsv',['unit','title','criterion','status','reason'],statuses)

source=[dict(source_id='Peters1990-author-notes-p8',url='https://cpeters1.win.tue.nl/ConfsAndSchools/Canada/surface.pdf',version='35-page author notes; exact layout already specified by admitted bibliography156',exact_locus='Chapter 1, Proposition 2.2 and the preceding point-blowup comparison, printed p.8; complete page read',sha256='51f9c99621b3819aa85894a8cdee4a528b0894364fc22b40a651f1bae55ceed3',bytes=255331,own_paraphrase='Point blowups preserve plurigenera and coherent Euler characteristic. The page does not supply the sheaf-level R1mu_*O identity; P260 proves that particular local assertion by the explicit two-chart convergent Laurent calculation.',reader='continuation3 conductor; freshly opened complete printed p.8 in this package review',date_utc=now,storage='Temporary primary cache outside checkpoint; no source PDF/text/page image copied into deliverable.')]
tsv('_sources.tsv',['source_id','url','version','exact_locus','sha256','bytes','own_paraphrase','reader','date_utc','storage'],source)

comparison=r'''# Package 13: complete original and receiving comparison

## Scope and exact guards

The main replacement covers the complete original “Elliptic cores and torsion-normal boundaries” subsection, containing UN66 and UN67. It gives three actual subsections: P260 elliptic alignment, UN66 contractions to elliptic cores, and UN67 torsion-normal rational obstruction. The full original main fragment matches the current source once.

Three additional exact guards insert P330 in its own subsection immediately after P319, replace the complete current K3 subsection by its bounded P330 application, and replace the complete current UN61 statement/proof by its bounded P330 applications. Each original guard matches once. No central source is edited by this package. The preceding P317–P319 unit is unchanged.

The complete original and receiving UN66, UN67, K3 and UN61 statements/proofs were read, as were the entire receiving P260/P330 statements/proofs. This is exposed editorial comparison. All old permanent labels and targets retain their exact multiplicities. The 26 main numbered formula payloads are unchanged. The KX13/KX14 payloads are unchanged at P330; PT7/PT8 are their identical sequence/action under F=F1 and Lambda_B=Gamma, with their old targets retained as same-counter aliases. There are 28 old-tag conversion rows. No refined P4R.13 or P4.40 use occurs.

## P260: the same elliptic map and its relative model

The general alignment paragraphs in UN66 and UN67 have one owner, with the full original domain: a proper map from a smooth threefold, connected two-torus fibres away from zero, a full reduced SNC central fibre, a component T and a proper connected-fibre elliptic map q:T→B whose entire boundary is vertical. The owner allows triple points elsewhere. It does not import the minimal-or-bundle hypothesis of UN66 or the rationality hypothesis of UN67.

UN16 is applied with root degree one and identity resolution, so its covering component is exactly T. Its two complex-linearly independent ambient fields commute and every constant combination is semicomplete. Their meromorphic coefficients depend on the base. Generic cancellation along T removes that divisor; the remaining codimension-two set away from the boundary is removed by Hartogs. The original polar-support argument is therefore retained on the same component.

On compact regular fibres the projected coefficients are constant and descend to commuting meromorphic fields Z1,Z2 on B. If Z1 is nonzero, their ratio is constant c. The exact pair is V=V2−cV1, Y=V1; V is nonzero and vertical, Y transverse, and V∧Y is nonzero. For a nonconstant h:B→P1 the Stein factor of h∘q is precisely q followed by h, because q has connected fibres and h is finite. P303 applies to those same fields and map, retaining its no-pole inverse-time and period-injection argument.

If both projections vanish, the ratio is q*H for a nonconstant meromorphic H on B. The graph resolution is the identity and the Stein map is exactly q followed by H. The entire current UN29 proof was reread: its RG12 period formula and injection prove monodromy on this map before relative contraction. P260 names that exact intermediate locus. Both cases therefore give identity integral monodromy of the original q.

The relative contraction τ:T→T0 removes only vertical exceptional curves. Each step lowers b2; the map descends by μ_*O=O. The resulting q0 satisfies q=q0τ and agrees on the marked smooth fibres away from finitely many values. Inclusion from the base with these extra values removed surjects on the fundamental group of the full smooth base of q0. P306 is then applied to this exact relatively minimal q0. Its complete full-fibre root, canonical-intersection, Kodaira-type, period and invariant-coefficient arguments give smooth multiple fibres, fixed Jacobian and R1(q0)_*O=O_B.

The original UN66 paragraph claimed smooth multiple supports directly for any such component, although its argument only supplied that conclusion after relative minimization. P260 states the relative-model conclusion precisely. For its conclusions on the original T, the proof retains μ_*O=O by Hartogs and proves R1μ_*O=0 on the two Stein blowup charts. On their annular overlap the normally convergent Laurent monomial x^m v^n extends to the first chart for n≥0 and becomes y^m u^(m−n) for n<0. Shrinking and Cauchy estimates give a convergent coboundary; the direct-image stalk vanishes. Leray transfers the entire direct-image line back to q. The freshly opened Peters p.8 supplies global pg/χ invariance only, and is not credited with this local sheaf computation. UN28 gives pg(T)≤1 on this same smooth normalization component.

## UN66: full contractions, normal extensions and Euler conclusions

The complete statement is preserved: the minimal-or-projective-bundle class, including F1; all four possible cores; reversal of the actual neighbourhood maps and every normal extension; absence of rational components; exact negative Euler formula; elliptic-centre zero case; the converse construction; and the broader nonminimal/all-elliptic-double-curve theorem with its exact zero criterion.

The canonical generator now applies UN17 to the same family with all multiplicities one, identity normalization/resolution and intrinsic conductor zero. Its CA3/CA4 maps give the unchanged MR3 coefficient k_w−k_v−1. The same formula remains valid for the final triple-point extension. All maximum-order degree partitions, ruled and plane alternatives, Hopf canonical-height/axis cases, equal-order propagation, and finite-normal Hopf-leaf alternative remain complete.

P260 applies to the same elliptic q,T,B. The receiving proof explicitly proves that its relative contraction is the identity on the minimal components and on projective-line bundles over an elliptic curve: every rational curve in the latter is a ruling fibre and has square zero. Thus the smooth-multiple conclusion is applied to q itself only on these verified component types.

The ruled torsion-normal section now has a complete lines-projectivization comparison. For the finite unramified pullback p:T′→C, the diagonal section has the original normal L. Put W=p_*O(C); fibrewise evaluation gives T′=P(W*). The pushed restriction sequence is 0→O→W→L→0. Dualizing and tensoring by L gives V=W*⊗L and the unchanged MR10 sequence 0→O→V→L→0. The section's dual evaluation L^-1→W* becomes O→V, so the marked section is P(O) and has normal L. The nontrivial torsion splitting, trivial-line additive-torsor finite trace, further étale cover, constant PGL2 deck action, quotient MR11 and all boundary identifications remain.

In the nonruled branch the degree-one UN31 map, torus quotient, canonical power MR12, κ=1 verticality and all Euclidean multiplicity lists remain. P330 is applied first to the principal T→B0 over an elliptic base after horizontal C makes its Chern class vanish. In the P1-base branch the original proof continued with parallel elliptic translates on T′ even though it had only proved T′ was a torus under the horizontal-C condition. The receiving proof settles vertical C at once, using the smooth irreducible fibre support and disjointness, and explicitly retains horizontal C for the rest. The same Euclidean base map, finite étale normalized pullback and positive-degree Chern map then prove c=0 on T′→E. P330 identifies that exact torsor as a torus. Its parallel translates and descended MR14 quotient now have all their hypotheses established. P260 applies to precisely MR14 on minimal T, through τ=identity.

The finite-normal propagation, simultaneous pg bound, simply connected graph for the genus-one root, genus-zero unicycle argument, and complete UN61/UN62 necessary tests remain. Their application is to the same final ordinary-blowdown family, with its actual components, boundary fibres, normal lines and analytic torsors. The proof then excludes rational boundaries, shows a rational contraction cannot remove the last rational component, and counts every higher-genus ruled component once. The unchanged EL5 Euler comparison proves MR1. Every elliptic-centre normal extension, reverse neighbourhood map, converse ordinary blowup and proper punctured family remains.

The final broader extension retains the exclusion of higher-genus ruled minimal models, the exact component minimal-model/Euler comparisons and MR16 with its triple term t. Its nonnegative terms prove both directions of the stated zero criterion. The program body path is removed only to separately prepared appendix158; no program execution is claimed.

## UN67: the nonminimal rational component

The obstruction statement and every Hopf interface/parent conclusion remain, including rational double curves and triple points away from the marked interface. The complete RH1–RH6 proof is retained: torsion-normal divisor restriction, cohomology induction, a basepoint-free pencil with fibre mJ, the finite Stein factor, the exact order forcing d=1, and adjunction giving a connected elliptic general fibre. Intersection with mJ proves every other boundary vertical.

P260 is applied to this original P and this exact q:P→P1. RH7 is its genuine vertical contraction. The point-blowup comparison preserves χ=1. P306's local root is specialized with m=a and identical u,h,w,s in RH8; its full multiple-fibre descent gives the unchanged RH9. Coherent Leray forces χ=0, the contradiction. The former long duplicate proof of relative minimality upstairs and invariant full-fibre coefficients now has one owner at P306, whose complete proof remains in the paper.

The Hopf interface proof is unchanged in content: finite normal orders from the exact root/axis maps, disjoint Hopf curves excluding a triple point there, the xy=t tensor product in RH10, and the torsion-normal obstruction on P. The terminal-pair characterization supplies the parent exclusion. No relative-minimal claim is applied to the original nonminimal P.

## P330, the K3 receiver and both UN61 receivers

P330 is extracted from the complete K3 KX13–14 and UN61 PT7–8 constructions. Its exact domain is a principal F1=C/ΛF1 torsor over the given elliptic B=C/Γ, with zero integral Chern class. The sheaf sequence, lift to H1(B,O), constant Dolbeault representative a dbar z, additive periods a bar γ, and rank-four lattice proof are retained. The projection remains the first coordinate and the principal action remains second-coordinate translation.

The original K3 prose identified the difference of transition systems with a zero-cochain. The receiving proof states the correct coboundary equation g_E−g_model=c_j−c_i. In the specified convention w_j=w_i+g_ij, the local maps w_i↦w_i+c_i glue from the model to E1, and translations by −c_i are the inverse. This proves the exact total-space isomorphism over B and compatibility with the principal action; no analytic torsor class is discarded.

The entire original and receiving K3 statements/proofs were read. Its equivariant Chern cocycle c=βc, invertibility of β−I and torsion-free lattice still prove c=0 first. The new receiver then applies P330 to this very q1:E1=E0/H→B and F1. All remaining finite-group, canonical-character, full multiplicity, fixed-point table, elliptic-pencil and compact realization arguments are unchanged. The full guard changes only the general torsor block and the hidden owner dependency.

The entire original and receiving UN61 statements/proofs were also read. Its first concrete application uses E1=P, B and F after a horizontal elliptic curve trivializes a finite base pullback and positive degree kills the original Chern vector. Its second uses E1=T0 after the actual inverse torsor has π1=Z4 and the injected fibre lattice makes the clutching commutator zero. P330 preserves each complete analytic torsor over B. PT7/PT8 keep their permanent targets at the identical KX equations under F=F1, ΛB=Γ and identity (z,w). Every root incidence map, dualizing-form calculation, height equation, inverse chart, collar group map, period family, compactness estimate and compact reconstruction remains unchanged outside those bounded transfers. The full sec10 unit remains open for its upcoming rewrite.

## Status and placement

The package has 110 per-instance defects, six exposed events, eight owner/conclusion maps, six dependency maps, four actual units and 104 criterion rows, one fresh primary-source row, 28 old-tag mappings and three exact remote guards. P330's own local order and restructuring are complete. P260/UN66/UN67 have their required local order, but D14 and structure remain open until root moves UN64–68 after sec10. Source-wide D18 and final integrated-page D23 remain open; D10/D16 stay done. The known later P326 collar applications are explicitly open section10 work, with P326's earlier placement owned by root. No manifest, seal, receipt, inventory difference or census refresh is made.
'''
(out/(prefix+'_comparison.md')).write_text(comparison,newline='\n')
report=f'13 READY: {len(rows)} per-instance defects; {len(events)} exposed proof events; {len(maps)} owner maps; {len(deps)} dependencies; {len(statuses)} criterion rows across four actual subsections; 28 old-tag identities; all26 main formula payloads unchanged; KX13/KX14 payloads unchanged; all old labels/targets preserved; main and all3 remote guards match once. Tags used P260/P330. LF verified. No central source edits.\n'
for p in out.glob(prefix+'*'):
    if p.is_file():assert b'\r' not in p.read_bytes(),p
(root/'code'/('S6_SERIES_PUBLISH_c3_conductor_13.out')).write_text(report,newline='\n')
print(report,end='')
