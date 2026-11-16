"""Exact bounded order probes on the exceptional (5,4) rational line.

Parameters are exactly integers n=-2,-1,0,1,2,3,4, with z=n/5.
Only assertions explicitly verified for that list are reported; no universal
integer or survivor claim is inferred from it.
"""
import sympy as S
from fourfolds_lattice_algorithm import order_and_conductor
from fourfolds_two_classes_lattices import factors
J=S.Matrix([[0,0,0,-1],[1,0,0,-1],[0,1,0,-1],[0,0,1,-1]])
A=S.diag(1,J);I=S.eye(5);X=S.Matrix([[0,1],[1,0],[0,4],[0,1],[0,3]])

def pair(n):
    z=S.Rational(n,5)
    Y=S.Matrix([[4*z+S.Rational(16,5),0,-2*z-1,S.Rational(4,5)-2*z,2*z],
                 [2*z-S.Rational(2,5),0,-z,S.Rational(2,5)-z,z]])
    C=(I+X*Y)*A
    assert C**4==I and (C*A.inv()-I)**2==S.zeros(5)
    assert (Y*A*X).det()==n and S.trace(A*A*C*C)==2
    return A,C

if __name__=='__main__':
    for n in range(-2,5):
        AA,C=pair(n)
        print('EXCEPTIONAL PARAMETER n=',n,flush=True)
        result=order_and_conductor(AA,C)
        if not result['stable_lattice']:
            print(result,flush=True);continue
        L=result['lattice_basis'];An=L.inv()*AA*L;Cn=L.inv()*C*L
        print('quotient cusp Smith',factors(Cn*An.inv()-I),flush=True)
        print('global cohomology coinvariant Smith',factors(S.Matrix.hstack(An-I,Cn-I)),flush=True)
    print('ALL SEVEN BOUNDED ORDER PROBES FINISHED',flush=True)
