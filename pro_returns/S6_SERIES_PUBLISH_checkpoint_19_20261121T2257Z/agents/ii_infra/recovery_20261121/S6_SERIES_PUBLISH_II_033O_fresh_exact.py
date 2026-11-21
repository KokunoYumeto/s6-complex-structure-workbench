"""Prerelease exact monodromy check; Python standard-library rational arithmetic."""
from fractions import Fraction as F
from pathlib import Path
import json

def ident(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]

def trans(a):
    return [list(v) for v in zip(*a)]

def mul(a,b):
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]

def sub(a,b):
    return [[x-y for x,y in zip(u,v)] for u,v in zip(a,b)]

def add(a,b):
    return [[x+y for x,y in zip(u,v)] for u,v in zip(a,b)]

def rref(a):
    a=[[F(x) for x in row] for row in a]
    row=0; piv=[]
    for col in range(len(a[0])):
        p=next((j for j in range(row,len(a)) if a[j][col]),None)
        if p is None: continue
        a[row],a[p]=a[p],a[row]
        q=a[row][col];a[row]=[v/q for v in a[row]]
        for j in range(len(a)):
            if j!=row:
                q=a[j][col];a[j]=[x-q*y for x,y in zip(a[j],a[row])]
        piv.append(col);row+=1
        if row==len(a):break
    return a,piv

def inv(a):
    n=len(a);b,p=rref([x+y for x,y in zip(a,ident(n))])
    assert p[:n]==list(range(n))
    return [row[n:] for row in b]

def kernel(a):
    b,p=rref(a);n=len(a[0]);out=[]
    for j in range(n):
        if j in p:continue
        v=[F(0)]*n;v[j]=F(1)
        for i,k in enumerate(p):v[k]=-b[i][j]
        out.append(v)
    return out

def commute_equations(matrices):
    units=[]
    for k in range(16):
        a=[[F(0)]*4 for _ in range(4)];a[k//4][k%4]=F(1);units.append(a)
    equations=[]
    for h in matrices:
        cols=[sum(sub(mul(e,h),mul(h,e)),[]) for e in units]
        equations.extend(trans(cols))
    return equations

def plain(v):
    if isinstance(v,F):return int(v) if v.denominator==1 else str(v)
    if isinstance(v,list):return [plain(x) for x in v]
    if isinstance(v,dict):return {k:plain(x) for k,x in v.items()}
    return v

T=[[[1,0,-2,-1],[0,0,-1,0],[0,1,0,-1],[0,0,0,1]],
   [[1,0,2,2],[0,1,1,1],[0,0,1,0],[0,0,0,1]],
   [[1,0,0,0],[0,1,0,0],[0,-1,1,0],[0,0,0,1]],
   [[1,0,0,-1],[0,1,1,0],[0,0,1,0],[0,0,0,1]]]
H=[trans(inv(t)) for t in T];I=ident(4)
assert mul(mul(mul(T[0],T[1]),T[2]),T[3])==I
assert all(mul(trans(t),h)==I for t,h in zip(T,H))
assert mul(mul(mul(H[0],H[0]),H[0]),H[0])==I
N=I;power=I
for j in range(1,4):power=mul(power,H[0]);N=add(N,power)
ell=[1,-1,-1,0];delta=[0,0,0,1]
Ncoords=[]
for v in trans(N):
    assert v[1]==-v[0] and v[2]==-v[0]
    Ncoords.append([v[0],v[3]])
assert all(v[0]%4==0 and v[1]%2==0 for v in Ncoords)
assert [4,0] in Ncoords and [0,2] in Ncoords
fixed=[kernel(sub(h,I)) for h in H]
hc=kernel(commute_equations(H));tc=kernel(commute_equations(T))
E41=[[F(i==3 and j==0) for j in range(4)] for i in range(4)]
E14=trans(E41)
for matrices,basis,e in [(H,hc,E41),(T,tc,E14)]:
    assert len(basis)==2
    assert all(mul(e,m)==mul(m,e) for m in matrices)
    assert len(rref([sum(I,[]),sum(e,[])])[1])==2
differences=[sub(h,I) for h in H]
expected_fixed=[[[1,-1,-1,0],[0,0,0,1]],
                [[1,-2,0,0],[0,0,1,0],[0,0,0,1]],
                [[1,0,0,0],[0,1,0,0],[0,0,0,1]],
                [[0,0,1,0],[0,0,0,1]]]
for h,basis,actual in zip(H,expected_fixed,fixed):
    assert len(basis)==len(actual)
    assert all(mul(sub(h,I),[[x] for x in v])==[[0]]*4 for v in basis)
    assert len(rref(basis)[1])==len(basis)

result={'method':'Fraction Gaussian elimination of 64 commutator equations, explicit integer columns and primitive coordinate maps; no SymPy or prior target program read.',
        'T':T,'H':H,'pairing_T_transpose_H_identity':True,'ordered_T_product_identity':True,
        'multiple_order_four':True,'differences_H_minus_I':differences,
        'rational_fixed_bases':fixed,'claimed_integral_fixed_bases':expected_fixed,
        'norm_matrix':N,'norm_columns_in_ell_delta_coordinates':Ncoords,
        'homology_centralizer_basis':[ [v[j:j+4] for j in range(0,16,4)] for v in hc],
        'cohomology_centralizer_basis':[ [v[j:j+4] for j in range(0,16,4)] for v in tc],
        'centralizer_dimensions':[len(hc),len(tc)],
        'all_assertions_passed':True}
out=Path(__file__).with_name('S6_SERIES_PUBLISH_II_033O_fresh_exact_output.json')
out.write_text(json.dumps(plain(result),indent=2)+'\n')
print(json.dumps(plain(result),indent=2))
