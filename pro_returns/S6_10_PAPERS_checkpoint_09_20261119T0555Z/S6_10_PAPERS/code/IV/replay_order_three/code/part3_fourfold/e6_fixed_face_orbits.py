"""Exact physical fixed faces of the executed E6 corner refinements.

Only literal common faces and the stated full period maps are identified.
Every normal arrow retains the actual source/base units.  No normal Chern
number, completed compact attachment, or total return is assigned.
"""
from pathlib import Path
from itertools import combinations,product
from collections import Counter,defaultdict,deque
from datetime import datetime,timezone
from fractions import Fraction
import hashlib,json
import sympy as S
from sympy.matrices.normalforms import hermite_normal_form

ROOT=Path(__file__).resolve().parents[2]
checks=[]
def ck(v,msg):
    assert v,msg
    checks.append(msg)
def mat(rays):return S.Matrix.hstack(*map(S.Matrix,rays))
def il(M):return [[int(z) for z in row] for row in M.tolist()]
def key(rays):return tuple(sorted(map(tuple,rays)))
def mv(M,v):return tuple(sum(a*b for a,b in zip(row,v)) for row in M)
def mm(A,B):return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()

def extract(name,cones,delta,periods,units,tagger,dimension=4):
    """units[k][unit_name] is the full torus multiplier exponent vector."""
    n=len(delta);faces={};charts=[];inverses=[];matrices=[]
    incidence=defaultdict(list)
    for ci,co in enumerate(cones):
        rays=[tuple(r) for r in co['rays']];N=mat(rays);A=N.inv()
        ck(abs(N.det())==1,f'{name} cone{ci} regular')
        w=list(map(int,A*S.Matrix(delta)))
        ck(list(N*S.Matrix(w))==delta,f'{name} cone{ci} actual delta')
        if 'physical_weights' in co:ck(w==co['physical_weights'],f'{name} cone{ci} saved weights')
        nz=[i for i,z in enumerate(w) if z];zero=[i for i,z in enumerate(w) if not z]
        f=key(rays[i] for i in nz)
        weights=[w[rays.index(r)] for r in f]
        rec=faces.setdefault(f,{'rays':f,'normal_weights':weights,'charts':[],'dimension':dimension-len(f),'tag':tagger(f)})
        ck(rec['normal_weights']==weights,f'{name} cone{ci} shared-face normal weights')
        rec['charts'].append(ci)
        ch={'cone':ci,'minimal_face':f,'normal_columns':nz,'tangent_columns':zero,
            'physical_weights':w,'dual_characters':il(A),
            'actual_parent':{k:co[k] for k in ('parent','kind','alternating','grouped','common3') if k in co},
            'full_parent_maps':{k:co[k] for k in ('parent_monomial_matrix','generic_references','parent_invariant_monomial_maps','nine_factor_parent_monomial_map','point_to_theta_unit_exponents','original_canonical_orders','original_marked_volume_orders','source_projection','whole_cone_source_charts','point_line') if k in co}}
        charts.append(ch);matrices.append(N);inverses.append(A)
        for fa in combinations(rays,n-1):incidence[key(fa)].append(ci)
    ck(all(len(v)<=2 for v in incidence.values()),f'{name} exact facet incidence')
    for k,P in periods.items():ck(list(S.Matrix(P)*S.Matrix(delta))==delta,f'{name} period{k} physical orientation')
    pnames=list(periods);rank=len(pnames)
    words=[]
    for coeff in product((-1,0,1),repeat=rank):
        if not any(coeff):continue
        M=S.eye(n);uv={}
        for k,e in zip(pnames,coeff):
            M=M*S.Matrix(periods[k])**e
            for un,v in units[k].items():
                uv.setdefault(un,[0]*n)
                uv[un]=[a+e*b for a,b in zip(uv[un],v)]
        words.append((coeff,il(M),uv))
    graph=defaultdict(list);relations=[]
    for f,rec in faces.items():
        for word,P,uv in words:
            target=key(mv(P,r) for r in f)
            if target not in faces:continue
            permutation=[target.index(mv(P,r)) for r in f]
            ck(all(rec['normal_weights'][j]==faces[target]['normal_weights'][permutation[j]] for j in range(len(f))),f'{name} period normal permutation')
            graph[f].append((target,word));relations.append({'source':f,'target':target,'word':word,'permutation':permutation,'unit_vectors':uv})
    components=[];face_component={};potential={}
    for f in sorted(faces):
        if f in face_component:continue
        component=len(components);face_component[f]=component;potential[f]=(0,)*rank
        queue=deque([f]);members=[];cycles=[]
        while queue:
            a=queue.popleft();members.append(a)
            for b,w in graph[a]:
                target_p=tuple(x+y for x,y in zip(potential[a],w))
                if b not in face_component:
                    face_component[b]=component;potential[b]=target_p;queue.append(b)
                else:
                    ck(face_component[b]==component,f'{name} period orbit consistency')
                    z=tuple(x-y for x,y in zip(target_p,potential[b]))
                    if any(z):cycles.append(z)
        basis=[]
        if cycles:
            H=hermite_normal_form(S.Matrix.hstack(*map(S.Matrix,cycles)))
            basis=[list(map(int,H[:,j])) for j in range(H.cols)]
        dims={faces[a]['dimension'] for a in members};tags={faces[a]['tag'] for a in members}
        ck(len(dims)==1 and len(tags)==1,f'{name} orbit dimension and boundary tag')
        components.append({'id':component,'dimension':next(iter(dims)),'tag':next(iter(tags)),
            'canonical_face':f,'normal_weights':faces[f]['normal_weights'],
            'face_occurrences':[{'face':a,'period_from_canonical':potential[a],'charts':faces[a]['charts']} for a in members],
            'period_stabilizer_basis':basis})
    for ch in charts:ch['component']=face_component[ch['minimal_face']]

    # Complete local normal-coordinate arrows on common maximal-chart facets.
    normal_maps=[]
    for facet,owners in incidence.items():
        if len(owners)!=2:continue
        i,j=owners
        f=charts[i]['minimal_face']
        if f!=charts[j]['minimal_face'] or not set(f).issubset(facet):continue
        arrow=inverses[j]*matrices[i]
        source_normal=charts[i]['normal_columns'];target_normal=charts[j]['normal_columns']
        permutation=[]
        for k in target_normal:
            vals=[arrow[k,l] for l in source_normal]
            ck(vals.count(1)==1 and sum(abs(z) for z in vals)==1,f'{name} local normal linear arrow')
            permutation.append(source_normal[vals.index(1)])
        normal_maps.append({'source_cone':i,'target_cone':j,'shared_facet':facet,
            'monomial_matrix':il(arrow),'normal_target_rows':target_normal,
            'normal_source_permutation':permutation,
            'invertible_source_columns':[k for k,r in enumerate(cones[i]['rays']) if tuple(r) not in facet],
            'units':{}})

    # Normal arrows on dense component overlaps for every saved period relation.
    # Tangent coordinates are inverted on this explicitly specified overlap.
    period_normal_maps=[]
    for rel in relations:
        i=faces[rel['source']]['charts'][0];j=faces[rel['target']]['charts'][0]
        M=S.eye(n)
        for pn,e in zip(pnames,rel['word']):M=M*S.Matrix(periods[pn])**e
        arrow=inverses[j]*M*matrices[i]
        rows=charts[j]['normal_columns'];cols=charts[i]['normal_columns']
        for k in rows:
            vals=[arrow[k,l] for l in cols]
            ck(vals.count(1)==1 and sum(abs(z) for z in vals)==1,f'{name} period normal linear arrow')
        un={k:list(map(int,inverses[j]*S.Matrix(v))) for k,v in rel['unit_vectors'].items()}
        period_normal_maps.append({'source_cone':i,'target_cone':j,'word':rel['word'],
            'monomial_matrix':il(arrow),'unit_exponents':un,
            'normal_target_rows':rows,'normal_source_columns':cols,
            'invertible_source_columns':charts[i]['tangent_columns'],
            'normal_units_are_restricted_to_fixed_component':True})
    for rec in components:
        # These are chart-star assertions only. The line-graph/source refinements
        # remain separate input gates even when the toric star is interior.
        rec['toric_interior']=rec['tag']=='interior'
        rec['requires_external_boundary_map']=rec['tag']!='interior'
        if rec['toric_interior'] and rec['dimension']==0:
            w=rec['normal_weights'];prodw=1
            for z in w:prodw*=z
            r=Fraction(4-sum(z*z for z in w),24*prodw)
            rec['local_positive_hyperplane_residue']=str(r)
            rec['local_physical_M_residue']=str(-r)
        if rec['toric_interior'] and rec['dimension']==1:
            # A complete one-dimensional toric star has exactly two opposite
            # tangent rays. These are checked before its degree is evaluated.
            occ=[ci for fo in rec['face_occurrences'] for ci in fo['charts']]
            ck(len(occ)==2,f'{name} interior curve complete two-chart star')
            w=rec['normal_weights'];canonical=rec['canonical_face'];degrees=[]
            for aux in ([1,11,103,1009],[2,17,89,701]):
                deg=[Fraction(0) for _ in canonical];tw=[];vertex=[]
                for ci in occ:
                    ch=charts[ci];face=ch['minimal_face'];pv=potential[face]
                    T=S.eye(n)
                    for pn,e in zip(pnames,pv):T=T*S.Matrix(periods[pn])**e
                    av=inverses[ci]*T*S.Matrix(aux)
                    ti=ch['tangent_columns'];ck(len(ti)==1 and av[ti[0]]!=0,f'{name} curve auxiliary tangent nonzero')
                    tangent=int(av[ti[0]]);tw.append(tangent)
                    ns=[]
                    for j,ray in enumerate(canonical):
                        tr=tuple(map(int,T*S.Matrix(ray)));col=[tuple(r) for r in cones[ci]['rays']].index(tr)
                        nv=int(av[col]);deg[j]+=Fraction(nv,tangent);ns.append(nv)
                    vertex.append({'cone':ci,'tangent_weight':tangent,'normal_weights':ns})
                ck(tw[0]==-tw[1],f'{name} curve complete opposite tangent rays')
                ck(all(d.denominator==1 for d in deg),f'{name} exact normal degrees integral')
                degrees.append(deg)
                rec.setdefault('auxiliary_curve_checks',[]).append({'cocharacter':aux,'vertices':vertex,'degrees':list(map(str,deg))})
            ck(degrees[0]==degrees[1],f'{name} independent auxiliary normal-degree agreement')
            rec['normal_degrees']=list(map(int,degrees[0]));prodw=1
            for z in w:prodw*=z
            c=4-sum(z*z for z in w)
            r=-sum((Fraction(c,z)+2*z)*d for z,d in zip(w,degrees[0]))/(24*prodw)
            rec['local_positive_hyperplane_residue']=str(r)
            rec['local_physical_M_residue']=str(-r)
    return {'cones':len(cones),'minimal_faces_before_period':len(faces),'components':components,
        'charts':charts,'period_generators':periods,'full_period_units':units,
        'period_relations':relations,'local_normal_maps':normal_maps,'period_normal_maps':period_normal_maps,
        'summary':[{'dimension':d,'tag':tag,'count':c} for (d,tag),c in sorted(Counter((r['dimension'],r['tag']) for r in components).items())]},face_component

