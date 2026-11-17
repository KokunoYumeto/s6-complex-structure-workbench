#!/usr/bin/env python3
"""Exact algebra for the actual two-flop scalar construction; geometry is NV1–4."""
from pathlib import Path
from datetime import datetime,timezone
import json
import sympy as s
R=Path(__file__).resolve().parents[2]
checks=[]
def eq(name,x,y=0):
 if isinstance(x,s.MatrixBase) or isinstance(y,s.MatrixBase):
  d=s.Matrix(x)-s.Matrix(y)
  assert all(s.simplify(z)==0 for z in d),(name,d)
 else:assert s.simplify(x-y)==0,(name,s.simplify(x-y))
 checks.append(name)
J,H,chi=s.symbols('J H chi',integer=True)
t=s.symbols('t');x=t*t+1
f=x*x+t;g=x**3+s.Rational(3,2)*t*x+s.Rational(3,8)
poly=48*t**4+8*t**3+96*t*t+72*t+57
eq('actual OS45 section',x**3-3*f*x+2*g,s.Rational(3,4))
eq('actual four selected cusp polynomial',64*(g*g-f**3),poly)
eq('four selected cusps simple',s.gcd(poly,s.diff(poly,t)),1)
eq('ordinary cap t=0 regular',poly.subs(t,0),57)
kap,al,gam,eta,q=s.symbols('kappa alpha g eta q',nonzero=True)
a,b,c=s.symbols('a b c',nonzero=True)
rows=[s.Matrix([kap*al*b*c,al**-1*a*b,kap**-1/b]),s.Matrix([gam*eta*b*c,eta**-1/c,gam**-1*a*c]),s.Matrix([1/a,a*b,a*c])]
for i,row in enumerate(rows):eq(f'height row C{i}',s.prod(row),a*b*c)
u,v,w=rows[0]
eq('C0 native reciprocal',kap*w,1/b)
eq('C0 native first normal',al*v,b*a)
eq('C0 native second normal',u/(kap*al),b*c)
AA,DD=s.symbols('A D',nonzero=True)
old_action={a:a/(AA*DD),b:AA*b,c:DD*c}
for i,row in enumerate(rows):
 expected=s.Matrix([AA*DD*row[0],DD**-1*row[1],AA**-1*row[2]])
 eq(f'full unit torus action row C{i}',row.subs(old_action,simultaneous=True),expected)
# Exact quaternion-chart overlap in the convention a+j*b.
zr,zi,ar,ai,cr,ci=s.symbols('zr zi ar ai cr ci',real=True)
z=zr+s.I*zi;n0=ar+s.I*ai;n1=cr+s.I*ci
def Q(u,v):return s.Matrix([[u,-s.conjugate(v)],[v,s.conjugate(u)]])
eq('literal K30/C0 Cox quaternion overlap',Q(1,z)*Q(n0,s.conjugate(n1)),Q(1/z,1)*Q(z*n0,s.conjugate(z*n1)))
# K30 reference-to-current inverse versus actual current-to-reference seam.
e,th=s.symbols('e theta',integer=True);L0,LW=s.symbols('loglambda0 logW')
cut_log=e*th*(L0-LW)+2*s.pi*s.I*e*J*th**2
native_inverse=e*th*(L0-LW)+s.pi*s.I*e*J*th*(th-1)
eq('full based physical-delta comparison log',cut_log-native_inverse,s.pi*s.I*e*J*th*(th+1))
eq('delta comparison starts at zero',(cut_log-native_inverse).subs(th,0),0)
eq('delta comparison endpoint integral winding',(cut_log-native_inverse).subs(th,1)/(2*s.pi*s.I),e*J)
# Exact lattice/period and target trace identities.
P=s.Matrix([[1,-1],[0,1]]);Q1=s.Matrix([[1,0],[-1,1]])
eq('first basis determinant',P.det(),1);eq('second basis determinant',Q1.det(),1)
eq('actual two-flop basis',P*Q1,s.Matrix([[2,-1],[-1,1]]))
B0=s.diag(0,2*J);B1=s.simplify(P.inv()*B0*P)
eq('actual full-unit winding conjugation',B1,s.Matrix([[0,2*J],[0,2*J]]))
physical=P.inv()*s.Matrix([0,1]);eq('physical target cocharacter',physical,s.Matrix([1,1]))
wgt=s.Matrix([physical[0],physical[1],-sum(physical)])
d=s.Matrix([-physical[0]-2*physical[1],-2*physical[0]-physical[1],physical[0]-physical[1]])
l=s.Matrix([B1[1,1]-B1[1,0],B1[0,0]-B1[0,1],B1[1,1]])
I=s.Matrix([J*wgt[i]+d[i]*(l[i]-J) for i in range(3)])
W=s.Matrix([J*wgt[i]-d[i]*(l[i]-J) for i in range(3)])
eq('target l',l,s.Matrix([2*J,-2*J,2*J]));eq('target I',I,s.Matrix([-2*J,10*J,-2*J]));eq('target W',W,s.Matrix([4*J,-8*J,-2*J]))
V0=s.Matrix([[2*J-6*H,2*J,-2*J],[2*J,2*J,0],[-2*J,0,2*J]])
D0=s.Matrix([2*J+6*H-24*chi,-2*J,2*J]);basis=[s.eye(3)[:,i] for i in range(3)]
I0=s.Matrix([-2*J,2*J,-2*J]);W0=s.Matrix([2*J,0,0]);w0=[0,1,-1]
for i in [1,2]:
 eq(f'initial integral variation prism {i}',V0*(w0[i]*basis[i]-w0[0]*basis[0]),I0[i]*basis[i]-I0[0]*basis[0])
 eq(f'initial derivative prism {i}',w0[i]*D0[i]-w0[0]*D0[0],W0[i]-W0[0])
