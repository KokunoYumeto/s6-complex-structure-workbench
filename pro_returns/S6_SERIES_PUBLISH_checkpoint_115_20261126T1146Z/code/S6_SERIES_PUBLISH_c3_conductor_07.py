#!/usr/bin/env python3
"""Prepare full rank-two and cyclic quotient units from a bounded input; no central edits."""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import csv,re

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'agents/continuation3_conductor'
PRE='S6_SERIES_PUBLISH_c3_conductor_07'
original=(OUT/(PRE+'_input.tex')).read_text()
rows=[]

def log(kind,owner,old,new,reason):
    rows.append(dict(change_id=f'II-C3-UNRESTRICTED07-{len(rows)+1:04d}',type=kind,statement_id=owner,
        old_location=f'pre-admission owner {owner}; exact bounded source span',old_page='cp35 PDF omitted; exact source span supplied',
        new_location=owner,new_page='pending integrated final PDF',old_text=old,new_text=new,reason=reason,
        review_status='Complete original and receiving proof read and compared; exposed editorial rereading; integrated PDF reading remains open.'))
def replace(text,old,new,kind,owner,reason):
    assert text.count(old)==1,(owner,old[:100],text.count(old))
    text=text.replace(old,new,1);log(kind,owner,old,new,reason);return text
def item(text,start,end):
    a=text.index(start);b=text.index(end,a);return text[a:b]

start22=original.index(r'\begin{proposition}')
start23=original.index(r'\begin{proposition}',start22+1)
u22=original[start22:start23].strip()
end23=original.index(r'\end{proof}',start23)+len(r'\end{proof}')
u23=original[start23:end23]
orphan=original[end23:].strip()
p1a=u22.index(r'\begin{proof}')
p1b=u22.index(r'\end{proof}',p1a)+len(r'\end{proof}')
p1=u22[p1a:p1b]
p2=u22[u22.index(r'\begin{proof}',p1b):]
st22=u22[:p1a].strip()