def corner_tag(face):
    if all(r[3]==0 for r in face):return 'generic_common_boundary'
    if all(r[2]==0 for r in face):return 'lower_boundary'
    return 'interior'
def selected_tag(face):
    # Actual nonnegative cover heights chi,eta,v in the quotient lattice.
    rows=((1,0,0,0),(-1,4,0,0),(0,0,1,0))
    missing=[n for n,row in zip(('chi_unit','eta_unit','v_unit'),rows) if all(sum(a*b for a,b in zip(row,r))==0 for r in face)]
    return '+'.join(missing) if missing else 'interior'
def selected_full_tag(face):
    missing=[n for i,n in enumerate(('eta_unit','v_unit','q_unit')) if all(r[i]==0 for r in face)]
    return '+'.join(missing) if missing else 'interior'

commonp=ROOT/'code/part3_root/e6_common_period_fan.json'
cp=json.loads(commonp.read_text())
K3=[[1,0,5],[0,1,1],[0,0,1]];J3=[[1,0,1],[0,1,2],[0,0,1]]
common,fcommon=extract('common',cp['cones'],[1,0,0],{'K':K3,'J':J3},
    {'K':{'p':[-3,1,0],'b':[-2,0,0]},'J':{'p':[-3,1,0],'b':[-1,0,0]}},lambda f:'common_base',dimension=4)

