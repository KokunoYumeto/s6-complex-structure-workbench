#!/usr/bin/env python3
"""Separate fresh KS homology work; partial checkpoint, original closed."""
from pathlib import Path
import json
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

ROOT=Path(__file__).resolve().parents[1]
raw=json.loads((ROOT/'agents/continuation6_iii_carriers/S6_SERIES_PUBLISH_III_02KS_raw_definitions.json').read_text())
row=raw['rows'][0]
J=s.Matrix([[0,1],[-1,0]])
I=s.eye(4)
T=[]
for index,(aa,gg) in enumerate(zip(row['elliptic_matrices'],row['generator_section_cocycle'])):
    A,g=s.Matrix(aa),s.Matrix(gg)
    z=(A-s.eye(2)).inv()*g if index!=1 else s.Matrix([-s.Rational(4,3),0])
    assert (A-s.eye(2))*z==g
    S=s.eye(4)
    S[:2,3]=z
    S[2,:2]=-12*z.T*J
    product=s.diag(A,s.eye(2))
    product[2,3]=raw['weights'][index]
    T.append(S.inv()*product*S)
assert T[0]*T[1]*T[2]==I
TII,Tc,Ts=T
D=s.Matrix.hstack(s.zeros(4),TII-I,Tc-I)
j0=s.Matrix.vstack(I,s.zeros(4),s.zeros(4))
j1=s.Matrix.vstack(s.zeros(4),I,s.zeros(4))
j2=s.Matrix.vstack(s.zeros(4),s.zeros(4),I)
j3=-s.Matrix.vstack(TII*Tc,Tc,I)
assert D*j3==I-Ts.inv()
FII=s.Matrix.hstack(I[:,2],s.Matrix([-1,1,0,1]))
Fc=s.Matrix.hstack(s.Matrix([-2,1,-16,0]),I[:,2])
Fs=s.Matrix.hstack(I[:,2],s.Matrix([-1,3,0,4]))
for matrix,fixed in [(TII,FII),(Tc,Fc),(Ts,Fs)]:
    assert (matrix-I)*fixed==s.zeros(4,2)
K=s.Matrix.hstack(j1*FII,j2*Fc,j3*Fs,j0*I[:,0],j0*I[:,1],j0*I[:,3])
assert D*K==s.zeros(4,9)
def smith_entries(M):
    B=smith_normal_form(M,domain=ZZ)
    return [abs(int(B[i,i])) for i in range(min(B.shape)) if B[i,i]]
assert smith_entries(D)==[1,1,3]
assert smith_entries(K)==[1]*9
pairs=[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
def exterior_square(M):
    return s.Matrix([[M[a,c]*M[b,d]-M[a,d]*M[b,c] for c,d in pairs] for a,b in pairs])
B2=s.Matrix.hstack(s.zeros(6),exterior_square(TII)-s.eye(6),exterior_square(Tc)-s.eye(6))
assert smith_entries(B2)==[1]*5
omega=s.Matrix([[12,0,0,0,0,-1]])
assert omega*B2==s.zeros(1,18)
for name,M in [('II',TII),('cusp',Tc),('star',Ts)]:
    print(name,'period=',M.tolist(),'wedge Smith=',smith_entries(exterior_square(M)-s.eye(6)))
print('D=',D.tolist())
print('D Smith=',smith_entries(D))
print('K=',K.tolist())
print('K Smith=',smith_entries(K),'D K=0')
print('B2=',B2.tolist())
print('B2 Smith=',smith_entries(B2),'omega B2=0')
print('PARTIAL: integral inverse maps, conductor specialization and complete global elimination remain due.')
