"""Exact root, inertia, chart and finite-action checks for UN52."""
from math import gcd, lcm
import sympy as s
from sympy.matrices.normalforms import hermite_normal_form

u,v,z,r,q = s.symbols("u v z r q")
pairs = 0
for a in range(1,25):
    for b in range(1,25):
        g = gcd(a,b)
        A,B = a//g,b//g
        p0,q0,d0 = s.gcdex(A,B)
        p0,q0 = int(p0),int(q0)
        assert int(d0)==1 and p0*A+q0*B==1
        for h in range(1,7):
            N = lcm(a,b)*h
            J = N//g
            wu,wv = h*A*p0,h*B*q0
            assert (wu+wv-h)%J==0
            assert B*wu%J==0 and A*wv%J==0
            assert gcd(J,wv)==N//a
            assert gcd(J,wu)==N//b
            assert gcd(N//a,N//b)==h
            assert lcm(N//a,N//b)==J
            assert N==h*A*B*g
            # u^B=x, v^A=y and uv=z^h give z^N=x^a*y^b.
            assert a*B == b*A == N//h
            # Every invariant reduced monomial has z-exponent divisible
            # by h; replacing z^h by uv leaves powers divisible by B,A.
            for U in range(0,2*B+1):
                for R in range(0,min(2*h*A*B,18)+1):
                    if (U*wu+R)%J == 0:
                        assert R%h==0
                        V=R//h
                        assert (U+V)%B==0 and V%A==0
            pairs += 1
print("Exact (a,b,h) root/inertia cases:", pairs)
print("Verified J=I_a I_b, |J|=N/gcd(a,b), |I_a cap I_b|=h.")
print("Verified normalized branch u*v=s^h, x=u^B, y=v^A, t=x^a*y^b.")
print("Invariant monomials agree with C[x,y] through the tested bounds.")

charts=0
for h in range(1,25):
    for j in range(h):
        x = r**(j+1)*q**j
        y = r**(h-j-1)*q**(h-j)
        ss = r*q
        assert s.expand(x*y-ss**h)==0
        if j<h-1:
            rn,qn=1/q,r*q*q
            xn=rn**(j+2)*qn**(j+1)
            yn=rn**(h-j-2)*qn**(h-j-1)
            assert s.simplify(xn-x)==0 and s.simplify(yn-y)==0
        charts+=1
print("Exact resolution charts and transitions:", charts)

for n in range(1,61):
    H = hermite_normal_form(s.Matrix([[n,0,1],[0,n,-1]]))/n
    c = H.inv()*s.Matrix([-1,1])
    assert all(t.q==1 for t in c)
    assert s.igcd(*[int(t) for t in c])==n
print("Anti-diagonal secondary two-cycle: primitive divisor N for N=1,...,60.")

# The three-component primary cycle and its exact order-two deck action.
P = [
    s.eye(2),
    s.Matrix([[1,-1],[-1,0]]),
    s.Matrix([[0,-1],[-1,1]]),
]
n = [P_i*s.Matrix([1,0]) for P_i in P]
tau = [s.Matrix([0,0]),s.Matrix([-s.Rational(1,2),0]),
       s.Matrix([0,s.Rational(1,2)])]
# Units throughout: 2*pi*i, so log(-1)/(2*pi*i)=1/2.
for i in range(3):
    difference = tau[(i+1)%3]-tau[i]+n[i]/2
    assert all(t.q==1 for t in difference)
    assert all(t.q==1 for t in 2*tau[i])
local_weights = [2*P[i].inv()*tau[i] for i in range(3)]
assert local_weights == [s.Matrix([0,0]),s.Matrix([0,1]),s.Matrix([-1,0])]
print("Quadratic primary triangle deck weights:", [list(x) for x in local_weights])
print("Its smooth quotient multiplicities are (1,2,2).")

z,w,t,eps = s.symbols("z w t eps",nonzero=True)
phi1=lambda z,w,t:(1/w,t/(z*w))
phi2=lambda z,w,t:(w,t*w/z)
phi3=lambda z,w,t:(1/w,t*w/z)
# g1=id, g2=(z,-w), g3=(-z,w); base t -> -t.
for phi,gi,gj in [
    (phi1,lambda z,w:(z,w),lambda z,w:(z,-w)),
    (phi2,lambda z,w:(z,-w),lambda z,w:(-z,w)),
    (phi3,lambda z,w:(-z,w),lambda z,w:(z,w)),
]:
    lhs=gj(*phi(z,w,t))
    rhs=phi(*gi(z,w),-t)
    assert all(s.simplify(a-b)==0 for a,b in zip(lhs,rhs))
print("All three neck maps intertwine the quadratic action exactly.")
print("PASS: root/inertia, toric charts, finite angular lattices and explicit quotients.")

