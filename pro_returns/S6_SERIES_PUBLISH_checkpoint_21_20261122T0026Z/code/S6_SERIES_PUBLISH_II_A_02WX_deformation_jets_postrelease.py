"""Postrelease checks of the printed WX deformation calculations.

No target-specific historic code is used. Sparse coefficient collection
computes transverse two-jets; a truncated fixed-point recursion computes
the critical graph and its two-variable Morse remainder. All arithmetic is
rational. The universal exponent bounds are proved in the comparison text.
"""
from fractions import Fraction as Q
from math import comb
import json


def add(a, b):
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, Q(0)) + v
        if not out[k]:
            del out[k]
    return out


def scale(a, c):
    return {k: v*c for k, v in a.items() if v*c}


def mul(a, b, bound=7):
    out = {}
    for ka, va in a.items():
        for kb, vb in b.items():
            k = tuple(x+y for x, y in zip(ka, kb))
            if all(x <= bound for x in k):
                out[k] = out.get(k, Q(0)) + va*vb
    return {k: v for k, v in out.items() if v}


def power(a, n, bound=7):
    out = {(0,)*len(next(iter(a))): Q(1)}
    for _ in range(n):
        out = mul(out, a, bound)
    return out


def transverse_second_coefficients(terms, transverse, axis):
    """Translate around an axis point, collect exactly degree-two terms.

    Terms have exponents in x,y,z,s. Axis coordinate and s remain formal.
    This is coefficient collection, without symbolic differentiation.
    """
    ans = {}
    for exp, coefficient in terms:
        trans = tuple(exp[j] for j in transverse)
        other = [j for j in range(3) if j not in transverse]
        if sum(trans) != 2:
            continue
        assert other == [axis]
        key = trans + (exp[axis], exp[3])
        ans[key] = ans.get(key, Q(0)) + coefficient
    return ans


def evaluate_twojet(jet, axis_value, s):
    a=b=c=Q(0)
    for (i,j,k,l), v in jet.items():
        val=v*axis_value**k*s**l
        if (i,j)==(2,0): a += 2*val
        elif (i,j)==(1,1): b += val
        elif (i,j)==(0,2): c += 2*val
        else: raise AssertionError((i,j))
    return [[a,b],[b,c]], a*c-b*b


def string_matrix(m):
    return [[str(v) for v in row] for row in m]


rows=[]
for p,q in [(3,3),(3,4),(4,5),(7,9)]:
    double=[((2,0,0,0),Q(1)),((0,2,2,0),Q(1)),
            ((0,2,0,1),Q(1)),((0,q,0,0),Q(1))]
    first=[((1,1,1,0),Q(1)),((p,0,0,0),Q(1)),
           ((2,0,0,1),Q(1))]
    second=first+[((0,q,0,0),Q(1)),((0,3,0,1),Q(1))]
    for name,terms,trans,axis in [
        ('finite_double',double,(0,1),2),
        ('first_triple_y_axis',first,(0,2),1),
        ('first_triple_z_axis',first,(0,1),2),
        ('second_triple_z_axis',second,(0,1),2),
    ]:
        jet=transverse_second_coefficients(terms,trans,axis)
        values=[]
        for z,s in [(Q(1),Q(1,2)),(Q(2),Q(-1,4)),(Q(-3),Q(1,3))]:
            m,det=evaluate_twojet(jet,z,s)
            wanted=4*(z*z+s) if name=='finite_double' else -z*z
            assert det==wanted
            values.append({'axis':str(z),'s':str(s),'matrix':string_matrix(m),'determinant':str(det)})
        rows.append({'p':p,'q':q,'case':name,'coefficient_jet':{str(k):str(v) for k,v in sorted(jet.items())},'evaluations':values})


# The implicit critical equation is xi = -(yz+p xi^(p-1))/(2s).
# Iteration raises total order of the error because p>=3 and xi has order2.
# Degree bound7 suffices for all coefficients checked after dividing by y².
yz={(1,1):Q(1)}
morse=[]
for p,q in [(3,3),(3,4),(4,5),(7,9)]:
    for s in [Q(1,2),Q(-1,4),Q(1,3)]:
        xi={}
        for _ in range(9):
            tail=power(xi,p-1) if xi else {}
            xi=scale(add(yz,scale(tail,Q(p))),-Q(1)/(2*s))
        residual=add(add(yz,scale(power(xi,p-1),Q(p))),scale(xi,2*s))
        assert all(i+j>=9 for (i,j),v in residual.items())
        value=add(add(mul(xi,yz),power(xi,p)),scale(power(xi,2),s))
        value=add(value,{(q,0):Q(1),(3,0):s}) if q!=3 else add(value,{(3,0):1+s})
        assert all(i>=2 for (i,j) in value)
        H={(i-2,j):v for (i,j),v in value.items()}
        hz={j:v for (i,j),v in H.items() if i==0}
        assert hz=={2:-Q(1)/(4*s)}
        hy=H.get((1,0),Q(0))
        assert hy==(Q(1) if q==3 else Q(0))+s
        assert hy!=0
        assert xi.get((1,1))==-Q(1)/(2*s)
        morse.append({'p':p,'q':q,'s':str(s),'xi_yz':str(xi[(1,1)]),'H_at_y0':{str(k):str(v) for k,v in hz.items()},'H_y_at_origin':str(hy),'critical_residual_min_total_degree':min((i+j for i,j in residual),default='zero')})


print(json.dumps({'timing':'postrelease; no added prereading credit','method':'exact sparse coefficient collection and fixed-point implicit-graph recursion','universal_scope':'For every p,q>=3 the omitted x^p and y^q terms have transverse degree>=3; the universal two-jet and axis-restriction proofs are in the comparison. Sample rows test implementation, not the quantifier.','transverse_rows':rows,'morse_rows':morse,'normalization_map':'(v,y,z) -> (X=yv,y,z); source v^2+H=0, H_y(0)!=0 gives dy(0)=0 and differential rank1.'},indent=2))
