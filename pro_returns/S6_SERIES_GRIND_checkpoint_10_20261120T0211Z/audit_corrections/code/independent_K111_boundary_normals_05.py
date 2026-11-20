"""Independent receiving checks of revised K111 C/F and their actual NC inputs.

Reads complete supplied data but imports no producing implementation. This is
post-reading algebra/finite geometry, not a whole-fan independent construction.
"""
import hashlib
import json
import time
from collections import Counter
from pathlib import Path
import sympy as s

ROOT=Path(__file__).resolve().parents[2]
INPUT=ROOT/'audit_sign'
started=time.perf_counter(); counts=Counter(); details={}

def require(name,ok):
    counts[name]+=1
    if not ok: raise AssertionError(name)
def equal(name,expr):
    xs=list(expr) if isinstance(expr,s.MatrixBase) else [expr]
    require(name,all(s.factor(s.cancel(q))==0 for q in xs))
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def add(a,b): return [x+y for x,y in zip(a,b)]
def mulmat(M,v): return [dot(row,v) for row in M]

# Entire E factors are independent symbols; they are not replaced by constants.
x,b,a,c,A,C,CO,E0,E1,E2,xi,zeta,xi2,zeta2=s.symbols('x b a c A C CO E0 E1 E2 xi zeta xi2 zeta2', nonzero=True)
fb0=(1-a)*E0; fb1=(1-zeta*a)*E1
vp=xi*zeta*fb0/fb1*A/(a-1)
equal('point a-chart full coefficient',vp-xi*zeta*E0/E1*A/(zeta*a-1))
fc0=(c-1)*E0/c; fc1=(c/zeta-1)*E1/(c/zeta)
vp=xi*zeta*fc0/fc1*C/(c-1)
equal('point c-chart full coefficient',vp-xi*E0/E1*C/(c/zeta-1))
equal('point two-frame compatibility',xi*E0/E1*(-c*A)+(c/zeta)*(xi*zeta*E0/E1*A))
fo0=(x-b)*E0/(b*(x-1)); fo1=(zeta*x-b)*E1/(b*(zeta*x-1))
vp=xi*zeta*fo0/fo1*(x-1)*CO
co_new=xi*zeta*(x-b)/(zeta*x-b)*E0/E1*CO
equal('O full coefficient with original b denominator',vp-(zeta*x-1)*co_new)
co_twice=xi2*zeta2*(zeta*x-b)/(zeta2*zeta*x-b)*E1/E2*co_new
equal('O full group composition',co_twice-xi2*xi*zeta2*zeta*(x-b)/(zeta2*zeta*x-b)*E0/E2*CO)
equal('a full group composition',(xi2*zeta2*E1/E2)*(xi*zeta*E0/E1)-xi2*xi*zeta2*zeta*E0/E2)
equal('c full group composition',(xi2*E1/E2)*(xi*E0/E1)-xi2*xi*E0/E2)
equal('physical subgroup on O',co_new.subs({zeta:1,E1:E0})-xi*CO)

# Original resolved source morphisms and their physical-preserving circle maps.
u,w,R,P=s.symbols('u w R P',nonzero=True)
for name,xx,cc,yy in [('first',u,u*w*w,R*u*w*w),('second',u*u*w,w,R*w)]:
    equal('resolved graph equation '+name,xx*cc-(u*w)**2)
    equal('resolved source equation '+name,xx*yy-(u*w)**2*R)
    equal('resolved x circle map '+name,xx.subs({u:zeta*u,w:w/zeta},simultaneous=True)-zeta*xx)
    equal('resolved c circle map '+name,cc.subs({u:zeta*u,w:w/zeta},simultaneous=True)-cc/zeta)
equal('resolved overlap P',(1/w)*(u*w*w)-u*w)
equal('resolved overlap x',(1/w)**2*(u*w*w)-u)
equal('resolved overlap c',u*w*w-u*w*w)
ub,Z=s.symbols('u_base Z',nonzero=True)
ug=R**2*ub*Z; wg=1/(R*Z)
equal('infinity exact P inverse',ug*wg-R*ub)
equal('infinity exact x inverse',ug**2*wg-R**3*ub**2*Z)
equal('infinity exact y inverse',R*wg-1/Z)

