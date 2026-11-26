from S6_SERIES_PUBLISH_c3_foundations_sec07_helpers import *

p=Package('pushout','subsec:II:normalization-boundary / before P210')
source=(ROOT/'S6_SERIES_PUBLISH_II.tex').read_text()
fragment=r'''\begin{lemma}[A proper modification and its conductor pushout]\hypertarget{tag-P294}{}\label{lem:II:proper-conductor-pushout}
\StatementRecord{lem:II:proper-conductor-pushout}{proved}{P294}{\cite[Proposition~0.16, p.~15; \S4.G, p.~459; Theorem~1.20, p.~43]{Hatcher2002}}
Let $h:X\to Y$ be a proper continuous surjection of compact Hausdorff spaces, let $C\subset Y$ be closed, and put $A=h^{-1}(C)$. Suppose that $h$ restricts to a homeomorphism $X\setminus A\to Y\setminus C$. Give $X$ and $C$ finite CW structures for which $A\subset X$ is a subcomplex. With $j:A\hookrightarrow X$ and $k=h|_A:A\to C$, the canonical map
\[
 X\cup_A C\longrightarrow Y
\]
is a homeomorphism, and the double mapping cylinder of $j,k$ has this homotopy type. In particular,
\[
 e(Y)=e(X)-e(A)+e(C).
\]
For nonempty connected $X,A,C$, the maps induced by $h$ and by $C\hookrightarrow Y$ give
\[
 \pi_1(Y)\simeq\pi_1(X)*_{\pi_1(A)}\pi_1(C).
\]
When $j_*$ is an isomorphism, the inclusion $C\hookrightarrow Y$ induces an isomorphism on fundamental groups. Its inverse on the image of $\pi_1(X)$ is $k_*j_*^{-1}$, and on $\pi_1(C)$ it is the identity.

For disconnected $A$ or $C$, form the incidence graph with vertices the connected components of $X$ and $C$ and one edge for each connected component of $A$, using $j$ and $k$ for its endpoints. A spanning forest gives a van Kampen presentation: take the free product of the fundamental groups of the vertex spaces, add one stable letter $t_a$ for each edge outside the forest, and impose
\[
 t_a^{-1}j_{a,*}(u)t_a=k_{a,*}(u)
 \qquad(u\in\pi_1(A_a)),
\]
with $t_a=1$ on forest edges and with the vertex paths used to base the two displayed homomorphisms. This presentation is taken separately on each connected component. In particular, for connected $X$ and nonempty $C$, writing $r=b_0(A)$ and $s=b_0(C)$ gives exactly $r-s$ stable letters. The quotient by all vertex groups is the free group $F_{r-s}$.
\end{lemma}
\begin{proof}
The map from $X\sqcup C$ to $Y$, given by $h$ on $X$ and inclusion on $C$, identifies exactly the equivalence classes defining $X\cup_A C$. Outside $C$ this follows from the stated homeomorphism; over $c\in C$, the whole fibre $h^{-1}(c)\subset A$ is identified with the point $c$. The induced map is therefore a continuous bijection. Its domain is compact and its target is Hausdorff, so it is a homeomorphism.

The CW-pair hypothesis gives the homotopy extension property by \cite[Proposition~0.16, p.~15]{Hatcher2002}. Apply the first paragraph of \cite[\S4.G, p.~459]{Hatcher2002} to the diagram $C\xleftarrow{k}A\overset{j}{\hookrightarrow}X$: the canonical collapse from
\[
 M=\bigl(X\sqcup(A\times[0,1])\sqcup C\bigr)
       /\bigl((a,0)\sim j(a),\ (a,1)\sim k(a)\bigr)
\]
to $X\cup_A C$ is a homotopy equivalence. Composing it with the homeomorphism already proved restricts to $h$ on $X$ and to the prescribed inclusion on $C$; thus this equivalence uses the required maps. The two open cylinder halves retract onto $X,C$ and their intersection onto $A$. Mayer--Vietoris \cite[\S2.2, pp.~149--150]{Hatcher2002} therefore gives $e(M)=e(X)+e(C)-e(A)$.

For connected $X,A,C$, Theorem~1.20 of \cite[p.~43, proof pp.~44--46]{Hatcher2002} applied to the same cover gives the displayed pushout of groups with edge maps $j_*,k_*$. When $j_*$ is invertible, the maps $k_*j_*^{-1}$ on $\pi_1(X)$ and the identity on $\pi_1(C)$ agree on $\pi_1(A)$. They define the stated inverse to the homomorphism induced by $C\hookrightarrow Y$.

For several components, base the edge maps by paths in their vertex spaces and collapse a spanning forest of the cylinder paths. Successive applications of the same van Kampen theorem give the displayed presentation: transport along the remaining cylinder path $t_a$ identifies $t_a^{-1}j_{a,*}(u)t_a$ with $k_{a,*}(u)$. This calculation uses the actual edge maps without an injectivity assumption. For connected $X$, surjectivity of $k$ makes the incidence graph connected, with $1+s$ vertices and $r$ edges, so it has $r-s$ edges outside a spanning tree. Killing the vertex groups leaves precisely the free group on these letters.
\end{proof}
'''

