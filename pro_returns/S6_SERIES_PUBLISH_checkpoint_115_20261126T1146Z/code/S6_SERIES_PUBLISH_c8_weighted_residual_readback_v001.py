"""Bounded readback repairs after the complete 1905-line residual proof reading."""
import csv
from datetime import datetime, timezone
import hashlib
from math import gcd
from pathlib import Path
import re
import sympy as sp
import S6_SERIES_PUBLISH_c8_integrate_units as units
root=Path(__file__).resolve().parent.parent
lane=root/'agents/continuation8_iii_weighted_units'
p=root/'agents/continuation8_iii_integration/units/weighted/residual_even_types.tex'
original=p.read_text();text=original
assert hashlib.sha256(p.read_bytes()).hexdigest()=='a0eef3d534944a8315a46040551551a3637c050391a8b909907ef644728781a9'
edits=[]
def change(owner,old,new,kinds,why,count=1):
 global text
 assert text.count(old)==count,(old[:150],text.count(old),count)
 for _ in range(count):
  a=text.index(old);edits.append((owner,kinds,text.count('\n',0,a)+1,old,new,why))
  text=text[:a]+new+text[a+len(old):]

changes=[
 ('LL',r'\mathrm{OS}&z&\kappa',r'\mathrm{OS}&i_0&\kappa','D20','Use the selected-index symbol in the remaining fixed-data table.'),
 ('LL','an cap-kernel','a cap-kernel','D23','Correct the article after removing workflow emphasis.'),
 ('LM','an cylinder boundary','a cylinder boundary','D23','Correct the article after removing workflow emphasis.'),
 ('LM','an combination','a combination','D23','Correct the article after removing workflow emphasis.'),
 ('LM',"is 'etale",r"is \'etale",'D23','Correct the TeX accent in the étale covering statement.'),
 ('LM','column Euclid on the last\ncoordinates','column Euclid on the last five\ncoordinates','D20;D23','Specify the exact five-coordinate projection in the integral section.'),
 ('LL',r'''\item The sphere convention is determined by the homomorphism
$\pi_3SO(3)\to\pi_3SO(6)$ has image $2\mathbb Z$.''',r'''\item The homomorphism $\pi_3SO(3)\to\pi_3SO(6)$ has image
$2\mathbb Z$ and fixes the sphere-framing convention.''','D23','Correct the joined grammatical construction without changing the representation map.'),
 ('LL','This proves the formula with its signs and all lower-order\nelements of every order.',
  'This proves the formula with its signs at every nonidentity\nelement, including all proper orders.','D02;D23;D26','State the entire finite-group element scope clearly.'),
 ('LL','is literally the stabilization','is the stabilization','D08','State Brown’s exact map without emphasis.'),
 ('LM','literally identity. Combining','identity. Combining','D08','State the exact simplicial composites.'),
 ('LM','The reference frame really induces','The reference frame induces','D08','State the proved tangent projection directly.'),
 ('LM','For clarity, the cusp characters','The cusp characters','D02','Remove the proof-process transition.'),
 ('LM','at default zero $3$','at base-profile position $3$','D04;D20','Use Q110’s defined base-profile notation.'),
 ('LM','The positive even powers of $T$ retain the full cyclic group',
  'The positive even powers of $T$ have coefficient group','D08;D20','State the full localized coefficient group directly.'),
 ('LM','Use $Z_{5,1}$ from Definition~\\ref{maps:def:minimal-odd-data},',
  'Use $Z_{5,1}$ from Definition~\\ref{maps:def:minimal-mixed-data},','D06;D22','Correct the exact model locator to Q207, which constructs OS55(a,b)=(1,5), selected1, e1, with identity refined generator. Q206 defines the odd input domain but not this model.'),
 ('LL','integral inverse sends $(x,y,z)$ to $(x,z,x+y+z)$ in the wall\nbasis.',
  'integral inverse sends a coordinate column $(r,s,t)^t$ to\n$(r,t,r+s+t)^t$ in the wall basis.','D20;D22','Separate basis classes x,y,z from a numerical coordinate column in the exact inverse.'),
 ('LM',r'$x\mapsto s$ and $(t,x)\mapsto((c/2)s,s)$, with inverse',
  r'$x\mapsto s$, and $t\mapsto(c/2)s$, $x\mapsto s$, with inverse','D20;D22','Write the second cyclic quotient map on each generator, avoiding a false rank-two target reading.'),
 ('LM','the torus and cone map in the third item.',
  'the displayed torus and cone map for the prescribed fan.','D06;D19','Replace a manual proof-item number by the named mathematical construction.'),
 ('LM','Its absolute value is computed from the complete\ncritical class in the next step.',
  'Its image in absolute cohomology is computed from the complete\ncritical class in the next step.','D20','Distinguish the absolute cohomology class from a numerical absolute value.')]
