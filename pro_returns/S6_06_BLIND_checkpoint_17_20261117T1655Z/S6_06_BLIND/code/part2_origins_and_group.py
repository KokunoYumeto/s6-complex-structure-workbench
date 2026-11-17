"""Independent exact origin and affine-commutator verification."""
import sympy as S
s,v,mu,C,U,l0,l1,l2,m,n=S.symbols('s v mu C U l0 l1 l2 m n')
b=4*l1+3*l2;a=b-12*l0
delta=S.Matrix([0,1]);gamma=S.Matrix([6*mu,C-s-12*v]);H=b*s+U
zg=S.Matrix([6*s*mu,-s*(s+1)/2+s*(C-12*v)])
o=S.Matrix([-b*mu*s/2,b*s*s/24-b*C*s/12+l0*s/2+v*(b*s+U)])
sig=-l0*zg+S.Matrix([6*a*mu*v,v*U+a*C*v-6*a*v*v+6*a*v])
F0=S.Matrix([mu*(s+12*v)/2,C*(s+12*v)/12-(s+12*v)**2/24+6*v])
assert S.simplify(sig-o-a*F0)==S.zeros(2,1)
identities=[
 ('Q o',o.subs(s,s+12)-o,-b*gamma+6*(b+l0)*delta),
 ('R o',o.subs(v,v+1)-o,H*delta),
 ('Q sigma',sig.subs(s,s+12)-sig,-12*l0*gamma+78*l0*delta),
 ('R sigma',sig.subs(v,v+1)-sig,H*delta+a*gamma),
 ('Q^m F',(sig-o).subs(s,s+12*m)-(sig-o),a*m*gamma-6*a*m*m*delta),
 ('R^n F',(sig-o).subs(v,v+n)-(sig-o),a*n*gamma-6*a*n*(n-1)*delta),
]
for name,left,right in identities:
 assert S.simplify(left-right)==S.zeros(2,1)
 print(name,'=',S.simplify(right).T)
print('F=(4*l1+3*l2-12*l0)*F0 verified exactly.')

E32=S.zeros(4);E32[2,1]=1
E41=S.zeros(4);E41[3,0]=1
Nq=-12*m*E32+12*m*E41;Nr=12*n*E41
assert Nq*Nq==Nr*Nr==Nq*Nr==Nr*Nq==S.zeros(4)
al,be,al2,be2,g,u,w,d,g2,u2,w2,d2=S.symbols('alpha beta alpha2 beta2 g u w d g2 u2 w2 d2')
lam=S.Matrix([g,u,w,d]);lam2=S.Matrix([g2,u2,w2,d2])
comm=(al*Nq+be*Nr)*lam2-(al2*Nq+be2*Nr)*lam
print('Intersecting-meridian commutator:',comm.T)
assert S.expand(comm[3]-12*((m*al+n*be)*g2-(m*al2+n*be2)*g))==0
print('delta equation checked; positive ratio denominator m*alpha+n*beta.')

A1=S.Matrix([[1,0,0],[6,0,1],[-6,-1,-1]])
A2=S.Matrix([[1,0,0],[0,0,-1],[-6,1,0]])
N=S.zeros(3);N[2,1]=1
K=N.col_join(N*A1).col_join(N*A2)
print('finite-orbit obstruction matrix:',K.tolist())
print('kernel:',K.nullspace())
assert K.nullspace()==[]
print('nonzero constraint rows:',[list(K.row(i)) for i in range(K.rows) if any(K.row(i))])
print('member (0,2,-1):',{'a':a.subs({l0:0,l1:2,l2:-1}),'b':b.subs({l1:2,l2:-1})})
print('All identities exact; no geometric hypothesis is certified by this script.')
