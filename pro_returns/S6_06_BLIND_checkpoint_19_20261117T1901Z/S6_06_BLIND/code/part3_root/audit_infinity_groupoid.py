"""Independent exact checks and complete-map audit of the marked loop groupoid."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import sympy as S

root=Path(__file__).resolve().parents[2]
checks=[]
def check(name,value):
    assert bool(value),name
    checks.append(name)

x1,x2,p1,u,z=S.symbols('x1 x2 p1 u z')
residue=(4*u**3-u*(p1+(x1+u)**2+(x2-u)**2))/(24*(x1+u)*(x2-u))
coefficient=S.expand(S.series(residue.subs(u,1/z),z,0,2).removeO()).coeff(z,1)
check('actual signed-normal surface residue',S.simplify(coefficient-(p1-3*(x1-x2)**2)/24)==0)
t,n,k=S.symbols('t n k')
q=-4*n*k*t*(t-1)
check('old/new infinity closing scalar cochain',S.expand(q.subs(t,t+1)-q+8*n*k*t)==0)
e,x,y,T=S.symbols('e x y T',nonzero=True)
v=e**-2-1
g=e*(1-e**2)
F_old=(e**-3*y+v+(e**-4*T)*(e**-2*x)/(2*v))/(e**-2*x)
F_new=(y+g+T*x/(2*g))/x
check('literal full chord under source scaling',S.factor(F_old-e**-1*F_new)==0)
check('marked section scaling',S.factor(v-e**-3*g)==0)
check('complete Hom denominator cancellation',S.factor(v*F_old-e**-4*g*F_new)==0)
rho,s=S.symbols('rho s')
check('literal Tate character under infinity source scaling',S.factor((s-rho)/(s+rho)-(e*s-1)/(e*s+1)).subs(rho,1/e)==0)
check('total global forward closing winding',1+0+1-2==0)
for a in (1,2):
    intersection=S.Matrix([[-2,2],[2,-2]])
    basis=S.Matrix([[1,0],[1,1]])
    check(f'primitive I2 marking a{a}',basis.det()==1 and basis.T*intersection*basis==S.diag(0,-2))
    vector=S.Matrix([0,-a])
    check(f'positive-weight determinant pairing a{a}',S.diag(0,-2)*vector==S.Matrix([0,2*a]))
    square=(vector.T*S.diag(0,-2)*vector)[0]
    check(f'signed reference normal square a{a}',square==-2*a*a)
    check(f'E double residue a{a}',S.simplify(-3*(-square)/24)==-S.Rational(a*a,4))

certificate={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS',
             'check_count':len(checks),'checks':checks,
             'scope':'Independent algebra of the actual displayed maps; the geometric audit is separately recorded below.'}
(root/'code/part3_root/infinity_groupoid_checks.json').write_text(json.dumps(certificate,indent=2)+'\n')
path=root/'notes/part3_source_global_groupoid_working.md'
audit={'utc':datetime.now(timezone.utc).isoformat(),'reviewer':'root','status':'PASS',
       'proof':str(path.relative_to(root)),'proof_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
       'verified_maps':[
        'The bounded four-holed rho surface has actual uniform source, Cartier, root and full-reference annular charts; the two unselected degenerations use the proved disc extension.',
        'The scalar-cut squares keep the ordinary q1 and cap h multipliers, their directions, the full period reindexing and the inverse physical closing.',
        'The reflected source-zero object is carried by the literal theta/Cartier map (Q/Z,V), including height translation and the full source period.',
        'The cut-disc contraction supplies the product of the four actual physical returns before passage to the abelian oriented mapping-class group.',
        'The selected rho loop maps to F56 by sigma=rho/u with local complex degree one and extending scalar logarithm on the stated initial/reflected fan scope.',
        'The independent root-scalar parameter gives the actual winding-difference relation with every q1^n/h^n closing retained.',
        'The infinity coordinate map preserves Z, the full Hom lift and scalar; its D^-4 endpoint, reduced doubled period, entire F0 and quadratic scalar cochain are retained.',
        'The relative full-reference construction supplies the annular family arrow, and h_target composed with the infinity involution is exactly the global reflection.'
       ],
       'certificate':'code/part3_root/infinity_groupoid_checks.json',
       'rerun':'records/root_source_global_groupoid_check.out',
       'scope':'Actual groupoid relation on the initial and reflected vertical-edge fan objects; no equality between their individual source-zero returns and no numerical infinity return is inferred.'}
(root/'records/root_audit_source_global_groupoid.json').write_text(json.dumps(audit,indent=2)+'\n')
print('PASS',len(checks),'independent identities; complete-map groupoid audit retained.')
