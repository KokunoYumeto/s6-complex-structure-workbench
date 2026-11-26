"""Map the three-family proof to the complete common smoothing/frame owners."""
from datetime import datetime, timezone
import S6_SERIES_PUBLISH_c8_integrate_units as u
import S6_SERIES_PUBLISH_c8_root_units as r

path=u.WORK/'root/named_fibrations.tex'
before=path.read_text()
after=before
df,ds=r.table(r.DEFECTS)
specs=[
 ('SMOOTHING-OWNER','D12',
  'A smooth approximation fixed near this torus preserves\nits whole inverse image: the compact complement of a\nsmaller such neighbourhood has image disjoint from the\nselected value, so a sufficiently close approximation\nthere still misses that value.\n\n',
  '',
  'The complete common Q255 proof owns the based bump, protected approximation and full-fibre argument. Its exact application is placed after the full differential below, where all regularity hypotheses have been verified.'),
 ('SMOOTHING-APPLICATION','D22',
  'derivative, these are the normal covectors of the retained\nmap. The ordered tangent and normal frame, relative to',
  r'''derivative, these are the normal covectors of the retained
map. Their independence follows from the invertibility of $R(q)$
and the nonzero radial and angular coordinate derivatives.
Apply Lemma~\ref{mapsIII:based-regular-fibre-smoothing} to this
family's retained map $f=H:X\to S^4$, the entire displayed torus
$N=H^{-1}(y)$, and any fixed $x_0\in W$, where $H(x_0)=*$.
The inverse naming map is $H=f$; the regular value $y$ is the
same chosen open-cell value, and the target coordinates are the
specified product-cell coordinates of
Definition~\ref{mapsIII:def:three-sphere-families}.
The full-fibre and smooth-neighbourhood assertions were proved
above, and the displayed independent covectors prove rank four.
That lemma supplies a based smoothing fixed on a closed tube
around this entire torus, preserving precisely this ordered
normal framing. The ordered tangent and normal frame, relative to''',
  'Give every actual common-lemma input after the complete fibre and differential calculation, including the based point, target coordinates and inverse map of notation; retain the whole finite-error construction at its sole earlier owner.'),
 ('FRAME-OWNER','D04',
  'This is the identical matrix $D(a,b)$ in the proof of\nTheorem~\\ref{maps:src:B.3.1}, under the identity map on the two\nangular coordinates and a constant frame change. Its two displayed\n$K_s$ factors therefore give the same periodic contraction here;\nthe inverse coordinate identification is again $(a,b)\\mapsto(a,b)$.',
  'This is the matrix $D(a,b)$ of\nProposition~\\ref{wb:h24:ret:framing-proposition}, under the identity\nmap on the two angular coordinates and the constant frame change\njust described. Its two displayed $K_v$ factors give the periodic\ncontraction of this same comparison matrix; the inverse coordinate\nidentification is $(a,b)\\mapsto(a,b)$.',
  'Name the exact sole formal owner of the unchanged D(a,b) contraction after retained-angle consolidation; use its actual homotopy parameter and preserve both angular identification directions.'),
]
for suffix,kind,old,new,reason in specs:
    assert after.count(old)==1,(suffix,after.count(old))
    after=after.replace(old,new,1)
    ident='III-C8-NAMED-SHARED-'+suffix
    assert not any(x['change_id']==ident for x in ds)
    ds.append(dict(change_id=ident,type=kind,statement_id='maps:src:B.4.1',
      old_location='three-family retained-angle proof',old_page='pending page concordance',
      new_location='same proof, exact shared-owner application',new_page='pending final PDF',
      old_text=old,new_text=new,reason=reason,
      review_status='bounded whole predecessor/current context read; staged exact application; canonical placement and readback pending'))
u.check_permanent_identifiers(before,after)
path.write_text(after,encoding='utf-8',newline='\n')
r.write_table(r.DEFECTS,df,ds)
print('UTC',datetime.now(timezone.utc).isoformat())
print('EXACT_SHARED_OWNER_EDITS',len(specs),'FINAL_LINES',after.count('\n'))
print('ALL_OLD_IDENTITIES_PRESERVED; CANONICAL_APPLICATION_PENDING')
