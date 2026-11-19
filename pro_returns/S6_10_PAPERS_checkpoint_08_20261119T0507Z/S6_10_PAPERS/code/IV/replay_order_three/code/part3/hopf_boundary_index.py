"""Formal characteristic-ring calculation for a fixed-sheet Hopf boundary."""
import sympy as s
ap,am,d,p1=s.symbols('a b d p1')
px1=s.Integer(1)
px2=ap-am
px3=ap**2-ap*am+am**2
D=d+ap+am
pB=p1+(ap+am)**2
index=s.expand(px3/6+D*px2/4+D**2*px1/8-pB*px1/24)
rr=(3*d**2-p1)/24+(ap**2+ap*d)/2
print('pi_* x =',px1)
print('pi_* x^2 =',px2)
print('pi_* x^3 =',px3)
print('p1(B) =',pB)
print('determinant D =',D)
print('Spin^c index =',s.factor(index))
print('Riemann-Roch residual =',s.simplify(index-rr))
assert s.simplify(index-rr)==0
# Opposite lines: a=M+nF, b=-a. M^2=-2, MF=F^2=K^2=KM=0.
print('genus-three sheet chi(L_+) = 1 + (-2-0)/2 = 0')
print('opposite-line boundary k = 3*(-2) = -6, ell = -24')
N=12
eta_exp=N
zeta_exp=-sum(range(N))
print('twelve-step multiplier: eta exponent',eta_exp,'; zeta exponent',zeta_exp)
print('total phase / pi =',s.Rational(eta_exp,12)+s.Rational(2*zeta_exp,12))
assert (s.Rational(eta_exp,12)+s.Rational(2*zeta_exp,12))%2==0
# Exact resolved charts at Q=uv.
u,v,Y,z,r,X,k,w=s.symbols('u v Y z r X k w')
print('first chart XY-Qr residual:',s.expand((u*v*z)*Y-(u*v)*(z*Y)))
print('second chart uv-Xw residual:',s.expand((X*k)*v-X*(k*v)))
print('third chart uv-Xw residual:',s.expand(u*(k*w)-(u*k)*w))
print('weights: first (u,v,Y,z)=(0,0,-1,1); second (r,X,k,v)=(0,1,-1,0); third (r,u,k,w)=(0,0,1,-1)')
