"""Pure-braid action on middle parabolic cohomology of the split cusp.

This is an algebraic calculation, not a proof that the finite collision
models extend over a particular parameter cover.  The fourth monodromy
Cd is central, so dragging that puncture gives the same representation.
"""
from pathlib import Path
from itertools import combinations
import json
import sympy as s

A1=s.Matrix([[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]])
A2=s.Matrix([[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]])
Cw=s.eye(4);Cw[2,1]=1
Cd=s.eye(4);Cd[3,0]=-1
inds=list(combinations(range(4),2))
def ext(A): return s.Matrix([[A.extract(i,j).det() for j in inds] for i in inds])
G=[ext(A.inv().T) for A in [A1,A2,Cw,Cd]]
I=s.eye(6)
assert G[0]*G[1]*G[2]*G[3]==I
assert all(G[3]*a==a*G[3] for a in G)
P=[s.Matrix(a) for a in [
[[1,-8],[2,-7],[0,-6],[0,1],[-2,1],[-1,-1]],
[[6,-3],[3,0],[6,0],[-1,0],[-1,-1],[1,-1]],
[[0,0],[0,0],[0,0],[0,0],[0,-1],[0,0]],
[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]]]
Pall=s.Matrix.vstack(*P)
D0=s.Matrix.vstack(*[a-I for a in G])
C=s.Matrix.hstack(*D0.columnspace())
B=C.row_join(Pall)
assert B.rank()==7

def inv(w): return [-x for x in w[::-1]]
def reduce(w):
    out=[]
    for x in w:
        if out and out[-1]==-x:out.pop()
        else:out.append(x)
    return out
def subst(w,F):
    out=[]
    for x in w: out+=F[x-1] if x>0 else inv(F[-x-1])
    return reduce(out)
def compose(F,H): return [subst(w,F) for w in H]
Id=[[1],[2],[3],[4]]
def sigma(i,sign):
    # The induced automorphism fixes a1*a2*a3*a4 exactly.
    F=[w[:] for w in Id]
    if sign==1:F[i-1]=[i,i+1,-i];F[i]=[i]
    else:F[i-1]=[i+1];F[i]=[-(i+1),i,i+1]
    assert subst([1,2,3,4],F)==[1,2,3,4]
    return F
def word_auto(braid):
    F=Id
    for i in braid:F=compose(F,sigma(abs(i),1 if i>0 else -1))
    return F
def eval_word(w,z):
    A=I;ans=s.zeros(6,z[0].cols)
    for x in w:
        g=G[abs(x)-1];v=z[abs(x)-1]
        if x<0:v=-g.inv()*v;g=g.inv()
        ans+=A*v;A=A*g
    return A,ans

out={}
actions=[]
for j in [1,2,3]:
    tail=list(range(3,j,-1))
    braid=tail+[j,j]+[-x for x in tail[::-1]]
    F=word_auto(braid)
    transformed=[]
    for i,w in enumerate(F):
        a,z=eval_word(w,P)
        assert a==G[i],(j,i,a,G[i],w)
        transformed.append(z)
    T=s.Matrix.vstack(*transformed)
    coeff=B.gauss_jordan_solve(T)[0]
    assert B*coeff==T
    A=coeff[-2:,:]
    actions.append(A)
    out[f'fourth_around_{j}']={
        'artin_word':braid,'free_group_automorphism':F,
        'action':A.tolist(),'determinant':A.det(),'trace':s.trace(A),
        'characteristic_polynomial':str(A.charpoly().as_expr()),
        'first_identity_power':next((r for r in range(1,25) if A**r==s.eye(2)),None)}
out['product_in_order_1_2_3']=(actions[0]*actions[1]*actions[2]).tolist()
out['product_in_order_3_2_1']=(actions[2]*actions[1]*actions[0]).tolist()
txt=json.dumps(out,indent=2,default=str)+'\n'
print(txt,end='')
Path(__file__).with_suffix('.out.json').write_text(txt)
