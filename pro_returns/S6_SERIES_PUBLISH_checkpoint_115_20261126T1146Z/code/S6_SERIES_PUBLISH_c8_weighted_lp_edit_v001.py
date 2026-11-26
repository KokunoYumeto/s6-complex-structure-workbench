"""Publication edit of the wholly read weighted Engel unit."""
import csv
from datetime import datetime, timezone
import difflib
import hashlib
from pathlib import Path
import re
import S6_SERIES_PUBLISH_c8_integrate_presentation as presentation
import S6_SERIES_PUBLISH_c8_integrate_units as units
root=Path(__file__).resolve().parent.parent
lane=root/'agents/continuation8_iii_weighted_units'
p=root/'agents/continuation8_iii_integration/units/weighted/weighted_engel_types.tex'
original=p.read_text();text=original
assert hashlib.sha256(p.read_bytes()).hexdigest()=='622ded23fa1ab43e632f49b461e6ca74215cf0df1054345e2448ec27223533d8'
receiver=(root/'agents/continuation7_iii_weighted_cups_receiving/S6_SERIES_PUBLISH_III_02LP_receiving.tex').read_text()
print('REPAIRED_INPUT_VS_RECEIVER_DIFF')
print(''.join(difflib.unified_diff(receiver.splitlines(True),original.splitlines(True),fromfile='admitted910',tofile='repaired914')),end='')
assert [x for x in receiver.splitlines() if x.strip()]==[x for x in original.splitlines() if x.strip()]
edits=[]
def change(old,new,kinds,why,count=1):
 global text
 assert text.count(old)==count,(old[:180],text.count(old),count)
 for _ in range(count):
  a=text.index(old);edits.append((kinds,text.count('\n',0,a)+1,old,new,why))
  text=text[:a]+new+text[a+len(old):]
def between(start,stop):
 a=text.index(start);return text[a:text.index(stop,a)]

old=between(r'\begin{theorem}', 'The manifold is simply connected.')
eq=old[old.index(r'\['):old.index(r'\]')+2]
new=r'''\subsection{Weighted Engel smooth types}

\begin{definition}[Weighted Engel data]\hypertarget{tag-Q250}{}\label{maps:def:weighted-engel-data}
{\normalfont\scriptsize tag Q250}\par
For every positive integer $d$, use the weight-$d$ Engel construction
of \ref{maps:src:D.2.34} and its prescribed cusp fan. Replace both
additive sites by good logarithmic caps, allowing every positive
integer $k,\ell$, every integer $r_i,n_i$, and every affine twist
in that construction, subject to
'''+eq+r'''
Here $u_i$ is the marked fixed direction at site $i$ of that construction.
Define $M_d$ to be the member with $k=\ell=1$, $n_0=1$, $n_1=-1$
and $r_0=r_1=0$, with the complex orientation. Its determinant is one.
These are the \emph{weighted Engel data}.
\end{definition}

\begin{theorem}[Weighted Engel smooth classification]\hypertarget{tag-02LP}{}\label{maps:src:D.2.48}
{\normalfont\scriptsize tag 02LP}\par
Every output $X$ of Definition~\ref{maps:def:weighted-engel-data}
is simply connected. Its complex first and second
'''
change(old+'The manifold is simply connected.  Its complex first and second\n',new,
 'D04;D05;D10;D11;D13;D14;D16;D26',
 'Put the complete positive-weight, positive k/ell, integer n/r and affine-lift domain in Q250, retaining the exact unit determinant and marked fixed directions. Define the actual universal realizing member Md. Keep the complete theorem and one proof.')
