"""Resolve the matrix/boundary notation and final readback locators in the cell unit."""
from datetime import datetime,timezone
import S6_SERIES_PUBLISH_c8_integrate_units as u
import S6_SERIES_PUBLISH_c8_root_units as r
p=u.WORK/'root/cell_presentation.tex';before=p.read_text();after=before
fields,rows=r.table(r.DEFECTS);changes=[]
def edit(suffix,kind,old,new,reason):
 global after
 assert after.count(old)==1,(suffix,after.count(old))
 after=after.replace(old,new,1)
 ident='III-C8-CELL-NOTATION-'+suffix
 assert not any(x['change_id']==ident for x in rows)
 changes.append(dict(change_id=ident,type=kind,statement_id='maps:src:B.5.1; maps:src:B.5.2',old_location='whole cell unit readback',old_page='pending page concordance',new_location='same mathematical construction with exact object names',new_page='pending final PDF',old_text=old,new_text=new,reason=reason,review_status='exact edit applied; final context readback pending'))
edit('PROOF-LIST','D08',r'\begin{enumerate}[label={$\langle1\rangle$\arabic*.},leftmargin=*]',r'\begin{enumerate}[leftmargin=*]','Use the common mathematical proof-step numbering instead of an inherited route marker.')
edit('LOG-COMPLEX-COORDINATE','D20',r'''For $s=\rho e^{-2\pi i\theta/m_j}$ the latter translation has
marked coefficient
$-\log(\rho)v_j/(2\pi i)+\theta v_j/m_j$.''',r'''For $s=\rho e^{-2\pi i\theta/m_j}$ the latter translation is
$-\log(\rho)\Pi(s)v_j/(2\pi i)+\theta\Pi(s)v_j/m_j$.''','Write the translation in its actual complex fibre coordinates; its real lattice drift is the second displayed term. No complex scalar is described as a real marked coefficient.')
edit('BOUNDARY-NAMES','D20',r'''spaces are $M_{A_1},M_{A_2},M_{M_0}$.  Their maps
$b_j:M_{A_j}\to U_*$ and $b_0:M_{M_0}\to U_*$ are the''',r'''spaces are $E_1=M_{A_1}$, $E_2=M_{A_2}$ and
$E_0=M_{M_0}$. Their maps
$b_j:E_j\to U_*$ and $b_0:E_0\to U_*$ are the''','Name all three boundary spaces explicitly while retaining M_0 for its fixed monodromy matrix. Each E_j naming map and inverse is the displayed equality of the actual mapping-torus object.')
replacements=[
 (r'\coprod_{j=0}^2(M_j\times[0,1])',r'\coprod_{j=0}^2(E_j\times[0,1])'),
 (r'for $Y=U_*,W,S_1,S_2,M_0,M_1,M_2$',r'for $Y=U_*,W,S_1,S_2,E_0,E_1,E_2$'),
 (r'[e_{M_j}x,3t-1]',r'[e_{E_j}x,3t-1]'),
 (r'$p_{M_j}$ on the middle prism',r'$p_{E_j}$ on the middle prism'),
 (r'each $M_j^c$ has counts',r'each $E_j^c$ has counts'),
 (r'$K_i=\ker(H_i(M_0)\to H_i(W))$',r'$K_i=\ker(H_i(E_0)\to H_i(W))$'),
 (r'they span a primitive subgroup of $H_2(M_0)$.',r'they span a primitive subgroup of $H_2(E_0)$.'),
 (r'Since $H_2(M_0)=\mathbb Z^6$',r'Since $H_2(E_0)=\mathbb Z^6$'),
 (r'$j:M_0\to X^\circ$',r'$j:E_0\to X^\circ$'),
 (r'$\sigma:H_2(W)\to H_2(M_0)$',r'$\sigma:H_2(W)\to H_2(E_0)$'),
 (r'$H_2(M_0)=\sigma H_2(W)\oplus K_2$',r'$H_2(E_0)=\sigma H_2(W)\oplus K_2$')]
for i,(old,new) in enumerate(replacements,1):
 edit('BOUNDARY-USE-'+str(i),'D20',old,new,'Apply the explicit E_j naming map only to boundary spaces; all matrix actions, invariant lattices and their M_0 symbol remain unchanged.')
edit('HUREWICZ-PAGES','D18',r'Corollary~4.33, pp.~366--367]{mapsHatcher02}',r'Corollary~4.33, pp.~366--368]{mapsHatcher02}','The complete opened primary statement/proof reading includes the proof continuation on p.368; give its full used page span.')
source=u.repairs.SOURCE.read_text();assert source.count(before)==1
candidate=source.replace(before,after,1);u.check_permanent_identifiers(source,candidate,set(),set())
p.write_text(after,encoding='utf-8',newline='\n');u.repairs.SOURCE.write_text(candidate,encoding='utf-8',newline='\n');r.write_table(r.DEFECTS,fields,rows+changes)
print('UTC',datetime.now(timezone.utc).isoformat());print('EXACT_DEFECT_ROWS',len(changes));print('ALL_OLD_IDENTITIES_PRESERVED; FINAL_NOTATION_CONTEXTS_PENDING')
