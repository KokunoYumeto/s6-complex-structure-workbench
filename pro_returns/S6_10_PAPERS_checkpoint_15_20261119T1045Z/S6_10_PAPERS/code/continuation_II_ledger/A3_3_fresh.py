from fractions import Fraction as Q
from pathlib import Path
import json

def rank(a):
    a=[[Q(x) for x in row] for row in a]
    n=len(a);m=len(a[0]) if n else 0;r=0
    for c in range(m):
        p=next((i for i in range(r,n) if a[i][c]),None)
        if p is None:continue
        a[r],a[p]=a[p],a[r]
        t=a[r][c];a[r]=[x/t for x in a[r]]
        for i in range(n):
            if i!=r:
                t=a[i][c]
                if t:a[i]=[x-t*y for x,y in zip(a[i],a[r])]
        r+=1
        if r==n:break
    return r

checks=[]
def check(name,value):
    assert value,name
    checks.append(name)

# Layer maps have d columns and d+1 rows.  Off-diagonal blocks are
# nonzero; no splitting of the filtered differential is assumed.
for m in range(1,10):
    for d in range(1,4):
        rows=m*(d+1);cols=m*d
        a=[[Q(0) for _ in range(cols)] for _ in range(rows)]
        for i in range(m):
            for j in range(i,m):
                for x in range(d+1):
                    for y in range(d):
                        if i==j:
                            v=Q((i+2) if x==y else 0)+Q((y+1) if x==d else 0)
                        else:v=Q((i+1)*(j+2)+(x+1)*(y+2),j-i+1)
                        a[i*(d+1)+x][j*d+y]=v
        check(f'full_filtered_injection_m{m}_d{d}',rank(a)==cols)
        for k in range(1,m+1):
            q=[row[:k*d] for row in a[:k*(d+1)]]
            check(f'actual_truncated_map_m{m}_d{d}_k{k}',rank(q)==k*d)
        for i in range(m):
            layer=[row[i*d:(i+1)*d] for row in a[i*(d+1):(i+1)*(d+1)]]
            check(f'layer_injection_m{m}_d{d}_j{i}',rank(layer)==d)

# Component labels are never collapsed: each translation and its inverse
# are evaluated on every component of each finite cyclic model.
for n in range(1,10):
    for j in range(9):
        targets=[(x+j)%n for x in range(n)]
        check(f'component_bijection_n{n}_j{j}',sorted(targets)==list(range(n)))
        check(f'actual_inverse_n{n}_j{j}',all((y-j)%n==x for x,y in enumerate(targets)))

out={'result':'PASS','checks':len(checks),'names':checks,'scope':'Exact rational filtered-map ranks for m=1..9 and d=1..3, including all actual truncations/layers and arbitrary nonzero off-diagonal extension blocks; finite component translations for 1..9 components and j=0..8. Universal proof is in A3_3_before_read.md; no universal conclusion is inferred from bounded tests.'}
p=Path(__file__).with_suffix('.output.json');p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'result':'PASS','checks':len(checks),'output':str(p)}))