elliptic_statement=r'''\begin{lemma}[Elliptic first integrals of commuting fields]\hypertarget{tag-P303}{}\label{lem:II:elliptic-first-integral}
\StatementRecord{lem:II:elliptic-first-integral}{proved}{P303}{\cref{lem:II:semicomplete-transport}; \cite[Theorem~6.2, pp.~564--566; \S8(iv)(11), p.~585]{Kodaira1963II}; \cite[\S2.3, arXiv v2 pp.~5--6]{UlmerUrzua2021}}
Let $X$ be a smooth compact complex surface and let $V,Y$ be commuting meromorphic vector fields with $V\wedge Y\ne0$, each semicomplete on its holomorphic locus. Resolve the graph of a meromorphic first integral of $V$ and take its Stein factorization
\[
 q:\widehat X\longrightarrow B
 \tag{C.RF.1}\hypertarget{tag-00YU}{}\label{cdp:eq:C.RF.1}
\]
with connected elliptic general fibre. There is a relatively minimal elliptic fibration $q_0:X_0\to B$ obtained from $\widehat X$ by vertical point blowdowns, with $g(B)\le1$, identity integral $H_1$ monodromy, and every fibre a positive multiple of a smooth elliptic curve. Its smooth fibres are torsors under one fixed elliptic curve. Moreover,
\[
 e(X_0)=K_{X_0}^2=\chi(\OO_{X_0})=\chi(\OO_X)=0.
\]
\end{lemma}
'''
elliptic_proof=p1.replace(r'\begin{proof}[The elliptic-first-integral step in \ref{cdp:st:C.2.UN.22}]',r'\begin{proof}',1)
setup=item(elliptic_proof,r'\item Let $X$',r'\item First, $V$')
new_setup=r'''\item Lift the two fields to $\widehat X$. Their brackets vanish on the common open isomorphism with $X$ and hence as meromorphic fields everywhere. Their semicompleteness on the full holomorphic loci follows from \cref{lem:II:semicomplete-transport}.

'''
elliptic_proof=replace(elliptic_proof,setup,new_setup,'D12','lem:II:elliptic-first-integral','The entire first-integral setup, including C.RF.1 and its compact analytic scope, moves to the statement of its own lemma. The remaining opening maps the lifted fields through the earlier birational semicompleteness owner.')
log('D02','lem:II:elliptic-first-integral',r'''The proof below does
not require $X$ to be K\"ahler.''',r'''Let $X$ be a smooth compact complex surface''','The positive compact-complex-surface hypothesis in the extracted statement carries the original analytic scope; the negative hypothesis disclaimer is removed.')
elliptic_proof=replace(elliptic_proof,r'''The time-form argument in \ref{cdp:st:C.2.UN.16} excludes poles
on $F$.''',r'''Apply the compact-curve clause of \cref{lem:II:semicomplete-transport} to $V|_F$; it excludes poles on $F$.''','D12','lem:II:elliptic-first-integral','The exact invariant compact elliptic fibre is supplied to the earlier no-poles owner; the following nowhere-zero translation flow and polar-divisor invariance remain.')
elliptic_proof=replace(elliptic_proof,r'''\item The projected field has no pole.  To verify this without
an unproved descent assertion about semicompleteness,
suppose that $Z$ has a pole of order $r\ge1$ at $b$.''',r'''\item Suppose that $Z$ has a pole of order $r\ge1$ at $b$.''','D02','lem:II:elliptic-first-integral','The complete inverse-time primitive and compact path-lifting contradiction are retained; the introductory defense against an unproved descent assertion is removed.')
old_cite=r'''\cite[Theorem~6.2, pp.~564--566; Section~8(iv)(11), p.~585]{Kodaira1963II}, together with the explicit positive-loop matrices in \citet[Section~2.3, pp.~5--6]{UlmerUrzua2021},'''
new_cite=r'''\cite[Theorem~6.2, pp.~564--566; \S8(iv)(11), p.~585]{Kodaira1963II}, together with the positive-loop matrices in \cite[\S2.3, arXiv v2 pp.~5--6]{UlmerUrzua2021},'''
elliptic_proof=replace(elliptic_proof,old_cite,new_cite,'D18','lem:II:elliptic-first-integral','Kodaira proper analytic setup and the cited classification statement/identity-monodromy clause were freshly opened in a reproduction of the original paper. Ulmer–Urzua arXiv:2002.01906v2 was downloaded and its entire local table visually read; the receiving locator names that exact version.')
elliptic_proof=replace(elliptic_proof,r'''now shows that every fibre has smooth elliptic support.
Here is the comparison for multiplicities, to specify
the use of the table.''',r'''gives the following local comparison. A component of coefficient one in a full fibre has a smooth point away from the other components at which the family is a submersion. The holomorphic submersion theorem gives a local section $\sigma$ over a smaller disc. On each smooth fibre $F_b$, the map $x\mapsto\OO_{F_b}(x-\sigma(b))$ identifies $F_b$ with its Jacobian $\operatorname{Pic}^0(F_b)$, identifying the integral homology local system and its positive-loop monodromy. This gives the local family with a section used in the cited table. Every multiplicity-one fibre in Kodaira's list has a coefficient-one component, so identity monodromy leaves only the smooth type $I_0$ in that case.

For a multiple fibre, use the following root comparison.''','D22','lem:II:elliptic-first-integral','The original table application is made explicit for both cases. Every multiplicity-one Kodaira type has a coefficient-one component; a local section gives the exact Abel–Jacobi fibre map and identical integral local system. The separate multiple-fibre root calculation follows intact.')
scope_old=r'''Among the reduced relatively minimal types in the
cited table, identity monodromy is the smooth type
$I_0$.'''
scope_new=r'''Every component of the reduced central fibre has coefficient one. The same local section and Abel--Jacobi map therefore identify the covering family's integral local system with that of a local Jacobian in the cited table. Among its reduced relatively minimal types, identity monodromy is the smooth type $I_0$.'''
elliptic_proof=replace(elliptic_proof,scope_old,scope_new,'D22','lem:II:elliptic-first-integral','The opened Ulmer–Urzua setup is Jacobian. A local section through a smooth point of the reduced fibre supplies the exact fibrewise identification and the same integral local system; Kodaira supplies the proper analytic local classification. The root cover is not assumed to have a global section.')
elliptic_proof=replace(elliptic_proof,r'''The argument applies to every connected covering
component and makes no connectedness assumption on
the root cover.''',r'''Apply the same argument to each connected covering component.''','D02','lem:II:elliptic-first-integral','The positive componentwise application retains the full disconnected-cover scope without a repeated negative disclaimer.')
elliptic_proof=replace(elliptic_proof,r'''$\mathbb C/\Lambda$.

\item Contract''',r'''$\mathbb C/\Lambda$. Adding back the extra removed regular values preserves trivial monodromy: the inclusion of $B^\circ$ into the full smooth base locus induces a surjection on fundamental groups. The local holomorphic period maps extend across those regular values and agree with the constant period map on the punctured neighbourhoods. Thus all smooth fibres are torsors under the same elliptic curve.

\item Contract''','D22','lem:II:elliptic-first-integral','The original all-smooth-fibres conclusion is matched explicitly to the smaller open set used for the flow: fundamental-group surjectivity and holomorphic continuation extend the same period comparison across the extra regular values.')
elliptic_proof=replace(elliptic_proof,r'''Both sides are interpreted as actual meromorphic
differentials.  Since $V$ is tangent to $q_0$, the''',r'''Since $V$ is tangent to $q_0$, the''','D08','lem:II:elliptic-first-integral','The displayed contraction is already an equality of meromorphic differentials; its tangent-frame existence and uniqueness proof remains in full.')
last_p1=item(elliptic_proof,r'\item No vanishing of $Z$',r'\end{enumerate}')
elliptic_proof=replace(elliptic_proof,last_p1,'','D11','lem:II:elliptic-first-integral','The stated positive-multiple conclusion already includes all multiple smooth fibres. The closing nonassertion and unneeded informal logarithmic-translation comparison are removed; no multiplicity restriction is added.')
elliptic=elliptic_statement+elliptic_proof+'\n'
log('D12','cdp:st:C.2.UN.22',p1,elliptic,'The first of two proof environments is a complete previously proved auxiliary result. It becomes one earlier numbered lemma with exactly its original smooth compact complex surface, commuting fields, semicompleteness and elliptic first-integral hypotheses; its full period, root and canonical calculations remain.')