eq('initial ordinary C0 left',-(D0[0]+V0[0,0])/2,12*chi-2*J)
eq('initial ordinary C0 right',(D0[0]-V0[0,0])/2,6*H-12*chi)
va=V0[0,0];db=D0[0];r=s.Matrix([1/wgt[i] for i in range(3)])
cc=wgt[2]**2*va-wgt[2]*I[2];ee=wgt[2]*(2*va-db)-W[2]
V1=s.simplify(s.diag(*[I[i]/wgt[i] for i in range(3)])+cc*r*r.T)
D1=s.simplify(s.Matrix([(W[i]+ee)/wgt[i] for i in range(3)]))
expected=s.Matrix([[2*J-24*H,4*J-24*H,-2*J+12*H],[4*J-24*H,14*J-24*H,-2*J+12*H],[-2*J+12*H,-2*J+12*H,2*J-6*H]])
eq('complete target variation',V1,expected)
eq('complete target derivative',D1,s.Matrix([2*J+36*H-48*chi,-10*J+36*H-48*chi,2*J-18*H+24*chi]))
eq('selected actual normal reset V',V1[2,2],va);eq('selected actual normal reset delta',D1[2],2*va-db)
for i in [1,2]:
 eq(f'target integral variation prism {i}',V1*(wgt[i]*basis[i]-wgt[0]*basis[0]),I[i]*basis[i]-I[0]*basis[0])
 eq(f'target derivative prism {i}',wgt[i]*D1[i]-wgt[0]*D1[0],W[i]-W[0])
n_double=s.expand((D1[1]-V1[1,1])/2);n_single=s.expand(n_double/2)
eq('target doubled native right',n_double,30*H-24*chi-12*J)
eq('target single free right',n_single,15*H-12*chi-6*J)
example={J:1,H:8,chi:1};A=H/2-chi
first=s.expand(A+(6*H-12*chi)/2);second=s.expand(first+n_single)
eq('OS45 initial physical class',A.subs(example),3)
eq('OS45 first fixed flop integer',first.subs(example),21)
eq('OS45 second native right',n_single.subs(example),102)
eq('OS45 final unreduced physical sum',second.subs(example),123)
# Direct full-unit basis transformations and literal two ruling charts.
A11,A12,A21,A22=s.symbols('A11 A12 A21 A22',nonzero=True)
Aprime=s.Matrix([[A11*A21,A12*A22/(A11*A21)],[A21,A22/A21]])
for i in range(2):
 for j in range(2):
  prod=s.prod(s.Matrix([[A11,A12],[A21,A22]])[h,k]**(P.inv()[i,h]*P[k,j]) for h in range(2) for k in range(2))
  eq(f'full period unit target {i}{j}',prod,Aprime[i,j])
z,n0,n1=s.symbols('z n0 n1',nonzero=True)
new=s.Matrix([n0/n1,z*n1,n1]);new2=s.Matrix([n1/n0,z*n0,n0])
eq('actual other-ruling height',s.prod(new),z*n0*n1)
eq('other-ruling reciprocal',new[0]*new2[0],1)
eq('other-ruling first normal transition',new2[1],new[0]*new[1])
eq('other-ruling second normal transition',new2[2],new[0]*new[2])
res={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','proof_status':'Working NV1–4; C0/native and target-product geometry submitted for independent audit. No active return theorem is promoted by this certificate.','checks':checks,'check_count':len(checks),'full_unit_scope':'All original kappa,alpha,g,eta; actual ordinary q^e*u closing and literal double seam retained.','initial_double':{'V':[[str(x) for x in row] for row in V0.tolist()],'delta':[str(x) for x in D0]},'target_double':{'basis':P.tolist(),'V':[[str(x) for x in row] for row in V1.tolist()],'delta':[str(x) for x in D1],'C1_native_right':str(n_double)},'concrete_OS45':{'source':'K10 explicit equation and G; M=8G-O,Q=G; scalar lambda=r; ordinary cap t=0; one marked simple zero tau','J':1,'H':8,'chi':1,'two_flop_basis':(P*Q1).tolist(),'initial_physical_class':3,'first_flop_class':21,'second_native_right':102,'working_final_class_mod28':11},'proof':'notes/part3_scalar_nonvertical_working.md'}
(R/'code/part3/scalar_nonvertical.json').write_text(json.dumps(res,indent=2,default=str)+'\n')
print(f'PASS: {len(checks)} exact identities. Candidate two-flop class11 remains submitted for geometric audit.')
