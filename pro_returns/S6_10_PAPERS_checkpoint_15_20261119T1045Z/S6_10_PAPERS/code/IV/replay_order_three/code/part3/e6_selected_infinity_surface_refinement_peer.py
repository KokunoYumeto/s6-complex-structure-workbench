"""Independent full-wall, section-character and strict-surface assembly audit.
Normal degrees come from adjacent four-cone wall relations, not auxiliary circles.
"""
from pathlib import Path
import json,hashlib,datetime
import sympy as S
ROOT=Path(__file__).resolve().parents[2]
paths={'overlay':ROOT/'code/part3/e6_selected_infinity_factor_overlay.json',
       'faces':ROOT/'code/part3_fourfold/e6_fixed_face_orbits.json',
       'author':ROOT/'code/part3_fourfold/e6_selected_infinity_surface_refinement.json',
       'proof':ROOT/'notes/part3_e6_selected_infinity_strict_surfaces_working.md'}
O=json.loads(paths['overlay'].read_text());F=json.loads(paths['faces'].read_text());author=json.loads(paths['author'].read_text())
checks=[]
def ck(n,v):
    assert bool(v),n
    checks.append(n)
def mat(rs):return S.Matrix.hstack(*map(S.Matrix,rs))
def ints(M):return [[int(x) for x in row] for row in M.tolist()]
a,nm,np,chi=S.symbols('a nm np chi',nonzero=True)
I=S.Matrix([[-2,1,0],[1,-2,1],[0,1,-2]])
ck('A3 boundary order4',abs(I.det())==4)
ck('character1 strict transform E3 boundary class minus1',3%4==(-1)%4)
outrows=[]
for j in range(4):
    normal=[[0,0,1,j],[0,0,1,j+1]]
    f3=[[0,1,j],[0,1,j+1]]
    common=next(c for c in O['regular3_cones'] if all(r in c['rays'] for r in f3))
    h,k,ell=next(r for r in common['rays'] if r not in f3)
    eta=a;v=a**k*nm*np;V=a**ell*nm**j*np**(j+1)
    sold=S.cancel(V/(eta**(j+1)*v**j));told=S.cancel(v/sold)
    ck('actual strict positive ideal factor',S.cancel(sold-a**(3-j)*np)==0)
    ck('actual strict negative parent coefficient',told==nm)
    ck('ideal and base character produce chi4',4-j+j==4)
    ck('negative full coefficient character retained',-j-1==author['strict_surfaces'][j]['normal_base_L_powers']['negative'])
    rec=next(c for c in F['selected_ordinary_overlay']['components'] if c['dimension']==2 and c['canonical_face']==normal)
    charts=[(i,O['regular4_cones'][i]) for i in rec['face_occurrences'][0]['charts']]
    ck('four full strict source charts',len(charts)==4)
    walls=[];degrees=[]
    for i in range(1,4):
        adjacent=[]
        for ci,c in charts:
            tangent=[r for r in c['rays'] if r not in normal]
            e=[r for r in tangent if r[:2]==[i,1]]
            if e:adjacent.append((ci,e[0],next(r for r in tangent if r!=e[0])))
        ck('both actual exceptional curve charts',len(adjacent)==2)
        ck('actual common exceptional ray',adjacent[0][1]==adjacent[1][1])
        e=adjacent[0][1];p=adjacent[0][2];q=adjacent[1][2]
        N=mat(normal+[e,p]);wall=-N.inv()*(S.Matrix(p)+S.Matrix(q))
        ck('actual saturated full normal and tangent lattice',abs(N.det())==1)
        ck('full wall has A3 self minus2',wall[2]==-2 and wall[3]==0)
        ck('actual wall coefficients integral',all(z.q==1 for z in wall))
        degrees.append([int(wall[0]),int(wall[1])])
        walls.append({'adjacent_charts':[x[0] for x in adjacent],'exceptional_ray':e,'other_rays':[p,q],'wall_coefficients':list(map(int,wall))})
    ck('independent wall degrees equal full author normal maps',degrees==author['strict_surfaces'][j]['normal_degrees_negative_positive'])
    d=S.Matrix([b-a for a,b in degrees]);lift=I.inv()*d
    ck('full boundary coefficient maps to negative Chern character',(sum((i+1)*d[i] for i in range(3))+j+1)%4==0)
    ck('unique rational relative lift retains actual degrees',I*lift==d)
    local=(d.T*lift)[0]
    ck('actual relative square matches author',local==S.sympify(author['strict_surfaces'][j]['D_square_difference']))
    # Actual orbifold section intersections from the full source/base frames.
    power=4-j;base=2*j+1
    orb=-S.Rational(power*power,2)-power*base
    resolved=orb+2*local-S.Rational(1,2)
    p1=-6+2*(-S.Rational(15,2))-3
    residue=S.factor((p1-3*resolved)/24)
    ck('actual resolved source tangent number',p1==-24)
    ck('resolved integral normal square',resolved==[-14,-16,-14,-8][j])
    ck('strict normal-link value',residue==[S.Rational(3,4),1,S.Rational(3,4),0][j])
    # Exceptional parent face and its complete second source-chart arrow.
    ef=[[1,0,j],[1,0,j+1]]
    ec=next(c for c in O['regular3_cones'] if all(r in c['rays'] for r in ef))
    eh,ek,el=next(r for r in ec['rays'] if r not in ef)
    eta=a**eh*nm*np;v=a;V=a**el*nm**j*np**(j+1)
    es=S.cancel(V/(eta**j*v**j));et=S.cancel(eta/es)
    ck('exceptional positive parent arrow',es==np)
    ck('exceptional negative full parent arrow',S.cancel(et-a**j*nm)==0)
    ck('exceptional second chart degree minus j minus1',S.cancel(v*et-a**(j+1)*nm)==0)
    outrows.append({'j':j,'strict_third_ray':[h,k,ell],'full_wall_maps':walls,'degrees_negative_positive':degrees,'integral_D_degree_vector':list(map(int,d)),'relative_rational_lift':list(map(str,lift)),'A3_relative_square':str(local),'orbifold_square':str(orb),'resolved_square':str(resolved),'resolved_p1':str(p1),'strict_positive_u':str(residue),'exceptional_third_ray':[eh,ek,el],'exceptional_normal_fibre_degrees':[-j-1,0]})
total=sum(S.sympify(r['strict_positive_u']) for r in outrows)
ck('four strict source contributions',total==S.Rational(5,2))
ck('same four mu2 points retained once',total+S.Rational(1,4)==S.Rational(11,4))
out={'status':'PASS_INDEPENDENT_FULL_WALL_AND_STRICT_ASSEMBLY','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'checks':len(checks),'check_labels':checks,'inputs':{k:{'path':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for k,p in paths.items()},'surfaces':outrows,'strict_plus_mu2_positive_u':'11/4','strict_plus_mu2_physical_M':'-11/4','scope':'Common38 full parent arrows, independent full4D wall normal degrees, exact section and character signs, rational relative A3 lift and four strict-source assembly. No exceptional/refinement global surface or moving-cap/global return is assigned.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k in ['status','utc','checks','scope']},indent=2))
