"""Bounded corrections after reading the full1368-line LV candidate."""
import csv
from datetime import datetime, timezone
import hashlib
from pathlib import Path
import re
import S6_SERIES_PUBLISH_c8_integrate_units as units
root=Path(__file__).resolve().parent.parent
lane=root/'agents/continuation8_iii_weighted_units'
p=root/'agents/continuation8_iii_integration/units/weighted/weighted_os45.tex'
original=p.read_text();text=original
assert hashlib.sha256(p.read_bytes()).hexdigest()=='21cbfe4e3543c96d8466c3183a701812d4a6b5b0fd86b39759a29bb7a0a4d7cd'
edits=[]
def change(old,new,kinds,why,count=1):
 global text
 assert text.count(old)==count,(old[:180],text.count(old),count)
 for _ in range(count):
  at=text.index(old);edits.append((kinds,text.count('\n',0,at)+1,old,new,why))
  text=text[:at]+new+text[at+len(old):]
def between(start,stop):
 at=text.index(start);return text[at:text.index(stop,at)]
change('an global bounding','a global bounding','D23','Correct the article after removing workflow emphasis.')
change('edges and triangle cells are in this formula.','edges and triangle cells are counted with their geometric multiplicities.','D20;D23','Keep the exact repeated-incidence meaning in a complete sentence.')
change('The torsion character in the original nine coordinates is','The torsion character in the nine coordinates of that marked presentation is','D04;D08','Refer to the defined peripheral presentation without historical-version language.')
change(r'\mathbb Zu',r'\mathbb Zt','D20','Complete the identity renaming of the integral Borel character in the OR11 kernel; finite u is unchanged.')
old=r'''Apply the complete primary calculation of \ref{maps:src:D.2.48}
with $r=15$ and $d=8$. Its $D_2=16$ and $D_3=8$, and
its positive cyclic generator is carried to $\tau$ by the splitting
\eqref{maps:eq:D.OF15}, with the evaluation inverse given there.
The integral K\"unneth decomposition therefore gives'''
new=r'''Use the cyclic homology calculation \eqref{maps:eq:D.WI22} at $d=8$:
its degrees two, four and six have orders $8,16,8$, with their
positive reduced projective-space generators. The splitting
\eqref{maps:eq:D.OF15} sends the positive cyclic generator to $\tau$.
Its fifteen integral coordinate projections and cyclic projection induce
\[
 K(\mathbb Z^{15}\oplus\mathbb Z/8,2)
 \longrightarrow(\mathbb{CP}^{\infty})^{15}\times K(\mathbb Z/8,2).
\]
The inverse is induced by the sum of the fifteen free inclusions and
the cyclic inclusion. Both composites induce identity on $\pi_2$;
the Eilenberg--Mac Lane classification makes them inverse up to based
homotopy. The free factor has free even homology and no odd homology.
The integral K\"unneth map has no torsion-product term and gives'''
change(old,new,'D06;D20;D22;D26',
       'Apply the arbitrary-d cyclic homology identity, then the actual rank15 product map/inverse. This avoids suggesting that the LP geometric-family relation r=d-1 can be specialized to r15,d8; no LP geometric theorem is applied outside its domain.')
old=between('last by \\(u^3\\). More explicitly, write', 'The boundary class that enters this remaining calculation')
new=old.replace(r'$e_0,\ldots,e_{14}$',r'$\varepsilon_0,\ldots,\varepsilon_{14}$')
new=new.replace(r'\gamma_\alpha(e)',r'\gamma_\alpha(\varepsilon)').replace(r'\gamma_\beta(e)',r'\gamma_\beta(\varepsilon)').replace(r'K_i e_i\gamma_2',r'K_i\varepsilon_i\gamma_2')
change(old,new,'D20','Use epsilon_i for the abstract free model generators, keeping the physical periods e1,e2 distinct in the ensuing boundary and sphere maps. The basis correspondence is identity in the displayed ordered coordinates.')

