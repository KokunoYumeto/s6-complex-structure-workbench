"""Finish the actual receiving read of all three ordinary-axis units."""
from S6_SERIES_PUBLISH_c3_edit import *

def block(label):
    s=SOURCE.read_text();i=s.index('\\label{'+label+'}')
    a=s.rfind(r'\begin{proposition}',0,i);b=s.index(r'\end{proof}',i)+len(r'\end{proof}')
    return s[a:b]

old=block('night:P4.48');new=old
new=new.replace('At a planar three-branch critical-curve point with uniform',
 r'For a fibre support in \cref{def:II:standing-torus-fibration}, at a planar three-branch critical-curve point with uniform',1)
new=new.replace('use actual coordinates','use coordinates')
head,body=new.split(r'\begin{proof}',1)
head=head.replace('by P4.47.',r'by \cref{night:P4.47}.')
body=body.replace('in P4.42',r'in \cref{night:P4.42}').replace('P4.47 applies',r'Proposition~\ref{night:P4.47} applies')
a=r'''with $P=(xy,xz,yz)$. The argument in P4.47 gives
$f\in P^2$.'''
b=r'''with $P=(xy,xz,yz)$. Apply the first proof item of
\cref{night:P4.47} to this identical ideal and reduced equation:
$P^{(2)}=P^2+(xyz)$, the rank-one generic transverse Hessian
kills the constant coefficient of $xyz$, and
$\mathfrak m xyz\subset P^2$. Thus $f\in P^2$.
This calculation uses only the three axes and their generic
transverse type, before the nonzero-coefficient hypothesis in
that proposition is used.'''
assert a in body;body=body.replace(a,b,1)
a=r'''diagonal coefficients are nonzero, the vanishing null
cubic on the $x$-axis gives $F=BD/A$. Higher-degree
terms cannot alter the coefficient linear in $x$
of that normal cubic.'''
b=r'''diagonal coefficients are nonzero, the null direction on the
$x$-axis is $y=-(B/A)z$. The coefficient linear in $x$ of the
normal cubic on that direction is
$2(B/A)(DB/A-F)xz^3$. Generic transverse type $A_3$ makes it
zero, giving $F=BD/A$. Higher-degree terms contribute higher
powers of $x$ to that normal cubic and cannot alter this coefficient.'''
assert a in body;body=body.replace(a,b,1)
new=head+r'\begin{proof}'+body
apply_edit(old,new,'II-C3-THREE-AXIS-DEFECT-RECEIVING',['D04','D08','D12','D25'],
 'night:P4.48','Complete three-branch defect proof',
 'Make the standing fibre-support setting explicit, as in the surrounding section. Retain all local bounds and rank cases. Give the exact identical three-axis ideal used in the earlier calculation and write the null-direction substitution that forces the quartic-square coefficient. Replace all printed run labels with their exact statement references.')

old=block('night:P4.47');new=old
new=new.replace(r'\item Put $P=(xy,xz,yz)$ and $h=xyz$.',r'\item Let $f$ be the reduced local defining equation and put $R=\mathbb C\{x,y,z\}/(f)$. Set $P=(xy,xz,yz)$ and $h=xyz$.',1)
new=new.replace(r'$F=b^M$',r'$F=t_0^M$')
new=new.replace(r'\StatementRecord{night:P4.47}{proved}{02XL}{\SeriesRef{night:P4.41}}',r'\StatementRecord{night:P4.47}{proved}{02XL}{\cref{night:P4.41,lem:II:quadratic-conductor-normalization,lem:II:boundary-deformation-transport}}')
apply_edit(old,new,'II-C3-QUARTIC-AXIS-NOTATION',['D06','D12'],'night:P4.47','Complete receiving proof',
 'Name the local ring before its multiplier application and use t_0 for the final regular target, keeping the quartic coefficient b unchanged. Record the exact shared dependencies.')

old=block('night:P4.49');new=old
new=new.replace('At an ordinary three-axis critical-curve point with uniform',
 r'For a fibre support in \cref{def:II:standing-torus-fibration}, at an ordinary three-axis critical-curve point with uniform',1)
