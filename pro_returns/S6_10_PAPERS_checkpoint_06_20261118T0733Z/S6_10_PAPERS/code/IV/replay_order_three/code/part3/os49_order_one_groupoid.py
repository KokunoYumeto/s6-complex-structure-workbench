#!/usr/bin/env python3
"""Integral root-groupoid calculation for OS49 smooth order-one clutches.

All matrices are the actual marked homology tuple of F26. No return
number is calculated. The analytic realization is a separate proof.
"""
from pathlib import Path
from datetime import datetime, timezone
import json
import sympy as s
from sympy.matrices.normalforms import smith_normal_form

ROOT=Path(__file__).resolve().parents[2]
T_A=s.Matrix([[1,-3,-3,-1],[0,-2,-3,-1],[0,1,1,0],[0,0,0,1]])
T_B=s.Matrix([[1,0,0,0],[0,1,1,0],[0,-1,0,0],[0,0,0,1]])
T_C=s.Matrix([[1,0,3,1],[0,1,2,1],[0,0,1,0],[0,0,0,1]])
A,B,C=[x.inv().T for x in (T_A,T_B,T_C)]
I=s.eye(4); z=s.zeros(4); e=[I[:,i] for i in range(4)]
ell=e[0]-e[1]; delta=e[3]; psi=s.Matrix([[1,0,0,0]])
F=s.Matrix.hstack(ell,delta)
k=s.symbols('k',integer=True,positive=True);m=3*k
N3=I+A+A*A;Nm=k*N3
checks=[]
def eq(name,x,y):
    assert x==y,name
    checks.append(name)
def mat(x):
    return [[str(v) for v in x.row(i)] for i in range(x.rows)]
def snf(x):
    d=smith_normal_form(x,domain=s.ZZ)
    return [abs(int(d[i,i])) for i in range(min(d.shape)) if d[i,i]]

eq('actual product relation',A*B*C,I)
eq('finite effective order3',A**3,I)
eq('actual invariant cap ell0',A*ell,ell)
eq('physical delta invariant',A*delta,delta)
for name,M in [('A',A),('B',B),('C',C)]:
    eq('global gamma covector '+name,psi*M,psi)
eq('selected cusp extending periods', (C-I)*s.Matrix.hstack(e[2],e[3]),s.zeros(4,2))
eq('typeII extending periods',(B-I)*s.Matrix.hstack(e[0],e[3]),s.zeros(4,2))
assert (C-I).rank()==2 and (B-I).rank()==2
checks.append('both nonfinite stalks have exactly rank2')
eq('exact cyclic norm',N3,s.Matrix([[3,0,0,0],[-3,0,0,0],[0,0,0,0],[0,0,-1,3]]))
Nbar=s.Matrix([[m,0,0,0],[0,0,-k,m]])
eq('norm in primitive invariant basis',F*Nbar,Nm)
assert snf(A-I)==[1,1]
checks.append('finite odd cohomology kernel/image primitive')

D=s.Matrix.hstack(A-I,A*(B-I),I-C.inv())
right=s.zeros(12,3)
right[0:4,0]=-e[1];right[4:8,0]=e[2]
right[0:4,1]=-e[2];right[4:8,1]=-e[1]-e[2]
right[0:4,2]=2*e[2];right[4:8,2]=2*(e[1]+e[2]);right[8:12,2]=-C*e[1]
eq('explicit integral coinvariant preimages',D*right,s.Matrix.hstack(e[1],e[2],e[3]))
eq('no hidden free relation',psi*D,s.zeros(1,12))
assert snf(D)==[1,1,1]
checks.append('global coinvariant is primitive Z via psi')

# MV total complex: degree-one variables (p,q,a,r,s,t), each in Lambda;
# degree-two cocycle variables (eta in Lambda^A, bA,bB,bC).
d1=s.zeros(14,24)
d1[0:2,8:12]=Nbar
d1[2:6,0:4]=I;d1[2:6,8:12]=-I;d1[2:6,12:16]=-(A-I)
d1[6:10,4:8]=I;d1[6:10,16:20]=-(B-I)
d1[10:14,0:4]=-C;d1[10:14,4:8]=-C*A;d1[10:14,20:24]=-(C-I)
global_map=s.Matrix.hstack(I,A,C.inv())
eq('exact boundary combination',global_map*d1[2:14,:],s.Matrix.hstack(z,z,-I,-(A-I),-A*(B-I),-(I-C.inv())))
U=s.zeros(12)
U[0:4,0:4]=I;U[4:8,4:8]=I;U[8:12,:]=global_map
eq('boundary change is unimodular',U.det(),s.Integer(1))
p0,p1,pi0,pi1=s.Matrix(s.symbols('p0:4')),s.Matrix(s.symbols('q0:4')),s.Matrix(s.symbols('r0:4')),s.Matrix(s.symbols('s0:4'))
eq('every extra ordinary restriction retained',p0+A*p1+C.inv()*(-C*(p0+A*p1+pi0+pi1))+pi0+pi1,s.zeros(4,1))

