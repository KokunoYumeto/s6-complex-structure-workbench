#!/usr/bin/env python3
"""Prepare exact common blowup owners and complete vertical-modification units."""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import csv,re

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'agents/continuation3_conductor'
PRE='S6_SERIES_PUBLISH_c3_conductor_05'
source=(ROOT/'S6_SERIES_PUBLISH_II.tex').read_text()
rows=[]

def span(ident):
    p=source.index(r'\StatementRecord{'+ident+'}')
    starts=list(re.finditer(r'^\\begin\{(?:proposition|lemma|theorem|corollary|example|remark|cited|definition)\}',source[:p],re.M))
    a=starts[-1].start();b=source.index(r'\end{proof}',p)+len(r'\end{proof}')
    return a,b
def block(ident):
    a,b=span(ident);return source[a:b]
def log(kind,owner,old,new,reason,newloc=None):
    p=source.find(old);line=source[:p].count('\n')+1 if p>=0 else ''
    rows.append(dict(change_id=f'II-C3-UNRESTRICTED05-{len(rows)+1:04d}',type=kind,statement_id=owner,
        old_location=f'pre-admission source line {line}; {owner}',old_page='cp35 PDF omitted; exact source span supplied',
        new_location=newloc or owner,new_page='pending integrated final PDF',old_text=old,new_text=new,reason=reason,
        review_status='Complete original and receiving owner read and compared; exposed editorial rereading; integrated PDF reading remains open.'))
def replace(text,old,new,kind,owner,reason):
    assert old in text,(owner,old[:90])
    text=text.replace(old,new,1);log(kind,owner,old,new,reason);return text
def item(text,start,end):
    a=text.index(start);b=text.index(end,a);return text[a:b]

u2=block('cdp:st:C.2.UN.2');u3=block('cdp:st:C.2.UN.3')
u4=block('cdp:st:C.2.UN.4');u14=block('cdp:st:C.2.UN.14')
boundary=block('lem:II:boundary-blowup-groups')
provisional=r'\subsection{Vertical modifications and component covers}\label{subsec:II:vertical-modification-inputs}'
start=source.index(provisional);stop=source.index(r'\begin{proposition}[No component of a torus degeneration has general-type normalization]',start)
original=source[start:stop]
assert source.count(provisional)==1
_,end3=span('cdp:st:C.2.UN.3');start4,_=span('cdp:st:C.2.UN.4')
orphan3=source[end3:start4].strip()
_,end14=span('cdp:st:C.2.UN.14')
orphan14=source[end14:stop].strip()

# The exact set-theoretic/projective-bundle and integral cohomology maps.
topology=r'''\begin{lemma}[Topology of a blowup]\hypertarget{tag-P234}{}\label{lem:II:blowup-topology}
\StatementRecord{lem:II:blowup-topology}{proved}{P234}{}
Let $Y$ be a connected smooth complex manifold and $Z\subset Y$ a smooth compact centre of complex codimension $r\ge2$. Write $\pi_Z:Y'\to Y$ for its blowup, $j:E_Z\hookrightarrow Y'$ for the exceptional inclusion, $p:E_Z=\PP(N_{Z/Y})\to Z$ for the projection, and $\xi=c_1(\OO_{E_Z}(1))$. The map $\pi_Z$ induces an isomorphism on fundamental groups and the integral cohomology isomorphism \eqref{cdp:eq:C.VR.9}. For every compact analytic subset $S\subset Y$ containing $Z$, its full inverse image $S'=\pi_Z^{-1}(S)$ satisfies \eqref{cdp:eq:C.VR.4}. These conclusions also hold on a compact smooth fibre tube with the centre in its interior and the blowup unchanged on its boundary. For a smooth divisor centre, the blowup is the identity and the formulas hold with $r=1$ and an empty extra cohomology sum.
\end{lemma}
\begin{proof}
For a divisor centre its ideal is invertible; the relative Proj of its Rees algebra is identified with $Y$ by each local generator, and these identifications glue to the blowdown isomorphism. Now take $r\ge2$. The restrictions of the blowup give
\[
 S'\setminus\pi_Z^{-1}(Z)\simeq S\setminus Z,
 \qquad \pi_Z^{-1}(Z)=E_Z=\PP(N_{Z/Y})\xrightarrow{p}Z.
 \tag{C.VR.3}\hypertarget{tag-015Y}{}\label{cdp:eq:C.VR.3}
 \hypertarget{tag-00FP}{}\SsixEquationAliases{\label{cdp:eq:C.EC.2}}
\]
Compatible finite triangulations and Euler additivity with compact supports on the complements give
\[
 \begin{split}
 e(S')-e(S)&=e(\PP(N_{Z/Y}))-e(Z)\\
           &=(r-1)e(Z).
 \end{split}
 \tag{C.VR.4}\hypertarget{tag-015Z}{}\label{cdp:eq:C.VR.4}
\]
Here the projective bundle has fibre $\PP^{r-1}$ of Euler number $r$; the formula uses the full inverse image even where $Z$ meets several components of $S$.

The integral map is
\[
 \begin{split}
 H^q(Y,\Z)\oplus\bigoplus_{i=1}^{r-1}H^{q-2i}(Z,\Z)
   &\longrightarrow H^q(Y',\Z),\\
 (\alpha,\beta_1,\ldots,\beta_{r-1})
   &\longmapsto \pi_Z^*\alpha+
       \sum_{i=1}^{r-1}j_*(\xi^{i-1}p^*\beta_i).
 \end{split}
 \tag{C.VR.9}\hypertarget{tag-0164}{}\label{cdp:eq:C.VR.9}
\]
Blowdown induces a proper continuous bijection $Y'/E_Z\to Y/Z$ and hence a homeomorphism. Tubular neighbourhoods make both pairs cofibrations, so this identifies their relative cohomology. The projective-bundle theorem decomposes $H^q(E_Z,\Z)$ into $\xi^i p^*H^{q-2i}(Z,\Z)$ for $0\le i<r$. The self-intersection map is $j^*j_*\eta=-\xi\eta$, so the extra terms in \eqref{cdp:eq:C.VR.9} map isomorphically, with sign minus, onto the terms with $i>0$. Comparing the relative exact sequences proves surjectivity, with the remaining $i=0$ term supplied by pullback from $Y$. The proper degree-one trace makes $\pi_Z^*$ injective: under Poincar\'e duality with Borel--Moore homology it is the identity $\pi_{Z*}(\pi_Z^*\alpha\mathbin\cap[Y'])=\alpha\mathbin\cap[Y]$. Restriction to $E_Z$ proves independence of the extra summands. This establishes the integral isomorphism, including its torsion groups. On a compact tube the same argument uses relative fundamental classes for its unchanged boundary.

For the fundamental group, choose a tubular neighbourhood of each connected component of $Z$. Its boundary is the sphere bundle $S(N_{Z/Y})$, with simply connected fibre $S^{2r-1}$. The old neighbourhood retracts onto $Z$; its blowup retracts onto $\PP(N_{Z/Y})$, whose fibre $\PP^{r-1}$ is also simply connected. Projection identifies all three fundamental groups with $\pi_1(Z)$, and the two boundary inclusions induce those identifications. Gluing the same exterior by van Kampen therefore proves that $\pi_Z$ induces an isomorphism. The argument applies component by component and also inside a tube.
\end{proof}
'''
old_euler=item(u4,r'\item Let $Z\subset S$',r'\item Choose a smooth point')
old_cohom=item(u4,r'\item For a smooth centre of codimension $r$',r'\item The point blowup adds')
old_component=item(u14,r'\item We specify the component comparison',r'\item Uniruledness is preserved')
log('D12','lem:II:blowup-topology',old_euler+old_cohom,topology,
    'The complete original Euler and integral blowup maps are given one owner, before every consumer. The same map is stated in its manifold and compact-tube domains; the short proof retains integral torsion, Gysin signs and the relative-boundary comparison.',
    'subsec:II:blowup-topology, before specialization-fundamental-group')
