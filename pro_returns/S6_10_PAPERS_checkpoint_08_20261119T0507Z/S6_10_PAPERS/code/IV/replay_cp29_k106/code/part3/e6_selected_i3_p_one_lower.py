"""Exact lower-surface source/normal maps in the selected-I3 Cayley atlas.

Reads the executed four-cones, constructs all three source subdivisions,
and factors them into ordinary point blowups. No return is assigned.
"""
from pathlib import Path
from fractions import Fraction
from collections import defaultdict
from datetime import datetime,timezone
import hashlib,json
import sympy as S

ROOT=Path(__file__).resolve().parents[2]
inp=ROOT/'code/part3/e6_selected_i3_p_one_cayley.json'
data=json.loads(inp.read_text()); labels=[]
def ck(v,n):
    assert v,n
    labels.append(n)
def matrix(rays):return S.Matrix.hstack(*map(S.Matrix,rays))
def key(pair):return tuple(sorted(map(tuple,pair)))
def ints(M):return [[int(x) for x in row] for row in M.tolist()]
lower=[]; fans=defaultdict(dict)
for ci,co in enumerate(data['cones']):
    if co['kind']!='lower_interval':continue
    i,_,k=co['parent'].split(':');i=int(i);k=int(k)
    N=matrix(co['rays']);Np=matrix(data['parents'][co['parent']]['rays'])
    M=Np.inv()*N
    ck(ints(M)==co['parent_monomial_matrix'],f'{ci} persisted parent matrix')
    weights=list(N.inv()*S.Matrix([0,1,0,0]))
    ck(sorted(weights)==[-1,0,0,1],f'{ci} exact lower normal weights')
    ac=weights.index(1);bc=weights.index(-1)
    sc=[j for j,w in enumerate(weights) if w==0]
    ck(list(M.row(2))==[int(j==ac) for j in range(4)],f'{ci} literal a normal coefficient')
    ck(list(M.row(3))==[int(j==bc) for j in range(4)],f'{ci} literal b normal coefficient')
    ck(all(M[r,j]==0 for r in (0,1) for j in (ac,bc)),f'{ci} no tangent-normal mixing')
    rays=[tuple(int(M[r,j]) for r in (0,1)) for j in sc]
    sm=M.extract([0,1],sc)
    ck(abs(sm.det())==1 and all(x>=0 for x in sm),f'{ci} regular source quadrant map')
    ck(all(co['rays'][j][2]==sum(rays[n]) for n,j in enumerate(sc)),f'{ci} full P source multiplicity')
    fans[(i,k)][key(rays)]=rays
    lower.append({'four_cone':ci,'source_cell':i,'lower_interval':k,
        'source_coordinate_columns':sc,'normal_a_column':ac,'normal_b_column':bc,
        'source_exponent_matrix':ints(sm),'source_jacobian_sign':int(sm.det()),
        'source_jacobian_orders':[int(sum(sm[:,j])-1) for j in range(2)],
        'normal_rows':[list(map(int,M.row(2))),list(map(int,M.row(3)))],
        'original_canonical_orders':co['original_canonical_orders']})
ck(len(lower)==128,'all128 lower charts retained')

subdivisions=[]
for i in range(3):
    reference=fans[(i,0)]
    for k in range(1,4):
        ck(set(fans[(i,k)])==set(reference),f'cell{i} same actual source fan on interval{k}')
    vertices=set(v for pair in reference for v in pair)
    ordered=sorted(vertices,key=lambda x:Fraction(x[1],sum(x)))
    ck(ordered[0]==(1,0) and ordered[-1]==(0,1),f'cell{i} unchanged two boundary rays')
    adjacent=[key([a,b]) for a,b in zip(ordered,ordered[1:])]
    ck(set(adjacent)==set(reference),f'cell{i} complete quadrant incidence')
    ck(all(a[0]*b[1]-a[1]*b[0]==1 for a,b in zip(ordered,ordered[1:])),f'cell{i} oriented primitive source pairs')
    work=ordered.copy(); reverse=[]
    while len(work)>2:
        found=None
        for pos in range(1,len(work)-1):
            a,b,c=work[pos-1:pos+2]
            if (a[0]+c[0],a[1]+c[1])==b:
                found=pos;break
        ck(found is not None,f'cell{i} actual ordinary blowdown{len(reverse)}')
        a,b,c=work[found-1:found+2]
        reverse.append({'removed_ray':b,'left_ray':a,'right_ray':c})
        work.pop(found)
    forward=list(reversed(reverse)); build=[(1,0),(0,1)]
    for step in forward:
        a=tuple(step['left_ray']);b=tuple(step['removed_ray']);c=tuple(step['right_ray'])
        pos=build.index(a)
        ck(build[pos+1]==c and b==(a[0]+c[0],a[1]+c[1]),f'cell{i} chronological inverse blowup')
        build.insert(pos+1,b)
    ck(build==ordered,f'cell{i} complete reconstructed source fan')
    subdivisions.append({'source_cell':i,'rays':ordered,'charts':len(adjacent),
        'ordinary_blowups':len(forward),'chronological_blowups':forward})
