#!/usr/bin/env python3
"""Consolidate the cusp and integral calculations without losing any target."""
from pathlib import Path
import re
from S6_SERIES_PUBLISH_editing import Editor, block, ROOT

e=Editor('V')
removed=[]

# One cusp theorem: the dual map is proved explicitly, not inferred from ranks.
product=block(e.text,'maps:src:E.1.3')
cusp=block(e.text,'night:P1.11')
new=cusp.replace('\\label{night:P1.11}',
 '\\label{night:P1.11}\\hypertarget{tag-02M6}{}\\label{maps:src:E.1.3}',1)
new=new.replace('with ranks $(1,3,9,9,10,3,1)$.',
 r'''with ranks
\begin{equation}
 (b_0,\ldots,b_6)=(1,3,9,9,10,3,1).
 \hypertarget{tag-029T}{}\label{maps:eq:E.6}
\end{equation}''',1)
new=new.replace('\\end{theorem}',r'''Dually, the specialization
$\kappa^*:H^k(C;\mathbb Z)\to H^k(T^6;\mathbb Z)$
has image equal to the full monodromy-invariant lattice.
Its kernel is zero except in degree four, where it is $\mathbb Z$.
\end{theorem}''',1)
dual=r'''\item Every homology group just computed is free, so the universal
coefficient maps identify cohomology with the integral duals of homology.
The transpose of the collapse has image
\[
 \operatorname{im}\kappa^*
 =\operatorname{Ann}(\ker\kappa_*)
 =\operatorname{Ann}\bigl((\bigwedge^kM_0-I)\bigwedge^k\Lambda\bigr)
 =\ker\bigl((\bigwedge^kM_0)^t-I\bigr).
\]
The first equality uses the primitive image of $\kappa_*$: an integral
functional on that image extends to the free central-fibre group.
Passing to saturation preserves the annihilator. The last group is
the full integral cohomology invariant lattice; inverse transpose
has the same fixed subgroup. The kernel of $\kappa^*$ is the
integral dual of $\operatorname{coker}\kappa_*$, giving precisely the
stated degree-four kernel.
'''
end=new.rfind('\\end{enumerate}')
new=new[:end]+dual+new[end:]

# Preserve the branch resolution's extra table once, with an explicit map to
# the retained moment-cell proof; its second complete proof is in the records.
p=re.search(r'\\begin\{enumerate\}[^\n]*\n(.*?)\\item For completeness, the possible higher differential',product,re.S)[1]
p=p.replace('\\item The normalization', 'The normalization',1)
p=re.sub(r'\n\\item ', '\n\n',p)
remark=r'''\begin{remark}[The branch resolution of the Kuhn fibre]
\hypertarget{tag-PV08}{}\label{pub:V:cusp-branch-resolution}
The branch resolution and the moment-cell complex have the following
augmentation. Over a dual cell $D_\eta$ of the Kuhn decomposition,
the angular lattice is $Q_\eta=\mathbb Z^3/L_\eta$ and the branch
indices form the simplex on the vertices of $\eta$. Tensor its
augmented integral simplex complex with $\bigwedge^qQ_\eta$ and
sum over dual cells. The degree-zero augmentation adds branch
coefficients; the higher branch terms map to zero. The incidence
maps $Q_\eta\to Q_\tau$ for cofaces $\tau\supset\eta$ commute
with this augmentation. Inserting the least vertex contracts each
augmented simplex complex. Thus the augmentation is a
quasi-isomorphism to the moment-cell complex of
\cref{night:P1.11}. Taking cohomology of the compact toric branch
intersections first gives the normalization table below.

'''+p+r'''
\end{remark}'''
e.replace(cusp,new+'\n\n'+remark,'D12','Unify the cusp homology and specialization statements by the integral dual of the primitive collapse map; retain the additional branch-table description.','night:P1.11')
e.replace(product,'','D12','The same marked cusp is already treated by night:P1.11. Its independent branch/purity/line-bundle proof is transferred to the check record.','maps:src:E.1.3')
removed.append(('maps:src:E.1.3',product))