st22=replace(st22,r'''curve. All actual multiple fibres and their multiplicities
are retained in this conclusion.''',r'''curve.''','D11','cdp:st:C.2.UN.22','The preceding phrase every fibre a positive multiple of a smooth elliptic curve already carries the complete multiplicity conclusion.')
st22=replace(st22,r'''have a K3 or Enriques minimal model. The assertion concerns
the actual specified root-cover component; quotients of that
component are compared separately.''',r'''have a K3 or Enriques minimal model.''','D11','cdp:st:C.2.UN.22','The statement expressly names the covering component E. The following quotient theorem has its own full hypotheses, so the repeated scope disclaimer is removed.')
old_meta=next(x for x in st22.splitlines() if x.startswith(r'\StatementRecord'))
new_meta=r'''\StatementRecord{cdp:st:C.2.UN.22}{proved}{01D0}{\cref{cdp:st:C.2.UN.16,lem:II:elliptic-first-integral,lem:II:semicomplete-transport,lem:II:zero-dimensional-field-surface,lem:II:algebraic-leaf-fibration}; \cite[Main Theorem and the following clarification, arXiv v2 p.~2; Proposition~22, p.~25]{Guillot2019}}'''
st22=replace(st22,old_meta,new_meta,'D14','cdp:st:C.2.UN.22','The targeted nonprinting input declaration follows the exact earlier owners used by the receiving proof; no derived inventory is refreshed.')

commuting_old=item(p2,r'''The bracket identity gives $[Z_1,Z_2]=0$. For nonzero''',r'''Thus $W=V_2-cV_1$''')
commuting_new=r'''For meromorphic fields $Z_1,Z_2$ on a connected curve with $Z_1\ne0$, write $Z_2=hZ_1$ on the open set where $Z_1$ is nonzero. Then $[Z_1,Z_2]=Z_1(h)Z_1$. A vanishing bracket makes the meromorphic function $h$ locally constant and hence constant on the connected curve. Thus
\[
              Z_1(Z_2/Z_1)=0,
              \qquad Z_2=cZ_1\quad(c\in\mathbb C).
                                                               \tag{C.RF.8}\hypertarget{tag-00Z1}{}\label{cdp:eq:C.RF.8}
\]

For any proper curve fibration on a smooth birational model $X'$ of $X$, a smooth rational general fibre $F$ has $F^2=0$ and $K_{X'}|_F\simeq\OO_{\mathbb P^1}(-2)$ by adjunction. Every positive pluricanonical section vanishes on every general fibre and hence on their dense union. This would give $\kappa(X')=-\infty$, contrary to $\kappa(X)\ge0$. Thus every genus-at-most-one fibration obtained below has elliptic general fibre.

'''
log('D14','cdp:st:C.2.UN.22',commuting_old,commuting_new,'The exact commuting-curve identity C.RF.8 precedes its first use in algebraic dimension one. The repeated rational-fibre exclusion is proved once, for the same smooth birational models to which the later cases apply.')

a0=item(p2,r'\item If $a(X)=0$',r'\item It remains to treat $a(X)=2$')
a0_new=r'''\item Suppose $a(X)=0$. Apply \cref{lem:II:zero-dimensional-field-surface} to $X$ and the given two-dimensional commuting semicomplete space $\mathfrak a$. Its minimal model is a two-torus or a Hopf surface. The latter has Kodaira dimension $-\infty$, so $\kappa(X)\ge0$ leaves the torus. Its coherent Euler characteristic is $1-2+1=0$, giving \eqref{cdp:eq:C.RF.5} by birational invariance.

'''
log('D12','cdp:st:C.2.UN.22',a0,a0_new,'The repeated a=0 holomorphic-model, common minimal surface and classification argument applies P301 with exactly the stated field space; the torus/Hopf alternatives and Kodaira exclusion remain explicit.')
a1=item(p2,r'\item We first treat',r'\item If $a(X)=0$')
a1=a1.replace(r'''\item We first treat the nonprojective cases by actual
meromorphic maps. If $a(X)=1$, choose''',r'''\item Suppose $a(X)=1$. Choose''',1)
tail1=r'''A nonzero constant linear combination in $\mathfrak a$
is thus vertical. On the compact general fibre its
semicompleteness excludes poles, so the genus is at most
one; genus zero again contradicts $\kappa(X)\ge0$ by
adjunction. This gives an elliptic fibration and reduces
the case $a(X)=1$ to \eqref{cdp:eq:C.RF.1}--\eqref{cdp:eq:C.RF.4}.'''
tail1new=r'''A nonzero constant linear combination $V\in\mathfrak a$ is therefore vertical. Its lifted restriction to the compact general fibre satisfies \cref{lem:II:semicomplete-transport}, so that fibre has genus at most one and hence is elliptic by the adjunction argument above. Choose a second member $Y\in\mathfrak a$ with $V\wedge Y\ne0$. The fields $V,Y$ and this graph-and-Stein map $q$ satisfy \cref{lem:II:elliptic-first-integral}, which gives all the asserted elliptic-fibration conclusions.'''
a1=replace(a1,tail1,tail1new,'D12','cdp:st:C.2.UN.22','The exact a=1 meromorphic function-field identity C.RF.9 and proper graph descent remain. The curve, rational-fibre and elliptic-first-integral arguments now apply their preceding owners with the selected V,Y and q.')
log('D08','cdp:st:C.2.UN.22',r'''\item We first treat the nonprojective cases by actual
meromorphic maps. If $a(X)=1$, choose''',r'''\item Suppose $a(X)=1$. Choose''','States the algebraic-dimension case directly; the full graph and field construction follows.')

