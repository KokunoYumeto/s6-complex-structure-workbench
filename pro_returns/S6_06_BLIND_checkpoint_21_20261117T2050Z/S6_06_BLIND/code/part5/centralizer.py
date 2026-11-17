from pathlib import Path
import sympy as s
T1=s.Matrix([[1,0,-6,2],[0,-1,1,1],[0,-1,0,1],[0,0,0,1]])
T2=s.Matrix([[1,6,0,-3],[0,0,-1,1],[0,1,0,0],[0,0,0,1]])
A1=T1.inv().T; A2=T2.inv().T
v=s.symbols('x0:16'); P=s.Matrix(4,4,v)
sol=s.linsolve(list(P*A1-A1*P)+list(P*A2-A2*P),v)
print('A1=',A1); print('A2=',A2); print('Centralizer=',sol)
P=P.subs(dict(zip(v,list(sol)[0])))
print('P=',P); print('detP=',s.factor(P.det()))
mu,tau,beta=s.symbols('mu tau beta')
Pi=s.Matrix([[6*mu,tau,1,0],[beta,mu,0,1]])
H=(Pi*P)[:,2:4]
print('H=',H)
print('Hodge obstruction=',s.simplify(H*Pi-Pi*P))
print('Global invariants=',(A1-s.eye(4)).col_join(A2-s.eye(4)).nullspace())
