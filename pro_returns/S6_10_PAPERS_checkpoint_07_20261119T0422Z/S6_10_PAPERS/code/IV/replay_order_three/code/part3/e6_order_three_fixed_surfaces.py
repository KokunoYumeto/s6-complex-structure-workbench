"""Full normal intersections of the 117 actual compact generic fixed surfaces.
All coefficients are read from the executed, full-unit three-end atlas.
Only this closed collection of inner faces is evaluated.
"""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
from datetime import datetime,timezone
import hashlib,json
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
paths={
 'faces':ROOT/'code/part3/e6_order_three_fixed_input.json',
 'generic':ROOT/'code/part3_root/e6_common_period_fan.json',
 'ends':ROOT/'code/part3/e6_common_corner_lift.json',
 'one':ROOT/'code/part3_fourfold/e6_p_one_common_cayley.json'}
face=json.loads(paths['faces'].read_text())
generic=json.loads(paths['generic'].read_text())['cones']
ends=json.loads(paths['ends'].read_text())['ends']
one=json.loads(paths['one'].read_text())
corners={'zero':ends['zero']['cones'],'one':one['cones'],'infinity':ends['infinity']['cones']}
periods={end:face['three_ends'][end]['period_generators'] for end in corners}
tests=[]
def ck(name,p):
    assert bool(p),name
    tests.append(name)
def mat(cols):return s.Matrix.hstack(*map(s.Matrix,cols))
def asints(v):
    ck('actual integral vector',all(x.q==1 for x in v))
    return list(map(int,v))
def tup(v):return tuple(map(int,v))
def transform(periods,word):
    M=s.eye(len(next(iter(periods.values()))))
    for name,power in zip(periods,word):M=M*s.Matrix(periods[name])**power
    return M
def rkey(v):return tuple(v)
common=face['common'];surfaces=[c for c in common['components'] if c['dimension']==2]
ck('exact common 117 surfaces',len(surfaces)==117)
# Actual section coordinate clutches, for all 510 complete common charts.
ref={end:{} for end in corners};section_records={}
for end,cones in corners.items():
    for ci,c in enumerate(cones):
        if c['kind']!='upper_star':continue
        lower=[s.Matrix(r) for r in c['rays'] if r[2]==0]
        ck(end+' single actual upper-star lower ray',len(lower)==1)
        for r in c['generic_references']:
            cid=r['common_cone']
            L=s.Matrix(r.get('full_corner_character_matrix',r.get('common_character_matrix')))
            ref[end][cid]={'lower_image':asints((L*lower[0])[:3]),'cone':ci,'reference':r}
    ck(end+' all510 upper-star reference arrows',len(ref[end])==510)
for cid,c in enumerate(generic):
    N=mat(c['rays']);w=asints(N.inv()*s.Matrix([1,0,0]))
    ck('saved physical weights exact',w==c['physical_weights'])
    orders={end:asints(N.inv()*s.Matrix(ref[end][cid]['lower_image'])) for end in corners}
    degrees=[-sum(orders[end][i] for end in corners) for i in range(3)]
    ck('every section full original canonical adjunction',sum(c['rays'][i][2]*degrees[i] for i in range(3))==-1)
    section_records[cid]={'weights':w,'orders':orders,'degrees':degrees,'end_maps':{end:ref[end][cid] for end in corners}}
endmatch={end:{v['common_component']:v['component'] for v in face['three_ends'][end]['generic_component_identifications']} for end in corners}
def aligned_charts(component,end):
    out=[];P=periods[end]
    for occurrence in component['face_occurrences']:
        M=transform(P,occurrence['period_from_canonical'])
        ck('period carries complete canonical face',sorted(tup(M*s.Matrix(v)) for v in component['canonical_face'])==sorted(map(tuple,occurrence['face'])))
        for ci in occurrence['charts']:
            N=M.inv()*mat(corners[end][ci]['rays'])
            ck('carried corner chart integral unimodular',abs(N.det())==1 and all(v.q==1 for v in N))
            out.append({'cone':ci,'N':N,'period_word':occurrence['period_from_canonical'],'occurrence':occurrence})
    return out
