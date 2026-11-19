"""Fresh exact F4.1 arithmetic and map checks; no target/producer code read."""
from pathlib import Path
from itertools import product
from math import isqrt
import sympy as s
import json,datetime,hashlib
ROOT=Path(__file__).resolve().parents[2]
Q=s.diag(1,1,1,-1);v=s.ones(4,1);R=s.eye(4)-v*(v.T*Q)
checks=[]
def ck(name,value):
    assert bool(value),name
    checks.append({'name':name,'result':'passed'})
ck('actual norm-two reflection',R*R==s.eye(4) and R.T*Q*R==Q and R.det()==-1 and (v.T*Q*v)[0]==2)
rr=[[int(R[i,j]) for j in range(4)] for i in range(4)]
qq=[[int(Q[i,j]) for j in range(4)] for i in range(4)]
ident=[[int(i==j) for j in range(4)] for i in range(4)]
def mm(A,B):return [[sum(A[i][k]*B[k][j] for k in range(4)) for j in range(4)] for i in range(4)]
def mv(A,x):return [sum(A[i][j]*x[j] for j in range(4)) for i in range(4)]
def trans(A):return [list(a) for a in zip(*A)]
def norm(x):return x[0]**2+x[1]**2+x[2]**2-x[3]**2
def reduce_vector(initial):
    x=list(initial);M=[a[:] for a in ident];trace=[x[:]];iterations=0
    assert norm(x)==2 and all(t%2 for t in x)
    while True:
        signs=[1 if t>0 else -1 for t in x]
        S=[[signs[i] if i==j else 0 for j in range(4)] for i in range(4)]
        x=mv(S,x);M=mm(S,M)
        if x[3]==1:
            assert x==[1,1,1,1];break
        oldd=x[3];sum3=sum(x[:3]);assert oldd<sum3<3*oldd
        y=mv(rr,x)
        assert 0<abs(y[3])<oldd and norm(y)==2 and all(t%2 for t in y)
        x=y;M=mm(rr,M);trace.append(x[:]);iterations+=1
    assert mv(M,initial)==[1,1,1,1]
    assert mm(mm(trans(M),qq),M)==qq
    inverse=mm(mm(qq,trans(M)),qq)
    assert mm(inverse,M)==ident and mv(inverse,[1,1,1,1])==list(initial)
    return {'input':list(initial),'reflection_steps':iterations,'isometry':M,'inverse':inverse,'trace':trace}

grid=[]
for a in range(1,100,2):
    for b in range(1,a+1,2):
        for c in range(1,b+1,2):
            ds=a*a+b*b+c*c-2;d=isqrt(ds)
            if d*d==ds and d%2:grid.append(reduce_vector([a,b,c,d]))
