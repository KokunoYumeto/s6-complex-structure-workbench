"""Exact Cox, full-unit, frame and polynomial identities for CF.1–5."""
from datetime import datetime,timezone
from pathlib import Path
import json
import sympy as S

root=Path(__file__).resolve().parents[2]
checks=[]
def ck(name,value):
    assert bool(value),name
    checks.append(name)
def equal(x,y):
    if isinstance(x,S.MatrixBase):
        return all(S.simplify(t)==0 for t in x-y)
    return S.simplify(x-y)==0

a,b,c,q,Z,V=S.symbols('a b c q Z V',nonzero=True)
A11,A12,A21,A22=S.symbols('A11 A12 A21 A22',nonzero=True)
A=S.Matrix([[A11,A12],[A21,A22]])
Q=[S.Matrix([[1,-1],[0,1]]),S.Matrix([[1,0],[-1,1]]),S.Matrix([[1,1],[0,1]])]
tables=[
S.Matrix([[A11*A21,A12*A22/(A11*A21)],[A21,A22/A21]]),
S.Matrix([[A11/A12,A12],[A11*A21/(A12*A22),A12*A22]]),
S.Matrix([[A11/A21,A11*A12/(A21*A22)],[A21,A21*A22]])]
newchars=[(Z*V,V),(Z,Z*V),(Z/V,V)]
newfirst=[S.Matrix([a/c,b*c,c]),S.Matrix([a/b,b,b*c]),S.Matrix([a*c,b/c,c])]
oldnative=[(b,a,c),(c,a,b),(a,b,c)]
selected=[2,2,0]
xi,ups=S.symbols('xi ups',integer=True)
weights=S.Matrix([-xi-ups,xi,ups])
for k in range(3):
    ck(f'integral inverse Q{k}',Q[k].det()==1 and all(t.q==1 for t in Q[k].inv()))
    R=Q[k].inv()
    AA=S.zeros(2)
    for i in range(2):
        for j in range(2):
            value=S.Integer(1)
            for h in range(2):
                for z in range(2):
                    value*=A[h,z]**(R[i,h]*Q[k][z,j])
            AA[i,j]=S.factor(value)
            ck(f'full unit matrix Q{k} entry{i}{j}',equal(AA[i,j],tables[k][i,j]))
    for j in range(2):
        p,r=Q[k][:,j]
        zz=q**p*A11**p*A12**r*Z
        vv=q**r*A21**p*A22**r*V
        for i in range(2):
            value=zz**R[i,0]*vv**R[i,1]
            expected=q**(1 if i==j else 0)*tables[k][i,j]*newchars[k][i]
            ck(f'complete period and height square Q{k} i{i}j{j}',equal(value,expected))
    newZ,newV=newchars[k]
    aa=(q/(newZ*newV)).subs({q:a*b*c,Z:b,V:c},simultaneous=True)
    bb=newZ.subs({Z:b,V:c},simultaneous=True)
    cc=newV.subs({Z:b,V:c},simultaneous=True)
    ck(f'actual first triangle Q{k}',equal(S.Matrix([aa,bb,cc]),newfirst[k]))
    ck(f'physical height Q{k}',equal(aa*bb*cc,a*b*c))
    z,n0,n1=oldnative[k]
    native=S.Matrix([n0/n1,z*n1,n1])
    if k==1:native=S.Matrix([native[0],native[2],native[1]])
    first=newfirst[k]
    actual=S.Matrix([first[0],first[1],first[2]]) if selected[k]==2 else S.Matrix([first[1],first[0],first[2]])
    ck(f'literal native other-ruling chart Q{k}',equal(native,actual))
    second=S.Matrix([n1/n0,z*n0,n0])
    if k==1:second=S.Matrix([second[0],second[2],second[1]])
    ck(f'native second base Q{k}',equal(second[0]*native[0],1))
    ck(f'native second normals Q{k}',equal(second[1:,0],native[0]*native[1:,0]))
    neww=R*S.Matrix([xi,ups])
    expectedweights=S.Matrix([-neww[0]-neww[1],neww[0],neww[1]])
    actualweights=[]
    for monomial in first:
        powers=monomial.as_powers_dict()
        actualweights.append(sum(powers.get(var,0)*weights[i] for i,var in enumerate((a,b,c))))
    ck(f'physical circle character Q{k}',equal(S.Matrix(actualweights),expectedweights))
