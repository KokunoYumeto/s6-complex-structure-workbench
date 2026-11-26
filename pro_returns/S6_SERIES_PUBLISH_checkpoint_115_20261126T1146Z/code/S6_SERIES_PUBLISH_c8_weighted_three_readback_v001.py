"""Bounded corrections after the complete 2340-line LF/LJ candidate readback."""
import csv
from datetime import datetime, timezone
import difflib
import hashlib
from pathlib import Path
import re
import S6_SERIES_PUBLISH_c8_integrate_units as units

root=Path(__file__).resolve().parent.parent
p=root/'agents/continuation8_iii_integration/units/weighted/three_primary_types.tex'
lane=root/'agents/continuation8_iii_weighted_units'
original=p.read_text()
assert hashlib.sha256(p.read_bytes()).hexdigest()=='f944bf672bb6f0eb672a57de234339f2485dca9a29e50f7073d8d4b83879e096'
text=original
edits=[]

def replace(owner,old,new,kinds,reason,count=1):
 global text
 assert text.count(old)==count,(owner,old[:180],count,text.count(old))
 for _ in range(count):
  a=text.index(old)
  edits.append((owner,kinds,text.count('\n',0,a)+1,old,new,reason))
  text=text[:a]+new+text[a+len(old):]

def between(start,stop):
 a=text.index(start);b=text.index(stop,a);return text[a:b]

replace('LF','The first row has the two additive choices in the statement.',
 'The first row has the two additive choices in \\eqref{maps:eq:D.T31}.',
 'D06;D20','Locate the complete input table after its relocation to the numbered definition.')
replace('LF',r'Choose $k\max r<1$',r'Choose $0<k<(\max r)^{-1}$',
 'D05;D22','Make the constructive positive roof choice explicit: the derivative k+(1-kr)b_y is strictly positive, so the stated map has its asserted inverse.')
replace('LJ',r'choose \(k\max r<1\)',r'choose \(0<k<(\max r)^{-1}\)',
 'D05;D22','Use the same explicit positive roof choice for every original additive cap; no output parameter or hypothesis is restricted.')
replace('LJ',r'\mathrm{II}I',r'\mathrm{III}','D04;D08;D20',
 'Repair the publication-editor alternation error in three profile headers; the original OS/III profiles and all counts are retained.',3)
for old,new in [
 (' 56&I_5',r' \mathrm{OS56}&I_5'),
 (' 56/II&I_2',r' \mathrm{OS56}/\mathrm{II}&I_2'),
 (' 56/III&I_5',r' \mathrm{OS56}/\mathrm{III}&I_5')]:
 replace('LJ',old,new,'D04;D20','Give the complete OS profile name in the ordered component table without altering its data.')

# Separate the real auxiliary line coordinate from the later physical z.
for owner,start,stop in [
 ('LF','On its real period\ncover define','For the nonzero elliptic short period'),
 ('LJ','For every row there is a doubled line','For the nonzero short period'),
 ('LJ','For the even sectors \\(c=6,30\\)','The physical Gaussian is')]:
 old=between(start,stop)
 new=re.sub(r'\bz\b',lambda m:r'\zeta_R',old)
 replace(owner,old,new,'D20','Use zeta_R for the real auxiliary line coordinate, retaining every factor, inverse, cocycle and physical z coordinate in the subsequent charts.')
replace('LF',r'frame and vector coordinate are $e_m=\chi^{-m}e$ and $z_m=\chi^mz$;',
 r'frame and holomorphic vector coordinate are $e_m=\chi^{-m}e$ and $\zeta_m=\chi^m\zeta$;',
 'D20;D22','State the same mutually inverse frame/vector maps using the holomorphic vector coordinate already defined by h,F,J.')
replace('LF',r'\psi(t)=t^tKt',r'\psi(v)=v^tKv','D20','Separate the fan lattice variable v from circle and Borel variables.')
replace('LF',r'2h^tKt+h^tKh',r'2h^tKv+h^tKh','D20','Use the declared fan lattice variable in its exact period difference.')
replace('LF',r'\psi_{\rm ph}(Ct)&=-t^tKt+a(\nu t_1-brt_2).',
 r'\psi_{\rm ph}(Cv)&=-v^tKv+a(\nu v_1-brv_2).',
 'D20','Retain the exact C pullback and affine gauge using the same lattice variable.')
replace('LF','In degree two the kernel of restriction to $Y$\nis spanned by the base class $t$ and',
 'Let $T=c_1(\\text{positive circle character})$ and $t_3=\\rho_3(T)$.\nIn degree two the kernel of restriction to $Y$\nis spanned by the base class $t_3$ and',
 'D20','Define the integral circle character before use and name its finite reduction explicitly.')