a2=item(p2,r'\item It remains to treat $a(X)=2$',r'\item It remains to treat a Zariski-dense')
a2new=r'''\item Suppose $a(X)=2$. Choose a smooth projective birational model. The bracket and generic rank are preserved on the common open isomorphism, coherent Euler characteristic is birationally invariant, and \cref{lem:II:semicomplete-transport} preserves semicompleteness on the full holomorphic loci. Work on this projective model and choose a basis $V_1,V_2$ of $\mathfrak a$.

When all regular leaves of $V_1$ have algebraic curves as their Zariski closures, apply \cref{lem:II:algebraic-leaf-fibration}. Its graph resolution and Stein map \eqref{cdp:eq:C.SC.6} have rational or elliptic general fibre. The adjunction argument above excludes a rational fibre. Thus \cref{lem:II:elliptic-first-integral} applies to this map and the meromorphic lifts of $V_1,V_2$.

'''
log('D12','cdp:st:C.2.UN.22',a2,a2new,'The original projective passage and all-algebraic-leaves case map to P239/P302/P303 in their exact scopes. The shared incidence construction, compact-curve pole proof and rational-fibre exclusion are not repeated.')
dense=item(p2,r'\item It remains to treat a Zariski-dense',r'\item We prove that the polar')
dense=replace(dense,r'''\item It remains to treat a Zariski-dense leaf of $V_1$.
Semicompleteness supplies the univalent maximal solution
required by \cite[Main Theorem and the clarification immediately
following it, p.~2]{Guillot2019}. On an actual smooth
birational model, either the surface is Abelian, when''',r'''\item A regular leaf not contained in an algebraic curve is Zariski dense in the projective surface. For such a leaf of $V_1$, \cref{def:II:semicomplete-fields} supplies a univalent maximal solution. The projective surface is K\"ahler, so \cite[Main Theorem and the following clarification, arXiv v2 p.~2; Proposition~22, p.~25]{Guillot2019} applies. On a smooth birational model, either the surface is Abelian, when''','D18','cdp:st:C.2.UN.22','Freshly reread the exact Main Theorem/clarification and Proposition22 in Guillot arXiv:1603.02288v2. The receiving paragraph supplies the projective/Kahler and univalent-maximal dense-solution hypotheses explicitly.')
dense=replace(dense,r'''Both lifted fields
remain semicomplete on their holomorphic loci by the same
birational-open comparison and closedness argument used
in \ref{cdp:st:C.2.UN.16}.''',r'''The lifted fields remain semicomplete on their holomorphic loci by \cref{lem:II:semicomplete-transport}.''','D12','cdp:st:C.2.UN.22','The birational-open and closedness comparison has one earlier owner; its hypotheses are the two lifted meromorphic fields on smooth birational models.')
polar=item(p2,r'\item We prove that the polar',r'\item Shrink to a nonempty')
polar=replace(polar,r'''We now rule out such a multisection with the actual finite
maps needed for this conclusion.''','','D08','cdp:st:C.2.UN.22','The full normalized multisection, finite isomorphism torsor and proper product graph construction follows directly.')
finite=item(p2,r'\item Shrink to a nonempty',r'\item It follows that $V_2$')
finite=replace(finite,r'''This argument
also explains the invariant-multisection step in
\cite[\S6.3]{Guillot2019}; no extension of an arbitrary
transcendental horizontal trivialization is being used.''','','D02','cdp:st:C.2.UN.22','The complete finite Weierstrass-coordinate cover and proper algebraic graph already justify the product comparison. The trailing defense and unneeded unpaginated source comparison are removed; no mathematical construction is deleted.')
descent=item(p2,r'\item It follows that $V_2$',r'\item Finally $\chi')
descent=replace(descent,commuting_old,r'''The bracket identity gives $[Z_1,Z_2]=0$, so \eqref{cdp:eq:C.RF.8} gives $Z_2=cZ_1$ for a constant $c\in\C$.
''','D12','cdp:st:C.2.UN.22','The identical ratio derivative C.RF.8 is applied after its earlier proof; its label and formula occur once.')
descent=replace(descent,r'''Apply the
preceding elliptic-first-integral proof to $W,V_1$
and \eqref{cdp:eq:C.RF.6}. It gives the stated relatively minimal
model, fixed period lattice, identity integral monodromy,
and \eqref{cdp:eq:C.RF.5}.''',r'''Apply \cref{lem:II:elliptic-first-integral} to $W,V_1$ and \eqref{cdp:eq:C.RF.6}. Its hypotheses hold by the displayed wedge, constant-linear-combination and commutation identities, so it gives the stated relatively minimal model, fixed period lattice, identity integral monodromy and \eqref{cdp:eq:C.RF.5}.''','D12','cdp:st:C.2.UN.22','The exact W,V1 and elliptic map now apply the unique earlier first-integral lemma, retaining every conclusion of the old preceding-proof reference.')
ending=item(p2,r'\item Finally $\chi',r'\end{enumerate}')
u22_new=st22+'\n\n'+r'\begin{proof}'+'\n'+commuting_new+r'\begin{enumerate}[label=\arabic*.,leftmargin=*]'+'\n'+a0_new+a1+a2new+dense+polar+finite+descent+ending+r'\end{enumerate}'+'\n'+r'\end{proof}'+'\n'
log('D12','cdp:st:C.2.UN.22',p2,u22_new[u22_new.index(r'\begin{proof}'):],'The completion becomes the theorem\'s single proof. Algebraic dimensions 0,1,2 are treated in dependency order; C.RF.8 precedes its first consumer. The complete invariant-multisection finite-cover/product-graph proof is retained, and every transferred general argument is applied with its maps and hypotheses.')

