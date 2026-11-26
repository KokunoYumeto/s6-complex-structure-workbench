"""Bounded corrections after the complete LP candidate reading."""
import csv
from datetime import datetime, timezone
import hashlib
from pathlib import Path
import re
import S6_SERIES_PUBLISH_c8_integrate_units as units
root=Path(__file__).resolve().parent.parent
lane=root/'agents/continuation8_iii_weighted_units'
p=root/'agents/continuation8_iii_integration/units/weighted/weighted_engel_types.tex'
original=p.read_text();text=original
assert hashlib.sha256(p.read_bytes()).hexdigest()=='57a8eaff0f3ad096c800d8086cc96ff48ed5b83c9f4d83c38ba5a8fe9ae33759'
edits=[]
def change(old,new,kinds,why,count=1):
 global text
 assert text.count(old)==count,(old,text.count(old),count)
 for _ in range(count):
  at=text.index(old)
  edits.append((kinds,text.count('\n',0,at)+1,old,new,why))
  text=text[:at]+new+text[at+len(old):]
change('Here is the complete fundamental-class invariant, including its\ntwo- and three-primary coordinates. Put',
       'The complete fundamental-class invariant includes the following\ntwo- and three-primary coordinates. Put','D08;D23',
       'State the invariant directly while retaining its full target.')
change('The angular vector $\\delta$ here is fixed by\n$N\\gamma_d=d\\delta$; this convention removes the possible\nopposite choice for the original scalar-circle parameter.',
       'The scalar-circle parameter is the angular vector $\\delta$\nfixed by $N\\gamma_d=d\\delta$.','D08;D20',
       'Bind the same angular generator by its exact monodromy equation without historical-version wording.')
change('self-intersection formula on each fixed curve. On a fixed curve it is',
       'self-intersection formula. The normal Euler class on each fixed curve is','D20;D23',
       'Identify the displayed normal Euler class explicitly.')
change(r'[X_d]',r'[X]','D20',
       'Use the already defined arbitrary member X of weight d in both localization evaluations; the identity X_d=X preserves every construction parameter.',2)
change('$P_{\\rm ref}=0$.  Suppose $d$ is even.  In the order-four\nfinite cap, put',
       '$P_{\\rm ref}=0$. For even $d$, at the finite cap with\norder-four elliptic monodromy, put','D23;D26',
       'Distinguish the elliptic monodromy order four from the permitted logarithmic multiplicity m1=4ell, preserving every positive ell.')
change(r'''$v\mapsto q_L^{-1}vq_R$. The factors are two-connected, so a map
from $N$ is determined by its two integer degrees $A,B$; inverse
representatives are the two degree maps supported in a positive
three-ball.''',r'''$v\mapsto q_L^{-1}vq_R$. The factors are two-connected, so
cellular obstruction theory identifies the homotopy classes of maps
from $N$ with $H^3(N;\mathbb Z^2)$. Evaluation on $[N]$ gives
the two integer degrees $A,B$. For the inverse, collapse the
complement of a positive three-ball and compose with the degree
$A$ and $B$ maps to the two three-spheres.''','D20;D22',
       'Specify the degree correspondence on homotopy classes, its cellular justification and its explicit inverse representatives; preserve both Spin4 factors and degree signs.')
change(r'\ell(N,C)=5kP,',r'\ell(N,C)=5kP.','D23',
       'End the linking equation with the sentence it completes.')
change('of \\ref{maps:src:D.2.34}. Define $M_d$ by this member.',
       'of \\ref{maps:src:D.2.34}, so they realize the member $M_d$\nof Definition~\\ref{maps:def:weighted-engel-data}.','D12;D13',
       'Use the single input definition of Md; the proof still verifies its actual existence and every freeness condition.')
for m in reversed(list(re.finditer(r'\n{3,}',text))):
 edits.append(('D23',text.count('\n',0,m.start())+1,m[0],'\n\n','Remove excess empty source lines after movement while keeping all text and identities.'))
 text=text[:m.start()]+'\n\n'+text[m.end():]
units.check_permanent_identifiers(original,text)
assert '\r' not in text
table=lane/'S6_SERIES_PUBLISH_LP_publication_defects.tsv'
with table.open(newline='') as f:
 r=csv.DictReader(f,delimiter='\t');fields=r.fieldnames;rows=list(r)
assert len(rows)==199
for i,(kinds,line,old,new,why) in enumerate(edits,154):
 for kind in kinds.split(';'):
  rows.append(dict(zip(fields,[f'III-C8-LP-PUB-{i:03d}-{kind}',kind,'maps:src:D.2.48',f'weighted_engel_types.tex readback edit line{line}',
   'pending page concordance','weighted/weighted_engel_types.tex','pending final build',old,new,why,
   'complete candidate read; bounded readback follow-up pending; global gates open'])))
p.write_text(text,newline='\n')
with table.open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
print('UTC',datetime.now(timezone.utc).isoformat(),'BOUNDED_EDITS',len(edits),'TOTAL_EDITS',153+len(edits),'DEFECT_ROWS',len(rows))
for kinds,line,old,new,why in edits:
 if old.strip(): print('CHANGED',kinds,'AT',line,'\n'+new)
print('LINES',len(text.splitlines()),'SHA256',hashlib.sha256(p.read_bytes()).hexdigest())
print('ALL32_IDENTITIES_PRESERVED; NO_MATH_REFUTATION; NO_INDEPENDENT_CREDIT; NO_SHARED_WRITES')
