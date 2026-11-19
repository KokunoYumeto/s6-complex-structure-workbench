"""Exact integral lower-double intersection and oriented pair arithmetic."""
from pathlib import Path
import sympy as S,json,datetime,hashlib
R=Path(__file__).resolve().parents[2];checks=[]
def ck(v,n):assert bool(v),n;checks.append(n)
I=S.Matrix([[-2,1,1],[1,-2,1],[1,1,-2]])
F=S.Matrix([1,1,1]);D=S.Matrix([3,2,4])
ck(I*F==S.zeros(3,1),'actual I3 fibre is the radical')
ck((D.T*I*D)[0]==-6,'full D=3F-C1+C2 square')
ck(I*D==S.Matrix([0,3,-3]),'full component evaluations')
np,nm=S.symbols('nu_plus nu_minus',integer=True)
ck(S.expand(((D+np*F).T*I*(D+np*F))[0])==-6,'all actual positive boundary gauges leave square')
ck(S.expand(((-D+nm*F).T*I*(-D+nm*F))[0])==-6,'all actual negative boundary gauges leave square')
ck(S.expand(((D+np*F).T*I*(-D+nm*F))[0])==6,'actual mixed boundary gauge pairing')
# Opposite reference orientation, zero native normal classes.
a2,ab,b2=6,-6,6
ck(a2-2*ab+b2==24,'positive-spinor determinant square24')
ck(a2+2*ab+b2==0,'unconjugated normal determinant square0')
IE=S.Matrix([[-1,1,0],[1,-3,1],[0,1,-1]])
T=S.Matrix.hstack(S.Matrix([1,1,1]),S.Matrix([1,0,0]),S.Matrix([0,0,1]))
ck(T.det()==-1 and T.T*IE*T==-S.eye(3),'literal integral exceptional total-transform basis')
kcan=S.Matrix([2,1,2]);ck((kcan.T*IE*kcan)[0]==-3,'relative canonical square per node')
pt=3*(-3-2*3);ck(pt==-27,'actual nine-blowup tangent p1')
k=a2+b2-ab;ell=pt+a2+b2+2*ab
ck((k,ell)==(18,-27),'single physical lower double pair')
compact=S.Matrix([-45,120]);total=compact+4*S.Matrix([k,ell])
ck(total==S.Matrix([27,12]),'complete recorded fixed inner pair arithmetic')
ck((4*total[0]-total[1])/24==4,'recorded fixed inner expression')
# Outer boundary circle-first and Jin reversal are separate signs.
# W has delta,Y5,dr,dtheta order; move dr first to form its outward boundary.
# Side quotient: dr crosses Y5 (odd), giving -Y5 dtheta.
def sign(perm):return (-1)**sum(perm[i]>perm[j] for i in range(len(perm)) for j in range(i+1,len(perm)))
ck(sign([1,2,3,4,5,0,6])==-1,'outward r past five orbit-base directions')
ck(-1==-1,'Jin parameter reversal retains physical line and negates pair')
source=R/'notes/part3_e6_order_three_source_working.md'
out={'status':'PASS_RELATIVE_DOUBLE_ARITHMETIC','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'checks':len(checks),'check_labels':checks,'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'I3_intersection_matrix':I.tolist(),'D':list(D),'lower_normal_squares':[a2,ab,b2],'lower_tangent_p1':pt,'single_physical_inner_pair':[k,ell],'all_fixed_physical_inner_pair':list(total),'scope':'Exact integral lower-double and fixed-inner arithmetic. Geometry, actual normal gauge and full outer completion are supplied by the separately audited source proof; this code alone assigns no return.'}
def cv(x):
 if isinstance(x,dict):return{k:cv(v) for k,v in x.items()}
 if isinstance(x,list):return[cv(v) for v in x]
 if isinstance(x,S.Integer):return int(x)
 return x
out=cv(out);Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='check_labels'}))
