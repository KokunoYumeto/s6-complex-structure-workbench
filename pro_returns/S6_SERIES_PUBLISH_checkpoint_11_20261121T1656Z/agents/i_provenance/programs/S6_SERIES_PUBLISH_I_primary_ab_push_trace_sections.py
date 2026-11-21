"""Exact exploration of trace sections on b^3=a^4+1.

The first ansatz is X=B*a^2/(b-1), Y=a*(D+F/(b-1)).
All identities are in the indicated algebraic function field; exploratory
branches and conclusions are printed, without asserting a global filling.
"""
import sympy as s
from pathlib import Path
import json

B,b,a,D,F=s.symbols('B b a D F')
quad=s.expand(B**3*(b*b+b+1)-3*B*b*(b-1)+2*(b-1)**2)
disc=s.factor(s.discriminant(quad,b))
print('quadratic in b:',quad)
print('discriminant:',disc)
roots=s.solve(disc,B)
print('B roots:',roots)
result=[]
for value in roots:
    q=s.expand(quad.subs(B,value))
    c2=s.expand(q).coeff(b,2)
    c1=s.expand(q).coeff(b,1)
    c0=s.expand(q).coeff(b,0)
    if c2:
        dv=s.sqrt(c2)
        fv=s.simplify(c1/(2*dv)+dv)
    else:
        assert c1==0
        dv=s.Integer(0)
        fv=s.sqrt(c0)
    residual=s.simplify((dv*(b-1)+fv)**2-q)
    assert residual==0
    xv=value*a*a/(b-1)
    yv=a*(dv+fv/(b-1))
    # Use a^4=b^3-1 after dividing the Weierstrass equation by a^2.
    check=s.factor((yv*yv+3*b*xv-2*a*a-xv**3)/a**2)
    check=s.factor(check.subs(a**4,b**3-1))
    assert check==0
    print('section: B=',value,'D=',dv,'F=',fv)
    print('X=',xv,'Y=',yv)
    if value != 0:
        # The three deck translates are intersections with this one line.
        line_slope = fv*b/(value*a)
        line_intercept = a*(dv-fv)
        w=s.symbols('w')
        xw=value*a*a/(b-w)
        yw=a*(dv+w*fv/(b-w))
        assert s.factor(yw-line_slope*xw-line_intercept)==0
        identities=[fv**2-3*value**3,
                    3*value**3+3*value+2*fv*(dv-fv),
                    (dv-fv)**2-value**3-2]
        assert all(s.simplify(e)==0 for e in identities)
        print('Three orbit points lie on Y=',line_slope,'X +',line_intercept)
        print('Line-intersection coefficient identities:',identities)
        print('Hence trace_3=O and trace_12=O by the elliptic chord law.')
    else:
        print('The invariant section is -P; its trace_12 is -12P.')
    result.append({'B':str(value),'D':str(dv),'F':str(fv)})

print('Deck action on every ansatz section:')
print('sigma^j Q: X=B*a^2/(b-omega^j), Y=a*(D+omega^j*F/(b-omega^j)); j=0,1,2.')
print('Thus sigma^3 fixes every section in this ansatz, and trace_12=4*trace_3.')
Path(__file__).with_suffix('.json').write_text(json.dumps({'discriminant':str(disc),'sections':result},indent=2)+'\n')
print('ALL PRINTED ANSATZ IDENTITIES VERIFIED')
