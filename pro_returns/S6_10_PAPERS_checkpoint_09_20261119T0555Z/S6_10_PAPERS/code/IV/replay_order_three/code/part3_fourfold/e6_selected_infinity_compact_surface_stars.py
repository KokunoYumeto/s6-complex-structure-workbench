"""Actual p and finite-base chart closures, full normal maps and intersections."""
from pathlib import Path
from fractions import Fraction as F
from functools import cmp_to_key
from datetime import datetime,timezone
from collections import defaultdict
import hashlib,json
import sympy as S
ROOT=Path(__file__).resolve().parents[2]
ip=ROOT/'code/part3/e6_selected_infinity_factor_overlay.json'
fp=ROOT/'code/part3_fourfold/e6_fixed_face_orbits.json'
ov=json.loads(ip.read_text());ff=json.loads(fp.read_text())
checks=[]
def ck(v,n):
    assert v,n;checks.append(n)
def mat(r):return S.Matrix.hstack(*map(S.Matrix,r))
def rows(M):return [[int(x) if x.q==1 else str(x) for x in r] for r in M.tolist()]
def vec(v):return tuple(map(int,v))
def normal_face(N,A):
    w=list(A*S.Matrix([0,0,0,1]))
    return tuple(sorted(tuple(N[:,i]) for i,z in enumerate(w) if z)),w
charts=[]
def add(kind,label,rays,extra=None):
    N=mat(rays);ck(abs(N.det())==1,'complete chart integral regularity')
    A=N.inv();face,w=normal_face(N,A)
    charts.append({'kind':kind,'label':label,'N':N,'A':A,'face':face,'w':w,'extra':extra or {}})
for ci,c in enumerate(ov['regular4_cones']):
    add('resolved_infinity',ci,c['rays'],
        {'source_unit_exponents':c['B_source_unit_exponents'],
         'full_Hom_unit_exponents':c['B_full_Hom_unit_exponents']})
boundary={}
for ci,c in enumerate(ov['regular4_cones']):
    rr=[tuple(r) for r in c['rays'] if r[2]==0]
    if len(rr)==3:boundary.setdefault(tuple(sorted(rr)),[]).append(ci)
Rp=(0,1,-1,0);Fm=(-1,0,0,0)
ck(len(boundary)==16,'all sixteen genuine v-unit cones')
for ci,f in enumerate(sorted(boundary)):
    add('p_graph',ci,[Rp]+list(f),{'localized_infinity_parents':boundary[f]})
for ci,c in enumerate(ov['regular3_cones']):
    add('native_finite',ci,[Fm]+[[0]+r for r in c['rays']],
        {'parent_full_unit_exponents':c['parent_full_unit_exponents']})
for j in range(4):
    add('native_finite_p',j,[Fm,Rp,(0,1,0,j),(0,1,0,j+1)])
ck(len(charts)==296,'entire literal source-base/p chart closure')

# Every p-cone has the exact p=1/v tangent coordinate and agrees with
# the localized quotient characters (chi^4,chi*sigma,V).
for c in charts:
    N=c['N']
    if c['kind']=='p_graph':
        ck(list((S.Matrix([[0,0,-1,0]])*N))==[1,0,0,0],
           'literal p tangent coordinate')
        ck((S.Matrix([[1,0,0,0],[0,1,1,0],[0,0,0,1]])*N)[:,0]==S.zeros(3,1),
           'other quotient coordinates unchanged by p-boundary ray')
    if c['kind'] in ('native_finite','native_finite_p'):
        ck(list((S.Matrix([[-1,0,0,0]])*N))==[1,0,0,0],
           'literal finite source-base tangent coordinate')

def polar_cmp(a,b):
    def half(v):return 0 if v[1]>0 or (v[1]==0 and v[0]>0) else 1
    ha,hb=half(a),half(b)
    if ha!=hb:return -1 if ha<hb else 1
    cr=a[0]*b[1]-a[1]*b[0]
    if cr:return -1 if cr>0 else 1
    return 0

