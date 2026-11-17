"""Exact Euclidean flip path for P3F.35; no numerical topology inference."""
from math import gcd
from pathlib import Path
import json

def add(v,w,n=1): return tuple(a+n*b for a,b in zip(v,w))
def neg(v): return tuple(-a for a in v)
def det(v,w): return v[0]*w[1]-v[1]*w[0]
def unoriented(v): return min(v,neg(v))
def edges(v,w): return {unoriented(v),unoriented(w),unoriented(add(v,w))}

def reduce_basis(v,w):
    assert abs(det(v,w))==1
    path=[{'basis':[v,w],'move':'start'}]
    def record(v1,w1,move):
        nonlocal v,w
        assert abs(det(v1,w1))==1
        before,after=edges(v,w),edges(v1,w1)
        assert before==after or len(before & after)==2
        path.append({'basis':[v1,w1], 'move':move,
                     'removed':sorted(before-after),
                     'added':sorted(after-before)})
        v,w=v1,w1
    while w[0]:
        q=v[0]//w[0]
        for _ in range(abs(q)):
            record(add(v,w,-1 if q>0 else 1),w,'unit column move')
        record(w,v,'interchange columns; same fan')
    if v[0]<0: record(neg(v),w,'reverse first column; diagonal flip')
    if w[1]<0: record(v,neg(w),'reverse second column; diagonal flip')
    q=v[1]
    for _ in range(abs(q)):
        record(add(v,w,-1 if q>0 else 1),w,'unit column move')
    assert (v,w)==((1,0),(0,1))
    return path

examples=[]
for v,w in [((1,0),(0,1)),((2,3),(3,5)),((-5,2),(7,-3)),((13,8),(8,5))]:
    path=reduce_basis(v,w)
    orders=[abs(det((0,1),e)) for e in (v,w,add(v,w))]
    assert all(gcd(orders[i],orders[j])==1 for i,j in ((0,1),(0,2),(1,2)))
    examples.append({'initial_basis':[v,w], 'edge_isotropy_orders':orders,
                     'path':path})
out={'statement':'P3F.35','purpose':'explicit integral flip paths and prime-order check',
     'examples':examples}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print('Four exact Euclidean flip paths verified; every changed fan shares precisely two edge classes.')
for x in examples:
    print(x['initial_basis'], 'orders',x['edge_isotropy_orders'],
          'moves',len(x['path'])-1)