old=r'''Here $P_{\mathrm{ref}}$ denotes Zhubr's class, to distinguish it from
the Seifert determinant $P$ in \eqref{maps:eq:D.WI1}.'''
new=r'''Here $P_{\mathrm{ref}}\in H_2(X;\mathbb Z)$ is Zhubr's refined
class, and $P$ in \eqref{maps:eq:D.WI1} is the Seifert determinant.
Write $\mathcal D_X:H^4(X;\mathbb Z)\to H_2(X;\mathbb Z)$ for
$c\mapsto c\frown[X]$, with inverse Poincar\'e duality, and put
$\mathfrak p_X=\mathcal D_X^{-1}(P_{\mathrm{ref}})$.
Thus $\mathfrak p_X\frown[X]=P_{\mathrm{ref}}$.'''
change(old,new,'D20;D22','Bind the homological refined invariant and cohomological obstruction by the actual cap-product isomorphism and its inverse; preserve all values and pairings.')
change(r'\operatorname{PD}\lambda',r'\mathcal D_X(\lambda)','D20','Use the declared cap-product map in the exact doubling identity.',2)
change(r'has obstruction $\operatorname{PD}P_{\rm ref}$.',r'has obstruction $\mathfrak p_X$.','D20','Use the cohomological complementary obstruction under the declared inverse cap map.')
change(r'\operatorname{lk}(N,\operatorname{PD}P_{\rm ref})',r'\operatorname{lk}(N,P_{\rm ref})','D20',
 'Write linking on its actual H3-by-H2 inputs. The former shorthand composed the cap-product identification; the displayed identity and full rational value are unchanged.')
change(r'''Here linking against a degree-four cohomology class means linking
against its Poincar\'e-dual two-cycle, fixing the convention in
the displayed expression.''',r'''The complementary cochain represents $\mathfrak p_X$.
Its cap product with $[X]$ is $P_{\rm ref}$, and the inverse map
is $\mathcal D_X^{-1}$. Thus $q/\operatorname{ord}(N)$ is the
linking with the displayed homology class.''','D20;D22',
 'Give the exact cochain-to-homology map and inverse at the relative linking step; no smooth or refined invariant is changed.')

# Put the complete detector target before its mixed and pure evaluations.
old=between(r'\item \emph{The complete integral target and inverse detectors.}',r'\item \emph{A finite-cap detector')
new=old.replace(r'''Consequently \eqref{maps:eq:D.WI15}
is the full fundamental-class invariant, with its precise
two- and three-primary coordinates.''',r'''Thus the evaluations in \eqref{maps:eq:D.WI15} determine the
entire fundamental-class invariant, including its two- and
three-primary coordinates. We compute these evaluations next.''')
change(old,'','D14','Move the entire Cartan elementary-complex, CPj, coefficient and Kunneth detector proof before the mixed/pure evaluations; every old auxiliary and D.WI22 identity remains.')
marker=r'\item \emph{The full mixed coordinates.}'
change(marker,new+'\n'+marker,'D14;D22','Establish the full integral target and both detector maps before reconstructing any fundamental-class coordinate.')
old=r'''Distinct prime components have relatively prime positive homology
orders, so their tensor and torsion products vanish. The Chinese
remainder isomorphism gives \eqref{maps:eq:D.WI22} for all $d$.'''
new=r'''Distinct prime components have relatively prime positive homology
orders, so their tensor and torsion products vanish. Write
$d=\prod_{p\mid d}p^{f_p}$ and, for $j=1,2,3$, put
$D_{j,p}=p^{f_p+v_p(j)}$ and $D_1=d$.
The coefficient reduction sends $g$ to $g_p$ and hence
$\gamma_j(g)$ to $\gamma_j(g_p)$, the positive reduced
$\mathbb{CP}^j$ generator in that factor. Choose
$c_{j,p}(D_j/D_{j,p})\equiv1\pmod{D_{j,p}}$.
The complete coordinate maps and inverse are
\[
 z\longmapsto(z\bmod D_{j,p})_{p\mid d},\qquad
 (z_p)_p\longmapsto
 \sum_{p\mid d}(D_j/D_{j,p})c_{j,p}z_p\pmod{D_j}.
\]
Each summand is one on its own factor and zero on the others,
so both composites are identity. At $j=1$ these are the underlying
coefficient maps; their induced Eilenberg--Mac Lane maps are inverse.
This proves \eqref{maps:eq:D.WI22} for all $d$; at $d=1$ each
group is zero. The argument retains the positive divided-power
generator at each stage.'''
change(old,new,'D20;D22;D26','Write the actual arbitrary-d primary coordinate and inverse maps on each full D_j, including the extra 2/3 factors, and identify their CPj generators. Preserve the complete integral detector scope.')

