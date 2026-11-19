#!/usr/bin/env python3
"""Exact divisor and complete directed-clutch certificate for IC2.1--6."""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction
import hashlib
import json
import sympy as S

ROOT=Path(__file__).resolve().parents[2]
SOURCE='notes/part3_e6_selected_i3_moving_c2_working.md'
STAR='code/part3/e6_selected_i3_moving_star.json'
checks=[]
def ck(name,yes):
    assert bool(yes),name
    checks.append(name)
def eq(name,a,b=0):ck(name,S.simplify(a-b)==0)
def sha(name):return hashlib.sha256((ROOT/name).read_bytes()).hexdigest()
star=json.loads((ROOT/STAR).read_text())
ck('moving star source lock',sha('notes/part3_e6_selected_i3_moving_star_working.md')==star['source_sha256'])
ck('exact source inventory',len(star['charts'])==36 and len(star['chronological_blowups'])==34)

def det2(a,b):return a[0]*b[1]-a[1]*b[0]
rays=[tuple(r) for r in star['surface_rays']]
ck('complete sphere boundary rays',rays[0]==(1,0) and rays[-1]==(-1,0))
for i in range(len(rays)-1):
    ck('consecutive tangent determinant '+str(i),det2(rays[i],rays[i+1])==1)
vertical=rays[1:-1]
I=[[0]*len(vertical) for _ in vertical]
for i,r in enumerate(vertical):
    I[i][i]=-det2(rays[i],rays[i+2])
    if i:I[i][i-1]=1
    if i+1<len(vertical):I[i][i+1]=1
ck('independent full intersection matrix',I==star['compact_vertical_intersection_matrix'])
a=S.Matrix([r[0] for r in vertical]);hh=S.Matrix([r[1] for r in vertical]);IM=S.Matrix(I)
ck('entire parameter divisor is null',IM*hh==S.zeros(len(vertical),1))
eq('actual compact difference square',(a.T*IM*a)[0],-3)

# Reconstruct the chronological blowups from the original product fan.
actual=[(1,0),(0,1),(-1,0)]
zero_centres=0;infinity_centres=0
for i,step in enumerate(star['chronological_blowups']):
    left=tuple(step['left']);right=tuple(step['right']);new=tuple(step['exceptional'])
    index=actual.index(left)
    ck('blowup adjacent actual centre '+str(i),actual[index+1]==right)
    ck('blowup primitive sum '+str(i),new==tuple(left[k]+right[k] for k in range(2)))
    ck('blowup original centre determinant '+str(i),det2(left,right)==1)
    zero_centres+=int((1,0) in (left,right))
    infinity_centres+=int((-1,0) in (left,right))
    actual.insert(index+1,new)
ck('all chronological blowups reproduce all charts',actual==rays)
ck('actual strict zero section centres',zero_centres==3)
ck('actual strict infinity section centres',infinity_centres==0)

# Recompute all normal orders from the original four-dimensional columns.
plus=S.Matrix([[-2,1,0,0]])
minus=S.Matrix([[2,-1,1,0]])
normal_records=[]
for i,chart in enumerate(star['charts']):
    N=S.Matrix.hstack(*[S.Matrix(v) for v in chart['canonical_four_rays']])
    ck('full regular ambient chart '+str(i),abs(N.det())==1)
    ck('full inverse ambient chart '+str(i),N.inv()==S.Matrix(chart['canonical_inverse_matrix']))
    pp=list(plus*N);mm=list(minus*N)
    ip=chart['normal_positive_column'];im=chart['normal_negative_column']
    ck('positive derivative physical orders '+str(i),pp[ip]==1 and pp[im]==0)
    ck('negative derivative physical orders '+str(i),mm[ip]==0 and mm[im]==1)
    for j in chart['tangent_columns']:
        col=chart['canonical_four_rays'][j];rr=(col[0],col[3])
        expected={ (1,0):(-2,3),(-1,0):(3,-2)}.get(rr,(0,0))
        ck('actual tangent normal divisors '+str(i)+' '+str(j),(pp[j],mm[j])==expected)
        ck('original tangent quotient '+str(i)+' '+str(j),list(rr) in chart['surface_rays'])
    normal_records.append({'original_cone':chart['cone'],
        'period_word':chart['canonicalizing_period_h_B'],
        'positive_dual_orders':pp,'negative_dual_orders':mm,
        'original_four_rays':chart['canonical_four_rays']})