log('D12','cdp:eq:C.EC.2',old_component,topology,
    'The exceptional projection is the same map as C.VR.3 with Z=C. Both original equation labels and permanent tags are retained on that single projective-bundle display using SsixEquationAliases.',
    'lem:II:blowup-topology; equation cdp:eq:C.VR.3 with alias cdp:eq:C.EC.2')
log('D17','lem:II:blowup-topology',old_cohom,topology,
    'Retains one short integral/tube proof of the exact pullback-Gysin map. The opened noncompact formula in Meng, arXiv:1811.10500v3 Theorem 1.2 p.2, is for real or complex local systems; the coefficient maps from Z annihilate finite torsion and do not determine the integral invariant used here. The quotient-pair map, integral projective-bundle basis and degree-one trace prove the required form.')

# Marking, component classes and uniruledness now have a numbered definition.
definition_text=u14[u14.index('Fix a proper holomorphic family'):u14.index('For every integer $k$')]
invariance=item(u14,r'\item Uniruledness is preserved',r'\item The newly introduced divisor')
definition=r'''\begin{definition}[Marked torus fillings and component classes]\hypertarget{tag-P235}{}\label{def:II:marked-torus-fillings}
\StatementRecord{def:II:marked-torus-fillings}{proved}{P235}{}
'''+definition_text.replace('Fix a proper holomorphic family','Let a proper holomorphic family',1).replace('of connected complex two-tori.','of connected complex two-tori be fixed.',1)+r'''
Over a compact base curve $B$, a marking away from a finite set $Q\subset B$ is a biholomorphism with a fixed torus family over $B\setminus Q$. The multiset at $b\in Q$ is defined using the components of $(Y_b)_{\rm red}$ in the same way.
\end{definition}
\begin{proof}[Well-definedness]
Two smooth resolutions of the normalization of the same component are bimeromorphic: the closure of the graph of their common dense normal open set, followed by normalization and resolution, has proper birational projections to both surfaces. Uniruledness is preserved by a bimeromorphism $Z'\dashrightarrow Z$. Compose a dominant meromorphic map $C\times\PP^1\dashrightarrow Z$ with the inverse on its dense isomorphism locus and resolve the graph of the composition. This gives a dominant meromorphic map to $Z'$. Applying the same construction to the inverse proves the converse. Hence both the class and its inclusion in $\mathcal E(f)$ are independent of the chosen resolution.
\end{proof}
'''
log('D13','def:II:marked-torus-fillings',definition_text+invariance,definition,
    'The marking, the uniruledness convention and the component multiset are actual definitions and receive one numbered owner. The original graph-composition proof supplies well-definedness; the compact marking is the same restriction over B minus Q already used in UN.14.')

