"""Exact source-zero vertical-fan recurrence in the actual doubled products."""
from pathlib import Path
from datetime import datetime,timezone
import sympy as s
import json,math

root=Path(__file__).resolve().parents[2]
j,N,b=s.symbols('j N b',integer=True);a=3-b
P=s.Matrix([[1,0],[j,1]])
W=s.Matrix([[1,b],[-a,N-2]])
B=2*P.inv()*W*P
ell=[B[1,1]-B[1,0],B[0,0]-B[0,1],B[1,1]]
t=N-1;weights=[0,1,-1];normal=[-2,-1,-1]
I=[t*weights[i]+normal[i]*(ell[i]-t) for i in range(3)]
D=[t*weights[i]-normal[i]*(ell[i]-t) for i in range(3)]
checks=[]
def ck(name,left,right):
    assert s.factor(left-right)==0,name
    checks.append(name)
ck('actual half trace',s.trace(B)/2,t)
ck('l0',ell[0],2*(N+a-2+(3-N-b)*j+b*j*j))
ck('l1',ell[1],2*(1+b*(j-1)))
ck('l2',ell[2],2*(N-2-b*j))
V11=I[1];delta1=D[1]-D[0]
ck('nonfixed orbit prism',V11,2*t-ell[1])
ck('nonfixed derivative prism',delta1,ell[1]-2*ell[0]+2*t)
right=s.factor((delta1-V11)/4)
ck('actual single right integer',right,-N+(N+2*b-3)*j-b*j*j)
ck('right via normal entries',right,(ell[1]-ell[0])/2)
choose2=lambda z:z*(z-1)/2
choose3=lambda z:z*(z-1)*(z-2)/6
F=2*b*choose3(j+1)+(3-b)*choose2(j+1)-N*choose2(j)
ck('initial fan',F.subs(j,0),0)
ck('exact full recurrence',F.subs(j,j-1)-F,right)
ck('known reflected diagonal comparison',F.subs(j,1),a)
ck('reduced closed polynomial',F.subs(b,1),2*choose3(j+2)-N*choose2(j))
ck('good relative polynomial',F.subs(b,2),j*(j+1)*(4*j-1)/6-N*choose2(j))

# Native C1 charts include the complete period units.
x,y,z,g,eta,A,DD=s.symbols('x y z g eta A DD',nonzero=True)
u=g*eta*y*z;v=1/(eta*z);w=x*z/g
ck('full native source inverse',eta*v,1/z)
ck('full native first normal',g*w,z*x)
ck('full native second normal',u/(g*eta),z*y)
ck('full target height',u*v*w,x*y*z)
ck('C1 seam height',DD*(A*DD)**-1*A,1)
ck('actual Q1 vertical step',(P*s.Matrix([[1,0],[-1,1]]))[1,0],j-1)

# Exhaustively check the integer polynomial on a stated finite rectangle.
cases=0;examples=[]
for aa,bb in [(1,2),(2,1)]:
  for p in range(1,8):
    m=4*p if aa==1 else 4*p-1
    for k in range(0,6):
      nn=k*m
      for jj in range(-40,41):
        val=s.factor(F.subs({b:bb,N:nn,j:jj}))
        rr=s.factor(right.subs({b:bb,N:nn,j:jj}))
        assert val.is_Integer and rr.is_Integer
        prev=s.factor(F.subs({b:bb,N:nn,j:jj-1}))
        assert prev-val==rr
        cases+=1
for jj in range(-4,7):
    relative=int(F.subs({b:1,N:0,j:jj}))
    rescaled=2+int(F.subs({b:1,N:3,j:jj}))
    examples.append({'vertical_index':jj,'a2_fixed_scalar_integer':relative,
                     'a2_fixed_scalar_mod28':relative%28,
                     'a2_p1_k1_integer':rescaled,'a2_p1_k1_mod28':rescaled%28})
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS',
 'symbolic_checks':len(checks),'identities':checks,'integer_rectangle_checks':cases,
 'bounds':{'branches':[[1,2],[2,1]],'p':[1,7],'k':[0,5],'j':[-40,40]},
 'right_integer':str(right),'relative_polynomial':str(s.factor(F)),
 'examples':examples,'scope':'Exact full-period vertical-fan C1 recurrence. Absolute reduced values use K80; no good-branch absolute value or nonvertical fixed-star invariant is inferred.'}
(root/'code/part3_root/source_zero_vertical_fans.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
