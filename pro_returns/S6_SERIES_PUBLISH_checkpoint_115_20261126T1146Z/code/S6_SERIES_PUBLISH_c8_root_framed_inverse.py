"""Display the inverse of the integral duality map used in the framing proof."""
from datetime import datetime, timezone
import S6_SERIES_PUBLISH_c8_integrate_units as u
import S6_SERIES_PUBLISH_c8_root_units as r

path=u.WORK/'root/framed_class.tex'
before=path.read_text(encoding='utf-8')
old=r'''For $\Omega=\gamma\wedge u\wedge w\wedge\delta$, the map
$\operatorname{PD}(v)=\iota_v\Omega$ has inverse determined
by its four coefficients. Since $\det A_j=1$,
evaluation on three vectors gives'''
new=r'''For $\Omega=\gamma\wedge u\wedge w\wedge\delta$, the integral map
$\operatorname{PD}(v)=\iota_v\Omega$ is
\[
 a\widehat\gamma+b\widehat u+c\widehat w+f\widehat\delta
 \longmapsto
 a\,uw\delta-b\,\gamma w\delta+c\,\gamma u\delta-f\,\gamma uw.
\]
Its inverse sends the coefficients $(A,B,C,D)$ in the ordered
basis $(uw\delta,\gamma w\delta,\gamma u\delta,\gamma uw)$
to $A\widehat\gamma-B\widehat u+C\widehat w-D\widehat\delta$;
both composites fix every coefficient. Since $\det A_j=1$,
evaluation on three vectors gives'''
assert before.count(old)==1
after=before.replace(old,new,1)
source=u.repairs.SOURCE.read_text(encoding='utf-8')
assert source.count(before)==1
candidate=source.replace(before,after,1)
u.check_permanent_identifiers(source,candidate)
fields,rows=r.table(r.DEFECTS)
ident='III-C8-FRAMED-PD-INVERSE'
assert not any(x['change_id']==ident for x in rows)
rows.append(dict(change_id=ident,type='D20',statement_id='maps:src:B.1.1',old_location='framing proof, integral duality map',old_page='pending page concordance',new_location='framing proof, integral duality map',new_page='pending final PDF',old_text=old,new_text=new,reason='Print all four signs of the coefficient map and its inverse, with both composites. The map and invariant subgroup are unchanged.',review_status='complete unit read; exact inverse readback and final PDF pending'))
path.write_text(after,encoding='utf-8',newline='\n')
u.repairs.SOURCE.write_text(candidate,encoding='utf-8',newline='\n')
r.write_table(r.DEFECTS,fields,rows)
print('UTC',datetime.now(timezone.utc).isoformat())
print(new)
print('ONE_EXACT_D20_ROW; ALL_PERMANENT_IDENTITIES_PRESERVED')