# A single divisor argument replaces the two copies in UN.3 and UN.14.
first_two=item(u3,r'\item We first record the precise birational comparison',r'\item Put')
pluri=orphan14[:orphan14.index('Thus the\nequality applies')].strip()
nonuniruled=r'''\begin{lemma}[Non-uniruled divisors under bimeromorphisms]\hypertarget{tag-P236}{}\label{lem:II:nonuniruled-divisors}
\StatementRecord{lem:II:nonuniruled-divisors}{proved}{P236}{\cref{def:II:marked-torus-fillings}; \cite[\S1.2.4 and Lemma~1.3.1, arXiv v4 p.~6; \S5.4, p.~25]{AKMW2002}}
Let $\phi:M\dashrightarrow N$ be a bimeromorphic map between smooth complex threefolds. It induces a bijection between their compact irreducible divisors whose smooth normalization resolutions are not uniruled, by taking strict transforms; corresponding resolutions are bimeromorphic. For a blowup of a smooth compact point or curve, this correspondence is the strict-transform map, and every new exceptional divisor is uniruled. For holomorphic maps $g:M\to B$ and $h:N\to B$ to a smooth curve with $h\circ\phi=g$ on the domain of $\phi$, corresponding fibre components have the same full-fibre multiplicities. Every smooth compact uniruled surface $Z$ has $H^0(Z,K_Z^{\otimes m})=0$ for $m>0$.
\end{lemma}
\begin{proof}
Fix a compact divisor $P\subset M$ as in the statement. Eliminate the indeterminacies of the inverse map near its compact graph over $P$, using smooth-centre blowups:
\[
 \widehat N\xrightarrow{\ a\ }N,
 \qquad b:\widehat N\longrightarrow M,
 \qquad b=\phi^{-1}a.
 \tag{C.UC.1}\hypertarget{tag-014C}{}\label{cdp:eq:C.UC.1}
\]
The elimination-of-indeterminacy construction in \cite[\S1.2.4 and Lemma~1.3.1, arXiv v4 p.~6]{AKMW2002} gives this diagram; its analytic form is stated in \cite[\S5.4, arXiv v4 p.~25]{AKMW2002}. The graph projections are proper, so its inverse image over $P$ and its image in $N$ are compact. On neighbourhoods of these compact sets finitely many resolution steps suffice; the displayed maps denote the resulting proper modifications there, composed with the inclusions into $M$ and $N$. For proper disc models one can instead shrink the disc about the compact central fibre, with compact centres above that fibre.

The strict transform $\widehat P$ maps birationally to $P$ under $b$. Indeed, the locus near $P$ over which the proper modification $b$ has positive-dimensional fibres is analytic. It cannot contain a divisor: its preimage would have dimension at least three and be a proper analytic subset of the corresponding irreducible threefold. Thus $b$ is finite over a dense open subset of $P$, where a finite modification of the normal manifold $M$ is an isomorphism. If $a$ contracted $\widehat P$, that compact divisor would be the strict transform of an exceptional divisor created at one of the blowups. In dimension three such a divisor is $\PP^2$ for a point centre, or $\PP(N_{C/Y})$ for a smooth curve centre. Its centre is compact, being the image of the compact divisor. Blowing up a divisor is an isomorphism and creates none.

Both displayed exceptional surfaces are uniruled. On affine charts $(u,v)\mapsto[1:u:v]$ gives a bimeromorphism $\PP^1\times\PP^1\dashrightarrow\PP^2$. For a smooth compact curve $C$, tensoring the rank-two normal bundle by a sufficiently positive line bundle supplies two global sections independent at the generic point. Their projectivization gives a bimeromorphism $C\times\PP^1\dashrightarrow\PP(N_{C/Y})$. The well-definedness proof of \cref{def:II:marked-torus-fillings} preserves uniruledness under their further strict transforms. Thus $a$ cannot contract $\widehat P$. Its image is a compact divisor, and the same generic-isomorphism argument for $a$ makes the map birational there. Applying the construction to $\phi^{-1}$ proves the stated bijection.

For a single blowup the restrictions $S_i'\to S_i$ are proper and are isomorphisms away from the lower-dimensional centre. Their normalized resolution graphs give the asserted bimeromorphisms, while \eqref{cdp:eq:C.EC.2} is the exceptional projection just used. At each generic point the blowdown is an isomorphism. Pullback of the local base parameter therefore preserves its vanishing order on the strict transform. For a bimeromorphism over the base, use the two generic isomorphisms in \eqref{cdp:eq:C.UC.1}; equality of the base functions on their common open set gives the same equality of orders.

A dominant meromorphic map $C\times\PP^1\dashrightarrow Z$ pulls back a nonzero pluricanonical section to a nonzero one, because its generic differential has full rank. The pullback is holomorphic away from the finitely many indeterminacy points and extends over them by Hartogs' theorem. On every $\{c\}\times\PP^1$ its line bundle has degree $-2m$, so its restriction vanishes. This contradicts its being nonzero and proves the final assertion.
\end{proof}
'''
log('D12','lem:II:nonuniruled-divisors',first_two+old_component+item(u14,r'\item The newly introduced divisor',r'\item Starting from any marked filling'),nonuniruled,
    'Complete original proofs read. One numbered owner retains elimination of indeterminacy, the codimension-one normality argument, explicit rational and projective-bundle maps, resolution graphs and vanishing-order comparison. UN.3 and UN.14 apply these exact statements.')
log('D13','lem:II:nonuniruled-divisors',pluri,nonuniruled[nonuniruled.index('A dominant meromorphic map'):nonuniruled.index(r'\end{proof}')],
    'The complete formerly orphaned pluricanonical pullback and negative-degree proof becomes the final asserted conclusion of the common uniruled-divisor lemma.')

# UN.4 retains its point/Fermat-quartic constructions, charts and induction.
u4_new=replace(u4,old_euler,r'''\item Apply \cref{lem:II:blowup-topology} to a smooth compact centre $Z\subset S$ of codimension $r$. For $\pi_Z:Y'\to Y$, the new reduced support is the full inverse image $S'=\pi_Z^{-1}(S)$, so the Euler change is \eqref{cdp:eq:C.VR.4}, including intersections with other components.

''','D12','cdp:st:C.2.UN.4','Applies the same full inverse-image map to the earlier Euler owner; every codimension and compactness hypothesis is retained.')
u4_new=replace(u4_new,old_cohom,r'''\item For the same blowdown maps, \cref{lem:II:blowup-topology} gives the integral isomorphism \eqref{cdp:eq:C.VR.9}, with $j$ the exceptional inclusion, $p$ its projection and $\xi=c_1(\OO(1))$. It applies both to the total space and to a compact fibre tube unchanged on its boundary.

''','D12','cdp:st:C.2.UN.4','The complete integral proof is transferred to P234; the receiving application identifies its blowdown, exceptional maps, sign convention and tube domain.')