records=[];sumKU=F(0);sumLU=F(0);blowups=0
for component in surfaces:
    cid=component['id'];canonical=list(map(tuple,component['canonical_face']))
    ws=component['normal_weights'];order=sorted(range(2),key=lambda i:ws[i])
    normal=[canonical[i] for i in order];weights=[ws[i] for i in order]
    ck('actual opposite signed normal characters',weights[0]<0<weights[1])
    ck('generic surface no period stabilizer',not component['period_stabilizer_basis'])
    local=[]
    for occurrence in component['face_occurrences']:
        M=transform(common['period_generators'],occurrence['period_from_canonical'])
        for gci in occurrence['charts']:
            N=M.inv()*mat(generic[gci]['rays'])
            rays=[tup(N[:,i]) for i in range(3)]
            nindices=[rays.index(v) for v in normal]
            ti=next(i for i in range(3) if i not in nindices)
            sr=section_records[gci]
            ck('normal eigenlines carried without exchange',[sr['weights'][i] for i in nindices]==weights)
            ck('one fibre-tangent coordinate',[sr['weights'][ti]]==[0])
            local.append({'common_cone':gci,'N':N,'normal_indices':nindices,'tangent_index':ti,
                          'self':sr['degrees'][ti],'normal_degrees':[sr['degrees'][i] for i in nindices],
                          'transverse':tup(N[:,ti]),'section_record':sr})
    ck('actual two complete fibre charts',len(local)==2)
    v0=s.Matrix(local[0]['transverse']);v1=s.Matrix(local[1]['transverse'])
    W=mat(normal+[local[0]['transverse']])
    wall=-W.inv()*(v0+v1)
    ck('complete opposite primitive fibre rays',wall[2]==0)
    fibre_degrees=asints(wall[:2]);section_self=[c['self'] for c in local]
    section_normal=[c['normal_degrees'] for c in local]
    star_records={};exceptional=None
    for end in corners:
        rec=face['three_ends'][end]['components'][endmatch[end][cid]]
        ck('matched surface dimension',rec['dimension']==2)
        ck('matched surface normal weights',sorted(rec['normal_weights'])==weights)
        ck('end no residual period stabilizer',not rec['period_stabilizer_basis'])
        aligned=aligned_charts(rec,end)
        nr=[tuple(rec['canonical_face'][rec['normal_weights'].index(w)]) for w in weights]
        star=[]
        for ch in aligned:
            N=ch['N'];rays=[tup(N[:,i]) for i in range(4)]
            ni=[rays.index(v) for v in nr];ti=[i for i in range(4) if i not in ni]
            star.append({**ch,'normal_rays':nr,'normal_indices':ni,'tangent_indices':ti,'tangent_rays':[rays[i] for i in ti]})
        first=star[0];basis=mat(nr+first['tangent_rays'])
        ck('surface quotient lattice is saturated',abs(basis.det())==1)
        quotient={}
        for ch in star:
            qrs=[]
            for r in ch['tangent_rays']:
                q=basis.inv()*s.Matrix(r);v=tup(q[2:])
                ck('actual quotient ray integral',all(a.q==1 for a in q))
                quotient[r]=v;qrs.append(v)
            ck('surface local quotient chart regular',abs(mat(qrs).det())==1)
        boundary=[r for r in quotient if r[3]==0]
        interior=[r for r in quotient if r[3]>0]
        ck('end full half-plane has two opposite boundary rays',len(boundary)==2 and s.Matrix(quotient[boundary[0]])+s.Matrix(quotient[boundary[1]])==s.zeros(2,1))
        ck('all finite base-ray multiplicities one',all(r[3]==1 for r in interior))
        ck('surface end has exactly two or three charts',len(star) in (2,3))
        if len(star)==2:
            ck('smooth ruled end has one middle ray',len(interior)==1)
        else:
            ck('only infinity has the extra corner',end=='infinity')
            ck('one extra ray in surface star',len(interior)==2)
            # Either of these two reduced fibre components is an actual -1 curve.
            # Choose the lexicographic one and retain its exact two chart arrows.
            er=sorted(interior)[0];other=next(r for r in interior if r!=er)
            diff=s.Matrix(quotient[er])-s.Matrix(quotient[other])
            ck('literal single toric blowup sum',tuple(diff) in [tuple(quotient[r]) for r in boundary])
            occ=[ch for ch in star if er in ch['tangent_rays']]
            ck('chosen exceptional curve complete two-chart star',len(occ)==2)
            far=[next(r for r in ch['tangent_rays'] if r!=er) for ch in occ]
            EW=mat(nr+[er,far[0]])
            relation=-EW.inv()*(s.Matrix(far[0])+s.Matrix(far[1]))
            ck('actual exceptional wall closes',relation[3]==0)
            ck('actual exceptional self-intersection minus one',relation[2]==-1)
            edeg=asints(relation[:2])
            incidence=[]
            for sec in local:
                target=ref[end][sec['common_cone']]['cone']
                targetstar=next(ch for ch in star if ch['cone']==target)
                incidence.append(int(er in targetstar['tangent_rays']))
            ck('two sections meet opposite fibre components',sum(incidence)==1)
            exceptional={'end':end,'ray':er,'other_fibre_ray':other,'wall_relation':asints(relation),
                         'normal_degrees':edeg,'section_incidence':incidence,'two_charts':[ch['cone'] for ch in occ],
                         'blowdown_ray_equation':{'exceptional':quotient[er],'old':quotient[other],'difference':tup(diff)}}
        star_records[end]={'component':rec['id'],'charts':[ch['cone'] for ch in star],
                          'canonical_normal_rays':nr,'surface_quotient_rays':[{'native':r,'quotient':v} for r,v in quotient.items()],
                          'full_period_words':[ch['period_word'] for ch in star],
                          'boundary_rays':boundary,'finite_base_rays':interior}
    b=int(exceptional is not None);blowups+=b
    ck('both actual section self-intersections',sum(section_self)==-b)
    n=fibre_degrees;q=section_normal[0];s0=section_self[0]
    if not b:
        I=s.Matrix([[s0,1],[1,0]])
        normals=[I.inv()*s.Matrix([q[i],n[i]]) for i in range(2)]
        sec1=I.inv()*s.Matrix([0,1])
        K=I.inv()*s.Matrix([-2-s0,-2])
    else:
        inc=exceptional['section_incidence'];ev=exceptional['normal_degrees']
        I=s.Matrix([[s0,1,inc[0]],[1,0,0],[inc[0],0,-1]])
        normals=[I.inv()*s.Matrix([q[i],n[i],ev[i]]) for i in range(2)]
        sec1=I.inv()*s.Matrix([0,1,inc[1]])
        K=I.inv()*s.Matrix([-2-s0,-2,-1])
    ck('actual surface intersection lattice unimodular',abs(I.det())==1)
    ck('second section disjoint and carries its full self-degree',(sec1.T*I*sec1)[0]==section_self[1])
    for i in range(2):
        ck('independent opposite-section line degree',(normals[i].T*I*sec1)[0]==section_normal[1][i])
    c11=F((normals[0].T*I*normals[0])[0]);c12=F((normals[0].T*I*normals[1])[0]);c22=F((normals[1].T*I*normals[1])[0])
    K2=int((K.T*I*K)[0]);euler=4+b
    ck('actual canonical square from adjunction',K2==8-b)
    p1=K2-2*euler
    ck('actual surface Pontryagin integral',p1==-3*b)
    w1,w2=weights;prod=w1*w2
    B=c11/F(w1*w1)+c12/F(prod)+c22/F(w2*w2)
    ku=B/F(prod)
    lu=(F(p1)-c11-c22-2*(F(w1,w2)+F(w2,w1))*c12+(w1*w1+w2*w2)*B)/F(prod)
    sumKU+=ku;sumLU+=lu
    records.append({'common_component':cid,'canonical_face':normal,'physical_normal_weights':weights,
        'generic_section_cones':[c['common_cone'] for c in local],
        'full_section_clutches':[c['section_record'] for c in local],
        'fibre_normal_degrees':n,'section_self_intersections':section_self,
        'normal_degrees_on_sections':section_normal,'end_surface_stars':star_records,
        'exceptional_curve':exceptional,'surface_type':'actual one-point blowup of the displayed split P1 bundle' if b else 'actual split P1 bundle',
        'intersection_basis':['S0','fibre','E'] if b else ['S0','fibre'],
        'intersection_matrix':[[int(v) for v in row] for row in I.tolist()],
        'normal_Chern_vectors':[asints(v) for v in normals],
        'normal_intersections':[str(c11),str(c12),str(c22)],
        'canonical_square':K2,'Euler_number':euler,'p1_surface':p1,
        'positive_hyperplane_pair':[str(ku),str(lu)],
        'physical_M_inner_pair':[str(-ku),str(-lu)],
        'physical_M_inner_residue':str(-(4*ku-lu)/24)})