endsfile=ROOT/'code/part3/e6_common_corner_lift.json';ends=json.loads(endsfile.read_text())['ends']
onefile=ROOT/'code/part3_fourfold/e6_p_one_common_cayley.json';one=json.loads(onefile.read_text())
configs={
 'zero':(ends['zero']['cones'],[-1,1,0,0],ends['zero']['period_matrices'],
         {'H1':{'b':[-1,1,0,0]},'K0':{'b':[-6,6,0,0]}}),
 'one':(one['cones'],[0,1,0,0],one['period_matrices'],
        {'h':{'p':[1,-2,0,0]},'B':{'c':[0,1,0,0]}}),
 'infinity':(ends['infinity']['cones'],[1,0,0,0],{k:ends['infinity']['period_matrices'][k] for k in ('K','J')},
             {'K':{'f':[2,0,0,0]},'J':{'f':[1,0,0,0]}})}
outputs={}
for name,(cones,delta,periods,units) in configs.items():
    data,fcomp=extract(name,cones,delta,periods,units,corner_tag)
    generic_matches=defaultdict(set)
    for ch in data['charts']:
        co=cones[ch['cone']];face=ch['minimal_face']
        if not all(r[3]==0 for r in face):continue
        for ref in co.get('generic_references',[]):
            F=S.Matrix(ref.get('full_corner_character_matrix',ref.get('common_character_matrix')))
            mf=key(tuple(map(int,(F*S.Matrix(r))[:3])) for r in face)
            ck(mf in fcommon,f'{name} actual common minimal-face map')
            generic_matches[ch['component']].add(fcommon[mf])
    for comp,targets in generic_matches.items():ck(len(targets)==1,f'{name} full generic orbit consistency')
    data['generic_component_identifications']=[{'component':c,'common_component':next(iter(v))} for c,v in sorted(generic_matches.items())]
    ck(len(generic_matches)==len([c for c in data['components'] if c['tag']=='generic_common_boundary']),f'{name} every generic fixed component matched')
    ck(set(next(iter(x)) for x in generic_matches.values())==set(range(len(common['components']))),f'{name} all common fixed components attained')
    outputs[name]=data