p210=block(source,'prop:II:minimal-boundary-complements')
anchor='\n'.join(p210.splitlines()[:2])
p.guard('P294 before P210',anchor,fragment+'\n'+anchor,'Place the complete common topological construction before its first P210 application.')
p.record('D12,D14','lem:II:proper-conductor-pushout','Repeated quotient/cofibration/van Kampen arguments in P210, P4R.3, P4R.7, CR.1 and UN.7; disconnected presentation used in the Hopf conductor calculation.',fragment,'One proved owner keeps the full proper-map fibre identification, cofibration, connected inclusion-induced inverse and disconnected incidence presentation. The stable-letter count is r−s for the connected source, with no injectivity assumption on edge homomorphisms.')

old='The map $h=\\eta\\pi$ expresses $S$ as the topological\npushout of\n'
new=r'''Apply \cref{lem:II:proper-conductor-pushout} to $(X,Y,A,C,h)=(Z,S,D_{\rm red},\Gamma_{\rm red},\eta\pi)$. Proposition~\ref{cdp:st:A.5.16} gives the full preimage equality and the isomorphism of complements. A compatible triangulation of the compact analytic pair $(Z,D_{\rm red})$ makes the inclusion a subcomplex \cite[Theorem~2, p.~464]{Lojasiewicz1964}; the compact conductor curve is triangulable as well. The resulting pushout uses the maps
'''
assert old in p210
p.guard('P210 pushout data',old,new,'State the precise spaces, support equality, complement map and cofibration at the first consumer.')
p.record('D12,D14','prop:II:minimal-boundary-complements',old,new,'The P210 map is exactly h=eta pi, not just its restriction to nonexceptional curves. Its original support hypotheses from A.5.16 verify P294.')
a=p210.index('Indeed $h$ is an isomorphism off these closed sets');b=p210.index('\\begin{equation}\n \\pi_1(S)',a)
old=p210[a:b]
new='The connected clause of that lemma, with $Z$ rational and $D_{\\rm red}$ simply connected as just proved, gives\n'
p.guard('P210 pushout application',old,new,'Retain A.RT.18 and A.RT.19 at their specific conductor maps; apply the earlier general proof.')
p.record('D12','prop:II:minimal-boundary-complements',old,new,'The common quotient and cylinder proof is removed only after its complete receiving P294 proof is supplied; the resulting inclusion-induced group isomorphism and all later conductor-image bounds remain.')
old='by Riemann--Hurwitz. Gluing their finitely many points over\nsingularities identifies the topological curve with a graph\nof simply connected spheres. Its fundamental group is a\nfree group, of rank $b_1(\\Gamma_{\\rm red})$.'
new='by Riemann--Hurwitz. Lemma~\\ref{lem:II:curve-normalization-graph} therefore identifies the fundamental group of this connected curve with the free group of rank $b_1(\\Gamma_{\\rm red})$.'
assert old in p210
p.guard('P210 curve graph application',old,new,'The existing P245 owns the compact-curve graph calculation at the same rational normalization data.')
p.record('D12','prop:II:minimal-boundary-complements',old,new,'Keep the specific Riemann–Hurwitz premise, then apply P245 rather than repeat its point-gluing proof.')

