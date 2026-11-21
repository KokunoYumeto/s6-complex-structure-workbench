"""Exact affine lift for R2 and the 12-shift residual scalar. No numerics."""
import sympy as s
n,tau,mu,beta,c,L0,L1=s.symbols('n tau mu beta c L0 L1')
a=s.Matrix([-s.Rational(7,2)*n*mu-s.Rational(3,2)*n*tau+2*n,
            -s.Rational(7,12)*n*beta-s.Rational(3,2)*n*mu+n*L0/3-n*L1/4])
def sub(expr,rule):
    return expr.subs(rule, simultaneous=True).applyfunc(s.factor)
g1={tau:(tau-1)/tau,mu:(1-mu)/tau,beta:beta+2-6*(1-mu)**2/tau,L0:L0-1}
g2={tau:-1/tau,mu:1+mu/tau,beta:beta-3-6*mu**2/tau,L1:L1-1}
R1=s.Matrix([[-1/tau,0],[(1-mu)/tau,1]])
R2=s.Matrix([[1/tau,0],[-mu/tau,1]])
d1=(sub(a,g1)-R1*a).applyfunc(s.factor)
d2=(sub(a,g2)-R2*a).applyfunc(s.factor)
assert d1==s.Matrix([-n,0])
assert d2==s.Matrix([-n/(2*tau),n*(tau+mu)/(2*tau)])
print('g1 affine defect:',list(d1))
print('g2 affine defect:',list(d2))
g0={tau:tau-1,beta:beta+1,L0:L0+1,L1:L1+1}
d0=(sub(a,g0)-a).applyfunc(s.factor)
assert d0==s.Matrix([s.Rational(3,2)*n,-n/2])
print('g0 affine defect:',list(d0))
Pi_target=s.Matrix([[6*mu,tau,1,0],[beta+c+12,mu,0,1]])
lambda12=s.Matrix([-7,-18,24,0])
res=(a.subs(n,12)-Pi_target*lambda12).applyfunc(s.factor)
assert res==s.Matrix([0,4*L0-3*L1+7*c+84])
print('12-shift lattice vector:',list(lambda12))
print('12-shift residual:',list(res))
print('Exponentiated residual: exp(14*pi*i*c)*t^4/(t-1)^3 = u^(-7)*t^4/(t-1)^3')
B0=s.Matrix([[0,1],[-1,0]])
q12=s.Matrix([-18,6])
fanres=q12-B0*s.Matrix([lambda12[0],lambda12[1]])
assert fanres==s.Matrix([0,-1])
print('Cusp fan residual:',list(fanres))
print('Rational scalar divisor orders at (0,1,infinity): (4,-3,-1); sum 0')
print('All exact checks passed.')
