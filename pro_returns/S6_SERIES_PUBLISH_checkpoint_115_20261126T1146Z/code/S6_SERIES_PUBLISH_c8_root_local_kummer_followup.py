"""Finish the Kummer unit's explicit fan, automatic equations and whole-read prose."""
from datetime import datetime,timezone
import re
import S6_SERIES_PUBLISH_c8_integrate_units as u
import S6_SERIES_PUBLISH_c8_root_units as r
p=u.WORK/'root/local_kummer.tex';before=p.read_text();after=before
fields,rows=r.table(r.DEFECTS);changes=[]
def edit(suffix,kind,label,old,new,reason):
 global after
 assert after.count(old)==1,(suffix,after.count(old))
 after=after.replace(old,new,1);ident='III-C8-KUMMER-FOLLOW-'+suffix
 assert not any(x['change_id']==ident for x in rows)
 changes.append(dict(change_id=ident,type=kind,statement_id=label,old_location='whole local/global Kummer readback',old_page='pending page concordance',new_location='same exact construction after readback correction',new_page='pending final PDF',old_text=old,new_text=new,reason=reason,review_status='exact edit applied; final changed contexts pending'))
edit('FAN-INPUT','D05','mapsIII:def:kummer-data',r'''with the holomorphic correction and prescribed $A_2$ fan of
Definition~\ref{mapsIII:def:cusp-suspension-maps}.''',r'''with the holomorphic correction of
Definition~\ref{mapsIII:def:cusp-suspension-maps}.
The fan in $N'=\mathbb Z^2\oplus\mathbb Z$ consists of the
cones over the height-one triangles
\[
 \{u,u+e_1,u+e_2\},\qquad
 \{u+e_1,u+e_2,u+e_1+e_2\},\qquad u\in\mathbb Z^2,
\]
and their faces; $e_1,e_2$ are the coordinates corresponding to
$\widehat w,\widehat\delta$.''','Q011 defines the correction but not the fan. Print the complete actual e1-e2 triangulation rather than assigning it to an absent clause of that definition.')
edit('ACTION-PROSE','D02','maps:src:C.1.1',r'''exist. This transfers the established cusp action property without a new
estimate on $C_N$.''',r'''exist. Hence the source action is free and properly discontinuous.''','State the proved source-action conclusion directly; its complete actual equivariant compact-set argument remains.')
for n in range(1,5):
 label='maps:eq:C.1.'+str(n);pos=after.index(r'\label{'+label+'}')
 start=after.rfind(r'\[',0,pos);end=after.index(r'\]',pos)+2
 old=after[start:end];assert r'\]' not in old[:-2] and r'\[' not in old[2:]
 new=r'\begin{equation}'+old[2:-2]+r'\end{equation}'
 edit('NUMBERED-ENV-'+str(n),'D19',label,old,new,'The inherited manual tag was inside an unnumbered display. Replace that exact display by an automatic equation environment, preserving its formula, permanent target and label.')
