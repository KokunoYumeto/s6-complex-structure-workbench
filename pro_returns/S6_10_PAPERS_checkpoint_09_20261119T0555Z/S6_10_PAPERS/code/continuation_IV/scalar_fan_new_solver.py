#!/usr/bin/env python3
"""New exact solution of the complete prism equations, not the closed formula.

Inputs are K73's mathematical seed, monomial winding and prism equations,
with K115's two actual primitive-family profiles. No producing code imported
or read. Each target is reconstructed by Gaussian elimination of ten
equations in nine free entries over Q. Runs at l=1 and l=2 recover exact
affine coefficients; linearity follows from the displayed linear equations.
"""
from fractions import Fraction as F
from pathlib import Path
from itertools import product
from math import gcd
import json

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'analysis/continuation_IV'
Q=(((1,-1),(0,1)),((1,0),(-1,1)))
VI=((0,0),(0,1),(0,2),(1,1),(1,2),(2,2))
def vi(a,b): return VI.index(tuple(sorted((a,b))))
def mul(A,B): return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)) for i in range(2))
def inv(A):
    a,b=A[0]; c,d=A[1]
    assert a*d-b*c==1
    return ((d,-b),(-c,a))
def gauss(equations):
    original=[[F(x) for x in row] for row in equations]
    rows=[r[:] for r in original]
    pivots=[]; pos=0
    for col in range(9):
        choices=[k for k in range(pos,len(rows)) if rows[k][col]]
        if not choices: continue
        k=choices[0]; rows[pos],rows[k]=rows[k],rows[pos]
        q=rows[pos][col];rows[pos]=[x/q for x in rows[pos]]
        for k in range(len(rows)):
            if k!=pos and rows[k][col]:
                q=rows[k][col];rows[k]=[x-q*y for x,y in zip(rows[k],rows[pos])]
        pivots.append(col);pos+=1
    assert pivots==list(range(9)), ('rank',pivots)
    assert all(any(r[:9]) or r[9]==0 for r in rows), 'inconsistent'
    sol=[rows[k][9] for k in range(9)]
    assert all(sum(a*x for a,x in zip(r[:9],sol))==r[9] for r in original)
    return sol
def seed(J,H,chi,j):
    V=[2*J-6*H+6*J*j*(j-1),2*J*(1-2*j),2*J*(2*j-1),2*J,0,2*J]
    delta=[2*J+6*H-24*chi-6*J*j*(j-1),2*J*(2*j-1),2*J*(1-2*j)]
    return list(map(F,V+delta)),F(H,2)-chi-F(J*j*(j-1),2)
def step(P,state,S,J,edge):
    P=mul(P,Q[edge]);Pinv=inv(P)
    B=mul(mul(Pinv,((0,0),(0,2*J))),P)
    ell=(B[1][1]-B[1][0],B[0][0]-B[0][1],B[1][1])
    x,y=Pinv[0][1],Pinv[1][1]
    w=(x,y,-x-y);d=(-x-2*y,-2*x-y,x-y)
    assert all(w)
    I=[J*w[k]+d[k]*(ell[k]-J) for k in range(3)]
    W=[J*w[k]-d[k]*(ell[k]-J) for k in range(3)]
    a,b=state[vi(edge,edge)],state[6+edge]
    equations=[]
    for j in (1,2):
        for k in range(3):
            row=[F(0)]*10
            row[vi(k,j)]+=w[j];row[vi(k,0)]-=w[0]
            row[9]=I[j]*(k==j)-I[0]*(k==0)
            equations.append(row)
    row=[F(0)]*10;row[vi(2,2)]=1;row[9]=a;equations.append(row)
    for j in (1,2):
        row=[F(0)]*10;row[6+j]=w[j];row[6]-=w[0];row[9]=W[j]-W[0];equations.append(row)
    row=[F(0)]*10;row[8]=1;row[9]=2*a-b;equations.append(row)
    solution=gauss(equations)
    increment=(b-a)/4
    assert all(v.denominator==1 for v in solution),('nonintegral free invariant',P,solution)
    assert increment.denominator==1,('nonintegral increment',P,increment)
    return P,solution,S+increment,increment
def profile(branch,l):
    return (3*l+2,6*(3*l+2),F(l+1)) if branch=='M6' else (l,F(2*l,3),F(l,3))
def execute(branch,l,j,word):
    J,H,chi=profile(branch,l);P=((1,0),(j,1));state,S=seed(J,H,chi,j);incs=[]
    for edge in word:
        P,state,S,increment=step(P,state,S,J,edge);incs.append(increment)
    return P,state,S,incs
def affine(v1,v2):
    slope=v2-v1;constant=v1-slope
    assert slope.denominator==1 and constant.denominator==1
    return [int(constant),int(slope)]

records=[];solves=0;prism_equations=0
for branch in ('M6','M2'):
    for j in range(-3,5):
        for depth in range(1,7):
            for tail in product((0,1),repeat=depth-1):
                word=(0,)+tail
                r1=execute(branch,1,j,word);r2=execute(branch,2,j,word)
                assert r1[0]==r2[0]
                coeff=[affine(a,b) for a,b in zip(r1[1],r2[1])]
                Scoeff=affine(r1[2],r2[2]);inc=[affine(a,b) for a,b in zip(r1[3],r2[3])]
                if branch=='M2': assert all(c[0]==0 for c in coeff+[Scoeff]+inc)
                # Third independent l value checks the predicted affine solution,
                # including every retained native increment along this word.
                r3=execute(branch,3,j,word)
                assert r3[1]==[F(c+3*m) for c,m in coeff]
                assert r3[2]==Scoeff[0]+3*Scoeff[1]
                assert r3[3]==[F(c+3*m) for c,m in inc]
                solves+=3*depth;prism_equations+=30*depth
                records.append(dict(branch=branch,seed=j,word=list(word),basis=r1[0],free_invariant_coefficients=coeff,S_coefficients=Scoeff,native_increment_coefficients=inc))

# Complete elementary residue argument for the M6 vertical witnesses.
units=[]
for l in range(7):
    j=0 if gcd(8*l+5,28)==1 else 4
    S=8*l+5-(3*l+2)*j*(j-1)//2
    assert gcd(S,28)==1
    units.append(dict(l_mod7=l,seed=j,S_mod28=S%28))
assert all((-(l*2*(2-1)//2))==-l for l in range(1,29))

path=OUT/'scalar_fan_new_solver.paths.jsonl'
with path.open('w') as f:
    for row in records:f.write(json.dumps(row,separators=(',',':'))+'\n')
summary={'all_passed':True,'profiles':['M6: J=3l+2, Hhat=6(3l+2), chihat=l+1','M2: J=l, Hhat=2l/3, chihat=l/3'],
         'seed_range':[-3,4],'word_rule':'first edge0; every binary continuation, length1 through6',
         'family_path_records':len(records),'exact_target_gaussian_solves':solves,'exact_prism_equations_verified':prism_equations,
         'M2_all_recorded_polynomials_homogeneous_in_l':True,'M6_vertical_unit_witnesses':units,
         'paths':str(path.relative_to(ROOT)),
         'scope':'Exact finite arithmetic audit of the stated prism systems; no new claim that finite enumeration proves every geometric fan or endpoint.'}
(OUT/'scalar_fan_new_solver.output.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