u23_new=u23
u23_new=replace(u23_new,r'''Every positive plurigenus of $Z$ is at most one.''',r'''Every plurigenus $P_m(Z)$, $m>0$, is at most one.''','D22','cdp:st:C.2.UN.23','Names the integer m directly, preserving the existing all-positive-pluridegrees conclusion.')
u23_new=replace(u23_new,r'''For the actual component cover in \ref{cdp:st:C.2.UN.16}, suppose its
minimal model is a two-torus. The quotient by its cyclic
stabilizer, followed by the specified proper birational
comparison to the original normalization, satisfies''',r'''For the component cover in \cref{cdp:st:C.2.UN.16}, suppose its minimal model is a two-torus. The quotient by its cyclic stabilizer and the proper birational maps of \cref{lem:II:cyclic-component-cover} give''','D08','cdp:st:C.2.UN.23','The component specialization names its exact earlier quotient maps and omits process qualifiers; all component/minimal-model hypotheses and conclusions remain.')
u23_new=replace(u23_new,r'''\item We first specify the canonical comparison used in every
case. Resolve the rational lift from $A$ to $Z$:''',r'''\item Resolve the meromorphic map from $A$ to $Z$ over $A/G$:''','D22','cdp:st:C.2.UN.23','The displayed graph gives the precise meromorphic comparison for every compact complex torus, with the same proper maps u and v.')
u23_new=replace(u23_new,r'''\item If the quotient map $A\to A/G$ is ramified along a
curve, its generic local form is''',r'''\item If the quotient map $A\to A/G$ is ramified along a curve, the quotient is smooth at a generic point of its branch image and the local map is''','D22','cdp:st:C.2.UN.23','The smooth branch-image scope from the old closing sentence is placed at the local map where it is used.')
u23_new=replace(u23_new,r'''This conclusion uses the actual ramification map,
including when the quotient is smooth along the
branch image.''','','D11','cdp:st:C.2.UN.23','The preceding local-map paragraph now states the smooth branch-image case positively; the repeated closing scope sentence is removed.')
u23_new=replace(u23_new,r'''the usual bielliptic presentation, without inferring
it only from the numerical invariants.''',r'''the bielliptic presentation.''','D02','cdp:st:C.2.UN.23','The full complementary-subtori isogeny and finite free lift-group construction already prove the product quotient; the numerical-comparison defense is removed.')
u23_new=replace(u23_new,r'''\item For clarity, its simple connectedness follows
through the quotient map as well.''',r'''\item We compute the fundamental group through the quotient map.''','D08','cdp:st:C.2.UN.23','Introduces the retained discrete-fixed-set, stabilizer-killing and rational-plumbing calculation directly.')
u23_new=replace(u23_new,r'''\item The vector $(1/n,r/n)$ is primitive in $N$ and
can be included in a smooth fan subdivision of
the quadrant.''',r'''\item The vector $(1/n,r/n)$ is primitive in $N$: a proper integral divisor of it would have positive first coordinate smaller than $1/n$, whereas every first coordinate in $N$ lies in $(1/n)\Z$. Include its ray in a smooth fan subdivision of the quadrant.''','D22','cdp:st:C.2.UN.23','Supplies the immediate lattice-coordinate reason for the primitive valuation vector at its use, preserving the same ray and Euclidean subdivision.')
component_old=item(u23_new,r'\item We finish with the component comparison.',r'\end{enumerate}')
component_new=r'''\item Use the equivariant resolution of \cref{lem:II:cyclic-component-cover} for the covering component $E$ in \cref{cdp:st:C.2.UN.16}. Its stabilizer $G$ is cyclic, and \eqref{cdp:eq:C.HQ.2} is the proper birational morphism $E/G\to S_i^\nu$. When the minimal model of $E$ is a torus $A$, the same lemma makes the contraction $\rho:E\to A$ equivariant and gives its proper birational quotient map \eqref{cdp:eq:C.HQ.3}. An element acting trivially on $A$ fixes the dense open subset where $\rho$ is an isomorphism and hence acts trivially on $E$. Thus the induced action on $A$ is effective. The maps give
\[
 \begin{array}{ccc}
 E&\longrightarrow&A\\
 \downarrow&&\downarrow\\
 E/G&\longrightarrow&A/G
 \end{array}
 \qquad
             E/G\dashrightarrow S_i^\nu
                                                               \tag{C.CQ.12}\hypertarget{tag-00CM}{}\label{cdp:eq:C.CQ.12}
\]
where the last birational comparison is the morphism \eqref{cdp:eq:C.HQ.2}. Resolve the graph of these proper quotient maps. Pullback and the same Hartogs comparison as in \eqref{cdp:eq:C.CQ.3} identify the pluricanonical spaces of the resulting smooth models. Applying \eqref{cdp:eq:C.CQ.1} therefore gives the stated minimal models of components with nonnegative Kodaira dimension.

'''
u23_new=replace(u23_new,component_old,component_new,'D12','cdp:st:C.2.UN.23','The repeated equivariant minimal contraction and quotient-graph proof applies P240. C.CQ.12 remains verbatim; its dashed comparison is explicitly the already proved proper morphism C.HQ.2. Faithfulness of the induced torus action is checked on the dense isomorphism locus, supplying the general theorem\'s effectiveness hypothesis.')
log('D04','cdp:st:C.2.UN.23',r'''as in
(C.HQ.1)--(C.HQ.3).''',component_new,'The inherited literal equation range is replaced by the exact named cyclic-cover owner and its preserved C.HQ.2/C.HQ.3 labels in the receiving component application.')
log('D11','cdp:st:C.2.UN.23',r'''This statement concerns this
actual torus-cover branch; the separate
rank-one fibration branch is handled by
the different comparison of \ref{cdp:st:C.2.UN.20}.''','','The torus-minimal-model hypothesis is explicit in both the statement and receiving application. The closing comparison with a separate rank-one branch is removed.')
old_meta=next(x for x in u23_new.splitlines() if x.startswith(r'\StatementRecord'))
new_meta=old_meta.replace(r'\SeriesRef{cdp:st:C.2.UN.20}',r'\cref{lem:II:cyclic-component-cover}')
u23_new=replace(u23_new,old_meta,new_meta,'D14','cdp:st:C.2.UN.23','The targeted nonprinting input list now names the cyclic-cover quotient owner used by the torus specialization; the rank-one fibration theorem is not a premise of this proof.')

