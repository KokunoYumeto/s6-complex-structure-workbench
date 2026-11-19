"""Full fixed-inner characteristic pairs, with the moving clutch left typed.

Recompute surface normal moments and curve degrees from actual full cone
matrices with a fresh auxiliary circle. No finite-group residue is lifted.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import sympy as S

ROOT=Path(__file__).resolve().parents[2]
paths={
 'stars':'code/part3_fourfold/e6_selected_infinity_compact_surface_stars.json',
 'faces':'code/part3_fourfold/e6_fixed_face_orbits.json',
 'interface':'code/part3_fourfold/e6_selected_infinity_curve_clutch.json',
 'strict':'code/part3_fourfold/e6_selected_infinity_strict_surfaces.json',
 'moving':'code/part3_root/e6_selected_infinity_moving_cap.json'}
data={k:json.loads((ROOT/v).read_text()) for k,v in paths.items()}
checks=[]


def ck(value,label):
    assert bool(value),label
    checks.append(label)


def pair_point(w):
    product=S.prod(w)
    return (S.Rational(1,product),S.Rational(sum(a*a for a in w),product))


def pair_curve(w,d):
    product=S.prod(w)
    ratio=sum(S.Rational(b,a) for a,b in zip(w,d))
    return (-ratio/product,(2*sum(a*b for a,b in zip(w,d))-sum(a*a for a in w)*ratio)/product)


def pair_surface(aa,ab,bb,p1):
    return (-(aa-ab+bb),-(p1+aa+2*ab+bb))


def expr(pair):
    return S.cancel((4*pair[0]-pair[1])/24)


def add(rows):
    return tuple(sum(row[i] for row in rows) for i in range(2))


def ser(pair):
    return list(map(str,pair))


delta=S.Matrix([0,0,0,1])
charts={}
for row in data['stars']['charts']:
    N=S.Matrix.hstack(*(S.Matrix(r) for r in row['rays']))
    inv=N.inv()
    ck(abs(N.det())==1,'full quotient chart regular over integral lattice')
    weight=inv*delta
    ck(list(weight)==row['physical_weights'],'actual physical weights from inverse chart matrix')
    charts[(row['kind'],row['label'])]={'N':N,'inverse':inv,'rays':row['rays'],
                                     'weights':weight}

# A fresh actual auxiliary cocharacter, selected by exact nonvanishing.
for candidate in ([5,13,29,53],[7,19,43,101],[11,31,97,307]):
    auxiliary=S.Matrix(candidate)
    nonzero=True
    for row in data['stars']['surfaces']:
        for key in row['charts']:
            c=charts[tuple(key)]
            v=c['inverse']*auxiliary
            nonzero &= all(v[i]!=0 for i,w in enumerate(c['weights']) if w==0)
    if nonzero:
        break
ck(nonzero,'fresh auxiliary circle has isolated surface vertices')

surface_rows=[]
surface_pairs={'exceptional':[],'refinement':[]}
for row in data['stars']['surfaces']:
    aa=ab=bb=p1=S.Integer(0)
    vertices=[]
    for key in row['charts']:
        c=charts[tuple(key)]
        v=c['inverse']*auxiliary
        tang=[i for i,w in enumerate(c['weights']) if w==0]
        neg=[i for i,w in enumerate(c['weights']) if w==-1]
        pos=[i for i,w in enumerate(c['weights']) if w==1]
        ck(len(tang)==2 and len(neg)==len(pos)==1,'surface actual tangent/negative/positive split')
        t1,t2=[v[i] for i in tang]
        a,b=v[neg[0]],v[pos[0]]
        denom=t1*t2
        aa+=a*a/denom;ab+=a*b/denom;bb+=b*b/denom
        p1+=(t1*t1+t2*t2)/denom
        vertices.append({'chart':key,'tangent':list(map(str,[t1,t2])),
                         'normal_negative_positive':list(map(str,[a,b]))})
    ck(aa-2*ab+bb==S.Rational(row['D_square']),f'surface{row["id"]}: full moments recover actual D square')
    ck(p1==S.Rational(row['p1']),f'surface{row["id"]}: fresh tangent number')
    pair=pair_surface(aa,ab,bb,p1)
    ck(expr(pair)==S.Rational(row['positive_u']),f'surface{row["id"]}: full pair recovers scoped polynomial')
    kind='exceptional' if 'v_unit' in row['type'] else 'refinement'
    surface_pairs[kind].append(pair)
    surface_rows.append({'id':row['id'],'kind':kind,'normal_squares_mixed':ser((aa,ab))+[str(bb)],
                         'p1':str(p1),'pair_U':ser(pair),'vertices':vertices})

ordinary=data['faces']['selected_ordinary_overlay']
interior_pairs=[];interior_rows=[]
for row in ordinary['components']:
    if row['tag']!='interior':
        continue
    w=list(map(S.Integer,row['normal_weights']))
    if row['dimension']==0:
        pair=pair_point(w)
        degrees=None
    else:
        ck(row['dimension']==1,'interior components have dimension zero or one')
        occurrence=row['face_occurrences'][0]
        ids=occurrence['charts']
        ck(len(ids)==2,'actual compact interior curve has two source charts')
        face=row['canonical_face']
        ends=[]
        for index in ids:
            c=charts[('resolved_infinity',index)]
            vv=c['inverse']*auxiliary
            tangent=[i for i,wi in enumerate(c['weights']) if wi==0]
            ck(len(tangent)==1,'curve has one actual tangent coordinate')
            tau=vv[tangent[0]]
            ck(tau!=0,'fresh auxiliary curve tangent nonzero')
            normals=[vv[c['rays'].index(ray)] for ray in face]
            ends.append((tau,normals))
        ck(ends[0][0]==-ends[1][0],'two exact curve tangent weights are opposite')
        degrees=[S.cancel((a-b)/ends[0][0]) for a,b in zip(ends[0][1],ends[1][1])]
        ck(degrees==row['normal_degrees'],'fresh full-matrix curve degrees match the normal clutch')
        pair=pair_curve(w,degrees)
    ck(expr(pair)==S.Rational(row['local_positive_hyperplane_residue']),'interior full pair recovers the fixed-inner polynomial')
    interior_pairs.append(pair)
    interior_rows.append({'id':row['id'],'dimension':row['dimension'],'weights':list(map(str,w)),
                          'degrees':None if degrees is None else list(map(str,degrees)),
                          'pair_U':ser(pair)})
ck(len(interior_rows)==124,'complete106-point and18-curve interior ledger')

curve_rows=[]
curve_pairs={'p_curves':[],'interface':[]}
for label,rows,value_key in (
    ('p_curves',data['stars']['p_curves'],'positive_u'),
    ('interface',data['interface']['curves'],'positive_u_residue')):
    for row in rows:
        w=list(map(S.Integer,row['normal_weights']))
        deg=list(map(S.Integer,row['normal_degrees']))
        pair=pair_curve(w,deg)
        ck(expr(pair)==S.Rational(row[value_key]),f'{label} curve{row["id"]}: full pair')
        curve_pairs[label].append(pair)
        curve_rows.append({'type':label,'id':row['id'],'weights':list(map(str,w)),
                           'degrees':list(map(str,deg)),'pair_U':ser(pair)})

# The two independent A3 boundary lifts are applied to each signed line.
I=S.Matrix([[-2,1,0],[1,-2,1],[0,1,-2]])
A3minus=[S.Matrix(v) for v in ([1,0,0],[1,-1,1],[0,0,1],[0,0,0])]
strict_rows=[];strict_pairs=[]
for j in range(4):
    aa0=S.Integer(0)
    ab=S.Rational((j+1)*(4-j),2)
    bb0=S.Rational(j*j,2)-8
    dminus=A3minus[j]
    a3=(dminus.T*I.inv()*dminus)[0]
    # MF2c-e: odd j has positive odd line; even j has negative odd line.
    aa=aa0+2*a3-(S.Rational(1,2) if j%2==0 else 0)
    bb=bb0-(S.Rational(1,2) if j%2==1 else 0)
    ck(aa-2*ab+bb==S.Rational(data['strict']['surfaces'][j]['resolved_D_square']),
       f'strict{j}: separate full A3/A1 line comparisons recover D square')
    pair=pair_surface(aa,ab,bb,-24)
    ck(expr(pair)==S.Rational(data['strict']['surfaces'][j]['positive_u_surface']),
       f'strict{j}: separate pair has prescribed source polynomial')
    strict_pairs.append(pair)
    strict_rows.append({'j':j,'orbifold_squares_mixed':list(map(str,[aa0,ab,bb0])),
                        'A3_negative_degrees':list(map(int,dminus)),
                        'each_A3_negative_square_change':str(a3),
                        'A1_nonzero_degree_line':'positive' if j%2 else 'negative',
                        'resolved_squares_mixed':list(map(str,[aa,ab,bb])),
                        'pair_U':ser(pair)})
mu2=tuple(4*x for x in pair_point([2,-1,-1,-1]))
subtotals={
 'strict_once':add(strict_pairs),
 'mu2_points_once':mu2,
 'interior_per_copy':add(interior_pairs),
 'exceptional_per_copy':add(surface_pairs['exceptional']),
 'refinement_per_copy':add(surface_pairs['refinement']),
 'p_curves_per_copy':add(curve_pairs['p_curves']),
 'interface_per_copy':add(curve_pairs['interface'])}
fixed_before_moving=add([subtotals['strict_once'],subtotals['mu2_points_once']]+[
 tuple(2*x for x in v) for k,v in subtotals.items() if k.endswith('_per_copy')])
c2c=S.Symbol('c2_actual_moving_clutch',integer=True)
moving=(c2c,6+4*c2c)
fixed_with_moving=add([fixed_before_moving,moving])
ck(expr(moving)==-S.Rational(1,4),'moving MC expression retains actual unspecified c2')
ck(expr(fixed_with_moving)==-1,'complete fixed-inner polynomial from exact pieces')
ck(S.diff(expr(fixed_with_moving),c2c)==0,'no free clutch integer selected from the sum')
out={'status':'PASS_FULL_FIXED_INNER_PAIR_LEDGER','utc':datetime.now(timezone.utc).isoformat(),
 'checks':len(checks),'check_labels':checks,
 'proof_sha256':hashlib.sha256((ROOT/'notes/part3_e6_selected_infinity_full_pair_ledger_working.md').read_bytes()).hexdigest(),
 'inputs':{k:{'path':v,'sha256':hashlib.sha256((ROOT/v).read_bytes()).hexdigest()} for k,v in paths.items()},
 'chart_inverse_maps':[{'chart':list(key),'inverse':[[int(t) for t in row] for row in value['inverse'].tolist()]} for key,value in charts.items()],
 'auxiliary':list(map(int,auxiliary)),'surface_rows':surface_rows,'interior_rows':interior_rows,
 'curve_rows':curve_rows,'strict_rows':strict_rows,
 'U_subtotals':{k:ser(v) for k,v in subtotals.items()},
 'U_before_moving':ser(fixed_before_moving),'U_moving':ser(moving),
 'U_with_actual_moving_clutch':ser(fixed_with_moving),
 'U_fixed_inner_expression':str(expr(fixed_with_moving)),
 'scope':'Complete fixed-inner characteristic ledger with exact source multiplicities; the actual moving c2 and the outer parameter/reference/physical transfer are separate unassigned calculations.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ('check_labels','surface_rows','interior_rows','curve_rows','strict_rows','chart_inverse_maps')},indent=2))
