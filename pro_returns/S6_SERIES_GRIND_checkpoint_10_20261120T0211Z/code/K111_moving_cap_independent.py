"""Independent reconstruction from the saved original coefficient rows and source fan."""
from pathlib import Path
from fractions import Fraction
import json,hashlib
R=Path(__file__).resolve().parents[1]
p=R/'audit_sign/K111_new_moving_cap.json';raw=p.read_bytes();x=json.loads(raw);checks=0

def check(v,msg):
 global checks
 checks+=1
 assert v,msg

def dot(a,b):return sum(i*j for i,j in zip(a,b))
def det(a,b):return a[0]*b[1]-a[1]*b[0]
rays=list(map(tuple,x['source_rays']));n=len(rays)-2
orders={}
for chart in x['charts']:
 tangents=[ray for ray,w in zip(chart['aligned_rays'],chart['physical_weights']) if w==0]
 check(len(tangents)==2,'source tangent rays')
 for ray,q,saved in zip(tangents,chart['source_rays'],chart['divisor_orders']):
  check(tuple(ray[1:3])==tuple(q),'native source quotient map')
  d=[dot(chart['negative_row'],ray),dot(chart['positive_row'],ray)]
  check(d==saved,'full normal coefficient monomial order')
  key=tuple(q)
  check(key not in orders or orders[key]==d,'common wall order agreement')
  orders[key]=d
for a,b in zip(rays,rays[1:]):check(det(a,b)==1,'original source determinant one')
Q=[[0]*n for _ in range(n)]
for i in range(n):
 Q[i][i]=-det(rays[i],rays[i+2])
 if i:nx=i-1;Q[i][nx]=Q[nx][i]=1
 check(Q[i][i]==x['walls'][i]['self_intersection'],'wall self intersection')
check(Q==x['intersection_matrix'],'complete intersection matrix')
vectors=[[orders[v][j] for v in rays[1:-1]] for j in range(2)]
check(vectors==x['divisor_coefficients'],'all compact coefficient divisors')
def pairing(a,b):return sum(a[i]*Q[i][j]*b[j] for i in range(n) for j in range(n))
dm,dp=vectors
intersections=[pairing(dm,dm),pairing(dm,dp),pairing(dp,dp)]
check(intersections==x['normal_divisor_intersections'],'normal divisor intersection triple')
# Reconstruct each actual blowdown in order and its two exceptional coefficients.
chain=list(rays);coeff={v:list(orders[v]) for v in rays};coeff[rays[0]]=[0,0];coeff[rays[-1]]=[0,0]
exceptions=[]
for contraction in x['chronological_contractions']:
 l,m,r=map(lambda k:tuple(contraction[k]),['left','removed','right'])
 i=chain.index(m)
 check(chain[i-1]==l and chain[i+1]==r,'current consecutive source rays')
 check(tuple(a+b for a,b in zip(l,r))==m,'ordinary blowup ray equality')
 e=[coeff[m][j]-coeff[l][j]-coeff[r][j] for j in range(2)]
 check(e==contraction['coefficient_divisor_exceptional'],'exceptional coefficient transport')
 exceptions.append(e);chain.pop(i);coeff.pop(m)
check(chain==[(1,0),(0,1),(-1,0)],'final original ruled source fan')
section=coeff[(0,1)]
check(section==x['marked_section_pairings'],'section pairings from final fibre divisor')
check(intersections==[-sum(a*a for a,b in exceptions),-sum(a*b for a,b in exceptions),-sum(b*b for a,b in exceptions)],'blowup reconstruction of intersection triple')
# Exact own-cap roots x=h+Dminus, y=-h-Dplus, with h²=0.
a=intersections[0]+2*section[0]
b=-intersections[1]-section[0]-section[1]
c=intersections[2]+2*section[1]
check([a,b,c]==x['own_cap_positive_line_intersections'],'own-cap root square/product transport')
c1sq=a+2*b+c;c2=b;p1=-3*len(exceptions)
check(c1sq==x['own_cap_bundle_c1_squared'],'c1 squared')
check(c2==x['own_cap_bundle_c2'],'c2')
check(p1==x['own_cap_tangent_p1'],'tangent Pontryagin blowup sum')
# Expanding the physical Euler denominator with weights (-1,+1),
# and dualizing the negative-weight root, gives these two expressions.
pair=[c1sq-c2,p1+c1sq-4*c2]
check(pair==x['physical_moving_pair'],'physical moving contribution')
check(pair==[-906,-111],'declared moving pair')
compact=[895,139];lower=[12,-24]
inner=[compact[i]+pair[i]+lower[i] for i in range(2)]
check(inner==[1,4],'sum with the independently checked compact pair and supplied lower total')
out={'status':'PASS','checks':checks,'input_sha256':hashlib.sha256(raw).hexdigest(),'charts':len(x['charts']),'source_rays':rays,'intersection_matrix':Q,'normal_divisors':vectors,'normal_intersections':intersections,'exceptional_coefficients':exceptions,'section_pairings':section,'positive_root_intersections':[a,b,c],'c1_squared':c1sq,'c2':c2,'tangent_p1':p1,'physical_moving_pair':pair,'inner_sum_with_supplied_lower_total':inner,'scope':'Independent native coefficient-row/source fan, divisor, chronological blowup, own-cap and residue arithmetic. The geometric point/O and outer finite-reference comparison still requires its full proof; the lower total is imported and explicitly identified.'}
q=R/'code/outputs/K111_moving_cap_independent.json';q.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ['intersection_matrix','normal_divisors','source_rays','exceptional_coefficients']},indent=2))
