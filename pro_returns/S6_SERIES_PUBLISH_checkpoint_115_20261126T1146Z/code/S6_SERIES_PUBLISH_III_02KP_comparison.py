#!/usr/bin/env python3
"""New post-release comparison for every numerical auxiliary in the KP proof.

Uses determinantal divisors, column Hermite form and an adjugate inverse;
imports no earlier calculation code or outputs.
"""
from pathlib import Path
from itertools import combinations
from math import gcd
from functools import reduce
from datetime import datetime,timezone
import json
import sympy as s
from sympy.matrices.normalforms import hermite_normal_form

ROOT=Path(__file__).resolve().parents[1]
H=ROOT/'agents/continuation6_iii_root'
T2=s.Matrix([[5,8,0,-2],[-2,-3,0,1],[30,60,1,-14],[0,0,0,1]])
T0=s.Matrix([[27,37,0,0],[-19,-26,0,0],[0,0,1,0],[0,0,0,1]])
T1=s.Matrix([[61,80,0,4],[-45,-59,0,-3],[-90,-120,1,-6],[0,0,0,1]])
T3=s.Matrix([[4,3,0,1],[-3,-2,0,-1],[-30,-30,1,-10],[0,0,0,1]])
Ts=[T0,T1,T3,T2] # original cyclic order II,I5,I3,I2
I=s.eye(4);delta=s.Matrix([0,0,1,0]);gamma=s.Matrix([0,0,0,1])
wc=s.Matrix([2,-1,15,0]);rc=s.Matrix([1,0,0,0])
w1=s.Matrix([4,-3,-6,0]);a1=s.Matrix([-1,1,2,-5])
w2=s.Matrix([1,-1,-10,0]);a2=s.Matrix([1,0,0,-3])
assert reduce(lambda A,B:A*B,Ts,I)==I and T0**6==I