# Explicit full-unit second native chart in the third case.
u,v,w=A11*b,a*b/A21,A21*c/(A11*b)
Apr=tables[2]
native2=S.Matrix([Apr[0,0]*w,Apr[1,0]*v,u/(Apr[0,0]*Apr[1,0])])
ck('complete-unit second C0 chart in Q2',equal(native2,S.Matrix([c/b,a*b,b])))
t=S.symbols('t',real=True)
phase=S.exp(S.I*S.pi*t)
U=S.Matrix([[1+phase,1-phase],[1-phase,1+phase]])/2
ck('explicit constant U2 normal-interchange path',equal(S.conjugate(U.T)*U,S.eye(2)))
ck('normal interchange path starts at identity',U.subs(t,0)==S.eye(2))
ck('normal interchange path ends at swap',U.subs(t,1)==S.Matrix([[0,1],[1,0]]))
m,n=S.symbols('m n',integer=True)
aa=-(m+n);bb=2*n+aa
newm,newn=m+2*n,-n
ck('selected variation after actual native reset',equal(-(newm+newn),aa))
ck('selected ambient derivative after native reset',equal(2*newn-(newm+newn),2*aa-bb))

j=S.symbols('j',integer=True,nonnegative=True)
P=S.Matrix([[1,-j],[0,1]])
B=-6*P.inv()*S.Matrix([1,0])*S.Matrix([[1,0]])*P
ck('literal staircase winding matrix',B==S.Matrix([[-6,6*j],[0,0]]))
l=S.Matrix([0,-6*(j+1),0])
ww=S.Matrix([j,1,-j-1]);dd=S.Matrix([-j-2,-2*j-1,j-1])
II=S.Matrix([-3*ww[i]+dd[i]*(l[i]+3) for i in range(3)])
WW=S.Matrix([-3*ww[i]-dd[i]*(l[i]+3) for i in range(3)])
ck('all staircase orbit traces',equal(II,S.Matrix([-6*(j+1),12*j*(j+1),6*j])))
ck('all staircase derivative traces',equal(WW,S.Matrix([6,-12*j*(j+1)-6,6])))
VM=S.Matrix([[0,6*(j+1),-6],[6*(j+1),18*j*(j+1),-6*j],[-6,-6*j,0]])
dv=S.Matrix([-12*(j+1),-24*j*(j+1)-12,12*j])
nativepairs=[(6*j,-6*(j+1)),(3*j*(j+1),-21*j*(j+1)-6),(-6*j-6,6*j)]
for i in range(3):
    ck(f'staircase native pair{i}',equal(-(dv[i]+VM[i,i])/2-6,nativepairs[i][0])
       and equal((dv[i]-VM[i,i])/2,nativepairs[i][1]))
ck('literal adjacent fan matrix',P*Q[1]==S.Matrix([[j+1,-j],[-1,1]]))
sequence=[int((-5-24*k*(k+1))%28) for k in range(7)]
ck('complete adjacent range',sequence==[23,3,19,15,19,3,23])
ck('period seven polynomial',equal((-5-24*(j+7)*(j+8))-(-5-24*j*(j+1)),-28*(12*j+48)))
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','check_count':len(checks),
     'checks':checks,'adjacent_period':7,'adjacent_range':sorted(set(sequence)),
     'scope':'Exact identities used by the written Cox/period/native-frame proof and the full induction; no general product reset inferred.'}
(root/'code/part3_root/source_cusp_mutation_exact.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS',len(checks),'exact Cox/unit/frame/induction identities')

