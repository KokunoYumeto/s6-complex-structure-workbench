"""Independent one-circle localization from complete compact-star maps.

The author's two generic auxiliary circles and divisor-square computation
are not imported.  This audit uses the native base circle (1,0,0,0),
retaining its fixed curves, their literal line clutches, and the remaining
isolated points.  Full source/unit identification is audited in prose.
"""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
from datetime import datetime, timezone
import json
import sympy as S

ROOT=Path(__file__).resolve().parents[2]
INPUT=ROOT/'code/part3_fourfold/e6_selected_infinity_compact_surface_stars.json'
data=json.loads(INPUT.read_text())
checks=0
def ck(x):
    global checks
    assert bool(x)
    checks+=1
def pair(x): return tuple(int(a) for a in x)
def matrix(rays): return S.Matrix.hstack(*[S.Matrix(r) for r in rays])
delta=S.Matrix([0,0,0,1])
epsilon=S.Matrix([1,0,0,0])
allcharts={}
for raw in data['charts']:
    N=matrix(raw['rays']);A=N.inv();w=A*delta
    ck(abs(N.det())==1)
    allcharts[(raw['kind'],raw['label'])]=(N,A,w)

rows=[]
for surf in data['surfaces']:
    cs=[allcharts[tuple(label)] for label in surf['charts']]
    labels=[tuple(label) for label in surf['charts']]
    N0,A0,w0=cs[0]
    ti=[i for i in range(4) if w0[i]==0]
    Q=A0[ti,:]
    qe=Q*epsilon
    ck(qe!=S.zeros(2,1))
    local=[]
    for label,(N,A,w) in zip(labels,cs):
        tis=[i for i in range(4) if w[i]==0]
        ni={int(w[i]):i for i in range(4) if w[i]!=0}
        ck(set(ni)=={-1,1})
        rr=[pair(Q*N[:,i]) for i in tis]
        md=A[ni[1],:]-A[ni[-1],:]
        aw=A*epsilon
        local.append({'label':label,'N':N,'A':A,'ti':tis,'rays':rr,
                      'md':md,'aw':aw,'m':md.dot(epsilon)})
    rr=[tuple(x) for x in surf['complete_surface_rays']]
    # Re-establish the entire cyclic support directly from all full charts.
    ck({frozenset(c['rays']) for c in local}==
       {frozenset((rr[i],rr[(i+1)%len(rr)])) for i in range(len(rr))})
    fixed_rays=[]
    p1=F(0);dsq=F(0);curve_data=[];point_data=[]
    for i,r in enumerate(rr):
        if S.det(matrix([r,pair(qe)]))!=0:
            continue
        fixed_rays.append(r)
        prev,nxt=rr[(i-1)%len(rr)],rr[(i+1)%len(rr)]
        left=[c for c in local if set(c['rays'])=={prev,r}][0]
        right=[c for c in local if set(c['rays'])=={r,nxt}][0]
        il=left['ti'][left['rays'].index(r)]
        ir=right['ti'][right['rays'].index(r)]
        otherl=left['ti'][left['rays'].index(prev)]
        otherr=right['ti'][right['rays'].index(nxt)]
        k=left['aw'][il];m=left['m']
        ck(k!=0 and right['aw'][ir]==k)
        ck(left['aw'][otherl]==right['aw'][otherr]==0)
        ck(right['m']==m)
        # Actual coefficient transition n_right = z_left^t n_left.
        degree=-(right['md']-left['md']).dot(left['N'][:,otherl])
        selfint=-S.det(matrix([prev,nxt]))
        # Check that the very same coefficient arrow transports the
        # surface normal (tangent to the fourfold's fixed surface).
        tangentdegree=-(right['A'][ir,:]-left['A'][il,:]).dot(left['N'][:,otherl])
        ck(tangentdegree==selfint)
        p1+=F(selfint)
        value=F(2*m*degree,k)-F(m*m*selfint,k*k)
        dsq+=value
        curve_data.append({'ray':r,'normal_weight':str(k),'D_weight':str(m),
                           'D_degree':str(degree),'self_intersection':str(selfint),
                           'D_square_contribution':str(value),
                           'charts':[left['label'],right['label']]})
    for c in local:
        tw=[c['aw'][i] for i in c['ti']]
        if any(t==0 for t in tw):
            ck(sum(t==0 for t in tw)==1)
            continue
        m=c['m'];dp=F(tw[0]**2+tw[1]**2,tw[0]*tw[1]);dd=F(m*m,tw[0]*tw[1])
        p1+=dp;dsq+=dd
        point_data.append({'chart':c['label'],'tangent_weights':list(map(str,tw)),
                           'D_weight':str(m),'p1_contribution':str(dp),'D_square_contribution':str(dd)})
    ck(p1==F(surf['p1']))
    ck(dsq==F(surf['D_square']))
    u=(p1-3*dsq)/24
    ck(u==F(surf['positive_u']) and -u==F(surf['physical_M']))
    rows.append({'id':surf['id'],'type':surf['type'],'fixed_curves':curve_data,
                 'isolated_points':point_data,'p1':str(p1),'D_square':str(dsq),
                 'positive_u':str(u),'physical_M':str(-u)})
ck(len(rows)==14)
out={'status':'PASS_INDEPENDENT_BASE_CIRCLE_COMPACT_STARS','reviewer':'blind_control',
     'utc':datetime.now(timezone.utc).isoformat(),'checks':checks,
     'input':str(INPUT.relative_to(ROOT)),'input_sha256':sha256(INPUT.read_bytes()).hexdigest(),
     'auxiliary_cocharacter':[1,0,0,0],
     'method':'Fixed-curve and isolated-point localization; every curve degree comes from the full normal coefficient arrow. No author divisor-square matrix or generic-circle sum used.',
     'surfaces':rows,
     'scope':'Four exceptional and ten refinement compact-star types for one O/T copy. Source/point-line global gluing and the second O/T orbit are retained separately in the geometric peer proof; no total source return.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':out['status'],'checks':checks,'surfaces':len(rows),
                  'fixed_curve_count':sum(len(r['fixed_curves']) for r in rows),
                  'isolated_point_count':sum(len(r['isolated_points']) for r in rows)}))
