"""Exact comparison of the displayed integral monodromy representations."""
from sympy import Matrix, symbols, linsolve, eye
from itertools import product

A1=Matrix([[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]])
A2=Matrix([[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]])
T0=Matrix([[0,-1,-1,0],[1,-1,0,0],[0,0,1,0],[0,0,0,1]])
T1=Matrix([[-1,1,-1,2],[-1,0,-1,1],[1,1,2,-1],[0,0,0,1]])
v=symbols('q0:16')
Q=Matrix(4,4,v)
print('A1^3=I:',A1**3==eye(4),'A2^4=I:',A2**4==eye(4))
for exponent in (1,-1):
    equations=list(T0*Q-Q*A1**exponent)+list(T1*Q-Q*A2**exponent)
    sol=list(linsolve(equations,v))[0]
    free=sorted(set().union(*(x.free_symbols for x in sol)),key=str)
    S=Matrix(4,4,sol)
    print('Exponent',exponent,'symbolic intertwiner',S,'det=',S.det().factor())
    found=None
    for values in product(range(-3,4),repeat=len(free)):
        M=S.subs(dict(zip(free,values)))
        if all(x.q==1 for x in M) and abs(M.det())==1:
            found=M
            break
    print('Integral unimodular example:',found)
    if found is not None:
        print('det=',found.det(),'; inverse=',found.inv())
        assert T0*found==found*A1**exponent
        assert T1*found==found*A2**exponent

# The convention actually used in the paper: positive C* circle and gamma.
Qchosen=Matrix([[2,-1,0,-2],[2,-1,0,-1],[0,2,1,3],[1,0,0,0]])
print('Chosen clockwise-to-counterclockwise dictionary Q=',Qchosen)
print('Chosen inverse=',Qchosen.inv(),'det=',Qchosen.det())
assert T0*Qchosen==Qchosen*A1.inv()
assert T1*Qchosen==Qchosen*A2.inv()
assert Qchosen[:,3]==Matrix([-2,-1,3,0])
M0=(A1*A2).inv(); Tinf=(T0*T1).inv()
assert Qchosen*M0*Qchosen.inv()==T0.inv()*Tinf.inv()*T0
print('All two finite monodromy and cusp path-conjugation identities verified exactly.')
