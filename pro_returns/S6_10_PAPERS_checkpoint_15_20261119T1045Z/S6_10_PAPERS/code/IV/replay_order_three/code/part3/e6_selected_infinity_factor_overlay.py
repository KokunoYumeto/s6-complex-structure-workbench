"""Exact common fan for the alternating and grouped E6 corner orders.

The file retains both actual parent morphisms, their point-line unit rows,
the period word, and the extension to the genuine mu4 quotient lattice.
It computes a local common modification and assigns no global return.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations
from collections import Counter
from functools import lru_cache
from math import gcd,lcm,ceil,floor
from datetime import datetime,timezone
import json,time,hashlib
import sympy as s

ROOT=Path(__file__).resolve().parents[2]
START=time.monotonic()
TESTS=[]
def check(name,p):
    assert bool(p),name
    TESTS.append(name)
def cross(a,b,c):
    return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
def area(poly):
    return sum(poly[i][0]*poly[(i+1)%len(poly)][1]-poly[i][1]*poly[(i+1)%len(poly)][0] for i in range(len(poly)))/2
def tidy(poly):
    out=[]
    for v in poly:
        if not out or v!=out[-1]:out.append(v)
    if len(out)>1 and out[0]==out[-1]:out.pop()
    if len(out)>=3 and area(out)<0:out.reverse()
    return out
def clip(poly,a,b):
    ans=[]
    for p,q in zip(poly,poly[1:]+poly[:1]):
        cp,cq=cross(a,b,p),cross(a,b,q)
        if cp>=0:ans.append(p)
        if (cp<0<cq) or (cq<0<cp):
            t=cp/(cp-cq)
            ans.append(tuple(p[i]+t*(q[i]-p[i]) for i in range(2)))
    return tidy(ans)
def intersect(p,q):
    for a,b in zip(q,q[1:]+q[:1]):
        if not p:return []
        p=clip(p,a,b)
    return tidy(p)
def inside(p,poly):
    return all(cross(a,b,p)>=0 for a,b in zip(poly,poly[1:]+poly[:1]))
def primitive(v):
    d=gcd(*map(abs,v))
    return tuple(x//d for x in v)
def ray(p):
    q=(p[0],1-p[0],p[1]);d=lcm(*(a.denominator for a in q))
    return primitive(tuple(int(d*a) for a in q))
def slice_point(v):return (F(v[0],v[0]+v[1]),F(v[2],v[0]+v[1]))
def mat(cols):return s.Matrix.hstack(*map(s.Matrix,cols))
@lru_cache(None)
def inverse(cols):return mat(cols).inv()
@lru_cache(None)
def determinant(cols):return int(mat(cols).det())
def coordinates(cols,v):return tuple(F(a) for a in inverse(tuple(cols))*s.Matrix(v))
def orient(cols):
    cols=tuple(cols)
    if determinant(cols)>0:return cols
    return cols[:-2]+(cols[-1],cols[-2])
def key(cols):return tuple(sorted(cols))
def int_matrix(M):
    check('integral matrix',all(a.q==1 for a in M))
    return [[int(M[i,j]) for j in range(M.cols)] for i in range(M.rows)]
def shifts(v,k):
    if len(v)==3:return (v[0],v[1],v[2]+4*k*(v[0]+v[1]))
    return (v[0],v[1],v[2],v[3]+k*(-v[0]+4*v[1]+4*v[2]))
def period_images(v):
    width=4*(v[0]+v[1]) if len(v)==3 else -v[0]+4*v[1]+4*v[2]
    height=v[-1]
    check('period support width nonnegative',width>=0)
    if width==0:
        check('zero-width point has zero height',height==0)
        return [v]
    return [shifts(v,k) for k in range(ceil(F(-height,width)),floor(F(width-height,width))+1)]
def regularize(initial,label):
    fan={key(c['rays']):c.copy() for c in initial};history=[]
    dimension=len(initial[0]['rays'])
    while True:
        bad=[c for c in fan.values() if determinant(c['rays'])>1]
        if not bad:break
        chosen=max(bad,key=lambda c:(determinant(c['rays']),c['rays']))
        cols=chosen['rays'];det=determinant(cols)
        generators=[]
        for i in range(dimension):
            e=tuple(int(i==j) for j in range(dimension))
            generators.append(tuple(int(a*det)%det for a in coordinates(cols,e)))
        residues={(0,)*dimension};queue=[(0,)*dimension]
        for old in queue:
            for gen in generators:
                new=tuple((a+b)%det for a,b in zip(old,gen))
                if new not in residues:residues.add(new);queue.append(new)
        check(f'{label} residue count',len(residues)==det)
        options=[]
        for r in residues-{(0,)*dimension}:
            numerator=tuple(sum(cols[j][i]*r[j] for j in range(dimension)) for i in range(dimension))
            check(f'{label} residue integral',all(x%det==0 for x in numerator))
            v=primitive(tuple(x//det for x in numerator));a=coordinates(cols,v)
            options.append(((max(a),sum(a),sum(map(abs,v)),v),v))
        _,v=min(options);images=period_images(v)
        if dimension==4:check('quotient refinement leaves chi-unit face fixed',all(r[0]>0 for r in images))
        nextfan={};removed=added=0
        for ck,c in fan.items():
            centres=[]
            for p in images:
                a=coordinates(c['rays'],p)
                if all(x>=0 for x in a) and sum(x>0 for x in a)>1:centres.append((p,a))
            check(f'{label} simultaneous period stars separated',len(centres)<=1)
            if not centres:nextfan[ck]=c;continue
            removed+=1;p,a=centres[0]
            check(f'{label} strict common-face coefficients',all(0<=x<1 for x in a))
            for i,x in enumerate(a):
                if x==0:continue
                child=list(c['rays']);child[i]=p;child=orient(child)
                check(f'{label} strict determinant descent',0<determinant(child)<determinant(c['rays']))
                nk=key(child);check(f'{label} child distinct',nk not in nextfan)
                nextfan[nk]={**c,'rays':child};added+=1
        check(f'{label} nonempty star',removed>0)
        history.append({'ray':v,'period_images':images,'parent_determinant':det,'removed':removed,'added':added})
        fan=nextfan
        check(f'{label} finite execution bound',len(history)<2000)
    return list(fan.values()),history
def facets_audit(fan,label):
    dim=len(fan[0]['rays']);facets=Counter(key(face) for c in fan for face in combinations(c['rays'],dim-1))
    boundary=[(1,0,0),(0,1,0),(0,0,1),(4,4,-1)] if dim==3 else [(1,0,0,0),(-1,4,0,0),(0,0,1,0),(0,0,0,1),(-1,4,4,-1)]
    for face,multiplicity in facets.items():
        check(f'{label} facet multiplicity',multiplicity in (1,2))
        if multiplicity==1:check(f'{label} no exposed interior facet',any(all(sum(a*b for a,b in zip(row,v))==0 for v in face) for row in boundary))
    lower={f for f in facets if all(v[-1]==0 for v in f)}
    upper={f for f in facets if all(v[-1]==(4*(v[0]+v[1]) if dim==3 else -v[0]+4*v[1]+4*v[2]) for v in f)}
    check(f'{label} exact top-bottom period faces',{key(shifts(v,1) for v in face) for face in lower}==upper)
    return {'all_facets':len(facets),'boundary_facets':sum(v==1 for v in facets.values()),'lower_period_faces':sorted(lower),'upper_period_faces':sorted(upper)}

A=lambda j:(1,0,j)
C=lambda j:(0,1,j)
alternating={};grouped={}
for j in range(4):
    alternating[f'A{j}:eta']=(C(j),A(j+1),A(j))
    alternating[f'A{j}:v']=(A(j+1),C(j+1),C(j))
for r in range(1,5):grouped[f'G{r}:eta']=(A(r),A(r-1),C(0))
for r in range(1,5):grouped[f'G{r}:v']=(A(4),C(r),C(r-1))
parents={'alternating':alternating,'grouped':grouped}
polys={which:{name:tidy([slice_point(v) for v in cols]) for name,cols in rows.items()} for which,rows in parents.items()}
for which,rows in parents.items():
    check(f'{which} exact rectangle area',sum(area(p) for p in polys[which].values())==4)
    for cols in rows.values():check(f'{which} smooth three-cone',abs(determinant(cols))==1)
cells=[]
for ak,ap in polys['alternating'].items():
    for gk,gp in polys['grouped'].items():
        poly=intersect(ap,gp)
        if len(poly)>=3 and area(poly)>0:cells.append({'alternating':ak,'grouped':gk,'polygon':poly})
check('overlay areas equal complete rectangle',sum(area(c['polygon']) for c in cells)==4)
vertices=set(p for c in cells for p in c['polygon'])
for c in cells:
    expanded=[]
    for a,b in zip(c['polygon'],c['polygon'][1:]+c['polygon'][:1]):
        edge=[p for p in vertices if cross(a,b,p)==0 and min(a[0],b[0])<=p[0]<=max(a[0],b[0]) and min(a[1],b[1])<=p[1]<=max(a[1],b[1])]
        edge.sort(key=lambda p:(p[0]-a[0])*(b[0]-a[0])+(p[1]-a[1])*(b[1]-a[1]))
        expanded+=edge[:-1]
    c['polygon']=expanded
    check('overlay cell in both literal parents',all(inside(p,polys['alternating'][c['alternating']]) and inside(p,polys['grouped'][c['grouped']]) for p in expanded))
initial3=[]
for ci,c in enumerate(cells):
    poly=c['polygon'][:];triangles=[]
    while len(poly)>3:
        found=False
        for i,b in enumerate(poly):
            a,cc=poly[i-1],poly[(i+1)%len(poly)]
            if cross(a,b,cc)<=0:continue
            triangle=[a,b,cc]
            if any(inside(p,triangle) for j,p in enumerate(poly) if j not in ((i-1)%len(poly),i,(i+1)%len(poly))):continue
            triangles.append(triangle);poly.pop(i);found=True;break
        check('exact conforming polygon ear exists',found)
    check('final overlay triangle positive',area(poly)>0);triangles.append(poly)
    check('triangulation preserves exact cell area',sum(area(t) for t in triangles)==area(c['polygon']))
    c['triangles']=triangles
    for tri in triangles:initial3.append({'rays':orient(tuple(ray(p) for p in tri)),'cell':ci,'alternating':c['alternating'],'grouped':c['grouped']})
facets_audit(initial3,'initial common3')
fan3,hist3=regularize(initial3,'common3')
faces3=facets_audit(fan3,'regular common3')
for c in fan3:
    N=mat(c['rays']);check('regular common3 determinant one',N.det()==1)
    c['parent_monomial_maps']={};c['parent_full_unit_exponents']={}
    for which in ('alternating','grouped'):
        P=mat(parents[which][c[which]]);M=P.inv()*N
        check('both parent morphisms nonnegative integral',all(q.q==1 and q>=0 for q in M))
        c['parent_monomial_maps'][which]=int_matrix(M)
        c['parent_full_unit_exponents'][which]={'vertical':list(map(int,P.inv()*s.Matrix([0,0,1]))),'source_reset':list(map(int,P.inv()*s.Matrix([1,-1,0])))}
    c['physical_weights']=list(map(int,N.inv()*s.Matrix([0,0,1])))
    c['B_target_rays']=[shifts(v,1) for v in c['rays']]
    Nt=mat(c['B_target_rays'])
    c['B_source_unit_exponents']=list(map(int,Nt.inv()*s.Matrix([1,-1,0])))
    c['B_full_Hom_unit_exponents']=list(map(int,Nt.inv()*s.Matrix([0,0,1])))

# Literal extension by the native chi ray in the original quotient lattice.
E=(4,1,0,0)
initial4=[{'rays':orient((E,)+tuple((0,)+v for v in c['rays'])),'common3':i,'cell':c['cell'],'alternating':c['alternating'],'grouped':c['grouped']} for i,c in enumerate(fan3)]
for c in initial4:check('cone-with-E has determinant four',determinant(c['rays'])==4)
fan4,hist4=regularize(initial4,'common mu4')
faces4=facets_audit(fan4,'regular common mu4')
raw4={which:{name:(E,)+tuple((0,)+v for v in cols) for name,cols in rows.items()} for which,rows in parents.items()}
invariants4={}
from itertools import product
for which,rows in raw4.items():
    invariants4[which]={}
    for name,cols in rows.items():
        w=4*inverse(cols)*s.Matrix([1,0,0,0]);weights=tuple(int(q)%4 for q in w)
        check('raw parent mu4 weights integral',all(q.q==1 for q in w))
        gens=[a for a in product(range(5),repeat=4) if 1<=sum(a)<=4 and sum(x*y for x,y in zip(a,weights))%4==0]
        invariants4[which][name]={'rays':cols,'weights':weights,'generators':gens}
for c in fan4:
    N=mat(c['rays']);check('regular common mu4 determinant one',N.det()==1)
    c['parent_invariant_monomial_maps']={}
    for which in ('alternating','grouped'):
        p=invariants4[which][c[which]];M=inverse(p['rays'])*N
        check('common mu4 child contained in both parents',all(q>=0 for q in M))
        rows=[]
        for g in p['generators']:
            row=s.Matrix([g])*M
            check('both coarse quotient invariant arrows holomorphic',all(q.q==1 and q>=0 for q in row))
            rows.append(list(map(int,row)))
        c['parent_invariant_monomial_maps'][which]=rows
    c['physical_weights']=list(map(int,N.inv()*s.Matrix([0,0,0,1])))
    c['local_volume_orders']=[v[1]+v[2]-1 for v in c['rays']]
    c['original_marked_volume_orders']=[-v[0]+5*v[1]+4*v[2]-1 for v in c['rays']]
    c['epsilon_exponents']=[v[1]+v[2] for v in c['rays']]
    c['q_new_exponents']=[v[0] for v in c['rays']]
    c['sigma_fourth_exponents']=[-v[0]+4*v[1]+4*v[2] for v in c['rays']]
    check('all original base and volume orders nonnegative',all(q>=0 for name in ('local_volume_orders','original_marked_volume_orders','epsilon_exponents','q_new_exponents','sigma_fourth_exponents') for q in c[name]))
    check('full base graph identity',all(a+b==4*d for a,b,d in zip(c['q_new_exponents'],c['sigma_fourth_exponents'],c['epsilon_exponents'])))
    c['B_target_rays']=[shifts(v,1) for v in c['rays']];Nt=mat(c['B_target_rays'])
    c['B_source_unit_exponents']=list(map(int,Nt.inv()*s.Matrix([0,1,-1,0])))
    c['B_full_Hom_unit_exponents']=list(map(int,Nt.inv()*s.Matrix([0,0,0,1])))
chi_unit_faces={key(f) for c in fan4 for f in combinations(c['rays'],3) if all(v[0]==0 for v in f)}
check('complete common3 unchanged on chi-unit open',chi_unit_faces=={key((0,)+v for v in c['rays']) for c in fan3})

# Full selected nine-factor extension, including its actual q=0 divisor.
def selected_embed(v):return (v[0],v[1],0,v[2])
Q0=(0,0,1,0);Q1=(0,0,1,1)
selected_parents={name:(Q0,)+tuple(selected_embed(v) for v in cols)
                  for name,cols in grouped.items()}
selected_parents['q:last']=(selected_embed(A(4)),selected_embed(C(4)),Q0,Q1)
selected_fan=[{'rays':orient((Q0,)+tuple(selected_embed(v) for v in c['rays'])),
               'common3':i,'grouped':c['grouped']} for i,c in enumerate(fan3)]
selected_fan.append({'rays':orient(selected_parents['q:last']),'common3':None,'grouped':'q:last'})
def selected_shift(v):return (v[0],v[1],v[2],v[3]+4*v[0]+4*v[1]+v[2])
selected_facets=Counter(key(f) for c in selected_fan for f in combinations(c['rays'],3))
selected_boundaries=[(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1),(4,4,1,-1)]
for face,multiplicity in selected_facets.items():
    check('selected full facet multiplicity',multiplicity in (1,2))
    if multiplicity==1:
        check('selected full no missing interior face',any(all(sum(a*b for a,b in zip(row,v))==0 for v in face) for row in selected_boundaries))
selected_lower={f for f in selected_facets if all(v[-1]==0 for v in f)}
selected_upper={f for f in selected_facets if all(v[-1]==4*v[0]+4*v[1]+v[2] for v in f)}
check('selected full exact period face pairing',{key(selected_shift(v) for v in f) for f in selected_lower}==selected_upper)
for c in selected_fan:
    N=mat(c['rays']);P=mat(selected_parents[c['grouped']])
    check('selected full smooth chart',N.det()==1)
    M=P.inv()*N
    check('selected full actual nine-factor parent morphism',all(v.q==1 and v>=0 for v in M))
    c['nine_factor_parent_monomial_map']=int_matrix(M)
    c['physical_weights']=list(map(int,N.inv()*s.Matrix([0,0,0,1])))
    c['point_to_theta_unit_exponents']=list(map(int,P.inv()*s.Matrix([0,0,0,1])))
    c['B_target_rays']=[selected_shift(v) for v in c['rays']]
    Nt=mat(c['B_target_rays'])
    c['B_source_unit_exponents']=list(map(int,Nt.inv()*s.Matrix([1,-1,0,0])))
    c['B_full_selected_Hom_unit_exponents']=list(map(int,Nt.inv()*s.Matrix([0,0,0,1])))
    c['original_marked_volume_orders']=[5*v[0]+4*v[1]+v[2]-1 for v in c['rays']]
    check('selected full original volume effective',all(v>=0 for v in c['original_marked_volume_orders']))
    c['sigma_exponents']=[v[0]+v[1] for v in c['rays']]
    c['q_exponents']=[v[2] for v in c['rays']]
selected_q_unit={key(f) for c in selected_fan for f in combinations(c['rays'],3) if all(v[2]==0 for v in f)}
check('selected q-unit restriction is literally same common3',selected_q_unit=={key(selected_embed(v) for v in c['rays']) for c in fan3})
check('selected full thirty-nine charts',len(selected_fan)==39)

def encode(v):
    if isinstance(v,F):return [v.numerator,v.denominator]
    if isinstance(v,(tuple,list)):return [encode(a) for a in v]
    if isinstance(v,dict):return {k:encode(a) for k,a in v.items()}
    return v
out={'status':'PASS','utc':datetime.now(timezone.utc).isoformat(),'checks':len(TESTS),
 'scope':'Actual common refinement of both factor orders, with exact parent invariant-ring morphisms, physical/source/full-Hom unit arrows, periodic faces, and native chi-ray mu4 quotient extension. No global compact assembly or return is assigned.',
 'slice':'eta+v=1, 0<=V<=4','three_dimensional_lattice':['eta','v','V_phys'],
 'four_dimensional_quotient_characters':['chi^4','chi*eta','v','V_phys'],
 'parent_factors':{'alternating':['eta','v']*4,'grouped':['eta']*4+['v']*4},
 'full_point_frame_arrow':'For selected period j, U_selected=q^(-j)*psi*(eta*v)^(-4j)*V_phys. The parent vertical unit rows act on q^(-j)*psi; the inverse arrow retains q^j*psi^(-1).',
 'full_B_arrow':'(eta,v,V)->(eta*c_b,v/c_b,CalC*(eta*v)^4*V), CalC=lambda*H*mathcalB. In quotient characters use T3->CalC*T1^4*T2^4*T0^(-1)*T3; all c_b and CalC unit powers are saved.',
 'original_marked_volume':'8*eta^4*v^3*d^(-2)*u*Omega_loc, character(-1,5,4,0); the full source derivative satisfies u_source=u_target*c_b*J_b.',
 'parents3':parents,'cells':cells,'initial3_cones':initial3,'regular3_cones':fan3,'stellar3_history':hist3,'faces3':faces3,
 'parents4':invariants4,'initial4_cones':initial4,'regular4_cones':fan4,'stellar4_history':hist4,'faces4':faces4,
 'selected_full_lattice':['eta','v','q','V_theta'],
 'selected_full_parent_factors':['eta']*4+['v']*4+['q'],
 'selected_full_parents':selected_parents,'selected_full_regular_cones':selected_fan,
 'selected_full_period_lower_faces':sorted(selected_lower),'selected_full_period_upper_faces':sorted(selected_upper),
 'selected_full_volume':'8*eta^4*v^3*d^(-2)*u*(partial chi/partial q)*deta wedge dv wedge dq wedge dlog V_theta; logarithmic character(5,4,1,0). Full derivative unit is retained.',
 'selected_full_Hom_unit':'C_selected=lambda*beta/kappa, beta=mathcalB*psi(T_b p)/psi(p); q=kappa*H. The physical selected period is V_theta->C_selected*(eta*v)^4*q*V_theta.',
 'counts':{'overlay_cells':len(cells),'overlay_vertices':len(vertices),'initial3_cones':len(initial3),'regular3_cones':len(fan3),'stellar3_steps':len(hist3),'initial4_cones':len(initial4),'regular4_cones':len(fan4),'stellar4_steps':len(hist4),'selected_full_regular_cones':len(selected_fan)},
 'seconds':round(time.monotonic()-START,3)}
Path(__file__).with_suffix('.json').write_text(json.dumps(encode(out),indent=2)+'\n')
print(json.dumps({k:out[k] for k in ('status','utc','checks','scope','counts','seconds')},indent=2))