comparison=r'''\begin{remark}[Projective torus quotients and their linear groups]\hypertarget{tag-P304}{}\label{rem:II:projective-torus-quotients}
\StatementRecord{rem:II:projective-torus-quotients}{proved}{P304}{\cref{cdp:st:C.2.UN.23}; \cite[Theorem~2.1, p.~136; Lemma~3.4, p.~139; Example~2.3, p.~137; Lemma~3.6, pp.~141--142]{Yoshihara1995}}
For an Abelian surface $A$ and a finite group $G$ of automorphisms, let $G_0$ be its translation subgroup. The derivative homomorphism $g\mapsto L_g$ has kernel $G_0$ and image $H\simeq G/G_0$. The classification in \cite[Theorem~2.1, p.~136; Lemma~3.4, p.~139]{Yoshihara1995} describes the birational type of a smooth resolution of the same quotient map $A\to A/G$ in terms of $H$ and the fixed loci. Its Enriques cases have $H$ equal to the Klein four group or the dihedral group of order eight, as in \cite[Example~2.3, p.~137; Lemma~3.6, pp.~141--142]{Yoshihara1995}. For a cyclic group $G=\langle g\rangle$, the image is $H=\langle L_g\rangle$. The Klein four group has three elements of order two, and the dihedral group of order eight is nonabelian, so neither is cyclic. This identifies the projective specialization of \cref{cdp:st:C.2.UN.23} through the identity on $A$ and its quotient morphism, and excludes the Enriques rows of the cited classification.
\end{remark}
'''
log('D13','rem:II:projective-torus-quotients',orphan,comparison,'The orphan literature paragraph becomes one numbered mathematical comparison. The exact derivative morphism, translation kernel and cyclic linear image identify the source\'s H with the projective specialization of the theorem; its noncyclic Enriques alternatives are explicitly excluded.')
log('D18','rem:II:projective-torus-quotients',orphan,comparison,'Freshly opened the primary J-STAGE paper at Theorem2.1 p.136, Example2.3 p.137, Lemma3.4 p.139, and Lemma3.6 with its proof pp.141–142; visually inspected the relevant classification table and group matrices. The full analytic quotient proof is retained for the stated compact complex torus scope; no novelty claim is inferred from the source\'s projective hypothesis.')

for name,owner in [('elliptic','lem:II:elliptic-first-integral'),('u22_new','cdp:st:C.2.UN.22'),('u23_new','cdp:st:C.2.UN.23')]:
    text=globals()[name]
    while (m:=re.search(r'\bactual\s+',text)):
        a=max(text.rfind('\n\n',0,m.start())+2,0);b=text.find('\n\n',m.end())
        if b<0:b=len(text)
        old=text[a:b];new=old[:m.start()-a]+old[m.end()-a:]
        for article_old,article_new in [('an relatively minimal elliptic fibration','a relatively minimal elliptic fibration'),('an section','a section'),('an product isomorphism','a product isomorphism')]:new=new.replace(article_old,article_new)
        log('D08',owner,old,new,'Names the mathematical map, model, section or birational comparison directly, with its corresponding article; the full construction and hypotheses are preserved.')
        text=text[:a]+new+text[b:]
    globals()[name]=text

heading=r'\subsection{Rank-two frames and elliptic fibrations}\label{subsec:II:rank-two-component-frames}'
heading_quotient=r'\subsection{Cyclic quotients of two-tori}\label{subsec:II:cyclic-torus-quotients}'
heading_next=r'\subsection{Rank-one fields on elliptic surfaces}\label{subsec:II:rank-one-elliptic-fields}'
working=heading+'\n\n'+elliptic+'\n'+u22_new+'\n'+heading_quotient+'\n\n'+u23_new+'\n'+comparison+'\n'+heading_next+'\n\n'
log('D14','sec:II:06',original,working,'Two complete subsection units replace the rank-two/quotient cluster. The elliptic-first-integral owner precedes its three applications; the curve identity precedes the algebraic-dimension-one use. The finite quotient has its own subsection, and the following UN.26 rank-one material is isolated under a new still-open heading. Whole-paper main-theorem ordering remains a separate open review.')

with (ROOT/'agents/continuation2_B/D19/S6_SERIES_PUBLISH_II_B2_D19_v1_equation_map.tsv').open() as f:
    established={r['old_tag']:r['target_label'] for r in csv.DictReader(f,delimiter='\t') if r['old_tag']}
for old_tag,target in established.items():
    if not re.fullmatch(r'C\.[A-Za-z0-9.]+',old_tag):continue
    token='('+old_tag+')'
    while token in working:
        p=working.index(token);a=max(working.rfind('\n\n',0,p)+2,0);b=working.find('\n\n',p)
        if b<0:b=len(working)
        old=working[a:b];new=old.replace(token,r'\eqref{'+target+'}',1)
        owner=list(re.finditer(r'\\StatementRecord\{([^}]+)\}',working[:p]))[-1].group(1)
        log('D04',owner,old,new,'The literal inherited equation citation resolves through its preserved label.')
        working=working[:a]+new+working[b:]