# Exact source rows are rederived from the printed original endpoint formulas.
scope=json.loads((INPUT/'K111_point_graph_lift_scope.json').read_text())
input_hashes={}; all_endpoint={}; exterior_count=0; il_count=0

def rows(endpoint,rays,band=0):
    if endpoint=='zero':
        xr=[v[1]+3*band*v[2]+band*v[3] for v in rays]
        yr=[-v[1]+3*(1-band)*v[2]+(1-band)*v[3] for v in rays]
        pr=[v[2] for v in rays]; rr=[v[2]+v[3] for v in rays]
    elif endpoint=='one':
        xr=[3*v[2]-v[0] for v in rays];yr=[v[0] for v in rays]
        pr=[v[2] for v in rays];rr=pr[:]
    else:
        xr=[v[1]+3*v[2]+2*v[3] for v in rays];yr=[-v[1] for v in rays]
        pr=[v[2]+v[3] for v in rays];rr=[v[2] for v in rays]
    return xr,yr,pr,rr

def route_orders(route,xr,pr):
    if route=='a':return {'a':[x-2*p for x,p in zip(xr,pr)]}
    if route=='c_first':return {'u':xr,'w':[p-x for x,p in zip(xr,pr)]}
    if route=='c_second':return {'u':[x-p for x,p in zip(xr,pr)],'w':[2*p-x for x,p in zip(xr,pr)]}
    raise AssertionError(route)

for ed in scope['endpoints']:
    ep=ed['endpoint']; path=INPUT/ed['input']; sha=hashlib.sha256(path.read_bytes()).hexdigest()
    require('input exact SHA',sha==ed['sha256']);input_hashes[path.name]=sha
    data=json.loads(path.read_text());cones=data['cones'];all_endpoint[ep]=data
    failed=[]; expected_exterior=[]
    for k,co in enumerate(cones):
        xr,yr,pr,rr=rows(ep,co['rays'],co.get('source_band',0))
        require('complete source rows agree '+ep,[xr,yr]==co['source_rows'])
        require('source node equation valuations '+ep,[x+y for x,y in zip(xr,yr)]==[2*p+r for p,r in zip(pr,rr)])
        wall=[x-2*p for x,p in zip(xr,pr)]
        if min(wall)<0<max(wall):failed.append(k)
        if any(v[2]==0 for v in co['rays']):expected_exterior.append(k)
    require('failed whole graph count retained '+ep,failed==ed['full_graph_crossing_charts'])
    require('localized exterior exhausts nonempty faces '+ep,expected_exterior==[q['parent'] for q in ed['localized_exterior']])
    for rec in ed['localized_exterior']:
        co=cones[rec['parent']]; face=[v for v in co['rays'] if v[2]==0]
        require('actual localized face '+ep,face==rec['face'])
        xr,yr,pr,rr=rows(ep,face,co.get('source_band',0))
        orders=route_orders(rec['route'],xr,pr)
        require('exterior graph map coefficients '+ep,orders==rec['morphism']['orders'])
        require('exterior graph map regularity '+ep,all(q>=0 for vals in orders.values() for q in vals))
        exterior_count+=1
    if ep=='one':
        require('exact twelve IL owners',len(ed['noncompact_owners'])==12)
        for owner,recs in ed['noncompact_owners'].items():
            require('three complete IL charts',len(recs)==3)
            for rec in recs:
                co=cones[rec['chart']]
                require('IL actual chart identity',co['rays']==rec['rays'])
                xr,yr,pr,rr=rows(ep,co['rays'])
                require('IL full original source rows',[xr,yr]==rec['source_rows'] and pr==rec['P_row'] and rr==rec['R_row'])
                orders=route_orders(rec['resolved_route'],xr,pr)
                require('IL resolved morphism coefficients',orders==rec['morphism']['orders'])
                require('IL resolved morphism regularity',all(q>=0 for vs in orders.values() for q in vs))
                il_count+=1
    if ep=='zero':
        recs=next(iter(ed['noncompact_owners'].values()))
        require('moving chart scope',len(recs)==31 and sum(q['graph_cross'] for q in recs)==26)