overlayfile=ROOT/'code/part3/e6_selected_infinity_factor_overlay.json'
ov=json.loads(overlayfile.read_text())
B4=[[1,0,0,0],[0,1,0,0],[0,0,1,0],[-1,4,4,1]]
selected,_=extract('selected_ordinary_overlay',ov['regular4_cones'],[0,0,0,1],{'B':B4},
    {'B':{'c_b':[0,1,-1,0],'CalC':[0,0,0,1]}},selected_tag)
selected['copy_gluing']='The O and T source copies are exchanged by the actual B source arrow. The listed toric B relations carry this copy switch; exterior source-chart identifications remain explicit global inputs.'
selected['parent_json_sha256']=sha(overlayfile)
selected_full,_=extract('selected_full',ov['selected_full_regular_cones'],[0,0,0,1],
    {'B':[[1,0,0,0],[0,1,0,0],[0,0,1,0],[4,4,1,1]]},
    {'B':{'c_b':[1,-1,0,0],'C_selected':[0,0,0,1]}},selected_full_tag)
interface,fi=extract('selected_interface',ov['regular3_cones'],[0,0,1],
    {'B':[[1,0,0],[0,1,0],[4,4,1]]},
    {'B':{'c_b':[1,-1,0],'CalC':[0,0,1]}},lambda f:'q_chi_unit_interface',dimension=4)
for dataset,name,drop in ((selected,'ordinary',0),(selected_full,'selected',2)):
    ids=defaultdict(set)
    for ch in dataset['charts']:
        face=ch['minimal_face']
        if not all(r[drop]==0 for r in face):continue
        ff=key(tuple(z for i,z in enumerate(r) if i!=drop) for r in face)
        ck(ff in fi,f'{name} exact q-chi unit interface face')
        ids[ch['component']].add(fi[ff])
    ck(all(len(v)==1 for v in ids.values()),f'{name} interface orbit consistency')
    ck(set(next(iter(v)) for v in ids.values())==set(range(len(interface['components']))),f'{name} complete interface fixed set')
    dataset['interface_identifications']=[{'component':k,'interface_component':next(iter(v))} for k,v in sorted(ids.items())]

out={'status':'PASS_FIXED_FACE_ORBITS','utc':datetime.now(timezone.utc).isoformat(),
 'checks':len(checks),'check_labels':checks,
 'inputs':{str(p.relative_to(ROOT)):sha(p) for p in (commonp,endsfile,onefile,overlayfile)},
 'common':common,'three_ends':outputs,'selected_ordinary_overlay':selected,
 'selected_full':selected_full,'selected_interface':interface,
 'physical_line_convention':'The actual nonzero-vector line M has class -u when u is the positive hyperplane class in SZ57. Its cubic and p1-linear integrals both use that exact dual map. No total numerical residue is assigned by this face extraction.',
 'scope':'Exact minimal fixed faces, full period words and stabilizers, actual common510 identifications, all local normal monomials and full unit period normal maps. Boundary/source/point-line graph and compact global attachment remain required before a completed characteristic calculation.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
summary={'status':out['status'],'checks':len(checks),'common':common['summary'],
 'three_ends':{k:v['summary'] for k,v in outputs.items()},'selected_ordinary_overlay':selected['summary'],
 'selected_full':selected_full['summary'],'selected_interface':interface['summary']}
Path(__file__).with_name('e6_fixed_face_orbits_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