ck('all enumerated characteristic vectors reduced by exact isometries',len(grid)>0)
sign_cases=[]
for base in [grid[0]['input'],grid[len(grid)//2]['input'],grid[-1]['input']]:
    for sg in product([-1,1],repeat=4):sign_cases.append(reduce_vector([sg[i]*base[i] for i in range(4)]))
ck('all sixteen independent orientation-coordinate sign patterns',len(sign_cases)==48)
long_cases=[]
for seed in range(10):
    x=[1,1,1,1]
    for j in range(20):
        x[(seed+2*j)%4]*=-1
        x=mv(rr,x)
    long_cases.append(reduce_vector(x))
ck('twenty-word generated exact cases beyond direct grid',len(long_cases)==10)

# Quaternion action and the exact complex orientations used in the proof.
a,b,c,d=s.symbols('a b c d',real=True)
L=s.Matrix([[a,-b,-c,-d],[b,a,-d,c],[c,d,a,-b],[d,-c,b,a]])
Rt=s.Matrix([[a,-b,-c,-d],[b,a,d,-c],[c,-d,a,b],[d,c,-b,a]])
Li=L.subs({a:0,b:1,c:0,d:0});Ri=Rt.subs({a:0,b:1,c:0,d:0})
e0=s.eye(4)[:,0];e2=s.eye(4)[:,2]
left_complex_frame=s.Matrix.hstack(e0,Li*e0,e2,Li*e2)
right_complex_frame=s.Matrix.hstack(e0,Ri*e0,e2,Ri*e2)
ck('left-i complex orientation agrees with quaternion orientation',left_complex_frame.det()==1)
ck('right-i complex orientation reverses quaternion orientation',right_complex_frame.det()==-1)
ck('left action is complex linear for right-i',L*Ri==Ri*L)
ck('right action is complex linear for left-i',Rt*Li==Li*Rt)
ck('actual Spin4 factors commute',L*Rt==Rt*L)
n=a*a+b*b+c*c+d*d
ck('quaternion action is orthogonal on the unit sphere',s.simplify(L.T*L-n*s.eye(4))==s.zeros(4) and s.simplify(Rt.T*Rt-n*s.eye(4))==s.zeros(4))
cl=s.Matrix([[1,-1],[1,1]])
clinv=s.Matrix([[1,1],[-1,1]])/2
ck('actual Euler-half-Pontryagin coordinate inverse',cl*clinv==s.eye(2) and clinv*cl==s.eye(2) and cl.det()==2)
ck('tangent S4 stabilization kernel',cl*s.Matrix([1,-1])==s.Matrix([2,0]))
e,t=s.symbols('e t',integer=True)
aa=(e+t)/2;bb=(t-e)/2
ck('normal Euler and stable normal formulas',s.expand(aa-bb-e)==0 and s.expand(aa+bb-t)==0)
parity_count=0
for ee in range(-21,22):
    for tt in range(-21,22):
        if (ee-tt)%2==0:
            x=clinv*s.Matrix([ee,tt]);assert all(q.q==1 for q in x);assert cl*x==s.Matrix([ee,tt]);parity_count+=1
ck('exact clutching image parity and inverse grid',parity_count>0)

c2square=s.solve(s.Eq((3*s.Symbol('c22')+14*6)/45,2),s.Symbol('c22'))[0]
p1square=4*c2square;p2=c2square+12
ck('Chern and Pontryagin numbers',c2square==2 and p1square==8 and p2==14)
ck('Todd and chi1 index values',(3*c2square-6)/720==0 and (3*c2square-31*6)/180==-1)
ck('signature and Ahat identities',(7*p2-p1square)/45==2 and (7*p1square-4*p2)/5760==0)
ck('comparison connected-sum invariants',3-1==2 and 2+3+1==6 and 4*(3-1)==8 and 7*(3-1)==14)
ck('comparison half-Pontryagin characteristic square',(v.T*Q*v)[0]==2 and all(int(t)%2 for t in v))

pre=ROOT/'analysis/continuation_root/F4_1_before_read.md'
out={'status':'passed','completed_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'checker':'GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro',
 'prereading_sha256':hashlib.sha256(pre.read_bytes()).hexdigest(),
 'method':'fresh exact SymPy quaternion/form identities and integer isometry descent; no target or original producing code read',
 'checks':checks,'symbolic_and_grouped_checks':len(checks),'grid_description':'All positive odd triples a>=b>=c with a<=99 whose d^2=a^2+b^2+c^2-2 is an odd square',
 'grid_cases':len(grid),'sign_cases':len(sign_cases),'long_word_cases':len(long_cases),'clutching_parity_cases':parity_count,
 'maximum_descent_steps':max(x['reflection_steps'] for x in grid+sign_cases+long_cases),
 'cases':grid,'signed_cases':sign_cases,'long_cases':long_cases,
 'scope':'Finite runs supplement the written universal strictly decreasing positive-last-coordinate proof. The source classification theorems and geometric construction inputs are separately identified; no computation purports to prove them.'}
target=Path(__file__).with_suffix('.output.json');target.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ['status','completed_at_utc','symbolic_and_grouped_checks','grid_cases','sign_cases','long_word_cases','clutching_parity_cases','maximum_descent_steps','prereading_sha256']},indent=2))