working=re.sub(r'\n{4,}','\n\n\n',working)
old_displays={}
for m in re.finditer(r'\\\[.*?\\\]',original,re.S):
    for lab in re.findall(r'\\label\{([^}]+)\}',m.group()):old_displays[lab]=m.group()
equations=[]
def number(m):
    old=m.group();tags=re.findall(r'\\tag\{([^}]+)\}',old)
    if not tags:return old
    assert len(tags)==1
    lab=re.findall(r'\\label\{([^}]+)\}',old)[0];assert established[tags[0]]==lab,(tags[0],lab)
    new=old.replace(r'\[',r'\begin{equation}',1);new=new[:-2]+r'\end{equation}';new=new.replace(r'\tag{'+tags[0]+'}','')
    owner=list(re.finditer(r'\\StatementRecord\{([^}]+)\}',working[:m.start()]))[-1].group(1)
    equations.append(dict(old_tag=tags[0],target_label=lab,statement_id=owner))
    log('D19',owner,old_displays[lab],new,'The same mathematical display, stable label and permanent target use the section equation counter; the owner transfer is recorded separately.')
    return new
working=re.sub(r'\\\[.*?\\\]',number,working,flags=re.S)

def payload(text):
    text=re.sub(r'\\tag\{[^}]+\}|\\label\{[^}]+\}|\\hypertarget\{[^}]+\}\{\}','',text)
    for token in (r'\[',r'\]',r'\begin{equation}',r'\end{equation}'):text=text.replace(token,'')
    return re.sub(r'\s+','',text).rstrip('.,')
new_displays={}
for m in re.finditer(r'\\begin\{equation\}.*?\\end\{equation\}',working,re.S):
    for lab in re.findall(r'\\label\{([^}]+)\}',m.group()):new_displays[lab]=m.group()
for lab,old in old_displays.items():assert payload(old)==payload(new_displays[lab]),('changed display',lab)
for kind in ('label','hypertarget'):
    pat=r'\\'+kind+r'\{([^}]+)\}'
    before=set(re.findall(pat,original));after=re.findall(pat,working)
    assert before<=set(after),(kind,before-set(after))
    assert not [x for x,n in Counter(after).items() if n>1],(kind,'duplicate')
assert Counter(re.findall(r'\\begin\{([^}]+)\}',working))==Counter(re.findall(r'\\end\{([^}]+)\}',working))
assert '\r' not in working
assert not re.search(r'\\tag\{|night:P4R\.13|night:P4\.40|\\eqref\{eq:II:manual:[A-Z]\}',working)
assert working.count(r'\begin{proof}')==3

# Bounded terminology guards clarify the already proved one-dimensional
# algebraic-leaf case used by UN.15 and UN.22; their full proofs are preserved.
current_source=(ROOT/'S6_SERIES_PUBLISH_II.tex').read_text()
for tag in ['P303','P304']:assert r'\hypertarget{tag-'+tag+'}' not in current_source
remote=[]
for ident,old_phrase,new_phrase in [
    ('lem:II:algebraic-leaf-fibration','whose regular solution leaves have algebraic closures.','whose regular solution leaves have algebraic curves as their Zariski closures.'),
    ('cdp:st:C.2.UN.15','When every regular leaf has algebraic closure,','When every regular leaf has an algebraic curve as its Zariski closure,')
]:
    p=current_source.index(r'\StatementRecord{'+ident+'}')
    a=list(re.finditer(r'^\\begin\{(?:proposition|lemma)\}',current_source[:p],re.M))[-1].start()
    b=current_source.index(r'\end{proof}',p)+len(r'\end{proof}')
    old=current_source[a:b]
    new=replace(old,old_phrase,new_phrase,'D22',ident,'Makes explicit the one-dimensional algebraic-curve closure used throughout the already proved Hilbert-incidence construction. The complete current statement/proof was read; every other word, hypothesis, formula and proof paragraph is preserved. This disambiguates algebraic leaves from the Zariski-dense alternative used in the same argument.')
    assert old.replace(old_phrase,new_phrase,1)==new
    remote.append(dict(statement_id=ident,old_text=old,new_text=new,reason='Exact algebraic-curve closure wording; complete receiving proof otherwise unchanged.'))

def tsv(suffix,fields,data):
    with (OUT/(PRE+suffix)).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(data)
(OUT/(PRE+'_replacement.tex')).write_text(working,newline='\n')
with (ROOT/'S6_SERIES_PUBLISH_defects_II.tsv').open() as f:df=next(csv.reader(f,delimiter='\t'))
tsv('_defects.tsv',df,rows)
tsv('_equations.tsv',['old_tag','target_label','statement_id'],equations)
tsv('_remote_repairs.tsv',['statement_id','old_text','new_text','reason'],remote)