# UN.14 uses the extracted definition and the exact component maps.
u14_new=replace(u14,definition_text,r'''Use the marked fillings and component multisets of \cref{def:II:marked-torus-fillings} for a fixed proper family $p^\times:\mathcal T^\times\to\Delta^\times$ of connected complex two-tori.

''','D13','cdp:st:C.2.UN.14','The same complete hypotheses and definitions are supplied by the preceding numbered Definition P235.')
first3=item(u14_new,r'\item We specify the component comparison',r'\item Starting from any marked filling')
u14_new=replace(u14_new,first3,r'''\item Each blowup in \cref{cdp:st:C.2.UN.4} has a smooth compact point or curve as centre in the central support. Apply \cref{lem:II:nonuniruled-divisors} to its blowdown. The strict-transform restrictions are bimeromorphisms of the original components, with the same full-fibre vanishing orders; their normalization resolutions correspond. The exceptional projection is \eqref{cdp:eq:C.EC.2}, and its surface is uniruled. The resulting bijection therefore preserves exactly the multiset $\mathcal E(f)$, including repetitions and multiplicities. Iterating these specified maps preserves the same data.

''','D12','cdp:st:C.2.UN.14','The receiving proof matches each constructed point/curve blowup to P236, retaining the exact map, component correspondence, repetitions and full-fibre multiplicities.')

# UN.3 retains all quotient, branch and base-change calculations.
u3_new=replace(u3,first_two,r'''\item We use \cref{lem:II:nonuniruled-divisors} for the compact central divisors of these proper smooth disc models. Its diagram \eqref{cdp:eq:C.UC.1} gives the bimeromorphic correspondence of every component whose smooth normalization resolution is not uniruled.

''','D12','cdp:st:C.2.UN.3','The first two proof items move together to P236; the local proper-disc scope is mapped explicitly before the unchanged constructions and obstructions.')
old_surface='Indeed the first Betti\nnumber of a smooth compact surface is\nunchanged by point blowups: a ball is\nreplaced by the simply connected exceptional\nneighbourhood, and van Kampen gives the\nsame fundamental group. Resolution of a\nsurface bimeromorphism therefore preserves\n$b_1$, whereas $b_1(A)=4$ differs from\nboth values in \\eqref{cdp:eq:C.UC.4}.'
new_surface=r'''Indeed, \cref{lem:II:blowup-topology}, applied to a point centre in a smooth compact surface, identifies its fundamental group with that of its blowup. Resolving a surface bimeromorphism into point blowups therefore preserves $H_1$ and $b_1$, whereas $b_1(A)=4$ differs from both values in \eqref{cdp:eq:C.UC.4}.'''
u3_new=replace(u3_new,old_surface,new_surface,'D12','cdp:st:C.2.UN.3','The exact surface point-blowup group comparison is now an application of P234; it preserves both the rank obstruction and the later integral-torsion obstruction.')
old_cite=r'; \cite[Section~1.2.4 and Lemma~1.3.1]{AKMW2002}'
u3_new=replace(u3_new,old_cite,r', \cref{lem:II:nonuniruled-divisors}','D18','cdp:st:C.2.UN.3','The analytical elimination input and exact source version are owned by P236; the receiving theorem cites that numbered owner once.')
old_exp='elliptic bundle with fibre $\\C^*/q^{\\Z}=E$.\nIt is smooth and proper'
new_exp=r'''elliptic bundle with fibre $\C^*/q^{\Z}$. The map $z\mapsto\exp(2\pi\mathrm i z)$ induces its biholomorphism with $E$: translation by $1$ fixes the exponential, translation by $\mathrm i$ multiplies it by $q$, and its kernel modulo $q^{\Z}$ is exactly $\Z+\mathrm i\Z$.
It is smooth and proper'''
u3_new=replace(u3_new,old_exp,new_exp,'D22','cdp:st:C.2.UN.3','The chosen value q=exp(-2 pi) is justified at its use by the exact exponential map and its period kernel.')
old_parameter='Taking a local\n$m$th root of the unit replaces its\nparameter by one with $t=s^m$.'
new_parameter=r'''Choose a local holomorphic logarithm of $u$ and put $\widetilde s=s\exp((\log u(s))/m)$. Its derivative at zero is nonzero, so it is a coordinate and $t=\widetilde s^{m}$. Denote this new coordinate by $s$ in the following charts.'''
u3_new=replace(u3_new,old_parameter,new_parameter,'D22','cdp:st:C.2.UN.3','Writes the actual local coordinate morphism and invertible derivative underlying the existing finite-base-change calculation.')

# The admitted P4.1 owns the n=1 geometry. Put the existing general n
# calculations before their n=1 specialization, then preserve both obstructions.
item_starts=list(re.finditer(r'\\item ',u3_new));enum_end=u3_new.index(r'\end{enumerate}',item_starts[0].start())
parts=[u3_new[m.start():(item_starts[i+1].start() if i+1<len(item_starts) else enum_end)] for i,m in enumerate(item_starts)]
assert len(parts)==9
geometry_start=parts[1].index('The quotient map')
geometry_stop=parts[1].index('\\[\n                         U|')
geometry_new=r'''The identity on $E\times\Delta$ lifts to the identity on $V$ and identifies the line bundle $L$ of \cref{night:P4.1} with $\OO_V(R)$, with $C=B=E$ and $A=C\times B$. That proposition gives the smooth proper elliptic-bundle quotient. Its fibre is identified with $E$ by $z\mapsto\exp(2\pi\mathrm i z)$: translation by $1$ fixes the exponential, translation by $\mathrm i$ multiplies it by $q$, and its kernel modulo $q^{\Z}$ is exactly $\Z+\mathrm i\Z$. The canonical-section trivialization of the same proposition gives
'''
parts[1]=parts[1][:geometry_start]+geometry_new+parts[1][geometry_stop:]
for row in rows:
    if row['type']=='D22' and row['old_text']==old_exp:row['new_text']=geometry_new
old_n1_geometry=item(u3,r'\item Put',r'\item The strict transform')
log('D12','cdp:st:C.2.UN.3',old_n1_geometry,parts[1],
    'The complete admitted P4.1 statement/proof was read. The identity on the base blowup and equality L=O(R), with C=B=E, identify the exact n=1 quotient and canonical-section marking; its smoothness/properness proof is no longer repeated.')