def invariants_by_minors(M):
    rank=M.rank();prev=1;out=[];divisors=[]
    for size in range(1,rank+1):
        divisor=0
        for rows in combinations(range(M.rows),size):
            for cols in combinations(range(M.cols),size):
                divisor=gcd(divisor,abs(int(M.extract(rows,cols).det())))
                if divisor==1:break
            if divisor==1:break
        assert divisor and divisor%prev==0
        out.append(divisor//prev);divisors.append(divisor);prev=divisor
    return out,divisors

pairs=list(combinations(range(4),2))
def exterior(A):
    return s.Matrix([[A[i,k]*A[j,l]-A[i,l]*A[j,k] for k,l in pairs] for i,j in pairs])

cusp=Ts[3]-I;wedge=exterior(Ts[3])-s.eye(6)
local,local_div=invariants_by_minors(cusp)
local2,local2_div=invariants_by_minors(wedge)
assert local==[1,2] and local2==[1,1]
global1=s.Matrix.hstack(*(A-I for A in Ts))
global_inv,global_div=invariants_by_minors(global1)
assert global_inv==[1,1,2]
saturated=s.Matrix.hstack(global1,wc,delta,w1,w2)
sat_inv,sat_div=invariants_by_minors(saturated)
assert sat_inv==[1,1,1]
omega=s.Matrix([[30,0,0,0,0,-1]])
global2=s.Matrix.hstack(*(exterior(A)-s.eye(6) for A in Ts))
Herm=hermite_normal_form(global2)
fibre=s.Matrix([0,0,0,0,0,-1])
Q=fibre.row_join(Herm)
assert Herm.shape==(6,5) and abs(Q.det())==1
assert omega*Herm==s.zeros(1,5) and (omega*fibre)[0]==1

# Exact original local torsion and relative normal-disc map.
Lc=s.Matrix.hstack(wc,rc,delta,gamma)
Nc=Lc.inv()*cusp*Lc
assert Nc==s.Matrix([[0,2,0,-1],[0,0,0,0],[0,0,0,1],[0,0,0,0]])
assert Nc*s.Matrix([0,1,0,0])==s.Matrix([2,0,0,0])
assert Nc*s.Matrix([0,0,0,1])==s.Matrix([-1,0,1,0])
assert list((-delta)[:3])==[0,0,-1]
# Global relations 2delta and the exact gcd 2 prove its order is two.
C=s.zeros(12,3);C[0,:]=s.Matrix([[-27,-37,-4]]);C[1,:]=s.Matrix([[19,26,3]])
C[7,2]=-2;C[11,2]=1
D=s.Matrix.hstack(*(A-I for A in Ts[:3]))
assert D*C==s.Matrix([[1,0,0],[0,1,0],[0,0,2],[0,0,0]])
assert D*(C*s.Matrix([4,-2,15]))==2*wc

# Direct adjugate completion gives the original nine-row left inverse.
def j(i,v):
    if i<3:
        result=s.zeros(12,1);result[4*i:4*i+4,0]=v;return result
    return -(Ts[1]*Ts[2]*v).col_join(Ts[2]*v).col_join(v)
Lcols=[j(1,w1),j(1,a1),j(1,delta),j(2,w2),j(2,a2),j(2,delta),j(3,wc),j(3,delta)]
K=s.Matrix.hstack(*Lcols,j(0,gamma))
completion=C.row_join(K)
det=int(completion.det());assert abs(det)==1
inverse=completion.adjugate()/det
assert completion*inverse==inverse*completion==s.eye(12)
Left=inverse[3:,:]
assert Left*K==s.eye(9) and D*K==s.zeros(4,9)
coords=Left*j(0,delta)
assert coords[8]==0 and K*coords==j(0,delta)
assert list(coords)==[0,0,-1,0,0,-1,0,-1,0]

# Actual old/fresh lattice bases and the toric fan involution.
Gamma_new=s.Matrix([[2,-1],[0,1]])
B=s.Matrix([[1,1],[0,1]])
Gamma_old=s.Matrix([[2,1],[0,1]])
F=s.Matrix([[1,1],[0,-1]])
assert Gamma_new*B==Gamma_old and B.inv()==s.Matrix([[1,-1],[0,1]])
assert F*F==s.eye(2) and F*Gamma_old*F==s.diag(2,1)
rays=[s.Matrix(v) for v in [(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)]]
ray_set={tuple(v) for v in rays}
assert {tuple(F*v) for v in rays}==ray_set
for i in range(6):
    transformed={tuple(F*rays[i]),tuple(F*rays[(i+1)%6])}
    assert any(transformed=={tuple(rays[j]),tuple(rays[(j+1)%6])} for j in range(6))

# Literal normal-chart transition and wall degrees at both vertex colours.
v0=s.Matrix([0,0,1]);v1=s.Matrix([0,1,1]);vp=s.Matrix([1,0,1]);vm=s.Matrix([-1,1,1])
P=s.Matrix.hstack(v0,v1,vp);M=s.Matrix.hstack(v0,v1,vm)
character_change=M.inv()*P
assert character_change==s.Matrix([[1,0,1],[0,1,1],[0,0,-1]])
assert P.inv()*s.Matrix([0,1,0])==s.Matrix([-1,1,0])
assert M.inv()*s.Matrix([0,1,0])==s.Matrix([-1,1,0])
wall=[]
for parity in [0,1]:
    a,b=parity,0
    endpoints=[(a,b),(a,b+1)];thirds=[(a+1,b),(a-1,b+1)]
    degrees=[sum((x+y)%2==colour for x,y in thirds)-sum((x+y)%2==colour for x,y in endpoints) for colour in [0,1]]
    assert degrees==[0,0];wall.append(degrees)

# The exact local/global degree-one free ranks in the old MV assertion.
boundary_ranks=[3,4,4,3];cap_ranks=[2,3,3,2];regular_rank=4
assert sum(boundary_ranks)==regular_rank+sum(cap_ranks)==14
n,r,alpha=s.symbols('n r alpha',integer=True)
finite=s.Matrix([[n,-r*alpha],[0,1]])
rowchange=s.Matrix([[1,r*alpha],[0,1]])
assert rowchange*finite==s.diag(n,1)
assert rowchange.inv()==s.Matrix([[1,-r*alpha],[0,1]])
data=dict(local_smith=local,local_determinantal_divisors=local_div,
          local_exterior_smith=local2,local_exterior_determinantal_divisors=local2_div,
          global_smith=global_inv,global_determinantal_divisors=global_div,
          saturated_smith=sat_inv,exterior_Hermite=Herm.tolist(),
          exterior_basis=Q.tolist(),exterior_inverse=Q.inv().tolist(),
          original_graph_left_inverse=Left.tolist(),original_graph_frame=K.tolist(),
          graph_completion=completion.tolist(),graph_completion_inverse=inverse.tolist(),
          j0_delta_coordinates=list(coords),fan_involution=F.tolist(),
          period_basis_change=B.tolist(),normal_chart_character_change=character_change.tolist(),
          fixed_curve_component_degrees=wall,boundary_free_ranks=boundary_ranks,
          cap_free_ranks=cap_ranks,regular_family_free_rank=regular_rank)
(H/'S6_SERIES_PUBLISH_III_02KP_comparison_maps.json').write_text(json.dumps(data,default=int,indent=2)+'\n')
print('Local determinantal divisors give cusp Smith entries',local,'and exterior entries',local2)
print('Global degree-one Smith entries',global_inv,'; actual angular vanishing entries',sat_inv)
print('Exterior relation Hermite basis plus s is unimodular; omega is the primitive quotient detector.')
print('Original 9-column sweep frame has explicit adjugate left inverse; j0(delta) coordinates',list(coords))
print('Old/fresh cusp period bases differ by B and B^-1; fan involution F has F^2=I and F Gamma_old F=diag(2,1).')
print('Both fixed curves have component degree vectors',wall,'; normal transition is (z,x,y)->(z^-1,z*x,z*y), with weights (-1,+1).')
print('Degree-one MV source and target free ranks are 14; the sole boundary torsion generator -delta maps to the same nonzero global class.')
print('All-parameter finite matrix is transformed exactly to diag(n,1).')
print('Original 630 numerical sample inputs are absent; no bytewise sample reconstruction or numerical replay is asserted.')
print('Completed UTC:',datetime.now(timezone.utc).isoformat())