surface_rows=[]
for rec in ff['selected_ordinary_overlay']['components']:
    if rec['dimension']!=2 or rec['tag'] not in ('chi_unit','chi_unit+v_unit'):continue
    face=tuple(tuple(r) for r in rec['canonical_face'])
    cs=[c for c in charts if c['face']==face]
    ref=cs[0];ti=[i for i,z in enumerate(ref['w']) if not z]
    Q=ref['A'][ti,:];R=ref['N'][:,ti]
    ck(Q*R==S.eye(2),'explicit quotient tangent lattice splitting')
    ck(all(Q*S.Matrix(r)==S.zeros(2,1) for r in face),'normal face killed by tangent quotient')
    iw={int(w):i for i,w in enumerate(ref['w']) if w}
    m0=ref['A'][iw[1],:]-ref['A'][iw[-1],:]
    rays=set();cones=[];loc=[]
    for c in cs:
        tt=[i for i,z in enumerate(c['w']) if not z]
        nr=[vec(Q*c['N'][:,i]) for i in tt]
        ck(abs(S.det(mat(nr)))==1,'surface chart tangent regularity')
        rays.update(nr);cones.append(frozenset(nr))
        ni={int(w):i for i,w in enumerate(c['w']) if w}
        ck(set(ni)=={-1,1},'actual surface physical weights')
        md=c['A'][ni[1],:]-c['A'][ni[-1],:]
        ck(all(((md-m0)*S.Matrix(r))[0]==0 for r in face),'normal difference descends to surface characters')
        ms=(md-m0)*R
        loc.append({'chart':c,'tangent_rays':nr,'local_D_character':ms})
    rr=sorted(rays,key=cmp_to_key(polar_cmp));n=len(rr)
    ck(len(cones)==n,'one surface cone for each complete boundary ray')
    ck(len(set(cones))==n,'distinct complete surface cones')
    ck(set(cones)=={frozenset((rr[i],rr[(i+1)%n])) for i in range(n)},
       'complete cyclic fan support and every common edge')
    for i in range(n):ck(S.det(mat([rr[i],rr[(i+1)%n]]))==1,'positive full surface support order')
    I=S.zeros(n)
    for i in range(n):
        I[i,i]=-S.det(mat([rr[(i-1)%n],rr[(i+1)%n]]))
        I[i,(i-1)%n]=I[i,(i+1)%n]=1
    coeff=[]
    for ray in rr:
        vals=[(r['local_D_character']*S.Matrix(ray))[0] for r in loc if ray in r['tangent_rays']]
        ck(len(vals)==2 and vals[0]==vals[1],'literal normal Cartier common-ray equation')
        coeff.append(vals[0])
    dv=S.Matrix(coeff);ones=S.ones(n,1)
    ds=(dv.T*I*dv)[0];c1sq=(ones.T*I*ones)[0];p1=c1sq-2*n
    ck(p1==3*(4-n),'independent tangent divisor intersection identity')
    local_results=[];vertex_rows=[]
    for aux in ([2,7,11,23],[3,11,17,41]):
        lp=F(0);ld=F(0);verts=[]
        for c in cs:
            aw=list(c['A']*S.Matrix(aux));tw=[aw[i] for i,w in enumerate(c['w']) if not w]
            nw={int(w):aw[i] for i,w in enumerate(c['w']) if w}
            ck(len(tw)==2 and all(x!=0 for x in tw),'generic actual tangent weights')
            lp+=F(tw[0]**2+tw[1]**2,tw[0]*tw[1])
            ld+=F((nw[1]-nw[-1])**2,tw[0]*tw[1])
            verts.append({'kind':c['kind'],'label':c['label'],'tangent':list(map(str,tw)),
                          'normal_negative_positive':[str(nw[-1]),str(nw[1])]})
        ck(lp==p1 and ld==ds,'full localization agrees with integral divisor intersections')
        local_results.append((lp,ld));vertex_rows.append({'auxiliary':aux,'vertices':verts})
    ck(local_results[0]==local_results[1],'two independent complete localization sums')
    transitions=[]
    for x in range(len(cs)):
        for y in range(x+1,len(cs)):
            if len(set(loc[x]['tangent_rays']) & set(loc[y]['tangent_rays']))!=1:continue
            c,d=cs[x],cs[y];M=d['A']*c['N']
            normal_maps=[]
            for ray in face:
                i=[tuple(c['N'][:,k]) for k in range(4)].index(ray)
                j=[tuple(d['N'][:,k]) for k in range(4)].index(ray)
                for other in face:
                    z=[tuple(c['N'][:,k]) for k in range(4)].index(other)
                    ck(M[j,z]==int(other==ray),'actual normal identity block on shared surface overlap')
                normal_maps.append(list(map(str,M[j,:])))
            transitions.append({'from':[c['kind'],c['label']],'to':[d['kind'],d['label']],
                                'full_character_matrix':rows(M),'normal_rows':normal_maps})
    ru=(p1-3*ds)/24
    surface_rows.append({'id':rec['id'],'type':rec['tag'],'face':rec['canonical_face'],
                         'charts':[[c['kind'],c['label']] for c in cs],
                         'quotient_projection':rows(Q),'complete_surface_rays':rr,
                         'integral_intersection_matrix':rows(I),'D_divisor_coefficients':list(map(str,coeff)),
                         'p1':str(p1),'D_square':str(ds),'positive_u':str(ru),'physical_M':str(-ru),
                         'all_normal_overlaps':transitions,'localizations':vertex_rows})
