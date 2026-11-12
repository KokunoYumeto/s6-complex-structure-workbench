import sympy as S
A1=S.Matrix([[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]])
A2=S.Matrix([[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]])
I=S.eye(4)
M0=(A1*A2).inv()
g,u,w,d=[I[:,i] for i in range(4)]
v1=S.Matrix([1,2,-4,0]); v2=S.Matrix([-1,-3,3,0]); epsp=-v2
N1=I+A1+A1**2; N2=I+A2+A2**2+A2**3
# Engel dictionary (lesson 6, (8.1)-(8.12))
E=S.Matrix([[0,-1,-1,0],[1,-1,0,0],[0,0,1,0],[0,0,0,1]])
L=S.Matrix([[0,1,0,0],[-1,0,-1,0],[0,0,1,0],[0,0,0,1]])
C=S.Matrix([[1,1,0,1],[0,1,0,0],[0,-1,1,0],[0,0,0,1]])
F=C*L*C.inv()
P=S.Matrix([[0,0,0,1],[1,-2,0,2],[1,1,1,-4],[-1,1,0,0]])
print('detP',P.det(), 'A1P=PE^-1',A1*P==P*E.inv(),'A2P=PF^-1',A2*P==P*F.inv(),'M0P=PFE',M0*P==P*F*E)
dE=S.Matrix([-2,-1,3,0]); e4=S.Matrix([0,0,0,1]); f4=C[:,3]
print('P dE = delta^',(P*dE).T,' P^-1 v1',(P.inv()*v1).T,' P^-1 v2 + f4 + dE',(P.inv()*v2+f4+dE).T)
print('E^3,L^4',E**3==I,L**4==I,'(EF)^-1 unipotent',((E*F).inv()-I)**2==S.zeros(4))
# general classification data: source w_j, target w'_j, shift n; solve N_j l_j = w_j - S_n w'_j with l0 in Lambda_tor
def solve(r1,k1,r2,k2,r1p,k1p,r2p,k2p,n):
    Sn=I+n*d*g.T
    w1=r1*v1+k1*d; w2=r2*epsp+k2*d; w1p=r1p*v1+k1p*d; w2p=r2p*epsp+k2p*d
    x=S.symbols('x0:4'); y=S.symbols('y0:4'); l1=S.Matrix(x); l2=S.Matrix(y)
    eqs=list(N1*l1-(w1-Sn*w1p))+list(N2*l2-(w2-Sn*w2p))
    l0=-M0*(l1+A1*l2)
    eqs+=[l0[0],l0[1]]
    sol=S.solve(eqs,list(x)+list(y),dict=True)
    return sol
for args in [(1,0,-1,0, -2,0,3,0, 0),(1,0,-1,0,-2,0,3,0,1),(1,0,-1,0,1,0,-1,1,1),(1,0,-1,0,1,0,-1,1,0),(1,0,-1,0,1,5,-1,0,0),(1,0,-1,0,4,0,-1,0,0),(1,0,1,0,-2,0,5,0,0)]:
    print(args, solve(*args))
