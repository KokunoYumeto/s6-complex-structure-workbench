"""Fresh small lower-parent certificate for K111 IL.

Builds every labelled determinant-three I2O raw lower cone from its
printed rays. Resolves the whole finite-quotient cone by actual stellar
maps, extracts every physical lower-face chart and computes its cyclic
normal wall relations with the original L period. No old fan, normal
degree table, 324-chart cycle or contraction histogram is loaded.

Scope: the minimal three-chart lower source star and its full raw-parent
morphism. The actual common-fan 324-chart refinements remain separate.
"""
from collections import deque
from functools import reduce
from itertools import product
from math import gcd
from pathlib import Path
import json
import sympy as S

checks=0
def ck(x,m):
    global checks
    checks+=1
    if not x: raise AssertionError(m)
def matrix(c): return S.Matrix.hstack(*map(S.Matrix,c))
def fractional(x): return x-S.floor(x)
def quotient_rays(B):
    inv=B.inv();zero=(S.Rational(0),)*4
    generators=[tuple(fractional(x) for x in inv[:,j]) for j in range(4)]
    seen={zero};q=deque([zero])
    while q:
        a=q.popleft()
        for b in generators:
            c=tuple(fractional(x+y) for x,y in zip(a,b))
            if c not in seen: seen.add(c);q.append(c)
    ck(len(seen)==abs(B.det()),'entire quotient lattice enumerated')
    out=[]
    for a in seen-{zero}:
        v=B*S.Matrix(a)
        ck(all(t.q==1 for t in v),'quotient point is integral')
        v=tuple(map(int,v));d=reduce(gcd,map(abs,v))
        out.append(tuple(x//d for x in v))
    return sorted(set(out),key=lambda v:(sum(abs(x) for x in v),v))

L=S.Matrix([[1,0,3,0],[0,1,1,0],[0,0,1,0],[0,0,0,1]])
T=S.Matrix([[1,0,0,0],[0,1,12,12],[0,0,1,0],[0,0,0,1]])
delta=S.Matrix([0,1,0,0])
upL=S.Matrix([1,1,0,0]);upT=S.Matrix([-1,0,0,0]);ucT=S.Matrix([0,1,0,0])
ck(L*T==T*L,'actual lattice periods commute')
ck(L*delta==T*delta==delta,'both periods preserve physical circle')
U0=(0,12,1,0);U3=(3,13,1,0)
data=[]
for label in range(12):
    e0=(0,label,0,1);e1=(0,label+1,0,1)
    raw=(e0,e1,U0,U3);R=matrix(raw)
    ck(abs(R.det())==3,'actual lower raw quotient order three')
    fan=[raw];steps=[]
    while any(abs(matrix(c).det())>1 for c in fan):
        c=next(c for c in fan if abs(matrix(c).det())>1)
        v=quotient_rays(matrix(c))[0]
        out=[];changed=[]
        for c0 in fan:
            B=matrix(c0);b=B.inv()*S.Matrix(v)
            if min(b)<0 or sum(bool(x>0) for x in b)<=1:
                out.append(c0);continue
            children=[]
            for i,x in enumerate(b):
                if x>0:
                    cc=list(c0);cc[i]=v;cc=tuple(cc)
                    ck(0<abs(matrix(cc).det())<abs(B.det()),'strict determinant descent on every changed cone')
                    children.append(cc);out.append(cc)
            changed.append(dict(parent=c0,barycentric=list(map(str,b)),children=children))
        ck(bool(changed),'stellar ray inserted into actual whole incident star')
        ck(v[3]>0,'upper generic boundary is untouched')
        steps.append(dict(ray=v,maps=changed));fan=out
    ck(len(fan)==8,'whole raw lower cone has eight regular children')
    ck(len({tuple(sorted(c)) for c in fan})==len(fan),'no repeated full cone')
    def vol(c):
        return S.Rational(abs(matrix(c).det()),6*S.prod(v[2]+v[3] for v in c))
    ck(sum(vol(c) for c in fan)==vol(raw),'all child slice volumes equal actual raw volume')
    invariants=[]
    for a in product(range(4),repeat=4):
        if not 0<sum(a)<=3:continue
        row=S.Matrix([a])*R.inv()
        if all(t.q==1 for t in row):invariants.append((a,row))
    for c in fan:
        B=matrix(c)
        for a,m in invariants:
            row=m*B
            ck(all(t.q==1 and t>=0 for t in row),'entire invariant-semigroup map to raw quotient')
        ck(all(0<=v[0]<=3*v[2] for v in c),'both actual source orders nonnegative')
        ck(abs(B.det())==1,'regular original-lattice chart')
    stars=[c for c in fan if e0 in c and e1 in c]
    ck(len(stars)==3,'all minimal physical lower-face charts extracted')
    tangents={v for c in stars for v in c if v not in (e0,e1)}
    tangents=sorted(tangents,key=lambda v:S.Rational(v[0],v[2]))
    ck([(v[0],v[2]) for v in tangents]==[(0,1),(1,1),(2,1),(3,1)],'complete minimal I3 quotient source fan')
    ck(S.Matrix(tangents[-1])==L*S.Matrix(tangents[0]),'actual L source period closes endpoints')
    charts=[]
    am=S.Matrix([[0,-1,0,label+1]])
    ap=S.Matrix([[0,1,0,-label]])
    for c in stars:
        a,b=sorted((v for v in c if v not in (e0,e1)),key=lambda v:v[0])
        B=matrix((e0,e1,a,b));weights=B.inv()*delta
        ck(weights==S.Matrix([-1,1,0,0]),'ordered physical negative/positive normal weights')
        ck((am*B)[:2]==[1,0] and (ap*B)[:2]==[0,1],'actual alpha/beta normal derivative rows')
        # Monomial inverse and complete coefficient columns for both periods.
        periods=[]
        for name,H,units in [('L',L,[upL]),('T',T,[upT,ucT])]:
            target=H*B
            E=target.inv()*H*B
            ck(E==S.eye(4),'full chart period matrix with transported owner')
            coeff=[]
            for u in units:
                forward=target.inv()*u;backward=-B.inv()*H.inv()*u
                ck(E.inv()*forward+backward==S.zeros(4,1),'actual full unit and inverse cancellation')
                coeff.append(list(map(str,forward)))
            periods.append(dict(name=name,target_matrix=[list(map(int,target.row(i))) for i in range(4)],unit_columns=coeff))
        charts.append(dict(rays=(e0,e1,a,b),inverse=[list(map(int,B.inv().row(i))) for i in range(4)],negative_row=list(map(int,am*B)),positive_row=list(map(int,ap*B)),period_maps=periods))
    walls=[]
    for i,r in enumerate(tangents[:-1]):
        left=tuple(map(int,L.inv()*S.Matrix(tangents[-2]))) if i==0 else tangents[i-1]
        right=tangents[i+1]
        B=matrix((e0,e1,r,left))
        relation=B.inv()*(-S.Matrix(left)-S.Matrix(right))
        ck(relation[3]==0 and relation[2]==-2,'full native wall relation and minimal self-intersection')
        ck(B*relation==-S.Matrix(left)-S.Matrix(right),'original four-lattice wall equality')
        walls.append(dict(ray=r,left=left,right=right,negative_degree=int(relation[0]),positive_degree=int(relation[1]),self_intersection=int(relation[2])))
    minus=[x['negative_degree'] for x in walls];plus=[x['positive_degree'] for x in walls]
    ck(sum(minus)==sum(plus)==0,'both line degrees vanish on actual whole I3 fibre')
    I=S.Matrix([[-2,1],[1,-2]])
    rminus=I.inv()*S.Matrix(minus[1:]);rplus=I.inv()*S.Matrix(plus[1:])
    pair=lambda a,b:(a.T*I*b)[0]
    pairings=[pair(rminus,rminus),pair(rminus,rplus),pair(rplus,rplus)]
    # This assertion is a final comparison, never an input to ray construction.
    ck(minus==[-1,0,1] and plus==[-1,1,0],'fresh full normal vectors agree with IL13')
    ck(pairings==[-S.Rational(2,3),-S.Rational(1,3),-S.Rational(2,3)],'fresh minimal intersection numbers agree with IL16')
    data.append(dict(label=label,raw_cone=raw,stellar_maps=steps,all_regular_cones=fan,invariant_generators=len(invariants),physical_charts=charts,full_wall_relations=walls,negative_degrees=minus,positive_degrees=plus,relative_lifts=[list(map(str,rminus)),list(map(str,rplus))],relative_pairings=list(map(str,pairings))))
out=dict(source='I2O.2 and IL.3-16',scope='All twelve minimal three-chart lower source stars, full raw-parent semigroup maps, original period-unit arrows and normal wall vectors. The 324-chart common refinements and321-step contraction histograms remain separately unverified.',checks=checks,labels=data)
p=Path(__file__).resolve().parents[1]
(p/'K111_lower_parent_reconstruction.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(dict(checks=checks,labels=len(data),regular_lower_cones=sum(len(x['all_regular_cones']) for x in data),physical_charts=sum(len(x['physical_charts']) for x in data),degrees=[data[0]['negative_degrees'],data[0]['positive_degrees']],scope=out['scope']),indent=2))
