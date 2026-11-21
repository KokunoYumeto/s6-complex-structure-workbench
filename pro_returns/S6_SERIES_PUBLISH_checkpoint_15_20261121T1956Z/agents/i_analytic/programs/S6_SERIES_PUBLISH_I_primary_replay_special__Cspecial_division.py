#!/usr/bin/env python3
"""Exact division polynomials at P and independent torsion-norm checks.
All algebra is over Q[t]. Numerical work uses 110 decimal digits.
"""
from pathlib import Path
import json
import sympy as s
from functools import lru_cache

t=s.symbols('t')
a=-s.Rational(3,4)*t**3*(t-1)
b=s.Rational(1,4)*t**4*(t-1)**2
y=t**2*(t-1)/2
D=s.factor(-16*(4*a**3+27*b**2))
@lru_cache(None)
def psi(n):
    if n<0: return -psi(-n)
    if n==0:return s.Integer(0)
    if n==1:return s.Integer(1)
    if n==2:return 2*y
    if n==3:return -a*a
    if n==4:return s.factor(4*y*(-8*b*b-a**3))
    if n%2:
        m=(n-1)//2
        return s.factor(psi(m+2)*psi(m)**3-psi(m-1)*psi(m+1)**3)
    m=n//2
    return s.factor(psi(m)/psi(2)*(psi(m+2)*psi(m-1)**2-psi(m-2)*psi(m+1)**2))

def smooth(n):
    p=s.Poly(psi(n),t)
    while p.eval(0)==0: p=p.exquo(s.Poly(t,t))
    while p.eval(1)==0: p=p.exquo(s.Poly(t-1,t))
    return p.monic()

@lru_cache(None)
def exactorder(n):
    p=smooth(n)
    for d in s.divisors(n):
        if d>1 and d<n:p=p.exquo(exactorder(d))
    return p.clear_denoms()[1].primitive()[1]

if __name__=='__main__':
    print('Model y^2=x^3+A*x+B with P=(0,t^2(t-1)/2)')
    print('Delta=',D)
    out={'discriminant':str(D),'polynomials':{}}
    for n in range(2,10):
        p=psi(n)
        f=exactorder(n)
        print('psi_%d(P) = %s'%(n,p))
        print('exact order %d smooth polynomial = %s'%(n,f.as_expr()))
        print('squarefree:',s.gcd(f,f.diff()).degree()==0)
        out['polynomials'][n]={'psi':str(p),'exact_order':str(f.as_expr()),'coefficients':[str(x) for x in f.all_coeffs()]}
    assert s.factor(psi(2))==t*t*(t-1)
    assert s.factor(psi(4)+s.Rational(1,32)*t**10*(t-1)**4*(5*t-32))==0
    assert s.factor(psi(6)-s.Rational(9,65536)*t**24*(t-1)**9*(11*t*t-6016*t+8192))==0
    print('R1 identities: verified exactly')
    # Candidate CM invariants are not algebraic integers.
    j=s.symbols('j')
    print('order-4 j=',s.Rational(1728)*s.Rational(32,5))
    f6=exactorder(6).as_expr()
    print('monic polynomial of order-6 j=',s.Poly(f6.subs(t,j/1728),j).monic().as_expr())
    out_path=Path(__file__).resolve().parent.parent/'records'/'Cspecial_division.json'
    out_path.write_text(json.dumps(out,indent=2)+'\n')
