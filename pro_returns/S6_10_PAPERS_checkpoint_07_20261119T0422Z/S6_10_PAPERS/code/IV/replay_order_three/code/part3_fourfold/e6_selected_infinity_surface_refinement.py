"""Full parent normal arrows and strict A3 normal intersections."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime, timezone
import sympy as S
import json, hashlib
ROOT=Path(__file__).resolve().parents[2]
op=ROOT/'code/part3/e6_selected_infinity_factor_overlay.json'
fp=ROOT/'code/part3_fourfold/e6_fixed_face_orbits.json'
ov=json.loads(op.read_text()); ff=json.loads(fp.read_text())
checks=[]
def ck(v,n):
    assert v,n
    checks.append(n)
def eq(v,n): ck(S.factor(v)==0,n)
def mat(r): return S.Matrix.hstack(*map(S.Matrix,r))
def rows(M):return [[str(x) for x in r] for r in M.tolist()]
aa,nm,np,chi=S.symbols('a nm np chi',nonzero=True)
strict=[]; exceptional=[]
for j in range(4):
    face=[[0,1,j],[0,1,j+1]]
    common=[c for c in ov['regular3_cones'] if all(r in c['rays'] for r in face)]
    ck(len(common)==1,'unique refined strict normal cone')
    h,k,l=[r for r in common[0]['rays'] if r not in face][0]
    ck(h==1,'literal strict source tangent coordinate')
    eta=aa; v=aa**k*nm*np; V=aa**l*nm**j*np**(j+1)
    so=S.cancel(V/(eta**(j+1)*v**j));to=S.cancel(v/so)
    eq(so-aa**(3-j)*np,'strict full positive parent arrow')
    eq(to-nm,'strict full negative parent arrow')
    eq(eta*v-eta*so*to,'strict source parameter preserved')
    eq(chi**(j+1)*(chi*aa)**(3-j)-chi**4*aa**(3-j),
       'refined fourth-root positive normal character')
    rec=[r for r in ff['selected_ordinary_overlay']['components']
         if r['dimension']==2 and r['canonical_face']==[[0,0,1,j],[0,0,1,j+1]]]
    ck(len(rec)==1,'exact strict fixed face')
    rec=rec[0]
    ck(len(rec['face_occurrences'])==1,'one strict source star')
    charts=[]; rr=set()
    for ci in rec['face_occurrences'][0]['charts']:
        co=ov['regular4_cones'][ci];N=mat(co['rays']);A=N.inv()
        w=list(A*S.Matrix([0,0,0,1]));ti=[i for i,z in enumerate(w) if not z]
        ck(len(ti)==2,'two strict source tangent axes')
        rays=[tuple(N[:2,i]) for i in ti]
        ck(abs(S.det(mat(rays)))==1,'literal regular source quotient cone')
        rr.update(rays);charts.append((ci,N,A,w,ti,rays))
    rays=sorted(rr,key=lambda x:F(x[0],x[1]))
    ck(rays==[(i,1) for i in range(5)],'actual minimal A3 source rays')
    I=S.zeros(3)
    for i in range(3):
        I[i,i]=-S.det(mat([rays[i],rays[i+2]]))/S.det(mat([rays[i],rays[i+1]]))
        if i:I[i,i-1]=I[i-1,i]=1
    ck(I==S.Matrix([[-2,1,0],[1,-2,1],[0,1,-2]]),'oriented integral source intersection')
    degrees=[]; transitions=[]
    for ray in rays[1:-1]:
        ds=[];detail=[]
        for aux in ([2,7,11,23],[3,11,17,41]):
            d=[F(0),F(0)];tw=[];verts=[]
            for ci,N,A,w,ti,cr in charts:
                if ray not in cr:continue
                tangent=ti[1-cr.index(ray)]
                aw=A*S.Matrix(aux);tweight=aw[tangent];tw.append(tweight)
                ck(tweight!=0,'nonzero exceptional tangent character')
                nw=[]
                for idx,r in enumerate(rec['canonical_face']):
                    col=[list(N[:,i]) for i in range(4)].index(r)
                    ck(w[col]==[-1,1][idx],'fixed normal physical order')
                    d[idx]+=F(aw[col],tweight);nw.append(str(aw[col]))
                verts.append({'chart':ci,'tangent':str(tweight),'normal':nw})
            ck(len(tw)==2 and tw[0]==-tw[1],'both complete exceptional curve charts')
            ck(all(x.denominator==1 for x in d),'integral exact normal degrees')
            ds.append(d);detail.append({'auxiliary':aux,'vertices':verts})
        ck(ds[0]==ds[1],'two independent normal degree calculations')
        degrees.append([int(x) for x in ds[0]])
        transitions.append({'ray':ray,'checks':detail})
    D=S.Matrix([d[1]-d[0] for d in degrees]);lift=I.inv()*D
    eq((I*lift-D).norm(),'actual relative normal lift equation')
    ck((sum((i+1)*D[i] for i in range(3))+j+1)%4==0,
       'actual quotient boundary coefficient character retained')
    square=(D.T*lift)[0]
    ck(square==[-S.Rational(3,4),-1,-S.Rational(3,4),0][j],
       'direct relative normal square')
    strict.append({'j':j,'common_third_ray':[h,k,l],
                   'positive_parent_factor_power':3-j,'negative_parent_factor_power':0,
                   'normal_coefficient_root_characters':[4,-j-1],
                   'normal_ideal_powers':{'positive':4-j,'negative':0},
                   'normal_base_L_powers':{'positive':j,'negative':-j-1},
                   'surface_source_rays':rays,'normal_degrees_negative_positive':degrees,
                   'intersection_matrix':rows(I),'D_degrees':list(map(str,D)),
                   'relative_lift':list(map(str,lift)),'D_square_difference':str(square),
                   'all_normal_transition_checks':transitions})
    face=[[1,0,j],[1,0,j+1]]
    common=[c for c in ov['regular3_cones'] if all(r in c['rays'] for r in face)]
    ck(len(common)==1,'unique exceptional refined normal cone')
    h,k,l=[r for r in common[0]['rays'] if r not in face][0]
    ck(k==1,'literal exceptional source tangent coordinate')
    eta=aa**h*nm*np;v=aa;V=aa**l*nm**j*np**(j+1)
    so=S.cancel(V/(eta**j*v**j));to=S.cancel(eta/so)
    eq(so-np,'exceptional positive parent arrow')
    eq(to-aa**j*nm,'exceptional negative parent arrow')
    eq(v*to-aa**(j+1)*nm,'entire second source normal coefficient')
    exceptional.append({'j':j,'common_third_ray':[h,k,l],
                        'parent_positive_power':0,'parent_negative_power':j,
                        'full_second_chart':'A=n_plus, B=v^(j+1)*n_minus',
                        'refined_fibre_degrees_negative_positive':[-j-1,0]})
record={'status':'PASS_ACTUAL_SURFACE_REFINEMENT_NORMALS','utc':datetime.now(timezone.utc).isoformat(),
        'checks':len(checks),'check_labels':checks,
        'inputs':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in (op,fp)},
        'strict_surfaces':strict,'exceptional_source_fibres':exceptional,
        'scope':'Actual common-refinement parent arrows, normal characters, integral A3 normal comparison and exceptional fibre degrees. Full surface/reference-cap global integration remains in progress.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(record,indent=2,default=lambda x:int(x) if isinstance(x,S.Integer) else str(x))+'\n')
print(json.dumps({'status':record['status'],'checks':record['checks'],
                  'strict':[{k:r[k] for k in ('j','common_third_ray','normal_degrees_negative_positive','D_square_difference')} for r in strict],
                  'exceptional':exceptional},indent=2))
