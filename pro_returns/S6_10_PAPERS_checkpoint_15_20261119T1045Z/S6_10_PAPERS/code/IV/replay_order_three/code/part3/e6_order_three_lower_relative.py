"""Integral boundary-gauge and relative normal arithmetic for the actual I3 domain."""
from pathlib import Path
import sympy as S,json,hashlib,datetime
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
ROOT=Path(__file__).resolve().parents[2]
proof=ROOT/'notes/part3_e6_order_three_lower_relative_working.md'
checks=[]
def ck(label,v):
    assert bool(v),label
    checks.append(label)
# Boundary abelianization in the actual (a,b,alpha) order.
boundary_relation=S.Matrix([[3,0,0]])
source_relations=S.Matrix([[1,0,0],[0,0,1]])
ck('boundary relation is exactly3a',smith_normal_form(boundary_relation,domain=ZZ)==boundary_relation)
ck('boundary integral free H1 has rank2',3-boundary_relation.rank()==2)
ck('source inclusion kills a andalpha only',source_relations.rank()==2 and source_relations*S.Matrix([0,1,0])==S.zeros(2,1))
ck('source integral H1 generator b primitive',source_relations[:,[0,2]].det()==1)
# H1 integral dual has no torsion class; source dual b*, quotient isalpha*.
bdual=S.Matrix([0,1,0]);alphadual=S.Matrix([0,0,1])
ck('both literal boundary circle maps kill3a',boundary_relation*bdual==S.zeros(1,1) and boundary_relation*alphadual==S.zeros(1,1))
ck('alpha remains primitive after source b gauge',S.Matrix.hstack(bdual,alphadual)[1:3,:].det()==1)
I=S.Matrix([[-2,1,1],[1,-2,1],[1,1,-2]])
F=S.ones(3,1);D=S.Matrix([3,2,4])
ck('actual whole fibre radical',I*F==S.zeros(3,1))
ck('actual retained point divisor square',(D.T*I*D)[0]==-6)
ck('full point divisor fibre intersection zero',(D.T*I*F)[0]==0)
n,m=S.symbols('n m',integer=True)
plus=D+n*F;minus=-D+m*F
ck('retained boundary winding preserves plus square',S.expand((plus.T*I*plus)[0])==-6)
ck('retained boundary winding preserves minus square',S.expand((minus.T*I*minus)[0])==-6)
ck('retained two boundary windings preserve mixed pairing',S.expand((plus.T*I*minus)[0])==6)
# Reference orientation is reversed in collision-minus-reference.
c11,c12,c22=S.Integer(6),S.Integer(-6),S.Integer(6)
w1,w2=S.Integer(1),S.Integer(-1);P=w1*w2
p1=S.Integer(-27)
B=c11/w1**2+c12/P+c22/w2**2
kU=B/P
ellU=(p1-c11-c22-2*(w1/w2+w2/w1)*c12+(w1*w1+w2*w2)*B)/P
ck('actual positive-hyperplane relative pair',(kU,ellU)==(-18,27))
ck('actual physical dual relative pair',(-kU,-ellU)==(18,-27))
out={'status':'PASS','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'checks':len(checks),'check_labels':checks,'source_sha256':hashlib.sha256(proof.read_bytes()).hexdigest(),'boundary_relation':[[3,0,0]],'source_H1_inclusion':[0,1,0],'I3_intersection':I.tolist(),'whole_fibre':[1,1,1],'point_divisor':[3,2,4],'normal_pairings_on_collision_minus_reference':[6,-6,6],'relative_tangent_p1':-27,'physical_relative_pair_per_lower_surface':[18,-27],'scope':'Exact integral source/boundary gauge calculation and scoped lower/reference fixed-surface pair. Outer selected-tube/Jin arrow and total source return are not assigned.'}
(ROOT/'code/part3/e6_order_three_lower_relative.json').write_text(json.dumps(out,indent=2,default=int)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ['check_labels']},indent=2,default=int))
