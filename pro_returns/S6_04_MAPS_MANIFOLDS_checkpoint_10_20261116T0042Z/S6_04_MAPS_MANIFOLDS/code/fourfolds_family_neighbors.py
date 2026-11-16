"""Exhaustive 2-neighbor lattice diagnostic for explicit family parameters.

For each v=0,1,2,3, enumerate EVERY nonzero proper F2 subspace of F2^6,
retain the subspaces stable under both finite matrices, and test the
corresponding integral index-power-of-two lattice. This is a bounded
neighbor search, not a classification of all stable lattices.
"""
from itertools import combinations, product
from math import prod, gcd, lcm
from functools import reduce
import json
from pathlib import Path
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ


def family(v):
    I=s.eye(5); A=s.zeros(5)
    for j in range(5): A[(j+1)%5,j]=1
    q=v*v-v+1
    X=I[:,0].row_join(I[:,2]+v*I[:,4])
    Y=s.Matrix([[0,-q,-v*v,-1,v],[0,1-v*q,-v*q,v*v-v,q]])
    B=A.inv()*(I-X*Y)
    P=I.copy(); P[:,0]=s.ones(5,1)/q
    An=P.inv()*A*P; Bn=P.inv()*B*P
    ss=v*v+v-1; rr=-(v+1)*(v*v-2)//2
    beta=s.Matrix([[ss,ss-v*rr,v*v*ss+v*rr,rr,-v*ss-rr]])
    AA=s.diag(1,An); BB=s.diag(1,Bn); BB[0,1:]=beta
    return AA,BB


def subspaces():
    for k in range(1,6):
        for pivots in combinations(range(6),k):
            free=[(i,j) for i,p in enumerate(pivots)
                  for j in range(p+1,6) if j not in pivots]
            for values in product((0,1),repeat=len(free)):
                cols=[1<<p for p in pivots]
                for (i,j),value in zip(free,values):
                    cols[i] |= value<<j
                yield pivots,cols


def contains(value,pivots,cols):
    for p,c in zip(pivots,cols):
        if (value>>p)&1:value ^= c
    return value==0


def action(M,value):
    return sum((sum(int(M[i,j]) for j in range(6) if (value>>j)&1)%2)<<i
               for i in range(6))


def tors(M):
    D=smith_normal_form(M,domain=ZZ)
    return prod(abs(int(D[j,j])) for j in range(min(D.shape)) if D[j,j])


allspaces=list(subspaces())
assert len(allspaces)==2823
records=[]
for v in range(4):
    A,B=family(v); stable=primitive=0; good=[]
    for pivots,cols in allspaces:
        if not all(contains(action(M,c),pivots,cols) for M in (A,B) for c in cols):
            continue
        stable+=1
        L=s.Matrix.hstack(*(s.Matrix([(c>>j)&1 for j in range(6)]) for c in cols),
                          *(2*s.eye(6)[:,j] for j in range(6) if j not in pivots))
        Ai=L.inv()*A*L; Bi=L.inv()*B*L
        assert all(z.q==1 for z in list(Ai)+list(Bi))
        N=Ai*Bi-s.eye(6)
        D=smith_normal_form(N,domain=ZZ)
        if [abs(int(z)) for z in D.diagonal() if z] != [1,1,1]:continue
        primitive+=1
        r=L.inv()*s.eye(6)[:,0]
        den=lcm(*(int(z.q) for z in r)); r*=den
        r/=reduce(gcd,(abs(int(z)) for z in r))
        da=tors((Ai-s.eye(6)).row_join(r))//tors(Ai-s.eye(6))
        db=tors((Bi-s.eye(6)).row_join(r))//tors(Bi-s.eye(6))
        if da==db==1:
            good.append({'pivots':pivots,'binary_columns':cols,'L':L.tolist(),
                         'A':Ai.tolist(),'B':Bi.tolist(),'invariant':list(r)})
    row={'parameter':v,'enumerated_subspaces':len(allspaces),'stable':stable,
         'primitive_cusp':primitive,'locally_split':len(good),'examples':good}
    records.append(row)
    print('parameter',v,'subspaces',len(allspaces),'stable',stable,
          'primitive cusp',primitive,'both finite divisibilities one',len(good))
    if good:print('first lattice',good[0]['L'],'invariant',good[0]['invariant'])
Path(__file__).with_suffix('.json').write_text(json.dumps(records,indent=2,default=int))
print('Complete bounded neighbor diagnostics saved; no global lattice exhaustion asserted.')
