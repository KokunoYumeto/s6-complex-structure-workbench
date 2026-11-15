"""Exact moving-branch monodromy for the scalar component cover.

For C_a: h^12=t^4/((t-1)^3(t-a)), the nontrivial character
pieces of H2 of the minimal elliptic pullback are parabolic H1
of the elliptic local system tensored by the character.
This calculation concerns that auxiliary surface, not a filling of
the actual seven-dimensional mapping torus or a Theta_7 value.
"""
from pathlib import Path
from itertools import product
import json
import sympy as s
from sympy.matrices.normalforms import smith_normal_form

R1=s.Matrix([[0,1],[-1,-1]])
R2=s.Matrix([[0,-1],[1,0]])
Cw=s.Matrix([[1,0],[1,1]])
assert R1*R2*Cw==s.eye(2)

def cols(A):
    return s.Matrix.hstack(*A.columnspace()) if A.rank() else s.zeros(A.rows,0)
def ker(A):
    K=A.nullspace()
    return s.Matrix.hstack(*K) if K else s.zeros(A.cols,0)
def inv(w): return [-x for x in w[::-1]]
def red(w):
    out=[]
    for x in w:
        if out and out[-1]==-x:out.pop()
        else:out.append(x)
    return out
def subst(w,F):
    out=[]
    for x in w:out+=F[x-1] if x>0 else inv(F[-x-1])
    return red(out)
Id=[[1],[2],[3],[4]]
def sigma(i,sign):
    F=[w[:] for w in Id]
    if sign==1:F[i-1]=[i,i+1,-i];F[i]=[i]
    else:F[i-1]=[i+1];F[i]=[-(i+1),i,i+1]
    assert subst([1,2,3,4],F)==[1,2,3,4]
    return F
def braid_auto(braid):
    F=Id
    for b in braid:F=[subst(w,F) for w in sigma(abs(b),1 if b>0 else -1)]
    return F
def simplify(A):return A.applyfunc(s.simplify)

result={}
for k,chars in [(3,[1,s.I,1,-s.I]),(6,[1,-1,1,-1])]:
    G=[c*A.inv().T for c,A in zip(chars,[R1,R2,Cw,s.eye(2)])]
    assert simplify(G[0]*G[1]*G[2]*G[3])==s.eye(2)
    im=[cols(A-s.eye(2)) for A in G]
    prefix=s.eye(2);relations=[]
    for A,B in zip(G,im):relations.append(prefix*B);prefix=prefix*A
    rel=s.Matrix.hstack(*relations)
    K=ker(rel)
    block=s.diag(*im)
    cocycles=block*K
    cob=cols(s.Matrix.vstack(*[A-s.eye(2) for A in G]))
    basis=cob;reps=[]
    for v in cocycles.columnspace():
        if basis.row_join(v).rank()>basis.cols:
            basis=basis.row_join(v);reps.append(v)
    P=s.Matrix.hstack(*reps)
    dim=P.cols
    assert dim==({3:2,6:3}[k])
    Ps=[P[2*i:2*i+2,:] for i in range(4)]
    def evalword(w):
        A=s.eye(2);v=s.zeros(2,dim)
        for z in w:
            M=G[abs(z)-1];b=Ps[abs(z)-1]
            if z<0:b=-M.inv()*b;M=M.inv()
            v+=A*b;A=A*M
        return simplify(A),simplify(v)
    actions=[];cert={}
    for j in (1,2,3):
        tail=list(range(3,j,-1))
        braid=tail+[j,j]+[-x for x in tail[::-1]]
        F=braid_auto(braid)
        transformed=[]
        for i,w in enumerate(F):
            a,z=evalword(w)
            assert a==G[i]
            transformed.append(z)
        T=s.Matrix.vstack(*transformed)
        coeff=basis.gauss_jordan_solve(T)[0]
        assert simplify(basis*coeff-T)==s.zeros(*T.shape)
        A=simplify(coeff[-dim:,:]);actions.append(A)
        cert[j]={'braid':braid,'automorphism':F,'matrix':A.tolist(),
                 'det':s.simplify(A.det()),'trace':s.simplify(s.trace(A)),
                 'charpoly':str(s.factor(A.charpoly().as_expr()))}
    words={}
    for word in [(1,2),(1,-2),(1,2,-1,-2),(2,3,-2,-3),(1,3,-1,-3),
                 (1,1,2,2),(1,2,1,2)]:
        A=s.eye(dim)
        for i in word:A=A*(actions[abs(i)-1] if i>0 else actions[-i-1].inv())
        A=simplify(A)
        words[str(word)]={'matrix':A.tolist(),'trace':s.simplify(s.trace(A)),
                          'det':s.simplify(A.det()),
                          'charpoly':str(s.factor(A.charpoly().as_expr()))}
    result[k]={'ranks':[a.cols for a in im],'dimension':dim,
               'cocycles':[a.tolist() for a in Ps],
               'meridian_actions':cert,'word_actions':words}
x=s.symbols('x')
cyclo=s.Poly(x**4-x**2+1,x)
base_traces=[6]+[2-(1+4*(j%4==0)+3*(j%3==0)) for j in range(1,12)]
base_chars=[]
for k in range(12):
    q=sum(s.Rational(base_traces[j],12)*x**((-j*k)%12) for j in range(12))
    a=s.Poly(q,x).rem(cyclo).as_expr()
    assert a.is_Integer
    base_chars.append(int(a))
assert base_chars==[0,1,1,0,0,1,0,1,0,0,1,1]
base_poly=s.expand(s.cyclotomic_poly(6,x)*s.cyclotomic_poly(12,x))
assert base_poly.subs(x,1)==1
curve_forms=[]
for j in range(12):
    a=-s.floor(s.Rational(j+2,3))
    b=s.ceiling(s.Rational(j-3,4))
    c=s.ceiling(s.Rational(j-11,12))
    dim=max(0,-a-b-c-1)
    if dim:curve_forms.append((j,int(a),int(b),int(c),int(dim)))
assert curve_forms==[(7,-3,1,0,1),(10,-4,2,0,1),(11,-4,2,0,1)]
coinv=s.Matrix.hstack(R1-s.eye(2),R2-s.eye(2))
smith=smith_normal_form(coinv,domain=s.ZZ)
assert abs(smith[0,0])==abs(smith[1,1])==1
result['torsor_global_inputs']={
    'base_H1_traces':base_traces,'base_H1_characters':base_chars,
    'base_H1_characteristic_polynomial':str(base_poly),
    'det_identity_minus_deck_on_H1':1,
    'curve_holomorphic_form_characters_and_exponents':curve_forms,
    'elliptic_global_coinvariant_matrix':coinv.tolist(),
    'elliptic_global_coinvariant_smith':smith.tolist(),
    'H1_Lie_characters':[6,3,2],
    'four_torsion_projection_multiplier':9,
    'obstruction_projection_difference_in_12Z':(9*6-6)//12,
    'scope':'Torsor and line-bundle inputs; no actual mapping-torus filling or Theta7 evaluation.'}
txt=json.dumps(result,indent=2,default=str)+'\n'
print(txt,end='')
Path(__file__).with_suffix('.out.json').write_text(txt)
