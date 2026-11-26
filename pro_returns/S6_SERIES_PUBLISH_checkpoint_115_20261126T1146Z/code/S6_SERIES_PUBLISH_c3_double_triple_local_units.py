"""Complete the ordinary-double and pole-coefficient local units."""
from S6_SERIES_PUBLISH_c3_edit import *

s=SOURCE.read_text();i=s.index(r'\label{night:P4.38}');start=s.rfind(r'\begin{proposition}',0,i);end=s.index(r'\end{proof}',i)+len(r'\end{proof}')
old=s[start:end];new=old
first_start=new.index(r'\item Throughout,');first_end=new.index(r'\item First suppose',first_start)
newfirst=r'''\item Write $F=Uf_0^m$ for the original local fibre map, where
$m$ is the multiplicity of the irreducible support and $U$ is a unit.
Choose $f=U^{1/m}f_0$, so that $F=f^m$ exactly. The reduced
critical-curve germ is unchanged: every critical component through
the origin has constant value zero, and on the zero divisor
$df=U^{1/m}df_0$. We use this root in both calculations below.

Choose a small closed ball transverse to the smooth zero-divisor
strata and to the smooth critical-curve links. At each such link,
the nondegenerate transverse quadratic form gives parameter Morse
coordinates, with the curve coordinate retained, in which the root
function is $XY$. These coordinates and their local inverses vary
holomorphically under the sufficiently small deformations below.
A real direction in the curve coordinate is tangent to every level
and transverse to the fixed boundary. On its remaining compact
part, submersivity persists. These are the boundary hypotheses of
\cref{lem:II:boundary-deformation-transport}. Apply that lemma to
the first root family with the exact equality $F=f^m$. Subsequent
coordinate and unit changes use its nested-ball comparison with
exponent one at the intermediate root levels. Their composition
maps every compact spherical representative and its intersection
push-off into the original full fibre $F=b^m$.

'''
new=new[:first_start]+newfirst+new[first_end:]
a=r'''curve. A reduced singular plane curve has an isolated critical
point. A generic small morsification $H_s$ has a Morse critical
point, and a small additive constant makes all these critical
values nonzero.'''
b=r'''curve. Apply the finite-gradient construction in the proof of
\cref{cdp:st:A.5.17} to this reduced singular plane function $H$.
It gives an arbitrarily small linear and constant perturbation
$H_s$ with a Morse critical point of nonzero critical value.'''
assert a in new;new=new.replace(a,b,1)
a=r'''\Cref{night:P4.16} gives its compact spherical class of square $-4$.
Nested boundary transport once more places this class in
the original nearby four-torus, a contradiction.'''
b=r'''The coordinate map $(X_0,Y_0,Z_0)=(Y,x,-Z)$ identifies this
function with $X_0^2-Y_0^2Z_0$. Apply \cref{cdp:st:A.5.15}
with $(a,b,c)=(2,2,1)$; its compact spherical class has square
$-2(2/\gcd(2,1))(1/\gcd(2,1))=-4$. The nested comparison in
the first item maps that same class into the original full fibre
$F=b^m$. Its sphere map lifts to the contractible universal cover
of the complex two-torus, so its homology class and square are
zero, contradicting the preserved square $-4$.'''
assert a in new;new=new.replace(a,b,1)
new=new.replace(r'\StatementRecord{night:P4.38}{proved}{02XB}{}',r'\StatementRecord{night:P4.38}{proved}{02XB}{\cref{lem:II:boundary-deformation-transport,cdp:st:A.5.15,cdp:st:A.5.17}}')
apply_edit(old,new,'II-C3-ORDINARY-DOUBLE-ROOT-TRANSPORT',['D12','D25'],
 'night:P4.38','Complete ordinary-double local-exclusion proof',
 'Specify the original irreducible-support common power F=(U^(1/m)f_0)^m before all deformations. Supply the exact parameter-Morse boundary charts and nested transport maps, and apply the existing plane-gradient and binomial spherical-class owners through the displayed functions and coordinates. Every original symbolic-square, Hessian and implicit-root calculation is retained.')

