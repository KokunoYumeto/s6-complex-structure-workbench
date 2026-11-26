#!/usr/bin/env python3
"""Prepare bounded 02KS P15 changes only; canonical TeX is never written."""
from pathlib import Path
import csv,re
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'agents/continuation9_findings'
s=(ROOT/'S6_SERIES_PUBLISH_III.tex').read_text()
start=s.index(r'\subsection{The three-component cusp}')
end=s.index(r'\subsection{Six primitive original families}',start)
proof=s[start:end]
rows=[]
def add(suffix,locus,old,new,reason):
 assert old!=new
 assert s.count(old)==1,(suffix,s.count(old))
 assert proof.count(old)==1,suffix
 rows.append(dict(change_id='CLAUDE-III-P15-02KS-'+suffix,type='D20',statement_id='maps:src:D.2.18',old_location='Paper III, tag02KS; '+locus,old_page='cp100 source; permanent anchor supplied',new_location='Paper III, tag02KS; '+locus,new_page='pending final build',old_text=old,new_text=new,reason=reason,review_status='Full1361-line three-component-cusp subsection reread; all incident expressions and exact maps checked. Canonical admission and final PDF gate pending.'))

add('COMPONENT-PERMUTATION','original-star Wang comparison',
 r'''is the inverse permutation. If the forward permutation is \(P\),
the two Wang complexes are identified by identity on their targets
and \(-P\) on their sources, since
\((P^{-1}-I)(-P)=P-I\), with source inverse \(-P^{-1}\).''',
 r'''is the inverse permutation. If the forward permutation is \(P_{\rm perm}\),
the two Wang complexes are identified by identity on their targets
and \(-P_{\rm perm}\) on their sources, since
\((P_{\rm perm}^{-1}-I)(-P_{\rm perm})=P_{\rm perm}-I\),
with source inverse \(-P_{\rm perm}^{-1}\).''',
 'The theorem fixes the section P=12G, which is used again after this passage in M=O(P-O). Name the component-permutation operator P_perm. The exact identification P_perm=P_old fixes every permutation of component generators. Its inverse operator, source map -P, source inverse -P^(-1), and Wang chain identity are all propagated unchanged.')

add('LEFT-INVERSE','graph-kernel inverse matrix',
 r'''Its last nine rows \(L\) satisfy \(LK=I\), and on the graph
kernel they give the complete inverse coordinates. In particular

\[
 Lj_0\delta=(-1,0,0,-1,-1,0,0,0,0)^t.
\]''',
 r'''Its last nine rows \({\mathsf L}\) satisfy \({\mathsf L}K=I\),
and on the graph kernel they give the complete inverse coordinates.
In particular

\[
 {\mathsf L}j_0\delta=(-1,0,0,-1,-1,0,0,0,0)^t.
\]''',
 'Name the actual nine-row graph-coordinate matrix mathsf L, leaving the later subgroup L=ZF_0+ZF_1 intact. mathsf L is exactly the same last nine rows of [C_0 K]^(-1); the assignment and its reverse preserve L K=I and the complete coordinate vector, including all signs.')
add('LEFT-INVERSE-TRANSFER','regular-log sweep elimination',
 r'''eliminations, adjoin six identity columns and the rows \(mLj_0\lambda\).''',
 r'''eliminations, adjoin six identity columns and the rows
\(m{\mathsf L}j_0\lambda\).''',
 'Propagate the same graph-coordinate matrix into the later transfer calculation, including the adjacent TeX product mLj_0. Its values, the six identity eliminations and inverse additions are unchanged.')

add('CYLINDER-PREIMAGE','fibre degree-two preimage matrix definition',
 r'''\(\omega=(12,0,0,0,0,-1)\). Define a right-preimage matrix \(P\) by its five columns''',
 r'''\(\omega=(12,0,0,0,0,-1)\). Define a right-preimage matrix
\(P_{\rm cyl}\) by its five columns''',
 'Keep the section P=12G and the component permutation separately named. P_cyl is precisely the existing five-column right-preimage matrix, with every tabulated wedge column retained. The reverse symbol map restores P_old.')
add('CYLINDER-PREIMAGE-IDENTITY','fibre degree-two chain identity',
 r'''Multiplication gives \(B_2P=F\). Together with''',
 r'''Multiplication gives \(B_2P_{\rm cyl}=F\). Together with''',
 'Propagate the same five-column matrix into B_2 P_cyl=F. The resulting image/kernel identification and the two explicit integral quotient maps therefore remain identical.')

add('NORMAL-FRAME','scalar-circle normal-frame matrix',
 r''' U(r,\theta)=\begin{pmatrix}
 \sin\beta(r)e^{-i\theta}&-\cos\beta(r)\\
 \cos\beta(r)&\sin\beta(r)e^{i\theta}
 \end{pmatrix},
\]

where \(\beta=r\) near zero and \(\beta=\pi/2\) on the boundary
collar. The inverse is \(U^*\).''',
 r''' {\mathsf U}(r,\theta)=\begin{pmatrix}
 \sin\beta(r)e^{-i\theta}&-\cos\beta(r)\\
 \cos\beta(r)&\sin\beta(r)e^{i\theta}
 \end{pmatrix},
\]

where \(\beta=r\) near zero and \(\beta=\pi/2\) on the boundary
collar. The inverse is \({\mathsf U}^*\).''',
 'The same circle-quotient calculation uses U as the surviving integral component class. Name the displayed SU(2) frame mathsf U and propagate its conjugate-transpose inverse. The entries are literally unchanged, so its product with that conjugate transpose remains I; the core reversal, orientation and normal exponential are retained.')

qstart=proof.index(r'Let \(Q=X/S^1\), using the smooth normal quotient')
qold=proof[qstart:]
# All49 literal Q occurrences in this bounded passage were individually read.
# There are no Q occurrences in a citation key, label, tag, command or field notation.
assert qold.count('Q')==49
qnew=qold.replace('Q',r'{\mathcal Q}')
add('ORBIT-SPACE','circle quotient through final framed reconstruction',qold,qnew,
 'The theorem fixes Q=G as an elliptic section. Name the orbit space mathcal Q=X/S^1 and propagate all49 occurrences, including Q_0, Q-prime, tangent bundles, relative groups, embeddings, oriented diffeomorphism, localized link pair and every twisted suspension. The exact map from Q_old to mathcal Q sends [x] to the same scalar-circle orbit [x], with identical inverse and orientation. It identifies each named complement and all induced maps. No quotient, isotopy, homology map, classification step or gluing/inverse is removed; the whole passage was read before and after the substitution.')

candidate=s
for row in rows:
 assert candidate.count(row['old_text'])==1,row['change_id']
 candidate=candidate.replace(row['old_text'],row['new_text'],1)
restored=candidate
for row in reversed(rows):
 assert restored.count(row['new_text'])==1,row['change_id']
 restored=restored.replace(row['new_text'],row['old_text'],1)
assert restored==s
for pattern in [r'\\label\{[^}]+\}',r'\\hypertarget\{[^}]+\}',r'\d+']:
 assert re.findall(pattern,candidate)==re.findall(pattern,s)
fields=['change_id','type','statement_id','old_location','old_page','new_location','new_page','old_text','new_text','reason','review_status']
with (OUT/'S6_SERIES_PUBLISH_c9_02KS_notation_defects.tsv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
print(f'{len(rows)} guarded02KS notation rows; full subsection read ({proof.count(chr(10))} lines).')
print('All49 quotient occurrences propagated; exact reverse, numeric literals, labels and targets preserved; canonical TeX untouched.')
