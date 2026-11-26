"""Readback precision for the extension and three-family input conventions."""
from datetime import datetime, timezone
import S6_SERIES_PUBLISH_c8_integrate_units as u
import S6_SERIES_PUBLISH_c8_root_units as r
df,rows=r.table(r.DEFECTS)
source=u.repairs.SOURCE.read_text(encoding='utf-8')
changes=[]
for key,edits in [
 ('extension_homotopy',[
  ('RESTRICTION','D20','mapsIII:def:torus-extension-data',
   'inducing the same homomorphism on $\\pi_1(U)$, a point $x_0\\in W$',
   'such that $\\alpha$ and $h|_U$ induce the same homomorphism on\\n$\\pi_1(U)$, a point $x_0\\in W$',
   'Name the restriction already used in the complete lifting proof, with identical domain and data.'),
 ]),
 ('named_fibrations',[
  ('MAP-CONVENTIONS','D05','mapsIII:def:three-sphere-families',
   'Put $L=\\ker\\chi$. For the logarithmic family use its constructed',
   'The cusp quotient maps use the product-cell collapses and suspension\\nconventions of Definition~\\ref{mapsIII:def:cusp-suspension-maps},\\nin each prescribed marked long-period basis.\\nPut $L=\\ker\\chi$. For the logarithmic family use its constructed',
   'Bind the existing three quotient maps to the preceding exact definitions and the unchanged prescribed bases before they occur in the theorem.'),
  ('LIFT-NOTATION','D20','maps:src:B.4.1',
   'Using a radial cut-off $b$ equal to zero near $W$ and one on the\\nouter collar, put\\n\\[\\n h=h_0+[b\\ell],\\qquad L=(1-b)\\ell.\\n\\]\\nThen $h(x_0)=0$, $h=\\alpha$ on the outer collar and\\n$\\alpha=h+[L]$.',
   'Using a radial cut-off $b_c$ equal to zero near $W$ and one on the\\nouter collar, put\\n\\[\\n h=h_0+[b_c\\ell],\\qquad L_{\\rm ext}=(1-b_c)\\ell.\\n\\]\\nThen $h(x_0)=0$, $h=\\alpha$ on the outer collar and\\n$\\alpha=h+[L_{\\rm ext}]$.',
   'The identity renaming b_c=b and L_ext=L separates this local cutoff and real lift from the already defined lattice basis vector b and kernel L; every formula and map is unchanged.'),
  ('LIFT-INPUT','D20','maps:src:B.4.1',
   'this $\\alpha,h,L$, and the based target maps',
   'this $\\alpha,h$, the lift $L=L_{\\rm ext}$ in that proof, and the based target maps',
   'Write the exact identification of the local real lift with the sole extension proof variable.'),
 ])]:
 path=u.WORK/'root'/(key+'.tex')
 before=path.read_text(encoding='utf-8');after=before
 for suffix,kind,label,old,new,reason in edits:
  old=old.replace('\\n','\n');new=new.replace('\\n','\n')
  assert after.count(old)==1,(suffix,after.count(old))
  after=after.replace(old,new,1)
  ident='III-C8-EXT-NAMED-READBACK-'+suffix
  assert not any(x['change_id']==ident for x in rows)
  changes.append(dict(change_id=ident,type=kind,statement_id=label,old_location=key+' pre-readback',old_page='pending page concordance',new_location=key+' final local readback',new_page='pending final PDF',old_text=old,new_text=new,reason=reason,review_status='exact manuscript edit; actual changed-context readback pending'))
 assert source.count(before)==1,key
 candidate=source.replace(before,after,1)
 u.check_permanent_identifiers(source,candidate,[],[])
 path.write_text(after,encoding='utf-8',newline='\n');source=candidate
u.repairs.SOURCE.write_text(source,encoding='utf-8',newline='\n')
r.write_table(r.DEFECTS,df,rows+changes)
print('UTC',datetime.now(timezone.utc).isoformat())
print('EXACT_DEFECT_ROWS',len(changes))
print('ALL_OLD_IDENTITIES_PRESERVED; NO_READING_OR_CHECK_CREDIT')