# Put the actual boundary-chain construction with the source-sphere proof.
old=between('The boundary class that enters this remaining calculation',r'\item \emph{The source sphere and refined class}')
new=old.replace('The boundary class that enters this remaining calculation has an\nexplicit integral prism description. Put',
                'The boundary class used to construct the sphere has the following\nintegral prism description. Put')
new=new.replace(r'\alpha',r'\alpha_{\partial}')
change(old,'','D14;D20','Move the full boundary-prism and cap-sweep argument to the source-sphere stage and distinguish its class alpha_partial from the complex sphere coordinate alpha.')
marker='complex critical curves, with the chain $B_C$ constructed above.\n'
change(marker,marker+new,'D14;D20;D22','Place the complete exact-order and two-nullchain construction before the sphere whose Mayer-Vietoris boundary it computes.')
change(r'a_i\wedge\delta=\alpha=e_1\wedge\delta',r'a_i\wedge\delta=\alpha_{\partial}=e_1\wedge\delta','D20','Use the same explicitly named boundary class in the source meridian calculation.')
old=between('The unperturbed sphere has Mayer--Vietoris boundary',r'\item \emph{The exact reference frame')
new=old.replace(r'\alpha',r'\alpha_{\partial}')
new=new.replace('Here is the integral detector that proves the needed oddness.','Its oddness is detected by the following integral boundary character.')
change(old,new,'D08;D20','Keep the complete split Wang character on the full boundary group and use alpha_partial consistently, without shadowing the sphere coordinate.')
change('markings in the statement.','markings of Definition~\\ref{maps:def:weighted-os45-data}.','D06','Point to the relocated complete input definition.')

# Explicit left Lie coordinates and the nonzero Bott homotopy.
old=r'''In the left complex Lie frame of $SL_2(\mathbb C)$ the $\delta$ vector is
constant diagonal and, on the other two coordinates, $df=ac\,u+bd\,v$.'''
new=r'''At $g=\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)$,
left multiplication identifies the Lie algebra with the tangent space;
its inverse multiplies by
$g^{-1}=\left(\begin{smallmatrix}d&-b\\-c&a\end{smallmatrix}\right)$.
The scalar vector is $g\operatorname{diag}(-1,1)$, and
\[
 df\bigl(g(\zeta_1E_{12}+\zeta_2E_{21})\bigr)
                          =ac\zeta_1+bd\zeta_2.
\]
This is the left complex Lie frame, with its two off-diagonal coordinates.'''
change(old,new,'D20;D22',
       'Give the exact left-trivialization and inverse, identifying the fixed delta vector and using zeta coordinates rather than shadowing the finite class u.')
old=r'''The pair has no common zero for $\varepsilon>0$: off the axes the two
equations imply $z_1=-\varepsilon^2z_1$, with
$z_1=\overline\alpha,z_2=\overline\beta$, and on each axis the remaining
term is nonzero.  Increasing $\varepsilon$ and normalizing gives the
pair $(z_1^2,-z_2^2)$.  The proper holomorphic quadratic map has four
regular preimages, all of positive real local degree.  Radial
normalization and simultaneous conjugation therefore give degree four
for this Bott matrix.'''
new=r'''For $0\leq s\leq1$, set
\[
 F_s=\bigl((1-s)\beta\overline\alpha+\varepsilon\overline\alpha^2,
          (1-s)\alpha\overline\beta-\varepsilon\overline\beta^2\bigr).
\]
At $s=0$ this is $(B,-A)$. It has no common zero: off the axes
the equations imply $((1-s)^2+\varepsilon^2)\overline\alpha=0$,
and on either axis the remaining square term is nonzero.
The polar map $z\mapsto(z/\|z\|,\|z\|)$ has inverse
$(w,r)\mapsto rw$. Its first component applied to $F_s$ gives
the homotopy to the radial map of
$(\overline\alpha^2,-\overline\beta^2)$.
The proper holomorphic quadratic map $(z_1,z_2)\mapsto(z_1^2,-z_2^2)$
has four regular preimages, each of positive real local degree.
Simultaneous conjugation of both complex coordinates has real
determinant one. These maps therefore give degree four for the Bott matrix.'''
change(old,new,'D20;D22','Replace the implicit increasing-parameter/radial step by an explicit nowhere-zero homotopy and polar map/inverse. The original Bott degree4 and all reference conventions are unchanged.')
change('The normalization of this parity is the quaternionic left-multiplication',
       'The coefficient convention is fixed by the quaternionic left-multiplication','D20','Tie the parity convention directly to its explicit unit frame and stabilization map.')