component_cut=parts[2].index('They meet in a single elliptic fibre')
parts[2]=parts[2][:component_cut]+r'''By \cref{night:P4.1}, $P$ is a primary Kodaira surface and $Q$ is the scalar Hopf surface in the display. They meet in one elliptic fibre $J$, and the map is $xy=t$ along $J$.

'''
old_n1_components=item(u3,r'\item The strict transform',r'\item Neither surface')
log('D12','cdp:st:C.2.UN.3',old_n1_components,parts[2],
    'The component identification and transverse local map are the exact P4.1 application. The full integral group calculation is retained once for P_n and Q_n before its n=1 use; the former equation-range citation is replaced by the actual current owner.')
general_old=parts[7]
general_start=parts[7].index('The canonical section again trivializes')
general_stop=parts[7].index('Each\n$P_n$ contains no rational curve')
general_maps=r'''If $g_{\alpha\beta}$ are the transition functions of $\OO_V(R)$, those of its $n$th tensor power are $g_{\alpha\beta}^n$. The quotient charts are therefore the same products with $E$ as in \cref{night:P4.1}, with these powered translation transitions; the maps to $V$ are smooth and proper. For local coefficients $s_\alpha$ of the canonical section, the ratios $\lambda_\alpha/s_\alpha^n$ agree on overlaps over the punctured disc. They give the product marking \eqref{cdp:eq:C.UC.3} for $U_n$. Its central support is $P_n\cup_J Q_n$, and the local base map along $J$ is still $xy=t$ because the projection to $V$ is a product in these charts.
'''
parts[7]=parts[7][:general_start]+general_maps+parts[7][general_stop:]
log('D12','cdp:st:C.2.UN.3',general_old,parts[7],
    'The general family is compared to the earlier chart construction by the exact tensor-power transitions and canonical-section ratios. Its full local map is identified before the later base-change application.')
split_point=parts[8].index('Integral first homology, including its torsion,')
group_part=parts[8][:split_point].rstrip()+'\n\n'
comparison_part=r'\item '+parts[8][split_point:]
rational_cut=parts[3].index('Thus their resolutions are not covered by')
parts[3]=r'''\item Taking $n=1$ in the preceding curve and group calculations gives $H_1(P,\Z)=\Z^3$, $H_1(Q,\Z)=\Z$, and no rational curves on either surface.
'''+parts[3][rational_cut:]
log('D12','cdp:st:C.2.UN.3',item(u3,r'\item Neither surface',r'\item All these supports'),parts[3],
    'The already proved all-n covering maps and circle-extension presentation supply their n=1 specialization; the non-uniruled divisor and Betti-number obstruction remain complete.')
euler_stop=parts[4].index('\\[\n                    e(P\\cup Q)')
parts[4]=r'''\item The principal elliptic-bundle projections of $P_n$ and $Q_n$ are locally trivial proper bundles, so their Euler numbers are the product of the Euler numbers of base and fibre, hence zero. The intersection $J$ also has Euler number zero. Additivity gives $e(P_n\cup_J Q_n)=0$ for every $n$; at $n=1$ this is
'''+parts[4][euler_stop:]
log('D12','cdp:st:C.2.UN.3',item(u3,r'\item All these supports',r'\item Consider a finite base change'),parts[4],
    'One bundle/additivity argument proves all family Euler values; the original n=1 equation C.UC.5 is retained verbatim as its specialization.')
ordered=[parts[0],parts[1],parts[2],parts[7],group_part,parts[3],parts[4],parts[5],parts[6],comparison_part]
reordered=u3_new[:item_starts[0].start()]+''.join(ordered)+u3_new[enum_end:]
log('D14','cdp:st:C.2.UN.3',u3,reordered,
    'The indexed quotient and complete integral group computations now precede the n=1 obstruction; the finite-base-change chart precedes the infinite-family persistence argument. Every original conclusion and label remains, with one proof of each local calculation.')
u3_new=reordered
u3_new=replace(u3_new,r'both values in \eqref{cdp:eq:C.UC.4}',r'the ranks given by \eqref{cdp:eq:C.UC.10} at $n=1$','D04','cdp:st:C.2.UN.3','Points to the preceding full integral group calculation after the n=1 duplicate is replaced by its specialization.')

log_model=r'''\begin{remark}[Proper models of logarithmic complex tori]\hypertarget{tag-P237}{}\label{rem:II:logarithmic-proper-models}
\StatementRecord{rem:II:logarithmic-proper-models}{proved}{P237}{\cite[\S5.1.1--2, p.~170; Theorems~5.2.1 and 5.3.2, pp.~171 and 180]{KKN2008}}
For a nondegenerate pairing $\langle\ ,\ \rangle:X\times Y\to\mathbb G_{m,\log,S}$ with the admissible monoid presentation of \cite[\S5.1.1--2, p.~170]{KKN2008}, let $A$ be its associated log complex torus over $S$. Here $X$ and $Y$ are the two lattices of the pairing. A complete $Y$-stable fan $\Sigma$ in its associated cone, with finitely many $Y$-orbits, gives
\[
 V(\Sigma)=\bigcup_{\sigma\in\Sigma}V(\sigma),\qquad
 A^{(\Sigma)}=V(\Sigma)/Y\lhook\joinrel\longrightarrow A.
\]
The chart inclusions and the quotient by the lattice action define these maps. The complete fan exists by \cite[Theorem~5.2.1, p.~171]{KKN2008}; \cite[Theorem~5.3.2, p.~180]{KKN2008} makes its quotient a proper log smooth model over the given base. For the fillings in \cref{cdp:st:C.2.UN.3}, the prescribed map on the puncture is \eqref{cdp:eq:C.UC.3}, and the component homology in \eqref{cdp:eq:C.UC.10} obstructs its bimeromorphic extension.
\end{remark}
'''
log('D01','rem:II:logarithmic-proper-models',orphan3,log_model,
    'Replaces narration about a proposed classification route by the exact published chart/quotient construction and the already proved obstruction for the specified punctured identification. The published hypothesis and both morphisms are stated positively.')
