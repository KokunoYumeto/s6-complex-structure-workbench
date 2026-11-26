"""Name both actual deck and point-return matrices in the Kummer comparison."""
from datetime import datetime,timezone
from collections import Counter
import re
import S6_SERIES_PUBLISH_c8_integrate_units as u
import S6_SERIES_PUBLISH_c8_root_units as r
df,ds=r.table(r.DEFECTS);changes=[]
p=u.WORK/'root/kummer_extension.tex';before=p.read_text();after=before
def edit(suffix,kind,old,new,reason):
 global after
 assert after.count(old)==1,(suffix,after.count(old));after=after.replace(old,new,1)
 ident='III-C8-KUMMER-EXT-'+suffix;assert not any(x['change_id']==ident for x in ds)
 changes.append(dict(change_id=ident,type=kind,statement_id='wb:cusp-cover-extension-theorem',old_location='completed Kummer publication text',old_page='pending page concordance',new_location='completed Kummer exact map conventions',new_page='pending final PDF',old_text=old,new_text=new,reason=reason,review_status='bounded follow-up; whole source and changed contexts read before admission'))
edit('SUBSECTION-TITLE','D16',r'\subsection{The Kummer cover extends across the toric cusp}',r'\subsection{Completed Kummer covers}','Use a short mathematical title for the complete actual subsection.')
edit('DECK-MATRIX-STATEMENT','D20',r'''The pulled-back target cusp monodromy is $M_0^N$, and its matrix in
the cover basis is $M_0$:''',r'''The fibre-linear matrix of the pulled-back clockwise analytic deck
generator is $M_0^N$, and its matrix in the cover basis is $M_0$:''','Identify the precise maps represented by the matrices under Q016, rather than leave the loop/point-return convention implicit.')
edit('DECK-RETURN-PROOF','D20',r'''For the clockwise cusp generator the pulled-back clutch is $M_0^N$.
Write $M_0=I+R$, where $R(a,b,c,d)=(0,0,b,-a)$ and $R^2=0$.
Then $M_0^N=I+NR$ and $M_0^NS_N=S_NM_0$.
Both affine clutches fix zero, represented by $(1,1)$ after
exponentiation, and $\zeta\mapsto N\zeta$ preserves it. Thus this
identity intertwines the affine clutches as well. Their action on
$\Lambda/S_N\Lambda$ is trivial because every change under $M_0^N$
is $N$ times a short period. The deck group therefore acts on the
whole punctured relative family.''',r'''The clockwise analytic deck generators have fibre-linear matrices
$M_0$ on the source and $M_0^N$ on the pulled-back target.
Write $M_0=I+R$, where $R(a,b,c,d)=(0,0,b,-a)$ and $R^2=0$.
Then $M_0^N=I+NR$ and $M_0^NS_N=S_NM_0$.
Their point-return maps have the inverse matrices by
Definition~\ref{mapsIII:def:three-filling-datum}; inversion gives
$M_0^{-N}S_N=S_NM_0^{-1}$. All these affine maps fix zero,
represented by $(1,1)$ after exponentiation, and
$\zeta\mapsto N\zeta$ preserves it. Both intertwining identities
therefore hold for the affine maps. On $\Lambda/S_N\Lambda$
the two target actions are trivial: their changes are respectively
$NR$ and $-NR$, whose images are $N$ times short periods.
Thus the deck group acts on the whole punctured relative family.''','Print the exact inverse point-return maps and both commuting matrix identities. Every formula, affine zero section and global deck conclusion is unchanged; the Q016 convention is now explicit.')
cp=u.ROOT/'S6_SERIES_PUBLISH_III.tex';c=cp.read_text();assert c.count(before)==1;d=c.replace(before,after,1)
for pattern in [r'\\label\{([^}]+)\}',r'\\hypertarget\{([^}]+)\}']:assert Counter(re.findall(pattern,c))==Counter(re.findall(pattern,d))
p.write_text(after,newline='\n');cp.write_text(d,newline='\n');r.write_table(r.DEFECTS,df,ds+changes)
print('UTC',datetime.now(timezone.utc).isoformat());print('EXACT_EDIT_ROWS',len(changes),'FINAL_LINES',len(after.splitlines()));print('ALL_IDENTITIES_AND_OTHER_TEXT_PRESERVED; NO_CRITERION_CREDIT')