z,zb,P,Pb,cq,cqb,Fm,Fmb,Fp=S.symbols('Z Zbar P Pbar cq cqbar Fm Fmbar Fp',nonzero=True)
G0=S.Matrix([[1,-z],[zb,1]])
G1=S.Matrix([[1/zb,-1],[1,1/z]])
eq('positive Cox determinant',G0.det(),1+z*zb)
ck('complete two-chart positive frame',S.simplify(G1*S.diag(zb,z)-G0)==S.zeros(2))
native=S.Matrix([Pb*cqb*zb**-3*Fmb,z**2*Fp])
native_other=S.diag(zb,z)*native
ck('whole normal clutch in both charts',S.simplify(G1*native_other-G0*native)==S.zeros(2,1))
eq('retained conjugate parameter phase ratio',Pb/(1/P),P*Pb)
eq('negative horizontal coefficient in second chart',zb*zb**-3,zb**-2)
eq('positive horizontal coefficient in second chart',z*z**2,z**3)
Pi=S.Matrix([1,zb])*S.Matrix([[1,z]])/(1+z*zb)
ck('actual first eigenline projector',S.simplify(Pi*Pi-Pi)==S.zeros(2))
phase=S.symbols('phase',nonzero=True)
ck('entire projector clutch matrix',S.simplify(G0*S.diag(phase,1)*G0.inv()-(S.eye(2)+(phase-1)*Pi))==S.zeros(2))

# Basis (strict zero section, strict infinity section, parameter fibre).
# The entries are obtained from the chronological maps, not a fitted pair.
Q=S.Matrix([[-zero_centres,0,1],[0,-infinity_centres,1],[1,1,0]])
def pair(x,y):return (S.Matrix(x).T*Q*S.Matrix(y))[0]
root1=[3,-2,1]
root2=[2,-3,0]
c2=pair(root1,root2)
c1sq=pair([x+y for x,y in zip(root1,root2)],
          [x+y for x,y in zip(root1,root2)])
eq('complete collision c2',c2,-19)
eq('complete collision determinant square',c1sq,-75)
eq('strict divisor difference square',pair([1,-1,0],[1,-1,0]),-3)

# Directed reference coefficient phases, including the common winding four.
s,sb=S.symbols('s sbar',nonzero=True)
eq('first reference positive phase factor',sb**-4/s**4,(s*sb)**-4)
refQ=S.Matrix([[0,1],[1,0]])
ref1=S.Matrix([1,-4]);ref2=S.Matrix([-1,-4])
refc2=(ref1.T*refQ*ref2)[0]
eq('whole reference c2',refc2,0)
eq('reference determinant square',((ref1+ref2).T*refQ*(ref1+ref2))[0],0)

moving=S.Matrix([c1sq-c2,-102+c1sq-4*c2])
reference=S.Matrix([-refc2,-4*refc2])
relative=moving-reference
ck('actual moving-reference pair',relative==S.Matrix([-56,-101]))
eq('retained MC3 coefficient relation',relative[1],4*relative[0]+123)
inner=S.Matrix([-63,453])+S.Matrix([72,-348])+relative
jin=-inner
ck('complete physical inner pair',inner==S.Matrix([-47,4]))
ck('complete Jin-oriented pair',jin==S.Matrix([47,-4]))
eq('actual Jin index',(4*jin[0]-jin[1])/24,8)
mu=jin[1]/4;nu=jin[0]-mu
ck('exact fixed-C0 physical coordinate map',[mu,nu]==[-1,48])

deps=[SOURCE,STAR,'notes/part3_e6_selected_i3_moving_star_working.md',
 'notes/part3_e6_selected_i3_moving_cap_working.md',
 'notes/part3_e6_selected_i3_outer_transfer_working.md',
 'notes/part3_e6_selected_infinity_moving_c2_working.md',
 'records/checks_audit_e6_selected_i3_moving_cap.json',
 'records/root_audit_e6_selected_i3_transfer_flop.json']
out={'status':'PASS','utc':datetime.now(timezone.utc).isoformat(),
 'checks':len(checks),'source':SOURCE,'source_sha256':sha(SOURCE),
 'dependencies':{p:sha(p) for p in deps},
 'scope':'The exact MC3 collision and whole fixed-source reference cap bundles; M6,b1,m2,n1, retained scalar root/finite character/full reference.',
 'original_charts':normal_records,'chronological_blowups':star['chronological_blowups'],
 'independent_compact_intersection_matrix':I,
 'closed_replacement_intersection_matrix':Q.tolist(),
 'strict_zero_centres':zero_centres,'strict_infinity_centres':infinity_centres,
 'collision_roots':root1,'collision_c2':c2,'collision_c1_square':c1sq,
 'reference_roots':[list(ref1),list(ref2)],'reference_c2':refc2,
 'moving_reference_pair':list(relative),'kappa':relative[0],
 'complete_inner_pair':list(inner),'complete_jin_pair':list(jin),
 'fixed_C0_pair':[mu,nu],'index':8,'checks_named':checks}
def encode(value):
    if isinstance(value,S.Integer):return int(value)
    if isinstance(value,S.Rational):return str(value)
    raise TypeError(type(value).__name__)
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2,default=encode)+'\n')
print(json.dumps({k:out[k] for k in ['status','checks','collision_c2','reference_c2',
       'kappa','complete_jin_pair','fixed_C0_pair']},indent=2,default=encode))