for args in changes:change(*args)

# Name the two semicharacter vectors, already fixed by the explicit Q.
old='Substitution verifies the base-loop identity obtained by replacing\n$\\Pi$ by $\\Pi+I$'
new=r'''Here $\eta=(Q(r),Q(\gamma))^t=(1,0)^t$: $r$ is primitive
and the elliptic quadratic form is one on every nonzero vector
of $\mathbb F_2^2$. Substitution verifies the base-loop identity
obtained by replacing $\Pi$ by $\Pi+I$'''
change('LL',old,new,'D20;D22','Define the long semicharacter vector by its actual marked generators; its numerical value follows from the displayed odd quadratic form. This is the same vector explicitly defined in LM.')
change('LL','The Gaussian exponent is\n$-U^tK_1',
 r'''Put $\epsilon=(Q(l),Q(p))^t$. Since the short plane is isotropic,
these two values specify its restricted semicharacter. The Gaussian
exponent is
$-U^tK_1''','D20;D22','Define the rank-one short semicharacter vector from the explicit Q and isotropic basis; preserve the same Gaussian and reciprocal inverse.')

# Keep the differential target distinct from the auxiliary equivariant line.
a=text.index(r'\item \emph{The reference frame and the critical-cycle defect.}')
b=text.index(r'\item\emph{The integral critical-cycle calculation',a)
old=text[a:b];new=old.replace(r'\mathcal L',r'\mathcal T')
change('LL',old,new,'D20',
 'Rename only the differential target f*TP1 and its occurrences in D44.5/reference splitting from L to T. The map is identity on that same line, with identity inverse; the auxiliary equivariant line L remains unchanged.')

# Classification conclusions belong to the theorem, following complete inputs.
change('LM','where $\\ell$ is the primitive fixed lift with\n$\\gamma^*(\\ell)=1$. These are exactly the simply connected data\nin this one-log sector, and all are free. Every affine twist is allowed.',
 'where $\\ell$ is the primitive fixed lift with\n$\\gamma^*(\\ell)=1$. Every affine twist is allowed.',
 'D13;D23','Move the freeness and exact simple-connectivity conclusion from the numbered input definition into its theorem; preserve the full definition domain.')
change('LM','All outputs of Definition~\\ref{maps:def:additive-residual-data} are spin and satisfy',
 r'''The data of Definition~\ref{maps:def:additive-residual-data} are
exactly the simply connected data in its listed one-log sector, and
all are free. Every resulting $X$ is spin and satisfies''',
 'D13;D23;D26','State the exact simple-connectivity/freeness result once in the theorem, with all eleven patterns and unrestricted finite/affine parameters.')

# Explicit definitions select the same embedded surgery representatives used
# in the full proof; existence and framings are proved there.
old=r'''The manifold $Z_{c,0}$ is surgery on an embedded two-sphere representing
$c$ times the generator of $H_2(S^2\times S^4)$. The manifold
$Z_{c,1}$ is surgery in $M_{\rm conic}\#(S^2\times S^4)$ on an
embedded sphere representing $(t,-c/2)\in\mathbb Z/2\oplus\mathbb Z$,
where $t$ is the conic-surgery generator of \ref{maps:src:D.2.8}.'''
new=r'''For $Z_{c,0}$, tube $c$ disjoint parallel copies of $S^2$ in
$S^2\times S^4$ and perform surgery on that sphere. For $Z_{c,1}$,
put the conic of $M_{\rm conic}$ in the plane $z_3=0$ with equation
$z_0z_2-z_1^2=0$. The line spanned by $(0,0,0,1)$ and $(1,0,1,0)$
is disjoint from it. Tube its image in $M_{\rm conic}$ to $c/2$
negatively oriented parallel spheres in the $S^2\times S^4$
summand and perform surgery. Its class is
$(t,-c/2)\in\mathbb Z/2\oplus\mathbb Z$, where $t$ is the
conic-surgery generator of \ref{maps:src:D.2.8}.'''
change('LL',old,new,'D22;D26','Specify the actual tube and conic-disjoint projective-line embeddings in the definition; the retained proof verifies disjointness, spin framing, trace quotient and complete invariants.')

