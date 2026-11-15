"""Exact local differential and intersection checks for Statement A.5.10."""
import sympy as s

g,v,r,n=s.symbols('g v r n')

def product(a,b):
    """(a0 C+a1 F)(b0 C+b1 F), with C^2=n, C.F=1, F^2=0."""
    return s.expand(a[0]*b[0]*n+a[0]*b[1]+a[1]*b[0])

for eps in (0,1):
    L=(2+eps,-n)
    M=(1-eps,2-2*g+r)
    q=s.expand(product(L,L)+product(L,M)+product(M,M))
    corrected=s.expand(q.subs(n,2-2*g-v))
    expected=3*(4-4*g-v+r) if eps else 12-12*g-2*v+4*r
    assert s.expand(corrected-expected)==0
    print(f'epsilon={eps}: L={L}, M={M}, Q={q}, after adjunction Q={corrected}')

u,t,a=s.symbols('u t a')
param=s.Matrix([u**2,u**3,t+a*u])
jac=param.jacobian([u,t])
minors=[s.factor(jac.extract(rows,[0,1]).det()) for rows in ((0,1),(0,2),(1,2))]
assert minors==[0,2*u,3*u**2]
assert s.gcd_list(minors)==u
assert s.gcd_list(list(jac[:,0].subs(a,0)))==u
assert s.gcd_list(list(jac[:,0].subs(a,1)))==1
print('Cusp differential minors:',minors)
print('Kernel aligned with ruling: vertical common factor u; induced base order 0')
print('Kernel not aligned: vertical common factor 1; induced base order 1')

for m in range(2,31):
    branch=s.Matrix([u**m,u**(m+1),t])
    jb=branch.jacobian([t,u])
    bm=[s.factor(jb.extract(rows,[0,1]).det()) for rows in ((0,1),(0,2),(1,2))]
    common=s.gcd_list(bm)
    assert s.Poly(common,u).degree()==m-1
    conductor=m*(m-1)
    assert conductor>=2*(m-1)
print('Vertical branch differential orders and conductor inequality checked for m=2,...,30')

# The two orientation inequalities and the equality case used in the proof.
assert s.expand(3*(4-4*g-v+r).subs(r,v/2))==12-12*g-3*v/2
assert s.expand((12-12*g-2*v+4*r).subs(r,v/2))==12-12*g
assert s.expand((n-(2-2*g)).subs(n,2-2*g-v))==-v
print('Equality case Hom(T_C,N_C) degree:',-v)

# Nonminimal smooth ruled normalization: W=V+D_p and Bv=R-D_p.
# C.W=v and C.Bv=r because a ruling section avoids D_p.
k,w2,wb,b2=s.symbols('k w2 wb b2')
gram=s.Matrix([[n,v,r,1],[v,w2,wb,0],[r,wb,b2,0],[1,0,0,0]])
for eps in (0,1):
    LL=s.Matrix([2+eps,1,0,k])
    MM=s.Matrix([1-eps,0,1,-k])
    Q=s.expand((LL.T*gram*LL+LL.T*gram*MM+MM.T*gram*MM)[0].subs(n,-k-v))
    expected=-6*k-3*v+3*r+w2+wb+b2 if eps else -6*k-2*v+4*r+w2+wb+b2
    assert s.expand(Q-expected)==0
    print(f'Nonminimal epsilon={eps}: Q={Q}')
assert s.expand((w2+wb+b2)-((w2+wb+b2/4)+3*b2/4))==0
print('Vertical quadratic equals (W+Bv/2)^2+3 Bv^2/4 exactly')
print('All exact A.5.10 checks passed')
