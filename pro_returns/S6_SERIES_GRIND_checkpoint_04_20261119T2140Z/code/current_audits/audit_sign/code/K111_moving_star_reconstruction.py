"""Fresh reconstruction of the complete K111 NS/MN moving star.

Inputs: printed I2Z raw cones/rays and source functional, NS native
characters and period. No old fan array or divisor totals are loaded.
The original 136442-cone atlas is not certified by this scoped program.
"""
from pathlib import Path
from itertools import product
from fractions import Fraction
import json
import sympy as S

checks=0
def ck(v,msg):
    global checks
    checks+=1
    if not v: raise AssertionError(msg)
def mat(cols): return S.Matrix.hstack(*[S.Matrix(x) for x in cols])
def add(a,b,n=1):return tuple(x+n*y for x,y in zip(a,b))
def dot(a,b):return sum(x*y for x,y in zip(a,b))
A=(0,0,0,1);B1=(-1,0,0,1);B2=(-2,-1,0,1);B3=(-1,-1,0,1)
U1=(-5,0,1,0);U2=(-10,-3,1,0);U3=(-13,-6,1,0)
raw=[(A,B1,U1,U2)]
raw += [(A,B1,(-10-k,-3-k,1,0),(-11-k,-4-k,1,0)) for k in range(3)]
raw += [(A,B1,U3,B2),(A,B3,U3,B2)]
fans=list(raw)
stellar_records=[]
def star(v):
    global fans
    out=[];changed=[]
    for c in fans:
        M=mat(c);co=M.inv()*S.Matrix(v)
        if all(x>=0 for x in co) and sum(bool(x>0) for x in co)>1:
            children=[]
            for k,x in enumerate(co):
                if x>0:
                    cc=list(c);cc[k]=v;cc=tuple(cc)
                    ck(mat(cc).det()!=0,'stellar child full dimensional')
                    children.append(cc);out.append(cc)
            changed.append({'parent':c,'barycentric':[str(x) for x in co],'children':children})
        else:out.append(c)
    ck(bool(changed),'new ray is inserted into an actual parent')
    fans=out;stellar_records.append({'ray':v,'maps':changed})

# These two actual I2Z.14 rays resolve the only singular raw moving cone.
star((-9,-2,1,1));star((-7,-1,1,1))
ck(all(abs(mat(c).det())==1 for c in fans),'initial moving refinements regular')
# Source-cut A-shifts are ordinary two-coordinate blowups. We keep all
# children here; only the complete surviving two moving faces are extracted.
for k in range(1,4):
    v=(-10-k,-3-k,1,0)
    for j in range(1,k+1):star(add(v,A,j))
ck(all(abs(mat(c).det())==1 for c in fans),'source-cut moving refinements regular')
first=[c for c in fans if A in c and B1 in c]
second=[c for c in fans if B2 in c and B3 in c]
ck(len(first)==7 and len(second)==4,'all eleven moving charts extracted')