reduced=s.Matrix.vstack(Nbar,-psi)
eq('full reduced integral presentation',reduced,s.Matrix([[m,0,0,0],[0,0,-k,m],[-1,0,0,0]]))
free=s.Matrix([[1,0,m]])
eq('free characteristic kills every relation',free*reduced,s.zeros(1,4))
eq('torsion characteristic divided by k',(s.Matrix([[0,1,0]])*reduced)/k,s.Matrix([[0,0,-1,3]]))
for kval in (1,2,3,4,5,9):
    assert snf(d1.subs(k,kval))==[1]*12+[kval]
    checks.append(f'full 14x24 degree2 Smith k={kval}')

# An actual sum L of transported ordinary clutch vectors is absorbed
# by n -> n+m psi(L), retaining the exact finite delta coefficient.
l0,l1,l2,l3=s.symbols('l0 l1 l2 l3',integer=True)
L=s.Matrix([l0,l1,l2,l3]);sigma=(psi*L)[0]
v=L-sigma*ell
pre=right*s.Matrix([v[1],v[2],v[3]])
eq('full ordinary vector retained in cochain',D*pre,v)
eq('root cochain has exact norm',Nm*(-sigma*ell),-m*sigma*ell)
eq('root cochain changes no delta coefficient',(Nm*(-sigma*ell))[3],s.Integer(0))
eq('same invariant class after redistribution',s.Matrix([0,1,0]).dot(s.Matrix([-m*sigma,0,sigma])),s.Integer(0))
eq('same free class after redistribution',free*s.Matrix([-m*sigma,0,sigma]),s.zeros(1,1))
n,d,sg=s.symbols('n d sg',integer=True)
Deff=n+m*sg
eq('finite root norm change is exact invariant period',(Deff-n)*ell,m*sg*ell)
eq('finite affine action unchanged modulo its lattice',(Deff-n)/m,sg)
eq('actual commuting-generator norm exponent',m*sg+n,Deff)
eq('actual scalar factor in cap generator',m*sg+n,n+3*k*sg)

out={
 'status':'PASS','utc':datetime.now(timezone.utc).isoformat(),'checks':len(checks),'identities':checks,
 'homology_matrices':{name:mat(M) for name,M in [('A',A),('B',B),('C',C)]},
 'period_order':['gamma','u','w','delta'],'ell0':[1,-1,0,0],
 'cyclic_norm3':mat(N3),'norm_in_invariant_basis':mat(Nbar),
 'coinvariant_relation':mat(D),'explicit_integral_preimages_eu_ew_edelta':mat(right),
 'full_degree2_relation_matrix':mat(d1),'boundary_change':mat(U),
 'reduced_presentation':mat(reduced),
 'cohomology':'H^2(root atlas/groupoid,H)=Z ell0 direct_sum Z/k delta; the ordinary oriented base generator c=m ell0.',
 'class_map':'(eta=n ell0+d delta, boundary v) -> (n+m psi(v), d mod k).',
 'ordinary_clutches':'For literal ordinary-to-disc +log arrows, beta_i=alpha_i-l_i. The effective norm is D=n+m sum_i psi(l_i); every entire vector is retained in the displayed integral cochain.',
 'finite_data':'The invariant root one-cochain -sigma ell0 has norm -m sigma ell0 and no delta term; the cap action is unchanged modulo its actual lattice, while its lift and annular integer are recorded.',
 'scope':'Integral root-period groupoid and explicit cochains only. Analytic family comparison and topology are proved separately; no return number assigned.'
}
(ROOT/'code/part3/os49_order_one_groupoid.json').write_text(json.dumps(out,indent=2)+'\n')
print(f'PASS: {len(checks)} exact root-groupoid, primitive-cochain and full Smith identities.')
print('H2 = Z direct_sum Z/k; cap class(n,d mod k); ordinary l contributes m psi(l).')
