"""Repair full-function transport in the two actual three-axis conductors."""
from S6_SERIES_PUBLISH_c3_edit import *

def owner(label):
    s=SOURCE.read_text();i=s.index('\\label{'+label+'}')
    a=s.rfind(r'\begin{proposition}',0,i);b=s.index(r'\end{proof}',i)+len(r'\end{proof}')
    return s[a:b]

old=owner('night:P4.47');new=old
new=new.replace('Consider an actual torus degeneration','Consider a torus degeneration')
new=new.replace('the actual conductor image ideal','the conductor image ideal').replace('lifts to an actual element','lifts to an element')
new=new.replace(r'''The actual conductor ring condition, with the hypotheses
verified in \cref{night:P4.41}, gives $f\in I^2$ by the two-by-two
adjugate calculation of de Jong--van Straten,
Theorem~1.12.''',r'''The conductor ring condition \eqref{eq:II:manual:4.41b}
applies to this regular ambient ring, reduced hypersurface and
Cohen--Macaulay conductor quotient. Its two-by-two adjugate calculation
\cite[Theorem~1.12, p.~532]{DeJongVanStraten1990Normalization}
gives $f\in I^2$.''')
# Preserve the separate boundary calculation in its own numbered remark.
a=new.index('At a generic boundary point');b=new.index('Add an arbitrarily small generic',a)
boundary=new[a:b]
new=new[:a]+new[b:]
anchor=r'''\item We exclude $U(0)=0$ by a deformation that keeps the
three axes fixed.

'''
replacement=r'''\item Suppose $U(0)=0$. Apply
\cref{lem:II:quadratic-conductor-normalization} with the same
$R$, $G$, $H=h=xyz$, $U$ and conductor $I=(G,h)$.
The sequence is regular: on each coordinate plane, $G$ restricts
to the product of its two coordinates times a unit. The normalization
is therefore $R+R(G/h)$, with $(G/h)^2=-U$, and its fibre algebra
is local. The original reduced germ $f$ is irreducible.

Write the original full fibre function as $F=Vf^M$ and take
\[
 f_0=V^{1/M}f=G_0^2+h^2U_0,\qquad
 G_0=V^{1/(2M)}G,\qquad U_0=V^{1/M}U.
\]
Then $F=f_0^M$ exactly. The conductor ideal remains $(G_0,h)$,
the quadratic part of $G_0$ is nondegenerate, and $U_0(0)=0$.
We use $f,G,U$ for these root data in the following deformation,
which keeps the three axes fixed.

'''
assert anchor in new;new=new.replace(anchor,replacement,1)
new=new.replace(r'''A diagonal linear change
puts the quadratic part of $G$ in the form
$G_2=xy+xz+yz$, changing $h$ only by a nonzero constant.''',r'''Write the quadratic part as $a xy+b xz+c yz$.
The diagonal substitution $(x,y,z)=(\alpha X,\beta Y,\gamma Z)$,
where $\alpha^2=c/(ab)$, $\beta=1/(a\alpha)$ and
$\gamma=1/(b\alpha)$, is invertible and gives $G_2=XY+XZ+YZ$.
It multiplies $h$ by the nonzero constant $\alpha\beta\gamma$.
Rename these coordinates $x,y,z$.''')
a=r'''Since the deformation retains boundary $A_3$, the
nested boundary transport embeds a Morse vanishing
sphere of square $-2$ into a nearby global torus fibre.
This contradicts asphericity. Therefore $U(0)=0$
cannot occur, proving the assertion.'''
b=r'''On each fixed critical-axis boundary link the nonzero transverse
quadratic coefficient and residual quartic coefficient give parameter
Morse coordinates and a fourth root of a unit, keeping the curve
coordinate. Their implicit inverses identify every sufficiently small
root deformation with $X^2+Y^4$ there. The real curve direction is
transverse to the fixed boundary; the remaining smooth support strata
have submersion charts. Thus \cref{lem:II:boundary-deformation-transport}
applies to this root family with the established equality $F=f_0^M$,
including the smaller balls used for the Morse calculation. It maps
the compact Morse sphere of square $-2$ and its intersection push-off
into the original full fibre $F=b^M$. A sphere map into the complex
two-torus lifts to its contractible universal cover and has zero
homology class, contradicting that preserved square. Hence $U(0)=0$
is excluded, and the rational normalization conclusion follows.'''
assert a in new;new=new.replace(a,b,1)
new=new.replace(r'\tag{4.47a}',r'\label{eq:II:axis-quartic-square}')
new=re.sub(r'\\\[(.*?\\label\{eq:II:axis-quartic-square\}.*?)\\\]',lambda m:'\\begin{equation}'+m.group(1)+'\\end{equation}',new,flags=re.S)
new=new.replace('(4.47a)',r'\eqref{eq:II:axis-quartic-square}')
# The bounded match must not span a preceding display.
assert new.count(r'\begin{equation}')==new.count(r'\end{equation}')
boundary=boundary.replace('$\\epsilon$', '$\\eta$').replace(r'\epsilon',r'\eta')
remark=r'''

\begin{remark}[Boundary nodes of a shifted square]\hypertarget{tag-P258}{}\label{rem:II:shifted-square-boundary-nodes}
\StatementRecord{rem:II:shifted-square-boundary-nodes}{proved}{P258}{}
Let $h=xyz$ and let $G$ vanish on the coordinate axes. Suppose
$G_y,G_z,U$ are nonzero at a point $(t,0,0)$ with $t\ne0$.
The family $f_\eta=(G-\eta)^2+h^2U$, on the transverse slice
$x=t$, has ordinary nodes at the two points $G=\eta$, $h=0$
for every sufficiently small nonzero $\eta$.

'''+boundary+r'''\end{remark}
'''
apply_edit(old,new+remark,'II-C3-QUARTIC-AXIS-FULL-ROOT',['D08','D11','D12','D18','D25'],
 'night:P4.47; rem:II:shifted-square-boundary-nodes','Complete quartic-square normalization proof and boundary calculation',
 'Prove the original full-function comparison through the actual conductor normalization and its local fibre before deforming. Preserve every conic parametrization, critical value, Hessian and lifted Morse point. Give the separate G-shift/two-node calculation its own numbered remark, with the complete original coordinate proof; it is not the U-deformation used for the normalization conclusion. Resolve the ring-condition locator and displayed equation label.')

