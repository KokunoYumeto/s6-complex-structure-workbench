"""Exact conductor, normalization, and two fixed-boundary polar calculations."""
from pathlib import Path
import json
import sympy as s
x,y,z,t,a,b,d=s.symbols('x y z t a b d')
k=y+z;h=y*z;g=x*k-y*h;I=[g,x*h,h*h]
M=s.Matrix([[h,0,a],[-k,h,b],[y,-x,d]])
assert s.expand(M.det()-a*g-b*x*h-d*h*h)==0
def intersect(A,B):
    basis=s.groebner([t*q for q in A]+[(1-t)*q for q in B],t,x,y,z)
    return [p.as_expr() for p in basis.polys if not p.as_expr().has(t)]
def colon(q):
    return s.groebner([s.cancel(v/q) for v in intersect(I,[q])],x,y,z)
def same_ideal(A,B):
    G=s.groebner(A,x,y,z);H=s.groebner(B,x,y,z)
    return all(G.reduce(q)[1]==0 for q in B) and all(H.reduce(q)[1]==0 for q in A)
colons={}
for label,q,expected in [('h',h,[x,h]),('x',x,[x*k,h,z*z]),('x2',x*x,[k,h])]:
    basis=[v.as_expr() for v in colon(q).polys]
    assert same_ideal(basis,expected)
    colons[label]=[str(s.factor(v)) for v in basis]
p=y*h*h*(x-h)
assert s.expand(x*h**3-y*g*h*h+y*p)==0
assert s.expand(h**4-y*g*h*h+k*p)==0

# The exact normalization multiplication relations are identities after
# substitution of the two rational adjugate fractions modulo f=0.
A,B,C,D,U=s.symbols('A B C D U')
f=A*g*g+B*g*x*h+C*g*h*h+D*x*x*h*h+U*p
aa=A*g+B*x*h+C*h*h;bb=D*x*h+U*y*h;dd=-U*y*h
v=-g/h;w=-(aa*k+bb*h)/h**2
rels=[A*v*v-B*x*v-C*h*v+D*x*x+U*x*y-U*y*h,
      x*w-A*y*v+B*x*y+(U+C)*y*h,
      v*w-U*h+D*x*y,
      w*w+((U+B)*y+C*k)*w-A*U*k+A*D*y*y-D*(U+C)*y*h-B*U*h]
for rel in rels:
    num,den=s.fraction(s.cancel(rel))
    assert s.rem(num,f,x)==0

# Standard-form polar.
X,K,W=s.symbols('X K W');H=(K*K-W*W)/4
F=X*X*K*K+X*H*H*(K-1)+H**4
xs=-K*K*(K-1)/32;point={X:xs,W:0};critical=12*K*K+7*K-3
grad=[s.factor(s.diff(F,q).subs(point)) for q in (X,K,W)]
assert grad==[0,K**5*critical/512,0]
val=s.factor(F.subs(point));det=s.factor(s.hessian(F,(X,K,W)).det().subs(point))
resultants={}
for name,expr in [('value',val),('Hessian',det)]:
    num=s.fraction(expr)[0]
    assert s.gcd(num,critical)==1
    resultants[name]=str(s.resultant(num,critical,K))

# Mismatch-form polar.
r,T=s.symbols('r T');alpha=T*T-T+1
Phi=T**4*(1-T)**4*r**7*(1+r*alpha)
pt={T:s.Rational(1,2),r:-s.Rational(7,6)}
assert all(s.factor(s.diff(Phi,q).subs(pt))==0 for q in (r,T))
mv=s.factor(Phi.subs(pt));mh=s.hessian(Phi,(r,T)).subs(pt);md=s.factor(mh.det())
assert mv==-s.Rational(823543,573308928)
assert md==s.Rational(1840891197733,427972821516288)

# Rational normal cubic cone after the exact linear transformation.
av,bv,dv,uv,xx,yy,vv,ww=s.symbols('av bv dv uv xx yy vv ww')
old=[av*vv**2-bv*xx*vv+dv*xx**2+uv*xx*yy,
     xx*ww-av*yy*vv+bv*xx*yy,vv*ww+uv*yy**2+dv*xx*yy]
V=av*vv-bv*xx/2;delta=av*dv-bv*bv/4
Y=delta*xx+av*uv*yy;W0=ww+bv*yy/2;NW=av*uv*W0+delta*V
G=s.groebner(old,ww,vv,yy,xx,domain=s.QQ.frac_field(av,bv,dv,uv))
assert all(G.reduce(s.expand(q))[1]==0 for q in [V*V+xx*Y,V*NW+Y*Y,xx*NW-Y*V])

out={'all_checks_passed':True,'adjugate':[[str(q) for q in row] for row in M.adjugate().tolist()],
     'colon_ideals':colons,'ring_condition_generator':str(p),
     'standard_polar':{'critical_polynomial':str(critical),'gradient':[str(q) for q in grad],
       'value':str(val),'Hessian_det':str(det),'nonzero_resultants':resultants},
     'mismatch_polar':{'value':str(mv),'Hessian':[[str(q) for q in row] for row in mh.tolist()],
       'Hessian_det':str(md)},'normalization_tangent_cone':'rational normal cubic cone'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print('Missing-coefficient A3 conductor and polar checks: PASS')
print('Standard polar resultants:',resultants)
print('Mismatch polar value:',mv)
print('Mismatch polar Hessian determinant:',md)