change(r'''it with the scalar Hopf sphere.  Its orientation sign is retained; only
the parity of the ensuing unit is needed.  Form''',r'''it with the scalar Hopf sphere and is its own inverse. Conjugating
its first complex coordinate has real determinant $-1$, which is
its orientation sign on the unit sphere. The orientations below are
fixed by the positive scalar circle and quotient. Form''','D20;D22;D26',
       'Give the exact inverse and orientation of the Hopf conjugation instead of a parity-only scope phrase; preserve the signed integral link orientation.')

for old,new,why in [
 ('The following integer identities also record','The following integer identities also give','State the complete character-substitution identities directly.'),
 ('All their phases and nonzero holomorphic units are retained.','These maps include all phases and nonzero holomorphic units.','Keep the full quotient factors without comparison wording.'),
 ('Retain the nonzero endpoint units in','Write the nonzero endpoint units as','State the actual endpoint functions used in the embedding.'),
 ('pair above retains the corresponding relative unit.','pair above has the corresponding relative unit.','Keep the relative orientation convention directly.'),
 ('To verify the marking, retain all peripheral generators and the','To verify the marking, use all peripheral generators and the','Use the full marked presentation without editorial wording.'),
 ('and retain \\(A_0\\) from','and use \\(A_0\\) from','Use the same fixed cusp matrix directly.'),
 ('The ordinary fibre and strip classes\nare unchanged; in particular','The resulting fibre and strip evaluations include','State the actual core area value under the full sign map.')]:
 change(old,new,'D08',why)
for title in ['The primitive lattice, cubic and critical cycle','The cyclic coordinate and component evaluations','The source sphere and refined class']:
 change('\\emph{'+title+'}','\\emph{'+title+'.}','D23','Use consistent proof-stage title punctuation.')
change('\n \n\\begin{enumerate}[leftmargin=*]','\n\\begin{enumerate}[leftmargin=*]','D23','Remove a whitespace-only source line at the proof opening.')
units.check_permanent_identifiers(original,text)
assert '\r' not in text
table=lane/'S6_SERIES_PUBLISH_LV_publication_defects.tsv'
with table.open(newline='') as f:
 r=csv.DictReader(f,delimiter='\t');fields=r.fieldnames;rows=list(r)
assert len(rows)==409
for i,(kinds,line,old,new,why) in enumerate(edits,323):
 for kind in kinds.split(';'):
  rows.append(dict(zip(fields,[f'III-C8-LV-PUB-{i:03d}-{kind}',kind,'maps:src:D.2.53',f'weighted_os45.tex readback edit line{line}',
   'pending page concordance','weighted/weighted_os45.tex','pending final build',old,new,why,
   'complete candidate read; bounded follow-up reading pending; global gates open'])))
p.write_text(text,newline='\n')
with table.open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
print('UTC',datetime.now(timezone.utc).isoformat(),'BOUNDED_EDITS',len(edits),'TOTAL_EDITS',322+len(edits),'DEFECT_ROWS',len(rows))
for kinds,line,old,new,why in edits:
 print('CHANGED',kinds,'AT',line,'\n'+new)
print('LINES',len(text.splitlines()),'SHA256',hashlib.sha256(p.read_bytes()).hexdigest())
print('ALL71_IDENTITIES_PRESERVED; NO_NEW_MATH_REFUTATION; NO_INDEPENDENT_CREDIT; NO_SHARED_WRITES')
