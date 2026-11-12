"""Exact algebra plus separately labelled finite numerical illustrations.
Analytic and nonlinear convergence are proved in companion notes, not here.
"""
import argparse
import json
import math
from pathlib import Path
import sympy as s

def run():
    k=s.Rational(3,2)
    j=s.Symbol("j", positive=True)
    z,x=s.symbols("z x")
    c,cj,q,b,d,r=s.symbols("c c_j q b d r", real=True)
    exact=[]; numerical=[]
    def check(name,left,right):
        error=s.cancel(s.expand(left-right))
        assert error==0,(name,error)
        exact.append({"name":name,"passed":True})
    for n in range(13):
        check(f"binomial coefficient n={n}",
              s.diff((1-x)**(-k),x,n).subs(x,0)/s.factorial(n),
              s.rf(k,n)/s.factorial(n))
    pgf=(1+j*(1-z))**(-k)
    check("full mass",pgf.subs(z,1),1)
    check("first positive-channel raw moment",s.diff(pgf,z).subs(z,1),k*j)
    check("second positive-channel raw moment",
          (s.diff(pgf,z,2)+s.diff(pgf,z)).subs(z,1),k*j+k*(k+1)*j*j)
    error=(cj/j)**2*(j*q+j*j*q*q)-2*(cj/j)*c*q*(j*q)+c*c*q*q
    check("conditional Poisson square",error,cj*cj*q/j+(cj-c)**2*q*q)
    poly=s.Poly(s.expand(error),q)
    check("Gamma-Poisson integrated square",
          poly.coeff_monomial(q)*k+poly.coeff_monomial(q*q)*k*(k+1),
          cj*cj*k/j+(cj-c)**2*k*(k+1))
    check("mixed complex amplitude denominator",
          (1+s.I*b*r)*(1-s.I*d*r)-b*d*r*r*z,
          1+b*d*r*r*(1-z)+s.I*(b-d)*r)
    t=s.Symbol("t",positive=True)
    cp=s.Symbol("c_positive",positive=True)
    for order in range(4):
        lhs=s.diff((1+cp*t)**(-k),t,order)
        rhs=(-1)**order*s.rf(k,order)*cp**order*(1+cp*t)**(-k-order)
        check(f"Gamma derivative r={order}",lhs,rhs)
    scale=100.0*math.sqrt(2.0)*math.pi
    for index in (2,3,10,100):
        lam=400.0*math.sqrt(2.0)*index*math.sin(math.pi/(4*index**2+2))
        time=0.2
        closed=(1+index*(-math.expm1(-time*lam)))**(-1.5)-(index+1)**(-1.5)
        term=(index+1)**(-1.5)
        terms=[]
        for n in range(1,20001):
            term*=((1.5+n-1)/n)*index/(index+1)
            terms.append(term*math.exp(-time*lam*n))
        error=abs(math.fsum(terms)-closed)
        assert error<2e-12
        numerical.append({"name":f"truncated series j={index}","terms":20000,
                          "absolute_error":error,"tolerance":2e-12,"passed":True})
    for index in (100,1000,10000):
        scaled=400.0*math.sqrt(2.0)*index**2*math.sin(math.pi/(4*index**2+2))
        bound=scale/(2*index**2+1)+400*math.sqrt(2)*math.pi**3*index**2/(6*(4*index**2+2)**3)
        error=scale-scaled
        assert -1e-12<=error<=bound+1e-12
        numerical.append({"name":f"scale-bound illustration j={index}",
                          "difference":error,"bound":bound,"roundoff":1e-12,"passed":True})
    return {"scope":"Exact finite algebra; numerical illustrations are not analytic proofs.",
            "not_certified":["Nonlinear fixed-box convergence","Infinite measure limits",
                             "Interacting four-dimensional continuum or mass gap"],
            "sympy_version":s.__version__,"exact_algebra":exact,
            "numerical_illustrations":numerical,
            "counts":{"exact_algebra":len(exact),"numerical_illustrations":len(numerical)},
            "all_passed":True}

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--output",type=Path)
    args=parser.parse_args()
    payload=json.dumps(run(),indent=2,ensure_ascii=False)+"\n"
    if args.output is not None:
        args.output.write_text(payload,encoding="utf-8")
    print(payload)
