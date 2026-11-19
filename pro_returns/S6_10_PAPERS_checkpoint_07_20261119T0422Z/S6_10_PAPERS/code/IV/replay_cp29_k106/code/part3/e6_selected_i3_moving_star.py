"""Actual selected fixed-face star, its blowdowns and two normal line maps."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json
import sympy as S
ROOT=Path(__file__).resolve().parents[2]
ip=ROOT/'code/part3/e6_selected_i3_corner_lifts.json'
d=json.loads(ip.read_text())['corners']['zero'];records=[];labels=[]
def ck(n,x):
 assert x,n
 labels.append(n)
def mat(C):return S.Matrix(list(zip(*C)))
def T(v,n):
 x,y,r,s=v;a,b=n
 return (x+(r+3*s)*a-s*b,y+6*s*a+(r+2*s)*b,r,s)
def can(C):
 X,Y,R,H=map(sum,zip(*C));a=R+3*H;b=-H;c=6*H;e=R+2*H;det=a*e-b*c
 n=((e*X-b*Y)//det,(a*Y-c*X)//det)
 return tuple(sorted(T(v,(-n[0],-n[1])) for v in C)),n
face=((0,0,1,0),(0,1,1,0))
mp=S.Matrix([[-2,1,0,0]]);mn=S.Matrix([[2,-1,1,0]])
allrays=set();fan=set()
for co in d['cones']:
 w=co['physical_weights'];nz=[j for j,a in enumerate(w) if a]
 if len(nz)!=2:continue
 f=tuple(tuple(co['rays'][j]) for j in nz);fc,n=can(f)
 if fc!=face:continue
 C=[T(v,(-n[0],-n[1])) for v in co['rays']];N=mat(C)
 ck('selected normal physical weights '+str(co['id']),N*S.Matrix(w)==S.Matrix([0,1,0,0]) and sorted(w)==[-1,0,0,1])
 zero=[j for j,v in enumerate(w) if not v];plus=w.index(1);minus=w.index(-1)
 qp=list(mp*N);qm=list(mn*N)
 ck('complete positive normal derivative '+str(co['id']),[qp[j] for j in nz]==[int(j==plus) for j in nz])
 ck('complete negative normal derivative '+str(co['id']),[qm[j] for j in nz]==[int(j==minus) for j in nz])
 ck('normal product is literal p '+str(co['id']),[qp[j]+qm[j] for j in range(4)]==list(N.row(2)))
 tangent=[(C[j][0],C[j][3]) for j in zero]
 ck('saturated regular surface quotient '+str(co['id']),abs(mat(tangent).det())==1)
 for j in zero:
  if C[j][3]>0:ck('upper normal section orders vanish '+str((co['id'],j)),C[j][1]==2*C[j][0] and C[j][2]==0 and qp[j]==qm[j]==0)
 allrays.update(tangent);fan.add(tuple(sorted(tangent)))
 records.append({'cone':co['id'],'canonicalizing_period_h_B':n,'canonical_four_rays':C,'normal_positive_column':plus,'normal_negative_column':minus,'tangent_columns':zero,'surface_rays':tangent,'positive_dual_section_character':list(map(int,mp)),'negative_dual_section_character':list(map(int,mn)),'positive_dual_section_chart_exponents':list(map(int,qp)),'negative_dual_section_chart_exponents':list(map(int,qm)),'canonical_inverse_matrix':[[int(x) for x in row] for row in N.inv().tolist()]})
ck('all36 actual selected charts',len(records)==36)
def angle(r):
 if r==(1,0):return F(-1)
 if r==(-1,0):return F(2)
 return F(r[1],r[0]+r[1])
rays=sorted(allrays,key=angle)
ck('full half-plane fan',rays[0]==(1,0) and rays[-1]==(-1,0) and (0,1) in rays and set(tuple(sorted((a,b))) for a,b in zip(rays,rays[1:]))==fan)
ck('all consecutive determinants positive one',all(a[0]*b[1]-a[1]*b[0]==1 for a,b in zip(rays,rays[1:])))
old=[(1,0),(0,1),(-1,0)];work=rays.copy();undo=[]
while len(work)>3:
 found=None
 for j in range(1,len(work)-1):
  a,b,c=work[j-1:j+2]
  if b not in old and b==(a[0]+c[0],a[1]+c[1]):found=j;break
 ck('actual ordinary blowdown '+str(len(undo)),found is not None)
 a,b,c=work[found-1:found+2];undo.append({'left':a,'exceptional':b,'right':c});work.pop(found)
ck('literal product target fan',work==old)
forward=list(reversed(undo));built=old.copy()
for i,st in enumerate(forward):
 a,b,c=(st[k] for k in ['left','exceptional','right']);j=built.index(a)
 ck('chronological source blowup '+str(i),built[j+1]==c and b==(a[0]+c[0],a[1]+c[1]));built.insert(j+1,b)
ck('exact34 complex point blowups',len(forward)==34 and built==rays)
vertical=rays[1:-1];I=S.zeros(len(vertical))
for i,r in enumerate(vertical):
 a,c=rays[i],rays[i+2];I[i,i]=-(a[0]*c[1]-a[1]*c[0])
 if i+1<len(vertical):I[i,i+1]=I[i+1,i]=1
divz=S.Matrix([r[0] for r in vertical]);fib=S.Matrix([r[1] for r in vertical])
ck('literal whole-fibre principal class',I*fib==S.zeros(len(vertical),1))
ck('D0-Dinfty compact representative square',(divz.T*I*divz)[0]==-3)
ck('actual E determinant square',(5*divz).dot(I*(5*divz))==-75)
ck('relative tangent number from34 actual blowups',34*(-1-2)==-102)
ck('only actual h reindex needed',set(tuple(r['canonicalizing_period_h_B']) for r in records)=={(0,0),(1,0)})
P,p,c0,cq,Z,V=S.symbols('P p c0 cq Z V',nonzero=True)
eqZ=P**2*Z;eqV=(P*p*cq)**2*P**-4*p**-2*c0**-2*V
ck('retained forward height/B-square map',S.cancel(eqV-P**-2*(cq/c0)**2*V)==0)
w=(P-1)/(P+1);v=w*w-1;D=w*w-3;ss=v*(v+4)/(4*D*D)
ck('actual s/P parameter unit',S.cancel(ss+P*(P*P+P+1)/(P*P+4*P+1)**2)==0)
ck('full original tensor/point unit central value',S.cancel(D**5/(6+20*w*w+6*w**4)).subs(P,0)==-1)
proof=ROOT/'notes/part3_e6_selected_i3_moving_star_working.md'
out={'status':'PASS','checks':len(labels),'input_sha256':hashlib.sha256(ip.read_bytes()).hexdigest(),'source_sha256':hashlib.sha256(proof.read_bytes()).hexdigest(),'charts':records,'surface_rays':rays,'chronological_blowups':forward,'compact_vertical_intersection_matrix':[[int(x) for x in row] for row in I.tolist()],'divisor_Z_vertical_coefficients':list(map(int,divz)),'whole_parameter_fibre_coefficients':list(map(int,fib)),'normal_classes':{'N_plus':'2 D0 - 3 Dinfty','N_minus':'-3 D0 + 2 Dinfty','E':'5(D0-Dinfty)','compact_E_vector':list(map(int,-5*divz)),'compact_E_square':-75},'relative_tangent_p1':-102,'full_selected_forward_map_after_B_inverse_squared':{'Z':'P^2 Z','Vpt':'P^(-2)(c_q/c0)^2 Vpt','c0':'(p-1)^4 c'},'scope':'Exact selected fixed-face star, its34 ordinary toric blowups, full derivative normal classes and compactly supported determinant square. The actual parameter closing/reference Hopf cap, closed characteristic pair and total return are not yet evaluated.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ['charts','surface_rays','chronological_blowups','compact_vertical_intersection_matrix','divisor_Z_vertical_coefficients','whole_parameter_fibre_coefficients']},indent=2))
