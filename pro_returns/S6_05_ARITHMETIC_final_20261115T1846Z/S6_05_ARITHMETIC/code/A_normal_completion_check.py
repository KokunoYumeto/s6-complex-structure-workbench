"""Exact finite Fourier completion of the radial Salié family."""
from math import gcd
from pathlib import Path
import sympy as sp
from B_A5_salie_audit import jacobi, salie_coeffs

ROOT = Path(__file__).resolve().parents[1]
x = sp.Symbol("x")

def conv(a,b):
    n=len(a); out=[0]*n
    for j,v in enumerate(a):
        if v:
            for k,w in enumerate(b):
                if w:
                    out[(j+k)%n] += v*w
    return out

def kloosterman(m,n,q):
    out=[0]*q
    for a in range(q):
        if gcd(a,q)==1:
            out[(m*a+n*pow(a,-1,q))%q]+=1
    return out

def gauss(q):
    out=[0]*q
    for a in range(q):
        out[a*a%q]+=1
    return out

def zero_at_root(a,q):
    p=sp.Poly.from_list(list(reversed(a)),x,domain=sp.ZZ)
    return p.rem(sp.Poly(sp.cyclotomic_poly(q,x),x,domain=sp.ZZ)).is_zero

def main():
    moduli=(5,7,11,13,17,25,35,49)
    shifts=(0,1,3,6,-2)
    ds=(-18,6,-12,0)
    count=0
    for q in moduli:
        b=pow(72,-1,q)
        for d in ds:
            for h in shifts:
                lhs=[0]*q
                for k in range(q):
                    t=salie_coeffs(2,b*(k*k+d),q)
                    for j,v in enumerate(t):
                        lhs[(j-h*k)%q]+=v
                rhs=conv(gauss(q),kloosterman(2-18*h*h,b*d,q))
                assert zero_at_root([a-jacobi(2,q)*b for a,b in zip(lhs,rhs)],q)
                count+=1
    print("PASS: finite Fourier completion in the exact cyclotomic ring:",count,"cases")
    print("q =",moduli,"; h =",shifts,"; d =",ds)
    print("sum_k T(2,bar72*(k^2+d);q)*e(-h*k/q)")
    print("  = Jacobi(2,q)*G(1;q)*S(2-18*h^2,bar72*d;q)")

    count=0
    for q in moduli:
        for h in shifts:
            m=2-18*h*h
            a=kloosterman(m,-pow(4,-1,q),q)
            lhs=[0]*(2*q)
            for j,v in enumerate(a):
                lhs[2*j]=v
            rhs=kloosterman(m,-1,2*q)
            assert zero_at_root([v+w for v,w in zip(lhs,rhs)],2*q)
            count+=1
    print("PASS: ordinary Kloosterman replacement at modulus 2q:",count,"cases")
    print("S(2-18*h^2,-bar4;q) = -S(2-18*h^2,-1;2q)")
    print("No square-root bound for the full count is inferred from these identities.")

if __name__=="__main__":
    main()