s=SOURCE.read_text();i=s.index(r'\label{night:P4.39}');start=s.rfind(r'\begin{proposition}',0,i);end=s.index(r'\end{proof}',i)+len(r'\end{proof}')
old=s[start:end];new=old
labels={'4.39a':'eq:II:triple-pole-transform','4.39b':'eq:II:triple-pole-order',
        '4.39c':'eq:II:triple-depressed-cubic','4.39d':'eq:II:triple-tangent-quadratic'}
def convert(match):
    body=match.group(1)
    for tag,label in labels.items():
        token=r'\tag{'+tag+'}'
        if token in body:
            body=body.replace(token,r'\label{'+label+'}')
            return '\\begin{equation}'+body+'\\end{equation}'
    return match.group(0)
new=re.sub(r'\\\[(.*?)\\\]',convert,new,flags=re.S)
for tag,label in labels.items():new=new.replace('('+tag+')',r'\eqref{'+label+'}')
a=r'''\item Put $d=\operatorname{mult}_0f$, and denote the ambient
exceptional divisor by $E$. Adjunction gives'''
b=r'''\item Put $d=\operatorname{mult}_0f$, and denote the ambient
exceptional divisor by $E$. Along the generic points of $C$,
the function and its derivatives of orders one and two vanish.
They therefore vanish on the reduced curve $C$, so $d\ge3$.
Adjunction gives'''
assert a in new;new=new.replace(a,b,1)
apply_edit(old,new,'II-C3-ORDINARY-TRIPLE-POLE-EQUATIONS',['D04','D11','D25'],
 'night:P4.39','Complete pole-coefficient proof',
 'Give the four displayed equalities section equation numbers and resolve every reference by its new exact label. State the existing d>=3 premise by vanishing of the first two derivative orders on the same reduced critical curve. Preserve the full blowup/residue identity, coefficient alternatives, homogeneous double-cover maps, discriminant at infinity and isolated-singularity coordinate argument.')

for unit,event,detail in [
 ('night:P4.38','II-C3-ROOT-ORDINARY-DOUBLE-UNIT',
  'The original full map is exactly F=f^m because the support is irreducible. Root checked the parameter-Morse fixed-boundary charts, complete-intersection square, symbolic intersection (z,h)^2 intersect (x,y)^2 for k=3,4, all coefficient perturbations, determinant F(s,z), simple root z(s), exact binomial coordinates and full-fibre sphere inclusion.'),
 ('night:P4.39','II-C3-ROOT-ORDINARY-TRIPLE-POLE-UNIT',
  'Root checked the ambient blowup and minimal-resolution domination, effective residue pole divisor, positive-genus coefficient cases, quartic tangent-cone genera, the depressed cubic with u,h orders, the exceptional double cover including infinity through Q_h(X,Xw,X^2q), and every remaining isolated-singularity case with the exact coordinate W=G. All eight proof items and the printed statement remain complete.')]:
    add_event(unit,event,'used and rechecked in this run',
      'Root read the complete original and receiving mathematical unit and compared every proof item. '+detail+
      ' All local defect classes were read; every identified instance is in the defect table. Final placement, bibliography-wide checks and final rendered pages remain open. No independent or final-page credit.',
      'S6_SERIES_PUBLISH_II.tex: complete local exclusion unit',source=__file__)
    for number in range(1,26):
        kind=f'D{number:02}'
        if kind in ['D10','D16']:continue
        status='open' if kind in ['D14','D18','D23'] else 'done'
        set_unit_status(unit,kind,status,
          'Complete current unit read; whole-paper placement, bibliography or final rendered typography remains.' if status=='open' else
          'Complete current unit read for this defect type, with every identified instance recorded and no local residue.',
          'CHECK_EVENTS.tsv: '+event)
print('Ordinary-double and pole-coefficient units fully compared; global gates remain open.')