replace('LF','has one common base coefficient $h$ on both components. The mixed\nproducts vanish on each finite isotropy section. Replace $U$ by\n$U-hT$, with inverse addition of $hT$, where $T$ is the positive\ncircle character. Both finite point characters now vanish.',
 'has one common base coefficient $c_B$ on both components. The mixed\nproducts vanish on each finite isotropy section. Replace $U$ by\n$U-c_BT$, with inverse addition of $c_BT$. Both finite point\ncharacters now vanish.',
 'D20;D22','Separate the common Borel coefficient from the deck map h and retain the one global adjustment with its inverse.')

# The universal general cochain scope of the original LJ proof survives once.
old=r'''For this normalization, Thomas's cochain formula is
\begin{equation}
 P_3(v)=(v^3,0)+(\Sigma^*v^2\delta v,1)
\hypertarget{tag-Q226}{}\label{maps:eq:third-power-cochain}
\end{equation}
\cite[(3.3)--(3.6), p.~268]{ffThomas56}.
For an integral cocycle the second term vanishes. The degree-zero
part of the diagonal carrier may be the iterated Alexander--Whitney
diagonal with augmentation one, and the carried homotopy identifies
any other such choice with it. Its product is consequently the
ordinary cube with coefficient one. This identifies Thomas's operation
with $Q_3$, including its coefficient map.
His odd-index suspension theorem gives'''
new=r'''Thomas's odd-prime operation, for the coefficient groups
$\mathbb Z/(pm)$ and $\mathbb Z/(p^2m)$, has the cochain representative
\begin{equation}
 \begin{aligned}
 P_p(v)&=(v^p,0)+(\Sigma^*v^{p-1}\delta v,1),\\
 P_3(v)&=(v^3,0)+(\Sigma^*v^2\delta v,1)\qquad(p=3,\ m=1).
 \end{aligned}
\hypertarget{tag-Q226}{}\label{maps:eq:third-power-cochain}
\end{equation}
Here $p$ is an odd prime and $m$ is a positive integer
\cite[(2.1),(2.6),(2.7), p.~267; (3.3)--(3.6), p.~268]{ffThomas56}.
For an integral cocycle the second term vanishes. The degree-zero
part of the diagonal carrier may be the iterated Alexander--Whitney
diagonal with augmentation one, and the carried homotopy identifies
any other such choice with it. Its product is consequently the
ordinary $p$-th power with coefficient one. For $p=3,m=1$ this
identifies Thomas's operation with $Q_3$, including its coefficient map.
The odd-prime relative construction gives vanishing on relative
boundaries and suspensions; the external-product identity reduces the
suspension to the zero product on the dimension-one interval factor.
Its order-three specialization is'''
replace('LF',old,new,'D06;D12;D17;D22;D26;D27',
 'Retain the original LJ general odd-prime coefficient/cochain and relative-boundary/suspension scope once, before its exact p=3,m=1 specialization. The retained Q226 identity now contains both the original general formula and the previously labeled specialization; no auxiliary mathematical scope is discarded.')

# Borel sphere hyperplane classes are different symbols from physical z.
for owner,start,stop in [
 ('LF','Put $A=a(\\nu-k)$ and let $z=',r'\paragraph{The coefficient-one detector'),
 ('LF','The normal roots on $C_0$ are', 'The action on the elliptic component'),
 ('LJ','On \\(C_f\\), set \\(A=a(\\nu-k)\\)', 'At \\(E_3\\), the actual primitive periods')]:
 old=between(start,stop)
 new=re.sub(r'\bz\b',lambda m:'z_C',old)
 replace(owner,old,new,'D20','Use z_C for the equivariant hyperplane class on the rational component, preserving every relation, normal root, integral and inverse marking; the physical chart coordinate z is unchanged.')
replace('LJ',r'\mathbb F_3t\oplus\mathbb F_3\eta\rho_3\xi.',
 r'\mathbb F_3t_3\oplus\mathbb F_3\eta\rho_3\xi.',
 'D20','Use t_3 for the mod-three circle character on the elliptic Borel space.')
replace('LJ','The common zero isotropy character removes the first coefficient.',
 'Here $t_3=\\rho_3(T)$ is the restricted positive circle character.\nThe common zero isotropy character removes the first coefficient.',
 'D20','Specify the exact restriction defining t_3 before the mixed elliptic class is used.')
replace('LJ',r'a fixed curve be \(x_1,x_2\), and their characters be \(\lambda,-\lambda\).',
 r'a fixed curve be \(x_1,x_2\), and their characters be \(\lambda,-\lambda\).'+
 '\nPut $t_p=\\rho_p(T)$ for the restricted positive circle character.',
 'D20','Define the base class in the odd-primary normal-root calculation separately from the model index t.')