# The previously proved general parity identity applies to the same framed
# three-manifold. Retain all of LP's explicit quaternion convention maps.
old=between(r'\item \emph{The actual tangent-parallelization parity.}',r'\item The following normal columns')
eq=old[old.index(r'\['):old.index(r'\]')+2]
new=r'''\item \emph{The tangent-parallelization parity.}
Apply \eqref{maps:eq:D45.15} to the closed oriented three-manifold
$N$ with the tangent parallelization obtained by the two projections
above. The identification with that statement's input is the identity
on $(N,TN)$ and on its projected frame, with identity inverse. Its
induced spin structure is the one used by the prescribed-spin filling
there. The coordinate maps in \eqref{maps:eq:D.WI9} and their
inverses reduce modulo two to identify
$H_1(N;\mathbb F_2)=\mathbb F_2^2$.

The explicit convention maps in that parity identity are as follows.
For $\operatorname{Spin}(4)=SU(2)_L\times SU(2)_R$, the action is
$(q_L,q_R)v=q_Lvq_R^{-1}$, with inverse action
$v\mapsto q_L^{-1}vq_R$. The factors are two-connected, so a map
from $N$ is determined by its two integer degrees $A,B$; inverse
representatives are the two degree maps supported in a positive
three-ball. The first column is $q_Lq_R^{-1}$, of degree $A-B$.
Stabilization has parity $A+B\pmod2$, because the two half-spin
summands have equal stable Pontryagin magnitude and opposite Euler
contributions. The quaternionic generator has framed coefficient one.
These are precisely the first-column and stable maps in the proof of
\eqref{maps:eq:D45.15}; its prescribed-spin handle and even-rank
intersection argument proves their parity is
$1+\dim H_1(N;\mathbb F_2)$ for every tangent parallelization and
its specified spin structure
\cite[Definition~1.7, Remark~1.8 and Theorem~3.1, pp.~239--240,243--246]{mapsKaplan79}.
For the present $N$ this gives
'''+eq+'\n\n'
change(old,new,'D06;D12;D17;D20;D22;D26',
 'Consolidate only the repeated general Kaplan/intersection derivation through the exact same (N,TN,tangent frame,induced spin) input to LM D45.15. Preserve its universal all-parallelization scope, all explicit Spin4 quaternion/action/inverse/degree maps, and D.WI10 at the actual dimension-two detector conclusion.')

# Correct proof order for the global vertical frame, retaining every map.
old=r'''A Hermitian complement to
$\delta$ and a unit section give a global frame $(\delta,v_2)$ of $V$.
Outside the critical cycle, a unit frame of $L$ lifts through
$df^*/\|df\|^2$; kernel projection and $df$ give its inverse.
'''
change(old,'','D14','Place the global frame and differential splitting after their line-triviality proof; no construction is removed.')
marker='Thus $V$ and $L$ admit full smooth frames.\n'
change(marker,marker+old,'D14;D22','Use the already proved trivial quotient and target to construct the full frame and its explicit inverse differential splitting.')

# Fix the actual action and orientation comparisons explicitly.
change(r'''Reversing the scalar generator reverses all weights and characters,
giving $\epsilon=1$. This is the precise comparison of the two
support conventions, and is compatible with $j\mapsto j+d$.''',r'''The circle automorphism $z\mapsto z^{-1}$, with itself as inverse,
induces $t\mapsto-t$ and negates every weight and character.
It sends $(\lambda_0,\epsilon)$ to $(-\lambda_0,1)$ in this
formula. The monomial frame maps above compare the two support
conventions, and both descriptions respect $j\mapsto j+d$.''',
 'D20;D22','Give the actual circle inversion and its action on the Borel character, while preserving the negative physical support weights and exact monomial frame transport.')
