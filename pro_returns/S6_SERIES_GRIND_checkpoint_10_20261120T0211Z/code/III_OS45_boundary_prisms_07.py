"""Exact order-two boundary class and its two core-quotient null witnesses.

After reading the retained proof. This derives the prism boundaries directly
from the two actual monodromies, then compares them with the saved full core.
It does not construct an embedded odd three-cycle or its normal framing.
"""
from pathlib import Path
import datetime, hashlib, itertools, json
import sympy as s
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp
R=Path(__file__).resolve().parents[1]
checks=[]
def check(name,test):
    assert bool(test),name
    checks.append(name)
def smith(A,name):
    D,U,V=[x.to_Matrix() for x in smith_normal_decomp(DomainMatrix.from_Matrix(A).convert_to(s.ZZ))]
    check(name+' exact Smith map',U*A*V==D)
    check(name+' integral row inverse',abs(U.det())==1)
    check(name+' integral column inverse',abs(V.det())==1)
    rank=sum(D[j,j]!=0 for j in range(min(D.shape)))
    return D,U,V,rank
pairs=list(itertools.combinations(range(4),2))
def exterior(A):
    return s.Matrix([[A[i,a]*A[j,b]-A[i,b]*A[j,a] for a,b in pairs] for i,j in pairs])
A0=s.Matrix([[1,8,0,24],[0,1,0,0],[0,-6,1,-16],[0,0,0,1]])
A1=s.Matrix([[1,1,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
B=exterior(A0)-s.eye(6)
C=exterior(A1)-s.eye(6)
alpha=s.eye(6)[:,1]
q=s.Matrix([1,0,0,1,0,0])
u=s.eye(6)[:,3]
check('cusp boundary of e1e2 plus e2delta is twice alpha',B*q==2*alpha)
check('all cusp fibre boundaries have even coordinates',all(int(x)%2==0 for x in B))
chi=s.Matrix([[0,1,0,0,0,0]])
check('explicit mod2 detector kills every cusp fibre boundary',all(int(x)%2==0 for x in chi*B))
check('explicit mod2 detector is one on alpha',(chi*alpha)[0]==1)
check('I1 prism boundary of e2delta is alpha',C*u==alpha)
DB,UB,VB,rb=smith(B,'cusp exterior square')
check('cusp fibre coinvariant rank two',rb==2)
check('cusp fibre coinvariant torsion two copies of Z2',[abs(int(DB[j,j])) for j in range(rb)]==[2,2])
data_path=R/'code/outputs/III_OS45_core_independent.json'
x=json.loads(data_path.read_text());M=s.Matrix(x['matrix']);origins=x['column_origins']
check('cusp actual matrix agrees with complete core input',s.Matrix(x['monodromies'][0])==A0)
check('I1 actual matrix agrees with complete core input',s.Matrix(x['monodromies'][1])==A1)
a=s.Matrix.vstack(alpha,s.zeros(17,1))
j=origins.index('core exterior coinvariant site1 bivector3')
check('literal exterior core column is alpha',M[:,j]==a)
cap=[i for i,o in enumerate(origins) if o.startswith('positive cap fixed exterior')]
matches=[(i,eps) for i in cap for eps in [1,-1] if eps*M[:,i]==a]
check('positive cap fixed-torus relation bounds the same marked alpha',len(matches)==1)
keep=[i for i,o in enumerate(origins) if not (o.startswith('positive cap') or o.startswith('fixed normal site0'))]
ME=M[:,keep];DE,UE,VE,re=smith(ME,'finite-filled cusp exterior core')
check('exterior relation shape',ME.shape==(23,55))
check('exterior relation rank',re==21)
check('exterior only nonunit Smith factor is two',[abs(int(DE[j,j])) for j in range(re) if abs(DE[j,j])!=1]==[2])
w=s.zeros(len(keep),1);w[keep.index(j)]=1
check('displayed integral exterior null witness',ME*w==a)
def encode(z):
    if isinstance(z,s.MatrixBase):return [[int(v) for v in row] for row in z.tolist()]
    raise TypeError(type(z).__name__)
out={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'author':'GPT-6 Astra, root, inherited effort',
 'exposure':'After reading the printed proof and the current complete core reconstruction. No before-proof or separate model-family claim.',
 'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'input_sha256':hashlib.sha256(data_path.read_bytes()).hexdigest(),'passed':len(checks),'checks':checks,
 'basis':['e1^e2','e1^delta','e1^gamma','e2^delta','e2^gamma','delta^gamma'],
 'A0':A0,'A1':A1,'cusp_boundary_matrix':B,'I1_boundary_matrix':C,'alpha':alpha,
 'twice_alpha_prism':q,'boundary_mod2_detector':chi,'I1_prism':u,
 'cusp_smith':DB,'cusp_row_map':UB,'cusp_column_map':VB,
 'exterior_kept_columns':keep,'exterior_matrix':ME,'exterior_smith':DE,
 'exterior_row_map':UE,'exterior_column_map':VE,'exterior_alpha_null_witness':w,
 'full_core_exterior_column':j,'positive_cap_relation':{'column':matches[0][0],'coefficient':matches[0][1],'origin':origins[matches[0][0]]},
 'proved_scope':'The actual fibre coinvariant has the displayed exact order-two class, with explicit prism bounding twice it and exact core/cap quotient witnesses for its images. The injection into boundary H2 is the fibre term of the integral mapping-torus exact sequence.',
 'remaining_gate':'Construct the actual embedded glued odd three-cycle, compare its tangent/normal/reference framings and evaluate its framed linking. No value of the refined0/4 class is inferred from these linear witnesses.'}
target=R/'code/outputs/III_OS45_boundary_prisms_07.json';target.write_text(json.dumps(out,indent=2,default=encode)+'\n')
print(json.dumps({'passed':len(checks),'boundary_order':2,'exterior_null_column':j,'cap_null_relation':out['positive_cap_relation'],'refined_class':'still0or4'}))