details['exterior_faces']=exterior_count;details['IL_full_charts']=il_count
details['whole_graph_failures_retained']={e['endpoint']:e['full_graph_crossing_count'] for e in scope['endpoints']}

# Reconstruct all 31 actual normal derivatives from original NS characters.
moving_path=INPUT/'K111_new_moving_cap.json';mov=json.loads(moving_path.read_text())
input_hashes[moving_path.name]=hashlib.sha256(moving_path.read_bytes()).hexdigest()
zero_by_rays={tuple(sorted(tuple(v) for v in c['rays'])):c for c in all_endpoint['zero']['cones']}
T0=[[1,0,8,1],[0,1,6,1],[0,0,1,0],[0,0,0,1]]
for chart in mov['charts']:
    require('moving chart lies in actual new atlas',tuple(sorted(tuple(v) for v in chart['original_rays'])) in zero_by_rays)
    after=chart['face']=='native zero after T0'
    aligned=[mulmat(T0,v) for v in chart['original_rays']] if after else chart['original_rays']
    require('moving exact T0 lattice alignment',aligned==chart['aligned_rays'])
    minus=[1,-2,1,1] if after else [1,-1,1,1]
    plus=[-1,1,0,0] if after else [-1,2,0,0]
    require('moving original native derivative characters',minus==chart['negative_row'] and plus==chart['positive_row'])
    require('moving complete analytic unit columns',chart['full_units']==(['c_q*f0/eta','eta/f0'] if after else ['c_q/eta','eta']))
    B=s.Matrix.hstack(*[s.Matrix(v) for v in aligned])
    require('moving regular lattice',abs(B.det())==1)
    weights=list(B.inv()*s.Matrix([-1,0,0,0]))
    require('moving actual physical weights',weights==chart['physical_weights'])
    ni=[i for i,q in enumerate(weights) if q]; ti=[i for i,q in enumerate(weights) if not q]
    require('moving ordered primitive normal weights',sorted(weights[i] for i in ni)==[-1,1])
    for i in ni:
        require('moving full normal derivative standard basis',(dot(minus,aligned[i]),dot(plus,aligned[i]))==((1,0) if weights[i]==-1 else (0,1)))
        require('moving base units have zero first normal term',aligned[i][1]==aligned[i][2]==0 and aligned[i][3]==1)
    require('moving actual quotient tangent rays',[[aligned[i][1],aligned[i][2]] for i in ti]==chart['source_rays'])
    require('moving all central normal divisor orders',[[dot(minus,aligned[i]),dot(plus,aligned[i])] for i in ti]==chart['divisor_orders'])

# Full source surface and its chronological blowdown morphisms.
rays=mov['source_rays'];ds=[v[:] for v in mov['divisor_coefficients']]
det=lambda a,b:a[0]*b[1]-a[1]*b[0]
require('moving complete regular ordered source fan',all(det(a,b)==1 for a,b in zip(rays,rays[1:])))
n=len(rays)-2;Q=s.zeros(n,n)
for i in range(n):
    Q[i,i]=-det(rays[i],rays[i+2])
    if i+1<n:Q[i,i+1]=Q[i+1,i]=1
require('moving independently rebuilt intersection matrix',Q.tolist()==mov['intersection_matrix'])
dminus=s.Matrix(ds[0]);dplus=s.Matrix(ds[1])
ints=[(dminus.T*Q*dminus)[0],(dminus.T*Q*dplus)[0],(dplus.T*Q*dplus)[0]]
require('moving all normal intersections',ints==mov['normal_divisor_intersections'])
current=[v[:] for v in rays]; coeff=[[0]+d+[0] for d in ds]; exceptional=[]
for rec in mov['chronological_contractions']:
    idx=current.index(rec['removed'])
    require('moving actual ordinary blowdown center',current[idx-1]==rec['left'] and current[idx+1]==rec['right'] and add(current[idx-1],current[idx+1])==current[idx])
    exc=[d[idx]-d[idx-1]-d[idx+1] for d in coeff]
    require('moving actual exceptional coefficient transport',exc==rec['coefficient_divisor_exceptional'])
    exceptional.append(exc)
    current.pop(idx)
    for d in coeff:d.pop(idx)
