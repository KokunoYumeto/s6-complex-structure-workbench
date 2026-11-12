"""Full original-coefficient cobar matrices and exact rank witnesses in (f,t)=(2,8)."""
from pathlib import Path
from itertools import product
from functools import lru_cache
import json,hashlib
W=Path(__file__).resolve().parent
Z=(0,0,0,0,0);degrees=(1,3,7,2,6);weights=(0,1,3,1,3)
gens=[tuple(int(i==j) for i in range(5)) for j in range(5)]
T0,T1,T2,X1,X2=gens
deg=lambda m:sum(a*b for a,b in zip(m,degrees))
weight=lambda m:sum(a*b for a,b in zip(m,weights))
def multiply(a,b):
    c=[x+y for x,y in zip(a,b)];q=0
    for i in range(2):
        k,c[i]=divmod(c[i],2);q+=k;c[i+3]+=k
    assert c[2]<2
    return q,tuple(c)
def addterm(d,key):
    if key in d:del d[key]
    else:d[key]=1
def tensor_product(a,b):
    d={}
    for (e,x,y) in a:
        for (f,u,v) in b:
            p,xu=multiply(x,u);q,yv=multiply(y,v)
            addterm(d,(e+f+p+q,xu,yv))
    return d
gen_delta=[]
for g in gens:gen_delta.append({(0,g,Z):1,(0,Z,g):1})
gen_delta[1][(0,X1,T0)]=1
gen_delta[2][(0,X2,T0)]=1
X1sq=multiply(X1,X1)[1]
gen_delta[2][(0,X1sq,T1)]=1
gen_delta[4][(0,X1sq,X1)]=1
@lru_cache(None)
def coproduct(m):
    result={(0,Z,Z):1}
    for i,k in enumerate(m):
        for _ in range(k):result=tensor_product(result,gen_delta[i])
    assert (0,m,Z) in result and (0,Z,m) in result
    if m!=Z:del result[(0,m,Z)];del result[(0,Z,m)]
    return result
monomials=sorted(m for m in product(range(2),range(2),range(2),range(5),range(2)) if deg(m)<=8)
by_degree={d:[m for m in monomials if deg(m)==d] for d in range(9)}
@lru_cache(None)
def words(f,t):
    if f==0:return [()] if t==0 else []
    return [(m,)+v for d in range(1,t+1) for m in by_degree[d] for v in words(f-1,t-d)]
def wordweight(v):return sum(weight(m) for m in v)
def differential(v):
    result={}
    for i,m in enumerate(v):
        for (e,a,b) in coproduct(m):
            assert e>=0 and weight(a)+weight(b)-e==weight(m)
            addterm(result,(e,v[:i]+(a,b)+v[i+1:]))
    return result
def matrix(basis,target):
    ids={v:i for i,v in enumerate(target)};cols=[]
    for v in basis:
        bit=0
        for e,u in differential(v):bit^=1<<ids[u]
        cols.append(bit)
    return cols
def apply(cols,x):
    y=0
    for i,c in enumerate(cols):
        if x>>i&1:y^=c
    return y
def elimination(cols):
    pivots={};selected=[];witness=[]
    for j,column in enumerate(cols):
        value=column;combination=1<<j
        while value:
            r=value.bit_length()-1
            if r not in pivots:
                pivots[r]=(value,combination);selected.append(j);witness.append(r);break
            v,k=pivots[r];value^=v;combination^=k
    return pivots,selected,witness
def determinant_mod2(rows):
    rows=list(rows);n=len(rows)
    for j in range(n):
        k=next((k for k in range(j,n) if rows[k]>>j&1),None)
        if k is None:return 0
        rows[j],rows[k]=rows[k],rows[j]
        for k in range(j+1,n):
            if rows[k]>>j&1:rows[k]^=rows[j]
    return 1
def certificate(cols):
    pivots,cs,rs=elimination(cols)
    minor=[sum(((cols[c]>>r)&1)<<j for j,c in enumerate(cs)) for r in rs]
    assert determinant_mod2(minor)==1
    return dict(rank_lower_bound=len(cs),columns=cs,rows=rs,minor_rows_binary=minor,determinant_mod2=1)
def annihilator(cols,chosen,n):
    # Solve ell . column=0 and ell[chosen]=1 by exact row elimination.
    equations=[(c,0) for c in cols]+[(1<<chosen,1)]
    pivots={}
    for row,value in equations:
        while row:
            p=row.bit_length()-1
            if p not in pivots:pivots[p]=(row,value);break
            a,b=pivots[p];row^=a;value^=b
        assert row or value==0
    solution=0
    for p,(row,value) in sorted(pivots.items()):
        value^=(row&solution).bit_count()%2
        if value:solution|=1<<p
    assert all((solution&c).bit_count()%2==0 for c in cols)
    assert solution>>chosen&1
    return solution
full={f:words(f,8) for f in [1,2,3]}
all_columns=[]
for f in [1,2]:
    for j,v in enumerate(full[f]):
        all_columns.append(dict(length=f,column=j,word=v,
            terms=[dict(coefficient_power=e,target_word=u) for e,u in sorted(differential(v))]))
rows=[]
cycle=(X1sq,X1sq)
for w in range(5):
    bases={f:[v for v in full[f] if wordweight(v)>=w] for f in [1,2,3]}
    d1=matrix(bases[1],bases[2]);d2=matrix(bases[2],bases[3])
    assert all(apply(d2,c)==0 for c in d1)
    j=bases[2].index(cycle);assert d2[j]==0
    c1,c2=certificate(d1),certificate(d2)
    assert len(bases[2])==c1['rank_lower_bound']+c2['rank_lower_bound']+1
    ell=annihilator(d1,j,len(bases[2]))
    rows.append(dict(weight=w,dimensions={str(f):len(bases[f]) for f in [1,2,3]},
        bases=bases,d1_columns_binary=d1,d2_columns_binary=d2,
        d1_rank_witness=c1,d2_rank_witness=c2,cycle_column=j,nonboundary_functional_binary=ell,
        conclusion='The class of tau_h^(4-w) [xi_1^2|xi_1^2] is a basis of H^(2,8,w).'))
report=dict(generator_order=['tau_0','tau_1','tau_2','xi_1','xi_2'],degrees=degrees,weights=weights,
    coefficient='F2[tau_h], weight(tau_h)=-1',full_bases=full,full_original_differential=all_columns,
    weight_slices=rows,scope='All original basis words and coefficient powers retained. Binary integer column masks index the explicitly listed bases. Nonzero minors give rank lower bounds; d2*d1=0, the dimension sum and the displayed nonboundary functional force the exact one-dimensional cohomology. Weight <=0 is covered by the proved coefficient isomorphism; weights >4 have zero cochains.')
out=W/'ORIGINAL_COEFFICIENT_H28_CERTIFICATE.json';out.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(rows=[dict(weight=x['weight'],dimensions=x['dimensions'],rank_d1=x['d1_rank_witness']['rank_lower_bound'],rank_d2=x['d2_rank_witness']['rank_lower_bound']) for x in rows],sha256=hashlib.sha256(out.read_bytes()).hexdigest())))