owners=[('lem:II:elliptic-first-integral','subsec:II:rank-two-component-frames'),('cdp:st:C.2.UN.22','subsec:II:rank-two-component-frames'),('cdp:st:C.2.UN.23','subsec:II:cyclic-torus-quotients'),('rem:II:projective-torus-quotients','subsec:II:cyclic-torus-quotients')]
with (ROOT/'CHECK_EVENTS.tsv').open() as f:ef=next(csv.reader(f,delimiter='\t'))
now=datetime.now(timezone.utc);events=[]
for ident,unit in owners:
    row={k:'' for k in ef}
    row.update(statement_id=ident,date=now.date().isoformat(),date_utc=now.isoformat(),who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; inherited effort not separately exposed; continuation3 conductor agent',type='used and rechecked in this run',outcome='Read the complete original UN.22 statement and both proofs, the complete UN.23 statement/proof and its source-comparison paragraph; compared each full receiving owner. Preserved elliptic periods and identity monodromy, the etale multiplicity root with a local section for the cited Jacobian table, canonical contraction, all algebraic-dimension cases, finite multisection/product graph, analytic ramification and toric valuations, and stabilizer/plumbing fundamental groups. Applied the admitted semicompleteness, a=0, algebraic-leaf and cyclic-component owners with their exact domains. Primary-source reading scope and versions are documented in the comparison. Exposed editorial rereading only; no independent proof or computation credit; final integrated PDF reading remains open.',event_id='publish:c3:conductor07:'+ident,phase='publication editorial comparison',source_file='agents/continuation3_conductor/'+PRE+'_replacement.tex',source_event_type='used and rechecked in this run',evidence_group='publish:c3:conductor07:'+unit,where=unit)
    events.append(row)
for r in remote:
    row={k:'' for k in ef}
    row.update(statement_id=r['statement_id'],date=now.date().isoformat(),date_utc=now.isoformat(),who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; inherited effort not separately exposed; continuation3 conductor agent',type='used and rechecked in this run',outcome='Read the complete current statement and proof, then compared the full receiving block. The phrase algebraic closures is made precise as algebraic curves being the Zariski closures; this is the one-dimensional closure already used by the incidence construction and its algebraic-leaf application. All other wording, hypotheses, displayed formulas and proof steps are unchanged. Exposed clarification and receiving-proof rereading; no independent credit.',event_id='publish:c3:conductor07:curve-closure:'+r['statement_id'],phase='publication editorial comparison',source_file='agents/continuation3_conductor/'+PRE+'_remote_repairs.tsv',source_event_type='used and rechecked in this run',evidence_group='publish:c3:conductor07:algebraic-leaf-scope',where=r['statement_id'])
    events.append(row)
tsv('_CHECK_EVENTS.tsv',ef,events)
units=[('subsec:II:rank-two-component-frames','Rank-two frames and elliptic fibrations'),('subsec:II:cyclic-torus-quotients','Cyclic quotients of two-tori')]
status=[]
for unit,title in units:
    for n in range(1,26):
        state='done';reason='Complete original and receiving unit read and compared; every local instance found is logged. D10 and D16 remain done.'
        if n==14:state='open';reason='Local owners and their applications are in dependency order; whole-paper placement relative to the main theorem remains under root review.'
        if n==18:state='open';reason='Exact edited primary loci opened and local version/page locators supplied; bibliography-wide admission and checking remain separate.'
        if n==23:state='open';reason='Final integrated typesetting and every page of the candidate PDF remain to be read.'
        status.append(dict(unit=unit,title=title,criterion=f'D{n:02d}',status=state,reason=reason))
    status.append(dict(unit=unit,title=title,criterion='structure',status='open',reason='Local construction-before-consumer order and one proof per result are complete. Whole-paper final placement remains open; following UN.26 begins a separate rank-one subsection and is not credited by this package.'))
tsv('_unit_status.tsv',['unit','title','criterion','status','reason'],status)
transfers=[('cdp:st:C.2.UN.22 first proof','lem:II:elliptic-first-integral','Complete compact analytic elliptic-first-integral argument; C.RF.1–4, projected-pole lifting, fixed periods, full multiplicity root, canonical contraction and chi=0.'),('cdp:st:C.2.UN.22 late proof step','cdp:st:C.2.UN.22 proof opening','C.RF.8 commuting curve ratio identity before its a=1 and dense-leaf uses; one rational-fibre adjunction argument.'),('cdp:st:C.2.UN.22 a=0 case','lem:II:zero-dimensional-field-surface','Exact two-dimensional commuting semicomplete space; torus/Hopf alternative with the retained kappa>=0 exclusion.'),('cdp:st:C.2.UN.22 algebraic-leaf case','lem:II:algebraic-leaf-fibration','Same projective surface and V1; C.SC.6 proper graph/Stein map, then elliptic-fibre specialization.'),('cdp:st:C.2.UN.22 birational and compact-curve uses','lem:II:semicomplete-transport','Exact smooth birational models and invariant compact general fibres.'),('cdp:st:C.2.UN.23 final component step','lem:II:cyclic-component-cover','Same equivariant E, cyclic stabilizer G and torus minimal model A; C.HQ.2/3 specialize in unchanged C.CQ.12.'),('unnumbered Yoshihara comparison','rem:II:projective-torus-quotients','Identity on projective A and same quotient morphism; derivative map with kernel G0 identifies H=G/G0, hence cyclic image.')]
tsv('_owner_transfers.tsv',['original_owner','receiving_owner','content'],[dict(zip(['original_owner','receiving_owner','content'],x)) for x in transfers])
print('Main replacement:',len(original),'->',len(working),'characters; new tags P303 and P304.')
print('Defect rows:',len(rows),'; exposed events:',len(events),'; equation identities:',len(equations),'; owner transfers:',len(transfers),'; status rows:',len(status))
print('Two complete local units; whole-paper structure and final PDF remain open. Next unit begins UN.26.')
print('Two bounded remote wording guards: P302 algebraic-curve hypothesis and UN.15 matching application; complete remaining proofs unchanged.')
print('All original labelled display payloads agree; all labels and permanent targets retained once; three proof environments for three proved results; LF. No central file changed.')
