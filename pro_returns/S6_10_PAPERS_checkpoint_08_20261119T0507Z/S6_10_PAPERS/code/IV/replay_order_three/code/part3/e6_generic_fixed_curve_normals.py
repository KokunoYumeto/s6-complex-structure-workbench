"""Actual three-end normal clutches for compact generic fixed curves.
The reference normal coordinates are the three toric characters dual to
one complete common cone.  The three end factors are computed from the
full native character matrices, including each corner divisor.
"""
from pathlib import Path
from fractions import Fraction as F
import sympy as s,json,hashlib,datetime
ROOT=Path(__file__).resolve().parents[2]
gp=ROOT/'code/part3_root/e6_common_period_fan.json';g=json.loads(gp.read_text())
ep=ROOT/'code/part3/e6_common_corner_lift.json';e=json.loads(ep.read_text())
op=ROOT/'code/part3_fourfold/e6_p_one_common_cayley.json';o=json.loads(op.read_text())
checks=[]
def ck(x,n):assert x,n;checks.append(n)
def mat(r):return s.Matrix.hstack(*map(s.Matrix,r))
refs={}
for end,cs in [('zero',e['ends']['zero']['cones']),('one',o['cones']),('infinity',e['ends']['infinity']['cones'])]:
 D={}
 for c in cs:
  if c['kind']!='upper_star':continue
  lower=[v for v in c['rays'] if v[2]==0];ck(len(lower)==1,'one lower ray')
  A=s.Matrix(lower[0]);ck(A==s.Matrix([0,0,0,1]),'native lower A')
  for r in c['generic_references']:
   cid=r['common_cone'];L=s.Matrix(r['full_corner_character_matrix'] if end=='one' else r['common_character_matrix'])
   D[cid]=(L*A)[:3]
 refs[end]=D
 ck(len(D)==510,'all common charts in '+end)
records=[];totU=F(0);total_kU=F(0);total_lU=F(0)
for cid,c in enumerate(g['cones']):
 N=mat(c['rays']);w=list(map(int,N.inv()*s.Matrix([1,0,0])))
 ck(w==c['physical_weights'],'common physical '+str(cid))
 if 0 in w:continue
 z=g['parent_zero_instances'][c['zero_parent']];i,j=z['shift']
 one=g['parent_one_instances'][c['one_parent']];r,t=one['shift']
 d0=s.Matrix([-6-3*i-3*j,i+j,0]);d1=s.Matrix([4*(2*r+t),0,0]);di=s.Matrix([0,0,1])
 for end,dv in [('zero',d0),('one',d1),('infinity',di)]:ck(list(dv)==list(refs[end][cid]),'actual lower common map '+end+str(cid))
 orders={end:list(map(int,N.inv()*dv)) for end,dv in [('zero',d0),('one',d1),('infinity',di)]}
 degrees=[-sum(orders[end][a] for end in orders) for a in range(3)]
 ck(sum(c['rays'][a][2]*degrees[a] for a in range(3))==-1,'original canonical adjunction '+str(cid))
 normalK=sum((2*c['rays'][a][2]-1)*degrees[a] for a in range(3));ck(normalK==-2-sum(degrees),'full adjunction '+str(cid))
 prod=w[0]*w[1]*w[2];c0=4-sum(a*a for a in w)
 RU=-sum((F(c0,a)+2*a)*d for a,d in zip(w,degrees))/(24*prod)
 kU=-sum(F(d,a) for a,d in zip(w,degrees))/prod
 lU=(2*sum(a*d for a,d in zip(w,degrees))-sum(a*a for a in w)*sum(F(d,a) for a,d in zip(w,degrees)))/prod
 ck((4*kU-lU)/24==RU,'separate characteristic pair '+str(cid))
 totU+=RU
 total_kU+=kU;total_lU+=lU
 records.append({'common_cone':cid,'rays':c['rays'],'normal_weights':w,'orders_of_common_normal_coefficient':orders,'normal_degrees':degrees,'positive_hyperplane_pair':[str(kU),str(lU)],'physical_M_inner_pair':[str(-kU),str(-lU)],'positive_hyperplane_residue':str(RU),'physical_M_inner_residue_before_outer_Jin_transfer':str(-RU),'period_stabilizer':[0,0],'base':'P1_p','normal_canonical_degree':normalK})
report={'status':'PASS','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'checks':len(checks),'check_labels':checks,'inputs':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [gp,ep,op]},'compact_curve_count':len(records),'curves':records,'sum_positive_hyperplane_pair':[str(total_kU),str(total_lU)],'sum_physical_M_inner_pair':[str(-total_kU),str(-total_lU)],'sum_positive_hyperplane_residue':str(totU),'sum_physical_M_inner_residue':str(-totU),'scope':'Compact generic fixed curves with three explicit end normal clutches only. Surface, corner-interior, exterior-reference and total boundary terms are not included; no return.'}
(ROOT/'code/part3/e6_generic_fixed_curve_normals.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k not in ['check_labels','curves']}))