log('D03','cdp:st:C.2.UN.3','Statement\n\\ref{cdp:st:C.2.UN.3} refutes that additional requirement\nfor the displayed fillings, even though\nthe punctured family is a product.',
    r'For the fillings in \cref{cdp:st:C.2.UN.3}, the prescribed map on the puncture is \eqref{cdp:eq:C.UC.3}, and the component homology in \eqref{cdp:eq:C.UC.10} obstructs its bimeromorphic extension.',
    'The consequence refers to the proved explicit maps and homology, with no conjectural classification request.')
log('D13','rem:II:logarithmic-proper-models',orphan3,log_model,'The substantive literature scope becomes one numbered remark; the exact published loci were opened before it was written.')
log('D02','cdp:st:C.2.UN.14',orphan14[len(pluri):].strip(),'','The pluricanonical proof is retained in P236 and its general-type implication remains an instance of the unchanged multiset equality. Repeated descriptions of a proposed occurrence problem and of comparisons not asserted are removed.')

# Apply the common owner to the already admitted UN.2 and P246.
old_u2_euler='Each curve blowup increases the Euler number of the central support by $e(C_2)=-2$: its exceptional projective bundle has Euler number $2e(C_2)$ and the intersection with the old component has Euler number $e(C_2)$. Each point blowup increases it by two: the old surface gains one, the exceptional plane contributes three, and their intersection subtracts two. Starting from $e(A)=0$ gives'
new_u2_euler=r'Apply \cref{lem:II:blowup-topology} to the specified curve and point blowdowns. At a genus-two curve the codimension is two, so \eqref{cdp:eq:C.VR.4} gives the increment $e(C_2)=-2$; at a point the codimension is three and the increment is two. Starting from $e(A)=0$ gives'
u2_new=replace(u2,old_u2_euler,new_u2_euler,'D12','cdp:st:C.2.UN.2','The already admitted family applies the earlier full-inverse-image formula at its exact centres and codimensions.')
old_u2_cohom='Excision for the exceptional projective bundle and its hyperplane class identifies the new cohomology summands of a curve blowup with $H^{j-2}(C_2,\\Z)$ in degree $j$. A point blowup adds one generator in degrees two and four. These are free summands, so the full cohomology remains torsion-free, and the $k$ curve and $m$ point blowups give'
new_u2_cohom=r'The map \eqref{cdp:eq:C.VR.9} of \cref{lem:II:blowup-topology}, for each curve blowdown of codimension two, adds $H^{j-2}(C_2,\Z)$ in degree $j$. For each point blowdown of codimension three it adds one generator in degrees two and four. These are free summands, so the $k$ curve and $m$ point blowups preserve torsion-freeness and give'
u2_new=replace(u2_new,old_u2_cohom,new_u2_cohom,'D12','cdp:st:C.2.UN.2','The exact Gysin/pullback isomorphism precedes the application; both specializations, general Betti vector and structure-sheaf calculation stay unchanged.')
old_pi1='For the surfaces, the blowup replaces a four-ball by the disc bundle\nof $\\mathcal O_{\\mathbb P^1}(-1)$, along their common boundary $S^3$.\nBoth inserted pieces and the boundary are simply connected, so van\nKampen gives the surface isomorphism.'
new_pi1=r'For the surfaces, apply \cref{lem:II:blowup-topology} to the point centre, of complex codimension two. Its inclusion and blowdown maps give the stated surface isomorphism.'
boundary_new=replace(boundary,old_pi1,new_pi1,'D12','lem:II:boundary-blowup-groups','The already admitted boundary statement, its full boundary proof and its commuting inclusion maps remain unchanged. The surface point-blowup proof transfers to the earlier P234 owner.')

# Per-instance wording and reference changes within the complete receiving bodies.
for name in ('u3_new','u4_new','u14_new'):
    txt=locals()[name];owner={'u3_new':'cdp:st:C.2.UN.3','u4_new':'cdp:st:C.2.UN.4','u14_new':'cdp:st:C.2.UN.14'}[name]
    for old,new in [('by the same point-blowup\ncomparison already used above','by \\cref{lem:II:blowup-topology} for each point blowup in a resolution'),('This proves that\nthere is no such bimeromorphic comparison.','This proves the asserted nonexistence of a bimeromorphic comparison.')]:
        if old in txt:txt=replace(txt,old,new,'D08',owner,'Uses the named mathematical map or conclusion directly.')
    for m in list(re.finditer(r'(?<![A-Za-z])\\SeriesRef\{([^}]+)\}',txt)):
        old=m.group();new=r'\cref{'+m.group(1)+'}';txt=replace(txt,old,new,'D04',owner,'The statement is referred to by its generated reader-facing number.')
    locals()[name]=txt

heading_mod=r'\subsection{Vertical modifications and component classes}\label{subsec:II:vertical-modification-inputs}'
heading_distinct=r'\subsection{Non-bimeromorphic torus fillings}\label{subsec:II:distinct-torus-fillings}'
heading_next=r'\subsection{Translation fields and component surfaces}\label{subsec:II:component-field-inputs}'
working=heading_mod+'\n\n'+definition+'\n'+nonuniruled+'\n'+u4_new+'\n\n'+u14_new+'\n\n'+heading_distinct+'\n\n'+u3_new+'\n\n'+log_model+'\n\n'+heading_next+'\n\n'
log('D14','sec:II:06',original,working,
    'The complete vertical-modification subsection now orders the marking and divisor invariant before UN.4 and UN.14; the next complete subsection contains all UN.3 constructions and the numbered literature remark. A separate following heading keeps unread component-field owners outside these completed units.')

