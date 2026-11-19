#!/usr/bin/env python3
"""Independent P1A.3 weights, residue and actual period derivatives.

Written before opening the target proof; no producing code is imported.
"""
from pathlib import Path
from itertools import combinations
import json
import sympy as s

gw=[0,-1,-2]
def coarse(n):return (4*n)//5+(-3*n)//4
def cohom(weights):
    dims=[0]*5;terms=[]
    for q in range(4):
        for sub in combinations(range(3),q):
            for w in weights:
                n=w+sum(gw[j] for j in sub);d=coarse(n)
                h0=max(d+1,0);h1=max(-d-1,0)
                dims[q]+=h0;dims[q+1]+=h1
                terms.append({'relative_degree':q,'weight':n,'coarse_degree':d,'H0':h0,'H1':h1})
    return dims,terms
A,At=cohom([5]);B,Bt=cohom([-4,-5,-6])
assert A==[1,2,1,0,0] and B==[0,0,0,1,1]
assert all(B[q]*A[q+1]==0 for q in range(4))
log=[a+b for a,b in zip(A,B)]
assert log==[1,2,1,1,1]
ordinary=log.copy();ordinary[0]-=1
assert ordinary==[0,2,1,1,1]
tangent=list(reversed(ordinary));assert tangent==[1,1,1,2,0]
section_exponent=(3*5+3)//4
assert section_exponent==4 and section_exponent-9==-5
a=-s.Rational(256,3125)
residue=a**(-5);assert residue!=0

lam,xi=s.symbols('lambda xi')
D=3125*lam+256
W=s.Matrix([
 [-8*(625*lam+48)/lam,-8,10*lam,s.Rational(75,2)*lam**2,0],
 [-s.Rational(125,2)/lam,-4*(625*lam+48)/lam,8,0,s.Rational(75,2)*lam**2],
 [300/lam**2,-375/lam,0,-48,60*lam],
 [120/lam**3,0,s.Rational(125,2)/lam,4*(625*lam+48)/lam,-8],
 [0,120/lam**3,50/lam**2,-s.Rational(125,2)/lam,8*(625*lam+48)/lam]
])/D
b=s.Matrix([[-s.Rational(25,6)/lam**2,-s.Rational(125,48)/lam,0,1,0]])/(lam-a)
Gamma=s.zeros(6);Gamma[0,1:6]=b;Gamma[1:6,1:6]=W
coef=s.Rational(625,96)*s.pi*s.I
F=s.zeros(6,3);F[1,0]=1;F[2,1]=1;F[3,2]=1;F[0,2]=coef*xi
quot=s.zeros(3,6);quot[0,0]=1;quot[0,3]=-coef*xi;quot[1,4]=1;quot[2,5]=1
assert quot*F==s.zeros(3)
base=(quot*Gamma*F).applyfunc(s.factor)
parameter=(quot*F.diff(xi)).applyfunc(s.factor)
detbase=s.factor(base.det())
assert s.factor(detbase-3/(625*lam**6*(lam-a)**3))==0
assert parameter.rank()==1 and parameter[0,2]==coef
assert parameter.det()==0
assert s.factor(detbase.subs(lam,1))!=0
out={'status':'PASS','old_target_proof_and_producing_code_read':False,
 'method':'Exact root-line cohomology enumeration and direct six-dimensional connection projection',
 'A_cohomology':A,'A_terms':At,'B_cohomology':B,'B_terms':Bt,
 'log_cotangent_twist':log,'ordinary_cotangent_twist':ordinary,'tangent_cohomology':tangent,
 'section_lambda_exponent':section_exponent,'residue_coefficient':str(residue),
 'quotient_times_F':'zero matrix',
 'base_KS_matrix':[[str(v) for v in row] for row in base.tolist()],
 'base_KS_determinant':str(detbase),'base_KS_determinant_lambda1':str(s.factor(detbase.subs(lam,1))),
 'parameter_KS_matrix':[[str(v) for v in row] for row in parameter.tolist()],
 'parameter_KS_rank':1,
 'scope':'The exact tangent dimensions and actual period derivatives are checked; the normal-sequence and analytic-germ arguments are written in P1A3_before_read.md.'}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ['status','A_cohomology','B_cohomology','tangent_cohomology','residue_coefficient','base_KS_determinant','parameter_KS_rank']},indent=2))
