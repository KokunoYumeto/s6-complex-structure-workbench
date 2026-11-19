"""Independent Paper V arithmetic checks; no prior checking program imported.

The finite-type enumeration uses direct cyclotomic multiplicity recursion.
The genus-two singularity calculation uses polynomial resultants and explicit
coordinate substitutions. These compute the stated data without floating point.
"""
from pathlib import Path
from itertools import combinations_with_replacement, permutations, combinations
import json
import sympy as s

x, lam, t, X, Y, u = s.symbols('x lambda t X Y u')
eligible=[d for d in range(1,51) if s.totient(d)<=5]
types=[]
def enumerate_types(i,remaining,ms):
    if i==len(eligible):
        if remaining==0 and ms.get(1,0)>0:
            order=s.ilcm(*list(ms)) if len(ms)>1 else next(iter(ms))
            types.append({'multiplicities':ms.copy(),'order':int(order),
                          'complex':ms.get(1,0)%2==0 and ms.get(2,0)%2==0})
        return
    d=eligible[i];weight=int(s.totient(d))
    for m in range(remaining//weight+1):
        if m:ms[d]=m
        else:ms.pop(d,None)
        enumerate_types(i+1,remaining-m*weight,ms)
    ms.pop(d,None)
enumerate_types(0,6,{})
assert len(types)==38
assert sum(q['complex'] for q in types)==19
assert sorted({q['order'] for q in types})==[1,2,3,4,5,6,8,10,12]
for typ in types:
    order=typ['order'];weights=[]
    for d,m in typ['multiplicities'].items():
        for _ in range(m):
            weights.extend((a*order//d)%order for a in range(1,d+1) if s.gcd(a,d)==1)
    assert len(weights)==6
    typ['exterior_invariant_ranks']=[sum(sum(c)%order==0 for c in combinations(weights,k)) for k in range(7)]

f=x**5+lam**3*x+lam**4
disc=s.factor(s.discriminant(f,x))
zero=s.factor(f.subs({lam:t**8,x:t**6*X})/t**30)
infty=s.factor(f.subs({lam:u**(-5),x:u**(-4)*X})*u**20)
assert zero==X**5+X+t**2
assert infty==X**5+u*X+1
assert s.factor(disc)==lam**15*(3125*lam+256)
node=s.Rational(-256,3125);root=-5*node/4
assert f.subs({lam:node,x:root})==0
assert s.diff(f,x).subs({lam:node,x:root})==0
assert s.diff(f,x,2).subs({lam:node,x:root})!=0

patterns={}
for k in [2,3]:
    patterns[k]=[(r,b) for r in combinations_with_replacement([2,4,6],k)
                 for b in range(4) if sum(r)==6*k-8+b]
assert patterns[2]==[((2,2),0),((2,4),2)]
assert patterns[3]==[((2,2,6),0),((2,4,4),0),((2,4,6),2),((4,4,4),2)]

vertices=[]
cells=[set() for _ in range(4)]
for perm in permutations(range(3)):
    v=[s.zeros(3,1)];cur=s.zeros(3,1)
    for i in perm:
        cur=cur.copy();cur[i]+=1;v.append(cur)
    det=s.Matrix.hstack(*(v[i]-v[0] for i in range(1,4))).det()
    assert abs(det)==1
    vertices.append({'permutation':perm,'vertices':[list(a) for a in v],'det':int(det)})
    vv=[tuple(int(z) for z in a) for a in v]
    for k in range(4):
        for face in combinations(vv,k+1):
            origin=min(face)
            cells[k].add(tuple(sorted(tuple(b[i]-origin[i] for i in range(3)) for b in face)))
assert [len(c) for c in cells]==[1,7,12,6]

out={'method':'fresh SymPy resultant/discriminant; direct integer recursion; exact simplex determinants',
     'cyclotomic_types':types,'type_count':len(types),'complex_type_count':sum(q['complex'] for q in types),
     'orders':sorted({q['order'] for q in types}),'rank_patterns':patterns,
     'pencil_discriminant':str(disc),'zero_chart':str(zero),'infinity_chart':str(infty),
     'node_lambda':str(node),'node_root':str(root),'kuhn_simplices':vertices,
     'kuhn_periodic_cell_counts':[len(c) for c in cells],
     'T_degree':str(s.Rational(2,5)-s.Rational(3,8))}
p=Path(__file__).with_suffix('.json');p.write_text(json.dumps(out,indent=2,default=str))
print(json.dumps({'checks':'passed','type_count':len(types),'complex_type_count':sum(q['complex'] for q in types),'discriminant':str(disc),'output':str(p)},indent=2))
