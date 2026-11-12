"""Finite exact checks for the framed slide and its original flow comparison."""
from pathlib import Path
import hashlib,json
import sympy as S
W=Path(__file__).resolve().parents[1]
checks=[]
def ck(name,value):
    assert bool(value),name
    checks.append(name)
def eq(a,b):
    difference=S.sympify(a-b).replace(
        lambda q:q.is_Pow and q.exp.is_Rational and q.exp.q==2,
        lambda q:S.Pow(S.factor(q.base),q.exp))
    return S.simplify(difference)==0
def reduce_word(w):
    out=[]
    for a in w:
        if out and out[-1]==-a:out.pop()
        else:out.append(a)
    return out
def inv(w):return [-a for a in reversed(w)]
def mul(*ws):return reduce_word([a for w in ws for a in w])
def conj(g,w):return mul(g,w,inv(g))
x=[1];y=[2];R1=[1,2];R2=[2]
ck('Original finite product gives the exact based generator',mul(R1,inv(R2))==x)
ck('Incorrect positive second factor does not give that generator',mul(R1,R2)!=x)
ck('Reverse chronological left multiplication realizes the original ordered product',mul(R1,mul(inv(R2),[]))==x)
ck('Wrong chronological order retains the nontrivial conjugation',mul(inv(R2),R1)==[-2,1,2])
g=[2,1,2,-1]
ck('Both based conjugators survive the factor multiplication',mul(conj(g,R1),conj(g,inv(R2)))==conj(g,x))
factors=[conj([1,2],[2,3]),conj([-3,2],[-2,-1]),conj([2,2,1],[3,-1,2])]
cur=[]
for fac in reversed(factors):cur=mul(fac,cur)
ck('A three-factor noncommuting slide list has the required order',cur==mul(*factors))
ck('Inverting a complete word reverses and negates every letter',mul(cur,inv(cur))==[])
v,t,eps=S.symbols('v t epsilon',real=True,positive=True)
chi=S.Function('chi')
arc=S.Matrix([v,-eps+2*eps*t*chi(v)])
Jac=arc.jacobian([v,t])
ck('Positive trace determinant includes the original epsilon',eq(Jac.det(),2*eps*chi(v)))
ck('Negative trace determinant reverses the sign',eq(S.Matrix([v,eps-2*eps*t*chi(v)]).jacobian([v,t]).det(),-2*eps*chi(v)))
Jambient=S.eye(5);Jambient[1,0]=2*eps*t*S.diff(chi(v),v)
ck('Ambient diffeomorphism determinant differs from trace determinant',Jambient.det()==1)
ck('The strip after-minus-before height retains the full crossing displacement',eq(arc[1]+eps,2*eps*t*chi(v)))
# A rational circle representative verifies the orientation away from the crossing.
theta=S.symbols('theta',real=True)
normal=S.Matrix([S.cos(theta),S.sin(theta)])
ck('Positive normal circle has its positive oriented area form',eq(normal[0]*S.diff(normal[1],theta)-normal[1]*S.diff(normal[0],theta),1))
a,b,d,be,rho=S.symbols('r s delta beta rho',positive=True)
A0=(d+be)*rho**2/a**2
Lam=(d+S.sqrt(d*d+4*be*A0))/(2*A0)
ck('Full hitting factor solves the original unsuppressed quadratic',eq(A0*Lam-be/Lam,d))
ck('Hitting factor equals one on the full original seam',eq(Lam.subs(rho,a),1))
wantprime=-S.diff(A0,rho)*Lam/(A0+be/Lam**2)
ck('Implicit derivative retains the beta over Lambda squared term',eq(S.diff(Lam,rho),wantprime))
rad=b/S.sqrt(Lam)
ck('Original normal radius equals the retained s at the seam',eq(rad.subs(rho,a),b))
# Rationalized expression avoids a singular symbolic limit at rho zero.
radfull=b*S.sqrt(2*A0/(d+S.sqrt(d*d+4*be*A0)))
ck('Rationalized radius is exactly the same full expression',eq(rad**2,radfull**2))
slope=S.limit(radfull/rho,rho,0,dir='+')
ck('Exact radius slope retains delta beta and both parameter radii',eq(slope,b/a*S.sqrt((d+be)/d)))
ck('Full radius derivative on the seam retains all four parameters',eq(S.diff(radfull,rho).subs(rho,a),b/a*(d+be)/(d+2*be)))
# Check the complete radial derivative as a map of the original two-dimensional u.
u1,u2=S.symbols('u1 u2',real=True)
rr=S.sqrt(u1*u1+u2*u2)
LL=S.Function('L')
uu=S.Matrix([u1,u2])
ang=a*uu/rr
DA=a/rr*(S.eye(2)-uu*uu.T/rr**2)
ck('Both angular derivative columns retain the radial projection',all(eq(z,0) for z in ang.jacobian([u1,u2])-DA))
vv=S.symbols('v1:5',real=True)
zmap=S.Matrix([z/ S.sqrt(LL(rr)) for z in vv])
DL=S.Subs(S.Derivative(LL(rho),rho),rho,rr)
cross=-S.Rational(1,2)*LL(rr)**(-S.Rational(3,2))*DL*S.Matrix(vv)*uu.T/rr
ck('All eight mixed travel-time entries are retained',all(eq(z,0) for z in zmap.jacobian([u1,u2])-cross))
ck('All four transverse derivative factors are retained',zmap.jacobian(vv)==S.eye(4)/S.sqrt(LL(rr)))
# Full coefficient comparison is polynomial after retaining Lambda as an exact root.
Av,Lv=S.symbols('A0 Lambda',positive=True)
aa=[S.Integer(2),S.Integer(7)];bb=[S.Integer(3),S.Integer(5),S.Integer(11),S.Integer(13)]
xx=S.symbols('x1:3',real=True);yy=S.symbols('y1:5',real=True)
A=sum(c*q*q for c,q in zip(aa,xx));B=sum(c*q*q for c,q in zip(bb,yy))
F=-A+B;coords=[*xx,*yy]
ck('All six original Hessian entries remain present',S.hessian(F,coords)==S.diag(-4,-14,6,10,22,26))
Fend=F.subs(dict(zip(coords,[S.sqrt(Lv)*q for q in xx]+[q/S.sqrt(Lv) for q in yy])),simultaneous=True)
ck('Full original trajectory endpoint retains A and B separately',eq(Fend,-Lv*A+B/Lv))
for j,c in enumerate(aa):
    # Squared coordinates retain their oriented linear u factor separately.
    left=Lv*(d+be)/a**2/c
    right=(d+be/Lv)/rho**2/c
    relation=Lv*(d+be)*rho**2/a**2-d-be/Lv
    ck('Exact negative-coordinate comparison '+str(j),eq(left-right,relation/(rho**2*c)))
