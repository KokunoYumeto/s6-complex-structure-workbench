import sympy as s
import itertools,json
T,U,V=s.symbols('T U V',real=True)
x,y,b=s.symbols('x y b',real=True)
R=s.Matrix([[6*x,y,1,0],[6*U,T,0,0],[b,x,0,1],[V,U,0,0]])
print('Real period determinant:',s.factor(R.det()))
print('Boundary kernel:',R.subs(V,6*U**2/T).nullspace())
vs=[s.Matrix([1,0]),s.Matrix([0,1]),s.Matrix([1,-1])]
chars=[s.Matrix([[0,1]]),s.Matrix([[1,0]]),s.Matrix([[1,1]])]
fan=set(tuple(e*v) for v in vs for e in [1,-1])
acts=[]
for entries in itertools.product(range(-1,2),repeat=4):
 Q=s.Matrix(2,2,entries)
 if abs(Q.det())!=1 or {tuple(Q*s.Matrix(v)) for v in fan}!=fan:continue
 action=[]
 for j,v in enumerate(vs):
  qv=Q*v
  for k,vk in enumerate(vs):
   for sign in [1,-1]:
    if qv==sign*vk:
     ach=chars[j]*Q.inv()
     m=1 if ach==chars[k] else -1
     assert ach==m*chars[k]
     action.append((k,sign*m))
 acts.append((list(Q),action))
print('Hexagon matrices and gluing coordinate actions:',acts)
print('Distinct actions:',sorted(set(tuple(a) for _,a in acts)))
# First two coordinates g1=-a^-1,g2=a^6. Check all 6 signed permutations symbolically.
a,q,qp=s.symbols('a q qp',nonzero=True)
g=[-1/a,a**6,-q/a**7];gp=[-1/a,a**6,-qp/a**7]
for act in sorted(set(tuple(a) for _,a in acts)):
 eq=[s.factor(gp[k]**e-g[j]) for j,(k,e) in enumerate(act)]
 print('action',act,'equations',eq)
# Exact sign convention: cohomology E = -Im H_E on the actual periods.
G=s.Matrix([[2*T,2*U],[2*U,V/3]])
H=-2*G.inv()
P=s.Matrix([[6*(x+s.I*U),y+s.I*T,1,0],[b+s.I*V,x+s.I*U,0,1]])
print('Im(Pi^T H_eta conjugate(Pi)):',s.simplify(s.im(P.T*H*s.conjugate(P))))