replace('LJ',r'2\lambda^2t^2+2\lambda t(x_1-x_2)',r'2\lambda^2t_p^2+2\lambda t_p(x_1-x_2)',
 'D20','Retain the exact root expansion in the declared primary Borel character.')
old=between(r'Choose \(n_0\theta+A_0\sigma=1\)',r'With \(S=(u,\delta)')
new=old.replace(r'\theta',r'\theta_N')
replace('LJ',old,new,'D20','Name the nodal Bezout integer theta_N, leaving the scalar-circle parameter theta and every determinant/inverse unchanged.')
for old,new in [('free C9 spaces','free $C_9$ spaces'),('restriction to C9','restriction to $C_9$'),('multiplies by C3','multiplies by $C_3$'),('specified C3 generator','specified $C_3$ generator')]:
 replace('LF',old,new,'D08','Typeset the previously defined cyclic group as a mathematical symbol in prose.')

# The previous proof-heading regex matched no proof delimiters. Correct it
# using a literal delimiter, and account for both complete proofs.
proofs=[(m.start(),text.index(r'\end{proof}',m.end())) for m in re.finditer(re.escape(r'\begin{proof}'),text)]
assert len(proofs)==2
heading_counts=[]
for a,b in reversed(proofs):
 old=text[a:b];block=old
 heads=list(re.finditer(r'\\paragraph\{([^\n]+)\}',block))
 heading_counts.append(len(heads))
 for h in reversed(heads):
  title=re.sub(r'^\d+[a-z]?\.\s*','',h[1]).replace('Exhaustion from the defining raw profiles.','Exhaustion of minimal fillings.').replace('The C9 localization',r'The $C_9$ localization')
  block=block[:h.start()]+r'\item \emph{'+title+'}'+block[h.end():]
 block=block.replace(r'\begin{proof}',r'\begin{proof}'+'\n'+r'\begin{enumerate}',1)+r'\end{enumerate}'+'\n'
 owner='LF' if a<text.index(r'\subsubsection{Orders six') else 'LJ'
 replace(owner,old,block,'D13;D14;D19',
  'Finish the ordered-proof conversion missed by the first publication script: one proof, automatically numbered mathematical stages, no manual paragraph numbers, and every mathematical stage retained.')
assert sorted(heading_counts)==[8,13]

units.check_permanent_identifiers(original,text)
assert text.count(r'\begin{enumerate}')==text.count(r'\end{enumerate}')==2
assert r'\paragraph{' not in text and r'\mathrm{II}I' not in text
assert r'k\max r<1' not in text and '\r' not in text
assert text.count(r'\begin{proof}')==text.count(r'\end{proof}')==2
table=lane/'S6_SERIES_PUBLISH_THREE_publication_defects.tsv'
with table.open(newline='') as f:
 reader=csv.DictReader(f,delimiter='\t');fields=reader.fieldnames;rows=list(reader)
for i,(owner,kinds,line,old,new,why) in enumerate(edits,1):
 for kind in kinds.split(';'):
  rows.append(dict(zip(fields,[f'III-C8-THREE-READBACK-{i:03d}-{kind}',kind,
   'maps:src:D.2.'+('39' if owner=='LF' else '42'),
   f'three_primary_types.tex readback sequential edit line{line}',
   'pending page concordance','weighted/three_primary_types.tex','pending final build',
   old,new,why,'whole 2340-line candidate read; bounded correction readback pending; global gates open'])))
with table.open('w',newline='') as f:
 writer=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');writer.writeheader();writer.writerows(rows)
p.write_text(text,newline='\n')
diff=''.join(difflib.unified_diff(original.splitlines(True),text.splitlines(True),fromfile='THREE2340_wholly_read',tofile='THREE_readback_corrected'))
(lane/'S6_SERIES_PUBLISH_THREE_readback_corrections.diff').write_text(diff,newline='\n')
print('UTC',datetime.now(timezone.utc).isoformat())
print('LINES',len(original.splitlines()),'TO',len(text.splitlines()),'BOUNDED_EDITS',len(edits),'TOTAL_SINGLE_TYPE_ROWS',len(rows))
print('PROOF_STAGES_LF8_LJ13; ALL_IDENTITIES_PRESERVED; OLD_GENERAL_COCHAIN_SCOPE_RETAINED; NO_SHARED_WRITES_OR_AUTOMATIC_CREDIT')
print('SHA256',hashlib.sha256(p.read_bytes()).hexdigest())
