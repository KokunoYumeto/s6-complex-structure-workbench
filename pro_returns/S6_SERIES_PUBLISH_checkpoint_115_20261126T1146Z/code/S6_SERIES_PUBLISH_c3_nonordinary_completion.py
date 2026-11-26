"""Read and complete the nonordinary triple and uniform tacnodal units."""
from S6_SERIES_PUBLISH_c3_edit import *

s=SOURCE.read_text(); i=s.index(r'\label{night:P4R.17}'); a=s.rfind(r'\begin{proposition}',0,i); b=s.index(r'\end{proof}',i)+len(r'\end{proof}'); old=s[a:b]; new=old
new=new.replace('In the remaining positive ruled case with uniform generic transverse\ntype $A_3$,',r'''In the setting of \cref{lem:II:positive-ruled-conductor-graph},
with generic transverse type $A_3$ along every conductor component,''',1)
a=new.index('Let \\(E_i\\subset K_i\\)'); b=new.index('Since the curve is nonplanar',a)
new=new[:a]+r'''Let \(E_i\subset K_i\) be the normalized conormal lattice, with
elementary-divisor orders \(e_1\le e_2\). Every first derivative of
\(f\) belongs to the radical ideal \(P\) of the critical curve, so
every Hessian column belongs to \(E_i\). Apply the column clause of
\cref{lem:II:rank-one-conormal-lattice} with
\(a=e_1,b=e_2,d=d_i,\beta=b_i\) and the same saturated Hessian line.
It gives
\[
                  \frac{d_i}{2}+b_i
                    \ge e_1+\frac{e_2}{2}.           \tag{A}
\]
This clause applies to every reduced defining equation with the
stated gradient condition, including its symbolic-square terms.

'''+new[b:]
new=new.replace(r'''Thus \(m\ge5\) gives \(D\ge19/2>9\). Only multiplicities three and four need inspection.''',r'''On a branch of multiplicity \(m_i\), the classes of
\(t_i,\ldots,t_i^{m_i-1}\) in its normalization quotient are linearly
independent, giving \(\delta_i\ge m_i-1\). The three branch values
modulo their common value add two gluing dimensions. Thus
\(\delta\ge\sum_i(m_i-1)+2=m-1\), and \(m\ge5\) gives
\(D\ge(m-1)+3+m/2\ge19/2>9\).
For the following multiplicity-three and multiplicity-four
classification, assume \(\delta=4\); the other delta invariants
are treated in the final item.''',1)
new=new.replace('The actual ring','The curve ring').replace('These are actual analytic ring isomorphisms.','These analytic ring isomorphisms give ambient isomorphisms as follows.').replace('the actual branch image','the branch image').replace('the actual reduced intersection ideal','the reduced intersection ideal')
new=new.replace(r'''Without restricting a symbolic-square coefficient of \(f\), (A) gives''',r'''The column estimate (A) gives''',1)
new=new.replace(r'''                         \begin{pmatrix}0&c\\c&0\end{pmatrix}.
\] A nonzero \(c\) gives a nonzero leading minor on the actual branch, contradicting generic rank one. Thus \(c=0\), and \(f\in\mathfrak m^4\).''',r'''                         x\begin{pmatrix}0&c\\c&0\end{pmatrix}.
\]
On the cusp, \(x=t^2+O(t^3)\) and \(y,z=O(t^3)\). The
\((y,z)\) block is therefore
\(t^2\left(\begin{smallmatrix}0&c\\c&0\end{smallmatrix}\right)
+O(t^3)\). Terms of degree at least four in \(f\) contribute
Hessian entries of order at least four on this branch. Its leading
minor is \(-c^2t^4\). Generic rank one forces \(c=0\), so
\(f\in\mathfrak m^4\).''',1)
new=new.replace('This exhausts multiplicity four. Together with Sections 1--2 it proves the strict local bound for every nonplanar three-branch curve with delta four. Only actual coordinate isomorphisms, conormal maps, and the rank-one Hessian were used; no boundary deformation has been introduced.','This exhausts multiplicity four. The multiplicity-three and multiplicity-four computations prove the strict local bound for every nonplanar three-branch curve with delta four.',1)
new=new.replace(r'''the ordinary nonplanar triple treated by \cref{night:P4.48} and the separate full-quartic conductor calculation.''',r'''the ordinary nonplanar triple treated by \cref{night:P4.48}, whose conductor equations and normalizations are determined in \cref{night:P4.47,night:P4.49}.''',1)
new,n=re.subn(r'\\par\\medskip\\noindent\\textbf\{(?:[1-4][ab]?\.) ([^}]+)\}\\par',lambda m:r'\item \emph{'+m[1]+'}',new)
assert n==8,n
new=new.replace('Bounds without an ordinary-square assumption','Bounds from Hessian columns')
for letter in 'ABCDEFGHIJKLM':
 pattern=r'\\\[([^\]]*?)\\tag\{'+letter+r'\}\s*\\\]'
 new,n=re.subn(pattern,lambda m:r'\begin{equation}\label{eq:II:nonordinary-triple-'+letter.lower()+'}\n'+m[1].rstrip()+'\n'+r'\end{equation}',new,count=1,flags=re.S)
 assert n==1,(letter,n)
 new=new.replace('('+letter+')',r'\eqref{eq:II:nonordinary-triple-'+letter.lower()+'}')
