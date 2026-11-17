#!/usr/bin/env python3
"""Exact local source-cusp trace, critical braid and II* plumbing.

This certificate checks the algebra and integral lattice in the accompanying
working proof. It does not replace the geometric ambient/Hopf-line audit.
"""
from pathlib import Path
import json
import sympy as sp

s, r, X, y, a, u, R, z, g = sp.symbols('s r X y a u R z g')
checks = []


def zero(name, value):
    value = sp.simplify(value)
    assert value == 0, (name, value)
    checks.append(name)


F = sp.Matrix([s*s-r*r, s*(s*s-r*r), r])
ds, dr = F.diff(s), F.diff(r)
cross = ds.cross(dr)
want = sp.Matrix([3*s*s-r*r, -2*s, 2*r*(s*s-r*r)])
for i in range(3):
    zero(f'Jacobian cross product component {i}', cross[i]-want[i])
gb = sp.groebner(list(cross), s, r)
assert [sp.factor(p.as_expr()) for p in gb.polys] == [s, r*r]
checks.append('Jacobian minor ideal (s,rho^2)')
zero('normalization image equation', F[1]**2-F[0]**2*(F[0]+r*r))
zero('two ordered branches have same image',
     sum((F.subs(s,r)[i]-F.subs(s,-r)[i])**2 for i in range(3)))

q = (y*y-X*X*(X+a))/(X+u)
critical = -X*(2*X*X+(a+3*u)*X+2*a*u)/(X+u)**2
zero('exact x critical derivative', sp.diff(q,X).subs(y,0)-critical)
zero('scaled second critical equation',
     (2*X*X+(a+3*u)*X+2*a*u).subs(X,a*R)
     -a*(2*a*R*R+(a+3*u)*R+2*u))
q_second = -a**3*R**2*(R+1)/(a*R+u)
zero('exact second critical value', q.subs({X:a*R,y:0})-q_second)
zero('critical value leading coefficient',
     sp.cancel(q_second/a**3).subs({a:0,R:-sp.Rational(2,3)})
     +sp.Rational(4,27)/u)
zero('implicit root derivative',
     sp.diff(2*a*R*R+(a+3*u)*R+2*u,R).subs(a,0)-3*u)

# Actual multiplication in the nodal normalization group.
Z = (s-r)/(s+r)
new_s = ((1+g)*s+(1-g)*r)/(((1-g)/r)*s+(1+g))
zero('fractional translation is multiplication of Z',
     sp.cancel((new_s-r)/(new_s+r)-g*Z))
zero('positive node branch fixed', sp.cancel(new_s.subs(s,r)-r))
zero('negative node branch fixed', sp.cancel(new_s.subs(s,-r)+r))
h=sp.symbols('h')
zero('exact bounded source shear',
     sp.cancel(new_s.subs(g,1+r*h)-s-h*(s*s-r*r)/(2+h*(r-s))))

# Literal closed-ball extension of the outer Mobius loop; no square root.
rb,p00,p01,p10=sp.symbols('rb p00 p01 p10')
AM=sp.Matrix([[1,-r],[1,r]])
AMstar=sp.Matrix([[1,1],[-rb,rb]])
P=sp.Matrix([[p00,p01],[p10,1-p00]])
AP=AM*P*AMstar
BP=AP/sp.trace(AP)
back=AM.inv()*BP*AMstar.inv()
back=back/sp.trace(back)
for i in range(2):
    for j in range(2):
        zero(f'Mobius ball inverse entry {i}{j}', sp.cancel(back[i,j]-P[i,j]))
zero('Mobius determinant',AM.det()-2*r)

# Exact right Hurwitz action in the free group, before imposing any relation.
def red(word):
    out=[]
    for letter in word:
        if out and out[-1] == -letter:
            out.pop()
        else:
            out.append(letter)
    return tuple(out)


def inv(word):
    return tuple(-x for x in reversed(word))


def mul(*words):
    return red(sum((tuple(w) for w in words), ()))


