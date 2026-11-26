"""Complete the cellular object comparisons and exact logarithmic chart direction."""
from datetime import datetime,timezone
import S6_SERIES_PUBLISH_c8_integrate_units as u
import S6_SERIES_PUBLISH_c8_root_units as r
path=u.WORK/'root/cell_presentation.tex'
before=path.read_text();after=before
df,ds=r.table(r.DEFECTS);changes=[]
def edit(suffix,kind,old,new,reason):
 global after
 assert after.count(old)==1,(suffix,after.count(old))
 after=after.replace(old,new,1)
 ident='III-C8-CELL-FOLLOW-'+suffix
 assert not any(x['change_id']==ident for x in ds)
 changes.append(dict(change_id=ident,type=kind,statement_id='maps:src:B.5.1',old_location='cell_presentation before complete publication readback',old_page='pending page concordance',new_location='cell_presentation after exact comparison expansion',new_page='pending final PDF',old_text=old,new_text=new,reason=reason,review_status='exact edit applied; final changed-context reading pending'))
edit('COUNT-MODEL-SCOPE','D20',r'''Replacing the maps by cellular maps on the smaller
torus cell structures gives a finite CW homotopy model with''',r'''Replacing the torus return maps and the attaching maps by
cellular maps on the product torus cell structures gives a
finite CW homotopy model with''','Name both object and arrow replacements actually used for the smaller homotopy model; the homeomorphic polyhedral model and exact cell counts remain unchanged.')
edit('LOG-CHART-DIRECTION','D25',r'''The logarithmic gluing translation is
$\log(s)\Pi v_j/(2\pi i)$.  Its clockwise drift is precisely
$v_j/m_j$.''',r'''Write
$\sigma_j(s)=\log(s)\Pi v_j/(2\pi i)$.
The logarithmic chart map from the filling to the regular bundle is
$\zeta_N\mapsto\zeta_J=\zeta_N+\sigma_j(s)$;
its inverse is $\zeta_J\mapsto\zeta_N=\zeta_J-\sigma_j(s)$.
For $s=\rho e^{-2\pi i\theta/m_j}$ the latter translation has
marked coefficient
$-\log(\rho)v_j/(2\pi i)+\theta v_j/m_j$.
It therefore gives exactly the positive drift in the displayed
boundary chart \cite[Lemma~6.5(ii), pp.~38--39]{mapsAC26}.''','The old positive logarithmic translation has negative clockwise drift; the boundary uses its inverse. Print both actual chart maps and the substitution, preserving the positive boundary chart and every attaching/homology formula. This is one bounded intermediate sign/direction correction, not a changed theorem or independent derivation.')
edit('MERIDIAN-LOCATOR','D18',r'\cite[Lemma~7.1, proof, p.~42]{mapsAC26}',r'\cite[Lemma~7.4, proof, p.~42]{mapsAC26}','The current author-hosted primary text places the complete meridian argument in Lemma 7.4. Its entire argument and logarithmic-chart direction were opened and read; the direct PDF byte fetch returned HTTP403 and is not given a current hash.')
start=after.index(r'\item For the smaller homotopy model')
end=after.index(r'\end{enumerate}',start)
old=after[start:end]
new=r'''\item For the smaller homotopy model put the usual product
cell structure on every torus. First replace each roof map by a
cellular approximation using \cite[Theorem~4.8, p.~349]{mapsHatcher02}.
Here is the comparison on each of the actual mapping-torus pieces.
Write $f_0$ for its roof map ($A_j^{-1}$, $M_0^{-1}$, or
$B_j^{-1}$), $f_1$ for the cellular approximation, and
$H(x,s)$ for the homotopy from $f_0$ to $f_1$.
The map from the old mapping torus to the new one fixes its
marked fibre and sends its cylinder to
\[
 [x,t]\longmapsto
 \begin{cases}
 [x,2t],&0\le t\le1/2,\\
 H(x,2-2t),&1/2\le t\le1.
 \end{cases}
\]
At $t=1/2$ both values are $f_1(x)$, and at $t=1$ the
value is $f_0(x)$, so the quotient relations are respected.
The homotopy inverse uses the same formula with
$H(x,1-s)$. For $U_*$ perform this construction on both
branches; their maps agree on the common fibre.
For $W$ use its face-phase cells directly: the edge maps
$b\mapsto\det(n_k,b)$ take the common phase vertex to the
circle vertex and are cellular on the product torus cells.

Denote these object maps by $e_Y:Y\to Y^c$ and
$p_Y:Y^c\to Y$, for $Y=U_*,W,S_1,S_2,M_0,M_1,M_2$;
on $W$ they are the identity. Their composite homotopies
$H_Y:p_Ye_Y\simeq\operatorname{id}_Y$ and
$K_Y:e_Yp_Y\simeq\operatorname{id}_{Y^c}$ are obtained by
contracting each extra path followed by its reverse.
Explicitly, with $\lambda(v)=\min(2v,2-2v)$, the two
contractions are $H(x,(1-r)\lambda(v))$ and
$H(x,1-(1-r)\lambda(v))$, followed by linear
reparametrization of the remaining cylinder interval.
They fix the marked fibre throughout.

For each of the six arrows $f:E\to Y$ (the $b_j$ and $r_j$),
choose a cellular approximation $f^c:E^c\to Y^c$ of
$e_Yfp_E$, with homotopy $L_f$ from $e_Yfp_E$ to $f^c$.
The endpoint paths for the comparison and its inverse are
\[
 A_f(x,s)=
 \begin{cases}
 e_YfH_E(x,1-2s),&0\le s\le1/2,\\
 L_f(e_Ex,2s-1),&1/2\le s\le1,
 \end{cases}
\]
\[
 B_f(y,s)=
 \begin{cases}
 p_YL_f(y,1-2s),&0\le s\le1/2,\\
 H_Y(fp_Ey,2s-1),&1/2\le s\le1.
 \end{cases}
\]
Thus $A_f$ runs from $e_Yf$ to $f^ce_E$, while $B_f$
runs from $p_Yf^c$ to $fp_E$.
On target pieces use $e_Y$; on the $j$th double-cylinder
prism use
\[
 [x,t]\longmapsto
 \begin{cases}
 A_{b_j}(x,3t),&0\le t\le1/3,\\
 [e_{M_j}x,3t-1],&1/3\le t\le2/3,\\
 A_{r_j}(x,3-3t),&2/3\le t\le1.
 \end{cases}
\]
The endpoint identities give a continuous quotient map.
Its homotopy inverse uses $p_Y$ on target pieces,
$p_{M_j}$ on the middle prism, and $B_{b_j},B_{r_j}$
on the two end thirds with the same orientations.
In the composites, the $L_f$ paths retrace and contract
by the displayed $\lambda$ formula. The square
$(r,s)\mapsto H_Y(f(H_E(x,r)),s)$ interchanges the remaining
endpoint paths. The corresponding reversed prism square gives
the $K_Y,K_E$ contraction in the other composite.
The object homotopies and linear reparametrization of each
remaining prism therefore give the identity; they agree on
the marked fibres and target pieces. This proves the claimed
homotopy equivalence with the cellular double-cylinder model.

The two finite surfaces are mapping tori of $T_L$, with
primitive circle coordinate
$s=m_j\gamma/\gamma(v_j)$, where
$\gamma(v_1)=1$ and $\gamma(v_2)=-1$.
Their matrices are $B_j=A_j|_L$ in the roof convention of
Definition~\ref{mapsIII:def:three-filling-datum}.
The cellular mapping-torus models have counts $(1,4,6,4,1)$.
The counts for $U_*^c$ are $(1,6,14,16,9,2)$, and
each $M_j^c$ has counts $(1,5,10,10,5,1)$.
In \eqref{maps:eq:B.5.4} the quotient honeycomb has two vertices,
three edges, and one hexagon. The surviving phase spaces are
respectively a point, a circle, and a two-torus, giving counts
$(2,3,4,2,1)$ for $W$. Adding these cells and one prism cell
for each boundary cell gives \eqref{maps:eq:B.5.2}.
'''
edit('CELLULAR-OBJECT-AND-ARROW-MAPS','D20',old,new,'Supply the precise cellular replacements of all torus mapping-torus objects, both comparison maps, their retracing homotopies, all six transported arrows and both whole double-cylinder maps. The old actual polyhedral structure and exact count vector remain; the finite-surface circle uses the signed primitive coordinate proved in JC.')
source=u.repairs.SOURCE.read_text()
assert source.count(before)==1
candidate=source.replace(before,after,1)
u.check_permanent_identifiers(source,candidate,set(),set())
path.write_text(after,encoding='utf-8',newline='\n');u.repairs.SOURCE.write_text(candidate,encoding='utf-8',newline='\n')
r.write_table(r.DEFECTS,df,ds+changes)
print('UTC',datetime.now(timezone.utc).isoformat());print('EXACT_DEFECT_ROWS',len(changes));print('CELL_LINES',len(before.splitlines()),len(after.splitlines()));print('ALL_OLD_IDENTITIES_PRESERVED; FINAL_CHANGED_CONTEXT_READING_PENDING')