# Convert the original equation tags, retaining their exact established labels.
with (ROOT/'agents/continuation2_B/D19/S6_SERIES_PUBLISH_II_B2_D19_v1_equation_map.tsv').open() as f:
    established={r['old_tag']:r['target_label'] for r in csv.DictReader(f,delimiter='\t') if r['old_tag']}
original_displays={}
for m in re.finditer(r'\\\[.*?\\\]',original,re.S):
    for lab in re.findall(r'\\label\{([^}]+)\}',m.group()):original_displays[lab]=m.group()
equations=[]
def numbering(text,owner):
    def number(m):
        old=m.group();tags=re.findall(r'\\tag\{([^}]+)\}',old)
        if not tags:return old
        assert len(tags)==1
        lab=re.findall(r'\\label\{([^}]+)\}',old)[0];assert established[tags[0]]==lab
        new=old.replace(r'\[',r'\begin{equation}',1);new=new[:-2]+r'\end{equation}';new=new.replace(r'\tag{'+tags[0]+'}','')
        prior=list(re.finditer(r'\\StatementRecord\{([^}]+)\}',text[:m.start()]))
        exact_owner=prior[-1].group(1) if prior else owner
        equations.append(dict(old_tag=tags[0],target_label=lab,statement_id=exact_owner))
        log('D19',exact_owner,original_displays.get(lab,old),new,'The stable formula/label/target uses the section equation counter; moved formula maps are identified in the owner-transfer rows.')
        return new
    return re.sub(r'\\\[.*?\\\]',number,text,flags=re.S)
topology=numbering(topology,'lem:II:blowup-topology')
working=numbering(working,'subsec:II:vertical-modification-inputs / distinct-torus-fillings')
equations.append(dict(old_tag='C.EC.2',target_label='cdp:eq:C.EC.2',statement_id='lem:II:blowup-topology'))
assert established['C.EC.2']=='cdp:eq:C.EC.2'
projective_display=next(m.group() for m in re.finditer(r'\\begin\{equation\}.*?\\end\{equation\}',topology,re.S) if r'\label{cdp:eq:C.EC.2}' in m.group())
log('D19','lem:II:blowup-topology',original_displays['cdp:eq:C.EC.2'],projective_display,'The same exceptional projection has one equation counter; the original C.EC.2 label and permanent tag remain as exact aliases under Z=C.')
specialization=r'\subsection{The specialization fundamental group}\label{subsec:II:specialization-fundamental-group}'
early=r'\subsection{Topology of blowups}\label{subsec:II:blowup-topology}'+'\n\n'+topology+'\n'+specialization
log('D14','sec:II:08',specialization,early,'The common blowup owner precedes its P246 and sec06 consumers; the existing specialization subsection title, label and complete contents remain unchanged.','subsec:II:blowup-topology')

# Original identities survive exactly once over the proposed replacement and remote edits.
all_old=original+u2+boundary
all_new=working+topology+u2_new+boundary_new
for kind in ('label','hypertarget'):
    pat=r'\\'+kind+r'\{([^}]+)\}'
    before=set(re.findall(pat,all_old));after=re.findall(pat,all_new)
    assert before<=set(after),(kind,before-set(after))
    assert not [x for x,n in Counter(after).items() if n>1],(kind,'duplicate')
for text in (working,topology,u2_new,boundary_new):
    assert '\r' not in text
    assert not re.search(r'\\tag\{|night:P4R\.13|night:P4\.40',text)
    assert Counter(re.findall(r'\\begin\{([^}]+)\}',text))==Counter(re.findall(r'\\end\{([^}]+)\}',text))

def tsv(suffix,fields,data):
    with (OUT/(PRE+suffix)).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(data)
(OUT/(PRE+'_replacement.tex')).write_text(working,newline='\n')
(OUT/(PRE+'_blowup_owner.tex')).write_text(topology,newline='\n')
(OUT/(PRE+'_UN2_receiving.tex')).write_text(u2_new+'\n',newline='\n')
(OUT/(PRE+'_P246_receiving.tex')).write_text(boundary_new+'\n',newline='\n')
remote=[dict(statement_id='sec:II:08',old_text=specialization,new_text=early,reason='Insert the shared blowup subsection before the unchanged specialization subsection.'),
        dict(statement_id='cdp:st:C.2.UN.2',old_text=u2,new_text=u2_new,reason='Apply the exact earlier blowup Euler and integral cohomology maps; all family statements and calculations remain.'),
        dict(statement_id='lem:II:boundary-blowup-groups',old_text=boundary,new_text=boundary_new,reason='The surface point-blowup group proof has one earlier owner; the boundary statement/proof and commuting maps remain.')]
tsv('_remote_repairs.tsv',['statement_id','old_text','new_text','reason'],remote)
with (ROOT/'S6_SERIES_PUBLISH_defects_II.tsv').open() as f:df=next(csv.reader(f,delimiter='\t'))
tsv('_defects.tsv',df,rows);tsv('_equations.tsv',['old_tag','target_label','statement_id'],equations)

with (ROOT/'CHECK_EVENTS.tsv').open() as f:ef=next(csv.reader(f,delimiter='\t'))
events=[];now=datetime.now(timezone.utc)
owners=[('lem:II:blowup-topology','subsec:II:blowup-topology','_blowup_owner.tex'),
 ('def:II:marked-torus-fillings','subsec:II:vertical-modification-inputs','_replacement.tex'),
 ('lem:II:nonuniruled-divisors','subsec:II:vertical-modification-inputs','_replacement.tex'),
 ('cdp:st:C.2.UN.4','subsec:II:vertical-modification-inputs','_replacement.tex'),
 ('cdp:st:C.2.UN.14','subsec:II:vertical-modification-inputs','_replacement.tex'),
 ('cdp:st:C.2.UN.3','subsec:II:distinct-torus-fillings','_replacement.tex'),
 ('rem:II:logarithmic-proper-models','subsec:II:distinct-torus-fillings','_replacement.tex'),
 ('cdp:st:C.2.UN.2','subsec:II:unrestricted-euler-parity','_UN2_receiving.tex'),
 ('lem:II:boundary-blowup-groups','subsec:II:normalization-genus','_P246_receiving.tex')]