ck('four exact one-point infinity blowups',blowups==4)
# The formal residue expansion is separately verified from the defining formula.
u=s.symbols('u');x1,x2,w1,w2,p1=s.symbols('x1 x2 w1 w2 p1')
z=s.symbols('z')
den=(x1+w1/z)*(x2+w2/z)
kseries=s.series((1/z)**3/den,z,0,2).removeO().expand().coeff(z,1)
lseries=s.series((1/z)*(p1+(x1+w1/z)**2+(x2+w2/z)**2)/den,z,0,2).removeO().expand().coeff(z,1)
Bt=x1*x1/w1**2+x1*x2/(w1*w2)+x2*x2/w2**2
ck('surface cubic residue exact',s.factor(kseries-Bt/(w1*w2))==0)
ck('surface p1-linear residue exact',s.factor(lseries-(p1-x1*x1-x2*x2-2*(w1/w2+w2/w1)*x1*x2+(w1*w1+w2*w2)*Bt)/(w1*w2))==0)
point_sums={}
for end in ('zero','infinity'):
    rows=[c for c in face['three_ends'][end]['components'] if c['dimension']==0 and c['tag']=='interior']
    ck('each corner has ten actual point faces',len(rows)==10)
    pair=[F(0),F(0)]
    for c in rows:
        ws=c['normal_weights'];pw=1
        for w in ws:pw*=w
        ku=F(1,pw);lu=F(sum(w*w for w in ws),pw)
        ck('actual point physical residue agrees',str(-(4*ku-lu)/24)==c['local_physical_M_residue'])
        pair[0]-=ku;pair[1]-=lu
    point_sums[end]={'count':len(rows),'physical_M_inner_pair':list(map(str,pair)),'physical_M_inner_residue':str((4*pair[0]-pair[1])/24)}
out={'status':'PASS_COMPACT_GENERIC_SURFACE_NORMALS','utc':datetime.now(timezone.utc).isoformat(),
 'checks':len(tests),'check_labels':tests,
 'inputs':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths.values()},
 'compact_surfaces':len(records),'ruled_surfaces':len(records)-blowups,'one_point_blowups':blowups,
 'surfaces':records,'sum_positive_hyperplane_pair':list(map(str,(sumKU,sumLU))),
 'sum_physical_M_inner_pair':list(map(str,(-sumKU,-sumLU))),
 'sum_physical_M_inner_residue':str(-(4*sumKU-sumLU)/24),
 'corner_point_terms':point_sums,
 'remaining_lower_surface_components':[c for c in face['three_ends']['one']['components'] if c['tag']=='lower_boundary'],
 'scope':'The117 compact generic fixed surfaces closed by the literal zero/one/infinity stars and their full normal clutches, plus separately the20 corner-interior points. Actual physical M=-u. The four p1 lower surfaces, external reference surfaces, original outer Jin transfer and total return are not assigned.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ('check_labels','surfaces','remaining_lower_surface_components')},indent=2))