edit('K4-SCOPE','D11','maps:src:C.1.3',r'''smooth compact complex manifold. Additional cusp sheets and additional
vertical branch fibres do not remove the obstruction. For $N=1$ the''',r'''smooth compact complex manifold. For $N=1$ the''','The arbitrary finite-map domain and even-one-cusp-component clause already include every additional cusp sheet and vertical branch fibre; the full proof retains both allowances. Remove only the repeated scope sentence.')
edit('K4-TRANSPORT-SQUARE','D20','maps:src:C.1.3',r'''and continuation along a loop with monodromy $A$ carries it to $AL_N$.
Translations do not change this subgroup, since the fibre group is abelian.''',r'''and continuation along a loop with point-return matrix $A$ carries it
to $AL_N$. Indeed the actual bundle transports satisfy
$F_1\widetilde H=HF_0$, hence
$F_{1*}\widetilde H_*=H_*F_{0*}$; the inverse loop uses
$H^{-1},\widetilde H^{-1}$ and recovers the original subgroup.
Translations induce the identity on the abelian fibre group by a path
from the translation point to zero.''','Print the exact transport square and inverse transport from the complete admitted K4 comparison; the convention is the explicit point-return convention.')
edit('K5-STATEMENT','D02','maps:src:C.1.4',r'''Even allowing a normal singular source, there is no finite global
extension whose whole inverse image of $N_0$ is the single prescribed
map $\kappa_N$, for $N>1$.''',r'''For $N>1$, the local map $\kappa_N$ has no finite global extension
from a normal compact complex source whose whole inverse image of
$N_0$ is that single prescribed map.''','State the exact full normal-source and whole-preimage domain directly, retaining the proved negative conclusion without category-comparison framing.')
start=after.index(r'\begin{proof}',after.index(r'\label{maps:src:C.1.4}'));end=after.index(r'\end{proof}',start)+len(r'\end{proof}')
old=after[start:end];new=old.replace(r'\begin{enumerate}[leftmargin=*]'+'\n'+r'\item ','',1).replace('\n'+r'\end{enumerate}','',1)
edit('K5-SINGLE-PROOF-FLOW','D08','maps:src:C.1.4',old,new,'After moving the separate finite calculation into its numbered remark, give the complete sole lattice/Stein argument connected prose rather than a one-item list.')
edit('K5-TRANSITION','D08','maps:src:C.1.4','equality of both residues $a,b$. Here is the full base-degree argument for the stated normal-source\nscope. Let $F:Z\\to X$ be such an extension and take the connected','equality of both residues $a,b$.\n\nLet $F:Z\\to X$ be such an extension and take the connected','Connect the exact lattice and base-degree arguments without announcing completeness in the proof itself.')
edit('K6-LOCATOR-1','D06','maps:src:C.1.5',r'cusp completion with the already normal smooth source in \ref{maps:src:C.1.1}.',r'cusp completion with the already normal smooth source in Theorem~\ref{maps:src:C.1.1}.','Name the actual theorem kind at the normal-completion use.')
edit('K6-LOCATOR-2','D06','maps:src:C.1.5',r'''as it is over $X^*$. The selected cusp component is smooth by
\ref{maps:src:C.1.1}.''',r'''as it is over $X^*$. The selected cusp component is smooth by
Theorem~\ref{maps:src:C.1.1}.''','Name the actual theorem kind at the selected-cusp smoothness use.')
edit('ETALE-SPELLING','D23','maps:src:C.1.1',r'''degree $N^2$. For $N>1$ it is quasi-etale, and its nonflat and non-etale''',r'''degree $N^2$. For $N>1$ it is quasi-\'etale, and its nonflat and non-\'etale''','Use the exact mathematical accent in the theorem statement.')
# Remaining proof occurrences receive individual exact context rows.
for i in range(after.count('etale')):
 pos=after.index('etale');start=after.rfind('\n',0,pos)+1;end=after.index('\n',pos)
 old=after[start:end];new=old.replace('etale',r"\'etale",1)
 edit('ETALE-PROOF-'+str(i+1),'D23','maps:src:C.1.1; maps:src:C.1.2; maps:src:C.1.3',old,new,'Apply the same mathematical spelling to the exact proof occurrence.')
source=u.repairs.SOURCE.read_text();assert source.count(before)==1
candidate=source.replace(before,after,1);u.check_permanent_identifiers(source,candidate,set(),set())
p.write_text(after,encoding='utf-8',newline='\n');u.repairs.SOURCE.write_text(candidate,encoding='utf-8',newline='\n');r.write_table(r.DEFECTS,fields,rows+changes)
print('UTC',datetime.now(timezone.utc).isoformat());print('EXACT_DEFECT_ROWS',len(changes));print('KUMMER_LINES',len(after.splitlines()));print('ALL_OLD_IDENTITIES_PRESERVED; FINAL_CONTEXT_READBACK_PENDING')
