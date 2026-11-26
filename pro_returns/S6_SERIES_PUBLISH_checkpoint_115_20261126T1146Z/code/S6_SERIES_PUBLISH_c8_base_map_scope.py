"""State the memberwise domain already proved by the complete base-map argument."""
from datetime import datetime, timezone
import S6_SERIES_PUBLISH_c8_integrate_units as u
import S6_SERIES_PUBLISH_c8_root_units as r

p = u.WORK / 'root/base_map.tex'
s = p.read_text()
old = 'The holomorphic map $f:X\\to\\mathbb P^1$ of the original\nsphere construction is null-homotopic.'
new = ('For every admissible member of Definition~\\ref{mapsIII:def:marked-family}\n'
       'with $|p|=1$, the holomorphic base map\n'
       '$f:X_p\\to\\mathbb P^1$ is null-homotopic.')
old_proof = '\\begin{proof}\nThe two reduced multiple fibres satisfy'
new_proof = ('\\begin{proof}\nFix such a member and write $X=X_p$. Its two reduced multiple fibres satisfy')
assert s.count(old) == s.count(old_proof) == 1
t = s.replace(old,new,1).replace(old_proof,new_proof,1)
u.check_permanent_identifiers(s,t,set(),set())
fields,rows = r.table(r.DEFECTS)
ident = 'III-C8-BASE-MAP-MEMBERWISE-SCOPE'
assert not any(x['change_id']==ident for x in rows)
rows.append(dict(change_id=ident,type='D26',statement_id='maps:src:B.2.1',
 old_location='root/base_map.tex complete theorem and first proof sentence',old_page='pending page concordance',
 new_location='same theorem and proof',new_page='pending final PDF',old_text=old+'\n'+old_proof,new_text=new+'\n'+new_proof,
 reason='Whole105-line proof reread. Q000 supplies the same exact multiplicities 3,4 for each admissible member, and earlier J4 supplies its smooth sphere and vanishing H1/H2 for |p|=1. Fixing X=Xp is an identity notation map with inverse Xp=X. Every divisor isomorphism, compatible frame, M/inverse, F_s, G, degree12 and pi6 calculation is then that same memberwise proof. The complete argument is unchanged; the statement now prints its actual full domain.',
 review_status='whole original proof and actual common Q000/J4 input read; bounded final statement readback and canonical application pending'))
p.write_text(t,encoding='utf-8',newline='\n')
r.write_table(r.DEFECTS,fields,rows)
print('UTC',datetime.now(timezone.utc).isoformat())
print('OLD',old+'\n'+old_proof)
print('NEW',new+'\n'+new_proof)
print('IDENTITIES_PRESERVED; NO_CRITERION_INCREMENT')