old=owner('night:P4.49');new=old
new=new.replace('the actual conductor','the conductor').replace('same actual normalization','same normalization')
new=new.replace(r'''The adjugate ring condition
of de Jong--van Straten, Theorem~1.12, applies to the
actual conductor as in \cref{night:P4.41}.''',r'''The adjugate form of \eqref{eq:II:manual:4.41b}
\cite[Theorem~1.12, p.~532]{DeJongVanStraten1990Normalization}
applies to this same conductor: its quotient is Cohen--Macaulay
and the reduced hypersurface lies in the regular ambient ring.''')
anchor=r'''\item Suppose $C(0)=0$. Perturb $D$ by a small constant'''
insert=r'''\item Suppose $C(0)=0$. Append
$(a,b,d)=(xk,hC,h^2D)$ to the Hilbert--Burch matrix of
$I=(xk,xh,h^2)$. Its determinant is the displayed $f$.
The same finite-duality and adjugate identification gives the
normalization generated by $1,v,w$, with
\[
 v=xk/h,\qquad w=xk^2/h^2+C.
\]
Indeed the adjugate fractions are $n_1=-a/h=-v$ and
$n_2=-(ak+bh)/h^2=-w$. The element $h=yz$ is a nonzerodivisor
modulo $f$: its restrictions to $y=0$ and $z=0$ are respectively
$x^2z^2$ and $x^2y^2$. Division in the total quotient ring gives
\[
 v^2=-xC-Dh^2,\qquad vw=-Dkh,\qquad w^2=Cw-Dk^2.
\]
The fibre is a nonzero quotient of
$\mathbb C[v,w]/(v,w)^2$. Apply the local-fibre assertion of
\cref{lem:II:quadratic-conductor-normalization} to this normalization.
It makes the original reduced equation irreducible. Write its full
map as $F=Vf^M$ and choose $f_0=V^{1/M}f$. Replacing $x$ by
$V^{1/(2M)}x$, with $y,z$ fixed, is invertible and writes this root
in the same form $x^2k^2+xh^2C+h^4D$. Its new coefficients are the
transported $V^{1/(2M)}C$ and $V^{1/M}D$, so $C(0)=0$ remains true.
Thus $F=f_0^M$ before the following root deformation.

Perturb $D$ by a small constant'''
assert anchor in new;new=new.replace(anchor,insert,1)
new=new.replace(r'''The boundary comparison embeds their square-$-2$
vanishing spheres in a nearby torus fibre, a
contradiction. Thus $C(0)=0$ is excluded.''',r'''The root boundary comparison is explicit: on every fixed axis
link the transverse quadratic and quartic coefficients remain units,
so parameter Morse coordinates and a fourth root give
$X^2+Y^4$, with their implicit inverses retaining the curve coordinate.
The curve direction is transverse to the boundary. Apply
\cref{lem:II:boundary-deformation-transport} with $F=f_0^M$
and its nested representative maps. The square-$-2$ Morse sphere
therefore lies in the original full torus fibre, a contradiction.
Thus $C(0)=0$ is excluded.''')
# The exact normalization algebra is valid before either kappa case.
new=new.replace(r'''\item We first treat $\kappa(0)\ne0$.
Use the appended coefficients''',r'''\item For both values of $\kappa(0)$, use the appended coefficients''')
a=r'''At the origin they give $v=w=0$, so there is one
normalization point. The last equation eliminates $k$
analytically, with $k$ in the maximal-ideal square.'''
b=r'''Since $A(0)\ne0$, reduction modulo the original maximal ideal
gives $v^2=vw=w^2=0$. The fibre algebra is local, so the first
assertion of \cref{lem:II:quadratic-conductor-normalization}, applied
to this same finite normalization, makes $f$ irreducible.

First take $\kappa(0)\ne0$. The last equation eliminates $k$
analytically, with $k$ in the maximal-ideal square.'''
assert a in new;new=new.replace(a,b,1)
a=r'''\item Finally suppose $\kappa(0)=0$. Perturb $D$ and the
linear part of $\kappa$ generically, and replace'''
b=r'''\item Finally suppose $\kappa(0)=0$. By the same local normalization
fibre, the original full map is $F=Vf^M$. Its root $f_0=V^{1/M}f$
has the same conductor ideal and the same displayed ring-condition
form: multiply each of $A,B,C,D,\kappa$ by $V^{1/M}$.
The first coefficient remains a unit and $\kappa(0)=0$ is preserved.
Use this root for the following deformation. Perturb $D$ and the
linear part of $\kappa$ generically, and replace'''
assert a in new;new=new.replace(a,b,1)
a=r'''Boundary transport gives the forbidden square-$-2$
vanishing sphere in a nearby torus fibre. Thus
$\kappa(0)=0$ is excluded, completing both ideal forms.'''
b=r'''The fixed-axis boundary charts are again the parameter Morse
and quartic-root maps $X^2+Y^4$, with the same transverse curve
direction and inverses. Apply \cref{lem:II:boundary-deformation-transport}
to this root family and the exact original equality $F=f_0^M$.
Its nested maps preserve the square-$-2$ sphere and its push-off
in the original full torus fibre. This contradicts the torus's
asphericity and excludes $\kappa(0)=0$, completing both ideal forms.'''
assert a in new;new=new.replace(a,b,1)
labels={'4.49a':'eq:II:first-axis-conductor-equation','4.49b':'eq:II:second-axis-conductor-equation'}
def convert(match):
    body=match.group(1)
    for tag,label in labels.items():
        token=r'\tag{'+tag+'}'
        if token in body:return '\\begin{equation}'+body.replace(token,r'\label{'+label+'}')+'\\end{equation}'
    return match.group(0)
