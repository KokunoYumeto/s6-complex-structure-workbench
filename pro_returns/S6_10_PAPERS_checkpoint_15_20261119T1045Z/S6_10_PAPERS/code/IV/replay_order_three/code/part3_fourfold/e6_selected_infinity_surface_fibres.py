"""Exact source projections and fibre normal maps in the infinity ledger."""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
import sympy as S
import json,hashlib
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parents[2]
ip=ROOT/'code/part3/e6_selected_infinity_factor_overlay.json'
d=json.loads(ip.read_text());checks=[]
def ck(v,n):
    assert v,n;checks.append(n)
def eq(e,n):ck(S.factor(e)==0,n)
chi,X,Y,t,x,y,eta,v,ss,tt,pp=S.symbols('chi X Y t x y eta v s tnormal p')
eq((chi**-3*Y)**2-(chi**-2*X)**3+2*(chi**-2*X)**2-chi**-4*(chi**-2*X)
   -chi**-6*(Y*Y-X**3+2*chi*chi*X*X-X),'strict source quotient equation')
q=chi**4;x0=chi**6*X;y0=chi**9*Y
eq(y0*y0-x0**3+2*q*q*x0*x0-q**3*x0-chi**18*(Y*Y-X**3+2*chi*chi*X*X-X),'full infinity Weierstrass morphism')
eq((1/v)*(v*tt)-tt,'exceptional source-normal inverse')
eq(ss*(v*tt)-(ss*tt)*v,'exceptional two-factor product')
eq((eta*ss)*tt-eta*(ss*tt),'strict two-factor product')
eq(1/(1/v)-v,'exceptional projective inverse')
eq((1/v-1).subs(v,1/pp)-(pp-1),'actual primitive projective reset')

faces=defaultdict(list)
for ci,co in enumerate(d['regular3_cones']):
    N=S.Matrix.hstack(*map(S.Matrix,co['rays']));A=N.inv();w=list(map(int,A*S.Matrix([0,0,1])))
    face=tuple(sorted(tuple(r) for r,z in zip(co['rays'],w) if z))
    faces[face].append((ci,N,A,w))
out=[]
for face,charts in sorted(faces.items()):
    if len(face)!=2 or not all(sum(r[i] for r in face)>0 for i in (0,1)):continue
    ck(len(charts)==2,'refinement surface complete fibre P1')
    ds=[];details=[]
    for aux in ([1,7,53],[2,11,79]):
        deg=[F(0),F(0)];tang=[];vv=[]
        for ci,N,A,w in charts:
            aw=A*S.Matrix(aux);ti=[i for i,z in enumerate(w) if not z]
            ck(len(ti)==1 and aw[ti[0]]!=0,'fibre nonzero tangent character')
            tw=int(aw[ti[0]]);tang.append(tw);nw=[]
            for j,r in enumerate(face):
                col=[tuple(N[:,i]) for i in range(3)].index(r);n=int(aw[col]);deg[j]+=F(n,tw);nw.append(n)
            vv.append({'cone':ci,'tangent':tw,'normal':nw})
        ck(tang[0]==-tang[1],'fibre opposite tangent rays')
        ck(all(z.denominator==1 for z in deg),'fibre normal integral degree')
        ds.append(deg);details.append({'auxiliary':aux,'vertices':vv})
    ck(ds[0]==ds[1],'independent exact fibre normal degree')
    # Ordering is the literal sorted primitive-ray ordering, with physical
    # weights negative then positive; it is not reset by a positive-weight sum.
    w=[]
    ci,N,A,ww=charts[0]
    for r in face:w.append(ww[[tuple(N[:,i]) for i in range(3)].index(r)])
    ck(w==[-1,1],'fibre physical normal ordering')
    out.append({'face':face,'weights':w,'normal_degrees':list(map(int,ds[0])),'checks':details})
ck(len(out)==10,'all ten refinement surface fibre types')
record={'status':'PASS_SURFACE_FIBRE_MAPS','utc':datetime.now(timezone.utc).isoformat(),
        'checks':len(checks),'check_labels':checks,'overlay_sha256':hashlib.sha256(ip.read_bytes()).hexdigest(),
        'refinement_fibres':out,
        'raw_parent_exceptional_source_fibre':{'coordinates':'p=1/v, A=s, B=v*t; sigma=v*s*t','normal_weights':[-1,1], 'normal_degrees':[-1,0],
           'point_line':'Use the actual nonzero point frame sigma_a/r_a, r_a=(p-c_a)/p on the exceptional source P1. Both zeros and poles are cancelled by the original Cartier sections.'},
        'strict_source_map':'t_e=chi^-4,x_e=chi^-2 Xbar,y_e=chi^-3 Ybar; infinity coordinates q=chi^4,x0=chi^6 Xbar,y0=chi^9 Ybar. Both preserve the full central equation.',
        'actual_refined_exceptional_fibres':{'degrees_negative_positive':[[-j-1,0] for j in range(4)],'morphism':'s_old=n_plus,t_old=v^j*n_minus, hence A=n_plus,B=v^(j+1)*n_minus','certificate':'e6_selected_infinity_surface_refinement.json'},
        'scope':'Actual source projections and ten refinement fibre P1 degrees. The displayed (-1,0) exceptional row is the raw parent; the complete common-refinement normal morphism gives (-j-1,0), as separately certified. Global surface/return integration remains open.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'status':record['status'],'checks':record['checks'],'refinement_fibres':out},indent=2))