T=S.Matrix([[1,0,8,1],[0,1,6,1],[0,0,1,0],[0,0,0,1]])
delta=S.Matrix([-1,0,0,0]);mminus=S.Matrix([[1,-2,1,1]]);mplus=S.Matrix([[-1,1,0,0]])
ck(T*S.Matrix(B3)==S.Matrix(A) and T*S.Matrix(B2)==S.Matrix(B1),'actual period identifies ordered normal rays')
ck(T*delta==delta,'period preserves physical cocharacter')
data=[];divisor={};quotient_cones=set()
for face,cones in [('first',first),('second',second)]:
    for c in cones:
        C=mat(c);align=S.eye(4) if face=='first' else T;D=align*C
        source_orders=[v[1]+3*v[2]+v[3] for v in c]
        ck(min(source_orders)>=0 or max(source_orders)<=0,'whole moving chart has one actual source band')
        ck(sum(v[3]==0 for v in c)<=1,'common upper lift leaves this whole moving chart unchanged')
        weights=C.inv()*delta
        ck(sorted(int(x) for x in weights)==[-1,0,0,1],'exact physical weights')
        indices=[i for i,x in enumerate(weights) if x==0]
        tangent=[tuple(int(x) for x in D[:,i]) for i in indices]
        qrs=tuple(sorted((v[1],v[2]) for v in tangent));quotient_cones.add(qrs)
        # The first face uses the infinity chart (a_inf,c_inf)=(Za0,Zc0).
        mm=mminus+S.Matrix([[0,1,0,0]]) if face=='first' else mminus
        mp=mplus+S.Matrix([[0,1,0,0]]) if face=='first' else mplus
        rowm=mm*D;rowp=mp*D
        for i,w in enumerate(weights):
            if w==-1:ck(rowm[i]==1 and rowp[i]==0,'negative normal derivative')
            if w==1:ck(rowm[i]==0 and rowp[i]==1,'positive normal derivative')
        for i,v in zip(indices,tangent):
            qr=(v[1],v[2]);degrees=(int(rowm[i]),int(rowp[i]))
            if qr in divisor:ck(divisor[qr]==degrees,'adjacent full normal maps agree')
            divisor[qr]=degrees
        owners=[]
        for p in raw:
            P=mat(p);b=P.inv()*C
            if all(x>=0 for x in b):
                # Every raw finite quotient invariant of degree <= det generates
                # its coordinate ring by the finite-character zero-sum proof.
                d=abs(int(P.det()));count=0
                for a in product(range(d+1),repeat=4):
                    if not 0<sum(a)<=d:continue
                    ex=S.Matrix([a])*P.inv()
                    if not all(x.q==1 for x in ex):continue
                    pull=ex*C
                    ck(all(x.q==1 and x>=0 for x in pull),'whole raw invariant semigroup morphism')
                    count+=1
                owners.append({'raw_rays':p,'barycentric':[[str(x) for x in b.row(k)] for k in range(4)],'invariant_generators_checked':count})
        ck(bool(owners),'every moving chart maps to an actual raw parent')
        data.append({'face':face,'rays':c,'matrix':[[int(x) for x in C.row(k)] for k in range(4)],'inverse':[[int(x) for x in C.inv().row(k)] for k in range(4)],'physical_weights':[int(x) for x in weights],'quotient_rays':qrs,'negative_derivative_row':[int(x) for x in rowm],'positive_derivative_row':[int(x) for x in rowp],'canonical_orders':[2*v[2]+v[3]-1 for v in c],'raw_parent_morphisms':owners})

expected_rays=[(1,0)]+[(j,1) for j in range(3,-7,-1)]+[(-1,0)]
ck(quotient_cones=={tuple(sorted((a,b))) for a,b in zip(expected_rays,expected_rays[1:])},'full native quotient fan and no missing chart')
ck(divisor[(1,0)]==divisor[(-1,0)]==(0,0),'both horizontal module orders zero')
dm=[divisor[(j,1)][0] for j in range(3,-7,-1)];dp=[divisor[(j,1)][1] for j in range(3,-7,-1)]
ck(dm==[-4,-4,-4,-4,-4,-5,-6,-5,-4,-3],'fresh negative normal table matches MN')
ck(dp==[5,5,5,5,5,5,4,3,2,1],'fresh positive normal table matches MN')
M=S.zeros(10)
for j in range(10):
    M[j,j]=-1 if j in [0,9] else -2
    if j<9:M[j,j+1]=M[j+1,j]=1
pair=lambda a,b:int((S.Matrix(a).T*M*S.Matrix(b))[0])
vals=[pair(dm,dm),pair(dm,dp),pair(dp,dp)]
ck(vals==[-5,2,-4],'reconstructed normal intersections')
record={'source':'cp15 IV I2Z.9-18, NS.3-23, MN.1-4','scope':'Complete eleven-chart moving star, actual raw-parent monomial maps, actual T0 alignment, physical normal derivatives and all MN normal divisors reconstructed. This does not verify the full common atlas or compact/lower sums.','method':'Two specified quotient regularizing rays followed by explicit source-cut ordinary stellar morphisms. All children retained, then every chart containing either protected physical face extracted. Native infinity/zero Cartier frames evaluated before intersection.','raw_moving_cones':raw,'stellar_sequence':stellar_records,'all_local_children':len(fans),'moving_charts':data,'divisor_orders':{'negative':dm,'positive':dp},'normal_intersections':vals,'checks':checks}
p=Path(__file__).resolve().parents[1]
(p/'K111_moving_star_reconstruction.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'checks':checks,'charts':len(data),'local_children':len(fans),'negative':dm,'positive':dp,'intersections':vals,'scope':record['scope']},indent=2))