new=re.sub(r'\\\[(.*?)\\\]',convert,new,flags=re.S)
for tag,label in labels.items():new=new.replace('('+tag+')',r'\eqref{'+label+'}')
apply_edit(old,new,'II-C3-AXIS-CONDUCTOR-FULL-ROOTS',['D08','D11','D12','D18','D25'],
 'night:P4.49','Complete two-conductor-form normalization proof',
 'Identify the original analytic factor scope from each actual three-generator conductor before any root deformation. The complete adjugate generators and multiplication relations show local normalization fibres, hence irreducibility. Give the exact root and coordinate maps preserving each ring-condition form, and explicit nested boundary transport with the original full power. Preserve every original ideal/colon identity, quotient map, rational tangent-cone resolution, formal-functions argument, weighted scaling, resultant, critical value and Hessian.')
add_event('night:P4.47; night:P4.49','II-C3-ROOT-ORDINARY-AXES-FULL-FIBRE-REPAIR','used and rechecked in this run',
 'Root read both complete old/receiving proofs and the full shared P257 algebra. Foundations also read both complete current proofs and checked the same actual-conductor generators; that comparison was exposed. For P447 use I=(G,h), h=xyz, with h a nonzerodivisor and B=R+R(G/h). U(0)=0 gives a local normalization fibre. For the first P449 ideal, the exact adjugate generators v=xk/h and w=xk^2/h^2+C satisfy all three printed multiplication equations, and C(0)=0 gives a local square-zero fibre. For the second ideal, A(0) nonzero and its four original relations give v^2=vw=w^2=0 in the fibre for every kappa(0); the algebra precedes both cases. These prove irreducibility before the three full maps F=f_0^M are formed. The root multiplication and coordinate changes preserve each stated ideal/equation type. Every original weighted critical-point/Hessian calculation remains, and the full-root boundary hypotheses and nested fibre inclusions are explicit. The two premises opened by II-C3-ORDINARY-AXES-FULL-FIBRE-PREMISE are resolved without changing either proposition scope. The separate shifted-square boundary computation remains complete in its numbered remark. No independent or final-page credit.',
 'S6_SERIES_PUBLISH_II.tex: full ordinary-axis conductor proofs',source=__file__)
print('P447/P449 full-root comparisons repaired; full receiving syntax/unit review follows.')
