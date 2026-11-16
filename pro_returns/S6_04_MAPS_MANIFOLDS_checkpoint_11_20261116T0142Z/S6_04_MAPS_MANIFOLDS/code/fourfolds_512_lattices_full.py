"""Bounded full p-neighbor search, allowing nonprimitive intermediate cusps.

For p=2,3 the Phi5 factor is irreducible. Every A-stable subspace
is U or U plus the degree-four irreducible module, with U a subspace
of F_p^2. Thus each neighbor step is exhaustive. The global depth
bound is six for p=2 and four for p=3; no completeness beyond it
is claimed. All primitive-cusp endpoints are printed with matrices.
"""
from sympy import Matrix, eye, zeros, ZZ, ilcm, igcd
from sympy.matrices.normalforms import smith_normal_form, hermite_normal_form

A=Matrix([[1,0,0,0,0,0],[0,1,0,1,0,0],[0,1,0,0,0,0],
          [0,-1,0,0,1,1],[0,1,-1,0,-1,0],[0,0,1,0,0,0]])
B=Matrix([[1,0,0,0,1,0],[0,0,1,0,0,0],[0,0,0,0,0,1],
          [0,1,-2,0,0,0],[0,0,1,0,-1,-1],[0,0,0,1,1,2]])
def factors(T):
 D=smith_normal_form(T,domain=ZZ)
 return [abs(int(D[i,i])) for i in range(min(D.shape)) if D[i,i]]
def rr(T,p):
 a=[[int(x)%p for x in T.row(i)] for i in range(T.rows)];piv=[];r=0
 for c in range(T.cols):
  j=next((j for j in range(r,len(a)) if a[j][c]),None)
  if j is None:continue
  a[r],a[j]=a[j],a[r];u=pow(a[r][c],-1,p);a[r]=[(x*u)%p for x in a[r]]
  for k in range(len(a)):
   if k!=r:
    u=a[k][c];a[k]=[(x-u*y)%p for x,y in zip(a[k],a[r])]
  piv.append(c);r+=1
  if r==len(a):break
 return Matrix(a),piv
def rank(T,p):return len(rr(T,p)[1])
def basis(T,p):
 R,q=rr(T.T,p)
 return R[:len(q),:].T
def kernel(T,p):
 R,q=rr(T,p);vs=[]
 for i in range(T.cols):
  if i in q:continue
  v=zeros(T.cols,1);v[i]=1
  for j,c in enumerate(q):v[c]=(-R[j,i])%p
  vs.append(v)
 return Matrix.hstack(*vs) if vs else zeros(T.cols,0)
def normalize(Q):
 den=1
 for x in Q:den=ilcm(den,int(x.q))
 vals=[int(x*den) for x in Q];g=0
 for x in vals:g=igcd(g,x)
 return hermite_normal_form(Matrix(6,6,vals)/g)

for p,bound in [(2,6),(3,4)]:
 queue=[(eye(6),0)];seen=set();levels={};good=[];edges=0
 while queue:
  Q,depth=queue.pop(0);key=tuple(Q)
  if key in seen:continue
  seen.add(key);levels[depth]=levels.get(depth,0)+1
  C=Q.inv()*A*Q;D=Q.inv()*B*Q
  assert all(x.q==1 for x in C) and all(x.q==1 for x in D)
  sn=factors(C*D-eye(6))
  if sn==[1,1,1]:
   good.append(Q)
   print('primitive endpoint prime',p,'depth',depth,'basis',Q,
         'A',C,'B',D,'q1 coinvariant',factors(Matrix.hstack(C-eye(6),D-eye(6))))
  if depth==bound:continue
  F=kernel(C-eye(6),p);E=basis(C-eye(6),p)
  assert F.cols==2 and E.cols==4
  us=[zeros(6,0),F[:,1:2]]
  us += [basis(F[:,0:1]+k*F[:,1:2],p) for k in range(p)]
  us += [F]
  assert len(us)==p+3
  for U in us:
   for X in [zeros(6,0),E]:
    S=basis(Matrix.hstack(U,X),p);d=S.cols
    if d in (0,6):continue
    if rank(Matrix.hstack(S,D*S),p)!=d:continue
    H=hermite_normal_form(Matrix.hstack(p*eye(6),S))/p
    Q1=normalize(Q*H);edges+=1
    if tuple(Q1) not in seen:queue.append((Q1,depth+1))
 print('prime',p,'depth bound',bound,'vertices by depth',levels,
       'directed neighbor edges',edges,'primitive endpoints',len(good))