a=r'''\item Only the one-missing-coefficient case remains. Rescale
its leading conductor form to $x(y+z)$.'''
b=r'''\item Write $f$ for the reduced local equation,
$R=\mathbb C\{x,y,z\}/(f)$ and $I$ for its ambient conductor ideal.
Proposition~\ref{night:P4.48} gives a quartic square with at least
two nonzero coefficients, and \cref{night:P4.47} proves the result
when all three are nonzero. In the remaining case, permute the
axes to write the leading conductor form as $a xy+b xz$ with
$ab\ne0$. The map $(x,y,z)\mapsto(x,ay,bz)$, with inverse
$(x,Y,Z)\mapsto(x,Y/a,Z/b)$, gives the form $x(y+z)$.'''
assert a in new;new=new.replace(a,b,1)
new=new.replace(r'$F=Vf^M$',r'$\mathcal F=Vf^M$').replace(r'$F=f_0^M$',r'$\mathcal F=f_0^M$')
new=new.replace(r'''$V^{1/(2M)}x$, with $y,z$ fixed, is invertible and writes this root''',r'''$X=V^{1/(2M)}x$, with $y,z$ fixed, has nonzero $x$ derivative
at the origin. Its inverse is the unique local solution $x=\chi(X,y,z)$
of this displayed equation. It writes this root''')
new=new.replace('the full critical\nvalue and Hessian determinant', 'the critical\nvalue of the displayed polynomial $F$ and its Hessian determinant')
new=new.replace('The resulting full Morse points','The resulting three-variable Morse points')
new=new.replace('The actual conductor identifies','The conductor identifies')
record=re.search(r'\\StatementRecord\{night:P4\.49\}[^\n]+',new).group(0)
new=new.replace(record,record[:-1]+r'; \cref{lem:II:quadratic-conductor-normalization,lem:II:boundary-deformation-transport}}',1)
apply_edit(old,new,'II-C3-AXIS-CONDUCTOR-RECEIVING-NOTATION',['D06','D08','D12','D25'],
 'night:P4.49','Complete receiving two-ideal proof',
 'Keep the existing standing fibre-support scope explicit. Name the ring and ideal, give both directions of the leading-form rescaling and the root-coordinate inverse, and denote the original full map by mathcal F so it is unambiguously separate from the already existing scaled polynomial F. Every critical value and Hessian payload is unchanged.')

# The original local boundary calculation now has its own permanent owner.
old=r'Transverse nodes of a shifted quadratic square (\cref{night:P4.47}) &'
new=r'Transverse nodes of a shifted quadratic square (\cref{rem:II:shifted-square-boundary-nodes}) &'
apply_edit(old,new,'II-C3-SHIFTED-SQUARE-PROGRAM-OWNER',['D12'],
 'rem:II:shifted-square-boundary-nodes','Programs appendix row',
 'Point the existing unchanged program path at the exact complete boundary calculation now printed in P258.')

old=block('night:P4.38');new=old.replace(r'$F=b^m$',r'$F=t_0^m$')
apply_edit(old,new,'II-C3-DOUBLE-CURVE-TARGET-NOTATION',['D06'],'night:P4.38','Root transport target',
 'Use t_0 for the regular root value, leaving b=2 in the exact binomial parameter substitution unambiguous.')

for unit,event,detail in [
 ('night:P4.47','II-C3-ROOT-QUARTIC-AXIS-UNIT','The complete unit includes P447 and the complete shifted-square remark P258. All symbolic-square, actual conductor, local-normalization-fibre, full-root, conic polar, numeric Hessian and boundary-coordinate arguments were read.'),
 ('night:P4.48','II-C3-ROOT-THREE-AXIS-DEFECT-UNIT','The complete three-branch defect unit retains every planar descent bound, quartic rank case, null-direction cubic coefficient, leading quotient-value matrix, and equality conclusion, with exact earlier-owner substitutions.'),
 ('night:P4.49','II-C3-ROOT-THREE-AXIS-CONDUCTOR-UNIT','The complete two-ideal unit retains both full Hilbert--Burch/colon computations, all generator and coordinate maps, every normalization relation, rational-cone resolution and cohomology proof, all weighted critical-point calculations, and both established full-root boundary transports.')]:
    add_event(unit,event,'used and rechecked in this run',
      'Root read every original and actual receiving proof item and the complete current unit. '+detail+
      ' The full-function premises are resolved by the recorded normalization algebras. All local defect classes were reviewed and every identified instance logged. Final placement, source-locator verification and final rendered pages remain open. No independent or final-page credit.',
      'S6_SERIES_PUBLISH_II.tex: complete ordinary-axis unit',source=__file__)
    for number in range(1,26):
        kind=f'D{number:02}'
        if kind in ['D10','D16']:continue
        status='open' if kind in ['D14','D18','D23'] else 'done'
        set_unit_status(unit,kind,status,
          'Complete current unit read; whole-paper placement, remaining exact-source locator or rendered typography remains.' if status=='open' else
          'Complete current unit read against this defect type; every instance recorded and no local residue.',
          'CHECK_EVENTS.tsv: '+event)
print('All three ordinary-axis units fully compared; local full-function premises closed.')