# Standard scholarly citation spacing at the already inspected exact loci.
replacements={
 r'\cite[Sections 3.11--3.14]':r'\cite[Sections~3.11--3.14]',
 r'\cite[Theorem 5]':r'\cite[Theorem~5, p.~796]',
 r'\cite[pp.471--472]':r'\cite[pp.~471--472]',
 r'\cite[Theorem 3.9 and formulas (4.1)--(4.4)]':r'\cite[Theorem~3.9 and formulas~(4.1)--(4.4), pp.~562--567]',
 r'\cite[pp.369--372]':r'\cite[pp.~369--372]',
 r'\cite[Section 5]':r'\cite[Section~5, pp.~8--9]',
 r'\cite[Definition 1.7, Remark 1.8, Theorem 3.1]':r'\cite[Definition~1.7, Remark~1.8 and Theorem~3.1]',
 r'\cite[Theorem 3 and Section 4.1]':r'\cite[Theorem~3, p.~795; Section~4.1, pp.~809--810]'}
for old,new in replacements.items():
 for m in reversed(list(re.finditer(re.escape(old),text))):
  owner='LL' if m.start()<text.index(r'\subsubsection{Additive caps') else 'LM'
  edits.append((owner,'D18',text.count('\n',0,m.start())+1,m[0],new,'Use the same inspected primary locus with scholarly citation spacing and its precise printed pages.'))
  text=text[:m.start()]+new+text[m.end():]

# Complete OS profile names also on indented table rows.
for m in reversed(list(re.finditer(r'(?m)^( +)(45|55)(/II|/\\mathrm\{base\})?&',text))):
 new=m[1]+r'\mathrm{OS'+m[2]+'}'+(r'/\mathrm{II}' if m[3]=='/II' else m[3] or '')+'&'
 owner='LL' if m.start()<text.index(r'\subsubsection{Additive caps') else 'LM'
 edits.append((owner,'D04;D20',text.count('\n',0,m.start())+1,m[0],new,'Spell out the same ordered OS profile on the remaining indented rows.'))
 text=text[:m.start()]+new+text[m.end():]
change('LM',r'55/\mathrm{base}\text{ or }II&',r'\mathrm{OS55}/\mathrm{base}\text{ or }\mathrm{II}&','D04;D20','Spell out the profile name in the common order-five fixed-component row.')

# The old individual representatives and the correct ones have exactly the
# same integral sum. All downstream uses depend on that sum or independently
# on the fixed-curve line data, whose formulas are unchanged.
aa,bb,kk=sp.symbols('a b k',integer=True)
K11=aa;K12=aa*bb*kk;K22=aa*bb**2*kk**2-bb
assert sp.expand((K11-K12)+(K22-K12)+K12-(K11-K12+K22))==0
rows=[('45II2O',8,24,4,0,1),('45II2F',8,40,4,0,1),('45II3O',8,-32,0,0,1),('45II3F',8,-16,0,0,1),
 ('55II3O',4,72,0,0,1),('55II3F',4,80,0,0,1),('55base2',20,352,4,8,5),('55base3',20,-68,14,8,5),
 ('55base4',20,352,4,8,5),('55II20O',20,352,4,8,5),('55II20F',20,392,4,8,5)]
for name,b,K,P,lam,order in rows:
 assert K%2==0 and (-K//2)%b==P and -K%b==lam and b//gcd(K,b)==order
 print('UNCHANGED_TOTAL',name,'b',b,'K',K,'P',P,'lambda',lam,'critical_order',order)
units.check_permanent_identifiers(original,text)
assert '\r' not in text
p.write_text(text,newline='\n')
table=lane/'S6_SERIES_PUBLISH_RESIDUAL_publication_defects.tsv'
with table.open(newline='') as f:
 reader=csv.DictReader(f,delimiter='\t');fields=reader.fieldnames;previous=list(reader)
for i,(owner,kinds,line,old,new,why) in enumerate(edits,1):
 for kind in kinds.split(';'):
  previous.append(dict(zip(fields,[f'III-C8-RESIDUAL-READBACK-{i:03d}-{kind}',kind,'maps:src:D.2.'+('44' if owner=='LL' else '45'),
   f'residual_even_types.tex bounded readback line{line}','pending page concordance','weighted/residual_even_types.tex','pending final build',old,new,why,
   'whole1905-line candidate read; bounded changes await final readback; global gates open'])))
with table.open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(previous)
for owner,kinds,line,old,new,why in edits:print('EDIT',owner,kinds,'LINE',line,repr(old),'TO',repr(new))
print('UTC',datetime.now(timezone.utc).isoformat(),'LINES',len(text.splitlines()),'BOUNDED_EDITS',len(edits),'DEFECT_ROWS',len(previous))
print('SHA256',hashlib.sha256(p.read_bytes()).hexdigest(),'OLD_IDENTITIES_PRESERVED; NO_NEW_TAGS; NO_INDEPENDENT_CREDIT; GLOBAL_GATES_OPEN')
