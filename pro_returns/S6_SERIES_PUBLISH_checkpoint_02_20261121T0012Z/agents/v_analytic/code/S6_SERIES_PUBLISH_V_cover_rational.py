"""Independent rational verification of the saved whole-base cover.

Uses a vertical-slab tiling proof, not quadtree prefix identities.  The cusp
exclusions use rational bivariate Bernstein bounds for a polynomial inequality,
not complex-ball inverse powers.  ODE enclosure values are inputs, not recomputed
here; their separate interval re-execution is recorded in the check notes.
"""
from fractions import Fraction as Q
from pathlib import Path
from math import comb
import json,re
import sympy as s

BASE=Path(__file__).resolve().parent.parent
OUT=BASE/'code/period_certificate_rerun/output'
U=Q('-1.0945402503114027801162682630549457037')
def ball(text):
    text=text.strip('[] ')
    if '+/-' in text:
        m,r=map(lambda a:Q(a.strip()),text.split('+/-'))
        return m-r,m+r
    v=Q(text);return v,v
def tiling(rects,whole):
    a,b,c,d=whole
    assert all(a<=x0<x1<=b and c<=y0<y1<=d for x0,x1,y0,y1 in rects)
    edges=sorted({v for r in rects for v in r[:2]})
    assert edges[0]==a and edges[-1]==b
    for lo,hi in zip(edges,edges[1:]):
        yy=sorted((y0,y1) for x0,x1,y0,y1 in rects if x0<=lo and x1>=hi)
        current=c
        for y0,y1 in yy: assert y0==current;current=y1
        assert current==d
    area=sum((x1-x0)*(y1-y0) for x0,x1,y0,y1 in rects)
    assert area==(b-a)*(d-c)
    return str(area)
def r2(box):
    x0,x1,y0,y1=box
    near=lambda a,b:Q(0) if a<=0<=b else min(abs(a),abs(b))
    return near(x0,x1)**2+near(y0,y1)**2,max(x0*x0,x1*x1)+max(y0*y0,y1*y1)
x,y=s.symbols('x y',real=True)
f=s.expand(s.re((1+(x+s.I*y)**5))*s.re((1+(x+s.I*y)**5))+s.im((x+s.I*y)**5)**2-s.Rational(1,16)*(x*x+y*y)**5)
coeff={(i,j):Q(int(v.p),int(v.q)) for (i,j),v in s.Poly(f,x,y).terms()}
def bernstein_upper(box):
    x0,x1,y0,y1=box;dx=x1-x0;dy=y1-y0
    power={}
    for (i,j),v in coeff.items():
        for a in range(i+1):
            xx=v*comb(i,a)*x0**(i-a)*dx**a
            for b in range(j+1):
                key=a,b;power[key]=power.get(key,Q(0))+xx*comb(j,b)*y0**(j-b)*dy**b
    vals=[]
    for i in range(11):
        for j in range(11):
            vals.append(sum(v*Q(comb(i,a),comb(10,a))*Q(comb(j,b),comb(10,b)) for (a,b),v in power.items() if a<=i and b<=j))
    return max(vals)
subdivisions=0
def cusp(box,depth=0):
    global subdivisions
    assert r2(box)[0]>0
    if bernstein_upper(box)<=0:return
    assert depth<6,('Bernstein certification failed',box)
    subdivisions+=1
    x0,x1,y0,y1=box;xm=(x0+x1)/2;ym=(y0+y1)/2
    for child in [(x0,xm,y0,ym),(xm,x1,y0,ym),(x0,xm,ym,y1),(xm,x1,ym,y1)]:cusp(child,depth+1)
summary=[]
lower_printed={'infinity':Q('-1.094216'),'zero':Q('-1.083056'),'cusp':Q('-1.083777'),'collar':Q('-1.030556')}
for domain in ['infinity','zero','cusp','collar']:
    data=json.loads((OUT/f'fresh_cover_{domain}.json').read_text())
    leaves=[json.loads(line) for line in (OUT/f'fresh_cover_{domain}.jsonl').read_text().splitlines()]
    rects=[list(map(Q,v['box'])) for v in leaves];whole=list(map(Q,data['initial_closed_rectangle']))
    area=tiling(rects,whole);k=0
    for leaf,box in zip(leaves,rects):
        reason=leaf['reason'];lo,hi=r2(box)
        if reason=='strict_height_bound':
            assert ball(leaf['height_lower'])[0]>lower_printed[domain]>U;k+=1
        elif reason=='outside_root_disc':assert lo>Q(49,50)**2
        elif reason=='outside_collar_outer_disc':assert lo>Q(103,100)**2
        elif reason=='inside_collar_inner_disc':assert hi<Q(49,50)**2
        elif reason=='central_hessian_square':assert max(abs(q) for q in box)<=Q(1,10)
        elif reason=='inner_cusp_certificate':assert hi<=Q(1,100)**2
        elif reason=='covered_by_cusp_disc':cusp(box)
        else:raise ValueError(reason)
    summary.append({'domain':domain,'leaves':len(leaves),'strict_height_bounds':k,'area':area,'exact_slab_tiling':True,'all_geometric_exclusions':True})
    print(summary[-1],flush=True)
local=json.loads((OUT/'fresh_local_domains.json').read_text())
tiling([list(map(Q,a['box'])) for a in local['central_closed_leaves']],list(map(Q,local['central_square'])))
for row in local['central_closed_leaves']:
    xx=ball(row['hxx']);yy=ball(row['hyy']);xy=ball(row['hxy'])
    assert min(xx[0],yy[0])-max(abs(xy[0]),abs(xy[1]))>Q(1,4)
for v,bound in zip(local['cusp_shifted_det_coefficients'],[Q(3,2),Q(9,2),Q(15,4),Q(1)]):
    assert ball(v['lower'])[0]>=bound
endpoint=json.loads((OUT/'fresh_frobenius.json').read_text())
mi,ma=ball(endpoint['h_b']['infinity'])
assert mi>Q('-1.094540250311402780116268263054945703726')
assert ma<Q('-1.094540250311402780116268263054945703725')
assert Q(49,50)**4>=Q(103,100)**-5
res={'scope':'exact rational finite coverage, serialized numerical inequalities, Hessian and cusp determinant signs; not new ODE enclosures','method':'slab tiling plus polynomial Bernstein cusp exclusions','domains':summary,'bernstein_extra_subdivisions':subdivisions,'all_passed':True}
(BASE/'S6_SERIES_PUBLISH_V_cover_rational.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps(res),flush=True)