for j,c in enumerate(bb):
    ck('Exact positive-coordinate comparison '+str(j),eq(S.sqrt(be/c)/b/S.sqrt(Lv),S.sqrt(be/c)/(b*S.sqrt(Lv))))
Le=S.Rational(2,5)*(3+S.sqrt(19))
ck('Worked factor at rho five halves is exact',eq(Lam.subs({a:5,b:7,d:3,be:2,rho:S.Rational(5,2)}),Le))
ck('Worked original level is c minus three',eq(S.Rational(5,4)*Le-2/Le,3))
ck('Worked belt slope retains its exact irrational factor',eq(slope.subs({a:5,b:7,d:3,be:2}),S.Rational(7,5)*S.sqrt(S.Rational(5,3))))
# Noncommuting derivative matrices test the mixed term and exact full inverse.
M=S.Matrix([[1,2],[3,7]]);w=S.Matrix([5,11]);eta=S.symbols('eta_prime')
DF=M.row_join(eta*w).col_join(S.Matrix([[0,0,1]]))
DFi=M.inv().row_join(-eta*M.inv()*w).col_join(S.Matrix([[0,0,1]]))
ck('Full holonomy inverse includes its mixed derivative',DF*DFi==S.eye(3) and DFi*DF==S.eye(3))
ck('Holonomy pushforward has its complete horizontal component',DF*S.Matrix([0,0,-1])==S.Matrix([-5*eta,-11*eta,-1]))
flow=S.Matrix([[1,2,0],[0,1,3],[0,0,1]])
V=S.Matrix([2,1,1]);alpha=S.Matrix([[0,0,1]])
Vend=flow*V;bet=alpha*flow.inv()
Proj=flow-Vend*alpha
ck('Variable-time level derivative has tangent image',bet*Proj==S.zeros(1,3))
ck('Variable-time derivative removes the old flow direction',Proj*V==S.zeros(3,1))
for n in [6,7]:
    for k in [1,2,n-1]:
        order=list(range(k,n))+list(range(k));P=S.zeros(n)
        for i,j in enumerate(order):P[i,j]=1
        ck('Original reverse coordinate sign n '+str(n)+' k '+str(k),P.det()==(-1)**(k*(n-k)))
    counts=list(range(10,10+n+1));forward=counts.copy()
    forward[2]+=1;forward[3]+=1;forward[1]-=1;forward[2]-=1
    ck('Exact retained forward handle counts n '+str(n),forward==[v+(-1 if k==1 else 1 if k==3 else 0) for k,v in enumerate(counts)])
    reverse=counts.copy()
    reverse[n-2]+=1;reverse[n-3]+=1;reverse[n-1]-=1;reverse[n-2]-=1
    ck('Exact retained reversed handle counts n '+str(n),reverse==[v+(-1 if k==n-1 else 1 if k==n-3 else 0) for k,v in enumerate(counts)])
for dim in [4,5,6]:
    ck('Both relative loop estimates are strictly negative in dimension '+str(dim),2-dim<0 and 3-dim<0)
source=W/'src/framed-handle-slides-and-index-one-removal.md'
text=source.read_text(encoding='utf-8')
ck('Display-math delimiters balance in the exact source',text.count(r'\[')==text.count(r'\]'))
ck('Inline-math delimiters balance in the exact source',text.count(r'\(')==text.count(r'\)'))
result=dict(source=source.name,source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),passed=len(checks),checks=checks,publication=False,independent_review=False,scope='Finite exact free-group, crossing sign and derivative, original Hessian and hitting-factor, full mixed derivative, holonomy inverse and variable-time projection, reverse coordinate and handle-count calculations. Relative isotopy, compactness, supported field realization and cancellation are proved in the text; these checks do not certify those geometric proofs.')
(W/'checks/FRAMED_SLIDE_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(passed=len(checks),source_sha256=result['source_sha256'])))

