"""Exact cubic value groups for two isometric E8^3 embeddings.

Trilinearity reduces the entire value group to the 8^3 basis triples.
The second embedding has coefficients in Q(sqrt(2)); we retain these as
rational coefficient pairs and use integer HNF, without approximation.
"""
from B_global_lattice import *
from B_triality import mul
from math import gcd
B=[[F(-1,2)]+[F(1,2)]*7]
for j in range(1,7):
 v=[F(0)]*8;v[j]=1;v[j+1]=-1;B.append(v)
v=[F(0)]*8;v[6]=v[7]=1;B.append(v)
BM=qmat(B);G=BM*BM.transpose();assert G.det()==1 and all(int(G[i,i])%2==0 for i in range(8))
def cubic(a,b,c):return mul(mul(a,b),c)[0]
old=[];new=[]
for a,b,c in product(B,repeat=3):
 old.append(cubic(a,b,c));aa=[F(0),F(0)]+a[2:];bb=[(a[0]-a[1])/2,(a[0]+a[1])/2]+[F(0)]*6
 new.append([cubic(aa,b,c),cubic(bb,b,c)])
den=lcm(*(x.denominator for x in old));g=gcd(*(int(x*den) for x in old));assert F(g,den)==F(1,2)
d=lcm(*(x.denominator for row in new for x in row));H=hnf([[int(x*d) for x in row] for row in new]);HB=[[F(x,d) for x in row] for row in H];assert len(HB)==2
two=[F(2)]+[F(0)]*7;rot_a=[F(0)]*8;rot_b=[F(1),F(1)]+[F(0)]*6
assert cubic(two,two,two)==8 and cubic(rot_a,two,two)==0 and cubic(rot_b,two,two)==4
print('E8 basis Gram determinant:',G.det())
print('All512 original cubic basis coefficients: additive group (1/2) Z')
print('All512 rotated cubic coefficient pairs in basis (1,sqrt(2)): HNF basis',HB)
print('Checked witness: original value8; rotated value4 sqrt(2).')
(REC/'B_cubic_embeddings.json').write_text(json.dumps({'E8_basis':qjson(BM),'E8_Gram':ints(G),'original_value_group':'(1/2)Z','original_512_coefficients':[str(x) for x in old],'rotated_512_coefficient_pairs':[[str(x) for x in row] for row in new],'rotated_value_group_basis':[[str(x) for x in row] for row in HB],'witness_original':'8','witness_rotated':'4sqrt(2)'}))