for ident,unit,file in owners:
    row={k:'' for k in ef}
    row.update(statement_id=ident,date=now.date().isoformat(),date_utc=now.isoformat(),who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; inherited effort not separately exposed; continuation3 conductor agent',type='used and rechecked in this run',
        outcome='Read the complete original owning statement/proof or transferred paragraphs and compared the complete receiving proof. Checked the exact blowdown, Gysin, fundamental-group, component-resolution and marking maps at their stated domains. Primary AKMW arXiv v4 p.6 and p.25 and KKN pp.170–171/180–181 were opened at their cited loci. Exposed editorial rereading; no independent reproof or computation credit. Integrated PDF reading remains open.',
        event_id='publish:c3:conductor05:'+ident,phase='publication editorial comparison',source_file='agents/continuation3_conductor/'+PRE+file,source_event_type='used and rechecked in this run',evidence_group='publish:c3:conductor05:'+unit,where=unit)
    events.append(row)
row={k:'' for k in ef}
row.update(statement_id='night:P4.1',date=now.date().isoformat(),date_utc=now.isoformat(),who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; inherited effort not separately exposed; continuation3 conductor agent',type='used and rechecked in this run',outcome='Read the complete current admitted P4.1 statement/proof, including both blowup charts, line-bundle frames, quotient properness, canonical-section ratios, primitive Chern calculation and tautological evaluation morphism. Matched C=B=E, the identity on the base blowup and L=O(R) to the receiving UN.3 application. P4.1 itself is unchanged. Exposed reading; no independent reproof credit.',event_id='publish:c3:conductor05:night:P4.1',phase='publication editorial comparison',source_file='S6_SERIES_PUBLISH_II.tex',source_event_type='used and rechecked in this run',evidence_group='publish:c3:conductor05:UN3-P4.1-map',where='sec:II:fibre-classification; receiving application subsec:II:distinct-torus-fillings')
events.append(row)
tsv('_CHECK_EVENTS.tsv',ef,events)

units=[('subsec:II:blowup-topology','Topology of blowups','Complete new subsection and all transferred source proofs compared.'),
 ('subsec:II:vertical-modification-inputs','Vertical modifications and component classes','Complete receiving subsection; original UN.4, UN.14 and all source paragraphs read.'),
 ('subsec:II:distinct-torus-fillings','Non-bimeromorphic torus fillings','Complete UN.3 and the original/receiving literature remark read.'),
 ('subsec:II:unrestricted-euler-parity','Euler parity and projective blowup families','04 unit retained; the complete edited UN.2 proof is reread. The unchanged UN.1 keeps its 04 reading.'),
 ('subsec:II:normalization-genus','Ruled normalizations and conductor genus','03 and root owners retained; full P246 original/receiving proof read. This edit changes only its surface blowup application.')]
status=[]
for unit,title,scope in units:
    for n in range(1,26):
        state='done';reason=scope+' Every newly found local instance is logged; unchanged rows retain their previous readings. D10 and D16 remain done.'
        if n==18:state='open';reason='Exact new primary-source loci opened; inherited bibliography-wide checking remains separate.'
        if n==23:state='open';reason='Integrated typesetting and final PDF page reading remain open.'
        status.append(dict(unit=unit,title=title,criterion=f'D{n:02d}',status=state,reason=reason))
    status.append(dict(unit=unit,title=title,criterion='structure',status='done',reason=scope+' P234 precedes every application; the definition and divisor owner precede their consumers. Apply all remote rows with the main replacement.'))
tsv('_unit_status.tsv',['unit','title','criterion','status','reason'],status)
transfers=[dict(original_owner='cdp:st:C.2.UN.4',receiving_owner='lem:II:blowup-topology',content='C.VR.3, C.VR.4, C.VR.9: exceptional maps, full-inverse-image Euler and integral cohomology'),
 dict(original_owner='cdp:st:C.2.UN.14',receiving_owner='lem:II:blowup-topology',content='C.EC.2 aliases C.VR.3 after the exact centre rename Z=C'),
 dict(original_owner='cdp:st:C.2.UN.14',receiving_owner='def:II:marked-torus-fillings',content='Marked filling, uniruledness, multiset and graph-composition well-definedness'),
 dict(original_owner='cdp:st:C.2.UN.3',receiving_owner='lem:II:nonuniruled-divisors',content='Complete inverse-resolution diagram C.UC.1 and non-contraction argument'),
 dict(original_owner='cdp:st:C.2.UN.14',receiving_owner='lem:II:nonuniruled-divisors',content='Strict transforms, rational exceptional maps, multiplicities and orphaned pluricanonical vanishing'),
 dict(original_owner='cdp:st:C.2.UN.3 / lem:II:boundary-blowup-groups',receiving_owner='lem:II:blowup-topology',content='The induced surface point-blowup fundamental-group isomorphism'),
 dict(original_owner='orphan after cdp:st:C.2.UN.3',receiving_owner='rem:II:logarithmic-proper-models',content='Exact published chart/quotient model and the explicit punctured-map obstruction')]
transfers.append(dict(original_owner='cdp:st:C.2.UN.3 n=1 construction',receiving_owner='night:P4.1',content='The earlier admitted quotient, properness, canonical-section trivialization and component identification are applied via C=B=E and the identity of V and L; P4.1 is unchanged.'))
tsv('_owner_transfers.tsv',['original_owner','receiving_owner','content'],transfers)
print('Main replacement:',len(original),'->',len(working),'characters; new tags P234–P237')
print('Defect rows:',len(rows),'; exposed events:',len(events),'; equation identities:',len(equations),'; status rows:',len(status))
print('Three exact remote actions: early blowup owner, UN.2 application, P246 surface application.')
print('All original labels/targets retained once; original D19 target labels matched; environments balanced; LF.')
print('UN.15 onward is outside completed units, under subsec:II:component-field-inputs. No central file changed.')
