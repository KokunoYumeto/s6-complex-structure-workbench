import sympy as s
from itertools import combinations
from pathlib import Path
A=s.Matrix([[1,0,0,1,-1,1],[0,1,-1,-1,1,0],[0,1,0,-1,0,0],[0,2,-1,-1,0,1],[0,2,0,-1,0,0],[0,1,1,-1,0,0]])
B=s.Matrix([[1,0,0,0,0,0],[0,0,-1,0,1,0],[0,0,-1,0,0,1],[0,0,-1,0,0,0],[0,1,-1,0,0,0],[0,0,-1,1,0,0]])
Cf=s.Matrix([[0,0,0,-1],[1,0,0,-1],[0,1,0,-1],[0,0,1,-1]])
Cg=s.Matrix([[0,0,0,-1],[1,0,0,0],[0,1,0,0],[0,0,1,0]])
S=s.Matrix([[0,0,0,1,0,0],[0,1,0,0,0,0],[0,0,1,0,0,0],[-1,0,0,0,1,0],[1,0,0,0,0,1],[-1,0,0,0,0,0]])
pairs=list(combinations(range(4),2))
def ext(M):return s.Matrix([[M.extract(i,j).det() for j in pairs] for i in pairs])
def wedge(u,v):return s.Matrix([u[i]*v[j]-u[j]*v[i] for i,j in pairs])
w=s.ones(6,1); Q=s.eye(6);Q[:,0]=w; pi=Q.inv()[1:,:]
k=s.Matrix([[1,-1,1,1,-1,1]])
J=s.zeros(4)
for n,(i,j) in enumerate(pairs):J[i,j]=k[n];J[j,i]=-k[n]
C=Cf*Cg.inv();NH=C-s.eye(4)
T=(B*A).inv();N=T-s.eye(6)
lines=[]
def out(name,x): lines.append(name+' = '+str(x))
for name,x in [('Cf',Cf),('Cg',Cg),('Q',Q),('pi',pi),('J',J),('C',C),('NH',NH),('T',T),('N',N),('A5',A**5),('B4',B**4),('N2',N*N),('N_rank',N.rank()),('NH2',NH*NH),('NH_rank',NH.rank()),('A_lower_minus_quotient',A[1:,1:]-(Q.inv()*ext(Cf.inv())*Q)[1:,1:]),('B_lower_minus_quotient',B[1:,1:]-(Q.inv()*ext(Cg)*Q)[1:,1:]),('Sdet',S.det()),('S_cohomology_cusp',S.T.inv()*T*S.T),('S_homology_cusp',S.inv()*(A.T*B.T).inv()*S),('N_colspace',s.Matrix.hstack(*N.columnspace())),('N_nullspace',s.Matrix.hstack(*N.nullspace()))]:out(name,x)
# symbolic canonical-root vector u and rank-three exterior image
u=s.Matrix(s.symbols('u0:4'));U=s.Matrix.hstack(*[pi*wedge(u,s.eye(4)[:,j]) for j in range(4)])
nu5=s.Matrix.vstack(s.zeros(1,4),U);NU=N*nu5
out('U',U);out('N_liftU',NU);out('3x3 minors N_liftU',[(idx,s.factor(NU.extract(range(6),idx).T*NU.extract(range(6),idx))) for idx in []])
minors={}
for rows in combinations(range(6),3):
 for cols in combinations(range(4),3):
  v=s.factor(NU.extract(rows,cols).det())
  if v: minors[str((rows,cols))]=v
out('nonzero_NU_minors',minors)
Path('audit_p18_independent_10/fresh_matrix_output.txt').write_text('\n\n'.join(lines)+'\n')
print('\n\n'.join(lines))
R=S.T
Tc=R*T*R.inv()
X=(R*nu5)[:3,:]
D=s.Matrix.hstack(*[wedge(u,s.eye(4)[:,j]) for j in range(4)])
acoeff=(k*D)[:,1:4]*X[:,1:4].inv()
new=[]
new.append('T_in_correct_S_dual_coordinates = '+str(Tc))
new.append('e_in_correct_S_dual_coordinates = '+str(R*s.eye(6)[:,0]))
new.append('top_projection_X = '+str(X))
new.append('det_X_columns_123 = '+str(s.factor(X[:,1:4].det())))
new.append('alpha_graph_row = '+str(acoeff.applyfunc(s.factor)))
new.append('alpha_graph_identity_remainder = '+str((acoeff*X-k*D).applyfunc(s.simplify)))
with Path('audit_p18_independent_10/fresh_matrix_output.txt').open('a') as f:f.write('\n'.join(new)+'\n')
print('\n'.join(new))
# Additional independent assertions for the complete written derivation.
assert A**5==s.eye(6) and B**4==s.eye(6)
assert Cg**4==-s.eye(4)
assert Cf.T*J*Cf==J and Cg.T*J*Cg==J
assert N*N==s.zeros(6) and N.rank()==3
assert NH*NH==s.zeros(4) and NH.rank()==1
assert A[1:,1:]==(Q.inv()*ext(Cf.inv())*Q)[1:,1:]
assert B[1:,1:]==(Q.inv()*ext(Cg)*Q)[1:,1:]
assert Tc==s.BlockMatrix([[s.eye(3),s.zeros(3)],[s.eye(3),s.eye(3)]]).as_explicit()
assert s.factor(X[:,1:4].det())==u[0]**3
assert (acoeff*X-k*D).applyfunc(s.simplify)==s.zeros(1,4)
Omega=s.zeros(4)
for i,j in pairs:Omega[i,j]=1;Omega[j,i]=-1
assert J*Omega==-s.eye(4)
d0=s.Matrix([0,1,1,1]);assert J*d0==s.eye(4)[:,0]
w0=s.Matrix(s.symbols('w0:4'));wb=s.Matrix(s.symbols('v0:4'))
z,zb=s.symbols('z zb');uu=w0+z*w0[0]*d0;ub=wb+zb*wb[0]*d0
beta=(uu.T*J*ub)[0];beta_base=(w0.T*J*wb)[0]
assert s.expand(beta-beta_base-(zb-z)*w0[0]*wb[0])==0
chi=(R*s.Matrix.vstack(s.zeros(1,1),pi*wedge(uu,ub)))[:3,:]
chi_base=(R*s.Matrix.vstack(s.zeros(1,1),pi*wedge(w0,wb)))[:3,:]
assert (chi-chi_base-s.Matrix([(zb-z)*w0[0]*wb[0],0,0])).applyfunc(s.expand)==s.zeros(3,1)
x,rr,ll,xc=s.symbols('x r l xc')
poly=x**5-5*xc**4*x+ll**4
G=x**3+2*xc*x**2+3*xc**2*x+4*xc**3
assert s.expand(poly-(ll**4-4*xc**5)-(x-xc)**2*G)==0
r=s.Rational(64,625);ls=-s.Rational(256,3125)
assert 5*r**4+ls**3==0 and ls**4==4*r**5
assert s.expand(3*ls**2*r+4*ls**3)==-r*ls**2/5
with Path('audit_p18_independent_10/fresh_matrix_output.txt').open('a') as f:
 f.write('\nAll additional exact assertions passed: polarization, exterior quotient, dual basis, graph determinant and contraction, beta and chi asymptotics, explicit plumbing factorization, and cusp derivative.\n')
print('All additional exact assertions passed.')