ck(len(surface_rows)==14,'all fourteen closed exceptional/refinement surfaces')

curve_rows=[]
for rec in ff['selected_ordinary_overlay']['components']:
    if rec['dimension']!=1 or rec['tag']!='v_unit':continue
    face=tuple(tuple(x) for x in rec['canonical_face']);cs=[c for c in charts if c['face']==face]
    ck(len(cs)==2,'complete two-chart p curve')
    c=[c for c in cs if c['kind']=='resolved_infinity'][0]
    d=[c for c in cs if c['kind']=='p_graph'][0]
    ct=[i for i,w in enumerate(c['w']) if not w][0]
    ck(list(c['N'][2,:])==[int(i==ct) for i in range(4)],'literal v coordinate at first curve end')
    M=d['A']*c['N'];degree=[];wr=[]
    for ray in face:
        i=[tuple(c['N'][:,k]) for k in range(4)].index(ray)
        j=[tuple(d['N'][:,k]) for k in range(4)].index(ray)
        ck(M[j,i]==1,'normal coefficient identity on p overlap')
        degree.append(-int(M[j,ct]));wr.append(int(c['w'][i]))
    ck(wr==rec['normal_weights'],'p curve physical normal order')
    for aux in ([2,7,11,23],[3,11,17,41]):
        deg=[F(0)]*3;tw=[]
        for c0 in cs:
            aw=list(c0['A']*S.Matrix(aux));tt=[aw[i] for i,w in enumerate(c0['w']) if not w][0];tw.append(tt)
            ck(tt!=0,'nonzero p curve tangent weight')
            for k,ray in enumerate(face):
                i=[tuple(c0['N'][:,z]) for z in range(4)].index(ray);deg[k]+=F(aw[i],tt)
        ck(tw[0]==-tw[1] and deg==degree,'both p-curve normal degree checks')
    product=1
    for w in wr:product*=w
    ru=-sum((F(4-sum(z*z for z in wr),w)+2*w)*de for w,de in zip(wr,degree))/(24*product)
    curve_rows.append({'id':rec['id'],'face':rec['canonical_face'],
                       'normal_weights':wr,'normal_degrees':degree,
                       'v_to_p_full_matrix':rows(M),'positive_u':str(ru),'physical_M':str(-ru)})
ck(len(curve_rows)==12,'all twelve closed p curves')
exc=sum((F(r['positive_u']) for r in surface_rows if r['type']=='chi_unit+v_unit'),F(0))
refn=sum((F(r['positive_u']) for r in surface_rows if r['type']=='chi_unit'),F(0))
cv=sum((F(r['positive_u']) for r in curve_rows),F(0))
ck(exc==-F(5,2),'four exceptional source surface sum')
ck(refn==-F(9,4),'ten refinement surface sum')
ck(cv==F(3,4),'twelve actual p-curve sum')
out={'status':'PASS_COMPLETE_SURFACE_AND_P_CURVE_STARS','utc':datetime.now(timezone.utc).isoformat(),
     'checks':len(checks),'check_labels':checks,
     'inputs':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in (ip,fp)},
     'new_source_maps':{'p_chart':'p=1/v, chi*sigma=T1*T2, V unchanged in the complete genuine point frame',
                        'p_boundary_ray':Rp,'finite_base_ray':Fm,
                        'point_frame':'sigma_a/((p-c_a)/p) at O, canonical at T; all horizontal divisors retained',
                        'selected_overlap':'q^j and psi retained; on each listed refinement component j=0 and psi=1'},
     'full_chart_count':len(charts),
     'charts':[{'kind':c['kind'],'label':c['label'],'rays':rows(c['N'].T),'physical_weights':list(map(int,c['w'])),
                'source_and_Hom_units':c['extra']} for c in charts],
     'surfaces':surface_rows,'p_curves':curve_rows,
     'positive_u_sums_per_O_or_T_copy':{'exceptional_source_surfaces':str(exc),'refinement_surfaces':str(refn),'p_curves':str(cv)},
     'physical_M_sums_per_O_or_T_copy':{'exceptional_source_surfaces':str(-exc),'refinement_surfaces':str(-refn),'p_curves':str(-cv)},
     'scope':'Actual compact normal stars after the literal p and finite-source closures. Strict source and moving selected cap are separate; no global return is assigned.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2,default=lambda x:int(x) if isinstance(x,S.Integer) else str(x))+'\n')
print(json.dumps({'status':out['status'],'checks':len(checks),'charts':len(charts),
                  'surfaces':[{k:r[k] for k in ('id','p1','D_square','positive_u')} for r in surface_rows],
                  'curve_sum':str(cv),'surface_sums':[str(exc),str(refn)]},indent=2))
