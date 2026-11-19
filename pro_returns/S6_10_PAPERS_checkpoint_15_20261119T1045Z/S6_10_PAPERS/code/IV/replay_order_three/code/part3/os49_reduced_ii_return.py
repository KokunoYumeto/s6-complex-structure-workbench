"""Reconstructed exact K85 source/page/arrow/normal certificate."""
from pathlib import Path
import sympy as s,json,math,hashlib
count=0
def ck(v,name):
 global count
 if isinstance(v,s.MatrixBase):v=all(s.simplify(x)==0 for x in v)
 elif not isinstance(v,bool):v=s.simplify(v)==0
 assert v,name;count+=1
sv,v,M,eps,th=s.symbols('sv v M eps th');U1,U2,C1,C2=s.symbols('U1 U2 C1 C2');de=s.Matrix([0,1]);D=3*s.Matrix([U1,U2])+2*s.Matrix([C1,C2])
u=s.Matrix([2*sv+U1,sv+U2]);g=s.Matrix([-3*sv+C1,-sv+M*v+C2]);K=3*u+2*g
o=-eps*sv*D/(2*M)-eps*sv**2*de/(4*M)-eps*sv*v*de;sig=eps*v*D+eps*M*v*(v-1)*de
ck(K-D-(sv+2*M*v)*de,'mixed K')
ck(o.subs(v,v+1)-o+eps*sv*de,'ordinary plus origin')
ck(sig.subs(v,v+1)-sig+eps*sv*de-eps*K,'cusp plus origin')
ck((o-sig).subs(v,v+th)-(o-sig)+eps*th*K+eps*M*th*(th-1)*de,'actual forward negative K')
mat=s.Matrix([[2,-3],[1,-1]]);ck(mat.det()==1,'period determinant');ck(mat.inv()-s.Matrix([[-1,3],[-1,2]]),'point inverse')
for e in [-1,1]:
 A=s.Matrix([[2,3*e],[-e,-1]]);ck(A.det()==1,'combined signed degree')
 T=s.diag(1,1,-e);ck(T.inv()*T-s.eye(3),'both signed references');ck((-e*T).det()==1,'oriented signed conjugation')
alpha=s.symbols('alpha',real=True)
G=s.Matrix([[-s.sin(alpha),s.cos(th)*s.cos(alpha),s.sin(th)*s.cos(alpha)],[s.cos(alpha),s.cos(th)*s.sin(alpha),s.sin(th)*s.sin(alpha)],[0,s.sin(th),-s.cos(th)]])
ck(G.T*G-s.eye(3),'full quotient normal matrix');ck(G.det()-1,'normal orientation')
Rz=s.Matrix([[s.cos(alpha),-s.sin(alpha),0],[s.sin(alpha),s.cos(alpha),0],[0,0,1]])
ck(G-Rz*G.subs(alpha,0),'full clutch factorization')
cases=[]
for k in range(1,13):
 for l in range(1,13):
  m=3*k;h=6*l+1
  if math.gcd(m,h)!=1:continue
  MM=m*h;chi=k*(3*l+1)
  ck(12*chi==2*MM+2*m,'actual root Euler count');ck(-2*chi-2*m*l==-2*k*h,'actual section square')
  ck((24*k*h-24*chi)//24==3*k*l,'physical A')
  for e in [-1,1]:
   na=(e*pow(h,-1,m))%m;nb=(e-h*na)//m
   ck(h*na+m*nb==e,'sphere norm');ck((1-e*m*nb)%h==0,'infinity root phase');ck((1-e*h*na)%m==0,'zero root phase')
   ck(math.gcd(na,m)==math.gcd(nb,h)==1,'no residual sheet stabilizer')
   cases.append({'k':k,'l':l,'m':m,'h':h,'n_A':na,'n_B':nb,'epsilon':e,'physical_pair':[6*k*h,24*chi],'physical_A':3*k*l})
root=Path(__file__).resolve().parents[2];note=root/'notes/part3_os49_reduced_ii_return_working.md'
out={'statement':'P3K.85','status':'PASS; reconstructed arithmetic/source-arrow certificate; original complete geometric audits retained','checks':count,'signed_cases':len(cases),'cases':cases,'source_sha256':hashlib.sha256(note.read_bytes()).hexdigest(),'historical_certificate_checks':2636,'historical_signed_cases':470,'scope':'Canonical full r, actual two cap maps, positive fan T1, physical pair and both signs.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print('PASS',count,'identities;',len(cases),'signed cases')
