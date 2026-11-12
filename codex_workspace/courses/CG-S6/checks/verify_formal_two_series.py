"""Finite supplementary checks for the complete formal-series proof."""
from pathlib import Path
from math import comb
from functools import reduce
import hashlib, json

W=Path(__file__).resolve().parents[1]
checks = []
def ck(name, test):
    assert test, name
    checks.append(name)

def toggle(s, x):
    if x in s: s.remove(x)
    else: s.add(x)

def rank(rows):
    pivots = {}
    for x in rows:
        while x:
            i = x.bit_length() - 1
            if i in pivots: x ^= pivots[i]
            else:
                pivots[i] = x
                break
    return len(pivots)

# The rows record all coefficients of the four full cocycle terms,
# together with symmetry, in the original coefficient variables c_i.
for n in range(2, 33):
    rows = {}
    for i in range(1, n):
        terms = set()
        toggle(terms, (n-i, i, 0)); toggle(terms, (0, n-i, i))
        for j in range(n-i+1):
            if comb(n-i, j) % 2: toggle(terms, (n-i-j, j, i))
        for j in range(i+1):
            if comb(i, j) % 2: toggle(terms, (n-i, i-j, j))
        for t in terms: rows[t] = rows.get(t, 0) ^ (1 << (i-1))
    equations = list(rows.values()) + [(1 << (i-1)) ^ (1 << (n-i-1)) for i in range(1, n)]
    power_two = n & (n-1) == 0
    generator = (1 << (n//2-1)) if power_two else sum((comb(n,i)%2) << (i-1) for i in range(1,n))
    ck(f'degree {n}: complete symmetric cocycle kernel dimension', rank(equations) == n-2)
    ck(f'degree {n}: displayed full generator in kernel', generator != 0 and all((row & generator).bit_count()%2 == 0 for row in equations))
    ck(f'degree {n}: diagonal coefficient', generator.bit_count()%2 == int(power_two))

# R = F_2[u]/(u^3), represented by three coefficient bits.
def rm(a,b):
    c=0
    for i in range(3):
        for j in range(3-i):
            if (a>>i)&1 and (b>>j)&1: c ^= 1 << (i+j)
    return c

def add(*polys):
    out={}
    for p in polys:
        for e,c in p.items():
            out[e]=out.get(e,0)^c
            if not out[e]: del out[e]
    return out

def scale(p,c): return {e:v for e,a in p.items() if (v:=rm(a,c))}

def mul(p,q,bound):
    out={}
    for e,a in p.items():
        for f,b in q.items():
            ef=tuple(x+y for x,y in zip(e,f))
            if sum(ef)>bound: continue
            c=rm(a,b)
            if c:
                out[ef]=out.get(ef,0)^c
                if not out[ef]: del out[ef]
    return out

def power(p,n,bound,variables):
    out={(0,)*variables:1}
    while n:
        if n&1: out=mul(out,p,bound)
        p=mul(p,p,bound); n//=2
    return out

def subst(p,args,bound):
    v=len(next(iter(args[0])))
    cache=[{i:power(a,i,bound,v) for i in {e[j] for e in p}} for j,a in enumerate(args)]
    out={}
    for e,c in p.items():
        term={(0,)*v:c}
        for j,i in enumerate(e): term=mul(term,cache[j][i],bound)
        out=add(out,term)
    return out

def inverse(h,bound):
    g={(1,):1}
    for j in range(2,bound+1):
        c=subst(h,[g],j).get((j,),0)
        if c: g[(j,)]=c
    return g

bound=12
x={(1,0):1}; y={(0,1):1}; t={(1,):1}; additive=add(x,y)
samples=[{(1,):1,(3,):2},{(1,):1,(2,):3,(3,):2,(5,):4},
         {(1,):1,(3,):1,(4,):2,(6,):5},{(1,):1,(2,):6,(5,):3,(7,):4}]
for si,h in enumerate(samples):
    g=inverse(h,bound)
    ck(f'sample {si}: both original inverse identities', subst(h,[g],bound)==t and subst(g,[h],bound)==t)
    F=subst(g,[add(subst(h,[x],bound),subst(h,[y],bound))],bound)
    ck(f'sample {si}: actual two-series', subst(F,[t,t],bound)=={})
    X={(1,0,0):1};Y={(0,1,0):1};Z={(0,0,1):1}
    ck(f'sample {si}: original associativity', subst(F,[subst(F,[X,Y],bound),Z],bound)==subst(F,[X,subst(F,[Y,Z],bound)],bound))
    original=F.copy(); L=t.copy()
    for n in range(2,bound+1):
        leading={e:c for e,c in F.items() if sum(e)==n}
        r=(n & -n); power_two=(r==n)
        if power_two:
            ck(f'sample {si}, stage {n}: vanishing power-of-two defect', not leading)
            c=0
        else:
            c=leading.get((n-r,r),0)
            gen=add(power(additive,n,bound,2),power(x,n,bound,2),power(y,n,bound,2))
            ck(f'sample {si}, stage {n}: exact leading full binomial', leading==scale(gen,c))
        change=add(t,{(n,):c} if c else {})
        inv=inverse(change,bound)
        F=subst(change,[subst(F,[subst(inv,[x],bound),subst(inv,[y],bound)],bound)],bound)
        L=subst(change,[L],bound)
        ck(f'sample {si}, stage {n}: all prior degrees retained', all(sum(e)>n or (e,c) in additive.items() for e,c in F.items()) and all(F.get(e)==c for e,c in additive.items()))
    ck(f'sample {si}: coordinate equality through degree {bound}', F==additive and subst(L,[original],bound)==add(subst(L,[x],bound),subst(L,[y],bound)))
    Linv=inverse(L,bound)
    ck(f'sample {si}: final two inverse identities', subst(L,[Linv],bound)==t and subst(Linv,[L],bound)==t)

# The worked nilpotent example is an exact polynomial identity: use a bound
# exceeding the degree of every composed polynomial, rather than truncating it.
h={(1,):1,(3,):2}; g={(1,):1,(3,):2,(5,):4}
ck('nilpotent example: exact polynomial inverse both ways', subst(h,[g],25)==t and subst(g,[h],25)==t)
F=add(x,y,{(2,1):2,(1,2):2,(4,1):4,(3,2):4,(2,3):4,(1,4):4})
ck('nilpotent example: every coefficient of the full original law', F==subst(g,[add(subst(h,[x],25),subst(h,[y],25))],25))
ck('nilpotent example: exact coordinate identity', subst(h,[F],25)==add(subst(h,[x],25),subst(h,[y],25)))
ck('nilpotent example: exact original two-series', subst(F,[t,t],25)=={})

for a in range(8):
    for b in range(8):
        f={(1,):1}; gg={(1,):1}
        if a: f[(2,)]=a
        if b: gg[(2,)]=b
        formula={(1,):1}
        if a^b: formula[(2,)]=a^b
        cross=rm(rm(a,a),b)
        if cross: formula[(4,)]=cross
        ck(f'additive composition over R, a={a}, b={b}', subst(gg,[f],4)==formula)

f={(1,):1,(2,):2}; gg={(1,):1,(2,):1}
ck('composition-order worked example: nonzero full difference', add(subst(gg,[f],4),subst(f,[gg],4))=={(4,):6})
src=W/'src/the-exact-characteristic-two-coordinate-calculation.md'
report=dict(passed=len(checks),source_sha256=hashlib.sha256(src.read_bytes()).hexdigest(),checks=checks,
 scope='Finite supplementary algebra checks. Complete cocycle coefficient systems in degrees 2 through 32; four formal-law examples through degree 12 over F_2[u]/(u^3); exact nilpotent polynomial example; all 64 two-term additive compositions over that ring. The written proof establishes the statements in all degrees and all specified rings. No topological cooperation classification is checked or asserted.')
(W/'checks/FORMAL_TWO_SERIES_CHECKS.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(passed=len(checks),source_sha256=report['source_sha256'])))
