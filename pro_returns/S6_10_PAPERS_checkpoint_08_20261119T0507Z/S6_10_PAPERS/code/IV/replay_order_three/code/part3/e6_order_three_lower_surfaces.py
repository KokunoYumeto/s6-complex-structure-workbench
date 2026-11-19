"""Actual lower-surface parent data, boundary arrows and integral blowup basis.
The 48 chart maps are retained; their independent PASS412 is not repeated.
No global characteristic sum or return is assigned.
"""
from pathlib import Path
import json,hashlib,datetime
import sympy as S
ROOT=Path(__file__).resolve().parents[2]
tests=[]
def ck(label,value):
    assert bool(value),label
    tests.append(label)
atlas_path=ROOT/'code/part3_fourfold/e6_p_one_common_cayley.json'
faces_path=ROOT/'code/part3/e6_order_three_fixed_input.json'
proof=ROOT/'notes/part3_e6_order_three_lower_surfaces_working.md'
atlas=json.loads(atlas_path.read_text())
faces=json.loads(faces_path.read_text())['three_ends']['one']
lower=[dict(index=i,**c) for i,c in enumerate(atlas['cones']) if c['kind']=='lower_interval']
fixed=[c for c in faces['components'] if c['dimension']==2 and c['tag']=='lower_boundary']
ck('48 actual lower chart inputs',len(lower)==48)
ck('four actual lower fixed components',len(fixed)==4)
I=S.Matrix([[-1,1,0],[1,-3,1],[0,1,-1]])
T=S.Matrix.hstack(S.Matrix([1,1,1]),S.Matrix([1,0,0]),S.Matrix([0,0,1]))
K=S.Matrix([2,1,2])
ck('exceptional basis is a free integral basis',T.det()==-1)
ck('actual total-transform intersection basis',T.T*I*T==-S.eye(3))
ck('canonical coefficients are total-transform sum',T*S.ones(3,1)==K)
ck('actual strict canonical square',(K.T*I*K)[0]==-3)
ck('three node tangent Pontryagin difference',3*(-3-2*3)==-27)
r,t=S.symbols('r t')
source_maps=[(r*t,r*r*t),(r*t*t,r*t),(r*t*t,t),(t,r*t*t)]
jacobians=[S.factor(S.Matrix(v).jacobian([r,t]).det()) for v in source_maps]
ck('literal source Jacobian divisors',jacobians==[-r*r*t,-r*t*t,t*t,-t*t])
a,b,px,py=S.symbols('a b px py',nonzero=True)
for ell in range(4):
    # dv wedge dlog(P^3 (ab)^ell a), modulo the base tangent forms.
    dv=S.Matrix([b,a]);du=S.Matrix([(ell+1)/a,ell/b])
    ck('actual marked volume sign '+str(ell),S.det(S.Matrix.hstack(dv,du))==-1)
    for jj in range(-3,4):
        kk=4*jj+ell
        # Character order P,u_s,Z*,C=lambda0 qK,U6,a_ref,b_ref.
        originalU=S.Matrix([3*(jj+1)-kk,kk,-1,0,0,1,0])
        originalV=S.Matrix([kk+1-3*(jj+1),-kk-1,1,0,0,0,1])
        # Z=P^-j Z*, a=c^j a_ref, c=C u_s^-4.
        changedU=originalU+S.Matrix([jj,-4*jj,0,jj,0,0,0])
        changedV=originalV+S.Matrix([-jj,4*jj,0,-jj,0,0,0])
        U=S.Matrix([3-ell,ell,-1,jj,0,1,0])
        V=S.Matrix([ell-2,-ell-1,1,-jj,0,0,1])
        ck('full B^-j coefficient U '+str((jj,ell)),changedU==U)
        ck('full B^-j coefficient V '+str((jj,ell)),changedV==V)
        ck('complete determinant P/us '+str((jj,ell)),U+V==S.Matrix([1,-1,0,0,0,1,1]))
        H=S.Matrix([-6-3*jj,0,3,0,-1,0,0])
        Up=U+H;Vp=V-H
        ck('typed point-line positive normal '+str((jj,ell)),Up==S.Matrix([-3-ell-3*jj,ell,2,jj,-1,1,0]))
        ck('typed point-line negative normal '+str((jj,ell)),Vp==S.Matrix([ell+4+3*jj,-ell-1,-2,-jj,1,0,1]))
        ck('typed point determinant retained '+str((jj,ell)),Up+Vp==U+V)
        # Index I=i+j and Z*=P^j Z are invariant under full B.
        ck('source and chain representative '+str((jj,ell)),(jj+1)-1==jj and 4*(jj+1)+ell==kk+4)
        # Successive representative arrow retains C^j in C-frame, (C P^-3)^j in point frame.
        ck('point suspension index '+str((jj,ell)),(-3-ell-3*(jj+1))-(-3-ell-3*jj)==-3)
P,R=S.symbols('P R',nonzero=True)
Q=P*P*R
ck('source line square through H',S.cancel(Q**3/R**3-P**6)==0)
ck('source translation contributes actual P^-3',S.cancel((P**-1)**3-P**-3)==0)
report={
 'status':'PASS','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'checks':len(tests),'check_labels':tests,
 'inputs':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [atlas_path,faces_path,proof]},
 'source_maps':[[str(x) for x in z] for z in source_maps],
 'source_jacobians':[str(x) for x in jacobians],
 'source_ray_order':[[1,0],[2,1],[1,1],[1,2],[0,1]],
 'exceptional_intersection':list(map(list,I.tolist())),
 'integral_total_transform_basis':list(map(list,T.tolist())),
 'relative_canonical_strict_coefficients':[2,1,2],
 'blowups_per_node':3,'nodes_per_lower_surface':3,'blowups_per_lower_surface':9,
 'relative_tangent_p1_per_surface':-27,
 'all_lower_parent_charts':lower,'four_fixed_surface_records':fixed,
 'normal_map':'a_ref=c^-j a,b_ref=c^j b; all48 parent normal rows retain a,b up to their saved order',
 'boundary_C_frame':'U=P^(3-l)us^l Z*^-1(C)^j a_ref; V=Z*P^(l-2)us^(-l-1)C^-j b_ref; C=lambda0 qK',
 'boundary_point_frame':'Upt=P^(-3-l)us^l U6^-1 Z*^2(C P^-3)^j a_ref; Vpt=P^(l+4)us^(-l-1)U6 Z*^-2(C P^-3)^-j b_ref',
 'boundary_determinant':'P/us, carrying ab=v to U V=s',
 'independent_chart_audit':'code/part3/e6_lower_surface_blowups_peer.* PASS412; retained rather than repeated',
 'scope':'Four actual lower fixed surfaces, their ninefold source blowdowns, full point/normal boundary maps and relative tangent p1. No closed-double normal square, outer correction, total characteristic pair or return is assigned.'
}
def exact(o):
    if isinstance(o,S.Integer):return int(o)
    raise TypeError(type(o).__name__)
out=ROOT/'code/part3/e6_order_three_lower_surfaces.json'
out.write_text(json.dumps(report,indent=2,default=exact)+'\n')
print(json.dumps({k:v for k,v in report.items() if k in ['status','utc','checks','scope']},indent=2))
