"""Symbolic candidate on the exceptional line and a stated finite test.

The polynomial identities are proved over Z[n].  The complete homology
tests in this file are run only at n=-4,-3,...,8; no extrapolation is made.
"""
import sympy as S
from fourfolds_survivor_test import test_pair, factors

def full_pair(n):
    A=S.Matrix([[1,0,1,-1,-1,0],
                [0,1,0,0,-4,0],
                [0,0,0,0,-4,-1],
                [0,0,1,0,-3,0],
                [0,0,0,1,-2,0],
                [0,0,0,0,5,1]])
    B=S.Matrix([[1,0,0,0,0,0],
                [0,-2*n-5,4,2*n+4,2*n-4,0],
                [0,-2*n-4,3,2*n+4,2*n-4,0],
                [0,-n-3,2,n+2,n-1,0],
                [0,-n-1,1,n+1,n-2,0],
                [0,2*n+8,-5,-2*n-5,4-2*n,1]])
    return A,B

if __name__=='__main__':
    n=S.Symbol('n',integer=True);A,B=full_pair(n);I=S.eye(6)
    assert (A**5-I).applyfunc(S.expand)==S.zeros(6)
    assert (B**4-I).applyfunc(S.expand)==S.zeros(6)
    assert ((A*B-I)**2).applyfunc(S.expand)==S.zeros(6)
    print('ALL SYMBOLIC FINITE-ORDER AND SQUARE-ZERO IDENTITIES PASSED',flush=True)
    for n in range(-4,9):
        A,B=full_pair(n)
        fs=factors(A*B-S.eye(6))
        print('PARAMETER',n,'cusp Smith',fs,flush=True)
        if fs!=[1,1,1]:continue
        result=test_pair(A.T,B.T)
        if not result['passes']:print(result,flush=True)
    print('ALL THIRTEEN SPECIFIED PARAMETER TESTS COMPLETED',flush=True)