require('moving original fixed sphere times disc target',current==[[1,0],[0,1],[-1,0]])
hp=[d[1] for d in coeff]
require('moving inherited marked section pairings',hp==mov['marked_section_pairings'])
chron=[-sum(e[0]**2 for e in exceptional),-sum(e[0]*e[1] for e in exceptional),-sum(e[1]**2 for e in exceptional)]
require('moving independent chronological intersections',chron==ints)
x2=ints[0]+2*hp[0];xy=-ints[1]-hp[0]-hp[1];y2=ints[2]+2*hp[1]
require('moving actual cap positive line classes',[x2,xy,y2]==mov['own_cap_positive_line_intersections'])
c1sq=x2+2*xy+y2;p1=-3*len(exceptional)
require('moving cap characteristic numbers',[c1sq,xy,p1]==[mov['own_cap_bundle_c1_squared'],mov['own_cap_bundle_c2'],mov['own_cap_tangent_p1']])
require('moving physical pair',[c1sq-xy,p1+c1sq-4*xy]==mov['physical_moving_pair'])
details['moving_charts']=len(mov['charts']);details['moving_pair']=mov['physical_moving_pair']

# NC exact sphere/base/normal matrices, including coefficient conjugation.
Z,Zb,alpha,alphab,beta,betab,em,ep=s.symbols('Z Zbar alpha alphabar beta betabar eminus_bar eplus',nonzero=True)
G=s.Matrix([[1,-Z],[Zb,1]])
Gother=s.Matrix([[1/Zb,-1],[1,1/Z]])
equal('NC positive Cox overlap',Gother*s.diag(Zb,Z)-G)
N=G*s.diag(em,ep)
equal('NC full normal inverse',s.diag(1/em,1/ep)*G.inv()*N-s.eye(2))
T=s.Matrix([[1,-Zb],[Z,1]])
Tother=s.Matrix([[1/Z,-1],[1,1/Zb]])
equal('NC held right coefficient overlap',Tother*s.diag(Z,Zb)-T)
aa,cc=s.symbols('a0 c0')
equal('NC native overlap after entire collar map',s.Matrix([1/(alpha*Z),(alpha*Z)*aa/(alpha*beta),(alpha*Z)*beta*cc])-s.Matrix([1/(alpha*Z),Z*aa/beta,alpha*beta*Z*cc]))
equal('NC entire collar product',alpha*(1/(alpha*beta))*beta-1)
y11,y12,y21=s.symbols('y11 y12 y21');Y=s.Matrix([[y11,y12],[y21,1-y11]])
D=s.diag(alpha,1);Db=s.diag(alphab,1);Y1=D*Y*Db;s1=s.trace(Y1);Y1=Y1/s1
Y2=D.inv()*Y1*Db.inv();Y2=Y2/s.trace(Y2)
equal('NC actual positive Hermitian ball inverse',Y2-Y)

# Physical negative-line conjugation and the final directed arithmetic.
xx,yy,zz,pp=s.symbols('x_squared xy y_squared p1')
B2=xx+yy+zz
ell=pp-xx-zz-4*yy+2*B2
equal('physical conjugation k formula',B2-(xx+2*yy+zz-yy))
equal('physical conjugation ell formula',ell-(pp+xx+2*yy+zz-4*yy))
require('actual inner Stokes pair',[895+12-906,139-24-111]==[1,4])
require('directed reference and Jin reversal',[-(1-72),-4]==[71,-4])
require('native held product and inverse-clutch value',-4//4==-1 and 71-(-1)==72 and (4*71+4)//24==12)

out={'status':'PASS','checks':sum(counts.values()),'check_groups':dict(counts),'details':details,
     'input_sha256':input_hashes,'seconds':round(time.perf_counter()-started,6),
     'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     'scope':'Fresh post-reading boundary/module/normal comparison of revised K111 C/F. Full supplied endpoint data are read, but no whole-fan construction or compact-owner implementation is imported or claimed independently reconstructed. Original full-graph failures remain explicit data.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ['check_groups','input_sha256']},indent=2))
