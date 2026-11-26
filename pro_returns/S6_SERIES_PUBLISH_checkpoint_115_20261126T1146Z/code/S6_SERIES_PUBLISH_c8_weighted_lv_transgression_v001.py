"""Unfold the already admitted relative cochain identity on the actual LV sphere."""
import csv
from datetime import datetime, timezone
import hashlib
from pathlib import Path
import S6_SERIES_PUBLISH_c8_integrate_units as units
root=Path(__file__).resolve().parent.parent
lane=root/'agents/continuation8_iii_weighted_units'
p=root/'agents/continuation8_iii_integration/units/weighted/weighted_os45.tex'
oldtext=p.read_text()
assert hashlib.sha256(p.read_bytes()).hexdigest()=='ac1baeb921b5489a3779bd94f6f6e6b889433ac95e21cdf9f0588b6073b3abef'
old=r'''\eqref{maps:eq:weighted-os45-total-link}. Apply the integral relative
transgression \eqref{maps:eq:D.WI13} to this embedded sphere $N$,
the differential reference $\rho$ and the complete chain $B_C$.
These are the same type of input as in that formula: the Bott residues
are the positive unit, the admissible sphere frame is the one specified
there, and the coefficient map is
$\mathcal D_X:c\mapsto c\frown[X]$, with its declared inverse.
The substitution is identity on this sphere, frame and chain.  Hence'''
new=r'''\eqref{maps:eq:weighted-os45-total-link}. Use the integral relative
cochain argument of \eqref{maps:eq:D.WI13} on this $X$ and its
embedded sphere $N$. The manifold is simply connected and spin with
$\lambda=0$; the unit Thom residues and the index-two normal-frame
map have been proved above. The admissible three-frame and its
rank-three spin complement in that argument give the obstruction
$\mathcal D_X^{-1}(P_{\rm ref})$ on this manifold. Its full frame
has even sphere parity, so its degree $q_0$ relative to $\rho$
satisfies $q_0\equiv\epsilon_\rho\pmod2$.
For an integral four-chain $D_4$ with $\partial D_4=8N$, the same
oriented cell obstruction is
\[
 -D_4\cdot C=2q+8q_0,
 \qquad q/8=\operatorname{lk}(N,P_{\rm ref})\quad\text{in }\mathbb Q/\mathbb Z.
\]
Here the second equality is the cap-product identification
$\mathcal D_X(c)=c\frown[X]$, with its declared inverse, and
$D_4\cdot C=8\ell(N,C)$ because $\partial B_C=C$.
Division by sixteen gives'''
assert oldtext.count(old)==1
text=oldtext.replace(old,new)
units.check_permanent_identifiers(oldtext,text)
table=lane/'S6_SERIES_PUBLISH_LV_publication_defects.tsv'
with table.open(newline='') as f:
 r=csv.DictReader(f,delimiter='\t');fields=r.fieldnames;rows=list(r)
assert len(rows)==448
why='Unfold the admitted LP relative cochain derivation for the actual LV manifold and order-eight sphere, keeping the integral obstruction before division and the exact cap-product inverse. This identifies all inputs without suggesting an identity map between two different manifolds; no invariant, sign or scope changes.'
for kind in ['D20','D22','D26']:
 rows.append(dict(zip(fields,[f'III-C8-LV-PUB-349-{kind}',kind,'maps:src:D.2.53','weighted_os45.tex final relative-transgression paragraph','pending page concordance','weighted/weighted_os45.tex','pending final build',old,new,why,'whole candidate and bounded follow-ups read; final paragraph readback pending; global gates open'])))
p.write_text(text,newline='\n')
with table.open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
print('UTC',datetime.now(timezone.utc).isoformat(),'EXACT_EDIT349; DEFECT_ROWS',len(rows))
print(new)
print('LINES',len(text.splitlines()),'SHA256',hashlib.sha256(p.read_bytes()).hexdigest())
print('ALL71_IDENTITIES_PRESERVED; NO_NEW_REFUTATION_OR_INDEPENDENT_CREDIT; NO_SHARED_WRITES')
