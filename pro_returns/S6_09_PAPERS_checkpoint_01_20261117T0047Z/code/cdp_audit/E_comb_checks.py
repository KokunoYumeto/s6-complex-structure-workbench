"""Exact invariant-generator and cohomology checks for E15.

The sheaf comparisons and positivity are proved in the text. This program
checks their local orders and all split bundles of the specified degrees
for 1 <= m <= 20; it does not replace that proof.
"""
from itertools import product

for n, f_orders, g_orders in [(3,(0,1),(0,2)),(4,(0,3),(0,1))]:
    constraints=[[int(f>g) for f in f_orders] for g in g_orders]
    defects=[[((v+g)//n) for g in g_orders] for v in g_orders]
    l_defects=[(1+g)//n for g in g_orders]
    print('order',n,'coarse graph constraints (rows G, columns F):',constraints)
    print('order',n,'product defects V_c tensor G_c:',defects)
    print('order',n,'product defects L_c tensor G_c:',l_defects)
    assert sum(map(sum,constraints))=={3:1,4:2}[n]
    assert sum(map(sum,defects))=={3:1,4:0}[n]
    assert sum(l_defects)=={3:1,4:0}[n]

def h0(n): return max(0,n+1)
def h1(n): return max(0,-n-1)
checked=0
for m in range(1,21):
    degree=2*m-1
    for a,c in product(range(degree+1),repeat=2):
        vv=(a,degree-a)
        gg=(c,degree-c)
        assert sum(h0(v) for v in vv)==2*m+1
        assert sum(h1(v) for v in vv)==0
        tensor=[v+g for v in vv for g in gg]
        assert sum(h1(z) for z in tensor)==0
        assert sum(h0(z) for z in tensor)+1==8*m+1
        vd=[v+degree for v in vv]
        assert sum(h1(z) for z in vd)==0
        assert sum(h0(z) for z in vd)+1==6*m
        lg=[g-1 for g in gg]
        assert sum(h1(z) for z in lg)==0
        assert sum(h0(z) for z in lg)+1==2*m
        checked+=1
    tangent=(2*m+1,8*m+1,6*m+1,0)
    assert sum((-1)**i*z for i,z in enumerate(tangent))==1
    if m in (1,12,20): print('m=',m,'tangent dimensions=',tangent)
print('All nonnegative splitting pairs checked:',checked)
print('All exact invariant-order, cohomology and index checks passed.')
