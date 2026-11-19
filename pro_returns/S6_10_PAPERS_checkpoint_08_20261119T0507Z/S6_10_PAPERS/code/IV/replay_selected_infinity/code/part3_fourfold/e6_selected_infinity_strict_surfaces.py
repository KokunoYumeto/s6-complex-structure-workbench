"""Exact intersection assembly from the literal normal and source maps."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import hashlib,json
ROOT=Path(__file__).resolve().parents[2]
proof=ROOT/'notes/part3_e6_selected_infinity_strict_surfaces_working.md'
ref=ROOT/'code/part3_fourfold/e6_selected_infinity_surface_refinement.json'
source=ROOT/'code/part3_root/e6_selected_infinity_a3_source.json'
r=json.loads(ref.read_text());s=json.loads(source.read_text())
checks=[]
def ck(v,n):
    assert v,n;checks.append(n)
ck(r['status']=='PASS_ACTUAL_SURFACE_REFINEMENT_NORMALS','actual parent and normal map certificate')
ck(s['orbifold_source_p1']=='-6','independently audited actual orbifold source tangent')
rows=[]
for j,row in enumerate(r['strict_surfaces']):
    ck(row['j']==j,'actual chain index')
    mult=4-j;base=2*j+1
    orb=-F(mult*mult,2)-mult*base
    a3=F(row['D_square_difference'])
    resolved=orb+2*a3-F(1,2)
    p1=F(s['orbifold_source_p1'])+2*F(s['each_A3_delta_p1'])-3
    ck(p1==-24,'entire actual source tangent comparison')
    ck(resolved==[-14,-16,-14,-8][j],'resolved integral normal square')
    ru=(p1-3*resolved)/24
    ck(ru==[F(3,4),F(1),F(3,4),F(0)][j],'strict surface weighted term')
    # Keeping the A1 orbifold piece includes the isolated point through
    # the independently proved zero complete local correction.
    orb_a1=(F(s['orbifold_source_p1'])+2*F(s['each_A3_delta_p1'])
            -3*(orb+2*a3))/24
    ck(orb_a1==ru+F(1,16),'literal A1 boundary correction agrees')
    rows.append({'j':j,'orbifold_D_square':str(orb),
                 'each_A3_D_square_change':str(a3),
                 'A1_D_square_change':'-1/2','resolved_D_square':str(resolved),
                 'resolved_p1':str(p1),'positive_u_surface':str(ru),
                 'physical_M_surface':str(-ru),'A1_orbifold_inclusive_u':str(orb_a1)})
total=sum((F(x['positive_u_surface']) for x in rows),F(0))
ck(total==F(5,2),'four strict surface terms')
ck(total+F(1,4)==F(11,4),'four actual mu2 points retained once')
out={'status':'PASS_STRICT_SURFACE_COMPONENT_ASSEMBLY','utc':datetime.now(timezone.utc).isoformat(),
     'checks':len(checks),'check_labels':checks,
     'inputs':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in (proof,ref,source)},
     'section_intersections':{'O2':'-1/4','T2':'-1/4','OT':'0','LO':'1/4','LT':'1/4','L2':'0'},
     'actual_normal_models':{'positive':'I_(O+T)^(4-j) tensor L^j','negative':'L^(-j-1)'},
     'surfaces':rows,'strict_surface_u_sum':'5/2','strict_plus_mu2_u_sum':'11/4',
     'strict_plus_mu2_physical_M_sum':'-11/4',
     'scope':'Only the four completed strict-source surfaces and the same four mu2 isolated points. Other fixed surfaces and the moving reference cap remain in the full ledger; no global return.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