change('up to the common harmless orientation sign.  It is odd.',r'''The orientations here are those of \eqref{maps:eq:D.WI11}, with
the cap-one $a$ normal intersecting $N$ positively. Reversing the
orientation of $N$ negates both linking values by linearity on chains;
the inverse is the same orientation reversal. In either orientation
this integer is odd.''','D02;D20;D22',
 'Tie the printed link to the already fixed Thom intersection and give the orientation-reversal map/inverse explicitly. Preserve both orientation conventions and the odd parity used in the full transgression.')

# Mathematical stage headings on every previously untitled proof item.
headings=[
 (r'\item Remove the divisorial',r'\item \emph{The corrected differential and reference frame.}'+'\n'+r'Remove the divisorial'),
 (r'\item The local Bott clutch',r'\item \emph{The complete critical cycle.}'+'\n'+r'The local Bott clutch'),
 (r'\item At a finite cap let',r'\item \emph{Extension across the finite caps.}'+'\n'+r'At a finite cap let'),
 (r'\item On every normalized cusp component',r'\item \emph{Component restrictions and the homology splitting.}'+'\n'+r'On every normalized cusp component'),
 (r'\item The scalar circle action',r'\item \emph{The fixed curves and the free complement.}'+'\n'+r'The scalar circle action'),
 (r'\item Since $H_1(X;',r'\item \emph{The common Borel character.}'+'\n'+r'Since $H_1(X;'),
 (r'\item Suppose now that $3\mid d$.',r'\item \emph{The full third-power operation.}'+'\n'+r'For the weights divisible by three,'),
 (r'\item Restrict to $C_N$',r'\item \emph{Localization at the full third-power modulus.}'+'\n'+r'Restrict to $C_N$'),
 (r'\item For arbitrary integers',r'\item \emph{The pure cyclic coordinate.}'+'\n'+r'For arbitrary integers'),
 (r'\item The following normal columns',r'\item \emph{The integral normal chain and linking number.}'+'\n'+r'The following normal columns')]
for old,new in headings:change(old,new,'D13;D14;D16','Give the existing complete proof step a descriptive mathematical heading; automatic enumeration retains its order.')

# Occurrence-level publication prose; keep every equation and map.
changes=[
 ('With repetitions retained when','Counting both directed incidences when','D08;D20','State the exact d2 incidence multiplicity.'),
 ('The maps retain all cusp boundary torsion','The maps include all cusp boundary torsion','D08','Preserve the complete integral boundary group.'),
 ('Apply its normal-disc and period-cylinder maps to the current\nholomorphic period functions, retaining their units.',
  'Apply its normal-disc and period-cylinder maps to the\nholomorphic period functions of this construction, including all units.','D08;D22','Use the actual period substitution and inverse, without version language.'),
 ('The root-loop column $g$ is retained. This is the Thom','The zero $g$ column is part of the Thom','D08;D22','State the full root-loop obstruction instead of recording its retention.'),
 ('the target retains its order-two kernel under reduction modulo $d$.',
  'reduction of this target modulo $d$ has its order-two kernel.','D08;D20','Keep the full2d target and its exact reduction kernel.'),
 ('The mixed coordinates retain the full modulus $D_2$ proved above.',
  'The mixed coordinates have the full modulus $D_2$ computed above.','D08','State the complete mixed coefficient scope.'),
 ('type already identified in \\ref{maps:src:D.1.11}.','type in \\ref{maps:src:D.1.11}, under the marking proved below.','D08;D22','Name the exact earlier prime-to-six recognition and its inverse marking.'),
 ('Thus every adjusted free generator and the positive cyclic generator\nhave the stipulated images in both directions.',
  'Thus every adjusted free generator and the positive cyclic generator\nhave the displayed images in both directions.','D08','State the actual marked diffeomorphism maps.')]
