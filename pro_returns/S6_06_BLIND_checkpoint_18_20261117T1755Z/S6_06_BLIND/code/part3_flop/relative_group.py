#!/usr/bin/env python3
"""Exact word and integer checks for the current-run flop boundary map."""
from pathlib import Path
import json
import sympy as s

ROOT=Path(__file__).resolve().parent
def red(w):
    out=[]
    for x in w:
        if out and out[-1]==-x: out.pop()
        else: out.append(x)
    return tuple(out)
def inv(w): return tuple(-x for x in w[::-1])
def subst(w,mp):
    out=()
    for x in w: out=red(out+(mp[x-1] if x>0 else inv(mp[-x-1])))
    return out
def compose(f,g): return tuple(subst(w,g) for w in f)
S=(1,);Q=(2,)
ID=(S,Q)
T=((-2,1,2),Q)
Ti=((2,1,-2),Q)
L=(S,(1,2))
Li=(S,(-1,2))
R=(S,(2,1))
Ri=(S,(2,-1))
A=Ti
B=(S,(1,2,-1))
Bi=(S,(-1,2,1))
checks={
 'T_inverse':compose(T,Ti)==ID and compose(Ti,T)==ID,
 'L_inverse':compose(L,Li)==ID,
 'R_inverse':compose(R,Ri)==ID,
 'L_R_commute':compose(L,R)==compose(R,L),
 'T_L_Tinverse_is_R':compose(T,compose(L,Ti))==R,
 'B_equals_L_Rinverse':compose(L,Ri)==B,
 'A_L_equals_L_A_B':compose(A,L)==compose(L,compose(A,B)),
}
# Relative normal-form coefficients (m,n,c) in L^m R^n C^c.
M=s.Matrix([[0,-1,0],[1,2,0],[0,1,1]])
v=s.Matrix(1,3,[1,1,0]);d=s.Matrix(1,3,[0,-2,0]);c=s.Matrix(1,3,[0,0,1])
checks.update({
 'conjugation_unimodular':M.det()==1,
 'variation_preserved':v*M==v,
 'derivative_change':d*M==d-2*v,
 'central_change':c*M==c+s.Matrix(1,3,[0,1,0]),
})
out={'checks':checks,'all_pass':all(checks.values()),
     'coefficient_matrix':[[int(x) for x in row] for row in M.tolist()],'inverse_matrix':[[int(x) for x in row] for row in M.inv().tolist()],
     'scope':'Exact local word identities and the specified relative-group central relation. Actual-family coefficient and oriented commutator comparison are separate proofs.'}
(ROOT/'relative_group.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
assert out['all_pass']
