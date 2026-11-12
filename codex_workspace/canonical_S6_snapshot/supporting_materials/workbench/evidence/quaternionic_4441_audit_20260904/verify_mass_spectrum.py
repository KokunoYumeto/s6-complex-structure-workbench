"""Exact retained-metric gauge inertia and vacuum-spectrum calculation."""
import sympy as S

count=0
def check(name,a,b=0):
    global count
    r=a-b
    entries=list(r) if isinstance(r,S.MatrixBase) else [r]
    assert all(S.cancel(S.expand(e))==0 for e in entries),name
    count+=1
    print("PASS",count,name)

chi,t,r,g2=S.symbols("chi t r g2",real=True)
I=S.I
Phi=chi*S.diag((1+3*t)/2,(1-3*t)/2,-1)
b=S.Matrix([0,0,r])
bb=b*b.H
r2=9*chi**2*(1-t**2)/4
comm=lambda x,y:x*y-y*x
tf=lambda x:x-S.trace(x)*S.eye(3)/3
inertia=lambda z:tf(comm(Phi,comm(Phi,z))+bb*z+z*bb)
def reduce_r(mat):
    return mat.applyfunc(lambda e:S.expand(e).subs(r**2,r2))
gens=[]
names=[]
for i,j in [(0,1),(0,2),(1,2)]:
    e=S.zeros(3);e[i,j]=1;e[j,i]=-1
    f=S.zeros(3);f[i,j]=I;f[j,i]=I
    gens += [e,f]
    names += [str(i+1)+str(j+1)+"real",str(i+1)+str(j+1)+"imag"]
gens += [I*S.diag(1,-1,0),I*S.diag(1,1,-2)]
names += ["Cartan zero","Cartan nonzero"]
lambdas=[9*chi**2*t**2]*2+[S.Rational(9,2)*chi**2*(1+t)]*2+[
    S.Rational(9,2)*chi**2*(1-t)]*2+[S.Integer(0),3*chi**2*(1-t**2)]
metric=S.Matrix([[-S.trace(v*w) for w in gens] for v in gens])
check("retained unscaled su3 generator metric",metric,S.diag(2,2,2,2,2,2,2,6))
for z,lam,name in zip(gens,lambdas,names):
    check("inertia eigenvector "+name,reduce_r(inertia(z)),lam*z)
    check("spatial matter current "+name,
          tf(comm(Phi,comm(z,Phi))-bb*z-z*bb),-inertia(z))
mat=S.Matrix([[-S.trace(v*inertia(w)) for w in gens] for v in gens])
mat=reduce_r(mat)
check("generalized Hessian with full trace metric",mat,metric*S.diag(*lambdas))
check("trace inertia",sum(lambdas),chi**2*(21+15*t**2))
check("trace squared inertia",sum(e**2 for e in lambdas),chi**4*(90+63*t**2+171*t**4))
delta=S.symbols("delta",real=True)
check("trace in invariant delta",S.expand(sum(lambdas)).subs(t**2,1-delta),chi**2*(36-15*delta))
check("squared trace in invariant delta",
      S.expand(sum(e**2 for e in lambdas)).subs(t**4,(1-delta)**2).subs(t**2,1-delta),
      chi**4*(324-405*delta+171*delta**2))
check("mass and Lorentz-average invariant",g2*lambdas[-1]/2,2*g2*r2/3)
a,phase=S.symbols("a phase",real=True)
T=I*S.diag(1,1,-2)
Db=T*b*a+I*phase*b
j=-I*((b.H*Db)[0]-(Db.H*b)[0])
check("exact vector-current linear coefficient",j,-4*r**2*a+2*r**2*phase)
for z in gens[:-1]:
    Db=z*b*a
    check("other generator has zero vector current",
          -I*((b.H*Db)[0]-(Db.H*b)[0]))
assert sum(e.subs(t,1)==0 for e in lambdas)==4
count+=1
assert sum(e.subs(t,0)==0 for e in lambdas)==3
count+=1
assert sum(e.subs(t,S.Rational(1,2))==9*chi**2/4 for e in lambdas)==5
count+=1
q=S.symbols("q",real=True)
poly=S.prod(q-e for e in lambdas)
check("eight-dimensional characteristic polynomial",poly,
      q*(q-3*chi**2*(1-t**2))*(q-9*chi**2*t**2)**2
      *(q-S.Rational(9,2)*chi**2*(1+t))**2
      *(q-S.Rational(9,2)*chi**2*(1-t))**2)
print("ALL",count,"EXACT CHECKS PASSED")
print("SymPy",S.__version__)