# Extract the smooth construction and its only van Kampen proof. All its
# homology and characteristic conclusions move to the single final theorem.
construction=block(e.text,'maps:src:F.2.5')
proof=re.search(r'\\begin\{proof\}\s*\\begin\{enumerate\}[^\n]*\n(.*?)\\end\{enumerate\}\s*\\end\{proof\}',construction,re.S)[1]
items=re.split(r'(?m)^\\item ',proof)
if len(items)!=6: raise ValueError(('smooth construction items',len(items)))
smooth=r'''\begin{lemma}[The marked smooth gluing]
\hypertarget{tag-PV11}{}\label{pub:V:smooth-gluing}
\StatementRecord{pub:V:smooth-gluing}{proved}{PV11}{}
The datum of \cref{pub:V:rank-six-data}, with its two affine caps,
the primitive Kuhn cusp in the marking $S$, and zero additional
translation clutch, gives a closed connected oriented smooth
eight-manifold $M$. It is simply connected, has Euler number six,
and admits an almost complex structure with this orientation.
\end{lemma}
\begin{proof}
\begin{enumerate}[label=\arabic*.,leftmargin=*]
'''
smooth+='\\item '+items[1]+'\\item '+items[2]
smooth+=r'''\item Euler additivity over the base strata gives $\chi(M)=6$:
the regular tori and finite free torus quotients have Euler number
zero, and \cref{night:P1.9} gives six for the cusp.
'''
smooth+='\\item '+items[4]+r'''\end{enumerate}
\end{proof}'''
e.replace(construction,'','D12','Move the construction and van Kampen argument into one preparatory lemma; the integral theorem below includes every homology and characteristic conclusion.','maps:src:F.2.5')
anchor='\\section{The genus-two pencil and the lifted period planes}'
e.replace(anchor,smooth+'\n\n'+anchor,'D14','Prove the marked smooth gluing before constructing its periods.','pub:V:smooth-gluing')
removed.append(('maps:src:F.2.5 rational and characteristic re-proof',construction))

# Separate the integral restriction calculation from its Leray application.
integral=block(e.text,'maps:src:F.2.6')
mat=re.search(r'\\begin\{proof\}\s*\\begin\{enumerate\}[^\n]*\n(.*?)\\end\{enumerate\}\s*\\end\{proof\}',integral,re.S)
its=re.split(r'(?m)^\\item ',mat[1])
if len(its)!=7: raise ValueError(('integral proof items',len(its)))
witness_start=its[5].index('For $k=1,2,3$')
witness=its[5][witness_start:]
calc=r'''\begin{lemma}[The integral restriction complex]
\hypertarget{tag-PV12}{}\label{pub:V:integral-restrictions}
\StatementRecord{pub:V:integral-restrictions}{proved}{PV12}{}
For the marked smooth gluing of \cref{pub:V:smooth-gluing}, the
integral image sheaves $\mathcal S_q$ and the point-supported
restriction kernels have the groups computed below. For $1\le q\le4$,
$H^2(\mathcal S_q)=\mathbb Z/2$; the only nonzero groups in base
degrees zero and one are $H^0(\mathcal S_1)=\mathbb Z$ and
$H^1(\mathcal S_3)=\mathbb Z^3$. Each of the three order-four
torsion suspension generators has nonzero image in the corresponding
global coinvariant group.
\end{lemma}
\begin{proof}
\begin{enumerate}[label=\arabic*.,leftmargin=*]
'''
calc+=''.join('\\item '+it for it in its[1:5])
calc+='\\item '+witness+r'''\end{enumerate}
\end{proof}'''
transgression=block(e.text,'mapsaudit:order-four-torsion-transgression')
e.replace(transgression,calc+'\n\n'+transgression,'D14','Compute the integral stalk maps and global torsion images before their geometric transgression is used.','pub:V:integral-restrictions')