for args in changes:change(*args)
for pattern,replacement,why in [
 (r'\bactual\s+','', 'Remove workflow emphasis while preserving the full mathematical object and proof.'),
 (r'\bliteral\s+','', 'State the integral cycle or covering directly.'),
 (r'\bcurrent\s+','', 'Refer to the constructed manifold directly.')]:
 for m in reversed(list(re.finditer(pattern,text))):
  edits.append(('D08',text.count('\n',0,m.start())+1,m[0],replacement,why))
  text=text[:m.start()]+replacement+text[m.end():]
change('an tangent parallelization','a tangent parallelization','D23','Correct the article after removing workflow emphasis.')

# All citation locations are unchanged primary scopes, with standard spacing.
for old,new in [
 ('equations (2.1), (2.8), and (3.4), pp.267--268','equations~(2.1), (2.8) and~(3.4), pp.~267--268'),
 ('equation (2.1), p.267','equation~(2.1), p.~267'),
 ('equations (3.4)--(3.6), p.268','equations~(3.4)--(3.6), p.~268'),
 ('equations (2.8), (3.4), pp.267--268','equations~(2.8), (3.4), pp.~267--268'),
 ("Expos\\'e 11, Theorems 1 and 4, pp.11-09--11-13; Appendix 1, pp.11-22--11-23", "Expos\\'e~11, Theorems~1 and~4, pp.~11-09--11-13; Appendix~1, pp.~11-22--11-23"),
 ('Theorem 1 and Section 5, pp.6,8--9','Theorem~1 and Section~5, pp.~6,8--9'),
 ('Theorems 3,5 and Section 4.1, pp.795--796,809--810','Theorems~3,5 and Section~4.1, pp.~795--796,809--810')]:
 change(old,new,'D18','Use scholarly citation spacing at the exact already inspected primary locus.')

before=text
text,changes,issues=presentation.statement_records_to_small_tags(text)
assert not changes and not issues
text,changes,issues,aliases=presentation.remove_manual_equation_tags(text)
assert not issues
for c in changes:edits.append((c.kind,before.count('\n',0,c.start)+1,c.old,c.new,c.reason))
assert not presentation.unresolved_literal_equation_references(text,aliases)
units.check_permanent_identifiers(original,text,['maps:def:weighted-engel-data'],['tag-Q250'])
assert text.count(r'\begin{definition}')==text.count(r'\end{definition}')==1
assert text.count(r'\begin{theorem}')==text.count(r'\end{theorem}')==1
assert text.count(r'\begin{proof}')==text.count(r'\end{proof}')==1
assert r'\tag{' not in text and '\r' not in text
fields=['change_id','type','statement_id','old_location','old_page','new_location','new_page','old_text','new_text','reason','review_status']
rows=[]
for i,(kinds,line,old,new,why) in enumerate(edits,1):
 for kind in kinds.split(';'):
  rows.append([f'III-C8-LP-PUB-{i:03d}-{kind}',kind,'maps:src:D.2.48',f'weighted_engel_types.tex sequential edit line{line}',
   'pending page concordance','weighted/weighted_engel_types.tex','pending final build',old,new,why,
   'whole input/originals/comparison/source/root evidence read; complete candidate readback pending; global gates open'])
p.write_text(text,newline='\n')
with (lane/'S6_SERIES_PUBLISH_LP_publication_defects.tsv').open('w',newline='') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n');w.writerow(fields);w.writerows(rows)
print('UTC',datetime.now(timezone.utc).isoformat(),'LINES',len(original.splitlines()),'TO',len(text.splitlines()),'EXACT_EDITS',len(edits),'DEFECT_ROWS',len(rows))
print('NEW_Q250_DEFINITION; ALL31_OLD_IDENTITIES_PRESERVED; NEXT_Q251; NO_MATHEMATICAL_REFUTATION; NO_INDEPENDENT_CREDIT')
print('SHA256',hashlib.sha256(p.read_bytes()).hexdigest(),'SHARED_WRITES0; AUTOMATIC_CRITERION_CREDIT0')
