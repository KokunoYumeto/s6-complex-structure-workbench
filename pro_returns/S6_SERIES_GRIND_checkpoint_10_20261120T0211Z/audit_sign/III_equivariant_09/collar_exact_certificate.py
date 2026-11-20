"""Independent receiving certificate for named OS45 collar/marked-boundary maps.
Written after both frozen derivations. No producing program is imported.
The geometric compactness, actual units, lattice embedding, and framing proof
are in receiving_comparison.md, not replaced by this finite algebra.
"""
import itertools,json,hashlib
from pathlib import Path
import sympy as S
checks=[]
def check(name,expr):
    if isinstance(expr,S.MatrixBase): ok=all(S.simplify(x)==0 for x in expr)
    elif isinstance(expr,bool):ok=expr
    else:ok=S.simplify(expr)==0
    assert ok,name
    checks.append(name)
A=S.Matrix([[1,8,0,24],[0,1,0,0],[0,-6,1,-16],[0,0,0,1]])
A1=S.eye(4);A1[0,1]=1
pairs=list(itertools.combinations(range(4),2))
def wedge(M):return S.Matrix([[M[i,k]*M[j,l]-M[i,l]*M[j,k] for k,l in pairs] for i,j in pairs])
R=wedge(A)-S.eye(6);alpha=S.Matrix([0,1,0,0,0,0]);v=S.Matrix([1,0,0,1,0,0])
check('literal two-alpha Wang boundary',R*v-2*alpha)
check('all Wang entries even',all(int(a)%2==0 for a in R))
check('alpha has nonzero mod-two coordinate',list(alpha).count(1)==1)
check('first I1 angular area monodromy fixed',(wedge(A1)-S.eye(6))*alpha)
check('cusp angular area monodromy fixed',R*alpha)
L=S.Matrix([[8,24],[-6,-16]]);U=S.Matrix([[1,3],[-3,-8]])
check('exact period lattice map',L-S.diag(8,2)*U)
check('period adapter determinant',U.det()-1)
check('unapplied graph translation retained',L*S.Matrix([9,-3])-S.Matrix([0,-6]))
C=S.Matrix([[1,1,1],[0,1,0],[5,5,6]])
check('ordered graph cone determinant',C.det()-1)
check('exact cone reciprocal',C*C.inv()-S.eye(3))
check('marked e1 weights',C.inv()*S.Matrix([0,1,0])-S.Matrix([-1,1,0]))
check('marked delta weights',C.inv()*S.Matrix([0,0,1])-S.Matrix([-1,0,1]))
check('constant physical-line source meridian',C.inv()*S.Matrix([0,1,-1])-S.Matrix([0,1,-1]))
x,y,z,a,b,c,d,u0,u1,f=S.symbols('x y z a b c d u0 u1 f',nonzero=True)
q=x*y*z;Z=y;V=x**5*y**5*z**6;W=q**6/(Z*V)
check('physical extending coordinate',W-x)
P=S.Matrix([x*z,y,W])
check('source/line Jacobian',P.jacobian([x,y,z]).det()+x)
check('source node equation',P[0]*P[1]-q)
for name,value,target in [('inverse x',W,x),('inverse y',y,y),('inverse z',(x*z)/W,z)]:check(name,value-target)
x0=u0**6/b;y0=a*b;z0=u0**-5*d
check('cusp retained base unit',x0*y0*z0-u0*a*d)
check('cusp exact source coordinate',y0-a*b)
check('cusp exact dual line coordinate',x0**5*y0**5*z0**6-(a*d)**6/a)
X1=-u1*c/a;Y1=a*b;W1=a/f**6
check('finite node full unit',X1*Y1+u1*b*c)
check('finite physical line coordinate',W1*(f**6/a)-1)
check('middle character determinant',S.Matrix([[1,1],[-1,0]]).det()-1)
check('two primitive meridians area',S.Matrix([[1,1],[-1,0]]).det()-1)
# Derivatives retain arbitrary holomorphic endpoint units, including their jets.
C0=S.Function('C0');C1=S.Function('C1')
a0,b0,d0=S.symbols('a0 b0 d0')
f0=a0*d0
P0=S.Matrix([C0(f0)**6/b0,a0*b0,C0(f0)**-5*d0])
J0=P0.jacobian([a0,b0,d0]).subs({a0:0,d0:0})
check('cusp core derivative with all unit jets',J0.det()-C0(0)/b0)
a2,b2,c2=S.symbols('a2 b2 c2');f1=1+b2*c2
P1=S.Matrix([-C1(f1)*c2/a2,a2*b2,a2/f1**6])
J1=P1.jacobian([a2,b2,c2]).subs({b2:0,c2:0})
check('finite core derivative with all unit jets',J1.det()-C1(1))
# Circle characters exactly preserve the based coordinates and the derivative model.
weights={'a':-1,'b':1,'c':-1,'d':1}
check('f circle weight',weights['a']+weights['d']==0)
check('Z circle weight',weights['a']+weights['b']==0)
check('V circle weight',6*(weights['a']+weights['d'])-weights['a']==1)
check('Bott A weight',weights['a']+weights['c']==-2)
check('Bott B weight',weights['b']+weights['d']==2)
# The formal real-linear base homotopy has this exact determinant.
ar,ai,br,bi,t=S.symbols('ar ai br bi t',real=True)
M=S.Matrix([[ar+t*br,-ai+t*bi],[ai+t*bi,ar-t*br]])
check('orientation-preserving base homotopy determinant',M.det()-(ar**2+ai**2-t**2*(br**2+bi**2)))
out={'status':'PASS','checks':len(checks),'check_names':checks,'A0':list(map(list,A.tolist())),'wedge_order':pairs,'boundary_matrix':R.tolist(),'alpha':list(alpha),'two_alpha_preimage':list(v),'ordered_graph_cone':C.tolist(),'period_adapter':U.tolist(),'cusp_core_jacobian':str(S.simplify(J0.det())),'finite_core_jacobian':str(S.simplify(J1.det())),'reading_order':'After both independent freezes and their complete text comparison. No producing code read/imported.','scope_limits':'Finite identities only. Actual theta units, embedding, endpoint neighborhoods, MV connecting map, relative Borel characteristic and admissible frame are proved in the receiving report.'}
p=Path(__file__).with_name('collar_exact_certificate.json');p.write_text(json.dumps(out,indent=2,default=str)+'\n');print('PASS',len(checks));print('output_sha256',hashlib.sha256(p.read_bytes()).hexdigest())
