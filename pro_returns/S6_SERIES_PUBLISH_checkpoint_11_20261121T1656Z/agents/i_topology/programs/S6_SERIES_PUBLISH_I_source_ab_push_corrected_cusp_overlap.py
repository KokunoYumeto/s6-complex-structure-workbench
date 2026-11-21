#!/usr/bin/env python3
"""Exact affine cusp overlap: all quantities are symbolic or integral."""
import json
from pathlib import Path
import sympy as sp

s,t,C,mu=sp.symbols('s t C mu')
delta=sp.Matrix([0,1])
gamma=sp.Matrix([6*mu,C-s-12*t])
L=s+12*t
f=sp.Matrix([mu*L/2,C*L/12-L**2/24+6*t])
b=gamma/12-delta/24
ds=(f.subs(s,s+1)-f).applyfunc(sp.expand)
dt=(f.subs(t,t+1)-f).applyfunc(sp.expand)
assert (ds-b).applyfunc(sp.expand)==sp.zeros(2,1)
assert (dt-gamma).applyfunc(sp.expand)==sp.zeros(2,1)
norm=sum((b.subs(s,s+k) for k in range(12)),sp.zeros(2,1)).applyfunc(sp.expand)
assert (norm-gamma+6*delta).applyfunc(sp.expand)==sp.zeros(2,1)
assert (b.subs(t,t+1)-b+delta).applyfunc(sp.expand)==sp.zeros(2,1)
assert (b.subs(s,s+1)-b+delta/12).applyfunc(sp.expand)==sp.zeros(2,1)

# The finite deck has q-height and r-height shifts one. Its twelfth power
# is exactly the original second period on cocharacters.
H=sp.eye(4)
H[1,2]=1
H[1,3]=1
G1=sp.eye(4)
G1[0,2]=12
G2=sp.eye(4)
G2[1,2]=12
G2[1,3]=12
assert H**12==G2
assert H*G1==G1*H

# Primitive cusp prisms, with twelve consecutive bottom cells in y1.
# For each bottom cell this is the k=0 bridge triangulation.
determinants=[]
for i in range(12):
    A=sp.Matrix([i,0,1,0]); B=sp.Matrix([i+1,0,1,0])
    C0=sp.Matrix([i,1,1,0]); D=sp.Matrix([i+1,1,1,0])
    E=sp.Matrix([0,0,0,1]); F=sp.Matrix([0,1,0,1])
    for cone in ((A,B,C0,E),(B,C0,D,E),(C0,D,E,F)):
        determinant=int(sp.Matrix.hstack(*cone).det())
        assert abs(determinant)==1
        determinants.append(determinant)

# The scalar phase in a twelfth iterate is exactly one:
# root deck contributes exp(2*pi*i*(0+...+11)/12), and
# the -delta/24 correction contributes exp(2*pi*i*12/24).
phase=sp.Rational(sum(range(12)),12)+sp.Rational(12,24)
assert phase==6

out={
    'status':'PASS',
    'section':[str(x) for x in f],
    'q_difference':[str(x) for x in ds],
    'r_difference':[str(x) for x in dt],
    'twelve_step_norm':[str(x) for x in norm],
    'desired_minus_one_rotation':'use -b and -f',
    'q_fibre_multiplicity_of_fractional_model':12,
    'phase_integer':int(phase),
    'H':list(H),'G1':list(G1),'G2':list(G2),
    'unit_cone_determinants':determinants,
    'scope':'Exact punctured-bidisc torsor comparison and a corrected r-central rotation; no completion at the bidisc origin is certified.'
}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2,default=str)+'\n')
print(json.dumps(out,indent=2,default=str))