r3=block(source,'night:P4R.3')
a=r3.index(r'\item The normalization morphism $\nu$');b=r3.index(r'\item Proposition~\ref{night:P4R.1}',a)
old=r3[a:b]
new=r'''\item The normalization $\nu:T\to S$ is finite and is an isomorphism away from its conductor. Its nonisomorphism locus is exactly $C$: a normal point is identified with a neighbourhood in the smooth normalization, while every smooth point is normal. Thus $D_{\rm red}=\nu^{-1}(C)$ and the complementary open sets are identified. A triangulation of the compact analytic pair $(T,D_{\rm red})$ makes its inclusion a subcomplex \cite[Theorem~2, p.~464]{Lojasiewicz1964}. Apply \cref{lem:II:proper-conductor-pushout} with $(X,Y,A,C,h)=(T,S,D_{\rm red},C,\nu)$. The three spaces in its connected clause are connected, since $D_{\rm red}$ is the section with rational trees and maps onto $C$. The preceding step gives the required isomorphism on the left edge, so
\[
 \pi_1(S)\simeq\pi_1(T)*_{\pi_1(D_{\rm red})}\pi_1(C)
       \simeq\pi_1(C).
\]
The second isomorphism is induced by $C\hookrightarrow S$, with inverse on $\pi_1(T)$ given by $(\nu|_{D_{\rm red}})_*(j_*)^{-1}$ for $j:D_{\rm red}\hookrightarrow T$.

'''
p.guard('R3 exact connected pushout application',old,new,'Retain the complete higher-genus ruling and boundary-isomorphism arguments, and apply P294 only after checking its exact normalization data.')
p.record('D12,D14','night:P4R.3',old,new,'The complete old/current R3 proof was read. The same finite normalization map and whole conductor give the pushout; its inclusion-induced isomorphism, curve bound and strict positivity remain at R3.')

r7=block(source,'night:P4R.7')
a=r7.index('In the quotient $T\\cup_A C$');b=r7.index('Proposition~\\ref{night:P4R.1}',a)
old=r7[a:b]
new=r'''A triangulation of $(T,A)$ makes $A\subset T$ a subcomplex \cite[Theorem~2, p.~464]{Lojasiewicz1964}. Apply \cref{lem:II:proper-conductor-pushout} with $(X,Y,A,C,h)=(T,S,A,C,\rho)$ to this whole proper map, including its exceptional curves. The curve $C$ is connected as the image of $A$. Since $j_*:\pi_1(A)\to\pi_1(T)$ is an isomorphism by the preceding step, the lemma gives
\[
 \pi_1(S)\simeq\pi_1(T)*_{\pi_1(A)}\pi_1(C)\simeq\pi_1(C).
\]
The inverse is the identity on $\pi_1(C)$ and is $(\rho|_A)_*j_*^{-1}$ on $\pi_1(T)$, as in that lemma.
'''
p.guard('R7 exact resolved pushout application',old,new,'Retain the resolved support equality and complement isomorphism from R6, with every contracted component included in the proper edge map.')
p.record('D12,D14','night:P4R.7',old,new,'The complete old/current R7 proof was read. The identical maps T→N→S, A→T and A→C verify P294. The ruling, genus, boundary group isomorphism, virtual-abelian comparison and e(S)≥0 remain at their original owner.')
old='\nThe curve $C$ is connected as the image of $A$.\nApply \\cref{lem:II:curve-normalization-graph}'
new='\nApply \\cref{lem:II:curve-normalization-graph}'
assert old in r7
p.guard('R7 repeated connectedness sentence',old,new,'Connectedness is now verified before the connected P294 application.')
p.record('D09','night:P4R.7',old,new,'State this input once, at the first point where it is needed.')
p.record('D18','lem:II:proper-conductor-pushout','Compatible triangulation invoked independently in P210, R3 and R7.','The exact old analytic pairs are triangulated at each application; the general owner assumes its subcomplex/cofibration.','The cited Lojasiewicz theorem concerns compatible triangulations of locally finite semi-analytic families in a countable real analytic manifold. The application uses the smooth real analytic surface and its compact analytic boundary; the owner makes no unproved general triangulability assertion about arbitrary compact spaces.')
p.record('D17,D18','lem:II:proper-conductor-pushout','The proposal repeated the standard HEP and van Kampen proofs, including both cylinder homotopies.','Apply Hatcher Proposition 0.16 p.15 and the exact canonical-map statement in Section4.G p.459; apply Theorem1.20 p.43, with its full proof pp.44–46. Retain only the proper quotient identification, comparison of the actual maps, the prescribed group inverse and the disconnected edge-path/count calculation.','Freshly opened the primary Cornell PDF. Read Proposition0.16 and its full proof p.15, Proposition0.18 and full proof p.16, Lemma1.15 and full proof p.35, Theorem1.20 and full proof pp.43–46, Mayer–Vietoris and its chain-complex derivation pp.149–150, Proposition4G.1 and full proof p.458, and the exact HEP pushout paragraph p.459. The general graph construction pp.92–93 was also read; its later injectivity theorem is not invoked. The retained short comparison is required to identify the exact proper quotient maps and noninjective edge homomorphisms used here.')
for row in p.rows:
    if row['statement_id']!='lem:II:proper-conductor-pushout':row['old_location']=row['statement_id']+' / complete current proof'
p.write(fragment)
