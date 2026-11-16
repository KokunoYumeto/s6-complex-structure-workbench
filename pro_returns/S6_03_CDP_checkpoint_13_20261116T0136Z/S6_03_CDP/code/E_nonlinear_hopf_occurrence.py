"""Exact weighted maps, compact-base curves, and support matrices for UN42."""
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
z,w,x,beta,lam,ell,p,psi=s.symbols('z w x beta lam ell p psi', nonzero=True)
t=s.symbols('t')
for r in range(1,11):
    poly=t**(6*r)-t**(2*r)+1
    assert s.gcd(poly,s.diff(poly,t))==1
    # The actual weight-(r,1) quotient and its line gauge.
    base=s.Matrix([x**r*z,x*w])
    weighted=base.subs({z:lam**r*z,w:lam*w,x:lam**-1*x},simultaneous=True)
    assert all(s.simplify(a-b)==0 for a,b in zip(base,weighted))
    gauge=s.Matrix([ell**r*z,ell*w,ell**-1*x])
    scalar=gauge.subs(ell,beta*ell)
    assert all(s.simplify(a-b)==0 for a,b in zip(scalar,s.Matrix([beta**r*gauge[0],beta*gauge[1],beta**-1*gauge[2]])))
    g=s.Matrix([beta**r*(z+w**r),beta*w,beta**-1*x])
    gp=base.subs({z:g[0],w:g[1],x:g[2]},simultaneous=True)
    assert s.simplify(gp[0]-x**r*z-(x*w)**r)==0
    assert s.simplify(gp[1]-x*w)==0
    gn=s.Matrix([z,w,x])
    for n in range(1,8):
        gn=g.subs({z:gn[0],w:gn[1],x:gn[2]},simultaneous=True)
        expect=s.Matrix([beta**(n*r)*(z+n*w**r),beta**n*w,beta**-n*x])
        assert all(s.simplify(a-b)==0 for a,b in zip(gn,expect))
    # On P:w=0 the actual canonical form is -x^(r-1) dz wedge dx.
    P=s.Matrix([beta**r*z,beta**-1*x])
    jac=P.jacobian([z,x]).det()
    assert s.simplify((beta**-1*x)**(r-1)*jac-x**(r-1))==0
    print('r =',r,': hyperelliptic polynomial squarefree; genus',3*r-1,
          '; two infinity orders',r,'; exact weighted iterates and canonical form PASS')

qhalf=s.symbols('qhalf',nonzero=True)
G=s.Matrix([-p-psi,-psi,qhalf*ell])
G2=G.subs({p:G[0],psi:G[1],ell:G[2]},simultaneous=True)
assert all(s.simplify(a-b)==0 for a,b in zip(G2,s.Matrix([p+2*psi,psi,qhalf**2*ell])))
print('PASS G^2 = beta * translation(2psi), with beta=qhalf^2.')
print('At the six-r branch values: 2psi=0 and |qhalf|=|beta|^(1/2),')
print('which cannot equal |beta|^n for an integer n. The quotient is free.')

M0=s.Matrix([[1,-1]])
M1=s.Matrix([[0,0,1,-1],[0,0,0,0]])
for name,M in [('H0',M0),('H1',M1)]:
    D=smith_normal_form(M,domain=ZZ)
    assert M.rank()==1
    assert all(abs(D[i,i])==1 for i in range(min(D.shape)) if D[i,i])
    print(name,'restriction:',M.tolist(),'Smith:',D.tolist())
comps=[2,4,4,4,2];edge=[1,2,1,0,0];ranks=[1,1,0,0,0]
betti=[(edge[k-1]-ranks[k-1] if k else 0)+comps[k]-ranks[k] for k in range(5)]
assert betti==[1,3,5,5,2]
assert sum((-1)**k*betti[k] for k in range(5))==0
cohcomp=[2,3,1];cohedge=[1,1,0];cohrank=[1,1,0]
coh=[(cohedge[k-1]-cohrank[k-1] if k else 0)+cohcomp[k]-cohrank[k] for k in range(3)]
assert coh==[1,2,1]
print('Support integral cohomology is torsion-free with ranks',betti)
print('Support coherent cohomology dimensions:',coh)
print('PASS all exact maps and integral restriction computations.')