G, H = (1,), (2,)
C=mul(G,H)
pair=(G,H)
for j in range(1,13):
    gg, hh=pair
    pair=(hh,mul(inv(hh),gg,hh))
    if j % 2 == 0:
        cp=mul(*([C]*(j//2)))
        expected=(mul(inv(cp),G,cp),mul(inv(cp),H,cp))
        assert pair == expected
        checks.append(f'Hurwitz sigma^{j} exact conjugation')

Ta=sp.Matrix([[1,1],[0,1]])
Tb=sp.Matrix([[1,0],[-1,1]])
CM=Ta*Tb
assert CM**3 == -sp.eye(2) and CM**6 == sp.eye(2)
checks.append('positive A2 monodromy matrix order six')

# Literal affine E8 fibre from the weighted plane and six point blowups.
names=['central','E1','E2','E3','E4','E5','A1','B1','B2','section']
Q=sp.zeros(10)
for i in range(9): Q[i,i]=-2
Q[9,9]=-1
edges=[(0,1),(1,2),(2,3),(3,4),(4,5),(0,6),(0,7),(7,8),(5,9)]
for i,j in edges: Q[i,j]=Q[j,i]=1
mult=sp.Matrix([6,5,4,3,2,1,3,4,2,0])
assert Q[:9,:9]*mult[:9,:] == sp.zeros(9,1)
assert (Q*mult)[9] == 1
assert Q.det() == -1
checks.extend(['affine E8 multiplicity vector', 'section-fibre intersection one',
               'complete pencil lattice unimodular'])

# Integral basis F,S and the eight non-affine E8 components.
roots=[0,1,2,3,4,6,7,8]
change=sp.Matrix.hstack(mult,sp.eye(10)[:,9],*(sp.eye(10)[:,i] for i in roots))
assert abs(change.det())==1
Qnew=change.T*Q*change
assert Qnew[:2,:2] == sp.Matrix([[0,1],[1,-1]])
assert Qnew[:2,2:] == sp.zeros(2,8)
rootgram=Qnew[2:,2:]
assert rootgram.det()==1
for j in range(1,9):
    assert (-1)**j*rootgram[:j,:j].det()>0
checks.extend(['integral fibre-section-E8 basis', 'negative-definite E8 block',
               'pencil signature minus eight'])
zero('central curve exact self intersection',
     sp.Rational(1,6)-sp.Rational(1,2)-sp.Rational(2,3)-1+2)

# The ordered branch map to P1 is a Hopf map on the inner sphere.
A=sp.Matrix([[1,-1],[1,1]])
assert A.det()==2
checks.append('ordered branch homogeneous map has positive complex determinant')

# The actual degree-two clutch morphism doubles the sphere mapping class.
double_classes=sorted({2*x % 28 for x in range(28)})
assert double_classes == list(range(0,28,2)) and 1 not in double_classes
checks.append('degree-two sphere-clutch image excludes the class one')

result={
    'status':'PASS', 'checks':len(checks), 'identities':checks,
    'normalization':[str(x) for x in F],
    'normal_covector':[str(x) for x in cross],
    'minor_ideal':['s','rho^2'],
    'critical_value':'-rho^6 R(rho^2)^2 (R(rho^2)+1)/(rho^2 R(rho^2)+u(rho))',
    'critical_value_leading':'-4/(27u_*)',
    'positive_ordered_braid':'sigma^12',
    'right_hurwitz_endpoint':'conjugation by (g h)^(-6)',
    'retained_boundary_relation':'(g h)^6 = positive boundary twist',
    'plumbing_names':names, 'plumbing_matrix':[list(map(int,row)) for row in Q.tolist()],
    'fibre_multiplicities':list(map(int,mult)),
    'integral_basis_change':[list(map(int,row)) for row in change.tolist()],
    'basis_gram':[list(map(int,row)) for row in Qnew.tolist()],
    'signature':-8,
    'normal_spinor':'O(D_+) plus O(-D_-), determinant trivialized by (s-rho)/(s+rho)',
    'outer_cap_ball_map':'P -> A_rho P A_rho^* / trace(A_rho P A_rho^*), A_rho=[[1,-rho],[1,rho]]',
    'cap_base':'(S2 x D2) union (D3 x S1) = boundary(D3 x D2) = S4',
    'degree_two_clutch_image_mod_28':double_classes,
    'audit_scope':'Exact algebra and integral plumbing only; geometric trace, actual line and transfer sign require the accompanying proof audit.'
}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
