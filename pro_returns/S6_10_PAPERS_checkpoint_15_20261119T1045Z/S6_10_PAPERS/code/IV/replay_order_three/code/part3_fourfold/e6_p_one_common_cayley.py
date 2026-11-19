"""Actual p-one four-dimensional lift of the full generic common fan.

Retains all native source/period/Cartier characters. In particular
b=(p-1)^-4 c^-1 is substituted before any corner extension.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations
from collections import Counter
from copy import deepcopy
from datetime import datetime,timezone
import hashlib,json
import sympy as S

base=Path(__file__).resolve().parents[2]
commonpath=base/'code/part3_root/e6_common_period_fan.json'
common=json.loads(commonpath.read_text())
labels=[]
def ck(value,name):
    assert value,name
    labels.append(name)
def mat(rays):return S.Matrix.hstack(*map(S.Matrix,rays))
def ints(M):return [[int(z) for z in row] for row in M.tolist()]
def key(rays):return tuple(sorted(map(tuple,rays)))
def orient(rays):
    rays=list(map(tuple,rays));D=int(mat(rays).det())
    assert abs(D)==1
    perm=list(range(len(rays)))
    if D<0:rays[0],rays[1]=rays[1],rays[0];perm[0],perm[1]=perm[1],perm[0]
    return rays,perm
def area(rays):return F(abs(int(mat(rays).det())),2*int(rays[0][2])*int(rays[1][2])*int(rays[2][2]))
def volume(rays):
    out=F(abs(int(mat(rays).det())),6)
    for ray in rays:out/=ray[2]+ray[3]
    return out
E=lambda r:(0,r,0,1)
nativeparents={}
for cell in range(3):
    I=lambda r:(cell+1,r,1,0)
    J=lambda r:(cell,r,1,0)
    for k in range(3):
        nativeparents[f'{cell}:x:{k}']={'rays':[I(k+1),I(k),J(0),E(0)],'free_coordinate_order':['a','b','y','v']}
        nativeparents[f'{cell}:y:{k}']={'rays':[I(3),J(k+1),J(k),E(0)],'free_coordinate_order':['x','a','b','v']}
    for k in range(4):
        nativeparents[f'{cell}:v:{k}']={'rays':[I(3),J(3),E(k+1),E(k)],'free_coordinate_order':['x','y','a','b']}

upper={}
for number,item in enumerate(common['cones']):
    parent=common['parent_one_instances'][item['one_parent']]
    r,s=parent['shift']
    native=[]
    for A,B,h in item['rays']:
        A-=(5*r+s)*h;B-=(r+2*s)*h
        native.append((B,A+B,h))
    ck(abs(int(mat(native).det()))==1,f'upper{number} regular integral native map')
    pn=f"{parent['source_cell']}:{parent['kind']}:{parent['k']}"
    # Full map (Z,W_C,P,v) to (Vreg,Zcommon,P,v), after b=v^-4 c^-1.
    full=S.Matrix([[-1,1,5*r+s,4*(2*r+s)],
                   [1,0,r+2*s,0],[0,0,1,0],[0,0,0,1]])
    pp=[-6-3*r-3*s,r+s,0,0]
    cc=[2*r+s,0,0,0]
    ck(abs(int(full.det()))==1,f'upper{number} full corner character inverse')
    for n,ray in enumerate(native):
        ck(list(full*S.Matrix(list(ray)+[0]))==list(item['rays'][n])+[0],f'upper{number} exact shifted ray{n}')
    rec=upper.setdefault(key(native),{'rays':native,'parent':pn,'generic_references':[]})
    ck(rec['parent']==pn,f'upper{number} consistent source-cell parent')
    rec['generic_references'].append({'common_cone':number,'one_parent':item['one_parent'],
        'period_shift':[r,s],'full_corner_character_matrix':ints(full),
        'p_unit_exponents':pp,'c_unit_exponents':cc,
        'retained_corner_factor':'b=v^-4 c^-1'})
ck(sum((area(u['rays']) for u in upper.values()),F(0))==9,'complete upper area9')

cones=[]
for rec in upper.values():
    raw=[E(0)]+[tuple(ray)+(0,) for ray in rec['rays']]
    rays,permutation=orient(raw)
    cones.append({'rays':rays,'raw_order_permutation':permutation,
        'parent':rec['parent'],'kind':'upper_star','generic_references':deepcopy(rec['generic_references'])})

edge_records=[]
for cell in range(3):
    pairs={}
    for rec in upper.values():
        for edge in combinations(rec['rays'],2):
            if all(w==3*h and cell*h<=z<=(cell+1)*h for z,w,h in edge):
                er=pairs.setdefault(key(edge),{'rays':list(edge),'generic_references':[]})
                er['generic_references'].extend(rec['generic_references'])
    ck(bool(pairs),f'cell{cell} nonempty upper-edge refinement')
    # Exact interval lengths show that these edges cover the entire old edge once.
    length=F(0)
    for er in pairs.values():
        a,b=er['rays'];length+=abs(F(a[0],a[2])-F(b[0],b[2]))
        ck(abs(a[0]*b[2]-b[0]*a[2])==1,f'cell{cell} primitive upper-edge lattice')
    ck(length==1,f'cell{cell} full top-edge length1')
    edge_records.append({'source_cell':cell,'edge_count':len(pairs),'edges':list(pairs.values())})
    for k in range(4):
        for er in pairs.values():
            raw=[E(k),E(k+1)]+[tuple(ray)+(0,) for ray in er['rays']]
            rays,permutation=orient(raw)
            cones.append({'rays':rays,'raw_order_permutation':permutation,
                'parent':f'{cell}:v:{k}','kind':'lower_interval',
                'generic_references':deepcopy(er['generic_references'])})

ck(len({key(x['rays']) for x in cones})==len(cones),'no duplicated four-cones')
for n,co in enumerate(cones):
    N=mat(co['rays']);Np=mat(nativeparents[co['parent']]['rays'])
    arrow=Np.inv()*N
    ck(N.det()==1,f'cone{n} oriented determinant1')
    ck(all(x.is_Integer and x>=0 for x in arrow),f'cone{n} parent semigroup')
    weights=N.inv()*S.Matrix([0,1,0,0])
    ck(all(x.is_Integer for x in weights),f'cone{n} actual physical weights')
    zexp=[r[0] for r in co['rays']]
    wexp=[3*r[2]-r[0] for r in co['rays']]
    ck(min(zexp+wexp)>=0,f'cone{n} full source chart Z,Q/Z')
    co.update(parent_monomial_matrix=ints(arrow),dual_characters=ints(N.inv()),
        physical_weights=list(map(int,weights)),
        base_multiplicities={'P':[r[2] for r in co['rays']],'v':[r[3] for r in co['rays']]},
        original_canonical_orders=[2*r[2]+r[3]-1 for r in co['rays']],
        source_projection={'Z_exponents':zexp,'Q_over_Z_exponents':wexp,'Q_over_Z_p_unit':1},
        point_line={'identity':'P^3 W_C=p U6 f_(p^-2)(Z) v_M','retained_P_divisor':3})
    # The generic character arrow includes all period/source scalars, even where
    # their v powers are nonzero. It is never stored as a bounded b unit.
    for ref in co['generic_references']:
        full=S.Matrix(ref['full_corner_character_matrix'])
        ref['chart_common_character_exponents']=ints(full*N)
        ck(all(z.is_Integer for z in full*N),f'cone{n} exact common character exponents')

# Recheck the persisted records independently of the construction loop. Shared
# upper-edge reference records must never overwrite another cone's matrix.
for n,co in enumerate(cones):
    for ref in co['generic_references']:
        ck(ref['chart_common_character_exponents']==ints(S.Matrix(ref['full_corner_character_matrix'])*mat(co['rays'])),
           f'cone{n} independent stored full-character matrix')

for pn,pa in nativeparents.items():
    ck(sum((volume(co['rays']) for co in cones if co['parent']==pn),F(0))==volume(pa['rays']),f'parent{pn} exact full support volume')

inc=Counter(key(face) for co in cones for face in combinations(co['rays'],3))
ck(all(n in (1,2) for n in inc.values()),'all four-dimensional facet incidences1or2')
boundary={f for f,n in inc.items() if n==1}
generic={f for f in boundary if all(ray[3]==0 for ray in f)}
ck(len(generic)==len(upper),'full generic common boundary510')
other=boundary-generic
H=S.Matrix([[1,0,3,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
B=S.Matrix([[1,0,-1,0],[0,1,3,4],[0,0,1,0],[0,0,0,1]])
ck(H*B==B*H,'full native h/B matrices commute')
facets=[]
for f in sorted(other):
    partners=[]
    for r in (-1,0,1):
        for s in (-1,0,1):
            if not(r or s):continue
            T=H**r*B**s
            target=key([tuple(map(int,T*S.Matrix(ray))) for ray in f])
            if target in other:partners.append({'word_h':r,'word_B':s,'target':target})
    ck(bool(partners),'every nongeneric facet has its full period partner')
    facets.append({'face':f,'partners':partners})

# Whole chart overlaps along each paired facet, with actual p and c units.
owner={f:[n for n,co in enumerate(cones) if set(f).issubset(set(co['rays']))] for f in other}
period_maps=[]
for rec in facets:
    f=rec['face'];source_index=owner[f][0];source_cone=cones[source_index];Ns=mat(source_cone['rays'])
    for pmap in rec['partners']:
        r,s=pmap['word_h'],pmap['word_B'];target_index=owner[pmap['target']][0]
        Nt=mat(cones[target_index]['rays']);T=H**r*B**s
        arrow=Nt.inv()*T*Ns
        facecols=[n for n,ray in enumerate(source_cone['rays']) if ray in f]
        ck(all(arrow[row,col]>=0 for row in range(4) for col in facecols),'period overlap localized semigroup')
        ck(all(z.is_Integer for z in arrow),'period overlap integral chart inverse')
        pu=Nt.inv()*S.Matrix([r,-2*r,0,0]);cu=Nt.inv()*S.Matrix([0,s,0,0])
        ck(all(z.is_Integer for z in list(pu)+list(cu)),'full p/c period unit lift')
        period_maps.append({'source_cone':source_index,'target_cone':target_index,
            'word_h':r,'word_B':s,'monomial_matrix':ints(arrow),
            'p_unit_exponents':list(map(int,pu)),'c_unit_exponents':list(map(int,cu)),
            'invertible_source_columns':[n for n in range(4) if n not in facecols]})

source=base/'notes/part3_e6_p_one_cayley_working.md'
out={'status':'PASS_P_ONE_COMMON_CAYLEY','utc':datetime.now(timezone.utc).isoformat(),
    'generic_input_sha256':hashlib.sha256(commonpath.read_bytes()).hexdigest(),
    'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
    'check_count':len(labels),'check_labels':labels,'upper_cones':len(upper),
    'regular_four_cones':len(cones),'top_edge_counts':[r['edge_count'] for r in edge_records],
    'native_lattice':['Z','W_C','P','v'],'parents':nativeparents,'cones':cones,
    'edge_refinements':edge_records,'facet_incidence':dict(Counter(inc.values())),
    'generic_boundary_facets':len(generic),'period_boundary_facets':len(other),
    'period_facets':facets,'full_period_chart_maps':period_maps,
    'period_matrices':{'h':ints(H),'B':ints(B)},
    'scope':'Exact p1 common upper fan Cayley extension, native factor parents, all support volumes, generic/shared/full-period facets, actual source maps and p,c,v character arrows. Original point-line P^3 factor and canonical orders retained.',
    'unassigned':'The point/O coincidence graph, global compact end attachment, Spin extension and characteristic return.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ('status','check_count','upper_cones','regular_four_cones','top_edge_counts','generic_boundary_facets','period_boundary_facets')},indent=2))
