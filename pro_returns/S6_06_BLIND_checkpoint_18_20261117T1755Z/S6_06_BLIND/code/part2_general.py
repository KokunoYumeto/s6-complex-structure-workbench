"""Exact identities for the coprime (3k,4l) extension; no floating point."""
import sympy as S

N,m,n,s,v,mu,C,U,b,l0=S.symbols('N m n s v mu C U b l0')
a=b-N*l0
g=S.Matrix([6*mu,C-s-N*v]); d=S.Matrix([0,1])
zg=S.Matrix([6*s*mu,-s*(s+1)/2+s*(C-N*v)])
o=S.Matrix([-6*b*mu*s/N,b*s*s/(2*N)-b*C*s/N+l0*s/2+v*(b*s+U)])
sigma=-l0*zg+S.Matrix([6*a*mu*v,v*U+a*C*v-N*a*v*v/2+N*a*v/2])
F=S.Matrix([6*mu*(s+N*v)/N,C*(s+N*v)/N-(s+N*v)**2/(2*N)+N*v/2])
def check(name,expr):
    assert all(S.expand(z)==0 for z in expr), (name,expr)
    print(name, ': exact zero')
check('sigma-o=aF',sigma-o-a*F)
check('Q difference',F.subs(s,s+N*m)-F-m*g+N*m*m*d/2)
check('R difference',F.subs(v,v+n)-F-n*g+N*n*(n-1)*d/2)
check('o Q descent',o.subs(s,s+N)-o+b*g-N*(b+l0)*d/2)
check('sigma Q descent',sigma.subs(s,s+N)-sigma+N*l0*g-N*(N+1)*l0*d/2)
check('o R descent',o.subs(v,v+1)-o-(b*s+U)*d)
check('sigma R descent',sigma.subs(v,v+1)-sigma-(b*s+U)*d-a*g)
k,l=S.symbols('k l',integer=True,positive=True)
deg=12*k*l+4*l*(1-k)+3*k*(1-3*l)
assert S.expand(deg-(4*l+3*k-k*l))==0
print('degree K^(-12kl) =',S.expand(deg))
print('Nonvanishing proof: gcd(3k,4l)=1 implies gcd(k,4l)=1; degree=0 would give k|4l, hence k=1, then degree=3l+3>0.')
E32=S.zeros(4); E32[2,1]=1
E41=S.zeros(4); E41[3,0]=1
AQ=S.eye(4)-N*m*E32+N*m*E41
AR=S.eye(4)+N*n*E41
assert (AQ-S.eye(4))*(AR-S.eye(4))==S.zeros(4)
assert AQ*AR==AR*AQ
print('Corner nilpotents commute and all pairwise products vanish.')

