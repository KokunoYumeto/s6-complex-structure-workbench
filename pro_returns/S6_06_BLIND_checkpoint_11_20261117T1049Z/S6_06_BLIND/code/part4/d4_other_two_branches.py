"""Exact conductor incidence partitions for the two-branch B sector."""
from pathlib import Path
import json
import sympy as s

def partitions(xs):
    if not xs:
        yield []
        return
    x = xs[0]
    for p in partitions(xs[1:]):
        yield [[x]] + [a[:] for a in p]
        for i in range(len(p)):
            q = [a[:] for a in p]
            q[i] = [x] + q[i]
            yield q

def allowed(h, mode):
    # (name, normalized global component, image local branch)
    toks = [('H'+str(i),'H','A') for i in range(h)]+[('R','R','A')]
    if mode == 'two_degree_one':
        toks += [(c+a,c,a) for c in ['V','W'] for a in ['+','-']]
    else:
        toks += [('V'+a+str(i),'V',a) for a,r in zip(['+','-'],mode) for i in range(r)]
    comps = {t[1] for t in toks}
    out = []
    for p in partitions(toks):
        if any(len({t[1] for t in a}) != len(a) for a in p):
            continue
        supports = [{t[2] for t in a} for a in p]
        if any(not supports[i] & supports[j] for i in range(len(p)) for j in range(i)):
            continue
        uf = {c:c for c in comps}
        def find(c):
            while uf[c] != c:
                c = uf[c]
            return c
        forest = True
        for a in p:
            for t in a[1:]:
                x,y = find(a[0][1]),find(t[1])
                if x == y:
                    forest = False
                    break
                uf[x] = y
            if not forest:
                break
        if forest:
            out.append([[t[0] for t in a] for a in p])
    return out

patterns = {}
for h in [1,2]:
    for mode in ['two_degree_one',(1,1),(1,2),(2,1),(2,2)]:
        p=allowed(h,mode)
        patterns[f'H_preimages={h};B={mode}'] = p
        expected = (4 if h == 1 else 0) if mode == 'two_degree_one' else ((2 if h == 1 else 4) if mode == (1,1) else 0)
        assert len(p) == expected

X,Y,u,z,k = s.symbols('X Y u z k')
assert s.expand((Y**2+X**2*k).subs(Y,X*u)-X**2*(u**2+k)) == 0
# The final exact valuation contradiction is 2*b=m and b=m*i, i>=1.
for m in range(1,100):
    for i in range(1,100):
        assert 2*m*i > m
out={'status':'PASS','three_branch_image_patterns':patterns,'normalization_pullback':'F_H(X,Xu,z)=X^2(u^2+k(X,z))','valuation_identity':'2b=m, b=m*i, i>=1 is impossible','proof':'notes/part4_d4_two_sheet_other_working.md; all unrestricted graph bounds and analytic ring maps are proved there.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
