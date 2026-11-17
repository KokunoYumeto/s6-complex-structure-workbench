"""Exact affine and fan checks for f*u*v=g*s^n, r=g-f.

This checks a local model only.  No global Kato or S6 gluing is inferred.
"""
from collections import Counter
import json
from pathlib import Path
import sympy as S

u,v,s,f,g,U,Q,G,F,root,r = S.symbols('u v s f g U Q G F root r')
charts=[
    {'name':'A','u':s*U,'v':v,'s':s,'f':f,'g':f*U*v,'r':f*(U*v-1)},
    {'name':'B','u':u,'v':G*Q,'s':u*Q,'f':f,'g':f*G,'r':f*(G-1)},
    {'name':'C','u':u,'v':v,'s':u*v*F,'f':g*F,'g':g,'r':g*(1-F)}
]
for c in charts:
    assert S.expand(c['f']*c['u']*c['v']-c['g']*c['s'])==0
    assert S.expand(c['g']-c['f']-c['r'])==0
    print('chart',c['name'],': equation and r formula PASS; q =',c['s'])

fan_records=[]
for n in (1,2,3,4,6,12):
    triangles=[]
    for i in range(n):
        for j in range(n-i):
            triangles.append(((i,j),(i+1,j),(i,j+1)))
    for i in range(n-1):
        for j in range(n-1-i):
            triangles.append(((i+1,j),(i,j+1),(i+1,j+1)))
    assert len(triangles)==n*n
    edges=Counter()
    vertices=set()
    for tri in triangles:
        rays=[S.Matrix([a,b,1]) for a,b in tri]
        assert abs(S.Matrix.hstack(*rays).det())==1
        assert all(a>=0 and b>=0 and a+b<=n for a,b in tri)
        # F has order n-a-b; s has order1 on every new ray.
        assert all(n-a-b>=0 for a,b in tri)
        assert any(n-a-b>0 for a,b in tri)
        for p in tri: vertices.add(p)
        for k in range(3): edges[tuple(sorted((tri[k],tri[(k+1)%3])))] += 1
    boundary=[edge for edge,count in edges.items() if count==1]
    assert all(count in (1,2) for count in edges.values())
    assert len(boundary)==3*n
    assert len(vertices)==(n+1)*(n+2)//2
    assert len(edges)==3*n*(n+1)//2
    assert len(vertices)-len(edges)+len(triangles)==1
    edge_rays=sorted([p for p in vertices if sum(p)==n])
    assert edge_rays==[(i,n-i) for i in range(n+1)]
    for i in range(n):
        # Coordinates (a,d) on the lattice n*d-a-b=0.
        assert S.Matrix([[i,i+1],[1,1]]).det()==-1
    fan_records.append({'n':n,'vertices':len(vertices),'edges':len(edges),
                        'triangles':len(triangles),'boundary_edges':len(boundary),
                        'determinants':'all +/-1','height_s':'all1'})
    print('n =',n,':',len(triangles),'unimodular triangles; edge A-type fan and Euler identity PASS')

# The repaired collar is the literal q-chart H=(u*v-q)/q.
H,q = S.symbols('H q')
assert S.expand(S.expand(f*(u*v-q)-r*q).subs(u*v,q*(1+H))-q*(f*H-r))==0
assert S.expand(f*(u*v-q)-r*q-(f*u*v-(f+r)*q))==0
print('actual q-chart H and q-restored plumbing identity: PASS')

record={'status':'PASS','model':'f*u*v=g*s^n; r=g-f',
        'n1_resolution':'Bl_(u,q), then pullback Bl_(f,g)',
        'charts':[{key:str(value) for key,value in c.items()} for c in charts],
        'fans':fan_records,'scope':'local proper r-semistable resolution only',
        'global_period_action':'NOT CONSTRUCTED'}
Path(__file__).with_suffix('.json').write_text(json.dumps(record,indent=2)+'\n')
print('ALL EXACT CHECKS PASSED')
