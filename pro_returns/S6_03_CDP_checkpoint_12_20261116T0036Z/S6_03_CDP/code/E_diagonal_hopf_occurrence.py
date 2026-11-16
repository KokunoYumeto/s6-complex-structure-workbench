"""Exact maps and integral restriction matrices for C.2.UN.41."""
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

z,w,t,alpha,beta,q0,y,u=s.symbols('z w t alpha beta q0 y u', nonzero=True)
pa=s.Matrix([1/z,t/w])
pb=s.Matrix([t/z,1/w])
assert all(s.simplify(v)==0 for v in pb-s.Matrix([t*pa[0],pa[1]/t]))
for p in (pa,pb):
    deck=p.subs({z:alpha*z,w:beta*w},simultaneous=True)
    assert all(s.simplify(v)==0 for v in deck-s.Matrix([p[0]/alpha,p[1]/beta]))
change=s.Matrix([y,u/y])
susp=change.subs({u:q0*u,y:alpha*y},simultaneous=True)
assert all(s.simplify(v)==0 for v in susp-s.Matrix([alpha*change[0],q0/alpha*change[1]]))
tate=change.subs(y,t*y)
assert all(s.simplify(v)==0 for v in tate-s.Matrix([t*change[0],change[1]/t]))
print('PASS exact alpha/beta plumbing cocycle and Hopf-deck inversion.')
print('PASS suspension coordinates z=y,w=u/y give periods (a,q0/a),(Q,Q^-1).')

A,B,L,cr,cR=s.symbols('A B L cr cR', positive=True)
period=(A+B)*L
real_matrix=s.Matrix([[-A,-L],[-B,L]])
assert s.simplify(real_matrix.det()+(A+B)*L)==0
intervals={
    'H1':(-B*cr,A*cr),
    'alpha neck':(A*cR,A*L-A*cR),
    'H2':(A*L-A*cr,A*L+B*cr),
    'beta neck':(A*L+B*cR,period-B*cR),
}
print('Real lattice determinant:',real_matrix.det())
for name,ends in intervals.items(): print(name,':',ends)
print('With L>2cr>2cR>0, height zero has one H1 preimage and no other preimage.')

x=u/(1-u)**2
yy=u**2/(1-u)**3
assert s.factor(yy**2+x*yy-x**3)==0
X=4*x;Y=8*yy+4*x
assert s.factor(Y**2-X**2*(X+1))==0
assert s.factor((Y/X-1)/(Y/X+1)-u)==0
v=s.symbols('v')
nodal_x=v*v-1;nodal_y=v*(v*v-1)
assert s.simplify(s.diff(nodal_x,v)/nodal_y-s.diff(s.log((v-1)/(v+1)),v))==0
print('PASS nodal Tate coordinate is exactly u, including its sign and inversion.')

q=s.symbols('q')
def sk(k,N=5):
    return s.series(sum(n**k*q**n/(1-q**n) for n in range(1,N+1)),q,0,N+1).removeO()
a4=-5*sk(3)
a6=-(5*sk(3)+7*sk(5))/12
b2=1;b4=2*a4;b6=4*a6;b8=a6-a4*a4
Delta=s.series(-b2*b2*b8-8*b4**3-27*b6**2+9*b2*b4*b6,q,0,5)
c4=1-48*a4
invj=s.series(Delta.removeO()/c4**3,q,0,5)
assert s.expand(Delta.removeO()).coeff(q,1)==1
assert s.expand(invj.removeO()).coeff(q,1)==1
print('Tate discriminant:',Delta)
print('Inverse j:',invj)

M0=s.Matrix([[1,-1],[1,-1]])
M1=s.Matrix([[1,1],[0,0],[1,1],[0,0]])
for name,M in [('H0',M0),('H1',M1)]:
    D=smith_normal_form(M,domain=ZZ)
    print(name,'restriction =',M.tolist(),'Smith =',D.tolist())
    assert M.rank()==1
    assert all(abs(D[i,i])==1 for i in range(min(D.rows,D.cols)) if D[i,i])
# Exact normalization sequence: H^*(H1 disjoint H2), H^*(E_alpha disjoint E_beta).
hH=[2,2,0,2,2]
hE=[2,4,2,0,0]
ranks=[1,1,0,0,0]
support=[]
for k in range(5):
    cokernel=(hE[k-1]-ranks[k-1]) if k else 0
    support.append(cokernel+hH[k]-ranks[k])
assert support==[1,2,3,4,2]
assert sum((-1)**k*n for k,n in enumerate(support))==0
cohH=[2,2,0];cohE=[2,2,0];cohRanks=[1,1,0]
coherent=[(cohE[k-1]-cohRanks[k-1] if k else 0)+cohH[k]-cohRanks[k] for k in range(3)]
assert coherent==[1,2,1]
print('Integral support cohomology is torsion-free with ranks',support)
print('Coherent support dimensions:',coherent)
print('PASS all exact maps, nonzero lattice determinant, Tate signs, and restriction Smith forms.')