apply_edit(old,new,'II-C3-NONORDINARY-TRIPLE-COMPLETE',['D02','D04','D08','D12','D23','D25'],'night:P4R.17','Complete nonordinary three-branch unit',
 'Preserve all exact analytic generators, ambient inverse-function maps, conormal matrices and four numerical lower bounds. Transfer the weaker column estimate to the identical lattice in P259; prove delta>=m-1; correct the missing x factor in the cubic Hessian and give its cusp leading-minor calculation. Turn eight pseudoheadings into proof items and thirteen manual tags into equation labels. The statement remains at the original positive ruled domain.')

s=SOURCE.read_text(); i=s.index(r'\label{night:P4.50}'); a=s.rfind(r'\begin{proposition}',0,i); b=s.index(r'\end{proof}',i)+len(r'\end{proof}'); old=s[a:b]; new=old
new=new.replace('In the requested full-fibration classes, no support\nwith positive-genus ruled resolution has positive\nEuler number and generic transverse type $A_3$\non every critical-curve component.',r'''In the irreducible-or-normal-crossings setting of
\cref{def:II:standing-torus-fibration}, every support whose
normalization has a resolution ruled over a positive-genus curve
and whose generic transverse type is $A_3$ along every
critical-curve component has nonpositive Euler number.''',1)
new=new.replace(r'\item P4.42 and P4.44 leave only',r'''\item Let $mS$ be such a full fibre with $e(S)>0$, and write
$\rho=\nu\sigma:T\to N\to S$ for its resolved normalization.
The connected ruled surface $T$ is irreducible, and hence so is
its image $S$. Apply \cref{lem:II:positive-ruled-conductor-graph}
to this same $f,Y,B,mS,\nu,\sigma$.
P4.42 and P4.44 leave only''',1)
new=new.replace('Every additional singular critical-curve point has\nstrictly positive defect and therefore is absent.',r'''The equality
$\sum_{p\in C}(r_p-1)=2$ in
\cref{lem:II:positive-ruled-conductor-graph} is already exhausted
by this three-branch point. Every additional singular point of
the critical curve would therefore be unibranch. The local
inequalities in P4R.10 give strictly positive defect there,
so such points are absent.''',1)
new=new.replace('Its minimal resolution cannot contract the horizontal\npositive-genus section. This contradiction proves\nthe assertion.',r'''Let $E$ be the reduced exceptional fibre of this same
$\sigma:T\to N$ containing the horizontal positive-genus
section $H$. Apply the exceptional-cohomology argument in
\cref{night:P4.35} over a Stein neighbourhood of $\sigma(H)$.
Rationality gives $R^1\sigma_*\mathcal O_T=0$; the ideal
sequence of $E$ and the proved vanishing of $R^2\sigma_*$
give $H^1(E,\mathcal O_E)=0$. Its curve normalization
sequence then forces every normalized component of $E$
to have genus zero. This contradicts the positive genus
of $H$ and proves the assertion.''',1)
for name in ['P4.33','P4.42','P4.44','P4.47','P4.48','P4.49','P4R.10','P4R.14','P4R.16','P4R.17','P4R.6']:
 new=re.sub(r'(?<![:{])\b'+re.escape(name)+r'\b',lambda m:r'\cref{night:'+name+'}',new)
new=new.replace('(4.42a)',r'\eqref{eq:II:refined-4-42a}')
apply_edit(old,new,'II-C3-TACNODAL-COMPLETION-COMPLETE',['D04','D05','D25'],'night:P4.50','Complete uniform tacnodal completion unit',
 'Replace the undefined workflow domain by the same standing full-fibration definition. Map the given irreducible ruled image to P314, use its exact branch-identification equality for all additional singular points, and apply the existing exceptional-cohomology proof to this same resolution and contracted section. All intermediate exclusions and the conclusion are retained.')
for unit,event in [('night:P4R.17','II-C3-ROOT-NONORDINARY-TRIPLE-UNIT'),('night:P4.50','II-C3-ROOT-TACNODAL-COMPLETION-UNIT')]:
 add_event(unit,event,'used and rechecked in this run',
  'Root read the complete original and receiving unit. Every branch model, numerical bound, full-fibre scope and application is compared. R17 includes the corrected x factor and explicit leading minor; P450 uses the same full fibre and rational-resolution cohomology map. Every local instance is logged; final placement, bibliography and PDF typography remain open. This is a proof comparison after exposure, not an independent check or final-page reading.',
  'S6_SERIES_PUBLISH_II.tex: '+unit,source=__file__)
 for number in range(1,26):
  kind=f'D{number:02}'
  if kind in ['D10','D16']:continue
  status='open' if kind in ['D14','D18','D23'] else 'done'
  set_unit_status(unit,kind,status,'Complete original/receiving unit read; final placement, bibliography and rendered typography remain open.' if status=='open' else 'Complete current unit read; all local instances recorded.','CHECK_EVENTS.tsv: '+event)
print('R17 and P450 complete receiving units admitted.')