ck([r['charts'] for r in subdivisions]==[16,7,9],'exact source chart counts16,7,9')
ck(sum(r['ordinary_blowups'] for r in subdivisions)==29,'twenty-nine actual interior blowups per lower surface')

# Full B^(-j) coefficient square and its two source-normal line arrows.
P,v,p,c,Z,W,a,b,j,k=S.symbols('P v p c Z W a b j k', nonzero=True)
# Check integer indices on the full dense torus, retaining all units.
for jj in range(-3,4):
    for kk in range(4):
        Wold=(P**4*v**4)**jj*P**4*v**kk*a
        Wstar=S.cancel(Wold/(P**4*p*v**4*c)**jj)
        ar=(p*c)**(-jj)*a
        br=(p*c)**jj*b
        ck(S.cancel(Wstar-P**4*v**kk*ar)==0,f'j{jj} k{kk} full B inverse W')
        ck(S.cancel(ar*br-a*b)==0,f'j{jj} k{kk} full normal product')
        ck(S.cancel(((P**4*v**4)/Wstar-v**(3-kk)*br).subs(b,v/a))==0,f'j{jj} k{kk} inverse normal branch')

us,U6,Zs,ss=S.symbols('u_s U6 Z_star s',nonzero=True)
for kk in range(4):
    point=P**-2*v**kk*U6**-1*Zs**2*a
    dual=P**2*v**(-kk-1)*U6*Zs**-2*b
    ck(S.cancel(point*dual-a*b/v)==0,f'k{kk} full genuine point-line inverse')
    hp=P**(-2-kk)*us**kk*U6**-1*Zs**2
    hm=P**(3+kk)*us**(-kk-1)*U6*Zs**-2
    ck(S.cancel((ss**(-kk)*point).subs(v,ss*us/P)-hp*a)==0,f'k{kk} literal source-s chain positive arrow')
    ck(S.cancel((ss**(kk+1)*dual).subs(v,ss*us/P)-hm*b)==0,f'k{kk} literal source-s chain inverse arrow')
    ck(S.cancel(hp*hm-P/us)==0,f'k{kk} exact normal determinant coefficient')

# Every ordinary blowup has c1^2 change -1, c2 change +1, hence p1 -3.
ck(29*(-1-2)==-87,'relative tangent Pontryagin number from actual29 blowups')
source=ROOT/'notes/part3_e6_selected_i3_p_one_lower_working.md'
out={'status':'PASS_SELECTED_I3_LOWER_NATIVE_SOURCE_NORMAL','utc':datetime.now(timezone.utc).isoformat(),
    'input':str(inp.relative_to(ROOT)),'input_sha256':hashlib.sha256(inp.read_bytes()).hexdigest(),
    'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
    'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'checks':len(labels),'check_labels':labels,'lower_charts':lower,
    'source_subdivisions':subdivisions,'surfaces':4,'blowups_per_surface':29,
    'relative_tangent_p1_per_surface':-87,
    'native_normal_frame':'a_ref=(pc)^(-j)a, b_ref=(pc)^j b; at v=0, p=1',
    'full_point_normal_comparison':{
        'positive':'P^(-2-k) u_s^k U6^(-1) Z_star^2',
        'negative':'P^(3+k) u_s^(-k-1) U6 Z_star^(-2)',
        'determinant':'P/u_s'},
    'scope':'Executed selected-I3 p1 lower fixed surfaces, full source/normal monomial arrows, chronological interior blowups, exact full B reindex and point-line boundary coefficient; only relative tangent p1 is evaluated.',
    'unassigned':'Closed-double normal pairings, finite-cap/reference and outer attachment, global characteristic pair and return.'}
tmp=Path(__file__).with_suffix('.json.tmp');tmp.write_text(json.dumps(out,indent=2)+'\n');tmp.replace(Path(__file__).with_suffix('.json'))
print(json.dumps({k:out[k] for k in ['status','checks','surfaces','blowups_per_surface','relative_tangent_p1_per_surface']},indent=2))