head=r'''\begin{theorem}[Integral homology and the middle form]
\hypertarget{tag-02NW}{}\label{maps:src:F.2.5}
\hypertarget{tag-02NX}{}\label{maps:src:F.2.6}
\hypertarget{tag-02QL}{}\label{night:P1.12}
\StatementRecord{maps:src:F.2.6}{proved}{02NX}{}
The marked smooth gluing $M$ of \cref{pub:V:smooth-gluing} is
three-connected and has torsion-free integral homology with Betti numbers
\begin{equation}
 (1,0,0,0,4,0,0,0,1).
 \hypertarget{tag-02F9}{}\label{maps:eq:F.5}
\end{equation}
It admits an almost complex structure, has signature two, and its
middle integral intersection form is
$3\langle1\rangle\oplus\langle-1\rangle$.
The compact holomorphic realization of \cref{maps:src:F.3.7}
has this same marked smooth type.
\end{theorem}
\begin{proof}
The marked identification in \cref{maps:src:F.3.7} compares its
finite affine actions, cusp fan and overlap maps with the gluing
of \cref{pub:V:smooth-gluing}. The bounded-correction comparison
\cref{pub:V:cusp-smooth-dependence} preserves its collars.
We compute the integral groups of that gluing.
By \cref{pub:V:integral-restrictions} and
\cref{mapsaudit:order-four-torsion-transgression}, the point-supported
torsion classes have differential
\begin{equation}
 d_2[w]=\pm[w]\in L_{q-1}/\operatorname{im}\Delta_{q-1}.
 \hypertarget{tag-02FA}{}\label{maps:eq:F.6}
\end{equation}
The three images are the nonzero global classes, as shown by the
integer witnesses in \cref{pub:V:integral-restrictions}.
'''
last=its[6]
cut=last.index('By \\cref{maps:src:F.2.5},')
last=last[:cut]
deduction=r'''The degree-one row of the same Leray sequence is
\[
 H^0(\mathcal R_1)=\mathbb Z
 \xrightarrow{d_2^{0,1}}H^2(\mathcal R_0)=\mathbb Z.
\]
Its kernel is $H^1(M;\mathbb Z)=0$ by
\cref{pub:V:smooth-gluing}. Its degree is nonzero, so it becomes
an isomorphism over $\mathbb Q$. The image-sheaf groups in
\cref{pub:V:integral-restrictions} give
$H^2(M;\mathbb Q)=H^3(M;\mathbb Q)=0$.
Universal coefficients
\cite[Theorem~3.2 and Corollary~3.3, pp.~195--196]{Hatcher2002}
identify the torsion of $H_2$ and $H_3$ with the corresponding
$\operatorname{Ext}$ subgroups of $H^3$ and $H^4$; both are zero.
Their rational ranks also vanish, so $H_2=H_3=0$.
Integral Poincar\'e duality
\cite[Theorem~3.30, p.~241]{Hatcher2002} gives the remaining groups.
The successive Hurewicz homomorphisms
\cite[Theorem~4.32, p.~366]{Hatcher2002} give $\pi_2=\pi_3=0$.
Finally the almost complex structure and Euler number in
\cref{pub:V:smooth-gluing} satisfy
\cref{sec:V-known-inputs}, which gives the stated signature and
middle form.
\end{proof}'''
e.replace(integral,head+last+deduction,'D12','One integral computation now proves all homology conclusions; its rationalization replaces the separate rational re-proof, and the characteristic proposition supplies the middle form.','maps:src:F.2.6')

# The coefficient-one lemma uses the earlier matrices, not the theorem whose
# conclusion it supports.
tr=block(e.text,'mapsaudit:order-four-torsion-transgression')
newtr=tr.replace('\\cref{maps:src:F.2.6}','\\cref{pub:V:integral-restrictions}')
newtr=newtr.replace('the marked matrices of \\cref{maps:src:F.2.5}','the marked matrices of \\cref{pub:V:rank-six-data}')
e.replace(tr,newtr,'D14','Refer to the preceding integral relation matrices in the transgression proof.','mapsaudit:order-four-torsion-transgression')

# The full compact realization already proves the other compact statement.
compact=block(e.text,'night:P1.10')
filling=block(e.text,'maps:src:F.3.7')
newfill=filling.replace('\\label{maps:src:F.3.7}',
 '\\label{maps:src:F.3.7}\\hypertarget{tag-02QJ}{}\\label{night:P1.10}',1)
statement_end=newfill.index('\\end{theorem}')
statement_start=newfill.index('\n\n',newfill.index('\\StatementRecord'))
oldstatement=newfill[statement_start:statement_end]
newstatement=r'''

For every transverse period parameter of \cref{night:P1.8}, the
marked gluing of \cref{pub:V:smooth-gluing} has a compact smooth
complex realization and a proper holomorphic map to $\mathbb P^1$.
Its regular fibres are complex three-tori; its two finite reduced
fibres are the free affine quotients of orders five and four in
\cref{pub:V:rank-six-data}; its remaining fibre is the index-one
Kuhn degeneration. With its complex orientation its fundamental
group is trivial and its Euler number is six.

'''
newfill=newfill[:statement_start]+newstatement+newfill[statement_end:]
newfill=newfill.replace('The smooth eight-manifold of Theorem \\ref{maps:src:F.2.6}','The marked smooth gluing')
newfill=newfill.replace('Theorem \\ref{maps:src:F.2.5}','\\cref{pub:V:rank-six-data}')
newfill=newfill.replace('Theorems \\ref{maps:src:F.2.5}--\\ref{maps:src:F.2.6}','\\cref{pub:V:smooth-gluing}')
newfill=newfill.replace('is the one whose integral topology was computed there.',
 'is the gluing of \\cref{pub:V:smooth-gluing}. Its fundamental group is trivial and its Euler number is six by that lemma.')
e.replace(filling,newfill,'D12','Merge the two compact-realization theorems and use the one van Kampen calculation in the preparatory smooth-gluing lemma.','maps:src:F.3.7')
e.replace(compact,'','D12','The single compact-realization statement now contains this parameter range and all its topological conclusions.','night:P1.10')
removed.append(('night:P1.10 repeated compact construction',compact))

e.save()
with (ROOT/'records/S6_SERIES_PUBLISH_V_removed_independent_proofs.tex').open('a') as f:
 for label,text in removed:
  f.write('\n% Retained as checking evidence: '+label+'\n'+text+'\n')
