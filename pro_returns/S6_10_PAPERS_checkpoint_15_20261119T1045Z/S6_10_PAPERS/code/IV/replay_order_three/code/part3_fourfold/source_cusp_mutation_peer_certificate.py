#!/usr/bin/env python3
"""Independent exact checks of the K59 native arrows and all-j induction."""
from pathlib import Path
from datetime import datetime,timezone
import json,sympy as S
ROOT=Path(__file__).resolve().parents[2]
checks=[]
def check(name,expr):
 vals=list(expr) if isinstance(expr,S.MatrixBase) else [expr]
 assert all(S.simplify(v)==0 for v in vals),(name,expr)
 checks.append(name)
a,b,c=S.symbols('a b c',nonzero=True)
A11,A12,A21,A22=S.symbols('A11 A12 A21 A22',nonzero=True)
units=S.Matrix([[A11,A12],[A21,A22]])
Q=[S.Matrix([[1,-1],[0,1]]),S.Matrix([[1,0],[-1,1]]),S.Matrix([[1,1],[0,1]])]
expected=[S.Matrix([[A11*A21,A12*A22/(A11*A21)],[A21,A22/A21]]),
 S.Matrix([[A11/A12,A12],[A11*A21/(A12*A22),A12*A22]]),
 S.Matrix([[A11/A21,A11*A12/(A21*A22)],[A21,A21*A22]])]
for i,q in enumerate(Q):
 qi=q.inv()
 u=S.Matrix(2,2,lambda r,s:S.prod(units[h,k]**(qi[r,h]*q[k,s]) for h in range(2) for k in range(2)))
 check(f'Q{i} determinant',q.det()-1)
 check(f'Q{i} full unit map',u-expected[i])
old=[(b,a,c),(c,a,b),(a,b,c)]
new=[(a/c,b*c,c),(a/b,b,b*c),(a*c,b/c,c)]
for i,(z,n0,n1) in enumerate(old):
 triple=new[i]
 native=triple if i in (0,1) else (triple[1],triple[0],triple[2])
 want=(n0/n1,z*n1,n1) if i!=1 else (n0/n1,n1,z*n1)
 check(f'Q{i} native first arrow',S.Matrix(native)-S.Matrix(want))
 check(f'Q{i} literal q',S.prod(triple)-a*b*c)
check('Q0 native second arrow',S.Matrix([c/a,a*b,a])-S.Matrix([old[0][2]/old[0][1],old[0][0]*old[0][1],old[0][1]]))
check('Q1 swapped native second arrow',S.Matrix([b/a,a,a*c])-S.Matrix([old[1][2]/old[1][1],old[1][1],old[1][0]*old[1][1]]))
vertex=S.Matrix([A11*b,a*b/A21,A21*c/(A11*b)])
U=expected[2]
native_second=S.Matrix([U[0,0]*vertex[2],U[1,0]*vertex[1],vertex[0]/(U[0,0]*U[1,0])])
check('Q2 complete second-vertex unit cancellation',native_second-S.Matrix([c/b,a*b,b]))
ep=S.Matrix([[1,1],[1,1]])/2;em=S.eye(2)-ep
check('U2 path complementary projections',ep*em)
check('U2 path idempotent plus',ep*ep-ep)
check('U2 path idempotent minus',em*em-em)
check('U2 path swap endpoint',ep-em-S.Matrix([[0,1],[1,0]]))
m,n=S.symbols('m n',integer=True)
aa=-(m+n);bb=aa+2*n
check('selected variation reset',-(m+2*n-n)-aa)
check('selected derivative reset',aa-2*n-(2*aa-bb))
check('selected central increment',(bb-aa)/2-n)
j=S.symbols('j',integer=True,nonnegative=True)
def state(j):
 v=S.Matrix([[0,6*(j+1),-6],[6*(j+1),18*j*(j+1),-6*j],[-6,-6*j,0]])
 d=S.Matrix([-12*(j+1),-24*j*(j+1)-12,12*j])
 return v,d
v,d=state(j);w=S.Matrix([j,1,-j-1]);l=[0,-6*(j+1),0];dw=[-j-2,-2*j-1,j-1]
I=S.Matrix([-3*w[i]+dw[i]*(l[i]+3) for i in range(3)])
W=S.Matrix([-3*w[i]-dw[i]*(l[i]+3) for i in range(3)])
check('all-j I trace',I-S.Matrix([-6*(j+1),12*j*(j+1),6*j]))
check('all-j W trace',W-S.Matrix([6,-12*j*(j+1)-6,6]))
for h in (1,2):
 e=S.zeros(3,1);e[h]=w[h];e[0]=-w[0]
 z=S.zeros(3,1);z[h]=I[h];z[0]=-I[0]
 check(f'all-j variation trace {h}',v*e-z)
 check(f'all-j stable trace {h}',w[h]*d[h]-w[0]*d[0]-(W[h]-W[0]))
vp,dp=state(j+1)
wp=S.Matrix([j+1,1,-j-2]);Ip=I.subs(j,j+1);Wp=W.subs(j,j+1)
rr=S.Matrix([1/x for x in wp]);sel_a=v[0,0];sel_b=d[0]
cc=wp[2]**2*sel_a-wp[2]*Ip[2]
ee=wp[2]*(2*sel_a-sel_b)-Wp[2]
vv=S.diag(*[Ip[k]/wp[k] for k in range(3)])+cc*rr*rr.T
dd=S.Matrix([(Wp[k]+ee)/wp[k] for k in range(3)])
check('unique all-j target variation',vv-vp)
check('unique all-j target stable derivative',dd-dp)
pairs=[(6*j,-6*(j+1)),(3*j*(j+1),-21*j*(j+1)-6),(-6*j-6,6*j)]
for h,(mm,nn) in enumerate(pairs):
 check(f'all-j native left {h}',-(d[h]+v[h,h])/2-6-mm)
 check(f'all-j native right {h}',(d[h]-v[h,h])/2-nn)
sj=1-3*j*(j+1)
check('all-j staircase central update',sj.subs(j,j+1)-sj-pairs[0][1])
check('all-j adjacent central class',sj+pairs[1][1]-(-5-24*j*(j+1)))
res=[int((-5-24*j*(j+1)).subs(j,t))%28 for t in range(7)]
assert res==[23,3,19,15,19,3,23]
checks.append('seven exact adjacent residues')
result=dict(utc=datetime.now(timezone.utc).isoformat(),status='PASS',checks=len(checks),identities=checks,adjacent_residues=res,
 scope='Independent algebraic verification of the audited literal maps and induction. Geometric bundle, period-quotient and relative-return identifications are supplied in CF.1--5, K54 and K55, not inferred from this certificate alone.')
(ROOT/'code/part3_fourfold/source_cusp_mutation_peer_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
