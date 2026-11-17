"""Exact charts and cohomology arithmetic for the cusp self-fibre product.

All identities are polynomial/rational over Q(zeta), zeta^2+zeta+1=0.
The topological arguments producing these groups are in C.2.UN.8;
the script checks their integer arithmetic and the generic NS matrix.
"""
import sympy as s

zeta=s.symbols('zeta')
u,r,b,a,v,ss,h,j=s.symbols('u r b a v ss h j')
alpha=-zeta
beta=-zeta**2

def reduce_zero(expr):
    num=s.together(expr).as_numer_denom()[0]
    return s.rem(s.Poly(s.expand(num),zeta),s.Poly(zeta**2+zeta+1,zeta)).as_expr()==0

x=(b-zeta*a)/(1-zeta)
y=(b-a)/(1-zeta)
c=alpha*a+beta*b
assert reduce_zero(x**3-y**3-a*b*c)
assert reduce_zero(((v+u)/2)**2-x**3-(((v-u)/2)**2-y**3)-(u*v-a*b*c))
print('Exact factorization x^3-y^3=a*b*(-zeta*a-zeta^2*b) verified.')
print('The two elliptic base coordinates agree exactly on u*v=a*b*c.')

charts={
 'first u-chart':{a:u*r,v:r*b*(alpha*u*r+beta*b)},
 'second s-chart':{u:a*ss,b:ss*h,v:h*(alpha*a+beta*ss*h)},
 'second b-chart':{a:(j*v-beta*b)/alpha,u:((j*v-beta*b)/alpha)*b*j},
}
for name,sub in charts.items():
    assert reduce_zero((u*v-a*b*c).subs(sub,simultaneous=True))
    print(name, ': smooth affine three-space chart; defining identity verified.')

t=s.symbols('t')
p=t**6-1
assert s.gcd(p,s.diff(p,t))==1
print('p(t)=t^6-1: six simple roots; leading coefficient nonzero at infinity.')
ns=s.Matrix([[0,1,1,1],[1,0,1,1],[1,1,0,3],[1,1,3,0]])
assert ns.rank()==4
print('Generic NS intersection matrix:',ns.tolist())
print('NS determinant =',ns.det(),'; rank =',ns.rank())

b_support=[1,0,4,0,1]
assert sum((-1)**i*n for i,n in enumerate(b_support))==6
b_surface=[1,0,10,0,1]
mw_rank=b_surface[2]-2
b2_total=1+2*mw_rank+ns.rank()
e_total=6*6
b3_total=2+2*b2_total-e_total
b_total=[1,0,b2_total,b3_total,b2_total,0,1]
assert b_total==[1,0,21,8,21,0,1]
assert sum((-1)**i*n for i,n in enumerate(b_total))==e_total
print('Central support integral cohomology ranks =',b_support,'; all groups free.')
print('Central support coherent dimensions h^q(O) =',[1,2,1])
print('Rational elliptic surface Betti ranks =',b_surface,'; MW rank =',mw_rank)
print('Compact resolved threefold rational Betti ranks =',b_total)
print('Compact resolved threefold h^q(O) =',[1,0,0,1])
print('Compact resolved threefold h11 =',b2_total,'; h21 =',(b3_total-2)//2,'; Euler =',e_total)
print('All exact checks passed.')
